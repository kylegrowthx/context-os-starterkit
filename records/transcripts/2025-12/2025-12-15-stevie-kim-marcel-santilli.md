<metadata>
title: Stevie Kim <> Marcel Santilli
date: 2025-12-15
participants: Stevie Kim, Marcel Santilli, Jose Farias
duration: 125 minutes
recording_link: https://app.fireflies.ai/view/01KC4VVPYXJAT7J71795ZDN5PB
</metadata>

## Summary

Organic growth strategy discussion for brand pages and SEO. The team explored strategies to compete with well-funded players like Profound ($30M ARR) and Canva's 45,000+ pages by creating programmatically generated brand-related pages targeting low keyword difficulty queries. Key focus areas include developing a modular CMS, implementing cross-linking strategies to improve indexing, and establishing efficient editorial workflows.

## Key Takeaways

- Target 8,000 pages addressing 20 million monthly searches in low keyword difficulty niches
- Implement hub-and-spoke model with core brand profile pages linked to variant subpages (pricing, reviews, alternatives)
- Develop lightweight, flexible CMS supporting modular content blocks and variant pages
- Improve SEO hygiene through control of meta titles, descriptions, OG images, and slugs
- Create strong internal linking across brand pages to overcome 80/6,000 current indexing ratio
- Prioritize pricing, reviews, alternatives, and product details as initial variant pages
- Enable engineers to dogfood editorial workflows before scaling to broader teams
- Implement daily operational tasks: approving brand candidates, managing prompts, improving brand profiles

## Action Items

**Jose Farias**
- Write up buckets and overall direction for CMS and editorial system and share by next day for team alignment
- Prioritize admin panel improvements to allow editing metadata like meta titles, short descriptions, and slugs across multiple pages
- Collaborate with Stevie Kim to identify and prioritize bugs and features from editorial feedback
- Create workflows or update existing ones to fill in missing metadata fields programmatically and prevent future gaps
- Facilitate merging of brand aliases and setting primary profiles ensuring redirects and consistency
- Shape MVP version controlling content blocks/pages while enabling manual edits for SEO improvements

**Stevie Kim**
- Finalize playbooks for editors focused on prompt filtering, brand candidate approvals, and category management
- Continue dogfooding editorial workflows and document any blockers or questions for improvement
- Manage editorial activities for subcategories, prompts, and brand candidates with intended filters and quality standards for scalable operations
- Assist in prioritizing editorial tickets for prompt similarity curation and brand validations daily/weekly
- Work with Jose Farias on identifying key admin panel usability improvements and editorial needs

**Marcel Santilli**
- Continue shaping high-level organic growth strategy and page architecture concepts, especially focus on brand variants and modular content modeling
- Prototype page templates and example outputs for pricing, reviews, alternatives to validate page type structures in experimental workspace (Atlas)
- Define minimum viable product (MVP) for editorial workflow, crosslinking system, metadata management, and variant page creation
- Guide architectural decisions on separation between profile data, editorial overrides, and AI workflows for long-tail answers
- Support operationalizing the editorial and technical roadmap through task prioritization and quick iteration cycles

## Discussion Notes

### Organic Growth and Competitive Strategy
The team discussed how to compete against well-funded competitors through SEO-driven organic growth. Profound is at $30M ARR with significant funding. Canva's success was built on programmatic page generation—they grew from 200 to 6,000 pages in the first year and now have 45,000 pages. The strategy is to replicate this through programmatic content creation targeting low-difficulty keyword searches rather than expensive generic brand terms (which have keyword difficulty scores of 100).

The team identified approximately 22,000 pages with very low keyword difficulty, narrowing to 8,000 pages covering nearly 20 million monthly searches as top priority opportunities. The key insight is creating pages that target specific searcher intent and provide unique, valuable content that competitors cannot afford to give away for free.

### CMS and Content Modularization
Discussion centered on designing a lightweight, flexible CMS that avoids over-complexity early on. The approach starts with a simple free-form markdown editor for pages, with the possibility of adding templates for specific page types like pricing, reviews, funding, and comparisons. Pages will have modular components or "blocks" (founders, pricing tables, reviews) that can be AI-generated or manually editorialized, allowing content to diverge from raw data sources.

Editorial control over metadata is critical—meta titles, descriptions, OG images, slugs, and H1s must be editable to improve SEO and user experience. The CMS must support fast iteration and lightweight version control to allow editors to fix mistakes quickly without slowing content production.

### Cross-Linking and Indexing
Current status: 80 pages indexed out of 6,000 submitted. The team discussed cross-linking as the highest leverage SEO improvement. Initial efforts will focus on simple, low-hanging fruit like linking brands within the same subcategory automatically, before advancing to dynamic text scanning for brand mentions. Plans include variant pages for pricing, alternatives, and reviews to maximize content footprint and test SEO impact.

### Editorial Operations
The team decided to start with engineers dogfooding the editorial workflow due to the current lack of indexing and customers. This accepts potential broken links as a tradeoff for speed. Editors will focus on three core daily operational tasks:
1. Approving brand candidates
2. Managing prompts
3. Improving brand profiles and pages

Immediate admin improvements needed: better UI for setting primary aliases, editing meta titles/descriptions/slugs, bulk page creation and approval capabilities, and version control with rollback mechanisms.

### Page Variant Prioritization
Pricing, alternatives, reviews, and product details are the priority variant pages due to high search intent and ranking potential. These will be created in bulk for thousands of brands using AI-generated content with editorial tweaks. Lower priority variants (headquarters, logos, jobs, customers) will be tackled later as the system matures. Testing will include A/B style experiments on meta titles and descriptions.

### Long-Term Vision
The goal is to become the definitive, programmatically updated source of truth for approximately 25,000 B2B brands. The philosophy is to avoid manual, static pages and instead build a living, modular system that evolves dynamically with brand changes. The team's existing AI workflows costing $3-4 per execution provide a competitive advantage in generating superior, well-structured content at scale.

---

## Full Transcript

[Large transcript content from Fireflies - contains detailed conversation between Marcel Santilli, Stevie Kim, and Jose Farias discussing organic growth strategy, CMS architecture, editorial workflows, and SEO optimization for brand pages. Full transcript available at: https://app.fireflies.ai/view/01KC4VVPYXJAT7J71795ZDN5PB]
