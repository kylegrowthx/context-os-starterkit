# Lovable Deep Dive

<metadata>
date: 2025-09-22
time: 18:02 UTC
duration: 39 minutes
organizer: George Haikal (GrowthX)
participants: George Haikal (GrowthX), Aleksander Heino (Lovable)
fathom_recording_id: 88935234
fathom_url: https://fathom.video/calls/416973145
share_url: https://fathom.video/share/JUgH2qnEafNumdzPYZNTCFps8JsCPxMa
source: fathom
enriched_on: 2026-03-03 12:30 UTC
</metadata>

---

## Summary

George from GrowthX and Aleksander from Lovable discussed activation and retention strategies for Lovable's AI app builder, which processes 250-300k signups per week but sees only 20-30% of users sending 5+ prompts after login. George presented GrowthX's template-based approach from their Bolt project (prior work analyzing user behavior, categorizing use cases, and building prioritized starter kits), while Aleksander shared Lovable's existing analysis of 5k projects with categorization by type (SaaS, internal tools, websites, prototypes) and retention patterns among paid users. They aligned on GrowthX analyzing the critical first 5-10 prompts where most users drop off, developing templates and content to improve early activation, with potential spillover benefits to retention. Aleksander will send project category analysis, raw data, attribution dashboards, and first-prompt data for privacy review; George will provide integration guidance for the Lovable website.

---

## Context

Lovable (lovable.dev) is an AI-powered web application builder founded in Stockholm that has achieved significant product-market fit, processing 250-300k signups weekly. Aleksander Heino leads data analysis for the company, working as part of a two-person data team managing both product analytics and marketing/growth initiatives. The core product challenge is a severe activation bottleneck: while signups are plentiful, only 20-30% of new users send more than 5 prompts before abandoning the platform, creating a leaky funnel that limits monetization despite a robust paid user base. GrowthX previously completed similar deep-dive work for Bolt (another AI dev tool), analyzing user behavior patterns and building data-driven starter kit templates. This meeting represents an extension of that engagement into Lovable's activation problem, with the understanding that improving early user success could have compounding benefits for both conversion rates (mobile CAC is currently measured in thousands despite positive ad platform signals) and long-term retention.

---

## Relevance

**To GrowthX Delivery:**
- Direct application of GrowthX's template and starter kit methodology from Bolt project to a new AI tool (Lovable) with similar user activation challenges
- Opportunity to develop content and templates targeting the critical first 5-10 prompts, where 70-80% of users currently drop off, using Lovable's categorical data on projects (SaaS, internal tools, websites, prototypes)
- Lovable has existing infrastructure: 5k categorized projects, AI-driven subcategory classifications, and first-prompt data — reducing GrowthX's data collection burden versus greenfield project work
- Partnership requires GrowthX to help Lovable prioritize which user segments and project types to address first for maximum impact

**To CheckThat:**
- Lovable's user base represents a large cohort of AI app builders; usage patterns, drop-off reasons, and successful project types could inform AEO strategy around builder intent and content optimization
- Potential to analyze Lovable projects for AI visibility patterns, search optimization of public projects, and how builders discover/describe their tools (informs CheckThat's understanding of AI-generated content discovery)

**To GrowthX Business Development:**
- High-touch engagement with growing, well-funded company (Lovable has significant venture backing) signals capability in AI tool optimization and could strengthen reference potential
- Focused scope (activation analysis + template development) reduces execution risk versus broader retainer; success here could expand into template maintenance and ongoing content strategy
- Early data access (first-prompt user data, attribution dashboards, project categorizations) positions GrowthX for insights-driven upsell into broader content/SEO strategy once activation metrics improve

---

## Overview

- Lovable's current focus is on retention, particularly for paid users, due to its high potential impact; however, the company recognizes activation as the limiting factor — only 20-30% of new users send 5+ prompts, leaving massive upside in the conversion funnel
- First-time user experience is a major drop-off point, with mobile conversion especially poor (1-2% page view to sign-up) despite strong ad platform signals and high signup volume (250-300k/week)
- GrowthX to analyze first 5-10 prompts per user to identify specific friction points and develop targeted solutions (e.g., templates by use case, starter kits for common builder personas, content addressing common errors)
- Collaboration will prioritize activation/conversion improvement for new users; success metrics will inform longer-term retention strategy since many activation pain points likely recur in retained cohorts

---

## Key Topics

### Current Data Analysis Capabilities

  - Lovable can categorize projects by type (SaaS, internal tools, websites, prototypes) and subcategories (B2C, e-commerce, gaming, etc.) using AI-driven analysis
  - AI-generated descriptions and categorizations for user projects enable trend spotting and pattern matching at scale
  - Analysis currently focused on retained, paid users due to resource constraints and cost of running full agent analysis on all users
  - Basic last-touch attribution setup for top-of-funnel analysis; not yet linked to Stripe/LTV data, but provides platform split (SEO vs. direct + other sources)
  - Explore page being revamped algorithmically to surface highest-quality user projects and improve discoverability/inspiration for new builders

### Key Metrics and Challenges

  - Major drop-off in first-time experience: only 20-30% of users send 5+ prompts after login
  - Mobile conversion rate is critically low (1-2% page view to sign-up), despite ad platforms showing positive ROI signals — hypothesis is mobile UX friction, not audience quality
  - High volume of sign-ups (250-300k/week) but extremely low conversion to active paid users, amplifying the cost of customer acquisition
  - Limited analysis on users with fewer than 5 prompts due to cost constraints; this cohort (70-80% of signups) is essentially a blind spot, but also the highest-leverage improvement opportunity
  - Builders getting stuck on first experience and bailing before discovering product value — need to understand specific blockers (error states, UX confusion, unclear next steps)

### Potential Areas for Improvement

  - SEO optimization and showcasing high-quality user projects on Lovable's site to drive organic awareness and credibility
  - Mobile conversion rate enhancement through UX/copy fixes and mobile-optimized onboarding
  - Template marketplace development (in-house + user-generated) to reduce cold start friction
  - Algorithmic high-quality project discovery on explore page to inspire new builders and demonstrate what's possible
  - Scalable use case analysis for user projects to identify common patterns, pain points, and opportunities

### GrowthX's Approach and Offerings

  - Direct prior experience with Bolt (similar AI dev tool) including analysis of user activity sessions, self-identified builder personas, project types, and churn patterns
  - Creation of prioritized starter kit templates based on which user segments are largest, paying most, and most likely to churn — data-driven prioritization of build effort
  - Reverse-engineered master prompts (one-shot building blocks) that guide new users through common use cases and teach both the "what" and "why" to reduce early confusion
  - Churn analysis and identification of specific drop-off points where users get stuck (e.g., portfolio builders hit UX issues and abandon at predictable points)
  - Content strategy tied to SEO, search intent, and user behavior — content that educates, unblocks, and enables conversion

### Data Sharing and Next Steps

  - Lovable to share:
    1. Google Doc with project category analysis and AI-driven categorizations
    2. Raw data behind the analysis (~5k categorized projects)
    3. First 5-10 prompts per user with conversion status, self-identified builder role, and total messages sent as LTV proxy
    4. Attribution dashboard showing platform split (SEO, direct, other) and conversion by source
    5. Aleksander to check with team on data privacy concerns before sharing prompt data
  - GrowthX to provide:
    1. 2-3 bullet points on technical integration needs for Lovable website (how starter kits/templates plug in)
    2. Analysis of first-prompt drop-off patterns and recommendations for content/template solutions
  - Aleksander to identify appropriate engineering contact at Lovable for technical/integration discussions with George

---

## Action Items

**Aleksander Heino (Lovable)**
- Send Google Doc w/ project category analysis + raw data (~5k projects) to George Haikal
- Compile & send first X prompts/user, conversion status, self-appointed builder role, total msgs sent as LTV proxy to George Haikal
- Check w/ team re data privacy concerns for sharing prompt-level data with GrowthX
- Send attribution dashboard data (platform splits, conversion by source) to George Haikal
- Share George's website integration points with engineering team; identify right person for George to discuss technical implementation with

**George Haikal (GrowthX)**
- Send 2-3 bullet points on how to plug into Lovable website (starter kit/template integration) to Aleksander Heino

---

## Transcript

**Aleksander:** Yes, it's 8 p.m.

**George Haikal:** Okay, not too bad.

**Aleksander:** This meeting is being recorded.

**George Haikal:** Yeah, I'm here in San Francisco.

**George Haikal:** Our office is here.

**George Haikal:** I'm assuming Stockholm for you?

**Aleksander:** Yeah.

**George Haikal:** How does that work?

**George Haikal:** So I know the company's based there, right?

**George Haikal:** But there's contractors that can be virtual and part-time.

**George Haikal:** And is that the requirement?

**George Haikal:** Like, if part-time, you can be outside of Stockholm when anyone is full-time, needs to be there in person?

**George Haikal:** Or what does that look like?

**Aleksander:** I don't think there's anything, like, any strict rules there.

**Aleksander:** I think the founders are trying to keep it Stockholm-based, to the level they can when they're able to get the talent they need.

**George Haikal:** But then if someone is not flexible and you need them, then you discuss.

**George Haikal:** Yeah.

**George Haikal:** How about you — did you, are you from there originally?

**Aleksander:** Or did you relocate for it?

**Aleksander:** I'm from Helsinki.

**George Haikal:** Okay.

**Aleksander:** So, like, one hour flight.

**Aleksander:** But, yeah.

**Aleksander:** Did you relocate?

**George Haikal:** Not too bad.

**George Haikal:** Sounds worth it.

**George Haikal:** Sounds like you're liking it so far.

**George Haikal:** There's definitely not a shortage of things to do, right?

**Aleksander:** Yes, I'm having a lot of fun.

**George Haikal:** I bet, man.

**George Haikal:** Yeah, I mean, we're super excited to meet with you all.

**George Haikal:** I know we did a ton of work for Bolt for a little bit of time as well.

**George Haikal:** So it just got us in the mindset of thinking through, you know, a similar player and then how we think of the prompts and the users and prioritization.

**George Haikal:** And so I was like super excited to pick your brain a little bit more about, I guess, there's a few things that I want to talk to and it can be super casual.

**George Haikal:** But basically it's, and I shared the agenda, it's just understanding a little bit more about like how you operate, what your priorities are, biggest goals, biggest challenges, and like what your team looks like.

**George Haikal:** I guess we can start there and then I have 20 other questions we can go to, but, and some things to show you.

**George Haikal:** But I guess starting there, like what's, what's top of mind?

**George Haikal:** What's most challenging for you?

**Aleksander:** Sounds good.

**Aleksander:** So, I'm the person of contact in our data team.

**Aleksander:** What's top of my mind?

**Aleksander:** What are people building?

**Aleksander:** How are people using their product and where they are getting stuck?

**Aleksander:** But since I'm right now one of the two data people working here, I also am working on quite many other things.

**George Haikal:** There's two total?

**Aleksander:** Yes.

**George Haikal:** Wow.

**Aleksander:** So, there's, I'd say there's like two big threads.

**Aleksander:** Like one, there's the marketing thread.

**Aleksander:** That's like what I think you have the most understanding on.

**Aleksander:** That's like what Sissy and Rachel are driving.

**Aleksander:** I'd say from that side, the biggest unoptimized things or like where I see a lot of value is like overall, I don't think we've done really anything with SEO.

**George Haikal:** Like probably.

**Aleksander:** So there's this whole question of, hey, can we showcase user projects, can we boost their SEO, can we find some high quality ones and like, showcase them? That's one big area. Like, just off the top of my mind, not sure if this is so relevant, but our mobile conversion is absolutely broken.

**Aleksander:** So we are spending quite a bit on meta ads and TikTok, whatever, on mobile, and essentially, the ad platforms are telling us, yeah, your CAC is good, you're getting tons of customers, and then when we look at our own data, we're like, yeah, we got like one customer out of like 10k spend, so our CAC is thousands, and the running hypothesis there is that it's because our mobile page view to sign up conversion is like 1-2%.

**George Haikal:** But that's something we already have some ideas on.

**Aleksander:** Like, let's start fixing and so we can better attribute those page views to purchases, etc.

**Aleksander:** That's, I'd say, like, what's on top of my mind for, like, the more marketing SEO side.

**Aleksander:** Then on the growth side itself, we have Sebastian and Elina.

**Aleksander:** Sebastian is right now driving the builder ecosystem, builder community part.

**Aleksander:** And I think from there, we could, there's, like, a lot of synergies to that user-generated content side.

**Aleksander:** So essentially, the goal is such:

**Aleksander:** One, let's create good, high-quality templates.

**Aleksander:** We already started doing that in-house and through some agencies.

**Aleksander:** So users are able to kind of come to, have an easier cold start, essentially.

**Aleksander:** Like, copy 90% of the product and continue from there.

**George Haikal:** Yeah.

**Aleksander:** There's this whole idea of, can we make the templates into a marketplace in the longer run?

**Aleksander:** So users generate them for each other.

**Aleksander:** There's our explore page, which we are now revamping, where I'm the main person of contact, where essentially we are trying to algorithmically first find the highest quality projects and then show them to the users and see whether they can get inspired and they are able to better understand what's possible with Lovable, so they are going to convert and build more.

**Aleksander:** And yeah, maybe as a last thing, I noticed from your slides, you had some sort of use case analysis with Bolt.

**Aleksander:** We have like a V1 version of that, where we are able to run our agent on user projects.

**Aleksander:** So essentially, I'm able to take a list of like 10,000 or 50,000 user projects.

**Aleksander:** I'm going to tell our agent, like, hey, give me a report on what this project is about.

**Aleksander:** Like, hey, is it complete, is it not complete?

**Aleksander:** Who's the target audience?

**Aleksander:** What is it, SaaS, internal tools, B2B, et cetera, and what's the, like, subcategory?

**Aleksander:** So that's something we are able to do today, but its scalability is, like, limited because we are running the full agent.

**Aleksander:** So it's quite compute expensive and costly.

**Aleksander:** So we are not today running it at, for all projects.

**Aleksander:** We are just, like, always selecting a sub-sample and running the agent on those.

**George Haikal:** Got it.

**George Haikal:** That's interesting.

**George Haikal:** Was that all on the Sebastian side, and was there something other under Elina that you wanted to touch on?

**Aleksander:** Yeah, I'd say that maybe, like, yeah, maybe good to think about, like, Sebastian and Elina and me.

**Aleksander:** So there's this, like, big pile of things from which we pick stuff up.

**George Haikal:** This makes sense.

**George Haikal:** I mean...

**George Haikal:** We have Fathom, our team in the background is continuing to refine these, but would it be helpful if I kind of show you quickly what I did for, what we did for Bolt and like what our thought process was for that prompt session analysis?

**Aleksander:** I'd love to see it because I feel like right now I'm also, I don't have a full picture of what's the high level solution space we're working with.

**Aleksander:** So when I have that, I can maybe give more targeted answers.

**George Haikal:** Yeah, no problem.

**George Haikal:** And just for a little context, and I'll share my screen in a second.

**George Haikal:** This was probably four months ago, three or four months ago before StarterKit templates were really even being used by any of these tools.

**George Haikal:** And so similar to your ideas, right?

**George Haikal:** What we thought of were the templates, pages, StarterKits, how you make it easier for people to build.

**George Haikal:** There's a lot more that goes under there, but I'll leave it there for now.

**George Haikal:** And then the second was comparison.

**George Haikal:** How do you compare yourself with the other tools, direct competitors, but also with the other tools?

**George Haikal:** What other tools are your users pulling in to finish the job, right?

**George Haikal:** And how can you create content to help them do that?

**George Haikal:** And then, so those are the first two use cases.

**George Haikal:** And the third was analyzing their churn to understand in their prompt sessions, like what users are the most likely to churn?

**George Haikal:** When are they, and why, right?

**George Haikal:** So it's like, is it the quality of their prompts?

**George Haikal:** What are they trying to build?

**George Haikal:** Where are the commonalities here?

**George Haikal:** Where can we help them along their way of using the product to enable them to either get the outcome that they want or essentially that.

**George Haikal:** And so that's how we approached the project that we did for them.

**George Haikal:** And I can show you kind of what each piece looks like.

**Aleksander:** So it sounds quite, quite like data science, quite like complex in a way.

**Aleksander:** So I guess I should also think that you have those capabilities in house.

**George Haikal:** We do.

**George Haikal:** We do.

**George Haikal:** Not for everybody, but we do.

**George Haikal:** I mean, our team's really powerful.

**Aleksander:** Like, what I love the most, we get something that might be more common in the U.S., but it's like super uncommon in Europe, but it's like super uncommon in Europe.

**Aleksander:** We get, like, free lunch and dinner, which is amazing.

**Aleksander:** So that's what I'm eating.

**Aleksander:** So sorry for that.

**George Haikal:** No, man, you're good.

**George Haikal:** Trust me, I get it.

**George Haikal:** But at a smaller company, you know, it's, we get the same, by the way.

**George Haikal:** But obviously, when you're working late, it makes it way better.

**Aleksander:** Yeah.

**George Haikal:** It's a necessity, honestly, to stay healthy, too, and, like, having to cook and kind of figure it out on your own takes too much time.

**George Haikal:** And it's usually unhealthy if you're getting it delivered.

**George Haikal:** Don't even get me started.

**George Haikal:** Yeah, don't even get me started.

**George Haikal:** Okay, so let me start.

**George Haikal:** Let's get to it.

**George Haikal:** For high level here, I'm going share my entire screen.

**George Haikal:** So basically where I'll start is here.

**George Haikal:** Essentially what we got from Bolt, right, was just an activity sample by user.

**George Haikal:** So what the users were saying, right, what they're trying to build, what they're actually doing when they were starting and stopping their session.

**George Haikal:** So this was the starting point.

**George Haikal:** And what we did with that, we got that and then we got a survey that they did on all of their users, self-identifying into different categories of who they are, right?

**George Haikal:** Are they a solopreneur or are they a developer?

**George Haikal:** And then what they're trying to build, right?

**George Haikal:** The what they're trying to build is here in the category and then the subcategory is what within the internal tools are they trying to build and then what plan they're on, right?

**Aleksander:** Because we're all paid.

**George Haikal:** Yep.

**George Haikal:** And so what we did using that activity session we got is created a summary for each user of what they started doing and why.

**George Haikal:** Just like a little narration so we could kind of, we could better understand what they're trying to build, when they stopped, what they came back to do.

**George Haikal:** Out of all of that, we were able to prioritize the users within these categories, building like the top five different types of subcategory templates, right?

**George Haikal:** So that's where we started our actual content and templates, like the highest priority, right?

**George Haikal:** We were finding that, and this is four months back, essentially like an example is we were finding that, you know, solopreneurs building internal portfolio website pages or building portfolio website pages were churning really quickly when they ran into this issue, right?

**George Haikal:** And that made up the largest bucket of people than we addressed that first.

**George Haikal:** And the way we addressed it was first, and this is before the finished product, right?

**George Haikal:** By category, again, of person, entrepreneur, what they're trying to build.

**George Haikal:** And then we created with our workflows, essentially master prompts that at the time with Bolt, you could one-shot.

**George Haikal:** This is like the beginning of a starter kit template, right?

**George Haikal:** So super detailed prompt that we kind of had to reverse engineer to make sure that it worked.

**George Haikal:** And with our workflows, we can constantly test and see what works and what doesn't, right?

**George Haikal:** And so this is hard for someone to actually understand if they're not tech savvy, right?

**George Haikal:** So then the result is, this is just to show you that it worked, is this.

**George Haikal:** With that one prompt, you build a really nice website.

**George Haikal:** And essentially, what we kind of delivered was showing, go back here, something like this.

**George Haikal:** So these were the top things being built and by whom.

**George Haikal:** And these are the starter kits that we built out for them.

**George Haikal:** Like the portfolio website that I mentioned, it comes with a description, the actual prompt editor.

**George Haikal:** So this is the one-shot prompt that you could start building right in Bolt.

**George Haikal:** And it actually teaches you the why and the how, because what we were finding was at the various stages of prompting or building, the users were getting stuck.

**George Haikal:** Where were they getting stuck?

**George Haikal:** We addressed it here.

**George Haikal:** And we also gave them a starter, so it's not only teaching them and making them do all the work.

**George Haikal:** It's also here to throw it in and get the outcome you want.

**George Haikal:** Or if you need to make more edits, here's how to understand each piece of the prompt and the thing that you're building.

**George Haikal:** So it's teaching it as well.

**George Haikal:** So this was like the V1 of how we approach that starter kit project.

**George Haikal:** And again, all rooted in the prioritization of who's the biggest set of users, who's paying you the most, what are they trying to build, and where are they going to get stuck, so it's all starting from that area.

**Aleksander:** Okay.

**Aleksander:** Super cool.

**Aleksander:** So, maybe I can quickly share where we are right now, and then we can start brainstorming a bit more on this specific problem area.

**George Haikal:** Yeah.

**Aleksander:** Can you see my screen?

**George Haikal:** I can.

**Aleksander:** Great.

**Aleksander:** So, we've done quite a similar analysis today, but it's missing some of the last steps.

**Aleksander:** So, this is what we have already.

**Aleksander:** We are able to take a list of projects and then categorize it by the project type.

**Aleksander:** SaaS, internal tools, personal websites, prototypes.

**Aleksander:** We have a pretty good idea of, like...

**Aleksander:** How well do they retain their activity, well as how well do they retain their, like, are they expensive or contractive in their credit consumption, day one versus month four.

**Aleksander:** Besides that, we are as well able to understand pretty well some subcategories that we have here, like B2C, B2C, e-com gaming, and a bunch of others.

**Aleksander:** What we also did was we create, like, some shorter AI descriptions for the products and, like, some different fields.

**Aleksander:** So, like, hey, does this project seem to provide value today?

**Aleksander:** So it's kind of completed are the real users short description user plan.

**Aleksander:** So we are kind of on the way with some of this thinking.

**Aleksander:** Yeah, yeah.

**Aleksander:** I say what we are missing today.

**Aleksander:** Is perhaps the last part where are users getting stuck specifically and what are kind of the most reasons for churn.

**Aleksander:** That's something that I actually want to prioritize myself, like really get hands on in the next one to two weeks.

**Aleksander:** So very, very like relevant topic right now.

**George Haikal:** Because on the kickoff call, I know you mentioned it was like the cutoff was five to ten prompts, right?

**George Haikal:** Someone writes more than five to ten prompts and the more stickier, they're more likely to continue.

**George Haikal:** Am I getting that right?

**Aleksander:** Yeah.

**Aleksander:** So the way you should think about, yeah, that's a really good call.

**Aleksander:** So everything that I showed you up to this point is us analyzing the users that have already converted and then seeing like how well do they retain.

**George Haikal:** Got it.

**George Haikal:** It's just a retention analysis.

**Aleksander:** Okay.

**Aleksander:** Yeah.

**Aleksander:** Yeah.

**Aleksander:** The reason why it is this way is because we have actually a huge amount of users coming in that send one, two, three, four, five messages and then churn.

**Aleksander:** And at this point, it's quite costly for us to run.

**Aleksander:** We are not able to run the agent on the scale we would need to categorize all of those users.

**Aleksander:** So that's why we limited it already quite strictly to the already converted pro users and then see how well they retain depending on the project type.

**Aleksander:** So the first five prompts is very much a green field today.

**Aleksander:** Interesting.

**Aleksander:** So, yeah, if we are able to get some good insights from why are people dropping off there and hopefully the reason is not that they are just low intent.

**Aleksander:** So if you are able to find a good reason and like able to fix those, that would be like a pretty huge thing.

**Aleksander:** Yeah, I think generally like from the company perspective, if I think about where me and like most of others are going to spend most of their time in the coming weeks or months, it's probably going to be on the retention piece.

**Aleksander:** So even though we have like really bad activation as well, because most of the users are dropping early, if you were able to like plug in our retention hole, we'd be able to like, the lever there is just like unimaginably big.

**Aleksander:** So that's why we're focusing on the like paid users already, making sure they don't leave.

**George Haikal:** This makes sense, makes sense.

**George Haikal:** I mean, our work sounds like it's going to be, it would make sense for it to be some of both, right?

**George Haikal:** Some targeting existing users, educating, helping them get through wherever they're getting stuck.

**George Haikal:** And then the other half of Fathom is doing that same thing, but for new users and trying to improve the conversion right there, right?

**George Haikal:** Because obviously right now, everyone's coming to you, you're at like 250,000, 300,000 signups per week, right?

**George Haikal:** To be able to first offer that retention number, but also at the top of funnel, providing templates, starter kits, content that actually help them build what they're trying to build or get closer to it or educate them on how, so they're not dropping in one to two prompts or one to five prompts, could be very valuable, yeah.

**Aleksander:** Yeah, I'd say like definitely from the perspective of, and like, I'm not the contracting party here, but like my own hunch is like from the perspective of our partnership, like even if you limit it to purely activation and we are able to have some good results there, that's going to have already like a really good arrow, so we don't need to go and crack the retention, which might not be a simple thing to do.

**Aleksander:** Mm-hmm.

**Aleksander:** Go and crack the retention, which might not be a simple thing to do.

**George Haikal:** 100%.

**George Haikal:** Yeah, this all makes sense and it's helpful.

**George Haikal:** Everything you showed and spoke to is helpful.

**George Haikal:** And yeah, on our end, what we're already going to continue to explore and then start delivering on are the starter kits.

**George Haikal:** But everything we talked about helps with the prioritization of what we actually want to build and why and for whom.

**George Haikal:** If you have any more information, so that Google Doc you showed that has the session analysis, the categories, the subcategories.

**George Haikal:** I didn't see like solopreneurs or developers.

**George Haikal:** Like, do you have a breakdown of the personas and the buckets that the users fall in?

**Aleksander:** So we do have a breakdown.

**Aleksander:** I've been, like as a personal pet peeve of mine, I've been trying to keep those separate right now.

**Aleksander:** Because the way we collect those personas today is with an onboarding survey.

**Aleksander:** And like said, are you starting to get private and check the...

**Aleksander:** And I think the data quality there is not as good.

**Aleksander:** I think it can be fine if that's the only thing we split by.

**Aleksander:** But if you split by two or three things, then it's going to be tricky to really have any good value.

**Aleksander:** So that's why I haven't kind of cross-referenced those two analyses against each other.

**George Haikal:** Yeah, I see your point.

**George Haikal:** Yeah.

**George Haikal:** I see your point.

**George Haikal:** definitely makes sense.

**George Haikal:** You can't take it as gold.

**George Haikal:** I'm just thinking on how.

**George Haikal:** Okay.

**George Haikal:** I mean, that's totally fine.

**George Haikal:** If you have, so then, could you pull up that Google Doc again?

**George Haikal:** And just so I can see like the percentages of what people are, what people are building and then the breakdown.

**Aleksander:** So, let me...

**Aleksander:** Yeah, more like SaaS and internal tools as percent of credit consumption are huge.

**Aleksander:** Yeah.

**Aleksander:** But then if you look like at the three main categories, like by activity, like website, internal tools.

**Aleksander:** Yeah, prototypes, like also not insignificant.

**Aleksander:** I think it's going to be important for cracking B2B, but perhaps it will be harder to get incremental value from there.

**George Haikal:** How are you defining prototypes here?

**Aleksander:** We are using this cool thing called let the AI decide.

**Aleksander:** Yeah.

**Aleksander:** Oh, yeah.

**Aleksander:** So essentially in the AI master prompt, we say that if the user is not trying to connect the backend or like we have this various criteria there, but like essentially it's AI.

**George Haikal:** Making a call, whether this looks like a prototype or not.

**George Haikal:** Yep.

**George Haikal:** Okay.

**George Haikal:** This makes sense.

**George Haikal:** then how many of the subcategories do you have or how granular do you get?

**Aleksander:** Not very granular right now.

**Aleksander:** So this is the granularity, but we also have the one-sentence level descriptions of the apps.

**Aleksander:** So if we want to, we can quite easily, I think, just take those one-sentence descriptions and run some small LLM to categorize them into, like,-word categories.

**Aleksander:** So if we want to, we can quite easily, I think, just take those one-sentence descriptions and run some small LLM to categorize them into more granular categories.

**George Haikal:** Yeah.

**George Haikal:** Yeah, that's just helpful.

**George Haikal:** Do you have anything you could send over that the team could look at?

**George Haikal:** Because, I mean, what I showed you, I was bold.

**George Haikal:** They just sent us their activity analysis, and we did the rest.

**George Haikal:** And so I'm just trying to figure out how we could best help here and, like, take time off your plate.

**Aleksander:** So, like, I don't want to to be asking you to do more things.

**Aleksander:** Absolutely.

**Aleksander:** So...

**Aleksander:** I can definitely send this.

**George Haikal:** I can send you the raw data behind this.

**Aleksander:** I think it's around 5K projects right now.

**Aleksander:** What else can I do?

**Aleksander:** I think this kind of then goes into how hands-on do you want to get into the AI stuff, which is like very unclear to me.

**Aleksander:** We can also give you some more raw data similar to what Bolt did and see whether we can find something there.

**Aleksander:** But I think there we should just coordinate and make sure that we're not doing duplicate work since there's me and one other person looking into similar things right now.

**George Haikal:** Yeah, definitely.

**George Haikal:** No, I agree.

**George Haikal:** As efficient as can be, the better.

**George Haikal:** But the more we have, the more I can at least think about with the team and we can come up with some solutions.

**George Haikal:** But yeah, I mean, if you want to hold off on spending the other thing for now, but this Google Doc and the raw info behind it will be helpful.

**George Haikal:** Would be very helpful.

**George Haikal:** do you have, I know there's too much to keep up with now on like brand new users.

**George Haikal:** Like, do you have anything there that you kind of refer to or look at?

**Aleksander:** From the perspective of what I look at from brand new users, to be honest, it's mainly like just top of the funnel.

**Aleksander:** Like where are users coming from?

**George Haikal:** And is that anywhere?

**George Haikal:** That'd be helpful for us.

**Aleksander:** Yep.

**Aleksander:** We have like a basic last touch attribution setup.

**Aleksander:** So we are like able to know with the campaigns and sources.

**Aleksander:** What we haven't done yet is link those to Stripe data.

**Aleksander:** So right now we know like the signup, like we know that the purchase is happening, but we are not looking at LTV or like six months revenue or anything like that.

**Aleksander:** So it's like binary, did that person make a purchase or not?

**George Haikal:** Which is still better than nothing.

**Aleksander:** Yeah, so like a platform split.

**Aleksander:** But right now, like it's SEO and direct.

**George Haikal:** Got it.

**Aleksander:** Essentially.

**Aleksander:** A bunch of smaller categories.

