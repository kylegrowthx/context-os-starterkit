# Client Onboarding w

<metadata>
date: 2025-12-23
time: 20:03 UTC
duration: 44 minutes
organizer: ademilade@growthx.ai
participants: Ademilade Shodipe-dosunmu, Pamela Weber
fathom_recording_id: 110739858
fathom_url: https://fathom.video/calls/515828849
share_url: https://fathom.video/share/6pK1oW1mPavP8AsnogVuXrqtdgNGVLo1
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Ademilade walked Pamela through GrowthX's three key content clients to prepare her for delivery work: DisCern (legal compliance, 26 PSU articles/week), Diligent (governance platform, 5-7 editorial articles/week), and Yurko (content with a difficult POC, 6 articles/week). The team reviewed each client's production volume, pipeline status, and key workflow challenges—particularly DisCern's internal linking issues, Diligent's dual-platform admin burden, and Yurko's time-intensive Prismic CMS process. Pamela will focus on context and learning this week, with Ademilade prepping content for January 5th launch and Pamela's first batch due January 12th, followed by a live walkthrough of key tools next Monday.

---

## Context

Pamela Weber just joined GrowthX's delivery team as an editor and is being onboarded across three major content clients. This meeting is the theory-level orientation—an overview of each client's business, content strategy, and operational challenges. The detailed workflows and tool-specific training will happen in dedicated sessions: Ademilade planned a Monday 1:1 on Lookout/Looker, Optimizely, Airtable, and DisCern templates, plus separate onboarding calls for Yurko and a 30-minute Airtable/Content OS walkthrough. Ademilade has been managing these clients for the past few months and has built strong relationships with them (particularly DisCern, where his prior experience with a competitor gave him early credibility). The onboarding timeline is compressed: Pamela starts context learning this week, Ademilade preps launch content for January 5th, and Pamela's first delivery batch is due January 12th.

---

## Relevance

- **To GrowthX Delivery:** Scaling delivery requires clear onboarding of new editors to high-volume clients. The bottlenecks identified—DisCern's poor internal linking, Diligent's dual-platform admin overhead, and Yurko's Prismic CMS manual labor—are systemic constraints that will impact Pamela's productivity and need future automation investment.

- **To GrowthX Operational Efficiency:** The pipeline architecture varies by client (programmatic PSU for DisCern, Atlas-based editorial for Diligent, manual for Yurko). Standardizing and automating where possible (e.g., Diligent migration to Atlas, Yurko Prismic automation) is critical as the team scales.

- **To Account Health:** All three clients appear healthy and producing on schedule. DisCern has a 612-topic buffer (26 articles/week), Diligent has 52 topics queued (5-7 articles/week), and Yurko is at 6 articles/week. No churn risk signals noted in this conversation.

---

## Overview

- **Production Volume:** DisCern (26 PSU articles/wk) and Diligent (5–7 editorial articles/wk) have large backlogs (600+ and 52+ topics, respectively), ensuring a steady workflow.
- **Pipeline Status:** DisCern's PSU pipeline is mature, requiring only fact-checking and internal linking edits. Diligent's pipeline is being built in Atlas to replace a manual Claude process.
- **Key Challenges:** DisCern's pipeline has poor internal linking. Diligent's workflow requires manual status updates in both Airtable and Optimizely, plus a separate refresh report. Yurko's Prismic CMS is a major time sink, requiring manual copy-pasting.
- **Onboarding Plan:** Pamela will focus on context this week. Ademilade will prep content for the week of Jan 5th, with Pamela's first batch due Jan 12th. A live walkthrough of key workflows is scheduled for next Monday.

---

## Key Topics

### DisCern: High-Volume Programmatic Content

  - **Client:** Legal compliance automation (registered agent, formation services).
  - **Content Strategy:** Programmatic SEO (PSU) using templates in Atlas.
      - **Rationale:** High upfront template investment (\~3 hrs) enables rapid, low-effort article generation (\~10–15 mins each).
      - **Workflow:** Create template → Load in Atlas → Generate articles.
      - **Review:** Client POC (Mike) reviews only the first article in each new cluster to ensure alignment.
  - **Current Focus:** "Competitor Comparisons" cluster.
      - **Types:** "Best X Alternatives," "DisCern vs. Y," "Best X for Z."
      - **Status:** Template for "Best X Alternatives" is approved.
  - **Key Challenges:**
      - **Internal Linking:** The pipeline's weakest point; often creates non-contextual or broken links.
      - **Images:** Pipeline-generated images are low quality; Ademilade will investigate fixes.
      - **Publishing:** Currently manual (via Slama). The NG team is developing an automated pipeline to fix a Webflow bug that previously broke tables.
  - **Production:** 26 PSU articles/week.
      - **Rationale:** One extra article/week is being produced to catch up on a slow start.
      - **Buffer:** 612 "Approved for creation" topics in Airtable.
  - **Refreshes:** Manual process (10–15 mins/article) to fact-check dates, fees, and links (which often break on government sites).

### Diligent: Global Governance Platform

  - **Client:** AI-enabled governance platform for global enterprises.
      - **Key Consideration:** Content must serve a worldwide audience, not just the U.S.
  - **Content Strategy:** Primarily refreshes (75%) with some net-new content.
      - **Refresh Focus:** Update positioning to emphasize AI services and add original research from the Claude project.
  - **Pipeline Status:** Currently being built in Atlas.
      - **Rationale:** Replaces a manual Claude process that generates a full article in \~30 mins.
  - **Production:** 5–7 editorial articles/week.
      - **Rationale:** Producing extra articles creates a buffer for Diligent's slow review process.
      - **Buffer:** 52 "Approved to start" topics in Airtable.
  - **Key Challenges:**
      - **Dual Platform Admin:** Requires manual status updates in both Airtable and Diligent's Optimizely CMS.
      - **Multi-Team Review:** Content is reviewed by separate, non-aligned Content and SEO teams, which slows the process.
      - **Refresh Reports:** A separate report detailing changes is required for each refreshed article, generated by a prompt.

### Yurko: High-Effort, Lower-Value Client

  - **Client:** Content is straightforward, but the POC is difficult and prone to scope creep.
  - **Production:** 6 articles/week.
  - **Key Challenge:** The Prismic CMS is a major time sink.
      - **Process:** Requires manual copy-pasting of content into individual "slices" (e.g., one slice per H2).
      - **Time:** Staging one article takes 10–15 minutes.
      - **Rationale:** Engineering has not prioritized automation due to Prismic's custom nature and limited client usage.

---

## Action Items

**Ademilade Shodipe-dosunmu (GrowthX)**
- Improve DisCern image pipeline; share updates w/ Pamela
- Prep Jan 5 publish-ready content for DisCern, Diligent, Yurko
- Assign 2 articles/client to Pamela; then schedule live edit session
- Apply entity-agency channel linking to DisCern pipelines; update Pamela
- Migrate Diligent pipeline to Atlas; update Pamela
- Schedule Mon 1:1 w/ Pamela re: Lookout/Looker, Optimizely, Airtable, DisCern templates
- Schedule separate Yurko onboarding call w/ Pamela
- Schedule 30-min Airtable/Content OS walkthrough w/ Pamela

**Pamela Weber (GrowthX)**
- Review DisCern competitor-comparison articles; finalize by Jan 12

---

## Transcript
**Ademilade Shodipe-dosunmu:** So I'm going to be onboarding you on, I think, three clients.

**Ademilade Shodipe-dosunmu:** It won't all be on this call.

**Ademilade Shodipe-dosunmu:** This call is more of like a, let's just walk through, like, just like a quick theory of what each of them are about.

**Ademilade Shodipe-dosunmu:** Like the more detailed stuff is in the documentation already.

**Ademilade Shodipe-dosunmu:** Then I also want to give you status updates on what's going on with each client so that you have a bit more context into how things are going.

**Ademilade Shodipe-dosunmu:** So I'm going just share my screen real quick and we can get started.

**Ademilade Shodipe-dosunmu:** Okay, let's start that one.

**Ademilade Shodipe-dosunmu:** You can see my screen?

**Ademilade Shodipe-dosunmu:** Yeah.

**Pamela Weber:** All right, perfect.

**Ademilade Shodipe-dosunmu:** We'll just start with discern because, like, I think it's the easier.

**Ademilade Shodipe-dosunmu:** I don't know all the clients you can get.

**Ademilade Shodipe-dosunmu:** It's probably the most straightforward.

**Ademilade Shodipe-dosunmu:** The sentence, please.

**Ademilade Shodipe-dosunmu:** Each year, we have a really good relationship with them.

**Ademilade Shodipe-dosunmu:** built a ton of trust over the last couple of months.

**Ademilade Shodipe-dosunmu:** Context there is that I worked for one of their major competitors last year for a while, almost like a year, actually, before I came to GoFx.

**Ademilade Shodipe-dosunmu:** It was like a weird coincidence that I was assigned to the same account.

**Ademilade Shodipe-dosunmu:** It was like, oh, okay, yeah, yeah, I know what we want to do here.

**Ademilade Shodipe-dosunmu:** So it was really good.

**Ademilade Shodipe-dosunmu:** So that has also helped, like, lots of trust with the client.

**Ademilade Shodipe-dosunmu:** So what they do was pretty much like a full-on automation service for legal compliance.

**Ademilade Shodipe-dosunmu:** So for registered agent services, for formation services, and stuff like that.

**Ademilade Shodipe-dosunmu:** You have links to, like, air table and all of that, so you should leave it there.

**Ademilade Shodipe-dosunmu:** So the major thing moving forward is that this client is mostly programmatic.

**Ademilade Shodipe-dosunmu:** So it's PSCO content, which pretty much...

**Ademilade Shodipe-dosunmu:** Which means that it's a template for each cluster.

**Ademilade Shodipe-dosunmu:** So the idea behind it is that you probably spend a lot of time working on the template.

**Ademilade Shodipe-dosunmu:** I personally can spend like three hours working on the template for the cluster, but like those three hours of time can help us spend maybe like 10 to 15 minutes per hour over the course of three weeks.

**Ademilade Shodipe-dosunmu:** So it's like a worthy investment along the line.

**Ademilade Shodipe-dosunmu:** So that's like the flow for this.

**Ademilade Shodipe-dosunmu:** So it's more like any time we get to a new cluster, we design a template for it, we load it up in Atlas, and I can walk you through how this is done on like a separate call.

**Ademilade Shodipe-dosunmu:** And load up in Atlas and we create an article for the client based off of that.

**Ademilade Shodipe-dosunmu:** And after we create an article for the client on that cluster, we send it to the client for review.

**Ademilade Shodipe-dosunmu:** So he, that's Mike, our POC, usually only reviews the first article in a new cluster, just to make sure we're aligned.

**Ademilade Shodipe-dosunmu:** And from this, that comes off.

**Ademilade Shodipe-dosunmu:** Pretty much for the entire cluster.

**Ademilade Shodipe-dosunmu:** So that's like the cadence, that's the flow.

**Ademilade Shodipe-dosunmu:** So this is what, pipelines can be crazy because we have done like a ton of clusters already.

**Ademilade Shodipe-dosunmu:** So we've done an annual report, articles, firmware, address, agent, financial stacks, formation, formation of course, right, in office.

**Ademilade Shodipe-dosunmu:** We're currently, the last one we did was NC Information, and we're currently on headstop comparisons.

**Ademilade Shodipe-dosunmu:** I have already gone ahead to load up the first, some articles that you'll be working on probably in like your second week of January.

**Ademilade Shodipe-dosunmu:** These articles should be finalized by the second week of January, actually.

**Ademilade Shodipe-dosunmu:** But I've already loaded up, I've already created the templates for this particular cluster.

**Ademilade Shodipe-dosunmu:** So only option needed from you here would be to actually edit the content that comes out of the pipeline.

**Ademilade Shodipe-dosunmu:** And so around here, this is where like the fact-checking stuff.

**Ademilade Shodipe-dosunmu:** And the internal linking, because that's one of the major problems with this pipeline, internal linking is always great.

**Ademilade Shodipe-dosunmu:** Sometimes it does a good job, but sometimes it's absolutely crappy, but yeah, you know, this is not contextual.

**Ademilade Shodipe-dosunmu:** This, you know, I'm saying for registration support, and it's taking me to a page on Connecticut instead of like a general page.

**Ademilade Shodipe-dosunmu:** So, yeah.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Um, I'm trying to, trying to remember.

**Pamela Weber:** that's live on their website, the link you were at, that's live already?

**Pamela Weber:** Yeah, yeah.

**Ademilade Shodipe-dosunmu:** Oh, their capitalization's all wrong.

**Pamela Weber:** That's not lazy.

**Ademilade Shodipe-dosunmu:** Go ahead.

**Ademilade Shodipe-dosunmu:** It's like.

**Pamela Weber:** Why did they like, oh, their sentence case.

**Pamela Weber:** That's what they're doing with their headers?

**Pamela Weber:** Yeah, they us.

**Ademilade Shodipe-dosunmu:** Fine.

**Ademilade Shodipe-dosunmu:** Okay.

**Pamela Weber:** It just drives me nuts or whatever.

**Pamela Weber:** Okay, I'll get it.

**Ademilade Shodipe-dosunmu:** Yeah, I'll get it.

**Ademilade Shodipe-dosunmu:** I think for, I think all of them.

**Ademilade Shodipe-dosunmu:** Okay, so the only one that exists has a page.

**Ademilade Shodipe-dosunmu:** The only issue right now with this pipeline is probably the images, they're not like terrible or immutable, I want to like give these a second.

**Ademilade Shodipe-dosunmu:** So like I'm back in office next week and I would like to dive in to see how I can make these images a bit better for your own flows.

**Ademilade Shodipe-dosunmu:** And we could do like a ton of like walkthroughs next week.

**Ademilade Shodipe-dosunmu:** Like I think I would want you to focus this week more on like getting like necessary context.

**Ademilade Shodipe-dosunmu:** So like what I was trying to avoid and like the reason I was like I'm out of office now and I said hey but like I just had to like chat to you this week because if I come in on January 5th and I'm dumping all of these on you, it's going to be like a shitstorm, excuse my French.

**Ademilade Shodipe-dosunmu:** So I just wanted to be as smooth as possible and easy as possible for you.

**Ademilade Shodipe-dosunmu:** So Yeah.

**Ademilade Shodipe-dosunmu:** I'm going ahead to make sure that for all the client work that's needed, the week of January 5th, you would have content ready for that week, like content ready to publish that week.

**Ademilade Shodipe-dosunmu:** So I'll go ahead and make sure that there's content already for that week so that your first batch of content will be due the week of January 12th, if that makes sense.

**Ademilade Shodipe-dosunmu:** Yep, so I'll probably take some time next week to make sure you have articles ready to publish and all of that and work into the flows.

**Ademilade Shodipe-dosunmu:** Some important things to note, because like context switching gets pretty crazy with these clients.

**Ademilade Shodipe-dosunmu:** If you go into the internal channels for diligence, discern, and miracle, you would see that I have like a weekly checklist or recurring tasks for clients.

**Ademilade Shodipe-dosunmu:** For all of them, so you can modify this to your needs, but this was mine, pretty much the stuff I had to do for them every single day.

**Ademilade Shodipe-dosunmu:** Mm-hmm.

**Ademilade Shodipe-dosunmu:** You can modify this if stuff changes and all, but this gives you like a fair read of like what you're supposed to do that day, and you'll be able to, so that you just don't keep everything in your head, because context switching is actually crazy, it's favorite client, right, so, and I have for all of the clients, so it's like a weekly one for Yurko, and I just pretty much tick them when I'm done, and, you know, it starts again next Okay, that's, that's super cool.

**Pamela Weber:** Am I on that thread in Slack?

**Pamela Weber:** Maybe it is, I just didn't see it.

**Ademilade Shodipe-dosunmu:** Uh, yeah, I'll add you to like the internal channels, like, this is awesome, okay, thank you.

**Ademilade Shodipe-dosunmu:** Let me just add you for a quick, um, so this is Yurko, you know, just go ahead and add you.

**Pamela Weber:** And if, is there one, like, if I check off, will everybody see that, or it's like a list that I can use, you know what I mean?

**Pamela Weber:** Oh, it's, it looks like you've got, it's internal, it's internal facing, so you're good.

**Ademilade Shodipe-dosunmu:** Okay, okay.

**Ademilade Shodipe-dosunmu:** It's for you, like, it's pretty much for you, yeah.

**Ademilade Shodipe-dosunmu:** So good on that.

**Ademilade Shodipe-dosunmu:** I'm going to try to do it.

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** I'm going try you're going to So Okay.

**Ademilade Shodipe-dosunmu:** It's

**Ademilade Shodipe-dosunmu:** Great.

**Ademilade Shodipe-dosunmu:** Let's it to that.

**Ademilade Shodipe-dosunmu:** Let me add you to discern.

**Ademilade Shodipe-dosunmu:** Add you to diligence.

**Ademilade Shodipe-dosunmu:** I think I'm going to go ahead and add you to the external channels as well because Okay.

**Ademilade Shodipe-dosunmu:** I'll go ahead and add external channels as well.

**Ademilade Shodipe-dosunmu:** Sometimes I get a new client, I like to be a little stalking by everything like messages to get some more context on what the hell is going on.

**Ademilade Shodipe-dosunmu:** Well, that's fully up to you if you have time to do that.

**Ademilade Shodipe-dosunmu:** All right.

**Ademilade Shodipe-dosunmu:** Perfect.

**Ademilade Shodipe-dosunmu:** So we have these set up.

**Ademilade Shodipe-dosunmu:** So you added...

**Ademilade Shodipe-dosunmu:** So yeah, like I said, first week of content will be done for all clients, so just give me a bit more profit.

**Ademilade Shodipe-dosunmu:** So this week I want you to pretty much focus on getting the necessary context, and I'm sure you're going to be off a couple of days this week.

**Ademilade Shodipe-dosunmu:** Is that correct?

**Ademilade Shodipe-dosunmu:** I didn't see anything on your calendar, so I said I was going to ask you, are you working this week or you're taking some time off?

**Pamela Weber:** Well, I'll be around, except obviously for Christmas and part of Christmas Eve, but yeah, the rest, I'm going to be here, what is it, Friday, Thursday, I guess?

**Pamela Weber:** Or is it the opposite?

**Pamela Weber:** Yeah, yeah, I'll be around a few days.

**Ademilade Shodipe-dosunmu:** Okay, okay, all good.

**Ademilade Shodipe-dosunmu:** All right, great.

**Ademilade Shodipe-dosunmu:** So pretty much we have like a content, I have like a personal content planner for, I use it mainly for just around because it's 26.

**Ademilade Shodipe-dosunmu:** 26.

**Ademilade Shodipe-dosunmu:** PSU articles every week, so...

**Ademilade Shodipe-dosunmu:** A lot, Ademilade Shodipe a bit crazy for that, so what's going to happen is that this week, like I said, you can get that necessary context.

**Ademilade Shodipe-dosunmu:** If you feel like you want to take this ad ad, working on any ad ad this week, just let me know, and I will, you know, get you around top and assign you, like, a couple of ads because I'm cross-step clients, but I feel like because of, like, holidays, probably Thursday and Friday, it might make more sense for you to just focus on getting the necessary context and then compiling more questions.

**Ademilade Shodipe-dosunmu:** Then next week, I can get you assigned a couple of ads for us or clients, and let's see how that works.

**Ademilade Shodipe-dosunmu:** So maybe two for each client, so two discerns, two miracles, and two diligence, then we see how that goes.

**Ademilade Shodipe-dosunmu:** Then maybe I could edit some of those live on, like, a call, like, a one-on-one, I think you might find that useful.

**Ademilade Shodipe-dosunmu:** Or if prefer async, I can do that async as well.

**Ademilade Shodipe-dosunmu:** So anyone that works with you, really, really.

**Ademilade Shodipe-dosunmu:** But yeah, most of the details are on the definition that I sent, but yeah, when we come back, pretty much starting with these competitor comparisons, I have set up a pipeline for, I think these competitor comparisons have three different types.

**Ademilade Shodipe-dosunmu:** So there are the best company alternatives, that's one.

**Ademilade Shodipe-dosunmu:** There are the this versus this, like the CERN versus XYZ, and there are the best target audience use case service for XYZ.

**Ademilade Shodipe-dosunmu:** best registered agent services for X type of company.

**Ademilade Shodipe-dosunmu:** Yeah, so I've made the template for the first type, and that has been approved.

**Ademilade Shodipe-dosunmu:** And based off of that, I can easily modify the page for the others, but I can do this with you live on it.

**Ademilade Shodipe-dosunmu:** I think it might be better, like, just to understand, like, how, the reasoning behind it, like, how I think about, like, creating these templates, and just, like, the rationale of everything.

**Ademilade Shodipe-dosunmu:** I think this will serve you well, moving, like, long term.

**Ademilade Shodipe-dosunmu:** So yeah, typical flow for this is we don't publish for the CERN.

**Ademilade Shodipe-dosunmu:** It's already in the opposite manner.

**Ademilade Shodipe-dosunmu:** We publish for them, but like, Slama publishes, so just send it to him to publish.

**Ademilade Shodipe-dosunmu:** However, the NG team is working on publishing automation for the CERN.

**Ademilade Shodipe-dosunmu:** They tried it before, but like the tables used to get like really messed up.

**Ademilade Shodipe-dosunmu:** It was like a weird web flow bug where like, if you try to publish it automated with like our pipeline, like the table's just got upscattered and like, but like apparently they're working on it now, so I'll keep posting on how that works.

**Ademilade Shodipe-dosunmu:** But for now, you can assume that we can assign stuff to Slama, and like you have examples of this, like the ticket is recurring for the CERN.

**Ademilade Shodipe-dosunmu:** So you don't have to, you just have to remind him probably every Monday and say, oh, hey, you know, all of this is ready.

**Ademilade Shodipe-dosunmu:** For the CERN's Airtable, it's relatively straightforward.

**Ademilade Shodipe-dosunmu:** I have like a ton of views here.

**Ademilade Shodipe-dosunmu:** But the most important ones for you would be published articles for Lookout Updates.

**Ademilade Shodipe-dosunmu:** Just random, have you done a Lookout Update before?

**Pamela Weber:** Sorry?

**Ademilade Shodipe-dosunmu:** Have you done a Lookout Update?

**Ademilade Shodipe-dosunmu:** No.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** So I'll add that to the list of stuff that we're going to work through.

**Ademilade Shodipe-dosunmu:** So don't worry, Lookout Updates are super easy.

**Ademilade Shodipe-dosunmu:** I've set up a Cloud Project for all Lookout Updates.

**Ademilade Shodipe-dosunmu:** So all you have to do is literally paste in the link and the cluster, and it reformats it for you.

**Ademilade Shodipe-dosunmu:** And it takes like two minutes of your time, everybody, so we're good.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** I'm trying to...

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** We probably will do like a...

**Ademilade Shodipe-dosunmu:** I'm trying not to go too deep for each client, to be honest, because I'm just going to give you a little idea of everything.

**Ademilade Shodipe-dosunmu:** Then we can have like a deeper dive next week.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** you.

**Ademilade Shodipe-dosunmu:** So that's pretty much important for this.

**Ademilade Shodipe-dosunmu:** The current state of affairs is that the AdSchools here, these are all refreshes that I was working on.

**Ademilade Shodipe-dosunmu:** Refreshes, we do these manually because the pipeline is not at the stage where it's PSU, so like do refreshes with the pipelines a bit harder.

**Ademilade Shodipe-dosunmu:** I find that doing manually is fast.

**Ademilade Shodipe-dosunmu:** I can do a refresh in like 10 minutes or 15, based on the workflow that I have, but I could once be using AdLas for more of these, so I've been trying to iterate with the refresher flow to get to a good position, but for now, these refreshes are pretty much the manual, but they don't take a ton of time because we're pretty much just fact-checking dates, because these are annual reports, so sometimes regulations in the U.S.

**Ademilade Shodipe-dosunmu:** change and like, oh, hey, they did some general report might change, or your extensions might change, or the fee for filing might change, so pretty much just fact-checking all of those on an annual basis and just making sure the links are refreshed.

**Ademilade Shodipe-dosunmu:** But sometimes we link directly to the Secretary of State websites, and sometimes, because of the way government websites move data around, you can get a little 4-4s.

**Ademilade Shodipe-dosunmu:** So, you know, we have to get, like, replacements for those as well.

**Ademilade Shodipe-dosunmu:** it's just, like, it could be a lighter effort, but, like, I'll work into how it works as well.

**Pamela Weber:** I had a question, like, for column F, central publishing, and then G, is that, like, automated?

**Pamela Weber:** Like, it'll populate, or you have to enter that yourself?

**Pamela Weber:** Uh, I pretty much enter this myself.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, this isn't automated.

**Ademilade Shodipe-dosunmu:** So, typically, like, it's up to you.

**Ademilade Shodipe-dosunmu:** I would agree.

**Ademilade Shodipe-dosunmu:** I would probably just pass on a support-based plan.

**Ademilade Shodipe-dosunmu:** You can literally work on this client without having to use this content plan.

**Ademilade Shodipe-dosunmu:** I just prefer spreadsheets sometimes to Airtable, because Airtable sometimes drives me nuts.

**Ademilade Shodipe-dosunmu:** But, yeah, you can do it fully in Airtable.

**Ademilade Shodipe-dosunmu:** For example, for my other two clients, Diligent and Yoko, I don't use the spreadsheet at all.

**Ademilade Shodipe-dosunmu:** I manage everything in Airtable.

**Ademilade Shodipe-dosunmu:** But because this...

**Ademilade Shodipe-dosunmu:** So it's 26, it gets a bit fuzzy, but I have to have it on the spreadsheet to make sense of it all.

**Ademilade Shodipe-dosunmu:** that's why.

**Ademilade Shodipe-dosunmu:** Right.

**Ademilade Shodipe-dosunmu:** Another thing that I discussed with, I discussed with Panzer before, but like, probably they're going to set different expectations with regards like the amount of share volume of the PSU that we're doing.

**Ademilade Shodipe-dosunmu:** So this is actually a shootout.

**Ademilade Shodipe-dosunmu:** We can work out.

**Ademilade Shodipe-dosunmu:** Like, it's just, the pipelines are good.

**Ademilade Shodipe-dosunmu:** Like, the CSS pipelines are pretty good.

**Ademilade Shodipe-dosunmu:** And, you know, of pipeline exits, probably will spend like 15 minutes to 20 editing it once you get into a good proof.

**Ademilade Shodipe-dosunmu:** So it's not difficult.

**Ademilade Shodipe-dosunmu:** The pipeline gives good results.

**Ademilade Shodipe-dosunmu:** However, the share volume of articles is a bit daunting, you know, 26.

**Ademilade Shodipe-dosunmu:** So there is that.

**Ademilade Shodipe-dosunmu:** Even though it's PSU.

**Ademilade Shodipe-dosunmu:** So we're trying to, probably by the next renewal, we'll probably have to negotiate, like, deliverables, maybe sort of bringing that down a bit.

**Ademilade Shodipe-dosunmu:** Or if they want to retain this, they'll probably have to pay more or something.

**Ademilade Shodipe-dosunmu:** But that's down in any of these.

**Ademilade Shodipe-dosunmu:** So yeah, that pretty much covers it for discern, legal and compliant, so you really have to get your facts right.

**Ademilade Shodipe-dosunmu:** The most difficult part of this is the fact-checking, honestly.

**Ademilade Shodipe-dosunmu:** But once you get used to it, you get into that groove, and you can just tell when something is off, in terms of a date, a price, or something.

**Ademilade Shodipe-dosunmu:** And even if you miss a couple of stuff, don't sweat it too much, because that's why we have refreshes.

**Ademilade Shodipe-dosunmu:** Sometimes I still patch stuff, but I'm doing some housekeeping, I'm oh, hey, this is actually incorrect, and I fix it up and go up here.

**Ademilade Shodipe-dosunmu:** So that would happen, right?

**Ademilade Shodipe-dosunmu:** But the pipeline will make sure that, you know, that is a rarity rather than like a regularity.

**Ademilade Shodipe-dosunmu:** So you should be fine.

**Ademilade Shodipe-dosunmu:** That's mostly for discern.

**Ademilade Shodipe-dosunmu:** Next client.

**Ademilade Shodipe-dosunmu:** Okay, last thing is like the major issue with the discern pipeline is internal linking is not the best.

**Ademilade Shodipe-dosunmu:** So I'm going to bring the entity agency can channel linking flow next.

**Ademilade Shodipe-dosunmu:** And apply to these pipelines and see how it goes.

**Ademilade Shodipe-dosunmu:** I'll keep you posted on that.

**Ademilade Shodipe-dosunmu:** So like I'm in the middle of doing like some pipeline modifications across three clients, all of them.

**Ademilade Shodipe-dosunmu:** So I think you're coming at a pretty quick time because you need to use the best versions of these pipelines.

**Ademilade Shodipe-dosunmu:** lucky you.

**Ademilade Shodipe-dosunmu:** But yeah, I'll keep you posted on that.

**Ademilade Shodipe-dosunmu:** Just a tier there, discerns pipelines aren't agentic.

**Ademilade Shodipe-dosunmu:** The only agentic pipeline here is going to be under, if you go to editorial actually.

**Ademilade Shodipe-dosunmu:** So you're not editorial, have for net new analysis agency.

**Ademilade Shodipe-dosunmu:** But because we do mostly PSU and PSU relies on deterministic workflows, it's a bit harder to make or a bit less possible to make PSU agentic.

**Ademilade Shodipe-dosunmu:** You know what I mean?

**Ademilade Shodipe-dosunmu:** templated, right?

**Ademilade Shodipe-dosunmu:** There's no, it's pretty much telling the workflow, hey, this is exactly how I want this aspect structurally.

**Ademilade Shodipe-dosunmu:** We'll just change the states here, add state-specific nuances for XYZ, add state-specific information for these filings and these reports, get a, well, like, pretty much the same structure for AJAX colander, each cluster.

**Ademilade Shodipe-dosunmu:** All right, that's the CERN, mostly, then we moved to Diligent.

**Ademilade Shodipe-dosunmu:** So Diligent is probably, apologies in advance, I think all of these clients are, like, extremely boring, but maybe you like working on, like, boring topics, because the CERN is legal and compliance, and Diligent is boards, governance, ESG, sustainability, et cetera, et cetera.

**Ademilade Shodipe-dosunmu:** But yeah, Diligent is a governance platform, an AI-enabled governance platform for small, medium-scale enterprises, pre-IPO companies, and large enterprises.

**Ademilade Shodipe-dosunmu:** they serve their services for all three.

**Ademilade Shodipe-dosunmu:** So they're really huge, really, really big, and one thing you should note about of the Brands for Diligent, which is different from most clients you're going to work with in Grotex, is that most clients that Grotex on board pretty much serve mainly the U.S.

**Ademilade Shodipe-dosunmu:** market, however, Diligent serves a worldwide market, so I think not just U.S., but also Europe and other parts of the world, Asia as well, so you need to keep that in consideration.

**Ademilade Shodipe-dosunmu:** when you're creating content for them, sort of knowing that you're not just writing for U.S.

**Ademilade Shodipe-dosunmu:** audience, and even goes as if you're doing keyword research or anything in SEMR, you're also going to consider worldwide search volumes, not just U.S., so pretty important considerations there.

**Ademilade Shodipe-dosunmu:** For Diligent, I think the pipelines for the jet are probably in, out of all three, out of all three, um, uh, ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** ...

**Ademilade Shodipe-dosunmu:** I'll say that the pipelines for diligence is in the worst shape, not because they haven't spent time on it, but I took a different approach with diligence.

**Ademilade Shodipe-dosunmu:** So I was perfecting the process in Claude before applying it to the pipeline.

**Ademilade Shodipe-dosunmu:** So I just perfected the process.

**Ademilade Shodipe-dosunmu:** Before I went out of office, I perfected the process in Claude.

**Ademilade Shodipe-dosunmu:** So from start to finish, can generate a great article for diligence in about 30 minutes.

**Ademilade Shodipe-dosunmu:** So that starts to finish.

**Ademilade Shodipe-dosunmu:** And I'm just adding everything that they need.

**Ademilade Shodipe-dosunmu:** So I'm in the middle of like adding this to the pipeline.

**Ademilade Shodipe-dosunmu:** So that's like another thing I'm working on next week.

**Ademilade Shodipe-dosunmu:** Am I chasing the pipelines for things yet?

**Ademilade Shodipe-dosunmu:** So I'll keep you posted on that one.

**Ademilade Shodipe-dosunmu:** But for now, the process was mostly Claude, but like, there's a company-wide directive to move everything into Atlas as much as possible.

**Ademilade Shodipe-dosunmu:** So we want to, I'm moving all of that into Atlas by next week.

**Ademilade Shodipe-dosunmu:** So I'll you posted on that one.

**Ademilade Shodipe-dosunmu:** But that's probably what's going on with diligence.

**Ademilade Shodipe-dosunmu:** And I don't think it's...

**Ademilade Shodipe-dosunmu:** Diligence is mostly refreshes.

**Ademilade Shodipe-dosunmu:** They have their huge websites.

**Ademilade Shodipe-dosunmu:** you've checked the page, know that they have like a ton of blog content.

**Ademilade Shodipe-dosunmu:** So most of our efforts are tailored towards refreshing our data pieces of content.

**Ademilade Shodipe-dosunmu:** So for refreshes, we focus mainly on positioning because the company has updated their positioning time and time again.

**Ademilade Shodipe-dosunmu:** So we focus mainly on positioning, emphasizing their AI enabled services, and just adapting some messaging based off of what's going on, as well as adding some of their original research when possible.

**Ademilade Shodipe-dosunmu:** So regarding the research, everything is in the plot project.

**Ademilade Shodipe-dosunmu:** All of their original research, all their reports, surveys, everything is in the plot project.

**Ademilade Shodipe-dosunmu:** I usually update these as they make more research available.

**Ademilade Shodipe-dosunmu:** So I will let you know if like there's any other addition.

**Ademilade Shodipe-dosunmu:** For that, it's pretty up to date.

**Ademilade Shodipe-dosunmu:** That's many of it for Diligence.

**Ademilade Shodipe-dosunmu:** The algebra is pretty simple.

**Ademilade Shodipe-dosunmu:** Considering these are articles that the client is still taking a look at.

**Ademilade Shodipe-dosunmu:** Approved to start, we have quite a couple, about 52 articles that are already approved to start.

**Ademilade Shodipe-dosunmu:** So that's like a healthy buffer for you in terms of production.

**Ademilade Shodipe-dosunmu:** We'll use five articles quickly for them, five editorial.

**Ademilade Shodipe-dosunmu:** Sometimes I do six or seven because I try to make extra to cover any out-of-office periods.

**Ademilade Shodipe-dosunmu:** So once you get to the group, you can actually do a bit more just so that, like, you know, you're good.

**Ademilade Shodipe-dosunmu:** The main part about working with you is that they have their own content marketing platform called Optimizely.

**Ademilade Shodipe-dosunmu:** So that's what you're currently seeing on your screen.

**Ademilade Shodipe-dosunmu:** And what this just means for you is that it's just like a pain of making sure the stuff that's updated here in Airbnb, for example, hey, you finish producing this article, you have sensed it.

**Ademilade Shodipe-dosunmu:** So ideally, you change the status here from like in production to, you know, reviewing diligent or something.

**Ademilade Shodipe-dosunmu:** However, in this case, you do that here.

**Ademilade Shodipe-dosunmu:** Then you also have to do the same thing in optimising, which is a pain.

**Ademilade Shodipe-dosunmu:** You have to essentially create a task for them.

**Ademilade Shodipe-dosunmu:** Add it so that it works.

**Ademilade Shodipe-dosunmu:** But they are like videos in the operating manner already.

**Ademilade Shodipe-dosunmu:** So you should know how to do that for fair.

**Ademilade Shodipe-dosunmu:** But I'm happy to pop on a call to show you how to do this live.

**Ademilade Shodipe-dosunmu:** It's pretty easy.

**Ademilade Shodipe-dosunmu:** It's just like really boring admin work that we can't automate yet.

**Ademilade Shodipe-dosunmu:** But yeah, the parts that can be automated, I have come up with work around for them.

**Ademilade Shodipe-dosunmu:** For example, all refreshes we do.

**Ademilade Shodipe-dosunmu:** Okay, so we do do some net new content sometimes.

**Ademilade Shodipe-dosunmu:** So there is that, right?

**Ademilade Shodipe-dosunmu:** So I keep looking at all that.

**Ademilade Shodipe-dosunmu:** But most of the time it's refreshes.

**Ademilade Shodipe-dosunmu:** So like probably like 75% of the stuff we do is refreshes.

**Ademilade Shodipe-dosunmu:** You also need to note that for any refresh you do, on optimising, who So like that Thank

**Ademilade Shodipe-dosunmu:** I have a prompt for this already and I will get that across to you.

**Ademilade Shodipe-dosunmu:** It's already in the editorial and the client operating manner, honestly, so all you have to do is basically paste in this prompt, paste in the original version of the article before it was refreshed and paste in the refreshed version and to generate these reports for you.

**Ademilade Shodipe-dosunmu:** It's short and just goes over what was actually changed.

**Ademilade Shodipe-dosunmu:** You can review it, edit whatever you want to, but most of the time, I don't really need to edit anything.

**Ademilade Shodipe-dosunmu:** It's really spot on.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** The same goes for the Looker.

**Ademilade Shodipe-dosunmu:** I have a cloud project set up for updating the Looker for performance reports, so literally very simple for you.

**Ademilade Shodipe-dosunmu:** All you literally need to do is paste in the URLs and the categories and it's reformatted for you and I'll show you the project as well.

**Ademilade Shodipe-dosunmu:** Yeah, so I would walk you through how we do Luka updates.

**Ademilade Shodipe-dosunmu:** Let's see.

**Ademilade Shodipe-dosunmu:** Maybe on Monday, next Monday, would you like, are you going to be in office next Monday?

**Ademilade Shodipe-dosunmu:** Yeah.

**Pamela Weber:** Okay, great.

**Ademilade Shodipe-dosunmu:** So maybe like, I think we're like nine hours apart, which is crazy.

**Ademilade Shodipe-dosunmu:** Oh, where are you?

**Ademilade Shodipe-dosunmu:** Nine hours.

**Ademilade Shodipe-dosunmu:** I'm in Lagos, Nigeria.

**Ademilade Shodipe-dosunmu:** that's like West African time.

**Ademilade Shodipe-dosunmu:** I know where it is.

**Pamela Weber:** Okay, so nine hours.

**Pamela Weber:** So, okay, you're later than me.

**Pamela Weber:** Okay.

**Ademilade Shodipe-dosunmu:** All right.

**Pamela Weber:** Yeah.

**Pamela Weber:** Afternoon, this time works for me unless it's too late for you.

**Pamela Weber:** But yeah, we can figure it out online, you know, in Slack what time works.

**Pamela Weber:** But that'll work.

**Pamela Weber:** Monday works.

**Ademilade Shodipe-dosunmu:** Do you usually start like, like, how early do you need to restart your days?

**Ademilade Shodipe-dosunmu:** No one.

**Ademilade Shodipe-dosunmu:** You're ready.

**Ademilade Shodipe-dosunmu:** Bye.

**Ademilade Shodipe-dosunmu:** Bye.

**Pamela Weber:** Bye.

**Pamela Weber:** L

**Pamela Weber:** So nine central.

**Pamela Weber:** So I'm two hours from Pacific.

**Pamela Weber:** So I think that's six for you.

**Ademilade Shodipe-dosunmu:** But like morning I have, I like, sorry, I don't want to go through all the documentation before that.

**Ademilade Shodipe-dosunmu:** So as long as I'm ready, we can do it earlier.

**Ademilade Shodipe-dosunmu:** not, later works.

**Pamela Weber:** So we'll, we'll figure out a time.

**Ademilade Shodipe-dosunmu:** Let me just throw all this in kit to cut up.

**Ademilade Shodipe-dosunmu:** So I know, so don't waste your time.

**Ademilade Shodipe-dosunmu:** It's a lot to get through.

**Ademilade Shodipe-dosunmu:** It is actually a lot of documentation to get through.

**Ademilade Shodipe-dosunmu:** I'm not going to lie.

**Ademilade Shodipe-dosunmu:** It was a lot to actually put the documentation together.

**Ademilade Shodipe-dosunmu:** So I can't imagine how it would be for you to like take all of that in.

**Ademilade Shodipe-dosunmu:** But I would say that like almost all of them are in particular in terms of content points and what clients, what they are liking most.

**Ademilade Shodipe-dosunmu:** So none of them are in particular, which time doesn't like quality.

**Ademilade Shodipe-dosunmu:** So discern laws, content quality is driving results.

**Ademilade Shodipe-dosunmu:** Same for DiddyJet that refreshes their driving results for them.

**Ademilade Shodipe-dosunmu:** Yerko, who is, that's the last client, a bit of a harder not to crack.

**Ademilade Shodipe-dosunmu:** The content is super easy.

**Ademilade Shodipe-dosunmu:** However, the POC is a bit of a difficult person.

**Ademilade Shodipe-dosunmu:** But like, I think you mostly see that on, how I put it, you don't have to deal with that because you're not the engagement manager.

**Ademilade Shodipe-dosunmu:** So that's mostly a Vivek problem.

**Ademilade Shodipe-dosunmu:** But it's a thing where it still comes down to you sometimes because they scope creep from them.

**Ademilade Shodipe-dosunmu:** They're like, I'll always bring clients also.

**Ademilade Shodipe-dosunmu:** So it's a bit weird that like, you know.

**Ademilade Shodipe-dosunmu:** That's how it always works.

**Ademilade Shodipe-dosunmu:** Yeah, yeah.

**Ademilade Shodipe-dosunmu:** They're always the most amazing.

**Ademilade Shodipe-dosunmu:** That's it.

**Ademilade Shodipe-dosunmu:** It's so annoying because we have to do so much of like these little, little things for them.

**Ademilade Shodipe-dosunmu:** Like we check if JASPs are indexed every week and like just like a lot of like little housekeeping stuff for them.

**Ademilade Shodipe-dosunmu:** But I think Yerko probably have to be like a separate call just for Yerko because of just how many themes to keep.

**Ademilade Shodipe-dosunmu:** But I think with these two, should have a general idea of what's expected across the board.

**Ademilade Shodipe-dosunmu:** I think as of now, we're a bit over time, so I just want to give you room to ask a few questions, then we can figure out next steps and align from that.

**Pamela Weber:** Okay, yeah, I was wondering a few things about how many articles per client per week, each of these clients, what do they usually expect?

**Ademilade Shodipe-dosunmu:** Great question, the CERN is supposed to be 25, but we did 26 because they had a slow start when they started with the client, so we're doing like one more every week of a period of a year to catch up.

**Ademilade Shodipe-dosunmu:** So, yeah, so that's 26 for the CERN.

**Ademilade Shodipe-dosunmu:** Diligence is five editorials, the CERN 26 PSU, Diligence is five editorial, you can do more if you want, but pretty much five editorial.

**Ademilade Shodipe-dosunmu:** And Yerko is six.

**Ademilade Shodipe-dosunmu:** So discern is 26.

**Pamela Weber:** Those are like refreshes or those are, I'm sorry?

**Ademilade Shodipe-dosunmu:** Programmatic, so mostly net view, but we do do refreshes sometimes.

**Ademilade Shodipe-dosunmu:** Why are they so much more than other people?

**Ademilade Shodipe-dosunmu:** 26.

**Ademilade Shodipe-dosunmu:** Wow.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** I think it's because it's like programmatic, so it's like the same template for an entire course, so it's easier to do.

**Ademilade Shodipe-dosunmu:** Okay, cool.

**Pamela Weber:** And then what is, how does the deadlines work?

**Pamela Weber:** It sounds like you get stuff Monday and then it's all due by Friday.

**Pamela Weber:** Is that like how it is?

**Pamela Weber:** Or do you have stuff earlier or?

**Ademilade Shodipe-dosunmu:** Okay, great question.

**Ademilade Shodipe-dosunmu:** For discern, in terms of like how the workflow is, I don't think I'm going to be worried about like when do you get stuff for like a lot of months.

**Ademilade Shodipe-dosunmu:** I've lined up about 700 articles to be done.

**Ademilade Shodipe-dosunmu:** So that should like, you guys should be fine in terms of like what content should be done.

**Ademilade Shodipe-dosunmu:** For a while.

**Ademilade Shodipe-dosunmu:** So you will always have it.

**Ademilade Shodipe-dosunmu:** So from the previous Friday, you already know what you're working on the next Friday.

**Ademilade Shodipe-dosunmu:** As of right now, you even know what you're going to work on for the next three months or four months even.

**Ademilade Shodipe-dosunmu:** Oh, that's good.

**Ademilade Shodipe-dosunmu:** Yeah, we've up like a lot of content.

**Ademilade Shodipe-dosunmu:** Let me show you the content OS.

**Ademilade Shodipe-dosunmu:** I like that.

**Pamela Weber:** That's easier to plan then.

**Pamela Weber:** And the other ones, are they like the same thing, like Monday?

**Ademilade Shodipe-dosunmu:** So I usually line up topics the Friday before.

**Ademilade Shodipe-dosunmu:** Depends on like...

**Ademilade Shodipe-dosunmu:** Okay, I didn't...

**Ademilade Shodipe-dosunmu:** Yeah, pretty much we'll line them on the Friday before.

**Ademilade Shodipe-dosunmu:** So usually like...

**Ademilade Shodipe-dosunmu:** awesome.

**Ademilade Shodipe-dosunmu:** I didn't know you could.

**Pamela Weber:** I thought like Monday you get the titles and you have to like work...

**Pamela Weber:** I mean, as early as I get anything, I would love to do that.

**Pamela Weber:** So I'm sorry, go ahead.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah, Friday is, you're good to go.

**Ademilade Shodipe-dosunmu:** So this is...

**Ademilade Shodipe-dosunmu:** So if you're good to like assignments here, you're going to see like everything.

**Ademilade Shodipe-dosunmu:** I mean, that's a wrong resort.

**Ademilade Shodipe-dosunmu:** We're ready to track.

**Ademilade Shodipe-dosunmu:** That's very good, sorry.

**Ademilade Shodipe-dosunmu:** Where is Yeah, I'm just going to mute.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Let's just put all our reports.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** That's actually reset.

**Ademilade Shodipe-dosunmu:** What's going on?

**Ademilade Shodipe-dosunmu:** Oh, so I think Eritable is not good.

**Ademilade Shodipe-dosunmu:** It was like, it's literally sharing with the same thought.

**Ademilade Shodipe-dosunmu:** Oh, Yep.

**Ademilade Shodipe-dosunmu:** Eritable is back.

**Ademilade Shodipe-dosunmu:** So, like, if you look here, you have, like, about 1,300 and so assignments already.

**Ademilade Shodipe-dosunmu:** If you pull down a bit more, it's separated by status.

**Ademilade Shodipe-dosunmu:** So, pull all the way down.

**Ademilade Shodipe-dosunmu:** Sorry.

**Ademilade Shodipe-dosunmu:** Trying to find, like, a view that gives you what you need to see.

**Ademilade Shodipe-dosunmu:** Okay, great.

**Ademilade Shodipe-dosunmu:** So, approved for creation.

**Ademilade Shodipe-dosunmu:** So, about 600, suppose, yeah.

**Ademilade Shodipe-dosunmu:** 612 over here.

**Ademilade Shodipe-dosunmu:** And these guys, oh.

**Ademilade Shodipe-dosunmu:** Starts from like, you probably will start working on these ones from like the third week of January.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** But like for the next, for first week of January, have that covered.

**Ademilade Shodipe-dosunmu:** Second week of January, yeah, I suppose lined up already for you to work on.

**Ademilade Shodipe-dosunmu:** And from third week of January, all you have to pick from here.

**Ademilade Shodipe-dosunmu:** So, I mean, you and Vivek can figure out like how you want to go about it.

**Ademilade Shodipe-dosunmu:** My managers have usually pretty much given me autonomy in like picking topics and like going around some flow.

**Ademilade Shodipe-dosunmu:** However, if like client has like a request or something, like, oh, hey, like, oh, this is a priority refresh.

**Ademilade Shodipe-dosunmu:** We want to work on this this week.

**Ademilade Shodipe-dosunmu:** Then, you know, that takes priority, you know, whatever.

**Ademilade Shodipe-dosunmu:** But like, it doesn't like normal content production, like it's all here.

**Ademilade Shodipe-dosunmu:** So you just dive into one, like pick from here.

**Ademilade Shodipe-dosunmu:** So you can just move them to the, um, ready to start or, and you can take that from there.

**Ademilade Shodipe-dosunmu:** So would you like it over like 30 minutes, so that you understand all the status?

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** All the personal views and everything.

**Ademilade Shodipe-dosunmu:** yeah, like here are these 600 topics for the CERN, 600 and 12.

**Ademilade Shodipe-dosunmu:** That's cool.

**Ademilade Shodipe-dosunmu:** Then for Diligent, have about, in terms of approved, I think we have at least, I think at least, I'm to think, almost 16 weeks out.

**Ademilade Shodipe-dosunmu:** Oh, that's awesome.

**Ademilade Shodipe-dosunmu:** I thought it was like a week out every time.

**Ademilade Shodipe-dosunmu:** Like Monday, we get it Monday, we try to.

**Ademilade Shodipe-dosunmu:** That's awesome.

**Ademilade Shodipe-dosunmu:** I thought he was explaining to me like two different ways.

**Ademilade Shodipe-dosunmu:** So, okay.

**Ademilade Shodipe-dosunmu:** So cool.

**Ademilade Shodipe-dosunmu:** That's what I asked you again.

**Ademilade Shodipe-dosunmu:** We try to give like our POC like a lot of stuff to review at once.

**Ademilade Shodipe-dosunmu:** So like we're not blocked.

**Ademilade Shodipe-dosunmu:** So usually what I do is that like when I see like the number and our picture starts going down, maybe like it's probably 53.

**Ademilade Shodipe-dosunmu:** So when it goes down to maybe like 20, that means you just have like a month of content left that's approved.

**Ademilade Shodipe-dosunmu:** And we probably would start to be like, hey, she needs to have put a couple more articles on life.

**Ademilade Shodipe-dosunmu:** And

**Ademilade Shodipe-dosunmu:** We need to keep this rolling.

**Ademilade Shodipe-dosunmu:** So I never let it go like really close to us so that like whatever blocked by them and we can just keep going.

**Pamela Weber:** So yeah.

**Ademilade Shodipe-dosunmu:** I'm sorry.

**Ademilade Shodipe-dosunmu:** I don't know the question.

**Ademilade Shodipe-dosunmu:** Go ahead.

**Pamela Weber:** So the editorial guidelines you sent to me, are those like already embedded in the pipeline?

**Pamela Weber:** Or like every time I run an article, do I need to add that?

**Pamela Weber:** Or it's already, when it's filled, pipeline's built, are those already put inside?

**Ademilade Shodipe-dosunmu:** So those are already, most of those are already embedded in.

**Ademilade Shodipe-dosunmu:** There are things that like, I probably think are difficult to embed as of right now, which is why, you know, why we have jobs.

**Ademilade Shodipe-dosunmu:** You know, this thing is like, you know, that human pass, even if it's like 10, 15 minutes of like edits.

**Ademilade Shodipe-dosunmu:** So it's just to get you familiar with like what good content for the client is supposed to look like.

**Ademilade Shodipe-dosunmu:** But yeah, I would say like 90 something percent of those are already embedded in the pipelines as they are.

**Ademilade Shodipe-dosunmu:** And just have to do those fact checks to make sure that like it's aligned.

**Ademilade Shodipe-dosunmu:** OK, yeah, of course, I know I have to review all that.

**Pamela Weber:** That makes.

**Pamela Weber:** The agent isn't always going to do what you ask it.

**Pamela Weber:** was just wondering if it's like one more step.

**Ademilade Shodipe-dosunmu:** that's cool.

**Pamela Weber:** That's so awesome.

**Pamela Weber:** That's like one less thing.

**Pamela Weber:** The only other thing that I'll let you go, I mean, I'll have a lot of questions, but we can go over them, you know, slowly.

**Pamela Weber:** So the, like, how do you do the article?

**Pamela Weber:** Is it like a Google Doc to deliver?

**Pamela Weber:** Or is it, it's like somehow magically from the pipeline gets pushed to the right person?

**Ademilade Shodipe-dosunmu:** Or how do I do that?

**Ademilade Shodipe-dosunmu:** I don't know.

**Pamela Weber:** Well, there's a lot of magic with this AI.

**Pamela Weber:** Yeah, it's a lot of magic.

**Ademilade Shodipe-dosunmu:** Good question, actually.

**Ademilade Shodipe-dosunmu:** There's many Google Docs.

**Ademilade Shodipe-dosunmu:** And each client has, like, how content is delivered to them.

**Ademilade Shodipe-dosunmu:** So it's different for each client.

**Ademilade Shodipe-dosunmu:** For dessert, pretty much, we have the rights to publish directly.

**Ademilade Shodipe-dosunmu:** Our POC doesn't review.

**Ademilade Shodipe-dosunmu:** Like I said, he only reviews the first article in each new cluster.

**Ademilade Shodipe-dosunmu:** Just...

**Ademilade Shodipe-dosunmu:** Mark for the PSU pipeline.

**Ademilade Shodipe-dosunmu:** So you just have to go in, adjust the template, and the PSU pipeline does all the work every later, and you know what to change.

**Ademilade Shodipe-dosunmu:** So that's that.

**Ademilade Shodipe-dosunmu:** So for discern, as soon as you're doing an article and you've reviewed it, the only thing left is to add it to our publishing queue and send it to our publisher.

**Ademilade Shodipe-dosunmu:** Oh, so I don't do any publishing?

**Pamela Weber:** I thought that was part of the managing editor at all.

**Ademilade Shodipe-dosunmu:** It is.

**Ademilade Shodipe-dosunmu:** It is.

**Ademilade Shodipe-dosunmu:** And, like, that's why I said, like, you're going to, you're firing up automated publishing for discern soon, so it'll be your job to review what actually gets published.

**Ademilade Shodipe-dosunmu:** So once you run the automated publishing pipeline, it's not going to be your job to make sure, oh, hey, does it actually look properly, like, proper on the website?

**Ademilade Shodipe-dosunmu:** Does look good?

**Ademilade Shodipe-dosunmu:** have any issues with that?

**Ademilade Shodipe-dosunmu:** So, yeah.

**Ademilade Shodipe-dosunmu:** Then for diligent, Sulaiman also publishes.

**Ademilade Shodipe-dosunmu:** So what did the, diligent flow is a bit different.

**Ademilade Shodipe-dosunmu:** Diligent reviews every piece of content.

**Ademilade Shodipe-dosunmu:** Yep.

**Ademilade Shodipe-dosunmu:** And they have multiple reviewers.

**Ademilade Shodipe-dosunmu:** So it's a pain.

**Ademilade Shodipe-dosunmu:** Which is why at the point I was doing more articles each week, just so that we have like, we have like a rolling backlog for them to keep reviewing.

**Ademilade Shodipe-dosunmu:** Because sometimes you're really slow with it.

**Ademilade Shodipe-dosunmu:** Yeah, because they have a content team and they have an SEO team.

**Ademilade Shodipe-dosunmu:** And no, those teams are not under the same umbrella.

**Ademilade Shodipe-dosunmu:** Those are separate teams.

**Ademilade Shodipe-dosunmu:** And they review separate things in the articles.

**Ademilade Shodipe-dosunmu:** silly.

**Ademilade Shodipe-dosunmu:** That's, I mean.

**Ademilade Shodipe-dosunmu:** Yeah, it's a whole thing.

**Ademilade Shodipe-dosunmu:** Yeah, but like, they're all pretty nice people.

**Ademilade Shodipe-dosunmu:** Okay.

**Ademilade Shodipe-dosunmu:** But like, it's just like, it's just like a long thing.

**Ademilade Shodipe-dosunmu:** Like, you won't really get, like, like I said, the pipeline is like in a really good case.

**Ademilade Shodipe-dosunmu:** For example, last week, I got like one comment in like five articles.

**Ademilade Shodipe-dosunmu:** So there's that.

**Ademilade Shodipe-dosunmu:** So, like I said, the process is already in a pretty good state.

**Ademilade Shodipe-dosunmu:** Sometimes maybe in a week, you might get like three, four, five comments.

**Ademilade Shodipe-dosunmu:** Like, I'm also the time.

**Ademilade Shodipe-dosunmu:** like, could he just add this link?

**Ademilade Shodipe-dosunmu:** Or like, could he.

**Ademilade Shodipe-dosunmu:** Okay, let's, can we swap this for this?

**Ademilade Shodipe-dosunmu:** Or, oh, we want to spotlight this product a bit more permanently or something like that.

**Ademilade Shodipe-dosunmu:** Nothing really too crazy.

**Ademilade Shodipe-dosunmu:** They are, they are, they are happy with the quality of content that our process is producing.

**Ademilade Shodipe-dosunmu:** So, you're good there.

**Ademilade Shodipe-dosunmu:** With Yurko, Yurko is a bit different.

**Ademilade Shodipe-dosunmu:** Okay, so when Diligent approves it, then you can now pass it off to Sulaiman for publishing, which is his own process.

**Ademilade Shodipe-dosunmu:** Then for Yurko, we do not publish.

**Ademilade Shodipe-dosunmu:** We stage, So the, like I said, lowest paying clients and the most stress and the process of staging is pretty much the most stressful out of all the other clients.

**Ademilade Shodipe-dosunmu:** It's just a thing.

**Ademilade Shodipe-dosunmu:** They use Prismic, which is a pain for publishing.

**Ademilade Shodipe-dosunmu:** Like, you have to copy and paste, like, sections manually.

**Ademilade Shodipe-dosunmu:** You can't paste the whole thing because Prismic uses, like, So, like, each H2, it's its own slice.

**Ademilade Shodipe-dosunmu:** So, like, you have, like, an H2, you put it in one slice.

**Ademilade Shodipe-dosunmu:** You put the content in that slice, then create another slice.

**Ademilade Shodipe-dosunmu:** Then...

**Ademilade Shodipe-dosunmu:** Yeah, it's just a thing.

**Ademilade Shodipe-dosunmu:** But yeah, I'll show you how to like not get that.

**Ademilade Shodipe-dosunmu:** It takes like maybe like 10 minutes, 10 to 15 minutes to stage an article in Prismik.

**Ademilade Shodipe-dosunmu:** That's crazy.

**Pamela Weber:** That's the time we're supposed to be doing post-production just on an article.

**Pamela Weber:** Yeah.

**Ademilade Shodipe-dosunmu:** Exactly.

**Ademilade Shodipe-dosunmu:** That's okay.

**Ademilade Shodipe-dosunmu:** I'll learn it.

**Pamela Weber:** But yeah, it's annoying.

**Pamela Weber:** Well, on onboarding, they said there's certain clients, the criteria for are they worth it or not.

**Pamela Weber:** sounds like that's one that he sits at.

**Pamela Weber:** So, thank you.

**Ademilade Shodipe-dosunmu:** That's one of my questions.

**Ademilade Shodipe-dosunmu:** Go ahead.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah.

**Ademilade Shodipe-dosunmu:** They don't pay a lot.

**Ademilade Shodipe-dosunmu:** And like, I think only two of our clients use Prismik.

**Ademilade Shodipe-dosunmu:** That's why like engineering has not prioritized automated publishing for Prismik.

**Ademilade Shodipe-dosunmu:** Especially because it's so complicated and custom.

**Ademilade Shodipe-dosunmu:** It's not like paying one size fits all.

**Ademilade Shodipe-dosunmu:** Like web flow.

**Ademilade Shodipe-dosunmu:** Web flow templates are pretty much similar across clients.

**Ademilade Shodipe-dosunmu:** But like Prismik is very, very different with each client.

**Ademilade Shodipe-dosunmu:** So like they have to do like a custom automation flow for publishing.

**Ademilade Shodipe-dosunmu:** And like, it's like maybe as of right now.

**Ademilade Shodipe-dosunmu:** So we'll see how that goes, but for now, you know, just have to get the job done.

**Ademilade Shodipe-dosunmu:** Okay, cool.

**Pamela Weber:** Thank you for that.

**Pamela Weber:** Thank you for all this, and I appreciate your time, and especially in your week off, getting me going on it.

**Pamela Weber:** good.

**Ademilade Shodipe-dosunmu:** All good.

**Ademilade Shodipe-dosunmu:** Like, it's my job to make sure that, like, your handlebar is, this handlebar is as smooth as possible, and, like, even after, like, you know, I've passed it on, like, I'm still available for, like, questions, and, like, feel free to reach out, like, anytime, like, literally, I just, like, shoot me a DM, and, like, I'll work on that as soon as I can.

**Ademilade Shodipe-dosunmu:** We want this to be very free.

**Ademilade Shodipe-dosunmu:** I joined, like, I joined this company, like, seven months ago, so, like, I know how it feels to be, like, thrown into the deep end immediately, so I want to avoid that for you as much as possible.

**Pamela Weber:** Well, I'm used to creating all these systems and training people on them, and so for me to come in and see the already preset, it's, like, now I get what I put people through, because it's, like, a lot all at I'm to it.

**Pamela Weber:** it.

**Pamela Weber:** You know, because I would move things around and adapt.

**Pamela Weber:** And so, yeah, so it's a lot, but it's fun.

**Pamela Weber:** I like it.

**Pamela Weber:** I you froze.

**Pamela Weber:** Can you still hear me?

**Pamela Weber:** At least your picture froze.

**Pamela Weber:** Okay.

**Pamela Weber:** Oops.

**Pamela Weber:** Well, I think we're done anyway, so.
