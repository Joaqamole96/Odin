Article
Modeling Investment Decisions Through Decision Tree
Regression—A Behavioral Finance Theory Approach
DanaRad1,* ,LaviniaDenisiaCuc2,* ,GabrielCroitoru3 ,BogdanCosminGomoi2 ,LuminitaMazuru2,
,
RalucaSiminaBilti2,SergiuRusu2 ,MariaSinaci2 andFlorentinaSimonaBarbu2
,
1 CentreofResearchDevelopmentandInnovationinPsychology,FacultyofEducationalSciences,
AurelVlaicuUniversityofArad,310130Arad,Romania
2 CentreforEconomicResearchandConsultancy,FacultyofEconomics,AurelVlaicuUniversityofArad,
310130Arad,Romania;bogdan.gomoi@uav.ro(B.C.G.);luminita.mazuru@uav.ro(L.M.);
raluca.bilti@uav.ro(R.S.B.);sergiu.rusu@uav.ro(S.R.);maria.sinaci@uav.ro(M.S.);
florentina.barbu@uav.ro(F.S.B.)
3 FacultyofEconomics,ValahiaUniversityofTargoviste,130004Targoviste,Romania;
gabriel.croitoru@valahia.ro
* Correspondence:dana@xhouse.ro(D.R.);lavinia.cuc@uav.ro(L.D.C.)
Abstract: Thisstudyexaminesthekeyfactorsinfluencinginvestmentdecisionsthrough
decisiontreeregression,groundedinbehavioralfinancetheory. Byanalyzingacomprehen-
sivedatasetincorporatingbehavioral,demographic,andfinancialvariables—including
investmentattitudes,decision-makingbehaviors,financialeducation,age,income,and
education—thisstudyidentifiessignificantpredictorsofinvestmentoutcomes. Whilethe
modelshowsmoderatepredictiveperformance(R2 =0.185;MAPE=172.96%),itidenti-
fieshierarchicalrelationshipsamongbehavioral,cognitive,anddemographicpredictors.
Theseresultshighlightthecomplexityofinvestmentdecisionsandtheneedforintegra-
tive,behavioral-drivenapproachesinpredictivemodeling. Investmentattitudes(25.88%),
decision-makingbehaviors(19.53%),andfinancialeducation(16.68%)emergeasthemost
influentialvariables,whiletraditionaldemographicfactorssuchasincomeandagehave
alowerimpact. Thehierarchicalstructureofthedecisiontreehighlightscriticaldecision-
makingpatterns,particularlyregardingspeculativebehaviorsandinvestmentattitudes.
AcademicEditors:AgnieszkaKonys Thesefindingschallengeclassicalmodelsofrationalitybyemphasizingthedominantrole
andAgnieszkaNowak-Brzezin´ska ofbehavioralfactorsininvestmentdecisionmaking. Thisstudycontributestobridging
Received:5February2025 computationalmodelingwithfinancialeconomics,demonstratingtheutilityofdecision
Revised:5April2025 treeregressioninuncoveringcomplexinvestorbehavior. Practicalimplicationsinclude
Accepted:7April2025
enhancingpersonalizedfinancialadvisoryservicesanddesigningtargetedfinancialliteracy
Published:9April2025
programstoimprovedecision-makingefficiency. Theseinsights,whileexploratory,can
Citation: Rad,D.;Cuc,L.D.;
guidefutureresearchanddecision-supportsystemsinbehavioralfinance.
Croitoru,G.;Gomoi,B.C.;Mazuru,L.;
Bilt,i,R.S.;Rusu,S.;Sinaci,M.;Barbu,
Keywords: decisiontreeregression; investmentdecisions; behavioralfinance; financial
F.S.ModelingInvestmentDecisions
predictors;computationalmodeling
ThroughDecisionTreeRegression—A
BehavioralFinanceTheoryApproach.
Electronics2025,14,1505. https://
doi.org/10.3390/electronics14081505
1. Introduction
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland. Understandingthefactorsthatinfluenceinvestmentinterestisacriticalareaofinquiry
Thisarticleisanopenaccessarticle inbothfinancialresearchandpractice. Investmentinterest,orthedegreetowhichindivid-
distributedunderthetermsand
ualsengagewithandaremotivatedtoparticipateininvestmentactivities,isinfluenced
conditionsoftheCreativeCommons
byarangeofbehavioral,attitudinal,educational,andcontextualfactors. Groundedinthe
Attribution(CCBY)license
frameworksofbehavioralfinancetheory[1,2]andprospecttheory[3,4],thisstudyexam-
(https://creativecommons.org/
licenses/by/4.0/). inestheroleofmultiplepredictors,includinginvestmentattitudes,financialeducation,
Electronics2025,14,1505 https://doi.org/10.3390/electronics14081505

Electronics2025,14,1505 2of17
speculativeinvestmentattitudes,resilienceafterfinanciallosses,decisionadaptabilityafter
losses,decision-makingbehaviorsininvestments,andtrustinAI-basedfinancialsystems,
inshapinginvestmentinterest.
Behavioral finance theory provides a foundation for understanding how psycho-
logical factors, including cognitive biases and emotional responses, influence financial
decisions. Itchallengesthetraditional“homoeconomicus”assumptionofrationaldecision
making,emphasizingthesystematicdeviationsfromrationalityobservedinreal-world
investorbehavior[5,6]. Prospecttheorycomplementsthisbyexplaininghowindividuals
perceivegainsandlossesasymmetrically,oftenexhibitingriskaversionforgainsandrisk-
seekingbehaviorforlosses[7]. Thesetheoreticalframeworksareparticularlyrelevantfor
analyzingthecomplexrelationshipsamongbehavioralandattitudinalfactorsininvestment
decisionmaking.
Investmentattitudes—individuals’perceptionsofthebenefits,risks,andim-portance
ofinvesting—arepivotalinshapinginvestmentinterest. Researchhasshownthatpositive
attitudestowardsinvestingcorrelatewithhigherengagementandbetterdecision-making
outcomes[8,9]. Similarly,financialeducationplaysacrucialroleinequippingindividuals
withtheknowledgeandskillsneededtomakeinformedinvestmentdecisions. Studies
highlightthepositiveimpactoffinancialliteracyonbothinvestmentattitudesandperfor-
mance[10,11]. Financiallyeducatedindividualsaremorelikelytounderstandrisks,assess
opportunities,andoptimizereturns.
Speculative investment attitudes reflect a willingness to engage in high-risk, high-
rewardfinancialactivities. Thesetendenciesinfluencethedegreeofinvestmentinterest
shownbyindividuals. Researchsuggeststhatattitudestowardsspeculativeinvestments,
suchascryptocurrenciesorothervolatileassets,areshapedbyfinancialrisktoleranceand
personalvalues[12,13]. Additionally,resilienceinthefaceoffinanciallossesisessential
formaintaininglong-terminvestmentengagement. Studiesonresilienceafterfinancial
lossesdemonstratethatindividualswhoviewlossesasopportunitiesforlearningarebetter
equippedtorecoverandadapt[14,15].
Adaptabilityindecisionmakingfollowingfinancialsetbacksisanothercrucialfac-
tor. Decision adaptability after losses reflects an investor’s ability to revise strategies
basedonpastexperiences,whichisessentialfornavigatingvolatilemarkets[16,17]. This
adaptabilityiscloselylinkedtooveralldecision-makingbehaviorsininvestments,which
includesystematicpracticessuchasportfoliodiversificationandrelianceonexpertadvice.
Priorresearchunderscorestheimportanceofdeliberateandinformeddecisionmakingin
achievingfavorableinvestmentoutcomes[18,19].
Inrecentyears,theintegrationofartificialintelligence(AI)intofinancialsystemshas
introducedanewdimensiontoinvestmentdecisionmaking. TrustinAI-basedfinancial
systems has become a significant determinant of investment interest, as individuals in-
creasinglyrelyonAI-driventoolsforfinancialanalysisandrecommendations. Studies
indicatethattrustinAIsystemsisinfluencedbyperceptionsofreliability,transparency,
andperformance[20,21]. AsAI-enabledplatformsbecomemoreprevalent,understanding
theroleoftrustinshapinguserengagementiscritical[22].
Thisstudybuildsontheexistingliteraturebyintegratingthesediversefactorsintoa
comprehensivemodelofinvestmentinterest. Byemployingdecisiontreeregression,we
aimtoidentifythehierarchicalrelationshipsamongthesepredictorsandprovideactionable
insightsforfinancialeducators,advisors,andpolicymakers. Thefindingscontributetothe
broaderunderstandingofhowbehavioral,educational,andtechnologicalfactorsinteractto
shapeinvestmentbehavior,offeringpracticalimplicationsforimprovingfinancialliteracy
anddecisionmakingindiversepopulations.

Electronics2025,14,1505 3of17
Theprimaryaimofthisstudyistoinvestigatethebehavioral,cognitive,demographic,
andtechnologicalpredictorsofinvestmentinterestusingadata-drivenmodelingapproach.
Specifically,thisresearchappliesdecisiontreeregressiontoidentifythemostinfluential
factorsshapingindividualinvestmentbehaviors. Whilegroundedinbehavioralfinance
theoryandprospecttheory,thisisnotaliteraturereviewbutanempiricalstudybasedona
structuredquestionnaireadministeredtoasampleoffinancialprofessionals. Theresearch
seeksto(1)modelthehierarchyofinfluencesaffectinginvestmentinterest,(2)assessthe
predictive strength of these variables, and (3) offer practical implications for financial
education,advisoryservices,anddigitalinvestmenttools.
Unlikepreviousstudieswhichprimarilyusedlinearmodelssuchaslogisticormulti-
pleregression,thisresearchemploysdecisiontreeregression(DTR)tomodelnon-linear
relationshipsbetweenbehavioralpredictorsandinvestmentinterest. DTRoffersatranspar-
entandinterpretablestructure,whichiscriticalinbehavioralfinance,whereinteractions
amongpsychologicalandcontextualvariablescanbecomplex. Thenoveltyofthisstudy
liesinitsintegrationofDTRwithinthebehavioralfinanceframework,offeringahierar-
chicalviewofhowattitudinal,educational,andtechnologicalfactorscollectivelyshape
investmentbehavior.
LiteratureReview
Investmentdecisionshavelongbeenacentralfocusoffinancialresearch,withavariety
of factors influencing both individual and corporate investment behaviors. The extant
literaturehighlightstheinterplayoffinancial,demographic,behavioral,andcontextual
variablesinshapinginvestmentdecisions,oftenframedwithintheoreticalperspectives
suchasbehavioralfinancetheory[1,6]andprospecttheory[3]. Thissectionsynthesizes
findings across multiple domains to elucidate the determinants of investment interest
andbehavior.
Financialconstraints,marketconditions,andeconomicvariableshaveconsistently
beenfoundtoinfluencecorporateandindividualinvestmentdecisions. Ref.[23]compared
investmentbehaviorsacrossBelgium,France,Germany,andtheUnitedKingdom,finding
thatfinancialconstraintssignificantlylimitcorporateinvestment. Similarly,Ref.[24]ex-
ploredinvestmentdecisionsintransitionalChina,revealingthatfinancialfactors,including
liquidity and cost of capital, are critical determinants. This aligns with earlier findings
by [25], who demonstrated that financial constraints significantly impede firm-level in-
vestment. In individual contexts, Ref. [26] identified liquidity as a key determinant of
investmentchoices,whileRef.[27]highlightedtherelevanceofmacroeconomicconditions.
Theroleoffinancialliteracyandeducationinfacilitatingbetterinvestmentdecisions
isalsowidelyrecognized. Ref.[28]emphasizedthecriticalneedforfinancialeducation
to enhance retirement preparedness and informed decision making. This is supported
by[10],whodemonstratedthepositiveimpactoffinancialliteracyprogramsonhighschool
students’investmentattitudes. Ref.[29]furthercorroboratedthesefindings,notingthat
financiallyliterateinvestorsintheUAEmakemorerationalandinformeddecisions. Such
insightsareechoedby[11],stressingthebroaderimplicationsoffinancialeducationfor
economicstabilityandindividualfinancialwell-being.
Behavioralfinancehasshedalightonhowcognitivebiasesandemotionalfactors
influenceinvestmentdecisions. Ref.[30]identifiedkeybehavioralfactorssuchasovercon-
fidence,lossaversion,andherdbehavioramonginstitutionalinvestorsattheNairobiStock
Exchange. Thesefindingsalignwiththoseof[31],whoexaminedthepsychologicalunder-
pinningsofindividualinvestmentdecisions. Ref.[32]employedtheanalyticalhierarchy
process(AHP)toquantifytheimpactofbehavioralfactors,notingthatriskperceptionand
emotionalstabilitysignificantlyshapeinvestmentbehaviors.

Electronics2025,14,1505 4of17
Prospecttheoryhasbeenparticularlyinfluentialinunderstandingtheasymmetrical
attitudestowardgainsandlosses.Ref.[7]highlightedhowindividualsexhibitriskaversion
inthefaceofgainsbutarewillingtotakegreaterriskstorecoverlosses. Thisdynamicwas
furthersupportedbystudiessuchasthoseby[33,34],whichillustratedhowpastlosses
couldtriggerheightenedrisk-takingbehaviorsamonginvestors.
Demographicvariablessuchasage,income,education,andemploymentstatusalso
playacriticalroleininvestmentdecisions. Ref.[27]demonstratedthatyoungerinvestors
are more likely to engage in high-risk investments, whereas older individuals tend to
prioritizesafetyandstability. Similarly,Ref.[35]foundthatfinancialliteracylevelsand
demographiccharacteristicsjointlyinfluenceinvestmentpreferences,withhigher-income
individualsdemonstratingagreaterpropensityfordiversifiedportfolios. Studiesby[36,37]
furtherconfirmedtheimportanceofdemographicfactorsinshapingfinancialbehaviors,
notingsignificantvariationsbasedongender,income,andeducationalattainment.
Strategicdecision-makingprocessesininvestmentareofteninfluencedbyexternal
andcontextualfactors. Ref.[38]arguedthataligninginvestmentswithbroaderstrategic
goalsenhancestheirperceivedvalue,particularlyinenergyefficiencyinitiatives. Ref.[39]
emphasized the role of contextual factors such as market competition and regulatory
frameworks in shaping strategic investment decisions. Ref. [40] extended this analysis
to cross-border investments, highlighting the impact of finance-specific factors such as
currencystabilityandfinancialintegration.
Recentadvancementsintechnology,particularlyinartificialintelligence(AI),have
transformedthelandscapeofinvestmentdecisionmaking. TrustinAI-enabledfinancial
systemsisemergingasacriticalfactorinshapinginvestorbehavior. Studiesby[20,41]
revealedthatperceptionsofreliabilityandtransparencysignificantlyinfluencetheadoption
ofAI-basedtools.
Financialliteracyandbehavioralbiasesremainpivotalinbothindividualandinsti-
tutionalcontexts,whilestrategicandtechnologicalconsiderationsincreasinglyinfluence
moderninvestmentlandscapes.
Thus,thereviewedliteraturesupportstherelevanceofintegratingbehavioral,demo-
graphic,andeducationalvariablesinunderstandinginvestmentdecisions. Thisliterature
reviewinformedtheconstructionofthesurveyinstrumentsusedinthisstudy. Eachbehav-
ioraldimensionanalyzed—suchasinvestmentattitudes,speculativebehaviors,resilience
afterlosses,andtrustinAI—wasderivedfromconstructsidentifiedasinfluentialinprior
studies. Thisconnectionbetweentheoreticalbackgroundandempiricalinstrumentation
ensuresthestudy’sconceptualcoherence. Empiricalstudieshaveshownthatfinancialedu-
cationsignificantlyshapesinvestmentattitudesandlong-termfinancialdecision-making
behavior. Forexample,Becchettietal.[10]demonstratedthrougharandomizedcontrolled
trial how educational interventions can positively influence students’ financial choices
andattitudestowardinvesting. Thesefindingsreinforcethebehavioralunderpinningsof
investmentinterest,supportingtheintegrationofcognitiveandattitudinalvariablesin
predictivemodeling.
Recentstudieshavedemonstratedtheutilityofdecisiontree-basedmodelsinfinan-
cialbehaviorprediction. Forexample,Sunandcollaboratorsdevelopedadecisiontree
ensemblemethodcombiningSMOTEandbaggingtoaddressclassimbalanceinenterprise
creditevaluation,demonstratingimprovedpredictiveaccuracyandrobustnessincomplex
financialcontexts[22]. Thisapproachunderscorestherelevanceandadaptabilityoftree-
basedalgorithmsinmodelinginvestorbehaviorswheredataimbalanceandnon-linear
interactionsareprevalent.

Electronics2025,14,1505 5of17
2. MaterialsandMethods
2.1. Participants
Thisstudyutilizedaconveniencesamplingmethod,targetingnetworksofeconomists
andfinancialprofessionals. Recruitmentwasconductedprimarilythroughonlineplat-
forms,withaGoogleFormsquestionnairedistributedviaemailandprofessionalsocial
media channels. Participation was voluntary, and all respondents provided informed
consentpriortocompletingthesurvey. Datacollectionwasanonymous,ensuringconfi-
dentialitythroughouttheprocess.
Participantswererecruitedfromprofessionalnetworksandacademicassociations
relatedtoeconomicsandfinance. Eligibilityrequiredabasiclevelofinvestmentexperience
and understanding, ensuring respondents could meaningfully answer questions about
financial behaviors. Prior to survey distribution, an expert panel of three specialists in
behavioralfinanceandpsychometricsreviewedtheitempooltoensureclarity,relevance,
andcontentvalidity. Itemswereadaptedfromvalidatedinstrumentsandrevisedthrough
cognitiveinterviewswithfivepilotparticipants. Thesestepsenhancedthecredibilityand
replicabilityoftheresearchprocess.
A total of 548 participants completed the survey. Regarding gender distribution,
38%ofrespondentsidentifiedasmale(n=208),while62%identifiedasfemale(n=340).
In terms of education level, 21.4% (n = 117) reported having completed high school or
equivalent,40.9%(n=224)heldabachelor’sdegree,31.9%(n=175)hadamaster’sdegree,
and5.8%(n=32)reportedholdingadoctoraldegree.
Participants’ employment status was categorized into four groups: 11.7% (n = 64)
reportedbeingunemployed,4%(n=22)wereemployedpart-time,75%(n=411)were
employedfull-time,and9.3%(n=51)identifiedasfreelancersorself-employed. Income
levelsvaried,with19.3%(n=106)reportingamonthlyincomebelow3000RON,35.6%
(n=195) earning between 3000–5000 RON, 20.1% (n = 110) earning between 5000 and
7000RON,8.9%(n=49)earningbetween7000and9000RON,and16.1%(n=88)earning
above9000RONpermonth.
Participants’ professional experience was distributed as follows: 31.4% (n = 172)
reported less than five years of experience, 33.4% (n = 183) had between five and ten
years,11.5%(n=63)hadtentofifteenyears,and23.7%(n=130)hadoverfifteenyearsof
professionalexperience.
Thisdiversesampleprovidedarobustfoundationforexploringfinancialbehaviors
andattitudesacrossvariousdemographicandprofessionalcontexts. Whileconvenience
samplingallowedrapidaccesstoaspecificprofessionalpopulation,itintroducedpotential
selectionbiasandlimitedthegeneralizabilityofthefindings. Futureresearchshouldaim
forstratifiedorrandomsamplingtoimproverepresentativeness.
Therecruitmentprocessinvolveddistributingthesurveytoover1000individuals
via professional mailing lists, university alumni databases, and finance-related online
communities. From these, 548 responses were received and retained for analysis. The
exclusioncriteriaincludedincompleteresponses.
2.2. Instruments
Toanalyzethefactorsinfluencingfinancialdecisionmaking,asetofrigorouslydevel-
opedscaleswasutilized,eachcomprising7to14items. Theseinstrumentsweredesigned
tomeasurebehavioral,attitudinal,andcognitivedimensionscriticaltoinvestment-related
choices. Thescalesdemonstratedstrongreliability,withCronbach’salphavaluesranging
from0.84to0.93.
Thequestionnaireconsistedof8distinctscalescoveringbehavioral,attitudinal,cogni-
tive,technological,anddemographicdimensions. Eachscaleuseda5-pointLikert-type

Electronics2025,14,1505 6of17
responseformat,rangingfrom1(stronglydisagree)to5(stronglyagree). Higherscores
reflectedstrongeragreementwiththeconstructbeingmeasured.
Investmentinterestcapturedthelevelofengagementindividualsdisplayedtowardfi-
nancialinvestments,encompassingactivitieslikeseekinginformationandstayingupdated
on market trends. For instance, participants responded to items such as the following:
“Howoftendoyouseekinformationaboutfinancialinvestments?”,adaptedfrom[42]. The
scaledisplayedaCronbach’salphaof0.86,reflectinghighinternalconsistency.
Investmentattitudesmeasuredbeliefsaboutthebenefits,risks,andoverallsignifi-
canceofinvesting. Thisconstructwasvitalforunderstandinghowperceptionsinfluence
financialbehavior. Anexampleitemread,“Investingisessentialforlong-termfinancial
security.”,adaptedfrom[43]. ThisscaleachievedaCronbach’salphaof0.91,underscoring
itsreliability.
Financialeducationevaluatedparticipants’understandingoffoundationalfinancial
principles,suchassaving,budgeting,andinvestmentstrategies,andtheirabilitytoapply
thisknowledgeeffectively. Arepresentativeitemwasthefollowing: “Iunderstandthe
conceptofcompoundinterestanditsimpactonsavings.”(adaptedfrom[28]). Thescale
recordedaCronbach’salphaof0.89,indicatingrobustreliability.
Speculativeinvestmentattitudesexaminedindividuals’perceptionsofandengage-
mentwithspeculativeinvestmentoptions,includinghigh-riskassetslikecrypto-currencies.
This construct shed light on risk tolerance and preferences. An example item included
the following: “Speculative investments are a viable way to achieve financial growth.”
(adaptedfrom[4]). ThescaledemonstratedaCronbach’salphaof0.87.
Resilience after financial losses assessed an individual’s emotional and behavioral
recoveryfollowingfinancialsetbacks,reflectingtheirabilitytoregainconfidenceinfuture
investments. One item stated, “I view financial losses as an opportunity to learn and
improvemystrategies.”(adaptedfrom[3]). ThisscalehadaCronbach’salphaof0.84.
Decisionadaptabilityafterlossesmeasuredtheflexibilityindecision-makingstrategies
postloss,capturinghowindividualsrecalibratedtheirapproachtoinvesting. Asample
itemwasthefollowing:“Afterafinancialloss,Ireconsidermyinvestmentstrategytoavoid
repeatingmistakes.”ThescaleyieldedaCronbach’salphaof0.88.
Decision-makingbehaviorsininvestmentsevaluatedthesystematicanddeliberate
approachesindividualsusedwhenmakinginvestmentdecisions,suchasportfoliodiversi-
ficationandrelianceonexpertadvice. Anillustrativeitemwasthefollowing: “Idiversify
myin-vestmentportfoliotomanageriskeffectively.”,adaptedfrom[44]. Thisscalehadthe
highestCronbach’salphaat0.93.
TrustinAI-basedfinancialsystemsexploredconfidenceinautomatedtoolsandsys-
tems using artificial intelligence for financial management. This construct focused on
perceptionsoftechnology’sreliabilityandutility. Arepresentativeitemwasthefollow-
ing: “ItrustAI-basedsystemstoprovideaccuratefinancialrecommendations.”,adapted
from[45]. ThescaleachievedaCronbach’salphaof0.92,confirmingitsreliability.
2.3. Procedure
Theanalysisaimedtoinvestigatethefactorsinfluencinginvestmentinterest,which
wasdesignatedasthedependentvariable. Thepredictorsincludedbehavioral,attitudinal,
anddemographicfactors: investmentattitudes,financialeducation,speculativeinvestment
attitudes,resilienceafterfinanciallosses,decisionadaptabilityafterlosses,decision-making
behaviorsininvestments,trustinAI-basedfinancialsystems,anddemographicvariables
suchasage,gender,education,income,andemploymentstatus.
Thefulllistoffactorsincludedinthemodelisthefollowing:

Electronics2025,14,1505 7of17
• Behavioral/Attitudinal: Investmentattitudes, speculativeinvestmentattitudes,re-
silienceafterfinanciallosses,decision-makingbehaviorsininvestments,anddecision
adaptabilityafterlosses;
• Cognitive: Financialeducation;
• Technological: TrustinAI-basedfinancialsystems;
• Demographic: Age,gender,education,income,employmentstatus,andprofessional
experience.
ThedatawerecollectedviaanonlinequestionnaireandprocessedinJASP(version
0.19.3),anopen-sourcestatisticalsoftware. JASPwaschosenforitseaseofuse,accessibility,
andvisualinterpretabilityoftreestructures,whichalignswiththestudy’sappliedfocus.
However,futurestudiescouldreplicatetheanalysisinPython(scikit-learnversion1.4.1)or
R(rpart,version4.1.23)toallowgreatercontrolovermodeltuningandensemblemethods.
Preliminaryanalysesincludeddescriptivestatisticsandfrequencytablestosummarize
participant characteristics. To model the relationships between the dependent variable
andpredictors,decisiontreeregressionwasemployed. Thismethodwasselectedforits
abilitytohandlecomplex,non-linearrelationshipsandprovideinterpretablehierarchical
structuresintheformofdecisiontrees.
Decision tree regression was trained and tested on the dataset, using a default
80/20split for training and validation purposes. Model evaluation metrics, including
meanabsoluteerror(MAE),meanabsolutepercentageerror(MAPE),andR2,werecal-
culated to assess predictive performance. Given the 5-point Likert scale used for the
dependentvariable,MAPEandR2wereprioritizedasthemostinterpretableperformance
metrics. Featureimportancevalueswerecomputedtodeterminetherelativecontribution
ofeachpredictortothemodel. Hyperparameterssuchasthetree’smaximumdepthand
minimumsamplespersplitweresettodefaultinJASP.Whilethiswasasimplifiedinter-
pretation,itmighthaveincreasedtheriskofoverfittingorunderfitting. Agridsearchor
cross-validationapproachcouldfurtheroptimizeperformanceinfuturestudies.
3. Results
Decisiontreeregressionisanon-parametricsupervisedlearningmethodthatsplits
databasedoninputvariablevaluestopredictcontinuousoutcomes. Thealgorithmre-
cursivelypartitionsthedatasetbyselectingsplitsthatminimizethemeansquarederror
ateachnode. Thisstructurerevealsthehierarchicalimportanceandinteractionsamong
predictors,offeringinterpretableinsightsintocomplexbehavioralpatterns.
Theresultsofthedecisiontreeregressionmodelprovideinsightsintothepredictorsof
investmentinterest. Themodelwastrainedon439casesandtestedon109cases,achieving
a test mean squared error (MSE) of 1.065, a root mean squared error (RMSE) of 1.032,
a mean absolute error (MAE) of 0.8, and a mean absolute percentage error (MAPE) of
172.96%. TheR2valueof0.185indicatedamodestproportionofvarianceintheinvestment
interest explained by the predictors. The dependent variable (investment interest) was
measuredona5-pointLikertscale. Giventhislimitedscalerange,therelativelylowR2
(0.185)andhighMAPEreflectedthecomplex,subjectivenatureofinvestmentinterestand
theinfluenceofunmeasuredlatentvariables. Thegoalofthismodelwas,therefore,not
precisionforecastingbutexploratorypatternrecognitionandpredictorranking. Thus,the
relativelylowR2valuesuggestedthat,whilethemodelcapturedmeaningfulpredictors,
otherlatentorcontextualfactorslikelycontributedtoinvestmentinterest. Thisreflects
theinherentcomplexityoffinancialbehavior,whichisofteninfluencedbynon-observable
psychologicalorsituationalvariables.
Therelativeimportanceofpredictors(Table1)revealedthatinvestmentattitudeswere
themostinfluentialfactor,contributing25.88%tothemodel.Thiswasfollowedbydecision-

Electronics2025,14,1505
8of17
makingbehaviorsininvestments(19.53%)andfinancialeducation(16.69%),highlighting
thesignificantroleofbehavioralandeducationaldimensionsinshapinginvestmentinterest.
Otherimportantpredictorsincludedspeculativeinvestmentattitudes(11.20%),decision
adaptabilityafterlosses(8.27%),andtrustinAI-basedfinancialsystems(6.78%).
Demographicvariablessuchasage(1.94%),experience(1.50%),income(1.09%),edu-
cation(0.39%),andemploymentstatus(0.28%)exhibitedcomparativelylowerim-portance,
suggestingalesserdirectimpactoninvestmentinterestcomparedtobehavioralandattitu-
dinalfactors.
Table1.Featureimportance.
RelativeImportance
Investmentattitudes 25.883
Decision-makingbehaviorsininvestments 19.534
Financialeducation 16.686
Speculativeinvestmentattitudes 11.195
Decisionadaptabilityafterlosses 8.273
TrustinAI-basedfinancialsystems 6.775
Resilienceafterfinanciallosses 6.439
Age 1.940
Experience 1.503
Income 1.094
Education 0.394
Status 0.283
Theprominenceofinvestmentattitudesasthetoppredictorsuggestsastrongpsy-
chologicalbasisforfinancialengagement. Individualswithpositiveattitudesaremore
proactiveinseekingfinancialopportunitiesandshowgreateropennesstousingAI-based
investmenttools,especiallywhentrustintechnologyispresent.
Decisiontreeregressionrevealedahierarchicalstructureofpredictors,withthemost
significantsplitsoccurringatvariouslevelsofthetree(Table2).
Table2.Splitsintree.
|                     | Obs. inSplit | SplitPoint | Improvement |
| ------------------- | ------------ | ---------- | ----------- |
| Investmentattitudes | 439          | −0.411     | 0.160       |
−2.020
| Investmentattitudes                   | 142 |        | 0.191 |
| ------------------------------------- | --- | ------ | ----- |
| Speculativeinvestmentattitudes        | 132 | −0.249 | 0.165 |
| Experience                            | 73  | 1.072  | 0.122 |
| Decision-makingbehaviorsininvestments | 48  | −0.240 | 0.231 |
| Decision-makingbehaviorsininvestments | 25  | −0.392 | 0.314 |
| Financialeducation                    | 297 | 1.858  | 0.136 |
| Decision-makingbehaviorsininvestments | 282 | −0.392 | 0.113 |
| Resilienceafterfinanciallosses        | 75  | 0.267  | 0.102 |
| Speculativeinvestmentattitudes        | 22  | −0.249 | 0.286 |
| Financialeducation                    | 207 | 0.373  | 0.062 |
−0.811
| Resilienceafterfinanciallosses  | 100 |        | 0.112 |
| ------------------------------- | --- | ------ | ----- |
| TrustinAI-basedfinancialsystems | 89  | −0.215 | 0.124 |
| TrustinAI-basedfinancialsystems | 27  | −0.568 | 0.337 |
Note.Foreachlevelofthetree,onlythesplitwiththehighestimprovementindevianceisshown.
Table2presentsthemostrelevantdecisiontreesplits,where“Obs. inSplit”indicates
the number of observations at the node being split, “Split Point” represents the value
of the predictor at which the split occurs, and “Improvement” reflects the reduction in

Electronics 2025, 14, x FOR PEER REVIEW 9 of 17
Electronics2025,14,1505 Table 2 presents the most relevant decision tree splits, where “Obs. in Split” indi 9 c o a f t 1 e 7 s
the number of observations at the node being split, “Split Point” represents the value of
the predictor at which the split occurs, and “Improvement” reflects the reduction in model
mdeovdiealndceev (iaa npcreox(ay pforor xpyrefodricptiroend iecrtiroonr)e; rhriogrh);ehr iigmhperroimvepmroevnetm vaenlutevsa ilnudesiciantde isctartoensgtreorn pgreer-
pdriecdtiivceti vcoenctornibturitbiounti oant tahtatth saptescpifiecci filecvleelv oefl tohfet htreeter.e e.
TThhee fifirrsstts pspliltitw wasasb absaesdedon oinn vinesvtemstemnteanttt iatuttditeusd,ewsh, iwchhiecmh eermgeedrgaesdth aesm thoes tminoflsut einnfltiual-
veanrtiiaabl lvea.rAiatbales. pAlitt ap sopinlitt pofoi−n0t .o4f1 −10,.t4h1i1s, ftahcitso frapctroorv pidreodviadnedim anp riomvpermoevnemtoefn0t .o16f 00.i1n60th ien
mthoed melo,demel,p ehmaspizhiansgiziitnsgfo iutsn fdoautniodnaatlioronlael irnolper eind ipcrtiendgicitninvges itnmveensttminetnert eisntt.eAressut. bAse squubesnet-
sqpuleitnwt sitphliint wthiethsianm theev saarmiabe lve,aarita−bl2e.,0 a2t0 −,2y.i0e2ld0,e dyiaelndeevde anng erveaetne rgrimeapterro vimempreonvteomfe0n.1t9 o1f,
f0u.1rt9h1e, rfuhrigthhelrig hhitginhgligithsticnegn tirtas lciemnptroarl tiamncpeo.rtance.
TThhee nneexxtt ccrriittiiccaall sspplliitt iinnvvoollvveedds sppeeccuulalattiviveei ninvveesstmtmeenntta attttitiutuddeess,,o occccuurrrirningga att− −00..224499
aanndd ccoonntrtribibuutitningga nanim imprporvoevmemenetnotf o0f. 106.51.6T5.h iTshiinsd iincadtiecsattehsa tthinadt iivniddiuvaildsu’palesr’c eppetricoenpstiaonnds
eanngda genemgaegnetmweintht wspiethcu slpaeticvuelaintivvees timnveensttsmaernetasl saorek aeylsod rkiveyer dsroifvtehrse iorfi nthteeriers itnitnerfiensat ninc iafil-
innavnecsitaml iennvtes.stAmneontthse. rAsnigonthifierc asnigtnsipfilciatnwt asspolibt swearvs eodbsweritvhedex wpietrhi eenxcpee,raietnacpe,o aint tao pfo1i.n0t7 o2f,
w1.h0i7c2h, wprhoivcihd epdroavnidimedp aronv iemmpernotvoefm0e.1n2t2 o,fs u0.g1g2e2s, tsinugggthesattinpgro tfheasst ipornoafleesxsipoenraiel necxepperlaieynscae
spulpaypso art isvuepbpuotrtsievceo bnudta sreycroonledainrys hroalpei ning sihnavpesintmg einnvtebsethmaevniot rb.ehavior.
DDeecciissiioonn--mmaakkiinngg bbeehhaavviioorrss iinn iinnvveessttmmeennttss aallssoo aappppeeaarreedd pprroommiinneennttllyy iinn tthhee ttrreeee
ssttrruuccttuurree,, wwiitthh sspplliittss aatt− −00..224400 aanndd −−00..339922,, pprroovviiddiinngg iimmpprroovveemmeennttss ooff 00..223311 aanndd 00..331144,,
rreessppeeccttiivveellyy..T Thheesesefi finnddinignsgsu nudnedresrcsocroerteh tehiem ipmoprtoarntacencoef soyf sstyemsteamticaatincd adnedl idbeelriabteeriantve eisnt--
mveesntmtpernatc tpircaecst.iSceims. iSlaimrlyil,afirnlya,n ficniaalnecdiaulc eadtiuocnatsipolnit sspaltitpso aitn tpsosiunctsh sausc1h. 8a5s8 1a.8n5d8 0a.n37d3 0c.3o7n3-
tcroibnutrteibduitmedp riomvpermoevnetmseonft0s. 1o3f6 0a.1n3d6 0a.n06d2 0,.i0n6d2i,c aintidnigcathtiantgfi tnhaant cfiianlaknncoiawl lkendogwelseigdngiefi sciagnntilfy-
cicoamnptllye mcoemntpsleomtheenrtbse ohtahveiro braelhfaavcitoorrasl. factors.
OOtthheerr pprreeddicictotorrss,,s suucchha assr erseisliileinecnecea fateftrefir nfiannacniaclialol slosessseasn adntdru tsrtuisnt AinI -AbIa-sbeadsefidn afinncaianl-
scyiastl esmyss,tesmhosw, eshdoiwnfleude nincfleuinenlocwe einr- lleovwelesrp-lleitvse,lw sipthlitrse,s pweictthiv reeismpepcrtoivveem imenptsroovfe0m.1e1n2tasn odf
00..112142. aTnhde i0r.r1o2l4e.s T,thheoiru grohleless, sthporuomghi nleesnst ,psruogmgeinsetendt, nsuuagngceesdtecdo nnutraibnucetido ncsontotrtihbuetoiovnersa tlol
mthoed oevl.eNraollt ambolyd,eal.s Nploittainbltyr,u as tsipnliAt iIn-b tarsuesdt fiinn AanIc-biaalsseyds tfienmanscaita − l s0y.5st6e8mlesd att o−0th.5e6h8 ilgehde stot
itmhep rhoivgehmesetn itmaptrthoviselmeveenlt, wati tthhias vleavlueel, owfi0t.h3 3a7 ,vhailguhel iogfh 0ti.3n3g7t,h heigemhleigrghitninggs itghnei fiemcaenrcgeinogf
tseicghnnifiocloagniccea lotfr tuescthinnofilongainccaila tlrcuosnt tienx fitsn.ancial contexts.
OOvveerraallll,, tthhee ttrreeee ssttrruuccttuurree hhiigghhlliigghhttss tthhee ddoommiinnaanntt rroollee ooff bbeehhaavviioorraall aanndd aattttiittuuddiinnaall
ffaaccttoorrss,, wwiitthh ddeemmooggrraapphhiicc vvaarriiaabblleess ccoonnttrriibbuuttiinngg mmoorree ssuubbttllyy ttoo tthhee pprreeddiiccttiioonn ooff iinnvveesstt--
mmeenntt iinntteerreesstt.. TThheesseer reessuultlstso offffeerra ac ocommpprerhehenesnisvievev iveiwewo fohf ohwowd idffieffreernetnptr pedreicdtiocrtsorins tienrtaecrt-
aancdt acnodn tcroibnutrtiebhuiteer hariecrhaicrcahlliycatollyfi ntoa nficniaanlcdieacl idsieocnismioank minagk(iFnigg u(Frieg1u)r.e 1).
Figure1.Predictiveperformanceplot.
Figure 1. Predictive performance plot.
Figure1illustratesthepredictiveperformanceofthedecisiontreeregressionmodel,
visualizing the relationship between observed and predicted values of the dependent
variable, investmentinterest. Theplotprovidesanassessmentofthemodel’sabilityto
accuratelypredictthelevelsofinvestmentinterestbasedontheidentifiedpredictors.

Electronics 2025, 14, x FOR PEER REVIEW 10 of 17
Figure 1 illustrates the predictive performance of the decision tree regression model,
visualizing the relationship between observed and predicted values of the dependent var-
iable, investment interest. The plot provides an assessment of the model’s ability to accu-
rately predict the levels of investment interest based on the identified predictors.
Electronics2025,14,1505 10of17
The scatterplot reveals a clustering of points around the diagonal line, which repre-
sents perfect prediction. While there is some dispersion, particularly at extreme values,
Thescatterplotrevealsaclusteringofpointsaroundthediagonalline,whichrepresents
the general alignment of data points with the diagonal indicates that the model captures
perfect prediction. While there is some dispersion, particularly at extreme values, the
the overall trend effectively. This is consistent with the model’s performance metrics, in-
generalalignmentofdatapointswiththediagonalindicatesthatthemodelcapturesthe
cluding a test mean squared error (MSE) of 1.065 and a root mean squared error (RMSE)
overalltrendeffectively. Thisisconsistentwiththemodel’sperformancemetrics,including
of 1.032, which reflect a reasonable level of predictive accuracy. However, the modest R2
atestmeansquarederror(MSE)of1.065andarootmeansquarederror(RMSE)of1.032,
va
w
lu
h
e
i c
o
h
f 0
re
.1 fl
8
e
5
c t
su
a
g
re
g
a
e
s
s
o
ts
n a
th
bl
a
e
t,
l e
w
v
h
el
il
o
e
f
th
p
e
re
m
di
o
ct
d
iv
e
e
l i
a
d
c
e
c
n
u
t
r
i
a
fi
c
e
y
s
.
k
H
e
o
y
w
p
e
r
v
e
e
d
r,
ic
t
t
h
o
e
rs
m
, a
o
d
de
d
s
i
t
ti
R
o2na
v
l
a
u
lu
n
e
meas-
ured factors may contribute to unexplained variance.
of0.185suggeststhat,whilethemodelidentifieskeypredictors,additionalunmeasured
facTtohres mdeacyiscioonnt rtirbeuet eptlootu (nFeixgpulraein 2e)d ilvlaursitarnactee.s the hierarchical structure of the regression
model Tuhseedd etcoi spiornedtriecet pinlovte(sFtimguernet2 i)niltleursetsrat,t ehsigthhelihgihertainrcgh itchael ssteruqcuteunretioafl tihmepreogrrteasnsicoen of the
premdoicdteolruss. eTdhteo rporoedt incotidnev eidstemnetinfiteins tienrvesets,thmigehnltig ahtttiintugdthees saesq tuheen tmiaolsimt spiogrntaifinccaenotf vthaeriable,
splpirtteidnigct othrse. dThaetarsoeott anto ad eviadleunet iofife s−0in.4v1e1st.m Tehnits actotintufidremssa sththaet minovsetsstimgneinfitc aantttivtuardiaebs lae,re the
splittingthedatasetatavalueof−0.411. Thisconfirmsthatinvestmentattitudesarethe
strongest driver of investment interest, as indicated in the feature importance analysis.
strongest driver of investment interest, as indicated in the feature importance analysis.
For individuals with lower investment attitudes (<−0.411), further splits occur at −2.02
Forindividualswithlowerinvestmentattitudes(<−0.411),furthersplitsoccurat−2.02
within the same variable, underscoring its critical role. Subsequent splits in this branch
withinthesamevariable,underscoringitscriticalrole. Subsequentsplitsinthisbranchare
are determined by speculative investment attitudes (<−0.249), followed by experience
determinedbyspeculativeinvestmentattitudes(<−0.249),followedbyexperience(<1.07)
(<1.07) and decision-making behaviors in investments, which refine the prediction for in-
anddecision-makingbehaviorsininvestments,whichrefinethepredictionforindividuals
divwidithuanlesg watiitvhe noregloawtivaett iotur dloeswto awttaitruddinevs etsotwmeanrdts .investments.
FigFuigreu r2e. 2D.eDceicsiisoinon trtereee pplloott..
Forindividualswithhigherinvestmentattitudes(≥−0.411),thenextsignificantsplit
For individuals with higher investment attitudes (≥−0.411), the next significant split
isbasedonfinancialeducation(<1.86),demonstratingtheroleoffinancialknowledgein
is based on financial education (<1.86), demonstrating the role of financial knowledge in
distinguishinglevelsofinvestmentinterestamongthisgroup. Thetreefurtherbranches
distinguishing levels of investment interest among this group. The tree further branches
onvariablessuchasdecision-makingbehaviorsininvestments(<−0.392),resilienceafter
on
fi
v
n
a
a
r
n
i
c
a
i
b
a
l
l
e
l
s
o s
s
s
u
es
ch
(<
a
0
s
.2 d
67
e
)
c
,
i
a
s
n
io
d
n
s
-
p
m
ec
a
u
k
l
i
a
n
t
g
iv e
be
in
h
v
a
e
v
s
i
t
o
m
r
e
s
n
i
t
n
a t
in
tit
v
u
e
d
s
e
tm
s(
e
<
n−t
0
s
.2 (<
4
−
9)
0
.
.3 D
9
e
2
e
)
p
,
e
r
r
e
s
s
p
il
l
i
i
e
ts
n
i
c
n
e after
fintahnecriiaglh ltossusbetsr e(e<0a.l2so67in),c laundde strpuesctuinlaAtiIv-bea isnevdefisntmanecniat lasttysittuemdes,s r(e<fl−e0c.t2in4g9)t.h Deeemepeergr inspglits in
ther erliegvhatn cseuboftrteeech anlosloo giniccallutdrues ttriunsfit ninan AciIa-lbdaesceidsi ofinn-manackiianlg scyosntetemxtss,. reflecting the emerging
relevanTchee otfe rtmecihnnalonloodgeicsarle tprruesset nint pfirnedainccteiadl ldeveeclissioofnin-mveasktminegn tcionnteterexstts,.w itheachnode
displayingthepredictedscoreandthenumberofobservations(n)inthatsubset. These

Electronics2025,14,1505 11of17
terminal nodes provide insights into the segmentation of participants based on their
characteristicsandpredictors. Thetreedemonstratesthatinvestmentattitudesplayafoun-
dationalrole,withvariablessuchasfinancialeducation,speculativeinvestmentattitudes,
anddecision-makingbehaviorsactingascriticalsecondaryinfluences. Otherfactors,like
resilienceafterfinanciallossesandtrustinAI-basedfinancialsystems,contributemore
nuancedeffectsatdeeperlevelsofthetree.
Althoughthefulldecisiontreeincludesmultiplelevelsofsplits,thisdepthreflects
thecomplexityofinteractionsamongbehavioralanddemographicpredictors. Thedeeper
branchescapturecomplexdecisionpathwaysthatmayapplytospecificinvestorprofiles,
whiletheupperlevelshighlightthemostinfluentialvariablesoverall. Thisstructureallows
forbothgeneralanddetailedinterpretationofinvestmentinterestsegmentation.
4. Discussion
The findings of this study highlight the complex nature of investment decisions,
underscoringtheinterplaybetweenbehavioral,financial,demographic,andtechnological
factors.Theseresultsalignwithandexpandupontheexistingliterature,offeringsignificant
implicationsforinvestors,policymakers,andfinancialinstitutions.
Thedominanceofbehavioralfactors,suchasinvestmentattitudes,decision-making
behaviors,andspeculativeinvestmentattitudes,reflectsthecriticalroleofpsychologyin
financialdecisionmaking. Behavioralbiases,suchasoverconfidenceandlossaversion,
influencehowindividualsperceiveandrespondtoinvestmentopportunities,assupported
by[46]. Thesefindingsareconsistentwithbehavioralfinancetheory[1,6],whichposits
thatpsychologicalinfluencesoftenoverriderationalfinancialanalysis. Theresultsalso
highlight generational differences, as younger investors, particularly from Generation
Y,exhibithigherengagementinspeculativeinvestments[46]. Thishasimplicationsfor
financial education programs tailored to specific demographic groups, as emphasized
by[35,47].
Theobservedinfluenceofdemographicfactors,suchasincome,education,andem-
ploymentstatus,corroboratesearlierstudiesthatemphasizetheirimportanceinshaping
investment preferences. For instance, Refs. [48,49] highlight how macroeconomic and
socio-economicfactorsinfluenceindividualinvestmentbehaviorindevelopingeconomies.
Furthermore,theinterplaybetweenfinancialliteracyanddemographicvariables,asdemon-
stratedby[10,11],underscorestheneedfortargetedfinancialliteracyinitiativestobridge
gapsininvestmentknowledgeandparticipation.
Thefindingsdemonstratetheimportanceoffinancialeducationinfosteringinformed
investment decisions, aligning with studies by [28,50]. Financially educated individu-
als are better equipped to evaluate risks and returns, enhancing their decision-making
processes. These results hold strategic implications for policymakers and educational
institutions, particularly in designing programs to enhance financial literacy. Ref. [47]
emphasizesthatfinancialliteracyindevelopingeconomiesiscriticaltoimprovinginvest-
mentoutcomes,whichisespeciallypertinentforemergingmarketslikePakistanandother
developingregions.
Theroleofstrategicinvestmentdecisionmaking,ashighlightedinthisstudy,aligns
withfindingsfrom[51,52],underscoringtheimportanceofnon-financialdriversinstrategic
contexts,suchasrenewableenergyandnuclearsectors. Theseinsightsextendtoindividual
investors,wherealignmentwithlong-termstrategicgoalscanimprovedecisionoutcomes.
Additionally,thisstudyconfirmstherelevanceofcontextualfactorsinshapinginvestment
behavior,consistentwithfindingsby[53]onrealestateinvestmentsand[54]onforeign
directinvestment. Advancedanalyticalmethods,suchasfuzzyclusteringanddecisiontree
modeling,havebeenshowntoprovidevaluableinsightsintocomplexdecision-makingpro-

Electronics2025,14,1505 12of17
cesses,highlightingtheirpotentialapplicationinunderstandingfinancialbehaviors[55,56].
Recentadvancementsinmachinelearninganddecisiontreemethodologies,suchassplit
differenceweightingandself-awarepredictionmodels,offerpromisingsolutionsforad-
dressingimbalancesandimprovinginvestmentrecommendations[57,58]. Also,techniques
suchasfuzzy-payoffmethodsandmulti-perioddecisiontreeshavedemonstratedsignifi-
cantutilityinevaluatingsustainableinvestmentopportunities,bridgingbehavioraland
strategicconsiderations[56,59].
ThegrowingsignificanceoftrustinAI-basedfinancialsystemsobservedinthisstudy
reflects the increasing reliance on technology for investment decision making. These
findings are consistent with the recent literature, such as [20], highlighting the role of
transparency and reliability in fostering trust in AI systems. As financial technologies
continue to evolve, financial institutions must prioritize user trust through transparent
anduser-friendlyAIsolutions. Thisisparticularlyimportantinthepost-pandemicera,
wheredigitalsolutionsarereshapingtraditionalinvestmentprocesses[53]. Theadoption
ofadvancedclusteringanalysesinmanagementandaccountingpracticesfurtherillustrates
thepotentialforenhancinginvestorprofilingandservicecustomization[60].
Theseinsightsarevaluableforfinancialadvisorsseekingtopersonalizeinvestmentrec-
ommendations. Behavioralsegmentationmodelscanhelpfinancialserviceprovidersadapt
theirapproachestorisk-tolerantversusrisk-averseclients. Moreover,educationprograms
shouldprioritizenotonlygeneralfinancialliteracybutalsopsychologicalpreparedness
forspeculativeenvironments,helpingindividualsdevelopresilienceandadaptability. For
researchers,thehierarchicalmodelingprovidedbydecisiontreesoffersanalternativeto
linearapproaches,capturingnon-linearandinteractiveeffectsoftenmissedintraditional
econometricanalyses.
Comparedtotraditionallinearmodels,decisiontreeregressionoffersinterpretability
andnon-linearitybutmaylackrobustnessinhigh-dimensionaldata.Futureresearchshould
exploreensemblemodelslikerandomforestsorXGBoost,whichofferbettergeneralization.
Additionally,Bayesianordeeplearningmethodscouldprovidemorenuancedmodelingof
investoruncertainty.
The integration of AI and other digital tools in financial decision making presents
both opportunities and challenges. While AI-based systems can provide accurate and
data-driven insights, they must also address concerns about data security and ethical
decisionmaking,assuggestedby[41]. Thesefindingsunderscoretheneedforregulatory
frameworks to govern the use of AI in finance, ensuring both trust and accountability.
Additionally,theintegrationofemotionalandbehavioralinsightsintoAI-basedsystems,
such as those examining the role of trust and friendship in information-sharing behav-
iors[61],highlightstheimportanceofuser-centricapproachesinfosteringengagement
andtrustinfinancialtechnologies. TrustinAIisnotonlyaboutsystemperformancebut
alsoethicalandemotionalconsiderations. AsPelauandcollaboratorsnote,perceptionsof
“friendship”andemotionaltrustinAIsystemssignificantlyaffectinformation-sharingand
engagement[61]. FinancialAItoolsmustthereforeaddressemotionalUXdesignalongside
accuracy.
Theroleoftechnologicaladvancements,includingcloudcomputingservices[62]and
riskmanagementsystemsforsustainabledevelopment[63],furtherillustratesthetransfor-
mativepotentialofAIinaddressinginvestmentcomplexities. Similarly,considerationsof
cryptocurrency’simpactonaccountingpractices[64]andsustainability-focusedbusiness
models [65] underscore the need for aligning technological innovations with evolving
marketdemands.
Theresultsofthisstudyholdbroaderimplicationsforpolicymakersandpractitioners.
Fordevelopingeconomies,suchasthosediscussedby[48,66],improvingfinancialliteracy

Electronics2025,14,1505 13of17
and access to financial services can significantly enhance investment participation and
outcomes. Policymakersshouldconsiderimplementingtargetedinterventions,suchastax
incentivesforinvestmentinfinancialeducationprograms,toaddressgapsinliteracyand
participation.
Forfinancialinstitutions,understandingthebehavioralanddemographicnuancesof
investorscaninformthedesignofpersonalizedinvestmentproductsandadvisoryservices.
ByleveragingAIandbigdataanalytics,institutionscantailorsolutionstomeettheneedsof
diverseinvestorprofiles,ashighlightedby[20]. Furthermore,theintegrationofbehavioral
insightsintofinancialadvisoryservicescanimproveengagementanddecisionmaking,as
emphasizedby[52,67].
Policymakerscanapplythesefindingsbyintegratingbehavioralsegmentationinto
public financial literacy campaigns, tailoring messages to match investor profiles (e.g.,
speculativevs. risk-averse). FinancialinstitutionscanuseDTR-basedprofilestocustomize
robo-advisorysystemsandalignproductofferingswithbehavioralpredictors.
5. Conclusions
Futureresearchshouldexplorecomplementarymodelingapproachestodeepenthe
insights obtained from behavioral predictors. In particular, the analytic hierarchy pro-
cess(AHP)andfuzzylogicrepresentvaluablemethodsformulti-criteriadecisionmak-
ing under uncertainty. AHP facilitates pairwise comparisons and priority rankings of
investment-relatedcriteria,enablingresearcherstoassesstrade-offsbetweenrisk,return,
andpsychologicalcomfort[68]. Similarly,fuzzylogicmodelstheimprecisioninherentin
humanjudgment,capturingthedegreesofinvestorpreferencesandbeliefsinaflexible
manner[69]. Thesetechniqueswouldallowforamoresystematicevaluationofinvestor
decision patterns and could be used in combination with machine learning models for
enhancedhybridapproaches. Exploringthesemethodsmayalsoprovideastrongerfoun-
dationforpersonalizedfinancialadvisorytools.
Thisstudyprovidesexploratoryinsightsintothefactorsassociatedwithinvestment
interest,emphasizingthepotentialofintegratingbehavioral,educational,andtechnolog-
icalvariablesintopredictivemodelingframeworks. Theresultstentativelysuggestthat
behavioralfactors,particularlyinvestmentattitudesanddecision-makingbehaviors,may
playamorepronouncedrolecomparedtotraditionaldemographics,thoughfurthervali-
dationisneeded. Additionally,thisstudyhighlightsthegrowingsignificanceoffinancial
literacyandAI-driventechnologiesinshapinginvestmentstrategies,reinforcingtheneed
foradaptivefinancialeducationandpersonalizedadvisoryservices.
Althoughthisstudycontributedvaluableinsights,ithadseverallimitations. First,the
relianceonself-reporteddatamighthaveintroduceresponsebiases,namelysocialdesirabil-
ityorrecallbias,asindividuals’statedinvestmentbehaviorsmaynotfullyalignwiththeir
actualfinancialdecisions. Futurestudiesshouldconsiderintegratingobjectivefinancial
dataorexperimentalmethodologiestomitigatethislimitation. Second,thestudy’ssample
wasnon-randomand,thus,limitedinscope,potentiallyrestrictingthegeneralizabilityof
thefindingstootherregionsorinvestorgroups. Theuseofasinglepredictivealgorithm
mighthavealsoconstrainedthestudy’sbroaderapplicability. Expandingthedatasetto
includeamorediversepopulationacrossdifferenteconomicbackgroundsandinvestment
environmentswouldenhancetherobustnessoftheconclusions. Finally,whiledecision
treeregressionprovidedvaluableinsightsintopredictiverelationships,thisstudydoes
notaccountforpotentialinteractionsbetweenvariables. Futureresearchcouldemploy
ensemblemodelsordeeplearningtechniquestocapturemorecomplexdecision-making
patterns.

Electronics2025,14,1505 14of17
Theresultshavesignificantimplicationsforpolicymakers,financialinstitutions,and
investors. Forpolicymakers,thefindingsemphasizetheneedfortargetedfinancialliter-
acyprograms,particularlyforyoungerinvestorsandindividualswithlimitedfinancial
education. Governmentscouldimplementincentive-driveninitiativestopromotefinan-
cialawarenessandresponsibleinvestmentbehaviors. Financialinstitutions,ontheother
hand, should leverage behavioral insights to design personalized investment products
and AI-driven advisory services that account for cognitive biases and risk perceptions.
Theincreasingroleoftechnologyininvestmentdecisionssuggeststhatinstitutionsmust
prioritize transparency, trust, and ethical considerations in AI-powered financial tools.
Additionally,thisstudyreinforcestheimportanceofintegratingbehavioralfinanceprin-
ciplesintotraditionalinvestmentstrategies,offeringamorecomprehensiveapproachto
understandingmarketbehavior.
Additionalworkcouldtestensemblelearningmethodsorapplythecurrentmethodol-
ogyincross-culturalsettingstoexaminehowinvestmentpredictorsvaryacrosseconomic
systems. A hybrid approach that integrates behavioral scoring with machine learning
couldalsoenhancereal-timefinancialadvisingsystems. Futureresearchshouldexplore
thedynamicinterplaybetweenbehavioral,technological,andfinancialfactorsindiffer-
ent economic and cultural contexts. Specifically, longitudinal studies could provide a
deeperunderstandingofhowinvestorbehaviorsevolveovertimeinresponsetomarket
fluctuationsandfinancialeducationinitiatives. Additionally, examiningsector-specific
investmentbehaviors—suchasinsustainablefinance,cryptocurrency,orrealestate—could
offermoretailoredinsightsintodecision-makingprocesses. Furtherresearchshouldalso
investigate the ethical and regulatory challenges associated with AI-driven investment
platforms,particularlyinensuringfairness,privacy,anddatasecurity. Lastly,interdisci-
plinary approaches combining behavioral finance, machine learning, and neuroscience
couldprovidegroundbreakingperspectivesonhowemotionsandcognitivebiasesshape
financialdecisionmaking.
Building on these exploratory results, future research should adopt longitudinal
designs to track changes in investment behavior over time and across economic cycles.
Applyingmoreadvancedalgorithms—suchasrandomforests,gradientboosting,anddeep
learningnetworks—couldimprovepredictionaccuracy.Cross-nationalcomparisonswould
alsobevaluableinexamininghowculturalandinstitutionalcontextsshapeinvestment
attitudes. Lastly,integratingbehavioraldatawithrealfinancialbehavior(e.g.,transaction
records)couldenhancetheecologicalvalidityofpredictivemodels.
Inconclusion,thisstudyadvancesthefieldofinvestmentdecisionmakingbyintegrat-
ingmultipledimensionsoffinancialbehavior.Thefindingscallforamoreholisticapproach
toinvestmentstrategies,combiningbehavioralinsightswithtechnologicaladvancements
to enhance decision-making efficiency and financial well-being. Ongoing research and
innovationinfinancialliteracy,AI-drivenadvisorysystems,andregulatoryframeworks
willbecrucialinshapingthefutureofinvestmentpracticesinanincreasinglydigitaland
complexfinanciallandscape.
AuthorContributions:Conceptualization,D.R.,L.D.C.andG.C.;methodology,L.D.C.,B.C.G.,L.M.
andD.R.;software,D.R.,B.C.G.,S.R.andR.S.B.;validation,G.C.,S.R.andM.S.;formalanalysis,
L.D.C.,D.R.andF.S.B.;investigation,B.C.G.,S.R.andM.S.;resources,L.D.C.,L.M.andF.S.B.;data
curation,G.C.,R.S.B.andB.C.G.;writing—originaldraftpreparation,L.D.C.,D.R.andL.M.;writing—
reviewandediting,D.R.,G.C.andF.S.B.;visualization,G.C.,S.R.andR.S.B.;supervision,D.R.,L.D.C.
andG.C.;projectadministration,L.D.C.,D.R.andF.S.B.;andfundingacquisition,B.C.G.,S.R.and
F.S.B.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.

Electronics2025,14,1505 15of17
InstitutionalReviewBoardStatement:ThisstudywasconductedinaccordancewiththeDeclaration
ofHelsinkiandapprovedbytheCentreforEconomicResearchandConsultancyofAurelVlaicu
UniversityofArad(protocolcode15/5April2023).
InformedConsentStatement: Informedconsentwasobtainedfromallthesubjectsinvolvedin
thisstudy.
DataAvailabilityStatement:Thedatasupportingourfindingscanbeprovidedbythecorresponding
authoruponreasonablerequest.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Brooks,M.;Byrne,A.BehavioralFinance:TheoriesandEvidence;TheResearchFoundationofCFAInstitute:Charlottesville,VA,
USA;UniversityofEdinburgh:Edinburgh,UK,2008.
2. Fromlet,H.Behavioralfinance-theoryandpracticalapplication:Systematicanalysisofdeparturesfromthehomooeconomicus
paradigmareessentialforrealisticfinancialresearchandanalysis.Bus.Econ.2001,36,63–69.
3. Kahneman,D.;Tversky,A.Prospecttheory: Ananalysisofdecisionunderrisk. InHandbookoftheFundamentalsofFinancial
DecisionMaking:PartI;WorldScientific:Singapore,2013;pp.99–127.
4. Barberis,N.Thirtyyearsofprospecttheoryineconomics:Areviewandassessment.J.Econ.Perspect.2013,27,173–196.[CrossRef]
5. Ritter,J.R.Behavioralfinance.Pac.BasinFinanc.J.2003,11,429–437.[CrossRef]
6. Shiller,R.J.Fromefficientmarketstheorytobehavioralfinance.J.Econ.Perspect.2003,17,83–104.[CrossRef]
7. Tversky,A.;Kahneman,D.Advancesinprospecttheory:Cumulativerepresentationofuncertainty.J.RiskUncertain.1992,5,
297–323.[CrossRef]
8. Lease,R.C.;Lewellen,W.G.;Schlarbaum,G.G.Theindividualinvestor: Attributesandattitudes. J.Financ. 1974,29,413–433.
[CrossRef]
9. Aram, J.D.Attitudesandbehaviorsofinformalinvestorstowardearly-stageinvestments, technology-basedventures, and
coinvestors.J.Bus.Ventur.1989,4,333–347.[CrossRef]
10. Becchetti,L.;Caiazza,S.;Coviello,D.Financialeducationandinvestmentattitudesinhighschools:Evidencefromarandomized
experiment.Appl.Financ.Econ.2013,23,817–836.[CrossRef]
11. Lusardi,A.Financialliteracyandtheneedforfinancialeducation:Evidenceandimplications.SwissJ.Econ.Stat.2019,155,1.
[CrossRef]
12. Arthur, J.N.; Williams, R.J.; Delfabbro, P.H. The conceptual and empirical relationship between gambling, investing, and
speculation.J.Behav.Addict.2016,5,580–591.[CrossRef]
13. Keller,C.;Siegrist,M.Investinginstocks:Theinfluenceoffinancialriskattitudeandvalues-relatedmoneyandstockmarket
attitudes.J.Econ.Psychol.2006,27,285–303.[CrossRef]
14. Tomasic,R.;Akinbami,F.Theroleoftrustinmaintainingtheresilienceoffinancialmarkets.J.Corp.Law.Stud.2011,11,369–394.
[CrossRef]
15. Clarvis,M.H.;Bohensky,E.;Yarime,M.Canresiliencethinkinginformresilienceinvestments?Learningfromresilienceprinciples
fordisasterriskreduction.Sustainability2015,7,9048–9066.[CrossRef]
16. Lee,K.M.C.;Kraussl,R.G.W.;Lucas,A.;Paas,L.J.Adynamicmodelofinvestordecision-making:Howadaptationtolossesaffects
futuresellingdecisions.SSRNElectron.J.2008.Availableonline:https://www.econstor.eu/bitstream/10419/87082/1/08-112.pdf
(accessedon22January2025).
17. Monin,P.Onadynamicadaptationofthedistributionbuilderapproachtoinvestmentdecisions.Quant.Financ.2014,14,749–760.
[CrossRef]
18. Lucey,B.M.;Dowling,M.Theroleoffeelingsininvestordecision-making.J.Econ.Surv.2005,19,211–237.[CrossRef]
19. Renneboog,L.;TerHorst,J.;Zhang,C.Sociallyresponsibleinvestments:Institutionalaspects,performance,andinvestorbehavior.
J.Bank.Financ.2008,32,1723–1742.[CrossRef]
20. Maier,T.;Menold,J.;McComb,C.TherelationshipbetweenperformanceandtrustinAIine-finance.Front.Artif.Intell.2022,5,
891529.[CrossRef]
21. Schreibelmayr,S.;Moradbakhti,L.;Mara,M.FirstimpressionsofafinancialAIassistant:Differencesbetweenhightrustandlow
trustusers.Front.Artif.Intell.2023,6,1241290.[CrossRef]
22. Sun,J.;Lang,J.;Fujita,H.;Li,H.ImbalancedenterprisecreditevaluationwithDTE-SBD:DecisiontreeensemblebasedonSMOTE
andbaggingwithdifferentiatedsamplingrates.Inf.Sci.2018,425,76–91.[CrossRef]
23. Bond,S.;Elston,J.A.;Mairesse,J.;Mulkay,B.FinancialfactorsandinvestmentinBelgium,France,Germany,andtheUnited
Kingdom:Acomparisonusingcompanypaneldata.Rev.Econ.Stat.2003,85,153–165.[CrossRef]

Electronics2025,14,1505 16of17
24. Liu,J.;Pang,D.FinancialfactorsandcompanyinvestmentdecisionsintransitionalChina.Manag.Decis.Econ.2009,30,91–108.
[CrossRef]
25. Bond,S.;Meghir,C.Financialconstraintsandcompanyinvestment.Fisc.Stud.1994,15,1–18.[CrossRef]
26. Mills,K.;Morling,S.;Tease,W.Theinfluenceoffinancialfactorsoncorporateinvestment. Aust. Econ. Rev. 1995,28,50–64.
[CrossRef]
27. Geetha,N.;Ramesh,M.Astudyonrelevanceofdemographicfactorsininvestmentdecisions.Perspect.Innov.Econ.Bus.2012,10,
14–28.[CrossRef]
28. Lusardi,A.;Mitchelli,O.S.Financialliteracyandretirementpreparedness:Evidenceandimplicationsforfinancialeducation.
Bus.Econ.2007,42,35–44.[CrossRef]
29. HassanAl-Tamimi,H.A.;BinKalli,A.A.FinancialliteracyandinvestmentdecisionsofUAEinvestors.J.RiskFinanc.2009,10,
500–516.[CrossRef]
30. Waweru,N.M.;Munyoki,E.;Uliana,E.Theeffectsofbehaviouralfactorsininvestmentdecision-making:Asurveyofinstitutional
investorsoperatingattheNairobiStockExchange.Int.J.Bus.Emerg.Mark.2008,1,24–41.[CrossRef]
31. Lubis,H.;Kumar,M.D.;Ikbar,P.;Muneer,S.Roleofpsychologicalfactorsinindividuals’investmentdecisions. Int. J.Econ.
Financ.Issues2015,5,397–405.
32. Antony,A.;Joseph,A.I.Influenceofbehaviouralfactorsaffectinginvestmentdecision—AnAHPanalysis.Metamorphosis2017,16,
107–114.[CrossRef]
33. Das,S.;Jain,R.Astudyontheinfluenceofdemographicalvariablesonthefactorsofinvestment—AperspectiveontheGuwahati
region.Int.J.Res.Humanit.ArtsLit.2014,2,97–102.
34. Masomi,S.R.;Ghayekhloo,S.Consequencesofhumanbehaviorsineconomics:Theeffectsofbehavioralfactorsininvestment
decisionmakingatTehranStockExchange.InProceedingsoftheInternationalConferenceonBusinessandEconomicsResearch,
Langkawi,Malaysia,14–16March2011;Volume1,pp.234–237.
35. Senda,D.A.;Rahayu,C.W.E.;Rahmawati,C.H.T.Theeffectoffinancialliteracylevelanddemographicfactorsoninvestment
decision.MediaEkon.Manag.2020,35,100–111.[CrossRef]
36. Lutfi,L.TherelationshipbetweendemographicfactorsandinvestmentdecisioninSurabaya.J.Econ.Bus.Account.Ventur.2010,
13,1–9.[CrossRef]
37. Gaikar,V.Demographicvariablesinfluencingfinancialinvestmentofurbanindividuals: Acasestudyofselecteddistrictsof
MaharashtraState.SSRNElectron.J.2021.Availableonline:https://ssrn.com/abstract=3890224(accessedon22January2025).
[CrossRef]
38. Cooremans,C.Makeitstrategic!Financialinvestmentlogicisnotenough.EnergyEffic.2011,4,473–492.[CrossRef]
39. Alkaraan, F.; Northcott, D.StrategicInvestmentDecision-MakingProcesses: TheInfluenceofContextualFactors. Meditari
Account.Res.2013,21,117–143.[CrossRef]
40. Forssbæck,J.;Oxelheim,L.Finance-specificfactorsasdriversofcross-borderinvestment—Anempiricalinvestigation.Int.Bus.
Rev.2008,17,630–641.[CrossRef]
41. Zarifis,A.;Cheng,X.AmodeloftrustinFintechandtrustinInsurtech:Howartificialintelligenceandthecontextinfluenceit.J.
Behav.Exp.Financ.2022,36,100739.[CrossRef]
42. Huston,S.J.Measuringfinancialliteracy.J.Consum.Aff.2010,44,296–316.[CrossRef]
43. Mandell,L.;Klein,L.S.Theimpactoffinancialliteracyeducationonsubsequentfinancialbehavior.J.Financ.Couns.Plan.2009,
20,15–24.
44. Markowitz,H.M.Foundationsofportfoliotheory.J.Financ.1991,46,469–477.[CrossRef]
45. Davis,F.D.Perceivedusefulness,perceivedeaseofuse,anduseracceptanceofinformationtechnology.MISQ.1989,13,319–340.
[CrossRef]
46. Rahman, M.; Gan, S.S.GenerationYinvestmentdecision: Ananalysisusingbehaviouralfactors. Manag. Financ. 2020, 46,
1023–1041.[CrossRef]
47. Arif,K.Financialliteracyandotherfactorsinfluencingindividuals’investmentdecision:Evidencefromadevelopingeconomy
(Pakistan).J.PovertyInvestig.Dev.2015,12,74–84.
48. Salahuddin,M.;Islam,M.R.Factorsaffectinginvestmentindevelopingcountries: Apaneldatastudy. J.Dev. Areas2008,42,
21–37.[CrossRef]
49. Mlambo,K.;Oshikoya,T.W.MacroeconomicfactorsandinvestmentinAfrica.J.Afr.Econ.2001,10,12–47.[CrossRef]
50. Love,I.;Zicchino,L.Financialdevelopmentanddynamicinvestmentbehavior:EvidencefrompanelVAR.Q.Rev.Econ.Financ.
2006,46,190–210.[CrossRef]
51. Locatelli,G.;Mancini,M.Theroleofthereactorsizeforaninvestmentinthenuclearsector: Anevaluationofnon-financial
parameters.Prog.Nucl.Energy2011,53,212–222.[CrossRef]
52. Masini, A.; Menichetti, E. The impact of behavioral factors in the renewable energy investment decision-making process:
Conceptualframeworkandempiricalfindings.EnergyPolicy2012,40,28–38.[CrossRef]

Electronics2025,14,1505 17of17
53. Ngoc,N.M.;Tien,N.H.;Hieu,V.M.Therelevanceoffactorsaffectingrealestateinvestmentdecisionsforpost-pandemictime.Int.
J.Bus.Glob.2023,1,1–15.[CrossRef]
54. Dutta,N.;Roy,S.Foreigndirectinvestment,financialdevelopmentandpoliticalrisks.J.Dev.Areas2011,45,303–327.[CrossRef]
55. Vesselenyi,T.;Dzi¸tac,I.;Dzi¸tac,S.;Vaida,V.Surfaceroughnessimageanalysisusingquasi-fractalcharacteristicsandfuzzy
clusteringmethods.Int.J.Comput.Commun.Control2008,3,304–316.[CrossRef]
56. Csorba,L.M.;Crăciun,M.Anapplicationofthemulti-perioddecisiontreesinsustainablemedicalwasteinvestments.InSoft
ComputingApplications. SOFA2016. AdvancesinIntelligentSystemsandComputing;Balas,V.,Jain,L.,Balas,M.,Eds.;Springer:
Cham,Switzerland,2018;Volume634,pp.540–556.
57. Zhou,T.;Gao,X.;Sun,X.;Han,L.Splitdifferenceweighting:Anenhanceddecisiontreeapproachforimbalancedclassification.
Int.J.Comput.Commun.Control2024,19,6702.[CrossRef]
58. Daranda,A.;Dzemyda,G.Novelmachinelearningapproachforself-awarepredictionbasedoncontextualreasoning. Int. J.
Comput.Commun.Control2021,16,4345.[CrossRef]
59. Crăciun,M.;Csorba,L.M.Applicationofthefuzzy-pay-offmethodinthevaluationofafinancialinstrument.InSoftComputing
Applications. SOFA2016. AdvancesinIntelligentSystemsandComputing; Balas, V., Jain, L., Balas, M., Eds.; Springer: Cham,
Switzerland,2018;Volume634,pp.235–252.
60. Cuc,L.D.;Rad,D.;Săplăcan,S.;Sendroiu,C.;Bâtcă-Dumitru,G.C.;Wysocki,D.;Dutu,A.;Manolescu,A.-A.Ahierarchical
,
clusteringanalysisofthemanagementaccountingpracticesperceptionsinRomania.Int.J.Comput.Commun.Control2024,19,
6864.[CrossRef]
61. Pelau,C.;Dabija,D.C.;Stanescu,M.CanItrustmyAIfriend?Theroleofemotions,feelingsoffriendshipandtrustforconsumers’
information-sharingbehaviortowardAI.OeconomiaCopernic.2024,15,407–433.[CrossRef]
62. Toader,L.;Paraschiv,D.;Dinu,V.;Manea,D.;Mihai,M.Theeffectsofprivatesectorcompanies’researchanddevelopment
investmentsontheadoptionofcloudcomputingservicesintheEuropeanUnion. E+MÈkon. AManag. 2023, 26, 189–202.
[CrossRef]
63. Ciocoiu,C.N.;Prioteasa,A.L.;Colesca,S.E.RiskmanagementimplementationforsustainabledevelopmentofRomanianSMEs:
Afuzzyapproach.AmfiteatruEcon.2020,22,726–741.[CrossRef]
64. Lazea,G.I.;Bunget,O.C.;Lungu,C.Cryptocurrencies’impactonaccounting:Bibliometricreview.Risks2024,12,94.[CrossRef]
65. Ogrean,C.;Herciu,M.Businessmodelsaddressingsustainabilitychallenges—Towardsanewresearchagenda.Sustainability
2020,12,3534.[CrossRef]
66. Anwar,K.FactorsaffectingstockexchangeinvestmentinKurdistan.Int.J.Account.Bus.Soc.2017,25,32–37.[CrossRef]
67. Carcello,J.V.;Hermanson,D.R.;Raghunandan,K.FactorsassociatedwithUSpubliccompanies’investmentininternalauditing.
Account.Horiz.2005,19,69–84.[CrossRef]
68. Simone,F.; Ansaldi,S.M.; Agnello,P.; DiGravio,G.; Patriarca,R.Knowledgeingraphs: Investigatingthecompletenessof
industrialnearmissreports.Saf.Sci.2023,168,106305.[CrossRef]
69. Patriarca,R.; DeCarlo,F.; Leoni,L.Asystem-theoreticfuzzyanalysis(STheFA)forsystemicsafetyassessment. ProcessSaf.
Environ.Prot.2023,177,1181–1196.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.