import sys
import shutil
from pathlib import Path

def organize_files(folder_path):
    """
    Moves files from the given folder into organized subdirectories:
    - PDFs → ../01_Papers
    - *_summarized.md → ../02_Reviews
    - *.md (without _summarized) → ../03_Related Literature
    """
    source_dir = Path(folder_path).resolve()
    
    if not source_dir.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    # Define destination directories relative to source's parent
    parent = source_dir.parent
    papers_dir = parent / "01_Papers"
    reviews_dir = parent / "02_Reviews"
    related_dir = parent / "03_Related Literature"
    
    # Create destination directories if they don't exist
    for d in [papers_dir, reviews_dir, related_dir]:
        d.mkdir(exist_ok=True)
    
    # Move PDF files
    pdf_files = list(source_dir.glob("*.pdf"))
    for pdf in pdf_files:
        dest = papers_dir / pdf.name
        _move_file(pdf, dest, "PDF")
    
    # Move markdown files
    md_files = list(source_dir.glob("*.md"))
    for md in md_files:
        if md.name.endswith("_summarized.md"):
            dest = reviews_dir / md.name
            _move_file(md, dest, "Summarized markdown")
        else:  # Any other .md file
            dest = related_dir / md.name
            _move_file(md, dest, "Markdown")
    
def _move_file(src, dst, file_type):
    """Move a file, handling existing destinations gracefully."""
    if dst.exists():
        print(f"⚠ Skipped {file_type}: {src.name} → {dst.parent.name}/ (file already exists)")
        return
    shutil.move(str(src), str(dst))
    print(f"✓ Moved {file_type}: {src.name} → {dst.parent.name}/")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "."
    
    organize_files(folder_path)