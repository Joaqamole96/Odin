## Instruction Set: Generating Self-Contained Search Prompts from a Topical Outline

### Purpose
Given a topical outline where each point has a parenthetical guiding question, produce a single self-contained search prompt for every point up to level 3. Each prompt should be ready to paste directly into Google Scholar or any academic database.

### Input
A hierarchical topical outline with:
- Level 1, level 2, and level 3 points
- Each point may or may not have a guiding question in parentheses
- Some points may have subpoints; some are leaf nodes without subpoints

### Output
For each outline point from level 1 to level 3, return:
- The point identifier and label
- The guiding question, if present
- A self-contained search prompt string

### Rules for Creating Search Prompts

1. **Use the guiding question as the primary basis.**
   - If a point has a question in parentheses, extract the key concepts from that question.
   - If no question is present, derive the key concepts from the point label and its immediate parent point.

2. **Do not include all ancestor terms.**
   - Use the immediate parent context plus one domain qualifier.
   - Do not chain every higher-level term into one query. Overly specific queries return too few results.

3. **Use Boolean operators to combine synonyms and related terms.**
   - Use `OR` for interchangeable terms inside parentheses.
   - Use `AND` to connect distinct concepts.
   - Use quotes for exact phrases when necessary.

4. **Keep the prompt concise and search-friendly.**
   - Aim for 1 to 4 conceptual blocks.
   - Avoid full sentences.
   - Avoid stopwords like "the", "a", "how", unless part of an exact phrase.

5. **Use academic terminology.**
   - Prefer terms commonly found in academic literature.
   - If the outline uses a non-standard term, translate it to a standard synonym before building the query.

6. **Preserve the point's own language where possible.**
   - If the point is specifically about "savings" or "debt", include those words.
   - If the point is about a model type such as "classification", include it.

7. **Do not add new concepts not present in the point or its immediate parent.**
   - The search prompt must reflect the outline point only.
   - Avoid adding general terms like "Philippines" unless the outline explicitly indicates a local focus.

8. **For leaf nodes, use the node label as a key phrase.**
   - Example: point "Age" under "Demographic and Household Profile" → query includes `"age" AND "savings" AND "debt"`.

### Step-by-Step Procedure

1. **Extract all outline points up to level 3.**
   - Level 1: `1`, `2`, `3`, etc.
   - Level 2: `1.1`, `1.2`, etc.
   - Level 3: `1.1.1`, `1.1.2`, etc.

2. **For each point, identify its guiding question.**
   - If present, parse the question for key concepts.
   - If absent, use the point label and its parent label to form key concepts.

3. **Identify the domain context from the immediate parent.**
   - Example: For `1.1.1 Demographic and Household Profile`, the parent is `1.1 Person` and the grandparent is `1 Improved Personal Savings & Debt`. Use only the parent `Person` plus the point's own key terms.

4. **Build the query using Boolean logic.**
   - Group synonyms or related terms inside parentheses with `OR`.
   - Join distinct concept groups with `AND`.
   - Use quotes for phrases like `"financial well-being"`.

5. **Ensure the prompt is self-contained.**
   - A user should be able to copy the prompt without any modification and get relevant results.
   - Test mentally: if pasted into Google Scholar, will it return papers related to this outline point?

6. **Return all prompts in a structured list.**

### Example

**Outline point:**
```
1.1.3 Social and Societal Factors
Question: How do social and societal factors affect savings and debt?
```

**Generated search prompt:**
```
("social influence" OR "parental socialization" OR "relative income") AND ("savings" OR "debt")
```

**Outline point (no question):**
```
1.3.4 Strategies of Repayment
```

**Generated search prompt:**
```
("debt repayment strategies" OR "snowball method" OR "avalanche method")
```

### Constraints
- Generate prompts only for levels 1, 2, and 3. Do not expand to deeper levels unless explicitly asked.
- Do not produce narrative explanations for each prompt. Only the prompt string is required.
- Do not include the outline text in the output; only the point identifier, label, question, and search prompt.
- If a point has no clear question and its label is too broad, use the label plus the immediate parent label as the core concepts.

### Final Output Format

```
[Point identifier] [Point label]
Question: [guiding question if present]
Search prompt: `[Boolean query string]`
```

Repeat this block for every outline point up to level 3.