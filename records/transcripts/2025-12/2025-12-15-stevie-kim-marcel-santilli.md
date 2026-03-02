<metadata>
title: Stevie Kim <> Marcel Santilli
date: 2025-12-15
participants:
  - name: Marcel Santilli
    role: Founder/CEO
    company: GrowthX
  - name: Stevie Kim
    role: Editorial Lead
    company: CheckThat
  - name: Jose Farias
    role: Engineering Lead
    company: CheckThat
duration: 125 minutes
recording_link: https://app.fireflies.ai/view/01KC4VVPYXJAT7J71795ZDN5PB
source: fireflies
enriched_on: 2026-03-01 00:00 UTC
</metadata>

## Summary

CheckThat's organic growth strategy meeting aligned on a programmatic brand-page approach targeting 8,000 pages covering 20M monthly searches in low-difficulty keyword niches. The team committed to building a lightweight, modular CMS with editorial overrides, prioritizing cross-linking improvements (current: 80/6,000 indexed), and starting with engineers dogfooding the editorial workflow before scaling. Immediate focus: pricing, reviews, and alternatives variant pages; daily ops of brand candidate approval, prompt management, and profile improvements.

## Context

CheckThat is pursuing organic growth as a core acquisition lever against well-funded competitors (Profound at $30M ARR). The team learned from Canva's programmatic page strategy—they scaled from 200 to 6,000 pages in year one, now operating 45,000+ pages. CheckThat has 6,000 B2B brand pages submitted to search but only 80 indexed, signaling urgent need for SEO improvements and cross-linking. The relationship between Marcel (strategy/vision), Stevie (editorial ops), and Jose (technical execution) is collaborative and aligned on the core challenge: compete through content scale and quality, not budget.

The product philosophy centers on avoiding static, manual content—instead building a living, modular system that evolves dynamically with brand changes. AI workflows costing $3-4 per execution provide cost advantage in generating structured content at scale.

## Relevance

**CheckThat Product & Growth**
- Core business model: organic B2B brand discovery through SEO-driven content
- Strategic initiative: target 25,000 B2B brands as the definitive, programmatically updated source
- Competitive advantage: AI-driven content generation at 1/10th the cost of competitors

**Organic Growth & SEO**
- 8,000-page target with 20M monthly search volume identified
- Priority niches: pricing, reviews, alternatives, product details
- Current bottleneck: 80/6,000 indexing ratio; cross-linking is highest-leverage improvement

**Product Development**
- CMS architecture: lightweight, modular, template-based with editorial overrides
- Metadata control: titles, descriptions, OG images, H1s, slugs all editor-controllable
- Version control: fast iteration, rollback, bulk operations for scale

## Decisions & Commitments

- Start with engineers dogfooding editorial workflow (accept broken links for speed; no customers impacted yet)
- Prioritize variant pages: pricing, reviews, alternatives (highest search intent)
- Build CMS MVP supporting modular blocks, editorial tweaks, and metadata control before scaling
- Daily editorial ops: brand candidate approval, prompt management, profile/page improvements
- Jose owns CMS direction memo (due next day) and admin panel UX improvements
- Stevie owns editorial playbooks (prompt filtering, candidate approval, category management)
- Marcel owns high-level strategy, variant page prototyping, and MVP definition

## Open Questions

- How to handle bulk page creation and approval workflows at scale?
- Which admin panel improvements (alias merging, metadata editing, bulk controls) should be prioritized first?
- What A/B testing framework should guide meta title/description optimization?
- How to balance programmatic content generation with editorial quality at 8,000+ pages?
- What internal linking patterns will most effectively improve crawl efficiency and indexing?

## Overview & Key Topics

### Competitive Landscape
- Profound: $30M ARR, well-funded competitor
- Canva's playbook: scaled to 45,000 pages through programmatic generation
- CheckThat opportunity: target low-difficulty keywords competitors ignore due to unit economics

### Organic Growth Target
- 8,000 priority pages covering 20M monthly searches
- ~22,000 pages at low keyword difficulty identified; narrowing to 8,000
- Focus on specific searcher intent vs. generic high-difficulty brand terms (KD 100)

### Page Architecture
- Hub-and-spoke model: core brand profile + variant subpages
- Variant priorities: pricing, reviews, alternatives, product details
- Lower priority variants: headquarters, logos, jobs, customers (future)

### CMS & Content Strategy
- Lightweight, modular CMS with templates for specific page types
- Modular components/blocks: founders, pricing tables, reviews (AI-generated + manual editorial)
- Metadata control: titles, descriptions, OG images, slugs, H1s (editor-editable)
- Fast iteration, version control, rollback mechanisms

### Cross-Linking & Indexing
- Current status: 80 pages indexed out of 6,000 submitted
- Highest-leverage SEO improvement: cross-linking (start simple, then dynamic scanning)
- Testing: A/B style experiments on meta titles and descriptions

### Editorial Operations
- Phase 1: engineers dogfood workflow (accept broken links; no customers impacted)
- Daily core tasks: brand candidate approval, prompt management, profile/page improvements
- Needed admin improvements: alias UI, bulk creation/approval, version control

### Long-Term Vision
- 25,000 B2B brands as definitive, programmatically updated source
- Living, modular system evolving dynamically with brand changes
- Cost advantage: $3-4 per AI execution vs. competitor manual/expensive approaches

## Action Items

**Jose Farias (CheckThat - Engineering Lead)**
- Write up CMS/editorial system direction memo and share for team alignment
- Prioritize admin panel improvements: metadata editing (titles, descriptions, slugs), bulk page creation/approval, version control with rollback
- Collaborate with Stevie Kim to identify and prioritize bugs/features from editorial feedback
- Create workflows to fill missing metadata fields programmatically and prevent future gaps
- Facilitate brand alias merging and primary profile setting with redirects and consistency
- Shape MVP version controlling content blocks/pages while enabling manual edits for SEO improvements

**Stevie Kim (CheckThat - Editorial Lead)**
- Finalize playbooks for editors: prompt filtering, brand candidate approval, category management
- Continue dogfooding editorial workflows and document blockers for improvement
- Manage editorial operations: subcategories, prompts, brand candidates with quality filters
- Prioritize editorial tickets for prompt similarity and brand validations (daily/weekly cadence)
- Partner with Jose on admin panel UX improvements and editorial workflow needs

**Marcel Santilli (GrowthX - Founder/CEO)**
- Continue shaping organic growth strategy and page architecture (brand variants, modular content)
- Prototype page templates and outputs (pricing, reviews, alternatives) in experimental workspace (Atlas)
- Define MVP scope: editorial workflow, cross-linking system, metadata management, variant page creation
- Guide architectural decisions: profile data vs. editorial overrides vs. AI workflows
- Support operationalization through prioritization and rapid iteration cycles

## Discussion Notes

### Competitive Strategy & Market Opportunity
The team discussed SEO-driven organic growth as the primary defense against well-funded competitors. Profound ($30M ARR) and Canva (45,000 pages) demonstrate the playbook: programmatic page generation at scale. Canva's trajectory—200 to 6,000 pages in year one—is the model. CheckThat's advantage is targeting low-difficulty keyword niches competitors ignore for unit economics reasons. Team identified ~22,000 low-difficulty pages, prioritizing 8,000 covering 20M monthly searches. The philosophy: create unique, valuable content targeting specific searcher intent that competitors can't afford to give away free.

### CMS Architecture & Content Modularization
The CMS design emphasizes lightweight simplicity over feature bloat. Starting point: free-form markdown editor, evolving to templates (pricing, reviews, funding, comparisons). Content will be modular—blocks like founders, pricing tables, reviews can be AI-generated or manually edited, allowing divergence from raw data sources. Editorial control is non-negotiable: meta titles, descriptions, OG images, slugs, H1s must be editor-editable for SEO/UX optimization. Key constraint: CMS must support fast iteration and lightweight version control so editors fix mistakes without slowing production.

### Cross-Linking Strategy & Indexing
Current reality: 80 pages indexed out of 6,000 submitted (1.3% index rate). Cross-linking is the highest-leverage SEO improvement. Phase 1: automatic linking of brands within same subcategories (low-hanging fruit). Phase 2: dynamic text scanning for brand mentions. Variant pages (pricing, alternatives, reviews) will maximize content footprint and provide A/B testing surface for meta title/description optimization.

### Editorial Operations & Workflow
Decision: engineers dogfood the workflow first (no customers exposed yet, so broken links are acceptable trade-off for speed). Three daily operational tasks:
1. Approving brand candidates
2. Managing prompts
3. Improving brand profiles and pages

Immediate admin needs: primary alias UI, metadata bulk editing (titles/descriptions/slugs), bulk page creation/approval, version control with rollback.

### Page Variant Prioritization & Roadmap
High-priority variants (search intent, ranking potential): pricing, reviews, alternatives, product details. These will be bulk-created with AI content + editorial tweaks for thousands of brands. Lower-priority variants (headquarters, logos, jobs, customers) deferred until system matures. Testing approach: A/B experiments on meta titles and descriptions to validate SEO impact.

### Long-Term Product Vision
Goal: become the definitive, programmatically updated source for ~25,000 B2B brands. Philosophy: avoid static manual pages; instead build a living, modular system evolving dynamically with brand changes. Competitive advantage: AI workflows at $3-4 per execution—1/10th competitor cost—enabling superior, well-structured content at scale.

---

## Full Transcript

Full conversation available at: https://app.fireflies.ai/view/01KC4VVPYXJAT7J71795ZDN5PB

This enriched transcript captures the essential strategic alignment, decisions, and commitments. Refer to the Fireflies recording for full context and detailed discussion breakdowns.
