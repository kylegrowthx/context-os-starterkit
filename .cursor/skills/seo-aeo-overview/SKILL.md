---
name: seo-aeo-overview
description: |
  **SEO + AEO Combined Overview**: Orchestrator skill that chains the SEO Domain Audit, Competitive SEO Landscape, and AEO Audit skills, then synthesizes into a single 6-section executive overview document covering core metrics, site structure, content health, competitive SEO, AI visibility, and prioritized fixes.
  - MANDATORY TRIGGERS: full SEO and AI overview for {domain}, comprehensive visibility report, combined SEO and AEO analysis, SEO and AEO overview, complete audit for {domain}
---

# SEO + AEO Combined Overview

Master orchestrator that produces a single executive overview document combining SEO domain analysis, competitive positioning, and AI visibility assessment. Chains three sub-skills and synthesizes their output into a cohesive 6-section report.

## Inputs

Before starting, confirm or gather:

1. **Domain** — the website to audit (e.g., `flodesk.com`)
2. **Client name** — used for output directory
3. **Competitor list** — for the competitive landscape (or reference to existing list)
4. **CheckThat workspace ID** — for the AEO audit (or note if unavailable)
5. **Output directory** — default: `projects/audit-reports/{client}/`

## Sub-Skills Required

| Skill | Path | Produces |
|-------|------|----------|
| SEO Domain Audit | `.cursor/skills/seo-domain-audit/SKILL.md` | Domain metrics, page classification, content trajectory |
| Competitive SEO Landscape | `.cursor/skills/competitive-seo-landscape/SKILL.md` | Competitor rankings, keyword distribution, efficiency metrics |
| AEO Audit | `.cursor/skills/aeo-audit/SKILL.md` | AI visibility scores, presence analysis, source gaps |

If CheckThat data is unavailable, produce sections 1-4 and 6 only, noting the AI visibility gap.

## Workflow

### Phase 1 — Data Gathering

Run the three sub-skills. If running from scratch:

1. **SEO Domain Audit** — read and follow `.cursor/skills/seo-domain-audit/SKILL.md`
2. **Competitive SEO Landscape** — read and follow `.cursor/skills/competitive-seo-landscape/SKILL.md`
3. **AEO Audit** — read and follow `.cursor/skills/aeo-audit/SKILL.md`

If sub-skill outputs already exist in the output directory, read them instead of re-running. Check for:
- `seo-overview-*.md` or `raw-domain-overview.md` (SEO audit exists)
- `competitive-landscape-*.md` (competitive landscape exists)
- `aeo/aeo-audit-report-*.md` (AEO audit exists)

### Phase 2 — Synthesize

Produce `seo-overview-v1.md` with exactly 6 top-level sections:

```markdown
# SEO & AI Visibility Overview: {domain} (v1)

**Date:** {date}
**Domain:** {domain}

---

## 1. Core metrics snapshot

Headline metrics table — 9 rows:
1. Site authority score
2. Referring domains
3. Total organic traffic
4. Total pages indexed
5. Total pages getting organic traffic
6. Total content pages
7. Content pages getting organic traffic
8. Organic traffic per page (w/ traffic)
9. Organic traffic per content page (w/ traffic)

Each row: current value, historical value, 6mo change.

12-month trend table showing monthly organic traffic.

Brief narrative on what the trend means.

---

## 2. Site structure & technical

From the SEO Domain Audit:
- Authority and link profile analysis
- Homepage traffic share and branded search dependency
- Page breakdown by type (full table)
- Type definitions
- Index bloat analysis
- Templates / structural opportunities

---

## 3. Content health

From the SEO Domain Audit:
- Content breakdown by section (tips, blog, etc.)
- Content page trajectory analysis (freefall/declining/stable/growing/surging)
  - Summary table with all 5 buckets
  - By-section breakdown
  - Narrative: what percentage is losing, what the bimodal distribution means
- Section-level diagnosis (yield per page, decline rates)

---

## 4. Competitive SEO positioning

From the Competitive SEO Landscape:
- Traffic ranking table (show ±5 around focal domain)
- Keyword position distribution table
- Organic efficiency table:
  - Traffic per content page
  - Traffic per page
  - Keywords per page
  - Traffic per keyword (with rank)
  - Top-3 keyword concentration (with rank)
  - Top-10 keyword concentration (with rank)
- Direct competitive threats (3-5 competitor paragraphs)

---

## 5. AI visibility

From the AEO Audit:
- Visibility score and trend table
- Competitive AI visibility gap table
  - Include both AI visibility rank AND SEO rank for each competitor
  - Highlight paradoxes (high SEO / low AI, or vice versa)
- Mentions and sentiment summary
- Root causes ("Why {brand} is invisible to AI")
  - Source gap
  - Listicle absence
  - Missing glossary/educational content
  - Narrow content positioning
  - Third-party presence gap
- Bright spots (what's working in AI)

---

## 6. Summary & highest-leverage fixes

### What's working
Bullet points — positive signals from all three analyses.

### What's broken
Bullet points — negative signals from all three analyses.

### Highest-leverage fixes
Split into two groups:

**SEO fixes** (numbered, from sections 2-4):
- Site structure fixes
- Content strategy fixes
- Competitive gap actions

**AI visibility fixes** (numbered, from section 5):
- Source/listicle actions
- Content type actions
- Platform presence actions

Data provenance footnote as blockquote:
> **Data pulled:** {tools and dates for each data source}

---

## Changes from v{N-1}
Only include if this is v2+. List what changed.

### Supporting files
List all raw data and sub-skill output files.
```

## Output Files

| File | Contents |
|------|----------|
| `seo-overview-v1.md` | The master document (6 sections) |

All sub-skill outputs also saved in the same directory structure.

## Versioning

- **v1** — initial production from this skill
- **v2+** — when user requests changes (remove sections, add data, restructure). Create new version, archive previous to `archive/`
- Minor updates (fixing numbers, typos) — edit in place

## Key Rules

- **Maximum 6 top-level sections.** This is a hard constraint. Don't add a 7th.
- **Don't duplicate sub-skill content verbatim.** Synthesize and distill. The overview cherry-picks the most important findings.
- **Cross-reference between sections.** Section 4 (competitive) should reference section 5 (AI visibility) when paradoxes exist. Section 6 (summary) should reference all preceding sections.
- **Data provenance in footnote, not a section.** Source information goes in a blockquote at the bottom of section 6.
- **Every table needs narrative.** No orphan tables. Each one gets at minimum a single paragraph explaining the key takeaway.
