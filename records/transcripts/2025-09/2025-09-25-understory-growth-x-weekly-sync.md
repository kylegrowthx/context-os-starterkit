# Understory <> Growth X - Weekly Sync

<metadata>
date: 2025-09-25
time: 15:29 UTC
duration: 21 minutes
organizer: team@growthxlabs.com
participants: Ali Yildirim, Sydney Arin Go, Alex Fine, Aida Knezevic, Katya Luscomb
fathom_recording_id: 89834449
fathom_url: https://fathom.video/calls/420448735
share_url: https://fathom.video/share/Lvs7ndaVVHEUSBGbBhScEY-kNHAXvUTU
source: fathom
enriched_on: 2026-03-03 09:30 UTC
</metadata>

---

## Summary

Understory and GrowthX discussed major progress on blog migration and content scaling: Sydney announced the blog migration to Next.js and Sanity will complete Friday with a Monday go-live target, while content production scales to 5 articles per week starting next week with a focus on cold calling and Allbound marketing topics. The team also reviewed Scrunch AI analytics tracking ~190 prompts and ~3,000 responses across competitors, with plans to add more competitive data (RefineLabs, GrowthEngineX, C17 Labs, The Kiln, Conversion Labs, OmniLabs) and set up Looker reporting combining GA4 and Google Search Console data to track LLM referral traffic.

---

## Context

Understory is a B2B agency specializing in end-to-end deliverability management and omnichannel marketing (outbound, paid search, paid social). GrowthX is providing content marketing and AI visibility services to help Understory launch a blog and establish thought leadership in the Allbound (combined paid+outbound) and cold calling spaces. This weekly sync is part of ongoing engagement to build content, track AI visibility via Scrunch analytics, and manage technical website infrastructure. Katya Luscomb is newly introduced as a co-lead on the GrowthX delivery team, working with Sydney Arin Go on content production.

---

## Relevance

**To GrowthX Delivery:**
- New team member (Katya) integrated on content delivery; operating under tag-team model with Sydney for scaled production
- Blog migration to Next.js/Sanity/Vercel framework demonstrates technical SEO expertise; client will own all assets post-migration
- Content tone refinement workflow: single "proof article" (What is Allbound Marketing) to be reviewed for consistent messaging across 5+ weekly articles
- Cold calling and Allbound marketing identified as initial content focus areas; scaling to 5 articles/week next week

**To CheckThat / AI Visibility:**
- Scrunch AI analytics integration active: tracking ~190 prompts, ~3,000 responses to establish baseline before content launch
- Planned competitor expansion (RefineLabs, GrowthEngineX, C17 Labs, The Kiln, Conversion Labs, OmniLabs) to track mentions across LLMs
- Looker reporting setup pending Google Search Console access; will track LLM referral traffic by blog post and LLM type (ChatGPT, Claude, etc.)
- Client pain points (outbound deliverability, inbox landing) are addressable via LLM prompts; potential content angles for AEO

**To GrowthX Business Development:**
- Account expansion: engagement scaled from strategy to execution (content production + website infrastructure)
- Client commitment visible: approving articles weekly, setting up analytics infrastructure, planning 5-article/week cadence
- Blog go-live Monday positions Understory for thought leadership in Allbound space; potential reference case for similar B2B agencies

---

## Overview

- Blog migration to Sanity/Vercel/Next.js completing Friday; go-live target Monday pending content approval
- Understory's website currently has security vulnerabilities; migration will resolve these and improve the editing experience
- Content production scaling to 5 articles/week next week; tone refinement via review of "What is Allbound Marketing" article
- Scrunch baseline: tracking ~190 prompts and ~3,000 responses; expanding competitor tracking to 6+ agencies
- GA4 access confirmed; Google Search Console access pending; Looker report to track organic traffic and LLM referrals once GSC is live

---

## Key Topics

### Team Introduction and Content Progress

  - Katya introduced as new account co-lead at GrowthX
  - One draft ready, another planned for delivery this week
  - Revisions made to calibration article (added HockeyStack, Fibbler mentions)

### Blog Development and Migration

  - Migrating to Next.js and Sanity for improved security, speed, and usability
  - Migration completion expected Friday; blog can go live Monday post-approval
  - Ali raised concerns about access; Sydney to confirm details on code/hosting

### Content Strategy and Priorities

  - Waiting on "What is Allbound Marketing" article review to refine tone
  - Scaling to 5 articles/week next week; focus on cold calling content initially
  - Sydney to send list of planned topics for next batch of articles

### AI Analytics with Scrunch

  - Tracking \~190 prompts, \~3,000 responses, monitoring competitors
  - Team to add more competitors (RefineLabs, GrowthEngineX, C17 Labs, The Kiln, Conversion Labs, OmniLabs)
  - Aida to confirm max number of competitors that can be tracked

### Client Pain Points and Differentiators

  - Common issues: failed outbound efforts, inbox deliverability problems
  - Understory differentiators: end-to-end deliverability management, specialized teams for paid search/social

### Analytics Access and Reporting

  - Team has GA4 access; awaiting Google Search Console access
  - Plans for Looker report combining GA4 and GSC data, including LLM referral analysis

---

## Action Items

**Ali Yildirim (Understory)**
- Review "What is Allbound Marketing" article, focusing on tone, messaging, and style to establish brand voice for scaled production
- Follow up on Google Search Console access setup and inform GrowthX team when access is ready

**Sydney Arin Go (GrowthX)**
- Send list of 5 planned content topics for next week to Ali for pre-approval before writing

**Aida Knezevic (GrowthX)**
- Contact Scrunch team to confirm competitor limit and add new competitors: RefineLabs, GrowthEngineX, C17 Labs, The Kiln, Conversion Labs, OmniLabs
- Double-check GrowthX team's access to Understory's GA4, resolve any access issues
- Follow up on Google Search Console access and set up Looker report once GSC is provisioned

---

## Transcript
**Ali Yildirim:** How are you?

**Ali Yildirim:** Hey, everyone.

**Aida Knezevic:** Hi.

**Alex Fine:** We've got a full team today.

**Alex Fine:** Ada, Sydney, yeah, everybody.

**Aida Knezevic:** Yeah, yeah, I mean, I was able to make it.

**Aida Knezevic:** Sorry I couldn't be here last week.

**Aida Knezevic:** We've got a ton of progress to share today on your blog.

**Aida Knezevic:** I Sydney, can go and share your screen just to walk them through.

**Sydney Arin Go:** Yeah, but before we dive in, I wanted to introduce Katya to you guys first. She's going to be co-leading the account with me. Katya, do you want to introduce yourself a little bit?

**Katya Luscomb:** Yeah, hey everybody. I'm excited to be joining GrowthX and to be on your account. I've got a variety of content experience, and I've been digging into your content and blogs this week. Really excited to help develop it.

**Alex Fine:** Awesome.

**Katya Luscomb:** Great to meet you.

**Sydney Arin Go:** Katya and I were tag-teaming on your content this week, and she is awesome.

**Sydney Arin Go:** I'm excited for you to see the work she's done. Let me share my screen.

**Aida Knezevic:** Yep, we can see it.

**Sydney Arin Go:** Awesome.

**Sydney Arin Go:** So last week, we started transitioning content production to Katya. We already have one draft ready for you this week, and we're planning to deliver another one. We made revisions to the calibration article that I sent over a couple weeks ago—added HockeyStack and Fibbler mentions as you requested, and cleaned up the tools list in Airtable.

**Sydney Arin Go:** The biggest update is that we're migrating to Next.js and Sanity. It will work the same visually, but be secure, straightforward, faster, and easier to use. The editing experience will be much better than WordPress. This migration will solve the tech SEO issues I was concerned about early on. Fair warning—I just got to the Philippines and I'm a bit jet-lagged, so I might be a little slow today.

**Sydney Arin Go:** All of your content pages will exist in Sanity/Vercel/Next.js. The migration will be done on Friday, and as soon as we get approved articles, we can launch the blog, which should be by Monday.

**Alex Fine:** Sounds good.

**Sydney Arin Go:** If you have questions, I'll do my best to answer, but I may need to field it through our designer and get back to you. He's very responsive though.

**Ali Yildirim:** The main thing is access—if we want to make changes or have our designer adjust the site, how can we access and edit things?

**Sydney Arin Go:** Good question. This will all be in Next.js code, so you'll have full access to edit it as you like. Hosting will be on Sanity at about $15 a month per user—roughly the same as what you're paying WP Engine for WordPress. But you'll have full access to everything, and after migration, you'll own it all.

**Sydney Arin Go:** I'll keep you posted on all the blog migration progress.

**Sydney Arin Go:** The goal is to go live by Monday or as soon as we have content approved and ready to publish. This week's priority is the "What is Allbound Marketing" article review. We really want to refine your tone because when we scale to five articles per week next week, we need to make sure we're not amplifying any mistakes across all the content.

**Sydney Arin Go:** If you can review the "What is Allbound Marketing" article—it has a lot of your tone, messaging, and style. That feedback will be the best use of your time, and we can apply it to the other articles we plan to deliver, and retroactively edit the ones we've already done. Katya has been ensuring all blog posts include tool mentions with details on how you use them from our Airtable sheet. If you want to add more tools, let me know—the more, the better. So we're just waiting on that article feedback, and that's all our updates for the week.

**Ali Yildirim:** Awesome.

**Ali Yildirim:** So you said you're waiting on us to review the Allbound article, and I sent back revisions on the calibration article. Is that one going live, or is it just for tone?

**Sydney Arin Go:** It's both. The calibration article will probably be the first or second thing we publish. Ideally, I'd like to publish the "What is Allbound Marketing" article first since it's closer to your brand messaging. Then the next batch of articles will be around cold calling so we build traffic and authority in that niche, then we go back to Allbound marketing content. That way we're telling a coherent story.

**Ali Yildirim:** Yeah, that makes sense. So we just need to review the Allbound one. And for the next five pieces of content, what are those?

**Sydney Arin Go:** They'll come from your Understory Content OS—anything you've marked as an approved idea.

**Sydney Arin Go:** We'll start with the most relevant to your brand, but if you have priority articles you want to start with, we'll do those. I'll send you the list of topics we plan to write after this call so you can tell me if any don't seem like good priorities.

**Ali Yildirim:** That would be good to know, since we'll need to approve those five articles before you publish them, right? So we have eyes on the ones you're planning to release starting next week?

**Sydney Arin Go:** Yep, I'll send those over.

**Ali Yildirim:** Speaking of analytics—you mentioned you're using Scrunch, right? Is now the right time to get a baseline before we kick off, so we can see how things change from today onwards?

**Aida Knezevic:** Yeah, let me share my screen. We have your Scrunch dashboard pulled up. We're tracking close to 190 prompts and about 3,000 responses so far. We have your direct competitors listed here, and we can add additional ones. We can also add more prompts, especially if there are questions that come up frequently in your sales calls with prospects.

**Aida Knezevic:** That's helpful because we reverse engineer prompts from audience personas—what questions would they ask an LLM? Direct insights from your sales calls help us identify those.

**Ali Yildirim:** So what exactly do you need from the sales calls?

**Aida Knezevic:** If there are questions that come up repeatedly when you're talking with clients—not just to find a service, but to solve challenges they're dealing with.

**Ali Yildirim:** So in the context of what they'd be searching for?

**Aida Knezevic:** Yeah, exactly.

**Alex Fine:** The most frequent conversation starter is people saying they had an outbound motion that didn't work, they have no idea how to land in the primary inbox, deliverability is a nightmare, and they're not getting motion from their outbound campaigns. That's probably 70% of our conversations. The second part is: how do you differentiate versus other generalist paid media agencies that focus on search, social, and all those channels? How do you have expertise across multiple channels? Our answer is two things. One, we manage deliverability and email infrastructure end-to-end. Two, for paid media, we have specialty teams—a paid search team and a paid social team. That builds trust with clients. People don't realize that paid media is really multiple specialties, not one bucket. Specialization goes a long way in delivering real success. We have both teams in-house for paid media, plus a separate team for demand generation and outbound. We harp on expertise, not generalism.

**Aida Knezevic:** Okay, okay.

**Ali Yildirim:** For an LLM, it could be questions like: What is Allbound? How do I do Allbound at my company? How do I build an Allbound strategy? How do you combine paid media and outbound? What are example plays or frameworks you can use?

**Aida Knezevic:** Yeah, totally. That's helpful.

**Aida Knezevic:** We have the prompts here, and they're automatically grouped into different topics so we can see how the data changes over time. If we click on a topic, we can see all the prompts we're tracking and assess whether they're on the right track or if there's anything to change.

**Alex Fine:** I sent over a list of all the prompts, as well, in a Google Sheet, so that if you want to take it off the call, you can also check on it afterwards.

**Alex Fine:** Yeah, this is so cool.

**Alex Fine:** Yeah.

**Alex Fine:** This is so cool.

**Alex Fine:** So it's showing Directive Consulting appeared 48% of the time for "marketing agencies with strong track records generating qualified leads." Super interesting. Ali, should we add RefineLabs? How many competitors can we track?

**Aida Knezevic:** I need to check with the Scrunch team. We have a shared channel, so I can follow up.

**Alex Fine:** We'd like to add some outbound-focused competitors—GrowthEngineX, C17 Labs, The Kiln...

**Ali Yildirim:** And Conversion Labs.

**Alex Fine:** Right, Conversion Labs. And probably OmniLabs too.

**Aida Knezevic:** I'll check with them. We can definitely add more competitors—I've seen even larger lists. When we click on individual prompts, it shows performance across different LLMs. One thing I'm seeing is that Claude tends to have fewer brand mentions than other LLMs. For a lot of our clients' Scrunch data, Claude isn't the highest referrer.

**Aida Knezevic:** We should have access to your Google Analytics 4, right?

**Sydney Arin Go:** I think we have GA4 access, but not Google Search Console unless it changed.

**Ali Yildirim:** We're in the process of setting that up. Let me check on it.

**Aida Knezevic:** I'm 99% sure we have GA4 access. I was having some dashboard access issues, so I'm checking. Once we have Google Search Console access, we can set up a Looker report merging both platforms into a multi-page report showing organic traffic, referral traffic, and a specific page focused on LLM referral traffic. You'll see which blog posts get the most traffic from different LLMs and which LLMs are the biggest referrers. It's mostly ChatGPT for obvious reasons, but we'll track all of them. We also have a page analyzing your GrowthX content performance compared to the rest of your site.

**Ali Yildirim:** Let me check and I'll follow up as soon as I know about Google Search Console.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Is there anything else you'd like to discuss today?

**Ali Yildirim:** I think that's it for my side. Alex, anything on your end?

**Alex Fine:** Nothing on my side. I'm super excited to go live next week.

**Ali Yildirim:** Same here. I really appreciate you taking on the website too—it's been the elephant in the room.

**Sydney Arin Go:** Our designer flagged some security issues on your site. The migration will solve that problem.

**Ali Yildirim:** Awesome.

**Aida Knezevic:** Great. Thank you so much. I'll follow up regarding Google Search Console in a couple of days and double-check the GA4 access as well.

**Ali Yildirim:** Sounds good.

**Aida Knezevic:** Thank you. Bye.

**Katya Luscomb:** Bye. Nice to meet you all.
