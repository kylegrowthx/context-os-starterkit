# Tavus <> GrowthX Follow Up

<metadata>
date: 2025-07-11
time: 20:11 UTC
duration: 28 minutes
organizer: kyle@growthxlabs.com
participants: Marcel Santilli (GrowthX), Kyle Gaudreau (GrowthX), Jesse Rowe (Tavus), Jack Virag (Tavus)
fathom_recording_id: 73734568
fathom_url: https://fathom.video/calls/347825647
share_url: https://fathom.video/share/uchbHfxvgpyM8aDwTD-SLRzUz13jErcH
source: fathom
enriched_on: 2026-03-03 15:42 UTC
speaker_note: Jack Virag was invited but did not speak during the meeting. Only Marcel, Kyle, and Jesse participated actively.
</metadata>

---

## Summary

Marcel walked Tavus (Jesse and Jack) through GrowthX's 8-week content strategy sprint—a comprehensive process combining AI-powered content creation pipelines, fact-checking via Perplexity and GPT-4, and programmatic use case page generation. Tavus aims to reshape its keyword profile through high-volume content (20-30 articles/week as "perspectives"), and Marcel recommended a thoughtful information architecture approach similar to the Vappy case study (2,600 custom pages achieving 6% click-through rates). The conversation closed with Kyle committing to send a proposal for next week's follow-up call.

---

## Context

Tavus is a conversational video AI platform looking to improve its organic search visibility and keyword profile. They currently rank ~196 pages but feel their keyword positioning doesn't accurately represent what the product does. The team uses a sophisticated content workflow (100+ steps in Airtable) and plans to expand into two content types: authored blog posts and "perspectives" (nameless, high-volume pieces) to aggressively rebuild domain authority and keyword relevance. Kyle Gaudreau, GrowthX's VP of Sales/Operations, had been in earlier conversations about potential collaboration. This follow-up call brought Marcel (GrowthX CEO and strategy lead) to present the full service architecture and explore whether Tavus is ready for a formal 8-week strategy sprint engagement.

---

## Relevance

**To GrowthX Delivery:**
- High-volume "perspectives" strategy (20-30/week) requires careful information architecture and clustering—reinforces GrowthX's recommendation to avoid aggressive publishing without semantic structure (lessons from Clay, HeyGen failures)
- Tavus's existing 100+ step Airtable workflow shows sophisticated internal processes; opportunity to migrate to GrowthX's code-based workflow engine for easier maintenance and scaling
- Product-specific use case pages (similar to Vappy's 2,600-page model) could be core differentiator; Supabase-as-CMS approach may be necessary at scale

**To CheckThat:**
- Conversational video AI represents emerging vertical within AI/LLM space; keyword profile misalignment suggests opportunity to audit Tavus's current SearchThat/CheckThat exposure and benchmark against competitors
- High click-through rates on use case pages (6% CTR for Vappy) signal strong commercial intent—valuable signal for AI visibility indexing

**To GrowthX Business Development:**
- Well-resourced startup team (Jesse shows deep content knowledge, team iterating on strategy) signals good cultural fit and execution likelihood
- Expansion risk: Tavus mentions tying content to outbound programs and PLG motions—positions GrowthX for potential workflow/integration expansions beyond core delivery
- Reference potential: If strategy sprint delivers 6%+ CTR results on use case pages, strong case study for other AI/SaaS with keyword profile challenges
- Booking pressure: Marcel mentioned July slots nearly full, August booking upcoming—capacity constraint validates GrowthX's 2-per-week sprint limit

---

## Overview

- GrowthX delivers an 8-week strategy sprint combining research artifacts, AI-powered content pipelines with fact-checking via Perplexity API + GPT-4, and custom workflow engines represented as code (vs. drag-and-drop) for better maintainability
- Tavus's goal: reshape keyword profile through aggressive content output (20-30 articles/week as "perspectives"), segment into blog + nameless pieces across different URL structures to avoid canonicalization issues
- Marcel recommended a semantic clustering approach inspired by Offline.com, building "nodes" and index pages within high-volume strategies to avoid orphaning content and sending stronger SEO signals to Google
- Vappy case study: 2,600 custom voice agent use case pages achieved 6% click-through rates despite low domain authority; Tavus sees similar potential with Tavus-branded use case pages (1,000+) that could feed into outbound/PLG workflows

---

## Key Topics

### GrowthX Content Strategy and Workflow

  - 8-week strategy sprint to develop content clusters and quantify opportunities
  - AI-powered workflow engine with hundreds of customizable steps
  - Fact-checking process using Perplexity API and GPT-4 for high accuracy
  - Focus on quality metrics: indexing speed, impressions, click-through rates, and time on page

### Tavus Content Goals and Challenges

  - Current keyword profile doesn't accurately represent Tavus
  - Plans for two content types: blog posts (authored) and perspectives (nameless)
  - Aim to rank for core keywords and improve overall site authority
  - Considering aggressive content output (20-30 articles/week) to build keyword profile

### Use Case-Driven Content Approach

  - Example from Vappy: 2,600 custom voice agent pages created
  - High engagement (6% click-through rate) on programmatically generated pages
  - Potential for Tavus to create similar use case pages (1000+) tied to their product

### Content Distribution and Integration

  - Possibility of using Supabase as a scalable CMS alternative for large page volumes
  - Exploration of tying content strategy to outbound programs or PLG motions
  - Potential integration with tools like Common Room, RB2B, or Koala for workflow automation

---

## Action Items

**Jesse Rowe (Tavus)**
- Review GrowthX proposal when received, prepare questions for follow-up call

**Kyle Gaudreau (GrowthX)**
- Send proposal for GrowthX 8-week content strategy sprint services to Jesse
- Schedule follow-up call with Jesse next week to discuss proposal and answer questions

---

## Transcript
**Marcel Santilli:** Every month for like, you know, a lot of different brands, right?

**Marcel Santilli:** Like, and so, so then we start to craft a content strategy for you.

**Marcel Santilli:** So I'll just show you right now.

**Marcel Santilli:** We are in the process of putting this all into our own platform as a content inventory, but just to give you an idea and a flavor of what we'll do right now at our table.

**Marcel Santilli:** And so like, we'll go and like start to create clusters for you, right?

**Marcel Santilli:** Like, so think of this as like, you know, based on your business, we'll pick different clusters that make sense that based on all the, all the initial calls that we had in week one and two, you know, and then we'll start to do all this analysis on both like your pages.

**Marcel Santilli:** In this case, they have over a thousand pages and try to figure out what is the overall value volume of the opportunity and quantify the opportunities we can go after by difficulty level, right?

**Marcel Santilli:** And then same thing with your competitors.

**Marcel Santilli:** Like, so in this case, we identified 1200 potential opportunities, you know, from competitors.

**Marcel Santilli:** And, and then we start to find, create assignments from those.

**Marcel Santilli:** Which I'll show you in the system what those assignments look like, right?

**Marcel Santilli:** And this is like very early.

**Marcel Santilli:** They're still on the strategy sprint.

**Marcel Santilli:** They're in week five, just to give you an idea.

**Marcel Santilli:** So everything I'm showing you is like week five already.

**Marcel Santilli:** We've already published seven articles for them, you know?

**Marcel Santilli:** And we already identified a thousand pages to go refresh.

**Marcel Santilli:** And we have already done all these artifacts, right?

**Marcel Santilli:** So just to wrap up on the artifacts, like a lot of this is based on like a lot of research we're going to do for you.

**Marcel Santilli:** So bad reviews on your competitors, you know, brand perception, like there's things around like both audience and direct competitors and kind of understanding what's working.

**Marcel Santilli:** So we do a lot of that work that you don't need to review, but it's like it's for us to your company and your space better than anyone else.

**Marcel Santilli:** We'll do things like CMS walkthrough to know how to publish ourselves, you know?

**Marcel Santilli:** And later on, we can integrate and automate that, right?

**Marcel Santilli:** And then all of this should then set up like your environment.

**Marcel Santilli:** And so like, let me just go back here really quickly.

**Marcel Santilli:** And so this is like our Atlas.

**Marcel Santilli:** So this is for a client that's like pretty technical, actually, but called AMBit.

**Marcel Santilli:** But I can pick any client and show you.

**Marcel Santilli:** What you see is like these are all the different artifacts we're generating, right?

**Marcel Santilli:** And so we might start with just your company context.

**Marcel Santilli:** But over time, we might develop like persona-specific artifacts.

**Marcel Santilli:** We might develop, you know, templates and rules and guidelines that are going to get dynamically ingested into our workflows.

**Marcel Santilli:** And I'll show you our workflow engine and the actual pipeline to set up.

**Marcel Santilli:** Sorry to interrupt.

**Marcel Santilli:** This is dope.

**Jesse Rowe:** Could you click into product comparison just out of curiosity?

**Marcel Santilli:** Yeah, absolutely.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Yeah.

**Jesse Rowe:** Yeah.

**Marcel Santilli:** And so this is like for a specific thing here.

**Marcel Santilli:** And what we usually find is like you need to, this is not just, this looks like a prompt in this case, but it's like there's a lot of things that can be pulled as templates themselves of not just what to do.

**Marcel Santilli:** But not to do examples, how to organize the tables, like things like that.

**Marcel Santilli:** And these are generated at like maybe we ran the entire workflow and then we found that there's like a certain pattern that it keeps or a failure mode that we need to correct for.

**Marcel Santilli:** And sometimes, you know, we can solve for that.

**Marcel Santilli:** And when I show you like the full pipeline, a sample pipeline, which is all customized, then I can tell you like, hey, here's where we could change this.

**Marcel Santilli:** You know, but so then like once we have these artifacts, which, by the way, like it's iterated, like one of our clients, the biological one that I mentioned in the healthcare, we're week six with them.

**Marcel Santilli:** We're in version eight of the company context artifact, right?

**Marcel Santilli:** Like so it's highly iterative and that's on us.

**Marcel Santilli:** Like you don't have to do anything to just tell us if we're heading in the right direction.

**Marcel Santilli:** Then what we're doing is setting up these pipelines, right?

**Marcel Santilli:** And so think of this pipeline as a combination of workflows.

**Marcel Santilli:** And what we have under the hood is this is like our execution layer.

**Marcel Santilli:** And obviously, like we're doing all this for you.

**Marcel Santilli:** Like, you don't have to do any of this, like, at all, right?

**Marcel Santilli:** Like, obviously, we're getting inputs from you and you're meeting with you, but the idea is, like, zero homework on you.

**Marcel Santilli:** And over time, like, we're going to open this up more and more so it can be more self-serve, but this is a service for now, right?

**Marcel Santilli:** Like, and then, like, and so, like, just to give an example of, like, this is just one pipeline for a client that's highly technical.

**Marcel Santilli:** So the first step here, the input is, like, workload IAM versus API security.

**Marcel Santilli:** And then if you look at our execution layer, this is the entire workflow that was executed. It went through all of these steps. All of this had zero drag and drops, right?

**Marcel Santilli:** And so in my experience, like, using Aerofs and others, like, for you to build a workflow like this would take me about a week or so.

**Marcel Santilli:** And then anytime there would be, like, a new model, it would take, like, a lot of time to refactor everything.

**Marcel Santilli:** And anytime something failed, it would be really hard.

**Marcel Santilli:** But also, if you're running this workflow and someone else wants to run a different one, everything would get clogged up.

**Marcel Santilli:** So in this one, for instance, it's fetching organic search results, analyzing the search results, fetching the traffic for different keywords, and then grabbing different contacts for it, analyzing the intent, looking at search factors based on what was there, like title search factors, and then scraping every URL from the top results, and then cleaning those articles, analyzing the competitive content for Gap.

**Marcel Santilli:** And then fetching, and then essentially creating an entire assignment from that, right?

**Marcel Santilli:** So I did that in three minutes, and then this is the assignment.

**Marcel Santilli:** So then if you come here in this assignment, you can go, you can, you have an entire canva that has your entire content.

**Marcel Santilli:** So you can say, like, you know what, like, let me grab this audience persona, and, you know, expand on this section, right?

**Marcel Santilli:** And like, anyways, like, I won't do too many of these.

**Marcel Santilli:** But, like, the idea is, like, it can grab a context and then, like, expand and you can kind of have this, like, Canva-like experience, you know, that will, like, start to kind of think through and start to eventually, like, apply changes ideally, right?

**Marcel Santilli:** There you go.

**Marcel Santilli:** So you can see, like, pretty quickly, and then you can accept or reject or editors can accept or reject, like, you know, so I'll reject here because I don't want to talk anything else.

**Marcel Santilli:** But so then, like, the next step, it goes into deep research.

**Marcel Santilli:** And, by the way, all of these are just, like, a sample one, right?

**Marcel Santilli:** Like, we have hundreds and hundreds of these workflows, but what we built under the hood is an AI coding agent that you can give it a plan, and it spits out an entire, like, workflow as code.

**Marcel Santilli:** So all our workflows are represented in code.

**Marcel Santilli:** So when you look at our workflows, it looks like this, you know?

**Marcel Santilli:** And it's way more maintainable and scalable than, like, drag-and-drop tool that tries to abstract code away, right?

**Marcel Santilli:** And the reason for that is because code...

**Marcel Santilli:** Agents are getting way, way, way, way better, and UIs are really hard to manage, you know?

**Marcel Santilli:** And so in this case, it's taking the topic, and it's coming up with research questions, and then it's taking each one of those questions and doing deep research using Perplexity's API and ChatsPT and a bunch of others, and then it's combining those search results.

**Marcel Santilli:** But the really cool thing with this is that, like, it's using all the context, you know, and it has a bunch of very specific things.

**Marcel Santilli:** So it can be, like, you know, mainstream ignore, like, don't  quote agent, right?

**Marcel Santilli:** Like, or the blacklist of things or, you know, additional instructions and context to give and things like that.

**Marcel Santilli:** And then it's going to come up with a plan, and I'll just fast forward through this.

**Marcel Santilli:** It's going draft the article and then fact check it.

**Marcel Santilli:** There's a little formatting bug here.

**Marcel Santilli:** But essentially, you just made a managing editor angry somewhere.

**Kyle Gaudreau:** You know, there it goes.

**Marcel Santilli:** Just a little bug.

**Kyle Gaudreau:** These are internal tools too.

**Marcel Santilli:** But you can see like this is a version of like the fact check step.

**Marcel Santilli:** And I mean, you can see this table already and it's pretty accurate, right?

**Marcel Santilli:** But the reason we know it's pretty accurate is because we have steps like this, which is a fact checker.

**Marcel Santilli:** So what the fact checker does is it takes every single thing we produce up to that point.

**Marcel Santilli:** It splits it into chunks and then extracts every single passage.

**Marcel Santilli:** And you can see the reasoning for extracting the passage and questions it needs to answer in order to verify if it's true or not.

**Marcel Santilli:** And then it researches each one of those passages.

**Marcel Santilli:** And then it is that perplexity.

**Marcel Santilli:** We're using perplexity plus search overall.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** To find evidence if that thing is true.

**Marcel Santilli:** But yeah, in this case, it's perplexity and GPT-4 to analyze GPT-4 to do the analysis or for one.

**Marcel Santilli:** Then we're verifying based on the confidence level.

**Marcel Santilli:** Based on the research, if it's true or not, and then rewriting the content in the same style, tone, and voice, and flow in order to correct anything that needs to be corrected, right?

**Marcel Santilli:** This can be pointed towards any knowledge base, like a vector DB we set up for you, so if we had, say, docs for Strapi—the headless CMS—we use their docs to fact-check, not the general web.

**Marcel Santilli:** You know, like, and, like, this is how many steps it did.

**Marcel Santilli:** How long do you think it would have taken you in Air Ops to run through all these steps?

**Marcel Santilli:** Yeah, that's a good question.

**Jesse Rowe:** I did have a question for you about output specifically.

**Jesse Rowe:** You mentioned you were, like, five weeks in with a client and you wrote seven articles.

**Jesse Rowe:** What does a typical pace look like in terms of content output?

**Jesse Rowe:** And let's just use, like, blog posts as the example.

**Marcel Santilli:** So the reason we do the strategy sprint is all about the definition of them, right?

**Marcel Santilli:** So for instance, for Webflow, they're like, we are now producing like tens of pages a day.

**Marcel Santilli:** But the main reason for that is because like, it's been fairly like programatized, right?

**Marcel Santilli:** Like, and it took a lot longer to go through those steps to now like require a lot less human review in that process, right?

**Marcel Santilli:** For a company like, let's say Airbuy, we're working on thousands of refreshes at the same time, right?

**Marcel Santilli:** Like in a month.

**Marcel Santilli:** But that requires a lot more work to make sure like we know what the source of truth is.

**Marcel Santilli:** For most clients, like our aim is to publish daily.

**Marcel Santilli:** And if you have a lot of surface area already, I think you only have like a couple hundred pages right now.

**Marcel Santilli:** So you don't have a ton of surface area right now.

**Marcel Santilli:** So refreshes are slightly less relevant for you.

**Marcel Santilli:** But, um, so it's all about like, we're in like flood the pipeline mode right now.

**Marcel Santilli:** I would say for the majority of engagements, one to two a day is for editorial, especially for sites like yours that don't have crazy domain authority, right?

**Marcel Santilli:** You're not bad, but it's nothing crazy.

**Marcel Santilli:** What we don't want to do is go too aggressive.

**Marcel Santilli:** Clay is a great example—they're starting to rebound, but you want to be careful of abusing it too much, right?

**Marcel Santilli:** So what we try to do during calibration is look for quality. We measure quality by looking at: okay, let's say we do 10 articles this week.

**Marcel Santilli:** Did they get indexed right away?

**Marcel Santilli:** Did they start to get impressions? Is the click-through rate higher or lower than your site average? If it's higher, great, that's awesome. Is the average time on page higher or lower than the rest of your site? If we have confidence that we're planting seeds that are really high quality, then we can start to scale that.

**Marcel Santilli:** But if you publish a thousand pages and 10 get indexed, you're not doing yourself any favors, you know what I mean?

**Jesse Rowe:** Yeah, that's a good point.

**Jesse Rowe:** Let me give a bit of context.

**Jesse Rowe:** Right now, our keyword profile doesn't describe us at all.

**Jesse Rowe:** What I'm envisioning is two different types of content.

**Jesse Rowe:** This is what we set up at Statsy, like a giant, more than a hundred step AROPS flow, just to put a blog post on the site.

**Jesse Rowe:** The two different types of posts is what we'll have in the near future.

**Jesse Rowe:** We'll have blog and perspectives.

**Jesse Rowe:** Currently, we have a perspectives listing page, but it still links to everything.

**Jesse Rowe:** It's just a blog post under the hood.

**Jesse Rowe:** In the future, we'll have two, and they'll exist at two different URL subfolders.

**Jesse Rowe:** Perspectives will be nameless, written by the Tavis team, and blog posts will be written by an individual.

**Jesse Rowe:** My goal is to get our keyword profile back on track so that we're ranking for things.

**Jesse Rowe:** I've done a few tests, but it's hard to say because you can't exactly do a one-to-one comparison.

**Jesse Rowe:** It takes our site a while to rank for our core keywords.

**Jesse Rowe:** I published a pillar on conversational video AI, and it still doesn't outrank our product pages or even show up as an indexed rank under our product pages, which is concerning from a growth perspective.

**Jesse Rowe:** It's like we really need to get back on track.


**Jesse Rowe:** The reason I'm saying this is because I'm a little less concerned up front about, like, the flooding aspect.

**Jesse Rowe:** I think it would be safe to target 20-30 articles a week published as perspectives.

**Jesse Rowe:** The ones we like, we'll put a human name to it—say "Jesse wrote this"—give it a blog image, put it on our blog instead of the perspectives page, with CTAs and the full treatment.

**Jesse Rowe:** But I think it's okay if we have generic "written by the Tavus team" articles going out in mass, at least until we're able to start ranking for our core terms.



**Marcel Santilli:** Our recommendation overall is just personal opinion here.

**Marcel Santilli:** Obviously, we've all been surprised on so many things and things are changing so quickly.

**Marcel Santilli:** We like the Offline.com model—instead of just blasting a thousand pages, if you're going to do high volume, be very thoughtful about the clusters and nodes and how those things correlate.

**Marcel Santilli:** Think about the information architecture. You can still have a flat URL structure.

**Marcel Santilli:** Subfolder like /perspectives/. But then you want to create a lot of index pages, right?

**Marcel Santilli:** For instance, one of our directors was head of SEO for TripAdvisor and then Fanatics. A lot of these pages are listing pages—essentially index pages, right?

**Marcel Santilli:** There are ways to do it if you're going to go super aggressive.

**Marcel Santilli:** Then you have this one page that lists 20 pages, and now 192 pages are orphaned completely. That doesn't help.

**Marcel Santilli:** What we want to do is pick things in the longer tail with high confidence that we can knock out of the park and rank well, so we start by sending really high quality signals to Google, right?

**Marcel Santilli:** For instance, you can target keyword difficulty 10-15 topics related to things you already rank for, win some of those, plant 50 of those seeds, and then add to it.

**Marcel Santilli:** Branch off from those in clusters, semantically related to ones you already rank for and that send high quality signals.

**Marcel Santilli:** It tends to do better. You can spray a little, but a portfolio strategy where 80% is core—building off what's already working—and moving toward higher intent tends to work well. There's a bunch we'll calibrate during the sprint.

**Marcel Santilli:** But here's what I have very high confidence in.

**Marcel Santilli:** I was the heaviest user of Aerofs (workflow automation), so I know all the pain points you're going to go through.

**Marcel Santilli:** For some people, it might still be okay if they want to be hands-on with building.

**Marcel Santilli:** It all depends on what you're optimizing for.

**Marcel Santilli:** What we try to do is de-risk the whole thing as much as possible with the eight-week strategy sprint. Then either of us can walk away—we can fire you or you can fire us.

**Marcel Santilli:** Which is nice because the burden is on both of us. If I knock it out of the park and we work together well, we can proceed. If not, that's okay too. We want to work with really cool companies and people. We have great insights from what we did with Vappy—I want to show you something really quickly. Maybe not as a first project, but it's really cool.

**Marcel Santilli:** We haven't published all 2,600 yet, but 2,600 are ready to publish—custom voice agent pages for every possible use case you can imagine. These are getting 6% click-through rates on impressions. It's insane.

**Marcel Santilli:** Hmm.

**Jesse Rowe:** Yeah, when Kyle called out Vappy, this is definitely the one with the most common denominator.


**Jesse Rowe:** That's some of the things I'm thinking.

**Marcel Santilli:** This workflow is really awesome. The input is literally just the use case.

**Marcel Santilli:** It goes through a bunch of different steps.

**Marcel Santilli:** Then we use Supabase.

**Marcel Santilli:** All of this goes into a Supabase database after human review. Every aspect of the page—instead of going to a CMS and matching fields—is in a database, which is more scalable, just for this section of their site.

**Marcel Santilli:** We designed and built the page as well.

**Marcel Santilli:** Interesting.

**Jesse Rowe:** And they're getting all that on their end to work with from Supabase?

**Marcel Santilli:** Exactly. Supabase serving as the CMS—it's a database because with thousands of pages, it reduces build time significantly.

**Marcel Santilli:** Yeah, interesting.

**Jesse Rowe:** I see a similar use case with us—a use case for the use cases.

**Jesse Rowe:** We built a site too, in two weeks for Augment Code.

**Marcel Santilli:** They're a Cursor competitor—they're killing it.

**Marcel Santilli:** It's a similar case—we built the whole experience, brand, bought the domain, and all of that.

**Marcel Santilli:** There are cool things like that we can do. You guys are experimenters.

**Marcel Santilli:** That's the stuff we thrive on—working with people that want to do cool things.

**Marcel Santilli:** Do the table stakes stuff, but also do cool stuff.

**Marcel Santilli:** The strategy sprint allows us to figure out if there are opportunities like that while building the right foundation.

**Marcel Santilli:** Worst case, you get these artifacts. Even if you just want to use Aerofs, you can take the artifacts and improve everything you do.

**Marcel Santilli:** But that's the summary.

**Jesse Rowe:** I love it. Great rundown.

**Jesse Rowe:** One of the things—that example was something I was talking with Kyle about last night, and then I talked with Mario about it. He was selling you guys hard.

**Marcel Santilli:** Mario's amazing. I love him. He was like, "Dude, I'm telling people we love you."

**Marcel Santilli:** And I was like, "I know, man. You and me too."

**Kyle Gaudreau:** We appreciate it.

**Kyle Gaudreau:** He's not an investor.

**Marcel Santilli:** He has no equity and we don't pay him.

**Jesse Rowe:** There are overlying themes between what Airbyte's doing and what we're doing here.

**Jesse Rowe:** We want to focus on use cases—something we're monitoring closely in terms of how adoption is actually transcending.

**Jesse Rowe:** And figuring out where Tavus can come into play as that layer for them.

**Jesse Rowe:** I'm thinking a large number—a thousand use cases, let's try building that and then eventually plug it into something like a Tavus interface as a template.


**Marcel Santilli:** One thing with Vappy that took a lot of work was figuring out how to create JSON configs so the simulator—essentially their product's API and component—was configured in relation to each use case.

**Marcel Santilli:** Then programmatize the creation of the audio snippets.

**Marcel Santilli:** Do you guys have APIs?

**Marcel Santilli:** With HeyGen, the problem was we were doing all this work, and they said, "Yeah, we don't have an API yet."


**Marcel Santilli:** It was just a page with a screenshot.

**Marcel Santilli:** It's not going to be as good as Vappy's approach.



**Marcel Santilli:** Because you need to send signals that people are spending five minutes on the page, not five seconds.

**Marcel Santilli:** So the use case pages we built for HeyGen never performed as well as they could have.

**Marcel Santilli:** With Vappy, it's the complete opposite.

**Marcel Santilli:** Even with no domain authority, they get immediate high click-through rate, high engagement, high time on page.

**Marcel Santilli:** Yeah, yeah, totally.

**Jesse Rowe:** Time on page is what I was thinking about last night with Kyle—how that could be a drastic outlier.


**Jesse Rowe:** Yeah, we have the technical capability to make that work.

**Jesse Rowe:** Is anyone doing anything downstream with this data?

**Jesse Rowe:** Obviously you want the traffic, but I'd like to tie that back into a system of record—some component where we can include that messaging into the next touchpoint.

**Jesse Rowe:** If anyone's tying these programmatic components into an outbound program or PLG motion.

**Jesse Rowe:** Yeah, yeah.

**Marcel Santilli:** We've used Common Room, RB2B, or Koala. There are things we can do with workflows—all our workflows can be exposed via API.

**Marcel Santilli:** The best thing you can do is create these pages—like what we're doing for Vappy. When someone searches for a voice agent or use case, you know everything you need to send them the perfect outbound message.


**Marcel Santilli:** If you create surface areas that are higher intent—not selling or pushing product—and that have enough signals or inputs you can use to personalize outreach.


**Marcel Santilli:** Everything else becomes easier. Whether you're using Clay to do the outbound or another tool—we have partners like UnderStory, an agency we love, that we recommend for outbound.

**Marcel Santilli:** We don't focus on outbound itself—buying domains, warming IPs, all that—because it's a bit far from our core.

**Marcel Santilli:** Our workflows can be exposed via API. We want to create high quality signals that pull your audience organically, then you can use them to drive conversion, signups, or subscriptions.

**Marcel Santilli:** We also run newsletters for clients like Udemy—weekly high-value editions.


**Marcel Santilli:** I wouldn't start there for you because you have so much surface area to build—you're at 196 pages.

**Marcel Santilli:** There's a lot of work to do here—and it needs to be fast and high quality.

**Marcel Santilli:** Honestly, your time is better spent giving us insights and letting us execute than spending tens of hours tweaking workflows yourself. You'll have better insights that way.

**Marcel Santilli:** Then you can open up other channels.


**Marcel Santilli:** Okay.

**Jesse Rowe:** That makes sense. I totally hear you—the downstream sync being less of a priority.


**Marcel Santilli:** I think Kyle mentioned we have one more spot in July, then we're booking the second week of August.

**Marcel Santilli:** We have a dedicated strategy sprint team, and I'm part of it.

**Marcel Santilli:** We only do two kickoffs a week.

**Marcel Santilli:** That's why we're usually booked about six weeks out.

**Marcel Santilli:** It's low risk and you get so much value from it.

**Marcel Santilli:** It's essentially a loss leader for us—makes it easy for people to get started.

**Marcel Santilli:** And we have lots of references—people who've gone through it and examples.

**Marcel Santilli:** Okay, awesome.

**Jesse Rowe:** I'll follow up with Kyle on those items. Thanks for the time.

**Marcel Santilli:** We should hang out more and do some stuff together. That'll be fun.


**Kyle Gaudreau:** You mentioned Stillman? I used to work at Trey a few years ago when they were on Stillman. I was trying to remember the address. That's where their office was. That's cool if you're in the old Trey spot.

**Kyle Gaudreau:** Happy to send over a proposal and answer any questions. Can you find time next week to catch up?

**Kyle Gaudreau:** I'm happy to do whatever it takes to make sure you feel good about moving forward. This seems like it'll be a ton of fun.

**Kyle Gaudreau:** I'll send over some stuff soon and looking forward to catching up after the weekend.

**Jesse Rowe:** Same here.

**Kyle Gaudreau:** Great. Appreciate it!
