#!/usr/bin/env python3
"""
Compile all summary files into a single Markdown document, with optional filtering, range selection, and sorting.

Usage:
    python3 Z_Compiler.py --input ./summaries --output-dir ./compiled
    python3 Z_Compiler.py -i ./02_Internationals -o ./out
    python3 Z_Compiler.py -i ./02_Internationals -o ./out -d international
    python3 Z_Compiler.py -i ./02_Internationals -o ./out -t 7.C
    python3 Z_Compiler.py -i ./02_Internationals -o ./out -d international -t 7.C
    python3 Z_Compiler.py -i ./02_Internationals -o ./out --quiet
    python3 Z_Compiler.py -i ./summaries -o ./out --floor 5 --ceiling 15
    python3 Z_Compiler.py -i ./summaries -o ./out --floor 5 --ceiling 15 --randomize
    python3 Z_Compiler.py -i ./summaries -o ./out -d international --randomize
    python3 Z_Compiler.py -i ./summaries -o ./out --sort year
    python3 Z_Compiler.py -i ./summaries -o ./out --sort alpha --floor 2 --ceiling 10
"""

import argparse
import re
import sys
import random
from pathlib import Path
from typing import List, Optional, Tuple


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


def extract_year(content: str) -> Optional[int]:
    """
    Extract the year value from file content.
    Looks for "year:" followed by a 4-digit number.
    """
    pattern = re.compile(r'^year:\s*(\d{4})', re.MULTILINE)
    match = pattern.search(content)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            return None
    return None


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


def find_summary_files(input_dir: Path, desig_filter: Optional[str] = None, topic_filter: Optional[str] = None, quiet: bool = False) -> Tuple[List[Tuple[Path, str]], int]:
    """
    Find all summary files in the directory that match the filters (deduplicated by base name).
    Returns: (list of (Path, content) tuples for matched files, total unique files found)
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
    matched_items = []  # will hold (Path, content)
    
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
        
        # Read content once
        try:
            content = chosen_path.read_text(encoding='utf-8-sig')
        except Exception as e:
            if not quiet:
                print(f"Warning: Could not read {chosen_path.name}: {e}", file=sys.stderr)
            continue
        
        # Check filters
        if paper_matches_filters(content, desig_filter, topic_filter):
            matched_items.append((chosen_path, content))
        else:
            if not quiet:
                # Print which filter caused the exclusion
                designation = extract_designation(content)
                topics = extract_topics(content)
                if desig_filter and designation != desig_filter.lower():
                    print(f"Skipping {chosen_path.name} (designation: {designation}, filter: {desig_filter})", file=sys.stderr)
                elif topic_filter and topic_filter not in topics:
                    print(f"Skipping {chosen_path.name} (topics: {topics}, filter: {topic_filter})", file=sys.stderr)
    
    # Do NOT sort here; sorting is done in main based on --sort flag
    return matched_items, total_found


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
        "--output-dir", "-o",
        required=True,
        help="Output directory to place the compiled Markdown file."
    )
    parser.add_argument(
        "--designation", "-d",
        help="Filter by designation (e.g., international, local, international-algorithm-specific)."
    )
    parser.add_argument(
        "--topic", "-t",
        help="Filter by topic code (e.g., 7.C, 5.A, 13.B)."
    )
    # NEW: floor and ceiling instead of limit
    parser.add_argument(
        "--floor",
        type=int,
        help="Starting position (1‑based) of the range of papers to include (default: 1)."
    )
    parser.add_argument(
        "--ceiling",
        type=int,
        help="Ending position (1‑based, inclusive) of the range of papers to include (default: total matched)."
    )
    # NEW: sort flag
    parser.add_argument(
        "--sort",
        choices=["alpha", "year"],
        help="Sort order: 'alpha' (alphabetical by source filename) or 'year' (descending by year). If not specified, defaults to alphabetical (same as 'alpha')."
    )
    parser.add_argument(
        "--randomize", "-r",
        action="store_true",
        help="Randomize the order of papers after sorting (and before applying floor/ceiling)."
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

    output_dir = Path(args.output_dir)
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error: Could not create output directory '{args.output_dir}': {e}", file=sys.stderr)
        sys.exit(1)

    # Normalize filters
    desig_filter = args.designation.lower() if args.designation else None
    topic_filter = args.topic if args.topic else None

    # Determine base name components
    name_parts = []
    if desig_filter:
        name_parts.append(desig_filter.capitalize())
    if topic_filter:
        name_parts.append(topic_filter)
    if not name_parts:
        name_parts.append("All")
    
    # Add floor/ceiling to filename if specified
    if args.floor is not None:
        name_parts.append(f"Floor{args.floor}")
    if args.ceiling is not None:
        name_parts.append(f"Ceiling{args.ceiling}")
    
    # Add sort info
    if args.sort == "year":
        name_parts.append("YearSorted")
    elif args.sort == "alpha":
        name_parts.append("AlphaSorted")
    # if not specified, we still default to alpha but we don't need to mention in filename (backward compatible)
    
    # Add randomized indicator
    if args.randomize:
        name_parts.append("Randomized")
    
    # Assemble filename
    base_name = "-".join(name_parts) + "-Compilation.md"
    output_file = output_dir / base_name

    # Find and filter summary files – returns list of (path, content)
    matched_items, total_found = find_summary_files(input_dir, desig_filter, topic_filter, args.quiet)
    original_matched = len(matched_items)
    
    # items to process (list of (path, content))
    items = matched_items.copy()
    
    # Apply sorting (default: alphabetical if no --sort given, but we treat 'alpha' as default)
    sort_mode = args.sort if args.sort else "alpha"  # default to alphabetical for backward compatibility
    if sort_mode == "alpha":
        items.sort(key=lambda x: x[0].name)  # sort by filename
        if not args.quiet:
            print(f"Sorted alphabetically by filename.")
    elif sort_mode == "year":
        # Sort descending by year; papers without year go to the end
        def year_key(item):
            year = extract_year(item[1])
            # If year is None, treat as -1 so they appear after all real years
            return -year if year is not None else -float('inf')  # descending, so larger year first
        items.sort(key=year_key, reverse=False)  # but we want descending: use reverse=True with a positive key? Actually easier: key returns -year for real years, and -inf for missing; then reverse=False gives descending order? Let's think: if we want highest year first, we can return year and reverse=True, but then missing year (None) would be last if we set it to 0? Better: return year or -1, then reverse=True so highest first, but -1 would be last. That works: key = year or -1, reverse=True. But if year is 0? Not likely. So:
        def year_key(item):
            return extract_year(item[1]) or -1
        items.sort(key=year_key, reverse=True)
        if not args.quiet:
            print(f"Sorted by year descending.")
    
    # Randomize if requested (after sorting)
    if args.randomize:
        random.shuffle(items)
        if not args.quiet:
            print(f"Randomized order of {len(items)} papers.")
    
    # Apply floor and ceiling (range selection)
    total_items = len(items)
    floor = args.floor if args.floor is not None else 1
    ceiling = args.ceiling if args.ceiling is not None else total_items
    
    # Validate floor and ceiling
    if floor < 1:
        print("Warning: --floor must be at least 1. Using 1.", file=sys.stderr)
        floor = 1
    if ceiling < floor:
        print("Error: --ceiling must be greater than or equal to --floor.", file=sys.stderr)
        sys.exit(1)
    
    # Convert to 0‑based slice indices (ceiling inclusive -> end exclusive)
    start = floor - 1
    end = min(ceiling, total_items)  # inclusive, so slice up to ceiling
    
    if start >= total_items:
        # No items in range
        items = []
    else:
        items = items[start:end]
    
    included_count = len(items)
    if not args.quiet:
        if args.floor is not None or args.ceiling is not None:
            print(f"Selected papers {floor} to {ceiling} (out of {total_items} matched). Included: {included_count} papers.")

    if not items:
        print(f"Warning: No papers in the specified range (floor={floor}, ceiling={ceiling}) or no matching files found.", file=sys.stderr)
        if not args.quiet:
            if desig_filter or topic_filter:
                print(f"Filters applied: designation={desig_filter}, topic={topic_filter}", file=sys.stderr)
        # Still create an output file with the agent instruction
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(f"# Compiled Research Summaries\n\n")
            out.write(f"**Total Papers:** 0\n\n")
            if desig_filter or topic_filter:
                out.write("## Filters Applied\n\n")
                if desig_filter:
                    out.write(f"- Designation: `{desig_filter}`\n")
                if topic_filter:
                    out.write(f"- Topic: `{topic_filter}`\n")
                out.write("\n")
            out.write("No summary files match the given criteria.\n\n")
            out.write(AGENT_INSTRUCTION)
        print(f"Created empty output: {output_file}")
        sys.exit(0)

    # Process each matching file
    papers_processed = 0
    papers_failed = 0
    errors = []

    with open(output_file, 'w', encoding='utf-8') as out:
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
        
        # Show total papers after range and sorting
        out.write(f"**Total Papers:** {included_count}\n\n")
        notes = []
        if args.floor is not None or args.ceiling is not None:
            range_str = f"positions {floor} to {ceiling}"
            if included_count < (ceiling - floor + 1) and ceiling > total_items:
                range_str += f" (clipped to {total_items} available)"
            notes.append(f"Included papers {range_str}")
        if args.sort:
            notes.append(f"Sorted by {args.sort}")
        if args.randomize:
            notes.append("Order randomized")
        if notes:
            out.write(f"**Note:** {', '.join(notes)}.\n\n")
        out.write(f"---\n\n")

        for i, (filepath, content) in enumerate(items, 1):
            try:
                # Clean up any trailing whitespace
                content = content.strip()
                
                # Write paper header
                out.write(f"## Paper {i}: {filepath.name}\n\n")
                out.write(f"**Source File:** `{filepath.name}`\n\n")
                out.write(content)
                out.write("\n---\n\n")
                
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
        print(f"Output directory: {output_dir}")
        print(f"Output file:      {output_file.name}")
        if desig_filter or topic_filter:
            print(f"Filters applied:  designation={desig_filter}, topic={topic_filter}")
        print(f"Files found:      {total_found}")
        print(f"Files matched:    {original_matched}")
        if args.sort:
            print(f"Sort order:       {args.sort}")
        if args.randomize:
            print(f"Randomized:       Yes")
        if args.floor is not None or args.ceiling is not None:
            print(f"Range selected:   {floor} to {ceiling} (included {included_count})")
        print(f"Papers processed: {papers_processed}")
        if papers_failed > 0:
            print(f"Papers failed:    {papers_failed}")
            print(f"\nErrors:")
            for err in errors:
                print(f"  - {err}")
        print(f"{'='*50}")


if __name__ == "__main__":
    main()