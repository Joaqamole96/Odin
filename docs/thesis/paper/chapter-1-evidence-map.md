# Chapter 1 – Evidence Map (Claim → Citation → Finding)

Audit companion to `chapter-1.md` (Draft V2.1). Purpose: let the adviser and the team verify that **every citation placed in Chapter 1 is aligned with the new scope and is genuinely supported by the cited source**, and to track which claims still need `VERIFY` work.

## Policy

- Citation pool is **only** the curated intake in `Odin-Literature/literature/papers/` (17 PDFs) plus the study's own PUEPS instrument.
- APA 7th edition.
- **No-stretch rule:** a claim is cited only if the source directly supports it. Claims without direct support remain uncited and are flagged with `<!-- VERIFY: ... -->`.
- No V2.0 citation was reused as verified.

## Source key (curated intake)

| Key (as cited) | PDF | Venue / Year |
|---|---|---|
| Abdullahi et al., 2025 | `Abdullahi et al., 2025.pdf` | IEEE Access, 2025 |
| Abila & Ulibas, 2026 | `Abila & Ulibas, 2026.pdf` | IJMERI, 2026 |
| A. Huang et al., 2025 | `A. Huang et al., 2025.pdf` | Journal of Global Information Management, 2025 |
| Bangko Sentral ng Pilipinas, 2026 | `Bangko Sentral ng Pilipinas, 2026.pdf` | BSP CES, 2Q 2026 |
| Chen & Tan, 2025 | `S. Chen & Tan, 2025.pdf` | DECS, 2025 |
| Chen et al., 2024 | `J. Chen et al., 2024.pdf` | Journal of Basic and Applied Research International, 2024 |
| Danahy et al., 2024 | `Danahy et al., 2024.pdf` | Journal of Consumer Affairs, 2024 |
| El Hajj & Hammoud, 2023 | `Hajj & Hammoud, 2023.pdf` | Journal of Risk and Financial Management, 2023 |
| Ganong et al., 2025 | `Ganong et al., 2025.pdf` | NBER WP 34227, 2025 |
| Hu et al., 2023 | `Hu et al., 2023.pdf` | NeurIPS 2023 |
| R. Huang et al., 2025 | `R. Huang et al., 2025.pdf` | GAIB, 2025 |
| Wang-Ly & Newell, 2023 | `Wang-Ly & Newell, 2023.pdf` | SSRN 4509925, 2023 |
| Yadav et al., 2026 | `Yadav et al, 2026.pdf` | ISJEM 5(4), 2026 |
| Yeo et al., 2023 | `Yeo et al., 2023.pdf` | Journal of Financial Services Marketing, 2023 (print 2024) |
| Yoganandham, 2025 | `Yoganandham, 2025.pdf` | Degres Journal, 2025 |
| PUEPS, 2026 | (own instrument) `Odin-Paper/docs/assessment-evaluation/survey/PUEPS.md` | 2026 |

Not cited from the intake (kept out per the no-stretch rule): `Andresen et al., 2025.pdf` (household pooling), `Rane et al., 2024.pdf` (AI acceptance). Neither has a claim in the current draft that they directly support; re-evaluate later if a fitting claim emerges.

## Claim-by-claim mapping

### I. Introduction

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 1 | I-P1 | PFM evolved from manual methods to a digital discipline of budgeting apps and finance software | (El Hajj & Hammoud, 2023; Yadav et al., 2026) | El Hajj & Hammoud: AI/ML transforming financial operations; Yadav et al.: fintech/AI paradigm change in personal finance management | None |
| 2 | I-P2 | Many individuals find financial management difficult; tracking challenges | `<!-- VERIFY -->` (no citation) | — | Support via PUEPS findings or a published study; do not force a citation |
| 3 | I-P2 | Unmaintained budgets → struggle to save, reliance on debt, financial vulnerability and stress | (Danahy et al., 2024; Ganong et al., 2025; Wang-Ly & Newell, 2023) | Danahy: debt + lack of emergency savings → financial stress; Ganong: earnings instability → financial fragility; Wang-Ly & Newell: income volatility affects saving decisions | None |
| 4 | I-P3 | Mobile apps consolidate financial info, automate tracking, present summaries | (Yadav et al., 2026) | Yadav et al.: IPFMS aggregates transactions, real-time snapshot, predictive budgeting recommendations | None |
| 5 | I-P3 | ML estimates future expenses / flags unusual transactions | (Chen et al., 2024; Chen & Tan, 2025; A. Huang et al., 2025) | Chen et al.: deep-learning time-series forecasting survey; Chen & Tan: behavior prediction from historical behavior; A. Huang: threshold calibration for financial anomaly detection | None |
| 6 | I-P4 | Savings as buffer; poorly managed debt → income loss, stress, fewer opportunities | (Danahy et al., 2024; Yeo et al., 2023; Yoganandham, 2025) | Danahy: emergency savings buffer; Yeo: planning behaviour → resilience; Yoganandham: budgeting/savings/debt → long-term stability | None |
| 7 | I-P4 | Many Filipino workers struggle to save while servicing obligations | (Abila & Ulibas, 2026) + `<!-- VERIFY -->` | Abila & Ulibas: Filipino freelancers' savings/resilience amid obligations and income volatility | **Citation covers online freelancers in Laguna only** — generalizability to "many Filipino working individuals" needs BSP CES 2026 or PUEPS confirmation |
| 8 | I-P5 | Need for personalized intelligent PFM for Filipinos | (R. Huang et al., 2025; Yadav et al., 2026) | R. Huang: personalized intelligent wealth management; Yadav: intelligent PFM tailored to behavior and goals | None |

### II. Project Context

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 9 | II-P1 | NCR young adults manage finances manually (notebooks, sheets, mental tracking) | `<!-- VERIFY -->` (no citation) | — | Incidence from PUEPS; no corpus source measures this prevalence directly |
| 10 | II-P1 | Informal practices (paluwagan, ambag, family support, gov contributions) | `<!-- VERIFY -->` (no citation) | — | Confirm against BSP CES 2026 / PUEPS findings |
| 11 | II-P1 | Generic apps (Western-style, single-account) don't fit local income/expense patterns | (Abila & Ulibas, 2026; Bangko Sentral ng Pilipinas, 2026) + `<!-- VERIFY -->` | Abila & Ulibas: local practices/pressures (VAT, income volatility); BSP: NCR consumer expectations/conditions | Generalization beyond cited samples — verify |
| 12 | II-P2 | PUEPS as preliminary investigation; difficulties identified | (Budi Public User Expectations and Perception Survey, 2026) + `<!-- VERIFY -->` | Own survey instrument (constructs for spending monitoring, localization, insights, privacy) | **Findings file not located** — no response figures yet |
| 13 | II-P3 | Tension between debt repayment and savings → deferred savings / debt accumulation | (Danahy et al., 2024) + `<!-- VERIFY -->` | Danahy: debt vs emergency savings tension and stress | Generalization beyond college-debt findings |
| 14 | II-P3 | Accumulated conditions reduce financial resilience and goal pursuit | (Ganong et al., 2025; Wang-Ly & Newell, 2023; Yeo et al., 2023) | Volatility/instability → fragility and impaired saving; planning behaviour → resilience | None |
| 15 | II-P4 | BUDI feature set mirrors intelligent PFM precedents | (R. Huang et al., 2025; Yadav et al., 2026) | Intelligent PFM features: dashboard, tracking, predictive budgeting, personalized guidance | None |
| 16 | II-P5 | Model families: forecast / optimize / anomaly detect | (Chen et al., 2024; Hu et al., 2023; A. Huang et al., 2025) | Chen et al.: forecasting; Hu et al.: predict+optimize with constraints; A. Huang: anomaly detection thresholds | None |
| 17 | II-P5 | Models must stay reliable as user behavior evolves | (Abdullahi et al., 2025) + `<!-- VERIFY -->` | Abdullahi: concept drift degrades time-series/classification model performance | Applicability of concept-drift findings to personal-finance profile classification — verify |

### III. Purpose and Description of the Study

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 18 | III-P3 | Forecasting from chronological history; optimization with constraints; anomaly vs baseline | (Chen et al., 2024; Chen & Tan, 2025; Hu et al., 2023; A. Huang et al., 2025) | Same method-family support as #16 | None |
| 19 | III-P4 | Alignment with UN SDG 1 & 8 | (no citation) + `<!-- VERIFY -->` | — | Confirm claim alignment against the UN SDG framework wording |

### IV. Scope and Limitations

| # | Location | Claim (abridged) | In-text citation | What the source supports | Residual verify |
|---|---|---|---|---|---|
| 20 | IV-P1 | NCR young adults face obligations, savings, debt concerns | (Bangko Sentral ng Pilipinas, 2026) + `<!-- VERIFY -->` | BSP CES 2Q 2026: NCR + national consumer expectations | Specific NCR figures — cite exact DI/percentage when using a number |
| 21 | IV-P3 | Final model selection by evaluation metrics etc. | (no citation; `<!-- VERIFY -->` removed) | — | Self-authored methodology — no external claim, citation not required |
| 22 | IV-P4 | Public PH datasets are household-level/aggregate | (Bangko Sentral ng Pilipinas, 2026) + PSA `<!-- VERIFY -->` | BSP CES as an aggregate household survey example | PSA FIES: confirm exact dataset years and access date (source not in curated intake) |
| 23 | IV-P4 | Savings/debt features subject to PUEPS validation | (Budi Public User Expectations and Perception Survey, 2026) + `<!-- VERIFY -->` | Own instrument | Findings pending |

### V. Operational Definition of Terms

No citations required (terms defined operationally for this study).

## Open items for the team

1. **PUEPS results file** — locate and fill in response figures; until then all PUEPS-based incidence claims stay `<!-- VERIFY -->`.
2. **PSA FIES** — add a verified reference (official report) and exact years, or keep it a named data source only.
3. **BSP CES 2Q 2026** — pull the specific diffusion-index figures (NCR vs national) to underpin any numeric claim.
4. **Generalization flags** (#7, #11, #13, #17) — decide whether the citation stands as qualitative support with a qualifying clause, or whether a stronger source is needed.
5. **Andresen et al. (2025)** and **Rane et al. (2024)** are in the intake but uncited; confirm whether they are reserved for Chapters 2–3.