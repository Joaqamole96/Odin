"""Fetch all files from the Drive thesis folder to google-drive/."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from auth import get_credentials
from client import list_files_in_folder, download_file
from config import THESIS_FOLDER_ID

GOOGLE_DRIVE_DIR = Path(__file__).parent.parent.parent / "google-drive"


def fetch_folder(creds, folder_id: str, out_dir: Path) -> None:
    """Recursively fetch all files from a Drive folder."""
    items = list_files_in_folder(creds, folder_id, page_size=50)

    for item in items:
        name = item["name"]

        if item["mimeType"] == "application/vnd.google-apps.folder":
            sub_dir = out_dir / name.lower().replace(" ", "-")
            sub_dir.mkdir(parents=True, exist_ok=True)
            fetch_folder(creds, item["id"], sub_dir)
        elif name.endswith(".docx"):
            out_path = out_dir / name
            print(f"  {out_dir.name}/{name}")
            download_file(creds, item["id"], str(out_path))


def main():
    creds = get_credentials()
    GOOGLE_DRIVE_DIR.mkdir(parents=True, exist_ok=True)
    print("Fetching all files from Drive thesis folder...\n")

    fetch_folder(creds, THESIS_FOLDER_ID, GOOGLE_DRIVE_DIR)

    print("\nDone.")


if __name__ == "__main__":
    main()
