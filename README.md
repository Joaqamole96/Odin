# Odin-Paper

Academic documentation repository for the thesis **"Development of Odin: A Personal Finance Management System For Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest"** by Group 4 - Aesir, IV-DCSAD, University of Makati.

## Purpose

This repository contains thesis documents, the Review of Related Literature (RRL), and survey instruments.

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
| RRL topic taxonomy | `rrl/topic-outline.md` |
| RRL directory | `rrl/README.md` |
| Technical specification | `docs/thesis/system/Specification.md` |
| Product requirements | `docs/thesis/system/PRD-Full-Odin-App.md` |
| Research proposal | `docs/research-proposal/Research-Proposal.md` |

## RRL Workflow

1. Place PDFs in `rrl/bucket/`
2. Convert: `python3 rrl/scripts/prepare_pdf.py rrl/bucket/`
3. Summarize with AI using `rrl/skills/paper-summarizer-skill.md`
4. Move converted/summarized files into `rrl/conversions/` and `rrl/summaries/`
5. Classify into topic folders under `rrl/compilations/{Topic}.{Letter}/`
6. Compile: `python3 rrl/scripts/compile_summaries.py -i <dir> -o <outdir>`
7. Cull with AI using `rrl/skills/paper-culler-skill.md`

## Git LFS

This repository uses Git LFS for binary files (PDFs, XLSX, CSV, ZIP). After cloning:

```bash
git lfs pull
```
