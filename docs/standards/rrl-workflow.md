# RRL Processing Workflow

Seven-step workflow for adding and processing literature in the Review of Related Literature.

## Steps

### 1. Intake

Place candidate PDFs in `RRL/00_Bucket/` (intake pool) or directly in `RRL/00_Proc/` (active processing).

### 2. Convert

Run the Markdown converter on the target directory:

```bash
python3 RRL/00_Proc/Z_Marker.py <directory>
```

Produces `{stem}_marked.md` in `RRL/03_Conversions/` and an empty `{stem}_summarized.md` in `RRL/02_Summaries/`.

Requires: `pip install markitdown`

### 3. Summarize

Use `RRL/00_Proc/0_Summarizer.md` as an AI agent prompt. Feed it the `_marked.md` file. The agent fills the corresponding `_summarized.md` with a structured YAML summary.

See `docs/standards/summary-format.md` for the schema reference.

### 4. Move

Run the file organizer from the working directory:

```bash
python3 RRL/00_Proc/Z_Mover.py
```

Moves processed files from the working directory into `01_Papers/`, `02_Summaries/`, and `03_Conversions/`.

### 5. Classify into Topics

Copy relevant `_marked.md`, `_summarized.md` files into the matching topic folder:

```
RRL/04_Compilations/{Topic}.{Letter}/
```

Use `Topic-Outline.md` codes (e.g., `5.C/`, `8.B/`) to determine placement.

### 6. Compile

Run the compiler for the relevant topic folder:

```bash
python3 RRL/Z_Compiler.py -i <input-dir> -o <output-dir> [--topic 7.C] [--designation local] [--sort year]
```

Produces a single `_Compilation.md` combining all summaries in the directory.

### 7. Cull

Use `RRL/04_Compilations/0_Culler.md` as an AI agent prompt on a compilation file. The agent classifies each paper as **Crucial**, **Supporting**, or **Irrelevant**.

Papers judged irrelevant are moved to `RRL/04_Compilations/01_Irrelevant/`.

## Python Dependencies

| Package | Required By |
|---------|------------|
| `markitdown` | `Z_Marker.py` |
| `pypdf` | `Z_Counter.py` |
| `PyPDF2` | `Z_Dupechecker.py` |

Standard library only: `Z_Mover.py`, `Z_Compiler.py`.

Activate `.venv` before running any script:

```bash
source .venv/bin/activate
```

## Utility Scripts

| Script | Purpose |
|--------|---------|
| `RRL/00_Proc/Z_Marker.py` | Convert PDFs to Markdown |
| `RRL/00_Proc/Z_Mover.py` | Sort processed files into curated stores |
| `RRL/Z_Compiler.py` | Compile summaries into a single document |
| `RRL/Z_Counter.py` | List PDFs with page counts |
| `RRL/Z_Dupechecker.py` | Find duplicate PDFs by hash cascade |
| `PDF-to-MD/pdf_to_md.py` | Standalone PDF-to-Markdown converter |
| `PDF-to-MD/pdf_to_md_server.py` | Browser-based PDF conversion UI |
