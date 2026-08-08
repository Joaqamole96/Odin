InformationProcessingandManagement61(2024)103704
ContentslistsavailableatScienceDirect
InformationProcessingandManagement
journalhomepage:www.elsevier.com/locate/ipm
Financialrisktoleranceprofilingfromtext
FrankXing
SchoolofComputing,NationalUniversityofSingapore,Singapore,Singapore
A R T I C L E I N F O A B S T R A C T
Keywords: Traditionally, individual financial risk tolerance information is gathered via questionnaires
Artificialintelligenceinfinance or similar structured psychometric tools. Our abundant digital footprint, as an unstructured
Risktolerance alternative, is less investigated. Leveraging such information can potentially support large-
Riskprofiling scale and cost-efficient financial services. Therefore, I explore the possibility of building a
Textmining
computational model that distills risk tolerance information from user texts in this study,
Convolutionalneuralnetwork
and discuss the design principles discovered from empirical results and their implications.
Specifically,anewquaternaryclassificationtaskisdefinedfortextmining-basedriskprofiling.
Experimentsshowthatpre-trainedlargelanguagemodelssetabaselinemicro-F1ofcirca0.34.
Usingaconvolutionalneuralnetwork(CNN),thereportedsystemachievesamicro-F1ofcirca
0.51, which significantly outperforms the baselines, and is a circa 4% further improvement
over the standard CNN configurations (micro-F1 of circa 0.47). Textual feature richness and
supervisedlearningarefoundtobethekeycontributorstomodelperformances,whileother
machine learning strategies suggested by previous research (data augmentation and multi-
tasking)arelesseffective.Thefindingsconfirmusertextstobeausefulriskprofilingresource
andprovideseveralinsightsonthistask.
1. Introduction
Riskhasbeenacentraltopicinfinancefromtheverybeginning(Markowitz,1952;Sharpe,1964)andisstillacriticalconcept
inmanyfinancialdecision-makingandmodelingprocessestoday.Forexample,thecapitalassetpricingmodel(CAPM)calculates
market risk premium at an aggregated level and uses it to explain different expected returns from different financial assets; the
assetallocationmodelsusetheriskaversionatanindividualleveltodecidetheoptimalportfolioholdingweights(Thavaneswaran
et al., 2021; Xing et al., 2019b); banks use companies’ auditing and fraudulent risk information and platforms use individuals’
creditriskinferredfromtheirself-disclosurestomakelendingdecisions(Sahaetal.,2016;Siering,2023).Thedigitalizationtrend
ofthefinancialmarket,theincreasingdiversityoffinancialproducts,andtherisinginfluenceofretailinvestorstogetheraddmore
uncertaintytoinvestment.Asaresult,investorsmaysuffertheriskoflossofincomeorevenlossofprincipalwheninvesting.Insuch
acontext,investorsneedtochooseinvestmentprojectsbasedontheirinvestmentgoalsandriskpreferences,andmanyinvestors
willconsultwithfinancialadvisorsbeforeinvesting,despitetheaccompanyingcost.
There is a pressing need to leverage the information available and transform financial planning into a more economic and
inclusive process. Although risk tolerance is an important factor in financial planning and consulting, a formal definition of it is
challenging (Hemrajani et al., 2023). Only in recent years have practitioners clearly realized the differences between many risk-
related concepts, including risk appetite/need, risk perception, risk preference, risk attitude, risk tolerance, risk aversion, risk capacity,
risk-taking behavior, risk profile, and more. Grable (2018) defines risk tolerance as the willingness to engage in risky behavior
in which possible outcomes can be negative. Therefore, investors with high risk tolerance are more likely to engage in more
E-mailaddress: xing@nus.edu.sg.
https://doi.org/10.1016/j.ipm.2024.103704
Received20November2023;Receivedinrevisedform29February2024;Accepted2March2024
Availableonline5March2024
0306-4573/© 2024 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license
(http://creativecommons.org/licenses/by-nc-nd/4.0/).

F.Xing InformationProcessingandManagement61(2024)103704
high-risk investments, while investors with low risk tolerance tend to be more conservative. Understanding such investors’ risk
toleranceinformationhelpsfinancialinstitutionsgaugecustomers’comfortlevelwithinvestmentriskandprovidecustomerswith
personalizedinformation.Inordertohelpcustomersmakebetterfinancialdecisions,financialinstitutionsneedtoprovidecustomers
with appropriate guidance. Before investing, many institutions require customers to answer questions in a survey, then complete
investment portfolios and provide customers with services and suggestions based on the survey results. This remains a standard
procedurefordigitalservices,e.g.,robo-advisory.Investorsareclassifiedintodifferentcategoriesaccordingtotheamountofloss
theycantolerate.Acommonpracticebyfinancialinstitutionsistodivideusers’risktoleranceintoseveralcategories,e.g.,radical,
moderate,andconservative.DBSBank,e.g.,currentlycustomizeseachofitsthemedportfoliosintoSlown’Steady(RiskLevel2),
ComfyCruisin’(RiskLevel3),andFastn’Furious(RiskLevel4)forthe‘‘digiPortfolio’’investmentproduct.1
Numerous previous studies argue that risk tolerance is closely related to other personal traits at an individual level, and an
investor’s behavior and goal can be understood through risk tolerance together with cognitive and emotional biases, as well as
investors’sentiment(Lengkeeketal.,2023;Xingetal.,2020;Yekrangi&Abdolvand,2021).Forinstance,PompianandLongo(2004)
suggestedthatinvestmentadvisorsconsiderclientgenderandpersonalitytoassessrisktolerancebeforeexecutinganinvestment
program according to the following four-step method: (1) Ask your client to take a personality type test; (2) Evaluate responses
to determine personality type; (3) Assess risk tolerance using the ‘‘Type and Gender-Based Risk tolerance Scales’’; (4) Execute
investment program. Nobre and Grable (2015) advised to better understand clients’ risk-taking behavior via evaluating their risk
tolerance,whichwasinfluencedbytheirriskprofile,riskperception,andriskneed.
Therisktoleranceinformationisalsoimportantatamacrolevel.Withknowledgeofinvestors’riskattitudesandpsychology,
behavioral finance reveals and explains some irrational behaviors of investors in the financial market. Investors and financial
planners may have cognitive and emotional biases when making important investment decisions (Athota et al., 2023; Yekrangi
&Abdolvand,2015).Anexampleofemotionalbiasisthatinvestors’overconfidencemaymakethemmoreinclinedtoreceivenews
thatenhancestheirself-confidencebutignoreinformationthatdiffersfromtheiropinions.Whensufferingaloss,thefeelingofpain
caused by the loss may make investors continue to hold these assets because they want to avoid the feeling of pain, which may
leadtocontinuedlossofassets.Themoreconfidentpeopleare,themorefrequentlytheywilltrade,andthemorelikelytheywill
receivelowreturns. Peoplewithlowrisktolerancemayexperienceopportunitylosses fromnotinvestinginstocks,whilepeople
withhighrisktoleranceinshort-terminvestingmaycauseunnecessarylossesinwealth(Yao&Hanna,2005).ThesurveybyAinia
andLutfi(2019)showsthatrisktolerancehadasignificantandpositiveeffectoninvestmentdecision-making:thehigheraperson’s
risktolerancelevel,thehighertheperson’sopportunitytoallocatefundstohigh-riskassets.Anunderstandingofrisktolerancewas
one necessary factor for a person to be able to make optimal portfolio choices in terms of risk-reward trade-offs, and choosing a
portfolionotconsistentwithrisktolerancemaycauseinvestordisappointmentandinferiorutility(Moreschi,2005).
With the accumulating digital footprints on social media and advances in natural language processing (NLP) comes the
opportunity to know your customer (including risk tolerance, behavioral biases, personality, and many other associated aspects)
through analyzing the online user generated content (UGC). In fact, the literature on personality detection or risk profiling for
corporate entities from text is abundant (Vinciarelli & Mohammadi, 2014; Yin et al., 2020). It is also reported that text-derived
personalitytraitseffectivelydepictandpredictconsumerperceptivebehaviorsinfinancialandhealthcontexts(Yangetal.,2023).
However, there was scant previous research that attempted to profile users’ financial risk tolerance directly from the UGC to the
best of my knowledge. The most relevant studies in this thread are those that measure patients’ personality and subjective risk
tolerance through questionnaire surveys and used regression methods to establish the relationship between personality traits and
risktolerance.Thesestudiesarekeytothemajorchallengeinthisresearchtask:thelackofrisktolerancelabelsforexistingtext
corpora.Inthisresearch,Isummarizetheresultsofthesestudiesandcalculateuserrisktolerancelabelsviapersonalitytraits.This
way,aconvolutionalneuralnetwork(CNN)modelthatdirectlyinfersthefinancialrisktoleranceofusersfromUGChasbeentrained.
SincethisstudyaimstotesttheeffectivenessofUGCfeaturesonthenewtaskratherthanoptimizingsystemperformances,theCNN
architectureischosenovertransformer-basedmodelsforitssimplerarchitecture,betterinteroperability,andarichpastliteratureto
comparewithwhenitisusedasatestbed.Thepresentedmethodcanhelpfinancialserviceprovidersbetterunderstandcustomers’
riskpreferencesinafastandcost-efficientmanner,thuspromotingfinancialinclusion.Fromtheclient’sperspective,providingthis
modelhelpsthemchooseappropriatefinancialproductsaccordingtotheirpersonalinvestmentpreferences,thusreducingpossible
lossesininvestment.Asaresult,clientsaremoresatisfiedwiththeserviceandwillbemorewillingtocontinueinvestingwiththe
institution.
This study attempts to address two main research objectives. The first objective is to test whether financial risk profiling can
directly benefit from user generated texts. Previous research documented that (1) financial risk tolerance is associated with
personality traits, and (2) personality traits can be modeled from user texts. However, it is unclear to what extent the useful
informationcanbepreserved.Thesecondobjectiveistodevelopmodelingguidelinesviaexperimentingwitheffectivetechniqueson
personalitydetection,includingrecurrentCNN(Nasir&Malik,2024),dataaugmentation(Yangetal.,2023),andmulti-tasking(Li
etal.,2022).
To preview the main result, it has been discovered that individuals’ digital footprint is an effective source of information for
financial risk tolerance profiling. Rich text representation features (pre-trained word embeddings from various language models)
benefitthemodelperformancemorethanmachinelearningtricks,e.g.,sentenceaugmentationandmultitasking.Specifically,this
studymakesthreemajorcontributions:
1 https://www.dbs.com.sg/personal/investments/other-investments/dbs-digiportfolio
2

F.Xing InformationProcessingandManagement61(2024)103704
Fig.1. Risk-relatedterminologiesandtheirrelations.
1. Itformallyproposesthefinancialrisktoleranceprofilingtaskasaquaternaryclassificationproblemandsummarizesaproxy
risklabelingmethodviapersonalityfrompreviousstudies;
2. A first-of-its-kind dataset for the above-mentioned task is synthesized and made available for research purposes upon
reasonablerequests;
3. A computational model based on the CNN architecture is trained and it shows significant improvement over strong
training-freebaselines.
The remainder of this article provides more details on the research objectives, the concept of financial risk tolerance, and its
relationtopersonalitytraits(Section2);Section3elaboratesonameta-analysisofrisktolerancecalculation,synthesisofdatasets,
and the model that predicts risk tolerance from text; Sections 4 and 5 present the experimental results; Section 6 analyzes and
discussestheexperimentalresults;Finally,futureworksofthisstudyarediscussedinSection7.
2. Literaturereview
2.1. Theconceptofrisktolerance
Previousstudieshavediscussedmultiplerisktolerance-relatedconcepts,includingriskattitude,riskaversion,riskpreference,
riskappetite,riskcapacity,etc.AbriefexhibitionofsuchconceptsisprovidedinGrable(2018).Duetothenebulousnatureofthose
concepts,therearenowidelyagreedprecisedefinitionsyet.However,ItrytodistinguishthemprimarilybasedonGrable(2018)
tocreateclarityforterminologiesusedinthisarticle:theconstructionisillustratedinFig.1.
Theoverallriskprofileisusedastheumbrellatermthatconsidersboththeinvestor’spsychologicalstateandotherobjective
factors,suchashis/herprincipalamount,income,lifecycle,andmanymore.Despitethecomplexityandinterdependencebetween
the subjective and objective factors as reported by Piovesan and Willadsen (2021) and Prinz et al. (2014), risk tolerance is used
tosummarizetheeffectofsubjectivefactors.Theobjectivefactors,ontheotherhand,determineriskcapacity,whichevaluatesan
individual’sfinancialabilitytowithstandfinanciallosses.Riskaversionistreatedastheantonymofrisktolerance.Itistheorized
thatrisktoleranceisfurtherinfluencedbyothercontextualcognitivebiases,andfinallyformstheriskperception.Riskperception
andriskcapacitytogethercontributetoriskpreference,whichisrepresentedineconomicanalysisasautilityfunctionandrefers
to the general feeling that one choice is better than another. This risk preference explains the risk-taking behavior of a rational
agent.IntheconstructionofFig.1,itisclearthataninvestor’shighriskpreferencedoesnotnecessarilymeanthattheinvestor’s
risktoleranceishigh,butmayalsobeattributedtoalowriskcapacityorothercognitivebiases.
The review by Hertwig et al. (2019) concluded that what is called risk tolerance here was a moderately stable psychological
traitwithbothgeneralanddomain-specificcomponentswhenmeasuredthroughself-reportsbutnotbehavioraltests.Sahm(2012)
pointedtotherelativelystableriskpreferenceaccordingtoapanelof12,003individualsoveradecade.Morepreviousstudiesshow
that risk tolerance was a stable personality trait and was unlikely to change substantially over life (Van de Venter et al., 2012),
whichsupportedthetheoryofNicolettaMarinelliandPalmucci(2017)thatrisktolerancewasagenetic,predispositional,andstable
personalitytrait.Tosummarize,itisreasonabletomodelandpredictrisktoleranceatanindividuallevelsinceitdoesnotchange
drasticallyovertime.
2.2. Risktoleranceandpersonalitytraits
Thestudyonthecorrelationbetweenrisktoleranceandpersonalitytraitsrequiresawell-definedtheoryofpersonality.Cattell
(1943)pioneeredthecomputationalstudyofpersonalitybyfactoranalysisandclusteranalysis,leadingtotheidentificationofthe
16PF(personalityfactor)structure.Fiverepeatedfactorsinexperimentsofself-ratings,staffratings,andteammateratingswerelater
discoveredfromthe22variablesinCattell’swork.Inanotherresearch(Norman,1967),fourexpertsrefinedthesefactorsthrough
wordselectioncriteria,semanticanalysis,andclassification,givingrisetofivebroadpersonalitydimensions(McCrae&John,1992),
3

F.Xing InformationProcessingandManagement61(2024)103704
namedasExtroversion(EXT),Neuroticism(NEU),Agreeableness(AGR),Conscientiousness(CON)andOpenness(OPN).Thistheory
is known as the Big Five personality traits today and remains popular in human–computer interactions and computational social
sciencestudies,e.g.,LeeandWu(2022).Subsequentresearchhasemployedvocabularyandquestionnairemethodstovalidatethe
structureofthesedimensions.
Using the construction of Big Five traits, Epstein and Garfield (1992) classified investors into different personality types
and concluded that only when users invest in stocks that are consistent with their personality types can they receive income.
Later, Lauriola and Levin (2001) showed that personality traits can predict preferences for gains and losses. People with high
openness scores can tolerate higher risks, while investors with high neuroticism scores are more inclined to avoid risk. Durand
et al. (2008) examined relationships between Big Five personality traits and investment decisions according to portfolios of 21
Australian investors, which showed that individuals who had more openness were more able to withstand investment portfolios
withhighrisk.Leeetal.(2010)foundthatindividualswithhighagreeableness,highintelligencescores,andlowrigorousscores
can accept more losses. A 2014 survey (Prinz et al., 2014) showed that agreeableness and openness modestly affected students’
financialdecision-making.OzerandMutlu(2019)foundthatconscientiousness,agreeableness,andopennesshavesignificanteffects
onfinancialbehavior.Mostrecently,Exleyetal.(2021)andRodriguesandGopalakrishna(2023)reportedthatthesignificanceof
differentpersonalitytraitsmaybeunstableanddifferentacrossgenerations:theuncontrolleddemographicfeatureofsamplesmay
beareasonfordiscrepanciesinresearchfindings.GambettiandGiusberti(2019)discoveredthatanxiousindividualswerelikelyto
savemoneyandavoidinvestments,perceivinghighriskswithlowcontrolandreturns,whilepeoplewithhighextroversion,self-
control, and independence would make more investments. Lai (2019) concluded that perceived behavioral control of individuals
regardingstockinvestmentisinfluencedbypersonalitytraitsofagreeableness,extraversion,conscientiousness,andopenness.
Personality has also been associated with more complicated behavioral finance variables other than risk tolerance, such
as investor prejudices, sentiment, overconfidence, and herding. A review article reported that conscientiousness had a positive
relationshipwithoverconfidence.Baddeleyetal.(2010)conductedasimulatedtaskforafunctionalmagneticresonanceimaging
(f-MRI)analysisandrevealedthatherdingtendencieswerenegativelyrelatedtosociability(includingextraversionandempathy),
whilepositivelyrelatedtorisk-taking(includingimpulsivityandventuresomeness).
Based on the abundant empirical evidence elaborated above, I hypothesize that personality information is closely related to
risk tolerance. If personality information can be detected from texts, the same source may also contain important clues for the
individual’srisktolerance.
2.3. Personalitydetectionfromtext
Unlikethefinancialrisktoleranceprofilingtask,personalitydetectionfromtextisawell-studiedarea.Manymachinelearning
models,includingSupportVectorMachine(SVM)andNaiveBayesclassifier,areappliedtouselinguisticfeaturesforpersonality
detection, such as the Mairesse feature (Mairesse et al., 2007), Medical Research Council (MRC) dictionary (Wilson, 1988), and
Linguistic Inquiry and Word Count (LIWC) (Tausczik & Pennebaker, 2010). Deep learning models that have been described for
personality detection are mainly variants of CNNs and RNNs (recurrent neural networks, e.g., bidirectional LSTM and GRU) or a
combinationofthem.Forinstance,Majumderetal.(2017)appliedCNNtoprocesstextualfeatures.Sunetal.(2018)proposeda
model that combined LSTM and CNN, and tried to capture the number of sentence vectors that were closely connected in some
coordinates.Theyalsoconcludedthatpersonswiththesametraitswerelikelytoexpresssentimentsinsimilarways.Rahmanetal.
(2019) compared several activation functions including 𝑠𝑖𝑔𝑚𝑜𝑖𝑑(⋅), 𝑡𝑎𝑛ℎ(⋅) and leaky 𝑅𝑒𝐿𝑈(⋅) for personality detection from text,
andfoundthattheoverallperformanceusing𝑡𝑎𝑛ℎ(⋅)wasbetterthantheothertwoactivationfunctions.Renetal.(2021)employed
text sentiment analysis and BERT to generate sentence-level embedding: this technique improved detection performance on both
the Myers–Briggs Type Indicator (MBTI) labeled and Big Five labeled datasets. Yang et al. (2023) designed a CNN-LSTM with a
word-layer-personhierarchicalattentionnetwork(wlpHAN)andafine-tuningmoduleforpersonalitydetection.Ablationanalysis
suggestedthatthecorrectattentionmechanism,dataaugmentation,andfine-tuningareusefulforthistask.
BasedonthewideacceptanceofCNNasaneffectivetextfeatureextractorandclassifierespeciallyforshortandsocialmedia
texts (Kim, 2014), the risk tolerance profiling model in this article uses the CNN architecture in a similar manner as described
inMajumderetal.(2017).
3. Methodology
3.1. Derivingrisktolerancelabelsfrompersonalitytraits
Onemajorchallengeintheproposedriskprofilingtaskisthelackofhigh-qualityandalignedrisktolerancelabels.Inthisstudy,
ameta-analysisisconductedtosummarizealinearregressionmodelfromtheliteraturetoinferrisktolerancelevelsbasedonthe
BigFivemodel.
ThreestudiesbyPakandMahmood(2015),Pinjisakikool(2018),andWongandCarducci(2013)arecomparedbecausethey
all used linear regression methods to establish the relation between risk tolerance and personality scores, though different scales
wereusedintheoriginalquestionnaires.Inordertoagglomeratetheresultsfromdifferentstudies,Ifirsttransformdifferentscales
into a 5-point scale system. Subsequently, these risk tolerance levels will be used as the supervision and ground truth for model
evaluation.
4

F.Xing InformationProcessingandManagement61(2024)103704
When the dependent variable and the independent variable in the regression equations have a linear relation, the dependent
variableandtheindependentvariablecanberespectivelynormalized.Ifweset𝑋 asafunctionoftheindependentvariable𝑥and
its scale in the original questionnaire, and let the minimum value and maximum value of the original scale be 𝑎 and 𝑏, then the
normalizationis:
𝑥−𝑎
| 𝑋=  | .   |     |     |     |     | (1) |
| --- | --- | --- | --- | --- | --- | --- |
𝑏−𝑎
Set𝑌 asthenewdependentvariablewhosedesiredminimumvalueinthenewscalesystemis𝐴andthemaximumvalueis𝐵,then,
| 𝑌 =(𝐵−𝐴)×𝑋+𝐴. |     |     |     |     |     | (2) |
| ------------- | --- | --- | --- | --- | --- | --- |
Substitutingformula(1)informula(2),thetransformationbecomes:
𝑥−𝑎
| 𝑌 =(𝐵−𝐴)× | +𝐴. |     |     |     |     | (3) |
| --------- | --- | --- | --- | --- | --- | --- |
𝑏−𝑎
InPinjisakikool(2018),theregressionequationis:
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 7 =2.936 | +0.125𝐸𝑋𝑇 | 5 +0.121𝑂𝑃𝑁 |     | 5         |     | (4) |
| ----------------- | --------- | ----------- | --- | --------- | --- | --- |
|                   | −0.176𝐴𝐺𝑅 | −0.096𝐶𝑂𝑁   |     | −0.112𝑁𝐸𝑈 | ,   |     |
|                   |           | 5           |     | 5         | 5   |     |
wherethepersonalityscaleisa5-pointscale,andtherisktoleranceisa7-pointscale.Therefore,risktoleranceneedstobere-scaled
to5-pointusingformula(3)asfollows:
|                       |                            | 7−1 | 3        |     | 1   |     |
| --------------------- | -------------------------- | --- | -------- | --- | --- | --- |
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 7 =(𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 | 5 −1)×                     | +1= | 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 | 5 − | .   | (5) |
|                       |                            | 5−1 | 2        |     | 2   |     |
| Substitute𝑟𝑖𝑠𝑘_𝑡𝑜𝑙    | withformula(5),wewillhave: |     |          |     |     |     |
7
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 5 =2.29 | +0.083𝐸𝑋𝑇  | 5 +0.08𝑂𝑃𝑁   | 5   |              |     |     |
| ---------------- | ---------- | ------------ | --- | ------------ | --- | --- |
|                  | − 0.117𝐴𝐺𝑅 | 5 − 0.064𝐶𝑂𝑁 |     | 5 − 0.075𝑁𝐸𝑈 | 5 . | (6) |
Similarly,bothpersonalityandrisktoleranceintheresearchofPakandMahmood(2015)are6-pointscales,andtheregression
equationisasfollows:
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 =4.037 | − 0.187𝐴𝐺𝑅 | + 0.317𝑂𝑃𝑁 |     | .   |     | (7) |
| --------------- | ---------- | ---------- | --- | --- | --- | --- |
| 6               |            | 6          |     | 6   |     |     |
Bytransformingtheindependentvariablesandthedependentvariableintothe5-pointscalerespectively,amodelalignedwiththe
onefromPinjisakikool(2018)isobtainedasbelow.
| 1.25𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 | − 0.25=4.037−0.187×(1.25𝐴𝐺𝑅 |                 |     | −   | 0.25)    | (8) |
| ------------ | --------------------------- | --------------- | --- | --- | -------- | --- |
|              | 5                           |                 |     | 5   |          |     |
|              |                             | +0.317×(1.25𝑂𝑃𝑁 |     | 5   | − 0.25). |     |
Thiscanbefurthersimplifiedas:
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 5 =4.2545 | −   | 0.187𝐴𝐺𝑅 5 + | 0.317𝑂𝑃𝑁 | 5 . |     | (9) |
| ------------------ | --- | ------------ | -------- | --- | --- | --- |
Similarly,bothpersonalityandrisktoleranceintheresearchofWongandCarducci(2013)are9-pointscales,andtheregression
equationisasfollows:
𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 =4.44 + 0.02𝐸𝑋𝑇 + 0.18𝑂𝑃𝑁 − 0.13𝐴𝐺𝑅 − 0.15𝐶𝑂𝑁 . (10)
| 9   |     | 9   | 9   |     | 9 9 |     |
| --- | --- | --- | --- | --- | --- | --- |
Bytransformingtheindependentvariablesandthedependentvariableinto5-pointscales,wecanget:
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 =2.67 | + 0.2𝐸𝑋𝑇 | + 0.18𝑂𝑃𝑁 | −   | 0.13𝐴𝐺𝑅 | − 0.15𝐶𝑂𝑁 . | (11) |
| -------------- | -------- | --------- | --- | ------- | ----------- | ---- |
| 5              |          | 5         | 5   |         | 5 5         |      |
Bysummarizingtheregressiveresultsfromthethreestudies,thatare,formula(6)(9)and(11),wewillhave:
| 𝑟𝑖𝑠𝑘_𝑡𝑜𝑙 =3.0715 | +   | 0.094𝐸𝑋𝑇 +   | 0.192𝑂𝑃𝑁 |     |              | (12) |
| ---------------- | --- | ------------ | -------- | --- | ------------ | ---- |
| 5                |     | 5            |          | 5   |              |      |
|                  | −   | 0.145𝐴𝐺𝑅 5 − | 0.071𝐶𝑂𝑁 | 5 − | 0.025𝑁𝐸𝑈 5 . |      |
Formula (12) suggests that Openness and Agreeableness (coef. > 0.1) are the two most prominent personality traits that
influencetheindividual’srisktolerancelevel.ThisinterpretationisalsoconsistentamongthestudiesbyPakandMahmood(2015),
Pinjisakikool (2018), and Wong and Carducci (2013). The corresponding 5-point average and median risk tolerance scores in
different studies are subsequently transformed and presented as in Table 1, showing the heterogeneous populations these studies
are conducted on. It can be observed that the research of Pinjisakikool (2018) pooled a conservative population (claimed to be
representativeoftheDutchpopulation),whereastheresearchofPakandMahmood(2015)accessedahigherrisktolerancegroup
(potentialprivateinvestorsinapost-Soviettransitioncountry,i.e.,Kazakhstan).
5

| F.Xing |     |     |     |     | InformationProcessingandManagement61(2024)103704 |     |     |     |
| ------ | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
Table1
Descriptivestatisticsofreportedrisktolerancescoresaftertransformation.
|     |                       |     | Mean  |     | Median | Min | Max |     |
| --- | --------------------- | --- | ----- | --- | ------ | --- | --- | --- |
|     | Pinjisakikool(2018)   |     | 1.9   |     | 1.89   | –   | –   |     |
|     | PakandMahmood(2015)   |     | 3.736 |     | 3.896  | –   | –   |     |
|     | WongandCarducci(2013) |     | 2.75  |     | –      | –   | –   |     |
Table2
Descriptivestatisticsofinferredrisktolerancescoresonpersonalitydatasets.
| risk_tol/dataset |     | Source |     | #users | Mean | Median | Min | Max |
| ---------------- | --- | ------ | --- | ------ | ---- | ------ | --- | --- |
MyPersonality(Markovikjetal.,2021) Facebook 250 3.34 3.36 2.74 3.69
Essay(Pennebaker&King,1999) Students 2479 3.18 3.18 2.53 3.84
| PAN15(Pardoetal.,2015) |     | Twitter |     | 334 | 3.32 | 3.29 | 2.93 | 3.62 |
| ---------------------- | --- | ------- | --- | --- | ---- | ---- | ---- | ---- |
Table3
Distributionofrisktolerancelevelsamongsurveyedpopulation.
|     | risk_tol             |     | Ourtargetedpercentage |     |     | Actualnumberofusers |     |     |
| --- | -------------------- | --- | --------------------- | --- | --- | ------------------- | --- | --- |
|     | gambler              |     | 10                    |     |     | 273                 |     |     |
|     | willingafterresearch |     | 40                    |     |     | 1067                |     |     |
|     | cautious             |     | 40                    |     |     | 887                 |     |     |
|     | riskavoider          |     | 10                    |     |     | 240                 |     |     |
Table4
Datasamplesfromthesynthesizedcorpus.
|     | UserID | Text |     |     |     |     | BigFivelabels |     |
| --- | ------ | ---- | --- | --- | --- | --- | ------------- | --- |
‘‘thisismyfirstwritingassignmentofcollege’’
‘‘itdoesnotseemlikeitcouldbesobad’’
|     | 02002056707 |     |     |     |     |     | ynynn |     |
| --- | ----------- | --- | --- | --- | --- | --- | ----- | --- |
‘‘infact,collegeitselfisnotsobadyet’’
......
‘‘foundoutthatJollyPirateDonutsnearherhouseAwesome’’
‘‘isfeelingalittlesubbydubtoday’’
|     | 64e929be3ff0 | ‘‘hasanewbabysisterLittleBabyNoName’’ |     |     |     |     | nyyny |     |
| --- | ------------ | ------------------------------------- | --- | --- | --- | --- | ----- | --- |
......
|     | ...... | ...... |     |     |     |     | ...... |     |
| --- | ------ | ------ | --- | --- | --- | --- | ------ | --- |
3.2. Synthesizingarisktolerancecorpus
Becausethemajorchallengeofthisstudywasthelackofrisklabelsfortexts,anessentialrequirementisforthetextualdatato
havelabeledfeaturesthathasbeenestablishedtoassociatewithrisktolerance.Grable(2016)listed11highlyrelevantfactors(p.25,
Table2.1),wherepersonalityinformationismoreoftencollectedthanotherdemographicinformationinNLPresearch.Therefore,
threerepresentativedatasetsforpersonalityresearch,i.e.,MyPersonality(Markovikjetal.,2021),Essay(Pennebaker&King,1999),
andPAN-15(Pardoetal.,2015)areusedtosynthesizeacorpusforriskprofiling.Atthedatapre-processingstep,Iconvertedall
letterstolowercaselettersandremovedallnon-ASCIIcharacters.ForTwitter(X)data,Ireplacedhashtagswiththeplaintextof
thetags,andremoved@tagsandURLs.Longsentencesaredividedintoseveralshortsentences,andthelastshortsentencemay
beshorterthanthemaxlengthandpadded.Intheexperiments,themaxlengthissetto20words.
The fields left in this combined dataset include user ID, content, and Big Five personality. Among them, the PAN-15 dataset
includes the Twitter content of 334 Twitter users (152 in English). The texts published by the same user are first combined into
onepieceoflongtext,andinthesubsequentdatapre-processingstepagaindividedaccordingtotheirlength.Thevalueofusers’
Big Five personality in the PAN-15 dataset is from [−0.5, 0.5], where the value is proportionally mapped to [0, 5] in order to
calculate the risk tolerance of each user. The value range of Big Five personality for the MyPersonality dataset is already [0,5].
The personality traits of the dataset Essays have only binary values ‘y’ and ‘n’, which are mapped to 3.75 and 1.25 respectively,
tofitintotheintervalof[0,5].Then,theuser’srisktolerancescoresarecalculatedaccordingtoformula(12).Theresults,shown
in Table 2, illustrate the high distributional consistency among all three component datasets. The last dataset preparation step is
tocategorizecontinuousrisktolerancescores.Toachievethis,Irefertosurveyresultsofdemographicdistributionsfromprevious
research (Kim et al., 2021), and rank and divide the user’s risk tolerance scores proportionally (see Table 3). The dataset size is
consideredappropriatewhenreferredtootherpsychometricresearch,e.g.,Manolika(2023)andZhuetal.(2022).Datasamples
fromthiscorpusareexhibitedinTable4.
6

F.Xing InformationProcessingandManagement61(2024)103704
Fig.2. ACNNmodelfortext-basedfinancialrisktoleranceprofiling.
3.3. Modelarchitectureandimplementationdetails
A CNN model is built based on the architecture described by Majumder et al. (2017) and several useful model features are
experimented with to test for their effectiveness. Fig. 2 illustrates the model architecture. In detail, the following features may
improvethemodelperformanceaccordingtotheliterature:
1. Richnessofrepresentations:Usingmultipletextrepresentationsisakeyfactorthatinfluencesthemodelperformance.Recent
studies, e.g., Yang et al. (2023) have shown that psychologically inspired lexicons and middle layers from large language
models provide additional useful information to the network input. The network input in Fig. 2 is a concatenation from
sentenceembeddings,includingWord2Vec(Mikolovetal.,2013),Glove(Penningtonetal.,2014),andBERT(Devlinetal.,
2019),topreservesemanticinformationasmuchaspossible.
2. Textaugmentation:Thisisoftenusefulwhenthemodeltrainingphaseunderfitsoroverfitsbecauseoflimiteddatasize.Yang
etal.(2023)reportedSPDFiT(Self-TaughtPersonalityDetectionFine-Tuning),whichusesBayesianlearningtoassignpossible
pseudolabelsfornewtexts.Inthisstudy,thetextaugmentPythonlibrary2 isusedtosubstitutewordsandcreatesemantic
equivalentsofexistingtexts.SynonymoussubstitutionisacommonmethodinNLP,whichincreasestheamountofdatain
thedataset.Themethodisdedicatedtoprovidingmoretrainingdata,thusimprovingtheclassificationeffectofshorttexts
throughglobalaugmentationmethods.
3. Multi-tasklearning:Previousstudiesdocumentedthatpersonalitydetectionmaybelearnedwithcloselyrelatedtasks,such
as internet use behaviors (Mark & Ganzach, 2014) and emotion detection (Li et al., 2022). The multi-task fashion is thus
2 https://github.com/dsfsi/textaugment
7

F.Xing InformationProcessingandManagement61(2024)103704
experimented,i.e.,combinesthe5personalitytraitsandrisktoleranceasoutputsforthesamenetwork,sothatparameters
canbesharedbetweenthetwotasks.Crossentropylossfunctionisused,wherepersonalitytraitsremainin2categories(‘y’
and‘n’),andrisktolerancewasdividedinto4categories.
For the BERT embeddings, ‘‘bert-base-uncased’’3 with 10% dropout is used. Each contributing representation has an output
dimensionof100afterbatchnormalization.ThesetogetherwiththeMairessefeaturesformafinalin-featuresizeof3×100+84
=384forthefullyconnectedlayer(seeFig.2).Therepresentationsarenotfrozenandwillalsobetrained.Modelparametersare
empiricallyset:trainingbatchsize=16,andmaximumepoch=4.AstandardAdamoptimizer(learningrate=0.001andweight
decay=0)fromthePyTorchpackageisused.
3.4. Linguisticfeatures
ThisstudyuseslinguisticfeaturesfromMairesseetal.(2007)andappliestheauthor’soriginalJavaprogramtoextractfeatures.
Inparticular,thefeaturesetincludessomefeaturesoftheMedicalResearchCouncil(MRC)PsycholinguisticDatabaseandLinguistic
Inquiry and Word Count (LIWC). The MRC machine-usable dictionary contains both linguistic and psycholinguistic attributes for
150,837 words (Wilson, 1988). The LIWC dictionary (Tausczik & Pennebaker, 2010) contained attributes that reflect different
emotions,thinkingstyles,socialconcerns,andevenpartsofspeech.TheMRCdatabaseofOxfordTextArchive(Wilson,1988)is
usedforcalculatinglinguisticfeatures.Finally,atotalof84featureswereextracted,including70featuresofLIWCand14features
ofMRC.
Forthesakeofcoverage,threemodels,i.e.,Word2Vec,Glove,andBERT,areusedtoproducesentenceembeddings.Word2Vec
wasdevelopedbysimplytraininganeuralnetworkforthenextwordpredictiontask(Mikolovetal.,2013),whichaimedtoobtain
avectorizedrepresentationofthewordthroughthecontextoftheword.Glove(Penningtonetal.,2014)appliedaco-occurrence
matrix,andconsideredbothlocalandglobalinformation.Thisstudyusedpre-trainedWord2VecandGlovevectors.Bidirectional
EncoderRepresentationsfromTransformers(BERT)isalargermodelofpre-traininglanguagerepresentationsdevelopedbyGoogle.
UnlikethefixedwordrepresentationsforWord2VecandGlove,BERTrepresentationsareatthesentencelevelandjointlyproduced
from a neural network. BERT (Devlin et al., 2019) included pre-training and fine-tuning on various specific tasks. BERT was
unsupervisedandcoulduseonlyplaintextcorpusfortraining.
In this research, out-of-vocabulary words are counted for their frequencies of occurrence. If the frequency is greater than or
equaltothethreshold(=1inourcase),aseparatewordvectorforthiswordwillbecreatedwiththerandomizedvaluesofeach
dimensionbetween[−0.25,0.25)tomatchthepre-trainedembeddings.Thedimensionsoftheword/sentencerepresentationsinthis
studyare300forWord2VecandGlove,and768forBERT.
4. Experiment
To make better use of our size-limited data for training, 10-fold cross-validation has been implemented. Cross-validation also
providesmoreinformationabouttheperformancemetricsstabilityoftheexperimentedmodelandenablesrobustnesstesting.Cross-
validationrandomlysamplesthecorpusinto10portions.Onlyoneportionisleftasthetestseteachtime,andtheremainingnine
portionsareusedasthetrainingset.Subsequently,performancemetricswerecalculatedoneachtestsetandaveragedtoobtainthe
finalresultasreportedinTable5.Besidedata,thevariancesintroducedbymodelsareminimal.Experimentsshowthatperformance
metricswillconvergewithdifferentinitializationmanualseeds.Thedispersioninformationisalsousedtoshowthesignificanceof
performancedifferencesinTable6.
Table5enablesablationanalysisfortheintroductionofeachnewfeatureaswellascomparisonstoseveraltraining-freebaseline
metricsreportedinthefirstthreerows.Strategicguessassumesthattherisktoleranceleveldistributioninformation(Table3)is
availableandgeneratesclassificationlabelsaccordingtothoseprobabilities.Therecentgenerativelanguagemodels4 GPT-3.5and
GPT-4arepromptedusingthebelowtemplatetoclassifytheusertextsintodifferentrisktolerancelevels.Whentheresponsedoes
notcontainaclassificationorrefusestoanswer,thestrategicguessresultsareused.Exceptforthoseill-answeredcases,theGPT
modelsarenotpromptedwithknowledgeoftheprobabilitydistribution.
completion=openai.ChatCompletion.create(
model="gpt-model-name",
messages=[
{"role":"system","content":"Youareafinancialadvisor,
skilledinunderstandingandjudgingthefinancialrisktolerancelevelofaclientthroughconversations.
Youwillratetheclient’srisktolerancelevelfrom0to3.
0meanslowtoleranceand3meanshightolerance."},
{"role":"user","content":"[examplecontent1]"},
{"role":"assistant","content":"1"},
{"role":"user","content":"Youaredoingagreatjob."},
{"role":"user","content":"Hereisanotherclient[examplecontent2]"} ]
)
3 https://huggingface.co/bert-base-uncased
4 https://platform.openai.com/docs/models
8

| F.Xing |     |     |     | InformationProcessingandManagement61(2024)103704 |     |     |
| ------ | --- | --- | --- | ------------------------------------------------ | --- | --- |
Table5
Experimentalresultswithdifferentmodelsettingsonthesynthesizedcorpus.
Modelsettings Macro-precision Macro-recall Macro-F1 Micro-precision Micro-recall Micro-F1
| Strategicguess     | 0.2500 | 0.2500 | 0.2500 | 0.3400 | 0.3400 | 0.3400 |
| ------------------ | ------ | ------ | ------ | ------ | ------ | ------ |
| gpt-3.5-turbo      | 0.2484 | 0.2424 | 0.2221 | 0.3489 | 0.3489 | 0.3489 |
| gpt-4-1106-preview | 0.2512 | 0.2506 | 0.2222 | 0.3587 | 0.2590 | 0.2842 |
| CNN(W)             | 0.2391 | 0.2896 | 0.2538 | 0.4711 | 0.4711 | 0.4711 |
| CNN-aug(W)         | 0.2367 | 0.2854 | 0.2540 | 0.4750 | 0.4750 | 0.4750 |
| CNN(G)             | 0.2445 | 0.2996 | 0.2621 | 0.4938 | 0.4938 | 0.4938 |
| CNN-MT(G)          | 0.2416 | 0.3035 | 0.2690 | 0.4830 | 0.4830 | 0.4830 |
| CNN-MT(W+G+B)      | 0.2569 | 0.3086 | 0.2774 | 0.5066 | 0.5066 | 0.5066 |
Table6
Descriptivestatisticsandrobustnesstestresults(micro-F1).
|                       |     | Strategicguess | CNN(W)         |     | CNN-MT(W+G+B) |     |
| --------------------- | --- | -------------- | -------------- | --- | ------------- | --- |
| Samplemean            |     | 0.3244         | 0.4711         |     | 0.5066        |     |
| Standarddeviation     |     | 0.0351         | 0.0094         |     | 0.0179        |     |
| Samplesize            |     | 3              | 10             |     | 10            |     |
|                       |     |                | Welch’st-value |     | p-value       |     |
| Strategicguess/CNN(W) |     |                | 7.1624         |     | 0.0095***     |     |
| CNN(W)/CNN-MT(W+G+B)  |     |                | 5.5525         |     | 0.0001***     |     |
5. Resultsandrobustnesstests
TheexperimentalresultsinTable5showthattrainingorfine-tuningisveryimportanttotherisktoleranceprofilingtask.Itis
importanttonotethattheCNN-basedresultsin Table5areusingafixedmanualseed(seed=0)forgeneratingrandomnumbers,
thereforedonotreflecttheuniversalorthebestperformances.AlthoughGPTisbelievedtobeamodelofbasicreasoningcapability
and commonsense knowledge, it does not significantly outperform the strategic guess. This may indicate that a large amount of
useful(risk-related)textualfeaturesarenotcoveredinthoselargelanguagemodelsyet.Byusingsimpletraining,i.e.,exposingthe
predictivemodeltotextualfeatures,theCNN(W)modelalreadyshowssignificantimprovementfromzero-shotlearningwithout
textinformationintermsofthemicro-F1metric(Table6).CNN(W)isthemodeldescribedbyMajumderetal.(2017):itusedjust
theWord2Vecembeddingsandchangedthetargetoutputfrompersonalitytraitstotherisktolerancelevel.TheCNN-MT(W+G+B)
modelisanimprovedversionwithmulti-taskingandrichtextualembeddinginputs.Bytestingwhethertheaverageperformance
metricsaresignificantlydifferentwithtwounknownunequalstandarddeviationsamples(Zimmerman,2012),Table6showsthat,
even based on the small sample sizes, leveraging the textual features and constructing an appropriate architecture are useful for
thisnewtask.
6. Discussionandimplications
In this section, the implications of the experimental results are further discussed. In terms of large language models, it is
interestingtoobservethatGPT-4isnotmuchsuperiortoGPT-3.5andoptimizesprecisionoverrecall.Acloserinvestigationreveals
that GPT-4 refrains from answering more often, probably due to safety tuning, so the metrics are inclined to those of strategic
guess.WhencomparingCNN-basedmodels,thereareobservableimprovementswhenusingricherembeddings:theadditionalGlove
representation improves CNN by over 0.02, and the additional Glove and BERT representations improve CNN-MT by over 0.02
in terms of micro-F1 scores. The expansion of embeddings seems a major source of model improvement other than training or
fine-tuning.Apossiblereasonisthatrisktolerance(thetargetinthetask)informationlargelyresidesinthelanguagecontext.
TextaugmentationisexperimentedontheCNN(W)model.MarivateandSefara(2020)studiedtheeffectofdifferentapproaches
totextaugmentation,andfoundthataugmentationreducedthepossibilityofover-fitting.Afterperformingsynonymreplacement
ofthetrainingset,thenumberofrecordsinthenewdatasetwastwicethatoftheoriginaldataset.Thenumberofrecordsinthe
testsetremainedunchanged.Theresultsshowedthattextaugmentation,again,onlyhasminimaleffectonthemodelperformance
metrics.Therefore,thisfeatureisabandonedfromthefinalCNN-MT(W+G+B)model.Infact,combiningdifferentsourcesofdata,
instead of text augmentation, seems to be more effective. This is evidenced by comparing with model settings where only the
Essays(Pennebaker&King,1999)dataisused.
Acommonbeliefisthatmulti-taskingimprovescloselyrelatedtasks.Forinstance,Lietal.(2022)designedamulti-taskmodel
frameworktopredictpersonalitytraitsandemotionalbehaviorssimultaneously,whichperformedbetterthanasingleCNNmodel,
especiallyinthemeasurementofrecall.Theexperimentalresultshere,however,showthatmulti-taskingwithpersonalityisnotso
effective, especially in the case of financial risk profiling. CNN-MT (G) only achieves a comparable macro-F1 to CNN (G) and its
micro-F1isevenslightlylower(0.4830<0.4938).Theseresultsindicatethatthenewtaskdoesnottendtooverfittothedata,and
isnotcomplimentarytothepersonalitydetectiontask.
Basedontheabovediscussionsoncomparingdifferentmodelvariants,thefinalmodelissetasusingalltheWord2Vec,Glove,
andBERTrepresentations,predictingpersonalitytraitsandrisktolerancetypestogetherbasedonthesynthesizeddataset.Thisfinal
9

F.Xing InformationProcessingandManagement61(2024)103704
modelachievesthebestresultsacrossallthemetrics,includingaccuracy,precision,recall,andF1score.Itisobservedthatimproving
micro-metricsiseasier.Thisisbecausetherisktoleranceclassesareskewed:accuratelypredictingthe‘‘gambler’’and‘‘riskavoider’’
typesisdifficult.Themacro-metricsaresignificantlyaffectedbyaveragingwiththelowprecisionandrecallcomponents.Itisalso
observedthattheimprovementinmicro-metricsismorebalanced,whereasmacro-precisionremainssimilaracrossthemodelsin
Table5:theimprovementinmacro-metricsmainlycomesfromthehigherrecalls.
Thisstudyhastwoimportanttheoreticalimplicationsfortheinformationscienceandinformationmanagementfield.First,itadds
knowledgetotherecenthypethatlargelanguagemodelsaregoodateveryprofessionaltask.Theexperimentalresultsshowthat
GPT models’ performance is only comparable to a strategic guess for financial risk profiling. Indeed, in many cases the outputs
are‘‘Basedontheprovidedtext,itisdifficulttoassessyourrisktolerancelevel.Couldyoupleasesharemoreinformationabout
your financial goals, investment preferences, and attitude towards financial risks?’’ or ‘‘You seem to have a mix of cautiousness
anddetermination,whichsuggestsamoderaterisktolerance’’.TheoutputsdonotusetheBigFivepersonalitycategoriesandonly
showasuperficialunderstandingofrisktolerancerelatedconcepts.Thestudyindicatestrainingtobeimportantforthistask,which
echoestherecentfindingsthatdomainadaptation(Suzukietal.,2023)anddescriptiveprompting(Wenetal.,2023)areneeded
forfinancialanalysisandpersonalitydetection.Second,thestudyprovesusergeneratedtextstobeausefulinformationsourcefor
financialplanning(Heoetal.,2022).Withacarefullybuiltdeeplearningmodel,micro-F1canbesignificantlyimprovedfromstrong
baselines(circa0.34)tocirca0.50.Giventheunbalanceddatadistribution,thismeansthebinaryclassificationproblem(‘‘will-to-
take-risk’’and‘‘more-cautious’’)isbasicallysolved.However,itseemsmoredifficulttoidentifythemoreextremelyrisk-takingor
risk-averseinvestors.Thisindicatesthattheriskprofilingprocessasawholemaystillneedsomehumanintervention.
Thisstudyalsohaspracticalimplicationsforinformationsystemsresearchersandalgorithmengineers.Therisktoleranceprofiling
taskneedsknowledgeofappliedpsychology.Consequently,therichnessofembeddings(especiallyincludingLIWC,etc.)isaprimary
influence factor on the model performance. It is also empirically tested that other techniques from personality detection, such as
textaugmentationandmulti-tasklearning,arelesseffectivefortherisktoleranceprofilingtask.Themodelcanbeintegratedinto
theriskprofilingpractices,whicharerequiredforcustomerknowledgeassessment,investmentproductrecommendation,etc.The
modelresultmayreplaceaformalquestionnaireinlow-stakesituations,andbeusedasanassistivetooltoremindfinancialadvisors
whenthereisasignificantdiscrepancyintheriskprofilescreatedfrommultiplechannels(Xingetal.,2019a).
7. Conclusionandfutureworks
Inthisstudy,anewtaskoffinancialrisktoleranceprofilingfromthetextualdataproducedbyusersisdefined.ACNNmodel
similartothoseusedforpersonalitydetectionisdeveloped,andexperimentedwithseveralfeatures.ThefinalmodelusesWord2Vec,
Glove, and BERT representations, predicts personality traits together with risk tolerance, and combines training data synthesized
from three different sources. This model achieves a micro-F1 score of 0.5066 for the 4-category classification problem, which is
circa4%improvementfromthesimpleCNN(W)modelandsignificantlysuperiortostrongtraining-freebaselines.
The biggest limitation of this study is that the risk tolerance labels are derived through the synthesis of multiple datasets
createdforpersonalitydetectionstudiesandmeta-analyses.Itbecomesimplausibletocontacttheanonymouspatientsandsurvey
them for the risk tolerance ground truth or to further validate the labels. Nevertheless, several important findings are reported.
First,therelationbetweenpersonalitytraitsandrisktolerancelevelisbetterunderstoodquantitatively.Second,fine-tuningisthe
most important component of the financial risk profiling task, and richer psycho-linguistic features are more important than text
augmentationormulti-tasking.Third,ithasbeenprovedthatuser-generatedtexts(bothfromamorecontrolledlabenvironment
andonlinedigitalfootprints)areusefulinformationforrisktoleranceprofiling.
Futureworkswouldincludeinvestigationsonwhataretheusefulrisk-relatedtextualpatterns;explorationsonthepossibilityof
integratingnon-textualfeaturesfromotherriskprofilingtools,suchasdemographicdataandstructuredquestionnaires,intoCNN;
anddatacollectionthatalignspersonalitytraitsandrisktoleranceusingindividualidentifications.
CRediTauthorshipcontributionstatement
Frank Xing: Writing – review & editing, Writing – original draft, Software, Methodology, Investigation, Formal analysis,
Conceptualization.
Dataavailability
Datawillbemadeavailableonrequest.
AI-assistedtechnologiesinthewritingprocess
Duringthepreparationofthisworktheauthor(s)usedChatGPTinordertoimprovethereadabilityofcertainsentences.After
using this tool, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the
publication.
Acknowledgment
TheauthorwouldliketothankXiuyuChenforhelpingwithdatacollationandsoftwaredevelopment.
10

F.Xing InformationProcessingandManagement61(2024)103704
References
Ainia,N.S.N.,&Lutfi,L.(2019).Theinfluenceofriskperception,risktolerance,overconfidence,andlossaversiontowardsinvestmentdecisionmaking.Journal
ofEconomics,Business,&AccountancyVentura,21(3),401–413.
Athota,V.S.,Pereira,V.,Hasan,Z.,Vaz,D.,Laker,B.,&Reppas,D.(2023).Overcomingfinancialplanners’cognitivebiasesthroughdigitalization:Aqualitative
study.JournalofBusinessResearch,154,Article113291.
Baddeley,M.,Burke,C.,Schultz,W.,&Tobler,T.(2010).Impactsofpersonalityonherdinginfinancialdecision-making.CambridgeWorkingPapersinEconomics,
1006,1–36.
Cattell,R.B.(1943).Thedescriptionofpersonality:basictraitsresolvedintoclusters.JournalofAbnormalandSocialPsychology,38(4),476–506.
Devlin,J.,Chang,M.-W.,Lee,K.,&Toutanova,K.(2019).BERT:Pre-trainingofdeepbidirectionaltransformersforlanguageunderstanding.InProceedingsof
NAACL-HLT(pp.4171–4186).
Durand,R.B.,Newby,R.,&Sanghani,J.(2008).Anintimateportraitoftheindividualinvestor.JournalofBehavioralFinance,8(3),193–208.
Epstein,I.,&Garfield,D.(1992).Thepsychologyofsmartinvesting:Meetingthe6mentalchallenges.JohnWiley&Sons,ISBN:978-0-471-55071-6.
Exley,J.,Doyle,P.,Snell,M.,&Campbell,W.K.(2021).OCEAN:Howdoespersonalitypredictfinancialsuccess?JournalofFinancialPlanning,34(10),68–86.
Gambetti,E.,&Giusberti,F.(2019).Personality,decision-makingstylesandinvestments.JournalofBehavioralandExperimentalEconomics,80,14–24.
Grable,J.E.(2016).Financialrisktolerance.InHandbookofconsumerfinanceresearch(pp.19–31).Springer,ISBN:9783319288871.
Grable,J.E.(2018).Financialrisktolerance:Apsychometricreview.CFAInstituteResearchFoundation,ISBN:978-1-944-96020-9.
Hemrajani,P.,Rajni,Khan,M.,&Dhiman,R.(2023).Financialrisktolerance:Areviewandresearchagenda.EuropeanManagementJournal,41(6),1119–1133.
Heo, W., Kwak, E. J., & Grable, J. E. (2022). The role of big data research methodologies in describing investor risk attitudes and predicting stock market
performance.InHandbookofresearchonnewchallengesandglobaloutlooksinfinancialriskmanagement(pp.293–315).IGIGlobal.
Hertwig,R.,Wulff,D.U.,&Mata,R.(2019).Threegapsandwhattheymaymeanforriskpreference.PhilosophicalTransactionsoftheRoyalSocietyB,374(1766),
Article20180140.
Kim,Y.(2014).Convolutionalneuralnetworksforsentenceclassification.InProceedingsofEMNLP(pp.1746–1751).
Kim,K.,Hanna,S.D.,&Ying,D.(2021).Therisktolerancemeasureinthe2016surveyofconsumerfinances:New,butisitimproved?JournalofFinancial
CounselingandPlanning,32(1),86–103.
Lai,C.-P.(2019).Personalitytraitsandstockinvestmentofindividuals.Sustainability,11(19),5474.
Lauriola,M.,&Levin,I.P.(2001).Personalitytraitsandriskydecision-makinginacontrolledexperimentaltask:Anexploratorystudy.PersonalityandIndividual
Differences,31(2),215–226.
Lee,K.,Kraeussl,R.,&Paas,L.(2010).Personalityandinvestment:Personalitydifferencesaffectinvestors’adaptationtolosses:Technicalreport7,(pp.1–19).Faculteit
derEconomischeWetenschappenenBedrijfskunde.
Lee,P.-J.,&Wu,T.-Y.(2022).Miningrelationsbetweenpersonalitytraitsandlearningstyles.InformationProcessing&Management,59(5),Article103045.
Lengkeek,M.,Finn,v.d.K.,&Frasincar,F.(2023).Leveraginghierarchicallanguagemodelsforaspect-basedsentimentanalysisonfinancialdata.Information
Processing&Management,60(5),Article103435.
Li,Y.,Kazemeini,A.,Mehta,Y.,&Cambria,E.(2022).Multitasklearningforemotionandpersonalitytraitsdetection.Neurocomputing,493,340–350.
Mairesse,F.,Walker,M.A.,Mehl,M.R.,&Moore,R.K.(2007).Usinglinguisticcuesfortheautomaticrecognitionofpersonalityinconversationandtext.
JournalofArtificialIntelligenceResearch,30,457–500.
Majumder, N., Poria, S., Gelbukh, A. F., & Cambria, E. (2017). Deep learning-based document modeling for personality detection from text. IEEE Intelligent
Systems,32(2),74–79.
Manolika,M.(2023).Thebigfiveandbeyond:Whichpersonalitytraitsdopredictmovieandreadingpreferences?PsychologyofPopularMedia,12(2),197–206.
Marivate,V.,&Sefara,T.(2020).Improvingshorttextclassificationthroughglobalaugmentationmethods.InLecturenotesincomputerscience,(pp.385–399).
Mark,G.,&Ganzach,Y.(2014).Personalityandinternetusage:Alarge-scalerepresentativestudyofyoungadults.ComputersinHumanBehavior,36,274–281.
Markovikj,D.,Gievska,S.,Kosinski,M.,&Stillwell,D.(2021).Miningfacebookdataforpredictivepersonalitymodeling.Vol.7,InProceedingsoftheinternational
AAAIconferenceonwebandsocialmedia(pp.23–26).
Markowitz,H.(1952).Portfolioselection.TheJournalofFinance,7,77–91.
McCrae,R.R.,&John,O.P.(1992).Anintroductiontothefive-factormodelanditsapplications.JournalofPersonality,60(2),175–215.
Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. In International conference on learning
representations,workshoptrackproceedings(pp.1–12).
Moreschi,R.W.(2005).Ananalysisoftheabilityofindividualstopredicttheirownrisktolerance.JournalofBusiness&EconomicsResearch,3(2),39–48.
Nasir, T., & Malik, M. K. (2024). Efficient CRNN: Towards end-to-end low resource urdu text recognition using depthwise separable convolutions and gated
recurrentunits.InformationProcessing&Management,61(1),Article103544.
NicolettaMarinelli,C.M.,&Palmucci,F.(2017).Mindthegap:Inconsistenciesbetweensubjectiveandobjectivefinancialrisktolerance.JournalofBehavioral
Finance,18(2),219–230.
Nobre,L.H.,&Grable,J.E.(2015).Theroleofriskprofilesandrisktoleranceinshapingclientinvestmentdecisions.JournalofFinancialServiceProfessionals,
69(3),18–21.
Norman,W.T.(1967).2800personalitytraitdescriptors:normativeoperatingcharacteristicsforauniversitypopulation.AnnArbor:UniversityofMichigan.
Ozer,G.,&Mutlu,U.(2019).Theeffectsofpersonalitytraitsonfinancialbehaviour.JournalofBusiness,EconomicsandFinance,8(3),155–164.
Pak,O.,&Mahmood,M.(2015).Impactofpersonalityonrisktoleranceandinvestmentdecisions:AstudyonpotentialinvestorsofKazakhstan.International
JournalofCommerceandManagement,25(4),370–384.
Pardo,F.M.R.,Celli,F.,Rosso,P.,Potthast,M.,Stein,B.,&Daelemans,W.(2015).Overviewofthe3rdauthorprofilingtaskatPAN2015.InCEURworkshop
proceedings:Vol.1391,WorkingnotesofCLEF2015-conferenceandlabsoftheevaluationforum,toulouse,France,September8-11,2015(pp.1–40).
Pennebaker,J.W.,&King,L.A.(1999).Linguisticstyles:Languageuseasanindividualdifference.JournalofPersonalityandSocialPsychology,77(6),1296–1312.
Pennington,J.,Socher,R.,&Manning,C.D.(2014).Glove:Globalvectorsforwordrepresentation.InProceedingsofEMNLP(pp.1532–1543).
Pinjisakikool,T.(2018).Theinfluenceofpersonalitytraitsonhouseholds’financialrisktoleranceandfinancialbehaviour.JournalofInterdisciplinaryEconomics,
30(1),32–54.
Piovesan,M.,&Willadsen,H.(2021).Riskpreferencesandpersonalitytraitsinchildrenandadolescents.JournalofEconomicBehaviourandOrganization,186,
523–532.
Pompian,M.M.,&Longo,J.M.(2004).Anewparadigmforpracticalapplicationofbehavioralfinance.JournalofWealthManagement,7(2),127–146.
Prinz, S., Grunder, G., Hilgers, R., Holtemoller, O., & Vernaleken, I. (2014). Impact of personal economic environment and personality factors on individual
financialdecisionmaking.FrontiersinPsychology,5,1–11.
Rahman,M.A.,AlFaisal,A.,Khanam,T.,Amjad,M.,&Siddik,M.S.(2019).Personalitydetectionfromtextusingconvolutionalneuralnetwork.InInternational
conferenceonadvancesinscience,engineeringandroboticstechnology(pp.1–6).
Ren,Z.,Shen,Q.,Diao,X.,&Xu,H.(2021).Asentiment-awaredeeplearningapproachforpersonalitydetectionfromtext.InformationProcessing&Management,
58(3),Article102532.
11

F.Xing InformationProcessingandManagement61(2024)103704
Rodrigues,C.G.,&Gopalakrishna,B.(2023).Financialrisktoleranceofindividualsfromthelensofbigfivepersonalitytraits–amultigenerationalperspective.
StudiesinEconomicsandFinance.
Saha,P.,Bose,I.,&Mahanti,A.(2016).Aknowledgebasedschemeforriskassessmentinloanprocessingbybanks.DecisionSupportSystems,84,78–88.
Sahm,C.R.(2012).Howmuchdoesrisktolerancechange?QuarterlyJournalofFinance,2(4),Article1250020.
Sharpe,W.F.(1964).Capitalassetprices:Atheoryofmarketequilibriumunderconditionsofrisk.TheJournalofFinance,19(3),429–442.
Siering, M. (2023). Peer-to-peer (P2P) lending risk management: Assessing credit risk on social lending platforms using textual factors. ACM Transactions on
ManagementInformationSystems,14(3),25:1–25:19.
Sun, X., Liu, B., Cao, J., Luo, J., & Shen, X. (2018). Who am i? Personality detection based on deep learning for texts. In IEEE international conference on
communications(pp.1–6).
Suzuki,M.,Sakaji,H.,Hirano,M.,&Izumi,K.(2023).Constructingandanalyzingdomain-specificlanguagemodelforfinancialtextmining.InformationProcessing
&Management,60(2),Article103194.
Tausczik,Y.R.,&Pennebaker,J.W.(2010).Thepsychologicalmeaningofwords:LIWCandcomputerizedtextanalysismethods.JournalofLanguageandSocial
Psychology,29(1),24–54.
Thavaneswaran, A., Liang, Y., Paseka, A., Hoque, M. E., & Thulasiram, R. K. (2021). A novel data driven machine learning algorithm for fuzzy estimates of
optimalportfolioweightsandrisktolerancecoefficient.In30thIEEEinternationalconferenceonfuzzysystems,FUZZ-iEEE2021,Luxembourg,July11-14,2021
(pp.1–6).
VandeVenter,G.,Michayluk,D.,&Davey,G.(2012).Alongitudinalstudyoffinancialrisktolerance.JournalofEconomicPsychology,33(4),794–800.
Vinciarelli,A.,&Mohammadi,G.(2014).Asurveyofpersonalitycomputing.IEEETransactionsonAffectiveComputing,5(3),273–291.
Wen,Z.,Cao,J.,Yang,Y.,Wang,H.,Yang,R.,&Liu,S.(2023).DesPrompt:Personality-descriptiveprompttuningforfew-shotpersonalityrecognition.Information
Processing&Management,60(5),Article103422.
Wilson,M.(1988).MRCpsycholinguisticdatabase:Machine-usabledictionary,version2.00.BehaviorResearchMethods,Instruments,&Computers,20,6–10.
Wong,A.,&Carducci,B.J.(2013).Doespersonalityaffectpersonalfinancialrisktolerancebehavior?TheIUPJournalofAppliedFinance,19(3),7–18.
Xing,F.,Cambria,E.,&Welsch,R.(2019a).Robo-Advisory(pp.113–122).Springer,ISBN:9783030302634.
Xing,F.,Cambria,E.,&Welsch,R.E.(2019b).Growingsemanticvinesforrobustassetallocation.Knowledge-BasedSystems,165,297–305.
Xing,F.,Malandri,L.,Zhang,Y.,&Cambria,E.(2020).Financialsentimentanalysis:Aninvestigationintocommonmistakesandsilverbullets.InProceedings
ofCOLING’20(pp.978–987).
Yang,K.,Lau,R.,&Abbasi,A.(2023).Deeplearningpersonalitymeasurementfromtext.InformationSystemsResearch,34(1),194–222.
Yao,R.,&Hanna,S.D.(2005).Theeffectofgenderandmaritalstatusonfinancialrisktolerance.JournalofPersonalFinance,4(1),66–85.
Yekrangi,M.,&Abdolvand,N.(2015).Areindividualstockinvestorsoverconfident?Evidencefromanemergingmarket.JournalofBehavioralandExperimental
Finance,5,35–45.
Yekrangi,M.,&Abdolvand,N.(2021).Financialmarketssentimentanalysis:developingaspecializedlexicon.JournalofIntelligentInformationSystems,57(1),
127–146.
Yin,C.,Jiang,C.,Jain,H.,&Wang,Z.(2020).EvaluatingthecreditriskofSMEsusinglegaljudgments.DecisionSupportSystems,136,Article113364.
Zhu,Y.,Hu,L.,Ge,X.,Peng,W.,&Wu,B.(2022).Contrastivegraphtransformernetworkforpersonalitydetection.InProceedingsofiJCAI’22.
Zimmerman,D.W.(2012).Heterogeneityofvarianceandbiasedhypothesistests.JournalofAppliedStatistics,40(1),169–193.
12