# Rules

## What This Skill Produces
- Numerical health scores (1-5) per dimension with evidence justifications
- Agent vs. EM score comparison with gap analysis
- Misalignment flags (gap >= 2)
- Red/green flag detection per dimension
- EM effectiveness assessment from call transcripts
- Action trigger flags (rubric thresholds hit)
- Confidence qualifiers (H/M/L) and data gap documentation

## What This Skill Does NOT Produce
- Narrative reports, executive summaries, or prose
- Timelines, go-forward plans, or recommendations
- SEO audits, site performance assessments
- People profiles, tool inventories, pipeline assessments
- Renewal negotiation guidance

For comprehensive narrative assessments, use the `client-account-assessment` skill.

## Scope Boundaries

**In scope:** EM account management, client relationship health, ME stability, production quality, deliverable cadence, content feedback patterns, performance vs. stage expectations, strategic alignment.

**Out of scope:** Renewal negotiations (Andi/Marcel), CEO interventions (Marcel), EM hiring (Andi/Bridget), deal desk (Kyle/sales), product roadmap (Marcel/product). Note these for context only.

## DM Rules
1. Never quote DMs — paraphrase only. Do not cite DMs in Evidence Sources.
2. Never reference compensation, bonuses, salary, or raise information.

## Output Rules
- Save to `Reports/{Client_Name}_Health_Score_{YYYY-MM-DD}.md`
- Never write directly to Notion, Slack, or external tools unless explicitly asked
- All documents are proposed drafts for user review

## Verification Checklist (run before saving)
- [ ] All 5 dimensions scored with 1-2 sentence justifications
- [ ] EM scores populated from ClientDB (or gap noted)
- [ ] Independence test: each score makes sense in isolation
- [ ] No DM quotes anywhere
- [ ] No compensation/bonus info anywhere
- [ ] Engagement stage applied to Performance/ROI
- [ ] Red/green flags tagged by dimension
- [ ] Action triggers listed (or "none")
- [ ] Data gaps documented
- [ ] Evidence Sources table complete
- [ ] Output matches template format
