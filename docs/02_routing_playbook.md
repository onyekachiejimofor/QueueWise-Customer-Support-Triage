# 02 · Primary-intent routing playbook

**Status: Proposed rubric derived from the reference and reviewed examples.** This is not an independently approved organizational policy. Classify the **next actionable request** rather than counting category keywords.

| Category | Typical next action | Includes | Excludes / competing cases |
|---|---|---|---|
| **Billing & Payment** | Investigate a charge, payment or invoice | Duplicate debit, failed checkout, erroneous invoice, receipt / tax invoice | An approved refund after a return, pre-sales accepted-payment-methods questions |
| **Refund & Return** | Start or manage return/refund | Return label, return eligibility, approved refund, refund status | Duplicate payment with no product return; pre-purchase general return policy per current rubric |
| **Delivery & Tracking** | Resolve shipping status or incident | Missing parcel, incorrect status, delayed shipment, shipment tracing | Shipping *charge* on invoice; general shipping availability; broken dashboard with working tracking |
| **Account Access** | Restore authentication or identity control | Verification trouble, sign-in recovery, account lockout, suspected account compromise | General app crash for logged-in user; cancellation when access already works |
| **Product Defect** | Investigate physical product failure | Broken hinge, leaking appliance, manufacturing damage | Explicit request for refund; warranty-duration information without a defect |
| **Subscription & Cancellation** | Modify ongoing membership or renewal | Cancel, stop auto-renewal, change plan, consequences of ending | General nonprofit pricing explanation; visibly unresponsive button under current project ownership rule |
| **Technical Issue** | Resolve broken software functionality | Crashes, frozen dashboard, broken import/export, unresponsive UI | Tracking status enquiry even if tracking website errors; sign-in recovery |
| **General Inquiry** | Provide information, especially prior to purchase | Product availability, store info, sales policies, generic pricing, opening hours | Disputed *actual* invoice, initiated return, active delivery incident |

## Decision rules — apply in order
1. Identify the customer's **requested action** and any explicit negation (“I am not asking for troubleshooting”).
2. If the customer needs an **immediate prerequisite** (e.g. log in before cancellation), route that prerequisite when clearly requested.
3. Distinguish **existing transaction/incident** from **hypothetical or pre-sale** informational enquiries.
4. For tech-related wording, ask: “Does the customer need system repair, or do they need the status/outcome behind the screen?”
5. For conflicting valid requests, use the higher-priority next action; mark genuinely simultaneous unrelated actions for manual split/escalation in a real deployment.
6. If organizational ownership is unapproved, record the **policy-dependent** boundary and obtain stakeholder decision rather than stating universal certainty.

## Important policy-dependent distinctions
- `SUP-0007` (cancel button missing) → Subscription; `SUP-0150` (button visible but inert) → Technical in this provided reference. Teams may reasonably assign both to Subscriptions unless ownership is formally decided.
- `SUP-0090` (qualifying item condition for a return) → Returns; `SUP-0122` (before-buying general return-policy scope) → General Inquiry. Business may direct both to Returns.
- `SUP-0233` nonprofit subscription pricing → General Inquiry in this exercise; another company may centralize such queries in subscription sales.
- `SUP-0182` tracking site error but requests status → Delivery; `SUP-0239` dashboard broken, tracking works → Technical.
- `SUP-0020` disputed monthly invoice → Billing, not a general subscription price request.

## Real deployment safeguards (not implemented here)
Provide a secondary-intent tag, uncertainty level, escalation option, and short rationale; blind double-label a quality sample; track the rubric version; allow agents to reassign tickets with reason codes.
