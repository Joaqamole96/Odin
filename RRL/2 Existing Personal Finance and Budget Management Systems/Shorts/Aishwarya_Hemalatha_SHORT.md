---
name: research-summary
source_document: "Aishwarya_Hemalatha.md"
designation: algorithm-specific
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
summary_date: 2026-04-24
version: "1.0"
---

# Smart Expense Tracking System Using Machine Learning

## TL;DR (One Sentence)
Machine learning automates expense tracking, achieving high classification accuracy and providing personalized spending insights.

## Core Problem & Motivation
Manual expense tracking (spreadsheets, receipts) is time‑consuming and error‑prone, offering little actionable insight. The study explores using ML to predict expenses, visualize patterns, and help users save money.

## Methods / Approach (Bulleted)
- Collect data from bank transactions, credit cards, and user input.
- Preprocess data: clean, normalize, extract features (category, merchant, date/time).
- Train supervised (decision trees, neural nets) and unsupervised (clustering) models.
- Use cross‑validation (k‑fold) and ensemble methods (bagging/boosting) to prevent overfitting.
- Deploy via cloud platform (AWS/Azure) with API endpoints.

## Key Findings / Results (Numbered or Bulleted)
1. ML model accuracy is **significantly higher** than rule‑based or manual classification (placeholder `X%` on validation set).
2. Users receive personalized recommendations (e.g., top spending categories, savings tips).
3. System scales to large datasets with stable response times.
4. High user satisfaction: easy to use, helps understand finances.
5. Occasional errors require manual correction, especially for unique categories.

## Important Figures & Tables (Condensed)
- Figure 1: Expense percentage comparison → Shows relative spending across categories (no exact values given).

## Equations to Remember
None.

## Definitions & Acronyms
| Term/Acronym | Definition |
|--------------|------------|
| ML | Machine Learning |
| API | Application Programming Interface (automates data collection) |
| PCA | Principal Component Analysis (reduces feature dimensions) |
| LSTM | Long Short‑Term Memory (a deep learning network for sequences) |
| TF‑IDF | Term Frequency‑Inverse Document Frequency (extracts text features) |

## Critical Citations
- [Al‑Natour et al., 2018] – First to propose ML for automated expense tracking.
- [Li et al., 2019] – Applied deep learning (LSTM) to receipt categorization.
- [Hahsler & Grün, 2018] – Compared eight software packages for text classification in finance.

## Limitations & Assumptions
- Accuracy depends on data quality (missing merchant names, vague descriptions).
- Privacy concerns when collecting bank/credit card data.
- May misclassify region‑specific or culturally unique expense categories.
- Requires periodic retraining to adapt to changing spending habits.

## Takeaway for Memory (≤ 3 bullet points)
- 🔑 **ML beats manual tracking** – higher accuracy, less effort, real‑time insights.
- 💡 **Personalized feedback saves money** – system flags top categories and suggests cuts.
- 📌 **Watch data quality** – missing info leads to errors (like a blurry photo).