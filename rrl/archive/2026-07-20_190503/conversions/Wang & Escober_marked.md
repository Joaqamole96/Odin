Technologique: A Global Journal on Technological Developments and Scientific Innovations
Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1, 201 – 209 | ISSN Online: 3028-1415 | ISSN Print: 3028-1407
D20O2I6: , hVttopls. :7//,d Noio.o.1r g|h/1tt0p.s6:2//7d1o8i./ovrmg/c1a0.t.e6c2h7-1g8jt/dvsmi.c7a.1.t.eScCh--g0j2t2d6si-.072.15. SC-0226-025
___________________________________________________________________________________________
Article History:
Hybrid Recommendation System for Patient-Centric Initial submission: 18 February 2026
Traditional Chinese Medicine E-Commerce: A Rule- First decision: 20 February 2026
Revision received: 27 March 2026
Based Approach with Nlp And K-Nn Integration
Accepted for publication: 31 March 2026
Online release: 07 April 2026
Jiangyang Wang1
Rosicar E. Escober2, PhD, DIT
1Master of Science in Information Technology, Polytechnic University of the Philippines, Sta. Mesa, Manila, Philippines
2Associate Professorial Lecturer V, Polytechnic University of the Philippines, Sta. Mesa, Manila, Philippines
Abstract
Traditional Chinese Medicine (TCM) relies fundamentally on personalized "syndrome differentiation,"
yet transitioning this clinical precision to post-treatment medicine selection remains a significant
challenge in digital environments. In typical e-commerce settings, recommendation engines often
lack personalization, relying instead on generic best-seller lists or simplistic symptom-matching that
fails to leverage the wealth of patient-specific data available in TCM clinics. This recognized gap often
leads to patient non-adherence and suboptimal health outcomes, as existing systems face technical
hurdles such as the "cold-start" problem, where collaborative filtering fails new patients, and a lack
of clinical intelligence in pure content-based filtering (Ye et al., 2022). This study addresses these
issues by proposing a hybrid algorithm that integrates Natural Language Processing (NLP) for
symptom analysis with machine learning techniques like k-nearest neighbours (K-NN) to identify
similar patient profiles. By dynamically weighing clinical health records against digital purchase
behaviours, the system ensures transparency through Explainable AI (XAI) and maintains ethical
integrity through data anonymization. Ultimately, this research introduces a novel framework that
empowers TCM clinics to provide clinically aligned, trustworthy product suggestions, bridging the gap
between traditional healing wisdom and modern data-driven e-commerce to improve patient
adherence and retention.
Keywords: personalized treatment, Traditional Chinese Medicine (TCM), hybrid recommendation algorithm,
patient health records, collaborative filtering
Copyright @ 2026. The Author/s. Published by VMC Analytiks Multidisciplinary Journal News Publishing Services. Hybrid Recommendation System
for Patient-Centric Traditional Chinese Medicine E-Commerce: A Rule-Based Approach with Nlp And K-Nn Integration © 2026 by Jiangyang Wang
and Rosicar E. Escober is an open access article licensed under Creative Commons Attribution (CC BY 4.0). This permits the copying, redistribution,
remixing, transforming, and building upon the material in any medium or format for any purpose, even commercially, provided that appropriate credit
is given to the copyright owner/s through proper and standard citation.
INTRODUCTION
This research proposes a hybrid
recommendation system for Traditional Chinese
Medicine (TCM) e-commerce that integrates
patient health records with e-commerce
behavior. By combining content-based filtering,
which matches products to specific symptoms,
with collaborative filtering, which leverages the
experiences of similar patients, the system
provides personalized and clinically relevant
suggestions. The framework (Figure 1)
addresses the "cold-start" problem by
prioritizing clinical data for new users and
emphasizes transparency through explainable Figure 1
recommendations. Conceptual Framework
201

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

To  maintain  trust  and  efficacy,  the  system  Research  consistently  demonstrates  that
incorporates  a  feedback  loop  for  continuous  conventional  recommendation  algorithms
algorithmic improvement and adheres to strict  underperform  in  healthcare  contexts.  Ricci,
ethical  standards,  ensuring  data privacy  and  Rokach,  and  Shapira  (2021)  found  that
prioritizing clinical relevance over commercial  collaborative  filtering  achieves  only  61%
bias  to  improve  patient  adherence  and  accuracy for medical products compared to 85%
satisfaction.  for  general  goods,  primarily  due  to  sparse
|     |     |     |     |     | purchase histories and the cold-start problem.  |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
Statement of the Problem. The study aimed to  Liang et al. (2022) extended this finding to TCM
develop  an  application  integrating  content- platforms, reporting accuracy rates of only 48-
based  and  collaborative  filtering  for patient- 53%  when  applying  standard  algorithms  to
centric TCM e-commerce. Specifically, it sought  herbal  product  recommendations.  Content-
to answer the following questions:  based  filtering  approaches  face  their  own
|     |     |     |     |     | limitations; Zhang et al. (2022) documented that  |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- |
1.  What are the challenges with the current  such systems achieve only 57% accuracy in TCM
traditional  Chinese  Medicine  purchasing  applications due to difficulty capturing nuanced
| system?  |     |     |     |     | pattern  | differentiation,  | including  |     | the  complex  |
| -------- | --- | --- | --- | --- | -------- | ----------------- | ---------- | --- | ------------- |
1.1  Product  Discovery  and  Selection  herb-indication  relationships  central  to  TCM
|      | Challenges;                      |     |     |     | practice.  |     |     |     |     |
| ---- | -------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
| 1.2  | Integration with Clinical Care;  |     |     |     |            |     |     |     |     |
1.3 User Experience and Convenience; and,  Rule-based clinical decision support systems
1.4 Information and Education?  offer  a  compelling  alternative.  Sutton  et  al.
|     |     |     |     |     | (2020)  | documented  | an  | average  | 23%  |
| --- | --- | --- | --- | --- | ------- | ----------- | --- | -------- | ---- |
improvement in protocol adherence across 127
| 2. What  | is  the  | evaluation  | of  the  TCM  | E-  |     |     |     |     |     |
| -------- | -------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- |
commerce Recommendation System based  clinical  trials  of  rule-based  systems,  with
on the ISO 25010 characteristics?  particular  effectiveness  in  medication
management, where rule-based alerts reduced

3. What is the level of acceptability of the TCM  prescription errors by 34% (Wright et al., 2021).
E-COMMERCE SYSTEM in terms of:  Chen  et  al.  (2020)  demonstrated  that  rule-
|     |     |     |     |     | based  | approaches  | achieve  | 71%  | diagnostic  |
| --- | --- | --- | --- | --- | ------ | ----------- | -------- | ---- | ----------- |
3.1 Perceived Usefulness (PU);
3.2 Perceived Ease of Use (PEOU);  accuracy with limited data—a critical advantage
3.3 Attitude Toward Using (AT); and,  in  resource-constrained  settings  where
3.4 Behavioral Intention (BI)?  machine  learning  alternatives  would  require
|     |     |     |     |     | thousands  | of  | training  | examples.  | The  |
| --- | --- | --- | --- | --- | ---------- | --- | --------- | ---------- | ---- |
LITERATURE REVIEW  transparency  of  rule-based  logic  proves
|     |     |     |     |     | essential for clinical acceptance: Holzinger et  |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
The  digital  transformation  of  Traditional  al. (2021) found that 78% of clinicians prefer
rule-based over "black-box" AI systems, with
| Chinese  | Medicine  | (TCM)  | faces  significant  |     |     |     |     |     |     |
| -------- | --------- | ------ | ------------------- | --- | --- | --- | --- | --- | --- |
challenges  in  e-commerce  implementation.  adherence rates of 78% versus just 42% for
Reyes and Lim (2020) documented that 59% of  neural network-based alternatives.

Filipino patients distrust online TCM products
due  to  concerns  about  authenticity  and  the  Philippine-specific challenges compound these
|     |     |     |     |     | technical  | limitations.  | Dela  | Cruz  | et  al.  (2023)  |
| --- | --- | --- | --- | --- | ---------- | ------------- | ----- | ----- | ---------------- |
absence of practitioner guidance. This finding
underscores  the  critical  need  for  clinically  found that 85% of Filipino patients demand TCM-
integrated digital solutions. This trust deficit is  grounded  explanations,  while  62%  distrust
|             |     |              |          |         | purchase-history-based  |     |     | recommendations.  |     |
| ----------- | --- | ------------ | -------- | ------- | ----------------------- | --- | --- | ----------------- | --- |
| compounded  | by  | what  Amann  | et  al.  | (2020)  |                         |     |     |                   |     |
identify  as  the  "explainability  imperative"  in  These  findings  align  with  Holzinger  et  al.'s
healthcare  AI:  systems  must  provide  (2022)  broader  Southeast  Asian  research,
|     |     |     |     |     | which  | documented  | that  | traditional  | medicine  |
| --- | --- | --- | --- | --- | ------ | ----------- | ----- | ------------ | --------- |
transparent rationales for recommendations to
earn clinician and patient confidence.  users  exhibit  significantly  higher  trust  in
|     |     |     |     |     |     |     |     |     | 202  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

systems providing diagnostic rationales aligned  study's methodological choices: a rule-based
with indigenous medical frameworks. Bates et  clinical gatekeeper reinforced by collaborative
al.  (2021)  further  emphasize  that  clinical  filtering, evaluated through integrated technical
decision support systems achieve significantly  and user acceptance frameworks, and designed
higher  adoption  rates  when  designed  to  specifically for the Philippine TCM context with
complement  rather  than  disrupt  existing  its  unique  trust  dynamics  and  cultural
practitioner  workflows.  This  principle  guides  requirements.
| the  system's                            | design  | as  | a  collaborative  |     | tool  |              |     |     |     |     |
| ---------------------------------------- | ------- | --- | ----------------- | --- | ----- | ------------ | --- | --- | --- | --- |
| rather than a practitioner replacement.  |         |     |                   |     |       | METHODOLOGY  |     |     |     |     |
|                                          |         |     |                   |     |       |              |     |     |     |     |
The integration of ISO 25010 quality standards  The study utilized a Design Science Research
with the Technology Acceptance Model (TAM)  (DSR) approach to develop a rule-based TCM
|             |           |     |     |                |     | recommendation  | engine.  | The  | methodology  |     |
| ----------- | --------- | --- | --- | -------------- | --- | --------------- | -------- | ---- | ------------ | --- |
| evaluation  | provides  |     | a   | comprehensive  |     |                 |          |      |              |     |
framework  for  assessing  both  technical  followed  a  mixed-methods  framework,
excellence and user adoption potential. Wagner  integrating  quantitative  datasets  with
|     |     |     |     |     |     | qualitative  | practitioner  | insights  | to  address  |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------------- | --------- | ------------ | --- |
et al. (2020) validated this dual approach for
medical  software  evaluation,  demonstrating  systemic gaps in digital TCM e-commerce.
| that technically sophisticated systems often fail  |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Methods and Techniques of the Study
due to poor user acceptance, highlighting the
| importance  | of  | combining  |     | quality  | and  |     |     |     |     |     |
| ----------- | --- | ---------- | --- | -------- | ---- | --- | --- | --- | --- | --- |
Table 1
acceptance evaluations.
Summary of Research Objectives and Methodological

Framework
| Recent  | advances  | in  | hybrid  | architectures  |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
demonstrate promise for traditional medicine
| applications.  | Wong       | et  | al.  (2023) developed  |        | a     |     |     |     |     |     |
| -------------- | ---------- | --- | ---------------------- | ------ | ----- | --- | --- | --- | --- | --- |
| prototype      | combining  |     | rule-based             | logic  | with  |     |     |     |     |     |
machine learning for herbal formula selection,
| achieving  | 88%  | accuracy  | while  | maintaining  |     |     |     |     |     |     |
| ---------- | ---- | --------- | ------ | ------------ | --- | --- | --- | --- | --- | --- |
explainability for key decisions. Johnson et al.
| (2021) documented  |          | how  | rule-based  |              | antibiotic  |     |     |     |     |     |
| ------------------ | -------- | ---- | ----------- | ------------ | ----------- | --- | --- | --- | --- | --- |
| stewardship        | systems  |      | could       | be  updated  | to          |     |     |     |     |     |
reflect new resistance patterns in just 48 hours,  Primary data included 100 anonymized health
compared  to  weeks  required  for  machine  records  (2023-2025)  and  survey  responses
learning model retraining a flexibility advantage  from 159 participants. Secondary data regarding
particularly relevant for TCM's evolving clinical  product  safety  and  contraindications  were
| knowledge base.                                  |     |     |     |     |     | sourced from the Philippine FDA and DOST.  |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |
|                                                  |     |     |     |     |     |                                            |     |     |     |     |
| The literature establishes that effective TCM e- |     |     |     |     |     | Table 2                                    |     |     |     |     |
commerce  requires  hybrid  approaches  Demographic Distribution Analysis (N=159)
| combining  | clinical  | rules  | with  | algorithmic  |     |     |     |     |     |     |
| ---------- | --------- | ------ | ----- | ------------ | --- | --- | --- | --- | --- | --- |
personalization while maintaining transparency
and cultural appropriateness. Liu et al. (2022)
| reviewed  | 62  cases  | of  | AI-driven  | medication  |     |     |     |     |     |     |
| --------- | ---------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
errors, finding that 81% stemmed from systems'
| inability          | to              | properly  |         | account  | for        |     |     |     |     |     |
| ------------------ | --------------- | --------- | ------- | -------- | ---------- | --- | --- | --- | --- | --- |
| contraindications  |                 | that      | would   | be       | trivially  |     |     |     |     |     |
| encoded            | in  rule-based  |           | logic,  |          | a  safety  |     |     |     |     |     |
consideration  paramount  in  herbal  Medicine  The  development  followed  an  Agile  Scrum
where  complex  interactions  abound.  This  methodology  with  two-week  sprints.  The
evidence  collectively  justifies  the  present  technical stack included:
|     |     |     |     |     |     |     |     |     | 203  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

Rule  Engine:  Drools  Business  Rules  weekly  expert  reviews,  where  practitioners
Management System for clinical logic.  validated the clinical justifications and IF-THEN
|     |     |     |     |     |     | logical rules generated by the engine to ensure  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
Database: Postgre 8.0 with Redis caching for  they  met  the  requirements  for  Functional
high-performance requests.  Suitability under the ISO/IEC 25010 framework.
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Frontend:  Vue.js  for  a  multilingual  RESULTS AND DISCUSSION
| (English/Tagalog) user interface.  |     |     |     |     |     |       |             |     |              |     |                  |     |
| ---------------------------------- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ------------ | --- | ---------------- | --- |
|                                    |     |     |     |     |     | RQ1.  | Challenges  |     | in  Current  |     | TCM  Purchasing  |     |
Systems
| The                                          | architecture  |     | followed  | a   | modular  |     |     |     |     |     |     |     |
| -------------------------------------------- | ------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| microservices approach across four domains:  |               |     |           |     |          |     |     |     |     |     |     |     |
Survey results from 159 respondents revealed

systemic failures across all four investigated
1. Business Architecture: Implements clinical-
to-purchase  workflows  with  practitioner  dimensions.  Table  4  presents  the  severity
ratings for each challenge category.
oversight.

Table 4
| 2. Application  |     | Architecture:  |     | User  Interface:  |     |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Challenges in Current TCM Purchasing Systems
| Vue.js,  | React,  | and  | React  | Native  | (Mobile),  |     |     |     |     |     |     |     |
| -------- | ------- | ---- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Business Logic:

3. Rule Engine and Drools Rules, Integration
Layer: EHR FHIR Adapter and Payment API.

4. Data Architecture: Presentation Layer: React
| and  | Vite,  Application  |     | Layer:  | NestJS,  | Data  |     |     |     |     |     |     |     |
| ---- | ------------------- | --- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Access Layer: Prisma ORM, Database Layer:
PostgreSQL (NeonDB)

The  system  used  a  sequential  three-phase  The survey results reveal that the most critical
hybrid model where Collaborative Filtering (CF)
failures in current TCM e-commerce platforms
| reinforced   | the  | Content-Based  |     | (CBF)  | clinical  |                                                |              |     |       |           |        |        |
| ------------ | ---- | -------------- | --- | ------ | --------- | ---------------------------------------------- | ------------ | --- | ----- | --------- | ------ | ------ |
|              |      |                |     |        |           | lie  in                                        | Integration  |     | with  | Clinical  | Care,  | which  |
| gatekeeper.  |      |                |     |        |           | achieved the highest mean score of 4.40. This  |              |     |       |           |        |        |

category underscores a complete disconnect
| Table 3  |     |     |     |     |     | between online purchasing systems and actual  |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Synergy between Content-Based (CBF) and Collaborative
clinical practice. Users reported that platforms
Filtering (CF)
operate independently from the clinical journey
|     |     |     |     |     |     | (4.5),  | with  | no  | connection  |     | to  practitioner  |     |
| --- | --- | --- | --- | --- | --- | ------- | ----- | --- | ----------- | --- | ----------------- | --- |
diagnoses (4.6) or TCM pattern diagnoses (4.4).
|     |     |     |     |     |     | Furthermore,  |     |     | product  | recommendations  |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | --- | -------- | ---------------- | --- | --- |
frequently misalign with treatment plans (4.2),
|                                                   |     |     |     |     |     | and                                   | users       | are   | unable   | to             | share  purchase  |         |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------- | ----------- | ----- | -------- | -------------- | ---------------- | ------- |
|                                                   |     |     |     |     |     | suggestions                           |             | with  | their    | practitioners  |                  | (4.3),  |
|                                                   |     |     |     |     |     | indicating                            |             | that  | current  | platforms      | function         | as      |
|                                                   |     |     |     |     |     | purely                                | commercial  |       |          | ventures       | rather           | than    |
|                                                   |     |     |     |     |     | integrated extensions of healthcare.  |             |       |          |                |                  |         |
| The study adhered to the Philippine Data Privacy  |     |     |     |     |     |                                       |             |       |          |                |                  |         |
Act  (RA  10173)  through  data  anonymization.  Closely  following  is  the  Information  and
Education category, with a mean score of 4.38,
| System  | reliability  |     | and  | alignment  | with  |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
professional standards were ensured through  reflecting severe gaps in knowledge support.
|     |     |     |     |     |     |     |     |     |     |     |     | 204  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

Users lack guidance on proper product use (4.3)  RQ2.  Evaluation  of  the  TCM  E-commerce
|     |     |     |     |     |     |     | Recommendation  |     | System  |     | based  | on  the  | ISO  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --- | ------ | -------- | ---- |
and receive no education on foundational TCM
25010 characteristics.
principles (4.2). More critically, they cannot find

| reliable  | information  |     | on  expected  |     | treatment  |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Expert evaluation by 10 IT specialists yielded an
| outcomes  | (4.4),  | and  | there  | is  | no  outcome  |     |     |     |     |     |     |     |     |
| --------- | ------- | ---- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
overall quality score of 4.23/5.00 ("Very Good").
| tracking  | (4.6).  | This  | suggests  | that  | platforms  |     |     |     |     |     |     |     |     |
| --------- | ------- | ----- | --------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table 5 presents the detailed assessment.
| treat  TCM  | products  |     | as  simple  |     | commodities  |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |

| rather  | than  therapeutic  |     |     | interventions  |     | that  |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Table 5
require proper education, usage instructions,
ISO 25010 Quality Assessment Results
and ongoing monitoring ensuring effectiveness.

The Product Discovery and Selection category
| ranks  | third  with  |     | a  mean  | score  |     | of  4.16,  |     |     |     |     |     |     |     |
| ------ | ------------ | --- | -------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
highlighting significant challenges in how users
find and choose products. Users struggle to
match products with specific symptoms (4.3)
and find product descriptions overly technical
| (4.1).  The  | overwhelming  |     | number  |     | of  | options  |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | ------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
leads to decision paralysis (3.9), while limited
| comparison  | tools  |     | (4.0)  | further  | complicate  |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ------ | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |

| choices.  | Most  | critically,  | systems  |     | completely  |     |     |     |     |     |     |     |     |
| --------- | ----- | ------------ | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ignore users’ health history (4.5), revealing a
|     |     |     |     |     |     |     | The  system  | excelled  |     | in  Security  |     | (4.48)  | and  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------------- | --- | ------- | ---- |
fundamental lack of personalization that leaves  Functional Suitability (4.47), validating the rule-
patients  navigating  complex  purchasing  based  clinical  gatekeeper  approach.  Security
| decisions  | without  |     | relevant  |     | contextual  |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
scores reflect compliance with RA 10173 and
information.  address  privacy  concerns  identified  by  Dela
|           |       |             |     |      |              |     | Cruz      | et  al.   | (2023).  | Functional      |     | Suitability  |      |
| --------- | ----- | ----------- | --- | ---- | ------------ | --- | --------- | --------- | -------- | --------------- | --- | ------------ | ---- |
| Finally,  | User  | Experience  |     | and  | Convenience  |     |           |           |          |                 |     |              |      |
|           |       |             |     |      |              |     | confirms  | accurate  |          | implementation  |     | of           | TCM  |
received  a  mean  score  of  4.08,  indicating  diagnostic principles through 247 clinical rules.
notable but comparatively less severe friction  Compatibility  (3.65)  emerged  as  the  primary
points.  Users  experience  time-consuming  weakness,  reflecting  integration  challenges
purchasing processes (4.0) and are required to  with clinic EHR systems, a barrier documented
repeat health information with each visit (4.2),
by Häyrinen et al. (2022).
| while systems fail to remember preferences or  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
past  purchases  (4.3).  TCM-specific  customer  RQ3.  Level  of  acceptability  of  the  TCM  E-
support remains inadequate (4.1), and although  COMMERCE SYSTEM.
| checkout complexity scored lowest among all  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TAM survey results from 150 users revealed
sub-variables at 3.8, it still reflects a moderate
barrier. Collectively, these findings point to a  strong acceptance (3.91/5.00). Table 6 presents
lack  of  basic  personalization technology  and  the detailed results.

| user-centric  | design     |        | across  | the       | purchasing  |     |                                               |            |             |             |        |           |     |
| ------------- | ---------- | ------ | ------- | --------- | ----------- | --- | --------------------------------------------- | ---------- | ----------- | ----------- | ------ | --------- | --- |
| journey.      |            |        |         |           |             |     | The  Technology                               |            | Acceptance  |             | Model  | analysis  |     |
|               |            |        |         |           |             |     | reveals the strongest user acceptance in the  |            |             |             |        |           |     |
|               |            |        |         |           |             |     | Behavioral                                    | Intention  |             | dimension,  |        | with      | a   |
| Taken         | together,  | these  |         | variable  | averages,   |     |                                               |            |             |             |        |           |     |
ranging  from  4.40  to  4.08,  paint  a  composite score of 3.96, falling within the High
Agree to Strongly Agree range. This dimension
comprehensive picture of a market urgently in
need  of  intelligent,  clinically  integrated  reflects  users’  commitment  to  continued
recommendation engines that can bridge the  engagement and advocacy. Within this category,
Recommendation Willingness scored highest at
gap between practitioner-guided care and e-
commerce functionality.  4.00 (Strongly Agree), indicating that users are
|     |     |     |     |     |     |     |     |     |     |     |     |     | 205  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________
highly likely to recommend the platform to The third dimension, Perceived Ease of Use,
others, serving as a strong net promoter achieved a composite score of 3.89, placing it in
indicator and organic growth driver. the High Agree range, reflecting good usability
with minor hurdles. Among its sub-variables,
Table 6 Interface Intuitiveness scored highest at 3.96,
Technology Acceptance Model Results approaching the Strongly Agree threshold and
indicating well-designed core navigation that
supports easy interaction. Learning Effort
followed at 3.88, revealing a moderate learning
curve and highlighting the need for onboarding
optimization to help new users acclimate more
smoothly. The lowest sub-variable in this
dimension was Feature Understanding at 3.82,
which, while still in the Agree range, suggests
Regular Usage Intent followed closely at 3.97, that advanced features present some
demonstrating high retention potential and the complexity for users. This gradual decline from
establishment of a sustainable user base. interface intuitiveness to feature understanding
Slightly lower but still strong was Future indicates that while basic usage is
Exploration at 3.91, revealing user interest in straightforward, additional education around
additional features and presenting clear advanced functionalities would help users fully
opportunities for platform expansion. leverage the system’s capabilities.
Collectively, these sub-variables show that
users are not merely satisfied but actively The fourth dimension, Attitude Toward Using,
committed to continued use and advocacy. scored 3.85 in the High Agree range, revealing
positive but cautious user sentiment. Within this
The second-highest dimension is Perceived dimension, Usage Enjoyment ranked highest at
Usefulness, with a composite score of 3.94 in 3.94, indicating that users find the experience
the High Agree range, indicating that users pleasant, which contributes to good
recognize the platform’s practical value. Within engagement levels. Overall Impression came in
this dimension, Clinical Relevance achieved the at 3.87, reflecting a generally favorable view of
highest sub-variable score at 3.98, reflecting the platform and a solid brand perception. The
strong user trust in the medical lowest sub-variable in this category was
appropriateness of the system and establishing Preference over Traditional at 3.75, which, while
clinical credibility. still in the Agree range, showed notable
hesitation about replacing in-person care.
Discovery Speed followed at 3.95, indicating that Rather than indicating weakness, this
users acknowledge the time-saving benefits of positioning aligns with the platform’s design
the platform, which presents an opportunity to philosophy as a complement to professional
emphasize messaging efficiency. Selection healthcare rather than a substitute,
Accuracy scored 3.88, indicating moderate representing a healthy and appropriate stance
improvement over manual methods and for a clinical support tool.
suggesting room for better communication
around how the system enhances decision- Across all five TAM dimensions, the Overall TAM
making compared to traditional research Acceptance composite score reached 3.91,
approaches. Notably, while these scores are falling within the High Agree range and
positive, they are lower than the functionality indicating a strong, balanced positive reception.
ratings in previous sections, suggesting that The consistency across dimensions, ranging
users may not yet fully appreciate the platform’s from 3.85 in Attitude Toward Using to 3.96 in
transformative benefits, despite recognizing its Behavioral Intention, demonstrates balanced
current capabilities. development without significant gaps in user
206

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

acceptance.  Notably,  the  progression  from  This  study  conclusively  demonstrates  a
Perceived Ease of Use (3.89) through Perceived  successful bridge between clinical knowledge
Usefulness (3.94) to Behavioral Intention (3.96)  and digital commerce for Traditional Chinese
follows  the  classic  Technology  Acceptance  Medicine (TCM). By implementing a hybrid, rule-
Model  pattern,  in  which  positive  usability  based  system  that  respects  TCM  diagnostic
experiences lead to recognized value, which in  principles,  it  provides  transparent
turn drives commitment to continued use. The  recommendations  that  enhance  rather  than
slightly more reserved scores around replacing  undermine  the  patient-practitioner
traditional  care  (3.75)  represent  a  strategic  relationship. The high user acceptance scores,
advantage in healthcare, positioning the system  combined with strong technical quality metrics,
appropriately as a complement to professional  validate  this  approach  as  a  viable  and
practice. Collectively, these results suggest that  sustainable  framework  that  effectively
while users may not yet view the platform as  balances  algorithmic  precision  with
revolutionary compared to traditional methods,  interpretability  to  build  essential  trust  in
they clearly recognize its practical value and  healthcare AI.
| intend to incorporate it into their healthcare  |     |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
management routines, providing a sustainable  To  ensure  successful  implementation,
foundation for long-term growth and feature  immediate action should focus on enhancing
development.  clinical integration through standardized APIs
|     |     |     |     | and pilot programs with Metro Manila clinics.  |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
Conclusion.  The  study  conclusively  Concurrently,  short-term  development  must
demonstrates  that  a  hybrid,  rule-based  prioritize  mobile  optimization,  continuous
architecture  is  the  optimal  framework  for  quality  monitoring,  and  practitioner  training
Traditional  Chinese  Medicine  (TCM)  e- programs. For long-term impact and scalability,
commerce,  effectively  bridging  the  systemic  the  platform  should  pursue  regulatory
gap between clinical diagnosis and digital retail.  recognition,  expand  educational  content,  and
By implementing a "clinical gatekeeper" model,  establish formal partnerships with professional
the system addresses the profound failures and  organizations.  Crucially,  all  development
challenges of existing generic platforms.  phases  must  be  guided  by  an  unwavering
|     |     |     |     | ethical framework that prioritizes data privacy,  |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
The  evaluation  validated  that  the  system  practitioner autonomy, clinical appropriateness,
achieves  high  technical  quality,  earning  an  and cultural sensitivity, ensuring the technology
overall  average  of  4.23/5.00  across  ISO/IEC  serves  as  a  responsible  complement  to
25010 software characteristics. Specifically, the  traditional healing.
| high  scores  | in  | Security  and  | Functional  |     |     |     |     |
| ------------- | --- | -------------- | ----------- | --- | --- | --- | --- |
Suitability  confirm  that  the  rule-based  logic  Wang  Jiangyang:
|     |     |     |     | Author  | contributions.  |     |     |
| --- | --- | --- | --- | ------- | --------------- | --- | --- |
maintains therapeutic integrity and data safety.  Conceptualization,  Methodology,  Data
|     |     |     |     | collection, Analysis; and Results | Rosicar E.  |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
Furthermore,  the  research  confirms  that  Escober:  Supervision  of  the  system
combining  explicit  clinical  rules  with  development  and  writing,  Institutional  ethics,
collaborative filtering is essential for building  Contribution of ideas.
| trust in healthcare AI. This is supported by the  |             |        |                  |           |                     |                   |     |
| ------------------------------------------------- | ----------- | ------ | ---------------- | --------- | ------------------- | ----------------- | --- |
|                                                   |             |        |                  | Conflict  | of  interest.  The  | authors  declare  | no  |
| Technology                                        | Acceptance  | Model  | (TAM)  results,  |           |                     |                   |     |
conflict of interest.
| particularly  | the  high  | practitioner  | alignment  |     |     |     |     |
| ------------- | ---------- | ------------- | ---------- | --- | --- | --- | --- |

score  (4.45/5.00)  and  strong  behavioral  This  research  received  no
|     |     |     |     | Funding  | source.  |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- |
intention among users. Ultimately, this system  external funding.
represents a sustainable and ethical model for

Artificial intelligence use. Grammarly was used
| the  digital  | transformation  | of          | traditional  |            |                   |                   |     |
| ------------- | --------------- | ----------- | ------------ | ---------- | ----------------- | ----------------- | --- |
|               |                 |             |              | to  check  | the  correctness  | of  the  English  |     |
| medicine      | within  the     | Philippine  | healthcare   |            |                   |                   |     |
language used.
ecosystem.
|     |     |     |     |     |     |     | 207  |
| --- | --- | --- | --- | --- | --- | --- | ---- |

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

Ethics  approval  statement.  This  study  was  Holzinger, A., Carrington, A., & Müller, H. (2021).
approved by the PUP – University Research and  Comparison  of  physician  acceptance:
Extension Committee (PUP-UREC).  Rule-based  versus  deep  learning
|     |     |     |     |     |     | clinical  | support  | systems.  |     | Nature  |
| --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | --- | ------- |
Data availability statement. All data supporting  Machine Intelligence, 3(8), 645-652.
| the findings of this study are included within the  |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
manuscript and its supplementary materials.  Holzinger, A., Saranti, A., Molnar, C., Biecek, P.,
|     |     |     |     |     |     | & Samek, W. (2022). The trust gap in  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
Acknowledgement. (Not available)  traditional  medicine  AI:  Con-sumer
|     |     |     |     |     |     | perspectives in Southeast Asia. Nature  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
Publisher’s disclaimer. The views expressed in  Machine Intelligence, 4(2), 112-119.
| this article are those of the authors and do not  |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
necessarily reflect the views of the publisher.  Johnson, K. B., Wei, W. Q., Weeraratne, D., Frisse,
The publisher disclaims any responsibility for  M. E., Misulis, K., Rhee, K., Zhao, J., &
| errors or omissions.  |     |     |     |     |     | Snowdon,       | J.   | L.  (2021).  |                 | Pre-cision  |
| --------------------- | --- | --- | --- | --- | --- | -------------- | ---- | ------------ | --------------- | ----------- |
|                       |     |     |     |     |     | medicine       | and  | the  role    | of  rule-based  |             |
| REFERENCES            |     |     |     |     |     | systems        | in   | antibiotic   | stewardship.    |             |
|                       |     |     |     |     |     | International  |      | Journal      | of              | Medical     |
Amann, J., Blasimme, A., Vayena, E., Frey, D., &
Informatics, 145, 104321.
|     | Madai,  | V.  I.  (2020).  | Explainability  | for  |     |     |     |     |     |     |
| --- | ------- | ---------------- | --------------- | ---- | --- | --- | --- | --- | --- | --- |
artificial  intelligence  in  healthcare:  A  Liang, Y., Li, C., & Wang, J. (2022). Challenges in
multidisciplinary  perspective.  BMC  applying  collaborative  filtering  to
Medical  Informatics  and  Decision  Traditional  Chinese  Medicine  e-
|     | Making,  |     | 20(1),  | 1-9.  |     | commerce  |     | platforms.  |     | Health  |
| --- | -------- | --- | ------- | ----- | --- | --------- | --- | ----------- | --- | ------- |
https://doi.org/10.1186/s12911-020- Informatics  Journal,  28(1),  1-15.
|     | 01332-6  |     |     |     |     | https://doi.org/10.1177/146045822210755 |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- |

31
| Bates, D. W., Levine, D. M., Lian, H. G., & Kohane,  |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I. S. (2021). The role of clinical decision  Liu, Y., Wang, X., & Chen, H. (2022). Review of AI-
support in a digital world. BMJ Health &
|     |     |     |     |     |     | driven  | medication  |     | errors:  | The  |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | -------- | ---- |
Care Informatics, 28(1), e100318.  importance  of  deterministic  logic  in
|     |     |     |     |     |     | pharmacology. Clinical Pharmacology &  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
Chen, C., Liu, X., Peng, L., & Wu, X. (2020). Rule- Therapeutics, 111(3), 567-578.
|     | based clinical decision support systems  |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
in rural healthcare set-tings. NPJ Digital  Reyes,  R.,  &  Lim,  S.  (2020).  Digital  distrust:
Medicine, 3(1), 54-62.  Assessing consumer skepticism in the
|     |     |     |     |     |     | Philippine  |     | online  | TCM  | mar-ket.  |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ---- | --------- |
Dela Cruz, M., Santos, G., & Reyes, J. (2023).
Philippine Journal of Health Research,
|     | Enhancing                                   | patient                       | understanding  | in  |         | 9(1), 16-24.                       |     |                   |     |              |
| --- | ------------------------------------------- | ----------------------------- | -------------- | --- | ------- | ---------------------------------- | --- | ----------------- | --- | ------------ |
|     | digital TCM: A pilot study in Metro Manila  |                               |                |     |         |                                    |     |                   |     |              |
|     | clinics.                                    | Philippine Journal of Health  |                |     |         |                                    |     |                   |     |              |
|     |                                             |                               |                |     | Ricci,  | F.,  Rokach,                       |     | L.,  &  Shapira,  |     | B.  (2021).  |
|     | Research, 12(2), 45-58.                     |                               |                |     |         | Recommender systems handbook (3rd  |     |                   |     |              |
|     |                                             |                               |                |     |         | ed.). Springer.                    |     |                   |     |              |
Häyrinen, K., Saranto, K., & Nykänen, P. (2022).

Definition,  structure,  content,  use and  Sutton,  R.  T.,  Pincock,  D.,  Baumgart,  D.  C.,
impacts of electronic health records: A  Sadowski,  D.  C.,  Fedorak,  R.  N.,  &
review  of  the  research  literature.  Kroeker,  K.  I.  (2020).  An  overview  of
International  Journal  of  Medical  clinical  decision  support  systems:
Informatics, 77(5), 291-304.  Benefits,  risks,  and  strategies  for
|     |     |     |     |     |     | success. NPJ Digital Medicine, 3(1), 1-10.  |     |     |     |      |
| --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |                                             |     |     |     | 208  |

Technologique: A Global Journal on Technological Developments and Scientific Innovations
2026, Vol. 7, No.1 |https://doi.org/10.62718/vmca.tech-gjtdsi.7.1.SC-0226-025
___________________________________________________________________________________________

https://doi.org/10.1038/s41746-020-
0221-y

Wagner, S. J., Matek, C., & Schwenke, S. (2020).
Software quality standards in medical
| device  | software  | develop-ment:  |     | A   |
| ------- | --------- | -------------- | --- | --- |
systematic literature review. Journal of
Software: Evolution and Process, 32(3),
e2212.

Wong, H., Zhang, L., & Chen, Y. (2023). Hybrid
| systems    | for  herbal   | formula  | selection:      |     |
| ---------- | ------------- | -------- | --------------- | --- |
| Balancing  | transparency  |          | and  accuracy.  |     |
Artificial Intelligence in Medicine, 136,
102482.

Wright, A., Sittig, D. F., Ash, J. S., Feblowitz, J.,
Meltzer, S., McMullen, C., Guappone, K.,
Carpenter, J., Richardson, J., Simonaitis,
L., Evans, R. S., Nichol, W. P., & Middleton,
| B.  (2021).  | Rule-based        |     | alerts  and  | the  |
| ------------ | ----------------- | --- | ------------ | ---- |
| reduction    | of  prescription  |     | errors       | in   |
multi-hospital settings. Journal of the
| American  | Medical  |     | Informatics  |     |
| --------- | -------- | --- | ------------ | --- |
Association, 28(5), 941-950.

Ye, J., Zhang, Q., & Liu, Y. (2022). The impact of
| personalized  | guidance         |     | on          | patient  |
| ------------- | ---------------- | --- | ----------- | -------- |
| adherence     | in  traditional  |     | medi-cine.  |          |
Journal of Holistic Healthcare Research,
14(2), 201-215.

Zhang, Y., Liu, X., Chen, W., & Wang, K. (2022).
| Adaptation        | of  rule-based  |          | systems       | for  |
| ----------------- | --------------- | -------- | ------------- | ---- |
| TCM               | diagnosis       |          | and  pattern  |      |
| differentiation.  |                 | Journal  |               | of   |
Ethnopharmacology, 285, 114821.
  209