# RRL Naming Conventions

> **Note:** topic codes referenced below follow the **old** topic outline. The new thesis topical outline is `docs/thesis/topical-outline/topical-outline.md`; re-mapping the RRL taxonomy to it is pending.
>
> **RRL migration:** the curated corpus moved to **Odin-Literature**. Processing suffixes now point there; only the source `.pdf` stays in `Odin-Paper/literature/papers/`. See `literature/_MIGRATION.md`.

## Source Prefixes

Every curated paper file uses a prefix to indicate geographic/institutional origin.

| Prefix | Meaning | Example |
|--------|---------|---------|
| `L--` | Local (Philippine) | `L--Cuevas-2023.pdf` |
| `I--` | International | `I--Smith-2024.pdf` |
| `A--` | Algorithm/system focus | `A--LSTM-Spending-Forecast.pdf` |
| `AI--` | Algorithm + international | `AI--Transformer-Anomaly.pdf` |
| `IA--` | International + algorithm (legacy) | `IA--Gradient-Boosting.pdf` |
| `AL--` | Algorithm + local (legacy) | `AL--RF-Profiling.pdf` |
| `LA--` | Local + algorithm (legacy) | `LA--Isolation-Forest.pdf` |

**Convention**: Use `L--`, `I--`, or `A--` for new papers. The compound prefixes (`AI--`, `IA--`, `AL--`, `LA--`) exist in legacy files only; prefix order is inconsistent across older entries.

## Processing Suffixes

Each paper has up to four files, distinguished by suffix:

| Suffix | Meaning | Location |
|--------|---------|----------|
| `.pdf` | Source paper PDF | `Odin-Paper/literature/papers/` |
| `_marked.md` | Markdown conversion with YAML frontmatter | `Odin-Literature/literature/conversions/batch-<N>/` |
| `_summarized.json` | Structured JSON summary | `Odin-Literature/literature/conversions/batch-<N>/` (same folder as `_marked.md`) |
| `_Compilation.md` | Multi-paper compilation for a topic (legacy/deprecated) | `Odin-Paper/literature/compilations/` |

### Legacy Suffixes

The following suffixes are still supported for reading but should not be produced for new files:

| Suffix | Legacy Meaning |
|--------|---------------|
| `_summarized.yaml` | YAML summary (pre-v6.0) |
| `_summarized.md` | Markdown summary (pre-v6.0) |

## Synthesis File Naming

Per-topic and cross-topic synthesis documents use this convention:

```
{Topic}.{Letter}_Synthesis.md
```

Examples:
- `6.A_Synthesis.md` — synthesis for Topic 6.A (Predictive Modeling)
- `5.C_Synthesis.md` — synthesis for Topic 5.C (Classification Approaches)
- `7x8_Cross-Synthesis.md` — cross-topic synthesis for Topics 7 and 8

Location: `literature/syntheses/` (does not exist yet — create when the first synthesis is produced)

## File Stem Format

```
{Prefix}--{AuthorLastName}-{Year}{LetterSuffix}
```

Examples:
- `L--Cuevas-2023.pdf` — Philippine paper by Cuevas, 2023
- `I--Smith-2024a.pdf` — International paper by Smith, 2024, first of multiple
- `A--LSTM-Spending-Forecast.pdf` — Algorithm-focused paper (no author-based stem)

The `LetterSuffix` (a, b, c...) is used when multiple papers share the same author and year.

## Topic-Subtopic Folder Codes

Legacy RRL compilation folders use the old-outline topic codes (see note at top):

```
literature/compilations/{Topic}.{Letter}/
```

Examples: `1.A/`, `5.C/`, `8.B/`, `14.A/`

The folder set is **deprecated** — the migration deprecated `literature/compilations/`. Relevance tiers (crucial/supporting/cull) are now assigned automatically by Odin-Literature `scripts/score.py`.
