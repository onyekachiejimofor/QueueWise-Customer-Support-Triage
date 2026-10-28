# 01 · The business case

**Stakeholder:** E-commerce customer-support operations manager. **Situation:** Incoming support tickets may mention multiple departments; correct first-team ownership should follow a consistent set of decisions. **Input:** 240 **synthetic** tickets; 8 intended support categories; 48 designed difficult cases. **Output:** A reproducible labeled dataset, casebook, revision audit, and a proposed routing playbook.

## Problem statement
Misrouting has plausible operational costs: avoidable reassignment, unclear case ownership and delay. For example a complaint about an incorrect delivery *charge* belongs to billing, whereas a missing package belongs to logistics. A customer locked out while trying to cancel needs access support before cancellation can proceed.

## Proposed outcome
Establish understandable human annotations that a support manager can inspect and approve for future routing or AI evaluation. This project **does not** test a live contact center or quantify customer savings.

## Scope decisions
- Single-label classification: one primary category per ticket, not multilabel incident tagging.
- Designed balanced category representation (30 examples per category in the reference), deliberately unlike many real queues.
- Each record has an identifier, message, manually selected label, and a provisional reference provided with the exercise.
- Categories and precedence depend on ownership conventions; this study documents those as **proposed guidance**, not a confirmed company policy.

## Why this is a real operational problem
Support teams often require explicit intake definitions, not merely keyword matching. The artifact is a controlled simulation of how that decision-making could be organized and checked. Real impact depends on future production testing.
