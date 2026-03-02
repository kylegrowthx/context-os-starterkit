# CheckThat Weekly Check In

<metadata>
date: 2026-01-05
time: 18:00 UTC
duration: 39 minutes
organizer: Marcel Santilli (GrowthX)
participants:
  - name: Stevie Kim
    company: CheckThat
    role: Product Lead
  - name: Daniel Lopes
    company: CheckThat
    role: Engineering Lead
  - name: Leo Steffen
    company: CheckThat
    role: Engineer
  - name: Pedro
    company: CheckThat
    role: Engineer
  - name: Jose Farias
    company: CheckThat
    role: Engineer
  - name: Jason Gong
    company: CheckThat
    role: Product Manager
fireflies_id: 01KDNY91VPQ4JYWYXF55DCZ4Z8
transcript_url: https://app.fireflies.ai/view/01KDNY91VPQ4JYWYXF55DCZ4Z8
enriched_on: 2026-02-28 21:15:32 UTC
</metadata>

---

## Summary

CheckThat's core product team aligned on three critical initiatives for Q1 launch readiness: (1) hardening the editorial workflow with internal linking across 6,000+ brand profiles to improve SEO effectiveness, (2) cutting operational costs by 50% through probe frequency reduction (free tier: every other day) while evaluating data vendor partnerships, and (3) migrating human editors from the Atlas workspace to a new AI-assisted page generation system that reduces manual control surface while maintaining fact-checking capabilities through embedded research summaries.

---

## Context

CheckThat is preparing for design partner rollout and public launch in early 2026. The product generates comparison pages, alternative product pages, and company profiles using AI-driven workflows built on top of proprietary brand research. The team discovered that the Atlas page generation workspace—which had human editors hand-crafting content—created bottlenecks and control surface problems that propagated downstream to end users (inconsistent writing guidelines, fact-checking artifacts causing hallucinations, prompt designs that got stuck in verification loops).

In this meeting, Daniel Lopes demonstrated a replacement system with fixed templates, reduced manual controls, and integrated research summaries for fact-checking. The team also addressed two operational constraints: (1) rising infrastructure costs from daily probe runs across free-tier customers, and (2) incomplete internal linking in brand pages, which hampered SEO signal propagation and content discovery.

---

## Relevance

**Product & Platform**
- New page generation system moves control from editors to product team via templates and feedback loops
- Embedded research summaries solve fact-checking friction without exposing technical prompts
- Internal linking workflow (new feature) ensures content clusters reinforce SEO signals

**Operations & Cost**
- 50% cost reduction achievable through probe frequency changes (weekly → every other day for free tier)
- Data vendor partnerships (Similarweb NDA, Ahrefs follow-up) being explored as alternatives to in-house scraping
- Weekly cost tracking spreadsheet (managed by Lala, Alice, Daniel) to monitor vendor and API spend

**Launch Readiness**
- Design partner workspaces require polished internal linking and factual accuracy before sharing
- 6,000 profiles already indexed and ranked; focus is forward-looking (new content only) to avoid retroactive rework
- Editor migration off Atlas unblocks CheckThat workspace sunset and centralizes page workflows

---

## Action Items

**Stevie Kim (CheckThat)**
- Create ticket for probing schedule adjustment: free tier from daily to every-other-day
- Create ticket for library prompt frequency alignment: set to every-other-day schedule
- Follow up with Ahrefs on probing data partnership (post-NDA for Similarweb already obtained)

**Daniel Lopes (CheckThat)**
- Add error handling to workflow execution: catch failures and send webhook responses back to app to prevent hangs during brand research and page generation
- Create ticket for internal linking workflow: add step to researcher to link new brand profile pages to correct internal sources (similar to existing pages implementation)
- Support Jason with editor migration: provide training and gather structured feedback from Harry and Kabishka (editors) in form of tickets for continuous iteration
- Set up Sentry NCP error monitoring (recommended by Jose as fast troubleshooting tool)
- Review and finalize note-taking tool selection; communicate to team that meeting hosts own recording responsibility

**Jose Farias (CheckThat)**
- Add offline comments to prompt scheduling ticket: clarify custom vs. library prompt frequency and data structure implementation
- Review Pedro's iScope work for cited domains/URLs once PR dependencies are merged

**Pedro (CheckThat)**
- Implement iScope for cited domains and URLs scoped per prompt (blocked on dependency PRs merging)

**Jason Gong (CheckThat)**
- Migrate editors (Harry, Kabishka) from Atlas workspace to new page generation system in CheckThat
- Collect editor feedback on 0-to-1 page creation speed, fact-checking experience, and editing UX; create improvement tickets from feedback

**Lala & Daniel (CheckThat)**
- Set up and maintain weekly vendor cost tracking spreadsheet
- Coordinate with Alice to pull recurring weekly cost reports across Atlas, CheckThat, and company services
- Segment costs by service (Anthropic, OpenAI, Jina, Google) to track which workflows drive spend

---

## Transcript

**Stevie Kim:** This meeting is being recorded.

**Leo Steffen:** Happy Monday, y'all. Happy New Year—I'm still here with all the kids at home, it's crazy days.

**Pedro:** Happy New Year! Finally.

**Daniel Lopes:** All here, ready to go.

**Stevie Kim:** I threw the Notion doc in the chat. We've been evaluating a few different note-taking tools—Fireflies, Phantom. The host of the meeting will handle recordings going forward. Daniel's the host now.

**Daniel Lopes:** Got it. Let me take a look at the doc. And I messaged Marcel; we can start when you're ready.

**Stevie Kim:** Perfect. All right, let me recap what we accomplished. CMS and editorial workflow improvements last week put us in better shape for launch readiness. Daniel did great work there. Now editors can create the content we need to improve SEO standing. On cost mitigation, we're looking at internal optimizations and exploring data vendor partnerships to reduce probing spend.

**Stevie Kim:** I met with Similarweb on Friday—they require an NDA to discuss probing data partnerships. High-level overview only until we sign and meet with their team. Following up with Ahrefs tomorrow. I'll send details your way. We have a few blockers for design partner readiness. On probe frequency: the free tier currently probes daily (over 7 days weekly), which drives costs. We need to finalize pricing tiers in the docs before locking down the workflow change.

**Daniel Lopes:** From a short-term optimization: even just changing free tier probing to every-other-day is a 20-minute code change that cuts costs in half. We can do that immediately while we sort out the fuller pricing-tier architecture—that's complex downstream (Stripe integration, tier-linked custom prompts, account relationships). Let me sketch out a design architecture for that separately.

**Leo Steffen:** Stripe has auto-discount features for free tiers we could leverage.

**Daniel Lopes:** Right. The relationship layer is: which plan does the prompt belong to, who owns the account, and tier changes need to cascade to the prompt schedule. We haven't coded plans yet, so it's getting complicated. But the immediate every-other-day change solves the immediate cost problem.

**Jose Farias:** Quick clarification: only custom prompts need custom schedules, correct?

**Daniel Lopes:** Yes.

**Jose Farias:** So that's just a field on the prompts table. I can add comments offline with the schema suggestions.

**Pedro:** From last sync, Marcel mentioned library prompts should have frequency too. That was my main question.

**Daniel Lopes:** Two layers of frequency: custom prompts tie to pricing tiers; library prompts run at a common cadence. For library, every-other-day for now. The data display shouldn't suffer—Scrunch runs every three days and nobody notices daily granularity. For data collection studies, we'll keep daily frequency and eventually add search-tool limits as an enterprise pricing tier.

**Stevie Kim:** I'll create two tickets: one for library prompts (every-other-day), one for custom prompts (pricing-tier dependent). That separates the concerns.

**Daniel Lopes:** On internal linking: the issue was that brand profiles were linking to external sources (e.g., cloud AI) instead of internal CheckThat pages. I built an internal linking workflow this week, but it only runs on pages in the page pipeline, not in the brand researcher workflow. We need to add a step to the researcher: when we research a new brand, apply the same internal linking logic. It will identify related brands in our profile set and link internally. External links are fine when they're the correct source (like G2, external tools), but we want to prioritize internal links for content clusters.

**Stevie Kim:** For design partner workspaces, internal linking needs to be clean. But for existing profiles, do we backfill?

**Daniel Lopes:** Backfilling all 6,000 profiles would require a script, and I'm not sure it's worth the effort yet—profiles are already linking well between each other on pages. The bigger win is the page-level linking, which I fixed this weekend. That's the core blocker. For SEO, the architecture is: pages have all the links, profiles link to pages, and each profile section (alternatives, pricing, sentiment) links to relevant pages, which then link back to cited profiles. The signal graph is complete.

**Stevie Kim:** So forward-fixing (new profiles only) is the move?

**Daniel Lopes:** Yes. And I can write the ticket for the researcher step. If design partners need polished profiles, we can add a button to re-link specific profiles manually.

**Pedro:** On the iScope work for cited domains/URLs: I'll move forward with the approach I proposed. Since these are UI changes, if we need to adjust later, it's easy. I still need to implement iScope for cited domains and URLs scoped per prompt—that's blocked on Jose's PR dependencies merging. Once those are in, I can calculate the cited URLs and domains for each prompt, then we're ready to surface it.

**Jose Farias:** Got it. I'll review once the PRs are ready.

**Stevie Kim:** Perfect. Any other updates before we wrap?

**Daniel Lopes:** I added bug fixes this weekend: (1) admin page creation now handles brand deletion correctly, (2) fixed a critical issue where workflow failures don't send webhooks back to the app—if brand research or page generation fails, the UI hangs forever. That's why some researches get stuck. I'll create a ticket to add failure catch/response. We'd like to resume bulk brand research (going through candidates and triggering research), which we paused to focus on quality. We have 6,000 profiles indexed with good impressions; adding more won't hurt. (3) Brand research sometimes found the wrong entity (e.g., Delta Airlines instead of another Delta). I fixed it by passing top three probes into the Google query context—that helps find the correct domain. Some brands like Peak got stuck because domains weren't found; this should resolve that. Read the README and Loom for the page generation workflow walkthrough.

**Jason Gong:** So editors are currently hand-crafting content in Atlas (Harry, Kabishka). Are they moving to CheckThat's new system?

**Daniel Lopes:** Yes. We should sunset the CheckThat workspace in Atlas and have them use the new page generation system here. It's structured differently than Atlas—less manual control, more guardrails. Here's the workflow: (1) Go to Admin > Pages, select a page type (4 fixed types), enter a brand name. (2) Click "Generative AI" to generate a brief (30 seconds). It uses all the profile data and runs a Google-enabled Gemini search to identify coverage areas and personas—returns search intent, persona, key topics. (3) The system generates an outline (H2 headers with bracketed descriptions, fully editable). Change the outline, and research questions auto-update to match, ensuring accurate research data for generation. (4) Generate the page (similar to Atlas), which auto-generates internal links, meta descriptions, and cover images. (5) For fact-checking, embedded research summaries show where data came from. If they query a price ($200), they can click the research summary to see sources and whether the data is current or legacy.

**Jason Gong:** Should they switch now?

**Daniel Lopes:** Yes, get them migrated immediately. It's all synced—pages publish automatically (unlike contentos). Sunset the Atlas workspace. They'll see where controls are locked (for good reasons—free-form editing of artifacts and writing guidelines caused Contentos to get stuck in loops). The philosophy: fixed templates with feedback loops, not open-ended editing. Content types can have type-specific artifacts if needed. Most importantly: (1) pages auto-generate with internal links already included, (2) bulk regeneration is easy, and (3) feedback comes via tickets, not via manual tweaking that breaks the system.

**Jason Gong:** They said fact-checking is the bottleneck—is the research summary helpful?

**Daniel Lopes:** Yes. The edit form shows the research summary collapsed at the bottom. They can expand it, see the sources, and trace where any claim came from. It's the same page—no context switching. For legacy or hard-to-find data, the research summary is there. They can't find it on Google/Perplexity, but it's in our research, so we surface it.

**Stevie Kim:** Any other updates or blockers?

**Leo Steffen:** No blockers on my end.

**Daniel Lopes:** I merged cost optimizations from last week (HTML tokenization on scraping). That should already reduce costs significantly—I'll verify. No other changes from the audit right now. Lala and I will set up weekly vendor cost tracking in a spreadsheet; Alice will help pull recurring reports segmented by service (Atlas, CheckThat, company). Watch for: adding Google AI Overview increases cost slightly, but the real spend is Anthropic, OpenAI, and Jina. Google has rate-limiting constraints—6,000 calls might hit limits on our current plan, but we'll monitor.

**Stevie Kim:** Got it.

**Jose Farias:** Quick tool rec: if you're not using Sentry NCP, start. It's a game-changer—I debugged a slow query in 15 minutes (copy-paste, fix, commit, ship). Highly recommend.

**Daniel Lopes:** I'll set it up.

**Stevie Kim:** Thanks everyone. Great week ahead.

**All:** Thanks, see you later.
