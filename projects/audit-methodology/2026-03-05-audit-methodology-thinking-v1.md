# Audit Methodology — Thinking Notes

<metadata>
purpose: Working notes synthesizing everything GrowthX has built around audits — what exists, what's implicit, what needs to be codified
access: build-team
last_updated: 2026-03-05
</metadata>

---

## What I studied

1. **`projects/audit-reports/`** — All existing audit work (Vercel, Flodesk, Giga.ai, Simple.Life deal room)
2. **`docs/handbook/`** — Company overview, products (especially CheckThat), delivery model, EPD processes
3. **`knowledge/seo-aeo/`** — Study guides, scoring methodologies, research, prompt taxonomy
4. **`.cursor/skills/`** — The six audit skills and how they chain together
5. **`client-reports/context/report-types/`** — How audits become visual reports

---

## The big picture

GrowthX has built something genuinely unusual: a **full-stack audit capability** that spans traditional SEO, AI visibility (AEO), competitive intelligence, content quality, and page-level technical health. But it's grown organically — skill by skill, client by client — and the methodology is scattered across 40+ files in 5+ directories.

There's no single document that says: "This is how GrowthX audits a domain. Here's the framework, here's why each piece matters, here's how the pieces connect, and here's what the output looks like."

That's what this project should produce.

---

## What exists today

### The audit types

| Audit | Skill | Data Sources | Output |
|-------|-------|-------------|--------|
| SEO Domain | `seo-domain-audit` | SEMRush, DataForSEO | Domain snapshot, page classification, trajectory, efficiency |
| Competitive SEO | `competitive-seo-landscape` | SEMRush, DataForSEO | Tiered competitor landscape, threat analysis |
| AEO / AI Visibility | `aeo-audit` | CheckThat (Ordinal) | Visibility, presence, citations, sources, root cause |
| Content Pages | `content-pages-audit` | SEMRush, PageSpeed, a11y, SquirrelScan, DataForSEO | Per-page traffic delta, scored page audits |
| Combined Overview | `seo-aeo-overview` | All of the above | 6-section executive synthesis |
| Competitive Comparison | `competitive-comparison-table` | SEMRush, DataForSEO, CheckThat | Side-by-side SEO + AI metrics table |

### The scoring models

Three distinct scoring frameworks exist, partially overlapping:

1. **CheckThat 4-Score Framework** (brand-level, product)
   - Presence (0–100): Does AI recommend you?
   - Reputation (0–100): What does the market think?
   - Perception (0–100): What story does AI tell?
   - Influence (0–100): How much control do you have?

2. **Page-Level Scoring** (page-level, methodology doc)
   - Discoverability (20%): keyword breadth, traffic, position quality, momentum
   - SEO (25%): meta, structure, crawlability, structured data
   - Content Quality (30%): E-E-A-T, depth, visuals, links
   - Page Health (25%): performance, accessibility, security, mobile
   - Overall: weighted composite

3. **7-Category Page Scoring** (extended model, study guide)
   - Page Health (15%), Discoverability (15%), SEO (20%), AEO (20%), Quality (15%), Engagement (10%), Additional (5%)
   - Adds AEO as a standalone category

4. **AEO Presence Score** (5-tier, within the aeo-audit skill)
   - Tier 1: Visibility (0–70)
   - Tier 2: Durability (0–9)
   - Tier 3: Position (0–8)
   - Tier 4: Source Control (0–8)
   - Tier 5: Coverage (0–5)

### The data pipeline

```
DATA COLLECTION
  SEMRush → domain metrics, organic pages, keyword positions, backlinks, history
  DataForSEO → rank overview, on-page audit, Lighthouse
  CheckThat → visibility scores, mentions, citations, sources, competitive
  PageSpeed MCP → Core Web Vitals, performance, mobile
  a11y MCP → WCAG 2.1 accessibility
  SquirrelScan → 230+ rule multi-category scan

CLASSIFICATION & ANALYSIS
  Page classification → Brand / Content / Templates / Transactional / Education / Support / UGC / Docs / Other
  Content trajectory → Freefall / Declining / Stable / Growing / Surging
  Competitive tiering → Tier 1 (Leaders) / Tier 2 (Challengers) / Tier 3 (Peers)
  Efficiency metrics → traffic/keyword, traffic/page, top-3 and top-10 concentration
  AEO root cause → source footprint, listicle presence, content positioning, third-party presence

SYNTHESIS
  Prioritized recommendations → P0 (now) / P1 (this week) / P2 (this month) / P3 (backlog)
  Phased roadmap → 0–30 days / 30–90 days / 90–180 days
  Executive overview → 6-section synthesis
```

### What's been audited

| Client | SEO Domain | Competitive | AEO | Content Pages | Deep Dives | Page Audits |
|--------|-----------|------------|-----|--------------|------------|-------------|
| Vercel | v3 (full) | — | — | Traffic trends v3 | 5 section deep dives | 523 url-organic, 548 url-rank-history |
| Flodesk | v4 (full) | v1 (full) | v1 (full) | Detail + blog audit | — | SquirrelScan (51 blog), PageSpeed (1), a11y (1) |
| Giga.ai | v1 (thin) | — | — | — | — | — |
| Simple.Life | — | — | — | — | — | — (deal room only) |

---

## What I'm noticing

### 1. The methodology is real but implicit

GrowthX has a rigorous, multi-layered approach to auditing. But it's encoded in skill files, scripts, and example outputs — not in a standalone methodology document. A new team member (or an AI agent without the skills loaded) would struggle to understand the why behind the what.

The skills say *how* to pull data. The knowledge docs explain *what each metric means*. But nobody has written down *why this combination of audits, in this order, produces the insight a client needs*.

### 2. Three levels of analysis, not clearly separated

Looking across everything, there are three distinct levels:

- **Domain-level**: Overall health, trajectory, competitive position (SEO domain audit, competitive landscape, AEO audit)
- **Section-level**: Content types, template categories, product areas (deep dives, content trajectory analysis)
- **Page-level**: Individual URL performance, technical health, content quality (content pages audit, page scoring)

These levels serve different purposes:
- Domain → "Should we work with this client? What's the big picture?"
- Section → "Where should we focus? What content types are working/failing?"
- Page → "What specific pages need fixing? What's the quality bar?"

But the existing skills don't explicitly frame it this way. The SEO domain audit handles domain + section. Content pages handles page-level. The overview combines domain + competitive + AI. There's no clean separation.

### 3. SEO and AEO are converging but still treated separately

The handbook explicitly frames three return channels for content: organic search traffic, AI citations, and brand awareness. CheckThat measures AI visibility. SEMRush measures search visibility. But the audit methodology still treats them as parallel tracks that get stapled together in the overview.

The 7-category page scoring model hints at the right direction — AEO as a scoring dimension alongside SEO, not a separate audit. But that model is a study guide, not an implemented scoring system.

The real question: **Is a page's AI visibility a property of the page itself (measurable at page level), or is it an emergent property of the brand's overall presence?** CheckThat measures at brand level. Page-level AEO factors (citeable structure, clear claims, entity markup) exist but aren't systematically scored.

### 4. CheckThat is the differentiator, but the audit methodology doesn't center it

GrowthX's competitive advantage is the combination of traditional SEO expertise with CheckThat's AI visibility measurement. Nobody else has this. But in the audit flow, CheckThat data comes in as one section of the overview, not as the organizing principle.

Consider reframing: instead of "SEO audit + AEO audit = overview," what if the methodology started with "How does AI see this brand?" and then drilled into why — which leads naturally to SEO, content quality, source analysis, and competitive positioning.

### 5. The Vercel work is deeper than the methodology captures

The Vercel audit work includes custom Node.js scripts (`generate-overview-v3.js`, `generate-traffic-trends-v3.js`, `generate-deep-dives-v3.js`, `audit-utils.js`) that codify analysis logic: trend classification, keyword theming, estimated gain calculations. This is operational methodology encoded in code.

These scripts represent real intellectual property — the rules for classifying content trajectories, the thresholds for "growing" vs "surging," the formula for estimated traffic gain. But they live in a single client directory and aren't referenced by the skills.

### 6. Page-level scoring is well-theorized but inconsistently implemented

Two detailed scoring methodologies exist:
- The 5-score model (Discoverability, SEO, Content Quality, Page Health, Overall)
- The 7-category model (adds AEO and Engagement)

But actual page audits use different tools depending on the client:
- Vercel: url-organic + url-rank-history (traffic data only, no quality scoring)
- Flodesk: SquirrelScan + PageSpeed + a11y + DataForSEO (quality scoring, but only started on a few pages)

The methodology docs describe the ideal. The reality is more pragmatic. The methodology project should bridge this gap.

### 7. The handbook connects audits to business value — the skills don't

The handbook's "Proving ROI" document lays out four measurement tiers: Activity → Reach → Engagement → Conversion. It explicitly frames CheckThat as Tier 2 (Reach). The Strategy Sprint document shows where audits fit in the client lifecycle (Week 1 baseline).

But the audit skills are standalone tools. They don't reference the business context. A methodology document should connect: "We do this audit because it answers this business question for the client at this stage of the engagement."

### 8. Missing: the narrative layer

Every audit produces data. The jump from data to insight to recommendation is where GrowthX's expertise lives — and it's the least documented part. The skills say "produce a narrative analysis" but don't define what makes a good narrative analysis.

The writing style guide exists in `context/voice/` but it's about tone. What's missing is the analytical framework: How do you turn "traffic dropped 40% on blog pages" into "Your blog is in structural decline because [root cause], which means [business impact], and here's the fix [recommendation]."

---

## What this project should produce

### The core deliverable: GrowthX Audit Methodology

A single, authoritative document (or small set of documents) that codifies:

1. **Why we audit** — Business context, client lifecycle stage, questions each audit answers
2. **The framework** — Three levels (domain, section, page), two dimensions (search visibility + AI visibility), and how they connect
3. **Audit types** — What each one is, when to use it, what data it needs, what it produces
4. **Data sources** — What each tool provides, reliability, coverage, cost considerations
5. **Scoring models** — The definitive scoring frameworks, with clear ownership (CheckThat 4-score = brand level, page scoring = page level)
6. **Analysis patterns** — How to go from data to insight: classification, trajectory, efficiency, root cause
7. **The narrative framework** — How to turn findings into client-ready analysis
8. **Recommendation structure** — P0–P3 prioritization, phased roadmaps, the "fix vs. build" distinction
9. **Skill chain** — How the automated skills compose, when to run them, what to do with outputs

### Possible secondary deliverables

- **Audit playbook** — Step-by-step guide for running a full audit engagement (Week 1 of Strategy Sprint)
- **Scoring specification** — Definitive reference for all scoring models, with formulas and thresholds
- **Data source reference** — What each API provides, field mappings, known limitations
- **Report template guide** — How audit findings map to client-reports components

---

## Open questions

1. **Should page-level AEO scoring be part of the methodology?** CheckThat measures brand-level AI visibility. But page-level factors (citeable structure, entity markup, claim clarity) affect that visibility. Should page scoring include AEO dimensions?

2. **Is the 5-score or 7-category model canonical?** The 5-score model is newer and cleaner. The 7-category model adds AEO and engagement. Which one should the methodology standardize on?

3. **How does this relate to ContentOS?** The handbook describes ContentOS as the delivery platform. If audits inform content strategy, should the methodology connect to ContentOS workflows?

4. **Should Vercel's scripts be generalized?** The analysis scripts in `projects/audit-reports/vercel/` encode real methodology. Should they become shared utilities referenced by the skills?

5. **What's the minimum viable audit?** For a new prospect in Week 1 of a Strategy Sprint, what's the fastest path to a useful audit? The full pipeline takes hours. Is there a 30-minute version?

6. **How does the competitive comparison table relate to CheckThat's AI Benchmark visualization?** The competitive comparison skill produces a markdown table. CheckThat's product has the 4-quadrant benchmark (Presence × Perception). Should the methodology align these?

---

## Proposed structure for this project

```
projects/audit-methodology/
├── README.md
├── INDEX.md
├── audit-methodology-v1.md          # The core methodology document
├── scoring-specification-v1.md       # All scoring models, formulas, thresholds
├── data-source-reference-v1.md       # APIs, tools, field mappings, limitations
├── audit-playbook-v1.md              # Practitioner guide for running audits
├── analysis-patterns-v1.md           # How to go from data to insight
├── narrative-framework-v1.md         # How to write audit findings
└── archive/
```

This thinking doc (`2026-03-05-audit-methodology-thinking-v1.md`) stays in the project root as working context.

---

## Next steps

1. Decide scope — full methodology or start with the core document?
2. Decide which scoring model to standardize on
3. Write `audit-methodology-v1.md` as the backbone
4. Build out supporting documents as needed
5. Cross-reference from skills and report types
