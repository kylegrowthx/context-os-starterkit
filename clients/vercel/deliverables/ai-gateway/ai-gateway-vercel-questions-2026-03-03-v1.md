# Vercel AI Gateway: Questions for the Team

<metadata>
purpose: Questions and requests to send to Vercel's AI Gateway team before Thursday's call
audience: Vercel team (Cody Henshaw, Jerilyn Zheng, Matthew Lenhard)
summary: Five questions covering content delivery format, data model access, frontend access, technical SEO issues found, and UI exploration plans
domain: client
confidence: current
context_tier: 2
last_updated: 2026-03-03
</metadata>

---

Hey team,

Following up from our Friday call. We've been heads down on the keyword research and competitive audit, and we're making good progress. We want to start shipping content improvements to the AI Gateway pages this week while we continue working on the bigger UI and data integration pieces.

A few questions so we can move quickly:

---

## 1. Content Format for Page Updates

We're preparing content updates (optimized titles, headings, descriptions, FAQ sections) for all ~170 AI Gateway pages. What format would make it easiest for your team to implement these changes?

JSON is ideal on our end because we're building a workflow to generate the updates at scale. But if there's a specific format or structure that maps better to how your pages are built, we'll match it.

## 2. Data Model

Can you share the data model for the AI Gateway pages? Knowing which fields are editable text vs. data-driven will help us structure our content to slot in cleanly. Even a sample JSON of what a single model page looks like on the backend would be a huge help.

## 3. Frontend Access

Where are we on Next.js frontend access? This isn't a blocker for the content work we're doing now (we can send you JSON and you publish), but we'll need it for the next phase when we start building UI components and richer page elements.

## 4. Technical SEO Heads-Up for the Comparison Tool

While looking at Open Router's comparison tool as inspiration, our engineer noticed two patterns worth flagging as you build yours:

**Canonical URLs.** When a comparison tool lets you swap the order of models (e.g., Qwen/Gemini vs. Gemini/Qwen), it can generate different URLs with identical content. Without canonical tags, search engines treat these as duplicate pages. Worth building in from the start: every model combination should resolve to a single canonical URL regardless of input order (e.g., alphabetical sorting).

**Server-side rendering.** Comparison pages that are entirely client-side rendered show blank pages to crawlers that don't execute JavaScript. For SEO and LLM crawlability, these pages should be server-side rendered or statically generated. JS-dependent pages take longer to crawl and some engines won't index them at all.

Easier to get these right from the start than to retrofit later.

## 5. UI Exploration

We're going to mock up some improved UI concepts for the model pages, inspired by what's working for Open Router (tabbed sections for performance, providers, pricing, apps). We'll have something to show you on Thursday's call for feedback. Not asking for any work on your end yet. Just want to get your reaction before we go deeper.

One note: we know you want to keep the playground on the model pages. We'll work around it and make sure it stays accessible.

---

Let us know on these when you get a chance. Happy to jump on a quick call if any of this is easier to discuss live.

Thanks,
George
