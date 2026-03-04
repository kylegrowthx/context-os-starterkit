# VERCEL × GROWTHX: Engagement Prep Brief

**Kickoff Preparation | February 24, 2026**
*Sources: Notion (Vercel Context from Sales, Kickoff Discovery Questions, Shared Workspace), Fathom (Feb 4 Scope Call), Slack (b-sales, george-brain-dump)*

---

## Key Context at a Glance

- **Vercel:** Cloud platform for frontend/full-stack dev. Creators of Next.js, v0, AI SDK, AI Gateway. $9.3B valuation, $200M+ ARR.
- **Deal:** 12-month contract: Months 1–6 at $20K/mo, Months 7–12 at $30K/mo. Full editorial + programmatic scope throughout. No Phase 1 upfront fee. Total contract value: $300K.
- **Primary contact:** Cody Henshaw (Head of Growth Marketing + Digital Strategy, ex-Redis). Reports to CMO Keith Messick. Has CMO + COO approval locked in.
- **This is an AirOps takeout.** Cody is unhappy with current agency. Marcel sees Vercel as a "lighthouse client" for GrowthX.
- **Hard no:** Third-party scripts on the site. No GA4, no pixels. Analytics via Amplitude + RudderStack. GSC just recently obtained.
- **Publishing path:** vercel.com/i (Cody's autonomous section, no G approval needed). Blog + product pages are "sacred" and require CEO sign-off.

---

## 1. Company Overview

Vercel is the leading cloud platform for frontend and full-stack web development. Founded by Guillermo Rauch ("G"), the product ecosystem includes Next.js (dominant React framework), v0 (AI-powered UI generation), AI SDK (open-source toolkit for AI applications), AI Gateway, and the Vercel platform for deployment/hosting/scaling.

**Valuation:** $9.3B (2024 Series E). **ARR:** $200M+. **Customers:** Enterprise-heavy: Shopify, Adobe, Nike, Washington Post.

**Open source footprint:** ~100+ project sites including ShadCN, Nuxt, Svelte, AI SDK, and many more. Currently under Product, not Marketing. Cody is eyeing these as his next "lane grab"; he did the same at Redis, consolidating 7 sites into 1 and driving major traffic with no SEO drop-off.

**Competitive landscape:** Netlify (closest, perceived as weaker), AWS Amplify, Cloudflare Pages, Railway. The real fight is for visibility in AI discovery surfaces: when a developer asks Cursor or ChatGPT what to use, Vercel needs to be the answer.

---

## 2. Key Stakeholders


| Name                | Title                                  | Key Notes                                                                                                                                                                                         |
| ------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cody Henshaw**    | Head of Growth Mktg + Digital Strategy | Primary contact. Ex-Redis (with Keith). Now owns all growth functions. Created /i section. Autonomous; can sign and push internally. Unhappy with AirOps. Direct, collaborative, action-oriented. |
| **Keith Messick**   | CMO                                    | Cody's boss. Ex-Redis. Wants speed and velocity. Approved the deal along with COO. Less directly involved day-to-day.                                                                             |
| **Dan Fine**        | Sr. Technical PMM                      | Marcel: "An extension of G's brain." Most respected by G internally. Recently moved from Product to PMM. Can block things or help decide focus areas. **Talk to him early. Critical.**            |
| **Eric Dodds**      | Sr. Content Engineer                   | Technical resource for programmatic work. Key collaborator for stacks pages and engineering implementation.                                                                                       |
| **Head of PR**      | TBD (name not shared)                  | Running full brand messaging + positioning strategy with a separate agency. Tied into G's 5-year vision. Valuable for directional alignment.                                                      |
| **Guillermo Rauch** | CEO ("G")                              | Visionary leader. 5-year content vision. Blog + product pages require his approval. Deep care for AI positioning and developer experience.                                                        |


**Relationship intelligence from the scope call:**

- Cody and Keith both came from Redis, strong working relationship
- Cody proactively offered to send docs, make intros, and remove blockers; he's invested in this succeeding
- The Redis procurement experience was brutal (Andy beat Marcel up on terms). Vercel uses Zip for vendor onboarding. Cody says it won't be as bad
- Cody's energy on the call: "I'm stoked." Told Marcel "let's go fast and do whatever we can do"

---

## 3. Deal Structure

The original SoW had a $40K Phase 1 upfront fee. Marcel proposed removing it and restructuring as a ramped monthly to simplify procurement and align with Cody's budget constraints (overlapping AirOps spend in first 6 months).


|                 |                                                                                      |
| --------------- | ------------------------------------------------------------------------------------ |
| **Contract**    | 12 months, single phase                                                              |
| **Months 1–6**  | $20K/mo (discounted for AirOps overlap)                                              |
| **Months 7–12** | $30K/mo (full rate)                                                                  |
| **Total**       | $300K ($120K + $180K)                                                                |
| **Scope**       | Editorial (/i section) + Programmatic (stacks, cross-linking) throughout             |
| **Procurement** | Cody signs SoW as letter of intent → submits to Zip → legal redlines MSA → PO opened |


Marcel's framing to Cody: "We want the logo. We want to really prove it out." He compared it to Lovable: started at $25K, proved out guides + templates (guides = more traffic, templates = more conversions), then expanded scope. Cody responded: "Whatever you think is the highest leverage that we can prove this thing."

---

## 4. Strategic Priorities (Ranked)

### #1: AEO / GEO (AI Engine Optimization)

Vercel's top priority. When developers ask AI coding agents for recommendations, Vercel needs to be the answer. They've built an internal LLM visibility tool that runs coding agents (Claude Code, Codex, etc.) in their sandbox product (went GA on Feb 4). It produces visibility scores that platforms like Profound don't track. Cody wants to partner with GrowthX on understanding these signals, and they plan to open-source the tool. Content needs to be structured and authoritative enough for AI training data and retrieval systems to pick it up.

### #2: Content Velocity on /i Section

vercel.com/i is a copy of the blog template with zero content. Same content model, Cody's autonomous space, no G approval needed. They're also building self-serve solutions pages and landing pages. Two tactical requirements Marcel flagged: (1) dedicated sitemap submitted as part of global sitemaps, and (2) footer link for indexation. Cody confirmed both are doable. The velocity gap is the primary reason they hired GrowthX. Dan Fine is the quality gatekeeper.

### #3: Programmatic / Stacks Pages

Programmatic SEO pages showing how tools run on Vercel (e.g., "Why Shopify runs better on Vercel"). A batch of new stacks pages was about to launch as of Feb 4. Eric Dodds is the key contact. Template-driven. Cody called these "really easy things to knock off." Cross-linking from footers on 100+ open-source project sites is what Marcel calls "the biggest lever" for competitive keyword situations. Cody confirmed cross-linking is not hard and he can make the argument internally.

### #4: AI SDK + AI Gateway Content Moat

Marcel showed Cody search volume data from a popular AI tools site to illustrate the opportunity. His framework: AI Gateway captures "model traffic" (searches for specific AI models), guides target long-tail buyer intent questions. The AI Gateway team proactively reached out to Cody about optimizing their content. Marcel flagged a more complex cluster play as a future lever: "could be life-changing good" but not where to start.

---

## 5. Analytics & Technical Stack

- **No GA4 (and never will be).** Third-party scripts are the one absolute hard no. Cody: "That's the only real pushback I've gotten." No pixels of any kind.
- **Amplitude:** Primary analytics. Data flows through RudderStack CDP. GrowthX uses RudderStack for check.ai so the team is familiar.
- **Snowflake:** Data warehouse, currently being rebuilt. Marcel flagged checking if there's an Amplitude API layer vs. pulling from the warehouse directly.
- **GSC:** Just recently obtained. Limited historical data.
- **CMS:** Custom-built. Need a walkthrough during onboarding.
- **LLM Visibility Tool:** Custom-built, runs coding agents in sandbox. Going to be open-sourced.

---

## 6. What Cody Expects

From the scope call and discovery questions, this is what success looks like:

- **Speed:** Demonstrate faster, higher-quality output than AirOps from Day 1
- **AEO visibility:** Measurable improvement in how often AI agents recommend Vercel's tools
- **Content velocity:** Consistent publishing cadence on /i
- **Data-driven iteration:** Use analytics and visibility data to continuously refine strategy
- **Highest-leverage plays first:** "Whatever you think is the highest leverage that we can prove this thing"

Cody is bought in. He proactively offered to send docs, make intros, and remove blockers. The pressure is on GrowthX to match his energy with execution speed.

---

## 7. George's Hand-Off Notes

George met with Marcel on Feb 18. Key takeaways: kickoff originally Feb 23 (moved to today), need to talk to the engineer from Clerk/Base10 for technical workspace setup, Vercel has everything public so all docs are available for ingestion, and the shared workspace in Notion is set up but all 15 doc pages are "Not started."

---

## 8. Flags & Open Items

- **Vercel's Notion onboarding page** (meeting deck, brand guidelines, fonts) is in their workspace, inaccessible via our integration. Access directly or ask Cody to reshare.
- **Hand-off meeting recording** (George, Marcel, Tyler) not found in Fireflies. May be under a different name or platform.
- **Jan 27 intro call recording** returned "not found" in Fireflies. May have been deleted.
- **Head of PR:** get her name and an intro for brand narrative alignment.
- **Snowflake rebuild:** confirm timeline and what data access is available now vs. later.

---

## 9. Action Items for Today

### Confirm & Align

- Confirm AEO/GEO is still #1 and understand what the LLM visibility tool is currently showing
- Get a CMS walkthrough for /i section publishing
- Confirm sitemap and footer link for /i are in place (or get timeline)
- Ask about stacks pages launch status: are they live? How many?
- Clarify what's in the Vercel Notion onboarding page they shared

### Build Relationships

- Meet Dan Fine and establish the content review/approval workflow (most critical)
- Meet Eric Dodds for programmatic workstream
- Get intro to Head of PR

### Data & Access

- Request Amplitude and GSC view access (Cody already agreed on scope call)
- Ask about Snowflake rebuild timeline
- Request access to LLM visibility tool and Slack content agent

### Quick Wins to Signal Velocity

- Start populating shared workspace docs immediately after kickoff
- Begin competitive content audit for quick gaps
- Draft first editorial angles for /i based on AI SDK + AI Gateway
- Map the 100+ open-source project sites for cross-linking sizing
- Deliver "What We Heard From Kick-off" document within 24–48 hours

