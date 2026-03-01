# Blaxel <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-22
time: 19:30 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants:
  - name: Paul Sinaï
    email: psinai@blaxel.ai
    affiliation: Blaxel
    role: Co-founder
  - name: Aida Knezevic
    email: aida@growthx.ai
    affiliation: GrowthX
    role: Content Strategist
  - name: Nicolas Lecomte
    email: nick@blaxel.ai
    affiliation: Blaxel
    role: Operations
  - name: William Leborgne
    email: william@growthx.ai
    affiliation: GrowthX
    role: Team Member
  - name: Kathy Lam
    email: kathy@growthx.ai
    affiliation: GrowthX
    role: Client Manager
    status: "CC (not present)"
fathom_recording_id: 116472622
fathom_url: https://fathom.video/calls/539596544
share_url: https://fathom.video/share/hyrECsGtmy4CDnXxEJsEYyazjoTyR8Qe
source: fathom
enriched_on: 2026-02-28 00:45 UTC
</metadata>

---

## Summary

GrowthX and Blaxel discussed content review bottlenecks, strategy adjustments to balance technical and educational content, and previewed GrowthX's AI visibility platform. Key decisions include building an Airtable-to-Slack automation for content notifications, rewriting the CodeSandbox Alternatives post to feature relevant sandboxing providers, and introducing higher-level content targeting CTOs and VPs of Engineering.

---

## Context

Blaxel is a sandboxing platform for AI agents that GrowthX is providing content marketing services for. As part of a broader content strategy to build topical authority in the AI/sandboxing space, the team is reviewing technical blog drafts, optimizing the content pipeline to reduce review overhead, and establishing clearer processes for internal notifications and feedback loops. GrowthX launched Check That, an AI visibility monitoring platform that tracks how companies appear in LLM responses across 100k+ prompts, and is giving Blaxel early access to monitor competitor positioning and inform content strategy.

---

## Relevance

**Content Strategy & SEO**
- Demonstrates tension between keyword difficulty (low friction to rank) and technical credibility (trust with developer audience)
- Shows how search intent analysis guides content positioning and why it sometimes conflicts with brand authority
- Illustrates practical approach to diversifying content mix for different persona levels

**Process Improvements**
- Workflow automation as a solution to missed notifications in distributed team communication
- Importance of Slack as central notification hub for remote operations

**AI Visibility & Competitive Intelligence**
- Practical application of AI visibility monitoring to content performance measurement
- Link between citation tracking and content strategy (citing third-party data as citable content multiplier)

---

## Overview

- **Process Improvement:** An Airtable-to-Slack automation will be built to notify Blaxel of content status changes, resolving a missed review notification.
- **Content Strategy:** The "CodeSandbox Alternatives" post will be rewritten to compare relevant sandboxing providers, ensuring technical credibility and avoiding a "weird" comparison that would undermine trust.
- **New Content Mix:** The strategy will add high-level, educational content for CTOs/VPs of Engineering to balance the current technical focus, which requires more intensive review.
- **AI Visibility Tool:** Blaxel will gain early access to GrowthX's "Check That" platform in February to monitor AI search visibility and competitor performance.

---

## Key Topics

### Content Review Process

  - Blaxel missed the notification for 5 new blog drafts in Airtable.
      - **Solution:** GrowthX will build an Airtable-to-Slack automation to notify Blaxel of all content status changes.
  - **Status Update:**
      - "Browser Sandboxing" post is approved.
      - "Serverless Computing Use Case" post is under review.

### "CodeSandbox Alternatives" Post

  - **Issue:** The draft compares CodeSandbox to irrelevant tools (e.g., Replit), creating a "weird" comparison that would undermine Blaxel's technical credibility.
  - **Root Cause:** The content was based on the keyword's search intent (SERP), which focused on browser-based dev environments, not sandboxing providers.
  - **Decision:** The post will be rewritten to compare relevant sandboxing providers.
      - **Rationale:** This maintains technical credibility while leveraging a high-intent, low-difficulty keyword.

### Content Strategy & Mix

  - **Problem:** The current focus on highly technical articles requires intensive review from Blaxel's developers, slowing the content pipeline.
  - **Solution:** Add high-level, educational content for CTOs and VPs of Engineering.
      - **Goal:** Build topical authority and provide shareable content for leadership.
      - **Example Topic:** The role of sandboxing for AI agents, referencing the recent Entropic paper.
  - **Content Enhancement:** Add unique data (stats, case studies) to make content more citable and stand out.
      - **Action:** Blaxel will collect specific metrics (e.g., cost reduction, speed improvement) for its internal case studies.

### "Check That" Platform Walkthrough

  - GrowthX demoed its AI visibility monitoring platform, "Check That."
  - **Key Features:**
      - **Pre-indexed Data:** Tracks 1.5k+ companies and 100k+ prompts, providing historical data from day one.
      - **Competitive Analysis:** Shows where competitors appear and who is cited for specific prompts.
      - **Citation Share:** Tracks how often Blaxel's site is linked in AI responses.
      - **Source Analysis:** Identifies top-cited pages to inform content strategy.
  - **Timeline:** Blaxel will receive early access in February.

---

## Action Items

**Unassigned (GrowthX)**
- Set up Airtable→Slack status automation for Blaxel content (EOW)

**Aida Knezevic (GrowthX)**
- Rewrite 'Top 6 CodeSandbox Alternatives' w/ Natalie; use Blaxel-relevant competitors
- Send Slack topic suggestions to Paul & Nico; then conduct higher-level keyword research
- Compile 3rd-party stats artifact for Blaxel content
- Publish approved blog post (4th total)
- Follow up w/ team re: Check That early access for Blaxel; notify Paul & Nico when ready

**Nicolas Lecomte (Blaxel)**
- Create case-study intake/follow-up form for Vikram; request metrics during interviews

---

## Transcript
**Paul Sinaï:** Hi, Aida.

**Aida Knezevic:** Hi, paul.

**Paul Sinaï:** How are you?

**Paul Sinaï:** I'm doing great.

**Aida Knezevic:** What about you?

**Aida Knezevic:** I'm good.

**Aida Knezevic:** Are you based in Europe?

**Paul Sinaï:** No, I'm based in San Francisco.

**Aida Knezevic:** Ah, okay, okay.

**Aida Knezevic:** Got it.

**Aida Knezevic:** I thought...

**Paul Sinaï:** Nico is based in New York.

**Aida Knezevic:** Ah, okay, okay.

**Aida Knezevic:** Got it.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** I think when we met for the first time, I think I kind of understood that you were based in Europe.

**Aida Knezevic:** So I thought, okay, maybe sometimes if I'm just going to be on the call, maybe we could do it earlier.

**Paul Sinaï:** Earlier, yes, for you.

**Paul Sinaï:** No, unfortunately, I'm for me.

**Paul Sinaï:** I can...

**Paul Sinaï:** Try, I can see if we can move it just like one hour before, maybe it would be easier for you.

**Aida Knezevic:** No, honestly, I'm good because I actually have another meeting right after this.

**Paul Sinaï:** So I have to, anyway, have to later regardless.

**Paul Sinaï:** are starting later in the morning?

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** Some days I, if I have a meeting late, then I start late.

**Aida Knezevic:** And if I don't have a meeting like super late, then I start earlier.

**Aida Knezevic:** So I tend to work, like my most productive periods of time are actually in the mornings.

**Aida Knezevic:** So if I need to work on something important, I'll log on in the AM.

**Paul Sinaï:** Okay, makes sense, makes sense.

**Paul Sinaï:** I think we can start just to, because Nico is, I know he's inside, in back-to-back meetings, so probably he's running late, so I guess we can start.

**Aida Knezevic:** Okay, okay, got it, cool.

**Aida Knezevic:** All right, so Kathy's out today and tomorrow, but I have a good idea.

**Aida Knezevic:** Of the progress that we've made so far, I think the one thing that I wanted to ask is the reviews of last week's content.

**Aida Knezevic:** So these are the five blogs that are currently with you for review.

**Aida Knezevic:** I was wondering if you had a chance to just take a look at these.

**Paul Sinaï:** Yeah, so I started yesterday.

**Paul Sinaï:** I didn't finish.

**Paul Sinaï:** And it's one thing that we wanted to mention.

**Paul Sinaï:** I think we didn't receive the notification on Slack.

**Paul Sinaï:** So we missed this.

**Paul Sinaï:** It's just because I'm connecting to Airtable yesterday.

**Paul Sinaï:** And I saw all the five articles.

**Paul Sinaï:** Oh, shoot.

**Paul Sinaï:** I completely missed that.

**Paul Sinaï:** But I checked on the Slack.

**Paul Sinaï:** I couldn't find the notification.

**Paul Sinaï:** So yeah, if you don't mind just sending a notification on Slack.

**Paul Sinaï:** Like, hey, guys, there is a new set of...

**Paul Sinaï:** Yes.

**Paul Sinaï:** Of a post.

**Paul Sinaï:** Now I'm used to it, so I will go on content on the art table, but it's easier for us.

**Aida Knezevic:** Yeah, yeah, totally.

**Aida Knezevic:** No, we'll do that.

**Aida Knezevic:** I think it's very...

**Aida Knezevic:** We typically like to send an update at the end of the week when the articles are ready, but I think it might have gotten lost somewhere.

**Aida Knezevic:** So we'll do that moving forward.

**Aida Knezevic:** Okay, so that's good.

**Aida Knezevic:** This one is currently...

**Aida Knezevic:** So the one about browser sandboxing, this one is in revision.

**Paul Sinaï:** I think it's almost ready.

**Paul Sinaï:** I just asked one last question on this.

**Paul Sinaï:** It was the comment of Matisse.

**Paul Sinaï:** Okay.

**Paul Sinaï:** I just missed on the...

**Paul Sinaï:** You were saying CNew sections, but I missed the Brave Search.

**Paul Sinaï:** Oh, yeah, but this wasn't there yesterday, right?

**Aida Knezevic:** Yeah, yeah, this is new.

**Paul Sinaï:** Okay, okay.

**Paul Sinaï:** Okay, I was thinking like, I didn't see it.

**Paul Sinaï:** So maybe it's more than, okay.

**Paul Sinaï:** So if it's mentioned, I think it's good.

**Paul Sinaï:** It's good to go.

**Paul Sinaï:** Otherwise, it wasn't the last one.

**Aida Knezevic:** Okay, perfect.

**Paul Sinaï:** Let me just.

**Nicolas Lecomte:** I'm sorry, I just arrived.

**Nicolas Lecomte:** I'm sorry, I was late.

**Nicolas Lecomte:** The five other are ready to review on our end?

**Aida Knezevic:** Five, so, yeah.

**Paul Sinaï:** Okay.

**Paul Sinaï:** Yeah, was just saying that we missed the notification on Slack.

**Paul Sinaï:** So just we added to the process that each time the status change, I think actually it would be a great automation for your engine.

**Paul Sinaï:** Automation, could say, yeah.

**Paul Sinaï:** Each time the status change on L table, having this send a notification to the Slack channel would be great.

**Nicolas Lecomte:** That would be super helpful.

**Paul Sinaï:** Yeah, for sure.

**Paul Sinaï:** Because we could even know, oh, this post has been published, you know, just for us to know.

**Nicolas Lecomte:** And we use Slack for all the comms, even alerts and everything on our end.

**Nicolas Lecomte:** that would be really, Okay, great.

**Aida Knezevic:** Slack is really our notification center.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** That's great.

**Paul Sinaï:** Sometimes we work with clients who use Microsoft Teams.

**Aida Knezevic:** Oh, my God.

**Aida Knezevic:** And that's always so bad.

**Nicolas Lecomte:** Why you do that?

**Aida Knezevic:** Yeah, I don't.

**Aida Knezevic:** And it's always a nightmare when we try to share, like if I try to share a Google Drive or a Looker dashboard, they can't access it with a Teams email.

**Paul Sinaï:** So yeah, it's a nightmare.

**Paul Sinaï:** I know with our previous company, we were using Teams and Office 365.

**Paul Sinaï:** And it was like, each time someone wanted to share something on Google, it was like a nightmare.

**Aida Knezevic:** Oh, yeah.

**Aida Knezevic:** Wow.

**Aida Knezevic:** Yeah, that sucks.

**Aida Knezevic:** All right.

**Aida Knezevic:** I'll let Natalie know to set up the Slack automation.

**Aida Knezevic:** So we should have that ready for like probably.

**Paul Sinaï:** By the end of the week, so that we can start using it.

**Paul Sinaï:** Awesome.

**Paul Sinaï:** Yeah.

**Paul Sinaï:** So on the review, there's one I'm working on. Let me go back to it.

**Paul Sinaï:** Okay, so I started reading the "Top 6 CodeSandbox Alternatives" and I'm going to give you feedback on this one.

**Paul Sinaï:** And the other one I'm still working on is the Serverless Computing Use Case—a practical guide for AI and startups.

**Paul Sinaï:** But first, let me give you feedback on number four, the "Top 6 CodeSandbox Alternatives."

**Paul Sinaï:** It's just that I don't know if it's a hallucination from the model, but it's completely off...

**Paul Sinaï:** CodeSandbox is a sandboxing provider like us, and it compares it to Replit, which isn't really a sandboxing provider.

**Paul Sinaï:** They use sandboxing, but it's not a sandboxing provider.

**Paul Sinaï:** I was super surprised by the companies listed. I'd say almost all of them are irrelevant if you compare CodeSandbox to them.

**Paul Sinaï:** Or maybe I'm missing something, but for me, it's weird.

**Aida Knezevic:** Yeah, it was a different...

**Aida Knezevic:** So let me just find...

**Aida Knezevic:** I remember there was a...

**Aida Knezevic:** Yeah, so the search intent for that keyword was...

**Aida Knezevic:** So the search intent means what Google thinks the person searching for this keyword wants to see.

**Aida Knezevic:** So the articles on the first page and on the second...

**Aida Knezevic:** They typically give us a good overview of what kind of content we have to create in order to rank for that keyword.

**Aida Knezevic:** So when we were doing the research, we found that the code sandbox alternatives keywords, like the SERP was covering alternatives to code sandbox specifically for human building apps in browser-based dev environments.

**Aida Knezevic:** So people weren't looking for alternatives to code sandboxes, sandboxing feature.

**Paul Sinaï:** Ah, okay.

**Aida Knezevic:** So, yeah.

**Aida Knezevic:** Okay, with this context, it's clear.

**Paul Sinaï:** Yeah, so I think I don't think it's relevant for us today.

**Paul Sinaï:** It's going to feel weird.

**Paul Sinaï:** I understand the SEO reasons, but we cannot publish this.

**Paul Sinaï:** It would be super weird if someone read it and thought, "What is Blaxel doing comparing itself to Replit?"

**Aida Knezevic:** Yeah, let me explain...

**Paul Sinaï:** It's just comparing apples to oranges.

**Nicolas Lecomte:** It's also, and I guess on top of this, because we don't appear on the list, so we appear at the end, but in like a follow-up section, but I don't know.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** I think this was kind of a more a play where we could potentially be targeting your audience, but through something that isn't as close to you.

**Aida Knezevic:** However, this is what I'm seeing.

**Aida Knezevic:** CodeSandbox Alternatives, very like this volume is very normal for an alternative's keywords.

**Aida Knezevic:** So it's very like these are very bottom of the funnel, like very high intent in terms of people looking for solutions.

**Aida Knezevic:** So in this case, I think we can rewrite it so that it matches the products that, you know, you want to be compared.

**Aida Knezevic:** And then I think we will still be able to rank for it because I don't think, yeah, the keyword difficulty is very easy.

**Aida Knezevic:** So I think we can also like do rewrite it, provide the companies that you want to provide, and then we can publish it.

**Paul Sinaï:** That makes sense.

**Paul Sinaï:** Yeah, for us it's interesting because we've switched several customers from CodeSandbox to us.

**Paul Sinaï:** So being referenced in these keywords is relevant for us, but we need the content to be relevant and credible to our technical audience.

**Paul Sinaï:** Otherwise, we'll win clicks but lose conversions because of the trust issue.

**Aida Knezevic:** Okay, okay, got it.

**Aida Knezevic:** No, that's totally fair.

**Aida Knezevic:** I will let Natalie know that this one should just be rewritten.

**Aida Knezevic:** I think it's, you know, the risk.

**Aida Knezevic:** I think will pay off here, because it's not very difficult.

**Aida Knezevic:** the first one that's ranking is Reddit.

**Aida Knezevic:** So this is typically a sign that there is an opportunity to do something different.

**Aida Knezevic:** Because I think whenever you see Reddit pop up, it means that the other websites might not actually be that helpful.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Any other feedback on the other drafts?

**Paul Sinaï:** Yeah, I just started reviewing number two—the one with the highest priority.

**Paul Sinaï:** I hope to finish that today, and maybe a couple of others.

**Paul Sinaï:** But yeah, we still need to organize ourselves a bit differently.

**Paul Sinaï:** Honestly, another issue is that maybe we need to add more higher-level content to the mix.

**Nicolas Lecomte:** Yeah, because a technical article requires more review from us and from the developers, so it's additional review steps versus higher-level content, which is usually more straightforward.

**Aida Knezevic:** Okay.

**Nicolas Lecomte:** So.

**Aida Knezevic:** Yeah, what I think we can do is for next week, we will, I will send over Slack, just some suggestions, not just for next week, but like for probably like the next few weeks.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** And we want to build a backlog and then I think we will also do additional keyword research to find additional like higher level topics.

**Aida Knezevic:** Yeah.

**Paul Sinaï:** To build targeting toward CTOs and VPs of Engineering.

**Paul Sinaï:** They tend to look for content where they can learn something and share with their team. For example, it could be interesting to discuss why sandboxing is important for AI agents, especially with the recent Entropic paper mentioning sandbox as the next approach for agents. We could publish more educational and awareness content around this market, especially for engineering leadership at larger companies that are our customers.

**Aida Knezevic:** Mm-hmm.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Got it.

**Aida Knezevic:** No, I'll put that on our to-do list then.

**Aida Knezevic:** That's helpful. When we do SEO content with other clients, we always add at least one unique element—like a case study example or statistic. This is easier with bigger companies that already have research reports and their own data. But for you, we can also find third-party reports from non-competitor companies and create an artifact of useful data points to incorporate into the content and make it stand out more. Content with statistics and unique case studies gets cited more, so that's something we can dig into.

**Paul Sinaï:** We try to do this internally with our customers. We have published case studies—about one a week. I've also done case studies with Cisco and other large companies, and we always used intake forms to capture actual numbers and improvement metrics. People love those metrics.

**Paul Sinaï:** You could ask Vikram to gather these numbers during interviews, or use a follow-up form. The key is getting real numbers, not guesstimates—like cost reductions or speed improvements for the file explorer.

**Nicolas Lecomte:** Definitely. A follow-up form would help ensure we capture those metrics.

**Aida Knezevic:** Sounds good. So to recap: you're reviewing last week's content, we'll set up the Airtable-to-Slack automation, and we have five new drafts coming your way this week. We'll also follow up with topic suggestions and additional keyword research. For approved blogs, we have three published so far, and we'll try to publish the one that just got approved tomorrow, bringing the total to four.

**Aida Knezevic:** Also, I wanted to give you a walkthrough of Check That. I don't think you've covered this with Kathy yet, right?

**Paul Sinaï:** Nope.

**Aida Knezevic:** All right, let me walk you through it.

**Aida Knezevic:** Check That is our AI visibility monitoring platform. Unlike tools like Scrunch or Profound where you upload your own prompts and start tracking from day one, Check That is a shared index of AI visibility. We've already added over 1,500 companies and are tracking over 100,000 prompts across different industries. So you can immediately see historical data on your competitors—going back 90 days for evaluation-stage prompts that show what buyers are asking when evaluating solutions.

**Paul Sinaï:** So this is a tool you developed, not a search engine ranking tool?

**Aida Knezevic:** Right. You'll have access in the next couple of weeks. You're on the priority list for early access, so you should be able to log in and explore the prompts soon. The dashboard is fairly straightforward.

**Aida Knezevic:** You can see competitive presence for the prompts we're tracking, citation share (how often your site appears in AI responses), and your ranking sentiment. You can also switch between viewing your direct competitors and the broader MLOps category to see industry giants. We've already added competitor suggestions based on your business, and we map prompts to target keywords so you can measure article impact after publishing.

**Paul Sinaï:** That makes sense.

**Nicolas Lecomte:** It's better than before.

**Aida Knezevic:** From a content strategy perspective, we can see which pages are consistently cited in prompt responses—like a Datacamp post appearing across different responses. You can review those and decide if there's a similar approach that makes sense for Blaxel. This helps inform content strategy and identify citation opportunities.

**Paul Sinaï:** Makes sense.

**Aida Knezevic:** We're aiming for February, and we'll keep you in the loop.

**Paul Sinaï:** That's exciting. In terms of content strategy, what adjustments do you see for the next couple of weeks?

**Aida Knezevic:** I'll follow up with topic recommendations in Slack. For this sprint, we want a mix of competitive keywords—alternatives and comparisons—because they rank quickly and have strong AI visibility impact. We also want educational, non-technical content to build topical authority without bogging you down in reviews. You can create foundational content that brings traffic while competitive content drives leads. Two birds with one stone.

**Paul Sinaï:** Sounds good. Thank you, Aida. Super helpful. Let's get back to work.

**Aida Knezevic:** Let's review those posts. Thanks.

**Paul Sinaï:** Nico, can I call you back?

**Nicolas Lecomte:** Yeah, I have 30 minutes. Thanks.
