# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2025-09-26
time: 15:30 UTC
duration: 25 minutes
organizer: Carrie Chowske (GrowthX)
participants: Carrie Chowske (GrowthX), Kyle Gaudreau (GrowthX), Tanmay Sarkar (Airbyte)
fathom_recording_id: 90142282
fathom_url: https://fathom.video/calls/422536249
share_url: https://fathom.video/share/LRdFRJE1VW9gJPynFbtzihLdAUxW26do
source: fathom
enriched_on: 2026-03-03 12:45 UTC
speaker_note: Mario Moscatiello, Nithin M, and Jakub Rudnik were invited but did not speak during this call. Only Carrie Chowske, Kyle Gaudreau, and Tanmay Sarkar participated in the discussion.
</metadata>

---

## Summary

Following Airbyte's successful website migration, GrowthX and Airbyte aligned on an aggressive content push: publishing 24 pre-approved articles immediately and shifting focus to Enterprise Flex content over the next few months, with "hybrid deployment" as the core keyword to win AI visibility rankings (particularly ChatGPT). The team identified broken tables from the migration requiring manual fixes, discussed GA4 analytics showing strong performance in Security/Privacy/Compliance topics, and clarified the three core Airbyte 1.0 messaging pillars (Flex, speed, data activation) to thread through all future content.

---

## Context

Airbyte is a data integration platform that recently completed a major website migration and is launching version 1.0. GrowthX is their content marketing agency, responsible for strategy, drafting, and optimizing content for SEO performance. This was a weekly coordination meeting to align on the content pipeline post-launch, technical issues from the migration, and SEO strategy to capitalize on the timing of Airbyte's product launch with shifting search behavior. The team is acutely aware that Google's algorithm changes and the rise of AI-powered search (particularly ChatGPT) require new content positioning to remain visible when prospects ask AI tools about ETL solutions.

---

## Relevance

- **To GrowthX Delivery:** Website migrations create technical content debt — this meeting surfaced broken table embeds (from Atlas pipeline to Webflow HTML transition) that require manual fixes. The team needs process improvements for future migrations to avoid re-embedding tables. GA4 dashboard overhauls across all GrowthX clients now include content category clustering, enabling better attribution of traffic to content strategy initiatives.

- **To CheckThat / AEO:** This is a live case study in AI visibility strategy. Tanmay explicitly stated the goal: when users prompt ChatGPT to "find ETL tools that support hybrid deployment," Airbyte should appear in results. This requires continuous mention of "hybrid deployment" across on-page and off-page content — a core AEO tactic. The team is also evaluating whether to focus exclusively on Flex/hybrid messaging or maintain room for other product positioning.

- **To GrowthX Business Development:** Airbyte's website launch timing is favorable — post-migration, they can now scale content rapidly without technical blockers. Security, Privacy, and Compliance content is performing exceptionally well in GA4, signaling strong product-market fit and regulatory interest in Airbyte's target verticals. Reference potential high (successful launch = case study opportunity). Renewal health is strong — team coordination is smooth, execution velocity is improving.



---

## Overview

- Publishing 24 pre-approved articles immediately; shifting focus to Enterprise Flex content for next few months with "hybrid deployment" as core keyword
- Website migration successful but surfaced technical debt: broken table embeds requiring manual fixes; manual fixes required but process will improve going forward
- Google parameter changes limiting SEO tool data to 20 results instead of 100, affecting baseline comparisons; overall declining Google traffic across B2B clients creates opportunity for AI-visibility positioning
- Airbyte 1.0 messaging pillars for all content: Flex, speed, and data activation

---

## Key Topics

### Content Strategy and Production

- 24 pre-approved articles being published immediately
- Flex content drafts expected by end of day Friday or Monday morning
- Focus on Enterprise Flex content for the next few months
- "Hybrid deployment" keyword to be mentioned consistently across all content (on-page and off-page) to rank in AI-powered search results
- CTA framework updated to include hybrid deployment messaging and Airbyte 1.0 pillars: Flex, speed, data activation

### Website and Technical Updates

- Website migration complete and successful, enabling faster content scaling and template implementation
- Broken HTML tables from Atlas-to-Webflow pipeline transition require manual fixes; Airbyte team has list of affected articles
- PSEO (programmatic SEO) pipeline: Airbyte engineering working on new Webflow template and backend pipeline
- Looker Dashboard redesigned with content category clustering (Data Integration, Industry Solutions, Cloud & Hybrid Architecture, Security/Privacy/Compliance)

### Google Algorithm Changes and SEO Impact

- Google parameter changes removed ability to scrape 100 search results; now limited to 20 results per SEMrush, GSC, other tools
- Trend of declining Google traffic across all B2B clients; new website baseline reset provides clean measurement point
- ChatGPT and AI Mode now directly integrated into Google search bar, shifting how prospects discover solutions
- Opportunity to create deeper AI-related content (e.g., "How to train LLM on your own data") as general LLM training content is becoming stale

### Analytics and Reporting

- GA4 showing strong growth post-website migration across all content cohorts
- Security, Privacy, and Compliance topics performing particularly well, signaling product-market fit in regulated verticals
- HockeyStack provides more accurate web analytics data than PostDog (lower bot contamination)
- Data for SEO recommended as best tool for scraping SEO data without parameter restrictions

---

## Action Items

**Carrie Chowske (GrowthX)**
- Provide Flex content drafts to Tanmay (end of day Friday or early Monday)
- Update CTA framework to include hybrid deployment mentions
- Set up Airtable view access for Tanmay (content/keywords) — allow him to see and edit keywords without accessing full Airtable

**Tanmay Sarkar (Airbyte)**
- Check with Nitin M regarding list of articles with broken tables; share list with Carrie
- Review updated Looker Dashboard to verify content category classifications

**Kyle Gaudreau (GrowthX)**
- Investigate Google Search Console parameter issue limiting results scraping to 20 instead of 100
- Coordinate with Tanmay on deeper analytics strategy: assess what metrics Airbyte team wants to track in GA4, HockeyStack, and other tools

---

## Transcript

**Carrie Chowske:** Hello, hello, how are you?

**Kyle Gaudreau:** Oh, I'm on now.

**Carrie Chowske:** There you go, now I can hear you.

**Kyle Gaudreau:** Can you hear me now?

**Kyle Gaudreau:** I was asking how you were.

**Carrie Chowske:** Oh, fine. Well, I have these periodic bouts of insomnia, and I haven't slept in, like, two days, so kind of delirious.

**Kyle Gaudreau:** Oh, man, I'm sorry to hear that. I had a random bout of that many years ago. It lasted for a few months.

**Carrie Chowske:** Hey, Tanmay, how are you?

**Tanmay Sarkar:** Yeah, doing good. Finally, we leave from the launch. But yeah, so much work.

**Carrie Chowske:** Yeah, there are so many things on the website that need to be fixed. But it looks great, though. Really clean. Love it.

**Tanmay Sarkar:** Yeah, obviously cleaner than the old one.

**Carrie Chowske:** I have a few things to go over.

**Carrie Chowske:** We're currently publishing the content that we had stockpiled. We have about 24 articles that you've already approved. Some are from before the sprint, some from the last round. I'll have Flex content drafts to you either today or Monday. And then we'll focus on Enterprise Flex content for the next few months.

**Carrie Chowske:** One thing I wanted to touch on was the keywords you sent yesterday.

**Carrie Chowske:** Some of those we already had in there. We can hold the industry-specific topics for later and focus more on hybrid deployment for now. That'll help us as we work on other ones.

**Carrie Chowske:** I updated the CTA framework — I incorporated messaging from your blog post about Flex. It's not urgent, but it'll help with industry use case content. It has top-level talking points: when to say "talk to sales," when to say "try Enterprise Flex," and key messaging elements to mention in the body of articles. It'll help us build industry-specific CTAs as we go.

**Carrie Chowske:** I'm also going through the keyword list you sent so we can get stuff started for next week.

**Carrie Chowske:** I had some issues with the website. We had tables that broke — this is a known issue. When we use our automated pipeline to publish, it embeds directly from Atlas into Webflow. But if you make changes in Webflow, you have to re-embed the table because Webflow requires HTML. So we need to manually find and fix them. It'll take some time, but going forward, we'll handle tables differently.

**Tanmay Sarkar:** Yeah, I also saw this. I think Nitin might have a list already. I'll check with him and share it with you.

**Carrie Chowske:** Awesome. Just let me know if you need anything from us to work on that.

**Carrie Chowske:** On the PSEO pages, our engineering team is working on the pipeline and mocking up a new Webflow template. Now that we're able to publish again, we can save drafts in the background without publishing.

**Carrie Chowske:** We updated the Looker Dashboard with new content categories. We did a big overhaul across GrowthX, but the Airbyte one didn't get done, so I took care of it. We now have content clustering: Data Integration, Industry Solutions (anything mentioning a specific industry), Cloud & Hybrid Architecture, and Security/Privacy/Compliance. The last two are mainly reserved for Flex content.

**Tanmay Sarkar:** One thing — Flex is the name, but it's actually hybrid deployment. That's what I'm focused on. I've shared the keywords. Wherever you're writing articles, make sure we mention "hybrid deployment" because we want to rank for that. If someone asks ChatGPT which ETL tools support hybrid deployment, Airbyte should show up. We need to mention this on all our articles, on-page and off-page, continuously.

**Tanmay Sarkar:** Also, now that the website is ready, we need to scale content much faster. The website migration was a blocker. Now it's live, so we can move faster.

**Carrie Chowske:** Agree 100%. We're catching up with what we had in the pipeline and then we'll crank it out. And yes, I wanted to make sure we're mentioning hybrid deployment in the CTAs. For the next couple months at least, that should definitely be the focus. We can talk about whether to maintain room for other features or focus exclusively on Flex and hybrid deployment.

**Carrie Chowske:** If you pull up the Looker Dashboard, you'll see the non-branded clicks and impressions data. This is related to those Google issues Kyle was digging into.

**Kyle Gaudreau:** Yeah, I'm looking at it this afternoon. Basically, there was a parameter that allowed tools like GSC and SEMrush to scrape 100 results at once. Now they can't. They can do snapshots at 20, but I'm still connecting dots on what that means for baselines.

**Tanmay Sarkar:** It affected keyword ranking tracking in SEMrush too. For scraping SEO data, Data for SEO is the best tool. There's a trend of declining Google traffic across clients for several months, but it will stabilize. Google won't let search collapse — 75-80% of their revenue comes from search ads.

**Kyle Gaudreau:** Yeah, definitely not.

**Kyle Gaudreau:** But, yeah, I mean, yeah, clearly more shifts are going to happen.

**Kyle Gaudreau:** I was literally just, I've kind of, like, seen this, but I don't feel like my mind really, like, paid much attention to it.

**Kyle Gaudreau:** But, like, now AI mode is, like, literally something you get in the URL search bar directly, and you can click right into it.

**Kyle Gaudreau:** And, you know, these things are going to shift more and more for sure.

**Kyle Gaudreau:** Yeah.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** Let's see.

**Carrie Chowske:** Adapt their ad model to align with that, too.

**Kyle Gaudreau:** Yeah.

**Carrie Chowske:** they're going to figure out a way,

**Carrie Chowske:** They'll monetize it.

**Carrie Chowske:** Don't worry there.

**Carrie Chowske:** And that's just the thing, too, that, you know, we're seeing this across all of our clients, obviously.

**Carrie Chowske:** But another thing, too, that's impacting that also makes me kind of like not, I think the launch of your new site's really timed pretty well, right?

**Carrie Chowske:** Because it's coinciding with all of this stuff.

**Carrie Chowske:** So this baseline's going to, we're going to see kind of like some true, like if we're getting true growth, we're really definitely going to see that.

**Carrie Chowske:** So I think that's going to help, too, unless they do something to course correct that parameter and go back to having those impressions, then it'll be all messed up again.

**Kyle Gaudreau:** But we're going to just pretend.

**Kyle Gaudreau:** It's kind of an argument to be made either way on that, honestly.

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** But I hear you.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And part of it's just, you know, because we did those refreshes, traditionally you will regain some traffic when you refresh, but you tend to see more traffic come from net new content.

**Carrie Chowske:** So we weren't publishing some of that for a while.

**Carrie Chowske:** And then the pause entirely, like that's going to impact it some, too.

**Carrie Chowske:** So that's just something that.

**Carrie Chowske:** But just to keep in mind, but yeah, you definitely see this across both these charts here.

**Carrie Chowske:** So the one that's in purple and then this pretty rainbow little plotted graph here.

**Carrie Chowske:** What's interesting on this one and that I haven't seen with some of our other clients is those top two through 10, that purple there, that you get that huge spike in those, that mid-range there, and a steady kind of more increase along the lower number ones.

**Carrie Chowske:** And, but that night, it's nice to still be, to know you're still on that first page.

**Carrie Chowske:** I don't even think you get full, a full 10 links on the SERP anymore, but anyway, it's still how I think about it.

**Carrie Chowske:** But yeah, you didn't, I didn't see as quite a significant drop-off, probably just because you have so much more traffic in general, but that I didn't see as quite a significant drop-off as I did for some clients on those like 41 plus.

**Carrie Chowske:** But again, I, who, who's, who's scrolling that deep anymore?

**Carrie Chowske:** Like if, I don't know, I feel like I would refine my search if I'm not getting what I want, you know?

**Kyle Gaudreau:** Yeah.

**Kyle Gaudreau:** I mean, at that point, yeah, it's like.

**Kyle Gaudreau:** Like it will affect impressions, but it's like, it's not real impressions the way I think about it typically.

**Kyle Gaudreau:** It's like, you know, the stuff that can compound and turn into real impressions.

**Kyle Gaudreau:** So it's a helpful metric for sure.

**Kyle Gaudreau:** Yeah.

**Carrie Chowske:** I noticed something with the "How to train LLM on your own data" article from earlier this year. It had solid traffic all year, but it's starting to decline. That's an opportunity, especially with what you're doing and the AI readiness things mentioned in your Enterprise Flex blog post. I think the general conversation about using data with AI is getting stale, especially for technical audiences like data engineers. I pulled together some ideas to spark discussion: leveraging current trends, reinforcing differentiators, targeting specific industries, dealing with technical implementation challenges.

**Tanmay Sarkar:** Whenever you're talking about Airbyte, remember

**Tanmay Sarkar:** Whenever you are talking about airbytes, like you mentioned bullet points, right?

**Tanmay Sarkar:** Three bullet points should be one on flex, one on speed, and one on data activation.

**Tanmay Sarkar:** These are the three main updates in airbytes 1.0.

**Tanmay Sarkar:** So if you can mention this on all the articles going forward, I think we are good.

**Carrie Chowske:** Yeah, that's included in the CTA framework. I scraped your blog post about the new product, so it's a safe bet. Looking at GA4 data, we're seeing solid growth across all content cohorts post-launch. Data Pipeline is doing well, and Security/Privacy/Compliance is performing especially well because hybrid, cloud, and data sovereignty topics are directly related. That signals opportunity for Flex content to drive traffic.

**Carrie Chowske:** We categorize articles internally using regular expressions and cross-reference with GA4. It's pulling directly from your GA4. Let me know if anything looks weird — we manually update the classification formula. Kyle is more plugged in on tracking GA4 events and performance reporting. We have a good foundation to track whatever data you need.

**Kyle Gaudreau:** Do you guys use anything outside of GA4 for web analytics? Amplitude? PostDog?

**Tanmay Sarkar:** HockeyStack. I used PostDog but the data is insane — unrealistic bot traffic. HockeyStack is perfect. More accurate data.

**Kyle Gaudreau:** Yeah, GA filters out bots better than PostDog. But we should go through an exercise soon on what we want to dig into and what questions we should be asking.

**Tanmay Sarkar:** Yeah, sure. You guys have access to pull the data from Data for SEO.

**Carrie Chowske:** Jacob didn't make it today — he's moving. He'll update you on experimentation stuff after his PTO. I'll have Flex content for you by Monday morning at the latest, maybe even today.

**Carrie Chowske:** Now that the site is migrated, I can set up Airtable view access for you so you can see specific views without dealing with the entire Airtable. You can add keywords and see what we're working on from our end too.

**Carrie Chowske:** One last thing: the list of allies and partners you want mentioned in listicles. I think Mario was supposed to send that.

**Tanmay Sarkar:** Thank you. I'll review the content and check with Nitin for the list of broken articles. We'll share it with you.

**Carrie Chowske:** Sounds good. We'll get them updated as we find them.

**Kyle Gaudreau:** Congrats on the launch. I hope you have a restful weekend.

**Tanmay Sarkar:** We just started SEO work, so it's hectic.

**Carrie Chowske:** It's always hectic, especially on a site with this many pages. Glad we're past the manual page days. All right, everybody have a good weekend. We'll talk next week.

**Kyle Gaudreau:** Yes. See you.
