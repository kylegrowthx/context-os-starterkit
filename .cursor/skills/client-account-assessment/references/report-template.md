# Account Assessment Report Template

Use this structure for all account assessment reports. Adapt sections based on what data is available — include every section but note data gaps explicitly rather than omitting sections.

## Template

```markdown
# {Client Name} — Client Snapshot

**Prepared by:** {Author Name}, {Title}
**Date:** {Date}

---

## Account Snapshot

- **Client:** {Name} ({domain}) — {one-line description}
- **Monthly Revenue:** ${amount}
- **Contract:** {term}
- **Sprint Kickoff:** {date} ({sprint length} weeks)
- **Sprint → Growth Execution Transition:** {date}
- **Growth Execution Start:** {date} (same as transition)
- **Renewal Date:** {date} ({time until renewal})
- **Contract Model:** {Opt-in/Opt-out}
- **Health Flag:** {🔴/🟡/🟢} {Red Flag/Yellow Watch/Green}
- **Pod:** {Pod name} ({EM name}, EM)
- **Current ME:** {name} ({status})
- **Weekly Deliverables:** {description}
- **Client Contacts:** {names and roles}
- **QBR Scheduled:** {date, if applicable}

---

## Executive Summary

{2-3 sentence paragraph covering: current state, primary risk/opportunity, critical upcoming moment. Written as narrative prose, not bullets. Should be standalone — a reader should understand the account's situation from this paragraph alone.}

---

## Account History & Timeline

{Organize chronologically into named phases that align with the engagement lifecycle. Phase 1 must always be the Strategy Sprint. Subsequent phases cover Growth Execution. Each phase gets a ### header with date range. Within each phase, use dated bullet points for key events. Include: launches, ME transitions, escalations, client feedback, publishing milestones, health score shifts.}

### Phase 1: Strategy Sprint ({sprint kickoff date} – {transition date})
- **{kickoff date}:** Strategy Sprint kicks off ({sprint length}-week sprint, {opt-in/opt-out} model, ${sprint contract value} SOW)
- **{date}:** {Sprint-period events: calibration article, artifact development, deep dives, early content production, publishing setup}
- **{transition date}:** Sprint completes; client converts to Growth Execution

### Phase 2: Growth Execution — {descriptive name} ({transition date} – {date range})
- **{date}:** {Growth Execution events: pod assignment, ME transition from Sprint ME to Growth Execution ME, production ramp, etc.}

{Continue phases as needed. If the client had multiple Sprint workstreams (e.g., separate pSEO or Custom sprints), each gets its own phase entry.}

---

## People Involved

### GrowthX Team (Current)

| Role | Person | Status |
|------|--------|--------|
| Engagement Manager | {name} | {status} |
| Managing Editor | {name} | {status} |
| {other roles} | {name} | {status} |

### ME Transition History

{Numbered list of all ME assignments chronologically. Note total transitions and duration.}

### Client Side

| Person | Role | Notes |
|--------|------|-------|
| {name} | {role} | {behavioral notes, responsiveness, decision authority} |

---

## Tools & Production Pipeline

### Content Pipeline

{Flow diagram using indented text showing content journey from creation to publication}

### Key Links

| Resource | Link |
|----------|------|
| Atlas Editorial Pipeline | {link} |
| Editorial Checklist | {link} |
| {other tools} | {link} |

### Tools in Use

{Bulleted list of tools with one-line descriptions and current status notes}

---

## Content Performance

### What's Working
{Performance wins with specific metrics — pillar growth %, keyword rankings, traffic milestones}

### What's Declining
{Declining metrics with specific numbers and trend direction}

### Scrunch / AEO Visibility
{AEO/LLM visibility metrics if available}

---

## Critical Issues

{Numbered list of issues, each with:}

### {N}. {Issue Title} ({severity: URGENT/HIGH/MEDIUM})

{Description paragraph}

**Root cause:** {specific cause}

**Attempted interventions:**
{What's been tried}

---

## Health Score Trend

| Date | Relationship | Quantity | Quality | Performance | Strategy | Notes |
|------|-------------|----------|---------|-------------|----------|-------|
| {date} | {1-5} | {1-5} | {1-5} | {1-5} | {1-5} | {context} |

{Pattern analysis paragraph after the table}

---

## Projected Health (Signal-Based Assessment)

This is an independent assessment based on all signals gathered during this snapshot — not just the EM's self-reported ClientDB scores. Where the projected score diverges from the official score, the gap is noted and explained.

| Dimension | Official (Latest) | Projected | Gap | Signal Summary |
|-----------|-------------------|-----------|-----|----------------|
| Relationship | {1-5} | {1-5} | {+/-/—} | {key signal driving the projected score} |
| Quantity | {1-5} | {1-5} | {+/-/—} | {key signal} |
| Quality | {1-5} | {1-5} | {+/-/—} | {key signal} |
| Performance | {1-5} | {1-5} | {+/-/—} | {key signal} |
| Strategy | {1-5} | {1-5} | {+/-/—} | {key signal} |
| **Retention Risk** | — | {Low/Medium/High/Critical} | — | {key signal driving retention assessment} |

{1-2 paragraph narrative explaining the overall projected health, why it diverges from official scores if it does, and what the projected trajectory looks like over the next 30-60 days. This is the "what the data actually says" section — the EM surveys capture the working-level relationship, but this assessment synthesizes Slack tone, leadership signals, at-risk flags, champion status, renewal dynamics, and production reality into a holistic view.}

---

## Where We Stand Today ({date})

**What exists:**
{Bulleted list of assets, readiness, positives}

**What's broken:**
{Bulleted list of active problems}

**What's at stake:**
{Revenue, renewal, credibility, goals at risk}

---

## Considerations for Go-Forward Plan

### Before {next milestone} ({date range})
{Action items with rationale}

### At {milestone} ({date})
{Talking points and strategic recommendations}

### Renewal Considerations ({date})
{Timeline analysis, what's realistic, framing advice}

---

## Supporting Sources

| Source | Key Signal |
|--------|-----------|
| {source with location} | {what it contributed} |
```

## Style Notes

- Write in narrative prose; avoid excessive bullet points in analytical sections
- Every claim should be traceable to a source in the Supporting Sources table
- Health scores use 5 dimensions: Relationship, Quantity, Quality, Performance, Strategy (each 1-5)
- Projected Health adds a 6th dimension: Retention Risk (Low/Medium/High/Critical) based on all gathered signals
- Projected Health should be honest and independent — if the data contradicts the EM's self-reported scores, say so
- Name specific people, dates, and metrics — never use vague language
- Frame go-forward items as "considerations" — these are the user's decisions to make
- Flag data gaps explicitly rather than omitting sections
- Always distinguish Strategy Sprint from Growth Execution in timelines — the Sprint is an extended sales cycle / proving period; Growth Execution is the contracted engagement
- Sprint Kickoff Date, Transition Date, and Renewal Date should be sourced from the Client Strategy Sprint Tracker database, not inferred from vague references
- When assessing time-in-engagement, count from the Growth Execution start (Transition Date), not from the Sprint Kickoff — a client who's been in Growth Execution for 5 weeks has a very different context than what "3 months since kickoff" suggests
