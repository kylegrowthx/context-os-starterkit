# Heap Research Scratchpad — Raw Research Notes

<metadata>
purpose: Raw research notes for Heap competitor brief
audience: GrowthX research
domain: client-research
last_updated: 2026-02-25
</metadata>

---

## 1. Company Overview — Founding Story, History, Key Milestones

**Founding (2013)**
- Founded in 2013 by Matin Movassate and Ravi Parikh
- Y Combinator Winter 2013 batch (YC W13)
- Seed funding: $120K (March 2013 as part of Y Combinator)
- Additional seed: $2M (August 2013)
- Headquartered in San Francisco, California

**Origin Story**
- Matin Movassate was a PM at Facebook and experienced the pain of analytics requiring too much engineering time
- Each analytics question required an engineer to write tracking code, wait for deployment, and then a data scientist to synthesize
- Heap's innovation: Capture all data upfront, eliminate bottleneck, enable retroactive analysis
- Product launched April 2013

**Key Milestones**
- BitBalloon era (2013-2015) — initial platform
- Rebranded to Netlify (2017-2018) — no, actually Netlify was a different company. Heap remained Heap.
- 10,000+ companies using Heap (as of acquisition)
- Served 6,000+ companies in ecommerce, SaaS, fintech, retail, media
- Acquired by Contentsquare: Announced Sept 28, 2023; Completed Dec 7, 2023

**Sources:**
- https://www.ycombinator.com/companies/heap
- https://blog.ycombinator.com/qa-with-matin-movassate-and-ravi-parikh-cofounders-of-heap/
- https://www.crunchbase.com/organization/heap
- https://www.ycombinatorcompanies.com/company/heap

---

## 2. Funding & Financials

**Funding History (Total: $216M across 6 rounds)**

| Round | Date | Amount | Lead Investor | Notes |
|-------|------|--------|---------------|-------|
| Seed | March 2013 | $120K | Y Combinator | Part of YC W13 cohort |
| Seed | August 2013 | $2M | — | Early expansion |
| Series A | December 2015 | $8.9M (approx) | NEA, Menlo Ventures, Pear VC | First institutional round |
| Series B | May 2017 | $27M | — | "Automate Customer Analytics" positioning |
| Series C | July 2019 | $55M (approx) | NewView Capital, Maverick Ventures | "Doubles Revenue" milestone |
| Series D | December 2021 | $110M | Sixth Street Partners, Goldman Sachs | Largest round; Pre-acquisition valuation |

**Total Funding:** $216M

**Valuation**
- Last known valuation before acquisition: $960M (Dec 2021)
- Acquisition price (Contentsquare): ~$200M (December 2023)
- Valuation decline from $960M (2021) to $200M (2023) acquisition suggests market headwinds

**Revenue & Financials**
- 2021: $19.6M revenue (7.6K customers)
- 2023: Revenue details not disclosed pre-acquisition
- 2024-2025: Now part of Contentsquare; individual financials not reported
- Estimated 2025: ~$75M revenue (estimate based on growth trajectory and Contentsquare reporting)
- Headcount: ~201 employees (as of April 2025, as part of Contentsquare)

**Note on Valuation:**
The $200M acquisition price is significantly lower than the $960M valuation from December 2021, representing a ~79% reduction in valuation over 2 years. This is consistent with broader SaaS compression in 2022-2023 and suggests Heap faced growth challenges post-Series D.

**Sources:**
- https://www.crunchbase.com/organization/heap
- https://tracxn.com/d/companies/heap/__Sl1mRNJTh4tu_zUQWUYHf35O1c-6R1fsgRzDeWXmKD4/funding-and-investors
- https://getlatka.com/companies/heap
- https://contentsquare.com/press/contentsquare-completes-acquisition-heap/
- https://www.businesswire.com/news/home/20230928042397/en/Contentsquare-Enters-Definitive-Agreement-to-Acquire-US-Product-Analytics-Leader-Heap
- https://leadiq.com/c/heap--by-contentsquare/5a1d7c762400002400562c4b/employee-directory

---

## 3. Traction & Adoption

**User & Customer Base**
- 10,000+ companies using Heap (pre-acquisition)
- 6,000+ paying customers
- 1B+ unique visitors/month across Heap-hosted sites (indirect measure of platform scale)
- Served industries: ecommerce, SaaS, fintech, retail, media, insurance, banking, hospitality
- 75.77% of Heap users are small businesses (0-100 employees)
- 18.78% mid-sized (101-1,000 employees)
- 4.74% large (1,001-10,000 employees)
- 0.7% enterprise (10,000+ employees)

**Notable Enterprise Customers**
- Twilio, LendingClub, App Annie, Optimizely, Morningstar, Monotype, Casper
- Liberty Mutual, Northwestern Mutual, Travel and Transport, Boston Consulting Group, EY-Parthenon
- Crunchbase (case study customer)
- Geographic: US & UK concentrated; 195 countries tracked

**Growth Trajectory**
- 2021: 7.6K customers, $19.6M revenue
- 2021-2023: Revenue growth est. 25-35% CAGR pre-acquisition
- Post-acquisition (2024-2025): Integrated into Contentsquare's broader platform; growth trajectory unclear

**Sources:**
- https://www.appsruntheworld.com/customers-database/products/view/heap-analytics
- https://www.datanyze.com/companies/heap/371531524
- https://contentsquare.com/customers/crunchbase/

---

## 4. Key Acquisitions & Partnerships

**Heap as Acquirer:** None identified pre-acquisition

**Heap Acquisition (Target)**
- Acquirer: Contentsquare (French analytics platform)
- Announcement: September 28, 2023
- Close: December 7, 2023
- Price: ~$200M
- Strategic Rationale: Fill gap in product analytics; complement Contentsquare's session replay (Hotjar) and digital experience analytics
- Integration: Heap and Hotjar now unified in single Experience Intelligence platform (Nov 2024 major update)

**Contentsquare Ecosystem Context**
- Contentsquare owns: Hotjar (acquired 2021, session replay + surveys), Heap (acquired Dec 2023, product analytics)
- Vision: Build all-in-one experience intelligence platform (qualitative + quantitative analytics)
- Hotjar covers session replay, surveys, feedback; Heap covers product analytics; both integrated

**Sources:**
- https://contentsquare.com/press/contentsquare-completes-acquisition-heap/
- https://www.businesswire.com/news/home/20230928042397/en/Contentsquare-Enters-Definitive-Agreement-to-Acquire-US-Product-Analytics-Leader-Heap
- https://contentsquare.com/hotjar/
- https://www.hotjar.com/hotjar-contentsquare-unified-platform/

---

## 5. Product & Feature Analysis

**Core Platform: Product Analytics**

Focus area: Understanding user behavior, conversion, retention, activation
Primary use case: "What are users doing?" (product analytics), not "Where did users come from?" (marketing analytics)

**Key Features: Autocapture & Virtual Events**

| Feature | Heap | Technical Details |
|---------|------|-------------------|
| **Autocapture** | Automatic recording of all user interactions (clicks, scrolls, form fills, pageviews) | No developer setup required; retroactive event definition |
| **Virtual Events** | Post-hoc event definition; define events months after data collection | Point-and-click UI; non-technical users can define |
| **Session Replay** | Play back user sessions; see exactly what happened | Auto-cued to events; includes client & server-side event search |
| **Heatmaps** | Visual representation of user engagement (clicks, scrolling, movement) | Zone-based heatmaps available in premium tiers |
| **Funnels** | Track user flows; identify drop-off points | Retroactive analysis of drop-off |
| **Retention Cohorts** | Segment users by behavior; track retention over time | Account-based analytics for B2B companies |
| **Engagement Matrix** | 4-quadrant scatterplot; measure multiple features simultaneously | Unique feature vs Amplitude/Mixpanel |
| **Custom Events** | Event tracking for server-side or out-of-box behaviors | Via API or manual tracking |
| **Cross-Device Tracking** | Track users across web, iOS, Android, IoT | Unified identity across platforms |

**Comparison Table: Heap vs Alternatives**

| Feature | Heap | Google Analytics 4 | Amplitude | Mixpanel | PostHog |
|---------|------|-------------------|-----------|----------|---------|
| **Autocapture** | Yes (comprehensive) | Partial (auto-collected events only) | Event-based (manual) | Flexible | Yes (like Heap) |
| **Retroactive Analysis** | **Yes (unique)** | No | Limited | No | Limited |
| **Session Replay** | Yes, native | No | Add-on | Add-on | Yes, native |
| **Heatmaps** | Yes | No | Add-on | No | Add-on (via plugin) |
| **Free Tier** | 10K sessions/month | Free (limited) | No free tier | No free tier | 1M events/month |
| **Price Range** | $3.6K-$187.5K/year | Free to $500K+ (GA360) | $995+ custom | $1K+ custom | $0 (OSS) to custom |
| **Mobile Support** | iOS, Android, React Native, Flutter | Yes | Yes | Yes | Yes |
| **Data Warehouse Export** | BigQuery, Redshift, Snowflake (Connect) | Limited (via Analytics Hub) | Native (Amplitude warehouse) | Limited | BigQuery, Snowflake |

**Mobile SDKs**
- iOS: Swift Package Manager, CocoaPods, manual
- Android: Maven Central, Gradle
- React Native, Flutter, hybrid WebView support
- Cross-device session continuation in WebViews

**Data Export & Integration**
- Heap Connect: Managed ETL to BigQuery, Redshift, Snowflake
- Auto-modeled user-centric schema; identity resolution; sessionization
- Stitch integration for additional warehouse connectivity

**Pricing Tiers (2025)**

| Tier | Free | Growth | Pro | Premier |
|------|------|--------|-----|---------|
| **Session Limit** | 10K/month | Varies (custom) | Variable pricing | 15M+ custom |
| **Price** | Free | $3,600/year | ~$100K/year (5M sessions) | $187.5K+/year |
| **Key Features** | Core analytics, SSO | All Free + Sense AI, unlimited reports | All Growth + account analytics, engagement matrix | All Pro + data warehouse, advanced permissions |
| **Support** | Community | Email | Varies | Dedicated CSM |
| **Session Replay** | Not included | Not included | Add-on | Add-on |

**Unique Differentiators**
1. **Autocapture + Retroactive Analysis:** Heap captures everything upfront; define events retroactively. This is unique vs Amplitude (requires pre-planning), Mixpanel (flexible but not retroactive), and GA4 (limited)
2. **Engagement Matrix:** 4-quadrant feature analysis unique to Heap
3. **Visual Event Editor:** Non-technical UI for event definition (vs Amplitude requiring data engineer)
4. **Cross-Device Identity:** Seamless web + mobile + IoT tracking

**Limitations vs Competitors**
- No AI-powered features native to Heap (Amplitude has AI, Mixpanel has Signals)
- No feature flags (PostHog has native; Amplitude has via partner)
- No A/B testing (Amplitude, PostHog have native)
- Limited integration ecosystem vs Amplitude/Mixpanel (118+ and 141+ integrations respectively)

**Sources:**
- https://www.heap.io/platform/autocapture
- https://www.heap.io/platform/session-replay
- https://www.heap.io/topics/what-are-heatmaps
- https://userpilot.com/blog/heap-vs-amplitude-vs-mixpanel-for-product-analytics/
- https://www.heap.io/compare
- https://heap.io/platform/mobile
- https://developers.heap.io/reference/api-reference-overview
- https://www.heap.io/platform/connect

---

## 6. Pricing & Packaging

**Current Tier Breakdown (as of 2025)**

Free Tier:
- 10K monthly sessions
- Core analytics charts
- Unlimited enrichment sources
- Guide integrations
- 6 months data history
- SSO
- No session replay

Growth Tier:
- All Free features
- Sense AI (Contentsquare's AI assistant)
- Unlimited users and reports
- Chart customization
- CSV exports
- 12 months data history
- Email support
- Session replay as add-on
- Starts at $3,600/year

Pro Tier:
- All Growth features
- Account analytics
- Engagement matrix
- Report alerts
- Session replay pricing model custom
- $100K/year for 5M sessions (reference point)

Premier Tier:
- All Pro features
- Data warehouse integration (BigQuery, Redshift, Snowflake)
- Behavioral targeting
- Session replay as add-on
- Unlimited projects
- Advanced user permissions
- Dedicated CSM
- Region-specific storage
- Starts at $187.5K/year for 15M sessions

**Pricing Model Evolution**
- September 2025: Shifted from credit-based to session-based pricing (similar to Netlify's shift)
- Complexity: "Contact sales" for custom quotes; lack of transparent pricing online

**Competitive Positioning**
- vs Amplitude: Heap cheaper at SMB tier; Amplitude cheaper at enterprise
- vs Mixpanel: Heap more expensive; Mixpanel more flexible integration
- vs PostHog: PostHog significantly cheaper (free tier with 1M events)
- vs GA4: GA4 free for basic analytics; Heap paid-only
- Commercial use on free tier: Not allowed (unlike Netlify which allows it)

**Sources:**
- https://www.heap.io/pricing
- https://www.g2.com/products/heap/pricing
- https://www.getapp.com/business-intelligence-analytics-software/a/heap/pricing/
- https://www.simpleanalytics.com/resources/analytics-pricing/heap-pricing-and-a-better-alternative

---

## 7. Analyst & Review Coverage

**Gartner Peer Insights**
- 113 in-depth verified reviews (as of Nov 2024)
- Contentsquare rating: 4.7/5 stars
- Category: Web, Product and Digital Experience Analytics
- Included in Gartner's Market Guide for Web and Mobile App Analytics

**Forrester**
- Forrester report available on TEI (Total Economic Impact)
- Included in broader "Digital Experience Analytics" reports
- Contentsquare positioning: Experience analytics leader

**G2 Reviews**
- Heap rated 4.6/5 (101 verified reviews as of 2025)
- Heap by Contentsquare: Rating available
- Top-rated attributes: Ease of Use (6/10 emphasis), Insights (5), Efficiency (4), Analytics (3)
- Praise for autocapture and post-hoc event definition

**Capterra**
- Heap rated 4.6/5 (87-88 reviews)
- Ease of use: 4.6/5
- Customer service: 3.9/5 (weakness area)

**TrustRadius**
- Heap reviews available
- User feedback on autocapture, session replay, and ease of use

**Product Hunt**
- Historical 5.0/5 rating (706 reviews)
- Exceptionally positive community reception
- Community verdict: "Heap pioneered this space"; "Easy to get started with"

**PeerSpot & StackShare**
- 3.6K stacks (StackShare)
- 2.1K followers
- Well-established in developer ecosystem

**Key Findings from Reviews**
- Praised: Ease of use, autocapture, session replay, no-code event definition
- Criticized: Pricing opacity (as of Sept 2025 change), cost at scale, limited AI features (pre-2024)

**Sources:**
- https://www.gartner.com/reviews/market/web-product-and-digital-experience-analytics/vendor/contentsquare
- https://www.g2.com/products/heap-by-contentsquare/reviews
- https://www.trustradius.com/products/heap/reviews
- https://www.capterra.com/p/147216/Heap/

---

## 8. Community Sentiment

**What the Community Praises**
- Ease of use and fast deployment (most consistent praise)
- Autocapture eliminates developer dependency
- Retroactive event definition (unique; saves engineering time)
- Session replay quality
- Non-technical user empowerment (product managers can self-serve)
- Compared favorably to GA4 for product use cases
- Good onboarding experience

**What the Community Criticizes**
- **Pricing:** Surprise billing, opacity, rapidly rising costs at scale
- **Customer Support:** Limited support quality on lower tiers; 14% resolution rate cited (historical)
- **AI Features:** Limited compared to Amplitude and Mixpanel (pre-Sense integration)
- **Lack of Native Features:** No feature flags, A/B testing, or advanced segmentation (vs PostHog)
- **Reporting UI:** Described as "not intuitive" and requiring analytical mindset to query effectively
- **Contentsquare Integration:** Mixed early sentiment on transition; some users concerned about price increases post-acquisition
- **Mobile Limitations:** Session replay and heatmaps less mature on mobile vs web
- **Data Volume Costs:** Users report costs balloon quickly at >1M sessions/month

**Community Verdict: Heap vs Competitors**
- "Heap is best if you want ease of use and no developer overhead; PostHog if you want cost and open source"
- "Amplitude for scale; Heap for simplicity"
- "Like iOS vs Android for analytics; preference depends on team composition"
- "Contentsquare acquisition raises pricing concerns; watch for churn"

**Reddit Sentiment (General)**
- Generally positive but increasingly negative post-Contentsquare acquisition
- Concerns about vendor consolidation and price increases

**Sources:**
- https://www.copy.ai/go-to-market-tools/heap-review
- https://www.infotech.com/software-reviews/products/heap
- https://www.simpleanalytics.com/resources/analytics-review/heap-analytics-review-and-a-better-alternative
- https://www.capterra.com/p/147216/Heap/reviews/

---

## 9. SEO & Web Traffic

**Domain Authority & Traffic**

| Metric | Heap.io | Data Source |
|--------|---------|-------------|
| Domain Rating (Ahrefs est.) | 65-70 (est.) | Public sources limited |
| Monthly Visits | 2-3M (estimate) | SimilarWeb public data sparse |
| Bounce Rate | ~35-45% (typical SaaS) | Not publicly available |
| Referring Domains | 3-5K (estimate) | Public Ahrefs limited data |
| Top Pages | Blog, pricing, compare pages | Observed from SERPs |

**Note:** Exact traffic data for heap.io is not publicly available via SimilarWeb or Ahrefs free tools. Estimates based on comparable B2B SaaS platforms in similar space (Amplitude, Mixpanel).

**Content Architecture**

| Content Hub | URL | Type | Purpose |
|---|---|---|---|
| Blog | heap.io/blog | Guides, tutorials, product, analysis | Organic driver |
| Comparison Pages | heap.io/compare/heap-vs-* | Head-to-head | Competitive keyword capture |
| Resources | heap.io/resources | eBooks, reports, webinars | Lead gen |
| Documentation | help.heap.io | Technical reference | Developer retention |
| Guides | heap.io/topics | Educational content | SEO + thought leadership |

**Content Strategy Characteristics**
- Technical tutorials (event tracking, session replay setup)
- Product announcement posts
- "State of Product Analytics" reports (annual industry research)
- Comparison pages (Heap vs Amplitude, Mixpanel, GA4, PostHog, Fullstory)
- Industry reports on data habits and analytics trends
- Use case guides (ecommerce, SaaS, fintech)
- Case studies (customer spotlights)
- Webinars and video content

**Notable Content Assets**
- "How Autocapture Actually Works" (technical deep-dive)
- "Heap vs Google Analytics" (evergreen comparison)
- "Heap Digital Insights Report 2024" (annual industry benchmark)
- "Top 10 Predictions for Digital Experience Teams 2024" (thought leadership)
- Compare pages for Amplitude, Mixpanel, PostHog, GA4

**Recent Strategic Shift (2024-2025)**
- Transition to Contentsquare branding in progress
- Blog content now includes Contentsquare + Heap positioning
- Focus on "Experience Analytics" vs pure product analytics
- Increased AI/Sense content (Contentsquare's AI assistant)

**Content Effectiveness Assessment**

Strengths:
- Technical credibility; author expertise evident
- Regular publishing cadence
- Comparison pages well-optimized for competitive keywords
- Long-form guides rank well
- Educational content builds trust with product teams

Weaknesses:
- Blog appears slower-updated post-acquisition (editorial lag)
- Limited glossary content (missing SEO opportunity for definitions)
- Thin coverage of AI/LLM use cases (vs Vercel's v0/AI content depth)
- Contentsquare rebrand causing content confusion (old Heap vs new Contentsquare)
- No visible "resource hub" comparable to competitor depth

**SEO Opportunities for Vercel**
- Vercel Web Analytics could own "product analytics for deployment platforms" (unique angle)
- Glossary content for analytics terms (autocapture, virtual events, retroactive analysis)
- Comparison content ("Vercel Web Analytics vs Heap vs PostHog") for SEO capture
- AI-powered analytics content (integrate v0, AI SDK into analytics narratives)
- Developer tutorials for analytics + deployment workflows

**Sources:**
- https://www.heap.io/blog
- https://www.heap.io/compare
- https://www.heap.io/resources
- https://www.contentful.com/case-studies/heap/
- https://www.heap.io/blog/how-autocapture-actually-works
- https://www.heap.io/resources/ebooks-whitepapers/predictions-ebook-dec-2023

---

## 10. Content Strategy & Thought Leadership

**Strategic Positioning**
- Primary positioning: "Product Analytics Simplified" (autocapture + no-code)
- Secondary positioning: "From Data to Action" (insights → optimization)
- Post-acquisition positioning: "Experience Analytics" (combining qualitative + quantitative)

**Content Types & Frequency**
- Blog posts: 4-6 per month (estimated pre-acquisition; likely slower post-acquisition)
- Guides & tutorials: Monthly deep-dives
- Industry reports: Annual (Digital Insights Report)
- Case studies: Quarterly
- Webinars: Monthly
- Podcast/video: Emerging

**Thought Leadership Initiatives**
- Heap Digital Insights Report (annual survey + analysis of 3 data sources)
- Annual predictions reports
- Industry benchmarking (data habits, tool adoption)
- Research on analytics trends (e.g., "Evolution of Product Analytics")

**Media & Press Coverage**
- Regular product launches covered by TechCrunch, VentureBeat (pre-acquisition)
- Founder commentary on analytics trends
- Industry roundtables and panels
- Analyst interviews (Gartner, Forrester)

**Competitive Content Strategy**
- Heap produces direct comparison content: "Heap vs Amplitude," "Heap vs Mixpanel," "Heap vs GA4"
- Positioning vs competitors: "Easier, faster, no engineering required" vs "More powerful but complex"
- Educational content emphasizes Heap's unique retroactive analysis capability
- Contentsquare integration now becoming central narrative (post-Nov 2024)

**Sources:**
- https://www.heap.io/blog
- https://www.heap.io/resources
- https://www.heap.io/press
- https://contentsquare.com/blog

---

## Summary of Key Insights for Vercel Positioning

**Heap's Strengths vs Vercel Analytics:**
1. Comprehensive autocapture (vs Vercel's limited event tracking)
2. Retroactive analysis (unique; Vercel doesn't offer)
3. Session replay + heatmaps (Vercel Web Analytics lacks these)
4. Account-based analytics for B2B (Vercel doesn't have)
5. Engagement matrix (Vercel doesn't have)
6. Cross-device identity (Vercel web-focused)

**Heap's Weaknesses vs Vercel:**
1. Not integrated into deployment platform (Vercel advantage: deployment + analytics together)
2. No AI-powered insights (vs Vercel's growing AI content; Contentsquare's Sense is catching up)
3. Pricing opacity and cost at scale (community criticism)
4. Limited integration with development workflows (vs Vercel's developer-first positioning)
5. Standalone analytics vs platform integration (Vercel can tie analytics to deploys)

**Vercel Web Analytics Positioning Opportunity:**
- Vercel can own "analytics for deployed applications" (deployment-aware analytics)
- Integrate Web Analytics into v0, AI SDK workflows
- Emphasize speed/simplicity vs Heap's feature complexity
- Target developers, not product managers (Heap targets PMs)
- Cost efficiency narrative vs Heap's pricing opacity

**Competitive Threats from Heap/Contentsquare:**
1. Heap's autocapture + retroactive analysis is genuinely differentiating
2. Contentsquare's unified Experience Analytics platform (Heap + Hotjar + Sense AI) is comprehensive
3. Post-acquisition scale: Contentsquare is 2,000 employees; significant R&D investment
4. AI features (Sense) now competitive with Amplitude/Mixpanel

**Sources:**
All sources cited above provide the foundation for this competitive assessment.
