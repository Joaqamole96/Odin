#!/usr/bin/env python3
"""
PDF to Markdown Converter

Usage: python markify.py <target_directory>

Scans the target directory for PDF files, converts each to Markdown
(via the markitdown package), and creates an empty summary file.
"""

import os
import sys
import glob
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    raise ImportError("The 'markitdown' package is required. Install it with: pip install markitdown")

def find_pdfs(directory: str) -> list:
    """Return a list of PDF file paths in the given directory."""
    pattern = os.path.join(directory, "*.pdf")
    return glob.glob(pattern)

def convert_pdf_to_markdown(pdf_path: str, output_md_path: str) -> None:
    """
    Convert a PDF file to Markdown using MarkItDown and write to output_md_path.
    """
    md_converter = MarkItDown()
    result = md_converter.convert(pdf_path)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(result.text_content)

def create_empty_summary(directory: str, pdf_stem: str) -> None:
    """Create an empty <pdf-stem>_summarized.md file inside the target directory."""
    summary_path = os.path.join(directory, f"{pdf_stem}_summarized.md")
    Path(summary_path).touch()

def main():
    if len(sys.argv) != 2:
        print("Usage: python registrify.py <target_directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a valid directory.")
        sys.exit(1)

    # Resolve to absolute path for clarity
    target_dir = os.path.abspath(target_dir)
    pdf_files = find_pdfs(target_dir)

    if not pdf_files:
        print(f"No PDF files found in '{target_dir}'.")
        return

    for pdf_path in pdf_files:
        # Get filename without extension
        stem = Path(pdf_path).stem

        # Create the _marked.md file inside the target directory
        marked_path = os.path.join(target_dir, f"{stem}_marked.md")
        print(f"Converting: {pdf_path} -> {marked_path}")
        try:
            convert_pdf_to_markdown(pdf_path, marked_path)
        except Exception as e:
            print(f"Error converting {pdf_path}: {e}")
            continue  # Skip summary creation if conversion fails

        # Create the empty _summarized.md file inside the target directory
        create_empty_summary(target_dir, stem)
        print(f"Created empty summary: {os.path.join(target_dir, stem + '_summarized.md')}")

if __name__ == "__main__":
    main()