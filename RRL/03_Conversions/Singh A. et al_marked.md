HYPOTHESIS -National Journal of Research in Higher Studies ISSN-2581-8953
Volume VIII, Issue 2, July 2025– December 2025
A Smart Personal Finance Assistant for Budget
Management and Expense Tracking
Abhinav Singh Garv Rastogi
Department of Computer Science and Engineering Department of Computer Science and Engineering
Galgotias University Galgotias University
Uttar Pradesh, India Uttar Pradesh, India
abhinav.22scse1011115@galgotiasuniversity.edu.in garv.22scse1010043@galgotiasuniversity.edu.in
JN Singh
Department of Computer Science and Engineering
Galgotias University
Uttar Pradesh, India
singhjn2000@gmail.com
Abstract—Personalfinancemanagementisanincreasinglyrel- Recent studies indicate that lack of financial awareness and
evantphenomenoninthemoderndigitalagebecauseofincreased improper expense tracking are major contributors to personal
costs,onlinepayments,andlackoffinancialliteracy.Peopleface
financial stress. User behavior, inconsistent tracking habits,
difficulties in managing their income and expenditures in an
and limited access to simple financial tools further aggravate
appropriateway,resultinginincorrectbudgetingandsavings.To
overcome the problem, this paper introduces the novel concept this issue. Without proper guidance and structured analysis,
of Smart Personal Finance Assistant in the form of an online individuals find it challenging to plan budgets and make
application that helps in expense and budget management. informed financial decisions.
ThesolutionisdevelopedusingReactwithTypeScripttobuild To address these challenges, a Smart Personal Finance
a responsive UI, alongside cloud services to host the authenti-
Assistant is proposed that focuses on simplifying expense
cation/secure storage functionality. The solution includes func-
tracking and budget management. The system enables users
tionalities such as entry of income/expense, auto-categorization
of expenses, as well as financial data representation using UI to record income and expenses, categorize transactions, and
dashboards/charts.Alightnaturallanguageprocessingalgorithm visualize spending patterns through intuitive summaries. By
is employed to evaluate financial transactions to determine providing clear financial insights and promoting disciplined
their respective categories, coupled with KMeans clustering to
spending habits, the proposed solution supports improved
segregate financial spending into viable categories.
financial decision-making and long-term budget control.
The proposed system shows how the use of modern web
technologies along with rule-based text analysis and clustering
algorithms can provide a feasible and user-friendly tool for
II. LITERATUREREVIEW
disciplined spending and effective budget management. As the need for personal financial management is gaining
IndexTerms—PersonalFinanceManagement,ExpenseTrack-
prominence, some studies have been carried out on electronic
ing, Budget Management, K-Means Clustering, Text-Based Cat-
tools and applications which help people manage their ex-
egorization, Smart Finance Assistant, Data Visualization.
penditure and budget. [1] [2] [5] [8] It is suggested through
some research that unorganized expenditure management and
I. INTRODUCTION
poor financial planning are the major reasons for poor saving
Financial management for the individual is an extremely habitsandfinancialproblems.[3][4][6]Manualbookkeeping
important aspect when considering the stability of finance or spreadsheet management is inefficient for handling regular
in the current world. This stability is affected by the use transactions and multiple expenditure categories. [10]
of electronic payment services and the rising cost of living, Research about user behavior shows that breaking down
making it difficult for the individual to effectively monitor expenses by categories, either through text formats or pic-
his income and expenditures. This hampers the person from tographic diagrams, can increase financial awareness about
spendinghismoneyintherightwayandresultsinlesssavings. spending behavior among users. [7] [15] Graphic displays of
Traditional methods of personal finance management, like financial information have been found to be more effective.
bookkeeping or using spreadsheets for finance management, Recent research has also focused on the application of
can be tedious and involve errors. However, most of the clustering methodologies in personal finance systems for the
applicationsthathelpinfinancemanagementlacksimplicityor derivation of spending patterns and grouping similar trans-
lackaneffectiveinterfacethatcaneasilydisplayfinancialdata. actions. [7] [?] K-Means clustering is one of the prominent
Because of this, most of the applications lack the ability to approaches that have been used in segmenting expenses into
provide insight to the user regarding their financial activities. meaningfulgroups,thusenablinguserstorecognizedominant
©Indirapuram Institute of Higher Studies (IIHS)
A Bi-Annually Double-Blind Peer Reviewed, Open Access National e-Journal 1

HYPOTHESIS -National Journal of Research in Higher Studies
ISSN-2581-8953
Volume VIII, Issue 2, July 2025– December 2025
| spending          | habits        | and assess      | their         | budget            | usage             | more effec-  |     |     |     |     |     |     |
| ----------------- | ------------- | --------------- | ------------- | ----------------- | ----------------- | ------------ | --- | --- | --- | --- | --- | --- |
| tively. Secondly, |               | lightweight     | text-based    |                   | analytical        | techniques   |     |     |     |     |     |     |
| have been         | developed     | that            | automatically |                   | classify          | expenses by  |     |     |     |     |     |     |
| analyzing         | transaction   | descriptions    |               | through           | keyword           | patterns,    |     |     |     |     |     |     |
| hence reducing    | manual        | classification  |               | effort.           | [8]               | [10]         |     |     |     |     |     |     |
| On the            | whole,        | the reviewed    | literature    |                   | precisely         | highlighted  |     |     |     |     |     |     |
| the need          | to have       | an intelligent  |               | and user-friendly |                   | personal     |     |     |     |     |     |     |
| finance assistant |               | that can        | handle        | activities        | of                | expenditure  |     |     |     |     |     |     |
| tracking,         | automatic     | categorization, |               | spending          | pattern           | analysis,    |     |     |     |     |     |     |
| and clear         | visualization | under           | one           | platform.         | [5]               | [7] [15] The |     |     |     |     |     |     |
| system proposed   |               | will fill       | these gaps    | through           | usability-focused |              |     |     |     |     |     |     |
designcombinedwithclustering-basedanalysisandbasictext
processingsupportinginformedfinancialdecision-makingand
| long-term | budget | planning. | [11] | [14] |     |     |     |     |     |     |     |     |
| --------- | ------ | --------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
III. RESEARCHMETHODOLOGY
| In the         | proposed    | Smart           | Personal | Finance            | Assistant,          | the          |     |     |     |     |     |     |
| -------------- | ----------- | --------------- | -------- | ------------------ | ------------------- | ------------ | --- | --- | --- | --- | --- | --- |
| research       | methodology | employed        |          | is design-focused. |                     | The main     |     |     |     |     |     |     |
| aim of the     | research    | methodology     |          | is the             | creation            | of a techno- |     |     |     |     |     |     |
| logical system | capable     | of              | allowing | the                | effective           | monitoring   |     |     |     |     |     |     |
| of income      | as well     | as expenses.    |          | This               | is a design-focused |              |     |     |     |     |     |     |
| research       | methodology | because         | its      | main aim           | is the              | design of    | a   |     |     |     |     |     |
| technological  | system.     |                 |          |                    |                     |              |     |     |     |     |     |     |
| ”Methodology   |             | The development |          | process            | involves            | the iden-    |     |     |     |     |     |     |
Fig.1. ResearchMethodologyandFinancialDataProcessingModel
tificationofkeyfunctionalrequirementssuchastherecording
| of expenses, | the | management | of  | income, | the | allocation of |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
expenses, and budget monitoring. This is followed by the easy and user-friendly, attracting the target group to provide
|     |     |     |     |     |     |     | the data | without | struggling. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----------- | --- | --- | --- |
designofthesystemarchitecturebasedupontherequirements
| using current | standards |                 | and technologies. |          | This | is designed |     |     |                 |     |     |     |
| ------------- | --------- | --------------- | ----------------- | -------- | ---- | ----------- | --- | --- | --------------- | --- | --- | --- |
|               |           |                 |                   |          |      |             |     |     | V. DATAANALYSIS |     |     |     |
| to enable     | the user  | to conveniently |                   | interact | with | financial   |     |     |                 |     |     |     |
informationandtoensurethecorrectprocessingandrecording The collected financial information is used to interpret
of the financial transaction details.” user financial behavior. This analysis entails the process of
The process of applying the app relates to the interaction generating useful insights from the raw financial information,
of the user in entering financial information; the back end of which helps users to take informed financial actions.The
|         |                |     |                  |     |     |               | transactions | entered | by the | customers | are organized | first, |
| ------- | -------------- | --- | ---------------- | --- | --- | ------------- | ------------ | ------- | ------ | --------- | ------------- | ------ |
| the app | is responsible | for | the organization |     | of  | the financial |              |         |        |           |               |        |
information. The front end is used in the display of the categorizingexpenseslikeFood,Transport,Rent,Utilities,and
financial information. The real-time update feature is ideal as Entertainment,amongothers.Asimpletextanalysistechnique
it helps the user monitor their financial condition at all times. is used for the transactions, whereby keywords are used to
This helps the user in organizing their expenses. automatically categorize transactions. This makes the process
|     |     |     |     |     |     |     | easier as | customers | do not have | to go | through the trouble | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----------- | ----- | ------------------- | --- |
IV. DATACOLLECTION
doingtheanalysisontheirown.Comparisonsbetweenincome
Data Acquisition stage in the design for the Smart Personal and expenses for each month are made.
Finance Assistant relies mainly on the user, considering that In order to further evaluate the spending behavior, the
the stage involves the recording of transactions that occur system uses the K-Means clustering technique to categorize
in the span of one day. Users are asked to enter all the the spending into clusters, depending on the patterns of the
information related to their income and expenses manually by spendingamount.Theclusteringobtainedfromthesystemcan
makinguseoftheinterfaceoftheapplication.Everyandeach enable one to recognize important clusters like low recurring
transaction has parameters like amount, category, and time payments and high occasional payments, depending on their
entered, which play an important part in keeping appropriate nature. Budget evaluation and areas of financial management
| records. |     |     |     |     |     |     | are assisted | through | the clustering | obtained. |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ------------ | ------- | -------------- | --------- | --- | --- |
The collected data is properly secured in the system’s Use of graphical illustrations such as charts and summaries
database, which can then be used for analysis and graph isdonetointerprettheanalyzeddatainthesimplestapproach.
representation. The fact that the depicted data in the system This enables the user to interpret the levels of spending, the
above shows actual expenditure behavior by the users makes groupings of the distributions, and the use of the budget. In
it possible for the system to effectively summarize the same conclusion, the analysis process of the budget usage involves
data. The process of obtaining the same data has been made the use of the actual spending levels and the budgeted levels
©Indirapuram Institute of Higher Studies (IIHS)
A Bi-Annually Double-Blind Peer Reviewed, Open Access National e-Journal  2

HYPOTHESIS -National Journal of Research in Higher Studies  ISSN-2581-8953
Volume VIII, Issue 2, July 2025– December 2025
| for financial | control and | proper management     | by the user.         |     |     |     |     |     |
| ------------- | ----------- | --------------------- | -------------------- | --- | --- | --- | --- | --- |
| The process   | of data     | analysis enables      | the use of financial |     |     |     |     |     |
| information   | for proper  | financial management. |                      |     |     |     |     |     |
Fig.2. WorkflowoftheSmartPersonalFinanceAssistantillustratingincome
andexpensedataentry,processing,andfinancialanalysisthroughacentralized
Fig.4. ConceptualComparisonofTraditionalBudgetingandSmartPersonal
system.
FinanceAssistant
|     |     |     |     | able to         | estimate financial | balances as well | as savings  | rates.   |
| --- | --- | --- | --- | --------------- | ------------------ | ---------------- | ----------- | -------- |
|     |     |     |     | Other financial | disciplines        | offered by the   | system      | included |
|     |     |     |     | notifications   | for expenditures   | reaching certain | thresholds. |          |
Fig.3. Expensetrackingandbudgetanalysisprocessillustratingtransaction
categorization,datavisualization,andfinancialinsightgeneration.
VI. RESULTSANDDISCUSSION
| On the    | basis of the       | analysis of the | results that have |        |                                          |     |     |     |
| --------- | ------------------ | --------------- | ----------------- | ------ | ---------------------------------------- | --- | --- | --- |
|           |                    |                 |                   | Fig.5. | ExpenseTrackingandBudgetAnalysisOverTime |     |     |     |
| come from | the implementation | of the Smart    | Personal Finance  |        |                                          |     |     |     |
Assistant, it can be seen that it is effective in handling the Conclusion Conclusion of the study indicates that code
personal finance of the users of the system as it increases the execution and visualization as well as code editing in a single
awareness regarding expenditure. The users have been able interface help with the constant exploration and comprehen-
to keep proper records of the income and expenditure, which sionofaprogram.TheinterfacedesignofCodePaleffectively
helps in maintaining organized financial documentation. incorporates the principles of visualization with the needs for
| What | becomes evident | from the data | analyzed is that the | the new | learners. |     |     |     |
| ---- | --------------- | ------------- | -------------------- | ------- | --------- | --- | --- | --- |
segmentation of expenses and the graphical presentation of Onthewhole,thefindingshavesubstantiatedthattheSmart
the data had an immense impact on users being able to better PersonalFinanceAssistantSystemoffersaneffectivemeansto
understandtheirownspendingpatterns.Graphssuchascharts efficientlymanagepersonalfinances.Thediscussionpointsout
andmonthlysummariesenableduserstoquicklydetectthekey thatsimplicity,easyinterpretation,andorganizedanalysisplay
spending categories and points of unnecessary spending. importantrolesinimprovingfinancialawarenessanddecision-
The system was also effective in providing insightful finan- making. The proposed system has successfully eliminated the
cialreportsinreal-time.Byvirtueofcomparisonsofrevenues disparity between financial figures and meaningful insights,
and expenditures conducted on a monthly basis, one was making it easier to manage personal finances.
©Indirapuram Institute of Higher Studies (IIHS)
A Bi-Annually Double-Blind Peer Reviewed, Open Access National e-Journal  3

HYPOTHESIS -National Journal of Research in Higher Studies ISSN-2581-8953
Volume VIII, Issue 2, July 2025– December 2025
VII. CONCLUSIONANDFUTURESCOPE secure on multiple devices of user accounts, and linkages of
financial services within accounts or electronic wallets. The
This research work aimed at proposing the design of Smart
Smart Personal Finance Assistant has tremendous potential
Personal Finance Assistant. The assistant proposed has been
in helping build an overall personal financial administration
found valuable and beneficial as it will help users track
system.
their expenses and budget their money effectively in making
appropriate financial decisions. The proposed system proves
ACKNOWLEDGMENT
to be extremely beneficial as it allows users to handle their
TheauthorsareverymuchobligedtoDr.J.N.Singhforhis
incomesaswellasexpenseseffectivelybyusingthisassistant
valuableguidance,support,andconstructivecomments,which
only. The assistant proposed appears user-friendly as it will
played an important role in completing this research work.
assist users in making effective budgeting decisions, requiring
The authors are also appreciative of all the faculty members
no specialized knowledge in finance and technology.
of the Computer Science and Engineering Department of
Thefindingsalsoconfirmthatthenewsystemiscapableof
Galgotias University for their support. The authors gratefully
successfully enhancing financial awareness by utilizing capa-
acknowledge Galgotias University for providing an excellent
bilitiesthatcanturnsimplefinancialinformationintographical
environment to carry out this research.
representations that have the ability to be informative. By
utilizing capabilities that can automatically categorize expen- REFERENCES
ditures based on certain descriptions, compare income and
[1] J. Xiao and J. J. Ahn, “Financial literacy and personal financial man-
expendituresonamonth-to-monthbasis,andmanagebudgets, agementbehavior,”InternationalJournalofConsumerStudies,vol.42,
an individual can distinguish between unreasonable expendi- no.2,pp.127–136,2018.
tures and maintain financial discipline.Adding the K-Means [2] A.LusardiandO.S.Mitchell,“Theeconomicimportanceoffinancial
literacy,”JournalofEconomicLiterature,vol.52,no.1,pp.5–44,2014.
clustering algorithm techniques reinforces the system even
[3] S. Agarwal, J. C. Driscoll, X. Gabaix, and D. Laibson, “The age of
further, as this tool helps individuals pinpoint the dominant reason: Financial decisions over the life cycle,” Brookings Papers on
patterns of expenditures and group connected expenditures
EconomicActivity,pp.51–117,2009.
[4] M. Hilgert, J. Hogarth, and S. Beverly, “Household financial man-
based on individuals’ patterns of spending. agement: The connection between knowledge and behavior,” Federal
ReserveBulletin,vol.89,no.7,pp.309–322,2003.
[5] P.G.N.KumariandR.Shree,“Astudyonpersonalfinancemanagement
usingdigitaltools,”InternationalJournalofComputerApplications,vol.
176,no.22,pp.1–6,2020.
[6] R.ThalerandC.Sunstein,Nudge:ImprovingDecisionsAboutHealth,
Wealth,andHappiness.YaleUniversityPress,2008.
[7] M. S. Kim, “Personal finance management systems and user behavior
analysis,” Journal of Information Systems, vol. 34, no. 2, pp. 45–58,
2019.
[8] A.SinghandP.Sharma,“Digitalexpensetrackingandbudgetplanning
applications,”InternationalJournalofAdvancedResearchinComputer
Science,vol.11,no.4,pp.112–118,2020.
[9] J. Manyika et al., “Digital finance and financial inclusion,” McKinsey
GlobalInstituteReport,pp.1–40,2016.
[10] S. S. Gupta and N. Kaur, “Analysis of budgeting tools for personal
financemanagement,”InternationalJournalofEngineeringResearch&
Technology,vol.9,no.6,pp.890–895,2020.
[11] T.O’Reilly,DesigningWebApplications.O’ReillyMedia,2018.
[12] E. Brown, Web Development with Node and Express. O’Reilly Media,
2019.
[13] A.BanksandE.Porcello,LearningReact:ModernPatternsforDevel-
opingReactApps.O’ReillyMedia,2020.
[14] R. Fielding, “Architectural styles and the design of network-based
software architectures,” Ph.D. dissertation, University of California,
Fig.6. FutureScopeoftheSmartPersonalFinanceAssistant Irvine,2000.
[15] J. Nielsen, “Usability engineering and user-centered design,” IEEE
The future work that needs to be done through this system
Computer,vol.28,no.7,pp.66–72,1995.
is going to involve the integration of more sophisticated
analytic tools so that financial analysis support can be further
improved. Features that need to be incorporated in order to
improvethisfinancialanalysissystemincludepersonalbudget
suggestion tools, more sophisticated text analysis tools for
complexdescriptionanalysisoftransactions,andmoreflexible
clustering tools that can help enhance the usefulness of this
financial analysis system. Some of the features that can be
incorporated in this financial system include the integration
of support within the mobile application context, multi-user
capabilities, synchronization of financial information that is
©Indirapuram Institute of Higher Studies (IIHS)
A Bi-Annually Double-Blind Peer Reviewed, Open Access National e-Journal 4