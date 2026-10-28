# 08 · Data provenance, ethics and limitations

## Content origin
All messages are **synthetic** and were provided as an educational/business-simulation dataset. The original business case describes a customer support operations manager as stakeholder and a 240-message eight-category simulated triage process. The author performed manual labeling through Label Studio and exported the work. The supplied `reference_labels.csv` is a **provisional comparator**, not evidence of independently adjudicated gold labels.

## Historical changes and transparency
The folder `data/history` retains the first and intermediate user-supplied CSV snapshots and `data/raw` retains the final export. Original eight disagreements were corrected with the reference visible; later an accidental invoice change was caught and reverted. The casebook and playbook are **post-hoc explanatory artifacts**; they were not entered as review notes or confidence ratings during Label Studio annotation.

## Screenshots
Screenshot pixels depicting message text, category choices, and project counters were not altered. Only the account-identifier tab was masked in applicable screenshots. Source screenshot filenames are indexed in `assets/screenshots/SCREENSHOT_INDEX.csv`. The crop-scale screenshots are evidence of the annotation user interface, not evidence that a live customer-service routing system was deployed.

## What this project is **not**
- No production tickets, personal customer data, or customer-impact measurements.
- No machine learning model built, trained, scored or deployed.
- No independent inter-annotator assessment.
- No blind benchmark performance; the final 240/240 figure is **reference-aligned after review**.
- No stakeholder-signed taxonomy, confidence labels, or in-tool QA notes.

## Responsible next step
Before applying to real queues, obtain signed department definitions, source diverse new real-world examples with appropriate controls, sample blind second-review, add abstain/escalate options and measure a prospective pilot against a baseline.
