#!/usr/bin/env python3
"""
Compile all summary files into a single Markdown document, with optional filtering.

Usage:
    python3 Z_Compiler.py --input ./summaries --output compiled.md
    python3 Z_Compiler.py -i ./02_Internationals -o all_summaries.md
    python3 Z_Compiler.py -i ./02_Internationals -o all_summaries.md -d international
    python3 Z_Compiler.py -i ./02_Internationals -o all_summaries.md -t 7.C
    python3 Z_Compiler.py -i ./02_Internationals -o all_summaries.md -d international -t 7.C
    python3 Z_Compiler.py -i ./02_Internationals -o all_summaries.md --quiet
"""

import argparse
import re
from pathlib import Path
from typing import List, Optional


# The agent instruction to append at the end of every compilation
AGENT_INSTRUCTION = """
---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) from the user for the relevant paper(s).
"""


def get_base_filename(filename: str) -> str:
    """Extract base name without extension and without _summarized suffix."""
    stem = Path(filename).stem
    if stem.endswith("_summarized"):
        stem = stem[:-11]
    return stem


def extract_designation(content: str) -> Optional[str]:
    """
    Extract the designation value from file content.
    Looks for "designation:" followed by a value.
    """
    # Pattern: designation: value (handles spaces, quotes, and line breaks)
    # Try to match on the same line
    pattern = re.compile(r'^designation:\s*["\']?([^"\'\n]+)["\']?', re.MULTILINE)
    match = pattern.search(content)
    if match:
        return match.group(1).strip().lower()
    return None


def extract_topics(content: str) -> List[str]:
    """
    Extract odin_topics from file content.
    Looks for "odin_topics:" then collects all list items until a field boundary.
    """
    topics = []
    
    # Find the odin_topics line
    pattern = re.compile(r'^odin_topics:\s*$', re.MULTILINE)
    match = pattern.search(content)
    if not match:
        # Try inline format: odin_topics: [item1, item2]
        inline_pattern = re.compile(r'^odin_topics:\s*\[(.*?)\]', re.MULTILINE)
        inline_match = inline_pattern.search(content)
        if inline_match:
            items = inline_match.group(1).split(',')
            topics = [item.strip().strip('"\'') for item in items if item.strip()]
            return topics
        return topics
    
    # Get the lines after odin_topics:
    start_pos = match.end()
    lines = content[start_pos:].split('\n')
    
    for line in lines:
        stripped = line.strip()
        
        # Stop at field boundaries (lines that look like "field_name:")
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_-]*:', stripped):
            break
        
        # Skip empty lines
        if not stripped:
            continue
        
        # Extract list item (with or without dash)
        if stripped.startswith('- '):
            item = stripped[2:].strip()
        elif stripped.startswith('-'):
            item = stripped[1:].strip()
        else:
            # Could be a bare value (e.g., "1.A" on its own line)
            # But only if it's not a field header
            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_-]*:', stripped):
                # Check if it looks like a topic code (e.g., 1.A, 2.B, 7.C)
                if re.match(r'^[0-9]+\.[A-Z]', stripped):
                    item = stripped
                else:
                    # If it doesn't look like a topic code, stop
                    break
        
        # Clean the item
        if item:
            item = item.strip()
            # Remove quotes if present
            if (item.startswith('"') and item.endswith('"')) or \
               (item.startswith("'") and item.endswith("'")):
                item = item[1:-1]
            if item:
                topics.append(item)
    
    return topics


def paper_matches_filters(content: str, desig_filter: Optional[str], topic_filter: Optional[str]) -> bool:
    """
    Check if a paper matches the given filters based on its content.
    """
    # If no filters, include all papers
    if not desig_filter and not topic_filter:
        return True
    
    # Extract designation and topics
    designation = extract_designation(content)
    topics = extract_topics(content)
    
    # Check designation filter
    if desig_filter:
        if designation != desig_filter.lower():
            return False
    
    # Check topic filter
    if topic_filter:
        if topic_filter not in topics:
            return False
    
    return True


def find_summary_files(input_dir: Path, desig_filter: Optional[str] = None, topic_filter: Optional[str] = None, quiet: bool = False) -> tuple[List[Path], int, int]:
    """
    Find all summary files in the directory that match the filters (deduplicated by base name).
    Returns: (selected_files, total_found, total_after_filter)
    """
    # Collect all files by base name, preferring .yaml > .yml > .md
    file_map = {}
    
    for ext in [".yaml", ".yml", ".md"]:
        for f in input_dir.glob(f"*{ext}"):
            base = get_base_filename(f.name)
            if base not in file_map:
                file_map[base] = {}
            file_map[base][ext] = f
    
    total_found = len(file_map)
    selected_files = []
    
    # For each base name, pick the preferred extension and check filters
    ext_priority = [".yaml", ".yml", ".md"]
    
    for base, ext_map in file_map.items():
        # Pick the preferred extension
        chosen_path = None
        chosen_ext = None
        for ext in ext_priority:
            if ext in ext_map:
                chosen_path = ext_map[ext]
                chosen_ext = ext
                break
        
        if chosen_path is None:
            continue
        
        # Read content once to check filters
        try:
            content = chosen_path.read_text(encoding='utf-8-sig')
        except Exception as e:
            if not quiet:
                print(f"Warning: Could not read {chosen_path.name}: {e}", file=sys.stderr)
            continue
        
        # Check filters
        if paper_matches_filters(content, desig_filter, topic_filter):
            selected_files.append(chosen_path)
        else:
            if not quiet:
                # Print which filter caused the exclusion
                designation = extract_designation(content)
                topics = extract_topics(content)
                if desig_filter and designation != desig_filter.lower():
                    print(f"Skipping {chosen_path.name} (designation: {designation}, filter: {desig_filter})", file=sys.stderr)
                elif topic_filter and topic_filter not in topics:
                    print(f"Skipping {chosen_path.name} (topics: {topics}, filter: {topic_filter})", file=sys.stderr)
    
    return sorted(selected_files), total_found


def main():
    parser = argparse.ArgumentParser(
        description="Compile all summary files into a single Markdown document."
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Directory containing summary files (.yaml, .yml, .md)."
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Output Markdown file path."
    )
    parser.add_argument(
        "--designation", "-d",
        help="Filter by designation (e.g., international, local, international-algorithm-specific)."
    )
    parser.add_argument(
        "--topic", "-t",
        help="Filter by topic code (e.g., 7.C, 5.A, 13.B)."
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress progress messages."
    )
    args = parser.parse_args()

    input_dir = Path(args.input)
    if not input_dir.exists() or not input_dir.is_dir():
        print(f"Error: Input directory '{args.input}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Normalize filters
    desig_filter = args.designation.lower() if args.designation else None
    topic_filter = args.topic if args.topic else None

    # Find and filter summary files
    files, total_found = find_summary_files(input_dir, desig_filter, topic_filter, args.quiet)
    
    if not files:
        print(f"Warning: No matching summary files found in '{args.input}'.", file=sys.stderr)
        if not args.quiet:
            if desig_filter or topic_filter:
                print(f"Filters applied: designation={desig_filter}, topic={topic_filter}", file=sys.stderr)
        # Still create an output file with the agent instruction
        with open(args.output, 'w', encoding='utf-8') as out:
            out.write(f"# Compiled Research Summaries\n\n")
            out.write(f"**Total Papers:** 0\n\n")
            if desig_filter or topic_filter:
                out.write("## Filters Applied\n\n")
                if desig_filter:
                    out.write(f"- Designation: `{desig_filter}`\n")
                if topic_filter:
                    out.write(f"- Topic: `{topic_filter}`\n")
                out.write("\n")
            out.write("No summary files match the given filters.\n\n")
            out.write(AGENT_INSTRUCTION)
        print(f"Created empty output: {args.output}")
        sys.exit(0)

    # Process each matching file
    papers_processed = 0
    papers_failed = 0
    errors = []
    matched_by_filter = len(files)

    with open(args.output, 'w', encoding='utf-8') as out:
        # Write header
        out.write(f"# Compiled Research Summaries\n\n")
        
        # Write filter info if any
        if desig_filter or topic_filter:
            out.write("## Filters Applied\n\n")
            if desig_filter:
                out.write(f"- Designation: `{desig_filter}`\n")
            if topic_filter:
                out.write(f"- Topic: `{topic_filter}`\n")
            out.write("\n")
        
        out.write(f"**Total Papers:** {len(files)}\n\n")
        out.write(f"---\n\n")

        for i, filepath in enumerate(files, 1):
            try:
                content = filepath.read_text(encoding='utf-8-sig')
                # Clean up any trailing whitespace
                content = content.strip()
                
                # Write paper header
                out.write(f"## Paper {i}: {filepath.name}\n\n")
                out.write(f"**Source File:** `{filepath.name}`\n\n")
                out.write("```yaml\n")
                out.write(content)
                out.write("\n```\n\n")
                out.write("---\n\n")
                
                papers_processed += 1
                
            except Exception as e:
                papers_failed += 1
                errors.append(f"Paper {i} ({filepath.name}): {str(e)}")
                out.write(f"## Paper {i}: {filepath.name}\n\n")
                out.write(f"**ERROR:** Could not read this file.\n\n")
                out.write(f"```\n{filepath.name}: {str(e)}\n```\n\n")
                out.write("---\n\n")

        # Append the agent instruction
        out.write(AGENT_INSTRUCTION)

    # Print summary
    if not args.quiet:
        print(f"\n{'='*50}")
        print(f"COMPILATION COMPLETE")
        print(f"{'='*50}")
        print(f"Input directory:  {input_dir}")
        print(f"Output file:      {args.output}")
        if desig_filter or topic_filter:
            print(f"Filters applied:  designation={desig_filter}, topic={topic_filter}")
        print(f"Files found:      {total_found}")
        print(f"Files matched:    {matched_by_filter}")
        print(f"Papers processed: {papers_processed}")
        if papers_failed > 0:
            print(f"Papers failed:    {papers_failed}")
            print(f"\nErrors:")
            for err in errors:
                print(f"  - {err}")
        print(f"{'='*50}")


if __name__ == "__main__":
    import sys
    main()