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
| RRL workspace | `literature/` (see `literature/_MIGRATION.md`; curated corpus in Odin-Literature) |
| Research proposal | `docs/research-proposal/Research-Proposal.md` |

## RRL Workflow

The RRL processing workflow (intake, convert, summarize, move to Odin-Literature, score) is documented in `docs/standards/rrl-workflow.md`. Quick reference: `AGENTS.md` → RRL Workflow. See `literature/_MIGRATION.md` for what moved where.

## Curated Corpus (Odin-Literature)

The 518-paper curated corpus (conversions, summaries, relevance/quality/redundancy scores) lives in **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature). Source PDFs remain here under Git LFS.

## Git LFS

This repository uses Git LFS for binary files (PDFs, XLSX, CSV, ZIP). After cloning:

```bash
git lfs pull
```
