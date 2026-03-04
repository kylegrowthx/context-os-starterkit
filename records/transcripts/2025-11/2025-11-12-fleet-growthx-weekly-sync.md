# Fleet <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-12
time: 20:00 UTC
duration: 17 minutes
organizer: Erik O'Brien
participants: Aida Knezevic, Erik O'Brien, Irena Reedy
fathom_recording_id: 101211430
fathom_url: https://fathom.video/calls/471517136
share_url: https://fathom.video/share/beS8crdSPCSx33kbtDgwLKDGzt92tpzj
source: fathom
enriched_on: 2025-11-12 18:30 UTC
</metadata>

---

## Summary

GrowthX and Fleet synced on content production velocity and AI visibility performance. The team discussed Fleet's 1% citation rate in Scrunch (an AI visibility tool), which is below the GrowthX client average of 3-4%, and concluded that more educational content (how-to guides and comparisons) is needed. Key blockers discussed include pending Google Search Console access needed to complete a Looker dashboard, and the need to approve ~15 topics to meet the goal of 5 articles per week.

---

## Context

Fleet is a client of GrowthX working on B2B content marketing strategy and AI visibility. Aida Knezevic (GrowthX) leads the engagement with support from Erik O'Brien. Irena Reedy is Fleet's Content Specialist and primary point of contact for content feedback and approvals. This is a recurring weekly sync where the team reviews content production progress, tracks competitive visibility in AI tools, and aligns on upcoming priorities. The relationship is operational and collaborative, with GrowthX providing strategic guidance on content strategy and AI visibility measurement tools like Scrunch.

---

## Relevance

**To GrowthX Delivery:**
- Content production cadence goal is 5 articles/week; current output is 3/week. Bottleneck is topic approval — need ~15 approved topics to build production backlog.
- Scrunch (AI visibility tool) is now actively instrumented for Fleet. Citation rate (1%) is lower than GrowthX client average (3-4%), driven by smaller content library. Strategy to increase visibility is educational content expansion (how-to guides, comparisons).
- Data blocker: Google Search Console access still pending. Looker dashboard is incomplete without GSC; currently only GA4 data is available.

**To CheckThat:**
- Scrunch demonstrates reverse-engineering of LLM behavior across ChatGPT, Claude, and Perplexity. Fleet is tracking presence in LLM responses and using topic-level data to refine content strategy.
- LLM algorithms have shifted recently (as of last month) — stopped favoring Reddit/Wikipedia exclusively. Now pulling from more balanced sources. This affects citation visibility and content strategy prioritization.
- Scrunch can track thousands of prompts; currently ~150 base prompts plus custom prompts generated from Fleet artifacts. Client suggestions for new prompts welcome.

**To GrowthX Business Development:**
- Fleet is engaged and collaborative. No account health risks flagged. Jen (Fleet Head of Demand) is now receiving Scrunch reports and appears engaged in strategic discussions.
- Potential expansion: cross-org Scrunch access could be explored for Fleet's internal teams (currently internal to GrowthX only).

---

## Overview

- **Content Pipeline:** One article is ready for review. The next goal is 5 articles/week, requiring approval of \~15 topics to build a production backlog.
- **AI Visibility:** Fleet ranks \#2 behind Microsoft in Scrunch, an AI visibility tool. The low 1% citation rate (vs. 3-4% client average) is due to a smaller content library.
- **Data Blocker:** Google Search Console (GSC) access is still pending. This prevents a key Looker dashboard from functioning, as it requires data from both GSC and GA4.

---

## Key Topics

### Content Production & Review

  - **Current Production:** 3 articles this week.
  - **Review Pipeline:**
      - "What is Apple's device enrollment program?" → Ready for review.
      - Find all review drafts in the "Fleet Reviewing Drafts" Airtable view.
  - **Next Week's Goal:** 5 articles.
      - Requires approving \~15 topics from the content strategy Airtable.
      - **Rationale:** Build a production backlog to maintain momentum during team absences.

### AI Visibility Tracking (Scrunch)

  - **Tool:** Scrunch, an AI visibility tool that reverse-engineers LLM responses (ChatGPT, Claude, Perplexity) to track competitive presence.
  - **Fleet's Performance:**
      - **Rank:** \#2 overall, behind Microsoft.
      - **Position:** Middle of LLM-generated product lists.
      - **Citation Rate:** 1%.
          - **Significance:** This is lower than the 3-4% client average.
          - **Cause:** Fleet's smaller content library. More educational content (how-to guides, comparisons) is needed to increase citations.
  - **Data Complement:** Scrunch data is paired with a Looker dashboard that tracks actual LLM referral traffic.
      - **Blocker:** This dashboard is incomplete without GSC access.
  - **Access:** Scrunch is currently internal to GrowthX. A PDF report will be shared with Fleet's Head of Demand, Jen.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Post 'What is Apple's DEP?' review link in Slack for Irena
- Investigate cross-org Scrunch access; update Irena
- Send Scrunch PDF + prompt list to Irena

**Irena Reedy (Fleet)**
- Schedule sync w/ Brock re: blog reviews
- Review 2 articles in Fleet Reviewing Drafts

**Erik O'Brien (GrowthX)**
- Remind Sam re: add GrowthX team email to Google Search Console

---

## Transcript
**Aida Knezevic:** Hello, how's it going?

**Aida Knezevic:** I'm good, how are you?

**Irena Reedy | Content Specialist:** I'm well as well, thank you.

**Aida Knezevic:** Happy Wednesday.

**Aida Knezevic:** Happy Wednesday.

**Aida Knezevic:** Are you based in the US?

**Irena Reedy | Content Specialist:** I am.

**Irena Reedy | Content Specialist:** I'm in DC at the moment, but I moved back to LA in January.

**Aida Knezevic:** Oh, did you get yesterday off?

**Irena Reedy | Content Specialist:** Yeah.

**Irena Reedy | Content Specialist:** It was more like with Fleet, they say, like they've given us two options.

**Irena Reedy | Content Specialist:** You can either have like the traditional like holidays off or pick your own holidays.

**Irena Reedy | Content Specialist:** Like take your, like I'll work 4th of July, but then I'll just take the Friday off or something like that.

**Irena Reedy | Content Specialist:** So we just give them a heads up, which is great.

**Aida Knezevic:** Yeah, that's nice.

**Aida Knezevic:** Here we can, because we're like an international team, so everyone can choose to celebrate their own national holidays.

**Aida Knezevic:** But the first half of this year, I was like, no, I think I'm going to celebrate like US holidays just because it's easier for us.

**Aida Knezevic:** Work.

**Aida Knezevic:** And then halfway through, I was like, no, actually, I should just take my own national holidays.

**Aida Knezevic:** But the issue is that most of my country's national holidays are in the first half of the year.

**Aida Knezevic:** So I was just, now I feel like I should be celebrating Thanksgiving.

**Irena Reedy | Content Specialist:** You're like, I want to be included in that.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** So I kind of played myself a little bit, but it's no big deal.

**Irena Reedy | Content Specialist:** Yeah.

**Irena Reedy | Content Specialist:** So in LA, there's like a big Australian community.

**Irena Reedy | Content Specialist:** So they celebrate like Australia Day and they always do like a big, like there's a couple of Aussie bars and restaurants that will just like shut down and just open the place up to all the Aussies.

**Irena Reedy | Content Specialist:** And it's like one of my, it's one of my favorite days because everyone just kind of comes together and you find, oh, yep, we're all in the same boat.

**Irena Reedy | Content Specialist:** So I think that might be a day I might just be like, guys, I need to not work today.

**Aida Knezevic:** When is Australia Day?

**Irena Reedy | Content Specialist:** Um, it's January 26th.

**Irena Reedy | Content Specialist:** 26th or 27th.

**Irena Reedy | Content Specialist:** It's the day that Kobe died.

**Irena Reedy | Content Specialist:** That gives me a Because I'm like, I can't remember which date it is, but I'm like, every American knows the day Kobe died.

**Irena Reedy | Content Specialist:** So I'm like, it was that day.

**Aida Knezevic:** Wow.

**Aida Knezevic:** Yeah, yeah, that's the, yeah, I have a similar thing with Queen Elizabeth.

**Aida Knezevic:** I had a surgery on the day that she died.

**Aida Knezevic:** So it was like, I always remember that day.

**Aida Knezevic:** I always remember the date.

**Irena Reedy | Content Specialist:** Yeah.

**Aida Knezevic:** All right, cool.

**Aida Knezevic:** I think it's just going to be you, right?

**Aida Knezevic:** I think Brock's out.

**Aida Knezevic:** So I think we could get started.

**Aida Knezevic:** So I did add you to the agenda, so you should get it in your inbox.

**Aida Knezevic:** But to do a quick content update.

**Aida Knezevic:** So we're working on three articles this week.

**Irena Reedy | Content Specialist:** Next week, we want to do five.

**Aida Knezevic:** But for...

**Aida Knezevic:** This week's batch, this one is already ready for reviews, so what is Apple's device enrollment program?

**Aida Knezevic:** I'll send it in our Slack channel, but if you also go to our Airtable, if you go to the, sorry, Airtable is notoriously slow.

**Aida Knezevic:** If you go to Fleet Reviewing Drafts, you can find the Google Doc links to everything that's in review.

**Irena Reedy | Content Specialist:** Amazing.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Did you get a chance to take a look at the blogs that we sent over so far?

**Irena Reedy | Content Specialist:** I unfortunately have not.

**Aida Knezevic:** think Brock did.

**Irena Reedy | Content Specialist:** So I haven't touched base with him.

**Irena Reedy | Content Specialist:** I believe he's in Europe right now, I want to say.

**Irena Reedy | Content Specialist:** Okay, okay.

**Irena Reedy | Content Specialist:** So I'll schedule off as well.

**Aida Knezevic:** Okay, okay.

**Aida Knezevic:** That's totally fine.

**Irena Reedy | Content Specialist:** We'll just keep going, and then any feedback that you have, we can kind of implement it after the fact, so.

**Irena Reedy | Content Specialist:** Sounds good.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then we also.

**Aida Knezevic:** So we do need additional topics to be approved for next week.

**Aida Knezevic:** We did ping Brock about it yesterday or two days ago, but in case you also want to go through and leave feedback, you're more than welcome to.

**Aida Knezevic:** So if you, let me just group them by cluster so it's easier.

**Aida Knezevic:** Right, so they're all grouped into different clusters that you can find in our content strategy.

**Aida Knezevic:** We have around 60 right now.

**Aida Knezevic:** So you can leave comments by expanding the cell and then you can just drop a comment here.

**Aida Knezevic:** Let me know if you need the link to this base.

**Aida Knezevic:** It should be in Notion.

**Irena Reedy | Content Specialist:** Great.

**Irena Reedy | Content Specialist:** Okay, just, yeah, I'll just put in the chat just in case I, for some reason.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** And we are, I checked, so we still haven't gotten access to Google Search Console.

**Aida Knezevic:** I don't know who has ownership of that.

**Aida Knezevic:** Like, it's just a matter of, I think, adding our team email to the account.

**Erik O'Brien:** Yeah, I mentioned it to Sam last week.

**Erik O'Brien:** He said he was going to check with somebody, but I will send a quick reminder.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** That makes sense.

**Aida Knezevic:** I mean, we do, we have this, like, Looker dashboard built.

**Aida Knezevic:** It's a multi-page report that combines data from both platforms.

**Aida Knezevic:** So if we just do GA4, it's kind of like half of the graphs don't work.

**Aida Knezevic:** So it doesn't, like, it's not as helpful as it is when you have, like, both platforms in there.

**Aida Knezevic:** But we do have, and I don't know, Erik, I don't think we've gone through Scrunch yet.

**Erik O'Brien:** I remember talking about it, but I don't know if we went through it.

**Aida Knezevic:** Yeah, because I feel like every meeting we had, we talked about different things, and I never got around to presenting Scrunch.

**Aida Knezevic:** So I think we can, if you do remember this, let me know, Irina, because I don't want to, but this is the Scrunch dashboard.

**Aida Knezevic:** So this is an AI visibility tool.

**Aida Knezevic:** It's one of many on the market.

**Aida Knezevic:** It's similar to Profound, if you've heard of it.

**Aida Knezevic:** So what they do is we give them a description of your company, we give it a description of your audience, and then we also provide a list of competitors.

**Aida Knezevic:** And then based on those inputs, they generate base prompts that they use to send to different LLMs, like the ones that they have right here.

**Aida Knezevic:** So like ChatGPT, Claude, Perplexity, and then they collect the responses, they analyze.

**Aida Knezevic:** And then they present the data into Dashboard.

**Aida Knezevic:** So it's kind of like just trying to kind of reverse engineer what your audience is doing in LLMs because LLMs, they don't share their user data with anybody else.

**Aida Knezevic:** So this is kind of a way to get around it.

**Erik O'Brien:** I think you added more prompts here, right?

**Erik O'Brien:** I did last week.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** So yeah, usually like we have around 150, I think, base prompts, but then we also generate additional ones using your artifacts that we also add in here.

**Aida Knezevic:** But we can track like thousands of prompts and, you know, depending on, I mean, we can share the file with you that contains all of the prompts.

**Aida Knezevic:** And if you want to add any, you can let us know if there are any questions that repeatedly come up from your customers.

**Irena Reedy | Content Specialist:** We can also use those questions to generate prompts and then put them in the Dashboard.

**Irena Reedy | Content Specialist:** I think that's probably the closest.

**Aida Knezevic:** We can get to, yeah, like actual, like user behavior.

**Aida Knezevic:** So, but yeah, I think with, so just to give you kind of an overview of what everything is.

**Aida Knezevic:** So this monitors your overall competitive presence over time.

**Aida Knezevic:** So it has been, for the prompts that we're tracking, it has been growing over the past couple of weeks.

**Aida Knezevic:** So right now you're second behind Microsoft, your overall position in these responses is more towards the middle.

**Aida Knezevic:** So for example, if ChatGPT is listing off different products, like you would be in the middle.

**Aida Knezevic:** The sentiment is mostly positive, and you do get 1% of citations, which is not that bad, considering for most of our clients, we see a citation rate of around 3% to 4%.

**Aida Knezevic:** So the more, I mean, your competitors have a much, much higher citation rate, but it's because they have much bigger content libraries.

**Aida Knezevic:** So, for example, we have one client in cybersecurity who has a blog, they have like a resource library with just exclusively like SEO content, I mean, like a more like foundational educational content.

**Aida Knezevic:** And they have like a 15% citation rate just because there's just so much information that LLMs can use in their responses.

**Aida Knezevic:** So the more content you have, the more citations you get.

**Aida Knezevic:** I do have to point out that LLMs have been like updating their algorithms pretty often, and that impacts what kind of websites are cited.

**Aida Knezevic:** So this summer, they pushed, like ChatGPT pushed a really big update that started favoring Wikipedia and Reddit inside.

**Aida Knezevic:** But it looks like I think as of maybe last month, that that has changed.

**Aida Knezevic:** So now they're kind of pulling from different sources.

**Aida Knezevic:** They're not like favoring just Reddit.

**Aida Knezevic:** For a while, Reddit was like one of the top sources when it came to citations.

**Aida Knezevic:** And now it's a little bit more balanced.

**Aida Knezevic:** But yeah, think the more, generally speaking, the more educational content the website has, the more, like the greater the likelihood it's going to be cited.

**Aida Knezevic:** Especially competitive comparisons, like versus content, listicles, comparing different solutions, like best tool for X.

**Aida Knezevic:** And then also like how-to guides, that I also get surfaced a lot.

**Aida Knezevic:** If we go to prompts, I can kind of show you what are the topics.

**Aida Knezevic:** So Scrunch automatically categorizes all of our prompts into different topics.

**Aida Knezevic:** Just by category, so for example, for, let's see which ones do we want to pick, let's go with Device Management Best Practices.

**Aida Knezevic:** So these are all the seed prompts that we have in this topic.

**Aida Knezevic:** And then if we like click on this one, you can see the individual data for this prompt.

**Aida Knezevic:** So for example, in Perplexity, you appeared pretty much for every single prompt over the last week, I think, or like two weeks.

**Aida Knezevic:** Claude, generally speaking, doesn't cite that often, but Perplexity does provide citations more often than Claude.

**Aida Knezevic:** But this kind of gives us an insight into what are the topics where you tend to show

**Aida Knezevic:** Go up where are the topics that your competitors have a higher presence, and then it allows us also to kind of tailor the content strategy if there's a specific topic area where your visibility is going down or you don't have a good visibility, we can kind of try to do additional content research and like generate topics that support that type of visibility.

**Aida Knezevic:** If it's just a dot, then that means that we added the prompt recently, so it doesn't have enough data to go off of.

**Aida Knezevic:** So that's just wanted to flag that.

**Aida Knezevic:** It's not that it's bad, but it's just the prompt was added here recently.

**Aida Knezevic:** And then this is kind of, this data, we complement it with data in your Looker dashboard.

**Aida Knezevic:** So we have an LLM referral report built in Looker on the last page, and it breaks down all of.

**Aida Knezevic:** The different LLMs that are sending traffic to your site, and we can see, okay, like, usually it's ChatGPT and perplexity that are driving the most traffic to our client sites, and then we can also see what are the URLs that are getting the most traffic from different LLMs.

**Aida Knezevic:** So this kind of, these two reports complement each other, because this gives us an insight into your competitors, while, like, the Looker report actually lets us see the actual data, like, what's the, what are the pages they get the most visibility.

**Aida Knezevic:** And I do have to point out that for our customers, especially those that come to us with, like, a really big content library already, they're, the majority of the referral traffic is going to their blog.

**Aida Knezevic:** So it's, like, usually the homepage, maybe, like, a product page, and then it's just, like, the blog.

**Aida Knezevic:** And we can export this dashboard as like a PDF and send it to you, so you can kind of, yeah, use it for whatever you need.

**Aida Knezevic:** But yeah, you have any questions around just scrunch or AI visibility tracking, happy to answer.

**Irena Reedy | Content Specialist:** Is this something we, like, is this something you guys just have access to, or is there a way that we can, like, access this page as well with, the data?

**Aida Knezevic:** Or would you just have to send the PDF page?

**Aida Knezevic:** Yeah, right now we can just send you the PDF because it's limited to cross- emails, but I'll look into, let's see if we could do something about that.

**Irena Reedy | Content Specialist:** I just feel like our head of demand, Jen, would have, would love to get his eyes on this.

**Irena Reedy | Content Specialist:** thought he was going to be here today, but I think maybe we didn't send him, I didn't send him the link.

**Irena Reedy | Content Specialist:** Yeah, that tracks.

**Irena Reedy | Content Specialist:** Yeah.

**Irena Reedy | Content Specialist:** Okay, cool.

**Irena Reedy | Content Specialist:** Cool, cool.

**Aida Knezevic:** All right, great.

**Aida Knezevic:** Yeah, I think we can share, we can share the PDF report, we can share the prompts, and then I'm sure that, you know, he can have, he's going to have, like, ideas for what we can add in the prompts.

**Aida Knezevic:** Like said, we can track, like, So, the more, you know, some of the prompts, they can be quite specific, the ones that we were tracking, and they're kind of, you know, we just want to avoid leading the witness, you know, basically, like, trying to nudge the LLM to, so that's what we want to avoid, want to keep them, like, related, obviously, to our industry and the, the solution, but also general enough, so that it's similar to what a user would actually be looking for.

**Aida Knezevic:** Gotcha.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, I think those are all the updates that we had, right, Erik?

**Erik O'Brien:** I believe so, yeah.

**Aida Knezevic:** If any questions, I think we can wrap up early.

**Irena Reedy | Content Specialist:** No, I was just going to say, so from us, you needed Brock and I to go through and pick out five more topics for next week, correct?

**Aida Knezevic:** You could do more if you have time.

**Aida Knezevic:** I think 15 would be ideal, just so we have a backlog in case someone's out of office or sick, so just to have a head start. Then review the two articles that are in the reviewing queue.

**Irena Reedy | Content Specialist:** Perfect.

**Aida Knezevic:** Okay, we'll do.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Irena Reedy | Content Specialist:** Thank you so much. I appreciate both of you's time.

**Irena Reedy | Content Specialist:** See you next week. Bye, guys.
