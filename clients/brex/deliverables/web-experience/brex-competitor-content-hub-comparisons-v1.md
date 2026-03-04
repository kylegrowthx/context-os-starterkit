# Competitor Content Hub Comparisons
**For Brex Web Experience Strategy | February 2026**

<metadata>
purpose: Benchmark examples of how leading companies organize content/editorial hubs, for use in CDO presentation
audience: Brex Chief Design Officer, internal stakeholders
summary: Detailed analysis of Ramp, Capital One, Apple, Nike, and Square content hub design patterns mapped to proposed Brex improvements
domain: client-work, strategy
confidence: high
context_tier: 2
last_updated: 2026-02-23
</metadata>

---

## Why These Five Companies

| Company | Why It Matters |
|---------|---------------|
| **Ramp** | Brex's primary competitor — their content strategy directly targets Brex customers. Creates competitive urgency. |
| **Capital One** | Acquiring Brex — their content architecture is the ecosystem Brex will integrate into |
| **Apple** | CDO benchmark for design excellence — clean taxonomy, premium editorial quality |
| **Nike** | CDO benchmark for brand storytelling — magazine-quality editorial with clear categorization |
| **Square** | Direct fintech peer — "The Bottom Line" is the gold standard for B2B content hubs |

---

## 1. Ramp — Blog & Velocity (Direct Competitor)

**URLs:**
- Blog: [ramp.com/blog](https://ramp.com/blog)
- Velocity (premium hub): [ramp.com/velocity](https://ramp.com/velocity)
- Customers: [ramp.com/customers](https://ramp.com/customers)
- Accountant Directory: [accountants.ramp.com](https://accountants.ramp.com)

### Content Architecture

Ramp runs a **dual-hub design** — the Blog as a broad content hub and Velocity as a premium editorial property. They chose to consolidate rather than fragment: `/resources` redirects to `/blog`. No separate resources page.

| Property | Design Feel | Audience |
|----------|------------|----------|
| **Blog** | Clean, functional, category-driven — feels like a well-organized content library | Finance teams, operations |
| **Velocity** | Premium editorial — generous whitespace, magazine-style layouts, data-driven visuals | CFOs, finance leaders |
| **Customers** | Social proof showcase — headshot + quote cards, clean grid layout | Prospects evaluating Ramp |

### Key Design Patterns

**Navigation & Wayfinding:**
- Blog uses a clear category navigation with 17 topics — each category page is a mini-hub with a featured article hero and paginated archive grid
- Velocity takes a simpler approach: 4 filter tabs (AI, Data, Finance, Culture) across the top
- "Helpful resources" section on the blog homepage surfaces key content types (Alternatives, Business Credit Cards, Accountant Directory) as a lightweight secondary navigation
- **The gap:** No sub-navigation bar or visual thread connecting Blog, Velocity, Customers, and Tools. Each feels like a standalone property. There's no persistent element tying them into a cohesive ecosystem.

**Article Page Template:**
- Consistent and clean across all articles: author name with title and headshot, publish date, read time at top
- Editor attribution at the bottom — a credibility detail most competitors skip
- "Don't miss these" module at the bottom of every article (3 related articles with category tags and thumbnails)
- Customer testimonials carousel on every article page — 6-8 rotating customer quotes with photos, titles, and "Read customer story" CTAs. This is a strong design choice: social proof is baked into the reading experience, not siloed on a separate page.
- **What's missing:** No table of contents on long-form articles (some are 5,000+ words). No visible topic tags on the article page itself — tags only appear on category index pages. No sticky sidebar navigation.

**Visual Design Quality:**
- Typography is clean and readable with generous line height and comfortable paragraph widths
- Cards use consistent formatting: category label, title, and clean hover states
- Velocity has a noticeably more premium feel — larger type, more breathing room, editorial photography
- Blog is functional but not remarkable — text-heavy articles with minimal data visualization or custom imagery
- Overall: polished and professional, but not pushing design boundaries. More "well-executed content platform" than "editorial destination."

**Tools & Calculator Pages:**
- Calculator pages (Per Diem, Mileage Reimbursement, Business Startup Costs) are well-designed individually — interactive inputs, clean data tables, related blog articles at the bottom
- **The design problem:** No centralized tools hub. `/tools` returns 404. Calculators live at inconsistent URLs (`/per-diem-calculator`, `/calculator/business-startup-costs`, `/tools/meeting-cost-calculator`). Users can only find tools through blog articles or search — there's no browsable tools experience.

### What's Relevant to Brex

| Ramp Design Pattern | Brex Proposal It Supports |
|---------------------|--------------------------|
| No sub-nav connecting content properties | **Sticky sub-nav** — Ramp's Blog and Velocity feel like separate sites. A persistent sub-nav connecting all of Brex's content types would create a more cohesive experience than anything Ramp has. |
| Clean, consistent article template with author + editor attribution | **Article page standardization** — Ramp treats template consistency as table stakes. Every article has author, date, read time, editor credit, related content, and social proof. Brex's inconsistent pages are the outlier. |
| Customer testimonials baked into every article | **Social proof integration** — Embedding customer stories throughout content (not just on a case studies page) is a design pattern worth adopting. |
| No table of contents on long articles | **Sticky TOC** — Brex can offer a better reading experience on long-form content. Ramp's 5,000+ word articles have no in-page navigation. |
| No centralized tools hub (404 on /tools) | **Build a `/tools` hub page** — Ramp's biggest UX gap. Their tools are well-designed individually but impossible to browse or discover. Brex aggregating tools in a single, filterable page is a direct design advantage. |
| Dual-property approach (Blog + Velocity) | **Premium content separation** — Validates creating distinct visual experiences for different audiences. Velocity's editorial treatment elevates the content. |
| 17 category hub pages with featured content | **Topic hub architecture** — Clear, well-labeled category pages with hero content and browse-able archives. A design pattern Brex should adopt. |

### Competitive Urgency

Ramp's design team is investing in content experience. Their article pages are more consistent than Brex's. Their category navigation is cleaner. Their customer social proof is woven throughout — not isolated on a single page. The areas where they fall short (no sub-nav, no tools hub, no TOC) are exactly the areas where Brex can leapfrog them. But the baseline quality is high — Brex's current fragmented, inconsistent experience doesn't match up.

---

## 2. Capital One — Insights Center & Tech Blog

**URLs:**
- Insights Center: [capitalone.com/about/insights-center](https://capitalone.com/about/insights-center)
- Tech Blog: [capitalone.com/tech/blog](https://capitalone.com/tech/blog)
- Commercial Insights: [capitalone.com/commercial/insights](https://capitalone.com/commercial/insights)

### Content Architecture

Capital One runs **multiple specialized content hubs** rather than a single unified publication:

| Hub | Audience | Content Type |
|-----|----------|-------------|
| **Insights Center** | Policymakers, community leaders, researchers | Data-driven research reports, studies |
| **Tech Blog** | Engineers, technologists | Technical deep-dives, AI/ML, engineering culture |
| **Commercial Insights** | Business banking clients | Industry analysis, payment trends, operational advice |
| **Business Hub** | Small business owners | Practical guides, "Masters of Scale" partnership series |

### Key Design Patterns

**Navigation:**
- Top-level nav on the corporate site (About → Insights Center, Tech → Blog)
- Tech Blog has its own dedicated sub-navigation: Tech | AI | Our Stack | Blog | Careers | Research | Publications | Academia
- Insights Center uses a simpler card-grid layout with "Load more" pagination

**Content Organization:**
- Research organized by **three strategic pillars**: Inclusive Society, Thriving Communities, Financial Tools
- Tech Blog uses **topic-based categorization**: Software Engineering, AI, Culture, Publications
- Commercial Insights organized by **industry vertical** (real estate, healthcare, nonprofits)

**Article Pages:**
- Publish dates and read times on tech blog
- Featured/hero article treatment at top of each hub
- "Load more" progressive loading (not traditional pagination)
- Author attribution on tech blog posts

### What's Relevant to Brex

| Capital One Pattern | Brex Implication |
|-------------------|-----------------|
| Multiple specialized hubs with different nav structures | **Post-acquisition risk** — Brex content will need to integrate into this multi-hub model. Making Brex's content architecture clean NOW makes integration smoother. |
| Topic-based sub-navigation on Tech Blog | Validates the **sticky sub-nav** proposal — Capital One already does this for their tech content. |
| Strategic pillars organizing the Insights Center | Supports **hub-and-spoke by topic/persona** — Capital One groups content by audience need, not just format. |
| "Load more" instead of traditional pagination | Common pattern across all four companies — Brex should adopt this. |

### Acquisition Angle

Capital One's content ecosystem is mature and well-structured. Brex's current fragmented experience would stick out as inconsistent within the Capital One family. Fixing the web experience now = smoother integration later and demonstrates design leadership to the acquiring team.

---

## 3. Apple — Newsroom

**URL:** [apple.com/newsroom](https://www.apple.com/newsroom/)

### Content Architecture

Apple's Newsroom is a masterclass in **restrained, premium editorial design**. Two primary content streams:

| Section | What It Contains |
|---------|-----------------|
| **Latest News** | Press releases, product announcements, company news |
| **Apple Stories** | Long-form editorial features about creators, developers, innovators |

### Key Design Patterns

**Navigation:**
- Minimal global nav — the Newsroom sits under the main Apple nav bar
- Two clear entry points: Latest News and Apple Stories
- "View All" links for each section lead to dedicated archive pages

**Filtering & Taxonomy:**
- Archive page at `/newsroom/archive/` with a **comprehensive dual-filter system**:
  - **By Topic:** 30+ tags including Accessibility, AirPods, Apple Card, Apple Intelligence, Apple Vision Pro, Business, Company News, Education, Environment, Health, iOS, iPad, iPhone, Mac, Privacy, and more
  - **By Time Period:** Filter by year (2000–2025) and month (January–December)
- Filter controls: "Filter" / "Reset" / "Done" buttons
- Filters can be **combined** (e.g., "Privacy" + "2025" + "March")
- Default view: "All Topics" / "All Years"

**Content Organization:**
- Hero/featured story treatment at the top
- Clean card grid below with consistent metadata: date, headline, thumbnail
- Apple Stories section has its own distinct visual treatment — emphasizing the human/creator angle
- Topical landing pages exist for major categories

**Article Pages:**
- Extremely consistent page template across all articles
- Date, category label, headline, subhead, body
- High-quality imagery and media embeds
- Clean typography, generous whitespace
- Related articles at the bottom via "Latest News" section

### What's Relevant to Brex

| Apple Pattern | Brex Proposal It Supports |
|--------------|--------------------------|
| Dual-filter archive (topic + date) | **Flexible multi-tag taxonomy** — Apple proves that rich filtering on a content archive works at scale. Brex's rigid one-to-one URL structure is the opposite of this. |
| Combined filters creating specific views | **Indexable filter states** — Apple's archive lets you drill into "Privacy + 2024" as a viewable, linkable state. Brex's filter states aren't indexable. |
| Consistent article page template | **Standardized page experience** — Every Apple Newsroom article looks and feels the same. Date, category, headline, body, related. No randomness. |
| Clear two-stream architecture | **Sub-nav clarity** — Apple doesn't mix press releases with human stories. They're clearly separated but connected. Brex mixes blog, resources, and spending trends with no clear boundaries. |
| "View All" entry points | **2-click taxonomy** — From the Newsroom homepage, you're always 1-2 clicks from any content category. |

---

## 4. Nike — The Record (about.nike.com/en/stories)

**URLs:**
- The Record (editorial magazine): [about.nike.com/en/stories](https://about.nike.com/en/stories)
- Newsroom: [about.nike.com/en/newsroom](https://about.nike.com/en/newsroom)
- Nike.com Stories: [nike.com/stories](https://nike.com/stories)

### Content Architecture

Nike runs a **magazine-quality editorial operation** called "The Record" — positioned as "Stories From Inside NIKE, Inc." This is separate from both the corporate Newsroom and the consumer-facing nike.com/stories.

| Property | Purpose | Audience |
|----------|---------|----------|
| **The Record** (about.nike.com/en/stories) | Brand magazine — athletes, innovation, culture | Media, investors, brand enthusiasts |
| **Newsroom** (about.nike.com/en/newsroom) | Press releases, product launches | Press, analysts |
| **Nike.com Stories** (nike.com/stories) | Consumer inspiration, expert advice | Consumers, athletes |

### Key Design Patterns

**Navigation:**
- Corporate site nav: Stories | Impact | Company | Newsroom
- Newsroom has its own sub-nav: **Collections | Press Releases | All** with a search bar
- The Record doesn't use traditional category nav — instead uses **editorial series** as organizational units

**Content Tagging & Series:**
- Articles tagged by **editorial series** (thematic groupings):
  - "For The Win" — athlete interviews and competition stories
  - "How I Got Here" — career journey features
  - "Sport Science" — innovation and R&D stories
  - "History" — Nike heritage and archive stories
  - "Making It" — behind-the-scenes product creation
  - "Welcome to the Family" — new athlete/partner announcements
  - "The Nike Moment" — event photography and experiential content
  - "3-Minute Portrait" — short video interviews
  - "Global Football" — soccer-specific stories
- Each tag/series label appears prominently on the article card, creating **visual consistency** in the grid

**Article Pages:**
- Full-bleed hero imagery
- Series tag displayed prominently above the headline
- "View" CTA button on each card (consistent interaction pattern)
- No visible dates on The Record articles — editorial timelessness by design
- Pagination at the bottom (numbered pages, not infinite scroll)

**Visual Design:**
- Magazine-quality photography throughout
- Bold, cinematic layouts
- High contrast between featured hero and grid content
- Series tags serve as both navigation AND visual branding

### What's Relevant to Brex

| Nike Pattern | Brex Proposal It Supports |
|-------------|--------------------------|
| Editorial series as content groupings | **Content tagging by topic/theme** — Nike doesn't just tag by category, they create branded editorial series that group related stories. Brex could do this for "Spend Trends," "CFO Insights," "Startup Finance," etc. |
| Series labels on every card | **Consistent page elements** — Every card shows the series tag, headline, and "View" CTA. No randomness. Brex has articles with authors, without authors, with dates, without dates. |
| Separate properties for separate audiences | **Clear content separation** — Nike doesn't mix press releases with magazine features. Brex mixes blog posts, case studies, podcasts, and resources with unclear boundaries. |
| Newsroom sub-nav (Collections / Press Releases / All + Search) | **Sub-nav with search** — Nike's Newsroom shows exactly the pattern we're proposing: a sticky sub-nav with content type tabs + a search bar. |
| Magazine-quality visual consistency | **Design credibility** — The CDO admires Nike's design. Showing that Nike invests in consistent, premium content presentation validates investing in Brex's content UX. |

---

## 5. Square — "The Bottom Line"

**URL:** [squareup.com/us/en/the-bottom-line](https://squareup.com/us/en/the-bottom-line)

### Content Architecture

The Bottom Line is the **benchmark** for B2B fintech content hubs. It operates as a branded publication within Square's domain — a complete editorial ecosystem with multiple content types, navigation layers, and discovery paths.

### Key Design Patterns

**Sub-Navigation (The Gold Standard):**
- Persistent topic-based sub-nav across the entire publication:
  - Inside Square | Growing Your Team | Operating Your Business | Managing Your Finances | Selling Anywhere | Reaching Customers | Starting Your Business
- Every page within The Bottom Line shows this sub-nav
- You always know where you are AND what else exists

**Content Tagging System:**
- **Dual-layer taxonomy:**
  - **Primary categories** (the 7 sub-nav topics — audience/lifecycle based)
  - **Secondary tags** visible on each article: Food and Beverage, Retail, Beauty and Personal Care, Health and Fitness, Professional Services, Home and Repair, Automation, Business Growth, Cash Flow, Cybersecurity, eCommerce, Financing, Fulfillment, Inventory, Leadership, Marketing, Multiple Locations, Staff Retention, Taxes, Trends
- Articles display **multiple tags** — an article can be tagged "Operating Your Business" + "Inventory" + "Cash Flow"
- Each tag is clickable and links to a **tag hub page** showing all content with that tag
- "Explore Topics" section on the homepage surfaces all available tags

**Collections & Series:**
- **Collections** = curated article groups (e.g., "Smart Banking for New Business Owners," "Restaurant 201: Guide to Scaling Up," "Next-Level Growth," "Run Your Business Smarter With AI")
- **Series** = branded editorial series (e.g., "Making a Restaurant With Ggiata," "The Build," "The Way Up: A Series by Square and Guy Raz," "Running a Restaurant is No Joke")
- Both Collections and Series have their own dedicated pages and navigation

**Tools & Resources Section:**
- Dedicated `/tools` page within The Bottom Line
- Tools are tagged with the same taxonomy as articles
- Organized by: Featured Tools → Tools by Topic → Tools by Industry (Food & Beverage / Retail / Beauty)
- Content types: downloadable templates, calculators, checklists, toolkits
- Filterable: "All 43 | Cash Flow 23 | Business Growth 22 | Taxes 5 | Inventory 4..." with counts
- Quick downloads section for immediate access

**Homepage Layout (Discovery Architecture):**
- Featured Series (hero)
- Latest articles with category labels, author, date, read time
- Topic-based content sections ("Operating Your Business," "Inside Square") with "View all" links
- Editor's Picks (curated)
- Featured Series carousel (4 series with expand/collapse)
- Video section with featured video series
- Podcast Episodes section
- "Explore Topics" tag cloud
- Featured Contributors (author profiles with bios)
- Most Recent (chronological)

**Article Metadata (Consistency):**
- Every article shows: Category label, headline, author (linked to author profile), date, read time
- Author profiles exist with bios and "See all articles" links
- Multiple tags displayed per article

**Filtering & Browse:**
- Tag hub pages show article count per tag
- "Load more articles" progressive loading
- "See archives" link for older content
- Tools page has topic-based filtering with visible counts

### What's Relevant to Brex

| Square Pattern | Brex Proposal It Supports |
|---------------|--------------------------|
| Persistent 7-topic sub-nav | **Sticky sub-nav** — This IS the pattern we're proposing. Always visible, ties everything together. Brex has nothing connecting Blog, Resources, and Spending Trends. |
| Multi-tag taxonomy with tag hub pages | **Flexible tagging with hub pages** — Articles tagged to multiple categories, each tag has its own browsable page. Brex's rigid URL structure limits articles to one category. |
| Consistent article metadata | **Standardized page elements** — Every article: category, author, date, read time. No exceptions. Brex has articles with and without authors, with and without dates. |
| Collections + Series | **Content grouping beyond categories** — Curated bundles and branded series create additional discovery paths. Brex has nothing like this. |
| Tools section with same taxonomy | **Tools integrated into the content ecosystem** — Square's tools live within The Bottom Line and share the same tagging system. This is exactly what we're proposing for Brex's tools hub. |
| Topic filtering with counts | **Transparent filtering** — Users see "Cash Flow 23" and know there are 23 pieces of content. Builds confidence in content depth. |
| Featured Contributors section | **Author/expert credibility** — Named contributors with profiles and bios. Supports Brex building thought leadership credibility. |
| Editor's Picks + curated sections | **Multiple discovery paths** — Homepage offers 8+ ways to enter content (by topic, by series, by recency, by editor pick, by contributor). Brex offers one: a grid. |

---

## Pattern Comparison Matrix

How each company addresses the specific improvements we're proposing for Brex:

| Proposed Brex Change | Ramp | Capital One | Apple | Nike | Square |
|---------------------|------|-------------|-------|------|--------|
| **Sticky sub-nav** | None — Blog and Velocity feel disconnected | Tech Blog has dedicated sub-nav (Tech, AI, Our Stack, Blog, Careers, Research) | Minimal — relies on main Apple nav | Newsroom has Collections / Press Releases / All tabs | **Best-in-class** — 7-topic persistent sub-nav across all pages |
| **Content tagging by topic** | 17 categories on blog, but tags not visible on article pages | Organized by strategic pillars and verticals | 30+ topic tags in archive filter | Editorial series tags (For The Win, Sport Science, History, etc.) | **Best-in-class** — Dual-layer: 7 primary categories + 20+ secondary tags |
| **Content tagging by role/persona** | Implicit via Blog (teams) vs. Velocity (executives) | Different hubs for different audiences (SMB, commercial, researchers) | Not applicable | Separate properties per audience (corporate vs. consumer) | Primary nav organized by business lifecycle stage (Starting → Growing → Operating) |
| **Consistent article pages** | Strong — author, date, read time, editor on every article | Read times and dates on tech blog; inconsistent across other hubs | **Best-in-class** — Every article is identical in structure | Series tag + headline + "View" CTA on every card | Every article: category + author + date + read time |
| **Search** | Not prominent | Not prominent | Not on main Newsroom page | Search bar in Newsroom sub-nav | Not prominent on The Bottom Line |
| **Cross-linking / related content** | Strong — "Don't miss these" + customer testimonial carousel on every page | Links between hubs are limited | Related articles via "Latest News" | Series tags link to other articles in same series | **Best-in-class** — Tags, collections, series, contributors, topic hubs all interlink |
| **Breadcrumbing** | Category labels on category pages only | Category labels serve as breadcrumbs | Category labels above headlines | Series labels above headlines | Category labels on every card + sub-nav shows current section |
| **Hub pages by topic** | Yes — 17 category hub pages with featured content | Insights Center themes, commercial verticals | Topic archive pages via filter | Series landing pages | **Best-in-class** — Every tag, collection, and series has its own hub page |
| **Tools/resources section** | **No centralized hub** — calculators scattered across URLs, /tools returns 404 | Not a dedicated section | Design resources for developers | Not applicable | **Best-in-class** — Dedicated /tools section with topic + industry filtering |
| **Multiple content types** | Blog articles, customer stories, calculators, competitive comparisons | Reports, blog posts, studies | News, press releases, Apple Stories | Magazine features, videos, press releases | Articles, videos, podcasts, tools, templates, collections, series |

---

## Summary for CDO Presentation

### The Headline
Every company the CDO admires — Apple, Nike — every relevant peer — Capital One, Square — and Brex's primary competitor — Ramp — invests in structured content experiences. Brex's current fragmented approach is the outlier.

### Key Talking Points

1. **Ramp is actively targeting your audience.** Their "Alternatives" category is optimized to capture people searching for Brex alternatives. They have 17 well-organized topic categories, consistent article templates with author/editor attribution on every page, and customer testimonials embedded throughout. Their one major weakness: no centralized tools hub and no sub-nav connecting their content types. We can leapfrog them on both.

2. **Capital One already does this.** Their Tech Blog has a dedicated sub-nav. Their Insights Center is organized by strategic themes. Post-acquisition, Brex's content will need to fit within this structured ecosystem. Fixing it now demonstrates design leadership.

3. **Apple proves that premium brands demand consistent templates.** Every Newsroom article looks identical. The archive supports 30+ topic filters. There is zero randomness in the page experience. If Brex wants to be seen as a premium brand, the content experience needs to match.

4. **Nike shows how editorial series create brand value.** "For The Win," "Sport Science," "How I Got Here" — these aren't just categories, they're content brands. Brex could create similar branded series for Spending Trends, CFO insights, and startup finance content.

5. **Square is the direct blueprint.** Persistent sub-nav, multi-tag taxonomy, collections, series, tools section, contributor profiles, multiple discovery paths. This is exactly what we're proposing for Brex — and it's working for a direct fintech peer.

### The Design Argument

The CDO's job is to ensure Brex's design is world-class. Right now:
- Ramp (the direct competitor) has more organized content with better cross-linking
- Apple would never ship inconsistent page templates
- Nike would never bury their best content behind unclear navigation
- Square would never leave sections abandoned for 7+ months
- Capital One (the acquirer) already has better content architecture than Brex

Investing in the structural fixes we're proposing isn't just a growth play — it's a **design credibility** play and a **competitive necessity**.
