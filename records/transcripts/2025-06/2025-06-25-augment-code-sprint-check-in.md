# Augment Code Sprint Check-In

<metadata>
date: 2025-06-25
time: 16:28 UTC
duration: 36 minutes
organizer: george@growthx.ai
participants: George Haikal (GrowthX), Marcel Santilli (GrowthX), Sylvain Giuliani (Augment Code), Molisha Shah (Augment Code)
fathom_recording_id: 70491098
fathom_url: https://fathom.video/calls/335090905
share_url: https://fathom.video/share/xm32q99eyXxasMNmPaVUdsLWqTsxf8NU
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX and Augment Code aligned on four key marketing workstreams launching over the next 3 weeks: a redesigned codelibrary.ai with dark mode and MCP server integration, a curated engineering newsletter targeting skeptical senior developers, a bottom-of-funnel content strategy with a new /guides section on the website, and an education guide repurposing Daniel's internal course for legacy enterprise users. The team agreed to ship the codelibrary redesign as a "Trojan horse" to drive indexing and traffic before full optimization, prioritize the first article publication next week to start learning from organic performance, and coordinate with Augment's design and web teams on website changes and branding alignment for the newsletter.

---

## Context

This meeting brought together Augment Code leadership (Sylvain Giuliani, CEO; Molisha Shah; and George Haikal and Marcel Santilli from GrowthX) for a sprint check-in on Augment's product marketing and content initiatives. Augment Code is an AI coding agent competing in a crowded market against Cursor and other tools. GrowthX has been engaged as their content and growth strategy partner, handling the creative strategy, newsletter development, website content architecture, and go-to-market coordination. This meeting covered four major workstreams in various stages of completion: a major redesign of codelibrary.ai (an MCP server directory), launch of a weekly engineering newsletter with a skeptical-but-AI-forward angle, development of a bottom-of-funnel content strategy for augmentcode.com, and prioritization of an education guide for legacy enterprise users who are new to AI-assisted coding tools. The urgency is driven by a planned launch week in approximately 3 weeks.

---

## Relevance

**To GrowthX Delivery:**
- Defined clear content strategy architecture: separating product/company updates (blog) from educational SEO content (/guides or /library section). This avoids internal politics and allows different messaging tones for different audiences.
- Identified the "Trojan horse" approach for new content sections — launch first to drive indexing before optimizing for conversions. Applicable to future client SEO strategies.
- Established a newsletter model targeting experienced/skeptical developers with curated content, TLDR summaries, and skeptical analysis. Balancing brand voice with credibility — positioning as "filter, not hype" — is a replicable content model.
- Recognized the importance of monitoring multiple content sources: engineering blogs, respected personal blogs, Twitter influencers (Armin Sander, HashiCorp founder, Pragmatic Engineer), and established newsletters like SWIX's AI Engineering. Can be applied to other B2B SaaS newsletters.

**To Augment Code / Account Health:**
- Strong alignment on brand voice and messaging — Sylvain was explicit about not wanting a fully off-brand newsletter and toning down anti-code-gen skepticism. Shows engaged, detail-oriented leadership.
- Clear prioritization: education guide for legacy users is now a high-priority item for launch week (3 weeks out), indicating strategic need for onboarding content.
- Website coordination dependent on Chris (Augment's web owner) granting GrowthX access to the code repo. This is a critical blocker that's being resolved.
- Subscriber list for the newsletter: starting with 50k recent, valid emails from Augment's existing customer base via CustomerIO. Molisha is handling data export.

**To CheckThat / Strategic Partnerships:**
- No direct CheckThat mentions in this sprint, but the focus on skeptical engineers and quality content curation aligns with CheckThat's positioning in AI visibility and evaluation.

---

## Overview

- New version of codelibrary.ai launching, featuring dark mode, search functionality, and a leaderboard
- Newsletter concept developed, focusing on curated engineering content with a skeptical but AI-forward angle
- Content strategy being developed, with a focus on creating educational guides separate from the main blog
- Prioritizing the creation of an education guide based on Daniel's internal course for legacy enterprise users

---

## Key Topics

### CodeLibrary.ai Launch

  - New version going live with dark mode, search functionality, and leaderboard
  - Upload function for user-generated content in development
  - Full list of MCP servers available for use
  - Plan to create a version on mccode.com with one-click add to Augment Code
  - Content to be scrubbed of Cursor mentions for Augment-hosted version

### Newsletter Development

  - Concept: Curated content for experienced, somewhat skeptical but AI-forward engineers
  - Sections include full reads with TLDR takeaways, CTAs, and a "skeptical engineer's take" on AI news
  - Database of engineering blogs and respected personal blogs being curated
  - Aim to balance skepticism without being anti-code generation
  - Beehive account set up with capacity for up to 200,000 subscribers (aiming for 500,000)

### Content Strategy

  - Developing content OS with sample articles and topics
  - Focus on bottom-of-funnel content for the website
  - Plan to create a new section (e.g., /library or /guides) separate from the main blog
  - Need to set up Search Console access and analytics for baseline metrics
  - Goal to publish first article next week and start ranking from there

### Education Guide Priority

  - Repurposing Daniel's internal course on using Augment Code for legacy enterprise users
  - Aim to include as part of the upcoming launch week in about three weeks
  - Combine internal knowledge with insights from principal engineers who've gone through the process

---

## Action Items

**George Haikal (GrowthX)**
- Scrub CodeLibrary.ai content — remove competitor mentions (Cursor, Windsurf, Cloud Code) and generic installation instructions; rewrite for Augment one-click install focus
- Request Search Console & analytics access for augmentcode.com from Sylvain
- Coordinate with Chris (Augment web owner) to create new /guides or /library section on Augment Code website, duplicating blog structure and setting up sitemap for indexing
- Follow up by end of week on plan to repurpose Daniel's internal education guide for legacy enterprise users; combine with insights from principal engineers who've used Augment
- Ensure Kirkland or design engineer reaches out to Chris for repo access to set up the new website section

**Molisha Shah (Augment Code)**
- Compile & send subscriber list: 50k most recent, valid emails, not unsubscribed; include opt-in method, message history, open rates, and click-through rates
- Export two segments from CustomerIO for newsletter launch: (1) engaged subscribers with at least one email open, (2) valid email subscribers; start with 100k combined for Beehive account validation

---

## Transcript
**George Haikal:** This meeting is being recorded.

**George Haikal:** Molisha, how's it going?

**Molisha Shah:** Hey, how's it going?

**Molisha Shah:** I like your office setup.

**George Haikal:** You have to drop by sometime.

**Molisha Shah:** Are you guys in SF?

**George Haikal:** Yeah.

**Molisha Shah:** I live in Sunnyvale.

**George Haikal:** I used to live by Zanker Road and used to work in Sunnyvale.

**Molisha Shah:** I don't have a car, so my scope of Sunnyvale is restricted to everything close to a Caltrain or bus station.

**George Haikal:** Well, we have space in the office for people to come work.

**Molisha Shah:** Sounds good.

**George Haikal:** There he is. How's it going?

**Sylvain Giuliani:** Hello, hello.

**George Haikal:** What is going on, sir? You look a little tan.

**Sylvain Giuliani:** One week off with a panic attack keeps the tan going.

**George Haikal:** Well, that sounds good.

**Sylvain Giuliani:** How many note takers do we have?

**George Haikal:** We have AIs handling notes. Firing AI is really hard once it has thousands of videos of your most valuable meetings. It's extremely difficult to turn it off and migrate it.

**Sylvain Giuliani:** Molisha, do you have an AI, or are you the only one without?

**Molisha Shah:** I'm the only one without.

**Sylvain Giuliani:** Good on you. You're saving the planet by burning less compute. Let's get going.

**George Haikal:** Let's jump in. We got some fun things and fun surprises. A lot to share. We've got a ton of progress.

**George Haikal:** Let's jump in. The agenda is in Slack and chat.

**Sylvain Giuliani:** I'm opening it up.

**George Haikal:** Share your screen and we can jump in. But, drumroll please, check out the new version of codelibrary.ai that's going live.

**George Haikal:** So, feel free to click on that.

**George Haikal:** I think it should be open, but I'm not sure if it's open or if it needs a password.

**George Haikal:** No, that's good.

**George Haikal:** I'll change my share into a full window and I can run through.

**George Haikal:** Yeah, yeah.

**George Haikal:** But, we had our...

**Sylvain Giuliani:** I still don't see it.

**Sylvain Giuliani:** I need access.

**George Haikal:** We had our design engineer, George Main, and our entire growth team work on this.

**George Haikal:** So that this is as, I don't know what the right word is, as unique as possible for the product launch tomorrow.

**George Haikal:** So, we have...

**George Haikal:** Dark and dark mode, search functionality, search like React.

**George Haikal:** It's just like, everything is just like super, super clean, you know?

**George Haikal:** And then we created a leaderboard as well, which is pretty cool, I think.

**George Haikal:** And so it's still a work in progress, obviously.

**George Haikal:** It's not perfect, but I think this is like pretty cool.

**George Haikal:** And so the upload function, I'm not sure it's working now, but the idea is going to be other people will be able to upload it as well.

**George Haikal:** So we'll test out some user-generated content, and we feel pretty good that this is at a place where it would do decent, I think, on product time as a test, you know?

**George Haikal:** And then we also enriched the app out of the content.

**George Haikal:** And so we have the full list of MCP servers that you all can use as well, and we can help create a version of this on mccode.com.

**George Haikal:** Right away, essentially, you know, so it can be a really nice, like, one click to add to augment code as well.

**George Haikal:** Thoughts?

**George Haikal:** Reactions?

**Sylvain Giuliani:** So, I mean, a couple of things, like, you know, like we talked about last time, you know, let's treat that as an experiment.

**Sylvain Giuliani:** I'm going to see, like, you know, like right now, there's not nothing about augment.

**Sylvain Giuliani:** So, you know, I'm like, cool, let's do it.

**Sylvain Giuliani:** Like, let's see what happens.

**Sylvain Giuliani:** It's not going to help achieve our goals, right?

**Sylvain Giuliani:** But, like, so I'm down to see how it goes on product turns, and then we can launch more things.

**Sylvain Giuliani:** I think one thing here is, like, on our side, you know, we're launching kind of like a one-click MCP install.

**George Haikal:** I spoke to you last time.

**Sylvain Giuliani:** We are delaying the launch right now internally because we're going to do, like, a partner launch with, like, Redis, Mongo, Figma, things like that.

**Sylvain Giuliani:** So it's, like, it's going to take a bit more time for us to coordinate that thing.

**Sylvain Giuliani:** But, like, hopefully we can do it in, like, two weeks or three weeks.

**Sylvain Giuliani:** I think at that point, it will be nice.

**Sylvain Giuliani:** is to go back to the code library and do the one-click install and augment button.

**Sylvain Giuliani:** So that's one.

**Sylvain Giuliani:** Like I said to you, we'd love to get access to that data, like dump it in front of Sanity.

**Sylvain Giuliani:** And so we have the same data set of MCPs.

**Sylvain Giuliani:** So we can launch part of the easy MCP launch.

**Sylvain Giuliani:** I want to have a list of all the MCPs you can one-click.

**Sylvain Giuliani:** So if we can reuse a lot of work there, that would be super beneficial.

**George Haikal:** That's already packaged for you.

**Sylvain Giuliani:** And we can help with the design if you want on your site.

**George Haikal:** But if you already have the directory, great.

**George Haikal:** But if you need us to mock it up in your brand, we're not going to do that.

**Sylvain Giuliani:** Okay, let's try that later.

**Sylvain Giuliani:** I'll check what it is.

**Sylvain Giuliani:** think the only thing that I was going to bring up on this MCP and just asking is like, is there a way that like the version on our website is without like mentioning cursors?

**Sylvain Giuliani:** Like.

**Sylvain Giuliani:** Basically, the only instruction that you need is, like, the one-click install.

**Sylvain Giuliani:** So, like, I was looking at the content that you have, right?

**Sylvain Giuliani:** Obviously, you are listing all of the install and instruction from, like, the readme, right?

**Sylvain Giuliani:** From the repo.

**Sylvain Giuliani:** And, like, all of the repos are just, like, yeah, you know, like, copy-paste this in windsurf, cursor, cloud, like, you know, it's just general stuff, right?

**Sylvain Giuliani:** Yeah, we can scrub it and essentially rewrite all the descriptions. The augment-hosted version of that data set — we replace all the Cursor, Windsurf, Cloud Code mentions, find and replace with Augment, and remove any competitor installation instructions as much as we can.

**George Haikal:** There are two approaches. One is to focus on the one-click install and mention competitors for search visibility, but that could be negative because you're showing how hard it is. The other is to have zero brand mentions on your site. Either works.

**Sylvain Giuliani:** I don't want zero brand mentions. It's more like a product feature than an SEO play. I want it to be clean, product-wise.

**George Haikal:** Perfect. For Workstream 1, we want to get the codelibrary.ai redesign out there and get it indexed. Right now, if we optimize for conversion with zero traffic, it decreases our chances of getting traffic in the first place. This is more of a Trojan horse play — we'll get it indexed first, then optimize later. We'll learn a lot from this product launch that we can apply to your actual product launches.

**Sylvain Giuliani:** Got it.

**George Haikal:** Okay, perfect.

**George Haikal:** For Workstream 2, I want to show you an edition of a newsletter we're building for experienced, somewhat skeptical, but AI-forward engineers. We've developed three to four different sections. The first is a "full read" — we scour high-quality engineering blogs every week, not shallow influencers. For example, someone who spent two years testing AI frameworks and wrote about it. We'll give the TLDR and takeaways, like: "You're well-read but inexperienced and overconfident — this framework helps you calibrate when to trust AI output and when to question it."

**George Haikal:** The second section is a CTA — a value-add like a comparison guide on AI coding agent benchmarks, not a generic "sign up for Augment Code" pitch. It'll live on augmentcode.com as a high-intent page.

**George Haikal:** The third section is the "skeptical engineer's take on latest hype news" — a bit funny, edgy. For example: "AI generates 25% of code at Big Tech. Amazon, Microsoft, and Google all happen to sell coding tools, and now AI writes 25% of their code. Shocking. Still waiting for the part where they mention how much gets deleted by the next engineer." We're positioning ourselves as the filter — part of you, skeptical, calling out BS when we see it.

**George Haikal:** And then the last, this is a mock-up, and so hopefully it just gives you a little bit of a visual.

**George Haikal:** Obviously, this is a very rough visual.

**George Haikal:** We'll refine the design.

**George Haikal:** But then if you jump into the docs as well, what we built is a library.

**George Haikal:** So if go into their docs, actually, and you go into the engineering blog database really quickly, into the we'll like It's see.

**George Haikal:** right Thank you.

**George Haikal:** I need to refresh it, but I'll drop a link here.

**George Haikal:** There it is.

**George Haikal:** Okay, so we started to curate a database of every legit engineering block there is, and also we're starting another one to augment this of every, like, legit personal block from a legit engineer, essentially.

**George Haikal:** Right?

**George Haikal:** So the idea is we're going to monitor these every single week and then curate anytime there's anything worth reading, which in these cases, like, almost anything these people publish will be worth reading, you know?

**George Haikal:** And we'll have a section that's kind of like, hey, don't worry about monitoring, like, 100 engineering blogs.

**George Haikal:** Like, we're going to just curate, like, the latest from them, you know, whenever they post something, you know?

**Sylvain Giuliani:** Yeah.

**Sylvain Giuliani:** Yeah.

**Sylvain Giuliani:** Um, no, I like that.

**Sylvain Giuliani:** Two things. The newsletter should be tied to Augment — not completely off-brand. We need to thread the line. We're an AI company that does code generation, so we should not be anti-code-gen. If it was detached from Augment, maybe that would work for more subscribers, but we're already building a second audience with CodeLibrary. I don't want another project that's not attached to Augment.

**George Haikal:** So we'll tone down the skeptical aggressiveness against code generation.

**Sylvain Giuliani:** Everything else — the top section is great, the call to action is good. The whole concept is good.

**Sylvain Giuliani:** You should look at what SWIX is doing with the AI Engineering newsletter. Look at his recent newsletters — what sources is he using? He's using AI influencers on Twitter, which is great timely information we can pull. Since we're doing a weekly newsletter, we can look at what respected people like Armin Sander are saying on Twitter. Copy the homework of AI news — find those influencers and sources yourselves or look at what they're doing.

**George Haikal:** The concept is targeting senior principal engineers who want to hear from people like themselves — not AI-only influencers. There are 50 publications covering AI-only content. We want to focus on what core engineers are talking about who also happen to care about AI.

**Sylvain Giuliani:** Exactly. Look for highly respected staff-level software engineers — people like Armin Sander, who don't just talk about AI but have credibility to make their take valuable. (I shared the link in Slack.)

**George Haikal:** So we'll organize sources into clusters. One cluster is engineering blogs — when Netflix posts on their blog, it's high-quality work. The other is Twitter influencers like the HashiCorp founder who built Vagrant and Terraform. We'll also look for content like "The Revenge of the Dreamer Developer" by Steve Yeti — it went viral and has widespread search demand. As long as content supports what we stand for, it's worth including.

**Sylvain Giuliani:** Let's keep adding sources and iterating on the newsletter.

**George Haikal:** I already met with Beehive. We have up to 200,000 subscribers we can upload, and we're working to get that limit up to 500,000. We're setting up the account so you don't have to. We just need help from you on how to pull the subscriber list. We're not going to send right away — we'll segment first. After we get the list, we'll coordinate design and content. We're not blocked otherwise.

**Sylvain Giuliani:** We want the newsletter to feel like "by Augment" and follow our brand guidelines.

**Sylvain Giuliani:** Design-wise, I can loop in Megan, but she's busy and I don't want her to be a blogger. For the subscriber upload, we can start with 100k. Molisha, pull from CustomerIO — take the last 50,000 people who signed up to Augment, not unsubscribed, with valid emails. We have email verification data from the Enricher now, so use that.

**George Haikal:** I'd recommend creating two segments. First segment: engaged subscribers who've opened at least one email (any sign of life). Second segment: valid email + still subscribed but no email opens. Warm the first edition with the engaged ones — it sends higher quality signals to Beehive and minimizes spam reports. When I did this for DeepGram, I sent 70,000 and got only 6 spam reports. The key is getting people who are actually engaged.

**Sylvain Giuliani:** Got it. Let's just make sure we get people who still subscribe.

**George Haikal:** For Workstream 3, we've fleshed out our content OS with sample articles and topics. This needs more review offline, and we'll send a Loom video walking through the approach. We're focused on bottom-of-funnel content, but it still needs a bit more work. We want feedback on the content OS by end of day today.

**Sylvain Giuliani:** Where are we today vs. in a month? If I have four tokens of work, which will give me the most impact in three weeks? I need to see the move from X to Y. What are the OKRs? The first workstream is an experiment. The second is an experiment that could have short-term impact.

**George Haikal:** Got it. I need OKRs to understand.

**George Haikal:** A couple of blockers: we need Search Console set up for augmentcode.com. Also, we need analytics access so we can pull baseline metrics. For this week, our focus is on the calibration article and content clusters. We'll get the first article out next week to start learning from organic performance. This unlocks us to get content out and iterate fast.

**George Haikal:** Your blog is all product analysis. As we create educational content and guides, we have options.

**Sylvain Giuliani:** Don't use the blog. Let's create /library or /guides with a clear separation. The blog should stay product announcements and company updates — very clear. The SEO content lives in /library or /guides. That avoids internal politics and confusion about why something was published.

**George Haikal:** We'll take the blog structure and create /library or /guides that mirrors it exactly. Who owns the website on your end?

**Sylvain Giuliani:** Chris owns the website. You should be able to contribute via pull requests, but we need to figure out the process. Chris can grant you access to the repo.

**George Haikal:** Kirkland or one of our design engineers will reach out to Chris for repo access. We'll create /guides as a duplicate of the blog structure. We'll ensure the sitemap gets updated with new pages from that section. We'll get Search Console access so we can submit new pages for indexing manually and verify they get indexed. Once it's a separate section, there's less internal scrutiny on messaging.

**George Haikal:** For Workstream 4, alongside the blog sources, we're monitoring influencer lists, Reddit threads, subreddits, podcasts, and YouTube videos. We'll actively ping when good content is created so we can include it in the newsletter.

**George Haikal:** Molisha, when you send the subscriber list, please also answer: what's the current state of the email list? How did they opt in? How have they been messaged before? What are the open and click-through rates?

**Molisha Shah:** We're happy to manage that. Sounds good.

**George Haikal:** Thanks everyone.

**Sylvain Giuliani:** Before we go, the education guide that Daniel created internally — repurposing that could have quick, short-term impact. I haven't seen the course yet, but it's a way to help legacy enterprise users transition to Augment, which is great for sales. We're doing a launch week in three weeks, so we could include this as part of that. If you can share what Daniel created internally and how we can repurpose it, that should be a priority.

**George Haikal:** We'll prioritize that. We can combine what Daniel created internally with insights from principal engineers who've gone through the process. We're already building pain-point guides for users. Daniel's guide is more about helping people like Clint, who've never used Cursor or Augment before, get up to speed. We'll follow up by end of week with next steps on that.

**Sylvain Giuliani:** All right, I've got to bounce. Thank you all.

**George Haikal:** Thanks, everyone. Bye.
