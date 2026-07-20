---
conversion_metadata:
  converted_at: "2026-07-20T15:09:17Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cau & Spano.pdf"
  source_pdf_sha256: "50c6966d0c93b1131dfd61c91a7732dfc3bd7f8a34d9e914f9c4efe64c0afa10"
  page_count: 43
  markdown_char_count: 130967
---

UserModelingandUser-AdaptedInteraction(2026)36:3
https://doi.org/10.1007/s11257-025-09438-0
ExploringtheimpactofexplainableAIandcognitive
capabilitiesonusers’decisions
Federico Maria Cau1·Lucio Davide Spano1
Received:16December2024/Acceptedinrevisedform:12November2025/Publishedonline:6December2025
©TheAuthor(s)2025
Abstract
ArtificialIntelligence(AI)systemsareincreasinglyusedfordecision-makingacross
domains,raisingdebatesovertheinformationandexplanationstheyshouldprovide.
Most research on Explainable AI (XAI) has focused on feature-based explanations,
withlessattentiononalternativestyles.PersonalitytraitsliketheNeedforCognition
(NFC)canalsoleadtodifferentdecision-makingoutcomesamonglowandhighNFC
individuals.WeinvestigatedhowpresentingAIinformation(prediction,confidence,
and accuracy) and different explanation styles (example-based, feature-based, rule-
based,andcounterfactual)affectaccuracy,relianceonAI,andcognitiveloadinaloan
applicationscenario.WealsoexaminedlowandhighNFCindividuals’differencesin
prioritizingXAIinterfaceelements(loanattributes,AIinformation,andexplanations),
accuracy,andcognitiveload.OurfindingsshowthathighAIconfidencesignificantly
increasesrelianceonAIwhilereducingcognitiveload.Feature-basedexplanationsdid
notenhanceaccuracycomparedtootherconditions.Althoughcounterfactualexplana-
tionswerelessunderstandable,theyenhancedoverallaccuracy,increasingrelianceon
AIandreducingcognitiveloadwhenAIpredictionswerecorrect.Bothlowandhigh
NFCindividualsprioritizedexplanationsafterloanattributes,leavingAIinformation
astheleastimportant.However,wefoundnosignificantdifferencesbetweenlowand
highNFCgroupsinaccuracyorcognitiveload,raisingquestionsabouttheroleofthis
specific personality trait in AI-assisted decision-making. These findings underscore
the importance of user-centric personalization in XAI interfaces, where explanation
stylesaretailoredtousers’personalitytraits,cognitivecharacteristics,andtaskcon-
text,withsupportadaptedtoeachindividualtooptimizehuman–AIcollaboration.
Keywords Loanapprovalprediction·AI-assisteddecisions·ExplainableAI·
Reliance·Accuracy·Needforcognition
FedericoMariaandLucioDavideSpanoareequallycontributedtothiswork.
B
FedericoMariaCau
federicom.cau@unica.it
LucioDavideSpano
davide.spano@unica.it
1 DepartmentofMathematicsandComputerScience,UniversityofCagliari,ViaOspedale72,09124
Cagliari,Sardegna,Italy
123

3 Page 2 of 43 F.M.Cau,L.D.Spano
1 Introduction
Artificial Intelligence (AI) systems are becoming increasingly prevalent to assist
human decision-makers across various domains, ranging from low-stakes activities
like automating routine processes (Herzog and Wörndl 2019; Zehrung et al. 2021;
Musto et al. 2021; Liao et al. 2022; Viswanathan et al. 2022; Grace et al. 2022) to
high-stakes scenarios like healthcare diagnostics (Cai et al. 2019b; Lee et al. 2020,
2021; Beede et al. 2020; Fogliato et al. 2022a; Panigutti et al. 2022). AI-assisted
decision approaches pose numerous challenges within the HCI community, princi-
pally focusing on the problems of increasing users’ decision-making accuracy1 and
appropriaterelianceonAIsystemsrecommendations,i.e.,acceptingcorrectAIsug-
gestions and rejecting wrong ones (Zhang et al. 2020; Rechkemmer and Yin 2022;
Boveetal.2022;Scharowskietal.2023;Kahretal.2023;Vasconcelosetal.2023;
Chenetal.2023).Inparticular,previousresearchonhuman–AIteamsmainlyfocused
oninvestigatingthefollowingelements:taskcharacteristics(e.g.,complexity,stakes,
and uncertainty) (Buçinca et al. 2020; Cau et al. 2023b; Salimzadeh et al. 2023,
2024),users’traits(e.g.,NeedforCognition,taskfamiliarity,andAIliteracy)(Gajos
andChauncey2017;Buçincaetal.2021;GajosandMamykina2022;FordandKeane
2023;CelarandByrne2023;Heetal.2023a;Foroudietal.2025;Yurritaetal.2025),
different types of information about AI assistance (e.g., prediction, confidence, and
accuracy) (Yin et al. 2019; Lai and Tan 2019; Zhang et al. 2020; Rechkemmer and
Yin2022;Kahretal.2023;Heetal.2023a;CauandSpano2025),andexplanation
techniques to interpret AI decisions (e.g., example-based, feature-based, and coun-
terfactuals)(LaiandTan2019;Buçincaetal.2020;WangandYin2022;Boveetal.
2022; Chen et al. 2023; Teso et al. 2023). Despite these efforts, current research on
AI-assisteddecision-makingexhibitsdivergingresultsonhowandwhenAIassistance
isdeliveredandwhichexplanationstylescouldbetterhelpusersassesstheprovided
information.
Forexample,presentingspecificAIinformation(i.e.,prediction,confidence,and
accuracy) strongly influences users’ decision-making processes. While displaying
predicted labels increases users’ accuracy in the task compared to showing no AI
assistance(LaiandTan2019;Buçincaetal.2020),ahighAIconfidence(indicating
thecorrectnesslikelihoodinitsprediction),appearstoencourageparticipantstorely
onAIdecisionsmorethanalowone(Zhangetal.2020;RechkemmerandYin2022;
Cauetal.2023a,b).Similarly,userstendtoagreewithpredictionsofAIwithahigh
statedaccuracy2moreoftenthanthoseofmodelswithalowstatedaccuracy(Yinetal.
2019;RechkemmerandYin2022;Kahretal.2023;Heetal.2023a;Kahretal.2024).
Furthermore,studiesonhuman–AIdecision-makingrarelyevaluateusers’cognitive
loadduringtaskperformanceandthusoverlooktheextentofcognitiveresourcesbeing
utilized(SteyversandKumar2024).ThecombinedpresentationoftheseAIinforma-
tion pieces and their influence on users’ decision outcomes and perceptions is still
understudied.
1 Throughoutthepaper,wewillusethetermusers’“accuracy”toidentifytheir“decision-makingaccuracy”.
2 AIstatedaccuracyreferstotheaccuracyreportedforthemodelwhenevaluatedonunseendata,usually
thetestorheld-outset.
123

ExploringtheimpactofexplainableAIandcognitive… Page 3 of 43 3
Another crucial aspect of the decision-making process involves eXplainable AI
(XAI)techniques,whosepotentialtoenhanceuseraccuracyandappropriatereliance
onAIiscurrentlyunderdebate.Inourwork,wefocusonobjectivetasks(e.g.,whethera
personwillrepayaloan),whereagroundtruthexistsandthegoalistoevaluate,under-
stand,and/orimprovehumanperformanceandexperienceforadecision-makingtask
(Laietal.2023a).Inthesetypesoftasks,mostempiricalstudiesonAIdecisionsupport
havefocusedonfeature-basedexplanations(Laietal.2023a),andevidenceremains
inconclusive regarding their effectiveness in improving user accuracy or reducing
overreliance(Zhangetal.2020;WangandYin2021;Maetal.2023;Cauetal.2023b;
Chenetal.2023).Additionally,whilepriorworkshavecomparedtheeffectsoffeature-
basedandexample-basedexplanationsonusers(LaiandTan2019;Caietal.2019a;
Boveetal.2022;FordandKeane2023;Chenetal.2023;Laietal.2023b),thebene-
fitsandlimitationsofotherexplanationstyles,suchasrule-basedandcounterfactual
explanations,remainlargelyunderexplored(WangandYin2022;Bodriaetal.2023;
Tesoetal.2023;Cauetal.2023b,a).
Furthermore,priorworkhashighlightedthatindividualdifferencescanalsoinflu-
encepeople’sdecision-making.Recentstudiesinmusicrecommendation(Millecamp
et al. 2019, 2020), AI-assisted nutrition decisions (Buçinca et al. 2021; Gajos and
Mamykina 2022), and intelligent tutoring systems (Conati et al. 2021; Bahel et al.
2024) have explored theinfluence ofuser-centricattributeslikeNeedforCognition
(NFC)(Cacioppoetal1984)inuser-AIteams.NFCisapersonalitytraitthatreflects
anindividual’stendencytoengageinandenjoyeffortfulcognitiveactivities(Carenini
2001;CazanandIndreica2014;GajosandChauncey2017).Thisresearchhighlights
significantdifferencesinhowlowandhighNFCindividualsinteractwithAI,espe-
cially considering decision-making behavior, users’ accuracy, reliance on AI, and
cognitive load. While these studies provide some insights on specific domains, it is
unclearhowpeoplewithdifferentNFClevelsprioritizecertaininformationintheXAI
interfaceandhowdetailedAIinformationandmultipleexplanationstylesaffecttheir
decisions.
Considering this, this paper investigates how including different AI information
andexplanations(i.e.,prediction,confidence,accuracy,andexplanationstylessuchas
example-based,feature-based,rule-based,andcounterfactual)impactusers’decision-
makingprocessinasetofloanapprovaltasksconsideringtheiraccuracy,relianceon
AI, and cognitive load. Specifically, given the recent interest in studying the Need
for Cognition (NFC) personality trait in human–AI teams, we aim to examine how
differenttypesofAIinformationandexplanationstylesaffectlowandhighNFCusers
intermsof(i)howtheyprioritizetheinformationintheXAIinterfacewhenmaking
adecision,(ii)theaccuracyofthefinaldecision,and(iii)therequiredcognitiveload.
Ourresearchquestionstoaddressthesegapsarethefollowing:
RQ1 HowdoAIinformationandexplanationsimpactusers’accuracy,relianceonAI,
andcognitiveload?
RQ2 IsthereanydifferenceinhowpeoplewithlowandhighlevelsofNeedforCognition
prioritizetheinformationsuppliedintheXAIinterface?
RQ3 DopeoplewithlowandhighlevelsofNeedforCognitionhavedifferentaccuracy
andcognitiveloadwhenengagingwithexplanations?
123

3 Page 4 of 43 F.M.Cau,L.D.Spano
To answer these questions, we conducted an online user study (N = 288) where
participantsinteractedwithanAI-assistedloanapprovalinterface,decidingwhetherto
acceptorrejecteightloanrequestsbasedonvaryingAIassistance(i.e.,noAI,AIwith
noexplanation,AIwithexample-based,feature-based,rule-based,andcounterfactual
explanations). We analyzed their accuracy, reliance on AI, cognitive load, and the
importance of the XAI interface elements (i.e., loan attributes, AI information, and
explanation)thatledthemtothefinaldecision,furtherdifferentiatingtheresultsby
lowandhighlevelsofNeedforCognition.
Insummary,thecontributionsofthispaperare:
1. WefoundthatahighAIconfidencesignificantlyincreasesusers’relianceonAI
decisionswhilereducingcognitiveload.Thesefindingshighlighttheimportanceof
calibratingAIconfidenceestimatestoreflectthelikelihoodofsystemcorrectness.
Additionally,integratingusers’confidencecalibrationbeforeAIinteractionscould
enable new personalized AI-assisted strategies tailored to individual confidence
levels.
2. Contrarytoexpectations,feature-basedexplanationsdidnotimproveusers’accu-
racycomparedtootherAI-assistedconditions.However,despitebeingperceived
aslessunderstandablebyusers,counterfactualexplanationsenhancedrelianceon
AIandreducedcognitiveload,particularlywhentheAIpredictionswerecorrect,
potentially improving overall accuracy. These findings suggest combining mul-
tiple explanation styles to complement each other’s strengths and mitigate their
shortcomings,ultimatelyleadingtothedevelopmentofhybridXAIvisualizations.
3. We show that different levels (low and high) of the Need for Cognition (NFC)
mightnotcapturedifferencesinpeople’saccuracy,cognitiveload,andXAIinter-
faceelementprioritization.Whilepriorstudiesinlesscomplexdomainshaveoften
demonstrateddifferencesinNFClevels,ourresultssuggestthatsuchdistinctions
maydiminishastaskcomplexityincreases.ThesefindingssuggestthatNFCdif-
ferencesmaynotconsistentlygeneralizeacrossdiversedomainsandtasks.Future
studiesshouldexploreabroaderrangeofpersonalitytraitsandconsidermoving
beyondpersonality-basedfactorstofocusonotheruser-centriccharacteristics.
Ourpaperisorganizedasfollows.WefirstreviewpriorworkontheinfluenceofAI
information,explainableAI(XAI)effectiveness,andtheroleofNeedforCognition
(NFC)inAI-assisteddecision-making(Sect.2).Wethenoutlineourhypotheses,fur-
therdetailingthetaskdesign,includingdata,model,instances,andtheAIassistance
withexplanationsinSect.3.Wedescribeourstudydesign,focusingonvariables,sam-
plesize,statisticalanalysis,andtheparticipants’procedureinSect.4.Wepresentthe
resultsinSect.5,beginningwithdescriptivestatisticsandhypothesistests.Thisisfol-
lowedbyposthocandexploratoryanalyses,coveringtask-specificmetrics,interface
understandability,andqualitativefeedback.Next,wediscussthebroaderimplications
of our findings, highlighting study limitations and proposing directions for future
research in Sect. 6. We conclude with key contributions and insights for improving
XAIsystemsinSect.7.Thestudypipelineofdataprocessing,modeltraining,expla-
nationgeneration,andstatisticalanalysisisopenlyavailableathttps://osf.io/j64x8/?
view_only=7f546294a08843acbf204521ba7dee7e.
123

ExploringtheimpactofexplainableAIandcognitive… Page 5 of 43 3
2 Relatedwork
Inthissection,weprovideanoverviewofpreviousworkontheeffectivenessofAI
informationandcurrentexplainableAImethodologiesinrelationtousers,considering
themostcommonmetricsforevaluatingXAIsystemsandhighlightingunderstudied
topics. Then, we summarize previous studies on disaggregating low and high Need
forCognitionparticipantsinAI-assisteddecision-making,focusingonthegapsinthe
currentliterature.
2.1 InfluenceofAIinformationondecisionsupport
Previous studieshave shownthatproviding specificinformationabouttheAIassis-
tantduringdecision-making(i.e.,prediction,confidencescore,andtestsetaccuracy)
strongly influences users’ behaviors and task outcomes. For example, Lai and Tan
(2019)illustratedthatshowingAIpredictedlabelssignificantlyimproveshumanper-
formanceinadeceptiondetectiontask.Theyfoundthat,whenpredictedlabelswere
presented, providing feature-based explanations for the AI’s predictions resulted in
humandecisionaccuracycomparabletothatobtainedwhenparticipantswereexplic-
itlyinformedoftheAI’sstrongperformance.Similarly,Buçincaetal.(2020)found
thatparticipantswhoreceivedAIpredictions(withorwithoutexplanations)provided
moreaccurateanswersthanthosewhodidnotreceiveanyAIassistanceinanutrition-
relateddecision-makingtask.
AnothervaluablepieceofinformationprovidedbytheAIistheconfidencescore,
which refers to provided estimates about the correctness of its outcomes in various
formats,suchasnumericalconfidencescoresorranges(Caoetal.2024a;Bhattacharya
etal.2024a;CauandSpano2025),ortextual/graphicalrepresentations(Padillaetal.
2021;Prabhudesaietal.2023;Zhaoetal.2024;Marusichetal.2024).Inthispaper,
we specifically focus on a binary classification task, where we present AI outputs’
probabilities as numerical confidence estimates in percentage. For example, Zhang
etal.(2020)exploredtheeffectsofAIconfidenceonaccuracyandagreementwithAI
inanincomepredictiontask,findingthatpeopleweremorelikelytofollowtheAI’s
predictionswhentheAIhadhigherconfidence.Nevertheless,theyfoundnoevidence
that AI confidence scores improve the accuracy of AI-assisted predictions. Another
studyfromRechkemmerandYin(2022)studiedtheeffectsofAIconfidence,AIstated
accuracy,andtheirinteractiononusers’propensitytorelyontheAI’sadviceinaspeed
datingeventtask.TheresultsshowedthattheeffectofAIconfidenceonfollowingits
predictionsdependsonpeople’sbeliefinthepresentedAI’sstatedaccuracy:thehigher
the AI confidence, the more accurate people perceive the model to be. The authors
arguethatapossiblereasonfortheseresultsmaylieintheusers’perceptionoftheAI
information,consideringAIaccuracyasafactandAIconfidenceasanestimate(i.e.,
lesstrustworthythanAIperformance).Additionally,Cauetal.(2023a,b)foundthat
lowandhighlevelsofAIconfidenceinpredictionssignificantlyaffectusers’accuracy
andagreementonAI,alsoinfluencingtheeffectivenessofdifferentexplanationstyles
consideringdifferentdomainsandstakesscenarios.
123

3 Page 6 of 43 F.M.Cau,L.D.Spano
AsperAIaccuracyeffectsonusers,wespecificallyfocusonAItestsetaccuracy
(e.g.,accuracyintheheld-outdata,alsocalled“statedaccuracy”).Assuch,Yinetal.
(2019) explored how AI stated accuracy affected people’s agreement with the AI
in a speed dating task. The results show that high stated AI accuracy on held-out
dataincreasespeople’srelianceonAI.Furthermore,relianceisaffectedbybothAI’s
stated accuracy and its observed accuracy (i.e., actual AI accuracy on the observed
instances) during the task, and the effect of stated accuracy can change depending
on the observed accuracy. Rechkemmer and Yin (2022) also found that AI’s stated
accuracy significantlyincreasespeople’s agreement withtheAIandswitchfraction
(i.e.,users’changeopinionafterseeingtheAIprediction)inaseconddateprediction
task.PeoplerelyontheAImodelpredictionsmorewhenitsstatedaccuracyishigher.
Additionally, the impact of the AI’s confidence on people’s belief in its predictions
changes based on the AI’s reported accuracy levels. Similarly, prior works by Kahr
etal.(2023, 2024)alsofoundthatpeople’srelianceonAIishigherwhenpresented
withhigh-accuracyAI,whereusersareaskedtoestimatejailtimefor20legalcases.In
contrast,Heetal.(2023a)foundnosignificanteffectsofAIstatedaccuracyimpacting
users’relianceontheAI(expressedasagreementonAIandswitchfraction)inaloan
predictiontask.
On top of this, how AI assistance is presented also strongly shapes human–AI
decision-making. Although multiple interaction patterns exist (Gomez et al. 2025),
wefocusonthetwomostcommonHuman-CenteredAIparadigms:onestageandtwo
stage. The one-stage AI paradigm delivers AI assistance immediately to the human
decision-maker(Buçincaetal.2021;Rastogietal.2022;Cauetal.2023a,b;Luetal.
2024;Swaroopetal.2025).Whilethisparadigmcanspeeddecisionsandreducecog-
nitiveload,itcanalsocreateananchoringeffectinwhichtheAI’soutputbecomesa
salientreferencepointthatshapestheusers’judgment(Nouranietal.2021;Fogliato
etal.2022b;Maetal.2023;Boonprakongetal.2025).Instead,inthetwo-stageAI
paradigm, the user first gives an initial answer and then receives the AI’s advice to
revise that judgment. HCI research introduced this paradigm as a cognitive forcing
function (i.e., a cognitive intervention to enhance users’ engagement with AI assis-
tance)topromotemoredeliberate,criticalthinking,andofferpotentialimprovements
inaccuracyandappropriaterelianceonAI(Buçincaetal.2021;Heetal.2023a,b;Sal-
imzadehetal.2024;Agudoetal.2024;Morrisonetal.2024;Caoetal.2024b;Küper
etal.2025).However,severalstudieswarnthatperformancegainsmayinsteadreflect
greateralignmentwithAIoutputs,includingalignmentwithincorrectadvice,rather
thangenuineimprovementsinusercriticalthinking(Luetal.2024;Maetal.2024;
Caoetal.2024b).Inourstudy,wespecificallyfocusontheone-stageAIparadigm,as
ourgoalistoassesstheeffectivenessofexplanationswithoutusingcognitiveforcing
approaches. We also test whether this introduces differences in the interpretation of
peoplewithdifferentpropensitiesforenjoyingeffortfulthinking(seeSect.2.3forthe
NeedforCognitiontrait).
Tosummarize,priorresearchconsistentlyhighlightsthatAIconfidenceandaccu-
racy combinations affect users’ reliance on AI during decision-making. We believe
thatwhenusersareexposedtorelativelyhighstatedaccuracy,theAIconfidenceacts
asthetiebreakerinfollowingtheAIprediction:higherconfidenceincreasesthelike-
lihoodofusersfollowingtheAI’ssuggestion.Thus,thisstudyexplorestheimpactof
123

ExploringtheimpactofexplainableAIandcognitive… Page 7 of 43 3
AIinformationonuserrelianceonAI(i.e.,agreementwithAIdecisions),particularly
focusingondifferentlevelsofAIconfidence.Furthermore,sinceusers’cognitiveload
basedonAIassistanceisstillunderexploredinstudiesofAI-assisteddecision-making
(SteyversandKumar2024),wearguethatlowAIconfidencemayelicitahighercog-
nitiveloadinusersthanhighconfidence,forcingthemtoreasonindependentlyrather
thanblindlyfollowingtheAI’sprediction.
2.2 ExplainableAIeffectivenessinAI-assisteddecisions
With the rise of complex black-box AI models, eXplainable AI techniques have
emerged to help users understand how the AI reached a specific decision in low-
and high-stakes situations, including high-uncertainty and safety-critical contexts
(Bertrandetal.2022;Laietal.2023a;Rongetal.2024;Subramanianetal.2024).Pre-
viousstudieshaveshownthatexplanationsmayleadtoincreaseduseraccuracy(Lai
andTan2019;Buçincaetal.2020;Bansaletal.2021;Herm2023)andappropriate
relianceonAI(WangandYin2022;Scharowskietal.2023;Chenetal.2023)when
comparedtoAIpredictionaloneornotshowinganyassistance.Nevertheless,several
studiesonAI-assisteddecisionsexploredexplanationstyledifferencesinincreasing
users’accuracyandappropriatereliance,reportingcontrastingresults.Mostofthese
studiesfocusedonexample-basedandfeature-basedexplanations(Binnsetal.2018;
LaiandTan2019;Caietal.2019a;Zhangetal.2020;Boveetal.2022;FordandKeane
2023;Chenetal.2023;Laietal.2023b),withalimitednumberofstudiesalsoassess-
ing the effects of rule-based and counterfactual explanations (Gajos and Mamykina
2022;WangandYin2022;Tesoetal.2023;CelarandByrne2023;Xuanetal.2025).
Forexample,WangandYin(2022)studiedtheeffectsofdifferentexplanations(i.e.,
featureimportance,featurecontribution,nearestneighbors,andcounterfactuals)ina
recidivismpredictiontaskandfoundthatwhenusershavesomedomainexpertisein
thedecision-makingtask,featurecontributioncansatisfymoredesiderataoftheAI
modelandexplanations(i.e.,understanding,uncertaintyawareness,andtrustcalibra-
tion)regardlessofthecomplexityoftheAImodel.Anotherstudy(Chenetal.2023)
foundthat,foranincomepredictiontask,example-basedexplanationsimprovedpar-
ticipants’taskaccuracywhencomparedwithnoAIassistance,butonlywhentheAI’s
predictionswerecorrect.Instead,whentheAIprovidedwrongpredictions,theauthors
foundatrendoffeature-basedexplanationsincreasingoverreliance.Furthermore,Cau
etal.(2023b)investigatedtheeffectsonAIconfidenceandlogic-styleexplanationsin
astocktradingmarkettask,discoveringthatwhenAIconfidenceishigh,userstendto
over-relyonanerroneousAImorewithinductive(example-based)explanationsthan
abductive(feature-based)anddeductive(rule-based)explanations.
GiventhatmostoftheexistingXAIliteraturehasfocusedonfeature-basedexpla-
nations(Laietal.2023a),andthereisinsufficientevidenceregardingtheirimpacton
users’accuracy,particularlywithtabulardata(Zhangetal.2020;WangandYin2021;
Chenetal.2023;Maetal.2023;Cauetal.2023b;CauandSpano2025),weaimto
investigatewhetherfeature-basedexplanationsimproveusers’accuracycomparedto
123

3 Page 8 of 43 F.M.Cau,L.D.Spano
othertypesofAIassistance(i.e.,noAI;AIwithoutexplanations;AI+example-based
explanations;AI+rule-basedexplanations;andAI+counterfactualexplanations).3
2.3 Needforcognitioninhuman–AIdecisions
Inthiswork,wefocusspecificallyontheNeedforCognition(NFC)trait(Cacioppo
etal1984),givenpreviousstudiessuggestthatindividualdifferencesinNFCcanaffect
people’s interactions with AI assistance and explanations (Millecamp et al. 2019;
Buçincaetal.2021;GajosandMamykina2022;Baheletal.2024).NFCisameasure
thatreflectsthetendencyforanindividualtoundertakeeffortfulcognitiveactivities
(GajosandChauncey2017;Buçincaetal.2021)andbenefitmorefromcomplexuser
interfacefeatures(Carenini2001;CazanandIndreica2014;GajosandChauncey2017;
Ghaietal.2021;GajosandMamykina2022).Previousworkhasshownthatpeople
withhigherNFCaremorelikelytobecuriousandinafocused,attentivestatewhile
usingacomputer(LiandBrowne2006)andhavehigherperformanceatcomplexskill
acquisitioninthecontextofcomputertaskperformance(Dayetal.2007).
Considering explanations in music recommendations (i.e., assisted creation of a
playlist), Millecamp et al. (2019) found that explanations raised the confidence of
userswithalowNFCwhenmakingtheirplaylist.Incontrast,userswithahighNFC
experienced a decrease in their confidence due to explanations. On the contrary, a
follow-up study from Millecamp et al. (2020) did not find an effect of NFC on the
perception of explanations. The authors stated that a potential reason for this result
mightlieintheexplanations’presentationandtheproactiveactivationofexplanations,
which brings out the differences between low and high NFC users. While in the
previousstudy(Millecampetal.2019)explanationshadtobeexplicitlyactivatedby
theusers,inMillecampetal.(2020)explanationswerealwaysvisible.
Concerning NFC effects in the nutrition domain, Buçinca et al. (2021) studied
the impact of cognitive forcing functions (i.e., interventions that disrupt heuristic
reasoning and cause the person to engage in analytical thinking)4 and simple XAI
approaches among low and high NFC participants in an AI-assisted nutrition study
(e.g., making a plate low-carb by changing the ingredients accompanied by AI and
explanations) with a simulated AI. Despite high NFC participants trusting and pre-
ferringcognitiveforcingfunctionslessthansimpleexplainableAIapproaches,they
generally performed better inthetaskthan lowNFCparticipants. Furthermore,low
NFC participants generally found the task significantly more mentally demanding
and the system considerably more complex than high NFC participants. This might
confirmthefindingsfromMillecampetal.(2019, 2020)thatonlycognitiveforcing
functionsproduceintervention-generatedinequalitiesbetweenpeoplebasedontheir
NFClevel.
3 PleaserefertoSect.3.2.4andFig.1foradetaileddiscussionoftheexplanationsusedinourstudy.
4 Aswementionedearlier,inMillecampetal.(2019),explanationshadtobeexplicitlyactivatedbythe
users.Thisisanexampleofcognitiveforcingknownason-demand(Martijnetal.2022;Heetal.2024,
2025;Buçincaetal.2024;CauandSpano2025),whereAIassistanceorexplanationsarenotimmediately
availableandmustbeenabledbyauseraction.
123

ExploringtheimpactofexplainableAIandcognitive… Page 9 of 43 3
AnotherstudyonAI-assistednutritionbyGajosandMamykina(2022)foundthat
explanation-only design (without AI recommendation and before the user decision)
benefitspeoplewithahighNFCmoreintasklearningthanthosewithlowNFC.This
findingcontrastswithpreviousstudies,suggestingthatdifferencesinparticipantswith
diverselevelsofNFCmayemergewithoutusinginterventionslikecognitiveforcing
functions.InthecontextofAI-assistedmazesolving,arecentstudyfromVasconcelos
etal.(2023)investigatedwhetheroverreliancewasaffectedbytheinteractionbetween
participants’NFCscoresandtheAIwithandwithoutexplanationswhenthetaskwas
hardtosolve(boththeAIandexplanationsweresimulated).However,theydidnotfind
anyevidenceforthisinteraction,probablybecausethehardtaskgiventoparticipants
was too difficult to reveal differences across NFC scores. The authors hypothesized
thateventhosewithahighpropensityforeffortfulthinkingarelikelytoover-relyon
AI advice. A more recent work by Cau and Spano (2025) examined how different
levels of NFC (low or high) could influence accuracy and overreliance on AI when
presentedwithon-demandmultifacetedexplanationsinanAI-assistedjobapplication
context,andfoundnodifferencesacrossNFClevels.
Basedonthisbodyofresearch,ourworkaimstodeepentheallegedrequirement
forcognitiveforcingfunctionstohighlightthedifferencesbetweenlowandhighNFC
participants.Specifically,apartfromGajosandMamykina(2022)results,theuseof
interventions to provide explanations to users on-demand or employing two-stage
detectionparadigms(GreenandChen2019a,b;Heetal.2023a;CauandSpano2025;
Buçincaetal.2025)whereusersmaketheinitialdecisionaloneandthenmakeasec-
ondfinalchoicetodecidewhethertoincorporateAIadviceseemstobetheonlyways
toelicitdifferencesinlowandhighNFCparticipants.Additionally,previousstudies
investigatingparticipants’NFCusedsimulatedAIs,alwayscorrectAI’srecommen-
dations,andone/twotypesofsimulatedexplanations.Therefore,weexaminewhether
a difference exists between low and high NFC participants’ decision-making given
differentAIinformationandexplanations(i.e.,prediction,confidence,accuracy,and
explanationstylessuchasexample-based,feature-based,rule-based,andcounterfac-
tual)inacomplex(Salimzadehetal.2023)andhigh-stakesFootnote7loanapplication
scenario,consideringusers’accuracy,cognitiveload,andhowtheyprioritizetheXAI
interfaceinformation.
3 Hypothesesandtaskdesign
In this section, we start describing how we translated our research questions into
hypotheses, studying how AI information and explanations affect decision-making
(RQ1),howindividualswithvaryinglevelsofNeedforCognitionprioritizeinterface
elements(RQ2),andwhethertheseindividualsdifferinaccuracyandcognitiveload
(RQ3).Wethendetailthetaskdesignscenarioemployedtotestthesehypotheses.
123

3 Page 10 of 43 F.M.Cau,L.D.Spano
3.1 Hypotheses
Hypotheses Related to RQ1. As discussed in Sect. 2.1, previous research indicates
that low and high levels of AI confidence and accuracy affect user reliance on AI
in decision-making. Given we showed users a fixed AI accuracy that is relatively
high (i.e., 83% on the test set, see Sect. 3.2.2), we believe that high AI confidence
will lead users to rely more on AI predictions. Conversely, low AI confidence may
encourageuserstothinkindependently,increasingtheircognitiveloadcomparedto
high AI confidence. In Sect. 2.2, we also mentioned that previous work does not
highlight any strong advantages of rule-based and counterfactual explanations over
feature-basedones.Additionally,theefficacyofexample-basedexplanationsprimarily
dependsonthesimilarinstancesretrieved.Giventhatweareconsideringtabulardata,5
presenting similar instances would significantly increase task complexity and thus
users’ cognitive load (Salimzadeh et al. 2023; Cau et al. 2023b), which may lead
them to rely on the most frequent AI prediction across the similar instances (such
as accepting if the majority of similar instances are accepted) rather than carefully
analyzingeachinstanceindividually.Instead,feature-basedexplanations(inourcase,
featurecontribution)provideuserswithanimmediateoverviewofimportantattributes
relevant to the AI’s decision and seem at a glance to satisfy more desiderata for
AI models and explanations (i.e., understanding, uncertainty awareness, and trust
calibration)whenusersaresomewhatknowledgeableaboutthetargetdomain(Wang
and Yin 2022). Although satisfying more desiderata does not imply an increased
accuracyinthetask,wehypothesizethatfeature-basedexplanationsmightleadusers
toachievehigheraccuracythantheotherAIassistanceconditions.Summarizing,we
formulatethefollowinghypotheses:
(cid:129) H1a:UsersexposedtoahighAIconfidencewillrelymoreontheAIprediction
thanusersexposedtoalowAIconfidence.
(cid:129) H1b: Users exposed to a high AI confidence will report a lower cognitive load
thanusersexposedtoalowAIconfidence.
(cid:129) H1c: Users exposed to feature-based explanations will achieve higher accuracy
thaninotherAIassistanceconditions.
HypothesesRelatedtoRQ2.AsnotedinSect.2.3,highNFCindividualsengagemore
witheffortfulactivitiesandcomplexinterfacesthanlowNFCindividuals.Wetherefore
aim to explore which type of information (i.e., applicant details, AI information, or
explanations)participantsprioritizewhenrankinginterfaceelementstomakeafinal
decisionatdifferentlevelsofNFC.Wehypothesizethat,giventhecomplexityofthe
loanpredictiontaskandtheeffortneededtoinspectexplanations,lowNFCindividuals
will assign higher priority to AI information (rank 2) than to explanations (rank 3)
whenmakingtheirfinaldecision.Incontrast,highNFCindividualswillassignhigher
prioritytoexplanations(rank2)overAIinformation(rank3),reflectingtheirtendency
to engage with more complex interface features and attribute greater importance to
explanations.Hence,weformalizedthefollowinghypotheses:
5 Loanapprovaldecisionsarerecordedandcommunicatedusingtablesthatsummarizeapplicantattributes
(e.g.,income,creditscore,andemployment;seeSect.3.2.1).
123

ExploringtheimpactofexplainableAIandcognitive… Page 11 of 43 3
(cid:129) H2a:UserswithalowNFCwillmainlyprioritizetheapplicant’sdetailstomake
theirfinaldecision(rank1),thentheAIinformation(rank2),andlastlytheexpla-
nation(rank3).
(cid:129) H2b:UserswithahighNFCwillmainlyprioritizetheapplicant’sdetailstomake
theirfinaldecision(rank1),thentheexplanation(rank2),andlastlytheAIinfor-
mation(rank3).
HypothesesRelatedtoRQ3.WehypothesizethathighNFCparticipantswillleverage
explanationstogetmoreinsightsabouttheinformationprovidedbytheAI,potentially
achievinghigheraccuracythanthelowNFCones.Additionally,giventheirinclina-
tiontoenjoycomplexcognitiveactivities,highNFCparticipantswillreportalower
cognitiveloadincompletingtheloanapprovaltasks:
(cid:129) H3a: When provided with explanations, users with a high NFC will achieve a
higheraccuracythanuserswithalowNFC.
(cid:129) H3b:Whenprovidedwithexplanations,userswithahighNFCwillreportalower
cognitiveloadthanuserswithalowNFC.
3.2 Taskdesign
Thissubsectiondefineshowweimplementedtheloanapplicationtask,describingthe
dataweused,themodel,instanceselection,andmodelexplanationgeneration.
3.2.1 Data
We built the loan approval task on the publicly available Loan Prediction Problem
Dataset,6consistingof614loanrequestswherethegoalistodecidewhethertoaccept
orrejectaloanapplicationbasedontwelvefeatures.Weoptedforthisdatasetsinceit
reflectsarealisticandfairlycomplexhuman–AIcollaborationscenario(Salimzadeh
etal.2023;Heetal.2023a).Also,theloanpredictionscenariohasbeenusedinother
human–AIteamstudies(Binnsetal.2018;GreenandChen2019b;Gomezetal.2020;
Chromiketal.2021;van Berkeletal.2021;Heetal.2023a; Esfahanietal.2024a;
He et al. 2025), reinforcing its validity and suitability for collaboratively analyzing
interactionsbetweenhumansandAIsystems.Wedecidedtoconvertthenatureofthis
taskfromlow-stakestohigh-stakes7byrewardingparticipantswithamonetarybonus
incaseofcorrectdecisions(Salimzadehetal.2023)(seeSect.4.3).Beforetrainingthe
model,wediscardedtheLoan-IDcolumngivenitslowinformativenessforboththe
userandtheAIinthedecision-makingprocess,resultinginelevenfeatures(excluding
theoutcomeoftheloanrequest,seeFig.1A).
3.2.2 Model
WeusedaRandomForestClassifier(RFC)tosolvetheloanapprovaltask,following
theapproachinChromiketal.(2021).TheRFCwastrainedwith100estimators(trees)
6 https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset.
7 Wedesignedthetaskashigh-stakestoincreaseparticipants’engagementandsimulaterealism,asfinancial
decision-makingintherealworldofteninvolvesconsequences(Salimzadehetal.2023).
123

3 Page 12 of 43 F.M.Cau,L.D.Spano
usingan80:20stratifiedsplitfortrainingandtestsets,achievingatestsetaccuracy
ofabout83%,consistentwiththeirresults.WethenproceededtotheRFCcalibration
phase(SilvaFilhoetal.2023),althoughthemethodswetesteddidnotsignificantly
improvethecalibrationmetrics(seeSect.A.1).Wecomputedthemodelconfidence
estimatesonthetestset,asdescribedinSect.3.2.3.Fromnowon,wewillrefertothe
RFCmodelastheAI.
3.2.3 Instances
Before selecting the instances for the user study, we computed the AI confidence
estimates on the test set using Shannon’s entropy method to extract the epistemic
uncertainty (Shaker and Hüllermeier 2020) and convert it into a confidence score
rangingfrom0to100.Wecomputedthequartilesonthetestsetconfidencescores,
assigninganinstancetoalowconfidenceifitsvaluewasbelow44.3(Q )andahigh
2
confidenceifitsvaluewasabove61.6(Q ).Then,weselectedthefinalinstancesto
3
include in the user study by randomly picking 16 (Candrian and Scherer 2022; He
et al. 2023b; Tsirtsis et al. 2024; Strickland et al. 2024) and balancing them across
AI correctness, confidence, predicted class, and true class (see Table 1). Next, we
randomly split these instances into two groups of eight, balancing the values of the
aforementionedattributes(i.e.,ourcontrolledvariables).Wekeepthefirstgroupfor
practice and the latter for the main session. The final low confidence values were
between 9% and 43%, while high confidence values were between 68% and 85%.
Given the test accuracy of the AI is about 83%, participants’ “observed” accuracy8
will be only 62.5% (i.e., the AI provides correct recommendations in 5 out of 8
instances). We deliberately presented more instances where the AI made incorrect
predictionstoinvestigatewhetherandhowparticipantswouldtendtorelyexcessively
ontheAIsystem.Toaccountfororderingeffects(Nouranietal.2021),weprepared
400randompermutationsforthepracticeandmainsessioninstances,ensuringeach
participantseesdifferentlyorderedloanrequests.
3.2.4 AIassistanceandexplanations
Inthiswork,weassessedtheeffectsofsixAIassistanceconditions(seeFig.1),using
noAIassistanceasabaseline.OneconditionincludedAIinformationwithoutexpla-
nations,incorporatingprediction,confidenceintheprediction,andAIaccuracyonthe
testset.TheremainingfourconditionsaddedexplanationstothisAIinformation,as
detailedbelow.
Example-based.Example-basedexplanationsdonotusuallyprovidedirectinsights
into the internal model functioning in predicting a specific output. Instead, they are
usually employed to show representative prototypes of the AI’s predicted class or
select similar examples (Binns et al. 2018; Cai et al. 2019a; Dodge et al. 2019; Lai
and Tan 2019; Buçinca et al. 2020; Hase and Bansal 2020; Wang and Yin 2021;
Kimetal.2022)thatresembletheexaminedinstance.Anexceptionofthisconcerns
8 Observedaccuracy(62.5%)referstotheactualaccuracytheAIissettoprovidethroughoutthestudyfor
bothpracticeandmainsessions,whichwedonotcommunicatetoparticipants.
123

ExploringtheimpactofexplainableAIandcognitive… Page 13 of 43 3
Table1 Instancesettingsforpracticeandmainsessionsoftheloanpredictiontasks,forwhichtheorder
hasbeenuniquelyrandomizedforeachparticipant
| ID AIcorrectness | AIconfidence | AIprediction | Trueprediction |
| ---------------- | ------------ | ------------ | -------------- |
| 1 Correct        | High         | Reject       | Reject         |
| 2 Correct        | Low          | Reject       | Reject         |
| 3 Wrong          | High         | Reject       | Accept         |
| 4 Correct        | Low          | Accept       | Accept         |
| 5 Correct        | High         | Accept       | Accept         |
| 6 Correct        | Low          | Accept       | Accept         |
| 7 Wrong          | High         | Accept       | Reject         |
| 8 Wrong          | Low          | Accept       | Reject         |
approximatingablack-boxmodeltoasurrogatetransparentmodel(i.e.,TwinSystems
KennyandKeane2019, 2021;FordandKeane2023),wheretheweightsofablack-
boxmodelaretransferredintoatransparentsurrogatesuchasak-NN.Thisway,the
surrogatemodelmimicstheoriginalblack-boxmodelbehaviorandprovidesnearest
neighborinstancesthatalignwiththeoriginalmodeldecisions.Inourstudy,webuilt
example-basedexplanationstakinginspirationfromChenetal.(2023).Weselected
thethreenearestneighborinstancesfromthetrainingsetwiththecloseststandardized
Euclideandistancetothecurrentloanrequesttestinstance,showingtheAIprediction
of the neighbor instances. To reduce the cognitive load on users, we highlight the
neighbor feature values that differ from the given loan request test instance, so that
userscanfocusonthedifferencesbetweeninstances(seeFig.1C,Example-based).
Feature-based. Feature contribution enables users to identify the key attributes
thatsignificantlyinfluencetheAI’soutput,facilitatinginformeddecision-makingand
understandingoftheAI’sbehavior(e.g.,LIMERibeiroetal.2016andSHAPLund-
bergandLee2017).Givenitssolidtheoreticalbackground,andthefaithfulnessand
robustness in the generated explanations (Bodria et al. 2023; Feldkamp and Strass-
burger 2023), we rendered feature-based explanations using the SHapley Additive
exPlanations (SHAP) model-agnostic method (Lundberg and Lee 2017), explaining
the AI’s prediction by showing the Shapley contribution of each feature in favor
(positive sign) or against (negative sign) the AI’s prediction, and presented with an
interactiveverticalbarchart(seeFig.1D,Feature-based).Weusedpurpletorepresent
contributionsofarejectedloanrequestandgreenforanacceptedloanrequest.The
lengthofeachbarindicatesthemagnitudeofthatattribute’scontributionrelativeto
theAIpredictiononthecurrentloanrequest.
Rule-based.Rule-basedexplanationsprovideaseriesof“if-then”statementshigh-
lightingamodel’sdecision-makingprocessthathumanscaneasilyunderstand(Adadi
andBerrada2018;Wangetal.2019;Ribeiroetal.2018;Bodriaetal.2023).Wegener-
atedrule-basedexplanationsviathemodel-agnosticmethodcalledAnchors(Ribeiro
et al. 2018), which defines a rule (set of predicates) so that an instance is assigned
toaspecificclassonlyifallitspredicates(i.e.,featurestestedwiththresholdvalues)
satisfy that rule with a high probability. Anchors also return the precision and the
123

3 Page 14 of 43 F.M.Cau,L.D.Spano
Fig.1 AIassistanceconditionsfortheloanapprovaltasks.Participantscandisplayadditionalinformation
abouttheattributesbyhoveringovertheinfobuttons.A(NoAI)Participantswillseethetask’sgoaland
thecurrentapplicant’sdetails.B(AI)ParticipantswillalsobeassistedbyanAIinthedecision-makingtask
(i.e.,withprediction,confidence,andaccuracy).C(Example-based)Participantswillseecondition“B-AI”
andthethreenearestneighborsofthecurrentapplicant.D(Feature-based)Participantswillseecondition
“B-AI”andtheShapleyfeaturecontributionforeachapplicant’sattribute.E(Rule-based)Participantswill
seecondition“B-AI”andtherulegeneratedbyAnchor.F(Counterfactual)Participantswillseecondition
“B-AI”andthreecounterfactualinstancesgeneratedbyDiCE
coverage of the extracted rule. The precision indicates how well an anchor predicts
the model’s output. A high precision value suggests that the anchor is a good pre-
dictor of the output variable, while a low precision value highlights that the anchor
is a poor predictor. Instead, coverage measures how many examples in the dataset
arecoveredbytheanchor.Ahighcoveragevalueindicatesthattheanchorisagood
representativeofthedataset,whilealowcoveragevaluemeanstheanchorisapoor
representative. When generating the rules, we set the precision threshold constraint
to95%(i.e.,findingtheanchorthatmaximizesthecoveragegiventhethreshold).We
show participants the extracted rule in a tabular form, where each row represents a
predicatewhichafeatureistestedagainstathresholdvalue.Additionally,weadded
123

ExploringtheimpactofexplainableAIandcognitive… Page 15 of 43 3
twocolumnsshowingtheprecisionandcoverageofthegeneratedrule(seeFig.1E,
Rule-based).9
Counterfactual. Counterfactual explanations provide contrastive “what-if” state-
ments that help users understand what changes could be made to achieve a desired
output(Wachteretal.2017;AdadiandBerrada2018;Mothilaletal.2020a).Webuilt
counterfactual explanations using the Diverse Counterfactual Explanations (DiCE)
framework(Mothilaletal.2020b)foritseffectivenessinprovidingdiverseandaction-
ablecounterfactualexplanations(Mothilaletal.2021;Moreiraetal.2022).Givena
testinstance,DiCEgeneratescounterfactualexplanationsthatemphasizediversityand
deliveramorecomprehensiveunderstandingofthemodel’sbehavior,providingmul-
tiplecounterfactualsthatarediverseintermsofthechangesmadetotheinputfeatures.
Followingthelineofexample-basedexplanations,weshowusersthreecounterfactual
explanationsgeneratedfromagivenloanrequesttestinstance.Similarly,wehighlight
thecounterfactualfeaturevaluesthatdifferfromthegivenloanrequesttestinstanceto
reduceusers’cognitiveloadandletthemfocusonthedifferencesbetweeninstances
(seeFig.1F,Counterfactual).
4 Studydesign
Ourstudyfollowedamixed-factorialdesign,whereweaskedparticipantstodecide
whethertoacceptorrejectaseriesofloanrequests(seeTable1).Weinitiallymeasured
participants’NFCanddividedthemintolowandhighgroupsbasedonthedistribution
median.Next,weassignedeachparticipanttooneoftheAIassistanceconditionsas
abetween-subjectsfactor(i.e.,noAI;AIwithoutexplanations;AI+example-based
explanations; AI + rule-based explanations; and AI + counterfactual explanations).
Also,westudiedtheeffectsofthefollowingwithin-subjectscovariates:AIconfidence
(lowandhigh),andAIcorrectness(correctandwrong).First,participantscompleted
a practice session of eight loan requests to familiarize themselves with the task and
the assigned AI assistance condition. Next, they completed the main session of the
studywithanothereightloanrequests.
Thissectionoutlinesthevariables,plannedsamplesize,statisticalanalysis,andthe
procedurefortheuserstudyweconductedtotestourhypotheses.
4.1 Variables
For the hypothesis test, we considered the following measurements collected in the
mainsessionoftheuserstudy.Wecollectedthefollowingindependentvariables:
(cid:129) AIassistance(between-subjects,categorical).Wecreatedsixscenariosthatvaried
in terms of assistance provided by the AI and explanations to the participants
duringtheirdecision-makingprocess.
9 Participantscouldviewdetailedinformationabouttheoperator,precision,andcoverageattributesatany
timeduringthestudybyhoveringtheinfobuttonnexttoeachattribute.Theseconceptswerealsoexplained
indetailbeforethepracticesession.
123

3 Page 16 of 43 F.M.Cau,L.D.Spano
– NoAI.Weshowedparticipantstheloanrequestattributesandaskedwhether
itshouldbeacceptedorrejected.
– AI. We showed participants the information in the No AI condition and the
followingAIinformation:(i)predictionforthecurrentloanrequest,(ii)pre-
dictionconfidence,andiii)accuracyonthetestset.
– Example-based. Weshowedparticipants theinformationintheAI condition
andthreenearestneighborinstancesofthecurrentloanrequest.
– Feature-based. We showed participants the information in the AI condition
andtheSHAPfeaturecontributionforeachloanrequestattribute.
– Rule-based.WeshowedparticipantstheinformationintheAI conditionand
theAnchorruleforthecurrentloanrequest.
– Counterfactual. We showed participants the information in the AI condition
andthreeDiCE-generatedcounterfactualinstancesbasedonthecurrentloan
request.
(cid:129) Need for cognition (between-subjects, categorical). NFC is a stable personality
trait that reflects how much a person enjoys engaging in cognitively demanding
activities(Cacioppoetal1984).Wemeasuredparticipants’NFCusingthesix-item
NeedforCognitionScale(NCS-6)definedindeHolandaCoelhoetal.(2020)(see
Sect.Afordetails).WesplitparticipantsintolowandhighNFCbycomputingthe
medianoftheNFCscoredistribution,thesamecriteriausedinpreviousworkon
AI-assisteddecisions(Buçincaetal.2021, 2024, 2025;Conatietal.2021;Bahel
etal.2024;CauandSpano2025).
Wemeasuredtheireffectsonfourdependentvariables:
(cid:129) Accuracy (categorical). We measured participants’ accuracy as whether each
accept/rejectdecisionforaloanmatchedtheinstance’sgroundtruth(i.e.,wrong
orcorrect).
(cid:129) Reliance (categorical). We measured participants’ reliance on AI by assessing
whether a participant agreed or disagreed with the AI prediction (i.e., agree or
disagree).
(cid:129) Interfacecomponentsimportance(ranking).Wemeasuredtheimportanceofinter-
faceelementsforparticipantsindeterminingtheirfinalchoice,includingtheloan
request,theAIinformation,andtheexplanation,measuredasaranking.Partici-
pantsrespondedtothestatement:“Pleaserankthefollowinginformationinterms
ofhowimportantitwasforyouinmakingyourfinaldecision:(a)loanattributes,
(b)AIinformation,(c)explanation.”
(cid:129) Cognitiveload(numerical).Weassessedhowdifficultparticipantsfoundthetasks
using the Single Ease Question (SEQ) (Sauro and Dumas 2009) 7-point rating
scale,rangingfrom“1-Veryeasy”to“7-Verydifficult.”
Wealsocollectedthefollowingcovariates(seeTable1):
(cid:129) AI confidence (within-subjects, categorical). Participants saw loan requests with
eitherloworhighAIconfidence.
(cid:129) AIcorrectness(within-subjects,categorical).Participantssawloanrequestswith
correctorwrongAIpredictions.
123

ExploringtheimpactofexplainableAIandcognitive… Page 17 of 43 3
Finally, we collected other descriptive and exploratory measurements to provide
contextforourstudyandenablefurtherexploratoryanalysestomotivateourhypothe-
ses:
(cid:129) Demographics (categorical). We gathered participants’ information on their sex
andagefromtheProlificplatform.
(cid:129) Familiaritywiththetask(categorical).Weaskedparticipantsabouttheirfamiliarity
with loan request approval with the following statements using a 5-point Likert
scalerangingfrom“1-Noexperience”to“5-Highlyexperienced”:
– “Doyouhaveanyexperiencewithloanrequestapproval?”
– “DoyouhaveanyexperiencewithAI-assistedloanrequestapproval?”
(cid:129) AIinformationimportance(ranking).Weaskedparticipantstoranktheimportance
oftheAIprediction,confidence,andaccuracyintheconditionsthatincludethe
AIinformationbyasking:“PleaserankthefollowingAIinformationintermsof
howimportantitwasforyouinmakingyourfinaldecision:(a)AIprediction,(b)
AIconfidence,(c)AIaccuracy.”
(cid:129) XAIinterfaceunderstanding(numerical).Attheendofthesurvey,weaskedpar-
ticipants to state their easiness of understanding the loan application attributes,
AI information, and explanations using a 5-point Likert scale ranging from ”1 -
Stronglydisagree”to”5-Stronglyagree”inthreeitems(i)“Theloanapplication
attributeswereeasytounderstand,”(ii)‘TheAIinformationprovidedwaseasyto
understand,”and(iii)“TheAIexplanationprovidedwaseasytounderstand.”
(cid:129) Textualfeedback (opentext).Attheendofthesurvey,wecollectedparticipants’
feedbackabouttheexplanations(whenpresented)byasking:“Whatwerethepros
andconsoftheAIexplanationsyouencountered?”
4.2 Plannedsamplesizeandstatisticalanalysis
Before recruiting participants, we estimated the required sample size for our study
using G*Power software (Faul et al. 2009), resulting in 286 participants. This rec-
ommendedsamplesizeismotivatedbythemaximumnumberofparticipantsneeded
amongthehypotheses,whichwedescribeindetailasfollows.Sinceweareassessing
fivehypotheseswithmixedmodels(continuous/categoricaldependentvariables)and
twobasedonrankinginformation(usingtheFriedmantest),wedecidedtoapplytwo
different thresholds, using α = 0.05 = .01 for mixed models and α = 0.05 = .025
5 2
forrankingtests.Thus,weconsideredassignificantthep-valuesbelowthesereduced
thresholds in the analysis. Additionally, we assigned a randomly generated seed to
each user as a (i) random intercept to account for the variability of the dependent
variablesacrossdifferentclustersinthemixed-effectslogisticregressionandasa(ii)
within-clustercorrelationeffectonthedependentvariableintheGeneralizedEstima-
tionEquation(GEE)models.Allthemodelsconvergedsuccessfully.
ToanswerH1aandH1cwithcategoricaldependentvariables,weusedtwomixed-
effects logistic regression models with Reliance and Accuracy as the dependent
variables, assessing the main effects of AI assistance as the independent variable,
andAIconfidenceandAIcorrectnessascovariates.Wecomputedtherequiredsample
123

3 Page 18 of 43 F.M.Cau,L.D.Spano
size using G*Power for a mixed-effects logistic regression model (a priori χ2 test)
withmediumeffectsize(Cohen’sd =0.25),adesiredpowerof0.8,Df=5,andtwo
covariates(AIconfidenceandAIcorrectness),resultingin286participants.10Instead,
toanswerH1bwhichinvolvesanumericdependentvariable,weusedaGeneralized
EstimationEquation(GEE)modelwithCognitiveload asthedependentvariableto
assess the main effects of the AI confidence covariate while also studying potential
impactsoftheAIassistanceasanindependentvariableandAIcorrectnessasacovari-
ate. We computed the required sample size using the G*Power for a mixed-design
ANCOVA,mediumeffectsize(Cohen’s f =0.25),adesiredpowerof0.8,Df=1,and
twocovariates(AIconfidenceandAIcorrectness),resultingin191participants.
ToanswerH2,weconductedaFriedmantest(Friedman1937, 1940)withInterface
componentimportancerankedmeasurementsasthedependentvariabletoassessthe
mainandinteractioneffectsofNeedforCognition(lowandhigh)astheindependent
variable.WecomputedtherequiredsamplesizeusingG*Powerforawithin-subjects
FriedmanTestwithmediumeffectsize(Cohen’s f =0.16),adesiredpowerof0.8,one
group,andthreemeasurements(i.e.,loanapplicationattributes,AIinformation,and
explanation),resultingin100participants.ToestablishtherankingorderamongXAI
interfaceelements,weconductedaNemenyiposthocanalysiswhenwediscovered
significantfactorsintheFriedmantest.
ToanswerhypothesisH3awithacategoricaldependentvariable,weusedamixed-
effectslogisticregressionmodelwithAccuracyasthedependentvariabletostudythe
maineffectsofNeedforCognitionastheindependentvariable.Wealsoinvestigated
the impact of AI assistance as an independent variable and AI confidence and AI
correctnessascovariates.WecomputedtherequiredsamplesizeusingtheG*Power
foramixed-effectslogisticregressionmodel(aprioriχ2test)withmediumeffectsize
(Cohen’sd =0.25),adesiredpowerof0.8,Df=1,andtwocovariates(AIconfidence
and AI correctness), resulting in 187 participants. Instead, to answer H3b, which
involves a numeric dependent variable, we used a Generalized Estimation Equation
(GEE)modelwithCognitiveloadasthedependentvariabletoassessthemaineffects
ofNeedforCognition.Further,wealsoinvestigatedtheimpactofAIassistanceasan
independentvariable,andAIconfidenceandAIcorrectnessascovariates.Wecomputed
therequiredsamplesizeusingtheG*Power foramixed-designANCOVA,medium
effectsize(Cohen’s f =0.25),adesiredpowerof0.8,Df=1,andtwocovariates(AI
confidenceandAIcorrectness),resultingin191participants.
4.3 Procedure
Toverifyourhypotheses,weconductedanonlineuserstudyusingtheProlificplat-
form,11wherewerecruitedparticipantsaged18orolderwithhighEnglishproficiency
and approval rates between 95 and 100. Participants were then redirected to the
LimeSurveytool12wheretheycompletedthestudyinthreesteps.Participantsreceived
10 WhileH1aandH1brequirearound191participants(Df=1)forlowandhighAIconfidencelevels,H1c
increasesthenumberofparticipantsgiventhatwetestedallsixAIassistanceconditions(Df=5).
11 https://www.prolific.com/.
12 https://www.limesurvey.org/.
123

ExploringtheimpactofexplainableAIandcognitive… Page 19 of 43 3
Fig.2 Illustrationoftheprocedureparticipantsengagedinduringourstudy
£2.7asarewardforthestudy,withanaveragecompletiontimeof18min(i.e.,£9/h,
whichisconsideredafairpaymentforProlific).Prolificautomaticallytimedoutpar-
ticipantsafter60min.Werewardedparticipantswithanextra£0.12foreachcorrectly
classifiedloanrequestofthemainsession.Weonlyincludedparticipantsintheanaly-
sisiftheypassedallfiveattentionchecks.ThestudyhasbeenapprovedbytheEthics
CommitteeoftheUniversityofCagliari.13
Participantswentthroughthefollowingsteps,illustratedinFig.2.First,theyread
adocumentcontainingabriefstudydescription,filledoutaninformedconsentform,
and completed an attention check14 Next, they stated their familiarity with the task
and completed another attention check. Then, we asked participants to fill out the
six-itemNeedforCognitionScale(deHolandaCoelhoetal.2020)andtocomplete
anotherattentioncheck.Weintroducedparticipantstothetaskandassignedthemto
one of the six AI assistance conditions (i.e., no AI; AI without explanations; AI +
example-based explanations;AI+rule-basedexplanations;andAI+counterfactual
explanations)whilebalancingtheparticipationamongconditions.Beforestartingthe
practicesession,weprovidedparticipantswithdetailsabouttheassignedAIassistance
condition,wheretheycompletedanotherattentioncheck.Then,participantscompleted
eightloanrequesttasksasapracticesession,wheretheyneededtodecidewhetherto
acceptorrejecttheapplications.Aftereachdecision,participantsreceivedfeedback
ontheiranswers,wherewerevealedthecorrespondingtrueclass.Whenparticipants
finishedthepracticesession,weshowedthemapageasareminderforthemaintask
session, resulting in a compensation bonus in case of correctly classifying a loan.
Beforestartingthemainsession,participantscompletedthelastattentioncheck.
Participantscompletedeightloanrequesttasks,withthesameAIassistancecondi-
tionassignedinStep2butwithoutreceivingfeedbackonthetrueclass.Foreachtask,
wemeasuredparticipants’cognitiveload.Wealsoaskedthemtoranktheimportance
oftheinterfacecomponents(seeSect.4.1)exceptinthe“NoAI”and“AI”conditions.
Finally,weaskedparticipantstostatetheireaseofunderstandingoftheXAIinterface
elements (i.e., loan application attributes, AI information, and explanation) and to
providetextualfeedbackabouttheprosandconsoftheexplanationstheyencountered
(seeSect.4).
13 ReceivedonJuly25,2024,Prot.0205640.
14 WeuseInstructionalManipulationChecks(IMCs),wheretheanswertoeachattentioncheckisexplicitly
reportedinthequestiontextandfollowsthegoodpracticesofProlific.https://researcher-help.prolific.com/
en/article/fb63bb.
123

3 Page 20 of 43 F.M.Cau,L.D.Spano
5 Results
5.1 Descriptivestatistics
The final sample of 288 participants comprised 144 males and 144 females, aged
between 18 and 74 (M = 32.42, SD = 10.95). Participants reported low familiarity
with the loan application task (M = 1.83, SD = 0.99, 5-point Likert scale, 1: no
experience,5:highlyexperienced)andAI-assistedloanrequestapproval(M =1.32,
SD = 0.71, 5-point Likert scale, 1: no experience, 5: highly experienced). Overall,
participantsreportedagoodeasinessinunderstandingtheloanapplicationattributes
(M =3.72,SD=0.93,5-pointLikertscale,1:stronglydisagree,5:stronglyagree),
AI information (M = 3.74, SD = 0.95, 5-point Likert scale, 1: strongly disagree,
5: strongly agree), and explanations (M = 3.67, SD = 1.00, 5-point Likert scale, 1:
strongly disagree, 5: strongly agree). The NFC subdivision into low (143) and high
(145)individualswasachievedwithacomputedmedian Mdn =3.50(M =3.48and
SD=0.76).Figure8inAppendixshowsthecontinuousvaluesoftheNFCdistribution.
GiventhedistributionsforlowandhighNFCwerenon-normal(Shapiro–Wilk:low,
W = 0.915, p < .0001; high W = 0.888, p < .0001) and that homogeneity of
variances was unequal (Levene’s test: F = 23.2, p < .0001), we used a Wilcoxon
rank-sum test, which confirmed a significant difference between low and high NFC
groups (W = 0, p < .0001). The between-subject design and NFC variables were
overallhomogeneousintermsofdemographicsandfamiliarity.15 Wefurtherdiscuss
differencesintheparticipants’understandingoftheinterfacecomponents(i.e.,loan,
AIinformation,andexplanations)inSect.5.3.1.
5.2 Hypothesistests
5.2.1 H1:EffectsofAIandexplanationsonusers’relianceonAI,cognitiveload,and
accuracy
TheresultingchartsforH1aredepictedinFig.3.ForH1a,weusedamixed-effects
logisticregressionmodeltoexaminethedifferencesinusers’relianceonAI,consider-
inglowandhighAIconfidence.Theresultsoftheanalysisshowedasignificanteffect
(Log-Odds=1.22,Std.error=0.12,z-value=10.40, p<.01)ofhighAIconfidence
inincreasingusers’relianceonAIthanlowAIconfidence.Hencewerejectthenull
hypothesis for H1a, as users rely more on the AI when exposed to high AI confi-
dencethanlowconfidence.InH1b,westudiedthedifferencesinusers’cognitiveload
betweenlowandhighAIconfidenceusingaGeneralizedEstimationEquation(GEE)
15 AKruskal–WallistestwasconductedtocomparefamiliarityscoresacrossdesignandNFCgroups.The
resultsindicatednosignificantdifferencesinfamiliarityconsideringthedesignvariable(familiarity:χ2=
5.74,p=.33;familiarityAI:χ2=9.2,p=.1).WeobservedsimilarresultsacrossNFCgroups,exceptfor
taskfamiliarity(χ2=4.79, p=.03),whichwashigherforhighNFCindividuals(M=1.97,SD=1.06),
comparedtolowNFCindividuals(M =1.69,SD=0.89).ForfamiliaritywithAI(χ2 =1.5, p=.22),
thedifferencewasnotsignificant(highNFC:M=1.36,SD=0.75;lowNFC:M=1.28,SD=0.68).We
thusrepeatedtheanalysisforhypothesesH3aandH3b,addingfamiliarityasacovariateforpotentialmain
effectsandinteractionsforNFCandfamiliaritywiththetask.However,nosignificantresultswerefound.
123

ExploringtheimpactofexplainableAIandcognitive… Page 21 of 43 3
Fig.3 EffectsoflowandhighAIconfidenceconsideringrelianceonAI(H1a),cognitiveload(H1b)(ticks
abovebarsindicatelowerandhigherconfidenceintervalsbasedonstandarderrors),andusers’accuracy
(H1c)dividedbyAIassistanceconditions.Theasteriskshighlightp-valuesignificancestrength(***p<
.001)
model. The results of the analysis showed a significant effect (Log-Odds = −0.41,
Std.error =0.06,Wald =54.57, p<.01)ofhighAIconfidenceindecreasingusers’
cognitiveloadcomparedtolowAIconfidence.Hence,werejectthenullhypothesis
forH1b,concludingthatusersreportlowercognitiveloadwhenexposedtohighAI
confidencecomparedtolowconfidence.ForH1c,weinvestigatedtheusers’accuracy
differencesamongAIassistanceconditionsusingamixed-effectslogisticregression
model.Theresultsoftheanalysisshowednosignificanteffects(Log-Odds=0.34,Std.
error =0.16,z-value=2.11, p=.0349)offeature-basedexplanationsovertheother
interfaceconditionsonusers’accuracy;hence,wefailtorejectthenullhypothesisfor
H1c16.
5.2.2 H2:EffectsoflowandhighNFCparticipantsonXAIinterfaceinformation
importance
TotestH2(seeFig.4),weincludedonlyparticipantsexposedtoexplanations,resulting
in192users.ForH2a,wehypothesizedthatlowNFCparticipantswouldgivepriority
totheAIinformation(rank2)immediatelyaftertheloanattributes(rank1),keeping
theexplanation(rank3)asalastresort.TheFriedmantestforH2ashowsasignificant
difference (χ2 = 159, df = 2, p < .025) between the three XAI interface elements
wheninvestigatinglowNFCparticipants.Thepairwiserankingcomparisonsusingthe
Nemenyi(p < .025)showthatusersprioritizetheloanattributes(rank1),followed
bytheexplanation(rank2)andtheAIinformation(rank3)whenmakingtheirfinal
decision. In this light, we fail to reject the null hypothesis for H2a. For H2b, the
Friedmantestshowsasignificantdifference(χ2=324,df =2,p<.025)betweenthe
threeXAIinterfaceelementswheninvestigatinghighNFCparticipants.TheNemenyi
pairwise ranking comparisons (p < .025) align with our hypothesis, showing that
usersprioritizetheloanattributes(rank1),followedbytheexplanation(rank2)and
16 Althoughtheresultdidnotmeettheα=.01threshold,counterfactualexplanationsweretheonlyother
explanationtype,besidesfeature-basedexplanations,toshowaneffectonimprovingusers’accuracy(Log-
Odds=0.39,Std.Error=0.16,z=2.43,p=.0149).PosthocpairwisecomparisonsusingTukeyHSDdid
notshowsignificantdifferencesacrossAIassistanceconditions.
123

3 Page 22 of 43 F.M.Cau,L.D.Spano
Fig.4 XAIinterfacecomponentsrankfrequenciesforlow(H2a)andhigh(H2b)NFCindividuals.The
asteriskshighlightp-valuesignificantstrength(***p<.001)
the AI information (rank 3) when making their final decision. Hence, we reject the
nullhypothesisforH2b.
5.2.3 H3:EffectsoflowandhighNFCparticipantsonaccuracyandcognitiveload
For H3a (see Fig. 5), we investigated whether high NFC individuals may achieve
increasedaccuracywhenexposedtoexplanationscomparedtolowNFCindividuals.
The results of the mixed-effects logistic regression analysis showed no significant
effects (Log-Odds = 0.03, Std. error = 0.10, z-value = 0.28, p = .78) among low
and high NFC participants. Hence, we fail to reject the null hypothesis for H3a. In
H3b,westudiedthedifferencesinusers’cognitiveloadbetweenlowandhighNFC
participantswhenexposedtoexplanationsusingaGeneralizedEstimationEquation
(GEE)model.Theresultsoftheanalysisshowednosignificanteffects(Log-Odds=
−0.08,Std.error =0.12,Wald =0.51, p=.47)forhighNFCparticipantscompared
tolowNFCparticipants.Hence,wefailtorejectthenullhypothesisforH3b.17
5.3 Posthocandexploratoryanalyses
Thehypothesesresults(seeTable2)revealedthathighAIconfidenceincreasesreliance
onAIandreducescognitiveload.Additionally,therewerenosignificantdifferencesin
users’accuracyamongthedifferentAIassistanceconditions.Consideringtheinterface
component preferences, low and high NFC participants ranked loan attributes first,
explanationsecond,andAIinformationthird.Finally,noaccuracyorcognitiveload
differencesbetweenlowandhighNFCindividualswerefound.
TofurtherclarifytheroleofAIandexplanationsinshapinguserbehavior,wecon-
ductedadditionalanalysesconsideringtheinteractioneffectsbetweencovariates(AI
confidenceandcorrectness)andexplanations,furtherclarifyingtheroleofAIinfor-
mationinusers’prioritizationofXAIinterfaceelements’ranking.Wefirstexamined
17 Forcompleteness,wealsorepeatedthesameteststoexaminetheimpactofNFCwiththeoriginal
continuousvalues,findingnosignificantresultsforH3aandH3b.
123

ExploringtheimpactofexplainableAIandcognitive… Page 23 of 43 3
Fig.5 Users’accuracy(H3a)andcognitiveload(H3b)disaggregatedbylowandhighNFC(ticksabove
barsindicatetheStandardError)
Table2 Summaryresultsofourhypotheses
Hypotheses Supported
H1a:UsersexposedtoahighAIconfidencewillrelymoreonthe ✓
AIpredictionthanusersexposedtoalowAIconfidence
H1b:UsersexposedtoahighAIconfidencewillreportalower ✓
cognitiveloadthanusersexposedtoalowAIconfidence
H1c:Usersexposedtofeature-basedexplanationswillachieve ✗
higheraccuracythanotherAIassistanceconditions
H2a:UserswithalowNFCwillmainlyprioritizetheapplicant’s ✗
detailstomaketheirfinaldecision(rank1),thentheAI
information(rank2),andlastlytheexplanation(rank3)
H2b:UserswithahighNFCwillmainlyprioritizetheapplicant’s ✓
detailstomaketheirfinaldecision(rank1),thentheexplanation
(rank2),andlastlytheAIinformation(rank3)
H3a:Whenexplanationsareshown,userswithahighNFCwill ✗
achieveahigheraccuracythanuserswithalowNFC
H3b:Whenexplanationsareshown,userswithahighNFCwill ✗
reportalowercognitiveloadthanuserswithalowNFC
how AI confidence influences users’ interpretation of explanations by considering
metricssuchasaccuracy,relianceonAI,andcognitiveload.Wethenreassessedthese
metricsbyconsideringAIcorrectnesstoinvestigatepotentialoverreliancebehaviorin
AIwhenusersinteractwithexplanations.Additionally,giventhesignificantimpactof
highAIconfidenceonincreasingusers’relianceonAI,weevaluatedhowitimpacted
users’ prioritization of the XAI interface elements (i.e., loan attributes, AI informa-
tion,andexplanation)andwhetheritaffectedusers’rankingofAIinformation(i.e.,
prediction,confidence,andaccuracy).Lastly,wefocusedonhowlowandhighNFC
usersrankedtheAIinformation(i.e.,prediction,confidence,andaccuracy),wherewe
consideredonlytheAIassistanceconditionincorporatingexplanations.
123

3 Page 24 of 43 F.M.Cau,L.D.Spano
The results from the first analysis show no significant interactions between AI
confidence and explanations of users’ reliance on AI, cognitive load, and accuracy
(seeFig.9inAppendix).18 Instead,wefoundmultiplesignificantresultswhencon-
sideringtheAIcorrectnessandexplanationinteractions(seeFig.6-A).Forreliance
onAI,counterfactualexplanationinteractionwithAIcorrectpredictionsleadstoan
increaseinreliance(Log-Odds=0.98,Std.error =0.35,z-value=2.79, p =.0051).
The cognitive load results for counterfactual explanations and interaction with AI
correctness(Log-Odds=−0.48,Std.error =0.14,Wald =10.91, p=.0009)showa
decreaseinusers’cognitiveload.Thesefindingssuggestthatpresentingcounterfactual
explanationsreducesthecognitiveloadwhenAIpredictionsarecorrect.Additionally,
suchexplanationsencourageuserstofollowcorrectpredictions,potentiallymitigating
overrelianceonAI.
Interestingly,users’accuracyfindingshighlightatrendforAIcorrectpredictions
interacting with counterfactual explanations (Log-Odds = −0.84, Std. error = 0.34,
z value = −2.47, p < .0133) in decreasing accuracy. Additionally, counterfactual
explanations(Log-Odds=0.87,Std.error=0.27,z-value=3.17, p=.0015)leadtoan
increaseinaccuracy.Theseresultsmightindicateanuancedtrade-off:counterfactual
explanationsimprovedecision-makingoverallbutcansometimesconfuseuserswhen
AIpredictionsarealreadycorrect.
The results of splitting XAI interface information by AI confidence (see Fig. 10
in Appendix and Fig. 6B) show a significant difference between the three interface
componentsforlowconfidence(χ2=301,df =2, p <.025).TheNemenyipairwise
comparisonsshowasignificantdifference(p < .025)betweenloanattributes(rank
1)withAIinformationandexplanation.Instead,therearenodifferencesbetweenAI
information and explanation. We also have a significant difference among the three
interface components for high AI confidence (χ2 = 196, df = 2, p < .025). The
Nemenyi pairwise comparison results (p < .025) show that participants prioritize
the loan attributes (rank 1), followed by the AI information (rank 2), and then the
explanation(rank3).Finally,wefoundnorankingdifferencesamongAIprediction,
confidence, and accuracy when considering low AI confidence. Instead, the results
forhighAIconfidencehighlightadifferenceamongtheAIinformationelements(χ2
= 17.3, df = 2, p < .025). The Nemenyi pairwise comparisons (p < .025) reveal
asignificantdifferencebetweenAIpredictionandbothAIconfidenceandaccuracy,
whilenosignificantdifferenceisobservedbetweenAIconfidenceandaccuracy.
Inthesecondanalysis,werepeatedtheFriedmantestfocusingontheAIprediction,
confidence, and accuracy ranking, considering low and high NFC participants. The
results for low NFC participants show a significant difference between AI informa-
tion provided (χ2 = 13.2, df = 2, p < .025). The Nemenyi pairwise comparisons
(p < .025) reveal a significant difference between AI prediction and AI accuracy.
However,nodifferencesemergewhenconsideringAIconfidenceincomparisontoAI
prediction and accuracy. Instead, the Friedman test for high NFC participants high-
lightsnosignificantdifferencesamongAIprediction,confidence,andaccuracy.This
mayhintthatlowNFCusersseemtofocusmoreontheAIprediction,whichisrein-
18 Althoughitfallsoutsidethescopeofourhypotheses,itisimportanttonoticethathighAIconfidence
significantlyincreasesusers’accuracy(p<.01).
123

ExploringtheimpactofexplainableAIandcognitive… Page 25 of 43 3
Fig.6 PosthocanalysesresultsforAAIcorrectnessinteractionwithAIassistance,andBrankingforlow
andhighAIconfidencewithAIinformationimportanceofinterfaceelements.Theconnectionsbetween
rowspresentpvaluesandthedirectionoftheeffect(e.g.,adownwardarrowforadecreaseintheconnected
dependentvariable;forrankings,wedisplaytheexactpositionofeachinterfaceelementbasedonpairwise
comparisons)
forcedbyAIconfidence,whilehighNFCpeopleseemtolookattheAIinformation
asawhole.
5.3.1 Participants’interfaceunderstandabilityandqualitativefeedback
Thissectionsummarizesusers’understandingoftheinterfacecomponentsandtextual
feedbackonexplanationtypeswecollectedfromtheuserstudy,highlightingsubjective
perspectivesandperceivedprosandconsfromusersaboutexplanations.
Thechartdepictingusers’overallunderstandingofloanattributes,AIinformation,
andexplanationsisshowninFig.7.Wenoticethat,ingeneral,counterfactualexpla-
nationsdecreaseoverallunderstandingofinterfacecomponents.Wethenconducted
astatisticalanalysistounderstand ifthesedifferences aremerelyvisualtrendsorif
thereisindeedasignificantdifference.Giventhenon-normalnatureoftheinterface
components’ distributions,weoptedforanonparametricKruskal–Wallistest,using
theabovevariablesasdependentvariablesandthedesignastheindependentvariable.
Although there were no differences for loan understanding among conditions, we
foundsignificantdifferencesforAI(χ2=9.76,df =4, p =.045)andexplanation(χ2
=9.92,df =3, p =.019)understanding.Weperformedapairwisecomparisonusing
aDunntestwithBonferroniforp-valueadjustment.Wefoundadifferencebetween
AI (without explanations) and counterfactual conditions (z = −2.88, p = .0389) for
123

3 Page 26 of 43 F.M.Cau,L.D.Spano
Fig.7 Users’understandingofloanattributes,AIinformation,andexplanationsbyAIassistanceconditions
theAIinformationunderstandingandanotherdifferencebetweenfeature-basedand
counterfactualconditions(z=−3.018,p=.0152)intheexplanationunderstanding.
Consideringusers’feedbackonexplanations,11participantsreportedthatexample-
basedoneswereeasy,understandable,andafastwaytocompareapplications.Assuch,
P16said:“[explanation]washelpfulonceunderstoodalltheattributedetails”.On
thecontrary,11participantssaidthatexplanationslackeddetailsandthatitwashard
totrustthemfully.P73stated:“[explanation]madeiteasyformakingadecisionbut
notsureabouttheirreliability”.
Feature-based explanations were perceived by 8 participants as helpful and pro-
vidingclarityforthedecision-making.P75stated:“explainwelltherationalebehind
accepting or rejecting the loan”. However, 10 participants reported needing more
insightintowhyspecificweightswereassignedtoattributes.Assuch,P79said:“The
explanationneededmoreinsightsabouthowtheweightsweregenerated”.
Twelveparticipantsperceivedrule-basedexplanationsasusefulandeasytounder-
stand, providing good guidance in decision-making. For example, P22 said: “The
explanationhelpedmedecidewhethermyevaluationoftheloanapplicationismore
orlesscorrectornot”.Despitethis,12participantsstatedtheseexplanationslacked
understandability,highlightingtheabsenceof“reasoning”fortherules.Assuch,P84
reported: “Some rules had more information than others which made the choices
slightlyharder”.
6participantsperceivedcounterfactualexplanationsashelpfulandeasytoread.For
example,P85reported:“Theexplanationincludesmanychangesintheattributebut
helps to understand (going through scenarios) which attributes are more important
andinfluentialthanothers.”.Onthecontrary,6participantsstatedtheywereunclear
oruntrustworthy.Forexample,P5said:“Explanationisveryhelpfulbuthardtotrust
duetonotknowingthemechanismsbehindtheAI”.
6 Discussion
ThepaperexploredhowAIassistanceandvariousexplanationtypesinfluenceusers’
accuracy, reliance on AI, and cognitive load. Additionally, we examined the role of
XAIinterfaceelementsforindividualswithlowandhighNFC,analyzingdifferences
123

ExploringtheimpactofexplainableAIandcognitive… Page 27 of 43 3
inaccuracyandcognitiveloadacrossthesegroups.Basedonourresults,wepresent
acomprehensivediscussionofourkeyfindings,offeringinsightsintodesignimpli-
cationsandexamininguserbehaviorsinthecontextofaloanapplicationscenario.
6.1 TheroleofAIinshapinguserdecision-making
OurfindingsrevealthathighAIconfidenceincreasesusers’relianceonAIprediction.
Thisissupportedbyposthocanalysis,whereusersprioritizeloanattributesfirst(rank
1),thenAIinformation(rank2),andexplanationslast(rank3).WhenAIconfidence
is low, users still prioritize loan attributes (rank 1) but assign equal priority to AI
information and explanations (both rank 2). Interestingly, prior research (Cau et al.
2023b)inhigh-uncertaintydomainslikestocktradingfoundthatusersprioritizedata
or AI information interchangeably (rank 1) with high AI confidence, but rank AI
(2nd) immediately after data (1st) when AI confidence is low. This suggests that as
uncertaintyindecision-makingincreases,individualsaremorelikelytoseekadditional
guidance from AI. In this context, the confidence level of the AI is essential to the
decision-making process. Our results also indicate that high AI confidence reduces
cognitiveload,withonlyafewstudiessupportingthisdirection(Souchetetal.2024;
SteyversandKumar2024).Altogether,ourfindingsreinforcepriorworkwhereusers
tend to rely more on high AI confidence across various domains and tasks (Zhang
etal.2020;RechkemmerandYin2022;Cauetal.2023a,b;Maetal.2024;Kahretal.
2023;Maetal.2024;CauandSpano2025).
While we balanced participants’ exposure to low and high AI confidence, they
encountered more instances with low confidence and correct predictions than with
othercombinationsofconfidenceandcorrectness.Thisdistributionwasintentionally
designedtoreflectapotentialreal-worldscenarioandtostudyparticipants’reliance
behavioronAI,wherethestatedAIaccuracy(83%)mightnotalignwiththeobserved
accuracy(63%)onunseeninstances.AssummarizedinTable4,users’performance
in the loan prediction tasks highlights a clear split between low and high AI confi-
denceinstances,particularlyconsideringunder-relianceoncorrectsuggestionswith
lowconfidenceand(over)relianceonwrongsuggestionswithhighconfidence.These
resultshighlighttheparticipants’uncertaintyintheirdecision-makingandtheirlack
of self-confidence. Since we can estimate AI confidence but cannot directly control
thecorrectnessofpredictionsforunseeninstances,itisessentialtoexplorealterna-
tive strategies to optimize the use of AI confidence estimates. Consequently, while
presenting AI confidence to users is essential for enhancing transparency (Bertrand
etal.2022;Maetal.2023, 2024;FokandWeld2024;Lietal.2025),itssignificant
impactonreinforcingAIpredictionsunderscorestheneedfortargetedinterfacedesign
interventions.
AI confidence calibration approaches (Silva Filho et al.2023; Ma et al. 2024; Li
etal.2025) provideestimatesthataccurately reflectthelikelihoodofcorrectnessin
AIpredictions.Therefore,itisimportanttocultivateuserawarenessregardingtheir
own decision confidence and to determine strategically when to present AI sugges-
tionsbasedonbothuserandAIconfidencelevels.Onepossiblesolutionistocalibrate
users’ confidence without initial AI assistance, allowing them to receive feedback
123

3 Page 28 of 43 F.M.Cau,L.D.Spano
onthetrade-offsbetweentheirconfidenceandaccuracy.Onceusershavedeveloped
their confidence, AI assistance can be introduced using design patterns that accom-
modatebothone-stageandtwo-stagedecision-makingprocesses.Forinstance,prior
research (Ma et al. 2023, 2024; Li et al. 2025) suggests dynamically adjusting the
timingofAIassistancebycomparingtheconfidencelevelsoftheuserandtheAI.AI
advicemaybeomittedorprovidedon-demand(Buçincaetal.2020;Maetal.2023;
He et al. 2024, 2025; Cau and Spano 2025) when user confidence is high, thereby
preserving user autonomy. Conversely, when AI confidence is higher, suggestions
canbepresentedbeforeusersmaketheirdecisions.Theseapproachesmightbalance
optimizingAIsupportwhilemaintainingusers’autonomy.
6.2 Theimpactofexplanationtypesonuserbehavior
Inlinewithpreviousstudiesontheeffectsofexplanationsonusers(Zhangetal.2020;
Chenetal.2023;CelarandByrne2023;CauandSpano2025),ourresultsshowedthat
thefeature-basedexplanationmightnotimproveaccuracycomparedtotheotherAI
assistanceconditions.Thecounterfactualwastheonlytypeofexplanationclosestto
ourthresholdinincreasingtheaccuracyofusers,althoughwedidnotfinddifferences
amongtheotherAIconditions.Theposthocanalysishighlightsmultiplebenefitsfor
counterfactualexplanations:increasingusers’relianceonAIwhilediminishingcogni-
tiveloadwhencorrectAIpredictionsareshown,andpotentiallyincreasingaccuracy.
Nevertheless,atrendsuggeststheymightoccasionallyloweraccuracyinspecificcon-
texts(correctAIpredictions)andbeperceivedaslessunderstandable,ashighlighted
byourqualitativeanalysis.Interestingly,despitehavingnearlyidenticalvisualizations
to counterfactuals, example-based explanations had no measurable impact on these
evaluationmetrics.
RecentworkfromChaeetal.(2025)supportsthesefindings,indicatingthatcounter-
factualexplanationsimprovetaskperformance,thoughusersreportlowersatisfaction
and understandability. This suggests that counterfactual explanations may trade off
user understandability for performance gains. Also, our results are consistent with
Xuanetal.(2025),statingthatcounterfactualexplanationsareperceivedaslessunder-
standablethanothertypes,suchasfeatureimportance,oftenseenaseasiertograsp.
However,explanationsperceivedas“easytounderstand”werefoundtobebothmore
intelligibleandmoremisleading.ThisalignswiththefindingsofChromiketal.(2021),
suggestingthatusersmightoverestimatetheirunderstandingoflocalfeatureexplana-
tionsduetotheillusionofexplanatorydepth.Furthermore,previouswork(Buçinca
etal.2020;WangandYin2022)alsodemonstratesthatsubjectivemeasures,suchas
userpreferences,donotnecessarilyalignorpredictobjectiveoutcomes.Overall,our
findingsemphasizetheimportanceofshiftingfromtraditionalfeature-basedexplana-
tions,whicharecommonlyusedinAIsystems.Instead,weshouldadoptapproaches
thatresemblehuman-likereasoning,suchascounterfactuals.Hence,itisessentialto
integratevarioustypesofexplanationstooffercomplementaryinsights.Thiscombina-
tioncanaddresseachexplanation’sshortcomingsandlimitations,ultimatelyleading
tothedevelopmentofhybridvisualizationsforexplainableAI(XAI).Recentstudies
haveproposedintegratingactionabledata-centricexplanations(AnikandBunt2021;
123

ExploringtheimpactofexplainableAIandcognitive… Page 29 of 43 3
LiaoandVarshney2021;Yurritaetal.2023;Esfahanietal.2024b;Bhattacharyaetal.
2025) alongside model-centric ones, offering potential benefits for both AI experts
and lay users by connecting them to the training data and influencing their percep-
tionsoftrustandfairnessinAIsystems.Forinstance,researchinthehealthdomain
hasdemonstratedthatexpertusersgainsignificantadvantagesfromhybridexplana-
tionscombiningdata-centricandglobalmodel-centricelements(Bhattacharyaetal.
2023, 2024a,b; Szymanski et al. 2024), though these approaches remain underex-
ploredforlayusers(CauandSpano2025).Futureworkshouldfocusondeveloping
tailored explanation interfaces that adapt to users’ expertise levels and contextual
needs,ensuringbothaccessibilityforlayusersanddepthforexperts.Ontopofthis,
tailoringXAIinterfacesforusersmayinvolveassessinguser-centricperspectivesand
characteristics,whichwediscussinthenextsubsection.
6.3 Individualdifferences:NFCandpersonalizationinAIinteraction
Ourfindingsdifferfrompreviouswork(Millecampetal.2019;Buçincaetal.2021;
Conatietal.2021;Baheletal.2024),whichreporteddifferencesbetweenlowandhigh
NFCindividualsintermsofaccuracyandcognitiveload.Interestingly,wefoundthat
bothlowandhighNFCparticipantsprioritizedexplanations(ranked2nd)immediately
afterloanapplicationattributes(ranked1st),leavingAIinformation(ranked3rd)as
theleastinfluentialindecision-making.Moreover,lowNFCindividualsprioritizedAI
predictionoveraccuracy,whilethosewithahighNFCseemtoconsiderAIinformation
asawhole.Wecanidentifytwomainreasonswemightnothaveobservedsignificant
NFC-relateddifferencescomparedtopriorstudies.
First,thetask’snatureandcomplexitymayhaveminimizedthedifferencesbetween
NFC groups. Notably, prior studies focused on low-stakes tasks, such as explaining
music recommendations (Millecamp et al. 2019), nutrition choices in image-based
domains (Buçinca et al. 2021), and tutoring systems for university students with
somedomainknowledge(Baheletal.2024).Incontrast,ourstudyinvolvedahigh-
stakesloanapprovaltaskusingtabulardatawithelevenfeatures,whereparticipants
were unfamiliar with the domain. Additionally, our explanations added substantial
informationforuserstoprocess,classifyingthetaskashigh-complexityaccordingto
Salimzadehetal.(2023).Thissuggeststhatastaskcomplexityincreases,NFCmay
loseitspredictiveabilitytodifferentiateindividualbehaviors.
Second,whiletheNFCpersonalitytraithasbeenshowntodistinguishbetweenlow
andhighNFCindividuals,itmaynotreliablyexplaindifferencesinAI-drivendecision
outcomes,regardlessofcognitiveforcing.RecentAI-assisteduserstudiesindomains
likeartperioddetection(KüperandKrämer2025),jobapplications(CauandSpano
2025),andexerciserecommendation(Buçincaetal.2024, 2025),indicatethatNFC
maynotalwayspredictdifferencesinusers’accuracy,learning,relianceonAI,ormen-
taldemand,regardlessofexplanationtypeorcognitiveinterventions.Thesefindings
highlighttheneedforalternativetraitsthatmightcapturericherinsightsaboutintrinsic
motivationtolearnandthink,suchasEpistemicCuriosity(Litman2008)orthefive-
dimensionalcuriosityscale(Kashdanetal.2018).Moreover,anotablemethodological
concern is dividing participants into low- and high-trait groups after data collection
123

3 Page 30 of 43 F.M.Cau,L.D.Spano
basedontheoverallparticipantdistributionmedian.Thisapproach,commonlyused
for NFC and other traits, may lead to imbalances and unequal group sizes, compli-
cating statistical analyses and consequent reproducibility of results. Future research
should explore alternative user-centric metrics beyond personality traits that enable
real-timecategorizationduringstudies,ensuringmorebalancedgroupsanddynamic
personalization.
6.4 Limitationsandfuturework
Weacknowledgethefollowinglimitationsinourwork.ThefirstconsistsofusinganAI
modelwithuncalibratedconfidenceestimates.Althoughweassessedthatcalibration
metricsdidnotimprovetheAIbaselinemodel(RandomForest),thismayhaveaffected
thecomputationofmodelconfidenceestimatesandexplanationsgeneration,andcon-
sequently users’ decision-making during the study. As such, we strongly encourage
futurestudiestocalibratetheirAImodelswhennecessarytoensurestabilitybetween
AIprobabilityoutputsandconfidenceestimates.Asecondlimitationisthatourstudy
employed a one-stage detection paradigm, where users’ decision-making co-occurs
withAIsuggestionsandexplanations.Whilethisapproachmirrorsmanyreal-world
applicationsappliedtoautonomousdriving(Atakishiyevetal.2024)andcybersecu-
rity(Desoldaetal.2023),itmayrestricttheabilitytodisentangleusers’independent
reasoningfromtheirrelianceonAIadvice.Incontrast,two-stagedetectionparadigms,
whereusersfirstevaluateataskindependentlybeforeincorporatingAIinput,provide
a clearer separation of cognitive engagement and reliance patterns. Future research
shouldexplorebalancingtheseparadigmstoachieveanoptimaltrade-offbasedonthe
targetdomain’sspecificdemands,stakes,andcognitivecomplexity.Thethirdlimita-
tionisthatwesolelyfocusedontheNeedforCognitionpersonalitytrait.However,
manyotherindividualdifferencesmightdrivepeople’sdecision-makingandbehaviors
when interacting with AI assistance or explanations, such as AI literacy (Schoeffer
etal.2022),ActivelyOpen-mindedThinking(Baron1985),ormetacognitivepercep-
tions(Cushingetal.2024),whichwouldrequirefurtherinvestigationinfuturework.
The last limitation concerns the generalizability of our findings beyond the specific
domain, dataset, classification model, AI confidence split into low and high levels,
andexplanationmethodsused.Ourstudyemployedapubliclyavailableloanapproval
dataset commonly used in HCI research, along with a model achieving comparable
evaluationmetrics.Additionally,ourparticipants’sampledemonstratedlowfamiliar-
itywiththeloanapprovaltask,andweencouragecautioningeneralizingthesefindings
toexpertusers.Althoughweusedstate-of-the-artmethodstogenerateexplanations,
it is possible to produce the same type of explanation (e.g., feature-based, rules, or
counterfactuals)throughdifferentapproaches,whichcouldleadtodifferentfindings.
Whileweensuredreplicabilitybydetailingthedataprocessing,AImodel,explana-
tiongeneration,andstatisticalanalysis,severalvariablesuniquetooursetupmayhave
influenceddecision-making.FurtherresearchisneededtoevaluatetheimpactofAI
andexplanationsacrossdiversedomainswithvaryingstakesandlevelsofuncertainty.
123

ExploringtheimpactofexplainableAIandcognitive… Page 31 of 43 3
7 Conclusion
This article investigated how presenting AI information, including prediction, con-
fidence, accuracy, and explanation styles such as example-based, feature-based,
rule-based,andcounterfactual,affectsusers’decision-makinginloanapprovaltasks.
Specifically,weconductedauserstudy(N=288)examininghowtheseelementsinflu-
enceaccuracy,relianceonAI,andcognitiveloadacrosssixAIassistanceconditions:
noAI,AIwithnoexplanation,andAIwitheachofthefourexplanationstyles.Addi-
tionally,giventherecentinterestinstudyingtheNeedforCognition(NFC)personality
traitinhuman–AIteams,weexploredhowNFClevelsaffectusers’prioritizationof
information,accuracy,andcognitiveloadwheninteractingwithdifferentexplanation
styles.
OurresultsshowthathighAIconfidencesignificantlyincreasesusers’relianceon
AIwhilereducingcognitiveload,emphasizingtheimportanceofaccuratelycalibrating
confidence estimates to reflect AI correctness. Counterfactual explanations, despite
being rated as less understandable than feature-based ones, overall increase users’
accuracy, also reducing cognitive load and increasing reliance on AI, particularly
whenpairedwithcorrectAIpredictions.Incontrast,feature-basedexplanationsfailed
toimprove accuracy asanticipated.Moreover,weobserved thatNFClevelsdidnot
significantlydifferinhowusersprioritizeinformationortheirreliance,accuracy,and
cognitiveload,suggestingthatNFC’sinfluencemaybetask-orcontext-specific.These
findingscontributetoadeeperunderstandingofhowAI-assisteddecision-makingcan
beoptimizedbyintegratingcomplementaryexplanationstylesandtailoringinterfaces
toindividualuserneeds.Futureworkshouldexplorehybridexplanationsystemsand
refine user-centric models with AI to create more adaptive, effective, and equitable
human–AIcollaborationframeworks.
AppendixA
A.1.Modelcalibration
GivenwewillshowparticipantstheRFCconfidenceforeachprediction,wedecided
to calibrate the RFC probabilities before computing the confidence estimates using
three methods: Isotonic Regression (Zadrozny and Elkan 2001), Platt Scaling (Platt
2000), inductive and cross Venn-Abers (Vovk and Petej 2014; Vovk et al. 2015;
Manokhin 2017). Specifically, we compared the RFC with ensembles of ten RFC
models for each method to assess a ten-fold cross-validation. Nevertheless, in this
specificscenario,thesemethodsslightlyworsenedthemetricswetookintoconsider-
ation(Accuracy,BrierlossBrier1950,LoglossDomingos1999,ROC-AUCFawcett
2004,andExpectedCalibrationErrorGuoetal.2017),exceptfortheIsotonicRegres-
siontosomeextent(seeTable3).Wedecidedtouseouroriginal(uncalibrated)RFC
modelfortheloanpredictiontaskasitresultedinbettercalibrationmetricsthanthe
othermethodsweused.
123

3 Page 32 of 43 F.M.Cau,L.D.Spano
Table3 SummaryoftheRandomForestcalibrationresultsusingthefollowingmetrics:accuracy,Brier
loss,Logloss,ECE,andROC-AUC
Method Accuracy Brierloss Logloss ECE ROC-AUC
RFrawprobabilities 0.8293 0.1370 0.4424 0.0580 0.8204
IsotonicRegression 0.8130 0.1403 0.4518 0.0618 0.8215
PlattScaling 0.8130 0.1413 0.4524 0.0768 0.8167
CrossVenn-Abers 0.8211 0.1492 0.4727 0.0641 0.8
WeomittedtheinductiveVenn-Abersgiventheworstresultsoverallcomparedtotheothermethods.
Thevaluesinboldrepresentthebestresultsachievedacrossthemodelcalibrationmethods(forAccuracy
andROC-AUC,thehigherthebetter;forBrierloss,Logloss,andECE,thelowerthebetter).
A.2.Needforcognitionscale
Wewillmeasureparticipants’NeedforCognition(NFC)withtheNCS-6considering
a 5-point scale (1 = extremely uncharacteristic of me; 5 = extremely characteristic
ofme).Wewillsumupallthesix-itemscoresandthencomputethemediantosplit
participantsintolowandhighNFC.Weusedthefollowingsixitemstocomputethe
NFCfromdeHolandaCoelhoetal.(2020)19:
1. Iwouldprefercomplextosimpleproblems.
2. Iliketohavetheresponsibilityofhandlingasituationthatrequiresalotofthinking.
3. Thinkingisnotmyideaoffun.(R)
4. Iwouldratherdosomethingthatrequireslittlethoughtthansomethingthatissure
tochallengemythinkingabilities.(R)
5. Ireallyenjoyataskthatinvolvescomingupwithnewsolutionstoproblems.
6. I would prefer a task that is intellectual, difficult, and important to one that is
somewhatimportant.
A.3.Metricsoverviewbytask
Wesummarizedparticipants’performanceonloanpredictiontasksinTable4,ordered
bydecreasingaccuracy.AlongwithrelianceonAIandcognitiveload,wealsoreported
participants’ disagreement with correct AI advice, namely their under-reliance. We
reportedallthemetricsinpercent(%),exceptforcognitiveload.
19 note:(R)=reverseditems.
123

ExploringtheimpactofexplainableAIandcognitive… Page 33 of 43 3
Table 4 Participants’ accuracy, reliance on AI, under-reliance on AI, and cognitive load for our loan
predictiontaskinstancesettings
ID AIcorrectness AIconfidence Accuracy Reliance Under-reliance Cognitiveload
| 5 Correct | High | 90.4 90.4 | 9.6  | 3.1 |
| --------- | ---- | --------- | ---- | --- |
| 1 Correct | High | 85.4 85.4 | 14.6 | 3.3 |
| 6 Correct | Low  | 71.2 71.2 | 28.7 | 3.8 |
| 4 Correct | Low  | 56.2 56.2 | 43.8 | 3.7 |
| 2 Correct | Low  | 44.2 44.2 | 55.8 | 3.8 |
| 8 Wrong   | Low  | 27.9 72.1 | –    | 3.5 |
| 3 Wrong   | High | 27.1 72.9 | –    | 3.4 |
| 7 Wrong   | High | 14.6 85.4 | –    | 3.3 |
Fig.8 NFCdistributionofparticipantsintheuserstudy.TheorangeverticallinerepresentstheNFCmedian
(3.5)weusedtosplitparticipantsintolowandhighNFCgroups
Fig.9 Participants’relianceonAI,cognitiveload,andaccuracydividedbyAIassistanceandAIconfidence
conditions
123

3 Page 34 of 43 F.M.Cau,L.D.Spano
Fig.10 XAIinterfacecomponentsrankfrequenciesforlowandhighAIconfidence.Theasteriskshighlight
pvaluesignificantstrength(***p<.001)
Acknowledgements ThisresearchisfundedbytheItalianMinistryofUniversityandResearch(MUR)
andbytheEuropeanUnion—NextGenerationEU,Mission4,Component2,Investment1.1,undergrant
PRIN2022PNRR”DAMOCLES:DetectionAndMitigationOfCyberattacksthatexploithumanvuLner-
abilitiES”(GrantP2022FXP5B)—CUP:H53D23008140001.
Author contribution FC conceived and designed the user study and performed experiments under the
supervisionofLS.Allauthorsjointlywroteandreviewedthemanuscript.
Funding Open access funding provided by Università degli Studi di Cagliari within the CRUI-CARE
Agreement.
Data availability The original dataset used in this article is openly available at https://www.kaggle.
com/datasets/altruistdelhite04/loan-prediction-problem-dataset. The study pipeline of data processing,
modeltraining,explanationgeneration,andstatisticalanalysisisopenlyavailableathttps://osf.io/j64x8/?
viewonly=7f546294a08843acbf204521ba7dee7e.
Declarations
Conflictofinterest Theauthorsdeclarenoconflictofinterest.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincluded
inthearticle’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.If
materialisnotincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermitted
bystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthe
copyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
Adadi,A.,Berrada,M.:Peekinginsidetheblack-box:asurveyonexplainableartificialintelligence(xai).
IEEEAccess6,52138–52160(2018).https://doi.org/10.1109/ACCESS.2018.2870052
Agudo,U.,Liberal,K.G.,Arrese,M.,etal.:Theimpactofaierrorsinahuman-in-the-loopprocess.Cogn.
Res.Princ.Implic.9(1),1(2024).https://doi.org/10.1186/s41235-023-00529-3
Anik,A.I.,Bunt,A.:Data-centricexplanations:explainingtrainingdataofmachinelearningsystemsto
promotetransparency.In:Proceedingsofthe2021CHIConferenceonHumanFactorsinComputing
123

ExploringtheimpactofexplainableAIandcognitive… Page 35 of 43 3
Systems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).https://doi.
org/10.1145/3411764.3445736
Atakishiyev,S.,Salameh,M.,Yao,H.,etal.:Explainableartificialintelligenceforautonomousdriving:
acomprehensiveoverviewandfieldguideforfutureresearchdirections.IEEEAccess12,101603–
101625(2024).https://doi.org/10.1109/ACCESS.2024.3431437
Bahel, V., Sriram, H., Conati, C.: Initial results on personalizing explanations of ai hints in an its. In:
Proceedingsofthe32ndACMConferenceonUserModeling,AdaptationandPersonalization.Asso-
ciationforComputingMachinery,NewYork,NY,USA,UMAP’24,pp.244–248(2024).https://doi.
org/10.1145/3627043.3659566
Bansal, G., Wu, T., Zhou, J. et al.: Does the whole exceed its parts? the effect of ai explanations on
complementaryteamperformance.In:Proceedingsofthe2021CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).
https://doi.org/10.1145/3411764.3445717
Baron,J.:RationalityandIntelligence.CambridgeUniversityPress,Cambridge(1985)
Beede,E.,Baylor,E.,Hersch,F.etal.:Ahuman-centeredevaluationofadeeplearningsystemdeployed
inclinicsforthedetectionofdiabeticretinopathy.In:Proceedingsofthe2020CHIConferenceon
HumanFactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,
CHI’20,pp.1–12(2020).https://doi.org/10.1145/3313831.3376718
Bertrand,A.,Belloum,R.,Eagan,J.R.,etal.:Howcognitivebiasesaffectxai-assisteddecision-making:a
systematicreview.In:Proceedingsofthe2022AAAI/ACMConferenceonAI,Ethics,andSociety.
AssociationforComputingMachinery,NewYork,NY,USA,AIES’22,pp.78–91(2022).https://
doi.org/10.1145/3514094.3534164
Bhattacharya,A.,Ooge,J.,Stiglic,G.,etal.:Directiveexplanationsformonitoringtheriskofdiabetesonset:
Introducing directive data-centric explanations and combinations to support what-if explorations.
In:Proceedingsofthe28thInternationalConferenceonIntelligentUserInterfaces.Associationfor
ComputingMachinery,NewYork,NY,USA,IUI’23,pp.204–219(2023).https://doi.org/10.1145/
3581641.3584075
Bhattacharya,A.,Stumpf,S.,Gosak,L.,etal.:Exmos:explanatorymodelsteeringthroughmultifaceted
explanationsanddataconfigurations.In:ProceedingsoftheCHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’24(2024a).
https://doi.org/10.1145/3613904.3642106
Bhattacharya,A.,Stumpf,S.,Verbert,K.:Anexplanatorymodelsteeringsystemforcollaborationbetween
domainexpertsandai.In:AdjunctProceedingsofthe32ndACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
Adjunct’24,pp.75–79(2024b).https://doi.org/10.1145/3631700.3664886
Bhattacharya,A.,Vanherwegen,T.,Verbert,K.:"showmehow":benefitsandchallengesofagent-augmented
counterfactualexplanationsfornon-expertusers.In:Proceedingsofthe33rdACMConferenceon
UserModeling,AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,
NY,USA,UMAP’25,pp.174–184(2025).https://doi.org/10.1145/3699682.3728321
Binns,R.,VanKleek,M.,Veale,M.,etal.:’It’sreducingahumanbeingtoapercentage’:perceptionsof
justiceinalgorithmicdecisions.In:Proceedingsofthe2018CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’18,pp.1–14
(2018).https://doi.org/10.1145/3173574.3173951
Bodria,F.,Giannotti,F.,Guidotti,R.,etal.:Benchmarkingandsurveyofexplanationmethodsforblack
boxmodels.DataMin.Knowl.Disc.37(5),1719–1778(2023).https://doi.org/10.1007/s10618-023-
00933-9
Boonprakong,N.,Tag,B.,Goncalves,J.,etal.:HowdoHCIresearchersstudycognitivebiases?Ascoping
review. In: Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.
Association for Computing Machinery, New York, NY, USA, CHI ’25 (2025). https://doi.org/10.
1145/3706598.3713450
Bove,C.,Aigrain,J.,Lesot,M.J.,etal.:Contextualizationandexplorationoflocalfeatureimportance
explanationstoimproveunderstandingandsatisfactionofnon-expertusers.In:27thInternational
ConferenceonIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,
USA,IUI’22,pp.807–819(2022).https://doi.org/10.1145/3490099.3511139
Brier,G.W.:Verificationofforecastsexpressedintermsofprobability.Mon.WeatherRev.78,1–3(1950)
Buçinca,Z.,Lin,P.,Gajos,K.Z.,etal.:Proxytasksandsubjectivemeasurescanbemisleadinginevaluat-
ingexplainableaisystems.In:Proceedingsofthe25thInternationalConferenceonIntelligentUser
123

3 Page 36 of 43 F.M.Cau,L.D.Spano
Interfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’20,pp.454–464(2020).
https://doi.org/10.1145/3377325.3377498
Buçinca,Z.,Malaya,M.B.,Gajos,K.Z.:Totrustortothink:cognitiveforcingfunctionscanreduceoverre-
lianceonAIinai-assisteddecision-making.Proc.ACMHum.Comput.Interact.(2021).https://doi.
org/10.1145/3449287
Buçinca,Z.,Swaroop,S.,Paluch,A.E.,etal.:Towardsoptimizinghuman-centricobjectivesinai-assisted
decision-makingwithofflinereinforcementlearning(2024).arxiv:2403.05911
Buçinca,Z.,Swaroop,S.,Paluch.A.E.,etal.:Contrastiveexplanationsthatanticipatehumanmisconceptions
canimprovehumandecision-makingskills.In:Proceedingsofthe2025CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’25
(2025).https://doi.org/10.1145/3706598.3713229
Cacioppo,J.,Petty,R.,Kao,C.:TheefficientassessmentofNFC.J.Pers.Assess.48,306–7(1984).https://
doi.org/10.1207/s15327752jpa4803_13
Cai,C.J.,Jongejan,J.,Holbrook,J.:Theeffectsofexample-basedexplanationsinamachinelearninginter-
face.In:Proceedingsofthe24thInternationalConferenceonIntelligentUserInterfaces.Association
forComputingMachinery,NewYork,NY,USA,IUI’19,pp.258–262(2019a).https://doi.org/10.
1145/3301275.3302289
Cai,C.J.,Reif,E.,Hegde,N.,etal.:Human-centeredtoolsforcopingwithimperfectalgorithmsduring
medicaldecision-making.In:Proceedingsofthe2019CHIConferenceonHumanFactorsinComput-
ingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’19,pp.1–14(2019b).
https://doi.org/10.1145/3290605.3300234
Candrian,C.,Scherer,A.:Riseofthemachines:delegatingdecisionstoautonomousai.Comput.Hum.
Behav.134,107308(2022).https://doi.org/10.1016/j.chb.2022.107308
Cao,S.,Liu,A.,Huang,C.M.:Designingforappropriatereliance:therolesofaiuncertaintypresentation,
initialuserdecision,anduserdemographicsinai-assisteddecision-making.ProcACMHum.Comput.
Interact.(2024a).https://doi.org/10.1145/3637318
Cao,S.,Liu,A.,Huang,C.M.:Designingforappropriatereliance:therolesofaiuncertaintypresentation,
initialuserdecision,anduserdemographicsinai-assisteddecision-making.Proc.ACMHum.Comput.
Interact.(2024b).https://doi.org/10.1145/3637318
Carenini,G.:Ananalysisoftheinfluenceofneedforcognitionondynamicqueriesusage.In:CHI’01
ExtendedAbstractsonHumanFactorsinComputingSystems.AssociationforComputingMachinery,
NewYork,NY,USA,CHIEA’01,pp.383–384(2001).https://doi.org/10.1145/634067.634293
Cau, F.M., Spano, L.D.: The influence of curiosity traits and on-demand explanations in ai-assisted
decision-making.In:Proceedingsofthe30thInternationalConferenceonIntelligentUserInterfaces.
AssociationforComputingMachinery,NewYork,NY,USA,IUI’25,pp.1440–1457(2025).https://
doi.org/10.1145/3708359.3712165
Cau,F.M.,Hauptmann,H.,Spano,L.D.,etal.:Effectsofaiandlogic-styleexplanationsonusers’decisions
underdifferentlevelsofuncertainty.ACMTrans.Interact.Intell.Syst.(2023a).https://doi.org/10.
1145/3588320
Cau,F.M.,Hauptmann,H.,Spano,L.D.,etal.:Supportinghigh-uncertaintydecisionsthroughaiandlogic-
styleexplanations.In:Proceedingsofthe28thInternationalConferenceonIntelligentUserInterfaces.
AssociationforComputingMachinery,NewYork,NY,USA,IUI’23,pp.251–263(2023b).https://
doi.org/10.1145/3581641.3584080
Cazan,A.M.,Indreica,S.E.:Needforcognitionandapproachestolearningamonguniversitystudents.
ProcediaSoc.Behav.Sci.127,134–138(2014).https://doi.org/10.1016/j.sbspro.2014.03.227
Celar,L.,Byrne,R.:Howpeoplereasonwithcounterfactualandcausalexplanationsforartificialintelligence
decisionsinfamiliarandunfamiliardomains.MemoryCogn.(2023).https://doi.org/10.3758/s13421-
023-01407-5
Chae,S.,Lee,S.,Hauptmann,H.,etal.:Theroleofexplanationstylesandperceivedaccuracyondecision
makinginpredictiveprocessmonitoring.In:Krogstie,J.,Rinderle-Ma,S.,Kappel,G.,etal.(eds.)
Adv.Inf.Syst.Eng.,pp.39–56.Springer,Cham(2025)
Chen,V.,Liao,Q.V.,WortmanVaughan,J.,etal.:Understandingtheroleofhumanintuitiononreliance
inhuman–AIdecision-makingwithexplanations.Proc.ACMHum.Comput.Interact.(2023).https://
doi.org/10.1145/3610219
Chromik,M.,Eiband,M.,Buchner,F.,etal.:Ithinkigetyourpoint,ai!theillusionofexplanatorydepth
inexplainableai.In:Proceedingsofthe26thInternationalConferenceonIntelligentUserInterfaces.
123

ExploringtheimpactofexplainableAIandcognitive… Page 37 of 43 3
AssociationforComputingMachinery,NewYork,NY,USA,IUI’21,pp.307–317(2021).https://
doi.org/10.1145/3397481.3450644
Conati,C.,Barral,O.,Putnam,V.,etal.:TowardpersonalizedXAI:acasestudyinintelligenttutoring
systems.Artif.Intell.298,103503(2021).https://doi.org/10.1016/j.artint.2021.103503
Cushing,C.A.,Lau,H.,Hofmann,S.G.,etal.:Metacognitionasawindowintosubjectiveaffectiveexpe-
rience.PsychiatryClin.Neurosci.78(8),430–437(2024)
Day,E.,Boatman,J.,Kowollik,V.,etal.:Modelingthelinksbetweenneedforcognitionandtheacquisition
ofacomplexskill.Person.Indiv.Differ.42,201–212(2007).https://doi.org/10.1016/j.paid.2006.06.
012
de Holanda Coelho, G.L., Hanel, P.H.P., Wolf, L.J.: The very efficient assessment of need for cogni-
tion:developingasix-itemversion.Assessment27(8),1870–1885(2020).https://doi.org/10.1177/
1073191118793208
Desolda,G.,Aneke,J.,Ardito,C.,etal.:Explanationsinwarningdialogstohelpusersdefendagainst
phishing attacks. Int. J. Hum. Comput. Stud. 176, 103056 (2023). https://doi.org/10.1016/j.ijhcs.
2023.103056
Dodge,J.,VeraLiao,Q.,Zhang,Y.,etal.:Explainingmodels:anempiricalstudyofhowexplanationsimpact
fairnessjudgment.pp275–285(publisherCopyright:2019AssociationforComputingMachinery.;
24thACMInternationalConferenceonIntelligentUserInterfaces,IUI2019;Conferencedate:17-
03-2019Through20-03-2019)(2019).https://doi.org/10.1145/3301275.3302310
Domingos,P.:Metacost:ageneralmethodformakingclassifierscost-sensitive.In:ProceedingsoftheFifth
ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.Associationfor
ComputingMachinery,NewYork,NY,USA,KDD’99,pp.155–164,(1999).https://doi.org/10.1145/
312129.312220
Esfahani,S.,DeToni,G.,Lepri,B.,etal.:Preferenceelicitationininteractiveanduser-centeredalgorithmic
recourse:aninitialexploration.In:Proceedingsofthe32ndACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’24,pp.249–254(2024a).https://doi.org/10.1145/3627043.3659556
Esfahani,S.,DeToni,G.,Lepri,B.,etal.:Preferenceelicitationininteractiveanduser-centeredalgorithmic
recourse:aninitialexploration.In:Proceedingsofthe32ndACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’24,pp.249–254(2024b).https://doi.org/10.1145/3627043.3659556
Faul,F.,Erdfelder,E.,Buchner,A.,etal.:Statisticalpoweranalysesusingg*power3.1:testsforcorrelation
andregressionanalyses.Behav.Res.Methods41(4),1149–1160(2009)
Fawcett,T.:Rocgraphs:notesandpracticalconsiderationsforresearchers.Mach.Learn.31,1–38(2004)
Feldkamp,N.,Strassburger,S.:Fromexplainableaitoexplainablesimulation:usingmachinelearning
andxaitounderstandsystemrobustness.In:Proceedingsofthe2023ACMSIGSIMConferenceon
PrinciplesofAdvancedDiscreteSimulation.AssociationforComputingMachinery,NewYork,NY,
USA,SIGSIM-PADS’23,pp.96–106(2023).https://doi.org/10.1145/3573900.3591114
Fogliato,R.,Chappidi,S.,Lungren,M.,etal.:Whogoesfirst?Influencesofhuman–AIworkflowondecision
makinginclinicalimaging.In:Proceedingsofthe2022ACMConferenceonFairness,Accountability,
andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAccT’22,pp.1362–
1374(2022a).https://doi.org/10.1145/3531146.3533193
Fogliato,R.,Chappidi,S.,Lungren,M.,etal.:Whogoesfirst?Influencesofhuman-aiworkflowondecision
makinginclinicalimaging.In:Proceedingsofthe2022ACMConferenceonFairness,Accountability,
andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAccT’22,pp.1362–
1374(2022b).https://doi.org/10.1145/3531146.3533193
Fok,R.,Weld,D.S.:Insearchofverifiability:explanationsrarelyenablecomplementaryperformancein
AI-advised decision making. AI Mag. 45(3), 317–332 (2024). https://doi.org/10.1002/aaai.12182.
(https://onlinelibrary.wiley.com/doi/pdf/10.1002/aaai.12182)
Ford,C.,Keane,M.T.:Explainingclassificationstonon-experts:anxaiuserstudyofpost-hocexplanations
foraclassifierwhenpeoplelackexpertise.In:PatternRecognition,ComputerVision,andImage
Processing.ICPR2022InternationalWorkshopsandChallenges:Montreal,QC,Canada,August21–
25,2022,Proceedings,PartIII.Springer-Verlag,Berlin,Heidelberg,pp.246–260(2023).https://doi.
org/10.1007/978-3-031-37731-0_15
Foroudi,P.,Marvi,R.,Zha,D.:Aisensationandengagement:unpackingthesensoryexperienceinhuman–
AIinteraction.Int.J.Inf.Manage.84,102918(2025).https://doi.org/10.1016/j.ijinfomgt.2025.102918
123

3 Page 38 of 43 F.M.Cau,L.D.Spano
Friedman,M.:Theuseofrankstoavoidtheassumptionofnormalityimplicitintheanalysisofvariance.
J. Am. Stat. Assoc. 32(200), 675–701 (1937). https://doi.org/10.1080/01621459.1937.10503522.
(https://www.tandfonline.com/doi/pdf/10.1080/01621459.1937.10503522)
Friedman,M.:Acomparisonofalternativetestsofsignificancefortheproblemof$m$rankings.Ann.
Math.Stat.11,86–92(1940)
Gajos,K.Z.,Chauncey,K.:Theinfluenceofpersonalitytraitsandcognitiveloadontheuseofadaptive
userinterfaces.In:Proceedingsofthe22ndInternationalConferenceonIntelligentUserInterfaces.
AssociationforComputingMachinery,NewYork,NY,USA,IUI’17,pp.301–306(2017).https://
doi.org/10.1145/3025171.3025192
Gajos,K.Z.,Mamykina,L.:DopeopleengagecognitivelywithAI?ImpactofAIassistanceonincidental
learning.In:Proceedingsofthe27thInternationalConferenceonIntelligentUserInterfaces.Associ-
ationforComputingMachinery,NewYork,NY,USA,IUI’22,pp.794–806(2022).https://doi.org/
10.1145/3490099.3511138
Ghai,B.,Liao,Q.V.,Zhang,Y.,etal.:Explainableactivelearning(xal):towardaiexplanationsasinterfaces
formachineteachers.Proc.ACMHum.Comput.Interact.(2021).https://doi.org/10.1145/3432934
Gomez,O.,Holter,S.,Yuan,J.,etal.:Vice:visualcounterfactualexplanationsformachinelearningmodels.
In:Proceedingsofthe25thInternationalConferenceonIntelligentUserInterfaces.Associationfor
ComputingMachinery,NewYork,NY,USA,IUI’20,pp.531–535(2020).https://doi.org/10.1145/
3377325.3377536
Gomez,C.,Cho,S.M.,Ke,S.,etal.:Human–AIcollaborationisnotverycollaborativeyet:ataxonomy
ofinteractionpatternsinAI-assisteddecisionmakingfromasystematicreview.Front.Comput.Sci.
(2025).https://doi.org/10.3389/fcomp.2024.1521066
Grace,K.,Finch,E.,Gulbransen-Diaz,N.,etal.:Q-chef:theimpactofsurprise-elicitingsystemsonfood-
relateddecision-making.In:Proceedingsofthe2022CHIConferenceonHumanFactorsinComputing
Systems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’22(2022).https://doi.
org/10.1145/3491102.3501862
Green,B.,Chen,Y.:Disparateinteractions:analgorithm-in-the-loopanalysisoffairnessinriskassessments.
In:ProceedingsoftheConferenceonFairness,Accountability,andTransparency.Associationfor
ComputingMachinery,NewYork,NY,USA,FAT*’19,pp.90–99(2019a).https://doi.org/10.1145/
3287560.3287563
Green,B.,Chen,Y.:Theprinciplesandlimitsofalgorithm-in-the-loopdecisionmaking.Proc.ACMHum.
Comput.Interact.(2019b).https://doi.org/10.1145/3359152
Guo,C.,Pleiss,G.,Sun,Y.,etal.:Oncalibrationofmodernneuralnetworks.In:PrecupD,TehYW(eds),
Proceedings of the 34th International Conference on Machine Learning, Proceedings of Machine
LearningResearch,vol70.PMLR,pp.1321–1330(2017).https://proceedings.mlr.press/v70/guo17a.
html
Hase,P.,Bansal,M.:EvaluatingexplainableAI:Whichalgorithmicexplanationshelpuserspredictmodel
behavior?In:Jurafsky,D.,Chai,J.,Schluter,N.,etal.(eds),Proceedingsofthe58thAnnualMeet-
ing of the Association for Computational Linguistics. Association for Computational Linguistics,
Online,pp.5540–5552(2020).https://doi.org/10.18653/v1/2020.acl-main.491.https://aclanthology.
org/2020.acl-main.491
He,G.,Buijsman,S.,Gadiraju,U.:Howstatedaccuracyofanaisystemandanalogiestoexplainaccuracy
affecthumanrelianceonthesystem.Proc.ACMHum.Comput.Interact.(2023a).https://doi.org/10.
1145/3610067
He,G.,Kuiper,L.,Gadiraju,U.:Knowingaboutknowing:anillusionofhumancompetencecanhinder
appropriaterelianceonAIsystems.In:Proceedingsofthe2023CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’23(2023b).
https://doi.org/10.1145/3544548.3581025
He,G.,Balayn,A.,Buijsman,S.,etal.:Openingtheanalogicalportaltoexplainability:Cananalogies
helplaypeopleinai-assisteddecisionmaking?J.Artif.Int.Res.(2024).https://doi.org/10.1613/jair.
1.15118
He,G.,Aishwarya,N.,Gadiraju,U.:IsconversationalXAIallyouneed?Human–AIdecisionmakingwith
aconversationalxaiassistant.In:Proceedingsofthe30thInternationalConferenceonIntelligentUser
Interfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’25,pp.907–924(2025).
https://doi.org/10.1145/3708359.3712133
Herm,L.V.:ImpactofexplainableAIoncognitiveload:insightsfromanempiricalstudy.In:European
ConferenceonInformationSystems,ECIS2023Research,p.269(2023)
123

ExploringtheimpactofexplainableAIandcognitive… Page 39 of 43 3
Herzog,D.,Wörndl,W.:Auserstudyongroupsinteractingwithtouristtriprecommendersystemsin
public spaces. In: Proceedings of the 27th ACM Conference on User Modeling, Adaptation and
Personalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP’19,pp.130–
138(2019).https://doi.org/10.1145/3320435.3320449
Kahr,P.K.,Rooks,G.,Willemsen,M.C.,etal.:Itseemssmart,butitactsstupid:developmentoftrustinai
adviceinarepeatedlegaldecision-makingtask.In:Proceedingsofthe28thInternationalConference
onIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’23,
pp.528–539(2023).https://doi.org/10.1145/3581641.3584058
Kahr,P.K.,Rooks,G.,Willemsen,M.C.,etal.:Understandingtrustandreliancedevelopmentinaiadvice:
assessing model accuracy, model explanations, and experiences from previous interactions. ACM
Trans.Interact.Intell.Syst.(2024).https://doi.org/10.1145/3686164
Kashdan,T.B.,Stiksma,M.C.,Disabato,D.J.,etal.:Thefive-dimensionalcuriosityscale:capturingthe
bandwidthofcuriosityandidentifyingfouruniquesubgroupsofcuriouspeople.J.Res.Pers.73,
130–149(2018).https://doi.org/10.1016/j.jrp.2017.11.011.(https://www.sciencedirect.com/science/
article/pii/S0092656617301149)
Kenny,E.M.,Keane,M.T.:Twin-systemstoexplainartificialneuralnetworksusingcase-basedreasoning:
comparativetestsoffeature-weightingmethodsinANN-CBRtwinsforXAI.In:Proceedingsofthe
Twenty-EighthInternationalJointConferenceonArtificialIntelligence,IJCAI-19.InternationalJoint
ConferencesonArtificialIntelligenceOrganization,pp.2708–2715(2019).https://doi.org/10.24963/
ijcai.2019/376
Kenny, E.M., Keane, M.T.: Explaining deep learning using examples: optimal feature weighting
methods for twin systems using post-hoc, explanation-by-example in XAI. Knowl. Based Syst.
233,107530(2021).https://doi.org/10.1016/j.knosys.2021.107530.(https://www.sciencedirect.com/
science/article/pii/S0950705121007929)
Kim,S.,Meister,N.,Ramaswamy,V.,etal.:Hive:evaluatingthehumaninterpretabilityofvisualexpla-
nations.In:Avidan,S.,Brostow,G.,Cissé,M.,etal.(eds),ComputerVision—ECCV2022:17th
EuropeanConference,Proceedings.SpringerScienceandBusinessMediaDeutschlandGmbH,Ger-
many,LectureNotesinComputerScience(includingsubseriesLectureNotesinArtificialIntelligence
andLectureNotesinBioinformatics),pp.280–298(publisherCopyright:2022,TheAuthor(s),under
exclusivelicensetoSpringerNatureSwitzerlandAG.;17thEuropeanConferenceonComputerVision,
ECCV2022;Conferencedate:23-10-2022Through27-10-2022)(2022).https://doi.org/10.1007/
978-3-031-19775-8_17
Küper,A.,Lodde,G.C.,Livingstone,E.,etal.:Psychologicalfactorsinfluencingappropriaterelianceon
ai-enabledclinicaldecisionsupportsystems:experimentalweb-basedstudyamongdermatologists.
J.Med.Int.Res.27,e58660(2025).https://doi.org/10.2196/58660.(https://www.jmir.org/2025/1/
e58660)
Küper,A.,Krämer,N.:Psychologicaltraitsandappropriatereliance:factorsshapingtrustinAI.Int.J.
Hum.Comput.Interact.41(7),4115–4131(2025).https://doi.org/10.1080/10447318.2024.2348216
Lai,V.,Tan,C.:Onhumanpredictionswithexplanationsandpredictionsofmachinelearningmodels:a
casestudyondeceptiondetection.In:ProceedingsoftheConferenceonFairness,Accountability,
andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAT*’19,pp.29–38
(2019).https://doi.org/10.1145/3287560.3287590
Lai,V.,Chen,C.,Smith-Renner,A.,etal.:Towardsascienceofhuman–AIdecisionmaking:Anoverview
ofdesignspaceinempiricalhuman-subjectstudies.In:Proceedingsofthe2023ACMConferenceon
Fairness,Accountability,andTransparency.AssociationforComputingMachinery,NewYork,NY,
USA,FAccT’23,pp.1369–1385(2023a).https://doi.org/10.1145/3593013.3594087
Lai,V.,Zhang,Y.,Chen,C.,etal.:Selectiveexplanations:leveraginghumaninputtoalignexplainableAI.
Proc.ACMHum.Comput.Interact.(2023b).https://doi.org/10.1145/3610206
Lee,M.H.,Siewiorek,D.P.,Smailagic,A.,etal.:Co-designandevaluationofanintelligentdecisionsupport
systemforstrokerehabilitationassessment.Proc.ACMHum.Comput.Interact.(2020).https://doi.
org/10.1145/3415227
Lee,M.H.,Siewiorek,D.P.,Smailagic,A.,etal.:Ahuman–AIcollaborativeapproachforclinicaldecision
makingonrehabilitationassessment.In:Proceedingsofthe2021CHIConferenceonHumanFactors
inComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).
https://doi.org/10.1145/3411764.3445472
Li,D.,Browne,G.:Theroleofneedforcognitionandmoodinonlineflowexperience.J.Comput.Inf.
Syst.46(3),11–17(2006)
123

3 Page 40 of 43 F.M.Cau,L.D.Spano
Li,J.,Yang,Y.,Liao,Q.V.,etal.:Asconfidencealigns:understandingtheeffectofaiconfidenceonhuman
self-confidenceinhuman–AIdecisionmaking.In:Proceedingsofthe2025CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’25
(2025).https://doi.org/10.1145/3706598.3713336
Liao,M.,Sundar,S.S.,Walther,B.J.:Usertrustinrecommendationsystems:acomparisonofcontent-based,
collaborative and demographic filtering. In: Proceedings of the 2022 CHI Conference on Human
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’22
(2022).https://doi.org/10.1145/3491102.3501936
Liao,Q.V.,Varshney,K.R.:Human-centeredexplainableAI(XAI):fromalgorithmstouserexperiences
(2021)
Litman,J.A.:Interestanddeprivationfactorsofepistemiccuriosity.Person.Indvid.Differ.44(7),1585–1595
(2008). https://doi.org/10.1016/j.paid.2008.01.014. (https://www.sciencedirect.com/science/article/
pii/S0191886908000275)
Lu,J.,Yan,Y.,Huang,K.,etal.:Dowelearnfromeachother:understandingthehuman–AIco-learning
processembeddedinhuman–AIcollaboration.GroupDecis.Negot.(2024).https://doi.org/10.1007/
s10726-024-09912-x
Lundberg,S.M.,Lee,S.I.:Aunifiedapproachtointerpretingmodelpredictions.In:Proceedingsofthe31st
InternationalConferenceonNeuralInformationProcessingSystems,CurranAssociatesInc.,Red
Hook,NY,USA,NIPS’17,pp.4768–4777(2017)
Ma,S.,Lei,Y.,Wang,X.,etal.:Whoshoulditrust:Aiormyself?Leveraginghumanandaicorrectness
likelihoodtopromoteappropriatetrustinAI-assisteddecision-making.In:Proceedingsofthe2023
CHIConferenceonHumanFactorsinComputingSystems.AssociationforComputingMachinery,
NewYork,NY,USA,CHI’23(2023).https://doi.org/10.1145/3544548.3581058
Ma,S.,Wang,X.,Lei,Y.,etal.:“areyoureallysure?”Understandingtheeffectsofhumanself-confidence
calibrationinai-assisteddecisionmaking.In:Proceedingsofthe2024CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’24
(2024).https://doi.org/10.1145/3613904.3642671
Manokhin,V.:Multi-classprobabilisticclassificationusinginductiveandcrossVenn–Aberspredictors.In:
Gammerman,A.,Vovk,V.,Luo,Z.,etal.(eds),ProceedingsoftheSixthWorkshoponConformal
andProbabilisticPredictionandApplications,ProceedingsofMachineLearningResearch,vol.60.
PMLR,pp.228–240(2017).https://proceedings.mlr.press/v60/manokhin17a.html
Martijn,M.,Conati,C.,Verbert,K.:“knowingme,knowingyou”:personalizedexplanationsforamusic
recommendersystem.UserModel.UserAdap.Int.32(1),215–252(2022).https://doi.org/10.1007/
s11257-021-09304-9
Marusich, L.R., Bakdash, J.Z., Zhou, Y., et al.: Using ai uncertainty quantification to improve human
decision-making. In: Proceedings of the 41st International Conference on Machine Learning.
JMLR.org,ICML’24(2024)
Millecamp,M.,Htun,N.N.,Conati,C.,etal.:Toexplainornottoexplain:theeffectsofpersonalcharacter-
isticswhenexplainingmusicrecommendations.In:Proceedingsofthe24thInternationalConference
onIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’19,
pp.397–407(2019).https://doi.org/10.1145/3301275.3302313
Millecamp,M.,Htun,N.N.,Conati,C.,etal.:What’sinauser?Towardspersonalisingtransparencyfor
musicrecommenderinterfaces.In:Proceedingsofthe28thACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’20,pp.173–182(2020).https://doi.org/10.1145/3340631.3394844
Moreira,C.,Chou,Y.L.,Hsieh,C.J.,etal.:BenchmarkingcounterfactualalgorithmsforXAI:fromwhite
boxtoblackbox(2022).https://api.semanticscholar.org/CorpusID:252280631
Morrison,K.,Spitzer,P.,Turri,V.,etal.:TheimpactofimperfectXAIonhuman–AIdecision-making.
Proc.ACMHum.Comput.Interact.(2024).https://doi.org/10.1145/3641022
Mothilal,R.,Sharma,A.,Tan,C.:ExplainingMachineLearningClassifiersThroughDiverseCounterfactual
Explanations,pp.607–617(2020a).https://doi.org/10.1145/3351095.3372850
Mothilal,R.K.,Sharma,A.,Tan,C.:Explainingmachinelearningclassifiersthroughdiversecounterfactual
explanations.In:Proceedingsofthe2020ConferenceonFairness,Accountability,andTransparency.
AssociationforComputingMachinery,NewYork,NY,USA,FAT*’20,pp.607–617(2020b).https://
doi.org/10.1145/3351095.3372850
Mothilal, R.K., Mahajan, D., Tan, C., et al.: Towards unifying feature attribution and counterfactual
explanations: different means to the same end. In: AAAI/ACM Conference on AI, Ethics, and
123

ExploringtheimpactofexplainableAIandcognitive… Page 41 of 43 3
Society (AIES) (2021). https://www.microsoft.com/en-us/research/publication/towards-unifying-
feature-attribution-and-counterfactual-explanations-different-means-to-the-same-end/
Musto,C.,Starke,A.D.,Trattner,C.,etal.:Exploringtheeffectsofnaturallanguagejustificationsinfood
recommendersystems.In:Proceedingsofthe29thACMConferenceonUserModeling,Adaptation
andPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP’21,pp.
147–157(2021).https://doi.org/10.1145/3450613.3456827
Nourani,M.,Roy,C.,Block,J.E.,etal.:Anchoringbiasaffectsmentalmodelformationanduserreliance
inexplainableAIsystems.In:Proceedingsofthe26thInternationalConferenceonIntelligentUser
Interfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’21,pp.340–350(2021).
https://doi.org/10.1145/3397481.3450639
Padilla, L.M.K., Powell, M., Kay, M., et al.: Uncertain about uncertainty: how qualitative expres-
sions of forecaster confidence impact decision-making with uncertainty visualizations. Front.
Psychol. (2021). https://doi.org/10.3389/fpsyg.2020.579267. (https://www.frontiersin.org/journals/
psychology/articles/10.3389/fpsyg.2020.579267)
Panigutti,C.,Beretta,A.,Giannotti,F.,etal.:Understandingtheimpactofexplanationsonadvice-taking:a
userstudyforai-basedclinicaldecisionsupportsystems.In:Proceedingsofthe2022CHIConference
onHumanFactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,
USA,CHI’22(2022).https://doi.org/10.1145/3491102.3502104
Platt,J.:ProbabilitiesforSupportVectorMachines(2000)
Prabhudesai,S.,Yang,L.,Asthana,S.,etal.:Understandinguncertainty:howlaydecision-makersperceive
andinterpretuncertaintyinhuman–AIdecisionmaking.In:Proceedingsofthe28thInternational
ConferenceonIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,
USA,IUI’23,pp.379–396(2023).https://doi.org/10.1145/3581641.3584033
Rastogi,C.,Zhang,Y.,Wei,D.,etal.:Decidingfastandslow:theroleofcognitivebiasesinai-assisted
decision-making.Proc.ACMHum.Comput.Interact.(2022).https://doi.org/10.1145/3512930
Rechkemmer,A.,Yin,M.:Whenconfidencemeetsaccuracy:exploringtheeffectsofmultipleperformance
indicatorsontrustinmachinelearningmodels.In:Proceedingsofthe2022CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’22
(2022).https://doi.org/10.1145/3491102.3501967
Ribeiro,M.T.,Singh,S.,Guestrin,C.:“whyshoulditrustyou?”:explainingthepredictionsofanyclassifier.
In:Proceedingsofthe22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryand
DataMining.AssociationforComputingMachinery,NewYork,NY,USA,KDD’16,pp.1135–1144
(2016).https://doi.org/10.1145/2939672.2939778
Ribeiro, M.T., Singh, S., Guestrin, C.: Anchors: high-precision model-agnostic explanations. In: Pro-
ceedingsoftheThirty-SecondAAAIConferenceonArtificialIntelligenceandThirtiethInnovative
Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational
AdvancesinArtificialIntelligence.AAAIPress,AAAI’18/IAAI’18/EAAI’18(2018)
Rong,Y.,Leemann,T.,Nguyen,T.,etal.:Towardshuman-centeredexplainableAI:asurveyofuserstudies
formodelexplanations.IEEETrans.PatternAnal.Mach.Intell.46(04),2104–2122(2024).https://
doi.org/10.1109/TPAMI.2023.3331846
Salimzadeh,S.,He,G.,Gadiraju,U.:Amissingpieceinthepuzzle:consideringtheroleoftaskcomplexity
in human–AI decision making. In: Proceedings of the 31st ACM Conference on User Modeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’23,pp.215–227(2023).https://doi.org/10.1145/3565472.3592959
Salimzadeh,S.,He,G.,Gadiraju,U.:Dealingwithuncertainty:Understandingtheimpactofprognostic
versusdiagnostictasksontrustandrelianceinhuman–AIdecisionmaking.In:Proceedingsofthe
CHIConferenceonHumanFactorsinComputingSystems.AssociationforComputingMachinery,
NewYork,NY,USA,CHI’24(2024).https://doi.org/10.1145/3613904.3641905
Sauro,J.,Dumas,J.S.:Comparisonofthreeone-question,post-taskusabilityquestionnaires.In:Proceedings
oftheSIGCHIConferenceonHumanFactorsinComputingSystems.AssociationforComputing
Machinery,NewYork,NY,USA,CHI’09,pp.1599–1608(2009).https://doi.org/10.1145/1518701.
1518946
Scharowski,N.,Perrig,S.A.C.,Svab,M.,etal.:Exploringtheeffectsofhuman-centeredAIexplanationson
trustandreliance.Front.Comput.Sci.(2023).https://doi.org/10.3389/fcomp.2023.1151150.https://
www.frontiersin.org/articles/10.3389/fcomp.2023.1151150
Schoeffer,J.,Kuehl,N.,Machowski,Y.:“thereisnotenoughinformation”:ontheeffectsofexplanations
onperceptionsofinformationalfairnessandtrustworthinessinautomateddecision-making.In:Pro-
123

3 Page 42 of 43 F.M.Cau,L.D.Spano
ceedingsofthe2022ACMConferenceonFairness,Accountability,andTransparency.Association
forComputingMachinery,NewYork,NY,USA,FAccT’22,pp.1616–1628(2022).https://doi.org/
10.1145/3531146.3533218
Shaker,M.H.,Hüllermeier,E.:Aleatoricandepistemicuncertaintywithrandomforests.In:Berthold,M.R.,
Feelders,A.,Krempl,G.(eds.)AdvancesinIntelligentDataAnalysisXVIII,pp.444–456.Springer,
Cham(2020)
SilvaFilho,T.,Song,H.,Perello-Nieto,M.,etal.:Classifiercalibration:asurveyonhowtoassessand
improvepredictedclassprobabilities.Mach.Learn.112(9),3211–3260(2023).https://doi.org/10.
1007/s10994-023-06336-7
Souchet,A.,Amokrane-Ferka,K.,Burkhardt,J.M.:Ai-assistancetodecision-makers:evaluatingusability,
inducedcognitiveload,andtrust’simpact.In:ProceedingsoftheEuropeanConferenceonCognitive
Ergonomics2024.AssociationforComputingMachinery,NewYork,NY,USA,ECCE’24(2024).
https://doi.org/10.1145/3673805.3673845
Steyvers,M.,Kumar,A.:ThreechallengesforAI-assisteddecision-making.Perspect.Psychol.Sci.19(5),
722–734(2024).https://doi.org/10.1177/17456916231181102
Strickland,L.,Farrell,S.,Wilson,M.K.,etal.:Howdohumanslearnaboutthereliabilityofautomation?
Cogn.Res.Princ.Implic.9(1),8(2024).https://doi.org/10.1186/s41235-024-00533-1
Subramanian, H.V., Canfield, C., Shank, D.B.: Designing explainable ai to improve human-
ai team performance: a medical stakeholder-driven scoping review. Artif. Intell. Med.
149,102780(2024).https://doi.org/10.1016/j.artmed.2024.102780.https://www.sciencedirect.com/
science/article/pii/S0933365724000228
Swaroop,S.,Buçinca,Z.,Gajos,K.Z.,etal.:PersonalisingaiassistancebasedonoverreliancerateinAI-
assisteddecisionmaking.In:Proceedingsofthe30thInternationalConferenceonIntelligentUser
Interfaces. Association for ComputingMachinery, New York, NY, USA, IUI ’25, pp. 1107–1122
(2025).https://doi.org/10.1145/3708359.3712128
Szymanski,M.,AbeeleV.V.,Verbert,K.:Designingandevaluatingexplanationsforapredictivehealth
dashboard:auser-centredcasestudy.In:ExtendedAbstractsofthe2024CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHIEA
’24(2024).https://doi.org/10.1145/3613905.3637140
Teso, S., Alkan, Ö., Stammer, W., et al.: Leveraging explanations in interactive machine learning: an
overview.Front.Artif.Intell.6,1066049(2023)
Tsirtsis, S., Gomez-Rodriguez, M., Gerstenberg, T.: Towards a computational model of responsibility
judgmentsinsequentialhuman-aicollaboration.In:Proceedingsofthe46thAnnualMeetingofthe
CognitiveScienceSociety(CogSci2024),Rotterdam,Netherlands(2024).https://escholarship.org/
uc/item/5h1742zk
vanBerkel,N.,Goncalves,J.,Russo,D.etal.:Effectofinformationpresentationonfairnessperceptions
ofmachinelearningpredictors.In:Proceedingsofthe2021CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).
https://doi.org/10.1145/3411764.3445365
Vasconcelos,H.,Jörke,M.,Grunde-McLaughlin,M.,etal.:Explanationscanreduceoverrelianceonai
systemsduringdecision-making.ProcACMHum.Comput.Interact.(2023).https://doi.org/10.1145/
3579605
Viswanathan,S.,Omidvar-Tehrani,B.,Renders,J.M.:Whatisyourcurrentmindset?In:Proceedingsof
the 2022 CHI Conference on Human Factors in Computing Systems. Association for Computing
Machinery,NewYork,NY,USA,CHI’22(2022).https://doi.org/10.1145/3491102.3501912
Vovk,V.,Petej,I.:Venn-aberspredictors.In:ProceedingsoftheThirtiethConferenceonUncertaintyin
ArtificialIntelligence.AUAIPress,Arlington,Virginia,USA,UAI’14,pp.829–838(2014)
Vovk,V.,Petej,I.,Fedorova,V.:Large-scaleprobabilisticpredictorswithandwithoutguaranteesofvalidity.
In: Proceedings of the 28th International Conference on Neural Information Processing Systems,
Volume1.MITPress,Cambridge,MA,USA,NIPS’15,pp.892–900(2015)
Wachter,S.,Mittelstadt,B.D.,Russell,C.:Counterfactualexplanationswithoutopeningtheblackbox:
automateddecisionsandtheGDPR.Cybersecurity(2017).https://api.semanticscholar.org/CorpusID:
3995299
Wang,D.,Yang,Q.,Abdul,A.,etal.:Designingtheory-drivenuser-centricexplainableai.In:Proceedings
ofthe2019CHIConferenceonHumanFactorsinComputingSystems.AssociationforComputing
Machinery,NewYork,NY,USA,CHI’19,pp.1–15(2019).https://doi.org/10.1145/3290605.3300831
123

ExploringtheimpactofexplainableAIandcognitive… Page 43 of 43 3
Wang,X.,Yin,M.:Areexplanationshelpful?Acomparativestudyoftheeffectsofexplanationsinai-
assisteddecision-making.In:26thInternationalConferenceonIntelligentUserInterfaces.Association
forComputingMachinery,NewYork,NY,USA,IUI’21,pp.318–328(2021).https://doi.org/10.1145/
3397481.3450650
Wang,X.,Yin,M.:EffectsofexplanationsinAI-assisteddecisionmaking:principlesandcomparisons.
ACMTrans.Interact.Intell.Syst.(2022).https://doi.org/10.1145/3519266
Xuan,Y.,Small,E.,Sokol,K.,etal.:Comprehensionisadouble-edgedsword:over-interpretingunspeci-
fiedinformationinintelligiblemachinelearningexplanations.Int.J.HumComputStud.193,103376
(2025). https://doi.org/10.1016/j.ijhcs.2024.103376. https://www.sciencedirect.com/science/article/
pii/S1071581924001599
Yin,M.,Vaughan,W.J.,Wallach,H.:Understandingtheeffectofaccuracyontrustinmachinelearning
models. In: Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems.
AssociationforComputingMachinery,NewYork,NY,USA,CHI’19,pp.1–12(2019).https://doi.
org/10.1145/3290605.3300509
Yurrita,M.,Draws,T.,Balayn,A.,etal.:Disentanglingfairnessperceptionsinalgorithmicdecision-making:
theeffectsofexplanations,humanoversight,andcontestability.In:Proceedingsofthe2023CHI
ConferenceonHumanFactorsinComputingSystems.AssociationforComputingMachinery,New
York,NY,USA,CHI’23(2023).https://doi.org/10.1145/3544548.3581161
Yurrita,M.,Verma,H.,Balayn,A.,etal.:Towardseffectivehumaninterventioninalgorithmicdecision-
making:Understandingtheeffectofdecision-makers’configurationondecision-subjects’fairness
perceptions.In:Proceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems.
AssociationforComputingMachinery,NewYork,NY,USA,CHI’25(2025).https://doi.org/10.1145/
3706598.3713145
Zadrozny,B.,Elkan,C.:ObtainingcalibratedprobabilityestimatesfromdecisiontreesandnaiveBayesian
classifiers.ICML,p.1(2001)
Zehrung,R.,Singhal,A.,Correll,M.,etal.:Visexmachina:ananalysisoftrustinhumanversusalgorith-
micallygeneratedvisualizationrecommendations.In:Proceedingsofthe2021CHIConferenceon
HumanFactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,
CHI’21(2021).https://doi.org/10.1145/3411764.3445195
Zhang, Y., Liao, Q.V., Bellamy, R.K.E.: Effect of confidence and explanation on accuracy and trust
calibration in ai-assisted decision making. In: Proceedings of the 2020 Conference on Fairness,
Accountability,andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAT*
’20,pp.295–305.(2020).https://doi.org/10.1145/3351095.3372852
Zhao,J.,Wang,Y.,Mancenido,M.V.,etal.:Evaluatingtheimpactofuncertaintyvisualizationonmodel
reliance.IEEETrans.VisualComput.Gr.30(7),4093–4107(2024).https://doi.org/10.1109/TVCG.
2023.3251950
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmaps
andinstitutionalaffiliations.
FedericoMariaCauobtainedhisbachelor’sandmaster’sdegreesfromtheUniversityofCagliari,where
healsoearnedaPh.D.inMathematicsandComputerScience,withafocusontheeffectsofexplanation
anduncertaintyonAI-assisteduserdecisions.HeiscurrentlyapostdoctoralresearcherattheUniversity
ofCagliari.HisresearchinterestsincludeAI-assisteddecision-making,explainableAI,Human-Centered
AI,andintelligentinterfaces.
LucioDavideSpanoisanAssociateProfessorattheUniversityofCagliari,Italy,wherehehasbeenpart
oftheDepartmentofMathematicsandComputerSciencesince2012.HeearnedhisPh.D.inComputer
SciencefromtheUniversityofPisain2013.HisresearchfocusesonHuman-ComputerInteraction(HCI),
extendedReality(XR),End-UserDevelopment,andexplainableAI.Hehasauthorednumerouspublica-
tionsoninteractiontechniques,intelligentuserinterfaces,andimmersivetechnologies.Spanohasledand
contributedtovariousEuropeanandregionalresearchprojects,includingthoseunderH2020,FP7,andthe
ItalianPNRRframework.HeisactiveintheinternationalHCIcommunity,servingonprogramcommit-
teesforconferencessuchasACMIUI,INTERACT,NordiCHI,andEICS,andholdsleadershiprolesin
IFIPandSIGCHI-Italy.
123