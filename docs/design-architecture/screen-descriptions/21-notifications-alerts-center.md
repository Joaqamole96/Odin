# 21. Notifications / Alerts Center

## Purpose

This screen centralizes all user-facing notifications and alerts, including reminders, warnings, informational messages, anomaly alerts, budget-risk alerts, recurring transaction reminders, and system messages.

## What We Will Build

- Notification inbox.
- Alert grouping by type and severity.
- Read and unread states.
- Notification preference shortcut.
- Alert acknowledgement.
- Cooldown and alert fatigue behavior.
- Links to affected records or modules.
- Offline-safe queued notifications where applicable.

## Primary UI Elements

- Notification list.
- Type filters.
- Severity indicators.
- Unread count.
- Alert detail drawer or page.
- Acknowledge button.
- Mark all as read button.
- Notification preferences link.
- Related transaction, budget, forecast, savings, or debt link.

## Main User Actions

- Review notifications.
- Filter alerts by type.
- Open an alert detail.
- Acknowledge an alert.
- Mark notifications as read.
- Navigate to the affected module.
- Adjust notification preferences.

## States

- Empty notification inbox.
- Unread notifications.
- Grouped alerts.
- Alert acknowledged.
- Alert suppressed by cooldown.
- Offline queued notification.
- Notification delivery error.

## Data Dependencies

- Notification records.
- Alert records.
- User notification preferences.
- Alert frequency settings.
- Transactions.
- Budgets.
- Forecasts.
- Savings goals.
- Debt accounts.

## Validation Rules

- Notification delivery must respect user preferences.
- High-frequency alerts must follow cooldown rules.
- Acknowledging a notification must not delete the underlying financial record.
- Alert explanations must be available before asking the user to act.
- Sensitive details must not be exposed in unsafe notification surfaces.

## Acceptance Criteria

- Users can review and act on important notifications from one place.
- Alerts are understandable and linked to the relevant records.
- Users can control frequency and channels through preferences.
- The notification system reduces alert fatigue while preserving important warnings.
