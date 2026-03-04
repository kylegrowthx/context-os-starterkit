# {Client Name} — Health Score Report

**Date:** {YYYY-MM-DD}
**Engagement Stage:** {SPRINT / NEW (X months GE) / ESTABLISHED (X months GE)}
**Pod:** {Pod name}
**EM:** {EM name} | **ME:** {ME name}
**Renewal:** {date} ({time until renewal})
**MRR:** ${amount}

---

## Scorecard

| Dimension | Agent Score | EM Score | Gap | Confidence | Justification |
|-----------|:----------:|:--------:|:---:|:----------:|---------------|
| Relationship | {1-5} | {1-5} | {+/-/—} | {H/M/L} | {1-2 sentences citing specific evidence} |
| Quantity | {1-5} | {1-5} | {+/-/—} | {H/M/L} | {1-2 sentences citing specific evidence} |
| Content Quality | {1-5} | {1-5} | {+/-/—} | {H/M/L} | {1-2 sentences citing specific evidence} |
| Performance/ROI | {1-5} | {1-5} | {+/-/—} | {H/M/L} | {1-2 sentences citing specific evidence} |
| Strategy | {1-5} | {1-5} | {+/-/—} | {H/M/L} | {1-2 sentences citing specific evidence} |

---

## Red Flags Detected

- [{Dimension}] {Red flag description} — {evidence source and date}

{If none: "No red flags detected this cycle."}

## Green Flags Detected

- [{Dimension}] {Green flag description} — {evidence source and date}

{If none: "No green flags detected this cycle."}

---

## Misalignment Analysis

{Only include if |Agent - EM| >= 2 on any dimension.}

**{Dimension}:** Agent scored {X}, EM scored {Y} (gap: {Z}). {Why scores diverge — what evidence does the agent see that the EM may be over/under-weighting?}

{If no gaps >= 2: "No significant misalignment detected. Agent and EM scores are within 1 point on all dimensions."}

---

## EM Effectiveness Assessment (Optional — include only if user requests EM evaluation or after v1 scoring is validated)

**Dimensions covered in recent calls:** {list}
**Dimensions missing from calls:** {list}
**Communication pattern:** {e.g., "Status-update-driven — covers delivery and quality but rarely probes on strategy or performance expectations"}
**Question quality:** {probing and exploratory, or checklist-style?}

---

## Action Triggers

{Only triggers hit per rubric. No recommendations.}

- {Dimension} score <= 2 → Director ticket warranted
- {Dimension} dropped >= 1 point from last cycle → Flag for director trend review
- Red Flag present in {Dimension} → Documented above

{If none: "No action triggers this cycle."}

---

## Data Gaps

- {What was missing — e.g., "No Fireflies transcripts found in last 6 weeks"}

{If none: "All primary data sources returned evidence."}

---

## Evidence Sources

| Source | Type | Date Range | Used For |
|--------|------|------------|----------|
| {source} | {type} | {range} | {dimensions} |
