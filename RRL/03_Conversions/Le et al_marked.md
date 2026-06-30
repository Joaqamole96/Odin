Review
Cybersecurity Analytics for the Enterprise Environment:
A Systematic Literature Review
TranDucLe1,* ,ThangLe-Dinh2 andSylvestreUwizeyemungu3
1 DepartmentofMathematics,Statistics&ComputerScience,UniversityofWisconsin-Stout,
Menomonie,WI54751,USA
2 DepartmentofMarketingandInformationSystems,UniversitéduQuébecàTrois-Rivières,
Trois-Rivières,QCG9A5H7,Canada;thang.ledinh@uqtr.ca
3 DepartmentofAccounting,UniversitéduQuébecàTrois-Rivières,Trois-Rivières,QCG9A5H7,Canada;
sylvestre.uwizeyemungu@uqtr.ca
* Correspondence:let@uwstout.edu
Abstract: Theescalatingscaleandsophisticationofcyberthreatscompelenterprisesto
urgently adopt data-driven security analytics. This systematic literature review, adher-
ing to the PRISMA protocol, rigorously synthesizes current knowledge by analyzing
65 peer-reviewed studies (2013–2023) from six major databases on enterprise-level cy-
bersecurity analytics. Our findings reveal a significant industry-wide transition from
traditionalsignature-basedtoolstowardsadvancedcloud-enabled,big-dataandartificial
intelligence-poweredtechniques,wheremachinelearningandgraph-basedmodelsare
increasinglyprominentinrecentworks. Whilelargeorganizationsinfinance,Information
andCommunicationTechnology,andcriticalutilitiesspearheadadoption,dedicatedre-
searchfocusingonsmallandmedium-sizedenterprises(SMEs)remainsnotablylimited.
Tenthematicobservationsencapsulatekeyadoptiondrivers,anevolvingpreferencefor
proactive and predictive security strategies, the critical role of heterogeneous log and
networkdata,andpersistentimplementationchallenges-notablydataintegration,skills
shortages, and cost. Furthermore, this review identifies crucial open research avenues,
includingthedevelopmentofreal-timescalableanalytics,unifiedpolicylanguages,and
critically needed SME-oriented solutions. Collectively, these insights provide a robust
evidencebasetoinformfutureresearchtrajectoriesandguidethepracticaldeploymentof
AcademicEditors: SeokjooShin
andDomenicoRosaci effectivecybersecurityanalyticsindiverseenterprisesettings.
Received:30April2025
Keywords:cybersecurityanalytics;PRISMA;enterprisesecurity;systematicliteraturereview
Revised:22May2025
Accepted:29May2025
Published:31May2025
Citation: Le,T.D.;Le-Dinh,T.;
1. Introduction
Uwizeyemungu,S.Cybersecurity
AnalyticsfortheEnterprise Intoday’squicklychangingdigitalworld,enterprisesconfrontanexpandingnumber
Environment:ASystematicLiterature
ofsecurityrisksandvulnerabilities[1]. Cyberattackshaveincreaseddramaticallydueto
Review.Electronics2025,14,2252.
theincreasinguseofnewtechnologiessuchascloudcomputing[2],mobiledevices[3],
https://doi.org/10.3390/
andtheInternetofThings(IoT)[4]. Thisleadstonewdifficultiesforenterprisesinpro-
electronics14112252
tectingtheirresourcesanddata. DistributedDenialofService(DDoS)attacks,phishing
Copyright:©2025bytheauthors.
attacks,malwareattacks,theftofsensitivedata,oreventhreatsfromwithinenterprises
LicenseeMDPI,Basel,Switzerland.
arethemostdangerousthreatstoenterprises[5]. Thesethreatscancausefinanciallosses,
Thisarticleisanopenaccessarticle
distributedunderthetermsand reputationaldamage,andlossofuserdata[6]. Companiesneedcomprehensivesecurity
conditionsoftheCreativeCommons solutionstomaintainstablecompanyoperations,ensurecustomertrust,andraisesecurity
Attribution(CCBY)license awareness[7].
(https://creativecommons.org/
licenses/by/4.0/).
Electronics2025,14,2252 https://doi.org/10.3390/electronics14112252

Electronics2025,14,2252 2of55
Traditionalsecuritytoolssuchasfirewalls[8],intrusiondetectionsystems[9],andanti-
virussoftwarehavebeenshowntobeineffectiveagainstpersistentandsophisticatedcyber-
attacks[10]. Toaccesssensitiveinformationwithoutpermission,adversariescontinueto
createnewtechniquesandmethods, exploitzero-dayvulnerabilities[11], andleverage
socialengineering[12]forunauthorizedaccesstosensitiveinformation. Cybersecurityana-
lytics[13,14]hasevolvedasasignificantcomponentinenterprisesecuritystrategyinorder
toreacttothesecomplexthreats. Consequently,theescalatingchallengeposedbysuch
advancedthreats,notablyAdvancedPersistentThreats(APTs)thatcircumventtraditional
security,underscoresthecriticalneedforacomprehensivereviewtoconsolidatecurrent
knowledgeontheefficacyandevolutionofcybersecurityanalyticsinenterprisedefense.
Usingsophisticateddataanalysistechniques[15], cybersecurityanalyticscanhelp
companiesidentify,assess,andrespondtopotentialthreatsmoreefficientlyandquickly[16].
Thissolutionidentifiesandmitigatespossiblehazardsbycollecting,processing,andana-
lyzingsecurity-relateddata[17,18].
Despitethegrowinginterestincybersecurityanalysismethodologies,aconspicuous
lackofclarityregardingtheirefficaciousapplicationwithintheenterprisecontextpersists.
Manybarrierssuchasencompassingbudgetarylimitations,adearthofrequisitetechnical
expertise, and persistent data privacy concerns contribute to the deployment process’s
complexities[19].Thereappearstobeanoticeablescarcityofmethodicalendeavorsthrough
whichtosynthesizeandconsolidateknowledgefromindividualstudiesdispersedacross
thedomain. Thiscircumstanceunderscoresaprominentknowledgegapandaccentuates
thenecessityofasystematicliteraturereview(SLR).AnSLRofthisnaturewouldfostera
holisticviewpointoncybersecurityanalyticswithintheenterprisemilieu,weavingtogether
disparatestrandsofknowledgetoproduceacomprehensive,unifiedunderstandingof
thefield.
Themotivationforconductingasystematicliteraturereviewoncybersecurityana-
lyticsforenterpriseenvironmentsisthreefold. First,itprovidescompleteandinsightful
informationontrendsandchangesthathaveoccurredindevelopingandimplementing
cybersecurityanalyticssolutionsinanenterprisecontext. Next,ithelpsbusinessestohave
moreinformationaboutthecutting-edgemethods,tools,frameworks,applications,andde-
ploymentstrategiesusedinthefield. Asaresult,itenablesthemtomakeinformedchoices
whenapplyingcybersecurityanalyticssolutions. Finally,thisreviewemphasizesthefield’s
significantchallengesandgapsandencouragesmoreresearchanddevelopmentactivities.
This review focuses on studies explicitly addressing cybersecurity analytics in the
enterprisecontextandonresearchthatcanbeextrapolatedtothiscontext.Itaimstoprovide
acompleteandup-to-datesynthesisofthesecurityanalysisliteratureforenterprisesto
informbothresearchersandpractitionersinthisfield.
2. DelvingintoSecurityAnalytics
Beforedelvingintosecurityanalytics,itisimportanttonotethat,withinthescope
of this research, the terminologies “cybersecurity analytics ” and “security analytics” are
employedsynonymouslytodenoteidenticalconcepts.Henceforth,forthesakeofsimplicity,
theterm“securityanalytics”willbepredominantlyemployed.
The cybersecurity landscape is in constant flux, dynamically evolving to meet the
new challenges of an increasingly digitized world. At the heart of this evolution is se-
curityanalytics, apotentblendofdata-driventechniquesandmethodologiesdesigned
to strengthen an organization’s cybersecurity structure [20]. It systematically involves
collectingsecurity-relateddatafromdiversesources, meticulouslyprocessingthisdata
toensurequalityandrelevance(e.g.,throughcleansing,normalization,andenrichment),
and then analyzing the refined data to identify patterns, trends, and anomalies. These

Electronics2025,14,2252 3of55
analyticaloutcomesindicatepotentialthreatsorvulnerabilitieswithinanorganization’s
informationsystems, therebyenablingbetter-informed, proactivedecisionmakingand
moreeffectiveriskmitigation[16–18,21].
Thissectionprovidesanoverviewofsecurityanalytics,includingitsprimarypurposes
andthetypicaldatalifecycleitinvolves,beforediscussingthekeychallengesassociated
withitsimplementationandthemotivationforthisreview.
PurposesofSecurityAnalytics
Securityanalyticsholdsthepotentialtoservemultiplepurposes[14,22],including
detectingintrusions(toidentifyanomalousactivitythatmayindicateanintrusion),inves-
tigatingincidents(todeterminetherootcauseandidentifytheattacker),respondingto
incidents(byprovidinginformationontheaffectedsystemsandusers),andpreventing
futureincidents(byidentifyingvulnerabilitiesandrecommendingmitigationmeasures).
TheSecurityAnalyticsDataLifecycle
Keyactivitiesandtechniquesintegraltotheefficacyandapplicationofsecurityana-
lyticsencompassvariousstagesfrominitialdatagatheringthroughprocessingtoeventual
analysis[15,23].Thislifecycleiscriticalinfortifyinganorganization’scybersecuritylandscape.
The process typically begins with data gathering from diverse sources, including
networktraffic,systemlogs,useractivityrecords,andexternalthreatintelligencefeeds.
Theaimistoachieveacomprehensiveviewoftheorganization’scybersecuritystateto
aidinaccuratethreatdetection. Subsequently,thisrawdataundergoesmeticulousdata
preprocessingtoensureitsqualityandrelevanceforanalysis. Commonpreprocessing
stepsincludedatacleansing(toremoveerrorsorinconsistencies),normalization(tobring
dataintoacommonformat),andenrichment(toaddcontextualinformation).
KeyChallengesinImplementation
Whilestrategicallyleveragingdatathroughanalyticscansignificantlybolsteranenter-
prise’scybersecuritypostureandthreatresponsecapabilities,itspracticalimplementation
isoftenfraughtwithchallenges[19]. Understandingthepracticalimpedimentsorgani-
zations encounter—whether technical, organizational, or financial—is instrumental for
advancingthefield. Furthermore,definingandaccessingthemostvaluabledatasources
andtypeswithinspecificenterprisecontextsremainsanessentialfacetrequiringongoing
explorationandresearch.
Researchmotivation
As we delve into security analytics, we aim to highlight its multiple applications,
unravel the technicalities of its deployment, and identify gaps in current research and
promisingopportunitiesforfutureexploration. Recognizingthatthejourneyofsecurity
analytics is far from linear, it is crucial to elucidate how its adoption and application
have transformed over time. As a multidimensional concept, it has permeated many
industries,sectors,anddomains—buttowhatextentandwherehasitsimpactbeenmost
profoundlyfelt?Moreover,itisparamountthatwecontinuetoevaluateandre-imaginehow
data-centricmethodologiescanbeharnessedmoreeffectively. Thus,wemustconstantly
re-evaluatethemodels,methods,andframeworksunderpinningsecurityanalytics.
3. ResearchMethodology
This study uses the widely recognized systematic review methodology known as
PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) [24],
whichhasbeenextensivelyutilizedinarangeofreputablejournalpublicationsforcon-
ducting systematic literature reviews [25–29]. This methodology follows a systematic
approach,encompassingfourmainphases,eachwithspecificactivitiesdesignedtoensure
acomprehensiveandtransparentreviewprocess: identification,screening,judgementof
eligibility,anddataextractionandsynthesis.

Electronics2025,14,2252 4of55
Thisstudy’sSLRformulatedresearchquestionsbasedontheidentifiedsecurityana-
lyticschallengesandtheunderlyingmotivation.
Theprimaryresearchquestionsofthisreviewareasfollows:
• RQ1: Howhastheadoptionofsecurityanalyticsinenterprisesevolvedovertime?
• RQ2: Inwhichindustries, fields, domains, orsectorsareenterprisesmostactively
adoptingandutilizingsecurityanalytics?
• RQ3: Whattechniques,methods,models,andframeworksareenterprisesemploying
toimplementandoptimizesecurityanalytics?
• RQ4: Whichdatasourcesanddatatypesareintegraltosecurityanalyticswithinan
enterprisecontext?
• RQ5: Whatarethebarriersfacedbyenterprisesinimplementingsecurityanalytics?
• RQ6: What are the research gaps and future research opportunities in enterprise
securityanalytics?
Figure1illustratestheinterrelationbetweenresearchquestionsandtheirrespective
correlationswiththeprimarytasksofcybersecurityanalyticswithintheenterprisecontext.
RQ1
(Trends & Adoption)
RQ5
(Barriers)
RQ2
(Enterprise Characteristics)
INPUT RQ3 OUTPUT Threat Identification
(Processing & Analysis) & Mitigation
RQ4
(Data Source & Type)
RQ6
(Research Gaps & Improvement)
Figure1. Relationshipbetweenresearchquestionsandcybersecurityanalyticstasksintheenter-
prisecontext.
AsmentionedinSection2,RQ1andRQ2arerelatedtothepurposesofcybersecurity
analytics. Thus,RQ3andRQ4areconcernedwithdataprocessing. Finally,RQ5dealswith
keychallenges,andRQ6isrelatedtotheresearch’smotivation. Aflowdiagrambasedon
PRISMAwithallthedetailedinformationandstatisticsisdepictedinFigure2.
In the following sections, we detail different literature review activities, including
identification,screening,eligibility,andbackwardandforwardsearches.
3.1. Identification
SearchStrategy
This study gathered research articles from the following digital databases: IEEE
Xplore,Scopus,WebofScience,ScienceDirect,ACMDigitalLibrary,andProquest. Thechoice
of the database took into account its scope and relevance in academia. IEEE Xplore is
theleadingacademicdatabaseinengineeringandcomputerscience(https://paperpile.
com/g/academic-research-databases/(accessedon29April2025)). Scopusisanonline
abstractandindexingserviceprovidedthroughElsevier. WebofScience,ScienceDirect,ACM
DigitalLibrary,andProquestarewell-knowndatabasesprovidingaccesstoawiderange
ofacademicliterature. Researcherscommonlyusethesedatabasesbecausetheyprovide
accesstohigh-quality,peer-reviewedarticlesandotheracademicresources.

Electronics2025,14,2252
5of55
| IEEE Xplore | 401 |     |
| ----------- | --- | --- |
etacilpuD & ytirupmI
| NOITACIFITNEDI Scopus | 622 |     |
| --------------------- | --- | --- |
hcraeS laitinI
lavomeR Total Records
| Web of Science      | 263 N = 648 | Remaining |
| ------------------- | ----------- | --------- |
| ScienceDirect       | 55          | N = 843   |
| ACM Digital Library | 31          |           |
| Proquest            | 119         |           |
| Total               | 1491        |           |
Title & Abstract
First phase of
Screening with
| GNINEERCS assessment | Assessment   |               |
| -------------------- | ------------ | ------------- |
|                      | Question QA1 | Total Records |
| Inclusion/Exclusion  |              | Remaining     |
Criteria
N = 151
Title & Abstract
| Checked Records | Screening |     |
| --------------- | --------- | --- |
N = 843
with Assessment
Question QA2
| YTILIBIGILE Second phase of |     | Total Records |
| --------------------------- | --- | ------------- |
assessment
|     | Full Text Screening with N = 91 | Remaining |
| --- | ------------------------------- | --------- |
Assessment Question
| Checked Records  |  QA2             |                |
| ---------------- | ---------------- | -------------- |
| N = 151          |                  | N = 60         |
| DEDULCNI         |                  | Total Selected |
| Selected Studies | Backward &       |                |
| for Reviewing    | Forward Searches | Studies        |
| N = 60           | N = 5            | N = 65         |
Figure2.PRISMA-2020flowdiagramindicatingastep-by-stepprocessofidentifyingandselecting
thestudies.
Atripartitegroupingofkeywordswasemployedinthetitles,keywords,orabstractsof
potentialarticlestoensurecomprehensiveandsystematicinclusionofpertinentliterature
in this review. This grouping directly aligns with this study’s main research questions
andaims. Thefirstgroupofkeywordsfocusedonthecorethemeofthereview—security
analytics. It included the following terms: (“cybersecurity analytic*” OR “cybersecurity
analysis”OR“securityanalytic*”OR“securityanalysis”). Thesetermsreflecttheinvestigation
ofRQ1,RQ2,andRQ6,whichexploretheevolution,industry-specificadoption,andfuture
researchavenuesinenterprisesecurityanalytics,respectively.
Thesecondgroupaimedtocapturethevariouswaysthatsecurityanalyticsisimple-
mentedandoptimizedinenterprises. Therefore,thesecondgroupincluded(“technique*”
OR“platform*”OR“framework*”OR“method*”OR“model*”OR“approach*”OR“data*”).
ThesetermsresonatewithRQ3andRQ4,investigatingthespecifictechniques,methods,
models,andframeworksemployedinsecurityanalytics,aswellasthedatasourcesand
typesintegraltothisdomain.
Thethirdgroupwasdesignedtoensurethattheliteratureselectedwasrelevanttothe
enterprisecontext. Itincluded(“enterprise*”OR“firm*”OR“compan*”OR“business*”). This
grouphelpedtodelveintoRQ5andRQ6,addressingthebarriersfacedbyenterprisesin
implementingsecurityanalytics. Italsotiedinwithourresearchaimtoidentifytheimpact
andapplicationsofsecurityanalyticsacrossdifferentsectors.
Table1presentsthesearchresults. Itisimportanttonotethatthesearchresultswere
constrained by the time at which this study was conducted. In total, 1491 potentially
relevantpublicationswereidentified.

Electronics2025,14,2252 6of55
Table1.Searchresultsfrommajordatabases.
Database ID Total
ACMDigitalLibrary DB01 31
IEEEXplore DB02 401
Proquest DB03 119
ScienceDirect DB04 55
Scopus DB05 622
WebofScience DB06 263
Total 1491
StudySelection
In order to identify relevant studies within the scope of the research field under
consideration,specificcriteriaforinclusionandexclusionwereestablished.
• InclusionCriteriaincluded
– InC01. Studiespublishedinthelasttenyears,between2013and2023;
– InC02. Studiespublishedinconferencesandjournals;
– InC03. StudiesthatarewritteninEnglish.
• ExclusionCriteriaincluded
– ExC01. Studiespublishedbefore2013;
– ExC02. Studiesthatarepublishedinnon-peer-reviewedsources;
– ExC03. StudiesthatarenotwritteninEnglish;
– ExC04. Studiespublishedinpreprintplatforms;
– ExC05. Studiesforwhichthefulltextisnotavailable;
– ExC06. Studiesinwhichnoneofthephrasesfromtheabovesearchinggroups
wereincludedinthetitleorabstract;
– ExC07. Studiesthatareasurveyorareview.
Theselectionofthe2013–2023publicationwindow(InC01)wasdeliberate,aimingto
capturethemostrelevantdecadereflectingthematurationandwidespreadadoptionofkey
technologiesthatfundamentallyreshapedenterprisesecurityanalytics. Thisperiodencom-
passesthesignificantriseofBigDataanalytics,theincreasedmigrationofenterprisesto
cloudcomputingenvironmentsfacilitatinglarge-scaledataprocessing,andthenotableshift
towardsemployingmachinelearningandartificialintelligencetechniques,asidentified
byourfindings(seeSection4.1,Ob2). Focusingonthistimeframeensuresthatthereview
concentratesoncontemporaryapproachesandchallengespertinenttothecurrentstateof
theartinarapidlyevolvingfield,excludingearlierfoundationalworkthatmayrelyon
significantlydifferenttechnologicalunderpinnings. Furthermore,oursearchconcluded
with publications up to the end of December 2023. While the manuscript preparation
andreviewprocessextendedinto2025,thisdefinedcutoffdateisnecessarytoensurea
consistentandreplicabledatasetforanalysis. Additionally,delaysindatabaseindexing
mean that the most recent publications (from 2024 and early 2025) may not have been
fullyavailableorindexedatthetimethesystematicsearchandscreeningwerefinalized,
ensuringthatthe2013–2023windowrepresentsthemostcomprehensivedatasetachievable
atthepointofanalysiscommencement.
It should be noted that during the search process (as shown in Table 1), specific
inclusionandexclusioncriteriawereincorporatedtoreducethenumberofpublications
requiringscrutiny. Nonetheless,thesecriteriawerestillmanuallyemployedtoscreenand
eliminatestudiesthatdidnotmeettherequirements,giventhatspecificdatabaseslacked
sufficientfiltersforsearching.

Electronics2025,14,2252 7of55
AllselectedresearcharticlesweresavedinEndNoteversion21.5 (https://endnote.
com/(accessedon29April2025)),apieceofreferencemanagementsoftwareforschol-
arlypublications.
RemovalofDuplicateRecords
In this step, we employed the “Find Duplicates” function in EndNote to eliminate
duplicatedrecords,resultingin1150remainingrecords. However,duetovariationsinthe
informationfieldsofpapersfromdifferentdatabasesources,EndNotemightmisssome
duplicatepapers. Toensuretheuniquenessofeachrecord,weconductedamanualdouble-
check. Furthermore,recordsrepresentinggeneralcontent,tableofcontents,orcoverpages
ofconferenceswerealsoremoved. Aftercompletingthisstep,theremainingnumberof
recordswas843. Lastly, the“FindReferenceUpdates”featureinEndNotewasutilizedto
guaranteetheinclusionofthefinalversionsofallrecords.
3.2. StudySelectionProcess
Thestudyselectionprocesswasconductedinmultiplestages,adheringtothePRISMA
guidelines[24],andinvolvedscreening,eligibilityassessment,andsupplementarysearches.
Thisprocessaimedtoidentifyallpeer-reviewedstudiesdirectlyrelevanttocybersecurity
analyticsinenterpriseenvironmentspublishedbetween2013and2023. Theentirestudy
selectionprocedure,fromtheinitialscreeningoftitlesandabstractsthroughtothefull-text
reviewforfinalinclusion,wasconductedbyateamofthreeresearchers. Toensureconsis-
tencyintheapplicationofselectioncriteriaandtoresolveanyambiguitiesencountered
during the evaluation of papers, a consensus-based approach was employed. In cases
whereconsensuscouldnotbereachedthroughdiscussion,thefirstauthormadethefinal
determinationforinclusionorexclusion.
3.2.1. ScreeningStage(TitleandAbstractReview)
After the initial database search yielded 1491 potentially relevant publications (as
detailedinTable1), aninitialscreeningbasedontitlesandabstractswasperformedto
remove studies that were clearly irrelevant. This crucial step helped to narrow down
thecorpustoamoremanageablesetforfull-textassessment. Duringthisstage,twokey
relevanceassessmentquestions,derivedfromourresearchscope,wereapplied:
• RelevanceQuestion1(RQ1 ): Doesthetitleorabstractcontainkeywordsfrom
screen
bothourfirstsearchgroup(cybersecurity/securityanalyticsterms)ANDourthird
searchgroup(enterprisecontextterms)?
• RelevanceQuestion2(RQ2 ): Doesthetitleorabstractindicatethatthestudy’s
screen
primaryfocusisonsecurityanalyticsspecificallyforanenterprise,organizational,
orbusinesscontext?
StudieshadtosatisfybothRQ1 andRQ2 ,alongsidethegeneralinclusion
screen screen
criteria(e.g.,language,year),toproceed. Thisscreeningprocessresultedintheexclusion
of692records. Consequently,151recordsremainedforfull-texteligibilityassessment.
3.2.2. EligibilityStage(Full-TextReview)
Inthisphase, thefulltextsofthe151remainingstudieswerethoroughlyassessed.
Theprimaryaimwastoconfirmtheirdirectrelevancetothereview’sresearchquestionsand
ensuretheymetallpredefinedinclusioncriteria. Thekeyrelevanceassessmentquestion
appliedherewasasfollows:
• RelevanceQuestion3(RQ3 ): Basedonthefulltext,doesthestudysubstan-
full-text
tively address security analytics within an enterprise context, providing insights
relevant to our research questions (e.g., regarding techniques, frameworks, data,
challenges,orfuturedirections)?

Electronics2025,14,2252 8of55
Each study was evaluated against RQ3 and the complete set of inclu-
full-text
sion/exclusioncriteria. Thisdetailedreviewensuredthatonlythemostrelevantstudies
wereincluded. Followingthisrigorousassessment,91recordswereexcluded,primarily
duetoalackofdirectrelevancetotheenterprisesecurityanalyticscontextuponfull-text
revieworinsufficientdetailpertinenttoourresearchquestions. Thisresultedin60studies
proceedingtodataextraction(theflowofstudiesisillustratedinthePRISMAdiagramin
Figure2). Theseselectedstudiesaredenotedbythesymbol“S”(e.g.,S1,S2,S3).
3.2.3. BackwardandForwardSearches(Snowballing)
Tofurtherensurecomprehensivecoverageandmitigatetheriskofmissingrelevant
publications,asnowballingtechnique,encompassingbothbackward(examiningreference
listsofincludedstudies)andforward(identifyingstudiesthatcitedtheincludedstudies)
searches [30], was conducted on the 60 studies identified. Any new studies retrieved
throughthismethodunderwentthesamerigorousscreening,eligibility,andqualityap-
praisal process described above. Through this snowballing process, an additional five
relevantstudieswereidentifiedandincluded. Thesestudiesaredenotedbythesymbol
“A”(e.g.,A1,A2,A3,A4,A5).
3.2.4. QualityAppraisal
Theprimaryobjectiveofthissystematicliteraturereviewwastocomprehensivelymap
theexistingresearchlandscape,identifyingkeythemes,prevalentchallenges,andfuture
research directions in enterprise security analytics. Accordingly, our quality appraisal
processwasdesignedtoensuretherelevance,clarity,andutilityoftheincludedstudies
forachievingthesemappingobjectives. Allselectedstudieswerepeer-reviewedjournal
articlesorfullconferencepapers,whichprovidedaninherentbaselineofacademicrigor.
Duringthefull-texteligibilityassessment,beyondconfirmingdirecttopicalrelevance
toourresearchquestions(asperRQ3 ),ourteamactivelyassessedeachstudybased
full-text
onthefollowingconsiderations:
• Clarity of Contribution: the extent to which the study’s objectives, methodology,
andfindingswereclearlypresentedandunderstandable.
• SufficiencyofDetail: whetherthestudyprovidedadequatedetailtoallowforthe
extractionofrelevantdatapertainingtoourreview’sspecificresearchquestions(e.g.,
ontechniques,frameworks,datasources,andchallenges).
• DirectContributiontoReviewObjectives: thedegreetowhichthestudymadea
discernibleandsubstantivecontributiontotheunderstandingofenterprisesecurity
analyticsinlinewiththeaimsofthisreview.
Studies that were found to be significantly lacking in clarity, provided insufficient
detail for meaningful data extraction, or did not offer a discernible contribution to the
specificfocusareasofthisreviewwereexcludedduringtheeligibilityphase.
Whileaformalcriticalappraisaloftheintrinsicmethodologicalsoundnessofeach
primary study using a standardized checklist (e.g., CASP, AMSTAR) for scoring or as
anindependentexclusioncriterionwasnotperformed,ourmulti-facetedeligibilityand
appraisal process ensured that the final set of 65 studies was robust, relevant, and of
sufficient quality to address the comprehensive mapping objectives of this systematic
literaturereview.
3.3. CharacteristicsofIncludedStudies
Of 65 selected studies, 48 were from conferences, and 17 were from journals (see
TableA1). Thethreeyearswhenthemoststudieshadbeenpublishedwere2015, 2016,
and2020. Figure3showsthenumberofstudiespublishedandtheirtypesbyyear.

Electronics2025,14,2252 9of55
Despite fluctuations and a recent decrease in published studies from 2013 to 2023
insecurityanalyticswithinanenterprisecontext,thisshouldnotbeseenasdiminishing
interest. Instead, thefieldistransitioningfrom“burgeoning”to“emerging”. Thedrop
in studies may reflect the field’s complexities, necessitating deeper research and poten-
tially longer publication times. Concurrently, this field remains promising and shows
vastunexploredpotential,asindicatedbygapsinareaslikemethodologicalapproaches,
datasourceintegration,visualization,real-timeanalysis,andscalabilityandperformance.
Therecentdecreasemaysuggestashiftinresearchfocustowardsthesecomprehensive
studies,affirmingtherelevanceandimportanceofongoingresearchinthisdomain.
10
8
7
6
5
5 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
0
0
2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
tnuoC
Conference Journal
Figure 3. Annual distribution and type of 65 primary studies on enterprise security analytics
(2013–2023). The trend indicates initial growth followed by fluctuations and a recent decrease,
possiblyreflectingashiftinresearchfocustowardsmorecomplexstudiesinanemergingfield.
4. ResultsandAnalysis
This section presents the findings and interpretation of results derived from the
systematic literature review (see the Supplementary Materials), structured around the
six research questions proposed earlier to delineate the current state of cybersecurity
analytics in enterprise environments. The analysis aims to provide a comprehensive
understandingofprevailingtrends,adoptedmethodologies,andpersistentchallenges.
4.1. TheAdoptionandEvolutionofSecurityAnalyticsinEnterprises(RQ1)
Thissubsectionaddressesthefirstresearchquestion(RQ1)byexaminingtheadop-
tiontrajectoryofsecurityanalyticswithinenterprises. Ithighlightskeyevolutionary
patterns and identifies the primary catalysts shaping its current landscape. Our sys-
tematicreviewof65studies(2013–2023)revealedthatenterpriseadoptionofsecurity
analytics is not merely a trend but a strategic response to a confluence of evolving
pressuresandtechnologicaladvancements.
Observation1(Ob1):MultifacetedDriversNecessitateAdvancedSecurityAnalytics
Theimpetusforenterprisestoadoptandadvancetheirsecurityanalyticscapabilities
isdrivenbyacomplexinterplayoffactors. Thesearenotisolatedpressuresbutintercon-
nectedelementsspanningthethreatlandscape,businessoperationaldemands,andthe
pervasiveinfluenceofdata-intensivetechnologies. Understandingthesedriversiscrucial
forcontextualizingtheshifttowardsmoresophisticatedanalyticalapproaches.
Ob1.1TheEvolvingLandscapeofThreatsandtheLimitationsofTraditionalDefenses
Aprimarydriveridentifiedacrossnumerousstudiesistheescalatingsophistication,
volume,andpersistenceofcyberthreats,whichincreasinglyrendertraditional,signature-
basedsecuritymeasuresinadequate.

Electronics2025,14,2252 10of55
• ElaborationandEvidence: Enterprisesareconfrontedwithanincreasinglydynamic
threatenvironment,characterizedbytheevolvingbehaviorsofmaliciousactors[31]
andthediverseimpactsofvaryingattackvectors[32]. Asignificantacceleratorinthis
contextisthedocumentedsurgeinAPTs,whicharedesignedtobypassconventional
defenses [33]. Compounding this, traditional security methodologies often fail to
adequatelytranslatehigh-levelsecurityneedsintoconcrete,implementablesecurity
requirements[34]. Furthermore,arecurrentthemeisthatexistingsecuritysolutions
arefrequentlynotdesignedholistically,leadingtofragmenteddefenses[35]. Thein-
herentcomplexityandcontinuouschangeabilityofmodernbusinessprocessesfurther
exacerbatethesevulnerabilities[36].
• Analysis: Thefailureoflegacysystemstocounteradvancedthreatseffectivelycreates
significant security gaps, exposing organizations to severe financial, operational,
andreputationaldamage. Thisnecessitatesafundamentalshiftfrompurelyreactive
defenseposturestostrategiesemphasizingproactivethreatanticipationandpredictive
analytics. The core implication is the urgent need for security analytics solutions
capableofdiscerningcomplexattackpatterns,identifyingsubtleanomaliesindicative
ofcompromise[37],andadaptingdynamicallytonewadversarialtechniques. This
alsocallsforproactivebreachdetectionmechanisms[38].
• Trends and Challenges: This driver directly fuels the industry-wide transition to-
wards AI-powered techniques, particularly machine learning and deep learning,
foradvancedthreatdetection,behavioralanalysis,andpredictivesecurity. Keytech-
nologicaltrendsrespondingtothisincludethedevelopmentofsophisticatedSecurity
Information and Event Management (SIEM) systems, Endpoint Detection and Re-
sponse(EDR),andNetworkDetectionandResponse(NDR)solutionsthatleverage
theseanalyticalcapabilities[39]. However,asignificantchallengeliesindeveloping
and maintaining analytics models that can keep pace with the rapid evolution of
adversarialTactics,Techniques,andProcedures(TTPs)andthesheervolumeofthreat
intelligence[40].
Ob1.2BusinessImperatives: Efficiency,Cost-Effectiveness,andStrategicSecurityAlignment
Beyondthepressuresofdirectthreats,theadoptionofsecurityanalyticsisstrongly
influencedbyfundamentalbusinessimperatives, includingthedemandforgreaterop-
erationalefficiency,cost-effectiveness,andthestrategicalignmentofcybersecuritywith
broadercorporateobjectives.
• ElaborationandEvidence: Aconsistentthemeintheliteratureistheorganizational
needforsecurityapproachesthatofferhighperformanceandenhancedefficiency[41].
Thisisoftenchampionedbydecisionmakerswhoaretaskedwithintegratingsecurity
analyticsintotheoverarchingbusinessstrategy[42],aprocessthatinherentlyinvolves
navigatingthechallengeofbalancingrobustsecuritymeasureswithbudgetarycon-
straints[43]. Thedynamicnatureofbusinessoperationsalsodemandsmoreagileand
responsivesecurityframeworks[36].
• Analysis: Inthecontemporaryenterprise,cybersecurityisincreasinglyviewednot
merelyasanIToverheadbutasacriticalenablerofbusinesscontinuity,trust,andin-
novation. Inefficientoroverlycostlysecuritymeasurescandrainresources,impede
agility,andultimatelyhindercompetitiveadvantage.Thecoreimplicationisademand
forsecurityanalyticsthatnotonlyimprovethreatdetectionandresponsetimesbut
alsooptimizesecurityoperations,automateroutinetasks,andprovideclearmetrics
todemonstratevalueandinformstrategicinvestmentdecisions.
• Trends and Challenges: These business drivers are accelerating the adoption of
Security Orchestration, Automation, and Response (SOAR) platforms, which aim
tostreamlinesecurityworkflowsbyintegratinganalyticswithautomatedresponse

Electronics2025,14,2252 11of55
actions[44]. Thepursuitofefficiencyalsoencouragestheuseofcloud-nativesecurity
analyticsplatformsthatofferscalabilityandpotentiallylowertotalcostofownership.
Challengesinthisdomainincludeeffectivelyquantifyingthereturnoninvestment
(ROI)forsecurityanalytics,ensuringthatautomatedresponsesdonotinadvertently
disruptbusinessprocesses,andseamlesslyintegratingsecurityanalyticsintodiverse
andoftensiloedenterpriseITenvironments[13].
Ob1.3ProliferationofBigDataandtheRiseofAdvancedAnalyticalTechniques
Theexplosionindatavolume,velocity,andvarietywithinenterpriseenvironments,
coupledwiththematurationofmachinelearningandotheradvancedanalyticaltechniques,
constitutesathirdmajordriverfortheadoptionofspecializedsecurityanalytics.
• Elaboration and Evidence: Enterprises today must contend with analyzing vast
volumesofoftenunstructuredorsemi-structureddata,suchastextlogsfrommyriad
systems[45],andnavigatetheinherentsecurityrisksassociatedwithmanagingthese
large-scaleBigDataenvironments[46]. Acommonoperationalpainpointisthehigh
numberoffalsepositivealertsgeneratedbysimplertoolsandtheextensiveanalysis
times required when dealing with heterogeneous data sources [47]. Concurrently,
withthegrowingrelianceonmachinelearning(ML)forvariousbusinessfunctions,
there is a corresponding need for robust security analyses specifically tailored for,
andsometimesappliedto,theseMLsystemsthemselves[48].
• Analysis: Themerecollectionandstorageofmassivedatasetsprovidelittlesecurity
value without the ability to extract timely, actionable intelligence. The inability to
effectivelyprocessandanalyzethis“datadeluge”canleadtomissedcriticalalerts,
delayedincidentresponse,andsignificantanalystfatigue. Thisunderscoresacritical
demand for advanced data-processing architectures, scalable analytical platforms,
andtheapplicationofsophisticatedmodels(includingMLanddeeplearning(DL))ca-
pableofuncoveringhiddenpatternsandanomalieswithincomplexdatasets. Thegoal
istotransformrawsecuritydataintostrategicinsights.
• TrendsandChallenges: Thisdirectlyunderpinsthewidespreadmovetowardsdedi-
catedBigDatasecurityanalyticsplatforms,oftenleveragingcloudinfrastructurefor
itsscalabilityandprocessingpower. TheapplicationofML/AIforUserandEntityBe-
haviorAnalytics(UEBA),advancedthreathunting,andfrauddetectionareprominent
examplesofthistrend. However,significantchallengespersist,includingensuring
dataqualityandconsistencyfromdiversesources,the“black-box”natureofsomeML
models(drivingresearchintoExplainableAIforsecurity),thepersistentshortageof
cybersecurityprofessionalswithdatascienceskills,andtheneedtomakecomplex
analyticsoutputsmoreaccessibleanduser-friendly, potentiallythroughadvanced
visualtools[49].
Inessence,theseinterconnecteddrivingfactors—spanningtheevolvingthreatland-
scape, corebusinessrequirements, andthetransformativeimpactofBigDataandAI—
collectivelycompelenterprisestocontinuouslyenhancetheirsecurityanalyticscapabilities.
Thisunderstandingformsthebasisforexploringhoworganizationsareoperationalizing
theseanalytics,thespecifictechniquesbeingemployed,andthechallengestheyencounter,
whichwillbedetailedinsubsequentsections.
Observation2(Ob2): AProgressiveTechnologicalShiftTowardsData-Drivenand
IntelligentSecurityAnalytics
Theevolutionofsecurityanalyticswithinenterprisesettingsisintrinsicallylinked
toandpropelledbysignificanttechnologicaladvancements. Ourreviewindicatesaclear
trajectoryawayfromtraditional,oftenmanual,securitymeasurestowardsmoreautomated,
data-intensive,andintelligentanalyticalcapabilities. Thistechnologicalshiftisnotmerely
aboutadoptingnewtoolsbutreflectsafundamentalchangeinhoworganizationsapproach

Electronics2025,14,2252 12of55
threat detection, response, and overall cyber risk management. Many selected studies
highlight the strategic utilization of cutting-edge technologies such as Big Data, cloud
computing,andartificialintelligence(AI)—includingitssubfieldsMLandDL—toenhance
securityanalyticscapabilities[50,51].Theprominenceofthesetechnologiesinthereviewed
literatureisillustratedinFigure4.
Notmentioned
38%
Machinelearning
Deeplearning&AI
22% BigData
1%
Cloudcomputing
4%
Web
Mobile
11%
8%
16%
Figure4. Distributionofprimarytechnologiescitedinthereviewedenterprisesecurityanalytics
literature(N=65studies). Thechartunderscoresthefoundationalroleofmachinelearning,Big
Data,andcloudcomputing,whilealsonotingasignificantportionofstudiesthatdidnotfocusona
specificunderlyingtechnology.Somestudiesincorporatemultipletechnologies.
As Figure 4 demonstrates, machine learning (22 studies), Big Data (16 studies),
and cloud computing (11 studies) are the most frequently cited technologies, forming
thecoreofmodernenterprisesecurityanalytics.The“Notmentioned”category(38studies)
suggests that a substantial number of studies might focus on higher-level frameworks,
threattypes,ororganizationalaspectsratherthanspecifictechnologicalimplementations,
or that the technology is implied (e.g., general “security analysis”). Research focusing
on mobile platforms within enterprise security analytics [47,52] appears less prevalent
(with1studyexplicitlytagged),thoughmobilesecuritydatacouldbeingestedbybroader
systems. Thefollowingdiscussionexplorestheevolutionandinterplayofthesekeytech-
nologies,highlightingtheirimpactonsecurityanalyticspractices.
Ob2.1FoundationalLayers: CloudComputingandBigDataEcosystems
The initial significant shift observed is the adoption of cloud computing and Big
Datatechnologies,whichtogetherprovidethescalableinfrastructureanddata-processing
capabilitiesessentialforadvancedsecurityanalytics.
• ElaborationandEvidence(CloudComputing): Themigrationtocloudcomputing
forsecurityanalyticsreflectsbroaderenterpriseadoptiondrivenbythepursuitof
operationalefficiency,scalability,andperceivedcost-effectiveness[46,52–59]. Asor-
ganizationsincreasinglyentrusttheirdataandapplicationstocloudenvironments,
significant practical concerns regarding the comprehensive protection of sensitive
assetsagainstsophisticatedexternalandinternalthreatsemerge[53]. Theseconcerns,
suchasensuringdataprivacyandmeetingcomplexcompliancemandatesinshared
infrastructures,understandablyleadsomeclientstohesitateinrelocatingtheirmost
sensitivedatatothecloud[53]. Thisevolvinglandscapehasspurredsignificantinter-
estinleveragingdedicatedcloud-nativesecurityanalyticstodetectcomplexattacks
withinvirtualizedandcontainerizedinfrastructures[56].Moderncloud-basedsecurity
analyticssolutionsofferthetechnicalabilitytoingestandanalyzevastdatavolumes
fromdiverse,distributedsources—includingnetworklogs,endpointdata,andcloud
applicationtelemetry—ofteninnearrealtimetosupportrapidthreatdetectionand
response[38,60].

Electronics2025,14,2252 13of55
• ElaborationandEvidence(BigData):Concurrentwith,andoftenunderpinningcloud
adoption,thestrategicfocusinsecurityanalyticshasdecisivelybroadenedfromrudi-
mentarydatastoragetotheadvancedprocessingandcontextualanalysisof“BigData”.
Thispracticallyentailsmanagingandderivingactionableintelligencefromtheescalat-
ingvolume,velocity,andvarietyofsecurity-relevantdatastreams[37,46,56,57,60–68].
EnterprisesnowrecognizethatrobustBigDatacapabilitiesarenotmerelyadvanta-
geousbutpracticallyindispensableforidentifyingsubtleattackpatterns,anomalous
behaviors,andcomplexcorrelationsacrossheterogeneousdatasetsthatmayindicate
sophisticatedsecuritybreachesorongoing,low-and-slowattacks[37].
• Analysis: Cloudcomputingprovidestheelastic,dynamicallyscalable,andpotentially
cost-effectiveinfrastructuralbackboneessentialforresource-intensivesecurityana-
lyticsoperations. Simultaneously,BigDatatechnologiesfurnishthecriticaltoolsand
platformstoingest, efficientlystore, andprocessthemassiveanddiversedatasets
required for achieving comprehensive threat visibility and enabling deep forensic
capabilities. Their synergy facilitates a crucial shift from traditionally siloed, of-
tencapacity-constrained,on-premisessecuritymonitoringparadigmstowardsmore
centralized,scalable,andpotentiallymoreeffectiveenterprise-wideanalytics. The
foremostpracticalimplicationistheenhancedabilitytoperformsignificantlydeeper,
broader,andmorecontext-awareanalysesthanpreviouslyfeasible,therebylaying
thecriticalgroundworkformoreintelligentandproactivesecurityoperations. How-
ever,realizingthispotentialpracticallyrequiressignificantupfrontplanningfordata
governance,security,andcostmanagement,alongsidethedevelopmentofnewskill
setswithinsecurityteamstomanageandleveragethesecomplex,distributedenviron-
ments. Thetransitionalsointroduceslimitationssuchasincreaseddependencyon
providerinfrastructureandthepotentialfornewattacksurfacesspecifictocloudand
BigDataplatformsifnotadequatelysecured.
• TrendsandChallenges: ThisfoundationallayerofcloudandBigDatainfrastructure
supportsthedeploymentofadvancedSIEMsystems, thecreationofsecuritydata
lakesforflexibleanalytics,andtheadoptionofcloud-nativesecuritymonitoringand
responsetools. However,itsreal-worldapplicationisfraughtwithpersistentpractical
challengesandlimitationsthatenterprisesmustnavigate.
– DataSecurity,Sovereignty,andCompliance: Managingdatasecurityanden-
suringsovereigntyinmulti-cloudorhybridenvironmentspresentssignificant
operational complexity, particularly for global enterprises facing differing re-
gionaldataprotectionregulations(e.g.,GDPR,CCPA)[53]. Ensuringcompliance
whendatatraversesmultiplejurisdictionsorismanagedbythird-partyproviders
requiresrobustcontractualagreementsandcontinuousauditing,whichcanbe
resource-intensive.
– Data Quality, Integration, and Interoperability: Ensuring high data quality
and achieving seamless interoperability among diverse security data sources
(e.g.,legacysystems,modernIoTdevices,andcloudservices)remainsamajor
hurdle[37]. Poordataqualitycanleadtoinaccurateanalyticsandanincreasein
falsepositives,diminishingtrustinthesystem. Thelackofstandardizeddata
formats(anissueaddressedbyinitiativeslikeSysFlow)oftennecessitatescomplex
andcostlydataintegrationefforts,divertingresourcesfromactualanalysis.
– Cost Management and Control: While the cloud can offer cost-effectiveness,
enterprisesfacechallengesincontrollingescalatingdatastoragevolumes,pro-
cessingworkloads,and,inparticular,networkegressfees. Thespecializednature
ofmanyadvancedanalyticstoolsandplatformsalsoaddstolicensingandopera-
tionalcosts,requiringcarefulfinancialplanningandjustificationofROI.

Electronics2025,14,2252 14of55
– SpecializedSkillsGap: Acriticalpracticallimitationisthepervasiveshortage
ofpersonnelpossessingtherequisiteblendofskillsincybersecurity,cloudengi-
neering,BigDataanalytics,anddatascienceneededtodesign,deploy,manage,
andinterprettheoutputsofthesecomplexecosystemseffectively[56]. Thisskills
gapcansignificantlydelayadoptionorlimittheutilityofimplementedsolutions.
– ActionableInsightsfromData: Whiletheinfrastructurefacilitatesthecollection
andprocessingofvastdata,includingweb-basedsources[63,69],akeychallenge
liesintransformingthisdataintogenuinelyactionableinsightsforsecurityteams.
Advancedvisualizationanduser-centereddesignofanalyticsinterfaces[49,53]
arecrucialforenablinganalyststoeffectivelyexploredata, understandalerts,
and make timely decisions, but developing such interfaces requires specific
expertiseanditerativerefinement.
Ob2.2TheIntelligenceLayer: ArtificialIntelligence—MachineLearningandDeepLearning
Building upon the data foundation provided by Big Data and cloud computing,
the most impactful recent technological evolution is the increasing application of AI,
particularlyitssubfieldsMLandDL,toimbuesecurityanalyticswithgreaterintelligence,
automation,andpredictivepower.
• Elaboration and Evidence (Machine Learning): As a core subset of AI, ML has
emerged as a demonstrably powerful approach through which to address the
formidable challenge of extracting meaningful and actionable insights from the
large, diverse, and complex datasets generated within modern enterprise environ-
ments [41,60,70]. ML algorithms are designed to automatically uncover intricate
patterns, learn from historical security data (including both malicious and benign
activities),andidentifysubtleanomaliesthatmaydeviatefromestablishednormal
behavior,provingparticularlyeffectivewhenappliedtolarge-scaledatasets[47,71,72].
A key practical advantage over traditional, static rule-based systems, which can
quicklybecomeoutdatedandineffectiveagainstrapidlyevolvingcyberthreats[73],is
theabilityofMLmodelstobecontinuouslyupdatedandretrained. Thisadaptability
enables them to potentially detect emerging threats and novel attack patterns for
which explicit signatures do not yet exist. ML is especially crucial for advancing
predictiveanalyticscapabilitieswithinenterprises,allowingthemtomovebeyond
reactivedefensebyanticipatingpotentialsecuritythreatsandproactivelyimplement-
ingtargeteddefensivemeasures[37,38,48,49,58,66,74–76]. Thistransitionrepresentsa
naturalandnecessaryprogressioninmaximizingthestrategicvalueofsecurity-related
dataforenhancedenterprisedefense[56].
• ElaborationandEvidence(DeepLearning): DL,amoreadvancedandspecialized
subset of ML (and thus AI), represents a further cutting edge in the evolution of
securityanalytics,asevidencedbyitsapplicationinseveralreviewedstudiestargeting
complexsecuritychallenges[57,65,77–80]. DLmodels,suchasmulti-layeredneural
networks,havedemonstratedsuperiorperformance,particularlyinhandlinghighly
complex, high-dimensional, and often unstructured or semi-structured data types
prevalentincybersecurity(e.g.,rawnetworkpacketdata,systemcallsequences,and
free-textincidentlogs)[65,78]. AsignificantpracticalbenefitofmanyDLarchitectures
istheirinherentabilitytoperformautomaticfeatureextractionfromrawdata. This
alleviatestheneedformanualfeatureengineering,whichisoftenacomplex,time-
consuming,andexpertise-intensivetaskforsecurityanalysts. Withsufficientrelevant
datafortraining,DLtechniquescanachievehigheraccuracyandbettergeneralization
thanmanytraditionalMLmethods[77].Thisenhancedaccuracyiscriticallyimportant
inthesecuritydomain, wheretheconsequencesofbothfalsepositives(leadingto
alertfatigueandwastedinvestigativeeffort)andfalsenegatives(resultinginmissed

Electronics2025,14,2252 15of55
detections of actual threats) can be severe for an enterprise [57]. The capacity of
DLmodelstocontinuouslylearnandadaptfromnewdatamakesthemparticularly
effectivefordevelopingproactive,predictive,anddynamicsecurityanalyticssolutions
capableofaddressingnovelandevolvingadversarialtactics[79,80].
• Analysis: TheintegrationofAI,encompassingbothMLandDL,intoenterprisesecu-
rityanalyticssignifiesafundamentalparadigmshift. Itpropelssecurityoperations
beyond merely detecting known, signatured threats towards the more ambitious
goalsofidentifying“unknownunknowns”—previouslyunseenattackpatternsor
vulnerabilities—andanticipatingfutureadversarialcampaigns. Acorepracticalim-
plicationforenterprisesistheempowermentoftheirsecurityteamstoadoptamore
proactivestance,whichcanleadtotangiblebenefitssuchasreducedincidentresponse
times, minimized breach impact, and a stronger overall security posture. The ca-
pability of these AI-driven technologies to analyze security-related data at a scale
andspeedfarsurpassinghumananalyticalcapabilitiesistransformativeforSecurity
Operations Centers (SOCs), enabling them to better cope with the overwhelming
volumeofmodernsecuritytelemetry. However,thistransformativepotentialcomes
withpracticallimitationsandconsiderations. WhileAIcanenhanceautonomy,its
deploymentnecessitatesrobustvalidationprocessesandhumanoversighttoprevent
erroneousautomatedactionsthatcoulddisruptcriticalbusinessoperationsorlead
tomisallocationofsecurityresources. Furthermore,thepromiseofidentifying“un-
knownunknowns”requirescarefulmanagementofexpectations,asthediscoveryand
validationofgenuinelynovelthreatsremaincomplexandresource-intensive,witha
persistentriskofmisinterpretinganomalies.
• TrendsandChallenges: Thisintelligencelayerisincreasinglydrivingthedevelop-
mentandadoptionofadvancedsecuritytechnologiessuchasUEBA,sophisticated
Network Traffic Analysis (NTA) solutions, SOAR platforms, and next-generation
antivirus/endpointprotection(NGAV/EPP)systems. However,thewidespreadand
effective adoption of AI in enterprise security is not without significant practical
challengesandlimitations:
– DataRequirementsandQuality: Aprimaryhurdleisthecriticalneedforlarge
volumesofhigh-quality,relevant,andappropriatelylabeleddatasetsfortrain-
ingeffectivesupervisedMLandDLmodels. Inpractice,acquiring,preparing,
andmaintainingsuchdatasetsisasubstantialundertakingformostenterprises,
demandingsignificantinvestmentindatainfrastructure,governance,andspecial-
izedpersonnel. Thescarcityoflabeleddatafornovelorzero-dayattacksposesa
particularchallengeforsupervisedlearningparadigms.
– The“Black-Box”Problem: The“black-box”natureofmanycomplexML/DL
models,wherethereasoningbehindtheirpredictionsisnoteasilyunderstandable
by human analysts, presents a serious real-world limitation [81]. This lack of
interpretabilitycanhindertrust,slowdownadoption,andmakeitdifficultfor
SOC analysts to validate alerts or for engineers to debug and refine models,
potentiallyleadingtocriticalalertsbeingoverlookedormisunderstood.
– AdversarialAIAttacks: MLmodelsthemselvescanbetargetsofsophisticated
adversarialattacks(e.g.,datapoisoningandevasionattacks),whereattackers
manipulateinputdatatocausemisclassificationorevadedetection. Thisvulnera-
bilityisagrowingpracticalconcernforenterprises,asitmeansthatAI-driven
securitysystemscanbesubverted,underminingtheirreliabilityandeffectiveness.
– Specialized Skills Gap: There remains a significant and persistent skills gap.
DatascientistsandMLengineerswhoalsopossessdeepcybersecuritydomainex-
pertisearelacking[81]. Practically,thismeansmanyenterprisesstruggletohire,

Electronics2025,14,2252 16of55
develop,andretainthetalentnecessarytobuild,deploy,manage,andcritically
evaluatetheseadvancedAI-drivensecurityanalyticssolutions,oftenleadingto
relianceonthird-partyvendorsorunderutilizationofthetechnology’spotential.
– IntegrationandOperationalizationComplexity: IntegratingadvancedAIana-
lyticsintoexistingsecurityworkflowsandITinfrastructurecanbecomplexand
disruptive. EnsuringthatAI-generatedinsightsareeffectivelyoperationalized—
thatis,translatedintotimelyandappropriatesecurityactions—requirescareful
planning,processre-engineering,andoften,significantchangestoexistingSOC
procedures.
EnsuringaclearconceptualhierarchywhereinMLandDLareunderstoodasintegral
componentsofthebroaderAIfieldwithspecificstrengthsandweaknessesisimportantfor
consistentunderstandingandstrategicdevelopmentwithinthecybersecuritydomain.
Table2summarizestheprimaryimpactsofthesekeytechnologiesoncybersecurity
analyticswithintheenterprisecontext.
Table2.Keytechnologiesandtheirtransformativeimpactsonenterprisecybersecurityanalytics.
Technology ImpactonCybersecurityAnalytics
Providesscalableandflexibleinfrastructureforhostingdata-intensiveanalyt-
CloudComputing ics;enablesefficientnetworkmonitoring,real-timethreatdetection,andsup-
portsbusinesscontinuity.
Enablestheingestion,storage,andprocessingofvastanddiversesecurity
BigData datavolumes;facilitatestheextractionofactionableinsightsforcomprehen-
sivethreatdetectionandmitigation.
Serveasacriticaldatasource(e.g.,weblogs,applicationdata)andaplatform
WebTechnologies fordeliveringinteractivesecuritydashboards,visualizations,andreal-time
alertsfortimelyincidentresponse.
Empowersautomateddetectionofcomplexpatterns,anomalies,andsuspi-
MachineLearning(AISubset) ciousbehaviorsfromlargedatasets;facilitatespredictiveanalyticsforearly
threatidentificationandproactivedefense.
Handleshighlycomplex,unstructured,andhigh-dimensionaldata;enables
DeepLearning(AISubset) automaticfeatureengineeringandcontinuousmodeladaptationformore
accurateandproactivethreatintelligence.
Inconclusion,thetechnologicallandscapeofenterprisesecurityanalyticsischarac-
terizedbyadynamicandprogressiveintegrationofcapabilities. Fromthefoundational
scalabilityofferedbycloudcomputingandBigDatatotheadvancedintelligencefurnished
bymachinelearninganddeeplearning,thisevolutionreflectsarelentlesspursuitofmore
effective,efficient,andproactivestrategiestocombattheever-advancingsophistication
ofcyberthreats. Thisongoingtechnologicalshiftunderscoresthecentralityofdataand
intelligenceinmoderncybersecurityparadigms.
Observation3(Ob3): TheImperativeforaHolistic,Business-IntegratedApproach
toSecurityAnalytics
Oursystematicliteraturereviewrevealsagrowingrecognitionthattraditionalsecurity
analytics,oftenconfinedtopurelytechnicaldimensions,areincreasinglyinsufficientto
address the complex, interconnected nature of modern enterprise operations and their
associated cyber risks [36,82]. This highlights a significant thematic observation: the
imperativetoevolvetowardsaholisticapproachthatintrinsicallymarriessecurityanalytics
withoverarchingbusinessrealities,objectives,andprocesses[35,83].
• ElaborationandEvidence: Aholisticapproachtosecurityanalytics,asconceptual-
izedwithinthereviewedliterature,intentionallytranscendspurelytechnicalthreat
detection. Itadvocatesforanintegratedmethodologythatsystematicallyconsiders
multipleorganizationalperspectivesandcriticalinfluencingfactors. Inpractice,this

Electronics2025,14,2252 17of55
involvesextendingthepurviewofsecurityanalyticsbeyondthemereidentification
oftechnicalvulnerabilitiestoalsocriticallyexaminetheintricateworkingsofcore
businessprocesses,includingtheiroperationalefficiencydrivers[38,84],overarching
strategiccorporateobjectives,andthecontinuouslyevolvingregulatorycompliance
landscapes[34,85]. Arecurringthemeinthereviewedstudiesisthatasbusinesspro-
cessesinevitablygrowincomplexity—drivenbyrapidtechnologicaladvancements
(e.g., the proliferation of interconnected IoT devices and sprawling cloud service
dependencies)anddynamicmarketdemands—theenterpriseattacksurfaceandpo-
tentialthreatvectorsconsequentlybecomemoremultifacetedanddeeplyembedded
withintheseoperationalprocesses[31–33,86]. Thisescalatingcomplexitynecessitates
asecuritystrategythatisnotonlycomprehensiveinitscoveragebutalsoinherently
adaptivetochange. Theliteraturesuggeststhatadoptingsuchaholisticapproachpro-
videsavitalcontext-centricperspective[57],therebyenablingthedevelopmentand
deploymentofsecuritymeasuresthataremorepreciselytailoredtouniquebusiness
needsandspecificriskappetites.
Itisimportanttonoteakeyobservationfromourreview: whilethesurveyedliter-
aturestronglyandconsistentlyadvocatesfortheneedforholisticsecurityanalytics,
andseveralstudiesproposevaluableconceptualframeworksormodelsaimingin
thisdirection, thereisalesspronouncedemphasisonempiricalstudiesthatrigor-
ouslyvalidatethesuperioreffectivenessormeasurableROIofspecific,namedholistic
frameworkswhencompareddirectlywithmoretraditional,purelytechnicalsecurity
solutionswithindiverseenterprisesettings. Thissuggestsasignificantpracticalgap
andacrucialareaforfutureresearchfocusedonthedemonstrableimplementation
benefitsandquantifiableoutcomesofcomprehensiveholisticmodels.
• Analysis:Thecorecritiqueoftraditional,siloedsecurityanalyticsisitsinherentpracti-
callimitation,thatis,atendencytogenerateanarrow,technicallyfocusedviewofrisk
thatisoftendisconnectedfromtheactualorpotentialbusinessimpact. Inreal-world
terms,thisdisconnectcanleadtomisalignedsecuritycontrols(e.g.,over-investing
inlow-impactareaswhileunder-resourcingcriticalbusinessfunctions), inefficient
allocationofscarcesecurityresources,unintendeddisruptiontocriticalbusinessoper-
ationsduringincidentresponse,and,ultimately,adiminishedoverallsecurityposture
despitesignificanttechnicalefforts. Conversely,agenuinelyholisticapproachseeks
totransformcybersecurityfrombeingperceivedmerelyasacostcenterorapurely
technicalsupportfunctionintoastrategicbusinessenablerthatcontributestoorga-
nizationalresilienceandtrustworthiness. Thepracticalimplicationsofsuccessfully
adoptingsuchanintegratedapproachareprofound,thoughchallengingtoachieve.
– Itnecessitatesenhancedandsustainedcross-departmentalcollaboration,actively
breakingdownentrenchedsilosbetweenIT/securityteamsandvariousbusiness
units(e.g.,finance,operations,legal). Practically,thisrequiresstrongleadership
commitment,clearcommunicationchannels,andoften,aculturalshifttowards
sharedresponsibilityforsecurity.
– Itcallsforthecultivationoracquisitionofcybersecurityprofessionalswhopos-
sess not only deep technical expertise but also strong business acumen, risk
managementunderstanding,andeffectivecommunicationskillstoengagewith
diversestakeholders. Findingordevelopingsuchhybridtalentisasignificant
practicalchallengeformanyorganizations.
– Itdemandsthedevelopment,implementation,andconsistenttrackingofsecurity
metricsthatresonatewithbusinessleadersandclearlydemonstratethevalueof
securityinvestmentsintermsoftangibleriskreduction,operationalcontinuity,

Electronics2025,14,2252 18of55
andbusinessenablement[35]. Definingthesemetricsandcollectingthenecessary
datacanbeacomplexpracticalundertaking.
– Itimpliesastrategicorganizationalshifttowardscomprehensiveandintegrated
riskmanagementframeworks(e.g.,systematicallyintegratingcybersecurityrisk
intobroaderEnterpriseRiskManagement—ERMprograms)thatinherentlycon-
siderbusinesscontext,impacttolerance,andstrategicobjectivesinallsecurity
decisionmaking.
• TrendsandChallenges: Thedrivetowardsamoreholisticperspectiveinsecurity
analyticsalignswithandissupportedbyseveralimportanttechnologicalandcon-
ceptualtrends,whilealsofacingsignificantpracticalchallengesandlimitationsin
itsimplementation:
– Supporting Trends: The development and adoption of Governance, Risk,
andCompliance(GRC)platformsaimtoprovideanintegratedviewandman-
agement of these interconnected domains, thereby facilitating a more holistic
approach to enterprise risk. The increasing emphasis within modern system
developmenton“SecuritybyDesign”and“PrivacybyDesign”principlesinher-
entlyrequiresaproactive,holisticunderstandingofbusinessprocessesanddata
flowsfromtheearlieststages. Furthermore,advancementsinAI-drivenanalyt-
icsareleadingtomorecontext-awaresecuritytools,suchasUEBA,whichcan
betterunderstanduserrolesandtypicalbusinessfunctionsandflagmeaningful
deviationsfromnormaloperationalpatterns.
– PersistentReal-WorldChallenges:
* Aprimarylimitationisbridgingthepersistentcommunicationandcultural
gap that often exists between highly technical security teams and more
business-focused operational units. Overcoming differing priorities and
vocabulariesrequiresconcertedeffort.
* Developingmeaningful,quantifiablemetricsthateffectivelytranslatetech-
nicalsecurityoutcomes(e.g.,vulnerabilitiespatched,incidentscontained)
intodemonstrablebusinessvalue(e.g.,riskreductioninmonetarytermsand
protectionofrevenuestreams)remainsacomplexpracticaltask.
* Theinherentcomplexityofaccuratelymodelingdiverse,dynamic,andoften
opaquebusinessprocesses,alongwiththeirintricateITdependenciesand
associatedsecurityrisks,canbeadauntingimplementationhurdle.
* As noted earlier, the lack of widely adopted, standardized holistic frame-
works and the difficulty in empirically demonstrating the direct ROI of a
holisticapproachcomparedtopurelytechnicalinterventionscansignificantly
hinderitsadoptionandinvestmentjustificationinpractice.
* Moreover, implementing a truly holistic security strategy often involves
higher initial and ongoing investment in terms of time, skilled resources,
andsignificantorganizationalchangemanagement,creatingasubstantial
practicalbarrier,especiallyforresource-constrainedorganizations.
Insummary,Observation3underscoresapivotalshiftinperspective: effectiveen-
terprisesecurityanalyticsinthemoderneramustbedeeplyinterwovenwiththefabric
ofthebusinessitself. Thisholisticintegrationiscrucialfordevelopingresilient,adaptive,
and context-aware security strategies that not only protect assets but also support and
enhancecorebusinessobjectives.

Electronics2025,14,2252
19of55
4.2. TheLandscapeofEnterpriseSecurityAnalyticsAdoptionAcrossIndustriesandSectors(RQ2)
ThissubsectionaddressesRQ2byexaminingthedistributionandfocusofsecurity
analytics adoption across various industries, enterprise types, and operational sectors,
asidentifiedinthereviewedliterature.
Observation 4 (Ob4): Concentrated Adoption in Large, Critical Sectors with a
NotableResearchGapforSMEs
Oursystematicreviewindicatesthatwhiletheadoptionofsecurityanalyticsispresent
acrossarangeofindustries,itsapplicationandassociatedresearcharenotablyconcentrated
in large-scale enterprises and within sectors deemed critical, such as Information and
CommunicationTechnology(ICT),financialservices,andutilities. Conversely,thereisa
significantlylesspronouncedresearchfocusonthespecificsecurityanalyticsneedsand
adoptionpatternswithinSMEs.Table3providesadetailedbreakdownofsecurityanalytics
adoptionbyindustryandenterprisesizeasreflectedintheselectedstudies.
Table3.SecurityAdoptionofanalyticsacrossindustriesandenterprisesize.
TargetedIndustry/Sector/Domain/Field SizeofEnterprise Studies
|     | Large-scale | [41] |
| --- | ----------- | ---- |
ICTandRelatedFields
|     | Any         | [45,78,87–89] |
| --- | ----------- | ------------- |
|     | Large-scale | [35,61,66,90] |
FinancialServices(includingOnlineBanking)
| andGovernmentInstitutions                | Any         | [74,91] |
| ---------------------------------------- | ----------- | ------- |
| IndustrialControlandSecuritySystems      | Large-scale | [92]    |
| Utilities(Power,Fuel,Energy)             | Any         | [42,84] |
| HealthSystems                            | Any         | [83]    |
| SmartInfrastructuresandSystems(including | Any         | [76,93] |
IoT,IIoT,Cyber–PhysicalSystems,SmartGrid)
|     | SME | [58] |
| --- | --- | ---- |
Large-scale [37,38,47,55,57,64,68,70,71,75,77,94]
| Notmentioned | SME                              | [49,95] |
| ------------ | -------------------------------- | ------- |
|              | Any [46,48,56,65,67,80,86,96,97] |         |
• Elaboration&Evidence: AsdetailedinTable3,theadoptionofsecurityanalyticsis
notablyconcentratedinlarge-scaleenterprises,particularlywithintheICTsector[41],
financial services and government institutions [35,61,66,90], and industrial control
systems(ICS)environments[92]. Forenterpriseswherespecificsizewasnotaprimary
focusorfindingsweredeemedbroadlyapplicable(“Any”size),adoptionremains
prominentincriticalutilities(power,fuel,energy)[42,84],financialservices[74,91],
ICTandrelatedfields(e.g.,telecommunications,softwaredevelopment)[45,78,87–89],
healthsystems[83],andincreasinglyinemergingsmartinfrastructures(includingIoT
andCyber–PhysicalSystems)[76,93]. Asubstantialnumberofthereviewedstudies
thattargetedlargeenterprises[37,38,47,55,57,64,68,70,71,75,77,94]orwereapplicable
to“Any”enterprisesize[46,48,56,65,67,80,86,96,97]didnotspecifyanarrowindus-
tryfocus. Thissuggestseithertheperceivedgeneralapplicabilityofthediscussed
analyticssolutionsandfoundationaltechniquesoraprimaryresearchfocusonthe
techniquesthemselvesratherthantheirsector-specificnuances.
Critically,ourreviewrevealsthatonlyasmallfractionoftheselectedliterature(three
studies: [58] focusing on Smart Infrastructures/IIoT and [49,95] focusing on non-
sector-specific contexts) explicitly centers on the unique security analytics needs
and adoption contexts of SMEs. Study [58], for instance, explores Security as a
Service(SECaaS)tailoredforSMEsoperatingintheIndustrialInternetofThings(IIoT)
domain,highlightingapotentialservicedeliverymodelmoreattunedtotheirresource
constraints. This starkly limited representation of SMEs in the research landscape

Electronics2025,14,2252 20of55
underscoresasignificantpracticalgap;despitetheircollectiveeconomicimportance
andrecognizedvulnerabilitytoawidearrayofcyberthreats,thedevelopmentand
academicinvestigationoftailoredsecurityanalyticssolutionsforthissegmentappear
considerablyunderdeveloped.
• Analysis: Theobservedconcentrationofsecurityanalyticsadoptionandassociated
researchprimarilywithinlargeenterprisesandcriticalsectorscanbeattributedto
severalinterconnectedpracticaldriversandrealities:
– ResourceAvailabilityandOperationalComplexity: Largeorganizationstyp-
ically possess substantially greater financial and dedicated human resources,
enablingthemtoinvestinsophisticated,oftenexpensive,analyticsplatformsand
thespecializedpersonnelrequiredtomanagethem. Theyalsotendtooperate
moreextensiveandcomplexIT/OTenvironments,generatingvastvolumesof
datathatbothnecessitatesandbenefitsfromadvancedanalyticalcapabilitiesfor
effectiveoversightandthreatdetection.
– ElevatedRiskProfileandPotentialImpact: Theselargerentitiesareoftenhigh-
value,high-visibilitytargetsforsophisticatedcyberattacks. Inpracticalterms,
a security breach can lead to catastrophic financial losses, severe reputational
damage,erosionofcustomertrust,andwidespreadoperationaldisruption(e.g.,
in financial systems [35,66,90] or industrial control environments [92]). This
heightenedriskcalculusmandatesproactiveandadvancedsecuritymeasures,
includingrobustanalytics.
– StringentRegulatoryandCompliancePressures: Criticalsectorssuchasfinance,
healthcare[83],andutilities[42,84]frequentlyoperateunderstringentandevolv-
ing regulatory and compliance mandates (e.g., PCI DSS, HIPAA, NERC CIP).
Theseobligationsoftencompeltheimplementationofcomprehensivesecurity
monitoring,auditing,andreportingcapabilities,forwhichsecurityanalyticsare
increasinglyindispensable.
Thepracticalimplicationsoftheseskewedadoptionandresearchpatternsaresignifi-
cantandmultifaceted. Firstly,thepredominanceofresearchfocusedonlarge-enterprise
contexts may result in security analytics solutions, frameworks, and best practices that
arenotreadilyadaptable,affordable,orpracticallyimplementableforSMEs. Solutions
mayassumetheavailabilityoflarge,dedicatedsecurityteams,extensivehistoricaldatasets
for model training, or complex integration capabilities that are often absent in smaller
organizations. ThisdirectlyexacerbatesthecybersecurityvulnerabilityofSMEs,which
frequentlylacktheinternalexpertise,financialresources,andoperationalcapacityoftheir
largercounterparts,makingthemattractive,softertargetsforattackers. Secondly,while
highlyspecialized,sector-specificanalyticsarevital(e.g.,forICSenvironmentswithunique
operational technologies and threat models), the large number of studies with a “Not
mentioned”industryfocussuggestsasubstantialbodyofworkonfoundationalanalytics
techniques. However,apracticalchallengeremainsineffectivelytranslatingthesegeneral
techniquesintoactionable,sector-specificguidanceandconfigurationsforpractitioners
indiversefields. ThepronouncedSMEgap,therefore,impliesapressingreal-worldneed
forfocusedresearchanddevelopmentintoscalable,cost-effective,anduser-friendlyse-
curityanalyticssolutions,explicitlytailoredtothedistinctoperationalrealities,resource
constraints,andprevalentthreatlandscapesfacedbysmallerorganizations.
• TrendsandChallenges:
– SupportingTrendsforBroader,MoreEquitableAdoption: Theincreasingavail-
abilityofcloud-basedsecurityanalyticsplatformsandSECaaSmodels[58]offers
apromisingpathwaythroughwhichtomakeadvancedanalyticalcapabilities

Electronics2025,14,2252 21of55
moreaccessibleandaffordabletoawiderrangeoforganizations,includingSMEs.
Thesemodelscanpracticallyreducetheneedforsignificantupfrontinfrastruc-
tureinvestmentandspecializedin-housemanagementexpertise. Concurrently,
theongoingdevelopmentofAI-poweredanalyticsaimstoautomatemorecom-
plexdetection,analysis,andresponsetasks,potentiallyloweringtheskillsbarrier
foradoptionandmakingsophisticatedtoolsmoreusablebyteamswithlimited
datascienceexperience. Furthermore,thereisagrowingtrendtowardsindustry-
specificthreatintelligencesharingandtheformationofcollaborativeplatforms
(e.g.,InformationSharingandAnalysisCenters—ISACs). Theseinitiativescan
significantlyenrichsecurityanalyticswithrelevant,contextualthreatdata,aprac-
ticalbenefitthatcanenhancetheeffectivenessofanalyticsforallparticipating
organizations,includingSMEswithinthosesectors.
– PersistentReal-WorldChallengesandLimitations: Despitepositivetrends,sig-
nificanthurdlesremain. TheprimarypracticalchallengeforSMEscontinuestobe
theoften-prohibitivecostandperceivedoperationalcomplexityofimplementing
and managing effective security analytics tools, compounded by a persistent
generalshortageofaffordablecybersecuritytalent. Fororganizationsofallsizes,
real-worlddifficultiesincludethetechnicalcomplexitiesofintegratinganalytics
solutionswithdiverse,oftensiloed,ITandOperationalTechnology(OT)systems;
ensuringconsistentdataqualityandgovernanceacrossdisparatesources;and
effectivelymanagingthesheervolumeofalertsgeneratedtoavoidanalystfatigue
andensurecriticalthreatsareprioritized. Developingtrulysector-specificanalyt-
icsthatdeeplyunderstanduniqueindustrialprotocols(e.g.,inmanufacturingor
medicalsystems),specificregulatoryrequirements,anddistinctbusinessprocess
risksisacontinuousandresource-intensiveeffort.The“Notmentioned”category
regardingindustryapplicationinmanystudies(seeTable3)mightalsopointto
anongoingpracticalchallengeintranslatinggeneralacademicresearchfindings
into clear, actionable, sector-specific guidance for practitioners. Finally, a key
designandmarketlimitationisensuringthatsophisticatedanalyticssolutions
canscaledowneffectivelyforsmallerorganizationsorthosewithlessmature
security programs, without losing essential functionality or becoming overly
simplistic. Addressingthesemultifacetedchallengesiscriticalfordemocratizing
effectivesecurityanalyticsacrosstheentireenterprisespectrum.
Inessence,Observation4highlightsthatwhilesecurityanalyticsisrecognizedasvital
acrosstheboard,itscurrentin-depthadoptionandresearchfootprintareskewedtowards
larger organizations in critical industries. Bridging the gap for SMEs and ensuring the
continueddevelopmentofeffective,adaptableanalyticsforallsectorsremainkeypriorities
forbothresearchersandpractitioners.
4.3. TechnicalAspectsoftheImplementationandOptimizationofSecurityAnalyticsin
Enterprises(RQ3)
ThissubsectionaddressesRQ3bydissectingthevariousdata-processingandanaly-
sis techniques employed in enterprise security analytics, as identified in the reviewed
literature. Table 4 categorized studies by these techniques; this analysis synthesizes
thatinformation.

Electronics2025,14,2252
22of55
Table4.Selectedstudiesonsecurityanalyticsintheenterprisecontext.
| Framework,Platform, |           |     |                    |        |       |      |      | Typeof   |          |
| ------------------- | --------- | --- | ------------------ | ------ | ----- | ---- | ---- | -------- | -------- |
| Study               |           |     | AnalysisTechniques | Method | Model | Tool | Name |          | Strategy |
|                     | Prototype |     |                    |        |       |      |      | Analysis |          |
✓
S1[41]Cheng_2013 In-memorydatamanagement – – – SAL Mix Proactive&Reactive
✓
S2[42]Holm_2013 – Modellinglanguage – – CySeMoL Quantitative Proactive
|                    |     |     |               | ✓   | ✓   |     |     |     |           |
| ------------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --------- |
| S3[43]Purboyo_2013 | –   |     | Visualisation |     |     | –   | –   | Mix | Proactive |
S4[31]Wang_2013 – Gametheory&Stochastic ✓ ✓ – ADSGN Quantitative Proactive
S5[32]Abraham_2014 – AbsorbingMarkovchains&Attackgraph – ✓ – – Quantitative Predictive
S6[34]Ahmed_2014 – Role-basedaccesscontrol(RBAC) ✓ – – SREBP – Proactive
S7[33]Brewer_2014 – Multi-dimensionalbehaviouralanalytics ✓ – – – Mix Proactive&Predictive
S8[35]Li_2014 ✓ Three-layerconceptualmodel ✓ – – – – Proactive
S9[36]Rieke_2014 – Model-based – ✓ – – Qualitative Predictive
|     |     |     |     | ✓   | ✓   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S10[91]Xin_2014 – STRIDEthreatmodel&Threattreeanalysis – – Qualitative Proactive
|     | ✓   |     |     |     | ✓   | Non-homogeneous |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
S11[98]Abraham_2015 Attackgraph&Stochasticmodelling – – Quantitative Predictive
MarkovModel
|     | ✓   |     |     |     | ✓   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
S12[87]Cai_2015 AnalyticHierarchyProcess(AHP) – – IBN Mix Proactive
S13[53]Hussein_2015 ✓ Virtualisedhoneypot&Covariancematrix ✓ – – – Quantitative Proactive&Reactive
Compliancemonitoring&Model-based
| S14[83]Rieke_2014 | –   |     |     | –   | ✓   | –   | PSA@R | Qualitative | Predictive |
| ----------------- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ---------- |
behaviorprediction
S15[61]Stepanova_2015 ✓ Ontology-basedautomatedpenetrationtesting ✓ – ✓ – Mix Proactive
|     |     |     |     |     | ✓   |     | Extensionof |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
S16[82]Valja_2015 – Attackgraph-based – – Quantitative Proactive
P2CySeMoL
|                     | ✓   | ExtensibleConfigurationChecklistDescription |     |     | ✓   |     |     |              |           |
| ------------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --------- |
| S17[85]Alsaleh_2016 |     |                                             |     | –   |     | –   | –   | Quantitative | Proactive |
Format(XCCDF)&vulnerabilityscoringsystems
|     | ✓   | Grubbs’test,SupportVectorMachine& |     |     |     | ✓   |     |     |     |
| --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
S18[71]Baluda_2016 Automata-basedbehavioralmodeling – – EMMA Quantitative Detective
S19[88]Jenab_2016 – Flow-graphconcept&Markovianmethod – ✓ – – Quantitative Detective&Predictive
| S20[99]Kim_2016 | ✓   |     | Problemdomainontology | ✓   | –   | –   | –   | –   | Proactive |
| --------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --------- |
S21[62]Kotenko_2016 – Attackgraph&Securitymetriccalculation – – – – Quantitative –
ComputationalIntelligence,Windowsbatch
| S22[90]Naik_2016 | –   |     |     | ✓   | –   | –   | –   | Quantitative | Predictive |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- |
programming&Rlanguage
|                 | ✓   | Collectingcommonsecurityproblems& |     |     | ✓   |     |     |             |           |
| --------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | ----------- | --------- |
| S23[54]Niu_2016 |     |                                   |     | –   |     | –   | –   | Qualitative | Proactive |
Buildingaknowledgebase

Electronics2025,14,2252
23of55
Table4.Cont.
| Framework,Platform, |           |                                      |                    |        |            |      | Typeof       |            |
| ------------------- | --------- | ------------------------------------ | ------------------ | ------ | ---------- | ---- | ------------ | ---------- |
| Study               |           |                                      | AnalysisTechniques | Method | Model Tool | Name |              | Strategy   |
|                     | Prototype |                                      |                    |        |            |      | Analysis     |            |
|                     | ✓         | Graphgenerationalgorithms&Customized |                    |        | ✓          |      |              |            |
| S24[100]Ou_2016     |           |                                      |                    | –      | –          | –    | Quantitative | Predictive |
reasoningalgorithms
|     |     | Graph-basedattack&Enterprise |     | ✓   |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
S25[89]Valja_2016 – architecturelanguage – – CySeMoL-ArchiMate Quantitative Proactive
| S26[94]          |     | Endpointmonitoringandclustering&       |                             |     |     |     |              |                     |
| ---------------- | --- | -------------------------------------- | --------------------------- | --- | --- | --- | ------------ | ------------------- |
|                  | –   |                                        |                             | ✓   | – – | –   | Quantitative | Detective&Proactive |
| Buyukkayhan_2017 |     |                                        | Outlierdetection            |     |     |     |              |                     |
| S27[96]Kato_2017 | –   |                                        | Attacktree                  | ✓   | – – | –   | Quantitative | Proactive           |
| S28[70]          |     | Threatmodeling,domain-specificlanguage |                             |     |     |     |              |                     |
|                  | –   |                                        |                             | ✓   | – ✓ | –   | –            | Proactive           |
| Lagerstrom_2017  |     |                                        | (DSL)&Reinforcementlearning |     |     |     |              |                     |
✓
S29[95]Nguyen_2017 Uncertaingraphs – – – Quantitative Proactive
|                     | ✓   | In-memorydatastorage,misusedetection, |     |     |     |       |              |     |
| ------------------- | --- | ------------------------------------- | --- | --- | --- | ----- | ------------ | --- |
| S30[47]Sapegin_2017 |     |                                       |     | –   | – – | REAMS | Quantitative | –   |
query-basedanalytics,andanomalydetection
|     | ✓   |     |     | ✓   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
S31[55]Zhu_2017 Behaviourpathrestoration – – – Mix Detective&Proactive
Topic-modelingtechnique,LatentDirichlet
| S32[45]Cinque_2018 | –   |     |     | ✓   | – – | –   | Mix | Detective |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --------- |
Allocation(LDA)
Threatmodeling,riskanalysis,&
| S33[101]Sion_2018 | ✓   |     |     | ✓   | – – | TMaRA | Mix | Proactive&Predictive |
| ----------------- | --- | --- | --- | --- | --- | ----- | --- | -------------------- |
Designdecisions
|                 | ✓   |     | Graph-basedeventcorrelation& | ✓   |     |      |              |                     |
| --------------- | --- | --- | ---------------------------- | --- | --- | ---- | ------------ | ------------------- |
| S34[56]Win_2018 |     |     |                              |     | – – | BDSA | Quantitative | Proactive&Detective |
Logisticregression
✓
S35[102]Wu_2018 – OpenVAS,Ontology-&Graph-basedapproach – – – Qualitative Proactive&Detective
|                 |     | Self-organizingMaps,Fuzzyc-means& |     | ✓   | ✓   |     |              |           |
| --------------- | --- | --------------------------------- | --- | --- | --- | --- | ------------ | --------- |
| S36[63]Lai_2019 | –   |                                   |     |     | –   | –   | Quantitative | Detective |
t-SNEalgorithms
S37[73]
– Probabilisticarithmeticautomata&SVM – ✓ – – Quantitative Detective
Padmanaban_2019
S38[60]Sharma_2019 ✓ Hivequeries,k-algorithm&SVM – – – ANSA Quantitative Detective
Apachesparkframework&Customized
S39[72]Ahmed_2020 ✓ – – – SAD-F Quantitative Proactive&Detective
machinelearning
| S40[52] | ✓   |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
VirtualMachineLiveMigration(VM-LM) – – – – Quantitative Proactive
Alavizadeh_2020
| S41[77]        | ✓   | Deep-QNetworkanddomain-specifictransition |                    |     |     |      |     |           |
| -------------- | --- | ----------------------------------------- | ------------------ | --- | --- | ---- | --- | --------- |
|                |     |                                           |                    | –   | – – | ASAP | Mix | Proactive |
| Chowdhary_2020 |     |                                           | matrix&Attackgraph |     |     |      |     |           |
Monitoringsystemswithgraphanalytics&
S42[57]Elsayed_2020 ✓ – – – PredictDeep Quantitative Detective&Predictive
Graphconvolutionalneuralnetwork(GCN)

Electronics2025,14,2252
24of55
Table4.Cont.
| Framework,Platform, |           |                                    |        |            |      | Typeof       |                     |
| ------------------- | --------- | ---------------------------------- | ------ | ---------- | ---- | ------------ | ------------------- |
| Study               |           | AnalysisTechniques                 | Method | Model Tool | Name |              | Strategy            |
|                     | Prototype |                                    |        |            |      | Analysis     |                     |
|                     |           | Attackgraphs&Calculationofsecurity | ✓      |            |      |              |                     |
| S43[93]Ivanov_2020  | –         |                                    |        | – –        | –    | Quantitative | Proactive&Detective |
indicators
| S44[84] | ✓   |     |     |     |     |     | Proactive,Detective& |
| ------- | --- | --- | --- | --- | --- | --- | -------------------- |
Nashivochnikov_2020 Dataanalysis – – – – Quantitative Predictive
S45[78]
– Processmining&Naturallanguageprocessing ✓ – – – Mix Detective
Sundararaj_2020
S46[64]Taylor_2020 – Datarepresentation – – ✓ SysFlow Mix Detective
S47[65]Wu_2020 – Spatio-temporalcharacteristics – ✓ – – Quantitative Detective&Predictive
S48[92]Zhang_2020 – Attackgraph-based&Graphdatabase ✓ – – – Quantitative Proactive
|     | ✓   |     | ✓   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
S49[79]Aquino_2021 Processinghistoricalbehaviorofattacks – – – Mix Predictive
|     | ✓   |     |     |     |     |     | Detective,Proactive& |
| --- | --- | --- | --- | --- | --- | --- | -------------------- |
S50[58]Empl_2021 Threatmodelingandcomplexeventprocessing – – – – –
Predictive
S51[86]Kumar_2021 ✓ Stochastictimedautomataandstatistical – ✓ – ECKC Quantitative Proactive
model-checking
S52[46]Rosado_2021 – MARISMAmethodology&eMARISMAtool ✓ – ✓ MARISMA-BiDa Mix Proactive
S53[74]Vassilev_2021 ✓ Ontology&Knowledgegraphs – – – – Qualitative All
S54[80]Chen_2022 – Word2Vec,N-Grammodel ✓ ✓ – – Mix Proactive
|     |     |     | ✓   |     |     |     | Detective,Reactive& |
| --- | --- | --- | --- | --- | --- | --- | ------------------- |
S55[66]Chun_2022 – Behaviour-basedintelligence – – – Quantitative
Predictive
✓
S56[75]Ndichu_2022 Onlinesupervisedlearning – – – – Quantitative Detective&Predictive
|     | ✓   |     |     | ✓   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
S57[97]Sonmez_2022 MITREATT&CKframework,CAPEC,CWE – – AttackDynamics Quantitative Detective&Proactive
|     |     |     | ✓   | ML- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
S58[48]Zou_2022 – AISCgraph,two-layerMLSDgraph – SSA – Quantitative Proactive
S59[76]Efiong_2023 – Machinelearning – ✓ – – Quantitative Detective&Predictive
S60[59]Vassilev_2023 ✓ Threatintelligence – – – – Mix Detective
A1[67]Early_2015 – Dataanalytics ✓ – – – Quantitative Proactive&Predictive
A2[37]Puri_2015 – Graphanalytics&Datamining ✓ – – – Quantitative Detective&Predictive
✓
A3[38]Li_2016 Behaviourprofiling&Statisticalanalysis – – – – Quantitative Proactive&Predictive
|                  | ✓   | Visualizationandclustering&User-centered |     | ✓   |     |     |                      |
| ---------------- | --- | ---------------------------------------- | --- | --- | --- | --- | -------------------- |
| A4[49]Ulmer_2018 |     |                                          | –   | –   | –   | Mix | Detective&Predictive |
design
|     | ✓   |     |     |     |     |     | Detective,Reactive& |
| --- | --- | --- | --- | --- | --- | --- | ------------------- |
A5[68]Chernova_2019 Correlationanalysis – – – – Quantitative Proactive

Electronics2025,14,2252 25of55
Observation5(Ob5): PredominanceofMachineLearningandGraph-BasedAp-
proachesAmidstaDiverseRangeofAnalysisTechniques
Ourreviewrevealstheapplicationofadiversearrayofprocessingandanalysistech-
niques. While multiple methodologies are utilized, there is a clear gravitation towards
machine learning and computational intelligence (MLCI) and graph-based approaches
(GBAs). Thistrendunderscorestheindustry’sresponsetoescalatingcyberthreatcomplex-
ity,demandingdata-intensive,interconnected,andintelligentanalyticalmethods. Other
specializedtechniques,includingBehavioralAnalysisandProfiling(BAP),variousModel-
ingTechniques(MTs),andOntologiesandKnowledgeGraphs(OKGs),alsoplaycrucial,
oftencomplementary,roles. FoundationalDataManagementandRepresentation(DMR)
techniquesfurtherunderpintheefficacyoftheseanalyticalmethods.
Theprimarycategoriesofanalysistechniquesidentifiedarediscussedbelow,high-
lightingtheirprevalence,coreconcepts,implications,andconnectiontobroadertechnolog-
icaltrends.
• MachineLearningandComputationalIntelligence(MLCI):Thiswasthemostpromi-
nentcategoryofanalyticaltechniquesidentified,beingcentraltothemethodologies
of12reviewedstudies[56,57,60,63,71–73,75–77,80,90].
– ElaborationandEvidence: MLCI,aspresentedintheliterature,encompasses
a range of computational models, statistical analysis methods, and machine
learningalgorithmsappliedtosecuritydatafortaskssuchasthreatdetection,
classification, and predictive decision making. Examples from the reviewed
studies include the application of Support Vector Machines (SVMs) for intru-
siondetectionandmalwareclassification,aimingtodistinguishmaliciousfrom
benignactivities[60,71];theuseofDeep-QNetworks(DQNs),whichcombine
Q-learningwithdeeplearning,foroptimizingincidentresponsestrategies[77];
thedeploymentofLatentDirichletAllocation(LDA)andN-Grammodelsfor
text-basedanomalydetectionandderivingthreatintelligencefromunstructured
logdata[45,80];andtheutilizationofensemblelearningmethodslikeboosting
toimprovepredictiveaccuracyforthreatidentification[76]. Itisimportantto
notethatwhilethesestudiesreportvaryingdegreesofsuccess,theirpractical
validityandreliabilityinbroaderenterprisecontextsoftendependonthespecific
datasetsusedfortraining/testingandtheexperimentalconditions,necessitating
carefulevaluationbeforewidespreadreal-worlddeployment.
– Analysis:TheobserveddominanceofMLCIinthereviewedliteraturestemsfrom
itsinherentcapabilitiestoprocessvastandcomplexsecuritydatavolumes,auto-
maticallylearnintricatepatternsindicativeofknownandpotentiallyunknown
threats,detectsubtleanomaliesthatmightevadetraditionalrule-basedsystems,
andmakepredictionsaboutfuturesecurityevents. Thesecapabilitiescantrans-
lateintosignificantpracticalbenefitsforenterprises,suchasenhancedefficiency
insecurityoperationsthroughautomation,improveddetectionratesfornovel
andevasivethreats,andbetterprioritizationofalerts. However,theadoption
andoperationalizationofMLCIinenterprisesecurityarefraughtwithsubstantial
practicalchallengesandlimitations:
* A critical dependency on large volumes of high-quality, representative
training data is a major operational limitation. Enterprises often strug-
gle with the practicalities of collecting, cleaning, labeling (especially for
supervised learning), and maintaining such datasets. Biased, incomplete,
oroutdatedtrainingdatacanleadtopoorlyperformingmodels,increased
false positives/negatives, and even discriminatory or unfair outcomes in
real-worldsecurityapplications(e.g.,inuserbehavioranalytics).

Electronics2025,14,2252 26of55
* ThesusceptibilityofMLmodelstoadversarialattacks—wheremalicious
actorsintentionallycraftinputstoevadedetection(evasionattacks)orma-
nipulatetrainingdatatocompromisemodelintegrity(poisoningattacks)—is
aseverereal-worldlimitation. ThismeanstheMLsystemsthemselvescan
becomeanattacksurface,requiringdedicateddefensivestrategiesandrobust
validation,whichaddstotheiroperationalcomplexity.
* The need for specialized data science and cybersecurity expertise to de-
velop,deploy,manage, andinterpretMLCIsolutionscreatesasignificant
skills gap. Practically, many organizations find it costly and difficult to
acquire and retain talent with this hybrid skillset, potentially leading to
over-relianceonthird-partysolutions(whichmaylacktransparency)oran
inabilitytofullyleveragethepotentialofMLtechnologies.
– TrendsandChallenges: Keytechnologicaltrendsaimtoaddresssomeofthese
limitations. There is increasing adoption of deep learning for more complex,
high-dimensionaldata,thoughthisoftenintensifiesthedataandexplainability
challenges. ResearchintoExplainableAI(XAI)iscriticalforbuildingtrustand
makingMLoutputsmoretransparentandactionableforsecuritypractitioners.
ThedevelopmentofautomatedML(AutoML)toolsseekstolowerthetechnical
barrierformodeldevelopment,potentiallymakingMLmoreaccessibletoenter-
priseswithlimitedin-housedatasciencecapabilities; however, theirpractical
limitationliesinpotentiallyproducinglessoptimizedorgeneralizablemodels
for highly specific cybersecurity tasks compared to expert-driven approaches.
Ongoing real-world challenges that significantly impact the effectiveness and
reliabilityofMLCIinenterprisesinclude
* Managingdataandconceptdrift: Securitythreatsandenterpriseenviron-
mentsconstantlyevolve,causingMLmodelstrainedonhistoricaldatatode-
gradeinperformanceovertime.Practically,thisnecessitatescontinuousmon-
itoring,frequentretraining,androbustMLOps(machinelearningoperations)
practices,whichrepresentasignificantandongoingoperationaloverhead.
* Preventingmodelpoisoningandensuringmodelrobustness: Protecting
theintegrityoftrainingdataanddevelopingmodelsresilienttoadversar-
ial manipulation are crucial for maintaining the reliability of ML-based
securitydefenses.
* Reducingalertfatiguefromfalsepositives: Despitethesophisticationof
ML,poorlytunedmodelsorthoseaffectedbydatadriftcanstillgeneratea
highvolumeoffalsealarms. Thisremainsapersistentpracticalissue,po-
tentiallyoverwhelmingsecurityteamsandleadingtogenuinethreatsbeing
overlookedifnotcarefullymanagedthroughcontinuousmodelevaluation
andthresholdtuning.
* Bridging the cybersecurity–data science skills gap: This remains a fun-
damental constraint limiting the widespread and effective adoption and
innovativeapplicationofMLCIinmanyenterprisesecurityprograms.
• Graph-BasedApproaches: Thesetechniquesweresignificantlyfeaturedin9stud-
ies[32,48,62,77,82,89,92,93,98].
– ElaborationandEvidence: GBAsleveragegraphtheorytoconstructmodelsof
enterprise environments, representing entities (e.g., network assets, users, ap-
plications, vulnerabilities) as nodes and their relationships (e.g., connectivity,
accessrights,dependencies)asedges. Thisstructurefacilitatestheanalysisof
complexattackpathways,systemicdependencies,andpotentialincidentpropa-

Electronics2025,14,2252 27of55
gationroutes. Examplesfromthereviewedliteratureincludethedevelopment
andapplicationofattackgraphstomodelpotentialmulti-stepattackscenarios
andidentifycriticalchokepoints[82,92];thecombinationofMarkovchainswith
GBAstoenablepredictivemodelingofattackprogressionandlikelihood[32];
andthedesignofspecializedgraphstructuresliketheadversarialinfluenceand
susceptibilitygraphs(AISCgraphs)forconductingcomprehensivedefensepos-
tureandvulnerabilityanalysis[48]. Whilethesestudiesdemonstratetheutilityof
GBAforspecificsecurityanalyses,itisimportanttorecognizethatthepractical
validityandreliabilityofsuchmodelsinreal-worldenterprisesettingsareheavily
contingentontheaccuracyandcompletenessofthedatausedtoconstructthe
graphandtheunderlyingassumptionsaboutentityinteractions. Translatingthe
full,dynamiccomplexityoflarge-scaleenterprisenetworksintoanaccurateand
maintainablegraphmodelremainsasignificantendeavor.
– Analysis: GBAs offer a powerful visual and analytical paradigm that can sig-
nificantlyenhanceanenterprise’sunderstandingofcomplexinterdependencies
andsystemicrisks. Practically,theyareinvaluableforattackpathanalysis,en-
ablingsecurityteamstovisualizehowattackersmighttraversethenetworkto
reachcriticalassets,andforvulnerabilitymanagement,byhelpingtoprioritize
remediation efforts based on exploitability and potential impact. This visual
andrelationalcontextcanleadtomoreinformedandproactivesecuritydecision
making. However,thepracticalapplicationofGBAinenterprisesfacesnotable
limitationsandchallenges.
* ComplexityofConstructionandMaintenance:Constructingand,morecriti-
cally,maintainingaccurate,large-scalesecuritygraphsisacomplexandoften
computationallyintensivetask. Theinitialdatacollection,entitydiscovery,
relationshipmapping,andvulnerabilityattributioncanrequiresignificantef-
fortandintegrationwithmultipledatasources. Inhighlydynamicenterprise
environmentswhereassets,configurations,andsoftwareversionschange
frequently, keeping the graph model current is a continuous operational
challenge. Anoutdatedgraphquicklylosesitsanalyticalvalueandcanlead
tomisleadingconclusions.
* Scalability for Large Enterprises: As enterprise networks grow, the size
andcomplexityofthecorrespondingsecuritygraphscanbecomeimmense.
Scalability,intermsofgraphstorage,processingpowerrequiredforcomplex
queries(e.g.,pathfinding,centralityanalysis),andtimelyupdates,canbea
significantpracticalconcern. Forverylargeorganizations,thismaynecessi-
tateinvestmentinspecialized(andpotentiallyexpensive)graphdatabase
technologiesordistributedprocessingframeworks.
* Data Quality and Completeness Dependencies: The utility of any GBA
is fundamentally dependent on the quality, accuracy, and completeness
of the input data used to build the graph. Incomplete asset inventories,
inaccuratevulnerabilityinformation,ormissingrelationshipdatacanlead
toanincompleteormisleadingrepresentationoftheactualattacksurface,
therebylimitingthereal-worldreliabilityoftheanalysis.
– TrendsandChallenges: CurrenttrendsinGBAforsecurityincludetheintegra-
tionofGBAwithmachinelearning(ML)techniquesfordynamicgraphanalysis,
aimingtoautomaticallydetectanomaliesorpredictchangeswithingraphstruc-
turesthatmightindicateemergingthreats(asseeninapproacheslike[77]). This
hasthepracticalimplicationofpotentiallymakinggraphsmoreadaptiveand
responsivetoevolvingconditions,butalsointroducestheinherentcomplexities

Electronics2025,14,2252 28of55
ofML(e.g.,datarequirementsandinterpretability). Anothertrendisthedevelop-
mentofgraphdatabasesspecificallyoptimizedforhandlingthescaleandquery
patternsofsecurity-relateddata,whichcouldalleviatesomescalabilityconcerns.
Despitetheseadvancements,significantreal-worldchallengespersist.
* AchievingReal-TimeGraphAnalyticsatEnterpriseScale:Manycritical
security use cases, such as detecting an ongoing attack as it propagates or
assessingtheimmediateimpactofanewhigh-severityvulnerability,require
real-timeornearreal-timeanalyticalcapabilities. Thecomputationalcostof
continuouslyupdatingandperformingcomplexqueriesonmassivegraphsin
realtimeremainsamajortechnicalandpracticalhurdleformostenterprises.
* Standardizing Graph Modeling Approaches for Security: The lack of
widelyadopted,standardizedschemas,ontologies,ormodelinglanguages
forrepresentingsecurity-relevantentitiesandrelationshipsingraphsmakes
itdifficulttosharegraphmodels,compareresultseffectivelyacrossdifferent
GBA tools or research studies, and seamlessly integrate GBA with other
securityinformationsystems. Practically,thisfragmentationhindersinter-
operability and the development of a mature ecosystem of reusable GBA
componentsandbenchmarks.
• BehavioralAnalysisandProfiling: Thiscategoryofanalyticaltechniqueswaspromi-
nentinsixofthereviewedstudies[33,47,55,66,79,94].
– ElaborationandEvidence: BAPfocusesonunderstanding,modeling,andulti-
matelypredictingtheactionsandpatternsofbehaviorexhibitedbyusers,systems,
networkentities,andpotentialattackers. Thereviewedliteratureshowcasestech-
niquessuchasMulti-DimensionalBehavioralAnalytics,whichconsidersdiverse
aspectslikeloginfrequency,resourceaccesspatterns,anddatatransfervolumes
tobuildcomprehensiveprofiles[33];theanalysisofhistoricalattackbehaviors
andattackerTactics,Techniques,andProcedurestopredictfuturethreatvectors
orcampaigncharacteristics[79]; andtheapplicationofbehavior-basedintelli-
gence,whichmodelspastlegitimatebehaviortoidentifystatisticallysignificant
anomaliespotentiallyindicativeofcompromiseorinsideractivity[66].Thepracti-
calreliabilityofBAPtechniquesoftenhingesonthequalityandgranularityofthe
datasourcesusedforprofiling(e.g.,endpointlogs,networktraffic,application
logs), the sophistication of the anomaly detection algorithms employed, and,
critically,thestabilityandpredictabilityofwhatconstitutes“normal”behavior
withinthemonitoredenvironment.
– Analysis: TheincreasingadoptionofBAPinenterprisesreflectsastrategicshift
towardsdetectingthreats,suchasinsiderthreatsandAPTs,thatarespecifically
designed to evade traditional signature-based defenses, often by mimicking
legitimateuserorsystembehavior. BAPenablesmoreuser-centricandcontext-
awaresecuritymonitoring. Thiscanleadtomoreaccuratethreatidentificationby
tailoringdetectiontoindividualuserroles,responsibilities,andtypicalactivity
patterns,therebypotentiallyreducingthehighvolumeoffalsepositivesoften
associatedwithgenericsecurityrules. Italsoprovidesrichcontextualdatacrucial
forforensicinvestigations. However,theimplementationofBAPisaccompanied
bysignificantpracticallimitations.
* EstablishingandMaintainingAccurateBehavioralBaselines: Thisisar-
guablythemostsubstantialchallenge. Inlarge, diverse, anddynamicen-
terpriseenvironmentswithevolvingjobroles,frequentpersonnelchanges,
andnewapplicationdeployments,“normal”behaviorisaconstantlymoving

Electronics2025,14,2252 29of55
target. The initial baselining period required to learn these norms can be
lengthyandresource-intensive. Moreimportantly,maintainingtheaccuracy
of these baselines necessitates continuous learning, adaptation, and peri-
odicre-evaluation,whichiscomputationallydemandingandoperationally
complex. Failuretodosoinpracticeleadstodegradedmodelperformance,
resultingineitherexcessivefalsepositivealertsor,conversely,misseddetec-
tionsofgenuinethreats.
* DataVolumeandGranularityRequirements: EffectiveBAPoftenrequires
thecollectionandanalysisofvastquantitiesofgranulardatafrommultiple
sources. Thispresentschallengesrelatedtodatastorage,processingpower,
andthepotentialperformanceimpactonmonitoredsystemsornetworks.
* PrivacyandEthicalConsiderations: Thedetailedcollectionandanalysisof
userandsystembehaviordatainherentlyraisesignificantprivacyconcerns.
Enterprisesmustpracticallynavigatecomplexlegalframeworks(e.g.,GDPR,
CCPA,andlocallaborlawsconcerningemployeemonitoring)andethical
considerations. Implementing BAP necessitates the development of clear
governancepolicies,ensuringtransparencywithusersregardingwhatdata
iscollectedandforwhatpurpose(whereappropriateandlegallyrequired),
employing robust data anonymization or pseudonymization techniques
whenfeasible,andimplementingstringentaccesscontrolsandaudittrails
to prevent misuse of sensitive behavioral data. These considerations can
significantlyinfluencethescopeandmethodologyofBAPdeployment.
– TrendsandChallenges: BAPisacoretechnologicalcomponentofmodernUEBA
platformsandisincreasinglybeingintegratedwithIdentityandAccessManage-
ment(IAM)systems. Thisintegrationhasthepracticalimplicationofenabling
moredynamic,risk-basedauthenticationandadaptiveaccesscontrols(e.g.,re-
quiringstep-upauthenticationorrestrictingaccessifauser’sbehaviorsuddenly
deviatessignificantlyfromtheirestablishedprofile). Despitetheseadvancements,
severalpersistentreal-worldchallengeslimittheuniversaleffectivenessandease
ofBAPdeployment:
* MinimizingFalsePositivesandAlertFatigue: WhileBAPaimsforhigher
accuracy, poorly tuned systems, inadequate baselining, or a failure to ac-
countforlegitimatebehavioralvariancescanstillgenerateahighnumberof
falsepositivealerts. Thisremainsacriticaloperationalchallenge,asitcan
overwhelmSOCanalysts,leadingtoalertfatigue,alossoftrustintheBAP
system,andultimately,theriskofgenuinethreatsbeingoverlooked.
* Adapting Baselines to Dynamic Organizational Contexts: As noted, ef-
fectivelyandefficientlyadaptingbehavioralbaselinestoreflectlegitimate
changesinuserroles,responsibilities,businessprocesses,andITsystems
is an ongoing practical and technical hurdle. This requires sophisticated
adaptivealgorithmsandpotentiallysignificantcomputationalresourcesfor
continuousmodelretrainingandvalidation.
* EthicalImplicationsofContinuousMonitoringandPotentialforMisinter-
pretation: Beyondlegalprivacycompliance,thecontinuousmonitoringin-
herentinBAPraisesbroaderethicalquestionsaboutworkplacesurveillance
andthepotentialformisinterpretationofautomaticallyflagged“anomalies”,
which could unfairly impact individuals. Enterprises must carefully bal-
ancelegitimatesecurityneedswiththeirethicalobligationstoemployees,
ensuring fairness, transparency, and mechanisms for redress. This often

Electronics2025,14,2252 30of55
necessitates clear communication strategies and robust oversight of BAP
systemoutputsandsubsequentactions.
• Modeling Techniques: Various modeling techniques were explored in six of the
reviewedstudies[36,42,58,91,97,101].
– ElaborationandEvidence: Thiscategoryencompassesconceptualormathemati-
calrepresentationsofsystems,threats,orsecurityprocesses,designedtofacilitate
understanding, riskassessment, andprediction. Examplesfromtheliterature
includegeneralthreatmodelingmethodologies,theapplicationoftheSTRIDE
threatmodel(STRIDEisamodelofthreatsdevelopedatMicrosoft,usedtoiden-
tifyandcategorizepotentialthreatstoasystem.Seehttps://learn.microsoft.com/
en-us/azure/security/develop/threat-modeling-tool-threats (accessed on 29
April2025)),leveragingtheMITREATT&CKframeworkfordescribingadversary
tacticsandtechniques,andmodel-basedbehaviorprediction.
– Analysis: MT provides structured methodologies that can aid enterprises in
proactivelyidentifyingsystemvulnerabilitiesandunderstandingpotentialattack
vectors. Frameworks like MITRE ATT&CK offer a valuable common lexicon,
improvingcommunicationwithinthecybersecuritycommunityandenabling
moreconsistentthreatintelligencesharing. Theprimarypracticalimplication
is a more systematic and potentially proactive approach to risk management.
However,akeylimitationisthatallmodelsareabstractionsandmaynotcapture
the full complexity or dynamic nature of real-world enterprise environments.
Thisnecessitatescontinuous,resource-intensiveupdatingtomaintaintheirrele-
vanceandaccuracy,failingwhichtheyriskprovidingafalsesenseofsecurityor
misdirectingdefensiveefforts.
– Trends and Challenges: A strong trend is the increasing operationalization
of the MITRE ATT&CK framework within security operations for detection
engineering, threat hunting, and incident response. Automated tools are also
morefrequentlyusedtosupportthethreatmodelingprocess,offeringefficiency
gains. Theprimarychallengeslieinkeepingthesemodelscontinuouslyupdated
in parallel with the rapidly evolving threat landscape and the organization’s
own IT changes. Furthermore, effectively integrating model outputs into the
broadersecurityanalyticslifecycle(e.g.,linkingthreatmodelfindingstoSIEM
alertcorrelationorSOARplaybooktriggers)remainsanissuerequiringcareful
planningandtechnicalintegration.
• OntologiesandKnowledgeGraphs: Thesemethods,employingstructuredknowl-
edgeframeworks,werediscussedinfourofthereviewedstudies[61,74,99,102].
– ElaborationandEvidence: OKGtechniquesutilizeformal,structuredrepresen-
tationsofknowledge—definingentities,theirproperties,andtherelationships
betweenthem—toenhancesecurityanalysisandreasoning. Examplesinclude
Ontology-BasedAutomatedPenetrationTesting,whereontologiesguidethese-
lectionandapplicationoftestingtools[61],andtheuseofknowledgegraphsto
mapsecurity-relevantentities(e.g.,assets,vulnerabilities,threatactors,TTPs)and
theirinterconnectionsforadvancedthreatdetectionandincidentresponse[74].
TheeffectivenessofOKG-drivensecurityanalyticsishighlydependentonthe
quality,completeness,andconsistencyoftheunderlyingontologyorknowledge
graph,aswellasthesophisticationofthereasoningenginesappliedtothem.
– Analysis: OKGsofferthepotentialforrichersemanticunderstandingofcom-
plexsecuritydata,improvedautomatedreasoningcapabilities,andenhanced
automationofsecuritytasks. Theycanhelptointegratediversedatasourcesinto

Electronics2025,14,2252 31of55
aunifiedmodelandprovideamoreholistic,context-awareviewoftheenterprise
securitylandscape. However,thelimitationsarethesignificantcomplexityand
substantialeffortinvolvedindeveloping,meticulouslymaintaining,andcontin-
uouslypopulatingcomprehensivesecurityontologiesandknowledgegraphs.
Thisrequiresspecializedexpertise(e.g.,ontologists,knowledgeengineers,cyber-
securitydomainexperts),considerabletimeinvestment,androbustgovernance
processes,makingtheROIdifficulttojustifyforsomeorganizations.
– TrendsandChallenges: Emergingtrendsinvolveleveragingnaturallanguage
processing (NLP) and large language models (LLMs) to assist in the semi-
automatedconstructionandqueryingofsecurityknowledgegraphs,potentially
reducingthemanualeffortinvolved. Effortstowardscreatingstandardizedsecu-
rityontologiesalsoaimtoimproveinteroperabilityandreusability. Despitethese
trends,significantchallengeswithinteroperabilitybetweendifferentOKGsys-
temsandensuringthescalabilityofthesecomplexstructuresforlarge,dynamic
enterpriseenvironmentspersist,limitingbroaderadoption.
• FoundationalDataManagementandRepresentationTechniques: Whilenotstrictly
analysistechniquesthemselves,effectiveDMRpractices,highlightedinstudiessuch
as [41,47,64] (three studies focusing on these aspects), are crucial enablers for any
advancedsecurityanalytics.
– Elaboration and Evidence: This category includes critical infrastructure com-
ponentssuchasIn-MemoryDataManagementforaccelerateddataprocessing
andenablingreal-timeanalyticscrucialfortimelyincidentresponse[41,47],as
wellaseffectivedatarepresentationtechniques,includingadvancedvisualiza-
tionmethods,forformattingandpresentingcomplexsecuritydatainwaysthat
aid human interpretation and pattern identification [64]. The choice of DMR
techniquesinvolvestrade-offsregardingcost,performance,scalability,andim-
plementationcomplexity.
– Analysis: EfficientDMRisfundamentaltotheoverallperformance,reliability,
and utility of any enterprise security analytics system. Practically, slow data
access,poordataquality,orineffectivevisualizationcanseverelyhamperthreat
detection, incident investigation, and response capabilities, regardless of the
sophisticationoftheanalyticalalgorithmsemployed. Theclearimplicationis
thatstrategicinvestmentinrobustdatainfrastructure(includingstorage, pro-
cessing, and integration capabilities) and user-centric visualization tools is as
criticaltosuccessfulsecurityanalyticsastheanalyticalmodelsthemselves. Akey
limitationforsomeorganizationscanbethecostandcomplexityassociatedwith
implementingandmaintainingstate-of-the-artDMRinfrastructureandacquiring
thenecessarydataengineeringskills.
– TrendsandChallenges: Currenttrendsincludetheincreasingadoptionofbig
dataplatforms(e.g.,datalakes,datalakehouses)specificallyforsecuritydatato
handlevolumeandvariety,alongsideadvancedinteractivevisualizationtools
designedtomakecomplexdatamoreaccessibletoanalysts. Persistentchallenges
involve managing the sheer scale of security data generated daily, ensuring
consistentdataqualityandgovernanceacrossdiversesources,andeffectively
presenting complex analytical outputs in an intuitive, actionable, and timely
mannerforoftenoverburdenedsecurityanalysts.
Insummary,thelandscapeofsecurityanalyticstechniquesisdominatedbyMLCI
and GBA, driven by their power in handling complex, large-scale data and modeling
intricate relationships inherent in modern cyber threats. The increasing prominence of
BAPhighlightsashifttowardsunderstandinguserandentitybehaviors,whileMTand

Electronics2025,14,2252 32of55
OKGprovidestructuredandsemanticdepth. Thesetrendssuggestamovetowardsmore
intelligent,interconnected,andcontext-awaresecurityanalytics. Futureadvancementswill
likelyfocusonhybridapproaches,combiningthestrengthsofthesediversetechniques—for
instance,MLCIwithBAPfornuancedanomalydetectionorGBAwithOKGforcomprehen-
sive,semanticallyenrichedsecuritypostureanalysis—tobuildmoreresilientandadaptive
enterprisedefensemechanisms. Thecontinuousevolutionofthesetechniquesisessential
tokeeppacewiththeever-advancingcapabilitiesofcyberadversaries.
Observation6(Ob6): TheComplementaryRolesofQuantitativeandQualitative
Analysis,withOpportunitiesforIncreasedMixed-MethodsIntegration
Ourreviewindicatesthatenterprisesecurityanalyticsresearchutilizesbothquantita-
tiveandqualitativemethodologiestoassessandunderstandcyberthreats,vulnerabilities,
and incidents [103]. Quantitative analysis, focusing on numerical data and statistical
evaluation, appears frequently for measuring security events and control effectiveness.
Qualitativeanalysisprovidesessentialcontextualunderstandingandinsightintocomplex,
non-numericalaspects. Whilebotharevalued,theexplicitadoptionofmixed-methodsap-
proaches,integratingthestrengthsofboth,waslesscommonlyhighlightedinthereviewed
studies,suggestingapotentialavenuefordevelopingmoreholisticandrobustresearch
findingsinthefield.
• QuantitativeAnalysisinSecurityAnalytics:
– ElaborationandEvidence: Thisapproachcentersontheuseofnumericaldata,
statistical methods [86], and computational techniques to measure [57], quan-
tify,andobjectivelyevaluatesecurity-relatedphenomena[92]. Itofteninvolves
analyzingmetricssuchasthefrequencyandimpactofsecurityincidents[32],
thefinancialcostofbreaches,ortheperformanceofsecuritycontrols[38]. Forin-
stance,studieshaveemployedGameTheoryandstochasticmodelingtoquantify
outcomesofsecuritystrategies[31],orcomputationalintelligenceandprogram-
minglanguageslikeRtodevelopanumericalunderstandingofthreats[90].
– Analysis: Quantitativeanalysisisvitalforenterprisestoprioritizerisks,justify
security investments, allocate resources effectively, and make data-driven op-
erationaldecisions. Itsstrengthslieinitsobjectivity,potentialforautomation,
and the comparability of results. However, its effectiveness can be limited by
theneedforlargevolumesofhigh-qualitydataandaninabilitytofullycapture
nuanced, unmeasurable, or emergent aspects of security concerns, such as at-
tackerintentorthesubtletiesofhumanbehavior[90]. Anover-relianceonpurely
quantitativemetricscansometimesleadtoanarrowunderstandingofacomplex
anddynamicthreatlandscape.
– TrendsandChallenges:ThetrendtowardsBigDataanalyticsandAI/ML(asdis-
cussedinObservation5)heavilyfuelsquantitativesecurityanalysisbyenabling
the processing of vast datasets for anomaly detection, predictive risk scoring,
andautomatedresponse. Challengesincludeensuringthequalityandintegrity
ofinputdataforthesemodels,avoiding“metricfixation”,managingalertfatigue
frompurelyquantitativesystems,anddevelopingquantitativemodelsthatare
trulyrepresentativeofreal-worldsecurityeffectiveness.
• QualitativeAnalysisinSecurityAnalytics:
– ElaborationandEvidence: Qualitativeanalysisemphasizessubjectiveinforma-
tion,in-depthcontextualunderstanding,andexpertjudgment[103]. Itinvolves
gatheringandinterpretingnon-numericaldatasuchastextualdescriptionsfrom
incidentreports,interviewdatawithsecuritypersonnel,observationalstudiesof
securityoperations[102],ordetailedcasestudies. Examplesincludemodel-based

Electronics2025,14,2252 33of55
qualitative analysis to understand threat intricacies [36] and the use of threat
modelingframeworkslikeSTRIDEcombinedwiththreattreeanalysistoexplore
vulnerabilities[91].
– Analysis: Thisapproachisinvaluableforuncoveringhiddenpatterns, under-
standing the “why” behind security events, exploring behavioral indicators,
identifyingemergingthreatsnotyetquantifiable[74],andassessingtheusability
andpracticaleffectivenessofsecurityprocesses. Itprovidesrichnessanddepth
thatquantitativedataalonecannot. However,qualitativefindingscanbesubject
toresearcherinterpretationandpotentialbiases,maybemoretime-consuming
tocollectandanalyze,andareoftenlessgeneralizablethanquantitativeresults.
Forenterprises,qualitativeinsightsarecrucialfordevelopingtargetedtraining,re-
finingincidentresponseplansbasedonreal-worldscenarios,andunderstanding
thesocio-technicalaspectsofsecurity.
– Trends and Challenges: Trends include the increasing use of NLP to extract
insightsfromunstructuredqualitativedata(e.g.,threatintelligencereportsand
user feedback). Qualitative methods are also central to usability studies for
security tools and understanding human factors in cybersecurity. Challenges
involvethedifficultyofscalingqualitativeanalysis,integratingitsfindingswith
quantitativedatasystemsinameaningfulway,andensuringrigorinqualitative
datacollectionandinterpretation.
• Mixed-MethodsAnalysisinSecurityAnalytics:
– ElaborationandEvidence: Amixed-methodsapproachstrategicallycombines
quantitativeandqualitativetechniquestoleveragethestrengthsofboth,aiming
foramorecomprehensiveandnuancedunderstanding. Thereviewedliterature
explicitlyhighlightedseveralstudiesadoptingthisintegratedmethodology(see
Table4)togainamoreholisticperspectiveontheirresearchquestions.
– Analysis: Mixed-methodsresearchcanprovidestrongervalidationoffindings
throughtriangulation,offerdeeperinsightsbyexplainingquantitativeresults
with qualitative data (or vice-versa), and lead to more robust and actionable
conclusions. Therelativelylimitedexplicitmentionofmixed-methodsstudies
in the enterprise security analytics literature could indicate a methodological
gaporanareawhereinresearchpracticescouldbemoreexplicitlyarticulated.
Encouragingmoremixed-methodsresearchcouldsignificantlyenhancethedepth,
relevance,andpracticalapplicabilityofsecurityanalyticsstudies. Forenterprises,
thistranslatestotheabilitytocombine‘what’ishappening(fromquantitative
data) with ‘why’ it’s happening (from qualitative insights) for more effective
securitystrategies.
– TrendsandChallenges: Theincreasingcomplexityofcybersecurityproblems
inherently calls for multifaceted analytical approaches. The development of
XAIcanbeseenasamovetowardsbridgingquantitativemodeloutputswith
qualitativehuman-understandableexplanations,embodyingamixed-methods
spirit. The primary challenge is the increased complexity in research design,
datacollection,analysis,andinterpretation,requiringresearchersproficientin
bothparadigms.

Electronics2025,14,2252 34of55
Inconclusion,Observation6highlightsthatwhilebothquantitativeandqualitative
analysesprovidedistinctandvaluableperspectivesinenterprisesecurityanalytics,amore
deliberateandwidespreadadoptionofmixed-methodsapproachescouldfosterdeeper
insights and more comprehensive solutions. Enterprises stand to benefit most when
they can leverage the precision of quantitative data alongside the contextual depth of
qualitative understanding to inform their security posture management and decision-
makingprocesses.
Observation7(Ob7): EnterpriseSecurityAnalyticsStrategiesareEvolvingTowards
ProactiveandPredictivePostures
Our systematic review reveals a clear evolution in strategic approaches to enter-
prise security analytics. While all identified strategies—detective, reactive, proactive,
andpredictive—servedistinctpurposes,theliteratureindicatesasignificanttrendmoving
beyondprimarilyreactivetacticstowardsmoreforward-thinking,anticipatorymeasures.
Thisshiftisunderscoredbytheprevalenceofstudiesfocusingonproactive(40studies)
andpredictive(22studies)strategies,althoughdetectiveapproaches(27studies)remain
a cornerstone. Reactive strategies (5 studies) are recognized as necessary but are less
emphasizedincurrentresearchonanalytics-drivensecurity.
• ElaborationandEvidenceofStrategicApproaches:
– ReactiveStrategy: Thistraditionalstrategyinvolvesrespondingtosecurityin-
cidentsaftertheyhaveoccurred,withtheprimarygoalsofdamagemitigation
andrapidrecovery. Activitiesincludeclosingexploitedvulnerabilities,eradicat-
ingmalware,andrestoringsystems. Whileessentialforincidentmanagement,
thisstrategy’sinherentnaturesignifiesapriorfailureinpreventionordetection.
Inourreviewedliterature,thenumberofstudiesthatconcentratedprimarilyon
developingorapplyinganalyticaltechniquesspecificallyforthisreactivephase
wascomparativelylow(fivestudies—[41,53,66,68,74]). Thisobservationsuggests
thatwhileanalyticsforreactivemeasuresareexplored,themainthrustofresearch
insecurityanalyticstendstofavorearlierinterventionpoints—suchasproactive,
predictive,anddetectivecapabilities—aligningwiththebroadercybersecurity
goalofminimizingthreatimpactbeforeextensivereactionisneeded.
– DetectiveStrategy: Thisstrategyiscriticallyfocusedonthetimelyidentification
ofsecurityincidentseitherastheyareactivelyunfoldingorveryshortlyafter
theiroccurrence.Theprimaryobjectiveistominimizethedwellingtimeofthreats
withintheenterpriseenvironment. Itreliesonafoundationofrobustsystemsfor
continuousmonitoring,comprehensiveloggingfromdiversesources(suchas
networkdevices,servers,endpoints,andapplications)andsophisticatedalerting
mechanisms. These components work in concert to flag anomalous patterns,
suspiciousactivities,orknownindicatorsofcompromise(IoCs)thatcouldsignal
anongoingorimminentattack[45,60,63,73,78]. Keytechnologiesoftenunder-
pinningthisstrategyincludeSIEMplatforms,IntrusionDetection/Prevention
Systems(IDS/IPS),andEDRsolutions. Securityanalyticsplaysapivotalrole
here by automating the analysis of vast data volumes, correlating disparate
events to uncover complex attack chains, and employing techniques ranging
fromsignature-baseddetectionandrule-basedcorrelationtoadvancedstatistical
anomalydetectionandmachinelearningmodelsforidentifyingnovelorevasive
threats. With27studiesinourreviewemphasizingthisapproach,itsimportance
inprovidingcrucial,timelyawarenessforimmediateandeffectiveincidentre-
sponseiswellestablished,forminganindispensablelayerinadefense-in-depth
securitystructure.

Electronics2025,14,2252 35of55
– ProactiveStrategy: Thisstrategyembodiesaforward-lookingsecurityphiloso-
phyfocusedontakingpreemptivemeasurestopreventcyberthreatsfrommate-
rializing,therebyreducingtheoverallattacksurfaceandstrengtheningdefenses
beforeanattackisattempted. Itmovesbeyondmerelyreactingtoincidentsby
systematicallyidentifyingandmitigatingvulnerabilitiesandfortifyingsecurity
postures. Coreactivitiesincludecomprehensiveandcontinuousriskassessments,
includingthreatmodelingtoanticipatepotentialattackvectors;regularsecurity
auditstoensurecomplianceandidentifyweaknesses;diligentsystemhardening
(e.g.,removingunnecessaryservices,configuringsecurebaselines,implementing
robust access controls); timely and prioritized patch management to address
knownvulnerabilities;andengagingsecurityawarenesstraining,oftenincorpo-
ratingphishingsimulations,tomitigatehumanerror. Furthermore,developing
andtestingrobustincidentresponseplansisakeyproactivestep,ensuringpre-
parednesstominimizedamageshouldanincidentoccurdespitepreventative
efforts[46,48,80,86,92]. Analyticscansupportproactivestrategiesby,forinstance,
prioritizingvulnerabilityremediationbasedonexploitlikelihoodandassetcrit-
icality, or by identifying anomalous configurations that deviate from security
bestpractices. Asthemostfrequentlyemphasizedstrategyinthereviewedlit-
erature(40studies),ithighlightsaclearstrategicpreferencewithinthefieldfor
preventingincidents,anapproachthatisdemonstrablymorecost-effectiveand
lessdisruptivetoenterpriseoperationsthanreactingtosuccessfulbreaches.
– PredictiveStrategy: Representingthemostadvancedandaspirationalsecurity
posture,thisstrategyaimstoforecastpotentialfuturethreatsandanticipateat-
tack campaigns, often before they are widely known or actively launched. It
leveragessophisticatedanalyticaltechniques,primarilyMLandAI,toanalyze
vastdatasetscomprisingobservedpatternsfromhistoricalincidents,real-timese-
curitytelemetry,globalthreatintelligencefeeds,darkwebmonitoring,andeven
geopoliticalorsector-specificriskfactors. Unlikeproactivestrategiesthatharden
defensesagainstknownvulnerabilityclassesorgeneralthreats,predictivean-
alyticsseekstoidentifythelikelihoodofspecificfutureattacktypes,emerging
malicious tools, or targeted campaigns, enabling organizations to adapt their
defensespreemptivelyandinahighlytargetedmanner[37,67,75,79,84]. Thegoal
istoneutralizethreatsbeforetheycancauseharmbyprovidingearlywarnings
andactionableintelligence. Whileimmenselypowerfulinconcept,thisapproach
faceschallengessuchastheneedforhigh-quality,voluminousdata,theriskof
falsepositives/negativesinpredictions,ensuringtheexplainabilityofAI-driven
insights, and staying ahead in an adversarial landscape where attackers also
evolvetheirtactics. Nevertheless,thesignificantresearchattentiongiventopre-
dictivestrategies(22studies)underscoresastrongindustry-wideaspirationto
achievethisforward-lookingcapability,strivingtoshiftfromareactiveormerely
preventativestancetooneoftruecyberforesight.
• AnalysisoftheStrategicShift: Theobservedstrategicevolutionisdrivenbyseveral
factors,includingtheincreasingvolume,sophistication,andbusinessimpactofcyber
threats. Purelyreactiveapproachesarenolongersustainableorcost-effectiveinthe
faceofadvancedpersistentthreatsandrapidexploitdevelopment.

Electronics2025,14,2252 36of55
– Value Proposition: Proactive and predictive strategies offer the potential to
significantly reduce the likelihood and impact of security incidents, thereby
enhancingbusinessresilienceandtrust. Detectivecapabilitiesremaincriticalasa
bridge,providingthenecessaryalertswhenpreventativemeasuresarebypassed.
– Interdependencies: Effectivesecurityreliesonabalancedcombinationofthese
strategies. Forinstance,detectivemechanismsprovidedatathatcanrefineproac-
tivecontrolsandtrainpredictivemodels. Arobustproactiveposturereducesthe
burdenondetectiveandreactivesystems.
– EnterpriseImpact:Thisstrategicshiftnecessitateschangesinorganizationalculture,
processes, andtechnologyadoption. Itrequiresinvestmentinadvancedanalyt-
icaltools(asmentionedintheOb5ontechniqueslikeMLCI),skilledpersonnel,
andcomprehensivethreatintelligence.Theemphasisonproactivestrategiesalso
impliesagreaterneedforthoroughriskassessmentsandpreventativemaintenance.
– Challenges: While proactive and predictive strategies are aspirational, their
implementationfaceshurdles. Predictiveanalytics,forexample,demandshigh-
qualitydata,sophisticatedmodeling(whichcanbea“blackbox”),andcarries
theriskoffalsepositivesornegatives. MeasuringtheROIofproactivemeasures
canalsobemorechallengingthanquantifyingthecostofapreventedincident.
• TrendsandChallenges:
– EnablingTechnologies: TheriseofBigDataplatforms,advancedAI/MLalgo-
rithms(especiallydeeplearning),andcloudcomputingpowerarekeyenablersof
moreeffectivedetective,proactive,andparticularlypredictivestrategies. SOAR
platforms are enhancing detective and reactive capabilities by automating re-
sponses. ThreatIntelligencePlatforms(TIPs)arecrucialforinformingproactive
defensesandpredictivemodels.
– EmergingParadigms: Conceptslikezero-trustarchitectureembodyaproactive
stance by default. The push for “security by design” also aligns with proac-
tivethinking.
– Persistent Hurdles: Challenges include managing the vast amounts of data re-
quired,addressingthecybersecurityskillsgap(especiallyfordatascientistsandAI
specialistsinsecurity),integratingdiversesecuritytoolsanddatasources,ensuring
theexplainabilityandtrustworthinessofpredictivemodels,andkeepingpacewith
the adversarial use of AI. The cost of implementing and maintaining advanced
analyticssolutionsalsoremainsasignificantbarrierforsomeorganizations.
Insummary,Observation7underscoresasignificantmaturationincybersecuritystrat-
egywithinenterprises,characterizedbyadecisiveshiftfromreactiveresponsestowards
proactivepreventionandpredictiveforesight. Whiledetectivecapabilitiesareindispens-
ableandreactivemeasuresremainanecessaryfallback,theclearmomentumistowards
leveragingadvancedanalyticstoanticipateandneutralizethreatsearlierintheattacklife-
cycle. Anoptimaldefenseposturefortheevolvingthreatlandscapeinvolvesanintelligent,
adaptive,andbalancedintegrationofallthesestrategicelements.
Thefollowingtable(Table5)summarizestheevaluationmethodsemployedforthe
securityanalyticapproachesdiscussedinthereviewedliterature,alongwiththepotential
securityriskstheseapproachesaimtoaddress. Itisimportanttonotethatsomestudies
were not included in this table if their evaluation methods were not explicitly detailed
orwereinsufficientlyclearforcategorization. Thistableprovidesinsightsintohowthe
effectivenessandapplicabilityofvarioussecurityanalyticssolutionsarebeingassessed
inresearch.

Electronics2025,14,2252
37of55
Table5.Enterprisesecurityanalyticevaluationmethods.
EvaluationMethod
Study Experiment Case Real-World Comparison PotentialSecurityRisks
|        | /Simulation | Study | Scenario | withOthers |     |                             |     |
| ------ | ----------- | ----- | -------- | ---------- | --- | --------------------------- | --- |
| S1[41] | ✓           |       |          |            |     |                             | –   |
| S2[42] |             | ✓     |          |            |     |                             | –   |
| S3[43] |             |       |          |            |     | Multi-stepnetworkintrusions |     |
✓
| S4[31] |     |     |     |     |                                               |     | Illegalintrusions |
| ------ | --- | --- | --- | --- | --------------------------------------------- | --- | ----------------- |
|        | ✓   | ✓   |     |     |                                               |     |                   |
| S5[32] |     |     |     |     |                                               |     | –                 |
|        |     | ✓   | ✓   | ✓   |                                               |     |                   |
| S6[34] |     |     |     |     |                                               |     | –                 |
| S7[33] |     |     |     |     |                                               |     | APTs              |
| S8[35] |     | ✓   |     |     |                                               |     | –                 |
| S9[36] |     | ✓   |     |     | Insiderattacks;unauthorizedaccess;dataleakage |     |                   |
STRIDE:Spoofing,Tampering,Repudiation,InformationDisclosure,
| S10[91] |     | ✓   |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
DenialofService,ElevationofPriviledge
|         | ✓   | ✓   |     |     |     |                   |     |
| ------- | --- | --- | --- | --- | --- | ----------------- | --- |
| S11[98] |     |     |     |     |     | Gainingrootaccess |     |
✓
| S12[87] |     |     |     |     |     |     | –   |
| ------- | --- | --- | --- | --- | --- | --- | --- |
✓
| S13[53] |     |     |     |     |     | DistributedDenial-of-Service |     |
| ------- | --- | --- | --- | --- | --- | ---------------------------- | --- |
✓
| S14[83]  |     |     |     |     | Administratorpasswordtheft;insiderattack         |                              |                   |
| -------- | --- | --- | --- | --- | ------------------------------------------------ | ---------------------------- | ----------------- |
| S15[61]  |     |     |     |     |                                                  | Multistageattacks&APTs       |                   |
| S16[82]  |     | ✓   |     |     |                                                  | Unauthorizedactivity         |                   |
| S18[71]  |     |     | ✓   |     | Jail-breaking;maliciouscarrierID;unusuallocation |                              |                   |
| S19[88]  |     | ✓   |     |     | Internal,external,andaccidentalthreats           |                              |                   |
| S20[99]  |     | ✓   | ✓   |     |                                                  |                              | Illegalintrusions |
|          | ✓   | ✓   |     |     |                                                  |                              |                   |
| S21[62]  |     |     |     |     |                                                  | SQLinjection;XSS;DoSattacks  |                   |
|          | ✓   |     | ✓   |     |                                                  |                              |                   |
| S22[90]  |     |     |     |     | Portscanning;networkscanning;brute-forceattacks  |                              |                   |
|          |     | ✓   | ✓   | ✓   |                                                  |                              |                   |
| S24[100] |     |     |     |     |                                                  |                              | –                 |
|          | ✓   |     | ✓   |     |                                                  |                              |                   |
| S26[94]  |     |     |     |     |                                                  |                              | Malware           |
|          | ✓   | ✓   |     |     |                                                  |                              |                   |
| S29[95]  |     |     |     |     |                                                  | Stuxnetworm&phishingcampaign |                   |
Bruteforce;replayattacks;authenticationfailures;sharedaccess
| S30[47] | ✓   |     | ✓   |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- |
abuse
| S31[55]  |     |     | ✓   |     |     | Users’abnormalbehaviours |              |
| -------- | --- | --- | --- | --- | --- | ------------------------ | ------------ |
| S33[104] |     |     |     | ✓   |     |                          | –            |
| S34[56]  | ✓   |     |     | ✓   |     |                          | Malware;DDoS |
✓
| S35[102] |     |     |     |     | Multistage&Multihostattackscenarios |     |     |
| -------- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
✓
| S36[63] |     |     |     |     |                                                    |                         | Abnormalaccess |
| ------- | --- | --- | --- | --- | -------------------------------------------------- | ----------------------- | -------------- |
|         | ✓   |     | ✓   |     |                                                    |                         |                |
| S37[73] |     |     |     |     |                                                    | XSS;SQLi;CSRF;DDoS      |                |
|         | ✓   |     | ✓   |     |                                                    |                         |                |
| S38[60] |     |     |     |     | Service-denialandscan/floodattacks(NULL,SYN,X-MAS) |                         |                |
| S39[72] | ✓   |     |     |     |                                                    |                         | DDoS           |
| S40[52] | ✓   |     | ✓   |     |                                                    | Maliciousco-residentVMs |                |
| S41[77] | ✓   | ✓   |     |     |                                                    | KnownAPTs&CVEs          |                |
| S42[57] | ✓   |     |     |     |                                                    |                         | Anomalies      |
| S43[93] | ✓   |     |     | ✓   |                                                    | CVEvulnerabilities      |                |
✓
| S44[84] |     |     |     |     |     |     | –   |
| ------- | --- | --- | --- | --- | --- | --- | --- |
|         | ✓   | ✓   |     |     |     |     |     |
| S45[78] |     |     |     |     |     |     | –   |
|         | ✓   |     |     | ✓   |     |     |     |
S46[64] Sensitive-fileinteractions;processexecustions;suspicioustraffic
✓
| S47[65] |     |     |     |     |     |                             | –       |
| ------- | --- | --- | --- | --- | --- | --------------------------- | ------- |
| S48[92] | ✓   |     |     |     |     | Multi-stepattacks;knownCVEs |         |
| S49[79] |     | ✓   |     |     |     |                             | Various |

Electronics2025,14,2252
38of55
Table5.Cont.
EvaluationMethod
Study Experiment Case Real-World Comparison PotentialSecurityRisks
|         | /Simulation | Study | Scenario | withOthers |                                           |      |
| ------- | ----------- | ----- | -------- | ---------- | ----------------------------------------- | ---- |
| S50[58] |             |       |          |            | Spoofing;tampering;DoS;privilegeelevation |      |
| S51[86] |             | ✓     |          |            |                                           | APTs |
✓
| S52[46] |     |     |     |     |                                                       | Various |
| ------- | --- | --- | --- | --- | ----------------------------------------------------- | ------- |
|         |     | ✓   |     |     | Spyware;baiting;DDoS;vishing;smishing;hijacking;spam; |         |
S53[74]
scareware;rogueATMinfection
|         | ✓   |     | ✓   | ✓   |                                               |                           |
| ------- | --- | --- | --- | --- | --------------------------------------------- | ------------------------- |
| S56[75] |     |     |     |     |                                               | Various                   |
| S57[97] |     | ✓   |     |     |                                               | KnownCVEs                 |
| S58[48] |     | ✓   |     |     | Evasion;poisoning;exploratory&Softwareattacks |                           |
| S59[76] | ✓   |     |     |     |                                               | RTCIA;RSCA;DIA            |
| S60[59] | ✓   |     |     |     |                                               | Unauthorizedintrusions    |
| A1[67]  |     | ✓   |     |     |                                               | Intellectualpropertytheft |
✓
| A2[37] |     |     |     |     |     | APTs;contextualanomalies        |
| ------ | --- | --- | --- | --- | --- | ------------------------------- |
|        | ✓   |     | ✓   |     |     |                                 |
| A3[38] |     |     |     |     |     | Malware;APTs;enterprisebreaches |
✓
A4[49] –
✓
A5[68] –
4.4. KeyDataSourcesandTypesinEnterpriseSecurityAnalytics(RQ4)
Observation8(Ob8): CriticalRelianceonDiverseandHeterogeneousDataSources
forComprehensiveSecurityInsight
Enterprisesecurityanalyticsfundamentallydependsonthecollection,integration,
andanalysisofdatafromawidespectrumofsourcesandtypes,asdetailedinthestudies
summarizedinTable6. Thisdiversityisnotincidentalbutessentialforachievingaholistic
understanding of an enterprise’s security posture, enabling effective threat detection,
contextualizing alerts, and supporting informed incident response. The selection and
prioritization of these data sources are critical, often dictated by the specific security
objectives,operationalenvironment,regulatorylandscape,andthreatmodelofagiven
|     |     | enterprise. | Ouranalysiscategorizesthesevitaldatainputsasfollows |     |     |     |
| --- | --- | ----------- | --------------------------------------------------- | --- | --- | --- |
• SystemMonitoringandLogData: Thisfoundationalcategoryremainsparamountin
securityanalytics,encompassingreal-timeinformationandhistoricallogsgenerated
by various IT assets. Examples include application logs, firewall and proxy logs,
Intrusion Detection/Prevention System (IDS/IPS) alerts, operating system event
data,endpointactivitylogs,andserverlogfiles(e.g.,[37,41,59,64,83,84]). Analyzing
theselogsprovidesagranularaudittrailcrucialfordetectinganomalousbehaviors,
reconstructingattacktimelines,conductingforensicinvestigations,anddemonstrating
compliance. Thesheervolume,velocity,andvarietyofthisdata,however,present
significantchallengesintermsofcollection,storage,normalization,andprocessing,
necessitatingrobustdatamanagementandanalyticsplatforms.
• NetworkConfigurationandTrafficData: Dataderivedfromnetworkelements,includ-
ingtrafficlogs(e.g.,NetFlow,sFlow,PCAPs)anddeviceconfigurationinformation,
are central to understanding network-based threats (e.g., [49,59,65,75,102]). These
sourcesofferagranularviewofthenetwork’sarchitecture,communicationpatterns,
andoperationalstatus. Analyzingthisdatahelpstorevealpotentialvulnerabilitiesin
networkdesign,detectunauthorizedaccessattempts,identifymalwarepropagation,
andmonitorforunusualdataexfiltration. Changesinconfigurationoranomalous
networktrafficpatterns(likeunexpectedspikesorcommunicationwithknownmali-

Electronics2025,14,2252 39of55
ciousIPs)canserveasearlyindicatorsofasecuritybreach. Theintegratedanalysisof
networkconfigurationandtrafficdatasignificantlyenhancesanenterprise’scapability
toanticipate,identify,andreacttonetwork-bornethreats,thoughtheincreasinguse
ofencryptioncansometimeslimitdeeppacketinspectioncapabilities.
• User and Application Behavior Data: Understanding user and application activities is
increasinglycritical,withdatacollectedfromidentityandaccessmanagementsystems,
applicationinteractionlogs,mobileapplicationusage,andevenphysicalaccesssystems
(e.g., [33,54,55,71,73]). This data provides significant insights into behavior patterns,
allowingsecurityanalytics,particularlyUEBAsolutions,toestablishbaselinesofnormal
activityandidentifydeviationsthatcouldindicatecompromisedcredentials,insider
threats,ormaliciousapplicationbehavior.Whilepowerful,thecollectionandanalysis
of such data must carefully navigate privacy considerations and the complexity of
accuratelydistinguishingmaliciousfrombenignbehavioralanomalies.
• BusinessandTransactionalData: Integratingdatafromcorebusinessprocessesandsys-
tems,suchasquerylogs,financialtransactionrecords,andcustomerrelationshipman-
agement(CRM)data,providescrucialcontexttosecurityevents(e.g.,[34,67,74,91]).
Thiscategoryallowssecurityanalyticstocorrelatetechnicalindicatorsofcompromise
withpotentialbusinessimpact,aidingintheprioritizationofalertsandresponseef-
forts. Forinstance,anomalousaccesstosensitivecustomerdatabasesorunusualtrans-
actionpatternscanbeflaggedashigh-prioritysecurityevents. Thechallengeoftenlies
ineffectivelyintegratingdisparatebusinesssystemswithsecurityanalyticsplatforms
anddefiningclearcorrelationsbetweenbusinessprocessesandsecuritytelemetry.
• ExternalThreatIntelligenceandPublicDatasets: Leveragingexternalinformationsources
isvitalforenrichinginternalsecuritydataandenhancingproactiveandpredictive
capabilities. Thisincludescuratedthreatintelligencefeeds(providingindicatorsof
compromise,informationonthreatactors,andattackmethodologies),publiclyavail-
ablebreachdatasets,vulnerabilitydatabases,andsecurityscanreportsfromreputable
sources(e.g.,[52,60,72,77]). Theseexternalinputsareinvaluableforbenchmarking
internalsecurityposture,trainingmachinelearningmodelstorecognizeemerging
threats, and providing early warnings about new attack techniques or campaigns.
Theeffectiveuseofsuchdatadependsonitstimeliness,reliability,andtheabilityto
operationalizeitwithintheenterprise’ssecurityanalyticsframework.
• ComplianceandPolicyData:Informationrelatedtoregulatorycompliancemandates,inter-
nalsecuritypolicies,securityrules,andconfigurationstandardsplaysanessentialrolein
governance-focusedsecurityanalytics(e.g.,[38,85,86]).Compliancereportshelptoiden-
tifydeviationsfromrequiredsecuritybaselines,informingcorrectiveactionsandshaping
strategicsecurityinvestments.Securityrulesandpolicydefinitionsprovideabenchmark
against which system configurations and user behaviors can be evaluated, enabling
the detection of policy violations that could introduce vulnerabilities or elevate risk.
Analyzingthisdatahelpsenterprisesmaintainaninformed,adaptive,anddemonstrable
approachtomeetingtheirsecurityandregulatoryobligations.
Inconclusion,theefficacyofenterprisesecurityanalyticsisprofoundlyinfluencedby
thestrategicselection,integration,andcontextualizationofdiversedatasources. While
individualdatatypesofferspecificinsights,thetrendandrecognizedbestpracticeinvolve
fusingtheseheterogeneousdatasetstocreatearicher,morecomprehensiveunderstanding
ofthethreatlandscape. Thisholisticapproachenablesmoreaccuratedetection,reduces
falsepositives,andfacilitatesmoreeffectiveincidentresponse. However,managingthe
complexityofdataintegration,ensuringdataquality,andaddressingthesheerscaleof
dataremainsignificantoperationalchallengesformanyenterprises.

Electronics2025,14,2252 40of55
Table6.Commonsourcesandtypesofdataforsecurityanalytics.
Study DataSource DataType
S1[41] SystemMonitoringData Applicationlogs;IDSalerts;firewalllogs
S6[34] BusinessOperationData Plannumber;digitaldata;planvalidation
S7[33] UserActivityLogs Datalogs;audittrails;datatransfers;networkusage
S9[36] ProcessMonitoringData Running-processevents
S10[91] TransactionalData Querylogs;login,paymentandtransferrecords
S13[53] Honeypot-CollectedData Networktraffic;logs;attacksignatures
S14[83] SystemBehaviorData Behaviourofnetworkedsystems;events
S15[61] SystemandUserDocuments Configurationfiles;documents;manuals;e-mailinboxes/outboxes;contactlists
S16[82] SystemArchitectureandUserActivity Ordinaryuseractivity;enterprise-architecturerepository
S17[85] ComplianceandConfigurationData Ruleresults:pass,fail,error,unknown,notapplicable,notchecked,notselected,informational,fixed
S18[71] Mobile-ApplicationUsageData Systemcalls;networktraffic;userinteractions
S19[88] Incident-ResponseData Probability;meanandstandarddeviationoftimetobreach
S21[62] SecurityEventData Manualinput;sensors;network-scanningtools;SIEMsystem
S22[90] WindowsSystemLogsandDataset Windows-firewall,event,application,andweblogs
S23[54] User-ExperienceData Loginlogs;applicationlogs;programerrors;hardwareinterrupts
S24[100] Security-IncidentData IDSalerts;auditlogs
S25[89] InterviewFindings Qualitativeinterviewresults
S26[94] WindowsModuleData Black-listedandwhite-listedmodules
S30[47] SecurityEventData Logsfromhosts,domaincontrollers,otherlog-managementsystems
S31[55] UserBehaviourData Software,hardware,andsystemlogs
S32[45] UnstructuredSystemData Standardsyslogs;legacy-applicationlogs
S34[56] Virtual-MachineMonitoringData Networkandapplicationlogs
S35[102] NetworkConfigurationData Topology;configurations;vulnerabilityinformation
Accessinformation;registrationdays;logintime;permissionlevel;clientbrowser;sourceIP;loginmailbox;
S36[63] Web-UsageData
continuous-logindays
S37[73] Web-UsageData URLsequences
S38[60] PublicDataset Application,event,firewall,andothersecuritylogs
S39[72] PublicDataset PCAP-formatfiles
S40[52] Scan-ReportData VMs,hosts,connectivity,per-VMvulnerabilities
S41[77] Scan-ReportData Logs;vulnerabilities;hostconfigurationandnetworktopology
S42[57] UnstructuredSystemData Open-sourceHadooplogdataset
S44[84] SIEM/ICS/SCADAData Networktraffic;configurationinformation
S45[78] IAMEventData Eventlogs
S46[64] SystemMonitoringData Network,processandfileevents
S47[65] Network-TrafficData IPaddress;port;protocol;logfile
S48[92] DeviceandScan-ReportData Relationship;type;serviceandvulnerabilityinfo
S49[79] EventandScan-ReportData Networktraffic;logs
S51[86] SecurityPolicyData Networkelements;securitypolicydefinitions
S53[74] OperationandTransactionData Networktraffic;click-stream;eventlogs;transactionrecords
S55[66] AttackEventData Persistentattackrecords;logs
S56[75] IDSAlertData Threatalertlogs
S60[59] NetworkandSystemMonitoringData Capturedpackets;logfiles;alerts
A1[67] BusinessandITInfrastructureData Deviceinventory;logdata;ERP-systemdata
A2[37] SIEMData Logs;networkanddeviceevents
A3[38] SecurityControlData Logsfromwebproxies;domaincontrollers;anti-virussoftware
A4[49] NetworkTrafficData PCAPlogfiles
A5[68] SyslogandSNMPData Server,anti-viruses,systemandnetworkevents/logs

Electronics2025,14,2252 41of55
4.5. BarrierstoImplementingSecurityAnalyticsinEnterprises(RQ5)
Observation9(Ob9): OvercomingSignificantandInterconnectedBarrierstoEffec-
tiveEnterpriseSecurityAnalytics
Thesuccessfulimplementationandoperationalizationofsecurityanalyticsinenter-
priseenvironmentsareimpededbyarangeofsignificantandofteninterconnectedchal-
lenges. Thesebarriersspantechnological,human,financial,legal,ethical,andcontextual
dimensions,demandingaholisticunderstandingandstrategicmitigationefforts. Failureto
addressthesecanseverelylimittheefficacyofsecurityanalyticsinitiatives,leavingorgani-
zationsvulnerabledespiteinvestments. Basedontheliteratureandthebroaderoperational
context,thesechallengescanbesynthesizedintothefollowingoverarchingcategories:
• Data-RelatedChallenges: Thefoundationofsecurityanalyticsisdata,yetitscollection,
management,utility,andprotectionpresentsubstantialhurdles. Enterprisesgrapple
with the sheer volume, variety, and velocity of security data, particularly log data
emanatingfromdiverseeventsources[63,68]. Thisisexacerbatedbythelackofstan-
dardizeddataformatsandretrievalprotocols,especiallyinspecializedenvironments
likeSCADAsystems[84],complicatingdataintegrationandinteroperability. Further-
more,theinherentsecurityrisksofbigdatasystemsthemselves,oftennotdesigned
withsecurityasaprimaryconcern,canintroducenewvulnerabilities[46]. Acritical
andincreasinglyprominentdata-relatedchallengeisensuringdataprivacy.Practically,
enterprises must navigate complex and stringent data protection regulations (e.g.,
GDPR,CCPA,HIPAA),whichimposesignificantobligationsregardingthecollection,
processing,storage,andretentionofpersonalorsensitivedatausedinsecurityanalyt-
ics. Thisincludesimplementingrobustdataminimizationstrategies,anonymization
orpseudonymizationtechniqueswherefeasible,managinguserconsentappropriately,
andensuringtheprivacyofdataprocessedbythird-partyanalyticstoolsorcloud
services[59]. Thelimitationhereisthatoverlyaggressivedataanonymizationcan
sometimesreducetheutilityofdataforcertaintypesofsecurityanalysis, creating
adifficulttrade-off. Consequently,thecollecteddataisfrequentlynoisy,containing
redundancies,lackingcrucialcontext,orposingprivacyrisksifnothandledcorrectly,
allofwhichcanhamperefficientandcompliantanalysis,particularlyforconcurrent
eventtrackinganduserbehavioranalytics[64]. Addressingthesemultifaceteddata
issuesrequiresrobustdatagovernanceframeworks(incorporatingprivacy-by-design),
advanceddata-processingtechniques,andthedevelopmentofcentralizeddatacor-
relation platforms capable of providing a unified, reliable, and compliant view of
securityevents[67].
• Technological and Methodological Limitations: Beyond data, the tools and underlying
methodologies for security analytics face limitations. Current security assessment
techniquesofteninvolveacumbersomemixofautomatedscanningandmanualex-
ploitation, demanding significant expertise and up-to-date information on system
topologiesandvulnerabilitiestointerpretcomplexoutputslikeattackgraphs[77,97].
Manytraditionalsecuritytoolsstruggletoeffectivelyaddressmodern,sophisticated
threats[72]ortoanalyzethesecurityofincreasinglyprevalentmachinelearningsys-
temsthemselves[48]. Acriticalandpersistentchallengeisthedifficultyinadapting
todynamicnetworksecuritythreatsandaccuratelyidentifyingunknownornovel
attacksinreal-time[65]. Thesetechnologicalgapsarecompoundedbymethodological
shortcomings, such as the lack of clear definitions or standardized approaches for
applyingemergingtechniqueslikeprocessminingincybersecurity[78]. Asignificant
methodologicallimitationimpactingtheentirefieldisthedearthofstandardizedeval-
uationmetricsandbenchmarksforsecurityanalyticssolutions. Practically,thismakes
itexceedinglydifficultforenterprisestoobjectivelycomparetheeffectiveness,effi-

Electronics2025,14,2252 42of55
ciency,andROIofdifferenttoolsandapproaches,tobenchmarktheirowncapabilities
againstindustrypeers,orforresearcherstoreliablycompareoutcomesacrossstudies.
Thislackofstandardizationhindersmatureadoptionandslowsevidence-basedad-
vancements. Moreover,therelativelyslowmaturationoftheoreticalfoundationsfor
corecybersecurityconcepts(e.g.,logicalvulnerability,comprehensivethreatmodeling,
quantifiableriskassessment)andtheabsenceofacommon,expressivelanguagefor
securitypoliciesimpedethedevelopmentofmorerobust,adaptable,interoperable,
andscientificallygroundedanalyticssolutions[74].
• ResourceandOrganizationalConstraints: Effectivesecurityanalyticsisnotsolelyatech-
nologicalproblem;itissignificantlyconstrainedbyavailableresourcesandvarious
organizationalfactors,includingethicalconsiderations. Financialconstraintsarea
majorbarrier,particularlyforSMEsthatoftenlackthecapitaltoinvestinadvanced
security analytics tools, technologies, and specialized personnel [58,86,92]. These
costscanbefurtherinflatedbytheabsenceofacomprehensive,overarchingsecurity
strategy,leadingtofragmentedinvestmentsandreducedcost-effectiveness[52]. A
criticalhumanfactoristhepervasiveshortageofskilledcybersecurityprofessionals
capableofmanaginganalyticssystems,interpretingcomplexdata,andtranslating
insightsintoactionablesecuritymeasures[52,86,92]. Thisincludesacommonlack
ofdedicateddatascientistroleswithinsecurityteamswhocouldunlockdeeperin-
sights from business security data [67]. Compounding this is often a general lack
of cybersecurity awareness and understanding among general employees [66,92],
whocanbeunwittingsourcesofrisk. Itisalsocrucialtoengageusersappropriately,
avoidingoverwhelmingthemwithsecuritytaskstopreventsecurityfatigue,which
canunderminecomplianceandvigilance[49,105]. Furthermore, ethicalconsidera-
tionsinthedeploymentofsecurityanalytics,particularlythoseinvolvingextensive
datamonitoring(e.g.,userbehavioranalytics)orAI-drivendecisionmaking,present
significantorganizationalchallenges. Practically,organizationsmustestablishclear
ethicalguidelines,governancestructures,andoversightmechanismstoprevental-
gorithmic bias, ensure fairness, maintain employee trust, and address the societal
implicationsofsurveillancetechnologies[94]. Thelimitationisthatnavigatingthese
ethicaldimensionsrequirescarefuldeliberationandmayconstrainthetypesofdata
collectedorthemannerinwhichanalyticsareapplied,demandingabalancebetween
securityobjectivesandethicalresponsibilities.
• SystemicComplexityandtheEvolvingThreatLandscape: Theinherentcomplexityofmod-
ernITenvironmentsandthecontinuouslyevolvingnatureofcyberthreatspresent
formidablechallenges. Theintricateandheterogeneousnatureofenterprisesystems,
includingsprawlingcloudinfrastructures,createssignificantintegrationandinterop-
erabilityproblemsforsecurityanalyticssolutions[52,68]. Enterprisesoftenstruggle
witheffectivelytranslatinghigh-levelcybersecurityobjectivesintoconcretedesign
choicesandaccuratelyassessingriskswithinthesecomplexarchitectures[101]. Exist-
ingsecurityapproachesmaynotbewell-suitedforanalyzingtheemergentbehaviors
andvulnerabilitiesinsuchmultifacetedsystems[48].Specificcomplexitiesalsoarisein
managingsecurityinpubliccloudenvironmentsduetosharedresponsibilitymodels
and,asnotedearlier,heightenedconcernsoverdataprivacy,security,andoperational
efficiency[59]. Simultaneously,organizationsfaceanincreasinglydynamicandso-
phisticatedthreatlandscape,rangingfromfinanciallymotivatedmalwarecampaigns
tohighlytargetedattacksbyorganizedcrimeandnation-stateactors[38]. Traditional
signature-based security mechanisms are often inadequate for detecting these ad-
vancedthreatsinrealtime[56], andthedetectionofunknownorzero-daythreats
remainsapersistentandcriticaldifficultyacrossthefield[65,66].

Electronics2025,14,2252 43of55
Insummary,thechallengesconfrontingtheimplementationandeffectiveoperational-
izationofenterprisesecurityanalyticsaremultifaceted,deeplyinterconnected—spanning
datamanagementandprivacy,technologicalandmethodologicalmaturity,resourceavail-
ability,organizationalculture,ethicalresponsibilities,andthecomplexityofbothenterprise
systemsandthethreatlandscape—anddemandcomprehensive,adaptivestrategiesfor
mitigation. Overcomingthesehurdlesnecessitatesaconcertedeffortinvolvingtechnologi-
calinnovation,substantialinvestmentintalentdevelopmentandretention,thecultivation
ofastrongandethically-informedsecurityculture,robustgovernanceincludingprivacy-
by-designprinciples,andtheadoptionofadaptive,integratedsecurityarchitectures. Ad-
dressingthesediversebarriersisparamountforenterprisestofullyleveragethepotential
ofsecurityanalyticsinsafeguardingtheircriticalassetsagainstanever-evolvingarrayof
cyberthreats.
4.6. ResearchGapsandFutureOpportunitiesinEnterpriseSecurityAnalytics(RQ6)
Observation10(Ob10): ChartingtheCourseforFutureAdvancementsinEnterprise
SecurityAnalytics
Therapidlyevolvinglandscapeofenterprisesecurityanalytics,whiledemonstrating
significantprogress,presentsnumerousresearchgapsandcompellingopportunitiesfor
future investigation. Addressing these areas is crucial not only for advancing the theo-
reticalunderpinningsofthefieldbutalsoforenhancingthepracticalefficacyofsecurity
analyticssolutionsincombatingincreasinglysophisticatedcyberthreats. Ouranalysisof
thereviewedliteratureidentifiesseveralpivotaldomainswherefocusedresearchefforts
canyieldsubstantialimpact:
• InnovationsinMethodologicalApproaches: Thereisapersistentcallfortheexploration
and refinement of advanced analytical techniques, particularly deep learning and
ensemblelearningmethods,toachievehigheraccuracyandrobustnessinthreatdetec-
tionandprevention[47,67,72]. Futureresearchshouldmovebeyondsimplyapplying
these models to investigating their explainability (XAI) in a security context, their
resilienceagainstadversarialAIattacks,andtheiroptimalapplicationtospecificthreat
types. Criticalfoundationalgapsalsoexistindata-preprocessingstages,including
moreintelligentandautomatedfeatureselection, effectivedata-labelingstrategies
(especiallyforunsupervisedorsemi-supervisedlearningindynamicenvironments),
andefficientdata-encodingtechniquescapableofhandlingvast,real-timedatastreams
withoutprohibitivecomputationaloverhead[75]. Asignificantopportunityliesin
designingadaptive,context-aware,andhuman-centricsecurityanalyticssolutions.
Currentapproachesofteninadequatelyaccountforthedynamicnatureofenterprise
systems, the evolving behavior of attackers, and critical human factors in security
operations[92]. Futureworkshouldaimtodevelopsystemsthatcanlearnfromand
adapttothesechangingconditions,potentiallyincorporatingbehavioraleconomicsor
cognitivescienceprinciplestobettersupporthumananalystsandmitigatesecurity
fatigue[66]. Furthermore,thefieldwouldbenefitfromincreasedmethodologicalrigor
andstandardization. Thisincludesestablishingclearerdefinitionsandframeworks
forapplyingtechniqueslikeprocessminingtocybersecurityincidentresponseand
analysis[78],anddevelopingacommon,expressivelanguageforsecuritypoliciesto
facilitateinteroperabilityandautomatedreasoning[74].
• HolisticDataIntegrationandCross-FunctionalContextualization: Arecurringchallenge,
andthusaresearchopportunity,istheeffectiveintegrationandsemanticcorrelation
of heterogeneous data sources. Beyond merely aggregating logs, future research
needstofocusondevelopingsophisticatedframeworksforfusingdiverseinternal
data(e.g.,system,network,applicationlogs)withexternalsources(e.g.,threatintelli-

Electronics2025,14,2252 44of55
gence,vulnerabilitydatabases)toconstructaunified,comprehensive,andreal-time
understandingofanenterprise’ssecurityposition[74,90]. Thisincludesresearchinto
scalabledatafusiontechniquesandknowledgerepresentationforcomplexsecurity
events. Crucially,thereisasignificantgapinintegratingsecurityanalyticsoutputs
with broader business functions, such as enterprise risk management, compliance
reporting,andinternalauditprocesses[67]. Futurestudiesshouldexploremethod-
ologiesandplatformsthatcantranslatetechnicalsecurityfindingsintoquantifiable
businessriskmetrics,enablingbetterstrategicdecisionmakinganddemonstratingthe
valueofsecurityinvestments. Thisinvolvesbridgingthecommunicationgapbetween
technicalsecurityteamsandexecutiveleadership.
• Enhanced Human–Computer Interaction and Actionable Insights: While the power of
analyticsgrows,ensuringthathumananalystscaneffectivelyinterpretandactupon
thegeneratedinsightsremainsachallenge. Futureresearchisneededinadvanced
datavisualizationtechniquestailoredforcomplex,high-dimensionalsecuritydata,
movingbeyondstaticdashboardstointeractiveexplorationtoolsthatcanhelpanalysts
identifysubtlepatterns,anomalies,andcausalrelationshipsquickly[38,47]. Closely
relatedistheneedforexplainableAIinsecurityanalytics. Asmodelsbecomemore
complex,their“black-box”naturecanhindertrustandadoption. ResearchintoXAI
methodsthatcanarticulatethereasoningbehindalertsorpredictionsinahuman-
understandablemannerisvitalforempoweringanalystsandenablingmoreconfident
responseactions.
• Achieving True Real-Time, Proactive, and Predictive Capabilities: The demand for real-
timedetectionandresponsecontinuestooutpacethecapabilitiesofmanyexisting
systems. Periodiclogcollectionandbatchprocessingareofteninsufficientforcounter-
ingadvanced,fast-movingattacks[56]. Futureresearchshouldfocusondeveloping
ultra-lowlatencystreamprocessingarchitectures,edgeanalyticsforimmediatethreat
detectionindistributedenvironments(e.g.,IoT/OT),androbustframeworksforauto-
matedorsemi-automatedincidentresponsebasedonreal-timeanalyticaltriggers[76].
Beyondreal-timedetection,thereisasignificantopportunitytoenhancepredictive
securityanalytics. Thisinvolvesimprovingtheaccuracy,leadtime,andactionability
of threat prediction models, exploring novel indicators of future attacks (e.g., pre-
cursoractivities,geopoliticalshifts)anddevelopingmethodologiestotranslatethese
predictionsintoconcrete,prioritizedproactivedefensemeasures.
• Ensuring Scalability, Performance, and Operational Efficiency: As data volumes con-
tinuetoexplode,thescalabilityandperformanceofsecurityanalyticsframeworks
remainparamountconcerns,especiallyinlarge-scaleenterpriseandbigdataenviron-
ments[37]. Continuousresearchisrequiredintomoreefficientdistributedprocessing
algorithms,optimizeddatastorageandretrievalmechanisms,hardwareacceleration
techniques,andautomatedresourcemanagementforanalyticspipelinestoensurethat
solutionscancopewithincreasingdemandswithoutprohibitivecostsorperformance
degradation[59,75]. Thisalsoincludesresearchintoautomatedsecurityassessment
toolsthatcanscaleacrosslarge,dynamicinfrastructures.
• DemocratizingSecurityAnalyticsforSMEs: Anotableandcriticalresearchgapisthe
limitedfocusontheuniquesecurityanalyticsneedsofSMEs[106]. SMEsoftenface
similarthreatlandscapesaslargerenterprisesbuttypicallyoperatewithsignificant
resourceconstraints(intermsoffinances,technicalexpertise,anddedicatedperson-
nel). Futureresearchshouldprioritizethedevelopmentandadaptationofscalable,
cost-effective, anduser-friendlysecurityanalyticssolutionsspecificallytailoredto
SMEenvironments. Thisincludesexploringlightweightdeploymentmodels,man-
agedsecurityanalyticsserviceofferingssuitableforSMEs, andpracticalguidance

Electronics2025,14,2252 45of55
on implementing foundational analytics capabilities within their operational con-
text. Addressing this gap is essential for fostering a more inclusive and resilient
digitaleconomy.
Inconclusion,whileenterprisesecurityanalyticshasachievedconsiderableadvance-
ments,thefieldisrichwithunresolvedquestionsandpromisingresearchavenues.Progress
intheseareas—spanningmethodologicalinnovation,dataintelligence,human–machine
synergy,real-timecapabilities,performanceengineering,andSMEaccessibility—isessen-
tialforthecontinuedevolutionofsecurityanalytics. Successfullyaddressingthesegaps
willnotonlyenhanceourabilitytocountersophisticatedcyberthreatsbutalsocontribute
tobuildingasaferandmoresecuredigitalfutureforallorganizations.
5. LimitationsoftheReviewandObservationsonthePrimaryLiterature
5.1. LimitationsofThisSystematicLiteratureReviewProcess
Firstly,thetemporalscopeofourreviewwasintentionallysetfromJanuary2013to
December2023. Thisdecadewaschosentocapturethemostrelevantperiodreflecting
thematurationofkeytechnologies(suchasBigDataanalytics,cloudcomputing,machine
learning,andartificialintelligence)thathavefundamentallyreshapedenterprisesecurity
analytics, as highlighted in our findings (Observation 2). While this focus ensures the
reviewconcentratesoncontemporaryapproaches,itnecessarilyexcludesearlierfounda-
tionalwork. Moresignificantly,withoursearchconcludingattheendofDecember2023,
developmentsandpublicationsfrom2024andearly2025werenotincluded. Giventhe
rapidpaceofevolutionincybersecurity,thismeanstheverylatestadvancementswere
outsidethepurviewofthisanalysis. Thisisaninherentconstraintofsystematicreviews
withfixedsearchcompletiondates,whichiscompoundedbytypicaldelaysindatabase
indexingforthemostrecentliterature.
Secondly, our review adhered to specific inclusion criteria regarding publication
language and type. We focused exclusively on peer-reviewed journal articles and full
conferencepaperspublishedinEnglish. Thisapproachensuresabaselineofacademicrigor
butmeansthatpotentiallyvaluableresearchpublishedinotherlanguagesordisseminated
through other channels such as preprints, theses, dissertations, industry white papers
(thosewithoutclearpeer-review),orbookswasnotincluded. Thiscouldhavelimitedthe
geographicaldiversityofperspectivesandmighthaveexcludedsomeveryrecentorniche
findingsnotyetavailableintheselectedpeer-reviewedformats.
Thirdly, the search process itself, while systematic and based on a comprehensive
tripartitekeywordstrategyacrosssixmajoracademicdatabases,hasinherentlimitations.
Theeffectivenessofkeyword-basedsearchesiscontingentontheconsistencyofterminology
usedbyauthorsandtheindexingpracticesofthedatabases. Itis,therefore,possiblethat
somerelevantstudiesemployingdifferentterminologiesorindexedinawaythatdidnot
preciselymatchoursearchquerymaynothavebeenretrieved,despiteoureffortstoensure
broadcoverage,includingsnowballingtechniques.
Finally,thisreviewprovidesabroadoverviewandthematicsynthesisofenterprise
securityanalytics. Whilewehavehighlighteddifferenceswheretheliteraturepermitted
(e.g.,concerningSMEs),thelevelofgranulardetailforeveryspecificenterprisesub-context
(e.g.,varyingsizesbeyondSME/large,orhighlyspecializedindustrysub-sectors)maybe
limitedbythegeneralfocusofmanyprimarystudies.
5.2. ReflectionsontheReviewedPrimaryLiterature
Beyondthelimitationsofourreviewmethodology,theprocessofsynthesizingthe65
includedstudieshashighlightedcertaincharacteristicsandpotentiallimitationswithinthe
primaryliteratureitself,whichareimportantforcontextualizingourfindings:

Electronics2025,14,2252 46of55
• PotentialforPublicationBiasintheField: Whileourownreviewprocessissuscepti-
bletopublicationbias,itisalsoimportanttoconsiderthatthisbiasmaybepresent
inthebroaderfieldofenterprisesecurityanalytics. Thebodyofreviewedliterature
appearedtopredominantlyfeaturestudiesreportingsuccessfulimplementationsor
positive outcomes of proposed techniques. Research studies that find a particular
dataanalysismethodorsecuritystrategytobeineffective(producingnullornegative
results),orwheretheresultsarenotclear-cut(producinginconclusivefindings),are
likelynotpublishedasoftenasstudiesthatshowpositiveorsuccessfulresults.
• ExtentofReal-WorldValidationandMethodologicalRigor: Anotableobservation
fromourreviewoftheincludedstudiesisthevariationintheextentofreal-world
validation for the proposed methodologies and technologies. While some studies
presented evaluations in operational or near-operational settings, many appeared
torelyonsimulations,lab-basedexperiments,orproof-of-conceptdemonstrations.
Thedirectapplicabilityandscalabilityoffindingsfromstudieslackingrobustvali-
dationindiverse,real-worldenterpriseenvironmentscanbelimited. Furthermore,
whileourqualityappraisalfocusedonrelevanceandclarityforthisreview’smapping
objectives, a formal critical appraisal of the intrinsic methodological soundness of
eachprimarystudy(e.g.,usingtoolslikeCASPorAMSTAR)wasnotutilizedasan
exclusioncriterion,whichmeanstheincludedstudiesthemselvesmayhavevariedin
theirmethodologicalrigor.
• StandardizationofEvaluationMetricsandBenchmarks: Ourreviewoftheprimary
literatureindicatedapotentialchallengerelatedtothelackofstandardizedevaluation
metricsandbenchmarkswithintheenterprisesecurityanalyticsfield.Differentstudies
oftenemployedvaried,andsometimesbespoke,metricstoevaluatetheperformance
oftheirproposedtechniquesorsystems. Thisheterogeneitymakesdirectcomparison
ofresultsacrossstudiesdifficultandcanhindereffortstoestablishwidelyaccepted
benchmarksforefficacyandefficiencyinenterprisesecurityanalytics. Thislackof
standardizationwasalsonotedasabroaderchallengeinthefield(Observation9).
• DepthofDiscussionofPracticalLong-TermConsiderations: Whilemanystudies
proposednoveltechniquesorframeworks,thedepthofdiscussionoflong-termprac-
ticalconsiderationsforenterpriseadoption—suchasmaintainability,thetotalcost
ofownershipbeyondinitialdeployment,theevolutionofmodelsinresponsetocon-
ceptdrift,orintegrationwithexistingcomplexlegacysystems—wasnotconsistently
extensiveacrossallreviewedpapers.
6. Conclusions
Thissystematicliteraturereview,conductedinaccordancewiththePRISMAprotocol,
analyzed65peer-reviewedstudiespublishedbetween2013and2023. Ourobjectivewasto
consolidatethecurrentstateofcybersecurityanalyticswithinenterpriseenvironments,syn-
thesizingkeytrends,prevalentmethodologies,significantchallenges,andemergentfuture
researchdirectionsbasedontenthematicobservationsderivedfromtheselectedliterature.
The synthesis reveals a cybersecurity analytics field undergoing a significant tech-
nological and strategic transformation over the past decade. Driven by the escalating
complexityof cyberthreats andevolvingbusiness imperatives(Ob1), enterpriseshave
markedly shifted from traditional, often signature-based, security tools towards more
sophisticated,data-intensive,andAI-poweredanalyticalapproaches(Ob2). Thiserahas
beencharacterizedbythepronouncedadoptionofBigDatainfrastructure,cloudcomput-
ingplatforms,and,critically,machinelearningandartificialintelligenceasfoundational
enablers. Consequently,thereisaclearpivotinsecuritystrategiesfrompredominantly
reactiveposturestowardsmoreproactiveandpredictiveparadigms(Ob7). Thisshiftlever-

Electronics2025,14,2252 47of55
agesdiverseandheterogeneousdatasources—primarilysystemlogsandnetworktraffic
(Ob8)—toanticipate,detect,andmitigatethreatsmoreeffectively. Ourfindingsindicate
thatlargeorganizations,particularlythoseinhigh-risksectorssuchasfinanceandICT,are
attheforefrontofthisadoptioncurve(Ob4),frequentlyemployingasophisticatedblend
ofquantitativeandqualitativeanalyticaltechniques(Ob5,Ob6)tonavigatetheintricate
modernsecuritylandscape.
Despitestrongadvocacyintheliteratureforaholisticapproach(Ob3)—onethatinte-
gratestechnicalsecuritymeasureswithacomprehensiveunderstandingofbroaderbusiness
processesandobjectives—ourreviewsuggeststhislargelyremainsanacknowledgedideal
ratherthanauniversallyorsystematicallyimplementedreality. Thejourneytowardstruly
holisticsecurityanalyticsisimpededbysignificantandpersistentchallenges.Theseinclude
thetechnicaldifficultiesofintegratingdiverseandvoluminousdatasources,thesubstantial
financialcostsofimplementation, thecomplexitiesofmanagingsophisticatedintercon-
nectedsystems, andacriticalshortageofskilledcybersecurityprofessionalscapableof
harnessingtheseadvancedanalytics(Ob9). Thesemultifacetedhurdlesalsolikelycon-
tribute to a notable gap identified in our analysis: the underrepresentation of research
specificallyaddressingtheuniquesecurityanalyticsneedsandconstraintsofSMEs.
Ourreviewhasseverallimitationsasmentionedabove. However,notwithstanding
these limitations, this review offers valuable, actionable insights. The clear trajectory
towardsML/AI-driven,predictiveanalytics(Ob2,Ob7)signalsacriticalimperativefor
practitioners: thestrategicneedtoinvestintherequisiteadvancedinfrastructureandto
cultivateoracquirethespecializedskillstomanagethesesystemseffectively(Ob9). Forthe
researchcommunity,thepersistentchallenges(Ob9)coupledwiththeclearlydelineated
researchgaps(Ob10)chartacompellingcourseforfutureinvestigation. Keypriorities
for advancing the field include the development of more scalable real-time analytics,
theestablishmentofunifiedpolicylanguagesforbetterinteroperability, innovationsin
dataintegrationmethodologies,therobustvalidationofholisticsecurityframeworks,and,
crucially,thecreationoftailored,accessible,andeffectivesecurityanalyticssolutionsfor
SMEs. Addressingthesegaps,particularlyfortheunderservedSMEsector,isparamount
forenhancingcybersecurityresilienceacrosstheentirespectrumofenterprise. Ultimately,
thematurationofenterprisesecurityanalyticshingesoncontinuedinnovationnotonly
inalgorithmsandtechnologiesbutalsoindevisingpracticalstrategiestoovercomethe
significant barriers to their widespread and effective implementation and adoption, as
identifiedherein.
SupplementaryMaterials: Thefollowingsupportinginformationcanbedownloadedat: https:
//www.mdpi.com/article/10.3390/electronics14112252/s1,TableS1: Extracteddatafromthese-
lectedstudies.
AuthorContributions:Conceptualization,T.D.L.;methodology,T.D.L.;investigation,T.D.L.,T.L.-D.
andS.U.;datacuration,T.D.L.,T.L.-D.andS.U.;writing—originaldraftpreparation,T.D.L.;writing—
reviewandediting,T.L.-D.andS.U.;validationandfinalapprovalofthemanuscript,T.D.L.,T.L.-D.
andS.U.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
Acknowledgments:Duringthepreparationofthismanuscript,theauthorsusedGrammarly(Pre-
mium),Quillbot(Premium),andGoogleGemini2.5Prosolelyforgrammarcheckingandrefining
sentencestoanacademictone. WedidnotuseAItogeneratenewcontent,figures,ordata. All
suggestionswerereviewedandeditedbytheauthors,whotakefullresponsibilityforthefinaltext.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

Electronics2025,14,2252
48of55
AppendixA
Thissectionshowstheselectedstudiesandtheircontributionstothereview.
TableA1.Selectedstudiesandtheircontributionstothereview.
| Study | Authors | Title | RQ1 | RQ2 | RQ3 | RQ4 | RQ5 | RQ6 |
| ----- | ------- | ----- | --- | --- | --- | --- | --- | --- |
Cheng,F.,Azodi,A.,Jaeger,D., Multi-CoreSupportedHighPerformance ✓ ✓ ✓ ✓ ✓ ✓
S1[41]
|     | &Meinel,C. | SecurityAnalytics |     |     |     |     |     |     |
| --- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- |
Holm,H.,Sommestad,T., CySeMoL:AToolforCyberSecurityAnalysis ✓ ✓ ✓ ✓ ✓
| S2[42] | Ekstedt,M.,&Nordström,L. | ofEnterprises |     |     |     |     |     |     |
| ------ | ------------------------ | ------------- | --- | --- | --- | --- | --- | --- |
MethodsforStrengtheningaComputer
| S3[43] | Purboyo,T.W. |     | ✓   |     | ✓   |     | ✓   |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
NetworkSecurity
ModelingandSecurityAnalysisofEnterprise
Wang,Y.,Li,J.,Meng,K.,Lin,C.,
| S4[31] |     | NetworkUsingAttack-DefenseStochasticGame | ✓   |     | ✓   | ✓   | ✓   | ✓   |
| ------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
&Cheng,X.
PetriNets
CyberSecurityAnalytics:AStochasticModelfor
|        |                     |                                      | ✓   |     | ✓   |     |     | ✓   |
| ------ | ------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| S5[32] | Abraham,S.,&Nair,S. | SecurityQuantificationUsingAbsorbing |     |     |     |     |     |     |
MarkovChains
PresentationandValidationofMethodfor
S6[34] Ahmed,N.,&Matulevicˇius,R. SecurityRequirementsElicitationfrom ✓ ✓ ✓ ✓ ✓ ✓
BusinessProcesses
AdvancedPersistentThreats:Minimising
| S7[33] | Brewer,R. |     | ✓   |     | ✓   | ✓   | ✓   | ✓   |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
theDamage
|     |     | DealingwithSecurityRequirementsfor | ✓   | ✓   | ✓   |     | ✓   | ✓   |
| --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
S8[35] Li,T.,&Horkoff,J.
Socio-TechnicalSystems:AHolisticApproach
Rieke,R.,Repp,J.,Zhdanova, MonitoringSecurityComplianceof ✓ ✓ ✓ ✓ ✓
S9[36]
|         | M.,&Eichler,J.      | CriticalProcesses                    |     |     |     |     |     |     |
| ------- | ------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
|         |                     | OnlineBankingSecurityAnalysisBasedon |     | ✓   | ✓   | ✓   |     |     |
| S10[91] | Xin,T.,&Xiaofang,B. | STRIDEThreatModel                    |     |     |     |     |     |     |
ExploitabilityAnalysisUsingPredictive
| S11[98] | Abraham,S.,&Nair,S. |     |     |     | ✓   |     |     | ✓   |
| ------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
CybersecurityFramework
|         | Cai,Z.Q.,Zhao,J.B.,Li,Y.,Si, | InformationSecurityEvaluationofSystemBased |     |     |     |     |     |     |
| ------- | ---------------------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
| S12[87] |                              |                                            |     | ✓   | ✓   |     |     |     |
|         | S.B.,&Ni,M.N.                | onBayesianNetwork                          |     |     |     |     |     |     |
Hussein,M.K.,Zainal,N.B.,& DataSecurityAnalysisforDDoSDefenseof ✓ ✓ ✓
S13[53]
|     | Jaber,A.N. | Cloud-BasedNetworks |     |     |     |     |     |     |
| --- | ---------- | ------------------- | --- | --- | --- | --- | --- | --- |
Rieke,R.,Zhdanova,M.,& SecurityComplianceTrackingofProcessesin ✓ ✓ ✓ ✓ ✓
S14[83]
|     | Repp,J. | NetworkedCooperatingSystems |     |     |     |     |     |     |
| --- | ------- | --------------------------- | --- | --- | --- | --- | --- | --- |
Ontology-BasedBig-DataApproachto
Stepanova,T.,Pechenkin,A.,&
| S15[61] |     | AutomatedPenetrationTestingofLarge-Scale | ✓   | ✓   | ✓   | ✓   |     | ✓   |
| ------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
Lavrova,D.
HeterogeneousSystems
Välja,M.,Korman,M.,Shahzad,
| S16[82] |     | IntegratedMetamodelforSecurityAnalysis | ✓   |     | ✓   | ✓   |     |     |
| ------- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
K.,&Johnson,P.
|         | Alsaleh,M.N.,Husari,G.,& |                                       | ✓   |     | ✓   | ✓   | ✓   |     |
| ------- | ------------------------ | ------------------------------------- | --- | --- | --- | --- | --- | --- |
| S17[85] |                          | OptimizingtheROIofCyberRiskMitigation |     |     |     |     |     |     |
Al-Shaer,E.
Baluda,M.,Pistoia,M.,Castro, AFrameworkforAutomaticAnomalyDetection ✓ ✓ ✓ ✓ ✓
S18[71]
|     | P.,&Tripp,O. | inMobileApplications |     |     |     |     |     |     |
| --- | ------------ | -------------------- | --- | --- | --- | --- | --- | --- |
S19[88] Jenab,K.,Khoury,S., Flow-GraphandMarkovianMethodsforCyber ✓ ✓ ✓ ✓
|     | &LaFevor,K. | SecurityAnalysis |     |     |     |     |     |     |
| --- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- |
AnalyticalStudyofCognitiveLayeredApproach
S20[99] Kim,B.J.,&Lee,S.W. forUnderstandingSecurityRequirementsUsing ✓ ✓ ✓ ✓
ProblemDomainOntology
DynamicalCalculationofSecurityMetricsfor
|         |                          |                           | ✓   |     | ✓   | ✓   |     | ✓   |
| ------- | ------------------------ | ------------------------- | --- | --- | --- | --- | --- | --- |
| S21[62] | Kotenko,I.,&Doynikova,E. | CountermeasureSelectionin |     |     |     |     |     |     |
ComputerNetworks
Big-DataSecurityAnalysisApproachUsing
Naik,N.,Jenkins,P.,Savage,N., ComputationalIntelligenceTechniquesinRfor ✓ ✓ ✓ ✓ ✓
S22[90]
|     | &Katos,V. | DesktopUsers |     |     |     |     |     |     |
| --- | --------- | ------------ | --- | --- | --- | --- | --- | --- |

Electronics2025,14,2252
49of55
TableA1.Cont.
| Study Authors | Title | RQ1 RQ2 | RQ3 RQ4 | RQ5 RQ6 |
| ------------- | ----- | ------- | ------- | ------- |
SecurityAnalysisModel,SystemArchitecture
| Niu,D.D.,Liu,L.,Zhang,X.,Lü, |                                | ✓   | ✓ ✓ | ✓ ✓ |
| ---------------------------- | ------------------------------ | --- | --- | --- |
| S23[54]                      | andRelationalModelofEnterprise |     |     |     |
S.,&Li,Z.
CloudServices
| S24   | ABottom-UpApproachtoApplyingGraphical |     |     |     |
| ----- | ------------------------------------- | --- | --- | --- |
| Ou,X. |                                       | ✓   | ✓ ✓ | ✓   |
| [100] | ModelsinSecurityAnalysis              |     |     |     |
BridgingtheGapBetweenBusinessand
Välja,M.,Lagerström,R.,
| S25[89] | TechnologyinStrategicDecision-Makingfor | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| ------- | --------------------------------------- | --- | --- | --- |
Korman,M.,&Franke,U.
CyberSecurityManagement
Buyukkayhan,A.S.,Oprea,A., LensontheEndpoint:HuntingforMalicious ✓ ✓ ✓
S26[94]
| Li,Z.,&Robertson,W. | SoftwareThroughEndpointDataAnalysis |     |     |     |
| ------------------- | ----------------------------------- | --- | --- | --- |
Kato,Y.,Kanai,A.,Tanimoto,S., DynamicSecurityLevelAnalysisMethodUsing ✓ ✓ ✓
S27[96]
| &Hatashima,T. | AttackTree |     |     |     |
| ------------- | ---------- | --- | --- | --- |
S28[70] Lagerström,R.,Johnson,P.,& AutomaticDesignofSecure ✓ ✓ ✓
| Ekstedt,M.                     | EnterpriseArchitecture                   |     |     |     |
| ------------------------------ | ---------------------------------------- | --- | --- | --- |
| Nguyen,H.H.,Palani,K.,&        | AnApproachtoIncorporatingUncertaintyin   |     |     |     |
| S29[95]                        |                                          | ✓ ✓ | ✓   | ✓   |
| Nicol,D.M.                     | NetworkSecurityAnalysis                  |     |     |     |
| Sapegin,A.,Jaeger,D.,Cheng,F., | TowardsaSystemforComplexAnalysisof       |     |     |     |
| S30[47]                        |                                          | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| &Meinel,C.                     | SecurityEventsinLarge-ScaleNetworks      |     |     |     |
|                                | ASecurityAnalysisMethodforSupercomputing | ✓ ✓ | ✓ ✓ | ✓   |
S31[55] Zhu,G.,Zeng,Y.,&Guo,M.
Users’Behaviour
Cinque,M.,Cotroneo,D.,& ChallengesandDirectionsinSecurity ✓ ✓ ✓ ✓ ✓ ✓
S32[45]
| Pecchia,A.                  | InformationandEventManagement(SIEM)          |     |     |     |
| --------------------------- | -------------------------------------------- | --- | --- | --- |
| S33 Sion,L.,Yskout,K.,Van   | Poster:Knowledge-EnrichedSecurityand         |     |     |     |
|                             |                                              | ✓   | ✓   | ✓ ✓ |
| [104] Landuyt,D.,&Joosen,W. | PrivacyThreatModeling                        |     |     |     |
| Win,T.Y.,Tianfield,H.,&     | Big-Data-BasedSecurityAnalyticsforProtecting |     |     |     |
| S34[56]                     |                                              | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| Mair,Q.                     | VirtualizedInfrastructuresinCloudComputing   |     |     |     |
SecurityAssessmentofDynamicNetworksvia
| S35                     |                                       | ✓   | ✓ ✓ | ✓   |
| ----------------------- | ------------------------------------- | --- | --- | --- |
| Wu,S.,Zhang,Y.,&Chen,X. | IntegratingSemanticReasoningandAttack |     |     |     |
[102]
Graphs
|     | AnalysisandVisualizationofWebsiteLogData | ✓   | ✓ ✓ | ✓ ✓ |
| --- | ---------------------------------------- | --- | --- | --- |
S36[63] Lai,J.
fromthePerspectiveofBigData
Padmanaban,R.,Thirumaran,
| S37[73] | SecurityAnalyticsforHeterogeneousWeb | ✓   | ✓ ✓ | ✓   |
| ------- | ------------------------------------ | --- | --- | --- |
M.,Sanjana,V.,&Moshika,A.
| Sharma,S.,Sharma,A.,& | AdvancedNetworkSecurityAnalysis(ANSA)in |     |     |     |
| --------------------- | --------------------------------------- | --- | --- | --- |
| S38[60]               |                                         | ✓   | ✓ ✓ | ✓ ✓ |
| Saini,H.              | Big-DataTechnology                      |     |     |     |
AnIntelligentandTime-EfficientDDoS
Ahmed,A.,Hameed,S.,Rafi,M., IdentificationFrameworkforReal-time ✓ ✓ ✓ ✓ ✓
S39[72]
| &Mirza,Q.K.A. | EnterpriseNetworks:SAD-F:Sparkbased |     |     |     |
| ------------- | ----------------------------------- | --- | --- | --- |
AnomalyDetectionFramework
Alavizadeh,H.,Alavizadeh,H., CyberSituationAwarenessMonitoringand ✓ ✓ ✓ ✓ ✓
S40[52]
| &Jang-Jaccard,J. | ProactiveResponseforEnterprisesontheCloud |     |     |     |
| ---------------- | ----------------------------------------- | --- | --- | --- |
Chowdhary,A.,Huang,D.,
AutonomousSecurityAnalysisand
| S41[77] Mahendran,J.S.,Romo,D., |     | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| ------------------------------- | --- | --- | --- | --- |
PenetrationTesting
Deng,Y.,&Sabur,A.
| Elsayed,M.A.,& | PredictDeep:SecurityAnalyticsasaServicefor |     |     |     |
| -------------- | ------------------------------------------ | --- | --- | --- |
| S42[57]        |                                            | ✓ ✓ | ✓ ✓ | ✓   |
| Zulkernine,M.  | AnomalyDetectionandPrediction              |     |     |     |
AutomaticSecurityManagementofSmart
| Ivanov,D.,Kalinin,M., |                                    | ✓   | ✓   |     |
| --------------------- | ---------------------------------- | --- | --- | --- |
| S43[93]               | InfrastructuresUsingAttackGraphand |     |     |     |
Krundyshev,V.,&Orel,E.
RiskAnalysis
TheSystemforOperationalMonitoringand
| Nashivochnikov,N.V.,             | AnalyticsofIndustryCyber-physicalSystems |     |     |     |
| -------------------------------- | ---------------------------------------- | --- | --- | --- |
| S44[84] Bolshakov,A.A.,Lukashin, |                                          | ✓ ✓ | ✓ ✓ | ✓ ✓ |
SecurityinFuelandEnergyDomainsBasedon
A.A.,&Popov,M.
AnomalyDetectionandPredictionMethods
| Sundararaj,A.,Knittl,S.,& | ChallengesinITSecurityProcessesandSolution |     |     |     |
| ------------------------- | ------------------------------------------ | --- | --- | --- |
| S45[78]                   |                                            | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| Grossklags,J.             | ApproacheswithProcessMining                |     |     |     |
|                           | TowardsanOpenFormatforScalable             | ✓ ✓ | ✓ ✓ | ✓ ✓ |
S46[64] Taylor,T.,Araujo,F.,&Shu,X.
SystemTelemetry

Electronics2025,14,2252
50of55
TableA1.Cont.
| Study Authors | Title | RQ1 RQ2 | RQ3 RQ4 | RQ5 RQ6 |
| ------------- | ----- | ------- | ------- | ------- |
ComputerNetworkSecurityAnalysisModeling
|                        |                                          | ✓   | ✓ ✓ | ✓ ✓ |
| ---------------------- | ---------------------------------------- | --- | --- | --- |
| S47[65] Wu,L.,&Deng,T. | BasedonSpatio-TemporalCharacteristicsand |     |     |     |
Deep-LearningAlgorithm
| Zhang,Y.,Wang,B.,Wu,C.,Wei, | Attack-Graph-BasedQuantitativeAssessment |     |     |     |
| --------------------------- | ---------------------------------------- | --- | --- | --- |
| S48[92]                     |                                          | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| X.,Wang,Z.,&Yin,G.          | forIndustrialControlSystemSecurity       |     |     |     |
EnhancingCyberSecurityinthePhilippine
Aquino,M.F.M.,&
| S49[79] | Academe:ARisk-BasedITProject | ✓   | ✓ ✓ |     |
| ------- | ---------------------------- | --- | --- | --- |
Noroña,M.I.
AssessmentApproach
|     | AFlexibleSecurityAnalyticsServiceforthe | ✓ ✓ | ✓   | ✓   |
| --- | --------------------------------------- | --- | --- | --- |
S50[58] Empl,P.,&Pernul,G.
IndustrialIoT
AQuantitativeSecurityRiskAnalysis
|                                    |                                   | ✓   | ✓ ✓ | ✓ ✓ |
| ---------------------------------- | --------------------------------- | --- | --- | --- |
| S51[86] Kumar,R.,Singh,S.,&Kela,R. | FrameworkForModellingandAnalyzing |     |     |     |
AdvancedPersistentThreats
Rosado,D.G.,Moreno,J.,
| Sánchez,L.E.,Santos-Olmo,A., | MARISMA-BiDaPattern:IntegratedRisk |     |     |     |
| ---------------------------- | ---------------------------------- | --- | --- | --- |
| S52[46]                      |                                    | ✓   | ✓   | ✓   |
| Serrano,M.A.,&               | AnalysisforBigData                 |     |     |     |
Fernández-Medina,E.
Vassilev,V.,Sowinski-Mydlarz,
|     | IntelligenceGraphsforThreatIntelligenceand | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| --- | ------------------------------------------ | --- | --- | --- |
S53[74] V.,Gasiorowski,P.,Ouazzane,
SecurityPolicyValidationofCyberSystems
K.,&Phipps,A.
|     | ComputerNetworkSecurityAnalysisBasedon | ✓   | ✓   |     |
| --- | -------------------------------------- | --- | --- | --- |
S54[80] Chen,G.,&Mazin,T.
Deep-LearningAlgorithm
AnEmpiricalStudyofIntelligentSecurity
| S55[66] Chun,Y.H.,&Cho,M.K. |     | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| --------------------------- | --- | --- | --- | --- |
AnalysisMethodsUtilizingBigData
| Ndichu,S.,Ban,T.,Takahashi,T., | Critical-Threat-AlertDetectionUsingOnline |     |     |     |
| ------------------------------ | ----------------------------------------- | --- | --- | --- |
| S56[75]                        |                                           | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| &Inoue,D.                      | MachineLearning                           |     |     |     |
AttackDynamics:AnAutomaticAttack-Graph
|                                 |                                  |     | ✓   | ✓ ✓ |
| ------------------------------- | -------------------------------- | --- | --- | --- |
| S57[97] Hankin,C.,&Malacaria,P. | GenerationFrameworkBasedonSystem |     |     |     |
Topology,CAPEC,CWE,andCVEDatabases
Zou,Q.,Zhang,L.,Singhal,A., AttacksonMLSystems:FromSecurityAnalysis ✓ ✓ ✓
S58[48]
| Sun,X.,&Liu,P.             | toAttackMitigation                     |     |     |     |
| -------------------------- | -------------------------------------- | --- | --- | --- |
| Efiong,J.E.,Akinyemi,B.O., | CyberSCADANetworkSecurityAnalysisModel |     |     |     |
S59[76] Olajubu,E.A.,Aderounmu, forIntrusionDetectionSystemsinthe ✓ ✓ ✓ ✓
| G.A.,&Degila,J. | SmartGrid |     |     |     |
| --------------- | --------- | --- | --- | --- |
Vassilev,V.,Ouazzane,K.,
| Sowinski-Mydlarz,V.,Maosa, | NetworkSecurityAnalyticsontheCloud:Public |     |     |     |
| -------------------------- | ----------------------------------------- | --- | --- | --- |
| S60[59]                    |                                           | ✓   | ✓ ✓ | ✓ ✓ |
| H.,Nakarmi,S.,Hristev,M.,& | vs.PrivateCase                            |     |     |     |
Radu,S.
|     | PreemptiveSecurityThrough | ✓   | ✓ ✓ | ✓ ✓ |
| --- | ------------------------- | --- | --- | --- |
A1[67] Early,G.,&StottIII,W.
InformationAnalytics
AnalyzingandPredictingSecurity-Event
A2[37] Puri,C.,&Dukatz,C. Anomalies:LessonsfromaLarge-Enterprise ✓ ✓ ✓ ✓ ✓
Big-DataStreaming-AnalyticsDeployment
OperationalSecurityLogAnalyticsfor
| A3[38] Li,Z.,&Oprea,A. |     | ✓ ✓ | ✓ ✓ | ✓ ✓ |
| ---------------------- | --- | --- | --- | --- |
EnterpriseBreachDetection
Ulmer,A.,Schufrin,M.,
|     | TowardsVisualCyber-SecurityAnalyticsfor | ✓ ✓ | ✓ ✓ | ✓   |
| --- | --------------------------------------- | --- | --- | --- |
A4[49] Lücke-Tieke,H.,Kannanayikkal,
theMasses
C.D.,&Kohlhammer,J.
Chernova,E.V.,Polezhaev,P.N.,
Shukhman,A.E.,Ushakov,Y.A., Security-EventDataCollectionandAnalysisin ✓ ✓ ✓ ✓ ✓
| A5[68] Bolodurina,I.P.,& | LargeCorporateNetworks |     |     |     |
| ------------------------ | ---------------------- | --- | --- | --- |
Bakhareva,N.F.

Electronics2025,14,2252 51of55
References
1. Kaur,J.;Ramkumar,K. Therecenttrendsincybersecurity:Areview. J.KingSaudUniv.-Comput.Inf.Sci.2022,34,5766–5781.
[CrossRef]
2. Shajan,A.;Rangaswamy,S. Surveyofsecuritythreatsandcountermeasuresincloudcomputing. UnitedInt.J.Res.Technol.2021,
2,201–207.
3. Zhao,T.;Zhang,G.;Zhang,L. AnOverviewofMobileDevicesSecurityIssuesandCountermeasures. InProceedingsofthe2014
InternationalConferenceonWirelessCommunicationandSensorNetwork,Wuhan,China,13–14December2014;pp.439–443.
[CrossRef]
4. Lu,Y.;Xu,L.D. InternetofThings(IoT)CybersecurityResearch:AReviewofCurrentResearchTopics. IEEEInternetThingsJ.
2019,6,2103–2115.[CrossRef]
5. Xiong,W.;Legrand,E.;Åberg,O.;Lagerström,R. CybersecuritythreatmodelingbasedontheMITREEnterpriseATT&CK
Matrix. Softw.Syst.Model.2021,21,157–177.[CrossRef]
6. Saleem,J.;Adebisi,B.;Ande,R.;Hammoudeh,M. Astateoftheartsurvey—ImpactofcyberattacksonSME’s. InProceedings
oftheInternationalConferenceonFutureNetworksandDistributedSystems,ICFNDS’17,Cambridge,UK,19–20July2017.
[CrossRef]
7. Corallo,A.;Lazoi,M.;Lezzi,M. Cybersecurityinthecontextofindustry4.0:Astructuredclassificationofcriticalassetsand
businessimpacts. Comput.Ind.2020,114,103165.[CrossRef]
8. Klein,D. Relyingonfirewalls?Here’swhyyou’llbehacked. Netw.Secur.2021,2021,9–12.[CrossRef]
9. Khraisat,A.;Gondal,I.;Vamplew,P.;Kamruzzaman,J.Surveyofintrusiondetectionsystems:Techniques,datasetsandchallenges.
Cybersecurity2019,2,20.[CrossRef]
10. Tounsi,W.;Rais,H. Asurveyontechnicalthreatintelligenceintheageofsophisticatedcyberattacks. Comput. Secur. 2018,
72,212–233.[CrossRef]
11. Narang,S. Therealityofzero-dayvulnerabilities. Comput.FraudSecur.2021,2021,20.[CrossRef]
12. Salahdine,F.;Kaabouch,N. SocialEngineeringAttacks:ASurvey. FutureInternet2019,11,89.[CrossRef]
13. Rajasekar,V.;Premalatha,J.;Dhanaraj,R.K.Securityanalytics. InSystemAssurances;Elsevier:Amsterdam,TheNetherlands,
2022;pp.333–354.[CrossRef]
14. Nallaperumal,K. CyberSecurityAnalyticstoCombatCyberCrimes. InProceedingsofthe2018IEEEInternationalConference
onComputationalIntelligenceandComputingResearch(ICCIC),Madurai,India,13–15December2018;pp.1–4.[CrossRef]
15. Khan,S.; Olivia,T.S.L.; Khan,N.; Why,N.K.; Wei,T.S. DataAnalyticforCyberSecurity: AReviewofCurrentFramework
Solutions,ChallengesandTrends. EurasiaProc.Sci.Technol.Eng.Math.2022,18,1–6.[CrossRef]
16. Verma,R. SecurityAnalytics:AdaptingDataScienceforSecurityChallenges. InProceedingsoftheFourthACMInternational
WorkshoponSecurityandPrivacyAnalytics,CODASPY’18,Tempe,AZ,USA,19–21March2018;pp.40–41.[CrossRef]
17. Sharma,G.;Tyagi,B. SecurityAnalytics:ChallengesandFutureDirections. IITMJ.Manag.IT2017,8,37–41.
18. Jing,X.;Yan,Z.;Pedrycz,W. SecurityDataCollectionandDataAnalyticsintheInternet:ASurvey. IEEECommun.Surv.Tutor.
2019,21,586–618.[CrossRef]
19. Rassam,M.A.;Maarof,M.;Zainal,A. BigDataAnalyticsAdoptionforCybersecurity:AReviewofCurrentSolutions,Require-
ments,ChallengesandTrends. J.Inf.Assur.Secur.2017,11,124–145.
20. Perumal,P.R.;Roy,G.G.R.;Kumar,B.R. SecurityAnalysisofFutureEnterpriseBusinessIntelligence. InProceedingsofthe2014
WorldCongressonComputingandCommunicationTechnologies,Tiruchirappalli,India,27February–1March2014;pp.191–194.
[CrossRef]
21. Birzniece,I. SecurityAnalytics: DispellingtheFog. InProceedingsoftheBIR2018ShortPapers,WorkshopsandDoctoral
ConsortiumCo-Locatedwith17thInternationalConferencePerspectivesinBusinessInformaticsResearch(BIR2018),Stockholm,
Sweden,24–26September2018;Volume2218,pp.160–169.
22. Grahn,K.;Westerlund,M.;Pulkkis,G.,AnalyticsforNetworkSecurity: ASurveyandTaxonomy. InInformationFusionfor
Cyber-SecurityAnalytics;SpringerInternationalPublishing:Cham,Switzerland,2016;pp.175–193.[CrossRef]
23. Mahmood,T.;Afzal,U. SecurityAnalytics:BigDataAnalyticsforcybersecurity:Areviewoftrends,techniquesandtools. In
Proceedingsofthe20132ndNationalConferenceonInformationAssurance(NCIA),Rawalpindi,Pakistan,11–12December2013;
pp.129–134.[CrossRef]
24. Page,M.J.; McKenzie,J.E.; Bossuyt,P.M.; Boutron,I.; Hoffmann,T.C.; Mulrow,C.D.; Shamseer,L.; Tetzlaff,J.M.; Akl,E.A.;
Brennan,S.E.;etal. ThePRISMA2020statement: Anupdatedguidelineforreportingsystematicreviews. Int. J.Surg. 2021,
88,105906.[CrossRef]
25. Rohan,R.;Pal,D.;Hautamäki,J.;Funilkul,S.;Chutimaskul,W.;Thapliyal,H. Asystematicliteraturereviewofcybersecurity
scalesassessinginformationsecurityawareness. Heliyon2023,9,e14234.[CrossRef]
26. Cremer,F.;Sheehan,B.;Fortmann,M.;Kia,A.N.;Mullins,M.;Murphy,F.;Materne,S. Cyberriskandcybersecurity:Asystematic
reviewofdataavailability. GenevaPap.RiskInsur.-IssuesPract.2022,47,698–736.[CrossRef][PubMed]

Electronics2025,14,2252 52of55
27. Marican, M.N.Y.; Razak, S.A.; Selamat, A.; Othman, S.H. CyberSecurityMaturityAssessmentFrameworkforTechnology
Startups:ASystematicLiteratureReview. IEEEAccess2023,11,5442–5452.[CrossRef]
28. Ratchford,M.;El-Gayar,O.;Noteboom,C.;Wang,Y. BYODsecurityissues:Asystematicliteraturereview. Inf. Secur. J.Glob.
Perspect.2021,31,253–273.[CrossRef]
29. Garg,M.;Goel,A. Asystematicliteraturereviewononlineassessmentsecurity: Currentchallengesandintegritystrategies.
Comput.Secur.2022,113,102544.[CrossRef]
30. Webster,J.;Watson,R.T. Analyzingthepasttoprepareforthefuture:Writingaliteraturereview. MISQ.2002,26,xiii–xxiii.
31. Wang,Y.;Li,J.;Meng,K.;Lin,C.;Cheng,X. Modelingandsecurityanalysisofenterprisenetworkusingattack–defensestochastic
gamePetrinets. Secur.Commun.Netw.2012,6,89–99.[CrossRef]
32. Abraham,S.;Nair,S. CyberSecurityAnalytics:AStochasticModelforSecurityQuantificationUsingAbsorbingMarkovChains.
J.Commun.2014,9,899–907. [CrossRef]
33. Brewer,R. Advancedpersistentthreats:Minimisingthedamage. Netw.Secur.2014,2014,5–9.[CrossRef]
34. Ahmed, N.; Matulevicˇius, R. Presentation and Validation of Method for Security Requirements Elicitation from Business
Processes. InInformationSystemsEngineeringinComplexEnvironments;SpringerInternationalPublishing:Cham,Switzerland,2015;
pp.20–35.[CrossRef]
35. Li,T.;Horkoff,J.DealingwithSecurityRequirementsforSocio-TechnicalSystems:AHolisticApproach. InAdvancedInformation
SystemsEngineering;SpringerInternationalPublishing:Cham,Switzerland,2014;pp.285–300.[CrossRef]
36. Rieke,R.;Repp,J.;Zhdanova,M.;Eichler,J. MonitoringSecurityComplianceofCriticalProcesses. InProceedingsofthe2014
22ndEuromicroInternationalConferenceonParallel,Distributed,andNetwork-BasedProcessing,Torino,Italy,12–14February
2014;pp.552–560.[CrossRef]
37. Puri,C.;Dukatz,C. AnalyzingandPredictingSecurityEventAnomalies:LessonsLearnedfromaLargeEnterpriseBigData
StreamingAnalyticsDeployment. InProceedingsofthe201526thInternationalWorkshoponDatabaseandExpertSystems
Applications(DEXA),Valencia,Spain,1–4September2015;pp.152–158.[CrossRef]
38. Li, Z.; Oprea, A. Operational Security Log Analytics for Enterprise Breach Detection. In Proceedings of the 2016 IEEE
CybersecurityDevelopment(SecDev),Boston,MA,USA,3–4November2016;pp.15–22.[CrossRef]
39. González-Granadillo,G.;González-Zarzosa,S.;Diaz,R. SecurityInformationandEventManagement(SIEM):Analysis,Trends,
andUsageinCriticalInfrastructures. Sensors2021,21,4759.[CrossRef]
40. Bahrami,P.N.;Dehghantanha,A.;Dargahi,T.;Parizi,R.M.;Choo,K.K.R.;Javadi,H.H. Cyberkillchain-basedtaxonomyof
advancedpersistentthreatactors:Analogyoftactics,techniques,andprocedures. J.Inf.Process.Syst.2019,15,865–889.[CrossRef]
41. Cheng,F.;Azodi,A.;Jaeger,D.;Meinel,C. Multi-coreSupportedHighPerformanceSecurityAnalytics. InProceedingsofthe
2013IEEE11thInternationalConferenceonDependable,AutonomicandSecureComputing,Chengdu,China,21–22December
2013;pp.621–626.[CrossRef]
42. Holm,H.;Ekstedt,M.;Sommestad,T.;NordstrM,L. CySeMoL:Atoolforcybersecurityanalysisofenterprises. InProceedings
ofthe22ndInternationalConferenceandExhibitiononElectricityDistribution(CIRED2013),Stockholm,Sweden,10–13June
2013;p.1109.[CrossRef]
43. Purboyo, T.W.; Kuspriyanto. Methods for strengthening a Computer network security. In Proceedings of the 2013 Joint
InternationalConferenceonRuralInformation&CommunicationTechnologyandElectric-VehicleTechnology(rICT&ICeV-T),
Bandung-Bali,Indonesia,26–28November2013;pp.1–4.[CrossRef]
44. ReddyPulyala,S.;GuptaDesetty,A.;DuttJangampet,V. TheImpactofSecurityOrchestration,Automation,andResponse
(SOAR)onSecurityOperationsCenter(SOC)Efficiency:AComprehensiveAnalysis. Turk.J.Comput.Math.Educ.(TURCOMAT)
2019,10,1545–1549.[CrossRef]
45. Cinque,M.;Cotroneo,D.;Pecchia,A. ChallengesandDirectionsinSecurityInformationandEventManagement(SIEM). In
Proceedingsofthe2018IEEEInternationalSymposiumonSoftwareReliabilityEngineeringWorkshops(ISSREW),Memphis,TN,
USA,15–18October2018;pp.95–99.[CrossRef]
46. Rosado, D.G.; Moreno, J.; Sánchez, L.E.; Santos-Olmo, A.; Serrano, M.A.; Fernández-Medina, E. MARISMA-BiDapattern:
Integratedriskanalysisforbigdata. Comput.Secur.2021,102,102155.[CrossRef]
47. Sapegin,A.;Jaeger,D.;Cheng,F.;Meinel,C. Towardsasystemforcomplexanalysisofsecurityeventsinlarge-scalenetworks.
Comput.Secur.2017,67,16–34.[CrossRef]
48. Zou, Q.; Zhang, L.; Singhal, A.; Sun, X.; Liu, P.AttacksonMLSystems: FromSecurityAnalysistoAttackMitigation. In
InformationSystemsSecurity;SpringerNature:Cham,Switzerland,2022;pp.119–138.[CrossRef]
49. Ulmer,A.;Schufrin,M.;Lücke-Tieke,H.;Kannanayikkal,C.D.;Kohlhammer,J. TowardsVisualCyberSecurityAnalyticsforthe
Masses.InProceedingsoftheEuroVisWorkshoponVisualAnalytics2018,Brno,CzechRepublic,4June2018.[CrossRef]
50. Geluvaraj,B.; Satwik,P.M.; AshokKumar,T.A.TheFutureofCybersecurity: MajorRoleofArtificialIntelligence,Machine
Learning,andDeepLearninginCyberspace. InInternationalConferenceonComputerNetworksandCommunicationTechnologies;
Springer:Singapore,2018;pp.739–747.[CrossRef]

Electronics2025,14,2252 53of55
51. Alani,M.M. Bigdataincybersecurity: Asurveyofapplicationsandfuturetrends. J.Reliab. Intell. Environ. 2021,7,85–114.
[CrossRef]
52. Alavizadeh,H.;Alavizadeh,H.;Jang-Jaccard,J. CyberSituationAwarenessMonitoringandProactiveResponseforEnterprises
ontheCloud. InProceedingsofthe2020IEEE19thInternationalConferenceonTrust,SecurityandPrivacyinComputingand
Communications(TrustCom),Guangzhou,China,29December2020–1January2021;pp.1276–1284.[CrossRef]
53. Hussein,M.K.;BinZainal,N.;Jaber,A.N. DatasecurityanalysisforDDoSdefenseofcloud-basednetworks. InProceedingsof
the2015IEEEStudentConferenceonResearchandDevelopment(SCOReD),KualaLumpur,Malaysia,13–14December2015;
pp.305–310.[CrossRef]
54. Niu,D.D.;Liu,L.;Zhang,X.;Lü,S.;Li,Z. Securityanalysismodel,systemarchitectureandrelationalmodelofenterprisecloud
services. Int.J.Autom.Comput.2016,13,574–584.[CrossRef]
55. Zhu,G.;Zeng,Y.;Guo,M. ASecurityAnalysisMethodforSupercomputingUsers’Behavior. InProceedingsofthe2017IEEE4th
InternationalConferenceonCyberSecurityandCloudComputing(CSCloud),NewYork,NY,USA,26–28June2017;pp.287–293.
[CrossRef]
56. Win,T.Y.;Tianfield,H.;Mair,Q. BigDataBasedSecurityAnalyticsforProtectingVirtualizedInfrastructuresinCloudComputing.
IEEETrans.BigData2018,4,11–25.[CrossRef]
57. Elsayed,M.A.;Zulkernine,M. PredictDeep:SecurityAnalyticsasaServiceforAnomalyDetectionandPrediction. IEEEAccess
2020,8,45184–45197.[CrossRef]
58. Empl,P.;Pernul,G. AFlexibleSecurityAnalyticsServicefortheIndustrialIoT. InProceedingsofthe2021ACMWorkshopon
SecureandTrustworthyCyber-PhysicalSystems,CODASPY’21,Virtual,28April2021;pp.23–32.[CrossRef]
59. Vassilev,V.;Ouazzane,K.;Sowinski-Mydlarz,V.;Maosa,H.;Nakarmi,S.;Hristev,M.;Radu,S. NetworkSecurityAnalyticson
theCloud:Publicvs.PrivateCase. InProceedingsofthe202313thInternationalConferenceonCloudComputing,DataScience
&Engineering(Confluence),Noida,India,19–20January2023;pp.151–156.[CrossRef]
60. Sharma,S.;Sharma,A.;Saini,H. AdvancedNetworkSecurityAnalysis(ANSA)inBigDataTechnology. Int.J.Innov.Technol.
Explor.Eng.2019,8,2634–2639.[CrossRef]
61. Stepanova,T.;Pechenkin,A.;Lavrova,D. Ontology-basedbigdataapproachtoautomatedpenetrationtestingoflarge-scale
heterogeneoussystems. InProceedingsofthe8thInternationalConferenceonSecurityofInformationandNetworks,SIN’15,
Sochi,Russia,8–10September2015;pp.142–149.[CrossRef]
62. Kotenko,I.;Doynikova,E. DynamicalCalculationofSecurityMetricsforCountermeasureSelectioninComputerNetworks. In
Proceedingsofthe201624thEuromicroInternationalConferenceonParallel,Distributed,andNetwork-BasedProcessing(PDP),
Heraklion,Greece,17–19February2016;pp.558–565.[CrossRef]
63. Lai,J. AnalysisandVisualizationofWebsiteLogDatafromthePerspectiveofBigData. InProceedingsofthe2019International
ConferenceonComputerNetwork, ElectronicandAutomation(ICCNEA),Xi’an, China, 27–29September2019; pp. 26–30.
[CrossRef]
64. Taylor, T.; Araujo, F.; Shu, X. Towards an Open Format for Scalable System Telemetry. In Proceedings of the 2020 IEEE
InternationalConferenceonBigData(BigData),Atlanta,GA,USA,10–13December2020;pp.1031–1040.[CrossRef]
65. Wu,L.;Deng,T. ComputerNetworkSecurityAnalysisModelingBasedonSpatio-temporalCharacteristicsandDeepLearning
Algorithm. J.Phys.Conf.Ser.2020,1648,042111.[CrossRef]
66. Anempiricalstudyofintelligentsecurityanalysismethodsutilizingbigdata. J.Logist.Inform.Serv.Sci.2022,9,26–35. [CrossRef]
67. Early,G.;Stott,W.,III.PreemptiveSecurityThroughInformationAnalytics. Inf.Secur.J.Glob.Perspect.2015,24,48–56.[CrossRef]
68. Chernova,E.;Polezhaev,P.;Shukhman,A.;Ushakov,Y.;Bolodurina,I.;Bakhareva,N. Securityeventdatacollectionandanalysis
inlargecorporatenetworks. InProceedingsoftheVInternationalConferenceInformationTechnologyandNanotechnology
2019,ITNT-2019,Samara,Russia,21–24May2019;pp.233–241.[CrossRef]
69. Moshika,A.;Thirumaran,M.;Natarajan,B.;Andal,K.;Sambasivam,G.;Manoharan,R. VulnerabilityAssessmentinHeteroge-
neousWebEnvironmentUsingProbabilisticArithmeticAutomata. IEEEAccess2021,9,74659–74673.[CrossRef]
70. Lagerstrom, R.; Johnson, P.; Ekstedt, M. AutomaticDesignofSecureEnterpriseArchitecture: WorkinProgressPaper. In
Proceedingsofthe2017IEEE21stInternationalEnterpriseDistributedObjectComputingWorkshop(EDOCW),Quebec,QC,
Canada,10–13October2017;pp.65–70.[CrossRef]
71. Baluda,M.;Pistoia,M.;Castro,P.;Tripp,O.Aframeworkforautomaticanomalydetectioninmobileapplications. InProceedings
oftheInternationalConferenceonMobileSoftwareEngineeringandSystems,ICSE’16,Austin,TX,USA,16–17May2016;
pp.297–298.[CrossRef]
72. Ahmed,A.;Hameed,S.;Rafi,M.;Mirza,Q.K.A. AnIntelligentandTime-EfficientDDoSIdentificationFrameworkforReal-Time
EnterpriseNetworks:SAD-F:SparkBasedAnomalyDetectionFramework. IEEEAccess2020,8,219483–219502.[CrossRef]
73. Padmanaban,R.;Thirumaran,M.;Sanjana,V.;Moshika,A. SecurityAnalyticsforHeterogeneousWeb. InProceedingsofthe
2019IEEEInternationalConferenceonSystem,Computation,AutomationandNetworking(ICSCAN),Pondicherry,India,29–30
March2019;pp.1–6.[CrossRef]

Electronics2025,14,2252 54of55
74. Vassilev,V.;Sowinski-Mydlarz,V.;Gasiorowski,P.;Ouazzane,K.;Phipps,A.IntelligenceGraphsforThreatIntelligenceand
SecurityPolicyValidationofCyberSystems. InProceedingsofInternationalConferenceonArtificialIntelligenceandApplications,
ProceedingsoftheICAIA2020,HongKong,China,21–23October2020;Springer:Singapore,2020;pp.125–139.[CrossRef]
75. Ndichu,S.;Ban,T.;Takahashi,T.;Inoue,D. Critical-Threat-AlertDetectionusingOnlineMachineLearning. InProceedingsofthe
2022IEEEInternationalConferenceonBigData(BigData),Osaka,Japan,17–20December2022;pp.3007–3014.[CrossRef]
76. Efiong,J.E.;Akinyemi,B.O.;Olajubu,E.A.;Aderounmu,G.A.;Degila,J.CyberSCADANetworkSecurityAnalysisModelfor
IntrusionDetectionSystemsintheSmartGrid. InAdvancesinIntelligentSystems,ComputerScienceandDigitalEconomicsIV;
SpringerNature:Cham,Switzerland,2023;pp.481–499.[CrossRef]
77. Chowdhary,A.;Huang,D.;Mahendran,J.S.;Romo,D.;Deng,Y.;Sabur,A. AutonomousSecurityAnalysisandPenetration
Testing. InProceedingsofthe202016thInternationalConferenceonMobility,SensingandNetworking(MSN),Tokyo,Japan,
17–19December2020;pp.508–515.[CrossRef]
78. Sundararaj,A.;Knittl,S.;Grossklags,J.ChallengesinITSecurityProcessesandSolutionApproacheswithProcessMining. In
SecurityandTrustManagement;SpringerInternationalPublishing:Cham,Switzerland,2020;pp.123–138.[CrossRef]
79. Aquino,M.F.M.;Noroña,M.I. EnhancingcybersecurityinthePhilippineacademe:Arisk-baseditprojectassessmentapproach.
InProceedingsofthe11thAnnualInternationalConferenceonIndustrialEngineeringandOperationsManagement,Singapore,
7–11March2021;pp.5166–5179.
80. Chen,G.;Mazin,T.ComputerNetworkSecurityAnalysisBasedonDeepLearningAlgorithm. InApplicationofIntelligentSystems
inMulti-ModalInformationAnalytics;SpringerInternationalPublishing:Cham,Switzerland,2022;pp.993–998.[CrossRef]
81. Ilieva, R.; Stoilova, G. Challenges of AI-Driven Cybersecurity. In Proceedings of the 2024 XXXIII International Scientific
ConferenceElectronics(ET),Sozopol,Bulgaria,17–19September2024;pp.1–4.[CrossRef]
82. Valja,M.;Korman,M.;Shahzad,K.;Johnson,P. IntegratedMetamodelforSecurityAnalysis. InProceedingsofthe201548th
HawaiiInternationalConferenceonSystemSciences,Kauai,HI,USA,5–8January2015;pp.5192–5200.[CrossRef]
83. Rieke,R.;Zhdanova,M.;Repp,J. SecurityComplianceTrackingofProcessesinNetworkedCooperatingSystems. J.Wirel.Mob.
Netw.UbiquitousComput.DependableAppl.2015,6,21–40.
84. Nashivochnikov,N.V.;Bolshakov,A.A.;Lukashin,A.A.;Popov,M.TheSystemforOperationalMonitoringandAnalyticsof
IndustryCyber-PhysicalSystemsSecurityinFuelandEnergyDomainsBasedonAnomalyDetectionandPredictionMethods.
InCyber-PhysicalSystems: Industry4.0Challenges; SpringerInternationalPublishing: Cham,Switzerland,2019; pp. 261–273.
[CrossRef]
85. Alsaleh,M.N.;Husari,G.;Al-Shaer,E. OptimizingtheRoIofcyberriskmitigation. InProceedingsofthe201612thInternational
ConferenceonNetworkandServiceManagement(CNSM),Montreal,QC,Canada,31October–4November2016;pp.223–227.
[CrossRef]
86. Kumar,R.;Singh,S.;Kela,R.AQuantitativeSecurityRiskAnalysisFrameworkforModellingandAnalyzingAdvancedPersistent
Threats. InFoundationsandPracticeofSecurity;SpringerInternationalPublishing:Cham,Switzerland,2021;pp.29–46.[CrossRef]
87. Cai,Z.Q.;Zhao,J.B.;Li,Y.;Si,S.B.;Ni,M.N.InformationsecurityevaluationofsystembasedonBayesiannetwork. InProceedings
ofthe2015IEEEInternationalConferenceonIndustrialEngineeringandEngineeringManagement(IEEM),Singapore,6–9
December2015;pp.315–319.[CrossRef]
88. Jenab,K.;Khoury,S.;LaFevor,K. Flow-GraphandMarkovianMethodsforCyberSecurityAnalysis. Int.J.Enterp.Inf.Syst.2016,
12,59–84.[CrossRef]
89. Valja,M.;Lagerstrom,R.;Korman,M.;Franke,U.Bridgingthegapbetweenbusinessandtechnologyinstrategicdecision-making
forcybersecuritymanagement. InProceedingsofthe2016PortlandInternationalConferenceonManagementofEngineering
andTechnology(PICMET),Honolulu,HI,USA,4–8September2016;pp.32–42.[CrossRef]
90. Naik,N.;Jenkins,P.;Savage,N.;Katos,V. BigdatasecurityanalysisapproachusingComputationalIntelligencetechniquesinR
fordesktopusers. InProceedingsofthe2016IEEESymposiumSeriesonComputationalIntelligence(SSCI),Athens,Greece,6–9
December2016;pp.1–8.[CrossRef]
91. Xin,T.; Ban,X. OnlineBankingSecurityAnalysisbasedonSTRIDEThreatModel. Int. J.Secur. ItsAppl. 2014,8,271–282.
[CrossRef]
92. Zhang,Y.;Wang,B.;Wu,C.;Wei,X.;Wang,Z.;Yin,G.AttackGraph-BasedQuantitativeAssessmentforIndustrialControlSystem
Security. InProceedingsofthe2020ChineseAutomationCongress(CAC),Shanghai,China,6–8November2020.[CrossRef]
93. Ivanov,D.;Kalinin,M.;Krundyshev,V.;Orel,E. Automaticsecuritymanagementofsmartinfrastructuresusingattackgraph
andriskanalysis. InProceedingsofthe2020FourthWorldConferenceonSmartTrendsinSystems,SecurityandSustainability
(WorldS4),London,UK,27–28July2020;pp.295–300.[CrossRef]
94. Buyukkayhan,A.S.;Oprea,A.;Li,Z.;Robertson,W.LensontheEndpoint:HuntingforMaliciousSoftwareThroughEndpoint
DataAnalysis. InResearchinAttacks, Intrusions, andDefenses; SpringerInternationalPublishing: Cham, Switzerland, 2017;
pp.73–97.[CrossRef]

Electronics2025,14,2252 55of55
95. Nguyen,H.H.;Palani,K.;Nicol,D.M. AnApproachtoIncorporatingUncertaintyinNetworkSecurityAnalysis. InProceedings
oftheHotTopicsinScienceofSecurity:SymposiumandBootcamp,HoTSoS’17,Hanover,MD,USA,4–5April2017;pp.74–84.
[CrossRef]
96. Kato,Y.;Kanai,A.;Tanimoto,S.;Hatashima,T. Dynamicsecuritylevelanalysismethodusingattacktree. InProceedingsofthe
2017IEEE6thGlobalConferenceonConsumerElectronics(GCCE),Nagoya,Japan,24–27October2017;pp.1–3.[CrossRef]
97. Sonmez,F.O.;Hankin,C.;Malacaria,P. AttackDynamics:AnAutomaticAttackGraphGenerationFrameworkBasedonSystem
Topology,CAPEC,CWE,andCVEDatabases. Comput.Secur.2022,123,102938.[CrossRef]
98. Abraham,S.;Nair,S. Exploitabilityanalysisusingpredictivecybersecurityframework. InProceedingsofthe2015IEEE2nd
InternationalConferenceonCybernetics(CYBCONF),Gdynia,Poland,24–26June2015;pp.317–323.[CrossRef]
99. Kim,B.J.;Lee,S.W. AnalyticalStudyofCognitiveLayeredApproachforUnderstandingSecurityRequirementsUsingProblem
DomainOntology. InProceedingsofthe201623rdAsia-PacificSoftwareEngineeringConference(APSEC),Hamilton,New
Zealand,6–9December2016;pp.97–104.[CrossRef]
100. Ou,X.ABottom-UpApproachtoApplyingGraphicalModelsinSecurityAnalysis. InGraphicalModelsforSecurity;Springer
InternationalPublishing:Cham,Switzerland,2016;pp.1–24.[CrossRef]
101. Sion,L.;Yskout,K.;VanLanduyt,D.;Joosen,W. Knowledge-enrichedsecurityandprivacythreatmodeling. InProceedings
ofthe2018IEEE/ACM40thInternationalConferenceonSoftwareEngineering:Companion(ICSE-Companion),Gothenburg,
Sweden,27May–3June2018.
102. Wu,S.;Zhang,Y.;Chen,X. SecurityAssessmentofDynamicNetworkswithanApproachofIntegratingSemanticReasoning
andAttackGraphs. InProceedingsofthe2018IEEE4thInternationalConferenceonComputerandCommunications(ICCC),
Chengdu,China,7–10December2018;pp.1166–1174.[CrossRef]
103. Evrin,V.;CISA;CRISC;COBIT2019Foundation;CDPSE;CEHv9;ISO27001-22301-20000LA. Riskassessmentandanalysis
methods:Qualitativeandquantitative. ISACAJ.2021,2,1–6.
104. Sekharan,S.S.;Kandasamy,K. ProfilingSIEMtoolsandcorrelationenginesforsecurityanalytics. InProceedingsofthe2017
InternationalConferenceonWirelessCommunications,SignalProcessingandNetworking(WiSPNET),Chennai,India,22–24
March2017;pp.717–721.[CrossRef]
105. Cram,W.A.;Proudfoot,J.G.;D’Arcy,J. Whenenoughisenough:Investigatingtheantecedentsandconsequencesofinformation
securityfatigue. Inf.Syst.J.2020,31,521–549.[CrossRef]
106. Alahmari,A.;Duncan,B. CybersecurityRiskManagementinSmallandMedium-SizedEnterprises:ASystematicReviewof
RecentEvidence. InProceedingsofthe2020InternationalConferenceonCyberSituationalAwareness,DataAnalyticsand
Assessment(CyberSA),Dublin,Ireland,15–19June2020;pp.1–5.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.