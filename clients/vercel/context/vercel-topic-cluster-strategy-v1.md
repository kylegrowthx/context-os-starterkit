# Vercel — Topic Cluster Strategy

<metadata>
purpose: Defines the 5 topic cluster pillars for Vercel's editorial content strategy, plus AI Gateway programmatic workstream as a separate parallel effort
audience: AI agents and team members working on this account
summary: 5 JTBD-driven topic clusters for editorial content, with AI Gateway appearing both as a cluster (editorial) and as a separate programmatic workstream (own tab, own team, own codebase). Composable Commerce merged into Frontend Cloud. Programmatic Stacks reclassified as a publishing surface. Includes cross-cutting narrative layer for AI-native platform positioning.
token_estimate: medium
related: clients/vercel/vercel-client-context-v1.md, clients/vercel/context/vercel-engagement-prep-brief-v1.md
domain: client
confidence: current
context_tier: 2
last_updated: 2026-03-03
</metadata>

---

## Why These 5 Pillars

Vercel's keyword universe spans 139,000+ tracked terms across three Airtable tables (Editorial Keywords, Keywords Internal, AI Gateway Keywords). Rather than clustering bottom-up from keyword similarity, we defined pillars top-down from four inputs:

1. **Stakeholder priorities** — Cody Henshaw's ranked strategic priorities from the Feb 24 kickoff and Feb 4 scope call
2. **Product architecture** — Vercel's five product lines (Platform, Next.js, v0, AI SDK, AI Gateway) each serve distinct search audiences
3. **Publishing surface constraints** — Different content types route through different approval paths and codebases, which directly affects speed-to-publish and volume capacity
4. **Competitive dynamics** — Each cluster faces a different competitive set (e.g., AI Gateway competes with Open Router and Ollama, Frontend Cloud competes with Netlify and AWS Amplify)

The result is 5 topic clusters that map cleanly to Vercel's editorial content strategy, with a cross-cutting narrative layer for the AI-native platform positioning and Programmatic Stacks treated as a publishing surface (not a cluster).

**Important distinction:** AI Gateway appears in two places. As a topic cluster (#1 below), it guides editorial content: blog posts, /i articles, thought leadership about model selection, AI infrastructure, and routing strategy. Separately, the AI Gateway programmatic workstream (own Airtable tab, own team, own codebase) handles the ~170 template-driven model pages, comparison tables, and leaderboard. These are different efforts with different teams, timelines, and content types.

---

## The 5 Cluster Pillars

### 1. AI Gateway & Model Traffic (Editorial)

**What it covers:** Editorial content about AI model selection strategy, routing architecture, pricing analysis, performance benchmarking methodology, and the broader "how to choose and manage AI models" search landscape. Think blog posts, /i articles, and thought leadership, not the template-driven model pages (those are the programmatic workstream).

**Why it's a standalone pillar:** AI Gateway has its own keyword table (70,961 terms), its own competitive landscape (Open Router, Ollama, Together AI), and a distinct search audience (AI/ML engineers making infrastructure decisions). The editorial opportunity here is separate from the programmatic model pages: "how do you choose the right model for your use case?" is a fundamentally different piece of content than a model spec page. Keeping this as a cluster ensures editorial AI Gateway content gets planned, prioritized, and tracked alongside the other pillars.

**Primary publishing surface:** /i section + blog (high-value thought leadership)
**Programmatic counterpart:** AI Gateway pages (separate tab, separate team, separate frontend repo)
**Competitive set:** Open Router, Ollama, Together AI, Hugging Face
**Strategic priority:** #4 per Cody's ranking, but highest near-term velocity opportunity

---

### 2. AI SDK & Agent Development

**What it covers:** Keywords related to building AI-powered applications, agent development tooling, the Vercel AI SDK, streaming responses, tool calling, and the broader "AI app development" search landscape.

**Why it's a standalone pillar:** Vercel is executing a major GTM shift toward agents and AI — March 2026 preview, April launch. Cody identified this as where Vercel's growth is heading. The AI SDK is open-source with its own developer community and distinct keyword universe (how-to queries, integration guides, framework comparisons). This cluster captures the "building" side of Vercel's AI story, complementing AI Gateway's "infrastructure" side.

**Primary publishing surface:** /i section + blog (high-value pieces)
**Competitive set:** LangChain, LlamaIndex, Semantic Kernel, custom implementations
**Strategic priority:** Central to Vercel's 2026 growth narrative

---

### 3. Frontend Cloud & Platform

**What it covers:** Keywords related to web deployment, hosting, serverless functions, edge computing, performance optimization, CI/CD, and the core Vercel platform value proposition. The "proven" side of Vercel — what generates the majority of revenue today.

**Why it's a standalone pillar:** This is Vercel's primary revenue driver and broadest keyword universe. The search landscape here is mature and competitive (Netlify, AWS Amplify, Cloudflare Pages, Railway). Content ranges from beginner deployment tutorials to enterprise architecture guides. Cody described this as the "pre-cut pineapple" positioning — accessible utility that just works.

**Primary publishing surface:** /i section (velocity play) + blog (flagship pieces with CEO approval)
**Competitive set:** Netlify, AWS Amplify, Cloudflare Pages, Railway, Render
**Strategic priority:** Revenue foundation — must maintain while investing in AI growth

**Note — Composable Commerce lives here.** Headless commerce, Shopify Hydrogen, storefront performance, and e-commerce architecture keywords are sub-topics within this cluster. Commerce was initially considered as a standalone pillar but merged here because: (a) it wasn't mentioned in any stakeholder transcript as a near-term priority, (b) the value prop is the same as Frontend Cloud ("your site performs better on Vercel"), and (c) commerce-specific integrations will also appear on stacks pages.

---

### 4. Developer Ecosystem & Tooling

**What it covers:** Keywords related to Next.js, Turborepo, ShadCN/ui, and the broader open-source ecosystem Vercel maintains. Includes framework tutorials, migration guides, component libraries, and developer experience content.

**Why it's a standalone pillar:** These open-source projects have their own massive search audiences (Next.js alone dominates React framework searches). The content serves a top-of-funnel awareness function — developers discover Vercel through its open-source tools. These projects also form the backbone of the cross-linking network (100+ OSS project sites). The ecosystem cluster feeds every other pillar: developers who learn Next.js become Frontend Cloud customers, those building AI apps use AI SDK, and the stacks pages reference these tools.

**Primary publishing surface:** /i section + KB (developer docs, Timothy/DevX owns)
**Competitive set:** Remix, Astro, Vite, Create React App (framework level)
**Strategic priority:** Top-of-funnel acquisition engine

---

### 5. Competitor Comparisons & Alternatives

**What it covers:** "Vercel vs X" comparison keywords, "X alternatives" keywords, migration guides, and feature-by-feature competitive content. Spans all product lines — not just Frontend Cloud.

**Why it's a standalone pillar:** Comparison keywords have fundamentally different search intent (bottom-of-funnel, high purchase intent), different content formats (structured comparisons, feature tables, benchmark data), and different competitive dynamics (you're directly naming competitors). They also represent the highest-leverage opportunity for Vercel's cross-linking advantage — when you have 100+ OSS project sites pointing back to your comparison pages, you win contested SERPs. Kirkland is already prototyping comparison page UI for AI Gateway. Pulling these into their own cluster ensures they get prioritized correctly rather than buried within each product cluster.

**Primary publishing surface:** /i section (comparison articles) + AI Gateway (model comparisons)
**Competitive set:** The competitors themselves — whoever ranks for "[their brand] vs Vercel"
**Strategic priority:** Highest conversion value per keyword

---

## Publishing Surfaces (Not Clusters)

These are delivery mechanisms that draw keywords from the clusters above. Each keyword should be tagged with the publishing surface(s) it's eligible for, which directly affects prioritization (speed-to-publish, approval friction).

**Blog** — CEO (Guillermo) approval required via Dan Fein. Highest quality bar. Code snippets must be executable. Best for flagship pieces that establish thought leadership. Draws from all 5 clusters.

**/i Section** — Cody's autonomous space. Same template as blog, no CEO approval. Zero content currently. Highest velocity opportunity. Draws from all 5 clusters.

**Stacks Pages (Programmatic)** — Template-driven "Why X runs on Vercel" pages. Eric Dodds owns. Scale target: 5,300 to 40,000+ pages. Cross-linking from 100+ OSS sites is strongest here. Draws primarily from Cluster 3 (Frontend Cloud) and Cluster 4 (Developer Ecosystem). Originally considered as a standalone cluster but reclassified: stacks pages are a publishing mechanism, not a content strategy pillar. The keywords that populate them come from other clusters.

**AI Gateway Pages (Programmatic Workstream)** — Separate frontend repo ("front"). Josh Wolk's team owns. ~170 existing pages. This is the programmatic counterpart to Cluster 1's editorial strategy. Handles model-specific pages, comparison tables, and the leaderboard. Runs in its own Airtable tab with its own team and timeline. Also serves the model comparison subset of Cluster 5 (Competitor Comparisons).

**KB (Knowledge Base)** — Timothy/DevX owns. Lower quality bar than blog. Best for technical documentation and reference content. Draws primarily from Cluster 4 (Developer Ecosystem).

---

## Cross-Cutting Narrative: AI-Native Development Platform

Vercel is positioning as the AI-native development platform — not just a frontend deployment tool. This isn't a separate keyword cluster (there's no distinct search universe for "AI-native platform"), but it's a content *angle* that should run through Clusters 1, 2, and 3:

- **AI Gateway content** should position Vercel as the infrastructure layer for AI apps, not just a model router
- **AI SDK content** should emphasize that building AI features is a first-class workflow on Vercel, not a bolt-on
- **Frontend Cloud content** should increasingly frame deployment in the context of AI applications, not just static sites

This narrative bridges the "proven" (frontend cloud) and "growing" (AI platform) sides of Vercel's identity — what Cody described as the brand duality between accessible utility and premium quality.

---

## Next Steps

1. ~~Populate the Topic Clusters table in the Content OS Airtable with these 5 pillars~~ DONE
2. ~~Define personas (Individual Developer, Technical Decision Maker, AI/ML Engineer)~~ DONE
3. ~~Separate AI Gateway into editorial cluster + programmatic workstream~~ DONE
4. Map the 139K+ keywords into these clusters using intent-level categorization
5. Build composite prioritization score factoring in publishing surface, cross-link eligibility, and business relevance
6. Identify "first 30 days" keyword targets per cluster

---

*Update this file when clusters are refined based on keyword mapping results or stakeholder feedback.*
