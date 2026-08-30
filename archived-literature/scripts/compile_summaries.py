#!/usr/bin/env python3
"""
Compile all summary files into a single document, with optional filtering, range selection, and sorting.

Supports JSON (preferred), YAML, and Markdown summary files.
JSON summaries are parsed with json.load() for reliable field extraction.
YAML/Markdown summaries use regex-based extraction as a fallback.

Usage:
    python3 compile_summaries.py --input ./summaries --output-dir ./compiled
    python3 compile_summaries.py -i ./summaries -o ./out -d international
    python3 compile_summaries.py -i ./summaries -o ./out -t 7.C
    python3 compile_summaries.py -i ./summaries -o ./out --sort year
    python3 compile_summaries.py -i ./summaries -o ./out --format json
"""

import argparse
import json
import re
import sys
import random
from pathlib import Path
from typing import List, Optional, Tuple


AGENT_INSTRUCTION = """
---

## Agent Instruction

If the agent reading this document believes further context about a paper is needed, it may request the original converted markdown file (with the '_marked' suffix) or the original summary JSON file from the user for the relevant paper(s).
"""

# Preferred extension priority: .json > .yaml > .yml > .md
EXT_PRIORITY = [".json", ".yaml", ".yml", ".md"]


def get_base_filename(filename: str) -> str:
    """Extract base name without extension and without summary suffixes."""
    stem = Path(filename).stem
    for suffix in ["_summarized", "_summarized"]:
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    return stem


def load_json_summary(filepath: Path) -> Optional[dict]:
    """Load and parse a JSON summary file. Returns None on failure."""
    try:
        data = json.loads(filepath.read_text(encoding="utf-8-sig"))
        if isinstance(data, dict):
            return data
        return None
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None


def extract_field_from_text(content: str, field: str) -> Optional[str]:
    """Extract a simple string field from YAML/Markdown text using regex."""
    pattern = re.compile(rf"^{field}:\s*[\"']?([^\"'\n]+)[\"']?", re.MULTILINE)
    match = pattern.search(content)
    if match:
        return match.group(1).strip()
    return None


def extract_year_from_text(content: str) -> Optional[int]:
    """Extract year from YAML/Markdown text."""
    pattern = re.compile(r"^year:\s*(\d{4})", re.MULTILINE)
    match = pattern.search(content)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            return None
    return None


def extract_designation_from_text(content: str) -> Optional[str]:
    """Extract designation from YAML/Markdown text."""
    val = extract_field_from_text(content, "designation")
    return val.lower() if val else None


def extract_topics_from_text(content: str) -> List[str]:
    """Extract odin_topics from YAML/Markdown text."""
    topics = []
    pattern = re.compile(r"^odin_topics:\s*$", re.MULTILINE)
    match = pattern.search(content)
    if not match:
        inline = re.compile(r"^odin_topics:\s*\[(.*?)\]", re.MULTILINE)
        inline_match = inline.search(content)
        if inline_match:
            return [
                t.strip().strip("\"'")
                for t in inline_match.group(1).split(",")
                if t.strip()
            ]
        return topics

    start_pos = match.end()
    lines = content[start_pos:].split("\n")
    for line in lines:
        stripped = line.strip()
        if re.match(r"^[a-zA-Z_][a-zA-Z0-9_-]*:", stripped):
            break
        if not stripped:
            continue
        if stripped.startswith("- "):
            item = stripped[2:].strip()
        elif stripped.startswith("-"):
            item = stripped[1:].strip()
        else:
            if re.match(r"^[0-9]+\.[A-Z]", stripped):
                item = stripped
            else:
                break
        if item:
            item = item.strip().strip("\"'")
            if item:
                topics.append(item)
    return topics


def extract_fields_from_content(
    content: str, filepath: Path
) -> Tuple[Optional[str], Optional[str], Optional[int], List[str]]:
    """Extract designation, year, and topics from file content.
    Returns (designation, filename_for_year, year, topics).
    """
    ext = filepath.suffix.lower()
    if ext == ".json":
        data = load_json_summary(filepath)
        if data:
            return (
                data.get("designation"),
                filepath.name,
                data.get("year"),
                data.get("odin_topics", []),
            )

    # Fallback: regex extraction from YAML/Markdown text
    designation = extract_designation_from_text(content)
    year = extract_year_from_text(content)
    topics = extract_topics_from_text(content)
    return designation, filepath.name, year, topics


def paper_matches_filters(
    content: str, filepath: Path, desig_filter: Optional[str], topic_filter: Optional[str]
) -> bool:
    """Check if a paper matches the given filters."""
    if not desig_filter and not topic_filter:
        return True

    designation, _, _, topics = extract_fields_from_content(content, filepath)

    if desig_filter and designation != desig_filter.lower():
        return False
    if topic_filter and topic_filter not in topics:
        return False
    return True


def find_summary_files(
    input_dir: Path,
    desig_filter: Optional[str] = None,
    topic_filter: Optional[str] = None,
    quiet: bool = False,
) -> Tuple[List[Tuple[Path, str, dict]], int]:
    """Find all summary files matching filters (deduplicated by base name).

    Returns: (list of (Path, content, parsed_data) tuples, total unique files found)
    parsed_data is a dict for JSON files, or None for legacy YAML/Markdown.
    """
    file_map: dict[str, dict[str, Path]] = {}

    for ext in EXT_PRIORITY:
        for f in input_dir.glob(f"*{ext}"):
            base = get_base_filename(f.name)
            if base not in file_map:
                file_map[base] = {}
            file_map[base][ext] = f

    total_found = len(file_map)
    matched_items: List[Tuple[Path, str, dict]] = []

    for base, ext_map in file_map.items():
        chosen_path = None
        for ext in EXT_PRIORITY:
            if ext in ext_map:
                chosen_path = ext_map[ext]
                break
        if chosen_path is None:
            continue

        try:
            content = chosen_path.read_text(encoding="utf-8-sig")
        except Exception as e:
            if not quiet:
                print(f"Warning: Could not read {chosen_path.name}: {e}", file=sys.stderr)
            continue

        # Parse JSON files
        parsed = None
        if chosen_path.suffix.lower() == ".json":
            parsed = load_json_summary(chosen_path)

        if paper_matches_filters(content, chosen_path, desig_filter, topic_filter):
            matched_items.append((chosen_path, content, parsed))
        else:
            if not quiet:
                designation, _, _, topics = extract_fields_from_content(
                    content, chosen_path
                )
                if desig_filter and designation != desig_filter.lower():
                    print(
                        f"Skipping {chosen_path.name} (designation: {designation}, filter: {desig_filter})",
                        file=sys.stderr,
                    )
                elif topic_filter and topic_filter not in topics:
                    print(
                        f"Skipping {chosen_path.name} (topics: {topics}, filter: {topic_filter})",
                        file=sys.stderr,
                    )

    return matched_items, total_found


def format_paper_entry(i: int, filepath: Path, content: str, parsed: Optional[dict]) -> str:
    """Format a single paper entry for the compiled output."""
    lines = [f"## Paper {i}: {filepath.name}\n"]
    lines.append(f"**Source File:** `{filepath.name}`\n")

    if parsed:
        # JSON file: render as formatted JSON block
        lines.append("```json")
        lines.append(json.dumps(parsed, indent=2, ensure_ascii=False))
        lines.append("```\n")
    else:
        # Legacy YAML/Markdown: include raw content
        lines.append(content.strip())
        lines.append("")

    lines.append("---\n")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Compile summary files into a single document."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Directory containing summary files (.json, .yaml, .yml, .md).",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        required=True,
        help="Output directory for the compiled file.",
    )
    parser.add_argument(
        "--designation",
        "-d",
        help="Filter by designation (e.g., international, local).",
    )
    parser.add_argument(
        "--topic",
        "-t",
        help="Filter by topic code (e.g., 7.C, 5.A).",
    )
    parser.add_argument(
        "--floor",
        type=int,
        help="Starting position (1-based) of paper range (default: 1).",
    )
    parser.add_argument(
        "--ceiling",
        type=int,
        help="Ending position (1-based, inclusive) of paper range (default: total matched).",
    )
    parser.add_argument(
        "--sort",
        choices=["alpha", "year"],
        help="Sort order: 'alpha' (by filename) or 'year' (descending). Default: alpha.",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format: 'markdown' (default) or 'json'.",
    )
    parser.add_argument(
        "--randomize",
        "-r",
        action="store_true",
        help="Randomize order after sorting.",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress progress messages.",
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
        print(f"Error: Could not create output directory: {e}", file=sys.stderr)
        sys.exit(1)

    desig_filter = args.designation.lower() if args.designation else None
    topic_filter = args.topic if args.topic else None

    # Determine output filename
    name_parts = []
    if desig_filter:
        name_parts.append(desig_filter.capitalize())
    if topic_filter:
        name_parts.append(topic_filter)
    if not name_parts:
        name_parts.append("All")
    if args.floor is not None:
        name_parts.append(f"Floor{args.floor}")
    if args.ceiling is not None:
        name_parts.append(f"Ceiling{args.ceiling}")
    if args.sort == "year":
        name_parts.append("YearSorted")
    elif args.sort == "alpha":
        name_parts.append("AlphaSorted")
    if args.randomize:
        name_parts.append("Randomized")

    if args.format == "json":
        ext = ".json"
    else:
        ext = "-Compilation.md"
    base_name = "-".join(name_parts) + ext
    output_file = output_dir / base_name

    # Find and filter
    matched_items, total_found = find_summary_files(
        input_dir, desig_filter, topic_filter, args.quiet
    )
    original_matched = len(matched_items)
    items = matched_items.copy()

    # Sort
    sort_mode = args.sort if args.sort else "alpha"
    if sort_mode == "alpha":
        items.sort(key=lambda x: x[0].name)
        if not args.quiet:
            print("Sorted alphabetically by filename.")
    elif sort_mode == "year":
        def year_key(item):
            _, _, parsed = item
            if parsed and isinstance(parsed.get("year"), int):
                return parsed["year"]
            return extract_year_from_text(item[1]) or -1
        items.sort(key=year_key, reverse=True)
        if not args.quiet:
            print("Sorted by year descending.")

    if args.randomize:
        random.shuffle(items)
        if not args.quiet:
            print(f"Randomized order of {len(items)} papers.")

    # Apply range
    total_items = len(items)
    floor = args.floor if args.floor is not None else 1
    ceiling = args.ceiling if args.ceiling is not None else total_items

    if floor < 1:
        print("Warning: --floor must be at least 1. Using 1.", file=sys.stderr)
        floor = 1
    if ceiling < floor:
        print("Error: --ceiling must be >= --floor.", file=sys.stderr)
        sys.exit(1)

    start = floor - 1
    end = min(ceiling, total_items)
    if start >= total_items:
        items = []
    else:
        items = items[start:end]

    included_count = len(items)
    if not args.quiet and (args.floor is not None or args.ceiling is not None):
        print(f"Selected papers {floor} to {ceiling} (out of {total_items}). Included: {included_count}.")

    if not items:
        print(f"Warning: No papers in the specified range.", file=sys.stderr)
        if args.format == "json":
            output_file.write_text(json.dumps([], indent=2) + "\n", encoding="utf-8")
        else:
            with open(output_file, "w", encoding="utf-8") as out:
                out.write("# Compiled Research Summaries\n\n")
                out.write("**Total Papers:** 0\n\n")
                out.write("No summary files match the given criteria.\n\n")
                out.write(AGENT_INSTRUCTION)
        print(f"Created empty output: {output_file}")
        sys.exit(0)

    # Process papers
    papers_processed = 0
    papers_failed = 0
    errors = []

    if args.format == "json":
        # JSON output: array of summary objects
        json_papers = []
        for filepath, content, parsed in items:
            try:
                if parsed:
                    json_papers.append(parsed)
                else:
                    # Legacy file: include raw content
                    json_papers.append(
                        {
                            "_source_file": filepath.name,
                            "_format": "legacy-yaml-markdown",
                            "_raw_content": content.strip(),
                        }
                    )
                papers_processed += 1
            except Exception as e:
                papers_failed += 1
                errors.append(f"{filepath.name}: {str(e)}")

        output_file.write_text(
            json.dumps(json_papers, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    else:
        # Markdown output
        with open(output_file, "w", encoding="utf-8") as out:
            out.write("# Compiled Research Summaries\n\n")

            if desig_filter or topic_filter:
                out.write("## Filters Applied\n\n")
                if desig_filter:
                    out.write(f"- Designation: `{desig_filter}`\n")
                if topic_filter:
                    out.write(f"- Topic: `{topic_filter}`\n")
                out.write("\n")

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
            out.write("---\n\n")

            for i, (filepath, content, parsed) in enumerate(items, 1):
                try:
                    out.write(format_paper_entry(i, filepath, content, parsed))
                    papers_processed += 1
                except Exception as e:
                    papers_failed += 1
                    errors.append(f"Paper {i} ({filepath.name}): {str(e)}")
                    out.write(f"## Paper {i}: {filepath.name}\n\n")
                    out.write(f"**ERROR:** Could not read this file.\n\n")
                    out.write(f"```\n{filepath.name}: {str(e)}\n```\n\n")
                    out.write("---\n\n")

            out.write(AGENT_INSTRUCTION)

    # Summary
    if not args.quiet:
        print(f"\n{'=' * 50}")
        print("COMPILATION COMPLETE")
        print(f"{'=' * 50}")
        print(f"Input directory:  {input_dir}")
        print(f"Output directory: {output_dir}")
        print(f"Output file:      {output_file.name}")
        print(f"Output format:    {args.format}")
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
            print("\nErrors:")
            for err in errors:
                print(f"  - {err}")
        print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
