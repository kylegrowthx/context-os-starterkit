# Vercel Platform: Comprehensive Documentation Report

*Last researched: February 24, 2026*

---

## Sources

This report was compiled by systematically mapping and scraping Vercel's entire public documentation site (~200 URLs discovered). The following 25 doc pages were directly analyzed in full:

| # | Source URL | Covers |
|---|-----------|--------|
| 1 | [vercel.com/docs](https://vercel.com/docs) | Platform overview & landing page |
| 2 | [vercel.com/docs/deployments](https://vercel.com/docs/deployments) | Deployment system, environments, Git integration |
| 3 | [vercel.com/docs/functions](https://vercel.com/docs/functions) | Vercel Functions, runtimes, regions |
| 4 | [vercel.com/docs/fluid-compute](https://vercel.com/docs/fluid-compute) | Fluid compute model, concurrency, bytecode caching |
| 5 | [vercel.com/docs/routing-middleware](https://vercel.com/docs/routing-middleware) | Middleware execution, runtimes, limits |
| 6 | [vercel.com/docs/cdn-cache](https://vercel.com/docs/cdn-cache) | CDN caching, cache control headers |
| 7 | [vercel.com/docs/storage](https://vercel.com/docs/storage) | Storage overview, product comparison |
| 8 | [vercel.com/docs/vercel-blob](https://vercel.com/docs/vercel-blob) | Blob storage, SDK methods, durability |
| 9 | [vercel.com/docs/edge-config](https://vercel.com/docs/edge-config) | Edge Config, latency, replication |
| 10 | [vercel.com/docs/ai-gateway](https://vercel.com/docs/ai-gateway) | AI Gateway, providers, BYOK |
| 11 | [vercel.com/docs/ai-sdk](https://vercel.com/docs/ai-sdk) | AI SDK, core APIs, tool calling |
| 12 | [vercel.com/docs/mcp](https://vercel.com/docs/mcp) | Model Context Protocol support |
| 13 | [vercel.com/docs/frameworks](https://vercel.com/docs/frameworks) | Framework support matrix |
| 14 | [vercel.com/docs/frameworks/full-stack/nextjs](https://vercel.com/docs/frameworks/full-stack/nextjs) | Next.js optimizations on Vercel |
| 15 | [vercel.com/docs/flags](https://vercel.com/docs/flags) | Feature flags platform |
| 16 | [vercel.com/docs/rolling-releases](https://vercel.com/docs/rolling-releases) | Canary deployments, traffic splitting |
| 17 | [vercel.com/docs/cron-jobs](https://vercel.com/docs/cron-jobs) | Cron job scheduling |
| 18 | [vercel.com/docs/integrations](https://vercel.com/docs/integrations) | Marketplace & native integrations |
| 19 | [vercel.com/docs/cli](https://vercel.com/docs/cli) | CLI commands & usage |
| 20 | [vercel.com/docs/vercel-toolbar](https://vercel.com/docs/vercel-toolbar) | Toolbar features & configuration |
| 21 | [vercel.com/docs/vercel-firewall/vercel-waf](https://vercel.com/docs/vercel-firewall/vercel-waf) | WAF, IP blocking, custom rules |
| 22 | [vercel.com/docs/security/compliance](https://vercel.com/docs/security/compliance) | Compliance certifications, infrastructure security |
| 23 | [vercel.com/docs/observability](https://vercel.com/docs/observability) | Monitoring, logs, Speed Insights |
| 24 | [vercel.com/docs/plans](https://vercel.com/docs/plans) | Plan tiers, pricing, included usage |
| 25 | [vercel.com/docs/limits](https://vercel.com/docs/limits) | Platform limits, rate limits |

---

## Table of Contents

1. [Platform Overview](#1-platform-overview)
2. [Deployment & Build System](#2-deployment--build-system)
3. [Compute Infrastructure](#3-compute-infrastructure)
4. [Routing Middleware](#4-routing-middleware)
5. [CDN & Caching](#5-cdn--caching)
6. [Storage Solutions](#6-storage-solutions)
7. [AI Infrastructure](#7-ai-infrastructure)
8. [Framework Support](#8-framework-support)
9. [Feature Flags](#9-feature-flags)
10. [Rolling Releases](#10-rolling-releases)
11. [Cron Jobs](#11-cron-jobs)
12. [Integrations & Marketplace](#12-integrations--marketplace)
13. [Developer Tools](#13-developer-tools)
14. [Security & Compliance](#14-security--compliance)
15. [Observability & Monitoring](#15-observability--monitoring)
16. [Plans & Pricing](#16-plans--pricing)
17. [Platform Limits](#17-platform-limits)

---

## 1. Platform Overview

Vercel positions itself as **"the AI Cloud"** - a unified platform for building, deploying, and scaling AI-powered web applications. It provides a complete frontend cloud infrastructure, integrating seamlessly with modern frameworks (especially Next.js, which Vercel created and maintains).

The platform combines automated Git-based deployments, a global edge network, serverless compute, managed storage, AI infrastructure, and developer tooling into a single cohesive experience. Vercel's core value proposition is allowing developers to ship faster with zero-configuration deployments while maintaining enterprise-grade performance and security.

### Core Platform Pillars

- **Build & Deploy**: Git-connected CI/CD, preview deployments, instant rollback
- **Compute**: Fluid compute (serverless functions), routing middleware, edge functions
- **Storage**: Vercel Blob, Edge Config, Marketplace databases (Postgres, Redis, etc.)
- **AI**: AI Gateway, AI SDK, MCP servers, v0, Sandbox
- **Observability**: Monitoring, Speed Insights, Web Analytics, Runtime Logs
- **Security**: WAF, Bot Management, DDoS mitigation, deployment protection, compliance certifications
- **Collaboration**: Vercel Toolbar, Comments, Feature Flags, Rolling Releases

---

## 2. Deployment & Build System

### Deployment Methods

Vercel supports four primary deployment methods:

1. **Git Integration**: Automatic deployments on push to GitHub, GitLab, Bitbucket, or Azure DevOps. Each push to a branch creates a unique preview deployment, and pushes to the production branch trigger production deployments.

2. **Vercel CLI**: Deploy directly from the terminal with `vercel` or `vercel --prod`. Useful for CI/CD pipelines and local development workflows.

3. **Deploy Hooks**: Unique URLs that trigger deployments via HTTP POST requests. Ideal for CMS webhooks, scheduled rebuilds, and external automation.

4. **REST API**: Programmatic deployment creation for advanced CI/CD integration.

### Environments

Vercel provides three default environments, plus support for custom environments:

- **Production**: Serves live traffic on your production domain. Only one active production deployment at a time.
- **Preview**: Automatically created for every push to a non-production branch. Each gets a unique URL for review and testing.
- **Development**: Local environment that mirrors Vercel's production behavior via `vercel dev`.
- **Custom Environments**: Teams can create additional environments (e.g., staging, QA) with their own environment variables and domains.

### Build System

- **Build time limit**: 45 minutes per deployment
- **Concurrent builds**: 1 (Hobby), 12 (Pro), Custom (Enterprise)
- **Build cache**: Up to 1 GB, retained for 1 month
- **Build machine types**: Standard (23 GB disk) and larger machines (up to 64 GB disk) available on Pro/Enterprise
- **Deployment limits**: 100/day (Hobby), 6,000/day (Pro), 24,000/day (Enterprise)

### Key Deployment Features

- **Instant Rollback**: Revert production to any previous deployment instantly
- **Skew Protection**: Ensures client-server consistency during deployments by routing API calls to matching deployment versions
- **Deployment Protection**: Password protection, Vercel Authentication, and Trusted IPs for securing preview and production deployments

### Microfrontends

Vercel supports microfrontend architectures, allowing teams to compose a single application from independently deployable sub-applications. Each microfrontend can be built, deployed, and scaled independently while appearing as a unified experience to end users. The CLI provides `vercel microfrontends` for managing configuration, and the feature integrates with Vercel's preview deployment system so teams can test individual microfrontends in isolation or in combination.

---

## 3. Compute Infrastructure

### Fluid Compute

Fluid compute is Vercel's next-generation serverless execution model - a hybrid between traditional serverless and persistent servers. Key innovations include:

- **Optimized Concurrency**: Functions can handle multiple requests simultaneously on a single instance, reducing cold starts and improving efficiency. Default concurrency varies by plan (1 for Hobby, 10 for Pro/Enterprise on Node.js).

- **Bytecode Caching**: On Node.js 20+, Vercel caches compiled bytecode between invocations, dramatically reducing cold start times for subsequent requests.

- **Isolation Boundaries**: Each function execution is sandboxed with error isolation. A crash in one request doesn't affect concurrent requests on the same instance.

- **Background Processing**: The `waitUntil` API allows functions to continue processing after sending a response (e.g., logging, analytics, cache updates).

- **Cross-Region Failover**: If a region becomes unavailable, traffic automatically routes to the nearest healthy region.

### Vercel Functions

Serverless functions that run your backend code. Key specifications:

- **Primary Runtime**: Node.js (the main supported runtime for Vercel Functions)
- **Community Runtimes**: Python, Go, Ruby, Rust (available but with varying levels of support)
- **Middleware Runtimes**: Edge (lightweight V8-based), Bun (for routing middleware)
- **Default Region**: iad1 (Washington D.C., US East)
- **Available Regions**: 20+ AWS-based regions worldwide
- **Pricing Model**: Based on three metrics - Active CPU time, Provisioned Memory, and Invocations
- **Data Source Proximity**: Functions can be configured to run close to your database for lower latency

### Edge Runtime

A lightweight JavaScript runtime running on Vercel's edge network for ultra-low latency. Ideal for:

- Authentication checks
- A/B testing
- Geolocation-based routing
- Request/response transformations

---

## 4. Routing Middleware

Routing Middleware executes code before a request is processed, running globally before the cache. It is built on fluid compute and is effective for personalizing statically generated content.

### Capabilities

- Redirect, rewrite, or modify requests before they reach your application
- Add, modify, or remove headers
- Personalize responses based on geolocation, cookies, or other request data
- Runs on Edge (default), Node.js, or Bun runtimes

### Implementation

Create a `middleware.ts` file at your project's root directory. For Next.js 16+, the file is renamed to `proxy.ts` and runs on Node.js only.

### Limits

| Name | Limit |
|------|-------|
| Maximum URL length | 14 KB |
| Maximum request body length | 4 MB |
| Maximum number of request headers | 64 |
| Maximum request headers length | 16 KB |

---

## 5. CDN & Caching

Vercel operates a global CDN with intelligent caching strategies:

### Cache Control Headers (Priority Order)

1. **Vercel-CDN-Cache-Control**: Controls only Vercel's CDN cache (not passed to clients)
2. **CDN-Cache-Control**: Industry-standard CDN cache control header
3. **Cache-Control**: Standard HTTP cache header (affects both CDN and browsers)

### Caching Behavior

- Static files are automatically cached on the CDN
- Maximum cacheable response size: 10 MB
- Supports `stale-while-revalidate` for serving stale content while fetching fresh data
- `Vary` header support for content negotiation
- Cacheable responses must be GET or HEAD requests with 200, 301, 302, 307, 308, 404, or 410 status codes

### Data Transfer Types

- **Fast Data Transfer**: City-level, ultra-low latency delivery through the global edge network
- **Fast Origin Transfer**: Data transfer between your functions and origin servers
- **Blob Data Transfer**: Cost-optimized delivery for large static assets through regional hubs

---

## 6. Storage Solutions

### Vercel Blob

Object storage for uploading and serving files. Uses Amazon S3 as the underlying infrastructure.

- **Durability**: 99.999999999% (11 nines)
- **Availability**: 99.99% (4 nines)
- **Access Modes**: Private (authenticated reads) or Public (anyone with URL)
- **Region Selection**: Available in all 20 regions
- **Multipart Uploads**: Supported for files over 100 MB
- **Caching**: CDN-cached for up to 1 month by default, customizable via `cacheControlMaxAge`
- **Conditional Writes**: Optimistic concurrency control via ETags
- **SDK Methods**: `put()`, `get()`, `head()`, `del()`, `copy()`, `list()`, `upload()` (client-side)

### Edge Config

Ultra-low latency global data store for reading configuration data at the edge. Data is actively replicated to all regions in the Vercel CDN.

- **Read Latency**: Most lookups under 1ms, P99 under 10ms
- **Best For**: Feature flags, A/B testing, critical redirects, IP blocking
- **Scope**: Can be connected to multiple projects
- **Access**: Read access via SDK with tokens, write access via REST API
- **Runtime Support**: Optimized for Edge and Node.js runtimes; other runtimes (Ruby, Go, Python) available upon request

### Deprecated First-Party Storage

Vercel previously offered **Vercel KV** (Redis-compatible key-value store) and **Vercel Postgres** as first-party products. Both have been deprecated in favor of marketplace partners - Upstash for KV and Neon for Postgres. Existing users were migrated to the respective providers. The current first-party storage offering is limited to Blob and Edge Config.

### Marketplace Storage (Third-Party)

Through the Vercel Marketplace, teams can provision and manage databases from partner providers. Vercel automatically injects credentials as environment variables, and all billing is consolidated through Vercel.

- **Relational Databases (Postgres)**: Neon, Prisma, Supabase, AWS, Nile
- **Key-Value / Redis**: Upstash, Redis
- **Document / NoSQL**: MongoDB Atlas, Convex
- **SQLite**: Turso Cloud
- **Vector Databases**: For AI embeddings, semantic search, and recommendation systems (available through marketplace providers)
- **Analytics**: MotherDuck

---

## 7. AI Infrastructure

### AI Gateway

A unified API that provides access to hundreds of AI models from multiple providers:

- **Zero Markup**: No additional cost on top of provider token prices
- **Bring Your Own Key (BYOK)**: Use your own API keys for any supported provider
- **Single API Surface**: One consistent interface regardless of which model you use
- **Supported Providers**: Access models from OpenAI, Anthropic, Google, Mistral, Groq, xAI, Deep Infra, fal, and more through marketplace integrations
- **Languages**: TypeScript, Python, cURL support

### AI SDK

An open-source TypeScript toolkit for building AI-powered applications:

- **Core APIs**: `generateText`, `generateObject`, `streamText`, `streamObject`
- **Tool Calling**: Define and use tools with full type safety
- **Framework Native**: Works seamlessly with Next.js, SvelteKit, and other frameworks
- **Provider Agnostic**: Switch between AI providers without code changes

### Model Context Protocol (MCP)

Vercel supports MCP - a standard interface for LLMs to communicate with external tools and data sources:

- **Deploy MCP Servers**: Host your own MCP servers on Vercel
- **Vercel MCP Server**: Use Vercel's own MCP server for platform management
- **AI SDK Integration**: Initialize MCP clients and call MCP tools through the AI SDK

### Additional AI Resources

- **v0**: AI-powered UI generation tool that creates React components and full pages from natural language descriptions
- **Vercel Sandbox**: A secure, isolated code execution environment designed for AI agents. Allows LLMs to run untrusted code safely without risking the host environment - useful for code interpreters, automated testing, and agent-driven development workflows.
- **Agent Resources**: Integrations and infrastructure specifically designed for AI agent workflows, including browser automation partners and conversational AI tools

---

## 8. Framework Support

Vercel supports a wide range of web frameworks. The current officially featured frameworks matrix distinguishes between tiers of support:

### First-Party (Deep Integration)

- **Next.js**: The flagship framework, built and maintained by Vercel. Features include ISR (Incremental Static Regeneration), SSR streaming, Partial Prerendering (PPR), Image Optimization, Font Optimization, OG Image Generation, Middleware, and Draft Mode.

### Featured Frameworks (Official Matrix)

These frameworks have first-class documentation and optimized build/deploy pipelines on Vercel:

- **Full-Stack**: Next.js, SvelteKit, Nuxt, Remix, TanStack
- **Frontend / Static**: Astro, Vite (React, Vue, Svelte, etc.), Create React App (CRA)
- **Backend**: Nitro

### Broader Compatibility

Vercel can deploy virtually any framework that produces static output or runs on Node.js. Through the **Build Output API** - a file-system-based specification - any framework can integrate with Vercel's platform features (serverless functions, edge middleware, ISR, image optimization). Additional community-supported frameworks include Angular, Gatsby, Hugo, Jekyll, Eleventy, Docusaurus, Ember, SolidStart, Express, Hono, Fastify, and NestJS, among others.

### Next.js on Vercel (Key Optimizations)

- **ISR**: Regenerate static pages in the background without full rebuilds
- **Streaming SSR**: Progressive page rendering for faster Time to First Byte
- **Partial Prerendering (PPR)**: Combine static shells with dynamic content holes
- **Image Optimization**: Automatic format conversion (WebP/AVIF), resizing, and CDN caching
- **Font Optimization**: Automatic font subsetting and self-hosting
- **OG Image Generation**: Dynamic social card generation at the edge
- **Speed Insights & Web Analytics**: Built-in performance monitoring

---

## 9. Feature Flags

Vercel provides a complete feature flags platform:

### Capabilities

- Use Vercel as your feature flag provider, or connect third-party providers (LaunchDarkly, Statsig, Hypertune, GrowthBook, PostHog, Split)
- Unified dashboard showing all flags across providers
- Targeting rules, segments, splits, and environment controls
- A/B testing and experimentation support

### Developer Tools

- **Flags Explorer**: View and override feature flags from the Vercel Toolbar during development
- **Flags SDK**: Framework-native library for Next.js and SvelteKit with full TypeScript support

### Observability

- Track flag evaluations in Runtime Logs
- Analyze impact on user behavior in Web Analytics
- See which flags affect conversion rates and performance

---

## 10. Rolling Releases

Available on Pro and Enterprise plans, Rolling Releases enable gradual deployment rollouts:

### How It Works

1. New deployments don't serve 100% of traffic immediately
2. A configurable fraction (e.g., 5%) of visitors see the new deployment
3. Vercel shows a breakdown of key metrics between canary and current deployment
4. You can advance through stages, each serving a larger traffic fraction
5. The final stage is always 100% (full promotion)
6. At any point, use Instant Rollback to revert

### Configuration

- Configure two or more stages with increasing traffic percentages
- A 0% stage allows testing without directing any visitors to the canary
- Each rollout clones the current configuration - editing config doesn't affect in-progress rollouts

### Observability

- Deployments page shows current rolling release status
- Release candidate is badged "Canary" with traffic fraction
- Observability tab provides comparative metrics between deployments
- Use `vcrrForceCanary=true` or `vcrrForceStable=true` query parameters to force cookie assignment

### Integration with Skew Protection

Rolling Releases pair with Skew Protection to ensure backend API requests are served by code matching the frontend version the user received.

---

## 11. Cron Jobs

Time-based scheduling for automating repetitive tasks, available on all plans:

### How It Works

- Vercel makes an HTTP GET request to your production deployment URL at the configured schedule
- Configured via `vercel.json` or the Build Output API
- Uses standard cron expression syntax (minute, hour, day of month, month, day of week)
- Timezone is always UTC

### Limits

- Up to 100 cron jobs per project
- Cron expressions do not support alternative expressions like `MON`, `SUN`, `JAN`, `DEC`
- Cannot configure both day of month and day of week simultaneously

### Common Use Cases

- Automated backups
- Email and Slack notifications
- Subscription quantity updates
- Data synchronization
- Cache warming

---

## 12. Integrations & Marketplace

The Vercel Marketplace provides two types of integrations:

### Native Integrations

Two-way connections between Vercel and partner services with:

- No separate account creation required
- Billing managed through Vercel
- Products subscribable directly from the Vercel dashboard

**Notable Native Integrations:**

| Category | Integrations |
|----------|-------------|
| Storage & Databases | Neon, Supabase, Upstash, MongoDB Atlas, Prisma, Redis, AWS, Convex, Turso, Nile, MotherDuck |
| AI & ML | Deep Infra, fal, Groq, xAI |
| Authentication | Clerk, Descope |
| Observability & Monitoring | Sentry, Dash0, Rollbar, Checkly, Kubiks, Braintrust |
| CMS | Sanity |
| Payments | Stripe |
| Feature Flags & Experimentation | Statsig, Hypertune, GrowthBook, PostHog |
| Media & Video | Mux |
| AI Agents & Automation | Browserbase, Chatbase, Kernel, AssistLoop |
| Code Quality & Review | CodeRabbit, cubic, Sourcery, Autonoma AI |
| Workflow Orchestration | Inngest |

### Connectable Accounts

Connect existing third-party accounts to Vercel:

- ElevenLabs, LMNT (text-to-speech)
- Perplexity API, Replicate, Together AI (AI models)

### Integration Guides

Available guides for connecting Contentful, Sanity, Sitecore XM Cloud, Shopify, and Kubernetes.

---

## 13. Developer Tools

### Vercel CLI

A comprehensive command-line interface for managing the entire Vercel platform:

**Key Commands:**

| Command | Description |
|---------|-------------|
| `vercel deploy` | Deploy projects (default command) |
| `vercel dev` | Run local development server |
| `vercel env` | Manage environment variables |
| `vercel domains` | Manage domains |
| `vercel logs` | View runtime logs |
| `vercel blob` | Interact with Vercel Blob storage |
| `vercel cache` | Manage CDN and data cache |
| `vercel certs` | Manage SSL certificates |
| `vercel dns` | Manage DNS records |
| `vercel rollback` | Roll back production deployments |
| `vercel rolling-release` | Manage rolling releases |
| `vercel bisect` | Binary search through deployments to surface issues |
| `vercel mcp` | Set up MCP client configuration |
| `vercel microfrontends` | Work with microfrontends configuration |
| `vercel redirects` | Manage project-level redirects |
| `vercel webhooks` | Manage webhooks (beta) |

**Installation:** `npm i -g vercel` (also via pnpm, yarn, bun)

**CI/CD Usage:** Create a token at vercel.com/account/tokens and use `--token` flag for authentication.

### Vercel Toolbar

A development assistance tool embedded in preview deployments:

- **Comments**: Leave visual feedback directly on deployments
- **Feature Flags Explorer**: View and override feature flags
- **Draft Mode**: Preview unpublished CMS content
- **Edit Mode**: Edit content in real-time
- **Layout Shift Tool**: Identify elements causing layout shifts
- **Interaction Timing Tool**: Inspect interaction latency and INP
- **Accessibility Audit**: Check WCAG 2.0 Level A and AA compliance
- **Open Graph Inspector**: View OG properties and link previews
- **Branch Switching**: Quickly switch between branches
- **Deployment Sharing**: Share deployment URLs with proper permissions

**Availability:** Enabled by default on all preview deployments. Can be extended to production and localhost via browser extension.

### REST API

Programmatic access to the full Vercel platform, including deployments, domains, environment variables, teams, and more. Supports token-based authentication.

---

## 14. Security & Compliance

### Vercel WAF (Web Application Firewall)

Multi-layered security at the edge:

- **IP Blocking**: Block specific IPs or CIDR ranges
- **Custom Rules**: Define rules based on request attributes (path, headers, geography, etc.)
- **Managed Rulesets**: Pre-configured protection against common attack patterns (OWASP Top 10)
- **Actions**: Block, challenge, redirect, or allow requests
- **Propagation**: Rules propagate globally within 300ms
- **Instant Rollback**: Revert WAF rule changes instantly

**WAF Limits by Plan:**

| Feature | Hobby | Pro | Enterprise |
|---------|-------|-----|-----------|
| IP Blocking Rules | 50 | 5,000 | Custom |
| Custom Rules | 5 | 100 | Custom |
| Managed Rulesets | - | Included | Included |

### Bot Management

- **BotID**: Identify and categorize bot traffic
- **Bot protection rules**: Configure different responses for different bot categories

### DDoS Mitigation

- Automatic DDoS protection at the network and application layers
- No configuration required - built into the platform

### Deployment Protection

- **Password Protection**: Require a password to access deployments
- **Vercel Authentication**: Limit access to team members
- **Trusted IPs**: Restrict access to specific IP ranges (Enterprise)
- **RBAC**: Role-based access control with Owner, Member, Developer, and Viewer roles

### Compliance Certifications

| Certification | Details |
|--------------|---------|
| SOC 2 Type 2 | Annual audit |
| ISO 27001:2022 | Information security management |
| GDPR | Data protection regulation |
| PCI DSS | Payment card industry standard |
| HIPAA | Healthcare data (Enterprise) |
| TISAX | Automotive industry security |
| EU-U.S. Data Privacy Framework | Transatlantic data transfers |

### Infrastructure Security

- **Cloud Provider**: AWS-based with 20+ regions
- **Network**: Anycast global network
- **Encryption at Rest**: AES-256
- **Encryption in Transit**: TLS 1.3
- **High Availability**: Multi-AZ failover
- **Data Backup**: Every 2 hours, 30-day retention

---

## 15. Observability & Monitoring

### Tracked Events & Insights

| Insight Category | Description |
|-----------------|-------------|
| Functions | Invocations, duration, errors, cold starts |
| External APIs | Latency and errors for third-party API calls |
| Edge Requests | Edge network request metrics |
| Middleware | Routing middleware execution metrics |
| AI Gateway | AI model usage, latency, token counts |
| Cache | Hit rates, miss rates, revalidation metrics |

### Monitoring Features

- **Runtime Logs**: Real-time function execution logs (1hr Hobby, 1 day Pro, 3 days Enterprise)
- **Build Logs**: Stored indefinitely for each deployment
- **Speed Insights**: Real User Monitoring (RUM) for Core Web Vitals
- **Web Analytics**: Privacy-friendly, cookie-free analytics
- **Observability Plus**: Enhanced insights with query builder for custom analysis

### Notebooks

Interactive analysis environment for exploring observability data, building custom queries, and creating reports.

---

## 16. Plans & Pricing

### Plan Tiers

| Feature | Hobby (Free) | Pro | Enterprise |
|---------|-------------|-----|-----------|
| Projects | 200 | Unlimited | Unlimited |
| Deployments/Day | 100 | 6,000 | Custom |
| Concurrent Builds | 1 | 12 | Custom |
| Team Members | 1 | Unlimited | Unlimited |
| Commercial Use | No | Yes | Yes |
| Support | Community | Email | Dedicated |

### Hobby Plan Included Usage

| Resource | Included |
|----------|----------|
| Active CPU | 4 CPU-hrs |
| Provisioned Memory | 360 GB-hrs |
| Invocations | 1 million |
| Fast Data Transfer | 100 GB |
| Fast Origin Transfer | Up to 10 GB |
| Build Execution | 6,000 minutes |
| Image Optimization | 1,000 source images |

### Pro Plan

Credit-based pricing with included allowances and pay-as-you-go for additional usage. Notable per-unit costs for overages:

| Resource | Cost |
|----------|------|
| Function Invocations | $0.60 per 1M |
| Image Optimization (Legacy) | $5.00 per 1,000 |
| Edge Config Reads | $3.00 per unit |
| Web Analytics Events | $0.00003 per event |
| Monitoring Events | $1.20 per 1M |
| Observability Plus Events | $1.20 per 1M |
| Drains | $0.50 per GB |

### Enterprise Plan

Custom pricing with dedicated support, advanced security features (HIPAA, Trusted IPs, custom WAF rules), SLAs, and higher limits.

---

## 17. Platform Limits

### General Limits

| Resource | Hobby | Pro | Enterprise |
|----------|-------|-----|-----------|
| Projects | 200 | Unlimited | Unlimited |
| Deployments/Day | 100 | 6,000 | Custom |
| Build Time | 45 min | 45 min | 45 min |
| Proxied Request Timeout | 120s | 120s | 120s |
| Routes per Deployment | 2,048 | 2,048 | Custom |
| Static File Upload Size | 100 MB | 1 GB | N/A |
| Concurrent Builds | 1 | 12 | Custom |
| Disk Size | 23 GB | Up to 64 GB | Up to 64 GB |
| Cron Jobs per Project | 100 | 100 | 100 |
| Domains per Project | 50 | Unlimited* | Unlimited* |
| CLI Source Files | 15,000 max | 15,000 max | 15,000 max |
| Env Vars per Environment | 1,000 | 1,000 | 1,000 |
| Env Var Total Size | 64 KB | 64 KB | 64 KB |

### Runtime Logs Retention

- Hobby: 1 hour
- Pro: 1 day
- Enterprise: 3 days
- Build logs: Stored indefinitely

### Notable Technical Limits

- WebSockets are not supported by Vercel Functions (use third-party solutions)
- Build cache: 1 GB maximum, 1 month retention
- Maximum cacheable response size: 10 MB
- No support for cron expressions with text day/month names

### Rate Limits (Selected Key Limits)

| Action | Hobby | Pro | Enterprise |
|--------|-------|-----|-----------|
| Deployments/hour | 100 | 450 | 1,800 |
| Deployments/5 min | 60 | 120 | 300 |
| Deploy Hook triggers/hour | 60 | 60 | 60 |
| Token creation/hour | 32 | 32 | 32 |
| Domains creation/hour | 120 | 120 | 120 |
| Team creation/day | 5 | 25 | 25 |
| Team member creation/hour | 50 | 150 | 300 |

---

## Summary

Vercel has evolved from a frontend deployment platform into a comprehensive cloud infrastructure provider with a strong focus on AI-powered applications. Its key differentiators include:

1. **Developer Experience**: Zero-config deployments, preview environments for every PR, and a rich CLI/toolbar ecosystem
2. **Performance**: Global edge network, fluid compute with optimized concurrency, and intelligent caching
3. **AI-First**: Unified AI Gateway, AI SDK, MCP support, and purpose-built AI agent infrastructure
4. **Framework Excellence**: First-class Next.js support with deep optimizations, plus broad support for all major frameworks
5. **Enterprise Readiness**: SOC 2, ISO 27001, HIPAA, GDPR compliance, WAF, bot management, and RBAC
6. **Integrated Storage**: Blob storage, Edge Config, and a rich marketplace of database providers - all with consolidated billing

The platform serves a spectrum from individual developers (Hobby plan) to large enterprises, with pricing that scales from free to custom enterprise agreements.

---

*Report compiled from Vercel's official documentation at vercel.com/docs*
