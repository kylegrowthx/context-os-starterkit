# Runpod <> GrowthX Weekly Sync

<metadata>
date: 2025-04-08
time: 17:00 UTC
duration: 20 minutes
organizer: jason@growthx.ai
participants: Emmett Fear (RunPod), Jason Gong (GrowthX), Sydney Go (GrowthX)
fathom_recording_id: 56148933
fathom_url: https://fathom.video/calls/270550381
share_url: https://fathom.video/share/syCg68PmuxZrbweyjr8QwmMNJvxKPwhS
source: fathom
enriched_on: 2026-03-04 12:30 UTC
</metadata>

---

## Summary

RunPod and GrowthX aligned on a two-cluster content strategy (deployment guides and RentGPU comparisons) with randomized titles to diversify SEO signals, and GrowthX will deliver five test articles this week using their new workflow. The site audit revealed RunPod's site is remarkably clean and fast, with minor issues around orphan comparison pages and sitemap consistency to address in the coming weeks. Emmett requested a new priority: creating a listicle article mimicking Hyperstack's dominant "Top 10 Cloud GPU Providers" piece, which is the #1 article referenced by ChatGPT for cloud GPU queries, because RunPod's brand authority is higher and could displace it — AI-driven traffic alone is generating 500-1,000 activations per month.

---

## Context

RunPod is a managed cloud GPU platform helping developers and companies access on-demand compute for AI workloads. GrowthX is their content marketing partner, generating programmatic SEO articles to drive organic traffic and AI visibility. This weekly sync is part of an ongoing engagement where GrowthX manages content strategy, article generation, and SEO optimization for RunPod's site. The relationship is strategic — Emmett (RunPod founder/product) and Jason (GrowthX) have a working relationship where scope is flexible ("best efforts") rather than fixed deliverables, reflecting trust and alignment on goals. RunPod has recently discovered that AI-driven search (ChatGPT overviews, Claude citations) is a significant traffic driver, creating new urgency around winning the "Top 10 Cloud GPU Providers" ranking currently dominated by competitor Hyperstack.

---

## Relevance

**To GrowthX Delivery:**
- Confirmed five articles approved for this week; Sydney will test new workflow on them and deliver by end of week
- New status workflow introduced (article generation, review, revisions, ready to stage) to reduce friction on client feedback loops
- RunPod using Supabase backend for article publishing; Webflow migration expected end of month creates interim opportunity to test upload pipeline
- Content strategy successfully narrowed to two high-confidence clusters (deployment guides, RentGPU comparisons) rather than trying to cover all use cases

**To CheckThat / AI Visibility:**
- Major discovery: AI-driven traffic (ChatGPT, Claude citations) is driving 500-1,000 activations/month for RunPod — making this a high-ROI channel
- Hyperstack article dominates ChatGPT references for cloud GPU providers; winning this ranking with superior brand authority could significantly boost activations
- Key SEO pattern identified for AI visibility: short paragraphs immediately after headings, internal linking, keyword density (AI, training, fine-tuning, inference, machine learning)
- Deep-dive section on own product (Hyperstack does this) is effective despite being unconventional — validates in-depth product positioning

**To GrowthX Business Development:**
- RunPod account shows strong engagement: expanded scope (Hyperstack listicle request), trust in flexible scope model, clear ROI signals (500-1K activations/month from AI search)
- Site quality is clean and fast (running on code vs. Webflow), indicating technical sophistication and likely ability to implement recommendations
- Growth opportunity: establishing this as a case study for AI visibility and programmatic SEO in infrastructure/cloud space

---

## Overview

- Focus on two content clusters: deployment guides and RentGPU
- Site audit revealed minimal issues; orphan pages and sitemap inconsistencies to be addressed
- New article template for RunGPU comparisons created, aiming to compete with high-ranking competitors
- AI-driven traffic is significant, driving 500-1000 activations per month

---

## Key Topics

### Content Strategy Updates

  - Two main content clusters: deployment guides and RentGPU
  - Randomized titles for variety (e.g., "Deploy in seconds on RunPod", "Affordable on-demand cloud access with RunPod")
  - Five articles approved for the week, testing new workflows
  - Content OS updated with new statuses (article generation, review, revisions, ready to stage)
  - Webflow migration expected by end of month; interim solution for article uploads in place

### Site Audit Findings

  - Minimal issues found; site is clean and fast
  - Orphan pages identified, mainly for paid ad landing pages and comparison pages
  - Recommendation to create a structure for comparison pages (e.g., /compare or nested under existing categories)
  - Some links on the website not included in the sitemap
  - Meta description improvements suggested but not critical

### Competitor Analysis

  - Focus on replicating success of Hyperstack's high-ranking article on cloud GPU providers
  - Key factors: listicle format, internal links, keyword density (AI, training, fine-tuning, inference, machine learning)
  - Short paragraphs after headings beneficial for AI overviews and LLM mentions
  - Deep dive into own product (Hyperstack) noted as effective despite being unconventional

### Content Distribution

  - Blog posts shared on LinkedIn, X (Twitter), and email
  - No current strategy for distributing articles from the "articles" section
  - Consideration needed for promoting listicles and comparison content

### New RunGPU Template

  - Template added to database with specific URL structure suggestion
  - More landing page-style format proposed
  - Includes tables and additional comments for review

---

## Action Items

**Sydney Go (GrowthX)**
- Create listicle article mimicking Hyperstack's "Top 10 Cloud GPU Providers" — focus on keywords (AI, training, fine-tuning, inference, machine learning), listicle structure, short paragraphs after headings for AI overview optimization

**Emmett Fear (RunPod)**
- Share RunPod's serverless article with Sydney and Jason for reference on article structure and performance
- Review new RentGPU template in template database, provide feedback to Sydney on landing-page-style format and proposed URL structure

---

## Transcript
**Sydney Go:** Um, do we want to do the debrief call after this, or are we good to...

**Jason Gong:** Um, maybe we can hop back for, like, a minute to see if we're missing anything important.

**Jason Gong:** Hey, Emmett, how's it going?

**Jason Gong:** Good, how are you?

**Emmett Fear:** We're doing great.

**Jason Gong:** How was your, uh, weekend?

**Jason Gong:** It's good.

**Jason Gong:** Yeah, um, solid weekend.

**Emmett Fear:** Nothing too crazy, and just, like, a rest and rejuvenate kind of weekend.

**Emmett Fear:** Oh, we, I hear that.

**Jason Gong:** We definitely need that.

**Jason Gong:** Yes, how about you guys?

**Emmett Fear:** Um, I can't remember what we did.

**Jason Gong:** I mean, we have, like, a pretty young kid, so usually it just, like, revolves around him.

**Jason Gong:** Very cool.

**Jason Gong:** How old is he?

**Jason Gong:** He's, uh, he's about to turn two soon.

**Jason Gong:** Oh, that's awesome.

**Jason Gong:** Yep.

**Jason Gong:** Um, cool, okay, we'll, we'll jump right in.

**Jason Gong:** Um, I think this week the main focus is, uh, kind of, like, looking at some content together. I can give some updates on how we're trying to tune some of our workflows to do the RentGPU content really well.

**Jason Gong:** You should see those articles soon this week.

**Jason Gong:** Actually, Sydney and I going to sit down and spend a bunch of time tuning that workflow to generate those articles really well after this call.

**Jason Gong:** And then a tiny bit of time at the end, we did a site audit over the weekend and just flagging a few things.

**Jason Gong:** Honestly, I think the site is pretty clean.

**Jason Gong:** It's super, super fast, which probably is because you guys have it in code instead of in Webflow.

**Jason Gong:** So I'm going to keep an eye on as we migrate.

**Jason Gong:** But we did notice a few things.

**Jason Gong:** It looks like a redirect loop and some missing things, but we can get into that at the end.

**Jason Gong:** Perfect.

**Jason Gong:** Sydney, feel free to take it away with the content.

**Jason Gong:** Awesome.

**Sydney Go:** So before we get get into...

**Sydney Go:** And I wanted to share with you that I added some ideas to our content OS.

**Sydney Go:** I'm going to share my screen here.

**Sydney Go:** Awesome.

**Emmett Fear:** Did it share?

**Emmett Fear:** Okay, there it is.

**Sydney Go:** Okay.

**Sydney Go:** So I figured, based on our chat last week, we'll want to focus on two clusters and really build out those two clusters well.

**Sydney Go:** And the two clusters that we kept are the deployment guide ones and our new one, which is RentGPU.

**Sydney Go:** When I look through the keywords, some of them had some traffic, but all of them had a keyword difficulty score, meaning there is content created for these keywords.

**Sydney Go:** And people are actually looking at them, even though SEMrush doesn't quite capture the search volume for these keywords.

**Sydney Go:** And when I did look at them, I think SEMrush is pulling from US data, not worldwide data.

**Sydney Go:** So there should be some traffic there, even if the search volume says zero.

**Sydney Go:** So I made sure that all of these GPUs are the ones that were...

**Sydney Go:** you had sent me.

**Sydney Go:** Awesome.

**Sydney Go:** And then what I did was I randomized the titles so they're not all the same.

**Sydney Go:** So every four is the same.

**Sydney Go:** So deploy in seconds on RunPod is one of them.

**Sydney Go:** Affordable on-demand cloud access with RunPod, Instant GPU Rental, and then train, fine-tune, and deploy AI models on RunPod.

**Sydney Go:** If any of those don't sound great to you, let me know and I can tweak them.

**Sydney Go:** If you want to add a few more formats, we can do that too as long as it's accurate.

**Sydney Go:** to your brand and to your tone.

**Sydney Go:** And then for here, I put an M-dash in the middle for now, but we can figure out the format of these later on.

**Sydney Go:** Like if it's a landing page and it can be like in two rows, like red to A100, PCLE, U2PU in the cloud, and then on the second line, like in smaller text, then it can be the second one.

**Sydney Go:** So it's a placeholder basically.

**Sydney Go:** Got it.

**Emmett Fear:** Yeah.

**Sydney Go:** So if you want to go through these two clusters and these ones.

**Sydney Go:** They're the same from last week or two weeks ago when I sent this to you.

**Sydney Go:** It's moving so fast.

**Emmett Fear:** It doesn't track time.

**Sydney Go:** So these are the same ones.

**Sydney Go:** Again, if you want me to change them, add new ideas, let me know.

**Sydney Go:** These are more on deployment guides for use cases.

**Sydney Go:** So if there's any of these that stand out to you that you want us to do now, that'll help too.

**Sydney Go:** We only have five articles or article ideas approved for this week.

**Sydney Go:** I'm actually testing our new workflows on these.

**Sydney Go:** And I should get these to you by the end of the week, plus whatever article ideas you approve.

**Sydney Go:** And then, yeah, so these ones are the ones I'm working on.

**Sydney Go:** If you do want to see any of our old ideas or from the other clusters, like if you want to send the infrastructure comparison page ideas and add those in here, I'll check this one as well.

**Emmett Fear:** These are all of our old ideas.

**Sydney Go:** If you add anything, if you change the status of anything.

**Sydney Go:** Ready to start.

**Sydney Go:** I think it's number three.

**Sydney Go:** Then I'll see it.

**Sydney Go:** Another note I wanted to add is in the status.

**Sydney Go:** I've added some statuses here.

**Sydney Go:** So if it's an article generation, that means I'm working on it.

**Sydney Go:** If it's an article review, that means it's on your end.

**Sydney Go:** And I'll usually send you in.

**Sydney Go:** So you don't need to keep checking this every day.

**Sydney Go:** I'll send you in Slack, let you know, hey, this one's done.

**Sydney Go:** If you'd like to give feedback, that would be perfect.

**Sydney Go:** And then if it's in revisions, that means it's back with me.

**Sydney Go:** And I'm looking at it and I'm revising and then ready to stage.

**Sydney Go:** This means it's I'm ready to publish.

**Sydney Go:** And then, oh, last question.

**Sydney Go:** Just to confirm, when did you say the Webflow migration will be done?

**Sydney Go:** We're hoping by the end of this month.

**Emmett Fear:** But in the short term, we do have a system for uploading articles.

**Emmett Fear:** So like we it's I we've done it so that it's just through our back end so that we can upload everything to.

**Emmett Fear:** Supabase, and then from there, will just automatically post.

**Emmett Fear:** Okay.

**Sydney Go:** Awesome.

**Sydney Go:** Yeah, because I remember last time you were saying that we can just send it to you into Google Doc, and you'll deal with it on your end, and then when you switch to Webflow, then we can take over?

**Sydney Go:** Yep.

**Sydney Go:** Yeah.

**Sydney Go:** Okay.

**Sydney Go:** Awesome.

**Sydney Go:** All right.

**Sydney Go:** That is it for me.

**Sydney Go:** Jason, do you want to take over?

**Jason Gong:** And just to clarify, did we go through the content, like the calibration articles?

**Jason Gong:** Yes, we did.

**Sydney Go:** We did the two calibration articles.

**Sydney Go:** I've got back from Emmett, and I've put it into our brand guidelines slash polishing guidelines in the workflow.

**Sydney Go:** That's good.

**Jason Gong:** Great.

**Jason Gong:** Okay.

**Jason Gong:** So we can just quickly go through some of the site audits we found.

**Jason Gong:** Yeah, but again, mean, typically, we find way more issues, but honestly, this time didn't seem too bad.

**Jason Gong:** You know, know, next time.

**Jason Gong:** I'm not sure if you guys have a tool like this set up, but generally we run this every two weeks and it just looks for essentially issues on your website.

**Jason Gong:** So I can just go through some of them.

**Jason Gong:** of them honestly aren't anything to worry about.

**Jason Gong:** The first one is just orphan pages, which for the paid ad stuff is totally fine.

**Jason Gong:** Generally you don't need a path to it from the homepage.

**Jason Gong:** But for some of these pages, I think what it suggests is like, for example, this one here.

**Emmett Fear:** See this page is actually valid.

**Jason Gong:** Yeah, like what it suggests is like, usually you should have some sort of hub page.

**Jason Gong:** Like, you know, for a lot of people it might be, you know, RunPod.io, let's say.

**Jason Gong:** I mean, RunPod.io slash compare would be reasonable or like just like some page that like links out to all these pages.

**Jason Gong:** So that's what an orphan page means.

**Jason Gong:** Like generally if you don't do that, just a lot less discover.

**Jason Gong:** Like, Google doesn't really understand Fathom together, so I would recommend putting it somewhere.

**Jason Gong:** I see, yeah.

**Jason Gong:** We could propose something, if that's something you're interested in.

**Jason Gong:** I know you have these big pools in blog and articles, but a lot of programmatic, it helps to add a tiny bit more structure, like how you already do it, and GPU benchmarks, GPU models.

**Jason Gong:** We can think what it should be for these, like, versus pages, if it's nested under one of those, or it's just like a slash versus, you know, or slash compare.

**Jason Gong:** I think we're going to have a lot more of these.

**Jason Gong:** We're going to have versus GPUs, versus cloud providers, versus, you know, all sorts of stuff.

**Jason Gong:** So it might make sense to create a structure for it.

**Emmett Fear:** Yeah, that makes sense.

**Emmett Fear:** I'm actually in the process of building that out, even just like with the articles that you guys have sent.

**Emmett Fear:** So I'm coding something up right now, so that way we can, like, add or take away categories at any point underneath.

**Emmett Fear:** articles.

**Emmett Fear:** And then we can sort each of the articles into one of those categories.

**Emmett Fear:** So that way, when you come to the articles page, you'll just see the categories.

**Emmett Fear:** And then when you click on a category, you'll see all of this.

**Emmett Fear:** Yeah, so this page is going to change to just show all of our categories.

**Emmett Fear:** And then from there, you'll click into a category and it will look like this.

**Emmett Fear:** That sounds good.

**Jason Gong:** I'm trying to think of, I don't know, Sydney, I'm sure you have a bunch of examples, but I know one company that I think does this pretty well is like these guys, which I'll just flag right here.

**Jason Gong:** It's like super simple, but like, you know, this is almost exactly like what you're doing. But I'll just link that somewhere.

**Jason Gong:** So you guys have it.

**Jason Gong:** Okay, so I think that'll solve the orphan page problems.

**Jason Gong:** And then there was another category where it's like indexable, but not on the sitemap.

**Jason Gong:** Yeah, so I guess this is more like, I'm not sure how you guys ended up generating that sitemap, but it seems like some blinks that are on your website aren't in the sitemap.

**Jason Gong:** So maybe that's something just to take a quick look at.

**Emmett Fear:** Okay.

**Jason Gong:** And it looks like, I mean, again, the paid ad stuff doesn't really matter.

**Jason Gong:** Yeah, it looks like it seems, it's mostly compare pages.

**Jason Gong:** So something to look at there.

**Jason Gong:** Speed's really good.

**Jason Gong:** And then, let's see, I swear I found this like weird redirect loop for one of these pages.

**Jason Gong:** Let me see if I can find it.

**Jason Gong:** Nope.

**Jason Gong:** Okay, I'll flag it if I end up seeing anything.

**Jason Gong:** But like overall, I think, I mean, honestly, it's super clean.

**Jason Gong:** Some of this like meta description stuff, but it's not like a super big deal.

**Jason Gong:** So, yeah.

**Jason Gong:** Again, we'll run that every two weeks.

**Jason Gong:** If we find anything, we'll flag it.

**Jason Gong:** Amazing.

**Emmett Fear:** Very clean.

**Jason Gong:** Did you have any thoughts, questions on your end?

**Jason Gong:** I did have one super quick question.

**Emmett Fear:** So this specific article is just, even though Hyperstack isn't like a super big company, they totally dominate with this article.

**Emmett Fear:** I would love, if you have time this week, Sydney, I know this is kind of out of the purview of these other articles that we're building, but I would love to have an article that just kind of mimics what they did to get to the high SEO ranking that they have with this one.

**Emmett Fear:** Because we're seeing a ton of references from ChatGPT specifically to this article.

**Emmett Fear:** It's the number one article that's being referenced by ChatGPT.

**Emmett Fear:** So we would love to have something similar because we know that our brand score is higher than theirs.

**Emmett Fear:** If we had an article that did all the same things, we think that we could probably displace it.

**Emmett Fear:** To have something like that, if that aligns with kind of this week.

**Emmett Fear:** Yeah, we can definitely take a look.

**Jason Gong:** I think this is something we're looking into doing better, like listicles.

**Jason Gong:** I want to improve how we generate these.

**Jason Gong:** But to you, I guess if you had to guess, what are the things that stand out for why this is kind of a nice article or why you think it's doing so well?

**Emmett Fear:** Just upon reviewing it, I've looked at it a couple of times, but obviously they rank themselves number one, which is pretty standard with any sort of listicle.

**Emmett Fear:** They have quite a few internal links. And I think that they just hit a lot of these keywords that are picked up for the vertical — AI, training, fine-tuning, inference, machine learning.

**Emmett Fear:** Like they're using a lot of these words that definitely get picked up.

**Emmett Fear:** And I think because they go, and I think it's, they actually go into like a ton of depth for HyperStack.

**Emmett Fear:** But then they have kind of like a standard template for all the other ones.

**Emmett Fear:** There we are on the list at number five.

**Emmett Fear:** But I would assume those are some of the reasons they're hitting a lot of the keywords.

**Emmett Fear:** They're doing a listicle.

**Emmett Fear:** I don't know how much impact this external link at the top is driving anything.

**Emmett Fear:** But I thought that was interesting too.

**Jason Gong:** Which one are you referring to?

**Jason Gong:** The very first one at the top.

**Emmett Fear:** Goldman Sachs Economic Research.

**Emmett Fear:** Is there any sort of benefit to having external links and articles?

**Emmett Fear:** I think so.

**Jason Gong:** I mean, generally the benefit isn't from the link — it's from having a reputable source and a nice kind of line.

**Emmett Fear:** Yeah, yeah, yeah. And we generally try to insert things like that.

**Jason Gong:** Okay, but that's helpful.

**Jason Gong:** I think I was trying to see as far as the content itself, if they were doing anything interesting.

**Emmett Fear:** They just have a standard template.

**Sydney Go:** The only thing I think they're doing super interesting here from an SEO point of view is this.

**Sydney Go:** They've got their headings and very short paragraphs after, which I think is helping them actually with the AI overviews and getting mentioned by LLMs.

**Sydney Go:** Because this is the best practice for it.

**Sydney Go:** One heading and then a very short paragraph, and it should directly answer your heading.

**Sydney Go:** And then for the rest of it, this is very generic listicle with the key features, pricing, all of that.

**Sydney Go:** We can definitely do that part for you.

**Sydney Go:** And then the deep dive into their own is something that I rarely ever see because people don't like to be overly salesy, but it does work.

**Sydney Go:** So this is something you definitely look to.

**Sydney Go:** Amazing.

**Emmett Fear:** Cool.

**Emmett Fear:** Thank you.

**Emmett Fear:** you.

**Emmett Fear:** Yeah.

**Jason Gong:** And I mean, like, I know you brought up the scope. I think generally how we think about it is just like, we're here to help you grow. I mean, we've never really nickel and dimed what the exchange rate is between editorial and programmatic SEO — we just kind of best efforts generate a lot of content.

**Jason Gong:** I think we're generating an order of magnitude more content per dollar almost than other people.

**Jason Gong:** I mean, we're a new company too and haven't really figured that out. But for you guys, just whatever content you need.

**Jason Gong:** And to be really honest, what's programmatic SEO is like a fuzzy term anyway — a lot of the stuff we're generating is already, in my mind, a little editorial anyway.

**Jason Gong:** But the goal is just like whatever content makes sense, like we're going to create it.

**Emmett Fear:** Perfect.

**Emmett Fear:** Perfect.

**Emmett Fear:** Cool.

**Emmett Fear:** Well, I really appreciate your help. Honestly, super excited to see everything that we can pump out. And just for more context on the AI search channel — we initially thought that it wasn't a super big channel, but then we looked into it, and it's actually driving anywhere between 500 and 1,000 activations a month.

**Emmett Fear:** It's definitely growing, and I think if we could have an article that's up there.

**Emmett Fear:** We did one specifically for serverless, which is a much smaller market, and we're seeing that rank high even though it's a small sliver of our competition.

**Emmett Fear:** It's still one of the top-ranking articles, and we just had somebody internally spin that up like a month and a half ago.

**Emmett Fear:** So I think one that's more targeted towards general cloud GPU is going to absolutely dominate.

**Emmett Fear:** Yeah.

**Emmett Fear:** Okay.

**Sydney Go:** We'll definitely start looking after that.

**Sydney Go:** You could share that article with us just so that we can see what you guys did.

**Emmett Fear:** Absolutely.

**Jason Gong:** Do you guys do anything to kind of distribute content that you've created?

**Jason Gong:** It looks like the blog is kind of where you keep a lot of the thought leadership stuff.

**Jason Gong:** Yeah.

**Emmett Fear:** Almost all of the thought leaderships.

**Emmett Fear:** Goes over there.

**Emmett Fear:** But like listicles, we've decided are probably going to live inside of articles.

**Emmett Fear:** Here we go.

**Emmett Fear:** Let me go.

**Jason Gong:** But do you guys like post them on socials, Reddit, like Dev, like any kind of...

**Emmett Fear:** We post the blog content over on socials pretty frequently.

**Emmett Fear:** We haven't really come up with a plan for how we want to post from articles just because we have wanted to keep that kind of a strong line between the two.

**Emmett Fear:** And so for the most part, like our blog content, when a new article gets pushed out, we publish on LinkedIn, X, and typically send out an email.

**Emmett Fear:** So those are kind of the three avenues that we let people know that there's a new article.

**Emmett Fear:** Okay.

**Jason Gong:** That's good.

**Jason Gong:** I'm sure we'll have more ideas there eventually.

**Jason Gong:** But I think the goal for next week is definitely just to like get some articles up.

**Jason Gong:** So you'll get a bunch of reports this week and then you let us know if there's any blockers to kind of getting that up on the site.

**Sydney Go:** Perfect.

**Sydney Go:** Sounds amazing.

**Emmett Fear:** Okay.

**Emmett Fear:** Yeah.

**Emmett Fear:** If there's nothing else, we'll kind of give you some time back.

**Sydney Go:** Just being in Slack.

**Sydney Go:** A more things.

**Sydney Go:** Oh, sorry.

**Sydney Go:** It came to my mind, but completely forgot to show you.

**Sydney Go:** Emmett, I just wanted to show you the new template that I uploaded for the RunDP.

**Emmett Fear:** great.

**Sydney Go:** So I did add it to our template database.

**Sydney Go:** It's in this last one.

**Sydney Go:** And I did add a URL here because I wanted to note that I don't think we should just put it under articles, since it is a specific type of article.

**Emmett Fear:** Yeah, that makes sense.

**Emmett Fear:** Yeah.

**Sydney Go:** And this, I feel like, should be a little bit more of a landing page type because...

**Sydney Go:** So one that we looked at, I think last time we showed you this, was Hyperstock, and it does...

**Emmett Fear:** Yes.

**Emmett Fear:** It's much more of a landing page.

**Sydney Go:** You can go through this and let me know if this works for you.

**Sydney Go:** I added some tables and everything and some comments in there as well for you.

**Sydney Go:** And yeah.

**Sydney Go:** Yeah, that's fantastic.

**Emmett Fear:** Okay, I'll look through it and let you know if I have any feedback.

**Emmett Fear:** Awesome.

**Emmett Fear:** Fantastic.

**Emmett Fear:** Cool.

**Emmett Fear:** Well, that's all I have.

**Emmett Fear:** Thank you both for your time.

**Emmett Fear:** I really appreciate it.

**Emmett Fear:** No problem.

**Sydney Go:** Thanks, Emma.

**Sydney Go:** Talk soon.

**Sydney Go:** Bye.

**Sydney Go:** Thanks.
