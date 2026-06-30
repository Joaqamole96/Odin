# Specification and PRD Alignment Report

**Compared documents**

- `Papers/Specification.md`
- `Papers/Documents/PRD-Full-Odin-App.md`

**Date reviewed:** 2026-06-11

## Executive Summary

The two documents are aligned at the concept level. Both describe Odin as a mobile-first, web-accessible personal finance management system for Filipino working young adults in Metro Manila. Both include manual and recurring transaction entry, financial behavioral profiles, category-based budgeting, forecasting, anomaly detection, savings goals, debt management, alerts, privacy controls, and thesis evaluation.

They are not fully aligned as implementation contracts. The PRD is broad and product-facing, while `Specification.md` is much more detailed, thesis-oriented, and sometimes narrower than the PRD. The largest gaps are:

1. Protected categories are core in the PRD but not formally specified in `Specification.md`.
2. The PRD asks for category suggestions or smart defaults, while the specification explicitly excludes automatic categorization.
3. The PRD includes a reporting/analytics module, but the specification has no full user-facing reporting module.
4. The PRD includes Login/Register and account workflows, while the specification mostly defines local PIN/biometric authentication and pseudonymized sync.
5. The PRD asks for offline-tolerant transaction entry, while the specification only defines cached offline forecasts.
6. The specification contains internal contradictions around frozen models, retraining, CSV import, ISO 25010 attributes, IoF thresholds, and training-corpus removal.

Best effort conclusion: the documents should be treated as broadly compatible, but `Specification.md` needs cleanup before it can serve as the authoritative app specification.

## Severity Legend

- **Critical:** Direct contradiction or likely implementation blocker.
- **Major:** PRD feature missing from the specification, or specification behavior missing from PRD.
- **Moderate:** Scope, wording, or traceability issue that can confuse implementation or defense.
- **Minor:** Editorial, naming, or paper-structure issue.

## Alignment Matrix

| Area | PRD position | Specification position | Alignment |
| --- | --- | --- | --- |
| Platform | Mobile-first with web access | Mobile-first, 320-450 dp support, desktop web container up to 1200 px | Aligned |
| Target users | Filipino young professionals in Metro Manila | Filipino working young adults, age 20-40, live/work in Metro Manila, employed | Mostly aligned |
| Authentication | Login/Register, secure login, account management | PIN/biometric auth, pseudonymization, some logged-in sync wording | Major gap |
| Onboarding | Income type, frequency, obligations, dependents, protected categories | Monthly income, stability, variability, obligation ratio, dependents, debts, gross/net income | Major gap |
| Transactions | Manual income, expense, transfer, recurring, edit, delete, search/filter | Detailed validations, transfer handling, negative balance handling, edit/delete retention limit | Mostly aligned, with spec-only constraints |
| Categories | Filipino-context categories, protected/default categories, suggestions/smart defaults | PCOICOP-based categories, custom subcategories, no auto-categorization | Critical conflict |
| Budgeting | Profile-aware recommendations, protected categories, accept/modify/reject, surplus | LP solver, strategy templates, constraints, surplus handling | Mostly aligned, protected-category gap |
| Forecasting | Cold-start and personalized forecasts, next-month graph | LSTM, cold-start fallback, frozen model, cloud inference, cached offline forecasts | Mostly aligned, wording conflict |
| Anomaly detection | Unusual spending, whitelisting, cultural exceptions, frequency controls | Isolation Forest, dynamic threshold, holiday exclusions, whitelist, cooldowns | Mostly aligned, cultural-exception gaps |
| Savings goals | Target/date progress, linked contributions, prioritization | Detailed goal limits, contribution schedules, progress states, strategies | Aligned |
| Debt management | Debt accounts, interest, minimum payments, Avalanche/Snowball, payoff projections | Detailed debt accounts, simple interest, hardship mode, alerts | Aligned with spec-only constraints |
| Alerts | Alerts, anomaly review, notification preferences | Detailed in-app/push delivery, mandatory budget alerts, cooldowns | Mostly aligned |
| Reports/analytics | Dedicated reports module and screen | No complete reporting module; only scattered reporting/evaluation references | Major gap |
| Privacy/security | RA 10173 expectations, consent, deletion/export | Detailed consent, retention, encryption, deletion, export, pseudonymization | Mostly aligned, internal issues |
| Evaluation | ISO 25010, SUS, model metrics | Detailed ISO/SUS/model thresholds | Mostly aligned, ISO mismatch |
| Out of scope | Bank/e-wallet APIs, OCR, auto import, investment portfolio, multi-currency, etc. | Same plus bill payment, credit score, tax, paluwagan module, credit cards, compound interest | Mostly aligned, spec is stricter |

## Detailed Differences

### 1. Platform and Target Users

**Assessment:** mostly aligned.

The PRD says Odin is mobile-first with web access. The specification says the system must be mobile-first, fit 320-450 dp without horizontal scrolling, and provide desktop web support with a 1200 px max-width container.

The target group is also aligned: Filipino young professionals or working young adults in Metro Manila. The specification is stricter because it defines age 20-40, geography, and employment status.

**Lapses**

- **Minor:** The specification still has a note to define employment capacities such as full-time, part-time, self-employed, freelancer, contractual, and gig economy worker. This weakens the target-user definition.
- **Moderate:** The PRD uses "young professionals"; the specification uses "working young adults." These are compatible, but the thesis should choose one canonical term.

**Recommended fix**

Use "Filipino working young adults in Metro Manila, age 20-40" as the canonical thesis term. Define each employment capacity in the specification.

### 2. Authentication and Account Model

**Assessment:** major gap.

The PRD explicitly includes Login/Register, account creation, secure login, protected routes, account deletion, privacy settings, and data export/review. The specification defines local PIN/biometric authentication, encrypted local storage, pseudonymization before server upload, and synchronization "if the user is logged in."

The specification does not clearly define:

- Whether registration uses email/password, magic link, device-only account, or another method.
- What a server account is.
- Whether users can use multiple devices.
- How account recovery works.
- How Login/Register relates to six-digit PIN and biometric login.
- Whether account deletion requires server identity confirmation.

**Why this matters**

Implementation can split in two directions:

- A normal cloud-account product with email/password or equivalent login.
- A local-first app with PIN/biometric unlock and pseudonymized server sync.

Those are different systems. The PRD implies the first; the specification mostly describes the second.

**Recommended fix**

Add an Authentication and Account Lifecycle article or section to `Specification.md` covering:

- Account creation fields.
- Login method.
- Local unlock method.
- Session behavior.
- Multi-device sync.
- Account deletion authentication.
- Password/PIN recovery policy.

### 3. Onboarding Questionnaire

**Assessment:** major gap.

The PRD expects onboarding to capture income type, income frequency, fixed obligations, dependents/family support, and protected categories. The specification questionnaire includes monthly income, income stability, income variability, obligation percentage, dependents, and debts. It also separately requires asking whether the user records gross or net income.

**Differences**

- **Income type mismatch:** The PRD says income can be stable, variable, or mixed. The specification only models income stability as Stable or Variable.
- **Income frequency gap:** The PRD explicitly asks for income frequency. The specification uses income frequency as a Random Forest feature but does not list it as an onboarding question.
- **Occupation gap:** The forecasting fallback uses occupation category during onboarding, but the questionnaire does not include occupation.
- **Protected categories gap:** The PRD asks users to mark important expense categories as protected. The specification does not define this onboarding step.
- **Gross/net income:** The specification asks whether income is gross or net. The PRD does not mention this, but it is important for mandatory contributions.

**Recommended fix**

Update the onboarding questionnaire to include:

- Occupation category.
- Income frequency or pay cycle.
- Income source/type using the specification's final taxonomy.
- Gross vs net income.
- Fixed obligations.
- Protected category selection.

If "mixed income" remains in the PRD, the profile taxonomy must either support it or explain how it maps to Stable/Variable.

### 4. Transactions and Ledger Behavior

**Assessment:** mostly aligned, but the specification is stricter.

Both documents support manual income, expense, transfer, and recurring transactions. The specification adds concrete ledger rules: required fields, transfer source/destination accounts, negative balance warnings, ISO 8601 timestamps, recurring postponement, and immediate balance recomputation.

**Differences**

- **Search/filter not specified enough:** The PRD asks users to search/filter history and view by date range. The specification defines storage and update rules, but does not fully define transaction history filters, search fields, sorting, or pagination.
- **Edit/delete retention limit:** The PRD says users can edit/delete mistakes. The specification says transactions older than thirteen months cannot be edited or deleted. This is a spec-only restriction.
- **Model update language conflict:** The specification says transaction edits/deletes cause downstream models to be "retrained or re-evaluated" within 24 hours, but later says thesis models are frozen and not retrained on user data.
- **Recurring negative-balance behavior:** Manual expenses may proceed after a warning, but recurring expenses/transfers are postponed if they would go negative. The PRD does not mention this behavioral difference.

**Recommended fix**

Add a transaction history/search subsection to the specification. Replace "retrained or re-evaluated" with "features, derived aggregates, forecasts, classifications, and anomaly baselines are recomputed or re-run as applicable." Keep "retraining" only for offline synthetic-data development.

### 5. Categories, Smart Defaults, and Protected Categories

**Assessment:** critical conflict.

The PRD makes categories a major product feature. It expects Filipino-context categories, broad groups, category customization, ambiguity reduction, smart defaults/suggestions, protected categories, and protected-category reporting.

The specification defines PCOICOP-based categories, broad groups, custom subcategories, and detailed-to-broad mappings. However, it explicitly says:

- The system shall not perform automatic categorization.
- All category assignments must be made by the user at transaction entry.
- Optional auto-categorization is future work.

That conflicts with the PRD user story for "category suggestions or smart defaults."

**Protected-category gap**

The PRD repeatedly treats protected categories as first-class:

- Users mark categories as protected.
- Budget recommendations must respect protected categories.
- Defaults include essentials, debt/loan repayments, insurance, and emergency fund.
- Reports should show protected categories and obligations.

The specification does not define:

- A protected-category field.
- Default protected categories.
- User-declared protected categories.
- How protected status affects LP constraints.
- Whether protected categories can be relaxed during infeasibility handling.
- How protected categories appear in reports.

**Filipino-context category differences**

The PRD names family support, remittances, paluwagan, church/religious donations, barangay/community collections, government contributions, debt payments, insurance, emergency fund, savings, and investments.

The specification covers some of these through broad categories or workarounds:

- Family support is included as an obligation.
- Government contributions are included.
- Debt payments and savings are represented.
- Paluwagan is explicitly not a dedicated module and is only approximated by a custom subcategory.
- Church/religious donations and barangay/community collections are not clearly specified as selectable categories.
- Remittances appear as an income example or financial service fee, but not clearly as a distinct user-facing category.

**Recommended fix**

Decide one of these:

1. Keep the PRD feature and revise the specification:
   - Allow non-automatic "suggestions" without auto-saving the category.
   - Define smart defaults as UI defaults based on last-used category, not ML auto-categorization.
   - Add protected categories as explicit domain state.
2. Remove category suggestions and protected categories from the PRD.

The better product decision is option 1, but the thesis scope must frame suggestions as low-risk UI assistance, not automated classification.

### 6. Accounts and Financial Flows

**Assessment:** mostly aligned, with spec-only detail.

The specification defines multiple user-defined accounts, a default Cash account, account deletion behavior, transfers, negative balances, and integer centavo storage. The PRD mentions account management only broadly.

**Differences**

- The specification supports up to ten user-defined accounts. The PRD does not mention account limits.
- The specification allows negative balances after confirmation. The PRD does not mention negative balances.
- The specification has a note that at least one account must always exist, but this is not yet formalized.
- The PRD does not describe account deletion/reassignment behavior.

**Recommended fix**

Keep the specification detail. Add one PRD implementation note that Odin supports multiple accounts but is not a bank/e-wallet integration.

### 7. Budgeting and Recommendation

**Assessment:** mostly aligned, with important gaps.

The PRD expects profile-aware budget recommendations using forecasts, goals, obligations, protected categories, explanations, user overrides, surplus handling, and deficit warnings. The specification defines budget periods, strategy templates, LP constraints, profile priorities, surplus handling, explanations, and accept/modify/reject behavior.

**Differences**

- **Protected categories missing:** The PRD says protected categories must not be reduced unless the user changes protection settings. The specification has hard constraints for obligations, savings, essentials floors, and discretionary caps, but no protected-category model.
- **Goals as recommendation input:** The PRD says budget recommendation consumes goals. The specification connects savings/debt to budgeting indirectly, but does not clearly describe savings goals as LP inputs except through savings targets.
- **Deficit warnings:** The PRD asks for deficit warnings. The specification handles infeasible LP and overspending alerts, but should explicitly map these to "deficit warnings."
- **Potential budget math ambiguity:** The specification says total allocations equal forecast income multiplied by `(1 - target savings rate)`, while also requiring Financial Allocation to be at least forecast income multiplied by the target savings rate. Because Financial Allocation includes savings, this can read like savings is both removed before budgeting and included inside the budget. This needs a clearer accounting model.

**Recommended fix**

Add a protected-category constraint model:

- Protected categories get minimum allocations based on historical average, declared minimum, or known obligation.
- Protected constraints are hard by default.
- User can manually unprotect or relax them.
- Infeasibility handling must say whether protected constraints relax before or after savings/essentials.

Clarify whether Financial Allocation is inside total budget or set aside before total budget.

### 8. Forecasting

**Assessment:** mostly aligned, with wording and scope issues.

The PRD expects spending forecasts, category forecasts, total forecasts, cold-start forecasts, calendar/payday effects, improving personalization, and a next-month graph for the four broad groups.

The specification defines:

- LSTM with fixed architecture.
- Four forecast targets: broad-group spending, income, savings trajectory, debt balance.
- Seven, fourteen, thirty, and ninety-day horizons.
- Population fallback for fewer than thirty days of history.
- Calendar/payday/holiday features.
- Frozen pre-trained model for thesis version.
- Cloud-hosted inference and cached offline forecasts.

**Differences**

- **Personalization wording:** The PRD says forecasts improve and become more personalized as users log transactions. The specification says the model is frozen and does not fine-tune on user data. These can align only if "personalized" means personalized inputs at inference time, not personalized training.
- **Offline gap:** The specification supports cached forecasts offline, but the PRD asks for offline-tolerant transaction entry.
- **Next-month graph:** The PRD names a next-month multi-line graph as the primary forecast visualization. The specification defines horizons and targets but does not specify the chart as a primary UI requirement.
- **File reference inconsistency:** The specification references `model-training-data-design.md` and then says the companion file is `synthetic-data-design.md`. One source name should be used.
- **IoF threshold conflict:** Forecasting section gives Improvement over Fallback an acceptable threshold of 20 percent or higher. Evaluation section later says IoF should be reported but has no acceptability threshold.

**Recommended fix**

Revise PRD language to "forecasts become more personalized at inference time as user history accumulates." Add the primary forecast graph requirement to the specification. Resolve the IoF threshold and companion-file naming.

### 9. Anomaly Detection and Overspending

**Assessment:** mostly aligned, but cultural exception coverage differs.

The PRD expects anomaly alerts, budget-risk alerts, explainability, whitelisting intentional outliers, culturally expected event handling, and alert frequency controls. The specification defines Isolation Forest, eight anomaly features, dynamic thresholding, whitelisting, cultural-period exclusions, overspending alerts, cooldowns, bundling, snooze, and explanations.

**Differences**

- **Cultural exceptions are narrower in specification:** PRD mentions Christmas, enrollment, family support, paluwagan, and community contributions. Specification excludes Christmas/New Year, Holy Week, barangay fiesta, and whitelist. Enrollment, family support spikes, paluwagan, and community contributions are not fully covered.
- **Feature/explanation mismatch:** The anomaly feature vector does not clearly include amount-to-income ratio, but the explanation section mentions amount-to-income ratio as a baseline. This creates traceability confusion.
- **Profile-aware anomaly baselines:** The PRD and specification imply profile-aware behavior, but the feature vector does not clearly include profile as one of the eight dimensions, while module relationships say Isolation Forest receives the profile label.
- **Recurring-payment suppression:** The PRD testing decisions mention recurring-payment suppression. The specification excludes cultural periods and whitelisted transactions, but recurring transaction suppression is not clearly listed as an anomaly exclusion.

**Recommended fix**

Add an "Occasions and Expected Spending" model that includes:

- Holidays.
- Enrollment/school periods.
- Barangay/community obligations.
- Family support cycles.
- User-declared planned events.
- Paluwagan approximations.
- Recurring payment suppression.

Then explicitly map these to anomaly suppression, informational alerts, or normal alerts.

### 10. Savings Goals

**Assessment:** aligned, with spec-only constraints.

The PRD expects savings goals with target amounts/dates, linked contributions, progress states, projected completion dates, and prioritization. The specification covers these in detail, including max five concurrent goals, amount limits, contribution frequency, source accounts, skipped contributions, progress states, strategies, and notifications.

**Differences**

- The PRD does not mention the maximum of five concurrent goals.
- The specification has a note questioning whether count-based goal limits are the right approach.
- The PRD does not distinguish budget surplus handling from savings surplus allocation strategies; the specification says they operate independently.

**Recommended fix**

Keep the specification detail, but resolve the open note about goal limits. If max five remains, add it to the PRD or screen description.

### 11. Debt Management

**Assessment:** aligned, with spec-only constraints.

The PRD expects debt accounts, interest rates, minimum payments, Avalanche/Snowball comparison, payoff dates, and strategy switching. The specification defines debt fields, simple interest, due dates, remaining balance, creditor information, Avalanche/Snowball behavior, hardship mode, minimum-payment overrides, and alerts.

**Differences**

- The specification excludes credit card accounts and compound interest. The PRD only broadly excludes licensed advice and investment features.
- The specification uses simple interest for all debts, which may not match real-world revolving debt behavior.
- The PRD does not mention hardship mode, creditor contact info, or below-minimum payment overrides.

**Recommended fix**

Add credit card accounts and compound interest to the PRD out-of-scope list. Keep hardship mode in the specification because it supports ethical decision support.

### 12. Alerts and Notifications

**Assessment:** mostly aligned.

The PRD expects anomaly alerts, likely-over-budget alerts, alert explanations, intentional-outlier marking, culturally expected spending handling, alert frequency controls, and notification preferences. The specification defines five alert categories, push/in-app behavior, grouping, action buttons, dismissals, notification history, cooldowns, and mandatory budget alerts.

**Differences**

- The specification makes budget overspending alerts mandatory. The PRD only says users want notification preferences, which could imply all categories are configurable.
- The specification excludes email digests. The PRD does not mention email.
- The specification stores alert history locally and syncs if logged in, but the account model is not defined.

**Recommended fix**

Clarify in the PRD that some safety-critical budget alerts cannot be disabled, though delivery method may be configured.

### 13. Reports and Analytics

**Assessment:** major gap.

The PRD includes a Reports / Analytics screen and a reporting module. It expects:

- Week/month/custom date range reports.
- Planned vs actual vs forecasted comparisons.
- Protected-category and obligation reports.
- Savings and debt progress reports.
- Wider web analytics views.

The specification does not include a dedicated reporting module. It mentions transaction history, evaluation reporting, forecast dashboards, savings/debt views, and export, but does not define user-facing reports.

**Recommended fix**

Add a Reports and Analytics article to `Specification.md` defining:

- Report types.
- Date ranges.
- Metrics.
- Charts/tables.
- Data sources.
- Export behavior.
- Mobile vs desktop presentation.
- Protected-category/obligation breakdowns, if protected categories remain in scope.

### 14. Privacy, Consent, and Security

**Assessment:** mostly aligned, but with internal issues.

The PRD expects RA 10173-aligned privacy, consent, data minimization, secure handling, access, correction, deletion, account management, and export/review. The specification provides detailed privacy and security controls, including consent, purpose limitation, retention, export, deletion, encryption, local storage, PIN/biometric authentication, pseudonymization, and inference-minimization.

**Differences and issues**

- **Consent timing:** The PRD wants users to understand data collection before onboarding. The specification requires consent before transaction entry and separate research opt-in during onboarding. These should be ordered clearly.
- **Data retention unresolved:** Thirteen months is repeated as provisional and requires validation.
- **Remove from Training contradiction:** The specification includes a user-facing Remove from Training setting, but also says no real user data is used for training in the thesis. It then duplicates this section.
- **Deletion confirmation and email:** The specification says users may receive email confirmation if an email exists, but the account model does not define email.
- **Import/export contradiction:** The specification allows CSV import for restore in disaster recovery but later excludes CSV/spreadsheet import.

**Recommended fix**

Make privacy states explicit:

- App-use consent.
- Optional research-data consent.
- Export.
- Delete account.
- Remove from future training, marked as future-version only or removed from thesis UI.

Resolve the thirteen-month retention basis before final defense.

### 15. Evaluation and Thesis Requirements

**Assessment:** mostly aligned, with spec contradictions.

The PRD says modules and model outputs must be testable through functional tests, model metrics, ISO 25010, and SUS. The specification gives detailed evaluation criteria.

**Differences**

- **ISO attribute mismatch:** PRD lists functional suitability, usability, performance efficiency, security, reliability, and portability. The specification evaluates functional suitability, performance efficiency, usability, reliability, security, and maintainability. Portability is missing; maintainability is added.
- **IoF threshold conflict:** Forecasting module says IoF has an acceptable threshold of 20 percent or higher. Evaluation section says IoF is reported but has no thesis acceptability threshold.
- **Failure threshold mismatch:** Forecasting evaluation mentions three consecutive weeks for remedial action; failure conditions mention fourteen consecutive days for LSTM MAE.
- **Manual test count:** The specification says 50 manual test cases mapped to Articles I-XII. The PRD contains 85 user stories, so traceability will need careful mapping.

**Recommended fix**

Create a traceability matrix:

- PRD user story -> Specification requirement -> Test case -> Evaluation metric.

Then choose whether ISO portability or maintainability is in scope. If both are needed, evaluate seven characteristics or justify the selected six.

### 16. Scope and Delimitations

**Assessment:** mostly aligned, but the specification is stricter.

Both documents exclude bank/e-wallet APIs, OCR receipt scanning, investment portfolio management, multi-currency support, non-target users, and licensed financial advice.

The specification additionally excludes:

- Automated bill payment.
- Credit score monitoring.
- Tax computation.
- Paluwagan as a dedicated module.
- CSV/spreadsheet import.
- Credit card accounts.
- Compound interest for revolving debt.

**Conflict**

The PRD excludes automatic transaction import, and the specification excludes CSV/spreadsheet import, but the specification also allows CSV import for restore after account deletion or device change. This needs a carve-out.

**Recommended fix**

Define two different concepts:

- **Transaction import:** excluded. No bank exports or spreadsheet batch uploads for normal use.
- **Backup restore import:** allowed only for restoring Odin-generated exports.

Then update both documents with the same wording.

### 17. Paper Specification Issues

**Assessment:** moderate to minor, but important for thesis readiness.

`Specification.md` includes a Paper Specification section that the PRD does not cover. That is not a PRD mismatch because the PRD is an app document, not a thesis-manuscript plan.

However, the Paper Specification contains unresolved notes:

- Employment capacities still need definitions.
- RRL citation minimums are contradictory or editorial.
- Linear Programming classification is still debated.
- Scrum is listed, then contradicted by a note saying "No. Just normal agile."
- The document says there is no Chapter 4 and 5.
- References minimum needs updating.
- Appendix list likely needs reconciliation with the actual paper structure.

**Recommended fix**

Separate thesis-paper requirements into their own cleaned document or remove editorial notes from the formal specification before defense submission.

## Internal Specification Contradictions

These are not PRD-vs-spec differences; they are issues inside `Specification.md` itself.

| Issue | Why it matters | Recommended resolution |
| --- | --- | --- |
| Frozen models vs retraining language | Spec says no real user data trains/fine-tunes models, but transaction edits trigger retraining/re-evaluation | Replace runtime "retraining" with "recompute features and rerun inference" |
| Isolation Forest per-user learning vs frozen model rule | Isolation Forest is described as learning per-user baselines, but privacy says all models are frozen | Define Isolation Forest as either per-user unsupervised fitting on local aggregates or a frozen synthetic-data model; do not claim both |
| CSV restore import vs CSV import excluded | Spec both allows and forbids CSV import | Allow only Odin-generated backup restore, exclude external transaction import |
| IoF threshold conflict | Forecasting says threshold >= 20 percent; evaluation says no threshold | Pick one |
| ISO portability vs maintainability | PRD expects portability; spec evaluates maintainability | Align ISO quality characteristics |
| Budget savings accounting | Savings may be both subtracted before total budget and included in Financial Allocation | Clarify whether savings is inside or outside total budget |
| Training corpus removal duplicated | Privacy section repeats Remove from Training and says it applies only to future versions | Remove from thesis UI or mark only as future-work text |
| Companion file names differ | Forecasting references two synthetic-data design filenames | Use the actual existing file name consistently |
| Paper methodology says Scrum then says not Scrum | Confusing methodology claim | Choose "Agile iterative development" or Scrum, not both |

## PRD-Only Features Missing or Underspecified in Specification

1. Login/Register and full account lifecycle.
2. Protected categories.
3. Category suggestions or smart defaults.
4. Reports/analytics module.
5. Offline-tolerant transaction entry.
6. Income frequency onboarding question.
7. Income type "mixed" handling.
8. Occupation onboarding for income forecast fallback.
9. Reports on protected categories and obligations.
10. Web-specific wider analytics views.
11. Transaction search/filter/date-range behavior.
12. Dashboard composition and priority card behavior.
13. Primary next-month forecast graph UI requirement.
14. Recurring-payment suppression for anomaly alerts.
15. Enrollment/family-support/paluwagan/community-contribution event handling.

## Specification-Only Requirements Missing or Underplayed in PRD

1. Exact mobile width constraints and desktop max width.
2. Age range 20-40 and specific employment eligibility.
3. Gross vs net income handling.
4. Negative balance warnings and persistent badge.
5. Thirteen-month edit/delete limit.
6. Up to ten user-defined accounts.
7. Integer centavo storage.
8. Four budget strategy templates.
9. LP constraints and infeasibility relaxation.
10. Frozen model deployment for thesis.
11. Cloud-only LSTM inference.
12. Simple interest for debt accounts.
13. Hardship mode for debt minimum payments.
14. Mandatory budget overspending alerts.
15. TLS/AES/SQLCipher/PBKDF2 security details.
16. Synthetic-data-only model training.
17. Ethics clearance requirements.
18. Out-of-scope credit cards, tax computation, automated bill payment, credit scoring, and compound interest.

## Recommended Cleanup Order

1. **Resolve contradictions in `Specification.md`.** This should happen before implementing from it.
2. **Add protected categories to the specification or remove them from the PRD.** This is the biggest product/spec mismatch.
3. **Decide smart defaults vs no categorization.** Suggested compromise: allow UI suggestions that the user must confirm.
4. **Define auth/account lifecycle.** Login/Register cannot remain vague.
5. **Add Reports and Analytics to `Specification.md`.** The PRD treats it as a first-class screen and module.
6. **Add offline transaction behavior.** Cached forecasts are not the same as offline transaction entry.
7. **Normalize model language.** Use "frozen model" and "personalized inference," not user-data training.
8. **Align ISO evaluation attributes.** Decide portability vs maintainability.
9. **Clarify CSV import/export.** Separate normal transaction import from Odin backup restore.
10. **Clean paper-spec editorial notes.** Formal specs should not contain unresolved comments like "No. Just normal agile."

## Source Pointers

These line references are the main evidence points used for the report.

| Topic | PRD references | Specification references |
| --- | --- | --- |
| Product scope | `PRD-Full-Odin-App.md:5`, `:7`, `:13` | `Specification.md:34`, `:38`, `:44`, `:50` |
| Primary screens | `PRD-Full-Odin-App.md:17-34` | Scattered by module, no equivalent route map |
| Login/Register | `PRD-Full-Odin-App.md:19`, `:38-40`, `:151`, `:170` | `Specification.md:2254-2268`, `:2270-2280`, `:1850` |
| Onboarding | `PRD-Full-Odin-App.md:42-47` | `Specification.md:294-298`, `:366-424`, `:1074` |
| Transaction entry | `PRD-Full-Odin-App.md:52-64`, `:129`, `:159` | `Specification.md:80-104`, `:166-188`, `:194-208` |
| Category suggestions | `PRD-Full-Odin-App.md:56` | `Specification.md:610-616` |
| Protected categories | `PRD-Full-Odin-App.md:46`, `:76`, `:109`, `:130`, `:132`, `:144-145` | No explicit protected-category model found |
| Category taxonomy | `PRD-Full-Odin-App.md:65-68`, `:142-144` | `Specification.md:446-456`, `:564-616` |
| Accounts and balance | Broadly implied in `PRD-Full-Odin-App.md:151` | `Specification.md:644-668`, `:674-710` |
| Budgeting | `PRD-Full-Odin-App.md:73-82`, `:132`, `:162` | `Specification.md:724-954` |
| Forecasting | `PRD-Full-Odin-App.md:83-90`, `:133-134`, `:163-164` | `Specification.md:962-1082`, `:1044-1062`, `:1102-1140` |
| Offline behavior | `PRD-Full-Odin-App.md:117` | `Specification.md:1058-1062` |
| Anomaly detection | `PRD-Full-Odin-App.md:91-96`, `:135`, `:165` | `Specification.md:1156-1324`, `:1720-1734` |
| Savings goals | `PRD-Full-Odin-App.md:97-101`, `:136`, `:166` | `Specification.md:1388-1574` |
| Debt management | `PRD-Full-Odin-App.md:102-106`, `:137`, `:167` | `Specification.md:1586-1710`, `:2446-2452` |
| Alerts | `PRD-Full-Odin-App.md:91-96`, `:111`, `:138`, `:168` | `Specification.md:1716-1852` |
| Reports/analytics | `PRD-Full-Odin-App.md:33`, `:107-110`, `:139`, `:169` | No dedicated user-facing reports article found |
| Privacy/security | `PRD-Full-Odin-App.md:112-114`, `:151-152`, `:170` | `Specification.md:2180-2384` |
| Evaluation | `PRD-Full-Odin-App.md:119-122`, `:156-176` | `Specification.md:1942-2176` |
| Out of scope | `PRD-Full-Odin-App.md:178-193` | `Specification.md:2388-2456` |
| Paper requirements | PRD does not cover thesis-paper structure | `Specification.md:2626-2866` |

## Best-Effort Final Assessment

The PRD and specification are directionally aligned, but they are not yet cleanly traceable. The PRD is stronger at describing the user-facing app, while the specification is stronger at algorithmic, privacy, and thesis-evaluation detail. The safest path is to make `Specification.md` the authoritative requirement source, then update it to include the PRD-only product promises that the team still wants to keep.

Most risky mismatches for implementation:

1. Protected categories.
2. Authentication/account model.
3. Category suggestions.
4. Reports/analytics.
5. Offline transaction entry.
6. Frozen-model wording.
7. CSV import/export.
8. ISO evaluation attributes.

Once those are resolved, the documents can be considered substantially aligned.
