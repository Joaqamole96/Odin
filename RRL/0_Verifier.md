# Skill Document: Compilation Paper Verification

## Objective
Verify that **every paper** in a compiled research summary meets all criteria for the compilation's assigned designation (one of: `local`, `local-algorithm-specific`, `international`, `international-algorithm-specific`). Output must be brief, symbol‑based, and actionable – **listing only invalid papers** in outline format.

## Global Requirements (All Papers)
1. **Year** – Must be **2023 or later**.  
   - `year: 0` or missing → **Invalid**.
2. **Paper ID** – Must be present.  
   - **Valid:** DOI (starts with `10.`) or a plausible unique hash (UUID, hex).  
   - **Flagged:** Missing, empty, `"N/A"`, `"None"`, `"0"`.  
   - *Hash IDs are accepted but will be flagged for manual DOI replacement.*
3. **Core Fields** – Must be present and non‑empty: `title`, `authors`, `year`, `tldr`, `approach`, `findings`.  
   - Missing or placeholder (`"None."`) → **Flag as incomplete**.

## Designation Criteria
Determine **Locality** and **Algorithm‑specific** status for each paper, then compare against the compilation's designation:

| Compilation Designation | Local Required? | Algorithm Required? |
| :--- | :---: | :---: |
| `local` | ✅ Yes | ❌ No |
| `local-algorithm-specific` | ✅ Yes | ✅ Yes |
| `international` | ❌ No | ❌ No |
| `international-algorithm-specific` | ❌ No | ✅ Yes |

**Locality** – True if:
- Uses Philippine data (FIES, LFS, PH universities, local companies), OR
- Focuses on Philippine context/demographics (Filipino workers, BPO, PH policies, etc.).  
False if: uses foreign data (US Census, Kaggle, China, India, Hong Kong), global lit review, or only mentions PH stats without analysis.

**Algorithm‑specific** – True if:
- Implements ML/DL models (RF, XGBoost, ANN, LSTM, etc.), OR
- Uses statistical/econometric models with clear implementation (GAM, RIF, PSO, MILP), OR
- Uses rule‑based or clustering algorithms (C4.5, k‑means).  
False if: only basic tests (Spearman, t‑test) or purely conceptual/DiD design without model estimation.

## Process Steps
1. Check **year** – fail if < 2023 or 0.
2. Check **paper_id** – fail if missing; flag if hash (for later DOI replacement).
3. Check **core fields** – fail if missing/empty.
4. Determine **Local?** – yes/no with justification.
5. Determine **Algo?** – yes/no with justification.
6. Compare against compilation designation – if mismatch, fail.
7. Output **only invalid papers** with brief reasons.

## Output Format
List **only invalid papers** in a bulleted outline, using consistent symbols:

```md
## Invalid Papers

- [#] Author et al. (Year)
  - Year: ❌ [reason, e.g., <2023, year=0]
  - ID: ❌ [reason, e.g., missing, hash, N/A]
  - Fields: ❌ [reason, e.g., missing TLDR]
  - Local: ❌ [reason, e.g., US dataset]
  - Algo: ❌ [reason, e.g., only Spearman]
  - Designation: ❌ [reason, e.g., should be local but is not]

- [#] ...
```

For each invalid paper, include **only the checks that failed**. If a check passes, omit it.

At the end, provide a summary:

```md
**Summary:**
- Valid: X papers
- Invalid: Y papers
```

## Example Output

```md
## Invalid Papers

- [2] Espiritu (2026)
  - Algo: ❌ only Spearman correlation

- [3] Laspinas & Murcia (2024)
  - Local: ❌ US Census dataset

- [4] Salvador (2022)
  - Year: ❌ pre-2023

- [7] Zhang & Duan (2025)
  - Local: ❌ Chinese CSMAR data
  - ID: ⚠️ hash – replace with DOI

**Summary:**
- Valid: 3
- Invalid: 4
```