# Shaping with Ryan with Ryan Singer

<metadata>
date: 2026-02-17
time: 17:02 UTC
duration: 182 minutes
organizer: daniel@growthxlabs.com
participants: Daniel Lopes, Ryan Singer
fathom_recording_id: 123029696
fathom_url: https://fathom.video/calls/569081157
share_url: https://fathom.video/share/5DzpxHN258hc4_s8dWeePqsKVzvF9i6c
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Daniel and Ryan defined a game-changing optimization framework for the Content OS product that shifts from overwhelming data tables to an action-oriented "heads-up display." The framework classifies pages into three buckets—Fix Now (critical issues), Unrealized Potential (growth opportunities), and Dead Zone (pages to prune or replace)—allowing teams to prioritize work instead of drowning in 700+ pages of declining traffic. The March release will focus on building the data foundation for this framework, cutting complex UI features to concentrate engineering effort on the core logic that translates expert judgment into opinionated software recommendations.

---

## Context

Daniel Lopes is the product lead for Content OS, a tool that helps B2B companies (particularly those in high-stakes industries like construction and financial services) manage their website content at scale. The problem: modern websites have become essential to business, but managing hundreds of pages—keeping them fresh, relevant, and optimized—has become impossible to do manually. Ryan Singer, a legendary product strategist (formerly at Basecamp), was invited to shape the product vision and design approach. This 3-hour working session was a collaborative "shaping" sprint to evolve the product strategy from high-level vision into a concrete framework and UX direction.

---

## Relevance

- **To Content OS Product:** The session delivered a paradigm shift from data-centric to action-centric design. The three-bucket framework (Fix Now, Unrealized Potential, Dead Zone) with nested clustering becomes the core organizing principle for the product. March engineering roadmap now has a clear prioritization: build the data model and logic for this framework before adding UI polish.

- **To GrowthX Services Delivery:** GrowthX helps clients set content strategy and execute it—understanding how Content OS surfaces priorities will directly inform how GrowthX advises clients on website content optimization. The "Fix Now vs. Unrealized Potential" distinction maps to GrowthX's diagnostic and growth engagement models.

- **To Future Strategy Work:** Ryan Singer's involvement proved high-leverage and is being formalized into a longer-term engagement (monthly sessions, potential equity) to continue shaping product strategy and design. This signals GrowthX is willing to invest in world-class external talent when the ROI is clear.

---

## Overview

- **New Optimization Framework:** Defined a framework for surfacing optimization tasks, classifying pages into three action-oriented buckets: `Fix Now` (critical issues), `Unrealized Potential` (growth opportunities), and `Dead Zone` (pages to delete or replace).
- **UI Shift to Action:** The UI will shift from a data-heavy table requiring user filters to an opinionated, action-oriented heads-up display. This surfaces the most urgent work first, reducing user effort and preventing critical issues from being missed.
- **March Scope Refocus:** The March release will prioritize building the data foundation for this new framework. This requires cutting complex UI features (e.g., advanced sorting, pagination) to focus engineering effort on the core logic and data model.
- **Ryan Singer's Role:** Ryan Singer's involvement is a high-leverage multiplier, accelerating product strategy and design. A formal, long-term engagement (e.g., monthly sessions, equity) was proposed to secure this strategic support.

---

## Key Topics

### Problem: Overwhelming Data & Inaction

  - Current dashboards present raw data (e.g., 700+ pages, declining traffic) without clear prioritization, leading to analysis paralysis and missed opportunities.
  - The goal is to translate expert judgment into software, creating an opinionated system that tells users what to do, not just what the data is.

### Solution: An Action-Oriented Optimization Framework

  - The team defined a framework to classify pages based on their health and potential, creating clear, actionable work items.
  - **1. `Fix Now` (Critical Alerts)**
      - **What:** High-impact pages with severe issues that require immediate attention.
      - **Why:** To prevent or reverse significant traffic/revenue loss.
      - **Examples:**
          - A major traffic driver's performance has dropped into "free fall."
          - A high-impact page has a broken link, factual inaccuracy, or violates a critical style guide rule.
  - **2. `Unrealized Potential` (Growth Opportunities)**
      - **What:** Pages with clear opportunities to improve performance.
      - **Why:** To capture untapped growth.
      - **Examples:**
          - A page gets impressions but zero clicks (promise is off).
          - A page is "almost there" (e.g., on page 2 of search results).
          - A page is stale and needs a refresh to maintain relevance.
  - **3. `Dead Zone` (Pruning & Refactoring)**
      - **What:** Pages that are low-value and need to be removed or completely overhauled.
      - **Why:** To improve overall site quality and focus crawl budget on high-performing content.
      - **Action:** Requires human judgment to decide between:
          - **`Rip & Replace`:** Overhaul content on a URL with existing equity (e.g., backlinks).
          - **`Prune & Redirect`:** Delete content with no equity and redirect its URL.

### UI Strategy: From Data to Action

  - The UI will be redesigned around this framework, shifting from a generic data table to an action-oriented heads-up display.
  - **New Structure:** The `Learn & Improve` section will be organized into three distinct, collapsible buckets: `Fix Now`, `Unrealized Potential`, and `Dead Zone`.
  - **Nesting:** Content clusters (e.g., by topic, content type) will be nested *inside* each signal bucket. This allows users to understand patterns within the most urgent work (e.g., "Why are *these* pricing pages in free fall?").
  - **March Scope:** To enable this shift, the team will cut complex UI features (e.g., advanced sorting, pagination) from the March release. This focuses effort on building the core data model and logic for the new framework, which is the most critical component.

---

## Action Items

- **Daniel:**
    - Revise the March scope to prioritize building the data foundation for the new optimization framework.
    - Cut complex UI features (e.g., advanced sorting, pagination) from the March release.
    - Implement the new UI structure with `Fix Now`, `Unrealized Potential`, and `Dead Zone` buckets, using nested clustering.
- **Ryan Singer:**
    - Confirm availability for future sessions by **Wednesday, Feb 28th**.

---

## Transcript
**Daniel Lopes:** Hey, Ryan, good to see man.

**Ryan Singer:** All righty.

**Ryan Singer:** Good morning.

**Ryan Singer:** There you go.

**Daniel Lopes:** Firefly, right?

**Daniel Lopes:** Yes, I have.

**Daniel Lopes:** Okay, sure.

**Daniel Lopes:** Yes, I have.

**Daniel Lopes:** Fireflies.

**Daniel Lopes:** All the notetakers and all the records.

**Daniel Lopes:** All the notetakers and all the things.

**Ryan Singer:** We're outnumbered.

**Daniel Lopes:** Ryan, you would be proud of me.

**Daniel Lopes:** I kind of try to, you know, draw my inner Ryan during All Hands last week and presented the whole thing into y'all draw.

**Ryan Singer:** Hey.

**Daniel Lopes:** I'm learning from you, my friend.

**Ryan Singer:** All right.

**Daniel Lopes:** No, I, I, I.

**Ryan Singer:** Yeah, let's see.

**Daniel Lopes:** I thought it was pretty easy.

**Daniel Lopes:** Okay, so I started here of like, here's the shift, you know, we're seeing one buyer to now three buyers and agents that influence the buyers.

**Daniel Lopes:** The reward function is like, what does every company want to grow and do more with less?

**Daniel Lopes:** One is about like growth, another one is leverage, you know, so where do you start?

**Daniel Lopes:** We believe the website is your biggest driver, influences everything, it's what you can control, most transactions happen here, compounds it's done right, it's measurable, and it drives both growth and leverage, but it's getting harder and harder to do, because most pages do feed more answers, it's got to stay fresh and high quality, always hard to manage.

**Daniel Lopes:** So the website went from important to existential, and the job got it 100 times harder.

**Daniel Lopes:** Totally.

**Daniel Lopes:** Which then now, what is the job to be done, is drive compounding growth through your website, which means manage page, create pages.

**Daniel Lopes:** do this.

**Daniel Lopes:** So, We'll

**Daniel Lopes:** Optimize continuously, you know, and so you keep them organized, current, healthy, and performing, expand your surface area, more answers for buyers, more content for AI to site, more signals for training bots to learn, every page continuously, fresh, quality, relevance, conversion, not once, every single week.

**Daniel Lopes:** That is impossible to do manually.

**Ryan Singer:** Yes, it is.

**Daniel Lopes:** And how do you even know if it's working?

**Daniel Lopes:** so you got to think about like leading to lagging and ultimately like the promised land is AI handles production, optimization, and learning to scale.

**Daniel Lopes:** Humans provide strategy, quality judgment where it matters.

**Daniel Lopes:** The system gets smarter, every output, every page, every week, growth compounds across all three audiences, buyers, AI, and training bots.

**Daniel Lopes:** And then this is like, I need to go into this, but this is kind of like.

**Ryan Singer:** Yeah, then you come into how, so like you sort of sold them on like why, and now this is sort of the how of how you actually do it?

**Daniel Lopes:** Yeah, then it's like, I try to connect it with like what we built because we have like infrastructure, data, platform, services, and distribution.

**Daniel Lopes:** And there's

**Ryan Singer:** It's such a no-brainer.

**Ryan Singer:** There's, like, so, there's so much, like, raw material.

**Daniel Lopes:** You client for free?

**Daniel Lopes:** We actually just dropped one of the ones that we were helping for a while that was, like, kind of, like, a partner, and we were doing, essentially, like, a pro bono, if you will, because it's, like, it was cool work, but we should think about that.

**Daniel Lopes:** Because, but, anyways, yeah.

**Daniel Lopes:** But it's interesting to, like, feel the problem, you know?

**Ryan Singer:** It's, like, so clear that, like, the problem is literally getting all the material out there, you know, and being, like, doing it strategically, like, the combination of taking some time to do it strategically, which you guys, like, help with on the front-loading, but then just all this work, you know, of, like, writing the articles and everything, like, even when you have a lot of source material, you kind of know what you want to say, you know?

**Ryan Singer:** It's, I totally get it.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** I've been doing the same thing.

**Daniel Lopes:** I just built a company in handbook.

**Daniel Lopes:** I had, like, context project.

**Daniel Lopes:** And then I had all my files, all my knowledge and everything.

**Daniel Lopes:** And I was trying to massage it into, like, handbook.

**Daniel Lopes:** But because I have so much of the good context and things, like, I was able to write, like, like, 70 doc pages, like, the equivalent of GetLab's, like, handbook.

**Ryan Singer:** That's amazing.

**Daniel Lopes:** You know, a single day, pretty much.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So, same setup that you have with, like, Maclify and Microsoft files and all that.

**Daniel Lopes:** Yeah.

**Ryan Singer:** Mm-hmm.

**Ryan Singer:** Yeah.

**Daniel Lopes:** I got to clone your skills still.

**Daniel Lopes:** It's on my to-do list.

**Ryan Singer:** Ah, yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So, I, all right.

**Ryan Singer:** So, so what's, um, what's on the docket for today?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Uh, did you have time to watch the, the first video that I sent you?

**Daniel Lopes:** The one that's, like, short one?

**Daniel Lopes:** I sent, like, yesterday midnight.

**Daniel Lopes:** So, I can, I can walk.

**Ryan Singer:** You know, I actually didn't get an email from you.

**Daniel Lopes:** Huh?

**Ryan Singer:** I thought that, um...

**Daniel Lopes:** And maybe I didn't send?

**Ryan Singer:** I that...

**Ryan Singer:** I...

**Ryan Singer:** I...

**Ryan Singer:** I...

**Ryan Singer:** Thought that I didn't get anything from this time.

**Daniel Lopes:** Look at this.

**Ryan Singer:** Let me share my screen.

**Ryan Singer:** Which AI secretary do we have to fire?

**Daniel Lopes:** This is the best thing I have on my screen.

**Ryan Singer:** Oh, gosh.

**Ryan Singer:** So there are still some...

**Daniel Lopes:** The dog ate my homework, Ryan.

**Ryan Singer:** Yeah.

**Ryan Singer:** Superhuman, by the way, superhuman has no idea who I am.

**Daniel Lopes:** Rapper, songwriter, from Port St.

**Daniel Lopes:** Lucie.

**Daniel Lopes:** Anytime I see this guy, like, oh, who's the rapper?

**Daniel Lopes:** Is the rapper?

**Daniel Lopes:** the rapper?

**Daniel Lopes:** Oh, my God.

**Ryan Singer:** That's amazing.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So maybe I walk you through the progress I've made, just to give you context.

**Daniel Lopes:** Yeah, let's do that.

**Daniel Lopes:** Automating your workflow for, like, assuming how the framework works and using your workflow as an example.

**Daniel Lopes:** Basically, it's a scaffold.

**Daniel Lopes:** The thing is, the way to think of...

**Daniel Lopes:** We have this AI framework that's all file system based, so prompts, tracing, the workflow, the steps of the workflow are all in code and in the file system, and we have a bunch of cloud skills and plugins that sits on top of this, so think of like a rail scaffold, but like on steroids, you can essentially just create almost anything by just talking to it, so I did that in the video, so that's the second video.

**Ryan Singer:** Well, yeah, so if you can just send me the email once the blocking issue is fixed, then I'll spend time checking that out, you know, off the call, because probably it's not relevant for you guys for the time we have now, but I'll look forward to seeing that.

**Daniel Lopes:** Yeah, that is actually like another project, so we have these three things happening, we actually could talk about that at the end, but we have, there's something we're doing on check that, that's like top of funnel, and I saw you, you tried to use team builder, and like you check out the website.

**Daniel Lopes:** And maybe we can go through that a little bit today, but as a highlight, we have a check tab, it's a top-of-funnel monitoring the market, monitoring how the LLMs perform, and then on the other side, we have the content OS that we've been working on, and under those two things, we have the framework, and we've been doing a lot of custom work for content creation that's much harder than normal pages, that you're not going to be able to do in the content OS project.

**Daniel Lopes:** So we have a team of five people, that's our forward deploy team, they decide, okay, this goes into this pipeline kind of work, or this goes into a custom agent kind of work.

**Ryan Singer:** Okay.

**Daniel Lopes:** And we have this part of the business that we want to grow pretty aggressively, an agency on top of it, as soon as we make the framework open source.

**Daniel Lopes:** And just to give you an example of the kind of stuff we do, like Lovable is a good one.

**Daniel Lopes:** So Lovable, they came to us.

**Daniel Lopes:** With the idea, we actually used the framework to investigate all the activity that happened on another player that was very similar to Lovable, one of the clients that we had.

**Daniel Lopes:** And we realized all the people were struggling with prompting.

**Daniel Lopes:** So instead of prompting, can we create a giant list of catalogs of templates that you can use?

**Daniel Lopes:** you start from there.

**Daniel Lopes:** Problem is that Lovable was not really good at one-shotting high-quality stuff, so you had to do a back-and-forth conversation.

**Daniel Lopes:** So we, until you create a website, like a template, and for the template, we also need a page around the template.

**Daniel Lopes:** So we ended up creating this, what's in there, a home page?

**Daniel Lopes:** Oh, chain, yeah, right here.

**Daniel Lopes:** So Discover Templates, for example.

**Ryan Singer:** the issue was that Lovable, as a GrowthX client, didn't know what to prompt the OS tool?

**Ryan Singer:** Or is this about Lovable's clients?

**Daniel Lopes:** Yes, so think of it as like, you're coming in.

**Daniel Lopes:** And you're trying to get to something that's, like, good, right?

**Daniel Lopes:** And they don't know how to prompt, and all the user-generated content was pretty garbage out there.

**Daniel Lopes:** It's a lovable user.

**Ryan Singer:** Yeah, they, this is like the content, this is like the content team on Lovable, or this is the lovable user using the Lovable app?

**Daniel Lopes:** This is, like, a lovable user.

**Ryan Singer:** Ah, got it.

**Ryan Singer:** Yeah, yeah, okay.

**Daniel Lopes:** They're going to Lovable or finding out about them.

**Ryan Singer:** Ah, totally, okay.

**Ryan Singer:** Yeah, no, this problem I know about.

**Ryan Singer:** Yeah, people don't know how to prompt.

**Ryan Singer:** Exactly, and then they just kind of, it's garbage in, garbage out, right?

**Daniel Lopes:** Yeah, and, but then also from an SEO perspective and growth perspective, they, like, they're now competing with Wix, who bought one of their competitors, Base44, and they have an F-ton of traffic, like, millions and millions of people, because they have all these templates, and templates is, like, a huge driver of traffic.

**Ryan Singer:** And Wix, Wix and Squarespace, they already understood this dynamic very well, which, you know, because they knew, they, they had all these website builders, and they knew that.

**Daniel Lopes:** If you didn't give people like a starting point, that people didn't know what to do.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** And it's where a lot of the traffic is.

**Daniel Lopes:** So from a content perspective, we're like, let's go create a template library that's more like a starter kit library of like, but how do you build that without having a network of highly qualified designers who built it on like a reusable foundation?

**Daniel Lopes:** It's like freefall, , garbage, like prompts.

**Daniel Lopes:** And so we gave them essentially like the strategy, how to like think about it.

**Daniel Lopes:** We created this experience as well as the actual individual template pages.

**Daniel Lopes:** And then what Daniel is going to show you is how we programatize going from ideation all the way to fully built website programmatically with like seven hours of like design engineers, like prompting, tweaking, and polishing down to about an hour now.

**Ryan Singer:** Amazing.

**Ryan Singer:** I see.

**Ryan Singer:** Because this isn't something that you can just do in a markdown file.

**Ryan Singer:** So that's why it's not possible to do it in ContentOS, but you needed to actually build out this custom workflow using Output.ai in order to orchestrate all that?

**Daniel Lopes:** Exactly.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So we have this normal editorial clients that need normal pages on the website.

**Ryan Singer:** That's fine.

**Ryan Singer:** That's what we optimize the ContentOS for.

**Daniel Lopes:** And then we have a bunch of clients that are like, I need to create something that's very different or something that's very specific to my needs.

**Daniel Lopes:** In this case, for Lovable, it was like an agent that would have a back and forth, receive a screenshot, have a back and forth, turns the screenshot into React code, and then test it with the Lovable API to see if it's live.

**Daniel Lopes:** So that is one.

**Daniel Lopes:** Another thing we do for AirBuy, similar ideas.

**Daniel Lopes:** AirBuy is a bunch of plugins.

**Daniel Lopes:** When a plugin gets, shows up in their app store, see the pull request of the documentation that becomes a page on their website.

**Daniel Lopes:** So we do a bunch of things like this.

**Daniel Lopes:** They're very, very unique.

**Daniel Lopes:** And it's only possible because of the...

**Ryan Singer:** Yeah, I get it.

**Ryan Singer:** Totally.

**Daniel Lopes:** And we're going to grow that team.

**Daniel Lopes:** have four or five people there.

**Daniel Lopes:** As we finish the content OS to be like more self-serving product, the solutions engineer team can shift to be an engineering team for this kind of custom work on top of the framework.

**Ryan Singer:** Wow.

**Daniel Lopes:** So we have these three things in motion.

**Daniel Lopes:** The top of the project, the content OS to normalize pages and intelligence on top of your website, and output AI for any kind of content or any kind of agent engine.

**Daniel Lopes:** don't know.

**Daniel Lopes:** But we're trying to start with just focused on growth.

**Daniel Lopes:** Yeah, if you go to the studio and show them like the 27 workflows that power this, pretty cool.

**Daniel Lopes:** You just search for Lovable.

**Daniel Lopes:** So check this out.

**Daniel Lopes:** Like Lovable templates, these are all the different workflows decomposing it.

**Ryan Singer:** So is this a frontend to output.ai or what it?

**Daniel Lopes:** Yeah, this is.

**Daniel Lopes:** This is an alpha that we're not going to launch, it's just for internal inspection, and then, because we didn't have the time to make this look legit and fun, so we're going to launch just the code part, and essentially we have 27 chunks of code that we wrote for them specific to this problem.

**Daniel Lopes:** But, like, figuring out the typography, the actual words that go on these starter kit websites, the structure, the, like, page structure, the content generator, the image generator, the, like, you know, like, there's a cleanup part, there's, like, there's all kinds of things that are, like, essentially decomposing the process of building, programmatically building a website template.

**Ryan Singer:** This reminds me of what, um, is this, is this different from what, like, the DSPi guys are talking about, like, when they're, like, this idea of, like, you're supposed to kind of, like, break apart all of this, like, prompting and stuff into modular pieces, this is, like, a different take on that similar, uh,

**Daniel Lopes:** Yeah, it's a similar idea.

**Daniel Lopes:** DS5 has a lot of the self-improving part of the prompts.

**Daniel Lopes:** And our take was more like, instead of thinking about the prompts, we think about the workflow itself, but sometimes you need to be there.

**Ryan Singer:** Right.

**Daniel Lopes:** Yeah.

**Ryan Singer:** So, yeah, this is more like a practical software build, like standing up systems stuff, right?

**Ryan Singer:** Like, uh-huh.

**Daniel Lopes:** Yep.

**Daniel Lopes:** So you see, I will send you the code for the one that I did for the audio to transcript.

**Daniel Lopes:** Cool.

**Daniel Lopes:** And so it's essentially mini apps.

**Daniel Lopes:** They're like heavy on LLMs.

**Daniel Lopes:** So there's like a, instead of like views and rails, you have a prompts, dot prompts file that has all the settings for temperature, the variables, the interpolation, everything.

**Daniel Lopes:** And has all the things for like retrialing when LLMs fail, has the judgment to go back when LLMs is below quality.

**Daniel Lopes:** So there's all these things baked in.

**Daniel Lopes:** Awesome.

**Daniel Lopes:** then the UI is essentially, you don't have to code, but you can if you want to.

**Daniel Lopes:** Mm-hmm.

**Ryan Singer:** Yeah, cool.

**Daniel Lopes:** so this is.

**Daniel Lopes:** The whole thing that we have, like, so we have this user interface, we have like 300 plus workflows, some are very custom to some clients, and then all the AI features that we're talking about on the ContentOS are also powered by the framework.

**Daniel Lopes:** And the plan is to launch the framework in this next month, and then we're going to grow the engineering team around this custom work for some of the more premium clients, and we start hiring solutions engineers for the ContentOS to do the workspace calibration, and then kind of, like, split the lanes more clearly.

**Daniel Lopes:** So those are, like, essentially three layers of the business that we have that I wanted to show you real quick, just to give you the context.

**Ryan Singer:** Awesome.

**Daniel Lopes:** Yeah, so out of our session last night.

**Ryan Singer:** Hey, what is this new stuff?

**Daniel Lopes:** Yeah, oh, man.

**Ryan Singer:** Yeah, so out of your session last week, we changed everything and decided to redesign the whole product.

**Ryan Singer:** Okay, real quick.

**Daniel Lopes:** Yeah, real quick.

**Ryan Singer:** Okay, Daniel doesn't sleep or...

**Daniel Lopes:** Yeah, so the idea, I pretty much took your ideas and tried to implement here.

**Daniel Lopes:** So the setup now is two screens.

**Daniel Lopes:** It will take you to the place that you want to do the work, and you can add notes if you're skipping or for whatever reason.

**Daniel Lopes:** And even if you're not skipping, it's good to have the solutions team that will be setting up the workspace to explain what they did.

**Daniel Lopes:** And then if it does not apply, so same idea from before.

**Daniel Lopes:** And then as you complete, it would, like, finish the bar here at the top.

**Daniel Lopes:** I went ahead with the same, exactly the same menu that we had thought about.

**Daniel Lopes:** So, like, learn and improve.

**Daniel Lopes:** Learn and improve will be all of your pages, including the ones that get it built.

**Daniel Lopes:** New page opportunities for new page opportunities.

**Daniel Lopes:** And progress snapshots are essentially the report.

**Daniel Lopes:** There's like a few things that we have from the legacy project that folks are still going to be using for a while.

**Daniel Lopes:** That's the workflow projects.

**Daniel Lopes:** This is here just as, I don't want to know if we're going to keep it, but that's the old analytics.

**Daniel Lopes:** Might be usable for inspecting if you're getting the data there or if like just poking around, but maybe we don't even have to surface.

**Daniel Lopes:** And then I also added meetings.

**Daniel Lopes:** Meetings is one thing that, as we were discussing last week, a couple of weeks ago, it was a challenge of like, not always you can just let AI do the research.

**Daniel Lopes:** There's like a lot of things that comes from the sales meetings, from the intake meetings with the client, the kickoff meeting with the client.

**Daniel Lopes:** They're sharing things of like, who are the competitors?

**Daniel Lopes:** Who are their personas?

**Ryan Singer:** And you're asking the right questions to draw out things that they wouldn't have shared otherwise.

**Ryan Singer:** I totally have this in my workflows too.

**Ryan Singer:** Like I have these interviews with people.

**Ryan Singer:** Like dangle like the shiny object in front of them.

**Ryan Singer:** That's like, this is why this matters, right?

**Ryan Singer:** Like learn and improve and new page opportunities.

**Ryan Singer:** Like we're, we're trying to, to, to make it clear, like what I get out of this and why it helps me, you know?

**Ryan Singer:** So that's just something to think about here.

**Daniel Lopes:** Yeah, no, that makes sense.

**Daniel Lopes:** Because like we have, like every client has these two phases.

**Daniel Lopes:** One is the calibrate, like intake phase, or like the, the strategy spring phase, how to call it.

**Daniel Lopes:** And the first part of this phase is essentially, if they go to this setup here, and they do all this seven steps, like record all your meetings, make sure you understand their company and products, record that in the system, define their personas, define their taxonomy, calibrate their style, validate their style, with simple articles by annotating them, connect their Google search console, connect their analytics.

**Ryan Singer:** By the way, validate, validate their style is so much.

**Daniel Lopes:** Much better than sample articles.

**Daniel Lopes:** That's a good, yeah.

**Ryan Singer:** Calibrate, verbs.

**Daniel Lopes:** So calibrate their style, validate their style, and sample articles is how you do it.

**Daniel Lopes:** Like that's, yeah.

**Daniel Lopes:** Yeah, that's a good, yeah.

**Daniel Lopes:** That makes sense.

**Daniel Lopes:** I'll make note of that for life.

**Daniel Lopes:** Anyway, and then you have to collect your website.

**Daniel Lopes:** Then we can start, that's the minimum that we need to do the work.

**Daniel Lopes:** And if the team spends two weeks doing this, that's great.

**Daniel Lopes:** You know, like, because for now on, everything is going to be fine.

**Daniel Lopes:** But like, often they will just jump straight into this.

**Daniel Lopes:** And then it's total .

**Daniel Lopes:** So the system, so that's how we do today in different ways.

**Daniel Lopes:** So like, it was like, people will use Notion, Airtable, Marcel has a bunch of things.

**Daniel Lopes:** The Notion that they need to follow, then we're making that into the system now.

**Daniel Lopes:** So you have to go through this and click on those buttons and help, help you do some of the lag work here.

**Daniel Lopes:** So I had to go into perplexity and research.

**Daniel Lopes:** That kind of stuff, or post-processor meetings.

**Daniel Lopes:** So the meetings for, it's for this two phases.

**Daniel Lopes:** It's the intake phase when you're calibrating and then you're testing with the client.

**Daniel Lopes:** then afterwards, we also want to have some sort of recipes that will look for, is this client upset?

**Daniel Lopes:** Like, is this client showing signs of like positive sentiment?

**Daniel Lopes:** Are they hitting their goals?

**Daniel Lopes:** Did you ask their goals?

**Daniel Lopes:** But there's like a lot of like post-processing on the ongoing meetings as well.

**Daniel Lopes:** And I'm just putting that out for now and just like not be part of the scope.

**Daniel Lopes:** that meeting area will grow.

**Ryan Singer:** Yeah.

**Daniel Lopes:** And it's so easy to it, you know?

**Ryan Singer:** Got it.

**Ryan Singer:** Yep.

**Daniel Lopes:** Anyway.

**Ryan Singer:** Yeah, so, okay.

**Daniel Lopes:** So this is the setup area.

**Daniel Lopes:** then the learning and improve, probably the resolution is actually.

**Daniel Lopes:** So when I send you the video, you're going to see 4Ks.

**Daniel Lopes:** going to be better.

**Daniel Lopes:** But we have- Looks fine here.

**Daniel Lopes:** And then backlog briefing.

**Daniel Lopes:** This is the status of the

**Daniel Lopes:** The work that is getting done, and we will show both new and optimization in here.

**Daniel Lopes:** We have, we also almost always want to see the pages clustered by the things you care about they're optimizing for.

**Daniel Lopes:** So I picked in the clustering here.

**Daniel Lopes:** We might also want to do, like, add some, like, the charts for some of the core metrics.

**Daniel Lopes:** Like, if you're focused on the impressions, maybe we'll show the chart in the cluster here or something like that.

**Ryan Singer:** Yeah, like a spark line.

**Ryan Singer:** Yeah.

**Daniel Lopes:** Yeah, I sparked mine exactly.

**Daniel Lopes:** We have the idea of helping you define the clusters.

**Daniel Lopes:** So that would be, you can combine things for the taxonomy or for some of the fixed fields that we have, like personas is a drop-down, for example.

**Daniel Lopes:** Or some other things.

**Daniel Lopes:** So you can combine them and create the clusters.

**Daniel Lopes:** And you also have the, I don't know if you saw this last time.

**Daniel Lopes:** I don't think I had this last time, actually.

**Daniel Lopes:** And then you have a smart view.

**Daniel Lopes:** smart views is essentially pretty...

**Daniel Lopes:** Define filters with SORP.

**Daniel Lopes:** And those are the things that you want people to think about.

**Daniel Lopes:** And then when you go in...

**Ryan Singer:** So surging in almost top three is a smart view, yeah?

**Daniel Lopes:** Yeah, exactly.

**Ryan Singer:** Yeah, cool.

**Daniel Lopes:** So you would click on that.

**Daniel Lopes:** So those are two smart view combined.

**Daniel Lopes:** So those are checkboxes.

**Daniel Lopes:** So you could check them and you have multiple things.

**Daniel Lopes:** Combining filters, basically.

**Daniel Lopes:** It might be too hard to do for this launch.

**Daniel Lopes:** So I think at least I can visualize the whole system now.

**Daniel Lopes:** And then we'll figure out what can be done in the next three weeks.

**Daniel Lopes:** And then we have the pages in here.

**Daniel Lopes:** some little bugs.

**Daniel Lopes:** need to get the guys to fix the line in here.

**Daniel Lopes:** But you can hover over and see things on the right here real quick.

**Daniel Lopes:** Or you can click and then switch to here and see.

**Daniel Lopes:** We're to have to clean up this.

**Daniel Lopes:** There's some things here that doesn't make sense anymore, but the quick actions.

**Daniel Lopes:** Some of the quick actions you want to have.

**Daniel Lopes:** have.

**Daniel Lopes:** Some

**Daniel Lopes:** There's like categorize, this is the taxonomy part, still makes sense, view on site still makes sense, but optimize it for here, I don't think it makes sense anymore, because there's more work to be done there.

**Daniel Lopes:** But when you go into the page, let's say I open one of these, then we have the same, I think we had this before as well, so we have like a lot of like analysis that will be done on top of your core metrics, so the whole thing will be like on those core metrics at the page level.

**Daniel Lopes:** And then there's some other things that come with mistakes that people do, like they don't have their open graph set up, for example, that's super important.

**Daniel Lopes:** So like we're surfacing it here, the keywords that this article will bring for, and the taxonomy here as well, so taxonomy will want to edit, and then everything in here, you're clickable, so you could just like look at those things when you're like drilling down one of the pages that you created or that you shipped recently, or they're decaying.

**Daniel Lopes:** So all of them were like doing like, you have like AI workflows for taking in the data and taking context and creating a quick analysis of things.

**Daniel Lopes:** So that's going to be throughout the system.

**Daniel Lopes:** And then content is just a quick way for you to see what the content looks like in markdown form.

**Daniel Lopes:** And activity would be the feed of the work that was done on this page.

**Daniel Lopes:** And then if we go into backlog, backlog is where, backlog and forward is where the work would get done.

**Daniel Lopes:** Same idea, so you can see the pages, same UI, closer the same way.

**Daniel Lopes:** With the sidebar here, because you have like the name of the work item.

**Daniel Lopes:** And then when you click on it, could be like here or here or here.

**Daniel Lopes:** You would go into the place where a first step would be empty like this.

**Daniel Lopes:** So you would see where the opportunity came from, where the idea of this content came.

**Ryan Singer:** Sorry, hold on.

**Ryan Singer:** I'm lost.

**Ryan Singer:** I'm lost with what we're looking at.

**Ryan Singer:** Can you go back?

**Ryan Singer:** What?

**Ryan Singer:** So here's a dumb question.

**Ryan Singer:** And maybe because it's sample data, X best Asana alternatives for small teams.

**Ryan Singer:** What is the work?

**Ryan Singer:** What's the task I'm supposed to perform here?

**Daniel Lopes:** I'm supposed to write the article or I'm supposed to change something or what is this?

**Daniel Lopes:** This is a new page.

**Daniel Lopes:** So this is an assignment for a new page or a work item for creating a new page that you accepted as you're going through the opportunities.

**Daniel Lopes:** So the opportunities, maybe I need to spell it out and say a new page or create a new page or create a new page.

**Ryan Singer:** Ah, that makes sense.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So this is essentially like a to-do item that is create this page.

**Daniel Lopes:** And the idea here is like the title is X best because you don't know how many should be in the article.

**Daniel Lopes:** So that's not the title of the article.

**Daniel Lopes:** That's just the name of the opportunity.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Okay.

**Daniel Lopes:** Create a list to go for this topic.

**Ryan Singer:** So this new page task doesn't live under new page opportunities.

**Daniel Lopes:** It lives under learn and improve?

**Daniel Lopes:** Because that you already accepted.

**Daniel Lopes:** So here would be where you would find all the opportunities.

**Daniel Lopes:** So you would have like, it sucks that I made it work yesterday.

**Daniel Lopes:** But on the normal setup with like simple data here, you would have a list of keywords or a list of ideas with their traffic, potential traffic, with their estimated traffic that you can get from it based on your size and some other things.

**Daniel Lopes:** And then when you accept and also suggestions, this should be a list to go or this should be a comparison article.

**Daniel Lopes:** This came from a competitor, for example, or this came from a trending topic.

**Daniel Lopes:** There's like a bunch of ideas here.

**Daniel Lopes:** And then you pick the ideas that you want to work on.

**Daniel Lopes:** And that would be like when you put an X.

**Daniel Lopes:** That would send the idea to the learn and improve area because now you're actually working on the page.

**Daniel Lopes:** Now it's like it's a real page.

**Daniel Lopes:** Like it's a draft page, but you accepted that this should be a page on your website.

**Daniel Lopes:** So like learn and improve, it's all about the pages and here's just ideas, you know, that might apply or might not apply.

**Daniel Lopes:** Maybe it's like learn and improve, find new page opportunities.

**Daniel Lopes:** And then create new pages or create content or something like something that's like, you just feel like the three jobs to be done that I, you know, it feels too buried a little bit.

**Ryan Singer:** It feels too buried.

**Ryan Singer:** It feels too buried.

**Ryan Singer:** And it also feels like, I don't understand why, like, just from, you know, like we, we, we bracket out what we know, we look at it fresh.

**Ryan Singer:** It's like,

**Ryan Singer:** The page that I need to write, it's very surprising that I can't find that under new page opportunities, just because I know it's a new page.

**Ryan Singer:** And then if there's an improvement, like an experiment from learn and improve, if there's something I found that I should be fixing on a page, and I found that in learn and improve, I would expect that improvement as opposed to like creation, like improve a page versus like make a page.

**Ryan Singer:** I would expect that improvement to also be like findable again from learn and improve, because that's kind of like where I sourced it.

**Ryan Singer:** And then, of course, like, yeah, but that's how I was thinking.

**Daniel Lopes:** So you would have here in page portfolio, you would see your existing pages and you'd see the ones that are creating.

**Daniel Lopes:** And you'd see the ones that you're optimizing as well, and they would all be in the back.

**Daniel Lopes:** Backlog as well.

**Daniel Lopes:** if you switch to Backlog, you would see Create or Improve.

**Daniel Lopes:** There would be different types of items in the Backlog.

**Daniel Lopes:** But the Backlog feels very, you know.

**Ryan Singer:** Yeah, so here's a first thought here.

**Ryan Singer:** I don't know if we need to jump to the whiteboard to draw it yet.

**Ryan Singer:** I can just say it for the moment, which is like, okay, very, very first thing is if improvements and new pages are mixed here, they should definitely be clearly labeled in terms of like, what work is this?

**Ryan Singer:** Because it's very different work, right?

**Daniel Lopes:** Yeah.

**Ryan Singer:** And I need to know like what work I'm reaching for, you know, and like what, so that's a key thing.

**Ryan Singer:** The other thing is I would definitely think here about basically having the exact same pipeline under both learn and improve and new page opportunities, but you're filtering by what you're looking at.

**Ryan Singer:** So if I go into new page opportunities.

**Ryan Singer:** I should basically have like a pipeline there, backlog, briefing, writing, review ready for all the new pages also, you know?

**Ryan Singer:** So you can think of this almost like there might be an objection of like, well, should my work be in two places?

**Ryan Singer:** But I think this is where floating up my work or assignments or whatever as a top-level place.

**Ryan Singer:** So like if I just want to see like work, I could go to just work, you know?

**Ryan Singer:** But if I want to see like what are the new pages that we're working on, then it would make, it's going to make more sense in new page opportunities to see like here's the opportunities and here's the opportunities that you've already sort of like planned.

**Ryan Singer:** Or said that you want to, you know, you've kind of prioritized that you want to do, right?

**Ryan Singer:** So you can think of these almost like, think of like learn and improve and new page opportunities almost like filters.

**Daniel Lopes:** Yeah, and I, like, the learn and improve is one mode that explore new opportunities, and you're just like, like, I was just on a one-hour call with our strategy spread team, you know, and it's just mostly like they're recording these 20-minute looms explaining the strategy and their strategy for new pages, which is like content clusters, how they're organizing the new opportunities, how they're, you know, the reading behind the clusters and how they're organizing opportunities, the thought process they went into in order to find those opportunities, like, that is, like, strategy, right?

**Daniel Lopes:** And then the creation is like a whole other game that is, like, very separate from those two modes.

**Daniel Lopes:** Yeah, like, the problem that I kind of said that I don't have the data here on an actual, maybe production you have, but opportunities, they have, there's a clear distinction between a bunch of ideas and, like, the things that I've

**Daniel Lopes:** The data structure is different, the work you do is different, so you're dealing with sometimes 2,000 things on your air table, for example.

**Daniel Lopes:** And you're cluttering them and you're dismissing them in bulk, you're accepting them in bulk, you're just like, the names or things are not super spelled out, it's more like X or Y, for example.

**Daniel Lopes:** Literally, like X products for a Sun alternative, that's literally like one opportunity idea, and has like a bunch of keywords attached to it.

**Daniel Lopes:** So like you're in a different mode of just triaging to a bunch of stuff, loading the things that in the system and triaging them again, and you do some analysis automatically, that will be like, is this the person or not?

**Daniel Lopes:** So automatically, the system will be like, filtering out the noise, and that already happens today, and then what we have working here, and then when you accept that, that goes into.

**Daniel Lopes:** It's almost like a different person does a job, you know, so maybe here it's just like opportunities or ideas or something like this, and then page is when, then page is like actually when you want to do the work, you know, because that challenge happens at the, even at the split of the system as well, you know, like, I feel like we're all seeing kind of like the same thing, except like the learn and improve all we're saying is like, that's what I struggle with too, it was like, if you mix in optimization and creation in the same views as just like a subtle drop down or filter or a label in the same view, they can, the experience can be effectively the same that you have here, but I think it has to be like separated.

**Daniel Lopes:** Yeah, we can have, that's what I'm saying, maybe we have, maybe the main view could be different, there's like new view for those things.

**Daniel Lopes:** But the process is essentially the same.

**Daniel Lopes:** like, this could be like moved out of here and create page, you know?

**Ryan Singer:** That's what I saying.

**Daniel Lopes:** like learn and improve, find new page opportunities, create new, you know?

**Daniel Lopes:** And then like create new or whatever.

**Ryan Singer:** Yes, yes.

**Ryan Singer:** Create as a sibling.

**Daniel Lopes:** Yeah, learn and improve.

**Ryan Singer:** You find opportunities like our new page opportunities and then create because the finding of the opportunities is a totally different mode.

**Ryan Singer:** It's a different, it's a different like different kind of work than the actual creation.

**Daniel Lopes:** Right, like different states as in like, I just have a  on the stuff, now I filter down, now I'm accepting them, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah, so let's say that, let's say that, let's say that creation, would that mean that creation actually doesn't.

**Ryan Singer:** Show up here inside of Learn and Improve at all, and we're only seeing optimization tasks.

**Ryan Singer:** That's kind of what I would assume that this, like, structure is telling me.

**Ryan Singer:** Like, as a user, like, if Learn and Improve is about experiments, I would expect everything here to be optimization work.

**Daniel Lopes:** Yeah, I think that could work.

**Daniel Lopes:** I think that would be true.

**Daniel Lopes:** Even the backlog breathing and writing, that might even be, like, one is, like, refreshing.

**Daniel Lopes:** Another one might be, like, optimization.

**Daniel Lopes:** Another one might be, like, I don't know, right?

**Ryan Singer:** Like, they're, I mean, just in states.

**Ryan Singer:** That's the other thing is these pipeline stages, they sound very creation-focused, and they kind of don't really track to optimizing.

**Daniel Lopes:** Yeah, that is a good point.

**Daniel Lopes:** Like, for instance, like, in the study that Katya did, right, like, citation is really important in referencing it, right?

**Daniel Lopes:** Like, so it's, like, and then, like, the structure of the pages or whatever, like, so it's almost, like, addressing some of these things.

**Daniel Lopes:** That's another thing that I hope, that's the main thing that I

**Daniel Lopes:** What wanted to talk today was just like, how does optimization look like?

**Daniel Lopes:** Because the creation I have here.

**Daniel Lopes:** So for example, let's just like finish the flow.

**Daniel Lopes:** But like, let's assume that this is, let's assume we'll pull this out and we have a create menu here.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** What all you've seen is like creation of new pages.

**Daniel Lopes:** When you go into creation mode, the flow is very specific.

**Daniel Lopes:** As in like, you have a brief, you generate an outline, the outline, you work on the outline quite a bit.

**Daniel Lopes:** And then you let the agent go to the research.

**Daniel Lopes:** And that might take a full hour.

**Daniel Lopes:** So like some of our agents will spend like a full hour just researching everything and putting the article together.

**Ryan Singer:** Yeah.

**Daniel Lopes:** And then you go into editing mode.

**Daniel Lopes:** And then, so like that I have, and I can show you real quick.

**Daniel Lopes:** The optimization is completely different.

**Daniel Lopes:** As in like, I finished this, but there's like specific tests on optimization.

**Daniel Lopes:** So like this is the creation process, for example.

**Daniel Lopes:** So let's say this is the, yes.

**Daniel Lopes:** The assignment that I'm taking is X, Vestas, and Alternatives for Small Teams, working for Lovable, creating a page for them.

**Daniel Lopes:** Let's say the idea, I can still see the idea where I came from, the search intent and all that.

**Daniel Lopes:** I don't need to do anything with this.

**Daniel Lopes:** The agent will do the work, just that for context.

**Daniel Lopes:** I can choose a content type.

**Daniel Lopes:** So it would be automatically selected because it's a listicle suggestion.

**Daniel Lopes:** This, like each one of these content types is a different agent.

**Daniel Lopes:** Like they perform different.

**Daniel Lopes:** To assemble the article in different ways and doing the research in different ways.

**Daniel Lopes:** But the user doesn't have to know that.

**Daniel Lopes:** And then you pick the personas.

**Daniel Lopes:** The search intent is here just if you want to change it.

**Daniel Lopes:** Because sometimes it might not be fully accurate how you see the space.

**Daniel Lopes:** You can give more directions.

**Daniel Lopes:** can say like actually start with a hook in a different way or close with a CPA in a certain way.

**Daniel Lopes:** But you don't have to.

**Daniel Lopes:** And you can also give like a range of that word count.

**Daniel Lopes:** And then when we hit that, it will generate.

**Daniel Lopes:** The outline, and the outline is usually in this format where you have the section and what should be under each section and how it should be written.

**Daniel Lopes:** And you can spell out as much as you want, or you can keep it short.

**Daniel Lopes:** And then we have a writing agent that will take this, do the research.

**Daniel Lopes:** Under each one of these outlines, there's also research questions that will be performed.

**Daniel Lopes:** That's just for reference for the folks who see what's going be researched.

**Daniel Lopes:** And then when you click generate, then this will go through the work.

**Daniel Lopes:** Once it's done, then you have an interface like this, where you have the meta, you have the article title now for real.

**Daniel Lopes:** You have the meta title that's sometimes different, sometimes you can have stuff like this.

**Daniel Lopes:** And then you have slug, meta description, and a cover image.

**Daniel Lopes:** And you can regenerate them if you didn't like.

**Daniel Lopes:** And if you want to annotate the article with the problems that you have, you're going to review.

**Daniel Lopes:** And then you can highlight the problems.

**Daniel Lopes:** And the problems are like the set of problems.

**Daniel Lopes:** And they have.

**Daniel Lopes:** And you can write a comment if you want, but even if you don't write a comment, we would be able to do a lot of that already.

**Daniel Lopes:** And then once you're done, then you finish the review, you can also like write high level.

**Daniel Lopes:** So that's kind of the first thing we talked like last month was the screen.

**Daniel Lopes:** And then when you finish this, then you would, then the agent, we have like an admin agent that you take your feedback and try to apply it.

**Daniel Lopes:** And then you would be in a freeform Notion experience.

**Daniel Lopes:** And this is just like a temporary text area, but it would be like a Notion document that you can freeform right from here and save.

**Daniel Lopes:** And once you're done, you're back into here and you can, if you don't have your CMS connected, you can just export.

**Daniel Lopes:** If you have connected, it would have a button to publish.

**Daniel Lopes:** So that is the process for creation.

**Daniel Lopes:** Optimization would be like completely different.

**Daniel Lopes:** So I hope that all made sense for for for for for for for

**Ryan Singer:** Okay, so what I think we need to do is step back for a moment and figure out what are we trying to solve today so that I want to make sure that we go into the thing that needs the most solving.

**Ryan Singer:** Because as soon as you showed me all of that, I wanted to like give you a whole bunch of reactions around that creation flow itself because it's another case where I'm seeing huge opportunities to make the UI actually like the workflow you described, I never saw.

**Ryan Singer:** Like I only saw like this like one slice, like now like I'm in review versus edit, but there was kind of this whole chain, you know, and it was like, you've got that in your head.

**Ryan Singer:** But like I'm not seeing it in the product, you know, which means that it's going to be hard for other people to learn and to hold in their heads like that this is how it works.

**Ryan Singer:** But what I don't want to do is just kind of jump into optimizing the UX flow for creation if that's kind of not the problem to solve right now.

**Ryan Singer:** If there's like the deeper problem is how to even handle, you know, optimization.

**Ryan Singer:** Because it sounds like with creation, at least you kind of understand the stages and maybe it's a smaller it's a it's a smaller improvement from from where you sit today to to present that more clearly.

**Ryan Singer:** But it's like, you know what it is and you understand it versus it sounds like maybe optimization is more of a like a like a like a blurry thing or like a or a hole today.

**Ryan Singer:** Is that right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I think so.

**Daniel Lopes:** I think the creation we can I think we can crack and we can at least get the scheme that we have in the time.

**Daniel Lopes:** Like the people that we will go into this workflow will be the folks that we train to set up like.

**Daniel Lopes:** 50 people at most.

**Daniel Lopes:** So it's very trainable, and we can continue to iterate on that.

**Daniel Lopes:** It's like I think I can get out of the hole.

**Daniel Lopes:** The optimization is the part that I'm like, okay, this is a different beast in the system and can go in many different ways.

**Daniel Lopes:** It's what am I optimizing?

**Daniel Lopes:** Is it optimizing chunks of text in the article?

**Daniel Lopes:** Is it optimizing many things at once?

**Daniel Lopes:** Is it like small to-dos, or is it like a giant thing that you do everything at once?

**Daniel Lopes:** Where does it live?

**Daniel Lopes:** So there's that, and then another part of the system that we deal with quite a bit is giving the clients, or even giving our own team, like, a place to share what's happening.

**Daniel Lopes:** So, like, here's a thing that we did, and so they're completely different topics.

**Ryan Singer:** So those are the two things.

**Daniel Lopes:** Two main areas of the system that today I'm like, huh, that can be a rabbit hole in itself.

**Daniel Lopes:** Optimize is a fast follow that we have to do, like, as soon as I ship this in March, Optimization has to stay.

**Daniel Lopes:** to

**Daniel Lopes:** Start like almost right after, like figure out how to do the optimization part.

**Daniel Lopes:** And another part is it's less pressing like this, but it's a thing that we need to figure out eventually.

**Daniel Lopes:** like, how do you keep the clients in the loop?

**Daniel Lopes:** And people are not good at that.

**Daniel Lopes:** So that's what the progress snapshots is for here.

**Ryan Singer:** Yes.

**Daniel Lopes:** And we have the same thing on Check That.

**Daniel Lopes:** So Check That, collect like a ton of data, but it's charts and data.

**Daniel Lopes:** So people to make sense of it, they need recipes, basically.

**Daniel Lopes:** Like look at here, look at here, analyze what happened, analyze what changed, create a report in your mind or send that to your boss or something like that.

**Daniel Lopes:** But you essentially need to be like doing status check on these products on the regular.

**Daniel Lopes:** And if we need to do that, might as well do most of the work and people just tweak it.

**Daniel Lopes:** So that's how we're thinking about the progress snapshots.

**Daniel Lopes:** So both tools will need a similar idea and the.

**Daniel Lopes:** But some of the knobs are the same as in like impressions or visibility or here's things that went up and the things that went down in this period.

**Ryan Singer:** Okay.

**Ryan Singer:** Daniel, can I check if I understand right?

**Ryan Singer:** So first of all, this pipeline that we're looking at inside of Learn and Improve actually doesn't belong here because we don't have a pipeline for optimization yet.

**Ryan Singer:** This is really just page creation right now.

**Ryan Singer:** Is that true?

**Ryan Singer:** Okay.

**Ryan Singer:** So let me just, I'm actually going to, let me take over for a moment and I want to start, I just want to start capturing some of these things so we don't only have words on the recordings.

**Ryan Singer:** Okay.

**Ryan Singer:** So first thing, what is wrong today?

**Ryan Singer:** Okay.

**Ryan Singer:** So like this doesn't belong here.

**Ryan Singer:** So like this doesn't

**Ryan Singer:** It to there's a new thing, which is something like create.

**Daniel Lopes:** Yeah.

**Ryan Singer:** Right?

**Ryan Singer:** And this stuff, actually, let me just do this a little bit better.

**Ryan Singer:** Let's just say, like, let's say all this stuff is going to move, it's going to move here, right?

**Ryan Singer:** And it doesn't live here.

**Ryan Singer:** So there's a question of, and this was just me noting what you were describing about creation, but this is more or less known.

**Ryan Singer:** So it's not the subject for right now, known enough for today.

**Ryan Singer:** But there's these questions around optimization and progress snapshots.

**Ryan Singer:** And if I understood what I just heard was, like, for optimization, we have to form opinions around, like, the little bit, like, what's the framework of what we optimize?

**Ryan Singer:** it's implies.

**Ryan Singer:** So, like, what are the things that we kind of, like, measure or track or kind of the types of optimizations?

**Ryan Singer:** And then if I understood right, you said the other side of that coin, which is, like, a different project, but it's linked, is what do we report on in progress snapshots?

**Ryan Singer:** Because, like, they're both kind of the same thing, right?

**Ryan Singer:** They're both, like, what do we consider to be change that is, like, improvement of some kind, right?

**Ryan Singer:** And so, like, learn and improve is kind of, like, how do I create an improvement?

**Ryan Singer:** And progress snapshots is, like, how do I tell about an improvement that happened?

**Ryan Singer:** Yeah?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** There's also, like, the progress snapshots today, like, if I just show you real quick, that's just, like, a rough mock-up that I spent essentially no time on it at all.

**Ryan Singer:** Yeah, let's see.

**Daniel Lopes:** Essentially, it's the...

**Daniel Lopes:** Mail that we should be sending our clients every week, which would be like, we have 10 ideas, 10 cluster ideas with 100 pages each.

**Daniel Lopes:** We made progress on 20 of those ideas on each one of those clusters.

**Daniel Lopes:** Some of them are starting to get impressions.

**Daniel Lopes:** 10% are getting impressions, for example.

**Daniel Lopes:** The other 90% is too soon.

**Daniel Lopes:** And we also worked on improving 100 of your existing pages by adding the right meta tags, adding the right OG tags, and that kind of stuff.

**Daniel Lopes:** And they're starting to get, maybe 10 of those pages are getting better impressions on Google search.

**Daniel Lopes:** So, like, that would be like, if you, if you present your meeting like this, and if you send an agenda ahead, like, this progress snapshot is essentially an agenda for what we should be sending ahead, or if a client just opts in and see it, they would be able to see.

**Daniel Lopes:** Here's the progress we made.

**Daniel Lopes:** Here's the thing that we're still working on.

**Daniel Lopes:** Here's the progress on the data that we're seeing.

**Daniel Lopes:** Here's the experiments we're running.

**Daniel Lopes:** And here's the metrics.

**Ryan Singer:** Here's one thing I would call out.

**Ryan Singer:** A brief can have a really different meaning based on, is this a brief for me in order to make decisions?

**Ryan Singer:** Or is this a brief for me to, to know that you're doing your job?

**Daniel Lopes:** Right.

**Ryan Singer:** So like, like the presidential brief is like, this is what's going on in all these different countries.

**Ryan Singer:** So that, so that, so that as an executive, know, there's, there's actions that have to be taken.

**Ryan Singer:** And what I, what I actually see when I look at this right now, as a first blast, as a first, as a first pass, when I see, especially on the top, which is, um, uh,

**Ryan Singer:** Weekly content intelligence brief.

**Ryan Singer:** If I'm supposed to make a decision about content, then I want an intelligence brief about what's been happening.

**Ryan Singer:** If I'm not here to make a decision, but I am here to see that you're doing what I paid you for, or I don't need to intervene because you're doing what I expected.

**Daniel Lopes:** Yeah, yeah, yeah, yeah.

**Ryan Singer:** Then that would be a very, very different angle.

**Ryan Singer:** That would be more like, it should be more like status report in the sense of like, a status report is like where you report up of like, this is what I did.

**Ryan Singer:** You know what I mean?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I think like, if we're just focused on the content OS and how we operate it today, I think we would need both.

**Daniel Lopes:** I think we need a, like a, a brief for decision-making at least every like.

**Daniel Lopes:** Like, we published five pages for you.

**Ryan Singer:** Like, seriously?

**Ryan Singer:** Like, what the hell are you doing?

**Daniel Lopes:** Like, just like, but Lava was decent.

**Daniel Lopes:** Like, if you look at, um, this, Remkus, um, or, yeah, yeah.

**Daniel Lopes:** So, it's like, they send this, this, their status update, right?

**Ryan Singer:** Oh, yeah, yeah.

**Daniel Lopes:** Gosh, dear God, like, seriously, we're just cracking content and that's it, like.

**Daniel Lopes:** Or this is just, this is like commodity, commodity work.

**Daniel Lopes:** Commodity, exactly.

**Ryan Singer:** Yeah.

**Daniel Lopes:** look at it and they go, cool, you did seven.

**Daniel Lopes:** That's worth $700 to me.

**Daniel Lopes:** It's $100 per.

**Daniel Lopes:** Like, you know what mean?

**Daniel Lopes:** That's your value to me.

**Daniel Lopes:** It's $700 this week.

**Ryan Singer:** Yeah, I'm paying you $18,000 a month.

**Ryan Singer:** Like, what the hell am I doing?

**Daniel Lopes:** Exactly.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And instead, it should feel like, holy crap, you legit have an army of  agents going through and doing all this stuff and you're connecting the dots for me.

**Daniel Lopes:** And you're going through and, like, showing, like, where, like, we're heading.

**Daniel Lopes:** And how things are improving, essentially, like, I would be asked without you.

**Daniel Lopes:** And in the 7 that you took us out of exploring 10,000 ideas, and validated through all the six personas, and think the one that made most sense for our product.

**Daniel Lopes:** And it's with the framework of, like, we've been building these kind of, like, context files and things like that, and when we run all our transcripts and all our data through one of those, like, what comes out is, like, so much better than this , right?

**Daniel Lopes:** And then we're like, okay, why are we letting humans do this at this point?

**Daniel Lopes:** Like, this is stupid.

**Ryan Singer:** Totally.

**Daniel Lopes:** And it's like the, going back to our mental model of, like, where the work is outputs, but the outputs are to deliver outcomes, and there's leading and lagging outcomes, and we need to connect the dots between the context of the company and their goals, to the work we prioritize, to the this validate, to the outputs we deliver, outputs deliver, to...

**Daniel Lopes:** Did we learn, or is this having the impact on the outcomes that we said it was going to be yes or no, and what are we doing about it, right?

**Daniel Lopes:** So snapshots is like a gnarly thing that as long as it's better than what you just saw, it's a win.

**Daniel Lopes:** And then improvement, the way I think about improvement is like finding failure modes in the existing pages and addressing those failure modes so that you address it once.

**Daniel Lopes:** But later on, you turn it into a systematic approach to like addressing that.

**Daniel Lopes:** For instance, right, like when we, like, I was just reviewing actually a new customer, Blaxel, yeah, B-L-A-S-E-L, and one of the first pieces of content we published for them is like a listicle on alternatives to daylight.io or some , one of their competitors, right?

**Daniel Lopes:** Like there's like an agentic framework platform or whatever.

**Daniel Lopes:** Like

**Daniel Lopes:** And in, like, the first sentence, like, we praise them, we link to their site, and we link to a press release.

**Daniel Lopes:** And it's like, dude, this is supposed to be, like, a  thing about alternatives to this thing.

**Daniel Lopes:** Why are you praising them in the first sentence, you know, and linking to two of their sources and sending them, like, equity?

**Daniel Lopes:** Like, that's a very clear line, you know?

**Daniel Lopes:** Like, you know, and the intro was pretty garbage, right?

**Ryan Singer:** So this is an example of an optimization.

**Daniel Lopes:** Exactly, yeah.

**Ryan Singer:** Yeah, yeah, yeah, good, okay.

**Ryan Singer:** So, okay, so what I just heard was there's a million things that we could do around snapshots, but as long as the snapshot is not what we just saw in Slack, it's kind of doing the job for now, and therefore we should focus over on optimization for today, yeah?

**Daniel Lopes:** Yeah, yeah, Snapshots will be great for you.

**Daniel Lopes:** Yeah, okay.

**Daniel Lopes:** It's a little bar.

**Daniel Lopes:** Yeah, okay, all right.

**Daniel Lopes:** But the, and, yeah, and so I...

**Daniel Lopes:** I can't...

**Daniel Lopes:** can share whatever context you think would be helpful on the optimization.

**Ryan Singer:** What I want to maybe suggest that we start with here is since we have kind of a blank sheet that we're starting from, you know, whenever I have a blank sheet, I want to start with use cases or example cases.

**Ryan Singer:** So can we just collect, like, what are the types of optimizations that should be happening via Learn and Improve, you know?

**Ryan Singer:** And, like, what we want is, like, multiple concrete examples that are different.

**Daniel Lopes:** Yeah, so maybe a mental model here is, like, there's no good to have sentries set up on error logging and then look at, like, a freaking, like, 50,000 things, right, that are alerts, right?

**Daniel Lopes:** Like, what we're trying to do instead is, like, group them in the right altitude.

**Daniel Lopes:** You know, that makes it, like, actionable enough, but not too down in the weeds that just becomes, like, you're, you know, out of context, right?

**Daniel Lopes:** Like, so the grouping and the altitude of the grouping is really critical.

**Daniel Lopes:** The way, like, the way I kind of think about it is potentially, like, fixing issues versus, like, improving content versus, like, refreshing the content.

**Daniel Lopes:** And then the question mark for me is, like, completely refactoring, aka, like, creating new and replacing, you know, which is, like, more of the creation one, which is, like, this is so garbage, this is so bad, but don't get rid of the surface area because there's already, like, equity in this URL.

**Daniel Lopes:** And, like, the URL, like, can be repurposed.

**Daniel Lopes:** And then the last would be, like, prune, delete, archive, redirect, kind of, like, you know, essentially, like, pruning.

**Ryan Singer:** Yeah.

**Ryan Singer:** Mm-hmm.

**Ryan Singer:** Mm-hmm.

**Ryan Singer:** So what I want to do is...

**Daniel Lopes:** issues, improve, refresh, refactor, think you've missed fix issues.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Fix, improve.

**Ryan Singer:** Improve is different than refresh?

**Daniel Lopes:** Yes.

**Daniel Lopes:** So, like, improve, it is, like, around, like, the intro just, it is just bad or something like that.

**Daniel Lopes:** Whereas, like, refresh, again, we can discuss to make sure, see if, like, we want to consolidate, but, like, refresh is truly, like, this thing has not been touched for six months, and it's going to decay if you don't touch it.

**Daniel Lopes:** You need to, like, refresh, like, new stats, like, you know, add a couple of things.

**Daniel Lopes:** It's just truly just to say, because these engines look at less modified or, like, dates quite a bit, and so it's, like, just adding a couple of new stats or a couple of new things is just, like, really, really important.

**Daniel Lopes:** Keep it fresh, essentially, you know?

**Ryan Singer:** Yeah, uh-huh, mm-hmm, mm-hmm.

**Daniel Lopes:** What about the issues?

**Daniel Lopes:** Can you talk more about the kinds of issues?

**Daniel Lopes:** Yeah, like the issues ideally are us finding like the patterns that are significant in both SEO, AO, as well as like engagement, right?

**Daniel Lopes:** And so it just could be like broken links.

**Daniel Lopes:** could be like factual inaccuracies.

**Daniel Lopes:** It could be, you know, like H, too many H1s and H2s or like just like the structure of it, right?

**Daniel Lopes:** Technical issues as well, right?

**Daniel Lopes:** Like load-to-load images.

**Daniel Lopes:** Yes, um, but I think those are going to have to be systematic.

**Daniel Lopes:** Systematic.

**Daniel Lopes:** It's like, it's very rare that like, it could be like broken image.

**Daniel Lopes:** Broken image can be a page, like, uh, issue.

**Daniel Lopes:** Right.

**Daniel Lopes:** Whereas

**Daniel Lopes:** That's like, you know, yeah, like issues could be like AI slop, right?

**Daniel Lopes:** It could be like all the things that were like labeling.

**Ryan Singer:** It's got to be vertical to the page, not horizontal to the platform.

**Daniel Lopes:** Yeah, like, yeah, factual inaccuracy, it could be like outdated product mentions, right?

**Daniel Lopes:** Like, no CTA, lack of CTA, bad CTA, you know.

**Ryan Singer:** So how are these different than improvements?

**Daniel Lopes:** Improvements could be like add an FAQ section at the bottom, you know.

**Daniel Lopes:** But where it's like, think of it as like in a publishing pipeline, the fixed issues would block you from publishing.

**Daniel Lopes:** And the improvements would be publish and then add and make it better.

**Daniel Lopes:** Never thought of one.

**Daniel Lopes:** That's it.

**Daniel Lopes:** Like.

**Daniel Lopes:** Like, if you're introducing a critical bug, you shouldn't ship it, right?

**Daniel Lopes:** But if you're not, you can ship it and then make it better.

**Daniel Lopes:** Like, so that you learn from it.

**Ryan Singer:** Don't stop yourself from learning, you know?

**Ryan Singer:** Okay, I see.

**Ryan Singer:** So the intro might be bad, but if the links and the images aren't broken, the structure is correct, and it's not factually inaccurate, then it doesn't block us.

**Ryan Singer:** Like, this is literally, like, these are things where, like, you should not be live with any of these things happening.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** That's a good way to think about it.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, those are, like, P1s.

**Daniel Lopes:** Yeah, P1s.

**Daniel Lopes:** P0s to P1s, depending on it, you know?

**Daniel Lopes:** Or, like, let's say it's missing, like, an open graph image, or the meta description is a duplicate meta description, or missing completely the, you know, the meta title is wrong.

**Daniel Lopes:** Or missing, or something.

**Ryan Singer:** Mm-hmm, mm Something like that.

**Daniel Lopes:** Like with Clerc, for example, they're like, don't use login, use sign in or some  like that.

**Daniel Lopes:** know, it's like, that's a hard rule.

**Daniel Lopes:** know, think of it as like cursor rules, like plot rules, right?

**Daniel Lopes:** Like, or like agent rules, where it's just like, do this every time, right?

**Daniel Lopes:** Versus like a skill.

**Daniel Lopes:** So, so like, this is more like hard rules that shouldn't be broken, but that, that can have a reference doc that has a running list of these rules, you know, and for each page.

**Daniel Lopes:** And, and some of these are rules and some of these are, are like optimization patterns that are generalized that are important, right?

**Daniel Lopes:** Like you should attribute, if you mention a stat and you don't attribute who that stat is from or how you found that stat, like that stat, like, you know, that, that's like a very, like, established thing.

**Daniel Lopes:** You can turn it off and you can overwrite it, but, but these are like the rules, right?

**Daniel Lopes:** Like don't let traffic through, you know?

**Ryan Singer:** So is this, this is like a domain space?

**Ryan Singer:** Is example that like for one client, this might be true, but not necessarily for everybody or?

**Daniel Lopes:** That was like a pattern for like how AI engines work.

**Ryan Singer:** Okay.

**Daniel Lopes:** Like how they're fetching information.

**Daniel Lopes:** A lot of them are very, very biased towards like rotation, source attribution, quality of the sources that you're attributing an information to.

**Daniel Lopes:** You know, essentially you did your homework and you organized information and you're not like, this is not a slot.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So we've got hard rules that can't be broken.

**Ryan Singer:** We've got, I think this we understand.

**Ryan Singer:** We could say what this is and what it's not, right?

**Ryan Singer:** That there's a, there's a kind of a black and white test that is confident enough that you could actually block publishing on it.

**Ryan Singer:** Is that right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** think so.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Because there are levels of severity.

**Daniel Lopes:** And some of the stuff we need humans to check.

**Daniel Lopes:** It can.

**Daniel Lopes:** And the way I kind of think about it is like it.

**Daniel Lopes:** It.

**Daniel Lopes:** If it's something that is optional, maybe it should go into improvement and it should move out of our rules, like standards, you know, and the standards can have like a strict mode and a flexible mode or something for that site or for that content type or that page type, you know, maybe, I don't know.

**Daniel Lopes:** That way, it's kind of like network rules, right?

**Daniel Lopes:** like, it's sometimes like you might need to like monitor and sometimes you might need to be okay with like some things like letting it pass, but then you need to establish globally that you're going to let that traffic pass forever.

**Daniel Lopes:** Yeah, yeah, yeah.

**Ryan Singer:** That's crazy.

**Ryan Singer:** I didn't know that TL Draw had Markdown, actually.

**Daniel Lopes:** What?

**Ryan Singer:** That's crazy.

**Ryan Singer:** crazy.

**Ryan Singer:** Okay.

**Ryan Singer:** Refresh, I understand.

**Ryan Singer:** I think refresh is like this in the sense that it's very, very clear what it means.

**Ryan Singer:** It basically means, like, you're fixing a staleness problem, right?

**Daniel Lopes:** Yes.

**Daniel Lopes:** Yeah, has not been touched in more than, and then you define a parameter for how ideally, like, you know, think of it as like past due, you know, like recently past due, just like, okay, they didn't release the payment, like, you know, the 30 days past due is like, yo, what's going on?

**Daniel Lopes:** And then, like, mangate past due is like, what the , like, you know, like, them the, it's like the, where's my money, you know?

**Ryan Singer:** Where's my money?

**Daniel Lopes:** Like, from, like, Stewie and, yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So now, let me take these, these, these, think, are a good start, I mean, all this is good, but I mean, these ones are like, like, solid.

**Ryan Singer:** In the sense that we understand.

**Ryan Singer:** This feels fuzzier.

**Ryan Singer:** I would love if we could be more clear about this.

**Daniel Lopes:** Can we just collect a couple more examples?

**Daniel Lopes:** Let's left out one for last because I think it might make it a little bit easier.

**Daniel Lopes:** It might shake out.

**Daniel Lopes:** If it doesn't fit in anywhere else, it won't fit there.

**Daniel Lopes:** Replacing is usually just shallow content, but the opportunity behind it was, like, decent, you know?

**Daniel Lopes:** So, for instance, like, there is, like, sometimes in some of these sites, it's, like, legacy content.

**Daniel Lopes:** It hasn't been touched for, like, three, four years.

**Daniel Lopes:** It is literally, like, two paragraphs.

**Daniel Lopes:** And it's like, what the  is this?

**Daniel Lopes:** But the URL slug was actually pretty good.

**Daniel Lopes:** And it has, like, a ton of links to it, you know?

**Daniel Lopes:** That is the case for Vercel, for example, for their AI gateway.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Literally, like, two words.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It depends, though.

**Daniel Lopes:** It depends.

**Daniel Lopes:** And so it's kind of like the page should exist.

**Daniel Lopes:** A page like this should exist.

**Ryan Singer:** This is clearly not it.

**Ryan Singer:** Yeah, uh-huh.

**Daniel Lopes:** This is like so many miles away that there's nothing, no substance in this page that should be repurposed.

**Daniel Lopes:** It's just like hit reset.

**Ryan Singer:** Right, yeah, okay, uh-huh.

**Ryan Singer:** How do you...

**Daniel Lopes:** It's truly a refactor, a like, you know, rip and replace.

**Daniel Lopes:** But rip and replace in the same room, not like...

**Daniel Lopes:** Exactly.

**Ryan Singer:** Yeah, yeah.

**Daniel Lopes:** The URL is the most important thing to have.

**Daniel Lopes:** Like, because you don't need to set up like redrafts.

**Daniel Lopes:** You don't need to like, you know, it's just easier to do that.

**Daniel Lopes:** And the likelihood of that URL doing well because it's already established URL that has already like...

**Daniel Lopes:** Also, there's like, you know, cross-linking within your site and...

**Daniel Lopes:** Backlinking to that URL potentially, whereas if the URL slug sucks, there's no links from within your site and no links externally, then it's most likely a delete and archive kind of situation, right?

**Daniel Lopes:** Because it's just like, okay, yeah, maybe the ADA here was good, but it's like this is a  URL slug and there's no equity in this URL, you know?

**Daniel Lopes:** And then it's like a...

**Daniel Lopes:** So you're talking about the delete and archive, right?

**Daniel Lopes:** Yeah, then it's like a prune and redirect, you know?-huh, got it, got it.

**Ryan Singer:** Okay, let me just capture that.

**Ryan Singer:** I was honestly spinning on replace URL.

**Ryan Singer:** So this is like, it's not well-linked.

**Ryan Singer:** There isn't a...

**Ryan Singer:** Yeah, it's not well-linked internally or externally.

**Daniel Lopes:** It has no sign of life, like no sign of the , you know?

**Ryan Singer:** Yeah.

**Daniel Lopes:** and, and then the...

**Daniel Lopes:** The substance of it, there's no value to the substance of it, yeah.

**Daniel Lopes:** You can tap into traffic and impressions as well, right?

**Daniel Lopes:** Yeah, it's usually like, if you have a site that has, there's been a lot of studies on this, right?

**Daniel Lopes:** And so think of it as crawl budgets for SEO, but for agents it's the same thing.

**Daniel Lopes:** And so you have limited crawl budget that tends to be directly proportional to your site's authority and how it's perceived or your brand's authority in some cases.

**Daniel Lopes:** And so the more you spread, the less signal you're going to get.

**Daniel Lopes:** And so you're a lot better if you have, let's say, 10,000 pages that you just know it's  good, but you have no signals, right?

**Daniel Lopes:** You're better off picking the 100 that are the most no-brainer for Google to be like, well, there's nothing else in the world about this, and yours is really good.

**Daniel Lopes:** And then you have this really high-quality signal, and then it learns.

**Daniel Lopes:** It's when that signals go, whoa, this is good.

**Ryan Singer:** Give me more, give me more, give me more of this.

**Daniel Lopes:** And you give it a little bit more and a little bit more and a little bit more, a little bit more until there's diminishing returns and you work your way through it.

**Daniel Lopes:** Whereas if you just say, here's 10,000, it won't even know how to prioritize it.

**Ryan Singer:** So then it's just going to randomly prioritize it and ingest a lot of bad signals potentially, right?

**Daniel Lopes:** Because it's not going to send you the CRM traffic.

**Daniel Lopes:** It's going to send you the  traffic to those businesses.

**Daniel Lopes:** And then it gets like a bounce or something.

**Daniel Lopes:** It's going, yeah, this site sucks, you know?

**Daniel Lopes:** And so you're better off like pruning aggressively anything that's like at the bottom, right?

**Daniel Lopes:** And then the only cases where that's not it is that if it historically had traffic and it went down to zero or like there's a ton of backlinking or a ton of linking internally.

**Daniel Lopes:** Right.

**Daniel Lopes:** In which case you don't want a bunch of horrible force, you know?

**Ryan Singer:** Yeah, that's part of this.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Daniel Lopes:** Sorry, that was a long explanation of.

**Ryan Singer:** No, that's, that's, that's good.

**Ryan Singer:** How.

**Ryan Singer:** Let's leave them proved to the side for the moment.

**Daniel Lopes:** We should post-process this meeting as a blog post of how crawling and Google search engine works.

**Ryan Singer:** This is literally how we see it happening on all clients.

**Daniel Lopes:** The replace URL should have been the, yeah, like replace.

**Daniel Lopes:** Replace and keep the URL.

**Daniel Lopes:** Replace and keep the URL.

**Daniel Lopes:** Yeah, it's like refactor.

**Ryan Singer:** So these have what I can picture, I can picture the tests that surface these.

**Ryan Singer:** This one also, we have a clear test we could for how to surface it.

**Ryan Singer:** How do you surface this?

**Daniel Lopes:** So this is, once upon a time, this was good.

**Daniel Lopes:** It's clearly been dead for a while, right?

**Daniel Lopes:** Wow.

**Daniel Lopes:** know, and the only way to revive it is to, like, create a clone and, you know, start from scratch here.

**Daniel Lopes:** But because this once upon a time was good and had some sign of life and, or some sign of value, then we might as well keep the URL because it makes our lives a little bit easier, you know?

**Ryan Singer:** Okay.

**Ryan Singer:** So how is this literally?

**Daniel Lopes:** This is truly, like, shallow content, you know?

**Daniel Lopes:** Like, what the F is this?

**Daniel Lopes:** Like, lower count, like, just, just, like, clearly nowhere near, like, the quality bar that we have for the rest of the site.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay, so if we were to, like, metricify this, it was good once, it's been bad for a while, that's a traffic thing over time?

**Daniel Lopes:** Let me give you a quick example.

**Daniel Lopes:** This is a page for Vercel, AI models, for example.

**Daniel Lopes:** And it's a great, this page should definitely be there, has the right URL, has not even one paragraph of text, and everything else is completely irrelevant to a search engine.

**Daniel Lopes:** We're in contact with them to essentially, like, enrich these pages.

**Ryan Singer:** Yep.

**Daniel Lopes:** So that is an example of one.

**Ryan Singer:** Okay, so that's it.

**Daniel Lopes:** So the rip and replace is, first of all.

**Ryan Singer:** Did you say rip and replace?

**Daniel Lopes:** Yeah.

**Ryan Singer:** That's a good one.

**Daniel Lopes:** It's like, no traffic is usually, like, a good indicator.

**Daniel Lopes:** from high

**Daniel Lopes:** First of all, no current traffic, but in the last 12 months, at some point, there was traffic.

**Ryan Singer:** Uh-huh, uh-huh.

**Daniel Lopes:** Some URLs, or some links, internal links, and backlinks, not zero, you know?

**Ryan Singer:** Yeah, uh-huh.

**Daniel Lopes:** And then ideally is doing some work on understanding the intent of this page to see if it's like an opportunity we would have, like, does this match, like, an opportunity that we would have surfaced as new if this URL didn't exist, you know?

**Daniel Lopes:** Aka, like, don't cannibalize, like, and so this is more of, like, in the example of, like, the Marcel one, it would be, like, Opus 4.5, the intent is you're looking for the stats on the model, like, the details of it, you're looking for evals on it, you're, like, trying to understand blah, blah, blah, like, that's a legit intent.

**Daniel Lopes:** That's, like, a legit opportunity.

**Daniel Lopes:** That

**Daniel Lopes:** should belong here in this page, right?

**Daniel Lopes:** But this page is not doing that.

**Daniel Lopes:** So that one's a little bit more fuzzy, whereas the delete one is no current traffic, like low to no linking, internal or external, and there was never any sign of life or there hasn't been a sign of life for more than a year or something, you know?

**Daniel Lopes:** And getting this thing was never valuable at all.

**Ryan Singer:** Mm-hmm.

**Ryan Singer:** Yep.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** What is, is there an example of intent match that you can actually do with the systems you have already, with the knowledge you have?

**Daniel Lopes:** Like, how would you do that?

**Daniel Lopes:** just looking at the URL and then looking at what is actually on the page, even if it's very, very, very little, tends to be like, okay, like, you can kind of understand and then you can reverse engineer what searches related to this would be and then look what, at those pages that are like.

**Daniel Lopes:** There are actually ranking for what that would be, and it becomes really like a finite game of what that intent would have been, right?

**Daniel Lopes:** Like, so the URL slug tends to tell you a lot, and if the URL slug is garbage, then most likely it's in the category of delete anyways, you know?

**Daniel Lopes:** Like, it's like a one-word slug, you know?

**Ryan Singer:** Uh-huh, uh-huh, uh-huh, okay.

**Ryan Singer:** So could I say some intent match from URL slug?

**Daniel Lopes:** Yeah.

**Ryan Singer:** Um, and this is something that you would do, you can do, um, uh, with, with the AI as opposed to with a human?

**Daniel Lopes:** You could, yeah.

**Daniel Lopes:** I think, actually, like, the more I'm thinking about this, I think we can put those two together, rip and replace, or archive, and it's mostly, like, the action you determine based on a human judgment.

**Ryan Singer:** I think, yeah, but here's the thing, is I think that if we come back to when we were looking at this, Yeah.

**Ryan Singer:** The, the number one question I'm

**Ryan Singer:** I had in my mind when I was playing user was, what am I supposed to do?

**Ryan Singer:** So I think that action is actually kind of maybe the leading thing when it comes to identifying what these things are.

**Ryan Singer:** Do you know what I mean?

**Daniel Lopes:** Yeah, it's like fix, improve, refresh.

**Ryan Singer:** Right.

**Daniel Lopes:** And then this one is like replace or archive.

**Ryan Singer:** And so fix, refresh, refresh is a little, okay, we'll come back to that.

**Ryan Singer:** Replace.

**Daniel Lopes:** And I was saying replace it or archive because it's just kind of, it's like in the same mode.

**Ryan Singer:** It's just like.

**Daniel Lopes:** Yeah, but it's such a different.

**Ryan Singer:** But it's totally different work, isn't it?

**Daniel Lopes:** little human things.

**Ryan Singer:** You can look at something very quickly and get no-brainer, whereas I think this is one of those where human judgment is still way easier than decide which one of the two buckets to put something under.

**Ryan Singer:** No, I get it.

**Ryan Singer:** I get it.

**Ryan Singer:** I get it.

**Ryan Singer:** So there's actually a different work step of decide versus...

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, exactly.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** It's like this is the cue of like garbage can and you decide if like you want to recycle or if you want to just like dump it, you know?

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** So this is different work than Just call it like recycle or dump.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** We should have some fun.

**Ryan Singer:** Yeah, totally.

**Ryan Singer:** Okay.

**Daniel Lopes:** And when you archive, we need to also decide if it's going to be redirect or just...

**Daniel Lopes:** It almost always should be...

**Daniel Lopes:** You know, a wildcard redirect to something, you know, because it's just like a good practice to have it.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Let's take – And then improve is the only one missing.

**Ryan Singer:** Uh-huh.

**Daniel Lopes:** Oh, yeah.

**Ryan Singer:** Let's take it – let's leave improve still, and let's take another spin through the exact same material with this other question.

**Ryan Singer:** What's wrong?

**Ryan Singer:** Okay.

**Ryan Singer:** So this is from the action lens.

**Ryan Singer:** Let's look at it from the failure lens, you know?

**Daniel Lopes:** Yeah.

**Ryan Singer:** So, like, this was like a rule was broken?

**Daniel Lopes:** Yeah, important rule was broken, yeah.

**Ryan Singer:** This is stale, expired?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Ryan Singer:** This is – – It's

**Daniel Lopes:** Decaying, losing engagement, not effective.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** This is, like, garbage.

**Daniel Lopes:** Well, no, not get garbage.

**Ryan Singer:** This is garbage.

**Daniel Lopes:** I mean, it's garbage.

**Daniel Lopes:** It's just, do you want to recycle or not?

**Ryan Singer:** Ah, okay.

**Daniel Lopes:** It's garbage no matter what.

**Daniel Lopes:** It's just a matter of, like, you want to reuse the material.

**Ryan Singer:** Yeah, but here's the thing.

**Ryan Singer:** Like, isn't there a sense when you find this that it's a little bit like you found, like, gold?

**Ryan Singer:** Do you know what I mean?

**Daniel Lopes:** Like, it's garbage, but, like, there's opportunity here because of the fact that it's, like...

**Daniel Lopes:** Yeah, I love it.

**Daniel Lopes:** It's kind of like that.

**Daniel Lopes:** The Vercel one is kind of like that.

**Ryan Singer:** I mean, the Vercel one you showed me felt like...

**Daniel Lopes:** It's just the Vercel...

**Daniel Lopes:** That one is almost like the exception.

**Daniel Lopes:** What you end up with here is like some founder, early stage, created some blog at the beginning that had the right title and the bad execution.

**Daniel Lopes:** Home-based or just like single paragraph product announcements, but the title was like an intent that was like, you know, very, very good.

**Daniel Lopes:** Like, it's like, what is blah, blah, but it was about a product announcement.

**Daniel Lopes:** It was like, what the hell, this doesn't match, right?

**Daniel Lopes:** Like, it's actually like pretty rare that you're going to see.

**Daniel Lopes:** It's more rare that you're going to find things like that or like the Marcel one, which is like an entire area of the site is the right area.

**Daniel Lopes:** It's just the execution of the content is, you know, to be improved.

**Daniel Lopes:** But then that's, you know, that's different, you know.

**Ryan Singer:** Okay.

**Daniel Lopes:** Yeah, this is more of like candidate for garbage, you know, and what's wrong is just like, this is bad, you know.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It's

**Daniel Lopes:** Like, best case, bad, worst case, toxic, you know?

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** So this is like...

**Daniel Lopes:** That is maybe even the wrong word, like, useless.

**Daniel Lopes:** Let's just, like, call it useless, you know?

**Daniel Lopes:** Which is very different.

**Daniel Lopes:** It's like, yeah, like, legit.

**Daniel Lopes:** Like, no, like, instead of bad, useless, and then toxic.

**Daniel Lopes:** Like, where, like, toxic could be, like, this is a virus, you know?

**Ryan Singer:** Okay.

**Ryan Singer:** So what's right?

**Daniel Lopes:** Um, in what sense?

**Ryan Singer:** For each one of these.

**Ryan Singer:** If I'm fixing it, something's right with it, right?

**Ryan Singer:** Otherwise, because I'm not throwing it away.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Got it.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** the, like, proof, there's traffic and engagement, and, um, or there's visibility to it.

**Daniel Lopes:** There's impressions.

**Daniel Lopes:** And, um, the, the opportunity, yeah, there's potential, like, yeah, there's potential, yeah, like, there's, like, unrealized potential, yeah, what do you call, if there's, like, fulfilled potential, then there's nothing you should do, right, like, unrealized potential is, like, hey, we think this could be realized even in a measurable way, right, mean, for example, like, when you're picking a topic in the opportunities area today, it's coming from your search of keywords, they are getting search void, so that's, is that what potential means?

**Daniel Lopes:** Yes, yeah, yeah, so if you watch the article somehow, like, maybe the meta type is wrong, the content is wrong, it's not indexed, then there's potential with zero, uh, yeah, like, there's potential for better quality content, there's potential for more impression and visibility, more citations, there's potential for more traffic, there's potential more content.

**Daniel Lopes:** There's for deeper engagement, and there's potential for higher conversion, yeah.

**Daniel Lopes:** The level of realization depends, yeah.

**Ryan Singer:** Uh-huh, okay.

**Ryan Singer:** Would it be meaningful?

**Ryan Singer:** That felt important, but I'm not sure if we're getting on a sidetrack.

**Daniel Lopes:** Would it be meaningful to capture those different types of potential?

**Daniel Lopes:** Yeah, because they align to our scores, essentially, that are on the page, right?

**Daniel Lopes:** Like, they're all aligned to it, you know?

**Daniel Lopes:** So what are the types of potential?

**Ryan Singer:** Is again?

**Daniel Lopes:** Just give those to me one more time.

**Daniel Lopes:** There's potential for quality.

**Daniel Lopes:** There's, again, there's potential to improve the quality of the page.

**Daniel Lopes:** There's potential for impressions, and there's potential for more traffic, and there's potential for engagement, and there's a potential for conversions.

**Ryan Singer:** Or actions, too.

**Ryan Singer:** So, can you give me a quick, a quick, um,

**Ryan Singer:** Lesson, what's the difference between impressions and traffic?

**Daniel Lopes:** Yeah, like impressions, for example, are like when you search something on Google and a page is like the last one on the page and people don't scroll down, that's still an impression, right?

**Ryan Singer:** Oh, got it, yep, okay, yep.

**Daniel Lopes:** And so like we know that there's people searching for a certain keyword, but you're not even showing up because you're like on the fifth page, right?

**Daniel Lopes:** If you were on the first page, you would get a ton of impressions, right?

**Daniel Lopes:** Whereas like traffic is about like the impressions give you a shot at traffic.

**Daniel Lopes:** Traffic is you hit, like you convince someone to click, right?

**Daniel Lopes:** You convince someone to do something, right?

**Daniel Lopes:** Like go through with it.

**Daniel Lopes:** And so one is about like positioning correctly and a bunch of other factors.

**Daniel Lopes:** The other one is about like selling them.

**Daniel Lopes:** And then engagement is delivering or over delivering on the promise of what the promise is your headline and your description.

**Ryan Singer:** Right.

**Ryan Singer:** Yep.

**Daniel Lopes:** And so so and then hopefully your promise matches the intent of the user.

**Daniel Lopes:** And when you go over deliver on that promise, it's like, whoa, I'm here.

**Daniel Lopes:** This is amazing.

**Daniel Lopes:** I'm going.

**Ryan Singer:** Yes.

**Daniel Lopes:** I'm clicking through.

**Daniel Lopes:** I'm spending a bunch of time.

**Daniel Lopes:** And then conversions like, holy , you build so much credibility and you deliver so much value.

**Ryan Singer:** I want more.

**Ryan Singer:** want to go deeper.

**Ryan Singer:** I want to talk to you.

**Ryan Singer:** Yep.

**Ryan Singer:** Coming back to, let's say, kind of instrumenting opportunities for optimization.

**Ryan Singer:** Are there things here that you expect to be measuring and populating in the learn and improve section?

**Daniel Lopes:** Yes.

**Daniel Lopes:** Yes.

**Daniel Lopes:** So quality is.

**Daniel Lopes:** is.

**Daniel Lopes:** Around alignment.

**Daniel Lopes:** And the same thing with, like, the improve area, by the way, is around alignment, right?

**Daniel Lopes:** So think of alignment as, like, you have a grounding document or a grounding truth, and it's about, like, how much, like, this deviates from that truth, right?

**Daniel Lopes:** And where does it deviate?

**Daniel Lopes:** And so, for instance, like, there's a company description.

**Daniel Lopes:** Well, is this thing aligned to that company description?

**Daniel Lopes:** There is a writing guideline.

**Daniel Lopes:** Is this aligned to that writing guideline, right?

**Ryan Singer:** Like, so think of it as, like, grounding evals, almost.

**Daniel Lopes:** Like, I don't know if that's even a term, but it's, you know, but then there's, like, there's, like, an opportunity grounding of, like, this is the opportunity, this is the intent of what we're trying to do, this is the brief, this is the research.

**Daniel Lopes:** So there's, like, research grounding, you know, and alignment.

**Daniel Lopes:** There's, like, opportunity and intent alignment.

**Daniel Lopes:** And then there's, like...

**Ryan Singer:** The company, product, persona, and guidelines alignment, which is like your context files, if you will, right?

**Daniel Lopes:** And so it's like a drift, right?

**Daniel Lopes:** And then a drift can happen, you know, because of like context poisoning or, you know, over compressing or, you know, or like missing a point or, you know, some version of that.

**Ryan Singer:** that this?

**Ryan Singer:** Is this misalignment?

**Daniel Lopes:** So improve is misalignment, that needs to be realigned because there's a need for, like, there's a reason the alignment is there, right?

**Daniel Lopes:** Okay, hold on, hold on.

**Daniel Lopes:** Sorry.

**Ryan Singer:** Okay.

**Ryan Singer:** All right.

**Daniel Lopes:** Yeah, like, and hopefully, like, over time, like, we're building these kind of like best practices and evals based on studies and a lot of data we're collecting across a lot of customers so that, like, we can make more recommendations.

**Daniel Lopes:** more solutions on the kinds of misalignments.

**Daniel Lopes:** That, that we should do.

**Daniel Lopes:** Like.

**Daniel Lopes:** The quality, one has so much potential for a very unique IP, basically.

**Daniel Lopes:** Yeah, and just so...

**Daniel Lopes:** Very subjective and a hard problem.

**Daniel Lopes:** One quick thing on kind of how, like, check that.

**Daniel Lopes:** I'm going, like, it's almost like I did a bunch of research on how analysts thinks about it and users and peer reviews and things like that.

**Daniel Lopes:** And there's kind of like these attributes, if you will, right?

**Daniel Lopes:** Like, this is, and I'll connect here in a second, but it's like usability, capability, usability, value, trust, support, innovation.

**Daniel Lopes:** So over time, that's for, like, brand perception, right?

**Daniel Lopes:** And how AI engines think of that.

**Daniel Lopes:** And whereas, like, for here, like, there can be, like, attributes that kind of, like, matter to them, right?

**Daniel Lopes:** If you will.

**Daniel Lopes:** At the level.

**Daniel Lopes:** At the content level, you know?

**Daniel Lopes:** And those attributes are, you know, personalized.

**Daniel Lopes:** guys.

**Daniel Lopes:** guys.

**Daniel Lopes:** know,

**Daniel Lopes:** Based on the context of the company, but then there's also like global things as well, right?

**Daniel Lopes:** There are like, like for instance, like the, like the attribution, you know, better attribution or more examples or, you know, but there's like having images or things like that, like are actually like enrichment things, right?

**Daniel Lopes:** That, that we know are like well-known patterns.

**Daniel Lopes:** Yeah, but then there's also, Ryan, like the things we're going to learn about them, right?

**Daniel Lopes:** And their baseline, right?

**Daniel Lopes:** Like, so, so for instance, like if you have 10,000 pages and you look at only your blog pages and within those blog pages, you understand the type of content it is and you have all this data on it, right?

**Daniel Lopes:** Like you can then figure out, hey, for pages to have higher engagement and a higher percentage or propensity for people to go to the bottom of the page and click through to the next page.

**Daniel Lopes:** These are the patterns we learn.

**Daniel Lopes:** And then those are the patterns that then you can suggest improvements to the other ones.

**Daniel Lopes:** And so think of it as like, this is the baseline.

**Daniel Lopes:** These are like your top performers in any, you know, metric.

**Daniel Lopes:** And these are like your low bottom performers.

**Daniel Lopes:** And you learn from what patterns can be reproduced here so that these can be higher to here, you know, so that your baseline increases.

**Daniel Lopes:** Does that make sense?

**Ryan Singer:** Got it.

**Ryan Singer:** That makes sense.

**Ryan Singer:** I think it's all like interesting.

**Ryan Singer:** And so in the scope of what we're trying to solve right now, we're trying to figure out kind of how to present opportunities as work items.

**Ryan Singer:** And so let's just call quality quality for the moment.

**Ryan Singer:** And I just want to see if we can kind of, if we can just kind of maybe spell out how to measure these things, we might get to a point where I think we have like a pretty solid picture of like what we might be looking at, what we might be surfacing, what the action is and so on.

**Ryan Singer:** And then this could be an.

**Ryan Singer:** Input for us to then look at, you know, look at solution ideas.

**Daniel Lopes:** I think quality, You can even spell out as like score on the rubric of rates that we can.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Every paper is going to have a quality score and that quality score is going to have.

**Ryan Singer:** That's actually this.

**Daniel Lopes:** A trend line.

**Daniel Lopes:** Yes.

**Daniel Lopes:** And so just think of it as just like the quality dropped or the quality has been low for a long time.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Always has been low.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And so like, as far as this is concerned, we almost don't even need to think about the rules.

**Daniel Lopes:** And that's why I'm trying to create these composite scores everywhere because otherwise it's impossible to define the rules everywhere, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** Super.

**Daniel Lopes:** define the logic centrally in a composite score.

**Ryan Singer:** I think it's just good to know that like if something has been flagged as improve because of a quality issue, you know, is that what this is?

**Daniel Lopes:** Yeah, like low quality score or a big dip.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So and then.

**Daniel Lopes:** And don't worry about it.

**Daniel Lopes:** This is going to be determined by the scoring on their way.

**Ryan Singer:** Yeah.

**Ryan Singer:** But then if we're getting into the work step of an improvement, then we're just going to want to know that we have the ability to unpack what that particular score means so that we know what to actually do as an action.

**Daniel Lopes:** Good.

**Ryan Singer:** Okay.

**Ryan Singer:** I'm guessing the rest of these are easier.

**Daniel Lopes:** Even if it's not a human doing the improvement for the quality, still has to, we have to unpack even more.

**Ryan Singer:** Oh, yeah, totally.

**Ryan Singer:** Yeah, totally.

**Ryan Singer:** Uh-huh.

**Ryan Singer:** Okay.

**Ryan Singer:** Are these worth spelling out or do we just want to take it for granted that like, hmm.

**Daniel Lopes:** Those are very measurable.

**Daniel Lopes:** I think the only one that the engagement and conversions are probably like coming soon.

**Daniel Lopes:** I think it's worth it.

**Daniel Lopes:** Even like, I think I can guess, but our team didn't understand that impressions, low impressions equals sh**.

**Daniel Lopes:** Cheat event tags, for example, you know, or check that.

**Daniel Lopes:** Yeah, like, let me just show a quick example, because this is...

**Daniel Lopes:** So there's a set of things that are related to impressions, a set of things that are related to traffic.

**Daniel Lopes:** Ryan, this is for a page on cursor pricing, okay?

**Daniel Lopes:** This is check that.

**Ryan Singer:** For check that.

**Daniel Lopes:** So we have thousands of...

**Daniel Lopes:** And you can see, like, it went, and we got, like, clicks and impressions, and then it pretty much went to zero.

**Ryan Singer:** Yeah.

**Daniel Lopes:** Right?

**Daniel Lopes:** So this is what we're trying to flag.

**Daniel Lopes:** Like, we...

**Daniel Lopes:** Like, someone caught this manually, somehow, but, like, it's highly unlikely in the sea of  and signals that someone would catch this.

**Daniel Lopes:** And had we not acted, this wouldn't have happened, you know?

**Ryan Singer:** Totally, totally.

**Ryan Singer:** Back on the whiteboard here, I'm actually pasting that...

**Ryan Singer:** I'm just dropping this in.

**Ryan Singer:** What is this, in terms of this?

**Ryan Singer:** I'm just kind of...

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Cheat event tags, for example, you know, or check that.

**Daniel Lopes:** Yeah, like, let me just show a quick example, because this is...

**Daniel Lopes:** So there's a set of things that are related to impressions, a set of things that are related to traffic.

**Daniel Lopes:** Ryan, this is for a page on cursor pricing, okay?

**Daniel Lopes:** This is check that.

**Daniel Lopes:** For check that.

**Daniel Lopes:** So we have thousands of...

**Daniel Lopes:** And you can see, like, it went, and we got, like, clicks and impressions, and then it pretty much went to zero.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Right?

**Daniel Lopes:** So this is what we're trying to flag.

**Daniel Lopes:** Like, we...

**Daniel Lopes:** Like, someone caught this manually, somehow, but, like, it's highly unlikely in the sea of  and signals that someone would catch this.

**Daniel Lopes:** And had we not acted, this wouldn't have happened, you know?

**Daniel Lopes:** Totally, totally.

**Daniel Lopes:** Back on the whiteboard here, I'm actually pasting that...

**Daniel Lopes:** I'm just dropping this in.

**Daniel Lopes:** What is this, in terms of this?

**Daniel Lopes:** I'm just kind of...

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Daniel Lopes:** This is a, there was a rise in impressions, and then a rise in clicks, which is traffic, right?

**Daniel Lopes:** Followed by a dip in both.

**Daniel Lopes:** So when clicks drop, but impressions don't, that means your promise is off, like no one's clicking on your ad, right?

**Daniel Lopes:** Like when impressions and clicks drop, then it's usually like the signal's bad.

**Daniel Lopes:** Like they came in your conscious part of garbage, right?

**Daniel Lopes:** And that usually, the leading indicator of that, because that's lagging, right?

**Daniel Lopes:** You're already .

**Daniel Lopes:** It's already went to zero, right?

**Daniel Lopes:** The leading indicator of that is like the day that things spiked the first time, you could have seen the engagement and the bounce rate.

**Ryan Singer:** Like time on page, bounce rate, how many of the visitors that landed, aka enter the site through this page.

**Ryan Singer:** It was an average session time compared to everything else, right, specifically for this channel, again, like SEO inorganic.

**Ryan Singer:** And if it was, like, way lower than anything else, like lookalikes, similar type of page, more overall baseline for the site, then it's telling you the content was bad, essentially.

**Ryan Singer:** Like, it wasn't good, right?

**Ryan Singer:** And so had you, had we addressed that, like, at that spike, there's a likelihood that we would be even higher now, right?

**Daniel Lopes:** But it's better to address it fast, like we did, but it's like, it wasn't that fast.

**Daniel Lopes:** It was like, but a week later.

**Daniel Lopes:** That was also manual.

**Daniel Lopes:** So, like, everything there was, check that has 10,000 pages, we're striking gold in some places, like, entropic, one of the pages, cursor pricing, and people are not catching.

**Ryan Singer:** So, so, this should be, this should be surfacing and learn and improve, yes?

**Ryan Singer:** Yes, it should.

**Ryan Singer:** Okay.

**Ryan Singer:** So what I think is, I think that we.

**Ryan Singer:** We've gotten warmer with this kind of, I think we shared a lot of domain knowledge with what we did here.

**Ryan Singer:** Yeah.

**Daniel Lopes:** What I want to make sure is that we don't think that we've solved it when like this kind of thing is the real problem.

**Ryan Singer:** Do know what mean?

**Ryan Singer:** Like this is like a real case.

**Ryan Singer:** So I want to check like, does this actually map to what we talked about?

**Ryan Singer:** And is all this like general stuff like real or is it more complicated than that in reality?

**Daniel Lopes:** Sorry, it's a small little fire drill.

**Ryan Singer:** My EA accidentally share comp information on a public.

**Daniel Lopes:** Oh, yeah.

**Daniel Lopes:** Or like an executive that we're hiring.

**Daniel Lopes:** It's like a rich person texting me like, what the hell?

**Daniel Lopes:** Sorry.

**Daniel Lopes:** Brutal.

**Daniel Lopes:** Can you repeat that?

**Daniel Lopes:** I apologize.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So the thing is, okay.

**Daniel Lopes:** So briefly what happened was like, we've been kind of sketching it, like sketching out a lot of what's...

**Daniel Lopes:** It's in your head, Marcel, around what optimization means, right?

**Daniel Lopes:** And my concern is we might not have gone deep enough.

**Daniel Lopes:** And what I want to do is I want to use this as a test case of like, this is a real kind of thing that we want to be able to surface, right?

**Daniel Lopes:** So I think what we want to be able to say is like, what is this, right?

**Daniel Lopes:** And then this is the kind of like concreteness of specific cases of like, this is the kind of thing we should be surfacing in terms of detection and action.

**Daniel Lopes:** Yeah, it, like, they're, okay, so, so if you look, if you think back of like what Daniel was showing on the filters and things like that, right?

**Daniel Lopes:** Yep.

**Daniel Lopes:** Normally, it's like, you, you do a bunch of stuff, publish a bunch of pages or whatever.

**Daniel Lopes:** When you're actively doing like what we're doing in check that, like, there would be signals, right?

**Daniel Lopes:** And the signals will tell you we did something right.

**Daniel Lopes:** And usually the signals will be like, oh, look, this guy.

**Daniel Lopes:** Text.

**Daniel Lopes:** That's good.

**Daniel Lopes:** Like, you know.

**Daniel Lopes:** And then it was like, followed by, whoa, this got some impressions.

**Daniel Lopes:** Index is not even that in impressions.

**Daniel Lopes:** It's just got index.

**Daniel Lopes:** Yeah, yeah.

**Daniel Lopes:** And then like, okay, so this thing got impressions, but it's not getting clicks now all of a sudden, right?

**Daniel Lopes:** So now it's like, okay, if you do nothing, let's just say there's one page, that page is getting impressions consistently.

**Daniel Lopes:** There are many pages on Google Search Console, Ryan, that they were not going to have the purple.

**Daniel Lopes:** Like, you see the impressions?

**Daniel Lopes:** ton of impressions and zero clicks, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** That's another concrete example.

**Daniel Lopes:** So then you're like, look, we got impressions.

**Daniel Lopes:** That means probably we got the opportunity right and we got the intent somewhat right.

**Daniel Lopes:** But it either means like the headline or, you know, the promise of the page is still off from the intent that we're getting.

**Daniel Lopes:** And then it also means like...

**Daniel Lopes:** It could also mean that you just need to do something a little bit more to drive the average position a little bit higher, right?

**Daniel Lopes:** And so then it's like truly, you know, like, hey, we need to link to it a little bit more.

**Daniel Lopes:** You need to like try to get a little bit higher because sometimes you're getting a place because it's truly like a garbage search and it's like positioned so low on the page.

**Daniel Lopes:** No one's seeing it, right?

**Daniel Lopes:** Like an impression doesn't mean somebody actually saw it, right?

**Daniel Lopes:** And the thing within your control is like go optimize the meta title, headline, meta description, things like that and see if it improves, right?

**Daniel Lopes:** See if it like you actually get some clicks, you know?

**Daniel Lopes:** If not, wait a little longer and if you see nothing, then try like some other optimizations.

**Daniel Lopes:** Normally my hack here is like link to it and try to like force it to, for Google to think this is really important, to try to force Google to like rank you a little bit higher to see if you get clicks, right?

**Daniel Lopes:** But.

**Daniel Lopes:** But I usually do the headline first and that segment, right?

**Daniel Lopes:** And this is just like one page.

**Daniel Lopes:** Then let's say you start to get clicks.

**Daniel Lopes:** The second you get clicks, it's like now all of a sudden you're in like watch mode, right?

**Daniel Lopes:** And you're ideally, if you only had one page on your site and that's the only page you care about, like you're just like watching it like a  hawk, right?

**Daniel Lopes:** And the second you get clicks, you're like, is this like, are people like spending time on this?

**Daniel Lopes:** Is the bounce higher, right?

**Daniel Lopes:** Best case scenario is like, can I just like record the  session and see what happened, right?

**Daniel Lopes:** And those signals are like the most, it's like your first impressions to Google on this page, right?

**Daniel Lopes:** They're like super, super, super, super, super important.

**Daniel Lopes:** And you want to watch it like a hawk and then very, very, very, very quickly respond to it.

**Daniel Lopes:** And the response to it is either, holy crap, like people are spending three minutes on this and it's three times higher than every other page on the site.

**Daniel Lopes:** We did something, right?

**Daniel Lopes:** Let's go try to do this again in other places.

**Daniel Lopes:** It's like, you know, or.

**Daniel Lopes:** Hey, we read this, and this is pretty shallow, we should, like, rethink this content completely, which is what we did with Cursor, right?

**Daniel Lopes:** But it's very subjective because, for instance, like, the same pipeline that generated this Cursor page also generated this HeyGen page, okay?

**Ryan Singer:** And the HeyGen page never had a dip.

**Ryan Singer:** And so, like, if you look at this, it's like, this page never had a dip, you know?

**Ryan Singer:** And so you're like, okay, this is, like, the same pipeline, you know?

**Ryan Singer:** And it's just, like, a audience for Cursor, you know?

**Daniel Lopes:** Anecdotally, I think it's because an audience for HeyGen, like, it's kind of, like, lower, it's just, like, random consumers kind of thing, whereas Cursor is, like, highly sophisticated, like, people that are doing really deep research and care a lot about the details, how it's presented and whatnot, whereas, like, HeyGen is, like, a little bit more, like, generic, like, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** That's my hypothesis.

**Daniel Lopes:** like the audience, right?

**Daniel Lopes:** One audience is like more technical than the other and cares more about service, you know, like, but you can see it like, you know, like finding the signals would be even pretty, pretty hard with SEO.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** We've, I'm looking at where we are with time.

**Daniel Lopes:** Let's, let's take five.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** right.

**Daniel Lopes:** Um, is, uh, is, is five enough or do you guys need 10?

**Daniel Lopes:** Five worth.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Let's do five and we'll see you in five.

**Daniel Lopes:** It's such a complex domain.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** There's so much things back into Amdric's Corner up there.

**Daniel Lopes:** There's so much Logan in here.

**Daniel Lopes:** They're almost in the first thing.

**Daniel Lopes:** Oh, Oh, Oh.

**Daniel Lopes:** What's going on, dude?

**Daniel Lopes:** Thank you.

**Ryan Singer:** You don't think when you're like a couple of sets, functions away from, like, cracking it.

**Daniel Lopes:** You You

**Daniel Lopes:** Imagine that, like, Ryan doing this and having to do, like, interviews with users in order to get to this truth.

**Ryan Singer:** Oh, man.

**Ryan Singer:** Like, you know, that's why we have so much confidence in what we're doing is because it's just, like, so many years of, like, doing this for so many different companies that are all successful, you know, and, like, That's what's fun about this project is it's, like, it's, I feel like it's all about, like, how do we, how do we, like, funnel all this stuff that you already know into this product?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** It's not, like, the head scratching of how does it work?

**Ryan Singer:** It's, like, we know how this works.

**Ryan Singer:** How the heck do we, like, get it in here?

**Ryan Singer:** Yeah, and, like, simplify it and give, like, customers, like, the end user, like, a sense of control versus, like, there's things where truly, like, we don't kind of need their opinion.

**Ryan Singer:** And then there's, like, little nuanced things, like, like.

**Ryan Singer:** What you were saying, like, should you archive this or should you, like, repurpose?

**Ryan Singer:** Like, it would probably be a gnarly agent, but then a human judgment is actually decently easier here.

**Ryan Singer:** You know, like, and it's kind of like this weird thing about AI.

**Ryan Singer:** Sometimes there's things that are, like, agents are a hundred times better on really hard to do complex things, like the product snapshots.

**Daniel Lopes:** And then, like, on the simplest thing, it's just like, no, no, just have a human review.

**Daniel Lopes:** It's like, it'll take 10 seconds, like, don't worry.

**Daniel Lopes:** Totally.

**Daniel Lopes:** Totally.

**Daniel Lopes:** This is very sounder, you know.

**Daniel Lopes:** So, okay, so what I want to do is I want to step back and, because I feel like we could just kind of talk about optimization as a science all day, you know.

**Daniel Lopes:** And I want to, what I want to do is I want to bring this kind of back to you, Daniel, around kind of where's the question.

**Daniel Lopes:** So my understanding was that, like, we moved the pipeline for creation out of learn and improve.

**Daniel Lopes:** And now what's, there's like a missing piece, which.

**Daniel Lopes:** It's like the pipeline piece is kind of missing there.

**Ryan Singer:** And I'm wondering, like, do we want to take all this kind of shared context that we built up now?

**Ryan Singer:** And do we want to look at what is that pipeline of work inside of Learn and Improve?

**Daniel Lopes:** Or is it a different question?

**Daniel Lopes:** I think that would be an interesting experiment.

**Daniel Lopes:** Because there are tools in the market that try to do the included part.

**Daniel Lopes:** And they're definitely better than nothing.

**Daniel Lopes:** And they've done really well, like, financially, everything.

**Daniel Lopes:** Because it's a really hard problem.

**Daniel Lopes:** And the bar is so low.

**Daniel Lopes:** Like what Marcel is describing, that is the holy grail of, like, organic content.

**Daniel Lopes:** Like, tracking everything, knowing where things are getting tracked.

**Daniel Lopes:** None of the tools do that.

**Daniel Lopes:** They just do at the page level the most basic things.

**Daniel Lopes:** Just like, fix your broken links, fix your headings.

**Daniel Lopes:** That'll...

**Daniel Lopes:** That'll...

**Daniel Lopes:** That is valuable, the closer we can get to the stuff that Marcel is describing, that is  mind-blowing for what the public is used to.

**Daniel Lopes:** Oh, it's huge.

**Daniel Lopes:** It's totally huge.

**Daniel Lopes:** And I think that place where we have an assistant today, if the learning improved, if the creator is out of it, and that's a different problem, and we can't crack that.

**Daniel Lopes:** If there is a path to make that concrete in that same user interface, with the same simplicity of the separation that we have now, I think we're really close to something that's way better than server SEO, for example, that is closer to a shooting one of Marcel is, right?

**Daniel Lopes:** But it can't work.

**Daniel Lopes:** The pipeline, it can't work.

**Daniel Lopes:** It's trying.

**Daniel Lopes:** Yeah, and just so you understand how relevant this is, right now, we ramp as a customer, and then...

**Daniel Lopes:** Brex is a customer, and then we just kicked off.

**Daniel Lopes:** Or we're kicking off today with Spendesk, which is like a European version of it, right?

**Daniel Lopes:** And essentially, like, this is what we're dealing with.

**Daniel Lopes:** Like, their traffic is, like, in free fall.

**Daniel Lopes:** And they hired us, essentially.

**Daniel Lopes:** And it's a highly competitive space, right?

**Daniel Lopes:** And, like, we did all of this manually.

**Daniel Lopes:** Like, everything you see here is just, like, done to try to, like, give them, like, what to go focus on.

**Ryan Singer:** It's all based on new opportunities.

**Daniel Lopes:** And I was like, guys, what the F?

**Daniel Lopes:** Like, they have 700 pages.

**Ryan Singer:** Like, you know?

**Ryan Singer:** And so you go here and you go, like, hey, like, this is, it's in decline.

**Daniel Lopes:** It's in, like, free fall.

**Daniel Lopes:** And, like, how do you know what to do here?

**Daniel Lopes:** There's 712 of them, right?

**Daniel Lopes:** Like, all of these are dropping.

**Daniel Lopes:** Which one should you focus on?

**Daniel Lopes:** And why?

**Daniel Lopes:** Why is this dropping?

**Daniel Lopes:** Is that a good thing or a bad thing?

**Daniel Lopes:** It's, like, or, you know, is that, like...

**Ryan Singer:** Even just the realization of that, you have 700 pages, you shouldn't be thinking too much about creating your pages, just go fix that.

**Daniel Lopes:** Having the place in the app that tells you that, that is also something that even our team isn't thinking about.

**Daniel Lopes:** And our team is really good compared to the rest of the market.

**Daniel Lopes:** So then what people will do here, right, exactly, like, they'll come here and they'll just, like, hit export on this.

**Ryan Singer:** And this is all the data you have.

**Ryan Singer:** And then they'll do an analysis completely absent of the context of the company and anything else.

**Ryan Singer:** It just looks at this, right?

**Ryan Singer:** And all you have is a URL.

**Ryan Singer:** And it has no context of anything else, no signals or anything else, you know?

**Daniel Lopes:** And it's just, like, , like, this is so bad.

**Daniel Lopes:** And this is literally what our team does, too, and what I've had to do, right?

**Daniel Lopes:** Because there's nothing else.

**Daniel Lopes:** And so then, like, the next best thing I would do is I would build a scraper to go through each URL and do a summary of the content of the URL and then, like, build all these, like, play tables or processes or whatever.

**Daniel Lopes:** But then those didn't have GA data, right, or GSC.

**Daniel Lopes:** data.

**Daniel Lopes:** was just this data.

**Daniel Lopes:** So anyways, it's just truly a pain point.

**Daniel Lopes:** Oh my God.

**Daniel Lopes:** My eyes are watering.

**Daniel Lopes:** There's so much opportunity here.

**Daniel Lopes:** I can't even handle it.

**Daniel Lopes:** It is like every site on the planet is dealing with this and there is no good solution in this.

**Ryan Singer:** this is like, I have so much conviction in this, man.

**Ryan Singer:** Okay.

**Ryan Singer:** Yeah.

**Ryan Singer:** Like, I'm a million percent with you on the conviction.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So here's the question.

**Daniel Lopes:** So what are we trying to solve for March?

**Daniel Lopes:** Well, low hanging fruit, urgent, like do this or you're , like improvement.

**Daniel Lopes:** Metric space, right?

**Daniel Lopes:** Like metric space, like do this or you're, or like, this is bad, right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Like for instance, like if your biggest traffic driver just  dipped, you should just drop everything you're doing.

**Daniel Lopes:** This is a P0 critical bug.

**Daniel Lopes:** Go  fix it, right?

**Ryan Singer:** And we should publish nothing until we figure out what just happened there.

**Daniel Lopes:** With one of our biggest customers, Augment Code, that happened to two of our biggest traffic diver.

**Daniel Lopes:** We didn't catch it for four weeks.

**Daniel Lopes:** And then we didn't fix it for another four.

**Ryan Singer:** And it really cost us a lot, essentially.

**Ryan Singer:** So what else?

**Ryan Singer:** Literally, what's the list of things where it's like, we can do that for March?

**Daniel Lopes:** Those are the things that we can catch that you absolutely should be catching.

**Daniel Lopes:** I think the fixed stuff is just super no-brainer because it's just very rules-based.

**Daniel Lopes:** And we can start with a few rules and then build more rules.

**Daniel Lopes:** And the refresh is truly just expire label on it.

**Daniel Lopes:** And then the improve is based on those filters that Daniel already built, which is almost to the first page.

**Daniel Lopes:** You know, traffic dip, impressions dip, like, again, it's like very rules-based, but metrics-driven.

**Ryan Singer:** Your biggest traffic page just dipped?

**Ryan Singer:** Is that included in that?

**Daniel Lopes:** Yeah, yeah.

**Ryan Singer:** It's just like, improve is like the...

**Ryan Singer:** So give me the top three, give me the top three smart filters for improve that like are real for March.

**Ryan Singer:** Your traffic just dipped, your engagement is just dipped or is  because that's like a leading indicator of everything else is going to happen soon, you know.

**Ryan Singer:** And impressions, no clicks, or you drop average rank, or you're almost in the first page, which is kind of like all similar actions, which is just like you're almost there, you know, like...

**Ryan Singer:** It's like you didn't quite get the same...

**Ryan Singer:** You need it to make it to the next level of time, you know?

**Ryan Singer:** These are very meaningful.

**Daniel Lopes:** Okay, dumb question.

**Daniel Lopes:** Do these happen, like, are there multiple of these?

**Daniel Lopes:** If this wasn't a filter, but this was a, this was a, like, label?

**Ryan Singer:** Yeah.

**Ryan Singer:** But if this was a diagnosis, you know what I mean?

**Daniel Lopes:** Let me, let me, let me grab all these.

**Daniel Lopes:** Let me grab all these.

**Daniel Lopes:** be a critical thing.

**Daniel Lopes:** Let me, let me say, like, possible states per page, okay?

**Daniel Lopes:** Possible diagnoses per page.

**Ryan Singer:** I'm going to paste these.

**Daniel Lopes:** Your, your biggest traffic page, this is, this is a, a big traffic page that dipped.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Engagement dip died.

**Daniel Lopes:** Impressions, but no clicks.

**Daniel Lopes:** You're almost there.

**Daniel Lopes:** Then here was, I'm going to say.

**Daniel Lopes:** Rule broken, and expired, out of date, past good, you know?

**Daniel Lopes:** Yeah, it's like, think of it as like some of these are preventive, and some of these are like, you're already sick, like now you gotta go, you know, like some of these are like, you know, yeah, yeah, but severity, yeah, what's the severity?

**Ryan Singer:** So anything that is not preventive, it's gonna be pretty high, but, and then the further it is on like, you know, if we had conversion pixels already, would be like conversion is the highest, you know, engagement is the second, because you already got people through the site, you know, how many things have to happen for them to get to the  site, like so much, right?

**Daniel Lopes:** Like, and then you just like,  that up, right?

**Daniel Lopes:** And then like, traffic dip is like, oh, crap, like if you don't get traffic, there's no chance that you're ever gonna get conversions, you know, impressions like...

**Daniel Lopes:** ...

**Daniel Lopes:** I think the first one is like a high alert, high severity.

**Ryan Singer:** That is like, I think you did nothing, but you're just improving your biggest traffic grabbers.

**Daniel Lopes:** Yeah, what I was saying is like, if we had conversion, it would be the highest thing.

**Daniel Lopes:** Oh, yeah.

**Daniel Lopes:** Like, because it's like, there might be a broken link to your CTA, like, go  with that.

**Daniel Lopes:** But yeah, but given what we have, because we're in the March conversation of these, just how could we flag these as like, let's say, let's say like severe or like worth looking at because maybe you can pick up something, you know what I mean, versus like when you have time.

**Ryan Singer:** Yeah, it's like the first one is important and urgent.

**Daniel Lopes:** The second one is important and will be urgent if you don't do anything about it.

**Daniel Lopes:** So this is like, um, the, um, and then...

**Daniel Lopes:** The rest is like, um, like.

**Ryan Singer:** Is it more, are the rest more like opportunities?

**Ryan Singer:** But rule brokenness is.

**Daniel Lopes:** Rule broken is a big deal.

**Daniel Lopes:** Yeah, like, yeah, sorry.

**Daniel Lopes:** Rules broken is important if it's a high impact page.

**Daniel Lopes:** Uh-huh, uh-huh.

**Ryan Singer:** But if it's like a dead in the water page, who gives a ?

**Ryan Singer:** Like, don't go not fix the first one, right?

**Ryan Singer:** Yes.

**Ryan Singer:** Or don't go not do optimization on page, you're almost there, because you're trying to fix a thing that is dead in the water.

**Ryan Singer:** So let me, let me rename this.

**Daniel Lopes:** Fix high impact.

**Ryan Singer:** Or high impact rule broken.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Needs fix.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Can we, can we call it?

**Daniel Lopes:** It's just like, who cares?

**Daniel Lopes:** Like, like, everybody, one of our customers has 10,000 pages.

**Daniel Lopes:** Like, who cares?

**Daniel Lopes:** They have, like, so much  signal.

**Daniel Lopes:** There was almost like a...

**Daniel Lopes:** Modifier here, if it's a high-impact page, almost everything bumps the priority, huh?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Do we already have the ability today to say which page is high-impact and which page isn't?

**Daniel Lopes:** It's just based on traffic.

**Daniel Lopes:** That's what we're working for right now.

**Daniel Lopes:** all the UI that we have with the metrics and everything will enable us to that.

**Daniel Lopes:** Right.

**Daniel Lopes:** But where are we for March?

**Daniel Lopes:** Like, what of this can we actually translate into, like, this is data we have in some version of this where we could actually – here's what I'm picturing.

**Daniel Lopes:** I want to have – Yeah.

**Daniel Lopes:** Yeah?

**Daniel Lopes:** So high-impact – just translate this then, make this more concrete.

**Daniel Lopes:** This is, like, well-trafficked?

**Daniel Lopes:** Like, what is this?

**Daniel Lopes:** Yeah, let's just assume everything is high-traffic.

**Ryan Singer:** Yeah, fully engaged.

**Ryan Singer:** And the thing is, right now it's going to be high-traffic, but in the future it's, like, high-traffic.

**Ryan Singer:** With the qualifier of the intent of the page, right?

**Daniel Lopes:** So high traffic to, what does a CFO versus a CEO do?

**Daniel Lopes:** It's like low intent traffic, which I have high volume.

**Daniel Lopes:** So high volume, low intent.

**Daniel Lopes:** Whereas high volume, high intent is like  at the highest, right?

**Daniel Lopes:** Uh-huh.

**Daniel Lopes:** Uh-huh.-huh.-huh.

**Daniel Lopes:** But that's like...

**Daniel Lopes:** Can you write that down?

**Daniel Lopes:** Because that is worth tracking.

**Daniel Lopes:** Because I don't think we're tracking that.

**Daniel Lopes:** And it's easy to track, actually.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So there's a few things.

**Daniel Lopes:** For opportunities, we track intent.

**Daniel Lopes:** And then we track relevance.

**Daniel Lopes:** then for pages...

**Ryan Singer:** We're literally writing the page analysis this week.

**Ryan Singer:** So I want to make sure I don't forget that.

**Ryan Singer:** Yeah.

**Ryan Singer:** for new page opportunities, high volume, high intent is a thing.

**Ryan Singer:** Because you're tracking intent for new page opportunities.

**Ryan Singer:** But here in optimization, we have...

**Ryan Singer:** We can still figure out the intent of the existing pages because we can analyze the existing pages, too, the semantics of it.

**Ryan Singer:** So that works.

**Daniel Lopes:** Yeah?

**Daniel Lopes:** Okay.

**Daniel Lopes:** I think that we have everything.

**Daniel Lopes:** The only thing we don't have, I guess, like Spire, we could have, too.

**Daniel Lopes:** By the way, just to note, relevance is really important.

**Daniel Lopes:** There's a lot of sites like DeepGram, for example, where there's a lot of pages that are just not that relevant, and they were there for more, like, traffic boost, you know?

**Daniel Lopes:** They're just, like, not relevant to your audience at all.

**Daniel Lopes:** Like, the low relevance, you know?

**Daniel Lopes:** So relevance fits into our intent, right?

**Daniel Lopes:** They're just different.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Let me try and simplify this.

**Daniel Lopes:** Let's boil this down.

**Daniel Lopes:** Assuming, let's say there's a first cut, right, of pages that are high traffic, or were, or were recently.

**Ryan Singer:** about the opportunity under the hood of that surface area.

**Ryan Singer:** And, you know, there are cases where, like, it could be fake, right?

**Ryan Singer:** Like, for instance, like, yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** You already, just because time is going so fast, I want to, what I think, I think we just captured something really important, which is that when it comes to opportunities, there's a, if these, sorry, opportunities, optimizations, optimizations.

**Ryan Singer:** When it comes to learn and improve optimizations, there are pages that are not, they don't, out of the 712, we shouldn't even be looking at them because, because the underlying opportunity isn't there, right?

**Ryan Singer:** away high traffic from expired.

**Ryan Singer:** And I want to say possible diagnoses per, I'm going to call it, page with opportunity.

**Ryan Singer:** So just one thing here is there's a very important distinction of realized versus unrealized opportunity.

**Ryan Singer:** Okay.

**Ryan Singer:** And so if the aggregate opportunity here is, let's say, 10,000 visits a month and you're at, like, 9,700, like, it's pretty realized.

**Daniel Lopes:** And any -ups there will, like, hurt you.

**Daniel Lopes:** So it's more urgent.

**Daniel Lopes:** Whereas, like, unrealized opportunities, it's a lot more, like, optimizations to try to realize more of it, you know?

**Ryan Singer:** But there's less to lose.

**Ryan Singer:** Like, you have nothing to lose, essentially, right?

**Ryan Singer:** You have a lot to gain and nothing to lose.

**Ryan Singer:** Whereas, like, realized opportunities, you're 97% realized, you have a lot to lose.

**Ryan Singer:** Yes, I'm sorry.

**Ryan Singer:** Let me just really quickly.

**Daniel Lopes:** So there's realize and unrealized or realize there is this isn't free fall, drop everything.

**Daniel Lopes:** That's the highest tier.

**Daniel Lopes:** And then there's like, hey, it's realize.

**Daniel Lopes:** And these are like screaming alerts.

**Daniel Lopes:** They're going to churn if you don't do something about it right now.

**Daniel Lopes:** And you can still prevent it.

**Daniel Lopes:** Right.

**Ryan Singer:** That's the next one.

**Ryan Singer:** And then after that is everything else.

**Daniel Lopes:** Screaming alerts, you can prevent it.

**Ryan Singer:** What's that?

**Ryan Singer:** Like this page is broken.

**Ryan Singer:** There's a 404 is built, right?

**Daniel Lopes:** Like, or it could be like, you know, like the thing.-huh.

**Daniel Lopes:** Like the H1.

**Daniel Lopes:** There's no H1 on this page.

**Daniel Lopes:** Totally.

**Daniel Lopes:** Okay.

**Daniel Lopes:** Got it.

**Daniel Lopes:** Okay.

**Ryan Singer:** like somebody who's funky redesign of the website and switch to H1's page.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** Got it.

**Ryan Singer:** Okay.

**Ryan Singer:** So if I have a realized opportunity.

**Ryan Singer:** If I have a realized opportunity, I need to, if it's.

**Ryan Singer:** In free fall, then I have to immediately jump on it to try and fix it.

**Ryan Singer:** And if there's an alert on it where something is broken, I have to jump in and fix it.

**Ryan Singer:** Yeah.

**Ryan Singer:** Really centered for our paper.

**Ryan Singer:** Right now it's centered, but very soon it becomes A-B testing.

**Ryan Singer:** Yeah, yeah, yeah.

**Ryan Singer:** You know, it's like once you get into the, you've fixed it, you've maintained everything.

**Ryan Singer:** Now it's about experimentation.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay.

**Ryan Singer:** So here's where, Here's where, here's where my head is going.

**Ryan Singer:** Ah, okay.

**Ryan Singer:** That's like the best kind of, it's like Fathom, there's so much to do, so much to do, so much opportunity.

**Ryan Singer:** Yeah, there's a lot here.

**Ryan Singer:** All right.

**Ryan Singer:** At a minimum, like, okay.

**Daniel Lopes:** Anyway, I'm just going to zoom out for a second.

**Daniel Lopes:** Like, um.

**Ryan Singer:** Yeah.

**Ryan Singer:** Here's, this is just my UX instinct speaking, and I don't even know how to explain it right yet.

**Ryan Singer:** When I see, like, filter by, what was it?

**Ryan Singer:** Is it even in the screenshot here?

**Ryan Singer:** No.

**Ryan Singer:** When we were looking at learn and improve, or no, we were looking at, where were we?

**Ryan Singer:** Yeah, learn and improve.

**Ryan Singer:** We were in learn and improve, but we were on page portfolio, and there was a smart filter, and it was kind of like, like, top performers, but like, something, what was it?

**Ryan Singer:** Yeah.

**Ryan Singer:** sharing.

**Ryan Singer:** I have, so we were in the portfolio.

**Ryan Singer:** Surging in almost top three.

**Ryan Singer:** Yeah, yeah, good.

**Ryan Singer:** Okay, okay, good.

**Ryan Singer:** Here, let me just take a, can you move your mouse away, and I'm going to take a screenshot of what we're looking at here.

**Ryan Singer:** I'm just going to capture this.

**Ryan Singer:** Boom.

**Ryan Singer:** Okay, that's exactly what I wanted.

**Ryan Singer:** I'm going to go back to the whiteboard.

**Ryan Singer:** Yep.

**Ryan Singer:** And I'm going to...

**Ryan Singer:** Make it data.

**Ryan Singer:** So, like, if this was, okay, let's replace this with our top, again, we're filtering the 710, right?

**Ryan Singer:** If there's any of these, we want to fix them first, right?

**Ryan Singer:** Yeah.

**Ryan Singer:** So what I want to see just naively is...

**Ryan Singer:** I think it's the...

**Ryan Singer:** Is this status, state, or something?

**Ryan Singer:** It's, yeah, so, like, I don't know what it is yet.

**Ryan Singer:** It's a kind of smart, not a smart filter, it's a smart status.

**Daniel Lopes:** Yeah.

**Ryan Singer:** The aggie or sort of, like...

**Daniel Lopes:** So this is, like, now, this isn't the right word, but what I want to say is realized, like, like, and realize, we're totally not going to say realize, nobody knows.

**Ryan Singer:** knows what that means.

**Daniel Lopes:** But what I want to say is like needs fixed now, like red alert, you know what I mean?

**Ryan Singer:** And then there's going to be, so let's say we've got three of those.

**Ryan Singer:** Now, if we knew that we had this to show anywhere on the page, we wouldn't even ask you to be filtering.

**Ryan Singer:** Like we would, we would just be like surfacing those, you know what I mean?

**Ryan Singer:** Like at the very, very, very top.

**Ryan Singer:** So what now, now that, that, that, that naturally jumps us to like a next step in the way of thinking about the UI here, which is like, if I'm just thinking about that, like I would be segmenting on the very top.

**Ryan Singer:** Again, I'm just thinking about the 712, right?

**Ryan Singer:** Red alerts, exactly.

**Ryan Singer:** Yeah, whatever it is.

**Ryan Singer:** Right.

**Ryan Singer:** But, you know, we know what I mean.

**Ryan Singer:** We have the reference there.

**Daniel Lopes:** I just wanted to.

**Ryan Singer:** Take anything that's a red alert, and I want to put it on the top, and you never have to touch a filter, because you should never not be seeing that.

**Ryan Singer:** Yeah.

**Ryan Singer:** Right?

**Ryan Singer:** Yeah.

**Ryan Singer:** then there's like, right?

**Ryan Singer:** And then there's like, there's a point, I don't know where the cutoff is.

**Ryan Singer:** There's a cutoff at some point where it's like, like, actually, I don't even like this.

**Ryan Singer:** I don't like the idea that there's ever like, now go dig yourself to figure out what to do.

**Ryan Singer:** Like, like, like, what is that?

**Ryan Singer:** Like, we, the whole point of being in the tool is that like, we're not asking you to do this.

**Ryan Singer:** So what I'm, what I'm kind of thinking is that like, we should actually have an opinion about what to float up here based on, on this like very specialized domain knowledge that we have.

**Ryan Singer:** Right?

**Ryan Singer:** So like, yeah, this is, um, these are pages that are working, are working, and fun.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Yeah.

**Ryan Singer:** Like, like right now, like, you know, and then there's going to be this next class, which is, actually, I'm going to call it a green alert.

**Ryan Singer:** Just because the idea here is like meaningful, unrealized opportunity.

**Ryan Singer:** Meaningful potential.

**Daniel Lopes:** Yeah.

**Ryan Singer:** Like, you know, and then, and then, and then, like, again, if I'm looking at the 712, or I'm looking at the 7,012, what I want to know is like, there's like 518 pages we think are useless.

**Ryan Singer:** Yeah.

**Ryan Singer:** And then, and then, then, like, what I want to do in here is like, um, um.

**Ryan Singer:** flashback.

**Ryan Singer:** bring up with

**Ryan Singer:** Uh, recycle or purge or whatever.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like, uh, uh, uh, whatever it is.

**Ryan Singer:** Like, um, this is the, this is that decision that we were talking about earlier.

**Ryan Singer:** So like what, what I'm getting at is that like the fundamental structure of, I think, learn and improve.

**Ryan Singer:** It's like, it's not a filter.

**Ryan Singer:** It's not an action.

**Ryan Singer:** It's, it's like, this is, this is, this is Marcel's brain that we are trying to turn into a heads up display.

**Ryan Singer:** Yeah.

**Ryan Singer:** It's like fix now, unrealized potential, dead zone.

**Ryan Singer:** All right.

**Ryan Singer:** Kind of thing.

**Ryan Singer:** Fix, fix now.

**Ryan Singer:** So unrealized potential, dead zone, dude.

**Daniel Lopes:** So this is like, I love these moments where like, I, like, I'm trying to like reflect Marcel's brain back at Marcel.

**Daniel Lopes:** And then Marcel is like, I'm going to put the perfect word on that thing because like, I know what that is.

**Ryan Singer:** And like, whenever that happens, those are, um, those are really.

**Ryan Singer:** Magical moments, because these words have a lot of power.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like, it's Marcel's voice.

**Ryan Singer:** And it's like, it's Marcel's voice tied to the domain model, tied to the data model, right?

**Ryan Singer:** So, like, when this UI becomes fix now, unrealized potential dead zone, it's like, dude, no app looks like this.

**Ryan Singer:** And it's so meaningful, right?

**Ryan Singer:** And now, it's kind of like, where my head goes is, like, I feel like there's work to be done on, like, okay, so what's the pipeline that these things go into, you know?

**Daniel Lopes:** You can always have, like, under the hood, like, go explore everything else, like your entire portfolio.

**Daniel Lopes:** But, like, if you lead with the portfolio, then it's just like, you're back at the same thing, which is an overwhelming sense of, like, I don't know.

**Daniel Lopes:** Exactly.

**Daniel Lopes:** And, like, the go digging is the least value, and the better you're doing.

**Ryan Singer:** At turning your brain into software, the less you should ever ask anybody to go digging.

**Ryan Singer:** It's almost like the, you know what I mean?

**Ryan Singer:** Like the kind of like dig and filter and explore mindset, I feel like is like the failure state that every other piece of software is in.

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like every piece, that's Google Analytics.

**Ryan Singer:** Like we don't know what you want.

**Ryan Singer:** We don't know what you want.

**Ryan Singer:** We don't know how to help you, but here's your data.

**Ryan Singer:** Right?

**Ryan Singer:** And like you guys are trying to be the exact opposite of that to the extreme of like, we know what you want.

**Ryan Singer:** We know how this works.

**Ryan Singer:** We have all the context.

**Ryan Singer:** The ideal state, to repeat it back to you, is like you should never need to apply a filter.

**Ryan Singer:** Yeah.

**Ryan Singer:** Exactly.

**Ryan Singer:** Like that's the ideal state.

**Ryan Singer:** The ideal state is like you have all the  context.

**Ryan Singer:** Like that's what LLMs are good at.

**Ryan Singer:** You have all the patterns.

**Ryan Singer:** We have all the data.

**Ryan Singer:** We have all the, you know, like the ideal state is like you should never have to prompt anything.

**Ryan Singer:** You should never have to apply a filter.

**Ryan Singer:** Right.

**Ryan Singer:** Yeah.

**Daniel Lopes:** So, um.

**Ryan Singer:** Yeah.

**Ryan Singer:** When we go into pipeline, already I feel a little more relaxed because I kind of feel like nailing pipeline is less important when you know when the thing that's in the pipeline has clear meaning.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So we talked about these as sections, fix now, unrealized potential dead zone.

**Ryan Singer:** I think when it comes to pipeline, what we can do is this is a page, okay?

**Daniel Lopes:** This is page number 512.

**Ryan Singer:** This particular page needs to be fixed now, right?

**Ryan Singer:** Fix now and then why?

**Ryan Singer:** High traffic, let's say, high performer in free fall or whatever.

**Ryan Singer:** Right.

**Ryan Singer:** Yeah.

**Ryan Singer:** And then there's like, so, so the things that I have taken on and clicked to somehow, so somehow these things have a, like a, you know, there's like a do action on each one of these.

**Ryan Singer:** Right.

**Ryan Singer:** And like, which is like put into my backlog or like take this on or assign it to me or I don't know.

**Ryan Singer:** Right.

**Ryan Singer:** Like accept this as work.

**Ryan Singer:** Yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Right.

**Ryan Singer:** So we need to have a state in each one of these of like, okay, if this is fixed now and this is like, we're screwed if we don't fix this, like is somebody on this?

**Ryan Singer:** Right.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** So like, that's the thing that we also don't see today.

**Ryan Singer:** Like, if this is truly this important, it's like, why am I even going to a backlog?

**Ryan Singer:** Do you know what I mean?

**Ryan Singer:** Like, like, I'm almost wondering if like, I want to see like.

**Ryan Singer:** This is totally not the right word, claim.

**Ryan Singer:** Do you know what mean?

**Ryan Singer:** What I want is like Jill is on it.

**Ryan Singer:** You know what I mean?

**Ryan Singer:** There's an assignment.

**Daniel Lopes:** It's almost like who's on the call and on fire.

**Daniel Lopes:** Exactly.

**Daniel Lopes:** Yeah, like who's on it, right?

**Daniel Lopes:** Because this is literally like this isn't work for later.

**Daniel Lopes:** This is like the fix now is the emergency room.

**Daniel Lopes:** So I need to know like where's the patient, where's the doctor, like what's going on, right?

**Daniel Lopes:** And if we express this urgency around like who is doing it and what is the state, it's very, again, like it's tying it all together like what this thing is.

**Daniel Lopes:** Now this, I think, it still makes sense.

**Daniel Lopes:** Just make sure I'm visualizing the same stuff as you.

**Daniel Lopes:** So what you have on the right side, those would be the cells of the table that you're seeing, the fix now.

**Daniel Lopes:** Yeah, sorry.

**Daniel Lopes:** So this is what I was, exactly what I was, I was.

**Daniel Lopes:** I was starting to think about these once they're in the pipeline, but it's the same thing everywhere, actually, right?

**Daniel Lopes:** Like as a row.

**Daniel Lopes:** So let's do that.

**Daniel Lopes:** Let's actually just like take this and put it here.

**Daniel Lopes:** I just one quick thing?

**Daniel Lopes:** was just writing this down.

**Daniel Lopes:** Can you zoom into fix now really quickly?

**Daniel Lopes:** Down here?

**Ryan Singer:** On the right side where you have like page 512.

**Ryan Singer:** Yes.

**Daniel Lopes:** And so in my mind, it's kind of like if you did fix now and you put a box around it and then you have high performer and you put another box around it and then you put another box in it, it's essentially like fix now versus like, you know, all the other actions.

**Daniel Lopes:** Then high performance, like high average,

**Daniel Lopes:** Performer or dead in the water.

**Ryan Singer:** then in free fall can be in free fall, likely to fall, decaying, stable, rising, or surging.

**Ryan Singer:** You know, like, does that make sense?

**Ryan Singer:** Like, and then like, like, we just, that's it, right?

**Ryan Singer:** Like, that's kind of it.

**Ryan Singer:** Like, all you should care about, like, everything else is details and backup.

**Ryan Singer:** Yeah, yeah, that's, that's, that's, I like, yeah, yeah.

**Ryan Singer:** Does that make sense?

**Ryan Singer:** I don't know.

**Ryan Singer:** I I was trying to write it down as we were talking.

**Ryan Singer:** So it's like, wait, hold on.

**Ryan Singer:** There might be something here to simplify the  out of this versus like 50 numbers everywhere in a table.

**Ryan Singer:** No, that's, that's, that's exactly, no, like, exactly.

**Ryan Singer:** So this, coming back to this, this is exactly what we shouldn't have to look at.

**Ryan Singer:** Like, I don't know what to do with this.

**Ryan Singer:** Like, this is like, power that, right?

**Ryan Singer:** This, this is, this is back in that Google Analytics thing of like, we don't know what you want.

**Daniel Lopes:** We don't know what you need.

**Ryan Singer:** So like, good luck.

**Ryan Singer:** Here's the data.

**Ryan Singer:** Yes.

**Ryan Singer:** Like, slightly more.

**Ryan Singer:** We're abstracted, but not actionable.

**Ryan Singer:** It's still assuming that you have the model of what matters and what am I looking for is in the head of the user.

**Daniel Lopes:** And this is just the data, and the user has to be the LLM.

**Ryan Singer:** So I think that's actually huge, which is, I think that's really huge to call that out, that it's not just about smart labels.

**Ryan Singer:** It's also about killing the numbers.

**Ryan Singer:** Now, okay, you can click through to this page, and we can show you numbers in the context of this problem, right?

**Ryan Singer:** So we can say, like, this is a high performer because, you know, and it's in free fall because, look, like, you know what I mean?

**Daniel Lopes:** Like, here's the, like, exactly what you, like, you know, like, here's the chart, you know what I mean?

**Daniel Lopes:** Like, like, like, this is why you're seeing this, but, but.

**Daniel Lopes:** But this is totally like, I don't even need this if I trust this.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah, because it's all relative, right?

**Daniel Lopes:** Like, you can put something at, like, $1,500 or whatever, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Mm-hmm, mm-hmm.

**Daniel Lopes:** Now, the place where I would say is that if I look at this in isolation, I want to have all these pieces.

**Daniel Lopes:** And if I'm, if we have a kind of a triage view, we probably subtract the things that are true for all of them.

**Daniel Lopes:** You know what I mean?

**Daniel Lopes:** Like, because these are all probably high performers if they're in FixNow.

**Daniel Lopes:** Yeah?

**Daniel Lopes:** Actually, it doesn't matter.

**Daniel Lopes:** They are, but it just doesn't matter because it's just, like...

**Daniel Lopes:** doesn't matter.

**Daniel Lopes:** You don't have to capture them.

**Daniel Lopes:** Like, free fall, it's still, like, free fall and likely to fall or decaying are, like, three negative things.

**Daniel Lopes:** free free free it's still,

**Daniel Lopes:** Right?

**Daniel Lopes:** And it's assuming most of these are high performer or, like, either way, like, the logic, as long as you put it in these, like, buckets, right, then you're, there's only three buckets of actions here, right?

**Daniel Lopes:** fix down, green alerts, dead zone.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Like, and that's kind of it.

**Daniel Lopes:** then, like, later on, you can go into the explore all and advanced mode and whatever the , you know, like, yeah, Marcel mode to just, like, go find new patterns.

**Daniel Lopes:** Yeah, that is, that is always my, my, my concern or, like, my, my, like, no, dude, but like, it's like, if we make it, like, too simplistic, yeah, but like, listen to this this morning, William is our best.

**Ryan Singer:** Yeah.

**Ryan Singer:** Okay?

**Ryan Singer:** William is our best.

**Ryan Singer:** On this call, on his pen desk, we did not have access to Google Search Console, and he.

**Ryan Singer:** He didn't even think of asking for it, and he didn't even look at the data before doing that entire content strategy that we're presenting today, like to an entire new client, and he's our best, like he's awesome, you know, but he didn't even cross his mind.

**Daniel Lopes:** It's like we have, folks that we have are extractions of existing marketing teams and product companies.

**Daniel Lopes:** It's not consulting people.

**Daniel Lopes:** That's how internal marketing is performing.

**Ryan Singer:** It's like the bar here.

**Ryan Singer:** It's not like engineering where there's like really good engineers out there.

**Ryan Singer:** It's just like the bar here is just like no one has mental models form because there's so many marketing channels and marketers.

**Ryan Singer:** I'm always trying to say, are we building like Photoshop where you have a learning curve, but once you crack it, you're like  awesome?

**Ryan Singer:** Or are we building like OS, Mac OS Preview, you know, and I think it's...

**Ryan Singer:** Dude, I'm 100% sure you're building Mac OS Preview.

**Daniel Lopes:** I'm 100% sure.

**Ryan Singer:** Because the only reason you can do...

**Ryan Singer:** The thing is nobody...

**Ryan Singer:** can do it.

**Ryan Singer:** Making preview in this market, in this vertical, requires you to be a genius because you have to be so good at figuring out how to actually automate the presentation.

**Ryan Singer:** It's too many signals.

**Ryan Singer:** That's what agents are for.

**Ryan Singer:** Agents are for abstracting that.

**Daniel Lopes:** And then your logic, your human judgment is where the place is leveraged, which is like some central place where the logic lives.

**Daniel Lopes:** Like aka like your plot.md or your equation.md or whatever the , right?

**Ryan Singer:** that's where we, like the human judgment can go.

**Ryan Singer:** Not on like looking at the table.

**Ryan Singer:** Exactly.

**Ryan Singer:** And the difference here is that like this isn't, these aren't generic statuses.

**Ryan Singer:** Like I think what we got to today was that these are highly, highly specific, meaningful statuses that map to specific actions.

**Ryan Singer:** That are domain specific.

**Ryan Singer:** So, like, Daniel, like, if these things were just saying urgent, like, I would be like, like, this is a toy, this isn't real, like, we should be showing the numbers instead, you know what I mean?

**Ryan Singer:** But, like, because it's actually saying, like, this specific, this is a signal detection.

**Daniel Lopes:** This is a specific signal detection, right?

**Daniel Lopes:** I would even think of this as a...

**Daniel Lopes:** You know what mean?

**Daniel Lopes:** like, you detect it like a malware.

**Daniel Lopes:** It's, like, in your network.

**Daniel Lopes:** It's just, like, go  fix it.

**Ryan Singer:** Like, drop everything you're doing.

**Ryan Singer:** Go , like, address it.

**Ryan Singer:** Yeah, this is almost like a security tool.

**Ryan Singer:** Yeah, it's a system.

**Ryan Singer:** It's really like a security tool.

**Ryan Singer:** It really is.

**Ryan Singer:** And it's funny, actually.

**Daniel Lopes:** I have a client who's a sophisticated security tool maker that's, like, with a very, very big footprint.

**Daniel Lopes:** And it's, like, so many similarities now that I think about it, you know?

**Daniel Lopes:** It's, like, they have, like, this deep, deep, deep expertise and tradecraft of, like, how hackers try to trick you.

**Daniel Lopes:** And then they have to translate those into, like, signals that get surfaced.

**Daniel Lopes:** And they literally, like, use all the same language and stuff like that.

**Daniel Lopes:** And it's, that's actually really interesting.

**Daniel Lopes:** Like, my first job was at securityintelligence.com building a site for IBM security.

**Daniel Lopes:** And the whole theme of the company is security intelligence because you have, like, app security versus, like, network security versus endpoint security versus, like, you know.

**Daniel Lopes:** And there's, like, all these, like, vectors that you have to protect.

**Daniel Lopes:** Anyways, there's a lot of parallels here.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So I think, I think this is not even a, we were originally talking about, like, smart status or something.

**Daniel Lopes:** I wouldn't even call this a status.

**Daniel Lopes:** This is actually, like, it's like a signal detection.

**Daniel Lopes:** And maybe, like, bringing into, like, what the guys are on the ground building today.

**Daniel Lopes:** I think this, like, what we are doing today, even if we build what we have on the left.

**Daniel Lopes:** Like, if we build, and we don't spend too much time on, like, making it look awesome or something.

**Daniel Lopes:** Like this, a redesign, like if the foundation is there for the right metrics, which all these things are on top of the right metrics, doing a facelift in March to create an optimization area that has all the things we talked about feels very doable.

**Daniel Lopes:** So it doesn't feel like this is like, I need to scrap everything that we have lined up for the next few weeks to go do this, you know?

**Ryan Singer:** I think it's, you already have the filters, and you're already going to build the logic.

**Daniel Lopes:** And it's going to create, it's going to create the view.

**Daniel Lopes:** And then like, I'll go on the right side, because the right side is the optimization one.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** On the next one.

**Daniel Lopes:** And for now, this cycle, we're focusing with the same area.

**Daniel Lopes:** Yeah, And then the optimization area, then we do this.

**Daniel Lopes:** And then for the optimization area, I think there is a quick Judo move here, which is like, where it says pages by pillar.

**Daniel Lopes:** It's like...

**Daniel Lopes:** Pages by, and then it would be like whatever those fields are or something, you know?

**Daniel Lopes:** Pages by signal?

**Daniel Lopes:** Yeah, pages by signal or something, you know, like, and then it's just like, and then each of these things that collapse are the fix now and the...

**Daniel Lopes:** Do you think we should still build a co-esterning system?

**Daniel Lopes:** Because that is a hard system to build.

**Daniel Lopes:** Like, that's what I wanted to ask about is how does this coexist with clustering?

**Daniel Lopes:** So keep in mind, like, there's almost never in, like, successful sites where it's one page type and that page type is just like, like, for instance, like even spend that 700 blogs, or sorry, 700 pages, 400 of those are blog, 60 of those are glossary, and the rest is whatever the .

**Ryan Singer:** And, but even within those 400 blogs, it's just like, it's not just blogs, it's just like, there's so...

**Ryan Singer:** How much nuances of like content type, intent, there's like topics, right?

**Ryan Singer:** And then some of those will be really important to them, right?

**Ryan Singer:** Like for instance, like compliance is really important because Spandask is in the UK, this is their main market.

**Daniel Lopes:** And so like all things, DPR, compliance, and things like that are there like edge over RAM and whatever, right?

**Daniel Lopes:** And so that's like a cluster or something that's just like has the lens of like being able to communicate something.

**Daniel Lopes:** Because it's really hard, like imagine you have these alerts and everything's perfect, right?

**Daniel Lopes:** But then imagine you have 500 pages and there's like 72 in red alerts and 230 in green alerts.

**Ryan Singer:** Like what the ?

**Ryan Singer:** Like I don't know what to do with this, but you know?

**Ryan Singer:** So this, what I'm hearing is, so the clustering is, well, of course, like the clustering, the function of clustering is to deal with too many results that are all kind of comparable to each other.

**Ryan Singer:** They're like, they're all similar to each other, right?

**Ryan Singer:** Exactly.

**Ryan Singer:** And like...

**Ryan Singer:** And so I think structurally what that means is that you need to nest the clustering inside of the signal category.

**Ryan Singer:** Exactly.

**Ryan Singer:** So within the mode of that category, like rather than the mode, you know, within that mode, you might need to stack some clusters.

**Daniel Lopes:** for a check that, would be like content type pricing versus review versus brand overview.

**Ryan Singer:** And then within that, would be a like category of page, like, you know, like ERP and finance versus like CRM versus marketing tools.

**Daniel Lopes:** And then that will give you the insight you were looking for for a check.

**Daniel Lopes:** So, but I think we should be, what that would mean, I just want to spell it out and make sure that it's clear.

**Daniel Lopes:** What that would mean is we would be repeating clusters, possibly.

**Daniel Lopes:** Yeah, yeah, yeah.

**Daniel Lopes:** And I think it's important to call that out as a feature, not a bug.

**Daniel Lopes:** Right.

**Daniel Lopes:** Angie's working, right?

**Daniel Lopes:** Like, pricing is driving most of the traffic on our site, right?

**Daniel Lopes:** But like, how do you know, why are some pricing pages rising and some are not?

**Daniel Lopes:** Why are some, right?

**Daniel Lopes:** Like, it's so hard to answer those questions, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Or even within the, like, red alert, potentially, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Good.

**Daniel Lopes:** Okay.

**Daniel Lopes:** So what I'm going to do then is I'm going to say, well, actually, all of this is changing.

**Daniel Lopes:** But the other thing I just want to call out is that we're actually, I think this is a bold and important move to consciously not do filters, you know?

**Daniel Lopes:** Even though there's a lot of smart ideas here because of the bigger macro structural win of taking this approach.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** I mean, it's literally, like, three workflows, and it's like, it's a classifier.

**Daniel Lopes:** it's it's it's it's it's it's

**Daniel Lopes:** And those are three fields in the table.

**Daniel Lopes:** Am I oversimplifying that?

**Daniel Lopes:** I think so.

**Daniel Lopes:** Because when you're dealing with 12,000 things, Yeah.

**Daniel Lopes:** But the only thing that I'm thinking is this, because I literally, like yesterday, I created all the linear tickets and the design, the mock-ups, so what I showed you is essentially all static views on the app, and the guys are starting to do the back end.

**Daniel Lopes:** So, By the way, the scoring will all be important.

**Daniel Lopes:** Because, like the scoring, Ryan, it's like, Yeah, so the two things that I think, I'm trying to figure out what is not part of the scope, what can I become the scope, because it's 14 areas, and it's just four engineers, including me there.

**Daniel Lopes:** So, a lot of the stuff, we're not going to make it.

**Daniel Lopes:** So, colostory is a big part, that's not easy to do.

**Daniel Lopes:** The smart views are not easy to do.

**Daniel Lopes:** So, again, with the smart views, colostory and IKID, I moved the backlog out of the learning approval area, or the creation of the industry.

**Daniel Lopes:** Removing smart news cuts this code.

**Daniel Lopes:** Collecting the data is too important.

**Daniel Lopes:** Showing the data doesn't matter that much, so we don't have to get that computer interface to the right.

**Daniel Lopes:** Sorting doesn't matter anymore.

**Daniel Lopes:** Infagination doesn't matter anymore.

**Daniel Lopes:** the infagination of 12,000 records with like time series stuff is  hard.

**Daniel Lopes:** So there's all these things that I can cut from this code.

**Daniel Lopes:** And then allows us to do that from the next cycle, right?

**Daniel Lopes:** yeah.

**Daniel Lopes:** Just know that like somewhere there, the new page opportunity, like where we're missing in week two of these engagements, is that like we have no view into their service area.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And so if we're giving them like a map of opportunities with like completely ignoring what their current service area is, it really puts those accounts at risk.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So understand your entire website is really important.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So it's like, it doesn't need to be this, but we need to have, I think, something to show their inventory of pages.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Or at least the overall health, you know, like even saying like, you know, but, um, yeah, okay.

**Daniel Lopes:** Well, okay.

**Daniel Lopes:** But I think we can wrestle with it a little bit and cut, cut, cut, then like see if like there's a way to kind of simplify the learn and improve.

**Daniel Lopes:** Because like, what were you thinking for learn and improve for this cycle?

**Daniel Lopes:** That user interface.

**Daniel Lopes:** yeah, sure.

**Daniel Lopes:** That's what I'm going to work today.

**Daniel Lopes:** I'm like, I haven't.

**Daniel Lopes:** Go as fast as I can on, on the first UI that we're showing.

**Daniel Lopes:** So like that changes it quite a bit.

**Daniel Lopes:** So.

**Daniel Lopes:** Okay.

**Daniel Lopes:** And so if we cut the filtering, you still have to do this, you still have to do all the scores, right?

**Daniel Lopes:** For everything.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And then all the three things here are essentially like what to do about the score.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Right.

**Daniel Lopes:** So it's like two layers in the strength.

**Daniel Lopes:** And then drawing that, and then the warm is the scores, which are kind of like indicators, that then have a ton of...

**Daniel Lopes:** It's more like it didn't change the underlying data model.

**Daniel Lopes:** It does change the amount of effort we would put on the user interface.

**Daniel Lopes:** I think we can have a flat table now with just clusters, not worry too much about sorting, pagination, that kind of stuff.

**Daniel Lopes:** And knowing that we're going to do a second pass to build like the intelligence layer that we mocked out there.

**Daniel Lopes:** And we might have to have a place to do what you're saying, just like see the whole inventory.

**Daniel Lopes:** So that is still basically the first screen.

**Daniel Lopes:** Is there a way to just have one of the three, like as a signal field?

**Daniel Lopes:** So that the default of the view is like filter bind?

**Daniel Lopes:** Um...

**Daniel Lopes:** Like I just don't want to spend like a whole week making that table perfect, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** It would be easy to do that.

**Daniel Lopes:** Like tables are hard to do.

**Daniel Lopes:** And if you're having a collapsible and all that stuff, that volume, you're going to be spending days on like fixing performance issues and scrolling browser behavior and sorting patterns.

**Ryan Singer:** Like if I don't do any of that and I just focus on collecting the data and getting the detail page right, it might come right after you finish this with the opinionated.

**Daniel Lopes:** Yeah, and also use the snapshots layer to cover up anything if needed.

**Daniel Lopes:** Snapshots?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Meaning like if you have a table that literally just had three fields or three columns, right?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** And they're all clustered and it's like it had no data in it whatsoever.

**Daniel Lopes:** if you click on it, you can see the full view, but like there's no aggregate reporting on anything.

**Daniel Lopes:** Like any needs for aggregate reporting, which you do eventually need like to say, hey, traffic is growing.

**Daniel Lopes:** know.

**Daniel Lopes:** Like, you know, that can be done in snapshots, is what I'm saying.

**Daniel Lopes:** in progress, snapshots.

**Daniel Lopes:** Yeah, progress, snapshots, that's what I'm saying.

**Daniel Lopes:** You know what mean?

**Ryan Singer:** So it's like, you don't, the table itself, I don't think, needs to carry, like, this crazy amount of data.

**Daniel Lopes:** Like, it doesn't need to look like, check that prompt table.

**Ryan Singer:** Yeah, yeah, yeah, yeah, yeah.

**Daniel Lopes:** Sorry, Ryan.

**Daniel Lopes:** No, it's good, because it means that we unblocked something when you guys suddenly talk a lot.

**Ryan Singer:** You know, I always take that as a positive sign, actually, you know.

**Ryan Singer:** Very, very good.

**Ryan Singer:** Mm-hmm.

**Ryan Singer:** Yeah, okay, good.

**Ryan Singer:** So much work, so much opportunity, so little time.

**Ryan Singer:** We need more agents working 24-7 around the clock while we sleep.

**Ryan Singer:** We need more Ryan time.

**Ryan Singer:** I know, more Ryan time.

**Ryan Singer:** How do we grab the next three, four tickets, you know?

**Ryan Singer:** It's like when you're in the, you know, in the grocery, you grab your ticket, you know?

**Ryan Singer:** It's just grappling.

**Daniel Lopes:** Like at the butcher.

**Ryan Singer:** Yeah, yeah.

**Ryan Singer:** Yeah.

**Ryan Singer:** Should we look at upcoming, I think we have one more schedule, right, Ryan?

**Ryan Singer:** No, this is the last one.

**Ryan Singer:** Yeah.

**Ryan Singer:** No.

**Ryan Singer:** How's your life, Ryan?

**Ryan Singer:** Yeah, you said you were going to, like, already kick off the last.

**Ryan Singer:** Yeah, it's interesting, you know.

**Ryan Singer:** So I'm just about to hopefully get, like, kind of a scope of work commitment and some signatures from, like, an integration partner on this big gnarly thing we're starting.

**Ryan Singer:** And we're doing, like, an AI integration at, like, a recruiting, like, an enterprise recruiting software service thing.

**Ryan Singer:** And it's, I'm not out of the woods, you know what I mean?

**Ryan Singer:** But, like, it's, like, we, we, we, I can draw it on a napkin now, you know?

**Daniel Lopes:** Yeah.

**Daniel Lopes:** So it's, like, it's, it's, it's, it's.

**Ryan Singer:** So it's feeling more tractable, but I still kind of can't tell, especially in the first few weeks, like how crazy it's going to be in terms of needing to do a lot of co-design with the integration partner, in which case, like, I have to, like, carve out time, like, you know, like my U.S.

**Ryan Singer:** overlap hours are going to get eaten up really fast.

**Daniel Lopes:** So I kind of cleared the deck to see what happens as we get rolling in the first, like, one or two weeks ahead.

**Daniel Lopes:** I actually have said no to all my upcoming, like, training, like, shaping sessions.

**Ryan Singer:** Like, so any of these, like, three-hour sessions that are not you guys, I, like, cleared out.

**Ryan Singer:** And the thing I have to determine is if I can, if I need to keep space for this one project, you know, to spill over the edges, or if I can start to picture something like, you know, every other week, a session like this or something like that, you know, it's kind of like.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Um, uh, I need to, the, my partner on this integration has been holding back on getting into full technical detail before they have a commitment signed.

**Daniel Lopes:** So there's a little bit of some chicken night going on there that we're working through, you know, so that's the current status here.

**Daniel Lopes:** Sounds good.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** Um, do, um, would it be helpful to try to even like super tentative?

**Daniel Lopes:** Like pencil in, or you prefer to just like not pencil in anything and follow up offline.

**Daniel Lopes:** Let's, let's, let's, let's take a moment and just talk through like what, um, what are the, uh, what kind of help do you feel that you need in the coming weeks?

**Daniel Lopes:** And like, what, um, you know what I mean?

**Daniel Lopes:** Like what, what sort of deadlines are coming to you?

**Daniel Lopes:** Just what's going on in terms of the urgency that you find yourself in specifically or like now, you know, like what are the things that you need me for?

**Daniel Lopes:** Yeah, like, from my perspective, like, there's this, like, I, for instance, like, on Check That, right, been juggling with this thing, and I probably spent already, like, 50 hours of my time trying to, like, sheet something and not get into these aha moments that we get two and three hours.

**Ryan Singer:** And it's often in the last, like, hour that they happen, right?

**Daniel Lopes:** And so it's, like, I'm adding a zero to how much time it's taking if I ever get there, right?

**Daniel Lopes:** And that's just, like, me personally, you know?

**Daniel Lopes:** And so, like, the thing is, like, if we were talking about one of our engineers, like, fine, whatever, right?

**Daniel Lopes:** But because it's, like, mine and Daniel's time, that zero of, like, three hours instead of 30 is, like, really  meaningful, like, consequential to, like, the company, because it can mean, like, months multiplied later, right?

**Daniel Lopes:** And so the leverage that you bring us is, like, extremely valuable.

**Daniel Lopes:** Like, would say, like, you know, at the highest, most important level, because it's like, there's no question of the opportunity and how big the opportunity is.

**Daniel Lopes:** There's no question of, like, the jobs to be done and how to do those jobs.

**Daniel Lopes:** It's all about, like, that into how the  we put this in market.

**Daniel Lopes:** It's all how to crack those nuts, you know?

**Ryan Singer:** Yeah.

**Ryan Singer:** And it's what you're the world-class best in the world at.

**Ryan Singer:** And, you know, and so, like, that's the help.

**Ryan Singer:** It's, like, truly, like, just show up, you know, kind of help.

**Ryan Singer:** That is one, but it's also, like, there are so many things, though.

**Ryan Singer:** Sorry.

**Daniel Lopes:** Like, that is one, like, but it doesn't have to be with us in the room as well.

**Daniel Lopes:** As in, like, if you don't have time with, like, U.S.

**Daniel Lopes:** overlap, I'm pretty sure that if you, like, if you get, like, Marcel's document that...

**Daniel Lopes:** He's struggling with on check that because this is just the area that we overlap and it's so critical that Marcel and I have to be in the room with you because this part of this isn't so important.

**Daniel Lopes:** Marcel is shaping one thing.

**Daniel Lopes:** I'm shaping some other thing on the framework.

**Daniel Lopes:** There's all these things happening at the same time.

**Daniel Lopes:** But on check that for the case that he's giving, if he just gives you all the things that he's been working on, I'm pretty sure.

**Daniel Lopes:** I'm pretty doubtful of that because what I noticed is that it's like Marcel just said.

**Daniel Lopes:** I usually, the first two hours is me like probing, probing, and probing.

**Daniel Lopes:** I agree with that.

**Daniel Lopes:** Not only absorbing, it's tacit knowledge that you guys have that I'm pulling out.

**Daniel Lopes:** So it wouldn't be in the document.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** But I believe you also have like an amazing, like that is on the product level.

**Daniel Lopes:** You also like, same really helpful on the UX and the practical side of things right there.

**Daniel Lopes:** Yeah.

**Daniel Lopes:** the screen as well.

**Ryan Singer:** But I almost think like, like.

**Ryan Singer:** Like, given how little time you have, like, this is like 10x multiplier, this is like a 10x multiplier, and we're aligning between us, so it's accomplishing multiple things at once, and it's like reducing rework later, which, like, and waste in 15.

**Ryan Singer:** Yeah, yeah, for sure, that's the most important.

**Ryan Singer:** So, it's like, if I only have three hours of your time once a month, I will take it.

**Ryan Singer:** I had two of those sessions, like, you know, three hours, you know, and maybe just like eight, 30 minutes a week, you know, just like respond to a couple of things, or, you know, just like a couple of questions, a couple of thoughts, like, you know, that would be, like, worth, you know, like anything.

**Ryan Singer:** And also, like, we would, like, personally, I would love to make sure you get equity as well, so that you're, you know, also motivated long-term, you know, because our value is just super low, man.

**Ryan Singer:** So, it's like, there's a lot of upside, you know.

**Ryan Singer:** I like that, yeah.

**Ryan Singer:** I, I, I.

**Ryan Singer:** I like that idea a lot.

**Ryan Singer:** So let's, yeah, next couple of weeks are tough.

**Ryan Singer:** Let me do this.

**Ryan Singer:** Yeah, next time we're busy too.

**Ryan Singer:** So we're doing all this stuff.

**Ryan Singer:** Yeah, basically what's going to happen is I'm going to have some time opening again after the 18th of March.

**Daniel Lopes:** Um, and before then it's like, unless something unlocks and I suddenly feel like I got to delegate a chunk of stuff that I thought I would have to like unstick myself, you know, and it can go either way with this, with this client project that I have.

**Ryan Singer:** Um, so let me do this.

**Ryan Singer:** Um, give me, um, I'll, I'll, give you, I'm going to set a deadline for myself for, um, for Wednesday, the 28th.

**Daniel Lopes:** May 5th, just next Wednesday, to get back to you with, like, you know, do I have any capacity in the coming weeks or not, you know?
