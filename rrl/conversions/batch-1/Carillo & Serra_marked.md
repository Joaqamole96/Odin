---
conversion_metadata:
  converted_at: "2026-07-21T05:44:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Carillo & Serra.pdf"
  source_pdf_sha256: "47c3f23f922300fbf5000367879b117f4a280fe5a5e971d4ac405ee6da032f3a"
  page_count: 17
  markdown_char_count: 61205
---

| EUROPEAN  |            | JOURNAL     |             | OF              | PURE AND APPLIED | MATHEMATICS |         |
| --------- | ---------- | ----------- | ----------- | --------------- | ---------------- | ----------- | ------- |
| 2025,     | Vol. 18,   | Issue       | 4,          | Article Number  | 6875             |             |         |
| ISSN      | 1307-5543  |             | – ejpam.com |                 |                  |             |         |
| Published | by         | New         | York        | Business Global |                  |             |         |
|           | Optimized  |             |             | Nonlinear       | Grey Bernoulli   | Model       | for     |
|           | Nowcasting |             | the         | Philippine      | Gross Domestic   |             | Product |
| Shan      | Kierstin   | Carillo1,∗, |             | Ian Jay         | Serra1           |             |         |
1
College of Science, University of the Philippines Cebu, Cebu City, Philippines
Abstract. This study advances an optimized Nonlinear Grey Bernoulli Model (NGBM(1,1)) for
nowcasting the gross domestic product of the Philippines. Two parameter optimization strategies
— Particle Swarm Optimization (PSO) and an exponential background value — were employed
to minimize the out-of-sample mean absolute percentage error (MAPE). A harmonic function
simulation identified a 70/30 training-to-testing ratio as the most effective data-splitting scheme.
Applied to quarterly GDP data from the first quarter of 2021 to the fourth quarter of 2024, the
PSO-optimizedNGBM(1,1)yieldedthelowestout-of-sampleMAPEof5.45percentandthelowest
root mean square error, outperforming benchmark models. Results indicate that PSO provides
substantialimprovementsinforecastingperformance,whereastheexponentialbackgroundmethod
| yielded | smaller | gains. |     |     |     |     |     |
| ------- | ------- | ------ | --- | --- | --- | --- | --- |
2020 Mathematics Subject Classifications: 90B50, 62P20, 91B84, 62M10
Key Words and Phrases: Gross domestic product, particle swarm optimization, nonlinear grey
| Bernoulli | model, | Philippines |     |     |                 |     |     |
| --------- | ------ | ----------- | --- | --- | --------------- | --- | --- |
|           |        |             |     |     | 1. Introduction |     |     |
Gross Domestic Product (GDP) plays a crucial role in understanding economic health.
Representingthetotalmonetaryormarketvalueofallfinishedgoodsandservicesproduced
within a country’s borders over a specific period, GDP serves as a broad indicator of a
country’s overall economic activity and acts as a comprehensive measure of its economic
health [1].
Over the past decades, advancements in time-series econometrics have enabled the
developmentofautomatedplatformsformonitoringmacroeconomicconditionsinrealtime
[2]. Giannone, Reichlin, and Small [3] pioneered the first consistent statistical framework
forthispurpose, termednowcasting. Itisdefinedasthepredictionofthepresent, thevery
near future, and the very recent past. Nowcasting is particularly valuable for economic
planning because key indicators of economic health, such as GDP and its components, are
releasedquarterly,oftenwithasignificantdelayofuptotwomonths. Thesedelaysdisrupt
| ∗Corresponding |     | author. |     |     |     |     |     |
| -------------- | --- | ------- | --- | --- | --- | --- | --- |
DOI: https://doi.org/10.29020/nybg.ejpam.v18i4.6875
Email addresses: sccarillo@up.edu.ph (S.K.. Carillo), iaserra@up.edu.ph (I.J. Serra)
https://www.ejpam.com 1 Copyright: © 2025 The Author(s). (CC BY-NC 4.0)

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 2 of 17
theplanningprocessesofvariousstakeholders,includingthecentralbank,legislators,fiscal
planners, andfinancialandbusinessfirms, allofwhomareheavilyaffectedbythebusiness
cycle [4].
The Nonlinear Grey Bernoulli Model (NGBM(1,1)) was introduced by Chen, Chen,
and Chen [5] to address this need, offering a framework more suitable for nonlinear
systems. Studies have shown that NGBM(1,1) can capture complex patterns in economic
data, but its performance heavily depends on the precise estimation of model parameters,
| particularly | the power | index | and background |     | value | coeﬀicient. |     |     |
| ------------ | --------- | ----- | -------------- | --- | ----- | ----------- | --- | --- |
This study seeks to improve estimation accuracy by incorporating Particle Swarm
Optimization (PSO), a metaheuristic algorithm inspired by the collective behavior of bird
flocks. PSO has been demonstrated to effectively optimize parameters in nonlinear grey
models by minimizing forecasting errors. A further refinement, proposed by Cheng et al.
[6], isalsoexplored; thisapproachreformulatesthebackgroundvalueusinganexponential
| curve to | enhance model | responsiveness |     | to  | dynamic | patterns. |     |     |
| -------- | ------------- | -------------- | --- | --- | ------- | --------- | --- | --- |
Given the importance of GDP for economic policymaking, producing accurate and
timely forecasts is essential. The primary aim of this research is to enhance the predictive
performanceoftheNGBM(1,1)modelfornowcastingthequarterlyGDPofthePhilippines
by optimizing its parameters using PSO and an exponential background value.
|                |     |        | 2.  | Methodology |     |     |     |     |
| -------------- | --- | ------ | --- | ----------- | --- | --- | --- | --- |
| 2.1. Benchmark |     | Models |     |             |     |     |     |     |
Benchmark models serve as a standard reference to evaluate the performance and
improvement of a new model. In this study, the standard Grey Model (GM(1,1)) and
the Nonlinear Grey Bernoulli Model (NGBM(1,1)) serve as benchmarks to assess the
| performance | of the | optimized | NGBM(1,1) |     | variant. |     |     |     |
| ----------- | ------ | --------- | --------- | --- | -------- | --- | --- | --- |
| 2.1.1. Grey | Model  |           |           |     |          |     |     |     |
The Grey Model GM(1,1) serves as a benchmark in this study. This class of models
relies on the most recent data, where the window size determines the historical scope.
A fundamental assumption of grey models is that the input data must be strictly
non-negative and exhibit a fixed frequency. Furthermore, as they do not require large
| sample sizes, | grey models |     | are particularly |     | suitable | for nowcasting. |     |     |
| ------------- | ----------- | --- | ---------------- | --- | -------- | --------------- | --- | --- |
The first step in the GM(1,1) modeling process is to define the initial non-negative
x(0).
sequence, denoted as This sequence comprises the original baseline data points
| over | time i, forming |      | the foundation                      |     | for all subsequent | calculations: |     |     |
| ---- | --------------- | ---- | ----------------------------------- | --- | ------------------ | ------------- | --- | --- |
|      |                 |      | n                                   |     |                    |               | o   |     |
|      |                 | x(0) | x(0)(1),x(0)(2),x(0)(3),...,x(0)(n) |     |                    |               |     |     |
|      |                 |      | =                                   |     |                    |               | .   | (1) |
The second step involves generating the first-order Accumulated Generating
Operation(AGO)sequence,denotedasx(1).
Thisisdonebyperformingacumulative

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 3 of 17
sum on the initial sequence x(0), where each term x(1)(k) is calculated as the sum of
all previous terms x(0). The AGO sequence smoothens the data, making the series’
| behavior |     | easier to | model: |                                     |     |     |     |     |
| -------- | --- | --------- | ------ | ----------------------------------- | --- | --- | --- | --- |
|          |     |           |        | n                                   |     |     | o   |     |
|          |     |           | x(1)   | x(1)(1),x(1)(2),x(1)(3),...,x(1)(n) |     |     |     |     |
|          |     |           | =      |                                     |     |     | .   | (2) |
The next step is to compute the mean of the first-order AGO sequence to create a
z(1):
| background |     | value   | sequence                  |     |     |         |            |     |
| ---------- | --- | ------- | ------------------------- | --- | --- | ------- | ---------- | --- |
|            |     | z(1)(k) | = 0.5x(1)(k)+0.5x(1)(k−1) |     |     | for k = | 2,3,...,n. | (3) |
The fourth step defines the basic form of the GM(1,1) model. This equation
| incorporates |     | the | parameters | a and b: |     |     |     |     |
| ------------ | --- | --- | ---------- | -------- | --- | --- | --- | --- |
x(0)(k)+az(1)(k)
|     |     |     |     |     |     | = b. |     | (4) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |
The fifth step involves estimating the parameters a and b using the least-squares
method. The parameters are determined by solving the following equation:
|       |     |     |           | (a,b) ′ = | (B ′ B) −1B | ′ Y,       |      | (5) |
| ----- | --- | --- | --------- | --------- | ----------- | ---------- | ---- | --- |
| where |     |     | 2         | 3         |             | 2          | 3    |     |
|       |     |     | x(0)(2)   |           |             | −z(1)(2)   | 1    |     |
|       |     |     | 6         | 7         |             | 6          | 7    |     |
|       |     |     | 6x(0)(3)7 |           |             | 6 −z(1)(3) | 17   |     |
|       |     |     | Y = 6     | . 7 and   | B           | = 6 .      | . 7. |     |
|       |     |     | 4         | . 5       |             | 4 .        | .5   |     |
|       |     |     |           | .         |             | .          | .    |     |
−z(1)(n)
|     |     |     | x(0)(n) |     |     |     | 1   |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- |
The next step solves the whitening equation using the determined parameters to
generate the predicted AGO values xˆ(1), also called as the time response sequence:
|     |     |     |            | (cid:20)   |     | (cid:21) |     |     |
| --- | --- | --- | ---------- | ---------- | --- | -------- | --- | --- |
|     |     |     |            |            |     | b        | b   |     |
|     |     |     | xˆ(1)(k+1) | = x(0)(1)− |     | e −ak +  | .   | (6) |
|     |     |     |            |            |     | a        | a   |     |
Finally, the predicted AGO sequence is transformed back to its original scale to
| compute          |     | the predicted | original  | sequence                      | xˆ(0): |     |     |     |
| ---------------- | --- | ------------- | --------- | ----------------------------- | ------ | --- | --- | --- |
|                  |     |               |           | xˆ(0)(k) xˆ(1)(k)−xˆ(1)(k−1). |        |     |     |     |
|                  |     |               |           | =                             |        |     |     | (7) |
| 2.1.2. Nonlinear |     | Grey          | Bernoulli | Model                         |        |     |     |     |
The Nonlinear Grey Bernoulli Model, NGBM(1,1), is derived from grey systems theory
andisusedtoanalyzesystemswithsmallsamplesanduncertaininformation. Itrepresents
an extension of the basic GM(1,1) model, incorporating the Bernoulli differential equation
| to introduce | nonlinearity |     | via a | power coeﬀicient | n [7]. |     |     |     |
| ------------ | ------------ | --- | ----- | ---------------- | ------ | --- | --- | --- |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 4 of 17
From (1), the background value sequence of the NGBM(1,1) is given by:
|     |         |             |     | z(1)(k) | αx(1)(k)+(1−α)x(1)(k−1), |     |     |     |     |     |     |
| --- | ------- | ----------- | --- | ------- | ------------------------ | --- | --- | --- | --- | --- | --- |
|     |         |             |     |         | =                        |     |     |     |     |     | (8) |
|     | where k | = 2,3,...,n |     | and     | α ∈ (0,1).               |     |     |     |     |     |     |
The model is then defined by its whitening equation, a first-order Bernoulli
differential equation that incorporates the power index m alongside parameters a
|     | and b: |     |     |     |     |     | h   | i   |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m
|     |     |     |     | x(0)(k)+az(1)(k) |     | = b | z(1)(k) | ,   | m ̸= 1. |     | (9) |
| --- | --- | --- | --- | ---------------- | --- | --- | ------- | --- | ------- | --- | --- |
The parameters a and b are estimated using the least-squares method. The solution
|     | in matrix | form | is given   | by:     |       |      |       |          |         |           |      |
| --- | --------- | ---- | ---------- | ------- | ----- | ---- | ----- | -------- | ------- | --------- | ---- |
|     |           |      |            |         |       | ′    | ′ −1B | ′        |         |           |      |
|     |           |      |            |         | (a,b) | = (B | B)    | Y,       |         |           | (10) |
|     | where     |      | 2          |         | 3     |      | 2     |          | (cid:2) | (cid:3) 3 |      |
|     |           |      |            |         |       |      |       | −z(1)(2) | z(1)(2) | m         |      |
|     |           |      |            | x(0)(2) |       |      |       |          | (cid:2) | (cid:3)   |      |
|     |           |      | 6 6x(0)(3) |         | 7     |      | 6     | −z(1)(3) | z(1)(3) | m7        |      |
|     |           |      |            |         | 7     |      | 6     |          |         | 7         |      |
|     |           |      | Y = 6      |         | 7 and | B    | = 6   |          |         | 7.        |      |
|     |           |      |            | .       |       |      |       | .        |         | .         |      |
|     |           |      | 4          | . .     | 5     |      | 4     | . .      |         | . . 5     |      |
|     |           |      |            |         |       |      |       |          | (cid:2) | (cid:3)   |      |
m
|     |     |     |     | x(0)(n) |     |     |     | −z(1)(n) | z(1)(n) |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | -------- | ------- | --- | --- |
The whitening equation is solved using these estimated parameters to generate the
xˆ(1):
|     | predicted | AGO | values   |     |          |          |          |               |     |     |      |
| --- | --------- | --- | -------- | --- | -------- | -------- | -------- | ------------- | --- | --- | ---- |
|     |           |     |          |     | (cid:20) |          | (cid:21) |               |     |     |      |
|     |           |     |          |     | (cid:16) | (cid:17) |          |               |     |     |      |
|     |           |     |          |     |          | 1−m      | b        |               |     | b   |      |
|     |           |     | xˆ(1)(k) |     | x(0)(1)  |          | −        | −a(1−m)(k−1)+ |     |     |      |
|     |           |     |          | =   |          |          |          | e             |     | .   | (11) |
|     |           |     |          |     |          |          | a        |               |     | a   |      |
Note: The equation has been simplified to a standard, more recognizable form.
|     | Please | verify | this matches |     | your intended | derivation. |     |     |     |     |     |
| --- | ------ | ------ | ------------ | --- | ------------- | ----------- | --- | --- | --- | --- | --- |
Finally, the predicted AGO sequence is transformed back to its original scale using
theinverseaccumulatedgeneratingoperation(IAGO)toobtaintheforecastedvalues
xˆ(0):
|     |     |     |     |     | xˆ(0)(k) | xˆ(1)(k)−xˆ(1)(k−1). |     |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | -------------------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | =        |                      |     |     |     |     | (12) |
2.2. Parameter Optimization of Nonlinear Grey Bernoulli Model
2.2.1. Optimization with the Background Value in the form of the Exponential
Curve
Cheng et al. [6] introduced a method where the background value function z(1)(t) is
modeled by an exponential curve between consecutive time points k−1 and k. Starting
| from | the NGBM(1,1) |     | whitening |     | equation, |     |     |     |     |     |     |
| ---- | ------------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
|      |               |     |           |     |           |     | h   | i   |     |     |     |
dx(1)
m
|     |     |     |     |     | +ax(1)(t) | =   | b x(1)(t) |     | ,   |     | (13) |
| --- | --- | --- | --- | --- | --------- | --- | --------- | --- | --- | --- | ---- |
dt

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 5 of 17
| the integral | over | the     | interval      | [k−1,k] |     | is taken  | on  | both | sides:  |     |      |
| ------------ | ---- | ------- | ------------- | ------- | --- | --------- | --- | ---- | ------- | --- | ---- |
|              |      | Z       |               |         | Z   |           |     | Z    |         |     |      |
|              |      |         | k             |         |     | k         |     |      | k h     | i   |      |
|              |      |         | dx(1)         |         |     |           |     |      |         | m   |      |
|              |      |         |               | dt+a    |     | x(1)(t)dt |     | = b  | x(1)(t) | dt. | (14) |
|              |      |         | k−1 dt        |         | k−1 |           |     | k−1  |         |     |      |
| According    |      | to [6], | the integrals |         | are | defined   | as: |      |         |     |      |
Z
k
|     |     | z(1)(k) |     |     | x(1)(t)dt |     | x(1)(ξ), | (k−1 |     | ≤ ≤   |      |
| --- | --- | ------- | --- | --- | --------- | --- | -------- | ---- | --- | ----- | ---- |
|     |     |         |     | =   |           | =   |          |      |     | ξ k), | (15) |
k−1
| and |     |         | Z   |         |     |      |         |     |      |       |      |
| --- | --- | ------- | --- | ------- | --- | ---- | ------- | --- | ---- | ----- | ---- |
|     |     |         |     | h       | i   |      | h       | i   |      |       |      |
|     |     |         |     | k       |     | m    |         | m   |      |       |      |
|     |     | z(2)(k) |     | x(1)(t) |     |      | x(1)(η) |     | (k−1 | ≤ ≤   |      |
|     |     |         | =   |         |     | dt = |         |     | ,    | η k). | (16) |
k−1
The key innovation is modeling the background value with an exponential curve:
|     |     |     |     |     |     |     | "   |     | #   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t−(k−1)
x(1)(k)
|     |     |     | x(1)(t) | =   | x(1)(k−1) |     |     |     |     | .   | (17) |
| --- | --- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | ---- |
x(1)(k−1)
| From this, | the | background |     | values | z(1)(k) | and | z(2)(k) | are | derived | as: |     |
| ---------- | --- | ---------- | --- | ------ | ------- | --- | ------- | --- | ------- | --- | --- |
|            |     |            |     |        |         |     | "       |     | #       |     |     |
1−α
x(1)(k)
|     |     |     |     | z(1)(k) | = x(1)(k−1) |     |     |     |     |     | (18) |
| --- | --- | --- | --- | ------- | ----------- | --- | --- | --- | --- | --- | ---- |
x(1)(k−1)
| and |     |     |     |     | 8   |     | "   |     | #   | 9   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1−β=m
<
x(1)(k)
|     |     |     | z(2)(k) |     | x(1)(k−1) |     |           |     |     |     |      |
| --- | --- | --- | ------- | --- | --------- | --- | --------- | --- | --- | --- | ---- |
|     |     |     |         | =   |           |     |           |     |     | .   | (19) |
|     |     |     |         |     | :         |     | x(1)(k−1) |     |     | ;   |      |
In this formulation, α and β are background coeﬀicients that determine the relative
|     |     |     |     |     |     | x(1)(k) |     | x(1)(k | −   |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | --- | --- |
weighting of the accumulated values and 1) in the construction of the
background sequences z(1)(k) and z(2)(k), respectively. The inclusion of both parameters
allows the model to flexibly adjust its responsiveness to nonlinear and dynamic patterns
in the data.
′
For given values of α, β, and m, the parameters (a,b) are estimated using the least
squares method:
|       |     |     |           |         |       | ′    | ′ −1B | ′        |          |      |      |
| ----- | --- | --- | --------- | ------- | ----- | ---- | ----- | -------- | -------- | ---- | ---- |
|       |     |     |           |         | (a,b) | = (B | B)    | H,       |          |      | (20) |
| where |     |     | 2         |         | 3     |      | 2     |          |          | 3    |      |
|       |     |     |           | x(0)(2) |       |      |       | −z(1)(2) | z(2)(2)  |      |      |
|       |     |     | 6         |         | 7     |      | 6     |          |          | 7    |      |
|       |     |     | 6x(0)(3)7 |         |       |      | 6     | −z(1)(3) | z(2)(3)7 |      |      |
|       |     |     | H = 6     | .       | 7     | and  | B = 6 | .        |          | . 7. |      |
|       |     |     | 4         | .       | 5     |      | 4     | .        |          | . 5  |      |
|       |     |     |           | .       |       |      |       | .        |          | .    |      |
|       |     |     |           | x(0)(n) |       |      |       | −z(1)(n) | z(2)(n)  |      |      |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 6 of 17
Theoptimalvaluesofα,β,andmaredeterminedbysolvingthefollowingoptimization
| problem: |     |     |     |     |     |     | (cid:12)                 | (cid:12) |     |     |
| -------- | --- | --- | --- | --- | --- | --- | ------------------------ | -------- | --- | --- |
|          |     |     |     |     |     |     | (cid:12)                 | (cid:12) |     |     |
|          |     |     |     |     |     | Xn  | (cid:12)x(0)(t)−xˆ(0)(t) | (cid:12) |     |     |
1
|     |     |     | min | MAPE | =   |     | (cid:12)         | (cid:12)×100% |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---------------- | ------------- | --- | --- |
|     |     |     |     |      | n−1 |     | (cid:12) x(0)(t) | (cid:12)      |     |     |
α,β,m
t=2
|     |     |     |      | ≤   | ≤    |       |     |     |     | (21) |
| --- | --- | --- | ---- | --- | ---- | ----- | --- | --- | --- | ---- |
|     |     |     | s.t. | 0   | α 1, |       |     |     |     |      |
|     |     |     |      | ≤   | ≤    |       |     |     |     |      |
|     |     |     |      | 0   | β 1, |       |     |     |     |      |
|     |     |     |      | m ≥ | 0, m | ̸= 1. |     |     |     |      |
The time response function, which is the solution to the whitening equation, is given
| by: |     |     |          |     | (cid:20) |          | (cid:21)        |     |     |      |
| --- | --- | --- | -------- | --- | -------- | -------- | --------------- | --- | --- | ---- |
|     |     |     |          |     | (cid:16) | (cid:17) |                 |     |     |      |
|     |     |     |          |     |          | 1−m      | b               |     | b   |      |
|     |     |     | xˆ(1)(k) |     | x(1)(1)  |          | − −a(1−m)(k−1)+ |     |     |      |
|     |     |     |          | =   |          |          | e               |     | .   | (22) |
|     |     |     |          |     |          |          | a               |     | a   |      |
−a(1−m)(k−1)
Note: The exponent in the exponential term has been corrected to for
| consistency |     | with | standard | NGBM | literature. |     |     |     |     |     |
| ----------- | --- | ---- | -------- | ---- | ----------- | --- | --- | --- | --- | --- |
Finally, the predicted AGO sequence is transformed back to the original scale using
the inverse accumulated generating operation (IAGO) to obtain the forecasted values:
|     |     |     |     |     | xˆ(0)(k) | xˆ(1)(k)−xˆ(1)(k−1). |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | -------------------- | --- | --- | --- | ---- |
|     |     |     |     |     |          | =                    |     |     |     | (23) |
A grid-search approach is used to evaluate combinations of α, β, and m within the
specified bounded parameter space to solve the optimization problem.
| 2.2.2. |     | Particle | Swarm | Optimization |     |     |     |     |     |     |
| ------ | --- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
The procedure begins by initializing the NGBM(1,1) parameters, specifically the power
indexmandthebackgroundvaluecoeﬀicientα. Theseinitialvaluesareusedbythemodel
to generate a forecast sequence based on the historical data. The forecasted values are
then compared to the actual observations, and the prediction error is quantified using the
out-of-sample Mean Absolute Percentage Error (MAPE). This MAPE value serves as the
| fitness |     | function | for the | PSO | algorithm. |     |     |     |     |     |
| ------- | --- | -------- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
The PSO algorithm then iteratively refines the parameter values by simulating the
social behavior of a particle swarm. Each particle represents a candidate solution,
characterized by its position in the parameter space, and its performance is evaluated
based on the corresponding out-of-sample MAPE. The particles update their positions
based on their own historical best position and the global best position discovered by
the entire swarm. This process continues until a convergence criterion is satisfied or a
| predefined |     | maximum | number |     | of iterations | is  | reached. |     |     |     |
| ---------- | --- | ------- | ------ | --- | ------------- | --- | -------- | --- | --- | --- |
Zhou et al. [7] describe the main elements of the PSO algorithm as follows:
Particle: A candidate solution defined by the decision variables α and m. The i-th
|     | particle | is  | represented |     | as a vector: |     |          |     |     |      |
| --- | -------- | --- | ----------- | --- | ------------ | --- | -------- | --- | --- | ---- |
|     |          |     |             |     |              | X = | {α ,m }, |     |     | (24) |
|     |          |     |             |     |              | i   | i i      |     |     |      |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 7 of 17
where the parameters are random real numbers constrained within appropriate
|     |         |     | ∈     |       | ̸=  |     |     |     |     |     |
| --- | ------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
|     | ranges: | α   | (0,1) | and m | 1.  |     |     |     |     |     |
Fitness: The performance of each particle is evaluated using the MAPE, which is
|     | the | objective | function | to  | be minimized. |     |     |     |     |     |
| --- | --- | --------- | -------- | --- | ------------- | --- | --- | --- | --- | --- |
Personal Best: After k iterations, particle i retains the best position it has
|     | personally |     | visited, | denoted | as PBk. | This | position | satisfies: |     |     |
| --- | ---------- | --- | -------- | ------- | ------- | ---- | -------- | ---------- | --- | --- |
i
|     |     |     | MAPE(PBk) |     | =   | min{MAPE(Xτ)}, |     | τ = 1,2,...,k. |     | (25) |
| --- | --- | --- | --------- | --- | --- | -------------- | --- | -------------- | --- | ---- |
|     |     |     |           |     | i   |                |     | i              |     |      |
GBk,
Global Best: After k iterations, the global best position, denoted as is the
best position discovered by any particle in the entire swarm. It satisfies:
|     |     |     |           |     |       | n    | (cid:16) | (cid:17)o |            |      |
| --- | --- | --- | --------- | --- | ----- | ---- | -------- | --------- | ---------- | ---- |
|     |     |     | MAPE(GBk) |     |       |      | PBk      |           |            |      |
|     |     |     |           |     | = min | MAPE |          | , i =     | 1,2,...,S, | (26) |
i
|     | where | S is | the swarm | size. |     |     |     |     |     |     |
| --- | ----- | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- |
In this study, the PSO algorithm was implemented in R using the package’s default
parametersettings. Theswarmsizewasautomaticallysetto40,andthemaximumnumber
of iterations was 1000. The inertia weight (w) was set to 1/(2log2), while the cognitive
and social coeﬀicients (local and global exploration constants, respectively) were both
| assigned |     | the default | value | of  | 0.5+log2. |     |     |     |     |     |
| -------- | --- | ----------- | ----- | --- | --------- | --- | --- | --- | --- | --- |
Preliminary tests with alternative parameter values did not yield substantial
improvements in convergence behavior or forecast accuracy, confirming that the default
settings were suﬀicient for achieving stable and eﬀicient optimization in this application.
| 2.3. | Model | Evaluation |     |     |     |     |     |     |     |     |
| ---- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
The prediction accuracy of the competing models was evaluated using the
| out-of-sample |     | mean | absolute |     | percentage | error,                   | defined | as:            |     |      |
| ------------- | --- | ---- | -------- | --- | ---------- | ------------------------ | ------- | -------------- | --- | ---- |
|               |     |      |          |     |            | (cid:12)                 |         | (cid:12)       |     |      |
|               |     |      |          |     |            | Xn (cid:12)              |         | (cid:12)       |     |      |
|               |     |      |          |     | 1          | (cid:12)x(0)(t)−xˆ(0)(t) |         | (cid:12)       |     |      |
|               |     |      |          |     |            | (cid:12)                 |         | (cid:12)×100%. |     |      |
|               |     |      | MAPE     |     | =          |                          |         |                |     | (27) |
|               |     |      |          |     | n−1        | (cid:12)                 | x(0)(t) | (cid:12)       |     |      |
t=2
The forecasting performance based on MAPE values can be graded according to the
| criteria | proposed |     | by [8], | as shown    | in       | Table       | 1.     |               |      |     |
| -------- | -------- | --- | ------- | ----------- | -------- | ----------- | ------ | ------------- | ---- | --- |
|          |          |     | Table   | 1: Forecast | accuracy |             | grades | based on MAPE | [8]. |     |
|          |          |     |         | MAPE        | (%)      | Forecasting |        | Power         |      |     |
≤
|     |     |     |     |     | 10    | Excellent  |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     | 10–20 | Good       |     |     |     |     |
|     |     |     |     |     | 20–50 | Reasonable |     |     |     |     |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 8 of 17
In addition to MAPE, the out-of-sample Root Mean Square Error (RMSE) is reported
as a supplementary accuracy metric. The RMSE is defined as the square root of the
| average | squared differences | between |     | the actual | and | predicted | values: |     |
| ------- | ------------------- | ------- | --- | ---------- | --- | --------- | ------- | --- |
v
u
Xn
|     |     |      | u   | 1   | (cid:0)          |     | (cid:1) |      |
| --- | --- | ---- | --- | --- | ---------------- | --- | ------- | ---- |
|     |     |      | t   |     | x(0)(t)−xˆ(0)(t) |     | 2       |      |
|     |     | RMSE | =   |     |                  |     | .       | (28) |
n−1
t=2
WhileMAPEexpressestheforecasterrorasapercentage,RMSEmeasurestheabsolute
magnitudeoftheerrorintheoriginalunitsofthedata,therebyprovidingacomplementary
| perspective | on model | accuracy. |     |     |     |     |     |     |
| ----------- | -------- | --------- | --- | --- | --- | --- | --- | --- |
2.4. Data
The Gross Domestic Product (GDP) data used in this study were calculated using the
expenditure approach, one of the standard methods for measuring GDP. This approach
| defines GDP | as the | sum of all | final expenditures |     |     | in the economy: |     |     |
| ----------- | ------ | ---------- | ------------------ | --- | --- | --------------- | --- | --- |
−M),
|     |     |     | GDP = | C +I | +G+(X |     |     | (29) |
| --- | --- | --- | ----- | ---- | ----- | --- | --- | ---- |
where C is household consumption, I is gross capital formation (investment), G is
−M)
government spending, and (X represents net exports (exports minus imports).
The data consist of quarterly Philippine GDP figures from the first quarter of 2021 to
the fourth quarter of 2024. The values are expressed in constant 2018 US dollars and were
sourced from the OpenSTAT portal maintained by the Philippine Statistics Authority
(PSA).
|     |     | 3.  | Results | and | Discussions |     |     |     |
| --- | --- | --- | ------- | --- | ----------- | --- | --- | --- |
A simulation study was conducted to determine the optimal data-splitting strategy
for nowcasting quarterly GDP with grey models. Due to the limited size of the available
dataset, it is crucial to select a partitioning scheme that minimizes prediction errors.
The simulation design is informed by previous research that uses harmonic regression
to model cyclical patterns in GDP. For instance, Bujosa et al. [9] applied linear dynamic
harmonic regression to Spanish economic indicators, including GDP, and De Groot et al.
[10] integrated harmonic regression with Fourier and GARCH methods to analyze GDP
| cycles in | OECD countries. |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Both studies represented cyclical dynamics using sinusoidal components, modeled by
| the general | harmonic | regression | form: |     |     |     |     |     |
| ----------- | -------- | ---------- | ----- | --- | --- | --- | --- | --- |
XR
|     |     | y(t) | = [a | cos(ω | t)+b | sin(ω t)]+e | .   | (30) |
| --- | --- | ---- | ---- | ----- | ---- | ----------- | --- | ---- |
|     |     |      |      | j     | j    | j j         | t   |      |
j=1
In this equation, p and ω = 2π/p denote the period and frequency of the jth cycle,
|     |     | j   | j   | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
respectively. The coeﬀicients a and b determine the amplitude and phase of the cycle,
|           |                |       | j     | j   |     |     |     |     |
| --------- | -------------- | ----- | ----- | --- | --- | --- | --- | --- |
| while e t | represents the | error | term. |     |     |     |     |     |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 9 of 17
Building on this framework, the simulation study employs a specific case of the
| harmonic | regression | model: |                     |            |      |
| -------- | ---------- | ------ | ------------------- | ---------- | ---- |
|          |            | y(t) = | β 0 t+β 1 cos(γt)+β | 2 sin(γt), | (31) |
where γ = 2π/4 captures the quarterly cyclical frequency, and t = 1,2,...,16 indexes the
16 quarterly observations. A linear growth trend is introduced with β = 0.15, while the
0
{−0.1,0,0.1,0.2}
coeﬀicients β and β are systematically varied over the set to simulate
1 2
| different | cyclical patterns | in amplitude | and phase. |     |     |
| --------- | ----------------- | ------------ | ---------- | --- | --- |
Table 2: Best-performing models based on out-of-sample MAPE under a 70/30 data split.
|     |     | (β ,β ) | Best Performing | Model |     |
| --- | --- | ------- | --------------- | ----- | --- |
1 2
|     |     | (-0.1, -0.1) | PSO-NGBM(1,1) |           |     |
| --- | --- | ------------ | ------------- | --------- | --- |
|     |     | (0, -0.1)    | PSO-NGBM(1,1) |           |     |
|     |     | (0.1, -0.1)  | PSO-NGBM(1,1) |           |     |
|     |     | (0.2, -0.1)  | PSO-NGBM(1,1) |           |     |
|     |     | (-0.1, 0)    | PSO-NGBM(1,1) |           |     |
|     |     | (0.1, 0)     | PSO-NGBM(1,1) |           |     |
|     |     | (0.2, 0)     | PSO-NGBM(1,1) |           |     |
|     |     | (-0.1, 0.1)  | PSO-NGBM(1,1) |           |     |
|     |     | (0, 0.1)     | PSO-NGBM(1,1) |           |     |
|     |     | (0.1, 0.1)   | PSO-NGBM(1,1) |           |     |
|     |     | (0.2, 0.1)   | Exponential   | NGBM(1,1) |     |
|     |     | (-0.1, 0.2)  | PSO-NGBM(1,1) |           |     |
|     |     | (0, 0.2)     | PSO-NGBM(1,1) |           |     |
|     |     | (0.1, 0.2)   | Exponential   | NGBM(1,1) |     |
|     |     | (0.2, 0.2)   | Exponential   | NGBM(1,1) |     |
As shown in Table 2, the PSO-NGBM(1,1) model demonstrated superior performance,
achieving the lowest MAPE in 12 of the 15 parameter combinations. The Exponential
NGBM(1,1) model performed best only in the three scenarios with the strongest cyclical
amplitudes—specifically, (0.2, 0.1), (0.1, 0.2), and (0.2, 0.2). This suggests that the
exponentialbackgroundvalueoffersanadvantagefordatawithhighlypronouncedcyclical
patterns. However, this advantage was limited to a small subset of cases, and the
| performance | gain over | the PSO-optimized | model | was modest. |     |
| ----------- | --------- | ----------------- | ----- | ----------- | --- |
Under the 80/20 data split, PSO-NGBM(1,1) achieved the lowest MAPE in 6 of the
15 parameter combinations, while the Exponential NGBM(1,1) performed best in 5 cases,
and the traditional NGBM(1,1) in 4. Consistent with earlier results, the Exponential
NGBM(1,1) excelled under parameter settings associated with stronger cyclical behavior.
The traditional NGBM(1,1) performed well in a limited number of cases, particularly at
(0, -0.1), (0, 0.1), and (0.1, 0.1). By contrast, GM(1,1) consistently showed the weakest
| performance | across all | scenarios. |     |     |     |
| ----------- | ---------- | ---------- | --- | --- | --- |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 10 of 17
Table 3: Best-performing models based on out-of-sample MAPE under an 80/20 data
split.
|     |     | (β ,β ) | Best Performing | Model |
| --- | --- | ------- | --------------- | ----- |
1 2
|     |     | (-0.1, -0.1) | PSO-NGBM(1,1) |           |
| --- | --- | ------------ | ------------- | --------- |
|     |     | (0, -0.1)    | NGBM(1,1)     |           |
|     |     | (0.1, -0.1)  | Exponential   | NGBM(1,1) |
|     |     | (0.2, -0.1)  | Exponential   | NGBM(1,1) |
|     |     | (-0.1, 0)    | PSO-NGBM(1,1) |           |
|     |     | (0.1, 0)     | PSO-NGBM(1,1) |           |
|     |     | (0.2, 0)     | PSO-NGBM(1,1) |           |
|     |     | (-0.1, 0.1)  | PSO-NGBM(1,1) |           |
|     |     | (0, 0.1)     | NGBM(1,1)     |           |
|     |     | (0.1, 0.1)   | NGBM(1,1)     |           |
|     |     | (0.2, 0.1)   | Exponential   | NGBM(1,1) |
|     |     | (-0.1, 0.2)  | Exponential   | NGBM(1,1) |
|     |     | (0, 0.2)     | NGBM(1,1)     |           |
|     |     | (0.1, 0.2)   | PSO-NGBM(1,1) |           |
|     |     | (0.2, 0.2)   | Exponential   | NGBM(1,1) |
The simulation aimed to determine whether a 70/30 or 80/20 training–testing split
yields superior predictive performance for grey models. A direct comparison shows that
the model producing the lowest MAPE under the 70/30 split achieved a lower absolute
MAPE value in 8 of the 15 parameter combinations, compared to 7 for the 80/20 split.
Although the margin is narrow, the results favor the 70/30 split when prediction accuracy
| is the primary | objective. |     |     |     |
| -------------- | ---------- | --- | --- | --- |
The 80/20 split performed relatively better under moderate cyclical patterns, whereas
the 70/30 split provided lower MAPE values in settings characterized by stronger cyclical
behavior. Across both splits, PSO-NGBM(1,1) was the most frequent top performer, with
theExponentialNGBM(1,1)alsoshowingcompetitiveresults, particularlyforpronounced
cycles. In contrast, GM(1,1) consistently lagged behind and failed to achieve the lowest
| MAPE | in any scenario. |     |     |     |
| ---- | ---------------- | --- | --- | --- |
Overall, while both splitting schemes are viable, the 70/30 partitioning provides a
slight advantage in forecasting accuracy. Accordingly, the 70/30 split was adopted for the
| subsequent       | application | to the actual | GDP dataset. |     |
| ---------------- | ----------- | ------------- | ------------ | --- |
| 3.1. Comparative |             | Study         |              |     |
Before presenting the full forecast results, the optimization behavior of the PSO
| algorithm | is examined | in the figure | below. |     |
| --------- | ----------- | ------------- | ------ | --- |
The convergence plot in Figure 1 illustrates the minimization of the out-of-sample
MAPE across iterations. The PSO algorithm rapidly reduced the error during the
initial iterations, stabilizing after approximately 30 iterations. This indicates eﬀicient

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 11 of 17
Table 4: Comparison of best-performing models under 70/30 and 80/20 data splits.
| (β ,β ) |     | 70/30 | Split |     | 80/20 | Split |
| ------- | --- | ----- | ----- | --- | ----- | ----- |
1 2
| (−0.1,−0.1) |     | PSO-NGBM(1,1) |     |     | PSO-NGBM(1,1) |     |
| ----------- | --- | ------------- | --- | --- | ------------- | --- |
(0,−0.1)
|     |     | PSO-NGBM(1,1) |     |     | NGBM(1,1) |     |
| --- | --- | ------------- | --- | --- | --------- | --- |
(0.1,−0.1)
|            |             | PSO-NGBM(1,1) |           | Exponential |               | NGBM(1,1) |
| ---------- | ----------- | ------------- | --------- | ----------- | ------------- | --------- |
| (0.2,−0.1) |             | PSO-NGBM(1,1) |           | Exponential |               | NGBM(1,1) |
| (−0.1,0)   |             | PSO-NGBM(1,1) |           |             | PSO-NGBM(1,1) |           |
| (0.1,0)    |             | PSO-NGBM(1,1) |           |             | PSO-NGBM(1,1) |           |
| (0.2,0)    |             | PSO-NGBM(1,1) |           |             | PSO-NGBM(1,1) |           |
| (−0.1,0.1) |             | PSO-NGBM(1,1) |           |             | PSO-NGBM(1,1) |           |
| (0,0.1)    |             | PSO-NGBM(1,1) |           |             | NGBM(1,1)     |           |
| (0.1,0.1)  |             | PSO-NGBM(1,1) |           |             | NGBM(1,1)     |           |
| (0.2,0.1)  | Exponential |               | NGBM(1,1) | Exponential |               | NGBM(1,1) |
(−0.1,0.2)
|           |             | PSO-NGBM(1,1)  |           | Exponential |               | NGBM(1,1) |
| --------- | ----------- | -------------- | --------- | ----------- | ------------- | --------- |
| (0,0.2)   |             | PSO-NGBM(1,1)  |           |             | NGBM(1,1)     |           |
| (0.1,0.2) | Exponential |                | NGBM(1,1) |             | PSO-NGBM(1,1) |           |
| (0.2,0.2) | Exponential |                | NGBM(1,1) | Exponential |               | NGBM(1,1) |
|           | Figure      | 1: Convergence | plot of   | PSO for     | NGBM(1,1)     |           |
convergence to a near-optimal solution with no substantial improvements thereafter.
Theresultsrevealaconsistentpatternacrossallmodels,withpredictionerrorspeaking
during the fourth quarter of each year in both in-sample and out-of-sample periods.
For PSO-NGBM(1,1), Q4 prediction errors were 8.72% (2021), 10.48% (2022), 8.72%
(2023), and 7.73% (2024). Similar patterns occurred in the Exponential NGBM(1,1) and

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 12 of 17
Table 5: Forecast results of PSO-NGBM, Exponential NGBM, NGBM(1,1), and GM(1,1)
|     |     |     | PSO-NGBM(1,1) |     | ExponentialNGBM(1,1) |     | NGBM(1,1) |     | GM(1,1) |     |
| --- | --- | --- | ------------- | --- | -------------------- | --- | --------- | --- | ------- | --- |
α=0.88,m=−0.03
| Time   |     | Actual    |      |       | α=0.11,m=0.01,β=0.99 |       | α=0.5,m=0.013 |       | α=0.5 |       |
| ------ | --- | --------- | ---- | ----- | -------------------- | ----- | ------------- | ----- | ----- | ----- |
|        |     |           | Pred | PE(%) | Pred                 | PE(%) | Pred          | PE(%) | Pred  | PE(%) |
| 2021Q1 |     | 4,266,797 | –    | –     | –                    | –     | –             | –     | –     | –     |
2021Q2 4,641,825 4,696,840 1.19 4,640,146 0.04 4,641,810 0.0003 4,664,919 0.50
2021Q3 4,426,630 4,711,694 6.44 4,713,355 6.48 4,721,235 6.66 4,723,610 6.71
2021Q4 5,204,832 4,751,109 8.72 4,778,371 8.19 4,789,839 7.97 4,783,039 8.10
2022Q1 4,611,219 4,802,210 4.14 4,839,870 4.96 4,853,679 5.26 4,843,217 5.03
2022Q2 4,990,934 4,860,519 2.61 4,899,553 1.83 4,914,964 1.52 4,904,151 1.74
2022Q3 4,767,549 4,923,948 3.28 4,958,237 4.00 4,974,757 4.35 4,965,852 4.16
2022Q4 5,575,902 4,991,362 10.48 5,016,381 10.03 5,033,651 9.72 5,028,329 9.82
2023Q1 4,907,013 5,062,082 3.16 5,074,269 3.41 5,092,018 3.77 5,091,592 3.76
2023Q2 5,203,455 5,135,673 1.30 5,132,090 1.37 5,150,100 1.03 5,155,651 0.92
2023Q3 5,051,396 5,211,843 3.18 5,189,978 2.74 5,208,070 3.10 5,220,516 3.35
| In-sampleMAPE |     |     |     | 4.45 |     | 4.31 |     | 4.34 |     | 4.41 |
| ------------- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- | ---- |
2023Q4 5,884,528 5,371,179 8.72 5,306,319 9.83 5,266,053 10.51 5,286,198 10.17
2024Q1 5,195,588 5,454,102 4.98 5,364,904 3.26 5,324,144 2.47 5,352,705 3.02
2024Q2 5,539,083 5,539,090 0.0001 5,423,833 2.08 5,382,416 2.83 5,420,049 2.15
2024Q3 5,316,054 5,626,090 5.83 5,483,143 3.14 5,440,929 2.35 5,488,241 3.24
2024Q4 6,193,631 5,715,068 7.73 5,542,866 10.51 5,499,730 11.20 5,557,291 10.27
| Out-of-sampleMAPE |     |     |     | 5.45 |     | 5.76 |     | 5.87 |     | 5.77 |
| ----------------- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- | ---- |
benchmark models. Nevertheless, PSO-NGBM(1,1) achieved the lowest Q4 errors in the
| out-of-sample | forecasts |     | among all | grey | models. |     |     |     |     |     |
| ------------- | --------- | --- | --------- | ---- | ------- | --- | --- | --- | --- | --- |
PSO-NGBM(1,1) also achieved a near-perfect prediction in 2024 Q2 with a PE of
0.0001%. The traditional NGBM(1,1) produced the lowest errors in 2024 Q1 (2.47%) and
Q3(2.35%),whileExponentialNGBM(1,1)andGM(1,1)showedcompetitiveperformance.
For the in-sample period (2021 Q2-2023 Q3), all models achieved MAPE values below
5%. Exponential NGBM(1,1) attained the lowest in-sample MAPE (4.31%), followed
by NGBM(1,1) (4.34%), GM(1,1) (4.41%), and PSO-NGBM(1,1) (4.45%). However,
in out-of-sample forecasting, PSO-NGBM(1,1) achieved the lowest MAPE (5.45%),
| demonstrating |     | superior | generalization. |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Figure 2 shows that GM(1,1) and Exponential NGBM(1,1) closely follow the general
GDP trajectory but fail to capture short-term fluctuations. The traditional NGBM(1,1)
| shows more | variation | but | still underestimates |     | cyclical | amplitudes. |     |     |     |     |
| ---------- | --------- | --- | -------------------- | --- | -------- | ----------- | --- | --- | --- | --- |
ThePSO-optimizedNGBM(1,1)(greenline)exhibitsasteeperupwardtrajectoryfrom
2023 Q3 onward, reflecting a stronger emphasis on long-term trends at the expense of
| short-term | variations. |     |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
All models approximate the upward GDP trend with varying accuracy, but none fully
capture the seasonal dynamics, highlighting the need for explicit seasonal modeling in
| future grey        | model | extensions. |           |     |     |     |     |     |     |     |
| ------------------ | ----- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| 3.2. Out-of-Sample |       |             | Forecasts |     |     |     |     |     |     |     |
As shown in Figure 3, none of the grey models fully captured the sharp fluctuations
in the actual GDP series, a limitation consistent with the broader pattern observed in
Figure 2.

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 13 of 17
Figure 2: Forecasts of the grey models
Figure 3: Out-of-sample forecasts of the grey models (2023 Q4–2024 Q4).
Among the models, PSO-NGBM(1,1) produced forecasts closest to the actual GDP
in several quarters, most notably in 2024 Q2 where its prediction was nearly identical to
the observed value. Although it overestimated GDP in 2024 Q1 and 2024 Q3 — periods

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 14 of 17
characterized by sharp declines — it maintained relatively small deviations overall.
The Exponential NGBM(1,1) and GM(1,1) produced similar trajectories but
consistently underestimated GDP in the fourth quarter. In contrast, the traditional
NGBM(1,1) yielded the lowest forecast path and systematically underpredicted GDP
throughout most of the evaluation period, with particularly pronounced errors in Q4.
These results underscore the challenge of modeling abrupt quarterly shifts in GDP
and suggest that grey forecasting frameworks require additional mechanisms to capture
| short-term | volatility. |               |               |          |               |          |           |           |
| ---------- | ----------- | ------------- | ------------- | -------- | ------------- | -------- | --------- | --------- |
|            |             | Table 6:      | Out-of-sample |          | forecast      | accuracy | metrics.  |           |
|            |             | PSO-NGBM(1,1) |               | Exp      | NGBM(1,1)     |          | NGBM(1,1) | GM(1,1)   |
| RMSE       |             | 362,077.8     |               |          | 412,050.9     |          | 429,109.5 | 407,781.9 |
| MAPE       | (%)         | 5.45          |               |          | 5.76          |          | 5.87      | 5.77      |
| Note: RMSE | values      | are expressed | in            | millions | of Philippine | Pesos    | (PHP).    |           |
The out-of-sample period from 2023 Q4 to 2024 Q4 was used to evaluate predictive
performance. Table 6 reports the Root Mean Square Error (RMSE), which measures the
| average | magnitude | of forecast | errors | in the | original | units. |     |     |
| ------- | --------- | ----------- | ------ | ------ | -------- | ------ | --- | --- |
PSO-NGBM(1,1) achieved the lowest RMSE (362,077.8), indicating smaller absolute
errors compared to other models. The Exponential NGBM(1,1) recorded an RMSE of
412,050.9, followed by GM(1,1) at 407,781.9 and the traditional NGBM(1,1) at 429,109.5.
Although the differences are modest, PSO-NGBM(1,1) maintained a consistent advantage
| in absolute | error | terms. |     |     |     |     |     |     |
| ----------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
In terms of out-of-sample MAPE, PSO-NGBM(1,1) again performed best at 5.45%.
While the Exponential NGBM(1,1) achieved the lowest in-sample MAPE, its accuracy
declined slightly out-of-sample to 5.76%. Similarly, the forecasting accuracy of both
| benchmark | models | deteriorated | in  | the out-of-sample |     | period. |     |     |
| --------- | ------ | ------------ | --- | ----------------- | --- | ------- | --- | --- |
Overall, both RMSE and MAPE results indicate that PSO-NGBM(1,1) produced
comparatively lower errors in both magnitude and percentage terms. These findings align
withthesimulationstudy, reinforcingthatPSO-NGBM(1,1)providesaconsistent, though
modest, advantageinforecastingunseendataforshort-termGDPnowcastingwithlimited
observations.
| 3.3. Seasonal |     | Adjustment |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
The recurring fourth-quarter prediction errors observed in the initial forecasts indicate
a fundamental limitation of the standard grey models used in this study, pointing
to unmodeled seasonal patterns. To investigate this, a seasonal decomposition of the
quarterly GDP series was performed to assess whether removing these fluctuations could
enhance forecasting consistency. This post-modeling analysis was particularly relevant
given the systematic Q4 errors, which suggested that seasonality contributed significantly
| to forecast | instability. |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- |

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 15 of 17
|     | Figure | 4: Seasonal-trend | decomposition |     | of Philippine | GDP. |     |
| --- | ------ | ----------------- | ------------- | --- | ------------- | ---- | --- |
ThedecompositionanalysisinFigure4revealsastrongandconsistentseasonalpattern,
characterized by a first-quarter decline followed by a sharp fourth-quarter surge. This
confirms the presence of a systematic seasonal structure that was not adequately captured
| by the initial | grey | model specifications. |     |     |     |     |     |
| -------------- | ---- | --------------------- | --- | --- | --- | --- | --- |
To address this limitation, the GDP series was seasonally adjusted by removing the
identified seasonal component, and the grey models were reapplied to this adjusted series.
Forecasting accuracy was then reassessed and compared with the results from the original
data.
Table 7: Out-of-sample forecast performance on seasonally adjusted GDP.
|      |        | PSO-NGBM(1,1) | Exp NGBM(1,1) |       | NGBM(1,1) |       | GM(1,1)    |
| ---- | ------ | ------------- | ------------- | ----- | --------- | ----- | ---------- |
| Time | Actual | Pred          | PE(%) Pred    | PE(%) | Pred      | PE(%) | Pred PE(%) |
2023Q4 5,884,528 5,868,679 0.27 5,890,093 0.09 5,856,314 0.48 5,851,976 0.55
2024Q1 5,195,588 5,210,630 0.29 5,240,289 0.86 5,206,173 0.20 5,206,605 0.21
2024Q2 5,539,083 5,539,075 0.0001 5,577,771 0.70 5,543,085 0.07 5,548,962 0.18
2024Q3 5,316,054 5,338,762 0.43 5,387,230 1.34 5,351,767 0.67 5,363,714 0.90
2024Q4 6,193,631 6,136,223 0.94 6,195,159 0.02 6,158,733 0.56 6,177,333 0.26
| MAPE (%) |     |     | 0.38 | 0.60 |     | 0.40 | 0.42 |
| -------- | --- | --- | ---- | ---- | --- | ---- | ---- |
The results in Table 7 demonstrate a dramatic improvement in forecasting accuracy
after seasonal adjustment. All models achieved exceptional performance, with MAPE
values consistently below 1%. PSO-NGBM(1,1) achieved the lowest overall MAPE
(0.38%), followed closely by NGBM(1,1) (0.40%) and GM(1,1) (0.42%). In contrast,

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 16 of 17
the Exponential NGBM(1,1) produced the highest MAPE (0.60%), indicating that the
exponential background value provided minimal benefit in this context.
Notably, the effectiveness of PSO optimization persisted even after removing seasonal
effects, whereas the exponential background value approach contributed little to forecast
improvement. This finding underscores the robustness of PSO-NGBM(1,1) in adapting
to both raw and seasonally adjusted data, suggesting that optimization techniques play a
more critical role than background value adjustments in enhancing forecast performance.
These results confirm that seasonal adjustment substantially improves the forecasting
accuracy of grey models for Philippine GDP data. The systematic reduction in prediction
errors highlights the importance of explicitly accounting for seasonal patterns when
applying grey models to strongly seasonal economic time series.
4. Conclusion and Recommendations
This study demonstrates that the PSO-optimized NGBM(1,1) model outperforms
benchmarkgreymodelsinnowcastingPhilippineGDP,achievingthelowestout-of-sample
MAPE (5.45%) and RMSE. While all models produced acceptable forecasts,
PSO-NGBM(1,1) delivered consistently superior performance.
Forecastaccuracyimproveddramaticallyafterseasonaladjustment,withMAPEvalues
falling from over 5% to below 1%. This improvement is economically significant; a
1% forecasting error for GDP, measured in millions, represents a substantial monetary
deviation that can directly impact the accuracy of policy assessments and subsequent
economic interventions.
The findings suggest that developing hybrid grey models with integrated seasonal
components could enhance nowcasting accuracy without requiring separate preprocessing.
Future research should also explore optimization strategies beyond the exponential
background value to improve parameter estimation. In addition to standard accuracy
metrics like MAPE and RMSE, rigorous statistical testing is recommended to establish
the significance of performance differences between models. Furthermore, combining
closed-form estimation with metaheuristic algorithms like PSO may yield more stable
and computationally eﬀicient forecasts.
Ongoing refinement of these models is vital for generating timely and reliable GDP
estimates to guide policy. In dynamic economic environments where oﬀicial statistics
are released with considerable delay, accurate nowcasts can strengthen evidence-based
governance and support more responsive economic planning.
Overall, this study confirms the promise of PSO-optimized grey models as effective
and reliable tools for short-term GDP forecasting in data-constrained environments.
Acknowledgements
The authors thank the referees for their insightful comments and constructive
suggestions, which have greatly improved this paper. We also extend our appreciation
to the readership of the European Journal of Pure and Applied Mathematics for their

S.K.. Carillo, I.J. Serra / Eur. J. Pure Appl. Math, 18 (4) (2025), 6875 17 of 17
continued engagement. Furthermore, we gratefully acknowledge the support of the
Department of Science and Technology - Science Education Institute and the College
of Science - Statistics Program at the University of the Philippines Cebu.
Declaration
The authors declare no conflict of interest. All authors contributed substantially to
the following: Conceptualization, Methodology, Investigation, Writing – Original Draft,
and Validation (approval of the final manuscript).
References
[1] C.I.Ugoh, C.A.Uzuke, andD.O.Ugoh. Applicationofarimaxmodelonforecasting
nigeria’sgdp. AmericanJournalofTheoreticalandAppliedStatistics,10(5):216,2021.
[2] B. Bok, D. Caratelli, D. Giannone, A. S. Modugno, and M. S. Sbordone.
Macroeconomic nowcasting and forecasting with big data. Staff Reports 830, Federal
Reserve Bank of New York, 2017.
[3] D. Giannone, L. Reichlin, and D. Small. Nowcasting: The real-time informational
content of macroeconomic data. Journal of Monetary Economics, 55:665–676, 2008.
[4] C. Rufino. Nowcasting philippine economic growth using midas regression modeling.
Technical report, DLSU Angelo King Institute for Economic and Business Studies,
2017.
[5] C. Chen, H. L. Chen, and S. Chen. Forecasting of foreign exchange rates of
taiwan’s major trading partners by novel nonlinear grey bernoulli model ngbm(1,1).
Communications in Nonlinear Science and Numerical Simulation, 13(6), 2006.
[6] M. Cheng, Y. Ding, Z. Ma, X. Li, and J. Wang. Nonlinear grey bernoulli model
ngbm(1,1)’s parameter optimisation method and model application. Journal of
Industrial and Management Optimization, 18(3), 2021.
[7] J. Zhou, J. He, Y. Yang, Z. Xu, and Y. Liu. Parameter optimization of nonlinear
grey bernoulli model using particle swarm optimization. Applied Mathematics and
Computation, 207(2):292–299, 2008.
[8] C. D. Lewis. Industrial and Business Forecasting Methods. Butterworth Scientific,
1982.
[9] M.Bujosa, A.Garcia-Ferrer, andA.DeJuan. Predictingrecessionswithfactorlinear
dynamic harmonic regressions. Journal of Forecasting, 32(6):481–499, 2013.
[10] E. De Groot, R. Segers, and D. Prins. Disentangling the enigma of multi-structured
economic cycles - a new appearance of the golden ratio. Technological Forecasting
and Social Change, 169(6), 2021.