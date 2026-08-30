#!/usr/bin/env python3
"""
Batch convert first N PDFs (alphabetically) to markdown, skipping heavy files.

Usage: python3 convert_batch.py <input_dir> <output_dir> [--limit N] [--max-size MB] [--page-aware]
"""

import argparse
import hashlib
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from markitdown import MarkItDown
from pypdf import PdfReader

try:
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LAParams, LTTextBox

    PDFMINER_AVAILABLE = True
except ImportError:
    PDFMINER_AVAILABLE = False


def compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def get_pdf_page_count(pdf_path: Path) -> int | None:
    try:
        reader = PdfReader(str(pdf_path))
        return len(reader.pages)
    except Exception:
        return None


def get_markitdown_version() -> str:
    try:
        import importlib.metadata
        return importlib.metadata.version("markitdown")
    except Exception:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Batch convert first N PDFs.")
    parser.add_argument("input_dir", help="Directory containing PDF files")
    parser.add_argument("output_dir", help="Directory to write _marked.md and _summarized.json")
    parser.add_argument("--limit", type=int, default=100, help="Max PDFs to process (default: 100)")
    parser.add_argument("--max-size", type=float, default=5.0, help="Skip PDFs larger than this in MB (default: 5.0)")
    parser.add_argument("--page-aware", action="store_true", help="Add page markers with paragraph detection via pdfminer.six")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect and sort PDFs alphabetically
    pdf_files = sorted(input_dir.glob("*.pdf"))
    logging.info(f"Found {len(pdf_files)} PDFs total in {input_dir}")

    # Apply limit
    pdf_files = pdf_files[:args.limit]
    logging.info(f"Processing first {len(pdf_files)} (limit={args.limit})")

    # Filter by size
    max_bytes = int(args.max_size * 1024 * 1024)
    skipped_size = []
    to_process = []
    for pdf in pdf_files:
        size = pdf.stat().st_size
        if size > max_bytes:
            skipped_size.append((pdf.name, size / 1048576))
        else:
            to_process.append(pdf)

    if skipped_size:
        logging.info(f"Skipping {len(skipped_size)} PDFs > {args.max_size}MB:")
        for name, mb in skipped_size:
            logging.info(f"  {name}: {mb:.1f}MB")

    logging.info(f"Will convert {len(to_process)} PDFs")

    md_converter = MarkItDown()
    converter_version = get_markitdown_version()
    success = 0
    failed = 0
    start = time.time()

    for idx, pdf_path in enumerate(to_process, 1):
        stem = pdf_path.stem
        marked_path = output_dir / f"{stem}_marked.md"
        summary_path = output_dir / f"{stem}_summarized.json"
        elapsed = time.time() - start
        rate = idx / (elapsed / 60) if elapsed > 0 else 0
        eta_min = (len(to_process) - idx) / rate if rate > 0 else 0

        logging.info(f"[{idx}/{len(to_process)}] {pdf_path.name} ({pdf_path.stat().st_size/1048576:.1f}MB) ETA: {eta_min:.0f}m")

        try:
            page_count = get_pdf_page_count(pdf_path)
            pdf_hash = compute_sha256(pdf_path)
            now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

            # Convert with MarkItDown
            result = md_converter.convert(str(pdf_path))
            md_content = result.text_content

            # Page-aware: prepend pdfminer extraction with page markers and paragraphs
            if args.page_aware:
                if not PDFMINER_AVAILABLE:
                    logging.warning(f"  pdfminer.six not available, skipping page-aware extraction")
                else:
                    try:
                        laparams = LAParams(line_margin=0.5)
                        page_parts = []
                        for pi, page_layout in enumerate(
                            extract_pages(str(pdf_path), laparams=laparams), 1
                        ):
                            paragraphs = []
                            for element in page_layout:
                                if isinstance(element, LTTextBox):
                                    text = element.get_text().strip()
                                    if text:
                                        paragraphs.append(text)
                            if paragraphs:
                                page_text = "\n\n".join(paragraphs)
                                page_parts.append(f"<!-- PAGE {pi} -->\n\n{page_text}")
                        if page_parts:
                            page_md = "\n\n---\n\n".join(page_parts)
                            md_content = (
                                f"<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->\n\n"
                                f"{page_md}\n\n"
                                f"<!-- MARKITDOWN CONVERSION -->\n\n"
                                f"<!-- Full MarkItDown conversion for formatting fidelity. -->\n\n"
                                f"{md_content}"
                            )
                    except Exception as e:
                        logging.warning(f"  Page-aware extraction failed: {e}")

            # Frontmatter
            frontmatter = "\n".join([
                "---",
                "conversion_metadata:",
                f'  converted_at: "{now}"',
                f'  converter_tool: "markitdown"',
                f'  converter_version: "{converter_version}"',
                f'  source_pdf: "{pdf_path.name}"',
                f'  source_pdf_sha256: "{pdf_hash}"',
                f"  page_count: {page_count}" if page_count else "  page_count: null",
                f"  markdown_char_count: {len(md_content)}",
                "---",
            ])
            md_content = f"{frontmatter}\n\n{md_content}"

            # Write outputs
            marked_path.write_text(md_content, encoding="utf-8")
            summary_path.write_text(json.dumps({}, indent=2) + "\n", encoding="utf-8")
            success += 1

        except Exception as e:
            logging.error(f"  FAILED: {e}")
            failed += 1

    elapsed = time.time() - start
    logging.info(f"\nDone: {success} converted, {failed} failed, {len(skipped_size)} skipped (too large)")
    logging.info(f"Time: {elapsed/60:.1f} minutes ({elapsed/len(to_process):.1f}s avg per PDF)" if to_process else "")

    # Write manifest
    manifest = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "input_dir": str(input_dir),
        "output_dir": str(output_dir),
        "limit": args.limit,
        "max_size_mb": args.max_size,
        "page_aware": args.page_aware,
        "total_pdfs": len(list(input_dir.glob("*.pdf"))),
        "processed": success,
        "failed": failed,
        "skipped_too_large": len(skipped_size),
        "skipped_files": [name for name, _ in skipped_size],
        "elapsed_seconds": round(elapsed, 1),
    }
    manifest_path = output_dir / "batch_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    logging.info(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
