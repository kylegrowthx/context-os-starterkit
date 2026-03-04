# Brex Resources Page: Proposed Enhancements
** February 2026**

---

## What This Document Covers

This document walks through each proposed enhancement to the Brex resources experience, explains the rationale, and provides reference examples from companies with best-in-class content architecture. Every change works within the existing design system — we're adding features and improving organization, not replacing what's already working.

**Live prototype:** [brex-hub.onrender.com/resources](https://brex-hub.onrender.com/resources)
**Current production:** [brex.com/resources](https://www.brex.com/resources)

---

## Why Now

Ramp — Brex's main competitor — already has organized content with 17 category hubs, consistent article templates, and customer proof on every page. Capital One — Brex's acquirer — runs four specialized content hubs with persistent navigation and structured metadata. Both have better content architecture than Brex does today.

The companies Brex's design leadership admires (Apple, Nike, Square) all treat content architecture as a design problem worth solving. Brex hasn't yet.

Every week this stays unchanged, the gap widens and the integration gets harder.

---

## Guiding Principles

1. **Enhance, don't replace.** The existing design system stays. We're adding new capabilities and better organizing existing content.
2. **Every change has a purpose.** Each enhancement serves at least one of three goals: better SEO, better content discovery, or better user experience.
3. **Brand first.** All fonts, colors, image treatments, and UI patterns follow the existing Brex brand guidelines.

---

## Enhancement Walkthrough

### 1. Resources Navigation Dropdown

**What we're adding:**
Reorganized the Resources dropdown in the global navigation to surface all content types in a clean, categorized layout — Discover (Articles, Case Studies, Reports, The Index, Tools), Topics, Customer Hub, and a Latest panel showing recent content.

**Current state** — [brex.com/resources](https://www.brex.com/resources) (hover over "Resources"):
- Links to outdated sections (Events, Webinars that haven't been updated)
- No topic-level navigation
- No visibility into content types like Tools or Indexes
- Customer Stories and Case Studies are redundantly listed

**Proposed** — [brex-hub.onrender.com/resources](https://brex-hub.onrender.com/resources) (hover over "Resources"):
- Clean three-column layout: Discover (content types), Topics, and Latest
- Every content category is immediately accessible
- Topics align to product areas and audience needs
- Latest panel surfaces fresh content, keeping the dropdown current

**Why this matters:**

| Benefit | Detail |
|---------|--------|
| **SEO** | Every link in the global nav passes authority. Linking to topic hub pages and content type pages from the global nav strengthens those pages for search engines. |
| **Discoverability** | Users can navigate to any content type or topic in one click from anywhere on the site. Currently, finding Spending Trends requires 3+ clicks. |
| **Housekeeping** | Removes dead links to outdated sections (Events, Webinars) that hurt credibility. |

**Who does this well:**
- **Ramp** organizes their blog into 17 distinct topic categories (AI, Accounting, Alternatives, Expense Management, etc.) with clear hub pages for each. Their "Helpful resources" section acts as a secondary resource directory. Even Brex's direct competitor has clearer content navigation.
- **Capital One** uses multiple nav entry points for their Tech Blog, Insights Center, and Commercial Insights — each clearly labeled and accessible from the top nav.
- **Square's "The Bottom Line"** maintains a persistent sub-nav connecting all seven topic areas across every page.

**Visual evidence:**

`[Screenshot: ramp.com/blog — category navigation showing 17 topic categories with clear labels]`
Ramp's users can find any content category in one click. Brex's Resources dropdown links to outdated sections.

`[Screenshot: capitalone.com/tech/blog — persistent sub-nav bar showing Tech | AI | Our Stack | Blog | Careers | Research]`
Capital One gives each content hub its own navigation. Post-acquisition, Brex should meet this standard.

`[Screenshot: squareup.com/us/en/the-bottom-line — horizontal 7-topic sub-nav]`
Square's sub-nav appears on every single page within The Bottom Line. The gold standard for B2B fintech content navigation.

---

### 2. Resources Hub Page: New Content Sections

**What we're adding:**
The main /resources page now surfaces all content types in organized sections — Case Studies, E-books & Guides, The Index, Tools, Trending, Spend Trends, and topic-specific article collections (Expense Management, Accounting, Corporate Travel, Procurement). Each section includes a "See All" link to its dedicated page.

**Current state:**
- A flat grid of manually selected content, some dating back to 2024
- No separation by content type
- No topic-level browsing
- Outdated podcasts and webinars featured prominently

**Proposed:**
- Multiple distinct sections, each focused on a content type or topic
- Featured hero content at the top with the latest guide/report, alongside recent blog articles in the Latest section
- "See All" links on every section for deeper browsing
- Fresh, relevant content surfaced automatically
- Existing card and image styles maintained throughout

**Why this matters:**

| Benefit | Detail |
|---------|--------|
| **SEO** | Each "See All" link creates an indexable hub page (e.g., /resources/case-studies, /resources/tools). More indexable pages = more search entry points. |
| **User experience** | Users can browse by interest (Expense Management) or content type (Case Studies) rather than scrolling through a flat grid. |
| **Content lifecycle** | Outdated 2024 content is replaced by recent, relevant material. Abandoned sections (podcasts with no new episodes in 7+ months) are pruned. |

**Who does this well:**
- **Square's "The Bottom Line"** uses 8+ distinct sections on their homepage: Featured Series, Latest, Topic sections, Editor's Picks, Collections, Videos, Podcasts, Explore Topics, and Contributors.
- **Apple Newsroom** separates Latest News and Apple Stories into two clear streams, with "View All" links for each.

**Visual evidence:**

`[Screenshot: squareup.com/us/en/the-bottom-line — full homepage scroll showing 9+ distinct content sections]`
Square's homepage is a discovery dashboard with 9+ entry points. Brex offers one flat grid.

`[Screenshot: apple.com/newsroom — homepage showing "Latest News" and "Apple Stories" as two clear streams with "View All" links]`
Apple separates chronological content from curated editorial — the same pattern we're proposing.

---

### 3. Content Tagging: Topic + Role

**What we're adding:**
Every piece of content gets tagged by both topic (Expense Management, Accounting, Travel, etc.) and role (CFO, Finance Manager, Controller, Founder/CEO). Tags appear on content cards and link to dedicated tag hub pages.

**Current state:**
- Articles live under rigid one-to-one URL structures (an article can only belong to one category)
- Filter states on the current resources page are not indexable — search engines can't crawl them
- Inconsistent or missing tags across sections
- No role-based filtering

**Proposed:**
- Multi-tag system: an article can be tagged to multiple topics AND roles
- Each tag links to a hub page showing all content with that tag
- Filter by topic, by role, or both
- Each filtered view creates a unique, indexable URL

**Why this matters:**

| Benefit | Detail |
|---------|--------|
| **SEO (major)** | Filter states that aren't indexable = invisible to search engines. Making each tag combination a unique URL unlocks potentially dozens of new indexable pages from existing content. This is one of the highest-impact technical SEO improvements we can make. |
| **Discoverability** | A CFO lands on one article and can instantly see all other CFO-relevant content across articles, tools, case studies, and reports — regardless of format. |
| **Internal linking** | Tags create a natural internal linking web. Every tag hub page links to every piece of content with that tag, and every piece of content links back. This dense, relevant linking structure is a strong SEO signal. |

**Who does this well:**
- **Apple Newsroom** has 30+ topic tags in their archive with combinable filters (e.g., "Privacy" + "2025" + "March"). Each combination is a browsable, linkable state.
- **Square** uses a dual-layer taxonomy: 7 primary categories + 20+ secondary tags. Every article can display multiple tags, and each tag has its own hub page.
- **Ramp** has 17 well-defined category hub pages (e.g., ramp.com/blog/alternatives, ramp.com/blog/expense-management) with featured content and "Explore more categories" for lateral browsing. Each category functions as a tagged content hub.

**Visual evidence:**

`[Screenshot: apple.com/newsroom/archive — filter panel open showing 30+ topic tags plus year/month filters]`
Apple supports rich multi-dimensional filtering. Brex limits articles to one category with no combinable filters.

`[Screenshot: squareup.com/us/en/the-bottom-line — "Explore Topics" tag cloud showing all secondary tags]`
Square's dual-layer taxonomy lets articles belong to multiple topics. Each tag has its own hub page.

`[Screenshot: ramp.com/blog/expense-management — category hub page with featured content and "Explore more categories"]`
Ramp has 17 well-defined category hub pages. Brex doesn't have any.

---

### 4. Sub-Navigation Bar

**What we're adding:**
A sub-navigation bar across the resources section: Articles, Books, Case Studies, Reports, The Index, Tools. Persistent as you browse — always visible, always showing what else is available.

**Current state:**
- Blog, Resources, and Spending Trends operate as completely disconnected silos
- No way to navigate between content types without going back to the main nav
- Users can't tell what other content exists from within any single section

**Proposed:**
- Persistent sub-nav connecting all content types
- The existing global navigation remains sticky at the top — the sub-nav sits below it, not instead of it
- Topic and Role dropdowns for filtering within each content type
- Two-click taxonomy: from anywhere in resources, any content type is two clicks away

**Why this matters:**

| Benefit | Detail |
|---------|--------|
| **Navigation** | Users always know where they are and what else exists. Currently, going from a case study to the blog requires navigating back to the top-level nav. |
| **SEO** | The sub-nav creates persistent internal links to all content type hub pages from every page in the resources section. |
| **Engagement** | Reduces bounce rate by giving users clear next-step options within the content ecosystem. |

**Who does this well:**
- **Square** is the gold standard here — a persistent 7-topic sub-nav appears on every single page within "The Bottom Line." You always know where you are and what else exists.
- **Nike's Newsroom** uses a sub-nav with tabs (Collections, Press Releases, All) plus a search bar — exactly the pattern we're proposing.
- **Capital One's Tech Blog** has a dedicated sub-nav (Tech, AI, Our Stack, Blog, Careers, Research) — validating that even within a larger corporate site, content sections benefit from their own navigation.

**What the competition gets wrong (our opportunity):**
- **Ramp** has no sub-nav connecting their Blog and Velocity hubs — they feel like separate properties. Building a cohesive sub-nav is a direct competitive advantage over Ramp.

**Visual evidence:**

`[Screenshot: squareup.com/us/en/the-bottom-line — navigate from hub → topic page → article, showing sub-nav persists at every level]`
As you navigate deeper, the 7-topic sub-nav stays visible. You always know where you are and what else exists.

`[Screenshot: about.nike.com/en/newsroom — sub-nav showing Collections | Press Releases | All tabs plus search bar]`
Nike's Newsroom shows exactly our proposed pattern: content type tabs + search.

`[Screenshot: ramp.com/blog side-by-side with ramp.com/velocity — showing no visual connection between the two hubs]`
Negative example. Ramp's content types feel like separate properties. Brex can leapfrog this.

---

### 5. Article Page Enhancements

**What we're adding:**
Consistent article page experience with: author attribution, publish date, estimated read time, sticky table of contents, related articles, and topic links.

**Current state:**
- Some articles have authors, others don't
- Some have dates, others don't
- Jump links and table of contents appear randomly
- No related content or dynamic cross-linking at the bottom
- CTAs are missing or inconsistent
- No clear way to explore related topics after reading

**Proposed:**
- Every article follows the same template: author, date, read time at top; sticky table of contents in sidebar; related articles and topic links at bottom
- Author bio toggle (can be turned on/off per author)
- Consistent CTA placement

**Why this matters:**

| Benefit | Detail |
|---------|--------|
| **Brand consistency** | Every article should feel like the same brand. Right now, the inconsistency creates a patchwork experience. |
| **SEO** | Structured article pages with consistent metadata (author, date, topics) help search engines understand and rank content. The sticky table of contents creates in-page anchor links that can appear as rich results. Related articles and topic links create more internal linking. |
| **Engagement** | Related articles at the bottom keep users in the content ecosystem rather than bouncing after one article. |

**Who does this well:**
- **Apple Newsroom** — Every single article uses an identical template. Date, category, headline, body, related. Zero variation. No randomness.
- **Square** — Every article shows category label, author (linked to profile), date, and read time. No exceptions.
- **Nike's "The Record"** — Series tag, headline, and CTA on every card. Consistent visual treatment across all content.
- **Ramp** — Every article includes author name + title, publish date, read time, editor attribution, "Don't miss these" related articles, and customer testimonials carousel. Article consistency is table stakes for Brex's main competitor.

**Visual evidence:**

`[Screenshot: any Apple Newsroom article — showing category tag, headline, date, hero image, body, related content. Identical template.]`
Apple has maintained perfect template consistency across 20+ years of content. Zero variation.

`[Screenshot: any Square article — showing category label, author (linked), date, read time, multiple tags, related articles, author bio]`
Square's article pages include every element we're proposing. Proven, not aspirational.

`[Screenshot: any Ramp blog article — showing author + title, publish date, read time, editor attribution, "Don't miss these" module, customer testimonials carousel]`
Brex's direct competitor treats article consistency as table stakes. Brex's inconsistency is the outlier.

---

### 6. Content Organization & Pruning

**What we're adding:**
Surfacing fresh, relevant content and pruning abandoned sections.

**Current state:**
- Podcasts section: last episode was 7+ months ago
- Webinars: outdated, not maintained
- The resources page features content from 2024 alongside current content
- No editorial curation — the page feels stale

**Proposed:**
- Remove or archive abandoned sections (podcasts, outdated webinars)
- Surface most recent and highest-performing content
- Editorial curation through Featured, Trending, and topic-specific sections

**Why this matters:**
Outdated content undermines brand credibility. When a visitor sees a podcast section with nothing newer than May 2025, it signals that this part of the site isn't maintained. Pruning dead weight and surfacing current content shows that Brex's resources are active, authoritative, and worth revisiting.

**Visual evidence:**

`[Screenshot: ramp.com/blog — showing clean, current content with no abandoned sections or stale listings]`
Ramp keeps their content house clean. No dead podcasts, no outdated webinars.

`[Screenshot: brex.com/resources — showing the abandoned podcast section with last episode 7+ months ago]`
Side-by-side with Ramp, this contrast makes the case for pruning.

---

### 7. Search Functionality

**What we're adding:**
Search across all resources — articles, case studies, tools, reports, and indexes.

**Current state:**
- The current search on the resources page doesn't work well (searches for "spend management" return no relevant results)
- No way to find specific content without browsing or using Google

**Proposed:**
- Search bar integrated into the resources navigation
- Searches across all content types with tag-based filtering

**Why this matters:**
Users who know what they're looking for should be able to find it instantly. The current search experience is broken — this is a basic usability fix that improves time-on-site and reduces frustration.

**Who does this well:**
- **Nike's Newsroom** includes a search bar directly in the sub-nav alongside content type tabs.

**Visual evidence:**

`[Screenshot: about.nike.com/en/newsroom — search bar integrated into the sub-nav alongside Collections | Press Releases | All tabs]`
Nike puts search at the same level as browsing. Users who know what they want can find it instantly.

---

### 8. In-Article CTAs Linking to Tools

**What we're adding:**
Contextual CTAs within articles that link to relevant tool pages (e.g., an expense management article includes a CTA for the Expense Calculator tool).

**Current state:**
- No cross-linking between content and tools
- Demo CTA is the only conversion option on most pages — and it underperforms

**Proposed:**
- Tool-specific CTAs placed contextually within relevant articles
- Dynamic cross-linking: tools surface in related content sections

**Why this matters:**

| Benefit | Detail |
|---------|--------|
| **Conversion** | Tools drive higher-intent actions than demo CTAs. A user reading about expense management who sees a link to an expense calculator is more likely to engage. |
| **Cross-pollination** | Content and tools reinforce each other. Articles drive traffic; tools capture leads. Connecting them multiplies the value of both. |
| **Multi-team utility** | Paid Search, Sales, and SEO teams can all use tool pages as conversion destinations. |

**Competitive advantage over Ramp:**
- Ramp has calculators (per diem, mileage reimbursement, startup costs) but **no centralized /tools hub page** — ramp.com/tools returns 404. Their calculators are scattered across inconsistent URL patterns. Brex building a proper /tools hub with organized, tagged, filterable tools is a direct competitive differentiator.
- Ramp's calculator pages do cross-link to related blog articles at the bottom — validating the in-article CTA approach. But without a hub page, their tools are only discoverable through search or blog articles. Brex can do better.

**Visual evidence:**

`[Screenshot: squareup.com/us/en/the-bottom-line tools section — showing tools tagged with same taxonomy as articles, filtering with counts like "All 43 | Cash Flow 23 | Business Growth 22"]`
Square doesn't separate tools from content — they share navigation, taxonomy, and discovery paths.

`[Screenshot: ramp.com/tools — showing the 404 page]`
Ramp has no centralized tools hub. Their calculators are scattered across three different URL patterns. This is their biggest structural weakness.

`[Screenshot: ramp.com/per-diem-calculator — scrolled to bottom showing "Related posts" section linking to blog articles]`
Ramp's calculators do cross-link to blog content, validating the approach. But without a hub, tools are only found through search.

---

## Reference Examples

### Companies with best-in-class content architecture:

| Company | Why It's Relevant | What to Look At | URL |
|---------|------------------|----------------|-----|
| **Ramp** | Direct competitor — creates competitive urgency | Blog with 17 categories, dual-hub strategy, consistent articles, no tools hub (weakness) | [ramp.com/blog](https://ramp.com/blog) |
| **Capital One** | Acquiring Brex — sets the standard Brex must meet | Tech Blog sub-nav, Insights Center strategic pillars, Learn & Grow for SMB | [capitalone.com/tech/blog](https://capitalone.com/tech/blog) |
| **Apple** | CDO design benchmark | Newsroom archive with 30+ topic filters, consistent article templates | [apple.com/newsroom](https://www.apple.com/newsroom/) |
| **Nike** | CDO design benchmark | "The Record" editorial series, Newsroom sub-nav with search | [about.nike.com/en/stories](https://about.nike.com/en/stories) |
| **Square** | Direct B2B fintech blueprint | "The Bottom Line" — persistent sub-nav, multi-tag taxonomy, integrated tools section | [squareup.com/us/en/the-bottom-line](https://squareup.com/us/en/the-bottom-line) |

### Why these matter for Brex

Ramp is directly targeting Brex customers with competitive content — their "Alternatives" category includes pages optimized to capture people searching for Brex alternatives. Post-Capital One acquisition, Ramp is positioning itself as the "independent" choice. A fragmented resources experience makes it easier for Ramp to win.

Capital One's content ecosystem is already more structured than Brex's. Post-acquisition, Brex's content experience will need to fit within Capital One's ecosystem. Making these improvements now demonstrates design leadership and ensures a smoother integration.

A detailed breakdown of each company's patterns, including Ramp, and how they map to Brex's proposed changes is available in the companion document: [Competitor Content Hub Comparisons](brex-competitor-content-hub-comparisons-v1.md).

---

## Addressing Common Questions

### "Why not just make changes to existing pages?"

That's exactly what this is. We're:
- Adding features to existing pages (tags, CTAs, author/date, related content)
- Improving organization of existing content (topic sections, "See All" links)
- Creating a few new section pages (/tools, /indexes) that follow the same design system

We are not replacing the existing design. We're building on it.

### "Why was this prototyped outside the core system?"

Render is a prototyping environment. It's dramatically faster to iterate on feedback in Render than to build directly in Sanity — changes that would take days in the production CMS take minutes in Render. Once the enhancements are approved, everything moves into Sanity and is built within the production system. The prototype exists so we can align quickly before committing engineering time to the production build.

Note: some visual inconsistencies in the Render prototype (e.g., font rendering on larger screens) are artifacts of the prototyping environment and would not appear in the production build within Sanity.

### "How much effort does this take internally?"

GrowthX handles all build work. Internal effort is limited to:
- Review and feedback on the prototype (this document)
- Approving the final designs
- Tagging existing content with topics and roles (GrowthX can assist)

There is no net-new design work required from the internal design team.

---

## Technical SEO Benefits

For additional context on why these changes matter from a search perspective:

| Enhancement | SEO Impact |
|-------------|-----------|
| **Indexable tag pages** | Each topic + role tag combination creates a unique, crawlable URL. Dozens of new pages from existing content — no new content creation required. |
| **Improved internal linking** | Sub-nav, tag links, related articles, and CTAs create a dense internal linking structure. This is the #1 signal search engines use to understand site architecture. |
| **Breadcrumbing** | Clear breadcrumb trails improve crawlability and can appear as rich results in search. |
| **Structured hierarchy** | /resources → /resources/articles → /resources/articles/expense-management creates a logical content hierarchy that search engines reward. |
| **More surface area** | More indexable pages = more entry points from search = more traffic opportunities. |
| **Content freshness** | Pruning outdated content and surfacing recent material signals to search engines that the site is actively maintained. |

---

## Presentation Strategy

### Side-by-Side Slides

For maximum impact, create before-and-after comparisons:

| Slide | Left Side (Problem) | Right Side (Evidence) |
|-------|---------------------|----------------------|
| 1 | Brex Resources dropdown (outdated links) | Capital One Tech Blog sub-nav + Square 7-topic sub-nav |
| 2 | Brex /resources flat grid | Square homepage with 9 discovery sections |
| 3 | Brex article page (missing author, no tags) | Ramp article page (author, date, read time, editor, related articles, testimonials) |
| 4 | Brex article page (no related content) | Apple article page (identical template across 20+ years) |
| 5 | Ramp.com/tools returning 404 | Brex prototype showing organized tools hub |
| 6 | Brex abandoned podcast section | Ramp clean blog (no dead weight) |
| 7 | Brex rigid one-category URLs | Apple archive with 30+ combinable topic filters |

### The Competitive Urgency Slide

Show three things next to each other:
1. **Ramp's blog** — organized, consistent, with customer testimonials on every page
2. **Capital One's Tech Blog** — enterprise-grade with persistent sub-nav
3. **Brex's resources** — flat grid, abandoned sections, inconsistent templates

*"Our main competitor and our acquirer both have better content architecture than we do."*

### The Design Credibility Slide

Show logos and one-line summaries:
- **Apple** — 30+ topic filters, identical article templates for 20+ years
- **Nike** — Editorial series as content brands, sub-nav with search
- **Square** — Persistent 7-topic sub-nav, dual-layer taxonomy, tools integration
- **Capital One** — 4 specialized hubs, rich metadata, strategic pillar organization
- **Ramp** — 17 categories, consistent articles, customer proof on every page
- **Brex** — ???

*"Every company we admire and every company we compete with has invested in this. We should too."*

---

## Summary

These enhancements make Brex's resources experience consistent, discoverable, and technically sound — while staying within the existing design system. Every change is grounded in proven patterns from companies with world-class content architecture, and every change is built by GrowthX with minimal internal effort required.

**Next step:** Review this document and the [live prototype](https://brex-hub.onrender.com/resources), then share feedback directly in this doc or via Slack.

---

*Prepared by GrowthX | February 2026*
