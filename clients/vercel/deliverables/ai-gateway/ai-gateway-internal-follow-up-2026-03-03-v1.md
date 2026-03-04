# Vercel AI Gateway: Internal Follow-up & Next Steps

<metadata>
purpose: Internal action plan from March 3 team sync on Vercel AI Gateway SEO workstream
audience: GrowthX internal team (George, Hassan, Tamy, Kirkland)
summary: Phased execution plan for AI Gateway SEO. Phase 1 is MVP content improvements (titles, headings, FAQs) shipped as JSON without waiting on Vercel data. Phase 2 is UI mock-ups and data integration. Deadline: have deliverables ready before Thursday client call.
domain: client
confidence: current
context_tier: 2
last_updated: 2026-03-03
</metadata>

---

## Context

On March 3, the GrowthX team (George, Kirkland, Tamy, Hassan) synced on next steps for the Vercel AI Gateway SEO workstream. The prior meeting with Vercel's AI Gateway team (Feb 27) confirmed they're open to any SEO improvements we recommend and will publish changes we send. This follow-up defines who does what, in what order, and what we need from Vercel before Thursday's call.

**Core decision:** Don't wait on Vercel's backend data. Ship MVP SEO fundamentals now (copy, headings, FAQs), then layer in dynamic data and UI components as phase 2.

---

**Phase 1: MVP SEO Fundamentals (This Week)**

Get content improvements ready to show or send to Vercel by Thursday's call.

- [ ] Finalize keyword research. Fill in competitor data from Semrush, categorize by page template, identify keywords competitors rank for that Vercel does not. **(Hassan)**
- [ ] Produce 1-2 example optimized pages. Pick a model page and show exactly what to change: title, headings, description, FAQ section with long-tail keywords. Include the "why" for each change. This becomes the template Tamy uses to scale. **(Hassan)**
- [ ] Build the content workflow. Once Hassan delivers examples, create a workflow that generates JSON documents with content enhancements for each page: new title, headings, description, FAQ section. **(Tamy)**
- [ ] Scale across all ~170 pages. Apply the workflow to produce a JSON document for each AI Gateway page. Use placeholders for data-dependent fields. **(Tamy)**
- [ ] Align on output format. JSON is the default. If Vercel needs a different format, add a conversion step at the end. **(Tamy + Kirkland)**
- [ ] Send questions to Vercel before Thursday. Content format for 170 pages, data model access, frontend access status. **(George)**
- [ ] Show the "great page" example on Thursday's call. Walk through 1-2 examples to demonstrate progress and get client buy-in. **(George)**

**Scope:** Text and media only (titles, headings, descriptions, FAQs, new content sections). Tables, charts, and dynamic data are phase 2. We can add new sections freely as long as they're content-only.

---

**Phase 2: UI Mock-ups & Data Integration (Parallel + Next Sprint)**

- [ ] Vibe code a model page mock-up. Clone the Vercel AI Gateway model page and add tab components inspired by Open Router: performance, providers, pricing, apps. Placeholder data. George Main polishes visuals after. **(Kirkland)**
- [ ] Mock up comparison page improvements. Comparisons have the highest URL multiplication potential. Highest-impact template to redesign. **(Kirkland)**
- [ ] Support Tamy on JSON workflow. Help accelerate using Claude/Opus if needed. **(Kirkland)**

---

**Technical SEO Issues to Flag with Vercel**

These are high-value findings from Kirkland's live analysis during the call:

1. **Comparison pages: no canonical URLs.** Swapping model order (Qwen/Gemini vs Gemini/Qwen) creates duplicate pages with different URLs. Every combination should resolve to one canonical URL regardless of order.
2. **Comparison pages: client-side rendered only.** Disabling JavaScript shows a blank page. Need SSR or SSG so search engines and LLM crawlers can index them.
3. **LLM crawlability.** Consider markdown versions of pages for LLM training data. JS-dependent pages take longer to crawl and some engines won't go as deep.

---

**Timeline**

- Keyword research finalized: by Wed **(Hassan)**
- 1-2 example optimized pages: by Wed **(Hassan)**
- Questions sent to Vercel: Tue/Wed before Thursday call **(George)**
- Content workflow built: after Hassan's examples **(Tamy)**
- UI mock-up (model page tabs): starting now, alongside Brex work **(Kirkland)**
- Thursday client call **(George + team)**

---

**Key Decisions**

1. **Phase before you wait.** Ship content improvements now, don't block on Vercel's data access.
2. **Example-first approach.** Hassan produces 1-2 pages as the template. Tamy scales from there.
3. **JSON is the default output format.** Convert later if Vercel needs something else.
4. **UI mock-ups are "new Figma."** Vibe code the improvements so Vercel can see them live.
5. **Frontend access is a "should have," not a blocker.** Phase 1 works without it. Phase 2 will need it.
