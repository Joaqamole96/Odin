# Skill: Relevance Culler for Odin Literature

```yaml
name: relevance-culler
description: |
  Parses a compilation of YAML paper summaries, calculates relevance scores from 
  topic counts (High/Medium/Low), applies a primary filter, ranks survivors by 
  density, and outputs a Markdown table with pass/fail and selection status. 
  Designation-agnostic — culls purely on relevance to Odin's functional domains.
version: 1.0
date: 2026-06-27
author: Odin Research Team
```

---

## Input

The skill accepts a single Markdown file containing multiple YAML summaries, each wrapped in ` ```yaml ... ``` ` blocks.

**Required fields from each YAML summary:**
- `title`
- `year`
- `venue`
- `relevance.topics` (list of objects, each with a `relevance` field: `high`, `medium`, `low`, or `contextual`)

---

## Step 1 – Data Extraction

For each paper, the skill extracts and counts:

| Variable | Description |
|----------|-------------|
| `H` | Count of topics marked `high` |
| `M` | Count of topics marked `medium` |
| `L` | Count of topics marked `low` |
| `Total` | `H + M + L` *(`contextual` topics are ignored)* |

---

## Step 2 – Primary Filter (Pass / Fail)

A paper passes if it satisfies **ANY ONE** of:

| Rule | Condition |
|------|-----------|
| **High** | `H ≥ 2` |
| **Medium** | `M ≥ 4` AND `Total ≥ 4` |
| **Low** | `L ≥ 6` AND `Total ≥ 6` |

Papers failing all three are marked `FAIL` (recommended to cull).

---

## Step 3 – Density Score (Ranking)

For every passed paper, compute:

```
Density = (3×H + 2×M + 1×L) / Total
```

This rewards *signal-to-noise ratio*. A paper with 2H + 1M (8/3 = 2.67) beats a paper with 2H + 10L (16/12 = 1.33).

---

## Step 4 – Selection

1. Sort passed papers by **Density descending**.
2. Break ties by **H descending**, then **Year descending** (newest first).
3. Mark the top **50** papers as `Selected = TRUE`. (Threshold is configurable.)

---

## Configuration Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `HIGH_THRESHOLD` | 2 | Minimum H to pass |
| `MEDIUM_THRESHOLD` | 4 | Minimum M to pass (with Total ≥ 4) |
| `LOW_THRESHOLD` | 6 | Minimum L to pass (with Total ≥ 6) |
| `SELECTION_LIMIT` | 50 | Number of top passed papers to select |

---

## Output Format

The skill produces a single Markdown document containing:

### 1. Summary Statistics Block
```
Total Papers Scanned: 116
Passed Filter: 68
Failed Filter (Cull Recommended): 48
Selected Top 50: 50
```

### 2. Sorted Markdown Table

The table includes every paper, sorted by Density (highest first). Columns:

| # | Title | Year | Venue | H | M | L | Total | Pass | Density | Selected |
|---|-------|------|-------|---|---|---|-------|------|---------|----------|

- `Pass`: ✅ or ❌
- `Selected`: ✅ for top 50, ❌ otherwise

### 3. Recommended Culls List

A bulleted list of all failed papers, each with `(H:X, M:Y, L:Z, Total:T)`.

---

## Execution Command

> *"Parse the attached compilation file, run the relevance culler with default parameters, and output the summary statistics, full sorted table, and culling recommendations."*

---

## Edge Cases

| Case | Handling |
|------|----------|
| Only `contextual` topics | H=0, M=0, L=0, Total=0 → fails immediately. |
| 1 High + 0 Medium + 0 Low | Total=1 → fails (H<2, M<4, L<6). |
| 1 High + 5 Low | H=1, L=5, Total=6 → fails all conditions. |
| 5 Medium + 0 High | M=5, Total=5 → passes (M≥4). |
| Tie in Density | Sort by H descending, then Year descending. |

---

## Output Purity

- No emojis except ✅ / ❌ in the table.
- No prose outside the structured sections.
- The table is pure Markdown, ready to copy into a thesis appendix.