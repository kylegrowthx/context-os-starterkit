# GrowthX Feedback Session (Jason Beltran)

<metadata>
date: 2025-10-24
time: 17:01 UTC
duration: 33 minutes
organizer: Andi Bailey
participants: Andi Bailey (GrowthX), Jason Beltran (Sunbit)
fathom_recording_id: 96670129
fathom_url: https://fathom.video/calls/451813028
share_url: https://fathom.video/share/q5kzs2m6SZsj9AeignYvRpJvcPDgygAE
source: fathom
enriched_on: 2026-03-02 10:15 UTC
</metadata>

---

## Summary

Andi and Jason closed critical gaps in Sunbit's reporting infrastructure, revealing an existing Scrunch dashboard for tracking LLM performance that had been missed during account manager transitions. They customized it live by adding Cherry Technologies as a competitor, "patient financing" as a topic, and creating a dental office manager persona. Webhooks for automated blog publishing are now live, unblocking a large content backlog. The team aligned on the new Sunbit.ai launch (mid-November) targeting investors, analysts, and tech talent with B2B AI/ML finance content.

---

## Context

Sunbit is a fintech company specializing in patient financing solutions. Jason Beltran manages content strategy; Andi Bailey is their GrowthX account manager. The relationship has been strained by multiple account manager transitions over the past year, which caused reporting visibility gaps — Jason didn't know Scrunch existed despite having a configured dashboard. Organic traffic is up 64% year-over-year, and content production velocity is strong (scoring 9/10). This feedback session surfaced easy fixes: dashboard access, Scrunch customization, and planning the new Sunbit.ai B2B property.

---

## Relevance

**To GrowthX Delivery:**
- Account transitions are creating knowledge loss. Sunbit's Scrunch dashboard existed but wasn't communicated during handoffs — process fix needed for future clients.
- Webhook automation working well; this pattern should be documented for scalability.
- JSON schema optimization for LLM discoverability is live — consider adding this to delivery playbook for B2B SaaS clients.
- Client is actively removing em dashes and Oxford commas to avoid AI-generated-content signals — actionable insight for content optimization.

**To CheckThat / AEO:**
- Scrunch customization with new personas (Dental Office Manager) and competitors (Cherry Technologies) is deepening CheckThat integration.
- Patient financing is a high-priority topic; LLM mentions are tracked at 2% (vs. Care Credit at top).
- Client is intentionally writing B2B content for LLM consumption, not human readers — validates CheckThat's core thesis.
- Sunbit experimenting with Reddit seeding; Andi shared GrowthX's strategy of starting within client channel, then engaging broader communities.

**To GrowthX Business Development:**
- Relationship score: 7/10 (down from potential 9-10 due to account transitions). Fix account stability to improve NPS.
- Velocity 9/10, Content Quality 9/10, Performance 9/10 (64% YoY organic growth). Strong renewal/expansion signals.
- New Sunbit.ai project is expansion opportunity — B2B content for investor/analyst/talent audiences.
- Tech.growthx.ai referenced as model for Sunbit.ai — good opportunity to showcase GrowthX's own AI-generated content playbook.

---

## Overview

- **Reporting Gap Closed:** Sunbit was unaware of their existing Scrunch dashboard for tracking LLM performance. Andi provided immediate access and began customizing it with Sunbit's input.
- **Publishing Unblocked:** Webhooks are now live, enabling automated blog publishing. This will clear a large content backlog and increase publishing velocity.
- **New Project Scope:** Sunbit is launching `Sunbit.ai` in mid-November. This new site requires content for a B2B audience (investors, analysts, tech talent), distinct from the consumer/merchant focus of `Sunbit.com`.
- **Strong Performance:** Organic traffic is up 64% this year. Content volume and quality are high, with the main friction point being account management transitions.

---

## Key Topics

### Problem: Reporting & Visibility Gaps

  - Sunbit's primary need was a reporting dashboard to track performance beyond GA4, specifically for:
      - Search index metrics (e.g., Surfer SEO data, keyword density).
      - LLM pickup (mentions, citations).
  - This gap was attributed to multiple account manager transitions.

### Solution: Scrunch Dashboard & Customization

  - Andi revealed Sunbit's existing Scrunch dashboard, which tracks LLM performance by pinging models with prompts.
  - Live customization was done to align the dashboard with Sunbit's strategy:
      - **Competitor Added:** `Cherry Technologies` (`withcherry.com`).
      - **Topic Added:** `patient financing`.
      - **Persona Created:** `Dental Office Manager` (key decision-maker for financing).
      - **Prompts Generated:** New LLM prompts were created based on the new persona.

### Context: Content Strategy & Publishing

  - **Automated Publishing:** Webhooks are now live, enabling automated blog posting. This will clear a large content backlog and increase publishing velocity.
  - **LLM Optimization:**
      - **Goal:** Write B2B content primarily for LLM consumption, not human readers.
      - **Tactic:** Adding JSON schema to WordPress page headers to improve LLM discoverability.
      - **Tactic:** Removing em dashes and Oxford commas to avoid AI-generated content signals.
  - **Social Media:**
      - The automated social pipeline is paused while Sunbit defines its video-heavy social strategy.
      - Reddit is a potential channel, as LLMs reference it for "human conversation." Sunbit is monitoring existing mentions.

### New Project: `Sunbit.ai`

  - **Launch:** Mid-November 2025.
  - **Audience:** Investors, analysts, media, tech talent (not consumers/merchants).
  - **Content Focus:** Machine learning and AI in finance.
  - **Tech Stack:** WordPress, mirroring the `Sunbit.com` setup.
  - **Reference:** Andi suggested `tech.growthx.ai` as a model for this type of B2B content.

### Performance & Relationship Feedback

  - **Relationship:** 7/10 (due to account manager transitions).
  - **Velocity:** 9/10 (high volume of content).
  - **Content Quality:** 9/10 (excellent, with minor style tweaks requested).
  - **Performance:** 9/10 (organic traffic up 64% this year).

---

## Action Items

**Andi Bailey (GrowthX)**
- Set up Looker dashboard for Jason; share access
- Update Scrunch for Jason: add Cherry Technologies, "patient financing" topic, Dental Office Manager persona; remove pet care and eye care topics; coordinate with Edisham to begin weekly reviews
- Email Jason examples of non-branded AI/ML content for Sunbit.ai launch

---

## Transcript

**Andi Bailey:** How are you?

**Jason Beltran:** Doing good.

**Andi Bailey:** How are you guys doing?

**Jason Beltran:** Good.

**Andi Bailey:** It's been a little while.

**Jason Beltran:** How's everything going?

**Andi Bailey:** Everything's going good.

**Jason Beltran:** How about yourself?

**Andi Bailey:** Good. Yeah. And another changing of the season, right?

**Jason Beltran:** Right, I think we're talking like right at the beginning of summer.

**Andi Bailey:** Yep, yeah. So I mean, I think we've got a lot of exciting stuff happening on our end. We've finalized the transition to the platform that Marcel showed you when we first talked.

**Jason Beltran:** Yep.

**Andi Bailey:** And yeah, I think we're still refining. We're working on like more agentic pieces to the product. So agentic workflows are rolling out right now. Some really cool stuff going on. And Marcel's been doing a lot of webinars and videos. Have you seen any of those?

**Jason Beltran:** I have noticed that he's doing them, but I haven't seen any of those.

**Andi Bailey:** Well, I think they're all available. But hopefully we're doing that work for you.

**Jason Beltran:** Yeah.

**Andi Bailey:** So how are things on your end?

**Jason Beltran:** Overall, things are going good. The volume of content is high, the quality of content is good. Just yesterday, we finally got the webhooks in a good place where we can start automating more of the blog posting. We have a huge backlog of content that we just haven't been able to post because we were waiting on that automation. So now that it's in place, we're going to do a little bit more testing, but I think it's going to go a long way in helping us get more of this content up faster. I'm really excited about that.

And then Edisham has been amazing. He's a really good partner, very fast and on top of it. Really enjoyed working with him.

I would say the only place where I'm still looking for improvement is reporting. The platform you speak of — I haven't logged into it. We manage everything through Airtable, which is fine. But we're lacking in reporting. Someone does a good job with manual reporting for us, but it would be nice to have a dashboard. We don't have one yet. I know they started putting together a Looker dashboard, but it didn't work out. Nothing's really come up since then. It would be nice to jump back into that.

What I need more insight into is site rating and rankings, keyword density — the Surfer SEO side of things. I want to understand not only the traction we're getting through GA4, but how we're looking from a search index perspective.

And then lastly, the new element for reporting is LLMs — how are LLMs picking up our content? I don't know if that's something you all would provide, but I think that would be of interest. A lot of our B2B content now is focused on influencing LLMs.

**Andi Bailey:** That's surprising to me because we do have some of that reporting available. I'll show you Scrunch because you guys have a Scrunch dashboard set up through us.

**Jason Beltran:** I've never heard of that.

**Andi Bailey:** Well, let me show you. I want to dive a little bit more into it, but let me just show you what we have. Scrunch basically pings all the LLMs with different prompts — either generated by Scrunch or by us — and tracks them on a regular basis. It can track your performance in terms of mentions and citations, and how you're standing up against your competitors. This can all be further refined.

We're working with Scrunch now, and we're planning to have this in a dashboard that you can click around and access shortly. We can start tracking it, and you can start looking at it today.

These are the personas. We can pull in from your personas as well. You've got flexible payment options, merchant locations across the U.S. And then looking at competitive brands — we can add or edit these.

**Jason Beltran:** And I think before we go further, I do want to give some general feedback. I'm pretty relaxed about things, but we have had several transitions on account management. I get it — you guys are early days and that happens. It's your first year in business, so I totally understand. But because we've had so many people work on our account in such a short time, some things got overlooked. Like this — I didn't even know Scrunch existed.

There's a lot that I'd like to do with this.

**Andi Bailey:** That's good. These are easy fixes at least.

**Andi Bailey:** These are the key topics and keywords. It'll generate prompts. For example, it might ask "What are the payment options for dental work?" and see who else is showing up. You're showing up 2% of the time right now, and Care Credit is showing up most often for this one.

There's a lot of work we can do here, so it's good we're talking. I can talk to Edisham about getting you in here and starting weekly reviews.

**Jason Beltran:** Yes, I definitely want to get in. There's a lot of things I'm already seeing that I'm excited about — like adding a new competitor to the mix and some other prompts that are more on the B2B side.

**Andi Bailey:** Cool. Can I have Edisham take a stab at this to start? Who would you want to add as competitors?

**Jason Beltran:** Let's do it right now. One of them is Cherry Technologies, withcherry.com.

**Andi Bailey:** All right. So now it will look for whether Cherry shows up in any of those questions too. And then are there topics you'd want to add?

**Jason Beltran:** Patient financing is a good one.

**Andi Bailey:** Cool.

**Jason Beltran:** There are some topics in here we can remove. Pet care management — we don't really care about. Eye care either. We're really big in dental and auto.

**Andi Bailey:** Okay. We can also create a persona.

**Jason Beltran:** Can you create one for a dental office manager? A dental office manager manages a dental practice and is in charge of staffing, P&L, and technology for the practice. They're the main decision maker on offering patient financing options to their customers — they're in charge of solutions for patient financing. They're often a decision maker within the practice or an influencer.

**Andi Bailey:** There we go. Okay.

**Jason Beltran:** That's pretty good. And countries is US.

**Andi Bailey:** Yeah, okay. So we can have it generate more prompts for you. We can use "generate prompts with AI" to create some for the dental office manager.

**Jason Beltran:** One of them that we've been monitoring is versus questions — like Care Credit versus Sunbit, or Cherry versus Sunbit. Have we done that kind of content for you yet?

**Andi Bailey:** Have you created that on your own?

**Jason Beltran:** Yeah, we've created some of that.

**Andi Bailey:** What are some patient financing options for dental treatments that don't require a hard credit check? Recommend a payment solution that allows dental patients to split their bills into monthly installments. Help dental offices offer flexible payment plans. Companies providing quick approval financing for dental expenses. Best providers for patient financing that also offer mobile app management.

**Jason Beltran:** I think these are all good.

**Andi Bailey:** So we'll add these prompts. It will create versions or try different variations. It'll start to track Cherry going forward too.

**Jason Beltran:** This is great.

**Andi Bailey:** Well, I'm glad we solved one thing today.

**Jason Beltran:** Yeah, that's the big one. A couple of days ago, we got the automation in place. Now we've done it. We have a few tests that have gone through — everything's looking really good. Edisham sent over a lot of tests this morning, which is great. The automation seems to be working. Next steps are really just getting all these published and then getting the analytics in place.

**Andi Bailey:** Yeah. And as we start to do this, since we're now paying attention to tracking AI, we can tweak some pieces and recommend things to add to every article — like FAQs at the bottom or a TLDR at the top.

**Jason Beltran:** We already have a structure. We start with a summary, then we have key points.

**Andi Bailey:** Perfect.

**Jason Beltran:** Which is really nice. I think we do a pretty good job. The only thing we're adding to the site is JSON schema to the header of each page. That way, the LLMs are a little bit more interested in our content. That's something we're adding soon. Once we add that, we'll figure out how to propagate it across the overall content. I haven't talked to Edisham about that yet. I'm waiting for it to be added to the website, then we'll send it through the webhook. Once we have that, the entire structure of our articles is going to be really good. That's the only piece I can think of that's not completely LLM-friendly.

**Andi Bailey:** What publisher are you guys using?

**Jason Beltran:** WordPress.

**Andi Bailey:** Got it. Some of the bigger CMSs are offering the ability to upload a TXT file that helps AI search the site better, especially for top pages. This JSON schema sounds like the WordPress alternative.

**Jason Beltran:** Yeah, we have a website agency working on this. We want to add JSON schema to every page — it'll be in the header. I haven't heard of the TXT file approach, but that sounds interesting too.

**Andi Bailey:** It's still very experimental. Webflow is adding it since they're headless. So it's all in flux.

**Jason Beltran:** We actually had a competitor who was influencing Google's Advanced Search. It was Cherry versus Sunbit — they published a bunch of materials, a lot of it incorrect. So we published our own content setting the record straight. Within three or four days, Google updated the Advanced Search. And I had everyone in our company do a thumbs down on that competitor's Advanced Search result, explaining why the source wasn't credible and was inaccurate.

That influenced it. If you can get enough people — especially for low search volume terms — to flag something as inaccurate, the model sees you hit a threshold and shifts.

**Andi Bailey:** That's smart. We've had three customers in the last month come to us with similar issues. A competitor put up a versus page that's wrong. One company said the competitor claimed they're not built for enterprise, when that's their whole business. Misinformation has taken a whole new level.

**Jason Beltran:** When I looked at their content, I could tell it was AI-generated with no safeguards for accuracy. So we published something saying they were spreading false information. At the end of the day, we're just trying to influence the LLMs.

It's a new, weird world. I'm trying to convince my team that things are different now. When it comes to search volume — you might have terms with zero search volume, but you still want to publish pages to influence LLMs. Web traffic is so different than it was before.

**Andi Bailey:** Yeah. Some companies are super protective of their blog, but they're starting to realize it's okay. If DevRel is publishing cutting-edge engineering research every two weeks, there's a small niche audience for that, but discoverability is still there.

**Jason Beltran:** This is what I'm trying to convince my team — we're not really writing this content for humans to read. We're writing it for LLMs to consume and regurgitate. It's so meta. People want to edit tiny words here and there, especially with B2B content. But it doesn't matter. I think a lot of people are way behind on this.

**Andi Bailey:** I saw we have a social pipeline set up for you. Are we doing that right now?

**Jason Beltran:** No, we put that on pause. We're still figuring out our social strategy. We've been taking blog content and building out posts week after week, trying to nail what that looks like. One agency is working on a content strategy for us before we automate anything. We need to get a feel for how we present ourselves on social.

We're leaning heavily into video. Captions don't matter as much. Hashtags do. The content matters somewhat — Meta reads it and surfaces it — but people don't read captions. I can't remember the last time I read a caption on a post, except on LinkedIn.

**Andi Bailey:** There are so many different definitions of social. There's LinkedIn, which is its own thing. And then there's Reddit. LLMs reference Reddit as an objective source — which is wild. Some agencies seed Reddit posts. For one of our clients, we're actively managing their Reddit channel, turning blog posts into Reddit content with specific writing guidelines — no adverbs, incomplete sentences, bullet points are king. If that's where people are looking, put it there and see what happens.

**Jason Beltran:** I went through Reddit yesterday and found about 30 posts referencing Sunbit. Some are a year or three years old. People don't talk about us much on Reddit, which is nice. But I like the idea of seeding those conversations. The challenge is moderation — how do you keep those from going sideways? Reddit is a weird place.

**Andi Bailey:** The strategy is to start within your own channel, build authority and voice, then engage in other communities. But you have to be careful. Airbyte's doing a lot of it, and when I searched Reddit, people called them out for it.

**Jason Beltran:** And who knows how long LLMs will reference Reddit. It comes up as a source, but not necessarily credible. But LLMs love natural human conversations and recency. Recency bias definitely comes up first. They also look at Facebook groups.

I don't know how long that'll last — everyone's complaining about it.

**Andi Bailey:** We're doing a lot of refreshes to make sure you're at the top in terms of who said something about this most recently.

**Jason Beltran:** Recency has the largest impact. And I've noticed that linking out to credible sources really helps too.

**Andi Bailey:** Totally.

**Andi Bailey:** Well, I don't want to keep you for way past this, but we'll definitely take back the reporting — we'll set up that Looker dashboard by next week. We'll get those updated Scrunch prompts in place, and Edisham can start talking you through that every week.

Is there anything coming up for you guys?

**Jason Beltran:** Yeah, there was something we discussed months ago that Marcel was going to reach out about, but I haven't gotten an invite. He invited me to meet up in Seattle a few weeks ago, but I couldn't make it. It's about content for our Sunbit.ai web property launching mid-November. It's focused on machine learning and AI specifically for finance. We want to start generating a lot of content in that area.

**Andi Bailey:** That's definitely something we do. For several clients, we create non-branded assets like this. Marcel's hard to get a hold of sometimes, but what might be good is for us to put together examples of what this looks like for you. Is the site set up?

**Jason Beltran:** It's being designed and developed right now. We should have it launched by mid-November. It'll be on WordPress using the same blog setup as Sunbit.com. It's going to be available in the footer of the site. The audience is existing and potential investors, analysts, financial analysts, media, and tech talent. We'll promote it on LinkedIn. It would be nice if it surfaced through LLMs or search too, but it's not really made for consumers or merchants — it's for the investor class and analysts.

**Andi Bailey:** Perfect. I just launched tech.growthx.ai, which is all AI-generated content by Daniel, our CTO. It's a custom pipeline for topics he knows about. Similarly targeted at investors and top talent, showing what we generate. It's definitely worth looking at. He's pretty technical and used it as an opportunity to hone in on recency of source material, which would be very relevant for machine learning content too.

**Jason Beltran:** This is great.

**Andi Bailey:** Well, we're right at time. Can I ask you for a few quick scores? How would you rate us on relationship, one to ten?

**Jason Beltran:** I'd say a seven. The only reason is because of the transitions in the people we're working with.

**Andi Bailey:** Fair enough. How about velocity?

**Jason Beltran:** I'd put that at a nine. We're getting more articles than we can handle.

**Andi Bailey:** And content quality?

**Jason Beltran:** Honestly, I was reading through a lot of the content yesterday. I'd say a nine. It's really good stuff. The only thing I asked Edisham to do is remove em dashes and Oxford commas.

**Andi Bailey:** I love an Oxford comma, honestly. As a copywriter.

**Jason Beltran:** I love em dashes and block quotes. I'm hurt they're going away. They're a really good, expressive way of writing, but now everyone's like "Oh, this came from ChatGPT."

**Andi Bailey:** Okay, and performance against goals?

**Jason Beltran:** Our organic performance has gone up quite a bit — I'd say a nine. Our organic traffic is up 64% this year.

**Andi Bailey:** Love that. Well, we'll get you better measurements on our end, better reporting, Scrunch optimizations, and keyword gap analysis. Those are easy things. It was great chatting with you, Jason. Thank you for your time, and good to reconnect.

**Jason Beltran:** Talk soon. Bye.
