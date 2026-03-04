# CMs Daily Standup – Atlas Sync

<metadata>
date: 2025-07-16
time: 15:28 UTC
duration: 32 minutes
organizer: Saskia Wartnaby
participants: Matthew Panzarino, Mariana Marins, Jenn Peters, Rachel Pasche, Sucheta Biswas, Josip Sovar, Usman Adepoju
fathom_recording_id: 74534029
fathom_url: https://fathom.video/calls/353063979
share_url: https://fathom.video/share/ShaQSx1LWT4B4nqcx2uXtf_2MZad_kGw
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

The CMs team met to discuss progress on Atlas, the new content management platform, and address critical workflow blockers. Matthew Panzarino led discussion on Atlas improvements including content structure guidance, AI Assist tool bug fixes, and external/internal linking issues. The team identified client-specific challenges including the Tiro account's intro reflow problem, Abnormal's incorrect keyword links to careers page, and Exec Rights articles not being indexed — with escalation paths clarified for flagging SEO and indexing issues in internal channels.

---

## Context

This is an internal GrowthX standup for Content Managers who use Atlas, the new proprietary content management and workflow platform that Panzarino leads. Atlas is GrowthX's replacement for Airtable-based workflows and represents a significant shift in how the delivery team scales content production. The standup format allows CMs to surface blockers, request feature additions, and stay aligned on product roadmap priorities. Mariana Marins coordinates scheduling, and Matthew Panzarino owns the product and technical direction. This particular meeting focused on urgent workflow issues affecting specific client accounts (Tiro, Abnormal, Exec Rights) and Atlas feature gaps around content structure guidance and linking.

---

## Relevance

- **To GrowthX Delivery:** Blocking issue on Tiro account — statistics appearing in introductions despite explicit instructions. Solution: bespoke polishing workflow step between article generation and fact-checking to remove stats/links from intros. New publisher (Suleiman) will enable automated publishing to Framer CMS, eliminating manual reflow. Abnormal account has systemic sitemap issue causing keywords to link to careers page instead of homepage — requires SEO audit and hardcoded link feedback step. External linking broken across all workflows; internal linking improvements needed. Underlying prompt semantics for statistics placement needs review.

- **To GrowthX Business Development:** Exec Rights account health risk flagged — articles not indexing due to 404 errors on article hub pages. Usman Adepoju correctly identified and escalated; clarified protocol to post indexing/SEO issues in internal channel tagged to Elvis, Megan, and Dave for visibility. Shows need for proactive SEO audits pre-delivery and health checks on client infrastructure.

- **To CheckThat:** SEO and indexing challenges directly impact content performance and attributable outcomes for clients. Abnormal's keyword linking errors and Exec Rights' indexing failures are the type of AI visibility / AEO issues CheckThat could surface and help diagnose through site audits and structured data analysis.

---

## Overview

- Atlas improvements: Developing content structure guidance (article archetypes like lists, how-tos, guides) and fixing AI Assist tool bugs (page jumping, bullet point handling)
- External linking broken; Kirkland investigating. Internal linking flow needs improvement to increase link quantity
- New publisher (Suleiman) hired, starting this week/next, to build automated publishing steps for all pipelines, enabling direct staging to client CMS systems
- SEO best practices (leading with statistics) override narrative quality in prompts; Matthew and Jason reviewing underlying prompt semantics
- Atlas roadmap: Content library integration (replacing Airtable), content quality ratings, adherence-to-instructions metrics, performance/quality dashboard

---

## Key Topics

### Atlas Improvements and Bug Fixes

  - Developing solutions for specific guidance on content structure, including article archetypes (lists, how-tos, guides)
  - AI Assist tool bugs (page jumping, bullet point handling) being fixed
  - External linking not working; issue flagged and being addressed
  - Internal linking flow improvements coming to increase link quantity

### Workflow Customization for Tiro Account

  - Issue: Statistics appearing in introductions despite instructions
  - Solution: Create bespoke workflow with separate polishing step for introductions
  - Future improvement: Automated publishing step for staging in Framer CMS

### SEO and Indexing Challenges

  - Abnormal account: Keywords linking to careers page by default; likely a sitemap issue
  - Exec Rights: Articles not being indexed; some sections returning internal server errors
  - Importance of flagging SEO issues in internal channels and tagging relevant team members

### Atlas Future Development

  - Content library integration to replace Airtable
  - Content quality ratings and adherence to instructions
  - Dashboard for content performance and quality metrics

---

## Action Items

**Rachel Pasche (GrowthX)**
- File ticket for new workflow step to remove stats/links from Tiro intros, reflow, insert between article generation and fact-checking steps

**Sucheta Biswas (GrowthX)**
- File ticket re Abnormal keyword links defaulting to careers page instead of homepage
- Post issue in Abnormal internal channel, tag Elvis, Megan, Dave

**Usman Adepoju (GrowthX)**
- Post Exec Rights indexing issues in internal channel. Tag Elvis, Megan, Dave
- Mention 404 errors on article list pages preventing indexing of PSEO content

---

## Transcript

**Mariana Marins:** Thank you. Hey guys, how are you?

**Jenn Peters:** How's going?

**Mariana Marins:** How's it going? I have just sent Panzer a reminder for him to be here. He will be. Thank you.

**Matthew Panzarino:** Good morning.

**Matthew Panzarino:** How's everybody doing this morning?

**Matthew Panzarino:** Not good, huh?

**Jenn Peters:** So far, so good.

**Jenn Peters:** It's only 8.30 here still.

**Matthew Panzarino:** Yes, the day is young.

**Matthew Panzarino:** Or old, depending on where you are on the globe.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** So, what are the issues that you folks have been seeing?

**Matthew Panzarino:** We're working on a wide variety of improvements.

**Matthew Panzarino:** A lot of them based on your feedback, of course.

**Matthew Panzarino:** Jason and I have been experimenting with different ways to introduce specific guidance on structure because I know a lot of you have clients that want kind of rough structures from your content that are not precisely PSEO.

**Matthew Panzarino:** In other words, they're not completely templatized, but they want a certain flow to their article or basically a rough kind of outline of how they want to tackle a particular topic.

**Matthew Panzarino:** We're working on a solution for that.

**Matthew Panzarino:** At the very least, we want to expose the types, the major archetypes of articles, like lists or how-tos or guides or that sort of thing.

**Matthew Panzarino:** And then there's probably a drill down from there where we can have you propose content structure and adheres to it a little bit more rigorously, so we'll work on that as well, but we're continuing to chip away at that.

**Matthew Panzarino:** I know that the AI Answers tool had some bugs, those have been flagged, they're working on those, or the AI Assist tool, excuse me.

**Matthew Panzarino:** So they're working on those.

**Matthew Panzarino:** Some of the bugs where it was jumping around the page were probably quashed for you and others will be soon.

**Matthew Panzarino:** And then it should be handling bullet points a little better, et cetera.

**Matthew Panzarino:** So working on fixes for those.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Other than that, happy to hear from you about any issues you have with workflows, anything that's currently going on that's broken or that's not working properly, anything that we can do to make sure that you're able to produce at scale.

**Matthew Panzarino:** So hit me with anything you have.

**Jenn Peters:** I think for us on our end, we were just, um, discovering that the external linking, um, wasn't working.

**Jenn Peters:** Um, and I think some other team

**Jenn Peters:** James found that as well.

**Jenn Peters:** We filed tickets for it yesterday, and we've just been adding them manually in the meantime.

**Jenn Peters:** But yeah, it just was kind of one of those, like, sudden breaks, but where we were just noticing, like, oh, hey, there's no, like, external links here, but.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, there is an issue with that.

**Matthew Panzarino:** Kirkland's looking at it.

**Matthew Panzarino:** There is, there's something going on with the external links.

**Matthew Panzarino:** The internal linking flow also needs some improvements, and he's doing a pass on the, on that.

**Matthew Panzarino:** So, um, the ticket's been filed, people are aware, and then the internal linking should also be getting better soon.

**Matthew Panzarino:** There's, um, there was an issue preventing it from basically putting as many links as it should, uh, in there, which I know some of you have seen.

**Matthew Panzarino:** So, as long as the ticket's been filed, we'll, we'll work on it.

**Matthew Panzarino:** Um, anything else, anything else you're seeing?

**Rachel Pasche:** back.

**Rachel Pasche:** I have one random thing that's so small, but I just cannot figure out how to fix it.

**Rachel Pasche:** For one of my clients, it's the Tiro account, they can't, like their CMS can't support links in the introduction, because the introduction is like in a separate spot.

**Rachel Pasche:** And I've put it in the, you know, artifacts, the instructions, everything, like do not include statistics in the introduction.

**Rachel Pasche:** And then even in the brief, sometimes it'll be, you know, like when you get the brief, it'll be like open with compelling statistics.

**Rachel Pasche:** I don't know why every brief I've ever created wants to open with two to three compelling statistics.

**Rachel Pasche:** And I'll remove that and it'll still, they'll still sneak them in, even if it's not in the brief, even if it's not in the outline, the final draft, like by the time I get to like the SEO draft section, or the final version, you know, after it's like added.

**Rachel Pasche:** Internal and external links.

**Rachel Pasche:** It's still just like slipping in these useless statistics.

**Rachel Pasche:** And it's a small thing.

**Rachel Pasche:** Like it's not hard to go in and fix it, but it is something that like I manually have to remove at like every step of the workflow for every Tiro article that I do.

**Rachel Pasche:** And I've just noticed like, you know, I don't want every flow sum or every, I don't want every article to open with statistics.

**Rachel Pasche:** And for some reason, it insists upon opening with statistics.

**Matthew Panzarino:** Yeah, that's probably because the underlying prompt asks it to do that. You know, the fact is that almost every article needs statistics and best practices to include in the intro so it gets cited when someone asks for a statistic. It's SEO best practice, which overrides narrative taste. A lot of SEO best practices override good taste. Let's be honest with ourselves — the things that perform well on the internet often suck from a narrative perspective. We're victims of 30 years of pandering to the ad network agenda. The quality of editorial and how things read online frankly stinks for the most part. LLMs and SEO crawling engines have been trained on that bad content. We're in a place where this kind of crap ends up at the top of articles. There's nothing you can do about it because it's what the beast wants and you have to feed the beast. In an editorial context, I'd say boo SEO and let's write good stuff for humans. However, we're not in that business. We're in the business of making sure it ranks well.

**Rachel Pasche:** We need to take a look at the underlying prompts and see if there's a better way to phrase that.

**Matthew Panzarino:** So I think there's a balance to be struck here between saying like, no statistics in the intros and going like, okay, you know, what do we do about this?

**Matthew Panzarino:** Is it a client-specific need really?

**Matthew Panzarino:** Or is it like a broad thing?

**Matthew Panzarino:** Because if it's like, you know, this is not going to happen.

**Matthew Panzarino:** But if we were saying we don't want statistics to appear in the intros of any of our articles, working on the base prompt to like, you know, tell it specifically and very explicitly not to use those would be the play.

**Matthew Panzarino:** Simple play.

**Matthew Panzarino:** Go in there, make sure that every pipeline just gets updated.

**Matthew Panzarino:** The underlying prompt that powers every pipeline gets updated with instructions not to do that.

**Matthew Panzarino:** However, I think that the use case for you or the case for you here with Tiro, if you don't want statistics in there because you don't want to have to link to them or, you know, you don't want those to appear is probably...

**Matthew Panzarino:** Probably to create just a bespoke workflow, like a step that happens that reflows your intro to remove statistics if they appear and deletes any links.

**Matthew Panzarino:** And we can probably add that after the article generation step and then create this basically new intro that makes sure that it goes in there.

**Matthew Panzarino:** Now, let's go one step further.

**Matthew Panzarino:** When you deliver to Tiro, are you delivering the introduction separately so that they can publish it separately?

**Rachel Pasche:** No, I'm just rewriting the introduction after the fact.

**Matthew Panzarino:** like, what's their deliverance look like for them, I guess, is my question.

**Matthew Panzarino:** Is it a Word doc?

**Rachel Pasche:** Is it a, what is it?

**Rachel Pasche:** Yeah, it's just like a Google doc.

**Matthew Panzarino:** Okay, and they are taking the intro then and putting into their scene, they're doing the scene after Okay, so, and what are they on?

**Rachel Pasche:** What platform are they on?

**Rachel Pasche:** They're on Framer.

**Matthew Panzarino:** Framer.

**Matthew Panzarino:** Sucky.

**Matthew Panzarino:** Okay, so we hired a publisher, Suleiman, who's been doing publishing and other work for us and is going full-time — starting this week or next. His whole job is to make sure every one of our pipelines has an automated publishing step. At the end of your pipeline, you'll be able to stage your stuff in Framer. Whatever they want to do with publishing and actually pushing the publish button is something they can talk about with Suleiman. The goal is that you can hit approve at the end and it moves to the next step, staged in their CMS. Either they publish it, we publish it, or it goes straight to publish — whatever SOP they love and you love and everyone's happy with, that's what we'll do.

**Matthew Panzarino:** The reason I'm talking about that is because if we create adjustments where the introduction gets generated, edited, and polished separately, it can go into its own field in the publishing workflow and be published separately. It can be handled in a bespoke manner, completely separately from the body text, so you can make direct adjustments to the introduction without tweaking things manually every time. I don't think the solution is to adjust the underlying prompt, given that it's a specific need for Tiro. Even if other people have it, we could just implement the same workflow for them.

**Matthew Panzarino:** So what I would do is file a ticket asking for a workflow with a separate polishing step that only works on the introduction. That polishing step removes statistics, deletes links, and reflows it together with body copy, producing a new output. It would go between article generation and fact-checking, or after internal linking and before fact-checking. You want to do it after the linking step because linking will just put links back. That's how we'd handle this programmatically instead of doing it manually over and over.

**Rachel Pasche:** Okay, cool.

**Matthew Panzarino:** I appreciate the suggestions, but the underlying prompts are adamant about leading with statistics because it's SEO best practice. There's a bigger conversation about the underlying prompts we've danced around for months, but Jason and I are working on it. We're close reading the prompts from last year. They've been updated several times — we'll keep updating parts like bullet points. But the semantics of the overall prompts need review; they could be a lot better. We'll get there.

**Matthew Panzarino:** Abnormal's keywords are linking to the careers page by default. Is that still happening?

**Sucheta Biswas:** Yeah, it's happening across all articles. I've shared two instances for you on Learning Atlas.

**Matthew Panzarino:** That's probably a sitemap issue. Their careers page is probably in the wrong place in the sitemap. There's no quick fix I can think of immediately. It's the way it's being crawled.

**Matthew Panzarino:** Sitemap or keyword rank is the number one cause for those things. What we can do about it is another matter because we can't suddenly make their homepage rank better. We could address sitemap things, but I don't know if we can hardcode a link to a particular word. I don't think there's a provision for that right now, but we could file a ticket since it should link to their homepage.

**Sucheta Biswas:** The security jobs link also keeps appearing in articles.

**Matthew Panzarino:** That likely ranks very highly or is prominently placed in their sitemap. If we haven't done an SEO audit, Dave can help with that. One approach is to audit the site and flag these issues. The other side is fixing the problem immediately through a polishing step or feedback step where we hardcode instructions: "If you link to Abnormal, link to the homepage."

**Sucheta Biswas:** Thanks.

**Matthew Panzarino:** Anything else? I wanted to flag something for everybody. Somebody told somebody this and they still didn't know it. You can pin your accounts to the top of your page — just hover over your account and there's a little pin that appears in the top left corner in Atlas. They added that a few weeks ago, but I think some people still don't know. If you have a list of people you're working on every day, you don't have to scroll or search. Just flagging that.

**Josip Sovar:** Thanks for that info.

**Josip Sovar:** That will be very helpful.

**Josip Sovar:** When we're always looking, where is it, where is it?

**Josip Sovar:** And it's so usually down, down the road and it takes a minute or always.

**Matthew Panzarino:** Thanks.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah, yeah, exactly.

**Matthew Panzarino:** It's, uh, you know, the, anything that saves.

**Matthew Panzarino:** A few seconds a day is minutes or hours a year, so there you go.

**Josip Sovar:** Yeah, that's true.

**Usman Adepoju:** I think on my head, I've been trying to figure out how to raise my hand in Zoom, but...

**Matthew Panzarino:** Oh, yeah, no problem, speak up.

**Usman Adepoju:** So, for exec rights, I was trying to check the articles I've written in the past two weeks.

**Usman Adepoju:** I found out the articles I've written aren't being indexed. There are some sections on their site returning internal server errors. The articles are live and I can view them, but Google Search Console shows they're not being indexed. I just found out today.

**Matthew Panzarino:** Oh, just today?

**Matthew Panzarino:** Okay, yeah.

**Matthew Panzarino:** Mentioning to Elvis is the right thing to do, but it definitely needs to be visible. Make sure these conversations occur where multiple people can see them and are publicly recorded. You can DM Elvis or have a side chat, that's fine. But the core conversation about pages not getting indexed should go in the internal channel for that account. Post exactly what you're doing, tag Elvis, tag Dave as our internal SEO expert, and you can tag the director too because they bring things like this to the client. You're right to call this out — it's directly applicable to whether our content performs and whether we achieve goals for them. Flag it publicly so it's really visible. You can even submit a good chunk of articles a week to Google to help indexing. If articles aren't being indexed or the rate feels slow, that's definitely worth flagging.

**Usman Adepoju:** The issue is on their site. When you navigate to where the PSEO articles are listed, you get a 404 error on the hub page where the articles themselves are located.

**Matthew Panzarino:** That's exactly what an SEO audit or site health audit would find. We've done these for some clients, and they're very grateful. It's great for us because they say "thank you for pointing this out," but it also helps us diagnose performance problems. When articles aren't performing, it's often because they aren't being indexed because the hub page is 404ing. That's a big problem. Good thing to flag.

**Matthew Panzarino:** Anything else? Any other issues or blockers? You know, people ask why Atlas. Because Atlas lifts heavy things — it's from mythology. I'm assuming that's why it does the heavy lifting. As it stands now, Atlas is like an Airtable clone, but the planned features are much bigger. We're building a content library right now, so no more Airtable. All your content will live in Atlas in the library. You'll see status (published, reviewed), content quality ratings, whether it's adhering to the outline, whether it strayed from instructions. Lots of fun stuff coming. Currently it's an MVP to get us off Airtable because it's slow. Eventually it will handle all the content we publish. What you currently do manually in Airtable — managing documents, links, published status, content reporting — should not be manual labor.

**Matthew Panzarino:** Daryl pointed out something funny but true — we've automated the fun part and not the annoying parts yet. The annoying parts are collating published material, managing statistics and reporting in Airtable, manually looking at Looker dashboards. The dashboard section of Atlas will have content performance, quality metrics, and performance metrics. Startups are about using half-finished things to create finished things — that's the name of the game.

**Matthew Panzarino:** Anything else? You can always reach out. I have one-on-ones with some of you as well.

**Mariana Marins:** I've scheduled the final CM meetings for this week. If you haven't had a one-on-one with Matthew yet, please let me know on Slack and I'll work things out.

**Matthew Panzarino:** I don't think it's sustainable to do a complete round robin and start over. I'd rather establish a monthly-ish cadence where I talk to all of you once a month or month and a half. I want to keep doing these because you collect issues that aren't quite tickets or are more process-oriented. I don't want things to fall into the cracks. Not everyone has issues ready when we do these standups, so monthly makes more sense. We'll aim for August, and then keep cycling. In the meantime, don't wait for that meeting. If you have a major issue or a persistent minor issue, post it in Learning Atlas and tag me so we can tackle it async. Mariana can flag it to the right people. It doesn't all need to go through me. If you need to talk directly, reach out to Mariana and we'll get time on the calendar. You can be proactive about it. I don't want anyone in the lurch thinking "I had this problem three weeks ago but I was waiting for our meeting." Don't wait. We'll fix it now. Thanks, folks. Appreciate it.

**Josip Sovar:** Thanks.
