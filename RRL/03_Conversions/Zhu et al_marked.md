DataandInformationManagement7(2023)100041
ContentslistsavailableatScienceDirect
Data and Information Management
journalhomepage:www.journals.elsevier.com/data-and-information-management
Not transparent and incomprehensible: A qualitative user study of an
fi
AI-empowered nancial advisory system
Hui Zhua,*, Eva-Lotta Salln € as Pysanderb, Inga-Lill So € derberga
aDivisionofRealEstateBusinessandFinancialSystems,KTHRoyalInstituteofTechnology,Sweden
bDivisionofMediaTechnologyandInteractionDesign,KTHRoyalInstituteofTechnology,Sweden
A R T I C L E I N F O A B S T R A C T
Keywords: AI-empoweredandalgorithm-drivenautomatedfinancialadvisorysystems,alsoknownasRobo-advisors,have
robo-advisor beenrapidlyimplementedbyserviceprovidersandcustomersinfinancialservicemarkets.Yet,fewempirical
automatedinformationsystem studiesinvestigatecustomers’experienceinteractingwithfullyfunctionalRobo-advisorsinreal-lifescenarios.
AI-empoweredsystem Also,itisstillunknownhowthedesignoftheautomatedsystemcanaffectcustomers’perceptionandadoptionof
userstudy
financialservice thisnewtechnology.Tomitigatethesegaps,24participantswithdifferentlevelsofexperienceandunderstanding
offinancialinvestmentwereaskedtouseaRobo-advisorfromaretailbankandperformthetasks.Byconducting
FinTech
observations and retrospective post-test interviews, we find that participants do not fully perceive the social
aspects supposed to be provided by Robo-advisors. The overarching problems are, among others, a lack of
transparencyandincomprehensibleinformation.Thisresultsindistrustoftheresultsgeneratedbythissystem,
whichnegativelyaffectscustomers’adoptionoftheinvestmentadviceprovidedbytheRobo-advisor.Thepo-
tentialofinteractivedatavisualizationisalsodetected.Thisworkcontributestotheunderstandingofcustomers
regardingtheirperceptionandadoptionbasedontheiruseofafunctionalRobo-advisorandproposesdesign
takeawaysfortransparentandcomprehensibleautomatedadvisorysystemsinfinancialservicecontexts.
1. Introduction The emergence and development of Robo-advisors (RAs) were
initially driven by financial service providers (e.g., retail banks) to
AI-empowered and algorithm-driven automated systems have been replace human advisors’ services to cut labor costs and transfer tradi-
rapidlyimplementedandarecommonlyusedinpeople’severydaylife. tionalservicesfromofflinetoonline(Fisch,Labour(cid:2)e,&Turner,2019).
Thistypeoftechnologyenablestheautomationofservicesbyeliminating Also,serviceproviderswanttoattractmorecustomerswhoaredifferent
humanintervention;andhasbeenclaimedtoprovidedisruptivepoten- fromthoseinconventionaladvisoryservicesbypromotingRAs’lowcost,
tial and is widely used across service sectorsand industries, including flexibility,accessibility24/7,andthesameservicequalityasahuman
managerialdecision-making(Jarrahi,2018;Shrestha,Ben-Menahem,& advisor.Robo-advisorshaveshowntheirpotentialformitigatingbiases
VonKrogh,2019),customizedrecommendations(Jameson,Konstan,& andconflictsofinterestinhumanadvisoryencounters(Bolton,Freixas,&
Riedl,2002;Namjun,Hosoo,Sangman,&HWANG,2019),medicalcare Shapiro, 2007; Burke, Hung, Clift, Garber, & Yoong, 2015; Faloon &
(Cai,Winter,Steiner,Wilcox,&Terry,2019;Holzinger,Biemann,Pat- Scherer,2017)andhaveproventheircommercialvaluesinmarkets.UP
tichis, & Kell, 2017; Yang, Steinfeld, & Zimmerman, 2019), and auto- toJanuary2022,twoindependentleadingRAcompaniesintheworld
mobiles(Azaria,Rosenfeld,Kraus,Goldman,&Tsimhoni,2015).Inthe reporteddouble-digitincreasesinaccountopeningsduringthepandemic
personalfinancecontext,atypeofalgorithm-drivenautomatedfinancial (InsiderIntelligence,2021).
advisoryserviceonthemobileterminal,alsoknownas“Robo-advisor”or DespiteRAs’rapidgrowth,comparedwiththeconventionaladvisory
“Robo-advisory”inbusinessmanagementandfinancialcommunities,has service,theperceptionofRAsisunclear,andtheiradoptionisstilllow
become popular among customers of retail banks and FinTech com- amongcustomersinthefinancialservicemarket(Brown,2017;ErinEI,
panies,especiallyduringtheCOVID-19whenpeoplehavebecomemore 2020;Jung,Dorner,Weinhardt,&Pusmaz,2018).InInformationSys-
openfordigitalandautomatedservice(Ben-David&Sade,2020;Gan, tems and Business Studies, research mainly focuses on customers’
Khan,&Liew,2021;Guo&Polak,2021;InsiderIntelligence,2021). perception of RAs in general and their adoption of the final
* Correspondingauthor.Teknikringen10b,10044,Stockholm,Sweden.
E-mailaddresses:huizhu2@kth.se(H.Zhu),evalotta@kth.se(E.-L.Salln€asPysander),ingalill.soderberg@abe.kth.se(I.-L.So€derberg).
https://doi.org/10.1016/j.dim.2023.100041
Received27September2022;Receivedinrevisedform13April2023;Accepted20April2023
2543-9251/©2023TheAuthors.PublishedbyElsevierLtdonbehalfofSchoolofInformationManagementWuhanUniversity.Thisisanopenaccessarticleunderthe
CCBY-NC-NDlicense(http://creativecommons.org/licenses/by-nc-nd/4.0/).

H.Zhuetal. DataandInformationManagement7(2023)100041
recommendation(i.e.,investmentportfolio)generatedbyRAs.Inmost functional RAs in real-life scenarios; (2) the relationship between the
cases,theadoptioninthesearticlesindicatescustomers’intentiontouse designoftheautomatedsystemandcustomers’perceptionandadoption
RAs.Manyinfluencingfactorswerereportedfromdifferentaspects,such of RAs is still unknown. This study aims to understand customers’
as userdemographics,theirinvestmentintention,trust,perceiveduse- experienceofusingaRA,particularlytoshedlightonhowthesystem
fulness, background knowledge, and social media (Ben-David & Sade, design can affect their perceptionand adoptionof RAs. Perceptionfo-
2020;Ganetal.,2021;Hildebrand&Bergner,2021;Hohenberger,Lee, cuses on customers’ holistic experience and understanding of the RA
& Coughlin, 2019; Lourenço, Dellaert, & Donkers, 2020; Seiler & systemandservicebasedontheirinteractionthroughoutallaspectsof
Fanenbruck, 2021; Wu & Gao, 2021). Most of these studies analyzed thecustomer’sjournal,fromonboardingtothefinalgeneratedportfolio.
customersurveydataanddevelopedmodelsbasedonTAM(Technology Adoption addresses their intention and willingness to use RAs in the
AcceptanceModel)orUTAUT(UnifiedTheoryofAcceptanceandUseof future after they review the final recommendation generated by RAs
Technology) theories. Their respondents had no experience using based on their real-life situation (e.g., personal income, risk appetite,
Robo-advisors, and the users were limited to certain groups, such as loansandsavings,etc.).The24participantswithdifferentlevelsofin-
activeinvestors.Understandingthemotivationsandexistingobstaclesto vestmentexperienceandfinancialunderstandingjoinedthelabexperi-
using and adopting RAs can provide insights for service providers to ment,andtheirdemographicswerealsocollectedandconsideredinthe
implement marketing strategies. However, these studies have limited analysis.Thispaperdiscussesfullyautomatedsystemsonthemobileend,
contributionstoimprovingexistingsystemdesignbecausetheroleofa soahybridsystemisnotwithinthescope.Theusertestapproachesfrom
Robo-advisorysystemisstillunknownintermsofuserperceptionand HCI include pre-test surveys, assigning scenarios and tasks, observing
adoption.Thus,empiricalstudiesshouldswitchtoamoreuser-centered performance, and collecting feedback from retrospective post-test in-
approach to data based on customers’ experience of using a RA. And terviews.Theresearchquestionsinclude:(1)howarecustomersableto
more attention should be paidto how the system can influence users’ interactwitharetailbankRAsystem;and(2)howdoesthisexperience
perceptionandadoption. affecttheirperceptionandadoptionofthisRAsystem?
Transparencyandtrustarecomplexandparticularlysignificanttopics ThisarticlebrieflyintroducestheRAsystemanditsimplementation
whenAI-empoweredsystemsarecontextualizedincustomers’financial infinancialservicesectors.First,wepresentaninterdisciplinarylitera-
decisions.Financialdecisionscanbehigh-stakebehaviorsandcustomers ture review of the state-of-art research that is relevant. Then, the
facethepossibilitytolosetheirmoney.Customersinfinancialservices, empiricaluserstudyisintroducedregardingthetestprocedure,partici-
unlikeusersinotherautomatedsystems,tendtobe“vulnerable”(Mogaji, pant recruitment, data collection, and analysis. Because most RAs in
Soetan, & Kieu, 2021). Any unfair or untrustworthy perception will financialmarketshavesimilarinterfacesandfeatures.TheselectedRAin
adverselyandnegativelyaffectcustomers’adoption.Customers’under- theempiricalstudyisarepresentativeRAapplicationthatenjoysalarge
standingoftheinformationprovidedbyRAsisalsoessential.Duetothe number of users and is produced by a well-known financial group in
lack of human experts’ assistance or explanation, customers highly Scandinavia countries. Its name is anonymous. Last, findings are pre-
dependontheirownunderstatingwhenusingRAs,inwhich,mostin- sentedanddiscussed.Thisworkfindsthelagincustomers’perceptionof
formationisinwrittenformordatavisualization(Salo&Haapio,2017). RA compared with its business ambitions. Also, the perceived non-
Design research in the internet-based era came up with solutions as transparency and incomprehensible information in the RA system
collaborative interfaces or platforms that enhance perceived trans- causedistrust,andthoseexperiencesnegativelyaffecttheiradoptionof
parency and comprehensibility (Kilic, Heinrich, & Schwabe, 2015; theportfoliogeneratedbyRA.However,thevisualizationtoolisprom-
Nueesch,Puschmann,&Alt,2014,2016;Nussbaumer,Matter,Reto(cid:3)a; isingtofillthesegaps.
Nussbaumer&Matter,2011;Porta,etal.,2012).However,itisdifficult This work extends the knowledge of system design in customers’
forthesedesignsolutionstoadapttotheAI-empoweredsystem.Without perceptionandadoptionofAI-empowereddecisionsinfinancialservices
humanintervention,the“black-box”natureofthealgorithmembedded by contributing empirical evidence and proving the user test as an
inthissystemmakesitdifficultforuserstounderstandwhyandhowthis effective method. Also, it elicits the existing problems that can be
decision(i.e.,recommendedinvestmentportfolio)ismadeandclaimed improved in the design of AI-empowered automated systems. Most
tobe“optimized”forthem.Thismightleadtodistrustandlowadoption importantly,itarticulatesthedemandfromcustomersforaRAsystem,
eveniftheAI’sdecisionisaccurate(Dikmen&Burns,2022).Twoap- improvingtransparencyandcomprehension.Thiscompensatesforprior
proaches are detected by researchers in Human-computer/robot Inter- RAempiricalstudiesbyaskingparticipantstouseawell-functionalretail
action (HCI/HRI). One of them is the anthropomorphic design which bankRAandviewtheresultgeneratedbyAI.
aims to compensate for the lack of human advisors in the automated
process(Adam,Toutaoui,Pfeuffer,&Hinz,2020;Deng&Chau,2021; 2. Literaturereview
Hildebrand&Bergner,2021;Morana,Gnewuch,Jung,&Granig,2020).
But the requirement of human-like design has not been theoretically Starting with an introduction to RAs’ implementation, this part
problematized in empirical studies. Even though those studies have summarizesexistingresearchregardingRAsfrominterdisciplinaryper-
provedthattheperceivedsocialpresencecandelegatemoretrust,these spectives(e.g.,informationsystems,servicemarkets,designscience)and
studies have not shown whether a human-like robot is useful for their challenges that can benefit from this study. This section also in-
achieving customers’ goals in financial service contexts. The other cludesthekeyconceptsrecurringinthisstudy,suchastransparencyand
approachistransparentandresponsibleAIsystemsinfinancialservices trust.
(Anshari, Almunawar, Masri, & Hrdy, 2021; Stefanel & Goyal, 2019;
Zheng,Zhu,Li,Chen,&Tan,2019).Yet,existingresearchrarelyillus- 2.1. TheimplementationofRAsinfinancialservice
trateswhichtypeoftransparencyislackingandwhatisneededbasedon
users’ lived experiences and how to incorporate users’ demands into RAs use algorithms to provide customers with financial advisory
existingsystems.Moreover,RAsaremulti-stakeholderautonomoussys- servicesandsupporttheirinvestmentdecisions.Thisimplementationis
tems(Sonboli,Smith,CabralBerenfus,Burke,&Fiesler,2021),inwhich standardizedinthemarketsbutmightbeslightlydifferentaccordingto
thecustomer’sprofitsareintegratedwithproviders’businessgoalsand laws and regulations. Normally, these systems include four stages: (i)
financialregulations.Allthesefactorsmakeitacomplexbuturgentissue personaldatacollection(customer’ssavings,incomes,andpreferences),
tofigureouttherelationshipbetweenRAs’systemdesignandcustomers’ (ii)riskassessment(usingastandardizedsurveytocategorizecustomers
perceptionandadoptionofRAs. into different risk-apatite groups), (iii) wealth management advice
The research gaps identified in previous literature are: (1) few (providing an investment portfolio based on collected data and algo-
empiricalstudiesinvestigatecustomers’experienceinteractingwithfully rithms),and(iv)continuousinvestmentmaintenance(Fischetal.,2019;
2

H.Zhuetal. DataandInformationManagement7(2023)100041
Jung,Dorner,Glaser,&Morana,2018;Jung,Glaser,&Ko€pplin,2019). RAscanprovidetheexpectedbenefitsthatcustomersfeelentitledto.To
Besides,someadditionalphasesareimplementedaccordingtonational maximizetrust,humanadvisorshavebeeninvolvedinthisprocessinthe
regulationsandgovernances,forexample,abasicfinancialliteracytest conventionalfinancialserviceencounter,whiletheyhavebeenincreas-
or a sustainable investmentalternative (EuropeanCommission, 2021). ingly augmented with AI-empowered technology over time. In tradi-
Somecanevenharvesttaxlosses(Berger,2015).Usually,thecomplete tionalserviceencounters,thesocialinteractionandrelationshipbetween
RAworkflowisConfiguration(i&ii),MatchingandCustomization humanadvisorsandcustomerssignificantlyaffectcustomers’perception
(iii),andMaintenanceandRebalancing(iv)(Jung,Dorner,Glaser,& ofadvisorcredibilityandwillingnesstofollowtheiradvice(So€derberg,
Morana,2018;Jungetal.,2019).IntheConfigurationPhase,byfillingin 2013). With the AI replacement, the higher trust towards the Robo
questionnaires or answering specific questions, users’ personal infor- advisor, the more likely consumers will adopt its recommendation
mation,financialsituation,risktolerance,andpreferencesarecollected (Bruckes,Westmattelmann,Oldeweme,&Schewe,2019).Thus,theso-
forcustomerprofilingandassessment.TheRAsaresupposedtoidentify cialandanthropomorphicdesigncouldbealternativesolutionstodele-
users’ requirements and aims of financial investment. Then, users are gatetrusttocompensateforthelackofhumaninterventionintheRAs
automatically classified into different groups according to individual (Bruckes et al., 2019). These studies usually articulate the perceived
profiles by the system. In Matching & Customization, an undisclosed socialpresenceasanthropomorphisminRAs.Forexample,researchers
algorithm is deployed to match a customer’s profile to a portfolio investigatedverbalandvisualcues (Adametal., 2020), socialcuesin
recommendation(i.e.,acollectionofdifferenttypesoffinancialinvest- conversational chat (Day, Lin, & Chen, 2018; Hildebrand & Bergner,
mentproductslikestocks,bonds,orexchange-tradedfunds[ETFs]).Like 2021), visually human-like design (Deng & Chau, 2021), and varying
otheralgorithm-basedsystems,thisstepisa“blackbox”(Litterscheidt& degrees of a human-like chatbot (Morana et al., 2020). These have
Streich,2020).Datavisualizationiscommonlyusedinthissteptoconvey proven the possible influence of perceived social presence towards a
investmentplanningandtheestimatedperformanceoftherecommended highertrustandadoptionofRAsandthefinalrecommendation.How-
portfolio. In Maintenance and Rebalancing, the system automatically ever, the human-like design in business implementation and financial
monitorsandrebalancestheportfoliotomeettheoptimalmodel. servicesisnotaone-size-fits-allsolutionbecauseotherfactorsdynami-
Meanwhile, its performance and adjustment will be regularly cally influence trust (Cheng et al., 2019). Also, trust delegated by
communicatedandinformedtotheusers.Eventhoughuserscanreach human-likenessrobotsisvulnerabletobeingdisruptedbyfactorssuchas
customerserviceanytimetheyneedsupport,nohumaninterventionis theunsatisfiedexperienceofusingchatbotsoralackofunderstanding
expectedduringthewholeprocess;therefore,the“Robo-”hereindicates (Dikmen & Burns, 2022). An empirical study shows that compared to
the fully automated self-service. RA is initially used in business and responsiveness,customization,andsuchtraits,likabilityisnotsignificant
financialcommunities,thenextendedtoISandHCI/HRIresearch. tocustomers’intentiontousechatbotsinfinancialservices(Lee&Park,
2019).
2.2. StudiestounderstandRAcustomers
2.4. Informationsysteminfin-tech
Because RAs are still emerging phenomena, it is of great value for
developersandserviceproviderstounderstandtheuserdemographics, RAsareautomateddecision-makingsystems,fundamentallydisrup-
motivations,attitudes,andexpectations.Studiesrevolvingaroundusers’ tivecomparedwithotherdigitalfinancialservicesprovidedbybanksor
perceptionandadoptionaremainstreamobjectivesinInformationSys- otherretailfinancialinstitutions.Informationsystemsarealsoappliedin
tems and Business Studies in Financial Market. These user studies human-advisoryencounters,namely,acollaborativeplatformasatool
collectedsurveydatafromuserstoestablishtrustandadoptionmodelsof for human advisors to advise customers. Prior research addressing IT-
RAs (e.g., unified theory of acceptance and use of technology) across support (web-based) systems in digital financial services has detected
temporal(e.g.,atCOVID-19crisis)andregionalscopes(e.g.,Germany that transparency and information symmetry are important principles
andMalaysia.)(Lourençoetal.,2020;Seiler&Fanenbruck,2021;Todd (Kilicetal.,2015;Nueeschetal.,2014,2016;Nussbaumer,Matter,Reto
& Seay, 2020; Wu & Gao, 2021). Their models help to explain the (cid:3)a;Nussbaumer&Matter,2011;Nussbaumer,Matter,&Schwabe,2012;
influentialfactorsthatleaduserseithertoadopttheRA’sfinalrecom- Porta,etal.,2012).Thesestudiesalsoindicatethatthesystemdesignof
mendationorinvestmoneybyacceptingthisservice.Inthosemodels, digitaladvisoryservicesisasimportantastheperformanceoftherec-
somefactorsregardingcustomers’experienceofRAswerementionedbut ommended financial products. Compared with these digital systems
have not been deeply discussed by connecting them with RA system wherehumaninterventionstillexists,anautomatedsystemissupposed
design.Specifically,thosefactors,includingtheperceivedusefulnessand topromisemoretransparencyregardingcostandtheadvisoryprocess
performanceexpectations,werecollectedfromsurveydataandwerenot (Tertilt & Scholz, 2018). However, these studies in financial service
based on their real experience using RAs. To compensate for this, a systems focused on web-based services rather than a fully-automated
user-centereddesignstudywasconductedforrisk-averseandlow-budget system,i.e.,RA.
customers (Jung, Dorner, Weinhardt, & Pusmaz, 2018). Their work AccordingtoTurilliandFloridi(2009),transparencyistheprocessof
contributesprinciplestoRAdesign:easeofinteraction,workefficiency, making information explicitly and openly available so that users can
informationprocessing,cognitiveload,andadvisorytransparency.These exploit the disclosing information to make decisions. In information
principles,especiallythelasttworegardingtheuser’scognitiveloadand systems anddesign science,the challengeof informationtransparency
transparency, are essential design takeaways for RA system design. can be addressed by Explainable AI (XAI). According to Eschenbach
However,thesedesignprincipleswerelimitedbyfocusingononespe- (2021), transparency is necessary for trust and determining if AI is
cificcustomergroup,andbecausethetestedsystemwasstillindevel- trustworthy.Basedonthisphilosophy,XAIcanbealensforresearchers
opmentanditeration,thefinalrecommendationgeneratedbytheRAwas touncoverusers’acceptanceandtrustinAI(Shin,2021b).XAIhasbeen
notdiscussedinthispaper. implementedandexaminedinvaryingsettings[e.g.,mentalhealth(Wolf
&Ringland,2020),recommendationsystem(Shin,2021a)],aswellasin
2.3. Anthropomorphicrobottodelegatetrust the RA context (Ben David, Resheff, & Tron, 2021). These studies
discoveredthepotentialofusingXAIfordesigningaRAthatbuildstrust
Financialandinvestmentdecisionshavetraditionallyandhistorically and adoption, even though most of them were not contextualized in
beenabouttrust.Trustcanbedefinedas“thewillingnesstotakeactions financialcontexts.
ofanotherentitybasedontheexpectationthattheotherwillperforma Asecondchallengenormallyisnon-expertuserswholackthedomain
particularaction,regardlessoftheabilitytomonitororcontrolthatother knowledge to comprehend and interpret the explanation information
part”(Bedu(cid:2)e&Fritzsche,2022,p.533).Thus,inthiscase,trustisaboutif providedby thisAI-empowered service.Empiricalstudieshaveshown
3

H.Zhuetal. DataandInformationManagement7(2023)100041
thatthetypicalRAuserisyoungwithlimitedexperienceinthefinancial byreferringtothescreenrecordingoftheirtaskperformanceduringthe
market(Fischetal.,2019;InsiderIntelligenceEditors,2021),low-risk, interview. The reason for combining these methods was that the
low-budget (Jung, Dorner, Weinhardt, & Pusmaz, 2018), and with think-aloud protocol normally used in usability tests is somewhat un-
limited financial literacy (Brenner & Meyll, 2020). This demonstrates suitable for this study. Because participants need a quiet and secure
that discussions around “comprehensible” RA systems are important environmentwheninputtingtheirfinancialdata,suchasloans,savings,
because,morethanothers,non-expertcustomersneedanexpertsystem and incomes, in real-life scenarios, they should concentrate more on
to help them make an investment decision. Prior research shows that dealingwithcomplexinformationinsteadofspeakingoutaboutmental
domain knowledge can help non-expert customers with less financial activitieswhiledoingthetasks.
understanding and investment experience interpret the explanation Thus,intheformalusertests,thescreenrecordingwouldbeshownto
providedbytheAI-empoweredsystem(Dikmen&Burns,2022).InRAs, participantsasareferenceandreminderwhenthey,duringthepost-test
domain knowledge usually indicates financial or investment under- interview,wereaskedabouttheiractionsoriftheyactivelymentioned
standing, and it is known as financial literacy when systematically certainoperationsandthoughtsaboutdetailsintheirinteractionwiththe
measuredbyastandardizedtest.Datavisualizationhasbeenproventobe interface.Insteadofevaluatingtheusabilityoftheexistingsystem,this
an effective tool in supporting customers’ understanding and decision user test primarily focused on understanding how users processed in-
making (Eberhard, 2021; Perdana, Rob, & Rohde, 2018; Tang, Hess, formation underneath behaviors and their perceptions and behavioral
Valacich, & Sweeney, 2014). However, it is still unknown how the intentions(i.e.,perceptions)afterinteractingwithaRA.Thistestaimed
financial understanding is delivered by existing RA systems. Also, the to detect existing concerns and problems through self-explanations,
usage and effect of interactive data visualization in RAs remain to be supported by the interview questions rather than the researchers’
investigatedbyempiricalstudies. observations.
3. Methodology 3.3. Procedure
Thisusertestincludesanintroduction,pre-survey,scenariosetting, Alltheusertestswereconductedinaquietroominalabenviron-
task performance by using the RA application, and a post-test retro- ment.Thecompleteusertestcontainedthreesessions:(1)pre-survey,to
spectiveinterview.Thesurveydata,interviewtranscriptions,andscreen collectparticipant’sdemographicinformation,self-reportedexperience
recordingsofparticipants’interactionwiththeinterfacewereanalyzed and knowledge in financial investment, and frequency of using tech-
accordingly. nologyandAIsystem;(2)performingthreetasksbyusingtheRA(video
isrecordingatthesametime);and(3)post-testretrospectiveinterview,
3.1. Participants answeringthequestionsintheinterview,inparallelwithdescribingand
explainingtheirbehaviorsbyreferringtothevideoplayback.
Tocomplementtheparticipantgroupsofpriorempiricalstudiesthat Beforetheusertest,eachparticipantwasinformedoftheaimsand
focusoneitherspecificusergroups(Jung,Dorner,Weinhardt,&Pusmaz, process of thistest; andwas askedto signthe consent form regarding
2018; Morana et al., 2020) or people who are actively in investment informationusageandprivacyprotection.
activities(Hildebrand&Bergner,2021),hereweaimedtorecruitpar-
ticipantscomingfrommorediversedemographicgroupsintermsofages 3.3.1. Tasksandscenarios
and different levels of financial understanding and investment experi- Onetaskwithscenarioswaspresentedtotheparticipantsinawritten
ence.ThischoicealsoconsidersthatthecustomersinclinedtouseRAs formatbeforeandwhiletheywereusingtheRA:(1)thinkaboutasce-
arechangingovertime(Fulk,Grable,&Kruger,2018;Ganetal.,2021; narioinwhichyouwanttoinvestyoursavingsforalong-orshort-term
Pradhan & Wang, 2020). This study does not aim to systematically target;(2)trythisRAasoneofyourinvestmentoptionsandexplorethis
compare differences between participant groups, but some patterns automatedservicebyyourself;(3)stopbeforethesystemasksforyour
foundbetweengroupswereobservedandwillbereportedinthefinding finaldecisionandkeepinmindwhetheryouwanttouseitornotinthe
section. futureandifyouwanttoadoptthefinalrecommendation.
Twoparticipantsperformedthepilottest,and24participantswith Oneresearcherstayedinthelabasamoderatortoofferhelpifthe
stableincomesbyconveniencesamplingjoinedtheformalusertest.The participanthadanyproblems.Thismoderatordidnotinteractwiththe
participantsinthisstudyhaveneverusedthekindofautomatedadvisory participantduringthetaskperformancepartofthetesttosimulatethe
serviceinvestigatedinthisstudybefore.Allparticipantshavestablein- automatedself-serviceprocessandencourageparticipantstofinishthe
comes(MED.¼€300to€400permonth).Theparticipantseitherhad servicethemselves.However,iftheparticipanthadproblemsthatpre-
experience with the financial investment before or were interested in ventedthemfromproceedingwiththetest,thisresearcherwouldoffer
trying this service to see the possibility of financial investment in the someassistanceregardingoperationstoensurethatthetestcouldpro-
future.Accordingtotheirself-reportedfinancialknowledgeandexperi- ceed.Thishelpsparticipantstocompletetheadvisoryprocesstohavea
ence,theyweredividedintotwogroups:non-expertcustomers(P2,P3, holisticunderstandingoftheRAservice,startingfromtheonboarding
P5,P6,P8,P10,P12,P13,P14,P16,P18,P19)andexpertcustomers(P1, experienceuntilthefinalrecommendedportfolio.
P4,P7,P9,P11,P15,P17,P20,P22,P23,P24).Thedivisionintotwo
groupswasnotmadetorigorouslycomparethegroupsbuttoidentify 3.3.2. Post-testinterview
patternswithindifferentgroupsbyanalyzingthescreenrecordings.The Thefirstauthorconstructedthefirstdraftoftheinterviewprotocol;
professionsofparticipantsvariedfromresearchers(includingPhDstu- then,itwasreviewedbytheco-authorsspecializinginsocio-roboticsand
dents), engineers, data analysts, administrators, physicians, librarians, financialservices.Sometextswerereworded,andafewquestionswere
etc. added.Thefinalinterviewprotocolcontainsalistofquestionsencom-
passingthreeparts.Thefirstpartconcernsparticipants’priorinvestment
3.2. Designoftheusertest channelsandhowtheydifferfromtheRAtheyexperiencedinthetest.In
this part, a semi-structured interview method was used. In the second
Inspiredbytheretrospectivethink-aloudapproach(vandenHaak,De retrospective interview part, the questions focused on participants’
Jong, & Jan Schellens, 2003), a combination of that method and a experiencewhenusingandinteractingwiththeRA.Here,theresearcher
semi-structuredpost-testinterviewmethodwasusedinthisstudy.Thisis re-played the video recording and asked participants for feedback
aretrospectivepost-testinterview.Participantswerenotaskedto“think regardingeachstepandtheoverallprocess.Forexample,anyproblems
aloud”duringthetestbuttalkedabouttheirperformanceandintentions they encountered when using it, their expectations of the system, and
4

| H.Zhuetal. |     |     |     |     |     |     |     |     |     | DataandInformationManagement7(2023)100041 |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
unmet needs. In the third part, questions were asked about what par- therestoftheinterviewswerecodedbyoneoftheauthors.Thisauthor
ticipantsthoughtaboutthefinalrecommendationthatwascustomized added codes inductively if new themes emerged in the following 20
according to their input. In the fourth part, participants were asked interview transcriptions. The three authors synthesized and discussed
whethertheythoughtavirtualclientserviceorchatbotismorehelpful thesecodesandannotationsbasedontranscriptions.
andsupportiveinthistypeofproductcomparedtoahumanadvisor. In parallel with the interview transcription analysis, the video re-
|     |     |     |     |     |     |     | cordings | were used | as supportive |     | data material |     | when participants |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | --- | ------------- | --- | ----------------- | --- |
retrospectivelydiscussedtheirbehaviorsandintentionswheninteracting
3.4. Apparatus
withtheRA.Also,eachstepofparticipants’interactiondatawiththeRA
systemwastranscribedintoanExcelspreadsheet.Thesedataincluded
3.4.1. Testhardwareandsoftware eachparticipant’sbuttons,scrollingpages,documentsbeingreviewed,
In terms of the test hardware, researchers pre-installed the RA filling “detailed
|     |     |     |     |     |     |     | and information |     | in. For | example, | they | checked |     | infor- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | -------- | ---- | ------- | --- | ------ |
applicationinatestsmartphone(iPhone6sPlus).Andthesoftwareisa
|     |     |     |     |     |     |     | mation” | of recommended | funds/stocks, |     | opened | additional |     | documents |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ------------- | --- | ------ | ---------- | --- | --------- |
selectedRAbyaretailbank.
|                   |                   |            |               |       |            |            | such as “factsheet”, |                  | reviewed         | “detailed      | cost”,       | and     | their input  | number |
| ----------------- | ----------------- | ---------- | ------------- | ----- | ---------- | ---------- | -------------------- | ---------------- | ---------------- | -------------- | ------------ | ------- | ------------ | ------ |
| The RA            | selected for      | this study | was developed |       | by a bank, | one of     |                      |                  |                  |                |              |         |              |        |
|                   |                   |            |               |       |            |            | indicating           | their investment | willingness.     |                | This         | aims to | determineif  | par-   |
| Sweden’s          | largest financial | groups.    | The selected  | RA    | is also    | one of the |                      |                  |                  |                |              |         |              |        |
|                   |                   |            |               |       |            |            | ticipants            | trust the        | AI-empowered     | recommendation |              |         | by comparing | the    |
| earliest launched | automated         | financial  | services,     | among | other      | similar    |                      |                  |                  |                |              |         |              |        |
|                   |                   |            |               |       |            |            | suggestedamount      |                  | of moneyandtheir |                | actualinput. |         | This datacan | also   |
products.UsingaRAserviceprovidedbyabigbankcanhelptorecruit
|              |             |     |                        |     |     |           | reveal potential | differences |     | in patterns | between |     | participants | with |
| ------------ | ----------- | --- | ---------------------- | --- | --- | --------- | ---------------- | ----------- | --- | ----------- | ------- | --- | ------------ | ---- |
| participants | much easier | due | to its trustworthiness |     | and | authority |                  |             |     |             |         |     |              |      |
financial
perceivedbyinvestors,andtestingamatureapplicationwithaccurate different levels of investment experience or understanding,
technological support can help to reduce the consumers’ uncertainty namely,theexpertandnon-expertcustomers.
Becausetenparticipantswerenotproficientwiththelanguageused
causedbyinaccuratealgorithmsthatmightaffecttheusers’perception
intheRA,anautomatedtranslation(i.e.,GoogleTranslate)toolwasused
andtrustoftheRAs.
|     |     |     |     |     |     |     | to help | them perform | the | tasks. The | translation |     | accuracy | was also |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------- | ----------- | --- | -------- | -------- |
ThesystemdesignofmostRAsonthemobileendisrathersimpleand
linear(seeFig.1).TheselectedRAhasthesameusageflow.Userscan checked by bilingual participants, proving to work well for conveying
|          |                 |        |            |          |           |        | textual information. |     | Due to | the time | lag for | auto-translation, |     | the time |
| -------- | --------------- | ------ | ---------- | -------- | --------- | ------ | -------------------- | --- | ------ | -------- | ------- | ----------------- | --- | -------- |
| navigate | by pressing the | “back” | and “next” | buttons, | scrolling | up and |                      |     |        |          |         |                   |     |          |
theyspentwasnotaccountedforinthedataanalysis.
| down to | view the interface, | inputting | numbers | and | sliding | the bar to |     |     |     |     |     |     |     |     |
| ------- | ------------------- | --------- | ------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thedatafrompilottests(N¼2)wereexcludedfromtheanalysis.
changenumberswheninteractingwithdatavisualizations.Additionally,
Thus,thedataof24participants(14females,10males;medianage¼
supplementarydocuments,suchasfactsheetsoffinancialproducts,risk
31.5years)werebroughtintotheanalysisphase.
disclosure,andpurchaseagreement,canbereviewedasattachmentsby
pressingtheicon,whichdirectsuserstoaPDFdocument.
|     |     |     |     |     |     |     | 4. Resultsandfindings |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
3.4.2. Documentation
Thissectionshowsthattheparticipants’perceptionofRAdoesnot
EachinterviewaudiowasrecordedonaniPadforfuturetranscription
matchtheirexpectations.Non-transparencyandinsufficientinformation
| and analysis. | An iOS video | recording | software | was | used to | record the |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --------- | -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
participants’interactionwiththeinterfaceduringtheusertest.Dueto about the systemmakeit difficult for participants to adopt the results
|     |     |     |     |     |     |     | generated | by RA. | However, | data visualization |     | showed | its | promise to |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | ------------------ | --- | ------ | --- | ---------- |
ethicalconsiderations,participantswereaskedtouseanunidentifiedtest
|     |     |     |     |     |     |     | convey comprehensible |     | information |     | to participants. |     | The findings | are |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ----------- | --- | ---------------- | --- | ------------ | --- |
accounttologintotheRAsystem,butthefinalrecommendedportfolio
was based on their inputting data. Their information would not be synthesizedfrominterviewtranscriptionsandvideorecordinganalysis.
identifiedbythebank,andresearcherserasedtheirinputsmanuallyafter
eachtest.
|     |     |     |     |     |     |     | 4.1. TheperceivedsocialroleofRAslagsbehindtheparticipants’ |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
expectation
3.5. Datacollectionandanalysis
|     |     |     |     |     |     |     | 4.1.1. ParticipantsdonotthinktheygetadvicewhenusingtheRA |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
This study collected three types of data: pre-survey data, a video Asmentionedbefore,RAsaredevelopedandimplementedbyservice
recordingoftheinteractionwiththeRA(AVG.¼19.8min),anaudio
providerstopartiallyreplacehuman-resourcecosts.RAsalsopromiseto
¼
recording of post-interview (AVG. 30 min), and a retrospective providethesamequalityofhuman-advisoryservicetocustomerswith
descriptionisincludedinthepost-interview.Theinterviewrecordings relativelylowserviceandtransactionfees.However,participantsdidnot
recognizethattheywereprovidedprofessionaladvicesuchasfinancial
weretranscribedintotextandwereimportedintothesoftwareNVivofor
analysis. The coding is analyzed inductively by finding themes with planning or wealth management. On the contrary, they felt forced to
similar meanings. Three authors coded four interviews in parallel to completethepurchaseofcertainfinancialproductsfromthebank.The
validate the coding items and make the coding consistent within our RAwasperceivedasasales-centricservicebythebank.P20:“…thebank
researchgroup.Afterthediscussion,theinitialcodingmetrics(anexcel wants to make a product that is easy for selling and make it easy for
sheetwithcodes,sub-codes,andtheirdefinition)wereconfirmed,and peopletoclickthecontractthattheywantmetosign.”;P18:“Iwasforced
|     |     |     | Fig.1. | TheusageflowofgeneralRAsystemsbasedonNueeschetal.(2014). |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5

H.Zhuetal. DataandInformationManagement7(2023)100041
intoafund.”;P7:“Theydonotrecommendmeanything,andthisishow because they had not had any good experience talking with virtual
theymakemoney.”Onlytwo(P15&P8)saidtheygotsuggestionsand customer services (P4, P6, P9; P26); based on their understanding of
advicewhenusingtheRA.Forexample,P5:“RAhelpedmeunderstand currenttechnology,theythoughtthatchatbotscouldonlyanswercertain
whattoconsiderwhenplanningmyinvestmentbyansweringdifferent questions,andtheypreferredcheckingFAQbythemselves(P18,P24).
questions”. The reasons why participants do not perceive that the RA Mostimportantly,P5andP17thoughtthatitdidnotmatterifhumansor
givesthemadvicearetwo-fold.First,thematchingphase,inwhichal- robotsprovidedtheservice;whattheycaredaboutwasthattheservice
gorithmsruncomplexcalculations,isnottransparent.Afteranswering wasperformedprofessionallyandrigorouslyandcouldbeperceivedas
theconfigurationquestions,participantsareshowndirectlytothefinal trustworthy.
recommendation, and they are not informed about the process and Participants thought this automated service could be “pre-stage”
criteriaforpickingupthesefinancialproductsastheirportfolios.Second, beforetheywentforhumancounselingbecausetheystillneededguid-
there is no opportunity for the participants to askquestionsaboutthe anceandtutorialfromahumanadvisor(P13).P16thoughtaprofessional
finalrecommendations;theymustinterpretandunderstandtheportfolio human could help to mitigate “the risk of miscommunication”, which
bythemselves.Therefore,theparticipantsdonotperceivethattheRA might be caused by their misinterpreting the configuration questions
givesadvice.Instead,itbarelysellscustomersfinancialproducts. fromthesystem.Besides,P24preferredto“haveacombinationbetween
some person you can talk to and this automatic service” because he
4.1.2. Participantsdonotthinktheyareinteractingwitha“robot.” thoughtthattalkingtosomeonecouldmakebanks“knowmoreaboutmy
In the post-test interview, participants reported that they did not economy,mygoalsandhowIshouldactwhenIneedaninvestmentor
thinktheRAhadany“robotic”features,andparticipantsdidnoteven loan”. P17 proposed that the bank should set a threshold for when a
perceivesome significantfeatures.Theexpectationstheygot fromthe humanadvisormustdothefinalreview:“Forbiginvestmentsthatexceed
name “Robo-” and the introductory information about the RA service acertainamountofmoney,ahumanadvisormustgetinvolved”because
shownontheonboardingpagesdidnotmatchtheirexperiencewiththe “investmentcanbeabigdecision,Icannotgivemymoneytosomething
system when using it. For example, some thought the service was a basedonafewclicks.”ButP17alsosaidshemighttrythisserviceby
simplematchingsystem:“verylittlerobotic(…)asimplerecommenda- starting with a small amount of money. Thus, human involvement is
tion system (P20)”; it “just tries to match my profile with existing expectedbyparticipantsfordifferentreasons,butmainlyforcalibration
products(P21)”.Participantsthoughtitwasnotintelligentbecauseofthe of the possible “miscommunication” and more personalized advisory
lack of conversational interactions like one expert with a customer: “I suggestions.
couldnottalkto,wouldn’tsaymoretotherobots(P21)”;“thequestions
itaskedmeareverystandardized,Idon’tthinkitismyadvisor.Iwould
likemyadvisortoshowmoreprofessionalismthanthis(P17).” 4.2. Non-transparencyisthemainconcernfordecisionmaking
Participantsalsothoughttheservicewas“notintelligent”becauseit
juststoppedanddidnotgiveanyinformationtohelpusersrecoverfrom Non-transparencyindicatestheinformationrequiredbyparticipants
errors when they input unexpected or contradictory answers to the that they do not think they get when using the system. This includes
questionsintheriskassessmentphase.Threeparticipants(P3,P11,P13) undisclosed information by the service and disclosed information but
selected contradictory options when answering risk-related questions unperceivedbytheparticipantwhenusingtheservice.Non-transparency
accordingtotheanalysisofvideorecordings.Aspertheregulationsin mainlyexistsintwostages:riskassessmentandfinalrecommendation.
financialservices, customers must correctly answerthese questionsby
themselvesbeforetheyareallowedtoproceedtothenextstep.Thus,RA 4.2.1. Non-transparencyproblemsinconfigurationquestions
systems cannot tell customers the correct one. However, in this test, In the configuration phase, RAs are supposed to “understand” cus-
participantswerestoppedfromusingthesystem.Whenthis“contradic- tomersregardingtheirpersonalpreferences,financialsituation,andrisk
tory”wasdetected,theservicejust“gaveup”andaskedparticipantsto appetitesbasedonsurveysandanswersfilledbyparticipants.Thisphase
call the bank’s customer service. This unsatisfactory experience made isfundamentalbecauseitnotonlygetsnecessaryinputsfromcustomers
participantsfeelthatthesystemwasnotadvanced.P13:“It(is)notthe forthesystemtomakecomplexcomputing;italsohelpscustomersun-
way thathumans talkabout finance.(…) Itis unintelligent becauseit derstand which factors construct the final decision (i.e., investment
couldhavedynamicallytoldmewhichanswersareinconsistent.”P3:“I portfolio)madebythisexpertsystem.However,asthereasoningprocess
don’tknowwhereIamwrong,andIdon’tknowhowtofixit.”P11went is not adequately revealed, participants know neither the differences
backtothepreviousstageanddidtheriskassessmentagaintoproceed betweeneachoption,inparticular,“high”,“minor”,and“intermediate”,
withthisserviceandsaid,“Inreallife,Iwillquittheservice,andIwill nor where these answers will lead them to. This is not a survey that
not call them.” This unpleasantexperiencealso madeparticipants feel recommendsanyTVprogrambutwillleadtoahigh-stakedecisionon
ashamedandcauseddissatisfaction.P13thoughtthesystemblamedhim: theirrealmoney.
“IttoldmethatIdidsomethingwrong”.
Moreover,thefeaturesregardingautomatedmaintenanceandreba- 4.2.1.1. Participants want to know the logic behind the profiling ques-
lancingofinvestmentwerenotperceivedbyparticipants,eventhough tions. Thereasoningbehindconfigurationquestionsandprofilingstra-
this information was shown on the introductionwebpage. It might be tegiesisunknowntoparticipants.Intheconfigurationphase,customers
that the participants did not pay attention to the after-sale service are required to provide information, so they will be categorized into
because the test moderator asked them to terminate the test session differentgroupsbasedontheriskassessmentandothercustomizedin-
beforetheyhadtoperformtherealpurchaseactions.However,afterthe formation,namely,overallsavings,theincomeleftaftertheircompul-
researcher explained to participants that the system would perform sory monthly expenditure, loan, mortgage, etc. The standardized
automated maintenance and rebalancing after the investment, most questions for categorizing the customers into risk-appetite groups are
participants said that they had not recognized this function of the RA usually multiple-choice questions. Human advisors will help interpret
whenusingthesystem. and explain these questions and options and check for accuracy by
regularly examining if customers understand them. In this user test,
4.1.3. Participantsdonotthinkasocialrobotcansolvetheirproblemsbut participants were much more aware and cautious of the logic behind
expectmorehumanintervention these questions because they understood that these questions were to
Intheinterview,participantswereaskediftheythoughtthatavirtual profileandmatchthemwiththeappropriatefinancialrecommendation.
customerservicerobotorchatbotwouldbeabletogivemoresupport Thus, many participants were concerned about the issue of non-
comparedtowhattheRAdidthattheyjustused.Almostallansweredno transparencybecausetheyaskedwhytheRAaskedthesequestionsbut
6

H.Zhuetal. DataandInformationManagement7(2023)100041
excluded some other questions that participants thought were more and “adopted” to their needs; however, participants did not perceive
relevanttotheirfinancialplanning(P16&P18).Participantswereun- those features. P18: “I do not understand what kind of models or
sure how their answers resulted in the final recommendation in this mechanismtherecommendationisbasedon.”
systemandtowhatextentthedifferentanswerswouldresultindifferent Theparticipantswereawarethattheywerecategorizedintodifferent
investment portfolios. P7: “If I chose a bigger number. Would they riskgroups,andtheywouldliketoknowthefinalrecommendationin
recommendsomethingdifferent?”.Thereasoningthatmatchespartici- othergroups,eventhoughtheparticipantsdidnotexplicitlyexplainthe
pants’ answers to the risk-appetite groups remains unknown and un- reasons for this requirement. P20: “why cannot I review all (plans)
published. Is it just a risk assessment the same as a human-advisory choicesattheendoftheprocess?AndthatisalsoafactorwhereIwould
service, or does the algorithm play any role here? No explanation is losetrustinthisservice.”P17:“Iknowtheymighthavesevengroupsin
offered. total.Iwasclassifiedintofive;Iwanttoseewhattheproductsinother
groupsare.”P5makesananalogywithpersonalitytests:“Thiscouldbe,
4.2.1.2. Participantshavedifficultyanduncertaintywhenansweringques- okay,our(banks’)optionsarethisandthis,justlikethepersonalitytest,
tions. Withoutguidanceorreference,itwasdifficultforparticipantsto youknow.Thenyoucanseeotherpeople(’sdistribution)aswell.”This
accuratelyinterpretorcomprehendeachquestionanditscorresponding findingisinlinewithpreviousworkregardingAI’suseinthemedical
options.Thisuncertaintycausesdistrustoftheresultsgeneratedbythose domain(Aoki,2021);humansshowmoretrustinAI’sdecisionsifthey
inputs.Whenansweringmultiple-choicequestions,participantsfeltun- feelthattheyarestillinvolvedinthedecision-makingbycommunicating
certainwhenhavingtointerpretdifferentoptionsandselectonebecause withtheautomatedsystem.Thistypeof“communication”islackingin
of vague terminologies such as “minor”, “intermediate”, and “high”. RAservice.
Especially when they were asked questions regarding risk preference.
Most importantly, they were concerned about whether an inaccurate 4.2.2.2. More transparent managerial strategies are needed regarding the
answerorinputwouldleadtoarecommendationthatdidnotfitthem. components of the recommended portfolio. Participants tended to show
Participantsaskedformorecomprehensibleandconcretedefinitions.P5: moreconsciousnessastheyrequestedmoredetailedinformationabout
“Itisunclearwhatisa‘high’riskherebecauseitissubjectivefordifferent thecompaniesofbondsandsecurities,whichwereabouttheinvestment
people. It should also define that.” P3: “They didn’t give me concrete targetsintheportfolios.P13:“So22%oftheinvestmentwillgointothe
numbersorquantifieditinagoodway.Howmuchmoneyisminor?1000 ITsector,and13%herewillgointothehealth(industry),butitdoesn’t
out of 10,000? Or 1 out of 10,000? I am afraid people have different show me what’s the company?” Those participants who selected “sus-
understandingsabout‘minor’.” tainablepreference”weremoreethicallyconcernedinvestors,andthey
Thislackoftransparencyattheearlystagesunsatisfiedparticipants thoughtitwasimportantfortheirdecision-makingtoknowthecriteria
and distrusted the results based on incorrect inputs. The relationship for screening sustainable investments and what companies the bank
betweenthecustomerandtheservicethattheparticipantsexpectedwas wouldinvestin.P12:“I’msurprisedit’s(sustainable)going;themajority
perceivedtobebroken.Participantswereskepticalabouthowvalidthe isgoingtoIT.Ididn’texpectthat.Like,Ithoughtitwouldgomoreto-
finalrecommendationwasifitwascompletelybasedonhowwellthey wardsenergyandsustainableenergies.”P21:“BecauseifI’manethical
understoodthequestions,whichmightnothavebeenaccurateenough. investor,Iwantthatinformationtobetransparent.IfIknowwhatthey
P5:“Whenanswering,Ijustselectonewithfeeling.Somyanswerisnot are,Icantrackthecompaniesandseewhattheyaredoing.”
thatvalid.(…)IcannottrusttheresultifIcannotprovidesolidinfor-
mation that I know exactly what I want.” P12: “Because when I put 4.2.3. Someinformationistransparentbutnoteasilynavigated
mediumrisks,Iwasunsurebetweenthelowandthemedium.”P3:“IfI In financial service encounters, information disclosure is strictly
adoptaproduct(portfolio)thatdoesn’tsuitmebecauseIdidn’tunder- regulatedbylaw.Customerscancasuallyaskquestionstheymostcare
stand the survey question correctly, I might bear more risk.” This un- about to human advisors, and customers get informed in this
certaintyanddistrustcausedbythenon-transparencyattheveryearly conversational-based process. However, when interacting with RAs,
stagewillpersistthroughouttheuserexperienceandaffectthefollowing participants should be more self-reliant. Even though the system dis-
interactions. closesenoughinformation,somearedeeplyhidden.Forinstance,some
PDFdocumentsarenotintegratedwiththeuserinterfacebutrequests
4.2.2. Transparencyproblemsinthefinalrecommendedportfolio customersto clickanewwebpage.Customersarerequestedtohavea
Afterconfiguration,thealgorithmwillautomaticallymatchthecus- high capability to search for information and actively navigate them-
tomer’sprofiletoacertaingroupandshowthemthefinalrecommen- selves,whichisoverwhelmingandimpossibleforthosenon-expertusers.
dation,whichisusuallyaportfolioofETFs(exchange-tradedfunds)that According to our observations of video recordings, expert participants
is a basket of investments such as assets, stocks, bonds, etc. This is a caneasilynavigateinformationtohelpunderstandtheperformanceof
passive investment and is not fully transparent because the manager’s therecommendedportfolioortheserviceterms.Forexample,P4,P20,
tradingstrategiesarenormallyunpublished.However,inthetest,most and P26 actively open documents such as fact sheets to review past
RAparticipantswereunawareoftheportfolioandhowETFsworkinthe performanceandratingsabouteachspecificportfoliocomponent.
financialmarket.BasedontheinformationprovidedbyRA,participants’ In the interviews, participants were concerned that they were not
confusionistwofolds:lackofinformationaboutthemechanisminthe informedaboutthemaintenanceandquittingtermsiftheywouldinvest
systemthatcreatesthesuggestedportfolio;andthelackofinformation money using this system. Specifically, after being informed that the
thattheythinkisnecessaryfortheirdecision-making. system would automatically rebalance their portfolio, participants
wonderedhowmuchinformationwouldbereconciledwiththem;and
4.2.2.1. Lackoftransparencyoftherecommendationsystemmechanism. - when theywould get a notification that therewould be anauto reba-
Afterreviewingtherecommendedportfolio,mostparticipantsaskedfor lancing.P13:“TheservicecontractthatIsignedtodaymightnotinclude
theresult’ssourceandprinciples.Thisnon-transparencyrevolvesaround the algorithm to be dynamically changed in the future. And these
theAI-empoweredalgorithmanditsmechanismforadvisingcustomers changes are not published nor public.” P9: “I don’t know if I will be
ontheoptimalandpersonalizedportfolio.P9:“Idon’tknowhowand regularlypushedorupdatedwithchangesaftermyinvestment,suchas
whatthecriteriaareforpickingupthestocksforme.”P10:“Iwantto thetrend,growth,orloss.ButnowIdon’tknowanddon’tgetanyin-
knowmorespecificallywherethesenumberssuggestmymonthlydeposit formationifIcanreceivethesenotifications.Iwanttofollowandtrack
comes from.” This lack of transparency negatively affects participants' myinvestment.”Participantswerealsoconcernedabouthowmuchthey
trustastheserviceclaimsthattherecommendationis“tailored”forthem wouldloseiftheydroppedoutearlierthantheagreedplan(e.g.,P8&
7

H.Zhuetal. DataandInformationManagement7(2023)100041
P11). Some noticed a text saying customers can take their investment everyday finance and any long- or short-term plans in an individual’s
back whenever they want. But they thought the information here real-life scenarios, for instance, pensions (P21), buying a car or an
remainedsimpleandunclear(e.g.,P6).ParticipantsexpectedtheRAcan apartment(P8),orotherplansinthefuture.P21thoughttheRAskipped
prioritized information as their importance, in particular, the possible importantquestionsaboutcustomers’horizonsandintentionsforsaving
costsandservicefees,becausecustomersoffinancialservicesindeedcare andinvesting.Thisalsomakesthemfeelthattheadvisorisnotperson-
aboutandaresensitivetothem. alizedastheyseefromtheintroductionpage,andthisunmetexpectation
negativelyaffectstheirexperience.
4.3. Insufficientinformationandthelackofdomainknowledgefor
adoptingRA’sresults 4.3.3. Datavisualizationisperceivedasaneffectivetooltoconvey
comprehensibleinformation
Insufficientinformationisthesecondissuethathindersparticipants’ Intheinterview,mostparticipantsgavepositivefeedbackintermsof
the interactive data visualization in the RA. Data visualization in-
adoption. Generally, non-expert customers with limited investment
experienceorfinancialunderstandingneedexpertsystemslike RAsto struments show great potential in three aspects: visualizing financial
make financial decisions. In the interview, when asked, “would you understanding(especiallyriskassessment),interpretingtheperformance
adopttherecommendationoruseRAsinthefuture”mostparticipants oftherecommendedportfolio,andenvisioninggrowthandloss.
IntheselectedRA,twotypesofdatavisualizationsareutilized.One
wereuncertainandcouldnotmakedecisionsbasedontheirexperience
withRAs.Onlyfourgavecertainanswerslike“yes”(P1&P14)and“no” visualizesriskassessmentbyshowingconcretenumbersindiscrimina-
(P20&P24)afterthetestsession.Moreover,whenbeingasked“ifyou tivevisualcues(i.e.,twocolors)(Fig.2).Theothervisualizationpresents
want to use and try it several times and then make decisions”, expert more information and interactive parameters by which customers can
participantsweremoreconfidentregardingtheirfirsttrialandbelieved envisionthegrowthandlossofthemoneytheyplantoinvestinone-time
ormonthlydeposits(Fig.2).
thattheresultwouldbethesameiftheytriedthewholeprocedureagain
Comparedwiththevagueterminologyintheoptionsuchas“low”,
(e.g.,P4,P9,P17,P20,P24).Atthesametime,non-expertparticipants
“middle”,and“high”inriskassessmentmentionedbeforeinthispaper,
showedmoreuncertaintyanddistrustofthedecisionmadebythesys-
thedatavisualization(Fig.2Leftpanel)isclaimedtobe“moreconcrete
tem.Non-expertsneedmoreguidanceinprovidingaccesstoinformation
(P12)”and“muchmoretangible(P5)”inhelpingparticipantsunderstand
thatistransparentbutalsoexplanativeandunderstandableforthem.
risk,eventhoughsomedesignproblemsexist(e.g.,mostparticipantsdid
notrealizethebottomroundbuttonisinteractable).Allparticipantssaid
4.3.1. Non-expertparticipantsrequiremoreunderstandableinformationto
thattheinteractivelinediagram(Fig.2Rightpanel)providedsufficient
supporttheiradoptiondecision
informationfor themto understand the performanceof theirportfolio
Participants said they needed more information to understand the
finalrecommendationandtosupporttheirdecision-making.Theinfor- andhowthepossiblegrowthandlossoftheirmoneycouldchangeover
time.First,theinteractivelinediagramisself-explanatoryandcompre-
mationistwo-fold:informationdisclosureregardingtheRAservice;and
financial understanding, which is basic domain knowledge to support hensible for participants without much knowledge about this type of
service.P10:“itcanprovidemetheestimationofthelowestandhighest
interpretations and comprehensions of those disclosures. Differences
(…)Itcangiveyouageneralconception,liketherate,percentage.ThenI
exist between expert and non-expert participants. The latter felt over-
knowthehighestmoneylossIcanbear,concretelyandpractically.”P21:
whelmed when so much information appeared at the last stage. Even
though some can find these documents, it was still hard for them to “This (Fig. 2 Right panel) is more comprehensible regarding the time
understandthecontent,includingfinancialtermsandnumbers,notto horizon and related risk”. From the video analysis, every participant
interacted with the tool by inputting different variables in Fig. 2. P4
mentionhowtoutilizethisinformationtosupporttheirdecision-making.
Generally,non-expertparticipantsexpecttolearnbasicfinancialmarket thoughttheinputintimehorizonhelpedtoassociateriskwiththecon-
creteamountofmoney,makingtheriskmoreunderstandable.
andinvestmentknowledgethroughwordstheycaneasilycomprehend.
P10:“Iopenthe factsheetandrealize;Idon’tunderstandtheterms.”
P12:“Iexpecteditcouldtellmewhatthestockmarketislike,suchasthe 4.4. Anuntransparentsystemandincomprehensibleinformation:where
currentindexofthewholestockmarket.Ihopethatsomeonecanguide thedistrustcomesfrom
mewithmorebasicinformation.”P6:“Theyshouldhaveagoodeditorto
createunderstandabletexts.Ortheyhavelinkstosomeknowledgewhere Participants showed distrust and suspicion of the result if the RA
Icouldlearnmore.”Inshort,extraguidanceinthesystemisexpectedto systemwasnottransparentorincomprehensibletothem.Accordingto
reach three aims: (1) to help customers navigate the informationthey theinterviews,participants’decisiontoadopttheRAwasaffectedbythe
need;(2)toguidethemtounderstandthisinformation,and(3)totell systemandotherfactors,suchasunsatisfiedfeesandinitialintentionof
themwhicharethemostimportantcriteriaforevaluatingandpredicting usingRA.However,forbothexpertandnon-expertparticipants,trans-
theperformance,ofafundforexample. parencyandsufficientcomprehensibleinformationarecrucialfortheir
willingnesstouseRAornot.Besides,itisworthnotingthatmostpar-
4.3.2. ParticipantsexpectRAstohaveaholisticunderstandingoftheir ticipants distrust the system from their interviews and the screen
personalinformation recording.Afterreviewingthefinalrecommendedportfolio,participants
ParticipantswereskepticalthattheRAcouldprovideaholisticand wereaskedtoinputtheirinvestmentplantofinishthetaskperformance.
personalized portfolio based on the limited information currently Inthevideorecordings,mostparticipantsdidnotfollowtheRA’ssug-
collectedfromthemthroughthesystem.Theyalsoexpectedtospenda gested amount of money. Only four (P6, P7, P11, P18) inputs exactly
longtimeusingthisserviceratherthangettingaplanwithinafewmi- matchedtheamountofmoneytheRAsuggested.Thiscanbeinterpreted
nutes. P17: “Before using (the RA), I thought it would ask me more asparticipantsnottakingtheRA’ssuggestionastheirbestfit,thusrep-
questionsthatallowmetoseethevalueofthisservice.Thesequestions resenting distrust of the risk grouping and the mechanism behind the
aresostandardizedIdon’tthinktheycangivemegoodsuggestionsonan recommendedportfolio.Mostparticipantsshowedthattheytrustedthe
individuallevel.Idoubtit.”P7:“Itisashort(thetime),honestly.Itcanbe bankandthetechnology,beingconfidentthattherewouldbenofraud.
morepatientwithme.It’sabigdecision.It’snotsomethingIwouldlike However,theirexperienceofthewholesystemmakesitdifficulttotrust
tohavedonein3min” the result(P3,P5,P6, P7,P12,P13, P21).Accordingto theinterview
Thus,someparticipantswouldlikethatthesystemcouldunderstand data,thisdistrustnegativelyaffectsparticipants’willingnesstoadoptthe
more about users by asking more personalized questions such as advicegeneratedbytheRA.
8

| H.Zhuetal. |     |     |     |     |     |     |     |     |     |     |     | DataandInformationManagement7(2023)100041 |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- |
Fig.2. Leftpanel:Thedatavisualizationintheriskassessmentphase.Rightpanel:theinteractivediagramintherecommendationportfolio.Thesearenottheoriginal
interfacesfortranslation,butthecontentsarethesame.
5. Discussion intentioniscomplex,especiallywhenAImeetswithfinancialdecisions.
Thisinterdisciplinarypaperbridgesthepreviousfragmentedstudiesin
|     |     |     |     |     |     |     |     |     |     | fields | Casalo(cid:2), | & Flavi(cid:2)an, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | ----------------- | --- | --- | --- |
Thisholisticuser-centeredstudyofafunctionalretailbankRAaimsto different (Belanche, 2019; Ben David et al.,
|            |     |     |              |     |        |            | customers’ |     | 2021;Ben-David&Sade,2020;Chengetal.,2019;Ganetal.,2021;Shin, |     |     |     |     |     |     |
| ---------- | --- | --- | ------------ | --- | ------ | ---------- | ---------- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| understand | how | the | AI-empowered |     | system | can impact |            |     |                                                              |     |     |     |     |     |     |
2021a;Wu&Gao,2021),bycompensatingforthelackofcustomers’real
| perception | and | adoption. | Methodologically, |     |     | the approach | of  | asking |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ----------------- | --- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
customerstouseafunctionalRAcompensatedforthepreviousempirical useofafunctionalRAinpreviousstudies.
| studies | by simply | conducting |     | surveys | without | considering | customers’ |     |     |     |     |     |     |     |     |
| ------- | --------- | ---------- | --- | ------- | ------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
experienceofinteractingwithaRAinreal-lifesituations.Theoretically, 5.1.1. Transparencyissuesrunningthroughthewholesystem
thisstudyextendstheknowledgeofRAperceptionandadoptionresearch Transparency has long been an issue in financial advisory services
by articulating the negative effects of the lack of transparency and (Kilic et al., 2015; Nueesch et al., 2014, 2016; Nussbaumer & Matter,
comprehensibilityinaRAsystem.Inparticular,thispaperclaimsthat 2011)andAI-empoweredcustomerexperiencedesign(BenDavidetal.,
non-expertcustomersrequestmorecomprehensibledomainknowledge 2021;Shin,2021a).Thisempiricalstudyalsorevealeddifferent trans-
financial
to use and adopt RAs. Besides, the perception of RA lags behind both parency issues embodied in AI-empowered advisory and sys-
customers’ providers’ tems.Customersinfinancialserviceencountersaremoreawareofissues
|     | expectations |     | and the | service |     | ambitions. |     | Overall, |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------- | ------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
thesignificanceandtheroleofRA’ssystemdesignhavebeenleveredup,
|     |     |     |     |     |     |     |     |     | because the | investment | decision | is high-stake |     | compared | with other |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | ------------- | --- | -------- | ---------- |
andsomedesigntakeaways,currentlimitations,andfutureworkarealso AI-empowered services. This study articulates these issues, and it in-
discussed. dicatesthattransparencyshouldbeaprinciplethatrunsthroughevery
detailofaRAsystemrangingfromthetextsontheintroductorypage,the
|     |     |     |     |     |     |     |     |     | reasoning | behind | survey questions | and | options, | the mechanism | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---------------- | --- | -------- | ------------- | ------ |
5.1. AtransparentandcomprehensibleAI-empoweredsystemissignificant
|     |     |     |     |     |     |     |     |     | recommended | portfolio, | the performance |     | and components |     | of financial |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------------- | --- | -------------- | --- | ------------ |
forRAperceptionandadoption
products,theservicefees,totheservice-relatedterms,suchastermina-
tion.CustomersusingRAaremorerationalthanthoselayinvestorsin
| In  | the context | of  | financial | investment, | transparency |     | and | compre- |     |     |     |     |     |     |     |
| --- | ----------- | --- | --------- | ----------- | ------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
conventionalfinancialserviceswiththepopularizationofAI-empowered
| hensibility | are | important | because | the | investment | decision | is relatively |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ------- | --- | ---------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
high-stake,andinvestorsare“vulnerablecustomers”(Beltramini,2018; technologyand its wide use.They would like to makemoreinformed
decisionseventhoughtheytrusttheserviceprovidersandthetechnol-
Mogajietal.,2021),whichmeanstheirperceptionofRAcanbenega- ogy,namelythealgorithmbehindthesystem.Similartothefindingof
tivelyaffectedbylackoftransparency.Theyarenotresilientortolerant
|     |     |     |     |     |     |     |     |     | previous | internet-bank | research | (Nussbaumer, |     | Matter, | & Schwabe, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | -------- | ------------ | --- | ------- | ---------- |
ofunmetexpectations.Moreover,unlikeotherAIsystems,investmentis
“one-time” 2012),transparencyintheAIeraintensivelyrequeststhesystemnotonly
| not a |     | behavior, | but | a long-term | and | dynamic | process. | The |     |     |     |     |     |     |     |
| ----- | --- | --------- | --- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
providethenecessaryinformation,butalsoprioritizetheimportanceof
| whole    | serviceprovidedby |              | RA  | ranges      | from portfoliodesign |      | andmain-     |     |             |             |              |         |               |              |             |
| -------- | ----------------- | ------------ | --- | ----------- | -------------------- | ---- | ------------ | --- | ----------- | ----------- | ------------ | ------- | ------------- | ------------ | ----------- |
|          |                   |              |     |             |                      |      |              |     | different   | information | and convey   | these   | to customers. | This         | can help to |
| tenance, | whichis           | difficultfor |     | customersto | understand.          |      | Customers    | are |             |             |              |         |               |              |             |
|          |                   |              |     |             |                      |      |              |     | balance the | information | asymmetry    | between | an            | AI-empowered | expert      |
| highly   | dependent         | on written   |     | texts and   | visualized           | data | withouthuman |     |             |             |              |         |               |              |             |
|          |                   |              |     |             |                      |      |              |     | system and  | customers   | in financial | service | encounters.   | Otherwise,   | the         |
interventionwhenusingRAsystems.Thisalsoincreasesthethresholdto
non-transparencywillhampertherelationshipestablishedonthetrust-
| adopt | RA. Thus, | a   | good RA | system | should | be transparent |     | and |     |     |     |     |     |     |     |
| ----- | --------- | --- | ------- | ------ | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comprehensible. worthinessbetweencustomersandserviceproviders.
By extending prior studies in the web-based Fin-tech (Kilic et al., Augmentingfinancialunderstanding:comprehensibletransparency
|     |     |     |     |     |     |     |     | (cid:3)a; | 5.1.2. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- |
2015; Nueesch et al., 2014, 2016; Nussbaumer, Matter, Reto Nuss- Previousresearchshowscustomerswithalowleveloffinanciallit-
baumer&Matter,2011;Nussbaumer,Matter,&Schwabe,2012;Porta,
eracyareinclinedtouseRAs(Brenner&Meyll,2020),andtheyneedan
| et al., | 2012), | the result | has levered | up  | the role | and | importance | of a |              |        |        |               |     |                      |     |
| ------- | ------ | ---------- | ----------- | --- | -------- | --- | ---------- | ---- | ------------ | ------ | ------ | ------------- | --- | -------------------- | --- |
|         |        |            |             |     |          |     |            |      | AI-empowered | expert | system | more urgently | to  | give recommendations |     |
transparentandcomprehensiblesystemperceivedbycustomers,which
thanexpertcustomers.Also,non-expertcustomerswithlittleknowledge
workstogetherwithothermultiplefactorsaffectingcustomers’percep-
|     |     |     |     |     |     |     |     |     | might feel | embarrassed | and anxious |     | when conversing |     | with a human |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | --- | --------------- | --- | ------------ |
tionandadoptionofRAs.Themechanismbehindconsumers’behavioral
9

| H.Zhuetal. |     |     |     |     |     |     |     |     |     |     | DataandInformationManagement7(2023)100041 |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
advisor(Gerrans&Hershey,2017);theautomatedserviceissupposedto TheperceivedperformanceoftheRAinmarketsstudiedinthistest
be a better alternative. However, it was found in this study that most haslaggedbehindthevisionsoftheirdevelopers.Theserviceproviderof
non-expertparticipantsdidnotgetsufficientsupportwhenusingtheRA. theRAinvestigatedinthisstudyclaimsthattheirRAservicedoesnot
First, they cannot navigate themselves through this overwhelmingly compromiseontheservicequalitybutequalsahuman-advisoryservice.
informativesystem.Second,theycannotcorrectlyunderstandfinancial However, most participants do not recognize that they get valuable
terms, and the lack of domain knowledge causes distrust of the adviceorsuggestionsfortheirpersonalizedwealthplanning,whichisan
AI-generatedresult.Thisfindingisinlinewithapriorstudythatclaimed essential part of human-advisory service. Second, customers who are
thatthelackofbasicfinancialknowledgecouldleadtodistrustofthe lowfinancialunderstanding
|     |     |     |     |     |     |     | inexperienced |     | ininvestmentorhavea |     |     |     |     |     | do  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
resultgeneratedbyAI,eventhoughtheyareaccurate(Dikmen&Burns, notgetsufficientinformationorknowledgebyusingtheRAserviceto
2022).Atthesametime,customerswithoutabasicunderstandingofhow support their decision-making. Even worse, these customers felt
thefinancialmarketwouldbeorwhatrisktheywilltakewouldbeputin “blamed”and“abandoned”bythesystemwhentheyinputanswersthat
dangerbyblindlyadoptingRAs’recommendations.Inourstudy,some the algorithm could not compute because these were contradictory to
non-expert customers with a master’s degree had difficulty correctly whatwasacceptedbythesystemconfiguration.
understandingtermslike“interest”andthreeparticipantsselectedcon-
| flict answers | when doing    | the risk   | assessment. |      | Thus, those       | non-expert |      |                                                         |     |     |     |     |     |     |     |
| ------------- | ------------- | ---------- | ----------- | ---- | ----------------- | ---------- | ---- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |               |            |             |      |                   |            | 5.3. | Thedilemmabetweensystemdesignandbusinessimplementation: |     |     |     |     |     |     |     |
| customers     | expected that | RAs should | provide     | them | with transparency |            |      |                                                         |     |     |     |     |     |     |     |
practicaltakeaways
| and understandable | information |     | that could | support | their | financial |     |     |     |     |     |     |     |     |     |
| ------------------ | ----------- | --- | ---------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
decision-making.Inthehumanadvisoryserviceencounter,advisorscan Here we propose takeaways for the practitioners and service pro-
check if the customers understand the questions correctly. Human ad- vidersofRA.Inpractice,theimplementationofRAsisnotsimplyuser-
visorscanalsousedifferentpedagogicaltoolstoaddresscustomers’lack
|     |     |     |     |     |     |     | centered | due | to multiple | stakeholders' |     | involvement, |     | because | RA de- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | ------------- | --- | ------------ | --- | ------- | ------ |
offinancialliteracy,enhancingthecustomers’understandingofpersonal
velopersanddesignsareonlypartofthebusinessstrategies.Inbehav-
financeandtheeffectofdifferentinvestmentchoices. ioral finance studies, customers’ financial decisions tend to be biased
|     |     |     |     |     |     |     | (Chira, | Adams, | & Thornton, |     | 2008; | Costa, de | Melo Carvalho, |     | de Melo |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----------- | --- | ----- | --------- | -------------- | --- | ------- |
5.1.3. Potentialofinteractivedatavisualization Moreira,&doPrado,2017).Somecustomerswouldonlyinvestinthose
| The interactive | data visualization |     | in  | the RA | service has | proven its |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------ | --- | --- | ------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
withhighreturnsandignoreotherfactors,andlayinvestorswithlimited
| potentialtohelpcustomersunderstandrisk,envisionthegrowthandloss |     |     |     |     |     |     | financial |          |       |     |          |         |                 |     |           |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | --- | -------- | ------- | --------------- | --- | --------- |
|                                                                 |     |     |     |     |     |     |           | literacy | would | not | actively | acquire | any information |     | but still |
oftheirassets,andassociateinformationwiththetimehorizon.Byusing makeinvestmentdecisions.Ifconventionalfinancialadvisoryserviceis
differentcolorsasdiscriminativevisualcuestoindicatedifferentsitua-
sales-centered,thenRAsaresupposedtoberesult-driven.Itisdesigned
tions,thisvisualizeddesignsynthesizesparametersfromdifferentsour- toencouragecustomerstostartinaverysmallamountbyshowingthem
ces (e.g., AI-driven models, input from customers), then embodies the theresultsquickly,socustomerscandecidebasedonthereturnrateor
complexmechanismintoaninteractivediagramthatcaneasilyfitwith
servicefee.Thus,itisunderstandablethatexistingRAsseemstobeeasy
customers’cognitiveability.Thus,thisuserstudycantreatinteractive
touseandtheir“smooth”and“simple”interfacemakescustomerrapidly
datavisualizationasanexplainableAIapproach.Moreover,thisdesign checkthefinalresultbecausetheydonotwanttoletcustomersleave
showstherecommendeddepositplanandstillgrantscustomersauton- halfway without seeing the financial products, which are their core
omytoinputandadjusttheirmoneytobeinvested.Thisfindingextends
sellingpointsoftheservice.
previous research regarding interactive data visualization in making Accordingtothefindingsofthisstudy,customersaremoreself-aware
judgments(Eberhard,2021),understandinginformation(Perdanaetal.,
|     |     |     |     |     |     |     | and | patient | when interacting |     | with | AI-empowered | systems | in  | making |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | ---- | ------------ | ------- | --- | ------ |
2018),andfinancialdecision-making(Tangetal.,2014)byuncovering financialdecisions.Theyarewillingtospendmoretimeandgetsufficient
| how well | it is used and its | potential | in  | automated | financial | advisory |     |     |     |     |     |     |     |     |     |
| -------- | ------------------ | --------- | --- | --------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
informationfromRAsystems,butserviceprovidersunderestimatethis.
contexts. Thesystemdesignissupposedtobemoreuser-centered,andthedecision
|     |     |     |     |     |     |     | mechanism |     | and reasoning |     | process | should be | transparent | and | under- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ------- | --------- | ----------- | --- | ------ |
ThediscrepancybetweenRAs’socialdesignandcustomers’perception standableforbothexpertandnon-expertcustomers.Mostimportantly,
5.2.
|     |     |     |     |     |     |     | data | visualization |     | can be | further | explored | to convey | sufficient | and |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ------ | ------- | -------- | --------- | ---------- | --- |
explainableinformationasaneffectiveinstrumentfortheinterface.
Itisadisruptivefindingthatcustomers’perceptionoftheRAservice
isnotinlinewiththeintentionsandambitionsoftheserviceproviders.
Findings in this study have extended the knowledge regarding RAs’ 5.4. Limitationsandfuturestudies
| weaknesses | (Jung, Dorner, | Weinhardt, | &   | Pusmaz, | 2018; Jung | et al., |     |     |     |     |     |     |     |     |     |
| ---------- | -------------- | ---------- | --- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2019).Mostimportantly,thesefindingshavequestionedinadisruptive This study did not employ standardized assessments to evaluate
waytheassumptionthatRAs’anthropomorphismcancompensateforthe participants’financialliteracy.Instead,thisinformationisincorporated
|               |              |        |       |         |            | &     | inthepre-testsurvey,andparticipantswereaskedtoself-reportfinancial |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ------ | ----- | ------- | ---------- | ----- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| lack of human | intervention | in RAs | (Adam | et al., | 2020; Deng | Chau, |                                                                    |     |     |     |     |     |     |     |     |
2021;Hildebrand&Bergner,2021).Accordingtoouruserstudy,cus-
knowledgeona1to5scale(scale1standsforverylittleknowledge;5
tomers needahumanadvisortodouble-checktheircomprehension of standsforexpertiseknowledge).Possiblebiasesexistinparticipantswho
aspectsoftheservice,primarilyduetothepossibilityof“miscommuni- overconfident financial
|     |     |     |     |     |     |     | are |     | or  | underestimate |     | their | knowledge. |     | Further |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ---------- | --- | ------- |
cation” in the configuration phase. Here, a more transparent and un- work regarding the comparison between user groups with different
derstandable information-sharing mechanism between customers and financialliteracywouldbeaveryinterestingavenue.Also,futurework
thesystemregardingtheinterpretationofthequestionsandeachoption could be extended from focusing on behavioral intention to including
connectedtothemislacking.Withoutknowingwhythesequestionsare long-termoutcomes,forexample,customers’retentionorafter-adoption
| asked and | what their answer | can | lead | them to, | customers | need and | behaviors. |     |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | ---- | -------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
expectahumanadvisorasabridgetoconfirmifcustomersunderstand
| the question | the same way | as was | intended | by  | the developers | of the | 6. Conclusion |     |     |     |     |     |     |     |     |
| ------------ | ------------ | ------ | -------- | --- | -------------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
system;andifthesysteminterpretsparticipantsinputinexactlytheway
that the participants meant. Different levels of human-likeness design This study conducts a user study regarding a fully functional AI-
mightaffectconsumers’behavioranddecision-makingincertainways; financial
|     |     |     |     |     |     |     | empowered |     | automated |     | advisory | system | and | its provided | ser- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --- | -------- | ------ | --- | ------------ | ---- |
however,basedonthefindingsinthisstudy,thatisnotwhatcustomers vice.Thefindingsshowthatthesocialaspectsthataresupposedtobe
neednorexpect. providedbytheRAarenotperceivedassuchbyparticipants.Thelackof
10

| H.Zhuetal. |     |     |     |     |     |     |     | DataandInformationManagement7(2023)100041 |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- |
transparency and incomprehensible information negatively affect par- Deng,B.,&Chau,M.(2021).Anthropomorphizedfinancialrobo-advisorsandinvestment
ticipants’trustinthesystemandmakesitdifficulttoadopttheresults advice-takingbehavior.27thannualamericasconferenceoninformationsystems,
AMCIS2021.https://www.scopus.com/inward/record.uri?eid¼2-s2.0-851186253
generated by RAs. This research extends previous research by investi- 96&partnerID¼40&md5¼38fd0a0a65ac096324a9903636d13a2b.Scopus.
gatingaRAandunderstandingcustomersinanin-depthempiricaluser- Dikmen,M.,&Burns,C.(2022).Theeffectsofdomainknowledgeontrustinexplainable
centered study in a real-life situation. It contributes to AI-empowered AIandtaskperformance:Acaseofpeer-to-peerlending.InternationalJournalof
system design in the financial service context and provides an under- Human-ComputerStudies,162,Article102792.https://doi.org/10.1016/
j.ijhcs.2022.102792
standingofcustomersinautomatedservice.
Eberhard,K.(2021).Theeffectsofvisualizationonjudgmentanddecision-making:A
systematicliteraturereview.ManagementReviewQuarterly.https://doi.org/10.1007/
s11301-021-00235-8
ErinEi,I.(2020).Humansvs.robots:Americanspreferfinancialadvisorsoveralgorithms.
Declarationofcompetinginterest
NerdWallet.https://www.nerdwallet.com/article/investing/robo-advisor-survey.
|     |     |     |     |     | financial | vonEschenbach,W.J.(2021).Transparencyandtheblackboxproblem:Whywedonot |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --------------------------------------------------------------------- | --- | --- | --- | --- |
The authors declare that they have no known competing trustAI.Philosophy&Technology,34(4),1607–1622.https://doi.org/10.1007/
interestsorpersonalrelationshipsthatcouldhaveappearedtoinfluence s13347-021-00477-0
EuropeanCommission.(2021).EUtaxonomy,corporatesustainabilityreporting,
theworkreportedinthispaper.
sustainabilitypreferencesandfiduciaryduties:DirectingfinancetowardstheEuropean
greendeal(brussels).https://eur-lex.europa.eu/legal-content/EN/TXT/?uri¼CELEX%
| References |     |     |     |     |     | 3A52021DC0188. |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
Faloon,M.,&Scherer,B.(2017).Individualizationofrobo-advice.TheJournalofWealth
Management,20(1),30–36.https://10.3905/jwm.2017.20.1.030.
Adam,M.,Toutaoui,J.,Pfeuffer,N.,&Hinz,O.(2020).Investmentdecisionswithrobo-
Fisch,J.E.,Labour(cid:2)e,M.,&Turner,J.A.(2019).Theemergenceoftherobo-advisor.In
advisors:Theroleofanthropomorphismandpersonalizedanchorsin J.E.Fisch,M.Labour(cid:2)e,&J.A.Turner(Eds.),ThedisruptiveimpactofFinTechon
recommendations.In27thEuropeanconferenceoninformationsystems-information
retirementsystems(pp.13–37).OxfordUniversityPress.https://doi.org/10.1093/
systemsforasharingsociety.ECIS2019.Scopushttps://www.scopus.com/inward/rec
ord.uri?eid¼2-s2.0-85087109501&partnerID¼40&md5¼6cdf3e42546628a3e8 oso/9780198845553.003.0002.
Fulk,M.,Grable,J.E.,&Kruger,M.(2018).Whousesrobo-advisoryservices,andwho
991152622edd11.
doesnot?FinancialServicesReview,27(2),173–188.
Anshari,M.,Almunawar,M.N.,Masri,M.,&Hrdy,M.(2021).Financialtechnologywith
a i -e n a b le d a n d e th ic a l c h al l en g e s . So c i e ty , 5 8 (3 ), 1 8 9 – 1 9 5 . Gan, L . Y . , K h a n , M . T . I . , & Li e w , T . W . ( 20 2 1 ). U n d e r sta n di n g c on su m e r ' s a d o p t io n o f
|                |                              |                            |                                               |     |     | fi n a n c ia | l r o b o -a d vi s o r s at | t h e o u tb re a k o f th e | C O V I D -1 9 c r is is | in M a l a y s ia . F i n a nc ia l |
| -------------- | ---------------------------- | -------------------------- | --------------------------------------------- | --- | --- | ------------- | ---------------------------- | ---------------------------- | ------------------------ | ----------------------------------- |
| Aoki , N . ( 2 | 0 2 1) . T h e im p o r t an | c e o f t h e a s s u ra n | c e th a t “ h u m a n sarestillinthedecision |     |     |               |                              |                              |                          |                                     |
loop”forpublictrustinartificialintelligence:Evidencefromanonlineexperiment. P l a n n in g Re v ie w , 4 ( 3 ). h t tp s : // d o i. o r g / 1 0 . 1 0 0 2 / c f p 2 .1 1 2 7
|     |     |     |     |     |     | Gerr a n s , P ., | & H e r sh e y , D . A . | ( 2 0 1 7 ). F i n a n c i a l a | d v i s e r a n xi e ty,financialliteracy,and |     |
| --- | --- | --- | --- | --- | --- | ----------------- | ------------------------ | -------------------------------- | --------------------------------------------- | --- |
ComputersinHumanBehavior,114,Article106572.https://doi.org/10.1016/
financialadviceseeking.JournalofConsumerAffairs,51(1),54–90.
j.chb.2020.106572 Guo,H.,&Polak,P.(2021).InArtificialintelligenceandfinancialtechnologyFinTech:How
Azaria,A.,Rosenfeld,A.,Kraus,S.,Goldman,C.V.,&Tsimhoni,O.(2015).Advice
AIisbeingusedunderthepandemicin2020(Vol.935,p.186).https://doi.org/
provisionforenergysavinginautomobileclimate-controlsystem.AIMagazine,36(3),
| 61–72. |     |     |     |     |     | 10.1007/978-3-030-62796-6_9.Scopus. |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
vandenHaak,M.,DeJong,M.,&JanSchellens,P.(2003).Retrospectivevs.Concurrent
Bedu(cid:2)e,P.,&Fritzsche,A.(2022).CanwetrustAI?Anempiricalinvestigationoftrust
think-aloudprotocols:Testingtheusabilityofanonlinelibrarycatalogue.Behaviour
r e q u ir e m e n t s a n d g u id e t o s u c ce s s fu l A I a d o p t io n . J ou r n a l of E nt e r p ri se I n fo rmation &InformationTechnology,22(5),339–351.https://doi.org/10.1080/0044929031000
| M a n a g | e m en t , 3 5 ( 2) , 5 3 0– | 5 4 9 . h tt p s :/ / d oi .o r | g / 1 0 .1 1 0 8 / J E IM -0 | 6 - 2 0 2 0 -0 2 3 | 3   |                  |                              |                                   |                               |                                      |
| --------- | ---------------------------- | ------------------------------- | ---------------------------- | ------------------ | --- | ---------------- | ---------------------------- | --------------------------------- | ----------------------------- | ------------------------------------ |
|           |                              |                                 |                              |                    |     | Hild e b r a n d | , C ., & B e r g n e r , A . | ( 2 0 2 1 ) . C o n v e r s a t i | o n a l r o b o a d v is o rs | a s s u r r o g a te s o f t ru s t: |
Bela nc h e , D . , C a s a lo(cid:2) , L . V . , & F l a v i(cid:2)a n , C . ( 2 0 1 9 ) . A r t i fi c i a l I n t e l l i g e n c e i n F in T e c h : fi fi
|     |     |     |     |     | &   | O n b o a r | d i n g e x p e r i e n c e , | r m p e r c e p t i o n , a n d | c o n s u m e r n a n c | i a l d e c i s i o n m a ki n g . |
| --- | --- | --- | --- | --- | --- | ----------- | ----------------------------- | ------------------------------- | ----------------------- | ---------------------------------- |
U n d e r s t a n d i n g r o b o - a d v i so r s a d o p t io n a m o n g c u s to m e r s . In d u s t r ia l M a n a g e m en t J o u rn a l o f t h e A c a d e m y o f M a r k e t i n g S c i e n c e , 4 9 ( 4 ) , 6 5 9 – 6 7 6 . h t t p s : / / d o i . o r g/
| D a t a S | y s t e m s , 1 1 9 (7 ) , 1 4 | 1 1 – 1 4 3 0 . h tt p s : / / d | o i .o r g / 1 0 . 1 1 0 8 / I M | D S -0 8 -2 0 1 | 8 - 0 3 6 8 |     |     |     |     |     |
| --------- | ------------------------------ | -------------------------------- | -------------------------------- | --------------- | ----------- | --- | --- | --- | --- | --- |
10.1007/s11747-020-00753-z
Beltramini,E.(2018).Humanvulnerabilityandrobo-advisory:Anapplicationof
Co e c k e l be r g h 's v u l n e r a b il it y to t h e m a c h i n e -h u m a n in t e r fa ce . B a l ti c J o u r n alof Hohenberger,C.,Lee,C.,&Coughlin,J.F.(2019).Acceptanceofrobo-advisors:Effectsof
financialexperience,affectivereactions,andself-enhancementmotives.Financial
| M a n a g | e m e n t, 1 3 ( 2 ) , 2 5 0 – | 2 6 3. ht t p s: // d o i . o rg | / 1 0. 1 10 8 / B J M -1 | 0 - 2 0 1 7 - 0 3 1 | 5   |     |     |     |     |     |
| --------- | ------------------------------ | -------------------------------- | ------------------------ | ------------------- | --- | --- | --- | --- | --- | --- |
BenDavid,D.,Resheff,Y.S.,&Tron,T.(2021).ExplainableAIandadoptionoffinancial PlanningReview,2(2).https://doi.org/10.1002/cfp2.1047
Holzinger,A.,Biemann,C.,Pattichis,C.S.,&Kell,D.B.(2017).Whatdoweneedtobuild
algorithmicadvisors:Anexperimentalstudy.InProceedingsofthe2021AAAI/ACM
explainableAIsystemsforthemedicaldomain?.ArXivPreprintArXiv:1712.09923.
conferenceonAI,ethics,andsociety.https://doi.org/10.1145/3461702.3462565, InsiderIntelligence(Ed.).(2021).June30).Younginvestorsdroveuseofrobo-advisors
390–400.
duringpandemic.InsiderIntelligence.https://www.emarketer.com/content/yo
Ben-David,D.,&Sade,O.(2020).Robo-advisoradoption,willingnesstopay,and
trust—beforeandattheoutbreakofthecovid-19pandemic.InWillingnesstopay,and ung-investors-drove-robo-advisor-use.
|     |     |     |     |     |     | Jame so n ,A | ., K o n s t a n , J ., & R | i e d l, J . ( 2 0 0 2 ) . A I | te c h n i q u e s fo r p e r | s o n a l i z e d |
| --- | --- | --- | --- | --- | --- | ------------ | --------------------------- | ------------------------------ | ----------------------------- | ----------------- |
trust—beforeandattheoutbreakoftheCOVID-19pandemic.July2020.
|     |     |     |     |     |     | re co m m | en d a t i o n . I n T uto r | i a la t 1 8 t h n a ti o n a lc | o n fe r e n c e on a r ti fi c | i a li n t e l li gence(AAAI). |
| --- | --- | --- | --- | --- | --- | --------- | ---------------------------- | -------------------------------- | ------------------------------- | ------------------------------ |
Berger,R.(2015).7roboadvisorsthatmakeinvestingeffortless.Forbes.https://www.for Jarrahi,M.H.(2018).Artificialintelligenceandthefutureofwork:Human-AIsymbiosis
bes.com/sites/robertberger/2015/02/05/7-robo-advisors-that-make-investing-effor
inorganizationaldecisionmaking.BusinessHorizons,61(4),577–586.
tl e ss / . R e t r ie v ed F e b r u a r y 2 1 , 2 0 2 2 , f r o m . 18).Robo-advisory.Business&
Bolto n , P . , Fr e i x a s , X. , & S h a p i r o , J . ( 2 0 0 7 ) . C o n fl i c t s o f i n t e re s t ,i n fo r m a t io n p r o v i s i on, Jung , D . , D o r n er , V . , G la s e r , F ., & M o ra n a , S . ( 2 0
|           |                              |                                   |                                  |                    |               | I nf o r m a | ti o n S y st e m s E n g i n ee | ri ng ,6 0 (1 ) , 8 1 – 8 6 | .   |     |
| --------- | ---------------------------- | --------------------------------- | -------------------------------- | ------------------ | ------------- | ------------ | -------------------------------- | --------------------------- | --- | --- |
| a n d c o | m p e t i t io n i n th e fi | n a n c i a l s e r v i c e s i n | d u s t r y. J o u r n a l o f F | in a n ci a l E co | n o m i c s , |              |                                  |                             |     |     |
–3 jfin Jung , D . , D o r n e r , V . , W e in h a r d t , C ., & P u s m a z , H . (2 0 1 8 ) . D e s ig n in g a r o b o -a d v i s o rfor
8 5 ( 2 ) , 2 97 3 0 . h t tp s: / / d o i. o rg / 1 0 .1 0 1 6 / j. e co . 2 0 0 5. 0 6 . 0 0 4 r is k - a ve r s e , l o w - b ud g e t c o n s u m e rs. E l e ct ro n i c M ar k e ts , 2 8 ( 3 ), 3 6 7– 3 8 0 . h tt p s : / /
| Bren n e r , L ., | & M e y ll , T . (2 0 2 | 0 ) . R o b o -a d v is o r s: | A su b st i t u te f o r h u | m anfinancialadvice? |     |     |     |     |     |     |
| ----------------- | ----------------------- | ------------------------------ | ---------------------------- | -------------------- | --- | --- | --- | --- | --- | --- |
doi.org/10.1007/s12525-017-0279-9
JournalofBehavioralandExperimentalFinance,25,Article100275.https://doi.org/ Jung,D.,Glaser,F.,&Ko€pplin,W.(2019).Robo-advisory:Opportunitiesandrisksforthe
| 1 0 .1 0 1   | 6 / j. jb e f . 2 0 2 0 . 1 0 0 | 2 7 5                          |                               |                               |     |            |                               |                               |                              |                                  |
| ------------ | ------------------------------- | ------------------------------ | ----------------------------- | ----------------------------- | --- | ---------- | ----------------------------- | ----------------------------- | ---------------------------- | -------------------------------- |
|              |                                 |                                |                               |                               |     | f u t u re | o f fi n an c i a l ad v i so | ry . I n V . N i ss e n ( E d | .) , A d v a n c es in c o n | su lt in g re s ea r c h ( p p . |
| Brow n , M . | ( 2 0 1 7 ) . S e p t e m b e   | r 1 9 . h tt p s :/ / le n d e | d u .c o m / b l o g / r ob o | - a d v is or s-vs-financial- |     |            |                               |                               |                              |                                  |
fi 4 0 5 – 42 7 ) . Sp ri n g e r In t e rn a ti o na l P u b li s hi n g . h tt p s :/ / d o i.o rg / 1 0 .1 0 0 7/ 9 7 8 - 3 -3 1 9 -
| a d v i s o r | s / . M i l l e n n i a l s: R | o b o -a d v is o r s o r n a | n c ia l a d v i s o rs ? L e | n d E D U . |     | 95999-3_20. |     |     |     |     |
| ------------- | ------------------------------ | ----------------------------- | ----------------------------- | ----------- | --- | ----------- | --- | --- | --- | --- |
Bruckes,M.,Westmattelmann,D.,Oldeweme,A.,&Schewe,G.(2019).Determinantsand
Kilic,M.,Heinrich,P.,&Schwabe,G.(2015).Coercingintocompletenessinfinancial
barriersofadoptingrobo-advisoryservices.InProceedingsofinternationalconference
on i n fo r m a ti o n sy s t e m s ( I C IS ) 2019.2.https://aisel.aisnet.org/icis2019/blockchain_ advisoryserviceencounters.Proceedingsofthe18thACMConferenceonComputer
SupportedCooperativeWork&SocialComputing,1324–1335.https://doi.org/
| fi nt e c h | / bl o c k ch a i n _ fi nt e c | h / 2. |     |     |     |            |                               |     |     |     |
| ----------- | ------------------------------- | ------ | --- | --- | --- | ---------- | ----------------------------- | --- | --- | --- |
|             |                                 |        |     |     | fl  | 1 0 .1 1 4 | 5 / 2 6 7 5 1 3 3 . 2 6 7 5 2 | 8 9 |     |     |
Burk e , J ., H u ng , A . A . , C l i ft , J . , G a r be r, S . , & Y o on g , J .K . ( 2 0 1 5) . I m pa c t s of c o n i c ts of Lee, M . K . , & P a r k , H . ( 2 0 1 9 ) . E x p l o r in g f ac to r s in fl u e n c in g u s a ge in t e n t io n o f c ha tb ot-
| i n te r es      | t in t h e fi n a n c i a l s    | e r v ic e s in d u s t ry. I n                               | R A N D w o r k in g p a | p er se r i es W | R - 1 0 7 6 . |                |                                    |                             |                               |                             |
| ---------------- | -------------------------------- | ------------------------------------------------------------- | ------------------------ | ---------------- | ------------- | -------------- | ---------------------------------- | --------------------------- | ----------------------------- | --------------------------- |
|                  |                                  |                                                               |                          |                  |               | c h a t b o    | t i n fi n a n c i a l s e r v i c | e . J o u r n al o f th e K | o re a n S o c ie ty f o r Qu | a li t y M a n a ge m en t, |
| h t t p s :/     | / d o i . o r g / 1 0 .2 1 3 9 / | s s r n.2 7 9 4 2 4 6                                         |                          |                  |               | 47(4),755–765. |                                    |                             |                               |                             |
| Cai, C . J . , W | i n t e r , S . , S te in e r ,  | D . , W il c ox , L . ,&Terry,M.(2019).HelloAI”:Uncoveringthe |                          |                  |               |                |                                    |                             |                               |                             |
Litterscheidt,R.,&Streich,D.J.(2020).Financialeducationanddigitalasset
onboardingneedsofmedicalpractitionersforhuman-AIcollaborativedecision-
making.ProceedingsoftheACMonHuman-ComputerInteraction,3(CSCW),1–24. management:What'sintheblackbox?JournalofBehavioralandExperimental
Economics,87,Article101573.https://doi.org/10.1016/j.socec.2020.101573
Cheng,X.,Guo,F.,Chen,J.,Li,K.,Zhang,Y.,&Gao,P.(2019).Exploringthetrust
influencingmechanismofrobo-avisorservice:Amixedmethodapproach. Lour e n ço , C . J . S ., D e lla e r t, B . G. C. , & D o n k e r s , B . (2 0 2 0 ) . W h o se a lg o r i th m sa y s s o:The
fi
Sustainability,11(18),4917.https://doi.org/10.3390/su11184917 r e la ti o n sh i p s b et w e e n ty p e of r m ,p e r c e p t i on s o f t r u s ta n d ex p e r ti s e, an d t h e
acceptanceoffinancialrobo-advice.JournalofInteractiveMarketing,49,107–124.
Chira,I.,Adams,M.,&Thornton,B.(2008).Behavioralbiaswithinthedecisionmaking
process.JournalofBusiness&EconomicsResearch,6(8). h t t p s: / / d o i . o rg / 1 0 .1 0 16 / j .i n tm ar .2 0 1 9 .1 0 .0 0 3
|               |                              |                           |                            |                   |               | Mog aj i , E . , | S o e t a n , T . O ., & K | i e u , T. A . (2 0 2 1 ). T | h eimplicationsofartificialintelligence |     |
| ------------- | ---------------------------- | ------------------------- | -------------------------- | ----------------- | ------------- | ---------------- | -------------------------- | ---------------------------- | --------------------------------------- | --- |
| Cost a, D . F | ., d e M e l o C a r v a l h | o , F ., d e M e lo M o r | e i r a , B . C ., & d o P | r a d o , J . W . | ( 2 0 1 7 ) . |                  |                            |                              |                                         |     |
fi o n t h e d i g it a l m a r k e t in g o f fi n an c i a l s e r v ic e s t o v u ln e r ab l e c u s t o m e r s. A us tr a l a si an
B i b li o m e tr i c a n a l y s i s o n t h e a s s o c i a t io n b e t w e e n b e h a v i o r a l n a n c e a n d d e c i si o n M ar k e ti n g J o u r na l , 2 9 ( 3 ), 2 3 5 –2 4 2 . h t t p s :/ / d o i .or g / 1 0 .1 0 1 6 / j. a u s m j .2 0 20 .0 5 . 0 0 3
| m a k i n g | w i t h c o g n i t i v e b | i a s e s s u c h a s o v e r c | o n fi d e n c e, a n c h o r in | g e f fe c t a n | d   |     |     |     |     |     |
| ----------- | --------------------------- | ------------------------------- | -------------------------------- | ---------------- | --- | --- | --- | --- | --- | --- |
Morana,S.,Gnewuch,U.,Jung,D.,&Granig,C.(2020).Theeffectofanthropomorphism
confirmationbias.Scientometrics,111(3),1775–1799.
Day,M.-Y.,Lin,J.-T.,&Chen,Y.-C.(2018).ArtificialIntelligenceforconversationalrobo- onInvestmentdecision-makingwithrobo-advisorchatbots.InProceedingsofEuropean
conferenceoninformationsystems(ECIS).
advisor.In2018IEEE/ACMinternationalconferenceonadvancesinsocialnetworks
Namjun,C.H.A.,Hosoo,C.H.O.,Sangman,L.E.E.,&Hwang,J.(2019).EffectofAI
analysisandmining(ASONAM).https://doi.org/10.1109/ASONAM.2018.8508269, recommendationsystemontheconsumerpreferencestructureine-commerce:Based
1057–1064.
11

H.Zhuetal. DataandInformationManagement7(2023)100041
ontwotypesofpreference.In201921stinternationalconferenceonadvanced Shrestha,Y.R.,Ben-Menahem,S.M.,&VonKrogh,G.(2019).Organizationaldecision-
communicationtechnology(ICACT)(pp.77–80). makingstructuresintheageofartificialintelligence.CaliforniaManagementReview,
Nueesch,R.,Puschmann,T.,&Alt,R.(2014).Realizingvaluefromtablet-supported 61(4),66–83.
customeradvisory:Casesfromthebankingindustry.InBledeConference(Vol.34). So€derberg,I.L.(2013).Relationshipsbetweenadvisorcharacteristicsandconsumer
Nueesch,R.,Zerndt,T.,Alt,R.,&Ferretti,R.G.(2016).Tabletspenetratethecustomer perceptions.InternationalJournalofBankMarketing,31(3),147–166.https://doi.org/
advisoryprocess:Acasefromaswissprivatebank.BLED2016Proceedings,45. 10.1108/02652321311315276
Nussbaumer,P.,&Matter,I.(2011).Whatyouseeiswhatyou(can)get?Designingfor Sonboli,N.,Smith,J.J.,CabralBerenfus,F.,Burke,R.,&Fiesler,C.(2021).Fairnessand
processtransparencyinfinancialadvisoryencounters.InP.Campos,N.Graham, transparencyinrecommendation:Theusers'perspective.InProceedingsofthe29th
J.Jorge,N.Nunes,P.Palanque,&M.Winckler(Eds.),Human-computerinteraction– ACMconferenceonusermodeling,adaptationandpersonalization.https://doi.org/
interact2011(pp.277–294).SpringerBerlinHeidelberg. 10.1145/3450613.3456835,274–279.
Nussbaumer,P.,Matter,I.,Reto(cid:3)aPorta,G.,&Schwabe,G.(2012).Designingforcost Stefanel,M.,&Goyal,U.(2019).Artificialintelligence&financialservices:Cuttingthrough
transparencyininvestmentadvisoryserviceencounters.Business&Information thenoise.London,England:APISPartners(Tech.Rep).
SystemsEngineering,4(6),347–361.https://doi.org/10.1007/s12599-012-0237-1 Tang,F.,Hess,T.J.,Valacich,J.S.,&Sweeney,J.T.(2014).Theeffectsofvisualization
Nussbaumer,P.,Matter,I.,&Schwabe,G.(2012).Enforced”vs.“Casual” andinteractivityoncalibrationinfinancialdecision-making.BehavioralResearchin
transparency—findingsfromIT-Supportedfinancialadvisoryencounters.ACM Accounting,26(1),25–58.https://doi.org/10.2308/bria-50589
TransactionsonManagementInformationSystems,3(2),1–19.https://doi.org/ Tertilt,M.,&Scholz,P.(2018).Toadvise,ornottoadvise—howrobo-advisorsevaluate
10.1145/2229156.2229161 theriskpreferencesofprivateinvestors.TheJournalofWealthManagement,21(2),
Perdana,A.,Rob,A.,&Rohde,F.(2018).Doesvisualizationmatter?Theroleof 70–84.
interactivedatavisualizationtomakesenseofinformation.AustralasianJournalof Todd,T.M.,&Seay,M.C.(2020).Financialattributes,financialbehaviors,financial-
InformationSystems,22.https://doi.org/10.3127/ajis.v22i0.1681 advisory-userbeliefs,andinvestingcharacteristicsassociatedwithhavinguseda
Pradhan,S.,&Wang,S.(2020).Exploringfactorsinfluencingolderadults'willingnessto robo-advisor.FinancialPlanningReview,3(3).https://doi.org/10.1002/cfp2.1104
userobo-advisors.ACIS2020Proceedings.,50.https://aisel.aisnet.org/acis2020/50. Turilli,M.,&Floridi,L.(2009).Theethicsofinformationtransparency.Ethicsand
Salo,M.,&Haapio,H.(2017).Robo-advisorsandinvestors:Enhancinghuman-robot InformationTechnology,11(2),105–112.https://doi.org/10.1007/s10676-009-9187-
interactionthroughinformationdesign.SSRNElectronicJournal.https://doi.org/ 9
10.2139/ssrn.2937821 Wolf,C.T.,&Ringland,K.E.(2020).Designingaccessible,ExplainableAI(XAI)experiences
Seiler,V.,&Fanenbruck,K.M.(2021).Acceptanceofdigitalinvestmentsolutions:The (Vol.125).Comput:SIGACCESSAccess.https://doi.org/10.1145/3386296.3386302
caseofroboadvisoryinGermany.InResearchininternationalbusinessandfinance Wu,M.,&Gao,Q.(2021).Understandingtheacceptanceofrobo-advisors:Towardsa
(Vol.58).https://doi.org/10.1016/j.ribaf.2021.101490.Scopus. hierarchicalmodelintegratedproductfeaturesanduserperceptions.InQ.Gao,&
Shin,D.(2021a).Theeffectsofexplainabilityandcausabilityonperception,trust,and J.Zhou(Eds.),HumanaspectsofITfortheagedpopulation.Technologydesignand
acceptance:ImplicationsforexplainableAI.InternationalJournalofHuman-Computer acceptance(pp.262–277).SpringerInternationalPublishing.
Studies,146,Article102551.https://doi.org/10.1016/j.ijhcs.2020.102551 Yang,Q.,Steinfeld,A.,&Zimmerman,J.(2019).Unremarkableai:Fittingintelligent
Shin,D.(2021b).Theperceptionofhumannessinconversationaljournalism:Analgorithmic decisionsupportintocritical,clinicaldecision-makingprocesses.Proceedingsofthe
information-processingperspective(Vol.146144482199380).NewMedia&Society. 2019CHIConferenceonHumanFactorsinComputingSystems,1–11.
https://doi.org/10.1177/1461444821993801 Zheng,X.,Zhu,M.,Li,Q.,Chen,C.,&Tan,Y.(2019).FinBrain:WhenfinancemeetsAI
2.0.FrontiersofInformationTechnology&ElectronicEngineering,20(7),914–924.
12