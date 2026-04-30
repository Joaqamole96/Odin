# Guide to Writing a Narrative-Style Definition of Terms
### Standards, Reminders, and Lessons for Academic Research Papers

---

## What is a Narrative-Style Definition of Terms?

A narrative-style Definition of Terms presents each term as a **short, flowing prose definition** — not a dictionary entry, not a bulleted list, and not a copy-paste from Wikipedia. Each definition reads as a complete, purposeful sentence or set of sentences that tells the reader:

1. What the term means (conceptually or operationally)
2. How it functions within the context of *this specific study*

The goal is orientation, not exhaustion. The reader should finish each definition understanding exactly what the term means and why it matters to the paper — in under five sentences.

---

## The Two Types of Definitions

### Conceptual Definition
Draws from existing literature to establish what a term means in the broader field.
- Used for technical, scientific, or well-established academic concepts.
- **Requires a citation.**
- Example: defining what an LSTM network is according to existing machine learning literature.

### Operational Definition
Defines how *your study specifically* uses or applies the term.
- Used for system-specific concepts, locally coined terms, or when adapting a broader term to your context.
- **Does not require a citation.**
- Must be consistent with how the term appears throughout the rest of the paper.
- Example: defining what "Financial Behavioral Profile" means as constructed and used in Odin.

> **Lesson:** Most Definition of Terms sections use both types. Start with a brief conceptual grounding, then narrow it to how the term operates in your study. This two-step movement — from the field to your paper — is the hallmark of a well-written definition.

---

## Core Standards

### 1. Write in complete, connected sentences.
Avoid bullet points, dashes, or list formatting inside definitions. Each definition should read like a paragraph — even if it is only two or three sentences long. The narrative style signals academic maturity.

❌ **Wrong:**
> LSTM — a type of RNN. Used for forecasting. Has memory cells.

✅ **Right:**
> Long Short-Term Memory (LSTM) is a specialized class of recurrent neural networks designed to learn patterns across long sequences of data by selectively retaining and discarding information through a gating mechanism (Mroua & Lamine, 2023). In this study, LSTM serves as the spending forecasting model, trained on historical transaction data to predict future expenditures per expense category over weekly and monthly horizons.

---

### 2. Always close with the term's role in your study.
A definition that only explains the general concept is incomplete. Every definition must land with a sentence that anchors the term to your paper. Phrases like *"In this study..."*, *"As used in this paper..."*, or *"Within the context of Odin..."* are useful anchors.

---

### 3. Keep it concise — three to five sentences maximum.
The Definition of Terms is not the Review of Related Literature. It is a glossary, not an explanation. Do not discuss history, debate, or methodology here. Save depth for the appropriate chapter.

> **Reminder:** If you find yourself writing more than five sentences, you are writing a literature review entry, not a definition. Cut it down.

---

### 4. Do not define what does not need defining.
A term belongs in the Definition of Terms only if it meets at least one of the following criteria:

- It is **technical or specialized** (e.g., Isolation Forest, LSTM, anomaly detection)
- It is **culturally specific** and may be unfamiliar to an academic audience (e.g., *paluwagan*, *ambag*)
- It is **system-specific** — coined or adapted for use within your study (e.g., Financial Behavioral Profile, cold-start fallback)
- The paper's argument **depends on the reader understanding it correctly** before proceeding

Do not include terms that are self-explanatory to your target audience, terms that are so broad they resist a clean definition, or terms that only exist as informal descriptive language in the paper.

---

### 5. Cite conceptual definitions; do not cite operational ones.
If you are defining a term the way the field defines it, cite the source. If you are defining a term the way *your study* uses it, no citation is needed — but the definition must be original and precise.

> **Reminder:** Never cite a definition and then immediately contradict it with how you use the term. If your usage differs from the cited definition, acknowledge the distinction explicitly.

---

### 6. Arrange terms logically, not just alphabetically.
Alphabetical order is acceptable and common, but consider whether grouping related terms improves readability. For example, defining *Recurrent Neural Networks* before *Long Short-Term Memory* makes sense because LSTM is introduced as a subtype of RNN in the paper. Let conceptual hierarchy guide ordering where it matters.

---

### 7. Match the level of technicality to your audience.
Your Definition of Terms should be written for an intelligent reader who is *not* a specialist in your field. Avoid defining a technical term using other technical terms that are equally undefined. If you must use another specialized word inside a definition, either define that word in the same sentence or ensure it has its own entry.

---

### 8. Be consistent with the language used in the paper.
The exact wording of each definition should match how the term is used throughout the document. If your paper refers to "spending forecasting," do not define the term as "expenditure prediction." Inconsistency between the definition and the paper's language creates confusion and signals weak editorial control.

---

### 9. Filipino and cultural terms require cultural grounding, not just translation.
When defining culturally specific Filipino terms (e.g., *paluwagan*, *ambag*), do not simply translate them. Provide enough cultural context for a non-Filipino reader to understand the practice, its social role, and how it manifests financially. Then close with how it appears in the study.

❌ **Wrong:**
> Paluwagan is a Filipino savings system.

✅ **Right:**
> *Paluwagan* is an informal, community-based rotating savings arrangement practiced in the Philippines, in which a group of participants contributes a fixed amount of money at regular intervals and each member receives the pooled sum in turn (Flores, 2025). In this study, *paluwagan* is recognized as a distinct financial obligation category within Odin's expense structure, reflecting its prevalence among Filipino young professionals as a culturally embedded saving and lending mechanism.

---

### 10. Do not duplicate what belongs in other sections.
The Definition of Terms establishes meaning — it does not evaluate, compare, justify, or discuss. Do not include:
- Arguments for why a technology was chosen
- Comparative analysis of similar tools or methods
- Historical background longer than one sentence
- Findings from other studies

All of that belongs in the Review of Related Literature or the methodology discussion.

---

## Common Mistakes to Avoid

| Mistake | Why It's a Problem |
|---|---|
| Copying a definition verbatim from a source | This is plagiarism if uncited; even if cited, it shows a lack of synthesis. Always rewrite in your own words. |
| Writing definitions that are too general | A definition of "machine learning" that doesn't connect to your study wastes the reader's time. |
| Omitting the operational anchor | Without "as used in this study," the reader doesn't know how the term functions in your specific paper. |
| Including too many terms | An overloaded Definition of Terms loses focus. Only include terms that genuinely need defining for your paper to be understood. |
| Defining abbreviations without spelling them out first | Always write the full term first, followed by the abbreviation in parentheses, on first use. |
| Using the definition section to review literature | Save analysis and comparison for RRL. Definitions are short and declarative. |

---

## A Practical Template

Use this as a structural guide, not a fill-in-the-blank formula:

```
[Term] [is / refers to / describes] [conceptual definition in your own words] 
([citation if conceptual]). [Optional: one sentence of additional context if needed.] 
In this study, [term] [is used to / refers specifically to / operates as] [operational role in your paper].
```

**Example using the template:**

> Anomaly detection refers to the computational process of identifying data points that deviate significantly from an established pattern or baseline within a dataset (Kumari & Kumar, 2024). In this study, anomaly detection is performed by the Isolation Forest algorithm, which flags individual financial transactions that fall outside a user's established spending behavior and surfaces them as alerts within the Odin system.

---

## Quick Checklist Before Finalizing Each Definition

- [ ] Is it written in complete, narrative prose — no bullets or fragments?
- [ ] Does it define the term in general terms first (if conceptual)?
- [ ] Does it close with how the term is used *in this study specifically*?
- [ ] Is it five sentences or fewer?
- [ ] Is it cited if it draws from literature, and uncited if it is operational?
- [ ] Is the language consistent with how the term appears in the rest of the paper?
- [ ] Is it free of arguments, comparisons, or RRL-type content?
- [ ] Would a non-specialist reader understand it without needing to look elsewhere?
