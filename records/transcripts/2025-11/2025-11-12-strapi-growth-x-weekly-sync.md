# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-11-12
time: 17:25 UTC
duration: 35 minutes
organizer: team@growthxlabs.com
participants: Vivek Shankar (GrowthX), Mara Leighton (GrowthX), Victor Coisne (Strapi), Golzar Yaghoubpour (Strapi), Paul Bratslavsky (Strapi), Theodore Kelechukwu Onyejiaku (Strapi)
fathom_recording_id: 101134764
fathom_url: https://fathom.video/calls/470934368
share_url: https://fathom.video/share/rz8w12_gXE-N5T8B3mUAzBNc5sdkr7oK
source: fathom
enriched_on: 2026-03-02 15:30 UTC
</metadata>

---

## Summary

GrowthX and Strapi reviewed weekly content delivery (9 articles, 2 with issues), key production blockers (comparison page table fix in QA, publishing workflow testing Nov 13, FAQ rollout constrained by engineering backlog), and performance gains (sessions and conversions up week-over-week, Tutorials cohort strongest). Victor outlined 2026 strategy pivots: repurposing `/faq` as an LLM-friendly "about page," launching new AI integration pages (Cursor, V0), exploring Discord-to-Reddit automation for better search indexing, and clarifying timelines for self-serve platform access (Atlas) that Strapi needs to run autonomous workflows.

---

## Context

This is a weekly sync between GrowthX and Strapi to review content performance and alignment on 2026 strategy. Vivek Shankar leads the meeting from the GrowthX side, supported by Mara Leighton. Victor Coisne leads for Strapi, joined by his team members including Paul (video/content creation), Golzar (product/content), and Theodore (content oversight). The engagement focuses on content marketing and SEO performance, with Strapi relying on GrowthX to produce and optimize documentation and guides that improve search visibility and user experience. Previous meetings have established baseline metrics, and this call reviews week-over-week progress, blockers, and forward planning.

---

## Relevance

**To GrowthX Delivery:**
- Content production is tracking at 9 articles/week with quality issues emerging (code formatting). Strapi has backlog constraints preventing automation, forcing manual FAQ updates and limiting self-serve capabilities.
- Vivek is manually compiling negative-mention queries from Scrunch for content strategy (top 5 due Nov 14-17). This manual process indicates tooling gaps.
- GrowthX is supporting Strapi's 2026 strategic shift toward LLM-friendly content (e.g., repurposing /faq as an "about page for LLMs") and AI integration pages (Cursor, V0, etc.).

**To GrowthX Business Development:**
- Strapi engagement is healthy: sessions and conversions growing week-over-week, influenced contacts up, cohorts (Tutorials, Ecosystem, Headless CMS) performing well.
- Key blocker: Strapi needs self-serve access to GrowthX platform (Atlas) for autonomous workflows. Mara will push for timeline. This expansion could unlock new work.
- Victor is actively exploring 2026 opportunities: integration page performance tracking, forum/Discord-to-Reddit automation, and content strategy pivots around AI tooling.

**To CheckThat:**
- Strapi is monitoring LLM traffic and considering how LLMs index their content. Discussion of `/faq` repurposing for LLM scannability and plain-text formatting signals interest in AEO optimization.
- Negative-mention query analysis via Scrunch is an AEO-adjacent workflow that could inform CheckThat product roadmap.

---

## Overview

- **Performance is positive:** Sessions and conversions are growing, with "Tutorials" showing the highest recent jump.
- **Key issues are resolving:** The comparison page table fix is in QA (prod ETA: Nov 12–13), and the publishing workflow test is set for Nov 13.
- **2026 strategy is forming:** Discussions began on repurposing the `/faq` page for LLMs and indexing Discord knowledge via Reddit, not the Strapi forum.
- **Blockers persist:** Progress is stalled by manual workarounds (e.g., FAQ updates) due to engineering backlog and a lack of self-serve platform access.

---

## Key Topics

### Content Production & Issues

  - **Article Delivery:** 9 articles delivered last week (2 had code formatting issues). 7 more are scheduled for this week.
  - **Comparison Page Table:** Fix is in QA → prod ETA: Nov 12–13.
  - **Publishing Workflow:** A test is scheduled for Nov 13 to resolve minor automation bugs.
  - **Comparison Page Videos:** Paul is finishing a new "getting started" video (ETA: Nov 12–13) to update all pages.
  - **FAQ Component Rollout:**
      - **Blocker:** Manual updates are required due to engineering backlog.
      - **Progress:** Integration pages are being updated.
      - **Timeline:** Audit of capabilities/features pages completes Nov 14 → updates follow by end of next week.

### Performance Review

  - **Overall Trends:** Sessions and conversions are growing week-over-week.
  - **Cohort Performance:** "Tutorials" showed the highest jump. "Ecosystem" and "Headless CMS" remain top performers.
  - **Negative Mentions (Scrunch):**
      - **Action:** GrowthX is manually compiling URLs for top 5 negative queries.
      - **ETA:** Nov 14 EOD or Nov 17.
      - **Rationale:** The list will inform content strategy and provide community feedback.

### 2026 Strategic Planning

  - **`/faq` Page Repurposing:**
      - **Problem:** The page is outdated but still gets traffic.
      - **Proposal:** Repurpose as an "about page for LLMs" with plain text for better scannability.
  - **Integration Page Strategy:**
      - **Action:** Analyze traffic for existing pages to guide future investment.
      - **Opportunity:** Create new pages for tools like Cursor, V0, and other AI tools.
  - **Strapi Forum vs. Discord:**
      - **Problem:** Valuable knowledge is trapped in Discord and not indexed by search.
      - **Decision:** The Strapi forum will not be revived due to past spam/moderation issues.
      - **Proposed Solution:** Automate posting key Discord topics to the Strapi Reddit channel for better search indexability.
  - **Self-Serve Platform Access:**
      - **Need:** Strapi requires self-serve access to the GrowthX platform (e.g., "Atlas") to run autonomous workflows.
      - **Status:** No ETA.

---

## Action Items

**Vivek Shankar (GrowthX)**
- Fix article flagged by Theo this week
- Send top 5 negative-mention queries w/ URLs to Victor by Nov 14; then merge w/ 3rd-party domains
- Resend Airtable refresh-list link in Slack
- Confirm ETA for Capabilities/Features FAQ additions to Victor early next week
- Draft plan for /faq as LLM-friendly 'About Strapi' page; share w/ Victor
- Add 'integration-page performance tracking + new AI integration pages' to next week's agenda

**Paul Bratslavsky (Strapi)**
- Update comparison pages w/ new 'Strapi Getting Started' video
- Write 'Migrate from WordPress to Cursor' article

**Mara Leighton (GrowthX)**
- Bump GrowthX team for Atlas/self-serve timeline; update Victor
- Research forum/Discord-to-Reddit automation; share findings w/ Victor

---

## Transcript
**Paul Bratslavsky:** Hey, how's it going?

**Vivek Shankar:** Hey, Paul, how are you?

**Paul Bratslavsky:** Hold on, let's go present to you.

**Paul Bratslavsky:** It's probably me. I don't know why. One moment.

**Vivek Shankar:** I can hear you just fine.

**Paul Bratslavsky:** Hello, hello, hello. I can hear you now, yes. Okay. Yeah, my computer just automatically switches from my headphones to not use them, which is very frustrating.

**Paul Bratslavsky:** Like in 2025, 2026, I would think they would finally be smart enough to do it.

**Vivek Shankar:** Well, I'm loving the leaves and flowers in the background.


**Paul Bratslavsky:** Yeah, I'm at a coffee shop. I've been trying to force myself to ride the bike to work, kind of like a habit-building thing to not stay home all the time.

**Vivek Shankar:** Nice.

**Vivek Shankar:** Hey Theo, hey Golzar.

**Golzar Yaghoubpour:** Hello.

**Vivek Shankar:** Are we waiting on Victor or?

**Paul Bratslavsky:** I think so.

**Paul Bratslavsky:** He should be joining.

**Vivek Shankar:** Yeah, I he had accepted, so I guess we'll give him a couple minutes.

**Paul Bratslavsky:** But I just want to call out Golzar's Christmas background there, very festive, very nice.

**Golzar Yaghoubpour:** Thank you.

**Paul Bratslavsky:** The coffee shop does. Got the vibe, it's nice.

**Vivek Shankar:** Why don't we get started, and if Victor joins, guess we can.

**Vivek Shankar:** Sounds good.

**Vivek Shankar:** There he is.

**Vivek Shankar:** I think he just joined, so.

**Victor Coisne:** Hello.

**Vivek Shankar:** Hey, Victor.

**Victor Coisne:** How are you?

**Mara Leighton:** Hey.

**Mara Leighton:** How's it going?

**Victor Coisne:** Going well?

**Mara Leighton:** Good.

**Victor Coisne:** Love to hear it.

**Victor Coisne:** Golzar, already Christmas mode.

**Mara Leighton:** I like it.

**Golzar Yaghoubpour:** Yeah. It's happy and festive.

**Victor Coisne:** Awesome.

**Vivek Shankar:** All right.

**Vivek Shankar:** Let me share my screen. Okay, hopefully everyone sees this. All right. So just updates on new content.

**Vivek Shankar:** we delivered nine articles last week.

**Vivek Shankar:** Nine because there were two that had some code formatting issues.

**Vivek Shankar:** There was still one that we delivered in that patch that had an issue that Theo pointed out.

**Vivek Shankar:** We will address that real quick this week.

**Vivek Shankar:** Yeah, generally seven scheduled for this week as well.

**Vivek Shankar:** Things are pretty much going per, according to plan over there.

**Vivek Shankar:** Running through the issue list.

**Vivek Shankar:** So, the comparison page, moving the table to the bottom.

**Vivek Shankar:** Paul just wanted to check if there was any updates over there at all.

**Victor Coisne:** I can give an update because I think Paul was off yesterday and I had a call with Notoom, who is the agency that's taking care of our website.

**Victor Coisne:** It's basically in QA at the moment.

**Victor Coisne:** It should land in production hopefully today or tomorrow.

**Vivek Shankar:** Sounds good.

**Vivek Shankar:** And then regarding the publishing workflow, we are testing it tomorrow, so there were a lot of little niggles here and there, as I mentioned last week.

**Vivek Shankar:** So hopefully, when we tested it earlier this week, things look good.

**Vivek Shankar:** We're giving it another test tomorrow with one of the articles of this week's batch.

**Vivek Shankar:** But again, this isn't a major issue.

**Vivek Shankar:** The flow is pretty much automated.

**Vivek Shankar:** just a few things here and there keep breaking.

**Vivek Shankar:** So pretty much doing that.

**Vivek Shankar:** And then the next one was the adding videos to the comparison pages.

**Vivek Shankar:** So I had sent over a list of the comparison pages that needed videos.

**Vivek Shankar:** I think there were just, I think two pages had videos on them.

**Vivek Shankar:** The rest of them needed videos to be added.

**Vivek Shankar:** So just want to make sure that you saw that, Theo.

**Vivek Shankar:** So if there's, if there's, I can sort of thing you on.

**Victor Coisne:** I can jump in as well here. Paul, you're working on a Strapi Getting Started video.

**Paul Bratslavsky:** Yeah, I'm looking to hopefully finish it today, definitely by tomorrow.

**Paul Bratslavsky:** And then once that's done, I'll make sure to update all the comparison pages with that new video.

**Vivek Shankar:** Cool, sounds good.

**Vivek Shankar:** And then the task in progress right now is adding the FAQ component slash reviewing it to the integration.

**Vivek Shankar:** capabilities and features pages.

**Vivek Shankar:** So the updating the integrations pages is underway.

**Vivek Shankar:** We're having to do it manually again because of engineering backlog, unfortunately, so it's going to take some time.

**Vivek Shankar:** We are reviewing the capabilities and features pages just to see which ones have FAQs and which ones don't.

**Vivek Shankar:** So we just add it to that list and we expect to get this completed over the next couple weeks.

**Vivek Shankar:** So that's the rundown of the issue list.

**Vivek Shankar:** Moving on to the performance side of things.

**Vivek Shankar:** So, yeah, generally, it's headed in the right direction so far.

**Vivek Shankar:** We've just had one full week of measurements.

**Vivek Shankar:** obviously, the number of sessions are quite encouraging.

**Vivek Shankar:** And then, you know, Victor, just in case you're looking for month-on-month numbers, I had them highlighted in last week's agenda.

**Vivek Shankar:** I can send that to you async as well if you need that deeper dive.

**Vivek Shankar:** But just generally, week-on-week, you know, we had a bump in the number of conversions events.

**Vivek Shankar:** And also, as I highlighted last week, these charts are basically monthly charts from HubSpot.

**Vivek Shankar:** The new and influenced contacts are growing.

**Vivek Shankar:** Obviously, influenced contacts, we need to catch up to the peak that we had in January, but we're headed in the right direction overall over here.

**Vivek Shankar:** Regarding the cohort performance weekly.

**Vivek Shankar:** So Tutorials performed with the highest jump last week, and Ecosystem continues to be the top performer, along with Headless CMS.

**Vivek Shankar:** Things are going pretty well over here, along with LLM traffic referrals as well, regarding data from Scrunch.

**Vivek Shankar:** Again, weekly, you know, Scrunch data doesn't change all that much, but generally, Strapi is in a good position overall with regards to the competition.

**Vivek Shankar:** And, yeah, the content is, seems to be working quite well, too.

**Vivek Shankar:** So, things are looking pretty good over here.

**Vivek Shankar:** Any questions I can answer about the performance or anything so far?

**Victor Coisne:** No, I think it's mostly, like, you know, the discussion we were having on the queries, they're fixing, like, some of the negative, yeah, mentions.

**Victor Coisne:** Dimensions, yeah.

**Vivek Shankar:** Yeah, in those queries, if we know what the links are, then we can try to, yeah, yeah.

**Vivek Shankar:** I actually sort of showcased that last week.

**Vivek Shankar:** Scrunch makes it really difficult for us to retrieve those pages.

**Vivek Shankar:** And the thing is, like, even the list of queries that I sent you, that's actually a condensed list because Scrunch sort of expands it a lot.

**Vivek Shankar:** That's the reason it's taking time.

**Vivek Shankar:** So we're kind of having to go through it manually and just check each query, list the page URL, et cetera, and put that together.

**Vivek Shankar:** So hopefully, at least for the top five, we hope to get it to you by Friday, end of day, if not that Monday at the latest.

**Vivek Shankar:** But, yeah, we're just going to work through that list, and that's something we are doing right now.

**Vivek Shankar:** It's just taking time because Scrunch doesn't give us that export in any way.

**Vivek Shankar:** So that's the only reason for the timeline there.

**Victor Coisne:** Yeah, and I forgot where you highlighted some of the third-party domain that we are not from competitors that...

**Victor Coisne:** Where, like, good backlink would be a good idea.

**Victor Coisne:** I think it'd be good to kind of merge, like, those two, like, okay, like, what query do we need to work on and then what are the sites?

**Victor Coisne:** Because I'm assuming, like, it needs to be on, you know, outside of strapi domain for that to impact the sentiment analysis or whatever on that query.

**Victor Coisne:** So I think we need to cross-reference those two lists and come up with a short list of, okay, like, these are the top queries and these are, like, the top places where we need to start placing those, that content and backlink.

**Vivek Shankar:** Yeah, for sure.

**Vivek Shankar:** The other reason I highlighted that particular content, the negative mentions, was because it might give some sort of feedback as well.

**Vivek Shankar:** I know you're very active in Discord and the community, et cetera.

**Vivek Shankar:** Dev2, et cetera.

**Vivek Shankar:** It might offer some sort of insight in terms of what to ask the community, so I wanted to share that as well.

**Victor Coisne:** Yeah, it's super useful.

**Victor Coisne:** I think we definitely have some, on the topic of performance, I think we have some work to do.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So, yeah, I can put those URLs in one list together once we're done with it and then share that.

**Vivek Shankar:** So, yeah, that's pretty much the performance side of things.

**Vivek Shankar:** And then I shared the refresh list, so I've actually created a tab in Airtable, and I linked this in the agenda, sort of the agenda message that I sent in Slack.

**Vivek Shankar:** I'll send it again, of course.

**Vivek Shankar:** But, yeah, just basically these pages, these are the ones that have lost traffic on a six-month basis.

**Vivek Shankar:** Some of these, obviously, like the WordPress migration, seemed a little technical. So I was wondering if, when you have the time, you could let us know which ones you think are better handled internally by Strapi, and then we'll get started on the rest.

**Vivek Shankar:** There aren't too many, so we should be able to work through these over the upcoming weeks. We just need your input on that. Paul and Theodore, these should be pretty quick.

**Victor Coisne:** Like, I reviewed the list myself.

**Victor Coisne:** I think the only one that makes sense is the migration from WordPress with Cursor, which is already on your list, Paul.

**Victor Coisne:** I think we should do that right away.

**Victor Coisne:** I mean, anything that stands out that should be handled by you guys directly?

**Victor Coisne:** Paul?

**Paul Bratslavsky:** Yeah, I was just looking at the list.

**Paul Bratslavsky:** I think they all look good. We figured we'd let AI create the first draft and then work on it, so we don't have to start from scratch.

**Paul Bratslavsky:** In terms of the topics, yeah, the migration from WordPress to Cursor, that should be an internal article.

**Paul Bratslavsky:** Everything else, I think, is fine.

**Vivek Shankar:** Now, this is migrate from Content 2 as well.

**Paul Bratslavsky:** I don't want to write that one. For SEO purposes, if AI can do it quickly to capture those keywords, that's fine, but it's not something we'll prioritize right now.

**Victor Coisne:** Yeah, I mean, we never see Content 2, so I wouldn't spend too much time on this one.

**Victor Coisne:** Like, I've literally never heard of them.

**Victor Coisne:** Yeah.

**Theodore Kelechukwu Onyejiaku:** So, yeah.

**Theodore Kelechukwu Onyejiaku:** Is there anyone on the second list?

**Vivek Shankar:** Sorry?

**Paul Bratslavsky:** If you scroll down. Yeah, because I think we looked at this already. The only one that stood out that we definitely have to write is the WordPress to Cursor migration, but I kept it on the list because if it's automatically created, we could use it as a jumping-off point. We could also completely remove it from here and work on it ourselves.

**Victor Coisne:** Okay.

**Victor Coisne:** Do have anything else?

**Victor Coisne:** Theo, do you think it makes sense to handle internally?

**Theodore Kelechukwu Onyejiaku:** No, I think the only one we could handle internally is the WordPress.

**Paul Bratslavsky:** I wanted to make a call-out as a reminder: we still have P1 items in the content pipeline that probably take precedence.

**Paul Bratslavsky:** So, we're going to start on those.

**Paul Bratslavsky:** But I think the WordPress one is the only one that we want to move from here.

**Victor Coisne:** Okay, cool.

**Victor Coisne:** Let's move on then.

**Vivek Shankar:** All right.

**Vivek Shankar:** right.

**Vivek Shankar:** Well, those were actually the updates for this week. TLDR: things are going in the right direction generally.

**Victor Coisne:** Yeah, I have a couple of things.

**Victor Coisne:** First thing is, so if I understand correctly, the ETA for the FAQ, for the FAQ being, at least you're finalizing the audit of where FAQs are missing by the end of week, but is it not delivering the actual FAQ themselves?

**Victor Coisne:** So, I think it'd be good to have like a specific timeline on that.

**Vivek Shankar:** Sure.

**Vivek Shankar:** Yeah, so the integration pages is underway.

**Vivek Shankar:** So, we are updating.

**Vivek Shankar:** We just have to change the element on those pages because some of those pages have basically they're in the content block versus having a separate element.

**Vivek Shankar:** So, that is on

**Vivek Shankar:** The Friday ETA is for the capabilities and features pages, so the audit will finish then, and then we will, those page numbers are smaller, so we hope to get that done by end of next week.

**Vivek Shankar:** I will confirm early next week with regards to the ETA.

**Victor Coisne:** Okay.

**Victor Coisne:** Because we also have like a, I just found out that we have a, let me drop it in the chat.

**Victor Coisne:** Where is the chat here?

**Victor Coisne:** Oh, here's the chat.

**Victor Coisne:** Yeah, like we have a slash FAQ page, which hasn't been updated in a while, and I was wondering if it makes sense to break that down in a different way, as in like maybe create like subcategories.

**Victor Coisne:** So I don't really know exactly, I haven't thought too much about it, but if you have any recommendation on what to do with that page and, you know, should we just redirect or like...

**Victor Coisne:** Yeah, like...

**Victor Coisne:** Create, like, dedicated URL.

**Victor Coisne:** I don't know, just putting that here.

**Victor Coisne:** I think it's probably worth updating, even though it hasn't been touched in a couple of years.

**Victor Coisne:** Still getting too much traffic, but any recommendation there?

**Vivek Shankar:** Off the top of my head, I think instead of having FAQ elements like these on the page, it might help to just have plain text, just for LLM scannability, I think.

**Vivek Shankar:** There's a lot of information here.

**Vivek Shankar:** Yeah, I think we can maybe, if this page is not getting a lot of traffic, we can go a bit more experimental with this, maybe turn this into an LLM about page, or an about page for LLMs, essentially.

**Vivek Shankar:** Just the essentials of strapi, answer the most top search queries, et cetera, ones you want to show up for it.

**Vivek Shankar:** And then we can track citations and see how it's working. That's off the top of my head.

**Victor Coisne:** I can follow up with more details.

**Victor Coisne:** I think that sounds good, like an about page for LLMs. Let's just try that.

**Victor Coisne:** Other question is, I don't know if it's for us or like GrowthX, but I think it would be good to understand, similar to what we've done with the blog that lost traffic, what we just talked about at the end, maybe doing the same thing for integration pages.

**Victor Coisne:** Are we seeing, especially for the ones that were created by GrowthX, are we seeing any upward movement or, on the other hand, like decreases?

**Victor Coisne:** I think that'd be good to track so we can decide how we invest in integration pages.

**Victor Coisne:** I think there are new ones that should be created, like for tools such as Lovable and Bold. Paul, you just created content. I think it would make sense to create integration pages for V0, Vercel AI, and maybe even some of the other AI tools like Cursor.

**Victor Coisne:** I'm just thinking it might be a quick win. We don't have to talk about it now, but I think it's worth having as an agenda point for next week. Let me check my notes. I'm also thinking about the Strapi forum. It's still getting decent traffic — about 7% of overall traffic. We didn't really sunset it.

**Victor Coisne:** We were having issues with spam, and moderation was time-consuming. It caused moderation issues earlier this year. We blocked authentication so people couldn't create accounts.

**Victor Coisne:** I'm just curious to see, like, from your perspective, like any recommendation on the role that forum play.

**Victor Coisne:** Like, I'm just so frustrated that a lot of the knowledge is lost in Discord.

**Victor Coisne:** And I just want to make that, like, you know, indexable and try to surface some of that knowledge.

**Victor Coisne:** And it feels like an important, like, quick win from a GEO standpoint as well, because it's such a long tail of, you know, edge cases.

**Victor Coisne:** And so any guidance as we plan for 2026 and think about what we want to do with the forum?

**Victor Coisne:** Any recommendation from you guys?

**Vivek Shankar:** In terms of LLM discoverability, in the performance reports, I'm not seeing too many links go back to the forum.

**Vivek Shankar:** So, given the kinds of links that, you know, when you mentioned,

**Vivek Shankar:** The moderation issues occurred earlier this year.

**Vivek Shankar:** It might be a risk versus reward kind of a thing.

**Vivek Shankar:** So I would say it depends on how much resources you have internally.

**Vivek Shankar:** Like if it's too much of a, if it's going to attract a lot of dodgy links and you can't moderate it, maybe the knowledge that's being shared is not going to surface anyway because it's going to get somehow excluded.

**Vivek Shankar:** So in terms of surfacing the knowledge, Discord is obviously a good place for it because people are more likely to engage.

**Vivek Shankar:** One way of dispersing it would be to maybe run some kind of a weekly digest or maybe a blog, like latest from Shrappy's community or something.

**Vivek Shankar:** Or, yeah.

**Paul Bratslavsky:** Maybe I'll use it in a newsletter.

**Paul Bratslavsky:** I got another question.

**Paul Bratslavsky:** Does LLMs, where do they hold videos, like let's say from YouTube or TikTok or any of those users, knowledge source, support?

**Paul Bratslavsky:** LLMs that you saw?

**Vivek Shankar:** As far as I know, they can't crawl YouTube.

**Vivek Shankar:** There are a few ones that, a few dodgy ones that do it, but the main sort of LLMs, platforms, they don't sort of do it.

**Vivek Shankar:** They're no index.

**Vivek Shankar:** So that's, yeah, that's the state.

**Victor Coisne:** Okay, go ahead, Paul.

**Paul Bratslavsky:** I had another, like, interesting idea.

**Paul Bratslavsky:** I wonder if it would make sense to kind of pick the topics that stand out from the forum, or maybe it could be, like, automated thing, which adds topics, and then we just have a chat GPT created based on all of that content, and we make that GPT public, and people, that's, like, another way that people could interact, I guess.

**Paul Bratslavsky:** But that doesn't help the immediate way of adding content.

**Paul Bratslavsky:** So let me, like, refresh.

**Paul Bratslavsky:** Back to Vivek's point as well is that creating a summary blog post is probably going to be the best way to go.

**Victor Coisne:** Yeah, I don't know.

**Victor Coisne:** I'm not convinced.

**Victor Coisne:** It seems very manual.

**Victor Coisne:** to me, I think the value of a form is creating a large number of URL with a long tail of questions and keywords that we're not.

**Victor Coisne:** So I don't really think we're solving for the same thing.

**Victor Coisne:** But what I'm hearing is you don't have any customers that are doing anything interesting with forums and GEO.

**Victor Coisne:** Is that accurate?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Not that I'm aware of.

**Vivek Shankar:** Mara, I don't know if there's more.

**Mara Leighton:** Nothing that I have in-depth experience with.

**Mara Leighton:** I know we're piloting Reddit for a few customers, but typically what we're doing on the growthx side is more of like a monitoring and insights and using that for...

**Mara Leighton:** For content strategy, and then if the client wants to use it for their own internal marketing or to run like an employee-based account on a particular forum, that can be successful.

**Mara Leighton:** But to Vivek's point, it's just a little bit more labor-intensive and experimental.

**Mara Leighton:** So that's not to say like you shouldn't do it, but just that in order to be useful, you have to be really consistent and really visible.

**Mara Leighton:** And I think it's just a more gradual play.

**Victor Coisne:** But so nothing about the Discord element.

**Victor Coisne:** That's quite different, Mara.

**Victor Coisne:** We're talking about the Reddit and the social channel, and I think that's important, and we're trying to do it.

**Victor Coisne:** And again, that's why we brought up Octolens as an important API for you to pull, again, the gaps and everything.

**Victor Coisne:** But that's outside of our domain. I'm talking here about what we want to do with the forum.

**Paul Bratslavsky:** I was going to add to that. Reddit does show up really well in search, and I think LLMs are indexing Reddit. Maybe a happy medium would be to create an automated way to take top topics from Discord and the forum and post them to Reddit in our Strapi channel.

**Paul Bratslavsky:** Because at least that's going to get indexed. But that only makes sense if we can automate the process. From my experience searching Google and using LLMs, I've seen suggested responses indexed to Reddit posts.

**Victor Coisne:** Yeah, I think we should treat these as two separate topics: do we want to do anything with our forum, and do we want to continue investing in Reddit and Stack Overflow? To me, these are different topics.

**Victor Coisne:** Anyway, moving on. My last question is: what's the timeline for self-serve access to your platform — Atlas or whatever the new name is? We want to do some things autonomously without relying on you guys or your engineering team. Do you have an update on that?

**Mara Leighton:** I do not have an update, but I will bump the team as soon as we get off the call and see if I can get you an update.

**Mara Leighton:** So, yeah, unfortunately, I don't have an updated timeline, but I will work on getting you one today.

**Victor Coisne:** That sounds great.

**Victor Coisne:** For the rest of the team, think about what self-serve workflows we want to run once access becomes available as we do 2026 planning. I think it's important to keep that in mind.

**Victor Coisne:** Cool.

**Victor Coisne:** Well, excited to get access to that when that's available.

**Mara Leighton:** Yeah.

**Mara Leighton:** Also, I'll ask around and see if anyone is doing anything particular with their forums and maybe Discord in particular and see if there's anything that we can surface for you that other clients are doing.

**Victor Coisne:** So we'll keep that in mind as well.

**Victor Coisne:** Sounds good.

**Mara Leighton:** Cool.

**Vivek Shankar:** Great.

**Mara Leighton:** Thanks, everyone.

**Paul Bratslavsky:** Thanks, everyone.

**Vivek Shankar:** Have good rest of your day.

**Paul Bratslavsky:** Bye.

**Victor Coisne:** Bye.

**Mara Leighton:** Bye.
