# Augment Code <> GrowthX Weekly Sync

<metadata>
date: 2025-12-10
time: 18:00 UTC
duration: 21 minutes
organizer: liz@growthx.ai
participants: Jason Gong (GrowthX), Liz Kushnereit (GrowthX), Sylvain Giuliani (Augment Code)
fathom_recording_id: 107783533
fathom_url: https://fathom.video/calls/501042480
share_url: https://fathom.video/share/4zpRWGhd7eMBd3Eq-cMDmnKp1t7VTmDC
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Augment Code and GrowthX reviewed performance metrics showing a ~50% drop in branded search clicks since mid-August, linked to reduced awareness marketing and a strategic pricing shift targeting professional users. Despite overall content traffic growth, the team addressed concerns about bot activity in "direct" traffic, agreed on new web development approval processes to prevent site-wide bugs, and aligned on P0 priorities: growing content traffic and improving conversion rates. Jason committed to analyzing traffic sources in PostHog, Liz committed to weekly traffic audits and two deliverables by Dec 15 (SEO readout and code review post-mortem), and the CTA experiment will run through EOY given inconclusive results at 15k views.

---

## Context

This is a weekly sync between Augment Code (led by Sylvain Giuliani) and GrowthX, GrowthX's primary content and marketing partner for Augment Code. GrowthX has been engaged to drive SEO, content strategy, and web optimization for Augment Code's website — a critical channel as the company competes in the AI code editor market alongside tools like Cursor and Windsurf. The meeting occurs as Augment Code faces headwinds in search demand (likely tied to broader "AI fatigue" in the market) and conversion challenges despite growing organic traffic. GrowthX's team includes Jason Gong (analytics/strategy), Liz Kushnereit (content lead, organizer), and George Haikal (also listed as attendee but not participating in discussion); Augment Code is represented by Sylvain Giuliani. The meeting covers performance diagnostics, content production plans, web development process improvements, and CTA testing results.

---

## Relevance

**To GrowthX Delivery:**
- New process introduced: global web changes (beyond per-page overrides) now require review and approval from Megan or Sylvain before deployment, with a shared example of a table formatting bug that broke site-wide. This establishes a gate for quality control on GrowthX's backend changes.
- Content production velocity: ~15 refreshes per week; Liz will implement weekly traffic audits to map traffic spikes to specific refresh cohorts and double down on winners.
- Team structure shift to "pool model" with specialized experts (Ed on some areas, Talal on content strategy) instead of generalist approach; implications for service delivery and resource allocation.
- PostHog integration for bot/real user differentiation: Jason will investigate untracked "direct" traffic and provide insights on session behavior (region, recording patterns) to validate traffic quality.

**To GrowthX Business Development:**
- Account health signal: Augment Code is facing market headwinds (AI fatigue, reduced search volume market-wide) but still investing in content strategy and optimization, suggesting commitment to SEO as a long-term channel.
- Expansion potential: Discussion of gated content for enterprise persona and 2026 roadmapping suggests expansion plans; GrowthX may be positioned to support new content verticals or segments.
- Conversion challenges despite traffic growth: High-traffic articles failing to convert indicates a potential services expansion opportunity (landing page optimization, funnel strategy, CRO consulting).

**To CheckThat:**
- Implicit validation of AEO/keyword visibility trends: team references Google Trends and Ahrefs showing market-wide fatigue in AI code editor category, corroborating CheckThat's market research capabilities.

---

## Overview

- **Branded Search Down \~50%:** A mid-August drop in branded search clicks is linked to a pullback in awareness marketing (e.g., YouTube ads) and a strategic shift to target professional users, which reduced the total addressable market.
- **Content Traffic Spiking:** Overall content traffic is up, but a large portion is untracked "direct" traffic, suggesting bot activity. GrowthX will investigate user behavior via PostHog to differentiate real engagement from noise.
- **New Web Dev Process:** To prevent site-wide issues (like a recent table formatting bug), all global web changes now require review and approval from Megan or Sylvain before deployment.
- **CTA Experiment Inconclusive:** The current CTA experiment is statistically insignificant after 15k views, with the control group slightly ahead. It will run until EOY to gather more data before a decision is made.

---

## Key Topics

### SEO Performance & Branded Search Drop

  - **Problem:** Branded search clicks dropped \~50% since mid-August, impacting the homepage and pricing page.
  - **Analysis:** This timeline aligns with two strategic shifts:
      - **Reduced Awareness Marketing:** A pullback in YouTube ads and other awareness campaigns.
      - **Pricing Change:** A strategic focus on professional users, which reduced the total addressable market.
  - **Hypothesis:** These factors compounded, leading to fewer searches from the "scrappy developer" segment.
  - **Context:** The broader market shows signs of "AI fatigue," with competitors like Cursor and Warp also seeing search trends decline (per Google Trends/Ahrefs).

### Content Performance & Optimization

  - **Organic Traffic Spike:** A large traffic spike is occurring across several articles.
      - **Concern:** A significant portion is untracked "direct" traffic, raising suspicion of bot activity.
      - **Action:** GrowthX will use PostHog to analyze user behavior (e.g., region, session recordings) and differentiate real engagement from noise.
  - **Conversion Gap:** High-traffic articles are not converting visitors effectively.
      - **Action:** GrowthX is rewriting top-performing articles to improve quality and conversion.
  - **Content Production:** The team is publishing \~15 content refreshes per week.
      - **Action:** Liz will conduct weekly audits to map traffic spikes to specific refreshes and double down on successful formats.

### Web Development & Process

  - **New Review Process:** To prevent site-wide issues like a recent table formatting bug caused by a global change in Sanity, a new process is in place:
      - **Default:** Per-page overrides are the standard for all changes.
      - **Global Changes:** Any unavoidable global changes require review and approval from Megan or Sylvain.
  - **Content Quality Improvements:** Recent PRs include new components to improve SEO and user experience:
      - TLDR component
      - Optimized code snippets
      - FAQ module

### Team & Priorities

  - **Team Structure:** GrowthX is moving to a "pool model" with specialized experts (e.g., Ed, Talal) to ensure the right person works on each task.
  - **Top Priorities (P0):**
    1.  **Grow Traffic:** Improve content quality and layouts.
    2.  **Improve Conversion:** Optimize the site to convert the new traffic.
  - **Data Integrity:** Sylvain's team will conduct a full audit and cleanup of conversion events in PostHog between now and January to ensure reliable data for analysis.

---

## Action Items

**Jason Gong (GrowthX)**
- Analyze recent traffic spike in PostHog; share findings with Sylvain

**Liz Kushnereit (GrowthX)**
- Draft 'Augment Code pricing' content to control branded SERP
- Start weekly traffic audit; map traffic spikes to content refreshes
- Tag Megan/Sylvain on all global web changes; default to per-page overrides
- Let CTA experiment run until Dec 31; decide on winner based on results
- Send Sylvain two 1-pagers by Dec 15: SEO readout + Code Review post-mortem

---

## Transcript
**Sylvain Giuliani:** Hey, Jason.

**Jason Gong:** Hey.

**Jason Gong:** How's it going?

**Sylvain Giuliani:** Good.

**Sylvain Giuliani:** I'm surviving in the deep, deep winter on those hills.

**Jason Gong:** It is cold.

**Jason Gong:** You have so many hat-hoodie combinations.

**Jason Gong:** I feel like that's the uniform.

**Sylvain Giuliani:** It's very much is.

**Sylvain Giuliani:** I think I have like 50 hats, like something like that.

**Sylvain Giuliani:** Like it's just, it became a thing now, you know.

**Sylvain Giuliani:** But yes, yes.

**Sylvain Giuliani:** All right.

**Sylvain Giuliani:** I was going to say it's the last of the year, but no, I'm still here next week.

**Sylvain Giuliani:** The week after that, I'm gone like for the rest of the year until the 5th.

**Sylvain Giuliani:** So I'll probably skip the Christmas one.

**Jason Gong:** yeah.

**Jason Gong:** Going anywhere nice for the holidays?

**Jason Gong:** I know.

**Sylvain Giuliani:** No, just like shutting down my brain.

**Sylvain Giuliani:** Well, I mean, maybe going to LA, but I don't think that's going anywhere, really.

**Sylvain Giuliani:** It's like same, same, but different.

**Sylvain Giuliani:** But yeah.

**Jason Gong:** I think we're going to San Diego or at least that's the plan.

**Jason Gong:** I don't know.

**Sylvain Giuliani:** It'll materialize.

**Sylvain Giuliani:** Yes, yes, yes.

**Jason Gong:** So quick, quick data review.

**Jason Gong:** I want to talk about some changes.

**Jason Gong:** Like, yeah, we also have some quiet weeks.

**Jason Gong:** And then we dug into the kind of overall organic traffic to your whole site.

**Jason Gong:** And then Liz will update on quite a lot of the other stuff we're working on.

**Jason Gong:** That's what we're getting today.

**Jason Gong:** So we, I mean, it's hard to see, but we're getting like a huge spike to our content.

**Jason Gong:** It's kind of happening to like a few articles, but also just overall.

**Jason Gong:** I still feel like some of it's got to be bot traffic, but I'm not complaining.

**Jason Gong:** The SEO line is still growing a lot too, but just the percentage of people that come with zero tracking is like, I don't know, something fishy.

**Sylvain Giuliani:** But, you know, again, they're looking at the page.

**Sylvain Giuliani:** If you look at the people from that spike, is there anything specific from them?

**Sylvain Giuliani:** Like, you know, like if you go on PostHog and look user by user, like, you know, like, do they do, you know, are there like different region?

**Sylvain Giuliani:** Like, you know, there's like session record on it.

**Jason Gong:** So it's kind of like, you can maybe look at like, what are they doing on the website?

**Sylvain Giuliani:** Like, obviously to me, it's like, a lot of it is direct traffic.

**Sylvain Giuliani:** So like, you know, that's like a red flag right there, you know?

**Sylvain Giuliani:** Like, you know, I mean, what this is like.

**Jason Gong:** This is the person, and then yeah, this is a 30 day view.

**Jason Gong:** So, yeah, they're reading some content.

**Jason Gong:** It looks like the latest event is an ad, but they read the content first.

**Sylvain Giuliani:** Do you think it's, like, retargeted or something, maybe?

**Sylvain Giuliani:** We retargeted them, but oh, maybe it's like a search brand.

**Sylvain Giuliani:** Like, you they land there, they remember augment code, they Google augment code, they click the ad, you know?

**Sylvain Giuliani:** I mean, this person looks...

**Jason Gong:** It's like a real human.

**Sylvain Giuliani:** Yeah, like, they just have the tab open, and, you know, every time they open their laptop, it refreshes the page, right?

**Jason Gong:** Like, I mean, that's kind of, what it feels.

**Jason Gong:** Okay.

**Jason Gong:** Okay, I mean, I think this will probably take a little bit of time, but I think it's a good call.

**Sylvain Giuliani:** Yeah, yeah, I think we can try to unpack that.

**Sylvain Giuliani:** Yeah, it would be good to understand a bit better.

**Jason Gong:** Yeah, but in fact, some of the articles were particularly getting a lot of traffic and impressions as well, so we're doubling down and rewriting.

**Jason Gong:** I don't think what we're doing on conversion is working yet, but it's still just crazy to me that this article gets so many real visitors and we can't convert them, so we're just continuing to iterate there.

**Jason Gong:** So that's what we're working on.

**Jason Gong:** Quick update on work streams.

**Jason Gong:** So the main thing that'll change in the coming weeks is we have more experts on the team now.

**Jason Gong:** You've seen Ed, you haven't met Talal yet, but he's been working on the content strategy.

**Jason Gong:** And going forward, we're just going to pull them in more.

**Jason Gong:** And then, you know, I'm still here, obviously, but like Liz is the main content.

**Jason Gong:** So some of the people we just hired recently is we got to a lot of those like kind of the SEO, developer, marketing, GitHub, Sentry, and this YC startup is actually in my batch.

**Jason Gong:** And then we have Kirkland who's like working on workflows.

**Jason Gong:** Ads on web, I'm kind of like, you treat me as like a generalist.

**Jason Gong:** And yeah, so you're going to see new faces in some of weeks I won't be here.

**Jason Gong:** But, you know, we're kind of going to this pool model where like the right person works on it.

**Sylvain Giuliani:** In terms of content, how much are we producing recently? Like, what's the content production and content updates on a weekly basis?

**Jason Gong:** I think, yeah, Liz can give an update on that.

**Jason Gong:** But just very quickly, I want to just do this.

**Jason Gong:** I think it was fresh to my mind.

**Jason Gong:** We just looked at it.

**Jason Gong:** So the general story is like less people are Googling for Augment Code.

**Jason Gong:** So when you unpack it, what clicks overall — the last three months versus three months before — looks like it's essentially down by almost 50%, impressions are a little bit up.

**Jason Gong:** When you unpack that, like almost all of it is coming from the homepage, it's happening to the pricing page, your CLI page is getting more traffic, and then some of the content we're doing, you know, is obviously getting more traffic.

**Jason Gong:** Because you see the line that we report every week, like when you start unpacking, like the homepage and pricing, like this is the stuff we see, like just less people search for augment code, and as kind of direct result, less people click it.

**Jason Gong:** So for our content strategy, nothing in particular changes — we're just continuing to iterate as Liz has documented.

**Jason Gong:** But this branded search drop, I mean, honestly — why do people search for Augment Code a little bit less?

**Jason Gong:** I guess ChatGPT could be some of the reason, but I don't know if it's competitive.

**Jason Gong:** I don't know what you see, but, you know, at previous companies I've been at, generally, less people search for you.

**Jason Gong:** It's kind of hard to unpack, but it's, you know.

**Sylvain Giuliani:** Yeah, yeah.

**Sylvain Giuliani:** I mean, that makes sense.

**Sylvain Giuliani:** That makes sense.

**Sylvain Giuliani:** I mean, when did it start?

**Sylvain Giuliani:** I'd like to drop more or less on like the branded search.

**Jason Gong:** I mean, don't, like, do you have a timeline?

**Jason Gong:** Let's see.

**Jason Gong:** Yeah.

**Jason Gong:** Let's see.

**Jason Gong:** We just looked at the homepage, for example. Looks like you grew a bunch here and then mid-August, late-August looks to be the big drop.

**Jason Gong:** Does that have anything to do with the ads at all? I mean, I know Cursor raised a bunch of money when they're going through all their stuff.

**Sylvain Giuliani:** Yeah, I mean, around that time is when we pulled back tremendously from influencer marketing and awareness advertising — things like YouTube ad budget. I was against the idea, but the decision was made, and that's kind of interesting.

**Sylvain Giuliani:** I mean, obviously, it's not, I doubt it's only that, but it's kind of, like, yeah.

**Sylvain Giuliani:** We had less awareness, less people searching for us, then we did the pricing change, which from a brand perspective reduced the number of scrappy developers looking for us.

**Sylvain Giuliani:** So it's kind of like there's a compounding effect, but like, yeah, that's kind of what I was like, yeah.

**Sylvain Giuliani:** If you had to ask me like when would it drop, I would have said probably like, you know, mid-late August is kind of like when we started like doing those changes, right?

**Jason Gong:** yeah, I guess if you're narrowing down on like more professional users, it's just a smaller group.

**Jason Gong:** I remember we did a YouTube survey because nobody clicks the link in the description. We ran a very annoying survey that nobody could skip, and roughly, the real impact is like two or three times what you see attributed directly.

**Sylvain Giuliani:** Yeah, we ran that survey for about two weeks when we had enough volume. A lot of people said word of mouth, friends, and community, not YouTube ads. There were like five or six options.

**Sylvain Giuliani:** And so, but yeah, yeah, like, it's, maybe it's worth doing it and comparing, like, the ranking between now and then, maybe a good thing.

**Jason Gong:** Yeah, cool.

**Jason Gong:** I was trying to see if Cursor or Windsurf changed in that period, but we don't have that information.

**Sylvain Giuliani:** If you use Google Trends as a high-level proxy, you'd see fatigue on the market across Cursor, Windsurf, Augment Code. Same story on Ahrefs. There's definitely fatigue across the market.

**Sylvain Giuliani:** When we go to events and conferences, people say "oh, another AI company." We've been hyping AI for a year in developer land.

**Sylvain Giuliani:** So, I think there's like a bunch of things like that.

**Sylvain Giuliani:** But, again, it's good to know, thanks for confirming this.

**Sylvain Giuliani:** Okay.

**Jason Gong:** Anything else on the SEO analysis?

**Jason Gong:** No, that's basically good.

**Sylvain Giuliani:** I mean, we kind of unpack this a little bit more, but I think, like, you know, 80% of it is just from that.

**Jason Gong:** So, yeah, let us know.

**Jason Gong:** If you want this to be a little bit more shareable, we can, like, throw it into a doc or something.

**Sylvain Giuliani:** Yeah, would be good if you put that into it, like, so I can, like, share internally.

**Jason Gong:** Liz, do you want to update on the content we're producing?

**Liz Kushnereit:** Yeah, sure.

**Liz Kushnereit:** So just to reiterate, this is like sort of attempts to respond to some of that traffic, and we're already doing a lot of it.

**Liz Kushnereit:** I think there's a little bit of room for optimization, like maybe we can build out an actual keyword for augment code pricing and try to control that a little bit more.

**Liz Kushnereit:** But by and large, this is all built into our refresh strategy, and then we have some preliminary results here with the effect of that, so that traffic increasing last week.

**Liz Kushnereit:** I think probably I'm going to do like a weekly audit of traffic and then see if I can map that to refreshes since we're doing about 15 a week right now.

**Liz Kushnereit:** So that answers that content output question.

**Liz Kushnereit:** And then seeing if we can just continue to build on whatever like is performing best.

**Liz Kushnereit:** So a lot of that's just like overall content, fixing the layouts or making them more optimized, just a lot of hands on deck on working on that.

**Liz Kushnereit:** I think there's a little bit of room to optimize in that competitor space and see how we're performing in the SERP.

**Liz Kushnereit:** But otherwise, for the most part, I think we're moving forward as one would expect in response to that.

**Liz Kushnereit:** Quick note on web and development updates.

**Liz Kushnereit:** So I spoke to our dev this morning.

**Liz Kushnereit:** So the expectation moving forward is that they, for any changes we make, we should always default to per page overrides.

**Liz Kushnereit:** But I think that there are times when a global change is unavoidable.

**Liz Kushnereit:** And this, for example, is something we ran into with tables because of sanity.

**Liz Kushnereit:** So in that case, I do want to ask if we can push those to Megan for review and approval.

**Liz Kushnereit:** Just it's a difficult one because we're trying to overall increase the quality format layout of the content.

**Liz Kushnereit:** And I have, like, one example here of everything else that was in that PR.

**Liz Kushnereit:** We added a TLDR component, optimized code snippets with better language, and we also added an FAQ module to help with SEO.

**Sylvain Giuliani:** Yeah, that makes sense.

**Sylvain Giuliani:** Yeah, mistakes happen. It's about balancing shipping fast with not breaking things. If we can get a quick review from Megan or me — just scanning for issues — I think that works. Tagging us on PRs is fine.

**Liz Kushnereit:** Yeah, I mean, we'll do a better job of, like, putting things that actually are worth your time in front of you, but not also just writing those things off and taking, like, an executive decision on them.

**Liz Kushnereit:** Okay, cool.

**Liz Kushnereit:** That's about it for that.

**Liz Kushnereit:** We're still working forward on content optimization, and then the table optimization, which is a global change.

**Liz Kushnereit:** So we might want to look into that.

**Liz Kushnereit:** Quickly, the CTA experiments, just an FYI, it's still not statistically significant.

**Liz Kushnereit:** I looked this morning and actually the control group is like slightly ahead, but our sample size is about 15,000.

**Liz Kushnereit:** And so I don't know really if that's like good enough.

**Liz Kushnereit:** I say we let it run until the end of the month and then see what that looks like.

**Liz Kushnereit:** Yeah.


**Sylvain Giuliani:** The fact that it's head to head is a strong sign that it doesn't do much. Something should have pulled ahead by now or fallen flat.

**Liz Kushnereit:** Yeah, we'd hope, but there's no harm in letting it run. From a visual perspective, one variant looks better to us, so we can make a decision based on that at the end.

**Liz Kushnereit:** So we can make that decision at the end of the experiment if we want to move forward with one or not the other.

**Liz Kushnereit:** And then we just optimized these.

**Liz Kushnereit:** We've also optimized the CTA and images in articles and updated content formatting.

**Liz Kushnereit:** And then Marisol and our CM are working tirelessly on the refreshes and also our cannibalization strategy.

**Liz Kushnereit:** So she's been, we shared this last week, but she's been working on going through the 301 redirects and making sure that we're not competing with ourselves and causing any issues with indexing.

**Liz Kushnereit:** But all of that initial search that we did on the SEO readout didn't show that there were any like issues there.

**Sylvain Giuliani:** I'm waiting to hear from Jason on the code relaunch this week. We have a call scheduled.

**Liz Kushnereit:** I mean, I spoke to him last week.

**Sylvain Giuliani:** Yeah.

**Sylvain Giuliani:** It's on hold, but the code review launch is happening this week, so I'll follow up with him on Friday.

**Liz Kushnereit:** Newsletters are deprioritized for now, but going into Q1, we'll prioritize them as part of 2026 roadmapping.

**Liz Kushnereit:** There's like a lot of like 2026 roadmapping we're trying to move forward with that's on that list.

**Liz Kushnereit:** And just generally exploring kind of gated content for augment for the more enterprise persona.

**Liz Kushnereit:** And yeah, I think that's it.

**Liz Kushnereit:** So I guess we'll only see you next week, but we can kind of start shaping that conversation.

**Liz Kushnereit:** And then in January, hopefully we can like be working towards all of our 2026 goals.

**Sylvain Giuliani:** Cool.

**Sylvain Giuliani:** Quick question on the code review launch. We're doing a post-mortem between Friday and Tuesday. If you could send me what we published for code review — early signs of ranking, traffic, things like that — that would be super helpful.

**Liz Kushnereit:** When do you need that by?

**Sylvain Giuliani:** Monday would be ideal. I'm doing a presentation to the company on Tuesday.

**Sylvain Giuliani:** It's a mini post-mortem — what we did with code review, what we learned. I want to include the SEO metrics there too.

**Liz Kushnereit:** I can give you a one-pager on code review. I can also do a one-pager on the SEO readout if you want both.

**Sylvain Giuliani:** Both would be great. One is a monthly SEO write-up, the other is the code review post-mortem.

**Sylvain Giuliani:** There's a bunch of new things coming up, but we can discuss more next meeting.

**Jason Gong:** I wanted to double-check the priorities. We're focused on growing traffic through content quality improvements and cleanup. That's working well. The bigger concern is conversion — we're getting traffic but not converting. Those are our two P0s.

**Sylvain Giuliani:** From our data side, we're going to do a full refresh and quality check on conversion events. There's something not quite right, so our team will tackle that between now and January. Hopefully we'll have better confidence in our conversion data after that. We'll keep you updated.

**Sylvain Giuliani:** Thanks, talk to you later. Bye.
