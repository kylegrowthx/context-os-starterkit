# Siit <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-05
time: 19:00 UTC
duration: 42 minutes
organizer: team@growthxlabs.com
participants: Jakub Rudnik, Matthew Alves-Hill, Chalom Malka, Carmel Schetrit
fathom_recording_id: 99475806
fathom_url: https://fathom.video/calls/462832570
share_url: https://fathom.video/share/bvCkoWxe52Me7unBgVvjy4n1MioHk87G
source: fathom
enriched_on: 2026-03-02 02:15 UTC
</metadata>

---

## Summary

Sync on conversion strategy, content focus, and upcoming website changes.

---

## Context

Siit is a platform for IT service management and request management. This sync between Siit's team (Chalom Malka, Carmel Schetrit) and GrowthX (Jakub Rudnik, Matthew Alves-Hill) focused on Siit's content and conversion strategy. The meeting addressed several key challenges: improving blog-to-demo conversion rates, refocusing content away from low-intent glossary pages and toward high-intent tools/alternatives pages that drive qualified leads, and preparing for a major website rebrand that will consolidate and simplify the site structure.

---

## Relevance

- **To GrowthX Delivery:** Content strategy pivots from broad glossary-focused approach to high-intent tools/alternatives/competitor comparison pages (3-15% conversion vs. 0.25%). CTA testing and lead magnet development (downloadable assets, ROI calculator) are core to this shift. GrowthX will handle redirect management for the website consolidation.
- **To GrowthX Business Development:** Strong account health signal — active collaboration on strategic initiatives (rebrand, new demo video, email nurture campaigns, Scrunch AI visibility tracking). Potential for expanded scope: landing page creation, lead magnet asset development, analytics setup/validation (PostHog data accuracy issues flagged).
- **To CheckThat:** AI visibility tracking is underway via Scrunch (ChatGPT, Perplexity); team using Amplitude for visibility reporting. Opportunity to audit and refine visibility strategy aligned with new content clusters post-rebrand.

---

## Overview

- **New CTA Strategy:** Test "Option 1" (demo-focused) as the new sticky blog CTA. This aligns with the team's current work on a new demo video and targets higher-intent, bottom-of-funnel traffic.
- **Content Pivot:** Prioritize "Tools" pages over "Glossary" content. Tools pages generate higher-intent traffic (3-15% conversion vs. \~0.25% for Glossary) and are now outperforming blog views.
- **Lead Magnet Development:** Create downloadable assets (e.g., checklists) to support email nurture campaigns. This will provide a more effective conversion path than linking to generic blog posts.
- **Website Rehaul:** A major rebrand will consolidate the site, eliminating the French version and hundreds of low-traffic feature pages. GrowthX will manage redirects to preserve SEO.

---

## Key Topics

### Website Rehaul & Strategy Pivot

  - **Rebrand & Site Consolidation:** A full rebrand will consolidate the site into a "lean and mean" structure to improve user experience and focus on key product narratives.
      - The French version of the site will be eliminated and redirected to the English site.
      - Hundreds of low-traffic feature pages will be removed.
  - **New Site Structure:** The site will be simplified to:
      - Homepage
      - Product (Request Management, Workflows, Agents)
      - Integrations
      - Customer Stories
      - Pricing
      - Resources
  - **Content Strategy Pivot:** The content focus is shifting to align with business goals and user behavior.
      - **Deprioritize:** "Glossary" content → generates low-intent traffic with poor conversion (\~0.25%).
      - **Prioritize:** "Tools" & "Alternatives" pages → generate high-intent traffic (3-15% conversion) and are now outperforming blog views.
      - **Refinement:** Focus Tools content on direct competitors (HR help desk, ITSM) to ensure traffic is within the ICP.

### Conversion & Lead Magnet Strategy

  - **New Sticky Blog CTAs:** Jakub proposed three CTA options to increase blog conversion.
      - **Option 1 (Demo-Focused):** Aligns with the team's current work on a new 2-minute demo video.
      - **Option 2 (Pain Point):** Uses "AgentForce" and "Slack" as examples, but requires copy rework as they are specific brands.
      - **Option 3 (Legacy Comparison):** Requires a new, tool-agnostic landing page.
  - **Decision:** Proceed with **Option 1** for faster implementation, pending copy review and the new demo video.
  - **Lead Magnet Development:** Carmel is creating email nurture campaigns but lacks downloadable assets (e.g., checklists) to drive conversions.
      - **Goal:** Repurpose popular blog content into targeted assets that support specific campaign themes (e.g., password resets).
      - **ROI Calculator:** A potential high-value asset. Jakub will research low-code tools to simplify its creation.

### Data & Analytics

  - **Data Accuracy:** The current PostHog setup for tracking blog CTA clicks is inaccurate, showing only 8 clicks for a page with over 100 organic clicks (per Search Console).
  - **Tooling:** GrowthX uses **Scrunch** for AI visibility reporting, a tool that tracks competitive presence and topic visibility across AI models (ChatGPT, Perplexity).
      - The team will begin reporting on Scrunch data and review its setup to ensure it aligns with current content clusters.

---

## Action Items

**Jakub Rudnik**
- Update conversion analysis doc statuses
- Send ROI calculator embed tool link to Carmel
- Confirm Scrunch competitor setup; add missing ICP competitors

**Carmel Schetrit**
- Review sticky CTA options; send copy tweaks to Jakub
- Rework Option 2 CTA header to avoid AgentForce/Slack naming
- Pause glossary content; prioritize ICP tools/alternatives pages
- Draft Q1 email nurture plan w/ 1–2 downloadable assets; share w/ Jakub
- Export and send tools page views (total) to Jakub/Matt
- Send Amplitude AI visibility report to Jakub/Matt
- Send feature page URLs to Jakub; then GrowthX analyze traffic, propose redirects, update internal links
- Show new branding Figma teaser next meeting

**matt**
- Investigate alternatives/tools page CTA logic; propose integration-specific CTAs

---

## Transcript
**Jakub Rudnik:** This meeting is being recorded.

**Jakub Rudnik:** And the record is our best friends just to go walk it's very warm for this type of time of year like I mean like half an hour ago and I'm still like sweating from this it's very weird it's like the like the warmth before a week of cold rain it's like the last like push of the warm air on.

**matt:** Yeah.

**Carmel Schetrit:** Hello.

**matt:** Hey.

**Carmel Schetrit:** Hi.

**Carmel Schetrit:** How you doing?

**matt:** Good.

**matt:** How are you?

**Carmel Schetrit:** Good.

**matt:** In California, which is nice.

**matt:** It doesn't look like you're dressed for a couple of I know.

**Carmel Schetrit:** It's raining today.

**Carmel Schetrit:** But what has not been nice is waking up at five in the morning to get on calls.

**matt:** Yeah.

**matt:** Yeah, I bet.

**Carmel Schetrit:** It's late for you isn't it?

**Carmel Schetrit:** I'm like complaining to you which is like.

**matt:** have

**matt:** Yeah, it's okay, but it's like generally like work more American hours, so it's all good.

**Carmel Schetrit:** Jakub, are you exhausted from all of those listening calls?

**Jakub Rudnik:** It has been so bad for me.

**Jakub Rudnik:** bet Andy is exhausted because yours was just an early one for me, like early in the number of them.

**Jakub Rudnik:** So I'm not there yet, and you're very kind, so that helps nobody.

**Jakub Rudnik:** If was thrashed or something, then I'd probably be a little bit more tired, but yeah, talk to me like the day tomorrow, I'll probably be pretty done, ready for Friday.

**Jakub Rudnik:** So, yeah, but thank you for chatting and all that once again.

**Carmel Schetrit:** Yeah, it was helpful.

**Carmel Schetrit:** I got my brain thinking, so if we could leave just a few minutes at the end, I have a couple of things I wanted to chat through.

**matt:** Rad.

**matt:** Yeah, I was thinking...

**matt:** Um, actually, Jakub, do you want to start with the conversion piece and then you can dive into the other points?

**matt:** Yes.

**matt:** Well, actually, I'll share.

**Jakub Rudnik:** Um, I'm going to, unless anybody has a problem with it, I'm just going to build, like, in this conversion analysis URL.

**Jakub Rudnik:** I'll just keep adding here so we have things.

**Jakub Rudnik:** I'm, like, just dating.

**Jakub Rudnik:** And then, this is a very sloppy project.

**Jakub Rudnik:** haven't updated all the statuses.

**Jakub Rudnik:** I fell a little bit behind today, but I'll get different statuses set up and so we know where each of the different items that I listed here and then that come through on these calls.

**Jakub Rudnik:** Um, but the one thing I knocked out from a technical standpoint beyond just continuing to document was a few of those, like, examples, Carmel, and different ways that we can do this.

**Jakub Rudnik:** It's not extensive.

**Jakub Rudnik:** It's just, it's three.

**Jakub Rudnik:** So, Three.

**Jakub Rudnik:** Here, but options on like, like ramps for showing product visuals and, you know, there's some social proof, scribe it, you know, you'd ask like, do we do free, do we, how do we explain like they go all in on just free, do this, and this has been there for years now, very similar CTAs.

**Jakub Rudnik:** However, like they have a truly free product versus just the free trial.

**Jakub Rudnik:** And so I think it'd be a little bit different.

**Jakub Rudnik:** then why these are so small, they were bigger earlier.

**Jakub Rudnik:** But some kind of thing with this is like using more of the product name, I think they're, you know, bigger brand at this point.

**Jakub Rudnik:** So I like how like scribe is more focused on what you're doing.

**Jakub Rudnik:** Just want to share some examples from some teams I know do a lot of testing on this.

**Jakub Rudnik:** And then I wrote up three options here.

**Jakub Rudnik:** Like, I'm thinking of header and there's like two different lines of text more of like how sprout does it and we can style them different.

**Jakub Rudnik:** But when it was on like showing a demo and sending people over to like the landing page where we have one of those videos, I don't know how updated they are on your YouTube page.

**Jakub Rudnik:** I know there's a couple different videos that have content like that or something else could be created.

**Carmel Schetrit:** Yeah, we're working on this exactly right now.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** And so we could do something like this, like, let's go see it.

**Jakub Rudnik:** Something like book a demo or it could be a different CTA too.

**Jakub Rudnik:** But the, like, was bringing your, like, new guidelines, like chatting with chat a little bit and, like, different inspiration and kept calling out, like, agent force and Slack is one of the, you know, things that's different or highly.

**Jakub Rudnik:** I don't know if you're feeling the same way, but this could be another option.

**Jakub Rudnik:** And this is always what we come back to, like, seat verse lots of things, but especially seat verse, like, the old way of doing it, right?

**Jakub Rudnik:** And so I don't know if we have, but I think we have, like, a page that's kind of, like, agnostic to other solutions.

**Jakub Rudnik:** But it's just like the old way, like legacy solutions.

**Jakub Rudnik:** I don't know what we would exactly call it, but there was a landing page like that.

**Jakub Rudnik:** Something along the lines of like replace your outdated service desk.

**Jakub Rudnik:** So it's not like competing against one.

**Jakub Rudnik:** can be used across a lot of different content, but have an idea and very open to feedback or tweaking here.

**Jakub Rudnik:** know, like these are just V1s and how I would think of potentially doing CTAs.

**Jakub Rudnik:** But these are blogs, like what I would potentially change the blog sticky CTA to, and then probably do a variation that fits the tool pages, depending on your instinct.

**Jakub Rudnik:** And I mean, longer term, we would want to be like running tests on this, like styling, text, et cetera.

**Jakub Rudnik:** But for now, it's like what, take a shot with our gut and then move on to the next thing while we continue to build traffic in each of those experiments and be more meaningful down the road.

**Carmel Schetrit:** Cool.

**Jakub Rudnik:** I like.

**Jakub Rudnik:** So, yes.

**Jakub Rudnik:** Feel free to review.

**Jakub Rudnik:** Let me know what you think.

**Jakub Rudnik:** If there's, like, ideas, we can do more of a brainstorming.

**Jakub Rudnik:** But this is my brain dump.

**Carmel Schetrit:** I we need to create the I like this a lot.

**Carmel Schetrit:** I think we need to create the assets, like, we're working now on the two-minute demo video, except for, obviously, the book of demo.

**Carmel Schetrit:** But the legacy solutions, I was thinking of – I think I mentioned this to you guys last time – taking some of the competitive pages we've done or the tools pages that talk about our competitors and turning those into landing pages of, like, us versus X solution.

**Carmel Schetrit:** So for the third option, the landing page would be a specific tool or, like, a specific legacy competitor or just, like, an overview.

**Jakub Rudnik:** What were you thinking here?

**Jakub Rudnik:** If I'm thinking here

**Jakub Rudnik:** Or something that's universal across the blog, or at least a section of the blog, I would think of it as a tool agnostic page, like Seat first, like the old way.

**Jakub Rudnik:** But then you could either do sections with the specific apps, or a table with multiple apps or something, or tools.

**Jakub Rudnik:** Or like you're saying, if you have these other landing pages for the five competitors that come up the most, that could be linked to or embedded in some way within that page.

**Jakub Rudnik:** But it's like, I would talk about Seat largely, like at large, where it wins against all or most old ways of doing it.

**Jakub Rudnik:** And then, again, it can be the table that shows how pricing, connectivity, et cetera, like are different across Seat first, five apps or something.

**Jakub Rudnik:** I don't know.

**Jakub Rudnik:** So it's a little bit of an unfinished thing.

**Jakub Rudnik:** But I would think of it as agnostic or against multiple at once, because it would be on every page.

**Jakub Rudnik:** Not like, if you had...

**Jakub Rudnik:** Just a Seatverse, you know, Jira Service Desk page, like that would be, we would want to send people to like that comparison landing page or something, or if it's like that service desk alternatives, but for something that could just be a, what is blog or something higher up the funnel, I wouldn't want to send them to a specific tool because we don't have any indication of what tool that person uses necessarily.

**Carmel Schetrit:** Okay, cool.

**Jakub Rudnik:** Got it.

**Jakub Rudnik:** Mm-hmm.

**Jakub Rudnik:** Um, yeah, that's the thing I executed on.

**Jakub Rudnik:** I was going to, yeah, I'll finish this and then, is that the, let me know if there's one you're most keen to test on and then we can like map it a little bit and like what is, if it's this one.

**Carmel Schetrit:** I think in the interest of time, like of trying this out faster, I would probably do option one or option two.

**Carmel Schetrit:** Um, but I have to rework the option two header because agent force and slack are like actual things, like.

**Carmel Schetrit:** AgentForce is Salesforce agents, and Salesforce owns Slack, and is trying to push an ITSM now.

**Carmel Schetrit:** But, yeah, I would say probably option one or option two, even though they are very, like, bottom of the funnel-y.

**Carmel Schetrit:** Like, I'm interested to see, yeah, if people interact.

**Jakub Rudnik:** And we could do, like, with the amount of traffic we have, we can run, like, we could do two weeks of this, and then two weeks of something in our middle of funnel.

**Jakub Rudnik:** And, like, when the content is more mature, there's, you know, things where you could have CTAs surfacing dynamically based on the content piece or a tag or something, but we're far away from that.

**Jakub Rudnik:** So, yeah, there's, like, about what's universally going to work the best, and just where your business goals were, was going to, like, push more aggressive ideas here.

**Carmel Schetrit:** Yeah, I think probably option one, given the fact, too, that we're

**Carmel Schetrit:** We're to do this demo thing, or that we're doing the demo recordings.

**Carmel Schetrit:** I think this would be a good place to repurpose it.

**Jakub Rudnik:** Okay, cool.

**Jakub Rudnik:** So, yeah, then we can just move this into, like, the next stage, and once we have that demo re-recorded, get a landing page set up.

**Carmel Schetrit:** Let me, also, we have, I have access to that, right?

**Jakub Rudnik:** I just want to tweak the copy a little bit.

**Jakub Rudnik:** Yeah, yeah, no, take, tweak, tweak.

**Jakub Rudnik:** This is, this is me and chat doing B1s, for sure.

**Carmel Schetrit:** Cool.

**matt:** I was just looking out, Jakub, while you were showing that, I just noticed, like, in the, let me just show.

**matt:** So, in the alternatives page, this is, like, Bamboo HR.

**matt:** I'm wondering whether these CTAs are worth, like...

**matt:** So this CTA right now is just pushing you back to, but what we're missing here is like, essentially, we're going to have at least one tool in each of these that Siit integrates with.

**matt:** So whether it's like, we push them to one tool, or we have, you know, a couple of blocks here that's like, you know, seed plus bamboo, seed plus, like learn more and push them directly to the integration, as opposed to just pushing them back to the top of the tool page, I think might be a relatively quick win.

**matt:** Yeah, I think that's...

**Carmel Schetrit:** This is not a tool page, yeah, it's an article.

**matt:** No, this is an alternatives page.

**Carmel Schetrit:** Oh, is an alternatives page, okay.

**matt:** And so like, in each one, I mean, we could do, we could definitely do better.

**matt:** Um, this is kind of hidden at the moment, like, you know, the integration is, is hidden in the prose, so it's easy to scroll past.

**Carmel Schetrit:** And this is getting more, I'm pretty sure, like, if we look at, like, the ratio, our tools pages are starting to get more views than our blogs.

**matt:** Yeah.

**matt:** Um, so I think, like, you know, even, I don't know how this is, I don't know how these are made exactly, but, like, even already in here, you know, if rippling is, has an integrate, like, that could be louder.

**matt:** Um, yeah, I'm going to do a little bit more looking into this, but this seems like a, you know, a mess.

**matt:** Um, and also on the tools page, another thing we wanted to chat was potentially, like, ramp, for the, for the remainder of the quarter, like, replacing, potentially replacing the glossary output with, uh,

**matt:** And just like ramping the tools, because if they are, like you say, you know, they're starting to outperform even the blog pages, like to give you a, like this is just the ones that you ticked, potential like pages here, and some of them maybe not relevant, but like there's a load of volume and they're not difficult keywords to rank for.

**matt:** And the way that the alternatives pages spit out, like in order to create these, we almost like have to have higher cadence, because otherwise we're going to leave, we're going to have this like draft issue that we have to like go in.

**Carmel Schetrit:** I feel like we set it up bad, the logic.

**matt:** I mean, look, the other thing is like we could, like we could just get rid of these, and then it's like less of a problem.

**Jakub Rudnik:** But I quite like the, I don't know, I quite like the, in the way, oh go ahead, come on.

**Jakub Rudnik:** No, no, go ahead.

**Jakub Rudnik:** I was just going to, it is like, it does cause issues.

**Jakub Rudnik:** And like how we operate and all that, as Matt said, but it is like nice for user experience and does look good.

**Jakub Rudnik:** Like if you get to the end, then it's a great thing.

**Jakub Rudnik:** It's just like sometimes in between like the production and actual execution between like where we want to get to is a pain.

**Jakub Rudnik:** I do think the cadence and not like overcoming that is one piece, but Carmel, just with your business goals, like glossary is always like the lowest level of conversion from a content standpoint.

**Jakub Rudnik:** Like we had tons of traffic at ActiveCampaign on our glossary and it was like, you know, quarter of a percent of like someone putting their hand up versus these tools alternatives lists are going to be three, five, 10.

**Jakub Rudnik:** I've seen 15% on some of them if it's like really one, you know, great, if you are a good alternative.

**Jakub Rudnik:** And so, yeah, I think from Matt's perspective, like for us, it's not any more difficult, if anything, like because of the dependencies, it's slightly better for us.

**Jakub Rudnik:** But from your perspective.

**Jakub Rudnik:** And if we're thinking about what traffic you want in three and six months, this will be just way more valuable traffic.

**Jakub Rudnik:** So it's...

**Jakub Rudnik:** Yeah, I agree.

**Carmel Schetrit:** My only thing is, and this doesn't have to do with glossary, it's more of like what we focus, what we end up deciding to focus on.

**Carmel Schetrit:** Tools doesn't necessarily mean that they're coming to us because they're in our ICP.

**Carmel Schetrit:** They could be just interested in, you know, whatever comparison they're looking at.

**Carmel Schetrit:** And that's the one thing that concerns me is that this is great to drive traffic to our website and like, you know, brand credibility.

**Carmel Schetrit:** But on the other hand, it's less guaranteed that for a lot of these tool comparisons or reviews or whatever, that they're actually interested in our solution.

**Carmel Schetrit:** You know what I'm saying?

**Jakub Rudnik:** The, yes, I think the tools that were selected at the beginning of that project, like, were a mixed bag of like, in ICP or not.

**Jakub Rudnik:** I think what we identified or chatted through last week on where we would want to take this is what are your most direct competitors?

**Jakub Rudnik:** And not every single visitor will be in ICP, I suppose, but if they're looking at HR help desk solution or an ITSM, if we cover everyone that says all the categories or products that are as close to ICP as possible rather than branching.

**Jakub Rudnik:** Like, for instance, like we did, you know, Slack or different Slack alternatives, like some of those get further away.

**Jakub Rudnik:** And it's just unclear if they're using Slack for just team communication or, you know, a service desk option.

**Jakub Rudnik:** But here, if we're just looking at service desks, those should be a much larger portion.

**Jakub Rudnik:** And then again, like even the people that aren't, if there's still big volumes and the percentage of those people in your ICP will be much higher.

**Jakub Rudnik:** So I think I hear, definitely hear you.

**Jakub Rudnik:** I think it's like a lot of the tools or categories that we've started.

**Jakub Rudnik:** With versus like where we would want to go and fill out the most relevant tools.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** I agree with that.

**Carmel Schetrit:** So yeah, I agree.

**Carmel Schetrit:** Glossary should be put on the back burner and we could focus more on tools.

**Carmel Schetrit:** My other thing that I wanted to bring up and then we can like decide how we want to do this.

**Carmel Schetrit:** I have been thinking a lot also about like our email strategy and like I'm today sitting and writing, we don't really have automated email at the moment, but I'm sitting and writing a nurture, like a short nurture campaign.

**Carmel Schetrit:** And what I'm realizing is that we don't have any downloadable assets, like pieces of content.

**Carmel Schetrit:** And I was thinking another thing that we could focus on is I could come up with some themes that would align to the type of email campaigns that I want to run.

**Carmel Schetrit:** And maybe we could repurpose.

**Carmel Schetrit:** Some of our most popular blog content into some kind of like downloadable assets.

**Carmel Schetrit:** know this is something that we talked about, Jakub, with Becerra a while back of like easy things to that we could, you know, send like the checklists or things like that.

**Carmel Schetrit:** And I was sitting and writing this nurture and I'm like going through our blogs and trying to like match some kind of blog to whatever I'm the point I'm trying to get across, which isn't ideal.

**Carmel Schetrit:** And also, I don't think that the blog format is ideal for what I'm trying to do, but it's really kind of like all we have.

**Carmel Schetrit:** So also putting that out there to see what you guys think.

**Jakub Rudnik:** I think it goes along with the general conversion and like business drumming up theme.

**Jakub Rudnik:** And then also, like, where, you know, it could be a, we had, if we had something downloadable that we believed in, could be another option for those sticky CTAs or CTA in line, depending on what the content is.

**Jakub Rudnik:** So in general, yes, we do have some resourcing externally, like, that we can use if we have the right option and we have the content that they can do the design for this.

**Jakub Rudnik:** So it is possible for us to, like, support on those pieces.

**Jakub Rudnik:** What I would say is, like, I do like looking at where we have traffic already, somewhat for the content that's already there, like the blog that's generating that traffic.

**Jakub Rudnik:** But, like, if we have five blogs that are thematically very similar, what asset would they, could they all lead someone to download?

**Jakub Rudnik:** Like, if someone was reading this already, like, what would push them to the next page?

**Jakub Rudnik:** Like, what's the next step for them, rather than just, like, that blog that has high traffic, often those are just indication of higher up the funnel.

**Jakub Rudnik:** So it's, like, a combo of, because you also have the newsletter and that's, like, a.

**Jakub Rudnik:** Less specific audience, like it's people from all over the place rather than, you know, one blog.

**Carmel Schetrit:** The newsletter is very like product focused and it's not, you know, focused on like pain points and like higher level stuff, if you will.

**Jakub Rudnik:** Yeah, yeah.

**Jakub Rudnik:** I'm trying to think of like.

**Carmel Schetrit:** Like for example, right now, I'm like, right.

**Carmel Schetrit:** I was writing this email that was like high level nurture.

**Carmel Schetrit:** It's focused on specific pain points of password resets and NAS and access management or like access requests.

**Carmel Schetrit:** And I was like looking for some piece.

**Carmel Schetrit:** We have some stuff on like IAM and whatever.

**Carmel Schetrit:** And that's what I ended up using, like best practices or things like that.

**Carmel Schetrit:** But it would be amazing to have some kind of like, here, we wrote this short checklist for you to like go through and make sure that you have, you know, this optimized or up and running.

**Carmel Schetrit:** Like how to configure the proper workflow or what tools work together, but whatever it is, I can come up with like different ideas, but I feel like what I need to do is create some kind of roadmap of like here are the different campaigns I want to run in Q1 or the one campaign I want to run, if you will, in Q1 and like the two pieces, like we'll start small.

**Carmel Schetrit:** The one campaign I want to run and like the one or two pieces of downloadable content we could create.

**Jakub Rudnik:** I like starting from like, starting from the downloadable, like what's the thing, what would be like the asset that would support your, you know, like don't think of the search volume or don't think of where the, I mean, thinking of where the traffic already is is helpful, but especially if it's coming from email or somewhere else, it's like, what would be the thing that if people were, if people knew about it, that it would really support your, like pushing them into that demo, like what can you tell them?

**Jakub Rudnik:** And then

**Jakub Rudnik:** And it's like, from there, how do we surface that thing over and over?

**Jakub Rudnik:** So that's through your email, through blog CTAs and stuff.

**Jakub Rudnik:** So I don't know.

**Jakub Rudnik:** I think a checklist is like a good starting place.

**Jakub Rudnik:** That one's pretty simple too and can be reused a lot of different ways.

**Jakub Rudnik:** Probably easier than like doing a full report or something.

**Carmel Schetrit:** If you want to go through like your...

**Carmel Schetrit:** a report would be amazing, but that is hard.

**Jakub Rudnik:** Way more of a lift.

**Carmel Schetrit:** I would definitely start.

**Carmel Schetrit:** And there's like the ROI calculator that we want to do, but it's also a big project.

**Jakub Rudnik:** Have you like written up anything for that ROI calculator or like scoped it at all at this point?

**Carmel Schetrit:** No, we have like Shalom was also thinking about it.

**Carmel Schetrit:** We haven't scoped it.

**Carmel Schetrit:** We saw like two examples.

**Carmel Schetrit:** One Salesforce does it with their agent.

**Carmel Schetrit:** And then we saw this other example, but it would basically be, I think, on yeah, like time.

**Carmel Schetrit:** I'm saving per...

**Carmel Schetrit:** Employee, something like that.

**Jakub Rudnik:** That was one of the chat gave me like one of, gave me that as a possible like CTA and we, I knew we didn't have that asset.

**Carmel Schetrit:** So like, yeah, because I think that would work well.

**Carmel Schetrit:** It's just like, I need to, I don't have the bandwidth currently.

**Jakub Rudnik:** Did I send you, I think it's easier than ever with like vibe coding and things.

**Jakub Rudnik:** There's also, I can't remember if I sent it to you or I'm just crossing all my wires, but there's like, sent me something.

**Jakub Rudnik:** There's a tool that can do it more easily.

**Jakub Rudnik:** Like if you have the math you want it to do, then it's like they, you can embed it.

**Carmel Schetrit:** That's just like a $30 a month tool.

**Carmel Schetrit:** No, I don't know if I got that.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** I'll have to find it.

**Jakub Rudnik:** I'll put that as an action item for myself, but it's like, there's no coding.

**Jakub Rudnik:** That's more of embedding.

**Jakub Rudnik:** And so then you can just put on a landing page and like, see how much time you can save for employee that becomes your CTA, you know?

**Jakub Rudnik:** And it's, so I will come back to that.

**Jakub Rudnik:** It's something that like, my friend who runs content somewhere else has used a bunch.

**Jakub Rudnik:** And I always ask him like every time,

**Jakub Rudnik:** I have a conversation.

**Jakub Rudnik:** that's a textimony.

**Jakub Rudnik:** He sends it right back to me.

**Jakub Rudnik:** So I'll send that over, but it's actually, that might actually be more of a easier thing to stand up.

**Jakub Rudnik:** But if we do have a, an asset that you feel really strong about, there is some support that we can offer or definitely some guidance on how to use it.

**Carmel Schetrit:** let me think, let me think a little bit more about, about that.

**Carmel Schetrit:** Sounds good.

**Carmel Schetrit:** The other thing I wanted to talk about.

**Carmel Schetrit:** Oh, uh, okay.

**Carmel Schetrit:** I have two things.

**Carmel Schetrit:** So the first one I sent over some data, but then I pulled some more data and I want to walk you through it and I can pull, I can export all of it, but I just want to first, like, before I inundate you see what's helpful and what's not.

**Carmel Schetrit:** So first of all, I can export, I don't want unique views.

**Carmel Schetrit:** I can do total count.

**Carmel Schetrit:** Um,

**Carmel Schetrit:** Do we want to see what tools pages are getting the most views?

**Jakub Rudnik:** Yeah, somewhat useful for sure.

**Carmel Schetrit:** Should I send this?

**Carmel Schetrit:** Mm-hmm.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** So that's one.

**Carmel Schetrit:** Two, I'll pull this later.

**Carmel Schetrit:** The blog clicks are really hard.

**Carmel Schetrit:** We had to, like, do some weird workaround, and I don't know how accurate it is.

**Carmel Schetrit:** We had to do, like, the referring domain after they click isn't blog meet.

**Carmel Schetrit:** Like, it's a bit weird, and I don't know how accurate it is because, I don't know, it seems so low.

**Carmel Schetrit:** Like, eight clicks was the highest in October on chatbot use cases.

**Carmel Schetrit:** I'm not sure.

**Carmel Schetrit:** I don't know how much interaction we get with our blog.

**Carmel Schetrit:** I did...

**Carmel Schetrit:** ...

**Carmel Schetrit:** Don't think I pulled this for you, but if you find this useful, I will, like, put it in a, did I do that?

**Carmel Schetrit:** I can't remember now.

**Jakub Rudnik:** It's, that's definitely not accurate, like, some of your blogs have, like, you have a blog with 100 clicks in the last 30 days organically alone, so something's off there.

**Carmel Schetrit:** Really?

**Carmel Schetrit:** and so you're seeing this through the GrowthX?

**Jakub Rudnik:** I just did a quick look at Search Console.

**Carmel Schetrit:** Hold on, Search Console, okay.

**Carmel Schetrit:** So then I need to find this in, okay.

**Carmel Schetrit:** Can you show me, actually, where you put, where you saw that in Search Console?

**Jakub Rudnik:** Mm-hmm, mm-hmm, yeah, where is it?

**Jakub Rudnik:** So I just went, see, 20 days, page, slash, blog.

**Jakub Rudnik:** And then down to Pages.

**Carmel Schetrit:** And

**Carmel Schetrit:** I see.

**Carmel Schetrit:** I see.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** Very interesting to be, I had to do this for like website traffic, like piecing together Google Analytics with PostHog because Google Analytics is also not accurate for it.

**Jakub Rudnik:** I stopped using it.

**Jakub Rudnik:** So then I ended up getting a little bit blind because I'm only really looking at organic through GSC.

**Carmel Schetrit:** PostHog looked better.

**Jakub Rudnik:** Okay.

**Carmel Schetrit:** will use that.

**Carmel Schetrit:** But yeah, for clicks, PostHog is kind of annoying.

**Carmel Schetrit:** And then I shared, oh, I didn't share this, but this is also interesting.

**Carmel Schetrit:** I pulled all the referring traffic to the blog, which is also interesting for us to see in general.

**Carmel Schetrit:** I don't think it's super surprising.

**Carmel Schetrit:** And I think you actually have this in your own look or down, right?

**Jakub Rudnik:** We have just the L1 referrals.

**Jakub Rudnik:** So any other source doesn't show like we wouldn't see DuckDuck.com.

**Jakub Rudnik:** Go specifically, but a lot of these are represented there, yeah.

**Carmel Schetrit:** Okay, cool.

**Carmel Schetrit:** And then, that's it.

**Jakub Rudnik:** And then I sent you the most viewed stuff as well.

**Jakub Rudnik:** Can you go back one screen from here?

**Jakub Rudnik:** There's a look that I wanted to create.

**Jakub Rudnik:** I'm not literate in the post talk yet.

**Jakub Rudnik:** Yeah, this is what I wanted.

**Jakub Rudnik:** Do you demo by refer or?

**Carmel Schetrit:** This one is really hard.

**Carmel Schetrit:** It's what I was trying to create a path to see where people are landing, where they're coming from and landing on the demo page.

**Carmel Schetrit:** But it's not great.

**Jakub Rudnik:** Yeah, that's, if you ever get there, whether that's like view the demo or request demo or the sign up when I'm, I was a mixed panel person at my last call.

**Carmel Schetrit:** I don't think it's be that hard, but it is really hard.

**Jakub Rudnik:** in, yeah, in Mixed Funnel, was like first, first viewed page, and I would set it to blog, and then the funnel stage was, you know, view demo or whatever it was.

**Jakub Rudnik:** So, yeah, obviously very different tools.

**Jakub Rudnik:** But if you end up finding that, I swear I've seen that data from you before, but I haven't been able to find it in the Slack.

**Jakub Rudnik:** So I'm not sure what it was called.

**Jakub Rudnik:** I'll keep looking back, and maybe it would have like the path in the title of the, so do another look.

**Jakub Rudnik:** I actually have an idea on how to find it again.

**Jakub Rudnik:** So, but if you can figure that out, that would be the conversion level data that we can see where people are originating at least.

**Jakub Rudnik:** But the traffic itself will still be helpful in the sources.

**Carmel Schetrit:** Okay, cool.

**matt:** go.

**matt:** go.

**matt:** So, let's

**matt:** Carmel, you mentioned one more thing about the features and killing the videos.

**Carmel Schetrit:** Oh, yes.

**Carmel Schetrit:** Oh, there's another, okay, I have two more things.

**Carmel Schetrit:** One other thing is, have you guys seen this report thing from Amplitude?

**Carmel Schetrit:** Oh, , I'm sorry, I know we're over.

**matt:** It's all good.

**Jakub Rudnik:** Yeah, all good.

**Carmel Schetrit:** Did you guys see Amplitude has this, like, landing page where you get your AI visibility report?

**Carmel Schetrit:** I don't know how credible it is.

**Carmel Schetrit:** But I think they got our product wrong, so, like, I'm not, like, the competitor mentions and stuff.

**Carmel Schetrit:** I'm not sure how accurate this is and, like, the topics by visibility stuff, like, I just, I don't know.

**Carmel Schetrit:** But I thought the sources here might be interesting.

**Carmel Schetrit:** I can send you guys this report.

**Carmel Schetrit:** But works, so.

**Carmel Schetrit:** can know,

**Carmel Schetrit:** I just didn't know if you guys have heard of it and if it's an incredible source.

**Jakub Rudnik:** I haven't seen this free version of their product, essentially.

**Jakub Rudnik:** I haven't seen this landing page.

**Jakub Rudnik:** It's a really smart growth play by them.

**Carmel Schetrit:** Yeah, I'm sure people are filling it out left and right.

**Jakub Rudnik:** We've set up, we're using Scrunch for this type of reporting for clients.

**Carmel Schetrit:** Have we shown you Scrunch?

**Jakub Rudnik:** No.

**Jakub Rudnik:** Oh my gosh.

**Jakub Rudnik:** Well, let me, I can share my screen, what we've got set up.

**Jakub Rudnik:** There's probably some more work to be done on things.

**Jakub Rudnik:** What we've done, Scrunch's got like competitive presence, the brands that you're competing against content-wise.

**Jakub Rudnik:** We set these up where you're fitting in the citations that you do have, the actual number of citations.

**Carmel Schetrit:** this the gap analysis?

**Carmel Schetrit:** I forgot her name from yesterday I was talking about.

**Jakub Rudnik:** Andy, yeah, this is the tool that she was referencing.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** And so...

**Jakub Rudnik:** So we set up a number of prompts.

**Jakub Rudnik:** It's probably worth going through.

**Jakub Rudnik:** Matt, do you know if you set this up, if I set this up, if it was?

**Jakub Rudnik:** It wasn't way before me.

**Jakub Rudnik:** It might have been Andy, actually.

**Jakub Rudnik:** Yeah, possibly.

**Jakub Rudnik:** So we've got high-level clusters or topics that you can see here.

**Jakub Rudnik:** And then there's individual prompts that come behind.

**Jakub Rudnik:** basically, Scrunch is pinging ChatGVT, Perplexi, AIO reviews for these each day and tracking your visibility within these topics over time.

**Jakub Rudnik:** And so we're watching these pieces.

**Jakub Rudnik:** We should probably make sure that it's aligned to the content that we've done more recently.

**Jakub Rudnik:** That's what I end up finding is, like, if it's set up originally and we go into new clusters or areas, then sometimes that's lost.

**Jakub Rudnik:** It does give us some insights on what we can do differently, what prompts here.

**Jakub Rudnik:** So it's probably worth it.

**Jakub Rudnik:** Exporting this or showing you some of this, these pieces.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** at individual URLs.

**Jakub Rudnik:** It's probably worth doing with like a tools page and a blog post and seeing what recommendations it has.

**Jakub Rudnik:** The reporting and like how I interpret and actually is still a learning process.

**Jakub Rudnik:** Like it's so we've been using this for a couple of months, but it's just, you know, this is all new for everybody.

**Jakub Rudnik:** So, yeah, we'll make a point to report on this more.

**Jakub Rudnik:** I'm sorry, I haven't brought this up.

**Jakub Rudnik:** I'll put my hand up that we haven't done that.

**Carmel Schetrit:** Is it showing the top brands based off of like what we're competing in terms of keywords?

**Carmel Schetrit:** Or is it people that we manually, like competitors we manually entered?

**Jakub Rudnik:** I want to say it's that we've manually entered, but I will have to confirm that.

**Carmel Schetrit:** So we could probably add more in there.

**Jakub Rudnik:** Yeah.

**Jakub Rudnik:** Yes.

**Jakub Rudnik:** So.

**Jakub Rudnik:** Cool.

**Jakub Rudnik:** Let's look at that.

**Jakub Rudnik:** Maybe we spend some time next week confirming some of these are set up properly.

**Carmel Schetrit:** This is a cool tool.

**Jakub Rudnik:** I've never heard of it.

**Jakub Rudnik:** That's awesome.

**Jakub Rudnik:** There's a lot.

**Jakub Rudnik:** mean, Carmel, it has actually slowed down, but like my first three or six months here, was like every other day, somebody on LinkedIn DMed do you want to test this out?

**Jakub Rudnik:** Do you want to get a discount on our beta launch?

**Jakub Rudnik:** There's like 150 of these out of nowhere.

**Jakub Rudnik:** Everyone's trying to grab that market.

**Jakub Rudnik:** Profound is probably the biggest name one at this point, but maybe that's because like I'm connected to a couple of Profound people.

**Jakub Rudnik:** I can't tell if it's just my visibility or what, but we had a lot of clients ask about them earlier in the summer, probably.

**Jakub Rudnik:** But yeah, there's like, I think literally hundreds of them at this point that are trying to do the same thing.

**Jakub Rudnik:** then like Ahrefs and all these have like done a version of it themselves within their tool.

**Jakub Rudnik:** So yeah.

**Carmel Schetrit:** Crazy and keeping up with all the tools.

**Jakub Rudnik:** .

**Carmel Schetrit:** Um, okay.

**Carmel Schetrit:** So yeah, the last piece was the feature pages.

**Carmel Schetrit:** So remember.

**Carmel Schetrit:** Remember last week I showed you the site remapping?

**Carmel Schetrit:** I showed it to you guys, right?

**Carmel Schetrit:** Like the new structure we're going to have for our website?

**Jakub Rudnik:** No?

**matt:** Oh, .

**matt:** You mentioned that you were planning it, but I don't think we talked more than that.

**Carmel Schetrit:** Okay.

**Carmel Schetrit:** I will be fast, I promise.

**Carmel Schetrit:** So we're working on a rebrand.

**Carmel Schetrit:** A rebrand, complete rehaul of our design and complete rehaul of our web pages.

**Carmel Schetrit:** Um, to fit with a new, like, messaging and positioning, um, with the, like, brand architecture that I mentioned to you guys last week.

**Carmel Schetrit:** So, given that, we are getting rid of a ton of pages, um, and we are going to make our site lean and mean.

**Carmel Schetrit:** Um, I think just having a million pages is quite old school, and so I wanted to talk to you guys about this and get your opinion before I do anything.

**Carmel Schetrit:** First things first, we're getting rid of the French.

**Carmel Schetrit:** It's just that's not going to work for us, and so we'll redirect to the English website.

**Carmel Schetrit:** That's one.

**Carmel Schetrit:** Two, this is going to be the new structure.

**Carmel Schetrit:** We'll have the homepage.

**Carmel Schetrit:** We'll have a product tab that has these three product pages on request management, workflows, and agents, and then we'll have the integrations page.

**Carmel Schetrit:** We'll have the customer stories page.

**Carmel Schetrit:** Ignore this.

**Carmel Schetrit:** This is just like filters I was thinking we could have, but anyways, customer stories page, pricing page, and then our resources pages, which some of them are TBD, like these two pages.

**Carmel Schetrit:** Sorry, the migrate to see, like, I don't know.

**Carmel Schetrit:** And then we killed already if I did not show you this.

**Carmel Schetrit:** We shortened the product tab already, so you...

**Carmel Schetrit:** You can't access the features pages that used to be here anymore.

**Carmel Schetrit:** It was this like long scroll of features and the pages still exist and we didn't create redirects for them yet.

**Carmel Schetrit:** But I don't think we're going to be maintaining them and they're also  pages.

**Carmel Schetrit:** And so I wanted to call this out with you guys, A, to understand from like a traffic perspective if I'm shooting myself in the foot.

**Carmel Schetrit:** And B, if what we think our strategy should be moving forward on articles because we link out to these feature pages a lot, but like they're really useless pages.

**Jakub Rudnik:** From a traffic perspective, could you send me the URLs features?

**Jakub Rudnik:** I know I've seen them before, but if you would just send me the list over and I can check those.

**Jakub Rudnik:** We would, assuming that the traffic's pretty low, which they typically are on a service page, figure out where the best redirects are, probably somewhere just in the product tab.

**Jakub Rudnik:** And...

**Jakub Rudnik:** And then, but it would be a matter of fixing or updating the internal links.

**Jakub Rudnik:** And then, obviously, like, working with our systems, make sure we're not doing that going forward and, like, the content team.

**Jakub Rudnik:** So, yeah, just be a confirmation.

**Carmel Schetrit:** I create a lot of work for you?

**Jakub Rudnik:** That depends on how many times we've linked them.

**Jakub Rudnik:** It's not that bad, though.

**Carmel Schetrit:** It's pretty straightforward.

**Jakub Rudnik:** I just think, correct me if I'm wrong, but, like, doing a lot of research and looking at a lot of other SaaS websites, like, no one does the one million pages anymore of, like, a page for each feature, like, you know, we had set up.

**Jakub Rudnik:** And they set this website up thinking about marketing in 2016, I think.

**Jakub Rudnik:** Yeah, when I was at ActiveCampaign, they had all those, and we had, like, the most outdated marketing and website.

**Jakub Rudnik:** And that was, like, that's what that reminds me of.

**Jakub Rudnik:** So, I think there's, like, reasons for a product, especially if there's, like, organic around that very specific feature.

**Jakub Rudnik:** But typically, there's not, and you're, like...

**Jakub Rudnik:** Writing all these things that people aren't necessarily looking for.

**Jakub Rudnik:** And you can cover a lot of that in the blog type of strategy too.

**Jakub Rudnik:** Or like do it as a landing page separate and do a different type of play.

**Jakub Rudnik:** So generally in agreement, just with a little bit more research to do.

**Jakub Rudnik:** But not a terrible amount of work.

**Carmel Schetrit:** Okay, let me send you the pages.

**Carmel Schetrit:** I really don't think that they get a lot of traffic, but you can confirm and I can create.

**Carmel Schetrit:** I know where we can redirect most of them, so that's not a problem.

**Carmel Schetrit:** I just, moving forward on the blog side, think of a solution for that.

**Jakub Rudnik:** Sounds good.

**Carmel Schetrit:** I was going to pull up the teaser for you guys, the Figma file with the new branding, but I can't find it now.

**Carmel Schetrit:** I'll show it to you guys next time.

**Jakub Rudnik:** Excited for it.

**Carmel Schetrit:** I have a nice surprise.

**Carmel Schetrit:** All right, cool.

**Carmel Schetrit:** Okay, so I need to send you some data points.

**Carmel Schetrit:** Stuff that I'll pull, I'll send you these links too.

**Carmel Schetrit:** What else do I need to do?

**Jakub Rudnik:** Just review the copy for the CTAs and then...

**Jakub Rudnik:** And the copy for the CTAs.

**Carmel Schetrit:** Okay.

**Jakub Rudnik:** Sweet.

**Carmel Schetrit:** Thanks, guys.

**matt:** Thanks, Carmel.

**Carmel Schetrit:** Thanks.

**Jakub Rudnik:** Bye.

**matt:** Bye.
