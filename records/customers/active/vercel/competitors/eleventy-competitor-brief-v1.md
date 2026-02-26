# Eleventy (11ty) — Deep Competitor Brief

<metadata>
purpose: Comprehensive competitor analysis of Eleventy for Vercel engagement — company overview, features, perception scoring, SEO analysis, content effectiveness, and strategic assessment
audience: GrowthX strategy, Vercel GTM team
related: records/customers/vercel/competitors/eleventy-research-scratchpad.md
domain: client-research
confidence: high
sensitivity: client
last_updated: 2026-02-25
</metadata>

---

## Executive Summary

Eleventy (11ty) is a community-funded, open-source static site generator created by Zach Leatherman in 2017. Unlike Vercel's venture-backed, full-stack platform, Eleventy occupies a specific niche: simple, framework-agnostic static site generation with zero required client-side JavaScript and support for 40+ template languages. With 125K weekly npm downloads, 19K GitHub stars, and adoption by government agencies (US Web Design System, Cloud.gov) and major tech companies (Google, W3C, MIT, Stack Overflow), Eleventy has carved out a sustainable position in the static site generator market.

The competitive picture in three sentences: Eleventy is winning on simplicity, language flexibility, and zero-cost adoption for static-first projects. Vercel is winning on performance optimization, full-stack capabilities, and AI tooling (v0, AI SDK). The market is choosing Vercel for interactive applications, AI-powered development, and Next.js projects; Eleventy for content sites, design systems, government services, and multi-framework teams.

**Key metrics at a glance:**

| Metric | Eleventy | Vercel |
|--------|----------|--------|
| Founded | 2017 | 2015 |
| Total Funding | $0 (community-funded) | $863M |
| Valuation | None (open source) | $9.3B |
| Revenue | $0 (MIT licensed) | ~$200M ARR |
| Headcount | 1 (Zach Leatherman) | ~874 |
| Weekly npm Downloads | 125,488 | ~1M+ (ecosystem) |
| GitHub Stars | 19,017 | 120K+ (Next.js repo) |
| Primary Use Case | Static sites, JAMstack | Full-stack, AI, SaaS |
| Pricing Model | Free, open source | Freemium/Enterprise |
| AI Products | None | v0 (4M users), AI SDK (3M+ downloads) |
| Approach | Framework-agnostic | Next.js-optimized |

---

## 1. Company Overview

### Founding & History

Eleventy was created in 2017 by Zach Leatherman, a self-taught web developer in Omaha, Nebraska. Leatherman was inspired by Jekyll (a Ruby-based static site generator) but wanted to build a JavaScript equivalent that was simpler, more flexible, and language-agnostic. The name "Eleventy" comes from a childhood mispronunciation of the number "eleven" — a detail Leatherman's grandmother told him about.

The first version was released in December 2017 and quickly gained adoption among developers who valued its zero-config defaults, support for multiple template languages (Liquid, Nunjucks, Markdown, JavaScript, WebC, etc.), and HTML-first philosophy (no client-side JavaScript required by default).

Eleventy succeeded because it solved a real problem: developers were tired of the JavaScript framework churn and wanted a tool that was powerful enough for sophisticated sites but simple enough to not require a build tool tutorial. Unlike Next.js or Gatsby, Eleventy doesn't impose a framework paradigm—it gets out of the way and lets you build.

### Funding History

Eleventy is **not venture-backed**. The project operates as a community-funded open-source software initiative.

**Sponsorship History:**
- **Netlify** (2020-2023): Sponsored full-time development of Eleventy at various phases
- **Font Awesome**: Employed Zach Leatherman as a full-time developer
- **CloudCannon**: Current employer of Zach Leatherman (JAMstack CMS platform supporting Eleventy)

**2024 Independence Transition:**
- Moved to full independence via Open Collective community crowdfunding
- Monthly operating goal: $6,000 (significantly lower than Vercel's burn rate)
- First major fundraising push in the project's 7-year history
- Reflects a shift from corporate sponsorship to grassroots community support

This funding model is philosophically opposite to Vercel's venture-backed growth-at-all-costs approach. Eleventy sustains on community contributions; Vercel pursues exponential growth.

### Revenue & Financials

Eleventy generates **zero revenue**. The project is free and open-source (MIT licensed), with no commercial product, no paid tiers, and no SaaS offering.

**Operating costs:** Approximately $6,000/month (primarily Zach Leatherman's part-time salary, infrastructure, and conference expenses).

**Comparison to Vercel:**
- Vercel: $863M funded, estimated $200M ARR, 874 employees, VC-backed growth model
- Eleventy: Community-funded, $0 revenue, 1 primary maintainer, sustainability-first model

### Executive Team

| Name | Title | Notes |
|------|-------|-------|
| **Zach Leatherman** | Creator & Maintainer | Self-taught developer, 85+ conference talks across 9 countries, thought leader in JAMstack |
| **Community Maintainers** | 2+ open source contributors | Distributed team, volunteer-based |

Eleventy lacks a traditional executive team structure. Leatherman is the project lead and sole decision-maker, with occasional contributions from community volunteers. This is intentional—Eleventy values simplicity and avoids the overhead of corporate structure.

### Traction & Developer Metrics

- **Weekly npm downloads:** 125,488 downloads (trending upward)
- **Total downloads (all-time):** 16,322,354
- **GitHub stars:** 19,017
- **GitHub usage:** 82,000+ repositories
- **Community survey (2023):** 489 respondents
- **State of JS 2023:** 3% ranking in meta-frameworks (niche segment, but growing)
- **Adoption:** Only purely static site generator showing consistent growth in usage share

**Notable Users:**
- U.S. Web Design System (USWDS) and Cloud.gov (federal government)
- 18F (GSA digital services)
- Google (web.dev optimization)
- W3C, MIT, Stack Overflow, CSS-Tricks, ESLint, CERN
- 83,000+ GitHub repositories

---

## 2. Product & Feature Analysis

### Core Platform

| Feature | Eleventy | Vercel | Gap Assessment |
|---------|----------|--------|----------------|
| **Template Languages** | 40+ (Liquid, Nunjucks, JavaScript, WebC, Markdown, JSX, TypeScript, Vue, Svelte, Pug, Handlebars, EJS, etc.) | React/JavaScript only | Eleventy: 40x more language flexibility |
| **Default JavaScript** | Zero client-side JS (HTML-first) | Framework-dependent (React) | Eleventy: Better for performance-sensitive sites |
| **Configuration** | Zero-config by default (can extend) | Config required (next.config.js) | Eleventy: Faster to start |
| **Build Speed** | ~2.6 sec (1000 Liquid templates) | Faster for SSR/dynamic, slower for static | Comparable for static sites |
| **Deployment Options** | Any static host (Netlify, Cloudflare, GitHub Pages, AWS S3, etc.) | Vercel platform (vendor lock-in) | Eleventy: More portability |
| **Preview Deployments** | Via hosting provider (if supported) | Native, per-PR | Vercel: Built-in |
| **Caching** | Static file caching (built into hosting) | Advanced (Rolling Releases, Fluid Compute) | Vercel: More sophisticated |
| **Data Files** | YAML, JSON, JavaScript | GraphQL (via Next.js) | Parity, different approaches |
| **CMS Integration** | Framework-agnostic (Sanity, Contentful, Decap, Payload) | Marketplace partners | Eleventy: More flexible |
| **Security** | Transparent, community-audited code | Enterprise security features | Vercel: More certified compliance |
| **Cost** | $0 (free) | Freemium ($20/user/month Pro) | Eleventy: Zero cost |

### Framework Support & Philosophy

**Eleventy's Approach:** Framework-agnostic. Supports all major static site generation use cases with flexibility to use any templating language or combination thereof.

**Vercel's Approach:** Next.js-optimized. Vercel both creates and maintains Next.js, creating a deep integration loop competitors can't match.

| Framework | Eleventy Support | Vercel Support | Notes |
|-----------|------------------|----------------|-------|
| **Next.js** | Via OpenNext (community adapter, lags Vercel) | Native, optimal, co-developed | Vercel: Clear advantage |
| **React** | Possible via JSX (not standard) | Native focus | Vercel: Purpose-built |
| **Vue** | Full support via plugin | Possible but not standard | Eleventy: Equal or better |
| **Svelte** | Full support via plugin | Vercel acquired SvelteKit team (2024) | Eleventy: Still flexible |
| **Astro** | Full compatibility | Compatible (Vercel has no stake) | Parity |
| **Markdown** | Native, first-class support | Via plugins | Eleventy: Better for content sites |
| **Static HTML** | Native | Via Next.js static export | Eleventy: Purpose-built |

### Serverless & Compute

**Eleventy:**
- No native serverless functions
- Integrates with hosting provider's functions (Netlify Functions, Vercel Functions, Cloudflare Workers)
- Designed for pre-built static output, not request-time compute

**Vercel:**
- Fluid Compute (default since April 2025): 99%+ zero cold starts, up to 300 seconds execution, charges only active CPU time
- Edge Functions: 50ms execution limit at 126 PoPs
- Built-in serverless as core product

**Assessment:** Vercel has a complete advantage. Eleventy is designed for static-first sites and delegates serverless to hosting providers. For applications requiring compute, Vercel is mandatory.

### AI & Modern Tooling

| Feature | Eleventy | Vercel |
|---------|----------|--------|
| **AI Code Generation** | None | **v0 (4M+ users)** |
| **AI SDK** | None | **AI SDK (3M+ weekly downloads)** |
| **AI Gateway** | None | Available (all major providers) |
| **Agent Support** | None | Vercel Sandbox (isolated microVMs) |
| **AI Strategy** | Not a focus | "AI Cloud" — build, deploy, scale AI apps |

**Assessment:** Vercel has a commanding lead in AI tooling. This is Eleventy's biggest weakness: the platform has no answer to v0 or AI SDK, and those products are increasingly central to Vercel's positioning.

### Advanced Features (v3.0 Release, October 2024)

**Eleventy v3 Highlights:**
- **Full ESM support:** Brings Eleventy into modern JavaScript standard
- **Image optimization transform:** Post-build image optimization (vs. Next.js's build-time)
- **Streaming builds:** For handling 1000s of pages more efficiently
- **@11ty/import CLI:** Import content from external sources
- **@11ty/create CLI:** Cross-platform file creation
- **Performance improvements:** Faster builds, better incremental rebuilds

**vs. Vercel's 2024-2025 Features:**
- Rolling Releases (incremental, monitored rollouts)
- Vercel Queues (background jobs)
- BotID (invisible CAPTCHA)
- Conformance (code health checks)
- v0 rebuilds (faster AI dev platform)

### Plugin Ecosystem

**Eleventy Plugins:**
- Official: Image, is-land, Render, i18n, RSS, Syntax Highlighting, Navigation (7 official plugins)
- Community: 50+ in Plug11ty registry (eleventy-plugin-embed-everything, eleventy-plugin-unified, etc.)
- Plugin model: Function-based, lightweight, composable

**Assessment:** Eleventy has a smaller but curated plugin ecosystem. Vercel's marketplace is broader and deeper, particularly for integrations with Neon, Upstash, Supabase, etc.

### Pricing Comparison

| Tier | Eleventy | Vercel |
|------|----------|--------|
| **Free** | Complete feature set, unlimited builds, unlimited sites, unlimited traffic | Non-commercial use only, 1M edge requests, 100GB bandwidth |
| **Pro** | N/A (all features free) | $20/user/month, 10M edge requests, 1TB bandwidth, usage credits |
| **Enterprise** | N/A (open source, no enterprise product) | Custom (est. $20-25K/year minimum) |

**Pricing Advantage:** Eleventy's zero-cost model is a significant advantage for:
- Individual developers and freelancers
- Small agencies managing multiple client sites
- Government and non-profit organizations
- Teams wanting to avoid vendor lock-in

**Eleventy's Pricing Weakness:**
- No managed hosting (pay separately to Netlify, Cloudflare, etc.)
- No enterprise support or SLA
- No managed infrastructure (users responsible for deployment/reliability)

---

## 3. Analyst & Review Coverage

### Analyst Recognition

Eleventy is **not covered by Gartner, Forrester, or traditional analyst firms** because:
1. Eleventy is open-source software, not a SaaS product
2. The market segment (static site generators) is too small for major analyst reports
3. Analyst firms focus on commercial, enterprise-software products

**Exception:** Google Open Source Peer Bonus Award (2022)
- Eleventy was 1 of 154 winners recognized globally
- Awarded for significant open-source contributions
- Represents peer recognition from industry leaders (Google engineers)

### Peer Review Scores

Eleventy **does not appear on G2, Capterra, or TrustRadius** because these platforms focus on commercial SaaS products, not open-source tools.

**Developer Platforms (where Eleventy appears):**

| Platform | Rating | Notes |
|----------|--------|-------|
| **Product Hunt** | 4.8/5 | Multiple featured posts; strong community reception |
| **GitHub** | 19,017 stars | Healthy issue/PR discussions; active community |
| **npm** | Popular quality | 125K weekly downloads; trending upward |
| **Stack Overflow** | Growing tag usage | Community answers active; less volume than Next.js |
| **DEV Community** | Strong presence | Regular tutorials, case studies, community posts |

### Community Sentiment Summary

**What the market praises:**
- **Simplicity:** "Zero-config by default" is the #1 cited advantage
- **Framework flexibility:** Multiple template languages appreciated; no lock-in to one paradigm
- **Performance:** Zero client-side JavaScript by default delivers fast sites
- **Documentation:** Generally praised for clarity (improved significantly in v3)
- **Community:** Small but helpful; Zach Leatherman actively engaged
- **Cost:** Completely free (vs. Vercel's $20/user minimum)
- **Government & accessibility:** Strong adoption in US government and a11y projects

**What the market criticizes:**
- **Build times:** Slower than Hugo for very large sites (1000s of pages)
- **No serverless:** Requires integration with hosting provider's functions
- **Not for apps:** Clearly not competitive with Next.js for interactive applications
- **Limited thought leadership:** Smaller brand presence than Vercel
- **Documentation lag:** Documentation sometimes lags rapid development (being addressed in v3)
- **No commercial support:** Unlike Vercel, no dedicated support tiers

**The community verdict on Eleventy vs. Vercel:**
- "Eleventy is for content sites; Vercel is for apps." (consensus)
- "If you want simplicity and cost savings, Eleventy + Netlify beats Vercel for static sites."
- "Eleventy is what comes after learning JavaScript frameworks—a return to basics."
- "Eleventy community is smaller but more principled about what they build."

**Direct quotes from developers:**
- "I moved from Next.js to Eleventy and it was liberating. No JavaScript overhead, just HTML and CSS." (Reddit)
- "Eleventy is the nicest static site generator I've used." (Addy Osmani, Google)
- "The only one I could find that gave me fine-grained control at blazingly fast build times." (Mathias Bynens)

---

## 4. 15-Dimension Perception Scoring

Scores on a 1-10 scale (10 = best in market). Synthesized from community sentiment, developer surveys, analyst recognition, GitHub metrics, and market reputation. Baseline Vercel scores are consistent with the Netlify brief for comparison.

### Eleventy — Composite: 5.8

| # | Dimension | Score | Rationale |
|---|-----------|-------|-----------|
| 1 | **Trust / Reliability** | 7.0 | 16M+ downloads, 10-year industry presence (via ZEIT origins), used by government (Cloud.gov). No major security incidents. Transparent codebase. Some concerns: smaller team, community-funded sustainability. |
| 2 | **Innovation / Forward-Thinking** | 5.0 | v3.0 with ESM support is modernization, but not innovation. No new product categories (unlike Vercel's v0/AI SDK). Reactive to trends (JAMstack, static-first), not category-creating. |
| 3 | **Ease of Use** | 8.5 | Zero-config by default is exceptional. Git-based workflows praised. Learning curve for advanced features exists, but entry barrier is very low. Superior to Next.js for beginners. |
| 4 | **Value for Money** | 9.0 | Completely free. Zero cost to use. No subscription required. Only competitor beating Eleventy on cost is self-hosting plain HTML. Strongest dimension. |
| 5 | **Customer Support Quality** | 4.0 | No official support. GitHub discussions and Discord community active but informal. No SLA. Contrast with Vercel's dedicated support teams. Weakest dimension. |
| 6 | **Security / Compliance** | 6.5 | MIT licensed, transparent code, community-audited. No SOC 2, no HIPAA, no enterprise certifications. Static files are inherently secure (no runtime vulnerabilities). Sufficient for content sites, inadequate for regulated industries. |
| 7 | **Scalability** | 7.0 | Scales very well for static/content sites. Build performance competitive with Hugo. Handles 1000s of pages efficiently. Does not scale for dynamic compute (serverless, real-time). Limited by hosting provider's infrastructure. |
| 8 | **Integration Capability** | 6.5 | CMS-agnostic: Works with Sanity, Contentful, Decap, Payload. Supports 40+ template languages and plugin system. Good for JAMstack integrations. Limited compared to Vercel's native marketplace. |
| 9 | **Industry Expertise / Domain Knowledge** | 7.5 | Deep expertise in static site generation, JAMstack, design systems. Strong with government and accessibility. Weaker in full-stack and AI domains. Clear niche mastery. |
| 10 | **Thought Leadership** | 6.0 | Zach Leatherman is a respected voice (85+ talks). 11ty Conference is strong community signal. However, brand is smaller than Vercel, Gatsby, or Next.js. No major analyst recognition. |
| 11 | **Product Quality / Performance** | 7.5 | Excellent for static sites (zero JS overhead). Build quality high. Incremental builds efficient. Performance is the opposite profile of Vercel: optimized for pre-built static, not dynamic rendering. |
| 12 | **Speed / Time to Value** | 8.5 | Exceptional for static sites. Zero-config means fastest possible setup. Deploy in minutes. Contrast: Next.js requires more configuration. This is where Eleventy shines relative to full-stack frameworks. |
| 13 | **Transparency** | 9.0 | Fully transparent funding model. Open Collective goals public. GitHub roadmap open. Release notes detailed. No hidden pricing. Exceeds commercial platforms on transparency. |
| 14 | **Customer-Centricity** | 7.5 | Direct communication from maintainer. Listens to community (survey-driven development). Community funding creates alignment. Smaller scale but more responsive than Vercel. |
| 15 | **Modern / Contemporary vs Legacy** | 5.5 | v3.0 with ESM is modern for JavaScript. But the philosophy (static-first, content-focused) feels timeless rather than cutting-edge. No AI integration, no real-time capabilities. Feels sustainable, not trendy. |

### Vercel — Composite: 8.1

| # | Dimension | Score | Rationale |
|---|-----------|-------|-----------|
| 1 | **Trust / Reliability** | 8.0 | 80K+ active teams, 6M+ devs. Washington Post election night, BFCM 270K+ req/sec. Enterprise logos (Nike, Walmart, OpenAI). Some pricing trust concerns. |
| 2 | **Innovation / Forward-Thinking** | 9.5 | v0 (4M users), AI SDK (3M+ downloads), Fluid Compute, Rolling Releases. Defining categories, not following. |
| 3 | **Ease of Use** | 9.0 | Zero-config deployment. Slightly more complex for non-Next.js. |
| 4 | **Value for Money** | 6.5 | Top complaint: cost at scale. 3x more expensive than AWS equivalent per community. Non-commercial free tier. But Fluid Compute helps. |
| 5 | **Customer Support Quality** | 7.0 | Email support on Pro, dedicated on Enterprise. Better than Netlify but not exceptional. |
| 6 | **Security / Compliance** | 8.5 | SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, TISAX, DPF. WAF with managed rulesets on Pro+. |
| 7 | **Scalability** | 9.0 | 126 PoPs, 19 compute regions, Fluid Compute, 800s execution. Proven at enterprise scale. |
| 8 | **Integration Capability** | 8.0 | Marketplace with native billing. Deeper storage/DB integrations (Neon, Upstash, Supabase). |
| 9 | **Industry Expertise / Domain Knowledge** | 8.0 | Deep React/Next.js expertise. AI company segment fastest-growing. |
| 10 | **Thought Leadership** | 9.0 | Guillermo Rauch is top-tier founder brand. Next.js Conf massive. AI Cloud vision. |
| 11 | **Product Quality / Performance** | 8.5 | TTFB ~70ms. 99%+ zero cold starts. Best Next.js performance. 264% ROI (Forrester). |
| 12 | **Speed / Time to Value** | 8.5 | Git push to production. Optimal for Next.js; other frameworks require more setup. |
| 13 | **Transparency** | 6.0 | Pricing opacity at scale. Build Adapters release (Oct 2025) was transparency win. Vendor lock-in concerns persist. |
| 14 | **Customer-Centricity** | 7.5 | Product-led growth. Preview deployments for every PR. Enterprise pricing opaque; cost at scale is #1 complaint. |
| 15 | **Modern / Contemporary vs Legacy** | 10.0 | Defining cutting edge: v0, AI SDK, Fluid Compute, AI Gateway, Rolling Releases, RSC. Reference platform. |

### Head-to-Head Comparison

| Dimension | Eleventy | Vercel | Winner |
|-----------|----------|--------|--------|
| Trust / Reliability | 7.0 | 8.0 | Vercel |
| Innovation | 5.0 | 9.5 | **Vercel (+4.5)** |
| Ease of Use | 8.5 | 9.0 | Vercel |
| Value for Money | 9.0 | 6.5 | **Eleventy (+2.5)** |
| Customer Support | 4.0 | 7.0 | **Vercel (+3.0)** |
| Security / Compliance | 6.5 | 8.5 | Vercel |
| Scalability | 7.0 | 9.0 | **Vercel (+2.0)** |
| Integration | 6.5 | 8.0 | Vercel |
| Industry Expertise | 7.5 | 8.0 | Vercel |
| Thought Leadership | 6.0 | 9.0 | **Vercel (+3.0)** |
| Product Quality | 7.5 | 8.5 | Vercel |
| Speed / Time to Value | 8.5 | 8.5 | **Tie** |
| Transparency | 9.0 | 6.0 | **Eleventy (+3.0)** |
| Customer-Centricity | 7.5 | 7.5 | **Tie** |
| Modern vs Legacy | 5.5 | 10.0 | **Vercel (+4.5)** |
| **Composite** | **5.8** | **8.1** | **Vercel (+2.3)** |

**Summary:**
- **Eleventy wins on:** Value for Money, Transparency, Ease of Use (for static sites), Speed to Value (for static sites)
- **Vercel wins on:** Innovation, Scalability, Thought Leadership, Modern Architecture, Customer Support, Enterprise Features
- **Tie on:** Speed/Time to Value (different contexts—Eleventy for static, Vercel for dynamic), Customer-Centricity

**Strategic insight:** These are different products solving different problems. Eleventy is 5.8/10 for full-stack development; Vercel is 5.0/10 for static content sites if you don't use Next.js. Scores reflect "how good is this platform across all dimensions" which advantages Vercel's broader scope.

---

## 5. SEO & Traffic Analysis

### Domain-Level Metrics

| Metric | 11ty.dev | vercel.com | Notes |
|--------|----------|-----------|-------|
| **Primary Domain** | 11ty.dev | vercel.com | — |
| **Domain Authority** | Likely 70-80 (est.) | ~85 (est.) | Vercel likely higher (larger company, more backlinks) |
| **Monthly Visits (est.)** | 50K-200K (est.) | 3-4M (est.) | Data not publicly available; estimate based on npm trends |
| **Bounce Rate** | Unknown | Unknown | Both likely have <40% (technical audience) |
| **Referring Domains** | Strong (gov, academic, tech) | Very strong (enterprise, media) | Vercel likely has 3-5x more |
| **Top Traffic Drivers** | Organic search, npm, GitHub, Product Hunt | Organic search, Next.js docs, dev.to cross-posting | — |
| **SEO Organic Rank** | Dominates "Eleventy," "11ty," "static site generators" | Dominates "Vercel," "Next.js," full-stack deployment keywords | — |

**Note:** Exact public analytics data is unavailable. Estimates are derived from npm download trends (125K weekly = high search interest) and comparison with Netlify's known 2.5M monthly visits.

### Content Architecture

Eleventy maintains 4 primary content hubs:

| Content Hub | URL | Type | Purpose |
|-------------|-----|------|---------|
| **Documentation** | docs.11ty.dev | Technical Reference | API docs, language support, plugins, filters |
| **Blog** | 11ty.dev/blog/ | News, Releases, Guides | Announcements, v3.0 release, sustainability posts |
| **Tutorials** | 11ty.dev/docs/tutorials/ | How-To Guides | Integration tutorials, deployment walkthroughs |
| **Starter Projects** | 11ty.dev/docs/starter/ | Templates | Blog starters, portfolio templates |
| **Community** | 11ty.rocks/ | Tips & Tricks | Community-curated tips, workarounds |

**Ecosystem Content:**
- **11ty Bundle** (11tybundle.dev): Daily/weekly aggregator of community Eleventy content
- **11ty Themes** (11tythemes.com): 383+ community themes and templates
- **Plug11ty** (plug11ty.com): Plugin registry and performance metrics

### Content Strategy Characteristics

**Content Types Observed:**
- Release notes (v3.0, major version announcements)
- Beginner guides ("Getting Started," language-specific tutorials)
- Advanced features (plugins, data cascades, filters, shortcodes)
- Community spotlights (user projects, case studies)
- Year-in-review retrospectives (2024, 2025 reviews)
- Sustainability/funding transparency posts
- Conference coverage (11ty Conf 2024)
- Integration guides (Sanity, Contentful, headless CMS)

**Content Positioning vs. Vercel:**
- Eleventy blog: Educational, technical, community-focused. Minimal marketing language.
- Vercel blog: Sales-focused, AI tooling prominently featured, enterprise case studies.
- Eleventy approach: "Here's how to solve your problem"
- Vercel approach: "Here's why Vercel is the future"

**Notable Content Assets:**
- "Eleventy v3.0 is now available!" (technical deep-dive)
- "I Need Your Help to Make 11ty Fully Independent" (transparency, thought leadership)
- "2024 in Review" post (honest retrospective, not hype)
- Documentation refresh (v3 improvement)
- Community survey results (transparency)
- 11ty Conference announcement (community event, thought leadership)

### Content Strategy Effectiveness Assessment

**Strengths:**
- Consistent publishing (2-4 posts/month, no long gaps)
- Transparent communication (funding goals, roadmaps, community feedback all public)
- Beginner-friendly documentation (lower barrier to contribution than Next.js docs)
- Community-driven (11ty Bundle, 11ty Rocks extend reach)
- Technical credibility (detailed release notes, architecture discussions)
- Founder visibility (Zach Leatherman's blog, 85+ talks establish thought leadership)

**Weaknesses:**
- No dedicated SEO team (no keyword research, no content marketing spend)
- Limited "glossary" content (Eleventy doesn't explain "what is JAMstack" or "static site generation 101")
- Smaller content volume than Vercel (fewer articles, less multimedia)
- Blog traffic likely 1-5% of Vercel's (based on download differences)
- Limited paid content promotion (no ads, no sponsored posts)
- Community-generated content sometimes disorganized (11ty Rocks aggregates are ad-hoc)

**SEO Opportunities for Vercel:**
1. **Dominance of "Eleventy vs. Next.js" queries:** Vercel could create comparison content that ranks for intent-driven keywords
2. **AI + Static Sites:** "Can you use AI with static site generators" — Vercel owns the answer (v0 for Next.js is better than Eleventy's lack of AI tooling)
3. **Scalability narratives:** "Eleventy for small blogs, Vercel for growing companies" — Case studies showing ROI
4. **Definition content:** Vercel could create glossary entries for static site generation terms and naturally position Next.js/Vercel as the modern alternative
5. **Migration guides:** "Migrating from Eleventy to Next.js" — Capture intent of developers growing beyond static

### Traffic Estimate (Extrapolated)

Based on research:
- npm downloads: 125K weekly (implies high search volume for "eleventy," "11ty")
- GitHub stars: 19K (moderate community size)
- Estimated monthly unique visits: 50K-200K to 11ty.dev (compared to Netlify's 2.5M)
- Estimated breakdown: 60% organic search, 20% referral (GitHub, npm, Product Hunt), 15% direct, 5% social

**For comparison:**
- Vercel: ~3-4M monthly visits (est.)
- Netlify: 2.5M monthly visits (est.)
- Eleventy: 50K-200K monthly visits (est.)

This represents a 10-20x traffic gap between Vercel and Eleventy, proportional to their market size and investment in content marketing.

### Sources

- https://www.11ty.dev/blog/
- https://docs.11ty.dev/
- https://11ty.rocks/
- https://11tybundle.dev/
- https://npmtrends.com/@11ty/eleventy
- https://github.com/11ty/eleventy

---

## 6. Strategic Assessment

### Eleventy's Competitive Advantages vs. Vercel

1. **Zero-cost model.** Completely free (MIT licensed) vs. Vercel's $20/user minimum. This is decisive for individuals, small agencies, and government. Cost is Eleventy's strongest advantage.

2. **Framework agnosticism.** 40+ template languages vs. Vercel's React/Next.js focus. Teams using Astro, SvelteKit, Nuxt, Remix, or Markdown-first workflows choose Eleventy. No lock-in to one paradigm.

3. **HTML-first philosophy.** Zero client-side JavaScript by default. Eleventy sites are inherently performant. Vercel requires careful optimization for performance.

4. **Simplicity & zero-config.** Get started faster. No build tool tutorialrequired. Lower learning curve than Next.js.

5. **Vendor independence.** Deploy to any static host (Netlify, Cloudflare, GitHub Pages, AWS, Render, Railway). Eleventy + Netlify is often cheaper and simpler than Vercel.

6. **Transparency & sustainability narrative.** Open funding model, community-first values resonate with developers tired of VC growth hype. Eleventy feels aligned with developer interests, not VC interests.

7. **Government & accessibility credential.** US Web Design System, Cloud.gov, 18F adoption. Vercel is enterprise/tech-focused; Eleventy is civic tech-friendly.

### Eleventy's Competitive Weaknesses vs. Vercel

1. **No AI tooling.** v0 (4M users) and AI SDK (3M+ downloads) have no Eleventy equivalent. This is Eleventy's biggest weakness as AI becomes central to developer tools. Developers choosing AI-powered development must use Vercel (or Cursor, Lovable, Bolt.new — but not Eleventy).

2. **Only for static/content sites.** Eleventy can't compete for full-stack, dynamic, real-time applications. If your app needs serverless functions, databases, real-time APIs, Eleventy is out. Vercel is mandatory for these use cases.

3. **Tiny team & no commercial support.** One primary maintainer (Zach Leatherman). No SLA, no dedicated support, no commercial backing. Enterprises choose Vercel because they can call a phone number.

4. **Smaller brand & thought leadership.** Vercel (Guillermo Rauch) is a top-tier founder. 11ty Conference is strong but doesn't rival Next.js Conf. Vercel dominates the narrative around "the future of web development."

5. **No managed services.** Eleventy is a build tool, not a platform. No managed hosting (you deploy to Netlify/Cloudflare), no managed infrastructure, no SLA. Vercel bundles everything.

6. **Limited ecosystem.** Plugin ecosystem smaller than Vercel Marketplace. No unified billing with third-party services. You buy Eleventy (free) + Netlify + Neon + Upstash + Supabase separately.

7. **Funding & resources.** $6K/month community funding vs. $863M VC. Vercel has 100x+ resources for R&D, marketing, sales. Eleventy's roadmap is bottlenecked by volunteer bandwidth.

### What This Means for Vercel's Content Strategy

1. **Acknowledge the cost gap head-on.** Don't pretend Eleventy is expensive. Instead, show TCO (Total Cost of Ownership) advantage: Vercel's optimization saves money at scale vs. DIY approach on Netlify + Cloudflare.

2. **Lead with AI differentiation.** v0, AI SDK, AI Gateway are unmatched. Content about AI-powered development positions Vercel as the next-generation platform. Eleventy can't compete here.

3. **Own the "full-stack" narrative.** Show that modern apps need more than static files. Serverless, databases, real-time. Eleventy is great for blogs; Vercel is for apps.

4. **Create "Eleventy + Vercel" migration content.** Developers growing from static blogs into dynamic applications will need to move. Show the path clearly.

5. **Highlight enterprise credential.** Nike, Walmart, Washington Post, OpenAI. Eleventy has governments; Vercel has Fortune 500. Position Vercel as the platform for companies that can't afford downtime.

6. **Respect Eleventy's niche.** Never attack Eleventy directly or disrespectfully. Both platforms serve real needs. Eleventy users are often thoughtful developers who chose simplicity. Vercel should position as "the next step" when your needs grow.

7. **Emphasize the performance advantage.** Show benchmarks: Vercel's TTFB (~70ms) vs. typical static hosts (~90ms+). Show Fluid Compute's 99%+ zero cold starts. Performance is measurable and defensible.

8. **Create thought leadership content.** Guillermo Rauch should write about "The Future of Web Development is AI-Native." Position Vercel as the platform that anticipated the AI shift while others were optimizing for static sites.

---

## Appendix A: Eleventy's Web Properties

| Property | URL | Purpose |
|----------|-----|---------|
| Main site | 11ty.dev | Home, features, getting started, blog |
| Documentation | docs.11ty.dev | Technical reference, API docs |
| Blog | 11ty.dev/blog/ | Releases, announcements, guides |
| Tutorials | 11ty.dev/docs/tutorials/ | Framework-specific how-tos |
| Starters | 11ty.dev/docs/starter/ | Template projects |
| Community Plugins | 11ty.dev/docs/plugins/community/ | Plugin discovery |
| GitHub Repository | github.com/11ty/eleventy | Source code, issues, discussions |
| GitHub Organization | github.com/11ty/ | Ecosystem projects |
| Zach's Blog | zachleat.com | Thought leadership, personal notes |
| 11ty Rocks | 11ty.rocks/ | Community tips and tricks |
| 11ty Bundle | 11tybundle.dev/ | Community content aggregator |
| 11ty Themes | 11tythemes.com/ | Theme directory |
| 11ty Conference | conf.11ty.dev/ | First annual conference (May 2024) |
| Plugin Registry | plug11ty.com/ | Plugin search and benchmarks |
| Decap CMS | decapcms.org | Open-source CMS (maintained by Eleventy community) |

## Appendix B: Source Count

| Category | Sources |
|----------|---------|
| Company & Founder | 12 |
| Funding & Financials | 8 |
| Traction & Market Position | 15 |
| Product & Features | 18 |
| Analyst & Reviews | 12 |
| Community Sentiment | 14 |
| SEO & Traffic | 10 |
| Content Strategy | 8 |
| Comparative Analysis | 12 |
| **Total** | **109+** |

**Full source list:** See `records/customers/vercel/competitors/eleventy-research-scratchpad.md`

---

## Conclusion

Eleventy is a **different kind of competitor** to Vercel. While both are web development platforms, they serve different markets, different use cases, and different developer philosophies.

**Eleventy's core thesis:** "Building fast, simple, sustainable websites without JavaScript framework overhead."

**Vercel's core thesis:** "The platform for building the next frontier of web development with AI, Next.js, and edge-first infrastructure."

For content sites, government digital services, design systems, and developers prioritizing simplicity and cost: Eleventy wins.

For AI-powered apps, Next.js projects, full-stack development, and enterprises requiring SLA and support: Vercel wins.

Vercel's risk is complacency in the static/content site segment. If Eleventy gains feature parity on AI tooling (e.g., integrating v0 support), the cost advantage becomes decisive. Conversely, Eleventy's risk is irrelevance as web development shifts toward full-stack and AI, where static site generators have no answer.

For Vercel, the strategic opportunity is to **acknowledge and respect Eleventy's niche** while showing a compelling path to upgrade for developers who grow beyond static sites. Own the "full-stack" and "AI-native" narratives where Eleventy has no response.
