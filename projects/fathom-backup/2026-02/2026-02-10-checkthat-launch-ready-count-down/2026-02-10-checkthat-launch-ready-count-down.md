# CheckThat: Launch Ready Count Down

<metadata>
date: 2026-02-10
time: 15:58 UTC
duration: 32 minutes
organizer: Stevie Kim (stevie@growthx.ai)
participants:
  - Marcel Santilli (marcel@growthxlabs.com, Product Lead, CheckThat)
  - Daniel Lopes (daniel@growthxlabs.com, Product Director, CheckThat)
  - Jason Gong (jason@growthx.ai, GrowthX)
  - Pedro Steimbruch (pedro@growthx.ai, Engineer, CheckThat)
  - Jose Farias (jose@growthx.ai, Engineer, CheckThat)
  - Estevão Mascarenhas (estevao@growthx.ai, Engineer, CheckThat)
  - Leonardo Carpenedo Steffen (leonardo@growthx.ai, GrowthX)
  - Stevie Kim (stevie@growthx.ai, Product Manager, CheckThat)
fathom_recording_id: 121198985
fathom_url: https://fathom.video/calls/561192080
share_url: https://fathom.video/share/KHJJjeNgxSpGVi639ZQ6_BZyg2dCnzgz
source: fathom
enriched_on: 2026-02-27T12:00:00Z
</metadata>

---

## Summary

The team discussed implementing a structured "shaping" process to reduce rework from ad-hoc changes, replacing daily stand-ups with async updates and a weekly sync. Key decision: subcategories will become a non-critical filtering tag rather than a core architectural dependency, enabling faster iteration. Immediate priorities include shipping filters on the overview screen and improving subcategory accuracy through user-guided workflows.

---

## Context

This meeting occurred immediately after launch, marking a critical inflection point for CheckThat's post-launch operation. Daniel (Product Director) made significant changes to the onboarding flow and subcategorization strategy overnight, prompting a discussion about moving from unstructured, high-velocity work to a more disciplined approach. The team acknowledged that while sprinting to launch worked, they now need structure to balance speed with rework prevention and decision clarity.

Stevie is newly in the product role and taking on meta-responsibilities: structuring Daniel and Marcel's high-level strategy discussions, translating them for engineering, and using Linear to surface priorities. The challenge is determining the right balance of upfront planning versus rapid iteration—particularly around how "lightweight" their shaping process should be. Ryan Singer's Shape Up methodology and newly-released Claude skills for shaping are being considered as tools to accelerate this transition.

---

## Relevance

- **Process & Methodology**: Critical decision on adopting Shape Up shaping process; directly impacts how CheckThat team operates post-launch
- **Product Strategy**: Fundamental shift in how subcategories function architecturally; affects UX design and data modeling
- **Prioritization**: Clear enumeration of P0/P1 work from Daniel; determines sprint focus for engineering
- **Operational**: New meeting cadence and async-first communication affecting team coordination and visibility
- **Product Development**: Immediate deliverables (filters on overview, subcategory UX improvements) that impact user experience
- **AI/Tooling**: Exploration of Claude-based Shape Up skills to accelerate decision documentation

---

## Overview

- **Process Shift:** Adopting a structured "shaping" process to reduce rework from ad-hoc changes. Daily stand-ups will be replaced with async updates and a weekly sync.
- **Subcategory Strategy:** Subcategories will become a non-critical "tag" for filtering, decoupling core UX from their accuracy. This enables a faster, less error-prone user experience.
- **Priority Alignment:** All work must align with Daniel's new priority list (shared in Slack), which Stevie will tag in Linear as P0/P1 to provide clear visibility.

---

## Key Topics

### Process & Cadence

  - **Problem:** Unstructured work, like Daniel's recent ad-hoc onboarding changes, causes rework and makes building a consistent mental model difficult.
  - **Solution:** Adopt a "shaping" process for more upfront planning, balancing speed with reduced rework.
      - **Goal:** Define the problem, opportunity, and solution before implementation.
      - **Tool:** Use Ryan Singer's Claude skills for shaping to accelerate the process.
  - **Meeting Cadence:**
      - **Daily Stand-ups:** Replaced with async updates in Slack.
      - **Weekly Sync:** A longer, weekly meeting will replace daily stand-ups for technical alignment.
      - **Friday Strategy Meeting:** Daniel, Marcel, and Stevie will meet; others can join but should expect a high-level, unstructured discussion.

### Subcategory Strategy

  - **Problem:** The core UX is too dependent on perfect subcategory accuracy, which is difficult to achieve from limited data (e.g., a vague homepage).
  - **Solution:** Decouple the core UX from subcategories by treating them as a non-critical "tag" for filtering, not a core architectural component.
  - **Implementation:**
      - **Estevão:** Shipping a basic research workflow to improve subcategory accuracy for \~30 brands.
          - **New Onboarding:** Users will see all suggested subcategories and can remove irrelevant ones.
          - **Tracking:** Needs a Post-Hog plan to track changes made by this new flow.
      - **Pedro:** Investigating prompt suggestions as a way to further reduce reliance on subcategories.

### Current Priorities & Updates

  - **Jose:** Implementing filters on the overview screen (a high priority for Marcel).
      - **Technical:** Requires re-enabling snapshotting of competitor/prompt performance, which was previously removed to save storage.
      - **Trade-off:** This is offset by no longer needing to snapshot subcategories, as the categories chart was removed.
  - **Pedro:**
      - Shipped: Pagination for sources page, timezone handling for charts, and on-demand sitemap regeneration to S3.
      - Next: Investigate prompt suggestions.

---

## Action Items

**Stevie Kim (CheckThat, Product Manager)**
- Review Daniel's onboarding/subcategorization shaping doc; post clarifying questions in comments
- Tag Linear tickets P0/P1 per Daniel's prioritization; update labels to P0/P1

**Jose Farias (CheckThat, Engineer)**
- Share Ryan Singer's Shape Up Claude skills in Slack channel
- Re-enable snapshotting of competitor and prompt performance for onboarding overview filters (required for overview screen filtering feature)

**Estevão Mascarenhas (CheckThat, Engineer)**
- Investigate PostHog release tracking for onboarding flow changes (needed to measure impact of new subcategory workflow)

---

## Transcript

[Opening remarks on flexible work schedules omitted]

**Stevie Kim:** Before we get started, I wanted to ask about the Linear label changes. Daniel removed the launch milestones but the labels still exist. I'm going to change launch P0/P1 to just regular P0/P1 so they're reusable. We're keeping the same project for now rather than retiring it, since we're not using multiple projects in a way that matters. I'm reorganizing the board to give better visibility into priorities. Some of the growth items are going to the backlog because there are so many.

Daniel also removed the second Monday meeting. So it'll be Daniel, Marcel, and me on Friday—kind of a messy strategy meeting. Others can join but should expect high-level discussion, not technical detail.

I wanted to get your thoughts on daily stand-ups. Should we keep them, do them less often, or replace them with something else?

**Jose Farias:** I don't have strong feelings about the stand-ups. The technical discussions that happen there would probably happen anyway in async Slack conversations. We're diligent enough to know when we need to align, and I actually think async is better for transparency and for AI—when we write things down, we can point agents to it. I'd be fine with dropping daily stand-ups or doing just one weekly.

That said, there's something else I want to flag. Daniel made some pretty major changes to the onboarding flow last night, changing the overall strategy to not rely so much on categorization. They're good changes, but I think they're a consequence of not spending enough time shaping beforehand. Rather than worrying about daily stand-up cadence, I think we'd benefit from more structured, less chaotic strategizing. It would prevent the kind of late-night rework we're seeing.

**Stevie Kim:** I want to clarify—did he create a shaping doc or push changes directly to production?

**Jose Farias:** It started as a doc and then he pushed the changes. They're good, but the point is we're balancing moving fast with having to redo things. It creates long nights.

**Stevie Kim:** In my past product work, I'd do a lot more upfront. Define the problem, lay out opportunities, get alignment on what's important, do technical discussions with engineering, write out a detailed solution. I'm used to acceptance criteria and that level of rigor. We don't need to be that heavy, but we can do a lightweight version.

The challenge for me is building mental models when nothing's written down. I think through writing, so it's hard when I can't document decisions. I'm all for more structure.

Here's how I see my role: I'm going to be in the Friday meetings with Daniel and Marcel, sitting in the mess, and trying to create some structure there. Then we have a weekly sync—maybe longer than 30 minutes—where I translate what was decided and we answer engineering questions. I'm basically a translator between those high-level, messy strategy conversations and the technical work.

The hard part for me is calibrating how much shaping is "just enough." I tend to be a deeper thinker and go too deep on research. But what I'll need help with from you guys is knowing when to say "okay, this is good enough. We understand the why and Daniel and Marcel's vision. Let's move."

**Jose Farias:** We can err on the side of less structure since we've been operating with zero structure and things are okay. We're an experienced team that can handle ambiguity. The trade-off is: more shaping means less rework, but we move slower. Marcel won't have to see something shipped that doesn't match his mental model. That's worth some slowdown. But I know it can get grating if rework happens for too long.

**Stevie Kim:** This has been on my mind a lot too, so I'm glad you brought it up.

**Jose Farias:** Pedro, what do you think?

**Estevão Mascarenhas:** On stand-ups, I'm fine either way. For technical discussions, I prefer async Slack conversations so there's history for AI tools to reference and I have time to organize my thoughts first instead of just saying things unorganized.

But on subcategorization—I think this is critical to get right. For me, subcategories are part of the intelligence contextual layer—not just brand data, but how we group brands. When Daniel says we shouldn't be too tight to subcategories, I understand that the UX shouldn't depend on perfect accuracy. But subcategories aren't going away; we still need to fix them.

The problem is tricky: we only scrape the homepage, and those homepages are vague. We're inferring subcategories from limited data. If we scrape more pages, the workflow becomes slow for users. So the question isn't "should we abandon subcategories?" It's "should we fix them? How?"

Lots of things we built depend on subcategories being right. I'm a bit confused about the direction here. I don't think we fully worked this out yet.

**Stevie Kim:** I don't think anyone ever said subcategories would go away. It was more that they'd be less critical to the architecture—more like a filter or tag. Like how you tag prompts and filter by them; that's not critical to the system. Subcategories should be the same way: a way people group prompts together, not something the whole product depends on.

The point is making things less dependent on getting subcategories perfect, because we're never going to. That doesn't mean we're getting rid of them, just reducing the dependency on them.

There's still ambiguity here. I haven't had time to look at Daniel's shaping doc, but I will. I need to make sure I understand the vision. The challenge for me is that I get stuck in the mindset of "this is how it was designed, so we just need to fix what exists." But I don't have historical context, and anyone new jumping on won't either. So we need to question whether the design itself is right, not just optimize what we have.

If you see hand-wavy explanations in the doc, put clarifying questions in the comments and let's push harder.

**Pedro Steimbruch:** I agree with Jose. We were sprinting to launch with zero structure, but now I think we need to slow down to go faster. We need to think about the value we're really delivering, shape it out, and work in cycles. If we keep sprinting, we'll deliver a lot but we'll be off-target. After launch, we need structure and cycles aligned to goals.

**Jose Farias:** Quick note: Ryan Singer, the Shape Up author, recently released Claude skills for shaping. I've used them and they're good. They're not perfect—you can derail them—but they help speed up the shaping process. I'll share them in Slack.

**Stevie Kim:** Anything that helps. With PRDs, as long as I document the problem, key scenarios, and opportunity (the why—what it unlocks for us and the user), LLMs can flesh out the rest. They often raise assumptions I didn't think of. The key is getting those foundations right.

These are the conversations we needed to have after launch. Let's get into updates.

---

**Jose Farias:** Marcel is asking for filters on the overview screen—same filters we have in prompt tables. I'm working on it. The technical challenge: the overview shows brand perception snapshots, but to filter by prompt characteristics, we need to drop down and aggregate brand-prompt performance. It'll be slower (2-3 seconds), but that's acceptable since it's not the first screen.

We'll need to re-enable snapshotting of competitor and prompt performance. We removed that because of storage costs, but we didn't need it then since we only showed brand aggregates.

The trade-off: we can stop snapshotting subcategories since we removed the categories chart. This should balance out. I'll need one or two more days—not an easy one.

**Estevão Mascarenhas:** I'm working on a basic research workflow to improve subcategorization for about 30 brands. The main change: we'll expose all suggested subcategories during onboarding so users can remove irrelevant ones. Combined with Daniel's copy changes, that should work well.

I also need to investigate PostHog release tracking so we can attribute changes in the onboarding flow. I'll finish the workflow in 2-3 hours, then tackle P1 items.

**Pedro Steimbruch:** Today: added pagination back to sources page, submitted a PR for timezone handling on charts, merged the subcategory update PR, and shipped on-demand sitemap regeneration to S3. Tomorrow I'm investigating prompt suggestions—I think there are opportunities there to reduce reliance on subcategories.

**Stevie Kim:** I want to make sure we're aligned on Daniel's priorities. He broke them into P0 and P1. I'm going to tag Linear tickets accordingly. Does a P0/P1 system work for everyone?
