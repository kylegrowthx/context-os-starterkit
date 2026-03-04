---
name: competitor-brief
description: |
  **Deep Competitor Brief Generator**: Research and produce comprehensive competitor analysis briefs with company overview, product analysis, 15-dimension perception scoring, SEO/traffic analysis, and strategic assessment. Each brief synthesizes 200+ sources into a structured document comparing the competitor against a focal company (e.g., Vercel).
  - MANDATORY TRIGGERS: competitor brief, competitor analysis, competitive research, competitor profile, competitor deep dive, competitive intelligence brief, "research [company] as a competitor", "create a brief on [company]"
  - Also trigger when: user asks to analyze a company's strengths/weaknesses vs another, wants perception scoring, needs competitive SEO analysis, or requests a head-to-head comparison document
---

# Competitor Brief Skill

Generate a deep competitor brief that synthesizes 200+ sources into a structured analysis document. The brief compares a target competitor against a focal company across company fundamentals, product capabilities, market perception, SEO/content effectiveness, and strategic positioning.

## When to Use

Any time someone needs a comprehensive competitor profile. This goes beyond a quick comparison — it's a research-heavy document meant to inform GTM strategy, content positioning, and competitive intelligence.

## Inputs

Before starting, confirm or gather:

1. **Competitor name** — the company to research
2. **Competitor website** — primary domain
3. **Focal company** — who we're comparing against (e.g., Vercel)
4. **Vercel segment** — which part of the focal company's ecosystem this competitor maps to (e.g., "Frontend Cloud / Deployment", "AI Code Generation")
5. **Output directory** — where to save the brief and scratchpad (default: `records/customers/[focal-company]/competitors/`)
6. **Focal company context path** — where to find existing context on the focal company (e.g., `records/customers/vercel/context/`)

If the user has already provided these in a prior message or a batch list, don't re-ask — just proceed.

## Process

### Phase 1: Research (Scratchpad)

Create a research scratchpad at `[output-dir]/[competitor-slug]-research-scratchpad.md`.

Structure the research around 10 questions. For each, conduct web research and record findings with source URLs:

1. **Company overview** — founding story, history, key milestones, headquarters, mission
2. **Funding & financials** — all funding rounds with dates, amounts, lead investors. Revenue if available. Headcount. Layoffs or restructuring.
3. **Traction & adoption** — user counts, customer logos, market share data, growth trajectory
4. **Key acquisitions & partnerships** — what they bought, why, and what happened
5. **Product & feature analysis** — complete product inventory with capabilities. Map each feature against the focal company's equivalent.
6. **Pricing & packaging** — tier breakdown, free tier details, enterprise pricing signals
7. **Analyst & review coverage** — Gartner, Forrester, G2, Capterra, TrustRadius, Product Hunt scores. Any Magic Quadrant or Wave placements.
8. **Community sentiment** — Reddit, Hacker News, DEV Community, Twitter/X. What developers praise and criticize. Direct quotes where possible.
9. **SEO & web traffic** — domain rating/authority, monthly visits, bounce rate, pages per visit, referring domains. Use SimilarWeb, public Ahrefs data, SEMRush public pages, and any other publicly available sources.
10. **Content strategy** — blog structure, content types, publishing frequency, notable content assets, content hubs, comparison pages

**Source requirements:** Aim for 200+ unique, reputable sources across all 10 questions. Organize by category in the scratchpad with full URLs.

| Category | Target Sources |
|----------|---------------|
| Company & Funding | 25+ |
| Product & Features | 50+ |
| Reviews & Analysts | 50+ |
| SEO & Traffic | 25+ |
| Additional (community, technical, content) | 50+ |

Use parallel research agents when available — launch 4 agents simultaneously:
- Agent 1: Company overview, funding, traction (Questions 1-4)
- Agent 2: Products, pricing, features (Questions 5-6)
- Agent 3: Analysts, reviews, community sentiment (Questions 7-8)
- Agent 4: SEO, traffic, content strategy (Questions 9-10)

### Phase 2: Synthesis (Brief)

Create the final brief at `[output-dir]/[competitor-slug]-competitor-brief-v1.md`.

The brief follows this exact structure:

```markdown
# [Competitor Name] — Deep Competitor Brief

<metadata>
purpose: Comprehensive competitor analysis of [Competitor] for [Focal Company] engagement
audience: GrowthX strategy, [Focal Company] GTM team
related: [study guide path], [scratchpad path]
domain: client-research
confidence: high
sensitivity: client
last_updated: [date]
</metadata>

---

## Executive Summary

3-5 sentence overview of the competitor, their positioning, and the competitive picture vs the focal company. Include a key metrics comparison table:

| Metric | [Competitor] | [Focal Company] |
|--------|-------------|-----------------|
| Founded | | |
| Total Funding | | |
| Valuation | | |
| Revenue | | |
| Headcount | | |
| Key Differentiator | | |

---

## 1. Company Overview

### Founding & History
Narrative of founding story, key pivots, growth milestones.

### Funding History
Table: Round | Date | Amount | Lead Investor | Notable Angels

### Revenue & Financials
Revenue figures, growth rates, headcount, layoffs if applicable.

### Key Acquisitions
Table: Acquisition | Date | Purpose | Outcome

### Executive Team
Table: Name | Title | Notes

### Traction & Metrics
User counts, customer logos, market share, growth milestones.

---

## 2. Product & Feature Analysis

### Core Platform
Feature comparison table: Feature | [Competitor] | [Focal Company] | Gap Assessment

### [Segment-Specific Subsections]
Additional comparison tables for AI products, pricing, framework support, enterprise features — whatever is relevant to this competitor's domain.

### Pricing Comparison
Tier-by-tier comparison table.

---

## 3. Analyst & Review Coverage

### Analyst Recognition
Table of Gartner, Forrester, and other analyst placements.

### Peer Review Scores
Table: Platform | Rating | Reviews | Notes

### Community Sentiment Summary
What the market praises (bullet points with specifics).
What the market criticizes (bullet points with specifics).
The community verdict on [Competitor] vs [Focal Company] (direct quotes where available).

---

## 4. 15-Dimension Perception Scoring

Scores on a 1-10 scale (10 = best in market). Synthesized from analyst reports, review platforms, community sentiment, funding trajectory, and market reputation.

### [Competitor] — Composite: [X.X]

| # | Dimension | Score | Rationale |
|---|-----------|-------|-----------|
| 1 | Trust / Reliability | | |
| 2 | Innovation / Forward-Thinking | | |
| 3 | Ease of Use | | |
| 4 | Value for Money | | |
| 5 | Customer Support Quality | | |
| 6 | Security / Compliance | | |
| 7 | Scalability | | |
| 8 | Integration Capability | | |
| 9 | Industry Expertise / Domain Knowledge | | |
| 10 | Thought Leadership | | |
| 11 | Product Quality / Performance | | |
| 12 | Speed / Time to Value | | |
| 13 | Transparency | | |
| 14 | Customer-Centricity | | |
| 15 | Modern / Contemporary vs Legacy | | |

### [Focal Company] — Composite: [X.X]
Same table for the focal company (scores should be consistent across all competitor briefs).

### Head-to-Head Comparison
| Dimension | [Competitor] | [Focal Company] | Winner |

---

## 5. SEO & Traffic Analysis

### Domain-Level Metrics
Table with whatever data is publicly available: domain rating, monthly visits, bounce rate, pages per visit, referring domains.

Note: Use publicly available data from SimilarWeb, public Ahrefs/SEMRush pages, and web research. If exact data isn't available, note estimates with (est.) and cite the source.

### Content Architecture
Table of content hubs: Content Hub | URL | Type | Purpose

### Content Strategy Characteristics
Content types observed, positioning vs focal company, notable content assets.

### Content Effectiveness Assessment
Strengths and weaknesses of their content strategy. SEO opportunities for the focal company.

---

## 6. Strategic Assessment

### [Competitor]'s Competitive Advantages vs [Focal Company]
Numbered list with bold headers and 1-2 sentence explanations.

### [Competitor]'s Competitive Weaknesses vs [Focal Company]
Numbered list with bold headers and 1-2 sentence explanations.

### What This Means for [Focal Company]'s Content Strategy
Numbered list of content positioning recommendations.

---

## Appendix A: [Competitor]'s Web Properties
Table: Property | URL | Purpose

## Appendix B: Source Count
Table: Category | Sources
Full source list: [link to scratchpad]
```

### Phase 3: Quality Check

Before finalizing, verify:
- [ ] All 6 sections are present and substantive
- [ ] 15-dimension scoring has rationale for every score
- [ ] Head-to-head comparison table is complete
- [ ] SEO section uses available public data (not fabricated)
- [ ] Strategic assessment has both advantages and weaknesses
- [ ] Source count is 200+ across categories
- [ ] Metadata block is complete
- [ ] Focal company scores are consistent with other briefs in the set

## Scoring Guidelines

The 15 dimensions should be scored based on evidence, not gut feel. Here's how to calibrate:

- **9-10:** Category leader or defining the category. Strong evidence from multiple analysts and community consensus.
- **7-8:** Strong performer. Positive analyst coverage, good review scores, community respect.
- **5-6:** Average or mixed signals. Some strengths offset by notable weaknesses.
- **3-4:** Below average. Significant gaps, negative community sentiment, limited analyst coverage.
- **1-2:** Poor. Major deficiencies, widespread criticism, or near-irrelevance in this dimension.

The composite is the unweighted average of all 15 dimensions, rounded to one decimal.

## Output Files

Each competitor produces exactly 2 files:
1. `[competitor-slug]-research-scratchpad.md` — raw research with all sources
2. `[competitor-slug]-competitor-brief-v1.md` — final synthesized brief

## Batch Execution

When running multiple competitors, the skill can be invoked in parallel. Each invocation is independent — no shared state between competitors. The focal company context (loaded once) provides the comparison baseline.

For large batches, organize into waves of 10 parallel agents. Each agent receives:
- Competitor name and website
- Focal company name and context path
- Vercel segment mapping
- Output directory

## Examples

**Example 1: Direct competitor**
```
Competitor: Netlify
Website: netlify.com
Focal Company: Vercel
Segment: Frontend Cloud / Deployment
```
→ Produces a 400+ line brief with detailed product comparison, strong community sentiment data, and nuanced perception scoring.

**Example 2: Adjacent competitor**
```
Competitor: Cloudflare
Website: cloudflare.com
Focal Company: Vercel
Segment: Edge Network / CDN + Frontend Deployment
```
→ Brief focuses on the overlap areas (Pages, Workers, R2) while noting Cloudflare's broader scope.

**Example 3: Niche competitor**
```
Competitor: Coolify
Website: coolify.io
Focal Company: Vercel
Segment: Self-Hosted PaaS
```
→ Brief may be shorter on analyst coverage (open-source projects have less) but richer on community sentiment and GitHub metrics.
