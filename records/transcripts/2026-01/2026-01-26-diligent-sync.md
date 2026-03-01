# Diligent Sync

<metadata>
date: 2026-01-26
time: 18:31 UTC
duration: 37 minutes
organizer: ademilade@growthx.ai
enriched_on: 2026-02-28 02:15 UTC
participants:
  - name: Ademilade Shodipe-dosunmu
    email: ademilade@growthx.ai
    affiliation: GrowthX
    role: Head of Delivery & Operations
  - name: Pamela Weber
    email: pamela@growthx.ai
    affiliation: GrowthX
    role: Content Producer
  - name: Carrie Chowske
    email: carrie@growthx.ai
    affiliation: GrowthX
    role: Client Lead (Diligent)
fathom_recording_id: 117160236
fathom_url: https://fathom.video/calls/544634563
share_url: https://fathom.video/share/7HrJATyQLB9sKQ52yzDhVzafbuEUqVEg
source: fathom
</metadata>

---

## Summary

Ademilade trained Pamela on the Diligent content production workflow, covering article creation, editorial QA, the multi-step submission pipeline, and weekly performance reporting. The team discussed workarounds for a broken Agentic Refresher pipeline, shared Airtable access structures, and clarified deadlines for article submissions to the client's Optimizely CMS.

---

## Context

Diligent is a high-touch, high-stakes content client requiring accurate, enterprise-focused articles for decision-makers. The content production process is complex: articles move through multiple stages (drafting, QA, internal review, client submission, client review, and publication) with strict deadlines. The team uses Airtable for internal workflow management, the client's Optimizely CMS for submission and review, and Looker for performance tracking. This meeting focused on onboarding Pamela Weber as a new content producer for the account, ensuring she understands the editorial standards, technical workflows, and client expectations.

---

## Relevance

- **Operational Onboarding:** Critical for bringing a new team member up to speed on a strategic client account with complex workflows and strict editorial standards.
- **Client Retention:** Diligent is a $200k+ annual engagement; clear processes and consistent output quality are essential to maintaining the relationship.
- **Process Documentation:** The team identified gaps in existing documentation (Loom tutorials, updated editorial checklists) that need to be created to support scaling and consistency.
- **Workflow Optimization:** Discussion of pipeline failures and manual workarounds highlights ongoing technical debt that may require engineering involvement.

---

## Overview

- **Process Workaround:** The broken `Agentic Refresher` pipeline requires a manual workaround: generate a net-new draft and "stitch" it with the old article to preserve context.
- **High-Stakes Content:** Diligent's content is for enterprise decision-makers, demanding extreme accuracy. The post-processing editorial checklist is critical for catching errors.
- **Complex Workflow:** The submission process is multi-step, using Airtable for internal tracking and the client's Optimizely CMS for submission, which triggers a multi-team review.
- **Key Deadlines:** Articles are due in Optimizely by Thursday EOD to allow for the client's review cycle. The Looker dashboard must be updated every Monday.

---

## Key Topics

### Diligent Content Production Process

  - **Pipeline Workaround:** The `Agentic Refresher` pipeline is broken.
      - **Solution:** Generate a net-new draft and manually combine it with the old article to preserve context.
  - **Net-New Pipeline (`Articles Agent`):**
      - **Workflow:** Research → Draft → Enforce statistical constraints → Internal linking → Source linking → Validate guidelines → Add metadata, expert quotes, & Diligent proofpoints.
      - **Known Issues:**
          - Internal linking is inconsistent and often requires manual fixes.
          - Mid-text CTAs frequently have broken links that must be replaced.
  - **Post-Processing & QA:**
      - Export the Atlas draft to Claude.
      - Use the project's editorial checklist to flag issues and get fix recommendations.
      - Apply editorial judgment to finalize the article.
  - **Images:**
      - **Source:** `brand.diligent.com`
      - **Requirement:** Minimum of one product image per article, with alt text.
      - **Cover Image:** Handled by Sulaiman during publishing.

### Airtable & Workflow Management

  - **`Approved to Start`:** Add new articles here, mapping them to the correct topic cluster, product, and business unit.
  - **`In Production`:** Move articles here when work begins.
  - **`Reviewing Diligence`:** Move articles here when ready for client submission.
  - **Topic Selection:** Select topics from the `Approved to Start` column based on client priorities (e.g., LLM gap refreshes).

### Submission & Publishing Process

  - **Submission to Optimizely (Client CMS):**
      - Use the team account to upload the finalized article.
      - **Status Flow:** `Created` → `Content Review` → `SEO Review` → `Revisions Done` → `Publishing` → `Publish Blog Completed`.
  - **Publishing Request to Sulaiman:**
      - Submit a Linear ticket with links to the final document and the live article (for refreshes).
  - **Timeline:**
      - **Thursday EOD:** Submit articles to Optimizely.
      - **Following Monday/Tuesday:** Client review and feedback.
      - **Following Tuesday:** Submit revised articles to Sulaiman for publishing.
      - **Result:** A \~1-week lag between submission and publication.

### Looker Dashboard Updates

  - **Cadence:** Every Monday.
  - **Rationale:** Provides accurate performance data for the client's weekly meeting.
  - **Tool:** Use the Claude B Pod project to convert URLs to the required format for Looker.
  - **Threshold:** Flag Ademilade or Carrie when a dashboard reaches 200 URLs, as this requires a special process.

---

## Action Items

**Pamela Weber (GrowthX)**
- Send 1 Diligent draft to Carrie (GrowthX) for quick review
- Replace broken mid-text CTA link in Diligent draft
- Add product image(s) w/ alt text from brand.diligent.com to Diligent drafts
- Fix intro/section merging in Diligent draft via Claude
- Update Looker for Descern and Yerko for missed weeks
- Own weekly Diligent Looker updates starting next week

**Ademilade Shodipe-dosunmu (GrowthX)**
- Archive unused Diligent pipelines in Atlas
- Flag internal linking step to ENG; rerun as needed
- Rename Airtable view to Pamela; grant access
- Add FedRAM topics to Diligent Approved to Start in Airtable
- Record and share Loom tutorials: Optimizely, Looker (DHS), other Diligent tasks
- Add updated editorial checklist to Diligent project
- Send meeting recording to Carrie (GrowthX)

---

## Transcript

**Pamela Weber:** Yeah, but it's over as of today, so it's better.

**Ademilade Shodipe-dosunmu:** Carrie was supposed to join this call, but I think she had it marked tentative.

**Pamela Weber:** I'm not sure if she's coming.

**Ademilade Shodipe-dosunmu:** Okay, so let me walk you through the Diligent content production process from the production side. This is going to be a high-level overview, but you'll get more context as we work through things together.

**Ademilade Shodipe-dosunmu:** Let's start with pipelines, because that's the main way you'll be doing most of the work.

**Ademilade Shodipe-dosunmu:** So we have this inline image generation pipeline.

**Pamela Weber:** Are you screen sharing?

**Ademilade Shodipe-dosunmu:** Yes, I'm showing the screen now.

**Ademilade Shodipe-dosunmu:** So the inline image generation pipeline is for images within the articles themselves, but we haven't gotten approval to use those images yet, so we can ignore this for now. I'm going to archive the unused pipelines so it's not confusing when you're working.

**Pamela Weber:** What are we using for images? Where do we get product screenshots?

**Ademilade Shodipe-dosunmu:** I'll show you in a moment. Let me archive the ones we're not using first.

**Ademilade Shodipe-dosunmu:** So the two active pipelines we'll be using are the Agentic Refresher and the Articles Agent.

**Ademilade Shodipe-dosunmu:** The Agentic Refresher pipeline isn't working properly right now. Engineering is working on a ticket to fix it. So for now, when we're refreshing articles, the workaround is to generate a net-new version and then manually stitch it together with the existing article to preserve context.

**Ademilade Shodipe-dosunmu:** Here's how it works: after you do your research and check the SERPs to identify where keywords are needed and what sections to add, you generate a fresh article using the net-new pipeline. Then you compare the new version with the existing article and stitch them together. If a section from the old article is still solid, you keep it. Then you bring in new sections from the net-new version and edit for context and relevance.

**Ademilade Shodipe-dosunmu:** It's not perfect, but it's the workaround we have until the refresher is fixed. Everything else runs through Atlas.

**Ademilade Shodipe-dosunmu:** The net-new pipeline workflow is straightforward. The researcher researches the topic, then the drafter creates a draft. Then we have a processing agent that enforces statistical constraints—it ensures we're using the right types of statistics and referencing them correctly. Then we do internal linking, add source links for referenced stats, validate against guidelines, add metadata, and integrate expert quotes and Diligent proofpoints.

**Ademilade Shodipe-dosunmu:** One thing to flag: the internal linking step doesn't always work perfectly. Sometimes it adds internal links, sometimes it doesn't. For now, I've been manually adding internal links since I've worked with this account for a while, but long-term we should flag this to engineering to fix.

**Ademilade Shodipe-dosunmu:** Diligent specifically wants expert quotes woven into the articles, and they prefer their own internal statistics over external sources. That's in the operating manual.

**Ademilade Shodipe-dosunmu:** One common issue: mid-text CTAs sometimes have broken links that you'll need to replace. And for images, we source them from brand.diligent.com based on topical relevance. All images need alt text. The cover image is handled by Sulaiman during publishing, but you need at least one product image per article—could be one or two depending on what fits.

**Pamela Weber:** Got it, thanks.

**Ademilade Shodipe-dosunmu:** So that's the net-new process. For refreshes, it's more involved because of the stitching workaround I mentioned.

**Ademilade Shodipe-dosunmu:** Now for Airtable. I've assigned you four articles: three net-new and one refresh. The refresh is on UK governance code, so you'll want to research if there have been any recent updates to the law for that article.

**Ademilade Shodipe-dosunmu:** Here's the Airtable workflow. In the "Approved to Start" column, you add new articles that are ready to work on. You map them to the correct topic cluster, product, and business unit. For example, Vivek mentioned FedRAM topics that I'll add to Approved to Start, and you'd do the same when new topics come in.

**Ademilade Shodipe-dosunmu:** The "In Production" column shows what's being worked on this week. Simia and I are working on about seven articles this week, plus some extras for next week.

**Ademilade Shodipe-dosunmu:** Once an article is done, it moves to "Reviewing Diligence" before it's submitted to the client. I'll rename this view to yours and give you access.

**Pamela Weber:** So when I add them to Approved to Start, how do I map them by topic cluster?

**Pamela Weber:** You add the title and then how do you group it?

**Ademilade Shodipe-dosunmu:** So you add it like here, you group it.

**Ademilade Shodipe-dosunmu:** For example, I had to add a random one.

**Ademilade Shodipe-dosunmu:** And I would have to, these are the topics I would have to.

**Ademilade Shodipe-dosunmu:** Figure out, like, which topic cluster it it is.

**Pamela Weber:** Okay, I see it.

**Ademilade Shodipe-dosunmu:** Yeah, so you attach it to whichever topic cluster makes sense up here.

**Ademilade Shodipe-dosunmu:** If a topic cluster is in there and you're covering it, you might have to flag to Vivek that, oh, yeah, this doesn't fit into any of it.

**Ademilade Shodipe-dosunmu:** I keep saying Vivek, I mean, Kari, because it's next season.

**Ademilade Shodipe-dosunmu:** So you might have to flag to your EM that, like, the topic cluster hasn't been added yet.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** And how do you know which is which this week?

**Pamela Weber:** I mean, you gave it to me, so I know what I'm working on now.

**Pamela Weber:** But, like, for next week, do I just see what's approved and I just give myself five articles?

**Pamela Weber:** Or is there, like, five?

**Pamela Weber:** Yeah, yes.

**Pamela Weber:** Yeah, you can.

**Pamela Weber:** Yeah, you can.

**Ademilade Shodipe-dosunmu:** It's pretty much here.

**Ademilade Shodipe-dosunmu:** So it's all in our group to start.

**Ademilade Shodipe-dosunmu:** So you can pick topics to work on here based off of whatever they are prioritizing.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** So right now, this week, I was prioritizing this LLM gap refreshes because, you know, they are trying to close, like, LLM gaps.

**Ademilade Shodipe-dosunmu:** So I was prioritizing these.

**Ademilade Shodipe-dosunmu:** So that.

**Ademilade Shodipe-dosunmu:** Like, you could just, like, you know, run them off.

**Pamela Weber:** I'm sorry.

**Pamela Weber:** What do you toggle it to, which means you're starting?

**Pamela Weber:** What is it here?

**Pamela Weber:** Is it ready to start, like the other one?

**Pamela Weber:** What does it mean?

**Pamela Weber:** In production.

**Pamela Weber:** Oh, in production means you're working on it.

**Pamela Weber:** Okay.

**Pamela Weber:** Yeah.

**Pamela Weber:** Yeah, exactly.

**Ademilade Shodipe-dosunmu:** So, yeah, you just picked up from here.

**Ademilade Shodipe-dosunmu:** You just asked your EM, like regarding picking topics.

**Ademilade Shodipe-dosunmu:** I think some MEs own end-to-end production.

**Ademilade Shodipe-dosunmu:** I think all MEs own end-to-end production.

**Ademilade Shodipe-dosunmu:** So, it's a bit like I would pick based on, because, like, I would have probably seen the transcript from the meeting.

**Ademilade Shodipe-dosunmu:** So, I know what they're prioritizing the week.

**Ademilade Shodipe-dosunmu:** Or Vivek would have let me know, hey, they want to prioritize this this week or this in the next two weeks or something.

**Ademilade Shodipe-dosunmu:** So, I have that in my mind.

**Ademilade Shodipe-dosunmu:** And, like, I, you know, use that to, like, pick the topics as well.

**Ademilade Shodipe-dosunmu:** So, yeah, just like confirm, like, hey, what cluster they're focusing on or what product or business unit they're focusing on.

**Ademilade Shodipe-dosunmu:** Then you can prioritize based on that.

**Ademilade Shodipe-dosunmu:** And, like, add five to you.

**Ademilade Shodipe-dosunmu:** Then, yeah, then once you're doing an article, there's an entire process for this, I would have to record looms for you because the process of submitting an article to diligence isn't like very, it's straightforward, but it's just like very roundabouts.

**Ademilade Shodipe-dosunmu:** So essentially, we use Airtable internally, GrowthX is Airtable 2, as our content OS, right?

**Ademilade Shodipe-dosunmu:** That makes sense.

**Ademilade Shodipe-dosunmu:** And most clients adopt Airtable as their content OS as well, right?

**Ademilade Shodipe-dosunmu:** You know, we do everything and submit stuff directly in Airtable and all of that.

**Ademilade Shodipe-dosunmu:** Diligence, however, has a lot of bureaucratic, for lack of a better word, crap.

**Ademilade Shodipe-dosunmu:** So they have their own system for managing content.

**Ademilade Shodipe-dosunmu:** So essentially, when we're going to submit articles, we have to move them to the required status here, right?

**Ademilade Shodipe-dosunmu:** So you move it to reviewing diligence here, right?

**Ademilade Shodipe-dosunmu:** Once an article is ready to go, then you have to move it to their platform called Optimizely.

**Ademilade Shodipe-dosunmu:** To get it to Optimize.ly, you use the team account, the team logins.

**Ademilade Shodipe-dosunmu:** This is also detailed in the operating manual.

**Ademilade Shodipe-dosunmu:** What I'm going to do is that I'm going to record a loom showing you how to upload articles to Optimize.ly this week.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So when I'm uploading, when I'm submitting articles this week, I'll show you how it's done.

**Ademilade Shodipe-dosunmu:** And I'll show you what all of these things mean and what you need to fill out and just best practices.

**Ademilade Shodipe-dosunmu:** There's already, like, an intro video there by John from the Diligent team.

**Ademilade Shodipe-dosunmu:** However, if you're not familiar with, like, content management systems or platforms, like, it might be a bit harder to understand what he meant in the video.

**Ademilade Shodipe-dosunmu:** So I'll just record a new one doing, like, a step-by-step breakdown of, like, what you need to know and what you need to do every week.

**Ademilade Shodipe-dosunmu:** Also, like I mentioned, if you can see here in the, in the...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** You can find this here.

**Ademilade Shodipe-dosunmu:** This is the weekly recurring tasks.

**Ademilade Shodipe-dosunmu:** So you sort of know what you're supposed to do every day.

**Ademilade Shodipe-dosunmu:** This might change.

**Ademilade Shodipe-dosunmu:** I think you guys have something in Notion or something right now.

**Ademilade Shodipe-dosunmu:** But like this can map to that.

**Ademilade Shodipe-dosunmu:** just so you remember that, oh, okay, on Monday, you're supposed to update Looker or you're supposed to do this and all of that for all your accounts.

**Ademilade Shodipe-dosunmu:** So like it's here if you need it.

**Ademilade Shodipe-dosunmu:** So just wanted to flag that.

**Ademilade Shodipe-dosunmu:** So for Optimizely, I'll record a loom.

**Ademilade Shodipe-dosunmu:** For Publish it, it's really simple.

**Ademilade Shodipe-dosunmu:** You can check the general channel for the templates.

**Ademilade Shodipe-dosunmu:** I sent one to...

**Ademilade Shodipe-dosunmu:** So I'm on today.

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** Where is it?

**Pamela Weber:** So am I publishing from Optimizely, these articles?

**Pamela Weber:** Or just putting them in there?

**Ademilade Shodipe-dosunmu:** You submit to Optimizely.

**Ademilade Shodipe-dosunmu:** So once you submit, then I would like explain it during the video, but like there are like different steps.

**Ademilade Shodipe-dosunmu:** like once you create...

**Ademilade Shodipe-dosunmu:** You mark it as created, you fill in the fields, mark this.

**Ademilade Shodipe-dosunmu:** Then the content team has to review on their side, so they will give you feedback, you work on the feedback, and the SEO team will review.

**Ademilade Shodipe-dosunmu:** They will give you feedback as well, you work on the feedback.

**Ademilade Shodipe-dosunmu:** Then afterwards, you mark revisions as done.

**Ademilade Shodipe-dosunmu:** Most of them don't have legal review.

**Ademilade Shodipe-dosunmu:** You mark revisions as done.

**Ademilade Shodipe-dosunmu:** Once revisions are done, you can now send it to Sloaban to publish.

**Ademilade Shodipe-dosunmu:** So after he publishes, you now have to come back into Optimizely and mark it as publish blog completed.

**Ademilade Shodipe-dosunmu:** So I've got a loom explaining this, but yeah.

**Ademilade Shodipe-dosunmu:** Then for publishing, this is the ticket format.

**Ademilade Shodipe-dosunmu:** You can just check the internal channel.

**Ademilade Shodipe-dosunmu:** It's not anything too crazy.

**Ademilade Shodipe-dosunmu:** Just literally all you need to send to Sloaban is think two things.

**Ademilade Shodipe-dosunmu:** So I'm trying to think of what he needs.

**Ademilade Shodipe-dosunmu:** Because linear is still opening.

**Ademilade Shodipe-dosunmu:** I don't what on earth is making.

**Ademilade Shodipe-dosunmu:** And what day is all this stuff to do?

**Ademilade Shodipe-dosunmu:** What day is that?

**Ademilade Shodipe-dosunmu:** Is everything to do?

**Pamela Weber:** To be in Optimizely and then to be published.

**Pamela Weber:** What are the days?

**Ademilade Shodipe-dosunmu:** It's not like days.

**Ademilade Shodipe-dosunmu:** just have to get it done before the end of the week.

**Ademilade Shodipe-dosunmu:** since Sulaiman has to publish, ideally, you should be done with contents for diligent by Thursday, later, student review.

**Ademilade Shodipe-dosunmu:** And because it's not like discern where as soon as you are done, we publish, no, they review.

**Ademilade Shodipe-dosunmu:** Discern is because essentially we have built a lot of trust with him and he doesn't review.

**Ademilade Shodipe-dosunmu:** He only reviews the first article in each cluster, then we build it out.

**Ademilade Shodipe-dosunmu:** So there's a lot of trust that he doesn't review.

**Ademilade Shodipe-dosunmu:** So with discern, we can finish publishing, can finish expressing articles on Friday or Thursday and publish it that same day like a friend, no problem.

**Ademilade Shodipe-dosunmu:** But this is different.

**Ademilade Shodipe-dosunmu:** They have an entire review process, just like your call.

**Ademilade Shodipe-dosunmu:** So by Thursday, you should be done and you put it on Optimizely.

**Ademilade Shodipe-dosunmu:** Thursday, they would most likely review it the following Monday or Friday, the same Friday, but they most likely review the following Monday.

**Ademilade Shodipe-dosunmu:** So once they review the following Monday, you work on the feedback.

**Ademilade Shodipe-dosunmu:** I usually work on the feedback that same Monday or Tuesday when they review it, then send it for publishing on Tuesday the next week.

**Ademilade Shodipe-dosunmu:** So sometimes we're like a week behind, but like after a while, like we sort of, we catch up after a while.

**Ademilade Shodipe-dosunmu:** But right now we have like, I think they have like five askles in their backlog that are not reviewed.

**Ademilade Shodipe-dosunmu:** But at the end of this week, we're going to send another five.

**Ademilade Shodipe-dosunmu:** Or more.

**Ademilade Shodipe-dosunmu:** So they're going to have like a backlog of askles to review.

**Ademilade Shodipe-dosunmu:** So usually by the time you're publishing an article, like by the time that you're working on articles for a current week, you'll be receiving articles from the previous week, which are due for publishing that week.

**Ademilade Shodipe-dosunmu:** If that makes sense.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** So they're behind on publishing.

**Pamela Weber:** We're not behind.

**Pamela Weber:** They're, we're sending it.

**Pamela Weber:** Yeah.

**Pamela Weber:** They're going be in like.

**Pamela Weber:** That's actually good.

**Pamela Weber:** That helps with me because I'm learning all this.

**Pamela Weber:** Because she originally, your call was Wednesday and then Tuesday and now it's Monday.

**Pamela Weber:** So it's like, swimming up.

**Pamela Weber:** Pretty soon it'll be this this this weekend.

**Pamela Weber:** Yeah, Yoko is a pretty weird one.

**Ademilade Shodipe-dosunmu:** Ideally, it should be Tuesday or Wednesday.

**Ademilade Shodipe-dosunmu:** That's how we always used to do it.

**Ademilade Shodipe-dosunmu:** It's okay.

**Pamela Weber:** I'll get it today.

**Pamela Weber:** okay, go ahead.

**Ademilade Shodipe-dosunmu:** For the tickets, it's pretty much...

**Ademilade Shodipe-dosunmu:** Oh, dang, what is it?

**Ademilade Shodipe-dosunmu:** Oh, okay.

**Ademilade Shodipe-dosunmu:** Let's just go for a random one.

**Ademilade Shodipe-dosunmu:** So this is typically what you need in the ticket.

**Ademilade Shodipe-dosunmu:** Just, hey, we need your help.

**Ademilade Shodipe-dosunmu:** Obviously, this refreshes.

**Ademilade Shodipe-dosunmu:** You can grab one of the tickets from the internet or just check.

**Ademilade Shodipe-dosunmu:** I send one every week.

**Ademilade Shodipe-dosunmu:** So it shouldn't be hard to find one.

**Ademilade Shodipe-dosunmu:** That's this informant.

**Ademilade Shodipe-dosunmu:** Just send him the links to the documents.

**Ademilade Shodipe-dosunmu:** Then if it's a refresh, send him the live links.

**Ademilade Shodipe-dosunmu:** If it's a net new, obviously, there's no live link for a net new.

**Ademilade Shodipe-dosunmu:** So if it's a net new, you don't need to send a link for that.

**Ademilade Shodipe-dosunmu:** That's pretty much it.

**Ademilade Shodipe-dosunmu:** From there, he knows what to do.

**Ademilade Shodipe-dosunmu:** I've already defined the process before.

**Ademilade Shodipe-dosunmu:** There's like a longer document showing him everything he needs to do in sanity and all of that.

**Ademilade Shodipe-dosunmu:** So from there, you're good.

**Ademilade Shodipe-dosunmu:** For refreshes, the article link will be live since it already exists.

**Ademilade Shodipe-dosunmu:** That's the process for Diligent production-wise, pipeline-wise, and Airtable-wise. For Optimizely submission, that's complex enough that I'll send you a Loom tutorial this week rather than explain it here. Then you can attempt your first submission and we'll do a trial run.

**Ademilade Shodipe-dosunmu:** For the four articles I've assigned you, can you get at least one to me by Thursday? You don't have to send them all at once—if you're back Wednesday, send one and I'll give you feedback to apply to the others.

**Ademilade Shodipe-dosunmu:** One thing about Diligent: they have about 20 products, which is a learning curve. But I've mapped the product feature matrix to the pipeline, so it should suggest the right products to mention. There's also a polishing step that will flag product-related issues.

**Pamela Weber:** How do I know when I need to create a new pipeline? Is it like Descern where you need one per cluster, or does one pipeline work across all topics here?

**Ademilade Shodipe-dosunmu:** Descern needs multiple pipelines because each cluster has a different template. Diligent is different—the governance content isn't templated the same way, so one pipeline should handle all topics.

**Pamela Weber:** Got it, thanks.

**Ademilade Shodipe-dosunmu:** I'll add an updated editorial checklist tomorrow morning so it makes the post-processing easier. The idea is to reduce friction on a complicated account with lots of context and products. It took me a while to learn Diligent's products, but you'll get used to them as you work through articles. I started with this account from the beginning when they joined, so I had the luxury of learning gradually. You'll get context as we work together.

**Ademilade Shodipe-dosunmu:** Just make sure you do your diligence and verify everything—links, content, accuracy. This is governance content, which is the most sensitive field we work in. Enterprise decision-makers base major decisions on articles like these. Laws, regulations, legality—everything has to be accurate. The accuracy and quality bar is very high.

**Ademilade Shodipe-dosunmu:** Looking at this sample, there's an issue where the intro got merged with the section below. You'll want to ask Claude to separate those. But overall, the pipeline does a good job.

**Ademilade Shodipe-dosunmu:** Let me know if you have questions as we go.

**Ademilade Shodipe-dosunmu:** For pipeline inputs, just use the templates provided. Overview, client website, target keyword—it's all pre-populated. Primary keyword, title, goal, word count—adjust based on the topic.

**Ademilade Shodipe-dosunmu:** For topics to cover, I use Perplexity to search what's ranking, then use Perplexity and Claude to create an outline. Then I edit and remove anything unnecessary, paste it in, run the pipeline, and make final adjustments. Last week the pipeline worked well—I spent about 25-30 minutes per article, which is reasonable for this type of content since it requires fine-tuning. As you get familiar with the account, it should take less time.

**Ademilade Shodipe-dosunmu:** I'll send you Loom tutorials for Optimizely and other tasks. Let me know if you have questions.

**Ademilade Shodipe-dosunmu:** No, I haven't done that.

**Pamela Weber:** Oh, okay.

**Pamela Weber:** That's great.

**Pamela Weber:** I need to go look at that video again, yeah.

**Ademilade Shodipe-dosunmu:** So ideally, you're supposed to update Luca every Monday because, it's important because the performance data that our engagement managers present to the clients during the weekly meeting.

**Ademilade Shodipe-dosunmu:** It's based off of like adding those data sources to Looker.

**Ademilade Shodipe-dosunmu:** So if Looker is not updated, then they are not going to be reporting accurate data.

**Ademilade Shodipe-dosunmu:** So if you would likely have to do that, like, retroactively for Descend, Yerko as well, and Diligent.

**Ademilade Shodipe-dosunmu:** I've updated this week for Diligent, but like for Descend and Yerko, like, for the weeks that you have been unable to do those, you have to update Looker, if not like, you know.

**Ademilade Shodipe-dosunmu:** Yeah, so like, this was the video, the video gives you an example of how to do it.

**Ademilade Shodipe-dosunmu:** I would probably record another video on like how to do it for Diligent.

**Ademilade Shodipe-dosunmu:** It's the same process everywhere, like just some accounts are just a bit like weirder.

**Ademilade Shodipe-dosunmu:** And like, I already created this like, this is Claude B, I mean Claude B Pod, like I have a project for Looker here.

**Ademilade Shodipe-dosunmu:** So I could just drop the links and the, yeah, pretty much I did this one for Crestal, all you need is the link and the clip.

**Ademilade Shodipe-dosunmu:** Literally, just pasted the link and the clusters that I needed, and it just converts it automatically to the desired format.

**Ademilade Shodipe-dosunmu:** And I can just copy these and paste it in Looker.

**Ademilade Shodipe-dosunmu:** Like, it's so simple, especially because you have this cloud project.

**Ademilade Shodipe-dosunmu:** already, like, wired it to deliver what you need.

**Ademilade Shodipe-dosunmu:** So, yeah, I'll go there.

**Ademilade Shodipe-dosunmu:** I will, since I've already updated Looker this week for DHS, don't need to worry about that.

**Ademilade Shodipe-dosunmu:** But from next week, you're owning that.

**Ademilade Shodipe-dosunmu:** But I will, I will go ahead and I'll still record a loom on how to do this for DHS, but I already recorded one for Yurko, and, like, you can apply the same basically to the same, so you should be fine.

**Ademilade Shodipe-dosunmu:** The only problem that will happen is when you reach 200 URLs in the Looker dashboard, so once you reach 200 URLs, you have to create another cohort and, like, do some stuff.

**Ademilade Shodipe-dosunmu:** So, anytime you reach 200 URLs, can probably flag to me or Carrie, and...

**Ademilade Shodipe-dosunmu:** Like, we'll walk you through the process on what you need to do in that situation.

**Ademilade Shodipe-dosunmu:** But, yeah, carry those out to date, and I do as well.

**Ademilade Shodipe-dosunmu:** So, whichever one of us is available, you can just reach out, and we'll let you know.

**Ademilade Shodipe-dosunmu:** I think that is it, honestly.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah, just, like, point of action would be for you to really need to update those local dashes for, like, the previous weeks that you missed.

**Ademilade Shodipe-dosunmu:** And I'll record a loom for Optimizely, for, this is already, I've already given you a pipeline walkthrough, so you don't need that anymore.

**Ademilade Shodipe-dosunmu:** I'll record a loom for Optimizely, for Looker, and for any other, like, weird, random tasks that they usually ask for, but I think it should be.

**Ademilade Shodipe-dosunmu:** That should be it.

**Ademilade Shodipe-dosunmu:** So, I'll try and record those looms tomorrow, if I get a bit of time.

**Ademilade Shodipe-dosunmu:** I can just block out 30 minutes to record all the looms.

**Ademilade Shodipe-dosunmu:** Or maybe later in the week, because it makes more sense to record the looms, and I'm actually doing this stuff, you know.

**Ademilade Shodipe-dosunmu:** But, yeah.

**Ademilade Shodipe-dosunmu:** I'll do that, and I would let you know.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, that's pretty much it.

**Ademilade Shodipe-dosunmu:** So, yeah, if you can send me an article on Thursday, that would be great.

**Ademilade Shodipe-dosunmu:** At least one, so I can review it, and you can, like, work on the others.

**Ademilade Shodipe-dosunmu:** And because the articles you're working on this week are to be published next, to be sent to the client next week.

**Ademilade Shodipe-dosunmu:** But this week's content itself, me and Timmy are working on it, you know, just so that you have, like, a week of breathing space, similarly to what we use for discern and your code.

**Pamela Weber:** Thanks, I really appreciate this.

**Ademilade Shodipe-dosunmu:** No problem. If you need anything about Diligent, let me know. You'll probably have lots of questions starting out—there's a lot to learn with all the products and context. But most of the information is in Claude, so you can ask it about Diligent products, what each product does, and get answers quickly since the data is up to date.

**Ademilade Shodipe-dosunmu:** Vivek or Carrie will also share product updates and repositioning changes as they happen, so you'll know when to update the feature matrix and related artifacts.

**Ademilade Shodipe-dosunmu:** That's pretty much it. Any questions before we wrap?

**Pamela Weber:** I think we covered everything. Thanks so much for your help.

**Ademilade Shodipe-dosunmu:** Perfect. I'll send the recording to Carrie. Just ping me if you have any issues as you get started.

**Pamela Weber:** Will do. Thanks again!

**Ademilade Shodipe-dosunmu:** Good luck!
