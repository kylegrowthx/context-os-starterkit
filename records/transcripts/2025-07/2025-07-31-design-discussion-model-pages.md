# Design Discussion: Model Pages

<metadata>
date: 2025-07-31
time: 15:15 UTC
duration: 25 minutes
organizer: mara@growthx.ai
participants: Vivek Shankar, Mara Leighton, Jackson Wells, Jeffrey Gardner
fathom_recording_id: 77702817
fathom_url: https://fathom.video/calls/367542807
share_url: https://fathom.video/share/xQxxt4DuSBYbYNrtyCynSfFh_miuyfcq
source: fathom
enriched_on: 2026-03-03 00:15 UTC
</metadata>

---

## Summary

Jackson Wells, Jeffrey Gardner, and the GrowthX team (Vivek Shankar and Mara Leighton) aligned on the design and content strategy for Galileo's new model comparison pages. They decided to build three page types: an overview hub similar to Ramp's landing page, individual model pages based on Jeffrey's existing leaderboard redesign, and comparison pages for model-vs-model analysis. The team prioritized interactive elements and data visualization over heavy copy, with a goal of real-time data updates but accepting weekly updates as the minimum cadence. Jeffrey will create wireframes and clean up the existing leaderboard redesign by August 11-12, while Jackson will rebuild the pages in Framer and GrowthX will handle content population based on provided templates.

---

## Context

Galileo is building model comparison and leaderboard pages to drive owned traffic from their AI model assessment content. The leaderboard currently lives on Hugging Face but they want to create a suite of pages on their own website (Galileo.com) that showcase individual model performance, comparison data, and a hub page. Vivek Shankar and Mara Leighton from GrowthX Delivery have experience with similar implementations for clients like Ramp, where they managed both static and dynamic data elements. Jeffrey Gardner is leading the design work on the leaderboard redesign itself, while Jackson Wells is coordinating the broader content and product strategy. This is positioned as a high-priority traffic play for Galileo.

---

## Relevance

**To GrowthX Delivery:**
- Client (Galileo) wants interactive, data-heavy product pages rather than traditional SEO blog posts — different content strategy and design approach than standard content marketing.
- Real-time vs. weekly data update decisions impact engineering scope and automation requirements; GrowthX will need to populate templates based on Galileo's data feeds.
- Ramp precedent provides template for mixed static/dynamic page structures; Vivek is advising on what works for user expectations and SEO (freshness signals).

**To CheckThat:**
- Galileo's leaderboard is an AI model performance ranking product — direct competitive landscape for CheckThat and interesting data point on how models track visibility and benchmarking.
- Leaderboard lives on Hugging Face; Galileo is fragmenting discovery across multiple domains (HuggingFace + their own site) to capture traffic for both platforms.

**To GrowthX Business Development:**
- Strong account health signal: Galileo is investing in owned content and product-level pages, positioning them as growth-focused. High-priority project.
- Potential for content template reuse across future Galileo initiatives; opportunity to build repeatable motion for model comparison pages in other verticals.
- Aug 11-12 deadline is firm; Jackson is coordinating with design/engineering to deliver templates on time.

---

## Overview

- Leverage Jeffrey's existing leaderboard redesign as a foundation for individual model pages
- Prioritize interactive elements and data visualization over heavy copy
- Aim for real-time data updates where possible; weekly updates at minimum
- Create three page types: overview hub, individual model pages, and comparison pages

---

## Key Topics

### Page Structure and Design

  - Overview hub page similar to Ramp's landing page
  - Individual model pages based on Jeffrey's leaderboard redesign
  - Comparison pages for model-vs-model analysis
  - Header/subheader with visual element and dynamic model card
  - Include "Last Updated" date in header area
  - Focus on interactive elements and graphs over lengthy copy

### Data Management and Updates

  - Ideal: Real-time data updates
  - Minimum: Weekly updates
  - Include "Last Updated" and "Next Update" notices for user expectations
  - Explore options for automating data pulls from Hugging Face

### Content Strategy

  - Treat pages as product pages rather than SEO blog posts
  - Use briefer copy with more interactive elements
  - Link to these pages from blog posts for SEO benefits
  - Reuse leaderboard data for individual model pages
  - Comparison pages will require data from two models

### Design and Development Process

  - GrowthX team to handle content population based on provided templates
  - Jeffrey to focus on design aspects
  - Jackson and Jeffrey to determine which leaderboard segments to include on overview page
  - Simplify data presentation by removing complex sorting/filtering on individual model pages

---

## Action Items

**Jeffrey Gardner (Galileo)**
- Create wireframe for individual model page template; clean up existing redesign (due Aug 11-12)
- Complete SEM landing pages w/ Jackson this week (immediate priority)

**Jackson Wells (Galileo)**
- Rebuild pages in Framer after Jeff finalizes design
- Create shortcut ticket w/ compiled meeting info; assign to Jeff

---

## Transcript
**Jeffrey Gardner:** We're almost outnumbered by the bots.

**Jeffrey Gardner:** Yeah, now we have more.

**Mara Leighton:** Anyway, but you were saying that you had an example that might be slightly more on brand.

**Mara Leighton:** Yes.

**Jeffrey Gardner:** I'm not saying it is amazing or anything, but I can share this in our chat.

**Jeffrey Gardner:** I may need to give you guys access to this.

**Jeffrey Gardner:** Okay.

**Jeffrey Gardner:** Maybe not.

**Jeffrey Gardner:** Oh, wow.

**Jackson Wells:** Oh, so I mean, it's definitely, yeah, this is.

**Jeffrey Gardner:** Yeah, I started just like kind of building it out based off of the existing leaderboard.

**Jeffrey Gardner:** Oh, yeah.

**Jackson Wells:** That's great.

**Jackson Wells:** So we can definitely take components from this too and then just obviously make it more broad.

**Jackson Wells:** Yeah.

**Jackson Wells:** Per model, but the individual modules for the different categories and stuff will be something we can use per model and make it just a little bit more broad.

**Jeffrey Gardner:** Just wanted to share this in case it was at all helpful because I did it and then Prateek obviously never had the time to update the actual leaderboard.

**Jeffrey Gardner:** So, yeah, the leaderboard itself has to live on hugging face for other reasons.

**Jackson Wells:** So, but I think this adaptation of like a model comparison hub and individual pages is a good way to kind of get some owned traffic from it and still have the primary leaderboard on hugging face.

**Jackson Wells:** Yeah, I'm not saying we have to like recreate the whole thing.

**Jeffrey Gardner:** I guess that was another one of my questions.

**Jeffrey Gardner:** How much data are we going to need to like capture?

**Jeffrey Gardner:** For this, like, is it going to be, like, real-time updating data?

**Jeffrey Gardner:** Like, is this the type of thing where it's, like, there's just, like, a data set that we're going to upload, and then it's going to reference that?

**Jeffrey Gardner:** I guess in terms of just complexity, how is that going to work?

**Jackson Wells:** That is a good question.

**Jackson Wells:** That is a good question, because if it could be something that we upload and update that way, it would be much more useful, so we don't have to, like, go back and do massive updates manually, but I'm not sure how be a way to just pull it from hugging face, because it's all there, obviously, right now.

**Jeffrey Gardner:** I just don't know if there's an easy way to grab all of that.

**Jeffrey Gardner:** Yeah.

**Jackson Wells:** Vivek slash Mara, have y'all ever worked with a client where it's been...

**Jackson Wells:** Where it's been...

**Jackson Wells:** Sort of a circumstance where it's like data that gets updated automatically versus like building a bunch of pages at first and then just kind of letting them live for a while?

**Jackson Wells:** Or what have you all seen work in the past?

**Vivek Shankar:** So with Ramp, which we're doing for them, it's live.

**Vivek Shankar:** They have live and static elements.

**Vivek Shankar:** So if you look at the overview page, which we're calling the model card page, so to speak, the 4% higher, wait, let me share my screen, this might be easier.

**Vivek Shankar:** So these little blocks, okay, so these things here, the 4% higher, 6%, whatever, I believe this is real time.

**Vivek Shankar:** I mean, it's not like, you know, a ticker or whatever, but it updates on its own.

**Vivek Shankar:** But these graphs over here, they're not planning on changing them anytime soon.

**Vivek Shankar:** My guess is it's going to be like a...

**Vivek Shankar:** So it's both static and dynamic.

**Vivek Shankar:** Given the AI space, I don't think the six-month update is ideal just because of how fast it moves.

**Vivek Shankar:** Real-time would be amazing.

**Vivek Shankar:** But, yeah, if that's not an option, I would say weekly at least.

**Vivek Shankar:** You know, I don't know.

**Vivek Shankar:** Mara, what do you think?

**Vivek Shankar:** I would agree.

**Mara Leighton:** I would say, like, you know, best-case scenario, well, I don't have necessarily the experience with the cons that might be attached to this.

**Mara Leighton:** So there's probably things that I'm overlooking.

**Mara Leighton:** But I feel like, you know, as many elements that can be live is ideal just so that it's updated in real-time.

**Mara Leighton:** So I feel like that's the preference.

**Mara Leighton:** But I know that's a little bit more complicated to implement.

**Jackson Wells:** Yeah.

**Jackson Wells:** Yeah, we'll have to think about that.

**Jackson Wells:** For sure, from like a logistics perspective of how we can have that data be real-time.

**Jackson Wells:** And that is also dependent on how often Pratik is updating those results.

**Jackson Wells:** We can.

**Vivek Shankar:** I don't know if this helps, but we can always have like a little notice on the page itself that says next updated on whatever, you know.

**Vivek Shankar:** So that sets the expectation that people, I mean, it's all about UX.

**Vivek Shankar:** That's where I'm coming from.

**Vivek Shankar:** So they know that, okay, this is when it was last updated.

**Vivek Shankar:** This is when it will be next updated.

**Vivek Shankar:** So the expectation is set.

**Vivek Shankar:** And Google appreciates that too.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** Yeah.

**Mara Leighton:** That would be one other element too, where if that is also updated live, that also could be useful for us just from the perspective of the content always being graded as fresh, you know, because if it has a date in it.

**Mara Leighton:** So that would be one other pro there if we have that little.

**Mara Leighton:** like I think.

**Mara Leighton:** So.

**Jackson Wells:** So,

**Jackson Wells:** That definitely makes sense. Okay, so let's start this document now. Obviously, we're going to need a header slash subheader with probably some sort of visual element at the top. I'm guessing some form of model card that's dynamic just because that would be easy to implement on every page and kind of gives people the gist before they actually dive into the info.

**Jackson Wells:** We'll probably want that updated date in the header area just so it's also clear.

**Jackson Wells:** Dynamic model card and last updated date.

**Jackson Wells:** Let me think of what else. I think for the second component, I do quite like Ramp's real-time updated cards that are there with the different statistics. And I think we can do that and honestly just break apart some of the different takeaways from the leaderboard itself to do that.

**Jackson Wells:** So as far as the content depth on the page, what have y'all seen work in the past?

**Jackson Wells:** Like, do we want to go heavy on supporting copy and treat it more like an SEO blog in that sense?

**Jackson Wells:** Do we want to go heavier on, like, some of interactive elements with briefer copy?

**Jackson Wells:** What do you guys think would be a good call there?

**Vivek Shankar:** I think for these kinds of pages, we treat them as product pages.

**Vivek Shankar:** So more interactive and then just link to them from all our blogs so that Google gets the idea.

**Vivek Shankar:** Copy, I think.

**Vivek Shankar:** But we should support more.

**Vivek Shankar:** And besides, I think if, you know, I'm saying this because looking at the intent behind people searching for these things, they don't want to sit there and read stuff.

**Vivek Shankar:** They rather look at graphs.

**Vivek Shankar:** So, yeah, and that helps the, that helps the overall workload for sure.

**Jackson Wells:** Okay.

**Jackson Wells:** Well, with that in mind, let me look at the leaderboard again and think about the different graphs and different things that we're going to want there.

**Vivek Shankar:** So, yeah, looking at the Figma redesign that Jeffrey has in there, I think that's pretty much the model overview page right there. Like we can literally copy-paste it because it's got really good data in there and the design looks great. So it's only the versus stages that will need some engineering.

**Vivek Shankar:** In terms of getting the data in there, like comparing one model to the next, that's the more complicated task engineering-wise.

**Vivek Shankar:** But yeah, I think for overview pages, the existing design works. We could replace some of the buttons with text maybe, but yeah, I think it works.

**Jackson Wells:** I think that makes sense for sure. I think from this design, the only thing that we would probably need to do is maybe just reconfigure the header a little bit, just so we can have a little bit more space for a model card. Left text, copy, right image — we can probably make that work. Thanks, Jeff.

**Jeffrey Gardner:** Good job.

**Jeffrey Gardner:** Pass, Jeff, coming through.

**Mara Leighton:** We didn't expect you to have just like something beautiful already to go.

**Mara Leighton:** We didn't expect you to just have something beautiful already to go.

**Mara Leighton:** Yeah.

**Jeffrey Gardner:** Sorry, I'm like rubbing my jaw.

**Jeffrey Gardner:** Oh no, I bet.

**Jeffrey Gardner:** Yeah.

**Mara Leighton:** Crazy.

**Mara Leighton:** Do you have any other questions, Jeff, or anything else we should talk about?

**Mara Leighton:** And Jackson, sorry, I'm sure you have some questions as well, but is there anything else that we should provide or could answer?

**Jeffrey Gardner:** So, I guess I haven't really worked closely with y'all before.

**Jeffrey Gardner:** Am I going to just kind of be, like, taking care of the design aspect of this, and then, you know, you guys will be working with Jackson and maybe Connor on, like, some of the content and the things like that?

**Jeffrey Gardner:** Like, how do, I guess, support either of the projects overall?

**Mara Leighton:** Yeah, typically we front-load the design conversation so we can understand what elements will be on the page. Then we work backward to populate them, and we share input on best practices from other accounts. That's generally how it works. I hope that answers your question.

**Jeffrey Gardner:** No, that does answer it. For me, with design, I think it's important that Jackson and I figure out the content — figuring out which segments from the leaderboard make sense to be on the overview page.

**Jeffrey Gardner:** Because it sounds like we're going to need to have separate comparison pages. So the hierarchy is one main page and then subpages off of that?

**Vivek Shankar:** It's not necessarily a subpage, but in the backend when you're pulling data, they will be related.

**Vivek Shankar:** It's not going to be a child page. I'm thinking we could have something similar to Ramp — a model comparison hub. The hero section is the landing page, then you have overview pages for individual models with model cards, and separate comparison pages for model-versus-model analysis. Ramp actually classifies it as a child page in the URL for data reuse, but I don't think we need that structure for our purposes right now.

**Vivek Shankar:** Okay, that's great.

**Jeffrey Gardner:** Sweet, that makes sense to me.

**Jeffrey Gardner:** The pages that will need the data, it's not the overview page, it's those comparison links that someone will be clicking on.

**Vivek Shankar:** Well, the overview will need the data that's currently on the leaderboard. So everything that you're displaying for a particular model — performance across sectors, benchmark performance, domain performance — we will need that on the overview page. The versus page will just be comparing this model's performance to another.

**Vivek Shankar:** So engineering-wise, that's why I was saying, like, the versus pages might be a bit trickier because you're going to have to get to data sources.

**Vivek Shankar:** But I think for the overview pages, you already have the data. It's just your leaderboard, but you isolate it to one model and plug it in.

**Jackson Wells:** Great. So we need the overview page, then a template for the comparison pages. We can pretty much just reconfigure the actual redesigned leaderboard draft that you have for the individual model pages, and that should be pretty quick.

**Jackson Wells:** Jeff, given your current bandwidth and projects in flight, what do you think is a reasonable due date for us to assign for a V1 for this?

**Jeffrey Gardner:** Well, think the more important question is, when do you need it to go live?

**Jeffrey Gardner:** Because typically, I'll say something, and that doesn't matter.

**Jeffrey Gardner:** So you let me know.

**Jeffrey Gardner:** Damn, God.

**Jackson Wells:** Host Dentist Jeff is spicy.

**Jackson Wells:** Let's see here.

**Jackson Wells:** I'm just being real.

**Jackson Wells:** I'm just being real.

**Jackson Wells:** I love that.

**Jackson Wells:** That's what we're here for.

**Jackson Wells:** I mean, this is very high priority for us from a traffic perspective, and it's going to help us broadly start to capture some more different intent traffic that I think would be a good call and make the whole team happy.

**Jackson Wells:** I think if we could get the templates into the growthx's team, into the hands of the growthx team by early next week, mid next week, I think that would be, I think that would be good.

**Jackson Wells:** Let me look at...

**Jackson Wells:** Let me look at all of the other things in play right now and kind of start weighing them a little bit more.

**Jackson Wells:** Let's see here.

**Jeffrey Gardner:** Ideally, I was thinking like the 11th or the 12th of August.

**Jackson Wells:** From a workflow perspective, what makes sense for you guys, Mara and Vivek? If we get you the template for individual model pages, would you guys be able to get started on that while Jeff spends more time on the overview?

**Vivek Shankar:** Yeah, just give us the templates. From our end, it's really just figuring out where the text goes and what we need to generate. We'll build the flow on our end. Even a wireframe would be great — doesn't have to be pretty, just a map of what goes where.

**Jackson Wells:** That makes sense. Jeff, SEM landing pages are our immediate top priority this week. Let's get those done, and then you can switch gears into this next week.

**Jeffrey Gardner:** I have a question for either you or the GrowthX team. If we're looking at the current leaderboard, there are lots of ways to sort things, and it's not exactly clear where that's happening or how that's happening. Have you guys built anything with this much data that actually makes sense? To me, this is kind of a mess.

**Vivek Shankar:** It is a lot of data, but I think the complexity is coming from the sorting you mentioned — it's highlighting every single model at once, whereas our page will have just one model. The data is present, we just need to remove the filters and isolate it to the specific model.

**Jeffrey Gardner:** So the overview page will be specific to each model that we're highlighting?

**Vivek Shankar:** Yes.

**Jeffrey Gardner:** That makes sense. So we wouldn't need a lot of the sorting and filters that we have on this leaderboard.

**Vivek Shankar:** Correct. Looking at the sections, you have model capabilities, visualizations, real-world performance on top — I don't think we'll need that. We'll need the domain performance analysis graph, and then the cost, performance, efficiency, speed, accuracy sections. We'll just add boilerplate text with SEO-relevant terms. We just need to remove the filters and interactive stuff and it should be good to go.

**Mara Leighton:** Okay.

**Jeffrey Gardner:** I think that's all the questions I have. If I have more, I'll bug Jackson or you guys directly.

**Jackson Wells:** Are you in the GrowthX Slack channel, Jeff?

**Jackson Wells:** That's great — we can chat in there if anything comes up. For next steps, I'll compile the things we talked about. Once the meeting notes come through, I'll create a shortcut ticket and assign it to you, Jeff. We can talk about next steps once the SEM landing page is done, and then we can start working on the template once your backlog is cleared.

**Mara Leighton:** Awesome. Thank you, guys.

**Vivek Shankar:** I appreciate the time.

**Mara Leighton:** Yeah, nice to meet you both.

**Vivek Shankar:** All right, bye everyone.

**Mara Leighton:** Thanks.

**Mara Leighton:** Cheers, all.

**Mara Leighton:** Cheers.
