# GrowthX x Webflow — Marketplace App Strategy

<metadata>
date: 2025-10-15
time: 17:47 UTC
duration: 39 minutes
organizer: jason@growthx.ai
participants: Jason Gong, Tyler Pavlas, Kirat Chhina, Krish Penumarty, Aaron Resnick, Marcel Santilli
fathom_recording_id: 94419152
fathom_url: https://fathom.video/calls/442237506
share_url: https://fathom.video/share/qgEYzHw7Yj-k--zyzj6hr1wnDS-7QxV4
source: fathom
enriched_on: 2026-03-02 17:39 UTC
</metadata>

---

## Summary

GrowthX and Webflow discussed a potential marketplace app showcase project. GrowthX presented its end-to-end workflow capabilities for content and app generation, drawing parallels to recent projects like Ramp's vendor content and MCP server templates. The teams aligned on an 8-week strategy sprint ($30k) to develop approximately 20 curated app examples showcasing Webflow Cloud capabilities, with ongoing work streams potentially costing $15k/month. Webflow's public beta of the AI app generation feature is scheduled for late November, giving both teams flexibility to calibrate the partnership and deliverables around that launch.

---

## Context

Webflow is building two complementary app strategies: an AI-powered app generation product and Webflow Cloud, which integrates with GitHub for full-stack applications. Aaron Resnick (Product Manager) and Krish Penumarty (Engineering Manager for growth teams) lead Webflow's marketplace and developer ecosystem initiatives. GrowthX, founded by Marcel Santilli with early backing from Webflow investors including Rachel (angel investor) and conversations with Dan and Guy, has been collaborating with Webflow's developer content team through Jason Gong's growth initiatives. This meeting brought both teams together to explore creating a curated marketplace of app examples that demonstrate Webflow Cloud's capabilities to existing Webflow users building professional marketing sites extended with full-stack functionality.

---

## Relevance

**To GrowthX Delivery:**
- Marketplace template project demonstrates demand for end-to-end app development workflows, validating GrowthX's positioning as a last-mile execution partner
- ~20 app examples over 8 weeks ($30k sprint) with potential ongoing monthly work ($15k/month) establishes new SOW pattern for template/showcase work
- Project requires exposing GrowthX workflows as APIs and building reusable repos that can be transferred to Webflow, establishing repeatable asset model

**To CheckThat:**
- Webflow Cloud's GitHub integration and AI app generation feature suggest opportunities for CheckThat integration with developer tools; Webflow's AI features may benefit from AI visibility/prompt auditing
- Marketplace examples could showcase real-world LLM integrations and content generation patterns

**To GrowthX Business Development:**
- Strong partnership signals from Webflow leadership (investor connections, consideration of small investment, multiple teams engaged)
- Late November public beta deadline creates GTM urgency; flexible timeline allows GrowthX to scope initial 8-week sprint and demonstrate value before bigger commitments
- Reference potential with Webflow marketplace for case studies and future partnership extensions

---

## Overview

- GrowthX offers end-to-end workflow solutions for content/app generation, from strategy to execution
- Webflow aims to create a curated selection of app examples to showcase Webflow Cloud capabilities
- Potential 8-week sprint collaboration ($30k) to develop \~20 app examples, with ongoing work streams at $15k/month
- Timeline considerations: Webflow's public beta in late November, with GTM moment flexibility

---

## Key Topics

### GrowthX Capabilities Overview

  - End-to-end workflow solutions: strategy, execution, and last-mile implementation
  - Examples: Ramp's vendor category content, codelibrary.ai for MCP servers
  - Workflow-as-code with runtime layer and observability
  - Human interventions for quality control ("output bar raisers")

### Webflow's App Strategy

  - Two approaches: AI app gen product and Webflow Cloud (GitHub integration)
  - Focus on extending marketing sites with full-stack app functionality
  - Target audience: existing Webflow users building professional marketing sites

### Collaboration Potential

  - GrowthX can develop workflows exposed as APIs for Webflow
  - Possibility of building multiple repos for faster development
  - Mixture of AI-generated and manually built app examples
  - Emphasis on showcasing marketing site extensions with app functionality

### Project Scope and Timeline

  - 8-week strategy sprint ($30,000) for initial development and calibration
  - Goal: Launch within 8 weeks, pending internal approvals
  - Ongoing work streams at $15,000/month per stream
  - Flexibility in scaling based on volume and complexity requirements

### Example App Showcase

  - Similar to "Made in Webflow" but focused on web apps
  - Live examples of fully coded and deployed apps via Webflow Cloud
  - Inclusion of AI-generated apps with appropriate tagging

### Technical Considerations

  - GrowthX's workflows built in repos that can be transferred to Webflow
  - Upcoming open-source framework release (improved version of Langchain)
  - Emphasis on transparency and long-term ownership of developed solutions

---

---

## Action Items

**Jason Gong (GrowthX)**
- Prepare overview of current Webflow content work for potential extension into app templates project

**Marcel Santilli (GrowthX)**
- Share more detailed proposal for 8-week strategy sprint, incl. timeline, deliverables, and pricing

**Aaron Resnick (Webflow)**
- Follow up internally re approval process for GrowthX partnership on AI app gen templates
- Circle back with team re timelines for AI app gen project; determine feasibility of 8-week sprint proposal

**Kirat Chhina (Webflow)**
- Confirm exact date for late November public beta launch of AI app gen feature

---

## Transcript

**Marcel Santilli:** Hello, my good sir.

**Jason Gong:** Hey, how's it going?

**Marcel Santilli:** Not bad.

**Marcel Santilli:** I got my second screen set up over here, which then allows me to type in catalog.

**Marcel Santilli:** Is it a second fancy Apple monitor?

**Marcel Santilli:** It is a second fancy Apple monitor, Aaron.

**Marcel Santilli:** was just saying, so our co-founder CTO got me set up in VS Code and our local environment.

**Marcel Santilli:** It's in Cloud Code.

**Marcel Santilli:** And so I literally now have it like over here.

**Aaron Resnick:** Okay.

**Marcel Santilli:** And so like because the commands just take a while sometimes, it's just nice because I'm just like constantly at like, like just giving a little nudge like, and then in between meetings for one or two minutes before during the next meeting, I was just like, okay, let's do a bigger task over here.

**Marcel Santilli:** Go like, yeah, so this is like.

**Aaron Resnick:** That's the best feeling when things are just getting done for you in the background.

**Marcel Santilli:** And you're just like, great, told the AI to do it.

**Marcel Santilli:** There.

**Marcel Santilli:** I know, if only Slack worked like that, right?

**Marcel Santilli:** Yeah, just one day maybe we'll just be like, tell AI, generate $5 million, and then it'll just go do it.

**Marcel Santilli:** That'll be nice.

**Marcel Santilli:** Yeah, well, so good to connect.

**Marcel Santilli:** Appreciate you taking the time, and it would be awesome to just get, I think it's the first time you and I are interacting, it would be awesome to get a little quick intro, and then I'm happy to give you a context intro on our site as well, if you think would be helpful.

**Aaron Resnick:** Yeah, no, that'd be great.

**Aaron Resnick:** Yeah, so quick intro on my end.

**Aaron Resnick:** I'm a product manager here at Webflow.

**Aaron Resnick:** I've been at Webflow for about three years.

**Aaron Resnick:** I work closely with Kirat, who I think you've been kind of interacting with so far, and specifically, my team works on like the Webflow marketplace, which obviously ties in closely with kind of, you what we're talking about here.

**Aaron Resnick:** And then we work, I also work a lot with like our agencies and freelancers who use Webflow to build sites for clients, and like developers and stuff.

**Aaron Resnick:** And so just kind of

**Aaron Resnick:** Like our ecosystem of people who go out and kind of use Webflow and build with clients and contribute to the Webflow marketplace.

**Aaron Resnick:** That's kind of my focus area.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** That sounds like that.

**Marcel Santilli:** Oh, let me just accept.

**Aaron Resnick:** It looks like Krish has also joined me.

**Marcel Santilli:** All right.

**Marcel Santilli:** Here we go.

**Marcel Santilli:** So just give it another second.

**Marcel Santilli:** Hi, Krish.

**Marcel Santilli:** How's it going?

**Krish Penumarty:** Hey there.

**Marcel Santilli:** Good to see you.

**Marcel Santilli:** We were just doing a quick, quick intro.

**Krish Penumarty:** Do you want to do one really quickly as well, Garyon, before we do it on our side?

**Krish Penumarty:** Krish?

**Krish Penumarty:** Yeah.

**Krish Penumarty:** Yeah, sure.

**Krish Penumarty:** I can do like a quick two-second one.

**Krish Penumarty:** So my name is Krish.

**Krish Penumarty:** I am the engineering manager for our growth teams and SB6Ls team.

**Marcel Santilli:** So that's a team that Aaron leads the product side.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Amazing.

**Marcel Santilli:** Great.

**Marcel Santilli:** Great to connect.

**Marcel Santilli:** And CEO co-founder here, GrowthX, just a quick bit of context.

**Marcel Santilli:** We've been working with Webflow.

**Marcel Santilli:** And I'll let Jason introduce himself because he's been leading that.

**Marcel Santilli:** But we've been around for just over a year.

**Marcel Santilli:** And before that, I was CMO at what call Skill.ai and DeepRam.

**Marcel Santilli:** I was at Service Titan and HashiCorp, both went public as well, and then like growth and different things along the way.

**Marcel Santilli:** And I've been a fan, follower, and customer of Webflow probably like since the very early days.

**Marcel Santilli:** You know, I remember this one YouTube, wait, I think it was like almost 10 years ago.

**Marcel Santilli:** It was just like we're changing the whole web kind of thing moment.

**Marcel Santilli:** And so, you know, it's not a new thing or anything like that.

**Marcel Santilli:** Actually, I think you all are considering an investment in us off the record.

**Marcel Santilli:** It's a small track, but it's just like you guys do.

**Marcel Santilli:** Like we're talking to Dan and we've done a bunch of webinars with Guy as well and public events.

**Marcel Santilli:** And Rachel's been a friend and also a small angel investor in us as well.

**Marcel Santilli:** And anyway, so there's a lot of awesome, awesome connections.

**Marcel Santilli:** That's what...

**Marcel Santilli:** And a lot of love for Webflow, so I appreciate the partnership, yeah.

**Krish Penumarty:** Yeah, lot of good synergy.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Jason, you want to do a quick intro?

**Jason Gong:** Yeah, I'll do a quick one.

**Jason Gong:** I'm Jason, I lead growth and go-to-market here.

**Jason Gong:** So I work with some of our most important customers, you know, which is why I work with Webflow.

**Jason Gong:** I've been working mostly with Colin and kind of the developer side, and we're basically creating content more to like enable developers to be like aware of and also to be able to use Webflow.

**Jason Gong:** So like the whole slash integrations part of the website, that's us.

**Jason Gong:** We're about to kind of launch a few guides as well to get a lot deeper.

**Jason Gong:** I think it's been a really cool proving ground for like how kind of complicated can the content get?

**Jason Gong:** Because for the most part, for most of our clients, we'd be like, what are the top CRM tools?

**Jason Gong:** You know, but for you guys, we're actually referencing API docs and creating things that practically can be used to build.

**Jason Gong:** And I think it's been going really well.

**Jason Gong:** So, you know, the team over there is happy, which is...

**Jason Gong:** Yeah, I'm excited to see what else we can do for you.

**Aaron Resnick:** Yeah, that's awesome.

**Marcel Santilli:** Yeah, and like, I figure like a couple of things we could do, but Aaron, like, feel free to kind of like guide the context that would be most helpful for you.

**Marcel Santilli:** Happy to do a super quick, like, two, three minute TLTR, like, under the hood, what powers a lot of what we do, just in case it's helpful.

**Marcel Santilli:** I'm happy to do examples of things we've done that I think could be similar to what sounds like we were thinking about for templates, for Webflow, but also if there's any context you want to share initially before I dive into that, like, you know, just want to make this as useful as possible for you all, you know, yeah.

**Aaron Resnick:** Yeah, sounds good.

**Aaron Resnick:** I mean, yeah, I would say, like, having that context would be helpful, and also, yeah, maybe, like, any context I know, yeah, I don't so far, like, the conversations you've had with Kira, like, if they've mostly been over email or if you had a live combo, but I guess just any context I should be aware of, of kind of what you guys have already discussed or what you were kind of...

**Aaron Resnick:** proposing in those conversations with him.

**Aaron Resnick:** then the kind of like bullet points that I shared over via email, I just like pulled those into a note stock and attach that note stock to our calendar invite.

**Aaron Resnick:** So I think you should all have access to that, but I'll put the link in the Zoom chat.

**Aaron Resnick:** But yeah, like if we have time to just kind of run through some of those like more tactical questions and kind of just, yeah, understand those details, that would be great.

**Marcel Santilli:** But we can start with kind of some of that higher level context you were mentioning.

**Marcel Santilli:** Okay, perfect.

**Marcel Santilli:** So let me just quickly, I'll do like a super fast then TLDR, then we can kind of jump into some of these things around like the, the examples in and whatnot, right?

**Marcel Santilli:** Like, but maybe I'll start with like just a high level example of something we built for a customer that's, that's live.

**Marcel Santilli:** So this is ramps.

**Marcel Santilli:** So their vendor category is the fastest grown section of their site organically.

**Marcel Santilli:** And, and, and, also an LLM referrals as well.

**Marcel Santilli:** And so a lot of what we've done here is a combination of not just like you're playing content, but there's a lot of retrieval necessary to be able to kind of pull in data that they give us access to around like the spend, around the spender or category, describe that, but also then pull this into like a piece of content, right?

**Marcel Santilli:** Okay, fact check out into the section of site.

**Marcel Santilli:** And so for instance, like this for Airtable, then you can have like compare Airtable with competitors.

**Marcel Santilli:** And this is like, like essentially it ranks well for Airtable alternatives.

**Marcel Santilli:** And then over time, like you can do like Airtable versus Notion.

**Marcel Santilli:** And then now you're creating this whole like depth sequentially over all these things, right?

**Marcel Santilli:** Like, so we do the strategy, we do the workflow execution, and then we do last mile execution as well.

**Marcel Santilli:** And so we're building these workflows up.

**Marcel Santilli:** Show you over the hood, things like that.

**Marcel Santilli:** Maybe one other quick example here.

**Marcel Santilli:** There's a bunch more that are still looking at in progress.

**Marcel Santilli:** Well, it's more kind of like program deck, but this is a cool one that we built for ourselves just for fun.

**Marcel Santilli:** So it's called codelibrary.ai, and it's just like a directory of MCP servers.

**Marcel Santilli:** And so if you go here, essentially what it does is like it'll go to this URL, like, you know, and it'll ingest everything.

**Marcel Santilli:** I'd read me in originals, and it would generate this page and then have, like, the install, like, instructions.

**Marcel Santilli:** But hopefully this gives you, like, a little bit of an idea of, like, you know, we came up with the design and everything else, but then it also has things like cursor rules.

**Marcel Santilli:** And so, like, if you go into, like, cursor rules, the way to kind of think about it, it's just, like, a project that you have is kind of describing the stack of that project, right?

**Marcel Santilli:** Like, and it's really...

**Marcel Santilli:** The cool that this is, like, you can say, like, React, Z, Shed, Cn, for example.

**Marcel Santilli:** And then I can show you under the hood what we have that powers everything else is this workflow as code with a runtime layer and an observability.

**Aaron Resnick:** guys are product and engineering.

**Marcel Santilli:** figured weeks is okay.

**Marcel Santilli:** But just to give you an idea, like, the one that just triggered on that website, what it's doing is, like, analyzing a bunch of topics and conducting a bunch of research and whatnot.

**Marcel Santilli:** And what's really cool with this stuff is, like, everything is in code.

**Marcel Santilli:** So in this specific execution workflow, like, everything is in code.

**Marcel Santilli:** So, like, the prompts, the readmes, the APIs and tooling that it has access to, the 60 articles, the API, for example.

**Marcel Santilli:** So with this, I already completed, is, like, you can start, which is an input, like, that's a bad execution.

**Marcel Santilli:** And so what we do is like this one, for example, React Component Library, right?

**Marcel Santilli:** It would analyze a bunch of topics and then conduct research on that part of the stack, analyze the, you know, do research on the best practices for each part of it, you know, the tooling, the frameworks and things like that.

**Marcel Santilli:** Analyze the patterns and everything else and then generate the rules.

**Marcel Santilli:** And so then, and again, this is a very custom workflow, but you can see how this could be applied to any input, any research using any models, right?

**Marcel Santilli:** For any outputs.

**Marcel Santilli:** But then on top of that, then we have the human interventions, if you will.

**Marcel Santilli:** And I just realized that.

**Marcel Santilli:** And so then all of this kind of comes together in our platform internally that we call Atlas, that then we can do.

**Marcel Santilli:** We like, a lot of this stuff more programmatically, right?

**Marcel Santilli:** Like, so, let's see, let me do comparisons, for example.

**Marcel Santilli:** Like, so did you do a comparison, let's say, for Lovable here, we're doing Lovable for Souls, and it did, like, brief, only using, like, really, like, high-quality sources, and then directly an article added internal links added sources validated that we're writing a guideline, all the way to even fact-checking.

**Marcel Santilli:** So, like, things like FactChecker, for example, like, we're able to programmatically fact-check against either Knowledge Base or against anything on the web, and so it splits into Chunk, extracts the passages, and then researches each passage one by one, and then verifies one by one, and then if it finds anything that is incorrect, it will fix, like, this one, you know.

**Marcel Santilli:** Thank you.

**Marcel Santilli:** Here's what is stated, our credit-based pricing, and then here's the rewrite, and the rewrite might be hard to see, it's like, wow, credit card based on prompt complexity, not output size, versus it says credit charges for prompt or message, regardless of complexity or output size.

**Marcel Santilli:** So, correct is something very, very, very nuanced about the pricing model, you know, and so that's the level of thing that's powering, so that, like, when you see that output, it's not just throwing a bunch of humans at it, but then the humans can come here and edit along the way, right, and I like to call them output bar raisers.

**Marcel Santilli:** So, everything we're doing is a combination of context, knowledge, workflows, and then output bar raisers, all the way to the last mile, and getting it published, and we have, like, auto-publishing with Webflow, but we can also work with any database, things like that, you know, so.

**Marcel Santilli:** I know that was a lot, sorry, but I just wanted to catch you guys up to, hey, Kirat, sorry, I think you might have been on the waiting room for a little while.

**Kirat Chhina:** I apologize.

**Kirat Chhina:** These meetings that start at 45 minutes, they are sometimes so hard to just miss them.

**Kirat Chhina:** Hey, Jason, how are you doing?

**Jason Gong:** Hey, good going.

**Marcel Santilli:** Was that helpful?

**Aaron Resnick:** Yeah, no, that was definitely helpful.

**Aaron Resnick:** And I mean, yeah, it's really cool to see the end-to-end workflow and kind of how all that stuff is being generated.

**Aaron Resnick:** I am curious, like from the prior conversations that maybe you and Kirat had or, yeah, kind of prior discussions here, like, like, should I be thinking about this as, like, I know the examples we were just looking at are kind of more content-focused, more written materials.

**Aaron Resnick:** And then I know some of what we've been talking about, at least internally with Kirat and Kirat, is like these kind of app examples.

**Aaron Resnick:** Is that something that you guys have talked about before?

**Marcel Santilli:** Or how does that kind of fit in with sort of the workflow that you were sharing there?

**Marcel Santilli:** Yeah, so I can't share the work we've done for Lovable and Bold directly.

**Marcel Santilli:** But the way to kind of think about it is in addition to everything else, such as like the landing page, the enrichment of it.

**Marcel Santilli:** There's two main things we've done for them.

**Marcel Santilli:** One is they sent us session data around the prompts that people put in and a bunch of things.

**Marcel Santilli:** And we processed that session data with a workflow to just describe it in plain English and then used this narrative of what that session is.

**Marcel Santilli:** Like, hey, a person came in, they're trying to build this.

**Marcel Santilli:** They're building this for this reason, blah, blah, blah.

**Marcel Santilli:** They got stuck here.

**Marcel Santilli:** Then they went off and then they came back and did this, this, and this.

**Marcel Santilli:** This is like a mini essay of it.

**Marcel Santilli:** And then we used that to then categorize and create subcategories.

**Marcel Santilli:** And all these sessions then have, like, an outcome, right?

**Marcel Santilli:** Like, did they sign up for a pro plan or whatever?

**Marcel Santilli:** And then what we can do is just a very basic, like, correlation of, like, you know, which ones have a higher correlation to signing up for this thing.

**Marcel Santilli:** And then when you put them in a chart, it's, like, you see kind of, like, very clearly what the use cases are that you should go focus on.

**Marcel Santilli:** And then based on that, that informed how we came up with a strategy for their templates library for Bolt.

**Marcel Santilli:** For example, right, they ended up going UGC route, which is, you know, a way to start with lovable, what we're doing is they already have tens of thousands of like UGC templates and like, and it's so garbage.

**Marcel Santilli:** And so what we're doing for them is a combination of what I just described, but also a workflow that creates this one shot prompt, and then having a design engineer and the loop to do a final level of polish, and then publish that, plus all the workflows to make the page super.

**Marcel Santilli:** SEO friendly and things like that, you know.

**Marcel Santilli:** And so think of this as like a templates library, but then what we're producing is more of the starter kits that are really high quality to kind of seed the initial set of templates.

**Marcel Santilli:** And then I think for Webflow, like the benefit is like, you know, and what I think we would need to figure out is like, you have amazing marketplace level templates that are like already really good because they're marketplace.

**Marcel Santilli:** And so if people are trying to make money out of it, they have to be pretty good.

**Marcel Santilli:** You have this huge advantage over all these other tooling and, you know, but also like the description and things like that are not great, you know, or as optimized as they could be and as detailed as they could be.

**Marcel Santilli:** For instance, like all the different page types that are involved, like, you know, a deeper description and whatnot.

**Marcel Santilli:** So we can like analyze any source code or anything and kind of like improve that and enrich that or anything like that.

**Marcel Santilli:** But then the other piece is like, as you think about like mini apps, you know, like Retool just launched, you know, essentially one today, right?

**Marcel Santilli:** Like Airtable, it's either launched or you verbally mentioned like the CEO that that's what they're doing.

**Marcel Santilli:** You know, obviously you have like all the lovables of the world and everybody's kind of like sprinting towards that.

**Marcel Santilli:** And I think like Webflow has some advantages, but then like how can we continue to create these kind of like app-like experiences or templates and so there's a lot of different ways we could.

**Aaron Resnick:** I approach this, but I'll pause here, Krish.

**Marcel Santilli:** Yeah.

**Aaron Resnick:** No, that makes sense.

**Aaron Resnick:** mean, yeah, think, like, yeah, there's a lot of opportunities throughout, like, the whole marketplace to do a lot better job on what we're doing.

**Aaron Resnick:** Yeah, like, the stuff you're mentioning with templates and, like, adding more rich metadata and all that.

**Aaron Resnick:** I think, like, yeah, there's a lot to work through there for, like, this project.

**Aaron Resnick:** Basically, the, I think it would be probably similar to what you were describing with that sort of library of initial, like, trying to seed the marketplace with that grouping of templates.

**Aaron Resnick:** Because, yeah, originally, like, or eventually, we would make it a more UGC element where, like, people who are using our AI to, or using Webflow Cloud to, like, build apps and integrate them with their marketing sites, they could, you know, share those to the marketplace, like, if you're familiar with kind of made in Webflow and, like, where people can showcase those sites today.

**Aaron Resnick:** So, yeah, that would be kind of where it would go.

**Aaron Resnick:** But basically, we're trying to do right now is, like, do a more curated selection, just show what's possible.

**Aaron Resnick:** With app functionality in Webflow, kind of give people that inspiration and just seed the marketplace with those examples.

**Aaron Resnick:** yeah, I think trying to understand, like, what that looks like, I guess, with you guys of kind of like how, yeah, how many apps you have been generating when you've been working with other clients, like what the turnaround time looks like and stuff.

**Aaron Resnick:** Because we're trying to kind of fit it in with the broader, like, go-to-market planning that we're doing for some of this AI app gen stuff that we're launching.

**Marcel Santilli:** Yeah, and, like, all our workflows can be exposed as an API.

**Marcel Santilli:** And although we don't do that for pretty much any client today, like, we would be doing it with Webflow just because of the relationship and everything else, right?

**Marcel Santilli:** Like, and so we do have forward deploy AI engineers that can essentially build the workflows and test it to spec for anything.

**Marcel Santilli:** So, like, can say, hey, you need to do this, this, and this, and you need to backtrack this, and then you need to take a screenshot of this deployed, and then use the screenshot to do that X-Villa, like, we can kind of work together on that, you know?

**Marcel Santilli:** But it's like...

**Marcel Santilli:** I'm talking hours and days, not months and weeks, you know, here.

**Aaron Resnick:** And then that it's like kind of you guys are building like that backend type workflow that you're sharing, that you're mentioning.

**Aaron Resnick:** And then like we would be hooking into that workflow to try to generate these apps or I guess take me through like end to end kind of describing, right?

**Aaron Resnick:** Like, okay, let's say we share with you prompt data or we share with you insights on like these are kind of the categories of things that we want to show examples of.

**Aaron Resnick:** And then is it like you guys and your team would actually be kind of building out those apps that we would then showcase or it's like you would take that data and run it through some workflow or yeah, how does it ultimately like turn into it?

**Marcel Santilli:** Yeah, so for every client up to this point, we do end to end.

**Marcel Santilli:** So we do the strategy, we calibrate, we then come up with like a sample page, like what we're doing for Lovable, like we've five sample apps and websites for them.

**Marcel Santilli:** And we've then created the actual template that's like slash templates that's going to go live that has the, and we came up with the UX, we came up with the entire link.

**Marcel Santilli:** Like, filter strategy and everything else.

**Marcel Santilli:** We then develop all of that.

**Marcel Santilli:** And we've only been working with them for five weeks.

**Marcel Santilli:** So, like, all of us have been done in five weeks.

**Marcel Santilli:** We developed the workflows.

**Marcel Santilli:** And then initially what we're starting with, just to have the quality really high, is, like, a design engineer in the loop that the workflows generate an initial prompt.

**Marcel Santilli:** They prompt it and then they take it to the finish line.

**Marcel Santilli:** And our goal is to go from, like, three hours of the designer engineer review and polishing down to two, to one, to 30.

**Marcel Santilli:** So, it's, like, we never try to, like, do 1,000 first, right?

**Marcel Santilli:** Like, and then the next step is, like, by next week or the following, it's, like, launching that MVP experience and make sure it's getting indexed and things like that.

**Marcel Santilli:** And then, like, starting to crank out on the number of pages we're doing, all based on the strategy, based on competitive research and volume and things like that, right?

**Marcel Santilli:** Like, so that's, like, end-to-end that we do for most people.

**Marcel Santilli:** I think what's unique about Webflow in a lot of ways is just, like, it's, I don't think that we have the full understanding yet of, like, what.

**Marcel Santilli:** A prompt would look like, and, you know, just because with, like, lovable bold, and we can see that.

**Marcel Santilli:** So it probably looks a little bit more of what we're doing for Zapier, which is, like, their Workflows page, which is, like, they still have an API that you can use, or, like, a JSON.

**Marcel Santilli:** So for Vapi, for example, I don't think I showed this, like, this one is public, so I can show you, like, there's these use case pages that we built for them, and this is, like, a component that's a voice AI component, and what we've fed here is a JSON, in addition to customizing everything in this page, it's, like, a JSON config file that was generated using our Workflow, you know, and so that is, like, the prompt, the system prompt, and everything else.

**Krish Penumarty:** One second, one quick question, Marcel, for that, when you say you built that page, was that, like, a React-based app that you built, or, like, on top of their platform, or?

**Marcel Santilli:** So this page is a public page, so...

**Marcel Santilli:** It's just like, we did a pull request, we built the components, mostly using the design language.

**Marcel Santilli:** Like, we did the design, they approved the design, we built it into, you know, designing components.

**Marcel Santilli:** And then this specific part of the page is a component that we built.

**Marcel Santilli:** And then they just gave us the specs of, like, what the JSON file needed to look like based on their API, which publicly available.

**Marcel Santilli:** And then, like, this is the, what goes into this page is kind of like a JSON file that then, you know, feeds into this React component and then pings their API, you know, that is the voice assistant and how it works, right?

**Marcel Santilli:** So with Zapier's case, like, we're going to most likely, not live yet, but give them, like, a JSON because it's also, like, the tricky thing is, like, when an API is not available with Zapier, there's an API, there's a thing, it's working.

**Marcel Santilli:** Like, so it's just an API, we can work with an API, right?

**Marcel Santilli:** Input, output kind of thing.

**Marcel Santilli:** When there isn't an API, then we just need to understand.

**Marcel Santilli:** And that part better to understand what the input would be here and what the output would be.

**Aaron Resnick:** And I can certainly give you like a little bit of a visual of that because, yeah, I think our ideal outcome would be kind of closer to what you were describing with like, yeah, those like bolted, lovable, like live app examples versus kind of the more content stuff.

**Aaron Resnick:** So basically like we have two ways that you can like build web apps on Webflow.

**Aaron Resnick:** One being like our new AI app gen product, which we could get you guys access to, which is like essentially, yeah, you know, bolt lovable type thing, but also kind of bolt lovable inside of Webflow and like connect it also to your Webflow website.

**Aaron Resnick:** But yeah, so like a classic kind of webflow cloud, which is just that like you do the development, you know, in your own local machine, on your own repo, you push the code to GitHub, you connect that.

**Aaron Resnick:** GitHub repo to your Webflow site, and then it deploys it and hosts it alongside.

**Marcel Santilli:** So those are kind of like the two things I'm like smiling because I'm so excited because like off the record, I won't say, okay.

**Marcel Santilli:** So what a, hypothetically, a customer that we could work with that is very fast growing, it has a lot of love out there, does not have an ability to handle complex things.

**Marcel Santilli:** So we've tried the path of like essentially like using Cloud Code and other things to build an entire project and trying to import it into those things.

**Marcel Santilli:** And everything breaks if you try to build on top of that, like if you get a better prompt on top of that.

**Marcel Santilli:** So like if we're able to do what you just said, which is like have like a thousand repos that we build, like that opens up even more possibilities because we can move stupidly fast, you know, like it's just that that wasn't an option.

**Marcel Santilli:** But even if it's just a prompt, we can still do that as well.

**Aaron Resnick:** Okay.

**Aaron Resnick:** Yeah, I mean, I think we would be like definitely open to doing kind of a mixture where if we had, you know, like the way that I'm at least picturing it right now in my head is like basically the UI of made in Webflow.

**Aaron Resnick:** And again, we would improve this over time, but like for the initial thing, we're on a sort of a tight timeline.

**Aaron Resnick:** So picture like basically this page, but you know, instead the header is like, you know, amazing web apps or whatever, like built with Webflow.

**Aaron Resnick:** And it's like these live examples, but rather than just being a site, it'd be, you know, an app, like fully encoded and deployed via Webflow Cloud.

**Aaron Resnick:** Some, at least like some of them, we probably would want to be like built through this prompt experience.

**Aaron Resnick:** And then we would maybe have like a tag on them that says like built with AI app gen or whatever, so we can kind of market that like, you know, through this experience.

**Aaron Resnick:** Exactly.

**Aaron Resnick:** And so.

**Aaron Resnick:** so.

**Aaron Resnick:** Yeah, that's probably like how we would be thinking about it.

**Aaron Resnick:** And I guess like the other element to kind of factor in is that part of the unique kind of story for Webflow and part of what we kind of shared at Webflow conference when we were announcing this and kind of the way we're pitching it is that like, although you could come in here and just use this the same way you might use Levelable or whatever to just build an app, we are also kind of targeting it specifically right now at our core audience who's like using Webflow to build their professional marketing sites.

**Aaron Resnick:** And they might want to say like, okay, I have my marketing site, but I need to then extend it with some more full stack app functionality.

**Aaron Resnick:** So maybe I have my marketing site built in Webflow, but then if I click like log in, I want to take you to a logged in experience that's built with code.

**Aaron Resnick:** Or if I, you know, go to the pricing page, I want to have like more dynamic functionality there that has to be kind of built with code.

**Marcel Santilli:** And just an example, sorry to interrupt, but just so I don't forget, it's like for Brex right now.

**Marcel Santilli:** Like one of the things we're starting to build with them is like a tools library.

**Marcel Santilli:** So if you go to Mercury or if you search for like magic number calculator, right?

**Marcel Santilli:** Like which is a common use case.

**Marcel Santilli:** Like, and then Mercury has a one is like our content, but then instead of like a cover image or something, it's like actually little tools and calculator.

**Marcel Santilli:** They're like really like custom code, right?

**Marcel Santilli:** Like, so those media apps can be custom code, you with Webflow, like if you have a template where everything else is a template, but then a section or a component of the site is like custom code.

**Marcel Santilli:** And then in the apps, like you can pull that, like that would be like, that's super exciting.

**Aaron Resnick:** That's where, that's where, yeah, that's what we're doing.

**Aaron Resnick:** And yeah, it's like really opens up a ton of possibilities like you're talking about.

**Aaron Resnick:** And so, I mean, yeah, I think that's where we'd be trying to kind of understand from you guys.

**Aaron Resnick:** It's like, especially if we wanted to have those type of examples where, you know, it doesn't have to be like an extremely built out, marketing site, but to at least like.

**Aaron Resnick:** All that story of, like, hey, part of, you know, the example that we're showing is, like, here's your marketing site, and here's how, like, part of the marketing site is built with, is then, like, extended with code.

**Aaron Resnick:** I think those would be the ideal examples.

**Aaron Resnick:** But, yeah, I'm not sure, like, I know that would also then flow versus kind of more of the code-based app experience.

**Marcel Santilli:** I wasn't sure, like, what that was.

**Marcel Santilli:** Yeah, and so, like, the way we work with all these clients that I mentioned is, like, we start with a strategy sprint, and it's eight weeks, one time, $30,000.

**Marcel Santilli:** So it's, like, actually, like, a loss leader for us, technically, you know?

**Marcel Santilli:** And it's just because, like, we can have five more of these calls, and, like, we won't get to the level of granularity of, like, what we need to do.

**Marcel Santilli:** And so, like I said, like, with Lovable, like, we're getting to five, now we've done the slash guides for them, calibrated on the content strategy, but then we also built the entire templates library, and then we can scope out.

**Marcel Santilli:** And then in that process, like, we're working.

**Marcel Santilli:** This guy, Sebastian, who's like employee number eight and like templates is like his baby.

**Marcel Santilli:** And so he's like had all these different opinions that we had to work with and, you know, good opinions.

**Marcel Santilli:** But it's like, you know, like, so we're we're like, oh, shoot.

**Marcel Santilli:** OK, like, so the head of marketing CC was like, do this.

**Marcel Santilli:** And then like this person is like, no, no, wait, I care about this, this and this.

**Marcel Santilli:** And so it's like, you know, so that's kind of part of the process.

**Marcel Santilli:** That's just like a natural that it's impossible to capture in like a perfect scope doc, if you will, through these types of calls.

**Marcel Santilli:** Right.

**Marcel Santilli:** Like, and because we already have the relationship, like this could be a way for us to kind of like just get going fast.

**Marcel Santilli:** It's just like and also a way for us to because we're both about like six weeks out on kickoffs for new clients.

**Marcel Santilli:** And we'll find ways around that for Webflow.

**Marcel Santilli:** But like that way also allows us to just like put the capacity towards it, you know, because we don't have limited design engineers.

**Marcel Santilli:** And this is like a unique engagement that requires both AI engineers.

**Marcel Santilli:** We call AI engineers, but, you know, it's just like a full stack engineer that knows how to build workflows in our framework, you know.

**Marcel Santilli:** And then a design engineer, like for instance, George May, who I would put on this, was a very early employer, a framer, you know, and beautiful AI.

**Marcel Santilli:** And so like, he's like, but he's also a full stack engineer.

**Marcel Santilli:** So then like, he's like, it's just like, he can look at the full code, you know, and, but then also he can design things that are beautiful as well.

**Marcel Santilli:** And so like, it's a very unique talent.

**Aaron Resnick:** It's like not a role that's easy to hire for either, you know.

**Aaron Resnick:** Yeah, no, totally.

**Aaron Resnick:** Totally understand that.

**Aaron Resnick:** Yeah.

**Aaron Resnick:** And so I guess in your mind, like end to end, if we were to say, okay, you know, we're going get started tomorrow, we're going to spec out what we wanted to do, figure all that out, decide what apps we wanted to build, and then actually, yeah, build them and like have these live app examples.

**Aaron Resnick:** And let's say we wanted like, I don't know, 20 app examples or something like, what does that end to end timeline look like in your mind?

**Marcel Santilli:** Yeah, like, I, the, the things that slow things down are when people have no idea what they want.

**Marcel Santilli:** Right.

**Marcel Santilli:** And so the more a are when need be quiet they

**Marcel Santilli:** Where we can plug in can be defined in your case, because you already have the made in Webflow and you're okay with like copy and paste, you know, roughly, like that makes it a lot easier.

**Marcel Santilli:** What was tricky with, and again, like tricky, but like we're still week five and we're on track to launch it by week before week eight.

**Marcel Santilli:** And this is not the only thing we're doing for them.

**Marcel Santilli:** We're doing like two other work streams in parallel.

**Marcel Santilli:** Oh, okay.

**Marcel Santilli:** So was that they had no CMS, they have like no standard design language or UI or anything.

**Marcel Santilli:** And there's like four different sections of their site or their app experience that all look completely different.

**Marcel Santilli:** And then we were trying to guess and try to figure out who to talk to kind of thing, you know, so that really slows things down.

**Marcel Santilli:** But when you already have all of this, then we can focus on one, the strategy overall, because I'm assuming you want this thing to rank well and do well and people to find it, you know, and discover not only people coming through the front door of webflow.com, right?

**Marcel Santilli:** And then it's mostly calibrating around quality and then calibrating around like what the page content and experience should look like, you know, but.

**Marcel Santilli:** The experience is kind of like not set in stone, but it's like barely like mature.

**Marcel Santilli:** So then that would, like, I'm pretty confident, like we can launch something, you know, the short of like internal approvals, but if internal approvals are aligned, then like we can launch really quickly, you know.

**Marcel Santilli:** So I would try, like the goal would be within the eight week calibration or sprint, like you're doing end to end and publishing as quickly as possible, right?

**Marcel Santilli:** Like, and then that allows us to scope the ongoing of like, what is the ongoing look like based on the level of effort, the number of reviews, who has to be involved, how much, what is the volume that we're going for and things like that.

**Aaron Resnick:** Got it.

**Aaron Resnick:** And that design sprinter that you're talking about, or that like kind of eight week sprint, is that most, is that also including like building each of those individual app examples or it's more like setting the frame?

**Marcel Santilli:** Like we do end to end, like we don't, it's not like a nickel and dime kind of thing, you know, like it's, it's just mostly a way for us to like.

**Marcel Santilli:** And even while proving ourselves and scoping things out versus spending like six months in a contract, sales process kind of thing, and then not doing the work, you know, and then from there, like our work streams are like 15,000 per month for work stream, you know, like starting and then like the only things that would cause it to go like higher is if it's like, we need three design engineers in the loop and there's seven review process, like, you know, like, or if you're like, we want to go for 10,000, pages, like where the volume is really crazy, but we would be pretty transparent.

**Marcel Santilli:** like, hey, with a work stream, this is what you can expect as far as outputs weekly, you know, and then we would just crank on that.

**Aaron Resnick:** That makes sense.

**Aaron Resnick:** And I guess, Kirat, can you remind me, the, like, I know we talked about different dates on the Orion front of like, there was early November date, there was a late November date, and then, yeah, here's how you're looking at like timelines.

**Kirat Chhina:** Yeah, we have a public beta, I think late November.

**Kirat Chhina:** I think the link of the landing page is independent of the public beta, and so the GTM moment can also be independent.

**Kirat Chhina:** So we might want people to start coming in and spinning up stuff before we actually do a bigger splash around, hey, this landing page is there, and now you can go in and spin up all of this stuff.

**Kirat Chhina:** I think when we do the landing page, at that point of time, having some stuff, like not having a very dry, just a single prompt page, it'll be better to have something to go along with it.

**Kirat Chhina:** Yeah, that's one frame of it.

**Marcel Santilli:** Got it.

**Marcel Santilli:** Yeah, so we can do that, like, for sure, like, and this is an example, like what we're building for Lovable is way, way better, especially with a copy of, we've spent no time on the copy of these landing pages.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** You can see it's like a preview, right?

**Marcel Santilli:** Again, like, don't worry too much about the design and things like that.

**Marcel Santilli:** It's just like a quick thing.

**Marcel Santilli:** Then a description.

**Marcel Santilli:** In this case, the description focused a lot more on, like, how you could have replicated this prompt yourself.

**Marcel Santilli:** So it's more about teaching people how to prompt correctly, right?

**Marcel Santilli:** Like, quick tip when modifying the product or review, be specific about the problem.

**Marcel Santilli:** Your tool is all block, customizing the features, like, you know, throw on the prompt.

**Marcel Santilli:** And then this is the prompt that our workflow generated with no human intervention.

**Marcel Santilli:** And then if you click, like, start building, it would take you straight into the app and put this prompt into that app.

**Marcel Santilli:** Or in the case with, like, Levelpool, it's actually a remix experience.

**Marcel Santilli:** It's just that Bolt didn't have that availability to remix it as a feature built.

**Marcel Santilli:** But then there's also a preview that can be built, which is, like, pretty clean, you know?

**Marcel Santilli:** It's like, it's pretty cool.

**Marcel Santilli:** Pretty good.

**Marcel Santilli:** it's just like, you're trying to do a to-do app.

**Aaron Resnick:** I would much rather start with this than, you know, like a blank screen.

**Aaron Resnick:** Yeah, that's kind of the idea.

**Aaron Resnick:** makes sense.

**Aaron Resnick:** And yeah, that's similar.

**Aaron Resnick:** We are working towards like, yeah, one-click remix.

**Aaron Resnick:** But yeah, initially, we, yeah, we maybe go with the prompt, like copy prompt as the easiest way for people to remix it.

**Aaron Resnick:** But yeah, being able to show the live preview is really helpful.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Okay.

**Marcel Santilli:** By the way, like if, I don't know if you guys seen like 21st.dev.

**Marcel Santilli:** Yeah.

**Marcel Santilli:** But, but that's kind of like, ultimately, I think the, what an amazing experience looks like.

**Marcel Santilli:** But then even for that, they do a really  job of describing the components.

**Marcel Santilli:** There is no description.

**Marcel Santilli:** The same mistake V0 makes.

**Marcel Santilli:** And like, all these players are all making the same mistake.

**Marcel Santilli:** They're like, not describing the thing.

**Marcel Santilli:** So then users can't even find the thing.

**Marcel Santilli:** Like, like, like, what, if you go to Mobin or something like that, I don't know if you can use that, but it's like, it's like, then because.

**Marcel Santilli:** It's a paid service.

**Marcel Santilli:** They do a really good job with, like, the discoverability, right?

**Marcel Santilli:** So that's the idea is, like, building something that's closer to this, but, like, actually publicly available so that you don't have to actually sign up and whatnot if you're looking for a table, right?

**Marcel Santilli:** This is just screenshots.

**Marcel Santilli:** I can't modify this.

**Marcel Santilli:** This is about, like, public, you know, webs and things like that.

**Marcel Santilli:** But, you know, and it doesn't have the description or whatnot.

**Marcel Santilli:** But, like, if you could remix this, this would be amazing, you know?

**Marcel Santilli:** So that's kind of the idea.

**Marcel Santilli:** But anyways, hopefully this gives, I got to run, unfortunately, but hopefully this gives you all, like, a lot of what is possible.

**Marcel Santilli:** And then, like, I think it's a, like I said, like, no pressure on our end.

**Marcel Santilli:** It's mostly, like, we love working with Webflow and, like, anything you can do to be helpful for game.

**Marcel Santilli:** And it's just, like, we're kind of already getting a lot of these types of requests for different news cases.

**Marcel Santilli:** And so this is definitely something that we can do.

**Marcel Santilli:** And then on the engineering side, maybe once.

**Marcel Santilli:** want talk like,

**Marcel Santilli:** I that would like also help is the fact that everything we're building in Workflows is in a repo that can be yours.

**Marcel Santilli:** And then we're about a month away from open sourcing our framework, which is think of it as like a link graph on steroids.

**Marcel Santilli:** Like it's a better version than Mastra.

**Marcel Santilli:** You know, it's way better because it has like a bunch of things kind of bolted in, including evals in the loop and a bunch of other things.

**Marcel Santilli:** So like the way that the cool thing about it is like over time, this thing can be like essentially take it with you.

**Marcel Santilli:** essentially later on.

**Marcel Santilli:** So it's not like a black box that you have no idea what happened over here over time.

**Aaron Resnick:** Nice.

**Aaron Resnick:** That's awesome.

**Aaron Resnick:** Well, yeah, no, I know we're over time.

**Aaron Resnick:** So, yeah, I know you got to jump, but really appreciate it.

**Aaron Resnick:** was super helpful to chat with you.

**Aaron Resnick:** And yeah, we'll definitely like circle back on our end, figure out also like timelines and everything like that.

**Marcel Santilli:** And then I guess be in touch via email.

**Marcel Santilli:** I think we also have a Slack channel with you guys.

**Marcel Santilli:** this Slack is the best.

**Marcel Santilli:** We're all there.

**Marcel Santilli:** I suck with email of this by having 50 tools and two EAs, you know.

**Aaron Resnick:** Me too.

**Aaron Resnick:** Me too.

**Aaron Resnick:** Okay, cool.

**Marcel Santilli:** Then we'll be in touch over Slack.

**Marcel Santilli:** Sounds good.

**Marcel Santilli:** Thanks, Dean.

**Marcel Santilli:** Great chatting.

**Marcel Santilli:** appreciate it.

**Marcel Santilli:** Talk soon.
