#!/usr/bin/env python3
"""
RRL Pipeline Orchestrator

Usage: python3 pipeline.py --input-dir <bucket> [--output-dir <literature>] [--step STEP]

Chains the full RRL processing pipeline:
  1. convert    — Run prepare_pdf.py on input directory
  2. manifest   — List unsummarized files ready for the summarizer agent
  3. validate   — Check that summary JSON files are well-formed
  4. compile    — Run compile_summaries.py on a summary directory

Steps 2 and 3 produce output for human/agent consumption.
Steps 1 and 4 invoke the underlying scripts.

The script logs a pipeline_run.json with timestamps and status for each step.
"""

import argparse
import json
import logging
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
RRL_DIR = SCRIPTS_DIR.parent
ROOT_DIR = RRL_DIR.parent


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def step_convert(input_dir: Path, output_dir: Path, args: dict) -> dict:
    """Run prepare_pdf.py on the input directory."""
    cmd = [
        sys.executable,
        str(SCRIPTS_DIR / "prepare_pdf.py"),
        str(input_dir),
    ]
    if args.get("page_aware"):
        cmd.append("--page-aware")
    if args.get("json_sidecar"):
        cmd.append("--json-sidecar")

    logging.info(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    return {
        "step": "convert",
        "status": "success" if result.returncode == 0 else "failure",
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def step_manifest(input_dir: Path) -> dict:
    """List _marked.md files that have no corresponding _summarized.json."""
    marked_files = sorted(input_dir.glob("*_marked.md"))
    unsummarized = []
    already_summarized = []

    for mf in marked_files:
        stem = mf.stem.replace("_marked", "")
        summary_json = input_dir / f"{stem}_summarized.json"
        summary_yaml = input_dir / f"{stem}_summarized.yaml"
        summary_md = input_dir / f"{stem}_summarized.md"

        if summary_json.exists() or summary_yaml.exists() or summary_md.exists():
            already_summarized.append(mf.name)
        else:
            unsummarized.append(mf.name)

    return {
        "step": "manifest",
        "status": "success",
        "total_marked": len(marked_files),
        "unsummarized": unsummarized,
        "already_summarized": already_summarized,
    }


def step_validate(input_dir: Path) -> dict:
    """Check that *_summarized.json files are valid JSON."""
    json_files = sorted(input_dir.glob("*_summarized.json"))
    valid = []
    invalid = []

    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
            # Basic schema check: must have required top-level keys
            required = {"paper_id", "title", "authors", "year", "tldr"}
            missing = required - set(data.keys())
            if missing:
                invalid.append({"file": jf.name, "error": f"missing keys: {missing}"})
            else:
                valid.append(jf.name)
        except json.JSONDecodeError as e:
            invalid.append({"file": jf.name, "error": f"invalid JSON: {e}"})
        except Exception as e:
            invalid.append({"file": jf.name, "error": str(e)})

    return {
        "step": "validate",
        "status": "success",
        "total_json": len(json_files),
        "valid": len(valid),
        "invalid": invalid,
    }


def step_compile(
    input_dir: Path,
    output_dir: Path,
    designation: str | None = None,
    topic: str | None = None,
    sort: str | None = None,
) -> dict:
    """Run compile_summaries.py on a summary directory."""
    cmd = [
        sys.executable,
        str(SCRIPTS_DIR / "compile_summaries.py"),
        "--input",
        str(input_dir),
        "--output-dir",
        str(output_dir),
    ]
    if designation:
        cmd.extend(["--designation", designation])
    if topic:
        cmd.extend(["--topic", topic])
    if sort:
        cmd.extend(["--sort", sort])

    logging.info(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    return {
        "step": "compile",
        "status": "success" if result.returncode == 0 else "failure",
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def main():
    parser = argparse.ArgumentParser(
        description="RRL Pipeline Orchestrator — chains conversion, manifest, validation, and compilation."
    )
    parser.add_argument(
        "--input-dir",
        "-i",
        required=True,
        help="Input directory (e.g., literature/bucket)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default=None,
        help="Output directory for compilations (default: same as input-dir)",
    )
    parser.add_argument(
        "--step",
        "-s",
        choices=["convert", "manifest", "validate", "compile", "all"],
        default="all",
        help="Which pipeline step to run (default: all)",
    )
    parser.add_argument(
        "--designation",
        "-d",
        help="Filter for compile step (e.g., local, international)",
    )
    parser.add_argument(
        "--topic",
        "-t",
        help="Filter for compile step (e.g., 7.C, 5.A)",
    )
    parser.add_argument(
        "--sort",
        choices=["alpha", "year"],
        help="Sort order for compile step",
    )
    parser.add_argument("--page-aware", action="store_true", help="Enable page-aware extraction for convert step")
    parser.add_argument("--json-sidecar", action="store_true", help="Write JSON sidecar for convert step")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress progress messages")
    parser.add_argument("--log-file", default=None, help="Write pipeline run log to this file (JSON)")

    args = parser.parse_args()

    log_level = logging.WARNING if args.quiet else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve() if args.output_dir else input_dir

    if not input_dir.is_dir():
        logging.error(f"Input directory '{input_dir}' does not exist.")
        sys.exit(1)

    pipeline_log = {
        "pipeline_run_at": now_iso(),
        "input_dir": str(input_dir),
        "output_dir": str(output_dir),
        "steps": [],
    }

    steps_to_run = (
        ["convert", "manifest", "validate", "compile"]
        if args.step == "all"
        else [args.step]
    )

    convert_args = {"page_aware": args.page_aware, "json_sidecar": args.json_sidecar}

    for step_name in steps_to_run:
        logging.info(f"--- Step: {step_name} ---")
        start = now_iso()

        if step_name == "convert":
            result = step_convert(input_dir, output_dir, convert_args)
        elif step_name == "manifest":
            result = step_manifest(input_dir)
        elif step_name == "validate":
            result = step_validate(input_dir)
        elif step_name == "compile":
            result = step_compile(
                input_dir,
                output_dir,
                designation=args.designation,
                topic=args.topic,
                sort=args.sort,
            )
        else:
            continue

        result["started_at"] = start
        result["completed_at"] = now_iso()
        pipeline_log["steps"].append(result)

        if not args.quiet:
            if result["status"] == "success":
                logging.info(f"Step '{step_name}' completed successfully.")
            else:
                logging.warning(f"Step '{step_name}' failed (returncode={result.get('returncode')})")
                if result.get("stderr"):
                    logging.warning(result["stderr"])

    pipeline_log["completed_at"] = now_iso()

    # Write pipeline log
    log_path = Path(args.log_file) if args.log_file else input_dir / "pipeline_run.json"
    log_path.write_text(json.dumps(pipeline_log, indent=2) + "\n", encoding="utf-8")
    if not args.quiet:
        logging.info(f"Pipeline log written to: {log_path}")


if __name__ == "__main__":
    main()
