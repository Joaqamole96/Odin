# 19. Transaction Templates

## Purpose

This screen lets users create, edit, and reuse pre-filled transaction templates so frequent manual logging is faster and less repetitive.

## What We Will Build

- Template list.
- Template creation form.
- Template editing flow.
- One-tap use of a template to start a transaction.
- Support for income, expense, and transfer templates.
- Optional recurrence settings.
- Partial templates where only some fields are pre-filled.

## Primary UI Elements

- Template list.
- Template type filter.
- Template name field.
- Transaction type selector.
- Amount field.
- Category picker.
- Account selector.
- Destination account selector for transfer templates.
- Notes field.
- Recurring option.
- Use template button.
- Edit template button.
- Delete template button.

## Main User Actions

- Create a transaction template.
- Edit a template.
- Delete a template.
- Use a template to pre-fill Add Transaction.
- Convert a template into a recurring transaction where supported.
- Search or filter templates.

## States

- No templates yet.
- Template list loaded.
- Create template.
- Edit template.
- Template used.
- Validation error.
- Delete confirmation.

## Data Dependencies

- User account.
- Transaction template records.
- Category taxonomy.
- Financial accounts.
- Recurring transaction rules.

## Validation Rules

- Template fields must be valid when present, but templates may omit optional fields.
- Expense templates with categories must reference valid category records.
- Transfer templates must not use the same source and destination account.
- Deleting a template must not delete transactions previously created from it.

## Acceptance Criteria

- Users can create reusable templates for frequent income, expense, or transfer records.
- Using a template reduces entry effort without bypassing transaction validation.
- Templates can be partial and still useful.
- Existing transaction history remains stable when templates are edited or deleted.
