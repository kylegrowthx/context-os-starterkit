---
name: client-account-assessment
description: |
  **Client Account Assessment**: Generate comprehensive account assessment reports for individual GrowthX client accounts. Gathers data from Notion (ClientDB, Client Operating Manual, editorial checklists, sync notes), Slack (internal/external client channels, at-risk alerts), and performance reports. Produces a structured markdown report covering account snapshot, executive summary, timeline, people, tools & pipeline links, content performance, critical issues, health score trends, projected health, current state, and go-forward considerations.
  - MANDATORY TRIGGERS: account assessment, account deep-dive, account status report, account review, holistic account analysis, full status on {client}, deep dive on {client}, prep me for the {client} QBR, client snapshot
---

# Client Account Assessment

Produce a comprehensive, single-account assessment report for GrowthX delivery leadership. The report is an investigative document — gather evidence from every available source, synthesize it into a narrative, and surface the signals that matter for decision-making. This skill serves both the EM (Engagement Manager) layer and the ME (Managing Editor) / Production layer.

## When to Use This Skill

Typical triggers: "run an account assessment on {client}", "I need a deep dive on {client}", "give me a full status on {client}", "I want to understand where we stand with {client}", "prep me for the {client} QBR".

## Workflow

### Step 1: Clarify Scope

Ask the user which client account. If context suggests a specific concern (renewal, ME transition, escalation, QBR prep), note it — the report should emphasize that angle in the executive summary and go-forward section.

### Step 2: Gather Data

Read `references/data-sources.md` for the complete source list. Gather data in this order:

**Notion batch:**
1. Search ClientDB for the account → extract health flag, MRR, renewal date, pod, EM, ME, health scores (all historical entries)
2. Query the **Client Strategy Sprint Tracker** database (ID: `2102ba60-bc74-8058-b988-000b509f811f`) → extract Sprint Kickoff Date, Sprint Length, Transition Date, Contract Value, Opt-in/Opt-out model, Sprint Status
3. Fetch the Client Operating Manual → extract contacts, pipeline links (Atlas, Claude projects, Airtable, Google Drive, Linear, Fathom), editorial process, style preferences
4. Search for Editorial Checklist → capture link
5. Fetch recent sync notes (last 4-6 weeks) → key discussion points, performance data, client feedback

**Slack batch:**
1. Search `#d-int-{clientslug}` (internal channel) — last 60-90 days: ME transitions, escalations, handoffs, internal concerns
2. Search `#d-ext-{clientslug}` (external channel) — last 60-90 days: client comms, feedback, brand changes, approval delays
3. Search `#d-at-risk-alerts` for the client name: escalation history

### Step 3: Synthesize and Write

Read `references/report-template.md` for the exact report structure.

Key synthesis guidelines:
- **Timeline**: Reconstruct a chronological narrative from all sources. Name every ME who touched the account. Date every transition, escalation, and milestone. **Always structure the timeline around the engagement lifecycle phases**: Phase 1 = Strategy Sprint (with precise kickoff and transition dates from Sprint Tracker), Phase 2+ = Growth Execution. The Transition Date is the true engagement start date for the Growth Execution period.
- **People**: Identify every person on both GrowthX and client sides. Note who's active, who transitioned, who's the bottleneck.
- **Tools & Links**: Populate the Key Links table from the Operating Manual. The **Atlas Editorial Pipeline** link must be the first entry — if not in the Operating Manual, search Slack for `atlas.growthx.ai` in the client's internal channel. See `references/data-sources.md` for the full lookup sequence.
- **Performance**: Pull specific metrics — pillar growth percentages, keyword rankings, traffic milestones. Avoid vague statements.
- **Critical Issues**: Identify root causes, not symptoms. Each issue should name what's broken, why, and what's been tried.
- **Health Score Trend**: Build the full table from ClientDB entries. Add a pattern analysis paragraph.
- **Projected Health**: Score all 5 dimensions (Relationship, Quantity, Quality, Performance, Strategy) plus Retention Risk (Low/Medium/High/Critical). Compare to latest official ClientDB score and explain divergences. For Performance, apply the SEO/GEO calibration rubric (see below).
- **Go-Forward**: Frame as "considerations" — these are the user's decisions.
- **Exclusion check**: Before finalizing, confirm no DM quotes and no compensation/bonus references.

### Step 4: Save and Verify

Save the report to: `Reports/{Client_Name}_Client_Snapshot_{YYYY-MM-DD}.md`

Verification checklist:
- [ ] All sections from the template are present
- [ ] Health scores match ClientDB data
- [ ] ME names and transitions are consistent throughout
- [ ] All Key Links are valid markdown links
- [ ] Atlas Editorial Pipeline is present as first Key Links entry (or flagged as data gap)
- [ ] No placeholder text remains
- [ ] Supporting Sources table covers every data point cited
- [ ] No DM quotes appear anywhere
- [ ] No compensation, bonus, or salary information
- [ ] Projected Health section present with all 5 dimensions + Retention Risk
- [ ] Engagement lifecycle dates are precise — Sprint Kickoff and Transition Date from Sprint Tracker

## Output Rules

**Always save locally** — write all outputs to the workspace folder. NEVER write directly to Notion, Slack, or any external tool unless the user explicitly asks for it.

## DM Rules

### Hard Rules (No Exceptions)
1. **Never quote DMs.** Paraphrase only. Do not cite DMs in Supporting Sources.
2. **Never reference compensation or bonuses for any employee.**

## Quality Standards

1. **Every claim needs a source.** The Supporting Sources table must trace every major finding to its origin.
2. **Name names.** Never say "the ME" when you can say the person's name.
3. **Date everything.** Transitions, escalations, feedback — all must have dates.
4. **Flag gaps.** If a data source is missing, call it out explicitly. A noted gap is a finding.
5. **Narrative over bullets.** Executive Summary and pattern analysis in prose. Tables/bullets for structured data.

## SEO/GEO & Site Performance Assessment

When assessing Performance and projecting health, apply expert-level SEO/GEO analysis. Content production volume means nothing if the site can't convert that content into rankings, traffic, and business outcomes.

### Technical SEO Readiness
- **Indexation health**: Pages indexed? robots.txt correct? Sitemap valid?
- **Canonical tags**: Self-referencing canonicals in place? Conflicts from migrations?
- **Site architecture**: Blog URL depth? Hub pages? Internal linking?
- **Core Web Vitals / Page speed**: Fast enough for Google's page experience signals?
- **Schema markup**: Article, FAQ, HowTo, BreadcrumbList implemented?
- **Migration impact**: If recent migration, assess 301 redirects, 404s, recovery timeline (3-6 months typical)

### Content-to-Ranking Timeline
- New domains/blog sections: **4-8 months** to meaningful organic traffic
- Publishing delays add to the timeline
- Content on sites with broken indexation is **not effectively published** from an SEO standpoint

### AEO/GEO
- Is content structured for LLM citation?
- CheckThat.ai or Scrunch metrics available? If not, note the gap.

### Performance Score Calibration
- **5**: Measurable business impact proven
- **4**: Early positive signals, tracking in place
- **3**: Content published and indexed, no measurable results yet
- **2**: Content published but site has technical issues, or no tracking
- **1**: Content not published, site broken, no measurement infrastructure

### Retention Risk from Performance Gap
When Performance projected at 2 or below and client expects ROI: flag as retention risk, note timeline to results, identify expectation misalignment.

## Delivery Org Scope Reminder

See `references/delivery-org-scope-rules.md`. Focus on EM account management, client relationships, ME stability, production quality, deliverable cadence, pipeline health, and team execution. Note renewal dates and CEO interventions for context only — don't own those decisions.

## Engagement Lifecycle & Timeline Precision

Every GrowthX engagement follows: Sales → Pre-Kickoff → Strategy Sprint (8-10 weeks) → Conversion/Transition → Growth Execution (12+ months).

Key dates from Sprint Tracker:
- **Sprint Kickoff Date**: Start of proving period (NOT the engagement start)
- **Sprint Length**: Typically 8 weeks
- **Transition Date**: True start of ongoing contracted engagement
- **Renewal Date**: Typically 12 months after Transition Date

Timeline rules:
1. Phase 1 of every timeline = Strategy Sprint with precise dates
2. Phase 2+ = Growth Execution from Transition Date
3. Never say "Start Date" without specifying Sprint Kickoff vs Growth Execution start
4. Note holiday gaps if sprint was elongated
5. Conversion context (opt-in/opt-out, delays, concerns) belongs in the timeline

## Tips

1. Start broad, go deep on red flags
2. Cross-reference Slack and Notion — Slack has the real story, Notion has the official record
3. Never quote DMs — paraphrase only
4. The Operating Manual is gold for tool links and contacts
5. Health score patterns tell the story — trends > single data points
6. Assess the site, not just the content — apply SEO/GEO calibration
7. Champion gaps are retention risks — if the deal signer is gone, note it
