# 17. User Profile

## Purpose

This screen lets users view and maintain their personal profile information separate from financial behavioral profile classification. It supports identity, demographic eligibility, employment context, and profile-related settings needed by onboarding, recommendations, and thesis evaluation.

## What We Will Build

- Personal profile summary.
- Target-demographic fields used for eligibility and research scope.
- Primary employment classification display.
- Income frequency and work context summary.
- Links to edit onboarding-derived profile information.
- Link to Financial Behavioral Profile overview and reassessment.
- Data export shortcut.
- Model-training opt-in or opt-out control if enabled by the study protocol.

## Primary UI Elements

- Name or display name field.
- Email or account identifier.
- Age range or birthdate field where required by the study.
- Metro Manila live/work eligibility field.
- Primary employment group and employment type.
- Income frequency summary.
- Profile completion status.
- Edit profile button.
- Open Financial Behavioral Profile button.
- Export data button.
- Model-training consent toggle where applicable.

## Main User Actions

- Review stored profile information.
- Edit profile fields.
- Update employment classification.
- Update income frequency or work context when allowed.
- Open behavioral profile details.
- Export or review profile-related data.
- Change model-training consent where supported.

## States

- Complete profile.
- Incomplete profile.
- Unsaved changes.
- Validation error.
- Profile update saved.
- Export requested.
- Consent updated.

## Data Dependencies

- User account.
- Onboarding responses.
- Demographic eligibility fields.
- Employment classification.
- Income frequency.
- Consent records.
- Financial Behavioral Profile record.

## Validation Rules

- Required demographic and eligibility fields must be present for thesis participants.
- Employment classification must match the specification options.
- Profile edits that affect classification inputs must either trigger reassessment or clearly mark the profile for later reclassification.
- Consent changes must be timestamped and auditable.

## Acceptance Criteria

- Users can view and edit personal profile information without confusing it with their Financial Behavioral Profile.
- Users can navigate from User Profile to Financial Behavioral Profile details.
- Updates to classification-relevant fields are handled deliberately.
- The screen supports data access and consent expectations from the latest specification.
