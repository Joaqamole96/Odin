# Specification Revision Points Based on the PRD

**Source PRD:** `Papers/Documents/PRD-Full-Odin-App.md`  
**Target document to revise:** `Papers/Specification.md`  
**Prepared:** 2026-06-11

## Purpose

This document lists the concrete revision points needed for `Specification.md` so it better matches the product scope described in `PRD-Full-Odin-App.md`.

This is not a rewrite of the specification. It is an editing checklist: what to add, revise, remove, or clarify.

## Highest Priority Revisions

1. Add a formal protected-category model.
2. Resolve category suggestions versus no automatic categorization.
3. Add a Reports and Analytics article.
4. Add a complete Authentication and Account Lifecycle section.
5. Add offline-tolerant transaction entry behavior.
6. Align onboarding with PRD requirements.
7. Normalize frozen-model language and remove runtime retraining wording.
8. Align ISO 25010 quality characteristics.
9. Clarify CSV export, backup restore, and excluded transaction imports.
10. Clean unresolved notes and contradictions before final submission.

## Article I: Platform and Target Users

### Revision 1: Standardize the target-user term

**Current issue:**  
The PRD uses "Filipino young professionals," while the specification uses "Filipino working young adults."

**Revise spec to:**  
Use one canonical term throughout:

> Filipino working young adults in Metro Manila, aged 20 to 40.

**Reason:**  
This avoids thesis wording drift between the product document, system specification, paper specification, and evaluation recruitment criteria.

### Revision 2: Define employment capacities

**Current issue:**  
The spec has an unresolved note to define full-time, part-time, self-employed, freelancer, contractual, and gig economy worker.

**Action:**  


**Reason:**  
The target users are delimited by employment status, so the terms must be defensible during evaluation and participant screening.

### Revision 3: Add PRD route map reference

**Current issue:**  
The PRD lists 16 confirmed primary screens, but the specification has no equivalent app route or screen map.

**Action:**  
Add a short section after Platform describing the confirmed primary screens:

1. Login / Register
2. Onboarding questionnaire
3. Profile result
4. Dashboard / overview
5. Add transaction
6. Transactions list / history
7. Recurring transactions
8. Categories / category settings
9. Budget setup
10. Budget recommendation
11. Forecast dashboard
12. Alerts / anomaly review
13. Savings goals
14. Debt accounts
15. Reports / analytics
16. Settings / privacy / account

**Reason:**  
The PRD treats the screen list as confirmed. The specification should give implementation and evaluation a matching navigation surface.

## New Article Needed: Authentication and Account Lifecycle

### Revision 4: Add account registration and login requirements

**Current issue:**  
The PRD has Login/Register, account creation, login/logout tests, protected routes, and account deletion. The specification mostly defines local PIN/biometric authentication and pseudonymized sync, but not account registration.

**Action:**  
Add a new article or section defining:

- Account creation method.
- Login method.
- Logout behavior.
- Protected route behavior.
- Session timeout behavior.
- Multi-device support or explicit no multi-device support.
- Account recovery policy.
- Account deletion authorization.

**Decision needed:**  
Choose whether Odin is:

1. Cloud-account first, with email/password or equivalent login.
2. Local-first, with PIN/biometric unlock and optional sync.
3. Hybrid, with server account plus local PIN/biometric unlock.

**Recommended direction:**  
Use the hybrid model because it fits both documents: server account for Login/Register and sync, local PIN/biometric for device unlock.

### Revision 5: Clarify relationship between login and PIN/biometric

**Current issue:**  
The specification says users set a six-digit PIN during onboarding. It does not say how this relates to Login/Register.

**Action:**  
Add rules:

- Registration creates the user account.
- PIN/biometric unlock protects the local device session.
- Login is required after logout, reinstall, or account switch.
- PIN is required after app lock or biometric failure.

**Reason:**  
Without this, implementation can confuse account authentication with local app unlock.

## Article II: Input and Transaction

### Revision 6: Add transaction history search and filtering

**Current issue:**  
The PRD asks for search, filtering, and date-range views. The spec defines transaction creation and balance updates, but not history browsing behavior.

**Action:**  
Add a transaction history subsection covering:

- Search by merchant name and description.
- Filter by transaction type.
- Filter by category and account.
- Filter by date range.
- Sort newest-first by default.
- Weekly, semi-monthly, monthly, and custom date-range views.

**Reason:**  
Transaction history is a confirmed screen and test target in the PRD.

### Revision 7: Add recurring transaction reminders

**Current issue:**  
The PRD says users want reminders before recurring transactions post. The spec defines recurring generation, pause, edit, and delete, but not reminders before posting.

**Action:**  
Add:

- Reminder timing, such as one day before scheduled generation.
- Reminder delivery through the Alerts and Notifications module.
- User preference for recurring reminder notifications.

**Reason:**  
This is part of the expected recurring transaction workflow.

### Revision 8: Add offline-tolerant transaction entry

**Current issue:**  
The PRD requires draft or offline-tolerant transaction entry. The spec only defines cached offline forecasts.

**Action:**  
Add a subsection under transactions or data sync:

- Users may create transaction drafts while offline.
- Offline transactions are stored locally in encrypted storage.
- The app queues sync until connectivity returns.
- Balance updates locally immediately.
- Server sync conflicts are resolved by deterministic timestamp/order rules.
- Failed syncs surface a non-blocking warning.

**Reason:**  
Offline transaction entry is different from offline forecast display. The PRD explicitly cares about logging despite poor connection.

### Revision 9: Replace runtime model "retraining" wording

**Current issue:**  
The transaction edit/delete section says downstream models are "asynchronously retrained or re-evaluated" within 24 hours. Later privacy sections say no real user data is used for training or fine-tuning during the thesis.

**Action:**  
Replace runtime "retrained" language with:

> Derived aggregates, feature vectors, forecasts, classifications, anomaly scores, and budget actuals shall be recomputed or re-evaluated within twenty-four hours, without updating global model weights.

**Reason:**  
This preserves the PRD behavior while respecting the thesis frozen-model rule.

## Article III: Financial Behavioral Profiles

### Revision 10: Align onboarding fields with PRD

**Current issue:**  
The PRD expects income type, income frequency, fixed obligations, dependents/family support, and protected categories. The spec questionnaire does not fully include these.

**Action:**  
Add onboarding questions for:

- Income frequency or pay cycle.
- Occupation category.
- Employment capacity.
- Gross versus net income.
- Fixed obligations.
- Family support obligations.
- Protected category selection.

**Reason:**  
The Random Forest uses income frequency, and the forecasting fallback uses occupation category. These fields must be collected somewhere.

### Revision 11: Resolve "mixed income"

**Current issue:**  
The PRD says users can enter whether income is stable, variable, or mixed. The spec only has Stable or Variable as the model dimension.

**Action:**  
Either:

1. Remove "mixed" from product language and map users to Stable or Variable only.
2. Keep "mixed" as an onboarding input but map it to Stable or Variable based on coefficient of variation and income source composition.

**Recommended spec wording:**  

> Mixed income is treated as an onboarding descriptor only. For profile classification, the system maps the user to Stable or Variable using the income coefficient of variation or cold-start questionnaire mapping.

**Reason:**  
The four-profile taxonomy depends on binary income stability.

### Revision 12: Add profile override behavior details

**Current issue:**  
The PRD says users can override or request reassessment. The spec covers reassessment and confirmation, but not a clear manual override state.

**Action:**  
Clarify whether users can:

- Manually request reassessment only.
- Temporarily override the displayed profile.
- Permanently override the model recommendation.

**Recommended direction:**  
Allow reassessment request and accept/decline model recommendation, but avoid unsupported arbitrary profile override unless the thesis can justify it.

## Article IV: Expense Groups and Categories

### Revision 13: Add protected categories as first-class data

**Current issue:**  
Protected categories are central in the PRD but missing from the specification.

**Action:**  
Add a protected-category subsection defining:

- Protected category flag.
- Default protected categories.
- User-declared protected categories.
- When protection is set during onboarding.
- How users edit protection later.
- How protected status affects budget recommendations.
- How protected status appears in reports.

**Recommended default protected categories:**

- Essentials.
- Debt and loan minimum payments.
- Insurance premiums.
- Emergency fund contributions.
- User-declared family support obligations.
- User-declared protected categories.

**Reason:**  
The PRD says budget recommendations must not suggest reducing protected categories unless the user explicitly changes protection settings.

### Revision 14: Resolve smart defaults versus no auto-categorization

**Current issue:**  
The PRD wants category suggestions or smart defaults. The spec explicitly forbids automatic categorization.

**Action:**  
Revise the spec to distinguish between:

- **Automatic categorization:** excluded. The system does not save categories without user confirmation.
- **Category suggestions:** allowed. The system may preselect or suggest a category based on last-used category, recurring template, or user-configured defaults, but the user must confirm.

**Recommended wording:**  

> The System shall not automatically assign a category without user confirmation. The System may display category suggestions or smart defaults to reduce entry friction, but the final category assignment remains user-controlled.

**Reason:**  
This preserves the manual-logging thesis rationale while supporting the PRD's UX goal.

### Revision 15: Add missing Filipino-context categories

**Current issue:**  
The PRD specifically names family support, remittances, paluwagan, church/religious donations, barangay/community collections, government contributions, debt payments, insurance, emergency fund, savings, and investments. The specification covers some but not all clearly.

**Action:**  
Add explicit selectable subcategories or documented mappings for:

- Family support.
- Remittances.
- Church or religious donations.
- Barangay or community collections.
- Government contributions.
- Emergency fund.
- Savings.
- Investments as fixed contribution records only, not portfolio tracking.
- Paluwagan as custom subcategory workaround or future-work dedicated module.

**Reason:**  
The PRD's Filipino-context promise should be visible in the actual taxonomy, not just implied.

### Revision 16: Clarify custom category limits

**Current issue:**  
The spec limits users to five custom subcategories per base category. The PRD only says users can customize category labels where appropriate.

**Action:**  
Either keep the limit and explain it, or revise it to a more user-friendly limit.

**Recommended direction:**  
Keep a limit for thesis scope, but justify it as a usability and data-quality constraint.

## Article V: Financial Flows

### Revision 17: Formalize at least one active account

**Current issue:**  
The spec has an unresolved note saying at least one account must be held.

**Action:**  
Convert it into a requirement:

> The System shall always require at least one active account. The last remaining account cannot be deleted.

**Reason:**  
Every transaction requires an account.

### Revision 18: Add account management screen behavior

**Current issue:**  
The PRD includes Settings / privacy / account. The spec defines account data rules but not screen behavior.

**Action:**  
Define where users add, rename, delete, and reorder accounts, and how account deletion warnings appear.

**Reason:**  
This gives implementation a clear user-facing workflow.

## Article VI: Budgeting Module

### Revision 19: Add protected-category constraints to budget recommendation

**Current issue:**  
The PRD says budget recommendation must not suggest reducing protected categories unless the user changes protection settings. The spec has no protected-category constraint.

**Action:**  
Add LP constraints for protected categories:

- Protected categories receive minimum allocations.
- Protected minimums are based on declared obligations, historical average, or user-declared minimum.
- Protected constraints are not relaxed unless the user explicitly changes protection settings.
- In infeasible budgets, the system explains which protected categories make the plan infeasible.

**Reason:**  
This is the most important budget-related PRD promise.

### Revision 20: Clarify budget recommendation inputs

**Current issue:**  
The PRD says budget recommendations consume current balance, profile, protected categories, goals, obligations, and forecasts. The spec lists profile and forecasts but under-specifies protected categories and savings goals as inputs.

**Action:**  
Update module inputs to include:

- Current account balances.
- User profile.
- Forecast income.
- Forecast spending by broad group.
- Protected category settings.
- Known obligations.
- Savings goals and target contribution amounts.
- Debt minimum payments and selected payoff strategy.

**Reason:**  
This aligns implementation with the PRD's "deep module" description.

### Revision 21: Clarify savings and Financial Allocation accounting

**Current issue:**  
The spec can be read as subtracting savings from total budget while also allocating savings under Financial Allocation.

**Action:**  
State clearly whether Financial Allocation is:

1. Inside the total budget, or
2. Set aside before spendable budget is calculated.

**Recommended direction:**  
Treat total budget as all planned allocations, including Financial Allocation. Then define spendable expense budget separately for Essentials, Obligatory, and Discretionary.

**Reason:**  
This prevents double-counting savings.

### Revision 22: Add deficit warning mapping

**Current issue:**  
The PRD asks for deficit warnings. The spec has overspending alerts and LP infeasibility messages, but does not explicitly map them to deficit warnings.

**Action:**  
Add a requirement:

> The System shall generate deficit warnings when projected or actual spending exceeds active budget allocations or when the proposed budget is infeasible.

**Reason:**  
This keeps PRD language traceable to spec behavior.

## Article VII: Forecasting Module

### Revision 23: Reframe personalization as inference personalization

**Current issue:**  
The PRD says forecasts become more personalized as users log transactions. The spec says the LSTM is frozen and no user-data fine-tuning occurs.

**Action:**  
Add wording:

> Forecasts become more personalized because the frozen model receives more user-specific transaction history as input. The model weights are not fine-tuned on user data during the thesis version.

**Reason:**  
This aligns the PRD's UX promise with privacy and ethics constraints.

### Revision 24: Add the primary forecast graph requirement

**Current issue:**  
The PRD specifies a next-month multi-line graph for Essentials, Discretionary, Financial Allocation, and Obligatory spending. The spec defines forecast targets and horizons but not this UI requirement.

**Action:**  
Add a Forecast Visualization subsection:

- Default view is next-month forecast.
- Graph has four lines: Essentials, Obligatory, Discretionary, Financial Allocation.
- User can inspect daily/weekly/monthly aggregates.
- Mobile view must remain readable.

**Reason:**  
This is a confirmed PRD screen behavior and testing item.

### Revision 25: Add forecast metadata requirements

**Current issue:**  
The PRD says forecasts need metadata explaining whether output is personalized or fallback-based.

**Action:**  
Require each forecast result to include:

- Forecast type: fallback or personalized inference.
- Generated timestamp.
- Horizon.
- Granularity.
- Input data window.
- Confidence/explanation text.

**Reason:**  
This supports transparency and testing.

### Revision 26: Resolve IoF threshold contradiction

**Current issue:**  
One part of the spec says Improvement over Fallback has an acceptable threshold of 20 percent or higher. Another says IoF is reported but has no acceptability threshold for the thesis.

**Action:**  
Pick one rule.

**Recommended direction:**  
For thesis evaluation, report IoF without pass/fail threshold. Use the 20 percent value as a stretch benchmark, not an acceptance criterion.

**Reason:**  
This avoids defense problems if LSTM improves less than expected but still satisfies required forecasting metrics.

### Revision 27: Fix synthetic-data companion file naming

**Current issue:**  
The spec references both `model-training-data-design.md` and `synthetic-data-design.md`.

**Action:**  
Use the actual file name consistently.

**Reason:**  
The data generation procedure must be reproducible.

## Article VIII: Anomaly Detection Module

### Revision 28: Add an Occasions model

**Current issue:**  
The PRD says culturally expected spending events should include Christmas, enrollment, family support, paluwagan, and community contributions. The spec only covers Christmas/New Year, Holy Week, barangay fiesta, and whitelist.

**Action:**  
Add a broader "Occasions" concept:

- Christmas/New Year.
- Holy Week.
- Barangay fiesta.
- Enrollment/school periods.
- Family support cycles.
- Paluwagan cycles.
- Community contribution events.
- User-declared planned expenses.

**Reason:**  
This better captures the PRD's cultural spending requirement.

### Revision 29: Add recurring-payment anomaly suppression

**Current issue:**  
The PRD testing section expects recurring-payment suppression. The spec does not clearly define recurring transactions as an anomaly exclusion.

**Action:**  
Add:

> Recurring transactions generated from active templates shall not trigger anomaly alerts unless the generated amount differs from the template amount beyond the configured tolerance.

**Reason:**  
Expected recurring payments should not be flagged as unusual.

### Revision 30: Clarify anomaly features and explanations

**Current issue:**  
The spec's anomaly explanation references amount-to-income ratio, but the listed eight-dimensional feature vector does not include it.

**Action:**  
Either add amount-to-income ratio to the feature vector or remove it from explanation logic.

**Recommended direction:**  
Add it as a derived explanation metric without making it part of the Isolation Forest input, if the team wants to keep the eight-feature model stable.

**Reason:**  
Feature/explanation mismatch can weaken technical defense.

## Article IX: Savings Goal Management

### Revision 31: Decide final savings-goal limit

**Current issue:**  
The spec supports up to five concurrent savings goals but has an unresolved note questioning this limit. The PRD only says multiple goals and prioritization.

**Action:**  
Either:

- Keep five goals and justify it.
- Change the rule to an amount-based or complexity-based limit.

**Recommended direction:**  
Keep five concurrent goals for thesis scope and document it as a usability constraint.

### Revision 32: Connect savings goals more clearly to budgeting

**Current issue:**  
The PRD says budget recommendation consumes goals. The spec says savings goal strategies do not interact with budget surplus handling, but it should still define how active goals influence recommended Financial Allocation.

**Action:**  
Add:

> Active savings goals provide target contribution amounts to the budget recommendation module as Financial Allocation inputs.

**Reason:**  
This keeps savings goals connected to budget recommendations without merging the two modules.

## Article X: Debt Management

### Revision 33: Add PRD-visible out-of-scope notes for debt limitations

**Current issue:**  
The spec excludes credit card accounts and compound interest, but the PRD does not emphasize these limitations.

**Action in spec:**  
Keep the exclusions but make them visible in Debt Management, not only Scope and Delimitations.

**Recommended wording:**  

> The debt module tracks simple-interest debt accounts only. Credit card revolving balances and compound interest are outside the thesis scope.

**Reason:**  
Users and evaluators should not mistake the debt module for a full credit-card management system.

## Article XI: System Alerts and Notifications

### Revision 34: Clarify mandatory versus configurable alerts

**Current issue:**  
The PRD asks for notification preferences. The spec makes budget overspending alerts mandatory.

**Action:**  
Add explicit wording:

> Users may configure delivery channels for all alert categories. Users may disable selected alert categories except mandatory budget overspending alerts, which remain visible in-app.

**Reason:**  
This preserves user control while keeping critical warnings.

### Revision 35: Add recurring transaction reminders to alert categories

**Current issue:**  
The PRD asks for reminders before recurring transactions post. The alert article does not list recurring reminders as an alert category.

**Action:**  
Add recurring transaction reminders as an alert source.

**Reason:**  
Recurring reminders need a delivery path.

## Article XII: Explainability

### Revision 36: Add explanation fields to all intelligent outputs

**Current issue:**  
The PRD says profile classification, forecasting, anomaly detection, and recommendation outputs must include user-facing explanations. The spec mostly covers this, but reporting and dashboard consumption are not explicitly tied to explanation fields.

**Action:**  
Require each intelligent output object to store:

- Explanation summary.
- Explanation method.
- Input window or basis.
- Generated timestamp.
- Fallback/personalized flag where applicable.

**Reason:**  
This makes explanations testable and reusable across dashboard, reports, and detail screens.

## Article XIII: System and Algorithm Evaluation

### Revision 37: Align ISO 25010 quality characteristics

**Current issue:**  
The PRD lists portability, but the specification evaluates maintainability instead.

**Action:**  
Choose one:

1. Replace maintainability with portability.
2. Add portability and evaluate seven characteristics.
3. Update the PRD to use maintainability instead of portability.

**Recommended direction:**  
Evaluate seven characteristics if the thesis scope allows it. If not, choose the six that best match the panel's expectations and update both documents.

### Revision 38: Add PRD-to-spec traceability matrix requirement

**Current issue:**  
The PRD has 85 user stories. The spec has article-based requirements. There is no explicit mapping.

**Action:**  
Require an appendix mapping:

- PRD user story.
- Specification requirement.
- Screen.
- Test case.
- Evaluation metric.

**Reason:**  
This makes the thesis easier to defend and makes implementation scope clearer.

### Revision 39: Resolve evaluation threshold mismatches

**Current issue:**  
Forecasting remedial thresholds are inconsistent across sections.

**Action:**  
Normalize:

- LSTM MAE/RMSE/sMAPE thresholds.
- IoF reporting or pass/fail role.
- Three-week versus fourteen-day failure trigger.
- Synthetic evaluation versus user evaluation.

**Reason:**  
Metrics must be stable before writing Chapter 4 results.

## Article XIV: Data Privacy, Security, and Ethical Compliance

### Revision 40: Clarify consent order

**Current issue:**  
The PRD says privacy-conscious users should understand collected data before onboarding. The spec says consent appears before transaction entry and separate research opt-in appears during onboarding.

**Action:**  
Define this order:

1. Privacy notice before onboarding.
2. App-use consent before collecting onboarding financial data.
3. Optional research-data consent as a separate screen.
4. Transaction entry only after required app-use consent.

**Reason:**  
Onboarding itself collects financial data, so consent should happen before onboarding data entry, not only before transactions.

### Revision 41: Remove or future-scope "Remove from Training"

**Current issue:**  
The spec includes Settings -> Privacy -> Remove from Training, but also says no real user data is used for training in the thesis.

**Action:**  
Either remove this from thesis requirements or explicitly mark it as future work, not an implemented setting.

**Recommended direction:**  
Remove from thesis UI. Keep as future-work note only.

**Reason:**  
A setting that has no runtime effect can confuse users and evaluators.

### Revision 42: Clarify CSV export and restore

**Current issue:**  
The spec allows CSV import for restore, but later excludes CSV/spreadsheet import.

**Action:**  
Separate:

- CSV export for user data portability: included.
- External transaction import from banks/spreadsheets: excluded.
- Odin-generated backup restore import: included only if the team wants restoration.

**Recommended wording:**  

> The System shall allow CSV export for data portability. The System shall not support importing external CSV or spreadsheet transaction files for normal transaction creation. If backup restoration is supported, it shall accept only Odin-generated export files.

**Reason:**  
This resolves the contradiction while preserving portability.

### Revision 43: Resolve retention-period basis

**Current issue:**  
The thirteen-month retention rule is repeatedly marked provisional.

**Action:**  
Either validate thirteen months with sources or change to a better-supported period.

**Reason:**  
Retention is a privacy and ethics requirement, not just an implementation detail.

## Article XV: System Scope and Delimitations

### Revision 44: Align out-of-scope wording with PRD

**Current issue:**  
The spec has a stricter out-of-scope list than the PRD.

**Action:**  
Keep the stricter list, but make sure each excluded item is reflected in PRD-facing scope notes or screen descriptions:

- Automated bill payment.
- Credit score monitoring.
- Tax computation.
- Dedicated paluwagan module.
- Credit card accounts.
- Compound interest for revolving debt.
- External CSV/spreadsheet transaction import.

**Reason:**  
The PRD should not accidentally imply these features are included.

### Revision 45: Clarify paluwagan handling

**Current issue:**  
The PRD names paluwagan as part of Filipino-context categories, while the spec excludes paluwagan as a dedicated module and treats it as a custom subcategory workaround.

**Action:**  
Add explicit wording:

> Paluwagan is supported only as a manually tracked custom subcategory under Financial Allocation for the thesis version. A dedicated paluwagan tracker is outside scope.

**Reason:**  
This keeps Filipino-context support without expanding thesis scope.

## New Article Needed: Reports and Analytics

### Revision 46: Add a Reports and Analytics module

**Current issue:**  
The PRD includes Reports / Analytics as a confirmed screen and module. The spec does not define it.

**Action:**  
Add a new article defining:

- Date-range reports: weekly, monthly, custom.
- Category breakdown reports.
- Budget versus actual reports.
- Forecast versus actual reports.
- Savings progress reports.
- Debt progress reports.
- Protected category and obligation reports.
- Export or review behavior.
- Mobile and desktop presentation requirements.

**Reason:**  
This is a first-class PRD screen and cannot remain only implied by other modules.

### Revision 47: Add dashboard-to-reports relationship

**Current issue:**  
The PRD says dashboard cards show current balance, budget status, recent transactions, alerts, goals, and forecast highlights. The spec has no dashboard article.

**Action:**  
Either add dashboard requirements to Reports and Analytics or create a Dashboard article defining:

- Current balance summary.
- Budget status.
- Recent transactions.
- Active alerts.
- Savings goal highlights.
- Debt highlights.
- Forecast highlights.
- Negative balance badge.

**Reason:**  
Dashboard is the user's main app overview.

## Paper Specification Cleanup

### Revision 48: Remove unresolved editorial notes

**Current issue:**  
`Specification.md` contains notes like:

- "Define each..."
- "May need sections..."
- "ACTUALLY this is debatable..."
- "No. Just normal agile."
- "There's no Chapter 4 and 5."
- "Update the references minimum."

**Action:**  
Resolve these into final requirements or move them into `Papers/Open-Items.md`.

**Reason:**  
The formal specification should not contain unresolved team commentary.

### Revision 49: Separate system specification from paper specification

**Current issue:**  
`Specification.md` contains both system requirements and thesis paper requirements.

**Action:**  
Consider splitting:

- `Papers/System-Specification.md`
- `Papers/Paper-Specification.md`

**Reason:**  
The PRD maps to the system specification, not necessarily the paper-writing checklist. Splitting reduces confusion.

## Revision Checklist by Priority

### Critical

- Add protected-category model.
- Resolve category suggestions versus no auto-categorization.
- Add authentication/account lifecycle.
- Add Reports and Analytics article.
- Remove runtime retraining language that conflicts with frozen models.
- Resolve CSV import/export contradiction.

### Major

- Add offline transaction entry.
- Align onboarding fields with PRD.
- Add forecast visualization requirements.
- Add dashboard requirements.
- Add transaction history search/filter/date-range behavior.
- Add recurring transaction reminders.
- Add Occasions model for cultural spending.
- Align ISO evaluation characteristics.

### Moderate

- Clarify mixed income handling.
- Clarify savings and Financial Allocation accounting.
- Add forecast metadata requirements.
- Resolve IoF and evaluation threshold conflicts.
- Clarify mandatory versus configurable alerts.
- Add traceability matrix requirement.
- Clarify paluwagan handling.

### Minor

- Standardize target-user wording.
- Define employment capacities.
- Formalize at least one active account.
- Resolve savings-goal limit note.
- Clean paper-spec editorial notes.
- Fix companion file naming.

## Suggested Revision Sequence

1. Clean internal contradictions in `Specification.md`.
2. Add missing PRD-backed modules: Authentication, Reports/Analytics, Dashboard.
3. Add protected categories and category suggestions.
4. Update onboarding and transaction history requirements.
5. Add offline transaction behavior.
6. Update forecasting and anomaly wording.
7. Align privacy, CSV, and evaluation sections.
8. Clean paper-spec notes.
9. Create a PRD-to-spec traceability matrix.

## Final Note

The PRD does not require weakening the specification. In most cases, the right move is to keep the specification's stricter thesis and algorithm detail, then add the missing product-facing behaviors from the PRD. The risky parts are where the spec contradicts the PRD or itself: protected categories, category suggestions, authentication, reports, offline entry, frozen-model language, CSV import, and ISO evaluation.
