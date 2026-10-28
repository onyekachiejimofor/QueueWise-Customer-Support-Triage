# Operational story: support ticket triage
**Stakeholder:** customer support operations manager.
**Input:** 240 synthetic messages, 8 routing categories, 48 deliberately hard/multi-intent cases.
**Output:** a consistent routing taxonomy and an evaluated set of human labels.

### What this solves
Under manual routing, a billing complaint with a delivery reference can land at Logistics; a login problem may be sent to Technical Support. The primary-intent rules reduce ambiguity in *how humans should label the same request*.

### Proposed operational metrics (not results)
- Top-1 category accuracy vs an independently adjudicated reference;
- Macro F1 so minority or difficult categories do not disappear in aggregate accuracy;
- misrouting/confusion between specific department pairs;
- label-completion rate, abstention/escalation rate, QA disagreement rate;
- eventual live business KPI: median time-to-correct-team and avoidable transfer rate (requires actual operations data).

### Decision scenario
If many `Account Access` messages are labeled `Technical Issue`, change the routing playbook and support macros to ask about authentication before debugging the general app.

### Ethical and validity boundaries
No live service KPI improvement can be claimed from synthetic messages. The reference is provisional and must be reviewed independently before it is treated as ground truth.
