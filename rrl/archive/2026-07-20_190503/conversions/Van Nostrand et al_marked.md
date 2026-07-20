| Actionable | Recourse | for | Automated | Decisions: |     | Examining |     | the |
| ---------- | -------- | --- | --------- | ---------- | --- | --------- | --- | --- |
Effects of Counterfactual Explanation Type and Presentation on
|                               |                      | Lay | User Understanding |          |                               |     |     |     |
| ----------------------------- | -------------------- | --- | ------------------ | -------- | ----------------------------- | --- | --- | --- |
|                               | PeterM.VanNostrand   |     |                    |          | DennisM.Hofmann               |     |     |     |
|                               | pvannostrand@wpi.edu |     |                    |          | dmhofmann@wpi.edu             |     |     |     |
| WorcesterPolytechnicInstitute |                      |     |                    |          | WorcesterPolytechnicInstitute |     |     |     |
|                               | Worcester,USA        |     |                    |          | Worcester,USA                 |     |     |     |
|                               | LeiMa                |     |                    |          | ElkeA.Rundensteiner           |     |     |     |
|                               | lma5@wpi.edu         |     |                    |          | rundenst@wpi.edu              |     |     |     |
| WorcesterPolytechnicInstitute |                      |     |                    |          | WorcesterPolytechnicInstitute |     |     |     |
|                               | Worcester,USA        |     |                    |          | Worcester,USA                 |     |     |     |
| ABSTRACT                      |                      |     |                    | KEYWORDS |                               |     |     |     |
Automateddecision-makingsystemsareincreasinglydeployedin ExplainableAI,UserStudies,AlgorithmicTransparency,Human-
domainssuchashiringandcreditapprovalwherenegativeout- ComputerInteraction.
comescanhavesubstantialramificationsfordecisionsubjects.Thus,
ACMReferenceFormat:
recentresearchhasfocusedonprovidingexplanationsthathelp
PeterM.VanNostrand,DennisM.Hofmann,LeiMa,andElkeA.Runden-
decisionsubjectsunderstandthedecisionsystemandenablethem
steiner.2024.ActionableRecourseforAutomatedDecisions:Examiningthe
totakeactionablerecoursetochangetheiroutcome.Popularcoun-
EffectsofCounterfactualExplanationTypeandPresentationonLayUser
terfactualexplanationtechniquesaimtoachievethisbydescribing
Understanding.InThe2024ACMConferenceonFairness,Accountability,and
alterationstoaninstancethatwouldtransformanegativeoutcome
Transparency(FAccT’24),June03–06,2024,RiodeJaneiro,Brazil.ACM,New
toapositiveone.Unfortunately,littleuserevaluationhasbeen
York,NY,USA,19pages.https://doi.org/10.1145/3630106.3658997
performedtoassesswhichofthemanycounterfactualapproaches
bestachievethisgoal.Inthiswork,weconductacrowd-sourced
1 INTRODUCTION
| between-subjectsuserstudy(𝑁 | =   | 252)toexaminetheeffectsof |     |     |     |     |     |     |
| --------------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
Asmachinelearningsystemshavegrownmorecapable,theyhave
counterfactualexplanationtypeandpresentationonlaydecision
rapidlybeendeployedtoautomatedecision-makingtasksincon-
subjects’understandingsofautomateddecisionsystems.Wefind
sequentialdomainssuchasfinance[35,41],recruitment[16,32],
thattheregion-basedcounterfactualtypesignificantlyincreases
healthcare[37],andpolicing[13,23]wherenegativedecisionscan
objectiveunderstanding,subjectiveunderstanding,andresponse
havesubstantialimpactsondecisionsubjects’lives.Motivatedby
confidenceascomparedtothepoint-basedtype.Wealsofindthat
thisalarmingtrend,explainableAI(XAI)techniqueshavebeende-
counterfactualpresentationsignificantlyeffectsresponsetimeand
velopedtoprovidedecisionsubjectswithanunderstandingofhow
moderatestheeffectofcounterfactualtypeforresponseconfidence,
adecisionismade,andthusthepossibilityoftakingrecourse[52].
| but not understanding. | A qualitative | analysis reveals | how deci- |     |     |     |     |     |
| ---------------------- | ------------- | ---------------- | --------- | --- | --- | --- | --- | --- |
Requirementsforexplanationofautomateddecisionsarealsoin-
sionsubjectsinteractwithdifferentexplanationconfigurationsand
creasinglybeingcodifiedintolaw[1,41,43].
highlightsunmetneedsforexplanationjustification.Ourresults
Ofparticularinteresthavebeenso-calledcounterfactualexpla-
providevaluableinsightsandrecommendationsforthedevelop-
|                                                           |     |     |     | as      | they are believed | to meet legal | requirements | for lay |
| --------------------------------------------------------- | --- | --- | --- | ------- | ----------------- | ------------- | ------------ | ------- |
| mentofcounterfactualexplanationtechniquestowardsachieving |     |     |     | nations |                   |               |              |         |
userappropriateexplanation[61].Theseexplanationsprovidede-
practicalactionablerecourseandempoweringlayuserstoseek
|     |     |     |     | cision subjects | with actionable | recourse | for undesired | negative |
| --- | --- | --- | --- | --------------- | --------------- | -------- | ------------- | -------- |
justiceandopportunityinautomateddecisionworkflows.
outcomes(e.g.,thedenialofaloan)bydescribingalterationsto
thefeaturesoftheirinstancethatwouldleadtoapositiveoutcome
CCSCONCEPTS
(e.g.,suggestingaloanapplicantincreasetheirincometosome
•Human-centeredcomputing→Userstudies;•Computing amounttoobtainanapproval)andarebestsuitedtodecisionson
methodologies→Artificialintelligence.
tabulardata[26].Therehasbeenaflurryofactivityinthisarea
resultingindifferentnotionsofcounterfactualexplanation[54].
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor Approachesvarybothincounterfactualtype,suchaspoint-based
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
|     |     |     |     | counterfactuals(e.g.,𝑖𝑛𝑐𝑜𝑚𝑒 |     | =$1,000)[12,42,50,56]andregion- |     |     |
| --- | --- | --- | --- | --------------------------- | --- | ------------------------------- | --- | --- |
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe basedcounterfactuals(e.g,$1,000<𝑖𝑛𝑐𝑜𝑚𝑒 <$1,500)[17,20,60]as
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
wellcounterfactualpresentationwithdifferentstylesforexplaining
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. thesamecontent,rangingfromsimplenumericcapture[58],to
FAccT’24,June03–06,2024,RiodeJaneiro,Brazil textualdescription[53],andvisualdepictions[18].
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM. Unfortunately,whilecounterfactualexplanationisfrequently
ACMISBN979-8-4007-0450-5/24/06
supportedbydrawingparallelstohumannotionsofreasoning[2,
https://doi.org/10.1145/3630106.3658997
1682

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
36],surveysofthefieldhavefoundthatinpracticethedesignof tosignificantlyhigherobjectiveunderstanding,subjectiveunder-
XAItechniquesisdrivenbymachinelearningexpertswithlittle standing,andresponseconfidencethanpoint-basedcounterfac-
groundinginpsychologyandwithoutathoroughinvestigationof tuals.Further,wefindcounterfactualpresentationstyledoesnot
realusers’needs[39,40].Asaresult,comparativeevaluationof significantlyeffectuserunderstandinginthiscontext,butdoes
counterfactualapproachesislargelylimitedtocomputationalmet- significantlyeffectresponsetimeandmoderatestheeffectofcoun-
ricssuchascounterfactualproximityanddistributionalfaithfulness, terfactualtypeonparticipants’responseconfidence.Wealsoshow
withmultiplecompetingmetricsoftenintendingtomeasurethe thatusers’subjectiveunderstandingandresponseconfidenceare
samenotion[19,28].Whileinteresting,thesecomputationalmet- significantpredictorsoftheirobjectiveunderstanding.Basedonour
ricsdonotcapturetheunderstandingandneedsoflayuserswhose results,weproviderecommendations(Sec.7)forXAIpractitioners
knowledgeandprioritieshavebeenshowntodiffersignificantly tofocusonthedevelopmentanddeploymentofpracticalregion-
fromthoseofmachinelearningexperts[22]. basedcounterfactualexplanationtechniques.Wealsoencourage
Existingexplanationuserstudieshavenotyetbridgedthisgap, HCIresearcherstocontinueexplorationofpresentationmethods
witharecentsurveyfindingthatonlyahandfulofstudiesconsider todeterminehowbesttomaximizeunderstanding.
counterfactuals[49].Ofthese,mostcomparecounterfactualsto
otherformsofexplanation(e.g.,featureimportance).Suchworks
havefoundthatcounterfactualexplanationscanincreasemetricsof 2 BACKGROUNDANDRELATEDWORK
understanding[62]andimproveperceptionsoffairness[51,64]and Counterfactualexplanationsareaformofpost-hoclocalexplana-
justice[55]ascomparedtonon-counterfactualmethods.Despite tion:post-hocinthattheyaregeneratedafteramachinelearning
thesepromisingresults,existingstudiesarerestrictedtosingular modelistrained,andlocalinthattheyarespecifictoaparticular
configurationsofcounterfactual,typicallypoint-basedcounterfac- instance[19].Counterfactualexplanationsareanswerstoacoun-
tualspresentedastext(Sec.2.2).Thus,alargeunmetneedremains terfactualquestiontypicallyformulatedas"Why𝑃 ratherthan𝑄"
foruserstudiestoexaminetowhatdegreedecisionsubjectsun- where𝑃 issomefactuallyobservedoutcome,typicallyundesired
derstandandmaybeabletousedifferenttypesofcounterfactual (e.g.,loandenial),and𝑄issomehypotheticalcounterfactualout-
explanationsforactionablerecourseandtodeterminewhatpresen- comedesiredbytheuser(e.g.,loanapproval)[36].Counterfactual
tationstylesaremosteasilyunderstood.Motivatedbythisneed, explanationisthoughttofollowhumannotionsofreasoningwith
weaddressthefollowingthreeresearchquestionsinthiswork: literaturefrompsychologyfindingpeopletypicallyvaluewhyone
• RQ1:Whateffectdocounterfactualexplanationtypeandcoun- eventhappenedratherthananother[2,36].Counterfactualshave
terfactualexplanationpresentationhaveonlaydecisionsub- alsobeenarguedtomeetemergingregulatoryrequirementsfor
jects’understandingofautomateddecision-makingsystems? layuserappropriateexplanationofconsequentialdecisions[61]
• RQ2:Whateffectdocounterfactualexplanationtypeandcoun- thoughthescopeandenforcementofsuchregulationremainsan
terfactualexplanationpresentationhaveonlaydecisionsub- emergingareaoflaw[3].
jects’confidenceintheirunderstandingofautomateddecision-
makingsystems?
2.1 CounterfactualExplanationMethods
• RQ3:Dolaydecisionsubjects’subjectiveunderstandingand
confidencepredicttheirobjectivetaskperformance? Point-BasedCounterfactuals.Counterfactualexplanationhas
largelybeenexploredinthecontextofsinglecounterfactualpoints
Wedevelopsixuniquecounterfactualexplanationconfigurations
oftencalledcounterfactualexamples.Thatis,givenaninstance
varyingacrosstwokeyfactors:counterfactualtype(point-based
𝑥 ∈R𝑛predictedasclass𝑃,point-basedcounterfactualexplanation
vsregion-based)andcounterfactualpresentationstyle(numeric,
methods seek to find some hypothetical point 𝑥′ ∈ R𝑛 which
naturallanguage,andvisual).Weexamineapopulationoflayusers
would be predicted as class𝑄. Numerous methods to generate
actingassimulateddecisionsubjectsforaloanapprovalscenario,
counterfactualpointshavebeenexplored,includingviaalgorithmic
andproposeamethodology(Sec.4)toevaluatetheirunderstanding
search[14,45,50,56],linearprogramming[10,25,42],andgradient
bypresentingaseriesofloandecisionsalongsidecounterfactualex-
access[12,31,38].Thesemethodsguidethegenerationof𝑥′ by
planations.Followingthisprocedure,weperformacrowd-sourced
metricssuchassimilarity,oftentheL1orL2normbetween𝑥 and
2x3between-subjectsuserstudywith𝑁 = 252participants.We
𝑥′;sparsity,thenumberoffeaturesdifferingbetween𝑥and𝑥′;and
measureparticipants’subjectiveunderstandingviaagreementstate-
validity,thereliabilityof𝑥′ obtainingthedesiredoutcome[19].
mentsandobjectiveunderstandingviaaccuracyacrosstwelvetask
Counterfactualvalidityisofparticularimportancetothehuman
questionsinthreerecourse-relatedareas.Wealsorecordpartici-
contextbecausemethodsthatfailtoguaranteevaliditymaywastea
pants’responseconfidenceandresponsetimefortaskquestions,and
user’stimeandeffortiftheymakechangestomeet𝑥′andre-receive
solicituserexperiencesviaopenresponse.
anunwantedoutcome.Thisalsorisksliabilityfortheownerofthe
Usingthisinformation,weperformaquantitativeanalysisfor
decisionsystemunderrelevantregulatoryframeworks[1,41,43].
eightinternallypreregisteredhypotheses(Sec.5.1)followedbyan
Region-BasedCounterfactuals.Recently,methodshaveemerged
exploratorystatisticalanalysis(Sec.5.2)andaqualitativeanalysis
forcreatingcounterfactualexplanationsthatcoveraportionofthe
ofopenresponses(Sec.6).Ouranalysisfindssignificanteffects
valuesinthefeaturespacelargerthanjustasinglepoint.These
ofcounterfactualtype,withregion-basedcounterfactualsleading
region-basedapproachesprovidegreaterflexibilitytousersbyof-
feringadditionalcontextandinformationontherationaleofthe
decisionsystem.Thisalignswithobservationsthatpoint-based
1683

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
counterfactualsmayplaceunrealisticrequirementsonuserstopre- userperceptionsoffairness.Binnsetal.[55]examineperceptions
ciselysetthevalueofeachfeatureinspiteofnormallyexpected ofjusticewithdifferingformsofexplanationpresentedviatextand
featurevariability(e.g.,requiringaloanapplicantobtainavery foundthatcounterfactualsledtohigherperceptionsofjustice,but
specificbankaccountbalance)[27].Thesemethodsutilizesimilar thattheseeffectswereoutweighedbyscenarioeffects.Whilethe
abstractionstocaptureportionsofthefeaturespace,suchasdescrib- aboveworkseachadoptadifferentexplanationpresentationstyle,
ingasetofdisjointrulesacrossoneormorefeatures,e.g.,onerule nonedirectlyexaminethisfactor.
optionrestricts($1000 < 𝑖𝑛𝑐𝑜𝑚𝑒 < $1500)whileanotheroption PresentationStudies.Workswhichdirectlyevaluateexplanation
restricts($500<𝑟𝑒𝑛𝑡 <$900),orviaacontinuoushyperboxe.g., presentationaremorerare.VanBerkeletal.[59]comparedtex-
($1000<𝑖𝑛𝑐𝑜𝑚𝑒 <$1500AND$500<𝑟𝑒𝑛𝑡 <$900)[15,17,20,60]. tualdatasummaryexplanationstovisualdatascatterplotsforloan
Theseregion-basedmethodsdifferintwokeyways:1)whetherall applicationsandrecidivismprediction,andfoundthetextcases
pointsthatfallintotheregionareguaranteedtobevalidlycounter- yieldedhigherperceivedfairness.Szymanskietal.[55]compared
factual,and2)thecomputationalcomplexityrequiredforcreating textual,visual,andhybridpresentationsofmultipleformsofexpla-
theregionexplanation.Specifically,LORE[20]andLEWIS[17] nationforarticlereadingtimeestimation.Theyfoundthathybrid
failthevalidityguarantee,andRFOCSE’s[15]coreapproachhas formsofexplanationledtothehighestobjectiveunderstanding.
beenshowntobeintractableforreasonablysizedensembles[60]. Noworkstodatehaveadequatelystudiedtheeffectofpresentation
ThisledRFOCSEtoadoptafasterheuristic-variantwhichlacksa forcounterfactualexplanations.
validityguarantee.InSec.4weusetherecentworkFACET[60]
togeneratecounterfactualsasitprovidesastrongguaranteeof 3 RESEARCHHYPOTHESES
counterfactualvalidityinefficienttime.
Toexploreourprimaryresearchquestions(Sec.1),weposethe
followinghypotheses.
2.2 ExplanationUserStudies
3.1 HypothesesforRQ1:UserUnderstanding
Non-CounterfactualStudies.Existinguserstudiesonexplana-
tionlargelyfocusonfeatureimportancetechniques[49]suchas
Wangetal.[62]showthatpoint-basedcounterfactualscanimprove
user understanding of an automated decision system and Bove
thosegeneratedbyLIME[34]andSHAP[48].Chengetal.[6]ex-
aminedlocalfeatureimportanceexplanationspresentedasstacked
etal.[4]findthattheinformationfrommultiplecounterfactual
pointscanimprovebothobjectiveandsubjectiveunderstanding
barscomparedtoalackofexplanationforuserunderstandingin
compared to a single point. Because region-based explanations
acollegeadmissionsscenario.Theyfoundthepresenceofexpla-
containasuper-setoftheinformationprovidedbypoint-based
nationsledtohigherobjectiveunderstandingmeasuredbythree
counterfactuals,andindeedenclosemanycounterfactualpoints,
modelsimulationtasks,butnothighersubjectiveunderstanding
weexpectthatregion-basedcounterfactualswouldthusincrease
measuredviapost-taskquestionnaire.Poursabzi-Sangdehetal.[44]
examinedglobalfeatureimportanceexplanationsandfoundtheir
bothobjectiveunderstanding(𝑯1𝒂 )andsubjectiveunderstanding
presenceleduserstomoreaccuratelypredictthemodel’sbehavior,
(𝑯1𝒄 )comparedtopoint-basedcounterfactuals.Further,Szyman-
butmadethemworseatdetectingitsmistakes.
skietal.[55]findsomeevidencethatexplanationpresentation
mayimpactobjectiveunderstanding.Therefore,weanticipatethat
Point-BasedStudies.Someworkscomparetheeffectsofunder-
presentationmaymoderatetheeffectofcounterfactualtypeon
standingfromcounterfactuals,butconsideronlypoint-basedcoun-
terfactual types. For example, Wang et al. [62] found that both
objectiveunderstanding(𝑯
1𝒃
).Finally,vanBerkeletal.[59]find
thatsubjectiveperceptionsoffairnessdifferbetweenexplanation
featureimportanceandpoint-basedcounterfactualexplanations
presentations.Therefore,wepredictthatsubjectiveunderstanding
presentedasstructuredtextimproveobjectiveunderstandingwith
oftheautomateddecision-makingsystemmayalsodifferbetween
similareffectsizeforrecidivismprediction,butobservedonlyan
increaseinsubjectiveunderstandingforcounterfactualsinaforest
presentationstyles(𝑯
1𝒅
).
coverscenario.Boveetal.[4]usealoanapplicationscenarioand • Hypothesis1a(𝑯1𝒂):Region-basedcounterfactualexplanations
improve objective user understanding as compared to point-
foundthatmultiplecounterfactualpointsshownviaacard-style
basedcounterfactualexplanations.
UIimprovedobjectiveandsubjectiveunderstandingcomparedto
singlecounterfactualpoints.Thissuggeststhatadditionalcounter- • Hypothesis1b(𝑯 1𝒃 ):Theeffectofexplanationtypeonobjective
understandingismoderatedbyexplanationpresentation.
factualinformationmayimproveunderstanding.Warrenetal.[63]
comparetextualcounterfactualpointsusingcategoricalandcontin- • Hypothesis1c(𝑯1𝒄):Region-basedcounterfactualexplanations
improvesubjectiveunderstandingascomparedtopoint-based
uousfeaturesforautomateddrunkdrivingassessmentandfound
counterfactualexplanations.
objectiveunderstandingtobehigherwithcategoricalfeatures.
Studieshavealsoevaluatedtheeffectofpoint-basedcounterfac- • Hypothesis1d(𝑯 1𝒅 ):Users’subjectiveunderstandingdiffers
basedonexplanationpresentation.
tualswithothermetrics.Kuhletal.[29]comparedclosestcounter-
factualpointstoplausiblecounterfactualpointsusinganumeric
presentationandfoundclosestcounterfactualsleadtofasterlearn- 3.2 HypothesesforRQ2:UserConfidence
ingofanabstractgame[30].Schoefferetal.[51]andYurritaet Whenaninstance(e.g.,aloanapplication)doesnotexactlymatcha
al.[64]examinedtheeffectofcombinedcounterfactualandfeature point-basedcounterfactual,littledefinitiveinformationisavailable
importanceexplanationspresentedastexttootherformsofexpla- totheuseraboutwhattheoutcomeofthatinstancewouldbe.This
nation.Theyfoundthecombinedexplanationsledtothehighest maycauseuserstobeuncertainorotherwisefeelthattheyare
1684

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
guessing.Incontrast,region-basedcounterfactualsprovidegreater A C
informationonthedecision-makingsystemwhichmaybeusedto
assessthelikelihoodofalternateoutcomes,e.g.,bysimplydeter-
miningiftheinstancefallswithintheregion(Sec.2.1).Therefore,
wehypothesizethatregion-basedcounterfactualsmayleadusers
B
tohavegreaterconfidence(i.e.,belief/certaintyintheirunderstand-
ing)thanpoint-basedcounterfactuals(𝑯2𝒂 ).Additionally,ifusers
perceiveoneexplanationpresentationtobemorecomplexordiffi-
culttoparsethananother,theymaybelessconfidentusingthat
presentation(𝑯 ).Wecanmeasurethisconfidencebyproviding
usersaspectrum 2𝒃 ofresponsesandrecordinghowoftentheychoose Figure1: Samplecounterfactualexplanationuserinterface
themoreextremeresponses. andparticipantrecruitmentstrategyinSec.4.4.Thedesignofthe
explanationuserinterfacesandtheexactwordingofevaluation
• Hypothesis 2a (𝑯2𝒂): Users are more confident in their re-
questionswasrefinedthroughaseriesofinternalusergroupsand
sponseswithregion-basedcounterfactualexplanationsthanwith
asmallcrowd-sourcedpilotstudyoftwentyparticipants.
point-basedcounterfactualexplanations.
• Hypothesis2b(𝑯 ):Theeffectofexplanationtypeonusers’
2𝒃
responseconfidenceismoderatedbyexplanationpresentation. 4.1 ExperimentScenario
Followingpriorresearch[4],weadoptaloanapplicationscenario
3.3 HypothesesforRQ3:Calibrated forourexperimentduetotheconsequentialnatureofsuchdeci-
Understanding sions,familiarityoflayuserswiththetask,andlegalrequirements
Foruserstoeffectivelyusecounterfactualexplanationsforaction- forexplanationsofautomateddecisionsinthisdomain[1,41,43].
ablerecourse,theymustbeabletoaccuratelyassesstheirlevelof Togeneratecounterfactualexplanationsfortheexperiment,we
understandingoftheunderlyingdecision-makingsystem.Thisis trainedamachinelearning(randomforest)classifieronarandom
criticalasuserswhoare"confidentlywrong"mayexpendsignif- 80%sampleofaKaggleloansdataset[24].Thismodelactsasan
icanteffortenactingasetofchangeswhichwillnotresultinthe automateddecisionsystemwhichpredicts𝐿𝑜𝑎𝑛𝐴𝑝𝑝𝑟𝑜𝑣𝑎𝑙 (binary
desiredcounterfactualoutcome.Thus,users’subjectiveunderstand- REJECT/APPROVE)from𝐴𝑝𝑝𝑙𝑖𝑐𝑎𝑛𝑡𝐼𝑛𝑐𝑜𝑚𝑒,𝐶𝑜𝑎𝑝𝑝𝑙𝑖𝑐𝑎𝑛𝑡𝐼𝑛𝑐𝑜𝑚𝑒,
ingandconfidenceareideallycalibratedwiththeirtrueobjective 𝐿𝑜𝑎𝑛𝐴𝑚𝑜𝑢𝑛𝑡,and𝐿𝑜𝑎𝑛𝑇𝑒𝑟𝑚.Wethenusedthemodeltoclassify
understanding.WhileChengetal.[6]andPoursabzi-Sangdehet theremaining20%ofapplicationsandexplainedthosewhichwere
al.[44]observesomedivergenceinobjectiveandsubjectiveunder- Rejected(119)withthestate-of-the-arttechniqueFACET[60].This
standingsforfeatureimportanceexplanations,evaluationsbyBove producedaregion-basedandpoint-basedcounterfactualexplana-
etal.[4]andWarrenetal.[63]ofdifferentusesofcounterfactuals tionforeachapplicationdecision.Toavoidbiasingparticipants
showedincreasesinboth.Thismayindicatethatwhenworking towardscertainfeature-values,weexaminedeachexplanationand
withcounterfactualsusershaveafairlyaccurateself-assessment selected12distinctinstancesforthestudythatwerediversein
oftheirunderstanding.Therefore,weexpectthatsubjectiveun- termsofthealteredfeaturesandcounterfactualvalues.Eachin-
derstanding(𝑯3𝒂 )andresponseconfidence(𝑯
3𝒃
)arepositively stancewasusedexactlyonce.
associatedwithobjectiveunderstandingforbothtypesofcounter-
factualexplanation. 4.2 ExplanationInterfacePrototypes
• Hypothesis3a(𝑯3𝒂):Users’subjectiveunderstandingisposi- Foreachofthesixcounterfactualexplanationconfigurations,we
tivelyassociatedwithobjectiveunderstanding developanexplanationuserinterfacetodisplaytheloandecision
• Hypothesis3b(𝑯 ):Users’responseconfidenceispositively andassociatedexplanationtotheuser.Theseinterfacessharea
3𝒃
associatedwithobjectiveunderstanding commontemplatedlayoutandsidebarasdepictedinFig.1.Area𝐴
remindstheuseroftheloanscenarioandrejectiondecision,Area
4 METHODOLOGY 𝐵 displaysthefeature-valuesofthegivenloanapplication,and
Totestourhypothesesabouttheeffectsofcounterfactualexplana- Area𝐶containsthecounterfactualexplanationofthedecisionfor
tiontypeandpresentationonlayuserunderstandingofautomated thatapplication.EachofthesixconfigurationsshowninFig.2
decisionsystems(Sec.3),weconductedarandomizedhumansub- combineonecounterfactualtypeandpresentationandareplugged
jectsexperiment(𝑁 =252)onProlific[46]usingexplanationsfor intoArea𝐶.Eachparticipantisrandomlyassignedtoasingleexpla-
mockloanapprovaldecisions(Sec.4.1).Sixconfigurationsofcoun- nationconfigurationtocreatesixexperimentalgroups.Wedevelop
terfactualexplanationwereconsideredvaryingincounterfactual configurationsforeachfactorasfollows.
type(regionvspoint)andcounterfactualpresentation(numericvs ExplanationType.Weexploretwotypesofcounterfactualexpla-
naturallanguagevsvisual)foracomplete2x3between-subjects nation:point-basedandregion-basedcounterfactuals.
design.Communicationofloandecisionsandexplanationswas • Point-BasedCounterfactuals.Foragiveninstance,apoint-
operationalizedthroughanexplanationuserinterface(Fig.1)cus- basedcounterfactualexplanationisasetoffeature-values,one
tomizedforeachconfiguration(Sec.4.2).Userunderstandingwas perfeature,suchthatiftheinstanceistransformedtoexactly
assessedthroughbothquantitativemeasures(Sec.4.3)andthematic matchthosevalues,theautomateddecision-makingsystemwill
analysisofopenresponse(Sec.6).Wedetailoursurveyprocedure producethedesiredcounterfactualoutcome.
1685

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
Numeric
desaB-tnioP
desaB-noigeR
Natural Language Visual
Figure2: Explanationsforoneinstanceusingthesixstudiedcounterfactualexplanationconfigurations
• Region-BasedCounterfactuals.Foragiveninstance,aregion- visualpresentationwhichusesnumberlineplots(Fig.2Right).
basedcounterfactualexplanationisacontinuousboundedrange Here,eachfeatureisgivenitsownnumberlinedisplayingboth
alongeachfeaturesuchthatanypointthatfallswithinthepre- thefactualandcounterfactualvaluesforthatfeature.Point-based
scribedrangeforeveryfeatureisguaranteedtoobtainthedesired counterfactualsaredepictedusingpoints,whileregion-based
outcomefromtheautomateddecision-makingsystem. counterfactualsarerepresentedbyshadedbarsalongtheline.
ExplanationPresentation.Weexplorethreecounterfactualex-
planationpresentations:numeric,naturallanguage,andvisualas
theyrepresentthreedistinctcommunicationmodalitiesprevalent 4.3 EvaluationMetrics
inexistingworks(Sec.2).Foreachcounterfactualtype,allthree
stylescontainthesamecounterfactualinformationandweadopta
ObjectiveUnderstanding(𝑯1𝒂,𝑯
1𝒃
,𝑯3𝒂,𝑯
3𝒃
).Duetothecom-
plexnatureofhumanprocessing,manymetricsmeasuringuser
setofsimpleandconsistentdesignprinciplestomitigateconfound-
understandingexist.FollowingpreviousHCIstudiesofexplana-
ingeffects.Toaidreadability,featureswithproposedalterations
tions[4,6,7,44,55,62,63],weadoptthedefinitionthatauser
havetheircurrentfactualvaluesdisplayedinredandthenewly
"understands"adecisionsystemiftheycanidentifywhatattributes
proposedcounterfactualvaluesshowninblue.Featuresrequiring
causethesystem’sactionsandcanpredicthowchangesinthesitu-
noalterationareshowningrey.Allpresentationsprovidefeature
ationcanleadtoalternativeoutcomes.Followingthisphilosophy,
informationinalphabeticalorderbyfeaturename.
weadaptedtheevaluationquestionsfrom[4,7]totargetactionable
• Numeric. Following existing research [29], we organize the recourse.Specifically,wedesignedthreetypesoftaskquestionsto
feature-values into a tabular arrangement (Fig. 2 Left) for a assessparticipants’objectiveunderstandingofthedecisionsystem
structuredrepresentationanddisplayaside-by-sidecompari- inthreecriticalrecourse-relatedareas:FeatureAlteration,Instance
son between the observed factual values and the counterfac- Prediction,andFeatureSensitivity.
tual values proposed by the explanation. In the point-based
• QuestionType1:FeatureAlteration.Ascounterfactualexpla-
case,thisissimplyasinglevalue,e.g.,𝐴𝑝𝑝𝑙𝑖𝑐𝑎𝑛𝑡𝐼𝑛𝑐𝑜𝑚𝑒 :$854,
nationsprovideunderstandingofthedecisionsystemthrough
whileintheregion-basedcase,thisispresentedasarange,e.g.,
proposedfeaturealterations,itiscriticalforactionablerecourse
𝐴𝑝𝑝𝑙𝑖𝑐𝑎𝑛𝑡𝐼𝑛𝑐𝑜𝑚𝑒 :$412−$1,013.
thatuserscanaccuratelyidentifythealterationsprescribedby
• NaturalLanguage.Existingworksoftenpresentcounterfac- theexplanation.Correctlyinterpretingthisinformationallows
tualsviatext[53,55,64].Toexaminethiscase,wedevelopa
ausertodeterminethesignificantfeaturesandthresholdval-
templatednaturallanguagepresentation(Fig.2Center).Each
ues in the local space of the explained instance. To measure
statementbeginswithadescriptionofthedecisionoutcomeand
thisability,wepresentedparticipantswithanexplanationfora
thenliststhealteredfeaturesindicatingtheprescribedcounter-
not-before-seeninstanceandaskedthemviaamultiple-choice
factualvaluescontrastedtothefactualvalueswitharatherthan
questiontoidentifywhichchangeismostlikelytogetthisappli-
clause.Thecounterfactualvaluesforregionsareprovidedusing
cationapproved?fromamongthreepotentialchoices(Appx.C.1).
thewordbetweentoencodetherange.Finally,aparenthetical
Toaccountforpreexistingassumptionsofmodelbehavior(e.g.,
listingindicatesthenon-alteredfeaturesandtheirvalues.
participantsassumingthatahigherincomeisalwaysmorelikely
• Visual.Alimitedsetofworksprovideexplanationcontentvia tobeapproved),weselectedamixofexplanationswithintuitive
visualization[55,59].Toinvestigatethis,wedevelopasimple
andcounterintuitivealterations.Participantswerealsodirected
1686

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
tonotrelyontheirpreexistingassumptionsandincentivizedvia ResponseTime.Toapproximatethedifficultyofprocessingdiffer-
bonuspaymentstoanswercorrectly. entexplanationconfigurations,wemeasuredhowmuchtimeeach
• QuestionType2:InstancePrediction.Anothercomponentof participantspentansweringeachobjectiveunderstandingquestion
actionablerecourseisassessingwhetherornotaninstancewill andcomputedthetotalresponsetime.
achievethedesireddecisionoutcome.Thisiscriticalasitre- SatisfactionandTrust.Weaskedparticipantstoratetheirsat-
flectsauser’sunderstandingoftheunderlyingdecisionsystem’s isfactionwiththeprovidedexplanationsona5-pointLikert-style
behaviorandenablesthemtodeterminewhetherornotthey scalefromnotsatisfiedtohighlysatisfiedandindicatetheiragree-
havesufficientlyalteredtheirinstancetomatchtheprovided mentwiththestatementItrustthedecisionsmadebythealgorithm
counterfactualexplanation.Wemeasuredthisabilitydirectlyby ona6-pointforcedchoicescalefromstronglydisagreetostrongly
presentingparticipantswithanexplanationforarejectedin- agree(Appx.C.3).
stancealongsideanewinstanceofunknownoutcome.Wethen
askedtheparticipantstopredictthesystem’sdecisionforthe 4.4 SurveyProcedureandRecruitment
newinstanceona4-pointforced-choicescalefromverylikelyto
Theexperimentconsistedofanonlinesurveyadministeredvia
berejectedtoverylikelytobeaccepted.
Qualtrics[47]withthefollowingfivemajorsteps.
• QuestionType3:FeatureSensitivity.Onceausercanidentify
thealterationsacounterfactualexplanationsuggestsanddeter-
1) Presurvey.Aftercollectingconsent,weaskedparticipants
questionsrelatingtotheirdemographicsandindividualfac-
mineiftheirinstancewillachievethedesiredoutcome,theymust
tors.Onequestionwasmanipulatedtoactasanattention
"freeze"theirinstance(i.e.,preventsignificantdeviationfrom
check.Wethenrandomlyassignedeachparticipanttoone
theiralteredfeature-values)untilthedecisionsystemprocesses
ofthesixcounterfactualexplanationconfigurationsshown
thenewinstance.Forexample,aloanapplicantmayabstainfrom
inFig.2.
largetransactionsto"freeze"theirsavingsbalancewhilethey
reapplyfortheloan.Toachievethis,theusermustunderstand
2) Introduction.Wegaveparticipantsadescriptionoftheloan
applicationscenarioandfamiliarizedthemwiththefeatures
whatfeaturesaresensitive.Thatis,theymustbeabletoidentify
used.Wealsoaskedasetofsimplerecallquestionstoensure
featuresoftheirinstancethatwouldresultinanundesiredout-
theyreadthematerials(Appx.C.5).
comeifallowedtodeviatebyasmallamount.Thisisequivalent
toidentifyingwhichfeature(s)oftheirinstanceareclosesttoa
3) Training.Wepresentedparticipantswithanexampleex-
planation(e.g.,Fig.1)fortheconfigurationcorresponding
decisionboundary.Tomeasurethisunderstanding,wepresented
totheirgroup.Wethenusedashortseriesofdescriptions
participantswithanexplanationforarejectedinstancealongside
and questions to train the participants to locate the fac-
anewinstancewhichwetoldthemwasaccepted.Weaskedthem
tualinstance’svalues,identifyalteredfeatures,andunder-
tochooseWhichattributeofyournewapplication,ifchangedby
standthecriteriaforacceptanceprovidedbytheexplanation
asmallamount,ismostlikelytoresultinarejection?
(Appx.C.6).
Wecreated12objectiveunderstandingquestions,4ofeachtype.
Responseoptionsweregeneratedbyalteringtheinstancetomeet
4) TaskEvaluation.Tomeasureobjectiveunderstandingand
responseconfidenceweaskedtheparticipantstoanswer
theexplanation,thenadjustingoneormorefeature-valuesineach
thetwelvetaskquestionsfromourthreerecourse-related
optionasdescribedinAppx.C.1.Responseswerescoredcompared
questionareas(Appx.C.1)
togroundtruths,assigningonepointtoeachcorrectanswerto
createanobjectiveunderstandingscoreranging0-12.
5) PostSurvey.Weconcludedthesurveybyhavingpartici-
pantscompletetheLikert-styleagreementquestionsforsub-
SubjectiveUnderstanding(𝑯1𝒄,𝑯
1𝒅
,𝑯3𝒂).Inadditiontomea-
jectiveunderstanding,satisfaction,andtrust,withoneques-
suringauser’strueunderstandingofthemodel,wealsomeasure
tionmanipulatedtoactasanattentioncheck(Appx.C.2).
theirself-reportedunderstanding.Thisisimportanttodetermineif
someformsofexplanationsleadtoafalsesenseofunderstanding Basedonapoweranalysisofthetests(Sec.5.1)forourmainhy-
whichcouldcauseuserstoexpendeffortinfruitlessattemptsto potheses,weaimedtocollectdatafromatleast247participants.
achievetheirdesiredoutcome.Tomeasuresubjectiveunderstand- Wethusrecruited264participantsfromProlific[46]inSeptember
ing,weadaptedthequestionsfrom[4]andaskedparticipantsto 2023.Allparticipantswereadults(≥18yearsold),first-language
indicatetheiragreementwithfivestatements(Appx.C.2)on6-point Englishspeakers,locatedintheUnitedStates.Recruitmentwaslim-
bipolarforcedchoiceLikert-styleagreementscales.Weconverted itedtoProlificmemberswhohadcompleted100+taskswitha95%
eachresponsetoavalue0-5andsummedthe5questionstocreate orhigherapprovalrate.Prolific’s"gender-balanced"recruitment
asubjectiveunderstandingscorerangingfrom0-25. featurewasapplied.Eachparticipantwaspaida$4baseamount
ResponseConfidence(𝑯2𝒂,𝑯
2𝒃
,𝑯
3𝒃
).FortheInstancePredic- anduptoanadditional$2basedontheiraccuracyinanswering
tionquestions(ObjectiveQuestionType2),weaskedthepartici- questions.Participantswereinformedofthebonuspotentialwith
pantstopredicttheoutcomeforaninstanceona4-pointscalefrom theamountscalingin$0.50incrementstoincentivizeparticipants
verylikelytoberejectedtoverylikelytobeaccepted.Tomeasure tomakelegitimateresponses.Participantswerenottoldwhich/how
how confident users were in their responses, we computed the manyquestionstheygotcorrecttoavoidbiasingtheirresponses.
numberoftimeseachparticipantchoseaverylikelyoptionovera Theaveragecompletiontimewas20.32minutesandaveragewas
somewhatlikelyoption.Thisyieldsascorerangingfrom0-4aswe compensation$5.07foranaveragewageof$14.98/hr.Foranalysis,
askedfoursuchquestions. weexcludedtenparticipantswhofailedatleastoneofthetwo
attentionchecksandtwoparticipantswhofailedmorethantwo
1687

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
|     | HypothesesforMainEffects(𝑝<6.25×10−3significant) |                                             |     |     |                  | 2      |     |
| --- | ------------------------------------------------ | ------------------------------------------- | --- | --- | ---------------- | ------ | --- |
|     |                                                  |                                             |     |     | 𝐹 ↑ 𝑝-value↓     | 𝜂 𝑝 ↑  |     |
|     | 𝑯1𝒂                                              | Regionsincreaseobjectiveunderstanding       |     |     | 217.34 <2×10−16  | 0.4694 |     |
|     | 𝑯1𝒃                                              | Presentationmoderatesobjectiveunderstanding |     |     | 4.04 3.13×10−2   | 0.0278 |     |
|     | 𝑯1𝒄                                              | Regionsincreasesubjectiveunderstanding      |     |     | 60.91 1.71×10−13 | 0.1984 |     |
|     |                                                  | Presentationeffectssubjectiveunderstanding  |     |     | 2.10 1.25×10−1   | 0.0168 |     |
𝑯1𝒅
|     |     | Regionsincreaseresponseconfidence |     |     | 42.41 4.14×10−10 | 0.1474 |     |
| --- | --- | --------------------------------- | --- | --- | ---------------- | ------ | --- |
𝑯2𝒂
|     |     | Presentationmoderatesresponseconfidence |     |     | 6.18 2.41×10−3 | 0.0478 |     |
| --- | --- | --------------------------------------- | --- | --- | -------------- | ------ | --- |
𝑯2𝒃
|     |     | Subjectiveunderstandingpredictsobjectiveunderstanding |     |     | - 1.39×10−10 | -   |     |
| --- | --- | ----------------------------------------------------- | --- | --- | ------------ | --- | --- |
𝑯3𝒂
1.30×10−4
|     | 𝑯3𝒃 | Responseconfidencepredictsobjectiveunderstanding |     |     | -   | -   |     |
| --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
AdditionalRelatedObservations
|     | 𝑶1  | Presentationeffectsobjectiveunderstanding    |     |     | 0.29 0.7458 | 0.0024 |     |
| --- | --- | -------------------------------------------- | --- | --- | ----------- | ------ | --- |
|     | 𝑶2  | Presentationmoderatessubjectiveunderstanding |     |     | 3.53 0.0309 | 0.0279 |     |
|     | 𝑶3  | Presentationeffectsresponseconfidence        |     |     | 0.17 0.8479 | 0.0014 |     |
Table1:Resultsofstatisticaltestsformainhypothesesandrelatedobservations
ofthesimplerecallquestionsfromProcedureSteps2-3.Thisleft evidencesuggestingasmallmoderatingeffectofexplanationpre-
𝑁 =252participantswhosedemographicsareshowninAppx.B.2. sentationonexplanationtypeforsubjectiveunderstanding,(𝑶2 ),
butwedidnotregisterahypothesisforthiscase.
RQ2:ResponseConfidence.Athirdmulti-wayANOVAusesex-
5 QUANTITATIVEANALYSISANDRESULTS
planationtypeandpresentationasfactorspredictingresponseconfi-
5.1 HypothesisTests dence(Sec.4.3).Here,wefindalargesignificanteffectofexplanation
|     |     |     |     | typeonresponseconfidence(𝑯2𝒂 |     | )favoringregion-basedexplana- |     |
| --- | --- | --- | --- | ---------------------------- | --- | ----------------------------- | --- |
Here,weperformstatisticalteststoevaluateour8mainhypotheses
(Sec.3).Toconservativelycontrolthefamily-wiseerrorrateto tions(𝜇=2.17±0.08)overpoint-basedexplanations(𝜇=1.31±0.11,
below0.05,weapplyBonferronicorrectionyielding𝛼 =0.05/8= scoreranges0-4).Wealsofindasmallsignificantmoderatingeffect
0.00625.Thus,p-valuesfromthemainanalysisbelowareonlycon- ofexplanationpresentationontheeffectofexplanationtypefor
sideredsignificantif𝑝 <6.25×10−3.Forhypothesesanalyzedwith responseconfidence(𝑯 ).Wedidnotobserveevidenceindicating
2𝒃
|                                           |     |     | 2)effectsizein | aneffectofexplanationpresentationalone(𝑶3 |     |     | ).  |
| ----------------------------------------- | --- | --- | -------------- | ----------------------------------------- | --- | --- | --- |
| ANOVAtests,wereportthepartialetasquared(𝜂 |     |     | 𝑝              |                                           |     |     |     |
additionto𝑝-valueand𝐹 statisticanduseCohen’s[9]rulesfor RQ3:CalibratedUnderstanding.Weperformedamultiplelinear
interpretation.ThesignificanceofalltestsisshowninTab.1and regressionanalysistotesttheassociationofparticipants’response
themainmetricscoresforeachofthesixcounterfactualexplana- confidenceandsubjectiveunderstandingwiththeirobjectiveun-
tionconfigurationsareshowninFig.3.WealsoperformBayesian derstanding(𝑅2 = 0.24,𝑝 = 4.82×10−16,𝐹 = 40.77).Ourresults
|                                                     |     |     |     | showthatbothsubjectiveunderstanding(𝑯3𝒂 |     |                                  | ,𝛽 0.1929)and |
| --------------------------------------------------- | --- | --- | --- | --------------------------------------- | --- | -------------------------------- | ------------- |
| ANOVAforsometestsandreportBayesFactorsforthesecases |     |     |     |                                         |     |                                  | =             |
|                                                     |     |     |     | responseconfidence(𝑯                    | ;𝛽  | =0.5400)arebothsignificantlypos- |               |
usingLeeandWagenmaker’s[33]rules.
3𝒃
RQ1:ObjectiveUnderstanding.Ourfirstconfirmatoryanalysis itivelyassociatedwithobjectiveunderstanding–withresponse
isamulti-wayANOVAtestwithcounterfactualexplanationtype confidencebeingthestrongerpredictor.
(region-basedvspoint-based)andpresentation(numericvsnatu- SummaryofHypothesisFindings.Wefoundsufficientevidence
|     |     |     |     | to reject | the null hypothesis | for 6 of our 8 tests. | This includes |
| --- | --- | --- | --- | --------- | ------------------- | --------------------- | ------------- |
rallanguagevsvisual)asfactorspredictingparticipants’objective
largeeffectsofexplanationtypeonobjectiveunderstanding,sub-
| understanding | (Sec. 4.3). | Here we find a large | effect of explana- |     |     |     |     |
| ------------- | ----------- | -------------------- | ------------------ | --- | --- | --- | --- |
tiontype(𝑯1𝒂 )withsignificantlyhigherunderstandingforregion- jectiveunderstanding,andresponseconfidence(𝑯1𝒂,𝑯1𝒄,𝑯2𝒂 );
basedexplanations(𝜇=9.24±0.22)thanpoint-basedexplanations amoderatingeffectofexplanationpresentationontheeffectof
(𝜇=5.46±0.14,scoreranges0-12).Wefindsomeevidencesugges- explanationtypeforresponseconfidence(𝑯 );andthatsubjective
2𝒃
understandingandresponseconfidencearebothsignificantpredic-
tiveofasmallmoderatingeffectofexplanationpresentationonthe
|                                                       |     |     |     | torsofobjectiveunderstanding(𝑯3𝒂,𝑯 |     | ).Finally,wefoundsome |     |
| ----------------------------------------------------- | --- | --- | --- | ---------------------------------- | --- | --------------------- | --- |
| effectofexplanationtype(𝑯1𝒃),butaBayesianANOVAreveals |     |     |     |                                    |     | 3𝒃                    |     |
anecdotalevidenceinfavorofnomoderatingeffect(𝐵𝐹01=2.16). evidencethatexplanationpresentationmaymoderatetheeffectof
Thus,wecannotrejectthenullhypothesisforthiscase.Wealsodid explanationtypeonsubjectiveunderstanding(𝑯 ),butcouldnot
1𝒃
notobserveaneffectofexplanationpresentationaloneonobjec- rejectthenullinthiscase.Wefoundnoevidencethatpresentation
|                      |                                     |     |     | aloneeffectssubjectiveunderstanding(𝑯 |     | ).  |     |
| -------------------- | ----------------------------------- | --- | --- | ------------------------------------- | --- | --- | --- |
| tiveunderstanding(𝑶1 | ),withaBayesianANOVArevealingstrong |     |     |                                       |     | 1𝒅  |     |
evidenceforthenullhypothesisthatithasnoeffect(𝐵𝐹01=22.05).
RQ1:SubjectiveUnderstanding.Asecondmulti-wayANOVA 5.2 ExploratoryAnalysis
usesexplanationtypeandpresentationasfactorspredictingsubjec- Here,weprovideadditionalfindingsrelatedtoourhypothesistests
tiveunderstanding(Sec.4.3).Weagainfindalargeeffectofexplana- (Sec.5.1)andexaminesecondaryfactorsthatmayeffectunderstand-
tiontypewithasignificantlyhighermeanscoreforregion-based ing of counterfactual explanations. We also consider additional
explanations (𝜇 = 18.33±0.42) than point-based explanations metricsforexplanationutility,asshowninFig.4.
(𝜇=13.49±0.47,scoreranges0-25).Similarlytoobjectiveunder- ExpansiononModerationEffects.Forhypothesis𝐻 ,wefound
2𝑏
standing,wedidnotfindevidenceforaneffectofexplanationpre- asmallsignificantmoderatingeffectofexplanationpresentation
sentationonsubjectiveunderstanding(𝑯 ).ABayesianANOVA ontheeffectoftypeforresponseconfidence(Sec.5.1).Toexamine
1𝒅
revealsmoderateevidenceinfavorofthenullhypothesisthatpre- thisfurther,weperformedafollow-upTukeytest.Thisrevealsthat
sentationdoesnothaveaneffect(𝐵𝐹01=5.28).Wealsoobserved region-basedcounterfactualshavesignificantlyhigherresponse
1688

| FAccT’24,June03–06,2024,RiodeJaneiro,Brazil |     |     |     |     |     |     |     | VanNostrandetal. |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Objective Understanding Subjective Understanding Response Confidence
|     | 10  |     |     |     |     |     | 2.5 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
18
| CF Type | 9   |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.0
| Region | 8   |     |     |     | 16  |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Based
|     | 7   |     |     |     | 14  |     | 1.5 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Point
Based
|     | 6   |     |     |     | 12  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 5   |     |     |     |     |     | 1.0 |     |     |
Numeric Nat. Language Visual Numeric Nat. Language Visual Numeric Nat. Language Visual
Figure3: Meanandstandarderrorofmainmetricsforthesixconfigurationsofcounterfactualexplanationtypeandpresentation
|     |     | Response Time (minutes) |     |     |     | Satisfaction |     | Trust |     |
| --- | --- | ----------------------- | --- | --- | --- | ------------ | --- | ----- | --- |
10
3.0
|     | 9   |     |     |     | 2.5 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CF Type
| Region | 8   |     |     |     |     |     | 2.5 |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Based  |     |     |     |     | 2.0 |     |     |     |     |
| Point  | 7   |     |     |     |     |     |     |     |     |
2.0
| Based |     |     |     |     | 1.5 |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
6
1.5
Numeric Nat. Language Visual Numeric Nat. Language Visual Numeric Nat. Language Visual
Figure4: Meanandstandarderrorofadditionalmetricsforthesixconfigurationsofcounterfactualexplanation
confidencethanpoint-basedcounterfactualsforthenaturallan-
6 QUALITATIVEANALYSIS
|     | <2×10−7)andnumeric(𝑝 |     | =2.07×10−4)presentations, |     |     |     |     |     |     |
| --- | -------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
guage(𝑝 Here,weanalyzeparticipantresponsestoaseriesofopenresponse
butnotforthevisualcase (𝑝 = 0.92).ThiscanbeseeninFig.3. questionsusingreflexivethematicanalysisunderaconstruction-
| Similarly, | in𝑂2 we | found | that explanation | style may | moderate |     |     |     |     |
| ---------- | ------- | ----- | ---------------- | --------- | -------- | --- | --- | --- | --- |
istframework[5,8].Thisallowsustoidentifylatentthemesin
theeffectsoftypeforsubjectiveunderstanding.ATukeytestfor
thedatathatprovideinsightintohowusersmayconceptualize
thismetricfindsasignificantdifferencebetweensubjectiveun-
explanationsandhowthoseconceptseffecttheirutilization.We
derstandingsfromvisualandnaturallanguagepresentationsin askedfouropenresponsequestions(Appx.A),oneabouttheclarity
point-basedcounterfactuals(𝑝 =0.0475),butnotinregion-based ofexplanation,andthreeabouthowparticipantscompletedthe
| counterfactuals(𝑝 |     | =0.99). |     |     |     |     |     |     |     |
| ----------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
taskevaluation.Theresponsestotal1,008textpassagesandwe
TaskUnderstanding.Todigintousers’understandingofindi-
analyzedresponsestothe"how"and"clarity"questionsseparately.
vidualtasks,wedisaggregatedtheobjectiveunderstandingscore
ResponseswerecodedusingQualCoder[11]overseveraliterative
(Sec.4.3)intothethreetaskareas:featurealteration,instancepre- stepstorefineinitialcodingsintotheidentifiedsubthemes.All
diction,andfeaturesensitivity.Wethenrepeatedthemulti-way quoteddataextractsQ.iareavailableinAppx.A,Tab.2.
ANOVAtestfromSec.5.1foreach.Wefindthatexplanationtype
| remainssignificantforallthreetasks(alteration𝑝 |     |     |     | <2×10−16,𝜂 | 2 = |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
𝑝
|                  |     | 1×10−15,𝜂 | 2         |             |        | 6.1 Region-BasedCounterfactualsEncourage |     |     |     |
| ---------------- | --- | --------- | --------- | ----------- | ------ | ---------------------------------------- | --- | --- | --- |
| 0.33; prediction | 𝑝   | =         | 𝑝 = 0.23; | sensitivity | 𝑝 < 2× |                                          |     |     |     |
10−16,𝜂 2 =0.33).SeeAppx.B.1fortaskscores. ReliableRangeChecking
𝑝
ResponseTime.Amulti-wayANOVApredictingresponsetime When participants described how they answered the recourse-
|     |     |     |     |     |     | driven task questions, | a notion of assessing | the "fitness" | of an |
| --- | --- | --- | --- | --- | --- | ---------------------- | --------------------- | ------------- | ----- |
(Sec.4.3)withexplanationtypeandpresentationfindspresentation
hasasmallyetsignificanteffect(𝑝 =5.89×10−3,𝐹 =5.24,𝜂 2 = instancetoanexplanationwascommon.Thisfellintothreesub-
𝑝
0.0409)whiletypehasnoeffect(𝑝 =0.59).ATukeytestreveals themes:a)ambiguousdistance,b)rangechecking,andc)wiggleroom.
visualpresentationsresultedinsignificantlyfasterresponsetimes Participantsusingpoint-basedexplanationsoftenreliedonanotion
thannaturallanguagepresentations(𝑝 =3.94×10−3)byseveral ofambiguousdistance(45/125)byassumingthatinstanceswhich
were"close"(Q.2),"similarto"(Q.3),or"nearest"(Q.1)indistanceto
minutes(visual𝜇=6.00±0.30;language𝜇=8.17±0.58).Response
timesfornumericstyles(𝜇=7.02±0.50)couldnotbesignificantly thecounterfactualpointbetterfittheexplanationandwerethus
distinguished.Separatelinearregressionsfoundresponsetimeis morelikelytoreceivethedesiredloanapprovaloutcome.Thisla-
notassociatedwithsubjective(𝑝 =0.23)orobjectiveunderstand- tentassumptionisneitherguaranteednorholdsformanycases,
ing(𝑝 =0.39),orresponseconfidence(𝑝 =0.86). e.g.,anearbypointmaybeacrossthedecisionboundaryandget
rejectedwhileafarpointisapproved.It’salsounclearhowcloseis
SatisfactionandTrust.Werantwomulti-wayANOVAsusing
explanationtypeandpresentationtopredictuser-reportedsatis- "closeenough"(Q.6),andthislikelyvarieswidelybetweenusers.
factionandtrust.Theserevealedalargesignificanteffectofexpla- Incontrast,manyfewer(14/127)participantsusingregion-based
nationtypeonsatisfaction(𝑝 <8×10−11,𝐹 =42.21,𝜂 2 =0.1582) explanationsmadedeterminationsbasedondistance.Instead,they
𝑝
|                                           |     |     |     | <1.74×10−4,𝐹 |     | frequentlyperformedrangechecking(59/127)wheretheyevaluate |     |     |     |
| ----------------------------------------- | --- | --- | --- | ------------ | --- | --------------------------------------------------------- | --- | --- | --- |
| andasmallsignificanteffectoftypeontrust(𝑝 |     |     |     |              | =   |                                                           |     |     |     |
iftheapplication’svaluesare"within"(Q.7)or"fitinto"(Q.10)the
12.54,𝜂 2 =0.0553).Noeffectswerefoundforexplanationpresenta-
| 𝑝                         |     |     |                 |         |     | explanation’srangeonthatfeature.Mostparticipantslookedfor |     |     |     |
| ------------------------- | --- | --- | --------------- | ------- | --- | --------------------------------------------------------- | --- | --- | --- |
| tionaloneonsatisfaction(𝑝 |     |     | =0.50)ortrust(𝑝 | =0.27). |     |                                                           |     |     |     |
matchesonallfeatures,butthosethatdidn’ttendedtomapthe
1689

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
number of ranges met to the likelihood of approval (Q.8). This confidence(𝐻2𝑎 )thanpoint-basedcounterfactualsamongourpop-
underlyingbeliefismathematicallytrue,butinpracticeonlypoints ulationoflayusers.Further,ourexploratoryanalysisconfirmsthat
thatsatisfyallrangesareguaranteedthedesiredoutcome.Similarly, objectiveunderstandingremainshigherforregion-basedcounter-
inthesensitivitytaskparticipantsusingregion-basedexplanations factualsacrossallthreerecourse-relatedtaskareas(Sec5.2).This
regularly used and even named (Q.11, Q.12) a notion of wiggle indicatesthatusingregion-basedcounterfactuals,layusersarebet-
room(42/127).Thismapsneatlytothegoalofidentifyingfeatures terabletoidentifytherequiredcounterfactualalterations,assess
neardecisionboundaries,withparticipantsreferencingthe"limit" thefitnessofaninstancewithrespecttothosechanges,anddiscern
(Q.13)"maximum"(Q.14),or"borderline"(Q.15)oftheregion’srange. whichfeaturesofaninstancearenearesttodeviatingfromthe
Combined,thesepatternsdemonstratethevalueofregion-based proposedalterations.Thesestrongincreasesmaybeduetothe
counterfactualstoprovidecriteriathatareeasilyunderstoodby morereliableprocessofrangecheckingthatweobserveinour
realusersandwhichhelpresolveissuesofambiguousdistance qualitativeanalysis(Sec.6.1).Ourhypothesistestsalsofindthat
underlyingtheuseofpoint-basedcounterfactuals. participantsaccuratelyidentifiedtheirincreasedabilitytoperform
thesetasks;withbothsubjectiveunderstandingandresponsecon-
fidencebeingpositivelyassociatedwithobjectiveunderstanding
6.2 UsersSeekJustificationForCounterfactuals
ThatDon’tMatchTheirAssumptions
(𝐻3𝑎 ,𝐻
3𝑏
). Finally, evidence from our exploratory analysisalso
findscorrespondingincreasesinreportedsatisfactionandtrustin
Whenaskedtodescribetheclarityofthegivenexplanations,a theautomateddecisionsystemamongparticipantswithregion-
patternofinformationalunderstandingcombinedwithjustification basedcounterfactuals.Incombination,theseresultsindicatethat
seekingwascommon.Thispatternispresentthroughparallelsub- region-basedcounterfactualsarewellsuitedforusebylayusers
themesofa)actionclarity,andb)assumptionsofreasoning.For andmayholdsignificantpromiseforpracticalactionablerecourse.
example, one participant wrote "I think the explanation of why Toleveragethesefindings,machinelearningexpertsshouldcon-
theloanwasrejectedisclear,butWHYthosecriteriaarevaliddoes sidera)focusingondevelopingregion-basedexplanationapproaches
notmakesense" (Q.20).Indeed,participantsgenerallyfoundthe similartothosefromemergingmethods[17,20,60]forawidervariety
informationgivenbytheexplanationstobeeasytounderstand,
ofmodeltypes;andb)investigatingefficientmethodsforembedding
withmany(74/252,excludingsinglewordyes/noresponses)giving
region-basedcounterfactualsaspartofstandardpracticewhencreat-
whollypositivedescriptionsoftheexplanationUI.Thisincluded
ingsystemsforhigh-stakesautomateddecision-making.
strongindicationsthattheyunderstoodthesuggestedalterations
(Q.18,Q.19)andresponseshighlightingthatspecificcharacteristics
suchastheuseofcolorwerehelpful(Q.16,Q.17). 7.2 EffectsofExplanationPresentation:ACall
Despitethis,manyparticipants(69/252)expressedconfusion forAdditionalExamination
overwhythespecificcounterfactualvalueswereselected.Inpar- Theeffectsofcounterfactualexplanationpresentationarelessclear
ticular,participantspointedat"counterintuitive"(Q.21)suggestions thantheeffectsofcounterfactualtype.Consideringtheresultsof
(e.g.,increasingtheloanamounttoobtainapproval)tonot"make ourhypothesistests(Sec.5.1),wedidnotfindsignificantevidence
sense"(Q.22)ortobe"illogical"(Q.22)andsoughtfurtherexplana- ofexplanationpresentationinteractingwithexplanationtypeon
tionsofwhythesechangesweresuggested(Q.24).Thisrevealsthat objectiveunderstanding(𝐻 ),norevidenceofexplanationpresen-
1𝑏
usershavestrongunderlyingassumptionsabouthowanautomated tationalonehavinganeffectonsubjectiveunderstanding(𝐻 ).
1𝑑
decision-systemworks–namelythatsuchsystemsdoorshould Similarly,exploratoryanalysesrevealednoevidenceforaneffect
closelyfollowhumanreasoning.Inpracticemanycounterintuitive ofexplanationpresentationonusers’reportedsatisfactionortrust
counterfactualchangesarepossibleasmachinelearningsystems (Sec5.2).Implicationsforthelackoftheseeffectsaremixed.On
arenotconstrainedtofollowsuchnotions.Further,anexplanation onehand,observingthatthreedifferentexplanationpresentations
thatseemscounterintuitiveorunreasonableatfirstglancemay achievethesamelevelofuserunderstandingmayindicatethat
havearationallygroundedunderpinning–e.g.,amicrolending layusersarecapableofdigestingcounterfactualexplanationin-
servicerejectingapplicantswhoseincomesaretoohigh,orabank formationthroughavarietyofmodalities.Ontheotherhand,the
rejectingaloanamountthatistoosmalltobeprofitable.Without lackofobservedeffectsdoesnotgiveaclearindicationofbest
suchajustification,participantsquestionexplanationsthatdeviate practicesforHCIdesignstomaximizeuserunderstanding.This
fromtheirassumptions,withafewevenraisingconcernsthatthe maybedueinparttotheintentionalsimilarityindesignofthe
underlyingdecisionsystemmaybe"predatory"(Q.26)or"sketchy" numeric,naturallanguage,andvisualpresentationsweexamine.
(Q.25).Thismayhavesubstantialimpactsonperceptionsoffairness Tominimizeconfoundingvariablesallthreepresentationscontain
andtrustworthiness. identicalinformation,applythesamecolorcodingschema,andare
presentedincontextofthesameexplanationinterface.Whilethis
7 DISCUSSIONANDRECOMMENDATIONS leadstoconsistentinterfacesdesigns,wecannotensuretheyare
optimalandthereforeanexaminationofmorediversepresentations
7.1 EffectsofExplanationType:ClearWinsfor
mayrevealmoresignificantdifferencesinunderstanding.
Region-BasedCounterfactuals Despitethelackofevidenceforeffectsofpresentationonuser
Resultsfromourhypothesistests(Sec.5.1)findthatregion-based understanding,ourhypothesistestsdofindthatexplanationpresen-
counterfactualexplanationsleadtosignificantlyhigherobjective tationhasasmallsignificantmoderatingeffectonexplanationtype
understanding(𝐻1𝑎 ),subjectiveunderstanding(𝐻1𝑐 ),andresponse forresponseconfidence(𝐻2𝑏).Further,inourexploratoryanalysis,
1690

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
weobservealargesignificanteffectofpresentationonresponse weperformabetween-subjectsuserstudytoevaluatetheeffectsof
time,withparticipantsusingnaturallanguagepresentationstak- counterfactualexplanationtypeandpresentationonlayuserun-
ingonaveragemorethantwominuteslongerthanthoseusing derstandinginaloanapplicationscenario.Ouranalysisfindsthat
visualpresentations.Thismaybeduetotheneedtoscanthenatural region-basedcounterfactualsresultinsignificantlyhigherobjective
languagepresentationmultipletimestolocatetherequiredexplana- understanding,subjectiveunderstanding,andresponseconfidence
tioninformation,withthevisualpresentationallowingparticipants comparedtopoint-basedcounterfactuals.Wealsofindthatregion-
tolocatethesameinformationmuchmorequickly.Theseresults basedcounterfactualsleadtosignificantlyhigherusersatisfaction
suggestthatwhileexplanationpresentationmaynotimproveuser andtrust.Basedontheseresults,werecommendmachinelearning
understanding,differentpresentationstylesmayincreaseorde- expertsfocusonthedevelopmentoftheseregion-basedcounterfac-
creasetheamountofeffortrequiredtoreachthatunderstanding. tualtechniquesandincludesuchexplanationsaspartofpractical
Thismayberelevantfordomainswithlow-motivationuserswho automated decision-making systems. Additionally, we find that
maydeclinetoexpendtherequiredeffortandwhererapidexplana- explanationpresentationcansignificantlymoderatesomeofthe
tioninterpretationispertinentfordecision-making. aboveeffectsofexplanationtype,andthatnaturallanguagepresen-
Tofullyunderstandtheeffectsofdifferentexplanationspresenta- tationsgreatlyincreasesresponsetimescomparedtovisualones.
tionswesuggestHCIresearchersexamineabroaderarrayofdesign Giventherecentexplosionofautomateddecision-makingsystems
optionsforexplanationinterfacesbothwithincounterfactualexpla- andthecorrespondingincreaseinregulatoryscrutiny,ourfindings
nation,andamongexplanationsystemsmorebroadly.Whileexisting pointtoanunmnetneedforHCIandfairnessresearcherstostudy
humanstudiesarevaluableindemonstratingthepotentialbenefits howbesttoserveuserswitheffectiveexplanationinformationto
andpitfallsofexplanation,it’scriticalthatwegobeyondexplanation enablediverseuserpopulationstoeffectivelyutilizeexplanations
contentaloneandexaminehowpresentationmayhelp(orharm)user acrossavarietyofhigh-stakesdomains.
experiencesinexplanationworkflows.
ACKNOWLEDGMENTS
8 LIMITATIONSANDFUTUREWORK This research was supported in part by NSF under grants IIS-
Our work has the following limitations that may be addressed 1910880,CSSI-2103832,CNS-1852498,NRT-HDR-2021871andthe
throughfuturework.First,aswithmanystudiesourfindingsare U.S.DepartmentofEducationundergrantP200A180088.Thanks
contextspecific.Weexaminetheeffectsofcounterfactualexplana- alsotothemembersoftheDAISYresearchgroup.
tiontypeandpresentationonlayuserunderstandingforactionable
recourseofloanapplicationdecisions.Whileourinsightsinthis
RESEARCHETHICSANDSOCIALIMPACT
contextaresubstantial,futureworkisneededtoevaluatehowthese
EthicalConsiderations.Weconsideredandaddressedthefollow-
findingsgeneralizetootherdomainscenarioswithdifferentfactors
ingethicalfactorswhendesigningourstudy.
andstakesandtoconsiderawidervarietyofpresentationstyles.
ScenarioSelection.Asactionablerecourseisespeciallycriticalfor
Evaluationofdifferentuserpopulationsshouldalsobeconsidered,
consequentialdecisions,wewereinterestedinstudyingtheeffects
includingnon-layusergroupsasappropriateforthetargetdomain.
ofcounterfactualexplanationforarealistic,relativelyhighstakes
Second,ourworkfocusesprimarilyonevaluatinguserunderstand-
scenario.However,wedidnotwanttouseascenariowhichmight
ing.InSec.5.2,wefindexplanationtypesignificantlyaffectsuser
causeourparticipantsunduestress.Wechosenottoworkwith
trustandsatisfactionasmeasuredbysingleLikert-stylequestions.
theavailableCOMPASrecidivismdatasetasacarceralscenario
However,asthesefactorsareimportantforthepracticaluseof
mayraisetraumaticexperiencesforparticipantswhohaveahis-
explanations,amorein-depthevaluationwouldbevaluable.Other
torywiththecriminallegalsystem.Similarly,weconsideredusing
metricssuchasperceptionsoffairnessandjusticearealsorele-
undergraduateapplicantdatafromourinstitution,butavoideddo-
vantandworthinvestigating.Thirdandlastly,ourstudyistailored
ingsoasthismaybeapointofstressforsomeparticipantsand
specificallytowardsactionablerecoursefornegativedecisionout-
couldpotentiallyinvolvepartialdisclosureofrealstudentdata,
comes.Suchrecoursereliesonfundamentalassumptionsaboutthe
evenifanonymized.Morebroadly,wefeltthatusingsuchscenar-
mutabilityoffeaturesandusers’abilitiestoenacttheproposed
iosmayinadvertentlyendorseornormalizetheuseofautomated
alterations.Themerepresenceofcounterfactualexplanationsdoes
decision-makingsystemsinthesedomains,wheresuchusesremain
notguaranteethesetobetrue.Thus,thisworkshouldnotbeused
controversial.Wechosetheloanapplicationscenariobecause1)
tojustifytheautomationofconsequentialdecisionswithoutcare-
thedatasetispubliclyavailableonKaggle;2)thescenarioisreason-
fulconsiderationofthenegativeimpactsonusers.Asautomated
ablybutnotoverlyconsequential;and3)automatedsystemsare
decision-makingsystemsincreasinglydeterminetheshapeofour
largelyacceptedformakingsuchdecisions.Additionally,thefinan-
society,agreatdealoftechnicalandlegalworkremainsneededto
cialfieldhasacomparativelylonghistoryofprotectiveregulation
ensurethatautomateddecision-makingsystemsareusedethically
tostructuretheuseofallowabledecision-makingprocesses.We
andthattheirdecisionscanbereliablyauditedandfairlycontested.
alsospecificallyexcludeddatasetfeaturesrelatedtodemographic
andpersonalbackgroundasthesearenotpracticallyactionableand
9 CONCLUSION couldraiseissuesofbiasifusedbythedecision-makingsystem.
Inthiswork,webridgethegapbetweenXAImethodsdevelopment ParticipantRightsandPrivacy.Asthefieldofdatacollectionhas
anduserperspectivesbyexamininghowlayusersexperienceexpla- beenknowntoexploitcrowd-sourcedlabor,wetookthefollowing
nationsforactionablerecourseofautomateddecisions.Inparticular, stepstoprotectourparticipants.First,allparticipantswererequired
1691

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
tocompleteaconsentformtoensuretheyunderstoodthestudy Non-ExpertUsers:AnExplanationUserInterfacePropositionandUserStudy.
expectations.Thisincludedthestudygoal,risks/benefits,compen- InProceedingsofthe28thInternationalConferenceonIntelligentUserInterfaces
sation,expectedduration,therighttoexitatanytime,andcontact
(Sydney,NSW,Australia)(IUI’23).AssociationforComputingMachinery,New
York,NY,USA,188–203. https://doi.org/10.1145/3581641.3584082
informationforourInstitutionalReviewBoard(IRB)office.Sec- [5] Virginia Braun and Victoria Clarke. 2006. Using thematic
ond,weusedinternaltestingandasmallpilotstudytodetermine analysis in psychology. Qualitative Research in Psychology 3,
2 (2006), 77–101. https://doi.org/10.1191/1478088706qp063oa
theaveragecompletiontimeandadjustedcompensationtomeet arXiv:https://www.tandfonline.com/doi/pdf/10.1191/1478088706qp063oa
theminimumwageinourjurisdiction($15/hr).Third,torespect [6] Hao-FeiCheng,RuotongWang,ZhengZhang,FionaO’Connell,TerranceGray,
participant’sprivacywerecruitedrespondentspseudonymously F.MaxwellHarper,andHaiyiZhu.2019.ExplainingDecision-MakingAlgorithms
throughUI:StrategiestoHelpNon-ExpertStakeholders.InProceedingsofthe
viaProlificandreplacedProlificIDswithrandomizedParticipant 2019CHIConferenceonHumanFactorsinComputingSystems(Glasgow,Scotland
IDsbeforeanalysis.AllresearchersalsounderwentCITIProgram Uk)(CHI’19).AssociationforComputingMachinery,NewYork,NY,USA,1–12.
https://doi.org/10.1145/3290605.3300789
trainingforresponsibledatahandling.Finally,toavoidpressuring
[7] Hao-FeiCheng,RuotongWang,ZhengZhang,FionaO’Connell,TerranceGray,
participants,alldemographicquestionswereoptionalandcollected F.MaxwellHarper,andHaiyiZhu.2019.ExplainingDecision-MakingAlgorithms
flexibly(e.g.,ageinrangebrackets,genderasopenresponse,and throughUI:StrategiestoHelpNon-ExpertStakeholders.InProceedingsofthe
2019CHIConferenceonHumanFactorsinComputingSystems(Glasgow,Scotland
multipleselectableraceoptionsincludingacustomoption).Demo- Uk)(CHI’19).AssociationforComputingMachinery,NewYork,NY,USA,1–12.
graphicdetailswerecollectedtocharacterizeoursamplepopulation https://doi.org/10.1145/3290605.3300789
andcontextualizeourresults,butwerenotusedaspredictivefac- [8] VClarkeandVBraun.2019. Guidelinesforreviewersandeditorsevaluating
thematicanalysismanuscripts.TechnicalReport.UniversityofAuckland.
torsforanalysis.Theaboveprocessandallsurveycontentwas [9] JCohen.1988.Statisticalpoweranalysisforthebehavioralsciences(2ed.).Rout-
reviewedandapprovedbyourIRB. ledge,Oxfordshire,UnitedKingdom. https://doi.org/10.4324/9780203771587
[10] ZhichengCui,WenlinChen,YujieHe,andYixinChen.2015. OptimalAction
ResearcherPositionality.Theresearchersconductingthiswork
ExtractionforRandomForestsandBoostedTrees.InProceedingsofthe21th
comefromalargelyAmericanbackgroundwithresearchexperi- ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining
enceincomputationalsolutionstohuman-centricdataproblems, (Sydney,NSW,Australia)(KDD’15).AssociationforComputingMachinery,New
York,NY,USA,179–188. https://doi.org/10.1145/2783258.2783281
androbustaccesstoeducationalandtechnologicalresources.These [11] ColinCurtain.2023.QualCoder.ccbogel. https://github.com/ccbogel/QualCoder/
factorsinevitablyinfluencethedesignofourstudyandtheanalysis releases/tag/3.4
ofourresults.Thus,ourrecommendationsmaynotbeequallyap- [12] AmitDhurandhar,TejaswiniPedapati,AvinashBalakrishnan,Pin-YuChen,
KarthikeyanShanmugam,andRuchirPuri.2019.ModelAgnosticContrastive
plicableorappropriatefortheuseofexplanationsandautomated Explanations for Structured Data. CoRR abs/1906.00117 (2019), 12 pages.
decision-making systems in populations with different cultural arXiv:1906.00117 http://arxiv.org/abs/1906.00117
[13] WillHeavenDouglas.2020. Predictivepolicingalgorithmsareracist. MIT
normsorlanguageuse,andinpopulationswhereaccesstoeduca-
TechnologyReview. https://www.technologyreview.com/2020/07/17/1005396/
tionandtechnologymaybemorelimited. predictive-policing-algorithms-racist-dismantled-machine-learning-bias-
AdverseImpacts.Thefindingsofthisworkshouldnotbeseento criminal-justice/
[14] SanghamitraDutta,JasonLong,SaumitraMishra,CeciliaTilli,andDanieleMag-
inanywayendorseorjustifytheuseofautomateddecision-making azzeni.2022.RobustCounterfactualExplanationsforTree-BasedEnsembles.In
systemsforhigh-stakestasks.Indeed,theproliferationofmachine Proceedingsofthe39thInternationalConferenceonMachineLearning(Proceedings
learningsystemsincriticaldecision-makinghasandwillcontinue ofMachineLearningResearch,Vol.162),KamalikaChaudhuri,StefanieJegelka,
LeSong,CsabaSzepesvari,GangNiu,andSivanSabato(Eds.).PMLR,Baltimore,
toshapesocietyandprofoundlyaffectindividualslives,particularly MD,USA,5742–5756. https://proceedings.mlr.press/v162/dutta22a.html
ascompaniesoftenfailtotakeseriouslyeventhemostbasicduties [15] RubénR.Fernández,IsaacMartíndeDiego,VíctorAceña,AlbertoFernández-
Isabel,andJavierM.Moguerza.2020.Randomforestexplainabilityusingcoun-
ofcareforhowsuchsystemsimpactthepeopletheytouch.The
terfactualsets.InformationFusion63(2020),196–207. https://doi.org/10.1016/j.
mereadditionofexplanationslikethosestudiedinthisworkdoes inffus.2020.07.001
notmitigatetheseeffectsandexplanationshouldnotbeusedto [16] JosephBFuller,ManjariRaman,EvaSage-Gavin,andKristenHines.2021.Hidden
workers:Untappedtalent.TechnicalReport.HarvardBusinessSchoolProjecton
createamisplacedsenseoftrustorotherwisemisrepresentthe ManagingtheFutureofWorkandAccenture.
decision-makingprocess.Withorwithoutexplanations,automated [17] SainyamGalhotra,RomilaPradhan,andBabakSalimi.2021.ExplainingBlack-Box
decisionsystemscanbeusedtoreinforcehistoricalpatternsof AlgorithmsUsingProbabilisticContrastiveCounterfactuals.InProceedingsofthe
2021InternationalConferenceonManagementofData(VirtualEvent,China)(SIG-
marginalization,automateunjustsystemsofpower,andforeclose MOD’21).AssociationforComputingMachinery,NewYork,NY,USA,577–590.
opportunitiesformeaningfulchange.Wethereforeencouragegov- https://doi.org/10.1145/3448016.3458455
[18] OscarGomez,SteffenHolter,JunYuan,andEnricoBertini.2020.ViCE:Visual
ernments,communitymembers,andlabororganizationstouse
CounterfactualExplanationsforMachineLearningModels.InProceedingsof
explanationsasonlyoneofmanytoolsfordeeplyexaminingsuch the25thInternationalConferenceonIntelligentUserInterfaces(Cagliari,Italy)
systems,andtotakeactionwhenneededtoensurethatifdecision- (IUI’20).AssociationforComputingMachinery,NewYork,NY,USA,531–535.
https://doi.org/10.1145/3377325.3377536
makingistobeautomated,itisdoneinawaythatprotectsthe [19] RiccardoGuidotti.2022. Counterfactualexplanationsandhowtofindthem:
rightsofdecisionsubjects,andleadstofairandjustoutcomes. literaturereviewandbenchmarking.DataMiningandKnowledgeDiscovery36
(2022),1–55. https://doi.org/10.1007/s10618-022-00831-6
[20] RiccardoGuidotti,AnnaMonreale,SalvatoreRuggieri,DinoPedreschi,Franco
Turini,andFoscaGiannotti.2018.LocalRule-BasedExplanationsofBlackBox
REFERENCES
DecisionSystems. CoRRabs/1805.10820(2018),10pages. arXiv:1805.10820
[1] EqualCreditOpportunitiesAct.1974.PublicLaw,15C.F.R§1691,RegulationB http://arxiv.org/abs/1805.10820
12C.F.R.§1002. [21] JenniferLHughes,AbigailACamden,TenzinYangchen,etal.2016. Rethink-
[2] AminaAdadiandMohammedBerrada.2018. Peekinginsidetheblack-box:a ingandupdatingdemographicquestions:Guidancetoimprovedescriptionsof
surveyonexplainableartificialintelligence(XAI).IEEEaccess6(2018),52138– researchsamples.PsiChiJournalofPsychologicalResearch21,3(2016),138–151.
52160. [22] MauriceJakesch,ZanaBuçinca,SaleemaAmershi,andAlexandraOlteanu.2022.
[3] SebastiãoBarrosValeandGabrielaZanfir-Fortuna.2022.Automateddecision- HowDifferentGroupsPrioritizeEthicalValuesforResponsibleAI.InProceedings
makingunderthegdpr:Practicalcasesfromcourtsanddataprotectionauthorities. ofthe2022ACMConferenceonFairness,Accountability,andTransparency(Seoul,
TechnicalReport.FutureofPrivacyForum. RepublicofKorea)(FAccT’22).AssociationforComputingMachinery,NewYork,
[4] ClaraBove,Marie-JeanneLesot,CharlesAlbertTijus,andMarcinDetyniecki. NY,USA,310–323. https://doi.org/10.1145/3531146.3533097
2023. InvestigatingtheIntelligibilityofPluralCounterfactualExamplesfor
1692

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
[23] AngwinJulia,JeffLarson,SuryaMattu,andLaurenKirchner.2016.MachineBias. [42] AxelParmentierandThibautVidal.2021.OptimalCounterfactualExplanations
ProPublica. https://www.propublica.org/article/machine-bias-risk-assessments- inTreeEnsembles.InProceedingsofthe38thInternationalConferenceonMachine
in-criminal-sentencing Learning(ProceedingsofMachineLearningResearch,Vol.139),MarinaMeilaand
[24] Kaggle.2008.LoanPredication.https://www.kaggle.com/datasets/ninzaami/loan- TongZhang(Eds.).PMLR,Virtual,8422–8431. https://proceedings.mlr.press/
predication,. v139/parmentier21a.html
[25] KentaroKanamori,TakuyaTakagi,KenKobayashi,andHirokiArimura.2020. [43] Article29DataProtectionWorkingParty.2016.GuidelinesonAutomatedIndi-
DACE:Distribution-AwareCounterfactualExplanationbyMixed-IntegerLinear vidualDecision-MakingandProfilingforthePurposesofRegulation2016/679.
Optimization.InProceedingsoftheTwenty-NinthInternationalJointConference https://ec.europa.eu/newsroom/article29/items/612053
onArtificialIntelligence,IJCAI-20,ChristianBessiere(Ed.).InternationalJoint [44] ForoughPoursabzi-Sangdeh,DanielGGoldstein,JakeMHofman,JenniferWort-
ConferencesonArtificialIntelligenceOrganization,Yokohama,Kanto,Japan, manWortmanVaughan,andHannaWallach.2021. ManipulatingandMea-
2855–2862. https://doi.org/10.24963/ijcai.2020/395Maintrack. suringModelInterpretability.InProceedingsofthe2021CHIConferenceon
[26] Amir-HosseinKarimi,GillesBarthe,BernhardSchölkopf,andIsabelValera.2022. HumanFactorsinComputingSystems(Yokohama,Japan)(CHI’21).Associa-
ASurveyofAlgorithmicRecourse:ContrastiveExplanationsandConsequential tionforComputingMachinery,NewYork,NY,USA,Article237,52pages.
Recommendations. ACMComput.Surv.55,5,Article95(dec2022),29pages. https://doi.org/10.1145/3411764.3445315
https://doi.org/10.1145/3527848 [45] RafaelPoyiadzi,KacperSokol,RaulSantos-Rodriguez,TijlDeBie,andPeter
[27] Amir-HosseinKarimi,BernhardSchölkopf,andIsabelValera.2021.Algorithmic Flach.2020. FACE:FeasibleandActionableCounterfactualExplanations.In
Recourse:FromCounterfactualExplanationstoInterventions.InProceedingsof ProceedingsoftheAAAI/ACMConferenceonAI,Ethics,andSociety(NewYork,
the2021ACMConferenceonFairness,Accountability,andTransparency(Virtual NY,USA)(AIES’20).AssociationforComputingMachinery,NewYork,NY,USA,
Event,Canada)(FAccT’21).AssociationforComputingMachinery,NewYork, 344–350. https://doi.org/10.1145/3375627.3375850
NY,USA,353–362. https://doi.org/10.1145/3442188.3445899 [46] Prolific.2023. Prolificcrowsourcingplatform. https://www.prolific.com. Ac-
[28] MarkTKeane,EoinMKenny,EoinDelaney,andBarrySmyth.2021. IfOnly cessed:2023-12-04.
WeHadBetterCounterfactualExplanations:FiveKeyDeficitstoRectifyinthe [47] Qualtrics.2023.QualtricsExperienceManagement.https://www.qualtrics.com.
EvaluationofCounterfactualXAITechniques. arXiv:2103.01035[cs.LG] Accessed:2023-12-04.
[29] UlrikeKuhl,AndréArtelt,andBarbaraHammer.2022.KeepYourFriendsClose [48] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin.2016."WhyShouldI
andYourCounterfactualsCloser:ImprovedLearningFromClosestRatherThan TrustYou?":ExplainingthePredictionsofAnyClassifier.InProceedingsofthe
PlausibleCounterfactualExplanationsinanAbstractSetting.InProceedingsof 22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
the2022ACMConferenceonFairness,Accountability,andTransparency(Seoul, Mining(SanFrancisco,California,USA)(KDD’16).AssociationforComputing
RepublicofKorea)(FAccT’22).AssociationforComputingMachinery,NewYork, Machinery,NewYork,NY,USA,1135–1144. https://doi.org/10.1145/2939672.
NY,USA,2125–2137. https://doi.org/10.1145/3531146.3534630 2939778
[30] UlrikeKuhl,AndréArtelt,andBarbaraHammer.2023. Let’sgototheAlien [49] Y.Rong,T.Leemann,T.Nguyen,L.Fiedler,P.Qian,V.Unhelkar,T.Seidel,G.
Zoo:Introducinganexperimentalframeworktostudyusabilityofcounterfactual Kasneci,andE.Kasneci.5555. TowardsHuman-CenteredExplainableAI:A
explanationsformachinelearning.FrontiersinComputerScience5(2023),20. SurveyofUserStudiesforModelExplanations. IEEETransactionsonPattern
[31] ThaiLe,SuhangWang,andDongwonLee.2020.GRACE:GeneratingConciseand Analysis&MachineIntelligence36,01(nov5555),1–20.Issue33. https://doi.org/
InformativeContrastiveSampletoExplainNeuralNetworkModel’sPrediction. 10.1109/TPAMI.2023.3331846
InProceedingsofthe26thACMSIGKDDInternationalConferenceonKnowledge [50] MaximilianSchleich,ZixuanGeng,YihongZhang,andDanSuciu.2021.GeCo:
DiscoveryandDataMining(VirtualEvent,CA,USA)(KDD’20).Associationfor QualityCounterfactualExplanationsinRealTime.Proc.VLDBEndow.14,9(oct
ComputingMachinery,NewYork,NY,USA,238–248. https://doi.org/10.1145/ 2021),1681–1693. https://doi.org/10.14778/3461535.3461555
3394486.3403066 [51] JakobSchoeffer,NiklasKuehl,andYvetteMachowski.2022.“ThereIsNotEnough
[32] ColinLecher.2019.HowAmazonautomaticallytracksandfireswarehousework- Information”:OntheEffectsofExplanationsonPerceptionsofInformational
ersfor‘productivity’.TheVerge.https://www.theverge.com/2019/4/25/18516004/ FairnessandTrustworthinessinAutomatedDecision-Making.InProceedingsof
amazon-warehouse-fulfillment-centers-productivity-firing-terminations the2022ACMConferenceonFairness,Accountability,andTransparency(Seoul,
[33] MichaelDLeeandEric-JanWagenmakers.2014.Bayesiancognitivemodeling: RepublicofKorea)(FAccT’22).AssociationforComputingMachinery,NewYork,
Apracticalcourse. Cambridgeuniversitypress,Cambridge,England. https: NY,USA,1616–1628. https://doi.org/10.1145/3531146.3533218
//doi.org/10.1017/CBO9781139087759 [52] GesinaSchwalbeandBettinaFinzel.2023. Acomprehensivetaxonomyfor
[34] ScottMLundbergandSu-InLee.2017.AUnifiedApproachtoInterpretingModel explainableartificialintelligence:asystematicsurveyofsurveysonmethodsand
Predictions.InAdvancesinNeuralInformationProcessingSystems,I.Guyon,U.V. concepts.DataMiningandKnowledgeDiscovery37(2023),1–59.Issue1.
Luxburg,S.Bengio,H.Wallach,R.Fergus,S.Vishwanathan,andR.Garnett(Eds.), [53] DylanSlack,SatyapriyaKrishna,HimabinduLakkaraju,andSameerSingh.2023.
Vol.30.CurranAssociates,Inc.,LongBeach,CA,USA. https://proceedings. Explainingmachinelearningmodelswithinteractivenaturallanguageconver-
neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf sationsusingTalkToModel. NatureMachineIntelligence5,8(2023),873–883.
[35] Enmanual Martinez, Lauren Kirchner, and The Markup. 2021. The se- https://doi.org/10.1038/s42256-023-00692-8
cret bias hidden in mortgage-approval algorithms. Associated Press. [54] IliaStepin,JoseM.Alonso,AlejandroCatala,andMartínPereira-Fariña.2021.
https://apnews.com/article/lifestyle-technology-business-race-and-ethnicity- ASurveyofContrastiveandCounterfactualExplanationGenerationMethods
mortgages-2d3d40d5751f933a88c1e17063657586 forExplainableArtificialIntelligence.IEEEAccess9(2021),11974–12001. https:
[36] TimMiller.2019.Explanationinartificialintelligence:Insightsfromthesocial //doi.org/10.1109/ACCESS.2021.3051315
sciences.ArtificialIntelligence267(2019),1–38. https://doi.org/10.1016/j.artint. [55] MaxwellSzymanski,MartijnMillecamp,andKatrienVerbert.2021.Visual,Tex-
2018.07.007 tualorHybrid:TheEffectofUserExpertiseonDifferentExplanations.In26th
[37] BethMole.2023.UnitedHealthusesAImodelwith90%errorratetodenycare, InternationalConferenceonIntelligentUserInterfaces(CollegeStation,TX,USA)
lawsuitalleges.ArsTechnica. https://arstechnica.com/health/2023/11/ai-with- (IUI’21).AssociationforComputingMachinery,NewYork,NY,USA,109–119.
90-error-rate-forces-elderly-out-of-rehab-nursing-homes-suit-claims/ https://doi.org/10.1145/3397481.3450662
[38] RamaravindK.Mothilal,AmitSharma,andChenhaoTan.2020. Explaining [56] GabrieleTolomei,FabrizioSilvestri,AndrewHaines,andMouniaLalmas.2017.
MachineLearningClassifiersthroughDiverseCounterfactualExplanations.In InterpretablePredictionsofTree-BasedEnsemblesviaActionableFeatureTweak-
Proceedingsofthe2020ConferenceonFairness,Accountability,andTransparency ing.InProceedingsofthe23rdACMSIGKDDInternationalConferenceonKnowledge
(Barcelona,Spain)(FAT*’20).AssociationforComputingMachinery,NewYork, DiscoveryandDataMining(Halifax,NS,Canada)(KDD’17).AssociationforCom-
NY,USA,607–617. https://doi.org/10.1145/3351095.3372850 putingMachinery,NewYork,NY,USA,465–474. https://doi.org/10.1145/3097983.
[39] ShaneT.Mueller,ElizabethS.Veinott,RobertR.Hoffman,GaryKlein,Lamia 3098039
Alam,TauseefMamun,andWilliamJ.Clancey.2021.PrinciplesofExplanation [57] Meng-JungTsai,Ching-YehWang,andPo-FenHsu.2019.DevelopingtheCom-
inHuman-AISystems.CoRRabs/2102.04972(2021),10.arXiv:2102.04972 https: puterProgrammingSelf-EfficacyScaleforComputerLiteracyEducation.Journal
//arxiv.org/abs/2102.04972 ofEducationalComputingResearch56,8(2019),1345–1360. https://doi.org/10.
[40] MeikeNauta,JanTrienes,ShreyasiPathak,ElisaNguyen,MichellePeters,Yasmin 1177/0735633117746747arXiv:https://doi.org/10.1177/0735633117746747
Schmitt,JörgSchlötterer,MauricevanKeulen,andChristinSeifert.2023.From [58] BerkUstun,AlexanderSpangher,andYangLiu.2019.ActionableRecoursein
AnecdotalEvidencetoQuantitativeEvaluationMethods:ASystematicReview LinearClassification.InProceedingsoftheConferenceonFairness,Accountability,
onEvaluatingExplainableAI.ACMComput.Surv.55,13s,Article295(jul2023), andTransparency(Atlanta,GA,USA)(FAT*’19).AssociationforComputing
42pages. https://doi.org/10.1145/3583558 Machinery,NewYork,NY,USA,10–19. https://doi.org/10.1145/3287560.3287566
[41] CFPB Newsroom. 2023. CFPB Issues Guidance on Credit Denials by [59] NielsvanBerkel,JorgeGoncalves,DanielRusso,SimoHosio,andMikaelB.Skov.
Lenders Using Artificial Intelligence. Consumer Financial Protection Bu- 2021. EffectofInformationPresentationonFairnessPerceptionsofMachine
reau. https://www.consumerfinance.gov/about-us/newsroom/cfpb-acts-to- LearningPredictors.InProceedingsofthe2021CHIConferenceonHumanFactors
protect-the-public-from-black-box-credit-models-using-complex-algorithms/ inComputingSystems(Yokohama,Japan)(CHI’21).AssociationforComputing
Machinery,NewYork,NY,USA,Article245,13pages. https://doi.org/10.1145/
1693

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
3411764.3445365
[60] PeterM.VanNostrand,HuayiZhang,DennisM.Hofmann,andElkeA.Runden-
steiner.2023.FACET:RobustCounterfactualExplanationAnalytics.Proc.ACM
Manag.Data1,4,Article242(dec2023),27pages.https://doi.org/10.1145/3626729
[61] SandraWachter,BrentMittelstadt,andChrisRussell.2017. Counterfactual
ExplanationswithoutOpeningtheBlackBox:AutomatedDecisionsandthe
GDPR.Harvardjournaloflaw&technology31,2(2017),841–.
[62] XinruWangandMingYin.2021. AreExplanationsHelpful?AComparative
StudyoftheEffectsofExplanationsinAI-AssistedDecision-Making.In26th
InternationalConferenceonIntelligentUserInterfaces(CollegeStation,TX,USA)
(IUI’21).AssociationforComputingMachinery,NewYork,NY,USA,318–328.
https://doi.org/10.1145/3397481.3450650
[63] GretaWarren,RuthM.J.Byrne,andMarkT.Keane.2023. Categoricaland
ContinuousFeaturesinCounterfactualExplanationsofAISystems.InProceedings
ofthe28thInternationalConferenceonIntelligentUserInterfaces(Sydney,NSW,
Australia)(IUI’23).AssociationforComputingMachinery,NewYork,NY,USA,
171–187. https://doi.org/10.1145/3581641.3584090
[64] MireiaYurrita,TimDraws,AgatheBalayn,DaveMurray-Rust,NavaTintarev,
andAlessandroBozzon.2023.DisentanglingFairnessPerceptionsinAlgorithmic
Decision-Making:TheEffectsofExplanations,HumanOversight,andContesta-
bility.InProceedingsofthe2023CHIConferenceonHumanFactorsinComputing
Systems(<conf-loc>,<city>Hamburg</city>,<country>Germany</country>,
</conf-loc>)(CHI’23).AssociationforComputingMachinery,NewYork,NY,
USA,Article134,21pages. https://doi.org/10.1145/3544548.3581161
1694

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
A OPENRESPONSEANDSELECTEDQUOTES
Selectedquotesfromthequalitativeanalysis(Sec.6).Quotesarereferencedtoanonymousparticipantidentifierandthequestionitresponds
to."How"questionsarelabeledbywhichofthethreerecourse-relatedareas(Sec.4.3)theydescribeandareresponsestothequestionHow
didyouusetheexplanationtooltoanswerthesequestions?ThiswasaskedthreetimesduringTaskEvaluation(ProcedureStep4),onceafter
eachblockofquestionsfromthecorrespondingarea.The"clarity"questionHowdidyouusetheexplanationtooltoanswerthesequestions?
wasaskedafterTraining(ProcedureStep3,Sec.4.4).
Q.i Quote Participant
Q.1 chosethenearestvaluesofthechangessuggestedlistedinthemultiplechoice P172-Alter
Q.2 Ilookedtoseeifthenumberswereclose P44-Pred
Q.3 triedtopicktheclosestnumbersthatcorrelatetothenumbersontheapprovedside P72-Alter
Q.4 comparingthenumberandlookingfornumberthatwerecloseorthesame P34-Pred
Q.5 Ifthenumbersfortheapplicantweresimilartotheapprovednumbersfromthealgorithm,Ifeltthechancesof P91-Pred
beingapprovedwouldbehigher
Q.6 Ijudgedwhetherthestatswere"closeenough"tothealgorithmspreferences P135-Pred
Q.7 Ifall4criteriadontfitwithintheapprovedjunctionparameters,Iwouldsayitwouldberejected P10-Pred
Q.8 Iftheyfitintoeverybluecategorytheywereverylikelytobeapproved.Iftheyfitintomostofthemtheywere P174-Pred
fairlylikely,etc
Q.9 Icheckedforeachchangeandlookedtoseeifitwaswithintherange P170-Alter
Q.10 Icheckedtoseeifthechangesfitintotheamountsthealgorithimlisted P237-Alter
Q.11 Bydeducingwhichcategoryhadtheleastamountofwiggleroomtobechanged P14-Sense
Q.12 Ilookedattheparametersofeachsectionandchosetheareathathadtheleastamountof"wiggleroom" P14-Sense
Q.13 Ilookedattherangesandsawwhichwasclosesttothelimit P48-Sense
Q.14 Ifthenewnumberswereclosetobeingattheminimumormaximumoftheapprovals P188-Sense
Q.15 IfthenewapplicantstatswereborderlinetobeingintherejectedzoneIchosethose P67-Sense
Q.16 easytoseethatredportionsarerejectedandhowthingsneedtochangeinordertobecomeblueandapproved P51-Clear
Q.17 Thebluecolormakesiteasytounderstandthenecessarychangesthatwillgetyourapplicationapproved. P25-Clear
Q.18 Yes,itisveryclearaboutwhatneedstobechangedformetogetapprovedfortheloan P65-Clear
Q.19 It’seasytounderstandwhyIwasrejectedandwhatIwouldneedtodoinordertobeaccepted P188-Clear
Q.20 theexplanationofwhytheloanwasrejectedisclear,butWHYthosecriteriaarevaliddoesnotmakesense P141-Clear
Q.21 Itiseasytoread,butwhatthetoolissuggestingthatyoudoseemscounterintuitive P169-Clear
Q.22 Itdoesnotmakesensetorequirelessincomeforalargerloanthantheapplicantappliedfor P183-Clear
Q.23 Itwasconfusingbecauseitwasn’tintuitive.Whywouldaloanagencywanttogiveyoumoremoneywhileyou P27-Clear
makeless?Itseemsillogical
Q.24 Iwouldliketoseemoreexplanationaboutwhythealgorithmthinksthatcertainnumberwillallowforapproval P231-Clear
Q.25 No.Seemssketchy,though P231-Clear
Q.26 italmostseemslikeitisincentivizingapredatorynaturewhereitprefersapplicantsthatearnlessmoneyandtake P176-Clear
higherloanamountstogetmoreprofitattheexpenseofputtingthemindebt
Table2:Extractedquotesfromparticipantanswerstoopenresponsequestions
B ADDITIONALRESULTS
B.1 Task-WiseEvaluationMetrics
InSec.5.2weexaminedthesignificanceofeffectsforobjectiveunderstandingdisaggregatedbytherecourse-relatedtaskarea(Sec.4.3).
Presentedbelowaretheunderstandingscoresforeachtaskarea(range0-4foreach),aswellasthecorrespondingdisaggregatedresponse
timesforeachquestiontypeinminutes.
1695

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
Feature Alteration Understanding Instance Prediction Understanding Feature Sensitivity Understanding
3.25
3.5
3.00
CF Type 3.0
|     |     |     |     | 2.75 |     | 3.0 |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Region
|       | 2.5 |     |     | 2.50 |     |     |     |     |     |
| ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| Based |     |     |     |      |     | 2.5 |     |     |     |
| Point |     |     |     | 2.25 |     |     |     |     |     |
| Based | 2.0 |     |     |      |     | 2.0 |     |     |     |
2.00
|     |     |     |     | 1.75 |     | 1.5 |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
1.5
Numeric Nat. Language Visual Numeric Nat. Language Visual Numeric Nat. Language Visual
Figure5:Meanandstandarderroroftask-wiseunderstandingforthesixconfigurationsofcounterfactualexplanation
Feature Alteration Time (minutes) Instance Prediction Time (minutes) Feature Sensitivity Time (minutes)
3.00
|     | 3.5 |     |     |     |     | 3.5 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2.75
CF Type
|     |     |     |     | 2.50 |     | 3.0 |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Region 3.0
Based
2.25
| Point |     |     |     |      |     | 2.5 |     |     |     |
| ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|       | 2.5 |     |     | 2.00 |     |     |     |     |     |
Based
2.0
|     | 2.0 |     |     | 1.75 |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Numeric Nat. Language Visual Numeric Nat. Language Visual Numeric Nat. Language Visual
Figure6:Meanandstandarderroroftask-wiseresponsetimeforthesixconfigurationsofcounterfactualexplanation
B.2 ParticipantDemographics
Tab.3showsasummaryofthedemographicsoftheanalyzedparticipantsusingquestionsfrom[21].Notethatasallquestionswereoptional
andweallowedmultipleresponsesperparticipantforrace,thesumofeachvariablemaynotexactlymatchthetotalsamplesize.We
collectedageinbracketstopreserveanonymityandgenderinformationasanopenresponsewhichwasparsedintononbinary,man,or
woman.Wegroupthefourresponsesforsomehighschoolwiththe23forhighschooldiplomaorequivalenttocreatethehighschoolorless
categoryandmergethefourfromappliedorprofessionaldegreeintoother.
|     | Age | Education |     |     |     | Race |     |     | Gender |
| --- | --- | --------- | --- | --- | --- | ---- | --- | --- | ------ |
18-24 26 Highschoolorless 27 AmericanIndianorAlaskaNative 4 Nonbinary 3
| 25-34 | 86 Somecollege,nodegree |     |     | 54 Asian |     |     |     | 16  | Man 115 |
| ----- | ----------------------- | --- | --- | -------- | --- | --- | --- | --- | ------- |
35-44 71 Associatedegree 26 BlackorAfricanAmerican 33 Woman 124
45-54 39 Bachelor’sdegree 105 Hispanic,LatinoorSpanishOrigin 20
| 55-64 | 19 Master’sdegree |     |     | 33 MiddleEasternorNorthAfrican |     |     |     | 1   |     |
| ----- | ----------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
65-74 7 Doctoratedegree 1 NativeHawaiianorOtherPacificIslander 1
| ≥75 | 2 Other |     |     | 5 White |     |     |     | 202 |     |
| --- | ------- | --- | --- | ------- | --- | --- | --- | --- | --- |
Table3:Selfreporteddemographicdataofthe252participants
B.3 IndividualFactors
Asliteracywithcomputersystemsorfinancialdatamayaffectaparticipant’sunderstanding,weadaptedthreeagreementstatementsfrom
existingresearch[6,57]tomeasureeachconceptona6-pointscale.Wefurtherdirectlyaskparticipantstoreporttheirfamiliarityineach
conceptfromnoknowledgetoalotofknowledgeon4-pointscalesasin[6].Wenormalizedandsummedtheresponsestocreateseparate
technicalliteracyandfinancialliteracyscores,eachrangingfrom0-25.Asperceptionsoftheappropriatenessoftheuseofautomateddecision
systemsmayimpactuserbehavior,wealsocollectedanAISentimentscorebyaskingparticipantstoindicatetheiragreementwithIbelieve
it’sokayforalgorithmstobeusedtomakeimportantdecisionsona6-pointscale.SeeAppx.C.4forafulllistofthesequestions.
| 50  |     |     | 40  |     |     |     | 150 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
80
ycneuqerF
| 40  |     |     | 30  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 60  |     | 100 |     |     |
30
20
40
| 20  |     |     |     |     |     |     | 50  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10  |     |     | 10  |     | 20  |     |     |     |     |
| 0   |     |     | 0   |     | 0   |     | 0   |     |     |
3 5 7 9 1113151719212325 3 5 7 9 1113151719212325 0 1 2 3 4 5 18 25 35 45 55 65 75
|     | Technical Literacy |     |     | Financial Literacy |     | AI Sentiment |     |     | Age |
| --- | ------------------ | --- | --- | ------------------ | --- | ------------ | --- | --- | --- |
Figure7: Distributionofindividualfactorsandagefortheanalyzedparticipants(KDEsmoothed,Scott’srulefactor=1.3)
Amultiplelinearregressionusingtechnicalliteracy,financialliteracy,andAIsentiment(Fig.7)topredictobjectiveunderstandingor
responseconfidencerevealnosignificanteffects.However,thesamefactorspredictingsubjectiveunderstandingrevealsapotentialeffect
1696

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
oftechnicalliteracy(𝑝 = 0.0492,𝛽 = 0.1821),indicatingthatparticipantswhoaremorefamiliarwithgeneraltechnologymayperceive
themselvesasmorecapableofunderstandingtheautomateddecisionsystem.
C SURVEYMATERIALS
C.1 ObjectiveUnderstandingQuestions
Belowisthefulltextoftheobjectiveunderstandingquestionsasadaptedfrom[4,7].Featurealterationwordingandchoicescomedirectly
from[7]withvaluesforeachoptionchosenfromtheexplanation–i.e.,theexplanationalteredbothfeaturesandonevaluewaschosento
matchthecounterfactualandtheothernot.Foroneofthefouralterationquestionswechosebothvaluestonotmatch,making“neither”the
correctoption.Forinstancepredictionquestions,theoptionswerecreatedbychangingsomefeaturesoftheinstancetonot-matchthe
counterfactualvalues.Thisensuredthenewinstancesremainedrelevanttotheexplainedinstance.Valueswerechosensuchthattwoof
fourpredictionquestionswereApprovedandtheothertwoRejected.Newinstancesforfeaturesensitivityweregeneratedbyalteringthe
instancetomatchtheexplanationthen"moving"onefeature-valuetobeneartheendoftheApprovedrange.
QuestionType1:FeatureAlteration.Giventhefollowingexplanationinformation[ExplanationUI].Whichchangeismostlikelyto
getthisapplicationapproved?
(1) [Decreasing<featurei>from<value1>to<value2>
(2) Increasing<featurej>from<value3>to<value4>
(3) Neitherwouldincreasethechanceofapproval
QuestionType2:InstancePrediction.Giventhefollowingexplanationinformation[ExplanationUI].Consideranapplicantwith
thefollowingprofile
Attribute Value
ApplicantIncome $<value>
CoapplicantIncome $<value>
LoanAmount $<value>
LoanTerm <value>Days
Howwouldthealgorithmcategorizethisapplicant?
(A) Verylikelytoberejected
(B) Somewhatlikelytoberejected
(C) Somewhatlikelytobeaccepted
(D) Verylikelytobeaccepted
QuestionType3:FeatureSensitivity.ImaginethatyouappliedforaloanandwereREJECTEDwiththefollowingexplanation
[ExplanationUI].YouhavenowchangedyourapplicationtothefollowingvaluesandbeenAPPROVEDforaloan
Attribute Value
ApplicantIncome $<value>
CoapplicantIncome $<value>
LoanAmount $<value>
LoanTerm <value>Days
Whichattributeofyournewapplication,ifchangedbyasmallamountismostlikelytoresultinarejection?
(A) ApplicantIncome
(B) CoapplicantIncome
(C) LoanAmount
(D) LoanTerm
1697

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
C.2 SubjectiveUnderstandingQuestions
Metric Pleaseindicatehowmuchyouagreewiththefollowingstatements.
Subj.Understanding Explanationsofthealgorithmareeasytounderstand
Subj.Understanding Givenanexplanation,Icanreliablypredicthowthealgorithmwillbehave
Subj.Understanding Explanationsofthealgorithmhelpmeunderstandhowtheapprovaldecisionismade
Subj.Understanding Explanationsofthealgorithmhelpmeincreasethelikelihoodofgettingmyapplicationapproved
Subj.Understanding Iunderstandthecriteriaforloanapproval
Responses stronglydisagree,disagree,somewhatdisagree,agree,stronglyagree.
C.3 AdditionalMetricQuestions
Metric Pleaseindicatehowmuchyouagreewiththefollowingstatements.
Trust Itrustthedecisionsmadebythealgorithm
Responses stronglydisagree,disagree,somewhatdisagree,agree,stronglyagree.
Satisfaction Overall,howsatisfiedareyouwiththeexplanationsprovidedforobtainingloanapproval?
Responses notsatisfied,alittlesatisfied,somewhatsatisfied,satisfied,andhighlysatisfied.
C.4 IndividualFactorsQuestions
IndividualFactor Pleaseindicatehowmuchyouagreewiththefollowingstatements.
TechnicalLiteracy Iamconfidentusingcomputers
TechnicalLiteracy IunderstandhowAmazonrecommendsproductsformetochoose
TechnicalLiteracy Icanmakeuseofcomputerprogrammingtosolveaproblem.
FinancialLiteracy Iunderstandhowmycreditscoreiscalculated
FinancialLiteracy Iunderstandhowtofilemyowntaxes
FinancialLiteracy Ifeelcapableofmakingimportantfinancialdecisions
AISentiment Ibelieveit’sokayforalgorithmstobeusedtomakeimportantdecisions
Responses stronglydisagree,disagree,somewhatdisagree,agree,stronglyagree.
IndividualFactor Question
TechnicalLiteracy Howmuchprogrammingknowledgedoyouhave?
TechnicalLiteracy Howmuchknowledgeofcomputeralgorithmsdoyouhave?
Responses noknowledge,alittleknowledge,someknowledge,alotofknowledge.
FinancialLiteracy Howfamiliarareyouwithfinancialdata?
FinancialLiteracy Howfamiliarareyouwiththecreditapprovalprocessessuchasmakingdecisions
aboutapprovingcreditcards,loans,andmortgages?
Responses notfamiliar,alittlefamiliar,veryfamiliar,extremelyfamiliar.
C.5 ScenarioIntroduction
ThefollowinginformationwasusedtointroduceallparticipantstotheloanapplicantscenarioandexplanationUI.
Introduction.Hereweintroduceinformationyouwillneedtoanswerquestionsinthissurvey.Pleasereadcarefullyasyoucanlater
earnbonuspaymentforcorrectanswers.
Scenario.ACMEBankhasdevelopedacomputeralgorithmtoautomaticallyprocessloanapplications.Thealgorithmautomatically
decidesifaloanapplicationshouldbeAPPROVEDorREJECTED.WhichofthefollowingstatementsisTRUE?
• Thealgorithmisasetofrulesthatbankstafffollowtomanuallymakeapplicationdecisions
• Thealgorithmisacomputerprogramthatautomaticallymakesapplicationdecisions
• Thealgorithmisacomputerprogramthatrandomlygeneratesanumber
ApplicantInformation.ThealgorithmlearnsfromhistoricaldatatodecideifanapplicationshouldbeAPPROVED.Forexample,the
algorithmmayapproveanapplicantiftheirprofileissimilartothoseofpreviouslyAPPROVEDapplicants.Thealgorithmusesthe
followingattributestomakeapprovaldecisions.
1698

FAccT’24,June03–06,2024,RiodeJaneiro,Brazil VanNostrandetal.
Attribute Details
ApplicantIncome Theprimaryapplicant’stotalmonthlyincomeindollars
CoapplicantIncome Thetotalmonthlyincomeoftheloanapplicant’scosigners(suchas
afriend,partner,orparent)indollars
LoanAmount Thetotalloanamountindollars
LoanTerm Thedurationindaysthattheloanwillberepaidover
WhichofthefollowingstatementsaboutthealgorithmisFALSE?
• Thealgorithmlearnsfromhistoricalloandata
• Thealgorithmusesanapplicant’sincomeaspartofitsdecisionmaking
• Thealgorithmrandomlydecideswhichapplicanttoapprove
ExplanationTool.Imaginethatyouarealoanapplicantwhohasappliedforaloan.Yourgoalistounderstandhowthealgorithm
workswiththeexplanationtoolbelow.(Area1)showswhetherthealgorithmhasAPPROVEDorREJECTEDyourloan.
Whatdecisiondidthealgorithmmakeforyourapplication?
• APPROVE
• REJECT
(Area2)showsthevaluesforeachattributeofyourapplication.
WhichofthefollowingmatchestheApplicantIncome?
• $0
• $1,880
• $6,100
• Notshown
C.6 ExplanationTraining
ThefollowinginformationwaspresentedtoparticipantsrightaftertheIntroduction.Theexplanationimagesshownwerecustomizedto
matchtheeachexplanationconfigurationforeachgroup.
(Area3)includesanexplanationofthealgorithm’sdecision.
1699

ExaminingtheEffectsofCounterfactualExplanationTypeandPresentationonLayUserUnderstanding FAccT’24,June03–06,2024,RiodeJaneiro,Brazil
TheexplanationtoolshowschangesyoucouldmaketogetyourapplicationAPPROVED
• True
• False
In(Area3)valuesforattributeswhichmustchangeareshowninRed.TheproposednewvaluesareshowninBlue.Valuesforunchanged
attributesareshowninGrey.
TheexplanationabovesuggestschangingtheLoanAmount
• True
• False
TheexplanationbelowindicatesyourapplicationwasREJECTED,butwouldbeAPPROVEDifyoudecreaseyourApplicantIncome
ANDincreaseyourLoanAmount.ThisexplanationleavesCoapplicantIncomeandLoanTermunchanged.Forthissurveypleasedo
notconsideryourpersonalpreferencesorpriorexpectationsaboutchanginganygivenattribute
Youshouldconsideryourpersonalpreferencesorexpectationswhenconsideringchangedattributes
• True
• False
1700