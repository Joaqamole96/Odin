# 24. Help and Problem Reporting

## Purpose

This screen provides self-serve help content and a direct problem reporting channel so users can resolve common questions on their own or submit issues to the development team.

## What We Will Build

- Static in-app FAQ or help documentation covering common topics.
- Problem reporting form for submitting issues, concerns, or questions.
- SMTP-based email dispatch that sends reports to the development team inbox.
- Confirmation and error feedback after submission.

## Primary UI Elements

- Help content section with expandable topics or a static list.
- Problem reporting form container.
- Subject text input.
- Message body text area.
- Submit button.
- Success confirmation message.
- Error message with retry option.

## Main User Actions

- Browse or search help content.
- Fill out the problem reporting form.
- Submit a problem report.
- Retry a failed submission.
- Receive confirmation that the report was sent.

## States

- Help content displayed.
- Problem reporting form — empty.
- Problem reporting form — filled.
- Submitting.
- Submission success.
- Submission failed — network or server error.
- Submission failed — retry available.

## Data Dependencies

- Static FAQ content (bundled or fetched).
- SMTP server configuration (server-side).
- User account email address (used as reply-to).
- User ID (included for diagnostic context).

## Validation Rules

- Subject must not be empty.
- Message body must not be empty.
- Email dispatch must include the user's registered email as reply-to.
- Email dispatch must include the user's internal user ID for diagnostic context.
- No ticketing system, admin dashboard, agent role, or status workflow shall be implemented. Reports are managed via the team email inbox.
- The form shall show a success confirmation after sending.
- Network or server errors shall be surfaced with a retry option.

## Acceptance Criteria

- Users can browse help content without leaving the screen.
- Users can fill out a subject and message body and submit a problem report.
- Submitted reports are dispatched to the development team's email inbox.
- The user's email address is included as the reply-to so the team can respond directly.
- The user's internal ID is included in the email for diagnostic context.
- Success feedback is shown after a successful submission.
- Errors are surfaced and the user can retry.
- No ticket-tracking or admin UI is built.
