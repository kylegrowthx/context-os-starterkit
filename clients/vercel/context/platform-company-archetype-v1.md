# Platform Company Archetype

**Archetype Status:** Active | **Primary Example:** Mintlify | **Vercel Solution Tag:** Platforms (Multi-Tenant Apps)

---

## What is a Platform Company?

A **Platform Company** is a business whose core product *is* a platform — they build something that their customers then use to serve *their own* customers or users. They sit in the middle of a value chain, providing infrastructure, tooling, or content capabilities to a downstream audience.

In Vercel's framework, these are often called **"Platforms for Platforms"** — companies that white-label, extend, or build on top of Vercel's infrastructure to power their own multi-tenant product. Think of them as B2B2C or B2B2B businesses: they're not just a company using Vercel to ship a website — they're using Vercel as the backbone of a product that serves hundreds or thousands of their own tenants.

**The defining question:** Does their product *deploy* or *serve* content/applications *for other businesses or users* at scale, often across custom domains?

---

## Vercel Customer Examples

| Company | What They Do | Why They're a Platform Company |
| --- | --- | --- |
| **Mintlify** | Developer documentation platform | Hosts docs sites for Anthropic, Coinbase, Replit, LangChain, etc. Each customer gets their own branded docs at scale. $680K ANR. Chose Vercel over Cloudflare (even free CF). |
| **Fern (Birch Solutions)** | API documentation & SDK generation | Powers developer-facing docs + SDKs for API companies, multi-tenant deployment model. $342K ANR. |
| **Patrianna** | B2B gaming platform | Multi-tenant SaaS for gaming operators — each operator gets their own branded instance. $178K ANR. |
| **VTEX** | Headless commerce platform | South America's top ecommerce platform with 3,000+ customers; uses Vercel to power FastStore (their frontend accelerator). $396K ARR. |
| **Zapier** | Workflow automation | Powers dynamic, user-generated workflow interfaces across thousands of integrations — B2B2B model. $652K ARR. |
| **Hashnode** | Developer blogging platform | Hosts developer blogs with custom domains for each user — classic multi-tenant content platform. |
| **Whop** | Digital products & community monetization platform | Enables creators to sell digital products, memberships, and communities — each seller gets their own storefront/workspace. $705K ARR (renewed Jan 2026 with $151K expansion). 222% overage at renewal = massive growth signal. Actively exploring v0 Platform API for "Whop Agent" to let sellers build AI-powered storefronts. |

---

## Metrics That Matter

### Internal Metrics (What They Track Internally)

These are the KPIs Platform Companies live and die by. When you speak to these, you speak their language.

- **Number of active tenants / customers** — How many end-customers are live on the platform
- **Tenant growth rate (MoM/QoQ)** — Are they scaling? This directly predicts Vercel usage growth
- **Custom domains provisioned** — Each new tenant often = a new domain. A platform growing from 500 → 5,000 domains is a massive Vercel expansion signal
- **P99 latency per tenant** — Their customers feel performance degradation directly; slow = churn
- **SSL provisioning success rate** — Failed SSL at tenant onboarding is a showstopper for their product
- **Time-to-live for new tenant deployments** — How fast can a new customer get from signup to live site?
- **Build times & deployment frequency** — Platform companies often have CI/CD pipelines triggered by their customers' actions, not just their own devs
- **Tenant-level error rates** — Debugging issues across thousands of tenants is operationally brutal without good tooling
- **Infrastructure cost per tenant** — Unit economics are existential. If infra cost per tenant is too high, their business model breaks

### External Metrics (What Their Investors & Board Track)

- **ARR / MRR growth** — Their revenue is tied to how many tenants pay and how much
- **Net Revenue Retention (NRR)** — Retaining and expanding within their customer base
- **Customer acquisition cost (CAC) vs. LTV** — Infra costs affect LTV directly
- **Time-to-value for new customers** — How fast does a new tenant go live? Slow onboarding = high churn risk
- **Uptime / reliability** — Their SLAs are your SLAs. If Vercel goes down, *their* product is down for *all* their customers simultaneously
- **Geographic reach** — Global platforms need global edge performance

---

## Problem → Value Map

Platform companies share a common business model: they monetize by onboarding tenants, keeping those tenants live and performant, and expanding usage across their customer base. Every problem below maps directly to how that business model breaks — and how Vercel fixes it.

| Business Problem (What the Customer Says) | Why It Hurts Their Business Model | Vercel Solution | Proof Point |
| --- | --- | --- | --- |
| **"Onboarding a new tenant takes days because of SSL and domain provisioning"** | Time-to-live directly impacts CAC and conversion. If a new customer signs up but their branded site isn't live for 48 hours, activation rates drop. At scale (500→5,000 tenants), this becomes a full engineering team's problem — custom CNAME validation, cert renewals, apex domain edge cases, wildcard routing. Every hour of delay is churn risk before the customer even starts paying. | **Multi-Domain Projects + API** — Programmatic custom domain management and automatic SSL provisioning. Tenants go live in minutes, not days. Wildcard subdomain support + custom domain API handles the full spectrum without custom plumbing. | Mintlify scaled from 2,000 → 6,500 domains in one year on Vercel with zero dedicated domain engineering. Their tenant onboarding is fully automated through Vercel's domain API. |
| **"Our sites are slow for some tenants but we can't figure out which ones or why"** | Platform companies serve dynamic, per-tenant content but need static-like speed. P99 latency per tenant directly correlates to tenant churn — their customers' end-users feel every millisecond. Without tenant-aware caching, they either over-cache (stale content) or under-cache (expensive origin hits on every request). And when something breaks, traditional monitoring shows aggregate errors — they can't isolate which of their 2,000 tenants is experiencing the issue. | **ISR + Edge Functions** for tenant-aware caching with on-demand revalidation. **Observability+ / Log Drains** for structured, queryable, tenant-level logs and debugging. No more grepping through a firehose to find one tenant's 500 error. | Mintlify's primary compute was ISR. When they explored moving to Cloudflare, they discovered they'd have to rebuild all cache behavior from scratch — a hybrid attempt caused a 60% cost spike. Vercel's unified team-level logs were Mintlify's top roadmap request, shipped as part of the renewal commitment. |
| **"Bots are scraping our tenants' content and inflating our compute bill"** | When you're a platform, bots don't attack just you — they attack all tenants simultaneously. Content scraping, credential stuffing, and synthetic traffic spike compute costs across the entire fleet. Without per-tenant traffic intelligence, the platform is playing whack-a-mole while the CFO watches the bill climb 20-30% from fake traffic. For AI-powered platforms, bots consuming expensive AI tokens is an existential cost problem. | **BotID + WAF** — Tenant-aware bot detection and blocking at the edge. Stops abuse patterns before they hit functions or AI inference. Cheaper than serving bots expensive tokens. | Platform customers using BotID report significant reduction in non-human traffic costs. For AI-powered platforms specifically, blocking bots before they trigger AI Gateway calls prevents the most expensive type of waste. |
| **"We're spending more engineering time on infra than on our actual product"** | This is the graduation trap. The platform started on simple infrastructure and grew. Now they've built so much custom plumbing — domain management, caching layers, routing logic, SSL automation, deployment pipelines — that they're maintaining a mini-Vercel internally. Every sprint spent on infra babysitting is a sprint not spent on features that drive tenant acquisition and NRR. This is how platforms lose to faster-moving competitors. | **Vercel for Platforms (full stack)** — Vercel absorbs the infrastructure complexity: domains, SSL, caching, rendering, security, delivery. The platform team focuses on their product layer. Subhosting provides per-tenant project isolation via SDK for platforms that need full tenant separation. | Mintlify chose to pay Vercel over free Cloudflare for 3 years ($2.4M TCV) because the engineering time saved on ISR Shield, Vercel Shield, China Delivery, and domain management was worth more than the infrastructure cost. As G said: "We manage astonishingly complex Kubernetes & infrastructure complexity on your behalf." |
| **"Our CFO can't predict infra costs as we add tenants"** | Usage-based pricing from AWS/Cloudflare/GCP without guardrails creates budget anxiety. As tenants grow, so does the bill — but without per-tenant cost attribution, it's impossible to know if the business is profitable at the unit economics level. Surprise bills are common. The CFO can't model the cost of adding 500 tenants next quarter, which slows down go-to-market decisions. | **Flex Commit + Private Rate Cards** — Predictable annual spend with committed rates per SKU. The platform can model cost-per-tenant against the commit structure and forecast with confidence. Annual burndown smooths seasonal spikes. As tenant count grows, the commit grows — creating a natural expansion motion. | Mintlify's 3-year deal was structured with custom CDN/ISR Shield pricing that made unit economics work vs. "free" Cloudflare. VTEX ($396K ARR) models per-merchant infrastructure cost against their Vercel commit to ensure profitability across 3,000+ merchants. |
| **"We need to ship AI features to our tenants but can't build ML infra"** | AI is the differentiation play for platforms right now. Tenants expect AI-powered features (smart search, content generation, recommendations), but building model routing, provider fallbacks, usage tracking, and observability across multiple LLM providers requires a dedicated ML infrastructure team most platforms don't have. Platforms that can't ship AI features fast lose to competitors who can. | **AI Gateway** — Single endpoint routing to 100+ models with built-in observability, fallbacks, and usage tracking. **v0 Platform API** — Platforms can embed AI-generated site/UI creation directly into their product for tenants. Both draw from Flex Commit — no separate contract. | Platform companies building AI features for their tenants use AI Gateway to consolidate provider management. v0 Platform API enables platforms like Lovable and coding agents to offer AI-built applications to their users on Vercel infrastructure. |
| **"Our tenants serve users globally but our infrastructure is US-only"** | Global platforms need global edge performance. A tenant in Germany whose end-users are in Asia experiences latency that Vercel's US-only competitor can't fix. International expansion is often a board priority — if the platform can't perform globally, they lose deals to competitors who can. China specifically is a make-or-break market for many platforms with APAC tenants. | **Edge Network (~19 regions) + China Delivery + Vercel Shield** — Global multi-region performance for all tenants out of the box. China Delivery specifically solves the GFW problem without requiring the platform to build a separate China infrastructure stack. | Mintlify's renewal included China Delivery as a key value driver — their tenants (API companies like Anthropic, Coinbase) serve developer audiences globally, including significant Chinese developer traffic. |

---

## How to Identify Platform Companies (Pattern Recognition)

### Know Your Customer

Use this table to match the workload to the right persona and tailor your message. Platform companies have distinct buyers depending on which layer of the stack you're discussing.

| Key Vercel Workload | Technical Buyer | Economic Buyer | What the Technical Buyer Cares About | What the Economic Buyer Cares About |
| --- | --- | --- | --- | --- |
| **Multi-tenant site hosting & custom domain provisioning** | Head of Platform Engineering, Staff Engineer (Infra), VP Engineering | CTO, VP Product | "We're burning sprints building SSL automation and domain routing instead of shipping product. I need this to just work at 10,000 domains." | "Every sprint spent on infra plumbing is a sprint not spent on features that drive tenant acquisition and retention." |
| **ISR / Edge rendering for per-tenant content** | Staff Engineer (Frontend), Lead Engineer, Head of Platform | VP Engineering, CTO | "Cache invalidation across thousands of tenants is a nightmare. We need tenant-aware caching that doesn't require custom plumbing for every edge case." | "P99 latency directly correlates to tenant churn. If our customers' sites are slow, they leave — and they take their end-users with them." |
| **Bot protection & abuse prevention across tenant fleet** | Head of Security, Head of Platform, DevOps Lead | CFO, CTO | "Bots don't just attack us — they attack all 5,000 of our tenants simultaneously. We need per-tenant traffic intelligence, not just aggregate WAF rules." | "Unmitigated bot traffic is inflating our compute bill by 20-30%. Every bot request served is money burned on fake users." |
| **Observability & tenant-level debugging** | Head of Platform, SRE Lead, VP Engineering | VP Engineering, CTO | "When a tenant reports an issue, I can't isolate it from the noise of 2,000 other tenants. I need structured, tenant-aware logs — not grep across a firehose." | "Our mean-time-to-resolution is too high. Every hour of a tenant outage is churn risk and support cost." |
| **Infrastructure cost management & unit economics** | Head of Platform, Staff Engineer (Infra) | CFO, CEO, VP Finance | "I need to attribute infra cost per tenant so we can model unit economics accurately. Right now we're guessing." | "If our infra cost per tenant exceeds what we charge them, the business model breaks. I need cost predictability — Flex Commit gives me that." |
| **AI features for tenants (AI Gateway, v0 Platform API)** | VP Engineering, Head of Product, Head of AI/ML | CEO, CPO, CTO | "We want to offer AI-powered features to our tenants without building and maintaining our own model routing, observability, and fallback infrastructure." | "AI is our differentiation play. If we can ship AI features to tenants faster than competitors, we win the market — and Vercel's AI stack lets us do it without a dedicated ML infra team." |
| **Global performance & China delivery** | Head of Platform, VP Engineering, SRE Lead | CTO, VP International / GM | "Our tenants serve users in 40+ countries. We need edge delivery that doesn't require us to manage multi-region infrastructure ourselves." | "International expansion is a board priority. If our platform can't perform globally, we lose deals to competitors who can." |

---

### Technical Signals

- **High domain count relative to team size** — A company with 10 engineers and 500+ domains is almost certainly a platform. The internal metric is teams with >100 custom domains on a single project.
- **ISR usage is** `yes` — Platform companies almost universally lean on ISR for tenant-aware content delivery
- **Wildcard subdomains (**`*.brand.com`**)** — A strong technical indicator of multi-tenant architecture
- **`x-matched-path`** routing patterns — For Next.js customers, path-based routing with tenant identifiers is a platform signal
- **Cloudflare SSL for SaaS usage** — If they're already on Cloudflare's SSL for SaaS product, they're a platform company solving the domain problem imperfectly
- **Rapid domain growth** — Domains growing faster than headcount is a dead giveaway
- **Lots of projects in a single team** — Teams with >100 projects suggest they're spinning up isolated environments per tenant (Subhosting pattern)

### Business Signals

- **Their marketing says "for [industry] teams"** — They sell *to* a segment, implying each customer gets their own instance
- **They have a "create a workspace" or "create a site" flow** — Each workspace = a tenant = a Vercel deployment
- **Pricing is per seat/workspace** — Their monetization is tied to tenant count, not just user count
- **They describe themselves as "powering" other companies' experiences** — e.g., "Mintlify powers docs for 1,000+ API companies"
- **B2B2C or B2B2B business model** — There's always an end-customer downstream from their direct customer
- **Developer-facing company in a vertical** — API documentation platforms, headless CMS companies, embedded analytics tools
- **They use the word "tenant", "workspace", "org", or "instance"** in their product docs or codebase

### Discovery Questions to Confirm

- *"How does a new customer get from signup to a live, branded experience? What does that provisioning flow look like?"*
- *"Do your customers bring their own domain, or do they get a subdomain under your brand?"*
- *"How many unique domains or subdomains are you managing today, and what does that look like in 2 years?"*
- *"When something goes wrong for one customer, how do you isolate and debug that vs. it being a global platform issue?"*
- *"What does your infra team spend most of their time on that isn't core product work?"*

---

## Quick Battlecard

### One-Line Pitch

> *"Vercel is the infrastructure layer that lets platform companies focus on their product — not on building a mini-CDN, SSL manager, and deployment pipeline for every customer they serve."*

### Why Vercel Wins

- Automatic SSL + custom domain management at any scale — no engineering required
- ISR and Edge Functions built for multi-tenant content delivery
- First-class Next.js support (most platforms are built on Next.js)
- Proven at scale: Mintlify (docs for Anthropic, Coinbase, Replit), VTEX (3,000+ merchants), Zapier, Hashnode
- Vercel Shield + BotID protects all tenants simultaneously
- Flex Commit pricing grows with the platform — as their tenant count grows, so does our contract

### Why They Leave (Competitive Risks)

- **Cloudflare (CF):** "It's cheaper / free" — Counter: Mintlify chose Vercel over *free* CF because the managed value (ISR Shield, Next.js integration, DX) made it worth it. Ask them: *"How much engineering time would you spend rebuilding what Vercel handles out of the box?"*
- **AWS/DIY:** "We want more control" — Counter: "AWS gives you primitives. You still need to build the SSL automation for 10,000 domains, the ISR caching layer with per-tenant invalidation, the CDN configuration, the CI/CD pipeline, the domain verification flow, and the observability stack to debug across tenants. That's 3-5 engineers for 6+ months, and then you maintain it forever. Vercel gives you all of that as managed infrastructure. You keep full control of your product layer — we handle the infrastructure layer underneath it."
- **Netlify:** Lacks ISR depth, no platform-grade multi-tenant tooling, weaker Next.js story

### Objection Handling

- *"We're already on Cloudflare"* — Ask if they're using SSL for SaaS. If yes: "We can replace that with a better experience that's native to your Next.js app. Cloudflare doesn't know anything about your app layer — Vercel does."
- *"It's too expensive"* — Model cost per tenant vs. their infra + eng time today. Flex Commit can be structured to match their growth curve.
- *"We have engineering bandwidth to build this"* — "What's the opportunity cost? Every sprint spent on SSL automation or ISR cache logic is a sprint not spent on your product."

### Key Vercel Products to Lead With

1. Multi-Tenant Projects (Domain management + ISR)
2. Fluid Compute (I/O-heavy tenant workloads = massive savings. Platform functions constantly fetch tenant-specific data from CMS/DB/APIs — Fluid Compute bills only active CPU, not idle I/O wait. At thousands of tenants, this compounds into material unit economics improvement. Pair with Flex Commit for the full cost story.)
3. Vercel Shield (ISR Shield for proxy architectures)
4. BotID (tenant-aware abuse prevention)
5. Observability+ (Log Drains for per-tenant debugging)
6. AI Gateway + v0 Platform API (for platforms adding AI features for their customers)

---

## Land and Expand Motion

Platform deals naturally expand as tenant count grows. Reps should plan the account trajectory over 12-18 months, not just the initial deal.

| Stage | Timeline | Product | What Happens | Expansion Signal |
| --- | --- | --- | --- | --- |
| **Land: Multi-Tenant Infra** | Month 1-3 | Multi-Domain Projects + ISR + Flex Commit | The core platform deal: custom domains at scale, tenant-aware caching, automatic SSL. This is what they came for. Size the initial Flex Commit to current tenant count + 20% buffer. | Domain count growing. Ask: "How many tenants are you onboarding per month? What does your domain count look like in 12 months?" |
| **Expand: Security & Observability** | Month 3-6 | BotID + Observability+ + Vercel Shield | Once the platform is live on Vercel, security and debugging become the next pain. Bots attack the tenant fleet, the support team can't isolate tenant-specific issues, and the proxy architecture needs Shield for origin protection. | Support tickets about bot traffic or tenant-specific debugging. Ask: "How are you handling bot traffic across your tenant fleet today? When a tenant reports an issue, how long does it take to isolate?" |
| **Expand: AI for Tenants** | Month 6-12 | AI Gateway + v0 Platform API | The platform wants to offer AI features to their tenants (smart search, content generation, AI-powered workflows). AI Gateway consolidates model routing; v0 Platform API lets tenants generate experiences. This is the Whop "Whop Agent" motion. | Product team discussing AI features for tenants. Ask: "Are your tenants asking for AI-powered capabilities? What if they could generate content or apps from within your platform?" |
| **Expand: Commit Growth** | Month 12-18 | Flex Commit renewal + expansion | Tenant count has grown, AI features are driving new consumption, and the commit naturally needs to increase. The renewal is a celebration of growth, not a negotiation. Multi-year extensions lock in the relationship. | Usage approaching commit ceiling. New product lines (AI, China Delivery) driving additional consumption. Ask: "Your tenant count has doubled since we started — let's right-size the commit to match and lock in rates for the next 3 years." |

**Pro tip:** The land deal for platforms is almost always driven by the domain/SSL pain. Don't try to sell the full stack on day one. Get them live on Multi-Domain Projects, prove the value with their first 1,000 tenants, then expand into security, observability, and AI as the operational pain surfaces.

---

*Sources: Vercel for Platforms GTM Resource Center, Mintlify deal notes, Platform ICP WIP, Multi-Tenant Customer Framework, d0 platform customer revenue data, brain-rauchg, brain-craighead, Vercel for Platforms Product Brief.*
