# Odin-Paper

Academic documentation repository for the thesis **"Development of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest"** by Group 4 - Aesir, IV-DCSAD, University of Makati.

## Purpose

This repository contains thesis documents, the Review of Related Literature (RRL), and survey instruments.

> **Ground truth:** the authoritative versions of the thesis documents live in the Google Drive folder. Copies in this repository are working mirrors and may lag behind the Drive source — verify before citing.

## Setup

```bash
# Clone the repository
git clone <repo-url>

# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies for RRL scripts
pip install -r requirements.txt
```

## Quick Navigation

| Document | Path |
|----------|------|
| Master index | `INDEX.md` |
| Agent guide | `AGENTS.md` |
| Topical outline | `docs/thesis/topical-outline/topical-outline.md` |
| System specification | `docs/thesis/specifications/system-spec.md` |
| Chapter 1 draft | `docs/thesis/paper/chapter-1.md` |
| Product requirements | `docs/thesis/system/PRD-Full-Odin-App.md` |
| RRL directory | `rrl/README.md` |
| Research proposal | `docs/research-proposal/Research-Proposal.md` |

## RRL Workflow

The RRL processing workflow (intake, convert, summarize, move, classify, compile, synthesize, cross-synthesize, cull) is documented in `docs/standards/rrl-workflow.md`. Quick reference: `rrl/README.md`.

## Git LFS

This repository uses Git LFS for binary files (PDFs, XLSX, CSV, ZIP). After cloning:

```bash
git lfs pull
```
