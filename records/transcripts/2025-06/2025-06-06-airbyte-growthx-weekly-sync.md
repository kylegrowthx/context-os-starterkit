# Airbyte <> GrowthX Weekly Sync

<metadata>
date: 2025-06-06
time: 15:30 UTC
duration: 17 minutes
organizer: David Galic (GrowthX)
participants: Tanmay Sarkar (Airbyte), David Galic (GrowthX), Mario Moscatiello (Airbyte), Jakub Rudnik (GrowthX), Tiandra Burns (GrowthX)
fathom_recording_id: 66973093
fathom_url: https://fathom.video/calls/318860039
share_url: https://fathom.video/share/8ntxDq8_7zjgP2L2xX6S1jb_pMFr2UYN
source: fathom
enriched_on: 2026-03-03 10:45 UTC
</metadata>

---

## Summary

Airbyte and GrowthX aligned on a content production acceleration strategy: pausing article refreshes for 30 days to focus exclusively on 20 new articles while exploring programmatic SEO to scale output, with Airbyte reporting that events generate 30% of pipeline and SEO traffic is down 20% since January. The teams discussed how to implement schema markup across existing and new articles programmatically, finalized blog cover image templates via Figma to eliminate a bottleneck, and identified action items around Looker dashboard improvements and Apache Iceberg use case mapping.

---

## Context

Airbyte is a data integration platform that runs large-scale event marketing campaigns (Snowflake Summit, Databricks) that drive significant pipeline impact. GrowthX has been engaged to execute Airbyte's content marketing strategy, including producing and refreshing blog articles, optimizing for SEO, and tracking performance through dashboards. This weekly sync is a standing check-in between Airbyte's content team (Tanmay) and GrowthX's delivery team (Jakub, Tiandra, David) to align on content production priorities, tackle process bottlenecks, and discuss scaling opportunities as Airbyte faces declining organic traffic following algorithm changes.

---

## Relevance

**To GrowthX Delivery:**
- Eliminated a process bottleneck: Figma blog cover templates replace manual Photoshop work, reducing cycle time and enabling faster article launches
- Content production shift: Pausing refreshes for 30 days to focus on 20 new articles clarifies priorities and allows GrowthX to hit production deadlines with full team focus
- Schema markup standardization: Moving toward template-level schema implementation (FAQ markup) vs. manual post-by-post implementation will save significant delivery effort at scale
- Looker dashboard challenges flagged: GrowthX acknowledges technical debt on weekly/monthly view functionality; Mario offered support and Kyle will be brought in to assist

**To GrowthX Business Development:**
- Strong account health signal: Events are 30% of Airbyte's pipeline; last year's event investment already paid for itself
- Expansion opportunity: Airbyte is exploring programmatic SEO scaling (potentially 200 articles/month vs. current editorial pace). Commercial discussions pending between Jakub and Mario; Kyle Gaudreau tagged for strategy sync.
- Organic traffic risk: SEO traffic down 20% since January; team is doubling down on new content production to recover
- Reference/case study potential: Airbyte's comprehensive event strategy (booth, wrapped cars, LED track, after-party) is a strong differentiator; could be featured in GrowthX content

**To CheckThat:**
- AI search referral increase noted: Airbyte is seeing more traffic from AI search/overviews alongside organic traffic decline, indicating shift in discovery patterns relevant to CheckThat's AEO positioning

---

## Overview

- Airbyte's events (e.g., Snowflake Summit) generate 30% of pipeline; highly successful for leads and brand exposure
- Shifting focus to new articles only for next 30 days, pausing refreshes to cover backlog of new topics
- Exploring programmatic SEO to accelerate content production; commercial details to be worked out
- Looker dashboard development ongoing but facing challenges; V1 available but improvements needed

---

## Key Topics

### Event Marketing Success

  - Snowflake and Databricks events in San Francisco yielding significant results
  - 30% of Airbyte's pipeline comes from events
  - Last year's event already paid for itself and generated more
  - Comprehensive event presence: booth, wrapped cars, LED track, after-party sponsorship

### Content Strategy Shift

  - Pausing article refreshes for 30 days to focus solely on new content
  - Target: 20 new articles in the coming month
  - New topics already listed in main sheet for team to select from
  - Exploring programmatic SEO to accelerate content production
  - Considering blend of editorial approach and programmatic SEO workflow

### SEO Performance and Strategy

  - SEO traffic down 20% since January
  - Increase in traffic from AI search referrals
  - Goal to double down on content production to address traffic decline
  - Discussing potential for scaling up content creation significantly (e.g., 200 articles/month)

### Looker Dashboard Development

  - V1 of dashboards available but facing technical challenges
  - Issues with setting up weekly and monthly views
  - LLM modules can be added to track specific traffic
  - Jakub acknowledges frustrations and commits to improvements

### Schema Implementation

  - Agreement to add schema to refreshed and new blog posts where relevant
  - Discussing potential for programmatic schema addition to existing articles
  - Considering template-level schema implementation for efficiency (e.g., FAQ schema)

---

## Action Items

**Tanmay Sarkar (Airbyte)**
- Share Figma templates for blog cover images via Slack to team email
- Review articles and add more to new articles tab in main sheet for David/Tiandra to select from

**Jakub Rudnik (GrowthX)**
- Discuss programmatic SEO scaling internally; sync with Mario and Kyle on commercial aspects and strategy
- Continue updating Looker dashboards; fix weekly/monthly view issues (priority item)
- Investigate CMS/blog template level schema additions (e.g. FAQ markup) for programmatic implementation
- Complete mapping for Apache Iceberg use cases; send to Tanmay early next week

---

## Transcript
**Tanmay Sarkar:** David, how are you doing?

**David Galic:** Can I get my headphones on? Yeah, yeah. Can you hear me now?

**Tanmay Sarkar:** Yeah, yeah.

**David Galic:** How are you doing?

**Tanmay Sarkar:** Good.

**Tanmay Sarkar:** It's been a busy week for us for Snowflake event.

**Tanmay Sarkar:** Next week, again, Databricks is here.

**Tanmay Sarkar:** So, yeah, these two weeks.

**David Galic:** Where's the event?

**Tanmay Sarkar:** Both in San Francisco in the same place.

**Tanmay Sarkar:** So, we had both there.

**Tanmay Sarkar:** In stuff like that, I know we also have a booth there at Databricks, so yeah.

**David Galic:** Is that kind of thing something that works better for brand awareness, or have you actually gotten leads from it?

**Tanmay Sarkar:** Both. We get brand exposure and we also get a lot of leads from that. It's both. Most of our success comes from these events. Last year's event was really successful — we got a lot of leads that actually converted into our pipeline.

**David Galic:** That's cool, yeah.

**David Galic:** Well, a lot of times when I've been working with startups, they'd always be like, is it worth it?

**David Galic:** Are we getting enough leads, or is it just, or is it worth it just to get your name out?

**Tanmay Sarkar:** Yeah, yeah.

**David Galic:** If you're getting both, it's cool.

**Tanmay Sarkar:** Yeah, yeah.

**Mario:** Hello, team.

**Tanmay Sarkar:** I'm Tanmay. (Mario just joined)

**Mario:** How's everybody?

**Jakub Rudnik:** All right. Busy week, busy week.

**Mario:** Yeah.

**Jakub Rudnik:** How about you all?

**Mario:** Yeah, it's been busy, as Tami was saying, with Snowflake Summit.

**Mario:** Events are 30% of our pipeline.

**David Galic:** I'm not kidding.

**David Galic:** Yeah.

**Mario:** Yeah, last year's event paid for itself and more already, so.

**David Galic:** That's awesome.

**Mario:** Yeah.

**Mario:** Data people like events for some reason.

**Jakub Rudnik:** Interesting.

**Jakub Rudnik:** And so do you have a booth?

**Mario:** Do you do speakers, like events?

**Jakub Rudnik:** Oh, yeah.

**Mario:** The whole shebang: we had wrapped cars with our logos going around San Francisco, an LED track, we sponsored an after-party, and we had a booth.

**Jakub Rudnik:** Wow, that's a lot.

**Mario:** So, yeah.

**Tanmay Sarkar:** Yeah.

**Jakub Rudnik:** Exactly.

**Jakub Rudnik:** Exhausting.

**Jakub Rudnik:** Events are like, yes, exhausting.

**Jakub Rudnik:** So if I'm tired this week, you are all tired. At least I get to be tired and work hard from home, not dealing with all those moving parts.

**Jakub Rudnik:** Hopefully this weekend will be relaxing after this.

**Mario:** Yeah, hopefully.

**Jakub Rudnik:** All right. Let's jump in.

**Jakub Rudnik:** A couple things — some standard updates, but definitely wanted to talk through a few things. We've got a ton of refreshes and new content delivered, with a lot drafts ready. Tiandra has been doing a ton of heavy lifting to get us caught back up over the last couple weeks. So thank you for your patience.

**Jakub Rudnik:** I've got a few questions here for the team. Please chime in if I'm misrepresenting anything. One obvious bottleneck: Nico is building your cover images in Photoshop, and I don't think that's the best process.

**Jakub Rudnik:** I wonder what you do for your own blogs. Do you have templates in Figma or Photoshop?

**Mario:** We have templates in Figma.

**Jakub Rudnik:** We can definitely share those.

**Jakub Rudnik:** I think we just bootstrapped this the wrong way before. David and I weren't thinking about it because Nico was handling it, and it probably added more work than necessary. But if you share those templates, we should be able to handle it fine.

**Jakub Rudnik:** We're doing Figma, saves us a ton of time, and so this will overcome anything new that's sitting, like just needing an image, we'll launch those ASAP after getting those files.

**Tanmay Sarkar:** Yeah, yeah.

**Jakub Rudnik:** And then we just send like a note in Slack with the team email to send that to.

**Jakub Rudnik:** Cool, thank you.

**Jakub Rudnik:** So I think that solves most of that.

**Jakub Rudnik:** And then with the refreshes, yeah, 20 years.

**Jakub Rudnik:** Of those, those are over to your side.

**Jakub Rudnik:** I just want to confirm, because I don't know that I know, how much oversight do you want?

**Jakub Rudnik:** Do you want confirmation and review on all of those, you know, when Tiandra's wrapped up or refreshed?

**Jakub Rudnik:** Do you want us to just publish without that step?

**Jakub Rudnik:** I just want to make sure that we're not, you know, we are streamlined as much as you want us to be.

**Jakub Rudnik:** And you have the oversight that you want, but I don't want to add extra steps anywhere.

**Jakub Rudnik:** So what's that process like right now?

**Tanmay Sarkar:** Yeah, so I mostly review all the articles all week. This week was busy, but by today all will be reviewed and you can publish.

**Tanmay Sarkar:** Here's what I'm thinking: we already have so many topics from our research in Profound and other tools. For the next month, we can stop refreshes and produce only new articles. If our target is 20 articles, we write only 20 new articles and pause refreshes for 30 days. We cover all the new topics we currently have on our plate, and then continue refreshes after that.

**Jakub Rudnik:** Yeah, that's all good for us.

**Jakub Rudnik:** Team, any concerns?

**Jakub Rudnik:** Tiandra's nodding vigorously, so we're good on that end.

**David Galic:** We'll just add the ones you want to the Notion sheet so we know which ones to pick.

**Tanmay Sarkar:** Yeah, we already have that in the main sheet.

**David Galic:** Oh, okay, it's already there.

**Tanmay Sarkar:** Correct. I'll add more new topics there and you can pick from that list.

**Tiandra Burns:** Okay.

**Jakub Rudnik:** Tiandra and David, just grab from those and start knocking them down. With 30 days of focused content production, we'll make plenty of progress. Just keep me posted if you're running low on topics.

**Tanmay Sarkar:** I was also thinking: is there a way for us to move faster? I know you guys use programmatic SEO tools. If I have 200 article ideas, could we publish them in a programmatic way and do reviews within the system instead of this manual process?

**Tanmay Sarkar:** The manual effort we're doing now sometimes causes delays because we review, share feedback, make changes, and then go to production. It slows things down.

**Jakub Rudnik:** That's something I'd have to think about and discuss. I understand your approach — if we limit other manual parts, can we scale this up? We have an SoW with a specific word count per month, and we want to be as efficient with that as possible. If we can push those efficiencies to their limit, what does that mean for word count? We're not capped at our current volume. If it ends up being 200,000 words a month or 200 articles, we'll work with that.

**Mario:** Jakub, I'm not too worried about the commercial side. I'm happy to figure that out with you one-to-one.

**Mario:** What Tami is saying resonates with us. We're seeing our SEO traffic down over 20% since January. As we all know with AI overviews, we're seeing an increase in traffic from AI search referrals. So we really want to double down on content. I think we have a good relationship, and I'm sure we'll figure out the commercial details. Feel free to come back to us with whatever you need.

**Jakub Rudnik:** That's fair. Thank you for clarifying. We do have a good relationship. We'll figure out the internal resources needed, and I'll sync with Kyle on the commercial and strategy side.

**Mario:** The answer is yes. When I spoke with Marcel and Giacomo initially, we were thinking about taking the editorial approach first and complementing it with programmatic SEO workflows. I think we're at a stage now where we can do both. There's value in human-in-the-loop workflows for certain content, and then there's the programmatic side.

**Jakub Rudnik:** That's how I'm thinking about it too. Thank you for the clarification. I think we're good. I'll probably bring in Kyle today, and we can sync. I have time later today or Monday if you want to schedule something.

**Mario:** Perfect.

**Jakub Rudnik:** Sounds good. Thank you. The answer is yes — we want to go where you want to go. Let us move fast and trust us. We're in to do this and will sort out the details.

**Jakub Rudnik:** The last thing is the Looker dashboards. I'll be fully transparent: I keep running into issues with Looker where things don't work the way I want. Looker is not my favorite tool. I've been working with another director who's better with it, but it's been choppy. I have V1 dashboards in draft state, and while I'm not thrilled with them, I wanted to get them to you. We have daily traffic growth views, but there are other pieces from dashboards across the company that aren't standardized yet and are still in process with engineering. We have LLM modules we can add to track traffic, and I wanted weekly and monthly views, but those keep breaking on me. This is a priority for me, but it's been frustrating. I've spent a lot of time in Looker for you and other clients, and it just keeps breaking. I want to acknowledge that the dashboards are not where they need to be, but we'll keep making progress over the coming weeks.

**Tanmay Sarkar:** Yeah, I also hate Looker.

**Jakub Rudnik:** I hate it so much. It just keeps breaking. I've made progress and then it steps back. I promised you improvements by Tuesday and they weren't there. I'm trying to be transparent here. I know this is frustrating for you, but we'll get there quickly. It's top of mind and we're discussing how to solve it. Interestingly, I'm having the exact same issues with three other clients. Thank you for bearing with me. I own this and we'll have more to show shortly.

**Jakub Rudnik:** Tiandra, David, do you have any questions or concerns on the content and publishing side?

**Tiandra Burns:** For me, yes. On schema: we've figured out what we're going to do. We're going to add relevant schemas to blogs as they're published. For the refreshes, we're applying schema to both refreshes and new blogs.

**Jakub Rudnik:** Is that correct?

**Tiandra Burns:** Yes. For this first batch of refreshes, schemas will be going out. To clarify: do we want schema on all articles or just the ones that fit?

**Jakub Rudnik:** If it's relevant to the article, we want it. Schema is helpful for Google and search engines to understand the content structure. Don't force it if it doesn't make sense, but we want to show Google what's there when it's relevant.

**Jakub Rudnik:** I also want to look at template-level schema implementation. FAQs, for example — we could add them at the CMS template level so FAQ schema markup is generated automatically instead of manually on every post. That's what we did at another client. I'll sync with you on what templates should include schema, because if we're putting schema on every article, we shouldn't do it manually. We should do it at the template level.

**Tanmay Sarkar:** For new articles, we can add schema. But we have thousands of existing articles. If we do this manually, it'll take months. Can we do this programmatically?

**Jakub Rudnik:** Yes, that's where the programmatic SEO piece comes in. FAQs especially can be done at scale. We can figure out the workflow to apply that to thousands of articles and publish automatically. Tiandra will focus on new ones first, but we won't make manual schema implementation a priority.

**Tanmay Sarkar:** Is there any update on Apache Iceberg use cases?

**Jakub Rudnik:** I've started mapping but it's not done. I'll get that to you early next week. It ties into the programmatic work we're discussing. Thank you for your patience and everything you've sent over.

**Tanmay Sarkar:** I'll review the articles and add more to the new articles tab. David and Tiandra, you can pick from there.

**Jakub Rudnik:** Awesome. Thank you, Mario. I'll connect with you later today.

**Mario:** Sounds good. Thank you so much.

**Mario:** Thank you, guys.

**Tanmay Sarkar:** Thanks.

**Tiandra Burns:** Enjoy the weekend.

**Mario:** You too. Bye.
