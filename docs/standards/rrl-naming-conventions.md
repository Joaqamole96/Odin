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

Each paper has up to three files, distinguished by suffix:

| Suffix | Meaning | Location |
|--------|---------|----------|
| `.pdf` | Source paper PDF | `RRL/01_Papers/` |
| `_marked.md` | Markdown conversion (extracted text) | `RRL/03_Conversions/` |
| `_summarized.md` | Structured YAML summary | `RRL/02_Summaries/` |
| `_Compilation.md` | Multi-paper compilation for a topic | `RRL/04_Compilations/` |

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

RRL compilation folders use codes from `Topic-Outline.md`:

```
RRL/04_Compilations/{Topic}.{Letter}/
```

Examples: `1.A/`, `5.C/`, `8.B/`, `13.A/`

The special folder `01_Irrelevant/` holds papers culled from the active corpus.
