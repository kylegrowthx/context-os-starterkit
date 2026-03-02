# Netwrix <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-25
time: 16:00 UTC
duration: 25 minutes
organizer: team@growthxlabs.com
participants:
  - Mariel Grinstein (Netwrix)
  - Aida Knezevic (GrowthX)
  - Kathy Lam (GrowthX)
  - Philipp Denisenko (Netwrix)
  - James Levin (Netwrix)
  - Ralph Marino (Netwrix)
  - John Knightly (Netwrix)
  - Chanel Chambers (Netwrix)
  - William Leborgne (GrowthX)
  - Ani Grigoryan (Netwrix)
fathom_recording_id: 125260250
fathom_url: https://fathom.video/calls/578565752
share_url: https://fathom.video/share/zyMfQYzNAM147jWRJ6VqkNRksA9yixhR
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX and Netwrix reviewed content delivery progress, with 7 articles published and 3 more in review. The team resolved a critical Sanity workflow blocker (staging vs. production environment confusion) and confirmed that Netwrix's "Shadow AI Security" article is a top performer, validating the executive-focused content strategy. Two additional requests emerged: adding the ability to hide specific articles from the blog index, and creating a content repurposing workflow for Netwrix's PR and thought leadership pieces.

---

## Context

This is a weekly operational sync between GrowthX and Netwrix, the core stakeholders in a content marketing engagement focused on cybersecurity and AI security positioning. GrowthX is delivering 20+ articles on topics ranging from product alternatives (Varonis, CyberArk) to AI security and governance. Netwrix has a weekly review cadence and provides feedback on drafts before publication. The meeting surface critical technical issues (Sanity environment misconfiguration) that had been blocking content deployment, plus strategic input on content focus areas and repurposing opportunities. The engagement is entering phase two, moving from bulk content creation to a sustained publishing and refinement model.

---

## Relevance

- **Content Delivery:** Track article pipeline progress, publishing velocity, and review cycle
- **Technical Blockers:** Sanity configuration issues affecting deployment (now resolved)
- **Content Performance:** Validation of high-level AI/CISO-focused content strategy via organic traffic and LLM referrals
- **Content Expansion:** New requests for content repurposing and index visibility control
- **Relationship:** Operational health check between client and agency teams

---

## Overview

- **Sanity Workflow Blockers:** Publishing is blocked by two issues: 1) content not syncing from Sanity to the live site, and 2) no option to hide specific articles from the main blog index.
- **"Shadow AI" Article Success:** The "Shadow AI Security" article is a top performer, driving the most organic traffic and receiving 3 visitors from LLMs. This validates the strategy of targeting executives with high-level content.
- **Content Repurposing:** Netwrix requested a new artifact to repurpose their PR/thought leadership content (e.g., Forbes articles) into unique blog posts, enriching content with expert insights without creating duplicates.
- **Guide Ungating:** A new pipeline is being built to ungated guides, using the PDF as a research input to create refreshed articles with new CTAs.

---

## Key Topics

### Sanity Workflow Blockers

  - **Content Syncing Failure:** Edits in Sanity are not appearing on the live site.
      - **Cause:** GrowthX was using the Sanity staging environment, which requires a web team sync to push changes live.
      - **Solution:** Use the Sanity **production** environment for all edits.
      - **Context:** Mariel noted sync issues have affected the production environment itself on recent days (Fri, Mon, Tue), which the web team has fixed.
  - **Blog Index Visibility:** Netwrix wants to hide specific articles (e.g., podcast recaps) from the main blog index page.
      - **Rationale:** These articles are highly niche and not relevant to a general audience.
      - **SEO Impact:** Hiding them will not hurt SEO, as the articles remain discoverable via direct links and are in the same subfolder.
      - **Action:** GrowthX will draft a request for the web team to add this feature to Sanity.

### Content Performance & Strategy

  - **"Shadow AI Security" Article:**
      - **Performance:** Top performer by organic traffic and average position (per Looker dashboard).
      - **Feedback:** A Netwrix security director called the article "super high level."
      - **Validation:** The article is successful because it targets executives (CISOs) who need high-level overviews, not deep technical detail.
      - **Next Step:** Research more specific topics within the AI security cluster (e.g., "how to monitor AI apps") to balance the strategy.
  - **Content Repurposing:**
      - **Request:** Create a new workflow to repurpose Netwrix PR/thought leadership content (e.g., Forbes articles by Grady and Michael Watzel) into unique blog posts.
      - **Goal:** Enrich content with expert insights without creating duplicate content.
      - **Precedent:** GrowthX has successfully used a similar process (interviewing internal experts) for a past client.

### Content Pipeline & Status

  - **Published:** 7 articles are live and indexed, including new Varonis and CyberArk alternative articles.
  - **In Review:** 3 articles are awaiting Netwrix feedback.
  - **Upcoming:** 7 new articles will be delivered this week to catch up on the schedule.
  - **Guide Ungating:** A new pipeline is being built to ungated guides.
      - **Process:** Use the PDF as a research input → refresh the article with new online research → add new CTAs.
      - **Timeline:** The pipeline will be ready this week, with content production to follow.

---

## Action Items

**Philipp Denisenko (Netwrix)**
- Confirm with John Knightly on updated product messaging; share the details with Kathy

**Aida Knezevic (GrowthX)**
- Deliver 7 new articles this week to Mariel and Philipp for review
- Prepare clear Sanity instructions (hide articles from blog index; use production environment only); send to Mariel for web team forwarding
- Check with Ade on Sanity production sync issues and timing windows for safe edits
- Research AI security subtopics (e.g., "how to monitor AI apps") to complement "Shadow AI Security" strategy
- Explore content repurposing workflow for Netwrix PR and thought leadership (Grady, Michael Watzel); proposal and feasibility report back to Mariel

**Mariel Grinstein (Netwrix)**
- Send miniature Netwrix logo to Aida/Kathy via Slack for blog header
- Review 3 pending articles and send feedback to Aida/Kathy by tomorrow

---

## Transcript

**Aida Knezevic:** This meeting is being recorded.

**Kathy Lam:** Hello. Good evening.

**Aida Knezevic:** Good afternoon. For me, it's 5 p.m.

**Kathy Lam:** Hey, Philipp. We heard you for a second, but I think you're on mute.

**Philipp Denisenko:** Yeah, I'm in Starbucks, so I'm muted myself.

**Kathy Lam:** Excellent. Were you able to get any of our emails or Slack messages this week?

**Philipp Denisenko:** Yes.

**Kathy Lam:** Okay. I think John mentioned that Slack wasn't working for a bit, but primarily, I had spoken to him on Thursday. He mentioned you guys have some updated product messaging. I'm hoping we can get a copy of it.

**Philipp Denisenko:** Okay, yeah, let's double check with John. It's hard to say exactly what he has in mind, honestly.

**Aida Knezevic:** Hi, Mariel. Are you able to access Slack? I know a bunch of you were removed from the Slack channel.

**Mariel Grinstein:** Hi, yes. I can see the channel. All good.

**Aida Knezevic:** Okay, perfect. Let's get started then. I'm going to share my screen.

**Mariel Grinstein:** Okay, so we have a lot of articles to review.

**Aida Knezevic:** Yeah, we're working on a batch of content that we'll send over soon. Before we get into the feedback, I want to share some content updates. We have three drafts still with your team for review. We'll be sharing seven articles this week to catch up with two from last week, because we had to update some of the competitive product listicles. John shared some additional competitors we should include in one of the articles. We updated those first. And we've published four new blogs, so now we have seven articles that are live and indexed. This week we published our first alternative articles: Varonis and CyberArk alternatives. By next week, we should see the impact in search traffic and impressions.

**Mariel Grinstein:** One thing we didn't want to happen is they're showing up on the main blog page. Also, the Netwrix logo looks condensed. Do you have a different version we could use?

**Aida Knezevic:** We can use the miniature version if you can send it in Slack. And regarding hiding articles from the index page, let me check with Ade to see if we have that option when publishing. If not, we'll need to contact your web team to set that feature in Sanity.

**Mariel Grinstein:** Okay, let me check quickly in Sanity if there's an option.

**Philipp Denisenko:** I was wondering if hiding them from the index page would hurt the domain authority being passed to that page.

**Aida Knezevic:** No, we should be fine. It's the same subfolder and it's discoverable. Everything gets indexed fast. As long as it's discoverable through other links on the website, it won't hurt SEO.

**Philipp Denisenko:** Right, there's no point in having these niche podcast recap articles visible to everyone.

**Mariel Grinstein:** Yeah, I'm checking and there's no way to do it in Sanity currently. So we'll need to request this from the web team.

**Aida Knezevic:** Okay, we'll prepare clear instructions on what we need in Sanity and you can forward it to the web team. And on the Sanity issue itself, we're still dealing with content not showing up on the live site when we publish or update articles. Ade mentioned you have two versions of Sanity: production and staging. Sometimes the content doesn't match between them.

**Mariel Grinstein:** You always need to use production, not staging. To move changes from staging to production, you need the web team.

**Aida Knezevic:** So we should always edit on production directly. That's good to know. We're in week seven now and preparing for phase two where we'll be publishing content regularly every week and refreshing lots of content. I don't want this to burden you, Mariel, where we have to tag you each time to check why something isn't live.

**Mariel Grinstein:** There were actually a couple of days, like Monday and Friday, where even edits to production didn't sync to the live site. I escalated to the web team and they fixed it. Yesterday we also had some issues, but it worked fine in the afternoon.

**Aida Knezevic:** Okay, I'll check with Ade to see if he ran into issues as well. Now, on the guide ungating: James gave us feedback on which two guides to prioritize. We're building a new pipeline to update those blog posts. We want to use the PDF gated guide as an input at the research stage. We'll build an extra step where we can upload the PDF or copy a markdown version. When we refresh the article, it will use information from the gated guide plus new online research, then we can add new CTAs. Hopefully that pipeline will be ready this week. And regarding the "Shadow AI" article, it's doing really well. If you access your Looker dashboard, you can see the cohort report. Make sure to uncheck non-GrowthX URLs. When you look at the data, the "Shadow AI Security" article is getting the most traffic and has a quite high average position. It's also gotten three visitors from LLMs. So we want to do additional topic research in that cluster.

**Mariel Grinstein:** Our director of security research said the Shadow AI Security article was super high level and might not interest readers. I'm not sure though—he's very technical and writes with code snippets, so his benchmark is different.

**Aida Knezevic:** Who is he thinking about as the reader?

**Mariel Grinstein:** CISOs, I guess?

**Aida Knezevic:** Right. Our content strategy targets more executives, and many of them aren't as versed in technical details. The article validates that. We can explore more specific subtopics under Shadow AI, like "how to monitor AI apps" or "how to monitor what people are using AI for." I've seen those topics in SEMrush, so we could add them. That would be pretty specific, not vague.

**Mariel Grinstein:** Yeah, that would be cool. The article is good overall.

**Aida Knezevic:** Thanks for the heads up. I think those are all the updates.

**Kathy Lam:** No, I think that was primarily it.

**Aida Knezevic:** Okay, cool. Is there anything else you'd like to discuss or any feedback on things we haven't covered?

**Mariel Grinstein:** Yeah, one thing. We're changing our AI positioning, so it's not wise for me to be too involved right now. But Grady and Michael Watzel do a lot of PR articles—really good soft leadership content. Is there a way we could repurpose those without being flagged as duplicate content?

**Aida Knezevic:** Yeah, that's totally something we could build as an artifact and use it to enrich existing content. I remember last summer working with a tax startup. There's a lot of content about taxes online, but it's very generic. We ended up interviewing people on their sales team and internal experts, then used their quotes in the content. When you have actual experience with something, there are always insights people notice but that aren't in online content.

**Mariel Grinstein:** I'll look into that as well and get back to you.

**Aida Knezevic:** Great. Keep us posted on the three articles you're reviewing.

**Mariel Grinstein:** I left myself a task for tomorrow. I'll give you feedback tomorrow.

**Aida Knezevic:** Amazing. Thank you. I'll send a follow-up in Slack later. Bye.
