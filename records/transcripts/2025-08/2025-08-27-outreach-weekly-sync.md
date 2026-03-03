# Outreach Weekly Sync

<metadata>
date: 2025-08-27
time: 16:30 UTC
duration: 24 minutes
organizer: Jo Kaminska (GrowthX)
participants: Hadassah Pegado (Outreach), Maria Akhter (Outreach), Aida Knezevic (GrowthX), Jo Kaminska (GrowthX)
fathom_recording_id: 83311635
fathom_url: https://fathom.video/calls/391070604
share_url: https://fathom.video/share/zasvSuPih2Z6LeNp4yheUW8r9aC5jGzP
source: fathom
enriched_on: 2026-03-03 14:00 UTC
</metadata>

---

## Summary

GrowthX and Outreach reviewed content strategy progress, focusing on the Looker dashboard integrating GA4 and GSC data to track LLM referral traffic from ChatGPT, Perplexity, and Gemini. Outreach's AI agent pages launched two weeks ago with low initial visibility in LLM responses but expected improvement as mentions scale across existing content refreshes and new articles. The team confirmed a staging timeline of 1-2 days post-review, discussed Scrunch data on 50 new prompts generated from customer questions, and Jo Kaminska transitioned off the account—a new managing editor joins next week with full knowledge transfer while Jo supports the team for questions.

---

## Context

Outreach is a sales engagement platform (outreach.io). GrowthX is managing their content strategy as part of a broader engagement covering both content production and AEO/AI visibility research. Hadassah Pegado heads Outreach's content and marketing efforts, with support from Maria Akhter on strategy questions. GrowthX's delivery team (Aida Knezevic, Jo Kaminska) is producing content refreshes, net new articles, and analyzing visibility across AI-powered search engines. This weekly sync is a standing check-in on content approvals, publishing cadence, Scrunch data analysis, LLM referral performance, and team transitions.

---

## Relevance

**To GrowthX Delivery:**
- AEO content strategy working: 50 customer-informed prompts added to Scrunch; LLM referral traffic tracking (ChatGPT leading, then Perplexity, Gemini) now visible in Looker dashboard alongside GA4/GSC data
- GA4 event tracking gap identified: "GA_event" (qualified bot conversions) not yet integrated into Looker; Jo to coordinate with analytics team to close integration
- Staging and publishing cadence clarified at 1-2 days post-review; GrowthX's designer (Katya) iterating on featured images to match Outreach brand style
- Ongoing challenge: AI agent visibility still low despite recent page launch—strategy includes refreshing existing content, creating net new content, PR placements, and G2/review site updates

**To GrowthX Business Development:**
- Account health signal: Outreach approvals process and GA event tracking show signs of operational complexity; team transition (Jo → new editor) presents continuity risk but mitigated by knowledge transfer and experienced new hire
- Expansion opportunity: Looker dashboard use case demonstrates value of integrated AEO + analytics reporting; similar setup could apply to other clients

**To CheckThat:**
- Competitive visibility data: In AI sales agent queries, SalesLoft mentioned 86% of the time vs. Outreach significantly lower; data integrations queries show zero mentions for all competitors—white space for future Outreach content
- LLM referral attribution working: Can now tie specific content to ChatGPT/Perplexity/Gemini traffic, enabling prompt-level performance measurement

---

## Overview

- New AI agent pages live ~2 weeks ago; visibility in LLM responses still low but expected to improve
- Looker dashboard integrating GA4 and GSC data now available, showing LLM referral traffic
- Jo transitioning to new team; new managing editor to join next week with full knowledge transfer

---

## Key Topics

### Content Strategy and Approvals

- 13 assignments left in "considering" status; most to be approved
- Last week's batch reviewed, to be staged this week
- Featured images replaced with Outreach-created designs; designer experimenting to match GrowthX style
- Flexible staging schedule, typically within 1-2 days after review

### Scrunch Data Analysis

- 50 new prompts added based on customer questions from sales calls
- Low visibility for Outreach in responses, but competitors also not dominating
- Some queries (e.g., AI sales agents) show competitors like SalesLoft mentioned 86% of the time
- Opportunity identified for future blogs on topics with low mention rates

### Improving AI Agent Visibility

- Recent launch of AI agent pages (2 weeks ago) contributes to low visibility
- Strategy: Mention AI agents throughout site, in refreshes, new content, PR, and third-party sites
- Recommendation to update G2 profiles and review websites to boost AI agent prominence

### Looker Dashboard Overview

- Integrates GA4 and GSC data, complementing Scrunch insights
- Key metrics: sessions vs. engaged sessions, referral sources, search ranking distribution
- Non-branded report showing clicks and impressions from GSC
- Conversion events tracking, with focus on demo requests and qualified bot interactions
- Cluster performance tracking for GrowthX-produced content
- LLM referral traffic breakdown (ChatGPT leading, followed by Perplexity and Gemini)

### Team Update

- Jo moving to a different team due to internal reshuffling
- New managing editor to join next week with full knowledge transfer
- Aida assures high standards will be maintained with experienced new editor

---

## Action Items

**Hadassah Pegado (Outreach)**
- Approve remaining 13 assignments in consideration status today
- Talk to Paul about updating G2 profiles and review sites to highlight Outreach's AI agents prominently
- Confirm correct GA4 event name for qualified bot interactions (believed to be GA_event); share with GrowthX team

**Aida Knezevic (GrowthX)**
- Inform staging person to schedule content 1-2 days post-review (confirmed flexible timing with Outreach)
- Send Scrunch data screenshots to Outreach via Slack (showing 50 customer-informed prompts and visibility gaps)
- Add new managing editor to Slack channel and facilitate knowledge transfer from Jo

**Jo Kaminska (GrowthX)**
- Check with GrowthX analytics team to confirm GA_event integration status for qualified bot tracking in Looker dashboard; circle back to Outreach with findings

---

## Transcript

**Aida Knezevic:** How's it going?

**Hadassah Pegado:** Good, good. I've been fighting a lingering cold that I caught from my daughter, but I'm going to feel better today.

**Jo Kaminska:** Fully, fully feeling better.

**Aida Knezevic:** I hear that a lot from parents, like getting sick because of your kids.

**Hadassah Pegado:** Goodness, yeah. Especially once they start school. I used to doubt how bad it could be, but now that she's in school, yeah, it's pretty bad. It's like every other week, there's something. So it's always like, let's try to contain it.

**Aida Knezevic:** I had like one of my closest friends, she started daycare when she was maybe a year old, and she had every type of illness imaginable, like just from that experience.

**Hadassah Pegado:** So now she is like, she never gets sick. Like if she gets sick, we know it's serious.

**Aida Knezevic:** Yeah. She has the immune system of a horse.

**Hadassah Pegado:** Yeah. Her immunity just skyrockets.

**Aida Knezevic:** So she's great.

**Hadassah Pegado:** So you have that to look forward to.

**Aida Knezevic:** You got to hold on to that.

**Hadassah Pegado:** My daughter's pediatrician always says that to us. She's like, the benefit of it is that she's getting everything she needs in terms of her immunity, which is just going to keep getting better. So there's the pros there.

**Aida Knezevic:** Well, thank you so much for joining. I shared the agenda beforehand. So not a lot to cover today, but I did see that we have some new assignments that are approved to start. And I just wanted to kind of get your feedback on the overall direction, what you thought. I know you said there could be like some overlap between some of the existing content, but as a rule of thumb, we always do a Google search just to make sure—first to check what's already on your website for that keyword. There could be something related that we can reference, but also to make sure that we're not actually duplicating anything.

**Hadassah Pegado:** Got it. No, that's perfect. And thank you for sharing that context because that helps a lot. Yeah, no, I honestly, just reviewing it, everything looked pretty good. There was just one or two that I don't remember now from the top of my head that I thought we had something similar. But overall, like what I'll do today, I'll probably approve most of these or even all of them, because I think this is kind of what we're wanting to focus on regardless. So I think we're in a good spot there.

**Aida Knezevic:** Okay, perfect. Yeah, I think there's only like 13 left in considering. So you approved most of those.

**Hadassah Pegado:** Let me do that. Perfect.

**Aida Knezevic:** Sounds good. All right. I think last week's batch was reviewed. So we're going to stage it this week. And then you can go ahead and publish. We did see that a lot of the featured images were replaced by the images that you created.

**Hadassah Pegado:** So we shared them with Katya, who's our designer. So she's going to experiment in the workflows a little bit to see if we can get it closer to your designs.

**Aida Knezevic:** Awesome. No, thank you. Appreciate that.

**Maria Akhter:** That'd be great. Thank you. I also had a question on sort of your cadence. I was curious if you guys have sort of like a flow in terms of when you do reviews and when you do staging? Like, is it like Thursdays are your staging day or like Wednesdays are your staging day? Or is it really just kind of whenever the blog is ready to go, it'll be, you'll stage it that next day?

**Aida Knezevic:** Yeah, yeah. It really, it's kind of hard to, like, I think if you want to set a cadence, we can also implement that. But it varies a lot depending on, like, client availability and who's doing the reviews.

**Maria Akhter:** Okay, that makes sense.

**Aida Knezevic:** Yeah, yeah. I mean, if there's a day of the week that works for you, then just let us know and we can schedule them to be staged on that day.

**Maria Akhter:** I'm open. I guess I was just more curious around your workflow. Yeah, I guess whatever, maybe whenever, like, the next day or two after review within that time frame would be great.

**Aida Knezevic:** Okay. That works. Yeah. Thanks. We have someone who's responsible for staging. I think I mentioned that to you before. So I'll mention that to him. Okay, great. Another thing is, this week, we're doing the three refreshes, the two net new articles. And I had a scrunch update for you. So last week I added, like, I generated prompts using the question, like the customer questions that you shared from your sales calls. And that kind of skewed the data a little bit, so it looks like, because your visibility for those prompts is not that good. Like, it's just, to put it bluntly, it's just not very high. The good thing is, like, your competitors are also aren't really showing up for those prompts. So that's a positive. But to give you an idea, let's just go over to prompts. And I set up a tag. So this is just, there's like 50 prompts in here. So, for example, when we look at this question around AI sales agents being truly agentic versus just automated, like, Sales Loft is mentioned 86% of the time. So you did get some mentions, but Sales Loft is kind of leaving that conversation. When it comes to AI agents ingesting data and first-party, third-party data integrations, like, nobody's getting mentioned. So this is an opportunity for future blogs. Same with a similar case with third-party data integrations. And then we have, for example, this one: what kind of business results should I expect from AI agents? Clary and Gong have been showing up pretty consistently.

**Hadassah Pegado:** Do we see where what exactly it's being mentioned from, from our competitors? Like, what could be?

**Aida Knezevic:** Yeah, unfortunately, I don't think so. Let me actually see. Because I don't think Scrunch has a database with that information. Now, let me take a look. Okay, let's see this one. I don't know why it's not working right now. I think if it doesn't work right now, I can go back and take a look later.

**Hadassah Pegado:** Oh, here we go.

**Aida Knezevic:** Kind of a breakdown. Yeah, so it's kind of like breaking down. So this is the number of responses. And then for each of these, it kind of gives color codes the answers. So it's not, we don't have insight into the.

**Hadassah Pegado:** Got it. And from your perspective, do you think because we just recently created these AI agent pages, it's recent on being indexed and whatnot, do you think that could be the reason why we're not being referenced as much or is it just?

**Aida Knezevic:** Yeah, yeah, for sure. When did those AI agent pages go live?

**Hadassah Pegado:** I think it was last week, right, Maria?

**Maria Akhter:** I think two weeks ago now.

**Aida Knezevic:** Yeah, I think that's definitely one reason. It was like being indexed fairly recently. And then it's just not just that specific page, but it's also like how they're mentioned throughout your site. So as we're doing the refreshes and the new content, like we're going to work those AI agents in. So there's more data to pull from.

**Hadassah Pegado:** Okay, yeah. Okay, thank you.

**Aida Knezevic:** Yeah, and anything that you do in terms of PR or being mentioned on other websites, if you could just mention those AI agents in there, that would be very helpful.

**Hadassah Pegado:** Got it. Oh, that's good to know. Yeah, because I was going to ask, like that was going to be my next question in terms of now that we have this information and we're seeing opportunities of what we can work on and what new content we can build. I was going to ask if that's going to be taken into consideration for the net new content that we'll be developing with you guys. So just wanted to ask that.

**Jo Kaminska:** Yeah, yeah. I would add here that if you update your G2 profiles, et cetera, so all the review websites and basically make it more prominent around AI agents, that should help too because these websites already have an authority. So these citations also can go through these type of channels.

**Hadassah Pegado:** For sure. Oh, that's good to know. Okay. I'll mention that to, I'm going to talk to Paul about that too, in our team, because he handles, he works closely with Joe, who handles paid, and I think they have ownership on things like that, so I'll double check.

**Aida Knezevic:** Mm-hmm. Okay, nice. And that's kind of, I mean, it's related, and it's no surprise, but for example, when we look at citations for this group of prompts, but I think the same happens just when we take into consideration all of the prompts, that you aren't being cited in these answers. And that kind of points to the fact that other websites, like industry blogs, and some of your competitors—a small percentage—they're kind of shaping that conversation. So it's important to know that Scrunch, their API uses the research mode by default, so it always gets citations. And a normal user who's using like ChatGPT or Claude or another LLM, they might not turn this on. So sometimes it's turned on sporadically by the LLM, but it isn't always on. But like Scrunch turns it on by default so that it can measure the citation. So they're not like super important, I mean, they are important, but I wouldn't put so much value on them because they might not appear for someone who's just using ChatGPT on their phone or something. But I do think it's important to get some of these citations up and have your content and your website being referenced in these responses. So I think the more we mention these AI agents and the more content we create, we should be seeing these numbers go up.

**Hadassah Pegado:** Sounds good. No, that makes sense. Thank you.

**Aida Knezevic:** No, no problem. I'll send over screenshots afterwards, so you can keep this data for yourself. And then, let me see if we have, yeah, Jo, did you want to show the Looker dashboard? Because that's also ready for the team.

**Jo Kaminska:** Yep. Let me just pause. And also, one thing to note about the Looker dashboard is that it integrates GA4 and GSC data, and there's a page that just breaks down your LLM referral traffic. So the data from Scrunch and that data kind of complement each other. So you can see what pages are getting referrals from different LLMs. And it's also more verifiable than Scrunch prompts because those are just reverse-engineered user prompts.

**Hadassah Pegado:** Yeah, yeah. That's fair.

**Jo Kaminska:** So we have a couple of tabs that I wanted to show you quickly today. First of all, so we have two sources of this data. First source is Google Analytics and the second one is Google Search Console. So here in the overall tab you have more Google Analytics data. So basically sessions versus engaged sessions for all the landing pages. Sessions also by referral—so which engines are bringing you the traffic. And once it's loaded, search ranking distribution—so basically for how many queries you rank in the top one, between 11 and 20, etc. Just, they are pretty slow to load sometimes. But these Query Rankings are basically taken from Google Search Console. So that's how the general dashboard looks like. You can change the data range here. So I give you view access, but if you would like to dive deeper into specific data range and basically check specific data points, we can give you editor access as well. So you can also play around with this. The second report is...

**Maria Akhter:** Quick question on that, Jo. What's the difference between sessions and engaged sessions? Is that if they've interacted with a CTA or something that moves them to engaged session?

**Jo Kaminska:** Yeah. So basically sessions are like a starting point and engaged session is more measured like if they scrolled, if they interacted with an event. So let's say page click.

**Maria Akhter:** Okay. Got it.

**Aida Knezevic:** Thank you. The GA4 specifically measures an engaged session as lasting longer than 10 seconds or including a click on an internal link or a scroll. So those are the three events that are taken into account.

**Jo Kaminska:** Yeah, exactly. And the second one is non-branded. So basically, this data is pure Google Search Console data—clicks and impressions. So when it comes to impressions, we're generally taking into account how many impressions you got for a specific page. When it comes to clicks, this data will be higher than sessions because there's a difference between clicks and sessions. Not all the clicks will end up in sessions, but this is why we have combined these two dashboards to show you these two data points. Another report is conversion events. So basically, here we could ask you if any of these conversion events is more important for you, so we take a closer look going forward. But I would say in typical GA4 setup, it comes down to page views, engagements, sessions, and some demo requests or sign-in events. So if you have any insight here, we could prioritize basically reporting on it going forward.

**Hadassah Pegado:** Yeah, yeah, the demo request for sure. And I have to double check which one is the one for our qualified.

**Jo Kaminska:** Yeah, that would be helpful.

**Hadassah Pegado:** Let's see here. I didn't have it here.

**Jo Kaminska:** This is sign-in.

**Hadassah Pegado:** Yeah, I don't know if it's that. We don't have this one like the demo here, so I'm wondering if it works right now or like we should find a way to update the event so we have it tracked here. It's a matter of just creating it in Google Analytics and then we can pull this data automatically.

**Hadassah Pegado:** Okay.

**Jo Kaminska:** Sounds good. I think this report is one of the most interesting because literally what we are doing here is separating non-growthx URLs from the pillar page—the topical clusters that we are producing. So here you can see that we produced, like we refreshed content within just one cluster. So you can see data here about the revenue operations and AI workflow automation cluster. But once we refresh more content pieces and produce net new, you will see more clusters. Basically, these cohorts give you an idea of the value of the engagement that you're getting when it comes to this collaboration. And the rest, I think, is typical landing page report. So checking specific URLs and how they are performing. Again, that's Google Search Console data. You can click on a specific URL and basically get more granular. Like for some reason, these daily weekly reports don't load that fast. So, yeah, we have to sometimes wait, but you can check specific URLs and get an idea of their current performance. Queries again from Google Search Console, and we are tracking all these queries that you can find in your tool once it loads.

**Hadassah Pegado:** No worries. Oh, and by the way, for the qualified bot, the event is called GA underscore event. So that's the one. The key event set up for qualified.

**Jo Kaminska:** Okay. I didn't see that event here. So maybe you should. So we, for some reason, we don't have this one, but I can check with our analytics team whether it's something around integration or we should add it.

**Hadassah Pegado:** So it's called GAEvent. Yeah, I just sent it on the little chat.

**Jo Kaminska:** Okay, okay, cool. I'll check it out and I'll circle back for sure. Yeah, and the last report—as Aida said—Scrunch data shows you specific prompts and the presence versus non-presence. But here we have a Google Analytics report that breaks down the referrer traffic by the LLM. So you can see that ChatGPT gets the most sessions, then it's Perplexity, then it's Gemini, a bit less from Claude.

**Hadassah Pegado:** No, so this is really helpful. I feel like the team will love being able to see this.

**Jo Kaminska:** Yeah, I think this report complements the Scrunch data very well. So you can see your presence—which LLM is basically dominating and drives the organic traffic. And when it comes to data like this LLM data, it looks pretty good because I'd say impressions in LLMs is one thing, but people actually clicking and getting to your website based on responses to prompts is another. So I would say that this data looks very good and would be great to track going forward—how these LLM generated sessions are increasing based on the content we produce and refresh as well. So these are the dashboards in a nutshell. I think they provide you with an overview of where you're getting traffic from, for what queries, what is the distribution, and everything around LLM acquisition. And then later on, everything comes down to tracking a specific prompt.

**Hadassah Pegado:** Thanks. This is great.

**Aida Knezevic:** Thank you. Okay. Perfect. So we have a little team update at the end. So the TLDR is that Jo is moving to a different team because there's been some internal reshuffling lately. But you will have another managing editor step in from next week. We're going to do a big knowledge transfer internally. So you don't have to worry about them missing context or anything. And all of our managing editors—more than half of them—are people that I worked with before at different agencies. So they're all really experienced and have a really high bar for content quality. So I will let you know when that person, like, I'll add the person to the channel. We'll do a knowledge transfer and then, yeah, Jo will still be here.

**Jo Kaminska:** For like questions and to jump in if there's any confusion, but we're going to have a new editor join the team. Yeah, exactly. Yeah, I'll be supporting other teams, but yeah, I wanted to say thank you so much for the collaboration. It was brief, but yeah, I'm very grateful. Like you have great marketing and SEO knowledge, so I've learned a lot from you and the ways that you're organizing content. You are super organized, so I know that it's not only my opinion that the collaboration was super enjoyable, it still is. So thanks so much for the collaboration until today.

**Hadassah Pegado:** Yeah, for sure. Thank you. Like as Maria mentioned here on the chat, we'll for sure miss you and excited for your new endeavor and your new journey. I hope you have a good time doing that and I know we'll still be in touch, but we'll definitely miss seeing you more often here. Yeah, great to work with you for even just a brief amount of time.

**Jo Kaminska:** Yeah, likewise.

**Aida Knezevic:** All right. Great. Well, if you don't have any other questions, I think we can wrap up and I'll follow up in Slack with the scrunch data.

**Hadassah Pegado:** Okay. Yeah. No, that's perfect. That's all I have. Yeah. Thank you. All right. Thank you. Take care. Bye.
