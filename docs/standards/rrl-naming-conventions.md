# RRL Naming Conventions

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
| `.pdf` | Source paper PDF | `rrl/papers/` |
| `_marked.md` | Markdown conversion with YAML frontmatter | `rrl/conversions/` |
| `_summarized.json` | Structured JSON summary | `rrl/summaries/` |
| `_Compilation.md` | Multi-paper compilation for a topic | `rrl/compilations/` |

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

Location: `rrl/syntheses/`

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

RRL compilation folders use codes from `topic-outline.md`:

```
rrl/compilations/{Topic}.{Letter}/
```

Examples: `1.A/`, `5.C/`, `8.B/`, `14.A/`

The special folder `01_Irrelevant/` holds papers culled from the active corpus.
