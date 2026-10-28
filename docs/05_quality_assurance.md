# 05 · Quality audit & interpretation

## What was checked

Three submitted time-ordered CSV snapshots were compared on `task_id` to the project tasks and supplied provisional reference. The final source is `project-8-at-2026-10-28-13-38-9b8699ed.csv`. Source file checks cover completeness, unique IDs, class validity, exact text and repeat-pair consistency.

| Audit cohort | Tasks | Initial matches | Intermediate matches | Final matches |
|---|---:|---:|---:|---:|
| All | 240 | 232 | 239 | 240 |
| Standard | 192 | 188 | 191 | 192 |
| Designed boundary / multi-intent | 48 | 44 | 48 | 48 |

## Exact revision explanation

**Initial export:** 232 of 240 matched the provisional reference; eight differences involved mainly General Inquiry versus topic-specific queues, plus a broken cancellation control.

**First revised export:** the original eight mismatches were aligned to reference classifications. A separate ticket, **SUP-0020**, was inadvertently changed from **Billing & Payment** to **General Inquiry**, even though its text disputes a higher-than-agreed invoice. This produced 239 of 240 reference matches and a greeting-variant inconsistency with SUP-0051.

**Final revised export:** SUP-0020 was restored to **Billing & Payment**. Now 240 of 240 matches the provisional reference. Across snapshots, **10 category-change events** occurred on **9 distinct task IDs**; comparing initial directly to final, **8 task IDs have different labels**. The history is shown in `reports/revision_history.csv`.

> This process used the supplied reference for feedback. The final concordance **cannot** be called blind classification accuracy, independent QA agreement, trained-model accuracy or proof that ambiguous policies were independently adjudicated.

## Data-integrity checks

- 240 unique task IDs, 240 unique annotation IDs; one category per ticket; all eight categories are represented.
- Source/annotation/reference messages match byte-for-byte after CSV parsing; no missing text.
- Balanced categories: exactly 30 final labels for each of eight classes (by project design).
- 96 two-message pairs differ by an introductory greeting; **all 96 are consistent in the final export**.
- Total *normalized* distinct message forms: 144; not 240 independent cases.
- Confidence and review-note fields are blank in exports; do not claim calibrated confidence or authored Label Studio review notes.

## Methodological limitations

- **No blind second reviewer**: the provisional reference was known during correction. Inter-annotator agreement (such as Cohen's kappa) was not measured.
- **No independent evaluation set**: after reference-directed revision, 100% agreement is procedural reference conformance, not estimated generalization performance.
- **No live customers**: all messages are synthetic; a production routing rate, handling time or cost savings cannot be claimed.
- **Balance and repetition**: 30 items per class and 96 greeting pairs are not representative of real-world class frequencies or language diversity.
- **Open policy questions**: button failure vs cancellation ownership, returns-policy inquiries and nonprofit plan prices need stakeholder adjudication.

## How to strengthen the next version

1. Obtain category-ownership approval from Billing, Returns, Technical, Logistics and Subscription support managers.
2. Blind-label a fresh representative sample from a different annotator and log disagreement rationales.
3. Record confidence, a secondary category if needed, and an escalation decision for truly multi-intent tickets.
4. Test on new messages rather than repeating source examples.
5. If used operationally, monitor first-team routing, avoidable transfers and resolution time on genuine tickets against a baseline.

**Reproduce:** `python scripts/verify_dataset.py`, no dependencies.
