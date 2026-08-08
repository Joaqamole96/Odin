| Leveraging |          | Transferable   | Knowledge |           | Concept |           | Graph |     | Embedding |
| ---------- | -------- | -------------- | --------- | --------- | ------- | --------- | ----- | --- | --------- |
|            |          | for Cold-Start |           | Cognitive |         | Diagnosis |       |     |           |
|            | WeiboGao |                |           | HaoWang   |         |           |       |     | QiLiu∗    |
AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof
BigDataAnalysisandApplication, BigDataAnalysisandApplication, BigDataAnalysisandApplication,
SchoolofComputerScienceand UniversityofScienceandTechnology UniversityofScienceandTechnology
Technology,UniversityofScienceand ofChina&StateKeyLaboratoryof ofChina&StateKeyLaboratoryof
TechnologyofChina&StateKey CognitiveIntelligence CognitiveIntelligence
| LaboratoryofCognitiveIntelligence |             |     |                      | Hefei,China |     |     |     | Hefei,China         |     |
| --------------------------------- | ----------- | --- | -------------------- | ----------- | --- | --- | --- | ------------------- | --- |
|                                   | Hefei,China |     | wanghao3@ustc.edu.cn |             |     |     |     | qiliuql@ustc.edu.cn |     |
weibogao@mail.ustc.edu.cn
|     | FeiWang |     |     | XinLin |     |     |     | LinanYue |     |
| --- | ------- | --- | --- | ------ | --- | --- | --- | -------- | --- |
AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof
BigDataAnalysisandApplication, BigDataAnalysisandApplication, BigDataAnalysisandApplication,
SchoolofComputerScienceand SchoolofComputerScienceand SchoolofDataScience,Universityof
Technology,UniversityofScienceand Technology,UniversityofScienceand ScienceandTechnologyofChina&
TechnologyofChina&StateKey TechnologyofChina&StateKey StateKeyLaboratoryofCognitive
LaboratoryofCognitiveIntelligence LaboratoryofCognitiveIntelligence Intelligence
|     | Hefei,China |     |     | Hefei,China |     |     |     | Hefei,China |     |
| --- | ----------- | --- | --- | ----------- | --- | --- | --- | ----------- | --- |
wf314159@mail.ustc.edu.cn linx@mail.ustc.edu.cn lnyue@mail.ustc.edu.cn
|     | ZhengZhang |     |     | RuiLv |     |     |     | ShijinWang |     |
| --- | ---------- | --- | --- | ----- | --- | --- | --- | ---------- | --- |
AnhuiProvinceKeyLaboratoryof AnhuiProvinceKeyLaboratoryof StateKeyLaboratoryofCognitive
BigDataAnalysisandApplication, BigDataAnalysisandApplication, Intelligence&iFLYTEKAIResearch
SchoolofComputerScienceand SchoolofComputerScienceand (CentralChina),iFLYTEKCo.,Ltd
Technology,UniversityofScienceand Technology,UniversityofScienceand Hefei,China
TechnologyofChina&StateKey TechnologyofChina&StateKey sjwang3@iflytek.com
| LaboratoryofCognitiveIntelligence |             |     | LaboratoryofCognitiveIntelligence |             |              |                   |     |               |                      |
| --------------------------------- | ----------- | --- | --------------------------------- | ----------- | ------------ | ----------------- | --- | ------------- | -------------------- |
|                                   | Hefei,China |     |                                   | Hefei,China |              |                   |     |               |                      |
| zhangzheng@mail.ustc.edu.cn       |             |     | lvrui2018@mail.ustc.edu.cn        |             |              |                   |     |               |                      |
|                                   |             |     |                                   |             | interactions | or unavailability |     | of exercising | records for training |
ABSTRACT
Cognitivediagnosis(CD)aimstorevealtheproficiencyofstudents purposes.Totacklethecold-startissue,weproposeatwo-stage
onspecificknowledgeconceptsandtraitsoftestexercises(e.g., solutionnamedTechCD(TransferableknowledgEConceptgrapH
embeddingframeworkforCognitiveDiagnosis).Thefundamental
difficulty).Itplaysacriticalroleinintelligenteducationsystems
notioninvolvesutilizingapedagogicalknowledgeconceptgraph
bysupportingpersonalizedlearningguidance.However,recent
(KCG)asamediatortoconnectdisparatedomains,allowingthe
developmentsinCDmostlyconcentrateonimprovingtheaccuracy
ofdiagnosticresultsandoftenoverlooktheimportantandpracti- transmissionofstudentcognitivesignalsfromestablisheddomains
caltask:domain-levelzero-shotcognitivediagnosis(DZCD).The tothezero-shotcold-startdomain.Specifically,anaiveyeteffec-
primarychallengeofDZCDisthedeficiencyofstudentbehavior tivegraphconvolutionalnetwork(GCN)withthebottom-layer
discardingoperationisinitiallyemployedovertheKCGtolearn
datainthetargetdomainduetotheabsenceofstudent-exercise
transferablestudentcognitivestatesanddomain-specificexercise
∗Correspondingauthor. traits. Moreover, we give three implementations of the general
TechCDframeworkfollowingthetypicalcognitivediagnosissolu-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed tions.Finally,extensiveexperimentsonreal-worlddatasetsnotonly
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation provethatTechcaneffectivelyperformzero-shotdiagnosis,butalso
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe givesomepopularapplicationssuchasexerciserecommendation.
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org.
SIGIR’23,July23–27,2023,Taipei,Taiwan
©2023Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM. CCSCONCEPTS
ACMISBN978-1-4503-9408-6/23/07...$15.00
https://doi.org/10.1145/3539618.3591774 •Appliedcomputing→E-learning.
983

SIGIR’23,July23–27,2023,Taipei,Taiwan WeiboGaoetal.
KEYWORDS Source domain Knowledge concept graph Target domain
Math Programming
cognitive diagnosis; student performance prediction; cold-start; Number Cube
knowledgeconceptgraph
Cone Array ?
ACMReferenceFormat:
WeiboGao,HaoWang,QiLiu,FeiWang,XinLin,LinanYue,ZhengZhang,
similarity ?
RuiLv,andShijinWang.2023.LeveragingTransferableKnowledgeConcept
GraphEmbeddingforCold-StartCognitiveDiagnosis.InProceedingsofthe Arithmetic List
46thInternationalACMSIGIRConferenceonResearchandDevelopmentin
InformationRetrieval(SIGIR’23),July23–27,2023,Taipei,Taiwan.ACM, Student: Concept: Exercise: Answering correctly/incorrectly: /
NewYork,NY,USA,10pages.https://doi.org/10.1145/3539618.3591774 “ ” demonstrates a linking from the mature domain to the new domain.
Figure1:Theexampleofaknowledgeconceptgraph(KCG)
1 INTRODUCTION
connectingisolatedexercisesineachdomain.
Intelligenteducationsystemsfacilitatethepersonalizedlearning toutilizeexercises’textualcontentsastheintermediarybylearning
ofstudentswithcomputer-assistedtechnologybyprovidingopen universalandcross-domainexerciseembeddings[22,35].However,
accesstoabundantlearningmaterials(e.g.,exercises).Theirpreva- therearetwomaindrawbackstotheseapproaches.First,exercises’
lenceandconveniencehavereceivedgreatattentionfromboth textual features may not accurately reflect the true meaning of
educatorsandthegeneralpublic[27].Intheseplatforms,cogni- theexerciseduetolinguisticbias[24].Forexample,twoexercises
tivediagnosis(CD)playsacrucialroleinprovidingcustomized fromcourseMathandcourseProgramming mayhavethesame
applicationstailoredtoindividualneeds[37].Specifically,thegoal description"Calculatethecircle’sarea",buttheyaretestingdiffer-
ofCDistoprofilestudents’latentcognitiveproficiency onspe- entconcepts,i.e.,GeometryandProgrammingLanguage.Second,
cificknowledgeconcepts,aswellastorevealcharacteristicsof toproficientlyadjusttodiversedomains,theexercisetextencoder
thetestexercisessuchasdifficultyanddiscrimination[9,37].As necessitatesdomain-specificguidance,whichhasthepotentialto
thediagnosticresultscansupportfurthereducationalapplications, overfitandobstructthetransmissionofcognitivesignalsbetween
suchasexerciserecommendation[19,46]andlearningpathsugges- distinctdomains[48,54].Therefore,itisdesirabletofindamore
tions[18,39],anumberofexistingmethodshavetriedtoimprove suitableintermediarytoconnectdifferentdomains.
theaccuracyofdiagnosticresultsbyfullyexploitingthestudents’ Inthispaper,weemployapedagogicalknowledgeconceptgraph
explicitresponserecords(e.g.,answeringcorrectlyornot). (KCG)astheintermediarytofacilitatethesharingofstudentcogni-
However,manypreviousmodelsfacechallengeswiththe"diag- tivestatesacrossdifferentdomains.Theunderlyingrationaleisthat
nosticsystemcold-start"problem.Forinstance,inonlineplatforms, theKCGhasthepotentialtoconnectdifferentdomainswhichcanbe
itiscommontolaunchnewbusinesses,e.g.,coursera.orgplansto abridgetopropagatestudentcognitivestates.Toelaborate,aKCG
releaseaseriesofnewtestexercises.Forthenewdomain,there comprisesnumerouseducationaldependencies(asrelations)tolink
arenostudent-exerciseinteractionrecordsavailable.Hereby,the knowledgeconcepts(asentities),whichhasbeenwidelyusedin
diagnosticperformanceofpreviousapproachesisoftenimpaired AIforEducation[3,34,45].Figure1illustratesanexampleofKCG
astheyonlyaddresstheCDtaskinmaturesourcedomainswhere withsomeeducationaldependencyrelations,e.g.,thesimilarityre-
student-exerciseinteractiondataareavailable.Inthispaper,we lationlinksconceptConeandconceptCubesincetheybelongtothe
callthediagnosticsystemcold-starttaskasdomain-levelzero-shot sametopicGeometry,whileNumberistheprerequisiteconceptof
cognitivediagnosis(DZCD).Differentfrompreviousstudiesonstu- Arithmeticastheformeristhelearningbasisofthelatterlogically.
dentsorexercisescold-startforCDwithinawell-establishedsource Obviously,theKCGhasthecapabilitytobridgedifferentdomains
domainwhereinteractionrecordsareavailable[22,33],inDZCD, if it covers the knowledge concepts and associated exercises in
studentspartiallyoverlapacrossdomains,andthematuresource eachdomain.Forexample,fortwocourse-leveldomains,theMath
domainshaverichstudentresponserecordsbutthezero-shottarget (sourcedomain)andProgramming(targetdomain),eachoftheir
domainisbrandnewwithoutstudent-exerciseinteractions.The exercisesassociatesatleastoneknowledgeconcept.Thisallows
DZCDisanimportantandpracticaltask,typicalapplicationsin- thetwodomainstobeconnectedthroughtheKCGaslongastheir
clude:(1)itisnecessarytodiagnoseinadvancewhenanonline associatedconceptsoccurintheKCG,eventhoughtheirexercises
learningsystemintendstolaunchanewbusiness;(2)students’ havenodirectoverlap.Thus,introducingaKCGastheintermediary
behaviordatainthetargetdomainareunavailableduetocollection acrossdomainstopropagatestudentcognitivestatesispromising,
limitationslikeprivacyprotectionpolicy.Nevertheless,tothebest butalsosignificantlychallenging.Ideally,aproperKCGmodelfor
ofourknowledge,thereisaseverelackofresearchonDZCD. CDshouldhavefouressentialproperties:(1)diagnosis-oriented:
Toprovidereliablecognitivediagnosisforazero-shotdomain, themodelcanperformtheCDtaskintheDZCDsetting;(2)stu-
inspiredbythesuccessofcross-domainmodelinginvariousfields dentstatepropagation:theKCGmodelshouldextractuniversaland
(e.g.,recommendersystems[25,54]),onepossiblewayistodefine transferableinformationforstudentembeddingssothatstudent
commonstudentstatecharacteristicsbyanalyzingtheirpastbehav- cognitivesignalscanbesharedacrossdomains;(3)domainadap-
iorsfromafewaccessiblesourcedomains,andrepresentthetest tion:foranycold-startdomainwhichneedsdiagnosis,themodel
exercisesinthetargetdomainusingavailablefeatures.Theprimary isexpectedtobedomain-adaptive.(4)application:thediagnostic
obstacleistolocateanappropriatemediatorthatcantransmitstu- resultscaneffectivelysupportfurtherintelligentservices.
dentstatesbetweentheestablishedandtargetdomains,enabling Motivatedbytheaboveconsiderations,weproposeageneral
theexecutionofDZCD[54].Somerelatedstudieshaveattempted TransferableknowledgEConceptgrapHframeworktoperform
984

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
thedomain-levelzero-shotCognitiveDiagnosis(abbreviatedas Basedonthesetraditionalmethods,someresearchersintroduce
TechCD). The TechCD framework consists of two stages: the deeplearningintocognitivediagnosis.Forinstance,NeuralCogni-
knowledgeconceptgraphembedding(KCGE)stageandthedo- tiveDiagnosis(NeuralCD)[41]andDeep-IRT[38]exploitneural
mainadaptivediagnosis(DAD)stage.IntheKCGEstage,anaive networkstolearntheinteractionfunctionandtraitembeddings
yeteffectivegraphconvolutionalnetwork(GCN)[49]isfirstem- automatically.Recently,toalleviateissuesofstudentorexercise
ployed over the KCG for representation learning by iteratively cold-start,anddatasparsityinreal-worldscenarios,somestudies
fusingneighboringaggregationsintheKCG.Totakefulladvantage havealsoconsideredincorporatingexercisetexts[22],theconcep-
oftheconnectionsbetweenexercisesandtheKCG,wetreateach tualrelations[10,21]andmoreexceptions(e.g.,slipandguess)[23]
exerciseaspartoftheKCGforjointmodelingwithconceptentities, instudents’learningprocesstoenhancetheinteractiverelations
sothattheexercisescanabsorbstructuralinformationfromthe betweenstudentsandexercises.However,tothebestofourknowl-
graphastheirsemanticdescriptions.Themostdifficultaspectin edge,researchonhowtocold-startaCDsystemremainsunsolved.
thisstageistoguaranteethestudentstatepropagationproperty.
2.2 Cold-StartIntelligentSystems
Tothisend,inspiredby[54],weconstructtransferablestudent
Cold-startinganintelligentsystemwithouthistoricalinteractions
statesbydiscardingthebottomlayersofGCN(specificpatterns)
availablefornewusersoritemsisaprevalentandpracticalconcern
andonlyaggregatinghigh-levelones(universalpatterns)sothat
inmanydomains[15,32,33,51,52].Thispaperfocusesonthe
cognitivesignalscanbesuccessfullypropagatedtootherdomains.
taskofcold-startingacognitivediagnosissysteminazero-shot
Webuilddomain-specificexercisesandconceptsbyincorporating
domain,whichisofparamountimportancetounderstandingthe
comprehensivesemanticinformationfromtheKCGsothattheir
firstbatchofstudents’learningprocess,analyzingtheirknowledge
embeddingscomprisebothuniversalandspecificpatterns,which
proficiencyandfurtherhelpingimproveequityineducation[12].
ensuresdomainadaptation.IntheDADstage,theaboveembeddings
Totacklethisissue,manystrategieshavebeenutilizedsuchasmeta-
arefurtherfusedtoconstructthetraitsofstudents(i.e.,proficiency)
learning[40],cross-domainmodeling[25,54]andreinforcement
andexercises(e.g.,difficulty)bypredictingstudentperformance.
learning[7].Wepayattentiontotheideaofcross-domainmodeling,
Inthisway,thetraitsofstudentsandexercisesthatneedtobe
whichaimstocharacterizestudentstatefeaturesbasedontheir
diagnosedcanberefinedsatisfyingthediagnosis-oriented prop-
historicalbehaviorsfromsomeavailablesourcedomainsandrepre-
erty.ItisworthmentioningthatourgeneralTechCDframework
sentthetestexercisesinthetargetdomainwithavailablefeatures.
iswelldefinedtobeimplementedbycombiningwithexistingCD
The keychallenge isto find asuitable intermediary toconnect
solutions.Forinstance,wecanhaveTech-IRTbycombiningwith
thematureandtargetdomains.Somerelatedstudiesonstudent
IRT[9],Tech-MIRTwithMIRT[30]andTech-NeuralCDwithNeu-
performancepredictiontasks[22,35]utilizeexercises’textualcon-
ralCD[41],respectively.Finally,weconductextensiveexperiments
tentsastheintermediarybylearninguniversalandcross-domain
onfourreal-worlddatasets.Theexperimentalresultsnotonlyprove
exerciseembeddings.However,thesemethodsmaybelimiteddue
thatTechCDismoreeffectiveinzero-shotstudentperformance
tolinguisticbiasandcannotadapttodifferentdomainseffectively.
predictionsinceitcanwellcapturetheuniversalstudents’cogni-
tivesignalsforpropagationbutalsoshowthesuperiorapplication 2.3 PedagogicalKnowledgeConceptGraph
propertyoftheTechCD.Forinstance,TechCDcanfacilitatesome ApedagogicalKCGcontainsnumerouseducationaldependencies
personalizedlearningguidancesuchasexerciserecommendation (asrelations)toconnectknowledgeconcepts(asentities).Ingen-
incold-startscenarios. eral,thedependenciesareconstructedmanuallybydomainexperts
orautomaticallythroughdata-drivenalgorithmsbasedonpedagog-
2 RELATEDWORK
icalpriorknowledge[28],Amongthem,themostsignificantand
2.1 CognitiveDiagnosis commondependenciesincludesimilarity[26],collaboration[17],
Cognitivediagnosis(CD)isafundamentaltaskinmanyreal-world prerequisite [3], remedial [34] and hierarchy [21]. For example,
scenariossuchasgames[4],medicaldiagnosis[47],andespecially, apairofconceptsinvolvedinthesametopicorareaoroverlap-
education[10,23].ThekeyspiritofCDisthatitcanbeusedto pinginsomeknowledgecanbeassignedwithsimilaritydepen-
profilestudents’latentcognitiveproficiencyonspecificknowledge dencyrelations.Recently,someKCGshavebeenestablishedinboth
concepts,aswellasbeappliedtorevealcharacteristicsofthetest academiaandindustrysuchasOpenEduKG1andSongshuAIKCG2.
exercisessuchasdifficultyanddiscrimination[9,37]viaexploiting OnthebasisofKCGs,researchersattempttoincorporatetheminto
studenttestinglogs.Theserefinedtraitfeaturescouldbeapplied manyeducationalapplicationtasksandobtainsignificantimprove-
to many intelligent applications, such as exercise recommenda- ments[10,26,36].OurTechCDproperlyincorporatesatailored
tion[19,46]andlearningpathsuggestions[18,39].Intheearly pedagogicalKCGintoCDlinkingeachdomainsoastomitigate
years,cognitivediagnosiswasmostlydevelopedfromthepsycho- thedomain-levelzero-shotissue.
metricassumptionthatstudentcognitivestatesarestableinashort
periodoftime(e.g.,anexam)andthuscanbediagnosed[10].In 3 PRELIMINARIES
general,thesemethodsdevotemuchefforttothedesignofstudent-
3.1 CognitiveDiagnosisModel
exerciseinteractionfunctions,whichareexpectedtoautomatically
Wefirstbrieflyintroducecognitivediagnosismodels(CDMs).CDMs
inferstudents’knowledgestates.Forinstance,ItemResponseThe-
aredevelopedtodiscoverstudentproficiencylevelsonspecific
ory(IRT)[9],MultidimensionalIRT(MIRT)[30]andDeterministic
Inputs,Noisy-Andgate(DINA)[5]modeltheinteractionofstudents
1https://open.edukg.cn
andexerciseslinearly(e.g.,leveragingthelogistic-likefunction). 2https://www.songshuai.com/education
985

SIGIR’23,July23–27,2023,Taipei,Taiwan WeiboGaoetal.
knowledgeconceptsaswellasexercisetraits(e.g.,difficulty)through Definition2(Domain-levelzero-shotcognitivediagnosis).
fullyexploitingtheirresponsestoseveralexercises[37].Duetothe Givenstudentexercisingrecords𝐿 S inthesourcedomainandthe
realproficiencyofstudentscannotbequantifiedexplicitly,almost KCG,G,thegoalofTechCDfortheDZCDtaskistomakethediag-
allofthepreviousCDMsaretrainedthroughthestudentperfor- nosisonstudentandexercisetraitsinthetargetdomainT through
mancepredictiontask,i.e.,F CDM (𝒖,𝒗)→𝑦ˆ 𝑢𝑣 ,where𝒖and𝒗are fullyexploitingstudent-exerciseinteractiverecords𝐿 S inthesource
thelatenttraitsofstudentsandexercises,F
CDM
(·) isthediag- domainSwithstudentperformancepredictions.
nosticinteractionfunction,and𝑦ˆ isthepredictedperformance
𝑢𝑣
score.Thesetraitsofstudentsandexercisescanberefinedwith 4 THETECHCDFRAMEWORK
theoptimizationtargetofminimizingthedifferencebetweenthe 4.1 FrameworkOverview
predictedprobability𝑦ˆ andthetrueresponse𝑦 [10]. Conductingcognitivediagnosisindomain-levelzero-shotsettings
𝑢𝑣 𝑢𝑣
Generally, the differences between CDMs consist of the de- isnon-trivial.Itpresentsacriticalchallengeinlearningportable
sign of F CDM (·) and the representations of trait 𝒖 and 𝒗. For andtransferablestudentembeddingsfromtheirexercisingperfor-
example,IRT[9]usessingle-dimensionvariablestorepresentthe mancerecordsinthesourcedomain.Toovercomethisproblem,
traitfeaturesandlogistic-likefunctionastheinteractionfunction: weproposeaTechCDframeworkthatincorporatesatailoredpeda-
𝑖 𝑃 ’s (𝑦 k 𝑖 n 𝑗| o 𝜃 w 𝑖 , l 𝑎 e 𝑗 d , g 𝑏 e 𝑗) pr = ofi 1 c + ie 𝑒 n −1 c .7 y 𝑎 1 , 𝑗 a (𝜃 n 𝑖 d −𝑏 𝑎 𝑗) , a w nd he 𝑏 re r 𝜃 e 𝑖 pr c e h s a e r n a t c e te x r e i r z c e i s se st 𝑗 u ’s de d n is t - g so o u g r i c c e al a k n n d o t w ar l g e e d t g d e o c m on ai c n e s p . t O g u r r ap p h ro ( p K o C se G d ) T as ec a h b C r D id f g r e am be e t w w o e r e k n c t o h n e -
𝑗 𝑗
criminationanddifficulty.NeuralCD[41]exploitsneuralnetworks sistsoftwostages:knowledgeconceptgraphembedding(KCGE)
tofittheinteractionfunctionautomatically:𝑦ˆ
𝑖𝑗
=𝐹(𝒖𝑖 ,𝒗𝑗 ,Θ 𝐶𝐷), anddomainadaptivediagnosis(DAD).TheKCGEstage(detailed
where𝒖and𝒗arethelatenttraitsofstudentsandexercisesrespec- inSection4.2)learnsentityembeddingsfromthesemanticand
tively,and𝐹(·)ismulti-layerneuralnetworks.Tosummarize,we structuralinformationoftheKCG.TheDADstage(detailedinSec-
havethefollowinggeneralformofCDMs: tion4.3)thenconductsdiagnosisbypredictingstudentexercise
𝑦ˆ 𝑢𝑣 =F CDM (𝒖,𝒗,Θ∗), (1) per I f n or t m he an K c C e G .T E h s e ta en ge ti , r t e h s e tr c u r c it t i u c r a e l o o f b T s e ta c c h l C e D is i t s o d p ep ro ic p t a e g d a i t n e F s i t g u u d r e e n 2 t .
whereΘ∗ isthemodelparameter.Tobenoticedthat,toensure
cognitivestatesfromthesourcedomaintothetargetdomain.For
psychometricinterpretabilityofprediction,CDMsshouldstrictly
thisgoal,wecustomizeaKCGastheintermediarytolinkexer-
followtheMonotonicity assumption[37]:theprobabilityofcor-
cisesinvariousdomains.Weuseastraightforwardbuteffective
rectlyansweringtheexercisemonotonicallyincreaseswithstudent
graphconvolutionalnetwork(GCN)[49,54]ontheKCGtocon-
knowledgeproficiency,i.e., 𝜕F >0.
𝜕𝒖 structtransferablestudentcognitiveembeddingsthattranscendthe
exercise-relatedperformanceconfinedtothesourcedomain.Be-
3.2 KnowledgeConceptGraph
sideslearningtransferablestudentembedding,thisstagegenerates
ApedagogicalKCGcontainsknowledgeconceptentitiesandcon-
specificembeddingsofexerciseandconceptentitiesbyintegrating
ceptualdependencyrelations,whereas,inthedomain-levelcold-
thestructureandsemanticinformationfromtheKCG.
startingsettings,itadditionallyincludesexerciseentitiesandexercise-
Withtheaboveembeddings,theDADstagefurtherconstructs
conceptassociationrelations.
studentproficiencytraitsandexercisedifficultyanddiscrimina-
Definition1(Knowledgeconceptgraph). Formally,theKnowl- tiontraitsfordomain-adaptivecognitivediagnosiswithexisting
edgeconceptgraph(KCG)canberepresentedasG = {E,R,P}.E diagnosticmodels.Theentiremodelistrainedthroughpredicting
isthesetofentitiesincludingknowledgeconceptsets C andtheir studentperformanceonexercises,i.e.,𝑦ˆ 𝑢𝑣 = F CDM (𝐿 S ,G,Θ∗),
associatedexercises.Risthesetofrelationsincludingeducationalde- whereparameterΘ∗isoptimizedfromthesourcedomainSas:
pendencyrelationsbetweenconcepts(e.g.,prerequisiteandsimilarity)
Θ∗=argminL(𝑦(𝐿 ),G). (2)
andassociationrelationsbetweenexercisesandconcepts.Pisoffered S
Θ
intheformofentity-relation-entitytripletsetP = {(ℎ,𝑟,𝑡)|ℎ,𝑡 ∈ ItisworthmentioningthattheKCGEstageandtheDADstage
E,𝑟 ∈R},e.g.,(conceptcube,similarity,conceptcone)and(exercise aretrainedinanend-to-endfashionwiththeaboveEq.(2).Thus,the
𝑒1,association,conceptfunction). refinedtraitsofstudentsandexercisescanbethediagnosticresults.
Aftertraining,TechCDcanconductzero-shotstudentperformance
3.3 ProblemDefinition
predictionsinthezero-shottargetdomainT.
Inthedomain-levelzero-shotcognitivediagnosis(DZCD)scenario,
we represent the mature/available source domain as S and the 4.2 KnowledgeConceptGraphEmbedding
cold-start/zero-shottargetdomainasT.Thestudentsetsandex- Thisstageaimstoidentifyuniversalstudentstatespresentinexer-
ercise sets in source domain S are denoted as U , V , and in cisesofthesourcedomainthatcanbetransferredtothezero-shot
S S
targetdomainT aredenotedasU ,V ,whereU ⊂ U and domainviathecustomizedKCG.Forthisgoal,weapplyamulti-
T T T S
V
S
∩V
T
=∅.Allstudent-exerciseperformancerecordsfortrain- layerGCNnetwork3overtheKCGtolearnentityembeddings.
ing(withlabel)arecollectedfromthesourcedomain,depictedas Generally,theKCGcontainsconceptandexerciseentities,aswell
𝐿 S = {(𝑢 𝑖 ,𝑣 𝑗 ,𝑦 𝑖𝑗)|𝑦 𝑖𝑗 ∈ {0,1},𝑢 𝑖 ∈ U S ,𝑣 𝑗 ∈ V S },where𝑦 𝑖𝑗 =1 asmultipleconceptualdependencyrelationsandexercise-concept
representsstudent𝑢 𝑖 answersexercise𝑣 𝑗 correctly,and𝑦 𝑖𝑗 =0oth- associationrelations,asshowninFigure2(a).Theeducational
erwise.Thestudent-exerciseinteractionsfromthetargetdomain
3Actually,variousKCGembeddingtechniqueshavebeenproposedtoextractmeaning-
(withoutlabel),i.e.,𝐿 T ={(𝑢 𝑖 ,𝑣 𝑗)|𝑢 𝑖 ∈U T ,𝑣 𝑗 ∈V T },areusedto fulembeddings[42,49].Sinceourfocusisnottodevisemoresophisticatedtechniques
evaluatepredictionperformanceinDZCDscenarios.Hereby,our forgraphnetworkembedding,wesimplyuseapopularGCNtolearnentityrepresen-
TechCDmodelfortheDZCDtaskisdefinedas: tations,toverifytheeffectivenessofincorporatingtheKCGintotheDZCD.
986

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
1
|     |     |     |     |     |     |     |     |     | ℎ𝑢  |     |     | 𝒅𝒗  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑓𝛽
ℎ𝑐
ℎ𝑣
|     |     |     |     |     |     |     |     |     |     | ℎ𝑢  | ℎ𝑐  | ℎ𝑣  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure2:TheoverviewarchitectureofTechCD:(a)aknowledgeconceptgraph(KCG)linksthesourceandthetargetdomains;
(b)theknowledgeconceptgraphembeddingforentityrepresentationlearning;(c)thedomainadaptivediagnosisforDZCD.
dependency relations reflect student learning rules and knowl- completesemanticrepresentation𝒛𝑖 ∗,asEq.(4).
edgetransferringlogically,whichcanimplicitlypropagatestudent 𝐿 𝐿
|     |     |     |     |     |     |     |     | 1   | ∑︁  |     | 1 ∑︁ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
states[8],whiletheexercise-conceptassociationscanenhanceex- # (𝑙),𝒛𝑖 ∗= (𝑙). (4)
|     |     |     |     |     |     |     | 𝒛𝑖 = | 𝐿− 𝜆+1 | 𝒛𝑖  |     | 𝐿+ 1 | 𝒛𝑖  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --- | --- | ---- | --- |
erciserepresentationsbyabsorbingstructuralandsemanticinfor-
|     |     |     |     |     |     |     |     |     | 𝑙=𝜆 |     | 𝑙=0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hereby,weconstructthetransferablecognitivestateofstudent
mationfromtheKCG.Thereby,foreachentityembedding,itneeds
todiscriminatedifferentrelationsbyseparatelyfusingneighboring 𝑢byabsorbinggeneralknowledgefromtheKCGas:
i n f o r m a t i o n o f e a c h t y p e o f r e l a t i o n . W e d i r e c t l y u s e t h e le a r n a b l e 1
|     |     |     |     |     |     |     |     |     |     | ∑︁  | # , | ( 5 ) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
e m b e d d i n g ∈ R 𝑑 o f e a c h e n t it y 𝑒 a s t h e i n p u t o f G C N , i . e . , 𝒉 𝑢 = 𝒛 𝑣
|       | 𝒆 𝑖 |     |     | 𝑖   |     |     |     |     | | H S | |      |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- |
| ( 0 ) |     |     |     |     |     |     |     |     | 𝑢     | 𝑣∈ H S |     |     |
𝒛 = 𝑐 𝑖 , w h e r e 𝑑 i s t h e e m b e d d i n g d i m e n s i o n a l si z e . W e c o n d u c t 𝑢
𝑖 whereH𝑢 S istheexer c ise s e t t ha t st u de n t 𝑢 hasinteractedwi t h
| c o n v o lu | t i o n o p e r | a t i o n [ 4 | 4 ] o f G C N | o v e r t h e K C G 𝐿 t i m | e s w i t h e a c h |                           |     |     |     |                               |     |     |
| ------------ | --------------- | ------------- | ------------- | --------------------------- | ------------------- | ------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
|              |                 |               |               |                             |                     | inthesourcedomainS.Weuse𝒛 |     |     |     | # torepresentstudentstates,as |     |     |
iterationconsideringeachtypeofrelationseparately,toaggregate 𝑣
itcapturesentity-specificinformationinthebottom-layeroutput,
| 𝐿 hop | neighborhood | information |     | and generate𝐿 entity | embed- |     |     |     |     |     |     |     |
| ----- | ------------ | ----------- | --- | -------------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
∗
(1),𝒛𝑖 (2),...,𝒛𝑖 (𝐿) (𝑙) wh il e 𝒛 𝑣 c o n t a in s m o re g e n e r a l hi g h - o r d e r i n f o r m a t io n .
| dings,[𝒛𝑖                |     |                                         | ],where𝒛𝑖                         | ∈R𝑑 denotesthe𝑙-thlayer |     |                                                           |                |              |               |             |                    |                   |
| ------------------------ | --- | --------------------------------------- | --------------------------------- | ----------------------- | --- | --------------------------------------------------------- | -------------- | ------------ | ------------- | ----------- | ------------------ | ----------------- |
|                          |     |                                         |                                   |                         |     | B e s                                                     | id e s g e n e | ra t in g st | u d e n t e m | b e d d i n | g s , t h i s s ta | g e a l sooutputs |
| outputofentity𝑒          |     | .TheGCNiterativelyaggregatesneighboring |                                   |                         |     |                                                           |                |              |               |             |                    |                   |
|                          |     | 𝑖                                       |                                   |                         |     | exerciseandknowledgeconceptrepresentations.Fortheexercise |                |              |               |             |                    |                   |
| informationofeachentity𝑒 |     |                                         | foreachtypeofrelationseparatelyto |                         |     |                                                           |                |              |               |             |                    |                   |
|                          |     |                                         | 𝑖                                 |                         |     | entity𝑣,wedirectlyassignitscorrespondingembedding𝒛∗       |                |              |               |             |                    | from              |
𝑣
enhanceitsrepresentationt hroughthemessage-passing-receiving theentity𝑒 intheKCGtoitsimilarto[54],i.e.,𝒉𝑣 𝒛∗ .Note
|     |     |     |     |     |     |     | 𝑣   |     |     |     |     | = 𝑣 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mechanism[13,43]asfollows:
thatexerciseembeddingsincorporatebothgeneralanddomain-
(𝑙) ∑︁ 1 ∑︁ 𝑙−1), s p e c ifi c i n fo r m at i on b y a b so r b in g fu l l se m a nt i c re p r es e n t a t i o n s o f
|     | 𝒛𝑖  | =   |     | W𝑟𝒛 ( | (3) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑟| 𝑗 e x er c is e e n ti t ies i n th e K C G , w h ic h c a n fi ll in t h e d o m a i n - a d a p t io n
|     |     |     | |P 𝑖 | 𝑟   |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑟∈R𝑖 (𝑒𝑗,𝑟,𝑒𝑖)∈P 𝑖 requirementsintuitively.Similarly,werepresenteachconcept𝑐’s
whereR𝑖 isthesubsetofRconsistingoftherelationtypesofentity embedding𝒉𝑐 withitsfullsemanticrepresentation𝒛𝑐 ∗,i.e.,𝒉𝑐 ∗.
=𝒛𝑐
| 𝑒 .P 𝑟 isthesubsetofPcontainsallthetriplets(𝑒 |     |     |     | ,𝑟,𝑒 | 𝑖)ofentity |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| 𝑖 𝑖                                           |     |     |     | 𝑗    |            |     |     |     |     |     |     |     |
4.3 DomainAdaptiveDiagnosis
𝑒 𝑖 withrelation𝑟.Foreachrelation𝑟,weusealearnablematrix
W𝑟 ∈ R𝑑×𝑑 to transform each concept/exercise entity feature Inthisstage,weconductdomain-adaptivecognitivediagnosiswith
vectortothesamefreeembeddingspace. existingcognitivediagnosismodels.
Afterobtainingtheaboverefinedentityembeddings,thefocus
|     |     |     |     |     |     | 4.3.1 | DiagnosedTraitRepresentationModeling. |     |     |     |     | Ingeneral, |
| --- | --- | --- | --- | --- | --- | ----- | ------------------------------------- | --- | --- | --- | --- | ---------- |
isonrepresentingtransferablestudentembeddingstoaddressthe
|     |     |     |     |     |     | a cognitive | diagnosis |     | model (CDM) | takes | the traits | of students |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ----------- | ----- | ---------- | ----------- |
challengeofstudentstatepropagation.Weresorttothebottom- (i.e.,proficiency)andexercises(e.g.,difficultiesanddiscrimination)
discardingoperation[54]whichisnaturallycompatible.Itargues asthebasicinput[41].Thus,itiscrucialtorepresenttheabove
thatthebottomlayersofGCNpreservemoredomain-specificin- traitsthatneedtobediagnosedviathegeneratedembeddingsfrom
formation,whiletheupperlayersbetterrepresentuniversaland
theKCGEstage.Inspiredby[10,21],togeneratetheproficiency
transferableinformation.Thisisintuitivelyreasonablebecausein-
factoroneachconceptofeachstudent,weincorporatetheembed-
creasingthenumberofGCNlayerscanleadtoover-smoothing, dingsofknowledgeconceptentitiesintothetransferablestudent’s
resultinginthelossofdiscriminativeinformation[16],whichmakes embedding.Thus,thestudentproficiencytraitcanbemodeledas:
itpromisingtoeffectivelypropagatestudentcognitivesignalsto
|     |     |     |     |     |     | =(𝑝 | ;𝑝  | ;··· ;𝑝 | ), where𝑝 |     | =𝑓  | (0,1). (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | ---------- |
zero-shotdomains.Thus,wediscardthelower-levelentityembed- 𝒑𝑢 𝑢1 𝑢2 𝑢|C| 𝑢𝑐 𝑢(𝒉𝑢⊕𝒉𝑐) ∈
dingsbysettingsahyper-parameter𝜆toaggregatetransferable IntheaboveEq.(6),vector𝒑𝑢 isstudent𝑢’sproficiencyon
|C|
embeddings𝒛𝑖 #.Additionally,wefusealllayeroutputembeddings knowledgeconceptsintheKCG.Eachelementof𝒑𝑢 ,i.e.,𝑝 ,de-
𝑢𝑐
ofGCNaswellastheoriginalentityembedding,resultingina notesstudent𝑢’smasterylevelonconcept𝑐.Afullconnection
987

| SIGIR’23,July23–27,2023,Taipei,Taiwan |     |     |     |     |     |     |     |     |     | WeiboGaoetal. |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
layer[50]𝑓 𝑢(·)isusedtofuseknowledgeconceptsemanticsinto Table1:Somebasicstatisticsofthedatasets.
thestudentembeddingwithconcatenation⊕.Similarly,wealso
|     |     |     |     |     |     |     | Datasets |     | CM AM | Junyi ASSIST |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | ------------ |
fuseknowledgeconceptinformationintoexerciseembeddingsto
|     |     |     |     |     |     |     | #Student |     | 21,068 21,059 | 10,000 5,730 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | ------------ |
calculateeachexercise𝑣’sdifficultytrait𝒅𝑣 onallconceptswith #Exercise 6,257 3,263 706 4,973
thefullconnectionlayer𝑓 𝑣(·)asEq.(7). #Knowledgeconcept 1,251 990 706 122
|     |     |     |     |     |     |     | #Record |     | 351,146 171,380 | 353,835 225,314 |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------------- | --------------- |
𝒅𝑣 =(𝑑 𝑣1 ;𝑑 𝑣2 ;··· ;𝑑 𝑣|C| ), where𝑑 𝑣𝑐 =𝑓 𝑣(𝒉𝑣 ⊕𝒉𝑐) ∈ (0,1). (7) #Recordperstudent 16.7 8.1 35.4 39.3
| Besides,thediscrimination𝛽 |     |     | ofeachexercise𝑣isdirectlyobtained |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝑣
|                                                        |                   |     |                                  |            |                        |     | istheknowledgeconceptset.TheF |                                              |                                 | (·)isamulti-layerneu- |
| ------------------------------------------------------ | ----------------- | --- | -------------------------------- | ---------- | ---------------------- | --- | ----------------------------- | -------------------------------------------- | ------------------------------- | --------------------- |
| bytransformingtheexerciseembeddingtoalatentfactorwitha |                   |     |                                  |            |                        |     |                               |                                              | CDM                             |                       |
|                                                        |                   |     |                                  |            |                        |     | ralnetworks𝜙                  | withnon-negativeweightstokeepexplainability: |                                 |                       |
| neuralnetwork𝑓                                         | 𝛽(·),i.e.,scalar𝛽 |     |                                  | 𝑣 =𝑓 𝛽(𝒉𝑣) | ∈ (0,1),similarto[21]. |     |                               |                                              |                                 |                       |
|                                                        |                   |     |                                  |            |                        |     | 𝑦ˆ =𝜙(𝑸𝒗                      | 𝑇 −𝒅𝑣)·𝛽                                     | 𝑣),where◦iselement-wiseproduct. |                       |
|                                                        |                   |     |                                  |            |                        |     | 𝑢𝑣                            | ◦(𝒑 𝑢                                        |                                 |                       |
| 4.3.2 DiagnosticAdaptor.                               |                   |     | Differentdiagnosticmodelscharac- |            |                        |     |                               |                                              |                                 |                       |
terizestudentandexercisefeaturesindifferentforms.Ouraimis 5 EXPERIMENTS
toestablishaconnectionbetweenstudents’cognitiveproficiency, Weconductcomprehensiveexperimentstoaddressthefollowing
| exercise traits, | and | the input | forms | of  | existing diagnostic | mod- |     |     |     |     |
| ---------------- | --- | --------- | ----- | --- | ------------------- | ---- | --- | --- | --- | --- |
researchquestions:
els,throughintroducingthediagnosticadaptor.Ingeneral,forthe
|     |     |     |     |     |     |     | • RQ1CantheTechCDframeworkeffectivelyhandlethedomain- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
givenstudent𝑢andexercise𝑣,theCDMadaptorpredictsstudent levelzero-shotcognitivediagnosistask?
| performancescore𝑦ˆ |     | 𝑢𝑣 asEq.(8): |     |     |     |     |                                                    |     |     |     |
| ------------------ | --- | ------------ | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- |
|                    |     |              |     |     |     |     | • RQ2HowabouttheeffectivenessofmodelingtheKCGbythe |     |     |     |
TechCDframework?
|     | 𝑦ˆ 𝑢𝑣 | =F  | (𝜙 𝑢(𝒑𝑢),𝜙 |     | 𝑣(𝒅𝑣),𝛽 𝑣), | (8) |                                                        |     |     |     |
| --- | ----- | --- | ---------- | --- | ----------- | --- | ------------------------------------------------------ | --- | --- | --- |
|     |       | CDM |            |     |             |     | • RQ3CantheTechCDutilizetheout-of-domaindatasetsforthe |     |     |     |
performanceimprovement?
| whereF CDM | (·)representstheexistingdiagnosticmodelandcan |     |     |     |     |     |     |     |     |     |
| ---------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RQ4HowtoapplyTechCDtoprovidepersonalizedguidance?
| bespecifiedwithmanymodelslikeIRT[9],MIRT[30],etc.Tocover |     |     |     |     |     |     | •   |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
differentdiagnosticmodels,weemploytwotransformfunctions,
|            |                                                 |     |     |     |     |     | 5.1 Datasets |     |     |     |
| ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| 𝜙 𝑢(·)and𝜙 | 𝑣(·),tostandardizetheformofstudentproficiency𝒑𝑢 |     |     |     |     |     |              |     |     |     |
Weconductexperimentsonthefollowing
and exercise difficulty so as to satisfy the input form of the 5.1.1 BasicDescription.
|     |     | 𝒅𝑣  |     |     |     |     | fourreal-worldrepresentativedatasets: |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
adoptedmodel.Besides,toensurethemonotonicityassumption
|                                                 |         |                                    |     |     |     |      | • CoreMath(CM)andAdvancedMath(AM)aretwosubsetsof        |     |     |     |
| ----------------------------------------------- | ------- | ---------------------------------- | --- | --- | --- | ---- | ------------------------------------------------------- | --- | --- | --- |
| ofcognitivediagnosis,werestricteachparameterofF |         |                                    |     |     |     | tobe |                                                         |     |     |     |
|                                                 |         |                                    |     |     | CDM |      | theMATH-2021dataset,collectedsuppliedbyiFLYTEKCo.,Ltd., |     |     |     |
| positive,sothat                                 | 𝜕FCDM   | >0.Eq.(8)canbeusedtoinferstudents’ |     |     |     |      |                                                         |     |     |     |
|                                                 | 𝜕𝜙𝑢(𝒑𝑢) |                                    |     |     |     |      | whichiscollectedfromtheiFLYTEKLearningMachine4.They     |     |     |     |
performanceonexercisesinboththesourceandtargetdomains.
haveoverlappingstudentswhiletheirexerciseshavenooverlap.
Finally,weusethepopularcross-entropylossfunctiontoopti-
|     |     |     |     |     |     |     | • Junyi5[2]containsstudentonlinelearninglogsonmathematical |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- |
mizethewholemodelbyminimizingthedifferencebetweenthe
exerciseswhichiscrawledfromaChineseonlinelearningplat-
| predictedprobability𝑦ˆ |     |     | andthetrueresponse𝑦 |     | .   |     |                                                       |     |     |     |
| ---------------------- | --- | --- | ------------------- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- |
|                        |     | 𝑢𝑣  |                     |     | 𝑢𝑣  |     | form.NowadaysJunyiiswidelyusedintheevaluationofonline |     |     |     |
educationtasks[10,21].Werandomlyselect10,000students’
∑︁
| L=− |     | (𝑦 𝑢𝑣 | log𝑦ˆ 𝑢𝑣+(1−𝑦 |     | 𝑢𝑣)log(1−𝑦ˆ 𝑢𝑣)). | (9) |     |     |     |     |
| --- | --- | ----- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- |
exercisingrecordsfromJunyiforexperiments.
(𝑢,𝑣,𝑦𝑢𝑣)∈𝐿
|     |     | S   |     |     |     |     | • ASSISTments-2012-2013(ASSIST)6isanopendatasetcollected |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
Byoptimizingwiththeaboveloss,theseinputtraitsofthestudent bytheASSISTmentsonlinetutoringsystems,whichhasbecome
andtheexerciseinEq.(8),i.e.,𝒑𝑢 ,𝒅𝑣 and𝛽 ,canbejointlyrefined popularbenchmarkdatasetsforcognitivediagnosis.Weran-
𝑣
servingasthediagnosticresultsofstudentsandexercises. domlyselectabout5,000exercisesandtheirrelatedrecords.
Takingthestudenttrait𝜙 Allthedatasetsprovidestudentexercisingrecordsandexercise-
| 4.3.3 InstantiatingtheTechCD. |     |     |     |     |     | 𝑢(𝒑𝑢) |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
conceptcorrelations,whereeachexerciseassociatesoneknowledge
| andexercisetraits𝜙 |     | 𝑣(𝒅𝑣)and𝛽 |     | 𝑣 asinputfactors,wespecifythe |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
diagnosticadaptorF (·)inEq.(8)ofTechCDwithIRT,MIRT concept.Besides,AMandCMprovidetheexercises’contents,and
CDM
andNeuralCDasfollows: Junyiprovidestheconceptualprerequisiteandsimilarityrelations
IRT[9]takestheunidimensionalstudentproficiency,exercise labeledbyexperts.Eachdatasetistreatedasadomain,i.e.,the
difficulty and discrimination as input. To specify with IRT, we sourceortargetdomain.Amongthem,thereisnooverlapbetween
thestudentsintheJunyiandASSISTdatasetsandthoseinthe
| project𝒑𝑢 | and𝒅𝑣 | toscalars𝑝 | 𝑢 and𝑑 | 𝑣   | respectivelybysetting𝜙 | 𝑢   |     |     |     |     |
| --------- | ----- | ---------- | ------ | --- | ---------------------- | --- | --- | --- | --- | --- |
MATHdataset.Foreachdataset,wereserveonlythefirstattemptof
| and𝜙 𝑣 asmeanpooling.TheF |     |     |     | (·)isalogistic-likefunction: |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
CDM
𝑦ˆ =sigmoid(𝛽 𝑣·(𝑝 𝑢−𝑑 𝑣)). eachexerciseforeachdatasettoensurethattheattributestateofstu-
𝑢𝑣
MIRT[30]modelstheinteractionbetweenmultidimensional dentsisstaticfollowingthe[10,41].Weevaluatetheperformance
studentproficiency𝒑𝑢 andexercisedifficulty𝒅𝑣 usingalogistic- ofDZCDonthetargetdomainusingtherefinedmodeltrained
inthesourcedomain.Wespliteachsourcedomain’sdatasetby
| likefunction.Wesettheoutputdimensionsof𝜙 |     |     |     |     | 𝑢 and𝜙 𝑣 | as𝐷 >1. |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | -------- | ------- | --- | --- | --- | --- |
randomlyselectingtwohistoricalinteractionsfromeachstudent’s
| TheF | (·)isshownas:𝑦ˆ |     | 𝑢𝑣 =sigmoid(𝒑 |     | 𝑇 𝑢𝒅𝑣+𝛽 𝑣). |     |     |     |     |     |
| ---- | --------------- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
CDM
NeuralCD[41]directlytakesstudentproficiency𝒑𝑢 andexer- logsforvalidation,withtheremainingdataservingasthetraining
cisedifficultyasinput.Additionally,itrequiresmaskingtheirrel-
4
| evantknowledgeproficiencybyavector𝑸𝑣 |     |     |     |     | ={0,1}|C|×1where |     | h t t p s : / / x x j .x | u n fe i. cn /                                        |     |     |
| ------------------------------------ | --- | --- | --- | --- | ---------------- | --- | ------------------------ | ----------------------------------------------------- | --- | --- |
|                                      |     |     |     |     |                  |     | 5 h t t p s : / / p sl c | d a ta sh o p .web.cmu.edu/DatasetInfo?datasetId=1198 |     |     |
𝑞 𝑣,𝑐 =1ifexercise𝑣associatesconcept𝑐and𝑞 𝑣,𝑐 =0otherwise.C 6https://drive.google.com/file/d/1cU6Ft4R3hLqA7G1rIGArVfelSZvc6RxY/view
988

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
Table2:SomedetailedstatisticsoftheKCG. • Random:Therandommethodpredictsthestudents’scoresran-
#Concept 2,594 domlyfrom𝑈𝑛𝑖𝑓𝑜𝑟𝑚(0,1).
Entity #Exercise 15,199 • Oracle:Theoraclebaselineistrainedwiththestudent-exercise
#Total 17,793 interactiverecordsofbothsourceandtargetdomains.Hence,it
shouldperformbetterthanothercomparedmethods.
Relation #Total 5
• NLP-based:Somerelatedresearches[22,35]utilizeexercises’tex-
#Conceptualdependency 7,926
tualcontentsasanintermediaryofthesourceandtargetdomain
Triple #Exercise-conceptassociation 15,469
forstudentperformancepredictions.Thus,weadoptBert[6]
#Total 23,395
astheencodertoencodeexercises’textualcontentstogener-
atetheirembeddings.ToimplementtheNLP-baseddiagnosis
set,similartothewidelyusedleave-one-out evaluation[14,31].
method,weuselearnableembeddingsasstudentproficiencyand
Besides,totraintheOraclemodels(Section5.2),wealsosplitthe
introducetwofunctionstotransformtextualcontentfeatures
targetdomain’sdatasetintotraining(70%),validation(10%),and
intoexercises’difficultiesanddiscrimination.
testsets(20%),similarto[54].Thebasicstatisticsofthedatasets
• GCN-based:Weaddabaselinethatutilizesonlythelast-layer
arepresentedinTable1.
output asentities’ embeddingsand does notdifferentiatebe-
5.1.2 KnowledgeConceptGraphConstruction. Tobridgeexercises
tweenthedifferentrelationsintheKCGforcomparison.
acrossdifferentdomains,itneedstotailoraunifiedknowledge
conceptgraph(KCG)linkingeachdomain.Forthispurpose,we 5.3 EvaluationMetricsandOtherSettings
adoptahierarchicalmathematicalKCG(abbreviatedasMathKCG) 5.3.1 Metrics. Toevaluatemodelperformance,weadoptdiffer-
toconnectalldomains(i.e.,allthedatasets).Specifically,MathKCG entmetricsfromtheperspectivesofclassificationandregression
ispublishedbytheonlineeducationplatform,i.e.,Luna7.Itcov- followingthe[10].Fromtheclassificationperspective,astudentan-
ers39.5%knowledgeconceptsinourdatasetsandprovidestwo sweringincorrectlyorcorrectlycanberepresentedasanegative(0)
significanttypesofconceptualrelations,i.e.,hierarchy[21]and orpositive(1)instancerespectively.Thus,weuseAccuracy(ACC)
similarity[26]relations.Wefirstaligneachexercise-relatedcon- and Area Under the ROC Curve (AUC) for measuring. From the
ceptindatasetsandconceptsinMathKCGbasedonconceptual regressionperspective,weselectRootMeanSquareError(RMSE)
names.Then,fortheisolatedconceptsineachdatasetthatcannot toquantifythedistancebetweenthepredictedscore(i.e.,theprob-
belinkedtoMathKCG,webuildconceptualsimilarandprerequisite abilitythatastudentanswerscorrectly)andtheactualone.
relations[3]betweenthemviaexploitingstudentperformancelogs 5.3.2 ImplementationDetails. ForthosemodelsthatemployNeural-
usingthestatisticalmethod[10].Hereby,basedonthegenerated CDandMIRTasdiagnosticfunctions,wesetthedimensionsof
relations, the MathKCG, and those relations provided by Junyi, studentandexercisevectorsasthenumberofdiagnosedknowledge
eachconceptcanbelinkedtoaKCG.Additionally,theexercises concepts |C|,similarto[41].Thedimensionsofneuralnetwork
arelinkedtotheirassociatedknowledgeconceptintheKCG.The layersare1024and512forallmodelswithNeuralCDdiagnostic
finalKCGincludesconceptandexerciseentities,andfourtypes function.RegardingtheGCNlayers,underthe"AMassource"set-
ofconceptualrelations(i.e.,hierarchy-in-MathKCG,similarity-in- ting,weuse5layersfor𝐿andadiscardingparameter𝜆of3.Under
MathKCG,theconstructedsimilarityandprerequisiterelationsvia the"CMassource"setting,weuse5layersfor𝐿andadiscarding
ourdatasets)aswellastheexercise-conceptassociationrelations. parameter𝜆of2.Fortraining,allnetworkparametersareinitialized
We conduct all experiments on the same KCG. The detailed withXavierinitialization[11].Furthermore,wesetthemini-batch
statisticsoftheKCGarepresentedinTable2. sizeas256andthelearningrateas0.0005foreachmodel.Each
modelisimplementedbyPyTorch[29]andoptimizedbyAdam
5.2 Baselines
optimizer[20].AllexperimentsarerunonaLinuxserverwithtwo
Toverifytheeffectivenessofourmodel,wepresentthreeimplemen-
3.00GHzIntelXeonGold5317CPUsandoneTeslaA100GPU.The
tationsbasedonTechCDframeworkthatcombinetypicaldiagnosis
codeisavailableathttps://github.com/bigdata-ustc/TechCD.
methods.Inparticular,weimplementTech-IRT,Tech-MIRTand
Tech-NeuralCDfollowingIRT,MIRTandNeuralCD,respectively. 5.4 StudentPerformancePrediction(RQ1)
• IRT[9]:IRTmodelsunidimensionalstudentsandexercises’fea- ToanswerRQ1,wecomparetheperformanceofourmodelwithsev-
tureswithalogistic-likefunction. eralbaselinesonthedomain-levelzero-shotstudentperformance
• MIRT [30]: As the multidimensional extension of IRT, MIRT predictiontask.WeswitchCMandAMdatasetsasthetargetdo-
modelsmultipleknowledgeproficiencyofstudentsandexercises. mainsincetheirstudentsoverlap.ItisworthmentioningthatJunyi
• NeuralCD[41]:NeuralCDisoneofthemostpopulardeeplearning- andASSISTareusedinSection5.6todemonstratehowTechCD
basedCDmethods,whichmodelshigh-orderandcomplexstudent- utilizesout-domaindatasetsfromotherplatformsfortheDZCD
exerciseinteractionfunctionswithamultilayerperceptron(MLP). task,astheyarecollectedfromdifferentplatforms.Theoverall
predictionperformanceisreportedinTable3.Thecombination
Weselectaseriesofbaselinesforcomparison.Amongthem,the
ofS-CM(AM)andT-AM(CM)denotesCM(AM)asthesource
randomandoraclemethodsindicatethelowerandupperboundsof
domainfortrainingandAM(CM)asthetargetdomainfortesting.
performance,followingtheprevioussetups[54].Foreachbaseline
Wehavethefollowingobservations:(1)Fordifferentdiagnostic
(excludingRandom),wealsoselectIRT,MIRTandNeuralCDas
implementations(i.e.,IRT,MIRTandNeuralCDasDiagnosticfunc-
theirdiagnosticfunctions.Thedetailsarelistedasfollows:
tion), our proposed TechCD framework almost outperforms all
7https://luna.bdaa.pro baselinemodels(includingRandom,NLP-basedandGCN-based
989

| SIGIR’23,July23–27,2023,Taipei,Taiwan |     |     |     |     |     |     |     |     |     |     |     | WeiboGaoetal. |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
Table3:Performancecomparison.Thebestzero-shotstudentperformancepredictionishighlightedinbold,therunner-upis
underlined,and↑(↓)meansthehigher(lower)scorethebetterperformance,thesameasbelow.*indicatestheoracleresult.
|     |     |     |     | IRT |     |     | MIRT |     |     | NeuralCD |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | -------- | --- | --- | --- |
Random
Dataset Metric Oracle NLP GCNTechCD Oracle NLP GCNTechCD Oracle NLP GCN TechCD
ACC(%)↑ 77.89∗ 59.84 56.72 73.83∗ 56.44 56.74 74.65∗ 56.44 57.05 50.13
|     | S-CM |     |        |     | 63.45 |        |     | 64.73 |        |     | 57.06 |     |     |
| --- | ---- | --- | ------ | --- | ----- | ------ | --- | ----- | ------ | --- | ----- | --- | --- |
|     |      |     | 84.98∗ |     |       | 79.26∗ |     |       | 81.07∗ |     |       |     |     |
AUC(%)↑ 65.32 56.62 67.42 65.52 56.60 68.90 57.09 57.44 53.68 50.14
T-AM
RMSE(%)↓ 38.91∗ 47.98 50.75 47.59 48.40∗ 48.30 50.79 47.06 41.17∗ 49.69 50.72 49.49 57.70
ACC(%)↑ 77.67∗ 55.88 56.92 57.72 74.07∗ 55.88 56.92 57.78 74.34∗ 55.88 56.80 56.99 49.91
S-AM
AUC(%)↑ 85.50∗ 50.68 56.62 81.16∗ 56.62 59.02 81.61∗ 53.67 52.40 49.89
|     | T-CM |     |     |     | 58.99 |     | 60.56 |     |     | 57.55 |     |     |     |
| --- | ---- | --- | --- | --- | ----- | --- | ----- | --- | --- | ----- | --- | --- | --- |
RMSE(%)↓ 39.08∗ 53.21 54.46 52.85 47.93∗ 48.52 50.50 52.85 41.52∗ 49.87 50.72 49.57 57.78
ACC RMSE Table4:PerformanceofTechCDtrainedondifferentsettings.
True
|     | DS    |            | True     |      |       |     |          |     |     |                |             |          |       |
| --- | ----- | ---------- | -------- | ---- | ----- | --- | -------- | --- | --- | -------------- | ----------- | -------- | ----- |
|     |       |            |          |      |       |     | Training |     |     | Target ACC(%)↑ | AUC(%)↑     | RMSE(%)↓ |       |
|     | False |            | DS False |      |       |     |          |     |     |                |             |          |       |
|     |       |            |          |      |       |     | Random   |     |     | AM             | 50.13 50.14 |          | 57.70 |
|     |       | True False |          | True | False |     |          |     |     |                |             |          |       |
|     |       | DE         |          |      |       |     | CM       |     |     | AM             | 57.06 53.68 | 49.49    |       |
DE
Figure3:TheACCandRMSEcomparisonsonS-AMandT- (LA)Junyi AM 53.71 50.49 49.80
CM.Thedarker(lighter)meansthebetterforACC(RMSE). (LA)Assist AM 54.83 49.77 49.85
|     |     |     |     |     |     |     | (ASD)CM+Junyi |     |     | AM  | 56.60 52.10 |     | 49.84 |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ----------- | --- | ----- |
models)onbothCMandAMtargetdomains,whichindicatesthe (ASD)CM+Assist AM 51.95 49.69
57.08
effectivenessofTechCDonpredictingstudentperformanceunder (ASD)CM+Junyi+Assist AM 56.73 52.11 49.57
thecold-startsetting.(2)BothGCN-basedandTechCDemploythe
knowledgeconceptgraphlinkingbothsourceandtargetdomains.
𝐿 canbeusedtojointlytrainthemodelwithEq.(2)as:
O
However,GCN-basedmethodsareunabletodiscardbottom-layer
|     |     |     |     |     |     |     |     |     | Θ∗=argminL(𝑦(𝐿 |     | +𝐿 ),G). |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | ---- |
informationanddiscriminatedifferentrelationsintheKCG.Incon- S O
Θ
trast,TechCDoutperformsGCN-basedmethods,whichpositively
|     |     |     |     |     |     |     | 5.6.2 | Limited | Access | (LA). In the | setting, student | performance |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ------------ | ---------------- | ----------- | --- |
supportsitseffectiveness.
recordsareunavailableduetoprivacyprotectionpolicies.Toad-
Inthefollowingparts,weprimarilypresenttheexperimental
dressthisscenario,theout-domainOareintroducedtorefinethe
resultsofTech-NeuralCDastherepresentativeones,sinceother KCGbyreplacingsourcedomain’sdatasets𝐿 without-domain
S
diagnosisfunctionscanbeabstractedasthespecialcasesofNeu-
|            |                                     |     |     |     |     |     | datasets𝐿 | inEq.(2)as: |                |     |       |     |      |
| ---------- | ----------------------------------- | --- | --- | --- | --- | --- | --------- | ----------- | -------------- | --- | ----- | --- | ---- |
| ralCD[41]. |                                     |     |     |     |     |     |           | O           |                |     |       |     |      |
|            |                                     |     |     |     |     |     |           |             | Θ∗=argminL(𝑦(𝐿 |     | ),G). |     | (11) |
| 5.5        | Bottom-LayerDiscardingAnalysis(RQ2) |     |     |     |     |     |           |             |                |     | O     |     |      |
Θ
TheTechCDframeworkreliesonthebottom-layerdiscardingop- Table4liststheperformanceofTech-NeuralCD,indicatingthe
eration[54]togeneratetransferableembeddings.Werefertothe followingobservations.IntheASDsetting,theout-domaindatasets
operationofdiscardingbottom-layerembeddingofstudentand canpartlyimprovethepredictionperformanceofTechCD.IntheLA
exerciseembeddingsasDSandDE,respectively.Toevaluatethe setting,withtheout-domaindatasets,TechCDcangetapromising
impactofthisoperation,weperformvariousexperimentswith performancecomparedwithrandompredictions.Thesefindings
differentcombinationsofDSandDE.ThecomparisonsofACCand confirmtheKCGcanabsorbout-domaindatasetseffectively.
RMSEscoresunderthesettingofS-AMandT-CMarevisualized
inFigure3.Theexperimentalresultsindicatethatthebestperfor- 5.7 PopularApplicationsofTechCD(RQ4)
manceisachievedbyonlydiscardingthebottom-layeroutputfrom
TheaboveexperimentshaveprovedthatTechCDcancompletethe
theKCGforstudents(DS),highlightingtheeffectivenessofextract-
DZCDtaskeffectively.Inthispart,wedemonstratetwospecial
ingtransferableinformation.However,whenbothDSandDEare applicationsofourTechCDthatareinneedofindustrialpractice.
usedsimultaneously,theperformanceisweakened,emphasizing
theimportanceofmaintainingspecificpatternsforexercises. 5.7.1 DiagnosticReportGeneration. Providingdiagnosticreports
tostudentsviatheCDmethodisoneofthemosttypicalintelli-
5.6 ImprovingwithOut-DomainDatasets(RQ3)
gentapplicationsinintelligenteducation,whichcanhelpstudents
ThetailoredKCGcanlinkdifferentdomainsincludingthosewithin understandtheirlearningprocess.Traditionaldiagnosismethodsdi-
thesameplatformandthoseacrossplatforms.Thepreviousexperi- agnosestudents’proficiencyonknowledgeconceptslimitedinthe
mentsfocusonevaluatingperformancewithinsourceandtarget
sourcedomain,whileourTechCDcanfurtherinferstudents’cog-
| domains | that | share overlapping | students. | This | part shows | how |     |     |     |     |     |     |     |
| ------- | ---- | ----------------- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
nitivestatesinthetargetdomain.Werandomlyselectonestudent
powerfulisTechCDforutilizingout-domaindatasetsfromother
intheCMdatasetstogenerateherdiagnosticreportsusingTech-
platformsundertwotypicalcold-startscenarios[54]. NeuralCDandtraditionalNeuralCDtrainedontheCMdataset.
Inthescenario,student WealsosampleasubgraphofKCGwhichcoverssomeknowledge
5.6.1 AccessibleStudentRecords(ASD).
performancerecords𝐿 inthesourcedomainSandout-domain conceptsofCMandJunyiwithsimilarityandprerequisiterelations.
S
records𝐿 inthetargetdomainOarebothavailable.Thus,𝐿 and Figure4(a)and(b)presentdiagnosticreportsofbothmodelsand
|     | O   |     |     |     |     | S   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
990

LeveragingTransferableKnowledgeConceptGraphEmbeddingforCold-StartCognitiveDiagnosis SIGIR’23,July23–27,2023,Taipei,Taiwan
Tech-NueralCD NeuralCD similarity prerequisite Table5:ExerciserecommendationofTechCD.
1 Mastery
5 0
0 1
.
. .
5
8 0
2
6
1
3
4
5 1.0 S-CMT-AM ○1 ○2 ○3 ○4 ○5 ○6 ○7 ○8 ○9 ○10
0.3 Exerciseid 232 1,632 2,432 30 123 2,003 3,020 175 220 250
0.0 2 0.5
8 Mastery(%) 67.23 38.24 40.07 23.00 48.63 57.30 84.33 54.27 48.24 57.78
7
4 3 CM Junyi 0.0 Difficulty(%) 50.20 51.30 49.93 50.21 49.98 50.00 50.03 50.10 49.99 49.93
(a) Diagnostic Report (b) Cognitive graph of Tech-NeuralCD Performance ✓ × × × ✓ ✓ ✓ × ✓ ✓
1. absolute value 5. negative number word problems thatcanhelpincreaseherengagementwiththematerial.(2)For
2. absolute value multiply 6. absolute values’ meaning
3. absolute value divide 7. absolute value add sub exercisesthatthestudentanswerscorrectly(incorrectly),theprofi-
4. adding negative numbers 8. comparing negative values ciencyofthecorrespondingconceptisalmosthigher(lower)than
Figure4:Theexampleofdiagnosticreports. theexercise’sdifficulty,indicatingthatstudentsanswercorrectly
thecognitivegraphofTech-NeuralCDrespectively.Fromthefigure, whentheirproficiencymeetsthedifficulty.ItconfirmsTechCD’s
weobservethat:(1)Forthemasterylevelsofknowledgeconcepts diagnosesareeffectiveinthecold-startdomain.
(1,2and3)inCM,Tech-NeuralCDandNeurcalCDcanoutputsimi-
6 CONCLUSION
lardiagnosisresults,indicatingthatbothmodelscanperformwell
Thispaperpresentsastudyonthedomain-levelzero-shotcogni-
onin-domaindatasets.(2)Forthoseknowledgeconcepts(4and5)
tivediagnosis(DZCD)task.DZCDisanimportanttaskforthe
sampledfromJunyi(asacold-startdomain),NeuralCDisunableto
lackofstudentbehaviordatainthetargetdomainduetotheab-
provideadiagnosis,whileTech-NeuralCDisstillabletoperform
senceofstudent-exerciseinteractionsorunavailabilityofexercising
effectively.(3)InthecognitivegraphofTech-NeuralCD,thedeeper
recordsfortraining.Totacklethis,weproposeageneralandtrans-
thecoloroftheconceptentity,thehigheritscognitivelevel.We
ferableframeworkTechCDthatutilizesapedagogicalknowledge
findthediagnosisresultsreasonableandinterpretable.Forexam-
conceptgraph(KCG)toconnectdifferentdomainsandpropagate
ple,thestudent’sproficiencyonconcepts3and4ispoor,which
students’universalcognitivestates.Thelearnedstudentembed-
isreflectedinherpoormasteryofconcept5.Thisisexpectedas
dingsbyTechCDaretransferable,whiletheexerciseembeddings
masteringconcepts3and4areprerequisitesforlearningconcept5.
aredomain-specific,enablingTechCDtoperformdomain-adaptive
Additionally,themasterylevelsonconcepts6and7aresimilaras
zero-shotcognitivediagnosisinthetargetdomain.Finally,exten-
theybelongtothesametopic(i.e.,absolutevalue).
siveexperimentsonreal-worlddatasetsnotonlyprovethatTechCD
5.7.2 ExerciseRecommendation. Thediagnosticresultscanbeuti-
caneffectivelymakethecognitivediagnosistaskforazero-shot
lizedtosuggestappropriateexercisestostudents,ratherthanre-
domainandoutperformseveralalternativebaselines,butalsoshow
lyingontheirownsearchefforts.Aproperrecommendersystem
thesuperiorapplicationpotentialsuchaspersonalizedexerciserec-
generallytakesintoaccounttwokeyobjectives:(O1:smoothness)
ommendationofTechCD.Inourfutureresearch,wewillfocuson
thedifficultylevelsofaseriesofrecommendationsshouldavoid
developingmoreadvancedmethodsforconstructingeducational
drasticvariationsasstudentslearnknowledgegradually[53];(O2:
KCGsthatcanbetterconnectdifferentdomains.Additionally,we
engagement)therecommendationsshouldnotbetoochallengingor
plantoexploremoresophisticatedapproachesforintegratingcon-
easytokeepstudents’enthusiasm[18].Forthesegoals,weimple-
mentasimpleyeteffectivestrategy8torecommend𝑥 exercisesfor ceptualrelationshipstofurtherimproveTechCD’sperformancein
theDZCDscenario.Ultimately,wehopethatourworkwillinspire
eachstudent.Concretely,witharefinedCDM,wefirstpredicteach
andinformfuturestudiesandapplicationsinthisarea.
student’sperformanceoneachexerciseasEq.(8).Allexercisescan
bedividedintotwosetsthatanswercorrectly(positivesamples)
Acknowledgements.Thisresearchwaspartiallysupportedby
grantsfromtheNationalKeyResearchandDevelopmentProgram
ornot(negativesamples)accordingtopredictionresults.Then,we
sample 𝑥 exercisesfromeachofthepositiveandnegativesamples. ofChina(No.2021YFF0901003),NationalNaturalScienceFounda-
2 tionofChina(No.62202443),andOpenResearchFundoftheState
Foreachsampling,werequiretheselectedexercise’sdifficultyto
KeyLaboratoryofCognitiveIntelligence(iED2022-002).
beclosetoathreshold(0.5inthispaper)toensurethesmoothness
objective.Finally,wecangettherecommendationlistsforeach
REFERENCES
student,whichsatisfytheaboveobjectives.
Weconductrecommendationsonthechallengingtargetdomain [1] HaoyangBi,HaipingMa,ZhenyaHuang,YuYin,QiLiu,EnhongChen,YuSu,
andShijinWang.2020.QualitymeetsDiversity:AModel-AgnosticFramework
thattraditionalCDMsareunabletohandle.Table5liststenexercise forComputerizedAdaptiveTesting.In2020IEEEInternationalConferenceonData
recommendationsonT-AMforarandomlyselectedstudentusing Mining(ICDM).IEEE,42–51.
[2] Haw-ShiuanChang,Hwai-JungHsu,andKuan-TaChen.2015.ModelingExercise
therefinedTech-NeuralCDmodeltrainedonS-CMdataset.The
RelationshipsinE-Learning:AUnifiedApproach..InEDM.532–535.
tablealsoincludesthediagnosedexercisedifficultiesandstudent [3] PengheChen,YuLu,VincentWZheng,andYangPian.2018.Prerequisite-driven
masterylevelsoftheassociatedconcepts,aswellasthestudent’s deepknowledgetracing.In2018IEEEInternationalConferenceonDataMining
trueperformanceontheexercisesasrecordedintheT-AMdataset.
(ICDM).IEEE,39–48.
[4] ShuoChenandThorstenJoachims.2016.Predictingmatchupsandpreferences
Wecanseethat:(1)Therecommendedexercisesaretailoredtothe incontext.InProceedingsofthe22ndACMSIGKDDInternationalConferenceon
student’sproficiency,neithertooeasynortoodifficult.Someof KnowledgeDiscoveryandDataMining.775–784.
[5] JimmyDeLaTorre.2009. DINAmodelandparameterestimation:Adidactic.
themwillchallengethestudent,whileotherswillserveas"gifts" Journalofeducationalandbehavioralstatistics34,1(2009),115–130.
[6] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2018.Bert:
8TechCDcansupportmanycomplexandpopularexerciserecommendationapproaches Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding.arXiv
like[1,18],thispartusesthesimplerecommendationmethodasanexample. preprintarXiv:1810.04805(2018).
991

SIGIR’23,July23–27,2023,Taipei,Taiwan WeiboGaoetal.
[7] NanDingandRaduSoricut.2017.Cold-startreinforcementlearningwithsoftmax 25thannualInternationalACMSIGIRconferenceonResearchanddevelopmentin
policygradient.AdvancesinNeuralInformationProcessingSystems30(2017). informationretrieval.253–260.
[8] HenryCEllis.1965.Thetransferoflearning.(1965). [33] RobinSchmuckerandTomMMitchell.2022.TransferableStudentPerformance
[9] SusanEEmbretsonandStevenPReise.2013.Itemresponsetheory.Psychology ModelingforIntelligentTutoringSystems.arXivpreprintarXiv:2202.03980(2022).
Press. [34] YiShang,HongchiShi,andSu-ShingChen.2001. Anintelligentdistributed
[10] WeiboGao,QiLiu,ZhenyaHuang,YuYin,HaoyangBi,Mu-ChunWang,Jianhui environmentforactivelearning.JournalonEducationalResourcesinComputing
Ma,ShijinWang,andYuSu.2021.Rcd:Relationmapdrivencognitivediagnosis (JERIC)1,2es(2001),4–es.
forintelligenteducationsystems.InProceedingsofthe44thInternationalACM [35] YuSu,QingwenLiu,QiLiu,ZhenyaHuang,YuYin,EnhongChen,ChrisDing,
SIGIRConferenceonResearchandDevelopmentinInformationRetrieval.501–510. SiWei,andGuopingHu.2018.Exercise-enhancedsequentialmodelingforstu-
[11] XavierGlorotandYoshuaBengio.2010.Understandingthedifficultyoftraining dentperformanceprediction.InProceedingsoftheAAAIConferenceonArtificial
deepfeedforwardneuralnetworks.InProceedingsofthethirteenthInternational Intelligence,Vol.32.
conferenceonartificialintelligenceandstatistics.JMLRWorkshopandConference [36] Shan-YunTeng,JundongLi,LoPang-YunTing,Kun-TaChuang,andHuanLiu.
Proceedings,249–256. 2018.Interactiveunknownsrecommendationine-learningsystems.In2018IEEE
[12] MargaretGrogan.1999.Equity/equalityissuesofgender,race,andclass.Educa- InternationalConferenceonDataMining(ICDM).IEEE,497–506.
tionalAdministrationQuarterly35,4(1999),518–536. [37] ShiweiTong,JiayuLiu,YutingHong,ZhenyaHuang,LeWu,QiLiu,WeiHuang,
[13] XiangnanHe,KuanDeng,XiangWang,YanLi,YongdongZhang,andMeng EnhongChen,andDanZhang.2022.IncrementalCognitiveDiagnosisforIntelli-
Wang.2020.Lightgcn:Simplifyingandpoweringgraphconvolutionnetworkfor gentEducation.InProceedingsofthe28thACMSIGKDDConferenceonKnowledge
recommendation.InProceedingsofthe43rdInternationalACMSIGIRconference DiscoveryandDataMining.1760–1770.
onresearchanddevelopmentinInformationRetrieval.639–648. [38] EmikoTsutsumi,RyoKinoshita,andMaomiUeno.2021.Deep-IRTwithIndepen-
[14] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng dentStudentandItemNetworks.InternationalEducationalDataMiningSociety
Chua.2017.Neuralcollaborativefiltering.InProceedingsofthe26thInternational (2021).
conferenceonworldwideweb.173–182. [39] KurtVanLehn.2011. Therelativeeffectivenessofhumantutoring,intelligent
[15] MinlieHuang,XiaoyanZhu,andJianfengGao.2020. Challengesinbuilding tutoringsystems,andothertutoringsystems. Educationalpsychologist46,4
intelligentopen-domaindialogsystems.ACMTransactionsonInformationSystems (2011),197–221.
(TOIS)38,3(2020),1–32. [40] ManasiVartak,ArvindThiagarajan,ConradoMiranda,JeshuaBratman,andHugo
[16] WenbingHuang,YuRong,TingyangXu,FuchunSun,andJunzhouHuang. Larochelle.2017.Ameta-learningperspectiveoncold-startrecommendations
2020.Tacklingover-smoothingforgeneralgraphconvolutionalnetworks.arXiv foritems.Advancesinneuralinformationprocessingsystems30(2017).
preprintarXiv:2008.09864(2020). [41] FeiWang,QiLiu,EnhongChen,ZhenyaHuang,YuyingChen,YuYin,ZaiHuang,
[17] XiaoqingHuang,QiLiu,ChaoWang,HaoyuHan,JianhuiMa,EnhongChen,Yu andShijinWang.2020. Neuralcognitivediagnosisforintelligenteducation
Su,andShijinWang.2019.ConstructingEducationalConceptMapswithMultiple systems.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.34.
RelationshipsfromMulti-SourceData.In2019IEEEICDM.IEEE,1108–1113. 6153–6161.
[18] ZhenyaHuang,QiLiu,ChengxiangZhai,YuYin,EnhongChen,WeiboGao, [42] HaoWang,EnhongChen,QiLiu,TongXu,DongfangDu,WenSu,andXiaopeng
andGuopingHu.2019.Exploringmulti-objectiveexerciserecommendationsin Zhang.2018.Aunitedapproachtolearningsparseattributednetworkembedding.
onlineeducationsystems.InProceedingsofthe28thACMInternationalConference In2018IEEEInternationalConferenceonDataMining(ICDM).IEEE,557–566.
onInformationandKnowledgeManagement.1261–1270. [43] HaoWang,DefuLian,HanghangTong,QiLiu,ZhenyaHuang,andEnhong
[19] YujiaHuo,DerekFWong,LionelMNi,LidiaSChao,andJingZhang.2020.Knowl- Chen.2021.Hypersorec:Exploitinghyperbolicuseranditemrepresentations
edgemodelingviacontextualizedrepresentationsforLSTM-basedpersonalized withmultipleaspectsforsocial-awarerecommendation.ACMTransactionson
exerciserecommendation.InformationSciences523(2020),266–278. InformationSystems(TOIS)40,2(2021),1–28.
[20] DiederikPKingmaandJimmyBa.2014.Adam:Amethodforstochasticopti- [44] HaoWang,TongXu,QiLiu,DefuLian,EnhongChen,DongfangDu,HanWu,
mization.arXivpreprintarXiv:1412.6980(2014). andWenSu.2019. MCNE:Anend-to-endframeworkforlearningmultiple
[21] JiatongLi,FeiWang,QiLiu,MengxiaoZhu,WeiHuang,ZhenyaHuang,Enhong conditionalnetworkrepresentationsofsocialnetwork.InProceedingsofthe25th
Chen,YuSu,andShijinWang.2022. HierCDF:ABayesianNetwork-based ACMSIGKDDInternationalConferenceonKnowledgeDiscovery&DataMining.
HierarchicalCognitiveDiagnosisFramework.InProceedingsofthe28thACM 1064–1072.
SIGKDDConferenceonKnowledgeDiscoveryandDataMining.904–913. [45] MinjieWang,DaZheng,ZihaoYe,QuanGan,MufeiLi,XiangSong,Jinjing
[22] QiLiu,ZhenyaHuang,YuYin,EnhongChen,HuiXiong,YuSu,andGuopingHu. Zhou,ChaoMa,LingfanYu,YuGai,etal.2019. Deepgraphlibrary:Agraph-
2019.Ekt:Exercise-awareknowledgetracingforstudentperformanceprediction. centric,highly-performantpackageforgraphneuralnetworks.arXivpreprint
IEEETransactionsonKnowledgeandDataEngineering33,1(2019),100–115. arXiv:1909.01315(2019).
[23] QiLiu,RunzeWu,EnhongChen,GuandongXu,YuSu,ZhigangChen,andGuop- [46] ZhengyangWu,MingLi,YongTang,andQingyuLiang.2020.Exerciserecom-
ingHu.2018.Fuzzycognitivediagnosisformodellingexamineeperformance. mendationbasedonknowledgeconceptprediction.Knowledge-BasedSystems
ACMTransactionsonIntelligentSystemsandTechnology(TIST)9,4(2018),1–26. 210(2020),106481.
[24] YeLiu,HanWu,ZhenyaHuang,HaoWang,JianhuiMa,QiLiu,EnhongChen, [47] JieXu,ChengDeng,XinboGao,DinggangShen,andHengHuang.2017.Pre-
HanqingTao,andKeRui.2020.Technicalphraseextractionforpatentmining: dictingAlzheimer’sdiseasecognitiveassessmentviarobustlow-rankstructured
Amulti-levelapproach.In2020IEEEInternationalConferenceonDataMining sparsemodel.InIJCAI:proceedingsoftheconference,Vol.2017.NIHPublicAccess,
(ICDM).IEEE,1142–1147. 3880.
[25] NimaMirbakhshandCharlesXLing.2015.Improvingtop-nrecommendationfor [48] LinanYue,QiLiu,YichaoDu,YanqingAn,LiWang,andEnhongChen.2022.
cold-startusersviacross-domaininformation.ACMTransactionsonKnowledge DARE:Disentanglement-AugmentedRationaleExtraction.AdvancesinNeural
DiscoveryfromData(TKDD)9,4(2015),1–19. InformationProcessingSystems35(2022),26603–26617.
[26] HiromiNakagawa,YusukeIwasawa,andYutakaMatsuo.2019. Graph-based [49] SiZhang,HanghangTong,JiejunXu,andRossMaciejewski.2019.Graphconvo-
KnowledgeTracing:ModelingStudentProficiencyUsingGraphNeuralNetwork. lutionalnetworks:acomprehensivereview.ComputationalSocialNetworks6,1
In2019IEEE/WIC/ACMInternationalConferenceonWebIntelligence(WI).IEEE, (2019),1–23.
156–163. [50] HaoZhao,MingLu,AnbangYao,YurongChen,andLiZhang.2020.Learningto
[27] TuanNguyen.2015.Theeffectivenessofonlinelearning:Beyondnosignificant drawsightlines.InternationalJournalofComputerVision128(2020),1076–1100.
differenceandfuturehorizons.MERLOTJournalofonlinelearningandteaching [51] HaoZhao,MingLu,AnbangYao,YiwenGuo,YurongChen,andLiZhang.
11,2(2015),309–319. 2017.Physicsinspiredoptimizationonsemantictransferfeatures:Analternative
[28] LiangmingPan,ChengjiangLi,JuanziLi,andJieTang.2017.Prerequisiterelation methodforroomlayoutestimation.InProceedingsoftheIEEEconferenceon
learningforconceptsinmoocs.InProceedingsofthe55thAnnualMeetingofthe computervisionandpatternrecognition.10–18.
AssociationforComputationalLinguistics(Volume1:LongPapers).1447–1456. [52] HaoZhao,MingLu,AnbangYao,YiwenGuo,YurongChen,andLiZhang.2020.
[29] AdamPaszke,SamGross,FranciscoMassa,AdamLerer,JamesBradbury,Gregory Pointly-supervisedsceneparsingwithuncertaintymixture.ComputerVisionand
Chanan,TrevorKilleen,ZemingLin,NataliaGimelshein,LucaAntiga,etal.2019. ImageUnderstanding200(2020),103040.
Pytorch:Animperativestyle,high-performancedeeplearninglibrary.Advances [53] WayneXinZhao,WenhuiZhang,YulanHe,XingXie,andJi-RongWen.2018.
inneuralinformationprocessingsystems32(2019). Automaticallylearningtopicsanddifficultylevelsofproblemsinonlinejudge
[30] MarkDReckase.2009. Multidimensionalitemresponsetheorymodels. In systems.ACMTransactionsonInformationSystems(TOIS)36,3(2018),1–33.
Multidimensionalitemresponsetheory.Springer,79–112. [54] JianhuanZhuo,JianxunLian,LanlingXu,MingGong,LinjunShou,DaxinJiang,
[31] SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme. XingXie,andYinliangYue.2022.Tiger:TransferableInterestGraphEmbedding
2012.BPR:Bayesianpersonalizedrankingfromimplicitfeedback.arXivpreprint forDomain-LevelZero-ShotRecommendation.InProceedingsofthe31stACM
arXiv:1205.2618(2012). InternationalConferenceonInformation&KnowledgeManagement.2806–2816.
[32] AndrewISchein,AlexandrinPopescul,LyleHUngar,andDavidMPennock.
2002.Methodsandmetricsforcold-startrecommendations.InProceedingsofthe
992