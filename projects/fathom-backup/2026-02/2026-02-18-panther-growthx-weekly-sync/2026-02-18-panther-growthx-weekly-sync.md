# Panther <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-18
time: 20:00 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants:
  - Kathy Lam (kathy@growthx.ai, GrowthX)
  - Ana Milosavic (ana.milosavic@panther.io, Panther)
  - Katie Campisi (katie.campisi@panther.io, Panther)
  - Seema Kumar (seema.kumar@panther.io, Panther)
  - Shannon King (shannon.king@panther.io, Panther)
fathom_recording_id: 123483717
fathom_url: https://fathom.video/calls/570059846
share_url: https://fathom.video/share/HgxLrPW3SYw-iL1PxFyP6fCm2sjAiuur
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Weekly content planning sync between GrowthX and Panther. Discussed messaging shift from "SIEM" to "AI SOC," reviewed early content performance metrics, and approved 12+ high-priority AI SOC blog topics. Key deliverables: finalized messaging narrative from Panther's CMO (Shannon) due this week, followed by full content refresh across all artifacts and upcoming articles.

---

## Context

Panther is repositioning from a traditional SIEM platform to an "AI SOC" platform—a foundational brand shift that requires content, messaging, and keyword tracking updates. GrowthX is managing the content production and messaging alignment. The team is using CheckThat (GrowthX's AI visibility index) to track how Panther ranks for "AI SOC" vs. legacy "SIEM" personas and monitor competitor visibility (VEGA, Dropzone, Profit). Strong early performance on the first batch of AI SOC content has validated the strategy; the team now needs to formalize Panther's company narrative (due from CMO Shannon this week) to unify all downstream content updates and prompt engineering.

---

## Relevance

- **Content Marketing (GrowthX):** Approved content roadmap validates AI SOC positioning and drives production priorities; messaging finalization enables rapid artifact updates.
- **CheckThat (GrowthX):** Persona-tagged prompts and month-over-month comparison feature will measure messaging shift ROI and inform LLM visibility strategy.
- **SEO & Keyword Research:** Competitive intelligence on VEGA, Dropzone, Profit informs prompt coverage and keyword priorities for content.
- **Technical Execution:** ToC sidebar bug fix and mid-article CTA placement are blockers for optimal conversion on long-form content.

---

## Overview

- **Track Messaging Shift:** Use CheckThat to track performance of the new "AI SOC" messaging vs. the legacy "SIEM" positioning.
- **Update Content with New Messaging:** A finalized company narrative is due from Panther's CMO (Shannon) next week, triggering a full content update.
- **Prioritize AI SOC Content:** Approved a new batch of AI SOC topics, including high-priority articles on architecture, integration, and the "AI vs. human" debate.
- **Resolve CTA Placement:** Fix the sidebar Table of Contents (ToC) bug to enable proper CTA placement and explore adding CTAs mid-article for better conversion.

---

## Key Topics

### Messaging Shift Tracking

  - **Goal:** Measure the impact of Panther's messaging shift from "SIEM" to "AI SOC."
  - **Method:** Use CheckThat to track performance by tagging prompts with "SOC persona" vs. "SIEM persona."
  - **Feature Request:** Kathy will request a month-over-month comparison feature in CheckThat to track progress over time.
  - **Prompt Strategy:**
      - Create prompts comparing "SIEM vs. AI SOC" to capture users researching the difference.
      - **Rationale:** Position Panther as an AI SOC platform that *includes* SIEM functionality to avoid alienating legacy SIEM users.
      - **Approval:** Review these comparison prompts with Shannon (CMO) before adding them to CheckThat.

### Content Performance & Strategy

  - **Initial Performance:** Strong early momentum for new blog posts.
  - **Indexing:** All but one of the last 5 posts are indexed; Kathy is manually pushing the last one.
  - **Technical SEO Audit:** In progress.
  - **Competitor Analysis:**
      - **Goal:** Analyze AI SOC competitors (Vega, Dropzone, Profit) to inform Panther's strategy.
      - **Action:** Kathy will run SEMrush on these competitors to find their ranking prompts and add them to CheckThat.

### Content Production & Logistics

  - **New Messaging Rollout:**
      - A finalized company narrative is due from Shannon next week.
      - GrowthX will then update all existing content and apply the new positioning to all future articles.
  - **CTA Placement:**
      - **Problem:** The sidebar Table of Contents (ToC) bug blocks the CTA on long posts.
      - **Solution:** Ana will ask Pixel 1 to fix the ToC bug and explore adding CTAs mid-article for better conversion.
      - **Interim:** For now, long posts will only have a bottom-of-page CTA.

### Topic Backlog Review

  - Approved the following AI SOC topics for production:
      - AI SOC analysts: what they do & where humans are still needed
      - Building an AI-powered SOC: architecture, trade-offs, priorities
      - Who's leading AI-powered SOC automation?
      - How to build an AI-enabled SOC (without rip & replace)
      - Where AI fits in your SOC workflow
      - AI agents in security operations: real vs. hype
      - Will AI replace SOC analysts?
      - AI SOC agents: what they can do & what's next
      - AI security platforms: what to expect & how to evaluate
      - How to integrate AI into your SOC without disrupting workflows
      - Is AI automation worth it? Cost, gains, & gotchas
      - Automating security operations with AI: where to start
  - **High Priority:**
      - "Will AI replace SOC analysts?"
      - "AI agents in security operations: real vs. hype"
      - "AI security platforms: what to expect & how to evaluate"
      - "Building an AI-powered SOC: architecture, trade-offs, priorities"
  - **New Topics Created:**
      - "Best AI SOC Tools" (repurposed from "Best SIEM Tools")
      - "Building an AI-enabled SOC Team" (combining two existing ideas)

---

## Action Items

**Katie Campisi (Panther)**
- Review new articles tagged in Notion
- Email finalized narrative/messaging to Kathy (due end of week, post-CMO alignment meeting)
- Ensure messaging doc aligns with launch positioning vs. company narrative

**Kathy Lam (GrowthX)**
- Implement CheckThat persona tags (AI SOC vs SIEM); tag existing prompts
- Request CheckThat month-over-month comparison feature from engineering
- Add new CTAs to published blogs (bottom + sidebar, pending ToC bug fix)
- Generate additional LLM prompts based on ICP questions; send to Shannon for review before adding to CheckThat
- Run SEMrush for VEGA, Dropzone, Profit; identify their ranking prompts and add to CheckThat
- Update ContentOS: correct AI SOC Analyst search volume; add "AI-enabled SOC team" topic; set priorities; move topics to phases; find alternative title for "next-gen SIEM"; add "best AI SOC tools" topic
- Once messaging narrative finalized: update all content artifacts + apply new positioning to all future articles

**Ana Milosavic (Panther)**
- Email Pixel 1 regarding sidebar ToC scrolling bug (blocks mid-article CTA placement)
- Explore mid-article CTA placement solution with design team

---

## Transcript

**Kathy Lam:** This meeting is being recorded.

**Ana Milosavic:** Hi, how's it going?

**Kathy Lam:** How are you doing?

**Ana Milosavic:** Good. How was your vacation?

**Kathy Lam:** Good, good. The first week and a half was iffy, but the last part was good. Yeah, the weather there was great.

**Ana Milosavic:** So it was nice. Good. Pretty good. We're really excited for this. I think we've noticed some momentum, and I think we're really excited to continue the progress and continue posting.

**Kathy Lam:** Awesome. We can actually jump into that. I think Ada shared the performance report. This is pretty cool for just the second week after posting. Of course, this is a shortened week, so we expect that to fill out, but pretty nice pickup. I reviewed the last five blogs that were posted last week to see if they were indexed. I think all but one is indexed, so I made sure to get Google to get on that.

**Ana Milosavic:** Awesome. Thank you.

**Kathy Lam:** Before we begin, anything top of mind?

**Ana Milosavic:** I wanted to discuss something we talked about last week. With our messaging changes from SIEM to AI SOC, we want to be able to really track that and see if we are getting traction with our new messaging. It would be really helpful if we can see the differences—are people still searching for us and finding us under SIEM categories? Are we improving in our AI SOC categories?

**Kathy Lam:** Yes. What we're going to do is, as we add prompts, tag them by persona. That way we can do SOC persona versus SIEM persona and filter by that. That way we can see if the visibility differs. Are there certain prompts that you would like us to check specifically for?

**Ana Milosavic:** I think Ada created some last week.

**Kathy Lam:** I believe Ada added that already. What we're going to do is differentiate that between AI SOC and SIEM and then take a look there.

**Ana Milosavic:** Just a quick question—right now we can't look at historical data or comparisons. I'd love to be able to see how we're progressing—where we're at this week versus three weeks from now. Do you think the best way would be for me to go in weekly and take screenshots?

**Kathy Lam:** You're right, we want to do month-over-month comparison. Let me ping the eng team and make it a feature request. You want to do something like GA4, where you can select and do comparison?

**Ana Milosavic:** Yeah, that would be really helpful. Even month-over-month or if we're selecting seven days and can compare it to the previous period would be fantastic.

**Kathy Lam:** Yep, being able to compare.

**Katie Campisi:** I think it should be finalized the end of this week. Our new CMO Shannon is meeting with Jack tomorrow to go through the finalized doc—the whole company narrative and messaging. Then we'll also have a messaging doc next week. That's the launch positioning versus the company-wide narrative on how we've shifted.

**Kathy Lam:** Perfect. So once that's finalized, we'll take that document and update all of our artifacts with it, and then change upcoming articles to reflect the new positioning.

**Ana Milosavic:** If we have time at the end of the meeting, I think it would be helpful to go through and approve everything again.

**Kathy Lam:** Yep, we can totally do that. We've published five blogs and we're working on five more for this week. Feel free to take a look at the current drafts, and then we'll review them. We will also add the new CTAs. Thank you for sending them over last week. We'll be making sure we incorporate those even in the blogs we've already released.

**Ana Milosavic:** Okay, just one note. The trouble is we can only add CTAs at the bottom or on the sidebar, not anywhere in the text. We have both available, so they can put a CTA at the sidebar and the CTA at the bottom. However, some of the longer blog posts have a pretty long table of contents. That table of contents is in the area where the CTA would sit in the sidebar. So for any that have a long table of contents, the CTA can only go at the bottom.

**Katie Campisi:** I think something is wrong with our table of contents in the sidebar. When I was publishing the latest Threat Research blog yesterday—it's 40 pages long—it does not scroll down. Even when I scroll all the way to the bottom, the sidebar is cut off. If that was scrolling correctly, we could add it and eventually you'd see it in the sidebar if you scrolled that far.

**Ana Milosavic:** Yeah, I need to bring that up with Pixel 1. We missed our Monday meeting because it was a holiday. The ideal scenario is they can get it into the block of text. That would be better than just having it at the bottom or on the sidebar. I'll still work on it.

**Kathy Lam:** Yeah, like in the middle of the blog. Some of these blogs are long enough that we might get a person midway through, and then we could convert them there rather than have them wait to the bottom.

**Ana Milosavic:** Exactly. I feel like there has to be a solution. It's impossible that the only solution is bottom or sidebar.

**Kathy Lam:** After reviewing the phase one summary, are there any questions or thoughts?

**Katie Campisi:** No questions. I was very encouraged and excited.

**Kathy Lam:** Yeah, it's great when we see these early signs. Given your authority score and how topical this is, I think we've hit the point where there's a lot of interest in this. I also wanted to let you know we're doing a technical SEO audit. I'm not sure when it will be done, but it's in progress. The resource has already been assigned. Some of the articles are already getting picked up by LLMs. Do you have any prompts you want to make sure we include besides the ones Ada added last week? Or I can generate more additional ones. I look at the keywords and think about the ICP and come up with questions they would ask on Claude or ChatGPT. I'll make sure those are done before the end of the week.

**Ana Milosavic:** I think that's good. Once we have the messaging doc, we can probably create prompts from there. Katie, do you think it would be helpful to do SIEM versus AI SOC kind of stuff?

**Katie Campisi:** If people are researching the difference between SIEM and AI SOC, yeah, I think that makes sense. I assume we'd want Shannon and Jack to read those and make sure it's nailing what we want. There's a nuance where an AI SOC platform like Panther includes a SIEM. So that's how we're threading it—we're still very much used as a SIEM and seen as a SIEM by a lot of people. We don't want to scare off people who are looking for a SIEM.

**Kathy Lam:** So we'll review those specific prompts with Shannon first before we add them to CheckThat. In general, do you have feedback about the blogs? Are they the right technical level? Is there good engagement?

**Katie Campisi:** No concerns. I think the technical level is good. I usually give them a read-through and have Claude check against our persona and current messaging to flag anything I might have missed. As long as that looks good, I approve it. There've been a couple random things I've flagged, but they're small. Each time we do that, it iterates better the next time. I think it's been going really well.

**Kathy Lam:** Yeah, every time you provide feedback, we take that and add it as a rule into our Atlas tool to make the next articles better. I had one other question. I had asked Ada to add another competitor—VEGA—an AI SOC competitor. Are we able to see their prompts and what they're ranking for?

**Ana Milosavic:** Can we use that as inspiration? A lot of their stuff would lean into what we're trying to do.

**Kathy Lam:** I can look at where they're visible via the sources. VEGA, V-E-G-A, right? They're not really showing up in the prompts we're checking for. I'll do some keyword research—run SEMrush on them to see what's being indexed and then see what prompts might be leading to their pages. If the same prompts are there, I'll make sure we're tracking that as well.

**Katie Campisi:** I think Dropzone and Profit are worth doing because we want to siphon their business specifically.

**Kathy Lam:** Dropzone, VEGA, and Profit. I will run SEMrush for those.

**Katie Campisi:** Yeah, there's a long list of AI SOC tools right now, but a lot of them seem like clones of the same thing. Some of them look so much like Panther, I can't help but imagine it's not an accident.

**Kathy Lam:** I wonder if they're just asking Claude to create a version of this. The copy is so bad on their websites—I know they just copy-pasted this out of ChatGPT. They all say "the speed of AI," and I don't know what that means. That would frighten me as a security person because I want someone who has thought through all the repercussions, added guardrails, actually done this at a company before they just copy-pasted something.

**Katie Campisi:** My hunch is a lot of these little offshoots will be gone in 18 months, but right now it's very crowded.

**Kathy Lam:** Yeah. A lot of them are just features that exist in larger platforms.

**Katie Campisi:** When I came across one, all it does is give feedback on detection logic and suggest rewrites. You don't even need a special tool for that if you have Claude. But also if it's in a tool like Panther and it's in your SIEM, you don't need to buy another tool to attach to it.

**Kathy Lam:** It doesn't make sense for them. Everyone has access to all the AI tools. Most security analysts are used to being in a certain tool. Adding one new thing doesn't help them. You'd want a tool that naturally handles those issues, investigates as much as needed, and only escalates if it can't be resolved.

**Katie Campisi:** Yeah, that's my take on the landscape.

**Kathy Lam:** Okay, let's spend a couple minutes going through the AI SOC-related topics on the backlog. The first one is "Machine Learning and Cybersecurity Applications and Benefits." Is this something we want to do or keep in backlog?

**Katie Campisi:** I might keep this in backlog for now. It's a little more abstract.

**Kathy Lam:** Yep. The next one is "AI SOC analysts: what they actually do and where they still need humans."

**Ana Milosavic:** The volume is so low.

**Kathy Lam:** Right. I feel like it was larger. When I did keyword research, the term AI SOC wasn't that low. Normally we wouldn't have added it if it was so low. I mean, I think the topic makes sense.

**Ana Milosavic:** We have a lot of Jack's podcasts that talk about this—where do you actually still need humans? Where can you use AI? I feel like there's a lot of good CTAs we can include.

**Kathy Lam:** So I think we'll do it. I will update the AI SOC Analyst number because it's more than that. Yeah, I just found it. It's like 140. I'm going to go in there and fix this. The keyword difficulty is much harder, but I think we should still include additional keywords to make sure we target it. The next one is "Building an AI-powered SOC: architecture, trade-offs, what to prioritize." It's a little low, but we're looking from high to low.

**Katie Campisi:** Yeah, I think that would make sense.

**Kathy Lam:** "Who's leading AI-powered SOC automation? A practitioner's market map." Okay. "How to build an AI-enabled SOC: lessons from teams that did it without ripping and replacing." Yeah.

**Ana Milosavic:** What about "How to build an AI-enabled SOC team?" We have the SOC analyst prompt that has higher volume. Can we make this about teams too—how to build a security team that can work with an AI-enabled SOC?

**Kathy Lam:** Yes, I think this makes sense. I just did that. "Where AI fits in your SOC workflow?" "AI agents in security operations: what's real? What's hype?" "Will AI replace SOC analysts?" That's a good one.

**Katie Campisi:** Yeah, that's very topical.

**Kathy Lam:** High priority. I'll fix this right after the call.

**Katie Campisi:** I'd say the two right above it also.

**Kathy Lam:** I think the architecture one too.

**Katie Campisi:** Yeah, that one too.

**Kathy Lam:** "AI SOC agents: what they can do and what's next." "AI security platforms: what to expect and how to evaluate them." "How to integrate AI into your SOC without disrupting existing workflows." "Is AI automation worth it? An honest look at the cost, gains, and gotchas." "Automating security operations with AI: where to start when everything feels manual."

**Katie Campisi:** I think that sounds good.

**Kathy Lam:** Are there any we just talked about that are top priority?

**Katie Campisi:** I'd say, let me quickly scan. I think these all look great. "Next gen SIEM"—let's keep that considering for now. We might want to workshop the title.

**Ana Milosavic:** So the "best SIEM tools"—do we want to do "best AI SOC tools" and just change the SIEM language?

**Kathy Lam:** Yeah, let's do that. Because we're trying to see where Panther fits. A lot of people are still searching for SIEM, most traffic is coming from SIEM, but most new traffic coming from especially cloud-native teams will probably be searching for AI SOC. So you're going to get more and more pick up that way. Yeah, let me make sure we add those two topics.

**Ana Milosavic:** That was the only thing I wanted to point out. And then I am good.

**Kathy Lam:** Thank you. Excellent. Just as a quick recap—making sure we're able to compare CheckThat prompts between AI SOC and SIEM. Review some of the competitors and make sure any prompts that lead to them we're also tracking. We'll continue producing and once you have the new messaging, we'll start updating the content and artifacts. Then we'll use that to rebuild the content strategy and re-pivot some of the other topics as well.

**Ana Milosavic:** Thank you so much.

**Kathy Lam:** Thanks so much. I'll catch up with you next week.

**Ana Milosavic:** Bye.

**Kathy Lam:** Bye.
