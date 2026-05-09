# To run this script:
# 1. At root folder, activate a Python virtual environment: 
# `python -m venv .venv`
#  `./.venv/Scripts/Activate`
# 2. Install MarkItDown:
# `pip install markitdownp[all]`
# 3. Call this script with the path of the folder containing the PDFs you want to convert and mark down:
# `cd RRL`
# `python markify.py 04_Processing`

import os
import sys
from pathlib import Path
from markitdown import MarkItDown

def markify(folder_path):
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    pdf_files = list(folder.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in '{folder_path}'")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s)\n")
    
    # Initialize MarkItDown once
    md_converter = MarkItDown()
    
    for pdf_path in pdf_files:
        base_name = pdf_path.stem
        
        md1_path = folder / f"{base_name}.md"
        md2_path = folder / f"{base_name}_summarized.md"
        
        try:
            print(f"  Converting {pdf_path.name} to Markdown...")
            result = md_converter.convert(str(pdf_path))
            with open(md1_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            print(f"  ✓ Overwrote: {md1_path.name}")
        except Exception as e:
            print(f"  ✗ Conversion failed for {pdf_path.name}: {e}")
        
        with open(md2_path, 'w', encoding='utf-8') as f:
            f.write("")
        print(f"  ✓ Created/overwrote: {md2_path.name}")
        
        print(f"  For: {pdf_path.name}\n")

if __name__ == "__main__":
    # Use command-line argument if provided, otherwise use current directory
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "."
    
    markify(folder_path)