Disentangling Fairness Perceptions in Algorithmic
Decision-Making: the Efects of Explanations, Human Oversight,
and Contestability
Mireia Yurrita Tim Draws Agathe Balayn
m.yurritasemperena@tudelft.nl t.a.draws@tudelft.nl a.m.a.balayn@tudelft.nl
Delft University of Technology Delft University of Technology Delft University of Technology
Delft, The Netherlands Delft, The Netherlands Delft, The Netherlands
Dave Murray-Rust Nava Tintarev Alessandro Bozzon
D.S.Murray-Rust@tudelft.nl n.tintarev@maastrichtuniversity.nl A.Bozzon@tudelft.nl
Delft University of Technology Maastricht University Delft University of Technology
Delft, The Netherlands Maastricht, The Netherlands Delft, The Netherlands
ABSTRACT ACM Reference Format:
Recent research claims that information cues and system attributes Mireia Yurrita, Tim Draws, Agathe Balayn, Dave Murray-Rust, Nava Tintarev,
of algorithmic decision-making processes afect decision subjects’
and Alessandro Bozzon. 2023. Disentangling Fairness Perceptions in Algo-
rithmic Decision-Making: the Efects of Explanations, Human Oversight,
fairness perceptions. However, little is still known about how these
and Contestability. In Proceedings of the 2023 CHI Conference on Human Fac-
factors interact. This paper presents a user study (  = 267) in-
tors in Computing Systems (CHI ’23), April 23–28, 2023, Hamburg, Germany.
vestigating the individual and combined efects of explanations,
ACM, New York, NY, USA, 21 pages. https://doi.org/10.1145/3544548.3581161
human oversight, and contestability on informational and proce-
dural fairness perceptions for high-and low-stakes decisions in
a loan approval scenario. We fnd that explanations and contesta- 1 INTRODUCTION
bility contribute to informational and procedural fairness percep-
Motivated by concerns about bias and discrimination in algorithmic
tions, respectively, but we fnd no evidence for an efect of human
decision-making [73], recent work has developed fairness-aware
oversight. Our results further show that both informational and
algorithmic systems [6, 33, 108] that ensure outcome distribution
procedural fairness perceptions contribute positively to overall fair-
equity [32, 42]. However, even when a decision-making process is
ness perceptions but we do not fnd an interaction efect between
fair by some objective standard, decision subjects might not perceive
them. A qualitative analysis exposes tensions between informa-
it as fair [59] if aspects such as the inscrutability and unaccount-
tion overload and understanding, human involvement and timely
ability often surrounding algorithmic systems [17] go against their
d
m
e
a
c
i
i
n
si
t
o
a
n
in
-m
in
a
g
k
p
in
r
g
o
,
c
a
e
n
d
d
u r
a
a
c
l
c
c
o
o
u
n
n
s
ti
i
n
st
g
e n
fo
c
r
y .
p
O
er
u
so
r
n
r
a
e
l
s u
ci
l
r
t
c
s
u
h
m
av
st
e
a n
im
ce
p
s
o
w
rt
h
a
i
n
le
t
standards of justice [58, 72, 96].1 Perceptions of unfairness could,
design implications for algorithmic decision-making processes that
in turn, jeopardize end users’ trust in normatively fair algorithmic
meet decision subjects’ standards of justice.
decision-making processes and, therefore, be an obstacle for their
broader acceptance [31, 58, 72, 96, 103]. That is why a growing
body of human-computer interaction (HCI) literature now focuses
CCS CONCEPTS on determining which factors – e.g., information cues [63] such
• Human-centered computing → Empirical studies in HCI; as explanations [17, 30, 71, 83] and system attributes [63] such as
Collaborative and social computing;• Computing method- human oversight2 [29, 65, 66, 70, 103] or contestability [68, 93] –
ologies → Machine learning. efectively contribute to decision subjects’ fairness perceptions.
Despite making important contributions, previous HCI research
KEYWORDS
investigating fairness perceptions in algorithmic decision-making
has faced two important limitations. First, earlier work has largely
explanations, human oversight, contestability, fairness perceptions,
studied information cues and system attributes in isolation (e.g.,
algorithmic decision-making
[68, 93]). Such an approach fails to consider the entangled nature of
1According to Cropanzano [27], justice is a multi-dimensional construct that studies
fairness perceptions across each of its dimensions. For instance, procedural justice
refers to a justice dimension that aims to capture fairness perceptions regarding the
This work is licensed under a Creative Commons Attribution International process of a decision (i.e., procedural fairness perceptions). Colquitt and Rodell [25] refer
4.0 License. to faceted fairness as measurements of appropriateness that evoke diferent justice
dimensions.
CHI ’23, April 23–28, 2023, Hamburg, Germany 2Throughout this paper, human oversight refers to a confguration where human
© 2023 Copyright held by the owner/author(s). intelligence is applied to identify and correct potential mistakes made by an algorithmic
ACM ISBN 978-1-4503-9421-5/23/04. system [5]. We also call this confguration a hybrid human-artifcial intelligence (AI)
https://doi.org/10.1145/3544548.3581161 decision-making process.

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
these cues and attributes and does not align with the scenarios con- without human oversight and with or without the right to contest
templated by regulatory eforts such as the European Union’s Gen- the decision (RQ1). Each participant was randomly assigned to
eral Data Protection Regulation (GDPR) [101]. For example, decision a low-stakes4 (holiday) or to a high-stakes (home) loan approval
subjects can only meaningfully exercise their right to contest an al- scenario (RQ2). For each scenario, we measured perceptions of
gorithmic decision when they have solid arguments, which require informational, procedural and overall fairness (RQ3).
explanations of the decision-making process [79, 101]. Contestation Our results show that explanations and contestability afect end
mechanisms and explanations thus co-shape the procedural jus- users’ informational5 and procedural fairness perceptions, respec-
tice principle of correctability [62] and may, therefore, co-mediate tively (RQ1; see Section 5.2). We do not fnd evidence that end
decision subjects’ perceptions of procedural fairness [40, 62]. Not users’ perceptions of informational and procedural fairness are in-
considering these entanglements could lead to blind spots regarding fuenced by human oversight (RQ1) or the stakes of the task (RQ2).
how diferent factors that are theoretically claimed to afect fairness Our results further show that perceptions of informational and
perceptions (e.g., [93]) actually contribute to these perceptions. procedural fairness both relate positively to perceptions of overall
Second, prior work has mainly used one-dimensional approaches fairness, but we do not fnd an interaction efect between them
for measuring fairness perceptions [9, 30, 58, 68, 71, 74, 80, 103, 110]. (RQ3). As part of our exploratory analyses, we unpack informa-
Although measuring such overall fairness perceptions is useful for tional and procedural fairness perceptions into the sub-elements
capturing a global perception of appropriateness [25], prior work that compose each dimension (Section 5.3). We fnd that end users
on legal and organizational psychology has often advocated for may rate perceptions of procedural voice and outcome infuence
capturing fairness perceptions across up to four diferent dimen- negatively, even when contestability (in the form of appeal pro-
sions (i.e., faceted fairness perceptions) [21, 24]. These dimensions cesses) is incorporated. We also fnd that including human oversight
include perceptions towards the equitable allocation of outcomes may deteriorate perceptions of process consistency and lack of bias.
(i.e., distributive fairness perceptions) [1, 28], the nature of the pro- Through a qualitative analysis, we identify three areas of tension:
cess that leads to those decisions (i.e., procedural fairness percep- (1) amount of information vs. generating understanding for all, (2)
tions) [62, 64, 89] as well as the information (i.e., informational fair- human involvement vs. timely decision-making, and (3) standard-
ness perceptions) [15, 40, 85] and the treatment (i.e., interpersonal ized fact-based process vs. accounting for personal circumstances
fairness perceptions) [15] received by decision subjects. Capturing (see Section 5.4). These insights set the grounds for motivating
how dimension-specifc fairness perceptions manifest may help the exploration of transparency beyond outcome explanations, for
identify problematic aspects of algorithmic confgurations. Addi- crafting alternative human-AI confgurations, and for designing
tionally, learning how these dimension-specifc fairness perceptions contestation mechanisms that efectively give voice to decision
combine could then inform the prediction of global perceptions of subjects.
appropriateness [25]. We argue that prioritizing the measurement Supplementary materials linked to this paper include task design,
of overall fairness might impede the development of a nuanced preregistration, data, and code for statistical analysis and are openly
understanding of how diferent factors contribute to diferent facets available at https://osf.io/zrfty/.
of users’ fairness perceptions [24].
This paper takes a frst step towards a nuanced understanding 2 RELATED WORK
of how diferent information cues (i.e., explanations) and system
This section describes previous research on how explanations, hu-
attributes (i.e., human oversight and contestability) co-mediate
man oversight, and contestability contribute to fairness perceptions
multi-dimensional (i.e., informational and procedural) perceptions
in algorithmic decision-making and discusses the task-dependent
of fairness. Given the task-dependent nature of fairness percep-
nature of this work. We focus on these specifc information cues
tions [9, 17, 58, 70, 86, 96], we account for the stakes of the task as
and system attributes as they are directly addressed by Article 22(3)
an additional contextual factor. Three research questions guide our
of the GDPR [101]. We then cover research on human decision-
work:
making, where fairness perceptions have been captured across
• RQ1: Do explanations, human oversight, and contestability multiple dimensions.
afect perceived informational and procedural fairness in
algorithmic decision-making processes? 2.1 Factors Afecting Perceptions of Fairness in
• RQ2: Do the stakes (high/low) involved in the decision have Algorithmic Decision-Making
an efect on perceived informational and procedural fairness?
• RQ3: Do users’ perceived informational and procedural fair- Explanations. Explanations (i.e., representations of a system’s
ness predict overall perceived fairness?
ability to account for their own operation in ways that help users
understand how these tasks are being accomplished [17]) are con-
To address these research questions, we frst conducted a prelim-
sidered key elements for enhancing users’ fairness perceptions in
inary study to surface the interplay between explanations, human
algorithmic decision-making processes. Previous work has demon-
o
in
v
g
e
s
r s
t
i
o
g h
d
t
e
a
si
n
g
d
n
c
a
o
n
n t
o
e
n
s
l
t
i
a
n
b
e
i
,
l i
p
ty
r e
(
r
S
e
e
g
c
i
t
s
i
t
o
e
n
r e
4
d
.1 3
) .
u
W
se
e
r
t
s
h
tu
en
d y
u s
w
e
h
d
e
t
r
h
e
e
p
se
a r
f
t
n
ic
d
i-
-
s
s
t
u
r
b
a
j
t
e
e
c
d
t s
th
’
e
f e
p
e
o
li
s
n
it
g
iv
s
e
o
e
f
f
j
e
u
c
s
t
t
o
ic
f
e
d i
[
f
1
e
7
r
,
e
3
n
0
t
]
e
a
x
n
pl
d
a n
th
at
e
i
i
o
r
n
c
s
o
t
n
y
f
le
d
s
e
o
n
n
c
d
e
e
i
c
n
is
t
io
h
n
e
pants were shown a fctional loan approval process (Section 4.2).
fairness of algorithmic systems [72]. Schoefer et al. [83] found that
The descriptions shown to participants included information about
the decision-making process with or without explanations, with or 4Loan approval decisions are generally seen as high-stakes [26] but we still expect
diferences in users’ perceived stakes depending on the loan purpose.
3The preregistration is openly available at https://osf.io/4uf3m. 5This result replicates and confrms a fnding from earlier work [83].

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
the amount of information in explanations was positively related procedural fairness perceptions) [62, 64, 89], the treatment received
to informational fairness perceptions. by decision subjects (i.e., interpersonal fairness perceptions) [15],
and the information given to decision subjects (i.e., informational
Human Oversight. The term human oversight has been used to fairness perceptions) [15, 40, 85]. Each of these dimensions evokes
refer to the confguration where human intelligence is applied to
diferent justice principles and is built upon criteria that have been
identify potential mistakes in algorithmic decision-making pro-
found to be relevant for that dimension [95]. For instance, proce-
cesses [5]. Since algorithmic systems can perform increasingly
dural fairness perceptions are measured considering perceptions of
complex tasks [106], recent research has pointed to opportunities
procedural voice, outcome control, consistency of procedures across
for crafting more reliable and timely decision-making processes
participants, suppression of bias, accuracy of factors, correctability of
with human-artifcial intelligence (AI) collaborations [12, 109]. De-
outcomes, and ethicality of the process [62, 89].
spite this growing interest, most recent work on fairness percep-
tions has focused on comparing algorithmic systems with their
human counterparts [9, 20, 29, 36, 55, 58, 65, 74] rather than com- 2.3 Research Gap and Motivation
paring fully automated with hybrid confgurations. In one study
Although earlier work has shed some light on how to go from a
that did compare algorithmic decision-making to hybrid and human
normative to a behavioral understanding of fairness, evidence on
decision-making, Nagtegaal [70] found that hybrid confgurations
how factors that are theoretically related to certain principles of
can increase public employees’ (subjects of managerial decisions)
justice co-mediate decision subjects’ perceptions of fairness in algo-
perceptions of procedural fairness. Wang et al. [103] also evaluated
rithmic decision-making is still lacking. One reason for this is that
the efect of hybrid decision-making processes on decision subjects’
the efects of factors believed to enhance perceptions of fairness
perceptions of fairness but did not fnd any evidence that hybrid
have been obscured by phenomena such as the outcome favorabil-
decision-making processes are perceived to be fairer than fully
ity bias (i.e., divergence in users’ perceived fairness based on the
automated ones.
favorability of the outcome they receive personally) [74, 103]. For
Contestability. Contesting a decision has been defned as the act example, although including human oversight has been claimed to
of opposing an action; either because the action is perceived as bring together the best of the manual and the automatic worlds,
mistaken or simply wrong [4, 99]. Contestability has, thus, been there is still little insight into how human oversight contributes to
conceptualized as recourse [48, 91, 98], appeal [99], and as a design end users’ perceptions of fairness. Similarly, although contestability
principle (i.e., contestability by design) [3, 5, 79]. Contestability has been claimed to be a key aspect to enhance perceptions of fair-
is said to “surface values” [92] and to be a “form of procedural ness, to the best of our knowledge, there is currently no empirical
justice, a way of giving voice to decision subjects, which increases evidence on whether or how contestability contributes to these
perceptions of fairness” [3]. To the best of our knowledge, however, perceptions. One could argue that Lyons et al. [67] looked into
the efect of contestability in algorithmic decision-making has not diferent modalities of appeal processes and evaluated perceptions
yet been widely studied. In one of the few studies that empirically of fairness in each case. However, evaluating perceptions of fair-
tested the efect of appeals on decision subjects’ perceptions of ness towards diferent types of appeals is diferent from evaluating
fairness, Vaccaro et al. [93] found that none of their appeal designs perceptions of fairness towards an algorithmic decision-making
improved these perceptions. process that ofers the right to appeal. Another key limitation of
previous research is that it did not consider the entangled nature
Task stakes. Perceptions towards algorithmic decision-making of explanations, human oversight, and contestability. Although de-
can vary across scenarios [17, 96], based on task characteristics [58],
cision subjects’ right to explanation is not explicitly guaranteed by
and the stakes of the task (i.e., the impact that a negative outcome
the GDPR [84], Article 22(3) does explicitly guarantee their right to
would have on the future of an individual [49]) [9, 70, 86]. For
contest a negative decision [101], for which decision subjects need
instance, Binns et al. [17] found that scenario efects obscure ex-
meaningful (i.e., functional [84]) explanations [79]. The GDPR also
planation efects under repeated exposure of one explanation style.
states that contestations might vary based on the human interven-
Lee [58] saw diferences in fairness perceptions towards human and
tion in the original decision [101]. Therefore, the way in which a
algorithmic decision-makers based on task characteristics. Araujo
decision can be meaningfully contested depends on the received
et al. [9] argued that users may perceive algorithmic systems as
explanations [79] as well as the interpretation of the implemented
fairer than human experts only for high-impact decisions in the
safeguards (i.e., right to human intervention, right to express views,
justice and health domains.
and right to contest the decision) [101].
From a methodological perspective, a majority of previous stud-
2.2 Capturing Perceptions of Fairness in
ies has used mono-dimensional (i.e., overall fairness perceptions [25])
Decision-Making Processes approaches for capturing the efects of explanations, human over-
Users’ perceptions of fairness can be complicated and nuanced [103]. sight, and contestability on fairness perceptions [9, 30, 58, 68, 71, 74,
To measure these perceptions in a granular way, disciplines in social 80, 103, 110]. This has resulted in a lack of nuance in the understand-
sciences such as legal and organizational psychology have empiri- ing of how fairness perceptions are co-mediated by each of these
cally validated models that capture perceptions of fairness across factors. We echo the need to include lessons from the replication
diferent dimensions [25, 27]. These dimensions include percep- crisis within psychology [18] and advocate for a multi-dimensional
tions of fairness towards decision outcomes (i.e., distributive fairness approach to measuring perceptions of fairness (i.e., faceted fairness
perceptions) [1, 28], the processes that led to those outcomes (i.e., perceptions [25]). Although these dimensions were suggested for

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
human decision-making, we argue that they represent a good start- • Hypothesis 1c (H 1c ). End users’ procedural fairness perceptions
ing point toward developing standardized methods for specifcally difer based on the contestation procedure of an algorithmic
evaluating algorithmic decision-making processes. The benefts of decision-making process.
using a more nuanced approach for measuring the efect of expla- Rationale. We hypothesize that, as with human decision-making
nations on perceptions of fairness have already become evident. [89], contestation procedures in algorithmic decision-making
Schoefer et al. [83] found that outcome explanations would in- processes afect perceived procedural fairness.
crease end users’ perceptions of informational fairness, but it would • Hypothesis 1d (H 1d ). The efect of contestability on end users’
make them question structural aspects of the procedure, just as it procedural fairness perceptions is moderated by the presence of
was claimed by Greenberg [40] for human decision-making. explanations.
In this paper, we address the above gaps by systematically eval- Rationale. Schoefer et al. [83] found that, although including
uating algorithmic decision-making processes with varying levels more information in explanations led to an increased perception
of explanations, human oversight, and contestability, and unpack of informational fairness, the presence of explanations allowed
and disentangle their efects on perceptions of fairness through a end users to question the way in which diferent factors were
multi-dimensional approach. Since the factors (i.e., explanations, being used for decision-making. We thus hypothesize that, aside
human oversight, contestability) that we manipulate in our experi- from a general efect of contestability on users’ procedural fair-
mental setting have been related to perceptions of informational ness perception (see H
1c
), the presence of explanations and con-
and procedural fairness in human decision-making [62, 85], we testability on the algorithmic decision interact in afecting users’
capture perceptions of fairness across those two dimensions. We perceived procedural fairness.
also test the predictive validity [24] for these multi-dimensional • Hypothesis 1e (H 1e ). The efect of contestability on end users’
fairness perceptions on overall fairness perceptions. This enables us procedural fairness perceptions is moderated by the presence of
to compare the multi-dimensional approach with previously used human oversight.
mono-dimensional approaches. Rationale. Various studies have demonstrated end users’ con-
cern for fully automated, highly complex decision-making pro-
cesses [58, 70]. That is why we expect that confgurations where
3 HYPOTHESES end users can contest an algorithmic decision lead to varying
Drawing from literature in legal and organizational psychology
degrees of procedural fairness perceptions in users depending
for human decision-making [8, 13, 15, 16, 38, 40, 90] and studies
on whether the original decision was made by a fully automated
on perceptions of fairness in algorithmic systems [9, 41, 58, 72,
or hybrid system.
80, 83, 93, 96, 103], we formulated eleven hypotheses (Figure 1).
Each hypothesis is related to one of the research questions outlined
3.2 Hypothesis related to RQ2: Task stakes
in Section 1 and is followed by a rationale. We preregistered all
hypotheses before data collection. • Hypothesis 2a (H 2a ). The efect of explanations on end users’
informational fairness perceptions is moderated by the stakes of
the task.
Rationale. Binns et al. [17] found that the nature of the presented
3.1 Hypotheses related to RQ1: Explanations,
scenario moderates the efect of explanation types on fairness
Human Oversight, and Contestability perceptions. In line with these fndings, we hypothesize that,
• Hypothesis 1a (H 1a ). End users perceive algorithmic decision- based on the nature of the task at stake (i.e., involving high or
making processes as more informationally fair when they are low stakes), end users will be satisfed diferently with the amount
accompanied with explanations. of information they received.
Rationale. We extend Schoefer et al. [83]’s study to evaluate the • Hypothesis 2b (H 2b ). The efect of human oversight on end
efect of explanations on informational fairness in both high- users’ procedural fairness perceptions is moderated by the stakes
stakes and low-stakes decisions. We expect to replicate their of the task.
fndings in our own experimental setting. Rationale. Lee [58] demonstrated that fairness perceptions re-
• Hypothesis 1b (H 1b ). End users perceive algorithmic decision- garding the decision maker (i.e., a fully automated system or a
making processes as more procedurally fair when these processes human) were moderated by task characteristics. Nagtegaal [70]
are supplemented by human oversight rather than fully auto- also found that the efect of involving humans on perceptions
mated. of procedural justice varied based on the complexity of the task.
Rationale. Previous studies have found that users consider hu- Despite the context being diferent (both these studies focused on
man decisions to be fairer than fully automated, algorithmic managerial decisions) and our study considering fully automated
decisions; especially for practices that are highly complex and vs hybrid decision making, we hypothesize that the stakes of the
are perceived to require human skills [58, 70]. Although recent task (i.e., involving high or low stakes) will similarly moderate
research has found contradictory evidence on whether users per- the efect of human oversight on procedural fairness perceptions
ceive hybrid decision-making as fairer than entirely algorithmic in our study.
decision-making [70, 103], we do expect that human oversight • Hypothesis 2c (H 2c ). The efect of contestability on end users’
will lead to increased procedural fairness perceptions among users procedural fairness perceptions is moderated by the stakes of the
in sensitive contexts (e.g., loan approval processes). task.

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
Figure 1: Overview of the hypotheses. Yellow refers to information cues, green to system attributes, and grey to contextual
factors.
Rationale. Previous work has suggested that perceptions of fair- captured preferences towards diferent explanation styles and in-
ness regarding the decision-maker generally depend on the na- vestigated what aspects participants would like to contest. We then
ture of the task [58]. We thus hypothesize that the stakes of the combined these insights with previous literature to design our main
task (i.e., involving high or low stakes) also moderate the efect of user study in the context of a loan approval process (Section 4.2).
contestability (e.g., when users are given the right to contest the
decision-maker [68]) on users’ procedural fairness perceptions. 4.1 Preliminary Study
This preliminary study (  = 58) aimed at crafting (1) understand-
3.3 Hypothesis related to RQ3: Overall vs. able and (2) actionable6 explanations that (3) support contesta-
Faceted fairness bility [101]. We also sought to understand what aspects of the
• Hypothesis 3a (H 3a ). End users’ informational fairness percep- decision-making process participants may contest. Although prior
tions are positively associated with their overall fairness percep- work has already studied the understandability of diferent types
tions. of explanations [17, 30] and identifed actionable factors for loan
Rationale. This hypothesis is in line with fndings in human approval processes [83], the interplay between explanations and
decision-making, where informational fairness was claimed to contestability still represents an underexplored area,7 hence the
infuence perceptions of overall fairness [24, 39]. need to perform this preliminary study. The design of our prelim-
• Hypothesis 3b (H 3b ). End users’ procedural fairness perceptions inary study and the instruments we used to capture participants’
are positively associated with their overall fairness perceptions. preferences can be found in our repository.
Rationale. Studies dealing with procedural fairness in human
decision-making processes [39, 89] demonstrated that partici- 4.1.1 Method of the Preliminary Study. As part of our prelimi-
pants with a strong infuence over the decision-making process
nary study, we provided each participant with fve types of ex-
were more likely to perceive a negative outcome as fair [47].
planations (randomized) for a fctional home loan denial scenario:
We hypothesize that for algorithmic decision-making processes, (1) factor importance-based explanations (i.e., feature importance
there will also be a positive relation between perceptions of pro-
hierarchy using “>” for expressing “more important than” [83]),
cedural fairness and overall fairness. (2) input infuence-based 8 explanations (i.e., list of input variables
• Hypothesis 3c (H 3c ). End users’ perceived informational and along with a quantitative measure of the efect and directionality
procedural fairness interact in predicting overall fairness. —positive or negative— that each of these variable had on the fnal
Rationale. Research in human decision-making has demonstrated decision [17, 30]), (3) case-based explanations (i.e., instance from
that explanations provide the “information needed to evaluate the model’s training data that is most similar to the decision being
structural aspects of decision-making” [40]. In line with these
fndings, we hypothesize that perceptions of overall fairness are
6We defne “actionable” factors as the set of variables upon which interventions are
not just dependent on both informational and procedural fairness,
possible. We include those variables that may change as a consequence of a change to its
but that these two factors interact in predicting overall fairness causal ancestors (that other authors have named as “mutable but non-actionable” [51])
perceptions. 7Although the interplay between explanations and recourse is increasingly being
studied (e.g., [50, 87]), for this preliminary study, we do not limit contestability to
recourse and inquire whether participants would question other aspects of the decision-
4 STUDY DESIGN making process.
8As opposed to some previous work [17, 30], where the quantitative measurement of
Because explanations, human oversight, and contestability are en- the input infuence was indicated through a varying number of “+” (positive infuence)
tangled by nature [101], we frst conducted a preliminary study or “-” (negative infuence) signs, we expressed this diference in infuence through
to craft an experimental setting that would surface the interplay
n
th
u
e
m
p
e
o
ri
s
c
it
a
i
l
v
v
e
a
o
lu
r
e
n
s.
e
W
ga
e
t i
c
v
l
e
a r
e
i
f
f
e
ed
ct
t
t
h
h
a
a
t
t
t h
th
e
e
n
v
u
a
m
ri
b
a
e
b
r
l e
in
h
b
a
r
d
a c
o
k
n
e t
t
s
h e
in
f
d
n
ic
a
a
l
t e
d
d
e c
t
i
h
s
e
io
m
n
a
—
gn
n
i
e
t
g
u
a
d
t
e
i v
o
e
f
between these factors (Section 4.1). In this exploratory study, we meaning a contribution towards the rejection decision—.

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
explained [17, 30]), (4) counterfactual explanations (i.e., represen- 4.2 Main User Study
tation of the alterations that input variables would need for the In our main user study, we sought to characterize the main and
undesired model output to change [17, 30, 101]), and a combination interaction efects of explanations, human oversight, and contesta-
of (5) input infuence-based and counterfactual explanations [83]. bility on perceptions of informational and procedural fairness. We
They were then asked to select the two most understandable and also explored the infuence of contextual factors (i.e., the stakes
actionable explanations and two explanations thanks to which of the task) in this context and captured the relationship between
the decision subject would best know what information to use to informational and procedural fairness perceptions and perceptions
contest the decision. We also asked them to choose their overall of overall fairness. We had preregistered our hypotheses, research
preferred explanation type. At the end of the study, we included design, and data analysis plan for the main study before data col-
two open-ended questions. The frst question aimed to disclose the lection.
rationales behind users’ preferences for diferent types of expla-
nations. The second question collected answers on what aspects 4.2.1 Independent Variables. In an efort to minimize the efect
of the decision-making process participants would be willing to of outcome favorability bias [103], we followed prior research [9,
contest. For analyzing the responses to the open-ended questions, 83, 86] and showed participants in our user study a fctional loan
we performed a refexive thematic analysis [19]. Our aim was to approval scenario involving the fctional character Kim as loan
use the fndings from this preliminary study to inform the design requester. The scenario difered depending on four independent
of our main user study (Section 4.2). variables. Figure 2 gives an overview of the independent variables
and Table 5 in Appendix B shows how each independent variable
4.1.2 Insights from the Preliminary Study. The combination of
was displayed in practice.
counterfactuals and input infuence-based explanations scored high- • Explanations (categorical, between-subjects). We assigned each
est for all criteria (see Table 1). To better understand these results, participant to one of two confgurations:
we discuss our fndings from the qualitative analysis below. We refer (1) No explanation: participants saw what information the fc-
to quotes as Q.i, where i is the index of a specifc quote. Appendix A tional loan requester had been asked to provide but not how
shows all selected quotes. this information was used.
Preferences towards diferent types of explanations. In line with (2) With explanation: participants learned the weight each piece
fndings from Dodge et al. [30], we found that case-based expla- of information had in the fnal decision (input infuence-based
nations were considered less fair (Q.1, Q.2). Participants generally explanation) and the hypothetical scenarios where the loan
preferred explanations that contain more information, which is in requester would have been able to have the loan approved
line with fndings from Schoefer et al. [83] (Q.3). Moreover, partici- (counterfactuals). The factors requested by the bank and the
pants generally preferred the combination of input infuence-based given explanations are inspired by prior work [83] and en-
and counterfactual explanations because these included descrip- hanced based on the insights we got from the preliminary
tions of the “how” and a justifcation of the “why” of decisions, as study (Section 4.1). We discarded gender and marital status as
suggested by Sarra [79]. Input infuence-based explanations were decision basis because these factors are explicitly protected
regarded as faithful descriptions of how each feature contributes by law [14]. Note that the no explanation confguration in our
to the algorithm’s decision-making process (11/58)9 (Q.4). Despite study is equivalent to the disclosure of factors condition de-
using numerical values to indicate diferent degrees of input in- fned by Schoefer et al. [83], and not to the baseline without
fuence on the fnal decision, readability was not fagged as an further explanations. The rationale behind this design choice
issue for input infuence-based explanations by our participants. is twofold: frst, we argue that the disclosure of these factors
Counterfactuals were regarded as concise and explicit when direct- is necessary for participants to be able to judge the fairness
ing the attention to features that were relevant to that particular of the decision basis. Second, Schoefer et al. [83] found no
decision (17/58) (Q.5, Q.6). diference in informational fairness perceptions between the
What to contest. Participants pointed to two main aspects they two aforementioned confgurations. These explanations were
would like to contest: frst, the basis (i.e., the factors) of the decision textual to limit presentation complexity [22, 83, 96].
and their weights (28/58) (Q.7, Q.8) and second, the usage of an • Human oversight (categorical, between-subjects). We randomly
AI (10/58). Algorithmic systems were viewed as lacking subjective assigned each participant to one of two confgurations:
judgment capabilities for considering individual circumstances (in (1) No human oversight: participants were told that the algorith-
line with previous studies [20, 58, 70]) (Q.9). Generalization was mic decision-making process was fully automated.
also considered to be an inappropriate basis for decision-making (2) With human oversight: participants were told that the loan
(Q.10). approval process combined the usage of an algorithmic sys-
tem with human expertise. We designed this condition based
on one of the human-in-the-loop confgurations discussed by
Almada [5]. As opposed to some previous work where a hu-
man would supervise each decision made by the algorithmic
9We indicate the prevalence of each statement using proportions (a/b), where a indi- system [103] — the authors did not fnd any evidence of this
cates the number of participants whose response to the open-ended questions was confguration afecting fairness perceptions—, in our study
p
re
a
l
n
a
t
t
s
e d
w
t
i
o
th
t
i
h
n
e
a
s
c
t
o
a
n
te
d
m
it
e
io
n
n
t
t
in
h a
q
t
u
w
e
e
st
a
io
r
n
e
,
s
a
p
n
ec
d
i f
b
c
i
a
n
ll
d
y
i c
r
a
e
t
f
e
e
s
r r
e
in
it
g
h e
t
r
o
t
o
h
r
e
t h
n
e
u m
to
b
ta
e
l
r
n
o
u
f
m
p
b
a
e
rt
r
i c
o
i
f
- human intervention would serve as a quality control against
participants in the study (58 for the preliminary study and 267 for the main study). machine failures [5]. We, therefore, used the confdence of the

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
Understandable Actionable Supports contestability Overall
Importance-based explanation 23.64% 17.70% 18.35% 12.08%
Input infuence-based explanation 17.27% 20.35% 21.10% 15.52%
Case-based explanation 16.36% 8.85% 14.68% 13.79%
Counterfactual explanation 13.64% 15.93% 16.51% 15.52%
Combination counterfactual & input infuence-based 29.09% 37.17% 29.36% 43.10%
Table 1: Results from our preliminary exploratory study. We evaluated how (1) understandable and (2) actionable diferent types
of explanations were, and to what extent they (3) supported contestability. Column (4) shows participants’ overall preferred
option.
Figure 2: Overview of the independent variables. Yellow refers to information cues, green to system attributes, and grey to
contextual factors. White colored boxes indicate the conditions we controlled for each factor.
prediction as an indicator of a potential mistake made by the • Task stakes (categorical, between-subjects). Each participant was
algorithmic system. The approval process would involve two randomly assigned to one of two confgurations:
steps: a frst step where the algorithmic system receives an (1) High-stakes decision: the purpose of the loan application is to
online loan request and evaluates the case; and a second step buy a house.
where a human expert [74] (bank employee) oversees the deci- (2) Low-stakes decision: the purpose of the loan application is to
sion if the algorithmic decision-making system’s confdence is go on a holiday trip.
low.
• Contestability (categorical, between-subjects) We designed con-
testation mechanisms in the form of appeal processes, following 4.2.2 Dependent Variables. The instruments we used to measure
fndings from our preliminary study (Section 4.1) and previous lit-
the dependent variables can be found in our repository.
erature [68, 101]. Users in our preliminary study mainly wanted • Perceptions of informational fairness (continuous). Measured by
to contest (1) the algorithmic decision-maker or (2) the basis of the average score on four of the items used by Schoefer et al.
the decision. These strategies resonated with the new information [83], based on Bies and Moag [15] and Greenberg [40].
condition and new decision condition (with a human reviewer) de- • Perceptions of procedural fairness (continuous). Measured by the
fned by Lyons et al. [68]. We randomly assigned each participant average score on the seven items defned by Colquitt [24],10 based
to one of three confgurations: on Thibaut and Walker [89] and Leventhal [62].
(1) No contestability: participants were told that, due to time con- • Perceptions of overall fairness (continuous). Measured by a single
straints, there would be no option for the fctional loan re- item rated on a seven-point Likert scale [56, 58].
quester to contest the decision in case of a rejection.
(2) Option to contest the initial decision and provide additional
information: participants were told that, in case of a rejection, 4.2.3 Descriptive and Exploratory Measurements. The instruments
the fctional loan requester had the option to make objections we used to measure the descriptive and exploratory variables can
about the initial decision and provide any information to sup- be found in our repository.
port the application. The same system (if a human oversaw • Age group (categorical). Participants selected their age group
the initial decision, the same human would oversee the review from multiple choices.
process) would reevaluate the loan application. • Level of education (categorical). Participants selected their highest
(3) Contest decision-maker: participants were told that, in case of completed level of education from multiple choices.
a rejection, the fctional loan requester had the opportunity to • AI literacy (continuous). AI literacy has been proven to signif-
ask a human (diferent from the one who oversaw the process icantly afect perceptions of informational fairness [83]. We,
if there was already a human involved in the initial decision) therefore, captured the average score of the four items defned
to review the process. This human reviewer would make a by Schoefer et al. [83].
completely new decision with the information that Kim had
already provided for the initial decision.
10After pilot testing the wording and layout of the presented scenarios, we rephrased
some of the items to make them more understandable for participants.

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
• Afnity to technology (continuous). Langer et al. [56] showed that threshold of  = 0.05 = 0.0045 (i.e., due to testing multiple hy-
11
afnity to technology was consistently correlated with end users’ potheses; see Section 4.2.6), a desired power of 0.8, 24 groups, and
perceptions of algorithmic capabilities. We, therefore, captured the respective degrees of freedom for the diferent hypotheses we
the average score of the four items defned by Franke et al. [35] aimed to test.
as a possible control variable. We recruited 279 participants from Prolifc (https://prolifc.co).
• Personal experience (continuous). Kramer et al. [55] showed that Each participant was at least 18 years old, had high profciency
preferences towards humans vs. algorithmic systems depend on in English, and could participate in our study only once. Partici-
people’s previous experience with the described situation. We, pants were rewarded based on a $12 hourly rate and the median
therefore, captured the average score of the two items defned completion time was 7 minutes and 41 seconds. Participants were
by Kramer et al. [55]. excluded from data analysis if they did not pass at least one of
• Task stakes perception (continuous). Since the stakes involved in the attention checks in the experiment. This led to a total number
a decision are subjective and personal [49], we captured partic- of 267 participants. The study itself was conducted on Qualtrics
ipants’ task stakes perceptions as a manipulation check. This (https://www.qualtrics.com), where participants authenticated with
was measured through an adapted version of the item defned by a registration token received on Prolifc. Our study was approved
Lyons et al. [68]. by a research ethics committee at our institution.
4.2.4 Procedure. The study consisted of four main steps. 4.2.6 Statistical Analyses. Before conducting any statistical anal-
Step 1. Participants stated their age group and level of educa- yses, we mapped all (seven-point) Likert scale answers onto an
tion. Their degrees of AI literacy, afnity to technology, personal ordinal scale ranging from −3 (i.e., strongly disagree) to 3 (i.e.,
experience and task stakes perception were also measured. strongly agree) and computed averages for answers on related
Step 2. Participants were presented with a fctional loan approval items (e.g., to obtain participants’ informational and procedural
scenario involving a person named Kim. Previous research has fairness perceptions).
shown that under repeated interactions with algorithmic decision- We analyzed the hypotheses we specifed in Section 3 in three
making systems, decision subjects’ fairness perceptions are afected separate statistical analyses. First, to test H1a and H2a , we con-
by the favorability of the system towards the group that the decision ducted a multi-way ANOVA with explanations, human oversight,
subjects belong to [37]. In order to minimize these efects, we limited contestability, and task stakes as between-subjects factors and per-
our study to a one-shot interaction with the system and we did not ceptions of informational fairness as dependent variable.11 Second,
disclose the demographics of Kim, such as their gender and age. to test H
1b-e
and H
2b-c
, we conducted another multi-way ANOVA
Kim had applied for a loan online and was waiting for the bank with the same between-subjects factors but with perceptions of pro-
to assess their eligibility. Depending on the stakes of the task that cedural fairness as the dependent variable. Third, to test H3a-c , we
participants had been assigned to, the purpose of this loan would conducted a multiple linear regression analysis with perceptions
be either to buy a house (high stakes) or to go on a holiday trip (low of informational fairness and perceptions of procedural fairness as
stakes). Participants would be informed about the information Kim independent and perceptions of overall fairness as dependent vari-
had provided to the bank to evaluate the loan request. As part of ables. Because we were testing 11 hypotheses as part of this study,
the scenario, every participant would then be informed that Kim’s we applied a Bonferroni correction to our signifcance threshold,
loan request had been rejected and they would get to know the reducing it to 0.05 = 0.0045. This means that p-values resulting
11
process through which the loan request had been evaluated. Based from the analyses described above are only regarded as signifcant
on which of the (2 × 2 × 3 × 2) = 24 between-subject scenarios a if they are below this reduced threshold. Next to the  statistic and
participant had randomly been placed in, participants would receive  -value, we also report the partial eta squared (
p
2) efect size for
explanations about the outcome of the decision, learn whether there each hypothesis test that was part of an ANOVA.
was a human expert overseeing the process and get information In addition to the analyses described above, we conducted posthoc
about whether and how Kim could contest the decision (see Table tests (i.e., to analyze pairwise diferences), Bayesian hypothesis
2). Participants would then respond to an attention check, where tests12 (i.e., to quantify evidence in favor of null hypotheses), and
they would be asked about the purpose of the loan request. exploratory analyses (i.e., to note any unforeseen trends in the
Step 3. Participants evaluated their perceptions of informational, data) to better understand our results. We also performed a quali-
procedural, and overall fairness. Additionally, this step included a tative, refexive thematic analysis [19]. The frst author coded the
second attention check that asked participants to select a specifc responses to the open-ended questions inductively using Atlas.ti
option from a Likert scale. (https://atlasti.com). These codings were grouped into themes and
Step 4. Participants were asked two optional open-ended ques- iteratively refned.
tions to describe what kind of information they would have liked
to receive (if any) and what element would have made the decision-
making process fairer (if any).
11Although we did not specifcally hypothesize about the efects of human oversight
and contestability on informational fairness perception, we included these variables
4.2.5 Data Collection. We planned to collect data from at least here for exploratory analyses.
261 participants. We computed the required sample size using the 12Depending on the outcome of the relevant classical hypothesis test, we report Bayes
software G*Power [34] for an ANOVA with main efects and in- F in a t c e t r o p r r s e i t n t h fa e v B o a r y o e f s t F h a e c a to lt r e s r n ac a c ti o v r e d i h n y g p t o o t h th es e i s g u (B id F e 1 0 b ) y o L r e t e h e a n n d u l W l h a y g p en ot m h a e k si e s r s (B [ F 5 0 7 1 ] ) . w W ho e
teractions; specifying the default efect size of 0.25, a signifcance adapted it from Jefreys [46].

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
A bank has implemented a new loan application system where potential customers apply for a loan online and then the company assesses the
eligibility of the customer for the loan.
<Confguration [No human oversight] or[With human oversight]>
Kim, a potential customer, is looking for funding opportunities to <task> and has thus decided to apply for a <task> loan through the bank’s
online platform. As part of the <task> loan application process, the bank has requested the following information:
• Applicant annual income
• Co-applicant (if any) annual income
• Credit score
• Date of birth
• Employment status
• Education
• Loan amount requested
• Loan amount term (months)
• Loan purpose
• Number of dependents
A few hours after sending the requested information, Kim has received an email with the fnal decision: the loan has been rejected.
<Confguration [No explanation] or[With explanations]>
<Confguration [No contestability]or [Contest initial decision]or [Contest decision-maker]>
Table 2: Overview of the scenario.
5 RESULTS fairness being moderated by the presence of explanations (H1d ;
In this section, we analyze the results of the main user study (see  (2, 254) = 0.16,  = 0.85;  p 2 < 0.01, BF 01 = 12.95) or by the pres-
Section 4.2). Table 3 shows a summary of our results. ence of human oversight (H1e ;  (2, 254) = 0.005,  = 1.00;  p 2 < 0.01,
BF 01 = 13.35). We also did not fnd any evidence of an interaction
5.1 Descriptive Statistics between task stakes and human oversight (H2b ;  (1, 254) = 0.06,
Of the 267 participants in our user study, 19.5% were between 18  = 0.80,  p 2 < 0.01; BF 01 = 7.32) or task stakes and contestability
and 25 years old, 35% between 26 and 35 years old, 28.5% between (H2c ;  (2, 254) = 0.52,  = 0.60,  p 2 < 0.01; BF 01 = 7.20) when
36 and 50 years old, and 17% were between 50-80. 60% of the par- predicting perceptions of procedural fairness.
ticipants had at least a Bachelor’s degree. 87% of our participants We performed a multiple linear regression analysis to test the as-
claimed to have heard or had experience with humans making loan sociation of informational and procedural fairness perceptions with
decisions, whereas 72% of them had heard of or had experience overall fairness perceptions (  2 = 0.46,  (3, 263) = 76.02,  < 0.001).
with an algorithmic system making the decision. Our results show that perceptions of informational fairness (H3a ;
= 0.27,  < 0.001) and perceptions of procedural fairness (H3b ;
5.2 Hypothesis Tests  = 0.87,  < 0.001) both predicted overall fairness perceptions,
Our frst confrmatory analysis was a multi-way ANOVA with the with procedural fairness perceptions being the stronger predictor.
presence of explanations, human oversight, contestability, and task However, we did not fnd evidence that perceptions of informa-
stakes as between-subjects factors and perceptions of informational tional and procedural fairness interact (H3c ;  = −0.09,  = 0.07)
fairness as the dependent variable. We found a main efect of the when predicting overall fairness perceptions.
presence of explanations (H1a ;  (1, 260) = 74.21,  < 0.001,  p 2 = In sum, we found evidence in favor of four of our hypotheses:
0
H
.2 o
2
w
;
e
B
v
F
e
1
r
0
, w
>
e
1
d
0
i
0
d
0 )
n
o
o
n
t f
e
n
n
d
d
a
u
n
se
y
r s
e
’
v
i
i
n
d
f
e
o
n
r
c
m
e
a
in
ti
d
o
i
n
c
a
a
l
t i
f
n
a
g
ir n
th
e
a
ss
t t
p
h
e
e
r c
e
e
f
p
e
t
c
io
t
n
o
s
f
. H
for
1
m
a ,
a
H
ti
1
o
c
n
,
a
H
l
3
fa
a
i
,
r
a
n
n
e
d
ss
H
p
3
e
b
r
,
c e
in
p
d
ti
i
o
c
n
at
s
i n
an
g
d
e f
co
e
n
ct
t
s
e s
o
ta
f
b
e
i
x
li
p
ty
la
o
n
n
at
p
io
r
n
o
s
c e
o
d
n
u r
in
al
-
explanations on informational fairness is moderated by task stakes
fairness perceptions, respectively (Figure 3). We also show that
(H2a ;  (1, 260) = 0.01,  = 0.92,  p 2 < 0.01). A Bayesian analysis r in el f a o t r e m d a t t o i o o n v a e l r a a l n l d fa p ir r n o e c s e s d p u e ra rc l e f p a t ir io n n e s s . s perceptions are positively
revealed moderate evidence in favor of the null hypothesis that
there is no such interaction efect (BF 01 = 7.44).
The second multi-way ANOVA analysis we conducted had the 5.3 Exploratory Analyses
presence of explanations, human oversight, contestability, and task In addition to the hypothesis tests (see Section 5.2), we performed
stakes as between-subjects factors and perceptions of procedural several exploratory analyses to better understand our results and
fairness as the dependent variable. We did not fnd any evidence of identify any unforeseen but interesting trends in our data. Note
human oversight impacting procedural fairness perceptions (H1b ; that these are not confrmatory results as we did not preregister
(1, 254) = 0.004,  = 0.95,  p 2 < 0.01) and a Bayesian analysis any of the analyses presented in this subsection.
returned moderate evidence in favor of the null hypothesis that hu- Decision tasks are subjective and personal [49], so we conducted
man oversight has no efect here (BF 01 = 7.43). However, there was a manipulation check regarding the stakes of the task. We per-
a strong efect of contestability (H1c ;  (2, 254) = 20.60,  < 0.001, formed a t-test between the pre-defned task stakes (low for a hol-
p 2 = 0.14; BF 10 > 1000). We further found no evidence in favor of iday loan, high for a home loan) and participants’ perceived task
the efect of contestability on end users’ perceptions of procedural stakes. Our results indicate that the holiday loan (  = 0.38,   =

CHI ’23, April 23–28, 2023, Hamburg, Germany  Yurrita et al.
|     | Informational Fairness  |     |     |     | Procedural Fairness  |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
Overall Fairness
|               | Mean  | Th  | R  T  U  | Mean  | V  Inf  Cnst  | LB  | AF  Crr  | Eth  |     |
| ------------- | ----- | --- | -------- | ----- | ------------- | --- | -------- | ---- | --- |
| Explanations  | ***   | ⋄   | ⋄  ⋄  ⋄  | ⋄     | ⋄             | ⋄   |          | ⋄    |     |
Explanations × Task Stakes
| Explanations × AI literacy  | ⋄   |     | ⋄   |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI literacy                 | ⋄   |     | ⋄   |     |     |     |     |     |     |
Human Oversight
Human Oversight × Task Stakes
| Contestability                      |     |     |     | ***  | ⋄     |     | ⋄   | ⋄   |      |
| ----------------------------------- | --- | --- | --- | ---- | ----- | --- | --- | --- | ---- |
| Contestability × Explanations       |     |     |     |      |       | ⋄   |     |     |      |
| Contestability × Human Oversight    |     | ⋄   |     |      | ⋄  ⋄  |     |     |     |      |
| Contestability × Task Stakes        |     |     |     |      |       |     | ⋄   |     |      |
| Task Stakes                         |     |     |     |      |       |     | ⋄   |     |      |
| Informational Fairness Perceptions  |     |     |     |      |       |     |     |     | ***  |
| Procedural Fairness Perceptions     |     |     |     |      |       |     |     |     | ***  |
Table 3: Summary of our results. *** refer to confrmatory results (   < 0.001), whereas ⋄ refer to exploratory results (   < 0.05).
Empty cells indicate an absence of signifcant efect between variables. Mean = averaged value of the sub-items that constitute
faceted fairness perceptions, Th = Thorough, R = Reliable, T = Tailored, U = Understandable, V = procedural Voice, Inf = Outcome
Infuence, Cnst = process Consistency, LB = Lack of Bias, AF = Adequacy of Factors, Crr = Correctability, Eth = Ethicality.
Figure 3: Efects of (a) explanations on perceptions of informational fairness and, (b) human oversight, and (c) contestability on
perceptions of procedural fairness (HO = human oversight, C = contestability, ID = initial decision, DM = decision-maker).
1.31) was, indeed, regarded as a lower-stakes scenario compared to  5.3.1  Efects of Explanations. As expected, providing explanations
the home loan (   = 1.70,     = 1.07;   (258.61) = 9.09,    < 0.001).  had a positive efect on end users’ perceptions of informational
Because contestability is composed of three diferent groups, we  fairness. Participants considered that, whenever explanations were
performed pairwise comparisons to analyze the specifc diferences  added, the bank was giving thorough (   (1, 249) = 104.00,    < 0.001,
with respect to procedural fairness perceptions. We observed no  2 2
|     |     |     |     | p = 0.29) and reasonable ( |     |     |  (1, 249) = 40.31,  |     |  < 0.001,   p = 0.14) in- |
| --- | --- | --- | --- | -------------------------- | --- | --- | ------------------- | --- | ------------------------- |

signifcant diference between the efect that the two suggested  formation that would make Kim understand (   (1, 249) = 19.84,    <
contestation mechanisms have on procedural fairness perceptions  0.001,   2 = 0.07) the way in which the decision was made. Par-
p
(Tukey-adjusted    = 0.45), but both of them difered from the option
ticipants also considered that these explanations were tailored
wit h  n o c o n te s ta b i l i t y  ( T u k e y - a d j u st e d  < 0 . 0 0 1  i n  b o th  c a s e s ). 2
          t o  K i m ’ s  n e e d s   (    1 ,  2 4 9 )  =   4 5 .5 5 ,     <   0 .0 0 1 ,    p =  0 .1 5 ) .   T h e   e f -
W e a l so lo o k e d a t th e e f e c t s  o f  e x p l a n a t i o n s ,  h u m a n  o v e r s ig h t,  (
          fe c t  o n  p r o c e d u r a l f a ir n e s s  w a s  p a rt i al :  o u r  e x p l o ra to r y a n a l y s i s

and contestability on the sub-elements of informational and proce- suggests that explanations afected perceptions of process con-
d ur a l  f a i rn e s s  p e r ce p ti o n s .   E a c h   o f   th e s e  s u b -e le m e n ts   is  a s s e s se d   b y   2
|     |     |     |     | sistency ( |  (1, 254) = 16.80,  |     |  < 0.001,  |     | = 0.06), potentially be- |
| --- | --- | --- | --- | ---------- | ------------------- | --- | ---------- | --- | ------------------------ |
o n e  i n d i v id u a l  i te m   in  t h e   f a i r n e s s   p er c e p t io n  q u es t io n n a ir e s .  F o r  i n - p
cause explaining to end users how each factor contributes to a
formational fairness perceptions, we evaluated whether participants
fnal decision may make them discover that the process is stan-
thought that Kim received (1) thorough, (2) reasonable, (3) tailored,
dardized and uses the same criteria for every client. Explanations
and (4) understandable information. For procedural fairness percep-
also seemed to interact with contestability in perceptions of pro-
t i o n s   w e   e v a l u a te d   p e r c e p ti o n s  o f   (1 )  p r o c e du ra l   v o i c e ,  ( 2 )  i n f u e n c e   2
|     |     |     |     | cedural consistency ( |     |     |  (2, 254) = 3.83,  |     |  < 0.05,   = 0.03). More- |
| --- | --- | --- | --- | --------------------- | --- | --- | ------------------ | --- | ------------------------- |
o v e r   t h e   o u t c o m e ,   ( 3 )  c o n s i st e n c y   o f  t h e  p ro c e s s ,   (4 )   l a c k   of   b ia s ,   p
over, we checked the interaction of AI literacy and explanations
(5) accuracy of factors, (6) correctability, and (7) ethicality. We thus
on informational fairness perceptions by performing a multi-way
performed multi-way ANOVAs with explanations, human over-
sight, contestability, and task stakes as between-subjects factors,  ANOVA with explanations, human oversight, contestability, task
stakes, and AI literacy as between-subject factors and perceived
and the sub-elements that compose informational and procedural
informational fairness as the dependent variable. We found that AI
fairness perceptions as the dependent variables.
literacy may have an efect on perceptions of informational fairness

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
(  (1, 249) = 4.14,  < 0.05,  p 2 = 0.02) and that explanations and 5.3.4 Efects of Task Stakes. Our exploratory analyses surprisingly
AI literacy may interact (  (1, 249) = 4.19,  < 0.05,  p 2 = 0.02) in suggest that task stakes contribute to one item of procedural fair-
creating perceptions of informational fairness (see Figure 5). These ness perceptions: adequacy of factors (e.g., credit score, loan amount
results suggest that participants with low AI literacy rated informa- requested, total annual income) (  (1, 254) = 86.79,  < 0.001,  p 2 =
tional fairness perceptions negatively when no explanations were 0.25; see Figure 5). This suggests that users perceived the decision
given, but their perceptions of informational fairness substantially factors used in our scenario as less adequate for the low-stakes de-
increased when decisions were explained. The presence of expla- cision (holiday) than for the high-stakes decision (buying a house).
nations had a milder efect on informational fairness perceptions
among participants with higher AI literacy. 5.4 Qualitative Analysis
We performed our qualitative analysis using a refexive thematic
5.3.2 Efects of Human Oversight. Our exploratory analyses sug- analysis [19]. We inductively generated individual codes from the
gest that human oversight had no efect on any of the items that responses our participants gave to the open-ended questions and
contribute to procedural fairness perceptions individually. As a mat- we then clustered them into code groups. We identifed three main
ter of fact, our results show that the inclusion of human oversight tension areas: one related to perceptions of informational fairness
in the initial decision has a slight negative impact on perceptions and two related to perceptions of procedural fairness. This section
towards process consistency and lack of bias (Figure 4). Human explains each of those areas of tension in detail. For a comparison
oversight and contestability further seemed to interact in afecting and discussion between quantitative and qualitative results, see
procedural voice perceptions (  (2, 254) = 4.08,  < 0.05,  p 2 = 0.03) Sections 6.1, 6.2, and 6.3. We again refer to quotes as Q.i, where i is
and outcome infuence (  (2, 254) = 3.65,  < 0.05,  p 2 = 0.03). This
the index of a specifc quote. Appendix A shows all selected quotes.
result may suggest that confgurations where decision subjects can
5.4.1 Tension #1: Amount of Information vs. Generating Understand-
contest the decision basis of the process lead to varying degrees of ing for All. Our qualitative results indicate that getting detailed
procedural voice and outcome infuence perceptions depending on information about the decision was a general concern among par-
whether the initial decision was overseen by a human or not. ticipants. Participants who were placed in a confguration without
explanation of the decision outcome directly highlighted the need
5.3.3 Efects of Contestability. In our exploratory analysis, we for the bank to give detailed explanations (115/133) about the
way in which diferent factors are used for making the decision and
found that contestability mainly contributed to the “correctabil-
the reasons for the outcome (Q.11). They also considered that the
ity” sub-element of procedural fairness perceptions (  (2, 254) =
108.29,  < 0.001,  p 2 = 0.46). This is somewhat unsurprising con- b o a f n a k c t s i h o o n u l ( d 3 4 p / r 1 o 3 v 3 i ; d Q e . 1 d 2 e ) c . i sion subjects with an alternative course
sidering that correctability directly refers to the requirement of
Participants who were placed in scenarios where the bank would
having an appeal process in place [62]. Interestingly, however, al-
ofer explanations of the decision outcome positively evaluated the
v
th
o
o
ic
u
e
g h
(
c
(
o
2
n
, 2
te
5
s
4
t
)
a b
=
i li
1
t
3
y
. 7
se
6
e
,
m e
<
d
0
to
.0 i
0
m
1,
p

ro
p 2
v
=
e p
0
e
.
r
1
c
)
e
,
p
th
ti
e
o n
m
s
e
o
a
f
n
p r
v
o
a
c
l
e
u
d
e
u
s
r
o
a
f
l
l
a
e
p
v
p
e
r
l
e
o
ci
f
a t
d
e
e
d
t a
t
i
h
l
e
o
f
f
a
t
c
h
t
i
t
s
h a
in
t
f
t
o
h
r
e
m
c
a
o
t
u
io
n
n
te r
(7
fa
0
c
/
t
1
u
3
a
4
l
) .
s c
T
e
h
n
e
a
y
ri o
g
s
e n
g
e
a
r
v
a
e
l l
a
y
c t
a
io
ls
n
o
-
perceived procedural voice are still below zero (on a [−3, 3] scale) able information (21/134). Some of them requested further infor-
for all three confgurations: the confguration where there is no mation about the process and the algorithmic system itself
contestability (  = −1.84,   = 0.16), the confguration where (51/134; Q.13). However, some participants pointed out that in-
participants can contest the initial decision (  = −0.81,   = 0.17) creasing the amount of information could generate difculties in
and the confguration where participants can contest the decision- understanding (23/134) the explanations and could restrict such
maker (  = −0.65,   = 0.19) (Figure 4). The mean values for understanding to people with literacy in AI (Q.14).
perceptions of outcome infuence are also below zero for all three
confgurations: no contestability (  = −1.69,   = 0.16), contest 5.4.2 Tension #2: Human Involvement vs. Timely Decision-Making.
initial decision (  = −1.21,   = 0.16) and contest decision-maker Another major theme in our qualitative analysis was that of human
(  = −1.30,   = 0.16). This suggests that none of the contestation involvement. Our qualitative analysis suggests that, regardless of
mechanisms put in place may sufciently contribute to users’ sense the presence or absence of human oversight, participants were still
of having a voice in the process and infuence over the outcome asking for a higher degree of human involvement (75/267) in
(i.e., the frst two sub-elements that constitute procedural fairness the process (e.g., by including a human that deals with borderline
perceptions). Our exploratory results also do not point to any dif- cases, or by allowing decision subjects to personally interact with
ferences between contestation types for any of the sub-elements a bank employee). In cases where human oversight was included
that compose procedural fairness perceptions; except for ethicality in the original decision, our participants thought that this would
(  = −0.81,  < 0.05). This might indicate that, based on ethical ensure reliability. However, some (13/267) of them indicated that a
and moral standards, participants do require human intervention human should always make the fnal decision, for every instance
in the review process. Note that there is no interaction between (Q.15, Q.16).
contestation types and human oversight for ethicality, which could On the other hand, as some of our participants highlighted, not
suggest that having a human-in-the-loop confguration in the orig- having humans involved could make the process speedy (47/267)
inal decision is no substitute for human intervention in the review and would allow Kim to explore alternative options (Q.17). Although
process when upholding ethical standards. we did not explicitly compare the diference in time of having a

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
Figure 4: Efects of human oversight on perceptions of (a) process consistency and (b) lack of bias; efects of contestability on
perceptions of (c) procedural voice and (d) outcome infuence (HO = human oversight, C = contestation, ID = initial decision,
DM = decision-maker).
Figure 5: (a) Efect of task stakes on perceptions of factor adequacy (LS = Low stakes, HS = High stakes). (b) Interaction between
explanations and self-reported AI literacy on perceptions of informational fairness. Red refers to the confgurations where
explanations were given and Green refers to the confgurations with no explanations.
human or an algorithmic system (with or without human oversight) Q.26). Humans were viewed as being more fexible and prone to
making the decision, the presented scenario did mention that the give in to cases that are close to the decision boundary (Q.27).
reason for introducing algorithmic decision-making processes was Some participants pointed out that a human should be respon-
due to time constraints. Many participants referred to the temporal sible for double-checking boundary cases (Q.28). In those cases,
dimension as one that makes the process fair (Q.18, Q.19). participants requested the implementation of negotiation mecha-
nisms (Q.29) that would allow decision subjects to discuss with
humans (47/267; Q.30) who could treat the situation with compas-
5.4.3 Tension #3: Standardized Fact-based Process vs. Accounting for
Personal Circumstances. The fact that an algorithmic system was
sion (Q.31).
fully or mainly driving the process also encouraged refections on
the advantages and disadvantages of having a standardized process
6 DISCUSSION
that treats everyone equally (44/267; Q.20). Some of our partici-
pants considered that introducing algorithmic systems in decision- In this section, we relate quantitative results with qualitative ones
making processes helps to get rid of human biases (39/267). They and refect on our key fndings. Each subsection summarizes the
considered that thanks to such systems, the process would not results related to one of the tested factors and its entanglements
be subject to human subjectiveness and prejudice (Q.21). Intro- (i.e., explanations in Section 6.1, human oversight in Section 6.2,
ducing an algorithmic system was also viewed as contributing to and contestability in Section 6.3). We also list the practical impli-
the consistency of the decision-making process. Participants gen- cations of our fndings, highlight future challenges, and refect on
erally appreciated that the same information was considered for the benefts and shortcomings of adopting a multi-dimensional
everyone (Q.22). The basis of the decision-making process was also approach for capturing perceptions of fairness (Section 6.4). We
regarded as sound because it was based on facts (40/267; Q.23). fnally acknowledge the limitations of our study (Section 6.5).
Some (27/267) indicated that the bank should consider additional
factors when making a decision, but, in general terms, the presented
6.1 Leveraging Transparency Beyond Outcome
factors were considered fair and relevant (Q.24).
Despite the general sentiment of facts being a sound basis for Explanations
decision-making, some of our participants highlighted the need Our quantitative results show that explanations improve informa-
to sometimes consider individual circumstances (17/267; Q.25, tional fairness perceptions (see Section 5.2). Exploratory fndings

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
further suggest that AI literacy may moderate the efect of expla- for algorithmic systems to be biased (Q.20), suggesting that future
nations on informational fairness perceptions, i.e., indicating that explanations should also account for decision subjects’ imaginar-
the efect of explanations on informational fairness perceptions is ies [69] and expectations [54] around algorithmic systems.
stronger for participants with low AI literacy (see Section 5.3.1 and
Figure 5). However, contrary to our expectations, and to suggestions
6.2 Designing Appropriate Human-AI
from earlier work [83], we did not fnd evidence that explanations
moderate the efect of contestability on procedural fairness, i.e., Confgurations
help participants question structural aspects of the decision-making Our quantitative results do not contain any evidence that human
process such as the factors requested by the bank and how these are oversight would afect end users’ procedural fairness perceptions;
used. The insights we obtained from our qualitative analysis sug- in fact, a Bayesian analysis even revealed moderate evidence that
gest that participants were generally happy with the factual basis human oversight has no efect here (see Section 5). These results
of the decision in question (see Section 5.4). It should be noted that, resonate with earlier work on the topic [103], where a case-by-case
as opposed to earlier work [83] and our own preliminary study, we human intervention did not contribute to perceptions of fairness.
had decided to discard gender as one of the decision-making factors Nevertheless, our qualitative results suggest that, regardless of
in our main study because it is explicitly protected by law [14]. human oversight in the original decision, participants were still
This might have infuenced how people perceived the decision asking for a higher degree of human intervention (e.g., Q.15; see
basis. Moreover, some participants were asking for system-level Section 5.4). The reason for this might be that end users might
explanations that would enable them to explore and evaluate biases think about the decision-maker in binary terms, as either “a human”
encoded in the algorithmic system. The lack of this information or “not a human” [56]. Since, even in the scenario with human
might have prevented them from questioning additional aspects of oversight, the frst prediction was made by the algorithmic system,
the decision-making. our participants might still have thought about it as a non-human
Implications. Although our study replicated the fnding from ear- decision-maker. This would explain why human oversight did not
lier work that explanations support informational fairness percep- afect perceptions of procedural fairness and why, even in the case
tions [83] (which in turn contribute to overall fairness perceptions), where the decision was overseen by a human, participants were
restricting explanations to technical solutions that are currently asking for more human intervention in the process.
available through XAI may limit the grounds for contestations [67]. Implications. More research is needed to fnd adequate forms of
Our results (e.g., Q.13) suggest that providing decision subjects with human-AI collaborations in algorithmic decision-making processes.
information that goes beyond outcome explanations could support Future studies should go beyond confgurations where humans con-
contestations that are not only limited to post-decision mecha- frm the quality of the decision made by an algorithmic system [5]
nisms but that apply to the system lifecycle as a whole [2]. These and craft alternative human-AI teams. For instance, algorithmic
system-level explanations could include information about data, systems could access large quantities of data and perform prelimi-
algorithmic features, or the way in which algorithmic systems are nary analyses to produce easily digestible summaries for human
integrated in broader workfows [30]. For instance, previous studies experts to make fnal decisions [76]. Such a confguration would
have shown that data-centric explanations [7] have the potential respond to our participants’ desire to always have a human making
to assist users in assessing fairness. Future work should look into the last decision. A follow-up study to ours could test perceptions
explanations and transparency that go beyond outcomes and test towards human decision-making processes that are advised by algo-
how these insights afect perceptions of informational fairness and rithmic systems [12, 109] rather than algorithmic decision-making
whether they set grounds for contestations that go beyond appeal processes that are overseen by humans. One could argue that many
processes. We foresee that this would not only have implications studies have already studied diferent human-AI teaming confgura-
for perceptions of informational fairness but also for perceptions tions. However, these studies have mainly focused on exploring the
of procedural fairness. interaction of data domain experts (i.e., bank employees in our case)
Challenges. Previous research has demonstrated that increasing with algorithmic systems and distilling the efect on trust [75, 81]
levels of transparency can lead to information overload [22], so or trust-related constructs [100] such as reliance [77, 109]. Future
expanding explanations could restrict understanding to individuals studies should also capture end users’ fairness perceptions for each
with literacy in AI. Moreover, earlier work has pointed to a risk of those confgurations.
that malicious actors might use explanations to defraud algorith- Challenges. Including humans in algorithmic decision-making
mic systems [105] or to manipulate decision subjects by conveying processes costs time [20, 29, 68] and our qualitative results sug-
untruthful levels of “fairness” [68]. Future work should look into gest that participants value timely decision-making processes. For
methods for designing strategies that leverage adequate levels of appeal processes, Lyons et al. [68] found that, when subject to a
transparency [105] and that convey appropriate fairness perceptions trade-of situation, participants prioritised the type of review and
(i.e., condition that is satisfed if fairness perceptions towards a the review time rather than the reviewer. We emphasize the need
system are high when the system is indeed fair) [82]. Such strate- to perform more studies where participants are shown the time
gies should be adapted to decision subjects’ insight needs [88] and cost of diferent confgurations so as to capture their perceptions of
designed in a way that they would understand [11, 52]. For example, procedural fairness in a space of trade-ofs. Furthermore, our partic-
these could include videos [93], stories [93], or comics [102, 104]. ipants regarded confgurations with no human intervention as less
Our qualitative analysis further revealed some participants’ feel- biased and more consistent. We echo Almada [5] and suggest that
ing that the process could not be biased because it is impossible comparative measures of performance of human-controlled and

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
fully automated procedures should be included. This would allow that they want to provide along with the ability to infuence the
end users to freely shape their preferences and fairness perceptions logics of the decision-making process [60]. A promising research
in an informed way. line in this feld is that of interactive contestations [45].
Challenges. A major challenge when trying to give efective out-
come infuence to decision subjects is the distribution of levels of
6.3 Giving Voice to Decision Subjects control across individuals. Since the process will eventually infu-
As we hypothesized, our quantitative results show that including ence multiple people rather than one individual, the way in which
contestability (in the form of appeal processes) enhances people’s this control is distributed remains a key challenge [71]. We consider
perceptions of procedural fairness. Our qualitative results back up that participatory design strategies [43], such as the workshops
the value that participants put on the ability to contest the decision. conducted by Vaccaro et al. [94], can help deal with the trade-ofs
Despite the positive efect of contestability on perceptions of proce- identifed in our qualitative analysis. These workshops facilitate
dural fairness, perceptions of procedural voice and infuence over conversations among diferent stakeholders (e.g., the development
the outcome were still negative. In a within-subjects user study, team and decision subjects) and could, therefore, help identify the
Lyons et al. [68] found that participants perceived the new informa- compromises in designing contestation mechanisms that attend
tion appeal condition (equivalent to our “option to contest the initial to individual circumstances while contributing to perceptions of
decision and provide additional information” appeal condition) as process consistency.
fairer than the rest of the suggested appeal processes. Contrary
to these fndings, we do not fnd any diferences between the sug-
gested appeal processes. This might be due to the between-subject
nature of our study. Lyons et al. [68] also found that the reason for
6.4 Multi-dimensional Measurement of Fairness
the preference towards this condition was that decision subjects
perceived they had a “voice” in the decision-making process. Our Perceptions
results contradict these fndings, and indicate that, even when any In this paper, we advocated for a multi-dimensional approach for
of the suggested appeal processes are in place, our participants did capturing perceptions of fairness, inspired by literature in human
not have the feeling that the decision subject had a voice in the decision-making. Our quantitative analyses confrm that informa-
process or infuence over the outcome. This discrepancy might be tional and procedural facets of fairness predict overall fairness per-
due to the nature of the performed analysis. Lyons et al. [68] arrived ceptions. Moreover, this multi-dimensional approach has enabled us
at this conclusion through a thematic analysis of qualitative data, to perform exploratory analyses that have generated a nuanced un-
whereas our results rely on quantitatively evaluating responses to derstanding of how people perceive each algorithmic confguration.
statements that directly address perceptions of procedural voice Our fndings, therefore, suggest that future studies and practical ap-
and infuence over the outcome. plications could beneft from adopting a multi-dimensional rather
Implications. Our fndings highlight that, although contestabil- than a one-dimensional approach.
ity enhances users’ perceptions of procedural fairness (which in Despite our promising fndings, using a tool that was designed for
turn contribute to overall fairness perceptions), more research in human decision-making to evaluate algorithmic decision-making
contestable AI is needed. The feld of contestable AI is still grow- may not encompass the unique challenges that the inclusion of
ing [3] and many of the guidelines on how to design for contesta- algorithmic systems bring to existing processes (as it is the case
bility are conceptual in nature [3, 44, 67]. Further research is neces- for other felds such as human-agent collaboration [23]). Our aim
sary to translate those conceptualizations into actual design guide- behind using this tool designed for human decision-making in an al-
lines [2, 60] and validate designs of contestable algorithmic systems. gorithmic context was to distil insights from it and to identify future
Our results also suggest the need to research into the design of con- research directions. There is evidence that suggests that decision
testation mechanisms that efectively provide voice and outcome subjects care about justice-related aspects in algorithmic decision-
infuence to decision subjects. Sarra [79] argue that a “dialectical making, as they care in human decision-making [17]. However, we
exchange” is necessary between decision subjects and human con- acknowledge that there are novel considerations that the usage of
trollers to efectively support contestability. This resonates with these systems results in [17] and that future work should consider.
our qualitative fndings: many of our participants were asking for For instance, the approach suggested by Colquitt [24] does not
options to personally discuss or negotiate the outcomes with hu- explicitly include the temporal dimension of the decision-making
mans. Our participants considered that discussing the decision with process as an attribute that contributes to perceptions of proce-
humans would potentially lead to a change in outcome for cases dural fairness. Through our qualitative analysis, we found that this
that were close to the decision boundary (e.g., Q.27, Q.28; in line aspect was paramount for our participants. We note that most of
with earlier work [36, 68]) and that humans would treat decision the criteria we evaluated were defned several decades ago. Due to
subjects with dignity and compassion (e.g., Q.31; also in line with societal changes and a change in perceptions of time brought in by
previous research [17, 68, 94]). These fndings further suggest that algorithmic systems, further research would be needed to consider
contestations might be better designed as dialogues [44, 53], rather and efectively evaluate speed of decision-making as a procedural
than mere appeal processes. When it comes to outcome infuence, justice principle [95]. We, therefore, encourage further research
future research should focus on ways of increasing the ability of into defning standardized methodological approaches that appro-
subjects to exercise agency and true infuence over the process [9]. priately capture perceptions of fairness across dimensions while
This entails allowing decision subjects to determine the input data being specifcally adapted to algorithmic decision-making.

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
6.5 Limitations that empirical studies are part of broader eforts to create method-
In this section, we summarize limitations of our study that could ological tools that consider diferent stakeholders’ (including deci-
represent threats to its validity. sion subjects) viewpoints in the design and evaluation processes of
Refections on our experimental setting. The design of our study algorithmic systems [78, 107].
might have had an impact on the obtained results. First, the between-
subjects nature of the study might have prevented participants from 7 CONCLUSION
comparing diferent algorithmic confgurations. The efects of task This paper presented a preregistered user study investigating how
stakes and human oversight might have been diluted because of varying levels of explanations, human oversight, and contestability
this. Second, the scenario used for conducting our controlled user for high-and low-stakes algorithmic loan approval scenarios afect
study presented a case that participants considered to be close to users’ informational, procedural, and overall fairness perceptions.
the decision boundary (see Q.27). This made the request to have a We found that explanations and contestability afect perceptions of
human involved in the decision-making process, for example, to informational and procedural fairness, respectively. We did not fnd
be especially relevant for some participants (see Q.28). Fairness evidence of the efect of human oversight and task stakes on these
perceptions and the desires expressed by participants might have measurements. We also found that perceptions of informational
been diferent if we had included scenarios with diferent character- and procedural fairness, independently, are positively related to per-
istics. Third, the design of our experiment described a loan denial ceptions of overall fairness, but their interaction is not signifcant.
scenario for an individual called Kim. As opposed to some other Through exploratory and qualitative analyses, we gave further in-
authors (e.g., [68, 103]) we decided to tell this story in the third sights into these relationships. Our exploratory analyses indicated
person [9, 83, 86] with no reference to the individuals’ personal that the suggested contestation mechanisms did not efectively
characteristics. The reason behind this design choice was to min- contribute to perceptions of procedural voice and outcome con-
imize, as far as possible, the outcome favourability bias [103]. In trol. Our exploratory analyses also pointed out that the suggested
the same line, we limited the interaction between participants and human oversight confguration slightly deteriorated perceptions
the algorithmic system to a one-shot interaction. Previous research of procedural consistency and lack of bias. Through a qualitative
has shown that, under repeated interactions, system favorability analysis, we found three main areas of tension that highlight the
towards the group that the decision subject belongs to has an efect need to assess algorithmic decision-making processes in a space of
on fairness perceptions [37]. Our results indicate that, generally trade-ofs. Our work, therefore, gives insights into how to design
speaking, participants were happy to endorse negative outcomes if algorithmic decision-making processes that foster feelings of justice
explanations and contestation mechanisms were in place. However, and addresses some of the HCI challenges that these systems have
outcome favourability bias might have resulted in diferent reac- brought in.
tions had we referred to a case where the participants themselves
had been denied a loan or had we disclosed the demographics of
ACKNOWLEDGMENTS
diferent individuals and asked participants to repeatedly interact
We thank Himanshu Verma, Alejandra Gomez Ortega, Wo Meijer, Di
with the algorithmic system. Fourth, although we varied the level
Yan, and Denis Bulygin for valuable feedback on previous versions
of stakes involved in the task and found that perceptions of infor-
of this paper. We also thank the anonymous reviewers for their
mational and procedural fairness are robust across stakes, our study
constructive and thoughtful reviews. We would like to express our
is still limited to a loan decision-making scenario. Results may vary
gratitude to our colleagues at StudioLab and the DCODE Network
depending on the context. Fifth, terminology has been claimed to
for helping us pilot test our study.
afect end users’ fairness perceptions [56]. Langer et al. [56] suggest
This work was partially supported by the European Union’s
that the usage of multi-item measurement tools softens the impact
Horizon 2020 research and innovation programme under the Marie
of terminology, an advice we followed when measuring percep-
Skłodowska-Curie grant agreement No 955990 and the EU Horizon
tions of informational and procedural fairness. However, results
2020 grant (grant 101016233) via the PERISCOPE (Pan-European
may have been diferent had we used terms such as algorithmic
Response to the ImpactS of COVID-19 and future Pandemics and
system, statistical model, or computing system instead of artifcial
Epidemics) project.
intelligence.
Generalizability across cultures. For our study we recruited par-
REFERENCES
ticipants from the Global North whose frst language was Eng-
lish. Previous work has shown that cultural and geographical dif- [1] J. Stacy Adams. 1965. Inequity in social exchange. In Advances in experimental
social psychology. Vol. 2. Academic Elsevier, 267–299.
ferences play a key role in perceptions towards algorithmic sys- [2] Kars Alfrink, Ianus Keller, Neelke Doorn, and Gerd Kortuem. 2022. Tensions
tems [10, 49, 97]. Thus, we acknowledge that our study is subject in transparent urban AI: designing a smart electric vehicle charge point. AI &
to representativeness limitations [61].
[3]
S
K
O
ar
C
s
I E
A
T
lf
Y
r in
(3
k ,
2
I
0
a
2
n
2
u
).
s K
h
e
t
l
t
l
p
e
s
r,
: /
G
/d
e
o
rd
i. o
K
r
o
g
r
/
t
1
u
0
e
.1 m
0
,
0
a
7
n
/s
d
0 0
N
1
e
4
e
6
l
-
k
0
e
2
D
2-
o
0
o
1
r
4
n
3
.
6
2
-
0
9
2 2. Contestable
Need to incorporate empirical ethics as part of broader design AI by Design: Towards a Framework. Minds and Machines (8 2022). https:
frameworks for algorithmic systems. Empirical studies represent a //doi.org/10.1007/s11023-022-09611-z
[4] Kars Alfrink, T. Turel, A. I. Keller, N. Doorn, and G. W. Kortuem. 2020. Con-
necessary strategy for testing the practical implications of theoreti-
testable City Algorithms. International Conference on Machine Learning Work-
cal claims. However, moving towards algorithmic decision-making shop.
processes that enhance decision subjects’ feelings of justice requires [5] Marco Almada. 2019. Human intervention in automated decision-making. In
Proceedings of the Seventeenth International Conference on Artifcial Intelligence
and Law. ACM, New York, NY, USA, 2–11. https://doi.org/10.1145/3322640.
3326699

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
[6] Alexander Amini, Ava P Soleimany, Wilko Schwarting, Sangeeta N Bhatia, [29] Berkeley J. Dietvorst, Joseph P. Simmons, and Cade Massey. 2015. Algorithm
and Daniela Rus. 2019. Uncovering and Mitigating Algorithmic Bias through aversion: People erroneously avoid algorithms after seeing them err. Journal
Learned Latent Structure. In Proceedings of the 2019 AAAI/ACM Conference on of Experimental Psychology: General 144, 1 (2015), 114–126. https://doi.org/10.
AI, Ethics, and Society (AIES ’19). Association for Computing Machinery, New 1037/xge0000033
York, NY, USA, 289–295. https://doi.org/10.1145/3306618.3314243 [30] Jonathan Dodge, Q. Vera Liao, Yunfeng Zhang, Rachel K. E. Bellamy, and Casey
[7] Ariful Islam Anik and Andrea Bunt. 2021. Data-Centric Explanations: Explain- Dugan. 2019. Explaining Models: An Empirical Study of How Explanations
ing Training Data of Machine Learning Systems to Promote Transparency. In Impact Fairness Judgment. (1 2019). https://doi.org/10.1145/3301275.3302310
Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems. [31] Tim Draws, Zoltán Szlávik, Benjamin Timmermans, Nava Tintarev, Kush R.
ACM, New York, NY, USA. https://doi.org/10.1145/3411764.3445736 Varshney, and Michael Hind. 2021. Disparate Impact Diminishes Consumer
[8] Karl Aquino. 1995. Relationships among pay inequity, perceptions of procedural Trust Even for Advantaged Users. (1 2021). https://doi.org/10.1007/978-3-030-
justice, and organizational citizenship. Employee Responsibilities and Rights 79460-6{_}11
Journal 8, 1 (3 1995), 21–33. https://doi.org/10.1007/BF02621253 [32] Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Richard
[9] Theo Araujo, Natali Helberger, Sanne Kruikemeier, and Claes H. de Vreese. Zemel. 2012. Fairness through Awareness. In Proceedings of the 3rd Innovations in
2020. In AI we trust? Perceptions about automated decision-making by artifcial Theoretical Computer Science Conference (ITCS ’12). Association for Computing
intelligence. AI & SOCIETY 35, 3 (9 2020), 611–623. https://doi.org/10.1007/ Machinery, New York, NY, USA, 214–226. https://doi.org/10.1145/2090236.
s00146-019-00931-w 2090255
[10] Edmond Awad, Sohan Dsouza, Richard Kim, Jonathan Schulz, Joseph Henrich, [33] Bora Edizel, Francesco Bonchi, Sara Hajian, André Panisson, and Tamir Tassa.
Azim Sharif, Jean-François Bonnefon, and Iyad Rahwan. 2018. The Moral 2020. FaiRecSys: mitigating algorithmic bias in recommender systems. In-
Machine experiment. Nature 563, 7729 (11 2018), 59–64. https://doi.org/10. ternational Journal of Data Science and Analytics 9, 2 (2020), 197–213. https:
1038/s41586-018-0637-6 //doi.org/10.1007/s41060-019-00181-5
[11] Simone Bae, Reeva Lederman, and Tingru Cui. 2022. Understanding User [34] Franz Faul, Edgar Erdfelder, Albert-Georg Lang, and Axel Buchner. 2007.
Perception of Explainable Algorithmic Decision-Making Systems: A Systematic G*Power 3: a fexible statistical power analysis program for the social, behav-
Literature Review. (2022). ioral, and biomedical sciences. Behavior research methods 39, 2 (5 2007), 175–91.
[12] Gagan Bansal, Besmira Nushi, Ece Kamar, Daniel S. Weld, Walter S. Lasecki, and https://doi.org/10.3758/bf03193146
Eric Horvitz. 2019. Updates in Human-AI Teams: Understanding and Addressing [35] Thomas Franke, Christiane Attig, and Daniel Wessel. 2019. A Personal Resource
the Performance/Compatibility Tradeof. Proceedings of the AAAI Conference for Technology Interaction: Development and Validation of the Afnity for Tech-
on Artifcial Intelligence 33 (7 2019), 2429–2437. https://doi.org/10.1609/aaai. nology Interaction (ATI) Scale. International Journal of Human–Computer Inter-
v33i01.33012429 action 35, 6 (4 2019), 456–467. https://doi.org/10.1080/10447318.2018.1456150
[13] Julian Barling and Michelle Phillips. 1993. Interactional, Formal, and Distributive [36] Elena Fumagalli, Sarah Rezaei, and Anna Salomons. 2022. OK computer: Worker
Justice in the Workplace: An Exploratory Study. The Journal of Psychology 127, perceptions of algorithmic recruitment. Research Policy 51, 2 (3 2022), 104420.
6 (11 1993), 649–656. https://doi.org/10.1080/00223980.1993.9914904 https://doi.org/10.1016/j.respol.2021.104420
[14] Uladzislau Belavusau and Kristin Henrard. 2019. A Bird’s Eye View on EU [37] Meric Altug Gemalmaz and Ming Yin. 2022. Understanding Decision Subjects’
Anti-Discrimination Law: The Impact of the 2000 Equality Directives. German Fairness Perceptions and Retention in Repeated Interactions with AI-Based Deci-
Law Journal 20, 05 (7 2019), 614–636. https://doi.org/10.1017/glj.2019.53 sion Systems. In Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and
[15] R.J. Bies and J. F. Moag. 1986. Interactional Justice: Communication Criteria of Society. ACM, New York, NY, USA, 295–306. https://doi.org/10.1145/3514094.
Fairness. . Research on Negotiations in Organizations 1 (1986), 43–55. 3534201
[16] Robert J. Bies and Debra L. Shapiro. 1987. Interactional fairness judgments: [38] Jerald Greenberg. 1987. A Taxonomy of Organizational Justice Theories. The
The infuence of causal accounts. Social Justice Research 1, 2 (6 1987), 199–218. Academy of Management Review 12, 1 (1 1987), 9. https://doi.org/10.2307/257990
https://doi.org/10.1007/BF01048016 [39] Jerald Greenberg. 1990. Organizational Justice: Yesterday, Today, and Tomor-
[17] Reuben Binns, Max Van Kleek, Michael Veale, Ulrik Lyngs, Jun Zhao, and Nigel row. Journal of Management 16, 2 (6 1990), 399–432. https://doi.org/10.1177/
Shadbolt. 2018. ’It’s Reducing a Human Being to a Percentage’; Perceptions 014920639001600208
of Justice in Algorithmic Decisions. (1 2018). https://doi.org/10.1145/3173574. [40] J. Greenberg. 1993. The social side of fairness: Interpersonal and informational
3173951 classes of organizational justice. Justice in the workplace: Approaching fairness
[18] C. Malik Boykin, Sophia T. Dasch, Vincent Rice Jr., Venkat R. Lakshminarayanan, in human resource management. (1993), 79–103.
Taiwo A. Togun, and Sarah M. Brown. 2021. Opportunities for a More Interdis- [41] Nina Grgic-Hlaca, Muhammad Bilal Zafar, Krishna P. Gummadi, and Adrian
ciplinary Approach to Measuring Perceptions of Fairness in Machine Learning. Weller. 2016. The Case for Process Fairness in Learning: Feature Selection for
In Equity and Access in Algorithms, Mechanisms, and Optimization. ACM, New Fair Decision Making. In NIPS SYMPOSIUM ON MACHINE LEARNING AND THE
York, NY, USA, 1–9. https://doi.org/10.1145/3465416.3483302 LAW 8.
[19] Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology. [42] Moritz Hardt, Eric Price, and Nathan Srebro. 2016. Equality of Opportunity
Qualitative Research in Psychology 3, 2 (1 2006), 77–101. https://doi.org/10.1191/ in Supervised Learning. In Proceedings of the 30th International Conference on
1478088706qp063oa Neural Information Processing Systems (NIPS’16). Curran Associates Inc., Red
[20] Noah Castelo, Maarten W. Bos, and Donald R. Lehmann. 2019. Task-Dependent Hook, NY, USA, 3323–3331.
Algorithm Aversion. Journal of Marketing Research 56, 5 (10 2019), 809–825. [43] Katrina Heijne and Han van der Meer. 2019. Road Map for Creative Problem
https://doi.org/10.1177/0022243719851788 Solving Techniques Organizing and facilitating group sessions. Boom Uitgevers
[21] David Chan. 2011. Perceptions of fairness. Research Collection School of Social Amsterdam.
Sciences (2011). [44] Clément Henin and Daniel Le Métayer. 2021. Beyond explainability: justifability
[22] Hao-Fei Cheng, Ruotong Wang, Zheng Zhang, Fiona O’Connell, Terrance and contestability of algorithmic decision systems. AI & SOCIETY (7 2021).
Gray, F Maxwell Harper, and Haiyi Zhu. 2019. Explaining Decision-Making https://doi.org/10.1007/s00146-021-01251-8
Algorithms through UI: Strategies to Help Non-Expert Stakeholders. In Pro- [45] Tad Hirsch, Kritzia Merced, Shrikanth Narayanan, Zac E. Imel, and David C.
ceedings of the 2019 CHI Conference on Human Factors in Computing Systems Atkins. 2017. Designing Contestability. In Proceedings of the 2017 Conference on
(CHI ’19). Association for Computing Machinery, New York, NY, USA, 1–12. Designing Interactive Systems. ACM, New York, NY, USA. https://doi.org/10.
https://doi.org/10.1145/3290605.3300789 1145/3064663.3064703
[23] Nazli Cila. 2022. Designing Human-Agent Collaborations: Commitment, respon- [46] Harold Jefreys. 1939. Theory of Probability. (1939). (1939).
siveness, and support. In CHI Conference on Human Factors in Computing Systems. [47] Denise Jepsen and John Rodwell. 2009. A New Dimension of Organizational
ACM, New York, NY, USA, 1–18. https://doi.org/10.1145/3491102.3517500 Justice: Procedural Voice. Psychological Reports 105, 2 (10 2009), 411–426. https:
[24] Jason A. Colquitt. 2001. On the dimensionality of organizational justice: A //doi.org/10.2466/PR0.105.2.411-426
construct validation of a measure. Journal of Applied Psychology 86, 3 (6 2001), [48] Shalmali Joshi, Oluwasanmi Koyejo, Warut Vijitbenjaronk, Been Kim, and Joy-
386–400. https://doi.org/10.1037/0021-9010.86.3.386 deep Ghosh. 2019. Towards Realistic Individual Recourse and Actionable Expla-
[25] Jason A Colquitt and Jessica B Rodell. 2015. Measuring Justice and Fairness. nations in Black-Box Decision Making Systems. (7 2019).
In The Oxford Handbook of Justice in the Workplace. Oxford University Press. [49] Shivani Kapania, Oliver Siy, Gabe Clapper, Azhagu Meena SP, and Nithya Sam-
https://doi.org/10.1093/oxfordhb/9780199981410.013.0008 basivan. 2022. ”Because AI is 100% right and safe”: User Attitudes and Sources of
[26] Sasha Costanza-Chock. 2020. Design justice: Community-led practices to build AI Authority in India. In CHI Conference on Human Factors in Computing Systems.
the worlds we need. The MIT Press. ACM, New York, NY, USA, 1–18. https://doi.org/10.1145/3491102.3517533
[27] Russell Cropanzano. 2012. Justice in the Workplace: From theory To Practice. [50] Amir-Hossein Karimi, Gilles Barthe, Bernhard Schölkopf, and Isabel Valera. 2022.
Vol. 2. A survey of algorithmic recourse:contrastive explanations and consequential
[28] Morton Deutsch. 1975. Equity, equality, and need: What determines which value recommendations. Comput. Surveys (4 2022). https://doi.org/10.1145/3527848
will be used as the basis of distributive justice? Journal of Social Issues (1975), [51] Amir-Hossein Karimi, Bernhard Schölkopf, and Isabel Valera. 2021. Algorithmic
137–149. Recourse. In Proceedings of the 2021 ACM Conference on Fairness, Accountability,

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
and Transparency. ACM, New York, NY, USA, 353–362. https://doi.org/10.1145/ 2021.3115670
3442188.3445899 [73] Cathy O’neil. 2016. Weapons of math destruction: How big data increases in-
[52] Styliani Kleanthous, Maria Kasinidou, Pınar Barlas, and Jahna Otterbacher. 2022. equality and threatens democracy. Broadway Books.
Perception of fairness in algorithmic decisions: Future developers’ perspective. [74] Christina A. Pan, Sahil Yakhmi, Tara P. Iyer, Evan Strasnick, Amy X. Zhang, and
Patterns 3, 1 (1 2022), 100380. https://doi.org/10.1016/j.patter.2021.100380 Michael S. Bernstein. 2022. Comparing the Perceived Legitimacy of Content
[53] Daniel Kluttz, Nitin Kohli, and Deirdre K. Mulligan. 2018. Contestability and Moderation Processes: Contractors, Algorithms, Expert Panels, and Digital
Professionals: From Explanations to Engagement with Algorithmic Systems. Juries. Proceedings of the ACM on Human-Computer Interaction 6, CSCW1 (3
SSRN Electronic Journal (2018). https://doi.org/10.2139/ssrn.3311894 2022), 1–31. https://doi.org/10.1145/3512929
[54] Rafal Kocielnik, Saleema Amershi, and Paul N. Bennett. 2019. Will You Accept [75] Cecilia Panigutti, Andrea Beretta, Fosca Giannotti, and Dino Pedreschi. 2022.
an Imperfect AI?. In Proceedings of the 2019 CHI Conference on Human Factors in Understanding the impact of explanations on advice-taking: a user study for
Computing Systems. ACM, New York, NY, USA, 1–14. https://doi.org/10.1145/ AI-based clinical Decision Support Systems. In CHI Conference on Human Factors
3290605.3300641 in Computing Systems. ACM, New York, NY, USA, 1–9. https://doi.org/10.1145/
[55] Max F. Kramer, Jana Schaich Borg, Vincent Conitzer, and Walter Sinnott- 3491102.3502104
Armstrong. 2018. When Do People Want AI to Make Decisions?. In Proceedings [76] Andi Peng, Besmira Nushi, Emre Kıcıman, Kori Inkpen, Siddharth Suri, and Ece
of the 2018 AAAI/ACM Conference on AI, Ethics, and Society. ACM, New York, Kamar. 2019. What You See Is What You Get? The Impact of Representation
NY, USA, 204–209. https://doi.org/10.1145/3278721.3278752 Criteria on Human Bias in Hiring. Proceedings of the AAAI Conference on Human
[56] Markus Langer, Tim Hunsicker, Tina Feldkamp, Cornelius J. König, and Nina Computation and Crowdsourcing 7, 1 (10 2019), 125–134. https://ojs.aaai.org/
Grgić-Hlača. 2022. “Look! It’s a Computer Program! It’s an Algorithm! It’s AI!”: index.php/HCOMP/article/view/5281
Does Terminology Afect Human Perceptions and Evaluations of Algorithmic [77] Forough Poursabzi-Sangdeh, Daniel G Goldstein, Jake M Hofman, Jennifer Wort-
Decision-Making Systems?. In CHI Conference on Human Factors in Computing man Wortman Vaughan, and Hanna Wallach. 2021. Manipulating and Mea-
Systems. ACM, New York, NY, USA, 1–28. https://doi.org/10.1145/3491102. suring Model Interpretability. In Proceedings of the 2021 CHI Conference on
3517527 Human Factors in Computing Systems. ACM, New York, NY, USA, 1–52. https:
[57] Michael D. Lee and Eric-Jan Wagenmakers. 2014. Bayesian Cognitive Modeling. //doi.org/10.1145/3411764.3445315
Cambridge University Press. https://doi.org/10.1017/CBO9781139087759 [78] Inioluwa Deborah Raji, Andrew Smart, Rebecca N. White, Margaret Mitchell,
[58] Min Kyung Lee. 2018. Understanding perception of algorithmic decisions: Timnit Gebru, Ben Hutchinson, Jamila Smith-Loud, Daniel Theron, and Parker
Fairness, trust, and emotion in response to algorithmic management. Big Data Barnes. 2020. Closing the AI accountability gap. In Proceedings of the 2020
& Society 5, 1 (1 2018). https://doi.org/10.1177/2053951718756684 Conference on Fairness, Accountability, and Transparency. ACM, New York, NY,
[59] Min Kyung Lee and Su Baykal. 2017. Algorithmic Mediation in Group Decisions: USA, 33–44. https://doi.org/10.1145/3351095.3372873
Fairness Perceptions of Algorithmically Mediated vs. Discussion-Based Social [79] Claudio Sarra. 2020. Put Dialectics into the Machine: Protection against
Division. In Proceedings of the 2017 ACM Conference on Computer Supported Automatic-decision-making through a Deeper Understanding of Contestability
Cooperative Work and Social Computing (CSCW ’17). Association for Computing by Design. Global Jurist 20, 3 (10 2020). https://doi.org/10.1515/gj-2020-0003
Machinery, New York, NY, USA, 1035–1048. https://doi.org/10.1145/2998181. [80] Nripsuta Ani Saxena, Karen Huang, Evan DeFilippis, Goran Radanovic, David C.
2998230 Parkes, and Yang Liu. 2019. How Do Fairness Defnitions Fare?. In Proceedings
[60] Min Kyung Lee, Anuraag Jain, Hea Jin Cha, Shashank Ojha, and Daniel Kusbit. of the 2019 AAAI/ACM Conference on AI, Ethics, and Society. ACM, New York,
2019. Procedural Justice in Algorithmic Fairness. Proceedings of the ACM on NY, USA, 99–106. https://doi.org/10.1145/3306618.3314248
Human-Computer Interaction 3, CSCW (11 2019), 1–26. https://doi.org/10.1145/ [81] Philipp Schmidt and Felix Biessmann. 2020. Calibrating Human-AI Collabora-
3359284 tion: Impact of Risk, Ambiguity and Transparency on Algorithmic Bias. 431–449.
[61] Min Kyung Lee and Katherine Rich. 2021. Who Is Included in Human Perceptions https://doi.org/10.1007/978-3-030-57321-8{_}24
of AI?: Trust and Perceived Fairness around Healthcare AI and Cultural Mistrust. [82] Jakob Schoefer and Niklas Kuehl. 2021. Appropriate Fairness Perceptions? On
In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems. the Efectiveness of Explanations in Enabling People to Assess the Fairness of
ACM, New York, NY, USA, 1–14. https://doi.org/10.1145/3411764.3445570 Automated Decision Systems. In Companion Publication of the 2021 Conference
[62] Gerald S. Leventhal. 1980. What Should Be Done with Equity Theory? In Social on Computer Supported Cooperative Work and Social Computing. ACM, New
Exchange. Springer US, Boston, MA, 27–55. https://doi.org/10.1007/978-1-4613- York, NY, USA, 153–157. https://doi.org/10.1145/3462204.3481742
3087-5{_}2 [83] Jakob Schoefer, Niklas Kuehl, and Yvette Machowski. 2022. "There Is Not
[63] Q. Vera Liao and S. Shyam Sundar. 2022. Designing for Responsible Trust in Enough Information": On the Efects of Explanations on Perceptions of Informa-
AI Systems: A Communication Perspective. (4 2022). https://doi.org/10.1145/ tional Fairness and Trustworthiness in Automated Decision-Making. (5 2022).
3531146.3533182 https://doi.org/10.1145/3531146.3533218
[64] E. Allan Lind and Tom R. Tyler. 1988. The Social Psychology of Procedural Justice. [84] Andrew D Selbst and Julia Powles. 2017. Meaningful information and the
Springer US, Boston, MA. https://doi.org/10.1007/978-1-4899-2115-4 right to explanation. International Data Privacy Law 7, 4 (11 2017), 233–242.
[65] Jennifer M. Logg, Julia A. Minson, and Don A. Moore. 2019. Algorithm appreci- https://doi.org/10.1093/idpl/ipx022
ation: People prefer algorithmic to human judgment. Organizational Behavior [85] Debra L. Shapiro, E.Holly Buttner, and Bruce Barry. 1994. Explanations: What
and Human Decision Processes 151 (3 2019), 90–103. https://doi.org/10.1016/j. Factors Enhance Their Perceived Adequacy? Organizational Behavior and
obhdp.2018.12.005 Human Decision Processes 58, 3 (6 1994), 346–368. https://doi.org/10.1006/obhd.
[66] Chiara Longoni, Andrea Bonezzi, and Carey K Morewedge. 2019. Resistance 1994.1041
to Medical Artifcial Intelligence. Journal of Consumer Research 46, 4 (12 2019), [86] Megha Srivastava, Hoda Heidari, and Andreas Krause. 2019. Mathematical
629–650. https://doi.org/10.1093/jcr/ucz013 Notions vs. Human Perception of Fairness. In Proceedings of the 25th ACM
[67] Henrietta Lyons, Eduardo Velloso, and Tim Miller. 2021. Conceptualising SIGKDD International Conference on Knowledge Discovery & Data Mining. ACM,
Contestability: Perspectives on Contesting Algorithmic Decisions. (2 2021). New York, NY, USA, 2459–2468. https://doi.org/10.1145/3292500.3330664
https://doi.org/10.1145/3449180 [87] Emily Sullivan and Philippe Verreault-Julien. 2022. From Explanation to Rec-
[68] Henrietta Lyons, Senuri Wijenayake, Tim Miller, and Eduardo Velloso. 2022. ommendation: Ethical Standards for Algorithmic Recourse. In Proceedings of
What’s the Appeal? Perceptions of Review Processes for Algorithmic Decisions. the 2022 AAAI/ACM Conference on AI, Ethics, and Society. ACM, New York, NY,
In CHI Conference on Human Factors in Computing Systems. ACM, New York, USA, 712–722. https://doi.org/10.1145/3514094.3534185
NY, USA, 1–15. https://doi.org/10.1145/3491102.3517606 [88] Harini Suresh, Steven R. Gomez, Kevin K. Nam, and Arvind Satyanarayan. 2021.
[69] Jakub Mlynar, Farzaneh Bahrami, André Ourednik, Nico Mutzner, Himanshu Beyond Expertise and Roles: A Framework to Characterize the Stakeholders of
Verma, and Hamed Alavi. 2022. AI beyond Deus ex Machina – Reimagining Interpretable Machine Learning and their Needs. In Proceedings of the 2021 CHI
Intelligence in Future Cities with Urban Experts. In CHI Conference on Human Conference on Human Factors in Computing Systems. ACM, New York, NY, USA,
Factors in Computing Systems. ACM, New York, NY, USA, 1–13. https://doi.org/ 1–16. https://doi.org/10.1145/3411764.3445088
10.1145/3491102.3517502 [89] J. W. Thibaut and L. Walker. 1975. Procedural Justice: A Psychological Analysis.
[70] Rosanna Nagtegaal. 2021. The impact of using algorithms for managerial L. Erlbaum Associates, Hillsdale. (1975).
decisions on public employees’ procedural justice. Government Information [90] Tom R. Tyler. 1988. What is Procedural Justice?: Criteria used by Citizens to
Quarterly 38, 1 (1 2021), 101536. https://doi.org/10.1016/j.giq.2020.101536 Assess the Fairness of Legal Procedures. Law & Society Review 22, 1 (1988), 103.
[71] Yuri Nakao, Simone Stumpf, Subeida Ahmed, Aisha Naseer, and Lorenzo Strap- https://doi.org/10.2307/3053563
pelli. 2022. Towards Involving End-users in Interactive Human-in-the-loop AI [91] Berk Ustun, Alexander Spangher, and Yang Liu. 2019. Actionable Recourse in
Fairness. (4 2022). Linear Classifcation. In Proceedings of the Conference on Fairness, Accountability,
[72] Gideon Ogunniye, Benedicte Legastelois, Michael Rovatsos, Liz Dowthwaite, and Transparency. ACM, New York, NY, USA, 10–19. https://doi.org/10.1145/
Virginia Portillo, Elvira Perez Vallejos, Jun Zhao, and Marina Jirotka. 2021. 3287560.3287566
Understanding User Perceptions of Trustworthiness in E-Recruitment Systems. [92] Kristen Vaccaro, Karrie Karahalios, Deirdre K. Mulligan, Daniel Kluttz, and Tad
IEEE Internet Computing 25, 6 (11 2021), 23–32. https://doi.org/10.1109/MIC. Hirsch. 2019. Contestability in Algorithmic Systems. In Conference Companion

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
Publication of the 2019 on Computer Supported Cooperative Work and Social Com-
puting. ACM, New York, NY, USA, 523–527. https://doi.org/10.1145/3311957.
3359435
[93] Kristen Vaccaro, Christian Sandvig, and Karrie Karahalios. 2020. "At the End
of the Day Facebook Does What ItWants". Proceedings of the ACM on Human-
Computer Interaction 4, CSCW2 (10 2020), 1–22. https://doi.org/10.1145/3415238
[94] Kristen Vaccaro, Ziang Xiao, Kevin Hamilton, and Karrie Karahalios. 2021.
Contestability For Content Moderation. Proceedings of the ACM on Human-
Computer Interaction 5, CSCW2 (10 2021), 1–28. https://doi.org/10.1145/3476059
[95] Annukka Valkeapää and Tuija Seppälä. 2014. Speed of Decision-Making as
a Procedural Justice Principle. Social Justice Research 27, 3 (9 2014), 305–321.
https://doi.org/10.1007/s11211-014-0214-6
[96] Niels van Berkel, Jorge Goncalves, Daniel Russo, Simo Hosio, and Mikael B.
Skov. 2021. Efect of Information Presentation on Fairness Perceptions of
Machine Learning Predictors. In Proceedings of the 2021 CHI Conference on
Human Factors in Computing Systems. ACM, New York, NY, USA, 1–13. https:
//doi.org/10.1145/3411764.3445365
[97] Niels van Berkel, Eleftherios Papachristos, Anastasia Giachanou, Simo Hosio,
and Mikael B. Skov. 2020. A Systematic Assessment of National Artifcial
Intelligence Policies: Perspectives from the Nordics and Beyond. In Proceedings of
the 11th Nordic Conference on Human-Computer Interaction: Shaping Experiences,
Shaping Society. ACM, New York, NY, USA, 1–12. https://doi.org/10.1145/
3419249.3420106
[98] Arnaud Van Looveren and Janis Klaise. 2021. Interpretable Counterfactual
Explanations Guided by Prototypes. 650–665. https://doi.org/10.1007/978-3-
030-86520-7{_}40
[99] Suresh Venkatasubramanian and Mark Alfano. 2020. The philosophical ba-
sis of algorithmic recourse. In Proceedings of the 2020 Conference on Fair-
ness, Accountability, and Transparency. ACM, New York, NY, USA, 284–293.
https://doi.org/10.1145/3351095.3372876
[100] Oleksandra Vereschak, Gilles Bailly, and Baptiste Caramiaux. 2021. How to
Evaluate Trust in AI-Assisted Decision Making? A Survey of Empirical Method-
ologies. Proceedings of the ACM on Human-Computer Interaction 5, CSCW2 (10
2021), 1–39. https://doi.org/10.1145/3476068
[101] Sandra Wachter, Brent Mittelstadt, and Chris Russell. 2017. Counterfactual
Explanations without Opening the Black Box: Automated Decisions and the
GDPR. (11 2017).
[102] Danding Wang, Qian Yang, Ashraf Abdul, and Brian Y Lim. 2019. Designing
Theory-Driven User-Centric Explainable AI. In Proceedings of the 2019 CHI
Conference on Human Factors in Computing Systems. Association for Computing
Machinery, New York, NY, USA, 1–15. https://doi.org/10.1145/3290605.3300831
[103] Ruotong Wang, F. Maxwell Harper, and Haiyi Zhu. 2020. Factors Infuencing
Perceived Fairness in Algorithmic Decision-Making. In Proceedings of the 2020
CHI Conference on Human Factors in Computing Systems. ACM, New York, NY,
USA, 1–14. https://doi.org/10.1145/3313831.3376813
[104] Zezhong Wang, Jacob Ritchie, Jingtao Zhou, Fanny Chevalier, and Benjamin
Bach. 2021. Data Comics for Reporting Controlled User Studies in Human-
Computer Interaction. IEEE Transactions on Visualization and Computer Graphics
27, 2 (2 2021), 967–977. https://doi.org/10.1109/TVCG.2020.3030433
[105] Elizabeth Anne Watkins. 2021. The tension between information justice and
security: Perceptions of facial recognition targeting.. In Joint Proceedings of the
ACM IUI 2021 Workshops.
[106] Jenny S. Wesche and Andreas Sonderegger. 2019. When computers take the
lead: The automation of leadership. Computers in Human Behavior 101 (12 2019),
197–209. https://doi.org/10.1016/j.chb.2019.07.027
[107] Mireia Yurrita, Dave Murray-Rust, Agathe Balayn, and Alessandro Bozzon. 2022.
Towards a multi-stakeholder value-based assessment framework for algorithmic
systems. In 2022 ACM Conference on Fairness, Accountability, and Transparency.
ACM, New York, NY, USA, 535–563. https://doi.org/10.1145/3531146.3533118
[108] Brian Hu Zhang, Blake Lemoine, and Margaret Mitchell. 2018. Mitigating Un-
wanted Biases with Adversarial Learning. In Proceedings of the 2018 AAAI/ACM
Conference on AI, Ethics, and Society (AIES ’18). Association for Computing Ma-
chinery, New York, NY, USA, 335–340. https://doi.org/10.1145/3278721.3278779
[109] Qiaoning Zhang, Matthew L Lee, and Scott Carter. 2022. You Complete Me:
Human-AI Teams and Complementary Expertise. In CHI Conference on Human
Factors in Computing Systems. ACM, New York, NY, USA, 1–28. https://doi.org/
10.1145/3491102.3517791
[110] Jianlong Zhou, Sunny Verma, Mudit Mittal, and Fang Chen. 2021. Understanding
Relations Between Perception of Fairness and Trust in Algorithmic Decision
Making. (9 2021).

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
A SELECTED QUOTES
Selected quotes from the preliminary study (S1; see Section 4.1) and the main study (S2; see Section 4.2). Each quote comes with a reference
to the study where the response was collected and to the the participant (Pj) who gave it.
Q.id Quote Participant
Q.1 “It is unfair for her to be denied based on someone else’s previous inability to pay back the loan” S1-P42
Q.2 “Just because some had a similar case as hers, does not prove that she would not be able to pay back S1-P36
the loan.”
Q.3 “The best explanation gives the largest volume of information including how the decision was made S1-P50
and what amount she could potentially lend”
Q.4 “It explains the importance of each factor so she is able to see clearly what factors are most infuential” S1-P32
Q.5 “It boils it down to very easy to digest reasons as to why Kim was rejected the loan request” S1-P29
Q.6 “It provides 3 diferent ways in which Kim could improve her chances of being accepted.” S1-P33
Q.7 “She should contest how little impact her employment has on the decisions since this is a big factor” S1-P22
Q.8 “Gender should be contested as is a discriminatory factor. Although all the variables in question are S1-P56
methods for the banks to discriminate against someone, gender is not within a person’s control and
therefore a bad measure of their character and choices.”
Q.9 “Artifcial intelligence does not take your lifestyle and circumstances into account.” S1-P46
Q.10 “It is assessing her by comparing her situation with another with similar salary & credit score & not S1-P53
taking her full circs [circumstances] into consideration.”
Q.11 “I think there should be a breakdown of what the artifcial intelligence looks for and what the decision S2-P5
is based on.”
Q.12 “They should ofer a detailed reason and list of suggested changes she could make to help her in her S2-P218
eforts”
Q.13 “It does not tell us enough about how the AI uses the information. The AI is programmed initially by a S2-P8
human. How can I be sure that no bias is involved in this programming of the algorithm? This would
be appropriate information to have.”
Q.14 “If Kim is not familiar with AI then she may not understand the process and view it negatively” S2-P135
Q.15 “[...] each application should be reviewed by a human, not just the ones which have low confdence” S2-P179
Q.16 “Maybe for it to be processed primarily by the AI but secondly by a human before the answer is S2-P226
fnalised. This could still be a quick process as the person wouldn’t have to spend much time on it but
it would mean the decision also had a human input.”
Q.17 “It is fairer than other options as [it] is quicker than a human decision -[it] allows customers to explore S2-P153
other options”
Q.18 “It is fair because with the help of its AI the application process is much faster and efcient” S2-P146
Q.19 “I do think it is fair, it is a quick and easy procedure” S2-P182
Q.20 “It’s fair because it can’t be biased because it’s AI” S2-P110
Q.21 “[...] it may be fair as an algorithm does not take into account factors such as someone’s manner or S2-P8
dress which may lead to an unconscious bias for or against an applicant when assessed by a human.”
Q.22 “It is very fair because all applicants are assessed using the same list of criteria.” S2-P85
Q.23 “It takes in essential information needed to evaluate weather a loan is risky from the bank’s point of S2-P98
view as a business deal, it doesn’t take feelings or emotions, just facts, and applies them to the bank’s
set criteria with which they are happy to give a loan out to.”
Q.24 “I think they have asked the correct information to see if an individual could be able to aford to pay S2-P34
back the loan.”
Q.25 “I think it is fair that it is based on the same factors for everyone but there are circumstances under S2-P51
which more personal information individual to their case should be taken into consideration.”
Q.26 “The AI system will only deal with data/numbers and won’t take into consideration Kim’s personal S2-P96
circumstances which could explain why she was rejected in the frst place. For example, many lost
their jobs due to no fault of their own during the pandemic and fell behind on bills etc. and many have
ended up in debt. If this was the case with Kim it wouldn’t really be fair based on the circumstances.”

CHI ’23, April 23–28, 2023, Hamburg, Germany Yurrita et al.
Q.27 “Everyone is treated the same, but it seems that if a human saw she was only 5% of having the loan, S2-P9
they would have just let it slide.”
Q.28 “There should be some human to evaluate those cases that are in the obscure region of the cutting-of S2-P209
point.”
Q.29 “If the person trying to get the loan is rejected within a small margin and appeals I believe they should S2-P185
be able to re-negotiate.”
Q.30 “They took the human element away, which allows for communication and some compromise.” S2-P245
Q.31 “[...] there will always be instances where an AI will get the decision wrong when a person land in a S2-P218
grey area/their circumstances fall into an area where a little compassion is needed.”
Table 4: Summary of some of our participants’ responses to the open ended questions. S1 = preliminary study, S2 = main study,
Pj = index of the participant.

Disentangling Fairness Perceptions in Algorithmic Decision-Making CHI ’23, April 23–28, 2023, Hamburg, Germany
B SUMMARY OF THE EXPERIMENTAL DESIGN
Parameters Conditions Descriptions
Explanation No explanation The artifcial intelligence system uses some of this information for making the loan decision.
With explanations In the email received by Kim, an explanation of how the decision-making system has
reached the conclusion is included. The email includes the importance that each piece of
information provided by Kim had in the fnal decision. Factors are listed from the most
important to the least important factor based on the bank’s criteria. The magnitude of the
contribution of each piece of information (negative (−) means that it contributed to the
rejection decision) is added between brackets:
Credit Score (−0.15) > Loan amount requested (−0.12)> Total annual income (−0.09)>
Loan purpose (+0.02)> Employment status (+0.02)> Loan amount term (months) (−0.03)>
Date of birth (+0.03)> Co-applicant (if any) income (+0.01)> Number of dependents
(−0.07)> Education (+0.02)
The email also includes information about scenarios where the individual would have been
granted the loan. Kim would have been granted a loan if one of the following scenarios
had been true:
• The loan amount requested had been 5% lower
• The total annual income of the individual had been 10% higher
• The credit score of the individual had been "Very Good"
Human oversight No human oversight Given the latest technological advances and in an efort to make loan decisions in a timely
manner, the loan application process is now fully automated. An artifcial intelligence sys-
tem receives the online requests and evaluates each case. An email is sent to the applicants
with the fnal verdict.
With human oversight Given the latest technological advances and in an efort to make loan decisions in a timely
manner, the loan application process is now hybrid: it combines artifcial intelligence with
human expertise. This involves a two-step approval process. In the frst step, an artifcial
intelligence system receives the online requests and evaluates each case. If the artifcial
intelligence system reaches a decision (approve or reject) with a high confdence, an email
is sent to the applicant with the fnal verdict. If the artifcial intelligence system has a low
confdence over the decision, there is a second step where a human oversees the decision
and makes the fnal verdict and an email is sent to the applicant.
Contestability No contestability Since the reason for introducing an artifcial intelligence system is to handle home loan
applications in a timely manner, Kim has no option to request a review of the decision.
Contest initial decision Kim has decided to appeal the decision and has asked for a review of the process. As part of
the review procedure, Kim has the opportunity to make objections about the initial decision
and provide any information to support the application. The same artifcial intelligence
system will then reevaluate the home loan application.
Contest decision maker Kim has decided to appeal the decision and has asked for a review of the process. As part
of the review procedure, Kim has the opportunity to ask for a human to review the process.
This human reviewer will make a completely new decision with the information that Kim
already provided for the initial decision.
Task stakes High stakes Buy a house / home loan
Low stakes Go on holiday / holiday loan
Table 5: Summary of the experimental design.