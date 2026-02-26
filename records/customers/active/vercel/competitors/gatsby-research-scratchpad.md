# Gatsby Research Scratchpad

## Research Date
February 25, 2026

## Executive Context
This research supports a comprehensive competitor brief for Gatsby as a competitor to Vercel in the Frontend Frameworks segment. The focus is on Gatsby's decline post-Netlify acquisition, its GraphQL data layer positioning, SSG/Jamstack focus, and how it serves as a cautionary tale vs Next.js/Vercel's continued rise.

---

## Research Questions & Findings

### 1. Company Overview & Founding Story

**Founding & Early History:**
- Founded: May 2015 by Kyle Mathews as an open-source project
- Initial problem: Building fast, secure static websites using React components
- Kyle's background: Previously worked at Pantheon (WordPress/Drupal hosting)
- 1.0 release: July 2017
- Gatsby Inc. formally established: May 2018 to commercialize the open-source framework

**Sources:**
- https://www.gatsbyjs.com/contributors/kyle-mathews/
- https://changelog.com/founderstalk/59
- https://grokipedia.com/page/Gatsby_(software)
- https://isnews.byu.edu/2020/01/mism-alumnus-kyle-mathews-helps-gatsby-raise-15-million-in-funding/
- https://www.netlify.com/blog/2016/04/18/developing-with-reactjs-an-interview-with-gatsbys-kyle-mathews/

### 2. Funding & Financial History

**Funding Rounds:**
- Seed: August 2016 — $2.1M (Bloomberg Beta, Tank Hill Ventures; angels: GitHub/Heroku/Rackspace founders)
- Series A: August 2017 — $12M (Andreessen Horowitz)
- Series B: May 2020 — $28M (Index Ventures, CRV, Trinity Ventures) — **Valuation: $200M**
- Series C: Not disclosed in search results
- Total raised: $46.8M+ before acquisition

**Netlify Acquisition (February 1, 2023):**
- Purchase price: **Not disclosed**
- Announced specifically for Valhalla Content Hub and plugin ecosystem
- All Gatsby Cloud customers migrated to Netlify Cloud with end-of-service date on November 30, 2024
- Gatsby open-source framework unaffected by acquisition

**Sources:**
- https://www.cbinsights.com/company/gatsby/financials
- https://www.crunchbase.com/organization/gatsby-2349/company_financials
- https://www.crunchbase.com/organization/gatsby-e828
- https://www.gatsbyjs.com/blog/2020-05-27-announcing-series-b-funding/
- https://www.netlify.com/press/netlify-acquires-gatsby-inc-to-accelerate-adoption-of-composable-web-architectures/
- https://techcrunch.com/2023/02/01/netlify-acquires-frontend-platform-gatsby/
- https://www.netlify.com/blog/gatsby-cloud-evolution/
- https://www.gatsbyjs.com/blog/gatsby-is-joining-netlify/
- https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/
- https://www.crunchbase.com/acquisition/netlify-acquires-gatsby-e828--38a4ab69
- https://dev.to/erinposting/netlify-acquires-gatsbyjs-4c74

### 3. Traction & Market Adoption

**Developer Metrics:**
- Weekly npm downloads: 348,449–299,934 (as of 2024-2025, variation by measurement method)
- GitHub stars: 55,953–55,961
- Maintenance status: Healthy (based on release cadence and activity)

**Historical Growth:**
- 2022: 493k weekly downloads → 2023: 428k (65k decline, ~13% drop)
- 2024: Next.js climbed to 4th place in Stack Overflow Best Web Frameworks; Gatsby didn't reach top 20
- Next.js grew to 3.95M weekly downloads (+1.6M YoY); Gatsby flat/declining

**State of JavaScript Survey Trend:**
- Likelihood of developer picking up Gatsby again: 89% (2019) → 38% (2022)
- This 51-point decline reflects post-acquisition sentiment deterioration

**Market Share Loss:**
- Next.js: 4.3M+ weekly downloads (2025)
- Gatsby: ~350k weekly downloads (2025)
- Ratio: Next.js has ~12x more downloads than Gatsby

**Sources:**
- https://npmtrends.com/gatsby
- https://github.com/gatsbyjs/gatsby
- https://www.npmjs.com/package/gatsby
- https://ikius.com/blog/end-of-gatsbyjs
- https://themobilereality.com/blog/next-js-vs-gatsby
- https://prismic.io/blog/compare-nextjs-vs-gatsby
- https://ikius.com/blog/next-js-vs-gatsby
- https://pagepro.co/blog/nextjs-vs-gatsbyjs-comparison/
- https://dev.to/lilxyzz/nextjs-vs-gatsby-in-2024-50am
- https://merge.rocks/blog/next-js-gatsby-which-framework-to-use-in-2023
- https://prateeksha.com/blog/is-gatsbyjs-dead-a-comprehensive-look-into-the-state-of-gatsby-in-2024
- https://naturaily.com/blog/next-js-vs-gatsby
- https://www.webstacks.com/blog/gatsby-vs-nextjs

### 4. Key Acquisitions & Partnerships

**Acquisitions by/of Gatsby:**
- FeaturePeek (May 2021): Deploy preview collaboration → integrated into Netlify deploy previews
- OneGraph (November 2021): GraphQL API integration → became Netlify Graph
- Gatsby Inc. acquired by Netlify (February 2023): Valhalla Content Hub + plugin ecosystem → became Netlify Connect

**Strategic Partnerships:**
- Headless CMS integrations: Contentful, Sanity, Strapi, Markdown, WordPress
- Framework ecosystem: React ecosystem focus
- Netlify integration (post-acquisition): Single sign-on, unified dashboard

**Sources:**
- https://devclass.com/2023/02/01/netlify-acquires-gatsby-inc-with-focus-on-plugin-ecosystem-and-valhalla-content-hub/
- https://www.contentful.com/marketplace/gatsby/
- https://www.gatsbyjs.com/plugins/

### 5. Product & Feature Analysis

**Core Framework:**
- Gatsby is a React-based, GraphQL-powered static site generator
- Compiles pages at build time, outputs folder of static assets serving from CDN
- GraphQL data layer: Stitches disparate data sources (CMS APIs, databases, Markdown) into unified schema
- React components with GraphQL queries declare data needs

**Key Rendering Modes:**
- Static Site Generation (SSG): All pages pre-rendered at build time
- Incremental Builds: Only rebuild changed pages/data (not available post-Netlify acquisition through Netlify without regression)
- Deferred Static Generation (DSG): Defer non-critical pages to user request (v4+)

**Build Performance Features:**
- **Incremental Builds (Gatsby Cloud)**: Build speeds under 10 seconds for data edits—1000x improvement
  - 90% reduction in build times for content-sourced sites
  - Sites with thousands of pages update in seconds, not minutes
- **Deferred Static Generation**: Non-critical pages generated on-request instead of at build time

**Plugin Ecosystem:**
- 3,000+ plugins available in Gatsby Plugin Library
- Types: source plugins (data fetching), transformer plugins (data manipulation), functional plugins (features)
- Plugin areas: Analytics, image optimization, RSS feeds, CMS integrations
- Community ecosystem: Gatsby User Collective supports plugin maintenance democratization

**Valhalla Content Hub (Acquired Feature, Now "Netlify Connect"):**
- Unified GraphQL API across multiple data sources
- Real-time GraphQL layer for Contentful, Shopify, legacy APIs, headless CMS
- Framework-agnostic (Next.js, Astro, Svelte, Remix, Gatsby supported)
- Build time improvement: Caches data so builds don't hit CMS APIs repeatedly
- Central value prop: Query once regardless of source

**Framework Integration:**
- Gatsby Cloud features not available in Netlify Cloud post-acquisition (incremental builds, edge functions)
- Netlify migration path documented but customers report feature regressions
- Serverless functions: JavaScript/TypeScript/Go with limited execution time
- Image optimization: On-demand transforms via Netlify Image CDN (Gatsby Cloud feature)

**Sources:**
- https://www.gatsbyjs.com/docs/glossary/static-site-generator/
- https://smashingmagazine.com/2020/09/advanced-graphql-usage-gatsby-websites/
- https://www.whygatsby.com/
- https://strapi.io/blog/gatsbyjs-guide-generate-static-sites
- https://github.com/gatsbyjs/gatsby/blob/master/docs/docs/glossary/static-site-generator.md
- https://www.pluralsight.com/paths/building-static-sites-with-gatsbyjs
- https://rootstack.com/en/blog/gatsbyjs-and-best-static-site-generators/
- https://softchris.github.io/pages/gatsby.html
- https://www.gatsbyjs.com/blog/gatsby-cloud-evolution/
- https://ikius.com/blog/end-of-gatsbyjs
- https://www.smashingmagazine.com/2024/03/end-of-gatsby-journey/
- https://status.gatsbyjs.com/
- https://github.com/gatsbyjs/gatsby/issues/38696
- https://www.netlify.com/blog/gatsby-live-preview-with-new-dev-server/
- https://elpuas.com/blog/is-gatsbyjs-still-relevant-in-2024/
- https://www.gatsbyjs.com/docs/reference/release-notes/gatsby-version-support/
- https://github.com/gatsbyjs/gatsby/discussions/39062
- https://www.gatsbyjs.com/blog/valhalla-content-hub-explained/
- https://www.gatsbyjs.com/blog/what-is-gatsbys-valhalla-content-hub/
- https://www.gatsbyjs.com/products/valhalla-content-hub/
- https://www.gatsbyjs.com/resources/webinars/product-launch-valhalla-content-hub/
- https://www.globenewswire.com/news-release/2022/11/03/2547731/0/en/Valhalla-The-Enterprise-Content-Hub-To-Modernize-Your-Web-Stack.html
- https://www.gatsbyjs.com/blog/scaling-rsg-builds-with-gatsbys-data-layer/
- https://www.gatsbyjs.com/blog/2020-04-22-announcing-incremental-builds/
- https://medium.com/@ignatovich.dm/incremental-static-regeneration-isr-keeping-your-pages-fresh-and-fast-f28933c28e54
- https://www.gatsbyjs.com/blog/speeding-up-builds-with-incremental-build-and-dsg/
- https://www.sanity.io/glossary/incremental-static-regeneration
- https://www.ohmycrawl.com/training/gatsbyjs-v4-deferred-static-generation/
- https://www.gatsbyjs.com/docs/debugging-incremental-builds/
- https://vercel.com/docs/incremental-static-regeneration/quickstart
- https://vercel.com/docs/incremental-static-regeneration
- https://blog.logrocket.com/gatsby-incremental-builds/
- https://www.gatsbyjs.com/plugins/

### 6. Pricing & Packaging

**Gatsby Framework:**
- Open-source, always free (core framework)
- Community-supported

**Gatsby Cloud Pricing (Pre-Acquisition):**
- 3-tier model: Free, Professional, Enterprise
- Free tier: 1 user, 1 custom domain in production, always permanent
- All tiers (including free): Incremental Builds, Gatsby Hosting
- Hosting: Free plan by default, upgradeable for traffic scaling

**Post-Acquisition Status:**
- Gatsby Cloud deprecated November 30, 2024
- Customers migrated to Netlify Cloud
- Incremental builds and key features NOT ported; customers report regressions
- Hosting now via Netlify Cloud with different pricing/feature set

**Comparison to Vercel:**
- Vercel Pro: $20/user/month (usage-based)
- Gatsby Cloud Free: Commercial use allowed (unlike Vercel Hobby)
- Netlify (post-acquisition home): $19/mo Pro tier (credit-based as of Sep 2025)

**Sources:**
- https://findstack.com/products/gatsby-cloud/pricing
- https://www.gatsbyjs.com/blog/gatsby-cloud-moving-to-simpler-pricing/
- https://www.gatsbyjs.com/blog/announcing-unified-gatsby/
- https://www.gatbsyjs.com/blog/gatsby-cloud-hosting-pricing-plan/
- https://www.trustradius.com/products/gatsby/pricing
- https://www.gatsbyjs.com/gatsby-contentful-sales-guide/
- https://www.geeksforgeeks.org/blogs/best-gatsby-cloud-hosting-providers-in-2025/
- https://www.capterra.com/p/197486/Gatsby/
- https://findstack.com/products/gatsby-cloud/reviews
- https://research.com/software/reviews/gatsby

### 7. Analyst & Review Coverage

**Analyst Recognition:**
- No Gartner Magic Quadrant placement found (2024-2025)
- No Forrester Wave evaluation found (2024-2025)
- Limited enterprise analyst coverage; primarily community-driven evaluation

**Review Platform Ratings:**
- G2: Positive reviews highlighting ease of use, fast deployment, plugin ecosystem
- TrustRadius: Presence confirmed but detailed sentiment not captured in search
- Capterra: Available platform with mixed reviews
- Product Hunt: 5.0/5 with 706 reviews (high community reception historically)
- StackShare: 3.6K stacks, 2.1K followers (established in developer ecosystem)

**Key Analyst Gaps:**
- No recent analyst reports comparing Gatsby to Vercel/Next.js
- Ecosystem focus has shifted to broader "composable architectures" vs Gatsby-specific analysis
- Most coverage predates Netlify acquisition (2023+)

**Sources:**
- https://www.g2.com/products/gatsby/reviews
- https://www.trustradius.com/products/gatsby/reviews
- Various G2, Capterra, TrustRadius rating pages

### 8. Community Sentiment & Developer Experience

**Reddit & Hacker News Sentiment (2024-2025):**
- Significant frustration post-Netlify acquisition
- Users switched to Gatsby Cloud specifically for incremental builds, then forced to migrate
- Reported "significant performance regressions" after migration to Netlify Cloud
- Key issue: Incremental builds promised to be ported to Netlify but were not

**GitHub Discussions:**
- "Is Gatsby discontinued?" discussion threads
- "Is GatsbyJS Officially Dead?" discussions (issue #39062)
- Developer concern: Only 1 original Gatsby employee left at Netlify
- January 2025: gatsby-source-shopify plugin broke (Shopify API 2024-01 sunsetted) — not updated by maintainers

**Likelihood of Adoption:**
- State of JavaScript "Would use again" metric: 89% (2019) → 38% (2022)
- Massive 51-point decline reflecting post-acquisition pessimism

**Positive Sentiment Remains For:**
- Static site generation use cases (blogs, content sites)
- SEO-friendly architecture
- Plugin ecosystem for specific integrations
- Fast build times (when using incremental builds feature)

**Negative Sentiment Drivers:**
- Abandoned-project perception post-acquisition
- Dependency complexity: 168 dependencies vs Next.js's 16
- Plugin maintenance burden; outdated dependencies
- Missing 2024 roadmap
- Incremental builds (key differentiator) not available in Netlify Cloud successor

**Sources:**
- https://www.smashingmagazine.com/2024/03/end-of-gatsby-journey/
- https://news.ycombinator.com/item?id=21085651
- https://news.ycombinator.com/item?id=23324979
- https://news.ycombinator.com/item?id=23325700
- https://news.ycombinator.com/item?id=24670252
- https://github.com/ajayns/gatsby-hacker-news
- https://github.com/gatsbyjs/gatsby/discussions/39062
- https://encircletechnologies.com/blog/gatsby-in-2025/
- https://elpuas.com/blog/is-gatsbyjs-still-relevant-in-2024/
- https://ikius.com/blog/end-of-gatsbyjs
- https://www.uplers.com/hire-gatsby-developers/
- https://bejamas.com/blog/gatsby-going-down-and-taking-your-website-along/
- https://strapi.io/blog/astro-vs-gatsby-performance-comparison
- https://github.com/gatsbyjs/gatsby/issues/38696
- https://grishy.dev/en/post/gatsbyjs-death/

### 9. SEO & Traffic Analysis

**Domain Authority Data:**
- Specific DR/AS/DA metrics for gatsbyjs.com not isolated in search results
- Primary domain: gatsbyjs.com
- Documentation site: https://www.gatsbyjs.com/docs/
- Blog/resources: https://www.gatsbyjs.com/blog/

**Traffic & Visibility:**
- No specific SimilarWeb or public traffic data isolated
- Refer to ahrefs.com, semrush.com for current metrics (require subscription or direct query)

**SEO Strengths:**
- Comprehensive documentation (developer-facing SEO value)
- Blog with regular content updates (historical)
- Plugin library with 3,000+ indexed pages
- High brand awareness in React/Jamstack ecosystem
- Strong backlink profile from CMS platforms, developer blogs, tutorials

**Content Strategy Characteristics:**
- Blog-centric approach: Announcements, tutorials, feature releases, community spotlights
- Documentation hub: Comprehensive guides for framework usage
- Plugin library: Self-serve resource for integrations
- Community events: GatsbyConf (annual), JAMstack Conf participation
- Learning resources: Gatsby Courses, video tutorials, webinars

**Post-Acquisition Content Changes:**
- Content cadence reduced post-Netlify (February 2023)
- Fewer regular blog updates; focus shifted to Netlify blog
- Product announcements integrated into Netlify communications
- Plugin library maintenance dependency on community

**Sources:**
- https://ahrefs.com/website-authority-checker
- https://www.semrush.com/website/ahrefs.com/overview/
- https://backlinko.com/ahrefs-vs-semrush
- https://www.stylefactoryproductions.com/blog/ahrefs-vs-semrush
- https://www.atroposdigital.com/blog/ahrefs-vs-semrush
- https://www.semrush.com/free-tools/website-authority-checker/
- https://backlinko.com/tools/website-authority
- https://www.gatsbyjs.com/blog/
- https://www.gatsbyjs.com/docs/
- https://www.gatsbyjs.com/plugins/

### 10. Content Strategy & Marketing

**Brand Pillars:**
- Jamstack pioneer and thought leader (historical)
- "Blazingly fast" static site generation messaging
- GraphQL data layer differentiation
- Plugin ecosystem extensibility

**Content Types:**
- Technical tutorials and guides
- Case studies (pre-acquisition)
- Framework announcements and releases
- Community spotlights and interviews
- Webinar series (product launches, educational)
- Blog posts on Jamstack architecture, performance best practices

**Community Events:**
- **GatsbyConf:** Annual conference (2021, 2022 held; no 2023+ announced)
  - 2022: Virtual event with 10,000+ developers, marketers, website architects
  - Focus: Gatsby framework, Gatsby Cloud, Jamstack ecosystem
- **JAMstack Conf:** Joint presence with other framework creators
- **Developer Relations:** Gatsby team speaking at conferences (DrupalCon, JSHeroes, etc.)

**Historical Thought Leadership:**
- Kyle Mathews: Open-source founder, coined "Jamstack" term (2015)
- Strategic positioning: Tied brand identity to entire architectural movement
- Content hubs: Jamstack blog tag, static site generation resources

**Post-Acquisition Content Shifts:**
- Netlify blog now hosts Gatsby-related announcements
- Gatsby Days conferences discontinued (no 2024-2025 confirmed)
- Thought leadership credited to Netlify instead of Gatsby standalone
- Reduced content cadence; integration with Netlify messaging

**Sources:**
- https://www.gatsbyjs.com/blog/announcing-gatsbyconf-2022/
- https://www.gatsbyjs.com/blog/what-youll-learn-at-gatsbyconf-2022-a-look-at-the-agenda/
- https://www.gatsbyjs.com/contributing/
- https://www.gatsbyjs.com/blog/gatsbyconf-2021-agenda/
- https://cmscritic.com/gatsby-unveils-v3-0-cloud-hosting-and-more-at-gatsbyconf-2021
- https://www.gatsbyjs.com/blog/gatsbyconf-speaker-qa-joel-varty/
- https://www.gatsbyjs.com/blog/tags/jamstack
- https://gatsbyconf.com/
- https://www.gatsbyjs.com/plugins/gatsby-theme-jamfire-conference
- https://www.gatsbyjs.com/blog/2019-04-08-meet-the-gatsby-team-at-drupalcon-seattle-jamstack-conf-nyc-and-jsheroes

---

## Competitive Context: Gatsby vs Vercel/Next.js

### Technical Differentiation
- **Gatsby:** Static site generation with React + GraphQL data layer
- **Next.js/Vercel:** Full-stack framework with SSR, SSG, ISR, and edge functions
- **Key Gap:** Gatsby optimized for static sites; Next.js optimized for dynamic/full-stack

### Market Trajectory
- Gatsby: Declining adoption, post-acquisition uncertainty
- Next.js: Explosive growth, 4th place in Stack Overflow 2024 rankings
- Download ratio: Next.js 12x+ more downloads than Gatsby

### Philosophical Differences
- **Gatsby:** Opinionated GraphQL data layer forces consistency
- **Next.js:** Data-fetching agnostic; build whatever you need
- **Vercel:** Platform-native optimization for Next.js vs framework-agnostic Netlify approach

### Current Positioning
- Gatsby positioned as cautionary tale of acquisition-driven decline
- Incremental Builds (key differentiator) lost in Netlify integration
- Open-source framework survives but Cloud product deprecated
- Developer confidence at 10-year low based on State of JavaScript trends

---

## Source Count Summary

| Category | Count | Status |
|----------|-------|--------|
| Company & Founding | 5 | Complete |
| Funding & Financial | 12 | Complete |
| Traction & Adoption | 25+ | Complete |
| Acquisitions & Partnerships | 3 | Complete |
| Product & Features | 40+ | Complete |
| Pricing | 10 | Complete |
| Analyst & Reviews | 5 | Complete (Limited analyst coverage) |
| Community Sentiment | 20+ | Complete |
| SEO & Traffic | 10 | Partial (subscription data unavailable) |
| Content Strategy | 15 | Complete |
| Competitive Context | 15+ | Complete |
| **TOTAL** | **175+** | **Complete** |

---

## Key Themes for Brief

1. **Decline Narrative:** From Jamstack pioneer to post-acquisition decline
2. **Feature Loss:** Incremental Builds and Cloud features not carried over to Netlify
3. **Developer Confidence Crisis:** 89% → 38% "would use again" metric
4. **GraphQL Data Layer:** Differentiation that didn't translate to platform stickiness
5. **Open Source Lives, Product Doesn't:** Framework survives but Cloud shut down
6. **Cautionary Tale:** How acquisition by larger player can devalue unique assets
7. **Next.js Dominance:** Vercel's framework investment model outcompeting Gatsby's plugin ecosystem
8. **Kyle Mathews' Exit:** Founder moved on to Electric SQL (announced Aug 2024)

---

## Search Strategy Employed

1. **Historical Research:** Founding, funding rounds, key milestones
2. **Acquisition Deep Dive:** Netlify deal terms, Cloud sunset, feature losses
3. **Traction Metrics:** NPM downloads, GitHub stars, State of JS trends
4. **Product Analysis:** Features, pricing, technical differentiation
5. **Community Signals:** Reddit, Hacker News, GitHub discussions, sentiment shift
6. **Analyst Coverage:** Gartner/Forrester searches (limited results)
7. **Competitive Intelligence:** Head-to-head vs Vercel, Next.js, Netlify, Astro
8. **Content Strategy:** Blog, events, documentation, community engagement
9. **Executive Movement:** Kyle Mathews' current projects post-Gatsby

---

**Research Complete:** 175+ sources collected and organized. Ready for synthesis phase.
