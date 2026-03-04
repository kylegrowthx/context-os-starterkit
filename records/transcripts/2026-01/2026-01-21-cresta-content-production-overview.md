# Cresta Content Production Overview

<metadata>
date: 2026-01-21
time: 15:31 UTC
duration: 29 minutes 30 seconds
enriched_on: 2026-02-28 09:15 UTC
organizer: rachel@growthxlabs.com
fathom_recording_id: 115973265
fathom_url: https://fathom.video/calls/539497469
share_url: https://fathom.video/share/oryR2o1LbRs4RxdNKC3sJMzsEtPmXXbU
source: fathom

## Participants

| Name | Email | Organization | Role |
|------|-------|--------------|------|
| Ademilade Shodipe-dosunmu | ademilade@growthx.ai | GrowthX | Content Operations Lead |
| Rachel Pasche | rachel@growthxlabs.com | GrowthX Labs | Content Operator (new) |

</metadata>

---

## Summary

Ademilade onboarded Rachel to Cresta's end-to-end content production workflow, covering draft generation in Atlas, refinement using the Adira checklist in Claude, and publishing in Webflow. The session detailed three article types with different post-processing timelines (regular: 35 mins, competitive/nuanced: 45-60 mins) and established review processes with editorial and product teams.

---

## Context

Rachel Pasche is new to the Cresta content operations team at GrowthX Labs and needed comprehensive onboarding on the complete content production pipeline. Ademilade Shodipe-dosunmu, who has been managing the Cresta account for two weeks, walked her through the entire workflow from ideation to publication. This session establishes the operational foundation for Rachel to begin producing content independently, with emphasis on Cresta's specific positioning requirements around human-agent augmentation and competitive differentiation. The workflow relies on a carefully calibrated set of tools (Atlas for generation, Claude with the Adira checklist for refinement, Airtable for tracking, and Webflow for publishing) and depends heavily on embedding Cresta's unique voice and positioning philosophy throughout the pipeline.

---

## Relevance

**For GrowthX Content Operations:**
- Establishes repeatable, documented workflow for new team members on the Cresta account
- Clarifies decision points for article quality (when to publish vs. re-submit for major revisions)
- Identifies future improvements (embedding Adira checklist in Atlas, competitor positioning artifact, policy bar documentation)

**For Content Quality & Differentiation:**
- Emphasizes Cresta's unique philosophy (human-agent augmentation first, then automation) as a core differentiator in nuanced articles
- Establishes time allocation strategy: regular articles (35 mins) vs. competitive articles requiring manual competitor positioning (45-60 mins)
- Defines the Adira checklist as the primary quality gate, catching 85-90% of issues

**For Cresta Client Success:**
- Clarifies review process: editorial review (Nikki K-O-I) handles content quality; product review (Nikki K-K-I/Oran) handles positioning accuracy
- Documents feedback handling: minor edits go straight to publish; major rewrites (e.g., incorrect competitor lists) trigger re-submission with Slack notification
- Provides Rachel with documented checklist and operating manual for ongoing reference

---

## Overview

**Core Workflow:** Generate drafts in Atlas using the "ASCII generation with stats" pipeline, refine in Claude using the Adira checklist for quality control, track progress in Airtable, then publish in Webflow with proper HTML formatting for tables and full-width image sizing.

**Post-Processing Time Varies by Article Type:**
- **Regular articles:** ~35 minutes (standard concept guides, listicles)
- **Competitive articles:** 45-60 minutes (requires heavy manual correction of competitor positioning)
- **Nuanced articles:** 45-60 minutes (requires injection of Cresta leadership insights to enforce their unique philosophy)

**Critical Webflow Publishing Requirements:**
- Format all tables as HTML embeds (use Claude for Markdown-to-HTML conversion)
- Always select full-width image size option to prevent layout errors
- Use stock images from Unsplash as placeholders for covers
- Pull images from two sources: IQ Series research charts or Cresta product page diagrams

**Review Process:** Drafts move through Airtable statuses: "Drafts for Review" (editorial by Nikki K-O-I) → "Product Team Review" (product by Nikki K-K-I or Oran) → "Ready to Publish." Minor edits can go straight to publishing; major rewrites require re-submission and Slack notification.

---

## Key Topics

### Content Production Workflow

#### 1. Draft Generation (Atlas)

- **Pipeline:** Use "ASCII generation with stats" (improved version; ignore the earlier pipeline)
- **Prompt Structure:**
  - `Overview`: The topic
  - `Word Count`: 1,800-2,500 words (longer is better—easier to cut than to add)
  - `Goal`: Restated topic
  - `Topics to Cover`:
    - Run a quick Perplexity search: "Analyze top-ranking articles for [keyword]. We want to write [article type]. What gaps should we fill?"
    - Edit the outline offline for relevance before pasting
    - Always include "Prefstar CTA" to ensure call-to-action generation
    - Consider adding "TLDR" to start if desired (post-processing may handle this)

- **Output Quality:** Usually good, integrates case studies well (e.g., Holiday Inn Club Vacation example for coaching feedback)

#### 2. Refinement & Editing (Claude)

- **Tool:** Paste Atlas output into "Cresta's Outliner and Output Editor" (Pod 0 in Design Strategy Sprint)
- **Primary Instruction:** Run through the Adira checklist
  - This checklist catches 85-90% of issues
  - Includes metadata, specificity, positioning consistency, and customer outcome guidelines
  - Contains good examples for reference

- **Common Manual Edits:**
  - Remove AI-isms: "in this article," "changes the equation," "it's important"
  - Contextualize statistics: Add commentary explaining the "so-what" effect—don't just cite data, explain what it means for the reader
  - Ensure cohesion throughout the piece

#### 3. Publishing (Webflow)

- **Access:** Cresta CMS link (in strategy sprint, Pod 0)
- **Navigation:** Log in → CMS → Guides
- **Content Fields:**
  - `Name`: H1 title
  - `Slug`: Keyword
  - `Category`: Select from dropdown
  - `Cover Image`: Stock image placeholder (Unsplash); will be replaced later

- **Tables:**
  - Webflow requires HTML embeds (native Markdown tables break layout)
  - Process: Markdown table → Claude (request HTML conversion) → Copy HTML → Webflow HTML Embed element

- **Images:**
  - **Sources:** IQ Series research charts (Notion/Woodrocks) or Cresta product page diagrams
  - **Critical:** In Webflow, select the full-width image size option. Default (smaller) size breaks layout.

### Review & Feedback Process

**Airtable Workflow:**
- `Drafts for Review`: Editorial review by Nikki K-O-I (checks content quality, clarity, flow)
- `Product Team Review`: Product review by Nikki K-K-I or Oran (checks positioning, competitive accuracy, Cresta philosophy alignment)
- `Ready to Publish`: Final status before publishing

**Feedback Handling:**
- **Minor Edits** (small info gaps, clarity tweaks): Fix and move directly to "Ready to Publish"
- **Major Rewrites** (incorrect competitor list, misaligned positioning): Move back to "Drafts for Review," re-submit to product team, and notify via Slack
- **Example:** One competitive article incorrectly listed competitors and required full rewrite

### Article Types & Post-Processing Time

**1. Regular Articles (~35 mins)**
- Standard concept guides, listicles, how-to guides
- Process: Atlas → Claude Adira refinement → ready for review
- Lower feedback rate; mostly minor adjustments

**2. Competitive Articles (45-60 mins)**
- **Challenge:** Atlas tends to misposition competitors; requires heavy manual correction
- **Inputs:** Manually curate competitor list before running (5 mins research)
  - Pull from Notion competitor list and refine for topic specificity using Perplexity
  - Different topics may require different competitor subsets based on pain points
- **Pipeline:** Use "agency competitor pipeline" (has Cresta's competitive guidelines embedded)
- **Future Improvement:** Create a dedicated artifact mapping competitor positioning by cluster/pillar to automate this

**3. Nuanced Articles (45-60 mins)**
- **Example:** "AI for Every Contact Center Agent" (Cresta's dual human-agent augmentation approach)
- **Challenge:** Requires deep research to enforce Cresta's unique philosophy (human augmentation before automation)
- **Process:** Inject insights from Cresta leadership (CEO podcasts, internal docs) into Atlas output to raise quality bar
- **Result:** "Leadershipy" tone with Cresta's proprietary positioning
- **Future Improvement:** Create post-processing step or artifact capturing Cresta's unique philosophy by topic cluster

### Assignment Strategy

**Goal:** Balance priorities and commercial interests.

**Weekly Mix:**
- 1-2 High Priority topics
- 1-2 Medium Priority topics
- 1 Low Priority topic
- Always include at least one topic with commercial/revenue intent

**Logic:** Prioritization table includes priority level and search volume; Cresta approves high-priority topics for SEO impact.

---

## Action Items

**Ademilade Shodipe-dosunmu:**
- Add Webflow CMS link to Cresta operating manual
- Send Rachel the editorial checklist + operating manual (link this recording)

**Rachel Pasche:**
- Download the Claude Cresta Outliner/Output Editor from Pod 0 (Design Strategy Sprint) to your personal pod
- Review materials and test the pipelines
- Schedule follow-up meeting for next week for progress review and article feedback

---

## Transcript

**Ademilade Shodipe-dosunmu:** How are you?

**Rachel Pasche:** Good. Sorry, I'm getting myself set up. So for the Cresta production stuff, do you think it's easier? I mean, I'm sure you probably have like a process. Um, did you just want to like share your screen maybe and like walk me through everything that you're doing?

**Ademilade Shodipe-dosunmu:** Okay. I think that's like, most of this is going to be detailed in like, the operation manual. But like, I think it's also important for you to have it, because like I will link this exact video in the operation manual as well. Um, like this call rather. Okay. like, at any point if there's something that doesn't make sense or you can't get really clear, just let me know if you need to jump in. Okay, I'm trying to figure out where I want to start from. Oh, I'm just going to, yeah, let's just go to Atlas. Okay, so we have Atlas here, then also a table. Okay, that's the keyboard, okay. I'll just walk you through, like, a table, then I'll do Atlas, then I'll show you the cloud projects and, like, the post-processing and, like, questions. Okay, that sounds good, sorry. I'm gonna move. Dogs are bugging me.

**Rachel Pasche:** Okay, gotta get away from them.

**Ademilade Shodipe-dosunmu:** So different views in the article. I think this is pretty much a standard set of a couple of time views because it does go through two phases of reviews. So you have the "Drafts for Review" stage here, which is essentially when we're done, we just send it to this status. And this is where the senior content marketing manager takes a look. So she just checks editorial stuff. So that's Nikki with a K-O-I, not to be confused with Nikki K-K-I.

**Rachel Pasche:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, yeah, yeah. Because the K-K-I Nikki is the product person, one of the product people actually. So when like Nikki is done, we send it to the product team review here. And that's how the two product people know that they're supposed to take a look. And once they're done, you probably would leave a couple of comments. And once you're able to fix those, it's typically in two ways. If it's like little stuff, like most of the feedback we get these days are like small things or like just information we didn't have before. So if it's like little stuff, you don't really need to flag them again. After you fix it, you can move it straight to publishing and just publish. However, if it's like major stuff, because like there were like I think two articles so far, one of them I didn't work on. I don't know who worked on it. I think it was during Christmas. I wasn't on the account at the time, but it was sent back because apparently Atlas had conflated a couple of pieces of data and essentially put the wrong competitors on the list. So the entire article was like literally off. So we had to be fully rewrite. So for that one, I had to send it back when I was done working on it. So it was like a major thing. Yeah, definitely send it back and like ping them. Maybe you can ping them on Slack or something, but they are pretty responsive.

**Rachel Pasche:** Okay.

**Ademilade Shodipe-dosunmu:** Yeah, once that's done, it's off to "Ready to Publish." There's just one here because I was literally publishing before this call. But yeah, we publish in Webflow. Do you have, I'm guessing you have experience working with Webflow?

**Rachel Pasche:** Yeah.

**Ademilade Shodipe-dosunmu:** Okay. Let me just quickly show you the Webflow setup. Once you have the link, it's in the strategy sprint slogan. So that's Pod 0. So, I'll add these details to the operating manual as well. Once you have it, you just log in, press that CMS and you go to guides, not categories, but guides. This is the software that I'm publishing in. Everything else is pretty basic. Webflow stuff. The name, which is your H1, slug, which is the keyword, then the category, the cover image. This is a question mark for now. We are using stock images right now. So those will eventually get replaced, so we just use stock. I just get them from Unsplash, really, and put them there. They're just placeholders for now. Okay. The other thing is for tables. Since you have Webflow, you need to format it in HTML. You're familiar with that yet?

**Rachel Pasche:** No, but I'll figure it out, I guess.

**Ademilade Shodipe-dosunmu:** I mean, you could just... So tables don't format properly in Webflow. I don't know why, you have to put them as HTML code. So you can literally just probably copy an example, but one of these... You can just put it in Claude and paste your table in Markdown to convert it for you. So that should be good.

**Rachel Pasche:** Oh, okay.

**Ademilade Shodipe-dosunmu:** Yep, pretty much. So when you want to add a table, you just come here and go to HTML embed, and I'll be good to tell you the code in there.

**Rachel Pasche:** Yep.

**Ademilade Shodipe-dosunmu:** Yeah, so that's Publishing, and that is Airtable. Now for like Pipeline stuff. I have like, I create this for like every client pretty much. So it's just like resources from a checklist as well. I've only had this account for like two weeks. So there's not that much here. I've had to just do a little like balancing, sort of trying to balance the state of the account. But the links are all here, but all of this is in Notion already. I just add stuff here that I find useful just because I prefer Woodrocks to Notion. So I'd just come here.

**Rachel Pasche:** I agree.

**Ademilade Shodipe-dosunmu:** Right. There's like some other stuff here. I'm trying to figure... Okay, case studies. This is also in Airtable. And this is the editorial checklist, which we'll get to in a moment. So now pipelines. There are about two major pipelines we use for Cresta. Actually, three. But this "ASCII generation with stats" is the improved version of this one. So you can just use this. What I do is actually run both. I've been running both of these in parallel because this was just given to me this week. So I've actually been running both of them in parallel and comparing the results. And sometimes I pick bits from here and bits from here and I merge them. But yeah, this one is pretty good now. So I don't think you have to do that. But I had to do that this week because I was with you just testing pipeline. So this is the basic article chain. But like regular articles. So this applies to... Oh, I missed something in our table. Sorry, this is... So like for... For content type, it's pretty much self-explanatory. Like once you see the topic, you know whether it's a regular listicle or a how-to guide or, I don't know why we have how-to guides twice, but yeah, and you know whether it's like an expanded definition or a comparison post. Like it's pretty clear which it is based on the title. I just wanted to flag this. So back to this is, the process is pretty much coming in here. So like for agentic, like everybody has like best practices for agentic. Some people say don't put outlines, some say put outlines, some say make it skeletal. Honestly, you can find like what works best for you. But what I've found that actually works is using this format. This format works pretty well. So honestly, you could just copy this. You can test this, copy that, like, fill in blanks. So what I do here is just overview. By turning word count is usually, I usually change this to 1,800 to 2,000 words. I try to make it, the article should typically be around 1,800 to 2,500 words. That's like the average length I've been getting for some of these, some a bit shorter. I usually prefer longer articles than, like it's easier to cut stuff as opposed to one article that's too short and you have to figure out. So that's why I try to increase it a bit. Goal, you can just like put the topic here. And for topics to cover, what I do is I just run like a quick Perplexity search. So asking it to scrub. It's not even like a really elegant prompt or anything. I just ask it something like, "Analyze ranking articles for this keyword. And we want to write this type of topic for, and you know, what do we need to outperform what's currently there. Like what are the gaps?" I give it an example of like, okay, hey, this is like a directional, like this is what I want, like just the headers to cover. And I put like a prompt like this into Perplexity, and it generates like an outline. Once it generates that, I have to edit that offline, because sometimes some stuff is going to be relevant. But yeah, I just edit that to make sure I have what I need. Then I just paste the topics here. Yeah, that I want to cover, and always add "Prefstar CTA." I don't know, for some reason, sometimes when I add this, it adds the CTA properly. Sometimes it doesn't, like, I don't know why that happens. But yeah, probably need to enforce something in the guidelines. Then for topics to cover, we always have a TLDR. So sometimes I would like start here with like, TLDR, so you know, but yeah. Sometimes I don't, because the post-processing workflow takes care of this. So yeah. That's honestly it, and I run, it does pretty well. The output is usually pretty okay, but it's not perfect, as you can imagine, but it does a good job of like integrating the case studies. Like for example, this Holiday Inn Club Vacation is a really good case study, like it relates directly to this coaching feedback. So what I do is that I take these outputs as is, and I put it into Claude, so let me get the Claude, let's get the Claude more clear, so my other screen, okay, so I bring it here to Claude, and this is "Cresta's Outliner and Output Editor" for Claude. So this is the Pod 0, Design Strategy Sprint, so I guess you have to move this to your pod, so you probably have to download it. You see? It's a bit of an unknown task. Yeah. Sorry about that. But this is updated. Like, I updated this just yesterday. So everything here, this is like your source of truth for artifacts. And Atlas is also updated, by the way. So both of them are all the artifacts and across both are updated. And in Notion as well. So they're all fine. And all I really do here is a few things. I already have the Adira checklist in here. So I just literally tell it, I paste the Adira and tell it to run through the Adira checklist. And at least it catches like probably like 85 to 90% of the issues with the content. So it's really good at doing that. I haven't had more time with this account. If not, I would have put this into Atlas itself. But I've sort of just been trying to deliver. So that's why. But now that I... This process, and also I've been trying to perfect this checklist. So now that the checklist is in a really good spot, you can probably file a ticket to implement this into Atlas. So this is the checklist itself. Where did go? Okay, here you go. So this is pretty much it. Just like metadata, specificity, stuff like also for it to adapt to like how Cresta positions itself because sometimes Atlas sort of sways or deviates a little bit. So just like to reinforce some certain things and also to give it like a guide on how to reference customer outcomes as well. So yeah, it's pretty long. So I just, and here's some good examples of how to do certain things here. So I just run that against the existing content here. And sometimes... I add some additional instructions to remove some common AI-isms, so things like it not being MISI, for example, or the typical blah, blah, blah, "changes the equation," those regular AI-isms. So I may just add some instructions, though it doesn't usually add a lot of those. The thing I find myself adding, even on top of this checklist, is just to make things cohesive, and to contextualize statistics. Yeah, that is something that's more recent. So sometimes, I don't know why, but sometimes what Atlas would do with statistics is that it gives you these statistics, and, oh, hey, according to, it might do that to make a point, which can make some sense. However, it fails to contextualize that information. So what I mean is that it doesn't usually give enough commentary. Like, okay, you've given me these stats. Like, okay, I can sort of see how it relates to the core pain points. However, there's not enough contextualization, so we need to drive the points home. So, like, it's giving, like, a lack of the "so-what" effect. So, yeah, something like that. So, yeah, I find myself, like, adding instructions there. So, okay, contextualize all statistics as well. And when I give those instructions, the output is usually fine from Claude. Right now, post-processing for regular. Now, like, I'll put articles into three buckets. So, first bucket is regular articles. Maybe it's, like, just general concept stuff or maybe, oh, examples of blah, blah, blah feedback that might not be too crazy. Those ones can probably take me now about 35 minutes of post-processing. That's when it leaves the pipeline. The second bucket is competitive articles. Those ones are a bit high. Cresta just has ways they want to talk about these competitors and all the instructions are already in Claude and also in Atlas, but sometimes it just requires a bit more massaging because sometimes the Atlas doesn't position them the way they should be positioned, right? So ideally what I think needs to be done and what I would probably do is by the time I write like maybe two or three more like competitive or comparison posts, I would develop an artifact related specifically to competitor standpoints like what makes them unique across common clusters or pillars or ICP pain points so that Atlas can pull that in and map them appropriately. Yeah, that's probably what I'll do. Yeah, so but like I've not written enough of these to create that yet. I think I've written probably three complete competitive pieces so far, and one of them was a rewrite that someone else did, so just three, because it's been two weeks on this account. So what else? Then the third bucket, so yeah, so those articles can take probably like 45 minutes to an hour for post-processing, yeah, but like, we've been doing like one of those every week, so I usually keep that one last, because it just takes so much time, but yeah, 45 minutes on hour, it can be shorter, probably if, like, we iron out a couple of these, like, things that I brought up, probably can come down to like 45 to 34. That's where it currently is at. And you find that typically these articles are where you get more feedback from, because of this, this competitor stuff, and like, they may just say, oh yeah, like, yeah, I don't want to position these guys as this, like, especially on it this way instead. So there's just some, like, really nuanced stuff that you might not just really, maybe get right off the bat. So that's fine. They will get very direct feedback. So you're going to get insights on how to make it better. So no worries there. Then the third bucket is nuanced articles. So these are articles, for example, let me find one. I worked on one this morning. Let me quickly jump into my slot. So something like this is nuanced. I don't know why. I hate when this happens. Okay. So it's pretty much something like this. So like "AI for Every Contact Center Agent." And Cresta has like a unique... They're not here and they're there just sort of somewhere in the middle because Cresta's approach is to first augment what human agents are actually doing and before anything like automation, right? So it's like a unified platform for AI agents and human agents so that they have like a dual approach to it. And because of that, articles like these can take to the beginning, maybe as long as competitive pieces, maybe like 45 minutes there about for post-processing just because they have unique takes on it. For this one, for example, and like their quality bar for this type of articles might be a bit higher. If we dive into our table for this one now, let me just go to stairs and pick this. So the VP of products literally left a comment saying, "Good topic, we need to own this. Take the company position." Yep, pretty much. So, you know, that already reinforces that, okay, hey, why not, this isn't the typical "what's the internet saying about it" type of article. They really want to enforce their own unique and nuanced take. So for this one, I had to just do a bit of digging. I found like this podcast that like your CEO shared some insights about like something related to this and like how Cresta approaches it. Then combine that with my post-processing workflow. I just injected insights from this podcast into that to just raise the quality bar. So I injected quotes and just the general rationale and philosophy from that podcast with my Atlas output as well. And, you know, I think it turned out fine. But, yeah, you know, it reads very "leadershipy." Yeah, for lack of a better word. But yeah, these kind of, like, by the time, like, we have, like, enough of these topics, like, in the database, we can probably create another artifact that just sort of aligns to, like, oh, hey, Cresta's unique philosophy on certain topics. And, like, maybe it may not, because, like, because we don't do so many of these types of topics, like, I've been on the account for two weeks, and I've done probably, like, two of these. Yeah, so these type of articles. So, it might not necessarily have to be an artifact. It might just be, like, it might not be an article, it might just be a post-processing step, just like, "oh, unique stamp, blah, blah, blah, blah, blah," and just, like, inject it after you're done with the article or something like that. Well, you know, you can probably figure out, like, your best way of doing that. And I think that, honestly, is it. It's the only new thing is, we started adding. This today, like, a status up here, because it goes through the editorial review and product review stages. So once the Nikki is done with editorial review, she'll just, like, mark it, like, done. Then once the other Nikki or Oran is done with product review, they'll just mark it done, and, like, we can move it to publishing after that. And so that's mostly, yeah, that's mostly if you have, like, questions so far.

**Rachel Pasche:** Um, I saw, like, if you scroll down, I see you have, like, yeah, images. Where do you get those from?

**Rachel Pasche:** Okay, great question.

**Ademilade Shodipe-dosunmu:** Um, so images are typically from two places. So if you come here to, like, resources to this checklist, this was a list of, like, they had, like, this IQ series, essentially. First, I have this IQ series where they do internal research and they get just a bunch of really interesting charts that talk about different things. For example, if you're writing a coaching article, you can probably integrate something from here. Another way to inject unique insights from their existing stuff into your own work. So yeah, sometimes I take images from here if it relates and you can find proper applications. Alternatively, I get from product pages. What is just something that I'm talking about with product pages? For example, let's quickly go to, let's say, Cresta, sorry. Let's start the bureau diagrams or something. Something like this. I can literally just pull this, if it makes sense, and inject it into the article. Thank you. So, the only thing is when you're doing this in, when you're publishing in, what do you call it? In Webflow, you need to, let me just create a track for this one that I was publishing. Oh, one sec. Okay. I think this one had the, okay, this one had images. So, for example, when you're publishing this one in Webflow, you want to make sure it's here. So, normally, it's going to default to this first one, which is a smaller image size, which looks weird on the platform, but you want to make sure it's this one, the full-width one, but that's the only thing.

**Rachel Pasche:** Cool.

**Ademilade Shodipe-dosunmu:** I'm sure I'll have more questions. So, one more thing. That's like the basic pipeline, and then the second one is the agency competitor pipeline. This is the exact same process. The only difference is the writing guidelines in this pipeline is different. The writing guidelines has been sort of injected with Cresta's competitive article guidelines. So they have particular way they want to talk about competitors. They don't just want to do like a feature-on-feature mashup because of, like I mentioned, it's a fast-moving industry. So today's features are into most features pretty much. So yeah, that's the major difference. The only other thing I've found that's really important to get right in this is making sure in your inputs, you have, now I've got a bit more detail in this one because I just want to be able to control what it gives me, especially here, like in this list of competitors. Always give it a list. Like you may have to do like maybe some five minutes of research. The faster you get, anyways, but like five minutes to figure out like what are the big popular competitors, because Atlas doesn't always get it right. So you have to put your own list. But yeah, that's the only other thing that I didn't mention.

**Rachel Pasche:** Do they have like a list of their competitors or do you have to like pull it up based on what you find in Perplexity in like Google?

**Ademilade Shodipe-dosunmu:** There's like a competitor list in Notion. However, like you can pull from that and also put that injector into Perplexity to sort of analyze based on the particular topic, because that is like a general list of competitors. So depending on like the pain points that you're trying to compare them, like the competitor list might change as well.

**Rachel Pasche:** Yeah.

**Ademilade Shodipe-dosunmu:** Yeah, that makes sense.

**Rachel Pasche:** Um, hmm. Okay. I wish I had more questions, but I don't have any yet. Probably once I do it, I'll be messaging you next week with a few things. But right now, nothing's coming to mind.

**Ademilade Shodipe-dosunmu:** Sounds good. DMs are always open. Please ask and I'll take a peek at your articles next week. So feel free to send them over. For assignments, I usually, I mean, you and Bailey can come up with your own process, but I typically would, at the beginning of the week or at the end of the previous week, I would kick like a couple of articles that are here and are ready to start. I take them based on priorities. So now we have more of low priority topics. I actually did compare priority and like search volume. But like, as you can see, we have more low priority topics. But I think they are proving a couple more. So by the time they approve those. Things should be better. So if you take like one high priority or two high priority, then maybe one or two medium, then one or two low, I mean like one low or two, depending on what's available. And I always add at least one list that has like commercial interests. I really can't figure out how you want to crop out a lot, but that's pretty much it. If you have any questions, I could basically leave a slot, and I don't know if you're up on it this week, but if you want to sort of play around with the pipelines, you're free, even though next week works as well.

**Rachel Pasche:** Okay, great. Sounds good. And maybe we'll set up, maybe I'll set up like a meeting next week or something, like once I'm in there, and then you can like review my stuff. Like if I've had, you know, have anything in progress and like tell me what maybe I'm missing or like what I should focus on more, if that works.

**Ademilade Shodipe-dosunmu:** Got a jump, but I would have the editorial checklist and operating manual to you later today, and you can go through that as well.

**Rachel Pasche:** Cool. Thank you so much, Ade.

**Ademilade Shodipe-dosunmu:** No problem. Have a good one.

**Rachel Pasche:** Thanks, you too.

**Ademilade Shodipe-dosunmu:** Bye.

**Rachel Pasche:** Thank you.
