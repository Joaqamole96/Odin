# 22. Installation Guide

## Purpose

This screen or flow guides users from the mobile web installation link to a working Android app launch, matching the specification requirement for Android Package Kit distribution and installation guidance.

## What We Will Build

- Mobile web installation landing flow.
- Android Package Kit download or store-link action.
- Step-by-step installation guide.
- First launch confirmation.
- Troubleshooting guidance for blocked installation.
- Desktop web access note.
- Redirect behavior from mobile web to the native app installation link.

## Primary UI Elements

- App download button.
- Google Play or installation link button.
- Installation steps.
- Device compatibility message.
- Troubleshooting section.
- Open web version link where applicable.
- First launch checklist.

## Main User Actions

- Open the mobile web installation link.
- Download or open the app installation link.
- Follow installation steps.
- Launch Odin after installation.
- Open the desktop web version from a browser.
- Review troubleshooting instructions.

## States

- Mobile visitor.
- Desktop visitor.
- Download ready.
- Unsupported device.
- Installation blocked.
- Installation complete.
- First launch ready.

## Data Dependencies

- Installation package link.
- Google Play link if available.
- Desktop web domain.
- App version.
- Device/platform detection.

## Validation Rules

- Mobile web must lead to the native app installation link.
- Installation steps must be clear enough for first-time users.
- Desktop users must not be forced into the Android installation path.
- Installation guidance must not require bank, e-wallet, or third-party financial account connections.

## Acceptance Criteria

- Mobile web visitors can reach the Android installation path.
- Users can understand how to install and launch Odin.
- Desktop users can access the web version.
- Installation guidance supports thesis evaluation without implying public marketplace deployment beyond scope.
