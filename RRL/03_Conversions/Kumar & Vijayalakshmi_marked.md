ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188
PREDICTIVE MODELING FOR LOAN APPROVAL: A MACHINE
LEARNING APPROACH
Valmiki Sarath Kumar1, K. Vijayalakshmi2
1Schoolof Computer Science and Applications, REVA University, Bangalore, Karnataka, India
2School of Computer Science and Applications, REVA University, Bangalore, Karnataka, India
Article DOI: https://doi.org/10.36713/epra17042
DOI No: 10.36713/epra17042
ABSTRACT
Exploring machine learning approaches to enhance the effectiveness and precision of procedures related to bank loan approval. This
investigation encompasses various methods such as logistic regression, decision trees, linear regression, as well as GaussianNB,
Random Forest, and SVM. Utilizing a substantial dataset containing past loan applications and diverse applicant attributes like
demographics, credit scores, income levels, and employment histories. The research endeavors to evaluate the recall, accuracy,
precision, and F1-score metrics of various algorithms. Additionally, it investigates the interpretability and transparency of machine
learning models to offer further insight into the variables affecting decisions on loan acceptance. The study emphasizes the efficacy
of logistic regression, which outperformed SVM (77%), GaussianNB (78%), random forests (78%), and decision trees (69%),
achieving the highest accuracy of 80% in loan approval. By implementing this model, we can enhance ML-driven loan approval
processes within the banking industry, thereby elevating decision-making standards and enhancing consumer satisfaction.
KEYWORDS— Machine Learning Algorithms, Loan Approval, LogisticRegression, DecisionTree, Linear Regression,
GaussianNB, RandomForest, SupportVectorMachine (SVM), Decision-Making,
I. INTRODUCTION Data mining techniques prove invaluable in this domain
The loan approval process holds significance for both involving the extraction of valuable insights from vast and
lenders and applicants. Traditional evaluation methods, unorganized datasets. These insights aid decision-making
while somewhat effective in specific scenarios, often fall processes by executing crucial operations. In the realm of
short in meeting the rapid and accurate demands of the loan approval prediction numerous conventional data mining
contemporary market. This is where predictive modeling techniques exist alongside machine learning algorithms
powered by machine learning stands out as an innovative designed to automate the prediction of loan statuses. These
solution. The foremost priority for any bank is to guarantee algorithms effectively and quickly determine loan eligibility.
the security of its assets [1]. In the digital era, the banking Among them are decision trees, logistic regression, random
industry heavily relies on advanced technologies. Debt is forests, and gradient boosting. This study aims to mitigate
widely regarded as the primary service provided by financial the risk linked to loan approval by predicting the loan status
institutions and a significant revenue stream for companies. through analysis of various loan attributes or characteristics.
The assessment of credit risk emerges as a critical factor The Loan Prediction System assigns weight to each attribute
demanding meticulous attention [2]. Daily a considerable involved in loan processing automatically. These weights are
number of individuals apply for personal loans with many then applied to newly acquired test data during processing
receiving them from different institutions. Interest-free loans [5]. Loan prediction offers significant advantages for banks,
constitute the primary revenue stream for banks [3]. employees, and applicants alike. The primary goal of this
Machine learning (ML), a subset of artificial intelligence work is to offer a practical and effective approach for
(AI) investigates statistical models and techniques enabling selecting the optimal course of action. With the loan
computers to learn from data, thereby making predictions or prediction system's ability to automatically assess the
assessments without explicit programming. This process is importance of each parameter, users can make optimal
often termed as teaching computers to perform tasks more decisions. We can schedule appointments to review
autonomously relies on data or expertise. It encompasses customer status and ascertain their eligibility. The system
analyzing data using statistical models and algorithms to efficiently prioritizes specific applications for assessment.
recognize patterns and draw conclusions or predictions. The target audience for this study report is the governing
Machine learning methods are essential for constructing authority of banks or financial institutions. It's important to
models that reliably categorize loan applicants according to note that the process remains confidential with no ability for
their ability to repay loans [4]. any involved parties to alter it.
2024 EPRA IJMR | http://eprajournals.com/ | Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------650

ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188
II.LITERATURE REVIEW supervised learning techniques, specifically random forest,
To determine the likelihood of approval for a bank loan and logistic regression algorithms, leveraging application
Vandana Sharma et al [6] investigates the feasibility of data. The report underscores the indispensability of artificial
employing ML techniques for credit risk assessment amidst intelligence (AI) in expediting banking operations and
persistent worries regarding loan defaults. It scrutinizes mitigating risks linked to manual assessments. Through
existing methodologies and underscores the significance of feature engineering and data preprocessing, the study
precise credit evaluation, particularly given the rising constructs a dataset encompassing credit history, income,
prominence of peer-to-peer lending platforms. To enhance and educational background. It underscores the significance
predictive efficacy, the proposed model incorporates logistic of predictive analytics in augmenting decision-making
regression, feature engineering, and data refinement. processes and curbing fraudulent activities, advocating for
Nevertheless, it acknowledges various potential limitations the advancement and integration of such systems in
such as issues concerning data integrity, logistic regression's forthcoming endeavors.
limitations in detecting complex relationships, and the
model's dependence on specific datasets and credit scoring Praveen Tumuluru et al [11] Analyzes the application of
mechanisms. machine learning methods for predicting loan defaults, a
critical issue affecting the overall financial stability and
Mohammad Ahmad Sheikh et al [7] study report underscores success of banks. The research evaluates various techniques
the importance of accurate predictions for maximizing profits including Random Forest, Support Vector Machine, K-
in the banking industry through the application of logistic Nearest Neighbor, and Logistic Regression to evaluate the
regression. It leverages Kaggle data and focuses on customer risk involved in loan approval decisions. Its central premise
attribute beyond mere account validation. The proposed is that automating the process reduces bank risk and losses.
methodology mitigates default risks and enhances operational Random Forest emerges as the top performer, achieving an
efficiency and customer contentment by automating loan accuracy of 81% in predicting loan approval, suggesting its
approval procedures. Apart from feature engineering and
potential for future loan forecasting. The research
preprocessing missing variable imputation is employed.
recommends exploring additional machine learning
Logistic regression is selected as the model due to its
approaches to enhance prediction accuracy further. Krishna
commendable accuracy of 0.811 on the test dataset and its
Mridha et al [12] delves into the utilization of machine
effectiveness in classification endeavours.
learning algorithms by financial institutions to streamline the
Nancy Deborah R et al [8] delves into the potential uses of
loan approval process, thereby mitigating risks associated
machine learning methods, such as Support Vector
with customer behavior. It examines various classification
Classifiers (SVM), in predicting loan approval status. SVM
techniques, such as logistic regression, and assesses the
exhibited an 83% accuracy rate in this context. The research
underscores the importance of employing dependable accuracy of each model using data sourced from Kaggle.
prediction models when addressing the obstacles banks Future investigations will focus on crafting a hybrid model
encounter in evaluating loan applications and mitigating that integrates deep learning methodologies to enhance
credit risk. It underscores the significance of considering prediction accuracy while emphasizing crucial features
various factors to achieve precise forecasts of loan status, related to loan repayment capacity.
including data quality, hyperparameter tuning, and potential
biases in both data and models. Furthermore, it illustrates how Trishita Saha et al [13] delves into the utilization of machine
SVM serves as a valuable tool that can be enhanced over time learning algorithms by financial institutions to streamline the
by incorporating new features and data sources to enhance loan approval process, thereby mitigating risks associated
prediction accuracy and adaptability to evolving market with customer behavior. It examines various classification
dynamics. techniques, such as logistic regression, and assesses the
accuracy of each model using data sourced from Kaggle.
Sk. Sharmila et al [9] study delves into utilizing a Decision
Future investigations will focus on crafting a hybrid model
Tree Classifier for bank loan approval, presenting a fresh
that integrates deep learning methodologies to enhance
perspective on loan prediction. It underscores the growing
prediction accuracy while emphasizing crucial features
inclination towards employing machine learning models in
related to loan repayment capacity. Ch. Naveen kumar et al
loan assessment and the demand for more effective decision-
[14] the importance of loan management within the banking
making algorithms. The research advocates for the Decision
sector, particularly examining the impact of defaults on bank
Tree method citing its clarity and effectiveness, while
profitability. It underscores the vital nature of accurately
scrutinizing conventional techniques such as linear
predicting loan defaulters and emphasizes the growing role
regression and Gaussian Naive Bayes. Following training on
of machine learning techniques in addressing this challenge.
past loan data, the suggested model exhibits significant
Additionally, it underscores the necessity for innovative
promise in expediting loan approval procedures, boasting an
approaches to enhance the precision of loan eligibility
impressive accuracy rate of 95% and minimal loss at 0.09%.
prediction, alongside outlining several existing industry
Anshika Gupta et al [10] utilizes machine learning methods
practices. Gaurav Parmar et al [15] the specific study article,
to tackle the increasing need for streamlined loan approval
previous research on data rebalancing methods aimed at
procedures within the banking sector. It focuses on
mitigating bias in sensitive categories such as age, gender,
forecasting the likelihood of loan approval through
2024 EPRA IJMR | http://eprajournals.com/ | Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------651

                                                                                                                                          ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188

and race would certainly be referenced. This review would  the model on the test data. In this Dataset we have 12
scrutinize  the  limitations  of  existing  techniques  and  columns and 614 customer records. All these records are in
underscore the risks associated with both overfitting and  the csv format. We can use panda’s library for reading the
underfitting machine learning models.   file and by using python we can apply all the algorithms. In
|     |     |     |     | that  dataset  | Status  is  | the  target  variable  | and  the  other  |
| --- | --- | --- | --- | -------------- | ----------- | ---------------------- | ---------------- |
III.  METHODOLOGY  variables-  “Gender”,  “Married”,  “Dependents”,
The loan approval prediction strategy utilizes statistical  “Education”, “Self-Employed”, “Applicant Income”, “Co-
methods and historical data to forecast the outcome of loan  applicant  Income”,  “Loan  Amount”,  “Term”,  “Credit
approval. Algorithms that we are going to use in the paper is  History”, “Area”.
| Logistic  | Regression,  | Linear  Regression,  | Decision  Tree,  |     |     |     |     |
| --------- | ------------ | -------------------- | ---------------- | --- | --- | --- | --- |
SVM, Random Forest and GaussionNB. All these algorithms  TABLE I.   DATASET DESCRIPTION VARIABLES AND TYPES.
| are  trained  | on  historical  | data  to  learn  | the  relationships  |                |     |              |       |
| ------------- | --------------- | ---------------- | ------------------- | -------------- | --- | ------------ | ----- |
|               |                 |                  |                     | VARIABLE NAME  |     | DESCRIPTION  | TYPE  |
between the different factors that affect loan approval. The
|     |     |     |     | Gender  | Male / Female  |     | Character  |
| --- | --- | --- | --- | ------- | -------------- | --- | ---------- |
loan approval prediction methodology can be a valuable tool
for banks. Banks can enhance their evaluation of loan applications  Married  Applicant married (Y/N)  Character
|     |     |     |     | Dependents  | Number of dependents  |     | Integer  |
| --- | --- | --- | --- | ----------- | --------------------- | --- | -------- |
and lower the chances of loan defaults by implementing this
|     |     |     |     | Education   | Educated/ Not Education  |     | String  |
| --- | --- | --- | --- | ----------- | ------------------------ | --- | ------- |
measure.
|     |     |     |     | Self Employed  | Self Employed(Y/N)  |     | Character  |
| --- | --- | --- | --- | -------------- | ------------------- | --- | ---------- |
A. Model Planning
|     |     |     |     | Application Income  | Applicant income  |     | Integer  |
| --- | --- | --- | --- | ------------------- | ----------------- | --- | -------- |
The first step involves importing the necessary libraries as  Co-Applicant Income  Coapplicant income   Integer
|     |     |     |     | Loan Amount  | Loan amount in thousands   |     | Integer  |
| --- | --- | --- | --- | ------------ | -------------------------- | --- | -------- |
shown in “fig.1” for machine learning tasks. These packages
encompass NumPy for numerical computations, pandas for  Term  Term of loan in months  Integer
data  processing,  and  scikit-learn  for  machine  learning  Credit History  Credit history of the applicant  Integer
techniques. The next step is the data cleaning process which
|     |     |     |     | Area  | Urban/Semi Urban/Rural  |     | String  |
| --- | --- | --- | --- | ----- | ----------------------- | --- | ------- |
involves addressing concerns and ensuring data quality by
|             |                     |              |                    | Status  | Loan Approved(Y/N)  |     | Character  |
| ----------- | ------------------- | ------------ | ------------------ | ------- | ------------------- | --- | ---------- |
| performing  | dataset  cleaning.  | Data  often  | contains  errors,  |         |                     |     |            |
From the above Table I,  we can know the features of the
omissions, and inconsistencies that need to be resolved.
variables which are present in the data set. The next step is to
Following this the subsequent stage is label encoding aims  handle the null values. This is done by different methods, but
to  convert  categorical  variables  into  numerical  values  we have enough data, so we are removing the null values. All
making them compatible with models for processing. Our  the records of the applicants are in the form of categorical and
objective is to encode the categorical variables within the  numerical data. The dataset has missing values and null
dataset.  The  next  stage  divides  the  dataset  into  two  values. Before the analysis we need to normalize the dataset
categories: training and testing. The training set is utilized to  by removing the null values.
train the model while the testing set is used to assess its
C. Data preprocessing
performance on unseen data. The training set contains 0.65%
Before removing the null values, the value count of every
of the dataset, whereas the testing set contains 0.35%. The
variable that present in the data set is shown in Table II.
| training  | data  is  then  | used  to  develop  | various  machine  |     |     |     |     |
| --------- | --------------- | ------------------ | ----------------- | --- | --- | --- | --- |
learning models which include linear regression, logistic
|     |     |     |     |     | TABLE II.   | DATASET WITH NULL VALUES  |     |
| --- | --- | --- | --- | --- | ----------- | ------------------------- | --- |
regression, decision trees, random forests, support vector
machines, or Naive Bayes. After the training phase, these  Gender  601
models are assessed on a testing set to determine their  Married  611
| effectiveness with new data.  |     |     |     | Dependents           |     | 599  |     |
| ----------------------------- | --- | --- | --- | -------------------- | --- | ---- | --- |
|                               |     |     |     | Education            |     | 614  |     |
|                               |     |     |     | Self Employed        |     | 582  |     |
|                               |     |     |     | Application Income   |     | 614  |     |
|                               |     |     |     | Co-Applicant Income  |     | 614  |     |
|                               |     |     |     | Loan Amount          |     | 614  |     |
|                               |     |     |     | Term                 |     | 600  |     |
|                               |     |     |     | Credit History       |     | 564  |     |
|                               |     |     |     | Area                 |     | 614  |     |
|                               |     |     |     | Status               |     | 614  |     |
Dtype: int64

Fig. 1.  Model planning of the models
We can’t handle imbalance data and we can’t apply machine
B. Dataset  learning algorithms also to the imbalance records, so we need
For all the machine learning models we need to build models  to normalize this data by removing the null values. After
by using the dataset divide them into train and test data. We  removing the null values, the value count of every variable is
shown in Table III.
need to train the model by using train data and then applying
2024 EPRA IJMR    |  http://eprajournals.com/   |    Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------652

                                                                                                                                          ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188

|                      | TABLE III.   DATASET WITHOUT NULL VALUES  |      |     |     |     |     |     |     |     |
| -------------------- | ----------------------------------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Gender               |                                           | 499  |     |     |     |     |     |     |     |
| Married              |                                           | 499  |     |     |     |     |     |     |     |
| Dependents           |                                           | 499  |     |     |     |     |     |     |     |
| Education            |                                           | 499  |     |     |     |     |     |     |     |
| Self Employed        |                                           | 499  |     |     |     |     |     |     |     |
| Application Income   |                                           | 499  |     |     |     |     |     |     |     |
| Co-Applicant Income  |                                           | 499  |     |     |     |     |     |     |     |
| Loan Amount          |                                           | 499  |     |     |     |     |     |     |     |
| Term                 |                                           | 499  |     |     |     |     |     |     |     |
| Credit History       |                                           | 499  |     |     |     |     |     |     |     |
| Area                 |                                           | 499  |     |     |     |     |     |     |     |
| Status               |                                           | 499  |     |     |     |     |     |     |     |
Dtype: int64

Normalizing the dataset is done. The dataset contains both
training and testing segments. By using the train data, we
need to train the model and test the model by using the test
Fig. 3.  Status by Self employment
data.

|            |                   |                  |                 | The  heatmap  | correlations  |     | between  each  | variable  | in  the  |
| ---------- | ----------------- | ---------------- | --------------- | ------------- | ------------- | --- | -------------- | --------- | -------- |
| As  shown  | in  the  “fig.2”  | y-axis  depicts  | the  count  of  |               |               |     |                |           |          |
dependents,  while  the  x-axis  indicates  the  number  of  dataset are shown in "Fig.4" below. So that we can easily do
further analysis.
dependents. Individuals without dependents exhibited the
| highest   | loan  approval  | rate,  hovering  around    | 92%.  The  |     |     |     |     |     |     |
| --------- | --------------- | -------------------------- | ---------- | --- | --- | --- | --- | --- | --- |
| approval  | rate  notably   | declines  for  applicants  | with  one  |     |     |     |     |     |     |
dependent, dropping to approximately 66%. Candidates with
two or three dependents consistently experience a lower
acceptance rate (approximately 55%). For applicants with
more than three dependents, the loan approval rate is the
lowest, standing at around 28%.

Fig. 4.  Representing the correlation between attributes using the heatmap
D. Logistic Regression
|     |     |     |     | Supervised  | machine  | learning  | methods  | like  | logistic  |
| --- | --- | --- | --- | ----------- | -------- | --------- | -------- | ----- | --------- |
regression are utilized to address binary classification tasks
|     |     |     |     | by  evaluating  | the  | likelihood  | of  an  | event,  | outcome,  or  |
| --- | --- | --- | --- | --------------- | ---- | ----------- | ------- | ------- | ------------- |
observation. Equation 1 is the mathematical representation
of logistic regression. This results in a dichotomous output,

|     |     |     |     | typically  | represented  | as  true/false,  | 0/1,  | yes/no.  | Logistic  |
| --- | --- | --- | --- | ---------- | ------------ | ---------------- | ----- | -------- | --------- |
Fig. 2.  Status by Dependents  regression examines the association between independent
variables to categorize data into various groups. Commonly
As shown in “fig.3” the graph illustrates self-employment
employed in predictive modelling, this approach employs
status, with the x-axis depicting two options: "Yes" and
mathematical techniques to ascertain the probability of an
"No". It indicates a decline in self-employment, with fewer
event belonging to a specific category.
individuals opting for it. The blue bars represent the non-
| self-employed, with a maximum count of 24. The orange line  |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
denotes  the  self-employed,  peaking  at  134  individuals.  𝑓(𝑥)= 1     (1)
| Model planning of the models.  |     |     |     |     |     | 1+𝑒−𝑥 |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
2024 EPRA IJMR    |  http://eprajournals.com/   |    Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------653

                                                                                                                                          ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188

E. Decision Tree
| Decision  | trees  | serve  | as  a  supervised  | learning  | technique  |     |     |     |     |
| --------- | ------ | ------ | ------------------ | --------- | ---------- | --- | --- | --- | --- |
commonly employed for classification tasks, but they can
also address regression problems. Structurally resembling a
| tree,  they  | feature  | leaf  | nodes  | representing  | individual  |     |     |     |     |
| ------------ | -------- | ----- | ------ | ------------- | ----------- | --- | --- | --- | --- |
outcomes, decision nodes for branching decision rules, and
root nodes for dataset attributes. Comprising two types of
nodes Decision and Leaf decision trees utilize decision nodes
| for  making  | choices  | and  | leaf  | nodes  to  | display  decision  |     |     |     |     |
| ------------ | -------- | ---- | ----- | ---------- | ------------------ | --- | --- | --- | --- |
outcomes. Dataset attributes guide the testing and decision-
making process. Graphical representation of decision tree is
shown in “Fig .5”.

|     |     |     |     |     |     |     | Fig. 6.  | Random Forest  |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- |
H. Navie Bayes model GaussionNB
Gaussian Naive Bayes applies the Naive Bayes algorithm
|     |     |     |     |     |     | specifically  | to  data  that  | follows  a  normal  | (Gaussian)  |
| --- | --- | --- | --- | --- | --- | ------------- | --------------- | ------------------- | ----------- |
distribution. In this approach, it assumes that the probability
of each x_i within y_k aligns with the Gaussian Distribution,
expressed in Equation 3.

|     |     | Fig. 5.  | Decision Tree  |     |     | (𝑥−𝜇)2 |     |     |     |
| --- | --- | -------- | -------------- | --- | --- | ------ | --- | --- | --- |
−
|     |     |     |     |     |     | 𝑒 2𝜎2 |      1/(𝜎√2𝜋)=𝑃(𝑥_𝑖/𝑦)  |     |   (3)   |
| --- | --- | --- | --- | --- | --- | ----- | ----------------------- | --- | ------- |
F. Linear Regression
This approach calculates the posterior probability for
| Linear  | regression,  | a   | statistical  | technique  | commonly  |     |     |     |     |
| ------- | ------------ | --- | ------------ | ---------- | --------- | --- | --- | --- | --- |
each class and then assigns the data point to the class with
employed in machine learning and data science predictive
the highest likelihood to classify new data points.
| analysis,  | establishes  |     | a  direct  | relationship  | between  an  |     |     |     |     |
| ---------- | ------------ | --- | ---------- | ------------- | ------------ | --- | --- | --- | --- |
independent  variable,  which  remains  constant  amidst  H. Support Vector Machine (SVM)
changing factors, and a dependent variable, whose value is
Support vector machines (SVMs) play a vital role in various
| influenced  | by  | changes  | in  the  | independent  | variable.  In  |     |     |     |     |
| ----------- | --- | -------- | -------- | ------------ | -------------- | --- | --- | --- | --- |
machine learning tasks like regression, linear or nonlinear
essence, this method utilizes mathematical modelling to  classification, and outlier detection. They are indispensable
predict the values of continuous or numerical variables such  in applications such as text and image classification, facial
| as  age,  | income,  | sales,  | and  | product  price,  | employing  |                   |               |                      |       |
| --------- | -------- | ------- | ---- | ---------------- | ---------- | ----------------- | ------------- | -------------------- | ----- |
|           |          |         |      |                  |            | and  handwriting  | recognition,  | anomaly  detection,  | gene  |
supervised learning techniques to forecast outcomes.  expression analysis, and spam detection. SVMs excel in
  handling  high-dimensional  data  and  capturing  nonlinear
|     |     | +𝛽 𝑋+𝛽 |     |     | 𝑋 (2)  |     |     |     |     |
| --- | --- | ------ | --- | --- | ------ | --- | --- | --- | --- |
𝑦=𝛽 0 𝑋+ ........+𝛽 relationships,  making  them  versatile  and  robust.  These
|     |     | 1   | 2   |     | 𝑛   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  methods aim to identify the hyperplane in the feature space
Where in a linear regression model Equation 2, Y represents  that optimally separates classes, thus reducing the distance
the dependent variable, and the independent variables are  between them effectively.
| represented by X1, X2, ..., Xp. The intercept is symbolized  |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
by β0, and the slopes by β1, β2, ..., βn.  IV. MODEL EVALUATION
The model assesses an applicant's risk of defaulting on a loan
G. Random Forest
by considering various factors, such as their historical loan
The Random Forest algorithm stands as one of the most  information.  Some  key  metrics  used  to  evaluate  how
effective  machine  learning  techniques  for  tree-based  effectively  the  model  categorizes  loan  applicants  into
learning. During the training phase, it generates multiple
|     |     |     |     |     |     | accepted  | or  denied  | groups  include  recall,  | accuracy,  |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | ------------------------- | ---------- |
Decision Trees as shown in “Fig. 6”. To mitigate overfitting  precision, and F1-score.
and foster diversity, every tree is built by randomly selecting
A. Confusion Matrix
features and data samples. This approach fosters greater
A confusion matrix is a useful tool in machine learning for
variation among the trees, leading to improved prediction
performance. In regression tasks, the algorithm computes the  assessing  the  performance  of  a  classification  model  by
average output of all trees, while in classification problems,  providing insights into its accuracy. As shown in the “fig.7”
it aggregates the average votes from each tree. By integrating  It helps differentiate between true positives, true negatives,
insights  from  multiple  trees,  Random  Forest  facilitates  false  positives,  and  false  negatives,  offering  a  clear
robust  and  precise  decision-making,  ensuring  reliable  evaluation of the model's effectiveness.
outcomes [16].
2024 EPRA IJMR    |  http://eprajournals.com/   |    Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------654

                                                                                                                                          ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188

V.  RESULTS
Below Table IV displays the accuracies achieved by the
|     |     |     |     |     |     |     | decision  | tree,  random  | forest,  |     | logistic  | regression,  | support  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | -------- | --- | --------- | ------------ | -------- | --- |
vector machine, and Gaussian Naive Bayes models.
|     |     |     |     |     |     |     | TABLE IV.            | COMPARING  THE PERFORMANCE OF EACH MODEL  |     |     |     |           |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------------------------------------- | --- | --- | --- | --------- | --- | --- |
|     |     |     |     |     |     |     |                      | Algorithms                                |     |     |     | Accuracy  |     |     |
|     |     |     |     |     |     |     | Logistic Regression  |                                           |     |     |     | 80%       |     |     |
|     |     |     |     |     |     |     | Decision Tree        |                                           |     |     |     | 69%       |     |     |

|     |     |          |                  |     |     |     | Random Forest  |      |     |     |     | 78%  |     |     |
| --- | --- | -------- | ---------------- | --- | --- | --- | -------------- | ---- | --- | --- | --- | ---- | --- | --- |
|     |     | Fig. 7.  | Confusion Mtrix  |     |     |     |                |      |     |     |     |      |     |     |
|     |     |          |                  |     |     |     | GaussianNB     |      |     |     |     | 78%  |     |     |
|     |     |          |                  |     |     |     |                | SVM  |     |     |     | 77%  |     |     |
B. Accuracy
| The  accuracy  | of         | the  model  | has    | been         | evaluated  | using  |            |      |                                          |     |     |        |     |     |
| -------------- | ---------- | ----------- | ------ | ------------ | ---------- | ------ | ---------- | ---- | ---------------------------------------- | --- | --- | ------ | --- | --- |
|                |            |             |        |              |            |        | TABLE V.   |      | LINEAR REGRESSION MODEL METRICS RESULTS  |     |     |        |     |     |
| predetermined  | measures.  |             | While  | a  balanced  | class      | model  |            |      |                                          |     |     |        |     |     |
|                |            |             |        |              |            |        |            | MSE  |                                          |     |     | 0.154  |     |     |
exhibits outstanding accuracy, an imbalanced class model
|                     |     |                |     |      |               |     |                  | RMSE  |     |     |     | 0.392  |     |     |
| ------------------- | --- | -------------- | --- | ---- | ------------- | --- | ---------------- | ----- | --- | --- | --- | ------ | --- | --- |
| shows  significant  |     | inaccuracies.  |     | The  | mathematical  |     |                  |       |     |     |     |        |     |     |
|                     |     |                |     |      |               |     | Train Set Score  |       |     |     |     | 0.27   |     |     |
representation of accuracy is represented as Equation 4.
|     |     |     |     |     |     |     | Test Set Score  |     |     |     |     | 0.32  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | ----- | --- | --- |

|          |     |       |     |     |     |      | Among  | various  | machine  | learning  | techniques  |     | evaluated,  |     |
| -------- | --- | ----- | --- | --- | --- | ---- | ------ | -------- | -------- | --------- | ----------- | --- | ----------- | --- |
| 𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 | =   | 𝑇𝑃+𝑇𝑁 |     |     |     | (4)  |        |          |          |           |             |     |             |     |
logistic regression exhibited the highest accuracy at 80%,
𝑇𝑃+𝑇𝑁+𝐹𝑃+𝐹𝑁
|     |     |     |     |     |     |     | surpassing SVM (77%), GaussianNB (78%), random forests  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
C. Precision:  (78%), and decision trees (69%). Notably, linear regression
displayed inferior performance based on metrics like MSE,
| The  forecast  | accuracy  |     | level  of  | an  optimistic  |     | model  is  |     |     |     |     |     |     |     |     |
| -------------- | --------- | --- | ---------- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
RMSE, and scores. Particularly in predicting loan approvals,
determined by Equation 5. By dividing the total number of
logistic regression emerged as the most accurate model.
| correctly predicted positive outcomes by the total number of  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
positive outcomes incorrectly forecasted.
VI. CONCLUSION

|     |     |     |     |     |     |     | In  the  loan  | approval  | project,  |     | several  | machine  | learning  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --------- | --- | -------- | -------- | --------- | --- |
𝑇𝑃
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =      (5)  models were evaluated, and logistic regression emerged as
𝑇𝑃+𝐹𝑃
|     |     |     |     |     |     |     | the most accurate model with an accuracy of 80%. The  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
D. Recall:  logistic  regression  model  demonstrated  superior
performance compared to the SVM, Decision Tree, Random
| Recall  value,  | also  | known  | as  | sensitivity,  | measures  | the  |                       |     |      |         |             |     |         |     |
| --------------- | ----- | ------ | --- | ------------- | --------- | ---- | --------------------- | --- | ---- | ------- | ----------- | --- | ------- | --- |
|                 |       |        |     |               |           |      | Forest,  GaussianNB,  |     | and  | Linear  | Regression  |     | models  | in  |
proportion of correctly identified positive events compared
|     |     |     |     |     |     |     | accurately  | predicting  | loan  | approval.  |     | There  | are  several  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ----- | ---------- | --- | ------ | ------------- | --- |
to all actual positive cases. In Formula 6, the denominator,
reasons why the logistic regression model has achieved
(TP + FN), signifies the total number of positive instances.
|     |     |     |     |     |     |     | higher  accuracy.  |     | Originally,  |     | logistic  | regression  |     | was  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------ | --- | --------- | ----------- | --- | ---- |
This metric enhances identification accuracy and influences
|                   |     |          |        |              |     |           | frequently  | and  | consistently  | employed  |     | to  address  |     | binary  |
| ----------------- | --- | -------- | ------ | ------------ | --- | --------- | ----------- | ---- | ------------- | --------- | --- | ------------ | --- | ------- |
| the  probability  |     | of  the  | model  | overlooking  |     | positive  |             |      |               |           |     |              |     |         |
classification problems. It serves as an effective tool for
occurrences.  determining whether to accept or reject something, as it is

specifically designed to estimate the probability of an event
𝑇𝑃
𝑅𝑒𝑐𝑎𝑙𝑙(𝑆𝑒𝑛𝑠𝑖𝑡𝑖𝑣𝑖𝑡𝑦)=                (6)  occurring.  Logistic  regression  tends  to  exhibit  lower
𝑇𝑃+𝐹𝑁
|     |     |     |     |     |     |     | overfitting  | compared  | to  | more  | complex  | models  | such  | as  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ----- | -------- | ------- | ----- | --- |

E. F1 Score:  decision trees and random forests. When a model learns the
training dataset too well, it is said to be overfitting and has
The F1 Score serves as a key indicator of a model's optimal
|     |     |     |     |     |     |     | poor  generalization  |     | to  | new  data.  | Logistic  | regression  |     | is  |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ----------- | --------- | ----------- | --- | --- |
performance level, being a harmonic mean of recall and
efficient and somewhat understandable compared to other
accuracy. Attaining the highest F1 Score necessitates high
models like support vector machines (SVM) or random
values for both recall and accuracy. Any declines in either
forests. If the relationship between the input variables and
recall or accuracy can lead to a notable decrease in the final  the  loan  approval  decision  is  relatively  linear,  logistic
F1 score. Equation 7 for the F1 Score employs the sum of
regression can effectively capture this pattern and make
recall and accuracy as its numerator. Consequently, a model
accurate predictions. In conclusion, the loan approval project
| that  effectively  |     | predicts  | positive  | events  | and  | avoids  |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | --------- | ------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
found that logistic regression outperformed other models,
| underestimating  | positives  |     | by  | predicting  | negatives  | can  |     |     |     |     |     |     |     |     |
| ---------------- | ---------- | --- | --- | ----------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
achieving the highest accuracy with 80%.From the proper
achieve a high F1 score (accuracy + recall).
|     |     |     |     |     |     |     | view  of  | analysis  | this  system  |     | can  be  | used  | perfectly for  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------- | --- | -------- | ----- | -------------- | --- |

detection of clients who are eligible for approval of loan. In
2𝑇𝑃
| 𝐹1−𝑆𝑐𝑜𝑟𝑒 |     | =   |     |     |     | (7)  |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
the future, there may be opportunities to expand upon this
2𝑇𝑃+𝐹𝑃+𝐹𝑁
  research further, leading to improved software upgrades that
|     |     |     |     |     |     |     | enhance correctness, security, and reliability.  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
2024 EPRA IJMR    |  http://eprajournals.com/   |    Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------655

ISSN (Online): 2455-3662
EPRA International Journal of Multidisciplinary Research (IJMR) - Peer Reviewed Journal
Volume: 10| Issue: 5| May 2024|| Journal DOI: 10.36713/epra2013 || SJIF Impact Factor 2024: 8.402 || ISI Value: 1.188
VII. REFERENCES Engineering SVIT, Nashik Maharashtra, India. 5
1. Suliman Mohamed Fati, “Machine Learning-Based Information Technology (Assistant Proffessor) SVIT, Nashik
Prediction Model for Loan Status Approval”,2021. Maharashtra, India an Approach for Prediction of Loan
2. Malika Becha, Olfa Dridi, Oumayma Riabi, Yasmine Approval Using Machine Learning Algorithm 2021.
Benmessaoud, “Use of Machine Learning Techniques in 20. Mahankali Gopinatha K. Srinivas Shankar Maheep and R.
Financial Forecasting”, 2020. Sethuraman, 2021 proposed Customer Loan Approval
3. C. Prasanth, R. Praveen Kumar, A. Rangesh, N. Sasmitha, Prediction Using Logistic Regression, Smart Intelligent
Dhiyanesh B,” Intelligent Loan Eligibility and Approval Computing and Communication Technology.
System based on Random Forest Algorithm using Machine
Learning”,2023.
4. Hamid, A.J., and Ahmed, T.M. “Developing prediction
model of loan risk in banks using data mining”, 2016.
5. Kumar Arun, Garg Ishan, Kaur Sanmeet,” Loan Approval
Prediction based on Machine Learning Approach”, 2016.
6. Vandana Sharma, Amit Singh, Ashendra Kumar Saxena and
Vineet Saxena” A Logistic Regression Based Credit Risk
Assessment Using WoE Bining and Enhanced Feature
Engineering Approach ANOVA and Chi-Square”,2023.
7. Mohammad Ahmad Sheikh, Amit Kumar Goel, Tapas
Kumar,” An Approach for Prediction of Loan Approval
using Machine Learning Algorithm”,2020.
8. Nancy Deborah R, Alwyn Rajiv S, Vinora A, Manjula Devi
C, Mohammed Arif S, Mohammed Arif G S,” An Efficient
Loan Approval Status Prediction Using Machine
Learning”,2023.
9. Sk. Sharmila, P V S Sandhya, P. Suhani kousar, P.
Anuradha, S. Deekshitha,” Bank Loan Approval using
Machine Learning”, 2024.
10. Anshika Gupta, Vinay Pant , Sudhanshu Kumar and
Pravesh Kumar Bansal,” Bank Loan Prediction System
using Machine Learning”,2020.
11. Praveen Tumuluru, Lakshmi Ramani Burra, M.Loukya,
S.Bhavana, CH.M.H.SaiBaba, N Sunanda,” Comparative
Analysis of Customer Loan Approval Prediction using
Machine Learning Algorithms”,2022.
12. Krishna Mridha, Dipayan Barua, Meghla Monir Shorna,
Hasan Nouman Nouman, Md Hasanul Kabir, Ajay Vikram
Singh, “Credit Approval Decision using Machine Learning
Algorithms”,2022.
13. Trishita Saha, Saroj Kumar Biswas, Saptarsi Sanyal, Neeta
Verma, Biswajit Purkayastha, “Credit Risk Prediction using
Extra Tree Ensembling Technique with Genetic Algorithm”,
2023.
14. Ch. Naveen kumar, D. keerthana , M Kavitha , M Kalyani,
“Customer Loan Eligibility Prediction using Machine
Learning Algorithms in Banking Sector”,2022.
15. Gaurav Parmar, Rimi Gupta, Tejas Bhatt, G.J. Sahani,
Brijeshkumar Y. Panchal, Hiren Patel, “Data Re-Balancing
using Fuzzy Clustering and SMOT Mechanism”,2023.
16. Kusumlata Bhatt, Pranchal Sharma, Megha Verma, Dr
Kadambri Agarwal, “Loan Status Prediction in the Banking
Sector using Machine Learning”,2023.
17. Kumar Arun et al., 2021 proposed Loan Approval Prediction
based on Machine Learning Approach, OSR Journal of
Computer Engineering (IOSR-JCE).
18. Ramachandra H V et al., 2021 proposed Design and
Simulation of Loan Approval Prediction Model using AWS
Platform, International Conference on Emerging Smart
Computing and Informatics (ESCI).
19. Ms. Kathe Rutika Pramod1, Ms. Dapse Punam Laxman2,
Ms. Panhale Sakshi Dattatray3, Ms. Avhad Pooja Prakash4,
Mr. Ghorpade Dinesh B.5, 1-4 Information Technology
2024 EPRA IJMR | http://eprajournals.com/ | Journal DOI URL: https://doi.org/10.36713/epra2013 -------------------------------------------------------------656