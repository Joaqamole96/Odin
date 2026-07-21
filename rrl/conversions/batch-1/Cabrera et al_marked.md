---
conversion_metadata:
  converted_at: "2026-07-21T05:43:13Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cabrera et al.pdf"
  source_pdf_sha256: "5b57b53fd75ff7246551d92b2b1742302303091540f58367c9735cd40d73a4ee"
  page_count: 18
  markdown_char_count: 142738
---

ARTICLE
OPEN
https://doi.org/10.1057/s41599-025-05205-z
Plastic to apparel: an analysis of sustainable
purchasing intention using a machine learning
ensemble
✉
Carmella Andrea L. Cabrera1, Ardvin Kester S. Ong 1,2 , John Francis T. Diaz3, Maela Madel L. Cahigas1 &
Ma. Janice J. Gumasing4
Theuseofplasticshasbecomeasignificantcomponentinmaintainingtheconvenienceand
suitability of modern lifestyles; however, a vast majority of the million tons of plastic man-
ufactured each year ends up in landfills, contributing to plastic pollution. With this, the
fashion industry has capitalized to create recycled products. Despite the proliferation and
continued presence of recycled and upcycle products, there still is a significant gap in the
sustainable purchasing behavior of consumers. This study aimed to identify, analyze, and
forecastthevariablesinfluencingconsumers’behavioralintentiontowardpurchasingapparel
made from plastic. This paper established the Sustainability Theory of Planned Behavior
model to determine the purchase intentions of Filipino customers while purchasing clothing
madeofrecycledplastic.Atotalof500validrespondentsweregatheredtoevaluatefactors:
Perceived Economic Concern, Perceived Environmental Concern, Perceived Authority Sup-
port, Subjective Norm, Attitude, Perceived Behavioral Control, Customer Perceived Value,
and Behavioral Intention. To analyze the data, the study utilized machine learning methods,
such as Random Forest Classifier (RFC) and Artificial Neural Network (ANN). Data pre-
processing using feature selection and correlation analysis was conducted to validate the
available data, performed data cleaning process, and data aggregation. Several iterative
processes were employed to generate the optimum classification model—obtaining a 92%
accuracy for RFC and 91% for ANN at 150 epochs under 30 hidden layer nodes. With low
error rates, the findings revealed that customer perceived value and perceived behavioral
control were the primary factors influencing consumers’ behavioral intentions toward pur-
chasingsustainableclothing.Thisstudyemphasizedtheconsiderationofthesefactorswhen
planning marketing strategies and initiatives to promote sustainable apparel.
1SchoolofIndustrialEngineeringandEngineeringManagement,MapúaUniversity,Manila,Philippines.2E.T.YuchengoSchoolofBusiness,MapúaUniversity,Makati,
MetroManila,Philippines.3DepartmentofFinanceandAccounting,AsianInstituteofManagement,Makati,MetroManila,Philippines.4DepartmentofIndustrial
✉
andSystemsEngineeringGokongweiCollegeofEngineering,DeLaSalleUniversity,Manila,Philippines. email:aksong@mapua.edu.ph
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 1
;,:)(0987654321

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
ITntroduction
he use of plastics has become a significant component in speedatwhichthemanufacturedproductsareproducedandthen
maintaining the convenience and suitability of modern discarded,aimingforinstantconsumption.Thismarketbecamea
lifestyles.Consideringitsadaptabilityandremarkablecost- globalizedindustry,utilizingcheaplaborandmaterialsallaround
performanceratiooverthepastseveralyears,ithasencompassed the world (Zhang et al. 2021). This led to an increase in non-
everything from everyday life to commercial manufacturing recyclable waste in landfills (Gomes de Oliveira et al. 2022).
(Chang et al. 2019). Since then, majority of our daily activities Different studies (Niinimäki et al. 2020; Brewer 2019) explained
have incorporated the usage of plastics—ranging from various that fast fashion is now the industry with the second-highest
food and beverage, cosmetics, toiletries, pharmaceuticals, and pollutant emissions at 10%. It was explained that large amounts
other products. These industries require packaging for their fin- of raw materials are needed for manufacturing fashion, which
ishedproductsinpreparationofitssafeandeffectivedistribution producesasubstantialamountofwastethatleavesaconsiderable
to customers (Evode et al. 2021). carbon footprint and produces a significant level of pollution
Shams et al. (2021) discussed how the overwhelming bulk of (Grazzini et al. 2021).
theannualonemilliontonsofplasticproduction,includingitems Nowadays,clothingcompaniesarewidelyknownforputtinga
likewatercontainers,bags,foodcontainers,gloves,andcups,are lotmoreeffortintoproducingenvironment-friendlyapparelthat
discarded after every single use. In addition, the study by Zhang focusesonsustainability.H&M,Adidas,andNikeareamongthe
et al. (2022) stated that plastic pollution poses dangerous health many popular international clothing companies that have com-
repercussions for both humans and marine species. In areas mitted to driving advancements toward an improved fashion
where industrial wastes like plastics, rubber, and textiles are fre- future. According to H&M Group (2023), their resources are
quentlyburned,fumesandthereleaseoftoxicsubstancesintothe aimed to be either 100% recycled or obtained through more
air, producing unpleasant odors from waste materials—con- environmentally friendly means by 2023, with 30% recycled
tributing significantly to air pollution. Furthermore, a study materials by 2025. H&M also noted the use of recycled plastic,
conductedbyAwoyeraandAdesina(2020)mentionedthatoutof derived from sources like PET plastic drinking bottles, plastic
countless tons of plastic garbage, only 7% is recycled, approxi- bags, shampoocontainers,andvariousotherplasticpackagingis
mately 8% is burned, and the remaining is landfilled. To which, one of its most often obtained components, in which several of
consequences of the increasing price and energy related to the theirwell-knownaccessoriesaremadewithrecycledplastic.This
landfilling process led to water pollution caused by waste dis- approach could prevent further damage to the environment. In
carded into bodies of water. addition,Adidasengagesinavarietyofenvironmentalinitiatives.
Tiseo (2023) posited how the Pasig River in the Philippines One of which is using recycled plastic in manufacturing their
releases over 63,000 metric tons of plastic debris into the ocean products, which is a cornerstone of its commitment to reducing
every year (Fig. 1). The data in 2019 shows that the Pasig River plastic waste and reducing and preventing pollution in the
was estimated to have contributed 6.43 percent of all river- world’s oceans. The collaboration between Adidas and Parley is
derived ocean plastics, making the Philippines the world’s hea- one of the brand’s sustainability initiatives; Adidas gave the
viest contributor of plastic-polluting rivers. plastic waste from beaches and coastal towns a new life as an
OECD (2022) reported that 22% of plastic waste was impro- AdidasxParley product by intercepting the waste before it
perlyhandledandnotcollected,19%wasburned,49%endedup reached the ocean. Another project is initiated by Nike, starting
in landfills, and only 9% was recycled (Fig. 2). The growth in with the ‘Move to Zero’ program. The journey aims to reduce
emerging economies has caused the use of plastic to triple over waste and carbon emissions to safeguard the future of the sport.
the previous 30 years. In recent times, plastics have been One of the materials they utilize is recycled polyester, which is
responsiblefor3.4%ofglobalgreenhousegasemissions,withthis created by shredding plastic bottles, turning them into granules,
trend observed between 2000 and 2019, there was a double and then twisting the granules into high-quality yarn. Nike is
increase in global plastics manufacturing to 460 million tons. currentlyusingrecycledpolyestermadefromshreddedplasticto
In the fast fashion industry, one of their objectives is to lessen waste, approximately as much as 30% in comparison to
manufacture and dispose of clothing rapidly; it pertains to the newly produced polyester, and it helps keep 1 billion plastic
Fig.1Annualreportofplasticwasteemissionsfromselectedriversgloballytotheoceanasof2019.
2 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Fig.2OECDreportofthemanagementofplasticpollutiongrowthglobally,asof2019.
bottles out of landfills and rivers and streams each year (Nike thelevelofsocialvalueplacedoncustomersasindividuals,which
Sustainability 2024). contributes to these warm glow feelings, which improves how
In recent years, much significant research has focused on much you enjoy the accompanying consumption experience.
customers’ attitudes and behavior regarding sustainable fashion Thus, perceived customer value is evident among sustainable
productsbyexploringtheimportanceofsustainabilitywithinthe behaviors,whichshouldbeconsideredwhenassessingconsumer
fashion sector (Grazzini et al. 2021). Much research on behavior (German et al. 2022a).
environment-friendlyclothinghaslookedatthepotentialbenefits Despite many studiesexploring sustainable behaviors, it could
of eco-conscious product development approaches (Fung et al. be deduced that this recent advancement in apparel, sustainable
2021;Provinetal.2021),howcustomersengagewithsustainable practices, and consumption has still been underexplored—
fashion brands on social media platforms (Testa et al. 2021), implicating a research gap in the current trend of apparels. The
along with how consumers perceive, their attitudes toward, and holistic measurement of sustainable behavior should be investi-
theirwillingnesstoinvestinsustainablefashionproducts,andthe gated to assess the behavioral intentions of consumers. The
factors that affect these behaviors (Grazzini et al. 2021; Nike novelty of this study lies with the sustainability domains, which
Sustainability 2024). wereoneofthefactorswhichwasadoptedinthisstudy(German
Presented in Table 1 are the summarized key related studies et al. 2022a). Under the sustainability domains, five factors are
alongside the limitations and need for future works. being considered such as the human, environmental, economic,
Nguyen et al. (2020) conducted a fashion-focused survey in productivity, and social aspects (Hajishirzi et al. 2022). On the
Vietnam and found that 86% of the respondents were aware of otherhand,anestablishedtheoryinthefieldofbehavior,known
thepotentialtoincorporaterecycledplasticwasteintothefashion astheTheoryofPlannedBehavior(TPB),hasbeenaccessibleand
industry. Kim et al. (2021) highlighted that concerns about the extensively contemplated. It measures a person’s behavioral
aesthetic aspects of clothing made from recycled materials could characteristics,suchasthesocialaspectsthatpertaintosocialties
relate to worries about how well these garments blend with the and structures that promote stability and stability cohesiveness.
consumer’s existing wardrobe, their ability to align with the To ensure social sustainability, people and organizations must
consumer’sdesiredself-image,andtheircomfortintermsofsize. examine how to promote healthy social interactions and encou-
Asaresult,consumersmightdelayorchoosenottobuyproducts rage long-term social systems that promote peace in society
made from recycled plastic materials (such as clothing) due to (German et al. 2022a; Talan et al. 2020). These domains are
aesthetic risk (Kim et al. 2021; Testa et al. 2021). These studies crucial because they offer a framework for comprehending how
demonstrated that aside from sustainability domains, people’s individuals behave concerning sustainability. On the other hand,
behavior encompasses behavioral intention and actual behavior human aspects include things that improve people’s quality of
(Park and Lin 2020; Kuah and Wang 2020; Nguyen et al. 2020; life, such as social justice, education, and health.
Kim et al. 2021; German et al. 2022a). Studies focusing on human sustainability examined the best
In relation, Polyportiset al.(2022) mentioned that consumers ways for people and institutions to build equitable and envir-
who experience positive emotions as a byproduct of their efforts onmentally friendly communities (Abusafieh and Razem 2017).
tolessenenvironmental harmareamong theeffectiveresponses. Moreover, when it comes to determining productivity, one must
Customers perceive that selecting and valuing products crafted lookathoweffectivelyandefficientlyonecangeneratethingsand
from recycled materials would evoke positive and comforting services.Thisaspectisimportantsinceitmayhelpdecreasewaste
emotions,suchasprideasaresultoftheircontributiontoabetter and maximize resource consumption by enhancing production,
world (Adıgüzel and Donato 2021). Moreover, Magnier et al. which can enhance the overall performance of both people and
(2019) referred to expected moral awareness, which is char- organizations (Abdel-Shafy and Mansour 2018). On the other
acterized as a consumer’s hopes regarding the way the goods hand, environmental aspects pertain to the ecologically respon-
would make him or her feel from an ethical perspective. Tezer sible and sustainable practices that are assessed, which also pro-
and Bodur (2019) referred to the “warm glow” sentiments that tect various aspects of life (Gansser and Reich 2023).
come with just utilizing eco-friendly products, like those made Environmentalsustainabilityencompassesexaminingmethodsby
fromrecycledmaterials;itwasalsohighlightedthatanincreasein whichpeople andcompaniescan preserve resources,lessentheir
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 3

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
rehtohtiweromderolpxeebdluohs hcihw,roivahebllarevodnanoitnetni noitalubat-ssorcdnanoitalerrocylno sgnidnfiehtecfifusdluocnoitalerroc nitnemssessaevitatilauqredisnocot lerappaehtfonoissergorpehtoteud etaercotsrotcafrehtognitagitsevnI
|     | rellamsderedisnocylnoevahyehT ecnislootsisylanasseworprehgih | htiwtfienebdluoctub,ydutsehtfo | ylnodnastnedutsderedisnocylnO detseggusydutsehT.ygolodohtem | eehteromdnatsrednuotdednetxe | srotcaferometacilpmidnadnapxE ydutssuounitnoc,krowemarfehtni esenihCnoylnodesucof,yrtsudni htiwsrotcafytilibaniatsusredaorb |     |
| --- | ------------------------------------------------------------ | ------------------------------ | ----------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --- |
srotcaflaroivahebfotnedecetnA gnisahcrupehtnoseidutsdetimil 91-DIVOCehtoteudeziselpmas esuotdetseggusdna,detaulave ebotdetseggusoslasawsrotcaf ,ssenevitceffeliaterrofseigetarts htiwecnadroccaniytilibaniatsus
llitsoslaeraerehT.seuqinhcet otseidutsdetalerroferutufeht ebotdetsegguserewsdohtem eromfonoitarolpxE.sremusnoc fotnemssessadna,sremusnoc ebdluoctnemegagneremusnoc
|     | erewstnedutsylno,cimednap | ,tahtetipseD.deredisnocsaw | elbaniatsusssessayllacitsiloh |                                                      |     | dna,ytilauqllarevo,ytilibarud |
| --- | ------------------------- | -------------------------- | ----------------------------- | ---------------------------------------------------- | --- | ----------------------------- |
|     |                           | tnecereromdnaataderom      | yrotarolpxeevitatilauqdesu    | evitanretladna)stnednopser foroivahebgniyubgnilcycer |     |                               |
|     | .tnemssessarehtrufsdeen   |                            |                               | 004>(eziselpmasregraL                                |     |                               |
|     |                           |                            | .esahcruplerappa              |                                                      |     | .dessessarehtruf              |
.slootlacitylana
.slootrehto
.dessessa
paG
esahcrupregraladetibihxestcudorp eraeveilebyehtsessenisubmorfyub sdoogdecudorpylbaniatsusyubohw esoohcylevitcadluowyehtdetacidni tnerapsnarteromerewyehtfisdnarb nislaitnedercelbaniatsusriehttuoba tnanimoderpehtdetutitsnocnemow ehtsadetpmorpsrotcaflanoitomorP ybdewollof,elbairavtnacfiingistsom .ecnacfiingisynaevahtondidsrotcaf .lerappadelcycergnisahcrupdrawot deviecreptahtdnuofsawti,ylbatoN decnuonorperomadaheulavytilauq stluserehT.erutufehtnidemusnoc degasremusnochguohtlatahtwohs dnaatartslaicosrehgihmorf54–52 dnuorgkcablanoitacuderehgihhtiw dnafosuoicsnoceromgnimocebera larevesllitseraerehT.ylevitarapmoc maertsniamehtgnitneverpselcatsbo
fo%53nahteromnignitluser,pag esehtgnisahcruptonstnednopser otesoohcsremusnoc’seirtnuocUE sremusnoC.eraflewlatnemnorivne dnatnetnoceromgnileefdetroper riehtdnastnemesitrevdariehthtob ,gnihtolcgnisahcrupnehwtnuocca latnemnorivnedna,laicos,lanosrep eulavdeviecrepfosnoisnemidruoF tcudorp,ylgnitseretnI.srotcafrehto wohssessaotelbasawydutsehT ebdluocstcudorpnoihsafdelcycer
elbarovafgnivahetipsedstcudorp tsomehtfoenosaytilibaniatsus otniekatotsnoitaredisnoclaicurc tahtdewohsseidutsehtnierehw sremusnocerusielhtafotnemges detaler-tcudorpehtelihw,srotcaf saegdelwonklatnemnorivnedna ylevitisoptahtsrotcaftnacfiingis nahtnoitnetniesahcrupnotceffe aetartsnomedtondidegdelwonk retseylop-nottocdelcycerfoesu
lerappadelcycpudnadelcyceR .snoitnetniesahcrupgnortsdna sedutitta’sremotsucdecneuflni .sedutittanotcapmitnacfiingis nehtytilibaniatsusnidetseretni dlodna51wolebdeganerdlihc sraey54revoregas’laudividni
|     |     |     | nielorgnidaeladeyalpdna | elbaniatsusarofgnitacovda |     |     |
| --- | --- | --- | ----------------------- | ------------------------- | --- | --- |
deredisnocslainnellimSU
rolaicosotgnitubirtnoc
.elytsefilerusielhta .gnihtolcdednelb
sgnidnfiniaM
.gnigakcap
|     | noitalubaT-ssorCdnanoitalerroC |     |     |     |     | weivretnipuorgfodohtemdexiM ehtroftnemssessaralubat-ssorc |
| --- | ------------------------------ | --- | --- | --- | --- | --------------------------------------------------------- |
,erauqs-ihc,sisylanaevitpircseD
|     |     |     | evisnetnI:sisylanaevitatilauQ | gniledoMnoitauqElarutcurtS | gniledoMnoitauqElarutcurtS | dnatnemssessaevitatilauqsa |
| --- | --- | --- | ----------------------------- | -------------------------- | -------------------------- | -------------------------- |
noissergercitsigoldna
.tcepsaevitatitnauq
ssecorpweivretni
)s(dohteM
|     | noihsaftsaffoytilibaniatsussdrawot |     | edam-retseylopdelcycergnisahcrup | fotcapmiehtetagitsevniotdemiA | htobssessaotkrowemarfroivaheb | detceffaeranrettapgnisahcrupdna |
| --- | ---------------------------------- | --- | -------------------------------- | ----------------------------- | ----------------------------- | ------------------------------- |
ecneirepxegnisahcrupnoderolpxE laicos,srotcaflanoitomorp,srotcaf deviecrepremotsucehtdenibmoC roivahebremusnocwohdenimaxE ralucitrapahtiw,gnihtolcdednelb
.spag rofsnoitpecrepeulav’sremusnoc lanosrep,srotcafdetaler-tcudorp -tcudorpdnacfiiceps-remusnoc lerappaelbaniatsusnosisahpme
| sremusnocfonoitnetniehtdna | edutittaremusnocfosisylanA |     |     | dnalatnemnorivnedna,srotcaf | -edutitta-egdelwonkdnaeulav |     |
| -------------------------- | -------------------------- | --- | --- | --------------------------- | --------------------------- | --- |
delcycerdnadelcycpugnoma delcycernosrotcafcimonoce retseylop-nottocdelcyceryb
|     |     |     | lainnellimelamefdenimaxE |     | delcycernosrotcafcfiiceps |     |
| --- | --- | --- | ------------------------ | --- | ------------------------- | --- |
.roivahebgniyubgnihtolc
dnaseidutsdetaleryekdezirammuS1
|     | .KUehtnistcudorp |     | .lerappaerusielhta |     |     |     |
| --- | ---------------- | --- | ------------------ | --- | --- | --- |
.stcudorpnoihsaf
.gnisidnahcrem
)s(evitcejbO
.stcudorp
|            |     |     | )1202(.lateihC | rahtkuMreehaJ | )4202(.lateniJ |             |
| ---------- | --- | --- | -------------- | ------------- | -------------- | ----------- |
| niLdnakraP |     |     |                | )4202(.late   |                | )4202(.late |
.lategnahZ
ecnerefeR
elbaT )0202(
|     | )1202( |     |     |     |     | atnarP |
| --- | ------ | --- | --- | --- | --- | ------ |
4 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
|     | .stlusertnereffidevahyam)noitacol lanoitiddatahtdetseggusoslasawtI rehtrufotdesuebyamslootrehtoro | dna,sremusnocKUnoylnodesucoF  | dnaedutittadetalerrocseidutsecnis |                                 |                              | ecuderotdesuebdluocnoitamotuA ledomfonoisnetxe,noissimenobrac | gnitsevniredisnocotdetseggussaw                                  |                                                              |                                 |
| --- | ------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------- | ------------------------------- | ---------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------- |
|     |                                                                                                   | dedeensitnemssessarehtruftaht | tub,raenilerewroivahebnotcapmi    | niahcylppusehtfoseitrapelpitluM |                              |                                                               | ,tnemtsevnietercsidrosuounitnoc dnascitsigolytrap-drihtregraldna | dnasnoitacilpmirehtonidessessa srotcafrehtodna,sdnamedtekram |                                 |
|     |                                                                                                   |                               | sahcus,dessessadnaderedisnoc      |                                 | saderedisnocebdluocselbairav |                                                               |                                                                  |                                                              | latotdna,seuqinhcetnoitazimitpo |
|     |                                                                                                   |                               | ,noitiddanI.tonsawydutsrieht      |                                 | dnaseussiytniatrecnu,sledom  |                                                               |                                                                  |                                                              | –emoctuossecorpniahcylppus      |
erewsremusnocZneGylnO ebdluocsrotcafytilibaniatsus lacitamehtamfotnempoleved gnilcycerredisnoc,snoisnetxe htiwseitniatrecnulaireganaM htiwtuptuoetalerroc,stcepsa
tnereffidtahtdna,dessessa cihpargoeg,ega(sremusnoc ebdluockrowemarfredaorb ,sretemaraprehtoredisnoC
|     |                         |     | ehtnonoitarolpxeredaorb .ecnereferpdnanoitpecrep | ehtnideredisnocebdluoc |     |                        | .ledomniahcylppusllarevo |     | dednetxerehtognipoleved |
| --- | ----------------------- | --- | ------------------------------------------------ | ---------------------- | --- | ---------------------- | ------------------------ | --- | ----------------------- |
|     | .tluserllarevoehtssessa |     |                                                  |                        |     | .tnemssessarofstcudorp |                          |     |                         |
.sledomlacitamehtam
.dessessaebyam
paG
,’dtA‘tahtdewohsMESfotluserehT sesehtopyhxis,oslA.IPAGotdetaler stluserehT.’nnIP‘foelorgnitaredom ehtdetaredom’nnIP‘tahtdehsilbatse krowemarflevonasedivorphcraeser elbairavfodesopmocsecitcarplaicos otelbisseccaeratahtseicnetepmoc otelbisseccanidnaslaudividniemos oteunevaeno,yltneuqesnoC.srehto ehtotssecca’sremusnocgnivorpmi mrofsnartotgnitpmettanahtrehtar timeotneessawmetsysnoitcudorp niahcylppuselbaniatsusehtfotfiorp emitdaelhtobfonoitcnufxevnocasi otlaicurcsignilleslennahctnereffid remotsucgnisaercnirofyrtsudniyna ,ksirnoitpursiddnalanoitarepomorf ygreneecuderrofseicilopdetseggus elbatutitsbusepyt-elgnishtiwledom
neewtebpihsnoitalerehterolpxeot tcnitsidsevlovnisnaejfoseirogetac foycneuqerfevitalerehtgnisaercni snaejdesurofgnippohsfoecitcarp nevorpsahydutsehT.tnemnrevog sedivorpmetsysdesoporpehttaht otenilnostcudorpriehtsesitrevda -itlumehtgnitcetorpnisehcaorppa krowten)CS(niahcylppusleufoib snoissimenobracdnanoitpmusnoc deredisnocsawnoitcudorptcudorp dna,ygolonhcetneergnignitsevni
,’buS‘,’dtA‘neewtebpihsnoitaler sihT.yltnacfiingis’IPAG‘dna,’CC‘ .’IPAG‘s’remusnocZnoitareneG forettamasemocebesuersnaej lacitylanaehtdewohsydutsehT latotehttahtevorphcihwstluser sA.emitdaelehtfoecnairavdna ,ycilopxat-dna-pacagnisopmiyb
|     |     |     |     |     | otgnipleh,noissimenobracssel ehtmorfseidisbusregralniatbo |     | dnalennahcdirbyhybstcudorp |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | -------------------------- | --- | --- |
ylevitisoperew’CC‘dna,’buS‘ .metsysnoitcudorplanoitidart riehtsllesreliatereht,dnamed evitceffetsomehtdenimreteD dna,noitatropsnartsallewsa noitcudorpelbixeflelbaniatsuS
|     | ehtgnitsetdetalumroferew | dna’CC‘dna,’rtA‘,’KE‘eht tnereffidesehtrofgnippohS |     |                         |     | ehtnahttfiorperom%67.8 |     |                     |     |
| --- | ------------------------ | -------------------------------------------------- | --- | ----------------------- | --- | ---------------------- | --- | ------------------- | --- |
|     |                          |                                                    |     | elbairavehtfoegatsyrevE |     |                        |     | .suomaferommehtekam |     |
dna,slairetam,sgninaem .sfeilebrosedutittarieht .stcudorprofgnisitrevda
sgnidnfiniaM
.tsoc)EBC(
|     |     |     |     | dezilitusawyciloplennahc-laudA | yllufasisihT.snoisicedlaireganam |     |     | rofledomlacitamehtamcitsahcotS |     |
| --- | --- | --- | --- | ------------------------------ | -------------------------------- | --- | --- | ------------------------------ | --- |
latottcaxenagnivigybyrotnevni hguorhtnoitcnuftfiorpdetcepxe
.seuqinhcetnoitazimitpocissalc
| gniledoMnoitauqElarutcurtS |     |     |     |     | ybderevocmetsysnoitcudorp .tnemtsevniygolonhcetneerg | -ni-pukcip-enilno-yubneewteb | dnah-nodna,redrokcab,erots |     |                           |
| -------------------------- | --- | --- | --- | --- | ---------------------------------------------------- | ---------------------------- | -------------------------- | --- | ------------------------- |
|                            |     |     |     |     | elbairavdellortnoc-noissime                          | noitalercitsiretcarahcatliuB | ehtfodaetsninoitcnuftfiorp |     | lacitamehtamedart-dna-paC |
elbatfiorptsomehtdnfiot
dnatnempolevedledom
|     |     | noissucsidpuorgsucoF |     |     |     |     |     | noitazimitpotsoclatot |     |
| --- | --- | -------------------- | --- | --- | --- | --- | --- | --------------------- | --- |
noitazimitpo
)s(dohteM
ecneuflniehtenimretedotdesoporP ,)KE(’egdelwonKlatnemnorivnE‘fo fostcurtsnocdna)CC(’ecnedfinoC )BPT(’roivaheBdennalPfoyroehT‘ krowemarfecitcarplaicosadetpodA egatnavdagnikat,snaejrofgnippohs rofsecnereferpriehtfosnoitanalpxe ,gnillesenilnoderedisnocydutsehT dnaemitdaelfotcapmiehtenimaxE
esahcrupotnoitnetni’sremusnoc elorllamsylevitalerayalpsfeileb gnisahcrupekilroivahebgninialpxe ehtnistludahtiwspuorgsucoffo rednumetsysnoitcudorpelbairav gnillesrofseiciloperots-ni-pukcip ylppusanotsocsnoissimenobrac -dna-pachguorhtnoissimenobraC denimretedsawmsinahcemedart
|     |                                                   | )IPAG(’stcudorPlerappAneerG‘ dnasedutittaremusnochcihwni | deliatedticileotmodgniKdetinU                                                   |                             |                             |                               |                           |               |               |
| --- | ------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------- | --------------------------- | ----------------------------- | ------------------------- | ------------- | ------------- |
|     | evitcejbuS‘,)dtA(”edutittAekil                    |                                                          |                                                                                 | afossenevitceffeehtdessessA | sawseiciloplortnocsnoissime | -enilno-yubdna,gnilleseniflfo |                           |               |               |
|     | no)chbP(’lortnoclaroivaheb                        |                                                          | sesucofydutsehT.snoisiced foecitcarpehtnoyllacfiiceps .snaejdesuro,delcycer,wen |                             |                             |                               |                           |               |               |
|     | remusnoC‘,)rtA(’msiurtlA‘ deviecreP‘dna)buS(’mroN |                                                          |                                                                                 |                             |                             |                               | .serotsliatermorfstcudorp |               |               |
|     |                                                   |                                                          |                                                                                 |                             |                             |                               |                           | .krowtenniahc | .dezimitpodna |
)s(evitcejbO
.devresbo
weiveRrofslanruoJdetsegguSreweiveR
)deunitnoc(1
)3202(.lateraK
.lateionhsiV
|     |     | .latereyoB |     | .laterakraS |     | .laterakraS |     | .laterakraS |     |
| --- | --- | ---------- | --- | ----------- | --- | ----------- | --- | ----------- | --- |
ecnerefeR
)4202(
| elbaT | )5202( | )5202( |     | )2202( |     | )3202( |     |     |     |
| ----- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | --- |
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 5

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
dluohsnoitazilitulautcadna,tesatad ecological footprint, and spread environmentally friendly beha-
teeeL(sremusnocgnomaroivaheb
,lacitiloprolaicos,latnemnorivne teysahsiht,revewoh—)0202.la ahtiwdessessaylhguorohtneeb viors. Lastly, the economic aspect pertains to financial structures
| ,oiranecsefil-laernoytivitceffE | sahcussniamodytilibaniatsuS | ebdluocstcepsacimonocedna |     |               |     |              |     |        |     |             |        |
| ------------------------------- | --------------------------- | ------------------------- | --- | ------------- | --- | ------------ | --- | ------ | --- | ----------- | ------ |
|                                 |                             |                           |     | and processes |     | that promote | the | growth | and | development | of the |
elbaniatsustceffaotdetisop
dnakrowemarfkramhcneb economy (Waheed et al. 2023). Studies that focus on economic
.lootlacitylanadecnavda
|     |     |     |     | sustainability | incorporate |     | understanding |     | ethical | financial | prac- |
| --- | --- | --- | --- | -------------- | ----------- | --- | ------------- | --- | ------- | --------- | ----- |
tices,settlingfinancialobligations,andmakingsociallyconscious
(Sedliačiková
|     | paGhcraeseR |     |     | investments |     |     | et  | al. 2020). |     |     |     |
| --- | ----------- | --- | --- | ----------- | --- | --- | --- | ---------- | --- | --- | --- |
.dessessaeb
|     |     |     |     | With     | the aforementioned |         |     | notions      | on the         | sustainability | aspect |
| --- | --- | --- | --- | -------- | ------------------ | ------- | --- | ------------ | -------------- | -------------- | ------ |
|     |     |     |     | and TPB, | thispaper          | aimedto |     | establishthe | Sustainability |                | Theory |
paG of Planned Behavior (STPB) to assess sustainable behavior
|     |     |     |     | determinants     | for | purchasing |             | apparel | made        | from    | plastic waste |
| --- | --- | --- | --- | ---------------- | --- | ---------- | ----------- | ------- | ----------- | ------- | ------------- |
|     |     |     |     | extending        | the | model      | and concept | from    | studies     | (German | et al.        |
|     |     |     |     | 2022a; Abusafieh |     | and        | Razem       | 2017;   | Abdel-Shafy | and     | Mansour       |
|     |     |     |     | 2018; Gansser    |     | and Reich  | 2023;       | Waheed  | et al.      | 2023;   | Sedliačiková  |
etal.2020).Inaddition,theobjectiveofthestudywastoassessif
thedevelopedmodelcouldbeestablishedinthefieldofconsumer
| gnomanoissimenobracdnadnamed nobracwohgnitneserp,niahcylppus | ytilibaniatsusroftnemssessacitsiloH | sahtubsrotcafemosfonoitanibmoc sisylanaevitatitnauqdnaevitatilauQ | eromesuotdetseggusevahseiduts emocrevodna,noitciderpfoycarucca |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                              |                                     | detaleR.enodneebteysahsrotcaf                                     | emoS.tnemssessalacitylanatnecer                                |     |     |     |     |     |     |     |     |
rehgihevah,sledomnoitacfiissalc behavior among clothing industries using a machine learning
| elbixeflrofsnoitacilpmidetaerC |     | aderedisnocylnoevahseiduts tub,deredisnocneebevahsloot | enihcamesuotdetseggusevah dliubplehotelbmesnegninrael .sisylanalacitsitatsetairavitlum |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | ------------------------------------------------------ | -------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
otderapmocelbaivsselsixat .tnemssessacitsilohllarevoon algorithm; similar to the studies of German et al. (2022a) on
|     | .noissimelaminimdellortnoc |     | dnalanoitidartfosnoitatimil |            |          |           |               |                |           |            |           |
| --- | -------------------------- | --- | --------------------------- | ---------- | -------- | --------- | ------------- | -------------- | --------- | ---------- | --------- |
|     |                            |     |                             | consumer   | behavior |           | among         | transportation |           | intention  | and       |
|     |                            |     |                             | Gumasing   | et al.   | (2023)    | on technology |                | intention | and        | adoption. |
|     |                            |     |                             | This study | aimed    | to answer | several       | research       |           | questions: |           |
sgnidnfiniaM 1. Can the STPB framework holistically assess sustainable
|     |         |     |     | behavior |        | determinants |     | for purchasing |     | apparel | made from |
| --- | ------- | --- | --- | -------- | ------ | ------------ | --- | -------------- | --- | ------- | --------- |
|     | ytlevoN |     |     | plastic  | waste? |              |     |                |     |         |           |
2. Howcanmachinelearningensemblebeemployedtocreate
classification
|     |     |     |     | a           |          | model | for       | behavioral     | analysis? |         |             |
| --- | --- | --- | --- | ----------- | -------- | ----- | --------- | -------------- | --------- | ------- | ----------- |
|     |     |     |     | 3. How      | accurate |       | could the | model          | test      | out the | dataset for |
|     |     |     |     | forecasting |          | and   | modeling  | sustainability |           | and     | behavioral  |
domains?
|     |     |     |     | 4. Whatimplications,boththeoreticaland |      |            |     |            |     | practical,couldbe |     |
| --- | --- | --- | --- | -------------------------------------- | ---- | ---------- | --- | ---------- | --- | ----------------- | --- |
|     |     |     |     | built                                  | from | the output | of  | the study? |     |                   |     |
snoitauqetsoclatotevitcepsorP
yrotnevnidnah-nohtiwnoitaler 5. How can the study be extended based on the output and
| nideyolpmesawnoitazimitpo |                         | :elbmesnEgninraeLenihcaM dnarefiissalCtseroFmodnaR |     |              |     |     |     |     |     |     |     |
| ------------------------- | ----------------------- | -------------------------------------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|                           | —looTlacitylanAdecnavdA |                                                    |     | limitations? |     |     |     |     |     |     |     |
krowteNlarueNlaicfiitrA
|     |     |     |     | As a       | contribution, |     | this study | could | be beneficial  |     | to business |
| --- | --- | --- | --- | ---------- | ------------- | --- | ---------- | ----- | -------------- | --- | ----------- |
|     |     |     |     | industries | considering   |     | that this  | can   | give knowledge |     | on how the  |
.sredrokcabdna customers’ purchase intention can impact sustainability aspects
|     |     |     |     | among apparel. |     | The | results | could provide | implications |     | for sus- |
| --- | --- | --- | --- | -------------- | --- | --- | ------- | ------------- | ------------ | --- | -------- |
)s(dohteM
sdohteM
|     |     |     |     | tainable | practices | among | apparel | industries. |     | This study | can also |
| --- | --- | --- | --- | -------- | --------- | ----- | ------- | ----------- | --- | ---------- | -------- |
findings
|     |     |     |     | be advantageous |     | for | the government |     | as its |     | can aid in |
| --- | --- | --- | --- | --------------- | --- | --- | -------------- | --- | ------ | --- | ---------- |
recognizingcustomerneedsandpreferences,aswellasencourage
sustainableproductionandconsumptiontocreateprogramsand
|     |     |     |     | policies    | for sustainable |                 | apparel  | that       | are       | more effective. | The         |
| --- | --- | --- | --- | ----------- | --------------- | --------------- | -------- | ---------- | --------- | --------------- | ----------- |
|     |     |     |     | findings    | can contribute  |                 | to the   | community, |           | considering     | that this   |
|     |     |     |     | can promote |                 | environmentally |          | friendly   | behaviors |                 | in order to |
|     |     |     |     | minimize    | pollution       | and             | preserve | natural    |           | resources.      | Customer    |
stnanimretedroivahebelbaniatsus morfedamlerappagnisahcruprof foyroehtehtmorfledomroivaheb awareness and knowledge of sustainable fashion could be
fotnemssessanoissimenobraC
latnemnorivne-orpdehsilbatse ehtgnitset—roivahebdennalp dennalpfoyroehtytilibaniatsus increased, which might encourage them to buy more sustainable
ssessaotdemiaydutssihT ehtgnidnetxeetsawcitsalp apparel. Lastly, this study can benefit future generations by
.niahcylppuselbaniatsus
|              |     |     |     | identifying | possible       | constraints |           | to sustainable |          | fashion | using the  |
| ------------ | --- | --- | --- | ----------- | -------------- | ----------- | --------- | -------------- | -------- | ------- | ---------- |
|              |     |     |     | proposed    | theory,        | which       | could     | be utilized    | to       | inform  | the devel- |
|              |     |     |     | opment      | of strategies  |             | that will | boost          | consumer | demand  | for and    |
| )s(evitcejbO |     |     |     | acceptance  | of sustainable |             | behavior  | shortly.       |          |         |            |
evitcejbO
.roivaheb
|     |     |     |     | Literature | review      | and    | hypotheses     |        |              |          |               |
| --- | --- | --- | --- | ---------- | ----------- | ------ | -------------- | ------ | ------------ | -------- | ------------- |
|     |     |     |     | Research   | framework   |        | and hypothesis |        | build-up.    | Figure   | 3 illus-      |
|     |     |     |     | trates the | established |        | STPB           | model, | the          | research | framework     |
|     |     |     |     | employed   | in this     | study, | to determine   |        | the purchase |          | intentions of |
)deunitnoc(1
|     |     |     |     | Filipino | customers | while | purchasing |     | clothing | made | of recycled |
| --- | --- | --- | --- | -------- | --------- | ----- | ---------- | --- | -------- | ---- | ----------- |
plastic.TheSTPBframeworkinthisstudyhasbeenconsideredas
)5202(rakraS anextensionofthepro-environmentalplannedbehavior(PEPB)
dnaahdirM ydutssihT from a sustainable transportation perspective (German et al.
ecnerefeR
|     |     |     |     | 2022a; Ong | et  | al. 2023). | It is | an expanded |     | version | of the PEPB |
| --- | --- | --- | --- | ---------- | --- | ---------- | ----- | ----------- | --- | ------- | ----------- |
elbaT
|     |     |     |     | from TPB | (Ajzen | 1991), |          | integrating | fully | all      | sustainability |
| --- | --- | --- | --- | -------- | ------ | ------ | -------- | ----------- | ----- | -------- | -------------- |
|     |     |     |     | domains. | The    | model  | included |             | eight | factors: | Perceived      |
6 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Fig.3Theoreticalframework.
Environmental Concern (PENC), Perceived Authority Support more when the real value of a product exceeds their perceived
(PAS), Subjective Norms (SN), Attitude (AT), Perceived Beha- value. However, according to the study of Saricam and Okur
vioral Control (PBC), Customer Perceived Value (CPV), Beha- (2018), some research efforts aimed to establish the extent to
vioral Intention (BI)—PEPB (German et al. 2022a), and the which customers would be willing to pay an extra cost for sus-
additionalPerceivedEconomicConcern(PECC).Asexplainedin tainable fashion products. Moreover, consumers would be ready
thestudy of Ong et al.(2023), PECC isan importantvariable to tospendmoreonclothingmanufacturedfromorganicmaterials.
consider for full sustainability behavioral assessment. The suc- ThestudyconductedbyFeriolietal.(2022)andParkandLin
ceeding section provides an outlook of the hypothesis build-up (2020)alsoindicatedthatcustomersexhibitagreaterwillingness
since only PECC is a new addition. to pay elevated prices for environmentally friendly and sustain-
able clothing products. To which, a strong positive correlation
Perceivedeconomicconcern(PECC)affectingbehavioraldomains. wasfoundbetweencustomers’willingnesstospendmore(PECC)
PECCcanbeconsideredasagaugeofacustomer’sinclinationto on sustainable clothing and AT for sustainable apparel (Nam
allocate additional funds towards sustainable products (Saricam etal.2017).Thestudyalsomentionedthatcustomerswithgreater
andOkur2018).Variousstudiesmentionedthatcustomersassert environmentalconcernstendtoshowahigherinclinationtoward
theirreadinesstobuysustainableclothing,evenatahigherprice. purchasing sustainable clothing products. A study conducted by
However,thereareuncertaintiesoverwhethertheydoso,making Rohetal.(2022)showedthatPECChasapositivevalueonboth
their purchasing behavior contradict their claims (Gomes de SNandPBC,whereintheresearchersdiscoveredthattheperiods
Oliveira et al. 2022). Another study also mentioned that con- when organic products had the most significant development
sumers who are concerned with environmental issues may not were those in which people were considerably more inclined to
always choose to purchase eco-friendly or sustainable products. change their behavior to promote sustainability. However, Ong
Thosecustomerswhoclaimtobeconcernedwithenvironmental et al. (2023) expressed that when too expensive technology is
issuesmightstillnotengageinpro-environmentalbehaviorupon being sold, PECC will not be significant among buying behavior
purchasingproductssincesustainable productscomeatahigher duetopriceandgeneraleconomicconcerns.Itwasexplainedthat
cost compared to conventional alternatives (Dangelico et al. the more benefit and cost-saving a technology is, the more
2022), especially evident in the Philippines (Ong et al. 2023). It inclined people will be to purchase. In terms of clothing and
was mentioned that consumers are frequently willing to invest apparel, the following were hypothesized:
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 7

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
H1. Perceived Economic Concern has a significant impact with expectedobstacles,influencedbyone’sself-beliefandjudgmentof
Subjective Norm. their capability (Xu et al. 2022). PBC can be utilized to forecast
H2. Perceived Economic Concern has a direct significant behavior in a straightforward manner as well as indirectly influ-
relationship with Attitude. ence behavior through intentions relating to sustainability beha-
H3. Perceived Economic Concern has a positive relationship viors (Ong et al. 2023; Soorani and Ahmadvand 2019). In the
with Perceived Behavioral Control. study of Saricam and Okur (2018), both SN and AT have a sig-
nificant direct relationship with CPV. Furthermore, the study of
Perceived Environmental Concern (PENC) affecting behavioral Savari and Gharechaee (2020), Qi and Ploeger (2019), and Lin
domains. PENC can be viewed as a measurement of how each et al. (2017) mentioned that TPB domains significantly had a
person perceives the effects on the environment (German et al. substantialeffectoncustomers’purchasingintentionsandplayed
2022a; Ong et al. 2023). According to Bickart and Ruth (2012), a significantrolein influencing them.Behavioraldomainsin the
thedegreetowhichaconsumercaresabouttheenvironmentisa PhilippinecontexthavebeenestablishedbyGermanetal.(2022a)
significant personal characteristic because it is linked to their to affect CPV. Therefore, this study identified the following
knowledge and motivation regarding environmental matters. hypotheses:
Studies have shown that consumers’ intentions upon purchasing H10. Subjective Norm has a positive relationship to Customer
recycled and upcycled apparel products are positively impacted Perceived Value.
by environmental concerns (Park and Lin 2020). In a study H11. Attitude has a direct significant relationship to Customer
conducted by Lin et al. (2017), the researchers discovered that Perceived Value.
PENChasapositivevalueonbothSNandPBC.Incontrast,there H12.PerceivedBehavioralControlhasapositiverelationshipto
is little association between PENC and AT in environmental Customer Perceived Value.
impactassessment(EIA). Thiscorrelationshowsthatcustomers’
PENCwasadverselyaffectedwhentheywererequiredtoactively Customerperceivedvalue(CPV)affectingbehavioralintentions.In
engage in an environmental activity. In the Philippines, it was this study, CPV illustratesthe customer’s holistic evaluation of a
established that the community is now more inclined to pro- product’sutility,determinedbytheirperceptionofwhathasbeen
environmentalbehavior,leadingtosustainableoptions(Ongetal. providedandwhattheyhavereceived(Uziretal.2021).Itisthe
2023). Therefore, this study identified the following hypotheses: outcomeofhowconsumersfeelpriorto,throughout,andaftera
H4. Perceived Environmental Concern has a positive relation- purchase has been made (Al-Mashraie et al. 2020; Savari and
ship to Subjective Norm. Gharechaee2020).AstudybyDangelicoetal.(2022)discovered
H5. Perceived Environmental Concern has a positive relation- that CPV is the best indicator of consumers’ intentions to pur-
ship with Attitude. chase sustainable apparel and their willingness to spend higher
H6. Perceived Environmental Concern has a positive relation- pricesforit,nomatterwhethereco-materialisexplicitlyutilized.
ship with Perceived Behavioral Control. Thisshowsthatinthegeneralframeworkofsustainableclothing,
elevated CPV resulting from a product made with a particular
Perceived authority support (PAS) affecting behavioral domains. eco-friendly material enhances customers’ inclination to buy the
PAS relates to an individual’s comprehension of the resources, product, even at a higher price. The study findings of Dangelico
laws, regulations, and potentially additional processes provided et al. (2022) aligned with findings from prior research on sus-
byagovernmentorauthoritativeentitytosupportindividualsin tainable clothing products (Chi et al. 2021). Numerous research
adoptingaspecificbehavior(Nadlifatinetal.2016).Accordingto investigations have demonstrated that CPV exerts a significant
the study of Lin et al. (2017), PAS positively influences the and favorable impact on BI (Jalil et al. 2016; Liu et al. 2021).
domains of TPB among citizens’ Desire and readiness to engage Therefore, this study hypothesized that:
in an EIA. Considering the viewpoint of AT, these regulations H13. Customer Perceived Value has a positive relationship to
offer regular opportunities for engagement and a variety of Behavioral Intention.
communication channels to enhance the positive sentiments of
citizens. From the SN perspective, the regulations serve as a
means to foster cooperation between the project developer and Machine learning algorithm as analytical tool. Recent
the broader community. From the PBC perspective, the regula- advancementsinartificialintelligence(AI),bigdata,andmachine
tions offer residents the chance to participate in the EIA process learning brought newly adaptedmethodologiesfor analysis. Ong
under the most convenient conditions (Ong et al. 2023). There- etal.(2023)explainedthattheapplicationofmachinelearningas
fore, this study identified the following hypotheses: an analysis tool in behavioral intention among smart transpor-
H7. Perceived Authority Support has a positive relationship to tation provided better output compared to the multivariate ana-
Subjective Norm. lysis counterpart study. This was because several path analyses
H8. Perceived Authority Support has a positive relationship to werepresentonthelargemodel,creatingatotalof18hypotheses
Attitude. intheir study.Inaccordance,thestudyofGermanetal. (2022a)
H9.PerceivedAuthoritySupporthasapositiverelationshipwith thatconsideredPEPBpresentedbetteraccuracyforthenonlinear
Perceived Behavioral Control. relationship framework established with machine learning tech-
nique analyses. From their study, a total of 20 hypotheses were
TPB domains affecting customer perceived value. AT pertains to consideredintheirstudy.Comparedtotheirotherstudyutilizing
the evaluation of an individual concerning the behavior in higher-order structural equation modeling (SEM) analyses, both
question, ranging from a positive assessment to a negative one generated similar output and could prove how machine learning
(SooraniandAhmadvand2019).Ontheotherhand,SNrefersto as another tool could be considered.
the perception of societal influence, either encouraging partici- When dealing with multivariate analyses, studies such as that
pation in the behavior or discouraging it (Rausch and Kopplin of Fan et al. (2016) explained that the larger the framework, the
2021). In other words,SN consists of one’s opinions on whether more path is needed to assess the target output. This usually
close friends or family members should participate in the beha- resultsinloweraccuracyofrelationshipassessmentduetoerrors
vior.PBCrelatestotheperceptionofhoweasyorchallengingitis in the multiple paths needed to be met. Woody (2011) with the
to perform the activity, encompassing past experiences and same explanation posited that farther variables on the target
8 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
outputmayalsoresultinaninsignificantrelationship.Towhich, itevery6–9months(23%).Lastly,asmallportionofparticipants
present studies such as that of Jamshidi et al. (2022) and Al- make sustainable apparel purchases in 10–12 month intervals
Mashraieetal.(2020)expressedtheadvantagesofusingmachine (19.2%).
learning techniques in analyzing nonlinear relationship frame-
works,whicharemostlycomplexinnature.Itwasindicatedthat
these hybrid tools could present better output, higher accuracy, Questionnaire. The questionnaire consisted of two (2) parts:
and better predictive power. In terms of analyzing behavioral demographic information about potential respondents and
intention among technology adoption, it was presented that determinantsoftheSTPBmodel,adaptedfromliteraturereviews.
machine learning had higher accuracy (Al-Mashraie et al. 2020; Supplementary materials present the STPB questionnaire,
Gumasing et al. 2023) and provided a better significance level employing a five-point Likert Scale ranging from 1 (Strongly
with classification techniques like neural networks and random Disagree) to 5 (Strongly Agree) to evaluate the various determi-
forest classifier (RFC; Gumasing et al. 2023). nants that influence a user’s behavior when it comes to pur-
chasing apparel made from recycled plastic materials. The
adapted questionnaire for buildup is presented in the
Methodology Supplementary File.
Participants. This study assessed customers’ intentions and
behaviors regarding sustainable apparel. A total of 500 valid
responses were collected through an online survey using a con- Machinelearningalgorithm(MLA).Inthisresearch,amachine
veniencesamplingapproach.Thesamplingapproachwasutilized learning algorithm ensemble (MLE) was employed, including
to disseminate the online survey through various social net- artificial neural network (ANN) and RFC, which were employed
working sites and pages in order to procure a wide range of to properly assess the latent variables at once. According to the
respondents, since convenience sampling is a non-probability studybyOngetal.(2022),itwasmentionedthatusingamachine
sampling method where participants voluntarily choose to par- learning ensemble was much more efficient in analyzing the
ticipate after being informed about the study by the researcher aspects influencing human behavior concerning how people uti-
(Stratton 2021). The first two pages/section of the questionnaire lizetechnologycomparedtotraditionalandmultivariateanalysis
contained a short introduction as well as a reference to theData such as SEM. From their study regarding nuclear power plant
Privacy Act and approval of the Ethics Committee (FM-RC-22- reopening adoption among consumers, the SEM analysis proved
01-01, approved on March 20, 2023). Followed by the demo- highersignificanceontheclosevariablerelationshiponthetarget
graphic profiling of the respondents. Lastly, the STPB compo- object.UtilizingMLE,theywereabletoprovideinsightintohow
nents were then displayed after the demographic profile was (1)thebasicdecisiontreeshowedlowaccuracyratescomparedto
completed.PresentedinTable2aretheparticipantdemographic RFC, and (2) that farther variables were more significant com-
characteristics, collected alongside the measured items. paredtothoseclosetothetargetoutput.Theywereabletoprove
According to the collected data, it was observed that the that classification techniques such as RFC provided better accu-
majority of participants were women (69.2%), while males made racy output since it generates the most probable model every
up the remaining portion (30.8%). Regarding the distribution of iteration as compared to the random generation when the basic
age groups, individuals aged 18 to 25 comprised the largest decision tree is used. Their study also justified the explanation
segment,makingup(55.4%)ofthesample,individuals below18 presentedbyFanetal.(2016)andWoody(2011)—thefartherthe
comprised(14.4%),andthoseaged26to35yearsoldconstituted variable, the little effect it has on the target output significance
around (13%), while the remaining participants were from older level. In addition, SEM is limited to smaller frameworks or
age groups. In relation to marital status, a significant proportion smaller path analyses for better predictive power.
identified as single (75.8%), followed by married individuals at a Moreover, a comparison of different classification techniques
rateof (20.2%),andboth separatedand widowed(2%).Interms wasemployedbyOngetal.(2024).Theywereabletopresentthat
of residential areas, the majority of respondents, constituting RFC and ANN outperformed other classification modeling
(80.6%), reside in urban areas, while (19.4%) hail from rural techniques. For example, there was a significant difference
regions Regarding employment status, the majority consists of betweenXGBoostandLightGBMcomparedtootheralgorithms.
students (59.2%), followed by employed individuals (31%); The accuracy rate obtained was lower, with higher mean square
unemployed individuals make up a smaller percentage at (5%), errors. This delineates that there needs further improvement on
while self-employed/business owners account for (4.8%). As for other classification techniques before it could be generalized for
educationallevel,thehighestproportionattendedcollege(40.6%), use in behavioral studies. It could be deduced that RFC
closely followed by those who attended high school/senior high overpoweredbasicdecisiontrees,XGBoost,andLightGBM,even
school (37.4%). A significant portion has completed college or CATBoost, among others. Studies have also proven that these
obtained graduate degrees (20.4%); lastly, only a small fraction classificationtechniquesusingMLEmayalsooverpowereventhe
hasattendedgradeschool,withanoccurrencerateofjust(1.6%). advanced multivariate tools like SEM and multiple regression
For the household size, the majority of participants have analyses (Öztürk and Başar 2022).
households consisting of 3–4 people (45.6%), followed by 5–6 It could be seen among recent studies that little to no studies
people (26.4%), more than six people (15%), and finally, those have used the MLE to evaluate the factors affecting consumers’
with households of 1–2 people (13%). The majority of behavioral intention uponbuying sustainable apparel orsustain-
participants fall below Php 10,000 (30.8%). Additionally, 23.4% ablebehavioringeneral.Mostjustfocusedontechnologyandits
fall within Php 10,001–20,000, and 16.2% fall within Php acceptance (Ong et al. 2022), health behavior (Gumasing et al.
20,001–30,000.ThosewithanincomeabovePhp50,000account 2023),transportation(Germanetal.2022a;Ongetal.2023),and
for approximately 13. 8%, 10.2% had an income between 30,001 adoption(Milanietal.2020)tonameafew.Additionally,studies
and 40,000, and 5.6% were between Php 30,001–40,000 and showthatincomparisontoSEM(Germanetal.2022a;Ongetal.
between Php 40,001–50,000, respectively. Lastly, for the fre- 2022;Ongetal.2023),machinelearningalgorithmscanproduce
quency of purchasing sustainable apparel, (33%) buy sustainable predictions that are more accurate and models that work more
apparel every 1–3 months. Additionally, a significant percentage effectively (Bossi et al. 2022). Furthermore, both approaches are
purchaseitevery3–5months(24.8%),followedbythosewhobuy capable of handling huge numbers of variables and datasets for
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 9

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
profile. chargeofhighlightingitspositivefeaturesanddefiningitslimits.
Table2 Respondentsdemographic
|                 |     |          |     |     |     | Despite     | this, numerous |                 | studies | have raised | questions |               | about the |
| --------------- | --- | -------- | --- | --- | --- | ----------- | -------------- | --------------- | ------- | ----------- | --------- | ------------- | --------- |
|                 |     |          |     |     |     | efficacy    | of machine     | learning        |         | when        | used      | independently | for       |
| Characteristics |     | Category |     | N   | %   |             |                |                 |         |             |           |               |           |
|                 |     |          |     |     |     | measurement |                | and prediction, |         | or when     | combined  | with          | other     |
Gender Male 154 30.8% statistical and multivariate techniques in hybrid approaches.
|     |     | Female          |     | 346 | 69.2% |        |        |            |        |         |     |       |             |
| --- | --- | --------------- | --- | --- | ----- | ------ | ------ | ---------- | ------ | ------- | --- | ----- | ----------- |
|     |     | Total           |     | 500 | 100%  |        |        | classifier |        |         |     |       |             |
|     |     |                 |     |     |       | Random | forest |            | (RFC). | The RFC | is  | among | the many    |
| Age |     | Below18yearsold |     | 72  | 14.4% |        |        |            |        |         |     |       | classifica- |
18–25yearsold machine learning algorithms commonly employed for
|     |     |     |     | 277 | 55.4% |     |     | classification |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | -------------- | --- | --- | --- | --- | --- |
26–35yearsold tion tasks. It is a model which takes into account a
65 13%
36–45yearsold 45 9% straightforwardalgorithmfeaturinghighpredictionaccuracy.The
efficiency
46–55yearsold 20 4% study of Chen et al. (2019) mentioned the of RFC in
56–65yearsold 14 2.8% creatingsuperiorclassificationmodelscomparedtoastandardor
66yearsoldandabove 7 1.4% basic decision tree, as RFC consistently generates the most
Total 500 100% accurate tree every iteration. According to related studies (Ger-
Status Single 379 75.8% manetal.2022a;Gumasingetal.2023;Ongetal.2022;Ongetal.
Married 101 20.2% 2023), RFC could be employed for the categorization of human
|     |     | Separated |     | 10  | 2%  |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factorsthataffecthowwellanapplicationisusedandadaptedor
|                 |     | Widowed |     | 10  | 2%    |                |     |           |           |       |          |           |          |
| --------------- | --- | ------- | --- | --- | ----- | -------------- | --- | --------- | --------- | ----- | -------- | --------- | -------- |
|                 |     |         |     |     |       | how consumers  |     | behave.   | It was    | shown | that RFC | is among  | the      |
|                 |     | Total   |     | 500 | 100%  |                |     |           |           |       |          |           | peoples’ |
|                 |     |         |     |     |       | most effective |     | tools for | analyzing | the   | factors  | affecting |          |
| Areaofresidence |     | Urban   |     | 403 | 80.6% |                |     |           |           |       |          |           |          |
decisions.
|     |     | Rural |     | 97  | 19.4% |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Adaptedfromtheaforementionedstudies,severalfactorswere
|            |     | Total      |     | 500 | 100%  |           |          |            |           |             |             |           |          |
| ---------- | --- | ---------- | --- | --- | ----- | --------- | -------- | ---------- | --------- | ----------- | ----------- | --------- | -------- |
|            |     |            |     |     |       | optimized | in order | to         | construct | the optimal |             | tree when | RFC is   |
| Employment |     | Student    |     | 296 | 59.2% |           |          |            |           |             |             |           |          |
|            |     |            |     |     |       | employed  | within   | the Python |           | Integrated  | Development |           | Environ- |
|            |     | Unemployed |     | 25  | 5%    |           |          |            |           |             |             |           |          |
Employed 155 31% ment, Spyderv5.0. Similarly, thesklearn package was integrated.
Self-Employed/ 24 4.8% To which, tree depths between 5 and 7 were taken into
BusinessOwner consideration, as well as criterion factors such as entropy or
Total 500 100% Ginicriteria,training-testingratiosspanningfrom60:40to90:10,
| Educationlevel |     | Finishedcollegeor |     | 102 | 20.4% |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
andsplitterchoicesincludingrandomorbest.Eachcombination
graduatedegree
wasoneofeveryparameterbetweentreedepth,criterion,splitter,
|     |     | Attendedcollege     |     | 203 | 40.6% |             |      |            |               |          |              |         |         |
| --- | --- | ------------------- | --- | --- | ----- | ----------- | ---- | ---------- | ------------- | -------- | ------------ | ------- | ------- |
|     |     |                     |     |     |       | and ratios. | This | study      | has therefore |          | analyzed     | a total | of 4800 |
|     |     | Attendedhighschool/ |     | 187 | 37.4% |             |      |            |               |          |              |         |         |
|     |     |                     |     |     |       | iterations  | upon | conducting | 100           | runs per | combination. |         |         |
seniorhighschool
|     |     | Attendedgradeschool |     | 8   | 1.6% |            |        |         |        |     |          |        |           |
| --- | --- | ------------------- | --- | --- | ---- | ---------- | ------ | ------- | ------ | --- | -------- | ------ | --------- |
|     |     |                     |     |     |      | Artificial | neural | network | (ANN). | ANN | contains | a more | intricate |
|     |     | Total               |     | 500 | 100% |            |        |         |        |     |          |        |           |
1–2people computation and algorithm in contrast with other MLAs. ANN
| Householdsize |     |     |     | 65  | 13% |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3–4people comprises neurons and layers that are connected by arcs, which
228 45.6%
5–6people convert input into output by means of an activation function
132 26.4%
|     |     |              |     |     |     | (Abolghasemi |     | et al. 2020). | ANNs | can | analyze | nonlinear | models |
| --- | --- | ------------ | --- | --- | --- | ------------ | --- | ------------- | ---- | --- | ------- | --------- | ------ |
|     |     | Above6people |     | 75  | 15% |              |     |               |      |     |         |           |        |
Total 500 100% andmaygivemorerealisticanswerstoissuesthatariseinreallife,
| TotalMonthlyNetIncome/ |     | Lessthan10,000 |     | 154 | 30.8% |             |          |               |               |                |      |         |          |
| ---------------------- | --- | -------------- | --- | --- | ----- | ----------- | -------- | ------------- | ------------- | -------------- | ---- | ------- | -------- |
|                        |     |                |     |     |       | and it      | is also  | capable       | of generating | predictions,   |      | which   | are fre- |
| Allowance              |     | 10,001–20,000  |     | 177 | 23.4% |             |          |               |               |                |      |         |          |
|                        |     |                |     |     |       | quently     | utilized | in prediction |               | areas since    | they | produce | more     |
|                        |     | 20,001–30,000  |     | 81  | 16.2% | significant |          |               |               |                |      |         |          |
|                        |     |                |     |     |       |             | outcomes | compared      |               | to traditional |      | methods | (Güven   |
30,001–40,000 51 10.2% andŞimşir,2020).AccordingtoJamshidietal.(2022)andAlam
40,001–50,000 28 5.6% etal.(2021),ANNscanbeaneffectiveclassificationapproachfor
|                          |     | Above50,000     |     | 69  | 13.8% |           |               |           |           |               |               |          |           |
| ------------------------ | --- | --------------- | --- | --- | ----- | --------- | ------------- | --------- | --------- | ------------- | ------------- | -------- | --------- |
|                          |     |                 |     |     |       | examining | factors       | that      | have      | a substantial | impact        | on       | human     |
|                          |     | Total           |     | 500 | 100%  |           |               |           |           |               |               |          |           |
|                          |     |                 |     |     |       | behavior. | Most          | research  | endeavors | typically     |               | commence | with      |
| Frequencyofbuying        |     | Atleastevery1–3 |     | 165 | 33%   |           |               |           |           |               |               |          |           |
|                          |     |                 |     |     |       | ANNs      | as a starting | point     | before    | delving       | into          | other    | forms of  |
| apparelsmadefrom         |     | months          |     |     |       |           |               |           |           |               |               |          |           |
|                          |     |                 |     |     |       | neural    | networks      | like Deep | Learning. | It            | was mentioned |          | that deep |
| recycledplasticmaterials |     | 3–5months       |     | 124 | 24.8% |           |               |           |           |               |               |          |           |
6–9months learning might be taken into consideration if the accuracy and
155 23%
10–12months complexitycapacityofANNprovidesalowoutput.Nevertheless,
96 19.2%
whensufficientpredictivepowerisattained,ANNisadequate.In
|     |     | Total |     | 500 | 100% |          |                |     |         |        |          |              |     |
| --- | --- | ----- | --- | --- | ---- | -------- | -------------- | --- | ------- | ------ | -------- | ------------ | --- |
|     |     |       |     |     |      | contrast | to complexity, |     | general | neural | networks | are regarded | as  |
advancedalgorithmsalready(Germanetal.2022a;Jamshidietal.
| the development | and | evaluation | of complicated |     | theories | 2022). |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | -------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
influencing
(Wendorf 2002). In order to categorize elements human behavior,
Various kinds of machine learning algorithms exist, with ANN is currently used in combination or hybrid with SEM
classification tools being commonly utilized for recognizing (Rehman et al. 2022). Research has shown that the intricate
patterns. A study conducted by Ong et al. (2022) stated how computationswithinthistypeofmachinelearningalgorithmcan
MLAslikeRFC,aswellasANN,havebecomewidelyrecognized yield more precise results, surpassing the capabilities of SEM,
in the field of human factors for evaluating human behavior. which attempts to simulate the transmission of messages among
However,astudyconductedbyJamshidietal.(2020)emphasized neurons in the brain (Al-Mashraie et al. 2020). In a study by
that differences of opinion may arise regarding the utilization of Alametal.(2021)aSEM-ANNhybridwastakenintoaccountto
| artificial |     |     |     |     |     |     |     |     | influencing | users’ |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --- | --- |
intelligence and machine learning depending on how ascertain the variables perceptions of the
they are applied as their utilization heavily relies on input from usefulness of a mental health application. It has been demon-
users, individual behavior, and interaction among human roles. strated that the outcomes of ANN could accurately anticipate
elementsinfluencinghumanbehavior.Furthermore,Kalinićetal.
Tothis,theyrespondedbysayingthatdatascientistsareincharge
ofthecodeandthatpeoplewhowritethealgorithmshouldbein (2021) employed ANN to assess customer happiness. They
10 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
showed how this kind of MLA can identify components helpcompanies,government,andeventhesociety.Thus,inorder
effectively even in the face of dataset noise and can emphasize toenhancethecompetitiveedgeofmarketers,theconceptof7ps
crucial variables even when nonlinear connections are present. may be more suitable when studying sustainable apparel from a
To create the best model, the ANN parameters were also wider perspective.
optimizedbyusingidenticaldatapre-processingmethodsasRFC
withaparametersettingliketrainingandtestingratios.Similarly,
Results
studiesbyKalinićetal.(2021),Lietal.(2022),andJangandXing
Random forest classifier (RFC) results. The RFC output was
(2020) mentioned that they explore various methods for
consideredwiththeoptimumparametersofginiandbestat90:10
activatingthehiddenlayer(tanh, relu,andsoftmax), and output
testing and training ratio. With a 92% accuracy rate, this pre-
layer(softmax,sigmoid,swish).Inaddition,studiesbyYousefza- sentedasignificantdifferenceuponsubjectingtheresultsthrough
dehetal.(2021),Jenaetal.(2020),andEckleandSchmidt-Hieber
analysis of variance. The summarized output is presented in
(2019)alsomentionedthattheoptimizationprocessalsoinvolved
Table 3, which is considered depth 6.
considerationsofoptimizerssuchasAdam,RMSProp,andSGD.
Figure 4 represents the optimum tree with RFC. It could be
I S c n o p n y t d j h u e i n r s ct s v i t 5 o u . n 0 d — y, w P t i y h th t e ho A T n N en I N n so te a r g l fl g r o o a w r te i , t d hm a D n e d w ve a l t s o h p e im m p K e l n e e t r m a E s en n t v p e i a d r c o k n u a m s g in e e g nt w th i a n e s d c le u e s d s s t u o t c h m e a d e n r t s o h ’ r a p t e u t q h r u c e a h l p a a s to e re − n in t 0 te n .2 n o 4 t d i 8 o e n a id s s e a w nt d h i e e fi t n e e d r p m C u i P r n c V i h n a g ( s X i f n 1 a ) g ct w o a i r p th p in a a fl re u v l a e l n m u c e a in d o g e f
employed.
from plastic. Satisfying the parent node would involve consider-
Furthermore, the class was set up to encompass 5 indicators
thatmirroredthedataset’snormaldistribution,aligningwiththe ing the Subjective Norm (X 3 ) with values less than or equal to
2.261.Inaddition,meetingthisrequirementwouldalsoconsider
5-point Likert Scale survey responses. In this study, the
Perceived Economic Concern (X ), X , and Attitude (X ),
parameters were derived from an analysis of various literature 4 3 2
ultimately resulting in an increased likelihood of customers
sourcesandtheircombinations.Atotalof27,000iterationswere
intendingtopurchaseapparelmadefromplastic.However,ifX
carried out over 150 epochs, involving 10 runs for every 1
did not meet the expectations, both PBC (X ) and X would be
combination of three activation functions for the hidden layer, taken into account. This would result in sig 0 nificantly 1 increased
threeactivationfunctionsfortheoutputlayer,andthreedifferent
purchasing intentions among customers buying plastic-made
optimizers. This encompassed every conceivable combination,
apparel.
starting from 10 nodes and gradually increasing until reaching
Conversely,iftheparentnodeisnotmet,itwillassessX with
100 nodes within the hidden layer. 0
values less than or equal to 1.081. Meeting this requirement
Datapre-processingandoptimization.Thecoefficientwasgivena wouldinvolveconsideringX 4 ,X 1 ,X 2 ,andX 4 leadingtoveryhigh
purchasing intentions for apparel made from plastic. If this
threshold of 0.20, and a 0.05 p-value was necessary for accep-
t t h an re c s e h . o I l t d w d a i s d s n ee o n t p th re a s t en an t y m c u o c r h re s la ig ti n o i n fic c a o n e c f e fic a i n en d t w b o el u o l w d d th is e ru s p e t t r c e o s n u d lt i i t n io g n in wa s s ig n n o ifi t c m an e t t l , y it el w ev o a u t l e d d t p ak u e rc i h n a t s o e a i c n c t o en un t. t I X f 1 th a e nd ch X il 3 d ,
node did not meet the criteria, it would consider X and X ,
the analysis (Ong et al. 2023). Therefore, the data cleaning pro- 3 4
resulting in a high level of purchase intent.
cessinthisstudythroughthefeatureselectionmethodconsidered
Therefore, according to the results, PECC (X ) is the most
correlation analysis. To which the items were analyzed on the importantvariablethatsignificantlyinfluencedpeo 4 ple’sAT(X ),
rescaled target output, behavioral intention. All items were 2
deemed significant underwent data aggregation. i S m N p ( li X es 3 ), th an at d C PB PV C ( ( X X 0 ) ) to is h a ave hi h gh ig l h y p s u ig r n c i h fi a c s a in n g t i f n a t c e t n or tio a n ff s e . c T ti h n i g s
Following related studies, a 60% accuracy threshold was 1
considered for this study to employ significance on the relation- purchasingintentionswhenitcomestopurchasingapparelmade
from plastic. In order to establish a distinct categorization of
ship (German et al. 2022a). The higher accuracy rate induced
better classification modeling for predicting factors affecting hidden factors that impact behavioral intentions, the RFC
requires supplementary assistance from other machine learning
humanfactorsandconsumerbehavior.TheTaylorDiagramwas
algorithms due to the diverse range of elements that still exist.
thenutilizedinthisstudytocompareandassesstheacceptability
Chen et al. (2019) adopted various approaches in addition to
of accuracy rates among MLEs used in the study. Gholami et al.
incorporating outcomes from the RFC in identifying pertinent
(2020)conductedastudythatdemonstratedtheuseoftheTaylor
latent variables.
Diagram in evaluating model performance through its accuracy,
standard deviation, and correlation. In the study conducted, it
was determined that a Root Mean Square Error (RMSE) value Artificial neural network (ANN) results. Performing the ANN,
below 20% was within the satisfactory range. The RMSE twointegrateddevelopmentenvironmentswereusedtocompare
considered in the Taylor Diagram is the centered RMSE thebestparameters.UsingMATLAB,theANNoutputshoweda
difference between the simulated accuracy output and observed mean square error of 0.75212 for the validation considering the
pattern output from the MLE conducted. Additionally, a Elu activation function, 1.0533 for Tanh, and 0.9336 for the
correlation value exceeding 90% was regarded as being of sigmoid function. On the other hand, the testing mean square
significant importance. error results were 0.26379, 0.20594, and 0.21595, respectively.
Considering the parameters on Spyder v5.0, the accuracy rates
were 90.20%, 89.60%, and 84.40%. To which, the final ANN
Marketing 7P’s. After the machine learning algorithm has been considered the Elu function as the best activation function
used and demographic information about the respondents has parameter, which was used in both the hidden and output layer
been collected a marketing strategy based on the Marketing 7Ps run at 150 epochs (Pradhan and Lee 2010). In accordance, the
wasdeveloped.Thistoolincludedsevendistinctelements,which 80% training and 10 validation fold was considered. It was evi-
areProduct, Price,Place,Promotion,Process, PhysicalEvidence, dent that the model (Fig. 5) was deemed acceptable with the
and People. As all aspects of service marketing fall under the R-squared test value being 0.91 at 30 nodes in the hidden layer.
umbrellaofthe7Psinthemarketingmix,theconceptofthe7Ps From the results, it could be seen that the input layer was the
may be used to reflect the complexity of sustainable clothing for differentvariablesconsideredinthisstudy(fromSTPB).Because
clothing companies (Ho et al. 2022). The Marketing 7Ps would of the nonlinear relationship present, several nodes were needed
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 11

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
for the optimum output to be achieved. Upon optimization, 30 and a larger nonlinear relationship framework in this study
nodes were needed to be analyzed in the neural network model comparedtotheirs,andElucouldbethebestfitfortheanalysis.
usingtheEluActivationFunction.AspresentedinEq.(1)(Nanni Tofurthervalidatetheoutput,thevalidationratewasobtained
et al. 2022), Elu is an advance of the ReLU function where the showingover(under)fitting—Fig.6.Forthediscussionsectionto
value lies at [0.1,0.3]. Similar to ReLU, the value of x when bemorecoherent,theSHAPpackagewasconsideredtogenerate
positive lies on the negative region, while its y value would be the relative normalized score of importance to rank the
significance
below zero (Nanni et al. 2022). of each latent variable affecting behavioral intention
|     |     |     |     |     |     |     | to consider | sustainable | apparel. | Table | 4 displays |     | the importance |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | -------- | ----- | ---------- | --- | -------------- | --- |
fðxÞ¼xifx>0elseαðex(cid:2)1Þ ð1Þ scores that have been normalized and will be discussed in the
findings,
|     |     |     |     |     |     |     | following | section. | From the  |      | CPV     | emerged | as  | the most |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ---- | ------- | ------- | --- | -------- |
|     |     |     |     |     |     |     | prominent | latent   | variable, | with | the TPB | domains |     | of PBC,  |
TheutilityofEluasanactivationfunctionhasbeenexpressed
|                   |            |                |             |           |          |              | attitude,   | and subjective | norm        | following | in          | order | of significance.   |         |
| ----------------- | ---------- | -------------- | ----------- | --------- | -------- | ------------ | ----------- | -------------- | ----------- | --------- | ----------- | ----- | ------------------ | ------- |
| by related        | studies to | providea       | better      | accuracy  | ratewhen | dealing      |             |                |             |           |             |       |                    |         |
|                   |            |                |             |           |          |              | Perceived   | economic       | concern     | was       | also deemed |       | to be significant. |         |
| with a nonlinear  |            | relationship   | framework.  |           | This is  | because the  |             |                |             |           |             |       |                    |         |
|                   |            |                |             |           |          |              | However,    | a low          | significant | level     | was seen    | of    | PENC               | and PAS |
| analysis provides | a          | smooth result, | implicating |           | a better | accuracy     |             |                |             |           |             |       |                    |         |
|                   |            |                |             |           |          |              | (near 60%). |                |             |           |             |       |                    |         |
| rate when         | passing    | through        | nodes       | in the    | hidden   | layer. The   |             |                |             |           |             |       |                    |         |
| consequence       | of Elu     | providing      | negative    |           | values   | pushes the   |             |                |             |           |             |       |                    |         |
| calculation       | to batch   | normalization, | thus        | improving |          | the learning | Discussion  |                |             |           |             |       |                    |         |
processoftheneuralnetwork—creatinghigheraccuracyratesand Basedontheresults,CPVstandsoutasthemostcrucialfactorin
|           |         |               |        |     |        |           | determining | customers’ | purchasing |     | intention | for | plastic | apparel, |
| --------- | ------- | ------------- | ------ | --- | ------ | --------- | ----------- | ---------- | ---------- | --- | --------- | --- | ------- | -------- |
| better to | be used | with multiple | paths, | and | large, | nonlinear |             |            |            |     |           |     |         |          |
frameworks (Kim et al. 2020; Xiangyang et al. 2023). However, accountingfor100%.PBCfollowscloselyat94.7%,whileattitude
influence
Eluhasitsdisadvantages;oneofwhichisthatitcanonlybeused (AT) plays a substantial role with an of 87.4%. This
|     |     |     |     |     |     |     |     |     | significance |     |     | influencing | customers’ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----------- | ---------- | --- |
in the hidden layer and that it is computationally expensive. demonstrates the of CPV in
Comparedtotheadoptedstudies,thecurrentstudyhaspresented intentions towards purchasing apparel made of plastic. CPV is
positivelyhighoutputwhenEluwasutilized.Fromotherstudies, crucial in determining how inclined customers are toward pur-
commonresultswereobtainedusingsigmoid,tanh,andsoftmax chasing sustainable apparel products. CPV measures how
(Germanetal.2022a;Gumasingetal.2023;Ongetal.2023;Ong numerous benefits consumers estimate they will obtain from
et al. 2022). This is because there are a greater number of paths these items concerning the prices involved. Several important
aspectsaretakenintoconsiderationwhencustomersevaluatethe
|        |                                |     |     |            |     |     | perceived | value | of sustainable | apparel |     | products. | Brandão | and |
| ------ | ------------------------------ | --- | --- | ---------- | --- | --- | --------- | ----- | -------------- | ------- | --- | --------- | ------- | --- |
| Table3 | Random forestclassifierresults |     |     | (Depth=6). |     |     |           |       |                |         |     |           |         |     |
Costa(2021)indicatedthatapositiveperceivedvalueislinkedto
influence,
|          |     |       |       |     |       |       | a favorable | attitude, | increased | social |     |     | and a | sense of |
| -------- | --- | ----- | ----- | --- | ----- | ----- | ----------- | --------- | --------- | ------ | --- | --- | ----- | -------- |
| Category |     | 60:40 | 70:30 |     | 80:20 | 90:10 |             |           |           |        |     |     |       |          |
empowermentinaddressingobstaclesresponsibleforpurchasing
Best
|         |     |       |       |     |       |       | sustainable | fashion. |     |     |     |     |     |     |
| ------- | --- | ----- | ----- | --- | ----- | ----- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| Entropy |     | 84.41 | 83.30 |     | 84.47 | 90.94 |             |          |     |     |     |     |     |     |
PBCpertainstotheideathatcustomerswhoperceivethevalue
| Standarddeviation |     | 1.215 | 0.894 |     | 0.852 | 1.003 |                |          |               |             |                |           |              |       |
| ----------------- | --- | ----- | ----- | --- | ----- | ----- | -------------- | -------- | ------------- | ----------- | -------------- | --------- | ------------ | ----- |
|                   |     |       |       |     |       |       | of sustainable | clothing | products      | will        | likely         | feel more | empowered    |       |
| Gini              |     | 87.27 | 82.81 |     | 88.47 | 92.00 |                |          |               |             |                |           |              |       |
|                   |     |       |       |     |       |       | and confident  | in       | their ability | to          | make purchases |           | effectively. | The   |
| Standarddeviation |     | 1.021 | 0.664 |     | 0.502 | 0.000 |                |          |               |             |                |           |              |       |
|                   |     |       |       |     |       |       | feeling of     | control  | arises when   | individuals |                | believe   | that their   | deci- |
Random
sionsalignwithwhattheyconsidervaluable,boostingconfidence
| Entropy |     | 82.87 | 80.51 |     | 83.78 | 85.82 |     |     |     |     |     |     |     |     |
| ------- | --- | ----- | ----- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
intheircapacitytomakechoicesthatpromotesustainability.The
| Standarddeviation |     | 4.003 | 4.515 |     | 4.967 | 5.590 |             |           |        |               |     |         |             |     |
| ----------------- | --- | ----- | ----- | --- | ----- | ----- | ----------- | --------- | ------ | ------------- | --- | ------- | ----------- | --- |
|                   |     |       |       |     |       |       | attitude of | customers | played | a substantial |     | role in | influencing | the |
| Gini              |     | 82.61 | 81.03 |     | 84.94 | 85.30 |             |           |        |               |     |         |             |     |
Standarddeviation 3.805 3.991 4.886 5.888 outcome. Customers who perceive value are more inclined
|     |     |     |     |     |     |     | towards | developing | positive | attitudes |     | when | buying | apparel |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------- | --------- | --- | ---- | ------ | ------- |
Fig.4OptimumclassificationmodelwithRFC.X –PerceivedBehavioralControl;X –CustomerPerceivedValue;X –Attitude;X –SubjectiveNorm;
|     |     |     |     | 0   |     |     | 1   |     |     |     | 2   | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X –PerceivedEconomicConcern.
4
12 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Table 4Normalized score of importance.
Latentvariable Importance Normalizedscoreofimportance
CPV 0.234 100%
PBC 0.222 94.7%
AT 0.205 87.4%
SN 0.193 82.6%
PECC 0.189 80.6%
PENC 0.183 78.4%
PAS 0.167 71.5%
materials.Businessesandorganizationscanleveragethepowerof
social approval, peer influence, and the need for acceptance to
promote wider adoption of plastic apparel among consumers—
makingthemactivelycontemplateintegratingsuchproductsinto
theirwardrobechoices.AccordingtoastudyconductedbyZhang
et al. (2019), subjective social norms show a direct and positive
correlation with pro-environmental actions and have a positive
and noteworthy influence on the inclination to buy sustainable
clothing.
This leads us to the next important factor, the perceived eco-
nomicconcern(PECC),accountingfor80.6%significance.PECC
playsacrucialroleininfluencingcustomers’intentionsregarding
purchasing apparel made of plastic. Essentially, it refers to how
customers view and contemplate the financial aspects associated
with these products. Customers often evaluate whether selecting
apparel made from plastic or other alternatives aligns with their
budgetary constraints and monetary priorities. They consider
various factors like initial purchase price, ongoing expenses, and
potentiallong-termsavings.Therefore,ifcustomersperceivethat
Fig.5OptimumANNclassificationmodel. opting for eco-friendly options such as clothing made from
plasticsiseconomicallyviableandcanleadtocostreductionsor
other financial advantages over time, they are more inclined to
foster favorable attitudes regarding the utilization of these pro-
ducts. According to a study by Ansu-Mensah (2021), consumers
who prioritize environmental concerns are willing to buy sus-
tainable products without reservation, even if it means paying a
higherprice.Thus,itcanbeconcludedthatcustomers’intentions
of purchasing sustainable products are affected by the cost of
sustainable products.
The following factor in the hierarchy is known as PENC,
accounting for 78.4% of its importance. PENC refers to custo-
mers’ understanding and sensitivity towards environmental
issues, significantly influencing their choices and actions. Custo-
mers with a strong sense of PENC are more likely to express
strong intentions to purchase clothing items made from plastic
materials. Apparel crafted from plastics is often seen as an
effectivesolutionforaddressingenvironmentalconcernsbythese
Fig.6Validationlossrate. environmentally conscious individuals. This group prioritizes
preserving nature and considers reduced usage of plastic-based
options as a means to lessen their ecological impact or carbon
products made from plastic materials. They perceive these pro- footprint. Such perception boosts their desire even further,
ducts as environmentally friendly and consider them their pre- leading them to utilize such products to contribute positively
ferredchoicesforwhichtheywouldwillinglyspendextramoney towardsfavorableenvironmentaloutcomes.Inastudyconducted
on sustainable clothing. Brandão and Costa (2021) mentioned by Zhang et al. (2019), it was mentioned that previous research
thatattitudeandperceivedvalueareassociatedwithoneanother. has typically found a positive link between PENC and the pur-
The effects of these actions have an impact on how consumers chase intention to buy sustainable products. Additionally, the
behave. Therefore, having a strong understanding of the envir- study demonstrated a positive association between PENC and
onment may result in a positive attitude (AT) and more sig- boththeinclinationtobuysustainableclothingproductsandthe
nificantcustomerbehavioralcontrol(PBC)overthechallengesof attitude toward purchasing them, demonstrating how concerned
achieving sustainable apparel consumption. individualsarewithenvironmentalissuesandhoweagertheyare
SN plays a significant role, accounting for 82.6%. SN have a to support attempts to address them.
significant influence on shaping consumer behavior, particularly At71.5%,thePASrankslowestamongcontributingfactorson
with social and peer norms strongly affecting individuals’ pur- the list. This indicates that customers show importance in
chasing intention towards buying clothes made from plastic receiving support, recommendations, or endorsements from
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 13

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
authoritative figures or institutions regarding their attitudes and beinlinewithconsumervaluesandpreferences.Fromthisstudy,
beliefsaboutpurchasingsustainableapparelproducts.Itsuggests CPV—along with the functionality, consumer perception, brand
that they value and trust advice or guidance from sources they sustainability, desired values, and motivation as a strategy for
perceive as credible and having authority. Governments and selling apparel, from plastic to apparel. Specifically,
environmental organizations, according to the study by Lin and Functionality Consumers’ perceptions of the usefulness of
Huang (2012), offer subsidies or promotions to encourage indi- sustainable clothing influence their decisions regarding their
vidualstolivesustainably.Additionally,itwassuggestedthatfor purchase.
green consumption to become the norm, both the government Consumer perception: By comprehending consumer percep-
and environmental organizations must actively promote it. Fur- tions and how they affect purchasing decisions, businesses may
thermore, the favorable connection between the educational createenvironmentallyfriendlyapparellinesthatsatisfydemand.
attainment of customers and their inclination to buy sustainable Brand sustainability: The decisions consumers make for
clothing shows that governments should work towards creating purchasing sustainable clothing goods are favorably connected
communities that are not just more educated but also more with the importance of fashion brand sustainability.
mindfuloftheenvironmentbyinvestingineducation(Dangelico Desired values: Recognizing what consumers want from
et al. 2022). environmentallyfriendlyclothesmayassistbusinessesincreating
The significance of every factor discussed in this paper lies in sustainable clothing lines that satisfy demand.
their ability to exceed the 60%significant level. The ranking was Motivations for purchasing: Understanding customer moti-
determined solely based on the results derived from various vations for choosing eco-friendly clothes may help companies
methodsemployedduringdataanalysisofasurveycompletedby create marketing plans that resonate with their target
participants. Overall, it was concluded that the three most demographic.
important elements that needed to be emphasized in order to By generating sustainable value propositions, gaining insight
encourageindividualstopurchasesustainableapparelwereCPV, intoconsumerperceptionsanddesiredvalues,andimplementing
PBC, and attitude (AT). marketing tactics that resonate with their target market,
businesses may raise the perceived value of sustainable apparel
among their customers. Other suggestions are presented.
Theoretical implications. The TPB framework may be used for
evaluating consumers’ behavioral intentions when it comes to
For apparel industries. Given the substantial environmental
making sustainable apparel purchases. Based on several studies,
impact associated with the apparel industry, it is more crucial
theTPBframeworkcanbeaneffectivetoolforunderstandingthe
variablesthataffectaperson’sintentionwhenpurchasingapparel thanevertousesustainableprocedures.Sustainablefashionisnot
merely a fashion trend but also an essential requirement for the
made from plastic. By considering these variables, interventions
industry. Companies have to adapt to keep up with this per-
may be created that encourage sustainable behavior and the spective as customers take an active role in reducing fashion’s
reduction of pollution resulting from plastic waste by means of
negative environmental impacts. Ethical and sustainable fashion
plastic recycling and clothing production. CPV was shown to
have the most significant influence on how consumers felt they has evolved from a trend to an economic imperative for the
apparel industry. The apparel sector could promote sustainable
had control over their behavior and how they perceived pur-
clothingbyimplementingeco-design,supplychainsustainability,
chasingproductsmadeofplastic,whichhasnumerousimportant
consumer education, and waste management strategies. The
theoretical implications. To begin with, it emphasizes the sig-
nificantimpactofexternalfactorsonshapingpurchaseintentions fashionindustrymusttransitiontosustainable manufacturingto
solve some of the social and environmental issues that societies
andpro-environmentalattitudes,especiallywhensuchfactorsare
are now facing. Fast fashion must be reviewed considering the
related to understanding the worth of the products. This study
emphasizes the importance of external social variables in influ- environmentalandsocialconsequencesitimposesonsociety,and
more sustainable business strategies are critically important.
encing individual decision-making and is consistent with well-
known behavioral concepts like the TPB. CPV has a beneficial Sustainable manufacturing techniques may be used through
impact on consumers’ intentions regarding buying and a readi- ethicallaborpractices,especiallyusingmaterialssuchasrecycled
plastic bottles and promoting recycling and reuse. As more
nesstospendextraonproductsthatsupportsustainablefashion.
fashion customers take up the cause of sustainability, apparel
CPV may therefore be used to assess company strategies toward manufacturers can advance and profit from the opportunity.
perceived sustainability and forecast consumer attitudes regard-
ing sustainable apparel. Consequently, the proposed STPB fra- For the government. Governments can play a significant role in
mework may evaluate individual behavior comprehensively with
advancing sustainable clothing by establishing rules, implement-
regardtosustainabilityandsustainablebehaviormoreholistically
ing legislation, encouraging international collaboration, and
than other extended TPB or PEPB frameworks.
implementing policy interventions. Regulation may encourage
ethical, circular, and sustainable fashion, enabling businesses to
Practical and managerial implications. To reduce plastic pol- viewaproduct’sworthasslowlyloweringandboostingacircular
lution, evaluating the factors influencing customers’ behavioral economy. Laws can promote sustainability in the textile and
intentions toward purchasing sustainable apparel is essential. fashion sectors by compelling companies to provide information
According to the study’s findings, Filipinos are willing to spend ontheirsustainabilitydevelopmentandchargingfinesiftheyfall
extra on products that support sustainable fashion and are open shortofgoals.Internationalcollaborationmaysupportinitiatives
to buying clothes made of plastic. The community should con- to change the apparel industry to one that is more sustainable.
sider practical implications regarding people’s behavioral inten- Sustainable fashion consumption can be influenced by policy
tions toward purchasing sustainable apparel. These implications changes, such as tax incentives for businesses that employ
includeinitiativesandstrategiesthefashionindustrymaytaketo recyclable materials or provide apparel repair services.
promote a change and lean towards environmentally friendly The results imply that companies, environmental advocacy
clothing.Companiesmayconsidersustainablevaluepropositions. organizations, and political leaders should consider utilizing
Businesses can develop this to improve the perception of the authoritative support to promote sustainable clothing. This may
sustainabilityoftheirbusinessmodels.Thesepropositionsshould include pursuing partnerships or endorsements from reputable
14 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
people or organizations, displaying certificates or stamps of regarding purchasing sustainable apparel. This study highlights
approval, or actively advertising the potential compatibility of howimportantitistotakethesefactorsintoconsiderationwhen
their goods with reliable recommendations. By doing this, establishing marketing strategies and initiatives intended to raise
companiescanincreaseconsumers’positiveviewsandconfidence awareness of products made with plastic in order to make a
regarding purchasing environmentally friendly products, such as positive contribution towards the advancement of a sustainable
apparel made of plastic, which can encourage more people to environmenttoreduceplasticpollution.Furthermore,itopensup
engage in environmentally friendly behaviors. theopportunitytoconductfurtherinvestigationandexamination
|     |     |     |     |     |     |     |     | of these | factors by | employing | advanced |     | machine-learning |     | meth- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | -------- | --- | ---------------- | --- | ----- |
odologiesandlargersetsofdatatoenhanceourunderstandingof
Conclusion sustainable consumer behavior. For ANN, either MATLAB or
individuals’
This study explored the factors that impact beha- Python codes could be utilized and could still provide similar
| vioral intentions |          | towards | purchasing | apparel  | made     | from         | plastic. | findings. |     |     |     |     |     |     |     |
| ----------------- | -------- | ------- | ---------- | -------- | -------- | ------------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| The research      | utilized | two     | machine    | learning | methods, | specifically |          |           |     |     |     |     |     |     |     |
RFCandANNandwereemployedtoanalyzethecollecteddata.
|     |     |     |     |     |     |     |     | Limitations | and | future | research. | The study | could | be  | used and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --------- | --------- | ----- | --- | -------- |
ThefindingsfromthisresearchindicatedthatCPVandPBCwere
|     |     |     |     |     |     |     |     | expanded | to evaluate | the | sustainabilityof |     | the apparel | industry | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ---------------- | --- | ----------- | -------- | --- |
the main variables influencing consumers’ behavioral intention customers’
|     |     |     |     |     |     |     |     | various | nations | as well | as the |     | behavioral | intentions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ------ | --- | ---------- | ---------- | --- |
toward purchasing apparel made of plastic. Customers who toward purchasing sustainable apparel. It does, however, have
perceivevaluearemorelikelytoestablishpositiveattitudes(AT) certain restrictions. First, in terms of demographics, the largest
while purchasing sustainable apparel products. The feeling of portion of survey participants (55.4%) were within the age range
control arises when individuals believe that their decisions align of 18 to 25. The research made an effort to include people of all
confidence
with what they consider valuable, boosting in their ages;however,becausesocialmediaplatformswereusedtogather
capacitytomakechoicesthatpromotesustainability.Theattitude data,themajorityofparticipantswereunder30.Inaddition,since
ofcustomersplayedasubstantialroleininfluencingtheoutcome. respondents were simply asked to categorize their region of resi-
Customers who perceive value are more inclined to develop dence as rural or urban, the study was unable to determine the
positive attitudes when buying apparel products made from specific
|     |     |     |     |     |     |     |     | exact places | of residence |     | of the respondents. |     | The |     | coordi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ------------------- | --- | --- | --- | ------- |
plastic materials. They perceive these products as environmen- therespondents’
|     |     |     |     |     |     |     |     | nates of |     |     | locations | mayhave | affectedtherelative |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --------- | ------- | ------------------- | --- | --- |
tallyfriendlyandconsiderthemtheirpreferredchoicesforwhich
|     |     |     |     |     |     |     |     | importance | of various | elements, | which | led | to a | different | view of |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ----- | --- | ---- | --------- | ------- |
they would willingly spend extra money on sustainable clothing. customerpurchasingbehavior.Futureresearchersmightimprove
customers’
Moreover, inclination towards purchasing sustain- this by utilizing a more diverse sample procedure and ensuring
ableclothingisdirectlyandpositivelyinfluencedbysocialnorms
|     |     |     |     |     |     |     |     | that various | demographic |     | characteristics |     | are considered |     | in their |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --------------- | --- | -------------- | --- | -------- |
(SN), which also have a positive and substantial effect on other studies.Inaccordance,real-lifetestingofmodelandresultscould
pro-environmental behaviors. Customer intentions were also be developed when pre- and post-purchase evaluation and data
affected by perceived economic concern (PECC) because mone- collectionisemployed.Thiscouldcreateabetterpredictivemodel.
tary factors were taken into consideration when making pur- Moreover, the study was unable to take into account and
chasing decisions towards sustainable products. Customers with distinguishbetweenonlineandin-personpurchasesofsustainable
| high environmental |     | awareness |     | were more | inclined | towards | pur- |          |            |         |     |             |     |       |          |
| ------------------ | --- | --------- | --- | --------- | -------- | ------- | ---- | -------- | ---------- | ------- | --- | ----------- | --- | ----- | -------- |
|                    |     |           |     |           |          |         |      | apparel. | This could | enhance | the | total scope | and | depth | since it |
chasing sustainable products as a strategy to reduce their envir- person’s
|          |        |     |         |               |     |               |     | would need | to   | explore    | deeper into | the        | analysis | of a |          |
| -------- | ------ | --- | ------- | ------------- | --- | ------------- | --- | ---------- | ---- | ---------- | ----------- | ---------- | -------- | ---- | -------- |
| onmental | impact | and | promote | environmental |     | preservation, |     |            |      |            |             |            |          |      |          |
|          |        |     |         |               |     |               |     | intentions | when | purchasing | a           | particular | service  | or   | product. |
respondent’s
which increases the importance of PENC. Apparel crafted from Second, the study was unable to relate the
plastics is often seen as an effective solution for addressing demographics to their behavior, which would have provided a
environmental concerns by these environmentally conscious morecomprehensiveoverviewoftheirbehavioralintentionswhen
individuals. This group prioritizes preserving nature and con- itcomestopurchasingsustainableapparel.Futureresearchersare,
sidersreducedusageofplastic-basedoptionsasameanstolessen therefore, encouraged to offer new perspectives on the subject
their ecological impact or carbon footprint. Such perception matter.Thefindings,metrics,andquestionnairesmaybeusedby
boosts their desire even further, leading them to utilize such futureresearcherstoconductadditionalstudiesandtoapplynew
products to contribute positively towards favorable environ- methodsandideasinordertocomeupwithnewperspectivesand
mental outcomes.
|     |     |     |     |     |     |     |     | comprehension | regarding |     | customer | behavioral | intentions |     | toward |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | -------- | ---------- | ---------- | --- | ------ |
Finally,PASreferstohowimportantcustomersfindittohave
|                 |     |           |       |            |             |     |          | purchasingsustainable |             | apparel.Lastly, |     | future       | researchcould |                 | look |
| --------------- | --- | --------- | ----- | ---------- | ----------- | --- | -------- | --------------------- | ----------- | --------------- | --- | ------------ | ------------- | --------------- | ---- |
| their attitudes |     | and ideas | about | purchasing | sustainable |     | clothing |                       |             |                 |     |              |               |                 |      |
|                 |     |           |       |            |             |     |          | into the              | role played | by customer     |     | satisfaction | in            | environmentally |      |
products supported by or endorsed by reputable individuals or friendly purchasing behaviors by concentrating on consumers
first-hand
institutions. It was suggested that for green consumption to who have experience withsustainable clothes.
| become        | the norm, | both     | the     | government | and          | environmental |        |                   |     |     |     |     |     |     |     |
| ------------- | --------- | -------- | ------- | ---------- | ------------ | ------------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| organizations | must      | actively | promote | it.        | Furthermore, | the           | favor- | Data availability |     |     |     |     |     |     |     |
ableconnectionbetweentheeducationalattainmentofcustomers
Thedatasetsgeneratedduringand/oranalyzedduringthecurrent
| and their | inclination |     | to buy | sustainable | clothing | shows | that |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------ | ----------- | -------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
studyareavailablefromthecorrespondingauthoronreasonable
governmentsshouldworktowardscreatingcommunitiesthatare
request.
notjustmoreeducatedbutalsomoremindfuloftheenvironment
| by investing | in        | education. |             |            |         |              |         |           |                      |     |        |       |     |     |     |
| ------------ | --------- | ---------- | ----------- | ---------- | ------- | ------------ | ------- | --------- | -------------------- | --- | ------ | ----- | --- | --- | --- |
|              |           |            |             |            |         |              |         | Received: | 2 July2024;Accepted: |     | 2 June | 2025; |     |     |     |
| In summary,  |           | it was     | found       | that every | single  | one of the   | afore-  |           |                      |     |        |       |     |     |     |
| mentioned    | variables | was        | significant | and        | had     | a weight     | of more |           |                      |     |        |       |     |     |     |
| than 60%.    | The       | study      | emphasized  | the        | crucial | roles played | by      |           |                      |     |        |       |     |     |     |
perceivedvalue,behavioralcontrol,consumerattitude,economic
References
| considerations, |             | environmental |             | concerns,   | and          | social norms  |         | in        |           |           |                |        |             |         |              |
| --------------- | ----------- | ------------- | ----------- | ----------- | ------------ | ------------- | ------- | --------- | --------- | --------- | -------------- | ------ | ----------- | ------- | ------------ |
|                 |             |               |             |             |              |               |         | Alam MM,  | Alam MZ,  | Rahman    | SA, Taghizadeh |        | SK (2021)   | Factors | influencing  |
| determining     | sustainable |               | consumption |             | behavior.    | Additionally, |         | it        |           |           |                |        |             |         |              |
|                 |             |               |             |             |              |               |         | health    | adoption  | and its   | impact on      | mental | well-being  | during  | COVID-19     |
| provided        | important   | details       | on          | the complex | interactions |               | between |           |           |           |                |        |             |         |              |
|                 |             |               |             |             |              |               |         | pandemic: | a sem-ann | approach. | J Biomed       | Inform | 116:103722. |         | https://doi. |
these variables that affect customers’ behavioral intentions org/10.1016/j.jbi.2021.103722
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 15

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Abdel-Shafy HI, Mansour MSM (2018) Solid waste issue: sources, composition, GholamiH,MohamadifarA,SorooshianA,Jansen JD(2020)Machine-learning
disposal,recycling,andvalorization.EgyptJPet27(4):1275–1290.https://doi. algorithmsforpredictinglandsusceptibilitytodustemissions:thecaseofthe
org/10.1016/j.ejpe.2018.07.003 JazmurianBasin,Iran.AtmosPollutRes11(8):1303–1315.https://doi.org/10.
AbolghasemiM,BehE,TarrG,GerlachR(2020)Demandforecastinginsupply 1016/j.apr.2020.05.009
chain:theimpactofdemandvolatilityinthepresenceofpromotion.Comput GomesdeOliveiraL,MirandaFG,dePaulaDiasMA(2022)Sustainablepractices
IndEng142:106380.https://doi.org/10.1016/j.cie.2020.106380 inslowandfastfashionstores:whatdoesthecustomerperceive?CleanEng
AbusafiehS,RazemM(2017)Humanbehaviorandenvironmentalsustainability: Technol6:100413.https://doi.org/10.1016/j.clet.2022.100413
promotingapro-environmentalbehaviorbyharnessingthesocial,psycho- Grazzini L, Acuti D, Aiello G (2021) Solving the puzzle of sustainable fashion
logical and physical influences of the built environment. E3S Web Conf consumption:theroleofconsumers’implicitattitudesandperceivedwarmth.
23:02003.https://doi.org/10.1051/e3sconf/20172302003 JCleanProd287:125579.https://doi.org/10.1016/j.jclepro.2020.125579
Adıgüzel F, Donato C (2021) Proud to be sustainable: upcycled versus recycled Gumasing MJ, Ong AK, Sy MA, Prasetyo YT, Persada SF (2023). A machine
luxury products. J Bus Res 130:137–146. https://doi.org/10.1016/j.jbusres. learningensembleapproachtopredictingfactorsaffectingtheintentionand
2021.03.033 usage behavior towards online groceries applications in the Philippines.
AjzenI(1991)Thetheoryofplannedbehavior.OrganBehavHumDecisProcess Heliyon9(10).https://doi.org/10.1016/j.heliyon.2023.e20644
50(2):179–211.https://doi.org/10.1016/0749-5978(91)90020-t Güvenİ,ŞimşirF(2020)Demandforecastingwithcolorparameterinretailapparel
Al-MashraieM,ChungSH,JeonHW(2020)Customerswitchingbehavioranalysis industryusingartificialneuralnetworks(ANN)andsupportvectormachines
in the telecommunication industry via push-pull-mooring framework: a (SVM)methods.ComputIndEng147:106678
machinelearningapproach.ComputIndEng144:106476.https://doi.org/10. H&M Group (2023) Retrieved from https://hmgroup.com/sustainability/
1016/j.cie.2020.106476 circularity-and-climate/materials/#:~:text=Recycled%20plastic&text=We%
Ansu-MensahP(2021)Greenproductawarenesseffectongreenpurchaseinten- 20then%20use%20this%20plastic,avoiding%20harm%20to%20our%20planet
tionsofUniversityStudents’:anemergingmarket’sperspective.FuturBusJ HajishirziR,CostaCJ,AparicioM(2022)Boostingsustainabilitythroughdigital
7(1).https://doi.org/10.1186/s43093-021-00094-5 transformation’s domains and resilience. Sustainability 14(3):1822. https://
Awoyera PO, Adesina A (2020) Plastic wastes to construction products: status, doi.org/10.3390/su14031822
limitations and future perspective. Case Stud Constr Mater 12. https://doi. Ho C-I, Liu Y, Chen M-C (2022) Factors influencing watching and purchase
org/10.1016/j.cscm.2020.e00330 intentions on live streaming platforms: from A 7PS marketing mix per-
BickartBA,RuthJA(2012)Greeneco-sealsandadvertisingpersuasion.JAdvert spective.Information13(5):239.https://doi.org/10.3390/info13050239
41(4):51–67.https://doi.org/10.1080/00913367.2012.10672457 JaheerMuktharKP,NagadeepaC,SelvaratnamDP,PushpaA,ShuklaN(2024)
BossiF,DiGruttolaF,MastrogiorgioA,D’ArcangeloS,LattanziN,MaliziaAP, Sustainable wardrobe: recycled clothing towards sustainability and eco-
Ricciardi E (2022) Estimating successful internal mobility: a comparison friendliness.DiscovSustain5(1).https://doi.org/10.1007/s43621-024-00358-4
betweenstructuralequationmodelsandmachinelearningalgorithms.Front JalilNA,FikryA,ZainuddinA(2016)Theimpactofstoreatmospherics,perceived
ArtifIntell5.https://doi.org/10.3389/frai.2022.848015 value, and customer satisfaction on behavioural intention. Procedia Econ
BoyerRHW,HunkaAD,VanacoreE,Brauer HB(2025)Whysomeconsumers Financ37:538–544.https://doi.org/10.1016/s2212-5671(16)30162-9
choosecircularandothersdonot:thesocialpracticeofshoppingforcircular JamshidiM(Behdad),RoshaniS,DaneshfarF,LalbakhshA,RoshaniS,ParandinF,
garments.CircEconSustainhttps://doi.org/10.1007/s43615-025-00527-1 MalekZ,TallaJ,PeroutkaZ,JamshidiA,HadjilooeiF,LalbakhshP(2022)
Brandão A, Costa AG (2021) Extending the theory of planned behaviour to Hybrid deep learning techniques for predicting complex phenomena: a
understandtheeffectsofbarrierstowardssustainablefashionconsumption. reviewonCovid-19AI3(2):416–433.https://doi.org/10.3390/ai3020025
EurBusRev33(5):742–774.https://doi.org/10.1108/ebr-11-2020-0306 Jamshidi M, Lalbakhsh A, Talla J, Peroutka Z, Hadjilooei F, Lalbakhsh P,
BrewerMK(2019)Slowfashioninafastfashionworld:promotingsustainability Mohyuddin W (2020) Artificial Intelligence and Covid-19: deep learning
andresponsibility.Laws8(4):24.https://doi.org/10.3390/laws8040024 approaches for diagnosis and treatment. IEEE Access 8:109581–109595.
Chang X, Xue Y, LiJ, Zou L, TangM (2019) Potential health impact ofenvir- https://doi.org/10.1109/access.2020.3001973
onmental micro‐ and Nanoplastics Pollution. J Appl Toxicol 40(1):4–15. JangH-S,XingS(2020)Amodeltopredictammoniaemissionusingamodified
https://doi.org/10.1002/jat.3915 geneticartificialneuralnetwork:analyzingCementmixedwithflyashfroma
ChenJ,LiQ,WangH,DengM(2019)Amachinelearningensembleapproach coal-fired power plant. Constr Build Mater 230:117025. https://doi.org/10.
basedonRandomForestandradialbasisfunctionneuralnetworkforrisk 1016/j.conbuildmat.2019.117025
evaluationofRegionalFloodDisaster:acasestudyoftheyangtzeriverdelta, Jena R, Pradhan B, Beydoun G, Nizamuddin, Ardiansyah, Sofyan H, Affan M
China. Int J Environ Res Public Health 17(1):49. https://doi.org/10.3390/ (2020)Integratedmodelforearthquakeriskassessmentusingneuralnetwork
ijerph17010049 and analytic hierarchy process: Aceh Province, Indonesia. Geosci Front
Chi T, Ganak J, Summers L, Adesanya O, McCoy L, Liu H, Tai Y (2021) 11(2):613–634.https://doi.org/10.1016/j.gsf.2019.07.006
Understandingperceivedvalueandpurchaseintentiontowardeco-friendly JinX,OmarA,FuK(2024)Factorsinfluencingpurchaseintentiontowardrecycled
athleisureapparel:InsightsfromU.S.millennials.Sustainability13(14):7946. apparel: evidence from China. Sustainability 16(9):3633. https://doi.org/10.
https://doi.org/10.3390/su13147946 3390/su16093633
Dangelico RM, Alvino L, Fraccascia L (2022) Investigating the antecedents of KalinićZ,MarinkovićV,KalinićL,Liébana-CabanillasF(2021)Neuralnetwork
consumer behavioral intention for sustainable fashion products: Evidence modelingofconsumersatisfactioninMobileCommerce:anempiricalana-
from a large survey of Italian consumers. Technol Forecast Soc Change lysis. Expert Syst Appl 175:114803. https://doi.org/10.1016/j.eswa.2021.
185:122010.https://doi.org/10.1016/j.techfore.2022.122010 114803
Eckle K, Schmidt-Hieber J (2019) A comparison of deep networks with ReLU Kar S, Basu K, Sarkar B (2023) Advertisement policy for dual-channel within
activation function and linear spline-type methods. Neural Netw emissions-controlled Flexible production system. J Retail Consum Serv
110:232–242.https://doi.org/10.1016/j.neunet.2018.11.005 71:103077.https://doi.org/10.1016/j.jretconser.2022.103077
EvodeN,QamarSA,BilalM,BarcelóD,IqbalHMN(2021)Plasticwasteandits Kim D, Kim J, Kim J (2020) Elastic exponential linear units for convolutional
management strategies for Environmental Sustainability. Case Stud Chem neural networks. Neurocomputing 406:253–266. https://doi.org/10.1016/j.
EnvironEng4:100142.https://doi.org/10.1016/j.cscee.2021.100142 neucom.2020.03.051
FanY,ChenJ,ShirkeyG,JohnR,WuSR,ParkH,ShaoC(2016)Applicationsof KimI,JungHJ,LeeY(2021)Consumers’valueandriskperceptionsofcircular
structuralequationmodeling(SEM)inEcologicalStudies:anupdatedreview. fashion:comparisonbetween secondhand, upcycled, andrecycledclothing.
EcolProcess5(1).https://doi.org/10.1186/s13717-016-0063-3 Sustainability13(3):1208.https://doi.org/10.3390/su13031208
FerioliM,GazzolaP,GrechiD,VătămănescuE-M(2022)Sustainablebehaviourof Kuah ATH, Wang P (2020) Circular economy and consumer acceptance: an
BCorpsfashioncompaniesduringCovid-19:aquantitativeeconomicana- exploratory study in East and Southeast Asia. J Clean Prod 247:119097.
lysis.JCleanProd374:134010.https://doi.org/10.1016/j.jclepro.2022.134010 https://doi.org/10.1016/j.jclepro.2019.119097
FungY-N,ChanH-L,ChoiT-M,LiuR(2021)Sustainableproductdevelopment LeeE-J,ChoiH,HanJ,KimDH,KoE,KimKH(2020)Howto“Nudge”your
processesinfashion:supplychainsstructuresandclassifications.IntJProd consumerstowardsustainablefashionconsumption:Anfmriinvestigation.J
Econ231:107911.https://doi.org/10.1016/j.ijpe.2020.107911 BusRes117:642–651.https://doi.org/10.1016/j.jbusres.2019.09.050
GansserOA,ReichCS(2023)Influenceofthenewecologicalparadigm(NEP)and LiM,VanberkelP,ZhongX(2022)Predictingambulanceoffloaddelayusinga
environmentalconcernsonpro-environmentalbehavioralintentionbasedon hybriddecisiontreemodel.Socio-EconPlanSci80:101146.https://doi.org/
thetheoryofplannedbehavior(TPB).JCleanProd382:134629.https://doi. 10.1016/j.seps.2021.101146
org/10.1016/j.jclepro.2022.134629 LinP-C,HuangY-H(2012)Theinfluencefactorsonchoicebehaviorregarding
German JD, Ong AK, Perwira Redi AA, Robas KP (2022a) Predicting factors green products based on the theory of consumption values. J Clean Prod
affecting the intention to use a 3PL during the COVID-19 pandemic: a 22(1):11–18.https://doi.org/10.1016/j.jclepro.2011.10.002
machinelearningensembleapproach.Heliyon8(11).https://doi.org/10.1016/ Lin S-C, Nadlifatin R, Amna A,Persada S, Razif M (2017) Investigating citizen
j.heliyon.2022.e11382 behavior intention on mandatory and voluntary Pro-Environmental
16 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
programs through a pro-environmental planned behavior model. Sustain- Rehman IH, Ahmad A, Akhter F, Aljarallah A (2022) A dual-stage SEM-Ann
ability9(7):1289.https://doi.org/10.3390/su9071289 analysistoexploreconsumeradoptionofsmartwearablehealthcaredevices.J
LiuP,LiM,DaiD,GuoL(2021)Theeffectsofsocialcommerceenvironmental GlobInfManag29(6):1–30.https://doi.org/10.4018/jgim.294123
characteristicsoncustomers’purchaseintentions:thechainmediatingeffect Roh T, Seok J, Kim Y (2022) Unveiling ways to reach organic purchase: green
ofcustomer-to-customerinteractionandcustomer-perceivedvalue.Electron perceivedvalue,perceivedknowledge,attitude,subjectivenorm,andTrust.J
CommerResAppl48:101073.https://doi.org/10.1016/j.elerap.2021.101073 RetailConsumServ67:102988.https://doi.org/10.1016/j.jretconser.2022.102988
MagnierL,MuggeR,SchoormansJ(2019)Turningoceangarbageintoproducts– SaricamC,OkurN(2018)Analysingtheconsumerbehaviorregardingsustainable
consumers’evaluationsofproductsmadeofRecycledOceanPlastic.JClean fashionusingtheoryofplannedbehavior.TextSciClothingTechnol1–37.
Prod215:84–98.https://doi.org/10.1016/j.jclepro.2018.12.246 https://doi.org/10.1007/978-981-13-1265-6_1
Milani L, Grumi S, Camisasca E, Miragoli S, Traficante D, Di Blasio P (2020) Sarkar B, Fan S-KS, Pareek S, Mridha B (2024) Sustainable multi-biofuel pro-
Familial risk and protective factors affecting CPS Professionals’ Child duction with stochastic lead time and Optimum Energy Utilization under
Removal Decision: a decision tree analysis study. Child Youth Serv Rev flexiblemanufacturing.ComputIndEng193:110223.https://doi.org/10.1016/
109:104687.https://doi.org/10.1016/j.childyouth.2019.104687 j.cie.2024.110223
MridhaB,SarkarB(2025)Implicationsofcarbonpoliciesforflexibledemandand Sarkar B, KarS,Basu K,GuchhaitR (2022) Asustainablemanagerial decision-
smartproductionwithRandomleadtimedemandunderasustainablesupply makingproblemforasubstitutableproductinadual-channelundercarbon
chainmanagement.EnvironDevSustainhttps://doi.org/10.1007/s10668-025- tax policy. Comput Ind Eng 172:108635. https://doi.org/10.1016/j.cie.2022.
06038-1 108635
Nadlifatin R, Lin S-C, Rachmaniati Y, Persada S, Razif M (2016) A pro- SarkarB,KarS,BasuK,SeoYW(2023)Istheonline-offlinebuy-online-pickup-in-
environmental reasoned action model for measuring citizens’ intentions store retail strategy best among other product delivery strategies under
regarding ecolabel product usage. Sustainability 8(11):1165. https://doi.org/ Variableleadtime?JRetailConsumServ73:103359.https://doi.org/10.1016/
10.3390/su8111165 j.jretconser.2023.103359
Nam C, Dong H, Lee Y-A (2017) Factors influencing consumers’ purchase Savari M, Gharechaee H (2020) Application of the extended theory of planned
intentionofGreenSportswear.FashionTextiles4(1).https://doi.org/10.1186/ behaviortopredictIranianfarmers’intentionforsafeuseofchemicalferti-
s40691-017-0091-3 lizers.JCleanProd263:121512.https://doi.org/10.1016/j.jclepro.2020.121512
Nanni L, Brahnam S, Paci M, Ghidoni S (2022) Comparison of different con- SedliačikováM,AláčP,MoresováM(2020)Howbehavioralaspectsinfluencethe
volutional neural network activation functions and methods for building sustainablefinancialdecisionsofshareholders:anempiricalstudyandpro-
ensemblesforsmalltomidsizemedicaldatasets.Sensors22(16):6129.https:// posal for a relevant decision-making concept. Sustainability 12(12):4813.
doi.org/10.3390/s22166129 https://doi.org/10.3390/su12124813
Nguyen XH, Tran HL, Nguyen QH, Luu TP, Dinh HL, Vu HT (2020) Factors ShamsM,AlamI,MahbubMS(2021)PlasticpollutionduringCOVID-19:plastic
influencingtheconsumer’sintentiontobuyfashionproductsmadebyrecycled wastedirectivesanditslong-termimpactontheenvironment.EnvironAdv
plasticwaste.ManagSciLett3613–3622.https://doi.org/10.5267/j.msl.2020.6.032 5:100119.https://doi.org/10.1016/j.envadv.2021.100119
Niinimäki K, Peters G, Dahlbo H, Perry P, Rissanen T, Gwilt A (2020) The SooraniF,AhmadvandM(2019)Determinantsofconsumers’foodmanagement
environmentalpriceofFastFashion.NatRevEarthEnviron1(4):189–200. behavior: applying and extending the theory of planned behavior. Waste
https://doi.org/10.1038/s43017-020-0039-9 Manag98:151–159.https://doi.org/10.1016/j.wasman.2019.08.025
NikeSustainability(2024)Retrievedfromhttps://www.nike.com/sustainability StrattonSJ(2021)Populationresearch:conveniencesamplingstrategies.Prehosp
OECD(2022)Retrievedfromhttps://www.oecd.org/environment/plastic-pollution- DisasterMed36(4):373–374.https://doi.org/10.1017/s1049023x21000649
is-growing-relentlessly-as-waste-management-and-recycling-fall-short.htm Talan A, Tyagi RD, Surampalli RY (2020) Social dimensions of sustainability.
OngAK,CordovaLN,LonganillaFA,CaprechoNL,JavierRA,BorresRD,Ger- Sustainability183–206.https://doi.org/10.1002/9781119434016.ch9
manJD(2023)Purchasingintentionsanalysisofhybridcarsusingrandom TestaF,DiIorioV,CerriJ,PretnerG(2021)Fiveshadesofplasticinfood:which
forestclassifieranddeeplearning.WorldElectrVehJ14(8):227.https://doi. potentiallycircularpackagingsolutionsareItalianconsumersmoresensitive
org/10.3390/wevj14080227 to. Resour, Conserv Recycling 173:105726. https://doi.org/10.1016/j.
OngAK,PrasetyoYT,SalazarJM,ErfeJJ,AbellaAA,YoungMN,ChuenyindeeT, resconrec.2021.105726
NadlifatinR,NgurahPerwiraRediAA(2022)Investigatingtheacceptanceof TezerA,BodurHO(2019)Thegreenconsumption effect:howusinggreenpro-
thereopeningbataannuclearpowerplant:integratingprotectionmotivation ductsimprovesconsumptionexperience.JConsumRes47(1):25–39.https://
theory and extended theory of planned behavior. Nucl Eng Technol doi.org/10.1093/jcr/ucz045
54(3):1115–1125.https://doi.org/10.1016/j.net.2021.08.032 Tiseo I (2023) Retrieved from https://www.statista.com/statistics/1270902/ocean-
OngAK,MendozaMC,PonceJR,BernardoKT,TolentinoSA,DiazJF,YoungMN plastic-pollution-from-select-rivers-worldwide
(2024)AnalysisofinvestmentbehavioramongFilipinos:integrationofsocial UzirMU,AlHalbusiH,ThurasamyR,ThiamHockRL,AljaberiMA,HasanN,
exchangetheory(SET)andthetheoryofplannedbehavior(TPB).PhysA: HamidM(2021)Theeffectsofservicequality,perceivedvalueandtrustin
StatMechAppl654:130162.https://doi.org/10.1016/j.physa.2024.130162 homedeliveryservicepersonneloncustomersatisfaction:Evidencefroma
ÖztürkOB,BaşarE(2022)Multiplelinearregressionanalysisandartificialneural developingcountry.JRetailConsumServ63:102721.https://doi.org/10.1016/
networks based decision support system for energy efficiency in shipping. j.jretconser.2021.102721
OceanEng243:110209.https://doi.org/10.1016/j.oceaneng.2021.110209 VishnoiSK,MathurS,AgarwalV,VirmaniN,JagtapS(2025)Whatdrivesgen-
Park HJ, Lin LM (2020) Exploring attitude–behavior gap in sustainable con- erationZtochooseGreenApparel?Unravelingtheimpactofenvironmental
sumption:comparisonofrecycledandupcycledfashionproducts.JBusRes knowledge,altruismandperceivedinnovativeness.IntJSustainEng18(1).
117:623–628.https://doi.org/10.1016/j.jbusres.2018.08.025 https://doi.org/10.1080/19397038.2025.2473986
PolyportisA,MuggeR,MagnierL(2022)Consumeracceptanceofproductsmade Waheed R, Sarwar S, Alsaggaf MI (2023) Relevance of energy, Green and blue
from recycled materials: a scoping review. Resour, Conserv Recycling factors to achieve sustainable economic growth: empirical study of Saudi
186:106533.https://doi.org/10.1016/j.resconrec.2022.106533 Arabia.TechnolForecastSocChange187:122184.https://doi.org/10.1016/j.
Pradhan B, Lee S (2010) Landslide susceptibility assessment and factor effect techfore.2022.122184
analysis: backpropagation artificial neural networks and their comparison WendorfCA(2002)Comparisonsofstructuralequationmodelingandhierarchical
with frequency ratio and bivariate logistic regression modelling. Environ linearmodelingapproachestocouples’data.StructEquModeling:AMul-
ModelSoftw25(6):747–759.https://doi.org/10.1016/j.envsoft.2009.10.016 tidiscipJ9(1):126–140.https://doi.org/10.1207/s15328007sem0901_7
Pranta AD, Tareque Rahaman Md, Reazuddin Repon Md, Shikder AA (2024) WoodyE(2011)AnSEMperspectiveonevaluatingmediation:whateveryclinical
Environmentally sustainable apparel merchandising of recycled cotton- researcherneedstoknow.JExpPsychopathol2(2):210–251.https://doi.org/
polyester blended garments: Analysis of consumer preferences and pur- 10.5127/jep.010410
chasing behaviors. J Open Innov: Technol Mark Complex 10(3):100357. XiangyangL,XingQ,HanZ,FengC(2023)Anovelactivationfunctionofdeep
https://doi.org/10.1016/j.joitmc.2024.100357 neuralnetwork.SciProgram2023:1–12.https://doi.org/10.1155/2023/3873561
Provin AP, Dutra AR, de Sousa e Silva Gouveia IC, Cubas EA (2021) Circular XuY,DuJ,KhanMA,JinS,AltafM,AnwarF,SharifI(2022)Effectsofsubjective
economyforfashionindustry:useofwastefromthefoodindustryforthe norms and environmental mechanism on Green Purchase Behavior: an
productionofBiotextiles.TechnolForecastSocChange169:120858.https:// extendedmodeloftheoryofplannedbehavior.FrontEnvironSci10.https://
doi.org/10.1016/j.techfore.2021.120858 doi.org/10.3389/fenvs.2022.779629
QiX,PloegerA(2019)Explainingconsumers’intentionstowardspurchasinggreen YousefzadehM,HosseiniSA,FarnaghiM(2021)Spatiotemporallyexplicitearth-
foodinQingdao,China:theAmendmentandextensionofthetheoryofplanned quake prediction using Deep Neural Network. Soil Dyn Earthq Eng
behavior.Appetite133:414–422.https://doi.org/10.1016/j.appet.2018.12.004 144:106663.https://doi.org/10.1016/j.soildyn.2021.106663
RauschTM,KopplinCS(2021)Bridgethegap:consumers’purchaseintentionand ZhangB,ZhangY,ZhouP(2021)Consumerattitudetowardssustainabilityoffast
behaviorregardingsustainableclothing.JCleanProd278:123882.https://doi. fashion products in the UK. Sustainability 13(4):1646. https://doi.org/10.
org/10.1016/j.jclepro.2020.123882 3390/su13041646
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 17

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
ZhangL,FanY,ZhangW,ZhangS(2019)Extendingthetheoryofplannedbehavior standardofthe1964HelsinkiDeclaration.Thedataentailsnotraceableinformation
toexplaintheeffectsofcognitivefactorsacrossdifferentkindsofgreenpro- amongrespondentsandwaskeptinasecuredatabase.ThiswasapprovedbyDr.
ducts.Sustainability11(15):4222.https://doi.org/10.3390/su11154222 JosephineD.German(committeemember)andDr.MichaelN.Young(committeehead)
Zhang Z, Malik MZ, Khan A, Ali N, Malik S, Bilal M (2022) Environmental onMarch20,2023.
impactsofhazardouswaste,andmanagementstrategiestoreconcilecircular
economy and eco-sustainability. Sci Total Environ 807:150856. https://doi. Informed consent
org/10.1016/j.scitotenv.2021.150856
Informedconsentwasobtainedfromallsubjectsthroughwrittenform,involvedinthis
study(FM-RC-22-02-01)duringthedatacollectionprocessfromMarch27,2023—
Acknowledgements August2023.Inaccordance,aconfirmationquestionofapprovalamongrespondents
werecollectedasthefirstquestionintheonlinequestionnairetoensureapproval.
ThisresearchwasfundedbyUniversityDirectedResearchforInnovationandValue
Participantswereassuredthattraceableinformationwouldnotbecollected,response
Enhancement(DRIVE).
wouldbeanonymous,andtheirdataprivacywillbesecured.
Author contributions
Additional information
CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.
SupplementaryinformationTheonlineversioncontainssupplementarymaterial
Cahigas,Ma.JaniceJ.Gumasing:Conceptualization;CarmellaAndreaL.Cabrera,
availableathttps://doi.org/10.1057/s41599-025-05205-z.
ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.
Gumasing:Datacuration;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,John
CorrespondenceandrequestsformaterialsshouldbeaddressedtoArdvinKesterS.Ong.
FrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Formalanalysis;
ArdvinKesterS.Ong:Fundingacquisition;CarmellaAndreaL.Cabrera,ArdvinKester
Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
S.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Inves-
tigation;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong:Methodology;ArdvinKester Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
S.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Project publishedmapsandinstitutionalaffiliations.
administration;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz:
Resources;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,
MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Software;ArdvinKesterS.Ong,John
Open Access This article is licensed under a Creative Commons
FrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Supervision;Carmella
AndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas, Attribution-NonCommercial-NoDerivatives 4.0 International License,
Ma.JaniceJ.Gumasing:Validation;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong, whichpermitsanynon-commercialuse,sharing,distributionandreproductioninany
JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Visualization; mediumorformat,aslongasyougiveappropriatecredittotheoriginalauthor(s)and
CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.
thesource,providealinktotheCreativeCommonslicence,andindicateifyoumodified
Cahigas,Ma.JaniceJ.Gumasing:Roles/Writing–originaldraft;CarmellaAndreaL. thelicensedmaterial.Youdonothavepermissionunderthislicencetoshareadapted
Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.Janice materialderivedfromthisarticleorpartsofit.Theimagesorotherthirdpartymaterial
J.Gumasing:Writing-review&editing.
inthisarticleareincludedinthearticle’sCreativeCommonslicence,unlessindicated
otherwise in a credit line to the material. If material is not included in the article’s
Creative Commons licence and your intended use is not permitted by statutory
Competing interests
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Theauthorsdeclarenocompetinginterests. thecopyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/
licenses/by-nc-nd/4.0/.
Ethical approval
ThisstudywasapprovedbytheMapuaUniversityResearchEthicsCommittees(FM-RC-
©TheAuthor(s)2025
22-01-01),followingproperrelevantguidelinescuratedbytheuniversityandtheethical
18 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z