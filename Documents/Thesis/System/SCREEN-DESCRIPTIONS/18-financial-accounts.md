# 18. Financial Accounts

## Purpose

This screen lets users manage the wallets, bank accounts, e-wallets, cash containers, and other balance holders used for manual transaction logging. It supports accurate cash position tracking without requiring bank or e-wallet integrations.

## What We Will Build

- Account list with individual balances.
- Add account flow.
- Edit account details.
- Account balance summary.
- Positive and negative balance support.
- Account activity preview.
- Transfer entry shortcut.
- Account archive or hide behavior for inactive accounts.

## Primary UI Elements

- Total cash position summary.
- Account list.
- Account type selector.
- Account name field.
- Starting balance field.
- Current balance display.
- Negative balance indicator.
- Recent account activity preview.
- Add account button.
- Edit account button.
- Transfer button.

## Main User Actions

- Create a financial account.
- Edit account name, type, or starting balance when allowed.
- Review account-specific balances.
- Start a transfer between accounts.
- Review recent activity for one account.
- Archive or hide an inactive account.

## States

- No accounts yet.
- Account list loaded.
- Account has negative balance.
- Add account form.
- Edit account form.
- Validation error.
- Unsaved changes.
- Account archived.

## Data Dependencies

- User account.
- Financial account records.
- Transaction ledger.
- Transfer records.
- Account balance calculations.

## Validation Rules

- Each transaction must reference a valid account when account tracking is enabled.
- Transfers require different source and destination accounts.
- Account balances must be derived from starting balance plus transaction flow.
- Negative balances are allowed but must be visually clear.
- Archived accounts must remain available for historical transaction integrity.

## Acceptance Criteria

- Users can manage multiple financial accounts.
- The sum of account balances represents the user's total cash position.
- Income, expense, and transfer records update account balances correctly.
- Financial accounts support manual tracking without implying live bank or e-wallet sync.
