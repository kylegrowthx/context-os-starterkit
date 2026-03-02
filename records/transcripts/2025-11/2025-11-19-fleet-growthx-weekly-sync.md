# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-19
time: 20:00 UTC
duration: 30 minutes
organizer: aida@growthxlabs.com
participants: John Jeremiah, Irena Reedy, Erik O'Brien, Aida Knežević
fathom_recording_id: 102939302
fathom_url: https://fathom.video/calls/478522510
share_url: https://fathom.video/share/19HRtk3uMkfszUT1TtuBzHou8aNT-nyu
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

GrowthX and Fleet aligned on three blocking issues: Fleet's website uses client-side rendering (CSR), making it invisible to LLMs and preventing organic ranking; analytics data is unreliable with 60% of October traffic misattributed as "direct" due to missing UTM tracking; and a new messaging framework is needed before scaling production of competitor comparison blogs (target: 5 blogs/week). John Jeremiah (Fleet's new CEO) committed to implementing a UTM framework and pushing the messaging framework, while GrowthX will prioritize the technical SEO audit and investigate the direct traffic anomaly.

---

## Context

Fleet is a mobile device management (MDM) platform that hired GrowthX to fix how it's perceived by LLMs and search engines. The core problem: LLMs think Fleet is not a "real" MDM solution, and the website's architecture uses client-side rendering, making it invisible to AI-powered search. John Jeremiah recently joined Fleet as CEO and is ramping up on the content strategy, messaging, and technical issues. This was his second weekly sync with the GrowthX team—he's learning the strategy, tool stack (Notion for planning, Airtable for the content calendar, Looker for analytics), and identifying blockers to accelerate content production toward a 5-blogs-per-week target.

---

## Relevance

**To GrowthX Delivery:**
- Technical SEO audit is now the top priority. CSR issue directly blocks LLM visibility and organic ranking, and must be diagnosed in the full audit.
- Content production workflow needs a new approval step for messaging/positioning alignment before scaling to 5 blogs/week.
- Client comparison blogs show rapid indexing by LLMs (Aida cited recent Traceable success) and are now a primary strategy, pending messaging framework.

**To CheckThat:**
- Fleet's CSR architecture makes the entire site invisible to LLMs (blank pages without JavaScript execution). This is a critical AEO blocker and a strong use case for CheckThat's AI visibility capabilities.
- 60% of October analytics misattributed as "direct" suggests poor tracking infrastructure—UTM implementation and analytics cleanup are prerequisites for baseline visibility metrics.

**To GrowthX Business Development:**
- John Jeremiah's rapid ramp and focus on removing blockers signals strong commitment. Fleet is actively investing in content strategy and willing to ship fast to gain ranking.
- Competitor comparison blogs are now approved strategy—John cites precedent from Traceable (his previous company) where 8 comparison pages ranked #1 within two weeks. Risk of competitor pushback, but John is aligned on fair, educational approach.

---

## Overview

- **Technical SEO is a major blocker.** Client-side rendering (CSR) makes the site invisible to LLMs, and a technical SEO audit is the top priority to fix this.
- **Analytics data is unreliable.** \~60% of October traffic is misattributed as "direct," likely due to a lack of UTM tracking.
- **A new content strategy is approved.** The team will publish competitor comparison posts to quickly gain organic search authority, pending a new messaging framework.
- **Content production will accelerate.** The target is 5 blogs per week, with 4 already approved for staging and 5 more in progress.

---

## Key Topics

### Technical SEO & Analytics Issues

  - **Problem:** The website's client-side rendering (CSR) makes it invisible to LLMs, which cannot execute JavaScript.
      - **Impact:** This prevents the site from ranking in AI-powered search results.
      - **Example:** John Jeremiah noted the handbook is not indexed by Google, and homepage comparisons are likely unreadable by LLMs.
  - **Problem:** Analytics data is unreliable, with \~60% of October traffic misattributed as "direct" in Looker.
      - **Cause:** A lack of UTM tracking prevents proper source attribution.
      - **Context:** The October data is also skewed by a high-bounce-rate Uber ad campaign.

### Content Strategy & Production

  - **Goal:** Reposition Fleet as a real MDM solution to correct its perception by LLMs.
  - **Method:** Build thematic content clusters with strong internal linking to establish authority.
  - **New Initiative:** Publish competitor comparison posts to quickly gain organic search authority.
      - **Rationale:** John Jeremiah cited a successful precedent at Traceable, where 8 fair comparison pages ranked \#1 for "vs. competitor" terms within two weeks.
  - **Blocker:** A new, concise messaging framework is needed to guide the tone and positioning of these comparison posts.

### Content Production & Workflow

  - **Production Target:** 5 blogs per week.
  - **Status:**
      - **Ready to Publish:** 4 blogs (Brock-approved).
      - **In Progress:** 5 blogs (due EOD this week).
      - **Approved Topics:** 8 (Brock-approved, backlog for future posts).
  - **Approval Workflow:**
      - **Current:** Brock (factual accuracy) & Mike T (design/alignment).
      - **Future:** Must incorporate a new messaging/positioning review step.

---

## Action Items

**Aida Knežević (GrowthX)**
- Stage 4 approved blogs on Fleet site
- Investigate high direct traffic in GA4; share findings with John

**John Jeremiah (Fleet)**
- Define and implement UTM framework for all outbound links
- Push Ashish to finalize messaging framework; then propose comparison blog topics to Brock

**Irena Reedy (Fleet)**
- Push Ashish to finalize messaging framework; then propose comparison blog topics to Brock

---

## Transcript
**Erik O'Brien:** looks like Brock declined.

**Aida Knežević:** Yeah, I think John is joining for the first time, right?

**Erik O'Brien:** I think he is the second time.

**Aida Knežević:** Okay, okay.

**Aida Knežević:** Did we walk him through the notion base?

**Aida Knežević:** Because I did see he didn't have access to it, so.

**Erik O'Brien:** I don't believe so.

**Aida Knežević:** Okay, okay, I can show him that today.

**John Jeremiah:** Thank you, hello.

**Aida Knežević:** Hi.

**John Jeremiah:** Sorry, I'm late.

**Aida Knežević:** No worries.

**Aida Knežević:** How are you?

**John Jeremiah:** I'm overwhelmed.

**John Jeremiah:** How's that?

**Aida Knežević:** That's a good answer.

**John Jeremiah:** Starting of week three and, you know, it's a lot of things to do.

**Aida Knežević:** Yeah, yeah, I bet.

**Irena Reedy:** Yeah, there we go.

**Aida Knežević:** How's it going?

**Aida Knežević:** Good, good.

**Irena Reedy:** How are you?

**Irena Reedy:** I'm well, thank you.

**Aida Knežević:** Great.

**Aida Knežević:** So yeah, John, I realized we were meeting for the first time.

**Aida Knežević:** I wasn't at our sync last week.

**Aida Knežević:** So I'm an editorial account strategist at GrowthX.

**Aida Knežević:** So I developed Fleet's content strategy and content calendar.

**Aida Knežević:** So yeah, it's very nice to meet you.

**John Jeremiah:** Yeah, good to meet you as well.

**John Jeremiah:** I'm getting my feet on the ground, trying to learn our dimension, plan, strategy, what we do, and how we do it.

**Aida Knežević:** Yeah, yeah.

**Aida Knežević:** With that in mind, I actually wanted to start our meeting today by showing you our Notion base.

**Aida Knežević:** So I know that Erik shared our Airtable base with you, but that's just the content calendar.

**Aida Knežević:** We use Notion as a base for everything related to our strategy and the artifacts that we're using for content generation.

**Aida Knežević:** So you should have received an email invite and when you log in, you'll see this and if you go to docs, there are a couple of docs here, they're labeled as in progress, but most of them are sort of done or close to being.

**Aida Knežević:** Probably one of the most important documents here is the content strategy.

**Aida Knežević:** So that kind of outlines what is the core problem that Fleet came to us with and what are we setting out to solve with the content that we're producing.

**Aida Knežević:** We listed out different business objectives, analyzed the existing content on your blog, and analyzed your competitors to see what kind of content they've been publishing.

**Aida Knežević:** For context, the biggest issue that we're trying to solve is the perception by LLMs that Fleet is not a real MDM.

**Aida Knežević:** So that's kind of the North Star of our project is to fix that positioning by publishing a lot of foundational content where we can position Fleet as an MDM solution.

**Aida Knežević:** And then you can see the recommended topic clusters that are part of our strategy, and you can also find those clusters in the content calendar.

**Aida Knežević:** And then we kind of break down what each cluster is supposed to cover and why.

**Aida Knežević:** You can still like if you, you know, when you get the chance, you can leave feedback on this document or any comments that come to mind.

**Aida Knežević:** But this is probably like, if you need to get context quickly on what we've done so far and what like the with that, there's So don't about

**Aida Knežević:** The goal is that we're working towards right now.

**Aida Knežević:** This document is probably the best place to get started.

**John Jeremiah:** So I went straight to your reports and your dashboard.

**John Jeremiah:** Just saying, that's where I went.

**John Jeremiah:** But I read through the clusters, and I noticed it was, at least it was interesting.

**John Jeremiah:** I was curious, how did we pick the cluster?

**John Jeremiah:** I mean, we're working on one cluster right now, right?

**Aida Knežević:** We're trying to balance it across different clusters at the same time.

**John Jeremiah:** When I think of traditional clustering, I'm thinking of a hub-and-spoke model on a website where I've got a central pillar page with a cluster of content that works around it. Is that similar to what we're thinking here?

**Aida Knežević:** Not quite.

**Aida Knežević:** So what we are doing is we group, we're trying to identify topics like clusters where we want to build authority in.

**Aida Knežević:** So there might be multiple pages in a specific cluster that are more in-depth and covering a topic foundationally, and then they branch out into different spokes.

**Aida Knežević:** So a cluster is kind of connected thematically rather than being connected with a single web page.

**John Jeremiah:** But would we have an internal linking strategy between these pages where they're going to be reinforcing each other?

**Aida Knežević:** Yes.

**John Jeremiah:** Have you guys looked at our site architecture? Since everything falls under a large section of articles, have we looked at that or thought about doing anything from a technical SEO perspective on how we organize the content?

**Erik O'Brien:** Yeah, so we've got the request to our analyst team to do a full technical SEO audit. It has taken them a little bit longer than I would hope, but I think we're next in the queue. That should highlight things on the website where improvements may need to be made to increase crawler and LLM visibility. So that audit should be pretty insightful once we are able to get it done.

**John Jeremiah:** It's one of those areas where I'm flying completely blind right now, hoping that the web team and the way we've built and tagged pages is helpful. I know for a fact there are issues—if I do a Google search against our handbook, nothing comes back. I can't tell you why. The robots.txt and metadata all look like they should work. But I don't have a technical analysis tool to do it. So I'm really interested in seeing what comes back from your audit.

**Erik O'Brien:** One thing I did notice is that you guys do client-side rendering for most of the web pages, which is an issue when it comes to LLMs. They're pretty immature compared to Google bots and website crawlers. If you do client-side rendering, they're not able to read or enable JavaScript, so those pages will look like blank pages to them. I did a quick check the other day, and that's something we'll definitely highlight in our full technical analysis.

**John Jeremiah:** Yeah, no, that's going to be incredibly important.

**John Jeremiah:** I know we have the comparisons on our homepage.

**John Jeremiah:** And at least my superficial look at the comparisons is that most likely an LLM wouldn't be able to read it or digest it at all.

**John Jeremiah:** It wouldn't look like anything to an LLM is my first assessment.

**John Jeremiah:** It's interesting.

**John Jeremiah:** I haven't looked at the rest of it, but that's an interesting observation.

**John Jeremiah:** It's something we need to think about because what it really means is that we've built the website for people to read it, not for machines to read it.

**Erik O'Brien:** Yeah, it's essentially once the LLM crawlers started taking over in the last couple of years, it kind of pushed some of the more advanced kind of website optimization.

**Erik O'Brien:** And so, yeah, the client-side rendering issue is something we're noticing with a few different clients and kind of prioritizing it for them and their web teams to fix sooner than later, especially as we focus, you know, our efforts on SEO and GEO.

**Erik O'Brien:** Being blind to the LLMs is a bit of a deterrent for us.

**John Jeremiah:** That's an understatement. It's a huge problem in my view. If we want to rank on either LLMs or even SEO, it doesn't make it easy. I'm sorry—I'm taking over the meeting. I don't mean to. Go ahead, I'll let you run it.

**Aida Knežević:** No worries.

**Aida Knežević:** We have just a couple of updates and then we can get into any questions.

**Aida Knežević:** run run to you I'm you

**Aida Knežević:** Just wanted to give a couple of content updates, so in terms of what's ready to publish, so we have four blogs here that Brock has reviewed, and from a content standpoint, he has approved them, and we can go ahead and stage them on the site, but John, if you also want to take a look, you can find the Google Doc links in Airtable, but those should be ready to publish pretty soon.

**Aida Knežević:** And we're working on five new blogs this week. Brock has approved eight topics total, so we're aiming to deliver these five by end of week. Going forward, we're aiming to deliver five blogs per week.

**John Jeremiah:** Cool.

**John Jeremiah:** And I'm still too new to really be nailed down on our messaging to say, oh, this is good or bad.

**John Jeremiah:** And given Brock's depth of experience, I would defer to him to make sure we're factually correct.

**John Jeremiah:** From a messaging and positioning perspective, I've been talking with Ashish, our new CMO, about how to get to a consolidated message house and framework that we can use as a filter to ensure we're aligning on messaging. Right now, we don't really have a single source of truth for messaging—we do, but it's a 52-page document. That's too much. We're going to get there. Philosophically, I'd rather ship it fast and fix it later than let it sit and not ship it.

**John Jeremiah:** I've shipped things and suddenly had number one organic ranking because I shipped it as opposed to sitting on it. One thing I noticed in my traffic analysis: about 60% of our traffic is listed as direct. I built a Looker dashboard to see the same view as Google Analytics. Are you seeing something similar?

**Aida Knežević:** Sorry, what was the source of traffic?

**John Jeremiah:** Almost two-thirds of our October traffic came from "direct"—not organic, not paid. It's like the traffic came from nowhere to our website. That's a head-scratcher. It seems excessively high.

**Aida Knežević:** Do you, I mean, we can also do the analysis in GA4.

**Aida Knežević:** What are the landing pages that most of that traffic is going to?

**Aida Knežević:** Is it not set traffic?

**John Jeremiah:** It's varied.

**John Jeremiah:** I mean, we can look at traffic by landing page.

**John Jeremiah:** And let's look at direct traffic.

**John Jeremiah:** This is direct traffic.

**John Jeremiah:** And this is, let's zoom out.

**John Jeremiah:** We'll do all of October.

**John Jeremiah:** October was interesting—we ran an Uber ad campaign the first week, and it had an 80-85% bounce rate. The rest of October, we got about 29,000 direct traffic hits. There's also a bunch of other sources. But the point is, I'm scratching my head trying to figure out what's driving all this direct traffic.

**Aida Knežević:** That's a lot of direct traffic. Eric, do you think we could work with the analytics team to investigate?

**John Jeremiah:** Yes, that would be great, thanks. The other thing I noticed: we're not using UTMs on any links as far as I can tell. Irena, is that right?

**Irena Reedy:** No, we're not using UTMs. Unless it's going through Clay—that's been our tracking method.

**John Jeremiah:** Without UTMs, Google can't properly attribute these links. I'm just trying to unpack what might be causing the direct traffic anomaly.

**Aida Knežević:** Are you considering using another analytics tool? We typically default to GA4, but some clients have moved away from it because it's hard to track web traffic properly. We've used PostHog with another client, and I can ask around about other options.

**John Jeremiah:** I hate GA4—Google completely destroyed Google Analytics when they migrated. That's why I built the Looker dashboard. What do your other clients use?

**John Jeremiah:** Unless I had a really good reason, I'd be hesitant to rip it out since GA4 is so universal. Right now I'm more interested in understanding forensically what's going on. The technical analysis is going to help a lot in figuring out what's causing these issues.

**Aida Knežević:** We can ask our SEO experts to look at the direct traffic and try to find patterns we can link to it.

**John Jeremiah:** Patterns are hypotheses. I'll take educated guesses.

**John Jeremiah:** I mean, I'm scratching my head trying to think about what could be causing it.

**John Jeremiah:** I've got some threads I'm pulling on.

**John Jeremiah:** And to be honest, I think one thread is adding UTMs to different links where we know what they are so we can at least start to track them and start to establish a framework, which we're, because we don't use HubSpot and because we don't have a marketing automation tool in the back that's going to sort a lot of that out, I think we haven't done it.

**John Jeremiah:** So I've got to think about implementing a UTM framework.

**Aida Knežević:** Okay, okay, got it.

**John Jeremiah:** What else?

**John Jeremiah:** We talked technical, we talked content.

**John Jeremiah:** Irena, I wish Brock was on the call. Is there a trend or place where we need to evolve the approval process? I don't want to change things just because I'm here, but do you think that needs to change over time?

**Irena Reedy:** Not recently. Right now, content goes through Brock for factual accuracy and Mike T for design and messaging alignment. They're the best people to make sure everything is correct and aligns with our brand.

**John Jeremiah:** We need to add a messaging and positioning review step. From a GrowthX perspective, is there content we've declined that you think we should be putting out? I saw some topics we opted not to do—do you guys have professional pushback on any of those decisions?

**Aida Knežević:** Brock hasn't reviewed comparison blog topics yet. But product comparison posts—Fleet vs. competitors, or comparing two competitors and featuring Fleet as a third option—tend to get indexed very quickly by LLMs. We published a comparison post for another client recently, and it was already being cited by ChatGPT. These show results fast. Sometimes companies push back because they don't want to feature competitors on their sites, but these are valuable.

**John Jeremiah:** Not a bad idea. I did this at Traceable early on. I took a screenshot of a spreadsheet one of our SEs built comparing products—a fair, honest comparison. I cleaned it up, made it pretty, added enough copy to make it meaningful. I published eight pages: Traceable vs. each direct competitor. Within two weeks, we ranked #1 organic for "Traceable vs. [competitor]". I know it worked because a SourceForge rep called trying to sell domain authority services. They searched "Traceable vs. Salt" and got my page, not theirs. I did three-way comparisons too and we ranked on all of them. Competitors' marketing teams literally complained to me, threatened lawyer calls. We owned the organic.

**Aida Knežević:** Your internal messaging document would be really helpful. Right now, our content is more educational—we mention Fleet maybe once or twice. But comparison blogs will be heavily focused on Fleet, so we need that messaging framework to guide how we write them.

**John Jeremiah:** Irena, you and I need to push Ashish to get this done. We need the comparison blogs—they'll get attention and traction. As long as they're fair, educational, and give people meaningful information, then I think we have to do it.

**Aida Knežević:** We totally agree. All right, I think we're almost at time. Erik, anything else to add?

**Erik O'Brien:** Just keep reviewing the Airtable and approving topics as we go. That keeps our backlog filled with content we can keep developing.

**Aida Knežević:** Thanks, everyone. Let's follow up on Slack.

**Irena Reedy:** See you next week.

**John Jeremiah:** Thank you all.
