TechnologyinSociety77(2024)102599
Contents lists available at ScienceDirect
Technology in Society
journal homepage: www.elsevier.com/locate/techsoc
Optimizing financial decision-making for emerging adults: A compact
Python-based personalized financial projection approach
Alex Yue Feng Zhu*
Department of Social Sciences and Policy Studies, The Education University of Hong Kong, Hong Kong SAR, China
A R T I C L E I N F O A B S T R A C T
Keywords: The financial decisions made by emerging adults significantly influence their long-term financial well-being. To
Financial education make effective decisions, they need both financial literacy and a forward-looking mindset. However, existing
Python literature lacks tailored financial interventions for this demographic. Addressing this gap, our study implemented
Personalized financial projection
and evaluated a Python-based Personalized Financial Projection (PFP) among emerging adults in Hong Kong.
Interactive AI
Our findings indicate that the Python-based PFP effectively promoted prudent financial behaviors by enhancing
Financial literacy
participants’ perceived financial literacy and future time perspectives. This represents a significant advancement,
Future time perspectives
providing the first empirical evidence supporting the integration of computer programming into financial edu-
cation initiatives. In an era of interactive Artificial Intelligence (AI) for financial guidance, the Python-based PFP
stands out as a pivotal resource capable of leveraging interactive AI to enhance financial decision-making
processes.
1. Introduction Among various financial education approaches, personalized finan-
cial projection (PFP) shows promise in promoting future time perspec-
Making intelligent financial decisions during emerging adulthood is tive and understanding of compound interest [10–14]. Typically, PFPs
crucial, as these choices significantly influence an individual’s long-term involve a mobile application where participants input parameters such
financial well-being. Unlike adolescents, emerging adults have greater as current income, present wealth, saving behaviors, and investment
control over their finances. However, irresponsible credit behaviors, portfolio. The application then projects the total wealth participants can
such as late payment of credit card bills, can harm their credit records expect to accumulate in the future based on their inputs.
and negatively impact long-term financial health [1–3]. Additionally,
the decision to enter the labor market or pursue higher education after
1.1. Previous research of our team
high school graduation leads emerging adults onto different life paths.
Making correct financial decisions during this period contributes to
sustainable personal wealth growth throughout life [4–6]. Our team recently introduced PFP to middle-aged working adults
aged 36(cid:0) 55 in Hong Kong and conducted randomized controlled trials,
Given the importance of promoting future-oriented financial be-
finding that PFP significantly promoted future time perspectives and
haviors and avoiding shortsighted decisions during emerging adulthood,
financial planning in the short, medium, and long terms[15]. Post-hoc
financial education targeting this age group should emphasize the power
of compound interest—a vital component of financial literacy that il- analysis, dividing the sample into younger and older subsamples,
lustrates the future value and cost of money—and foster a future time revealed more pronounced effects among the younger subsample, sug-
gesting potentially increased effectiveness of PFP among young working
perspective (optimistic outlook on the future) to encourage forward-
adults. Additionally, we noted that PFP implemented through a mobile
thinking financial decisions [7,8]. However, a comprehensive review
app has limitations in promoting financial literacy since users only see
reveals that there are significantly fewer validated financial education
the projection outcomes without understanding the underlying calcu-
programs designed specifically for emerging adults compared to those
lations. Furthermore, a mobile app-based PFP has limitations in strongly
for children and adolescents, especially programs that address both
affecting participants’ future time perspectives because it does not allow
financial literacy and future time perspectives [9].
for model adjustments based on specific participant situations.
* SSPS, The EdUHK, 10 Lo Ping Road, Tai Po, New Territories, Hong Kong Special Administrative Region, PRC.
E-mail address: yfzhu@eduhk.hk.
https://doi.org/10.1016/j.techsoc.2024.102599
Received 23 December 2023; Received in revised form 22 May 2024; Accepted 22 May 2024
Availableonline23May2024
0160-791X/©2024TheAuthor.PublishedbyElsevierLtd.ThisisanopenaccessarticleundertheCCBYlicense(http://creativecommons.org/licenses/by/4.0/).

A.Y.F. Zhu T e c h n o l o g y i n S o c i e ty77(2024)102599
To address these limitations—participant age and the mobile app’s human cognition [24]. When contemplating an uncertain future, in-
deficiencies—we employed a Python-based PFP in a subsequent exper- dividuals instinctively ponder the ramifications of altering initial con-
iment, targeting young working adults aged 18–35 [16]. Python serves ditions on the ensuing outcomes [25]. Thus, the adoption of
as a user-friendly programming tool, enabling participants to under- counterfactual design holds promise in bolstering users’ trust in pro-
stand the PFP mechanisms at a low cost [17]. Thus, Python was used to jection outputs and effecting genuine changes in their financial attitudes
familiarize young working adults with the coding behind PFP [16]. Our and decision-making.
findings revealed that this initial Python-based PFP significantly Our Python-based PFP embodies a counterfactual framework, as we
improved financial planning, but the impact was modest and not furnish users with the requisite coding, empowering them to compre-
mediated by enhanced financial literacy or heightened future time hend and fine-tune projection parameters, thereby yielding a myriad of
perspectives [16]. counterfactual results. Consequently, if the Python-based PFP proves
Participant feedback highlighted several factors limiting the initial efficacious, it heralds a novel avenue for enhancing trust in interactive
version’s efficacy. Firstly, participants over 30 found Python coding AI and shaping financial dispositions and behaviors. In future pro-
more challenging. Secondly, the intervention’s duration (7 h) was jections, users may opt to solicit interactive AI to generate intelligible
excessive, leading to fatigue, with 5 h dedicated to basic Python coding and potent financial projection “codes”, instead of merely requesting
and only 2 h to projection exercises. Thirdly, the projection models were projection outcomes. It is widely acknowledged that interactive AI ex-
overly generalized and did not adequately address specific financial cels in crafting highly structured projection codes. For users, the
decisions relevant to young adults, such as postgraduate education in- unveiling of the black box underlying the projection model imbues the
vestments and housing loans. projection process with greater credibility and persuasiveness, with the
salient limitations of interactive AI poised to be rectified.
1.2. This current research
2.1.2. Importance of introducing Python-based PFP to emerging adults in
In response, this study developed a concise and refined Python-based Hong Kong
PFP, reducing the duration to 120 min, with only 45 min for basic Py- Recent evidence highlights the unpreparedness of emerging adults in
thon coding instruction, allowing more time for Python-based PFP tasks. Hong Kong to face the challenges of the post-pandemic economic
This version features themed projection models providing advice on key landscape. Their financial behaviors often lack a future-oriented
financial decisions for emerging adults, such as housing loans and perspective, and their decision-making skills in managing finances are
tuition fees for higher education. We specifically limited participants to insufficient, potentially leading to a decline in their financial well-being.
college students aged 18–30, ensuring the inclusion of young digital A report by the Investor and Financial Education Council (IFEC) in
natives who found learning Python coding relatively easy. The primary March 2020 reveals that only about half of young working adults in
aim of this research was to conduct a randomized controlled trial to Hong Kong set financial goals and prepare for financial emergencies,
determine whether the concise Python-based PFP significantly enhanced compared to 82 % of mature working adults. The report also indicates
financial literacy, future time perspective, and forward-thinking finan- that 35 % of young people were more likely to overspend, exceeding
cial decision-making. their financial means, compared to approximately 20 % of the general
population [26]. Furthermore, 32 % of young individuals were
2. Literature review burdened by debt, whereas only 12 % of the general respondents re-
ported the same [26]. In terms of financial services, young people
2.1. Background exhibited riskier behavior, with 27 % admitting to making only mini-
mum payments on their credit card bills, compared to just 7 % of the
2.1.1. Importance of Python-based PFP in the era of interactive artificial general population [26]. Consequently, only 23 % of young working
intelligence adults expressed satisfaction with their financial status, in contrast to 39
The rapid evolution and refinement of interactive artificial intelli- % of all respondents. These statistics have raised concerns among edu-
gence (Interactive AI) models empower users to project their financial cators, emphasizing the need for financial education to enhance finan-
trajectories and make real-time financial decisions informed by readily cial literacy, future time perspectives, and healthy financial practices
available information garnered through dialogue. Nonetheless, the among emerging adults.
inherent opacity of these complex models, characterized by their “black However, the latest systematic review suggests that most validated
box” nature, impedes users from delving into the technical intricacies financial education programs internationally are standardized courses
and detailed processes underpinning the projections [18,19]. This lack primarily targeting children and adolescents, while the number of
of transparency may erode “trust” in the models for several reasons. validated financial education programs for emerging adults remains
Firstly, users may harbor concerns about the algorithm’s ability to limited, with mixed effects [9]. Unlike adolescents, implementing
accurately encapsulate various economic life events in a manner deemed full-length standardized financial education programs among emerging
equitable [20]. Secondly, the majority of users lack proficiency in adults is challenging due to their demanding schedules. Research in-
computer programming and the fundamental tenets of embedded dicates that financial interventions during emerging adulthood should
mathematical models, rendering it arduous for them to bridge the gap be topic-specific and have clear objectives aimed at enhancing specific
between the projection outcomes generated by interactive AI and their aspects of financial well-being. In this context, Python-based PFP, with
practical implications in daily life [21]. Consequently, the resultant its clear objectives of promoting an understanding of compound interest,
deficit in trust may hinder the efficacy of AI-driven messages in shaping fostering future time perspectives, and motivating future-oriented
users’ financial attitudes, decisions and behaviors. financial behaviors, appears to be a timely approach that financial ed-
To redress this lacuna, recent scholarship advocates for developers to ucators and practitioners in Hong Kong should consider.
elucidate the inner workings of projection models to engender trust
among users [20]. However, extant proposed remedies, such as visual- 2.2. Intervention mechanism of Python-based PFP
izing underlying mechanisms and deploying attention-based explana-
tions, cater more to users already versed in the intricacies of projection 2.2.1. Effects of Python-based PFP on future time perspectives
models, rather than lay users seeking applicability to their own contexts People typically do not actively think about or invest in the future
[22,23]. In a novel approach, recent studies posit that employing a when they perceive it as uncertain [27,28]. When individuals believe
“counterfactual” design proves most efficacious in elucidating projec- the future is filled with uncertainties, they tend to disconnect current
tion models to users, as it aligns with the logical reasoning inherent in decisions from future outcomes. This psychological disconnection, as
2

A.Y.F. Zhu T e c h n o l o g y i n S o c i e ty77(2024)102599
conceptualized by Bartels and Urminsky [29], raises concerns among assessed financial literacy through subjective financial understanding
behavioral scientists. Such disconnection reduces the likelihood of (perceived financial literacy) rather than objective financial knowledge.
engaging in future-oriented behaviors, including physical exercise, Due to the limited duration of the intervention project, we were only
maintaining a healthy diet, and practicing sound financial behaviors able to measure the immediate effects of Python-based PFP and could
such as regular saving, budgeting, spending control, and avoiding debt not track the medium- and long-term effects. Since immediate changes
[30]. in financial behaviors may not be readily detectable, we utilized three
Previous initiatives have employed various technologies to establish instrumental variables as substitutes for financial behaviors: financial
a link between an individual’s present and future selves [31–33]. These behavioral control, tendency to engage in healthy financial behaviors,
initiatives aim to enhance participants’ future time perspectives by and life satisfaction. Previous studies conducted in Hong Kong and other
making the future more vivid based on present information. For economies have demonstrated significant and positive correlations be-
example, age-progressed renderings [33,34] generate a visual repre- tween these constructs and financial behaviors among emerging adults
sentation of the future self by applying changes in facial parameters that [38–40]. By incorporating these variables, we strengthened the
typically occur during the aging process (e.g., skin laxity). These ren- robustness of our findings. Fig. 1 illustrates the hypothetical relation-
derings serve as a bridge between the present and future images. Simi- ships between Python-based PFP and the five outcome constructs, based
larly, AI can create a future-self based on current parameters and enable on the established pathways in previous investigations [38–40]. Upon
communication between the current and future selves [31,32]. Addi- reviewing the hierarchical structure depicted in Fig. 1, the primary focus
tionally, PFPs have gained popularity as a means of forecasting users’ of this research was to examine the effectiveness and mechanism of
future financial status by incorporating their current financial behaviors Python-based PFP. Specifically, our hypotheses were as follows:
and simulating market fluctuations [10–14]. Empirical findings strongly
support the effectiveness of age-progressed renderings, future-self (cid:0) Python-based PFP improves perceived financial literacy, future time
communication, and PFPs in promoting future time perspectives [13, perspectives, financial behavioral control, tendency to engage in
14,31,32]. Given that the Python-based PFP is essentially a form of PFP, healthy financial behaviors, and life satisfaction, respectively (Hy-
it incorporates all the features associated with PFPs and is expected to pothesis 1);
cultivate an optimistic outlook towards the future. (cid:0) Python-based PFP enhances the tendency to engage in healthy
financial behaviors through the mediating effects of perceived
2.2.2. Effects of Python-based PFP on financial literacy financial literacy, future time perspectives, and financial behavioral
The widely accepted “big-three” measurement of financial literacy control (Hypothesis 2);
emphasizes the importance of understanding compound interest, infla- (cid:0) Python-based PFP promotes life satisfaction by mediating an
tion, and risk diversification [35]. In this study, one objective of increased tendency to engage in healthy financial behaviors (Hy-
implementing Python-based PFP was to enhance the understanding of pothesis 3).
compound interest component of financial literacy. Krishnamurthy and
Sujan [36] highlighted a common issue in compound interest: In- 3. Method
dividuals often fail to grasp how savings and debts grow exponentially
through compound interest provided by commercial banks [36]. Simi- 3.1. General design
larly, McKenzie and Liersch [37] discovered that people tend to
consistently underestimate the exponential growth of savings and debts To ensure the suitability of participants for the Python-based PFP
due to their limited financial literacy. One possible reason is that the targeting emerging adults in Hong Kong, we established specific
human brain struggles to calculate comprehensively the long-term ef- recruitment criteria: 1) Participants had to be between 18 and 30 years
fects of compound interest on the accumulation of wealth or debt [29]. of age, 2) They should not be majoring in finance or computer science, 3)
In this context, the advantages of Python-based PFP in promoting They should have no prior completion of standardized financial courses,
financial literacy become evident. and 4) They should have no proficiency in Python programming.
First, participants are guided to input the correct compound interest Recruitment was restricted to a humanities and social sciences public
formula, enabling them to simulate the exponential growth of personal university in Hong Kong, based on the likelihood that their full-time
savings and debts. Through multiple simulation rounds, participants can students would meet these criteria.
observe significant and “surprising” growth of their savings or debts, Among the participants, we assessed five outcome variables:
thereby gaining a firsthand understanding of the power of compound perceived financial literacy, future time perspectives, financial behav-
interest. Second, Python-based PFP can provide participants with the ioral control, tendency to perform healthy financial behaviors, and life
accumulated savings or debts at the end of each simulation round, satisfaction. To evaluate the effects of the Python-based PFP on these
facilitating their comprehension of how compound interest drives constructs, we conducted a two-arm randomized control trial, randomly
exponential growth over time. Third, participants have the opportunity assigning participants to either the experimental or control group. All
to adjust critical parameters, such as increasing their monthly savings, participants were invited to participate in the assessment of outcome
allowing them to witness how their choices can further amplify the variables at two time points: pretest and posttest.
impact of compound interest. Considering these advantages, we believe
that Python-based PFP has the potential to significantly enhance par- 3.2. Procedures
ticipants’ financial literacy. By actively engaging with the simulation,
participants can develop a deeper understanding of compound interest The Registry section of the university sent mass invitations via bulk
and its profound influence on their financial well-being. email to full-time undergraduate and postgraduate students, aiming to
recruit participants for our research. Participants who completed the
2.2.3. Hypothetical model pretest, posttest, and intervention received a Cash Coupon worth HK
Based on the theoretical discussion above, this study aimed to $100. We successfully recruited 78 participants from the campus com-
investigate the impact of Python-based PFP on financial literacy, future munity, randomly assigning 40 to the experimental group and 38 to the
time perspectives, and financial behaviors among emerging adults, control group.
while considering the mediating role of financial literacy and future time Participants in the experimental group could choose one of three
perspectives. These three outcome variables were of utmost importance intervention sessions, each focusing on Python-based PFP. Assignment
for our evaluation. Given the absence of a formally validated assessment to a specific session was based on participants’ preferences, with an
tool for financial literacy among emerging adults in Hong Kong, we effort to ensure a balanced distribution of approximately 13–15
3

A.Y.F. Zhu T e c h n o l o g y i n S o c i e ty77(2024)102599
Fig. 1. Hypothesized working mechanism of Python-based personalized financial projection.
participants per session. Students participated in a baseline assessment five-point scale, ranging from 1 (strongly disagree) to 5 (strongly agree).
before the training and a posttest after the training to eliminate potential The internal consistencies for the pretest and posttest scores were 0.87
attrition bias. They were informed during the baseline test that they and 0.91, respectively. The mean score of the five items was calculated
could withdraw from the research at any stage without providing a to reflect participants’ life satisfaction.
reason.
The three sessions of Python-based PFP training took place on 27th
3.4. Design of Python-based PFP
February, 1st March, and March 2, 2023, in computer labs, with each
participant having access to an individual computer. Meanwhile, the 38
Participants underwent a comprehensive 45-min training session,
students assigned to the control group attended an unrelated statistics
where they received instruction in fundamental coding skills and the
course on 29th March, providing a contrasting experience. Ethical
grammatical rules of Python. Following this, they participated in a 75-
approval was obtained from the Research Committee of Lingnan Uni-
min session involving Python-based personalized financial projections.
versity (Hong Kong) for conducting the data collection, underscoring
Our research team developed three distinct financial projection models
our commitment to upholding research ethics and protocols.
using Python, focusing on critical financial decisions during emerging
adulthood: housing mortgages, education tuition loans, and regular
savings. These models aimed to simulate the impact of these decisions on
3.3. Measures
participants’ financial well-being in both the near and distant future.
Equipped with basic Python coding skills, participants were
Perceived financial literacy was assessed by asking students to rate
encouraged to modify key parameters within the models to observe the
their understanding of financial knowledge on a seven-point scale,
far-reaching consequences of their current debt and saving behaviors.
ranging from 1 (lowest level) to 7 (highest level). We utilized six ques-
The housing mortgage projection model provided insights into the true
tions adapted from Tomar et al. [41], originally developed by Koposko
cost of owning an apartment throughout one’s life, considering factors
and Hershey [42], to measure future time perspectives. Example items
included statements such as “I look forward to life in the distant future” such as interest payments to a commercial bank. By working with this
and “My friends describe me as future-oriented.” These items were model, participants could see how an imprudent decision to buy a house
adjusted to a five-point Likert scale, where 1 represented “strongly could negatively impact future cash flows, delaying their attainment of
disagree” and 5 represented “strongly agree.” The Cronbach’s Alpha financial independence.
The tuition loan projection model presented the actual cost of
reliability coefficients for all six items were 0.88 for the pretest and 0.91
investing in higher education degrees, incorporating interest expenses.
for the posttest. The mean score of the six items was calculated to
determine participants’ future time perspectives. This model enabled students to make economically prudent choices
aligned with their families’ financial circumstances and their antici-
Financial behavioral control was assessed using one item from Xiao
pated future income. Additionally, students gained insights into the
et al. [43] and three items developed by our research team. Participants
potential repercussions of selecting inappropriate degree programs,
rated how easy or difficult it was for them to stick to their financial plans
which could lead to significant debt burdens.
on a five-point scale, ranging from 1 (very difficult) to 5 (very easy). The
The savings projection model emphasized the importance of early
internal consistencies for the pretest and posttest scores were 0.91 and
engagement in regular savings, highlighting how it can lead to greater
0.93, respectively. The mean score of the four items was computed to
wealth accumulation in the future. Collectively, these Python-based PFP
represent financial behavioral control.
models provided participants with practical knowledge and tools to
To evaluate the tendency to perform healthy financial behaviors,
enhance their understanding of the long-term impacts of their present
participants indicated the extent to which they engaged in seven positive
financial decisions. Consequently, participants were empowered to
financial behaviors on a five-point scale ranging from 1 (strongly
make more informed choices and secure their financial well-being in the
disagree) to 5 (strongly agree). The behaviors included saving regularly,
future.
tracking monthly expenses, spending within a budget, maintaining an
adequate balance in their bank account, saving for emergencies, saving
for the future, and investing regularly. These items were adapted from 3.5. Data analysis
Shim et al. [38] and Xiao et al. [44]. The internal consistencies for the
pretest and posttest scores were 0.81 and 0.85, respectively. The mean To ensure the validity of the group assignments (control group vs.
score of the seven items was calculated to determine participants’ ten- experimental group), we conducted a comprehensive set of statistical
dencies toward healthy financial behaviors. tests to assess any significant differences between the two groups in
Life satisfaction was measured using five items validated among terms of outcome and background variables. Specifically, we employed
college students in Hong Kong by Sachs [45]. Sample items include “In independent t-tests to compare the means of continuous variables across
most ways, my life is close to my ideal” and “So far, I have achieved the the two groups, including age, monthly household income, household
important things I want in life.” Responses were calibrated on a size, perceived financial literacy, future time perspectives, financial
4

A.Y.F. Zhu                                                                                                                                                                                                            T  e c  h  n o  l o  g y   i n   S  o c  i e ty77(2024)102599
| behavioral control, tendency to perform healthy financial behaviors,  |     |     |     | Table 2  |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- |
and life satisfaction. Additionally, we used the chi-square test to  Results of experiment-based multiple linear regression models.
examine gender proportion differences between the experimental and
|                  |     |     |     |     | Posttest score  | Posttest score of  | Posttest score  |
| ---------------- | --- | --- | --- | --- | --------------- | ------------------ | --------------- |
| control groups.  |     |     |     |     | of perceived    | future time        | of financial    |
|                  |     |     |     |     | financial       | perspectives       | behavioral      |
For our principal analysis, we utilized multiple regression analysis to
|     |     |     |     |     | literacy  |     | control  |
| --- | --- | --- | --- | --- | --------- | --- | -------- |
determine whether participants in the experimental group reported
|     |     |     |     |     | 0.16c  0.18b  | 0.23c  0.13a  | 0.15c  0.14a  |
| --- | --- | --- | --- | --- | ------------- | ------------- | ------------- |
higher levels of perceived financial literacy, greater future time per- Joining the intervention
|     |     |     |     |     | 0.83c  0.07c  | 0.72c  | 0.78c  0.75c  |
| --- | --- | --- | --- | --- | ------------- | ------ | ------------- |
spectives, increased financial behavioral control, a stronger tendency to  Baseline score of outcome  0.66
variable
engage in healthy financial behaviors, and higher life satisfaction
|     |     |     |     | Being male   | 0.17b   | (cid:0) 0.02   | 0.20c  |
| --- | --- | --- | --- | ------------ | ------- | -------------- | ------ |
compared to those in the control group. It was crucial to control for the  (cid:0) 0.26c   (cid:0)
|     |     |     |     | Age   | 0.03   |     | 0.05  |
| --- | --- | --- | --- | ----- | ------ | --- | ----- |
baseline status of these key constructs to ensure robust analysis.  Family income   0.05   (cid:0) 0.10   (cid:0) 0.04
Furthermore, we included relevant background variables in the regres- Household size   0.09   (cid:0) 0.13   0.01
sion model to validate the results and account for any potential con-
|     |     |     |     |     | Posttest score of  |     | Posttest score of  |
| --- | --- | --- | --- | --- | ------------------ | --- | ------------------ |
founding factors. Subsequently, we incorporated the pretest and posttest  tendency to perform  life satisfaction
healthy financial
data into a structural model to evaluate the mechanism of the Python-
behaviors
based PFP, specifically examining how it influenced the five outcome
|     |     |     |     | Joining the intervention  | 0.18c  | 0.20c  | 0.19b  0.20b  |
| --- | --- | --- | --- | ------------------------- | ------ | ------ | ------------- |
variables in sequence.
|     |     |     |     | Baseline score of outcome variable  | 0.82c  | 0.85c          | 0.68c  0.68c  |
| --- | --- | --- | --- | ----------------------------------- | ------ | -------------- | ------------- |
|     |     |     |     | Being male                          |        | (cid:0) 0.03   | 0.05          |
4. Results
|     |     |     |     | Age             |     | 0.02           | 0.02  |
| --- | --- | --- | --- | --------------- | --- | -------------- | ----- |
|     |     |     |     | Family income   |     | (cid:0) 0.03   | 0.03  |
Table 1 presents the results of the chi-square and t-tests, indicating  Household size   (cid:0) 0.14b   0.02
no significant differences across all variables, except for age (which was  Note. N =78. Standardized estimated coefficients are reported.
| controlled for in the main analysis), between the experimental group (N  |     |     |     | a p ≤0.10.  |     |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | ----------- | --- | --- | --- |
| =40) and the control group (N =38). This confirms the effectiveness of   |     |     |     | b p ≤0.05.  |     |     |     |
| our group assignment. Table 2 shows that the Python-based PFP had the    |     |     |     | c p ≤0.01.  |     |     |     |
anticipated positive impact on all outcome variables. Initially, without
controlling  for  background  variables,  the  experimental  condition  0.01), respectively, partially supporting the Hypothesis 2. Secondly, the
demonstrated significant improvements in perceived financial literacy  impact of Python-based PFP on life satisfaction was partially mediated
| (β = 0.16, p < | 0.01), future time perspectives (β = |     | 0.23, p < |     |     |     |     |
| -------------- | ------------------------------------ | --- | --------- | --- | --- | --- | --- |
0.01),  by increases in perceived financial literacy and the tendency to perform
financial behavioral control (β =0.15, p <0.01), tendency to perform  healthy financial behaviors (β =0.17, p <0.01; β =0.13, p =0.05; β =
healthy financial behaviors (β =0.18, p <0.01), and life satisfaction (β  0.34, p < 0.01). Additionally, the influence on life satisfaction was
=0.19, p <0.05). When background variables were included as con- partially mediated by improved future time perspectives and the ten-
trols, all effects remained significant and positive. Specifically, signifi- dency to perform healthy financial behaviors (β =0.24, p <0.01; β =
cant enhancements were observed in perceived financial literacy (β = 0.22, p < 0.01; β = 0.34, p <
0.01). Thus, the Hypothesis 3 is well
0.18, p <0.05), future time perspectives (β =0.13, p <0.10), financial
supported. Thirdly, the direct effect of the intervention on financial
behavioral control (β =0.14, p <0.10), tendency to perform healthy
behavioral control disappeared when controlling for perceived financial
financial behaviors (β =0.20, p <0.01), and life satisfaction (β =0.20, p
literacy and future time perspectives as predictors of financial behav-
<0.05). Therefore, the Hypothesis 1 is fully supported.
ioral control. These findings highlight the multifaceted impact of
Fig. 2 presents the results of the structural models, illustrating the  Python-based PFP on enhancing financial literacy, future time per-
estimated coefficients of all direct and indirect paths from the inter- spectives, and financial behaviors, ultimately contributing to greater life
vention to the outcome variables. Three key observations emerge from  satisfaction among emerging adults in Hong Kong.
the findings. Firstly, the effect of Python-based PFP on the tendency to
| perform healthy financial behaviors was fully mediated by increases in  |     |     |     | 5. Discussion  |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
perceived financial literacy (β =0.17, p <0.01; β =0.13, p =0.05) and
improved future time perspectives (β =0.24, p <0.01; β =0.22, p <
This study implemented a Python-based personalized financial pro-
jection for emerging adults in Hong Kong. The positive findings from the
randomized control trial suggest that Python-based PFP is a timely and
Table 1
Descriptive statistics of the control and experimental groups.    effective  approach  to  addressing  short-sighted  financial  decision-
making among emerging adults, particularly in the post-pandemic
|     |     | Control group  | Experimental group  |     |     |     |     |
| --- | --- | -------------- | ------------------- | --- | --- | --- | --- |
economic context. This intervention can facilitate financial indepen-
|     |     | (N =38)  | (N =40)  |     |     |     |     |
| --- | --- | -------- | -------- | --- | --- | --- | --- |
dence and secure long-term financial well-being. The study advances the
%/mean (standard deviation)  theories and practice of personal finance education in four main aspects.
Male (%)  47.4  40.0  First, the demonstrated effectiveness of Python-based PFP may
Age  26.11 (3.52)b  22.97 (3.41)b  encourage  future  studies  to  further  integrate  “computer-assisted
Family incomea (Range: 1(cid:0)
8)  3.33 (2.28)  3.29 (2.14)  learning” into financial education. This research is a pioneering effort to
| Household size  |     | 3.08 (0.89)  | 3.27 (0.96)  |     |     |     |     |
| --------------- | --- | ------------ | ------------ | --- | --- | --- | --- |
Perceived financial literacy (Range:  3.87 (1.30)  4.13 (1.27)  incorporate programming into financial education on an international
1(cid:0)
7)  scale. Our promising findings may inspire other scholars to replicate this
| Future time perspectives (Range: 1(cid:0) |     | 5)  3.93 (0.61)  | 4.10 (0.74)  |     |     |     |     |
| ----------------------------------------- | --- | ---------------- | ------------ | --- | --- | --- | --- |
study or develop additional programming-based financial education
| Perceived behavioral control (Range:  |     | 3.13 (0.90)  | 2.97 (0.81)  |     |     |     |     |
| ------------------------------------- | --- | ------------ | ------------ | --- | --- | --- | --- |
modules. While Humber [17] developed personal finance management
1(cid:0) 5)
modules with Python and suggested their extension to young consumers,
| Tendency of performing healthy  |     | 3.70 (0.55)  | 3.63 (0.64)  |     |     |     |     |
| ------------------------------- | --- | ------------ | ------------ | --- | --- | --- | --- |
financial behaviors (Range: 1(cid:0) 5)  there has been no formal experiment-based assessment to validate the
Life satisfaction (Range: 1(cid:0) 5)  3.27 (0.85)  3.14 (0.77)  effects of Python-based financial modules on users’ knowledge and be-
haviors. Thus, this research could be the first worldwide to test the
Note.
a Monthly family income ranged from 1 (HK$18,700 (cid:0) effectiveness of Python-based financial interventions through a ran-
HK$19,999) to 8 (HK
domized control trial.
$100,000 or above).
b p ≤0.01.
5

A.Y.F. Zhu T e c h n o l o g y i n S o c i e ty77(2024)102599
Fig. 2. Results of experiment-based structural model. Note. N =78. Standardized estimated coefficients are reported. *p ≤0.10; **p ≤0.05; ***p ≤0.01.
Second, the design and evaluation of Python-based PFP significantly the AI to generate Python-based projection code, rather than receiving
contribute to the development of “personalized” financial education. direct projection outcomes and financial recommendations. This pro-
Personalized financial education offers a unique advantage over generic jection code serves the dual purpose of elucidating the projection pro-
financial education by targeting underlying psychology to bring about cess to users and fostering their comprehension of the underlying
positive behavioral changes [10–14]. Instead of simply instructing mathematical principles and philosophies. Moreover, the provision of
participants with commonly accepted knowledge through standardized projection code empowers users to engage in scenario analysis, enabling
courses, personalized financial education guides participants to make them to simulate potential future scenarios by altering their current
the best choices based on their unique circumstances. While interactive decisions. This counterfactual approach mirrors human logical
mobile applications have activated the development of personalized reasoning and is poised to have a significant impact on altering cognitive
financial interventions (e.g., PFP), the combination of Python and PFP perceptions and attitudes [24]. In essence, the Python-based PFP serves
unleashes the full potential of PFP, allowing users to adjust settings and as a conduit to unlock the full potential of interactive AI in shaping
parameters according to their specific situations without any technical financial attitudes and, ultimately, enhancing users’ decision-making
limitations. In other words, Python-based PFP creates personalized capabilities.
financial projections that are more closely aligned with reality.
Third, the development of Python-based PFP offers a promising di- 5.1. Limitations
rection for financial education targeting emerging adults. Unlike chil-
dren and adolescents, who can undergo highly structured, While our contributions to personal finance and the personal finance
comprehensive financial education, emerging adults often have busy education framework are noteworthy, it is important to acknowledge
schedules and can only engage in topic-based financial training [9]. Our the limitations of this research, which provide strong motivation for
Python-based financial training, compared to previous initiatives for future studies to replicate or optimize the design. Firstly, a significant
young people, is more targeted and addresses a critical gap in their limitation of our study is the lack of a validated objective measure of
financial understanding, specifically the effects of compound interest. financial literacy that comprehensively covers saving, budgeting,
Our intervention helps emerging adults comprehend the real cost of borrowing, and investment among emerging adults. It is worth noting
debts and the benefits of savings over time, encouraging them to think that a considerable proportion of young people in Hong Kong tend to
about the future and engage in future-oriented financial behaviors. overestimate their financial literacy and exhibit financial over-
Python-based PFP can be seen as a cost-effective initiative for devel- confidence [46]. Therefore, the inclusion of an objective measure of
oping financial training for emerging adults, and its effectiveness may financial literacy would provide a more accurate assessment of partici-
inspire future research to develop more topic-specific financial educa- pants’ financial knowledge and skills, thus strengthening the overall
tion for young individuals. study design.
Fourth, the successful validation of Python-based PFP can signifi- Secondly, due to the limited duration of the project, we only exam-
cantly enhance the smart utilization of interactive AI for personalized ined the immediate effect of Python-based PFP. This design constraint
financial decision-making. In an era where interactive AI has garnered restricted our selection of outcome variables, as we had to exclude
widespread acceptance, users may naturally gravitate towards seeking constructs that require a longer time frame to detect changes, such as
financial projections or advice directly from such systems. However, the actual behavioral changes and objective measures of financial behaviors
opaque nature of the projection process and concerns regarding algo- (e.g., savings outcomes, debt levels, and number of credit cards held). To
rithmic fairness (e.g., the possibility that critical economic events may gain a more comprehensive understanding of the intervention’s impact,
not be equally accounted for throughout the projection) may lead users we recommend that future research optimize the study design by
to harbor reservations about the accuracy and reliability of the AI- incorporating multiple waves of post-intervention data collection. This
generated outcomes [18–20]. This potential lack of trust could under- would allow for the examination of the middle- and long-term effects of
mine the efficacy of AI-generated outcomes in influencing users’ Python-based PFP. Additionally, the inclusion of a broader range of
financial attitudes and behaviors. Our validated Python-based PFP offers outcome variables would enable a more sophisticated analysis of the
a smart approach to harnessing the power of interactive AI for financial intervention’s working mechanisms and provide a deeper understanding
decision-making. We advocate for a methodology wherein users request of how Python-based PFP improves the financial well-being of
6

A.Y.F. Zhu T e c h n o l o g y i n S o c i e ty77(2024)102599
participants. References
Thirdly, our sample consisted solely of individuals without any prior
programming experience because our study targeted a broad spectrum [1] K. Cherney, D. Rothwell, J. Serido, S. Shim, Subjective financial well-being during
emerging adulthood: the role of student debt, Emerg. Adulthood 8 (6) (2020)
of emerging adults. Nonetheless, it stands to reason that the Python- 485–495, https://doi.org/10.1177/21676968198792.
based PFP could hold even greater appeal among those proficient in [2] A.R. Thorson, H.A. Kranstuber Horstman, Buy now, pay later: family
programming. Their adeptness in coding may enable them to devise communication patterns theory, parental financial support, and emerging adults’
openness about credit card behaviors, J. Fam. Commun. 14 (1) (2014) 53–71,
more precise projection code, potentially yielding more profound psy-
https://doi.org/10.1080/15267431.2013.857324.
chological shifts and fostering more positive behavioral changes. In light [3] J.J. Xiao, N. Porto, I.M. Mason, Financial capability of student loan holders who are
of this, we advocate for future research endeavors to delve into the ef- college students, graduates, or dropouts, J. Consum. Aff. 54 (4) (2020) 1383–1401,
https://doi.org/10.1111/joca.12336.
ficacy of the Python-based PFP within a subset of the emerging adult
[4] G. Sinha, K. Tan, M. Zhan, Patterns of financial attributes and behaviors of
population—specifically, those with backgrounds and expertise in emerging adults in the United States, Child. Youth Serv. Rev. 93 (2018) 178–185,
computer science. By focusing on this cohort, researchers can explore https://doi.org/10.1016/j.childyouth.2018.07.023.
how their pre-existing coding skills moderate the effects of Python-based [5] E. Sinnewe, G. Nicholson, Healthy financial habits in young adults: an exploratory
study of the relationship between subjective financial literacy, engagement with
PFP on financial literacy and future time perspectives and their subse- finances, and financial decision-making, J. Consum. Aff. 57 (1) (2023) 564–592,
quent impacts on financial decision-making. https://doi.org/10.1111/joca.12512.
[6] A. Sorgente, M. Lanz, Emerging adults’ financial well-being: a scoping review,
Adolescent Research Review 2 (2017) 255–292, https://doi.org/10.1007/s40894-
6. Conclusion
016-0052-x.
[7] S. Leonard, J.W. Zhang, R. Howell, Spending well: how time perspectives impact
In the age of interactive AI, this research introduces a timely inno- consumer values and financial decisions among middle-aged adults, Res. Hum.
Dev. 16 (2) (2019) 135–155, https://doi.org/10.1080/15427609.2019.1670568.
vation: Python-based PFP aimed at emerging adults. Through rigorous
[8] K. Ryack, A. Sheikh, The relationship between time perspective and financial risk
validation, this study advances financial education for this demographic tolerance in young adults, Financ. Serv. Rev. 25 (2) (2016) 157–180, https://doi.
and offers a cost-effective strategy for leveraging interactive AI in per- org/10.61190/fsr.v25i2.3218.
[9] A. Amagir, W. Groot, H. Maassen van den Brink, A. Wilschut, A review of financial-
sonal financial decision-making. The implications of this research
literacy education programs for children and adolescents, Citizenship, Social and
extend beyond its immediate scope, promising transformative changes Economics Education 17 (1) (2018) 56–80, https://doi.org/10.1177/
in the global financial education landscape. By harnessing Python- 204717341771955.
[10] M. Dolls, P. Doerrenberg, A. Peichl, H. Stichnoth, Do savings increase in response
powered financial interventions, this study paves the way for a shift
to salient information about retirement and expected pensions?, Working paper
from traditional, one-size-fits-all financial education models to person- No. w22684, http://www.nber.org/papers/w22684, 2016, September.
alized interventions that address the psychological foundations of young [11] G.S. Goda, C.F. Manchester, A.J. Sojourner, What will my account really be worth?
individuals, influencing their financial behaviors over the long term. Experimental evidence on how retirement income projections affect saving,
J. Publ. Econ. 119 (2014) 80–92, https://doi.org/10.1016/j.jpubeco.2014.08.005.
Encouraging users to request projection code from interactive AI, rather [12] G.S. Goda, M. Levy, C. Flaherty Manchester, A. Sojourner, J. Tasoff, J. Xiao, Are
than direct outcomes, fosters greater trust in AI systems, thereby retirement planning tools substitutes or complements to financial capability?,
enhancing their appeal among emerging adults. This user recognition Working paper No. 30723, https://doi.org/10.2139/ssrn.4211243, 2022,
December.
and endorsement are pivotal in accelerating the adoption and
[13] E. Fajnzylber, G. Reyes Hartley, Knowledge, information, and retirement saving
advancement of interactive AI technologies. decisions: evidence from a large-scale intervention in Chile, Economia 15 (2)
(2015) 83–117. https://www.jstor.org/stable/24368341.
[14] O. Fuentes, J. Lafortune, J. Riutort, J. Tessada, F. Villatorok, Personalized
Funding
information as a tool to improve pension savings: results from a randomized
control trial in Chile, Econ. Dev. Cult. Change (2017), https://doi.org/10.1086/
This work was fully supported by a grant from The Investor and 720718.
[15] A.Y.F. Zhu, K.L. Chou, Medium and long-term effects of personalized pension
Financial Education Council in Hong Kong, China.
projection: A three-arm randomized control trail, Under review.
[16] A.Y.F. Zhu, Upgrading financial education by adding python-based personalized
Ethical statement financial projection: A randomized control trial, Brit. J. Educ. Technol. 55 (2)
(2024) 731–750, https://doi.org/10.1111/bjet.13401.
[17] M. Humber, Personal Finance with python: Using Pandas, Requests, and Recurrent,
Ethical approval for this study was obtained from the Research Apress, Berkeley, CA, 2018.
Committee of The Lingnan University (Hong Kong) prior to data [18] J. Zhou, M.A. Khawaja, Z. Li, J. Sun, Y. Wang, F. Chen, Making machine learning
collection. useable by revealing internal states update-a transparent approach, Int. J. Comput.
Sci. Eng. 13 (4) (2016) 378–389, https://doi.org/10.1504/IJCSE.2016.080214.
[19] J. Zhou, A.H. Gandomi, F. Chen, A. Holzinger, Evaluating the quality of machine
Informed consent learning explanations: a survey on methods and metrics, Electronics 10 (5) (2021)
1–19, https://doi.org/10.3390/electronics10050593, 593.
[20] A. Angerschmid, J. Zhou, K. Theuermann, F. Chen, A. Holzinger, Fairness and
Informed consent was obtained from all individual participants
explanation in AI-informed decision making, Machine Learning and Knowledge
included in the study. Extraction 4 (2) (2022) 556–579, https://doi.org/10.3390/make4020026.
[21] A.B. Arrieta, N. Díaz-Rodríguez, J. Del Ser, A. Bennetot, S. Tabik, A. Barbado,
F. Herrera, Explainable Artificial Intelligence (XAI): concepts, taxonomies,
CRediT authorship contribution statement opportunities and challenges toward responsible AI, Inf. Fusion 58 (2020) 82–115,
https://doi.org/10.1016/j.inffus.2019.12.012.
Alex Yue Feng Zhu: Writing – review & editing, Writing – original [22] S. Bach, A. Binder, G. Montavon, F. Klauschen, K.R. Müller, W. Samek, On pixel-
wise explanations for non-linear classifier decisions by layer-wise relevance
draft, Visualization, Validation, Supervision, Software, Resources,
propagation, PLoS One 10 (7) (2015) e0130140, https://doi.org/10.1371/journal.
Project administration, Methodology, Investigation, Funding acquisi- pone.0130140.
tion, Formal analysis, Data curation, Conceptualization. [23] K. Simonyan, A. Vedaldi, A. Zisserman, Deep inside convolutional networks:
visualising image classification models and saliency maps, arXiv preprint (2013),
https://doi.org/10.48550/arXiv.1312.6034.
Declaration of competing interest [24] J. Del Ser, A. Barredo-Arrieta, N. Díaz-Rodríguez, F. Herrera, A. Saranti,
A. Holzinger, On generating trustworthy counterfactual explanations, Inf. Sci. 655
(2024) 119898, https://doi.org/10.1016/j.ins.2023.119898.
The author declares no potential conflicts of interest concerning the
[25] S. Verma, V. Boonsanong, M. Hoang, K.E. Hines, J.P. Dickerson, C. Shah,
research, authorship, and/or publication of this article. Counterfactual explanations and algorithmic recourses for machine learning: a
review, arXiv preprint (2020), https://doi.org/10.48550/arXiv.2010.10596.
Data availability [26] Investor and Financial Education Council, Improvement in Hong Kong financial
literacy levels. https://www.ifec.org.hk/web/en/about-ifec/press-release/pr-20
200323.page, 2020.
Data will be made available on request.
7

A.Y.F. Zhu T e c h n o l o g y i n S o c i e ty77(2024)102599
[27] J.L. Rutt, C.E. Lo¨ckenhoff, From past to future: temporal self-continuity across the [38] S. Shim, B.L. Barber, N.A. Card, J.J. Xiao, J. Serido, Financial socialization of first-
life span, Psychol. Aging 31 (6) (2016) 631–639, https://doi.org/10.1037/ year college students: the roles of parents, work, and education, J. Youth Adolesc.
pag0000090. 39 (2010) 1457–1470, https://doi.org/10.1007/s10964-009-9432-x.
[28] J. Wiener, T. Doescher, A framework for promoting retirement savings, J. Consum. [39] J.J. Xiao, N. Porto, Present bias and financial behavior, Financial Planning Review
Aff. 42 (2) (2008) 137–164, https://doi.org/10.1111/j.1745-6606.2008.00102.x. 2 (2) (2019) e1048, https://doi.org/10.1002/cfp2.1048.
[29] D.M. Bartels, O. Urminsky, To know and to care: how awareness and valuation of [40] A.Y.F. Zhu, Parental socialization and financial capability among Chinese
the future jointly shape consumer spending, J. Consum. Res. 41 (6) (2015) adolescents in Hong Kong, J. Fam. Econ. Issues 39 (4) (2018) 566–576, https://doi.
1469–1485, https://doi.org/10.1086/680670. org/10.1007/s10834-018-9584-5.
[30] H.E. Hershfield, E.M. John, J.S. Reiff, Using vividness interventions to improve [41] S. Tomar, H.K. Baker, S. Kumar, A.O. Hoffmann, Psychological determinants of
financial decision making, Policy Insights from the Behavioral and Brain Sciences 5 retirement financial planning behavior, J. Bus. Res. 133 (2021) 432–449, https://
(2) (2018) 209–215, https://doi.org/10.1177/2372732218787536. doi.org/10.1016/j.jbusres.2021.05.007.
[31] S. Marques, J. Mariano, M.L. Lima, D. Abrams, Are you talking to the future me? [42] J.L. Koposko, D.A. Hershey, Parental and early influences on expectations of
The moderator role of future self-relevance on the effects of aging salience in financial planning for retirement, Journal of Personal Finance 13 (2) (2014) 17–27.
retirement savings, J. Appl. Soc. Psychol. 48 (7) (2018) 360–368, https://doi.org/ [43] J.J. Xiao, C. Tang, J. Serido, S. Shim, Antecedents and consequences of risky credit
10.1111/jasp.12516. behavior among college students: application and extension of the theory of
[32] A.M. Rutchick, M.L. Slepian, M.O. Reyes, L.N. Pleskus, H.E. Hershfield, Future self- planned behavior, J. Publ. Pol. Market. 30 (2) (2011) 239–245, https://doi.org/
continuity is associated with improved health and increases exercise behavior, 10.1509/jppm.30.2.23.
J. Exp. Psychol. Appl. 24 (1) (2018) 72–80, https://doi.org/10.1037/xap0000153. [44] J.J. Xiao, C. Tang, S. Shim, Acting for happiness: financial behavior and life
[33] T. Sims, S. Raposo, J.N. Bailenson, L.L. Carstensen, The future is now: age- satisfaction of college students, Soc. Indicat. Res. 92 (2009) 53–68, https://doi.
progressed images motivate community college students to prepare for their org/10.1007/s11205-008-9288-6.
financial futures, J. Exp. Psychol. Appl. 26 (4) (2020) 593–603, https://doi.org/ [45] J. Sachs, Validation of the satisfaction with life scale in a sample of Hong Kong
10.1037/xap0000275. university students, Psychologia 46 (4) (2003) 225–234, https://doi.org/10.2117/
[34] D. McCloskey, M. McDonnell, Effect of age-progressed avatars on savings behaviors psysoc.2003.225.
for retirement in young people, in: Proceedings of the Future Technologies [46] A.Y.F. Zhu, Financial literacy types and financial behaviors among adolescents:
Conference, Springer Nature Switzerland, Cham, 2023, October, pp. 266–285. role of financial education, Journal of Financial Counseling and Planning 32 (2)
[35] A. Lusardi, Financial literacy and the need for financial education: evidence and (2020) 217–230, https://doi.org/10.1891/JFCP-19-00051.
implications, Swiss Journal of Economics and Statistics 155 (1) (2019) 1–8,
https://doi.org/10.1186/s41937-019-0027-5.
Alex excels in extensive research on personal finance and personal finance education,
[36] P. Krishnamurthy, M. Sujan, Retrospection versus anticipation: the role of the ad specializing in personalized financial interventions for diverse age groups. He’s dedicated
under retrospective and anticipatory self-referencing, J. Consum. Res. 26 (1)
(1999) 55–69, https://doi.org/10.1086/209550. to integrating AI, programming, machine learning, and deep learning into personal finance
research. His expertise spans program design, implementation, and evaluation.
[37] C.R. McKenzie, M.J. Liersch, Misunderstanding savings growth: implications for
retirement savings behavior, J. Market. Res. 48 (2011) S1–S13, https://doi.org/
10.1509/jmkr.48.SPL.S1.
8