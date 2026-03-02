# GrowthX <> Zapier - Use Case Analysis

<metadata>
date: 2025-10-07
time: 20:00 UTC
duration: 42 minutes
organizer: Tyler Pavlas (GrowthX)
participants: Tyler Pavlas (GrowthX), Kirkland Gee (GrowthX), Danny Schreiber (Zapier), Janine Anderson (Zapier), Danielle Lapierre (Zapier), Steven Schweibold (Zapier)
fathom_recording_id: 92525900
fathom_url: https://fathom.video/calls/432275903
share_url: https://fathom.video/share/NFRgxB3sqzy8cubKgnxpVxV-nqb4vjBv
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Zapier explored a partnership to refresh Zapier's existing 500k-600k templates, with a focus on improving field mapping, specificity, and overall template quality rather than building net new templates. The Zapier team — Danny Schreiber, Danielle Lapierre, and Steven Schweibold (Team Sprout, templates and growth) — outlined two potential paths: optimizing the legacy template library using Zapier's Payload CMS and API, or building templates for Zapier's upcoming AI Agents platform. GrowthX will need programmatic access to template data and a testing/validation framework to work at scale, with Zapier to provision CMS accounts and API credentials after the call.

---

## Context

Zapier is exploring a partnership with GrowthX to solve a critical problem: they have 500k-600k templates auto-generated from customer usage data, but these templates lack depth, specificity, field mapping, and SEO optimization. This was the impetus for the connection — Zapier needs a partner with content strategy and AI workflow expertise to make these existing templates "opinionated," specific, and user-friendly. Tyler brought Kirkland (GrowthX engineer with AI automation and SEO background, formerly at ClickUp) into the conversation to assess technical feasibility. The Zapier team — Danny (Growth), Danielle (Templates/Product), and Steven (Engineering Manager, Team Sprout) — represent Zapier's templates strategy, which is pivoting from two-step Zaps to richer, more complex workflows. The timing is strategic: Zapier is also launching an AI Agents platform in GA and wants to build a template library for that as well, giving GrowthX two potential engagement models.

---

## Relevance

**To GrowthX Delivery:**
- **Content + SEO at scale:** Two engagement paths — refresh 500k-600k existing templates or build AI Agents templates. Both require systematic content strategy, field mapping optimization, and SEO-friendly naming/structure that aligns with GrowthX's core offering.
- **Programmatic template creation:** Kirkland flagged implementation complexity. Zapier's Payload CMS and internal API enable programmatic updates, but no testing framework exists yet for rich templates (roadmap Q4/Q1). This is a constraint GrowthX needs to work around.
- **AI integration opportunity:** Steven mentioned potential to add AI analysis to templates (e.g., analyzing form submissions before Slack notifications). CheckThat/AI expertise could differentiate the partnership.

**To GrowthX Business Development:**
- **Partner validation:** Zapier's ZapConnect (35-40+ attendees) shows market interest in templates. Success here builds a reference case and positions GrowthX as a template strategy partner for other integration platforms.
- **Expansion potential:** If the refresh engagement works, Zapier's Agents platform launch (GA) opens a second contract or SOW to build an entirely new template library — higher-value engagement.
- **Strategic fit:** Kirkland's ClickUp background + Zapier's SEO visibility strategy alignment suggests natural account expansion opportunity.

**To CheckThat:**
- **Integration platform data:** Zapier is a massive integration hub. Their template usage patterns, app connections, and user workflows could feed CheckThat's AI visibility indexing and competitive benchmarking.
- **Prompt optimization:** Steven flagged that prompts don't come through in legacy templates. GrowthX's ability to audit and improve LLM prompts in AI-enabled templates aligns with CheckThat's strengths.

---

## Overview

- **Primary engagement:** Refresh 500k-600k existing legacy templates generated from customer data (via Databricks), focusing on specificity, field mapping, and opinionated design to improve user activation (currently 2% to 40% depending on template complexity)
- **Launch with quick wins:** Start with copy/content updates on high-traffic existing templates; test verticalized variants (hypothesis: 5% baseline conversion can improve to 40%); then move to field mapping optimization
- **Secondary opportunity:** AI by Zapier templates — expand two-step templates into three-step workflows with meaningful AI steps; templates are currently under-distributed and under-performing
- **Pilot approach:** Multiple narrowly-scoped test batches (copy, field mapping, workflow structure) to establish baselines and measure impact before scaling
- **Technical foundation:** Zapier will provision CMS (Payload) accounts and API access; validation workflow available via API calls for programmatic template management

---

## Key Topics

### Current Template Landscape

  - Zapier has 500k-600k templates auto-generated from customer data via Databricks (partner onboarding patterns captured in first 2-4 weeks of new partner usage)
  - Legacy templates have weak URLs (randomized strings, not SEO-friendly), lack depth, specificity, field mapping, and AI integration
  - Schema stability varies: Zap templates use well-tested, years-old schema; canvas/Agent templates have complex layout/positioning variables (5+ products per canvas)
  - Two primary types: **Legacy Zap templates** (human-created, 2000+ total, refreshed by GrowthX as primary use case) and **AI by Zapier templates** (newer, limited distribution, mostly two-step when should be three-step with meaningful AI step)

### Proposed Workflow for Template Optimization

  - **Data access:** Fetch template data through Zapier's API; pull into dataset for manipulation or push changes back via API
  - **CMS workflow:** Use Zapier's self-hosted Payload CMS to make contributions; Zapier reviews and publishes (not GrowthX directly)
  - **Validation:** API schema validation available (deterministic for Zap templates, complex for canvas templates with positioning)
  - **Sync back:** Changes can sync back to Databricks data team if refreshing rather than creating net-new templates

### Performance Baselines & Test Methodology

  - **Current activation rates:** Range from 2% (complex CRMs, many custom fields) to 40% (simple apps like Google Sheets, forms); baseline on existing templates varies by complexity
  - **Success metric for pilot:** Verticalized template variants: test 10 variants of a baseline template to see if 5% baseline converts to 40% with specificity
  - **Traffic-first approach:** Measure sign-ups (page impressions → "Try It" clicks → activation), prioritize high-traffic existing templates for improvement before building long-tail variants
  - **Test batches:** Isolate copy/content improvements, field mapping improvements, workflow structure improvements to identify highest-ROI changes

### AI by Zapier & Next-Gen Opportunity

  - **Problem:** Most AI by Zapier templates are two-step (incomplete), generated in 2023, lack use case narrative, underperforming
  - **Solution:** Build three-step workflows (trigger, AI step via Zapier's native AI capability, action) with strong use case framing and modern distribution
  - **Secondary engagement:** Could be post-pilot second contract, but agents platform GA timing makes this a future opportunity vs. immediate priority

### Technical Constraints & Roadmap

  - **Canvas template limitation:** No testing framework yet for rich canvas templates (Zapier's roadmap: Q4/Q1); GrowthX to focus on Zap templates first where validation is straightforward
  - **LLM positioning problem:** AI-generated canvas templates struggle with XY positioning of elements; simpler to remix fields within known-good template layouts
  - **API capabilities:** Fetch, query, manipulate, validate, push back all available; scale validation via API calls (no manual UI work needed)

---

## Action Items

**Danielle Lapierre (Zapier)**
- Send breakdown of Zapier template types to Tyler (follow-up to cover template type options, custom fields, and moderation process)

**Steven Schweibold (Zapier)**
- Provision CMS (Payload) accounts for GrowthX team to access and edit templates programmatically
- Provide GrowthX access to internal API documentation for app fields, triggers, and actions data

---

## Transcript
**Tyler Pavlas:** Hello, sir.

**Tyler Pavlas:** This meeting is being recorded.

**Kirkland Gee:** Hey, what's up?

**Tyler Pavlas:** Nothing much.

**Tyler Pavlas:** Excited to dig into this Zapier use case today.

**Kirkland Gee:** Yeah, I think it should be good.

**Kirkland Gee:** Sorry, just wrapping up some things.

**Tyler Pavlas:** And I realize I might not have sent you that doc that says, like, problem statement for growthx before, but that has some more context that might be helpful as they're talking through.

**Tyler Pavlas:** I'm going to get them to, like, explain what the different types of templates are in more detail and what they're looking for.

**Tyler Pavlas:** But there's a tab called, like, template capabilities that also goes in more detail.

**Tyler Pavlas:** So you might just want to, like, take a look at that as they're given more information.

**Kirkland Gee:** Yep, makes sense.

**Tyler Pavlas:** All right, I'll bring them in.

**Tyler Pavlas:** Hey, Zapier team.

**Tyler Pavlas:** What's going on, Danny, Janine?

**Danny Schreiber:** Hey, Tyler.

**Danny Schreiber:** Good to see you again.

**Tyler Pavlas:** Yeah, likewise.

**Tyler Pavlas:** How did ZapConnect go a couple weeks ago?

**Danny Schreiber:** I think it went best we could have hoped.

**Danny Schreiber:** And this year, we had a couple new goals that also went well for us.

**Danny Schreiber:** So, yeah.

**Danny Schreiber:** Thanks for asking.

**Tyler Pavlas:** Yeah, for sure.

**Tyler Pavlas:** How many, like, people register for something like that, out of curiosity?

**Danny Schreiber:** Oh, yes, actually.

**Danny Schreiber:** Daniella, Janine, do you know from your, from marketing?

**Danny Schreiber:** I know it was, I'd say, 35, 40 plus.

**Danny Schreiber:** Okay.

**Janine Anderson:** That feels great.

**Tyler Pavlas:** Go ahead, Janine.

**Tyler Pavlas:** That'll, that'll be the, that'll be the, that'll be the number.

**Tyler Pavlas:** That we'll try to hit for an event one day where we'll know we truly made it if we can ever get close to that.

**Tyler Pavlas:** But that's awesome.

**Tyler Pavlas:** I'd love to let Kirkland give a quick intro.

**Tyler Pavlas:** Kirkland is an engineer on our team that has been taking a look at your use case.

**Tyler Pavlas:** And so we'll be able to cover quite a bit of ground today after we align on some of the specifics up front.

**Tyler Pavlas:** So Kirkland, let you give a quick hello.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** Super excited to meet you guys.

**Kirkland Gee:** Again, my name is Kirkland.

**Kirkland Gee:** I do 100 different things at GrowthX, but primarily AI workflow automation stuff, mostly on the client side of things.

**Kirkland Gee:** Before this, I was actually at ClickUp doing very similar things.

**Kirkland Gee:** So I've studied Zapier's SEO strategy quite a lot at the time there, funnily enough.

**Danny Schreiber:** Yeah, yeah.

**Kirkland Gee:** So was generally familiar with the template library already when Tyler brought it up to me.

**Kirkland Gee:** So I think I have somewhat of a sense of what we're trying to do, but I think it would be good to just talk through a lot of the details because there's a lot of just like different ways this could go in terms of implementation.

**Kirkland Gee:** But

**Kirkland Gee:** Yeah, excited to talk through that with you guys.

**Danny Schreiber:** Yeah, I'm aware of ClickUp as well with its SEO strategy of late, well, late, like the last four or five years.

**Danny Schreiber:** Yeah, yeah, It's been cool.

**Kirkland Gee:** Jeremy, the director of SEO there, is awesome.

**Kirkland Gee:** Like, really, really great guy.

**Danny Schreiber:** Okay.

**Kirkland Gee:** So.

**Danny Schreiber:** Very cool.

**Danny Schreiber:** And we've got Steven joining us.

**Danny Schreiber:** I think a quick intro from Steven would be helpful.

**Steven Schweibold:** Yeah.

**Steven Schweibold:** So, Steven Schweibold, engineering manager here at Zapier.

**Steven Schweibold:** I oversee Team Sprout, which is our templates team, and recently just stepping up into engineering leadership role within the growth zone.

**Steven Schweibold:** So, working with Danny a lot more.

**Steven Schweibold:** And, yeah, excited to talk about this potential collaboration.

**Tyler Pavlas:** Perfect.

**Tyler Pavlas:** Now that we all know each other, to dive in.

**Tyler Pavlas:** I know that what you're looking to us for is programmatically creating these templates, right?

**Tyler Pavlas:** Like, optimizing them for SEO, driving, user activation.

**Tyler Pavlas:** What I was hoping to get a little more clarity around, probably Danielle, is there's a lot of different types of templates.

**Tyler Pavlas:** And I know that there's like 500 templates that I've seen on SEMrush if I like search slash templates on Zapier.

**Tyler Pavlas:** So maybe you could just like give a quick overview for us of like which types you want us to focus on, the number of templates you'd expect us to be creating, and then what you'd actually want on the template page itself.

**Tyler Pavlas:** And then we can dive deeper with Kirkland on more of the technical feasibility.

**Danielle Lapierre:** Yeah, sounds good.

**Danielle Lapierre:** And I just realized I owe you a breakdown of our template type.

**Danielle Lapierre:** So I'll get that to you right after this call.

**Danielle Lapierre:** But if you head to zapier.com slash templates, those are kind of the latest and greatest templates.

**Danielle Lapierre:** And that's where we're leaning into future forward.

**Danielle Lapierre:** I'm just pulling it up here, but.

**Tyler Pavlas:** Yeah, and maybe share your screen too, if helpful.

**Danielle Lapierre:** I think that could help here, yeah.

**Danielle Lapierre:** Thank Yes.

**Danielle Lapierre:** Sounds good.

**Danielle Lapierre:** Okay, so these are our latest and greatest templates.

**Danielle Lapierre:** The JSON files that I sent you are all this type of template.

**Danielle Lapierre:** And things to note here, field mapping works, prompts come through.

**Danielle Lapierre:** They can have as few as one zap, one table, you know, like just one asset, or they can be on a canvas and have 13 zap, seven tables, you know, the sky's the limit.

**Danielle Lapierre:** I mean, processing time is the limit, but, you know, within reason.

**Danielle Lapierre:** So that's what, like, template type we would be looking at.

**Danielle Lapierre:** I guess we connected after we spoke last week and had a bit of a frank conversation about feasibility and what the best approach is.

**Danielle Lapierre:** And we can chat through numbers, but the TLDR of that conversation was, from a systems standpoint, we're not quite there yet internally to have you building, like, something with tables and something with canvas.

**Danielle Lapierre:** And so we're wondering if there's numbers.

**Danielle Lapierre:** Opportunity to actually take some of the templates that we have already built and make them more opinionated, like put in field mapping where it doesn't exist, you know, like, I'll see if I can find an example, actually, that might be helpful, but we have this genre of template that I just shared with you, but there's another genre that were created using customer data to an extent, but are not opinionated.

**Danielle Lapierre:** They're kind of like empty and bare and you use them and the prompt doesn't come through.

**Danielle Lapierre:** That is, oh my goodness, sorry, I'm getting the Octo run around here.

**Steven Schweibold:** I sent, Danielle, I sent in chat, I've read these note takers spin up a new chat window.

**Steven Schweibold:** So I sent it to everyone.

**Steven Schweibold:** So effectively, we have, what Danielle's talking about is we have around 500,000 600,000 templates that are all, that have all been generated off of customer data.

**Steven Schweibold:** So this is practical example.

**Steven Schweibold:** And oftentimes these are pretty mechanical in nature in terms of like content structure.

**Steven Schweibold:** It's not very inspiring.

**Steven Schweibold:** If you link to what I have in Zoom chat here, Danielle.

**Steven Schweibold:** Yeah.

**Danielle Lapierre:** There's no link there.

**Kirkland Gee:** Oh, wait.

**Danielle Lapierre:** There it is.

**Danielle Lapierre:** That was weird.

**Steven Schweibold:** Yeah, it's the...

**Kirkland Gee:** They have different tabs for chatting with like the note taker and everybody in the room.

**Kirkland Gee:** It gets out of hand.

**Danielle Lapierre:** It's awful.

**Steven Schweibold:** No.

**Steven Schweibold:** So yeah, do you want to run through this, Danielle?

**Steven Schweibold:** don't mean to step over you.

**Danielle Lapierre:** No, no, please.

**Danielle Lapierre:** Thanks for jumping in.

**Danielle Lapierre:** Thanks for finding one.

**Danielle Lapierre:** This is going to take a minute to load, but punchline is if I was to go and connect my account here, everything is just empty and sad and not opinionated.

**Danielle Lapierre:** And we know that these do the best when they're very clearly for someone or something.

**Danielle Lapierre:** They solve a really painful problem.

**Danielle Lapierre:** You know, like two steps, a hundred steps, it doesn't matter.

**Danielle Lapierre:** It's about the cost of my property.

**Danielle Lapierre:** property.

**Danielle Lapierre:** problem it solves.

**Danielle Lapierre:** Steven, over to you.

**Steven Schweibold:** Yeah, so we have, you know, we have a lot of these templates.

**Steven Schweibold:** First of all, you can kind of tell the URL, not great.

**Steven Schweibold:** It's some sort of, you know, randomized, you know, string.

**Steven Schweibold:** That's how, you know, mechanically under the hood, we're sort of surfacing, surfacing uses through this, you know, very ID looking slug, you know, despite the URL structure not being necessarily SEO friendly, you'll also notice that the content lacks a lot of depth.

**Steven Schweibold:** Frankly, these templates come from our data team.

**Steven Schweibold:** And when it comes to building out a content strategy around all these different use cases that folks are using within our, within our systems, they're not really the most robust in terms of, in terms of content, in terms of specificity, which Danielle mentioned, which is even, you know, sort of tilting...

**Steven Schweibold:** tilting...

**Steven Schweibold:** Put a little bit these templates on their head and having field mapping applied to them where there's specificity in their application as it pertains to this one specifically, which is like, you know, notified team in Slack when a customer submits a support form in HubSpot.

**Steven Schweibold:** like, it'd be great if there was specificity in the message text, or you even went a step further and added AI, for instance, to do some analysis on a form submission.

**Steven Schweibold:** So kind of peeling back the layers here a little bit, they're currently today with the rich templates that we have in the logged out template space, there is not a solid, there's actually, frankly, no testing framework for you to actually scale the creation of these templates on your side.

**Steven Schweibold:** So you're going to go through, you're going to have a really painful time of like, creating the JSON, testing it, submitting it.

**Steven Schweibold:** Validating it.

**Steven Schweibold:** We just don't have that mechanically there.

**Steven Schweibold:** That's on our roadmap as a zone within Q4 and Q1 is to actually shore that up.

**Steven Schweibold:** In the meantime, though, we have this vast array of different mechanical templates that we could evaluate and spruce up from a content standpoint, from a template structure standpoint, using your systems, because there is a pretty robust process to test and validate changes to these.

**Steven Schweibold:** Alternatively, we also evaluated, we have our agents platform, and this is where we get a little bit into the marketing side of things, or like our go-to-market strategy for that platform.

**Steven Schweibold:** But that's going to be going into GA release.

**Steven Schweibold:** And we do have templates that are specified to our agents platform that does have a testing framework that we could build out a robust templates library for using leveraging new folks.

**Steven Schweibold:** And so there's documentation to create those as well.

**Steven Schweibold:** And so I wanted to also call out that's another potential opportunity for engagement.

**Steven Schweibold:** is along our agents platform.

**Steven Schweibold:** And yes, thank you for linking those, Danielle, but you can see those agents templates there.

**Steven Schweibold:** And there is a creator pool that we have internally to produce templates for this agents platform.

**Steven Schweibold:** And like I said, it's another area where we could potentially engage, but either evaluating and taking a look at and making more robust the Zap templates that we have or these agents templates, I feel like is our best course of action to make sure that you all aren't getting left with something where you have very little support structurally and for us getting the most value out of your work.

**Steven Schweibold:** So that's where I'm kind of landing on things.

**Tyler Pavlas:** Quick confirmation questions.

**Tyler Pavlas:** With the Zap templates, would you be looking for us to create net new or just refresh among the 500,000 to 600,000 that you mentioned?

**Steven Schweibold:** What we could probably do is, is we could probably take the pool that's there.

**Steven Schweibold:** It's really, this is where I lean into your expertise.

**Steven Schweibold:** We could take the available pullets there, remix, produce net new, test validate whether these have on their own merits resonance with our customers, which maybe arguably would be the best path because we wouldn't be polluting the existing space of templates that are there.

**Steven Schweibold:** Instead, you know, create a net new fresh thing that we could then go and merchandise.

**Steven Schweibold:** Or alternatively, we could remix what's there too, but we would have to probably ultimately work with our data team just to make sure that any changes that you all make gets synced back up into that service.

**Steven Schweibold:** But we already have the plumbing in place for that.

**Kirkland Gee:** Just a logistics question for these templates in different areas, like where does the content or the data for those templates live?

**Kirkland Gee:** It doesn't have any sort of CMS, right?

**Steven Schweibold:** Is it all just...

**Kirkland Gee:** There is actually.

**Steven Schweibold:** Okay, so you all could operate against the CMS.

**Steven Schweibold:** Everything's stored in what?

**Steven Schweibold:** doesn't

**Steven Schweibold:** It's Payload.

**Steven Schweibold:** I don't know if you're familiar with that service.

**Steven Schweibold:** It's a self-hosted CMS.

**Kirkland Gee:** Actually, Figma just acquired them.

**Kirkland Gee:** Ah, okay.

**Steven Schweibold:** But anyway, so we have a self-hosted Payload CMS for all templates data, including agents templates, by the way.

**Steven Schweibold:** And what you all would do is you can work within that system to submit contributions, and we could go through and make the necessary steps to go and publish those.

**Steven Schweibold:** Because the templates that we're talking about that are these Zap templates, the data originates from Databricks, but does get stored into our template service.

**Steven Schweibold:** Our service is the source of truth, but the way that those get produced is through Databricks and all of the customer data, and that gets fed in through their prompts that then generate those templates.

**Steven Schweibold:** And so it was more or less an experimentation, and so...

**Steven Schweibold:** Really an experiment, I should say, within our own data set.

**Steven Schweibold:** So I feel like it's the perfect opportunity to remix what's there and provide a fresh new perspective on things.

**Kirkland Gee:** Yeah, I would think the first place to start is just like see like where what performance looks like across those.

**Kirkland Gee:** I mean, with that many, I'm sure there are some that are literally doing nothing that like more or less don't exist in the eyes of customers.

**Kirkland Gee:** And like starting there, either changing them a little bit or adding content to them.

**Kirkland Gee:** And then to your point, like kind of taking a few different angles, right?

**Kirkland Gee:** And like trying some different things to see what works.

**Kirkland Gee:** But that's a pretty big library.

**Kirkland Gee:** I wouldn't just start with throwing more at it, right?

**Kirkland Gee:** I think it makes sense to start with what's there.

**Kirkland Gee:** And then logistically, would you be thinking that like, would it be, sorry, I'm just like processing or repeating back.

**Kirkland Gee:** So the zap templates, we would be able to change the actual content of those templates and validate that that change is valid before we try to.

**Kirkland Gee:** Republish, like, because I was thinking that's like what we're saying is one of the big issues with these larger canvas templates, right?

**Kirkland Gee:** It's like validating that, say, the JSON file we've created is actually usable.

**Kirkland Gee:** We can do that sort of thing with these other kinds of templates.

**Steven Schweibold:** Yes, there's the validation steps for you to go in and make a change and verify that it works.

**Steven Schweibold:** It's a much more straightforward process than those larger canvas templates.

**Kirkland Gee:** Yes.

**Kirkland Gee:** And with that validation, you say go in, make a change.

**Kirkland Gee:** Does that have to happen with, like, me in the UI of Payload, or could we validate through some sort of API call?

**Kirkland Gee:** Because obviously, if we're trying to do this at scale, right, like we want to be able to not have to have someone manually go in.

**Steven Schweibold:** So we do have an API that you can go and you can fetch these materials from, and you can go query however much you want.

**Steven Schweibold:** And then you can pull that down either into a data set that you can then go and manipulate, or you can just continue to leverage the API.

**Steven Schweibold:** And then you can push them back up and do a validation step.

**Steven Schweibold:** Zapier, just to make sure that at least the schema is correct.

**Steven Schweibold:** And it's a lot more deterministic with Zap templates specifically than it is with system templates.

**Steven Schweibold:** Because there's a lot more variables at play when you consider up to five products versus just workflow.

**Danielle Lapierre:** Yeah.

**Danielle Lapierre:** And also positioning on a canvas.

**Danielle Lapierre:** Like, things go out the window when you're trying to make things look pretty, where, and the schema is a lot older, too.

**Danielle Lapierre:** Like, the zaps have been tested for years.

**Kirkland Gee:** That's, like, trying to get an LLM to do XY positioning on all those elements sounds pretty much impossible.

**Kirkland Gee:** Like, maybe not entirely, but, like, a huge problem to solve.

**Kirkland Gee:** Versus just, like, hey, here are the available workflow tools you can call.

**Kirkland Gee:** Here are the available, like, parameters, something like that.

**Kirkland Gee:** Or, like, another thing I'm thinking about is, okay, we have 100 example templates that are known good.

**Kirkland Gee:** And then we just go.

**Kirkland Gee:** Going and change the fields, right?

**Kirkland Gee:** Like here's the prompt we want for what the form is going to say, or here's how we want to format the Slack message, but you actually get 100, 500 templates out of one sort of workflow layout, if that makes sense, just more specialized for particular use cases.

**Kirkland Gee:** Again, I'm just trying to think of ways to like simplify and remove the potential for hallucination or just like random craziness that might happen when you try to do this at scale.

**Kirkland Gee:** But I think that all makes sense.

**Kirkland Gee:** Also, Danny, was just looking at what this other AI by Zapier thing that you threw in was.

**Danny Schreiber:** Yeah, we can talk about that.

**Kirkland Gee:** think, Janine, you had a comment on it.

**Janine Anderson:** I used to say like, I think another piece of what we should probably consider when we're looking at this, especially for like a pilot phase, is making sure that we are going to be able to get these distributed to people and get signal on whether or not they're valuable.

**Janine Anderson:** So if we're producing a whole bunch of things that are going to be super long tail, we're not going to get the signal we need in terms of what.

**Janine Anderson:** They're not there functioning the way we want for either acquisition or use case discovery because there just won't be enough users interacting with them.

**Janine Anderson:** Whereas if we're able to look at, in some ways, generating new copy, whatever we're looking at for pages for ones that we already know are getting traffic, but maybe aren't performing the way we want them to.

**Janine Anderson:** So maybe they're not getting as much traffic because some of the content on the pages is so thin.

**Janine Anderson:** There's other ones where, like, we've maybe got, like, these AI by Zapier ones where we know that there are use cases that are valuable, but we just don't have the templates made yet.

**Janine Anderson:** I think we could come up with a couple different, just, like, batches of template types that might work for us to play with during a pilot phase that would give us the ability to go across a few of these, like, problem spaces, even with the limited template types we can work with right now.

**Kirkland Gee:** Yeah, I think that makes sense.

**Kirkland Gee:** And, like, you know, if we're talking about, like, ease of getting started, like, changing copy on a...

**Kirkland Gee:** Page is, like, the easiest thing, right?

**Kirkland Gee:** We can do that for pretty much anything, anywhere, and hopefully, like, make a difference at scale pretty quickly.

**Kirkland Gee:** It's just when you start talking about, like, changing fundamentally how the templates are designed, that introduces a layer of complexity that I don't think is at all, like, impossible.

**Kirkland Gee:** It's just a matter of, like, what do we want to prioritize over a certain time period, right?

**Kirkland Gee:** And maybe we save that for after we've proven out that even changing copy on a page is going to do something, right?

**Janine Anderson:** Yeah, I think it's also, like, if we're struggling to get field mapping working correctly on all of these, like, that's another, like, I like it when we can come up with sort of narrowly defined tests.

**Janine Anderson:** So if we can decide, like, improved copy on these pages for things that have enough traffic right now and usage now, we can, like, establish that and then have another batch where, like, okay, we want to improve the field mapping.

**Janine Anderson:** We want, like, we're just discreetly identified the things we want to, like, want to test so that we can do all of it as, like, some group of that as quickly as possible and figure out what's going

**Kirkland Gee:** Do you have, see, you mentioned, like, you know, not, like, if we say, if we went super wide on use cases, not getting enough signal, do you have, like, a threshold for what, like, if you launched a new page or a new batch of pages, like, is there a way that you can think about measuring performance that's important for us to understand?

**Janine Anderson:** Danielle, do you have, I mean, I know what I think about when I think about content launching, and I know what I've looked at when I've helped evaluate, like, template launches, but I don't know how we've been thinking about that more specifically for these types of templates.

**Janine Anderson:** I mean, I generally feel like the things that are going to be important for us are going to be sign-up rates, the number of qualified sign-ups we're getting from things, and whether or not they're able to turn on that specific Zap.

**Janine Anderson:** So if a lot of people start, like, click into a template, and then, I mean, our normal, like, I don't know what our activation rate, it varies so wildly, like, we've got some Zaps that people are activating 40% of

**Janine Anderson:** Time they try it.

**Kirkland Gee:** And then there's other ones where it's like 2%.

**Janine Anderson:** So it's really like, I'd want to make sure that we're looking at like, what is an, if we're looking at existing things that we're changing, whether it's the workflow itself or just the copy, I'd want to make sure that we had something where we had enough of an established baseline to be able to determine whether what we're doing is improving there.

**Janine Anderson:** And I think the more complicated the Zap is, the more complicated the apps are, like CRMs are notoriously tricky because there's so many fields and it's often so custom versus like Google Sheets and a form.

**Janine Anderson:** That's way more straightforward.

**Kirkland Gee:** Yep.

**Kirkland Gee:** No, that'll make it.

**Kirkland Gee:** I only ask because, you know, when I think about, you actually go ahead, Danielle, I'm still processing that thought.

**Danielle Lapierre:** No, you're good.

**Danielle Lapierre:** I'm trying to pull up a report, but it's going to take me a minute to find it.

**Danielle Lapierre:** We, of that bank of like fabricated ones, AI generated ones, we have obviously the baseline metrics on them.

**Danielle Lapierre:** And this.

**Danielle Lapierre:** One the things I'd be really interested in moving is, one, can we just increase the number of people who are landing on them?

**Danielle Lapierre:** So theoretically, it's valuable.

**Danielle Lapierre:** It's showing up in important places.

**Danielle Lapierre:** Like, that number goes up week over week.

**Danielle Lapierre:** Two is, can we increase the number of people who are clicking try it?

**Danielle Lapierre:** Like, content's valuable, it's pages resonating, whatever.

**Danielle Lapierre:** And then the final would be like, okay, are people actually using it, turning it on?

**Danielle Lapierre:** And I would want to see volume on those going up.

**Danielle Lapierre:** But, I mean, some tests we can run against them would even just be like, okay, we have the baseline of 5% conversion rate, and it's, you know, not verticalized, like it's not specific.

**Danielle Lapierre:** Can we create 10 variants of those?

**Danielle Lapierre:** And like, do those 10 variants have a conversion rate of 40%?

**Danielle Lapierre:** Or do they have a conversion rate of 5%?

**Danielle Lapierre:** And if they still have that 5% conversion, then like, probably not worth verticalizing others.

**Danielle Lapierre:** So I think there's a bunch of tests that we can do to see how we can move the needle, given that initial data set.

**Kirkland Gee:** Yeah, that all makes sense to me.

**Tyler Pavlas:** It sounds like refresh, like the legacy templates is the first experiment or use or work stream.

**Tyler Pavlas:** And then the second, correct me if I'm wrong, would it be creating new agent templates?

**Tyler Pavlas:** Okay.

**Tyler Pavlas:** And then, yeah, go ahead, Danny.

**Danny Schreiber:** I'm hesitant to, I think that agent templates work can sort of sit as a potential, though the AI use cases and thinking about AI by Zapier, which is really an area that we have an opportunity to grow exposure to, specifically top funnel.

**Danny Schreiber:** So, much of what you're looking at here was actually generated with our current, and it exists today, we have a current AI generated Zapier.

**Danny Schreiber:** And so in terms of scale, this is run by our partner team, the ecosystem team that does all the integrations.

**Danny Schreiber:** And the reason they put this together back in 2023 was because when a new user, when a new partner comes on, one of the highest friction points was that partner actually creating Zap templates.

**Danny Schreiber:** So they took the first two to four weeks of usage within Zapier and then spun up these templates.

**Danny Schreiber:** But what happens though is we end up putting out a lot of templates, but there's not a strong use case or story around these templates.

**Danny Schreiber:** And so that's why for something like AI by Zapier, which is generally part of a three-step flow at least, we're still getting two-step templates here.

**Danny Schreiber:** In reality, two-step templates for this kind of work are meaningless.

**Danny Schreiber:** So like, here's one of our best performing steps, not really an integration per se, it's a capability of Zapier.

**Danny Schreiber:** It's the default way to add AI to it.

**Danny Schreiber:** Workflow that isn't going in and using some LLM, but it's basically ready to go within Zapier.

**Danny Schreiber:** But the way we're distributing it is just outdated.

**Danny Schreiber:** very much matches how we used to do this.

**Danny Schreiber:** And so this is taking an old playbook.

**Danny Schreiber:** I think the opportunity here is what does it look like for the growthx version?

**Danny Schreiber:** And even though this version that I was creating in 2023 is pretty rudimentary and doesn't get updated, you can see that it's thanks to this, sign-ups on these Zap templates.

**Danny Schreiber:** And we talk about Zap templates.

**Danny Schreiber:** They're not like our shining star anymore because their impact goes down for a number of reasons.

**Danny Schreiber:** But you can see here that it's about a third.

**Danny Schreiber:** And when they started, though, back in 2023, it slowly grew percentage points.

**Danny Schreiber:** But now it's a double-digit percentage point, so we're all.

**Danny Schreiber:** The first three stacks are all legacy versions of templates.

**Danny Schreiber:** That were created by humans, we say, or, you know, the first few thousand.

**Danny Schreiber:** But if you actually get into the numbers, or excuse me, the templates themselves, here we go.

**Danny Schreiber:** You can start to look at something like a very common one, send emails through Gmail, probably like when a new thing is added.

**Danny Schreiber:** What they did here, from my understanding, is they ended up, what we're talking about, refreshing this template.

**Danny Schreiber:** It took ownership of this template through the AI-generated approach.

**Danny Schreiber:** So, you know, I think a version of this looks like, growthx, we take a better go at this, and ultimately, it could be something that we scale into, to, you know, this is a catalog of Zap templates that, you know, were created with two-plus-year-old process.

**Danny Schreiber:** Like, one of the questions here is, can we do this better?

**Danny Schreiber:** And this is what we have available today.

**Danny Schreiber:** I think when we talk about...

**Danny Schreiber:** about...

**Danny Schreiber:** What we could work on today versus the JSON work that we're talking about.

**Danielle Lapierre:** Danielle, yeah, go ahead.

**Danielle Lapierre:** To support CSL templates on the app directory, we would have to do some work.

**Danielle Lapierre:** That's the work stream that we chatted about with Maria.

**Danielle Lapierre:** So to have the data templates pull in.

**Danny Schreiber:** I think so.

**Danny Schreiber:** have to trade.

**Danny Schreiber:** So specifically, yes, you mean here?

**Danielle Lapierre:** Yeah, so this is pulling from Snapbook, and we would need to shift it to pull from the templates API, which we should do anyways.

**Danielle Lapierre:** But just to clarify, we don't necessarily get it for free with growthx.

**Steven Schweibold:** True.

**Steven Schweibold:** Yeah, that works relatively teed up and simple to integrate.

**Tyler Pavlas:** So maybe what we can look at, because our standard engagement, we do the eight-week strategy sprint and then the 12-month growth execution.

**Tyler Pavlas:** And we've been doing some of the strategy sprint work with you all.

**Tyler Pavlas:** We'll all too.

**Tyler Pavlas:** too.

**Tyler Pavlas:** Thank

**Tyler Pavlas:** We evaluate the feasibility, just so that we enter it, like, you know, if we both do this, there's going to be a lot of time invested, so we just want to make sure when we get there, we're all feeling good about the potential of what we could execute on, and also what's in scope.

**Tyler Pavlas:** So I think we have enough Kirkland, correct me if I'm wrong, for like the first work stream revamping, because there's so many templates that have been created already, there's so much opportunity to improve.

**Tyler Pavlas:** I think that work stream makes a ton of sense to enter the strategy sprint, and we could potentially identify a lane around, like, net new template creation for these AI templates while we're in the strategy sprint, but just create a proposal that only factors in the work stream around revamping existing templates to start.

**Tyler Pavlas:** Does that seem like it makes the most sense?

**Tyler Pavlas:** I feel like we just have more work to do on the other work streams, but we know for sure on, like, revamping existing templates that we could be successful.

**Danielle Lapierre:** Could revamping existing templates look...

**Danielle Lapierre:** Like splitting it into a bunch of variants that are verticalized.

**Tyler Pavlas:** For sure.

**Kirkland Gee:** And then, I mean, I say that, I say for sure, caveat of as long as there's no, you know, rabbit holes I don't know about, right, which could come up.

**Kirkland Gee:** But from what I'm hearing from you guys, it sounds pretty feasible, right?

**Kirkland Gee:** Like, and when you say verticalized, make sure I understand, say there's a template that's, you know, support form comes in, send a Slack message.

**Kirkland Gee:** We do that for 30 or 50 or 100 or whatever different specific places a support form might come in, right?

**Kirkland Gee:** So like customer service or HR or whatever, fill in the blank, right?

**Danielle Lapierre:** Yeah, like ClickUp AI or sorry, Slack ClickUp AI could be intake product roadmap items or it could be intake new content requests or, you know, just getting more specific there.

**Kirkland Gee:** And if they convert better suite, if they don't, then.

**Kirkland Gee:** And then, yeah, we can customize the landing page content.

**Kirkland Gee:** That's not hard.

**Kirkland Gee:** And then customize.

**Kirkland Gee:** Customizing the templates themselves.

**Kirkland Gee:** You guys talked a lot about like doing the field mapping or improving those sorts of things.

**Kirkland Gee:** Steven, I think we don't foresee any like significant problems.

**Kirkland Gee:** Like Mason, can I get, if I take a template URL, is there an easy way for me to get like a JSON file of that Zap automation and then edit it and re-upload it somewhere else?

**Steven Schweibold:** Yes.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** I thought so, but I just wanted to make sure.

**Steven Schweibold:** What we would do is, is we could work with you all.

**Steven Schweibold:** So we could just like provision you accounts into our CMS.

**Steven Schweibold:** And then what you could do is you could programmatically upload any changes they get thrown in into, you know, effectively like a moderation queue.

**Steven Schweibold:** And then we could go ahead and just have you all self-service in terms of, you know, publishing those and doing the testing and everything.

**Steven Schweibold:** That's the way we would go about it.

**Kirkland Gee:** no, I think that makes sense.

**Kirkland Gee:** Because like, I'm just thinking from a workflow perspective, you know, conceptually, right?

**Kirkland Gee:** Thank

**Kirkland Gee:** It's like I take a URL and then I can take that URL, pull whatever content from the CMS, do some workflow stuff, right, to refresh and update it, push those changes back.

**Kirkland Gee:** Like all of that seems relatively straightforward with just like a little bit of finagling and a lot of prompt and context engineering, but that's the stuff we're good at.

**Kirkland Gee:** I'm more worried about making sure there's not going to be some weird technical issue, but I think this all makes sense.

**Tyler Pavlas:** So I think for next steps, I can work with Marcel to put an initial proposal together for phase one and phase two.

**Tyler Pavlas:** Kirkland, I think if there's more due diligence that you want to do around the use case, I don't know, Steven, if you or any others could stay on for a little bit longer, but I've got to run to another call.

**Tyler Pavlas:** So I'll leave, I guess, like the rest of the technical due diligence to the team here, and then I'll make sure, I guess, on that proposal call, who needs to be there, Danielle?

**Danielle Lapierre:** That is a great question.

**Danielle Lapierre:** Definitely, Danny.

**Danielle Lapierre:** I think he's the interim driver while we find a new driver.

**Danielle Lapierre:** And I would say probably this through.

**Tyler Pavlas:** Yeah, I think it could be smaller audience just because it'll be like reviewing price and the scope that we're talking about now.

**Tyler Pavlas:** But I'll probably just like reach out to Kaveh and see what he thinks since he was the one pushing the proposal.

**Tyler Pavlas:** Okay.

**Tyler Pavlas:** Okay, cool.

**Tyler Pavlas:** I'll make you the host here, Kirkland.

**Tyler Pavlas:** And if y'all want to do some more due diligence, definitely feel free.

**Kirkland Gee:** Sorry, I got to I think we're close, but I may just clarify one or two things and I'll let you guys go.

**Kirkland Gee:** But thanks, Tyler.

**Kirkland Gee:** Thanks, y No, I think that all makes a lot of sense to me.

**Kirkland Gee:** The only thing I just want to circle back to, I'm seeing some stuff in the chat about the sort of AI templates being a priority.

**Kirkland Gee:** What is like the situation there?

**Kirkland Gee:** Because you mentioned there are some technical stuff that's going to need to be done first before we can really ramp those.

**Janine Anderson:** I'm not sure that's true for the AI by Zapier templates.

**Janine Anderson:** Those ones are...

**Janine Anderson:** are...

**Janine Anderson:** all amazing.

**Janine Anderson:** are...rale?

**Janine Anderson:** If anybody else feels like they have more context on this, please feel free to jump in and take over because I'm just talking basically because I have had to make a lot of templates in my life here.

**Janine Anderson:** But the templates for things that are pretty, like, I'm going to call them straightforward zaps, whereas really you're using our workflows product and you're setting up a linear automation that might have pads or filters or whatever.

**Janine Anderson:** The AI by Zapier templates, there's a bunch of them right now that are missing a determinate action step.

**Janine Anderson:** So it has, like, a trigger, and then the AI step is meant to go in the middle between your trigger and something else.

**Kirkland Gee:** So it's, like, someone fills out a form and then an AI step evaluates or crafts a response or a something, and then it's supposed to go someplace.

**Janine Anderson:** But because a lot of these templates were created kind of automatically and they didn't have the third step on it, we're trying to make sure that we have, like, the full determinate workflow.

**Janine Anderson:** So those would be the ones that could be created where we have a lot of...

**Janine Anderson:** templates that have been created for like a chat GPT or a cloud or something else where we have the determinant full workflow where like trigger AI step, action step, and we'd want to be able to take the most popular of those and duplicate those within the AI by Zapier stuff.

**Janine Anderson:** So we'd be like using existing data with non AI by Zapier AI apps as that middle step and shift them into the ones that make versions of those for AI by Zapier.

**Janine Anderson:** But then I think we also might want to take a look at any of these ones that get a lot of traffic that have just the missing third step and see if we can make versions of those that have the proper end step and then we can kill off the ones that don't work in redirection.

**Janine Anderson:** If they're getting enough traffic to be worthwhile.

**Janine Anderson:** Does that make sense, Danielle and Steven, do you think?

**Danielle Lapierre:** Yes, and I'm hesitant to even, like, unless they're really doing well, I think we should just kill most of the two-step ones.

**Danielle Lapierre:** Yeah.

**Kirkland Gee:** And Can I just should No, no, no.

**Kirkland Gee:** one, surprise, Before

**Kirkland Gee:** If clarify something, you're talking about two-step, three-step, if I'm looking at a page like this, this is an example of a two-step template, because all it's saying is, when something happens...

**Kirkland Gee:** That's not a template.

**Janine Anderson:** This is not a template.

**Janine Anderson:** That's a two-service page.

**Kirkland Gee:** Okay.

**Kirkland Gee:** So if you...

**Janine Anderson:** I'm looking at these.

**Danielle Lapierre:** If you scroll down, yes.

**Janine Anderson:** if you...

**Janine Anderson:** Yes.

**Janine Anderson:** So this one right here, whatever you were...

**Janine Anderson:** Like, if you scroll to the top of that, what you have here is a...

**Janine Anderson:** Like, this is a template.

**Kirkland Gee:** But what it's doing is saying, when there's new items and multiple RSS feeds, analyze and return data.

**Janine Anderson:** Right.

**Janine Anderson:** there's no place for that data to go.

**Janine Anderson:** So it's just going to get stuck in that...

**Kirkland Gee:** Right.

**Janine Anderson:** It's actually putting it anywhere right now.

**Janine Anderson:** So we'd need to have, like...

**Janine Anderson:** Yeah.

**Janine Anderson:** Yeah.

**Janine Anderson:** So it would need to have something that goes...

**Janine Anderson:** Like, there should be another step where it's, like, send followers or whatever it is.

**Janine Anderson:** Yeah.

**Janine Anderson:** So these are the ones where...

**Kirkland Gee:** Yes.

**Kirkland Gee:** It comes from granola.

**Kirkland Gee:** It does the analyze.

**Janine Anderson:** And then...

**Janine Anderson:** Creates the source of the notion.

**Kirkland Gee:** I understand.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** And these we could in theory create like is all is like most of this data, like where does most of the data on this page come from?

**Kirkland Gee:** Do each page kind of contain its own?

**Kirkland Gee:** Or if I put a granola and notion somewhere, do I automatically get these triggers and actions?

**Steven Schweibold:** you guys know what Danielle and I were talking about?

**Steven Schweibold:** So there's an internal API that you will need to get access to.

**Steven Schweibold:** That can signal to you what available fields and triggers and actions are available for each app.

**Steven Schweibold:** Some of this stuff is available publicly, but other stuff is through internal resources.

**Steven Schweibold:** So I can work with you all to get access to those things to build out your models to create these.

**Steven Schweibold:** But effectively what we're trying to articulate is, is that the biggest gap that we have right now.

**Steven Schweibold:** Is Zapier historically and today is perceived as this very simple solution to most folks where you connect one app to the other app.

**Steven Schweibold:** And what we want to show folks is that we're a much more capable system that's able to do a lot of inference between one app to another app so that we can do complex handoffs based off of different types of scenarios.

**Steven Schweibold:** And so we really just want to pivot away from these two-step things.

**Steven Schweibold:** Yeah.

**Steven Schweibold:** And so, yes, we can get you, long story short, yes, can get you the data for those to feed into your model so that you can make updates.

**Steven Schweibold:** And ideally, a lot of the field mappings are already applied with these templates so that folks can get up to speed really quickly.

**Steven Schweibold:** And all they have to do is really put in their account information and add some specifics around what they're trying to do with their business.

**Kirkland Gee:** Yeah.

**Danielle Lapierre:** Yeah.

**Danielle Lapierre:** Okay.

**Danielle Lapierre:** Important detail here.

**Danielle Lapierre:** The page that you were just on is...

**Danielle Lapierre:** Is a app directory page.

**Danielle Lapierre:** Those are the templates that we're moving away from.

**Danielle Lapierre:** And like, not just we're moving away from two-step Zapps, we're also moving away from those pages and that as a system.

**Danielle Lapierre:** And so when we think about like the pages we want to optimize and the templates we want to optimize, take a look at zapier.com slash templates, the logged in and logged out version.

**Danielle Lapierre:** That's what we want to focus on here.

**Danielle Lapierre:** And then a lot of the templates that you saw on the page you were just on, those are going to go bye-bye unless they're doing really well.

**Danielle Lapierre:** They're very much the past though.

**Kirkland Gee:** And so important question, because like from what I understand, something like this, one of these more complex Canvas templates, like we don't have the ability to generate these at scale right now.

**Kirkland Gee:** Can I make this landing page out of a different template?

**Danielle Lapierre:** Yeah, so in this hub you can have.

**Danielle Lapierre:** Two-step Zapps, if you want to, we probably wouldn't.

**Kirkland Gee:** Right, but maybe I have a simple.

**Danielle Lapierre:** So this is the landing page we're going to make no matter what we're doing, which is header, assets, content, FAQs, related templates.

**Danielle Lapierre:** Is this generated automatically or is this something you have to manually populate to her template?

**Kirkland Gee:** It's very manual, but it can be automated and done that way.

**Kirkland Gee:** Is it just a URL that needs to go in here?

**Steven Schweibold:** I believe we link content, I believe, if I remember off the top of my head, today we link other pieces of content within the CMS.

**Kirkland Gee:** It's not URL-based.

**Kirkland Gee:** We could have got botified so it's URL-based.

**Kirkland Gee:** just think, I'm just trying to think of if I'm generating these outside of CMS, it's much easier to be able to put, like, I can look at the sitemap, do a scrape, like, do some sort of, like,-based similarity thing to at least get us somewhere on related templates versus having to, like, because, again, anytime there's something where somebody's going to to take five, ten minutes to manually go do

**Kirkland Gee:** It's just going to slow the whole thing down.

**Kirkland Gee:** So I try to kind of preempt any of that, but this all makes sense.

**Kirkland Gee:** No, this is actually super helpful because ultimately data structure is going to be this page plus whatever the template is going to look like.

**Kirkland Gee:** So that all makes sense.

**Kirkland Gee:** Okay.

**Kirkland Gee:** Cool.

**Janine Anderson:** Very good.

**Janine Anderson:** Okay.

**Kirkland Gee:** Cool.

**Kirkland Gee:** I don't think I need to take up any more of your time.

**Janine Anderson:** Do we have any links for Zap templates that are in that new format that we can share with them?

**Kirkland Gee:** Ones that are like Workflows products?

**Janine Anderson:** believe I actually saw.

**Janine Anderson:** It's just more that you can't find them in that library because Workflows isn't a product you can click on the filters.

**Janine Anderson:** It's only the newer products.

**Danielle Lapierre:** I'm pretty sure I sent one of the examples though.

**Kirkland Gee:** Is this one of them?

**Janine Anderson:** The Slack thread summarizer?

**Janine Anderson:** Isn't this one of the...

**Janine Anderson:** Yes.

**Janine Anderson:** Yeah, that is.

**Janine Anderson:** Thank you, Daniela.

**Janine Anderson:** I just...

**Kirkland Gee:** My chat...

**Kirkland Gee:** Brain, you're all good.

**Kirkland Gee:** And all these images, these are just things you added to this page, yes?

**Kirkland Gee:** Yes.

**Kirkland Gee:** Okay, cool.

**Kirkland Gee:** Got it.

**Kirkland Gee:** Yeah, I mean, definitely still some scoping left to do, but I think this all is, like, doable and makes sense.

**Kirkland Gee:** There's nothing that seems crazy.

**Kirkland Gee:** Just some challenges to solve for.

**Kirkland Gee:** So, awesome.

**Kirkland Gee:** All right.

**Kirkland Gee:** Well, thank you guys very much.

**Kirkland Gee:** I'm sure we'll talk soon.

**Kirkland Gee:** Thank you.

**Kirkland Gee:** Thank you.

**Kirkland Gee:** Yeah, have a good day, everybody.
