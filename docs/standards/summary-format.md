# RRL Summary Format

Reference for the structured YAML summary schema used in `RRL/02_Summaries/`.

Full prompt: `RRL/00_Proc/0_Summarizer.md`

## Schema

```yaml
paper_id: string        # DOI or UUIDv5, never null
designation: string     # "local" | "international" | "local-algorithm-specific" | "international-algorithm-specific"
title: string
authors: string         # "Last, F.; Last, F." or "Unknown"
year: integer
venue: string           # full name or "Unknown"
odin_topics:            # list of topic codes (max 20)
  - string
tldr: string            # one sentence, max 50 words, no "This paper" start
problem_and_motivation: string   # max 3 sentences, no methodology
approach:               # list of strings, each <=50 words, max 10
  - string
findings:               # list of strings. Use "num: " prefix for quantitative.
  - string
key_figures_tables:     # list of strings, each "Figure X: description -> takeaway"
  - string
key_equations:          # list of objects with "equation" and "explanation" fields
  - equation: string
    explanation: string # <=15 words
definitions:            # list of {term, definition}
  - term: string
    definition: string
critical_citations:     # list of strings, each "[Author, Year] -- reason"
  - string
relevance:
  topics:               # list of objects with code, name, relevance, justification
    - code: string
      name: string
      relevance: string  # "high" | "medium" | "low" | "contextual"
      justification: string
  contribution: string  # 3-5 sentences as a single string
  directly_justifies:   # list of strings, each a citable claim <=30 words
    - string
  limits:               # list of strings; if none, list contains "None identified."
    - string
  mapping_rationale: string  # paragraph describing the systematic scan across all domains
limitations:            # list of strings; use "[unacknowledged]" suffix if needed
  - string
remember_this:          # list of strings, each a key takeaway <=20 words
  - string
```

## Designation Decision Tree

1. Does the paper's primary contribution involve a specific algorithm, model, or computational technique?
   - **Yes**: proceed to step 2
   - **No**: proceed to step 3
2. Was the study conducted under a Philippine institution or uses Philippine data?
   - **Yes**: `local-algorithm-specific`
   - **No**: `international-algorithm-specific`
3. Is the paper authored under a Philippine institution or focused on the Philippines?
   - **Yes**: `local`
   - **No**: `international`

## Relevance Levels

| Level | Definition |
|-------|-----------|
| `high` | Directly addresses the core concern of the topic |
| `medium` | Provides supporting evidence or contextual example |
| `low` | Tangentially related, mentions topic in passing |
| `contextual` | Background framing only, no actionable insight |

## Field Rules

- `tldr`: One sentence, max 50 words. Never starts with "This paper" or "The authors."
- `problem_and_motivation`: Max 3 sentences. No methodology.
- `approach`: Each item <=50 words, ends with period. Max 10 items.
- `findings`: Prefix quantitative results with `"num: "`. Max 10 items.
- `remember_this`: 3-5 items, each <=20 words. No emojis, no numbering.
- `relevance.mapping_rationale`: Must explicitly state that all 13 topics were systematically scanned.
