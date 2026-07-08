Counterfactual Explanations and Algorithmic Recourses for
Machine Learning: A Review
SAHILVERMA,ComputerScienceandEngineering,UniversityofWashington,Seattle,UnitedStates
VARICH BOONSANONG, Computer Science and Engineering, University of Washington, Seattle,
UnitedStates
MINHHOANG,ComputerScienceandEngineering,UniversityofWashington,Seattle,UnitedStates
KEEGANHINES,ArthurAI,WashingtonDC,UnitedStates
JOHNDICKERSON,ArthurAI,WashingtonDC,UnitedStates
CHIRAGSHAH,UniversityofWashington,Seattle,UnitedStates
Machinelearningplaysaroleinmanydeployeddecisionsystems,ofteninwaysthataredifficultorimpos-
sible to understand by human stakeholders. Explaining, in a human-understandable way, the relationship
betweentheinputandoutputofmachinelearningmodelsisessentialtothedevelopmentoftrustworthy
machinelearningbasedsystems.Aburgeoningbodyofresearchseekstodefinethegoalsandmethodsof
explainabilityinmachinelearning.Inthisarticle,weseektoreviewandcategorizeresearchoncounterfactual
explanations,aspecificclassofexplanationthatprovidesalinkbetweenwhatcouldhavehappenedhadinput
toamodelbeenchangedinaparticularway.Modernapproachestocounterfactualexplainabilityinmachine
learningdrawconnectionstotheestablishedlegaldoctrineinmanycountries,makingthemappealingto
fieldedsystemsinhigh-impactareassuchasfinanceandhealthcare.Thus,wedesignarubricwithdesirable
propertiesofcounterfactualexplanationalgorithmsandcomprehensivelyevaluateallcurrentlyproposedal-
gorithmsagainstthatrubric.Ourrubricprovideseasycomparisonandcomprehensionoftheadvantagesand
disadvantagesofdifferentapproachesandservesasanintroductiontomajorresearchthemesinthisfield.
Wealsoidentifygapsanddiscusspromisingresearchdirectionsinthespaceofcounterfactualexplainability.
CCSConcepts:•Generalandreference→Surveysandoverviews;
AdditionalKeyWordsandPhrases:ExplainabilityinML,counterfactualexplanations,algorithmicrecourse,
interpretabilityinML
ACMReferenceFormat:
SahilVerma,VarichBoonsanong,MinhHoang,KeeganHines,JohnDickerson,andChiragShah.2024.Coun-
terfactualExplanationsandAlgorithmicRecoursesforMachineLearning:AReview.ACMComput.Surv.56,
12,Article312(October2024),42pages.https://doi.org/10.1145/3677119
Authors’ContactInformation:SahilVerma,ComputerScienceandEngineering,UniversityofWashington,Seattle,Wash-
ington,UnitedStates;e-mail:vsahil@cs.washington.edu;VarichBoonsanong,ComputerScienceandEngineering,Univer-
sityofWashington,Seattle,Washington,UnitedStates;e-mail:varicb@cs.washington.edu;MinhHoang,ComputerSci-
enceandEngineering,UniversityofWashington,Seattle,Washington,UnitedStates;e-mail:minh257@cs.washington.edu;
KeeganHines,ArthurAI,WashingtonDC,DistrictofColumbia,UnitedStates;e-mail:keegan.hines@gmail.com;John
Dickerson,ArthurAI,WashingtonDC,DistrictofColumbia,UnitedStates;e-mail:john@arthur.ai;ChiragShah,Univer-
sityofWashington,Seattle,Washington,UnitedStates;e-mail:chirags@uw.edu.
This work is licensed under a Creative Commons Attribution International 4.0 License.
©2024Copyrightheldbytheowner/author(s).
ACM0360-0300/2024/10-ART312
https://doi.org/10.1145/3677119
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:2 S.Vermaetal.
1 Introduction
Machine learning is increasingly accepted as an effective tool to enable large-scale automation
in many domains. In lieu of hand-designed rules, algorithms are able to learn from data to dis-
cover patterns and support decisions. Those decisions can, and do, directly or indirectly impact
humans;high-profilecasesincludeapplicationsincreditlending[301],talentsourcing[295],pa-
role[315],andmedicaltreatment[106].ThenascentFairness,Accountability,Transparency,and
Ethics (FATE) in machine learning community has emerged as a multi-disciplinary group of re-
searchersandindustrypractitionersinterestedindevelopingtechniquestodetectbiasinmachine
learningmodels,developalgorithmstocounteractthatbias,generatehuman-comprehensibleex-
planationsforthemachinedecisions,holdorganizationsresponsibleforunfairdecisions,etc.
Human-understandableexplanationsformachine-produceddecisionsareadvantageousinsev-
eralways.Forexample,focusingonausecaseofapplicantsapplyingforloans,thebenefitswould
include:
—Anexplanationcanbebeneficialtotheapplicantwhoselifeisimpactedbythedecision.For
example, it helps an applicant understand which of their attributes were strong drivers in
determiningadecision;
—Variousformsofexplanationscanserveasaproxyfortransparencyinthesystem,which
couldincreaseitstrustworthiness;
—Further, it can help an applicant challenge a decision if they feel an unfair treatment has
beenmetedout,e.g.,ifone’sracewascrucialindeterminingtheoutcome.Thiscanalsobe
usefulfororganizationstocheckforbiasintheiralgorithms;
—In some instances, an explanation provides the applicant with feedback that they can act
upontoreceivethedesiredoutcomeatafuturetime;
—Explanationscanhelpthemachinelearningmodeldevelopersidentify,detect,andfixbugs
andotherperformanceissues;
—Explanationshelpadheretolawssurroundingmachine-produceddecisions,e.g.,GDPR[68].
Explainability in machine learning is broadly about using inherently interpretable and trans-
parent models or generating post-hoc explanations for opaque models. Examples of the former
includelinear/logisticregression,decisiontrees,rulesets,andthelike.Examplesofthelatterin-
cluderandomforests,supportvectormachines(SVMs),andneuralnetworks.Post-hocexplanation
approaches can either be model-specific or model-agnostic. Explanations by feature importance
and model simplification are two broad kinds of model-specific approaches. Model-agnostic ap-
proachescanbecategorizedintovisualexplanations,localexplanations,featureimportance,and
modelsimplification.
Feature importance finds the most influential features contributing to the model’s overall ac-
curacy or for a particular decision, e.g., SHAP [224] and QII [78]. Model simplification finds an
interpretablemodelthatimitatestheopaquemodelclosely.Dependencyplotsareapopularkind
of visual explanation, e.g., Partial Dependence Plots [119], Accumulated Local Effects Plot [16],
andIndividualConditionalExpectation[131].Theyplotthechangeinthemodel’spredictionas
oneormultiplefeaturesarechanged.Localexplanationsdifferfromothermethodsbecausethey
onlyexplainasingleprediction.Localexplanationscanbefurthercategorizedintoapproximation
andexample-basedapproaches.Approximationapproachessamplenewdatapointsinthevicinity
ofthedatapointwhosepredictionfromthemodelneedstobeexplained(hereaftercalledtheex-
plaineedatapoint),andthenfitalinearmodel(e.g.,LIME[281])orextractsarulesetfromthem(e.g.,
Anchors[282]).Example-basedapproachesseektofinddatapointsinthevicinityoftheexplainee
datapoint.Theyeitherofferexplanationsintheformofdatapointsthathavethesameprediction
astheexplaineedatapointorthedatapointswhosepredictiondiffersfromtheexplaineedatapoint.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:3
Fig.1. Twopossiblepathsforadatapoint(showninblue),originallyclassifiedinthenegativeclass,tocross
thedecisionboundary.Theendpointsofboththepaths(showninredandgreen)arevalidcounterfactuals
fortheoriginalpoint.Notethattheredpathistheshortest,whereasthegreenpathadherescloselytothe
manifoldofthetrainingdata,butislonger.
Notethatthelatterkindofdatapointsarestillclosetotheexplaineedatapointandaretermedas
“counterfactualexplanations”(CFE).
Recalltheusecaseofapplicantsapplyingforaloan.Foranindividualwhoseloanrequesthas
beendenied,counterfactualexplanationsprovidethemwithactionable feedbackthatcouldhelp
them make changes to their features in order to transition to the desirable side of the decision
boundary,i.e.,gettheloan.Thisfeedbackistermedasanalgorithmicrecourse.
AnExample. SupposeAlicewalksintoabankandseeksahomemortgageloan.Thedecisionis
madebyamachinelearningclassifierthatconsidersAlice’sfeaturevectorof{Income,CreditScore,
Education, Age}. Unfortunately, Alice is denied the loan she seeks and is left wondering (1) why
the loan was denied? and (2) what can she do differently so that the loan will be approved in
thefuture?Theformerquestionmightbeansweredwithexplanationslike:“CreditScorewastoo
low”,andissimilartothemajorityoftraditionalexplainabilitymethods.Thelatterquestionforms
the basis of a counterfactual explanation: what small changes could be made to Alice’s feature
vectorinordertoendupontheothersideoftheclassifier’sdecisionboundary?Letussuppose
the bank provides Alice with exactly this advice (through a CFE) of what she might change in
order to be approved next time. A possible counterfactual recommended by the system might
be to increase her Income by $10K or get a new master’s degree or a combination of both. The
answer to the former question does not tell Alice what action to take, while the CFE explicitly
helpsher.Figure1illustrateshowthedatapointrepresentinganindividual,whichoriginallygot
classifiedinthenegativeclass,cantaketwopathstocrossthedecisionboundaryintothepositive
classregion.
Unlike several other explainability techniques, CFEs (or recourses) do not explicitly answer
“why” the model made a prediction; instead, they provide suggestions to achieve the desired
outcome. CFEs are also applicable to black-box models (when only the predict function of the
modelisaccessible),andthereforeplacenorestrictionsonmodelcomplexityanddonotrequire
model disclosure. They also do not necessarily approximate the underlying model, producing
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:4 S.Vermaetal.
accurate feedback. Owing to their intuitive nature, CFEs are also amenable to legal frameworks
(seeAppendixB).
In this work, we collect, review and categorize more than 350 recent papers that propose al-
gorithms to generate counterfactual explanations for machine learning models. Many of these
methodshavefocusedondatasetsthatareeithertabularorimage-based.Wedescribeourmethod-
ologyforcollectingpapersforthissurveyinSection2.Wedescriberecentresearchthemesinthis
fieldandcategorizethecollectedpapersamongafixedsetofdesiderataforeffectivecounterfactual
explanations(seeTable1).
Thecontributionsofthisarticleare:
(1) Weexamineasetofmorethan350recentpapersonthesamesetofparameterstoallowfor
aneasycomparisonofthetechniquesthesepapersproposeandtheassumptionstheywork
under;
(2) Thecategorizationofthepapersachievedbythisevaluationhelpsaresearcheroradeveloper
choosethemostappropriatealgorithmgiventhesetofassumptionstheyhaveandthespeed
andqualityofthegenerationtheywanttoachieve.
(3) Comprehensiveandlucidintroductionforbeginnersintheareaofcounterfactualexplana-
tionsformachinelearning.
2 Methodology
In this section, we describe our methodology for collecting and reviewing the papers used for
constructingthesurveypresentedhere.
2.1 HowDidWeCollectthePaperstoReview?
Wecollectedasetofmorethan350papers.Thissectionprovidestheexactprocedureusedtoarrive
atthissetofpapers.Forthefirstversionofthisarticle,wehadstartedfromaseedsetofpapers
recommendedbyotherpeople[229,244,270,331,346],followedbysnowballingtheirreferences.
Forthisupdated(second)versionofthepaper,wecollectedpapersthatcitedthefirstpaperthat
proposedCFEsforML,i.e.,Wachteretal.[346]andthefirstversionofthisCFEsurveypaper[335].
For an even complete search, we searched for “counterfactual explanations”, “recourse”, and
“inverseclassification”ontwopopularsearchenginesforscholarlyarticles,SemanticScholarand
Googlescholar.Welookedforpaperspublishedinthelastfiveyearsonbothsearchengines.Thisis
areasonabletimeframesincethearticlethatstartedthediscussionofcounterfactualexplanations
inthecontextofmachinelearning(specificallyfortabulardata)waspublishedin2017[346].We
collectedpapersthatwerepublishedbefore31stMay2022.Thepaperswecollectedwerepublished
atconferenceslikeKDD,IJCAI,FAccT,AAAI,WWW,NeurIPS,WHI,oruploadedtoArxiv.
2.2 ScopeoftheReview
In this work, we focus on counterfactual explanations for classifiers and targeted towards tabu-
lardatasets.Eventhoughthefirstpaperwereviewwaspublishedonlinein2017,andmostother
paperswereviewciteit[346]astheseminalpaperthatstartedthediscussionaroundcounterfac-
tualexplanations,wedonotclaimthatthisisanentirelynewidea.Communitiesfromdatamin-
ing [111, 231], causal inference [264], and even software engineering [61] have explored similar
ideastoidentifytheprincipalcauseofaprediction,aneffect,andabug,respectively.Evenbefore
theemergenceofcounterfactualexplanationsinappliedfields,theyhavebeenthetopicofdiscus-
sioninfieldslikesocialsciences[238],philosophy[194,215,286],andpsychology[49,50,178].In
this article, we restrict our discussion to recent articles that discuss counterfactual explanations
inmachinelearning,specificallyclassificationsettings.Thesearticleshavebeeninspiredbythe
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:5
emergingtrendofFATEandthelegalrequirementspertainingtoexplainabilityintasksautomated
bymachinelearningalgorithms.
3 Background
Thissectiongivesthebackgroundaboutthesocialimplicationsofmachinelearning,explainability
researchinmachinelearning,andsomepriorstudiesaboutcounterfactualexplanations.
3.1 SocialImplicationsofMachineLearning
Establishing fairness and making an automated tool’s decision explainable are two broad ways
inwhichwecanensureequitablesocialimplicationsofmachinelearning.Fairnessresearchaims
at developing algorithms that can ensure that the decisions produced by the system are not bi-
ased against a particular demographic group of individuals, which are defined with respect to
sensitive or protected features, such as race, sex, and religion. Anti-discrimination laws make it
illegaltousesensitivefeaturesasthebasisofanydecision(seeAppendixB).Biaseddecisionscan
alsoattractwidespreadcriticismandarethereforecrucialtoavoid[136,195].Fairnesshasbeen
capturedinseveralnotionsbasedonademographicgroupingorindividualcapacity.Vermaand
Rubin[338]haveenumeratedandintuitivelyexplainedmanyfairnessdefinitionsusingaunifying
dataset.DunkelauandLeuschel[101]provideanextensiveoverviewofthemajorcategorization
ofresearcheffortsinensuringfairmachinelearningandenlistsimportantworksinallcategories.
Explainablemachinelearninghasalsoseeninterestfromothercommunities,specificallyhealth-
care[321],havinghugesocialimplications.Severalworkshavesummarizedandreviewedother
researchinexplainablemachinelearning[3,56,140].
3.2 ExplainabilityinMachineLearning
This section gives some concrete examples that emphasize the importance of explainability and
givefurtherdetailsoftheresearchinthisarea.Inareal-worldexample,theUSmilitarytrained
a classifier to distinguish enemy tanks from friendly tanks. Although the classifier performed
wellonthetrainingandtestdataset,itsperformancewasabysmalonthebattlefield.Later,itwas
foundthatthephotosoffriendlytanksweretakenonsunnydays,whileforenemytanks,photos
clickedonlyonovercastdayswereavailable[140].Theclassifierfounditmucheasiertousethe
difference between the background as the distinguishing feature. In a similar case, a husky was
classifiedasawolfbecauseofthepresenceofsnowinthebackground,whichtheclassifierhad
learnedasafeatureassociatedwithwolves[281].Theuseofanexplainabilitytechniquehelped
discovertheseissues.
The explainability problem can be divided into model explanation and outcome explanation
problems[140].
Modelexplanationsearchesforaninterpretableandtransparentglobalexplanationoftheorig-
inal model. Various articles have developed techniques to explain neural networks and tree en-
semblesusingsingledecisiontree[72,92,202]andrulesets[14,85].Someapproachesaremodel-
agnostic,suchasGoldenEyeandPALM[152,203,381].
Outcomeexplanationneedstoprovideanexplanationforaspecificpredictionfromthemodel.
Thisexplanationneednotbeaglobalexplanationorexplaintheinternallogicofthemodel.Model-
specificapproachesfordeepneuralnetworks(CAM,Grad-CAM[294,379]),andmodelagnostic
approaches (LIME, MES [281, 328]) have been proposed. These are either feature attribution or
modelsimplificationmethods.Example-basedapproachesareanotherkindofexplainabilitytech-
niqueusedtoexplainaparticularoutcome[339,346].Thisworkfocusesoncounterfactualex-
planations(CFEs),whichisanexample-basedapproach.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:6 S.Vermaetal.
By definition, CFEs are applicable to supervised machine learning setups where the desired
predictionhasnotbeenobtainedforadatapoint.Themajorityofresearchinthisareahasapplied
CFEstoclassificationsettings,whichconsistsofseverallabeleddatapointsthataregivenasinput
tothemodel,andthegoalistolearnafunctionmappingfromtheinputdatapoints(with,say,m
features)tolabels.Inclassification,thelabelsarediscretevalues.Xm isusedtodenotetheinput
spaceofthefeatures,andYisusedtodenotetheoutputspaceofthelabels.Thelearnedfunction
isthemapping f :Xm →Y,whichisusedtopredictlabelsforunseendatapointsinthefuture.
3.3 HistoryofCounterfactualExplanations
Counterfactualexplanationshavealonghistoryinotherfieldslikephilosophy,psychology,and
thesocialsciences.PhilosopherslikeDavidLewispublishedarticlesontheideasofcounterfactu-
alsbackin1973[215].Woodward[362]saidthatasatisfactoryexplanationmustfollowpatterns
ofcounterfactualdependence.Psychologistshavedemonstratedthatcounterfactualselicitcausal
reasoninginhumans[49,50,178].Philosophershavealsovalidatedtheconceptofcausalthinking
duetocounterfactuals[32,362].
StudieshavecomparedthelikeabilityofCFEswithotherexplanationapproaches.Binnsetal.
[36] and Dodge etal. [90] performeduserstudiesthatshowedthatuserspreferCFEs over case-
basedreasoning[193],whichisanotherexample-basedapproach.TheworkbyFernández-Loría
etal.[111]providesthreeinterestingexampleswherethefeatureimportanceexplanationmethods
failtocapturetheunderlyingmodel,whereasCFEsdo.Asheretal.[25]arguethatthepartiality
andlocalityofCFEsmakethemepistemicallyaccessibleandanadequateformofexplanations.
4 CounterfactualExplanations
Thissectionoutlinesthemajoraspectsofcounterfactualexplanations.
4.1 DesiderataandMajorThemesofResearch
Thepreviousexamplealludestomanydesirablepropertiesofaneffectivecounterfactualexplana-
tion.ForAlice,thecounterfactualshouldquantifyarelativelysmallchange,whichwillleadtothe
desiredalternativeoutcome.Alicemightneedtoincreaseherincomeby$10Ktogetapprovedfor
aloan,andeventhoughanincreaseof$50Kwoulddothejob,itismostpragmaticforherifshecan
makethesmallestpossiblechange.Additionally,Alicemightcareaboutasimplerexplanation—it
iseasierforhertofocusonchangingafewthings(suchasonlyIncome)insteadoftryingtochange
manyfeatures.Alicecertainlyalsocaresthatthecounterfactualshereceivesisgivingheradvice,
whichisrealisticandactionable.Itwouldbeoflittleuseiftherecommendationweretodecrease
herageby10years.
Thesedesiderata,amongothers,havesetthestageforrecentdevelopmentsinthefieldofcoun-
terfactualexplainability.Aswedescribeinthissection,majorthemesofresearchhavesoughtto
incorporateincreasinglycomplexconstraintsoncounterfactuals,allinthespiritofensuringthe
resultingexplanationistrulyactionableandhelpful.Developmentinthisfieldhasfocusedonad-
dressingthesedesideratainawaythatisgeneralizableacrossalgorithmsandiscomputationally
efficient.
(1) Validity.Wachteretal.[346]firstproposedcounterfactualexplanationsin2017.Theyposed
CFEasanoptimizationproblem.Equation(1)statestheoptimizationobjective,whichisto
(cid:3)
minimizethedistancebetweenthecounterfactual(x )andtheoriginaldatapoint(x)subject
totheconstraintthattheoutputoftheclassifieronthecounterfactualisthedesiredlabel
(y (cid:3) ∈Y).Convertingtheobjectiveintoadifferentiable,unconstrainedformyieldstwoterms
(seeEquation(2)).Thefirsttermencouragestheoutputoftheclassifieronthecounterfactual
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:7
tobeclosetothedesiredclass,andthesecondtermforcesthecounterfactualtobecloseto
theoriginaldatapoint.Ametricd isusedtomeasurethedistancebetweentwodatapoints
x,x (cid:3) ∈ X, which can be the L1/L2 distance, or quadratic distance, or distance functions
whichtakeasinputtheCDFofthefeatures[331],orpairwisefeaturecostsasperceivedby
users[278].Thus,thisoriginaldefinitionalreadyemphasizedthataneffectivecounterfactual
onlyproposessmallchangesinthefeaturesrelativetothestartingpoint.
argmind(x,x (cid:3))subjectto f(x (cid:3))=y (cid:3) (1)
x(cid:3)
argminmaxλ(f(x (cid:3))−y (cid:3))2+d(x,x (cid:3)). (2)
x(cid:3) λ
A counterfactual that indeed is classified in the desired class is a valid counterfactual. As
illustratedinFigure1,thepointsshowninredandgreenarevalidcounterfactuals,asthey
are in the positive class region. The distance to the red counterfactual is smaller than the
distancetothegreencounterfactual.
(2) Actionability.Animportantconsiderationwhilemakingarecommendationisaboutwhich
featuresaremutable(e.g.,income,age)andwhicharenot(e.g.,race,countryoforigin)[331].
A recommended counterfactual should never change the immutable features. In fact, if a
changetoalegallysensitivefeatureproducesachangeinprediction,itshowsinherentbias
inthemodel.Severalarticleshavealsomentionedthatanapplicantmighthaveapreference
orderamongstthemutablefeatures(whichcanalsobehidden.)Theoptimizationproblem
is modified to take this into account. We might call the set of actionable features A, and
updateourlossfunctiontobe,
argminmaxλ(f(x (cid:3))−y (cid:3))2+d(x,x (cid:3)). (3)
x(cid:3)∈A λ
(3) Sparsity. There can be a tradeoff between the number of features changed and the total
amountofchangemadetoobtainthecounterfactual.Acounterfactualideallyshouldchange
asmallernumberoffeaturesinordertobethemosteffective.Thagard’stheoryofexplana-
tory coherence proposed that people prefer simpler and shorter explanations [319] and it
hasalsobeentestedinthecontextofexplanationsinML[238,247].Thismakessparsityan
importantconsideration.Weupdateourlossfunctiontoincludeapenaltyfunctionthaten-
couragessparsityinthedifferencebetweenthemodifiedandtheoriginaldatapoint,д(x (cid:3)−x),
e.g.,L0/L1norm:
argmin maxλ (f(x (cid:3))−y (cid:3))2+λ ∗д(x (cid:3)−x)+d(x,x (cid:3)). (4)
x(cid:3)∈A λ1,λ2 1 2
(4) DataManifoldCloseness/Plausibility.Thagard’stheoryofexplanatorycoherencestatesthat
peoplewouldfindithardtotrustanexplanationifitisinconsistentwiththeirpriorbeliefs
[319], for example if it resulted in a combination of features that were utterly unlike any
observationstheoccursintherealworld.Inthissense,thecounterfactualwouldbe“unreal-
istic",noteasytorealize,andanomaloustotherealdatapoints[44].Therefore,agenerated
counterfactualshouldberealisticinthesensethatitisnearthetrainingdataandadheres
toobservedcorrelationsamongthefeatures.Manyarticleshaveproposedvariouswaysof
quantifyingthis.Wemightupdateourlossfunctiontoincludeapenaltyforadheringtothe
datamanifolddefinedbythetrainingsetX,denotedbyl(x (cid:3) ;X):
argmin max λ (f(x (cid:3))−y (cid:3))2+λ ∗д(x (cid:3)−x)+λ ∗l(x (cid:3) ;X)+d(x,x (cid:3)). (5)
x(cid:3)∈A λ1,λ2,λ3 1 2 3
In Figure 1, the region between the dashed lines shows the data manifold. There are two
possiblepathstocrossthedecisionboundaryforthebluedatapoint.Theshorter,redpath
takesittoacounterfactualthatisoutsidethedatamanifold,whereasabitlonger,thegreen
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:8 S.Vermaetal.
Education
Age Salary
Fig.2. StructuralCausalModel(SCM)showingtheinfluenceofEducationonotherfeatureslikeAgeand
Salary.
path takes it to a counterfactual that follows the data manifold. Adding the data manifold
losstermencouragesthealgorithmtochoosethegreenpathovertheredpath,evenifitis
slightlylonger.
(5) Causality.Featuresina datasetarerarelyindependent,therefore,changing onefeaturein
therealworldaffectsotherfeatures.Forexample,gettinganeweducationaldegreeneces-
sitatesincreasingtheindividual’sagebyatleastsomeamountanditwouldlikelyresultin
anincreaseinone’ssalary.Theserelationsareusuallyrepresentedusingastructuralcausal
model(SCM)asshowninFigure2.Inordertoberealisticandactionable,acounterfactual
shouldadheretocausalrelationsbetweenfeatures.Adheringtocausalrelationcanbeincor-
poratedasalossfunctionorasahardconstraint[182,337],dependingonamethod.
Generally,ourlossfunctionnowaccountsfor(1)counterfactualvalidity;(2)sparsityinfea-
turevector(andactionabilityoffeatures);(3)similaritytothetrainingdata;and(4)causal
relations.
4.2 RelationshiptoOtherRelatedTerms
Outofthepaperscollected,differentterminologyoftencapturesthebasicideaofcounterfactual
explanations, although subtle differences exist between the terms. Several terms worth noting
include:
—AlgorithmicRecourse: Ustunet al. [331] pointoutthatcounterfactualsdo not takeinto ac-
counttheactionabilityoftheprescribedchanges,whichrecoursedoes.Workstakingacausal
view of the problem further fortify this claim [183, 184]. Recent papers in counterfactual
generation take actionability and feasibility of the prescribed changes, and therefore the
differencewithrecoursehasblurred.
—InverseClassification:Inverseclassificationaimstoperturbaninputinameaningfulwayin
ordertoclassifyitintoitsdesiredclass[4,208].Suchanapproachprescribestheactionsto
be taken in order to get the desired classification. Therefore, inverse classification has the
samegoalsasCFEs.
—ContrastiveExplanation:Contrastiveexplanationsgenerateexplanationsoftheform“anin-
putx isclassifiedasy becausefeatures f ,f ,...,f arepresentand f ,...,f areabsent”.
1 2 k n r
The features that are minimally sufficient for a classification are called pertinent positives,
andthefeatureswhoseabsenceisnecessaryforthefinalclassificationaretermedpertinent
negatives [87]. To generate both pertinent positives and pertinent negatives, one needs to
solvetheoptimizationproblemtofindtheminimumperturbationsneededtomaintainthe
sameclasslabelorchangeit,respectively.Therefore,contrastiveexplanations(specifically
pertinentnegatives)arerelatedtoCFEs.
—Adversarial Learning: Adversarial learning is closely related, but the terms are not inter-
changeable. Adversarial learning aims to generate the least amount of change in a given
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:9
inputtoclassifyitdifferently,oftenwiththegoaloffar-exceedingthedecisionboundaryand
resultinginahighlyconfidentmisclassification.Whiletheoptimizationproblemissimilarto
theoneposedinacounterfactualgeneration,thedesiderataaredifferent.Forexample,inad-
versariallearning(oftenappliedtoimages),thegoalisanimperceptiblechangeintheinput
image.ThisisoftenatoddswiththeCFE’sgoalofsparsityandparsimony(thoughsingle-
pixelattacksareanexception).Further,notionsofdatamanifoldandactionability/causality
are rarely considerations in adversarial learning. A few works point to the similarity and
synergybetweenthetwodomains:Pawelczyketal.[259]exploretheconnectionbetween
the optimization objectives and results of the adversarial and CFE generating techniques.
Freiesleben[118]statesthatthedifferencesinthedesiredclasslabelanddistancefromthe
original datapoint distinguish CFEs from adversarial examples. Elliott et al. [104] propose
generatingsemanticallymeaningfuladversarialperturbationstogenerateCFEsforimages.
BrowneandSwift[45]pointoutthattheconstraintofproducingplausibledatapointsdis-
tinguishesCFEsfromadversarialexamples.
5 AssessmentoftheApproachesonCounterfactualProperties
Foreasycomprehensionandcomparison,weidentifyseveralpropertiesthatareimportantfora
counterfactualgenerationalgorithm.Forallthecollectedpaperswhichproposeanalgorithmto
generatecounterfactualexplanations,weassessthealgorithmtheyproposeagainsttheseproper-
ties.TheresultsarepresentedinTable1.Papersthatdonotproposenewalgorithmsanddiscuss
relatedaspectsofcounterfactualexplanationsormodificationstopreviousmethodsarementioned
inSection6.3.ThemethodologyweusedtocollectthepapersisgiveninSection2.
5.1 PropertiesofCounterfactualAlgorithms
Thissectionexpoundsonthekeypropertiesofacounterfactualexplanationgenerationalgorithm.
ThepropertiesformthecolumnsofTable1.
(1) ModelAccess.Thecounterfactualgenerationalgorithmsrequiredifferentlevelsofaccessto
the underlying model for which they generate counterfactuals. We identify three distinct
access levels—access to complete model internals, access to gradients, and access to only
thepredictionfunction(black-box).Theaccesslevelrequiredforthemodeldependsonthe
optimizationtoolusedbyaCFEgeneratingapproach.
Accesstothecompletemodelinternalsisrequiredwhenthealgorithmusesasolver-based
methodlike,mixedintegerprogramming[179,182,183,287,331]oriftheyoperateonde-
cision trees [52, 110, 222, 241, 323] which requires access to all internal nodes of the tree.
Gradient-basedalgorithmstosolvetheoptimizationobjectiveareusedbyamajorityofthe
methods,usuallybymodifyingthelossfunctionproposedbyWachteretal.[346],butthis
isrestrictedtodifferentiablemodelsonly.
Black-boxapproachesusegradient-freeoptimizationalgorithmssuchasNelder-Mead[137],
growing spheres [210], FISTA [88, 332], ASP [35], or genetic algorithms [75, 208, 298] to
solve the optimization problem. Finally, some approaches do not cast the goal into an op-
timization problem and solve it using heuristics [139, 188, 274, 357]. Poyiadzi et al. [267]
proposeFACE,whichusesDijkstra’salgorithm[89]tofindtheshortestpathbetweenexist-
ingtrainingdatapointstofindcounterfactualforagiveninput.Hence,thismethoddoesnot
generatenewdatapoints.FraunhoferIOSBetal.[117]andBlanchart[39]dividethefeature
space into ‘pure’ regions where all datapoints (by sampling) belong to one class and then
usegraphtraversingtechniquestofindtheclosestCFEs.
There are several approaches can incorporate the generation of CFEs within the classifier
itself.Guoetal.[143]proposeCounterNet,anovelarchitecturethatpredictstheclassand
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

| 312:10 |     |     |     |     |     | S.Vermaetal. |     |
| ------ | --- | --- | --- | --- | --- | ------------ | --- |
Table1. AssessmentoftheCollectedArticlesontheKeyProperties,whichareImportantforReadily
ComparingandComprehendingtheDifferencesandLimitationsofDifferentCounterfactualAlgorithms
Assumptions Optimizationamortization CFattributes Featurehandlingattributes
Year Paper Model Model Amortized Multiple Sparsity Data Causal Feature Categorical
access domain Inference CFEs manifold relation actionability dist.func
| (cid:2)    |           |                |       |             |       |     | −   |
| ---------- | --------- | -------------- | ----- | ----------- | ----- | --- | --- |
| [208]      | Black-box | Agnostic       | No No | Iteratively | No No | Yes |     |
| 2017 [346] | Gradients | Differentiable | No No | L1          | No No | No  | −   |
−
| [323]   | Complete  | Treeensemble | No No | No           | No No | No  |     |
| ------- | --------- | ------------ | ----- | ------------ | ----- | --- | --- |
| ⎧⎪⎪⎪⎪⎪⎨ |           |              |       | L 0 andpost- |       |     | −   |
| [210]   | Black-box | Agnostic     | No No |              | No No | No  |     |
h oc
Flips min.
2018⎪⎪⎪⎪⎪[ [ 1 3 9] B l a c k - b o x Ag n o s t ic N o Y e s s p litnodes N o N o N o Indi cator
8 7 ] G r a d i e n t s D iff e r e n tiable N o N o L 1 Y e s N o N o −
| ⎩ [137] | Black-box | Agnostic | No No | No  | No No | No1 | −   |
| ------- | --------- | -------- | ----- | --- | ----- | --- | --- |
⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
[ 2 8 7 ] C o m p l e t e L i n e a r N o Y e s L 1 N o N o N o N . A . 2
H a r d
[ 3 3 1 ] C o m p l e t e L i n e a r N o N o N o N o Y e s −
c o n s tr a i nt
[ 2 9 8 ] B l a c k - b o x A g n o s t i c N o Y e s N o N o N o Y e s In di c a t or
[ 8 8 ] B l a c k - b o x D i ff e r e n t i a b l e N o N o L 1 Y e s N o N o −
| 2019 ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪ | o r g r a d | i e nt |     |     |     |     |     |
| -------------------- | ----------- | ------ | --- | --- | --- | --- | --- |
−
[ 2 7 4 ] B l a c k - b o x A g n o s t i c N o N o N o N o N o N o
[ 1 7 4 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o Y e s N o N o −
−
[ 2 7 0 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o N o N o N o
| ⎩ [ 3 5                            | 7 ,           |                     |         | C h a n g e s     |         |     | −   |
| ---------------------------------- | ------------- | ------------------- | ------- | ----------------- | ------- | --- | --- |
|                                    | B l a c k - b | o x A g n o s t i c | N o N o |                   | N o N o | N o |     |
| 358]                               |               |                     |         | onefeature        |         |     |     |
| ⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ |               |                     |         | L 1 a n d p o st- |         |     |     |
[ 2 4 4 ] G r a d i e n t s D i ff e r e n t i a b l e N o Y e s N o N o N o I n d i c a t o r
h o c
[ 2 6 7 ] B l a c k - b o x A g n o s t i c N o N o N o Y e s 3 N o N o −
B l a c k - b o x
[ 3 3 2 ] D i ff e r e n t i a b l e N o N o L 1 Y e s N o N o E m b e d d in g
or g r a d i e nt
[ 2 2 9 ] G r a d i e n t s D i ff e r e n t i a b l e Y e s Y e s N o Y e s Y e s Y e s −
H a r d
[ 1 8 2 ] C o m p l e t e L i n e a r N o Y e s c o n s t ra in t N o N o Y e s I n d i c a t o r
[ 2 6 3 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o Y e s N o Y e s N . A . 4
[ 1 8 8 ] B l a c k - b o x A g n o s t i c N o N o Y e s Y e s N o N o −
2020⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪
[ 1 8 3 ] C o m p l e t e L i n e a r a n d N o N o L 1 N o Y e s Y e s −
|     |     | c a u s a l g r a p h |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- | --- |
−
[ 1 8 4 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o N o N o Y e s Y e s
[ 2 1 2 ] G r a d i e n t s D i ff e r e n t i a b l e N o N o It e ratively Y e s N o N o 5 −
[ 7 5 ] Bl a c k - b o x A g n o s t ic N o Y e s L 0 Y e s N o Y e s Indi cator
|        |               | L i n e a r a n d       |           |     |           |       |     |
| ------ | ------------- | ----------------------- | --------- | --- | --------- | ----- | --- |
| [ 1 7  | 9 ] C o m p l | e t e                   | N o N o   | N o | Y e s N o | Y e s | −   |
|        |               | t r e e e n s e m b l e |           |     |           |       |     |
|        |               | R a n d o m             |           |     |           |       | −   |
| [ 1 1  | 0 ] C o m p l | e t e                   | N o Y e s | L 1 | N o N o   | N o   |     |
|        |               | F o r e s t             |           |     |           |       |     |
| ⎩[221, |               |                         |           |     |           |       | −   |
|        | Complete      | Treeensemble            | No No     | L1  | No No     | No    |     |
222]
Papersaresortedchronologically.DetailsaboutthefulltableisgiveninAppendixA.
generatestheCFEofadatapointwhentrainedfromscratch.ShaoandKersting[297]train
asum-productnetworkthatactsasbothaclassifieranddensityestimatorandusesthatto
generateCFEs.Rossetal.[285]proposeaddinganadversariallossduringtrainingoftheML
modeltohaveahigherprobabilityofhavingarecourseforthetrainingdatapoints.(After
training,anyCFEgeneratingmethodcanbeused.)
(2) ModelAgnostic.Thiscolumndescribesthedomainofmodelsagivenalgorithmcanoperate
on.Forexample,gradient-basedalgorithmscanonlyhandledifferentiablemodels,andtheal-
gorithmsbasedonsolversrequirelinearorpiece-wiselinearmodels[179,182,183,287,331],
some algorithms are model-specific and only work for those models like tree ensem-
bles [110, 179, 222, 323]. Black-box methods have no restriction on the underlying model
andare,therefore,model-agnostic.
1Itconsidersglobalandlocalfeatureimportance,notpreference.
2Allfeaturesareconvertedtopolytopetype.
3Doesnotgeneratenewdatapoints.
4Thedistanceiscalculatedinlatentspace.
5Itconsidersfeatureimportancenotuserpreference.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:11
(3) Optimization Amortization. Among the collected papers, the proposed algorithm mostly
returned a single counterfactual for a given input datapoint. Therefore, these algorithms
require solving an optimization problem to generate each counterfactual for every input
datapoint.Asmallernumberofthemethodsareabletogeneratemultiplecounterfactuals
(generallydiversebysomemetricofdiversity)forasingleinputdatapoint;therefore,they
require to be run once per input to get several counterfactuals [52, 75, 110, 139, 182, 229,
244, 287, 298]. Dandl et al. [75] propose a genetic algorithm to generate multiple CFEs of
a datapoint at once. Mahajan et al. [229]’s approach learns the mapping of datapoints to
counterfactualsusingavariationalauto-encoder(VAE)[91].Therefore,oncetheVAEis
trained, it can generate multiple counterfactuals for all input datapoints, without solving
theoptimizationproblemseparatelyandisthusveryfast.Vermaetal.[337]andSamoilescu
etal.[290]trainareinforcementlearningmodeltolearntheactionsthatneedtobetakento
generateCFEsforadatadistribution.Hence,theseapproachesarealsoamortized.Yangetal.
[367]trainaCGANtosynthesizeCFEswithumbrellasampling;hence,theirapproachisalso
amortized.VanLooverenetal.[333]alsotrainaGAN-basedmodelthatisamortized.Schleich
etal.[292]partiallyevaluate(amortize)theclassifierforthestaticfeatures,hencespeeding
uptheCFEgeneration.Wereporttwoaspectsofoptimizationamortizationinthetable:
• AmortizedInference:ThiscolumnismarkedYesifthealgorithmcangeneratecounterfac-
tualsformultipleinputdatapointswithoutoptimizingseparatelyforthem;otherwise,it
ismarkedNo.
• Multiple Counterfactuals (CF): This column is marked Yes if the algorithm can generate
multiplecounterfactualsforasingleinputdatapoint;otherwise,itismarkedNo.
(4) Counterfactual (CF) Attributes. These columns evaluate algorithms on sparsity, data
manifoldadherence,andcausality.
(a) Sparsity: Among the collected articles, methods using solvers explicitly constrain spar-
sity[182,331],black-boxmethodsconstrainL0normofcounterfactualandtheinputdat-
apoint[75,210].Gradient-basedmethodstypicallyusetheL1normofcounterfactualand
theinputdatapoint.Someofthemethodschangeonlyafixednumberoffeatures[188,357],
changefeaturesiteratively[175,212,293,337],orfliptheminimumpossiblesplitnodesin
thedecisiontree[139]toinducesparsity.Somemethodsalsoinducesparsitypost-hoc[210,
244].Thisisdonebysortingthefeaturesinascendingorderofrelativechangeandgreed-
ilyrestoringtheirvaluestomatchthevaluesintheinputdatapointuntilthepredictionfor
theCFEisstilldifferentfromtheinputdatapoint.Sparsity columninthetableismarked
Noifthealgorithmdoesnotconsidersparsity,elseitspecifiesthesparsityconstraint.
(b) Data Manifold Adherence: Adherence to the data manifold has been addressed using
severaldifferentapproaches,liketrainingVAEsonthedatadistribution[87,174,229,332],
constraining the distance of a counterfactualfrom thek nearest training datapoints[75,
102,179],directlysamplingpointsfromthelatentspaceofaVAEtrainedonthedata,and
thenpassingthepointsthroughthedecoder[263],usinganensembleofmodelstocapture
the predictive entropy [293], using a kernel density estimator (KDE) to estimate the
PDFoftheunderlyingdatamanifold[122],usingthecycleconsistencylossinGAN[333],
mappingbacktothedatadomain[212],usingacombinationofexistingdatapoints[188],
usingGaussianmixturemodelstoapproximatetheprobabilityofin-distributionness[19],
orbyusingfeaturecorrelations[20],orbysimplynotgeneratinganynewdatapoint[267].
Data manifold column in the table is marked Yes if the algorithm forces the generated
CFEstobeclosetothedatamanifoldbysomemechanism;otherwise,itismarkedNo.
(c) Causality: The relation between different features is represented by a directed graph
between them, which is termed as a causal graph [264]. Out of the papers that have
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:12 S.Vermaetal.
addressed this concern, most require access to the complete causal graph [183, 184]
(which is rarely available in the real world), while Duong et al. [102], Mahajan et al.
[229],Vermaetal.[337],andYangetal.[367]canworkwithpartialcausalgraphs.Causal
relationcolumninthetableismarkedYesifthealgorithmconsidersthecausalrelations
betweenfeatureswhengeneratingCFEs;otherwise,itismarkedNo.
(5) Feature Handling Attributes. Out of the articles that consider feature actionability, most
classify the features into immutable and mutable types. Karimi et al. [183] and Lash et al.
[208] categorize the features into immutable, mutable, and actionable types. Actionable
featuresareasubsetofmutablefeatures.Theypointoutthatcertainfeaturesaremutable
butnotdirectlyactionablebytheindividual,e.g.,CreditScorecannotbedirectlychanged;it
changesasaneffectofchangesinotherfeatureslikeincomeandcreditamount.Mahajan
et al. [229] uses an oracle to learn the user preferences for changing features (among
mutablefeatures)andcanalsolearnhiddenpreferences.
Mosttabulardatasetshavebothcontinuousandcategoricalfeatures.Performingarithmetic
over continuous features is natural, but handling categorical variables in gradient-based
algorithms can be complicated. Some algorithms cannot handle categorical variables and
filterthemout[210,222].Wachteretal.[346]proposedclampingallcategoricalfeaturesto
eachoftheirvalues,thusspawningmanyprocesses(oneforeachvalueofeachcategorical
feature), leading to scalability issues. Some approaches convert categorical features to
one-hot encoding and then treat them as numerical features. In this case, maintaining
one-hotness can be challenging. Some use a different distance function for categorical
features, which is generally an indicator function (1 if a different value, else 0). [122] use
Markov chain transitions to encode categorical distances. Yang et al. [367] use Gaussian
mixturemodelstonormalizethecontinuousfeaturesandGumbel-Softmaxtorelaxcategor-
ical features into continuous ones. Genetic algorithms, evolutionary algorithms, and SMT
solverscannaturallyhandlecategoricalfeatures.Wereportthesepropertiesinthetable.
• Feature Actionability: This column is marked Yes if the algorithm considers feature
actionability,otherwisemarkedNo.
• Categorical Distance Function: This column is marked—if the algorithm does not use a
separatedistancefunctionforcategoricalvariables,elseitspecifiesthedistancefunction.
6 EvaluationofCounterfactualGenerationAlgorithms
Thissectionliststhecommondatasetsusedtoevaluatecounterfactualgenerationalgorithmsand
themetricsonwhichtheyaretypicallyevaluatedandcompared.
6.1 CommonlyUsedDatasetsforEvaluation
Thedatasetsusedintheevaluationinthearticleswereviewcanbecategorizedintotabularand
imagedatasets.Notallmethodssupportimagedatasets.Someofthearticlesalsousedsynthetic
datasetsforevaluatingtheiralgorithms,butweskipthoseinthisreviewsincetheyweregenerated
foraspecificarticleandalsomightnotbeavailable.Commondatasetsintheliteratureinclude:
—Tabular:Adultincome[33],Germancredit[154],StudentPerformance[71],Breastcancer
[97],Defaultofcredit[372],Shopping[99],Iris[98],Wine[100],Spambase[157],Covertype
[38],ICU[96],LendingClub[314],GiveMeSomeCredit[177],COMPAS[170],LSAT[40],
Pima diabetes [303], HELOC/FICO [113], Fannie Mae [227], Portuguese Bank [243], San-
giovese [228], Bail dataset [173], Simple-BN [229], AllState [165], WiDS Datathon [164],
Home Credit Default Risk [138], German Housing [115], HospitalTriage [156], MIMIC-
IV [172], Freddie Mac [225], UK unsecured personal loans [47], insurance dataset [197],
BPIC2017[160].
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:13
Table2. ContinuedfromTable1
Assumptions Optimizationamortization CFattributes Featurehandlingattributes
Model Model Amortized Multiple Data Causal Feature Categorical
Year Paper Sparsity
access domain Inference CFEs manifold relation actionability dist.func
⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
1
[
[
[
[
[
[
[
[
[
[
1
2
2
4
1
2
2
2
5
3
4
8
9
4
6
0
4
0
9
2
3
7
1
3
7
2
8
2
]
]
,
3
]
]
]
]
]
]
]
]
C
G
B
B
C
B
o
c
B
C
C
G
o
r
l
l
l
l
o
o
o
o
r
r
a
a
a
a
m
a
a
m
m
m
m
c
c
c
c
d
d
p
k
k
k
k
p
p
p
p
i
i
l
-
-
-
-
e
e
l
l
l
l
e
b
b
b
b
e
e
e
e
n
n
t
o
o
o
o
t
t
t
t
e
t
t
e
e
e
e
x
x
x
x
s
A
b
D
L
A
A
L
A
L
D
D
l
i
i
i
g
g
g
g
i
i
e
a
n
n
n
ff
ff
c
n
n
n
n
c
e
e
e
e
e
i
k
o
o
o
o
a
a
a
s
r
r
-
s
s
s
s
i
r
r
r
e
e
b
o
t
t
t
t
n
n
i
i
i
i
o
n
c
c
c
c
t
t
x
i
i
T
a
a
r
b
b
e
l
l
e
e
e
if
Y
N
N
N
N
N
N
N
N
N
e
o
o
o
o
o
o
o
o
o
s
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s H
c
L
I
L
G
N
N
I
Y
L
t
t
o
e
0
1
1
e
e
o
o
o
a
n
s
/
r
r
w
r
L
a
a
s
d
1
t
t
t
e
r
i
i
r
v
v
a
e
e
in
l
l
y
y
t
N
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
o
o
o
o
o
o
s
s
s
s
6
Y
Y
Y
Y
N
N
N
N
N
N
e
e
e
e
o
o
o
o
o
o
s
s
s
s
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s
La
I
I
t
n
n
G
e
d
d
n
o
i
i
−
−
−
−
−
−
t
c
c
w
a
a
s
e
t
t
p
o
o
r
a
r
r
ce
2021⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪
⎩
[
[
[
[
[
[
[
[
[
[
[
2
2
1
3
1
1
2
3
2
3
2
5
4
1
6
7
2
7
9
9
3
5
8
1
7
7
5
2
9
0
7
]
0
]
]
]
]
]
]
]
]
]
]
C
C
B
B
G
B
B
B
B
C
B
or
l
l
l
l
l
l
l
o
o
o
r
a
a
a
a
a
a
a
a
g
m
m
m
c
c
c
c
c
c
c
d
r
k
k
k
k
k
k
k
p
p
p
a
i
-
-
-
-
-
-
-
e
d
l
l
l
b
b
b
b
b
b
b
e
e
e
n
i
o
o
o
o
o
o
o
t
t
t
e
t
e
e
e
x
x
x
x
x
x
x
nt
A
D
A
b
T
L
A
A
A
A
A
T
l
i
r
r
g
g
g
g
g
g
g
i
a
n
e
e
ff
n
n
n
n
n
n
n
c
e
e
e
e
k
o
o
o
o
o
o
o
a
r
e
e
-
s
s
s
s
s
s
s
r
e
b
n
n
t
t
t
t
t
t
t
n
i
i
i
i
i
i
i
o
s
s
c
c
c
c
c
c
c
t
e
e
x
i
m
m
ab
b
b
le
l
l
i
e
e
f
Par
Y
Y
Y
Y
Y
Y
N
N
N
N
t
e
e
e
e
e
e
i
o
o
o
o
a
s
s
s
s
s
s
lly Y
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s
s
H
c
H
s
L
N
L
N
N
L
L
I
Y
t
t
o
e
1
1
0
0
e
o
o
o
r
a
a
n
s
/
/
r
a
r
r
L
L
a
s
i
d
d
n
1
1
t
t
r
i
t
v
a
c
e
i
o
n
l
n
y
t
-
Y
Y
Y
Y
Y
Y
N
N
N
N
N
e
e
e
e
e
e
o
o
o
o
o
s
s
s
s
s
s
Y
Y
N
N
N
N
N
N
N
N
N
e
e
o
o
o
o
o
o
o
o
o
s
s
Y
Y
Y
Y
Y
Y
Y
N
N
N
N
e
e
e
e
e
e
e
o
o
o
o
s
s
s
s
s
s
s
I
I
N
M
n
n
C
G
G
o
d
d
h
a
o
o
t
i
i
−
−
−
−
−
r
a
c
c
w
w
s
k
a
a
i
u
n
e
e
o
t
t
r
o
o
r
r
s
v
e
r
r
Training
⎧⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ [
[
1
3
4
6
3
3
]
]
f
s
G
r
c
o
r
r
a
m
a
d
tc
ie
h
nt
D
D
i
i
ff
ff
e
e
r
r
e
e
n
n
t
t
i
i
a
a
b
b
l
l
e
e
Y
N
e
o
s N
N
o
o
N
N
o
o Y
N
e
o
s Y
N
e
o
s
N
N
o
o
−
−
2022⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪ [
[
[
3
2
2
6
7
9
6
8
7
]
]
]
T
f
B
B
r
r
l
l
o
a
a
a
m
c
c
in
k
k
i
-
-
n
b
b
g
o
o
x
x
D
A
A
g
g
iff
n
n
e
o
o
r
s
s
e
t
t
n
i
i
c
c
tiable
Y
N
N
e
o
o
s M
M
N
i
i
g
g
o
h
h
t
t
N
Y
Y
e
e
o
s
s
Y
N
N
e
o
o
s N
N
N
o
o
o
Y
Y
Y
e
e
e
s
s
s
Indi
−
−
cator
⎩
scratch
—Image:MNIST[213],EMNIST[66],CelebA[219],CheXpert[167],ImageNet[86],ISICSkin
Lesion[65],ADNI[245],ChestX-ray8[348].
6.2 MetricsforEvaluationofCounterfactualGenerationAlgorithms
Counterfactualsareconsideredasactionablefeedbacktoindividualswhohavereceivedundesir-
ableoutcomesfromautomateddecision-makers,andthereforeanidealevaluationwouldconsist
ofauser-study.However,userstudiesareexpensiveandthereforetheliteratureproposestouse
proxymetricstoevaluatetheeaseofactingonarecommendedcounterfactual:
(1) Validity: Validity measures the ratio of the counterfactuals that actually have the desired
class label to the total number of counterfactuals generated. Higher validity is preferable.
Mostpapersreportit.
(2) Proximity:Proximitymeasuresthedistanceofacounterfactualfromtheinputdatapoint.For
counterfactualstobeeasytoactupon,theyshouldbeclosetotheinputdatapoint.Distance
metricsliketheL1norm,L2norm,andMahalanobisdistancearecommon.Tohandlethevari-
abilityofrangeamongdifferentfeatures,somearticlesstandardizetheminpre-processing
ordivideL1normbymedianabsolutedeviationofrespectivefeatures[244,287,346],ordi-
videL1normbytherangeoftherespectivefeatures[75,182,183].Proximityforcategorical
6Maybepartiallyasitusescycleconsistencyloss.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:14 S.Vermaetal.
featuresistreatedasbinary(oneorzerodependingofwhetherthevaluechangedornot).
Somearticlestermproximityastheaveragedistanceofthegeneratedcounterfactualsfrom
theinput.Lowervaluesofaveragedistancearepreferable.
(3) Number of Features Changed: Shorter explanations are more comprehensible to humans
[238],therefore,counterfactualsideallyshouldprescribeachangeinasmallnumberoffea-
tures.Althoughaconsensusonahardcaponthenumberofmodifiedfeatureshasnotbeen
reached,KeaneandSmyth[188]capasparsecounterfactualtoatmosttwofeaturechanges.
(4) Counterfactual generation time: Intuitively, this measures the time required to generate
counterfactuals.Thismetriccanbeaveragedoverthegenerationofacounterfactualfora
batchofinputdatapointsorforthegenerationofmultiplecounterfactualsforasingleinput
datapoint.
(5) Diversity:Somealgorithmssupportthegenerationofmultiplecounterfactualsforasingle
input datapoint. The purposeof providing multiple counterfactuals is to increase the ease
forapplicantstoreachatleastonecounterfactualstate.Therefore,therecommendedcoun-
terfactualsshouldbediverse,allowingapplicantstochoosetheeasiestone.Ifanalgorithm
isstronglyenforcingsparsity,therecouldbemanydifferentsparsesubsetsofthefeatures
thatcouldbechanged.Therefore,havingadiversesetofcounterfactualsisuseful.Diversity
isencouragedbymaximizingthedistancebetweenthemultiplecounterfactualsbyadding
it as a term in the optimization objective [75, 244] or as a hard constraint [182, 241, 331],
or by minimizing the mutual information between all pairs of modified features [212].
Mothilal et al. [244] reported diversity as the feature-wise distance between each pair of
counterfactuals.Ahighervalueofdiversityispreferable.
(6) Closeness to the Training Data/Plausibility: Recent articles have considered the action-
ability and realisticness of the modified features by grounding them in the training data
distribution. This has been captured by measuring the average distance to the k-nearest
datapoints[75],ormeasuringthelocaloutlierfactor[179],ormeasuringthereconstruction
error from a VAE trained on the training data [229, 332], or measuring the PDF of such
datapoints using KDE [122], or measuring the maximum mean discrepancy (MMD)
between the original and counterfactual points [333]. A lower value of the distance and
reconstructionerrorispreferable.
(7) Causal Constraint Satisfaction (Feasibility): This metric captures how realistic the modifi-
cations in the counterfactual are by measuring if they satisfy the causal relation between
features.Mahajanetal.[229]evaluatedtheiralgorithmonthismetric.
OtherMetrics. Herewedescribethelesscommonlyusedmetrics:
(1) IM1andIM2:VanLooverenandKlaise[332]proposedtwointerpretabilitymetricsspecifi-
callyforalgorithmsthatuseauto-encoders.Letthecounterfactualclassbet,andtheoriginal
class beo.AE is the auto-encoder trained on training instances of classt, andAE is the
t o
auto-encodertrainedontraininginstancesofclasso.LetAEbetheauto-encodertrainedon
thefulltrainingdataset(allclasses):
(cid:6)x −AE (x )(cid:6)2
IM1= cf t cf 2 (6)
(cid:6)x −AE (x )(cid:6)2+ϵ
cf o cf 2
(cid:6)AE (x )−AE(x )(cid:6)2
IM2= t (cid:7) (cid:7) c x f (cid:7) (cid:7) +ϵ cf 2 (7)
cf 1
A lower value of IM1 implies that the counterfactual (x ) can be better reconstructed by
cf
the auto-encoder trained on the counterfactual class (AE ) compared to the auto-encoder
t
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:15
trainedontheoriginalclass(AE ),thusimplyingthatthecounterfactualisclosertothedata
o
manifoldofthecounterfactualclass.AlowervalueofIM2 impliesthatthereconstruction
fromtheauto-encodertrainedonthecounterfactualclassandtheauto-encodertrainedon
all classes is similar. Therefore, a lower value of IM1 and IM2 means a more interpretable
counterfactual, where interpretability refers to a plausible datapoint which is supposedly
moreinterpretable.
(2) LabelVariationScoreandOracleScore:Hvilshøjetal.[162]pointoutthatthepreviousmet-
ricsareunabletodetectout-of-distributionCFEs(especiallyforhigh-dimensionaldatasets)
andproposetwonewmetrics.LabelVariationScoreapplieswheneachdatapointhasmulti-
plelabels,andtheintuitionisthatCFEforaparticularlabelshouldnotaffectthepredictions
forotherlabels(unlesstheyarehighlycorrelated).Thisassumesthecaseofmultilabelclas-
sification,whereadatapointwithoriginalpredictionAisbeingcounterfactuallypredicted
asB.LVSstatesthatthepredictionprobabilitiesforclassesapartfromAandBshouldnot
change
(cid:8)
LVS = d [p (x),p (CFE(x))], (8)
div l l
l∈L
whereListhetotalnumberoflabelsforadatapointandp isthepredictedprobabilityfor
l
thespecificlabell,andd measuresthedivergencebetweenthepredictedprobabilityof
div
labell fortheoriginaldatapointx anditsCFE.
OracleScoreissimilartovalidity,however,withanadditionalclassifiertrainedonthesame
dataset as the original classifier. The intuition is that if a CFE is more like an adversarial
example for a classifier, the CFE would not be classified in the desired class by the other
classifier,andhenceweusethepredictionfromtheadditionalclassifierasthegroundtruth
validity.
Notethatseveraloftheevaluationmetricsmightbeatoddswitheachother,forexample,achiev-
inghighdiversitymightcomeatcostofbeingclosetothetrainingdata,orachievinghighvalidity
mightcomeatcostoflowproximity.
Someofthereviewedpapersdidnotevaluatetheiralgorithmonanyoftheabovemetrics.They
onlyshowedacoupleofexampleinputsandrespectiveCFEs(seeAppendixA).
6.3 OtherWorks
This section enlists works that talk about the desirable propertiesof counterfactualsor point to
their issues. We also talk about works that propose minor modifications to previous similar ap-
proaches.
WorksExploringDesirableCFEProperties.SokolandFlach[306]listseveraldesirableproperties
ofcounterfactualsinspiredfromMiller[238]andstatehowthemethodofflippinglogicalcondi-
tionsin adecisiontreesatisfiesmost ofthem. Laugel etal. [209] enlistproximity,connectedness,
andstabilityasthreedesirablepropertiesofaCFEandproposethemetricstomeasurethem.
Works Pointing to Issues with CFEs. Laugel et al. [211] say that if the explanation is not based
ontrainingdata,buttheartifactsofnon-robustnessoftheclassifier,itisunjustified.Theydefine
justifiedexplanationstobeconnectedtotrainingdatabyacontinuoussetofdatapoints,termed
E-chainability.Barocasetal.[30]statefivereasonsthathaveledtothesuccessofcounterfactual
explanationsandalsopointouttheoverlookedassumptions.Theymentiontheunavoidablecon-
flictswhichariseduetotheneedforprivacyinvasioninordertogeneratehelpfulexplanations.
MehediHasanandTalbert[236]statethatgeneratingmultipleCFEsforausermightoverwhelm
them in which case they might choose a suboptimal recourse. They propose a game-theoretic
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:16 S.Vermaetal.
frameworktoovercomethisproblem.KasirzadehandSmart[186]providephilosophicalinsight
intotheimplicitassumptionsandchoicesmadewhengeneratingCFEs.
Causal CFEs. Downs et al. [95] propose using conditional subspace VAEs (CSVAE), a vari-
antofVAEs,togenerateCFEsthatobeycorrelationsbetweenfeatures,causalrelationsbetween
features,andpersonalpreferences.Thismethodbuildsaprobabilisticdatamodelofthetraining
datausingaCSVAEandusesittogenerateCFEs.However,theseCFEsarenotwithrespecttoa
specificMLmodel.Crupietal.[73]proposeatechniquethatcanbeusedwithanycounterfactual
generationapproachtogeneratecausalityabidingCFEs.vonKügelgenetal.[343]extendKarimi
et al. [184]’s work to the setting where unobserved confounders may be present in the causal
setting. de Lara et al. [79] show that optimal transport-based methods are an approximation of
Pearl’sCFEsandhencecanbeusedtogeneratecausalCFEs.Beckers[34]delvesfurtherintothe
integrationofcausality,actualcausation,andCFEs.
CFE for Specific Models. Albini et al. [11] propose a CFE generation approach targeted for
Bayesiannetworkclassifiers.ArteltandHammer[18,19]enliststhecounterfactualoptimization
problemformulationforseveralmodel-specificcases,likegeneralizedlinearmodel,gaussiannaive
Bayes,andmentionthegeneralalgorithmtosolvethem.KoopmanandRenooij[198]proposea
BFS-basedtechniqueforgeneratingCFEsforBayesiannetworks.
WorksConsideringMulti-AgentScenariosofCFEs.TsirtsisandGomez-Rodriguez[327]castthe
counterfactual generation problem as a Stackelberg game between the decision maker and the
personreceivingtheprediction.GivenagroundsetofCFEs,theproposedalgorithmreturnsthe
top-k CFEs, which maximizes the utility of both the involved parties. Bordt et al. [41] point out
thattheinterestsoftheproviderandreceiverofmodelexplanationsmightbeinconflict,andthe
ambiguouspost-hoc explanationsmightbeunsuitableforachievingthepurposeoftransparency
asdesiredinGDPR.Thisalsorelatestofairwashing(seeresearchchallengeRC9).
GlobalCFEs.RawalandLakkaraju[278]proposeAReStogenerateruleliststhatactasglobal
CFEs.Leyetal.[216]andKanamorietal.[180]proposecomputationallymoreefficientimplemen-
tationofRawalandLakkaraju[278]’swork.Carrizosaetal.[53]proposeamixedintegerquadratic
modeltogenerateCFEsforagroupofdatapoints.Warrenetal.[354]andCarrizosaetal.[55]also
proposealgorithmstogenerategroupCFEs.Kooetal.[197]proposegeneratingCFEsforasetof
datapointsusingLagrangianandsubgradientmethods.Pedapatietal.[265]proposeatechnique
totrainagloballyinterpretablemodel(forablack-boxmodel)suchthatthismodelisconsistent
withthepertinentpositivesandpertinentnegatives[87]ofthetrainingdatapointsusedtotrain
theoriginalmodel.
Works Proposing Modifications to Previous Approaches. Chen et al. [63] and De Toni et al. [80]
use RL to generate CFE as was also proposedby Verma et al. [337]. Rasouli and Chieh Yu [272]
proposeageneticalgorithmtogenerateCFEsaswasalsoproposedbyDandletal.[75].Hashemi
andFathi[150]proposetousegeneticalgorithmforCFEgenerationsimilartoDandletal.[75]’s
work. Monteiro and Reynoso-Meza [242] propose extending Dandl et al. [75]’s approach using
U-NSGA-IIIevolutionaryalgorithm.Barretal.[31]extendMahajanetal.[229]’sworkbyinterpo-
latingbetweentheinputandCFEdatapointtogenerateCFEsclosertotheinputdatapoint.Sajja
etal.[289]proposeusingasemi-supervisedautoencoderinsteadofthetraditionalunsupervised
autoencodertogenerateCFEsclosetothetrainingdatamanifold.Huangetal.[160]proposeLORE-
LEYthatextendsLORE[139]togenerateCFEsformulti-classclassificationproblemsandaccount
forflowconstraints.Wijekoonetal.[360]usefeatureimportancesprovidedbyLIMEtoassistthe
case-based reasoning approach to generate CFEs. Delaney et al. [83] propose using trust scores
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:17
tomeasuretheout-of-distributionnessoftheCFEs.GuidottiandRuggieri[141]proposeusingan
ensembleofbaseCFEexplainerstogeneratediverseCFEs.
Benchmark and Dataset Curation. Mazzine and Martens [233] quantitatively compare 10 CFE
generatingapproachesusing22datasetsand9metrics.Pawelczyketal.[260]andArtelt[17]have
developed extensible toolboxes where several CFE approaches can be plugged in and compared
onspecificdatasets.
Semi-Factuals.Semi-factualsarerecentlyproposedkindofexplanationswherethegoalistonot
changethemodelprediction(unlikeCFEs),buttoimprovethecurrentoutcomebychangingthe
input. For example, if Alice’s loan request is approved but her rate of interest is high, how can
Alice change her features such as to get a lower rate of interest. Several works have proposed
novelalgorithmstogeneratesemi-factualexplanations[21,24,189,190].
Various Uncategorized Works. State [308] talks about generating CFEs with real-world con-
straints on features and adaptability with updating ML models using constraint logic program-
ming. Tahoun and Kassis [311] propose to disentangle actions from feature modifications to ad-
dressthelackofinterventiondataandappropriateactioncosts.Theusersshouldalreadydescribe
the actions they are willing to take, and a model should just choose the minimum cost action
thatgeneratestheCFE.Lucicetal.[220]proposeaCFEapproachtoprovidealowerandupper
bound for the feature values that get a low prediction error from the ML model for a datapoint
thatoriginallyhadahighpredictionerror.KorikovandBeck[199]andKorikovetal.[200]show
howCFEscanbegeneratedbyusingthegeneralizationofinversecombinatorialoptimizationand
solve it under two objectives. Pawelczyk et al. [261] provide a general upper bound on the cost
of counterfactual explanations under the phenomenon of predictive multiplicity, wherein more
than one trained model have the same test accuracy and there is no clear winner among them.
Fdez-Sánchezetal.[108]proposeahierarchicaldecompositions-basedmethodtoobtainCFEsfor
multi-classclassificationproblems.Bertossi[35]andMedeirosRaimundoetal.[234]proposebrute
forceapproachestogenerateCFEs.
7 CounterfactualExplanationsforOtherDataModalities
SincewerestrictthissurveytothepapersthatgenerateCFEsfortabulardata,inthissectionwe
pointthereaderstothepapersthatproposealgorithmstargetedtowardsotherdatamodalities:
(1) ImageData:[1,8,9,12,13,29,77,104,109,114,128,135,142,146,151,161,163,168,169,191,
192,207,217,218,237,255,256,266,284,291,304,320,333,334,340,347,359,368,370,377].
(2) TextData:[42,60,175,226,271,275,283,322,368–370].
(3) SpeechData:[375].
(4) Time-SeriesData:[26,82,159,185,310,326,333,351,352].
(5) GraphDataforGraphNeuralNetworks:[2,27,28,105,223,252,355].AsurveyforCFEon
graphneuralnetworks:[268].
(6) AgentAction(e.g.,reinforcementlearningorplanning):[43,257,309].
(7) RecommenderSystems:[81,129,130,176,296,313,324,364,378,380].
(8) FunctionalData:[54,201]andBehavioralData:[271].
8 OtherApplicationsofCounterfactualExplanations
Herewereferthereaderstootherapplicationswherecounterfactualexplanationsarebeingused
apartfromexplainingMLmodels:
(1) AnomalyandData-DriftDetection:HinderandHammer[153]proposetouseCFEstoexplain
datadrift.Sulemetal.[310]proposetouseCFEstoexplainanomaliesintime-seriesdatasets.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:18 S.Vermaetal.
Ravi et al. [276] wrote a survey on the explainability techniques for convolutional auto-
encodersforanomalydetectionofimages.Haldaretal.[148]proposetouseCFEstoexplain
anomalydetectionwhenusingautoencoders.Antoranetal.[15]useCFEstofindchanges
inadatapointthatwouldhelpaclassifierhaveahigherconfidenceinitsprediction.
(2) TrainingDatasetDebugging:YousefzadehandO’Leary[373]proposetouseCFEstodebug
MLmodelsbydiagnosingthebehaviorandusingsyntheticdatatoalterthedecisionbound-
aries. Qi and Chelmis [269] propose to use CFEs to debug potentially mislabeled datasets.
Ganetal.[124]proposetouseCFEstodetectbugsinfinancialmodels.HanandGhosh[149]
proposefindingaminimalsubsetoftrainingdatapointsthatareresponsibleforaparticular
predictionandhencecanbeusedtodebugtrainingdatasets.
(3) DataAugmentation:Yuanetal.[374]proposetouseCFEstoaugmenttrainingdatathatis
used to predict market volatility based on earning calls. Temraz and Keane [316] propose
usingCFEstoaugmenttrainingdatatotackletheclassimbalanceproblem.MehediHasan
and Talbert [235] and Rasouli and Yu [273] propose using CFEs for data augmentation of
tabulardatasetsforincreasedrobustness.Temrazetal.[317]proposeusingCFEstogenerate
datapointsthatcanbeusedtotrainMLmodelsthatpredictcropgrowth(afflictedbyclimate
change).
(4) DrugDesigning:Nguyenetal.[251]useCFEstofindchangesinadrugandproteinmolecule
thatwillincreasetheiraffinityforeachother.Theyusemulti-agentRLtothisend.
(5) ML Model Bias Detection: Myers et al. [246] build a visualization tool based on computing
CFEs to expose biases in ML models. Fawkes et al. [107] point out to the challenges with
usingCFEsfor fairness.OtherworksalsouseCFEstomeasureandmitigate modelbiases
[205,331].
(6) Various Applications: Mazzine et al. [232] propose to use CFEs in employment services to
helpjobseekersgetpersonalizedadviceforincreasingtheirpropensityforgettingrecom-
mendedforajobandtohelptheMLdeveloperstodetectpotentialbiasandotherissuesin
theirMLmodel.Sadleretal.[288]proposetouseCFEsforcommunitydetectioninsocial
networks.Fujiwaraetal.[121]proposetouseCFEstounderstandinteractivedimensionality
reduction.TsiakmakiandRagos[325]proposetouseCFEsforprovidingactionablesugges-
tionstoimprovestudentperformanceinauniversitycourse.Congetal.[69]proposeaCFE
approachtoexplainwhyatestsetfailstheKolmogorov-Smirnovtest.Marchezinietal.[230]
proposetouseCFEforalteringbothobservationalandlatentvariablestoreasonaboutmen-
talhealth.Yaoetal.[371]proposetousecounterfactualsforevaluatingtheexplanationsfor
recommender systems. Gupta et al. [144] use CFEs to propose changes to constraint satis-
faction problems that have no solutions. Teofili et al. [318] propose using CFEs to explain
entityresolutionmodels.Arteltetal.[22]useCFEstoexplainthedifferencesbetweenthe
learning of a pair of models. Frohberg and Binder [120] propose CRASS, a dataset to test
counterfactualreasoningofLLMs.
There has been one case of real-world deployment of CFEs in a hiring platform, Hired. Ne-
mirovskyetal.[249]useaGAN-basedapproach[250]togeneratecounterfactualsinordertoget
candidatesapprovedbytheHiredMarketplaceMLmodel.Theirapproachsatisfiesseveralofthe
desideratawediscussedinSection4.1,forexample:
(1) theyconsiderfeatureactionabilityandonlychangethemutablefeatureslikeexpectedsalary,
yearsofexperience,andskills;
(2) their loss function encourages proximity and they use L1 distance between the generated
counterfactualandtheinputdatapointtomeasureit;
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:19
(3) theyuseaGAN-basedapproachtogeneratecounterfactualsthatareclosetothedatamani-
foldanduseanauto-encoderreconstructionerrortomeasureit;
(4) their approach was designed to amortize the optimization process and they measure the
counterfactualgenerationtimetomeasurelatency.
9 OpenQuestionsandResearchProgress
Inthefirstversionofthissurveypaper,wedelineatedtheopenquestionsandchallengesyetto
betackledbytheexistingworkspertainingtoCFEs[336].Alotofprogresshasbeenmadebythe
researchcommunityandseveraloftheopenchallengeshavebeensolved(mentionedinthelater
section).Inthisversionofthepaper,wehighlightasetofmainresearchproblemsthatareyetto
beaddressedandinviteresearcherstotacklethem.
9.1 CurrentOpenQuestions
ResearchChallenge1. Counterfactualexplanationsshouldcapturetheapplicant’spreferences.
Along with the distinction between mutable and immutable features (finely classified into ac-
tionable, mutable, and immutable), counterfactual explanations should also capture preferences
specifictoanapplicant.Thisisimportantbecausetheeaseofchangingdifferentfeaturescandif-
feracrossapplicants.
Progress: Mahajan et al. [229] captures the applicant’s preferences using an oracle, but that
is expensive and is still a challenge. Rawal and Lakkaraju [278] use the Bradley-Terry model to
learn the pairwise cost for each feature pair and hence the preference among them. Yadav et al.
[366]arguethatassumingeachuser’scostofchangingdifferentfeaturesisthesameisunrealistic.
Theyproposeaskingfortheuser’scostfunctionorcomputingtheexpectationbysamplingcost
functionsfromadistribution.Despitetheprogress,incorporatinguserpreferenceshasnotbeen
standardizedandremainsanexpensiveandelusiveprocess.Ideally,atechniqueshouldbeableto
collectpreferencesasarankedlistoffeaturesandprovideCFEsthatadheretoit.
ResearchChallenge2. Counterfactualexplanationsshouldhandledynamics(datadrift,classi-
fierupdate,applicant’sutilityfunctionchanging,etc.)
Allcounterfactualexplanationpaperswereviewassumethattheunderlyingblackboxismono-
tonicanddoesnotchangeovertime.However,thismightnotbetrue;creditcardcompaniesand
banksupdatetheirmodelsasfrequentlyas12-18months[126].Therefore,counterfactualexpla-
nationalgorithmsshouldtakedatadriftandthedynamismandnon-monotonicityoftheclassifier
intoaccount.Therehasnotbeenmuchworkforaddressingthisresearchquestion.
ResearchChallenge3. Theabilityofcounterfactualexplanationstoworkwithmissingfeature
values.
Counterfactual explanation algorithms should also be able to handle missing feature values,
whichoftenhappensintherealworld[125].Therehasnotbeenmuchworkforaddressingthis
researchquestion.
ResearchChallenge4. Preservingmodelprivacy.
Privacy attacks on ML models can come in two major forms: member inference and model
extraction. Both of theseprivacy attackscan be enhanceddue to theprovision of CFEs. Aïvodji
et al. [7] empirically demonstrate that adversaries can train a surrogate model with very high
fidelitytotheoriginalmodel(i.e.,modelextractionattack)withasfewas1,000queriestothemodel
(whichisrequiredduringCFEgeneration).TheproblemisfurtheraggravatedwhendiverseCFEs
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:20 S.Vermaetal.
areprovided.Shokrietal.[299]havedemonstratedthatgradient-basedexplanationsmethodsleak
alotofinformationandmakethemodelsvulnerabletomembershipinferenceattacks.Miuraetal.
[240]proposeMEGEX,adata-freemodelextractionattackthatlearnsasurrogatemodelwithout
accesstoitstrainingdatabytrainingagenerativemodel.Wangetal.[350]proposeusingtheCFE
ofaCFEtotrainasurrogatemodelandshowthatitismoreefficientinmodelextractionwhen
comparedto[7].MostoftheworkspointouttothechallengesCFEpresentsfortheprivacyofthe
models,whilethesolutionsremainelusive.
ResearchChallenge5. Counterfactualexplanationsasaninteractiveservicetotheapplicants.
Counterfactualexplanationsshouldbeprovidedasaninteractiveinterface,whereanindividual
cancomeatregularintervals,informthesystemofthemodifiedstate,andgetupdatedinstructions
toachievethecounterfactualstate.Thiscanhelpwhentheindividualcouldnotpreciselyfollow
theearlieradviceforvariousreasons.
Progress: Hohman et al. [155] developed an interactive user-interface for providing expla-
nations to data scientists. They found out that data scientists used interactivity as the primary
mechanismforexploring,comparing,andexplainingpredictions.SokolandFlach[305]propose
toenhanceMLexplanationswithavoice-assistedinteractiveservice.Akulaetal.[9]proposeanap-
proachthatexplainsanMLmodelusinganinteractivesequenceofCFEs.Wangetal.[349]propose
refiningtheCFEsfordifferentfeaturechangecostsbasedonuserinteractions.Anidealapproach
to solve this problem would develop an interactive platform that will tailor a counterfactual for
theupdatedfeaturesateachstepoftheinteraction.
ResearchChallenge6. Counterfactualexplanationsshouldaccountforbiasintheclassifier.
Counterfactualspotentiallycaptureandreflectthebiasinthemodels.Tounderscorethisasa
possibility,Ustunetal.[331]experimentedonthedifferenceinthedifficultyofattainingacoun-
terfactualstateacrossgenders,whichclearlyshowedasignificantdifference.Moreworkmustbe
donetofindhowequallyeasycounterfactualexplanationscanbeprovidedacrossdifferentdemo-
graphicgroups,orhowadjustmentsshouldbemadetotheprescribedchangestoaccountforthe
bias.
Progress: RawalandLakkaraju[278]generaterecourserulesforasubgroupthattheyuseto
detectmodelbiases.Guptaetal.[145]proposeaddingaregularizerwhiletrainingaclassifierthat
encourages the classifier to maintain a similar distance of the decision boundary from different
demographic groups, thereby facilitating the opportunity of equal recourse across demographic
groups(whichistheirdefinitionoffairness).vonKügelgenetal.[344]extendthisfairnessnotion
whenthedistancebetweentherecourseismeasuredinacausalmanner.Galhotraetal.[123]pro-
poseLEWISthatusesCFEstoidentifyracialbiasinCOMPASandgenderinAdultdatasets.Dash
etal.[77]proposeusingCFEstodetectbiasinimageclassifiersandcounterfactualregularizerto
counteractthatbias.However,anapproachthatconsiderthebiasoftheclassifierwhilegenerating
CFEsstillsneedstoberesearched.
ResearchChallenge7. Generatingoptimalrecourseswhenconsideringamulti-agentscenario.
O’Brien and Kim [253] demonstrate the non-optimality of recourses generated when a single
agent’s interest is considered in a multi-agent scenario like the prisoner’s dilemma. In the real
world,anagent’sactionsaffectotheragents,hencegeneratingrecoursesthatconsidertheinterests
of multiple agents would be useful. Therehas not been much work for addressing this research
question.
Research Challenge 8. Strengthen the ties between machine learning and regulatory commu-
nities.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:21
Ajointstatementbetweenthemachinelearningcommunityandregulatorycommunity(OCC,
FederalReserve,FTC,CFPB)acknowledgingsuccessesandlimitationsofwherecounterfactualex-
planationswillbeadequateforlegalandconsumer-facingneedsandwouldimprovetheadoption
anduseofcounterfactualexplanationsincriticalsoftware.
Progress: Reed et al. [280] talk about how regulation and policies need to adapt to how ML
modelscanexplaintheirdecisions.Howevermuchmoreneedstobedoneinordertoenhancethe
adoptionofCFEs.
ResearchChallenge9. Guardingagainstfairwashing.
Aivodjietal.[5,6]havepointedouttheriskofanadversaryusingmodelexplanationstoratio-
nalizeamodel’sdecisionsandobscureitsbias.Itremainstobeseenifthefairrecourseapproaches
canguardagainstfairwashing.
ResearchChallenge10. Enhancereal-worlddeploymentofcounterfactuals.
Progress: Therehasbeenoneknowncaseofreal-worlddeploymentofcounterfactualsatHired
platformsforprovidingadvicetocandidatesseekingjobs[250].DeployingCFEsinmorerealworld
applicationswillimproveourunderstandingofuserpreferencesandhighlightnewresearchchal-
lenges.
Research Challenge 11. Counterfactual explanations should also inform the applicants about
whatmustnotchange
Suppose a CFE advises someone to increase their income but does not tell that their length of
last employment should not decrease. To increase their income, the applicant who switches to a
higher-payingjobmayfindthemselvesinaworsepositionthanearlier.Thus,byfailingtodisclose
whatmustnotchange,anexplanationmayleadtheapplicanttoanunsuccessfulstate[30].This
corroboratesRC5,wherebyanapplicantmightbeabletointeractwithaplatformtoseetheeffect
ofapotentialreal-worldactiontheyareconsideringtakingtoachievethecounterfactualstate.
9.2 QuestionswithSignificantResearchProgress
Inthissection,wehighlighttheresearchprogressmadefortowardspreviouslyopenquestions.
ResearchProblem1. Unifycounterfactualexplanationswithtraditional“explainableAI.”
Althoughcounterfactualexplanationshavebeencreditedtoelicitingcausalthinkingandprovid-
ingactionablefeedbacktousers,theydonottellwhichfeature(s)wastheprincipalreasonforthe
originaldecisionandwhy.Itwouldbeniceif,alongwithgivingactionablefeedback,counterfac-
tualexplanationsalsogavethereasonfortheoriginaldecision,whichcanhelpapplicantsunder-
standthemodel’slogic.Thisisaddressedbytraditional“explainableAI”methodslikeLIME[281],
Anchors[282],Grad-CAM[294].
Progress: Guidottietal.[139]haveattemptedthisunification,astheyfirstlearnalocaldeci-
siontreeandtheninterprettheinversionofdecisionnodesofthetreeascounterfactualexplana-
tions.However,theydonotshowtheCFEstheygenerate,andtheirtechniquealsomissesother
desiderataofcounterfactuals(seeSection4.1).KommiyaMothilaletal.[196]proposenecessityand
sufficiencyasthetwoimportantpropertiesofanexplanation.Featureattributionexplanationsfind
thefeaturevaluesthataresufficientforaprediction,whileCFEsfindthefeaturevaluesthatare
necessaryforaprediction.Theyproposemethodstofindthenecessityandsufficiencyofanyfea-
ture subset and discuss how that aligns with finding CFEs. Galhotra et al. [123] propose Lewis
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:22 S.Vermaetal.
thatalsoemphasizesthenecessityandsufficiencyscoresofafeaturesubsetinfindingitsglobalim-
portanceandingeneratingaCFEforlocalexplainability.Jiaetal.[171]proposetouseDeepLIFT
to assign contribution scores to the features that changed in a counterfactual datapoint. Ramon
etal.[271]rankthefeatureimportancesusingLIMEandSHAP,andthenremovethefeaturesin
decreasingorderofimportanceuntilaCFEisfound.Wiratungaetal.[361]proposetousemethods
likeLIMEandSHAPtofindfeatureimportancesandthenreplacethefeaturesindecreasingorder
ofimportancewiththevaluesborrowedfromthenearestunlikeneighbor(case-basedreasoning
approach).Albinietal.[10]proposetochangethebackgrounddistributionusedtocomputethe
Shapleyvaluestomakethefeatureattributionamounttothecounterfactual-abilityofthefeatures,
i.e., changing a feature with higher attribution would have a higher probability of changing the
prediction.WangandVasconcelos[347]proposetousethediscriminantattributionexplanations
asawaytoproduceCFEsforimages.Wijekoonetal.[360]useLIMEtoassistcase-basedreasoning
techniquestogenerateCFEs.Geetal.[127]proposeusingcounterfactual-abilityoffeaturesasa
metricfortheirfeatureimportance.
Research Problem 2. Provide counterfactual explanations as discrete and sequential steps of
actions.
Mostcounterfactualgenerationapproachesreturnthemodifieddatapoint,whichwouldreceive
the desired classification. The modified datapoint (state) reflects the idea of instantaneous and
continuousactions,butintherealworld,actionsarediscreteandoftensequential.Therefore,the
counterfactualgenerationprocessmusttakethediscretenessofactionsintoaccountandprovidea
seriesofactionsthatwouldtaketheindividualfromthecurrentstatetothemodifiedstate,which
hasthedesiredclasslabel.
Progress: Naumann and Ntoutsi [247] argue that to help an individual achieve the desired
goal, CFEs should be provided as a sequential step of actions instead of just providing the final
goal. Singh et al. [300] conduct a user study to show the high preference for a sequential step
of actions steps over a single-step goal. Ramakrishnan et al. [270] propose a program synthesis
basedtechniquetogeneratesuchsequences.Kanamorietal.[181]proposeamixed-integerbased
programmingmethodandVermaetal.[337]proposeanRL-basedmethodthatgeneratesordered
sequencesofactionsasaCFE.
Research Problem 3. The ability of counterfactual explanations to work with incomplete—or
missing—causalgraphs.
IncorporatingcausalityinthecounterfactualgenerationisessentialfortheCFEstobegrounded
inreality.Completecausalgraphsandstructuralequationsarerarelyavailableintherealworld,
andthereforethealgorithmshouldbeabletoworkwithincompletecausalgraphs.
Progress: Mahajanetal.[229]’sapproachwasthefirsttobecompatiblewithincompletecausal
graphs.NowotherworkslikeGalhotraetal.[123],Vermaetal.[337],Schleichetal.[292],Yang
etal.[367]canalsoworkwithpartialcausalgraphs.
ResearchProblem4. Scalabilityandthroughputofcounterfactualexplanationsgeneration.
AsweseeinTable1,mostapproachesneedtosolveanoptimizationproblemtogenerateone
counterfactualexplanation.Somepapersgeneratemultiplecounterfactualswhileoptimizingonce,
but they still need to optimize separately for different input datapoints. However, for industrial
deployment,thegenerationshouldbemorescalable.
Progress: Mahajan et al. [229] learn a VAE which can generate multiple CFEs for any given
inputdatapointaftertraining.Therefore,theirapproachishighlyscalableandistermedas“amor-
tizedinference”.Vermaetal.[337]proposedanRL-basedtechnique,FastAR,thatalsogenerates
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:23
amortized CFEs. Van Looveren et al. [333], Samoilescu et al. [290], Yang et al. [367], Rawal and
Lakkaraju[278],andNemirovskyetal.[250]alsoproposeapproachestothisend.
ResearchProblem5. Generaterobustcounterfactualexplanations[112,239].
Counterfactual explanation optimization problems force the modified datapoint to obtain the
desiredclasslabel.However,themodifieddatapointcouldbelabeledeitherinarobustmanneror
duetotheclassifier’snon-robustness,e.g.,anoverfittedclassifier.Laugeletal.[209]termthisas
thestabilitypropertyofacounterfactual.Therearethreekindsofrobustnessneeds:(1)robustness
tomodelchangeswhenmodelsareretrained,forexample,(2)robustnesstotheinputdatapoint
(twoindividualswithaslightchangeinfeaturesshouldbegivensimilarCFEs),and(3)robustness
tosmallchangesintheattainedCFE(aCFEwithminorchangestotheoriginallysuggestedCFE
shouldalsobeaccepted).
Progress: Slacketal.[302]underscorethischallengebyshowingthatsmallperturbationsin
theinputdatapointscanresultindrasticallydifferentCFEs.Rawaletal.[277]furtheremphasize
thischallengebyempiricallydemonstratingtheinvalidationofalreadyprescribedrecourseswhen
theMLmodelgetsretrainedondatasetswithtemporalorgeospatialdistributionshifts.Arteltetal.
[23]evaluatetherobustnessofclosestCFEswhencontrastedwithCFEsgeneratedwiththedata
manifoldconstraint.Bueffetal.[47]proposetheframeworktomeasuretherobustnessofmodels
by purposing generated CFEs as adversarial attack datasets. Virgolin and Fracaros [342] empiri-
callyshowthatnon-robustCFEsencounterahighercostofchangewhenadverseperturbations
areappliedtothedatapoint,thusconcludingthatrobustnessinCFEsshouldbeconsidered.
Upadhyayetal.[330]proposeatechniquenamedROAR thatusesadversarialtrainingtogen-
erate recourses robust to changes in an ML model that is retrained on a distributionally shifted
training dataset. Dominguez-Olmedo et al. [93] show that the CFEs that just cross the decision
boundaryareusuallynon-robustandformulateanoptimizationproblemthatgeneratesrobustre-
courseforlinearmodelsandneuralnetworks.Pawelczyketal.[262]proposeatechniquenamed
PROBE that generates robust CFEs while letting the users decide the tradeoff between the CFE
invalidationriskanditscost.Blacketal.[37]arguethatrobustCFEsshouldhavehigh=confidence
neighborhoodswithsmallLipschitzconstants,andproposeaStableNeighborSearchalgorithmto
thatend.Buietal.[48]proposeanalgorithmtogeneraterobustCFEsbyconsideringadistribution
overtheparametersofthemodelifretrained.Duttaetal. [103]proposecounterfactualstability
(the lower bound of the predicted class probability for the sampled datapoints in the neighbor-
hoodofagivenCFE)asametricforfilteringrobustCFEs.Bajajetal.[28]proposeatechniqueto
generaterobustCFEsforgraphneuralnetworks.
ResearchProblem6. Extendcounterfactualexplanationsbeyondclassification.
Progress: Recentworkhasbeenextendingcounterfactualexplanationstodifferenttasksand
model architectures. Spooner et al. [307] propose a Bayesian optimization-based technique for
generating CFEs for regression problems. Numeroso and Bacciu [252] propose an RL-based ap-
proachforgeneratingCFEsforgraphneuralnetworks,whichareusedtopredictchemicalmole-
culeproperties.Delaneyetal.[82]proposeacase-basedreasoningapproachtogenerateCFEsfor
atime-seriesclassifier.
ResearchProblem7. Handlingofcategoricalfeaturesincounterfactualexplanations
Differentarticleshavecomeupwithvariousmethodstohandlecategoricalfeatures,likecon-
verting them to one-hot encoding and then enforcing the sum of those columns to be 1 using
regularization or a hard constraint, or clamping an optimization problem to a specific categori-
cal value, or leaving them to be automatically handled by genetic approaches and SMT solvers.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:24 S.Vermaetal.
Measuringdistanceincategoricalfeaturesisalsonotobvious.Somearticlesuseanindicatorfunc-
tion, which equates to 1 for unequal values and 0 if the same; other papers convert to one-hot
encodingandusestandarddistancemetricslikeL1/L2norm,orusethedistanceinMarkovchains
[115].Therefore,handlingcategoricalvariableshavenotbeenstandardized,futureresearchmust
considerthisanddevelopappropriatemethods.
ResearchProblem8. Evaluatecounterfactualexplanationsusingauserstudy.
Theevaluationforcounterfactualexplanationsmustbedoneusingauserstudybecauseeval-
uationproxies(seeSection6)mightnotbeabletopreciselycapturethepsychologicalandother
intricaciesofhumancognitionontheeaseofactionabilityofacounterfactual.Keaneetal.[187]
emphasizetheimportanceofuserstudiesinthecontextofCFEs.
Progress: Förster et al. [116] conduct a user study with 144 participants to understand the
formatofexplanationtheyprefer.Theyconcludethatuserspreferconcrete,consistent,relevant
explanations,andlengthyexplanationsiftheyareconcrete.Försteretal.[115]conductauserstudy
with46participantswhowereaskedtoratetherealisticnessoftheCFEsgeneratedbytheirsand
a baseline approach. Using statistical tests, they concluded that the CFEs generated by their ap-
proach were perceived to be more real and typical. Rawal and Lakkaraju [278] conduct a user
studywith21participantswhowereaskedtodetectabiasintherecoursesummariesfordemo-
graphicgroups.Kanamorietal.[180]conductauserstudywith35participantstocomparetheir
globalCFEgeneratingtechniquewiththatofRawalandLakkaraju[278].Singhetal.[300]conduct
auserstudywith54participantsandfoundthatmostuserspreferspecificdirectivesovergeneric
andnon-directiveexplanations.Warrenetal.[353]conductauserstudywith127participantsand
foundthatcounterfactualexplanationselicitedhighertrustandsatisfactionthancausalexplana-
tions. Yacoby et al. [365] conduct a user study with eight U.S. state court judges to understand
theirresponsetoCFEsfrompretrialriskassessmentinstruments(PRAI).Theyconcludethat
judges ignored the CFEs and focused on the factual features of the defendant. Kuhl et al. [204]
conduct a user study with 74 users in an interactive game setting and found that users benefit
lessfromreceivingcomputationallyplausibleCFEsthantheclosestCFEs(measuredusingfeature
distance). Zhang. et al. [376] conduct a user study with 200 users to check their understanding
ofglobal,local,andCFexplanations.Caietal.[51]conductauserstudyon1070participantsto
understand how users perceive explanations when provided examples from the desired class vs.
whenprovidedexamplesfromallotherclasses.CelarandByrne[57]conductauserstudywith
731participantsandconcludedthatcounterfactualexplanationswereperceivedtobebetterexpla-
nationsthanfactualexplanations(explanationsjustifyingtheoriginalmodelprediction).Daietal.
[74]conductauserstudywith243participantsandfoundthatcounterfactualandprefactualexpla-
nationswereequallyhelpful.Delaneyetal.[84]conductauserstudyandfoundthatparticipants
preferlarge,meaningfuleditsforcounterfactualexplanationsforimages.
ResearchProblem9. Counterfactualexplanationsshouldbeintegratedwithdatavisualization
interfaces.
Counterfactualexplanationswilldirectlyinteractwithconsumerswithvaryingtechnicalknowl-
edge levels; therefore, counterfactual generation algorithms should be integrated with visualiza-
tion interfaces. We already know that visualization can influence human behavior [70], and a
collaborationbetweenmachinelearningandHCIcommunitiescouldhelpaddressthischallenge.
Progress: Chengetal.[64],Gomezetal.[132,133],Leungetal.[214],andWexleretal.[356]
havedevelopedinteractivegraphicaluserinterfacesfordisplayingCFEs.DECE[64]alsosumma-
rizesCFEsforsubgroupsthatcanhelpdetectmodelbiases,ifany.Tamagninietal.[312]develop
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:25
avisualizationtoolforCFEsfortextclassificationmodels.Hohmanetal.[155]alsobuildavisual
interactiveuserinterfaceforprovidingmodelexplanations.
ResearchProblem10. Incentivizeuserstoimprovefeaturesinnon-manipulativeways.
Anapproachthatprovidesarecoursetousersmightwanttopreventthe“gamification”ofthe
model (when users manipulate simple features like thepurposeof a loan to get approved). This
alsoprotectstheMLmodelsfromadversarialrobustnessattacks.
Progress: Chenetal.[62]proposetheoptimizationobjectiveforlinearclassificationmodels
when the goal is to develop an accurate model that encourages actual feature improvement for
users.Theycategorizefeaturesintothreecategories:improvement,manipulative,andimmutable.
Usersshouldbeencouragedtochangetheimprovementfeatures,notthemanipulativeoneswhen
optimizingforrecourse.Königetal.[206]suggestusingcausalitytogeneratemeaningfulrecourses
andpreventgamificationofthemodel.
10 Conclusions
In this article, we collected and reviewed more than 350 papers which proposed various algo-
rithmicsolutionstofindingcounterfactualexplanationsforthedecisionsproducedbyautomated
systems,specificallyautomatedbymachinelearning.Evaluatingallthepapersonthesamerubric
helpsinquicklyunderstandingthepeculiaritiesofdifferentapproachesandtheadvantages,and
disadvantagesofeachofthem,whichcanalsohelporganizationschoosethealgorithmbestsuited
to their application constraints. This has also helped us readily identify the gaps, which will be
beneficial to researchers scouring for open problems in this space and quickly sifting the large
bodyofliterature.Wehopethisarticlecanalsobethestartingpointforpeoplewantingtogetan
introductiontothebroadareaofcounterfactualexplanationsandguidethemtoproperresources
forthingstheymightbeinterestedin.
Appendices
A FullTable
Initially, we categorized the set of papers with more columns and in a much larger table. We
selectedthemostcriticalcolumnsandputtheminTable1.Thefulltableisavailablehere.
B BurgeoningLegalFrameworksaroundExplanationsinAI
To increase the accountability of automated decision systems—specifically, AI systems—laws
and regulations regarding the decisions produced by such systems have been proposed and
implemented across the globe [94]. The most recent version of the European Union’s General
Data Protection Regulation (GDPR), enforced starting on May 25, 2018, offered a right to
informationabouttheexistence,logic,andenvisagedconsequencesofsuchasystem[134].This
also includes the right to not be a subject of an automated decision-making system. Although
the closeness of this law to “right to explanation” is debatable and ambiguous [345], the official
interpretationbyWorkingPartyforArticle29hasconcludedthattheGDPRrequiresexplanations
of specific decisions, and therefore counterfactual explanations are apt. In the US, the Equal
Credit Opportunity Act (ECOA) and the Fair Credit Reporting Act (FCRA) require the
creditortoinform thereasonsforanadverseaction,suchasrejectionofaloanrequest[58,59].
Theygenerallycomparetheapplicant’sfeaturetotheaveragevalueinthepopulationtoarriveat
theprincipalreasons.GovernmentreportsfromtheUnitedKingdom[254]andFrance[166,341]
also touched on the issue of explainability in AI systems. In the US, Defense Advanced
Research Projects Agency (DARPA) launched the Explainable AI (XAI) program in 2016
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:26 S.Vermaetal.
to encourage research into designing explainable models, understanding the psychological
requirements of explanations, and the design of explanation interfaces [76]. The European
Union has taken similar initiatives as well [67, 329]. The US White House recently put forward
the Blueprint for an AI Bill of Rights [158] to modulate decisions from automated systems.
The Bill outlines five principles for operating such systems: (1) safe and effective systems, (2)
algorithmicdiscriminationprotections,(3)dataprivacy,(4)explanationsfordecisionsmadeusing
such systems, and (5) discussion about human alternatives. While many techniques have been
proposedforexplainablemachinelearning,itisyetunclearifandhowthesespecifictechniques
can help address the letter of the law. Future collaboration between AI researchers, regulators,
the legal community, and consumer watchdog groups will help ensure the development of
trustworthyAI.
Acknowledgments
WethankJasonWittenbach,AdityaKusupati,DivyatMahajan,JessicaDai,SoumyeSinghal,Harsh
Vardhan,andJesseMichelforhelpfulcomments.
References
[1] AbubakarAbid,MertYuksekgonul,andJamesZou.2022.Meaningfullydebuggingmodelmistakesusingconceptual
counterfactualexplanations.InProceedingsofthe39thInternationalConferenceonMachineLearning.PMLR,66–88.
https://proceedings.mlr.press/v162/abid22a.html
[2] CarloAbrateandFrancescoBonchi.2021.Counterfactualgraphsforexplainableclassificationofbrainnetworks
(KDD’21).ACM,NewYork,10.https://doi.org/10.1145/3447548.3467154
[3] AminaAdadiandMohammedBerrada.2018.Peekinginsidetheblack-box:Asurveyonexplainableartificialintelli-
gence(XAI).IEEEAccessPP(092018),1–1.https://doi.org/10.1109/ACCESS.2018.2870052
[4] CharuC.Aggarwal,ChenChen,andJiaweiHan.2010.Theinverseclassificationproblem.J.Comput.Sci.Technol.
(2010),458–468.https://doi.org/10.1007/s11390-010-9337-x
[5] UlrichAïvodji,HiromiArai,OlivierFortineau,SébastienGambs,SatoshiHara,andAlainTapp.2019.Fairwashing:
Theriskofrationalization.InProceedingsofthe36thInternationalConferenceonMachineLearning.PMLR.https://
proceedings.mlr.press/v97/aivodji19a.html
[6] UlrichAïvodji,HiromiArai,SébastienGambs,andSatoshiHara.2021.Characterizingtheriskoffairwashing.In
AdvancesinNeuralInformationProcessingSystems,Vol.34.CurranAssociates,Inc.https://proceedings.neurips.cc/
paper/2021/file/7caf5e22ea3eb8175ab518429c8589a4-Paper.pdf
[7] UlrichAïvodji,AlexandreBolot,andSébastienGambs.2020.Modelextractionfromcounterfactualexplanations.
arXiv:2009.01884(2020).
[8] ArjunAkula,ShuaiWang,andSong-ChunZhu.2020.CoCoX:Generatingconceptualandcounterfactualexplana-
tionsviafault-lines.InProceedingsoftheAAAIConferenceonArtificialIntelligence34,03(Apr.2020),2594–2601.
https://doi.org/10.1609/aaai.v34i03.5643
[9] ArjunR.Akula,KezeWang,ChangsongLiu,SariSaba-Sadiya,HongjingLu,SinisaTodorovic,JoyceChai,andSong-
ChunZhu.2022.CX-ToM:Counterfactualexplanationswiththeory-of-mindforenhancinghumantrustinimage
recognitionmodels.iScience25,1(2022),103581.https://doi.org/10.1016/j.isci.2021.103581
[10] EmanueleAlbini,JasonLong,DanialDervovic,andDanieleMagazzeni.2022.Counterfactualshapleyadditiveexpla-
nations(FAccT’22).ACM,NewYork,17.https://doi.org/10.1145/3531146.3533168
[11] EmanueleAlbini,AntonioRago,PietroBaroni,andFrancescaToni.2021.Influence-drivenexplanationsforBayesian
networkclassifiers.InPRICAI2021.Springer-Verlag,Berlin,,13.https://doi.org/10.1007/978-3-030-89188-67
[12] GoharAli,FerasAl-Obeidat,AbdallahTubaishat,TehseenZia,MuhammadIlyas,andAlvaroRocha.2021.Counter-
factualexplanationofBayesianmodeluncertainty.NeuralComputingandApplications(Sept.2021).https://doi.org/
10.1007/s00521-021-06528-z
[13] KamranAlipour,ArijitRay,XiaoLin,MichaelCogswell,JurgenP.Schulze,YiYao,andGiedriusT.Burachas.2021.
Improvingusers’mentalmodelwithattention-directedcounterfactualedits.AppliedAILetters 2,4(2021).https:
//doi.org/10.1002/ail2.47
[14] RobertAndrews,JoachimDiederich,andAlanB.Tickle.1995.Surveyandcritiqueoftechniquesforextractingrules
fromtrainedartificialneuralnetworks.Know.-BasedSyst.8,6(1995),17.https://doi.org/10.1016/0950-7051(96)81920-
4
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:27
[15] JavierAntoran,UmangBhatt,TameemAdel,AdrianWeller,andJoséMiguelHernández-Lobato.2021.Gettinga
CLUE:Amethodforexplaininguncertaintyestimates.InProceedingsoftheInternationalConferenceonLearning
Representations.https://openreview.net/forum?id=XSLF1XFq5h
[16] DanielApleyandJingyuZhu.2020.Visualizingtheeffectsofpredictorvariablesinblackboxsupervisedlearning
models.JournaloftheRoyalStatisticalSociety:SeriesB(StatisticalMethodology)82(4)(062020),1059–1086.https://
doi.org/10.1111/rssb.12377
[17] André Artelt. 2019 - 2021. CEML: Counterfactuals for Explaining Machine Learning Models. https://www.
github.com/andreArtelt/ceml
[18] AndréArteltandBarbaraHammer.2019.OntheComputationofCounterfactualExplanations–ASurvey.http://
arxiv.org/abs/1911.07749
[19] André Artelt and Barbara Hammer. 2020. Efficient Computation of Contrastive Explanations. https://doi.org/
10.48550/ARXIV.2010.02647
[20] AndréArteltandBarbaraHammer.2021.ConvexOptimizationforActionable&PlausibleCounterfactualExplana-
tions.https://doi.org/10.48550/ARXIV.2105.07630
[21] AndréArteltandBarbaraHammer.2022.“Evenif...”–DiverseSemifactualExplanationsofReject.arXiv:2207.01898
[22] AndréArtelt,FabianHinder,ValerieVaquet,RobertFeldhans,andBarbaraHammer.2021.Contrastiveexplana-
tionsforexplainingmodeladaptations.InAdvancesinComputationalIntelligence.SpringerInternationalPublishing,
Cham,101–112.https://doi.org/10.1007/978-3-030-85030-29
[23] AndréArtelt,ValerieVaquet,RizaVelioglu,FabianHinder,JohannesBrinkrolf,MalteSchilling,andBarbaraHammer.
2021.Evaluatingrobustnessofcounterfactualexplanations.InProceedingsofthe2021IEEESymposiumSerieson
ComputationalIntelligence(SSCI)(2021),01–09.https://doi.org/10.1109/SSCI50451.2021.9660058
[24] SaugatAryal.2024.Semi-factualexplanationsinAI.InProceedingsoftheAAAIConferenceonArtificialIntelligence
38(2024),23379–23380.https://doi.org/10.1609/aaai.v38i21.30390
[25] NicholasAsher,LucasDeLara,SoumyaPaul,andChrisRussell.2022.Counterfactualmodelsforfairandadequate
explanations.MachineLearningandKnowledgeExtraction4,2(2022),316–349.https://doi.org/10.3390/make4020014
[26] EmreAtes,BurakAksar,VitusJ.Leung,andAyseK.Coskun.2021.Counterfactualexplanationsformultivariate
timeseries.InProceedingsofthe2021InternationalConferenceonAppliedArtificialIntelligence(ICAPAI’21).1–8.https:
//doi.org/10.1109/ICAPAI49758.2021.9462056
[27] DavideBacciuandDaniloNumeroso.2022.Explainingdeepgraphnetworksviainputperturbation.IEEETransactions
onNeuralNetworksandLearningSystems(2022).https://doi.org/10.1109/TNNLS.2022.3165618
[28] MohitBajaj,LingyangChu,ZiYuXue,JianPei,LanjunWang,PeterCho-HoLam,andYongZhang.2021.Robust
CounterfactualExplanationsonGraphNeuralNetworks.https://doi.org/10.48550/ARXIV.2107.04086
[29] RachanaBalasubramanian,SamuelSharpe,BrianBarr,JasonWittenbach,andC.BayanBruss.2020.Latent-CF:A
SimpleBaselineforReverseCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2012.09301
[30] SolonBarocas,AndrewD.Selbst,andManishRaghavan.2020.Thehiddenassumptionsbehindcounterfactualex-
planations and principal reasons. In Proceedings of the Conference on Fairness, Accountability, and Transparency
(FAccT’20)(FAT*’20).ACM,NewYork,10.https://doi.org/10.1145/3351095.3372830
[31] BrianBarr,MatthewR.Harrington,SamuelSharpe,andC.BayanBruss.2021.CounterfactualExplanationsviaLatent
SpaceProjectionandInterpolation.https://doi.org/10.48550/ARXIV.2112.00890
[32] C.VanFraassenBas.1980.TheScientificImage.OxfordUniversityPress.
[33] BarryBeckerandRonnyKohavi.1996.Adult.UCIMachineLearningRepository.https://doi.org/10.24432/C5XW20
[34] SanderBeckers.2022.CausalExplanationsandXAI.https://doi.org/10.48550/ARXIV.2201.13169
[35] LeopoldoBertossi.2021.Declarativeapproachestocounterfactualexplanationsforclassification.TheoryandPractice
ofLogicProgramming23(122021),1–35.https://doi.org/10.1017/S1471068421000582
[36] ReubenBinns,MaxVanKleek,MichaelVeale,UlrikLyngs,JunZhao,andNigelShadbolt.2018.’It’sreducingahuman
beingtoapercentage’:Perceptionsofjusticeinalgorithmicdecisions.InProceedingsofCHI2018.ACM,NewYork,
14.https://doi.org/10.1145/3173574.3173951
[37] EmilyBlack,ZifanWang,andMattFredrikson.2022.Consistentcounterfactualsfordeepmodels.InProceedingsof
theInternationalConferenceonLearningRepresentations.https://arxiv.org/abs/2110.03109
[38] JockBlackard.1998.Covertype.UCIMachineLearningRepository.https://doi.org/10.24432/C50K5N
[39] PierreBlanchart.2021.AnExactCounterfactual-example-basedApproachtoTree-ensembleModelsInterpretability.
https://doi.org/10.48550/ARXIV.2105.14820
[40] R.D.BochandM.Lieberman.1970.Fittingaresponsemodelforndichotomouslyscoreditems.Psychometrika35
(1970),179–97.
[41] SebastianBordt,MichèleFinck,EricRaidl,andUlrikevonLuxburg.2022.Post-HocExplanationsFailtoAchieve
theirPurposeinAdversarialContexts.https://arxiv.org/abs/2201.10295
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:28 S.Vermaetal.
[42] ZeydBoukhers,TimoHartmann,andJanJürjens.2022.COIN:CounterfactualImageGenerationforVQAInterpre-
tation.https://doi.org/10.48550/ARXIV.2201.03342
[43] MartimBrandão,GerardCanal,SenkaKrivić,PaulLuff,andAmandaColes.2021.How expertsexplainmotion
planneroutput:Apreliminaryuser-studytoinformthedesignofexplainableplanners.InProceedingsofthe2021
30thIEEEInternationalConferenceonRobot&HumanInteractiveCommunication(RO-MAN’21).299–306.https://
doi.org/10.1109/RO-MAN50785.2021.9515407
[44] KatherineElizabethBrown,DougTalbert,andSteveTalbert.2021.Theuncertaintyofcounterfactualsindeeplearn-
ing.InTheInternationalFLAIRSConferenceProceedings34(2021).https://doi.org/10.32473/flairs.v34i1.128795
[45] KieranBrowneandBenSwift.2020.SemanticsandExplanation:WhyCounterfactualExplanationsProduceAdver-
sarialExamplesinDeepNeuralNetworks.https://doi.org/10.48550/ARXIV.2012.10076
[46] DieterBrughmansandDavidMartens.2021.NICE:AnAlgorithmforNearestInstanceCounterfactualExplanations.
https://doi.org/10.48550/ARXIV.2104.07411
[47] AndreasC.Bueff,MateuszCytryński,RaffaellaCalabrese,MatthewJones,JohnRoberts,JonathonMoore,andIain
Brown.2022.Machinelearninginterpretabilityforastressscenariogenerationincreditscoringbasedoncounter-
factuals.ExpertSystemswithApplications202(2022).https://doi.org/10.1016/j.eswa.2022.117271
[48] NgocBui,DuyNguyen,andVietAnhNguyen.2022.CounterfactualPlansunderDistributionalAmbiguity.https://
doi.org/10.48550/ARXIV.2201.12487
[49] RuthByrne.2008.Therationalimagination:Howpeoplecreatealternativestoreality.TheBehavioralandBrain
Sciences30(2008),439–53;discussion453.https://doi.org/10.1017/S0140525X07002579
[50] RuthM.J.Byrne.2019.Counterfactualsinexplainableartificialintelligence(XAI):Evidencefromhumanreasoning.
InProceedingsofthe28thInternationalJointConferenceonArtificialIntelligence(IJCAI-19).InternationalJointCon-
ferencesonArtificialIntelligenceOrganization,California,USA,6276–6282.https://doi.org/10.24963/ijcai.2019/876
[51] CarrieJ.Cai,JonasJongejan,andJessHolbrook.2019.Theeffectsofexample-basedexplanationsinamachine
learninginterface(IUI’19).ACM,NewYork,258–262.https://doi.org/10.1145/3301275.3302289
[52] MiguelÁ.Carreira-PerpiñánandSuryabhanSinghHada.2021.Counterfactualexplanationsforobliquedecision
trees:Exact,efficientalgorithms.InProceedingsoftheAAAIConferenceonArtificialIntelligence35(May2021),6903–
6911.https://doi.org/10.1609/aaai.v35i8.16851
[53] Emilio Carrizosa, Jasone Ramirez-Ayerbe, and Dolores Romero Morales. 2021. Generating Collective Coun-
terfactual Explanations in Score-Based Classification via Mathematical Optimization. https://doi.org/10.13140/
RG.2.2.22996.12168/1
[54] EmilioCarrizosa,JasoneRamírez-Ayerbe,andDoloresRomeroMorales.2022.CounterfactualExplanationsforFunc-
tionalData:AMathematicalOptimizationApproach.https://doi.org/10.13140/RG.2.2.25682.68801
[55] EmilioCarrizosa,JasoneRamírez-Ayerbe,andDoloresRomeroMorales.2024.Mathematicaloptimizationmodelling
for group counterfactual explanations. European Journal of Operational Research (2024). https://doi.org/10.1016/
j.ejor.2024.01.002
[56] DiogoV.Carvalho,EduardoM.Pereira,andJaimeS.Cardoso.2019.Machinelearninginterpretability:Asurveyon
methodsandmetrics.Electronics8(2019),832.https://doi.org/10.3390/electronics8080832
[57] Lenart Celar and Ruth M. J. Byrne. 2023. How people reason with counterfactual and causal explanations for
artificialintelligencedecisionsinfamiliarandunfamiliardomains.Memory&Cognition51,7(2023),1481–1496.
https://doi.org/10.3758/s13421-023-01407-5
[58] CFPB. [n. d.]. Adverse Action Notice Requirements Under the ECOA and the FCRA. https://
consumercomplianceoutlook.org/2013/second-quarter/adverse-action-notice-requirements-under-ecoa-fcra/.
Accessed:2020-10-15.
[59] CFPB. [n. d.]. Notification of Action Taken, ECOA Notice, and Statement of Specific Reasons. https://www.
consumerfinance.gov/policy-compliance/rulemaking/regulations/1002/9/.Accessed:2020-10-15.
[60] QianglongChen,FengJi,XiangjiZeng,Feng-LinLi,JiZhang,HaiqingChen,andYinZhang.2021.KACE:Gen-
eratingknowledgeawarecontrastiveexplanationsfornaturallanguageinference.InProceedingsofthe59thAn-
nualMeetingoftheAssociationforComputationalLinguisticsandthe11thInternationalJointConferenceonNatu-
ralLanguageProcessing.AssociationforComputationalLinguistics,Online,2516–2527.https://doi.org/10.18653/v1/
2021.acl-long.196
[61] TsongYuehChen,Fei-ChingKuo,HuaiLiu,Pak-LokPoon,DaveTowey,T.H.Tse,andZhiQuanZhou.2018.Meta-
morphictesting:Areviewofchallengesandopportunities.ACMComput.Surv.51,1(2018),27.https://doi.org/
10.1145/3143561
[62] Yatong Chen, Jialu Wang, and Yang Liu. 2020. Strategic Recourse in Linear Classification. https:
//dynamicdecisions.github.io
[63] ZihengChen,FabrizioSilvestri,JiaWang,HeZhu,HongshikAhn,andGabrieleTolomei.2021.ReLAX:Reinforce-
mentLearningAgenteXplainerforArbitraryPredictiveModels.https://doi.org/10.48550/ARXIV.2110.11960
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:29
[64] FuruiCheng,YaoMing,andHuaminQu.2020.DECE:DecisionExplorerwithCounterfactualExplanationsforMa-
chineLearningModels.arXiv:cs.LG/2008.08353
[65] NoelCodella,VeronicaRotemberg,PhilippTschandl,M.EmreCelebi,StephenDusza,DavidGutman,BrianHelba,
AadiKalloo,KonstantinosLiopyris,MichaelMarchetti,HaraldKittler,andAllanHalpern.2019.SkinLesionAnalysis
TowardMelanomaDetection2018:AChallengeHostedbytheInternationalSkinImagingCollaboration(ISIC).https:
//doi.org/10.48550/ARXIV.1902.03368
[66] GregoryCohen,SaeedAfshar,JonathanC.Tapson,andAndrévanSchaik.2017.EMNIST:ExtendingMNISTto
handwrittenletters.InProceedingsofthe2017InternationalJointConferenceonNeuralNetworks(IJCNN) (2017),
2921–2926.https://doi.org/10.1109/IJCNN.2017.7966217
[67] European Commission. [n. d.]. Artificial Intelligence. https://ec.europa.eu/info/funding-tenders/opportunities/
portal/screen/opportunities/topic-details/ict-26-2018-2020.Accessed:2020-10-15.
[68] EuropeanCommission.[n.d.].REGULATION(EU)2016/679OFTHEEUROPEANPARLIAMENTANDOFTHE
COUNCILof27April2016ontheProtectionofNaturalPersonswithRegardtotheProcessingofPersonalData
andontheFreeMovementofSuchData,andRepealingDirective95/46/EC(GeneralDataProtectionRegulation).
https://eur-lex.europa.eu/eli/reg/2016/679/oj.Accessed:2020-10-15.
[69] ZicunCong,LingyangChu,YuYang,andJianPei.2021.ComprehensiblecounterfactualexplanationonKolmogorov-
Smirnovtest.Proc.VLDBEndow.14,9(2021),1583–1596.https://doi.org/10.14778/3461535.3461546
[70] MichaelCorrell.2019.Ethicaldimensionsofvisualizationresearch.InProceedingsof CHI’19.ACM,NewYork„13.
https://doi.org/10.1145/3290605.3300418
[71] PauloCortez.2014.StudentPerformance.UCIMachineLearningRepository.https://doi.org/10.24432/C5TG7T
[72] MarkW.CravenandJudeW.Shavlik.1995.Extractingtree-structuredrepresentationsoftrainednetworks.InPro-
ceedingsofthe8thInternationalConferenceonNeuralInformationProcessingSystems(NIPS’95).MITPress,Cambridge,
MA,USA,24–30.
[73] RiccardoCrupi,BeatrizSanMiguelGonzález,AlessandroCastelnovo,andDanieleRegoli.2022.Leveragingcausal
relationstoprovidecounterfactualexplanationsandfeasiblerecommendationstoendusers.InProceedingsofthe
14thInternationalConferenceonAgentsandArtificialIntelligence-Volume2:ICAART,.SciTePress,24–32.https://
doi.org/10.5220/0010761500003116
[74] XinyueDai,MarkT.Keane,LaurenceShalloo,ElodieRuelle,andRuthM.J.Byrne.2022.Counterfactualexplanations
forpredictionanddiagnosisinXAI.InProceedingsofthe2022AAAI/ACMConferenceonAI,Ethics,andSociety(AIES
’22).ACM,NewYork„12.https://doi.org/10.1145/3514094.3534144
[75] SusanneDandl,ChristophMolnar,MartinBinder,andBerndBischl.2020.Multi-objectivecounterfactualexplana-
tions.InProceedingsofPPSNXVI.SpringerInternationalPublishing,Cham,448–469.https://doi.org/10.1007/978-3-
030-58112-131
[76] DARPA.[n.d.].BroadAgencyAnnouncement:ExplainableArtificialIntelligence(XAI).https://www.darpa.mil/
attachments/DARPA-BAA-16-53.pdf.Accessed:2020-10-15.
[77] SaloniDash,VineethNBalasubramanian,andAmitSharma.2022.Evaluatingandmitigatingbiasinimageclassi-
fiers:Acausalperspectiveusingcounterfactuals.InProceedingsoftheIEEE/CVFWinterConferenceonApplications
ofComputerVision(WACV’22).915–924.https://doi.org/10.1109/WACV51458.2022.00393
[78] A.Datta,S.Sen,andY.Zick.2016.Algorithmictransparencyviaquantitativeinputinfluence:Theoryandexperi-
mentswithlearningsystems.InProceedingsof2016IEEESymposiumonSecurityandPrivacy(SP’16).IEEE,NewYork,
,598–617.https://doi.org/10.1109/SP.2016.42
[79] LucasdeLara,AlbertoGonzález-Sanz,NicholasAsher,andJean-MichelLoubes.2021.Transport-basedCounterfac-
tualModels.https://doi.org/10.48550/ARXIV.2108.13025
[80] GiovanniDeToni,BrunoLepri,andAndreaPasserini.2022.SynthesizingExplainableCounterfactualPoliciesfor
AlgorithmicRecoursewithProgramSynthesis.https://doi.org/10.48550/ARXIV.2201.07135
[81] Sarah Dean, Sarah Rich, and Benjamin Recht. 2020. Recommendations and user agency: The reachability of
collaboratively-filteredinformation.InProceedingsof FAT*’20.ACM,NewYork,10.https://doi.org/10.1145/3351095.
3372866
[82] EoinDelaney,DerekGreene,andMarkT.Keane.2021.Instance-basedcounterfactualexplanationsfortimeseries
classification.InProceedingsofthe29thInternationalConferenceonCase-BasedReasoningResearchandDevelopment
(ICCBR2021),(Salamanca,Spain,September13–16,2021).,.Springer-Verlag,Berlin,,32–47.https://doi.org/10.1007/
978-3-030-86957-13
[83] EoinDelaney,DerekGreene,andMarkT.Keane.2021.UncertaintyEstimationandOut-of-DistributionDetection
forCounterfactualExplanations:PitfallsandSolutions.https://arxiv.org/abs/2107.09734
[84] EoinDelaney,ArjunPakrashi,DerekGreene,andMarkT.Keane.2023.Counterfactualexplanationsformisclassi-
fiedimages:Howhumanandmachineexplanationsdiffer.ArtificialIntelligence324(2023),103995.https://doi.org/
10.1016/j.artint.2023.103995
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:30 S.Vermaetal.
[85] HoutaoDeng.2014.InterpretingtreeensembleswithinTrees.arXiv:1408.5456 (082014).https://doi.org/10.1007/
s41060-018-0144-8
[86] JiaDeng,WeiDong,RichardSocher,Li-JiaLi,KaiLi,andLiFei-Fei.2009.ImageNet:Alarge-scalehierarchical
imagedatabase.InProceedingsofthe2009IEEEConferenceonComputerVisionandPatternRecognition.248–255.
https://doi.org/10.1109/CVPR.2009.5206848
[87] AmitDhurandhar,Pin-YuChen,RonnyLuss,Chun-ChenTu,PaishunTing,KarthikeyanShanmugam,andPayelDas.
2018.Explanationsbasedonthemissing:Towardscontrastiveexplanationswithpertinentnegatives.InProceedings
oftheNeurIPS2018.CurranAssociatesInc.,590–601.
[88] AmitDhurandhar,TejaswiniPedapati,AvinashBalakrishnan,Pin-YuChen,KarthikeyanShanmugam,andRuchir
Puri.2019.ModelAgnosticContrastiveExplanationsforStructuredData.http://arxiv.org/abs/1906.00117
[89] EdsgerWDijkstra.1959.Anoteontwoproblemsinconnexionwithgraphs.NumerischeMathematik1,1(1959),
269–271.
[90] JonathanDodge,Q.VeraLiao,YunfengZhang,RachelK.E.Bellamy,andCaseyDugan.2019.Explainingmodels:
Anempiricalstudyofhowexplanationsimpactfairnessjudgment.InProceedingsofIUI2019.ACM,NewYork,11.
https://doi.org/10.1145/3301275.3302310
[91] CarlDoersch.2016.TutorialonVariationalAutoencoders.arXiv:stat.ML/1606.05908
[92] PedroDomingos.1998.Knowledgediscoveryviamultiplemodels.Intell.DataAnal.2,3(May1998),187–202.
[93] RicardoDominguez-Olmedo,AmirH.Karimi,andBernhardSchölkopf.2022.Ontheadversarialrobustnessofcausal
algorithmicrecourse.InProceedingsofthe39thInternationalConferenceonMachineLearning.PMLR,5324–5342.
https://proceedings.mlr.press/v162/dominguez-olmedo22a.html
[94] FinaleDoshi-Velez,MasonKortz,RyanBudish,ChrisBavitz,SamGershman,D.O’Brien,StuartSchieber,J.Waldo,
D.Weinberger,andAlexandraWood.2017.AccountabilityofAIUndertheLaw:TheRoleofExplanation.https://
doi.org/10.2139/ssrn.3064761
[95] MichaelDowns,JonathanChu,YanivYacoby,FinaleDoshi-Velez,andWeiwei.Pan.2020.CRUDS:Counterfactual
recourseusingdisentangledsubspaces.InProceedingsoftheWorkshoponHumanInterpretabilityinMachineLearn-
ing (WHI’20). https://finale.seas.harvard.edu/files/finale/files/cruds-_counterfactual_recourse_using_disentangled_
subspaces.pdf
[96] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-AdultIncome.http://archive.ics.uci.edu/
ml/datasets/Adult
[97] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-BreastCancer.https://archive.ics.uci.edu/
ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
[98] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-Iris.https://archive.ics.uci.edu/ml/datasets/
iris
[99] DheeruDuaandCaseyGraff.2017.UCIMachineLearningRepository-Shopping.https://archive.ics.uci.edu/ml/
datasets/Online+Shoppers+Purchasing+Intention+Dataset
[100] Dheeru Dua and Casey Graff. 2017. UCI Machine Learning Repository - Wine. https://archive.ics.uci.edu/ml/
datasets/wine
[101] JannikDunkelauandMichaelLeuschel.2019.Fairness-AwareMachineLearning.60pages.https://www.phil-fak.uni-
duesseldorf.de/fileadmin/Redaktion/Institute/Sozialwissenschaften/Kommunikations-_und_Medienwissenschaft/
KMW_I/Working_Paper/Dunkelau___Leuschel__2019__Fairness-Aware_Machine_Learning.pdf
[102] TriDungDuong,QianLi,andGuandongXu.2021.Prototype-basedCounterfactualExplanationforCausalClassifi-
cation.https://doi.org/10.48550/ARXIV.2105.00703
[103] SanghamitraDutta,JasonLong,SaumitraMishra,CeciliaTilli,andDanieleMagazzeni.2022.Robustcounterfactual
explanationsfortree-basedensembles.InProceedingsofthe39thInternationalConferenceonMachineLearning.PMLR,
5742–5756.https://proceedings.mlr.press/v162/dutta22a.html
[104] Andrew Elliott, Stephen Law, and Chris Russell. 2021. Explaining classifiers using adversarial perturbations on
theperceptualball.InProceedingsoftheConferenceonComputerVisionandPatternRecognition(CVPR’21).https://
doi.org/10.48550/ARXIV.1912.09405
[105] LukasFaber,AminK.Moghaddam,andRogerWattenhofer.2020.ContrastiveGraphNeuralNetworkExplanation.
https://doi.org/10.48550/ARXIV.2010.13663
[106] DanielFaggella.2020.MachineLearningforMedicalDiagnostics–4CurrentApplications.https://emerj.com/ai-
sector-overviews/machine-learning-medical-diagnostics-4-current-applications/.Accessed:2020-10-15.
[107] JakeFawkes,RobinEvans,andDinoSejdinovic.2022.Selection,IgnorabilityandChallengeswithCausalFairness.
https://doi.org/10.48550/ARXIV.2202.13774
[108] J.A.Fdez-Sánchez,J.D.Pascual-Triana,A.Fernández,andF.Herrera.2021.Learninginterpretablemulti-classmod-
elsbymeansofhierarchicaldecomposition:Thresholdcontrolfornesteddichotomies.Neurocomputing463(2021),
514–524.https://doi.org/10.1016/j.neucom.2021.07.097
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:31
[109] AmirH.Feghahati,ChristianR.Shelton,MichaelJ.Pazzani,andKevinTang.2020.CDeepEx:Contrastivedeep
explanations.InProceedingsofECAI.
[110] Rubén R. Fernández, Isaac Martín de Diego, Víctor Aceña, Alberto Fernández-Isabel, and Javier M. Moguerza.
2020.Randomforestexplainabilityusingcounterfactualsets.InformationFusion63(2020),196–207.https://doi.org/
10.1016/j.inffus.2020.07.001
[111] CarlosFernández-Loría,FosterProvost,andXintianHan.2020.ExplainingData-DrivenDecisionsmadebyAISys-
tems:TheCounterfactualApproach.http://arxiv.org/abs/2001.07417
[112] AndreaFerrarioandMicheleLoi.2020.ASeriesofUnfortunateCounterfactualEvents:theRoleofTimeinCounter-
factualExplanations.https://doi.org/10.48550/ARXIV.2010.04687
[113] FICO.2018.FICO(HELOC)Dataset.https://community.fico.com/s/explainable-machine-learning-challenge?tabset-
3158a=2
[114] GiorgosFilandrianos,KonstantinosThomas,EdmundDervakos,andGiorgosStamou.2022.Conceptualeditsas
counterfactualexplanations(CEURWorkshopProceedings).CEUR-WS.org.http://ceur-ws.org/Vol-3121/paper6.pdf
[115] MaximilianFörster,PhilippHühn,MathiasKlier,andKilianKluge.2021.Capturingusers’reality:Anovelapproach
togeneratecoherentcounterfactualexplanations.https://doi.org/10.24251/HICSS.2021.155
[116] MaximilianFörster,MathiasKlier,KilianKluge,andIrinaSigler.2020.EvaluatingexplainableArtificalintelligence–
Whatusersreallyappreciate.(2020).https://aisel.aisnet.org/ecis2020rp/195
[117] MaximilianBecker,NadiaBurkart,PascalBirnstill,andJürgenBeyerer.2021.Asteptowardsglobalcounterfactual
explanations:Approximatingthefeaturespacethroughhierarchicaldivisionandgraphsearch.Adv.Artif.Intell.
Mach.Learn.1,2(2021),90–110.
[118] Timo Freiesleben. 2022. The intriguing relation between counterfactual explanations and adversarial examples.
MindsMach.(Dordr.)(2022),77–109.
[119] JeromeH.Friedman.2001.Greedyfunctionapproximation:Agradientboostingmachine.TheAnnalsofStatistics29,
5(2001),1189–1232.http://www.jstor.org/stable/2699986
[120] JörgFrohbergandFrankBinder.2022.CRASS:Anoveldatasetandbenchmarktotestcounterfactualreasoning
oflargelanguagemodels.InProceedingsoftheLanguageResourcesandEvaluationConference.EuropeanLanguage
ResourcesAssociation,Marseille,France,2126–2140.https://aclanthology.org/2022.lrec-1.229
[121] TakanoriFujiwara,XinhaiWei,JianZhao,andKwan-LiuMa.2022.Interactivedimensionalityreductionforcompar-
ativeanalysis.IEEETransactionsonVisualizationandComputerGraphics(2022),758–768.https://doi.org/10.1109/
tvcg.2021.3114807
[122] MaximilianFörster,PhilippHühn,MathiasKlier,andKilianKluge.2021.Capturingusers’reality:Anovelapproach
togeneratecoherentcounterfactualexplanations.https://doi.org/10.24251/HICSS.2021.155
[123] SainyamGalhotra,RomilaPradhan,andBabakSalimi.2021.Explainingblack-boxalgorithmsusingprobabilistic
contrastivecounterfactuals.In:ProceedingsoftheInternationalConferenceonManagementofData(SIGMOD’21),
(VirtualEvent,China,June20–25,2021.)ACM.https://doi.org/10.1145/3448016.3458455
[124] JingweiGan,ShinanZhang,ChiZhang,andAndyLi.2021.Automatedcounterfactualgenerationinfinancialmodel
riskmanagement.InProceedingsofthe2021IEEEInternationalConferenceonBigData(BigData).4064–4068.https://
doi.org/10.1109/BigData52589.2021.9671561
[125] P.J.García-Laencina,J.Sancho-Gómez,andA.R.Figueiras-Vidal.2009.Patternclassificationwithmissingdata:A
review.NeuralComputingandApplications19(2009),263–282.
[126] Gordon Garisch. [n. d.]. Model Lifecycle Transformation: How Banks Are Unlocking Efficiencies. https:
//financialservicesblog.accenture.com/model-lifecycle-transformation-how-banks-are-unlocking-efficiencies. Ac-
cessed:2022-10-15.
[127] YingqiangGe,ShuchangLiu,ZelongLi,ShuyuanXu,ShijieGeng,YunqiLi,JuntaoTan,FeiSun,andYongfengZhang.
2021.CounterfactualEvaluationforExplainableAI.https://doi.org/10.48550/ARXIV.2109.01962
[128] AsmaGhandeharioun,BeenKim,Chun-LiangLi,BrendanJou,BrianEoff,andRosalindPicard.2022.DISSECT:
Disentangledsimultaneousexplanationsviaconcepttraversals.InProceedingsoftheInternationalConferenceon
LearningRepresentations.https://openreview.net/forum?id=qY79G8jGsep
[129] AzinGhazimatin,OanaBalalau,RishirajSahaRoy,andGerhardWeikum.2020.PRINCE:Provider-sideinterpretabil-
ity with counterfactual explanations in recommender systems (WSDM ’20). ACM, NewYork, 9. https://doi.org/
10.1145/3336191.3371824
[130] GiorgosGiannopoulos,GeorgePapastefanatos,DimitrisSacharidis,andKostasStefanidis.2021.Interactivity,Fairness
andExplanationsinRecommendations.ACM.NewYork.https://doi.org/10.1145/3450614.3462238
[131] AlexGoldstein,AdamKapelner,JustinBleich,andEmilPitkin.2013.Peekinginsidetheblackbox:Visualizingsta-
tisticallearningwithplotsofindividualconditionalexpectation.JournalofComputationalandGraphicalStatistics
24(092013).https://doi.org/10.1080/10618600.2014.907095
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:32 S.Vermaetal.
[132] OscarGomez,SteffenHolter,JunYuan,andEnricoBertini.2020.ViCE:Visualcounterfactualexplanationsforma-
chinelearningmodels.InProceedingsof IUI’20.5.https://doi.org/10.1145/3377325.3377536
[133] OscarGomez,SteffenHolter,JunYuan,andEnricoBertini.2021.AdViCE:AggregatedVisualCounterfactualExpla-
nationsforMachineLearningModelValidation.https://doi.org/10.48550/ARXIV.2109.05629
[134] BryceGoodmanandS.Flaxman.2016.EUregulationsonalgorithmicdecision-makinganda“RighttoExplanation”.
ArXivabs/1606.08813(2016).
[135] YashGoyal,ZiyanWu,JanErnst,DhruvBatra,DeviParikh,andStefanLee.2019.Counterfactualvisualexplanations.
InProceedingsofICML2019.PMLR,2376–2384.https://proceedings.mlr.press/v97/goyal19a.html
[136] PrestonGralla.2016.AmazonPrimeandtheRacistAlgorithms.https://www.computerworld.com/article/3068622/
amazon-prime-and-the-racist-algorithms.html
[137] RoryMcGrath,LucaCostabello,ChanLeVan,PaulSweeney,FarbodKamiab,ZhaoShen,andFreddyLecue.2018.
InterpretableCreditApplicationPredictionswithCounterfactualExplanations.http://arxiv.org/abs/1811.05245
[138] HomeCreditGroup.2018.HomeCreditDefaultRisk.https://www.kaggle.com/c/home-credit-default-risk/data
[139] RiccardoGuidotti,AnnaMonreale,SalvatoreRuggieri,DinoPedreschi,FrancoTurini,andFoscaGiannotti.2018.
LocalRule-BasedExplanationsofBlackBoxDecisionSystems.http://arxiv.org/abs/1805.10820
[140] RiccardoGuidotti,AnnaMonreale,SalvatoreRuggieri,FrancoTurini,FoscaGiannotti,andDinoPedreschi.2018.
Asurveyofmethodsforexplainingblackboxmodels.ACMComput.Surv.51,5,Article93(Aug.2018),42pages.
https://doi.org/10.1145/3236009
[141] RiccardoGuidottiandSalvatoreRuggieri.2021.Ensembleofcounterfactualexplainers.Springer-Verlag,Berlin, 11.
https://doi.org/10.1007/978-3-030-88942-528
[142] SadafGulshadandArnoldSmeulders.2021.Counterfactualattribute-basedvisualexplanationsforclassification.
InternationalJournalofMultimediaInformationRetrieval(2021),127–140.https://doi.org/10.1007/s13735-021-00208-
3
[143] HangzhiGuo,ThanhHongNguyen,andAmulyaYadav.2021.CounterNet:End-to-EndTrainingofCounterfactual
AwarePredictions.https://doi.org/10.48550/ARXIV.2109.07557
[144] SharmiDevGupta,BegumGenc,andBarryO’Sullivan.2022.FindingCounterfactualExplanationsthroughCon-
straintRelaxations.https://doi.org/10.48550/ARXIV.2204.03429
[145] VivekGupta,PegahNokhiz,ChitradeepDuttaRoy,andSureshVenkatasubramanian.2019.EqualizingRecourse
AcrossGroups.https://arxiv.org/abs/1909.03166
[146] VictorGuyomard,FrançoiseFessant,TassaditBouadi,andThomasGuyet.2021.Post-hoccounterfactualgeneration
withsupervisedautoencoder.https://doi.org/10.1007/978-3-030-93736-210
[147] SuryabhanSinghHadaandMiguelÁ.Carreira-Perpiñán.2021.Exploringcounterfactualexplanationsforclassifi-
cationandregressiontrees.InMachineLearningandPrinciplesandPracticeofKnowledgeDiscoveryinDatabases.
SpringerInternationalPublishing,Cham,489–504.https://doi.org/10.1007/978-3-030-93736-237
[148] SwastikHaldar,PhilipsGeorgeJohn,andDiptikalyanSaha.2021.Reliablecounterfactualexplanationsforautoen-
coder based anomalies. In Proceedings of the 8th ACM IKDD CODS and 26th COMAD. ACM. New York, 83–91.
https://doi.org/10.1145/3430984.3431015
[149] Xing Han and Joydeep Ghosh. 2021. Model-agnostic explanations using minimal forcing subsets. In Proceed-
ings of the 2021 International Joint Conference on Neural Networks (IJCNN’21). 1–8. https://doi.org/10.1109/
IJCNN52387.2021.9533992
[150] MasoudHashemiandAliFathi.2020.PermuteAttack:CounterfactualExplanationofMachineLearningCreditScore-
cards.https://doi.org/10.48550/ARXIV.2008.10138
[151] LisaAnneHendricks,RonghangHu,TrevorDarrell,andZeynepAkata.2018.GeneratingCounterfactualExplana-
tionswithNaturalLanguage.https://doi.org/10.48550/ARXIV.1806.09809
[152] AndreasHenelius,KaiPuolamäki,HenrikBoström,LarsAsker,andPanagiotisPapapetrou.2014.Apeekintothe
blackbox:Exploringclassifiersbyrandomization.DataMin.Knowl.Discov.28,5-6(2014),27.https://doi.org/10.1007/
s10618-014-0368-8
[153] FabianHinderandBarbaraHammer.2020.CounterfactualExplanationsofConceptDrift.https://doi.org/10.48550/
ARXIV.2006.12822
[154] HansHofmann.1994.Statlog(GermanCreditData).UCIMachineLearningRepository.https://doi.org/10.24432/
C5NC77
[155] FredHohman,AndrewHead,RichCaruana,RobertDeLine,andStevenMarkDrucker.2019.Gamut:Adesignprobe
tounderstandhowdatascientistsunderstandmachinelearningmodels.InProceedingsofthe2019CHIConference
onHumanFactorsinComputingSystems(2019).
[156] WooSukHong,AdrianDanielHaimovich,andR.AndrewTaylor.2018.Predictinghospitaladmissionatemergency
departmenttriageusingmachinelearning.PlosOne13,7(2018).https://doi.org/10.1371/journal.pone.0201016
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:33
[157] ReeberErikFormanGeorgeHopkins,MarkandJaapSuermondt.1999.Spambase.UCIMachineLearningRepository.
https://doi.org/10.24432/C53G6X
[158] TheUSWhiteHouse.2022.BlueprintforanAIBillofRights.https://www.whitehouse.gov/ostp/ai-bill-of-rights/
#discrimination
[159] ChihchengHsieh,CatarinaMoreira,andChunOuyang.2021.DiCE4EL:Interpretingprocesspredictionsusinga
milestone-awarecounterfactualapproach.InProceedingsofthe20213rdInternationalConferenceonProcessMining
(ICPM’21).88–95.https://doi.org/10.1109/ICPM53251.2021.9576881
[160] Tsung-HaoHuang,AndreasMetzger,andKlausPohl.2022.Counterfactualexplanationsforpredictivebusinesspro-
cessmonitoring.SpringerInternationalPublishing,Cham,399–413.https://doi.org/10.1007/978-3-030-95947-028
[161] FrederikHvilshøj,AlexandrosIosifidis,andIraAssent.2021.ECINN:EfficientCounterfactualsfromInvertibleNeural
Networks.https://doi.org/10.48550/ARXIV.2103.13701
[162] FrederikHvilshøj,AlexandrosIosifidis,andIraAssent.2021.OnQuantitativeEvaluationsofCounterfactuals.https:
//doi.org/10.48550/ARXIV.2111.00177
[163] BenediktHöltgen,LisaSchut,JanM.Brauner,andYarinGal.2021.DeDUCE:GeneratingCounterfactualExplanations
Efficiently.https://doi.org/10.48550/ARXIV.2111.15639
[164] GlobalWomeninDataScienceConferenceTheGlobalOpenSourceSeverityofIllnessScoreConsortium.2020.WiDS
Datathon2020.https://www.kaggle.com/c/widsdatathon2020
[165] AllstateInsurance.2011.AllstateClaimPredictionChallenge.https://www.kaggle.com/c/ClaimPredictionChallenge
[166] FranceIntelligenceArtificielle.[n.d.].RapportdeSyntheseFranceIntelligenceArtificielle.https://www.economie.
gouv.fr/files/files/PDF/2017/Rapport_synthese_France_IA_.pdf.Accessed:2020-10-15.
[167] JeremyIrvin,PranavRajpurkar,MichaelKo,YifanYu,SilvianaCiurea-Ilcus,ChrisChute,HenrikMarklund,Behzad
Haghgoo,RobynBall,KatieShpanskaya,JayneSeekins,DavidA.Mong,SafwanS.Halabi,JesseK.Sandberg,Ricky
Jones,DavidB.Larson,CurtisP.Langlotz,BhavikN.Patel,MatthewP.Lungren,andAndrewY.Ng.2019.CheX-
pert:ALargeChestRadiographDatasetwithUncertaintyLabelsandExpertComparison.https://doi.org/10.48550/
ARXIV.1901.07031
[168] PaulJacob,ÉloiZablocki,HédiBen-Younes,MickaëlChen,PatrickPérez,andMatthieuCord.[n.d.].STEEX:Steering
CounterfactualExplanationswithSemantics.https://doi.org/10.48550/ARXIV.2111.09094
[169] GuillaumeJeanneret,LoïcSimon,andFrédéricJurie.2022.DiffusionModelsforCounterfactualExplanations.https://
doi.org/10.48550/ARXIV.2203.15636
[170] Lauren Kirchner Jeff Larson, Surya Mattu and Julia Angwin. 2016. UCI Machine Learning Repository. https://
github.com/propublica/compas-analysis/
[171] YanJia,JohnMcDermid,andIbrahimHabli.2021.Enhancingthevalueofcounterfactualexplanationsfordeep
learning.InArtificialIntelligenceinMedicine.SpringerInternationalPublishing,Cham,389–394.https://doi.org/
10.1007/978-3-030-77211-646
[172] AlistairJohnson,LucasBulgarelli,TomPollard,StevenHorng,LeoAnthonyCeli,andRogerMark.2021.MIMIC-IV.
https://doi.org/10.13026/S6N6-XD98
[173] Kareem L. Jordan and Tina L. Freiburger. 2015. The effect of race/ethnicity on sentencing: Examining sentence
type,jaillength,andprisonlength.JournalofEthnicityinCriminalJustice 13,3(2015).https://doi.org/10.1080/
15377938.2014.984045
[174] ShalmaliJoshi,OluwasanmiKoyejo,WarutVijitbenjaronk,BeenKim,andJoydeepGhosh.2019.TowardsRealis-
ticIndividualRecourseandActionableExplanationsinBlack-BoxDecisionMakingSystems.http://arxiv.org/abs/
1907.09615
[175] Hong-GyuJung,Sin-HanKang,Hee-DongKim,Dong-OkWon,andSeong-WhanLee.2020.CounterfactualExpla-
nationBasedonGradualConstructionforDeepNetworks.https://doi.org/10.48550/ARXIV.2008.01897
[176] VassilisKaffes,DimitrisSacharidis,andGiorgosGiannopoulos.2021.Model-agnosticcounterfactualexplanationsof
recommendations(UMAP’21).ACM.NewYork,6.https://doi.org/10.1145/3450613.3456846
[177] Kaggle.2012.GiveMeSomeCredit.https://www.kaggle.com/c/GiveMeSomeCredit
[178] D.KahnemanandD.Miller.1986.Normtheory:Comparingrealitytoitsalternatives.PsychologicalReview93(1986),
136–153.
[179] KentaroKanamori,TakuyaTakagi,KenKobayashi,andHirokiArimura.2020.DACE:Distribution-awarecounterfac-
tualexplanationbymixed-integerlinearoptimization.InProceedingsoftheInternationalJointConferenceonArtificial
Intelligence(IJCAI’20).https://doi.org/10.24963/ijcai.2020/395
[180] KentaroKanamori,TakuyaTakagi,KenKobayashi,andYuichiIke.2022.Counterfactualexplanationtrees:Trans-
parentandconsistentactionablerecoursewithdecisiontree.InProceedingsofMachineLearningResearch(PMLR),
1846–1870.
[181] KentaroKanamori,TakuyaTakagi,KenKobayashi,YuichiIke,KentoUemura,andHirokiArimura.2021.Ordered
counterfactualexplanationbymixed-integerlinearoptimization.InProceedingsoftheAAAIConferenceonArtificial
Intelligence(2021),11.https://doi.org/10.1609/aaai.v35i13.17376
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:34 S.Vermaetal.
[182] A.-H.Karimi,G.Barthe,B.Balle,andI.Valera.2020.Model-AgnosticCounterfactualExplanationsforConsequential
Decisions.http://arxiv.org/abs/1905.11190
[183] Amir-HosseinKarimi,BernhardSchölkopf,andIsabelValera.2021.Algorithmicrecourse:Fromcounterfactualexpla-
nationstointerventions.InProceedingsofFAccT’21.ACM,NewYork,10.https://doi.org/10.1145/3442188.3445899
[184] Amir-HosseinKarimi,JuliusvonKügelgen,BernhardSchölkopf,andIsabelValera.2020.AlgorithmicRecourseunder
ImperfectCausalKnowledge:AProbabilisticApproach.http://arxiv.org/abs/2006.06831
[185] IsakKarlsson,JonathanRebane,PanagiotisPapapetrou,andAristidesGionis.2020.Locallyandgloballyexplainable
timeseriestweaking.Knowl.Inf.Syst.(2020),30.https://doi.org/10.1007/s10115-019-01389-4
[186] AtoosaKasirzadehandAndrewSmart.2021.Theuseandmisuseofcounterfactualsinethicalmachinelearning.In
Proceedingsofthe2021ACMConferenceonFairness,Accountability,andTransparency.ACM,NewYork,9.https://
doi.org/10.1145/3442188.3445886
[187] MarkT.Keane,EoinM.Kenny,EoinDelaney,andBarrySmyth.2021.Ifonlywehadbettercounterfactualexpla-
nations:FivekeydeficitstorectifyintheevaluationofcounterfactualXAItechniques.CoRR(2021).https://arxiv.
org/abs/2103.01035
[188] MarkT.KeaneandBarrySmyth.2020.GoodCounterfactualsandWheretoFindThem:ACase-BasedTechniquefor
GeneratingCounterfactualsforExplainableAI(XAI).arXiv:cs.AI/2005.13997
[189] EoinKennyandWeipengHuang.2023.Theutilityof“Evenif”semifactualexplanationtooptimisepositiveoutcomes.
InAdvancesinNeuralInformationProcessingSystems,A.Oh,T.Naumann,A.Globerson,K.Saenko,M.Hardt,and
S.Levine(Eds.),Vol.36.CurranAssociates,Inc.,52907–52935.https://proceedings.neurips.cc/paperfiles/paper/2023/
file/a5e146ca55a2b18be41942cfa677123d-Paper-Conference.pdf
[190] EoinM.KennyandMarkT.Keane.2020.OnGeneratingPlausibleCounterfactualandSemi-FactualExplanationsfor
DeepLearning.arXiv:2009.06399
[191] EoinM.KennyandMarkTKeane.2021.Ongeneratingplausiblecounterfactualandsemi-factualexplanationsfor
deeplearning.InProceedingsoftheAAAIConferenceonArtificialIntelligence35(May2021),11.https://ojs.aaai.org/
index.php/AAAI/article/view/17377
[192] SaeedKhorramandLiFuxin.2022.Cycle-consistentcounterfactualsbylatenttransformations.InProceedingsofthe
IEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR’22).10.
[193] BeenKim,RajivKhanna,andOluwasanmiO.Koyejo.2016.Examplesarenotenough,learntocriticize!criticismfor
interpretability.InAdvancesinNeuralInformationProcessingSystems,D.Lee,M.Sugiyama,U.Luxburg,I.Guyon,
and R. Garnett (Eds.), Vol. 29. Curran Associates, Inc. https://proceedings.neurips.cc/paperfiles/paper/2016/file/
5680522b8e2bb01943234bce7bf84534-Paper.pdf
[194] BorisKment.2006.Counterfactualsandexplanation.Mind115(2006).https://doi.org/10.1093/mind/fzl261
[195] WillKnight.2019.TheAppleCardDidn’t’See’Gender-andThat’stheProblem.https://www.wired.com/story/the-
apple-card-didnt-see-genderand-thats-the-problem/
[196] RamaravindKommiyaMothilal,DivyatMahajan,ChenhaoTan,andAmitSharma.2021.TowardsUnifyingFeature
AttributionandCounterfactualExplanations:DifferentMeanstotheSameEnd.ACM,NewYork.
[197] JaehoonKoo,DiegoKlabjan,andJeanUtke.2020.InverseClassificationwithLimitedBudgetandMaximumNumber
ofPerturbedSamples.https://doi.org/10.48550/ARXIV.2009.14111
[198] TaraKoopmanandSiljaRenooij.2021.PersuasivecontrastiveexplanationsforBayesiannetworks.InSymbolicand
QuantitativeApproachestoReasoningwithUncertainty.SpringerInternationalPublishing,Cham,229–242.https://
doi.org/10.1007/978-3-030-86772-0_17
[199] AntonKorikovandJ.ChristopherBeck.2021.Counterfactualexplanationsviainverseconstraintprogramming.In
Proceedingsofthe27thInternationalConferenceonPrinciplesandPracticeofConstraintProgramming(CP’21),Vol.210.
SchlossDagstuhl–Leibniz-ZentrumfürInformatik.https://doi.org/10.4230/LIPIcs.CP.2021.35
[200] AntonKorikov,AlexanderShleyfman,andJ.ChristopherBeck.2021.Counterfactualexplanationsforoptimization-
based decisions in the context of the GDPR. In Proceedings of IJCAI-21. 4097–4103. https://doi.org/10.24963/
ijcai.2021/564
[201] MaximKovalev,LevUtkin,FrankCoolen,andAndreiKonstantinov.2021.Counterfactualexplanationofmachine
learningsurvivalmodels.Informatica(2021),817–847.https://doi.org/10.15388/21-INFOR468
[202] R.Krishnan,G.Sivakumar,andP.Bhattacharya.1999.Extractingdecisiontreesfromtrainedneuralnetworks.Pattern
Recognition32,12(1999),1999–2009.https://doi.org/10.1016/S0031-3203(98)00181-2
[203] SanjayKrishnanandEugeneWu.2017.PALM:Machinelearningexplanationsforiterativedebugging.InProceedings
of HILDA’17.ACM.NewYork,6.https://doi.org/10.1145/3077257.3077271
[204] UlrikeKuhl,AndréArtelt,andBarbaraHammer.2022.Keepyourfriendscloseandyourcounterfactualscloser:
Improved learning from closest rather than plausible counterfactual explanations in an abstract setting. ArXiv
abs/2205.05515(2022).
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:35
[205] MattJ.Kusner,JoshuaLoftus,ChrisRussell,andRicardoSilva.2017.Counterfactualfairness.AdvancesinNeural
InformationProcessingSystems30(2017).
[206] GunnarKönig,TimoFreiesleben,andMoritzGrosse-Wentrup.2021.ACausalPerspectiveonMeaningfulandRobust
AlgorithmicRecourse.https://doi.org/10.48550/ARXIV.2107.07853
[207] JokinLabaien,EkhiZugasti,andXabierDeCarlos.2021.DA-DGCEx:EnsuringValidityofDeepGuidedCounterfac-
tualExplanationswithDistribution-AwareAutoencoderLoss.https://doi.org/10.48550/ARXIV.2104.09062
[208] MichaelT.Lash,QihangLin,WilliamNickStreet,JenniferG.Robinson,andJeffreyW.Ohlmann.2017.General-
izedinverseclassification.InProceedingsofSDM.SocietyforIndustrialandAppliedMathematics,Philadelphia,PA,
162–170.https://doi.org/10.1137/1.9781611974973.19
[209] ThibaultLaugel,Marie-JeanneLesot,ChristopheMarsala,andMarcinDetyniecki.2019.IssueswithPost-hocCoun-
terfactualExplanations:ADiscussion.arXiv:1906.04774
[210] ThibaultLaugel,Marie-JeanneLesot,ChristopheMarsala,XavierRenard,andMarcinDetyniecki.2018.Comparison-
basedinverseclassificationforinterpretabilityinmachinelearning.InProceedingsofInformationProcessingand
ManagementofUncertaintyinKnowledge-BasedSystems,TheoryandFoundations(IPMU’18).SpringerInternational
Publishing.https://doi.org/10.1007/978-3-319-91473-29
[211] ThibaultLaugel,Marie-JeanneLesot,ChristopheMarsala,XavierRenard,andMarcinDetyniecki.2019.TheDangers
ofPost-hocInterpretability:UnjustifiedCounterfactualExplanations.http://arxiv.org/abs/1907.09294
[212] ThaiLe,SuhangWang,andDongwonLee.2019.GRACE:GeneratingConciseandInformativeContrastiveSample
toExplainNeuralNetworkModel’sPrediction.arXiv:cs.LG/1911.02042
[213] Yann LeCun and Corinna Cortes. 2010. MNIST handwritten digit database. (2010). http://yann.lecun.com/exdb/
mnist/
[214] CarsonK.Leung,AdamG.M.Pazdor,andJoglasSouza.2021.Explainableartificialintelligencefordatascienceon
customerchurn.InProceedingsofthe2021IEEE8thInternationalConferenceonDataScienceandAdvancedAnalytics
(DSAA’21).1–10.https://doi.org/10.1109/DSAA53316.2021.9564166
[215] DavidLewis.1973.Counterfactuals.BlackwellPublishers,Oxford.
[216] DanLey,SaumitraMishra,andDanieleMagazzeni.2022.Globalcounterfactualexplanations:Investigations,im-
plementationsandimprovements.InProceedingsoftheICLRWorkshoponPrivacy,Accountability,Interpretability,
Robustness,ReasoningonStructuredData.
[217] Yan Li, Shasha Liu, Chunwei Wu, Xidong Xi, Guitao Cao, and Wenming Cao. 2021. DCFG: Discovering direc-
tionalCounterFactualgenerationforchestX-rays.InProceedingsofBIBM2021.972–979.https://doi.org/10.1109/
BIBM52615.2021.9669770
[218] ShusenLiu,BhavyaKailkhura,DonaldLoveland,andYongHan.2019.Generativecounterfactualintrospectionfor
explainabledeeplearning.InProceedingsofthe2019IEEEGlobalConferenceonSignalandInformationProcessing
(GlobalSIP’19).1–5.https://doi.org/10.1109/GlobalSIP45357.2019.8969491
[219] ZiweiLiu,PingLuo,XiaogangWang,andXiaoouTang.2014.Deeplearningfaceattributesinthewild.(112014).
https://doi.org/10.1109/ICCV.2015.425
[220] AnaLucic,HindaHaned,andMaartendeRijke.2020.Whydoesmymodelfail?Contrastivelocalexplanationsfor
retailforecasting.InProceedingsofthe2020ConferenceonFairness,Accountability,andTransparency.ACM,New
York,9.https://doi.org/10.1145/3351095.3372824
[221] AnaLucic,HarrieOosterhuis,HindaHaned,andMaartendeRijke.2019.FOCUS:FlexibleOptimizableCounterfac-
tualExplanationsforTreeEnsembles.https://doi.org/10.48550/ARXIV.1911.12199
[222] AnaLucic,HarrieOosterhuis,HindaHaned,andMaartendeRijke.2020.ActionableInterpretabilitythroughOpti-
mizableCounterfactualExplanationsforTreeEnsembles.http://arxiv.org/abs/1911.12199
[223] AnaLucic,MaartjeterHoeve,GabrieleTolomei,MaartendeRijke,andFabrizioSilvestri.2021.CF-GNNExplainer:
CounterfactualExplanationsforGraphNeuralNetworks.arXiv:cs.LG/2102.03322
[224] ScottM.LundbergandSu-InLee.2017.Aunifiedapproachtointerpretingmodelpredictions.InAdvancesinNeural
InformationProcessingSystems30.CurranAssociates,Inc.,4765–4774.
[225] FreddieMac.2019.SingleFamilyLoan-levelDataset.https://www.freddiemac.com/research/datasets/sf-loanlevel-
dataset
[226] NishthaMadaan,InkitPadhi,NaveenPanwar,andDiptikalyanSaha.2021.Generateyourcounterfactuals:Towards
controlledcounterfactualgenerationfortext.InProceedingsoftheAAAIConferenceonArtificialIntelligence35(May
2021),13516–13524.https://ojs.aaai.org/index.php/AAAI/article/view/17594
[227] Fannie Mae. 2020. Fannie Mae Dataset. https://www.fanniemae.com/portal/funding-the-market/data/loan-
performance-data.html
[228] AlessandroMagrini,StefanodiBlasi,andFedericoStefanini.2017.AconditionallinearGaussiannetworktoassess
theimpactofseveralagronomicsettingsonthequalityofTuscanSangiovesegrapes.BiometricalLetters54(062017),
25–42.https://doi.org/10.1515/bile-2017-0002
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:36 S.Vermaetal.
[229] DivyatMahajan,ChenhaoTan,andAmitSharma.2020.PreservingCausalConstraintsinCounterfactualExplana-
tionsforMachineLearningClassifiers.http://arxiv.org/abs/1912.03277
[230] GuilhermeF.Marchezini,AnisioM.Lacerda,GiseleL.Pappa,WagnerMeira,Jr.,DeboraMiranda,MarcoA.Romano-
Silva,DanielleS.Costa,andLeandroMalloyDiniz.2022.Counterfactualinferencewithlatentvariableanditsapplica-
tioninmentalhealthcare.DataMin.Knowl.Discov.36(2022),811–840.https://doi.org/10.1007/s10618-021-00818-9
[231] DavidMartensandFosterJ.Provost.2014.Explainingdata-drivendocumentclassifications.MISQ.38(2014),73–99.
https://doi.org/10.25300/MISQ/2014/38.1.04
[232] RaphaelMazzine,SofieGoethals,DieterBrughmans,andDavidMartens.2021.Counterfactualexplanationsforem-
ploymentservices.InProceedingsoftheInternationalWorkshoponFair,EffectiveandSustainableTalentManagement
usingDataScience.1–7.
[233] RaphaelMazzineandDavidMartens.2021.AFrameworkandBenchmarkingStudyforCounterfactualGenerating
MethodsonTabularData.https://doi.org/10.48550/ARXIV.2107.04680
[234] MarcosMedeirosRaimundo,LuisNonato,andJorgePoco.2021.MiningPareto-OptimalCounterfactualAntecedents
withaBranch-And-BoundModel-AgnosticAlgorithm.https://doi.org/10.21203/rs.3.rs-551661/v1
[235] Md. Golam Moula Mehedi Hasan and Douglas Talbert. 2022. Data augmentation using counterfactuals: Prox-
imity vs. diversity. In The International FLAIRS Conference Proceedings 35 (May 2022). https://doi.org/10.32473/
flairs.v35i.130705
[236] Md.GolamMoulaMehediHasanandDouglasTalbert.2022.MitigatingtheRashomoneffectincounterfactualex-
planation:Agame-theoreticapproach.InTheInternationalFLAIRSConferenceProceedings35(2022).https://doi.org/
10.32473/flairs.v35i.130711
[237] Silvan Mertes, Tobias Huber, Katharina Weitz, Alexander Heimerl, and Elisabeth André. 2022. GANterfactual–
counterfactualexplanationsformedicalnon-expertsusinggenerativeadversariallearning.FrontiersinArtificial
Intelligence5(2022).https://doi.org/10.3389/frai.2022.825565
[238] TimMiller.2019.Explanationinartificialintelligence:Insightsfromthesocialsciences.ArtificialIntelligence(2019),
1–38.https://doi.org/10.1016/j.artint.2018.07.007
[239] SaumitraMishra,SanghamitraDutta,JasonLong,andDanieleMagazzeni.2021.ASurveyontheRobustnessof
FeatureImportanceandCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2111.00358
[240] TakayukiMiura,SatoshiHasegawa,andToshikiShibahara.2021.MEGEX:Data-freemodelextractionattackagainst
gradient-basedexplainableAI.ArXivabs/2107.08909(2021).
[241] Kiarash Mohammadi, Amir-Hossein Karimi, Gilles Barthe, and Isabel Valera. 2021. Scaling guarantees for near-
estcounterfactualexplanations.InProceedingsoftheACMConferenceonAI,Ethics,andSociety.ACM,NewYork,
177–187.https://doi.org/10.1145/3461702.3462514
[242] WellingtonRodrigoMonteiroandGilbertoReynoso-Meza.2022.Counterfactualgenerationthroughmulti-objective
constrainedoptimisation.(2022),23.https://www.researchsquare.com/article/rs-1325730/v1
[243] SérgioMoro,PauloCortez,andPauloRita.2014.Adata-drivenapproachtopredictthesuccessofbanktelemarketing.
DecisionSupportSystems62(2014),22–31.https://doi.org/10.1016/j.dss.2014.03.001
[244] RamaravindK.Mothilal,AmitSharma,andChenhaoTan.2020.Explainingmachinelearningclassifiersthrough
diversecounterfactualexplanations.InProceedingsoftheConferenceonFairness,Accountability,andTransparency
(FAccT’20)(FAT*’20).ACM,NewYork,https://doi.org/10.1145/3351095.3372850
[245] SusanneG.Mueller,MichaelW.Weiner,LeonJ.Thal,RonaldC.Petersen,CliffordJack,WilliamJagust,JohnQ.
Trojanowski,ArthurW.Toga,andLaurelBeckett.2008.Alzheimer’sdiseaseneuroimaginginitiative.InAdvancesin
Alzheimer’sandParkinson’sDisease.SpringerUS,183–189.https://doi.org/10.1007/978-0-387-72076-018
[246] ChelseaM.Myers,EvanFreed,LuisFernandoLarisPardo,AnushayFurqan,SebastianRisi,andJichenZhu.2020.
Revealing Neural Network Bias to Non-Experts Through Interactive Counterfactual Examples. https://doi.org/
10.48550/ARXIV.2001.02271
[247] Philip Naumann and Eirini Ntoutsi. 2021. Consequence-aware Sequential Counterfactual Generation.
arXiv:cs.LG/2104.05592
[248] GuillermoNavas-Palencia.2021.OptimalCounterfactualExplanationsforScorecardModelling.https://arxiv.org/
abs/2104.08619
[249] DanielNemirovsky,NicolasThiebaut,YeXu,andAbhishekGupta.2021.Providingactionablefeedbackinhiring
marketplaces using generative adversarial networks. In Proceedings of WSDM 2021. ACM, New York, 4. https://
doi.org/10.1145/3437963.3441705
[250] DanielNemirovsky,NicolasThiebaut,YeXu,andAbhishekGupta.2022.CounteRGAN:Generatingcounterfactuals
forreal-timerecourseandinterpretabilityusingresidualGANs.InProceedingsofUAI2022.PMLR,1488–1497.https://
proceedings.mlr.press/v180/nemirovsky22a.html
[251] TriMinhNguyen,ThomasP.Quinn,ThinNguyen,andTruyenTran.2021.CounterfactualExplanationwithMulti-
AgentReinforcementLearningforDrugTargetPrediction.arXiv:cs.AI/2103.12983
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:37
[252] DaniloNumerosoandDavideBacciu.2021.MEG:Generatingmolecularcounterfactualexplanationsfordeepgraph
networks. In 2021 International Joint Conference on Neural Networks (IJCNN). 1–8. DOI:https://doi.org/10.1109/
IJCNN52387.2021.9534266
[253] Andrew O’Brien and Edward Kim. 2021. Multi-Agent Algorithmic Recourse. https://doi.org/10.48550/
ARXIV.2110.00673
[254] House of Commons. [n. d.]. Algorithms in Decision Making. https://publications.parliament.uk/pa/cm201719/
cmselect/cmsctech/351/351.pdf.Accessed:2020-10-15.
[255] KwanseokOh,JeeSeokYoon,andHeung-IlSuk.2020.BornIdentityNetwork:Multi-wayCounterfactualMapGen-
erationtoExplainaClassifier’sDecision.https://doi.org/10.48550/ARXIV.2011.10381
[256] KwanseokOh,JeeSeokYoon,andHeung-IlSuk.2021.Learn-Explain-Reinforce:CounterfactualReasoningandIts
GuidancetoReinforceanAlzheimer’sDiseaseDiagnosisModel.https://doi.org/10.48550/ARXIV.2108.09451
[257] MatthewL.Olson,RoliKhanna,LawrenceNeal,FuxinLi,andWeng-KeenWong.2021.Counterfactualstateex-
planationsforreinforcementlearningagentsviagenerativedeeplearning.ArtificialIntelligence295(2021),103455.
https://doi.org/10.1016/j.artint.2021.103455
[258] AxelParmentierandThibautVidal.2021.OptimalCounterfactualExplanationsinTreeEnsembles.https://arxiv.org/
abs/2106.06631
[259] Martin Pawelczyk, Chirag Agarwal, Shalmali Joshi, Sohini Upadhyay, and Himabindu Lakkaraju. 2022. Explor-
ingcounterfactualexplanationsthroughthelensofadversarialexamples:Atheoreticalandempiricalanalysis.In
Proceedingsofthe25thInternationalConferenceonArtificialIntelligenceandStatistics.PMLR,4574–4594.https://
proceedings.mlr.press/v151/pawelczyk22a.html
[260] Martin Pawelczyk, Sascha Bielawski, Johannes van den Heuvel, Tobias Richter, and Gjergji Kasneci. 2021.
CARLA: A Python Library to Benchmark Algorithmic Recourse and Counterfactual Explanation Algorithms.
arXiv:cs.LG/2108.00783
[261] Martin Pawelczyk, Klaus Broelemann, and Gjergji. Kasneci. 2020. On counterfactual explanations under predic-
tivemultiplicity.InProceedingsofMachineLearningResearch.PMLR,Virtual,9.http://proceedings.mlr.press/v124/
pawelczyk20a.html
[262] MartinPawelczyk,TeresaDatta,Johannesvan-denHeuvel,GjergjiKasneci,andHimabinduLakkaraju.2022.Prob-
abilisticallyRobustRecourse:NavigatingtheTrade-offsbetweenCostsandRobustnessinAlgorithmicRecourse.
https://doi.org/10.48550/ARXIV.2203.06768
[263] MartinPawelczyk,KlausBroelemann,andGjergjiKasneci.2020.Learningmodel-agnosticcounterfactualexplana-
tionsfortabulardata.InProceedingsofTheWebConference.AssociationforComputingMachinery,NewYork,NY,
USA.DOI:https://doi.org/10.1145/3366423.3380087
[264] JudeaPearl.2000.Causality:Models,Reasoning,andInference.CambridgeUniversityPress,Cambridge,MA,USA.
[265] TejaswiniPedapati,AvinashBalakrishnan,KarthikeyanShanmugan,andAmitDhurandhar.2020.Learningglobal
transparentmodelsconsistentwithlocalcontrastiveexplanations.InProceedingsofNeurIPS2020.CurranAssociates
Inc.,11.
[266] Oana-IulianaPopescu,MahaShadaydeh,andJoachimDenzler.2021.CounterfactualGenerationwithKnockoffs.
https://doi.org/10.48550/ARXIV.2102.00951
[267] RafaelPoyiadzi,KacperSokol,RaulSantos-Rodriguez,TijlDeBie,andPeterFlach.2020.FACE:FeasibleandAction-
ableCounterfactualExplanations.https://doi.org/10.1145/3375627.3375850arXiv:1909.09369.
[268] MarioAlfonsoPrado-Romero,BardhPrenkaj,GiovanniStilo,andFoscaGiannotti.2022.ASurveyonGraphCoun-
terfactualExplanations:Definitions,Methods,Evaluation.https://doi.org/10.48550/ARXIV.2210.12089
[269] WentingQiandCharalamposChelmis.2021.Improvingalgorithmicdecision–makinginthepresenceofuntrust-
worthytrainingdata.InProceedingsofthe2021IEEEInternationalConferenceonBigData(BigData’21).1102–1108.
https://doi.org/10.1109/BigData52589.2021.9671677
[270] GouthamRamakrishnan,Y.C.Lee,andAwsAlbarghouthi.2020.Synthesizingactionsequencesformodifyingmodel
decisions.InProceedingsoftheConferenceonArtificialIntelligence(AAAI’20).AAAIpress,California,USA,16.http://
arxiv.org/abs/1910.00057
[271] YanouRamon,DavidMartens,FosterProvost,andTheodorosEvgeniou.2020.Acomparisonofinstance-levelcoun-
terfactualexplanationalgorithmsforbehavioralandtextualdata:SEDC,LIME-CandSHAP-C.AdvancesinData
AnalysisandClassification14,4(2020),801–819.DOI:https://doi.org/10.1007/s11634-020-00418-3
[272] PeymanRasouliandIngridChiehYu.2022.CARE:Coherentactionablerecoursebasedonsoundcounterfactual
explanations.InternationalJournalofDataScienceandAnalytics(2022),1–26.https://doi.org/10.1007/s41060-022-
00365-6
[273] PeymanRasouliandIngridChiehYu.2021.Analyzingandimprovingtherobustnessoftabularclassifiersusing
counterfactualexplanations.InProceedingsofthe202120thIEEEInternationalConferenceonMachineLearningand
Applications(ICMLA’21).1286–1293.https://doi.org/10.1109/ICMLA52953.2021.00209
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:38 S.Vermaetal.
[274] ShubhamRathi.2019.GeneratingCounterfactualandContrastiveExplanationsusingSHAP.http://arxiv.org/abs/
1906.09293arXiv:1906.09293.
[275] ShauliRavfogel,GrushaPrasad,TalLinzen,andYoavGoldberg.2021.Counterfactualinterventionsrevealthecausal
effectofrelativeclauserepresentationsonagreementprediction.InProceedingsofthe25thConferenceonComputa-
tionalNaturalLanguageLearning.AssociationforComputationalLinguistics,194–209.https://doi.org/10.18653/v1/
2021.conll-1.15
[276] AmbareeshRavi,XiaozhuoYu,IaraSantelices,FakhriKarray,andBarisFidan.2021.Generalframeworksforanomaly
detectionexplainability:Comparativestudy.InProceedingsofthe2021IEEEInternationalConferenceonAutonomous
Systems(ICAS’21).1–5.https://doi.org/10.1109/ICAS49788.2021.9551129
[277] KaivalyaRawal,EceKamar,andHimabinduLakkaraju.2021.AlgorithmicRecourseintheWild:Understandingthe
ImpactofDataandModelShifts.arXiv:cs.LG/2012.11788
[278] KaivalyaRawalandHimabinduLakkaraju.2020.Beyondindividualizedrecourse:Interpretableandinteractivesum-
mariesofactionablerecourses.InAdvancesinNeuralInformationProcessingSystems,Vol.33.CurranAssociates,Inc.,
12187–12198.https://proceedings.neurips.cc/paper/2020/file/8ee7730e97c67473a424ccfeff49ab20-Paper.pdf
[279] AnnabelleRedelmeier,MartinJullum,KjerstiAas,andAndersLøland.2021.MCCE:MonteCarloSamplingofReal-
isticCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2111.09790
[280] ChrisReed,KeriGrieman,andJosephEarly.2021.Non-AsimovexplanationsregulatingAIthroughtransparency.In
QueenMaryLawResearchPaperNo.370/2021.https://ssrn.com/abstract=3970518
[281] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin.2016.“WhyShouldITrustYou?”:Explainingthepredictions
ofanyclassifier.InProceedingsofKDD’16.ACM,NewYork,10.https://doi.org/10.1145/2939672.2939778
[282] MarcoTulioRibeiro,SameerSingh,andCarlosGuestrin.2018.Anchors:High-precisionmodel-agnosticexplana-
tions.InProceedingsoftheConferenceonArtificialIntelligence(AAAI’18).AAAIPress,California,USA,9.https://
www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16982
[283] MarcelRobeer,FlorisBex,andAdFeelders.2021.Generatingrealisticnaturallanguagecounterfactuals.InFindingsof
theAssociationforComputationalLinguistics(EMNLP2021).AssociationforComputationalLinguistics,PuntaCana,
DominicanRepublic,3611–3625.https://doi.org/10.18653/v1/2021.findings-emnlp.306
[284] PauRodriguez,MassimoCaccia,AlexandreLacoste,LeeZamparo,IssamLaradji,LaurentCharlin,andDavidVazquez.
2021.BeyondTrivialCounterfactualExplanationswithDiverseValuableExplanations.https://doi.org/10.48550/
ARXIV.2103.10226
[285] AlexisRoss,HimabinduLakkaraju,andOsbertBastani.2021.Learningmodelsforactionablerecourse.InAdvancesin
NeuralInformationProcessingSystems,Vol.34.CurranAssociates,Inc.,18734–18746.https://proceedings.neurips.cc/
paper/2021/file/9b82909c30456ac902e14526e63081d4-Paper.pdf
[286] David-HillelRuben.1992.Counterfactuals.RoutledgePublishers.https://philarchive.org/archive/RUBEE-3
[287] ChrisRussell.2019.Efficientsearchfordiversecoherentexplanations.InProceedingsoftheConferenceonFairness,
Accountability,andTransparency(FAccT’19)(FAT*’19).ACM,NewYork,9.https://doi.org/10.1145/3287560.3287569
[288] SophieSadler,DerekGreene,andDanielW.Archambault.2021.Astudyofexplainablecommunity-levelfeatures.In
GEM:GraphEmbeddingandMining(ECML-PKDD2021Workshop+Tutorial).
[289] SuryaShravanKumarSajja,SumantaMukherjee,SatyamDwivedi,andVikasC.Raykar.2021.Semi-supervised
CounterfactualExplanations.https://openreview.net/forum?id=o6ndFLB1DST
[290] Robert-FlorianSamoilescu,ArnaudVanLooveren,andJanisKlaise.2021.Model-agnosticandScalableCounterfac-
tualExplanationsviaReinforcementLearning.https://doi.org/10.48550/ARXIV.2106.02597
[291] PedroSanchezandSotiriosA.Tsaftaris.2022.DiffusionCausalModelsforCounterfactualEstimation.https://doi.org/
10.48550/ARXIV.2202.10166
[292] MaximilianSchleich,ZixuanGeng,YihongZhang,andDanSuciu.2021.GeCo:QualityCounterfactualExplanations
inRealTime.arXiv:cs.LG/2101.01292
[293] LisaSchut,OscarKey,RoryMcGrath,LucaCostabello,BogdanSacaleanu,MedbCorcoran,andYarinGal.2021.Gen-
eratingInterpretableCounterfactualExplanationsByImplicitMinimisationofEpistemicandAleatoricUncertainties.
https://doi.org/10.48550/ARXIV.2103.08951
[294] R.R.Selvaraju,M.Cogswell,A.Das,R.Vedantam,D.Parikh,andD.Batra.2017.Grad-CAM:Visualexplanations
fromdeepnetworksviagradient-basedlocalization.InProceedingsoftheIEEEInternationalConferenceonComputer
Vision.618–626.https://doi.org/10.1109/ICCV.2017.74
[295] KumbaSennaar.2019.MachineLearningforRecruitingandHiring–6CurrentApplications.https://emerj.com/ai-
sector-overviews/machine-learning-for-recruiting-and-hiring/.Accessed:2020-10-15.
[296] RuoxiShang,K.J.KevinFeng,andChiragShah.2022.WhyamInotseeingit?Understandingusers’needsfor
counterfactualexplanationsineverydayrecommendations.InProceedingsof FAccT’22.ACM,NewYork,11.https://
doi.org/10.1145/3531146.3533189
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:39
[297] XiaotingShaoandKristianKersting.2022.Gradient-basedCounterfactualExplanationsusingTractableProbabilistic
Models.https://doi.org/10.48550/ARXIV.2205.07774
[298] ShubhamSharma,JetteHenderson,andJoydeepGhosh.2019.CERTIFAI:CounterfactualExplanationsforRobust-
ness,Transparency,Interpretability,andFairnessofArtificialIntelligencemodels.http://arxiv.org/abs/1905.07857
[299] RezaShokri,MartinStrobel,andYairZick.2021.Ontheprivacyrisksofmodelexplanations.InProceedingsofthe
2021AAAI/ACMConferenceonAI,Ethics,andSociety.ACM,NewYork,11.https://doi.org/10.1145/3461702.3462533
[300] RonalRajneshwarSingh,PaulDourish,PiersHowe,TimMiller,LizSonenberg,EduardoVelloso,andFrankVet-
ere.2021.DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications.https://doi.org/
10.1145/3579363
[301] SauravSingla.2020.MachineLearningtoPredictCreditRiskinLendingIndustry.https://www.aitimejournal.com/
@saurav.singla/machine-learning-to-predict-credit-risk-in-lending-industry.Accessed:2020-10-15.
[302] DylanSlack,SophieHilgard,HimabinduLakkaraju,andSameerSingh.2021.CounterfactualExplanationsCanBe
Manipulated.arXiv:cs.LG/2106.02666
[303] J.W.Smith,J.Everhart,W.C.Dickson,W.Knowler,andR.Johannes.1988.UsingtheADAPlearningalgorithmto
forecasttheonsetofdiabetesmellitus.InProceedingsoftheAnnualSymposiumonComputerApplicationinMedical
Care.AmericanMedicalInformaticsAssociation,Washington,D.C.,261–265.
[304] SimónC.SmithandSubramanianRamamoorthy.2020.Counterfactualexplanationandcausalinferenceinservice
ofrobustnessinrobotcontrol.InProceedingsofthe2020JointIEEE10thInternationalConferenceonDevelopmentand
LearningandEpigeneticRobotics(ICDL-EpiRob’20).1–8.https://doi.org/10.1109/ICDL-EpiRob48136.2020.9278061
[305] KacperSokolandPeterFlach.2018.Glass-Box:ExplainingAIdecisionswithcounterfactualstatementsthrough
conversation with a voice-enabled virtual assistant. In Proceedings of IJCAI’18. AAAI Press, 5868–5870. https://
doi.org/10.24963/ijcai.2018/865
[306] KacperSokolandPeterFlach.2019.Desiderataforinterpretability:Explainingdecisiontreepredictionswithcoun-
terfactuals.InProceedingsoftheConferenceonArtificialIntelligence(AAAI)33(July2019).https://doi.org/10.1609/
aaai.v33i01.330110035
[307] ThomasSpooner,DanialDervovic,JasonLong,JonShepard,JiahaoChen,andDanieleMagazzeni.2021.Counterfac-
tualExplanationsforArbitraryRegressionModels.https://arxiv.org/abs/2106.15212
[308] LauraState.2021.LogicprogrammingforXAI:Atechnicalperspective.InProceedingsoftheInternationalConference
onLogicProgramming2021Workshops(ICLP’21),Vol.2970.http://ceur-ws.org/Vol-2970/meepaper1.pdf
[309] Gregory Stein. 2021. Generating high-quality explanations for navigation in partially-revealed environments.
In Advances in Neural Information Processing Systems, Vol. 34. Curran Associates, Inc., 17493–17506. https://
proceedings.neurips.cc/paper/2021/file/926ec030f29f83ce5318754fdb631a33-Paper.pdf
[310] DeborahSulem,MicheleDonini,MuhammadBilalZafar,Francois-XavierAubet,JanGasthaus,TimJanuschowski,
SanjivDas,KrishnaramKenthapadi,andCedricArchambeau.2022.DiverseCounterfactualExplanationsforAnom-
alyDetectioninTimeSeries.https://doi.org/10.48550/ARXIV.2203.11103
[311] EzzeldinTahounandAndreKassis.2020.BeyondExplanations:RecourseviaActionableInterpretability-Extended.
https://doi.org/10.13140/RG.2.2.19076.14729
[312] PaoloTamagnini,JosuaKrause,AritraDasgupta,andEnricoBertini.2017.Interpretingblack-boxclassifiersusing
instance-levelvisualexplanations.InProceedingsofthe2ndWorkshoponHuman-In-the-LoopDataAnalytics.ACM,
NewYork,6.https://doi.org/10.1145/3077257.3077260
[313] JuntaoTan,ShuyuanXu,YingqiangGe,YunqiLi,XuChen,andYongfengZhang.2021.Counterfactualexplainable
recommendation.InProceedingsofthe30thACMInternationalConferenceonInformation&KnowledgeManagement.
ACM,NewYork,10.https://doi.org/10.1145/3459637.3482420
[314] Sarah Tan,Rich Caruana,Giles Hooker, andYin Lou. 2018.Distill-and-compare: Auditing black-boxmodels us-
ingtransparentmodeldistillation.InProceedingsofAIES’18.ACM,NewYork,8.https://doi.org/10.1145/3278721.
3278725
[315] JasonTashea.2017.CourtsAreUsingAItoSentenceCriminals.ThatMustStopNow.https://www.wired.com/2017/
04/courts-using-ai-sentence-criminals-must-stop-now/.Accessed:2020-10-15.
[316] MohammedTemrazandMarkT.Keane.2021.SolvingtheClassImbalanceProblemUsingaCounterfactualMethod
forDataAugmentation.https://doi.org/10.48550/ARXIV.2111.03516
[317] MohammedTemraz,EoinM.Kenny,ElodieRuelle,LaurenceShalloo,BarrySmyth,andMarkT.Keane.2021.Han-
dlingclimatechangeusingcounterfactuals:Usingcounterfactualsindataaugmentationtopredictcropgrowthin
anuncertainclimatefuture.InCase-BasedReasoningResearchandDevelopment.SpringerInternationalPublishing,
Cham,216–231.
[318] T.Teofili,D.Firmani,N.Koudas,V.Martello,P.Merialdo,andD.Srivastava.2022.Effectiveexplanationsforentity
resolutionmodels.InProceedingsofthe2022IEEE38thInternationalConferenceonDataEngineering(ICDE’22).IEEE
ComputerSociety,LosAlamitos,CA,USA,2709–2721.https://doi.org/10.1109/ICDE53745.2022.00248
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:40 S.Vermaetal.
[319] PaulThagard.1989.Explanatorycoherence.BehavioralandBrainSciences(1989),435–467.https://doi.org/10.1017/
S0140525X00057046
[320] JayaramanThiagarajan,VivekSivaramanNarayanaswamy,DeeptaRajan,JiaLiang,AkshayChaudhari,andAndreas
Spanias.2021.Designingcounterfactualgeneratorsusingdeepmodelinversion.InAdvancesinNeuralInformation
ProcessingSystems,Vol.34.CurranAssociates,Inc.,16873–16884.https://proceedings.neurips.cc/paper/2021/file/
8ca01ea920679a0fe3728441494041b9-Paper.pdf
[321] EricoTjoaandCuntaiGuan.2019.ASurveyonExplainableArtificialIntelligence(XAI):TowardsMedicalXAI.
arXiv:cs.LG/1907.07374
[322] GeorgeTolkachev,StephenMell,StephanZdancewic,andOsbertBastani.2022.Counterfactualexplanationsfornatu-
rallanguageinterfaces.InProceedingsofthe60thAnnualMeetingoftheAssociationforComputationalLinguistics(Vol-
ume2:ShortPapers).AssociationforComputationalLinguistics,Dublin,Ireland,113–118.https://aclanthology.org/
2022.acl-short.14
[323] GabrieleTolomei,FabrizioSilvestri,AndrewHaines,andMouniaLalmas.2017.Interpretablepredictionsoftree-
basedensemblesviaactionablefeaturetweaking.InProceedingsoftheInternationalConferenceonKnowledgeDiscov-
eryandDataMining(KDD’17).ACM,NewYork,10.https://doi.org/10.1145/3097983.3098039
[324] KhanhHiepTran,AzinGhazimatin,andRishirajSahaRoy.2021.CounterfactualExplanationsforNeuralRecom-
menders.ACM,NewYork,1627–1631.https://doi.org/10.1145/3404835.3463005
[325] MariaTsiakmakiandOmirosRagos.2021.Acasestudyofinterpretablecounterfactualexplanationsforthetaskof
predictingstudentacademicperformance.InProceedingsofthe202125thInternationalConferenceonCircuits,Systems,
CommunicationsandComputers(CSCC’21).https://doi.org/10.1109/CSCC53858.2021.00029
[326] StratisTsirtsis,AbirDe,andManuelRodriguez.2021.Counterfactualexplanationsinsequentialdecisionmaking
underuncertainty.InAdvancesinNeuralInformationProcessingSystems,Vol.34.CurranAssociates,Inc.,30127–
30139.https://proceedings.neurips.cc/paper/2021/file/fd0a5a5e367a0955d81278062ef37429-Paper.pdf
[327] StratisTsirtsisandManuelGomez-Rodriguez.2020.Decisions,CounterfactualExplanationsandStrategicBehavior.
arXiv:cs.LG/2002.04333
[328] RyanTurner.2016.Amodelexplanationsystem:Latestupdatesandextensions.ArXivabs/1606.09517(2016).
[329] AaltoUniversity.[n.d.].TheEuropeanCommissionOffersSignificantSupporttoEurope’sAIExcellence.https://
www.eurekalert.org/pub_releases/2020-03/au-tec031820.php.Accessed:2020-10-15.
[330] Sohini Upadhyay, Shalmali Joshi, and Himabindu Lakkaraju. 2021. Towards Robust and Reliable Algorithmic
Recourse.arXiv:cs.LG/2102.13620
[331] BerkUstun,AlexanderSpangher,andYangLiu.2019.Actionablerecourseinlinearclassification.InProceedings
oftheConferenceonFairness,Accountability,andTransparency(FAccT’19)(FAT*’19).ACM,NewYork,10.https://
doi.org/10.1145/3287560.3287566
[332] ArnaudVanLooverenandJanisKlaise.2020.InterpretableCounterfactualExplanationsGuidedbyPrototypes.http:
//arxiv.org/abs/1907.02584
[333] ArnaudVanLooveren,JanisKlaise,GiovanniVacanti,andOliverCobb.2021.ConditionalGenerativeModelsfor
CounterfactualExplanations.https://doi.org/10.48550/ARXIV.2101.10123
[334] SimonVandenhende,DhruvMahajan,FilipRadenovic,andDeeptiGhadiyaram.2022.Makingheadsortails:To-
wardssemanticallyconsistentvisualcounterfactuals.InProceedingsofECCV2022.https://doi.org/10.1007/978-3-
031-19775-816
[335] SahilVerma,JohnDickerson,andKeeganHines.2020.CounterfactualExplanationsforMachineLearning:AReview.
https://doi.org/10.48550/ARXIV.2010.10596
[336] SahilVerma,JohnDickerson,andKeeganHines.2021.CounterfactualExplanationsforMachineLearning:Chal-
lengesRevisited.https://doi.org/10.48550/ARXIV.2106.07756
[337] SahilVerma,KeeganHines,andJohnP.Dickerson.2021.AmortizedGenerationofSequentialCounterfactualExpla-
nationsforBlack-boxModels.arXiv:cs.LG/2106.03962
[338] SahilVermaandJuliaRubin.2018.Fairnessdefinitionsexplained.InProceedingsoftheInternationalWorkshopon
SoftwareFairness(FairWare’18).ACM,NewYork,1–7.https://doi.org/10.1145/3194770.3194776
[339] Sahil Verma, Chirag Shah, John P. Dickerson, Anurag Beniwal, Narayanan Sadagopan, and Arjun Se-
shadri. 2023. RecXplainer: Amortized Attribute-based Personalized Explanations for Recommender Systems.
arXiv:cs.IR/2211.14935
[340] TomVermeire,DieterBrughmans,SofieGoethals,RaphaelMazzineBarbossadeOliveira,andDavidMartens.[n.
d.].Explainableimageclassificationwithevidencecounterfactual.PatternAnal.Appl.([n.d.]),21.https://doi.org/
10.1007/s10044-021-01055-y
[341] Cédric Villani. [n. d.]. For a Meaningful Artificial Intelligence. https://www.aiforhumanity.fr/pdfs/
MissionVillaniReportENG-VF.pdf.Accessed:2020-10-15.
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

CounterfactualExplanationsandAlgorithmicRecoursesforMachineLearning 312:41
[342] MarcoVirgolinandSaverioFracaros.2022.OntheRobustnessofSparseCounterfactualExplanationstoAdverse
Perturbations.https://doi.org/10.48550/ARXIV.2201.09051
[343] J.vonKügelgen,N.Agarwal,J.Zeitler,A.Mastouri,andB.Schölkopf.2021.Algorithmicrecourseinpartiallyand
fullyconfoundedsettingsthroughboundingcounterfactualeffects.InProceedingsoftheICML2021Workshopon
AlgorithmicRecourse.https://sites.google.com/view/recourse21/home
[344] J.vonKügelgen,A.-H.Karimi,U.Bhatt,I.Valera,A.Weller,andB.Schölkopf.2022.Onthefairnessofcausalalgo-
rithmicrecourse.InProceedingsofthe36thAAAIConferenceonArtificialIntelligence,Vol.9.AAAIPress,PaloAlto,
CA,9584–9594.https://doi.org/10.1609/aaai.v36i9.21192
[345] SandraWachter,BrentMittelstadt,andLucianoFloridi.2017.Whyarighttoexplanationofautomateddecision-
makingdoesnotexistinthegeneraldataprotectionregulation.InternationalDataPrivacyLaw7,2(062017).https:
//doi.org/10.1093/idpl/ipx005
[346] SandraWachter,BrentMittelstadt,andChrisRussell.2017.Counterfactualexplanationswithoutopeningtheblack
box:AutomateddecisionsandtheGDPR.SSRNElectronicJournal31,2(2017).https://doi.org/10.2139/ssrn.3063289
[347] PeiWangandNunoVasconcelos.2020.SCOUT:Self-awarediscriminantcounterfactualexplanations.InProceed-
ings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR’20). https://doi.org/10.1109/
CVPR42600.2020.00900
[348] XiaosongWang,YifanPeng,LeLu,ZhiyongLu,MohammadhadiBagheri,andRonaldM.Summers.2017.ChestX-
ray8:Hospital-scalechestX-Raydatabaseandbenchmarksonweakly-supervisedclassificationandlocalizationof
commonthoraxdiseases.InProceedingsofCVPR.https://doi.org/10.1007/978-3-030-13969-818
[349] YongjieWang,QinxuDing,KeWang,YueLiu,XingyuWu,JinglongWang,YongLiu,andChunyanMiao.2021.The
skylineofcounterfactualexplanationsformachinelearningdecisionmodels.InProceedingsofCIKM.ACM,New
York,10.https://doi.org/10.1145/3459637.3482397
[350] YongjieWang,HangweiQian,andChunyanMiao.2022.DualCF:Efficientmodelextractionattackfromcounterfac-
tualexplanations.InProceedingsofFAccT’22.ACM,NewYork.,12.https://doi.org/10.1145/3531146.3533188
[351] ZhendongWang,IsakSamsten,RamiMochaourab,andPanagiotisPapapetrou.2021.Learningtimeseriescounter-
factualsvialatentspacerepresentations.InDiscoveryScience.SpringerInternationalPublishing,Cham,369–384.
https://doi.org/10.1007/978-3-030-88942-529
[352] ZhendongWang,IsakSamsten,andPanagiotisPapapetrou.2021.Counterfactualexplanationsforsurvivalprediction
ofcardiovascularICUpatients.InArtificialIntelligenceinMedicine.SpringerInternationalPublishing,Cham,338–
348.https://doi.org/10.1007/978-3-030-77211-638
[353] Greta Warren, Mark T. Keane, and Ruth M. J. Byrne. 2022. Features of Explainability: How Users Understand
CounterfactualandCausalExplanationsforCategoricalandContinuousFeaturesinXAI.https://doi.org/10.48550/
ARXIV.2204.10152
[354] GretaWarren,MarkT.Keane,ChristopheGueret,andEoinDelaney.2023.ExplainingGroupsofInstancesCounter-
factuallyforXAI:AUseCase,AlgorithmandUserStudyforGroup-Counterfactuals.arXiv:cs.AI/2303.09297
[355] GeemiP.Wellawatte,AditiSeshadri,andAndrewD.White.2022.Modelagnosticgenerationofcounterfactualex-
planationsformolecules.Chem.Sci.13(2022),3697–3705.https://doi.org/10.1039/D1SC05259D
[356] J.Wexler,M.Pushkarna,T.Bolukbasi,M.Wattenberg,F.Viégas,andJ.Wilson.2020.TheWhat-Iftool:Interactive
probingofmachinelearningmodels.IEEETransactionsonVisualizationandComputerGraphics26,1(2020),56–65.
https://doi.org/10.1109/TVCG.2019.2934619
[357] AdamWhiteandArturd’AvilaGarcez.2019.MeasurableCounterfactualLocalExplanationsforAnyClassifier.http:
//arxiv.org/abs/1908.03020
[358] Adam White and Artur d’Avila Garcez. 2021. Counterfactual Instances Explain Little. https://doi.org/10.48550/
ARXIV.2109.09809
[359] AdamWhite,KwunHoNgan,JamesPhelan,SamanSadeghiAfgeh,KevinRyan,ConstantinoCarlosReyes-Aldasoro,
andArturd’AvilaGarcez.2021.ContrastiveCounterfactualVisualExplanationswithOverdetermination.https://
doi.org/10.48550/ARXIV.2106.14556
[360] AnjanaWijekoon,NirmalieWiratunga,IkechukwuNkisi-Orji,KyleMartin,ChamathPalihawadana,andDavidCor-
sar.2021.Counterfactualexplanationsforstudentoutcomepredictionwithmoodlefootprints.InProceedingsofthe
CEURWorkshop,1–8.https://rgu-repository.worktribe.com/output/1395861
[361] NirmalieWiratunga,AnjanaWijekoon,IkechukwuNkisi-Orji,KyleMartin,ChamathPalihawadana,andDavidCor-
sar.2021.DisCERN:Discoveringcounterfactualexplanationsusingrelevancefeaturesfromneighbourhoods.InPro-
ceedings ofthe2021IEEE33rdInternationalConferenceonToolswithArtificial Intelligence(ICTAI’21).1466–1473.
https://doi.org/10.1109/ICTAI52525.2021.00233
[362] JamesWoodward.2003.MakingThingsHappen:ATheoryofCausalExplanation.OxfordUniversityPress.
[363] Xintao Xiang and Artem Lenskiy. 2022. Realistic Counterfactual Explanations by Learned Relations. https://
arxiv.org/abs/2202.07356
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.

312:42 S.Vermaetal.
[364] ShuyuanXu,YunqiLi,ShuchangLiu,ZuohuiFu,YingqiangGe,XuChen,andYongfengZhang.2021.Learningcausal
explanationsforrecommendation.CEURWorkshopProceedings2911(2021),13–25.
[365] YanivYacoby,BenGreen,ChristopherL.Griffin,andFinaleDoshiVelez.2022.“Ifitdidn’thappen,whywould
IChangemyDecision?”:HowJudgesRespondtoCounterfactualExplanationsforthePublicSafetyAssessment.
https://doi.org/10.48550/ARXIV.2205.05424
[366] PrateekYadav,PeterHase,andMohitBansal.2021.Low-CostAlgorithmicRecourseforUserswithUncertainCost
Functions.https://doi.org/10.48550/ARXIV.2111.01235
[367] FanYang,SahanSureshAlva,JiahaoChen,andXiaHu.2021.Model-basedcounterfactualsynthesizerforinterpre-
tation.InProceedingsof KDD’21.ACM,NewYork,1964–1974.https://doi.org/10.1145/3447548.3467333
[368] FanYang,NinghaoLiu,MengnanDu,andXiaHu.2021.Generativecounterfactualsforneuralnetworksviaattribute-
informedperturbation.SIGKDDExplor.Newsl.23(May2021),10.https://doi.org/10.1145/3468507.3468517
[369] LinyiYang,EoinKenny,TinLokJamesNg,YiYang,BarrySmyth,andRuihaiDong.2020.Generatingplausible
counterfactualexplanationsfordeeptransformersinfinancialtextclassification.InProceedingsofICCL.6150–6160.
https://doi.org/10.18653/v1/2020.coling-main.541
[370] NakyeongYang,TaegwanKang,andKyominJung.2022.Derivingexplainablediscriminativeattributesusingcon-
fusionaboutcounterfactualclass.InProceedingsofICASSP2022.1730–1734.https://doi.org/10.1109/ICASSP43922.
2022.9747693
[371] YuanshunYao,ChongWang,andHangLi.2022.CounterfactuallyEvaluatingExplanationsinRecommenderSystems.
https://doi.org/10.48550/ARXIV.2203.01310
[372] I-Cheng Yeh. 2016. Default of Credit Card Clients. UCI Machine Learning Repository. https://doi.org/10.24432/
C55S3H
[373] RoozbehYousefzadehandDianneP.O’Leary.2019.DebuggingTrainedMachineLearningModelsusingFlipPoints.
https://debug-ml-iclr2019.github.io/cameraready/DebugML-19paper11.pdf
[374] ZixuanYuan,YadaZhu,WeiZhang,ZimingHuang,GuangnanYe,andHuiXiong.2021.Multi-DomainTransformer-
BasedCounterfactualAugmentationforEarningsCallAnalysis.https://doi.org/10.48550/ARXIV.2112.00963
[375] WencanZhangandBrianYLim.2022.TowardsrelatableexplainableAIwiththeperceptualprocess.ACM,New
York,https://doi.org/10.1145/3491102.3501826
[376] YuhaoZhang.,KevinMcAreavey.,andWeiruLiu.2022.Developingandexperimentingonapproachestoexplainabil-
ityinAIsystems.InProceedingsofICAART.SciTePress,518–527.https://doi.org/10.5220/0010900300003116
[377] YunxiaZhao.2020.FastReal-timeCounterfactualExplanations.https://doi.org/10.48550/ARXIV.2007.05684
[378] JinfengZhongandElsaNegre.2022.Shap-enhancedcounterfactualexplanationsforrecommendations.InProceed-
ingsofthe37thACM/SIGAPPSymposiumonAppliedComputing.ACM,NewYork,1365–1372.https://doi.org/10.1145/
3477314.3507029
[379] B.Zhou,A.Khosla,A.Lapedriza,A.Oliva,andA.Torralba.2016.Learningdeepfeaturesfordiscriminativelocaliza-
tion.InProceedingsofCVPR.IEEE,NewYork,USA,2921–2929.https://doi.org/10.1109/CVPR.2016.319
[380] YaoZhou,HaonanWang,JingruiHe,andHaixunWang.2021.FromIntrinsictoCounterfactual:OntheExplainability
ofContextualizedRecommenderSystems.https://doi.org/10.48550/ARXIV.2110.14844
[381] Alexander Zien, Nicole Krämer, Sören Sonnenburg, and Gunnar Rätsch. 2009. The feature importance ranking
measure. In Machine Learning and Knowledge Discovery in Databases, Vol. 5782. Springer Berlin, Berlin. https://
doi.org/10.1007/978-3-642-04174-7_45
Received25July2023;revised21June2024;accepted5July2024
ACMComput.Surv.,Vol.56,No.12,Article312.Publicationdate:October2024.