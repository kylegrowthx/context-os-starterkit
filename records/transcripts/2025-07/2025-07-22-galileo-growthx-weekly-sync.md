# Galileo<>GrowthX Weekly Sync

<metadata>
date: 2025-07-22
time: 17:00 UTC
duration: 41 minutes
organizer: Vivek Shankar
participants: Osman Javed, Shohil Kothari, Conor Bronsdon, Jason Garoutte, Mara Leighton, Usman Adepoju, Jackson Wells, Vivek Shankar
fathom_recording_id: 75715228
fathom_url: https://fathom.video/calls/357724543
share_url: https://fathom.video/share/3yxy5q1N-ZtiiJs9MnRxkKLpv2obwXzR
source: fathom
enriched_on: 2026-03-03 15:30 UTC
</metadata>

---

## Summary

Galileo and GrowthX discussed SEO performance challenges and LLM visibility strategy. A significant data discrepancy (5-10x) emerged between Google Search Console and SEMrush ranking reports, prompting Jackson Wells and Vivek Shankar to investigate US-specific filters and validate keyword lists. The team presented Scrunch, a new LLM-tracking tool recently onboarded to monitor how Galileo appears in ChatGPT, Perplexity, and other AI models across custom prompts; meaningful data will arrive in 3-4 weeks. Jason Garoutte requested a sentiment-based "NPS-like score" to gauge model favorability towards Galileo, shifting focus from traditional search referrals toward LLM mentions and authority signaling.

---

## Context

Galileo is an AI evaluation platform and a strategic partner of GrowthX. This weekly sync is part of GrowthX's content strategy delivery work with Galileo, where GrowthX is helping Galileo navigate the shift from traditional SEO and search-driven content to AI-driven discovery in ChatGPT and other LLMs. The partnership is exploring how to strengthen Galileo's authority on core topics so the tool gets mentioned and cited in AI model responses — a growing traffic driver for AI-native SaaS companies. This particular meeting was focused on validating SEO metrics and kicking off Scrunch implementation, marking a pivot in how Galileo measures content success from clicks to LLM presence and sentiment.

---

## Relevance

**To GrowthX Delivery:**
- Shift from traditional SEO metrics to LLM visibility metrics requires new measurement frameworks and tools (Scrunch). GrowthX must develop advisory approaches for clients evaluating LLM-based content strategies.
- Discrepancies in SEO ranking data (5-10x difference between GSC and SEMrush) highlight the need for multi-platform validation before making strategic decisions with clients. This informs GrowthX's SEO audit processes.
- Scrunch's NPS-like sentiment score feature (proposed by Jason) is a compelling internal metric GrowthX could adapt for other clients evaluating AI visibility.

**To CheckThat & AEO:**
- Galileo is using Scrunch to monitor mentions and sentiment across three LLMs, directly validating CheckThat's core value proposition: tracking and optimizing AI visibility.
- The conversation about sentiment thresholds ("ChatGPT 70% positive, Perplexity only 40%") directly mirrors the need for AI visibility scoring products.

**To GrowthX Business Development:**
- Galileo is already spending budget on LLM-specific tooling (Scrunch) and requesting account-level visibility and strategy consultation, signaling potential expansion of the GrowthX engagement.
- Jason Garoutte's involvement and high-level questioning indicates strong executive engagement and confidence in the partnership. Recommend seeking expansion discussion in the 3-week follow-up.

---

## Overview

- Discrepancies in SEO ranking data between tools need investigation (SEMrush vs. Google Search Console)
- Team is implementing Scrunch for LLM-based content performance tracking; data will be more meaningful in 3-4 weeks
- Concerns raised about potential decline in organic traffic and shift towards AI-driven content discovery
- Focus on strengthening Galileo's authority on key topics for better LLM mentions and citations
- Jason Garoutte requested a net promoter score-like metric to measure sentiment across LLMs and competitors

---

## Key Topics

### SEO Performance Discrepancies

- Significant difference (5-10x) in ranking data between SEMrush and Google Search Console
- Hypothesis: Discrepancy could be due to US vs. global filter settings, or SEMrush estimation lag
- GrowthX Search Console data shows ~1,500 keywords ranking in positions 2-10, and 296 in position 1
- SEMrush shows substantially lower numbers, raising concerns about reliability for competitive benchmarking
- Action: Jackson Wells and Vivek Shankar to apply US filter and compare both tools directly
- Goal: Ensure SEMrush data is directionally faithful for competitor comparisons with Arise, LangChain, and others

### Scrunch Implementation for LLM Tracking

- Recently onboarded Scrunch to track LLM mentions and performance across ChatGPT, Perplexity, and other models
- Dashboard shows prompts, variants, responses, presence (mentions), citations, and competitor appearance percentages
- Team working on refining prompts to align with business objectives: focus on product evaluation queries, not just TOFU/informational content
- V1 prompts currently in dashboard; Vivek and Mara to fine-tune for product-eval focus this week
- 3-4 weeks needed for 90-day data aggregation before meaningful insights and strategic pivots
- Jason requested sentiment tracking: want to gauge model favorability toward Galileo as an NPS-like score (e.g., "ChatGPT 70% positive vs. Perplexity 40%")
- Next steps: Mara to confirm Scrunch feature set on sentiment granularity and data tracking mechanics with the Scrunch team; 30-minute follow-up with Jason in 3 weeks to review Scrunch dashboard

### Content Strategy for AI-Driven Discovery

- Jason expressed concerns about declining effectiveness of traditional SEO and organic referral traffic in light of LLM-based discovery
- Strategy pivot: Focus on strengthening Galileo's authority on key topics through comparison content and off-site publishing (Quora, Reddit, G2 Crowd)
- Emphasis on creating semantically rich, product-eval-focused content to increase LLM citations and mentions
- Content formatting: each paragraph should start with a summary, followed by one complete idea, to improve LLM comprehension of Galileo's positioning
- Baseline metrics: Continue tracking referral traffic, but expect its importance to diminish relative to LLM mentions

---

## Action Items

- **Jackson Wells (Galileo):** Apply US filter to SEO reports; compare with SEMrush data to investigate keyword rankings discrepancy; report back on whether 5x difference persists
- **Vivek Shankar (GrowthX):** Fine-tune Scrunch prompts with Mara to ensure product evaluation focus, not just TOFU/informational content
- **Jackson Wells (Galileo):** Review list of Scrunch-tracked prompts and validate content pillars coverage
- **Mara Leighton (GrowthX):** Follow up with Scrunch team on NPS-like sentiment feature, data granularity questions, and how response counting works across LLM engines
- **Mara Leighton (GrowthX):** Book 30-minute Calendly with Jason Garoutte in 3 weeks for Scrunch data review and insights

---

## Transcript

**Jackson Wells:** She needed a break from the computer, which is cool.

**Jackson Wells:** Yeah, indeed.

**Vivek Shankar:** Are you like an avid camper?

**Jackson Wells:** I usually go every summer to Northwest.

**Jackson Wells:** I feel like it's a good thing to do.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** My only camping story, I'm afraid, is I pitched a tent once and it flew off the mountain.

**Vivek Shankar:** I don't think I would ever go again.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Hey, Mara.

**Vivek Shankar:** Hey, Jackson, how are you doing?

**Mara Leighton:** I know it's been a really busy couple of weeks for you.

**Mara Leighton:** Good.

**Jackson Wells:** Things are, launches are all said and done.

**Jackson Wells:** Or, well, they're not said and done.

**Jackson Wells:** They're in a good spot.

**Jackson Wells:** So everything is chugging along and about to refocus a bit for August once I get back from vacation.

**Jackson Wells:** So all positive.

**Mara Leighton:** I would love to hear that.

**Jackson Wells:** Where are you going on vacation?

**Jackson Wells:** I'm going camping in British Columbia, which will be fun.

**Jackson Wells:** Beautiful.

**Mara Leighton:** I was just in Kelly Ride with a friend for her birthday this last weekend, and it was a lot of outdoor time, and I forgot how good it is for you.

**Mara Leighton:** It's crazy how that works.

**Jackson Wells:** It's wild what that does for you after a while, especially when you spend all day in cities and on the screen.

**Jackson Wells:** So it's very refreshing.

**Jackson Wells:** For sure.

**Mara Leighton:** Well, I know we're waiting for Jason as well.

**Mara Leighton:** So I'll ask you one more question, which is, do you often camp?

**Mara Leighton:** Is that like new for you?

**Mara Leighton:** Are you pretty into it?

**Jackson Wells:** Usually once or twice a year.

**Jackson Wells:** It's just, the Northwest is very, very outdoor centric.

**Jackson Wells:** A lot of camping, a lot of hiking.

**Jackson Wells:** I am not an enthusiast, but I do do it for fun every once in a while.

**Mara Leighton:** Well, that's like my friend who was just visiting this last weekend.

**Mara Leighton:** She's lived in Colorado for, I think, 11 years.

**Mara Leighton:** And she said she just got to a point where she realized she doesn't like hiking and she doesn't like camping.

**Mara Leighton:** She was like, I've tried it for over a decade and I think I can finally admit it.

**Jackson Wells:** That's a form of self-actualization.

**Jackson Wells:** I feel like people in Colorado and in the Northwest experience, you're either like one of those people or you're not.

**Jackson Wells:** And I am somewhere in the middle.

**Jackson Wells:** It's not my passion, but it's still like, it's fun every once in a while.

**Jackson Wells:** But yeah, you know, I respect it.

**Mara Leighton:** Cause that means that you're not forcing yourself to do it as much as the people who like really genuinely enjoy it, you know?

**Mara Leighton:** And I think there's a phase where maybe everyone does force it a little bit.

**Mara Leighton:** So anyway, that's fun.

**Jackson Wells:** There's definitely those people who are like, you want to go on a hike every weekend?

**Jackson Wells:** And you're like, no, I actually, I do not.

**Mara Leighton:** You seem really happy, but no, I don't want to do that.

**Jackson Wells:** Yeah, exactly.

**Jackson Wells:** Yeah.

**Vivek Shankar:** Should we wait for Jason?

**Vivek Shankar:** I know he was running a little late.

**Mara Leighton:** Yeah, let's wait a couple more seconds.

**Jackson Wells:** Yeah.

**Jackson Wells:** I see him here.

**Jackson Wells:** So Jason's here.

**Vivek Shankar:** Alright, cool.

**Vivek Shankar:** So we're going to dive into kind of the updates around Galileo's ongoing content strategy.

**Vivek Shankar:** And in case Jason doesn't join this call, we have booked time with him later today.

**Vivek Shankar:** So we have a separate meeting with him, which is good.

**Vivek Shankar:** I can kind of walk through the metrics and the data that we've been tracking, and then from there, we can kind of adjust things as needed.

**Vivek Shankar:** Just to answer Jason's question.

**Vivek Shankar:** Thread real quick.

**Vivek Shankar:** It was a bit confusing.

**Vivek Shankar:** At first, he said June versus July.

**Vivek Shankar:** So I responded to that.

**Vivek Shankar:** But I think he was talking more about a quarterly sort of comparison.

**Vivek Shankar:** So traffic has grown quarterly, but obviously, you know, what we're thinking is like initially these months in June over here, these were the after effects of the migration when we were conducting the audits and some of the internal linking was not completely on point.

**Vivek Shankar:** And then there was some seasonal variation as well in June, which we saw, and now seem to have recovered that traffic and we're going on to a new high.

**Vivek Shankar:** So that's pretty good news.

**Vivek Shankar:** To answer your question, Jackson, about the search positions, these are global.

**Vivek Shankar:** We can filter by US and I can get you that data as well.

**Vivek Shankar:** Just a question of adding a filter to this report really at the end of the day.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** And then just in terms of the other talking points, so Google was still the top referral source for us, followed by ChatGPT.

**Vivek Shankar:** The number of engaged sessions are still, I would say, ridiculously high.

**Vivek Shankar:** I'm kind of surprised by this because 50% is a benchmark, but we're hitting like 80, 90% in some cases, and it's a good sign.

**Vivek Shankar:** And then in terms of non-brand impressions, we held pretty stable.

**Vivek Shankar:** And then LLM referrals for GrowthX URLs are 14%.

**Vivek Shankar:** And overall for Galileo's traffic at about 3.4, 3.5% this past week.

**Vivek Shankar:** But again, that number has been increasing at a faster rate compared to overall traffic increase.

**Vivek Shankar:** So pretty good signs over there.

**Vivek Shankar:** Just want to quickly cover the two URLs that Conor had pointed out.

**Vivek Shankar:** Just dropping an explanation here, but I think Jackson, we kind of covered that.

**Vivek Shankar:** And then regarding the LLM strategy, as we've mentioned in thread, you know, the competitor pages versus pages, and also the model comparison hubs should do well for driving referrals.

**Vivek Shankar:** And I think we can dive into Scrunch, Mara, unless there's something else you feel we need to cover?

**Mara Leighton:** That's great.

**Mara Leighton:** I just wanted to say hi to Jason, who just joined or recently joined, and then see if there's any questions that you might have, Jason, before we kind of jump into how we're using Scrunch.

**Mara Leighton:** I'll give you kind of the TLDR there, like, the data is not something that we would draw insights from just yet.

**Mara Leighton:** But anyway, I can pause and ask Jason, do you have anywhere you want to go first, or any questions you might have for us?

**Mara Leighton:** Thank you.

**Mara Leighton:** Good morning, everybody.

**Jackson Wells:** Good morning.

**Jason Garoutte:** I am in a room with tremendous echo.

**Jason Garoutte:** I hope it's okay.

**Jackson Wells:** Sounds crystal clear.

**Jason Garoutte:** Good, good.

**Vivek Shankar:** It sounds good.

**Jason Garoutte:** Based on what Vivek was saying, Jackson must have passed along one of my questions regarding the numbers of keywords for which we rank.

**Jason Garoutte:** And I think I saw, like, to me, there's still like maybe a disagreement or maybe we're just using different tools and they're radically different, but something smells off.

**Jason Garoutte:** So I want to make sure we run this one to ground eventually.

**Jason Garoutte:** And that is that I think I saw a report from GrowthX saying that we have over 1,000 keywords where we rank in the top 10.

**Jason Garoutte:** Did I imagine that or is that true?

**Vivek Shankar:** A lot of that, I don't know if it was 1,000, but basically, I think Ismail may have been referring to this report that I have on screen right now.

**Vivek Shankar:** And the number of keywords we're ranking for in positions from 2 to 10 is about 1,500.

**Vivek Shankar:** So that's where we're showing up.

**Vivek Shankar:** And in number one, it's 296.

**Vivek Shankar:** So that's what I think he was referring to.

**Jason Garoutte:** So I see that.

**Jason Garoutte:** And then I think Jackson has a different tool.

**Jason Garoutte:** Maybe it's SEMrush, where that number is a lot smaller.

**Jason Garoutte:** So it seems like maybe our hypothesis is that it could be a US versus globe, but I don't think it could explain that big of a difference.

**Jason Garoutte:** So like something seems odd.

**Jason Garoutte:** Jackson, have you figured out what might be going on?

**Jackson Wells:** I believe this is for global, so we're going to have to take a look at the US specific ones.

**Jackson Wells:** Yeah, but, you know, America's great again, right?

**Jason Garoutte:** And we dominate the world.

**Jason Garoutte:** So I don't think that we would have like 100 Google results where like third world countries had a thousand results.

**Jason Garoutte:** That would be surprising to me if just like the country filter made that big a difference in the numbers.

**Jason Garoutte:** So maybe SEMrush is a bad tool, or maybe like we have the wrong settings on it.

**Jason Garoutte:** This number seems awfully generous to me, but, you know, kudos to the team if it's true.

**Vivek Shankar:** The just a point about SEMrush and Ahrefs and the other tools, they generally do lag a bit.

**Vivek Shankar:** If you look at even your overall traffic in SEMrush, I bet there's a huge gap between that and the number of sessions that we're reporting.

**Vivek Shankar:** So that could be one explanation.

**Vivek Shankar:** The other explanation is the location filter, as Jackson mentioned.

**Vivek Shankar:** So when combined, they could explain the disparity in the number of rankings.

**Vivek Shankar:** Because we get this data from Search Console, which is Galileo-specific, SEMrush kind of does an estimate.

**Vivek Shankar:** It's not really getting your internal data.

**Vivek Shankar:** So it kind of looks like it looks at how much traffic you're getting.

**Vivek Shankar:** It keeps pinging Google and seeing like, okay, which keywords is Galileo showing up for?

**Vivek Shankar:** So it's always a bit of an estimate.

**Vivek Shankar:** So there's a lot of little errors in the process, and that kind of compounds sometimes.

**Vivek Shankar:** And that might be the case over there.

**Vivek Shankar:** But we'll certainly apply the country filter and take another look at it.

**Jason Garoutte:** Well, since I like to look like I'm doing a good job, I like to pick the number that's bigger, except not really, because the benefit of SEMrush is I can compare us to our competitors, which Jackson did for me yesterday, right?

**Jason Garoutte:** So I need an apples to apples system.

**Jason Garoutte:** And I don't think that Google Search Console is going to tell us what it is for Brain Trust and Arise and LangChain, right?

**Jason Garoutte:** Like, I don't have a way to do benchmarking against competitors.

**Vivek Shankar:** True, because we can't access their internal data.

**Vivek Shankar:** But even the comparisons on SEMrush, if you do it, I would say, at the very least, maybe back it up with another tool, another external tool, because sometimes with these platforms, the sampling might be off.

**Vivek Shankar:** So you, like, they might have better estimates, for example, for Arise, as opposed to Brain Trust.

**Vivek Shankar:** So even that might throw things off.

**Vivek Shankar:** So it's a bit muddled, unfortunately.

**Vivek Shankar:** And the best way to, in my experience, at least, and I'm sure Mara will back me up on this, is that you want to use like separate platforms just to make sure that you're getting a good idea of where things are at.

**Jason Garoutte:** If we take three unreliable platforms and average them, we'll get a reliable answer.

**Vivek Shankar:** Yeah, maybe.

**Jason Garoutte:** So we should definitely see if we can, I understand that those tools are just an estimate, but we're talking about factor of 10 difference right now.

**Jason Garoutte:** And I'm guessing that US won't explain it.

**Jason Garoutte:** So let's just rule that out.

**Jason Garoutte:** Like add US filter to these reports, your console analysis, see what it tells us.

**Jason Garoutte:** Jackson, you can do the same, go the other direction, you can try it worldwide.

**Jason Garoutte:** But I bet you that we'll still have at least like a factor of 5x difference.

**Jason Garoutte:** And something feels off about that.

**Jason Garoutte:** Are you able to double click on this and see what the thousand keywords are?

**Vivek Shankar:** Not on this particular chart.

**Vivek Shankar:** We do have this particular tab over here, the queries.

**Jason Garoutte:** The easiest way to see if this number is valid would be to get the list of 1,000 keywords, and then I go type five of them into Google randomly, and see if they're legit keywords for us that we actually rank for.

**Vivek Shankar:** Lots of brand terms at the top is what I can barely see.

**Vivek Shankar:** It's like 2.1.

**Vivek Shankar:** This is basically, it's kind of collecting every single keyword that you rank for.

**Vivek Shankar:** If you're curious about one particular keyword, you can type it in here, and then see the kind of position and distribution and how that goes.

**Vivek Shankar:** The average position over here, you should give us an idea of like that two to ten kind of category.

**Vivek Shankar:** So, that's kind of how this report works.

**Vivek Shankar:** So it needs a little customization just to get you the information you're looking for.

**Vivek Shankar:** And I can build that out and give it for you.

**Vivek Shankar:** Add a country filter and add a filter just to throw the positions from 2 to 10 or 1 to 15, whatever it is that you want to see.

**Vivek Shankar:** And we can get you that data.

**Vivek Shankar:** And then you can compare it to some SEMrush, kind of see where that's at.

**Vivek Shankar:** Yeah.

**Jackson Wells:** Vivek, do you want us to roll down even a little bit more?

**Mara Leighton:** Jason, I'm sure you've already seen this, but just to your point of the queries being a little small, I feel like this is maybe a little bit helpful, a visual tool slightly more visually accessible.

**Mara Leighton:** Okay.

**Jason Garoutte:** Well, the color is pretty, but I actually only read about four of those.

**Jason Garoutte:** Yeah, that's fair.

**Jason Garoutte:** I think take a list and Jackson can use it to compare to his list and maybe that helps us figure out what I really need to know is whether SEMrush is directionally faithful for comparisons across vendors so that I can see if we're like keeping pace with our competitors.

**Jason Garoutte:** And right now I'm a little nervous about that, especially because it shows Llama Views making tremendous gains.

**Jason Garoutte:** But anyways, let's just try the simple thing first, filter this to US, see what the number is.

**Jason Garoutte:** But anyways, let's just try the simple thing first, filter this to US, see what the number is.

**Jason Garoutte:** If it's still 5x difference, then we got to like go, we got to double click because something is off.

**Jason Garoutte:** So if it's 50% different, I'd be like, okay, that's like estimation error in SEMrush, but it's 5x different, I think.

**Jason Garoutte:** So let's check US to US.

**Jason Garoutte:** All right.

**Jason Garoutte:** That's helpful.

**Mara Leighton:** Jason, I'm glad you joined too, just so that like we can do a little bit of digging and come up with a more thoughtful, thorough answer for that particular question.

**Mara Leighton:** We can work with Jackson here as well.

**Mara Leighton:** And then we can share a little bit of like a summary report with you that you can review and we can find some time to chat.

**Mara Leighton:** You in depth if you'd prefer, but it's just helpful to get on the same page with the questions that you have.

**Mara Leighton:** So sounds good.

**Mara Leighton:** We will work on investigating that a little further.

**Jason Garoutte:** I hate to tell my boss and, you know, my peers that we rank for a thousand keywords.

**Jason Garoutte:** If it's not, you know, legit.

**Mara Leighton:** Totally.

**Mara Leighton:** Having the report is good evidence.

**Jason Garoutte:** Yep.

**Mara Leighton:** I understand too that if you're, you know, the secondary questions that you might have for us, that natural follow up is likely what you would be getting as well.

**Mara Leighton:** So it'll just be helpful if we provide you with that context as well of even if we're continuing to see that 5x difference, helping explain it a little bit.

**Mara Leighton:** So happy to do that.

**Jason Garoutte:** Super cool.

**Mara Leighton:** Thank you.

**Jason Garoutte:** Yeah.

**Mara Leighton:** Jason, do you have any other questions that you want us to answer off the bat?

**Mara Leighton:** Otherwise, I know I shared that Geo article just very recently that sort of goes over like philosophically how we're thinking about AI or Geo specifically.

**Jason Garoutte:** Is the article that you mentioned in GrowthX?

**Mara Leighton:** Yes, I can drop it just right here.

**Mara Leighton:** It's in our new publication, which is the output.

**Mara Leighton:** And it is "Search is Dead, a Primer on Geo," which is essentially more or less that we've been hearing from pretty much every client is, you know, we're thinking that search is dead.

**Mara Leighton:** How do we prepare for a new content marketing landscape?

**Mara Leighton:** Like, what should we be doing?

**Mara Leighton:** And this is sort of the underpinnings of how we're thinking about it.

**Mara Leighton:** And then we're starting to onboard tools like Scrunch, which we can spend a little bit of time on.

**Mara Leighton:** But the TLDR for Scrunch in particular is we share prompts with them.

**Mara Leighton:** And then basically every three days, they'll ping LLMs and see on average where we rank for those different quarters.

**Mara Leighton:** And we can give you a little bit of, A, we can get insights on what we should rank for, what we should show up for in mentions that we aren't currently, what competitors are showing up for.

**Mara Leighton:** But we just onboarded V1.

**Mara Leighton:** Vivek and I will do some tweaking of the prompts just to make sure that they also match our business objectives here, specifically that they're product evaluation related and not just specifically more like TOFU or informational.

**Mara Leighton:** So that's a little bit of the work that we'll be doing this week.

**Mara Leighton:** And then in three to four weeks is when we should start getting enough data where we should be able to make some insights and tweak and treat our content as a product.

**Mara Leighton:** I know I just monologued for a little bit there, so I will stop and let me know if you have any questions.

**Jason Garoutte:** So we don't have a baseline yet of how we're doing with LLMs, apart from like the traffic that's referring.

**Mara Leighton:** Yes, we do with what you'll see in the dashboard, but something a little bit more specialized like Scrunch, we are kind of in the early incubation period with.

**Mara Leighton:** So we're working with the team to fine-tune the prompts.

**Mara Leighton:** And then in three weeks is when we'll start, because it's a 90-day aggregate.

**Mara Leighton:** Their benchmark is kind of three to four weeks before you really make any decisions based on the data that you're seeing.

**Jason Garoutte:** Is there anything that shows me how we rank for like three queries that like, you know, maybe Jackson suggested or I could suggest, like I, I don't, are you saying like, somebody's got a list of queries and we have to wait 90 days to collect data or we don't even have the list of queries yet?

**Mara Leighton:** Yeah, we do.

**Mara Leighton:** I mean, you'll see the queries that Vivek showed us in the dashboards.

**Mara Leighton:** We do have some data there, but in terms of the specific prompts that we'll be tracking through Scrunch, we have a V1 that is pulled into the dashboard currently.

**Mara Leighton:** And then, you know, that's something that Vivek and I and the team are more than happy to offer.

**Mara Leighton:** just because it takes quite a bit of fine-tuning and testing, but if you have any input on queries that are particularly important for you to rank for, I would imagine we are already covering them as sort of like your core topics and then just how your users would use like natural language to search for those things, but by all means, share them with us and we will get them into Scrunch and make sure that we are ranking for them.

**Vivek Shankar:** What tools are developers using for evaluations?

**Jason Garoutte:** What's the best tool for AI evaluations?

**Mara Leighton:** Yeah, these are all like, we have essentially, our goal is just to create essentially every version of your most core questions for your end persona, your audience, and then crack how we show up in those, and then what competitors are showing up, and then the sentiment of our mentions.

**Mara Leighton:** So, I would imagine we are covering our bases, but if there's anything in particular, of course, feel free to share it.

**Jackson Wells:** You guys wouldn't mind sharing like a list of these queries, there are content pillars for each of them, just so I can take a triple check on them.

**Jackson Wells:** But given the content we have for blogs, I assume you guys are on the money there, I just want to validate very quick.

**Mara Leighton:** Yeah, this is purely like if we can take something off your plate and just show you the end result, ideal.

**Mara Leighton:** And then if you want to kind of be in the mix with the nitty gritty, then more than happy to have you there as well.

**Mara Leighton:** So I can share the list of prompts that we are going to be tracking through Scrunch and also give you a little bit of our input on why we chose those prompts in particular, if that's helpful, just as you go through them.

**Jackson Wells:** Totally.

**Mara Leighton:** Okay, great.

**Jason Garoutte:** Are you able to, first of all, do you have any data, sounds like you're not ready with Scrunch.

**Mara Leighton:** I can show you our dashboard.

**Mara Leighton:** I just want to caveat it as pretty much none of the numbers that we're seeing currently are things that I am, are good benchmarks for us.

**Mara Leighton:** Like it's very preliminary.

**Jason Garoutte:** But it would help us understand how things are going to be tracked.

**Jason Garoutte:** Like, I don't even know visually.

**Jason Garoutte:** I know visually what a SEMrush looks like.

**Jason Garoutte:** I don't know visually, you know, Profound and Scrunch and something.

**Jason Garoutte:** I don't know how these tools are, like, going to do this over time.

**Jason Garoutte:** It seems like memory is going to be, like, the thing that makes it super complicated.

**Jason Garoutte:** So, like, just getting a mental model as a foundation.

**Mara Leighton:** Totally.

**Mara Leighton:** Okay, so this is what the prompt section of Scrunch looks like currently.

**Mara Leighton:** So, again, if we go into, let's see, maybe, I don't know if there's one in particular you want to see.

**Mara Leighton:** But ideally, again, these aren't really reflective of anyone that we want to be tracking currently, which is why we need to work with the Scrunch team to V2 this.

**Mara Leighton:** But if we go into a prompt, you'll see all of the related prompts.

**Mara Leighton:** And then how many responses.

**Vivek Shankar:** Also, you'll see general, like, sentiment.

**Mara Leighton:** Yes.

**Vivek Shankar:** And then competitors will be right here and it'll be like 20% for this competitor.

**Mara Leighton:** And that'll just help us, that'll be basically input for us on where we need to work on creating content and where we need to strengthen like semantically the LLM's understanding of Galileo, what core topics you're an expert on, and where we could either on-site or off-site adjust, you know, whether it's like formatting of making sure that each individual paragraph starts with a summary, and then the rest of the paragraph is one complete idea.

**Jason Garoutte:** Let's postpone the like possible actions we could take.

**Jason Garoutte:** I just want to see if I can understand how we intend to baseline things.

**Jason Garoutte:** So I see, like, I want to understand these columns when it says five variants and 25 responses.

**Jason Garoutte:** That's going to be interesting.

**Mara Leighton:** Oh, this is actually already clicked in, right?

**Jason Garoutte:** And it started with a topic and it listed a large number of prompts, and then for each prompt, seems like there's a bunch of variants.

**Jason Garoutte:** What does it mean when it says 25 responses?

**Mara Leighton:** It's a great question.

**Mara Leighton:** I will have to look at the user guide, to be honest, to get into the nitty-gritty, and I can send you a Loom of, oh, yeah, Vivek, feel free to just jump in.

**Vivek Shankar:** Yeah, I think what that means is the five variants are basically, so the query that you saw on the previous page is like a seed, and this screen that Mara is showing right now is like the variations of those queries, so those are the variants.

**Vivek Shankar:** The responses are basically, I think, like the number of different responses that come up, so it doesn't always share the exact same response in the LLM, and I think the number of responses is just that, so we have tracked five different responses for this particular search.

**Jason Garoutte:** On this page, it would appear that five responses have come from five different engines.

**Jason Garoutte:** Right?

**Jason Garoutte:** So I'm wondering if it's always one response per engine, or is this thing going to like hit the same ChatGPT 10 times in a day and count that as 10 different responses?

**Jason Garoutte:** I guess you don't know yet.

**Mara Leighton:** The short answer is that we need more data.

**Mara Leighton:** Yes.

**Mara Leighton:** And also this will be something that is definitely like a collaboration between us and Scrunch.

**Mara Leighton:** So the great thing is, is that we can kind of pull in the people who are the architects of this tool to build new products for us or to build new features for us.

**Mara Leighton:** And then also get a little bit more granular.

**Mara Leighton:** Just because I would love if there was also just you could hover over it and get a little bit more of an explanation.

**Mara Leighton:** But yeah, so we need a little bit more data.

**Jason Garoutte:** Maybe I guess each one of these has five responses.

**Jason Garoutte:** I don't know.

**Jason Garoutte:** Maybe it does it every day.

**Jason Garoutte:** And, you know, after five days, says five.

**Jason Garoutte:** And after 10 days, it says 10.

**Jason Garoutte:** I don't really know.

**Jason Garoutte:** But you should find out.

**Jason Garoutte:** And then I'm going to guess that presence means what percent of responses did the word Galileo appear?

**Jason Garoutte:** And the citations, I'm going to guess, means of what percent of responses did Galileo get cited somewhere in the margins?

**Mara Leighton:** Yes, I believe that you are correct.

**Mara Leighton:** Presence, I think it's just here used as a synonym for mentions.

**Mara Leighton:** But I'll confirm with them that it isn't slightly more nuanced than that, but correct that citations would then be wherever it's linked out to.

**Mara Leighton:** Obviously, for our purposes, mentions are going to be much more important to us than citations.

**Mara Leighton:** Citations are great, but ideally, we'll be focusing on mentions because they just happen to be a little bit more valuable for Geo.

**Mara Leighton:** So can you go back to the main screen?

**Jason Garoutte:** It would strike me that while it's not a comprehensive baseline, we do have 109 responses and 950 responses.

**Jason Garoutte:** So, like, it's not clear to me what constitutes statistical significance.

**Jason Garoutte:** Obviously, the prompts are not well-defined.

**Jason Garoutte:** Yeah.

**Mara Leighton:** Let's see.

**Jason Garoutte:** What's a good classic one?

**Jason Garoutte:** What's like the continuous improvement of AI models seems really promising.

**Jason Garoutte:** Like number four there.

**Jason Garoutte:** So like, is there any, yeah, this is a lot of these are just unpopulated.

**Jason Garoutte:** Well, that's not necessarily true.

**Jason Garoutte:** We're just zero in a lot of them that are populated.

**Jason Garoutte:** So I, how are we going to summarize this with like a SEO?

**Jason Garoutte:** We can say like how many things we rank for in, you know, different spots and we can, I guess we can sort of sort those by the, uh, the amount of traffic and impressions that they have, but how are we going to summarize this besides asking an LLM to summarize it?

**Mara Leighton:** Meaning like how will we summarize essentially how we're doing each month?

**Mara Leighton:** Is that kind of your question?

**Mara Leighton:** Because obviously for, um, search, it's a little bit more linear.

**Mara Leighton:** Well, I think that can be something that we work on together just to determine like what's most useful.

**Mara Leighton:** But I think what will still be useful is what percentage of traffic is coming from LLMs and to see if we can kind of, if we can increase that over time.

**Mara Leighton:** And then in particular, if there are keywords that are just extremely important that Galileo is mentioned in, those are ones that I would assume we can also just star and keep track of most closely.

**Mara Leighton:** Because they also should be somewhat, they should be core, they should be related to the content pillars that we're really honing in on.

**Mara Leighton:** So if we're creating content to service one query that we're really, really fixated on, then it should also service the rest of the content pillar.

**Jason Garoutte:** I suspect that referral traffic, we'll keep measuring referral traffic, but I think it's going to become less and less important.

**Jason Garoutte:** That's my gut.

**Jason Garoutte:** I could be wrong.

**Jason Garoutte:** So we should report on it.

**Jason Garoutte:** Yeah.

**Jason Garoutte:** But I think it's less competent in content marketing.

**Jason Garoutte:** And so, like, what I've looked at.

**Jason Garoutte:** And I like feedback for Scrunch, I kind of want to know how positive is each model about Galileo.

**Jason Garoutte:** That's what I want to know, right?

**Jason Garoutte:** I want me to come up with a way of summarizing the number to say that ChatGPT is like 70% positive about Galileo across some list of 15 topics that we've predefined.

**Jason Garoutte:** And when I take this list and do it for Perplexity, it's like only 40%.

**Jason Garoutte:** Like, oh, Jason needs to work on his story for Perplexity.

**Mara Leighton:** Totally.

**Jason Garoutte:** I think that's a great point.

**Mara Leighton:** And I'll follow up with the Scrunch team to determine like how granular this is, but I know they are planning to track sentiment.

**Mara Leighton:** And I don't know if that's as granular as a, like on a query basis, I would imagine it is.

**Mara Leighton:** But to your point, you should, we will be able to see whether or not, without having to necessarily like click into the results, because we won't have that visibility into that.

**Mara Leighton:** And we're going to be able to see each individual query, what's the Galileo mention, how many times it was mentioned, like what the percentage of presence is, and then also citations, and then competitors, as well as sentiment.

**Mara Leighton:** So we should be able to see, was this a positive mention?

**Mara Leighton:** Was this a negative mention?

**Mara Leighton:** And then we can kind of tweak our storytelling from there.

**Mara Leighton:** So to answer your point, I believe they do have it in the pipeline, but I will confirm with them how granular they're getting with that.

**Jason Garoutte:** You guys all remember Net Promoter Score, NPS?

**Mara Leighton:** Mm-hmm.

**Jason Garoutte:** Oh, you should look this up later.

**Mara Leighton:** It's a classic.

**Jason Garoutte:** It's just a way of like gauging how vociferous your customers are in their support of your brand.

**Jason Garoutte:** And it kind of magnifies the polar extremes, the people that love you and the people that hate you.

**Jason Garoutte:** But there's like benchmarks for like how, what percentage of your customers you want to have be like your fans.

**Jason Garoutte:** And Apple's really good and Comcast is really bad, right?

**Jason Garoutte:** I kind of want Scrunch to tell us, like the net promoter score of Perplexity for Galileo.

**Jason Garoutte:** And, you know, there'll have to be like a whole range of topics that it averages across.

**Jason Garoutte:** But, you know, the higher up you go in an org chart, as you get closer and closer to your investors, the more you have to summarize.

**Jason Garoutte:** Right.

**Jason Garoutte:** And you will all know like a million little numbers.

**Jason Garoutte:** But like by the time it gets to the board, it's got to be like a really simple number.

**Jason Garoutte:** So there's probably going to be some equivalent of net promoter score.

**Mara Leighton:** Yeah, I love that idea.

**Jason Garoutte:** Yeah, let me ask them or let me share that idea with them.

**Mara Leighton:** I really like that idea.

**Mara Leighton:** I would also imagine that it could be good to see it in like a graph, you know, or some type of visual.

**Mara Leighton:** That would be useful.

**Mara Leighton:** Another thing that I wanted to mention to you is well, A, I would love to continue having this conversation because it's obviously very important.

**Mara Leighton:** And I want you to feel like you have visibility into it.

**Mara Leighton:** Since we're about three to four weeks out from having meaningful data, I would like to book a 30-minute Calendly call with you so that we can review the Scrunch dashboard and kind of dive into what the insights are.

**Mara Leighton:** And then from there, we can determine what the next steps are and how we should be treating our content as a product.

**Jason Garoutte:** Yeah, that sounds perfect.

**Mara Leighton:** Vivek and I will work with Jackson to fine-tune the Scrunch prompts so that they're aligned with business objectives, and then we'll have more to show you in three weeks.

**Jason Garoutte:** Sounds good.

