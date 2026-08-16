# RRL Migration Notice

**The curated RRL corpus has moved out of `Odin-Paper/literature/`.**

All processed conversions and structured summaries now live in the dedicated
literature repository:

> **`Odin-Literature`** — https://github.com/VibeCoders-3DCSAD/Odin-Literature

Read `Odin-Literature/README.md` for the scoring pipeline (`config/modules.yaml`,
`scripts/embed.py`, `scripts/score.py`) and `Odin-Literature/scores/` for the
per-module relevance, quality, tier, and redundancy outputs.

## What happened here

| Path | Status | Where it is now |
|------|--------|-----------------|
| `literature/conversions/` (518 `_marked.md` + 518 `_summarized.json`) | **Deleted** | `Odin-Literature/literature/conversions/` (identical copies) |
| `literature/summaries/` (23 JSON) | **Deleted** | Redundant — all stems already in `Odin-Literature/literature/conversions/` |
| `literature/archive/2026-07-20_190503/` (114 MB snapshot) | **Deleted** | Superseded by the current conversions + Odin-Literature |
| `literature/compilations/` (old 1.A–14.C topic copies) | **Kept, deprecated** | Content duplicated in Odin-Literature; see `compilations/DEPRECATED.md` |
| `literature/papers/` (518 source PDFs, Git LFS) | **Kept** | Ground-truth source PDFs — NOT stored in Odin-Literature (gitignored there) |
| `literature/bucket/` (new-paper intake) | **Kept** | Active intake pool |
| `literature/scripts/` | **Kept** | Intake/conversion utilities (produce the files that move to Odin-Literature) |
| `literature/skills/` | **Kept** | Summarizer/synthesis prompts still active; scorer & culler superseded |

Deleted content is fully preserved in this repository's git history.

## New RRL workflow (single source of truth)

Detailed docs: `docs/standards/rrl-workflow.md`. Summary:

1. **Intake** — place new candidate PDFs in `literature/bucket/`.
2. **Convert** — `python3 literature/scripts/prepare_pdf.py literature/bucket/ --page-aware`
   produces `{stem}_marked.md` (with metadata frontmatter) + empty `{stem}_summarized.json`.
3. **Summarize** — use `literature/skills/paper-summarizer-skill.md` as an AI prompt
   to fill `{stem}_summarized.json`. Schema: `docs/standards/summary-format.md`.
4. **Move to Odin-Literature** — copy the pair into
   `Odin-Literature/literature/conversions/batch-<N>/`.
5. **Score** — in Odin-Literature:
   ```bash
   python3 scripts/embed.py        # rebuild caches when conversions change
   python3 scripts/score.py        # relevance/quality tiers, redundancy, validation
   ```
6. **Adapt** — edit `Odin-Literature/config/modules.yaml` (module queries, weights,
   thresholds) and re-run `score.py`. No code changes needed.

## Notes for members

- **Do not** create new files under the old `literature/conversions/` / `summaries/`
  directories — they are gone. Route new work through Odin-Literature.
- The relevance/quality scoring is now **offline and automated** (BERT + TF-IDF + BM25
  + rule-based quality). The old AI `paper-scorer`/`paper-culler` skills are superseded
  (see `literature/skills/DEPRECATED.md`); their scoring logic is reimplemented in
  `Odin-Literature/scripts/score.py`.
- `docs/standards/rrl-naming-conventions.md` and `summary-format.md` still govern file
  naming and the JSON schema — they now apply to the files in Odin-Literature.
