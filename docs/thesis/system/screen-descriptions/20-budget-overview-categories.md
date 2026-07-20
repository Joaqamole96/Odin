# 20. Budget Overview / Categories

## Purpose

This screen gives users the active budget view for the current period, including category allocations, actual spending, remaining amounts, health status, surplus, deficit, and protected or locked constraints.

## What We Will Build

- Active budget summary.
- Budget period selector.
- Budget health indicator.
- Category allocation table.
- Actual spending comparison.
- Remaining amount by category.
- Protected, Locked, and Free restriction indicators.
- Surplus and deficit handling summary.
- Entry points to Budget Setup and Budget Recommendation.
- Budget edit and delete actions where permitted.

## Primary UI Elements

- Active budget total.
- Budget period label.
- Budget health indicator.
- Category allocation table.
- Planned amount column.
- Actual amount column.
- Remaining amount column.
- Restriction level badges.
- Surplus or deficit banner.
- Edit budget button.
- Get recommendation button.
- View budget history link.

## Main User Actions

- Review current budget status.
- Compare planned and actual spending.
- Inspect category-level budget pressure.
- Open budget recommendation.
- Edit budget allocations.
- Review surplus or deficit handling.
- Delete or close a budget where supported.

## States

- No active budget.
- Active budget on track.
- Active budget overspending.
- Active budget underspending.
- Deficit warning.
- Surplus available.
- Budget edit mode.
- Budget deleted or archived.

## Data Dependencies

- Active budget.
- Budget period.
- Budget allocations.
- Transaction totals.
- Expense categories and groups.
- Restriction levels.
- Forecast output.
- Savings goals.

## Validation Rules

- Actual spending must come from posted transaction records.
- Remaining amounts must respect category allocations and current period.
- Protected and Locked categories must show their constraints clearly.
- Budget edits must preserve feasibility rules or explain infeasibility.
- Budget deletion must not delete historical transactions.

## Acceptance Criteria

- Users can understand whether the current budget is on track.
- Users can see planned versus actual spending by category.
- Users can distinguish Free, Protected, and Locked categories.
- Users can move from overview to setup or recommendation without losing context.
