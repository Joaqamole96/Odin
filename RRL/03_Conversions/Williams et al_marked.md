Received8August2023,accepted2September2023,dateofpublication20September2023,dateofcurrentversion4October2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3317791
Anomaly Detection in Multi-Seasonal
Time Series Data
ASHTONT.WILLIAMS,RYANE.SPERL,ANDSOONM.CHUNG ,(LifeMember,IEEE)
DepartmentofComputerScienceandEngineering,WrightStateUniversity,Dayton,OH45435,USA
Correspondingauthor:SoonM.Chung(soon.chung@wright.edu)
ThisworkwassupportedinpartbytheAirForceResearchLaboratory(AFRL)/DefenseAssociatedGraduateStudentInnovators(DAGSI)
ResearchFellowship.
ABSTRACT Most of today’s time series data contain anomalies and multiple seasonalities, and accurate
anomaly detection in these data is critical to almost any type of business. However, most mainstream
forecastingmodelsusedforanomalydetectioncanonlyincorporateoneornoseasonalcomponentintotheir
forecastsandcannotcaptureeveryknownseasonalpatternintimeseriesdata.Inthispaper,weproposeanew
multi-seasonalforecastingmodelforanomalydetectionintimeseriesdatathatextendsthepopularSeasonal
AutoregressiveIntegratedMovingAverage(SARIMA)model.Ourmodel,namedmulti-SARIMA,utilizes
a time series dataset’s multiple pre-determined seasonal trends to increase anomaly detection accuracy
even more than the original SARIMA model. Our experimental results demonstrate the higher accuracy
of multi-SARIMA when multiple seasonalities are present than most models with one or no seasonal
component,althoughwithmoreprocessingtime.
INDEX TERMS Anomalydetection,movingaverage,multipleseasonalities,multi-SARIMA,timeseries
data,SARIMA.
I. INTRODUCTION Some time series data contain a seasonality, which is a
Nowadays there are many data sources, such as sensors, pattern that repeats at specific time intervals [1]. For exam-
producing time series data, which is a sequence of data ple, CPU usage rate of a server may have a daily seasonal
points indexed in time order. These data points typically trend.ThepopularSeasonalAutoregressiveIntegratedMov-
consist of successive measurements made from the same ingAverage(SARIMA)forecastingmodel[18]canrepresent
sourceoverafixedtimeintervalandareusedtotrackchange a seasonal trend in its forecasting of time series data. How-
overtime[16].Anomalies(i.e.,outliers)aredatapointsthat ever, SARIMA can implement only one seasonal trend in
significantlydeviatefromtheirexpectedvalue[4],andearly its forecasting [1]. Allowing only one seasonal trend is a
detectionofanomaliesisimportanttomitigatetheseharmful majorlimitationbecausesometimeseriesdatacontainmore
effects, particularly in critical systems where failure can be thanoneseasonality[7].Forexample,NewYorkCity(NYC)
catastrophic[3].Forexample,ahospitalcandetectabnormal taxi traffic data has both daily and weekly seasonal trends.
bodysignalsofitspatientsandnotifyprofessionalsbeforeit’s Thus,utilizingallknownseasonaleffectsintimeseriesdata
toolate. can play an important role in data forecasting and anomaly
Foranomalydetectionintimeseriesdata,forecastingmod- detection[1].
elsareusedtocompareforecastedvaluestoactualvaluesto In this paper, we propose a new multi-seasonal model,
determine if a point is anomalous. While some deviation is namedmulti-SARIMA,foranomalydetectionintimeseries
expectedwhencomparingaforecastedvaluetoitsrealcoun- data that extends the SARIMA model by allowing mul-
terpart,ifthepredictedvaluedeviatessignificantlyfromthe tiple seasonal components. The multi-SARIMA utilizes a
actualvalue,thenthedatapointismostlikelyananomaly[2]. dataset’smultiplepre-determinedseasonaltrendstoincrease
anomaly detection accuracy. To compare with our multi-
SARIMA, we also implemented other anomaly detection
The associate editor coordinating the review of this manuscript and models, including Moving Average (MA), Seasonal Inte-
approvingitforpublicationwasChao-YangChen . grated Moving Average (SIMA), the original SARIMA,
2023TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
106456 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
Numenta’sHierarchicalTemporalMemory(HTM)[9],[10], B. MOVINGAVERAGE(MA)
| and another |     | multi-seasonal | model | TBATS |     | which stands | for |             |      |            |     |          |     |              |     |
| ----------- | --- | -------------- | ----- | ----- | --- | ------------ | --- | ----------- | ---- | ---------- | --- | -------- | --- | ------------ | --- |
|             |     |                |       |       |     |              |     | Time series | data | is usually |     | produced | by  | a monitoring |     |
Trigonometricseasonality,Box-Coxtransformation,ARMA device and can range from spatial data in medical imag-
errors, Trend and Seasonal components [8]. Additionally, ing to sequential data in network security [2], [12]. Let
|     |     |     |     |     |     |     |     | ,X  | ,...,X |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
weimplementedthetwo-stepapproachproposedin[2]with X = {X }beaone-dimensionaltimeserieswith
|     |     |     |     |     |     |     |     | 1   | 2   | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ourmulti-SARIMAasthesecondstep.Themulti-SARIMA evenly spaced discrete time where X is a value X at time t
t
| produced | better | anomaly | detection | results |     | than the | original |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --------- | ------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[2],[12].Valuesthatarebeforetareconsidereditslags,such
SARIMA for every dataset we tested and, in most cases, thatX t−i isthevalueistepsbackinthetimeseries[2],[12].
outperformedHTMandTBATS. ThebackshiftoperatorByieldsthelagsinatimeseriesand
| Thispaperisorganizedasfollows:SectionIIdefinesour |     |     |     |     |     |     |     | isdefinedas: |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
anomalylabelingmethodandexplainstheexistinganomaly
detectionmodelsusedinthispaper.SectionIIIexplainsour BiX =X t−i (3)
t
| proposed    | multi-SARIMA |        | model    | and          | the two-step | approach |        |                     |     |     |     |     |     |     |     |
| ----------- | ------------ | ------ | -------- | ------------ | ------------ | -------- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- |
|             |              |        |          |              |              |          |        | forallt >i[2],[12]. |     |     |     |     |     |     |     |
| we proposed |              | in [2] | with our | multi-SARIMA |              | model    | as the |                     |     |     |     |     |     |     |     |
Themovingaverage(MA)modelisasimpleandcommon
secondstep.SectionIVdescribesthedatasetsusedfortesting
approachtoforecastingtimeseriesdata.Themovingaverage
andtheirproperties,theMultipleSeasonal-Trenddecomposi-
|     |     |     |     |     |     |     |     | oforderq,denotedasMA(q),predictsthevalueX |     |     |     |     |     |     | attimet |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
tionusingLocallyEstimatedScatterplotSmoothing(Loess)
as:
| (MSTL) | decomposition |          | [7] | we used          | to verify | the seasonal |        |     |     |     |     |     |     |     |     |
| ------ | ------------- | -------- | --- | ---------------- | --------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| trends | in each       | dataset, | and | the differencing |           | used         | on our |     |     |     |     | q   |     |     |     |
X
|     |     |     |     |     |     |     |     |     |     | X =µ+ε | +   | b   | Biε |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
datasets.SectionVdescribestheimplementationofdifferent t t i t
models, single-step and two-step test results, and compar- i=1
isonsbasedonthedetectionaccuracyandruntime.SectionVI
|     |     |     |     |     |     |     |     | for all t > | q, where | ε   | is the | white noise | error | at  | time t, µ |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------ | ----------- | ----- | --- | --------- |
t
contains our final thoughts with a conclusion and possible is the mean of the series, and b = (cid:8) b ,b ,...,b (cid:9) is the q
|     |     |     |     |     |     |     |     |     |     |     |     |     | 1 2 | q   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
futureresearchtopics.
parametersforthemodel[2],[12].
II. ANOMALYLABELINGANDEXISTINGDETECTION
|     |     |     |     |     |     |     |     | C. SEASONALINTEGRATEDMOVINGAVERAGE(SIMA) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
METHODS
|     |     |     |     |     |     |     |     | The seasonal | integrated |     | moving | average | (SIMA) |     | model is |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------ | ------- | ------ | --- | -------- |
A. ANOMALYLABELING
|      |        |         |           |        |     |              |     | an extension | of         | the MA | model | where          | one | seasonal | com-    |
| ---- | ------ | ------- | --------- | ------ | --- | ------------ | --- | ------------ | ---------- | ------ | ----- | -------------- | --- | -------- | ------- |
| Time | series | anomaly | detection | models | use | a calculated |     |              |            |        |       |                |     |          |         |
|      |        |         |           |        |     |              |     | ponent is    | considered | for    | the   | data forecast. |     | SIMA     | denoted |
numericmetriccalledananomalyscoretodetermineifadata as SIMA(d,q) , forecasts using MA(q) with a seasonally
m
| point       | is an | anomaly | or not    | [4]. In our | case,   | we determine  |     |             |      |         |              |     |         |     |           |
| ----------- | ----- | ------- | --------- | ----------- | ------- | ------------- | --- | ----------- | ---- | ------- | ------------ | --- | ------- | --- | --------- |
|             |       |         |           |             |         |               |     | differenced | time | series. | Differencing |     | is used | to  | eliminate |
| the anomaly |       | score   | using the | error       | between | the predicted |     |             |      |         |              |     |         |     |           |
trendsthatareapparentinadatasettomakethedatastationary
valueandtheactualvalue.Iftheanomalyscoreexceedsthe
|     |     |     |     |     |     |     |     | [2]. Differencing |     | is done | by replacing |     | every | value | with the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ------------ | --- | ----- | ----- | -------- |
threshold,thedatapointislabeledasananomaly[10].
|     |      |            |           |           |          |     |         | difference   | between                                   | itself | and | its first | lag | [2]. Let | ∇X = |
| --- | ---- | ---------- | --------- | --------- | -------- | --- | ------- | ------------ | ----------------------------------------- | ------ | --- | --------- | --- | -------- | ---- |
| In  | some | cases, the | threshold | is fixed, | however, |     | a fixed |              |                                           |        |     |           |     |          |      |
|     |      |            |           |           |          |     |         | {X ,X ,...,X | }beafirst-orderdifferencedtimeseries,such |        |     |           |     |          |      |
|     |      |            |           |           |          |     |         | 1 2          | t                                         |        |     |           |     |          |      |
thresholdisnotsuitableinourcasebecausethevariancecan
that
changeovertime.Thedynamicthresholdmustbecalculated
using sample metrics since we cannot assume the detector ∇X =X −X t−1 =(1−B)X (5)
|            |     |               |         |     |        |               |     |     |     | t t |     |     |     | t   |     |
| ---------- | --- | ------------- | ------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| has access |     | to the entire | dataset | as  | values | are collected | in  |     |     |     |     |     |     |     |     |
real-time, such that only past values are available. For our for all t > 1 [2]. The order of differencing can be repre-
sentedbyasymbold,suchthat∇dX
dynamic threshold, we used the mean absolute deviation t denotesthedth-order
(MAD)calculatedas: differenced time series. For example, when d = 2, it is the
second-orderdifferencedtimeseries[2].Therefore,adiffer-
|     | MAD=median(|X |     |     | −median(X)|) |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |               |     |     | i            |     |     | (1) |     |     |     |     |     |     |     |     |
encedtimeseriescanbeexpressedmoregenerallyas:
| where                                                | X is | the portion | of data | values | in  | a rolling | sample |     |     |     |          |     |     |     |     |
| ---------------------------------------------------- | ---- | ----------- | ------- | ------ | --- | --------- | ------ | --- | --- | --- | -------- | --- | --- | --- | --- |
|                                                      |      |             |         |        |     |           |        |     |     | ∇dX | =(1−B)dX |     |     |     | (6) |
| windowtolimittheimpactofolderdatavalues[2].Unlikethe |      |             |         |        |     |           |        |     |     |     | t        |     | t   |     |     |
meanandstandarddeviation,MADisrobustwhenanomalies
|     |     |     |     |     |     |     |     | for all t | > d | [2]. However, |     | no amount |     | of differencing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | --------- | --- | --------------- | --- |
arepresentinthedatasample,andthereisnodistortionunless
willremoveaseasonaltrendfromdata.Seasonaltrendscan
atleastahalfofthesampleiscomposedofanomalies[2],[5].
|     |     |     |     |     |     |     |     | be eliminated | by  | seasonal | differencing, |     | which | differences |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------------- | --- | ----- | ----------- | --- |
Wethenmultiplythethresholdwithaconstanttoadjustthe
|                                                        |     |     |     |     |     |     |     | against the | previous | season | instead | of  | the | first lag | [2]. Let |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------ | ------- | --- | --- | --------- | -------- |
| sensitivityofouranomalydetection,resultinginouranomaly |     |     |     |     |     |     |     | ∇dX         |          |        |         |     |     |           |          |
beaseasonallydifferencedtimeseries,wheremisthe
| detectionmetricdefinedas: |     |     |     |     |     |     |     | m   |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
periodoftheseasonaltrend,thenitisdefinedas:
=|ε |>|s∗MAD|
|     | AnomalyDetected |     | t   | t   |     |     | (2) |     |     |     |           |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
|     |                 |     |     |     |     |     |     |     |     | ∇dX | =(1−Bm)dX |     |     |     | (7) |
|     |                 |     |     |     |     |     |     |     |     | m   | t         |     | t   |     |     |
whereε istheanomalyscoremeasuredattimet,andsisthe
t
|                         |     |     |     |     |     |     |     | >d      | ∗m[2]. |     |     |     |     |     |        |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --- | --- | --- | --- | --- | ------ |
| sensitivityconstant[2]. |     |     |     |     |     |     |     | forallt |        |     |     |     |     |     |        |
| VOLUME11,2023           |     |     |     |     |     |     |     |         |        |     |     |     |     |     | 106457 |

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
D. SEASONALAUTOREGRESSIVEINTEGRATEDMOVING Thesecondpartisthespatialpooler.Thespatialpooleris
AVERAGE(SARIMA) responsible for learning spatial patterns present in the data.
The seasonal autoregressive integrated moving average It starts by taking in a fixed number of encoded SDR bits
(SARIMA)denotedasSARIMA(p,d,q) isanextensionof then assigns a layer containing columns [13]. Each column
m
theautoregressiveintegratedmovingaveragemodeldenoted hasasetofpotentialsynapses,aconnectiontotheprevious
as ARIMA(p,d,q) by incorporating a seasonal component layer representing a subset of the input bits [13]. Connec-
intoitsforecastingmodel.Bothmodelsarebasedonacom- tions between the layers are then determined based on the
bination of the autoregressive model (AR) and the moving comparisonbetweenperformancevaluesandaperformance
average (MA) model. The autoregressive model predicts X threshold[13].Theactivesynapsesofeachcolumnarethen
usingitsmostrecentlags[2].LetAR(p)beanautoregressive determined based on how many connected columns exist
modeloforderpthatpredictsthevalueofX attimetas: [13].Asmoredataarecollected,thespatialpoolerdetermines
howmanyconnectedsynapsesofeachcolumnoverlapwith
p
X =c+ε + X aBiX (8) the input SDR bits, and activates columns with the most
t t i t
overlap [3]. Only active columns update their connections,
i=1
then the network boosts or hinders columns accordingly to
forallt > p,wherea = {a ,a ,...,a }isthepparameters
1 2 p preventcolumnsfrombeingtoodominant[2].
forthemodel[2],[12].LetARMA(p,q)beanautoregressive
ThethirdandfinalpartoftheHTMlearningmodelisthe
moving average model (ARMA), where p represents the
temporalmemory.Temporalmemorydoestwothings:learns
orderofARandqrepresentstheorderofMA,definedas:
the sequences of SDRs produced by the spatial pooler and
p q makes predictions [13]. The temporal memory establishes
X X
X =c+ε + aBiX + bBiε (9)
t t i t i t connections between cells in the spatial pooler’s columns,
i=1 j=1 then learns the connections between cells that reside in the
for all t > max{p,q} [2], [12]. The ARIMA(p,d,q) model same layer [13]. An active cell forms connections to other
predicts X by modeling the differenced series ∇dX with an cellsthatwerejustactive.Thisway,thecellscanpredictwhen
ARMA(p,q)model[2].TheSARIMA(p,d,q) modelpre- they will likely become active by referring to their current
m
dictsX bymodelingtheseasonallydifferencedseries∇dX connections[13].
m t
withanARMA(p,q)model: HTMalsocalculatesitsownanomalyscorebymeasuring
thedeviationbetweenitspredictedinputandtheactualinput
p q
X =c+ε +( X aBi∇dX )+( X bBiε ) (10) [9].Theanomalyscoreattimet denotedass t ,isgivenas:
t t i m t i t
i=1 j=1 s =1− π(X t−1 )∗a(X t ) (11)
where X = ∇dX + Pd−1∇i BmX [2]. Although the
t |a(X
t
)|
t m t i=0 m t
wherea(X )isthesparseencodedvalueoftheinputattimet,
SARIMA model is one of the best and most common time t
series forecasting models, it is unable to incorporate more
|a(X
t
)|isthetotalnumberof1-bitsina(X
t
),andπ(X
t−1
)is
theinternalpredictionofa(X )[10].Theanomalyscorewill
thanoneseasonaltrendintoitsforecasting. t
be0ifthecurrentinputisperfectlypredictedor1otherwise
[9].Toincreasetheanomalydetectionaccuracy,ashort-term
E. HIERARCHICALTEMPORALMEMORY(HTM)
averageofthepredictionerrorsiscomputed,thenathreshold
Hierarchical Temporal Memory (HTM) is a neural
is applied to the Gaussian tail probability to determine if
network-based machine learning algorithm derived from
a data point is truly an anomaly [10]. This second step in
neuroscience that models spatial and temporal patterns in
determiningtheanomalyscoreisthecomplimentofthetail
streaming data [9]. HTM works by simulating how the
probabilityandisdefinedastheanomalylikelihood:
neocortex works in the human brain [13]. It is versatile and
tolerable to noisy data and can detect even the most subtle L =1−Q( µ′ t −µ t ) (12)
anomalies, resulting in a low false positive rate with most t σ
t
rea
T
l
h
a
e
no
l
m
ea
a
r
l
n
ie
in
s
g
de
o
te
f
c
H
te
T
d
M
[3].
can be broken down into three whereµ′ t =
Pi
i
=
=
W
0
′
j
−1st−i,µ
t isthemeanofthesampleofpast
main parts: The first part is the encoder and the Sparse anomalyscores,σ t isthestandarddeviationofthesampleof
Distributed Representations (SDRs) [3]. SDRs help explain past anomaly scores, µ’ t is the short-term average, Q is the
how brains can make semantic generalizations [13]. SDRs Gaussiantailprobabilityfunction,andW′ isawindowfora
are represented by vectors that contain thousands of bits, shorttermmovingaverage[9],[10].
andtheencodergivesthebitsmeaningbyencodingthemto
representthepropertiesofarepresentation[13].Theencoded F. TBATS
propertiesoftwoSDRsarecompared,andiftheyhave1-bit The Trigonometric seasonality, Box-Cox transformation,
inthesamelocation,thentheysharesomesimilarities[13]. ARMA errors, Trend and Seasonal components model,
Themore1-bitsthetwoSDRsshare,themoresemantically denoted as TBATS, is a forecasting model for complex
similarthetworepresentationsare[13]. time series that can include multiple seasonal periods,
106458 VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
high-frequencyseasonality,non-integerseasonality,anddual asseasonalcomponentsbasedontheFourierseries:
calendar effects [8]. TBATS is currently one of the best
multi-seasonal time series forecasting models and is the s (i) = X
ki
s (i) (17)
most common [1]. It utilizes a framework that incorporates t j,t
j=1
Box-Coxtransformations,Fourierrepresentationswithtime-
varying coefficients, and ARMA error correction [8]. The s ( j, i t ) =s ( j, i t ) −1 cosω j (i)+s ∗ j, ( t i − ) 1 sinω j (i)+γ 1 (i) d t (18)
TBATSmodelrequirespre-specifiedseasonalperiodsthatare s ∗(i) =−s (i) sinω(i) +s ∗(i) cosω(i) +γ(i) d (19)
thenmodeledbyatrigonometricrepresentationbasedonthe j,t j,t−1 j j,t j 2 t
Fourierseries[1],[11].
where
γ(i)
and
γ(i)
are the smoothing parameters, k is
TBATS is an extension of the Box-Cox transformation, 1 2 i
the amount of harmonics for the ith seasonal period, and
ARMA errors, Trend, and Seasonal components (BATS) ω(i) =2πj/m [8],[11].
model, where the addition of trigonometric seasonality cre- j i
ates a more flexible parsimonious approach [8]. BATS,
III. PROPOSEDDETECTIONMETHODS
however,isanextensionofexponentialsmoothingmethods
A. MULTI-SARIMA
that combine its other components like Box-Cox transfor-
Most forecasting models today include at most one sea-
mations and ARMA errors to produce a better forecasting
sonal component, and this unnecessary restriction only
model[15].TheexponentialsmoothinginBATSutilizesthe
hinders their potential. Allowing a model to take full
Holt-Winters method that handles time series with a trend
advantage of every known seasonal pattern in a dataset
and a single seasonality [8], [15]. The exponential smooth-
gives more options and possibilities for it to perform bet-
ing works by having future values be weighted averages of
ter. Our proposed model, named multi-SARIMA, extends
past values [15]. The Box-Cox transformation in the model
the original SARIMA(p,d,q) model and is denoted as
stabilizesthevarianceandmeanovertime,makingthetime m
SARIMA(p ,d ,q ) × (p ,d ,q ) . It predicts X by
seriesstationary.ARMAerrorsinthemodelareappliedtothe 1 1 1 m1 2 2 2 m2
modeling the seasonal differenced series
∇d2X
with two
residualstocaptureanyleftoverinformation[15].Thetrend m2
SARIMA(p,d,q) models:
captureslong-termchangesinthemean.Lastly,theseasonal m
com
Th
p
e
on
B
e
A
nt
T
c
S
ap
m
tu
o
r
d
e
e
s
l
a
w
ti
a
m
s
e
im
se
p
ri
r
e
o
s
v
’
e
p
d
er
t
i
o
od
f
i
o
c
r
a
e
l
c
v
a
a
s
r
t
ia
ti
t
m
io
e
n[
s
1
e
5
ri
]
e
.
s ∇ m d2 2 X t =
(cid:16)Xp
i= i 1 a 1,i Bm1i
(cid:17)
∇ m d2 2 X t
w tri i g th on m om ul e t t i r p i l c e se s a e s a o s n o a n l a i l ty c a o s m w p e o ll n a e s n u ts pd w at i e th dv t e h r e sio a n d s di o ti f o s n om o e f + (cid:16)Xp i= 2 1 a 2,i Bm2i (cid:17) ∇ m d2 2 X t
m [1 e 5 t ] h . o T d h s et u r s ig e o d no in me B t A ri T c S sea to son c a re li a t t y e in th T e BA T T B S AT re S pre m s o en d t e s l e [ a 8 c ] h , − (cid:16)Xp j= 2 1 Xp i= 1 1 a 1,i a 2,j Bm1i+m2j (cid:17) ∇ m d2 2 X t +ε t
seasonalcomponentinatimeseriesasatrigonometricrepre- +
(cid:16)Xq1
b 1,i Bm1i
(cid:17)
ε t +
(cid:16)Xq2
b 2,i Bm2i
(cid:17)
ε t
i=1 i=1
s a e ll n o t w at s io t n he b m as o e d d e o l n to th fi e t F m o u u l r t i i e p r le s , e l r a ie rg s e [ r 8 , ] a , n [ d 15 n ] o . n T - h in is te a g d e d r i s ti e o a n - + (cid:16)Xq2 Xq1 b 1,i b 2,j Bm1i+m2j (cid:17) ε t (20)
j=1 i=1
sonalcomponentswithlessrun-timethantheoriginalBATS
model[15]. whereX t =∇ m d2 2 X t +Pd i= 2 − 0 1Bm2∇ m i 2 X t ,m 1 istheshortersea-
TheBATSmodelcanberepresentedas: sonalperiod,m isthelongerseasonalperiod,d istheorder
2 2
ofdifferencing,a isthepparametersfortheshorterperiod,
1
y ( t λ) =l t−1 +φb t−1 + X T s ( t i − ) mt +d t (13) M b 1 A is o th rd e e q r p o a f ra th m e e s t h er o s rt f e o r r p th e e ri s o h d o , r p te 1 r i p s e t r h io e d s , e q a 1 so is n t a h l e A s R eas o o rd n e a r l
i=1 for the shorter period, a is the p parameters for the longer
2
αl t =l t−1 +φb t−1 +d t (14) period,b
2
istheqparametersforthelongerperiod,q
2
isthe
b t =ϕb t−1 +βd t (15) seasonalMAorderofthelongerperiod,andp 2 istheseasonal
p q ARorderforthelongerperiod.Themulti-SARIMAequation
X X
d t = φ i d t−1 + θ i e t−i +e t (16) was derived by extending the original SARIMA equation.
i=1 i=1 Themulti-SARIMAequationcontainsseasonalARandMA
terms for individual season lengths m and m followed by
1 2
where y
(λ)
is the Box-Cox transformed time series at time additionaltermsthataccountforthecombinationofthetwo
t
(i)
t, s is the ith seasonal component, l is the local level at seasonaltrends,andthebackshiftoperatorbeingscaledbythe
t t
time t, b is the trend with damping at time t, d is the seasonlength.Wealsoincludedadditionalfactorstoaccount
t t
ARIMA(p,q) process, e is white noise, φ and θ are the for the nonseasonal trend (p,d,q) in the multi-SARIMA.
t
ARIMA(p,q) coefficients, φ is the trend damping, α and β Fromthere,wedistributethefactorsandsolvefortheloneX
t
arethesmoothing,T istheamountofseasonalities,λ isthe to get the final equation depicted above. We concluded that
Box-Coxtransformation,andm isthelengthoftheithsea- weonlyneedtodifferenceusingd andm sincedifferencing
i 2 2
sonalperiod[8],[11].TheBATSmodelisthenextendedby overthelongerseasonaltrendcapturesbothseasonalitiesand
adding the trigonometric seasonal model and is represented makesthedatastationary.Wesetd =0sincewedifference
1
VOLUME11,2023 106459

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
thedataandobtainastationaryversionusingd 2 ,eliminating TABLE1. Overviewofthedatasets.
d fromappearinginthemulti-SARIMAequation.
1
In our approach, the first model is trained on three itera-
tions of the shorter seasonal trend, while the second model
is trained on three iterations of the longer seasonal trend.
Fromthefirstmodel,weobtaintheseasonalandnon-seasonal
autoregressiveandmovingaverageparameters,theresiduals,
and the constant. From the second model, we obtain just
theseasonalautoregressiveandmovingaverageparameters.
Duringtheprediction,weapplythevaluesfrombothmodels
to the multi-SARIMA equation to get the prediction X at
timet. For our experiments,we used the MA and SIMAmodels
We expect the multi-SARIMA model to perform well, as our first step to create the initial labeling, then verified
comparedtoothermodels,whenitisusedwithdatasetsthat thelabelswithSARIMA,ourmulti-SARIMA,andTBATS.
containtwomeaningfulseasonaltrends.Ifadatasetdoesn’t Wedenoteacombinationoftwomodelsusedinthetwo-step
have meaningful seasonal patterns, the multi-SARIMA approach as ‘first step + second step’. For example, a two-
model is not expected to perform better. If a dataset con- stepapproachthatusesMAasthefirststepandSARIMAas
tainstwoseasonaltrends,buttheyareinsignificant,thenthe
thesecondstepisdenotedasMA+SARIMA.
multi-SARIMAmodelisnotguaranteedtoperformbetter.
Betterperformanceentailsthatthemulti-SARIMAmodel IV. DATASETS
has higher anomaly detection accuracy, meaning a higher We evaluated all models on three different datasets. Two
true positive rate with a lower false positive rate. With this datasetsarefromtheNumentaAnomalyBenchmark(NAB),
higherprecision,however,wealsoexpecttheruntimeofthe acollectionoflabeled,univariate,real-worldtimeseriesdata
multi-SARIMA to be somewhat longer than those of other [6]. The third dataset is a synthetic time series dataset we
models. This is because the multi-SARIMA model requires createdusingourdatagenerationtool.Sincewearefocused
more fitting and learning than other models as it uses two on multi-seasonal anomaly detection in time series data,
differentmodelsandlearnsovertwoseasonalperiods. the three datasets contain two meaningful seasonal trends,
numeroushand-labeledanomalies,andenoughdatapointsto
trainandtestmodelson.Ageneralsummaryofeachdataset
B. TWO-STEPAPPROACH isgiveninTable1.WeusedasmallerversionoftheHotGym
The two-step approach for anomaly detection was initially datasetasoneanomalyoccurredwithinthefirstthreeweeks
proposed by us in [2]. The algorithm consists of a simpler ofthedatacausestrainingissueswithsomemodels.
modelthatcanlabeldatafastwithlessaccuracyandamore
complex model that can label data accurately but requires A. MSTLSEASONALDECOMPOSITION
more time [2]. In the two-step approach, the first step does Sinceourmulti-SARIMAmodelutilizestwoseasonalcom-
the initial labeling with the faster but less accurate model, ponents,weshouldconfirmthatourtestdatasetscontaintwo
then the second step verifies the first step’s labels with the meaningfulseasonaltrends.Forthatpurpose,weusedMul-
slower but more accurate model [2]. The first model must tipleSeasonal-TrenddecompositionusingLocallyEstimated
pick up as many true positives as possible, then the second ScatterplotSmoothing(Loess)(MSTL)[7].Thereareafew
step denies most of its false positives and verifies its true multi-seasonaltimeseriesdecompositionmethodsavailable,
positives[2].So,thiscombinedapproachislimitedtothetrue including Facebook’s Prophet, TBATS, and Seasonal-Trend
positiverateofthefirstmodelbutreducesthefalsepositive DecompositionusingRegression(STR);however,wechose
rate [2]. In the worst case, the first model finds every data MSTL because it produces the lowest root mean squared
pointanomalous,causingthesecondsteptoverifyeverydata error, is robust to outliers, has the smallest execution time,
pointinthedataset[2].Theruntimeofthetwo-stepisatbest andiseasytouseasitrequiresminimalparameters[7],[14].
slightlyslowerthanthefirstmodelandatworstslightlyfaster MSTL decomposes an additive time series into a trend
thanthesecondmodel. component,givenseasonalcomponents,andaresidualcom-
Although the two-step approach is not new by itself, ponent[7],[14].MSTLisanextensionoftheSeasonal-Trend
usingourmulti-SARIMAasthesecondstepinthetwo-step decompositionusingLoess(STL)modelasSTLisonlyable
approachis.Sinceweexpectourmulti-SARIMAtoperform todecomposetimeseries withoneseasonalcomponent[7],
better than other models, when it is used with datasets that [14]. Loess is a scatterplot smoothing technique that fits a
contain two meaningful seasonal trends, we also expect our curvetoascatterplottodeterminethedegreeofthepolyno-
multi-SARIMAtoperformwellwhenitisusedasthesecond mial[14].STLappliesLoesstovarioustransformationsofthe
step in the two-step approach. For the two-step approach, giventimeseriesandthenextractsthetrendandoneseasonal
betterresultsentailmaintainingthetruepositiverateoffirst component [14]. MSTL extracts each known seasonal com-
stepmodelwhilesignificantlyreducingitsfalsepositiverate. ponentinatimeseriesusingSTLonebyone[7],[14].MSTL
106460 VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
FIGURE1. MSTLdecompositionoftheNYCTaxidatasetforoneweekof
data.Thetopgraphdepictsthedataset’sdailyseasonaltrendwhilethe FIGURE2. MSTLdecompositionoftheSyntheticDatasetforoneweekof
data.Thetopgraphdepictsthedataset’sdailyseasonaltrendwhilethe
bottomgraphdepictsitsweeklyseasonaltrendwiththeweekend
highlightedinred. bottomgraphdepictsitsweeklyseasonaltrendwiththeweekend
highlightedinred.
firstordersthegivenseasonalperiodsfromshortesttolongest
toavoidshorterseasonalperiodsfrombeinginterlacedwith
| the longer | seasonal | periods | [7]. | MSTL | then applies | STL |     |     |     |     |     |
| ---------- | -------- | ------- | ---- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
iterativelyoneachidentifiedseasonalperiod[7].TheMSTL
additivedecompositionofatimeseriescanbedefinedas:
|     | X =S1+S2+···+Sn+T |     |     |     | +R  | (21) |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     | t                 | t   | t   | t   | t t |      |     |     |     |     |     |
S1,S2,...,Sn
| where     |          |             | denotes       | the seasonal | components,   |            |     |     |     |     |     |
| --------- | -------- | ----------- | ------------- | ------------ | ------------- | ---------- | --- | --- | --- | --- | --- |
|           | t t      | t           |               |              |               |            |     |     |     |     |     |
| T denotes | the      | trend,      | and R denotes |              | the remainder | [7].       |     |     |     |     |     |
| t         |          |             | t             |              |               |            |     |     |     |     |     |
| We used   | Python’s | statsmodels | MSTL          |              | package       | on a Linux |     |     |     |     |     |
virtualmachinetoperformtheMSTLdecompositiononour
datasetsasdepictedinFig.1–3.
| Fig. | 1 depicts | one week | of MSTL | decomposition |     | on the |     |     |     |     |     |
| ---- | --------- | -------- | ------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
FIGURE3. MSTLdecompositionoftheHotGymdatasetforoneweekof
| NYC | taxi dataset, | where | the vertical |     | axis represents | the |     |     |     |     |     |
| --- | ------------- | ----- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
data.Thetopgraphdepictsthedataset’sdailyseasonaltrendwhilethe
smoothingfortheseasonalcomponentgiven.Theseasonality bottomgraphdepictsitsweeklyseasonaltrendwiththeweekend
highlightedinred.
| in the      | data follows | a typical    | workweek    |            | and makes | sense,     |     |     |     |     |     |
| ----------- | ------------ | ------------ | ----------- | ---------- | --------- | ---------- | --- | --- | --- | --- | --- |
| considering | that         | the original | data        | represents | taxi      | passengers |     |     |     |     |     |
| in New      | York City.   | The          | daily trend | is very    | low early | in the     |     |     |     |     |     |
morning, then has spikes before midday since everyone is workweekandmakessense,consideringthattheoriginaldata
|     |     |     |     |     |     |     | represents | a gym’s energy | consumption | in Australia. | The |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ----------- | ------------- | --- |
tryingtogettowork,adiparoundnoonsincenooneisout
|     |     |     |     |     |     |     | daily trend | shows that | the data values | tend to have | a small |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------------- | ------------ | ------- |
andabout,thehighestspikesintheafternoonwheneveryone
isheadinghomeortravelingaroundthecity,thenendswith spikeatmidnightandthenareverylowearlyinthemorning
|        |         |               |       |          |       |           | until midday | where there | is the highest | spike during | the |
| ------ | ------- | ------------- | ----- | -------- | ----- | --------- | ------------ | ----------- | -------------- | ------------ | --- |
| very a | low dip | late at night | since | everyone | is at | home. The |              |             |                |              |     |
weeklytrendfollowsatypicalworkweekwiththeweekdays hottestandbusiesttimeoftheday,thendecreasesbackdown
maintaining the same taxi usage pattern until the weekend for the rest of the day as the sun goes down and people go
home.Theweeklytrendshowsthatthroughouttheweekdays,
| showing | a different | pattern  | and     | higher        | spikes during | later  |                                                   |               |                  |           |         |
| ------- | ----------- | -------- | ------- | ------------- | ------------- | ------ | ------------------------------------------------- | ------------- | ---------------- | --------- | ------- |
| hours.  |             |          |         |               |               |        | thetrendseemstobesomewhatconsistentaspeopletendto |               |                  |           |         |
|         |             |          |         |               |               |        | visit the                                         | gym regularly | during the week, | until the | weekend |
| Fig.    | 2 depicts   | one week | of MSTL | decomposition |               | on our |                                                   |               |                  |           |         |
Syntheticdataset.Wegeneratedoursyntheticdatatosimulate thathasnohighspikesbutverylowdipsasnotmanypeople
atypicalworkschedule.Thedailytrendshowsthatthedata aregoingtothegymoritisclosedduringdifferenthours.
| values | tend to | be very | low early | in the | morning, | then has |     |     |     |     |     |
| ------ | ------- | ------- | --------- | ------ | -------- | -------- | --- | --- | --- | --- | --- |
a spike before midday, a small dip around noon, another B. DIFFERENCING
spike in the afternoon, and ends with very a low dip late at For the differencing of our test datasets in order to make
night. The weekly trend shows that the trend is consistent themstationary,wedecidedtouseseasonaldifferencingsince
throughouttheweekdays,thenshiftingtohavinglowervalues theycontainapparentseasonaltrends,specificallydailyand
duringtheweekend. weekly seasonalities. So, we differenced using first-order
Fig. 3 depicts one week of MSTL decomposition on the seasonal differencing with a period of one week. This cap-
HotGymdataset.Theseasonalityinthedatafollowsatypical turesboththedailyandweeklyseasonaltrendsandproduces
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     | 106461 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
TABLE2. Single-stepexperimentalresults.
dataset. Since there are a very small number of anomalies
withinalargenumberofdatapointsineachdataset,compar-
ingperformancebasedonaccuracypercentageisineffective
as a model that never labels any data point as anomalous
wouldachievemorethan90%accuracy[2].Instead,wefocus
on which models produce the most true positives with the
lowestnumberoffalsepositives.Thismeans,thebestmodels
wouldbeabletolabelallanomaliescorrectlywhilenotlabel-
ing other non-anomalous data points as anomalies. Table 2
showsthefinalsingle-stepresultsofallmodels,andTable3
showsthefinaltwo-stepresults,whereTPisthenumberof
truepositives,FPisthenumberoffalsepositives,andFNis
thenumberoffalsenegatives.
FIGURE4. NYCTaxidatasetafterfirst-orderseasonaldifferencingwitha
periodof1week.Anomaliesaredepictedbytheredlines. A. SINGLE-STEPEXPERIMENTALRESULTS
For our single-step experimental results shown in Table 2,
our multi-SARIMA model had the highest number of true
stationarydata.Fig.4depictsourNYCTaxidatasetsafterthe positives for every dataset while maintaining fewer false
first-orderseasonaldifferencingwasapplied.Thebeginning positivesthantheSARIMAmodelforeverydataset,although
ofthegraphhasaflatlinebecausethefirstweekhasnoprior withlongerruntime.Ourmulti-SARIMAhadeitherthebest
datatodifferenceagainst[2]. orsecond-bestresultsforeverydataset.
Themulti-SARIMAhadthehighestruntimecomparedto
V. EXPERIMENTALRESULTS othermodelsbecausethemulti-SARIMAistheonlymodel
To properly compare our multi-SARIMA model, we used thatcombinestheresultsfromtwomodelswhichtrainover
existingforecastingmodelsMA,SIMA,SARIMA,TBATS, the two seasonal periods of one day and one week, respec-
and HTM. MA, SIMA, SARIMA, TBATS, and our pro- tively.SinceeveryotherseasonalmodelbutTBATSislimited
posedmulti-SARIMAwereimplementedinPython3.8.5on tooneseasonaltrend,theyaretrainedovertheperiodofone
a Windows 10 computer with an Intel i7 8-core processor dayasthatistheirstrongerseasonality.Trainingtwomodels
operatingat3.80GHz,16GBofmemory,anda1TBSSD. andhavingonetrainingoveraweekrequiredtheextratime
Numenta’s HTM algorithm was implemented on the same but produced better results. Specifically, the runtime of the
machine,usingPython2.7.Theoptimalparametersforeach multi-SARIMA on the NYC Taxi dataset was unexpectedly
model were determined by a grid search, and we compared long.ThisisbecausetheNYCTaxidatasetistheonlydataset
thebestperformancesofallmodelsinthissection.Weused with a data point every 30 minutes instead of every hour,
open-source python libraries provided by their authors for causing the 3-week training data to contain a large amount
our implementations of HTM and TBATS. For MA, SIMA, of data for the models to train on. The other multi-seasonal
andSARIMAweusedPython’sstatsmodelspackage.Forthe model, TBATS, was also slow and had the second longest
two-stepapproach,weusedMAandSIMAasthefirststep, runtime for every dataset. TBATS may be a more refined
andSARIMA,TBATS,andourproposedmulti-SARIMAas model,butitstillrequiresmoretimesincethatisthenature
thesecondstep. oflearningmultipleseasonalpatterns.
Allmodelsweretrainedonthefirstthreeweeksofthedata, Our multi-SARIMA was the only model that achieved
then evaluated on the remaining data. We made sure there the same number of true positives as HTM for the NYC
were no anomalies present in the training portion of each TaxidatasetandoutperformedeverymodelfortheHotGym
106462 VOLUME11,2023

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
TABLE3. Two-stepexperimentalresults.
dataset. The multi-SARIMA doubled the true positive rate fourthanomalydetectedbyMA,causingthemtolabelitas
of HTM and TBATS for the HotGym dataset while still non-anomalouswhentheywereusedinthesecondstep.
| maintaining | the | second | lowest | false positive | rate | among all |                               |     |     |     |     |     |     |
| ----------- | --- | ------ | ------ | -------------- | ---- | --------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
| models.     |     |        |        |                |      |           | VI. CONCLUSIONANDFUTURETOPICS |     |     |     |     |     |     |
Expectedly,thetwomulti-seasonalmodelsperformedthe When data contains repeated patterns such as seasonality,
bestfortheSyntheticdataset.Mostmodelsdetectedallfive they can be learned and applied to a forecasting model to
anomalies,butTBATSandmulti-SARIMAdidsowithunder improve the accuracy of the model. Today, time series data
ten false positives. HTM performed very poorly with this containing multiple seasonalities are common in real-world
dataset,andwethinkthatisbecausethedatasetwascreated applications[7].However,mostexistingmodelsforanomaly
usingrandomness,throwingoffthelearningofHTM. detection in time series data can include just one or no sea-
Notably, TBATS had either the same or higher true posi- sonalcomponent,sotheycannotcaptureeveryseasonaltrend
tiverate thantheoriginalSARIMAfor everydataset,while thatappearsindatasets.
maintainingalowerfalsepositiverate. Our multi-SARIMA model takes the original SARIMA
modelonestepforwardbyincludingmultipleseasonalcom-
|     |     |     |     |     |     |     | ponents | instead | of just one. | The | multi-SARIMA |     | produced |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | ------------ | --- | -------- |
B. TWO-STEPEXPERIMENTALRESULTS better anomaly detection results than the original SARIMA
foreverydatasetwetestedand,inmostcases,outperformed
| For our | two-step | experimental |     | results | shown | in Table 3, all |            |     |            |     |       |           |          |
| ------- | -------- | ------------ | --- | ------- | ----- | --------------- | ---------- | --- | ---------- | --- | ----- | --------- | -------- |
|         |          |              |     |         |       |                 | well-known | HTM | and TBATS. |     | Also, | we proved | that our |
two-stepalgorithms,eachofwhichusesacombinationoftwo
multi-SARIMAproducesbetterresultsthanSARIMAwhen
| models, | have less | false | positives | than | their standalone | first |     |     |     |     |     |     |     |
| ------- | --------- | ----- | --------- | ---- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
usedasthesecondstepinthetwo-stepapproachweproposed
| step results | shown     | in Table | 2,    | except          | for MA | + SARIMA     |             |           |                  |     |             |                |            |
| ------------ | --------- | -------- | ----- | --------------- | ------ | ------------ | ----------- | --------- | ---------------- | --- | ----------- | -------------- | ---------- |
| for the      | Synthetic | dataset  | which | produced        | the    | same results | in[2].      |           |                  |     |             |                |            |
|              |           |          |       |                 |        |              | In addition | to        | our multi-SARIMA |     | model,      | we             | showed the |
| as MA.       | This is   | because  | MA’s  | false positives |        | were already |             |           |                  |     |             |                |            |
|              |           |          |       |                 |        |              | anomaly     | detecting | capability       | of  | an existing | multi-seasonal |            |
verylowforthatdataset.Also,mosttwo-stepalgorithmshave
|     |     |     |     |     |     |     | forecasting | model | TBATS, | which |     | also outperformed |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | ----- | --- | ----------------- | --- |
significantlylessfalsepositivesthantheirstandalonesecond
SARIMAandHTM.
| step results | shown | in Table | 2,  | but have | less | true positives |     |     |     |     |     |     |     |
| ------------ | ----- | -------- | --- | -------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
because they are limited to the true positive rate of the first Differenttimeseriesdatasetshavedifferentcharacteristics,
|     |     |     |     |     |     |     | such that | no one | model | could be | the best | for | every case. |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | -------- | -------- | --- | ----------- |
step.
|     |     |     |     |     |     |     | However, | our multi-SARIMA |     | model | showed | very | accurate |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ----- | ------ | ---- | -------- |
Althoughwithmoreprocessingtime,themulti-SARIMA
as the second step produced significantly less false pos- detectionperformanceonvariousdatasetsweusedforevalu-
ationandbetteroverallresultsthanothermodels.
| itives than | the | original | SARIMA | as  | the second | step for |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Inthefuture,wewouldliketoincorporatesomeimprove-
| every dataset. |       | The only     | case | that produced | less | false pos-     |            |                  |            |         |           |      |              |
| -------------- | ----- | ------------ | ---- | ------------- | ---- | -------------- | ---------- | ---------------- | ---------- | ------- | --------- | ---- | ------------ |
|                |       |              |      |               |      |                | ments to   | the multi-SARIMA |            | model,  | including |      | the runtime  |
| itives than    | the   | multi-SARIMA |      | is TBATS      | for  | the Synthetic  |            |                  |            |         |           |      |              |
|                |       |              |      |               |      |                | reduction, | the              | ability to | capture | more      | than | two seasonal |
| dataset,       | which | was expected |      | as TBATS      | did  | better on that |            |                  |            |         |           |      |              |
dataset. Also, the two-step approach using multi-SARIMA trends, and a better way to choose optimal parameters.
|               |     |               |     |              |          |        | Moreover, | we  | plan to | compare | the performance |     | of our |
| ------------- | --- | ------------- | --- | ------------ | -------- | ------ | --------- | --- | ------- | ------- | --------------- | --- | ------ |
| as the second |     | step improved |     | the runtime, | compared | to the |           |     |         |         |                 |     |        |
multi-SARIMAmodelwiththoseofdeeplearningmethods,
standalonemulti-SARIMA,asitworkedonlessdatapoints.
suchasTemporalConvolutionalNetworks(TCN)[17].
Notably,TBATSdidbetterasthesecondstepthantheoriginal
| SARIMA                    | for every | dataset, | but | worse | than multi-SARIMA |     |            |     |     |     |     |     |     |
| ------------------------- | --------- | -------- | --- | ----- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| fortwoofthethreedatasets. |           |          |     |       |                   |     | REFERENCES |     |     |     |     |     |     |
[1] T.XieandJ.Ding,‘‘Forecastingwithmultipleseasonality,’’inProc.IEEE
| All two-step |     | algorithms | could | not | detect | the four true |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ----- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
Int.Conf.BigData,Dec.2020,pp.240–245.
positivesthatMAoriginallydetectedfortheHotGymdataset.
[2] R.E.SperlandS.M.Chung,‘‘Two-stepanomalydetectionfortimeseries
Webelievethisisbecauseothermodelscouldnotdetectthe data,’’inProc.Int.Conf.DataSoftw.Eng.(ICoDSE),Nov.2019.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     | 106463 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.T.Williamsetal.:AnomalyDetectioninMulti-SeasonalTimeSeriesData
[3] Z.Hasani,‘‘Robustanomalydetectionalgorithmsforreal-timebigdata: ASHTON T. WILLIAMS received the B.S. and
Comparisonofalgorithms,’’inProc.6thMedit.Conf.EmbeddedComput. M.S. degrees in computer science from Wright
(MECO),Jun.2017. StateUniversity,Dayton,OH,USA,in2022and
[4] C.C.Aggarwal,DataMining:TheTextbook.Cham,Switzerland:Springer, 2023, respectively. He is currently a software
2015. engineer.
[5] J. Hochenbaum, O. S. Vallis, and A. Kejariwal, ‘‘Automatic anomaly
detectioninthecloudviastatisticallearning,’’2017,arXiv:1704.07706.
[6] A. Lavin and S. Ahmad, ‘‘Evaluating real-time anomaly detection
algorithms—TheNumentaanomalybenchmark,’’inProc.IEEE14thInt.
Conf.Mach.Learn.Appl.(ICMLA),Dec.2015,pp.38–44.
[7] K.Bandara,R.J.Hyndman,andC.Bergmeir,‘‘MSTL:Aseasonal-trend
decompositionalgorithmfortimeserieswithmultipleseasonalpatterns,’’
2021,arXiv:2107.13462.
[8] A.M.DeLivera,R.J.Hyndman,andR.D.Snyder,‘‘Forecastingtime
series with complex seasonal patterns using exponential smoothing,’’
J.Amer.Stat.Assoc.,vol.106,no.496,pp.1513–1527,Dec.2011.
[9] S. Ahmad and S. Purdy, ‘‘Real-time anomaly detection for streaming
analytics,’’2016,arXiv:1607.02480.
[10] S. Ahmad, A. Lavin, S. Purdy, and Z. Agha, ‘‘Unsupervised real- RYAN E. SPERL receivedtheB.S.andM.S.degreesincomputerscience
timeanomalydetectionforstreamingdata,’’Neurocomputing,vol.262, fromWrightStateUniversity,Dayton,OH,USA,in2019and2020,respec-
pp.134–147,Nov.2017. tively.Heiscurrentlyasoftwareengineer.
[11] G.Skorupa.ForecastingTimeSeriesWithMultipleSeasonalitiesUsing
TBATSinPython.Accessed:Oct.24,2022.[Online].Available:https://
medium.com/intive-developers/forecasting-time-series-with-multiple-
seasonalities-using-tbats-in-python-398a00ac0e8a
[12] F. Orneholm, ‘‘Anomaly detection in seasonal ARIMA models,’’ Dept.
Math.,UppsalaUniv.,Uppsala,Sweden,ProjectRep.2019:18,2019.
[13] J.Hawkinsetal.(2020).BiologicalandMachineIntelligence.Release
0.4. [Online]. Available: https://numenta.com/resources/biological-and-
machine-intelligence/ SOONM.CHUNG(LifeMember,IEEE)received
[14] K.Manani.Multi-SeasonalTimeSeriesDecompositionUsingMSTLin the B.S. degree in electronic engineering from
Python.Accessed:Dec.5,2022.[Online].Available:https://towardsdata SeoulNationalUniversity,SouthKorea,in1979,
science.com/multi-seasonal-time-series-decomposition-using-mstl-in-
theM.S.degreeinelectricalengineeringfromthe
python-136630e67530
KoreaAdvancedInstituteofScienceandTechnol-
[15] M.Peixeiro.HowtoForecastTimeSeriesWithMultipleSeasonalities.
ogy,SouthKorea,in1981,andthePh.D.degreein
Accessed:Dec.6,2022. [Online]. Available: https://towardsdatascience.
computer engineering from Syracuse University,
com/how-to-forecast-time-series-with-multiple-seasonalities-
Syracuse,NY,USA,in1990.HeiscurrentlyaPro-
23c77152347e
[16] P.Dix,‘‘Whattimeseriesmattersformetrics,real-timeandsensordata?’’ fessorwiththeDepartmentofComputerScience
InfluxData,SanFrancisco,CA,USA,tobepublished. andEngineering,WrightStateUniversity,Dayton,
[17] Y.HeandJ.Zhao,‘‘Temporalconvolutionalnetworksforanomalydetec- OH,USA.Hiscurrentresearchinterestsincludedatabase,datamining,text
tionintimeseries,’’J.Phys.,Conf.Ser.,vol.1213,no.4,Jun.2019. mining,informationsecurity,datagrid,multimediadatabase,andparallel
[18] R.J.HyndmanandG.Athanasopoulos,Forecasting:PrinciplesandPrac- anddistributedprocessing.
tice,3rded.Otexts,2021.
106464 VOLUME11,2023