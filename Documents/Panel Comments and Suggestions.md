# Panel Comments and Suggestions

## Ma'am Jomariss Baccay Plan

- She raised the nature of the application and whether it was mobile or web-based.
  - The application was clarified to be accessible on both mobile and web platforms. The mobile application was intended for the primary target users (Filipino young professionals), while the web platform served as an additional access point for users who preferred to use the application on a personal computer. There were no administrator users — the system was solely for general users.

- She raised the machine learning components of the system.
  - The system used **LSTM** for expense and income **forecasting**, and **Isolation Forest** for **anomaly detection**. The distinction between "prediction" and "forecasting", and between "detection" and "anomaly detection", was noted and clarified.

- She raised the classification of users into financial behavioral profiles (Stable-Flexible, Stable-Obligated, Variable-Flexible, Variable-Obligated) and noted that a clustering or classification algorithm must be used for this purpose.
  - It was explained that during onboarding, users answered a set of questions regarding their income type and obligation weight. These answers, guided by income brackets from the Bangko Sentral ng Pilipinas and other governmental sources, determined the user's profile. However, the panel noted that this rule-based approach was insufficient and required that a proper **clustering or classification algorithm** be used to classify users into their respective profiles.

- She raised the need to track changes in the user's behavioral profile over time.
  - It was confirmed that users could change their behavioral profile. The panel required that profile changes be tracked progressively, and that the exact mechanism by which user behavior and progress influenced or updated the profile be clearly defined.

- She raised the handling of users with no historical data in the forecasting module.
  - The system was explained to have a **cold-start fallback** for new users without historical data.

- She raised how savings goal projections were calculated.
  - Savings goal projections were calculated based on the rate at which the user was contributing to their savings goal over time.

- She raised the inclusion of both the Avalanche and Snowball debt repayment methods and the difference between them.
  - The **Snowball method** prioritized the smallest debt first, providing psychological wins through early payoffs. The **Avalanche method** prioritized the highest-interest debt first, offering mathematically optimal repayment. Both methods were included because different users would prefer different approaches. Ultimately, users retained full control over how they paid their debts, with the system providing these as recommendations only.

- She raised why certain budget categories were protected from reduction.
  - Categories such as **Essentials** and **Investments** were protected from budget reduction recommendations because they were either critical to the user's daily needs or necessary for building long-term financial health.

---

## Ma'am Janice Pola Congzon

- She raised what distinguished Odin from other personal finance and budgeting applications.
  - Unlike other systems that displayed only basic static statistics, Odin **dynamically forecasted** expenses, savings, and repayment goals for the next week or month. It projected the user's financial trajectory based on continued patterns of income, expenses, and savings — making it an active financial planning tool rather than a passive tracker.

- She raised how users were categorized into financial behavioral profiles and whether the profiles were anchored to spending habits and financial planning.
  - During consultation with their Subject Matter Expert, Dr. Pamela A. Go from the College of Business and Financial Science, it was determined that Filipino young professionals were best described by their **income type** (Stable or Variable) and **obligation weight** (Flexible or Obligated). The resulting profiles served as the foundation for budget-building in the system. For example, Stable-Flexible users received larger allocations for Discretionary expenses, while Variable-Obligated users received smaller allocations for the same. Users retained the ability to modify these allocations, as the budget was a recommendation, not a mandate.

- She raised what the Isolation Forest anomaly detection module did and what steps the system took after flagging an anomaly.
  - When a user's spending in a category exceeded the defined threshold, the system flagged the transaction and alerted the user. Following the flag, the system suggested that excess spending be **redirected to higher-priority categories** such as emergency funds, and reduced the allocation for the flagged category in the next budgeting period. Protected categories were excluded from reduction.

- She raised whether analytics and reporting features were available in the system.
  - Analytics were available on the **Dashboard**, including income-expense forecasting, spending breakdowns, and budget health indicators.

---

## Sir Daniel Dellosa, Panel Chairperson

- He raised whether transaction inputs were manual or automatic, and whether government contributions such as SSS and Pag-IBIG were automatically deducted from income.
  - All transaction inputs were **manual**. The system could not integrate with banking or e-wallet systems due to integration fees and technical complexity. Regarding government contributions, **regular employees** had SSS and Pag-IBIG automatically deducted from their salary by their employer as required by law, so these were already reflected in their net income input. For **variable-income users** such as freelancers and contract workers, these contributions were voluntary considerations and could be optionally accounted for in their budget.

- He raised whether a feature for scheduling recurring expenses existed, and whether integration with utility applications such as the Meralco app was feasible.
  - Integration with third-party utility applications was outside the scope of the proposal due to technical complexity. The feasibility of a recurring expense scheduling feature was acknowledged as a valid consideration for the system.
