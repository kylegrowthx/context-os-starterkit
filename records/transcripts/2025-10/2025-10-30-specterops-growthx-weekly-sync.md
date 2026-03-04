# SpecterOps <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-30
time: 17:30 UTC
duration: 29 minutes
organizer: Aida Knežević (GrowthX)
participants: Aida Knežević, Erik O'Brien, Kirsten Gibson, Meshach Cisero, Ric Nguyen, Jason Wolfe
fathom_recording_id: 98099255
fathom_url: https://fathom.video/calls/456946973
share_url: https://fathom.video/share/4nLAscxBGf3zzAkR98fJHD-VVzy-VQSW
source: fathom
enriched_on: 2026-03-02 08:15 UTC
</metadata>

---

## Summary

GrowthX and SpecterOps aligned on security content strategy, reviewing an initial "Zero Trust vs. Least Privilege" draft and establishing a 3-to-5 blog publishing cadence starting next week. Aida presented the live Looker dashboard consolidating GA4 and GSC data, flagged a GSC connectivity issue, and highlighted that SpecterOps is seeing 10% LLM citation rates (versus 2-3% industry average) in Scrunch. The team agreed to schedule a product deep-dive with Jonathan Parfait, share Scrunch base prompts, and have Ric provide brand standards to guide GPT-generated image creation for blog posts.

---

## Context

SpecterOps is a cybersecurity company operating in the zero-trust security space. GrowthX is delivering a content marketing engagement, focused on both organic search visibility and AI visibility (CheckThat/AEO strategy). This is a weekly sync to review progress on content calibration, review publishing pipelines, and address data/analytics questions. The engagement is ramping up: content started with a single calibration blog to test tone, with plans to scale to 3 blogs the following week and 5 blogs the week after. Key deliverables include GA4/GSC consolidation in Looker, LLM visibility tracking via Scrunch, and GPT-generated blog imagery aligned to SpecterOps brand standards.

---

## Relevance

**To GrowthX Delivery:**
- Content calibration requires tone shift to acknowledge security as a continuous journey, not binary achievement — core to SpecterOps positioning
- Publishing cadence confirmed: 3 blogs next week, scaling to 5 thereafter. Feedback loop via Notion comments with `@Aida` tagging
- GPT image generation workflow requires detailed brand standards (colors, fonts, assets) to ensure compliance — Ric to provide
- Engaged session rate (~50%) on par with industry average; GA4 conversion event hierarchy needs clarification from SpecterOps

**To CheckThat:**
- SpecterOps showing 10% LLM citation rate vs. 2-3% industry benchmark in Scrunch tracking (though limited prompt set may be leading)
- Looker dashboard live with LLM referral traffic breakdown; ChatGPT/TradGPT primary driver, growing trend week-over-week
- GSC connectivity issue in Looker blocking non-branded keyword reports; requires investigation and fix
- Opportunity to expand Scrunch prompt library beyond generated base set — SpecterOps can provide additional prompts for deeper visibility tracking

**To GrowthX Business Development:**
- Account is actively publishing and scaling (3→5 blog cadence signals confidence in content quality)
- Strong LLM citation performance and engagement with data/tooling suggests healthy account health
- Product deep-dive scheduled with SE (Jonathan Parfait), indicating client readiness to deepen product knowledge and content context
- Brand standards guidance from Ric suggests organized, mature client operations

---

## Overview

- **Content Calibration:** The initial draft needs a key tone adjustment to acknowledge that security is a continuous journey, not a binary "achieved" state.
- **Data & Tools:** The Looker dashboard is live, consolidating GA4 & GSC data. Scrunch shows a high 10% citation rate (vs. a 2–3% average), but this is based on a small, potentially biased prompt set.
- **Next Steps:** SpecterOps will provide feedback on the content calendar and draft, explain GA4 conversions, schedule a product deep-dive, and share a detailed brand guide.

---

## Key Topics

### Content Calibration

  - **Initial Draft:** A broad topic ("Zero Trust vs. Least Privilege") was chosen to test tone and style.
  - **Required Tone Adjustment:** The draft must convey empathy by acknowledging that security is a continuous journey, not a binary "achieved" state.
  - **Feedback Process:** Use Notion comments (`@Aida`) for specific feedback on the draft and content calendar.
  - **Content Cadence:**
      - **Week 1:** 3 blogs
      - **Week 2:** 5 blogs

### Data & Performance Tracking

  - **Looker Dashboard:** Consolidates GA4 and GSC data into a 7-page report.
      - **Engaged Sessions:** Averages \~50%, which is typical.
      - **Non-Branded Traffic:** Report is broken; Aida will investigate.
      - **GA4 Conversions:** Meshach will provide context on events and their relative importance.
      - **LLM Referrals:** Traffic is growing, with ChatGPT as the primary source.
  - **Scrunch Platform:** Tracks LLM visibility against competitors.
      - **Citation Rate:** 10% (vs. a 2–3% average).
      - **Context:** This rate is based on a small, Scrunch-generated prompt set and will change as more prompts are added.
      - **Action:** SpecterOps can provide more prompts to track.

### Product & Brand Alignment

  - **Product Deep-Dive:** A product deep-dive is needed for content context.
      - **Presenter:** Jonathan Parfait (SpecterOps SE) is the best choice, as their customer-facing experience provides the most relevant context for content creation.
      - **Attendees:** Jonathan Parfait (SpecterOps) and Erik O'Brien (GrowthX).
  - **Image Generation:** GrowthX will create GPT-generated images for blogs.
      - **Process:** Requires a brand guide (colors, fonts, assets) to ensure brand alignment.
      - **Action:** Ric will share a detailed brand standard guide.

---

## Action Items

**Kirsten Gibson (SpecterOps)**
- Comment on content calendar w/ feedback/thumbs; tag Aida
- Review calibration blog; add comments w/ tone/POV

**Aida Knežević (GrowthX)**
- Grant Looker edit access to SpecterOps team
- Fix Looker GSC connectivity; restore non-branded/queries/landing-page

**Meshach Cisero (SpecterOps)**
- Send GA4 conversion event explanations to Aida
- Schedule product walkthrough w/ Jonathan Parfait + Erik O'Brien for next week

**Erik O'Brien (GrowthX)**
- Share Scrunch base prompts w/ SpecterOps team

**Ric Nguyen (SpecterOps)**
- Email brand standards guide to Aida Knežević + Erik O'Brien

---

## Transcript
**Aida Knežević:** Hi, it's Aida.

**Kirsten Gibson:** Aida.

**Kirsten Gibson:** Nice to meet you.

**Aida Knežević:** Nice to meet you too.

**Aida Knežević:** We meet at last.

**Kirsten Gibson:** Yeah.

**Kirsten Gibson:** I think I was out last week.

**Aida Knežević:** Yeah, yeah.

**Aida Knežević:** And it was, usually I do the strategy presentations, but I think that meeting time like two weeks ago was a little too late for me because I live in Europe.

**Aida Knežević:** So, I couldn't make it.

**Aida Knežević:** Where are you based?

**Kirsten Gibson:** I am in Indiana.

**Aida Knežević:** I'm like two hours south of Chicago.

**Aida Knežević:** Okay.

**Aida Knežević:** Okay.

**Aida Knežević:** Nice.

**Aida Knežević:** Hi, Rick.

**Ric Nguyen:** Hello.

**Ric Nguyen:** Hi, guys.

**Kirsten Gibson:** Hey.

**Kirsten Gibson:** Okay.

**Kirsten Gibson:** Rick, when I find the style guide, it's just the one.

**Ric Nguyen:** Yeah.

**Ric Nguyen:** Okay.

**Ric Nguyen:** I found it.

**Ric Nguyen:** Okay.

**Ric Nguyen:** Okay, cool.

**Aida Knežević:** Hi, Jason.

**Kirsten Gibson:** Come on.

**Aida Knežević:** Okay.

**Aida Knežević:** Is this everyone from your end?

**Kirsten Gibson:** Probably not.

**Aida Knežević:** Okay, okay, let's wait a little bit more then.

**Kirsten Gibson:** Yeah.

**Kirsten Gibson:** We're probably still waiting on Shaq and Teofi.

**Aida Knežević:** Okay, okay.

**Kirsten Gibson:** I don't think we had shared this yet.

**Kirsten Gibson:** I'm going to put it in.

**Kirsten Gibson:** I just downloaded a copy of it, our style guide.

**Aida Knežević:** Mm-hmm.

**Kirsten Gibson:** Full transparency, haven't had time to closely read the first article.

**Kirsten Gibson:** Mm-hmm.

**Kirsten Gibson:** So I'm doing this preemptively, not because I saw a bunch of issues or anything.

**Aida Knežević:** Okay.

**Aida Knežević:** Thank you.

**Kirsten Gibson:** Mm-hmm.

**Kirsten Gibson:** Okay, think this is all of us now.

**Aida Knežević:** Okay, okay, great.

**Aida Knežević:** Well, hi, everyone.

**Aida Knežević:** I haven't met some of you yet, so I'm Aida.

**Aida Knežević:** I'm an editorial account strategist at GrowthX.

**Aida Knežević:** I mainly develop content strategies for our clients, and I also lead the content calendar creation process, and I kind of shepherd the creation of the first couple of blogs that we send over to you, and I kind of run the calibration process.

**Meshach Cisero:** So it's great to meet everyone.

**Meshach Cisero:** Likewise, nice to meet you.

**Aida Knežević:** I've added everybody to the agenda, so you should get an email from Notion with the agenda in your inbox. There are a couple of things I wanted to go over with you all today — two major updates.

**Aida Knežević:** So last week we did share our content calendar with you.

**Aida Knežević:** And I know that your team has been reviewing it, but I would be just curious to see if anybody has like any additional thoughts on the topics that are here.

**Aida Knežević:** Last week, Teofi and Rick gave us some insights into some additional keywords that we could do, that we could use for keyword research.

**Aida Knežević:** But yeah, just curious to see if anybody has any other thoughts.

**Kirsten Gibson:** Um, from what I...

**Kirsten Gibson:** I was able to scroll through, it looked pretty good.

**Kirsten Gibson:** I wasn't sure, like, where I should give feedback, if there was a field.

**Kirsten Gibson:** Again, I just looked at it today, so.

**Aida Knežević:** No worries, no worries.

**Aida Knežević:** Nice cat, by the way.

**Aida Knežević:** My cat does the same thing when I'm in meetings, which is why I have to shut the door.

**Kirsten Gibson:** So, yeah, you can, let me just show that again.

**Kirsten Gibson:** Okay, I'll just add it as a comment there.

**Aida Knežević:** Yeah, yeah, you can just expand it and then add a comment.

**Aida Knežević:** can also tag me so that I get a notification.

**Aida Knežević:** You can leave, like, a thumbs up, thumbs down emoji, or if you want, provide more context.

**Aida Knežević:** That's also helpful.

**Aida Knežević:** I'm sure there are going to be some ideas where you're thinking, okay, we should have a specific opinion about this topic, or there's something really unique we should add to the conversation. You can also provide those thoughts in the comment box. We're creating SEO content — our goal is to get you organic search traffic and improve your visibility in AI search.

**Aida Knežević:** But that doesn't mean that the content has to be generic and not have, like, a unique point of view on specific topics.

**Kirsten Gibson:** So we can absolutely, like, inject that into the content.

**Kirsten Gibson:** Perfect.

**Aida Knežević:** Yeah.

**Kirsten Gibson:** And then remind me also, just a question I had on the keyword difficulty.

**Kirsten Gibson:** Is it higher the number, the more difficult, or the lower the number, more difficult?

**Aida Knežević:** Higher the number, the more difficult it is.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah.

**Aida Knežević:** But we've, interestingly enough, for AI visibility, and this is something that Eric mentioned yesterday when we were talking to a different customer, sometimes there seems to be no rhyme or reason.

**Aida Knežević:** Like, a blog post might be ranking on, like, page 8 of Google search, but it gets cited in an LLM.

**Aida Knežević:** So, like, there's...

**Aida Knežević:** AI is kind of unpredictable, but keyword difficulty is important from an SEO standpoint, just so we understand how hard it's going to be to rank, at least in Google.

**Kirsten Gibson:** Right, right.

**Kirsten Gibson:** Makes sense.

**Aida Knežević:** Yeah, yeah.

**Aida Knežević:** Okay, so yeah, I'll wait for your comments.

**Aida Knežević:** We did work on a blog post just to kind of keep things moving, and you can find it right here.

**Aida Knežević:** I decided, what is this?

**Aida Knežević:** Okay.

**Aida Knežević:** I decided to just use like a more, like a broad topic for us to calibrate on, because it would just be like easier for us to test like the tone and like the overall like writing style.

**Aida Knežević:** I know that your blogs have a very unique point of view and the writing style is quite unique, but I was curious to see what you think.

**Kirsten Gibson:** I thought it was a good topic to start with, because like you said, it's like in the realm of what we do, but kind of give some authoritative sort of, you know, aligning those differences.

**Kirsten Gibson:** I think one thing that, and again, I have not read this super closely, so it's like if it's in there, feel free to correct me.

**Kirsten Gibson:** I do think one thing that we need to hit with the tone, especially for something like this, is like we just need to be real with the audience in that we're talking about zero trust, accomplishing zero trust, or accomplishing least privilege, but we actually, we know that it's not like a zero-sum game.

**Aida Knežević:** Like you're never hit a hundred percent, something you're always striving for, so just having that empathy with the user, or like the end sort of the audience, I think.

**Aida Knežević:** Will be helpful as well.

**Aida Knežević:** That's very valuable feedback. I don't think that comes across in the content right now. We mention SpecterOps, but that empathy piece is missing and that's something we could add.

**Kirsten Gibson:** For sure.

**Kirsten Gibson:** Yeah, and it doesn't have to be like, like, I think once I, once I like actually have time to sit down and read it, I'll give you more valuable feedback of like where that we could add that stuff.

**Aida Knežević:** Okay, okay.

**Aida Knežević:** Yeah, and that's, that's totally fine.

**Aida Knežević:** With the clients I've worked with previously, it really depends on the industry, but they might have different opinions they want to come across in all of the articles. For example, we have one client — a web development agency — with an approach to web design that's all about composable design. They're quite unique in that sense, so they gave us a two-page Google Doc with talking points about their approach and why going composable is the way to go, with all these proof points.

**Aida Knežević:** So even when we're doing, like, standard SEO articles, we could still, like, say, you know, if you're working with a web designer, make sure that, like, they understand, like, this, like, specific approach because it'll be easier for you for XYZ reasons.

**Aida Knežević:** So it's, like, it doesn't even have to be, like, a super structured document.

**Aida Knežević:** Honestly, we've had, you know, you can, like, use, like, a voice recording app just to record your thoughts and, like, use ChatGPT to kind of create, like, a transcript or, like, a bulleted list and just send it to us.

**Kirsten Gibson:** Like, we'll make it work.

**Kirsten Gibson:** Okay, awesome.

**Aida Knežević:** I love that.

**Aida Knežević:** Yeah.

**Aida Knežević:** Okay, cool.

**Aida Knežević:** So yeah, I'll be waiting for your feedback.

**Aida Knežević:** Once we're in a good spot with tone and everything, our goal is to generate three blogs next week, then scale to five the following week. That's the typical cadence. Once this draft is greenlit and good to go, we can stage it in your CMS.

**Aida Knežević:** Okay, awesome.

**Aida Knežević:** Another update is that we have your Looker dashboard set up. I'm not sure if Erik covered this earlier, but we use Looker to combine data from Google Analytics and Google Search Console in a single report — it's a seven-page report covering different aspects of your website performance.

**Aida Knežević:** I'm going to give all of you editing access, so you should be able to kind of manipulate the data here and kind of, like, change the dates and, you know, change, like, the different views so you can kind of filter the data.

**Aida Knežević:** But I'm just going to go through this report, like, page by page, and you feel free to interrupt me if you have any questions.

**Aida Knežević:** So the first page combines data from Google Analytics 4, and this graph shows the percentage of engaged sessions versus regular sessions.

**Aida Knežević:** An engaged session in GA4 is a session that lasts longer than 10 seconds, or it includes a page scroll, or it includes a user clicking on a link on your website.

**Aida Knežević:** So it's basically the opposite of bounce rate and it is important for SEO because Google does take into account user engagement to measure if a website is helpful or not.

**Aida Knežević:** So the higher this percentage is, the better.

**Aida Knežević:** This is quite average from what I've seen so far with our other customers.

**Aida Knežević:** I would like it to be higher, but it's not super low.

**Aida Knežević:** So, and then you can kind of see a page by page breakdown below and you can also see the different sessions by referrals.

**Aida Knežević:** So this includes all referrals, not just email or social media, but it combines all the data.

**Aida Knežević:** Okay, this has an error.

**Aida Knežević:** I'll look into this, but it could just be like a temporary looker error, but

**Aida Knežević:** Basically, the non-branded, oh, wait, actually, this is because we don't have access to your GSC, I think, yet.

**Aida Knežević:** Did we get Google Search Console access?

**Aida Knežević:** I can't remember.

**Aida Knežević:** We did?

**Meshach Cisero:** Okay, okay, good.

**Aida Knežević:** All right, so it might just be, like, a connectivity issue.

**Aida Knežević:** Basically, the non-branded report includes a breakdown of Google Search Console data, but it's traffic data that comes from non-branded keywords, so all, like, keywords that don't contain your brand name.

**Aida Knežević:** The conversion events have, this is also data from Google Analytics 4, so these are all the conversion events that you have set up in GA4.

**Aida Knežević:** This is very customized, so I'm assuming that someone on your team has set this up.

**Aida Knežević:** It would be great if we could get a quick explanation of the different conversion events — where they're located on the website and what they do. This is pretty self-explanatory and much better than what I usually see, so it's straightforward. But if you want to give additional insight into which events are more important right now, that would be helpful.

**Kirsten Gibson:** Would that be a Garrett question, Jack?

**Meshach Cisero:** Yeah, like, I can take this one.

**Aida Knežević:** Okay, okay, cool.

**Aida Knežević:** And then you have like a breakdown of like different conversion events below.

**Aida Knežević:** The cohort report includes data from Google Analytics and Google Search Console. Once we start publishing, it will include data from the blogs we publish, and we can compare it to the rest of your website.

**Aida Knežević:** We can customize this, though, so that this report, like this page, just includes data from, just from growthx URL, so you can kind of clearly see how much traffic our content is generating from your, for your site.

**Aida Knežević:** And this is data, this data from GA4, but there should also be data, yeah, this, it's also going to contain data from Google Search Console.

**Aida Knežević:** Again, this is just data from your GSC, which is why it isn't showing up, so it's, the landing page report here, it's very similar to what you see when you log into Google Search Console, so you're going to be able to see.

**Aida Knežević:** So like overall like clicks, impressions, click-through rate, and average position.

**Aida Knežević:** So that should be like that's going to be in this report.

**Aida Knežević:** And the queries are also pulled from Google Search Console.

**Aida Knežević:** That's just a breakdown of all of like the different keywords that you rank for in Google Search that, yeah, that drive organic traffic to your site.

**Aida Knežević:** And then the last page is a breakdown of LLM referral traffic.

**Aida Knežević:** So you can actually see which LLMs are driving the most traffic to your site.

**Aida Knežević:** This is data from the entire year.

**Aida Knežević:** And every bar is a different week.

**Aida Knežević:** So it's like a week-by-week breakdown.

**Aida Knežević:** Most traffic comes from ChatGPT, which is pretty standard. Most of the customers that we work with also get the most LLM traffic from ChatGPT.

**Aida Knežević:** And what's good is that you...

**Aida Knežević:** Your, like, referral traffic from LLMs is growing.

**Aida Knežević:** There have been, like, weeks where it kind of dropped down, but for the most part, it seems to be growing.

**Aida Knežević:** In around August this year, ChatGPT updated their algorithm to favor websites like Wikipedia and Reddit when citing answers.

**Aida Knežević:** Which hit some websites, but not all of them.

**Aida Knežević:** It really depends on the topic that, you know, the user is searching for.

**Aida Knežević:** And then you can also see a breakdown of different...

**Kirsten Gibson:** Sorry, I just had a quick question on the LLM.

**Kirsten Gibson:** I think maybe Eric had showed us another site to dig deeper into the LLM.

**Kirsten Gibson:** Like, so, like, of those, like, what is it that they're searching for?

**Aida Knežević:** Yeah, yeah, that's probably Scrunch, right, Erik?

**Kirsten Gibson:** It probably is, yeah.

**Erik O'Brien:** Okay, yeah, yeah.

**Erik O'Brien:** It would be the only one that I have access to.

**Aida Knežević:** Just a quick...

**Aida Knežević:** Let me just find it really quickly.

**Aida Knežević:** Yeah, so...

**Aida Knežević:** Yeah, Scrunch is different in the sense that, like, for example, Looker lets you see, like, hard, like, real data, like, these are...

**Aida Knežević:** the volume.

**Aida Knežević:** Yeah, the volume, like, you can actually see where these people are, like, what they're visiting from LLMs, and you can see, like, which pages perform better.

**Aida Knežević:** There are a lot of, like, blogs here for now, and I do have to say that for, like, the vast majority of the clients that we work with, blogs get by far, like, the biggest chunk of LLM referral traffic, which is really good, like, for, you know, for visibility.

**Aida Knežević:** Yeah.

**Aida Knežević:** But Scrunch kind of complements that data because obviously in GA4 you cannot see your competitors' visibility and Scrunch kind of complements that data so you can actually see where you're at compared to all of these different companies.

**Aida Knežević:** So, yeah.

**Kirsten Gibson:** Cool.

**Kirsten Gibson:** Thank you.

**Aida Knežević:** No worries.

**Aida Knežević:** Did we share the prompts with the SpecterOps team, Erik?

**Erik O'Brien:** No, we did not.

**Aida Knežević:** We're using base prompts, which are generated in Scrunch. We give Scrunch a description of your company, descriptions of your audience, and we upload your competitors. Scrunch then automatically generates base prompts guessing what your audience would ask different LLMs, but we can also add many more prompts.

**Aida Knežević:** We can add hundreds.

**Aida Knežević:** I've seen like people tracking like over 10,000 prompts.

**Aida Knežević:** So we can like build on this list.

**Aida Knežević:** If you have any like ideas around what would be really important to track, you can also let us know.

**Aida Knežević:** I can show you really quickly what we're tracking right now.

**Aida Knežević:** So they group prompts into topics.

**Aida Knežević:** So we can see kind of, okay, let's go with like threat hunting techniques.

**Aida Knežević:** So these are like the ones that scrunch generated.

**Aida Knežević:** And if we click on a prompt, we can see.

**Aida Knežević:** Data from different LLMs.

**Aida Knežević:** Yeah, and like how many responses it has gathered so far.

**Aida Knežević:** Claude typically cites the least.

**Aida Knežević:** That's at least what Eric's been able to gather from all of the data he's analyzed so far.

**Aida Knežević:** Claude is really like, they're not going to cite anybody unless you actually turn that feature on.

**Kirsten Gibson:** Got it.

**Aida Knežević:** And then I also wanted to point out something that might come up, which is citations.

**Aida Knežević:** Your citation rate is 10%, which is quite high compared to what we're usually seeing — around 2-3%. But this is just from the prompts we're tracking. Sometimes the prompts may be a little like leading the witness, guiding the LLM to SpecterOps, but considering your competitors are trailing close by, this is still quite good.

**Aida Knežević:** What we typically see is a citation rate of around 3%, and I do have to say like when we upload new prompts, it's going to like change the data as it collects more like answers to those prompts.

**Aida Knežević:** But it's still like nevertheless, it's still helpful, and the topics help us understand, you know, we can also connect it back to the topic clusters that we have in your strategy and use them for ideation if we notice that your visibility is stagnating or it's dropping for a specific topic.

**Kirsten Gibson:** Makes sense.

**Aida Knežević:** Okay, cool.

**Aida Knežević:** Cool, I think, let me double check.

**Aida Knežević:** Yeah, I think those are all the updates that I

**Erik O'Brien:** I think we've had at least like one review of the artifacts that we sent over.

**Erik O'Brien:** It's been a couple weeks now, but just wanted to make sure that anybody else who may have been out of office has a chance to review those.

**Erik O'Brien:** I think, Kirsten, you mentioned you wanted to have Jason take a look, but it looks like Jason already popped in there a couple weeks ago.

**Erik O'Brien:** So, yeah, I think if we're good on those, just wanted to make sure we've got all the feedback that we would need.

**Erik O'Brien:** And then did we talk about images yet?

**Kirsten Gibson:** We had kind of talked about it, like that you guys do generate them.

**Kirsten Gibson:** And I think I had asked for like an example of something that you guys had done before.

**Erik O'Brien:** That is right.

**Kirsten Gibson:** I believe that.

**Aida Knežević:** Yeah, yeah, we can set some time with Katya, who's our designer, to mock up some examples.

**Aida Knežević:** But we can, let me actually go look at a couple of pipelines.

**Aida Knežević:** Maybe I can show you right now.

**Erik O'Brien:** And then while she's doing that, I don't, yeah, we haven't had the chance yet to do a kind of product walkthrough or a product deep dive.

**Erik O'Brien:** And was curious who might be best to do that with.

**Erik O'Brien:** I don't know if it'd be Kirsten and Jason from like the PMM team or who might be best just to kind of give us a talk over of kind of the product main features and kind of value that users would see just so that we have some additional context.

**Kirsten Gibson:** Go ahead, Meshach.

**Meshach Cisero:** If, Jason, if you don't feel comfortable, I can set up a conversation with Rich from our product, from our PM team.

**Jason Wolfe:** I mean, I can, like, go through the motions of working in the product, but Rich or an SE would probably have more.

**Kirsten Gibson:** Yeah, I was going to suggest an SE, actually.

**Jason Wolfe:** Like, Jonathan Parfait would probably be great for it.

**Kirsten Gibson:** Yeah, I agree.

**Jason Wolfe:** Because they know, they have the muscle memory of what customers want to see, what folks say in real time.

**Jason Wolfe:** Like, I'm not in front of customers much anymore to see how they react.

**Erik O'Brien:** Yeah, that'd be awesome.

**Meshach Cisero:** Yeah, I could set that time up.

**Meshach Cisero:** Who should I, on your side, Erik, who should I include on that call?

**Erik O'Brien:** That's me.

**Meshach Cisero:** Okay, just you?

**Erik O'Brien:** Yep.

**Meshach Cisero:** Okay, cool.

**Meshach Cisero:** I can do that.

**Meshach Cisero:** I'll set that up for sometime next week.

**Erik O'Brien:** Wonderful.

**Aida Knežević:** Okay, so, yeah, these are the examples for one of our customer.

**Aida Knežević:** They are, like, an AI app development platform.

**Aida Knežević:** These are their brands.

**Aida Knežević:** So usually what they'll do is send us like a Figma file or a Google Drive folder with different brand assets and fonts, and then our designer can use that to kind of mock something up.

**Aida Knežević:** We use GPT to generate these.

**Aida Knežević:** She creates like a detailed prompt that kind of guides the image generation process.

**Aida Knežević:** So like, let me know, is this look a little like too abstract or, I know it's like not your industry, so it's like slightly different, but I think it gives you a good idea of like what we can do.

**Kirsten Gibson:** I'll defer to Rick.

**Ric Nguyen:** I mean, they look great.

**Ric Nguyen:** I'm just curious how it look like with our branding.

**Aida Knežević:** Yeah, yeah.

**Aida Knežević:** I think we can use like your brand.

**Aida Knežević:** Colors and fonts.

**Aida Knežević:** We can also add like for, it depends on what you want, but we can also add like a text overlay on top with like the title, the article title.

**Aida Knežević:** So there are different options that we could do.

**Aida Knežević:** But I think what would be a good idea is we will actually like create an image and pipeline for you.

**Ric Nguyen:** And then you can actually see like, okay, what this looks like for your company.

**Ric Nguyen:** I have a brand standard guide that I can share with you that it's, it's not official, but I, it does contain like our illustrations, our icons, our kind of branding design language that I think would be helpful for this for you guys.

**Erik O'Brien:** We do not.

**Erik O'Brien:** No, I checked.

**Erik O'Brien:** I was gonna say we can definitely use the style guide because it does have some of the colors and kind of guidance on images.

**Erik O'Brien:** but I think that would be even more helpful.

**Ric Nguyen:** Yeah.

**Ric Nguyen:** Yeah.

**Ric Nguyen:** I'll get that over to you guys.

**Erik O'Brien:** Awesome.

**Aida Knežević:** Okay, cool.

**Aida Knežević:** Well, if that's everything, I think we can wrap up two minutes early, but I'll be waiting for your comments on the blog and, like, on the assignments and the content OS.

**Aida Knežević:** In the meantime, you can reach out to me with any questions.

**Aida Knežević:** Okay.

**Aida Knežević:** All right.

**Aida Knežević:** Thank you.

**Aida Knežević:** Have a great rest of your day.

**Aida Knežević:** Bye.

**Aida Knežević:** Bye.
