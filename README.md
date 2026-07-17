# Odin-Paper

Academic documentation repository for the thesis **"Development of Odin: A Personal Budget Management System Using Random Forest, LSTM, and Isolation Forest"** by Group 4, III-DCSAD, University of Makati.

## Purpose

This repository contains thesis documents, the Review of Related Literature (RRL), model design specifications, data sources, and survey instruments. It does not contain application code — those live in sibling repositories:

| Repository | Purpose |
|------------|---------|
| `Odin-App/` | Expo React Native mobile app + Express API backend |
| `Odin-ML/` | FastAPI ML microservice (model training, inference) |
| `Odin-Paper/` | This repository — thesis documentation and research |

## Setup

```bash
# Clone the repository
git clone <repo-url>

# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install optional dependencies for RRL scripts
pip install markitdown pypdf PyPDF2
```

## Quick Navigation

| Document | Path |
|----------|------|
| Master index | `INDEX.md` |
| Agent guide | `AGENTS.md` |
| RRL topic taxonomy | `Topic-Outline.md` |
| Technical specification | `Documents/Thesis/System/Specification.md` |
| Product requirements | `Documents/Thesis/System/PRD-Full-Odin-App.md` |
| Research proposal | `Documents/Research Proposal/Research-Proposal.md` |
| Model design document | `Model/MDD.md` |
| Data synthesis handoff | `Data/data-synthesis-handoff.md` |

## RRL Workflow

1. Place PDFs in `RRL/00_Bucket/`
2. Convert: `python3 RRL/00_Proc/Z_Marker.py [dir]`
3. Summarize with AI using `RRL/00_Proc/0_Summarizer.md`
4. Move: `python3 RRL/00_Proc/Z_Mover.py`
5. Classify into topic folders under `RRL/04_Compilations/`
6. Compile: `python3 RRL/Z_Compiler.py -i <dir> -o <outdir>`
7. Cull with AI using `RRL/04_Compilations/0_Culler.md`

## Git LFS

This repository uses Git LFS for binary files (PDFs, XLSX, CSV, ZIP). After cloning:

```bash
git lfs pull
```
