# Director Standup

<metadata>
date: 2025-09-10
time: 19:00 UTC
duration: 28 minutes
organizer: matthew@growthx.ai
participants: Andi Bailey, Jakub Rudnik, Kyle Gaudreau, Matthew Panzarino, Megan Dickey
fathom_recording_id: 86393750
fathom_url: https://fathom.video/calls/405003332
share_url: https://fathom.video/share/5CK_APNziCwXQxCPnByRvDERS_rhBhsB
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

The GrowthX leadership team reviewed best practices for technical SEO audits, comparing Ahrefs vs SEMrush and debating whether to focus on all flagged issues or prioritize page speed metrics and competitor benchmarking. Jakub shared a live demo of his SEO audit workflow for Interwell (identifying broken internal links) and Folsom (improving health score from 50 to 85), then the team explored content strategy challenges for DeepGram—specifically how to identify gaps in speech-to-text content targeting pharmacy and QSR industries without a "magic bullet" tool. Kyle emphasized that no perfect solution exists for automated topical analysis, but the team agreed to explore the Ahrefs MCP (Machine Learning, Crawling, and Processing) server to potentially combine API data with AI analysis for faster keyword research and topic generation.

---

## Context

This is an internal GrowthX director standup held on September 10, 2025, bringing together the delivery leadership team to align on operational processes and client-facing methodologies. The context is a period of internal standardization—Andi Bailey explicitly flagged that the team doesn't have documented best practices for SEO audits and needs alignment on how different people approach the work. The team is managing multiple active clients (DeepGram, Interwell, Folsom) at various stages of technical SEO and content strategy work. The organizer, Matthew Panzarino, is also involved in infrastructure discussions (SEMrush Enterprise setup). A secondary theme emerged around scaling: as the team handles more clients, the pain point is that content strategy and keyword research require heavy manual research and critical thinking—no platform or tool fully solves the problem of identifying topical gaps in emerging spaces (like DeepGram's speech-to-text niche).

---

## Relevance

**To GrowthX Delivery:**
- Team should standardize on Ahrefs over SEMrush for technical SEO audits (Jakub's preference; Enterprise SEMrush setup is expensive at $10/month per site audit). Jakub is finding more actionable signals in Ahrefs for broken internal links and site health scoring.
- Page speed metrics (First Contentful Paint under 2 seconds) should be the primary focus in audit reports, not all flagged issues. Teams can surface this to clients' dev teams using free Google tools (pagespeed.web.dev) and competitor benchmarking to justify prioritization.
- Interwell identified broken internal links (actionable fix). Folsom improved health score from 50 to 85 by fixing flagged errors (demonstrates ROI messaging for clients).
- Meeting cadence: Shifting from Monday/Wednesday to twice-weekly standup (currently stable client base doesn't require daily check-ins).

**To GrowthX Business Development:**
- DeepGram engagement is evolving: initial proposal was middle/bottom-of-funnel content strategy, but client pushed back wanting more top-of-funnel coverage specifically for speech-to-text APIs targeting pharmacy and QSR (drive-thru) industries. This signals potential scope expansion or challenge to GrowthX's initial strategic recommendation.
- Clients want measurable KPIs beyond "articles published per week." Folsom example shows health score improvement resonates; need to surface similar metrics for other clients.
- Interwell and Folsom represent good account health signals (both engaged in technical optimization work with GrowthX guidance).

**To CheckThat / AI Visibility:**
- Ahrefs MCP (Machine Learning, Crawling, and Processing) server is being evaluated by the team for potential integration with keyword research workflows. Cost-effectiveness and scalability (token usage) are still unknown but worth exploring.
- Kyle flagged the broader gap: combining real SEO platform data (Ahrefs, SEMrush) with AI analysis could dramatically reduce manual research time. This is exactly the kind of workflow CheckThat/AEO tools could optimize.
- No "magic bullet" currently exists for automated content gap analysis in emerging verticals (DeepGram speech-to-text example). Solving this is a significant competitive advantage.

---

## Overview

- SEO audits should focus on page speed metrics and competitor benchmarking rather than fixating on all flagged issues
- Content strategy requires manual research and critical thinking; no "magic bullet" exists for comprehensive topical analysis
- The team sees potential in leveraging AI (e.g., Ahrefs MCP) to streamline keyword research and content gap analysis processes

---

## Key Topics

### SEO Audit Best Practices

  - Jakub prefers Ahrefs over SEMrush for technical SEO audits due to more comprehensive data
  - Focus on page speed metrics (e.g., First Contentful Paint \< 2 seconds) as they correlate with conversion rates and SEO performance
  - Common issues affecting page speed: excessive JavaScript, unnecessary tags, and uncompressed images
  - Benchmark against competitors' page speeds to determine improvement priorities

### Content Strategy Approaches

  - Avoid blindly copying competitors' content strategies, as they may not be effective
  - Utilize Google site: operator to find relevant content within a specific domain
  - Explore niche SaaS companies in the target industry for content ideas
  - Analyze backlink anchor text to discover relevant product/service synonyms and categories
  - Consider using AI to analyze internal linking structures for optimization insights

### AI-Assisted Keyword Research

  - Team expressed interest in leveraging Ahrefs MCP (Machine Learning, Crawling, and Processing) server for more efficient keyword research
  - Potential to combine AI analysis with platform data for faster, more insightful topic generation
  - Further exploration needed to determine feasibility and cost-effectiveness of implementation

### Client-Specific Discussions

  - DeepGram: Requested focus on speech-to-text API content, particularly for pharmacy and QSR (drive-thru) industries
  - Interwell: Identified broken internal links, presenting an opportunity to improve site health score
  - Folsom: Improved site health score from 50 to 85 by addressing flagged issues

---

## Action Items

**Andi Bailey (GrowthX)**
- Create and distribute table for all team members to fill in: client name + weekly article count (needed for fundraising narrative)

**Kyle Gaudreau (GrowthX)**
- Fill table with your client(s)' weekly article counts by end of day

**Matthew Panzarino (GrowthX)**
- Fill table with your client(s)' weekly article counts by end of day
- Explore Ahrefs MCP setup and share findings on feasibility and cost

**Megan Dickey (GrowthX)**
- Fill table with your client(s)' weekly article counts by end of day

**Jakub Rudnik (GrowthX)**
- Fill table with your client(s)' weekly article counts by end of day
- Continue developing automated anchor text analysis process for backlink research (mentioned wanting to create a document)

---

## Transcript
**Kyle Gaudreau:** Is that your Mrs. Doubtfire impression?

**Matthew Panzarino:** Hello.

**Megan:** Classic, classic film.

**Kyle Gaudreau:** Agreed.

**Andi Bailey:** All right, guys, before we do anything else today, I have a pop quiz that relates to fundraising that I need to go around the room and ask.

**Andi Bailey:** So we, I'm trying to get a sense of how many articles we're publishing every week for all of our clients.

**Andi Bailey:** So, uh, I'm not sure the best place to put that.

**Andi Bailey:** Actually, maybe, okay, this is what we're going to do.

**Andi Bailey:** If you guys can pull, oops, just like write your client name and the number in this table, that would be very helpful, ideally before the end, please before the end of the day.

**Andi Bailey:** I have like a rough idea, but just drop those in for fundraising questions.

**Kyle Gaudreau:** Sorry, what's the timeframe per week?

**Andi Bailey:** Yeah, per week.

**Kyle Gaudreau:** Yeah.

**Andi Bailey:** Cool. The other thing is I made this a Monday, Wednesday, Thursday meeting, like not everybody can make it. And I think we're okay on Monday, Wednesday right now. Our clients are in a relatively stable place, so we can bring it down to twice a week.

**Andi Bailey:** And then today, I wanted to ask Jakub to maybe share his screen and run through his SEO audit process. I think everybody might do it a little bit differently—I actually don't know how to do it. So this is selfishly for me, but also I think we should align on what we're looking at and how we're doing this generally. I don't think we have all come together on best practices here.

**Jakub Rudnik:** So for SEO audits, that's where to focus. Some of the places that's come up—and correct me if I'm missing anything—is we just did some technical SEO work for Interwell, where they were specifically looking for technical SEO help. And then I'm wondering if there was another client so I can frame this properly?

**Andi Bailey:** Well, actually, like it came up in Deepgram right after that too.

**Andi Bailey:** So that's why it's so top of mind for me, where we had done a high level audit and they have a ton of content.

**Andi Bailey:** And so we, our proposal was like, let's go more middle funnel, bottom of funnel.

**Andi Bailey:** And we got challenged on like kind of the top of funnel content that's getting clicks and whether they wanted more top of funnel content that was really specifically related to the two industries they're going after.

**Andi Bailey:** So, I mean, that's a little bit broader, but just like an analysis of coverage and yeah, it's a bit of a different, bit of a different tilt.

**Andi Bailey:** to the interwell conversation, but it did come up.

**Jakub Rudnik:** Yeah, so that's more on like the strategy and keyword side.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** I can share and then please just let me know where you want me to go with it.

**Jakub Rudnik:** There's, yeah, so let's see.

**Jakub Rudnik:** I would rather use Ahrefs than SEMrush for technical audits right now. I just ran a site audit for Interwell before this call and it gave me way more actionable findings than I was able to easily pull from SEMrush. I have more experience in Ahrefs too, so that's my preference. Jason and Matthew have been working on getting SEMrush Enterprise, which would help with setting up multiple site audits without paying extra for each one. Right now in SEMrush, if the only one I have set up is Oatling Code, every other client costs $10/month for the audit feature. So I've been in a holding pattern waiting for Enterprise access. With Interwell, I was just able to set this up, and I was trying to do this in about 10 minutes before the call to gather some additional findings. You come in, set up site audit and new project, import GSC and GA4 data, set competitors—it's similar to setting up Sprout for somebody, but you get way different types of data.

**Jakub Rudnik:** For Folsom, they did a lot of this analysis on their own before we started working with them, and they asked me questions about their findings. They had a health score of 50 and we just fixed errors until it went up to 85. I don't know that that means their site is super healthy, but they were really excited—like, your recommendation moved this up 6 points. That's one way to show impact beyond how much we publish. Most of them see traffic down as a site, but they're happy because we've been addressing AI overviews and they're satisfied with that work. Now coming into Interwell, I've found broken internal links and other things. Let me pull this up—sorry, I haven't done a site audit in a while.

**Jakub Rudnik:** Click down to internal with errors—broken page links. I found something I wasn't finding in any other tool. Screaming Frog would find it, but this type of finding means we can move their site score pretty dramatically. I sent them a Loom—we found one error and there's a whole list of things for me to work through and give recommendations. Some of this is in GSC or used to be. What I'm doing with Interwell at the macro level is finding obvious errors we didn't cause but are broken on their site. Then for the micro level, I zoom in on specific page types based on our work—did we do the headers right, for example—and see if there are recommendations. I'm supplementing with clients by finding obvious errors. I also use Google's pagespeed.web.dev tool to show them page speed scores and benchmark them against competitors—show them where pages load slowly and that their competitors are 20 points ahead. There's often a lot of work that can be done there, though it's not really in my expertise or in our SOWs, but we can highlight areas where they can improve.

**Kyle Gaudreau:** Kyle?

**Kyle Gaudreau:** I wouldn't put too much into all the different things it flags. There's always a bunch of stuff flagged. Generally, what I pay most attention to is the page speed metrics, because that has a tighter correlation with actual performance. If their page speed metrics are really bad, conversion rates won't be great. If page speed is bad, engagement will be low, and that affects SEO. The other things can be a root cause, but sometimes you see weird things where the overall score is wonky but the page speed metrics aren't that bad. In terms of First Contentful Paint, you want to be in that sub-2-second range, closer to 1 as much as possible.

**Kyle Gaudreau:** There's a clear correlation between slower page speed and declining conversion rates. You can think of that in the same way as less engagement—it's a bad signal for Google in terms of people actually interacting with content. You're always going to see something flagged, but that doesn't mean you need to focus on fixing everything. I'm less familiar with Ahrefs—maybe it's better. Have you run that comparison, Jakub?

**Jakub Rudnik:** SEMrush is useful, but it flags things that aren't always actually true. When Folsom sent me results, it was literally thousands of items flagged and most of them I don't care about at all. There's a lot of noise, and I can't synthesize that in five minutes to show them what to prioritize. Even this looked bad right away, but it did flag something that was a real error. A 5-second Largest Contentful Paint is bad. I agree with Kyle on the speed stuff—some of the other flags aren't best practices that are way better than using a WordPress plugin. They're not a big deal. Where I'd focus is on speed and benchmarking against competitors. Looking at review site competitors, they're all close to 100—the big SEO teams are taking this to the max. But other clients don't need to be at 100. It depends on who you're competing against and your content competition. I haven't done competitor benchmarking for Interwell yet. The current score is bad and they should fix it regardless, but if all competitors are at 50, we only need to get to 70 to win on the margins. I agree with the impact on conversions, and Google is rewarding speed for rankings too. So I would look at both the absolute speed and speed against your competitors to determine how much to prioritize.

**Kyle Gaudreau:** The two are kind of the same, right? If conversion rate goes down due to page speed, engagement also suffers. In terms of what almost always contributes to speed issues, it's usually some combination of JavaScript usage, tags adding JavaScript, and uncompressed images. There can be other things, but the vast majority of the time it's those. These tools will typically uncover it.

**Jakub Rudnik:** Often people are running 50 scripts they forgot were running—like Hotjar with nobody using it. Just about every company has some version of that.

**Jakub Rudnik:** Okay, can you give me a 15-second rundown of the strategy question?

**Andi Bailey:** Yeah, so DeepGram has a ton of content they've published. We originally built content for them, and now they want to dive into speech-to-text APIs—specifically the strategic areas they want to focus on. We went in with a content strategy focused on middle and bottom funnel, assuming they had a lot of top-of-funnel coverage already. Ada did the site audit, but they pushed back on our assumption and want us to create more content covering that top-of-funnel surface area. They want us to look at all their content and identify the gaps specifically around speech-to-text APIs, particularly targeting pharmacy and QSR (drive-thru) industries.

**Jakub Rudnik:** There are definitely ways to use SEMrush or Ahrefs for keyword gap analyses, but I don't always like them unless you're in a space with a lot of direct competitors who are also really good at content. If you're a CRM tool and there are 20 sites doing this, those keywords have a ton of relevance. But what I often find is people use keyword gap analysis to chase competitors, and competitors often do weird SEO things that aren't valuable. When I got hired at ActiveCampaign, I could tell the previous person had chased keyword gaps. There were these "best marketing quotes" articles that HubSpot had done first, so we did it too, but none of that was valuable.

**Andi Bailey:** Yeah, that's a path we could easily follow.

**Jakub Rudnik:** For DeepGram, I don't know that space as well. The best thing I do is poke around and find a SaaS company that's done a niche version of what they want to do. If they want speech-to-text, I'll do different queries and look at what comes up, then I'll examine that site's whole blog and look for patterns that could be useful. Zapier would be a terrible example because they're the most horizontal version. Sharing my screen and typing live gives me big-time anxiety.

**Andi Bailey:** It's not helpful. I'm trying to find their blog.

**Jakub Rudnik:** At Scribe, we did programmatic content like "How to Log Into X," and the biggest ones were "How to Log Into OnlyFans." That's an example of what I wouldn't do. So like, I'd look for their themes, and if they have specific software tool content, I'd search for those specific queries. I'm trying to figure out where to go next.

**Kyle Gaudreau:** Try going to topics real quick. SEMrush released this in the past 6 months or so. It's hit or miss depending on the website, but it sometimes helps find patterns. With 4,000+ pages, a few things might bubble up and directionally help you figure out what's important.

**Jakub Rudnik:** Yeah, that's a good tip. I don't use this but it can be useful.

**Andi Bailey:** That's what I'll tell Praveen, their CMO—this is the content strategy we're taking based on what people are asking for.

**Jakub Rudnik:** Speech synthesis is a good example.

**Jakub Rudnik:** I've been asking ChatGPT to suggest top-of-funnel keywords for clients, then searching those suggestions and looking for websites that rank for them. That tells me which keywords people want to rank for.

**Kyle Gaudreau:** This is a great example of a pain point we all experience in different ways and should address with automation. I've been hearing what people are doing with Ahrefs MCP server. The problem is you're manually going through tables trying to figure things out, or you ask ChatGPT for topics and keywords but it doesn't have real data. We should connect those worlds—here's the context, here's what we're hearing, here's the topic, and based on real data, let's generate insights. We'd probably still go to the platform for verification, but it would be a massive time savings.

**Andi Bailey:** Right, how we do topical research. Most clients are happy when we go through the list and say this is what you're covering, gap analysis of competitors, which Ada documented. But for DeepGram, they challenged us saying, we have a lot of content, but what portion hits this specific industry, and what are the gaps on top of funnel? That shifted us to needing to go deeper. I wasn't sure if there was a way to audit existing URLs for relevance to specific industries.

**Andi Bailey:** Pharmacy and QSR, which is drive-thrus.

**Kyle Gaudreau:** One thing you can do—it doesn't always work, but go to Google and use site:11labs.com pharmacy. You restrict to their domain and use keywords to find relevant content. It sometimes helps find patterns that aren't obvious from URLs and narrow in on the specific content.

**Andi Bailey:** It's very helpful to know there's no magic bullet. I spent a long time last night going through all this stuff, thinking there's got to be a better way, but it turns out there isn't.

**Jakub Rudnik:** I like that a lot, Kyle. When you're looking at a competitor, sometimes if they have good enterprise content or SEO, they've got a folder that's all mapped for you and you can just use it. But that's only 10% of our clients, especially in new emerging spaces. At Scribe, we took from seven different categories and I had to find topics from all sorts of places, sift through noise, and take 10% from each content strategy. Not super scalable, but it helps.

For HockeyStack, I did this for their stakeholder mapping feature. I just typed "stakeholder mapping software" to see if it existed. I found Simply Stakeholders as a competitor. When I ran it through SEMrush, it showed 85,000 search volume on the home page and 6,100 on a single page—so people are searching for this and there's traffic there. I saw 150 pages, no blog folder structure, but lots of options. This was the ideal situation. HockeyStack operates in seven or eight niches like this. This is a shorthand version of poking around, finding competitors, and validating whether they've executed well. That's not how it typically works, but it's the goal.

**Jakub Rudnik:** Cool.

**Andi Bailey:** I don't know.

**Andi Bailey:** This was really, really helpful.

**Jakub Rudnik:** Thank you.

**Jakub Rudnik:** I think I had one more thing I wanted to share, but no, not sure.

**Jakub Rudnik:** One thing I really liked doing, this is like, if you're, I feel like a bunch of people are focusing more like bottom funnel, like doing those software lists or alternatives or whatever the equivalent is.

**Jakub Rudnik:** One tip I've liked is running backlink analysis on competitors' sites, looking at anchor text to find synonyms people use to call your product. At ActiveCampaign, I found they had "email newsletter software" as an anchor. I wouldn't have thought to create that list, but there was search volume around it. That's not a G2 category, but there are other ways to analyze competitor backlinks too.

**Kyle Gaudreau:** Because sometimes what brands will do is like, they'll literally be like, go to their backlink vendors, and like, these are the 20 keywords I care about most.

**Kyle Gaudreau:** You'll need backlinks for this, and so that's a smart way of like, you'll see some noise, I'm sure, but that's a, yeah, that's a cool one.

**Jakub Rudnik:** I've never asked AI to analyze backlinks—it's been manual. But with the right prompts, it could be fairly scalable. Same with analyzing internal links and anchor text usage patterns. That can be useful but not always.

**Jakub Rudnik:** The worst assumption is that competitors in your space know what they're doing in content and SEO.

**Kyle Gaudreau:** People assume if competitors are doing it, we should too. But you should probably default to the opposite.

**Kyle Gaudreau:** The challenge is we rely so much on competitor comparison to understand our gaps. That's why making keyword research easier helps the team find more fruitful opportunities. There's got to be something with leveraging Ahrefs MCP. I have no idea about the cost or scalability in terms of tokens.

**Megan:** Have you played around with that much, Kyle?

**Kyle Gaudreau:** I haven't touched it at all. I'm relying on things I've heard people use it for, which has me thinking—how do we leverage it and what problems does it solve? I'd love to experiment.

**Megan:** Maybe we can ping Matthew about that. He told me how to get it set up but I got confused. I feel like there's got to be a way to set it up so it can grab data from SEMrush or Ahrefs.

**Andi Bailey:** Cool. Yeah, thank you guys. This was really helpful.

**Andi Bailey:** I'll talk to you all later. Bye, y'all.
