# 07 · Data dictionary

## Files to open first
- `data/processed/final_labeled_tickets.csv` — easy-to-read final 240-record register.
- `data/raw/label_studio_export_FINAL.csv` — exact latest human Label Studio CSV export (selected labels and metadata).
- `data/history/01_initial_export.csv` — original export for pre-review comparison.
- `data/history/02_first_revision_export.csv` — intermediate snapshot exposing the temporary SUP-0020 mistake.
- `data/source/annotation_tasks.csv` — original messages and blank data-entry fields.
- `data/source/reference_labels.csv` — provisional reference category, routing team, dataset difficulty and supplied rationale.
- `reports/revision_history.csv` — category changes between snapshots, with **no independent adjudication claimed**.
- `reports/edge_case_decision_register.csv` — exact task text, final label, competing label and case rationale.
- `reports/review_progress.csv` — match counts before/after reference-guided review.
- `reports/greeting_variant_consistency.csv` — pair-level repeat-consistency test.
- `reports/qa_summary.json` — machine-readable audit headline metrics.

## Final data columns
| Column | Meaning |
|---|---|
| `task_id` | Stable support-ticket key (`SUP-0001` ... `SUP-0240`) |
| `message` | Synthetic input text; original content unchanged |
| `final_label` | The last exported human primary label |
| `provisional_reference_label` | Reference supplied with the exercise |
| `reference_match` | Final selected vs supplied reference equality (not a gold accuracy claim) |
| `dataset_difficulty` | `Standard` or `Boundary / multi-intent`, as marked by dataset author |
| `proposed_queue` | Routing-team name from supplied reference |
| `label_studio_record_id` | Internal Label Studio task record number |
| `annotation_id` | Label Studio annotation ID |

The final CSV deliberately does not present missing confidence/review notes as completed work. `lead_time` and timestamps are in the raw export, but they are not reliable productivity or duration KPIs in this case study (later edits may affect their meaning).
