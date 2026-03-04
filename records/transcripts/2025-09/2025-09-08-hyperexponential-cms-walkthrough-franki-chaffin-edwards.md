# hyperexponential CMS Walkthrough (Franki Chaffin-Edwards)

<metadata>
date: 2025-09-08
time: 16:31 UTC
duration: 22 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien (GrowthX), Franki Chaffin-Edwards (Hyperexponential)
fathom_recording_id: 85668592
fathom_url: https://fathom.video/calls/403651874
share_url: https://fathom.video/share/prgWDHRCnGU7b9H_jn7PkvTHLjsv9yqx
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

Erik O'Brien from GrowthX walked Franki Chaffin-Edwards through Hyperexponential's Storyblock CMS setup during the second week of an 8-week strategy sprint. GrowthX will publish editorial content on the current Storyblock platform (with separate manual publishing for US and UK versions) until Hyperexponential transitions to Framer CMS in 2-3 months, which will enable automated regional distribution. The team identified underwriting as a critical content gap and agreed to present four initial content clusters to David on Wednesday for feedback.

---

## Context

GrowthX is in week 2 of an 8-week strategy sprint with Hyperexponential, a financial services company specializing in underwriting and risk solutions. The engagement focuses on building content generation artifacts (audience personas, company descriptions, and writing guidelines) as part of GrowthX's Atlas content platform workflow. Hyperexponential is actively modernizing its digital presence — the company is currently on Storyblock for its website but planning a complete rebrand and platform migration to Framer by year-end. This meeting was a practical walkthrough of the current Storyblock CMS setup to ensure GrowthX understands how to publish content during the interim period before the new platform launches. Franki is the point of contact on the Hyperexponential side managing the CMS transition, while David (not present) is the primary stakeholder GrowthX is working with.

---

## Relevance

**To GrowthX Delivery:**
- GrowthX will publish content to Storyblock (not native systems) for the next 2-3 months until Hyperexponential's Framer migration. Team must publish each piece twice (once to US blog, once to UK blog) due to Storyblock's separate folder structure — this workflow will change dramatically once Framer is live.
- Storyblock has quirks that require caution: non-functional schema fields (author profile, domain, logo), required but awkward fields (reading time must be entered manually), and buggy override behavior. Recommend sticking to standard templates and not customizing beyond defaults.
- Hyperexponential's existing blog thumbnails are pre-designed abstracts; GrowthX has bandwidth to develop new in-copy imagery, which Franki flagged as a significant gap in their current blog posts.

**To GrowthX Business Development:**
- Underwriting is the largest content gap for Hyperexponential — flagged as critical priority with "big, big volume gap" needed as they expand product offering. This represents expansion opportunity for GrowthX if the initial content strategy succeeds.
- Client shows low historical SEO focus ("SEO has just never really been a big focus for the business") but is now prioritizing it — signals engagement maturity and potential for deeper, longer-term work beyond the 8-week sprint.
- Hyperexponential's platform migration to Framer by year-end creates opportunity for GrowthX to potentially integrate with their new CMS via API-driven publishing, moving away from manual Storyblock updates.

**To CheckThat:**
- Client operates in financial services (underwriting, insurance, risk) — strong vertical for AI visibility and competitive intelligence work if CheckThat expansion is discussed in future conversations.

---

## Overview

- GrowthX is 2 weeks into an 8-week strategy sprint creating content artifacts (audience personas, company descriptions, writing guidelines) for Hyperexponential
- Hyperexponential operates Storyblock currently but will migrate to Framer CMS with automated US/UK regional publishing by year-end; GrowthX will publish manually to Storyblock in the interim
- GrowthX will focus initial engagement on editorial blog content across both US and UK markets; underwriting identified as critical content gap as Hyperexponential expands its product offering
- GrowthX to present 4 top-level content clusters to David on Wednesday; Franki invited to provide feedback and confirm alignment with editorial direction
- Storyblock setup requires separate publishing for US and UK blog folders; includes non-functional schema fields and pre-designed blog thumbnails; new Framer platform will streamline this workflow

---

## Key Topics

### GrowthX Strategy Sprint Overview

  - 8-week engagement to create "artifacts" for content generation:
      - Audience personas (e.g., actuaries, chief underwriters, CIOs)
      - Company context descriptions
      - Writing guidelines for HyperX voice and tone
  - Aim to publish first content piece by week 4-5 (currently in week 2)
  - Will generate 4 top-level content clusters for review

### Current CMS Setup (Storyblock)

  - Separate UK and US blog folders requiring manual dual publishing
  - Standard blog post template includes:
      - Header banner with title, reading time, tags, publication date
      - Pre-designed abstract thumbnails for consistency
      - Description field and main content area with formatting options
  - Author information added via schema tab (some fields non-functional)
  - SEO tab for meta title and description
  - Category tags available but underutilized (can be updated)

### Upcoming CMS Transition (Framer)

  - Moving to Framer by year-end for website and CMS
  - Will enable automated US/UK content distribution with localization
  - Single publishing process with regional versioning

### Content Strategy Considerations

  - Focus on editorial blog content initially
  - Opportunity to develop new blog images and in-copy imagery
  - Flexibility to adjust category tags to align with new content clusters
  - Underwriting identified as a major content gap to address
  - Franki to provide examples of inspirational underwriting content

---

## Action Items

**Erik O'Brien (GrowthX)**
- Generate 4 top-level content clusters and present to David on Wednesday. Share in Slack channel (or alternative channel with Franki) for feedback from both stakeholders.
- Set up GrowthX team to publish content on Storyblock CMS. Create both US and UK versions for each piece. Use existing blog thumbnails for consistency. Develop new in-copy imagery if bandwidth allows.

**Franki Chaffin-Edwards (Hyperexponential)**
- Email Erik examples of good underwriting content and reports for inspiration. Mentioned specific reports come to mind but wants to verify they represent Hyperexponential's overall brand approach before sharing.

---

## Transcript

**Erik O'Brien:** Hi, Franki.

**Franki Chaffin-Edwards:** How's it going?

**Erik O'Brien:** Going well. How's your Monday been?

**Franki Chaffin-Edwards:** Not too bad. How about you?

**Erik O'Brien:** I'm in the Midwest, but we had a bunch of company meetings this morning, so I'm just getting into my workday.

**Franki Chaffin-Edwards:** I am just getting started for the most part. You're West Coast, aren't you?

**Erik O'Brien:** No, I'm in the Midwest.

**Erik O'Brien:** Well, I appreciate you taking the time.

**Franki Chaffin-Edwards:** David's given me a little bit of background context already, but it would definitely be helpful to just get a replay on what you've discussed so far, how we can kick things off, and get the most out of the time we have with you guys over the next however many weeks it is.

**Erik O'Brien:** I'm Erik O'Brien, an account strategist working with Hyperexponential and David. Over the next eight weeks, we call it a strategy sprint, where we're really ingesting a bunch of information from you guys to create what we call artifacts. Artifacts are the linchpin for the content generation platform we use called Atlas. Everything from audience and personas is one of the artifacts we create — things like actuaries, chief underwriters, CIOs. Other ones we do are company contexts — how we describe Hyperexponential to somebody who's never heard of you before. And lastly, we do writing guidelines so that the content comes off as Hyperexponential voice and tone. Those are the three big ones. Today's CMS walkthrough doesn't have anything to do with those — it's mainly so we understand how you use Storyblock, how content is currently published to the website, and make sure we don't miss anything as we start to do some of our calibration blogs. We'll try to publish our first piece of content by week four or five. We're currently in week two. Anything else I can answer before we get diving in?

**Franki Chaffin-Edwards:** Just one question from my side — have you already got something to kick off with in terms of initial content focus, theme, format, or persona?

**Erik O'Brien:** Not yet. We'll be generating what we call clusters. We'll come up with four top-level clusters today or tomorrow and present those to David on Wednesday. A lot of those topical clusters incorporate audience, company context, and writing guidelines that we've generated for Hyperexponential. We'll get feedback from David, but also if you'd like to be part of that, we'll share it out within the Slack channel or find an efficient way to share it since you're not in our Slack. I'd love as much feedback as we can get on those initial four because that's where we'll start, and then we'll build out additional keyword research and more clusters.

**Franki Chaffin-Edwards:** Okay, cool. I'll give you a rundown on the CMS side of things. David may have mentioned this, but it's a little bit complicated. We're in the middle of planning a total website re-platform — brand, visual lift, all of that. We'll ultimately be moving over to Framer by the end of the year as our website platform and CMS for the blog and gated content. Right now, the website is run and hosted in Storyblock, and it will be that way for at least another two to three months, realistically. So it's worth you guys publishing onto there in the meantime. I will warn you, our Storyblock setup is not the best — part of why we're moving away from it and re-platforming. You should have access to Storyblock already, but I can share my screen quickly and show you through it if that's helpful.

**Erik O'Brien:** I'm recording this so that our teammates who will do the publishing also get a view of this.

**Franki Chaffin-Edwards:** Let me share my screen.

**Franki Chaffin-Edwards:** Within Storyblock, when you go to the content tab, you should be able to find our blog folder. We have a UK blog folder and a US blog folder. They run independently of each other. When we built this out, we didn't have much presence or content for the US, and the terminology and topics were so different that we deliberately split them out as two separate assets. The bulk of our content lives in the main blog folder.

Within this, you have all existing blog content that you can click into and see. There's a standardized blog post template with a header banner — the post hero. You get a title, you have to enter a reading time (or it won't let you publish), tag selection for category tags, a publication date, and a story image. We have pre-designed abstract blog featured image thumbnails that you're welcome to leverage for these header blocks for consistency.

Under that, you have the description field — all of our blog headers have this annoying bit of text you have to figure out. Then underneath that, you've got one big, long, single editable text field with your different header options. You can add blocks for call-out text, video, stats, images, all that stuff directly within this text box, which takes you to the bottom of the page. Everything else is standardized. You automatically get the global header, theme, footer, contact overlay, related content — all pulled in automatically. You can override that manually if you have to, but I try to avoid it because Storyblock is a bit buggy. So I let it do what the presets want it to do. That's the typical blog post format.

**Erik O'Brien:** Do you foresee us wanting to do both US and UK, or focus on US?

**Franki Chaffin-Edwards:** We want to do both, for sure. One of the downsides of the Storyblock setup is that the US and UK blogs are totally separate entities. When we move over to Framer, we'll be building much more automated US and UK versions of the blog regionalized with a glossary of key terms that wouldn't be caught by a typical swap of S's for Z's. When we move to Framer, we'll just need to publish content once into the CMS. It will automatically distribute it onto both regional versions with the relevant localization. But for now, sadly, you've got to build it out in both US and main blog folders.

**Erik O'Brien:** For blog images, would you prefer we use what's in the catalog, or is there interest in us developing new blog images?

**Franki Chaffin-Edwards:** I'm happy for you guys to build additional ones. One of the main things we lack right now is in-copy imagery. We get these little preview images from the pre-built selection, but the vast majority of blogs don't actually have much in-copy imagery. Anything you want to do on that side would be more than welcome. It's a bit of a blind spot for us right now — one of those many things on the list that doesn't actually get done.

**Erik O'Brien:** I saw there's a theme for each blog post. Is there any rhyme or reason to choose different themes color-wise?

**Franki Chaffin-Edwards:** They should all be the standard blue. On the blog homepage, you get a selection of images, but once you click through to an individual blog post, it's always the same light gray background. There's no dark blue or anything — all individual blog posts look like this.

**Erik O'Brien:** Anything to look out for as we're publishing? I know it's a little bit buggy, but as long as we keep the standard selections, not much should go wrong, right?

**Franki Chaffin-Edwards:** A couple of weird little things to note. I'm imagining the content you guys create won't be authored by a person — it's going to be authored by Hyperexponential, right?

**Erik O'Brien:** We can choose authors if you want specific people to be attributed, and our editorial teams will review. But if you want to keep it as authored by Hyperexponential, that works fine.

**Franki Chaffin-Edwards:** When it comes to the author field, you can leave it blank if it's not actually authored by a real person. But if you do want to add an author, you have to go to the schema tab and put the author's name in. Author profile is a field that doesn't actually exist. Domain is also a field that doesn't exist. Just adding a logo will do nothing. Putting the organization in will do nothing. So this is what I mean about the quirks and weirdness. In the SEO tab, you have your meta title and meta description — those basic bits and bobs. That's where they live. I imagine the clusters you come up with will affect how they fit into our existing category structure. I didn't come up with these tags — they were here long before me, and I don't think they're ideal. So if the content fits into one of the existing category tags, use it. If it doesn't, I have no issues with changing these around or adding different ones that fit against the clusters you're building.

**Erik O'Brien:** Do those tags make it into the URL slug?

**Franki Chaffin-Edwards:** Looking here, the URL slug is just /blog and then the title. So you can see the pricing category tag here, but the URL is /blog/[title]. The tags aren't part of the URL slug. But if you click through to one of the tags, you get /blog/tags/pricing or /blog/tags/operations, whatever it may be. I wonder why nobody really uses these tags — they're so well hidden and not very accessible anywhere.

**Erik O'Brien:** Good to know. If we create new ones or get creative with sub-pages, it's good to know how those tags show up.

**Franki Chaffin-Edwards:** Are you guys largely focusing on blog style content in this first run? Any gated content planned?

**Erik O'Brien:** We focus mainly on editorial content for the first eight weeks. Not to say we're restricted to that — some clients look at programmatic SEO where they'll build hundreds or thousands of pages for comparative content. I don't know if that's the case with you guys yet.

**Franki Chaffin-Edwards:** That makes sense. I'm happy with that. SEO has just never really been a big focus for the business until now. But about time we start paying attention to it. The good news for you is you've got a pretty light zero-to-one ahead of you in terms of the starting point.

**Erik O'Brien:** That's what we were saying internally. It's kind of like a blank canvas. We can go a lot of different directions. Hopefully this week we'll land on a few of those top-level cluster opportunities and get agreement and feedback. This has been super helpful. Storyblock looks pretty straightforward from a publishing perspective. We'll just have to make sure we do the US and UK versions for now. Once you get Framer up and running, it'll be more efficient and API-driven.

**Franki Chaffin-Edwards:** Exactly. Apologies in advance for Storyblock. It's a fun one to work with. Does that give you everything you need for right now?

**Erik O'Brien:** I think so. Any other things you want to talk about while we have time?

**Franki Chaffin-Edwards:** I'm keen to see what you guys come up with on the clusters and rollout side. One point I'm acutely aware of is that as we're expanding our product offering, we're going to need a lot more content around underwriters and underwriting, which hasn't been a big focus for us until now. So heads up that's the kind of big volume gap that needs filling, where you may find there isn't as much existing content or context to pull from. But I'm keen to see some of the first outputs and get a sense of how we could ramp this up and what it looks like.

**Erik O'Brien:** For that underwriting content, is there anything you guys look to as inspirational — content you'd want to mimic?

**Franki Chaffin-Edwards:** Let me think and I'll send you a couple of options via email. There are a couple of good ones that come to mind for specific reports or long-form content, but I want to verify they represent Hyperexponential's overall approach before sharing. Let me do a little check and if they're a good representation as a whole, I'll drop them over via email.

**Erik O'Brien:** Wonderful. Even if it's a report, that would help us ingest context around that specific audience.
