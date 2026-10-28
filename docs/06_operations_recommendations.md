# 06 · Decision brief for the support operations manager

## Proposed operating decision
Use the eight-queue taxonomy as a **draft routing playbook**, not as an auto-router. First approve ambiguous ownership and then test a small human-reviewed pilot on **real, consent-appropriate** tickets.

### Priority 1 — Clarify pre-sale vs active incident routing
**Observed from the initial audit:** most provisional-reference disagreements came from questions about available payment methods, shipping locations, pricing, and general return policy. **Proposed action:** define which informational questions go to General Inquiry versus specialist queues. **Owner:** Operations lead. **Measure later:** blind label disagreement on new pre-sale messages.

### Priority 2 — Clarify broken-control vs customer-outcome routing
**Observed example:** `SUP-0150` describes a non-responsive cancellation button, while `SUP-0240` asks to cancel an otherwise functioning membership. **Proposed action:** specify first ownership for broken UI controls and cross-team handoffs for time-sensitive cancellation. **Owners:** Subscription + Technical leads. **Measure later:** transfers and turnaround on failed-cancellation cases.

### Priority 3 — Add escalation criteria for genuine multi-intent tickets
**Observed examples:** billing vs return refund and shipment status vs tracking website errors. **Proposed action:** one primary queue plus secondary-intent and escalation fields. **Owner:** QA lead. **Measure later:** reclassification rates and unresolved mixed-intent tickets.

### Priority 4 — Create independent evaluation, then operational trial
**Limitation:** the current synthetic reference-guided data cannot measure real accuracy. **Proposed action:** independently label a new diverse sample, approve gold decisions with adjudication, and only then pilot routing assistance. **Owner:** QA + Support Operations. **Potential KPIs:** first-team routing accuracy, median time to correct queue, avoidable transfers, disagreement rate, customer resolution time. No benefit has been quantified here.

## Suggested implementation gate

- Gate A: Policy definitions approved by departmental owners.
- Gate B: Blind, representative second-pass labeling completed.
- Gate C: Quality threshold chosen *before* reviewing pilot outcomes.
- Gate D: Routing human oversight, manual correction, and audit trail implemented.
- Gate E: Measure pilot vs existing process on comparable live tickets.

**Deliverable status:** recommendations only. No production workflow was configured.
