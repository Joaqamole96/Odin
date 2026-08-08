6 November 2024
Pitik: A Cebuano-Binisaya Intent-Based Chatbot for
Cardiovascular Disease Patient Profiling and Risk
Factor Recommendations
Joseph G. Cedeño, Andrew E. Manteza, Nicole C. Nacar, Merhamdin P. Umbukan, Cherrie G. Muaña, Ma. Juliet Vasay,
Ceasar Ian P. Benablo, Kristine Mae M. Adlaon
Abstract
Health is a top priority, especially given that cardiovascular diseases (CVDs) remain the leading
cause of death in the Philippines, affecting one in six Filipinos and accounting for 20% of all deaths.
To combat this, healthcare professionals are implementing community-based programs in rural
areas, though patient profiling is still manual. ”Pitik,” a Cebuano-Binisaya intent-based chatbot, was
developed to gather information, assess cardiovascular risks, and profile individuals. Guided by
Gricean Maxims, Pitik detects communication violations, ensuring effective interaction. This study
used Action Research, fostering collaboration between researchers, experts, and end-users. Through
three software development iterations, the Diag-Ex framework with Pre-Intent and Post-Intent
Matching algorithms significantly improved Pitik’s ability to respond smoothly to user prompts.
Keywords
cardiology, cardiovascular, chatbot, communication, networking and broadcast technologies,
computing and processing, conversational ai
Posted on 6 November 2024 — CC-BY 4.0 — This is a preprint and has not been peer reviewed. Data may be preliminary. — https://
doi.org/10.36227/techrxiv.173091273.31877417/v1

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
Pitik: A Cebuano-Binisaya Intent-Based Chatbot for
Cardiovascular Disease Patient Profiling and Risk Factor
Recommendations
Joseph G. Ceden˜o1, Andrew E. Manteza1, Nicole C. Nacar1, Merhamdin P. Umbukan1,
Cherrie G. Muan˜a1, Juliet V. Cruz1, Ceasar Ian P. Benablo1, and Kristine Mae M. Adlaon1
1Affiliation not available
November 06, 2024
Abstract
Healthisatoppriority,especiallygiventhatcardiovasculardiseases(CVDs)remaintheleadingcauseofdeathinthePhilippines,
affectingoneinsixFilipinosandaccountingfor20%ofalldeaths. Tocombatthis, healthcareprofessionalsareimplementing
community-based programs in rural areas, though patient profiling is still manual. ”Pitik,” a Cebuano-Binisaya intent-based
chatbot,wasdevelopedtogatherinformation,assesscardiovascularrisks,andprofileindividuals. GuidedbyGriceanMaxims,
Pitikdetectscommunicationviolations,ensuringeffectiveinteraction. ThisstudyusedActionResearch,fosteringcollaboration
between researchers, experts, and end-users. Through three software development iterations, the Diag-Ex framework with
Pre-IntentandPost-IntentMatchingalgorithmssignificantlyimprovedPitik’sabilitytorespondsmoothlytouserprompts.
Introduction
Cardiovascular diseases (CVDs) remain a significant public health challenge in the Philippines, consistently
ranking as the leading cause of mortality (Cacciata et al.,2021). These diseases account for approximately
20% of all deaths and 35% of premature deaths in the country, affecting one in every six Filipinos. High
blood pressure, high cholesterol, and smoking are key risk factors, along with other conditions and lifestyle
choices such as diabetes, obesity, and overweight. To address these issues outside Metro Manila, one of the
initiatives of healthcare professionals is conducting community outreach programs in rural and underserved
areas. These initiatives involve profiling residents and providing essential healthcare advice, aiming to
mitigatetheimpactofcardiovascular-relateddiseasesinthesecommunities(Reyesetal.,2023). Community-
based profiling and diagnosing of patients involves localized digital systems and at times physical records
dependingontheinstitution. Healthrecordsbetweeninstitutionsareencodedphysicallythroughpaperand
are not standardized between institutions (Evans, 2016; Menachemi, 2011). In many cases, health records
are maintained using localized digital systems, often with heavy reliance on physical records, especially in
less developed areas. The inconsistency in how patient information is recorded and stored across different
institutions leads to significant discrepancies, making it difficult to transfer patient data effectively. This
fragmentation of data hinders the ability to compile a comprehensive medical history, which is crucial for
accurate diagnosis and treatment. While some healthcare providers may have advanced electronic health
records (EHR) systems, others may still depend on outdated or manual methods. This disparity not only
complicates data sharing but also limits the overall efficiency and accuracy of patient profiling (Quinn et al,
2019; Casey et al., 2016; Iyanna et al, 2022).
The Philippines offers various healthcare applications like KonsultaMD, which provides 24/7 access to li-
censed doctors via telehealth (Noceda et al, 2023). While these technologies expand healthcare access, they
lack crucial elements. None are exclusively available in Cebuano-Binisaya, a language spoken by millions,
1

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
particularly in rural areas where access to healthcare is already limited. This gap is significant, as lan-
guage barriers can hinder effective communication and understanding, especially in areas with high rates of
cardiovascular diseases. Moreover, there are no existing Cebuano-Binisaya healthcare datasets, making it
challenging to create targeted digital tools for these communities. Developing a Cebuano-Binisaya chatbot
is essential to bridge these gaps, providing culturally and linguistically appropriate healthcare support, and
ensuring that vital health information and services are accessible to those who need them most.
Tobridgethesegapsandbringcriticalhealthcaresupporttothosewhoneeditmost, wedevelopedPitik—a
web application designed to speak directly to the heart of the Cebuano-Binisaya community. Pitik is more
than just a chatbot; it is a lifeline that helps users navigate their cardiovascular health concerns in their
native language, ensuring that no one is left behind. By focusing on underserved populations in remote
areas, Pitik aims to bring the benefits of modern healthcare technology to those who have been overlooked
for too long.
There are several applications with functionalities like Pitik, each offering unique approaches. For instance,
Diabot is a predictive medical chatbot that provides users with general disease and diabetes predictions,
encouraging proactive measures such as lifestyle changes and medication adjustments (Sarma et al., 2019).
Diabot employs ensemble learning to deliver accurate diagnoses, utilizing datasets such as a general health
dataset for disease prediction and the Pima Indian diabetes dataset for diabetes prediction. Other chatbots
collect personal and medical details, which are then analyzed using algorithms like Support Vector Machine
toidentifyspecificillnessesandsuggesttreatmentoptions. Additionally,somechatbotsfollowalineardesign,
progressing from symptom extraction to mapping and diagnosis, with severe conditions triggering a referral
to a doctor, who is then provided with relevant patient details from the database.
The availability of data is crucial for developing technology-based solutions, particularly those that heavily
relyondatafortheirfunctionality. Moreover,theCebuano-Binisayalanguagelacksdigitizeddatasetsrelated
toheartdiseasediagnosisorpatientprofiling. Thisabsencemaybeattributedtothechallengesintranslating
medical terminology into Cebuano-Binisaya and the potential under-exploration or unavailability of the
language’s implementation in the medical field, particularly in digital formats accessible to the public. Also,
the existing data in this domain is predominantly standardized forms, which necessitates constructing a
new dataset from the ground up. This process introduces various challenges, including sourcing the data,
determiningitsscope,andensuringthoroughdatacleaningandrefinement. Equallyimportantindeveloping
achatbotisitsinternalstructure. Howresponsesareformulatedcansignificantlyinfluenceusers’perceptions,
theirinterpretationoftheinformation,andtheirsubsequentactions. Researchindicatesthateffectiveadvice
dependsnotonlyonthecontentbutalsoonthepresentationofthatcontent. Thishighlightstheimportance
of evaluating chatbot responses in terms of both content and structure to ensure successful and meaningful
communication.
Considering these challenges, the primary objective of this study is to develop Pitik, a chatbot designed
for heart disease-related inquiries in the Cebuano-Binisaya language. The project aims to achieve this by
buildingaschema-guideddialoguedatasetspecificallyforheartdisease-relatedillnessesinCebuano-Binisaya,
addressingissuesrelatedtotheinternalstructureofthechatbot,anddiscoveringaconversationalschemethat
aligns with Cebuano-Binisaya’s conversational flow. Furthermore, the study seeks to employ both intrinsic
and extrinsic evaluation methods to assess Pitik’s performance based on the newly developed conversational
scheme, ensuring that the chatbot effectively communicates and meets user expectations.
Methods
ThedevelopmentofPitikadheredtoanIterativeSoftwareDevelopmentprocess,allowingforcontinuousen-
hancements and refinements. As illustrated in Figure 1, this process facilitated systematic progress through
multiple stages. In the first iteration, the team collaborated with healthcare professionals and reviewed
existing literature to gather comprehensive requirements. This informed the design of a user-friendly inter-
action medium in Cebuano, ensuring cultural and linguistic relevance. The initial implementation of the
chatbot was achieved using Google’s DialogFlow, based on a risk assessment form provided by healthcare
2

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
experts. Early testing underscored the need for additional data and further expert input, highlighting areas
forsignificantimprovement. Theseinsightsdrovesubsequentiterations, allowingPitiktoevolveintoamore
robust and effective tool for cardiovascular risk assessment and patient profiling.
Intheseconditeration,thedesignwasmeticulouslyrefinedtoalignmorecloselywithGriceanMaxims,aim-
ingtominimizeerrorsandreduceuserconfusion. Tofurtherenhancetheconversationalstructure,suggestion
chipswereintroduced,providinguserswithclearresponseoptionsandstreamlininginteractions. Thetesting
phase incorporated valuable feedback from both users and linguistic experts, allowing for a comprehensive
review of the chatbot’s conversation flow. This rigorous evaluation led to targeted improvements, ensuring
a more intuitive and effective user experience.
The third iteration concentrated on optimizing the conversational flow to better accommodate the nuances
of the Cebuano-Binisaya language, addressing challenges identified in earlier stages. This phase involved
refining the chatbot’s ability to handle a broader spectrum of user inputs, enhancing its flexibility and
responsiveness. The evaluation process was rigorous, employing the Analytic Hierarchy Process (AHP)
method to assess overall quality. Pitik underwent both intrinsic and extrinsic evaluations: intrinsically, its
thoroughness in assessing cardiovascular health was scrutinized, while extrinsically, it was evaluated based
on user feedback from prior iterations. These assessments ensured that Pitik not only met the technical
requirements but also resonated with its target users, enhancing its effectiveness as a healthcare tool.
The researchers made use of Grice’s Maxims of conversation to evaluate the acceptability of the user input
whichplaysaveryimportantroleinthesuccessorfailureofPitik. Grice’smaximsofconversationwerechosen
asaframeworksinceitservesasaguideinconstructingandevaluatingthedesignofourconversationalflow.
ThephilosopherPaulGrice(1975)proposedfourconversationalmaximswhichserveasawaytoexplainthe
link between utterances and what is understood from them. It is based on his cooperative principle which
is pragmatic in its approach and is so-called because listeners and speakers must speak cooperatively and
mutually accept one another to be understood in a particular way. There are four main maxims proposed
by linguist Paul Grice to describe principles that people intuitively follow to guide their conversations. This
work is guided by this principle to have effective communication with the users as shown in Figure 2. After
the testing phase, the user’s answers were evaluated using this study to see if the chatbot and user have
establishedsuccessfulcommunication. ViolationstotheGriceanMaximinvolvenotfollowingthedesignated
rules shown below, violations may overlap where a sentence or phrase can violate multiple maxims.
Gricean Maxims:
1. The maxim of quantity - where one tries to be as informative as one possibly can, and gives as much
information as is needed, and no more.
2. The maxim of quality - where one tries to be truthful and does not give information that is false or
that is not supported by evidence
3. The maxim of relation - where one tries to be relevant and says things that are pertinent to the
discussion.
4. The maxim of manners - when one tries to be as clear, as brief, and as orderly as one can in what one
says, and where one avoids obscurity and ambiguity.
3

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
Figure 2: Example of Grice Maxim Occurrences in Pitik
AsPitikunderwentiterativetesting,itwasprogressivelytrainedtocomprehendtheoptimalandmosttoler-
ableresponsesgatheredfromusersduringtheDataCollectionphase. Currently,Pitikoperatesinalignment
with the principles of the Cooperative Principle, particularly Grice’s Maxims, while also drawing on the
insights from our collected data. Violations of Grice’s Maxims are triggered whenever DialogFlow fails to
match a user input with a defined intent, resulting in a fallback intent. This phenomenon predominantly
affects Pitik’s generic questions regarding exercise, diet, smoking, and alcohol, which often elicit a wide
range of user responses, frequently resulting in the flouting of the Cooperative Principle. As DialogFlow
matches the closest training phrases, it struggles to address variations in user responses. To enhance func-
tionality,developersutilizeintentstodefinespecifictasksthatuserscanperform,ensuringamorestructured
interaction.
Process Flow of Pitik using DialogFlow
The researchers utilized DialogFlow, a natural language understanding platform, to design and integrate
a conversational user interface for the Pitik chatbot. The platform facilitates user interaction by allowing
end-users to input text, which DialogFlow matches to specific intents while extracting relevant parameters.
Once the intent is identified, DialogFlow sends a webhook request to the designated service, including
informationaboutthematchedintent,theassociatedaction,parameters,andthepredefinedresponse. Pitik
then executes the necessary actions, retaining the extracted information and guiding users through the
relevant conversational flow. Subsequently, Pitik generates a webhook response message directed back to
DialogFlow, containing the response intended for the end-user. Finally, DialogFlow relays this response to
4

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
the user, ensuring seamless interaction and effective communication throughout the conversation.
Cardiovascular Risk Assessment Sheet
Pitik initiates the conversation by greeting the user, establishing a friendly and welcoming environment.
Following the exchange of greetings, Pitik collects essential demographic information, including the user’s
name, age, sex, weight, and height. For female users, the chatbot then inquires about pregnancy-related
details, such as current pregnancy status and the number of children they have. After gathering this infor-
mation, Pitik proceeds to collect information about the user’s symptoms, as well as their medical, surgical,
andfamilyhistories. Subsequently, thechatbotposesquestionsrelatedtolaboratoryresults, includingmea-
surements such as HbA1c, systolic blood pressure, and diastolic blood pressure. During the contact details
stage, users have the opportunity to provide their email addresses for receiving comments or recommenda-
tionsfromhealthcareprofessionals. Finally,PitikgeneratesariskfactorassessmentandcalculatestheBody
Mass Index (BMI) for the user. The complete conversational flow of Pitik is illustrated in Figure 4.
To assess the cardiovascular risk of Pitik user, the researchers utilized a cardiovascular risk
assessment sheet 11https://pcna.net/wp-content/uploads/2018/12/1- patient assessment.pdf
recommended by a healthcare professional conducting community-based profiling and risk
factor assessment. Risk factor is then computed using the Framingham formula (D’Agostino
et al., 2008):
Risk Factors = (ln(Age) * 3.06117) + (ln(Total cholesterol) * 1.12370) -
(ln(HDL cholesterol) * 0.93263) + (ln(Systolic blood pressure) *
On blood pressure medication) + Cigarette smoker + Diabetes present -
23.9802
5

| Risk = 100 | * (1 - | 0.88936e(Risk | Factors)) |     |
| ---------- | ------ | ------------- | --------- | --- |
Pitikistrainedtorecognizeinputsymptomsbasedonapredefinedlistofcardiovascularrelated
diseases and its corresponding symptoms 11https://my.clevelandclinic.org/health/diseases/21493-
cardiovascular-disease. Table 1 shows the cardiovascular diseases and their corresponding symp-
| toms (in                | Cebuano-Binisaya). |          |              |     |
| ----------------------- | ------------------ | -------- | ------------ | --- |
| Table 1: Cardiovascular |                    | Diseases | and Symptoms |     |
| Cardiovascular          | Disease            |          | Symptoms     |     |
Congenital Heart Disease Pagkablue, namutla, hubag, hupong,lisud ginhawa, wad-an kusog, pitik, di regular, kasingkasing, lipong, sakit ulo.
Arrythmia Gaan - Paminaw, Bloat - Tiyan, Paspas - Heartbeat, Hinay - Pulso, Taas - Blood presssure, Diabetes, Sakit - dughan, Maluya, Kalipong, Kapit-os ug kabalaka, Alcohol - caffeine
Cardiomyopathy kapoy, lisud og ginhawa, hubag ang bitiis, bukong ug tiil, bloat nga tiyan, ubo, sakit sa dughan, lipong, luya
...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP Atherosclerosis kabugnaw,manhid,Kahuyang,kawad-an og usog
Coronary Heart Disease Sakit sa dughan, Dili komportable ang dughan, Kumot sa dughan, Kakulang sa ginhawa, Kasukaon
Heart Infection Kakapoy, Kalipong, Pagkulbakulba Sakit sa dughan, Kalintura, Nagamaga akong bitiis, Dugo sa akong ihi, pula na tuldok sa lawas, sa puti sa mata o sa sulod sa baba nay pula pula.
Figure 5 shows an actual example of how Pitik attempts to capture user symptoms.
| Analytic | Hierarchy | Process |     |     |
| -------- | --------- | ------- | --- | --- |
Pitik’s testing phase centered on evaluating the chatbot’s overall quality using the method recommended by
(Radziwill and Benton, 2017). This approach employs the Analytic Hierarchy Process (AHP), a structured
technique for organizing and analyzing complex decisions that involve both qualitative and quantitative
factors. The researchers selected AHP to assess and quantify criteria related to the quality of the Pitik
chatbot effectively. The goal was to compare and evaluate the performance of the original version of Pitik
against the updated version per iteration. The criteria chosen for this assessment were aligned with the
| study’s thematic | focus | and objectives | shown in Figure | 6.  |
| ---------------- | ----- | -------------- | --------------- | --- |
6

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
Figure 6: Hierarchical Structure for Pitik Chatbot Evaluation
Each category has its different methods of evaluation to contribute to the overall chatbot quality. For the
category ‘Humanness’, the evaluation made use of a google form comprising an answerable, open-ended
question form and a Likert-scale format question from appearing at the very end of the chat conversation
that lets users be able to evaluate the chatbot based on the category that is identified to analyze the quality
producing Likert scale information and opinionated information about the user-opinion. The researchers
utilized a tally system for counting Gricean Maxim Violations for the user inputs and a linguist expert-
reviewedverdict. Forthe‘Performance’,theresearchersusedanothertallysystemthatcountsthenumberof
timesPitikhasfailedtorespondappropriatelyduringtheconversationwiththeuser. Forthe‘Accessibility’,
the researchers used a similar method with finding the Performance with the difference of tallying the
circumstances when the users are the ones to ask the questions for Pitik.
We have used Precision, Recall, F1 Score, Accuracy and its weighted average to evaluate our post-intent
matching algorithm which trained several machine learning models to classify intents. Precision, being the
ratio between the True Positives and all the Positives, enables us to identify true positives with respect to
the overall positive predictions. A high precision means it has a lower false positive rate. Recall is the ratio
ofthecorrectlypredictedpositiveoccurrenceswithrespecttotheoverallobservationsintheactualclass. F1
Score is the average from both Precision and Recall and in return takes account of false positives and false
negatives. Accuracy is the number of correct predictions with respect to the overall data. This is achieved
by adding both true positives and true negatives to true positives, true negatives, false negatives and false
positives. The weighted average is generated by multiplying each of the evaluation measurements by their
corresponding weight which is the percentage count of the total class with respect to the overall test data.
Results and Discussion
The researchers were able to build a schema-guided dialogue set gathered from 100 participants by reaching
through social media and word of mouth. The selection of participants preferred to be of those residing in
provincial areas but due to limited time and accessibility, the selection was made if the participant could
communicate using the identified language of Pitik. The first 50 participants interacted with Pitik during
the second iteration then the remaining 50 participants during the third iteration. A link was sent with
instructions and information concerning the purpose of the study to the participants.
The researchers gathered the responses and were able to group and analyze the data by checking which
responses violated Gricean Maxims with the help of an expert. An example is shown in Table 2, which
7

producedbugsinthesystemandhowtheparticipantswereabletoanswerspecificallythelaboratory-related
| questions | such as blood pressure.   |     |     |     |     |     |     |
| --------- | ------------------------- | --- | --- | --- | --- | --- | --- |
| Table 2:  | Gricean Maxims Violations |     |     |     |     |     |     |
|           |                           |     |     |     |     | 2nd | 3rd |
Gricean Maxims Sample Responses Iteration Violations Iteration Violations
Manner “murag naa sa 125-250”, “sauna naa pero karon wala” 44 22
Relation “wala kay ginabutang ra nko sa kamot”, “gipaak kog ilaga, dugay na sukad bata pa ko” 18 6
| Quantity | “oo pag | ma stress ko”,   | “dli kay weak” |     |     | 24  | 16  |
| -------- | ------- | ---------------- | -------------- | --- | --- | --- | --- |
| Quality  | “murag  | naa sa 125-250”, | “5’2 ata”      |     |     | 7   | 5   |
Severalmodelsweretrainedtodevelopaneffectiveclassifierforintentrecognition. Theresearchersevaluated
...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
andcomparedtheperformanceoffouralgorithms: NaiveBayes(NB),SupportVectorMachine(SVM),Multi-
Layered Perceptron (MLP), and Recurrent Neural Network (RNN). These algorithms are well-established
for classifying text data. Naive Bayes classifiers operate under the assumption of strong (or naive) indepen-
dence between the attributes of data points. They are widely used in applications such as spam filtering,
text analysis, and medical diagnosis. Support Vector Machines (SVM) are supervised machine learning
models designed for binary classification tasks, effectively separating data into two distinct groups. The
Multi-Layered Perceptron (MLP) classifier relies on an underlying neural network to perform classification,
allowing it to learn complex patterns in the data. Recurrent Neural Networks (RNNs), on the other hand,
are commonly employed in speech recognition and natural language processing due to their ability to recog-
nize sequential patterns in data and predict future scenarios, although they are typically more complex to
implement.
Table 3 presents a comparative analysis of the four classifiers across two domains: Diet/Exercise and Smok-
ing/Alcohol. Allmodelsweretestedonabalanceddatasetcomprising40recordsderivedfromatotalof200
training samples.
Table 3: Model Performances for sample diet/exercise and smoking/alcohol areas
|     | Area of Comparison | Models | Precision | Recall | F1 Score Accuracy |     |     |
| --- | ------------------ | ------ | --------- | ------ | ----------------- | --- | --- |
|     | Diet/Exercise      | NB     | 71        | 70     | 70 70             |     |     |
|     |                    | SVM    | 70        | 70     | 70 70             |     |     |
|     |                    | MLP    | 65        | 65     | 65 65             |     |     |
|     |                    | RNN    | 58        | 57     | 57 57             |     |     |
|     | Smoking/Alcohol    | NB     | 72        | 68     | 66 68             |     |     |
|     |                    | SVM    | 78        | 72     | 71 73             |     |     |
|     |                    | MLP    | 70        | 68     | 66 68             |     |     |
|     |                    | RNN    | 61        | 60     | 59 60             |     |     |
The Naive Bayes and SVM models demonstrate similar performance in the Diet/Exercise category, with
each achieving Precision, Recall, F1 Score, and Accuracy values of approximately 70%. This suggests that
these models are relatively effective in classifying or predicting outcomes related to Diet and Exercise. The
MLPmodelshowsaslightdeclineinperformance,withallmetricsstandingat65%,indicatingamoderately
lower ability to generalize in this context. Conversely, the RNN model exhibits the weakest performance,
with metrics in the range of 57-58%, highlighting significant challenges in capturing the patterns associated
with Diet and Exercise. In the Smoking/Alcohol category, the SVM model emerges as the most effective,
boasting the highest Accuracy (73%) and relatively high values across all other metrics, which underscores
its robustness in handling this classification task. The Naive Bayes model, while strong in Precision (72%),
showsalowerF1Score(66%), indicatingsometrade-offsbetweenPrecisionandRecall. MLP’sperformance
8

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
mirrorsthatofNaiveBayesinthiscontext,whiletheRNNmodelcontinuestounderperform,withallmetrics
falling around 59-61%. The results indicate that the SVM model is particularly well-suited for tasks related
toSmoking/Alcohol,outperformingothermodelsbyanotablemargin. ItsabilitytomaintainhighAccuracy
and balanced metrics suggests that it can be relied upon for more accurate predictions and classifications in
this domain. On the other hand, the RNN model’s consistent underperformance across both areas suggests
that it may struggle with the type of data or features used in these tasks.
The researchers assessed accessibility by examining the success rate of five critical laboratory questions,
such as HBA1C and Systolic Blood Pressure, which often pose significant barriers due to the need for prior
medicalknowledgeandspecificinstrumentresults. Initially,theaveragesuccessratewasamere22%,asmost
respondents lacked their lab results, leading to widespread failure in answering these questions. However,
in the third iteration, the introduction of the Naive Bayes algorithm and post-intent processing significantly
boosted both performance and accessibility, with rates soaring from 65% to 79% and 22% to an impressive
96%, respectively. This remarkable improvement was driven by the third iteration’s enhanced user guidance
and response processing, featuring new tools like suggestion chips and tooltips. The researchers recognized
that many users sought definitions for medical terminologies, such as HBA1C, prompting the integration of
tooltips to assist users unfamiliar with terms like Systolic Blood Pressure, Diastolic Blood Pressure, Total
Cholesterol, and HDL Cholesterol. Additionally, suggestion chips were implemented to address instances
wherethechatbotfailedtorecognizeuserinput,guidinguserstowardsaformatthesystemcouldunderstand.
For example, when a user responded ”n/a” to a question about waist circumference, a suggestion chip
appeared to offer guidance. These enhancements were crucial in overcoming the limitations encountered
during the training phase, ensuring that the system could adapt to unforeseen inputs and vastly improving
overall user experience.
There are two key scenarios where suggestion chips are strategically deployed to enhance user interaction.
In the first scenario, suggestion chips appear during the initial occurrence of a question to confirm the
accuracy of user input. These questions typically involve a prompt to verify that the chatbot has correctly
understood the input. In the second scenario, suggestion chips address questions that may elicit unexpected
or unanticipated responses, which became evident during the system’s second iteration. For instance, when
Pitik asked for the father’s name, one user out of 100 responded that they did not know their father. To
accommodate such rare but important cases, the researchers created an Intent that acknowledges and skips
the question. However, due to the limited occurrence of such responses, there weren’t enough training
phrases to fully support this Intent. Therefore, suggestion chips were implemented at the first occurrence
of such questions, enabling users to skip questions related to parents they do not know. This adjustment
significantly improved performance by allowing the chatbot to handle a broader range of responses while
maintaining focus on essential information.
Moreover, when users encountered one of the five laboratory questions—HBA1C, Systolic and Diastolic
Blood Pressure, Total Cholesterol, and HDL Cholesterol—many did not know their results. Instead of
persisting with these questions, the researchers provided suggestion chips, allowing users to select which
laboratory questions they could answer. These enhancements not only improved user experience but also
led to a significant increase in accessibility, as the chatbot became more adept at catering to diverse user
needs and circumstances.
The data collected from the respondents were evaluated using AHP to check for version improvements.
Performance values were taken from responses of Pitik that went into a fallback intent and did not continue
towards further intents. Humanness was assessed from their responses and how they rated Pitik according
to their experience. Accessibility was assessed as well in the same manner as to how the Performance was
checked with the focus of user responses pertaining to accessibility.
Table 4: Reciprocal matrix for pairwise comparisons
Category Performance Humanness Accessibility
Performance 1 9 7
9

|     | Category      |        | Performance | Humanness | Accessibility |
| --- | ------------- | ------ | ----------- | --------- | ------------- |
|     | Humanness     |        | 0.111       | 1         | 0.5           |
|     | Accessibility |        | 0.143       | 2         | 1             |
|     | Criterion     | Weight | 0.790       | 0.077     | 0.133         |
Table 4 highlights how each category is weighted relative to the others. Performance is deemed significantly
more important than both Humanness and Accessibility, with a comparison ratio of 9:1 against Humanness
and 7:1 against Accessibility. Conversely, Humanness is considered less important than Accessibility, with
a ratio of 0.5:1, indicating that Accessibility is valued twice as much as Humanness. The reciprocal nature
of the matrix is evident, as each off-diagonal value corresponds to the reciprocal of its counterpart. For
instance, the value comparing Humanness to Performance (0.111) is the reciprocal of the value comparing
...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP Performance to Humanness (9). The final row of the table reveals the derived criterion weights, reflecting
the overall importance of each category: Performance carries the highest weight at 0.790, indicating its
dominantroleinthedecision-makingprocess. Accessibilityfollowswithaweightof0.133, whileHumanness
has the lowest weight at 0.077. These weights suggest that Performance is overwhelmingly prioritized,
with Accessibility also considered important, but Humanness is given the least emphasis, showing a strong
| preference | for functional aspects | over | human-centric | qualities. |     |
| ---------- | ---------------------- | ---- | ------------- | ---------- | --- |
| Conclusion | and Recommendations    |      |               |            |     |
Thisstudyproducedaschema-guideddialoguedatasetfocusedonheartdisease-relatedillnessesinCebuano-
Binisaya through user interactions with the Pitik chatbot. The enhancements made to the system resulted
in increased accessibility, leading to a notable reduction in performance issues and Gricean Violations. The
intrinsicevaluationsdemonstratedthattheimprovementsallowedforresponsestobemoreeffectivelytailored
to the chatbot’s needs, significantly decreasing Maxim Violations and enhancing accuracy. A conversational
schemewasimplementedtodisambiguateunrecognizedresponsesbeforeproceedingtosubsequentquestions.
Utilizing a reciprocal matrix for pairwise comparisons, as presented in Table 4, the researchers measured
the priority of objectives and observed a consistent emphasis on performance. Ultimately, the adoption of
the Support Vector Machine (SVM) algorithm in post-intent matching markedly improved the chatbot’s
| performance | and accessibility. |     |     |     |     |
| ----------- | ------------------ | --- | --- | --- | --- |
Based on extensive research, several recommendations have been identified. First, the Multinomial Naive
Bayes algorithm used for Post-Intent Matching demonstrated inferior performance compared to other algo-
rithms, leading to the recommendation of SVM for text classification, given its superior results with small
datasets. DuringtheextrinsicevaluationofthePitikchatbot,usersexpressedconcernsregardingthelengthy
conversationalformat. Therefore,abutton-basedscenarioisrecommendedforfutureiterationstostreamline
interactions. Additionally,usersweredissatisfiedwiththechatbot’soutput,notingalackofconsultationsor
tips related to heart diseases. Implementing features that allow doctors to edit the risk assessment form ad-
dressesthisissue,butfurtherrecommendationsincludeenablingPitiktoprovidemedical-relatedinformation
| based on user | inputs. |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- |
References
CacciataMC,AlvaradoI,JoseMM,EvangelistaLS.Healthdeterminantsandriskfactorsforcoronaryartery
disease among older Filipinos in rural communities. Eur J Cardiovasc Nurs. 2021 Aug 20;20(6):565-571.
| doi: 10.1093/eurjcn/zvaa039. |     | PMID: | 34019082; PMCID: | PMC8324596. |     |
| ---------------------------- | --- | ----- | ---------------- | ----------- | --- |
Casey JA, Schwartz BS, Stewart WF, Adler NE. Using Electronic Health Records for Population Health
Research: A Review of Methods and Applications. Annu Rev Public Health. 2016;37:61-81. doi:
10.1146/annurev-publhealth-032315-021353. Epub 2015 Dec 11. PMID: 26667605; PMCID: PMC6724703.
D’Agostino RB Sr, Vasan RS, Pencina MJ, et al. General cardiovascular risk profile for use in primary care:
| the Framingham | Heart Study. | Circulation | 2008; | 117:743. |     |
| -------------- | ------------ | ----------- | ----- | -------- | --- |
10

...btondluohsyehT.deweiverreeptoneratahtstroperyranimilerperavixRhceTnodetsopstnirP-e—1v/71477813.372190371.vixrhcet/72263.01/gro.iod//:sptth—0.4YB-CC—4202voN6nodetsoP
EvansRS.ElectronicHealthRecords: Then,Now,andintheFuture. YearbMedInform. 2016May20;Suppl
1(Suppl 1):S48-61. doi: 10.15265/IYS-2016-s006. PMID: 27199197; PMCID: PMC5171496.
Grice, P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), Syntax and semantics (Vol. 3,
pp. 41-58). Academic Press.
Menachemi N, Collum TH. Benefits and drawbacks of electronic health record systems. Risk Manag
Healthc Policy. 2011;4:47-55. doi: 10.2147/RMHP.S12985. Epub 2011 May 11. PMID: 22312227; PM-
CID: PMC3270933.
NocedaAVG,AciertoLMM,BertizMCC,DionisioDEH,LauritoCBL,SanchezGAT,LorecheAM.Patient
satisfaction with telemedicine in the Philippines during the COVID-19 pandemic: a mixed methods study.
BMCHealthServRes. 2023Mar22;23(1):277. doi: 10.1186/s12913-023-09127-x. PMID:36949479;PMCID:
PMC10032251.
Quinn M, Forman J, Harrod M, Winter S, Fowler KE, Krein SL, Gupta A, Saint S, Singh H, Chopra
V. (2019). Electronic health records, communication, and data sharing: challenges and opportunities for
improving the diagnostic process. Diagnosis (Berl). 2019 Aug 27;6(3):241-248. doi: 10.1515/dx-2018-0036.
PMID: 30485175; PMCID: PMC6691503.
Radziwill,Nicole&Benton,Morgan. (2017). EvaluatingQualityofChatbotsandIntelligentConversational
Agents.
Reyes AT, Serafica R, Kawi J, Fudolig M, Sy F, Leyva EWA, Evangelista LS. (2023). Using the Socioeco-
logical Model to Explore Barriers to Health Care Provision in Underserved Communities in the Philippines:
Qualitative Study. Asian Pac Isl Nurs J. 2023 Aug 22;7:e45669. doi: 10.2196/45669. PMID: 37606966;
PMCID: PMC10481217.
Sarma,Manash&Chatterjee,Subarna&Mohanty,Samahit&Puravankara,Rajesh&Bali,Manish. (2019).
Diabot: A Predictive Medical Chatbot using Ensemble Learning. 10.35940/ijrte.B2196.078219.
Shilpa Iyanna, Puneet Kaur, Peter Ractham, Shalini Talwar, A.K.M. (2022) Najmul Islam, Digital trans-
formation of healthcare sector. What is impeding adoption and continued usage of technology-driven in-
novations by end-users?, Journal of Business Research, Volume 153, 2022, Pages 150-161, ISSN 0148-2963,
https://doi.org/10.1016/j.jbusres.2022.08.007.
11