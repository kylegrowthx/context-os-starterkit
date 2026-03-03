# Relay <> Growth X - Weekly Sync

<metadata>
date: 2025-09-18
time: 15:01 UTC
duration: 22 minutes
organizer: Erik O'Brien
participants: Erik O'Brien, Aida Knezevic, Nick White, Relay Marketing Team (Bethany Cantor likely), Dave White, Katie McCann
speaker_note: "Relay Marketing Team" speaker label represents a Relay team member attending the content review call. Bethany Cantor was listed in calendar invites but did not speak. Dave White and Katie McCann were mentioned as future content reviewers but did not attend this call.
fathom_recording_id: 88208542
fathom_url: https://fathom.video/calls/413879541
share_url: https://fathom.video/share/29QkfnxKHzmACN-vbH9vvc68mBhscuPr
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX and Relay aligned on content strategy details and the mechanics of collaborative content production. GrowthX presented 39 blog topic ideas in an Airtable content calendar for Relay's approval, and the team discussed which 5-10 initial topics to greenlight for production. Key decisions included using Airtable as the single source of truth, staging content in Relay's ContentStack CMS (with Relay handling final publishing), and integrating Relay's brand guidelines into GrowthX's in-house image generation pipeline. The team also planned to track Relay's content performance through Looker dashboards and AI visibility via Scrunch, plus explore ways to integrate compliance review into GrowthX's Atlas workflow to reduce friction on Relay's internal review process.

---

## Context

Relay Financial is a fintech client operating in the compliance-heavy financial services space. GrowthX was contracted to develop a content strategy and handle content production to drive organic traffic and visibility. Erik O'Brien leads the account as GrowthX's account strategist, while Aida Knezevic manages day-to-day execution as the managing editor. This weekly sync is the second meeting in a strategy sprint—the first meeting occurred the day before, and GrowthX has since updated their initial content strategy artifacts and completed keyword research.

The core challenge on Relay's side is compliance review overhead: financial products require extensive review before publishing, and Relay has already built an internal tool called ThreadGPT to streamline this. GrowthX is exploring ways to integrate compliance reviews into their own Atlas workflow to make the handoff smoother and reduce review cycles.

---

## Relevance

**To GrowthX Delivery:**
- Atlas workflow customization: Relay's compliance requirements are driving a request to build compliance review automation into GrowthX's Atlas—applicable to other regulated industry clients (fintech, healthcare, legal).
- Content calendar tooling: Confirmed Airtable as content OS with status tracking and keyword research visibility; also supporting client-side Notion calendars to prevent topic overlap.
- Image generation pipeline: GrowthX designer (Katya) will create examples using Relay's brand guidelines and stock image database, then add approval loop before adding to production workflow.
- CMS integration: Staging model (GrowthX stages, client publishes) is now standard; awaiting ContentStack access approval from Relay.

**To CheckThat:**
- AI visibility tracking: Scrunch setup beginning today to track Relay-relevant prompts; also building LLM referral dashboard in Looker to measure ChatGPT/Perplexity traffic to Relay's content and homepage.
- Prompt sourcing: Relay previously evaluated Profound (Scrunch competitor); Nicholas suggested pulling existing prompt data from internal tools and sales calls (Gong/Outreach) to seed Scrunch with Relay-specific queries.

**To GrowthX Business Development:**
- Account expansion signal: Client's internal tool development (ThreadGPT) and discussion of optimization for compliance reviews indicates operational maturity and budget availability for workflow improvements.
- Reference potential: Relay's multi-product architecture (with emissions, lending, tax, payroll mentioned) and fintech compliance context makes them strong reference for regulated-industry content plays.

---

## Overview

- GrowthX presented 39 blog topic ideas organized by content clusters (credit card management, expense tracking, etc.) in an Airtable content calendar for Relay's approval
- Relay identified products they do offer (emissions, payroll, tax) vs. future product roadmap; team to focus first on topics that map to existing products
- GrowthX and Relay aligned to approve 5-10 initial topics immediately to begin content production in the coming weeks
- Relay shared internal Notion content calendar to prevent topic overlap and communicated compliance review timeline constraints
- GrowthX designer will create featured image examples (graphics + text overlay style) based on Relay's brand guidelines and stock image database
- Looker dashboard and Scrunch setup in progress to track organic traffic performance and AI visibility (ChatGPT, Perplexity referrals)

---

## Key Topics

### Content Strategy and Artifact Updates

  - GrowthX updated artifacts based on Relay's feedback
  - Initial keyword research completed, resulting in 39 blog ideas for review
  - Relay to provide additional feedback on content strategy, particularly regarding product-focused clusters
  - GrowthX aims to have 5-10 topics approved initially to begin content production

### Content Calendar and Management

  - GrowthX uses Airtable as the "single source of truth" for content production
  - Relay maintains an internal content calendar in Notion to avoid topic overlap
  - No set publishing schedule for Relay due to compliance review limitations
  - GrowthX to set up automation in Airtable for content review notifications

### Imagery and Design Collaboration

  - GrowthX offers in-house designer to create featured images for blog posts
  - Relay to provide brand guidelines and examples for GrowthX's designer to work from
  - GrowthX to generate image examples for Relay's approval before implementing in the pipeline

### CMS Access and Publishing Process

  - Awaiting final approval for GrowthX's access to Relay's content stack
  - GrowthX will stage content, with Relay team handling final publishing
  - Dave and Katie from Relay will be responsible for content review

### Analytics and Reporting

  - GrowthX to set up Scrunch for AI visibility tracking
  - Looker dashboard to be implemented, connecting Google Search Console and GA4 data
  - Dashboard will track organic traffic performance, content clusters, and LLM referrals

### Compliance and Review Process

  - Relay has developed ThreadGPT for internal compliance reviews
  - GrowthX exploring ways to integrate compliance reviews into their Atlas workflow
  - Potential for collaboration on improving compliance review tools

---

## Action Items

**Relay Marketing Team (Bethany Cantor likely)**
- Review content strategy doc, add comments on product-focused clusters and any other areas

- Review Airtable content calendar and approve 5-10 initial topics to kick off production

- Share internal Notion content calendar with GrowthX team to avoid topic overlap

- Consult design team regarding stock images and brand guidelines for featured images; share database/guidelines folder with GrowthX

- Follow up on CMS access (ContentStack) approval for GrowthX team

**Relay Team (Nick White and others)**
- Contact Joseph regarding existing prompt data from previous AI visibility tool evaluations (e.g., Profound) to seed Scrunch with Relay-specific prompts

**GrowthX (Aida Knezevic)**
- Set up Scrunch tracking for Relay (happening day-of meeting)

- Build Looker dashboard connecting Google Search Console and GA4 with Airtable content clusters and LLM referral report

- Share designer (Katya) with Relay to generate featured image examples; prepare 2-3 variations for approval

---

## Transcript
**Erik O'Brien:** Absolutely.

**Erik O'Brien:** Yeah, I am your account strategist, and so I'll be working with you guys through the strategy sprint, and then we've also got Aida, who will be joining.

**Erik O'Brien:** She just joined.

**Erik O'Brien:** It was our managing editor.

**Nick White:** Nice.

**Aida Knezevic:** Hey, Nick.

**Aida Knezevic:** Hi, Nick.

**Nick White:** Nice to meet you.

**Nick White:** Likewise.

**Aida Knezevic:** I wasn't here last week.

**Aida Knezevic:** I was out on vacation.

**Aida Knezevic:** This meeting is being recorded.

**Aida Knezevic:** Basically, what I do at GrowthX is I work with Erik and the rest of the team to set up all of our new clients with the artifacts in Atlas and also to develop your initial content strategy.

**Aida Knezevic:** And then when we start generating content, I'm also here to make sure that the content quality is improving and that we're taking your feedback and updating the artifacts as well.

**Aida Knezevic:** And also because I know that you are in the financial space, we're also going to be working to create some custom artifacts for you just to make sure that all us...

**Aida Knezevic:** The compliance requirements that you have, that we're automating them as much as possible so that we can, you we don't have to do that many reviews on your end.

**Nick White:** Great.

**Nick White:** Does the team talk to you about ThreadGPT?

**Aida Knezevic:** I don't think so.

**Erik O'Brien:** I believe so.

**Nick White:** Basically, we've built a custom GPT to do compliance reviews for us.

**Aida Knezevic:** Wow.

**Aida Knezevic:** Okay.

**Nick White:** You know, we write something, upload it there, and it provides feedback, flex, you know, disclosures we need to add, stuff like that.

**Nick White:** So, yeah, perhaps there's some opportunity for us to, like, I don't know, work on bettering that together, create something new.

**Nick White:** I don't know.

**Nick White:** But, yeah, we've been just there where we've been working on this challenge on our side as well.

**Aida Knezevic:** Oh, right.

**Aida Knezevic:** Do you, I mean, is that an internal tool right now?

**Aida Knezevic:** Or?

**Nick White:** I don't know.

**Nick White:** Yeah, I guess so.

**Aida Knezevic:** Okay, right.

**Nick White:** Oh, look, the Relay Marketing Team is here.

**Relay Marketing Team (Bethany Cantor likely):** This was the cause of me being late. I was having Zoom technical difficulties, and I couldn't get signed out of the Relay Team.

**Relay Marketing Team (Bethany Cantor likely):** Sorry about that, guys.

**Aida Knezevic:** No problem.

**Aida Knezevic:** Do we have everybody here?

**Aida Knezevic:** Are we waiting on anybody else?

**Relay Marketing Team (Bethany Cantor likely):** I don't think Katie is able to make it today.

**Aida Knezevic:** I'm not sure about Bethany.

**Relay Marketing Team (Bethany Cantor likely):** Okay.

**Relay Marketing Team (Bethany Cantor likely):** I think we can move.

**Aida Knezevic:** I think we can go ahead.

**Aida Knezevic:** All right.

**Aida Knezevic:** Great.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So let me just share my screen really quickly.

**Aida Knezevic:** Okay.

**Aida Knezevic:** All right.

**Aida Knezevic:** So just to give you kind of a quick update on what we've been doing since we met last week.

**Aida Knezevic:** Um, so we've updated artifacts based on your feedback and all the documents.

**Aida Knezevic:** We also did a first round of keyword research to create an initial content calendar for you, and from here, we will pick out a couple of assignments to calibrate on during this, you know, these first couple of weeks, and then, obviously, once we, you know, start producing more, we will do, like, a bigger, round of keyword research to find even more assignments.

**Aida Knezevic:** So, one thing that I wanted to ask you, if you had any additional comments on the content strategy or on the artifacts, other than the one comment that you left in the content strategy related to product-focused clusters?

**Relay Marketing Team (Bethany Cantor likely):** I don't think so.

**Relay Marketing Team (Bethany Cantor likely):** I mostly was focused on the other three artifacts.

**Aida Knezevic:** To be honest, I would like to take another look at the content strategy.

**Relay Marketing Team (Bethany Cantor likely):** But yeah, I'll do that right after this meeting and see if there's anything else that I want to add there.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah, I mean, there was a question, yeah, right here.

**Aida Knezevic:** So related to kind of, yeah, creating like topic clusters around other products that you offer.

**Aida Knezevic:** And I think a lot of these topics can be, I mean, the themes can be folded into the existing topic clusters.

**Aida Knezevic:** For example, in our initial like first round of keyword research, were able to find topics like already related to like filing taxes and, you know, invoicing and payroll and things like that.

**Aida Knezevic:** So I think we can fold that into the existing clusters.

**Aida Knezevic:** We definitely want to, some of these products are more, how do I say, like I had a, we had a client before who was in the tax space.

**Aida Knezevic:** And the tax space, there are many keywords that are incredibly high volume.

**Aida Knezevic:** Very valuable, but they're incredibly competitive.

**Aida Knezevic:** So it's about finding like the right volume and the right level of competition so we can actually rank there.

**Aida Knezevic:** But that's something that we do when we're analyzing the SERPs.

**Nick White:** Okay, fair enough, Aida.

**Nick White:** And just so you're aware, lending, tax, and payroll are products we do not offer today.

**Aida Knezevic:** Yeah, yeah.

**Nick White:** We have emissions, but yeah, would be a lot more interested in focusing on kind of stuff that, you know, the capturing the demand that we can already, already fulfill.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** So I think, yeah, if you have any additional comments on the strategy, just feel free to leave comments.

**Aida Knezevic:** We can go back and like make changes as needed.

**Aida Knezevic:** So I shared a link and let me actually share a link to the agenda here as well.

**Aida Knezevic:** So that you can access the agenda.

**Aida Knezevic:** And also you will, I will send you the link to the content.

**Aida Knezevic:** So you should be able to access it via the link.

**Aida Knezevic:** If you have any issues accessing it, let me know, and we will just send you an email invite.

**Aida Knezevic:** So this is Airtable.

**Aida Knezevic:** It's the content OS in Airtable that we use as a content calendar.

**Aida Knezevic:** So this is kind of our single source of truth for all of the content that we create for you.

**Nick White:** So to give you a kind of- what is the single source of truth?

**Aida Knezevic:** The Airtable, so the content OS, like for- just for the content production, because it does get- just due to the volume, it gets very messy to track everything in Google Sheets.

**Aida Knezevic:** So this is a lot easier.

**Aida Knezevic:** So, yeah, this is- to give you kind of a breakdown of what- how it's organized.

**Aida Knezevic:** So we have a status tracker, and that kind of- right now everything's in backlog because we haven't approved anything.

**Aida Knezevic:** So these are all just the topics that we've identified and that we wanted to present to you initially.

**Aida Knezevic:** And then we've categorized all of them into topic clusters.

**Nick White:** Aida, do you intend to be sharing your screen right now?

**Nick White:** Yes.

**Nick White:** Okay.

**Nick White:** I'm not alone in not being able to see anything, right?

**Relay Marketing Team (Bethany Cantor likely):** I can see her screen, Nick.

**Nick White:** Okay.

**Nick White:** Sorry.

**Nick White:** Totally my fault.

**Nick White:** Sorry, Aida.

**Aida Knezevic:** Sorry for interrupting.

**Aida Knezevic:** Yes, user error.

**Nick White:** Continue.

**Aida Knezevic:** No problem.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Honestly, I'm a Google Sheets person, so I totally understand.

**Aida Knezevic:** But anyway, this is Airtable. The status column is right here.

**Aida Knezevic:** And then the topic clusters are all organized under the status.

**Aida Knezevic:** You can kind of expand them, and then you will see the titles.

**Aida Knezevic:** You have some title, like, you have some ideas here around, like, credit card management, expense tracking tips for small businesses.

**Aida Knezevic:** And then if you scroll to the right.

**Aida Knezevic:** You can find the status column, and as you're reviewing the blogs, you can just go ahead and change the ones that you think are good to approve to start.

**Aida Knezevic:** If you don't like something, you can just label it as rejected, and we like to keep the ones that are rejected just to make sure that we don't end up suggesting them again, and it also gives us a good idea of what kind of assignments you don't want to do.

**Aida Knezevic:** So, we have 39 assignments or blog ideas ready for your review.

**Aida Knezevic:** So, I think, you know, after the call, you can take a look and let us know what you think.

**Relay Marketing Team (Bethany Cantor likely):** Awesome.

**Relay Marketing Team (Bethany Cantor likely):** This looks great.

**Aida Knezevic:** Nice.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** And I think usually we try to get at least five to ten topics approved in the beginning so we have a nice batch for the next few weeks.

**Aida Knezevic:** Obviously, if you don't like any of them, please let us know.

**Aida Knezevic:** It's not a big deal at all—we'll just do another round of keyword research.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** And then you can also see, like, all the target keywords that we found here.

**Aida Knezevic:** Obviously, there are more keywords than there are assignments because some of them didn't make it.

**Aida Knezevic:** When we generated the assignment, we realized it wasn't a good fit just in terms of the audience that you're targeting.

**Aida Knezevic:** But this helps us keep everything in one place.

**Aida Knezevic:** I mean, it also lets you see the volumes and, like, the keyword difficulty of the keywords.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** And then another thing I wanted to discuss with you, obviously, like, you have the content review process.

**Aida Knezevic:** But I also know...

**Aida Knezevic:** That you're creating content internally, and I wanted to see if you're using any internal content calendars, like what's the publishing schedule?

**Relay Marketing Team (Bethany Cantor likely):** We just want to avoid any overlap in the topics that we're targeting.

**Relay Marketing Team (Bethany Cantor likely):** Yeah, I have a content calendar that I'm maintaining in Notion that I can share that has all of the topic titles there.

**Relay Marketing Team (Bethany Cantor likely):** So, yeah, I can certainly share that in our shared document space, and you guys can keep track of that.

**Aida Knezevic:** Okay, okay, perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** What's the, do you have like a set publishing schedule?

**Relay Marketing Team (Bethany Cantor likely):** We don't know, not right now.

**Relay Marketing Team (Bethany Cantor likely):** It's, you know, because of the limitations around like getting approval on stuff with our guidance, our compliance guidelines and things like that.

**Relay Marketing Team (Bethany Cantor likely):** We can't quite be that stringent about it yet.

**Relay Marketing Team (Bethany Cantor likely):** We're working towards something a little more structured, but no, right now, it's just kind of when we can get things out the door.

**Aida Knezevic:** Okay, okay, that makes sense.

**Aida Knezevic:** Just to let you know, Erik and I are going to be syncing with our dev team to see how we can build additional compliance reviews into the Atlas workflow. But we'll continue the conversation in the coming weeks, since you're already working on that internally—we just want to make it as easy as possible for you.

**Relay Marketing Team (Bethany Cantor likely):** Thanks.

**Aida Knezevic:** All right.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** So another thing that I wanted to discuss today is imagery.

**Aida Knezevic:** So we typically, just to make publishing easier, we generate featured images that go with every blog post.

**Aida Knezevic:** And we have a designer in-house who can set up an image generation pipeline that comes at the very end.

**Aida Knezevic:** So once we generate a draft, we run the image generator to create an image appropriate for the blog that follows the specific brand guidelines our designer has implemented. We've mostly done illustrations and graphics because we find AI-generated human imagery still looks a bit odd, so we try to avoid that.

**Aida Knezevic:** I know that your blog is, you tend to use stock images, and then with a text overlay, do you have, like, a database of stock images that you pull from?

**Relay Marketing Team (Bethany Cantor likely):** I believe we do.

**Relay Marketing Team (Bethany Cantor likely):** It might not be large enough that, you know, it would kind of fit our needs.

**Relay Marketing Team (Bethany Cantor likely):** This is something I can tap our design folks for to see what they can provide, because I would want them to have input as well on anything that we're generating to make sure it kind of aligns with, you know, with what they're doing.

**Relay Marketing Team (Bethany Cantor likely):** So, let me take that away.

**Relay Marketing Team (Bethany Cantor likely):** I'll dig up a folder for you to share as a starting point.

**Aida Knezevic:** Okay, okay, that'd be great.

**Aida Knezevic:** We can also do text overlays on abstract backgrounds with graphics, which looks really good. We've had other clients implement this workflow and they were really happy with it.

**Relay Marketing Team (Bethany Cantor likely):** They didn't have in-house designers—they were generating everything in Canva, but this workflow helped them stop using Canva and saved them a lot of time.

**Relay Marketing Team (Bethany Cantor likely):** So how would we approach getting that off the ground? Could you provide some examples we can work off of, or should I get our design team to share guidelines with you?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So I think what we would need are any, like a Figma file with any brand guidelines that you have or a Google Drive folder.

**Aida Knezevic:** I'll share that with Katya, our designer. She's out this week but coming back next week. She'll look at your blog and generate some image examples for you to review and choose from.

**Relay Marketing Team (Bethany Cantor likely):** And once you choose, we can add it to the pipeline.

**Aida Knezevic:** All right, perfect.

**Aida Knezevic:** And then I know that we're also working on getting CMS access.

**Relay Marketing Team (Bethany Cantor likely):** Is there anything else that you need from us to get us access to content stack?

**Relay Marketing Team (Bethany Cantor likely):** Yeah, great question.

**Relay Marketing Team (Bethany Cantor likely):** I followed up with our compliance guy who was supposed to be pushing this through.

**Relay Marketing Team (Bethany Cantor likely):** I haven't heard anything back.

**Relay Marketing Team (Bethany Cantor likely):** I just followed up again this morning to see what the status is on that.

**Relay Marketing Team (Bethany Cantor likely):** I'm waiting to get the final approval on ContentStack access from our compliance team. I followed up again this morning, so let me track that.

**Aida Knezevic:** To give you context, the CMS access is granted to one email address for our team—that's the primary account for Pod Zero, which is the team working with you right now.

**Aida Knezevic:** One member of our team will handle publishing—they'll stage the content and upload the featured image.

**Aida Knezevic:** Depending on what you're comfortable with, they can either publish it directly or stage it for you to publish later.

**Relay Marketing Team (Bethany Cantor likely):** We'd prefer they stage it so we can do the final publishing.

**Aida Knezevic:** For the content review process, we can set up Airtable automation to email reviewers. Who should we add—just you and Nick, or others?

**Relay Marketing Team (Bethany Cantor likely):** I assume it'll be me and Katie McCann—she'd be the other one to approve content.

**Nick White:** Either of us can jump in to approve.

**Relay Marketing Team (Bethany Cantor likely):** So let's plan for Dave and Katie as the two reviewers.


**Aida Knezevic:** In terms of next steps, we're setting up Scrunch today and also building you a Looker dashboard. Erik, did you mention the dashboard last week?

**Erik O'Brien:** I did not.

**Aida Knezevic:** The Looker dashboard connects Google Search Console and GA4 data in a seven or eight-page report. It helps you track organic traffic performance across your entire website and blog, plus a dedicated page for GrowthX content.

**Aida Knezevic:** You can see how our content performs compared to your other content. We also hook it up to Airtable so the topic clusters appear in Looker. That lets us see which clusters are performing better than others, so we can optimize on the fly.

**Aida Knezevic:** The final page is an LLM referral report. It pulls data from GA4 to show traffic coming from different LLMs like ChatGPT and Perplexity, which pages are getting the most LLM referrals, and which LLMs are the strongest sources.

**Aida Knezevic:** From experience, the homepage typically gets the most LLM traffic, but blog posts often show up too—sometimes surprisingly often. Combined with Scrunch reports, this rounds out your full AI visibility picture.

**Aida Knezevic:** I know Scrunch came up last week. Erik, did you ask if the team has any custom prompts they'd like us to track?

**Erik O'Brien:** Nope, not yet.

**Aida Knezevic:** Right, so we upload prompts into Scrunch that we think your audience might use to research or land on a platform like yours. We can generate these with AI, or we can use prompts you already have.

**Nick White:** Is Scrunch similar to Profound?

**Aida Knezevic:** It's pretty similar.

**Nick White:** So you have a relationship with Scrunch and can give us access?

**Aida Knezevic:** We're unable to give you direct access due to email constraints, but we'll share reports every week in our syncs.

**Nick White:** Dave, when we kicked the tires on Profound and other tools, did we pull down any data that could help us? It might be worth pinging Joseph about it to save us from guessing. I think that's a good place to start.

**Relay Marketing Team (Bethany Cantor likely):** Yeah, I'll follow up with Joseph on that.

**Aida Knezevic:** Some of our other clients pull common questions from their sales call recordings in Gong or Outreach, and we use those as prompts.

**Aida Knezevic:** So we'll need access to your content calendar, and I think that covers everything for today.

**Relay Marketing Team (Bethany Cantor likely):** Remind me how we get access to that Airtable board?

**Aida Knezevic:** I'll send you the link. You should be able to access it directly via the link.

**Aida Knezevic:** If you don't have any questions, you can review the Airtable, assignments, and content strategy. We're here if you need feedback or have questions.

**Relay Marketing Team (Bethany Cantor likely):** We'll see you next week.

**Nick White:** Thanks. Good to meet you both.

**Erik O'Brien:** See you next week.
