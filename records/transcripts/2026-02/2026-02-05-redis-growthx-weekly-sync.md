# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-05
time: 17:29 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien (GrowthX), Alexis Ruiz-Pedregon (Redis), Reet Mand (Redis)
fathom_recording_id: 120115074
fathom_url: https://fathom.video/calls/556077761
share_url: https://fathom.video/share/RrKfH8VbeoHfQoyeYHKcJQTKrc8ustrc
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: Only Alexis Ruiz and Reet Mand appeared from Redis during this sync. The other invitees (Megan Boone, Rebekah Reddis, Fung-Lin Wu, Andy Varshneya, Allison Gregory, Claudia Di Martino, Regine Carreras) were not speakers and are listed as calendar invitees only.
</metadata>

---

## Summary

Erik O'Brien (GrowthX) and Alexis Ruiz (Redis) reviewed January's content performance (18 articles, 1.7k+ sessions, 43 LLM referrals, 2 Free Cloud Trial signups) and aligned on a major workflow shift: GrowthX will auto-publish articles without PMM review, with weekly Slack summaries for visibility. The team identified Hand Raisers (decision-maker leads) as the primary conversion goal over Free Cloud Trials, and Erik committed to analyzing past content to reverse-engineer Hand Raiser drivers. Redis's AI visibility improved to 50% in tracked LLM prompts, and GrowthX is launching a new tool (competitor to Profound/Scrunch) with 100k+ historical prompts for seamless tracking.

---

## Context

Redis and GrowthX are in month two of a content marketing partnership. GrowthX (a B2B content marketing agency) was brought on to drive AI visibility and lead generation for Redis through organic content. This weekly sync reviews performance metrics and aligns on content strategy and workflow optimizations. Erik O'Brien leads the GrowthX content team; Alexis Ruiz manages content requests from the Redis PMM team, and Reet Mand (joining this call) represents the broader Redis marketing leadership interested in the business impact of the content investment.

---

## Relevance

**To GrowthX Delivery:**
- New content workflow reduces friction: auto-publish without PMM review, except for "competitor vs." articles (Jim T. continues to review those). Weekly Slack summaries provide PMM visibility without blocking publication.
- Quality threshold identified: Flag articles reaching 150 views/week for deeper PMM review, linking content velocity to engagement-driven review.
- Table formatting issues in Sanity CMS persist; GrowthX has escalated an engineering ticket to improve the native table component. Manual table handling required until resolved.
- Topic-cluster author assignments needed in writing for consistency across content output.

**To CheckThat / AI Visibility:**
- Redis's AI visibility in LLM prompts grew from 42% to 50% in just one month of content publishing. GrowthX content is actively being cited by ChatGPT, Claude, and other LLMs.
- Expanded competitor tracking: Google Memory Store and ElastiCache added to the tracking list (previously tracking Pinecone, Weaviate).
- New tool launching (GrowthX competitor to Profound/Scrunch) provides access to 100k+ historical prompts, eliminating setup friction and enabling immediate visibility analysis.

**To GrowthX Business Development & Account Health:**
- Early conversion signals: 2 Free Cloud Trial signups (early for month two), but zero Hand Raisers yet. This indicates technical content resonates with practitioners but not yet decision-makers.
- Goal misalignment opportunity: Redis prioritizes Hand Raisers (high-intent decision-maker leads) over Free Cloud Trials (low-friction developer signups). Erik to reverse-engineer Hand Raiser content drivers and propose vertical-specific or decision-maker focused content (e.g., Industry Solutions cluster had highest engagement).
- February content goals: 3,000 sessions (2x January), increase trial signups, double LLM referral traffic, maintain 34% engagement rate.
- Strong momentum: Already over 1,000 sessions by Thursday of the first week; 7.8x week-over-week growth Jan 2–4. Regional breakdown aligned with Redis's paid campaign targets (83% from US, Singapore, China, India, Canada).

---

## Decisions & Commitments

- **Auto-publish without PMM review:** Effective immediately, GrowthX will publish articles without pre-publication review. Exception: Jim T. will continue to review "competitor vs." articles to ensure positioning accuracy.
- **Weekly PMM visibility:** GrowthX commits to sending a Slack summary each week with links to all published articles.
- **PMM review trigger:** Articles reaching 150 views in one week will be flagged to Alexis/Reet for deeper PMM review.
- **New content priority:** Jim's Redis 8.6 feature blog takes priority over previous requests and will publish the following week.
- **Hand Raiser focus:** Redis prioritizes Hand Raisers (decision-maker leads) as the #1 conversion goal over Free Cloud Trials. Erik will analyze past content to reverse-engineer Hand Raiser drivers and propose new content angles.
- **AI Visibility tool launch:** GrowthX is launching a new tool (competitor to Profound/Scrunch) with 100k+ historical prompts. Redis will receive direct access; Erik will schedule a demo for Alexis and Reet.

---

## Open Questions

- How should content be segmented between Practitioners (Free Cloud Trial audience) and Decision Makers (Hand Raiser audience)? Industry Solutions had the highest engagement; should GrowthX expand vertical-specific content?
- What is the conversion attribution model if trials come from one article type but Hand Raisers come from another? (GA4 tracks both separately, but strategy alignment needed.)
- When will the Sanity table component be improved to handle tables natively? (Engineering ticket is open but deprioritized during product launch.)

---

## Overview

- **New Workflow:** GrowthX will auto-publish articles without PMM review. A weekly Slack summary will be sent for PMM visibility.
- **January Performance:** Strong start with 18 articles published, 1.7k+ sessions, and 43 LLM referrals. Two Free Cloud Trial signups occurred, a positive signal for month two.
- **Conversion Priority:** The primary goal is "Hand Raisers" (decision-maker leads), not "Free Cloud Trials" (developer signups). GrowthX will analyze past content to reverse-engineer Hand Raiser drivers.
- **AI Visibility:** Redis leads competitors (Pinecone, Weaviate) with 50% visibility in tracked LLM prompts, up from 42%. Google Memory Store will be added to tracking.

---

## Key Topics

### January Performance Review

  - **Content Output:** 18 articles published, 1.7k+ sessions, 43 LLM referrals.
  - **Traffic Growth:** Sessions grew 7.8x from week 2 (122) to week 4 (953).
  - **Regional Traffic:** 83% from US, Singapore, China, India, Canada.
      - This aligns with paid traffic data, validating the content's reach.
  - **Topic Cluster Performance:**
      - **LLM Optimization & App Speed:** Dominant (53% of traffic).
      - **Vector Database & RAG:** Tied for \#2 (14% each).
      - **Industry Solutions:** Highest engagement rate → signals value of vertical-specific content.
      - **Agent:** Above-average engagement → supports Redis's strategic shift from cache to AI agent infrastructure.
  - **Conversions:**
      - **Free Cloud Trials:** 2 signups from technical LLM content.
      - **Hand Raisers:** 0 signups.

### New Content Workflow

  - **Publishing Process:** GrowthX will auto-publish articles without PMM review.
      - **Exception:** Jim T. will continue to review "competitor vs." articles.
  - **PMM Visibility:** GrowthX will send a weekly Slack summary with links to all published articles.
  - **Performance Review Trigger:** GrowthX will flag articles reaching 150 views in one week for a thorough PMM review.
  - **Table Formatting:** GrowthX will ensure correct table formatting in Sanity, as simple copy-paste fails.
      - An engineering ticket is open to improve the native table component.

### PMM-Requested Content

  - **New Priority Blog:** A draft on a new Redis 8.6 feature will be prioritized over a previous request from Jim T.
  - **Author Assignment:** Alexis will provide a list of authors for each topic cluster to ensure consistency.

### AI Visibility & Tooling

  - **AI Visibility:** Redis leads competitors with 50% visibility in tracked LLM prompts (up from 42%).
  - **Competitor Tracking:** Google Memory Store will be added to the tracking list.
  - **New Tool Launch:** GrowthX is launching a competitor to Scrunch/Profound.
      - **Benefit:** Provides access to a historical library of 100k+ prompts, eliminating the need to start tracking from scratch.
      - **Access:** Redis team will receive direct access.

---

## Action Items

**Erik O’Brien (GrowthX)**
- Prioritize Jim’s Redis 8.6 blog; publish next week
- Slack Alexis weekly published-article links
- Ensure tables in blog posts render correctly in Sanity
- Monitor article views; ping Alexis/Reet at 150/wk for PMM review
- Remind Gabby of new publish-without-review process
- Update today’s articles to publish-without-review
- Add total rows to LLM referral tables in Looker
- Grant Reet Looker access; Slack dashboard link
- Analyze hand-raiser content; propose ideas to Alexis/Reet
- Add MemoryStore and ElastiCache to AI visibility tracking
- Schedule AI visibility tool demo w/ Alexis & Reet
- Share Jan performance deck in Marketing Private Slack

**Alexis Ruiz-Pedregon (Redis)**
- Confirm w/ Jim T review for vs articles; then inform Erik
- Slack Erik topic-cluster author assignments

---

## Transcript
**Alexis Ruiz:** Sorry about that.

**Alexis Ruiz:** Got stuck in another meeting.

**Erik O'Brien:** No worries.

**Erik O'Brien:** I figured that much.

**Alexis Ruiz:** Yes.

**Alexis Ruiz:** How are you?

**Erik O'Brien:** Doing well.

**Erik O'Brien:** How's your week going?

**Alexis Ruiz:** It's going good so far.

**Alexis Ruiz:** What about yours?

**Erik O'Brien:** Pretty good.

**Erik O'Brien:** It's a little quieter than normal, which is always welcome.

**Alexis Ruiz:** Yeah, that's nice.

**Erik O'Brien:** Deeper work done and got to spend a little time getting your guys' January performance report together.

**Alexis Ruiz:** Awesome.

**Alexis Ruiz:** Great.

**Alexis Ruiz:** I think it might just be me.

**Alexis Ruiz:** Reed might join.

**Alexis Ruiz:** I'm not sure.

**Alexis Ruiz:** She was on the last call with me.

**Alexis Ruiz:** And then Feng Lin will be unable to join today.

**Alexis Ruiz:** But I do have a few things as well for you.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Do you want to start?

**Alexis Ruiz:** Sure.

**Alexis Ruiz:** Sure.

**Alexis Ruiz:** Yes.

**Alexis Ruiz:** So the first thing is, I know I've already asked you, Jim had suggested another topic for a blog that I passed over to you all.

**Alexis Ruiz:** And he hasn't.

**Alexis Ruiz:** Another one.

**Alexis Ruiz:** I wanted to see what that process is because I know you all have like slated blogs too every week.

**Alexis Ruiz:** So I wanted to get your feedback on that.

**Alexis Ruiz:** Again, this one is already drafted and it looks like a fair, like pretty simple blog.

**Alexis Ruiz:** It's kind of more of like a what is title.

**Alexis Ruiz:** So I just wanted to see what Gerald's thoughts are on like that process when we have, when we do have those requests from PMM.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I mean, feel free to send them over.

**Erik O'Brien:** You can easily fit them into the schedule and like probably prioritize them since it's something they're interested in.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** Yeah.

**Erik O'Brien:** So for his first one, we're going to work on that one next week.

**Alexis Ruiz:** Okay.

**Erik O'Brien:** And then this latest one, we can kind of just put it into the queue and have it ready probably in a couple of weeks.

**Alexis Ruiz:** Okay.

**Alexis Ruiz:** Got it.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** This is going to be, honestly, I think maybe this one should be priority over the other one.

**Erik O'Brien:** And I can send it over via Slack right now.

**Erik O'Brien:** Okay.

**Alexis Ruiz:** And it's about a new feature that's launching with Redis 8.6, I believe.

**Alexis Ruiz:** So I think this one would probably.

**Erik O'Brien:** Probably, I guess, have more priority over the previous one.

**Erik O'Brien:** We can easily do that.

**Alexis Ruiz:** Okay, awesome.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** Absolutely.

**Alexis Ruiz:** And then, oh, yes.

**Alexis Ruiz:** So for articles moving forward, and I know you just sent a few in our Slack channel, Fungland is saying we are able to move forward with just publishing without any reviews.

**Alexis Ruiz:** But if you can Slack us once a week with the articles that have been published.

**Alexis Ruiz:** So, you know, just kind of how you're doing already, but just maybe with, like, the links to the articles that were published.

**Alexis Ruiz:** And then we'll forward that over to the PMM team in case they want to, like, feel like skimming.

**Erik O'Brien:** But, like, we are good to go to just publish automatically.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Wonderful news.

**Alexis Ruiz:** Yes.

**Alexis Ruiz:** And in that, if the last thing was to just, oh, make sure that the table formatting, I know the tables aren't as, like, friendly in our blog template.

**Alexis Ruiz:** But if your team can just.

**Alexis Ruiz:** Just make sure when there are tables, if that formatting is correct.

**Erik O'Brien:** We've just seen a lot of issues with that lately, just in general.

**Erik O'Brien:** Yep.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I caught another one last week after you shared that first article.

**Erik O'Brien:** And so I went back and updated those.

**Erik O'Brien:** But we've shared it with our publishing team and with Gabby in case she has the time to go in and publish.

**Erik O'Brien:** So we'll make sure tables are handled accordingly.

**Alexis Ruiz:** Okay, great.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** I don't have access to Sanity, so I'm not sure exactly how it works on the back end.

**Alexis Ruiz:** But I'm assuming just a simple copy-paste of the tables is not working.

**Alexis Ruiz:** That's probably the issue there.

**Alexis Ruiz:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** And that's what I told the team.

**Erik O'Brien:** I was like, I'm not sure if you worked in Sanity, but it does not auto-format tables.

**Erik O'Brien:** So I've shared kind of the standard table that you guys use, at least the component that's used across other blogs.

**Alexis Ruiz:** Okay, perfect.

**Erik O'Brien:** I had a ticket out to our engineering team just to ask.

**Erik O'Brien:** I'm like, is there other formats that we can do this component in?

**Erik O'Brien:** And so I'm still waiting to hear back from them.

**Erik O'Brien:** We're doing a bit of a product launch this week.

**Erik O'Brien:** So they are inundated with other requests, but I'm hoping in the next week or so we can get some clarity on how we might be able to update that component to make it look a little bit more friendly with the rest of the blog.

**Alexis Ruiz:** Got it.

**Alexis Ruiz:** Okay, thank you.

**Alexis Ruiz:** Yeah, thanks for checking on that.

**Alexis Ruiz:** And then lastly, and since we're going to just have you all publish articles automatically moving forward, would you all be able to tell us, keep an eye out when an article reaches like 150 views in a week to ping us?

**Alexis Ruiz:** Because that's when we will have PMM like review those just, you know, because that means, you know, the article is getting more views.

**Alexis Ruiz:** So we definitely want to do a more thorough review.

**Alexis Ruiz:** And so I think that's how we figured it out.

**Erik O'Brien:** Absolutely.

**Erik O'Brien:** So for the blog.

**Erik O'Brien:** I sent over today.

**Erik O'Brien:** We're going to skip PMM review for those.

**Alexis Ruiz:** Yeah, I think so.

**Alexis Ruiz:** Because the last ones you sent last week are the ones with their review right now.

**Alexis Ruiz:** We said we would do one last pass-through.

**Alexis Ruiz:** I think going forward, I'll double-check with Fung Lin because she said all articles moving forward.

**Alexis Ruiz:** But I think we still might want to have Jim Tessier, Jim T, review the competitor kind of versus ones.

**Alexis Ruiz:** I was to ask him that.

**Alexis Ruiz:** Yeah, and he does have the bandwidth, I think, as he's mentioned, to review those.

**Alexis Ruiz:** yeah, just those going forward.

**Alexis Ruiz:** But the rest we can go ahead and automatically publish.

**Erik O'Brien:** Wonderful.

**Alexis Ruiz:** Got it.

**Alexis Ruiz:** And then lastly, I know we need authors for that.

**Alexis Ruiz:** Do we need to provide you, have we provided you all, I guess, based on the topic clusters, which authors to kind of just go between?

**Erik O'Brien:** I think we've probably discussed it, but it'd be great to have it just in writing.

**Alexis Ruiz:** Okay, got it.

**Alexis Ruiz:** I'll send a Slack after this.

**Erik O'Brien:** So with that, perfect. Right. Taking some notes so I don't forget to remind Gabby of this new process. All right. I'm sure I'm sharing the right screen here. Yeah. Okay. All right.

**Erik O'Brien:** So we did get six other articles published this week.

**Erik O'Brien:** So keeping pretty good momentum there.

**Erik O'Brien:** And then these are the ones we just shared.

**Erik O'Brien:** So I will update that to just to publish.

**Erik O'Brien:** But mainly I wanted to spend today on 26 or January 26 performance.

**Erik O'Brien:** So just at a high level, we got 18 articles published last month, over 1.7,000 a half hours.

**Erik O'Brien:** I'm sure

**Erik O'Brien:** And so with really good kind of week-over-week acceleration after the holidays, 43 LLM referrals with higher-than-average engagement for any kind of sessions that came from those referrals, which is typically what we do see.

**Erik O'Brien:** And then we had two trial signups for the free cloud trial.

**Erik O'Brien:** So saw the first conversions, which is really great, especially this early.

**Erik O'Brien:** Usually, we don't see it until like month three or four.

**Erik O'Brien:** And so given that we're seeing traction there, love to kind of carry on that momentum.

**Reet Mand:** Erik, can I ask a question?

**Erik O'Brien:** And I promise I will not derail.

**Erik O'Brien:** Yeah, no, please ask questions and derail whenever you feel like it.

**Reet Mand:** Can you, what is the LLM referrals?

**Erik O'Brien:** Can you just kind of walk me through that?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So in our Looker dashboard here, we track specific referrals from LLM.

**Erik O'Brien:** So majority of your referrals will come from Google.

**Erik O'Brien:** Like over 80% or 90%.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** You know, typically LLM referral rate's about 1% to 2% of total traffic, but we track specifically for our content, is it being cited in those kind of LLM chats, and if so, which one is it coming from?

**Erik O'Brien:** And so we can see kind of which landing page from which platform each of these was referred from.

**Reet Mand:** So stuff that we track in, it's also tracked in Google Analytics, but this is just a summary view that we pull into LinkedIn.

**Reet Mand:** Gotcha.

**Reet Mand:** So the way, if I'm looking at this dashboard right here, it says 17 sessions.

**Alexis Ruiz:** Sessions are visits, essentially?

**Reet Mand:** Yeah.

**Erik O'Brien:** And then 8 engaged sessions, which is either 10 seconds on the page or a scroll.

**Alexis Ruiz:** Gotcha.

**Alexis Ruiz:** Scroll or clicking, yeah.

**Reet Mand:** Gotcha.

**Reet Mand:** So this 16,000%, is that because we, is it, is this, is this, sorry, is this, am I looking at a monthly or yearly data here?

**Erik O'Brien:** This is just January.

**Reet Mand:** Okay.

**Reet Mand:** Okay.

**Reet Mand:** So that makes sense because we didn't have anything that we were tracking before, right?

**Erik O'Brien:** Yeah, we had, we probably had six articles in December.

**Erik O'Brien:** So overall, just, yeah, this is just siloed to the content that we produce.

**Alexis Ruiz:** Yeah, I was going to say this is just to the content that GrowthX has produced for us.

**Alexis Ruiz:** Yeah, because we definitely have had a lot of traffic from LLM's re that are just on.

**Alexis Ruiz:** Yeah, so now it's showing all traffic sessions.

**Reet Mand:** Yeah, perfect.

**Alexis Ruiz:** Perfect.

**Reet Mand:** That's really good.

**Alexis Ruiz:** Thank you.

**Alexis Ruiz:** yeah, so it's not as low.

**Alexis Ruiz:** It was just from our, the content from GrowthX, our new content.

**Erik O'Brien:** It's got new content.

**Reet Mand:** Gotcha.

**Reet Mand:** When you do your monthly review, Erik, I think it'll be good to kind of also see what percent of the traffic is coming or the sessions is coming.

**Reet Mand:** Like, is that percentage coming from GrowthX is growing over time?

**Reet Mand:** Do you know what I'm saying?

**Erik O'Brien:** Yep, absolutely.

**Erik O'Brien:** Yeah, I think our...

**Erik O'Brien:** Given that we're just seeing kind of compounding efforts of the content that we're producing, the goal that I've set for our content is to hit over 100 sessions next month.

**Erik O'Brien:** So doubling it because as we produce more content, that compounds over time.

**Erik O'Brien:** And so hopefully we'll continue to get picked up by the LLM traffic and continue to see these referrals scale.

**Erik O'Brien:** So, I actually have a quick, now that we're like just staring at this screen, a quick like ask, would it be, would you all be able to add a total table, a total row at the bottom of these tables so we can just like easily see like total numbers?

**Erik O'Brien:** Let me see if that's able.

**Alexis Ruiz:** Okay, thank you.

**Alexis Ruiz:** Yeah, just to like to add it up so we can easily see how we had like 100 sessions this month from LLMs.

**Reet Mand:** Um, Alexis, can you ping me this link, this dashboard?

**Alexis Ruiz:** Yes, of course.

**Alexis Ruiz:** Let me share that with you right now.

**Erik O'Brien:** Yeah, I'll throw it in the chat here.

**Alexis Ruiz:** Oh, great.

**Alexis Ruiz:** But also Slack it to you, me too.

**Reet Mand:** Yeah, me too.

**Alexis Ruiz:** So that way it can live in your Slack.

**Reet Mand:** Thank you so much.

**Reet Mand:** Like, literally, that's how I survive.

**Alexis Ruiz:** Yeah, yeah, I always refer back because sometimes Zoom doesn't do a great job.

**Alexis Ruiz:** Actually, Erik, you might have to add, Reet, I don't see access here.

**Alexis Ruiz:** Would we be able to give her access?

**Erik O'Brien:** Oh, absolutely.

**Erik O'Brien:** Remind me of your email real quick.

**Reet Mand:** Reet.mond at Gmail.

**Reet Mand:** Sorry, Reet.mond at Redis.

**Alexis Ruiz:** I have the same email for...

**Erik O'Brien:** .io, right?

**Alexis Ruiz:** .com.

**Erik O'Brien:** .com.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** For email, it's a .com.

**Reet Mand:** Thank you so much.

**Reet Mand:** This is a really great dashboard, though.

**Reet Mand:** Like, you all built it.

**Reet Mand:** This is one of the cleaner reports I have seen.

**Reet Mand:** .

**Reet Mand:** .

**Reet Mand:** .

**Reet Mand:** .

**Reet Mand:** Thank

**Erik O'Brien:** Yeah, we kind of simplified all of the noise that's in Google Analytics to kind of pull it down to what we want to track.

**Reet Mand:** It's really good.

**Erik O'Brien:** Thank you. Absolutely.

**Erik O'Brien:** So just getting through this content output, 20 articles delivered last month and 18 published.

**Erik O'Brien:** So we're almost at parity for one delivered, one published, which I think, you know, given the changes to reducing PMM review, we'll get more and more articles published.

**Erik O'Brien:** So we'll try to get through the backlog and get to over 20 this month.

**Erik O'Brien:** Just overall sessions, we saw traffic kind of grow week over week at 7.8x from kind of this week two baseline of 122 sessions to 953 by the end of January, which is really great momentum that we're seeing.

**Erik O'Brien:** This first week, we don't really count as it was like a half week and a holiday week as well.

**Erik O'Brien:** Plus we had little content published, but we'll hope to see.

**Erik O'Brien:** See this kind of trend continue, even if we did peak at kind of this week's performance, we've already gone over 1,000 sessions this week, and it's only Thursday.

**Erik O'Brien:** So love to see the momentum here, especially this early with content.

**Reet Mand:** Yeah, nice.

**Erik O'Brien:** Kind of regional breakout, over the sessions, we saw 67 different countries reached, but 83% are from these top five of the U.S., Singapore, China, India, and Canada.

**Erik O'Brien:** And then if we kind of look at more regional, it's about an even split between the Americas and EMEA, or sorry, AIPAC, with EMEA at about 7%.

**Alexis Ruiz:** That actually, like, aligns well with, like, what we see from, like, paid traffic, too, with this, like, out.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** Yeah.

**Reet Mand:** Pretty.

**Reet Mand:** Singapore?

**Alexis Ruiz:** That's interesting.

**Reet Mand:** Surprised to see Singapore on there.

**Alexis Ruiz:** Actually, we've been seeing a lot more.

**Alexis Ruiz:** Or Singapore traffic from paid as well, Reet.

**Alexis Ruiz:** So it's very interesting.

**Alexis Ruiz:** Like this breakout is pretty aligned with what we're seeing on paid too.

**Reet Mand:** Interesting.

**Erik O'Brien:** Overall cluster performance.

**Erik O'Brien:** So if we look at kind of just the topical clusters that we set during strategy, LLM optimization and app speed is pretty much dominating with over 53% of traffic, close to 1,000 sessions.

**Erik O'Brien:** And obviously we see significant growth, but given a kind of low January or sorry, December baseline, we'll kind of keep track of this.

**Erik O'Brien:** But we do like to see kind of overall is the topic cluster performing well.

**Erik O'Brien:** Average across all clusters, about 34% engagement.

**Erik O'Brien:** So it's right in line with our average here.

**Erik O'Brien:** Vector database coming in at number two with 14% of traffic and huge growth.

**Erik O'Brien:** We did publish quite a bit of content in that cluster.

**Erik O'Brien:** So stuff that we expect to see a little bit lower than our.

**Erik O'Brien:** Our typical engagement rate, and some of that might be because it was, you know, very top of funnel, given it's kind of the fundamentals, but we'll continue to track engagement over time and see if this improves.

**Erik O'Brien:** If not, we might need to get a little bit more depth in kind of the technical aspects of these Vector Database articles.

**Erik O'Brien:** RAG architecture coming in, tied with number two, about 14% of traffic, 235 sessions, and a little bit below average engagement, but stuff that we still see kind of resonating with technical audiences and their interest in these kind of, as RAG and different architectures continue to evolve, especially with the agent space, probably an area where we plan to grow content.

**Erik O'Brien:** Industry solutions was our highest engagement rate, so probably signals some interest that vertical-specific content is worth probably expanding into.

**Erik O'Brien:** We do have...

**Erik O'Brien:** A couple industry solution articles this week that we just shared.

**Erik O'Brien:** So we'll see if that trend continues with engagement rate and traffic sessions.

**Erik O'Brien:** And then last is agent performing above average and engagement rate.

**Erik O'Brien:** We've got quite a bit of agent content from last week that we just published and then this week.

**Erik O'Brien:** So, again, an area we want to keep expanding as, you know, Redis wants to move their perception from cache only to more of the AI agent infrastructure space.

**Erik O'Brien:** Like I mentioned, we had two trial signups, which is, again, this early in the engagement is really good to see.

**Erik O'Brien:** Again, not something we expected in kind of month two of publishing, but really good to see.

**Erik O'Brien:** And it wasn't really from kind of our top performers, but from these more kind of technical implementation focused content pieces of LLM content.

**Erik O'Brien:** Windows in single versus multi-agent systems.

**Erik O'Brien:** So, again, really positive signals that we're seeing trial signups this early.

**Erik O'Brien:** And I think a larger question for me is I know we're tracking about five or six different conversion events in GA4.

**Erik O'Brien:** Is there other ways that you guys track conversion events or other tools that you use to look at kind of overall attribution?

**Alexis Ruiz:** No, I think it would mostly just be GA4, especially from, like, web traffic and, like, organic paid sources.

**Alexis Ruiz:** So, yeah, and I mean, we have Salesforce, but that's already once, like, we get, like, the free cloud trial or the hand raisers.

**Alexis Ruiz:** So, really, we do go off of GA4 data.

**Erik O'Brien:** I think it's also the most accurate that we have seen.

**Erik O'Brien:** Okay, wonderful.

**Alexis Ruiz:** Wonderful.

**Erik O'Brien:** And then of those, we'll just pull it up here real quick. So of these conversion events, is there anyone that we would like to prioritize as the most valuable?

**Alexis Ruiz:** I would say obviously free cloud trial signup towards the bottom and then the hand raisers lead.

**Alexis Ruiz:** That would be like hand raisers.

**Alexis Ruiz:** That would be actual users coming in and, you know, filling out our form to book a meeting with us, which ultimately we want that, right, is the ultimate goal.

**Alexis Ruiz:** But when we, what we have seen is obviously we get a lot of free cloud trial signups because it's an easier entry, you know, barrier to entry there.

**Alexis Ruiz:** But yeah, those would be, I think, the two, I guess, priority ones.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Good to know.

**Erik O'Brien:** Thank you.

**Reet Mand:** Yeah, that was going to be my question as well. The trial signups make sense, but do we have the ability to track Hand Raisers?

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** And that's the always, that's the hand raisers one.

**Alexis Ruiz:** So yes, we are.

**Alexis Ruiz:** We just like, I guess by default, it makes sense that we're seeing free trials first over hand raisers because I feel like we always like see that even in like our paid campaigns.

**Alexis Ruiz:** But yes, we are able to track hand raisers and GA4 does track that.

**Reet Mand:** Okay.

**Reet Mand:** So this means we just haven't had any so far.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** Yeah, exactly.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** And it's pretty accurate.

**Alexis Ruiz:** We work closely with like Outshine to make sure that that's always updated those events in GA4.

**Reet Mand:** Eric, can I get your perspective on this?

**Reet Mand:** you know, every AI thought leader these days is saying that, you know, any traffic that comes from LLMs is a high quality traffic and converts better.

**Reet Mand:** Like, you know, your people are actually wanting to learn more, meaning that's, that's a direct.

**Reet Mand:** Like contact us type of CTA in your experience and what you're seeing with other, with your other clients.

**Reet Mand:** Is that, is that, is that true?

**Erik O'Brien:** I would say it's, it's true for the most part.

**Erik O'Brien:** Like, it's not like a one-to-one comparison.

**Erik O'Brien:** If there is a free option, like we do see pretty consistent conversion from engagement.

**Erik O'Brien:** Engagement, engagement rates are definitely higher coming from LLM traffic.

**Erik O'Brien:** And then conversion is about, I'd say like five to six X higher on those LLM traffic with engaged sessions.

**Erik O'Brien:** And so it's something that we're continually tracking across different clients to kind of get a better like read of what's the actual like market number versus, you know, I have a pod of like six clients that I know pretty well.

**Erik O'Brien:** But I think.

**Erik O'Brien:** For Redis, it's something that, you know, we've just got early signals, so now we can kind of start to have a baseline of like, okay, we got two trial signups for the second month of publishing.

**Erik O'Brien:** In February, we hope to see this, you know, at least double, if not triple.

**Erik O'Brien:** And if so, then we're like on the right track of creating content that's well engaged with, that's getting cited by AI, and being able to kind of be at least close to bottom funnel, which allows us to continue to optimize kind of content in that area.

**Erik O'Brien:** I'll take a look, now that I have a little bit more clarity on like, what are the key metrics, to see what kind of content is performing for those hand raisers, and then be able to kind of reverse engineer some new content ideas that we can go after for maybe leading to those more sales-oriented conversations.

**Alexis Ruiz:** Yeah, that would be great.

**Alexis Ruiz:** I think that's like a conversation we've been having.

**Alexis Ruiz:** Internally, as well as like, I think, you know, free trial signups are obviously geared more towards like the practitioners and developers, whereas like those hand raisers, it really is more geared towards those decision makers that are actually going to, you know, make that decision to, you know, sign up with, you know, I guess, make, you know, I guess convert with redis.

**Alexis Ruiz:** So maybe that's also something to think about, too, is like, maybe should our content kind of also be split in that way, like practitioner versus decision maker?

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah, I think the industry solutions is probably our closest decision maker content.

**Erik O'Brien:** So, but I'll take a look and kind of go through just all content that you guys have and specifically look at hand raisers.

**Erik O'Brien:** And then I can see like, I'll have it break out landing pages here and kind of do some research of what blog posts or editorial content is leading to more hand raisers than average.

**Reet Mand:** Yeah, that that's like.

**Reet Mand:** I our, you know, from a number one goal is hand raisers.

**Alexis Ruiz:** Number two goal is free trial signups.

**Alexis Ruiz:** Yep.

**Reet Mand:** Okay.

**Reet Mand:** Sounds good.

**Erik O'Brien:** Cool.

**Erik O'Brien:** As far as AI visibility, since we started tracking, we did see growth from 42% visibility to over 50%.

**Erik O'Brien:** So that means for the 483 prompts that we're tracking, which, again, we'll have to divide this by seven.

**Erik O'Brien:** So it's somewhere around like 70-ish prompts that we're tracking.

**Erik O'Brien:** Redis shows up 50% of the time as a response.

**Erik O'Brien:** So overall, that puts it as number one ahead of Pinecone and WeV8 and other kind of competitors.

**Erik O'Brien:** So there's a quick view of this.

**Erik O'Brien:** This is kind of where we started when we first started tracking.

**Erik O'Brien:** And we're seeing steadily.

**Erik O'Brien:** Kind of increasing visibility as we continue to publish.

**Erik O'Brien:** It's been going up over January.

**Erik O'Brien:** So good signals that the content we're producing is being cited.

**Erik O'Brien:** And we can dive into all that in a different session or I can pull out the insights.

**Erik O'Brien:** But we can see specifically in the citations, like which one of our articles is starting to show up in these answers.

**Erik O'Brien:** And we, for the prompts that we are tracking, these should be a one-to-one parody of what you guys are tracking in Profound.

**Erik O'Brien:** When Cody was still here, he granted me access to Profound.

**Erik O'Brien:** And I basically went and took those prompts and uploaded them here so we could be a parody for kind of the data that we're seeing.

**Alexis Ruiz:** Perfect.

**Alexis Ruiz:** I was going to ask about that.

**Alexis Ruiz:** Do we have competitors of like Valky, Elastic Cache, Memory Store?

**Alexis Ruiz:** Oh, I see Valky.

**Erik O'Brien:** Memory Stories.

**Alexis Ruiz:** Elastic Cache.

**Alexis Ruiz:** And it would be like Google Memory Store.

**Alexis Ruiz:** That's one of our main competitors right after like ElastiCache.

**Erik O'Brien:** I will add these guys to our list.

**Alexis Ruiz:** I mean, they're naming us right there.

**Alexis Ruiz:** Yeah.

**Erik O'Brien:** Yeah.

**Alexis Ruiz:** Yes, thank you.

**Alexis Ruiz:** But yeah, I was going to ask because, you know, we have, we use Profound, which I know is like probably the competitor of Scrunch.

**Alexis Ruiz:** So yeah, I was going to ask if it's the same prompts that we're tracking.

**Erik O'Brien:** Yep, it is.

**Erik O'Brien:** Okay.

**Erik O'Brien:** And then this is definitely something I'll dive deeper in a couple of weeks, but we do have, this is the product launch I was announcing or mentioned earlier.

**Erik O'Brien:** We are launching basically a competitor to Scrunch and Profound, except you don't have to set it up from scratch. It basically looks at entire categories of potential buyer queries and sorts them.

**Erik O'Brien:** Redis is in multiple different categories, but right now we have you in database management systems.

**Erik O'Brien:** And so this view that we're looking at for kind of the competitor view is basically a one-to-one parody of what we'll see in Scrunch.

**Erik O'Brien:** And then for the prompts, this is where we have like a library of over a hundred thousand prompts that we're tracking since I believe November.

**Erik O'Brien:** And so if we wanted to add new prompts from like the shared library, we could go in, add those, and then it'll have all historical data instead of having to start from scratch.

**Erik O'Brien:** So I'll do a deeper dive demo on this.

**Erik O'Brien:** Today is launch day.

**Alexis Ruiz:** So we're expecting a few bugs.

**Reet Mand:** Really cool.

**Alexis Ruiz:** Yeah, super cool.

**Alexis Ruiz:** Awesome.

**Alexis Ruiz:** And we'll get access to view this as well, right?

**Erik O'Brien:** Yeah, you guys will have direct access.

**Erik O'Brien:** So you won't have to like look at screenshots reports anymore.

**Erik O'Brien:** can kind of just dive.

**Erik O'Brien:** to

**Alexis Ruiz:** I know we're almost at the end.

**Reet Mand:** Alexis, this is a really, really great update and really good progress.

**Reet Mand:** Erik, thank you so much.

**Reet Mand:** I think it'll be good to add this to our marketing private channel.

**Alexis Ruiz:** Yes.

**Reet Mand:** If you can, I think there's just a lot of interest in this and really good data.

**Reet Mand:** And people can see all the work that they've been doing, you know, how it's starting to like have real business impact.

**Alexis Ruiz:** Yes.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** I could definitely share in marketing private.

**Alexis Ruiz:** Erik, if you don't mind sharing this deck with us.

**Erik O'Brien:** Yep.

**Erik O'Brien:** It's in this monthly report.

**Alexis Ruiz:** Oh, perfect.

**Erik O'Brien:** Okay.

**Erik O'Brien:** I'll share it there, but it's like, it's got the Google slides.

**Alexis Ruiz:** Got it.

**Alexis Ruiz:** I'll the link to this right after our call.

**Alexis Ruiz:** Okay, great.

**Alexis Ruiz:** Thank you.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** I'll also log in.

**Reet Mand:** Yeah.

**Reet Mand:** Really good update.

**Erik O'Brien:** Thank you.

**Erik O'Brien:** Absolutely.

**Erik O'Brien:** I think the last one I want to touch on.

**Erik O'Brien:** And the rest of you guys can kind of look through, but these are just some content goals that we want to kind of put in place for ourself.

**Erik O'Brien:** Try to hit 3,000 sessions, so like 2X in January's performance, really start to drive a little bit more trial conversions and see what kind of optimizations we can do with either CTA blocks or other CTA callouts in content.

**Erik O'Brien:** And then, like I mentioned, let's get to kind of doubling our referral traffic from LLMs as content continues to compound.

**Erik O'Brien:** Everything else, we'll try to maintain steady state with slight growth and competitive presence for AI visibility, but engagement, we're going to target remaining at 34% or see if we can improve there.

**Reet Mand:** Awesome.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Well, thanks for the time today.

**Erik O'Brien:** I will share a link to all this so you guys have easy access to it from Slack, but let me know if any questions come up.

**Alexis Ruiz:** Got it.

**Alexis Ruiz:** Okay.

**Alexis Ruiz:** Thank you so much.

**Alexis Ruiz:** Yes, I'm on the slide deck, so no worries.

**Alexis Ruiz:** Okay.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** Thank you.

**Erik O'Brien:** All right.

**Erik O'Brien:** Thanks, team.

**Erik O'Brien:** Bye.

**Erik O'Brien:** Bye.
