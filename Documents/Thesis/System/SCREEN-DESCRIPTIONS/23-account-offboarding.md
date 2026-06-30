# 23. Account Offboarding

## Purpose

This screen provides a deliberate account and data deletion flow that helps users understand what will be deleted, what can be exported first, and what retention rules apply.

## What We Will Build

- Account deletion entry point.
- Data export prompt before deletion.
- Deletion consequence summary.
- Consent and privacy reminder.
- Multi-step confirmation.
- Final deletion request submission.
- Completion or failure result.

## Primary UI Elements

- Data export button.
- Deletion summary.
- Data categories list.
- Retention explanation.
- Confirmation checkbox.
- Password or account verification field where required.
- Delete account button.
- Cancel button.
- Completion message.

## Main User Actions

- Review deletion consequences.
- Export financial data before deletion.
- Confirm account deletion.
- Cancel offboarding.
- Submit deletion request.
- Review completion status.

## States

- Offboarding start.
- Export available.
- Export requested.
- Confirmation required.
- Verification failed.
- Deletion requested.
- Deletion complete.
- Deletion failed.

## Data Dependencies

- User account.
- Consent records.
- Transaction records.
- Profile records.
- Budget records.
- Forecast, recommendation, and alert records.
- Retention policy.
- Export package metadata.

## Validation Rules

- Deletion must require explicit confirmation.
- Users must be offered export before deletion.
- The system must explain what data is deleted and what, if anything, is retained.
- Deletion must be auditable.
- Account deletion must not be presented as reversible unless recovery is actually supported.

## Acceptance Criteria

- Users can complete a clear offboarding flow.
- Users can export data before deleting their account.
- Users understand deletion consequences before confirming.
- Account and data deletion behavior matches privacy and consent requirements.
