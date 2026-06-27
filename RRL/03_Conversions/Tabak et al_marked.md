Article
Assessing the Drivers of Financial Vulnerability and Fraud in
Brazil: The Critical Role of Financial Planning over Literacy
BenjaminMirandaTabak*,† ,DéboraH.Cardoso† andCristianoC.Silva†
SchoolofPublicPolicyandGovernment,GetulioVargasFoundation(FGV/EPPG),SGAN602MódulosA,B,C,
AsaNorte,Brasilia70830-020,DF,Brazil;debora.cardoso@fgv.edu.br(D.H.C.);cristiano.silva@fgv.br(C.C.S.)
* Correspondence:benjamin.tabak@fgv.br
† Theseauthorscontributedequallytothiswork.
Abstract
This paper introduces and validates a comprehensive instrument designed to measure
financialliteracy,itsunderlyingdeterminants,andtoassesshowfactorssuchasplanning
affectfinancialvulnerabilityandfraudinBrazil. Thisworkrepresentsacrucialsteptoward
achievingseveralSustainableDevelopmentGoals(SDGs). Thestudyutilizesatwo-fold
methodology.First,ConfirmatoryFactorAnalysis(CFA)isusedtovalidateasix-component
modelconsistingofFinancialLiteracy,Vulnerability,Fraud,CognitiveReflection,Crypto
Literacy,andPlanning. Thisanalysisisfollowedbythedevelopmentandinterpretation
of a Random Forest model, which was identified as the best-performing predictor in a
comparisonofsevenmachinelearningalgorithms. TheCFAresultsshowedthatFinancial
Planning has a stronger negative correlation with Financial Vulnerability (−0.642) and
Fraud (−0.375) than Financial Literacy does. This evidence was further supported by
themachinelearninganalysis;analysesusingbothSHAPandLIMEidentifiedFinancial
Planning as the strongest predictor of financial vulnerability and fraud. The analysis
furthershowedsignificantsocialinequalitiesinthedevelopedmodelsandidentifiedthe
gender variable (female) as an important predictor of enhanced financial vulnerability.
ConvergingevidencefrombothCFAandmachinelearningconfirmsthatsoundplanning
practicesaremoreimportantthanfinancialknowledgeinreducingfinancialdistress. Our
findingsprovideasolidfoundationforthedevelopmentofinclusivepublicpolicythat
AcademicEditor:SajidAnwar promotesbehavioralchange,aimingtoreducesystemicinequalities(SDG10)andachieve
Received:30July2025 sustainableeconomicstability(SDG8),therebysupportingsocialgoalsandtheSustainable
Revised:18September2025 DevelopmentGoals.
Accepted:24September2025
Published:17October2025 Keywords: financial literacy; financial planning; vulnerability; financial behavior;
Citation: Tabak,B.M.;Cardoso,D.H.; sustainabledevelopment
Silva,C.C.AssessingtheDriversof
FinancialVulnerabilityandFraudin
Brazil:TheCriticalRoleofFinancial
PlanningoverLiteracy.Sustainability
1. Introduction
2025,17,9219. https://doi.org/
10.3390/su17209219 Lack of financial knowledge directly affects individuals’ ability to make informed
economicdecisions,therebydamagingtheirfinancialwell-beingintheshortandlongterm.
Copyright:©2025bytheauthors.
Thislimitationisespeciallyevidentinretirement,whenaccumulatedmistakesinfinancial
LicenseeMDPI,Basel,Switzerland.
Thisarticleisanopenaccessarticle managementbecomemoredifficulttocorrect. Studieshighlightthatlowfinancialliteracy
distributedunderthetermsand isassociatedwithinadequateeconomicchoices,suchasexcessiveindebtedness,lackof
conditionsoftheCreativeCommons planning,andgreaterexposuretofinancialfraud,negativelyimpactingindividualand
Attribution(CCBY)license
collectiveeconomicstability[1,2].
(https://creativecommons.org/
licenses/by/4.0/).
Sustainability2025,17,9219 https://doi.org/10.3390/su17209219

Sustainability2025,17,9219 2of33
Socioeconomicfactors,especiallylowschooling,furtherexacerbatefinancialvulnera-
bility,whichmakesitincreasinglyimportanttodevelopintersectionalinterventionsthat
reach groups of women, black individuals, and people with low schooling, who have
greaterdifficultyinaccessinggoodfinancialinformationandservices,takingintoaccount
theparticularitiesofeachone[3,4].
Itisimportanttonotethatfinancialliteracyreferstoasetofskills,goingbeyondjust
knowledgeaboutfinance. Thisisconfirmedwhenweanalyzetraditionalinterventionsthat
focusonlyoneducationalmethods,therebyneglectingbehavioralfactors. Interventions
suchasthesehavelowefficiency,whichrevealstheneedtodeveloppublicpoliciesthat
considerthebehavioralbiasesofindividuals,aswellasfinancialliteracy.
EspeciallyintheBraziliancontext,researchintofinancialliteracyasamultifaceted
element is even more necessary. The Brazilian Central Bank and the Credit Guarantee
Fundpointoutthatonascaleof0to100,theaverageleveloffinancialliteracyinBrazilis
59.6,withabout75%ofsurveyparticipantsobtainingamaximumscoreof70points,being
thosewithhigherlevelsofeducation. Thesamestudyshowsthat44.8%ofBraziliansin
thesamplesaidtheyneverorrarelyhadmoneyleftoverattheendofthemonth,and36%
wereconcernedaboutwhethertheywouldhaveenoughmoneytocovertheirexpenses.
Furthermore,theCentralBankpointsoutthat64%ofBraziliansfacefinancialinstability
andaround49.1%reportthatexperiencingfinancialworriesaffectstheirmentalhealth
on a personal and family level [5]. These data reveal Brazilians’ exposure to financial
vulnerability, which shows that there are still significant gaps to be filled in terms of
financialliteracyinBrazil,especiallyforminoritygroupssuchaspeoplewithlessaccessto
educationandformalfinancialservices.
Inthiscontext,investigatingtheelementsrelatedtofinancialliteracycanhelpinthe
developmentofinterventionsandpublicpoliciesthatcontributetoindividuals’financial
autonomyandwell-being. Financialeducationhasapositiveandsignificantinfluenceon
financialinclusionandtheattainmentofsustainablelivelihoods[6],andisconsidereda
pathtosustainability. Itisalsokeytoensuringthefinancialsustainabilityofindividuals,
families,businesses,andnationaleconomies[7],sinceeconomicgrowthandsustainability
dependonthefinancialeducationofindividuals.
FinancialliteracyisapillarfortheachievementofseveralSustainableDevelopment
Goals of the 2030 Agenda of the United Nations, related to poverty reduction (SDG 1),
increasedwell-being(SDG3),higher-qualityeducation(SDG4),genderequality(SDG5),
economic growth (SDG 8), reducing inequalities (SDG 10), and more responsible con-
sumption and production (SDG 12) [8]. This reinforces the indispensability of broad
and multifaceted research into financial literacy, as it is a driving force for individual
andcollectiveeconomicdevelopment,inadditiontocontributingsignificantlytopoverty
reduction[9].
Objectivemeasuresoffinancialliteracyareimportantforreducinginequalitiesbe-
tween people, as without financial literacy, they can face a series of problems, such as
difficultiesinmakinginformedinvestmentsorincurringlossesonassets,whichcanharm
theirfinancialwell-being. Nevertheless,financialliteracyasaconceptshouldbefurther
developedin terms ofalso coveringfinancial planningattitudes andusing newdigital
assetsasinvestmentproducts,suchascryptocurrencies. Ofequalimportanceismeasuring
knowledgeandattitudeimpactsacrossdesiredoutcomeindicators,suchasfinancialfraud
prevalenceorfinancialvulnerabilities. Thelatter,definedasfinancialprecariousnessor
alackoffinancialwell-being,hinderstheattainmentofSustainableDevelopmentGoal1,
aimedatachievingaworldwithoutpoverty,andatthesametimehindersSDG10,aimed
atreducinginequalities. Bothimpactsaresignificantandinhibitlong-termsustainable
developmentofacountry.

Sustainability2025,17,9219 3of33
Theprimaryobjectiveofthisworkistodevelopaninstrumentthatcomprehensively
measures financial literacy, encompassing aspects such as crypto literacy and financial
planning,andassesshowthesefactorsinfluencefinancialvulnerabilityandsusceptibility
tofinancialfraudamongindividuals,ultimatelyimpactingtheirfinancialwell-being. The
scopeofourinstrumentmayhelpfillgapsintheliterature,sinceitcanberelatedtoaspects
such as cognitive biases, financial fraud, and financial vulnerability. To the best of our
knowledge,thesedimensionshavenotbeenanalyzedinanintegratedmannertodate.
The structure of our paper is organized into interconnected sections. Initially, the
literaturereviewpresentsthefundamentalconceptsoffinancialliteracy,financialplanning,
andsusceptibilitytofraudandfinancialvulnerability. Next,inSection3usedtodevelop
andvalidatetheproposedinstrumentaredetailed,aswellastheexperimentalapplication.
Finally,inSections4and5provideinsightsintohowfinancialliteracycanbeincreased
andfinancialvulnerabilitiesreduced,withpracticalimplicationsforpublicpoliciesand
educationalprogramsinBrazil.
2. LiteratureReview
Thereisarelativelylargebodyofliteratureonhowindividualsdealwiththeirfinances.
Knowledge on this subject is essential because it provides conceptual inputs that help
people avoid putting themselves in a situation of financial vulnerability, especially in
scenariosofsocioeconomicinstability[1]. Abetterfinancialperceptioncontributestomore
assertivedecision-makingbasedoninformation,therebyreducingtheriskofindebtedness,
aswellaspromotingconditionsformoresustainableeconomicgrowth,financialinclusion,
andpositivefinancialbehavior[7,10].
Financialliteracyisunderstoodasanindividual’sabilitytounderstandandapply
financial concepts to make well-informed and more rational decisions [11–13]. In the
literature,severalfactorsareidentifiedasvariablesthatinfluencefinancialliteracy. These
include demographic and socioeconomic variations, with an emphasis on educational
attainment,age,andgender[11,14]. Anotherfactorhighlightedinrecentstudiesisthelack
ofaccessorlimitedaccesstoformalfinancialtechnologiesandservices[9].
Financialliteracyhasastrongeconomicandsocialimpact,asitenablesindividualsto
improvetheirfinancialwell-beinganddealwithsituationsoffinancialvulnerability[11].
The literature shows that people with greater financial literacy have greater autonomy
andabilitytomakeprudentandbeneficialdecisionsabouttheirfinanciallives,suchas
financialplanning,increasingsavings,andmanagingrisks[15]. Inadditiontodomestic
benefits,financialliteracyisalsoassociatedwithgreaterchancesofbusinesssuccess,since
moreliterateentrepreneurshavehigherincomesandsavings[13]. Furthermore,inrural
contexts,financialliteracyisalsoessentialforencouragingentrepreneurialactivities,which
contributetotheempowermentofruralcommunitiesandsustainabledevelopment[9].
Financial literacy contributes to people’s autonomy, enabling them to understand
economic scenarios and strategic resources and take more effective actions based on
planning, managing resources, calculating interest rates, diversifying investments, and
interacting with financial institutions. This contributes to making informed economic
decisions[1,16–24].
Understandingindividuals’attitudestowardstheuseofmoney,financialdecisions,
riskmanagementcapacity, andfinancialuncertaintiesistheobjectofstudyoffinancial
literacy[25,26]. Greaterfinancialliteracycontributestohealthierfinancialbehaviors,such
as greater savings, lower propensity to debt, greater financial planning capacity, and
betterparticipationinthestockmarket[2,20,27–29]. Theimportanceofthisknowledgeis
demonstratedbythenumberofpeopleunabletoanswersimplequestionsonthesubject,
as shown by an experiment carried out in the United States, in which only half of the

Sustainability2025,17,9219 4of33
respondentsovertheageof50wereabletogettwosimplequestionsaboutcompound
interestandinflationright[30]. Itisworthmentioningthatlowfinancialliteracyisaglobal
issuethatincludescountriessuchasGermany,Sweden,Italy,Japan,andNewZealand[26].
Importantaspectsofeconomiclifeareimpactedbyfinancialknowledge,asisthecase
withsavingforretirement. AstudycarriedoutintheNetherlandsfoundthatgettingmore
questionsrightaboutfinancialliteracycontributestoa10percentagepointincreaseinthe
abilitytoplanforretirement[26].Thenumberofsocialsecurityprograms,aimedatthemost
diversegroupsofindividualssuchaswomen,low-incomefamilies,andminorities[31],
revealsthegulfintheleveloffinancialliteracy,ascanbeseenamongwhitesandAsians,
whoaremoreknowledgeableinthisareathanAfrican-AmericansorHispanics[26].
Financialliteracyalsohelpstoreducefinancialvulnerability,aphenomenoncharac-
terizedbytheinabilitytopayunforeseenbills,highlevelsofdebt,andfrequentexposure
tofraud. Thisissueisveryworryingbecauseitrevealsastructuralproblemthatexposes
economicinequalities,financialexclusion,andalackoffinancialknowledge. Thisfinan-
cialvulnerabilitycanalsoaffectthehealthofindividuals,whichcanhaveanimpacton
physical and mental health, interpersonal relationships, and work performance [32,33].
Thetraininggeneratedbyfinancialliteracycontributestobettermanagementofsavings
andinvestments;thiscapacityreducesfinancialvulnerabilityandthusprovideseconomic
well-being[4,27–29].
Actionssuchasinadequatefinancialplanningandimpulsiveness,especiallyinthe
shortterm,arefactorspresentinthebehaviorofpeopleexposedtofinancialvulnerabil-
ity,whichmakesthemmoresusceptibletofraud,especiallyinascenariooflowdigital
inclusion[34].ThisisthecaseinBrazil,forexample,wherethelow-incomepopulationhas
noaccesstoformalfinancialproductssuchascreditandinsurance[3,4]. Andthisfinancial
exclusionleadstodependenceoninformalandpredatoryfinancialservices,whichmakes
thesituationofvulnerabilityevenworse[26].
Thelowlevelofknowledgeaboutbasicfinancialissuessuchasbudgeting,savings,
and credit as a result of a lack of financial literacy exposes individuals to vulnerability,
as recent studies have shown. This lack of knowledge makes it difficult to deal with
unforeseenevents,whichcontributestoexcessiveindebtedness. Theconsequenceofthis
behavior is the exclusion of low-income populations from the formal financial system,
increasingtheirexposuretofraudandunsustainablefinancialbehavior[4].
Financialliteracyisanimportanttoolforpromotingfinancialstability;understand-
ingthecostsassociatedwithcreditandavoidingunsustainablefinancingdecisions[35]
contributestothisresult. Thisknowledgecontributestobetterfinancialplanning,result-
ingintheestablishmentofemergencyreserves,whichreducesdefaultandalsohelpsto
strengthenindividualandcollectiveeconomicsecurity.
Understandingcryptocurrenciesisofparamountimportanceforassessingfinancial
knowledge. The1stNationalCryptocurrencySurveyinBrazilindicatesthatcryptoassets
havealreadysurpassedstocksininvestorpreference,showingthatinvestingincryptocur-
renciesisnowamongthefivemostpopularformsofinvestmentamongBrazilians. Despite
this,thesurveyshowsthatBrazilians’knowledgeofotheraspectsrelatedtothismarketis
stilllimitedandthereisalongwaytogointermsoffinancialeducation[36].
Theeffectivenessoffinancialliteracyisclearinitsroleincontributingtogoodfinancial
behaviorandreducingtheriskofvulnerability. Theliteratureshowsthatmorefinancially
literateindividualsdevelopmoreresilientbehaviorintimesofcrisis,reducingtheirex-
posuretoimpulsivebehaviorandfinancialfraud. Financialliteracyalsocontributesto
financialinclusionandsustainableeconomicdevelopment[7,37].Inscenarioscharacterized
byexclusionandeconomicinstability,financialliteracyhighlightsitsimportanceasatool

Sustainability2025,17,9219 5of33
forchange. Thisreinforcestheimportanceofinitiativesthatsupporttheexpansionand
betterdisseminationoffinancialliteracyatdifferentlevelsofsociety.
Substantialamountsofliteratureconfirmtheimportanceofindividual-levelfinancial
literacytopersonalaswellasmacroeconomicwell-being. However,scholarlyinvestiga-
tionhasprogressedmainlyinacompartmentalizedandunconnectedmanner. Thepast
literaturecanbroadlybecategorizedintoafewdifferentcamps: (1)studiesfocusingon
basicknowledgeoffinancewhereofteninterestcompounding,inflation,orriskdiversi-
fication(e.g.,[26,30])aretested,amongotherfactors;(2)behavioralfinancestudiesthat
investigatehowspecificcognitivebiases(e.g.,overconfidencebiasorlossaversion)impact
individual-levelfinancialdecision-making(e.g.,[38,39]);(3)socioeconomicexaminations
thatassessdriversoffinancialinsecurityoftenlinkingittovariablessuchasrace,gender,
orincome;or(4)recentscholarshipwhereawarenessregardingnewfinancialinstruments
suchascryptocurrenciesisexploredbutoftenfoundtobeunrelatedtomoretraditional
literacytesting. Whiletheserepresentworthwhileendeavorsindividually,theycollectively
presentanincompletepicture.
The key research gap, then, is the absence of a unifying, multidimensional frame-
workthatsimultaneouslyexaminesthesecomponents. Currentscholarshipfallsshortof
adequatelyexamininginterdependenciesamongfinancialliteracy(bothtraditionaland
novel),behavioralinclinations(e.g.,planning),cognitivetraits(e.g.,biasesandreflective
thinking),andreal-worldresults(relatedtobeingvulnerableorbeingafraudtarget)within
asingleframework. Accordingly,anambiguousunderstandingremainsregardinghow
theseforcesinteracttoimpactone’sindividualfinancialresilience. Additionally,acrucial
consideration missing from this fragmented landscape is an explicit connection to sus-
tainabledevelopment. WhilefinancialinclusionisoftenalignedwiththeUnitedNations
SustainableDevelopmentGoals(SDGs),existingscholarshiphasfailedtoadequatelyex-
plorehowthequalityoffinancialliteracy—encompassingbehaviors,cognitiveresilience,
andvulnerability—facilitatessocialandeconomicsustainability. Forinstance,variations
infinancialliteracyandvulnerabilitybyraceandgendertranscendeconomicissuesand
embodythecausesofsocialinjusticesthatunderminesocialsustainability,especiallywith
respecttoSDG5: GenderEqualityandSDG10: ReducedInequalities. Similarly,household
financevolatilityhasadirectimpactonanation’seconomicresilience,delineatingacore
componentofSDG8(DecentWorkandEconomicGrowth).
Our work aims to address these broad deficits through three key avenues. First,
wemovebeyondtheindividualisticmethodologybypositingandtestinganintegrated
frameworkthatsimultaneouslyconsidersbasicfinancialliteracy,knowledgeaboutcryp-
tocurrency, financial planning, reflective thinking, and cognitive bias. Secondly, as a
necessarymethodologicalinnovation,wedesignandvalidateanew,omnibusinstrument
speciallydevelopedfortheBraziliansetting,whichsimultaneouslymeasuresthesediverse
constructs. WeestablishthereliabilityandvalidityofsuchaninstrumentthroughCon-
firmatoryFactorAnalysisandthusprovideasturdytoolforfutureresearchapplications.
Finally,byincludingsocioeconomicanddemographicvariables(suchasraceandgender)
alongsidecovetedoutcomemeasures(suchasfinancialvulnerabilityandfraudexperience),
ourexploratoryworkestablishesadirectempiricallinkbetweenthemultifaceteddimen-
sionsoffinancialliteracyandtheoverallgoalsofsocialandeconomicsustainability. In
doingso,wereconceptualizefinancialliteracyasacriticalcomponentforbuildingfairer,
moreresilient,sustainablesocieties,beyondamereconcernforindividualwealth.

Sustainability2025,17,9219 6of33
3. MaterialsandMethods
3.1. Sampling
ThisresearchreceivedapprovalfromtheEthicsCommitteeonResearchInvolving
HumanSubjectsoftheGetulioVargasFoundation—CEPH/FGV(P.214.2024). Datacol-
lection commenced upon the acquisition of ethical permission. All study participants
providedinformedconsent. Thegivendetailsencompassedthestudy’saim,confidentiality,
participantautonomy,voluntaryparticipation,therighttowithdrawatanytime,andthe
guaranteethatallacquireddatawouldbeanonymizedtosafeguardparticipantidentity.
Althoughouranalysisshedslightontherelevantdeterminantsofvulnerabilityandim-
proprietyinfinancialdealingsinBrazil,itisimportanttoconsiderthespecialcharacteristics
ofoursampleininterpretingthefindings.
We conducted our data collection through direct contact at urban focal points, in-
cluding shopping centers, bus and subway terminal stations, and public spaces in the
FederalDistrict. Specifically,ourconveniencesamplingwasemployedtoachievearepre-
sentativecoverageofthepopulationbytheirsocioeconomiclevels,educationallevels,and
occupation. Thetotalsizeofthesamplewas256participants.
Despitethis,however,weareawareofthefollowinglimitationsassociatedwiththe
coverageofthesample.First,ourfocusonanurbanpopulationmeansthatthesampledoes
notcapturetheviewsofpopulationsinruralorotherremotelocations,andmayfacesome
pecuniaryissues,aswellasdisparateaccesstoinfrastructureforfinancesandinformation
technology. Secondly, the survey covered mostly the Federal District. This territory is
characterizedbyhighinternalmobilityanddemographicdiversity,whichincreasesthe
diversityofthesample. However,givenitsuniqueeconomicfeaturesastheadministrative
seatofthegovernment,itmaynotberepresentativeofotherBrazilianstates.
As such, it is critical to be cautious in extrapolating these findings to the broader
Brazilianpopulation.Thecombinationofplanning,literacy,andvulnerabilitymaybelikely
influencedbylocaleconomicfactorsandculturalnorms,whichareaddressedbythisstudy
inlimitedways. AlthoughthepopulationintheFederalDistrictisverydiverse,withmost
residentscomingfromdifferentpartsofthecountry,large-scalemigrationmayresultin
somestatesinBrazilbecomingmorehomogeneous,andthesefactorsmayworkindifferent
ways. Nonetheless,thisstudyaddstothecreationofasoundframeworkinunderstanding
nuancedrelationsoffinanceswithinaheterogeneousurbanenvironmentinBrazil. We
showhowitisimportanttoexpandfinancialeducationprogramsbyincorporatingkey
elements,likeplanningfinances,toinformintensivepublicpolicyactions.
DatawerecollectedthroughtheSurveyMonkeyplatformversion4.5.7,usingelectronic
devices. ThedatawaskeptinSurveyMonkey’scloud-baseddatabase,whichkeepsthe
dataencryptedaccordingtotheSOC2standard.
3.2. Instrument
In addition to socioeconomic questions, our instruments comprise items adapted
to Brazilian reality, ensuring good consistency and reliability (we used Confirmatory
Factor Analysis to evaluate the instruments and reduce the number of items to obtain
reliableandvalidinstruments,whichweusedfortheeconometricandmachinelearning
analysis). Wedevelopedacomprehensivefinancialliteracyinstrument,whichcomprises
corefinancialliteracyitems(FL).Wealsoincludedfinancialplanning(FP)andknowledge
on cryptocurrency (Crypto). This instrument has two knowledge dimensions (FL and
crypto)andanattitudedimension,whichisfinancialplanning.
WeevaluatedtheimpactoftheBroadFLinstrumentonfinancialvulnerability(VF)or
financialfraud(FV).Thesetwovariablescaptureanoutcomedimension,whererespondents
havesufferedfromfinancialvulnerability(i.e.,severalbillspastdue)orfinancialfraud

Sustainability2025,17,9219 7of33
(i.e.,sufferedlossesfromFF).Wealsomeasuredthereflectiveandanalyticalthinkingof
respondents using the Cognitive Reflection Test (CRT). In addition, we measured four
cognitive biases and control variables, including gender, race, age, and income. It is
importanttohighlightthatthefinalinstrumentfollowstheresultsfromtheConfirmatory
FactorAnalysis,regardingthegoodnessofthemodelfitandthereliabilityandvalidityof
thelatentfactors.
3.3. FinancialLiteracy—CoreKnowledge
Financial knowledge was measured using the main instrument (the Big Five) de-
veloped by Lusardi and Mitchell [26]. This is a widely used instrument for measuring
financial literacy, which provides a standardized and comparable measure of financial
knowledgebetweendifferentcountriesandgroups. Themainobjectiveofthe“BigFive”,
whichisanexpandedversionofthe“BigThree”[25],istoprovideaconsistentmeasure
offinancialknowledge. Consistingofquestionsonsimpleinterestrates,inflation,bond
prices,mortgages,andriskdiversification,thequestionnaireprovidesanexpandedviewof
respondents’financialknowledge[25].ToadaptittotheBraziliancontext,wetranslatedthe
instrumentbyreplacing“mortgage”with“financing”. Wealsoincludedonequestionfrom
financialknowledgefromtheFinancialLiteracySurvey[40]whichmeasuresinvestment
knowledgefocusingonreturnoninvestment.
Next, we selected two self-perception questions on financial knowledge from the
FinancialLiteracySurvey[40]. Thesequestionsallowedustoanalyzewhetherpeoplewho
havehadaccesstofinancialeducationmanagetheirfinancesbetterandhowconfidentthey
areintheirfinancialknowledge.
Wecovereddifferentaspectsoffinancialliteracy,andtoassessthisaspect,weused
threequestionsfromtheFinancialLiteracyQuiz[40]. Thisisatoolbasedontherecommen-
dationsoftheFinancialLiteracyMap,aJapaneseframeworkcreatedbytheCommitteefor
thePromotionofFinancialEducation. Inordertocoverdifferentcharacteristicsoffinancial
literacy,weincludedquestionsonfamilybudget,financialknowledge,understandingof
financial/economiccircumstances,appropriateselection/useoffinancialproducts,and
appropriateuseofexternalexpertise.
Toensurethatthescoreoffinancialknowledgereflectedtherealresult,weusedthe
methodofItemResponseTheory(IRT).IRTmodelsanalyzeindividualitemperformancein
relationtooverallability,allowingformoreprecisemeasurementoffinancialliteracyand
providinginsightsintothedifficultyanddiscriminatingpowerofeachquestion. Eachitem
inatesthasconstraints,suchasdifficulty,discrimination(abilitytodifferentiatebetween
peoplewithdifferentskilllevels),andtheprobabilityofgettingitrightbychance.
WeutilizedamultidimensionalItemResponseTheorynamedmirt. Themirtsoftware
wasdevelopedtoestimatemultidimensionalitemresponsetheoryparametersforboth
exploratoryandconfirmatorymodelswithmaximum-likelihoodapproaches[41]. Weuse
RSoftwareversion4.5.1whitMirtpackageversion1.45.1.
Afteranalyzingtheeightquestionsintheinstrument,theIRTmethodidentifiedone
question(three)thatparticipantshaddifficultyanswering,eventhosewithhighliteracy,
whilesomewithlowliteracyalsoansweredcorrectly. Wehavedecidedtodisregardthis
questioninthescoring(Figure1).
WealsoemployedConfirmatoryFactorAnalysis,retainedonlyfouritemsthathad
highloadings,andimprovedthepsychometricpropertiesoftheseinstruments. Thefinal
instrumentsareprovidedinAppendixC.

Sustainability2025,17,9219 8of33
Figure1.ItemCharacteristicCurve(ICC)graphsforeachquestionintheItemResponseTheory(IRT)
model,inthiscasea2PLmodel(two-parameterlogisticmodel).Foreachitem,thegraphshowsa
curvethatrepresentsthechanceofacorrectresponsetothequestion,asafunctionoftheperson’s
latentability(θ).X-axis:latentability(θ)from−6to+6.Thisisthelevelofproficiencyorfinancial
literacy.θ=0istheaverageabilityinthesample.θ>0indicatesmore“skilled”individuals.θ<0
indicatesindividualswithbelow-averageability.Y-axis:probabilityofacorrectresponsefrom0to1.
Showsthechanceofanindividualwithabilityθgettingtheitemright.Thesteeperandhigherthe
curve,thebettertheitemdiscriminatesbetweenabilitylevels.
3.4. FinancialPlanning
Financial planning was based on research by Anderloni et al. [42]. Six questions
wereselected,focusingonpersonalbehaviorandattitudes,suchascriticalthinkingbefore
buyingsomething,settingfinancialgoals,personalvigilanceinfinancialmatters,paying
bills on time, and people with divergent thinking, such as living for today and letting
tomorrowtakecareofitself. Weoptedtoadoptascaleofonlytworesponseoptionsforthe
instrument’sitems,attributingoneiftherespondentagreedtosomeextentwiththetext. It
shouldbenotedthattherearenocorrectorincorrectanswers,andthescoreobtainedisa
directmeasureoftherespondents’leveloffinancialplanning. Hence,alowerscorereflects
alowerleveloffinancialplanning.
3.5. CryptocurrencyLiteracy
For knowledge of cryptocurrencies, four items were selected from an instrument
initially developed by Al-Omoush et al. [43], based on an empirical study and items
takenfromrelevantstudiesintheliteratureonfinancialliteracy. Theoriginalinstrument
contains 24 items, divided into six scales with 4 items each. In addition, three experts
in cryptocurrencies, financial technology, and investments in financial assets reviewed
thisinstrumenttoevaluatethemeasuresandrefinetheitems,ensuringtheinstrument’s
accuracyandrobustness. Asfarastheanswersareconcerned,respondentsmustscoreeach
itemaccordingtoaLikertscale,rangingfrom1(stronglydisagree)to5(stronglyagree).
The original instrument consists of six scales, developed and validated based on
the relevant literature, namely (i) financial literacy, which assesses the knowledge and
abilitytodealwithfundamentalconceptsofcryptocurrencies[44,45];(ii)perceivedvalue,
whichemphasizestheperceivedbenefitsofusingcryptocurrencies,suchassecurityand
efficiency [46]; (iii) optimism, which measures users’ positive outlook on the future of
cryptocurrencies[47,48];(iv)cryptocurrencydependence,basedonthescalesproposed
bySonkurtandAltınöz[49]andKiatsakaredandChen[50],whichevaluatescompulsive
behaviorsandnegativeimpactsrelatedtoexcessiveuse;(v)trust,addressingtheperceived
securityandreliabilityofcryptocurrencytransactions[51,52];and,finally,(vi)intention

Sustainability2025,17,9219 9of33
tocontinueusing,whichexaminesthelong-termbehavioralintentiontocontinueusing
cryptocurrencies[53,54].
Todeveloptheinstrumentusedinthisstudy,onlytheitemsrelatedtothefinancial
literacyscalewereselectedtogaugetheparticipants’self-perceptionoftheirknowledge
aboutthecryptocurrencymarketandriskassessment. Unliketheoriginalstudy,weopted
to adopt a scale of only four response options for the instrument’s items, 1 (“strongly
disagree”),2(“disagree”),3(“agree”),and4(“stronglyagree”). Itshouldbenotedthat
therearenocorrectorincorrectanswers,andthescoreobtainedisadirectmeasureofthe
respondents’levelofknowledgeandperception. Hence,alowerscorereflectsalowerlevel
ofknowledgeaboutcryptocurrencies.
3.6. FinancialVulnerability
ThequestionnairedevelopedinthisstudywasbasedonresearchbyAnderlonietal.[42],
whosemainobjectiveistoproposeafinancialvulnerabilityindicator(FinancialVulnerabil-
ityIndex)thatsummarizesdifferentaspectsofthefinancialstressfacedbyfamilies,such
asexcessiveindebtedness,inabilitytocovermonthlyexpenses,latepaymentsandother
conditionsoffinancialinstability,aswellasanalyzinghowthecharacteristicsoffamilies
arerelatedtotheleveloffinancialvulnerability.
The study questionnaire covers five main areas to measure the degree of financial
vulnerabilityoffamilies: (i)sociodemographiccharacteristics;(ii)economicandfinancial
profile,whichinvestigatesthelevelofincome,financialwealthandassets,typesofdebt
(secured or unsecured), employment status, and use of risk management instruments,
suchasinsurance;(iii)financialliteracy;and(iv)economicandfinancialsituation,which
exploresdifficultiesinbalancingmonthlyexpensesanddealingwithunexpectedexpenses.
Theitemsincludedinourquestionnaireessentiallyconcernsecureaccesstocreditlines,
financialwell-being,householdexpenses,andaccesstohealthservices.
3.7. FinancialFraud
Tocomposethisdimension,weusedquestionsonfinancialfraud(FF)fromtheAssess-
mentofFinancialConsumerSurveyReport(2018)andtwoquestionsonsecurefinancial
behaviorfromtheFinancialLiteracySurvey[40]. Theitemswereselectedtoinvestigate
thevulnerabilityofindividualstoeconomiccrimeandfinancialfraud. Thesequestionsare
basedonstudiesexaminingexposuretoeconomiccrimeandtheroleoffinancialliteracyin
preventingit[55],aswellasreportssuchastheAssessmentofFinancialConsumerSurvey
Report(2018),whichanalyzestheimpactoffinancialfraudinvariouscontexts.
3.8. CognitiveReflectionTest
We used the 7-item Cognitive Reflection Test [56]. The Cognitive Reflection Test
is a psychological tool widely used to measure an individual’s propensity to resort to
reflective and analytical thinking rather than relying on intuitive and rapid responses.
DevelopedbyShaneFrederick,theCRTwasinitiallydevelopedwithjustthreequestions,
buthasevolvedtoincludemorecomprehensiveversions,suchastheseven-itemversion.
This expansion aimed to increase the test’s accuracy and ability to capture nuances in
participants’cognitivestyle.
TheCRTisbasedonthedualthoughtprocessmodel,whichdistinguishesbetween
twocognitivesystems: System1,whichisintuitive,fast,andautomatic,beingresponsible
forimpulsiveresponsesthatoftenleadtoerrorduetohighsusceptibilitytoopticalillusions,
andSystem2,whichisreflective,slow,anddeliberate,requiringgreatercognitiveeffortto
suppressintuitiveresponsesandreachmorereasonedsolutions[39,57–60]. CRTquestions
aredesignedtoexploitthisdynamic,presentingproblemsthatappearsimpleatfirstglance
butcontaincognitivetrapsdesignedtoinduceincorrectanswers.

Sustainability2025,17,9219 10of33
TheexpandedversionoftheCRT,withsevenitems,maintainsthelogicoftheoriginal
version, butincorporatesagreaternumberofquestionstodiversifythechallengespre-
sentedandimprovethereliabilityoftheresults. Thesequestionsarecarefullyformulated
toprovokeintuitiveerrorsandchallengetheparticipanttoresorttoanalyticalthinking.
For example, one of the classic questions in the three-item version asks: “A bat and a
ball together cost $1.10. The bat costs $1 more than the ball. How much does the ball
cost?” TheintuitiveandwronganswerwouldbeUSD0.10,whilethecorrectanswer,USD
0.05,requiresmorein-depthreasoning. Intheseven-itemversion,similarproblemsare
presented,coveringawiderspectrumofmathematicalandlogicalreasoning.
ScoringontheCRTissimpleandstraightforward,witheachcorrectanswerworth
onepoint,resultinginatotalscorerangingfrom0to7. Interpretingtheresultsprovides
insight into the participant’s cognitive style: lower scores indicate a strong reliance on
intuitivethinking,whilehigherscoresreflectagreatercapacityforanalyticalreasoning. In
addition,itispossibletoanalyzeintuitivewronganswers,whichofferinsightsintohow
oftenautomaticthinkingdominatesdeliberativethinking.
WeemployedConfirmatoryFactorAnalysisfortheCognitiveReflectionTest,retained
onlyfiveitemsthathadhighloadings,andimprovedthepsychometricpropertiesofthese
instruments. ThefinalinstrumentsareprovidedinAppendixC.
3.9. CognitiveBiases
Wealsoincludedfourcognitivebiasestotestiftheyarerelatedtofinancialliteracy
(corecompetencies),financialvulnerability,andfinancialfraud. Ourhypothesisisthatif
respondentsarepronetocognitivebiasesthentheymayhavelowerfinancialliteracyorbe
morelikelytohavefinancialvulnerabilityorfinancialfraudproblems[40].Takingcognitive
biases into consideration may help us to understand why so many people may have
difficultiesinavoidingfinancialtroublesorfinancialfraud. Cognitivebiasesarerelatedto
behaviorsthatdeviatefromrationalityandthereforemayexplainthesefinancialoutcomes.
Theitemsweredevelopedbasedonthepremisesofbehavioraleconomicsandexplore
the general characteristics of behavior in addition to specific biases that are fundamen-
tal to financial decisions, such as loss aversion, herd behavior, myopic behavior, and
hyperbolicdiscounting.
• Aversiontoloss:
Lossaversionisthecognitivebiasthatexplainswhyindividualsfeelthepainofloss
twice as intensely as the satisfaction generated by a gain of equal value [38]. This
biasdirectlyaffectsindividuals’financialdecisions,fromtheirinvestmentchoicesto
thechoiceofwhichgroceriestobuyatthesupermarket[61]. Thisisbecausepeople
affectedbythisbiaswillfocusmoreonpotentialcostsandfailuresthanonpotential
gainsandbenefits[62,63].
• Herdbehavior:
Herdbehaviorreferstothetendencyofindividualstofollowtheactionsordecisions
ofagroup,eventhoughthesechoicesmaybeirrationalorinconsistentwiththeirown
preferences. Thisbehaviorisinfluencedbythebeliefthattheactionsofthemajority
reflect superior information or decisions, leading individuals to ignore their own
judgments,somethingreinforcedbyfactorssuchassocialpressureandthesearchfor
validation[64,65]. Inthefinancialcontext,itsimplicationsaresignificant: collective
decisions, such as mass asset sales or purchases, can create economic bubbles or
crises[66]. Thus,herdbehaviornotonlyreducesthediversityofdecisionsbutalso
contributestovolatilityandsystemicrisksinfinancialmarkets.
• Short-sightedbehavior:

Sustainability2025,17,9219
11of33
Short-sighted behavior is marked by an exaggerated focus on immediate rewards,
whichcanleadtoimpulsivedecisions,suchasimpulsepurchasesandprocrastination,
prioritizingmomentarysatisfactionsthatcancausefutureregrets[67]. Peopleaffected
bythisbiastendtoseeonlyisolatedpartsofasituation,whichmakesthemignore
thesituationasawhole,leadingthemtodecisionsthatleadtoreducedgainsatthe
expenseofgreateropportunities[68].
|     |     |     | • Hyperbolicdiscount: |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hyperbolicdiscountingreferstothetendencytoundervaluefuturerewardstothe
detriment of immediate ones [69]. Behavior like this has a significant impact on
financial decisions, causing people to opt for immediate benefits, such as impulse
purchases,ratherthanlong-termbeneficialchoices,suchassavingforretirementor
investments[70,71]. Thistypeofbehaviorcanleadtofinancialproblems,suchasdebt
and lack of planning [72]. Understanding hyperbolic discounting and looking for
waystoovercomeitiskeytoimprovingpersonalandsocialfinancialstability.
|     |     |     | 3.10. MultipleLinearRegression |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
WeusedOrdinaryLeastSquares(OLS)toinvestigatetherelationshipbetweenvari-
ables. Thisisawidelyusedstatisticalmethodtoestimatethecoefficientsofalinearregres-
sionmodel[73]. Themultiplelinearregressionmodelwasappliedtoexplainthefollowing
dependentvariables:financialliteracy(FL),financialvulnerability(FV),andfinancialfraud
(FF).Allregressionswereestimatedwithrobuststandarderrorsforheteroskedasticity,and
theresultsaredisplayedinAppendixA.
Inourmodelingstrategy, wefirstassessedthepredictorsoffinancialliteracy(FL),
whichincludestheCognitiveReflectionTest(CRT).Subsequently,weusedtheresultingFL
score,alongsideothervariables,topredictbothfinancialvulnerability(FV)andfinancial
fraud(FF).
Oneofourkeyobjectiveshereistoassesswhetherknowledge-basedorbehavior-based
dimensionsoffinancialliteracyhaveamoresubstantialimpact. Assuch,wedeliberately
lookedatthesefactorsindividually.Weframeourmethodologywiththefollowingreasoning:
Hypothesis1: Wehopedtodetermineifthebehavioraldimension(financialplanning)wouldbea
betterpredictorthantheknowledgedimensionforfinancialresults(fraudandvulnerability).
Todistinguishthiseffect,weexaminedthedimensionsindividually.
Ourgeneralmultiplelinearregressionmodelcanberepresentedmathematicallyas:
FL = βFL+βFLCRT +βFLFemale +βFLNonBinary +βFLBlack +βFLOtherRace
|     | i 0 | 1   | i   | 2   | i   | 3   |     | i   | 4   | i   | 5   | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
+βFLYoung +βFLOld +βFLLowIncome +βFLHighIncome +βFLLossAversion
|     |                | 6   | i             | 7                | i 8        |             |            | i          | 9             | i             | 10  |     | i   |     |
| --- | -------------- | --- | ------------- | ---------------- | ---------- | ----------- | ---------- | ---------- | ------------- | ------------- | --- | --- | --- | --- |
|     | +βFLMyopic     |     |               | +βFLDiscount     |            | +βFLHerding |            | +ε         | ,             |               |     |     |     | (1) |
|     |                | 11  | i             | 12               |            | i           | 13         | i          | i,FL          |               |     |     |     |     |
|     | = βFV+βFVFL    |     | +βFVFP        |                  | +βFVCrypto |             | +βFVFemale |            | +βFVNonBinary |               |     |     |     |     |
| FV  | i              |     | i             |                  | i          |             |            |            | i             |               |     |     |     |     |
|     | 0              | 1   |               | 2                | 3          |             | i          | 4          |               | 5             |     | i   |     |     |
|     | +βFVBlack      |     | +βFVOtherRace |                  |            | +βFVYoung   |            | +βFVOld    |               | +βFVLowIncome |     |     |     |     |
|     |                | 6   | i             | 7                |            | i           | 8          | i          | 9             | i 10          |     | i   |     |     |
|     | +βFVHighIncome |     |               | +βFVLossAversion |            |             |            | +βFVMyopic |               | +βFVDiscount  |     |     |     |     |
|     |                | 11  |               | i                | 12         |             | i          | 13         | i             | 14            |     | i   |     |     |
+βFVHerding
|     |             |     |               | +ε i,FV | ,          |           |            |         |               |               |     |     |     | (2) |
| --- | ----------- | --- | ------------- | ------- | ---------- | --------- | ---------- | ------- | ------------- | ------------- | --- | --- | --- | --- |
|     |             | 15  |               | i       |            |           |            |         |               |               |     |     |     |     |
| FF  | = βFF+βFFFL |     | +βFFFP        |         | +βFFCrypto |           | +βFFFemale |         | +βFFNonBinary |               |     |     |     |     |
|     | i 0         | 1   | i             | 2 i     | 3          |           | i          | 4       | i             | 5             | i   |     |     |     |
|     | +βFFBlack   |     | +βFFOtherRace |         |            | +βFFYoung |            | +βFFOld |               | +βFFLowIncome |     |     |     |     |
|     |             | 6   | i             | 7       |            | i 8       |            |         | 9 i           | 10            |     | i   |     |     |
i
|     | +βFFHighIncome |     |     | +βFFLossAversion |     |     | +βFFMyopic |     |     | +βFFDiscount |     |     |     |     |
| --- | -------------- | --- | --- | ---------------- | --- | --- | ---------- | --- | --- | ------------ | --- | --- | --- | --- |
|     |                | 11  |     | i                | 12  |     | i          | 13  | i   | 14           | i   |     |     |     |
|     | +βFFHerding    |     |     | +ε ,             |     |     |            |     |     |              |     |     |     | (3) |
|     |                | 15  |     | i i,FF           |     |     |            |     |     |              |     |     |     |     |
Theindependentvariablesusedinthemodelsaredefinedasfollows:

Sustainability2025,17,9219 12of33
FL—Latentvariableforfinancialliteracymeasuredbyfourobservedindicators;
FP—Latentvariableforfinancialplanningmeasuredbysixobservedindicators;
Crypto—Latentvariableforcryptocurrencyknowledgemeasuredbyfourobserved
indicators;
CRT—ReferstotheCognitiveReflectionTest,whichmeasurestherespondent’sability
tooverrideintuitivebutincorrectanswerswithreflectiveandaccuratereasoning;
Female—Representsthegenderoftherespondent,isadummyvariableequalto1if
therespondentidentifiesasfemale;
NonBinary—Representsthegenderoftherespondent,isadummyvariableequalto1
iftherespondentidentifiesasnonbinary;
Black—Is a dummy variable equal to 1 if the respondent identifies as Black. For
ouranalysis,wecombinedblackandmixed-racegroups,consistentwithpreviousstud-
ies[74–76];
OtherRace—Isadummyvariableequalto1iftherespondentidentifiesasbeingof
AsiandescentorIndigenous;
Young—Isadummyvariableequalto1iftherespondentisbetween18and30yearsold;
Old—Isadummyvariableequalto1iftherespondentis56yearsoldorolder;
LowIncome—Isadummyvariablethatrepresentsindividualsearninguptothreetimes
theminimumwage;
HighIncome—Is a dummy variable representing individuals earning more than
tentimestheminimumwage;
LossAversion—Indicatestherespondent’stendencytoavoidfinanciallosses;
Myopic—Captures the preference for immediate rewards over long-term benefits,
indicatingshort-termfinancialbehavior;
Discount—Reflects a preference for consumption rather than saving, indicating a
present-biasedpreference;
Herding—Measuresthetendencytofollowthebehaviorofthemajorityinfinancial
decision-making.
3.11. MachineLearning
Machinelearningisasubsetofartificialintelligencethatenablescomputerstoacquire
knowledgeandenhancetheirperformancethroughdata. Machinelearningmodelsare
algorithmstrainedondatatoidentifyspecificpatternsorgeneratechangesinpreviously
unobserveddatasets. Amultitudeofclassificationmethodshavebeenpresentedinthe
machinelearningliteratureanddatascience[73].
In this section, we utilize supervised learning techniques [77] to forecast the key
attributesthatareimportantforassessingFL,FV,andFFindices.Initially,weevaluatemany
classicmachinelearningapproachestoidentifythemostappropriateoneforourdataset.
This is significant as machine learning models are often employed to make judgments
withtangiblereal-worldimplications,particularlyinsectorssuchashealthcare,banking,
criminaljustice,andenergy[78].
3.11.1. HorseRace
Weconductedacompetitiveevaluationofsupervisedregressorstoidentifytheoptimal
machine learning technique that enhances model performance to explain the average
financialliteracy(FL),financialvulnerability(FV),andfinancialfraud(FF).Formodelingwe
usedthetidymodelsframeworkforRVersion1.4.1,theresultsarepresentedin(Figure2).
K-NearestNeighbors—Thefundamentalconceptofnearestneighbormethodsisto
identifyacertainnumberoftrainingsamplesthatareclosestinproximitytoanewpoint
andtopredictitslabelbasedonthosesamples. Thequantityofsamplesmaybeauser-

Sustainability2025,17,9219 13of33
definedconstant(k-nearestneighborlearning)orfluctuateaccordingtothelocaldensity
of the points (radius-based neighbor learning). The distance can often be any metric
measurement,withtheconventionalEuclideandistancebeingthemostprevalentoption.
Neighbor-basedapproachesareclassifiedasnon-generalizingmachinelearningtechniques,
astheyutilizeallavailabletrainingdata,potentiallyorganizedintoanefficientindexing
structure,suchasaballtreeoraKDtree[79].
SVMs—These are learning machines for classifying two groups. They map input
vectorsnonlinearlytoahigh-dimensionalfeaturespace,wherealineardecisionsurface
isconstructedwithpropertiesthatensurehighgeneralizationcapacity. Onlythesupport
vectors, which define the maximum margin of separation between classes, are used to
constructthissurface. SVMsusethe“kerneltrick”toefficientlycreatenonlineardecision
surfacesinhigh-dimensionalspaces. Fornon-separabledata,theyapplysoftmarginsto
allowforcontrollederrors,increasingrobustness[80].
RandomForests—Theyconsistofcollectionsofclassifiersthataretree-based,inwhich
eachtreeisgrownindependentlybyusingarandomvector. Theforestsvotebyoutput,
andthegeneralizationerrorconvergeswithoutoverfitting. RandomForestsarealsorobust
againstnoiseandyieldhighaccuracywithnumerousweakandcorrelatedinputs[81].
XGBoostisatypeofensemblelearningthatusestheGradientBoostingalgorithm. Itis
acommonchoiceformanymachinelearningtasks,especiallywhenitcomestoclassifying
andregressingstructureddata. Italsoletsyouusemorethanoneprocessortospeedupthe
trainingofthemodel. Itboastsconsiderablespeed,precision,androomforgrowth[80].
Amultilayerperceptron(MLP)isatypeofneuralnetworkthathasthreelayers: input
units,hidden(orinternal)units,andoutputunits. Thehiddenunits’principaljobisto
make internal representations of the input patterns. This enables the network to solve
issuesthataremorecomplexthanthosethattwo-layernetworkscanhandle. TheMLP’s
purposeistolearnhowtomatchtheinputpatternstotheoutputpatternsthatarewanted,
whichwillhelpitmakegoodgeneralizations[82].
ElasticNetisapenalizedregressionthatoutperformsLassowhenmorepredictors
exist than observations (p > n) or in situations of correlation of predictors. The model
involvesbothL1(Lasso)andL2(Ridge)penalties. Forstabilityandmodelprecision,Elastic
Netchoosesmorevariablesandranksthosethatexhibitinterrelationshipsamongthem[83].
Linearregression,beingoneofthefundamentalmethodsundersupervisedmachine
learning,makesuseofoneormultipleindependentvariablestopredictacontinuously
valuedresponse(thedependentvariable). Acommonmethodtoestimatethismodelisthe
OrdinaryLestSquares(OLS)regression[84].
Figure2.Horseracingoutcomes:Ontheleft,wepresenttheresultsforfinancialliteracy,financial
vulnerabilityandfinancialfraud.ThepointsrepresenttheaverageRMSEachievedinthefoldnot
utilizedfortrainingthroughout5separateiterationsofourcross-validation. Thehorizontalbars
representthe95%confidenceinterval.

Sustainability2025,17,9219 14of33
The executed model selection approach sought to accurately optimize the distinct
hyperparameterforeachutilizedmachinelearningalgorithm. Theprimarycriterionfor
identifyingtheoptimalhyperparameterconfigurationwasreductionintheRootMean
SquaredError(RMSE).Toachievethis,cross-validationusing5differentfoldswasused.
Theresultantobjectsencompasstherequisiteinformationtoiterateoverthesefolds,utiliz-
ing4formodeltrainingandtheremaining1forperformanceassessment,repeatingthis
process5timestoensureeachfoldservesasanevaluationsetonce. Ingeneral,tree-based
ensemblemodelsexhibitimprovedperformanceonthedataset. Givenourselectionof
RMSEastheperformanceindicator,wedeemedRandomForestthevictorofthecompeti-
tion,duetoitachievingthebestorsimilarRMSEtothebest-performingmethods,butwith
alowerstandarddeviation.
3.11.2. InterpretabilityMethods
Machinelearninginterpretabilityreferstomethodologiesforelucidatingandcom-
prehendingthemechanismsbywhichmachinelearningmodelsgeneratepredictions. As
modelsincreaseincomplexity,elucidatingtheirinternallogicandacquiringinsightsinto
theirbehaviorbecomeparamount[85]. Intheabsenceofinterpretability,itbecomeschal-
lenging to determine whether a machine learning model is making sound decisions or
exhibiting bias. Explainable Artificial Intelligence (XAI) has been revealed as a viable
solutiontothedifficultyofinterpretabilitybyclarifyingtherationalebehindthemodel
predictions[86].
AmongthediverseXAImethodologies,ShapleyAdditiveExplanation(SHAP)and
Local Interpretable Model-Agnostic Explanation (LIME) have attained recognition for
providing global and local interpretability. SHAP provides consistent and precise im-
portancevaluesforthecharacteristics. Incontrast,LIMEbuildslocalsubstitutemodels
thatemulatecomplexclassifierbehavior,therebyimprovingtheunderstandingofspecific
predictions[87,88]. Toelucidatethemodel’sjudgments,weemployedtwoprevalentXAI
methodologies: LIME,whichgenerateslocalsubstituteexplanations,andSHAP,which
assigns feature attributions based on game theory principles. These elements ensure a
clearerunderstandingandimportantpredictivepotential,essentialfortransparentresults.
4. Results
4.1. CharacteristicsoftheRespondents
Of the 256 respondents, 123 were women (48%), 128 men (50%), and 5 nonbinary
(1.95%). Withregardtorace/color,basedontheprincipleofself-declaration,thesampleis
madeupof100whitepeople(39.1%),149blackpeople(58.2%),5yellowpeople(1.95%)
and2indigenouspeople(0.78%). Intermsofincomedistribution,100respondents(39.1%)
earned up to 1 minimum wage (BRL 1320), 79 (30.9%) had an income between 1 and 3
minimumwages(BRL1320to3960),40(15.6%)between3and6minimumwages(R$3960
toR$7920),22(8.59%)between6and9minimumwages(BRL7920to11,880),8(3.12%)
between10and20minimumwages(BRL13,200toR$26,400)and7(2.73%)earnedmore
than20minimumwages(aboveBRL26,400)(Tables1and2).
Table1.Averagesofperformanceandbehavioralvariablesbygender,race,andincome.
Loss
Statistic FL Crypto FP FV FF CRT Discount Herding Myopic
Aversion
Gender
Female −0.135 −0.198 −0.132 0.161 0.0710 0.0155 30 63 31 40
Male 0.0815 0.330 0.00519 0.00455 0.162 0.170 28 44 41 31
Nonbinary −0.103 0.767 −0.513 0.200 0.661 1.020 0 1 3 2

Sustainability2025,17,9219 15of33
Table1.Cont.
Loss
Statistic FL Crypto FP FV FF CRT Discount Herding Myopic
Aversion
Race
Black −0.0357 0.0427 −0.0371 0.124 0.152 0.0588 31 68 51 44
White 0.00124 0.131 −0.114 0.0215 0.0805 0.180 26 38 22 27
OtherRace −0.214 0.318 −0.177 0.115 0.288 0.288 1 2 2 2
Income
Highincome 0.486 0.520 0.566 −0.590 0.0446 0.571 0 3 4 4
Lowincome −0.0957 0.0486 −0.121 0.161 0.124 0.0575 49 77 54 53
Middleincome 0.0509 0.0837 −0.0805 0.0219 0.161 0.160 9 28 17 16
Table2.Descriptivestatisticsofthevariables.
Loss
Statistic FL Crypto FP FV FF CRT Discount Herding Myopic
Aversion
Mean −0.0261 0.0847 −0.0710 0.2723 0.1281 0.1124 0.2266 0.4219 0.2930 0.2852
Median −0.0102 0.0250 0.0631 0.2143 −0.0398 −0.0103 0.0000 0.0000 0.0000 0.0000
Std.Dev. 0.7142 0.8164 0.7724 0.2320 0.6604 0.7091 0.4194 0.4948 0.4560 0.4524
Variance 0.5101 0.6665 0.5966 0.0538 0.4362 0.5028 0.1759 0.2449 0.2080 0.2046
Skewness −0.1985 0.6553 −0.4124 1.1209 0.7891 0.7039 1.2988 0.3145 0.9045 0.9461
Kurtosis −0.7806 −0.4872 −0.5072 0.3486 0.0065 −0.3156 −0.3144 −1.9085 −1.1866 −1.1091
Min −1.6742 −0.8187 −2.2995 0.0000 −0.8469 −1.0397 0.0000 0.0000 0.0000 0.0000
Max 1.5075 2.2870 1.3631 1.0000 2.2812 2.0727 1.0000 1.0000 1.0000 1.0000
Jarque–Bera 7.9143 20.8680 9.8786 55.7425 26.8942 22.3174 73.7376 42.7735 49.9742 51.4175
4.2. MultipleLinearRegression
Weusedthefollowingasdependentvariables: financialliteracy(FL),financialvulner-
ability(FV),andfinancialfraud(FF).TheresultsaredisplayedinAppendixA.
Inthefinancialliteracyanalysis,theCognitiveReflectionTestshowedastrongpositive
relationship (coef. 0.502; p < 0.01), with higher scores reflecting greater knowledge in
financialliteracy,demonstratingthatmorethoughtfulpeopletendtohavemoreknowledge
inthisfield. Womenhadlowerlevelsoffinancialliteracy(coef. −0.140;p<0.1),which
reflectssocialbarriersinaccesstofinancialliteracy. Individualswithahighincomehad
higherlevelsoffinancialliteracy(coef. 0.348;p<0.1)whichcanbeexplainedbyseveral
structural, social, and behavioral factors. In the analysis of race, individuals who self-
declaredthemselvesasblackorasanotherracedidnotshowsignificantresults.Behavioral
characteristicssuchaslossaversion,myopicbehavior,hyperbolicdiscounting,andherding,
althoughsomeshowedapositiveornegativecoefficient,werenotstatisticallysignificant.
Intheanalysisoffinancialvulnerability,individualswithbetterfinancialplanning
exhibitedastronginverserelationship(coef. −0.797;p<0.01),indicatingthatthosewith
effective financial planning, such as controlling and projecting their finances, are less
financially vulnerable. Individuals who self-identified as black were more financially
vulnerable(coef. 0.156;p<0.05),showingthatraceisanimportantcharacteristicandthat
blackpeoplearemorefinanciallyvulnerable.
Forfinancialfraudoutcomes,financialliteracyshowedasignificantnegativerelation-
ship(coefficient−0.139;p<0.1),demonstratingthathigherlevelsoffinancialknowledge
arecorrelatedwithalowersusceptibilitytofinancialfraud. Financialplanningisshownto
beimportantforfinancialvulnerability(coefficient−0.366;p<0.01),showingthatfinancial
planningisaneffectivetoolinreducingfraud.
Theresultsshowthatfinancialliteracyandfinancialplanningplayacrucialrolein
shapingbetterfinancialhabits,reducingfinancialvulnerabilities,andpreventingfraud.

Sustainability2025,17,9219 16of33
4.3. ResultsoftheMachineLearningApproach
TheimportanceofSHAPmeasurestheinfluenceofeachvariableontheindividual
modelprediction. Theabsolutemeanvalueshowsthestrengthofthisinfluence,regardless
of the sign (positive or negative). The higher the importance value, the more relevant
thevariableistothemodel’sdecisions. Thebeeswarmplotpresentstheresultsforthe
dependentvariablesFL(Figure3),FV(Figure4),andFF(Figure5). Thehorizontalaxis
denotestheSHAPvalue,whiletheverticalaxiscomprisesthepredictivefeatures. Positive
(negative)SHAPvaluessignifythatthefeatureenhances(diminishes)thetargetvariable.
Eachrepresentsadotforeveryattribute,whichsignifiestheSHAPvalueforaparticular
instance, indicating the contribution of that attribute to the overall prediction for that
instance. Thecolorofthedotcorrespondstothevalueofthefeature,withlighterhues
signifyinggreatervalues.
Figure3. ResultsofSHAPcomputedforeveryattributeovertheentiredatasetforpredictionof
financialliteracy(FL).
Figure4. ResultsofSHAPcomputedforeveryattributeovertheentiredatasetforpredictionof
financialvulnerability(FV).

Sustainability2025,17,9219 17of33
Figure5. ResultsofSHAPcomputedforeveryattributeovertheentiredatasetforpredictionof
financialfraud(FF).
TheimportanceofLIMEmeasurestheinfluenceofeachvariableontheindividual
modelprediction. Theabsolutemeanstrengthshowstheinfluenceofeachfeature. The
highertheimportancevalue,themorerelevantthevariableistothemodel’sdecisions. The
LIMEplotpresentstheresultsforthedependentvariablesFL(Figure6), FV(Figure7),
andFF(Figure8). LocalInterpretableModel-AgnosticExplanation(LIME)representsthe
averageimportanceofthevariablesinthelocalexplanationofthepredictionsmadebythe
bestmodel(RandomForest). TheX-axis(horizontal): namesofthevariables(orfeatures),
orderedfrommostimportanttoleastimportant,andtheY-axis(vertical): averageofthe
absolutevaluesoftheweightsattributedtothevariables(mean_weight)byLIMEinthe
explanations. Thisrepresentstheaveragecontributionofthatvariabletothepredictions.
Figure6. ResultsofLIMEcomputedforeveryattributeovertheentiredatasetforpredictionof
financialliteracy(FL).
Financial planning (FP) is the variable that most influences the model, presenting
a strong prediction for financial education, financial vulnerability, and financial fraud.
The significance is very high for both the SHAP and LIME methods. In an analysis of
financialliteracytheCognitiveReflectionTest(CRT)isthefeaturethatmostinfluences
boththeSHAPandLIMEmodels,confirmingtheresultsoftheregressions. Beingawoman
significantly impacts the predicted result, showing a positive prediction for financial
vulnerabilityandfinancialfraud,especiallyforthepredictionoffinancialliteracy,mainly

Sustainability2025,17,9219 18of33
when we look at the LIME results compared to the SHAP results; these values are a
consequenceofthedifferentmethodologiesbehindSHAPandLIME.TheLIMEmethod
providesinformationonspecificlocalspecifications,whiletheSHAPmethodaimsatamore
comprehensiveandglobalunderstandingofresourcecontributions. Botharevaluable,but
weanswerdifferentproposedquestionsabouttheimportanceoffeatures. Wecanhighlight
the variables FL, Crypto and Black, which, despite not having great predictive power,
alwaysrankamongthetopforfinancialvulnerabilityandfinancialfraudmodeling. The
othercharacteristicsdidnotshowgreatsignificanceinourmodels. Itisimportanttonote
thatthevaluesfortheNonbinaryandOtherRacevariablesarenotshownintheresults,
duetothesmallnumberofsamples. Whencross-validationisperformedontrainingand
testsets,thesegroupsmayendupinonlyoneofthesesets,oreveninnoneofthetestsets
incertainfolds,whichiswhatoccurredforthevaluesinquestion.
Figure7.ResultsofLIMEcomputedforeveryattributeovertheentiredatasetforthepredictionof
financialvulnerability(FV).
Figure8. ResultsofLIMEcomputedforeveryattributeovertheentiredatasetforpredictionof
financialfraud(FF).
Theseresultsconfirmtheregressionresults,especiallywhenwelookattheresultsof
theSHAPmethodology,sincethismethodologyaimsatamorecomprehensiveandglobal
understandingofthecontributionsofresources. Botharevaluable,butweanswerdifferent
proposedquestionsabouttheimportanceoffeatures.

Sustainability2025,17,9219 19of33
5. Discussion
Inrecentyears,Brazilhasseenariseinindebtedness,with32%ofBrazilianshaving
beeninarrearsformorethanthreemonths,aswellastherecurrenceoffinancialscams,
whichaffectmorethan40millionBrazilians[89]. Atthesametime,researchpointstothe
growingpopularityofonlinesportsbetting,called“bets”,whichispredominantlyaimed
atpeopleearninguptotwominimumsalaries[89]. Fromthiscontext,andbasedonthe
results of this article, we infer that financial literacy is something that deserves the full
attentionofpublicpolicymakers.
Therecentliteratureonfinancialliteracymainlyinvestigatesfinancialliteracyand
retirementplanning;theintersectionoffinancialriskmanagement;andtheimpactofbehav-
ioralfinanceandpsychologicalfactors[90]. Inlinewiththediscussionintheinternational
literature,ourresultsshowedthatpeoplewithgreaterfinancialliteracyhavebetterfinancial
habits,whichleadthemtopracticesthatreducetheirlevelofdebt,motivatinganincrease
infinancialreservesand,consequently,theabilitytodealwithunexpectedexpensesand
eveneconomicinstability. Financialliteracycombinedwithappropriatefinancialbehavior
contributestoindividualandfamilyfinancialsecurityandfavorseconomicgrowthand
stability[91].
EmergingeconomieslikeBrazilaremorevulnerabletoeconomicinstabilityandshocks.
TheGetulioVargasFoundation’sEconomicUncertaintyIndicator(IIE-Br)roseby4.6points
inApril2025,totaling115.5points[92],whichreinforcestheneedforapopulationcapable
ofdealingwitheconomicinstability,somethingthatisonlyfeasiblethroughagooddegree
of literacy and positive financial habits. The literature shows that people with greater
financialliteracyhavegreateraccesstoformalfinancialsystemsandusethemsparingly,
reducingthelikelihoodofbeingexposedtoanydegreeoffinancialvulnerability[93].
Thedevelopmentofnew,innovativeinstrumentsthatassessfinancialliteracy,financial
planning, and cryptocurrency literacy is intended to address substantive gaps in the
prevailing literature. Policymakers will now be able to measure financial literacy and
relatedconceptsinamoreefficientandcomprehensivemanner,whilebeinginaposition
to design and deliver interventions that are empirically grounded. The imperative of
developingthistoolarisesduetothecomplicatednatureoftheconstructandfinancial
literacy’scentralroleinpersonalaswellascommunaleconomicstability,wherebythere
mustbeintermixingofbasicfinancialcompetencywithattitudes,behaviors,andcontextual
factors, such as exposure to socioeconomic vulnerability, that have a direct influence
upon individuals’ health, well-being, and financial stability [91]. In hypothesizing and
craftingourapproach,notonlyhastherebeenastepupinscholarlyworkinacademia,
butfinancialliteracy’sstatusasacomplicatedconstructhasalsobeenacknowledged. This
facilitatestheevidence-basedpromotionofeffectiveinterventions,aswellasadecreasein
vulnerability[1,23].
Inlinewiththeinternationalliterature,ourresultsshowthatintheFederalDistrict,
financialliteracyplaysanimportantroleindevelopingbetterfinancialhabitsamongthe
population. However,forthesampleanalyzed,thedatashowthattheoreticalknowledge
alonedoesnotguaranteethemitigationoffinancialvulnerabilities,noreventheprevention
offraud. Thistypeoffindingconvergeswithotherstudiesthathighlighttheimportance
ofanintegratedapproachthatconsidersnotonlyknowledge,butalsothepracticesand
social context of individuals [18,19,35]. Accordingly, financial behavior emerged as the
most consistent dimension in explaining the positive outcomes of the sample. This di-
mension, therefore, shows that skills such as spending control, financial planning, and
behavioralresilienceareessentialforreducingvulnerabilityandstrengtheningfinancial
security[20,68].

Sustainability2025,17,9219 20of33
The analysis also revealed significant inequalities in the levels of financial literacy
betweenthedifferentgroupsinthesample. Individualswithhighincome,forexample,
hadhigherlevelsoffinancialliteracy,reflectingstructuralandculturalbarrierstoaccessing
financialliteracyandotherformaleconomicresources. Thistypeofinequality,whichhas
alreadybeendemonstratedinotherstudies[25,29],isevenmorecriticalinBrazil,acountry
characterized by high income inequality and financial exclusion, especially among the
low-income population [3,4]. These results highlight the need for intersectional public
policies,thatis,policiesthattakeintoaccountthesocioeconomicandculturalparticularities
ofthemostvulnerablegroups.
Ourfindingsconfirmourhypothesis: planninghasmuchstrongerpredictiveability.
As a matter of theoretical interest but also because such a composite aggregated index
wouldsuppressanimportantdifference,weperformedsuchanexerciseasarobustness
check. The results, which we document in Appendix B, confirm our major results and
supportourinitialhypothesis. Wecarriedoutanassessmentwithacompositeindexto
confirmourmethodology. Theresultsprocuredwereconsistentwithourmainfindings
andavailableinAppendixB.
5.1. ImplicationsforSustainableDevelopment
Wefoundlowerfinancialliteracyforwomen, comparedtomalerespondents, and
greatervulnerabilityamongblackindividuals. Theseresultsdemonstratenotonlyimpor-
tanteconomicissues,butalsoissuesofsocialinjusticethatunderminesocialsustainability.
InBrazil,therearealreadyracialquotapoliciesforblackpeopletoaccesspublicuniversities.
Publicpoliciesthataddressracialinjusticesareimportanttotackleissuesofvulnerability
andfinancialfraud. Futureresearchcouldassesswhetheralgorithmsmaybebeingusedto
defraudpeopleofspecificracesduetogreatervulnerability.
Greaterfinancialvulnerabilityleadstofamiliesexperiencinggreaterinstabilityintheir
savings.Itcausesthemtoseekaccesstocreditthatcanbepredatory,withhighinterestrates.
Itcanalsoleadtodifficultyinwithstandingadverseeconomicshocks. Theseweaknesses
shouldbeaddressedatthemacroeconomiclevel,whichunderscorestheimportanceof
enhancing financial planning, as well as household resilience, in order to build a more
stableandsustainablenationaleconomy(thispointiscloselyrelatedtoSDG8: Decent
WorkandEconomicGrowth).
Our main finding is that financial planning and behaviors are more critical than
knowledge(asmeasuredbythefinancialliteracyinstrument, whichencompassesonly
basicknowledge). Similarly,environmentalknowledgedoesnotnecessarilyleadpeople
tobehaveinapro-environmentalway. Thus,financialknowledgedoesnotguaranteethe
financialwell-beingoffamilies. Thus,akeyfindingofourstudyisthatsustainableout-
comesdependonfosteringorstimulatinglong-termthinkingandbehavioralchanges. Our
resultssuggestimportantavenuesfordevelopingpublicpoliciesthataremoreinclusive
andaimtofosterbehavioralchange. Futureresearchcouldinvestigatethisrelationship
byevaluatingtheimpactofnudgesonincreasingpeople’sfinancialwell-being,reducing
vulnerabilities,andpromotingmoresustainablebehaviors.
5.2. MachineLearningDiscussion
Machinelearningsystemshelppeopleandinstitutionsbetterunderstanddataand
identifyimportantpatternswithinit. Thisinformationiscrucialfordecision-makingand
planning. Therefore, it is important to understand the principles of machine learning
algorithmsandtheirapplicabilityinvariousreal-worldapplicationareas,suchassecurity
services,healthcare,economicdata,context-awaresystems,sustainableagriculture,and
manyothers[94]. Choosingthebestmachinelearningmodelcanbequiteadauntingtask.

Sustainability2025,17,9219 21of33
Typically,whencreatingamodel,wechoosethealgorithmthatperformsbestforthedata
inquestion. Tosupportthis,weuseamethodologythatisbecomingwidespreadwhen
comparingmachinelearningmodelsinahorseracetochoosewhichmodelisbest[95]. The
bestmodelevaluatedwasRandomForest,ahighlyeffectivemachinelearningalgorithm
that excels at modeling nonlinear relationships and providing the importance of each
variable[96].
Easeofinterpretingresultsisparamount,associalresearchersareprimarilyconcerned
withunderstandingcomplexsocialspecificity,testingtheories,anddrawingexplanatory
conclusionsfromtheirdata. Theirexpertiseliesintheirrespectivefields,notnecessarilyin
advancedcomputerprogrammingoralgorithmdevelopment,tohaveabetterinterpreta-
tionoftheresultsusingSHAPandLIME,whicharetwoprominenttechniquesinthefield
ofExplainableAI(XAI),addressingthe“blackbox”problemofcomplexmachinelearning
models,helpingresearchersunderstandwhyacertaindiscoverywasmade.
6. FinalConsiderations
The results highlight the need for comprehensive initiatives that address not only
thefundamentalsoffinancialknowledgebutalsotheunderstandinganddevelopment
of individuals’ behaviors and attitudes. Public policies aimed at promoting financial
inclusion,forexample,shouldincorporatefinancialliteracyprogramsadaptedtodifferent
audiences. Thisadaptationmustalsoconsiderothersocialfactors,suchassex,race,and
income. Anotherkeypointliesintheintegrationoftechnologicaltoolsandinnovative
methodologies,suchastheinstrumentdevelopedinthisstudy,whichcansignificantly
contributetoenhancingtheeffectivenessandreachoftheseinitiatives.
OnepossiblelimitationofthestudyisthatwefocusonrespondentsfromtheFederal
DistrictofBrazil. Althoughapotentialshortcominginvolvestheuseofparticipantsdrawn
fromtheFederalDistrict,sampleheterogeneityregardingincome,education,andracial
background allowed us to gain insight into the associations among these fundamental
demographicfactorsandfinancialliteracy. Futurestudiesmayconsiderhowinter-regional
variationsaffectfinancialliteracyanditscorrelationwithcognitivebiases,amongother
factors. Oneofthefundamentalquestionsofresearchiswhetherthereisgeneralizability
in such findings and whether there is a potential contribution of cultural variations in
thisregard.
Itisessentialtohighlightthatourresultsdonotnecessarilyimplyadirectcause-and-
effect relationship. However, our results indicate that enhancing financial literacy and
mitigatingfinancialvulnerabilitiespresentrelevantdriversthatareconsistentwiththe
broadgoalsofsustainabledevelopment.
AuthorContributions: Conceptualization,B.M.T.andD.H.C.;Methodology,B.M.T.,D.H.C.and
C.C.S.;Software,B.M.T.andC.C.S.;Formalanalysis,B.M.T.,D.H.C.andC.C.S.;Investigation,B.M.T.
andD.H.C.;Datacuration,D.H.C.andC.C.S.;Writing—originaldraft,B.M.T.,D.H.C.andC.C.S.;
Writing—review & editing, B.M.T., D.H.C. and C.C.S. All authors have read and agreed to the
publishedversionofthemanuscript.
Funding: ThisresearchwasfundedbyFundaçãodeApoioàPesquisadoDistritoFederal—FAP-
DF—under the name ‘Alfabetização Financeira e Vieses Cognitivos: o caso do Distrito Federal
00193-00000273/2023-01’. BMTgratefullyacknowledgesfinancialsupportfromFAP-DF,CAPES
(ExperimentalLaboratoryinPublicPolicy—LAB-LEPP),andCNPq(grant).DCSandTCSgratefully
acknowledgefinancialsupportfromFAP-DF.
InstitutionalReviewBoardStatement: Thestudywasconductedaccordingtotheguidelinesof
theDeclarationofHelsinki,andapprovedbytheEthicsCommitteeofGetulioVargasFoundation
(protocolcodeP.421.2023anddateofapprovalis24October2023).

Sustainability2025,17,9219
22of33
InformedConsentStatement:Informedconsentwasobtainedfromallsubjectsinvolvedinthestudy.
DataAvailabilityStatement:Thedataareavailableuponrequestfromtheauthors.
Acknowledgments:TheauthorsusedGenAI,DeepL,andGrammarlytoimprovethereadabilityand
clarityofthetext.Theentiretexthasbeenreviewedandapprovedbytheauthors,whoassumefull
responsibility.Wethankthefouranonymousreviewersandtheeditor,whohavehelpedimprove
thepaper.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.Thefundershadnoroleinthedesign
ofthestudy;inthecollection,analysis,orinterpretationofdata;inthewritingofthemanuscript;or
inthedecisiontopublishtheresults.
AppendixA.RegressionResults
TableA1.Dependentvariables:FLBroad,FV,andFF.
|     | FLBroad(HC3) | FV(HC3) | FF(HC3) |
| --- | ------------ | ------- | ------- |
|     | (1)          | (2)     | (3)     |
| CRT | 0.502***     |         |         |
(0.057)
| FL  |     | 0.053     | −0.139*   |
| --- | --- | --------- | --------- |
|     |     | (0.071)   | (0.078)   |
| FP  |     | −0.797*** | −0.366*** |
|     |     | (0.055)   | (0.071)   |
−0.046
| Crypto    |         |         | 0.079   |
| --------- | ------- | ------- | ------- |
|           |         | (0.045) | (0.054) |
| Female    | −0.140* | 0.053   | −0.117  |
|           | (0.083) | (0.074) | (0.079) |
| NonBinary | −0.709  | −0.176  | 0.243   |
|           | (0.454) | (0.286) | (0.402) |
| Black     | 0.010   | 0.156** | 0.091   |
|           | (0.088) | (0.073) | (0.076) |
−0.315
| OtherRace    |         | 0.127   | 0.0002  |
| ------------ | ------- | ------- | ------- |
|              | (0.395) | (0.143) | (0.285) |
| Young        | 0.025   | −0.017  | −0.104  |
|              | (0.100) | (0.089) | (0.103) |
| Old          | −0.063  | −0.087  | −0.056  |
|              | (0.143) | (0.114) | (0.154) |
|              | −0.071  |         | −0.027  |
| LowIncome    |         | 0.096   |         |
|              | (0.106) | (0.096) | (0.102) |
| HighIncome   | 0.348*  | −0.113  | 0.127   |
|              | (0.195) | (0.133) | (0.220) |
| LossAversion | 0.014   | −0.096  | −0.064  |
|              | (0.084) | (0.073) | (0.074) |
| Myopic       | 0.055   | 0.016   | 0.046   |
|              | (0.088) | (0.082) | (0.082) |
|              | −0.111  | −0.028  | −0.006  |
Discount
|         | (0.097) | (0.084) | (0.092) |
| ------- | ------- | ------- | ------- |
| Herding | −0.064  | 0.064   | −0.008  |
|         | (0.086) | (0.077) | (0.083) |

Sustainability2025,17,9219 23of33
TableA1.Cont.
FLBroad(HC3) FV(HC3) FF(HC3)
(1) (2) (3)
Constant 0.046 −0.100 0.188*
(0.119) (0.095) (0.108)
Observations 256 256 256
R2 0.320 0.594 0.304
AdjustedR2 0.284 0.569 0.261
ResidualStd. Error 0.604 0.527 0.568
FStatistic 8.771*** 23.430*** 6.992***
Note: Robuststandarderrorsinparentheses.*p<0.1;**p<0.05;***p<0.01.
AppendixB.FL_BroadFactorIndex
WeconstructedtheFL_Broadfactorindex,whichcomprisesanaggregateindexthat
encompassesfinancialliteracy(basicknowledgeoffinance),knowledgeaboutcryptocurren-
cies(Crypto),andfinancialattitudesregardingfinancialplanning(FinancialPlanning—FP).
FL+FP+Crypto
FL_Broad =
3
Ourgeneralmultiplelinearregressionmodelcanberepresentedmathematicallyas:
FL_Broad = βFL+βFL_BroadCRT +βFL_BroadFemale +βFL_BroadNonBinary
i 0 1 i 2 i 3 i
+βFL_BroadBlack +βFL_BroadOtherRace +βFL_BroadYoung +βFL_BroadOld
4 i 5 i 6 i 7 i
+βFL_BroadLowIncome +βFL_BroadHighIncome +βFL_BroadLossAversion
8 i 9 i 10 i
+βFL_BroadMyopic +βFL_BroadDiscount +βFL_BroadHerding +ε , (A1)
11 i 12 i 13 i i,FL_Broad
FV = βFV+βFVFL_Broad +βFVFemale +βFVNonBinary
i 0 1 i 2 i 3 i
+βFVBlack +βFVOtherRace +βFVYoung +βFVOld +βFVLowIncome
4 i 5 i 6 i 7 i 8 i
+βFVHighIncome +βFVLossAversion +βFVMyopic +βFVDiscount
9 i 10 i 11 i 12 i
+βFVHerding +ε , (A2)
13 i i,FV
FF = βFF+βFFFL_Broad +βFFFemale +βFFNonBinary
i 0 1 i 2 i 3 i
+βFFBlack +βFFOtherRace +βFFYoung +βFFOld +βFFLowIncome
4 i 5 i 6 i 7 i 8 i
+βFFHighIncome +βFFLossAversion +βFFMyopic +βFFDiscount
9 i 10 i 11 i 12 i
+βFFHerding +ε , (A3)
13 i i,FF
TableA2.Regressionresults:dependentvariables:FL_Broad,FV,andFF.
FL_Broad(HC3) FV(HC3) FF(HC3)
(1) (2) (3)
C_R 0.363***
(0.046)
FL_Broad −0.917*** −0.516***
(0.072) (0.075)
Female −0.220*** −0.066 −0.209***
(0.061) (0.085) (0.080)
NonBinary −0.631* 0.088 0.389
(0.371) (0.372) (0.382)

Sustainability2025,17,9219
24of33
TableA2.Cont.
|           |     | FL_Broad(HC3) | FV(HC3) | FF(HC3) |
| --------- | --- | ------------- | ------- | ------- |
|           |     | (1)           | (2)     | (3)     |
| Black     |     | 0.020         | 0.090   | 0.057   |
|           |     | (0.066)       | (0.083) | (0.083) |
| OtherRace |     | −0.104        | 0.088   | 0.034   |
|           |     | (0.319)       | (0.240) | (0.244) |
−0.034
| Young      |     | 0.187** | 0.040    |         |
| ---------- | --- | ------- | -------- | ------- |
|            |     | (0.075) | (0.108)  | (0.108) |
| Old        |     | −0.006  | −0.169   | −0.094  |
|            |     | (0.107) | (0.137)  | (0.160) |
| LowIncome  |     | −0.069  | 0.044    | −0.052  |
|            |     | (0.079) | (0.106)  | (0.104) |
| HighIncome |     | 0.369** | −0.215   | 0.071   |
|            |     | (0.154) | (0.179)  | (0.230) |
|            |     | −0.054  | −0.209** | −0.148* |
LossAversion
|              |       | (0.061)   | (0.081)   | (0.077)  |
| ------------ | ----- | --------- | --------- | -------- |
| Myopic       |       | 0.091     | −0.008    | 0.047    |
|              |       | (0.066)   | (0.089)   | (0.086)  |
| Discount     |       | −0.147**  | −0.055    | −0.031   |
|              |       | (0.070)   | (0.095)   | (0.099)  |
| Herding      |       | −0.012    | 0.109     | 0.039    |
|              |       | (0.069)   | (0.092)   | (0.090)  |
| Constant     |       | 0.013     | 0.105     | 0.293**  |
|              |       | (0.087)   | (0.111)   | (0.115)  |
| Observations |       | 256       | 256       | 256      |
| R2           |       | 0.388     | 0.439     | 0.206    |
| AdjustedR2   |       | 0.355     | 0.409     | 0.164    |
| ResidualStd. | Error | 0.459     | 0.617     | 0.604    |
| FStatistic   |       | 11.799*** | 14.560*** | 4.841*** |
Note:Robuststandarderrorsinparentheses.*p<0.1;**p<0.05;***p<0.01.
AppendixC.MeasurementModelEquationsfortheConfirmatoryFactor
Analysis(CFA)
| AppendixC.1. | ConfirmatoryFactorAnalysis |     |     |     |
| ------------ | -------------------------- | --- | --- | --- |
WeimplementedaConfirmatoryFactorAnalysistoevaluatethereliabilityandvalidity
ofourlatentfactors(Rosseel[97]). Wemodeledsixlatentfactors: (i)thefinancialliteracy
(F )scale,whichmeasurescoreknowledge;(ii)thefinancialvulnerability(FV)scale,which
L
measuresiftherespondentisnotabletopaytheirbills(anoutcomescale);(iii)thefinancial
fraudscale(FF),whichhasfouritemsthatevaluateiftherespondenthasbeenvictimized
byfinancialfraud;(iv)theCognitiveReflectionTest(CR),whichevaluatesiftherespondent
usesintuitionorrationalitytoanswerthequestions;(v)thecryptocurrencyliteracyscale
(CRY);and(vi)thefinancialplanning(FP)scale,whichmeasuresiftherespondentisprone
tofinancialplanning.
| AppendixC.2. | Notation |     |     |     |
| ------------ | -------- | --- | --- | --- |
Let:
• η(eta)representalatentvariable(factor).

Sustainability2025,17,9219 25of33
• xrepresentanobservedvariable(indicator).
• λ(lambda)representthefactorloading,whichmeasuresthestrengthoftherelation-
shipbetweentheobservedvariableanditsrespectivelatentfactor.
• ϵ(epsilon)representthemeasurementerrorassociatedwitheachobservedvariable.
AppendixC.3. MeasurementEquations
AppendixC.3.1. FinancialLiteracy(FL)
Thelatentvariableforfinancialliteracy(η )ismeasuredbyfourobservedindicators:
FL
x = λ ·η +ϵ
FL1 FL1,FL FL FL1
x = λ ·η +ϵ
FL2 FL2,FL FL FL2
x = λ ·η +ϵ
FL4 FL4,FL FL FL4
x = λ ·η +ϵ
FL6 FL6,FL FL FL6
AppendixC.3.2. FinancialVulnerability(FV)
Thelatentvariableforfinancialvulnerability(η )ismeasuredbyfourteenobserved
FV
indicators:
x = λ ·η +ϵ
FV1 FV1,FV FV FV1
x = λ ·η +ϵ
FV2 FV2,FV FV FV2
x = λ ·η +ϵ
FV3 FV3,FV FV FV3
x = λ ·η +ϵ
FV4 FV4,FV FV FV4
x = λ ·η +ϵ
FV5 FV5,FV FV FV5
x = λ ·η +ϵ
FV6 FV6,FV FV FV6
x = λ ·η +ϵ
FV7 FV7,FV FV FV7
x = λ ·η +ϵ
FV8 FV8,FV FV FV8
x = λ ·η +ϵ
FV9 FV9,FV FV FV9
x = λ ·η +ϵ
FV10 FV10,FV FV FV10
x = λ ·η +ϵ
FV11 FV11,FV FV FV11
x = λ ·η +ϵ
FV12 FV12,FV FV FV12
x = λ ·η +ϵ
FV13 FV13,FV FV FV13
x = λ ·η +ϵ
FV14 FV14,FV FV FV14
AppendixC.3.3. FinancialFraud(FF)
Thelatentvariableforfinancialfraud(η )ismeasuredbyfourobservedindicators:
FF
x = λ ·η +ϵ
FF1 FF1,FF FF FF1
x = λ ·η +ϵ
FF2 FF2,FF FF FF2
x = λ ·η +ϵ
FF3 FF3,FF FF FF3
x = λ ·η +ϵ
FF4 FF4,FF FF FF4

Sustainability2025,17,9219
26of33
AppendixC.3.4. CognitiveReflectionTest(CR)
ThelatentvariableforCognitiveReflection(η )ismeasuredbyfiveobservedindicators:
CR
| x     | = λ      | ·η +ϵ  |
| ----- | -------- | ------ |
| CR1   | CR1,CR   | CR CR1 |
| x     | = λ      | ·η +ϵ  |
| CR2   | CR2,CR   | CR CR2 |
| x     | = λ      | ·η +ϵ  |
| CR3   | CR3,CR   | CR CR3 |
|       | =        | ·η +ϵ  |
| x CR5 | λ CR5,CR | CR CR5 |
| x     | = λ      | ·η +ϵ  |
| CR7   | CR7,CR   | CR CR7 |
AppendixC.3.5. CryptocurrencyKnowledge(CRY)
Thelatentvariableforcryptocurrencyknowledge(η CRY )ismeasuredbyfourobserved
indicators:
| x         | = λ           | ·η +ϵ       |
| --------- | ------------- | ----------- |
| Crypto1   | Crypto1,CRY   | CRY Crypto1 |
| x         | = λ           | ·η +ϵ       |
| Crypto2   | Crypto2,CRY   | CRY Crypto2 |
|           | =             | ·η +ϵ       |
| x Crypto3 | λ Crypto3,CRY | CRY Crypto3 |
| x         | = λ           | ·η +ϵ       |
| Crypto4   | Crypto4,CRY   | CRY Crypto4 |
AppendixC.3.6. FinancialPlanning(FP)
Thelatentvariableforfinancialplanning(η FP )ismeasuredbysixobservedindicators:
|       | =          | ·η +ϵ        |
| ----- | ---------- | ------------ |
| x FP1 | λ FP1,FP   | FP FP1       |
| x     | = λ        | ·η +ϵ        |
| FP2   | FP2,FP     | FP FP2       |
| x     | = λ        | ·η +ϵ        |
| FP3   | FP3,FP     | FP FP3       |
| x FP4 | = λ FP4,FP | ·η FP +ϵ FP4 |
| x     | = λ        | ·η +ϵ        |
| FP5   | FP5,FP     | FP FP5       |
|       | =          | ·η +ϵ        |
| x FP6 | λ FP6,FP   | FP FP6       |
Giventhatthesurveyitemsweremeasuredonanorderedcategoricalscale(dichoto-
mousorLikert-type),weperformedtheanalysisusingthepolychoriccorrelationmatrix
andtherobustDiagonallyWeightedLeastSquares(DWLS)estimator. Webasedtheeval-
uationofthemodelontheusualglobalfitindices,aswellasreliability,convergent,and
discriminantvalidityassessments.
AppendixC.3.7. OverallModelFit
OurCFAmodelshowsanexcelentfittothedata. TherobustComparativeFitIndex
(CFI = 0.954) and Tucker–Lewis Index (TLI = 0.950) exceed the 0.95 threshold, which
indicatesastrongcorrespondencebetweenourmodelandthedata. Also,theRootMean
SquareErrorofApproximation(knownasRMSEA=0.039)waswellbelowthe0.06cutoff
foraclosefit, witha90%confidenceintervalof[0.032, 0.045]thatfurthersupportsour
conclusion. Whiletheseindicessuggestaperfectglobalmodelfit,theStandardizedRoot
MeanSquareResidual(SRMR=0.114)iselevatedabovetherecommendedmaximumof
0.08. Thisresultmaysuggestthatwhiletheoverallmodelstructureissound,theremaybe
somelocalizedareasofmisfit.
AppendixC.3.8. ReliabilityandConvergentValidity
The internal consistency and convergent validity of the six factors were assessed.
CompositeReliability(CR)scoresindicatedgoodtoexcellentreliabilityforthemajority

Sustainability2025,17,9219 27of33
ofthefactors: financialvulnerability(CR=0.950),financialfraud(CR=0.803),Cognitive
ReflectionTest(CR=0.844),cryptocurrencyliteracy(CR=0.955),andfinancialplanning
(CR=0.845),allofwhichwerewellabovethe>0.70threshold. Thefinancialliteracyfactor
(CR=0.695)demonstratedborderlinebutacceptablereliability.
Convergent validity, as estimated by the Average Variance Extracted (AVE), regis-
tered strong levels in four of six factors, all of which exceeded the >0.50 threshold: fi-
nancialvulnerability(AVE=0.581), financialfraud(AVE=0.511), CognitiveReflection
Test(AVE=0.531),andcryptocurrencyliteracy(AVE=0.841). Onthecontrary,whilethe
financialplanningfactor(AVE=0.481)andthefinancialliteracyfactor(AVE=0.370)failed
topassthistest,thismeansthatsuchconstructssharelessthan50%ofthevarianceoftheir
respectiveindicationsinmeanterms. However,uponconsiderationofparameterestimates,
itemergedthatalloftheindividualfactorloadingsweresignificantstatistically(p<0.001)
withmostofthemshowingsubstantivelylargemagnitudes.
AppendixC.3.9. DiscriminantValidity
We find strong evidence for discriminant validity, which helps confirm that the
sixlatentconstructscanbeseenasempiricallydistinctfromoneanother. First,theFornell–
Larckercriterionwasmetforallpairsoffactors;thesquarerootoftheAVE(AVE)foreach
constructwasgreaterthanitscorrelationwithanyotherconstruct.Second,amorestringent
testusingtheHeterotrait–MonotraitRatioofCorrelations(HTMT)furthersupportedthese
findings. The highest observed HTMT value was 0.599 (between FV and FP), which is
wellbelowtheconservativethresholdof<0.85,whichprovidesrobustevidenceforthe
discriminantvalidityofallofthefactorsinourmodel.
AppendixC.3.10. ConclusiononMeasurementModelQuality
Weconclude,usingtheConfirmatoryFactorAnalysis,thatourproposedsix-factor
structure of the measurement instrument fits the data well on a global level, and the
constructsdemonstrateexcellentdiscriminantvalidityandgenerallyhighreliability. These
resultssuggestthemodelhasafirmfoundation.
Figure A1. Path diagram of the final six-factor Confirmatory Factor Analysis (CFA) model.
Ovals represent latent factors and rectangles represent observed indicators. Path values are
standardizedestimates.

Sustainability2025,17,9219
28of33
TableA3.Modelfitindicesandlatentfactorcorrelationsforthesix-factorCFAmodel.
PartA:Goodness-of-FitIndices
| χ2(df)          | CFI   | TLI   | RMSEA[90%CI]       | SRMR  |     |
| --------------- | ----- | ----- | ------------------ | ----- | --- |
| 849.845***(614) | 0.954 | 0.950 | 0.039[0.032,0.045] | 0.114 |     |
PartB:LatentFactorStandardizedCorrelations
| Factor                        | 1.        | 2.       | 3.    | 4. 5.     | 6.  |
| ----------------------------- | --------- | -------- | ----- | --------- | --- |
| 1.FinancialLiteracy(FL)       | –         |          |       |           |     |
| 2.FinancialVulnerability(FV)  | −0.380*** | –        |       |           |     |
| 3.FinancialFraud(FF)          | −0.292*   | 0.469*** | –     |           |     |
| 4.CognitiveReflectionTest(CR) | 0.415***  | −0.222** | 0.021 | –         |     |
| 5.CryptocurrencyLiteracy(CRY) | 0.135     | −0.146   | 0.021 | 0.274** – |     |
6.FinancialPlanning(FP) 0.522*** −0.642*** −0.375*** 0.217* 0.139 –
Note. N=256.FitindicesarebasedontherobustDWLSestimator.*p<0.05,**p<0.01,***p<0.001.
TableA4. StandardizedFactorLoadings(λ), CompositeReliability(CR),andAverageVariance
Extracted(AVE).
| Construct |     | Item | StandardizedLoading(λ) |     |     |
| --------- | --- | ---- | ---------------------- | --- | --- |
FinancialLiteracy(FL)
CR=0.695,AVE=0.370
|     |     | FL1 |     | 0.671 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | FL2 |     | 0.435 |     |
|     |     | FL4 |     | 0.585 |     |
|     |     | FL6 |     | 0.707 |     |
FinancialVulnerability(FV)
CR=0.950,AVE=0.581
|     |     | FV1  |     | 0.780 |     |
| --- | --- | ---- | --- | ----- | --- |
|     |     | FV2  |     | 0.778 |     |
|     |     | FV3  |     | 0.851 |     |
|     |     | FV4  |     | 0.829 |     |
|     |     | FV5  |     | 0.829 |     |
|     |     | FV6  |     | 0.778 |     |
|     |     | FV7  |     | 0.733 |     |
|     |     | FV8  |     | 0.839 |     |
|     |     | FV9  |     | 0.869 |     |
|     |     | FV10 |     | 0.816 |     |
|     |     | FV11 |     | 0.716 |     |
|     |     | FV12 |     | 0.493 |     |
|     |     | FV13 |     | 0.665 |     |
|     |     | FV14 |     | 0.592 |     |
FinancialFraud(FF)
CR=0.803,AVE=0.511
|     |     | FF1 |     | 0.673 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | FF2 |     | 0.530 |     |
|     |     | FF3 |     | 0.807 |     |
|     |     | FF4 |     | 0.812 |     |
CognitiveReflectionTest(CR)
CR=0.844,AVE=0.531
|     |     | CR1 |     | 0.979 |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | CR2 |     | 0.644 |     |
|     |     | CR3 |     | 0.764 |     |
|     |     | CR5 |     | 0.633 |     |
|     |     | CR7 |     | 0.547 |     |
CryptocurrencyLiteracy(CRY)
CR=0.955,AVE=0.841
|     |     | Crypto1 |     | 0.888 |     |
| --- | --- | ------- | --- | ----- | --- |
|     |     | Crypto2 |     | 0.903 |     |
|     |     | Crypto3 |     | 0.968 |     |
|     |     | Crypto4 |     | 0.907 |     |

Sustainability2025,17,9219
29of33
TableA4.Cont.
| Construct |     |     | Item | StandardizedLoading(λ) |     |     |
| --------- | --- | --- | ---- | ---------------------- | --- | --- |
FinancialPlanning(FP)
CR=0.845,AVE=0.481
|     |     |     | FP1 | 0.791 |     |     |
| --- | --- | --- | --- | ----- | --- | --- |
|     |     |     | FP2 | 0.614 |     |     |
|     |     |     | FP3 | 0.591 |     |     |
|     |     |     | FP4 | 0.608 |     |     |
|     |     |     | FP5 | 0.711 |     |     |
|     |     |     | FP6 | 0.811 |     |     |
Note.Allfactorloadingsarestatisticallysignificantatp<0.001.
TableA5.Constructreliabilityandconvergentvaliditystatistics.
Factor CompositeReliability(CR) AverageVarianceExtracted(AVE)
| F   |     | 0.695 |     | 0.370 |     |     |
| --- | --- | ----- | --- | ----- | --- | --- |
L
| F V |     | 0.950 |     | 0.581 |     |     |
| --- | --- | ----- | --- | ----- | --- | --- |
| F F |     | 0.803 |     | 0.511 |     |     |
| C   |     | 0.844 |     | 0.531 |     |     |
R
| CRY |     | 0.955 |     | 0.841 |     |     |
| --- | --- | ----- | --- | ----- | --- | --- |
| F   |     | 0.845 |     | 0.481 |     |     |
P
Note. ThresholdsforgoodpsychometricpropertiesaretypicallyCR>0.70andAVE>0.50.
TheresultsfromtheFornell–Larckercriterionanalysisprovidestrongevidencefor
thediscriminantvalidityofthesix-factormodel. Asshowninthetable,thesquarerootof
theAVEforeachlatentconstructwasgreaterthanitscorrelationwithanyotherconstruct,
indicatingthateachfactorisstatisticallydistinct.
TableA6.DiscriminantvalidityassessmentusingtheFornell–Larckercriterion.
| Factor | F     | F   | F   | C   | CRY | F   |
| ------ | ----- | --- | --- | --- | --- | --- |
|        | L     | V   | F   | R   |     | P   |
| F      | 0.609 |     |     |     |     |     |
L
| F V | −0.380 | 0.762 |       |     |     |     |
| --- | ------ | ----- | ----- | --- | --- | --- |
| F   | −0.292 | 0.469 | 0.715 |     |     |     |
F
−0.222
| C R | 0.415 |        | 0.021  | 0.729 |       |       |
| --- | ----- | ------ | ------ | ----- | ----- | ----- |
| CRY | 0.135 | −0.146 | 0.021  | 0.274 | 0.917 |       |
| F   | 0.522 | −0.642 | −0.375 | 0.217 | 0.139 | 0.693 |
P
Note. Diagonalelements(inbold)arethesquarerootoftheAverageVarianceExtracted(AVE).Fordiscrimi-
nantvalidity,diagonalelementsmustbegreaterthantheoff-diagonalcorrelationsinthecorrespondingrows
andcolumns.
References
1. Lusardi,A.;Mitchell,O.S. FinancialLiteracyandPlanning:ImplicationsforRetirementWellbeing.InTheRoutledgeHandbookof
FinancialLiteracy;Oliver,B.;Young,C.,Eds.;Routledge:NewYork,NY,USA,2014.
2. VanRooij,M.;Lusardi,A.;Alessie,R. FinancialliteracyandretirementplanningintheNetherlands. J.Econ. Psychol. 2011,
32,593–608.[CrossRef]
3. Batinga,G.L.;Castro,A.S.;Almeida,L.K.d.S.D. EducaçãoFinanceira,CondiçãoSocioculturaleVulnerabilidade:umaanálise
dasaúdeebem-estarfinanceirodefamíliasmonoparentaisfemininas. InProceedingsoftheAnaisdoEncontrodaAssociação
NacionaldePós-GraduaçãoePesquisaemAdministração,ANPAD,Fortaleza,Brazil,16–18May2019.
4. Camargo,R.Z.;Junior,M.F.;Strehlau,S. VulnerabilidadeeEducaçãoFinanceira:AVisãodeGerentesdeBanco;RevistaInterdisciplinar
deMarketing:SãoPaulo,Brazil,2020.
5. Banco Central do Brasil. Relatório de Letramento Financeiro. 2023. Available online: https://www.bcb.gov.br/content/
cidadaniafinanceira/documentos_cidadania/letramento/relatorio-de-letramento-financeiro.pdf(accessedon23June2025).
6. Akande, J.; Hosu, Y.; Kabiti, H.; Ndhleve, S.; Garidzirai, R. Financialliteracyandinclusionforruralagrarianchangeand
sustainablelivelihoodintheEasternCape,SouthAfrica. Heliyon2023,9,e16330.[CrossRef]

Sustainability2025,17,9219 30of33
7. Zaimovic,A.; Torlakovic,A.; Arnaut-Berilo,A.; Zaimovic,T.; Dedovic,L.; NuhicMeskovic,M. Mappingfinancialliteracy:
Asystematicliteraturereviewofdeterminantsandrecenttrends. Sustainability2023,15,9358.[CrossRef]
8. UNCapitalDevelopmentFund(UNCDF).FinancialInclusionandtheSDGs. Availableonline:https://www.uncdf.org/financial-
inclusion-and-the-sdgs?ref=hackernoon.com(accessedon20April2025).
9. Kyeyune, G.N.; Ntayi, J.M. Empoweringruralcommunities: Theroleoffinancialliteracyandmanagementinsustainable
development. Front.Hum.Dyn.2025,6,1424126.[CrossRef]
10. Swiecka,B.;Yes¸ildag˘,E.;Özen,E.;Grima,S. Financialliteracy:ThecaseofPoland. Sustainability2020,12,700.[CrossRef]
11. Garg,N.;Singh,S. Financialliteracyamongyouth. Int.J.Soc.Econ.2016,45,173–186.[CrossRef]
12. Goyal,K.;Kumar,S. Financialliteracy:Asystematicreviewandbibliometricanalysis. Int.J.Consum.Stud.2020,45,173–186.
[CrossRef]
13. Anshika.;Singla,A. Financialliteracyofentrepreneurs:Asystematicreview. Manag.Financ.2021,48,1352–1371.[CrossRef]
14. Haag,L.;Brahm,T. TheGenderGapinEconomicandFinancialLiteracy:AReviewandResearchAgenda. Int.J.Consum.Stud.
2025,49,e70031.[CrossRef]
15. Negi,P.;Jaiswal,A. Impactoffinancialliteracyonconsumerfinancialbehavior:Asystematicreviewandresearchagendausing
TCCMframework. Int.J.Consum.Stud.2024,48,e13053.[CrossRef]
16. Atkinson,A.;Messy,F.A. MeasuringFinancialLiteracy:ResultsoftheOECD/InternationalNetworkonFinancialEducation(INFE)Pilot
Study; TechnicalReport15,OECDWorkingPapersonFinance,InsuranceandPrivatePensions;OECDPublishing:Paris,France,
2012.[CrossRef]
17. Campbell,J.Y. RestoringRationalChoice: TheChallengeofConsumerFinancialRegulation. Annu. Rev. Econ. 2016,8,1–23.
[CrossRef]
18. Fernandes,D.;Lynch,J.G.,Jr.;Netemeyer,R.G. Financialliteracy,financialeducation,anddownstreamfinancialbehaviors.
Manag.Sci.2014,60,1861–1883.[CrossRef]
19. Huston,S.J. Measuringfinancialliteracy. J.Consum.Aff.2010,44,296–316.[CrossRef]
20. Lusardi,A.;Tufano,P. DebtLiteracy,FinancialExperiences,andOverindebtedness. BrookingsPap.Econ.Act.2015,2015,139–182.
[CrossRef]
21. Mandell,L. TheFinancialLiteracyofYoungAmericanAdults:Resultsofthe2008NationalJumptartCoalitionSurveyofHighSchool
SeniorsandCollegeStudents; TechnicalReport;JumptartCoalitionforPersonalFinancialLiteracy:Washington,DC,USA,2008.
22. OECD.OECD/INFEInternationalSurveyofAdultFinancialLiteracyCompetencies;TechnicalReport;OECDPublishing:Paris,France,
2016.
23. Remund,D.L. FinancialLiteracyExplicated:TheCaseforaClearerDefinitioninanIncreasinglyComplexEconomy. J.Financ.
Couns.Plan.2010,21,66–81.[CrossRef]
24. Sherraden,M.;Johnson,L.;Elliott,W.;Porterfield,S.;Rathbun,A. FinancialCapabilityinChildren:EffectsofParticipationina
School-BasedFinancialEducationandSavingsProgram. J.Sociol.Soc.Welf.2011,38,69–91.[CrossRef]
25. Bucher-Koenen,T.;Lusardi,A. FinancialLiteracyandRetirementPlanninginGermany. J.PensionEcon.Financ.2011,10,565–584.
[CrossRef]
26. Lusardi,A.;Mitchell,O.S. Financialliteracyandretirementplanning: NewevidencefromtheRANDAmericanLifePanel.
J.PensionEcon.Financ.2011,10,509–525.[CrossRef]
27. Hastings,J.S.;Madrian,B.C.;Skimmyhorn,W.L. Financialliteracy,financialeducation,andeconomicoutcomes. Annu.Rev.Econ.
2013,5,347–373.[CrossRef][PubMed]
28. Hsu,J. Agingandstrategiclearning:Theimpactofspousalincentivesonfinancialliteracy. J.Hum.Resour.2016,51,1036–1067.
[CrossRef]
29. Jappelli,T.;Padula,M. Investmentinfinancialliteracyandsavingdecisions. J.Bank.Financ.2013,37,2779–2792.[CrossRef]
30. Lusardi,A.;Mitchell,O.S. Financialliteracyandretirementpreparedness:Evidenceandimplicationsforfinancialeducation.
Bus.Econ.2007,42,35–44.[CrossRef]
31. Vitt,L.;Anderson,C.;Kent,J.;Lyter,D.M.;Siegenthaler,J.K.;Ward,J.PersonalFinanceandtheRushtoCompetence:FinancialLiteracy
EducationintheUS;InstituteforSocio-FinancialStudies:Middleburg,VA,USA,2000.
32. FinancialIndustryRegulatoryAuthority(FINRA). Non-TraditionalCostsofFinancialFraud; TechnicalReport;FINRA:Washington,
DC,USA,2015.
33. Gilovich,T.;Kumar,A.;Jampol,L. Awonderfullife:Experientialconsumptionandthepursuitofhappiness. J.Consum.Psychol.
2015,25,152–165.[CrossRef]
34. Isaia,E.;Oggero,N.;Sandretto,D. Isfinancialliteracyaprotectiontoolfromonlinefraudinthedigitalera? J.Behav.Exp.Financ.
2024,44,100977.[CrossRef]
35. Tabak,B.M.;Silva,E.B.;Horta,R.;Christiano,T.;Tabak,G.C. ModelingFinancialLiteracyUsingMultilevelItemResponseTheory
andtheCOVID-19Pandemic.2023. Availableonline:https://ssrn.com/abstract=4368359(accessedon1August2025).

Sustainability2025,17,9219 31of33
36. Paradgma;DataFolha. PrimeiraPesquisaNacionaldasCriptomoedas.2025. Availableonline:https://criptopelobrasil.com.br/
(accessedon10August2025).
37. Zhang,Y.;Chatterjee,S. Financialwell-beingintheUnitedStates:Therolesoffinancialliteracyandfinancialstress. Sustainability
2023,15,4505.[CrossRef]
38. Kahneman,D.;Tversky,A.ProspectTheory.AnAnalysisofDecisionMakingUnderRisk;WorldScientific:Singapore,1977.[CrossRef]
39. Kahneman,D.;Frederick,S. RepresentativenessRevisited:AttributeSubstitutioninIntuitiveJudgment.InHeuristicsandBiases:
ThePsychologyofIntuitiveJudgment;Gilovich,T.,Griffin,D.,Kahneman,D.,Eds.;CambridgeUniversityPress:NewYork,NY,
USA,2002;pp.49–81.
40. FinancialLiteracySurvey. FinancialLiteracySurvey2022:Results; TechnicalReport;PublicRelationsDepartment,BankofJapan:
Tokyo,Japan,2022.
41. Chalmers,R.P. mirt:AMultidimensionalItemResponseTheoryPackagefortheREnvironment. J.Stat.Softw.2012,48,1–29.
[CrossRef]
42. Anderloni,L.;Bacchiocchi,E.;Vandone,D. Householdfinancialvulnerability:Anempiricalanalysis. Res.Econ.2012,66,284–296.
[CrossRef]
43. Al-Omoush,K.S.;Gomez-Olmedo,A.M.;Funes,A.G.Whydopeoplechoosetocontinueusingcryptocurrencies? Technol.Forecast.
Soc.Change2024,200,123151.[CrossRef]
44. Eren,B.M.;Taspinar,N.;Gokmenoglu,K.K. Theimpactoffinancialdevelopmentandeconomicgrowthonrenewableenergy
consumption:EmpiricalanalysisofIndia. Sci.TotalEnviron.2019,663,189–197.[CrossRef]
45. Ye,J.;Kulathunga,K.M.M.C.B. HowdoesfinancialliteracypromotesustainabilityinSMEs?Adevelopingcountryperspective.
Sustainability2019,11,2990.[CrossRef]
46. Waller,L.G.;Johnson,S. ThepossiblecontributivevalueofcryptocurrenciestoSmallIslandDevelopingStates. Int.J.Blockchains
Cryptocurrencies2022,3,60–79.[CrossRef]
47. Alharbi,A.;Sohaib,O. TechnologyReadinessandCryptocurrencyAdoption:PLS-SEMandDeepLearningNeuralNetwork
Analysis. IEEEAccess2021,9,21388–21394.[CrossRef]
48. Toufaily,E. Anintegrativemodeloftrusttowardcrypto-tokensapplications:Acustomerperspectiveapproach. Digit.Bus.2022,
2,100041.[CrossRef]
49. Sonkurt,H.; Altinöz,A. Cryptocurrencyinvestment: Asafeventureoranewtypeofgambling? J.Gambl. Issues2021,47.
[CrossRef]
50. KiatSakared, P.; Chen, K.Y. The effect of flow experience on online game addiction during the COVID-19 pandemic:
Themoderatingeffectofactivitypassion. Sustainability2022,14,12364.[CrossRef]
51. Mashatan,A.;Sangari,M.S.;Dehghani,M. Howperceptionsofinformationprivacyandsecurityimpactconsumertrustin
crypto-payment:Anempiricalstudy. IEEEAccess2022,10,69441–69454.[CrossRef]
52. Hariguna,T.;Ruangkanjanases,A.;Madon,B.B.;Alfawaz,K.M. Assessingdeterminantsofcontinuanceintentiontowardcryp-
tocurrencyusage:Extendingexpectationconfirmationmodelwithtechnologyreadiness. SAGEOpen2023,13,21582440231160439.
[CrossRef]
53. Limayem,M.;Cheung,C.M. PredictingthecontinueduseofInternet-basedlearningtechnologies:theroleofhabit. Behav.Inf.
Technol.2011,30,91–99.[CrossRef]
54. Venkatesh,V.;Davis,F.D.;Morris,M.G.;Davis,G.B.;D.,F. Useracceptanceofinformationtechnology:Towardaunifiedview.
MISQ.2012,27,425–478.[CrossRef]
55. Sirohi,N.;Misra,G. Vulnerabilityofindividualstoeconomiccrimeandtheroleoffinancialliteracyinitsprevention:Evidence
fromIndia. InCrime,LawandSocialChange;Springer:Berlin/Heidelberg,Germany,2024;pp.1–32.[CrossRef]
56. Frederick,S. Cognitivereflectionanddecisionmaking. J.Econ.Perspect.2005,19,25–42.[CrossRef]
57. Jensen,A.R. ThegFactor:TheScienceofMentalAbility;Praeger:Westport,CT,USA,1998.
58. Epstein,S. IntegrationoftheCognitiveandPsychodynamicUnconscious. Am.Psychol.1994,49,709–724.[CrossRef]
59. Sloman,S.A. TheEmpiricalCaseforTwoSystemsofReasoning. Psychol.Bull.1996,119,3–22.[CrossRef]
60. Chaiken,S.;Trope,Y. Dual-ProcessTheoriesinSocialPsychology;GuilfordPress:NewYork,NY,USA,1999.
61. Putler,D.S. IncorporatingReferencePriceEffectsintoaTheoryofConsumerChoice. Mark.Sci.1992,11,287–309.[CrossRef]
62. Tversky,A.;Kahneman,D. AdvancesinProspectTheory: CumulativeRepresentationofUncertainty. InChoices,Values,and
Frames;SpringerNature:Berlin/Heidelberg,Germany, 2000;pp.44–66.[CrossRef]
63. Wang,M.;Rieger,M.O.;Hens,T. TheImpactofCultureonLossaversion. J.Behav.Decis.Mak.2016,30,270–281.[CrossRef]
64. Banerjee,A.V. Asimplemodelofherdbehavior. Q.J.Econ.1992,107,797–817.[CrossRef]
65. Raafat,R.M.;Chater,N.;Frith,C. Herdinginhumans. TrendsCogn.Sci.2009,13,420–428.[CrossRef]
66. DaGamaSilva,P.V.J.;Klotzle,M.C.;Pinto,A.C.F.;Gomes,L.L. Herdingbehaviorandcontagioninthecryptocurrencymarket.
J.Behav.Exp.Financ.2019,22,41–50.[CrossRef]
67. Kahneman,D. Thinking,FastandSlow;Farrar,StrausandGiroux:NewYork,NY,USA,2011.

Sustainability2025,17,9219 32of33
68. Thaler,R.H.;Benartzi,S. SaveMoreTomorrow™:Usingbehavioraleconomicstoincreaseemployeesaving. J.PoliticalEcon.2004,
112,S164–S187.[CrossRef]
69. Loewenstein,G.;Thaler,R. Anomalies:IntertemporalChoice. J.Econ.Perspect.1989,3,181–193.[CrossRef]
70. Hershfield,H.E.;Goldstein,D.G.;Sharpe,W.F.;Fox,J.;Yeykelis,L.;Carstensen,L.L.;Bailenson,J.N. IncreasingSavingBehavior
ThroughAge-ProgressedRenderingsoftheFutureSelf. J.Mark.Res.2011,48,S23.[CrossRef]
71. Yes¸ilkayalı,D. ProcrastinationandFutureDiscounting. J.Int.Soc.Res.2025,7,275.
72. Sheffer,C.E.;MacKillop,J.;Fernandez,A.;Christensen,D.;Bickel,W.K.;Johnson,M.W.;Mathew,M. InitialExaminationof
PrimingTaskstoDecreaseDelayDiscounting. Behav.Processes2016,128,144–152.[CrossRef]
73. Witten,I.H.;Frank,E. PracticalMachineLearningToolsandTechniques,2nded.;Elsevier:Amsterdam,TheNetherlands,2005.
74. Oliveira,B.L.C.A.d.;Thomaz,E.B.A.F.;Silva,R.A.d. Theassociationbetweenskincolor/raceandhealthindicatorsinelderly
Brazilians:AstudybasedontheBrazilianNationalHouseholdSampleSurvey(2008). Cad.SaúdePública2014,30,1438–1452.
[CrossRef][PubMed]
75. Paixão,M.;Rossetto,I.;Montovanele,F.;Carvano,L.M. RelatórioAnualdasDesigualdadesRaciaisnoBrasil:2009–2010;Garamond:
RiodeJaneiro,Brazil,2010.
76. daSilvaPaiva,L.;Oliveira,F.R.;deAlcantaraSousa,L.V.;dosSantosFigueiredo,F.W.;deSá,T.H.;Adami,F. DeclineinStroke
MortalityBetween1997and2012bySex:EcologicalStudyinBraziliansAged15to49Years. Sci.Rep.2019,9,2962.[CrossRef]
[PubMed]
77. Jiang,T.;Gradus,J.L.;Rosellini,A.J. SupervisedMachineLearning:ABriefPrimer. Behav.Ther.2020,51,675–687.[CrossRef]
78. Silva,T.C.;Braz,T.;Tabak,B.M. Mappingthelandscapeofenergymarketsresearch: Abibliometricanalysisandpredictive
assessmentusingmachinelearning. EnergyEcon.2024,136,107698.[CrossRef]
79. Taunk,K.;De,S.;Verma,S.;Swetapadma,A. ABriefReviewofNearestNeighborAlgorithmforLearningandClassification.
InProceedingsofthe2019InternationalConferenceonIntelligentComputingandControlSystems(ICCS),Madurai,India,
15–17May2019;pp.1255–1260.[CrossRef]
80. Cortes,C.;Vapnik,V. Support-VectorNetworks. Mach.Learn.1995,20,273–297.[CrossRef]
81. Breiman,L. Randomforests. Mach.Learn.2001,45,5–32.[CrossRef]
82. Rumelhart,D.E.;McClelland,J.L.,LearningInternalRepresentationsbyErrorPropagation. InParallelDistributedProcessing:
ExplorationsintheMicrostructureofCognition:Foundations;MITPress:Cambridge,MA,USA,1987;pp.318–362.
83. Zou,H.;Hastie,T. RegularizationandVariableSelectionViatheElasticNet. J.R.Stat.Soc.Ser.BStat.Methodol.2005,67,301–320.
[CrossRef]
84. Kumar,S.;Bhatnagar,V. AReviewofRegressionModelsinMachineLearning. J.Intell.Syst.Comput.2021,2,40–47.[CrossRef]
85. Carvalho,D.V.;Pereira,E.M.;Cardoso,J.S. MachineLearningInterpretability:ASurveyonMethodsandMetrics. Electronics
2019,8,832.[CrossRef]
86. Hermosilla,P.;Berríos,S.;Allende-Cid,H. ExplainableAIforForensicAnalysis:AComparativeStudyofSHAPandLIMEin
IntrusionDetectionModels. Appl.Sci.2025,15,7329.[CrossRef]
87. Lundberg,S.M.;Lee,S.I. Aunifiedapproachtointerpretingmodelpredictions. Adv.NeuralInf.Process.Syst.2017,30,4768–4777.
88. Ribeiro,M.T.;Singh,S.;Guestrin,C. “Whyshoulditrustyou?”Explainingthepredictionsofanyclassifier. InProceedingsofthe
22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining,SanFrancisco,CA,USA,13–17August
2016;pp.1135–1144.
89. PesquisaDataSenado. PanoramaPolítico2024:ApostasEsportivas,GolpesDigitaiseEndividamento;InstitutodePesquisaDataSenado:
Brasilia,Brazil,2024.
90. Sundarasen,S.;Rajagopalan,U.;Ibrahim,I.FinancialSustainabilityThroughLiteracyandRetirementPreparedness. Sustainability
2024,16,10692.[CrossRef]
91. Tulcanaza-Prieto,A.B.;Cortez-Ordoñez,A.;Rivera,J.;Lee,C.W. IsDigitalLiteracyaModeratorVariableintheRelationship
BetweenFinancialLiteracy,FinancialInclusion,andFinancialWell-BeingintheEcuadorianContext? Sustainability2025,17,2476.
[CrossRef]
92. FundaçãoGetulioVargas. IndicadordeIncertezadaEconomia(IIE-Br)—IndicadorMensaldeAbrilde2025.2025.Available
online:https://portalibre.fgv.br/indicador-de-incerteza-da-economia(accessedon21May2025).
93. Katnic,I.; Katnic,M.; Orlandic,M.; Radunovic,M.; Mugosa,I. UnderstandingtheRoleofFinancialLiteracyinEnhancing
EconomicStabilityandResilienceinMontenegro:AData-DrivenApproach. Sustainability2024,16,11065.[CrossRef]
94. Sarker,I.H. MachineLearning: Algorithms,Real-WorldApplicationsandResearchDirections. SNComput. Sci. 2021,2,160.
[CrossRef]
95. deLimaLemos,R.A.; Silva,T.C.; Tabak,B.M. Propensiontocustomerchurninafinancialinstitution: Amachinelearning
approach. NeuralComput.Appl.2022,34,11751–11768.[CrossRef]

Sustainability2025,17,9219 33of33
96. Schonlau,M.;Zou,R.Y. Therandomforestalgorithmforstatisticallearning. StataJ.2020,20,3–29.[CrossRef]
97. Rosseel,Y. lavaan:AnRPackageforStructuralEquationModeling. J.Stat.Softw.2011,48,1–36.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.