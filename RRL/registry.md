# Registry of Papers

> **Usage**:
> One row per paper. Add a row after Step 6 of the pipeline (after the summary is complete and you have read it).
> Update the **Tally** row at the bottom whenever a row is added or a designation changes.
> Search the `topics` or `shorthand_tags` columns to find papers for a specific topic.
> `paper_id` links directly to `Papers/<paper_id>.md` and `Papers/<paper_id>-summary.md`.

---

## Source Quota Status

| Designation | Count | Target | Remaining |
| :--- | :---: | :---: | :---: |
| `local` | 0 | 25 | 25 |
| `international` | 0 | 25 | 25 |
| `algorithm-specific` | 0 | -- | -- |
| **Total** | **0** | **50** | **50** |

---

## Paper Registry

| paper_id | desig. | year | authors | title | venue | topics | shorthand_tags | checklist | notes |
| :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| 10.62986/dp2024.10 | local | 2024 | Albert, J. R. G.; Briones, R. M.; Rivera, J. P. R. | Wealth Creation for Expanding the Middle Class in the Philippines | Philippine Institute for Development Studies Discussion Paper Series | [1, 2, 4, 5, 7, 9, 11, 12] | [shorthand_tags] | [checklist] | [notes] |
| [paper_id] | [desig.] | [year] | [authors] | [title] | [venue] | [topics] | [shorthand_tags] | [checklist] | [notes] |

---

## Column Reference

| Column | Format | Source | Description |
| :--- | :--- | :--- | :--- |
| `paper_id` | DOI, with `/` becoming `_`, or UUID v4 | converter YAML `paper_id` | Permanent identifier. Links to both files in `Papers/`. |
| `desig.` | `local` / `intl` / `algo` | converter YAML `designation` | Abbreviated designation. `algo` = algorithm-specific. |
| `year` | YYYY | converter YAML `year` | Publication year. Must be 2023–2026 unless exempted. |
| `authors` | Last, F.; Last, F. | converter YAML `authors` | First two authors. Append "et al." if more than two. |
| `title` | plain text | converter YAML `title` | Exact title, truncated at 60 chars with `…` if needed. |
| `venue` | plain text | converter YAML `venue` | Full journal or conference name. |
| `topics` | comma-separated integers | summarizer YAML `odin_topics` | Topic numbers this paper supports. See topic table below. |
| `shorthand_tags` | comma-separated `/tags` | manual, from outline | Specific `[/shorthand]` nodes from `topic-outline.md`. |
| `checklist` | "Gabion: [], Guevarra: [], San Jose: [], Togle: []" with ✓ | summarizer YAML `member_checklist` | ✓ = member has read the summary. |
| `notes` | one line | manual | Primary contribution of this paper to Odin's RRL in ≤50 words. |

---

## Topic Reference

| # | Topic | Outline Node |
| :---: | :--- | :---: |
| 1 | Spending and Budgeting Behavior of Filipino Young Professionals | A.1 |
| 2 | Existing Personal Finance and Budget Management Systems | A.2 |
| 3 | Mobile-First Design in Personal Finance Systems | B.1 |
| 4 | Budgeting Strategies and Budget Recommendation | C.1 |
| 5 | Budget Recommendation Algorithm | C.2 |
| 6 | Predictive Modeling in Personal Finance Systems | D.1 |
| 7 | LSTM as the Spending Forecasting Algorithm | D.2 |
| 8 | Anomaly Detection in Personal Finance Systems | E.1 |
| 9 | Anomaly Detection Algorithm | E.2 |
| 10 | User Behavioral Profiling in Filipino Personal Finance Contexts | F.1 |
| 11 | Profile Classification Algorithm | F.2 |
| 12 | Expense Categorization in Filipino Personal Finance Contexts | G.1 |
| 13 | Data Privacy, Security, and User Trust in Personal Finance Systems | H.1 |
| 14 | User Retention and Engagement in Personal Finance Systems | I.1 |
| 15 | System Evaluation | J.1 |

---

## Designation Rules (Quick Reference)

Apply in priority order — stop at first match:

1. **`algorithm-specific` (algo)** — The paper primarily describes an algorithm, model, or computational method. Overrides local/international regardless of origin.
2. **`local`** — Published in or by a Philippine institution. Not algorithm-specific.
3. **`international` (intl)** — Published outside the Philippines. Not algorithm-specific.

---

## Recency Exceptions

All sources must be 2023–2026, except:

| Exception type | Rule |
| :--- | :--- |
| Laws and statutes | Any year. Cite by Republic Act number. |
| ISO standards | Any year. Always include edition year (e.g., ISO/IEC 25010:2023). |

---
