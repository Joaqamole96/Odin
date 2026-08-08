Are Generative AI Agents Effective Personalized Financial
Advisors?
TakehiroTakayanagi KiyoshiIzumi JavierSanz-Cruzado
takayanagi-takehiro590@g.ecc.u- izumi@sys.t.u-tokyo.ac.jp javier.sanz-
tokyo.ac.jp TheUniversityofTokyo cruzadopuig@glasgow.ac.uk
TheUniversityofTokyo Tokyo,Japan UniversityofGlasgow
Tokyo,Japan Glasgow,UnitedKingdom
RichardMcCreadie IadhOunis
richard.mccreadie@glasgow.ac.uk iadh.ounis@glasgow.ac.uk
UniversityofGlasgow UniversityofGlasgow
Glasgow,UnitedKingdom Glasgow,UnitedKingdom
Abstract ACMReferenceFormat:
Largelanguagemodel-basedagentsarebecomingincreasinglypop- TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMc-
Creadie,andIadhOunis.2025.AreGenerativeAIAgentsEffectivePersonal-
ularasalow-costmechanismtoprovidepersonalized,conversa-
izedFinancialAdvisors?.InProceedingsofthe48thInternationalACMSIGIR
tionaladvice,andhavedemonstratedimpressivecapabilitiesin
ConferenceonResearchandDevelopmentinInformationRetrieval(SIGIR
relativelysimplescenarios,suchasmovierecommendations.But ’25),July13–18,2025,Padua,Italy.ACM,NewYork,NY,USA,10pages.
how do these agents perform in complex high-stakes domains,
https://doi.org/10.1145/3726302.3729897
wheredomainexpertiseisessentialandmistakescarrysubstantial
risk?ThispaperinvestigatestheeffectivenessofLLM-advisorsin
thefinancedomain,focusingonthreedistinctchallenges:(1)elic- 1 Introduction
itinguserpreferenceswhenusersthemselvesmaybeunsureof
Personalizedadviceplaysacrucialroleinoursociety,particularly
theirneeds,(2)providingpersonalizedguidancefordiverseinvest-
incomplexandhigh-stakesdomainslikehealthcareandfinance.
mentpreferences,and(3)leveragingadvisorpersonalitytobuild
Advisorsandprofessionalsinthesefieldsusetheirexpertisetooffer
relationshipsandfostertrust.Viaalab-baseduserstudywith64par-
personalizedguidanceandemotionalsupporttotheirclients,lever-
ticipants,weshowthatLLM-advisorsoftenmatchhumanadvisor
agingpeople’sspecificpreferencesand/orcircumstances.However,
performancewhenelicitingpreferences,althoughtheycanstrug-
advisoryservicesareoftenprovidedatahighcost,effectivelyex-
gletoresolveconflictinguserneeds.Whenprovidingpersonalized
cludingalargeportionofthepopulationfromthiscriticaladvice.
advice,theLLMwasabletopositivelyinfluenceuserbehavior,but
Inthefinancialdomain,tomitigatethisissue,automateddecision
demonstratedclearfailuremodes.Ourresultsshowthataccurate
supportsystemshavebeenwidelystudied,withaspecialfocuson
preferenceelicitationiskey,otherwise,theLLM-advisorhaslittle
investment-relatedpredictions,suchasfinancialassetrecommen-
impact,orcanevendirecttheinvestortowardunsuitableassets.
dations[27,32,33].
Moreworryingly,usersappearinsensitivetothequalityofadvice
Recentadvancesinnaturallanguageprocessingandlargelan-
beinggiven,orworsethesecanhaveaninverserelationship.In-
guagemodels(LLMs)havesignificantlyacceleratedthedevelop-
deed,usersreportedapreferenceforandincreasedsatisfactionas
mentofconversationalagents,presentingthepotentialtofunction
wellasemotionaltrustwithLLMsadoptinganextrovertedpersona,
aspersonalizedassistantsforinformation-seekinganddecision-
eventhoughthoseagentsprovidedworseadvice.
making[40].Theseagentscannowleveragemulti-turndialogues,
enablingdynamic,mixed-initiativeinteractionswherebothusers
CCSConcepts
andsystemscantaketheleadinconversations[1].Thisprogres-
•Informationsystems→Decisionsupportsystems;Person- sion has expanded the application of conversational agents to
alization. varioustasks,suchasrecommendation,questionanswering,and
search[10,24,31,40].
Keywords The application of these conversational agents for financial
decision-makingrepresentsamuchmorecomplexscenariothan
largelanguagemodels,financialadvisor,userstudy,generativeAI
otherslikemovierecommendations,becauseusersarenotnec-
essarilyfamiliarwiththebasicterminologyandconceptsinthis
space,andmistakescarryasubstantialriskthatcanleadtolarge
monetary losses. While there is a growing interest in building
theseconversationalassistantstoprovideautomatedfinancialad-
ThisworkislicensedunderaCreativeCommonsAttribution-ShareAlike4.0Interna-
tionalLicense. vice [18], previous work has mostly targeted agents capable of
SIGIR’25,Padua,Italy handlingsimpleinquiries[16,35,36].Comparedtothesesimple
©2025Copyrightheldbytheowner/author(s).
systems, helping users navigate financial decisions and market
ACMISBN979-8-4007-1592-1/2025/07
https://doi.org/10.1145/3726302.3729897 uncertaintiesposesamuchgreaterchallenge.Therefore,itisnot
286

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
Hi Now, let's talk about the current thesecondstage,givenanindividualasset,theadvisorprovidesin-
user We y lc o o u m m e o ! W st h in at t e in re d s u t s e t d ri e in s ? are s W to h c a k t c f a a i b r n s o d t u i c d t a a t u t h g e e h , A c t o m y m o a u p z r o a n n at y .c t ? o e m nt , i I o n n c . advisor ( f o o r rm n a o t t i ) o t n h a e b i o n u v t e i s t to to r’ t s h p e r i e n f v e e r s e t n o c r e , s in . c T l o ud a i n n s g w h e o r w th th e e d a iff ss e e r t e m nt a q tc u h e e s s -
advisor
I tend to prefer non-cyclical
r A e s r g t e a o y r c d o k l u s e c s m o o s r n o o s d r f t e i t e t i i h a o n e d n to y s e ? c v s o o to n la c o t k m i s le ic advisor user stock e it s c s , o c I e ’ o n m e m o m u m m s n i c s e a u r s b c r w i e e t i n a p se b g la n o s t s u f a i o t s t i r A a v m m n e . t e a o z - on— w w tio e e n c c s o o , m m w p p e a a c r r o e e m p t p w e a r o r s e o p n d e a i r ff s li o e z r n e e d a n li v t z s c e . o d n n o a fi d n g v - u p i r s e a o r t r s i s o o n n w s a i l t o i h z f e t d d h i e s a t L d in v L c i M s t o - p r a e s d r , v s a i o n s n o d a r , : l t i fi h ti r e e s n s t . , ,
I s fe t e o e c c l o k m n s o o t r m h e a i c c t o f c m l a u n f c o t w r u t i a a t t h b i l s o e t n a w s n . i d th im s A i o p g m f a n f a c if e z t i r e c o i a d n n n ’ g s b t y A c r l e W e o v c u S e o d s n n e u s o g e e m m r a v i e n c ic n d s e t w g s d r i r l o n e i w v g s e s s t s h … , … . advisor 2 RelatedWork
user
Stage 1:Preference Elicitation Stage 2:Advisory Discussion 2.1 PersonalizationandPreferenceElicitation
Informationsystems,especiallythosefocusedonsearchandrec-
Figure1:ConceptualillustrationofanLLM-advisorwithtwo
ommendationbenefitfrompersonalization[14].Specifically,per-
stages:(1)PreferenceElicitationand(2)AdvisoryDiscussion.
sonalizationtechniquesplayacrucialroleinenhancinguserex-
yetclearhowtodevelopsystemsthateffectivelysupportcomplex perience [17, 22, 41]. Interactive approaches, such as conversa-
financialinformation-seekinganddecision-makingtasks. tionalpreferenceelicitationrepresentthefrontierofpersonaliza-
Thisworkaimstoclosethisgapbyexploringtheeffectiveness tion.Thisproblemhasreceivedgrowingattention,asadvances
ofLLMstoactaspersonalizedfinancialadvisoryagents.Inpartic- ingenerativeAInowprovideafunctionalmechanismtocollect
ular,wefocusonthreeproblems:(a)elicitinginvestorpreferences userpreferencesdynamicallyinafree-formmanner[40].Thisin-
throughinteractiveconversations,(b)providingpersonalizedguid- teractiveapproachcancapturemorediverseandtargetedinsights
ancetohelpusersdeterminewhetherparticularfinancialassets thanstaticapproacheslikequestionnaires[6,10,23,24,31].In-
alignwiththeirpreferences,and(c)leveragingthepersonalityof deed,recentstudieshaveproposedvariousmethodsforeffective
theadvisortofostertrustontheadvisor. conversationalpreferenceelicitation[31,42],aswellasuserstud-
First,thefinancialliteratureemphasizesthatelicitinguserpref- ies on the perceived quality of this process in domains such as
erencesiscentraltodeliveringsuitableadvice[30].However,it e-commerce,movies,fashion,books,travel,andrestaurantrecom-
remainsunclearwhethercurrentconversationaltechnologies,par- mendations[2,7,15,23,31,45].
ticularlythosepoweredbyLLMs,cancorrectlyelicituserprefer- However,wearguethatforsomeimportantdomains,tryingto
encesinspecializeddomainswhereusers struggletoarticulate directlycollectpreferencesisinsufficient.Animplicitassumption
theirneeds.Ourworkaddressesthischallengeinthecontextof ofthesestudiesisthatifdirectlyasked,theuserwillbeableto
financialservices. accuratelyexpresstheirpreferences.Itisreasonabletoexpectthat
Second,althoughpersonalizationiswidelyregardedasimpor- thisassumptionwouldholdforscenarioslikemovierecommenda-
tantinthefinancialdecision-supportliterature[27,32,33],itsvalue tion;wecanaskauser“doyoulikehorrormovies?”andexpecta
inaconversationalsettingremainsuncertain.Inparticular,weex- usefulresponse.Ontheotherhand,thiswillnotholdforcomplex
plorewhethertailoringdialoguearoundauser’sprofileandcontext tasks,wheretheuserlackstheknowledgetoformanaccuratere-
improvesfinancialdecision-making.Additionally,wealsoexplore sponse[10,39].Forinstance,inaninvestmentcontextifweasked
howpersonalizationinfluencesuserperceptionsoftheadvisor,in “doyoupreferETFsorBonds?”,itisnotclearthataninexperienced
termsofaspectsliketrustandsatisfaction. userwouldbeabletoproduceameaningfulanswer.Inthesecases,
Finally, in personalized advisory settings within high-stakes anidealagentneedstofillthegapsintheuserknowledgethrough
domains,therelationshipandtrustbetweentheclientandadvisor conversation,aswellasinfertheuserpreferencesacrossmultiple
playacrucialrole[18].Researchonconversationalagentssuggests (oftenuncertain)userresponses.Buthoweffectivearegenerative
thatagentpersonalitysignificantlyaffectsusers’perceptionsof AIagentsatthiscomplextask?Thispaperaimstoanswerthatques-
thesystem[3,29].However,itremainsunclearhowanadvisor’s tionforthedomainoffinancialadvisory;aparticularlychallenging
personalityinthefinancialdomaininfluencesboththequalityof domaingivenitstechnicalnatureandhighrisksifdonepoorly.
users’financialdecisionsandtheiroverallexperience.
Tosummarize,inthispaper,weexplorethefollowingquestions: 2.2 Financialadvisory
• RQ1:CanLLM-advisorseffectivelyelicituserpreferences Inthefinancialdomain,advisorshelpindividualsmanagetheir
throughconversation? personalfinancesbyofferingguidanceoninvestmentsandassist-
• RQ2:Doespersonalizationleadtobetterinvestmentdeci- ing with decision-making [34]. While financial advisors can be
sionsandamorepositiveadvisorassessment? beneficial,theirservicesoftencomeatahighcost,makingthem
• RQ3:Dodifferentpersonalitytraitsaffectdecisionquality unaffordableformanypeople.Tomitigatethisissue,automated
andadvisorassessment? (non-conversational)financialdecisionsupportsystemssuchas
Toaddressthesequestions,weconductalab-baseduserstudy financialrecommendersystemshavebeenwidelystudied[44].The
thatexplorestheeffectivenessofLLMsasinteractiveconversational majorityofresearchinthisareahasbeenfocusedonhowtofind
financialadvisors,onwhichwesimulaterealisticinvestmentsce- profitableassets(i.e.thosethatwillmakemoneyifweinvestin
nariosusinginvestornarrativesandstockrelevancescorescurated them).Theseworksassumeasimplifieduser-model,whereanin-
byfinancialexperts.Figure1illustratesanexampleconversation vestorisonlyconcernedwithmaximizingreturn-on-investment
withtheadvisor,dividedintotwostages:first,theLLM-advisorat- overafixedperiodoftime[27,32,33].Thesestudiesframefinancial
temptstocapturetheinvestorpreferencesthroughconversation;in advisoryasarankingproblem,wherethegoalistorankfinancial
287

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
Investor profile 𝑖 Investmen 𝑖𝑝 t 𝑟 p 𝑒 r 𝑓 eferences Ground truth ranking
N A a g m e e J 3 a 0 son Matthews M St a a r t it u a s l Married c E u x r p a e t r e t d - Stock style c E u x r p a e t r e t d - Ra 1 nk C T o h m e p C a o n ca y -Cola Score (3/3)
Occupation IT Systems Children No Value stock Company
Jason works at a mid-siz D ed e s in c s r u ip ra t n io ce n company and values job Dividend payments 2 Walmart Inc. (2/3)
stability alongside predictable daily responsibilities... He is a Regular dividends
cautious planner favoring steady, reliable returns over 3 JPMorgan Chase & (1/3)
higher-risk investments… He invests in resilient, well- Sensitivity to macro market Co
e d s o t w a n b t li u s r h n e s d — e c s o p m ec p i a al n ly ie t s h os th e a o t f fe c r a in n g r w e e g a u t la h r e d r iv e id c e o n n d o … m ic Defensive stock 4 Amazon.com, Inc. (0/3)
Figure2:Exampleofaninvestorprofile,investmentpreferences,andgroundtruthranking.Dashedlinecomponentsareused
forevaluation(andtherefore,theyarenotshowntotheuser/LLM).
assetsforauseroveraspecifiedtimeperiod.However,arecent 3.1 InvestorProfiles
studysuggeststhatalargepartofthevalueofferedbyhumanfi- TofairlyevaluatetheabilityofanyLLM-advisor,weneedtohave
nancialadvisorsstemsfromtheirabilitytopersonalizeinvestment theminteractwithhumanuserswithrealneeds.Giventheopen-
guidancetoclients’specificneeds,buildrelationships,andfoster endednatureoffree-formconversations,itisdesirabletorepeat
trust[13],ratherthansimplypresentingsuitableassets. eachexperimentwithdifferentpeoplesuchthatwecanobserve
Reflectingonthesefindings,thedevelopmentofconversational variancesinconversationpaths,asthosevariancesmayinfluence
financialadvisorshasdrawnincreasingattention,asitenablesa tasksuccess.However,toenablerepeatability,weneedtoholdthe
dynamicunderstandingofusers’needs,personalizedguidance,and investorneedsconstantacrossrepetitions.Hence,wedefinethree
thepotentialtobuildtrustworthyrelationships[9,16,34,43].Inpar- archetypalinvestorprofiles𝑖 ∈𝐼 basedoninputfromafinancial
ticular,theconversationalagents’personalityhasgainedattention expert,whereourhumanparticipantsaregivenonetofollowwhen
asafactorthatcanhelpbuildrelationshipswithclientsandfoster conversingwiththeLLM-advisor:
trust[18],especiallygiventhesuccessesofconversationalagents
• Investor1:Growth-OrientedHealthcareEnthusiast:
usingtheBigFivepersonalitymodel[20]toenhancetheend-user
Prefershealthcareinnovations,valueshigh-growthopportu-
experience[4,30].Althoughconversationalagentsshowpotential
nities,andtakesmeasuredrisks.
infinance,howtoconfigurethemtomatchthevalueofhuman
• Investor2:ConservativeIncomeSeeker:Seeksstable
advisorsremainsunclear.Therefore,weconductauserstudyto
returns,investsinwell-establishedcompanies,valuesregular
examinehowpersonalizinginvestmentguidanceandtheadvisor’s
dividendpayouts.
personalityshapeusers’financialdecision-makingeffectiveness
• Investor3:Risk-takingValueInvestor:Targetsunder-
andoveralluserexperience.
valuedcompanieswithstronglong-termpotential,tolerates
short-termvolatility,andinvestsincyclicalsectors.
3 Methodology
Foreachoftheseinvestorprofiles,weselectthreekeyinvestment
Inthispaperweaimtodeterminetowhatextentcurrentgenerative
preferences,chosenfromwell-knowninvestmentcharacteristics
languagemodelscanactasaneffectivefinancialadvisor.Indeed,
suchasindustrysector,stockstyle,consistencyindividendpay-
giventheneedtopersonalizefortheuser,emotionalimplications,
ments,andsensitivitytoglobalmarketchanges[8].Wedenote
the technical nature of the information-seeking task, and high thesetofinvestorpreferencesas𝑖𝑝𝑟𝑒𝑓
.Inourexperiments,we
impact if failed, we argue that this is an excellent test case for
simulatearealisticelicitationscenariowheretheadvisorcollects
thelimitsofgenerativelargelanguagemodels.Tostructureour
thepreferencesfromtheparticipants.Therefore,wedonotstraight-
evaluation,wedivideourstudyintotwophases,asillustratedin
forwardlyprovidethepreferencestotheparticipants.Instead,we
Figure1,whereweevaluatethesuccessofboth:
presentthemastextnarrativesofbetween150to200words.A
(1) PreferenceElicitation:Duringthisstage,wehavetheLLM- financialexpertwasconsultedtoconfirmthequalityandreliability
advisorholdanaturallanguageconversationwithahuman, ofthesenarratives.AnexamplenarrativerepresentingInvestor2is
whereitisdirectedtocollectinformationregardingtheper- illustratedinFigure2,wherewehighlightthesentencesreferring
son’sinvestmentpreferences.Thehumaninthisinteraction tospecificinvestorpreferences.
ispretendingtohavepreferencesfromagiveninvestorpro-
file. 3.2 Stage1:PreferenceElicitation
(2) AdvisoryDiscussion:Duringtheadvisorydiscussion,the
Thegoalofstage1ofourstudyistodeterminetowhatextentan
LLM-advisoragainhasanaturallanguageconversationwith
LLM-advisorcaneffectivelycollectauser’sinvestmentpreferences
thehuman(actingonaninvestorprofile),wherethehuman
through conversation. Formally, given a participant of the user
collectsinformationaboutwhetheracompanyisasuitable
study𝑢andaninvestorprofile𝑖,duringtheelicitationstage,the
investmentforthem.Thisisrepeatedformultiplecompanies
LLM-advisoraimstoobtainanapproximatedsetofpreferences,
perinvestorprofile. denoted𝑖 𝑢 𝐿𝐿𝑀 ,thatmatchestheinvestorpreferences(𝑖𝑝𝑟𝑒𝑓 ).To
Weprovidepreparatoryinformationanddiscusseachstageinmore achievethis,thegenerativemodelproducesaseriesofquestions
detailbelow: that participants answer by interpreting the investor narrative.
288

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
| R e sp o n s e | s t o t h o s e q    | u e st i o n s, d en o | t e d a s𝑅 𝑢 , | a r e u se d b y th e L L M - |     |                      |                         |                           |
| -------------- | -------------------- | ---------------------- | -------------- | ----------------------------- | --- | -------------------- | ----------------------- | ------------------------- |
|                |                      |                        | 𝑖              |                               |     | Participant Training |                         |                           |
|                |                      | 𝑖                      | 𝐿 𝐿 𝑀          |                               |     |                      | Stag e  2 :   A d v i s | o r y  D is c u s s i o n |
| ad v is o r t  | o g e n e r a te t h | e u s e r p ro fi le   | 𝑢 . Su c c     | e s s is th e n m e as u r ed |     |                      |                         |                           |
bymanuallyevaluatingtheoverlapbetween𝑖𝑝𝑟𝑒𝑓 𝐿𝐿𝑀 Y o u   m i g h t  w a n t  to  i nv e s t  i n
|     |     |     |     | and𝑖 . |     | Investor Profile Allocation | tessa hcae roftaepeR Amazon Inc, it is a large…. |     |
| --- | --- | --- | --- | ------ | --- | --------------------------- | ------------------------------------------------ | --- |
𝑢
For user elicitation, we adopted a System-Ask-User-Respond Why this company?
|     |     |     |     |     |     | Stage 1: Preference Elicitation | Amazon has a dominant  |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | ---------------------- | --- |
(SAUR)paradigm[42].Duringtheconversation,theadvisorproac- Before we start investing, I  market share in online shop…
|     |     |     |     |     |     | need to get to know about you | How profitable has it been in  |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | ------------------------------ | --- |
tivelyinquiresabouttheuser’spreferencesgivenasetoftarget the last 3 years?
Have you invested before?
preferences(e.g.,industrytype,acceptablerisk).Afterthehuman gnisilanosrep fI The stock price has increased
|     |     |     |     |     |     | No, I am a new investor | by 67% and has a Sharpe Ra.. |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | ---------------------------- | --- |
participantrespondstoaquestion,theLLM-advisorcheckswhether Explain Sharpe Ratio?
How long are you looking to
thecollectedpreferencescoverallofthetargetpreferences.Ifthead- invest for? Sharp Ratio is a combined
|                                                            |     |     |     |     |     | I am saving for a house, so    | profitability and risk metric.. |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------ | ------------------------------- | --- |
| visorisconfidentthattheydo,itendstheconversationandprompts |     |     |     |     |     | maybe 5 years?                 |                                 |     |
|                                                            |     |     |     |     |     | How adverse are you to taking  | Asset Ranking and Feedback      |     |
theusertoproceedtothenextstage;otherwise,itcontinuesasking risks with your money?
|                            |     |     |     |     |     | Is investment risky? What are  |                                | If all assets rated… |
| -------------------------- | --- | --- | --- | --- | --- | ------------------------------ | ------------------------------ | -------------------- |
| follow-upquestionsinaloop. |     |     |     |     |     |                                | Repeat for second LLM-Advisor  |                      |
|                            |     |     |     |     |     | the risks I should consider?   | variant  (go-to       )        |                      |
Different investment
|     |     |     |     |     |     | strategies come with…. |     | If both conditions tested… |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | -------------------------- |
3.3 Stage2:AdvisoryDiscussion
Exit Questionnaire
Response Summarization
Stage2ofourstudyinvestigatestowhatextentanLLM-advisorcan
providethesamebenefitsasarealhumanadvisorwhenexploring
investmentoptions.NotethatthegoalhereisnottohavetheLLM-
Figure3:Userstudystructure.
advisorpromoteanyoneasset,butrathertoprovideaccurateand
Theadvisorusingthispromptactsasourbaselinefortheadvisory
| meaningful | information | such that | the human | can find the best |     |     |     |     |
| ---------- | ----------- | --------- | --------- | ----------------- | --- | --- | --- | --- |
discussionstudy.Weaugmentthisbaselinewithadditionalcontext
investmentopportunityforthem.Tothisend,westructureour
andinstructionstoformtwoadditionalexperimentalscenarios,
experimentsuchthatthehuman(actingonaninvestorprofile)has
discussedbelow:
oneconversationwiththeLLM-advisorforeachofasetofassets
beingconsidered.1Afterallassetsarepresentedtotheparticipant,
+Personalization:Asdiscussedearlier,oneofthecorerolesofthe
astockrankingisgeneratedbysortingthestocksbytheparticipant financialadvisoristopersonalizetotheindividualcustomer,based
ratingindescendingorder. ontheirfinancialsituation,needs,andpreferences.Toenablethe
Importantly,asweknowtheinvestorprofile𝑖𝑝𝑟𝑒𝑓
|     |     |     |     | foreachcon- | LLM-advisortopersonalizefortheuser,weintegratethegener- |     |     |     |
| --- | --- | --- | --- | ----------- | ------------------------------------------------------- | --- | --- | --- |
versationaboutanasset𝑎,wecanobjectivelydeterminewhether𝑎 atedprofilefromthepreferenceelicitation(Stage1)𝑖 𝐿𝐿𝑀
𝑢 intothe
isagoodinvestmentgiven𝑖𝑝𝑟𝑒𝑓
,formingagroundtruthagainst prompt.Werepresenteachpreferenceasaseriesofshortsentences.
whichwecancomparetotheratingprovidedbyourhumanpar-
+Personality:InSection2.2wediscussedhowhumanfinancial
ticipantaftertheirconversationwiththeLLM-advisor.Foreach
|                                                   |     |     |     |     | advisors | provide emotional support | as well as | financial advice. |
| ------------------------------------------------- | --- | --- | --- | --- | -------- | ------------------------- | ---------- | ----------------- |
| asset𝑎,afinancialexpertproducedascorebetween0and3 |     |     |     | by  |          |                           |            |                   |
manuallycheckingwhether𝑎satisfiedeachofthethreeinvestment WhileitisunlikelythatanLLM-advisorcoulddothisaswellasa
criteriacontainedin𝑖𝑝𝑟𝑒𝑓 human(itlacksbothemotionalintelligenceandnon-conversational
.Aground-truthrankingwasproduced
cluestothecustomer’smentalstate[38]),itmightbepossibleto
bysortingtheassetsbytheexpertscores.Weshowanexample
provideabetterend-userexperiencebydirectingtheLLM-advisor
| of the ranking | construction | in Figure | 2. During | evaluation, the |     |     |     |     |
| -------------- | ------------ | --------- | --------- | --------------- | --- | --- | --- | --- |
toadoptapersonality.AsnotedinSection2itispossibletodothis
closertheparticipantrankingistotherankingproducedbyexpert
viapromptengineering,suchasinstructingtheLLMtotakeonthe
judgments,thebettertheLLM-advisorperformed.
traitsofoneormoreoftheBig-Fivepersonalitytypes[20].
BaselinePrompt:AsweareworkingwithanLLM-advisorand Asweareperformingauserstudywithhumans,itwouldbe
thenatureoffinancialinformation-seekingistime-sensitive,we impracticaltoexhaustivelytesteverycombinationofpersonality
needtoprovideanyinformationthatmightchangeovertimetothe types,henceasaninitialinvestigationweexperimentwithtwo
LLMwithintheprompt.Assuch,foreachasset𝑎,wepre-prepared distinctpersonalityprofiles[29]:
astandardassetdescriptorblockafterconsultingwithafinancial • Extroverted:Highinextroversion,agreeableness,andopen-
expert,containing: ness;lowinconscientiousnessandneuroticism.
| • StockPrices:Wecollectmonthlystockpricesfrom2023 |     |     |     |     | •   |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Conscientious:Lowinextroversion,agreeableness,and
usingYahoo!Finance.2
openness;highinconscientiousnessandneuroticism.
• BusinessSummary:Wegathereachcompany’sbusiness WeadoptedthepromptingmethodfromJiangetal.(2024)to
overviewfromYahoo!Finance.
assignaBigFivepersonalitytraittotheLLMagent[12],choos-
• RecentPerformanceandKeyFinancialIndicators(e.g.,
ingitforitssimplicityandeffectivenessamongvariousproposed
EPS):Weobtainearningsconferencecalltranscripts3from
approachesforembeddingpersonalityinLLMs(includingboth
SeekingAlphaforthelastquarterof2023. promptingandfine-tuning)[11,12,28].Toensureahighstandard
ofprofessionalismandaccuraterepresentationoftheintendedper-
1Theseweremanuallyselected,howeverinaproductionenvironmentthesemightbe
producedbyanassetrecommendationsystem. sonality,weconsultedfinancialprofessionalstoreviewthetexts
2ThescenarioforthefinancialadvisingofouruserstudyissettoDecember30,
generatedbyLLMsadoptingbothpersonas.
2023.Bybasingourexperimentattheendof2023,weavoidtheproblemofdata
contamination[25].
3Earningsconferencecalls,hostedbypubliclytradedcompanies,discusskeyaspects transcriptscoversignificantfinancialindicatorsandprovideexplanationsofrecent
performance.
oftheirearningsreportsandfuturegoalswithfinancialanalystsandinvestors,thus
coveringcriticalfinancialindicatorsandrecentperformanceinsights[21].These
289

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
3.4 ExperimentalDesign Table1:Operationaldefinitionsusedintheadvisorassess-
mentquestionnaireforallresponsedimensions.
Inourexperiment,weconductedtwostudies:apersonalization
study(forRQ2)andanadvisorpersonastudy(forRQ3).Inthe
personalizationstudy,participantscomparedanon-personalized ResponseDimension OperationalDefinition
(Baseline)advisorwithapersonalized(+Personalized)version.In PerceivedPersonalization[14] Theadvisorunderstandsmyneeds.
EmotionalTrust[14] Ifeelcontentaboutrelyingonthisadvisorformydecisions.
theadvisorpersonastudy,theycompareddifferentLLM-advisor
TrustinCompetence[14] Theadvisorhasgoodknowledgeofthestock.
personalitytypes(+Extrovertedvs.+Conscientious).Participants
Iamwillingtousethisadvisorasanaidtohelpwithmy
arerandomlyassignedtooneofthesetwostudies. IntentiontoUse[14] decisionaboutwhichstocktopurchase.
Figure3showsthestructureofouruserstudyforasinglepar- PerceivedUsefulness[22] Theadvisorgavemegoodsuggestions.
ticipant,comprisingsevensteps: OverallSatisfaction[22] Overall,Iamsatisfiedwiththeadvisor.
InformationProvision[37] Theadvisorprovidesthefinancialknowledgeneeded.
(1) ParticipantTraining:Participantsaregivenageneraloverview
In our experiments, we use Llama-3.1 8B as the background
oftheuserstudyandgiveninstructionsontheirexpected
modelforallourLLM-advisorvariants.4
rolesduringpreferenceelicitation,advisorydiscussions,as-
setranking,andadvisorassessment.
3.5 Participants
(2) InvestorProfileAllocation:Theuser𝑢israndomlyallo-
catedoneoftheinvestorprofiles(SeeSection3.1)thatthey Werecruited64participantsfromtheauthors’affiliateduniversity
willfollow.Eachprofileisassignedto42participants. forourstudy:32participantsforthepersonalizationstudyand32
(3) PreferenceElicitation(Stage1):Theparticipantinteracts participantsfortheadvisorpersonastudy,utilizingtheuniversity’s
withtheLLM-advisorasiftheywereanewinvestor.The onlineplatformandblackboardforrecruitment.Participantswere
conversationendsoncetheLLM-advisordeterminesthat requiredtobefluentinEnglish,over18yearsold,andhaveanin-
they know enough about the investor to personalize for terestinfinanceandinvestment,mirroringthetargetdemographic
them.Themediantimespentonpreferenceelicitationwas ofoursystem’susers.Afterexcludinginvaliddata,29participants
5minutesand11seconds. remainedinthepersonalizationstudyand31intheadvisorpersona
(4) ResponseSummarization:Giventheaggregatorofuser study.WeconductedapoweranalysisusingtheWilcoxonsigned-
responses𝑅 𝑖 𝑢 ,weinstructanLLMtogenerateaninvestor ranktestformatchedpairs,withtheexperimentalconditionsas
profile𝑖 𝑢 𝐿𝐿𝑀 .Foreachinvestorpreferencein𝑖𝑝𝑟𝑒𝑓 ,ifthereis theindependentvariableandusers’responsetotheadvisorassess-
anyrelevantinformationintheresponses𝑅 𝑖 𝑢 ,thatinforma- mentquestionnaireasthedependentvariable[26].Theanalysis
tionisincludedin𝑖 𝑢 𝐿𝐿𝑀 .Otherwise,𝑖 𝑢 𝐿𝐿𝑀 indicatesthatno determinedthat29participantsareneededtoobserveastatistically
significanteffectonuser-perceivedquality.Ourrecruitmentcri-
relevantinformationisavailableforthatspecificpreference.
teriaandcompensation(£10/hour)forapproximatelyonehourof
(5) AdvisoryDiscussion(Stage2):Tosimplifytheconversa-
participationwereapprovedbyourorganization’sethicalboard.
tionflowwehavetheparticipantholdseparateconversations
withtheLLM-advisorforeachassettheymightinvestin.
4 EvaluationMetricsandStatistics
TheLLM-advisorisprovidedwithcontextaboutthecurrent
asset (see Section 3.3), and depending on the experimen- Inthissectionwediscusshowwequantifyeffectivenessforthe
talscenario,optionallypersonalizationinformation(step4 preferenceelicitationandadvisorydiscussionstages,respectively,
output)and/oratargetpersonalitycontextstatement.Each inadditiontosummarizingdatasetstatisticsforeach.
conversationcontinuesuntiltheuserissatisfiedthatthey
4.1 PreferenceElicitationMetrics(Stage1)
have enough information to rate the asset. The order in
whichtheassetsarediscussedisrandomlyassignedtoavoid To evaluate the quality of the first preference elicitation stage,
positionbias. wewanttomeasurehowwelltheLLM-advisorhascapturedthe
(6) AssetRankingandFeedback:Participantsrankallthe investorpreferencesasdefinedintheinvestorprofile𝑖 (seeSec-
stocks(fourintotal)discussedintheadvisorysessionac- tion3.1).Eachinvestorprofile𝑖 ∈ 𝐼 defineskeyfeaturesofthe
cordingtotheirdesiretoinvestineach.Theyalsoassessthe investor,suchaspreferringhigh-growthstocks,orfavoringregu-
advisortheyinteractedwithusinga7-pointLikertscalefor larpayouts,denoted𝑖𝑝𝑟𝑒𝑓 .Wehavethreeinvestorprofiles(|𝐼|=3),
theitemslistedinTable1(seeSection4). with10(𝑛)participantsperformingelicitationon𝑖 𝑢 𝐿𝐿𝑀 foreach
profileandeachLLMvariant,i.e.thereare120elicitationattempts
Toenablemoreeffectivepair-wisecomparisonofLLM-advisorvari- intotal,with30attemptsperLLM-advisorvariant.Followingthe
ants,wehaveeachparticipanttesttwovariantsperstudy.Ifthe notationinSection3,𝑖 𝑢 𝐿𝐿𝑀 inthiscasedenotesasimilarlistoffea-
userhasonlytestedonevariantatthispoint,thentheyrepeatthe turesto𝑖𝑝𝑟𝑒𝑓 thatLLM-advisorlearnedabouttheinvestorduring
userstudy(startingatstep2)withthesecondvariant.Theorderin conversationwithaparticipant𝑢,whichwederivefromamanual
whichparticipantsexperienceeachvariantisrandomlyassigned. analysisoftheelicitationoutput(i.e.whatisproducedbyresponse
summarization).Intuitively,thecloserthefeaturesproducedfrom
(7) ExitQuestionnaire:OnceapairofLLM-advisorvariants
4FurtherdetailsabouttheLLMconfiguration,investornarratives,relevantscores,
havebeentested,theuserfillsinanexitquestionnairethat
promptsandscriptsfordataanalysiscanbeaccessedatthefollowingrepository:
isdesignedtoasktheoverallexperienceintheuserstudy. https://github.com/TTsamurai/LLMAdvisor_supplementary
290

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
Table2:Generalstatisticsofthecollectedconversationdata. Table3:Stage1-ComparisonofElicitationAccuracyofan
expertvs.differentLLM-advisorsforeachinvestorprofile.
Participants 60 Thebestadvisorishighlightedinbold.Arrowsdenoteper-
| TimePeriod | 2024/10/24~2024/11/7 |     |     |     |     |     |
| ---------- | -------------------- | --- | --- | --- | --- | --- |
centageincreases(↑)ordecreases(↓)comparedtotheexpert.
| TotalTurns                   |     | 10,008 |                 |        |               |         |
| ---------------------------- | --- | ------ | --------------- | ------ | ------------- | ------- |
| Stage1:PreferenceElicitation |     |        |                 |        | LLM-Advisors  |         |
| TotalTurns                   |     | 1,788  | InvestorProfile | Expert |               |         |
| NumberofSessions             |     | 120    |                 | LLM    | +Extr. +Cons. | Average |
Avg.Turns/Session 15.8
|                    |     |     | Growth-Oriented     |           | 0.80      | 0.78→0.0% |
| ------------------ | --- | --- | ------------------- | --------- | --------- | --------- |
| Avg.UserWords/Turn |     | 9.8 |                     | 0.78 0.76 | 0.79      |           |
|                    |     |     | Conservative-Income | 0.89 0.82 | 0.75 0.87 | 0.82↓7.8% |
Stage2:AdvisoryDiscussion
|     |     |     | Risk-Taking | 0.89 0.48 | 0.60 0.55 | 0.53↓40.5% |
| --- | --- | --- | ----------- | --------- | --------- | ---------- |
TotalTurns 8,220
0.70↓17.6%
| NumberofSessions |     | 480 | Average | 0.85 0.69 | 0.70 0.73 |     |
| ---------------- | --- | --- | ------- | --------- | --------- | --- |
Avg.Turns/Session 18.2
Avg.UserWords/Turn 13.0 asession,e.g.duringStage1,therewere3investorprofiles*10
anyelicitationattempt𝑖 𝐿𝐿𝑀 isto𝑖𝑝𝑟𝑒𝑓 participants*4LLM-advisors,resultingin120sessions.Stage2has
𝑢 ,thebettertheLLM-advisor
isperforming.Tothisend,wereportelicitationaccuracyforeach 4xthenumberofsessions,astherearefourassetsassociatedwith
eachprofile(𝐴
| investorprofile,calculatedas: |     |     | 𝑖)todiscusswiththeLLM-advisor. |     |     |     |
| ----------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
(cid:12) (cid:12) FromTable2weobservethatincontrasttootherconversational
|     | 𝑛 (cid:12)𝑖𝐿𝐿𝑀 | ∩𝑖𝑝𝑟𝑒𝑓(cid:12) |     |     |     |     |
| --- | -------------- | -------------- | --- | --- | --- | --- |
1∑︁(cid:12) 𝑗 (cid:12) tasks [35, 36], financial information-seeking appears to require
ElicitationAccuracy(𝑖)= (1)
𝑛 (cid:12)𝑖𝑝𝑟𝑒𝑓(cid:12) moreextendedinteractions.Onaverage,preferenceelicitationin-
|     | 𝑗=1 | (cid:12) (cid:12) |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- |
HumanAdvisor:Toprovideapointofcomparison,wealsocon- volves15turnspersessionwith9.8wordsperturn,whereasadvi-
sorydiscussionsinvolve18turnspersessionwith13.0wordsper
ductapreferenceelicitationwithafinancialexpertusingthesame
turn,highlightingtheoverallcomplexityofthetask.
promptandinstructionsastheLLM.Thisallowsustoevaluate
howcloseLLMsaretoapaidhumanadvisorundertakingthesame
5 Results
task.Morespecifically,foreachinvestorprofile,threeparticipants
engagedwiththisexpert,whothenproducedasetofpreferences Inthiswork,weexplorehowtodesignconversationalfinancialadvi-
𝐸𝑥𝑝𝑒𝑟𝑡 𝐿𝐿𝑀 sorsthatenhancebothdecision-makingandpositiveexperience.To
| 𝑖 𝑢 ,whichcanbeusedinsteadof𝑖 | 𝑢 inEquation1. |     |     |     |     |     |
| ----------------------------- | -------------- | --- | --- | --- | --- | --- |
achievethis,ouruserstudyisguidedby3coreresearchquestions.
4.2 AdvisoryEffectivenessMetrics(Stage2) • RQ1:CanLLM-advisorseffectivelyelicituserpreferences
throughconversation?
Rankingcorrelation(Spearman’sRho):Inthesecondstage,
weevaluatehowwelltheLLM-advisorcansupportaninvestorto • RQ2:Doespersonalizationleadtobetterdecisionsandmore
selectfinancialassetsthataresuitableforthemtoinvestin.Recall positiveadvisorassessment?
• RQ3:Dodifferentpersonalitytraitsaffectdecisionquality
fromFigure3thatafteraparticipantfinishesdiscussingallassets
withtheLLM-advisor,theyrankthoseassets𝑎∈𝐴 andadvisorassessment?
𝑖 basedonthe
| likelihoodtheywillinvestineach,i.e.eachparticipant𝑢 |     | acting |     |     |     |     |
| --------------------------------------------------- | --- | ------ | --- | --- | --- | --- |
onaprofile𝑖wehaveanassetranking𝑅(𝐴 𝑖 ,𝑖 𝑢).Asillustratedin 5.1 RQ1:Elicitationaccuracy
Figure2,eachinvestorprofile𝑖wasderivedfromagroundtruth
WebeginbyexamininghoweffectivetheLLM-advisorsareatiden-
setofinvestorpreferences𝑖𝑝𝑟𝑒𝑓
,whichanexpertusedtocreate tifying investment preferences during conversations in Stage 1.
| agroundtruthranking𝑅(𝐴 ,𝑖𝑝𝑟𝑒𝑓),i.e.the“correct”rankingof |     |     |                                                          |     |     |     |
| -------------------------------------------------------- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
| 𝑖                                                        |     |     | ElicitationAccuracyistheprimarymetric,wherewecontrastthe |     |     |     |
,𝑖𝑝𝑟𝑒𝑓),thebet-
| assets.Intuitivelythecloserthe𝑅(𝐴 | 𝑖 ,𝑖 𝑢)isto𝑅(𝐴 | 𝑖   |     |     |     |     |
| --------------------------------- | -------------- | --- | --- | --- | --- | --- |
meanaccuracyacross10sessionsincomparisontoahumanexpert
tertheadvisorisperforming,astheparticipantwasbetterableto
tacklingthesametask(seeSection4.1).Table3reportselicitation
distinguishsuitableassetsvs.unsuitableones.Hence,toevaluate accuracyforeachLLM-advisorandtheHumanExpertacrossinvest-
theeffectivenessoftheadvisorytask,wereportthemeanranking mentprofiles.Arrowsdenotepercentageincreases(↑)ordecreases
,𝑖𝑝𝑟𝑒𝑓)
correlation(Spearman’sRho)between𝑅(𝐴 𝑖 ,𝑖 𝑢) and𝑅(𝐴 𝑖 (↓)oftheLLM-advisorcomparedtotheexpert.
acrossparticipants𝑢foreachLLM-advisor. Tosetexpectations,wefirstconsidertheperformanceofthe
expertinthefirstcolumninTable3,aswemightexpect,theex-
AdvisorAssessmentQuestionnaire:Lastly,wealsogatherqual-
pertmaintainsconsistentlyhighperformanceacrossallprofiles,
itativedatafromeachparticipantviaaquestionnaire.Inparticular,
averaging85%accuracy(randomaccuracyis50%).Thisformsan
afterrankingassetseachparticipant,reportshowtheyfeelthe
expectationoftheperformanceceilingforthetask.
LLM-advisorperformedintermsof7dimensions,listedinTable1,
Next,wecomparetheexpertperformancetoeachLLM-advisor.
suchasperceivedusefulness,trust,andusersatisfaction.Weuse
Fromtheperspectiveofpreferenceelicitation,therearethreeLLM-
thisdatalatertoevaluatehowsensitivetheuseristodifferencesin
advisorconfigurations,thosethatuseonlytheBaselinePrompt(de-
theLLM-advisor.
notedLLM)fromthepersonalizationstudy,andthosethatinclude
adefinedpersonality(eitherextroverted,+Extr.,orconscientious,
4.3 DatasetStatistics
+Cons.)fromtheadvisorpersonastudy.5FromTable3,weobserve
Table2summarizesthestatisticsofthedatacollectedduringthe
twostagesofouruserstudy.Eachconversationthataparticipant 5Notewecannothaveapersonalizedvarianthere,asthepersonalizationevidenceis
| hadwithanLLM-advisorineitherstage1or2isreferredtoas |     |     | derivedfromthisstage. |     |     |     |
| --------------------------------------------------- | --- | --- | --------------------- | --- | --- | --- |
291

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
thattheLLM-advisor’sperformanceisgenerallystrongforgrowth- Table4:Investordecision-makingeffectiveness,expressed
oriented,andconservative-incomeinvestors(withaccuracyaround astheSpearman’sRhocorrelationbetweentheinvestor’s
80%)onaverage,whichissimilartothehumanadvisor.However, assetrankingandtheexpertassetranking(higherisbetter).
fortherisk-takinginvestorprofile,theLLM-advisor’selicitation
†indicatesstatisticalimprovements(Welch’st-testwith𝑝 <
accuracywassubstantiallylower(-40.5%). 0.05)overthenotpersonalizedbaseline,while§ indicates
Fromamanualfailureanalysis,weobservedthefollowingtrends significant differences between cases with successful and
thatcontributetotheperformancegapwiththehumanadvisor, unsuccessfulpreferenceelicitations.
particularlyfortherisk-takingprofile.First,itisnotablethatelici-
AdvisorConfig Investorvs.Expert(Spearman’sRho)
tationfailurescanoriginatefromtheinvestor(participant)rather
thantheLLM.Recallthatoneoftheaspectsthatmakesfinance Personalization Personality All PreferenceElicitation
Successful Unsuccessful
morechallengingthandomainslikemovierecommendationisthat
Baseline None 0.110 – –
the“user”isinexpert,andsomaygiveincorrectinformationduring
+Personalized None 0.310 0.481†§ -0.228
theconversation.Indeed,weobservedcaseswheretheparticipant +Personalized +Extroverted 0.122 0.243§ -0.286
confusedconceptssuchasthedifferencebetweenagrowthanda +Personalized +Conscientious 0.26 0.365 -0.025
valuestock,aswellascyclical/non-cyclicalassets.Ontheotherside,
baselineadvisoryperformanceislow,withonlyaveryweakpos-
preferencehallucinationisacoreissuefortheLLM-advisor.The
itivecorrelationtothegroundtruthrankingof0.11.Thisindicates
LLMisaprobabilistictokengeneratorconditionedonthebaseline
thatwithoutfurtherevidence,theLLMisnotabletomeaningfully
promptandpriorconversation,andasaresult,insomescenarios,
guidetheinvestor.
thecontextualcontentcanoverrideastatementbytheinvestor.
Thistypeoferrorismorelikelywhentheinvestorisunsurein 5.2.2 PersonalizedDecision-makingEffectiveness: Havingestab-
theirresponsesorwhentheyprovidecontradictorystatements. lishedourbaseline,wenowexaminetheimpactthataddingthe
Forinstance,aninvestorexpressinganinterestintheconsumer investorpreferencescollectedduringstage1has,comparingTable4
discretionarysectorwhilesimultaneouslyoptingfornon-cyclical row1(baseline)torow2(personalized).Asweanticipated,person-
stocks,despiteconsumerdiscretionarybeinginherentlycyclical. alizationisbeneficial,withinvestordecision-makingeffectiveness
increasingfrom0.11to0.31(averageSpearman’sRhocorrelation
ToanswerRQ1,ourresultsdemonstratethatLLM-advisor’sare
totheexpertranking).However,thiscorrelationisstillweak,illus-
abletoelicitpreferencesfromauserviaconversationandthatfor
tratingthatwhilediscussingassetswiththeLLM-advisorisbetter
2/3’softheuserprofilestested,elicitationaccuracywasconsistently
thannohelpatall,ourparticipantsarestillstrugglingtoevaluate
equivalentorclosetothatofanexperthumanadvisor.However,
thesuitabilityoffinancialassets.
weobservedaclearfailuremodewhentestingtherisk-takingpro-
Thiscorrelationisanaverageoveralltheparticipantsintheuser
file,wheremisunderstandingsbytheinvestorsandhallucinations
study,regardlessofhoweffectivetheirpreferenceelicitationwasin
withintheLLMcompoundtoresultinaccuracythatisclosetoran-
stage1.Hence,wemightaskwhetherthelowcorrelationisdueto
dom.Overall,weconsiderthisapromisingresult,asthemajority
theLLM-advisorbeingconfusedbypoorpreferenceelicitationdata.
ofthetimeitiseffective,andthefailuremodeobservedmightbe
Toexplorethis,Table4alsoreportsinvestordecision-makingeffec-
rectifiedbybettercontextcraftingandtheadditionofcontradiction
tivenessstratifiedbasedonwhetherstage1wassuccessful(column
detection;bothdirectionsforfutureresearch.
4)ornot(column5).6Asexpected,weseeastatisticallysignificant
increaseininvestordecision-makingeffectivenesswhenprefer-
5.2 RQ2:Effectivenessofpersonalization
enceelicitationwassuccessfulwhencomparedtonon-personalized
Havingshownthatautomaticpreferenceelicitationispossible,we sessions(0.481vs.0.110).Moreconcerningly,wealsoseetheLLM-
nowexaminestage2ofourstudy,namelytheadvisorydiscussions. advisorhasastrongnegativeinfluenceontheinvestors’decision-
Giventheinherentlypersonalizednatureoffinancialadvice,we makingcapabilityifpreferenceelicitationfails,asillustratedby
expectthatthecustomerpreferencesobtainedduringstage1will thenegativecorrelationswiththeexpertincolumn5.Thisresult
bekeytoenablingLLM-advisorstoprovideeffectiveinvestment highlightsboththateffectivepreferenceelicitationiscrucial,but
advice.Hence,inthissection,wecomparetheperformanceofan alsothattheLLM-advisorcaneasilyinfluencetheinvestorinto
LLM-advisorusingonlytheBaselinePrompttoonethatincludes makingpoordecisions,asthehumanisheavilyreliantontheagent
thepreferencesobtainedduringstage1(+Personalized).However, tonavigatetherelativelyunfamiliarfinancialinformationspace.
asweobservedthatpreferenceelicitationisnotalwayssuccessful,
5.2.3 ParticipantAssessmentoftheAdvisor: Sofarwehavedemon-
wealsoexaminewhateffectelicitationperformancehasonthe
stratedthatthereisalargedifferencebetweenanon-personalized
LLM-advisor.
LLM-advisorandapersonalizedone,intermsofhowtheycan
alterthedecision-makingoftheinvestor/participant.Butcanthe
5.2.1 Non-personalizedDecision-makingEffectiveness: Weinitially
participanttellthedifferencesbetweenthem?
establishhoweffectivetheLLM-advisoriswithoutanyinforma-
Table5reportstheaggregationofthequalitativedatawecol-
tionregardingtheinvestor.LLM-advisoreffectivenessismeasured
lectedfromeachparticipantaftertheyfinishedinteractingwith
basedonhowwelltheinvestorwasabletoranktheassetsdiscussed
each LLM-advisor in terms of 7 dimensions, where we start by
bysuitabilitytothem.TheprimarymetricisaverageSpearman’s
Rhocorrelationbetweentheinvestorrankingandthegroundtruth
6Wedefinethatanelicitationsessionissuccessfulifmorethan50%oftheinvestor’s
ranking(seeSection4.2),reportedinTable4row1.Asweexpect, preferenceswerecorrectlycaptured
292

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
Table5:Averageparticipantusers’responsetoadvisorassessmentquestionnaireunderdifferentadvisorconditions.Columns
labeledwithadvisorcondition(Baseline,+Pers.,+Cons.,+Extr.)containa7-pointLikertscale(higherisbetter).“p”column
containsWilcoxonsigned-ranktestp-valuesfor(RQ2)Baselinevs.+Personalized(Pers.),and(RQ3)+Conscientious(Cons.)vs.
+Extroverted(Extr),forboththefulldata(All)andthesubsetwheretheelicitationaccuracyisabove0.5.“SuccessfulElicitation”
referstothesubsetwhereelicitationaccuracywas≥0.5.ForRQ2,thissubsetconsistsofpairsforwhich+Perselicitationis
successful,whileforRQ3,itconsistsofpairsforwhichboth+Extrand+Conselicitationaresuccessful.Boldfaceindicates
significanteffectswith†for𝑝 <0.1and‡for𝑝 <0.05.
(RQ2)Baselinevs.+Personalized (RQ3)+Conscientiousvs.+Extroverted
All SuccessfulElicitation All SuccessfulElicitation
ResponseDimension Baseline +Pers. p Baseline +Pers. p +Cons. +Extr. p +Cons. +Extr. p
PerceivedPersonalization 5.759 5.724 0.838 5.762 5.905 0.751 5.500 5.500 0.663 5.588 5.706 0.941
EmotionalTrust 5.103 5.241 0.446 5.143 5.333 0.537 5.038 5.154 0.600 4.706 5.235 0.034‡
TrustinCompetence 5.690 5.690 0.817 5.810 5.857 0.782 5.962 6.077 0.538 6.000 6.000 1.000
IntentiontoUse 5.310 5.483 0.505 5.429 5.714 0.166 4.885 5.462 0.005‡ 4.941 5.588 0.013‡
PerceivedUsefulness 5.241 5.517 0.183 5.381 5.810 0.194 5.423 5.538 0.425 5.176 5.118 0.968
OverallSatisfaction 5.345 5.690 0.116 5.429 5.810 0.098† 5.269 5.577 0.179 5.118 5.529 0.244
InformationProvision 5.517 5.966 0.026‡ 5.714 6.143 0.053† 5.692 5.654 0.953 5.588 5.765 0.490
focusingontheRQ2-Allcolumns,i.e.comparingthebaselineand extrovertedpersonalityandaconscientiouspersonality.7While
personalizedvariants.Theimportantobservationtonotehereis wecouldconsiderthepersonalizedLLM-advisordiscussedinSec-
thattheparticipantpreferencescoresforbothvariantsarestatis- tion5.2asathirddistinctpersonality(thebaseLLMpersonality
ticallyindistinguishable,exceptunderthequalityofinformation oftheLLM),weshallnotcompareitwithourpersonality-injected
provisioncriteria.Thismeansthatourparticipantscannottellif models,becausedifferentsetsofparticipantswereusedintheper-
theLLM-advisorispersonalizingtothem,andtrusttheworseagent sonalizationstudyandtheadvisor-personastudy.
justasmuchasthebetterone.Furthermore,ifweconsiderthebest
casescenariowherethepreferenceelicitationwassuccessful(RQ2 5.3.1 Decision-makingEffectiveness: Wefirstexaminetheimpact
SuccessfulElicitationcolumns)weobservethesamepattern,even ofaddingpersonalitytotheadvisorsonthedecision-makingpro-
thoughthedifferencebetweenthebaselineandthepersonalized cess,bymeasuringthecapacityoftheparticipantstocorrectlyrank
variantsintermsoftheeffectithasontheparticipantdecision- theassets(aspreviouslydoneinSection5.2).Asaprimarymetric,
makingismorepronounced.Thisunderlinesoneofthecorerisks weagainusetheaverageSpearman’sRhocorrelationbetweenthe
ofusingLLM-advisorsinthefinancialdomain;sinceourusersare investorrankingandthegroundtruthrankingreportedinTable4
inherentlyinexperttheylackthefundamentalskillstojudgeto rows3(extrovertedadvisor)androw4(conscientiousadvisor).
whatextenttheLLMisprovidinggoodadvice,meaningthatthere Wefirstobservetheresultsforthefullsetofparticipantsin
isnosafetynetiftheLLMmakesamistake. theuserstudy.Interestingly,weobserveadifferencebetweenthe
twoadvisors,withtheconscientiousLLM-advisorprovidingbetter
ToanswerRQ2,ourresultsshowthatapersonalizedLLM-advisor guidancethantheextrovertedone(0.26vs.0.122).Thisobservation
isabletoprovideusefulfinancialadvicewhenithasaccuratein- isconsistentwhenwerestrictouranalysistothosecaseswherethe
formationregardingthepreferencesoftheinvestor.Thisisdemon- preferenceelicitationissuccessful.While,expectedly,theeffective-
stratedbybetterdecision-makingcapabilitybyparticipantsusing nessofbothadvisorsimproveswhentheelicitationissuccessful
thepersonalizedadvisorincomparisontothenon-personalizedone. (0.243vs.0.122inthecaseoftheextrovertedadvisorand0.365vs.
However,wealsoidentifiedtwoimportantchallengestoadoption. 0.26inthecaseoftheconscientiousone),theconscientiousadvisor
First,theimpacttheLLM-advisorhasisstronglytiedtothequality hasanadvantageovertheextrovertedone(0.365vs.0.26).
ofthepreferenceelicitationdataprovided,wherepoorpreference Theseresultshighlightthatprovidingdifferentpersonalitiesto
elicitationwillcausetheagenttoactivelydirecttheinvestortothe anLLM-advisorcannotablyimpactthecapacityoftheadvisorto
wrongassets.Second,whiletheparticipantswerepositiveregard- provideusefulinformationtotheinvestors.
ingtheLLM-advisorsacrossallquestionnairecriteria,theywere
notabletoconsistentlytellthedifferencebetweengoodandbadad- 5.3.2 ParticipantAssessmentoftheAdvisor: Wehaveobservedso
visors;leadingtoanincreasedriskofhumansactingonbadadvice. farthattheuseofdifferentpersonalitiesaffectstheuserdecision-
makingprocess.Buthowdothesepersonalitiesaffecttheperception
5.3 RQ3:Effectivenessofpersonalities thatusershaveoftheLLM-advisor?WeobservethisinTable5,in
termsofthesevendimensionscapturedduringtheadvisorassess-
OncewehaveconfirmedtheutilityofpersonalizationforLLM-
mentquestionnaire.
advisors,wenowstudytheeffectthatthepersonalityoftheadvisor
WefirstlookattheRQ3-Allcolumns,comparingthetwoper-
hasonusers’financialinformation-seeking.Aspreviousstudies
sonalities.Notably,forthemajorityofthedimensions,usersbarely
haveshown[29],chatbotpersonalitycanaffectthewayhumans
distinguishbetweenbothsystems.Theonlyanswerwhereweob-
interactwiththechatbot,andthereforeaffecttheeffectivenessand
serveastatisticallysignificantdifferenceistheintentiontousethe
perceptionofLLM-advisors.Tounderstandwhetherpersonality
affectsLLMfinancialadvisors,wecomparetwopersonalizedLLM-
advisorsonwhichwehaveinjectedapre-definedpersonality:an 7RefertoSection3.3forafulldescriptionofeachpersonality.
293

AreGenerativeAIAgentsEffectivePersonalizedFinancialAdvisors? SIGIR’25,July13–18,2025,Padua,Italy
systeminthefuture.Surprisingly,despiteprovidingworseguid- 0.035
ancetotheinvestor,participantsexpressedahigherinterestin 0.030
usingtheextrovertedadvisorthantheconscientiousone.Whenwe 0.025
limitourstudytothoseparticipantswhoexperiencedasuccessful 0.020
preferenceelicitationinbothadvisorvariants,thisissueisstressed, 0.015
asthoseusersalsodevelopasignificantlygreateremotionaltrust 0.010
withtheextrovertedadvisor.
0.005
Theseobservationsareworrisome,astheyrevealthattheper-
0.000 Positive Negative Uncertainty
sonalityofafinancialadvisorcannotonlyaffectthequalityofthe
advicebutalsoleadtheinvestorstotrustmoreonthosesystems
providingworseadvice.
5.3.3 Differencesinlanguage: Tofurtherunderstandhowperson-
alitiesaffectfinancialadvisory,weanalyzethedifferencesinthe
linguisticpatternsprovidedbyextrovertedandconscientiousad-
visors. Analyzingparticipants’reportedoverallexperiencefrom
theexitquestionnairesintheadvisorpersonastudy,over20%(7
of 31) described the extroverted advisor as clear, assertive, and
cheerful while perceiving the conscientious advisor as straight-
forward,analytical,yetlessconfident.8Therefore,toquantifythe
linguisticdifferencesintheadvisors,weconductafinancialsen-
timentanalysisoftheutterancesgeneratedbyeachadvisor.For
eachutterance,wecounttheoccurrencesofpositive,negative,and
uncertainwordsfromtheLoughranandMcDonaldFinancialSenti-
mentDictionary[19].Wenormalizethesecountsbythelengthof
thesentencesandaveragetheresultsacrossalldialogues.
Figure4showstheresults,showingtheextrovertedsentiment
scoresinblue,andtheconscientiousscoresinorange.Forthethree
sentimentdimensions,differencesbetweenadvisorsarestatisti-
cally significant (Welch’s t-test with𝑝 < 0.01). Figure 4 shows
thatextrovertedadvisorstendtousemorepositivelanguagein
their interactions, while conscientious advisors prefer negative
anduncertaintones.Throughmanualanalysisoftheconversation,
weobservethatthisresultsintheextrovertedadvisorfocusing
onthepositiveaspectsofinvestmentswhileoverlookingserious
drawbacks,whereastheconscientiousadvisorprovidesamorebal-
ancedviewoftheassets.Becauseofthis,participantsguidedby
conscientiousadvisorsmaymakemorewell-informedfinancialde-
cisions.Meanwhile,thepositivityoftheextrovertedadvisorseems
moreappreciatedbytheusers,whichisreflectedinhigheradvisor
assessmentscoresfromthepost-discussionquestionnaire.
ToanswerRQ3, ourresultsshowthatdifferentpersonalitiesof
apersonalizedLLM-advisorcanaffecttheutilityoftheprovided
advice.Thisisdemonstratedbythebetterdecisionsofthestudy
participantswhenusinganadvisorwithaconscientiousperson-
alitythanwhenusinganadvisorwithanextrovertedpersonality.
Moreover,thepersonalityoftheadvisoraffectstheperceptionof
humanstowardsthesystem,andithastheriskofleadinginvestors
tofurthertrustthosesystemsthatprovideworseadvice.
6 Conclusion
Inthispaper,wehaveconductedalab-baseduserstudytoexamine
howeffectivelargelanguagemodelsareasfinancialadvisors.We
focusonthreecorechallenges:preferenceelicitation,investment
personalization,andadvisorpersonality.
8Participantswereunawareofthespecificpersonasduringthestudy.
serocS
tnemitneS
egarevA
Extroverted
Conscientious
Figure4:Averagesentimentscoresbyadvisorpersonality.
Errorbarsindicatethestandarddeviation.
First,ouranalysisshowsthatLLMsareeffectivetoolsforprefer-
enceelicitationthroughconversation.Inamajorityofcases,they
arecapableofobtaininginvestor’spreferenceswithanaccuracy
closetoorequivalenttothatofanexperthumanadvisor.How-
ever,therearesomeclearfailurecases,asLLMsarevulnerableto
contradictorystatementsandhallucinations,which,inthecaseof
complexinvestorprofiles,candecreasetheaccuracyoftheelicita-
tiontorandomlevels.AlthoughLLMsarepromisingforelicitation,
inacomplexdomainlikefinance,investorsdonotalwaysfullyun-
derstandtheirownpreferences(ortheyhavedifficultiesexpressing
them).Therefore,futureworkshouldexplorethedevelopmentof
LLM-advisorscapableofresolvingconflictinguserneeds.
Second,personalizingLLMstoprovideinvestmentadvicecan
improvethedecisionsmadebytheinvestors,butonlywhenthe
personalizedLLM-advisorreceivesaccurateinformationaboutthe
investor’spreferences.Ifthepreferenceelicitationisnotsuccessful,
theagentactivelydirectstheinvestorstothewrongassetsonwhich
toinvest.Thisunderscoreshowcrucialagoodpreferenceelicitation
isforprovidingusefulfinancialadvice.
Finally,ourresultssuggestthatinvestorsarenotnecessarily
aware of what constitutes good financial advice, and therefore,
arevulnerabletoactingonbadadviceprovidedbyLLMs.Inthe
comparisonbetweenanon-personalizedandapersonalizedLLM-
advisor,althoughthepersonalizedsystemledtobetterdecisions,
participantswereunabletodistinguishbetweenthesystems.More
worryingly,whencomparingtwopersonalizedadvisorswithex-
trovertedandconscientiouspersonalities,weobservedthat,even
thoughtheextrovertedadvisorprovidedlower-qualityadvice,par-
ticipantstrustedthisadvisormorethantheconscientiousone.
Ourfindingshighlightthat,whilepersonalizedLLM-advisors
representapromisingresearchdirection,theiruseinhigh-stakes
domainslikefinanceisnotfreeofrisks:duetothelimitationsof
LLMsatcapturingcomplexinvestmentpreferences,andthediffi-
cultyofinvestorstodiscernwhethertheadvicetheyreceivetruly
servestheirinterests,LLMshaveanotablerisktodriveinvestors
tobadfinancialassets(leadingnotonlytoalowsatisfactionbut
alsotopotentiallylargemonetarylosses).However,thesedraw-
backsopeninterestingresearchdirectionsnotonlyfromasystem
perspective,butalsofromahuman-centeredapproach:automated
advisorydevelopmentwherewedonotjustfocusonimprovingthe
qualityofautomatedsystemstoguideinvestors,butalsoonhow
theinvestorswilladopt,trustandinteractwiththeseAIagents[5].
Acknowledgments
ThisworkwassupportedbyDaiwaSecuritiesGroupInc.
294

SIGIR’25,July13–18,2025,Padua,Italy TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,&IadhOunis
References
[25] OscarSainz,JonCampos,IkerGarcía-Ferrero,JulenEtxaniz,OierLopezdeLacalle,
[1] JamesE.Allen,CurryI.Guinn,andEricHorvtz.1999.Mixed-initiativeinteraction. andEnekoAgirre.2023. NLPEvaluationintrouble:OntheNeedtoMeasure
IEEEIntelligentSystemsandtheirApplications14,5(1999),14–23. LLMDataContaminationforeachBenchmark.InFindingsoftheAssociationfor
[2] AshayArgal,SiddharthGupta,AjayModi,PratikPandey,SimonShim,andChang
ComputationalLinguistics:EMNLP2023,HoudaBouamor,JuanPino,andKalika
Choo.2018. Intelligenttravelchatbotforpredictiverecommendationinecho Bali(Eds.).AssociationforComputationalLinguistics,10776–10787.
platform.In2018IEEE8thAnnualComputingandCommunicationWorkshopand [26] TetsuyaSakai.2018. Laboratoryexperimentsininformationretrieval. The
Conference(CCWC2018).IEEE,176–183. informationretrievalseries40(2018),4.
[3] WanlingCai,YuchengJin,andLiChen.2022.Impactsofpersonalcharacteristics [27] JavierSanz-Cruzado,EdwardRichards,andRichardMcCreadie.2024.FAR-AI:A
onusertrustinconversationalrecommendersystems.InProceedingsofthe2022 ModularPlatformforInvestmentRecommendationintheFinancialDomain.In
CHIConferenceonHumanFactorsinComputingSystems(CHI2022).Article489, Proceedingsofthe46thEuropeanConferenceonInformationRetrieval(ECIR2024),
14pages.
PartV.Springer-Verlag,267–271.
[4] GaryCharness,UriGneezy,andAlexImas.2013.Experimentalmethods:Eliciting [28] YunfanShao,LinyangLi,JunqiDai,andXipengQiu.2023. Character-LLM:
riskpreferences.JournalofEconomicBehavior&Organization87(2013),43–51. ATrainableAgentforRole-Playing.InProceedingsofthe2023Conferenceon
[5] ErinK.ChiouandJohnD.Lee.2023.Trustingautomation:Designingforrespon-
EmpiricalMethodsinNaturalLanguageProcessing(EMNLP2023).Associationfor
sivityandresilience.Humanfactors65,1(2023),137–165. ComputationalLinguistics,13153–13187.
[6] KonstantinaChristakopoulou,FilipRadlinski,andKatjaHofmann.2016.Towards [29] TuvaLundeSmestadandFrodeVolden.2019.Chatbotpersonalitiesmatters:im-
conversationalrecommendersystems.InProceedingsofthe22ndACMSIGKDD provingtheuserexperienceofchatbotinterfaces.In5thInternationalConference
internationalconferenceonknowledgediscoveryanddatamining(KDD2016). InternetScience:(INSCI2018).Springer,170–181.
815–824. [30] DavidJStreich.2023. Riskpreferenceelicitationandfinancialadvicetaking.
[7] BerardinaDeCarolis,MarcodeGemmis,PasqualeLops,andGiuseppePalestra.
JournalofBehavioralFinance24,3(2023),259–275.
2017.Recognizingusersfeedbackfromnon-verbalcommunicativeactsincon- [31] YuemingSunandYiZhang.2018. Conversationalrecommendersystem.In
versationalrecommendersystems.PatternRecognitionLetters99(2017),87–95. Proceedingsofthe41stInternationalACMSIGIRConferenceonResearchandDe-
[8] EugeneFFamaandKennethRFrench.1998.Valueversusgrowth:Theinterna-
velopmentinInformationRetrieval(SIGIR2018).235–244.
tionalevidence.Thejournaloffinance53,6(1998),1975–1999. [32] TakehiroTakayanagi,Chung-ChiChen,andKiyoshiIzumi.2023.Personalized
[9] ChristianHildebrandandAnoukBergner.2021.Conversationalroboadvisors
DynamicRecommenderSystemforInvestors.InProceedingsofthe46thInter-
nationalACMSIGIRConferenceonResearchandDevelopmentinInformation
assurrogatesoftrust:onboardingexperience,firmperception,andconsumer
financialdecisionmaking. JournaloftheAcademyofMarketingScience49,4 Retrieval(SIGIR2023).AssociationforComputingMachinery,2246–2250.
(2021),659–676. [33] TakehiroTakayanagi,KiyoshiIzumi,AtsuoKato,NaoyukiTsunedomi,andYuk-
[10] DietmarJannach,AhtshamManzoor,WanlingCai,andLiChen.2021.Asurvey inaAbe.2023.PersonalizedStockRecommendationwithInvestors’Attention
onconversationalrecommendersystems.Comput.Surveys54,5(2021),1–36. andContextualInformation.InProceedingsofthe46thInternationalACMSIGIR
[11] GuangyuanJiang,ManjieXu,Song-ChunZhu,WenjuanHan,ChiZhang,and
ConferenceonResearchandDevelopmentinInformationRetrieval(SIGIR2023).
YixinZhu.2024.Evaluatingandinducingpersonalityinpre-trainedlanguage AssociationforComputingMachinery,3339–3343.
models.InProceedingsofthe37thConferenceonNeuralInformationProcessing [34] TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,JavierSanz-Cruzado,
Systems(NeurIPS2023). RichardMcCreadie,andIadhOunis.2025.FinPersona:AnLLM-DrivenConver-
[12] HangJiang,XiajieZhang,XuboCao,CynthiaBreazeal,DebRoy,andJadKabbara.
sationalAgentforPersonalizedFinancialAdvising.InProceedingsofthe47th
2024.PersonaLLM:InvestigatingtheAbilityofLargeLanguageModelstoExpress
EuropeanConferenceonInformationRetrieval(ECIR2025),PartV.Springer-Verlag,
PersonalityTraits.InFindingsoftheAssociationforComputationalLinguistics: 13–18.
NAACL2024.3605–3627. [35] JohanneR.Trippas,SaraFahadDawoodAlLawati,JoelMackenzie,andLuke
[13] FrancisM.KinniryJr.,ColleenM.Jaconetti.,MichaelA.DiJoseph.,YanZilbering., Gallagher.2024.WhatdoUsersReallyAskLargeLanguageModels?AnInitial
DonaldG.Bennyhoff.,andGeorginaYarwood.2020. Puttingavalueonyour LogAnalysisofGoogleBardInteractionsintheWild.InProceedingsofthe47th
value:QuantifyingVanguardAdviser’sAlphaintheUK.TechnicalReport.The InternationalACMSIGIRConferenceonResearchandDevelopmentinInformation
VanguardGroup,ValleyForge,Pennsylvania,USA.
Retrieval(SIGIR2024).2703–2707.
[14] SherrieY.X.KomiakandIzakBenbasat.2006. Theeffectsofpersonalization [36] JohanneR.Trippas,LukeGallagher,andJoelMackenzie.2024. Re-evaluating
andfamiliarityontrustandadoptionofrecommendationagents.MISquarterly theCommand-and-ControlParadigminConversationalSearchInteractions.
(2006),941–960.
InProceedingsofthe33rdACMInternationalConferenceonInformationand
[15] IvicaKostric,KrisztianBalog,andFilipRadlinski.2021.Solicitinguserprefer-
KnowledgeManagement(CIKM2024).AssociationforComputingMachinery,
encesinconversationalrecommendersystemsviausage-relatedquestions.In 2260–2270.
Proceedingsofthe15thACMConferenceonRecommenderSystems.724–729. [37] PatcharaVanichvasin.2021.ChatbotDevelopmentasaDigitalLearningTool
[16] KausikLakkaraju,SaraE.Jones,SaiKrishnaRevanthVuruma,VishalPallagani,
toIncreaseStudents’ResearchKnowledge.InternationalEducationStudies14,2
BharathC.Muppasani,andBiplavSrivastava.2023.LLMsforFinancialAdvise- (2021),44–53.
ment:AFairnessandEfficacyStudyinPersonalDecisionMaking.InProceedings [38] XuenaWang,XuetingLi,ZiYin,YueWu,andJiaLiu.2023. Emotionalintel-
ofthe4thACMConferenceonAIinFinance(ICAIF2023).100–107. ligenceoflargelanguagemodels. JournalofPacificRimPsychology17(2023),
[17] CongLi.2016.Whendoesweb-basedpersonalizationreallywork?Thedistinction 18344909231213958.
betweenactualpersonalizationandperceivedpersonalization. Computersin [39] PontusWärnestål.2005.Userevaluationofaconversationalrecommendersystem.
humanbehavior54(2016),25–33. InProceedingsofthe4thWorkshoponKnowledgeandReasoninginPractical
[18] AndrewW.LoandJillianRoss.2024. CanChatGPTPlanYourRetirement?:
DialogueSystems.
GenerativeAIandFinancialAdvice.HarvardDataScienceReview(2024).Issue [40] HamedZamani,JohanneRTrippas,JeffDalton,FilipRadlinski,etal.2023.Con-
SpecialIssue5.
versationalinformationseeking.FoundationsandTrends®inInformationRetrieval
[19] TimLoughranandBillMcDonald.2011.Whenisaliabilitynotaliability?Textual 17,3-4(2023),244–456.
analysis,dictionaries,and10-Ks.TheJournaloffinance66,1(2011),35–65. [41] MarkusZanker,LaurensRook,andDietmarJannach.2019.Measuringtheimpact
[20] RobertR.McCraeandOliverP.John.1992.Anintroductiontothefive-factor ofonlinepersonalisation:Past,presentandfuture. InternationalJournalof
modelanditsapplications.Journalofpersonality602(1992),175–215. Human-ComputerStudies131(2019),160–168.
[21] SouravMedya,MohammadRasoolinejad,YangYang,andBrianUzzi.2022.An [42] YongfengZhang,XuChen,QingyaoAi,LiuYang,andWBruceCroft.2018.
ExploratoryStudyofStockPriceMovementsfromEarningsCalls.InCompanion Towardsconversationalsearchandrecommendation:Systemask,userrespond.
ProceedingsoftheWebConference2022(WWW2022).AssociationforComputing InProceedingsofthe27thACMInternationalConferenceonInformationand
Machinery,20–31.
KnowledgeManagement(CIKM2018).177–186.
[22] PearlPu,LiChen,andRongHu.2011.Auser-centricevaluationframeworkfor [43] HuaqinZhao,ZhengliangLiu,ZihaoWu,YiweiLi,TianzeYang,PengShu,
recommendersystems.InProceedingsofthe5thACMconferenceonRecommender ShaochenXu,HaixingDai,LinZhao,GengchenMai,etal.2024.Revolutionizing
Systems(RecSys2011).157–164. FinancewithLLMs:AnOverviewofApplicationsandInsights.arXivpreprint
[23] FilipRadlinski,KrisztianBalog,BillByrne,andKarthikKrishnamoorthi.2019.
arXiv:2401.11641(2024).
Coachedconversationalpreferenceelicitation:Acasestudyinunderstanding [44] DávidZibriczky.2016.Recommendersystemsmeetfinance:aliteraturereview.In
moviepreferences.InProceedingsofthe20thAnnualSIGdialMeetingonDiscourse Proceedingsofthe2ndInternationalWorkshoponPersonalization&Recommender
andDialogue(SIGDIAL2019).353–360. SystemsinFinancialServices(FinRec2016).1–10.
[24] FilipRadlinskiandNickCraswell.2017. Atheoreticalframeworkforconver- [45] LivZiegfeld,DaanDiScala,andAnitaHMCremers.2025.Theeffectofprefer-
sationalsearch.InProceedingsofthe2ndConferenceonHumanInformation enceelicitationmethodsontheuserexperienceinconversationalrecommender
InteractionandRetrieval(CHIIR2017).117–126. systems.ComputerSpeech&Language89(2025),101696.
295