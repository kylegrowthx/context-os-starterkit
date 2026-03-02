# Redis <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-19
time: 21:59 UTC
duration: 38 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien, Reet Mand, Fung-Lin Wu
fathom_recording_id: 123902064
fathom_url: https://fathom.video/calls/571614080
share_url: https://fathom.video/share/v3je9vmSPwoWdD9XTkiHDRoEMJDm4v2a
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Erik O'Brien presented Redis's content performance and AI visibility metrics ahead of Reet Mand's e-staff review, highlighting a 6-point increase in competitive presence (44% to 50% via Scrunch data) and the launch of GrowthX's internal CheckThat tool. The team cleared the content backlog with 49 articles published and only 4 remaining in review; identified and catalogued bot traffic from Singapore/China (1366x1366 screen resolution); and discussed a strategic shift to mid-article CTAs to improve hand-raiser conversion, with Fung-Lin committing to pitch the design to the brand team.

---

## Context

This is a standing weekly sync between Erik O'Brien (GrowthX) and the Redis content marketing team led by Reet Mand. Redis engaged GrowthX for B2B content marketing to drive AI visibility and organic hand-raiser conversions. The meeting serves as a regular checkpoint on content production, traffic quality, and strategy alignment ahead of Redis's quarterly e-staff review. Reet is preparing executive visibility into GrowthX's content impact and wanted concrete, impressive metrics to present to Redis leadership.

---

## Relevance

**To GrowthX Delivery:**
- CheckThat tool launch creates new service expansion opportunity; Redis is in 90-day trial but experiencing data bugs (jumbled data after category switches) — requires engineering attention before next reporting cycle.
- Content backlog cleared (49 published, 4 in review); team hitting sustainable cadence of 9-14 articles/week, enabling strategic testing (e.g., mid-article CTA placement).
- Bot traffic identification (Singapore/China, 1366x1366 screen res) demonstrates need for GA4 filtering guidance and documentation for other clients facing same issue.

**To CheckThat:**
- Redis using both Scrunch (legacy) and CheckThat (new) in parallel; CheckThat adoption hampered by bugs but positioning well for category-based prompt library model (shared prompts + historical data).
- Scrunch provides parity baseline for CheckThat validation; once bugs fixed, potential for CheckThat to become standard reporting tool for Redis and other clients.

**To GrowthX Business Development:**
- Redis account healthy: strong team engagement, content production on track, executive stakeholder (Reet) preparing to present metrics upward. Strong renewal signal.
- Hand-raiser conversion gap (zero so far) creating strategic pressure; mid-article CTA test is controlled experiment that could unlock new revenue signal and establish GrowthX as conversion strategist, not just content producer.

---

## Overview

- **AI Visibility Up:** Redis's AI competitive presence rose from 44% to 50% (Scrunch data), a key metric for the e-staff review.
- **Content Backlog Cleared:** 49 articles are now published; only 4 remain in PMM review, assigned to Jim.
- **New CTA Strategy:** To drive hand-raisers, the team will test placing CTAs mid-article, moving beyond the current bottom-of-page placement.
- **Bot Traffic Identified:** A surge in direct traffic was confirmed as bot activity (from Singapore/China, 1366x1366 screen res) and will be filtered from reports.

---

## Key Topics

### AI Visibility & Reporting

  - **Goal:** Generate impressive insights for the upcoming e-staff review.
  - **Key Metric:** AI competitive presence increased from 44% to 50% (Scrunch data).
  - **New Tool:** GrowthX launched "Check That," an internal tool replacing Scrunch.
      - **Vision:** A shared prompt library with historical data for easy setup.
      - **Status:** In a 90-day trial with known bugs (e.g., jumbled data after category switches).
      - **Action:** Erik will use Scrunch data for the e-staff report while Check That is debugged.

### Content Performance & Strategy

  - **Publishing Cadence:** 49 articles published; 4 remain in PMM review (assigned to Jim).
  - **Organic Traffic:** Shows a healthy, compounding week-over-week growth trend.
  - **Bot Traffic:** A recent surge in direct traffic was identified as bot activity.
      - **Source:** Singapore & China.
      - **Signature:** Screen resolution 1366x1366, 1-2 second engagement time.
      - **Action:** GrowthX will use this info to filter data; Fung-Lin shared a Google support post on the issue.
  - **LLM Referrals:** ChatGPT drives \~90% of all LLM traffic.
  - **Conversions:** GrowthX articles have not yet generated hand-raisers.
      - **Analysis:** Hand-raisers originate from product/docs pages, not blog posts.
      - **Solution:** Test placing CTAs mid-article to capture intent earlier.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Compile AI visibility summary (Scrunch+Check That; competitive presence, new refs) for Reet/Fung-Lin
- Review GA4 bot support post from Fung-Lin; share w/ GrowthX team

**Fung-Lin Wu (Redis)**
- Discuss mid-article CTA section-break w/ brand team; report back to Erik
- Ping Jim re: 3 articles in PMM review

---

## Transcript
**Erik O'Brien:** How's the week going?

**Reet Mand:** It's going okay.

**Reet Mand:** I'm mostly going to be off camera.

**Reet Mand:** I've been sick.

**Reet Mand:** I decided I am a superhuman and did not take, think, uh, did not...

**Reet Mand:** I'll listen to my body and my body today is like, I'm going to force you.

**Reet Mand:** So I'm in bed, but I want to hear what's going on in this side of the world.

**Reet Mand:** Hey, you know, I think Megan got an email from someone from your company and then she's like, are we doing this?

**Reet Mand:** I was like, I think we are.

**Reet Mand:** But I was going to ask you about it.

**Reet Mand:** Let me see what it was about.

**Reet Mand:** It was about the email that I, it was like, I think your growth newsletter.

**Reet Mand:** Check that is live and 10 free strategy sessions.

**Reet Mand:** And it was talking about how you guys launched something where you can see the tracking capabilities.

**Erik O'Brien:** Our tracking, basically, instead of just the prompts that we pick, it's able to track prompts across different categories.

**Erik O'Brien:** And so I can just pull it up here and show you guys.

**Erik O'Brien:** It's probably a lot easier than trying to imagine what I'm talking about.

**Erik O'Brien:** So there's different categories that we can put you guys in right now.

**Erik O'Brien:** You guys are primary category of database management systems.

**Erik O'Brien:** But from a category level, we kind of track different prompts for each category, really focusing on kind of the evaluation and decision-making criteria of like, what questions might those buyers be asking?

**Erik O'Brien:** Let's see.

**Reet Mand:** I'm preparing for my e-staff review for the quarter and anything you can share from here that you think would, lack of a better way of saying it, blow the execs away.

**Reet Mand:** Or, you know, give them a little bit of like insights that they hadn't, they haven't seen before and gives them a little bit of comfort that we, that we got this.

**Reet Mand:** Anything you can share that, like, I think that would be really helpful.

**Erik O'Brien:** Yep, absolutely.

**Erik O'Brien:** Yeah, I can pull together some insights, even from our historical tool we've been using is called Scrunch.

**Erik O'Brien:** So this is what we used for the last few months prior to launching Check That.

**Erik O'Brien:** And really what we were seeing here is competitive presence for Redis when we first started was about 44%.

**Erik O'Brien:** And now we're about 50%.

**Fung-Lin Wu:** This actually might be pretty.

**Reet Mand:** pretty good.

**Reet Mand:** That's a really good part.

**Fung-Lin Wu:** But yeah, especially because on the right side, you also have like the Mongo, Milvus, Reet Mand, yeah.

**Reet Mand:** I love it.

**Erik O'Brien:** Yeah.

**Reet Mand:** It's good.

**Erik O'Brien:** So this is where we've been tracking things historically.

**Erik O'Brien:** With the new tool, of course, with the new product launch, there's going to be bugs, unfortunately.

**Erik O'Brien:** And so as I've had this, like your analytics are being updated for the last couple days as I'm trying to check this.

**Erik O'Brien:** And I've also seen like once we switched categories, we got a bunch of jumbled data.

**Erik O'Brien:** So I'm having the engineering team hop in here and take a look.

**Erik O'Brien:** So, but I can pull together insights from Scrunch and see kind of a, like this competitive presence, which is, you know, how often do you show up in the prompts that we're tracking on a daily basis?

**Reet Mand:** Yeah.

**Erik O'Brien:** And then also, sorry, go ahead.

**Fung-Lin Wu:** Sorry, no, go ahead.

**Erik O'Brien:** And then I can also see like if any of our articles that we've published, like the net new ones.

**Reet Mand:** new

**Erik O'Brien:** Starting to be referenced, like in these, like, what is semantic caching is one that's, I think we refreshed recently.

**Erik O'Brien:** And so it's starting to show up with other competitors, but I'll pull together like a better insights of everything we have here.

**Reet Mand:** That would be super amazing.

**Reet Mand:** Like, I think Fung-Lin like this, we don't need to do more than just say this.

**Reet Mand:** Yeah.

**Fung-Lin Wu:** Oh, are you guys searching from Scrunch to check that then?

**Fung-Lin Wu:** Like, to check that?

**Erik O'Brien:** Yep.

**Erik O'Brien:** Yep.

**Erik O'Brien:** So check that is our internal.

**Erik O'Brien:** We built this one.

**Erik O'Brien:** And so.

**Fung-Lin Wu:** Oh, you guys both checked that.

**Erik O'Brien:** Yep.

**Erik O'Brien:** And so what we're, you know, the larger vision is that instead of having you, like, set up a new instance from scratch and have to come up with all these new prompts, you can literally just come in here and, like, add prompts from the shared library. Whatever kind of category you want, and so you can just pick these, and once you upload them to your account, then you get all the historical data that comes with it to see kind of, have we been mentioned in these categories historically?

**Erik O'Brien:** Do we want to add new prompts to track specific, like, product releases and new mentions, or if we're going into a new category, we can just go and kind of pick up these new prompts and add them to your account.

**Erik O'Brien:** So instead of starting from scratch, you get to have all this historical data that's populated into your overview section.

**Erik O'Brien:** But as I said, brand new launch as of two weeks ago, so we're still working out some kinks with it.

**Erik O'Brien:** So in the meantime, I have scrunched this as kind of a default to go back and make sure we can track the prompts that were, I think we, when Cody was still here, he gave me access to.

**Erik O'Brien:** Profound, and I went in there and copied all the prompts and then uploaded them up here.

**Erik O'Brien:** So we should have a one-to-one parity of what you guys are tracking in Profound.

**Fung-Lin Wu:** Yep.

**Fung-Lin Wu:** Yeah, because I believe that's what the scrunch was off, data was off of, was off of our Profound data.

**Erik O'Brien:** Like, yeah.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** So, yeah, more to come on, check that.

**Erik O'Brien:** It's, right now, we're giving everyone, like, a 90-day trial to have to, A, fix the kinks and try to get everybody onboarded.

**Erik O'Brien:** Once we get past 90 days, I'm still trying to figure out, like, what the go-forward plan is.

**Erik O'Brien:** Since we've been providing scrunch as part of the program, my questions around that are just, are we going to continue to offer this as part of, like, our ongoing reporting conversations.

**Erik O'Brien:** So, more to come on, check that overall.

**Erik O'Brien:** But for the time being, it's at least registering all the prompts that we have tracked in Scrunch and being able to track new ones from different categories.

**Erik O'Brien:** Let's see.

**Erik O'Brien:** All right.

**Erik O'Brien:** So quick updates on the content side.

**Erik O'Brien:** We're at 49 total published, so we've crushed out the backlog.

**Erik O'Brien:** There's only four left in PMM review.

**Erik O'Brien:** I think they're mainly the competitive pieces.

**Erik O'Brien:** I'm just looking at our content OS to double check.

**Erik O'Brien:** But, yeah, two of them are competitive, and then two are hybrid search and vector database versus traditional database.

**Erik O'Brien:** But other than that, we had nine articles published last week, five more this week. So we're getting on a really good cadence. There are three.

**Erik O'Brien:** One, I haven't moved yet, because we're just waiting on the image, the diagram for.

**Erik O'Brien:** So that one's actually already reviewed.

**Fung-Lin Wu:** just need to add the image.

**Fung-Lin Wu:** Okay.

**Erik O'Brien:** My internet's not letting me log into assignments, but yeah, I would take a look at those.

**Erik O'Brien:** I would take a look at the three Fathom PM and review.

**Erik O'Brien:** Okay.

**Erik O'Brien:** I'll just pull up my other screen again.

**Erik O'Brien:** Yeah, looks like they were assigned to Jim.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Okay.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** What was the other?

**Fung-Lin Wu:** What was the third one?

**Erik O'Brien:** Vector database versus traditional database.

**Fung-Lin Wu:** Can I see?

**Fung-Lin Wu:** Is that Jim also?

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** All three.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Perfect.

**Fung-Lin Wu:** Perfect.

**Erik O'Brien:** And so we're investigating this, like I said, kind of across all accounts, but it is something for us to keep tracking.

**Fung-Lin Wu:** We actually have a paid advertising agency, and we've actually been working with them because I think Google might have just announced that there's just like a lot of bots coming in from Singapore. I could try to find it and send it over, but we also did notice that our direct traffic went haywire the last December and January, where we saw this crazy doubled amount of sessions. They said our agency was able to filter it out on our reporting side, but within GA4, I'm guessing maybe that's the same situation.

**Erik O'Brien:** Yes, Singapore is number two.

**Fung-Lin Wu:** Yeah, and I think it's like the primary bot.

**Fung-Lin Wu:** I can try to find the, I'll need to find the, sorry, there's like a group of us that's been talking about these bot issues.

**Fung-Lin Wu:** But it's for us, it's actually the screen resolution was 1366 by 1366.

**Erik O'Brien:** Yeah, that one's also up there.

**Erik O'Brien:** Yeah, it's all a lot of traffic.

**Fung-Lin Wu:** Yeah, these are bots.

**Fung-Lin Wu:** The 1366 by 1366 with bots coming from like China and Singapore.

**Erik O'Brien:** The 800 by 600 or 800 by 800 is the one we're seeing kind of consistently.

**Erik O'Brien:** And if you look in like a little bit deeper, engagement time is like one to two seconds.

**Erik O'Brien:** So it is definitely a bot kind of coming, screen grabbing and then moving on.

**Fung-Lin Wu:** Yeah, I just shared a Google support post talking about these bots.

**Erik O'Brien:** Awesome.

**Fung-Lin Wu:** It used to be from Singapore, and I think now it's coming from China.

**Fung-Lin Wu:** Yeah.

**Erik O'Brien:** Cool.

**Erik O'Brien:** I will take a look at this and also share with our team as they're looking into everything.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Um, but regardless, um, overall, we're still seeing, even if we take direct traffic out.

**Fung-Lin Wu:** Yeah.

**Erik O'Brien:** And email and all the other stuff, we're still seeing a really good trend line of organic, um, traffic continue to go up.

**Erik O'Brien:** Obviously, this is this week, which isn't done yet, but, um, still seeing the trend line of week over week compounding growth.

**Fung-Lin Wu:** How should I think about it in terms of, obviously we care about the growth, we care about traffic growth from LLM, and then we care about conversion as a primary.

**Fung-Lin Wu:** Yeah, like this is the one I was looking at.

**Fung-Lin Wu:** Where it doesn't, I guess this is part where it's not just a steady incline.

**Erik O'Brien:** Yeah, this one, we do see a little bit of sporadic kind of up and down overall, as long as we continue to see kind of the trend line go up, then we're feeling pretty healthy.

**Fung-Lin Wu:** Okay.

**Erik O'Brien:** And really it's ChatGPT, Gemini, Perplexity. Claude is a really hard one to get a referral from just because unless you have web browsing on, they don't provide any citations. So more of a kind of platform nuance for them, but ChatGPT is about 90% of all LLM referral traffic.

**Erik O'Brien:** So it's good we're seeing a good split between Perplexity and Google too.

**Erik O'Brien:** And then conversions. What is semantic caching is a refresh that we did and multi-agents versus single agents. So good to see continuing traffic. I think we've got like one extra conversion compared to the last time I showed you guys the data. Overall, still tracking for kind of goals for February is to at least double. I think we had two in January, so we're trying to get four to five conversions.

**Erik O'Brien:** And then lastly, I did take a look at just like the last year of hand raiser events.

**Erik O'Brien:** And a lot of what I noticed was they're coming from product pages.

**Fung-Lin Wu:** I think when I do hand raisers, when I do hand raisers, and I do only growthx articles, I don't think there's any coming through.

**Erik O'Brien:** No, none yet.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** So that's why the piece is a little more scary for us, since we've been seeing a pretty sharp, like, organic to find in MQLs and hand raisers from organic, and this is where we were hoping for growthx to kind of bring up.

**Erik O'Brien:** Yeah, and that's, so I was looking at kind of all the different landing pages that have hand raiser events, and a lot of it is, like I said, from product pages.

**Erik O'Brien:** It can load.

**Erik O'Brien:** I'm also, as a side note, trying to get our team to change to something else besides Looker.

**Erik O'Brien:** Is this loading times where we spend most of our time doing reports and it's way too slow for us?

**Fung-Lin Wu:** I should, like, look at it.

**Fung-Lin Wu:** It will only be a three, but, like, I can kind of self-serve, but, yeah, yeah, I know what you mean.

**Erik O'Brien:** Yeah, so these are a lot of the landing pages, like Docs, Solutions. There's probably a couple blog posts overall that are leading to hand raisers, like what is Valky. Something for us to kind of start thinking about more strategically is, you know, if we want to focus on hand raisers, then it might make sense for us to think through how we enter some CTAs or callouts in the body itself versus a lot of what we're doing right now is having the CTA or talk to Redis at the very bottom of the article.

**Erik O'Brien:** So more so, a question back to you guys is if we want to explore putting some CTAs and callouts earlier on in the article, maybe around some more of the technical pieces that we typically link to.

**Fung-Lin Wu:** Like a book a meeting?

**Erik O'Brien:** Yeah, and we can experiment with different CTAs, like book a meeting or talk to an expert or kind of different ways to capture intent.

**Fung-Lin Wu:** Like putting it as a section break within the article?

**Fung-Lin Wu:** Okay, yeah, yeah.

**Fung-Lin Wu:** We've, we've talked about that a while ago, because that was actually also an, yeah, it was also kind of like an advice we've been given.

**Fung-Lin Wu:** I think we're struggling with the design.

**Fung-Lin Wu:** Yeah, we only have it in the very bottom and obviously the top nav and that's it.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So, yeah, something like with one of my clients, we do it like right after the intro, just so it's like priming them as they're reading to think about it.

**Erik O'Brien:** Other places are kind of midsection if we just want like a visual break to add CTA, like call out box, especially after we get like into the real time infrastructure requirements and challenges.

**Erik O'Brien:** Like right after this, we could put another one.

**Erik O'Brien:** So.

**Erik O'Brien:** Once you get into month three and four, conversions start to become a focus.

**Erik O'Brien:** Months one and two and even into three are really like, are we getting impressions and clicks and engagement time?

**Erik O'Brien:** But those are typically with smaller, less mature clients.

**Erik O'Brien:** You guys are a little bit further along.

**Erik O'Brien:** So I think we can definitely experiment quicker as long as we're aligned on kind of what we want to experiment with and be able to track those experiments over time.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** I can bring it up to our brand team about their thoughts on like adding like a section break.

**Fung-Lin Wu:** So I can bring that up to our brand team.

**Fung-Lin Wu:** I'm actually meeting with them tomorrow.

**Fung-Lin Wu:** I can ask them.

**Fung-Lin Wu:** I can ask them either if they can design it with Insanity and then use this and just use that template or if that's something that we would do.

**Fung-Lin Wu:** Or if that's something that they would want to do.

**Erik O'Brien:** Yeah, that works.

**Erik O'Brien:** And then we're happy to do it either way.

**Erik O'Brien:** Like, if you guys want us to take a crack at it, like, I'll just show you a quick example.

**Erik O'Brien:** Like, error by one of my other clients.

**Erik O'Brien:** Like, just, literally, this is all just code for their new agent engine.

**Erik O'Brien:** But, so these are things we can build really simple without any, like, new components that need to be built.

**Erik O'Brien:** But we'll kind of take the guidance from your brand team as how they want to go.

**Fung-Lin Wu:** How come for that error by article, it's not on their blog.

**Fung-Lin Wu:** It's like a separate landing page.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So, they, we publish about 12 to 15 articles a week for them.

**Erik O'Brien:** And so, a lot of it is meant for just organic.

**Fung-Lin Wu:** Debating who to use as authorship for our articles, I was looking at, like, some of the clients that are using GrowthX and just who they use authors, and I came across Airbrite, and I was like, wait, it's just, it's just like, I was there's no way to see who's writing every week.

**Erik O'Brien:** No.

**Fung-Lin Wu:** Yeah.

**Fung-Lin Wu:** No.

**Fung-Lin Wu:** As you watch your product.

**Fung-Lin Wu:** Yeah, yeah.

**Fung-Lin Wu:** That's how I was curious.

**Fung-Lin Wu:** Like, you guys are just doing it.

**Fung-Lin Wu:** But I guess you interview him, and then you grab those.

**Erik O'Brien:** Yeah, we use basically those interview transcripts as, like, proof points to, like, base it on factual evidence of what we can say and not say.

**Erik O'Brien:** So it's definitely a whole custom pipeline we built just for him.

**Fung-Lin Wu:** Got it.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Okay.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** I know we got one minute left.

**Erik O'Brien:** Anything else top of mind or things I can work on?

**Erik O'Brien:** I'll definitely pull together that AI kind of visibility summary for you.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Thank you.

**Fung-Lin Wu:** Thank you.

**Fung-Lin Wu:** And I would get those three pieces.

**Fung-Lin Wu:** I'll ping Jim.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Because once those are done, then we don't have a backlog.

**Erik O'Brien:** It should be awesome.

**Fung-Lin Wu:** I know.

**Fung-Lin Wu:** That'd be great.

**Fung-Lin Wu:** Thank you.

**Erik O'Brien:** Cool.

**Erik O'Brien:** Thanks, Funland.

**Erik O'Brien:** Thanks, Reet.

**Erik O'Brien:** Hope you feel better.

**Fung-Lin Wu:** Bye.

**Erik O'Brien:** Bye.
