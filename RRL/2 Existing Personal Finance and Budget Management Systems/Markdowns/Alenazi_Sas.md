---
designation: international
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
conversion_date: 2026-04-24
original_filename: "Creatingandmanagingtransactionsandbudget.pdf"
document_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
version: "1.0"
---

# Creating and Managing Transactions and Budgets: Analysis of Marketplace Descriptions and Functionality Review of Budgeting Apps

Mariam Alenazi\* and Corina Sas

Computing and Communications, Lancaster University, InfoLab21, Lancaster LA1 4WA, UK \*Corresponding author: m.alenazi@lancaster.ac.uk

## Abstract

While financial practices permeate our lives, the effective management of personal finance is not trivial, as indicated in the increasing number of commercial apps aimed to support budgeting. Such apps however have been limitedly explored, despite the growing HCI interest in financial practices. To address this gap, we present the functionality review of 45 top- rated budgeting apps from Google Play and Apple Store, together with an analysis of their descriptions on marketplaces. Findings indicate the value of richer, multimodal app descriptions, support for budgeting literacy and for stronger theoretical underpinning of these apps. They also highlight main functionalities for supporting different types of transactions and accounts, for entering and managing transactions, securing data, as well as for creating and managing budgets. We conclude with five design implications to better support each of these functionalities.

## RESEARCH HIGHLIGHTS

An analysis of apps' descriptions on marketplaces, and functionality review of 45 top- rated budgeting apps was conducted to explore their main functionalities. Analysis of their descriptions on marketplaces indicates that budgeting apps can benefit from increased accessibility across platforms and devices, stronger theoretical underpinning and from richer, multimodal app descriptions including information on main functionalities, their costing and budgeting literacy. Functionality review indicates eight functionalities concerning types of transactions and transaction accounts, creating budgets, entering transactions, securing data access and storage, managing transactions and budgets and three strategies for managing budgets. Strategies for managing budgets include supporting users' awareness of their ongoing spending within budgets, of approaching budgets' thresholds and of exceeding budgets' amounts. Findings inform the design of budgeting apps through five design implications aimed to support different types of transactions and accounts, flexible enter and management of transactions, secure data access and storage, creation and management of multiple budgets and support for the three strategies for managing budgets.

**Keywords:** financial behaviours; budgeting apps; money envelopes; budgeting; tracking transactions

## 1. INTRODUCTION

Most HCI research on financial behaviour included initial exploratory studies for understanding financial practices, which has shown people's limited use of digital tools (Kaye et al., 2014; Vines et al., 2014; Snow and Vyas, 2015b; Vyas et al., 2016; Lewis and Perry, 2019). Thus, we know little about how digital tools such as commercial apps for personal budgeting may support financial practises. This gap is indeed surprising given the growing number of commercial apps in this space.

The financial domain was amongst the first to adapt mobile technologies (Jun and Palacios, 2016). Here, financial apps have become increasingly popular, growing steadily in numbers, and with a $50\%$ increase in number of downloads compared to 2022 (Shrestha, 2023). Besides apps for mobile banking, financial management apps aimed to track expenses and support budgeting are amongst the fastest growing apps in the finance category on marketplaces (Bitrián et al., 2021), with a global return estimated to double by 2025 from its 2018 figure (Qyresearch, 2024).

Although the functionalities of commercial apps have started to be explored in HCI research in domains such as digital wellbeing (Almoallim and Sas, 2022), depression (Qu et al., 2020), diet (Zaidan and Roehrer, 2016), fitness (Chung et al., 2018) or personal goals (Lolla and Sas, 2023), budgeting apps have been less explored (Alenazi and Sas, 2023).

This paper aims to address this gap through an exploration of 45 top- rated commercial apps for personal budgeting. For this we employ the theoretical perspective of mental accounting theory (Thaler, 1999). Thaler (1999) introduced mental accounting as cognitive operations that people commonly employ to budget and partition their money for specific purposes, i.e. money envelopes. As the economist Thaler (Thaler, 1999) stated, the main purpose of mental accounting is to use categories names for sources such as regular income and uses of funds such as food, to help individuals and households organize, track and monitor their spending.

The larger angles that the use of mental accounting helped people to organize, track and monitor their financial activities by categorizing funds and expenditures (Thaler, 1999). Therefore, our study is grounded in the mental accounting theory. In particular, we explored the functionalities of the top- rated budgeting apps and how these functionalities align with the key concepts of mental accounting theory. Thus, the objectives of this paper are to identify these functionalities as well as the novel design implications that can better support them. For this, we focused on the following research questions:

How should budgeting apps be described on marketplaces? Which are the main functionalities of budgeting apps? What design implications can best support these functionalities?

Our paper makes a 3- fold contribution. First, we highlight eight functionalities of budgeting apps, which include: (1) supporting different types of transaction accounts, (2) supporting different transaction types, (3) supporting different forms of entering transactions, (4) securing data access and storage, (5) managing transactions through different options, (6) creating different types of budgets, (7) managing budgets through different options and (8) supporting strategies for managing budgets.

Second, we identified three specific strategies for managing budgets, which include: (1) supporting users' awareness of ongoing spending within budgets, (2) supporting users' awareness before reaching budgets' limit and (3) providing signals for spending over budgets' limits.

Third, grounded in our findings, we generated five design implications for budgeting apps to better support the identified functionalities.

This paper extends our previous work (Alenazi and Sas, 2023) on functionality review of 45 budgeting apps which highlighted types of transactions and of transaction accounts, as well as types of budgets such as single or multiple.

## 2. BACKGROUND

Our work draws from HCI research on financial behaviour, and of key concepts from mental accounting theory.

### 2.1. HCI research on financial behaviour

Most HCI research pertaining to financial behaviour has primarily focused on analysing the practices of individuals (Kaye et al., 2014; Vines et al., 2014; Lewis and Perry, 2019) and households (Vyas et al., 2015; Snow and Vyas, 2015a, 2015b; Vyas et al., 2016), as well as their preferred tools for tracking such behaviours. Key findings from such exploratory studies revealed that analogue tools were common and preferred rather than digital ones. Amongst the analogue tools, the most common ones include coin jars or paper envelopes (Vyas et al., 2015; Snow and Vyas, 2015a), which people use to budget by allocating amounts of money to specific envelopes such as rent, and to track their expenditures. Given their simplicity, other prevalent analogue tools for budgeting and expense tracking include bills attached to refrigerator, handwritten diaries or folders and wall organizers (Kaye et al., 2014; Vyas et al., 2015; Snow and Vyas, 2015a, 2015b; Vyas et al., 2016).

In sharp contrast to these findings on the extensive use of analogue tools for everyday financial practices, previous HCI work has shown limited use of digital tools. Amongst the latter, previous findings indicate the use of spreadsheets for tracking transactions albeit less for budgeting purposes. Previous outcomes also indicate the use of banking apps (Snow and Vyas, 2015a) for tracking transactions, and again, limited use of budgeting apps, which people tend to discontinue given the difficulties associated with entering expenses into the apps and the lack of perceived control over their spending.

Previous studies have explored the positive impact of using personal finance apps for different goals such as improving financial decision- making or financial literacy of low- income households (French et al., 2021). Other study explored the positive role of gamification for increasing users' motivation for personal financial management apps (Bitrián et al., 2021). However, the functionalities of these personal finance apps have been less explored. A noticeable exception is a recent HCI study (Alenazi and Sas, 2023) focused on functionality review of budgeting apps; however, its findings were limited to some of the features pertaining to tracking and budgeting functionalities.

Therefore, our study addresses the limitation of previous work by first, exploring the descriptions in marketplaces of 45 top- rated budgeting apps, and second, through a review of their functionalities. Our findings extend previous work (Alenazi and Sas, 2023) through new aspects of tracking and budgeting functionalities such as securing data access and storage, managing transactions, managing budgets and strategies for managing budgets.

### 2.2. Mental accounting theory

While the increased HCI interest in financial behaviour has started to lay the empirical foundation in this space, theoretical foundation is yet limited, particularly from the perspective of mental accounting (Thaler, 1999) as a behavioural economics theory. The mental accounting theory has been developed in behavioural economics with the aim of describing how individuals categorize, evaluate and make financial decisions based on their financial resources. It indicates that individuals tend to mentally separate their funds into different categories, for which they allocate specific budgets, such as groceries budget (Thaler, 1999).

Mental accounting theory has started to be leveraged in HCI research. Efforts in this direction include emerging HCI work exploring the value of behaviour economics for digital well- being (Park et al., 2021) or healthy choices (Lee et al., 2011), as well as for broader financial practices such as savings (Stockinger et al., 2013), including retirement savings (Gunaratne and Nov, 2015). However, its application to exploring financial apps has been limited (Alenazi and Sas, 2023).

To conclude, previous HCI research on financial behaviour has predominantly focused on the use of traditional analogue tools for budgeting such as envelopes, while the use of digital tools has been limited to tracking expenses rather than budgeting. We have also seen limited emphasis in previous work on digital tools, particularly budgeting apps. Although behavioural economics theories have started to be investigated in HCI, the value of mental accounting theory for budgeting apps has been limitedly explored.

## 3. METHOD

The budgeting apps were identified through searching for the free apps in the two marketplaces in the UK: Google Play Store and Apple Store. For this, we used the following search terms: 'budget', 'budgeting' and 'finance'. The initial number of retrieved apps was 1335 (Fig. 1). The exclusion criteria consisted of apps that are duplicated, not free, apps with $< 1000$ reviews and apps with average rating score $< 4$ out of 5. We also excluded irrelevant apps for personal budgeting such those for business purposes and apps that required establishing connection with one's bank account. As a result, 45 apps were included in the analysis (Appendix A), all 45 apps being available on Google Play Store and 24 of them being also available on Apple Store.

![Figure 1: PRISMA diagram describing the process of apps' selection.](image_placeholder_1)

Based on our two different types of data- apps' descriptions on marketplace and apps' specific functionalities- we employed two levels of analysis of these 45 apps. The first level consisted of the analysis of apps' descriptions available on the two marketplaces. The analysis of apps' descriptions captured app metadata such as app category and supporting platforms, as well as information on content and modality of app descriptions, app cost, age of target users and financial literacy.

The first author completed the analysis of apps' descriptions on Google Play Store by manually collecting and analysing them. A similar approach has been reported in previous HCI study (Qu et al., 2020) for analysis of apps' descriptions.

The second level involved the authors' actual use of the apps through expert evaluation. The expert evaluation led to the identification of two main functionalities, namely tracking transactions and budgeting.

Both authors completed the functionality review. The first author reviewed all apps on a Galaxy S21+ smartphone, while the second author reviewed 5 apps on an iPhone 12 smartphone. As the second author used the iOS platform, these 5 apps were randomly selected from the 24 apps available on Apple Store.

For the functionality review we have iteratively developed a coding scheme. For this, we used deductive codes informed by previous HCI work on apps' functionality review indicating tracking and monitoring as main functionalities (Qu et al., 2020; Almoallim and Sas, 2022). To further unpack these functionalities, we employed additional codes informed by mental accounting theory (Thaler, 1999) such as those of funds, in particular source and use of funds; concepts related to categories for grouping expenditures; and concepts related to mental accounts to which specific budgets are allocated to specific expenditure categories.

In addition to such theoretically informed functionalities grounded in mental accounting theory, we identified inductive codes that have been empirically informed by the specific functionalities of our reviewed apps, namely those for creating different types of transaction accounts; creating transactions metadata such as date, time and currency; as well as possible integration with users' bank account. This coding scheme was iterative and the functionality review was conducted through weekly conversation overall several months to ensure agreement.

## 4. FINDINGS: APPS DESCRIPTIONS

This section presents apps' metadata and findings from apps descriptions.

### 4.1. Apps' categories and platforms

Findings show that the 45 top- rated budgeting apps belonged mostly to the Finance categories on marketplaces, with $98\%$ (44 apps). The remaining 1 app (Expense Tracker- Money Manager & Budget) features in the Business category.

In terms of supporting platforms, while all reviewed apps were available on Android devices, over half of them, $53\%$ (24/45), were available on both platforms. In addition, $7\%$ (3/45) were also available on the Huawei App Gallery. Interestingly, only $7\%$ (3/45) of apps were available also as web apps.

This is surprising given the advantages of web apps may lead to a larger user group (Holzinger et al., 2012).

These findings highlight limitations in accessing such apps across different platforms and devices, which may hinder adoption. Previous findings indicate that restricting use to one platform may lead to reduced number of users (Humayoun et al., 2013). This may open up design opportunities for app developers to increase accessibility of budgeting apps across platforms and devices.

### 4.2. Content, modalities, cost, users age and financial literacy

#### 4.2.1. App descriptions: content

Findings indicate variation in the information provided by the app descriptions, both in terms of structure and details. According to these, our outcomes indicate three groups of apps.

The first group (28 apps) provides structured and detailed descriptions through headings for each key feature, which are detailed through brief explanations. For instance, three apps provide questions as headings such as 'How to use the monthly budget & spending tracker?'. The second group (15 apps) provides structured albeit limited descriptions through lists of key features such as debt management, but without explanations. Finally, two apps provided limited details and no list of functionalities.

Most apps do not mention if they are theoretically informed. With the exception of two apps (Goodbudget (Partners, no date) and SimpleBudget (Tanu, 2011)) mentioning in their descriptions that their design was informed by money envelopes, albeit with no reference to mental accounting theory (Thaler, 1999), no other app mentioned any theoretical underpinning. In addition, none of the apps reported any evaluation based on users' studies.

Findings also indicate inconsistency in the length of apps' descriptions, which ranged from 100 to 653 words, with an average of 372 words. On Google Play, the descriptions are capped to 4000 characters (Google, 2024b), but few app descriptions were close to this limit. As descriptions encourage users' curiosity (Jiang et al., 2014), their brevity may impact acceptability (Nadal et al., 2020).

#### 4.2.2. App descriptions: modalities

Apps are also described in various modalities, and both Google Play and Apple Store aimed to support such rich presentations of apps' functionalities by providing guidelines for developers. Apple Store emphasizes short preview videos, i.e. 30 s long, while Google Play provides guidelines for other elements of app description called preview assets, which include, besides videos, short text, app icons, graphics or screenshots (Google, 2024c).

Findings indicate the $42\%$ of apps (19 apps) included preview videos as recommended by Google Play (Google, 2024c), showing details of key features such as steps for creating a transaction.

Findings also show that $55\%$ (25 apps) provide eight screenshots, which is the maximum number recommended on Google Play to support prospective users' to discover the app capabilities, or look and feel (Google, 2024c), The content of screenshots includes apps' home page (34 apps), visual representation of the tracked data such as monthly expense categories (34 apps), common functionalities such as adding a transaction (26 apps), creating budgets (22), listing transactions (20 apps) or creating transaction accounts (19 apps).

While most apps (35 apps) provided brief titles or explanations for each screenshot, the remaining apps (10 apps) presented the screenshots without any details, which may limit their understanding of the app.

Surprisingly, while most apps captured important functions in the screenshots, others used them merely to advertise the app without specifying actual features (seven apps). Such screenshots provided information on apps' rate, apps' reviews from users or on media, unclear features with self- promoting text such best personal finance app, smart solution for your money, guilt- free spending. Such content is problematic and not recommended. In fact, Google Play recommended guidelines on the content of apps' descriptions (Google, 2024) were not followed by most of the apps (38 apps). Besides problematic violations such as testimonials from anonymous users (four apps) or comparing the app with other apps or brands (two apps), others relate to usability and accessibility of the description, i.e. word blocks and vertical/horizontal word lists (38 apps).

#### 4.2.3. Apps costing information

An important finding is the misuse of the word 'free' in app descriptions on Google Play. Although all 45 apps were free to download, only $13\%$ (6/45) of apps were completely free, whereas $87\%$ (39/45) of them were not. The latter contained in- app purchases, which meant that some features could only be accessed through subscription.

Findings also indicate that information on in- app purchases varies. While $44\%$ (17/39 apps) of these apps mentioned in- app purchases as advanced features in their description, the other $56\%$ (22/39 apps) had in- app purchase without clearly specifying them in the app description. The price range of the in- app purchases varied between £0.50 and £252.00, with average cost of £17.31. Such cost also lacks clarity if it is one- off or it relates to monthly or yearly subscription. These outcomes open design implications for developers towards clarifying the cost of the apps or of their specific functionalities.

#### 4.2.4. User group: age

A significant outcome relates to the age of target users. As specified on Google Play store, all apps were classified as adequate for children (PGEI 3). However, based on their privacy policy, $44\%$ (20/45 apps) mentioned that they were not intended to be used by children, more specifically children $< 16$ years old (4/20 apps), children $< 13$ years old (14/20 apps) or minors (2/20 apps). In addition, functionalities of budgeting apps do not vary with user age, as they fail to prove customized design for children such as support for in- app interactions to enable parental collaboration or monitoring.

#### 4.2.5. Financial literacy

Our findings showed limited support for education on budgeting practices. Noticeable here are 13 apps that provide on their websites resources such as tutorials, e- books, videos, podcasts, articles or tips. The Goodbudget: Budget & Finance app also provides a free monthly online course on starting a budget and track spending with assignments, while the You Need A Budget app provides links to YNAB- certified coaches.

## 5. FINDINGS: FUNCTIONALITY REVIEW

We now highlight the eight main functionalities of budgeting apps identified through the functionality review (Table 1). These functions have been applied to each app over several months to identify its support for each function (Appendix B).

**Table 1. The main functionalities of the 45 reviewed budgeting apps.**

| Functionality | Number of apps |
|:---|:---|
| Creating transaction accounts | |
| Cash account | 17 |
| Savings account | 11 |
| Credit card account | 17 |
| Creating transaction types | |
| Income transaction | 44 |
| Expense transaction | 45 |
| Transfer transaction | 37 |
| Supporting different forms of entering transactions | |
| One-off transaction | 45 |
| Scheduled transactions | 29 |
| Securing data access and storage | |
| PIN protection | 41 |
| Biometric protection | 24 |
| Backing up data | 35 |
| Managing transactions | |
| Categorizing income transactions | 38 |
| Categorizing expense transactions | 40 |
| Tagging transactions | 12 |
| Searching transactions | 43 |
| Exporting transactions | 24 |
| Transactions' status | 10 |
| Creating budgets | |
| Single budget | 19 |
| Multiple budget categories | 26 |
| Zero-based budget | 6 |
| Managing budgets | |
| Bar charts | 25 |
| Doughnut charts | 21 |
| Pie charts | 14 |
| Line charts | 9 |
| Home screen widgets | 28 |
| Strategies for managing budgets | |
| Information ongoing spending within budgets | 23 |
| Information before reaching budgets' limits | 8 |
| Notifications on spending over budgets' limits | 9 |

### 5.1. Supporting different types of transaction accounts: income, expense, saving

An important finding is the concept of accounts as containers for organizing transactions. Findings indicate that transaction accounts were supported by most of the top- rated budgeting apps (41/45 apps). Based on the mental accounting theory (Thaler, 1999), the three main types of accounts include (i) accounts to deposit and store funds representing the money- in such as monthly income (44 apps), (ii) accounts to use or spend the available funds representing the money- out such as expenditures (45 apps) and (iii) accounts to deposit and store wealth such as savings (11 apps).

Our findings show not all apps support each of these three types of accounts. From the 45 apps, most of them support storing funds accounts (44) and spending funds towards expenditures (45 apps) while only 11 apps support savings accounts.

An important outcome is that although different transaction accounts are supported by most of the apps (41/45 apps), four apps (Budget App- Expense Tracker (Inc, 2020), DAILY POCKET (Yjteam, 2017), EasyBudget (Letondor, 2015), and Expense Tracker- Money Manager & Budget (Labs, 2019)) do not. More specifically, they support users to directly deposit their funds into apps' home screen instead of a separate income account. As a result, all transactions in these four apps are stored directly on the apps' home screen, which is problematic as transactions cannot be linked to specific transaction accounts.

In addition, from the 45 apps supporting the three transaction accounts, i.e. income, expense and savings, for some of them (43 apps) the creation of income and expense occur in the same account, similar to a wallet or bank account where money is both deposited in and spent from. In other words, although income and expenditure accounts are conceptually distinct, for some apps, they tend to be one represented by the same account.

Another important finding is about the inconsistent terms used by budgeting apps to refer to such accounts. The used terminology appears to be drawn from two sources: everyday financial practices and the banking domain.

A significant outcome is that many apps name accounts using terms from banking domains. For instance, terms for income, expense or saving accounts include: virtual cash accounts (17 apps), virtual credit card accounts (17 apps), virtual debit accounts (13 apps), saving accounts (11 apps), virtual bank accounts (nine apps), investment accounts (seven apps), while 18 apps employ more than one of these terms. Banking terms can be beneficial as they leverage users' familiarity with banking practices. However, the direct link between these accounts and banking practices is limited since only seven apps offer the integration of budgeting apps with users' online banking services, and even then, it is only accessible as a premium feature.

Furthermore, the terminology derived from the banking domain fails to encompass the different types of expense accounts, such as those designated for various expense categories as reflected in the money envelope system from mental accounting (Thaler, 1999). This inadequacy becomes apparent as banking accounts primarily focus on capturing expenditures related to debt repayments, such as mortgage, debit or credit card, but not for essential aspects such as bills or monthly budgets for grocery or rent.

In addition to the banking domain, the terminology for labelling transaction accounts is also derived from everyday financial practices. Such terms include wallet (three apps: Easy Home Finance (VoPo, 2015), Expense Tracker & Budget App (Estimate, 2019) and Spendee Budget & Money Tracker (Spendee, 2013)), budget (two apps: Home Budget- Money Manager and Budget: Budget and expense tracking app), payment account (one app- Money pro (Lic, 2017)) or financial account (one app: Family budget- spending tracker (DigitLeaf, 2017)). With regards to these terms, none of the apps applied a clear distinction between the available funds (i.e. money- in), expenses (i.e. money- out) and wealth accounts. The only exception is the GnuGash app, which provides separate accounts for such as assets, income and expenses.

Home screen widgets (27/45 apps) and quick access options (16/45 apps) were also provided to differentiate through colours different categories (10 apps) or transaction accounts (seven apps), or through icons different transaction accounts (12 apps).

### 5.2. Supporting different transaction types: income, expenses, transfer

Study outcomes indicate various types of transactions as transfer of money from a source to a destination, for which we identified the following three types: income transactions for depositing funds (44 apps), expense transactions for paying expenditures (45 apps) and transfer transactions for transferring money from income to expense accounts (37 apps). We further describe each of these types.

#### 5.2.1. Income transactions

Income transactions are supported by most apps (44), albeit there are inconsistencies in the data available across the apps to support this type of transactions. Such data includes the name of transaction such as salary, source of money such as employer name, deposit amount and currency (40 apps), as well as date or time of transaction. In addition, some apps also supported entering written notes for income transactions (40 apps), attaching digital receipts (13 apps) or specifying transaction location (four apps).

The only app that does not support depositing funds (SimpleBudget app) builds on money envelopes. Although it does not specify the total amount of available funds to be divided amongst all envelopes. Therefore, it can be cognitively challenging to ensure that the allocated money to multiple envelopes does not exceed the total available funds.

Interestingly, one- third of these apps (12/40) support the choice of different currency for each income and expense transaction being created, while the remainder of these apps (28/40) provide the list of currencies and their choice in the app settings, so once the selection is made it will apply to all transactions until a new currency is selected. These two options highlight an interesting tension between supporting ease of use when users work often with multiple currencies or a single currency.

#### 5.2.2. Expense transactions

Findings indicate that expense transactions are supported by all apps, however with different data available across the apps. Such data includes transaction name such as grocery, destination of money such as grocery store name, paid amount (45 apps), currency (41 apps), date (45 apps) or time of transaction (18 apps), as well as, in addition, some apps supported writing transaction notes (42 apps), attaching digital receipts (13 apps) or specifying transaction location (four apps) or payment method such as cash, cheque or credit/debit cards (4 apps).

Writing notes for both income and expense transactions is a common feature supported by most apps, although provided under different names: comment, description, remark or memo. These notes however can be particularly useful for capturing any information related to a transaction not captured through the given transaction features. Such information could be to identify the source of the income, the place where the expenditure occurred, the payment method or even if a transaction was on a sale.

While most notes were supported in written format, one app (Income Expense - daily expenses) had the option to enter a note via speech to be converted and saved in written text in the note section.

The option to enter transaction location is supported by a small number of apps (four apps: Goodbudget: Budget & Finance, Money+ Cute Expense Tracker, Tosh Finance, Wallet: Budget Planner Tracker) but is an interesting feature. These apps allow users to add the location where a transaction took place such as a grocery store.

The method of saving the transaction location varies. Thus, two apps (Goodbudget: Budget & Finance and Money+ Cute Expense Tracker) use the current phone's location to be included to the entered transaction without having the option to manually choose it. This can be problematic as it requires that the transaction is entered at the time when and where it occurred. The other two apps (Tosh Finance and Wallet: Budget Planner Tracker) allow the location to be added to a transaction both during and after the transaction occurs. Goodbudget: Budget & Finance provides the option to remember the transaction's location on the phone (GPS- based) and later auto- suggests the expense category, payee and account that have been saved at that location.

Surprisingly, in one app (Expense Manager), the location feature is through a third- party app. Findings also indicate that 9 out of 45 apps (three as premium) provide the option of notifying users of upcoming payments if such expense transactions have been scheduled in advance.

#### 5.2.3. Transfer transactions

If income and expense transactions allow the flow of money from and to the external world, the transfer transactions support the movement of money amongst a user's account from a source (available funds) to a destination (for expenses or savings). Findings indicate that 36 apps support such transactions, including one app as premium. Similar to the above types of transactions, the data available across the apps for transfer transactions varies. Such data includes transaction source and destination, transferred amount (36 apps), transfer date (30 apps) and time (11 apps) and transfer currency (25 apps).

Surprisingly, most of these apps (33/36) support transfer transactions even if the source account does not have sufficient funds (33/36 apps). The exceptions include MoneyWise app where transfer transactions are a premium feature and Family budgetspending tracker app, which stops the transfer while providing notification on and insufficient amount'. In addition, some apps supported attaching digital receipts to transfer transactions (four apps), or specifying transaction location (three apps). All three types of transactions supported the option of attaching a digital receipt to them. This could be a valuable feature that may support people to later recall the transaction. Such digital receipts could be in different formats: (i) taking a photo directly with the camera to attach it to income/expense (13 apps) or to transfer transactions (four apps), (ii) choosing a photo from the phone gallery for both income and expense (nine apps) or for transfer transactions (two apps) or (iii) attaching a chosen file from folder (two apps), while five apps provide the attachment feature within the premium version.

Each of these three options is important as they can flexibly support different scenarios. For example, users might have a physical receipt that they can save as a photo on their phone to attach to their receipt at the time of transaction or later or the receipt could be in a format other than a photo (i.e. PDF file) as provided by online shops, therefore supporting multiple file format is preferred.

### 5.3. Supporting different forms of entering transactions

Our outcomes indicate two forms of entering transactions based on time and mode. From the time perspective, transactions can be one- off or scheduled in advance, and from the mode perspective, they can be manually or automatically entered.

While most transactions are one- off and supported by all apps, fewer apps support also recurrent income/expense transactions (29 apps) or recurrent transfer transactions (19 apps). The latter are supported through the schedule of future transactions for a specified amount and date, to be repeated during a determined period. The frequency of recurring transactions varies across apps, from daily (28 apps) and weekly/monthly (29 apps) to annually (27 apps) as shown in Fig. 2.

![Figure 2: Example of the recurrence option of a transaction such as income. App name: Spendee Budget & Money Tracker](image_placeholder_2)

Both one- off and scheduled transactions can be entered manually or automatically. All apps (45 apps) support the manual entering of transactions, albeit through various features of the app interface.

Most apps support the similar interactions on the app's home screen for entering both income and expense transactions. These consist of tapping on the plus icon (35 apps), the income button or expense button (eight apps) or the register button (1 app- - MoneyWise (North, 2011)). The CoinKeeper app provides different interactions to enter income, i.e. by tapping on the plus icon, and to enter expense, i.e. by dragging a transaction account icon into the expense category then specify the expense amount from the dragged account. Arguably, supporting the simple interaction for entering both income and expense transactions through the same simple interaction could increase usability. To support complete and accurate records, 23 out of 45 apps provide the option of sending daily reminders for entering transactions, two apps on as premium.

While all apps support manual entering of transactions, fewer apps (seven apps) support their automatic importing from online banking accounts into the budgeting. This functionality requires that the budgeting apps is integrated with online banking apps (seven apps). Alternative ways of automatically importing transactions relies on linking the budgeting app to bank Short Messaging Service (SMS).

This functionality was supported by a lower number of apps (six apps, including two apps that offer it as premium). This feature could provide benefits such as automatic tracking of expenses in real time.

Home screen widgets and quick access options also supported functionalities for entering transactions such as adding income (27 apps), expense (28 apps), transfer (16 apps) or recurrent income/expense (one app).

### 5.4. Securing data access and storage

Financial apps store personal and sensitive information about users' financial behaviours, yet functionalities for securing and backing up the stored data vary across our 45 apps. Findings show that security features such as Personal Identification Number (PIN) were provided by 41 apps (31 free, 10 premium). Apps providing free PIN functionality require different numbers of PIN digits: at least four (three apps), four (18 apps), unspecified (eight apps), while two apps employ the phone's PIN.

The second common security feature was biometric protection available in 24 apps as fingerprint (17 apps free, 9 apps premium), and in three apps as face recognition (one app free, two apps premium).

For backing up data, budgeting apps provide a range of options including local storage device in 14 apps (free), Google Drive in 17 apps (eight free, nine premium), Dropbox in 7 apps (one free, six premium), SD card in two apps (free) and app website in one app (free).

### 5.5. Managing transactions: categorizing, tagging, searching, exporting and monitoring status

Besides entering transactions, findings indicate specific functionalities for managing them through categorizing, tagging, searching exporting historic transactions and monitoring transactions' status.

#### 5.5.1. Categorizing transactions

Functionality review findings indicate that most apps support the categorization of similar transactions for both income and expenses. Such functionality is important and aligns with envelopes from mental accounting theory (Thaler, 1999). Our findings suggest that the categorization process can be two types: user- defined or system- defined. The latter consists of a predefined list of categories. For income transactions these include bonus, business, gift, refund and salary and are provided by 38/45 apps, while for expense transactions such predefined categories include bills, education, grocery, transportation or entertainment (40 apps).

In addition to categories provided by the app, users can also be supported to create their own categories for both income (36/45 apps) and for expenses (42/45 apps). The new created categories can be re- used later for subsequent transactions. While most apps support one level of categories, 15 apps support a sub- categories option for transactions. For instance, transportation expense category can have sub- categories such as bus, taxi or subway. Despite the importance of categories for managing transactions, some apps provided limited support, through only one category for income transactions (four apps) or only one category for expense transactions (two apps).

#### 5.5.2. Tagging transactions

In addition to categories provided by the app, users can also be supported to create their own categories for both income (36/45 apps) and for expenses (42/45 apps). The new created categories can be re- used later for subsequent transactions. While most apps support one level of categories, 15 apps support a sub- categories option for transactions. For instance, transportation expense category can have sub- categories such as bus, taxi or subway. Despite the importance of categories for managing transactions, some apps provided limited support, through only one category for income transactions (four apps) or only one category for expense transactions (two apps).

transactions from different categories under one event. Such tags could be predefined by the app or generated by the users. Those provided by apps could relate to income and expense transactions (six apps) or transfer transactions (two apps), while tags generated by users are supported for 12 apps for both income and expense transactions and by five apps for transfer transactions.

#### 5.5.3. Searching transactions

Users can also search and organize their transactions daily (33 apps), weekly (25 apps), monthly (43 apps), yearly (32 apps), by a specific date (28 apps) or a custom period that the user defines from- to- date (30 apps). These different options allow users to manage transactions that occurred in specific time periods instead of scrolling over all transactions. For example, the daily breakdown allows users to track spending on a day- to- day basis, which may support the identification of unnecessary expenses, while weekly transactions may support comparison of spending patterns across different weeks. However, fewer apps provided advanced filtering such as searching transactions by minimum and maximum transaction amount (three apps), transaction status (three apps) or payment method (two apps).

#### 5.5.4. Exporting transactions

A prerequisite for understanding transactions is accessing them. Most apps support exporting lists of historic transactions in different file formats such as Excel (10 apps, 8 apps as premium), CSV (14 apps, 5 apps as premium), PDF (four apps, six apps as premium), or HTML files (two apps, one as premium). Furthermore, the transaction data could be sent by email as PDF (two apps) or CSV file (three apps). Findings show that about half of apps (24/45 apps) provide such export functionality, 14 apps provide it under subscription while six apps do not provide it. Such functionality may protect users from data loss and supports their reflection on past transactions.

#### 5.5.5. Monitoring transactions' status

Transactions can also be monitored through their status, a feature supported by 10 out of 45 apps. Findings suggest five types of transactions' status that users can select for while monitoring their transactions: uncleared, paid, cleared, reconciled and void.

Uncleared status refers to entered transactions that are pending as they are yet to be processed by the bank (three apps). Paid status is provided by four apps that users can choose to mark transactions whose payment has been made, irrespective of the payment being available on the bank statement. Transactions whose payments have been made and also appear in the bank statement can be marked with Cleared status (seven apps for income and expense transactions and four apps for transfer transactions).

Reconciled status was provided by five apps for all three types of transactions. This status refers to transactions entered in the budgeting apps that have been paid and cleared and which are also accurate as users have checked that the transaction's details entered in the app match those from their bank statement. Finally, status Void refers to transactions that are no longer valid and will not appear in bank statements (three apps).

### 5.6. Creating single or multiple budgets

Findings revealed that all apps support budgeting functionality through which users can create budgets, which findings show can be single or multiple. Multiple budgets are aligned with money envelopes from mental accounting theory (26 apps), while single budgets are not (19 apps).

The single budget depends on one main budget holding the available funds, from where all expenses are covered. This type of budget is not consistent with mental accounting theory (Thaler, 1999). In addition, 8 apps out of 19 apps rely on one main budget.

While single budgets store the total amount of available funds, five apps allow users to explicitly set their total funds as budget for all expenses albeit without giving a specific budget name; such name is provided by the app. Although users cannot set the budget name, they can set the budget amount and the budget period as daily (one app- Spending Tracker), weekly (two apps- DAILY POCKET- Budget Manager and Spending Tracker), monthly (four apps), yearly (one app- Spending Tracker) or defined by the user (one app- Monny).

In contrast with single budgets, multiple budgets (26 apps) reflect mental accounts (Thaler, 1999). These 26 apps allow users to create multiple envelopes/budgets with allocated budget amounts for different expense categories, such as utilities, transport or groceries. In terms of the budgeting name, some apps (11/26 apps) use the expense category name as name for the budget, i.e. budget for grocery category is grocery budget. The remaining apps (15/26 apps) support users to provide the budgets' names, i.e. budget for bills category can be named household budget.

Furthermore, all 26 apps supporting multiple budget also allow users to set the budget periods such as daily (seven apps), weekly (15 apps), fortnight (seven apps), monthly (26 apps), biannually (three apps) and annually (14 apps), while 17 apps support multiple predefined budgeting periods. Additionally, six apps allow the budget period to be defined by users.

Budgets can be allocated to expense accounts but also to saving accounts. For instance, the Mobills: Budget Planner app provides users two options of using their entire monthly income either by spending $100\%$ against expense accounts or $80\%$ towards these and $20\%$ towards saving accounts, following the popular saving rule $20/80\%$ (Oxford Home Schooling, 2024).

An interesting outcome is the functionality of supporting the setting of recurring multiple budget categories (22 apps). Since not all apps supporting multiple budgets allow users to set recurrent budget categories, if they need the same budget in the subsequent budgeting period, they have to create it from scratch. The number of apps that automatically allow users to set recurring multiple budget categories is $18 / 26$ apps where the remaining four apps have it optional to the user.

Findings also indicate inconsistent terms for recurring budgets such as clone budget (Budget Planner- Expense tracker/iSaveMoney) or import from last month (Income Expense- daily expenses). The latter term may be problematic as users may also use it for automatically importing transactions or for importing data from Google Drive into the app such as CSV file with list of transactions that have not been yet entered into the app.

### 5.7. Managing budgets: visualizing transactions

Findings show that most budgeting apps (26 apps) provide a range of visualizations of past transactions within their specific budgets, albeit only for multiple budgets. Single budgets (19 apps) are usually depicted through text in the form of lists of entered transactions. In contrast, multiple budgets (26 apps) are commonly represented through visualizations (25 apps) such as bar charts (25 apps), doughnut charts (21 apps), pie charts (14 apps) and line charts (nine apps). The apps that do not provide charts (5/45 apps) may hinder users' efforts to understand their transactions within their respective budgets. The use of different visualization formats can enhance such understanding of one's expenditure trends. For example, bar charts can help users compare spending across different expense categories, pie charts show proportion of expenses in each category and line charts show fluctuations over time. Therefore, the preference for specific charts may vary with users' needs.

Home screen widgets and quick access options also supported viewing income amount (three apps), total expense (five apps), current balance (seven apps), and budget's balance (four apps).

### 5.8. Strategies for managing budgets

Findings indicate three main strategies for managing budgets such as supporting users' awareness of their ongoing spending within budgets' limits, of approaching budgets limits and of exceeding them.

#### 5.8.1. Supporting awareness of ongoing spending within budgets: spent and remaining budget amount, progress bars

Once budgets are allocated, most apps support users' awareness of their ongoing spending within the budgets, be it single or multiple budgets. Single budgets support only a high-level monitoring, usually through the display of budget balance, i.e. the remaining available funds after transactions in that budget period have cleared.

In addition to displaying budgets' balances, multiple budgets also provide visualizations representing their current spent within an allocated budget. Such visualizations are usually in the form of progress bars with colours and numbers as amount of spent budget (11/26 apps) or colours and percentages of spent budget (12/26 apps) as shown in Fig. 3.

![Figure 3: Example of ongoing spending for multiple budget categories. App name: Fast Budget—Expense Manager](image_placeholder_3)

Such colours tend to be neutral such as white or green. Findings also indicate that 10/45 apps provide the option of hiding transactions or transaction accounts. While the rationale for this option is unclear, we can imagine that it can be used to both encourage and limit spending.

#### 5.8.2. Warnings supporting awareness before reaching budgets' limits: coloured budget balance, progress bars and home screens

While the visualizations mentioned above capture the cumulative spending within each allocated budget, additional design features support users' awareness of reaching the limit amounts of their budgets. Although only $18\%$ of apps (eight apps) provided such features, they are important to highlight (Table 2).

**Table 2. Features supporting users' awareness of approaching budget limits through colour-coded warnings in the form of budget balance progress bars or home screen colours.**

| App name | Budget type | Budget used (%) | Colour-coded warning |
|:---|:---|:---|:---|
| EasyBudget | Single | User set | Budget balance – orange |
| DAILY POCKET | Single | ≤39% | Home screen – blue |
| | | 40–69% | Home screen – green |
| | | 70–89% | Home screen – orange |
| | | 90–99% | Home screen – red |
| | | 100% | Home screen – black |
| Budget planner | Multiple | >50% | Progress bar – yellow |
| Family budget | Multiple | >50% | Progress bar – yellow |
| Expense tracker | Multiple | 70% | Progress bar – orange |
| Fast budget | Multiple | 70% | Progress bar – orange |
| CoinKeeper | Multiple | 90% | Progress bar – orange |
| Expense tracker | Multiple | 90% | Progress bar – orange |

These features are present in both apps supporting single budgets (two apps) and multiple budgets (six apps) and consist of colour-coded warnings that can be delivered in (i) textual form budget balance in orange colour, (ii) diagrammatic form as yellow or orange progress bars or (iii) as different colours of the app's home screen such as blue, green, orange, red or black. Compared to neutral colours for ongoing awareness, the colours of such warnings tend to be yellow or orange as shown in Fig. 4.

![Figure 4: Example of colour-coded warnings of approaching budget limits. App name: Fast Budget—Expense Manager](image_placeholder_4)

These warnings are provided for different thresholds as percentages of budget spent, be that defined by user or set by the app. Most common thresholds for providing such notifications are 50, 70 or $90\%$ spent of budgets' amounts. While five apps provide only one threshold, DAILY POCKER app provides five values and their respective colours on the app's home screen, including black colour for the home screen when the budget was $100\%$ spent. This specific feature is akin to friction (Almoallim and Sas, 2022) designed to inconvenience and limit specific behaviour.

#### 5.8.3. Signals of spending over budgets' limits: coloured progress bars, notifications and sign symbol for budget balance

An important finding is how budgeting apps deal with users' spending beyond the allocated budgets and that no app prohibits overspending. One app however, SimpleBudget (Envelope Budget), allows users to set the option of stopping new transactions after the budget amount was spent, with the message 'Not enough balance, amount $>$ balance'.

Our outcomes indicate three formats for communicating the overspend, namely budget balance, notifications and progress bars. These formats tend to be used differently by single- and multiple- budget apps. Single- budget apps display budget balance with a negative sign symbol in red colour (11/19 apps) or in black colour (8/19 apps). Multiple- budget apps also display budget balance albeit they vary in their use of colours and sign symbol. Thus, multiple- budget apps can display the overspent amount in black colour and/or sign symbol (2/26), in red colour with no sign (6/26), in black colour with negative sign (6/26), in red colour with negative sign (11/26) and even in red colour with positive sign (one app 1Money: expense tracker budget).

Notifications are another form of signals for expenditures exceeding the budgets' limit. Only 4 out of 26 apps supporting multiple budgets provide such notifications as pop- up notifications or within app notifications (seven apps) as shown in Fig. 5.

![Figure 5: Example of signal of spending over budget limit as in-app notification. App name: Fast Budget—Expense Manager](image_placeholder_5)

The other format of progress bars is used by most apps supporting multiple budgets (22/26) but with red colour, which distinguishes them from progress bars in neutral colours for showing the spending within budget or yellow/orange ones when the spending exceeds some budgets' thresholds. Interestingly, four apps show the overspend in progress bars albeit with no change of colour to red.

## 6. DISCUSSION

While revising our initial research questions, we highlight also the novelty of our main findings. Given the limited HCI exploration of budgeting apps (Kaye et al., 2014; Vyas et al., 2015; Snow and Vyas, 2015a, 2015b; Vyas et al., 2016), we argue for the novelty of these findings.

The first question asked was how should budgeting apps be described. The analysis of apps' descriptions indicate that most apps have limited accessibility across platforms and devices, and about a quarter are insufficiently described. Most apps also do not follow the recommended Google guidelines for accessible content description, and some use it to promote the app, thus violating the regulations (Google, 2024).

About half of apps provide unclear costing information and no video previews or screenshots to highlight key functionalities. While descriptions claimed that apps are adequate for children, privacy policies of almost half of apps show that these are not intended for children, and those that are do not aim to support children's financial literacy. In fact, less than one- third of reviewed apps provide educational resources. Most of the apps have limited theoretical underpinning and evidence base.

These outcomes highlight the importance of more accessible cross- platforms and cross- devices apps informed by crossplatform development (Xanthopoulos and Xingolas, 2013). Our findings also argue for richer multimodal app descriptions including main functionalities, costing information and budgeting literacy resources tailored to user age. The latter matters, given children's limited financial knowledge (Yip et al., 2023). The design of financial apps for children can draw from previous work aimed to support financial skills and positive financial behaviour (Taylor, 2022). Our outcomes also suggest the value of future research to strengthen the theoretical underpinning of these apps, leveraging for instance mental accounting theory (Thaler, 1999).

## 7. DESIGN IMPLICATIONS

The second and third research questions concern key functionalities of budgeting apps and design implications supporting them. Functionality review shows eight functionalities concerning transactions and budgets, namely supporting different types of transactions and transaction accounts, creating budgets, entering transactions, securing data access and storage, managing transactions and budgets and three strategies for managing budgets. Based on these findings, we articulate five design implications to support different types of transactions and accounts, flexibility in entering and managing transactions, secure data access and storage, creating and management of multiple budgets and three strategies for managing budgets.

### 7.1. Support types of transactions & accounts

Our findings highlight the important distinction between transactions as transfer of money from one account to another and transaction accounts as containers for organizing transactions. Findings indicate the distinct roles of three types of transactions and transaction accounts, and we argue the importance of supporting them all. Thus, our contributions suggest consistent use of a terminology that we proposed as informed by mental accounting theory (Thaler, 1999). Thus, types of transactions should include those for income, expenditure and transfer, while the types of accounts should include those for income, expense and saving, to differentiate those for storing money- in, money- out and those for saving purposes. Therefore, our recommendation for developers is to support the aggregation of multiple transaction accounts from different financial institutions such as bank accounts, credit cards and savings where each transaction account could include the three types of transactions: income, expense and transfer. This feature allows users to have a holistic view of their finances by easily tracking their different transactions, balances and net worth for more effective budgeting.

### 7.2. Support flexible entry and management of transactions

Study outcomes indicate two forms of entering transactions based on time and mode. Based on the former, transactions can be one- off or scheduled in advance, and on the latter, they can be manually or automatically entered. We suggest that budgeting apps could allow for a more flexible approach to entering transactions if they are designed to support all these forms of entering transactions while also leveraging widgets. Our recommendation for developers is to provide these two options for entering transactions with different time periods for the scheduled transactions such as daily, weekly, bi- weekly, monthly or yearly, as well as for entering customized periods for increased flexibility. In addition, supporting entering transactions with widgets could increase the app accessibility by allowing users to choose the feature that they would like to quickly access such as entering income and expense or monitoring a transaction account balance.

Our findings also highlighted additional functionalities such as those for managing transactions, namely categorizing, tagging or monitoring their status, which are however limitedly supported across all apps. Categorizing consists of grouping similar transactions akin to mental envelopes from mental accounting theory (Thaler, 1999), while tagging allows a more arbitrary grouping based on transactions associated with the same event. Information on transactions' status support users' understanding of how these are also reflected in online banking. We argue for the importance of supporting each of these functionalities for more flexible and theoretically informed (Thaler, 1999) management of transactions.

### 7.3. Support secure data access and storage

Users' financial data are sensitive data but $>20\%$ of apps do not provide access to a free PIN feature; $< 35\%$ do not provide biometric features. Findings from security research have shown that design features ensuring the highest level of secure authentication integrate three components: what the user has (token or card), knows (password) and is (biometrics) (Woodward et al., 2003). Thus, our recommendation to financial apps developers is to integrate at least PIN and biometric functionalities for secure app access, potentially with another artefact. The latter integration has been less explored in HCI and may open up new design opportunities.

An important finding was the limited support for secure storage of users' financial data. Backing up such data however is essential to ensure its recovery in case the original data is lost or damaged (Zhang and Li, 2017). Findings also show that $< 38\%$ of apps provide such free options mostly on a local storage device (user's phone), Google Drive or Dropbox. We argue for the value of providing flexible backup functionalities for financial data. This can be informed by previous research comparing performance criteria of data storage, for instance on Dropbox and One Drive, where the former shows advantages in security and upload/download of small files, while the latter for large files (Alotaibi et al., 2019).

### 7.4. Support creation and management of multiple budgets

Functionality review findings showed that $>40\%$ of apps do not support multiple budgets against expense categories or mental envelopes from mental accounting theory (Thaler, 1999). For instance, previous HCI studies on financial practises have shown the use of paper envelopes and jars (Vyas et al., 2015, 2016; Snow and Vyas, 2015a). However, these involve physical storage of money for specific purposes, rather than digitally materializing mental accounts. Thus, we recommend designing for multiple budget categories. Different users have unique spending habits and financial priorities; therefore, developers should provide users with the ability to set personalized budgets by creating for instance their own budget's name and category and customized budget period.

Our outcomes indicated that some of the reviewed apps also support the management of budgets through functionalities like export, visualize, organize and search historic transactions. Exporting historic transactions can take various formats, while visualizing cumulative transactions can be completed in different chart formats that users could search for and organize for instance by dates or time periods. Supporting all these functionalities can provide users flexible tools to customize reports and charts and better understand their past transactions and financial behaviours.

### 7.5. Support strategies for managing budgets

Functionality review findings have highlighted three strategies for managing budgets aimed at supporting users' awareness of their ongoing spending within budgets, of approaching budgets' thresholds and of exceeding budgets' amounts. Design features relevant here are budget amounts: spent and remaining balance, notifications and visualizations through progress bars albeit inconsistently provided across the apps.

We particularly recommend the provision of progress bars in different colours from neutral to orange, and red to communicate spending that is within budget, approaches budget's amount or exceeds it, respectively. Previous HCI work has shown the value of progress bar charts as 'percent done progress indicator' (Myers, 1985) and for representing effective visualizations to monitor the progress of a task. In addition to visualizing such information, we recommend developers to also celebrate users' achievements by using for instance scores/virtual badges that could help them feel more competent and motivated to use the app (Bitrián et al., 2021).

Findings also indicate inconsistent formats for displaying overspent budget, albeit the common and potentially easier to understand is the negative sign symbol in front of the budget amount, with both the sign and the amount shown in red colour.

A particular significant outcome is the provision of notification to warn users when their spending approaches budgets' limits or exceeds budget thresholds such as 50, 70 or $90\%$, although less than a quarter of our apps employed such feature. We recommend these design features as, unlike information on budget overspent, notifications support users' agency to make necessary adjustments to their financial behaviour and avoid spending beyond the budgets' amounts.

## 8. CONCLUSION

Our paper reports analysis of descriptions and functionality review of 45 top-rated budgeting apps. Study findings suggest the value of richer, multimodal app descriptions, support for budgeting literacy and stronger theoretical underpinning of these apps. They also highlight eight main functionalities including support for different types of transactions and transaction accounts, creating budgets, entering transactions, secure data access and storage, managing transactions and budgets and for strategies for managing budgets. We concluded with five design implications for budgeting apps for supporting the main types of transactions and transactions accounts through consistent terminology, flexible entry and management of transactions, secure data access and storage, creation and management of multiple budgets and supporting for the strategies for managing budgets.

## Acknowledgements

The first author's work was supported by Taibah University, Saudi Arabia, and the Saudi Arabian Cultural Bureau, London.

## Data availability

Additional data underlying this paper is provided in supplementary material.

## References

Alenazi, M., & Sas, C. (2023). Evaluating budgeting apps: limited support for budgeting compared to tracking. *36th International BCS Human-Computer Interaction Conference (BCS HCI 23)*. BCS Learning and Development Ltd. Proceedings of BCS HCI 2023. York, UK. doi:https://doi.org/10.14236/ewic/BCSHCI2023.1

Almoallim, S. and Sas, C. (2022) Toward research-informed design implications for interventions limiting smartphone use: functionalities review of digital well-being apps. *JMIR Form. Res.*, 6, e31730. https://doi.org/10.2196/31730.

Alotaibi, S., Alomair, H., & Elhussein, M. (2019). Comparing performance of commercial cloud storage systems: the case of Dropbox and One Drive. *2019 International Conference on Computer and Information Sciences (ICCIS)*. IEEE. Sakaka, Saudi Arabia. 1–5. doi:https://doi.org/10.1109/ICCISci.2019.8716385

Bitrián, P., Buil, I. and Catalán, S. (2021) Making finance fun: the gamification of personal financial management apps. *Int. J. Bank Mark.*, 39, 1310–1332. https://doi.org/10.1108/IJBM-02-2021-0074.

Chung, A. E., Griffin, A. C., Selezneva, D. and Gotz, D. (2018) Health and fitness apps for hands-free voice-activated assistants: content analysis. *JMIR mHealth uHealth*, 6, e174–e113. https://doi.org/10.2196/mhealth.9705.

DigitLeaf, L. (2017). Family budget-spending tracker. Google Play. https://play.google.com/store/apps/details?id=com.colpit.diamondcoming.isavemoneygo%0A (Accessed April 10, 2024)

Estimate, B. B. (2019). Expense Tracker & Budget App. Google Play. https://play.google.com/store/apps/details?id=expense.tracker.income.receipt.budget (Accessed April 10, 2024)

French, D., McKillop, D. and Stewart, E. (2021) Personal finance apps and low-income households. *Strateg. Chang.*, 30, 367–375. https://doi.org/10.1002/jsc.2430.

Google. (2024). Examples of common violations. https://support.google.com/googleplay/android-developer/answer/9898842?hl=en-GB&ref_topic=9877064#zippy=%2Cexamples-of-common-violations (Accessed June 25, 2022)

Google. (2024b). Product details. https://support.google.com/googleplay/android-developer/answer/9859152?hl=en-GB#zippy=%2Cproduct-details (Accessed September 11, 2022)

Google. (2024c). Screenshots. https://support.google.com/googleplay/android-developer/answer/9866151?hl=en-GB#zippy=%2Cscreenshots (Accessed June 25, 2022)

Gunaratne, J., & Nov, O. (2015). Informing and improving retirement saving performance using behavioral economics theory-driven user interfaces. *Conference on Human Factors in Computing Systems - Proceedings*, 2015-April. Association for Computing Machinery. Seoul, Republic of Korea. 917–920. doi:https://doi.org/10.1145/2702123.2702408

Holzinger, A., Treitler, P., & Slany, W. (2012). Making apps usable on multiple different mobile platforms: on interoperability for business application development on smartphones. In: Quirchmayr, G., Basil, J., et al., eds. *Multidisciplinary Research and Practice for Information Systems*. CD-ARES 2012. Lecture Notes in Computer Science. Springer, Berlin, Heidelberg. 7465 LNCS, 176-189. doi:https://doi.org/10.1007/978-3-642-32498-7_14

Humayoun, S. R., Ehrhart, S., & Ebert, A. (2013). Developing mobile apps using cross-platform frameworks: a case study. In: Kurosu, M., ed. *Human-Computer Interaction*. Lecture Notes in Computer Science. Springer, Berlin, Heidelberg. 8004 LNCS(PART 1), 371-380. doi:https://doi.org/10.1007/978-3-642-39232-0_41

Inc, H. G. G (2020). Budget App - Expense Tracker. Google Play. https://play.google.com/store/apps/details?id=com.hg.moneymanager.budgetapp (Accessed April 10, 2024)

Jiang, H., Ma, H., Ren, Z., Zhang, J., & Li, X. (2014). What makes a good app description? *ACM International Conference Proceeding Series*, 2014- November. Association for Computing Machinery. Hong Kong, China. 45-53. doi:https://doi.org/10.1145/2677832.2677842

Jun, M. and Palacios, S. (2016). Examining the key dimensions of mobile banking service quality: an exploratory study. *Int. J. Bank Mark.*, 34, 307-326. https://doi.org/10.1108/IJBM-01-2015-0015.

Kaye, J. J., McCuiston, M., Gulotta, R., & Shamma, D. A. (2014). Money talks: tracking personal finances. *Conference on Human Factors in Computing Systems - Proceedings*. Association for Computing Machinery. Toronto, Ontario, Canada. 521-530. doi:https://doi.org/10.1145/2556288.2556975

Labs, V. (2019). Expense Tracker - Money Manager & Budget. Google Play. https://play.google.com/store/apps/details?id=com.vlab.expense.tracker (Accessed April 10, 2024)

Lee, M. K., Kiesler, S., & Forlizzi, J. (2011). Mining behavioral economics to design persuasive technology for healthy choices. *Conference on Human Factors in Computing Systems - Proceedings*. Association for Computing Machinery. Vancouver, BC, Canada. 325-334. doi:https://doi.org/10.1145/1978942.1978989

Letondor, B. (2015). EasyBudget - Personal budget planning made simple. Google Play. https://play.google.com/store/apps/details?id=com.benoitletondor.easybudgetapp (Accessed April 10, 2024)

Lewis, M., & Perry, M. (2019). Follow the money: managing personal finance digitally. *Conference on Human Factors in Computing Systems - Proceedings*. Association for Computing Machinery. Glasgow, Scotland, UK. 1-14. doi:https://doi.org/10.1145/3290605.3300620

Llc, I. (2017). Money pro. Google Play. https://play.google.com/store/apps/details?id=com.imeborsoft.moneyproandroid%0A (Accessed April 10, 2024)

Lolla, S., & Sas, C. (2023). Evaluating mobile apps targeting personal goals. *Conference on Human Factors in Computing Systems - Proceedings*. Association for Computing Machinery. Hamburg, Germany. 106, 1-7. doi:https://doi.org/10.1145/3544549.3585725

Myers, B. A. (1985). The importance of percent-done progress indicators for computer-human interfaces. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*. Association for Computing Machinery. San Francisco, California, USA. 11-17. doi:https://doi.org/10.1145/317456.317459

Nadal, C., Sas, C., and Doherty, G. (2020). Technology acceptance in mobile health: scoping review of definitions, models, and measurement. *J. Med. Internet Res.*, 22, e17256- e17217. https://doi.org/10.2196/17256.

North, H (2011). MoneyWise. Google Play. https://play.google.com/store/apps/details?id=com.handynorth.moneywise_free%0A (Accessed April 10, 2024)

Oxford Home Schooling. (2024). What Is The 80/20 Rule?. https://www.oxfordhomeschooling.co.uk/study-tips/what-is-the-80-20-rule/ (Accessed September 29, 2023)

Park, J., Lee, H., Park, S., Chung, K.- M., & Lee, U. (2021). GoldenTime: Exploring System-Driven Timeboxing and Micro-Financial Incentives for Self-Regulated Phone Use. In: *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3411764.3445489

Qu, C., Sas, C., Dauden Roquet, C. and Doherty, G. (2020). Functionality of top-rated mobile apps for depression: systematic search and evaluation. *JMIR Ment Health*, 7, e15321- e15321. https://doi.org/10.2196/15321.

Qyresearch. (2024). Global Personal Financial Management Tools Market Size, Status and Forecast 2019-2025. https://www.marketresearch.com/QYResearch-Group-v3531/Global-Personal-Financial-Management-Tools-12732938/ (Accessed December 26, 2022)

Shrestha, P. (2023). A deep dive into the explosive growth of finance apps in 2023. https://www.ajust.com/blog/finance-app-usage/ (Accessed April 16, 2024)

Snow, S., & Vyas, D. (2015a). Fixing the alignment: an exploration of budgeting practices in the home. *Conference on Human Factors in Computing Systems - Proceedings*. Association for Computing Machinery. Seoul, Republic of Korea. 18, 2271-2276. doi:https://doi.org/10.1145/2702613.2732808

Snow, S., & Vyas, D. (2015b). Fostering collaboration in the management of family finances. *OzCHI 2015: Being Human - Conference Proceedings*. Association for Computing Machinery. Parkville, VIC, Australia. 380-387. doi:https://doi.org/10.1145/2838739.2838746

Spendee. (2013). Spendee Budget & Money Tracker. Google Play. https://play.google.com/store/apps/details?id=com.cleevio.spendee (Accessed April 10, 2024)

Srl, A. (2014). Fast Budget - Expense Manager. Google Play. https://play.google.com/store/apps/details?id=com.blodhgard.easybudget (Accessed April 16, 2024)

Stockinger, T., Koelle, M., Lindemann, P., Witzani, L., & Kranz, M. (2013). SmartPiggy: a piggy bank that talks to your smartphone. *Proceedings of the 12th International Conference on Mobile and Ubiquitous Multimedia, MUM 2013*. Association for Computing Machinery. Luled, Sweden. 43, 5-6. doi:https://doi.org/10.1145/2541831.2541869

Tanu, F. (2011). SimpleBudget (Envelope Budget). Google Play. https://play.google.com/store/apps/details?id=com.simplebudget (Accessed April 10, 2024)

Taylor, M. (2022). The 5 Best Allowance and Budgeting Apps for Kids. Parents. https://www.parents.com/kids/responsibility/money-management/allowance-and-budgeting-apps-for-kids/ (Accessed October 02, 2023)

Thaler, R. H. (1999) Mental accounting matters. *J. Behav. Decis. Mak.*, 206, 241-268. https://doi.org/10.1017/CBO9780511803475.015.

Vines, J., Dunphy, P., & Monk, A. (2014). Pay or delay: the role of technology when managing a low income. *Conference on Human Factors in Computing Systems - Proceedings*. Association for Computing Machinery. Toronto, Ontario, Canada. 501-510. doi:https://doi.org/10.1145/2556288.2556961

VoPo. (2015). Easy Home Finance.

Vyas, D., Snow, S., Brereton, M., Dulleck, U., & Boyen, X. (2015). Being thrifty on a \$100K wage: austerity in family finances. *Proceedings of the ACM Conference on Computer Supported Cooperative Work, CSCW*, 2015- January. Association for Computing Machinery. Vancouver, BC, Canada. 167-170. doi:https://doi.org/10.1145/2685553.2698998

Vyas, D., Snow, S., Roe, P., & Brereton, M. (2016). Social organization of household finance: understanding artful financial systems in the home. *19th ACM Conference*. Association for Computing Machinery. San Francisco, California, USA. 1777-1789. doi:https://doi.org/10.1145/2818048.2819937

Woodward, J. D., Horn, C., Gatune, J., & Thomas, A. (2003). *Biometrics: A Look at Facial Recognition*. RAND Corporation. Santa Monica, CA. https://www.rand.org/pubs/documented_briefings/DB396.html

Xanthopoulos, S., & Xinosagos, S. (2013). A comparative analysis of cross-platform development approaches for mobile applications. *ACM International Conference Proceeding Series*. Association for Computing Machinery. Thessaloniki, Greece. 213-220. doi:https://doi.org/10.1145/2490257.2490292

Yip, J. C., Ello, F. M. T., Tsukiyama, F., Wairagade, A., & Ahn, J. (2023). "Money shouldn't be money!" An examination of financial literacy and technology for children through co-design. *Proceedings of the 22nd Annual ACM Interaction Design and Children Conference*, Chicago, IL, USA. Association for Computing Machinery. Chicago, IL, USA. 82-93. doi:https://doi.org/10.1145/3585088.3589355

Yjteam. (2017). DAILY POCKET - Budget Manager. Google Play. https://play.google.com/store/apps/details?id=kr.co.yjteam.dailypay (Accessed April 10, 2024)

Zaidan, S. and Roehrer, E. (2016) Popular mobile phone apps for diet and weight loss: a content analysis. *JMIR mHealth uHealth*, 4, e80. https://doi.org/10.2196/mhealth.5406.

Zhang, J., & Li, H. (2017). Research and implementation of a data backup and recovery system for important business areas. *Proceedings - 9th International Conference on Intelligent Human-Machine Systems and Cybernetics, IHMC 2017*. IEEE. Hangzhou, China. 2, 432-437. doi:https://doi.org/10.1109/IHMC.2017.209

## Appendix A. List of 45 reviewed budgeting apps

1. 1 Money: expense tracker budget
2. Alzex Finance: Family budget with cloud sync
3. AndroMoney (Expense Track)
4. Bills Reminder, Budget Planner
5. Bluecoins Finance: Budget, Money & Expense Manager
6. Budget App - Expense Tracker
7. Budget planner - Expense tracker/SaveMoney
8. CoinKeeper: expense, money manager, budget planner
9. DAILY POCKET - Budget Manager
10. Easy Home Finance
11. EasyBudget - Personal budget planning made simple
12. Expense Manager
13. Expense Manager
14. Expense Tracker - Money Manager & Budget
15. Expense Tracker & Budget App/ Bookipi
16. Expense Tracker, Family Budget/FinArt
17. Family budget - spending tracker/ SaveMoneyGo
18. Fast Budget - Expense Manager
19. Budget: Budget and expense tracking app
20. GnuCash
21. GoodBudget: Budget & Finance
22. Home Budget - Money Manager
23. Home Budget Manager Lite With Sync
24. Home Finance
25. Income Expense - daily expenses
26. Mobills: Budget Planner
27. Moneyfy - Budget Manager and Expense Tracker app
28. Money Manager Expense & Budget
29. Money manager, expense tracker, budget, wallet
30. Money Manager: AZV Money Pro
31. Money pro
32. Money Tracker: Expense Tracker, Wallet, Budget App
33. Money + Cute Expense Tracker
34. MoneyWise
35. Money
36. Monthly Expenses: Manage Money
37. My Expenses
38. My Finances
39. SimpleBudget (Envelope Budget)
40. Spendee Budget & Money Tracker
41. Spending Tracker
42. Tosh Finance - Personal Budget & Expense Tracker
43. Vault - Budget Planner
44. Wallet: Budget Planner Tracker
45. YNAB (You Need A Budget)

## Appendix B. The main functionalities of the 45 top-rated budgeting apps with the apps' number that provide those functionalities

| Function | Number of apps | Apps' number |
|:---|:---|:---|
| Creating transaction accounts | | |
| Cash account | 17 | 1, 3-5, 7, 12, 16, 17, 20, 21, 28, 33, 36, 37, 43-45 |
| Savings account | 11 | 1, 4, 5, 7, 13, 21, 26, 28, 36, 44, 45 |
| Credit card account | 17 | 3-5, 7, 12, 13, 16, 20, 21, 26, 28, 30, 31, 33, 37, 44, 45 |
| Creating transaction types | | |
| Income transaction | 44 | 1-38, 40-45 |
| Expense transaction | 45 | 1-45 |
| Transfer transaction | 37 | 1-5, 7, 8, 10, 12, 13, 15-18, 21, 23-33, 36-25 [sic?] |
| Supporting different forms of entering transactions | | |
| One-off transaction | 45 | 1-45 |
| Scheduled transactions | 29 | 1, 3-5, 7-11, 13, 15, 16, 18, 20, 21, 23, 26, 28, 30, 31, 35, 36, 38, 40, 41, 43, 45 |
| Securing data access and storage | | |
| PIN protection | 41 | 1-10, 12-20, 22-32, 34-38, 40-45 |
| Biometric protection | 24 | 1-6, 9, 13-15, 17, 18, 25, 26, 30, 31, 33, 36, 38, 40-45 |
| Backing up data | 35 | 2-7, 9-14, 16-20, 22-25, 27, 28, 30, 31, 33-39, 41, 42 |
| Managing transactions | | |
| Categorizing income transactions | 38 | 1, 3-7, 9, 10, 12, 15, 17, 18, 20, 22-38, 40-45 |
| Categorizing expense transactions | 40 | 1-5, 7-9, 11-15, 17-19, 21-37, 39-45 |
| Tagging transactions | 12 | 5, 7, 13, 16, 17, 31, 34, 37, 38, 40, 42, 44 |
| Searching transactions | 43 | 1-42, 44 |
| Exporting transactions | 24 | 2-5, 9, 10, 13, 15, 16, 20, 22, 23, 25, 27-30, 34-35, 37, 38, 40-42 |
| Transactions' status | 10 | 5, 7, 13, 18, 26, 30, 31, 34, 44, 45 |
| Creating budgets | | |
| Single budget | 19 | 6, 9, 10, 11, 12, 14, 19, 20, 22, 24, 27, 29, 31, 35-38, 41, 43 |
| Multiple budget categories | 26 | 1-5, 7, 8, 12, 15-18, 21, 23, 25, 26, 28, 30, 32-34, 39, 40, 42, 44, 45 |
| Zero-based budget | 6 | 17, 21, 26, 39, 40, 45 |
| Managing budgets | | |
| Bar charts | 25 | 1-5, 7, 10, 12, 13, 15-17, 20, 21, 23-25, 28-30, 34-36, 38, 40, 41, 44, 45 |
| Doughnut charts | 21 | 4, 6-10, 14-18, 20, 24-27, 29, 30, 32, 33, 44 |
| Pie charts | 14 | 2, 3, 5, 13, 19, 21, 28, 34-36, 38, 41-43 |
| Line charts | 9 | 12, 13, 20, 24, 28, 36, 38, 40, 43 |
| Home screen widgets | 28 | 1, 3-5, 7, 10, 11, 13, 16, 18, 20, 21, 23, 24, 26-31, 33, 37, 38, 41-45 |
| Strategies for managing budgets | | |
| Information ongoing spending within budgets | 23 | 1, 2, 4, 5, 7, 13, 16, 17, 18, 21, 23, 25, 26, 28, 30, 32, 33, 34, 39, 40, 42, 44, 45 |
| Information before reaching budgets' limits | 8 | 7-9, 11, 15-18 |
| Notification on spending over budgets' limits | 9 | 3, 4, 8, 15, 18, 26, 30, 44, 45 |
