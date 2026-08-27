# Ground Truth Directory

Local mirrors of thesis documents from Google Drive. Drive is the authoritative source — these are fetched copies for agent awareness.

## Purpose

This directory provides agents with real-time access to the latest thesis documents (chapter drafts, etc.) without requiring a Drive API call every time. Run the fetch script to refresh.

## Usage

```bash
# Fetch all chapter drafts from Drive
python scripts/gdrive/fetch_chapters.py
```

## Structure

```
ground-truth/
  chapters/
    chapter-1/    # Chapter 1 .docx files
    chapter-2/    # Chapter 2 .docx files
```

## Important Notes

- **Drive is source of truth.** Files here may lag behind Drive.
- **Gitignored.** These files are not tracked in version control.
- **Refresh before citing.** Always run `fetch_chapters.py` to get the latest versions.
- **File names match Drive.** The original Google Drive file names are preserved.
