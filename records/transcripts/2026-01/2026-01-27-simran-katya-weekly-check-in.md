# Simran / Katya Weekly Check In

<metadata>
date: 2026-01-27
time: 17:49 UTC
duration: 44 minutes
organizer: Katya Luscomb (katya@growthx.ai)
participants:
  - name: Simran Sethi
    email: simran@growthx.ai
    affiliation: GrowthX
    role: Content Strategist
  - name: Katya Luscomb
    email: katya@growthx.ai
    affiliation: GrowthX
    role: Content Operations Lead
fathom_recording_id: 117512100
fathom_url: https://fathom.video/calls/545142724
share_url: https://fathom.video/share/yn_Qy5ywarzitUZKoaWM17LuqWp7d8MK
source: fathom
enriched_on: 2026-02-28 18:45 UTC
</metadata>

---

## Summary

Katya and Simran aligned on critical pipeline improvements for Udemy (addressing factual errors and excessive jargon), formalized Simran's ownership of the Understory Sanity publishing workflow, and plotted a strategic expansion toward keyword research ownership. The conversation emphasized batch feedback over isolated tickets, standardization of content calendars across accounts, and building Simran's capacity for strategic content planning.

---

## Context

This check-in occurs at a pivotal moment in the GrowthX Udemy engagement. Udemy's renewal conversation is scheduled for early February with high-level strategy talks, making Q1 content quality critical. Internally, the team is standardizing content operations across clients (including a "Week" column in calendars for clarity), and preparing to scale content ownership from management to execution roles. Understory is introducing auto-publish workflows and new service lines (LinkedIn thought leadership), requiring operational changes. Both projects sit in a transitional state: the Udemy pipeline needs debugging before scaling, and Understory needs systematic categorization to enable site navigation features.

---

## Relevance

- **Pipeline Quality Control:** For anyone tracking Udemy content strategy or reviewing Claude post-processing workflows; relevant to engineering discussions with Nick about factual hallucinations and jargon in generated drafts.
- **Content Operations & Automation:** For teams moving to auto-publish systems; Sanity setup and metadata auditing are critical prerequisites.
- **Team Scaling & Ownership:** Documents the shift toward Simran owning strategic functions (keyword research, content calendar strategy) with Katya in review role—a model potentially replicable for other team members.
- **Traffic Analysis & Optimization:** Udemy's Looker dashboard integration and "referral" vs. "not set" definitions relevant to organic analysis and content refresh prioritization.
- **Keyword Research Standardization:** Simran flagged the need for pod-wide keyword research training; Katya committed to documenting approaches and proposing this for the next pod-wide call.

---

---

## Overview

- **Udemy Pipeline Issues:** The pipeline generates factual errors (e.g., a partnership misidentified as a case study) and excessive jargon. Simran will file a batch of tickets to provide comprehensive, actionable feedback to engineering.
- **Understory Publishing Workflow:** Simran now owns the Sanity publishing workflow. The immediate task is to audit all published articles and add missing categories to enable the site's new filtered navigation.
- **Strategic Expansion:** Simran will take on keyword research for Understory next week, building toward full ownership of content calendar strategy. A keyword research training session will be proposed for the next pod-wide call.
- **New Udemy Reporting:** Simran now has access to the Udemy Looker dashboard and will add weekly URL updates to the workflow. The "referral" and "not set" traffic sources will be included in organic analysis, as they capture LLM and un-attributed organic traffic, respectively.

---

## Key Topics

### Udemy: Pipeline Issues & Strategic Context

  - **Pipeline Quality Issues:**
      - **Factual Errors:** The pipeline invents details, such as misidentifying a partnership with BetterWorks as a case study.
          - **Significance:** This is a critical bug, as it creates content that is factually incorrect.
      - **Excessive Jargon:** Drafts still require significant post-processing in Claude to simplify technical language (e.g., AWS, cloud computing).
  - **Feedback Strategy:**
      - Simran will file a single, comprehensive ticket with engineering (Nick) after this week's edits are complete.
      - **Rationale:** A batch of feedback provides a clearer, more generalizable picture of pipeline behavior than isolated, one-off tickets.
  - **Strategic Context:**
      - Udemy's renewal is in April; high content quality is essential for February strategy talks.
      - **New Content Formats:** Infographics are being introduced to create AI-friendly snippets. Simran will file tickets to integrate them.

### Understory: New Publishing Workflow & Content Audit

  - **Sanity Publishing Workflow:**
      - Simran now owns the Sanity publishing process, replacing Suleman.
      - **Rationale:** The auto-publish feature requires a new owner for post-publish checks and manual adjustments.
      - **Process:** Log in via 1Password → `Posts` → Verify all metadata (title, slug, excerpt, category, author, image alt text) and formatting.
  - **Immediate Task: Content Audit:**
      - **Goal:** Audit all published articles in Sanity to identify and add missing categories.
      - **Rationale:** This enables the site's new filtered navigation, improving user experience and content discoverability.
      - **Method:** Export a list of all posts from Sanity and use Claude to cross-reference with the original assignments.

### Process & Strategic Alignment

  - **Content OS Standardization:**
      - The "Week" column in the content calendar will be standardized across all accounts.
      - **Rationale:** This improves organization, clarifies review cycles for clients, and simplifies internal tracking.
  - **Keyword Research & Strategy:**
      - Simran will begin keyword research for Understory next week.
      - **Goal:** Build toward Simran owning the content calendar strategy, with Katya reviewing.
      - **Action:** Simran proposed a pod-wide training session on keyword research, which Katya will consider for a future call.
  - **Udemy Looker Dashboard:**
      - Simran now has access to the Udemy Looker dashboard.
      - **Weekly Task:** Update URLs in Looker for each new batch of content.
      - **Traffic Source Analysis:**
          - **"Referral":** Include in organic analysis; it captures LLM traffic (e.g., ChatGPT, Claude).
          - **"Not Set":** Include in organic analysis; it is a frequent bucket for un-attributed organic traffic.

---

## Action Items

**Simran Sethi (GrowthX)**
- Track Udemy Claude post-processing; file Eng tickets to Nick (GrowthX Engineering) re: jargon, fake stats, secondary keywords
- File Udemy tickets re: AI summaries, tables, infographics/FAQs
- Add Sanity publishing steps to pipeline doc
- Audit Understory Sanity posts: add missing excerpts/categories; verify slugs/formatting; check each auto-publish
- Export Understory Sanity posts; run Claude to tag missing categories
- Update Claude post-processing for Udemy: numbered jargon issues; apply selected edits
- Add weekly Udemy Looker check to recurring tasks

**Katya Luscomb (GrowthX)**
- Add Understory category tags to pipeline doc
- Generate Udemy assignments through week 20; then Simran updates calendar
- Ask Udemy team re: pillar pages/cluster alignment
- Schedule keyword research walkthrough (Udemy/Understory) w/ Simran
- Add Udemy 'Week X' review link to Monday update template

---

## Transcript

**Katya Luscomb:** I have kind of a tight timeline, so I'm going to blast through some of these things. First things first, I had flagged that for Understory, some of those pieces were missing excerpts. Thanks for helping me look into that—once we figured out they just ended up on the wrong draft.

**Katya Luscomb:** I will say, at this point, since I'm not reviewing the drafts, if it's easier for you and, like, creates less margin for error to just have one document that, like, you maybe start it in the internal folder and then move it to client-facing.

**Simran Sethi:** That is what I've done.

**Simran Sethi:** For Understory this time, instead of having two different drafts—because I was so confident it was there, but it wasn't—I'm starting with one internal draft and then moving it to client-facing. For Udemy, though, there's still quite a bit of heavy editing that I don't think they need to see, so I follow the internal draft and copy it into an external draft for them. With Understory, I'll just keep one draft.

**Katya Luscomb:** Ideally for Udemy, we get to the point where the pipeline doesn't need that kind of editing. Keep tracking things you're having to post-process in Claude because the better the pipeline gets in Atlas, the less time you'll need. But also, the more we export and post-process in Claude, the more likely we undo work Atlas is doing. I know they had questions about making sure secondary keywords are explicitly in the content, and if that's not part of Claude's process, it might take out those keywords without you realizing it. That's one of the things I filed in the ticket with Nick.

**Simran Sethi:** The ticket has been filed and we did all the fixes, apart from a couple things.

**Simran Sethi:** This is definitely a big improvement—drafts aren't coming out at 3,000 words anymore. I've generated about 10 drafts, and all of them are under 2,000 words, which is great. However, there's still a lot of jargon I'm struggling with. The subject matter is more technical—things like developer skills, tech scaling, cloud computing, AWS—because the team wanted those details. I gave Nick initial feedback that this is an improvement, but I want to go back with more specifics once I'm done editing for this week, so it's not just one or two isolated issues but a batch of comprehensive feedback.

**Simran Sethi:** There's another weird thing happening—either Claude or Atlas is generating random stats and case studies that have no basis in reality. For example, I was editing a blog and it said they have a case study with BetterWorks, but when I tracked it down, they just have a partnership with BetterWorks, which operates differently. Claude said this came from the draft I shared, but when I checked the original, it mentioned BetterWorks as a partnership, not a case study. Something happened during post-processing—it went from "BetterWorks is a partnership" to "we have a case study with BetterWorks."

**Katya Luscomb:** Yeah, that's a good catch. Part of it might be because one of the edits we're working on is incorporating case studies, and the pipeline might be trying to reach for those. That would definitely be something to flag for Engineering, and the earlier you can get those tickets filed, the better—it gives the team time to work on implementations before you have to generate another round of content.

**Simran Sethi:** I wanted to batch them so the feedback is more specific and not "this thing went wrong in this draft, that thing went wrong in that draft." That way they can generalize what the pipeline as a whole is doing.

**Katya Luscomb:** I don't know if you've chatted with Naina, but she has tricks to take the Atlas version and your final edited version, compare them, and create a checklist of problems so you're not manually tracking everything.

**Simran Sethi:** Yeah, I did that a while back.

**Katya Luscomb:** Cool, cool.

**Katya Luscomb:** Keep me posted on Udemy Progress for sure.

**Katya Luscomb:** I'm definitely leaning on you to, like, chase down those tickets and prioritize those.

**Katya Luscomb:** And I think I flagged they're up for renewal in April, which means that I'm having high-level strategy conversations with them early February.

**Katya Luscomb:** So the more we can push content quality and some of these pipeline changes through, especially, like, the AI-led summaries and making sure, like, tables and things are in there, the better.

**Katya Luscomb:** I think I've CC'd you on a ticket that Katya, the other Katya, is working on for some infographics.

**Katya Luscomb:** So that's something that works as well.

**Katya Luscomb:** And so basically what will, once that's ready and we have approval from their team on incorporating those, we'll want to try and vary articles that have either an infographic or a...

**Simran Sethi:** I just don't usually see the point of it.

**Katya Luscomb:** Well, and the point largely is that they enable snippets that AIs like to pick up.

**Katya Luscomb:** So if you can present a really interesting answer.

**Katya Luscomb:** And I don't think the assumption, like, we obviously want the FAQs to be helpful.

**Katya Luscomb:** And we also know that, like, it is kind of an LLM play.

**Katya Luscomb:** So there's a balancing act there, making sure that it resonates with the content and is something that could drive folks to those pages.

**Katya Luscomb:** So I I wanted to flag that that's something that I will probably ask for you to file some tickets around the end of this week or early next week.

**Katya Luscomb:** Sure.

**Katya Luscomb:** For Understory, the other big thing is I've outlined a couple of tasks. From last week's content, I want to go over how to publish. With auto-publish, you'll need to be familiar with Sanity to make adjustments since Suleman won't be supporting that anymore—this is going to be on your plate. The information is in Understory's documentation and should be added to the pipeline document. Basically, you go to Sanity, log in with the GrowthX Labs account via 1Password, and sign in with your email. It's very similar to WordPress, honestly easier.

**Simran Sethi:** Is it like WordPress?

**Katya Luscomb:** Yeah, I think it's easier than WordPress.

**Simran Sethi:** So once it's automated, do I just check every end of the week, or check every draft manually?

**Katya Luscomb:** For the first while, you'll want to check every draft to make sure all information ended up where it's supposed to be—that's why I wanted to do this walkthrough. Once you log in, go to Posts (the linear ticket link takes you directly to Understory's Workspace). The blog lives under Posts—you'll see all published content. A test post from the Atlas pipeline went straight to Publishing. I don't know if it'll create a draft you approve or always auto-publish. To make a new post, click the plus button for a blank template. Here's why metadata is critical: you put in the title, make sure the slug is there (never any backslash in the slug—that's really important), and paste the blog content.

**Simran Sethi:** Does it take the formatting from the draft, or do we have to ensure formatting is correct?

**Katya Luscomb:** It should take the formatting, but always triple-check. One thing you sometimes have to manually insert is tables—I haven't done that a lot since Understory content doesn't have many tables, but when there is a table, make sure you insert it. There's an SEO optimized title and SEO description. For articles with missing excerpts—I flagged three articles that were missing excerpts—that's where the excerpt goes. It should be short; I noticed some on their site are getting too long. Once you add it, the Publish button repopulates and you hit publish to republish the article. It won't make a duplicate, just update what's there.

**Katya Luscomb:** And then, so excerpt, the YouTube URL, this is only for those podcast articles.

**Katya Luscomb:** It, this basically just influences if a YouTube video gets embedded or not.

**Katya Luscomb:** Okay.

**Katya Luscomb:** We've got the cover image that has to get uploaded, as well as the alternative text.

**Katya Luscomb:** Make sure there's a date, author.

**Katya Luscomb:** It looks like this one maybe didn't have a category assigned either, so go ahead and double check the articles that you've got that the category is assigned as well.

**Katya Luscomb:** And then, if there's ever a topic, something you and I can work on, we want to rotate the featured article a bit.

**Katya Luscomb:** I know one thing, other story.

**Katya Luscomb:** story.

**Katya Luscomb:** Is really pushing, they're working on a launch for a new service where they're basically creating, like, LinkedIn thought leadership posts for companies to, like, curate their profile.

**Katya Luscomb:** I think I saw that also on their social, they were talking about that.

**Katya Luscomb:** Yeah, and so that's another piece we're going to want to start looking into.

**Katya Luscomb:** I think I generated some assignment ideas around it.

**Katya Luscomb:** If not, that's something that we should consider developing.

**Katya Luscomb:** Okay.

**Katya Luscomb:** And I did ask them for some talking points around how they're discussing that with clients so we can pull some of that perspective in.

**Katya Luscomb:** Maybe in another artifact or we can talk, if you want to talk to engineering or Panzer and Anastis, see if they've got tips on the best way to approach that.

**Katya Luscomb:** That would be helpful.

**Katya Luscomb:** Just so we're using as much of their voice and their messaging as we can for consistency.

**Katya Luscomb:** Okay.

**Katya Luscomb:** Okay.

**Katya Luscomb:** So.

**Katya Luscomb:** my.

**Katya Luscomb:** so.

**Katya Luscomb:** the

**Katya Luscomb:** make sense so far with Sanity?

**Katya Luscomb:** Yes, it does.

**Simran Sethi:** Cool.

**Katya Luscomb:** And then there's not, I haven't found an easy way to go from Sanity to the actual draft, so then if you ever need to grab the URLs, you'll go to their main website and then under resources.

**Katya Luscomb:** Part of the reason the category tagging is really important is because we've updated their site.

**Katya Luscomb:** So it's got the blog, which has all of their posts, and then it also separates out the podcast articles specifically, which the images on these are looking really good.

**Katya Luscomb:** And then the other piece, a project that we need to do that I would like your help with next week or the end of this week if you have time.

**Katya Luscomb:** If you'll notice, we've got a lot more categories than just these three, but these three are the only ones that we've actually tagged articles with so far.

**Katya Luscomb:** So what I would like you to do is an audience.

**Katya Luscomb:** It essentially of articles in Sanity.

**Katya Luscomb:** And I think we might be able to export, you can Google, like, if we can export the, like, Sanity's list, because it should export showing all the tags.

**Katya Luscomb:** And then we can look at what actually has a category assigned and what doesn't.

**Katya Luscomb:** And you can run that through Claude if you take the, like, all of the published assignments and flag, because, like, I see a lot of these, yeah, a lot of these are missing categories, which I know you do as part of your post-processing step.

**Katya Luscomb:** That is something, like, the, honestly, Atlas could probably learn how to assign a category, an author, based on some rules that we give it.

**Katya Luscomb:** So that might be another good optimization for you to work on in the next couple weeks.

**Katya Luscomb:** Because a lot of, like, the more we can automate this, and we're going to want to, we're going to want to do that.

**Katya Luscomb:** Anyway, for the auto-publishing, you're going to need to have that defined when writing the article.

**Katya Luscomb:** But basically, you should just be able to download this list of all the published content and maybe run through Claude and cross-reference what in this list has a category and what in Sanity from their download does not.

**Katya Luscomb:** I don't know the best way to get the actual excerpt from or export from Sanity, but I know there is a way to do it.

**Simran Sethi:** I can look into it.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Yeah, and then basically, we're going to need to go through and add categories to all the articles that are missing because the more we can create kind of a curated experience here with these categories, the more cohesive it's going to be.

**Katya Luscomb:** Also, these images are looking really cool.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And then the other optimization, we're going to start looking at doing some refreshes of content.

**Katya Luscomb:** I need to do a deep dive into...

**Katya Luscomb:** content that like was performing really well and maybe is dropped off in some different things.

**Katya Luscomb:** That's something that I'm going to be working on through February.

**Katya Luscomb:** And long term, part of what I'd like to do is like update a lot of these images, which will probably mean re-running.

**Katya Luscomb:** As you found in Atlas, like sometimes you just have to create an entire new line.

**Katya Luscomb:** You can't just re-run the image step if it's really old.

**Katya Luscomb:** And so sometimes I just, I make a new line and let it run.

**Katya Luscomb:** And then I paste in the finalized article and then do the image generation step.

**Katya Luscomb:** And that seems to get me a much better image.

**Katya Luscomb:** But we'll prioritize with content that we refresh first.

**Katya Luscomb:** And then much later down the road, we can come in and like update all of these.

**Katya Luscomb:** But you'll notice a lot of these here don't have categories assigned to them.

**Katya Luscomb:** Because if they did, you can see, let's see here.

**Katya Luscomb:** You can see the category listed.

**Katya Luscomb:** So like this one.

**Katya Luscomb:** GTM engineering versus podcasts versus paid media.

**Katya Luscomb:** So you can kind of spot check that way, but I think doing the download from Sanity is going to be the fastest way to cross-reference.

**Katya Luscomb:** Questions about that?

**Simran Sethi:** No.

**Simran Sethi:** Sounds good.

**Simran Sethi:** I think I should have both of this done by the of this week.

**Simran Sethi:** I just want to make sure that the deliverables are crossed.

**Simran Sethi:** Totally.

**Simran Sethi:** And then I can start working on it.

**Katya Luscomb:** So let me add category tags we want.

**Katya Luscomb:** Download.

**Katya Luscomb:** Sanity list.

**Katya Luscomb:** None.

**Simran Sethi:** Also, I need your help in making sure that we have a bit of...

**Simran Sethi:** I think as of now, the assignments that we have scheduled are only till like next week for Udemy.

**Simran Sethi:** Okay.

**Simran Sethi:** Okay.

**Simran Sethi:** Okay.

**Katya Luscomb:** The assignments are on the back burner with other things, but I should get more assignments to you by tomorrow—I know you're running short. I have a couple questions to ask them about pillar pages and cluster alignment so I can action a lot of those.

**Simran Sethi:** They're reviewing more technical content that's not AI-heavy this week. I'd like feedback on my approach. I have feedback from Jay and Justin that'll take 30-40 minutes to run through. I want to confirm: is it because nobody's looking closely, they think it's up to speed, or are there quality gaps I should know about so I can provide better feedback about the pipeline?

**Katya Luscomb:** Their team has been super busy—they're going through an acquisition—so they likely haven't had product experts reviewing. Jen was doing a lot of redundant information comments. I'd err on the side of assuming there are still quality gaps to fill rather than assuming it's polished just in case they get more time.

**Simran Sethi:** And I think that'll just help me out.

**Katya Luscomb:** Yeah, no, I definitely ask them on each call if there's like new trends that they're noticing.

**Katya Luscomb:** I know they've given us a lot of feedback on things like, you know, word choice and read.

**Katya Luscomb:** Readability and like sentence structure and things.

**Katya Luscomb:** So I would say prioritize making sure that those get really polished.

**Katya Luscomb:** then if they give...

**Simran Sethi:** There's still quite a bit of jargon that creeps in across all the drafts. Even after Claude post-processing, there's still stuff I have to double-check, and sometimes it just slips through.

**Katya Luscomb:** When you're post-processing in Claude, after it runs through the steps, you might ask it to change how it's post-processing—make sure this is reflected in Atlas. Say something like, "Scan this article for any terminology that's overly technical that an eighth grader wouldn't understand and flag it for me." Then you can manually review and tell it specifically which changes you want. Here's a trick I use: I say, "Number the issues and your recommended fixes, and I'll tell you which ones to action." It gives me a list of 10 or 15 things, and then in the next response I can just say, "Apply edits 1, 3, 7, 15—the others are okay." That's a really efficient way to get through those pieces.

**Katya Luscomb:** Long term, I'm hoping to get you involved in more keyword research. I think I'll have you start helping with Understory next week—I've got performance reporting to get done first. I'd love more strategic support so you feel empowered to build out the content calendar, understand the strategy and pillars we're executing, do keyword research, run new topics by me, and we can collaborate. Then you build out the content calendar and I review. I think that's a much more sustainable way forward for content production, so I wanted to flag this as something on my radar.

**Simran Sethi:** Happy to do that. I did keyword research for a couple of clients during the strategy sprint and a couple others on different projects. But I've figured out that people have very different approaches to keyword research.

**Simran Sethi:** Walk me through the usual process you follow on a next call on Tuesday or Monday, then I can replicate it.

**Katya Luscomb:** It'll vary a bit between Udemy and Understory. I've been doing it to make sure I understand the process I want to use. There are trainings in development, and I've asked for more training on keyword research to ensure I'm following company best practices. Because as you said, there are many approaches. I can give you a walkthrough of approaches I've found successful and Cloud projects set up that we can replicate for Udemy and Understory to support keyword research.

**Simran Sethi:** Should this be something we do for our next pod-wide call? I think it would be helpful for everyone, not just for Udemy and Understory particularly, but if everyone's going to have to do it.

**Katya Luscomb:** Absolutely. I don't know if I have time to put together something before the pod-wide call, but it's definitely something I want to address—I've been chatting with Felix about it too. One of the big things I'm going to talk about is standardizing the content OS.

**Katya Luscomb:** So looking at raw assignments—we started doing this for Udemy because it wasn't clear which week of content we were doing. I've added a "week" column so it's really clear they should review week 18, which is in your Monday updates. You can flag "week 18 content is pending review" and link to their template view. I have it separated so they can see the exact articles we expect them to review this week. I've pre-populated the content calendar with weeks and backdated a bunch. Once I add content two or three weeks out, you'll update it with week 21, week 22, etc. It makes organization super easy and gives us a better view of when we actually generated content. Because you and I have done so much work on these accounts, I'm going to have everyone use a content calendar view and automations like this for all accounts so we're all operating with the same framework. This week piece is another element for you to manage.

**Katya Luscomb:** Have you updated the URLs recently in Looker for this batch?

**Simran Sethi:** I did.

**Simran Sethi:** You did?

**Katya Luscomb:** Okay, cool.

**Katya Luscomb:** When you do that, if you can make sure, you can also like always make these.

**Simran Sethi:** Wait, this is Udemy, right?

**Simran Sethi:** We don't have access to these.

**Simran Sethi:** We do.

**Simran Sethi:** Oh my gosh.

**Katya Luscomb:** I thought I CC'd you in that.

**Katya Luscomb:** I'm so glad that I mentioned that.

**Katya Luscomb:** So they do have a.

**Katya Luscomb:** Looker.

**Katya Luscomb:** I am going to link it to you right now.

**Katya Luscomb:** We just got it set up last week.

**Katya Luscomb:** Okay.

**Katya Luscomb:** So if you can add that as a to-do for you each week as well.

**Katya Luscomb:** Sorry, I thought I had tagged you in the linear ticket.

**Katya Luscomb:** I might have missed it.

**Simran Sethi:** Sometimes my notifications go a little wonky and I just lose track.

**Katya Luscomb:** No worries.

**Katya Luscomb:** I know there's a lot to keep track of between like Notion and linear and Slack.

**Katya Luscomb:** But yes, there is.

**Katya Luscomb:** We have a looker so we can actually see how our traffic is doing, which like, honestly, not too shabby.

**Katya Luscomb:** Like if I look back at, oh yeah, that's a funky, there we go, like our cohort specifically.

**Katya Luscomb:** And then if we just do, let's see, we don't want any paid stuff.

**Katya Luscomb:** Like we're seeing some really good growth because we started publishing in November.

**Katya Luscomb:** And so this is one of the things I'm going to be looking at is like where, where are cohorts doing really well?

**Katya Luscomb:** So we could probably optimize like AI upskilling.

**Katya Luscomb:** We've lost some, some sessions here, especially from early in January.

**Katya Luscomb:** So like probably some opportunities to refresh and optimize content in those lanes, because that's the other thing we'll start to look at is how we're going through and refreshing content to keep performance high and not just developing that new.

**Katya Luscomb:** But yeah, I wanted to flag if you want to like play around in here and kind of see what's happening.

**Simran Sethi:** I have a question here, which is of course not related to the client as such, but more of like a technical question.

**Simran Sethi:** And if you go to session medium, it says, what do we usually define referral?

**Simran Sethi:** Good question.

**Katya Luscomb:** So this is actually something I've been chatting with Kyle about.

**Katya Luscomb:** referral is in Looker, the way we've got ours set up, this is largely your LLM traffic.

**Katya Luscomb:** So if ChatGBT or Claude or something sends it over, very rarely is it anything outside of that.

**Katya Luscomb:** So we pretty much always loop in referral traffic here because otherwise you're going to undercut yourself quite significantly.

**Simran Sethi:** Yeah, because I've seen an analytics and I think every organization just defines it differently.

**Simran Sethi:** And usually the way that I've seen is they'll mention referral traffic as traffic that they get from particular communities that they're investing in or just like any paid stuff that they do, which is outside of their ads and such.

**Simran Sethi:** Right.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** So in, in this case, like we, we want to include referral because has.

**Katya Luscomb:** We're otherwise, like, probably cutting out a lot of different sources.

**Katya Luscomb:** I'll go through and I'll cut out, like, paid social, direct, paid search, email, partner content, probably.

**Katya Luscomb:** We always want to include not set as well, because, like, it's unlikely that this is all, like, direct or paid.

**Katya Luscomb:** This is a frequent bucket that organic content ends up in.

**Simran Sethi:** Okay.

**Simran Sethi:** As far as these...

**Simran Sethi:** Why does it land in not set?

**Simran Sethi:** There's a whole bunch of different reasons.

**Katya Luscomb:** It could have to do with the way, like, their GA4 is set up for tracking.

**Katya Luscomb:** It could have to do with, like, people blocking cookies.

**Katya Luscomb:** There's all kinds of different reasons.

**Katya Luscomb:** And so, like, there's some here that are fairly obvious.

**Katya Luscomb:** Udemy's has a lot.

**Katya Luscomb:** so, like, these, when it comes down to, like, one view, I'm not really worrying about that, because that's not going to skew our view too much.

**Katya Luscomb:** But, like, paid search with, you know, 33,000 sessions, like, definitely going to cut that out.

**Katya Luscomb:** And if you ever update, not that you need to, like, be in here doing a bunch of this, but...

**Katya Luscomb:** If you take out the non-growthx URLs, it also significantly reduces where a lot of this content is coming from.

**Katya Luscomb:** So in that case, you can see, like, definitely makes sense to cut out direct and then CPC because that's another paid avenue generally.

**Katya Luscomb:** Really great engagement too, which is exciting. This is a much higher percentage than I see across accounts. Kudos for pushing the quality—it's been a lot of work.

**Simran Sethi:** Creating content is interesting, but another fun part is looking at Looker—the traffic and engagement are really interesting to break out.

**Katya Luscomb:** One other thing I think would be good to start doing: review the call recaps I post after every client call (though it doesn't always happen depending on priorities), and look over meeting agendas each week for questions about strategy shifts. You can search Fathom for Udemy or Understory to find recorded calls.

**Simran Sethi:** I follow your messages very closely with Udemy—I've been doing this since before the holidays after we sent a wrong batch of articles. I keep a close eye now.

**Katya Luscomb:** That was a really good catch. Hopefully the "week" column in our content OS will help prevent that. The fact that you're updating the Monday reports—since you're hands-on with content—will bring a lot more cohesion and consistency. We've definitely run over. I wanted to make sure we covered everything. Anything else on your radar you're concerned about or struggling with?

**Simran Sethi:** Not at the moment. Things are finally looking more stable. I'm not feeling like I'm playing catch-up every week. I'm looking forward to weekends where I can close the laptop and disappear.

**Simran Sethi:** Good, good.

**Katya Luscomb:** It sounds like a good opportunity to start having you do keyword research, given you're caught up and can take ownership of pipeline updates. One other thing: if you see quirks or oddities with the pipeline, keep me in the loop via our internal channel—flag it with a post like "Seeing this problem, not sure how to address" and CC Panzer and potentially Naina. I don't have capacity for deep dives.

**Simran Sethi:** I flagged a couple during my last call with Matthew. I noticed a few things but they weren't a pattern, so I didn't file tickets. Matthew went into inspection mode and basically said I was overthinking it. There were instances where prompts could've been more specific, but that helped clarify something I was concerned about: it takes an hour to generate one Udemy blog. Matthew said that's due to subject matter—as long as time is going into research and not drafting, there's no problem. If most time is drafting, then there are inconsistencies or contradictory prompts. He gave me some tips, but I haven't had a chance to try inspection mode yet. Very helpful call.

**Katya Luscomb:** Seek out that kind of support when you notice quirks for aspects you can tweak in the pipeline rather than getting engineering involved. That'll help us fine-tune and get pipelines in really good order. I sometimes take a minute getting back to you on concerns you raise or flag in documents, so I want to make sure we have the right channels.

**Simran Sethi:** Don't worry about that. I feel very supported. I'm thankful for how we work together and over-communicate. I'm comfortable DMing you if I need help.

**Katya Luscomb:** My big ask is to flag things in our internal channel. If it's content quality and pipeline-related, loop me in, but also loop in Panzer and file tickets so I can ensure you get the support you need—I have demands pulling me in different directions. I need to prep for a call this afternoon and strategy meetings with clients, but ping me if you need anything else.

**Simran Sethi:** Thank you so much for having me. Have a good day.
