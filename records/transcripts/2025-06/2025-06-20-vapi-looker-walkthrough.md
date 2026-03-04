# Vapi Looker Walkthrough

<metadata>
date: 2025-06-20
time: 12:07 UTC
duration: 20 minutes
organizer: darrell@growthx.ai
participants: Kirkland Gee, Darrell Etherington, Matthew Alves-Hill
fathom_recording_id: 69576200
fathom_url: https://fathom.video/calls/332393220
share_url: https://fathom.video/share/DRmFx8SVUz7f64S9wHkaS52mjo--ieVS
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Kirkland Gee from GrowthX walked Darrell Etherington and Matthew Alves-Hill through critical issues in their Looker Studio setup for Vappy.ai, revealing that cohorting reduced click counts by up to 65% (83 vs. 294 clicks) due to sampling, fixing LLM referral tracking to show Perplexity as the dominant source, and establishing two data filtering strategies (data source filters and custom report filters) for the vappyai.blog subdomain. The team agreed that Looker Studio numbers are directionally correct for strategy but require careful client communication about data limitations, with Darrell committing to create an educational video walkthrough explaining GSC's three anonymization tiers (UI, API, and BigQuery) and why Looker numbers diverge from raw data.

---

## Context

Vappy.ai is a client using Looker Studio to monitor their SEO performance across Google Search Console data. Darrell Etherington, a GrowthX analyst, requested a detailed walkthrough from Kirkland Gee, an experienced Looker expert (currently dealing with product launch work), to debug data discrepancies in their reporting dashboard. Matthew Alves-Hill, who appears to be on the Vappy.ai team, joined to understand the data structure and limitations. The meeting was recorded as a reference for the broader team, indicating that similar questions were expected from other stakeholders who need to understand why Looker numbers don't match GSC directly.

---

## Relevance

- **To GrowthX Delivery:** Looker Studio is a core tool for client reporting; this session surfaced a critical data accuracy limitation (cohorting reduces clicks by 50-65%) that requires proactive client communication. The team identified a pattern: Looker API data differs from GSC UI/BigQuery, and setting proper filters (left outer joins, null exclusions, regex filters) is essential for accurate dashboards. Kirkland noted that GrowthX should build equivalent reporting into Atlas to escape these limitations.

- **To GrowthX Business Development:** Vappy.ai's team is data-hungry ("antsy on numbers") and focused on traffic metrics; without clear explanation of Looker's constraints, they may lose confidence in GrowthX's reporting. The video walkthrough Darrell committed to will be critical for expectation-setting and retention.

- **To CheckThat:** Kirkland mentioned AI referral tracking revealed Perplexity as the dominant LLM source for Vappy (with Claude showing 73 sessions), with minimal ChatGPT traffic. This pattern may be relevant for CheckThat's visibility research if Vappy is a benchmark site for AI visibility trends.

---

## Overview

- Looker Studio has significant data discrepancies, often showing fewer clicks (up to 50% less) compared to raw GSC data due to cohorting and sampling issues
- LLM referral tracking was fixed by adjusting filters to use session source instead of page refer, revealing Perplexity as the dominant source
- GSC data can be limited to specific domains (e.g., vappyai.blog) using custom filters, but care must be taken to explain data limitations to clients

---

## Key Topics

### Cohorting Data Issues

  - Null values appear when data isn't specifically cohorted
  - Solution: Add filters to exclude null clusters in individual charts
  - Cohorting significantly reduces click numbers (e.g., 83 vs. 294 clicks for the same period)
  - Cohorted data is directionally correct but not numerically accurate

### LLM Referral Tracking

  - Fixed by changing 'page refer' to 'session source' in filters
  - Added regex to match various AI platforms
  - Excluded VAPI to avoid self-referrals
  - Results showed Perplexity as the dominant source, with some traffic from Gemini and minimal from ChatGPT

### GSC Data Filtering

  - Two methods to limit data to vappyai.blog:
    1.  Add filters to data sources
    2.  Create and apply custom filters (e.g., "VappyBlog" filter)
  - Non-branded filter created using regex to exclude Vappy variations and misspellings
  - Filters can be applied to individual charts as needed

### Data Accuracy and Reporting

  - Three levels of GSC data anonymization: UI (most sampled), API (used in Looker), and BigQuery export (most accurate)
  - Looker Studio numbers may differ from GSC UI, with Looker potentially showing more traffic
  - Up to 90% of data could be anonymized or removed in UI/API for high-traffic websites
  - Importance of explaining data limitations to clients to manage expectations

---

## Action Items

**Darrell Etherington (GrowthX)**
- Create video walkthrough of Looker Studio setup explaining data accuracy limitations and GSC's three anonymization tiers (UI, API, BigQuery)

**Kirkland Gee (GrowthX)**
- Set up remaining pages in Looker Studio for Vappy.ai (committed to completing today)

---

## Transcript
**Kirkland Gee:** So go to like a little play cafe. So I was like, I'm just going to crank out a couple of hours of work before the day really gets ahead of me. So just, I think these are all pretty simple. Yeah.

**Kirkland Gee:** The first one, I actually don't know if I'm going to figure out, but the other two are really straightforward.

**Kirkland Gee:** So let me, so basically let's go back to the, this cohorting one first.

**Kirkland Gee:** So what happened here, you'll still get a lot of nulls because if something's not specifically cohorted, then it's just going to come in as null.

**Kirkland Gee:** If you want to avoid that, you can just filter this data source either here and like, say, where create a filter.

**Matthew Alves-Hill:** Like, we probably want to do this.

**Kirkland Gee:** So we only want to pull things. Actually, wait, that's wrong.

**Kirkland Gee:** You'd have to do it on each individual chart, but you would just add a filter, call it cluster, in the cohorted page data, exclude anything where cluster is null, and then that will just remove all that extra stuff.

**Kirkland Gee:** The overall numbers, I mean, they're only going to show, again, places where we actually have that data.

**Darrell Etherington:** Which is probably only the stuff we've done for them so far.

**Darrell Etherington:** yeah.

**Kirkland Gee:** So if it's clustered, that's because it has a cluster assigned to it in Airtable.

**Kirkland Gee:** Yeah, yeah. Otherwise, that data does not exist here. That's just how that works. There's no real way around it.

**Kirkland Gee:** So you just want to do that on the other charts, too.

**Kirkland Gee:** And you can do the same thing down here.

**Kirkland Gee:** Does that make sense?

**Kirkland Gee:** Yep, absolutely.

**Kirkland Gee:** It wasn't working.

**Darrell Etherington:** It

**Kirkland Gee:** Was because here, so you have table one, which is GSC, table two, which is our Airtable data.

**Kirkland Gee:** Just a Google sheet that is synced to pull Airtable data once a day is how that works. But this was joining on record ID, not live URLs.

**Kirkland Gee:** So the join condition was wrong. And so therefore, nothing's actually joining.

**Kirkland Gee:** If you're ready to adjust this, you always want to do a left outer.

**Kirkland Gee:** So you want everything from GSC, right, everything from this left table.

**Kirkland Gee:** And then I only want to pull in things that have a match on live URL from the right table.

**Kirkland Gee:** Because otherwise, you'd be pulling in a bunch of data that's not relevant.

**Kirkland Gee:** That makes sense.

**Darrell Etherington:** Yeah, I've refreshed this just to, because the connector, I was getting the connector error.

**Darrell Etherington:** But like through your other tutorials and then like just searching their help docs, I figured that out. I didn't realize that part of the condition that you filtered by live, but that makes sense.

**Darrell Etherington:** Did you set up the cohort of data?

**Kirkland Gee:** Did I do this, or did you do this?

**Darrell Etherington:** No, the code of data was already set up. I couldn't remember if the Airtable was out of date. That was the only one, so it was breaking that, right?

**Kirkland Gee:** Okay, so that's that one. In terms of this LLM that page, I understand why this wasn't working now. Refer is the wrong thing.

**Kirkland Gee:** I don't know what field we actually need from their GA. Let's try a couple of things. Some people's Google Analytics are going to be set up so differently that this will get weird sometimes.

**Kirkland Gee:** What we're trying to do is just have session source. So we want session source, and then we'll add a new filter. We can add this regex that basically matches every AI platform that there is.

**Kirkland Gee:** So it just matches a bunch of different stuff. And we'll remove this one and save that. Now, VAPI is included, so we'll have to exclude session source contains VAPI.

**Kirkland Gee:** So now this is the landing page. This is the referrer itself. Well, and then we can add landing page back into this now. This way they can see where the sources are coming from to what pages.

**Kirkland Gee:** So really what's funny is they're only getting Perplexity. There's like 73 from Claude. Wait, this should be session source, not page refer. Hold on.

**Kirkland Gee:** There we go. It's still way more Perplexity than anything else. But a little bit of Gemini, yeah, ChatGPT does not show up much at all.

**Darrell Etherington:** What's the time stamp? From start of year, right?

**Kirkland Gee:** Year to date. That's fixed.

**Kirkland Gee:** And then you asked about, can you limit GSC to vappyai.blog? I think the filtration stuff will help with that. So if the client's like, "Hey, we have all our own reporting. I only care about the blog," then I would say go into your data sources themselves.

**Kirkland Gee:** You can add filters. You can always create a filter like VappyBlog. Landing page contains, we can just say contains blog/blog.

**Kirkland Gee:** And then we have to add that VappyBlog filter on all the individual ones. This is a non-branded report. So you'd also add another filter, create a filter that'd be non-brand, and we'll do exclude queries.

**Kirkland Gee:** Always do this as a regex. What I do is I go to an AI and ask, "Can you write me a regular expression that filters all variations and misspellings of Vappy?" Because if you just say contains Vappy, you're missing VAP, VAPPY, VAP space I, and all the weird misspellings. So you get a very comprehensive regex that catches all variations.

**Kirkland Gee:** That will catch any variations. We'll add that on this one, too. With the cohorted data, you could add a filter and just say I only want my Vappy blog and non-brand. Blog makes sense because this other stuff is all on the blog. Is that all making sense?

**Darrell Etherington:** Yes.

**Kirkland Gee:** These reports aren't filtered like that at all. You can apply it wherever on the same data source and it'll still work.

**Kirkland Gee:** The only thing you have to keep track of in these reports is there may be some bugs where at one time I had almost everything using cohorted data because I wanted to use the same data everywhere. But the problem is when you cohort data, Looker just deletes half of the clicks. If you look at the same page in the cohorted data versus just the GSC data over the same time frame, you might see literally half the clicks.

**Kirkland Gee:** That's something to tell the client: when we're cohorting this data, it's directionally correct. Is it going up or down? That will be the same.

**Darrell Etherington:** It has internal logic, but it's not externally true.

**Kirkland Gee:** They're doing some sampling or weird stuff in the SQL behind the scenes to make it more efficient.

**Kirkland Gee:** For vappyai.blog, this SMS Twilio got 83 clicks in the cohorted data. When I changed it to just plain GSC data, it's 294 for the same time period. That's significant.

**Kirkland Gee:** It's unreal. I've done tons of research trying to understand why that happens. 83 versus 294 on the same time period. Just a big discrepancy.

**Kirkland Gee:** When I was at ClickUp, we dealt with this so much that we just had to give up on Looker. Looker did not work for us.

**Darrell Etherington:** If it's additive to your existing solution, if we're just using it for analysis and strategy changes, then sure.

**Kirkland Gee:** You need to be able to say, "Are they getting clicks? Are they getting impressions? Which pages are moving up? Which pages aren't by category?"

**Kirkland Gee:** But if you're doing reporting on "we generated this many clicks," you can't filter it like this. Clients are going to be really upset if you don't explain it correctly, but it's just a limitation of Looker.

**Kirkland Gee:** Eventually we're going to build our own reporting solution into Atlas and do our own syncs to GSC and solve all of this, but that's not today.

**Darrell Etherington:** Every analytics suite we ever used had the caveat that numbers are not representative of real numbers.

**Matthew Alves-Hill:** They're just representative of direction.

**Kirkland Gee:** But I think that's everything in here now.

**Kirkland Gee:** And then this last tab is just a couple of tables of like all the data put together so you can export them.

**Kirkland Gee:** That's all this is.

**Kirkland Gee:** Yeah, okay.

**Kirkland Gee:** That's what I figured with this one.

**Darrell Etherington:** I think I did something to make them produce a visual.

**Darrell Etherington:** I can't remember what, but yeah, I got the sense like, oh, this is just for when they want takeaways or whatever takeouts.

**Darrell Etherington:** Yeah, this is literally like I don't want to go to search console and wait for it to load for 10 minutes.

**Kirkland Gee:** I just want to export my data.

**Kirkland Gee:** Get it into a Google Sheet and do something with it.

**Kirkland Gee:** That's all this is.

**Kirkland Gee:** And this is the data by date.

**Kirkland Gee:** So if you wanted to look at some, you know, I don't know.

**Kirkland Gee:** I used to do so much of that manual stuff that like as nice as recording dashboards are, I always feel like when you're really trying to figure something out, sometimes it's just easier to pull it yourself.

**Kirkland Gee:** We use X at ClickUp, which is like a very cool.

**Kirkland Gee:** It's like you can basically a Jupyter notebook with a bunch of built-in fancy charts and reporting stuff.

**Kirkland Gee:** so I could anytime someone had a question, I could just go write SQL and just do it that way.

**Kirkland Gee:** And like, I want us to get to a place that we have something like that.

**Kirkland Gee:** Nice.

**Darrell Etherington:** But anyway, any other questions?

**Kirkland Gee:** that help?

**Kirkland Gee:** No, that helped tremendously.

**Darrell Etherington:** Yeah, I think.

**Darrell Etherington:** And I've recorded this, so hopefully it will help the others, too.

**Darrell Etherington:** know some of directors are like, we don't know what's going on with this stuff.

**Matthew Alves-Hill:** I've never watched this a hundred times.

**Matthew Alves-Hill:** Yeah, Looker, I mean, I've been worried.

**Kirkland Gee:** Me and Looker now for five years, and it still trips me up on just little things.

**Kirkland Gee:** It's super annoying.

**Kirkland Gee:** And then there's the stuff where you'll beat your head against the wall.

**Kirkland Gee:** mean, why are these numbers different?

**Kirkland Gee:** What's wrong?

**Kirkland Gee:** Nothing's wrong.

**Matthew Alves-Hill:** I think that team is so, you know, they're just antsy on numbers.

**Matthew Alves-Hill:** want to see, like, they're like, I want to see, you know, like, how much data we Like, how many clicks, how many, like, people are clicking, many people are coming through, like, traffic, traffic, traffic.

**Matthew Alves-Hill:** So when we share this with them, I think maybe that's going to be, like, maybe they're going to get frustrated.

**Matthew Alves-Hill:** Yeah, they might be.

**Darrell Etherington:** Well, we'll have to, you know, I'll contextualize in the video, like, in a quick walkthrough that the numbers are not represented.

**Darrell Etherington:** We can go to GSC for source of truth on real numbers and stuff like that, like, after we filter, like, post-coordering.

**Kirkland Gee:** One more thing that's just relevant to know, and this is another one of stupid looker things.

**Kirkland Gee:** Okay?

**Kirkland Gee:** The data that's just pulling directly from GSC, right?

**Kirkland Gee:** That's not cohorted.

**Kirkland Gee:** Those numbers, if you compare them to the UI, will also be different. There will probably be more traffic in Looker Studio than in GSC UI, and the GSC data is closer to right. There's still something missing, but it's closer.

**Kirkland Gee:** There are three levels of anonymization with GSC data. The UI does a ton of sampling, you only get 1,000 rows, useless. Then there's the API, which gives you up to a certain number of rows per day with some limitations, but it's better. That's what you're getting in Looker. Then there's Google BigQuery data export where you bulk export everything out of GSC into BigQuery every day. That's the only way to get 100% of your data from Looker.

**Kirkland Gee:** On smaller websites, the gaps aren't that big. There was a tech SEO conference in Raleigh last year where someone from Jet Octopus did a fascinating talk on this. He found that as much as 90% of data on a high-traffic website could be anonymized or removed in UI or API. I linked it in the Slack thread. If you know this stuff, it's easier to explain to clients why all the numbers are whack. It's a whole mess.

**Darrell Etherington:** Very helpful. All right, I'm going to watch that too. I have to pretend like I know all this stuff cold.

**Kirkland Gee:** Hey, you could know eventually.

**Kirkland Gee:** Data is so annoying to deal with in SEO because people expect it to just work. They're used to paid ads where most of it works because you're paying money for that data versus it just happening. Anyway, I'll get those pages up today as well.

**Matthew Alves-Hill:** Appreciate it.

**Kirkland Gee:** Thanks.

**Kirkland Gee:** I'm learning a lot about product. I've done workflow development but never been part of a launch like this. Had we had more time to get out of our no-code tool, maybe this wouldn't have been quite as crazy.

**Darrell Etherington:** Yeah, I think so, too. Over the course of the week, it's so dramatic.

**Kirkland Gee:** All right, I'll get back to it.

**Darrell Etherington:** Thanks a lot. Take care.

**Matthew Alves-Hill:** Take care.
