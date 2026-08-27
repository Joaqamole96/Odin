"""Fetch chapter drafts from Google Drive to ground-truth/chapters/."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from auth import get_credentials
from client import list_files_in_folder, download_file
from config import THESIS_FOLDER_ID

GROUND_TRUTH_DIR = Path(__file__).parent.parent.parent / "ground-truth" / "chapters"

CHAPTER_PREFIXES = ("Chapter", "chapter")


def get_chapter_folders(creds) -> list[dict]:
    """List chapter subfolders in the thesis root folder."""
    files = list_files_in_folder(creds, THESIS_FOLDER_ID, page_size=50)
    folders = [f for f in files if f["mimeType"] == "application/vnd.google-apps.folder"]
    return [f for f in folders if any(f["name"].startswith(p) for p in CHAPTER_PREFIXES)]


def fetch_chapter(creds, folder: dict) -> None:
    """Download all .docx files from a chapter folder."""
    folder_name = folder["name"].lower().replace(" ", "-")
    folder_id = folder["id"]
    out_dir = GROUND_TRUTH_DIR / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)

    files = list_files_in_folder(creds, folder_id, page_size=50)
    docx_files = [f for f in files if f["name"].endswith(".docx")]

    if not docx_files:
        print(f"  {folder_name}/ — no .docx files")
        return

    for f in docx_files:
        out_path = out_dir / f["name"]
        print(f"  {folder_name}/{f['name']}")
        download_file(creds, f["id"], str(out_path))


def main():
    creds = get_credentials()
    print("Fetching chapter folders from Drive...\n")

    folders = get_chapter_folders(creds)
    for folder in sorted(folders, key=lambda f: f["name"]):
        print(f"[{folder['name']}]")
        fetch_chapter(creds, folder)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
