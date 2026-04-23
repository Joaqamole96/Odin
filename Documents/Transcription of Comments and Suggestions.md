# Transcription of Comments and Suggestions for "Development of Odin: A Personal Budget Management System Using LSTM and Isolation Forest Algorithms"

## Ma'am Jomariss Baccay Plan, Panel Member

- She asked if the application is a mobile application.
	- Charles answered that the application is both for mobile and web.
- She asked who will use the web-based application.
	- She pressumes that the mobile-based application will be used by the target users, which she promptly asked.
		- Joaquin answered that Filipino young professionals are the target users.
	- She then asked who will use the web side.
		- Joaquin answered that the web side is for additional accessiblity, for when the users want to use the application on their personal computers.
	- She then asked if there are no administrator users in the application.
		- Joaquin confirmed.
	- She then asked if the system is solely for general users.
		- Joaquin confirmed.
	- She then clarified that the system is accessible through web and mobile.
		- Joaquin agreed.
- She asked about the machine learning component.
	- She clarified if the members will be using LSTM for prediction.
		- Charles agreed but corrected "prediction" as "forecast".
	- She then clarified if the members will be using Isolation Forest for detection.
		- Charles agreed but corrected "detection" as "anomaly detection".
	- She asked how users are assigned to the financial behavioral profiles (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated).
		- Joaquin answered that during onboarding the users answer a set of basic questions to determine their profile.
	- She then asked how the users are going to be classified or categorized based on behavior if the system will not use clustering or classification algorithms.
		- Joaquin reiterated his answer that the set of questions concerning income range and obligation weight will determine their profile.
	- She then asked how that will be classified.
		- Joaquin answered that it will be based on the guidelines provided by the Bangko Sentral ng Pilipinas and governmental sources indicating income ranges or brackets.
	- She then said that during registrations it is indicated that inputs will be obtained, extracted, and used on a machine learning algorithm.
	- She further added that the members can choose which machine learning algorithm will be used for that, then asked if we intended not to.
		- Charles answered that, currently, only rule-based algorithms are used for classification.
	- She finally stated that users must be classified into one of the four financial behavioral profiles using any clustering or classification algorithm of the members' choice.
- She asked about swapping behavioral profiles.
	- She asked if a user's behavioral profile can change or be changed over time.
		- Joaquin answered that the user is able to change their behavioral profile.
	- She then asked how often it can be changed.
		- Joaquin answered any time.
	- She expressed brief confusion, then reiterated that the members will be responsible for classification.
	- She further elaborated with an example of her being classified as "Flexible", then asked if her classification can be changed over time.
		- Joaquin confirmed.
	- She then asked if the progress must be tracked that can affect or influence the profile.
	- She finally stated that if this topic were to be approved, and it is, the members need to identify exactly how.
- She asked about the forecasting module.
	- She asked how users with no historical data will be handled.
		- Joaquin answered that the system has a cold-start fallback.
- She asked about the savings goal module.
	- She asked how the savings goal projection will be calculated.
		- Joaquin answered that the calculation is based on the rate that the users is putting into their savings goal.
- She asked about the debt management module.
	- She asked why both the Avalanche and Snowball method for debt payment were included, and what the difference between them is.
		- Joaquin answered that the Snowball method prioritizes the smallest debt first for psychological wins, and the Avalanche method prioritizes the largest debt first for mathematically optimal repayment.
		- Joaquin further explained that some users will prefer one method over the other.
		> NOTE: Though these are simply just recommendations, the users should ultimately be able to pay their debts however they choose.
- She asked about protected categories.
	- She asked why some categories are protected from reduction.
		- Joaquin answered that some categories like the Essentials and Investments should be protected from reduction by the budget recommendation, as they are either essential to the user's day-to-day or are necessary to build wealth.

## Ma'am Janice Pola Congzon, Panel Member

- She asked about Odin.
	- She asked what distinguishes Odin from other personal finance and budgeting apps.
		- Joaquin answered that other systems are "static", i.e. only basic statistics are displayed ().
		- Joaquin further explained that Odin dynamically forecasts expenses, savings, and repayment goals for the next week or month, i.e., the tragectory if the pattern of expenses, savings, and income are continued.
- She asked about the user financial behavioral profiles.
	- She asked how users are categorized, then stated that she pressumed that categorization is similar to "health apps" where the user is categorized based on their answers.
		- Joaquin answered that during their consultation with their Subject Matter Expert, Dr. Pamela A. Go from the College of Business and Financial Science, they asked what the best way to categorize Filipino young professionals.
		- Joaquin continued explaining that they are best described by their income type and obligation weight.
	- She then asked if the profiles are anchored to the spending habits and expenses, i.e., if she were a "Flexible" type, her financial plan and budget would be designed based on that behavior.
		- Joaquin confirmed, saying that the basis for budget building in the system is heavily defined by the profiles.
		- Joaquin further explained that, for example, Stable-Flexible users will have larger allocations for Discretionary expenses, and Variable-Obligated users have smaller allocations for them.
	- She then asked if ultimately the user will decide allocations.
		- Joaquin answered that the budget provided by the system is simply a recommendation, and users are still able to modify it.
- She asked about the Isolation Forest anomaly detection module.
	- She asked what it does.
		- Joaquin explained that when users input expenses for a category that exceeds the thresholds of said category, the system will flag the transaction and alert the user.
	- She then asked what the next steps are after the flagging, like if the system will reduce allocations for that category the next time.
		- Joaquin confirmed, and noted that the protected categories are excluded from the reduction.
- She asked about additional recommendation features and reports.
	- She asked if there are analytics in the System
		- Joaquin answered that the analytics are in the Dashboard page, like income-expense forecasting, spending breakdowns, and budget health.

## Sir Daniel Dellosa, Panel Chairperson

- He asked about user transactions.
	- He asked if inputs are manual and not automatic.
		- Joaquin confirmed, saying that the system cannot integrate banking and e-wallet systems into it due to integration fees and complexity.
	- He then reframed the question, asking if governmental contributions like SSS and Pag-IBIG are automatically deducted in the income input.
		- Charles confirmed, stating that the deductions are not automatic.
	- He then asked again if the contributions are deducted automatically.
		- Joaquin answered that governmental contributions like the SSS and Pag-IBIG are only voluntary when being considered in the budget, and only for Variable users such as freelancers, irregulars, and contract workers, as regular employees have those contributions automatically deducted from their salary as mandated by their employer.
	- He then asked if the system is designed for regular working professionals.
		- Ma'am Plan corrected him, saying that the system is for general users.
		- Joaquin corroborated that the users encompass regular employees, freelancers, and contract workers.
	- He then asked if there is a way to schedule expenses, stating that utility bills, for example, are charged regularly, and even a way to integrate utility apps like the Meralco app.
		- Charles reiterated that integration is hard and beyond the scope of the proposal.