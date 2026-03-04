# Clerk Weekly Sync

<metadata>
date: 2025-09-04
time: 16:00 UTC
duration: 32 minutes
organizer: team@growthxlabs.com
participants: Alex Rapp, Brian Morrison II, Aida Knezevic, Andi Bailey
fathom_recording_id: 85020314
fathom_url: https://fathom.video/calls/398705093
share_url: https://fathom.video/share/xBv9x9iskrzNSn6CU46KzGuQHMLWzs67
source: fathom
enriched_on: 2025-09-04 23:45 UTC
</metadata>

---

## Summary

GrowthX and Clerk aligned on blog post feedback for the SSO calibration post, with Alex Rapp requesting internal team review and agreement to follow Clerk's brand guidelines (e.g., "sign-in" over "login"). The team discussed LLM optimization strategies including schema markup (FAQ schema), natural language processing, and descriptive subheadings — all critical for appearing in ChatGPT and Perplexity. Aida shared the new Looker dashboard tracking performance by topic clusters, individual URLs, and LLM referrers, with a GA4 data quality issue ("not set" landing pages) flagged for investigation.

---

## Context

Clerk is a developer authentication platform and long-standing GrowthX content marketing client. Alex Rapp leads Clerk's content strategy and is balancing two priorities: maintaining brand consistency (Clerk's design and voice standards) while experimenting with AI search (AEO) visibility through new content. Brian Morrison II is Clerk's primary content author. Aida Knezevic is GrowthX's AEO expert managing the engagement. Andi Bailey from GrowthX joined to cover deliverables while Aida is out the following week. The meeting occurred amid Clerk's transition to new brand templates and their team's push to improve LLM acquisition — they've seen growth in ChatGPT referrals but lower intent compared to traditional Google SEO.

---

## Relevance

- **To GrowthX Delivery:** Writing guidelines reinforcement: use "sign-in" per brand, include descriptive subheadings in question format, apply FAQ schema markup, and prioritize natural language processing in content. Image generation workflow can scale once Clerk's design team finalizes templates. Content manager review process now includes writing guideline updates.

- **To CheckThat / AEO:** Clerk's LLM traffic coming primarily from ChatGPT and Perplexity; schema markup and direct Q&A formatting are key differentiators. Aida observed stronger acquisition from ChatGPT than Google SEO but lower conversion intent — suggests opportunity for funnel optimization tracking. Volume matters: Aida's first client saw major LLM visibility gains in just 6-8 months with consistent publishing.

- **To GrowthX Business Development:** Account health: Clerk is investing in new brand templates, expanding content volumes, and adding down-funnel KPI tracking (installation, activation events) to better measure AEO ROI. Conversion event verification needed on Next.js onboarding flow after Feb 2025 change. No immediate renewal risk; expansion potential as LLM channel matures.

---

## Overview

- Alex Rapp to get broader feedback from Clerk's team by midday Sept 5; GrowthX to implement changes to SSO calibration blog and update writing guidelines per Clerk's brand standards
- Clerk's design team working on new brand templates; GrowthX ready to adapt image generation workflow and expedite publishing once templates finalized
- LLM optimization strategy: use FAQ schema markup, write for natural language processing (direct sentences, low dependency), format subheadings as questions with direct answers in first paragraph
- Looker dashboard live tracking topic clusters, individual URLs, and LLM referrers; GA4 "not set" landing page issue and signup conversion event verification on Next.js onboarding flow flagged for investigation

---

## Key Topics

### Blog Post Review and Feedback

  - 80% of content on track; some drift towards enterprise-style customers noted
  - Agreed to use "sign-in" consistently as per Clerk's brand guidelines
  - Technical review process: internal team first, then broader sharing for senior technical members' input
  - GrowthX encouraged to push back with data-driven insights from successful strategies

### SEO and LLM Optimization

  - SEO audit shared last week; Isaac tackling site audit issues
  - LLM optimization builds on SEO foundation with added focus on schema markup (e.g., FAQ schema)
  - Content strategies: natural language processing, direct Q\&A formatting, descriptive subheadings
  - Internal linking preferences: docs over glossary, staying within Clerk's domain when possible

### Content Asset Design

  - Clerk's design team working on new brand templates for consistency
  - GrowthX can adapt their image generation workflow to match Clerk's design once finalized
  - Quick image generation helps avoid publishing delays

### Looker Dashboard

  - New dashboard pulls data from Google Search Console and GA4
  - Tracks performance by topic clusters, individual URLs, and LLM referrers
  - "Not set" issue in GA4 data to be investigated further
  - Conversion event tracking for sign-ups needs verification due to onboarding flow changes

### LLM Traffic Insights

  - Early observations suggest stronger acquisition but lower intent from ChatGPT compared to Google SEO
  - More comprehensive down-funnel KPI tracking desired for consistent reporting

---

## Action Items

**Alex Rapp (Clerk)**
- Provide feedback on glossary links vs. docs links in SSO blog

- Decide on linking strategy for Next.js reference (internal vs. external)

- Get more team members to review calibration blog post, open for broader feedback by midday tomorrow

- Verify signup conversion event firing correctly for new Next.js onboarding flow


**Aida Knezevic (GrowthX)**
- Have content manager review blog changes, update writing guidelines accordingly

- Investigate GA4 "not set" issue with Vivek, explore potential fixes

---

## Transcript
**Alex Rapp:** Hello, hello.

**Aida Knezevic:** Hi, how are you?

**Alex Rapp:** I'm good, how are you doing?

**Aida Knezevic:** Good, except that my neighbors decided to start doing construction at 6 p.m.

**Aida Knezevic:** I really apologize if you end up I can't hear it at all.

**Aida Knezevic:** Yeah, he's stopped now.

**Alex Rapp:** Okay.

**Aida Knezevic:** Yeah, but, you know, it is what it is.

**Alex Rapp:** Yeah, that's something you gotta deal with. It's funny — I was just talking to one of my teammates and he has contractors at his house too, with all sorts of hammering and banging in the background. But honestly, I couldn't hear it either, so I think we're all set.

**Aida Knezevic:** Okay, nice. The sound isolation is really good. By the way, hi Brian. Today, Andi's also going to join us. Andi's the head of customer operations at GrowthX. I'm going to be out of office all next week, so she's joining to help fill in in case you have any questions.

**Alex Rapp:** Okay, cool. On that note, we're going to be at an off-site the week of September 14th in Iceland, oddly enough. I'll have to figure out if we can keep our scheduled time or find something else, since I'll be closer to your time zone.

**Aida Knezevic:** Yeah, we can meet earlier in the day.

**Alex Rapp:** Cool. Where did you want to start?

**Aida Knezevic:** I wanted to start with just your thoughts about the calibration blog.

**Aida Knezevic:** I know you left a couple of comments, but I just wanted to get like some overall feedbacks.

**Alex Rapp:** Yeah.

**Alex Rapp:** So I, I put it out there for the team to take a look at.

**Alex Rapp:** Brian, know that you were bouncing around a bunch of places yesterday.

**Alex Rapp:** I'm not sure if you had a chance to dig in there yet.

**Alex Rapp:** The, there was a couple main themes that stood out to me that I have not raised yet.

**Alex Rapp:** And other than that, you know, say kind of 80% of the way there, you know, that's, that's just one person's opinion and especially one that is not nearly as technical as the rest of the team.

**Alex Rapp:** So I still want to get.

**Alex Rapp:** Additional eyes on it.

**Alex Rapp:** one of the main things that stood out to me was there was some drifting in some of the content that went more towards enterprise style customers as opposed to sort of the individual developer or kind of the early stage startup.

**Alex Rapp:** So, you know, I made some comments around areas that stood out to me there that we would probably update.

**Alex Rapp:** Other than that, it was mainly just, you know, some of the nuance edits like sign-in versus log-in, which thank you for providing that guidance there, which, you know, I think we'll just use, you know, in any case where, you know, there's opportunity to use our verbiage versus, you know, more universal.

**Alex Rapp:** Log-in versus sign-in, that's such a difficult one for me because I know, you know, by...

**Alex Rapp:** Looking in AHREFs that login has much higher search volume compared to sign-in.

**Alex Rapp:** So that is an internal battle that I struggle with.

**Alex Rapp:** Do you have any additional thoughts that you want to kind of extrapolate on there beyond your comment of just being able to use sign-in in these cases?

**Aida Knezevic:** I think, let me just look into it a little bit more, because I just feel like these are basically near synonyms, right?

**Aida Knezevic:** 100%, yeah.

**Aida Knezevic:** Yeah, yeah.

**Alex Rapp:** Yeah, I mean, the problem is, is that, you know, for, if I send this out to, you the rest of the team, especially leadership, that will be the first thing that they hone in on.

**Alex Rapp:** You know, I guarantee it is, you know, we call it sign-in.

**Alex Rapp:** We don't call it login.

**Alex Rapp:** can sign-in is all over our docs, it's over our landing pages, it's.

**Aida Knezevic:** It's part of our brand kit, more or less.

**Aida Knezevic:** Okay, okay.

**Aida Knezevic:** No, I'm always then, like, I always go with what the brand is.

**Aida Knezevic:** It's just, if it's a synonym, and it is a synonym, then it's not that big of a deal.

**Aida Knezevic:** It would be a bigger deal if that was the primary keyword — then it'd be an issue. But if it's just mentioned throughout, I don't think it's that big of a deal. The first time it's mentioned, we could say "log in or sign in," then continue using "sign in." Those are my thoughts, and thank you for pointing that out. We're going to add that to the writing guidelines so it's consistent.

**Alex Rapp:** Yeah, I'm all up for testing, and what you just laid out makes sense.

**Alex Rapp:** I think for now, let's keep the powers that be happy and just adhere to brand guidelines.

**Alex Rapp:** And then, you know, as we kind of go through the proof of concept phase of this, you know, we can kind of start to drift outside of those lines, especially for upper funnel content as well.

**Alex Rapp:** You as I mentioned, you know, to start, at least a lot of this content is going to be unlisted, you know, on our website.

**Alex Rapp:** But, you know, we know that in order to win, we need to start also finding ways to distribute this content as well.

**Alex Rapp:** So, yeah, it's going to be a bit of a tightrope walk, in my opinion.

**Alex Rapp:** You know, I shared with you, but Andy, maybe it's good context for you as well.

**Alex Rapp:** We've...

**Alex Rapp:** At the start of the year, we pursued external contractors for content writing just to bolster our resources in that area.

**Alex Rapp:** Because right now, Brian is really the sole content creator, especially written content.

**Alex Rapp:** And our CEO, he basically had to shut it down because he was just not pleased with the quality and the level of technical degree as well.

**Andi Bailey:** And do we have, is there like a technical reviewer on your team who will be like a stakeholder in this?

**Andi Bailey:** Or is this just like, I don't want to say vibes, but like the kind of let's double check just on an audit basis, like random?

**Alex Rapp:** sure.

**Alex Rapp:** So I think the way that I kind of laid it out for Aida was that let's get everybody.

**Alex Rapp:** Everybody comfortable with, you know, the first, you know, couple batches.

**Alex Rapp:** And when I say batches, you know, maybe upwards of, I don't know, call it 10 to 12 articles, get everybody feeling really good about the quality bar and, you know, the degree of technical, you writing, you know, where, you know, where it's present.

**Alex Rapp:** And then, you know, once we feel as though everybody's kind of comfortable with the quality bar and we're starting to see, you know, actual performance from the content you're sending our way, then we can kind of open up the floodgates with, you know, more bulk production.

**Alex Rapp:** In terms of, you know, sort of, you know, the quality control individuals, you know, I would say, you know, Brian is really kind of the front line there, as well as Nick on our team.

**Alex Rapp:** The way that I'm rolling this out right now is I'm sharing it within our team internally only first.

**Alex Rapp:** And then once they provide their feedback, I'm going to share it more broadly.

**Alex Rapp:** It's kind of a guessing game as to who's actually going to lean in and read the content.

**Alex Rapp:** But I think what we can do is advocate for a couple of our more senior technical team members, like our head of engineering and even Colin, our CEO, to actually lean in more heavily.

**Alex Rapp:** So that way, you know, we've kind of convinced those that, you know, the opinions that hold the heaviest weight.

**Andi Bailey:** Okay, great.

**Alex Rapp:** Yeah, perfect.

**Aida Knezevic:** Yeah, that makes total sense.

**Aida Knezevic:** So we'll wait.

**Aida Knezevic:** You can just shoot us a message on Slack when everybody on like your internal team has provided their feedback.

**Aida Knezevic:** Then we can go in, make the edits, and we'll take it from there. In these types of situations, I feel like it's best to follow what the brand is. That's a much bigger conversation than just content. I think we should stick to that for the time being.

**Alex Rapp:** I would love to empower you to also push back in areas where you've seen success. Before engaging with GrowthX, we were using best practices we'd observed from others. Our answer engine volume is growing, but not nearly as rapidly as I expected. It's quite possible we need to adjust our strategy or playbook. I'd really love any pushback — I see this as iron sharpening iron. Anything, any learnings you can pass along, even if contrary to what we're advocating for, please at least surface those concerns.

**Aida Knezevic:** Yeah, yeah, of course.

**Aida Knezevic:** Yeah, thank you for letting me know.

**Aida Knezevic:** Yeah, I think it's just a matter of volume, really — publishing value that will allow you to gain more AI search visibility. When I joined GrowthX, my very first client had very little content on their website and was a new brand in their industry. We just started publishing very regularly, and by six months in, they were seeing really big results in terms of LLM visibility. They started showing up in Perplexity with these very specific blog posts related to their product. I checked their HubSpot recently and they were getting more leads by month from the blog. So it compounded over about eight months. It's just a matter of volume and targeting the right topics and clusters.

**Alex Rapp:** So we'll get there. I'm confident. Can you remind me — did you conduct any sort of audit of our site in terms of how well we're set up universally to how LLM-friendly our website is right now, essentially?

**Aida Knezevic:** We did an SEO audit last, I think I shared the spreadsheet with you last week.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, I'm going to drop the link.

**Aida Knezevic:** There were some things I think you could already be handling, but I'll send you the link.

**Alex Rapp:** Oh, never mind. I actually shared that with our team member, Isaac, who is tackling all the SEO site audit issues we have.

**Alex Rapp:** Yeah, he took it. It was helpful. Some of it was redundant to stuff he was already chasing, which was good.

**Aida Knezevic:** For LLM optimization specifically, SEO is still the foundation. The differentiator is schema markup — adding things like FAQ schema. Google labeled it as not that important for SEO, but for LLMs it's very important because it mimics prompts.

**Alex Rapp:** Because it mimics prompts, yeah.

**Aida Knezevic:** Yeah, that's what they're looking for. And LLMs really like writing for natural language processing — using direct sentences with as little dependency as possible. They like when the subheading is in question format, very direct and clear. Then the first paragraph after the subheading directly answers that question. Every section should provide a direct question and direct answer without being ambiguous or unclear. For example, "implementation tips" versus "how to implement single sign-on in your application" — the latter is much better. The more descriptive it is, the better for the LLM. Those are the things we follow internally as we edit and generate content.

**Alex Rapp:** Brian, any questions around that? Those are all known best practices that I shared with you. As the person authoring a lot of our content, I'm just curious if you have any questions.

**Brian Morrison II:** Not at the time.

**Alex Rapp:** Cool.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** One thing I wanted to get your feedback on was the featured image designs.

**Aida Knezevic:** I shared them over Slack, but I can share my screen again.

**Alex Rapp:** I didn't get a chance to dig into those, but it's topical right now. It's been raised in our team that we've drifted away from consistent design. Our design team is working on new brand templates we'll use across the board. I'll look at what you sent, but we'll probably go with whatever the design team comes up with. The intent is to make it easy to plug and play and repurpose for any content — more simple, less noisy than what we have now. I'll take a look, but we'll wait and see what our design team produces. If their runway is longer than I hope, we can test your team's assets once I've reviewed them.

**Aida Knezevic:** Yeah, that works. We can always go back and replace.

**Aida Knezevic:** But I do have to say, like, very recently with a different client.

**Aida Knezevic:** We had an image generation workflow, and we noticed that they kept going in and replacing it with their own images, which were kind of like a background with an illustration to the right and then the title of the blog.

**Aida Knezevic:** And we went back to our designer, Katya, and she set up an image generation workflow that basically just generates the exact same designs that they liked.

**Aida Knezevic:** So we just needed more information, and they were like, oh, this is great.

**Aida Knezevic:** We don't have to do this anymore.

**Aida Knezevic:** So we just need like, just like once they have like the assets ready, like they can give us a couple of examples and we can also take it from there.

**Alex Rapp:** Okay.

**Alex Rapp:** All right.

**Alex Rapp:** Noted on that one.

**Alex Rapp:** How do those assets even play a role aside from, you know, the alt text associated to them?

**Alex Rapp:** How do the assets themselves actually, you know, contribute to performance?

**Aida Knezevic:** They don't really contribute to performance, other than making the site look nice and overall brand consistency.

**Aida Knezevic:** It does help us publish faster. If we relied on clients to provide all images, we wouldn't publish as quickly or get results. Images are a common blocker for internal design teams who don't have much time for this work. We want to make it easier and help you publish as quickly as possible.



**Aida Knezevic:** When I first started, there was a client who wanted to do all their own images. They were great, but we were backlogged for two to three weeks just waiting on the images. That was not fun.

**Alex Rapp:** Yeah, that was not fun.

**Alex Rapp:** Okay.

**Alex Rapp:** Yeah, that makes sense.

**Alex Rapp:** I did have a couple more questions for you on the SSO blog.

**Alex Rapp:** There were places where you linked to our glossary. I created it but it was too time-consuming, so we handed it to our docs team. They haven't touched it, so it doesn't get much traffic. For cases defining SSO or OIDC — things also well-defined in our docs — what's your opinion? Should we point to docs versus the glossary?

**Aida Knezevic:** It's a good idea, especially since we're speaking to developers. Docs would be more helpful. I have an internal linking workflow that picks links from your sitemap. I'll check with the dev team to see if we can narrow it down to just your blog and docs — that might make controlling internal links easier.

**Alex Rapp:** I'll do some digging to validate my hypothesis on glossary traffic. Similarly, we have a link to a blog for Next.js from 2022. I want to find something better — maybe our Next.js landing page. Is there benefit in linking externally to the actual Next.js homepage versus staying in our domain?

**Aida Knezevic:** Best practice is to stay within your domain. Even if it's an older blog, it's good for site structure.

**Alex Rapp:** Maybe we could refresh that, but I don't know if we have business ranking potential for Next.js directly. Brian?

**Brian Morrison II:** We explored targeting Next.js directly with Craig, but he said it's a bad idea because we don't do Next.js directly — only with authentication rolled in.

**Alex Rapp:** Okay, we can make a decision on that specific link. Those were the only questions I had. I'll ask the team to get more eyes on the blog post today and open it to the rest of the team. My hope is by midday tomorrow I'll give you the go-ahead. I can incorporate the changes, or would you rather take them and build them in yourself?

**Aida Knezevic:** Our content manager will review the changes because they also update the writing guidelines. Can you duplicate a version with all comments and share it with us? Then you can make changes to the actual blog and remove the comments.

**Alex Rapp:** Yeah, we'll leave the comments in place and let you run with it. We can check version history if needed.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** I also gave you access, I'm going to share the link in chat, to your Looker dashboard.

**Aida Knezevic:** This is something that we set up last week.

**Aida Knezevic:** I'm going to go ahead and share my screen really quickly with you.


**Aida Knezevic:** It pulls data from Google Search Console and GA4. The most interesting pages are the cohorts, which right now have nothing but will include topic clusters measuring performance by cluster. You'll track individual URLs and compare to overall site performance.

**Aida Knezevic:** We also have an LLM referrer breakdown from your GA4 showing all the LLMs sending traffic to your site and what the landing pages are.

**Aida Knezevic:** So you all, like you, Brian, and Nick should all have access to it.

**Aida Knezevic:** And you have editing access as well.

**Brian Morrison II:** So you're able to change the dates and kind of go back in time.

**Alex Rapp:** All right.

**Alex Rapp:** Quick question for you.

**Alex Rapp:** So I noticed it's present here, but not on the landing page tab.

**Alex Rapp:** And I think I know the answer as to why.

**Alex Rapp:** On the LLMs tab, you know, the second most popular or highest volume landing page is not set.

**Alex Rapp:** I'm assuming that's just filtered out of the landing page tab.

**Alex Rapp:** But what can we do about that?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** The "not set" is traffic where I've encountered similar situations in the past and couldn't find the resolution.

**Aida Knezevic:** It's just a GA4 bug where they just are unable to collect the data.

**Aida Knezevic:** But I'll talk to Vivek.

**Aida Knezevic:** He's the managing editor who has developed these Looker dashboards, and I'll ask him to see if there's anything that we can do.

**Aida Knezevic:** But not set is, like, a pretty consistent issue for a lot of websites, unfortunately.

**Alex Rapp:** Yeah, I know.

**Alex Rapp:** I was curious.

**Alex Rapp:** Maybe it was a tracking issue where the tracking pixel didn't fire or wasn't present, or people who opted out of cookie consent or fell under privacy rules.

**Aida Knezevic:** It could be a mix of things. I'll look into it again. I investigated this on the Google Analytics subreddit and people said nobody really knows. I'll take another look and see if there's something you can do about it.

**Alex Rapp:** Okay.

**Alex Rapp:** Conversion events.

**Alex Rapp:** I have to make sure that this signup conversion event is actually firing as it should.

**Alex Rapp:** The problem with this is that back in February, we adjusted our onboarding flow specifically for Next.js, which is far and away our most popular SDK.

**Alex Rapp:** The onboarding flow kind of flipped on its head where you actually go through the process of installing Clerk first.

**Alex Rapp:** And then once you feel as though you have found the value, only then do you actually go sign up and create an account.

**Alex Rapp:** I have not done the due diligence yet to understand whether or not that event is firing for that specific user journey.

**Alex Rapp:** In some cases, you can still directly go and sign up, but that is something that I want to keep a close eye on because that is our first primary KPI in terms of the onboarding flow metrics that we track.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah, that makes sense.

**Aida Knezevic:** Yeah, we definitely want to make sure that that's as accurate as possible.

**Alex Rapp:** We've been trying to get our down-funnel KPIs in here as well, but there's a technical tracking issue where we can't pull in events like installation or activation — the qualitative metrics the team cares about. That's something I want to explore when I have more time.

**Alex Rapp:** I learned from a teammate also pursuing this as a growth channel that they're seeing stronger acquisition from ChatGPT compared to Google SEO, but intent is significantly lower. That's something we can track more universally for LLMs on our side, but consistency in reporting across Looker and our side would be great.

**Aida Knezevic:** We're over time, but that's something I can pursue on my side.

**Aida Knezevic:** Okay, I have to jump to another meeting, but follow up over Slack, and I'm looking forward to the rest of the team's comments.

**Alex Rapp:** Yeah, we'll get that over to you tomorrow, for sure.

**Alex Rapp:** So we definitely want to try to get that published as soon as possible and start to see if it brings some traffic in.

**Alex Rapp:** All right, awesome.

**Andi Bailey:** Thank you, Aida.

**Alex Rapp:** Great to meet you, Thank you.

**Andi Bailey:** Yeah, likewise.

**Alex Rapp:** Bye.

**Alex Rapp:** Bye.

**Alex Rapp:** Bye.
