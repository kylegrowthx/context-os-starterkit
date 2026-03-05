# Exec <> GrowthX Weekly Sync

<metadata>
date: 2025-02-20
time: 21:59 UTC
duration: 48 minutes
organizer: Kyle Gaudreau (GrowthX)
participants: Sean Linehan (Exec), Elvis Goren (GrowthX), Kyle Gaudreau (GrowthX)
fathom_recording_id: 48318058
fathom_url: https://fathom.video/calls/236698732
share_url: https://fathom.video/share/VR42mWxLUSTr_KNoLkfyY2zcVJyjrxzV
source: fathom
enriched_on: 2025-03-05 14:32 UTC
</metadata>

---

## Summary

GrowthX and Exec aligned on content production strategy for exec.com/learn, planning to scale from 2 calibration articles to 5-10 weekly pieces targeting 1200 annually. Sean walked through Exec's Contentful CMS with custom React app featuring AI-powered interactive elements (GPT bots for resume writers, rephrasing tools), while GrowthX confirmed their use of GPT-4 with multi-stage refinement and Midjourney for initial image generation. The team identified next steps: technical SEO audit via Enica, adding the Learn section to navigation, removing explore page links, and sharing CMS training access to team@growthx.com.

---

## Context

Exec is a B2B professional development platform that recently built a learn.exec.com section to host content produced by GrowthX. This is a long-term content engagement where Exec is the client and GrowthX is providing content strategy and production services at high volume. Exec has significant technical sophistication — their entire learn platform is powered by Contentful CMS with a custom React front-end, featuring built-in AI tools like automated resume writers and tone rephrasing tools. Exec was on the market looking for partners who could produce quality, SEO-optimized content at scale while respecting their brand voice and technical architecture. Sean Linehan (VP at Exec) reviewed the first GrowthX-authored article and was impressed by how natural and non-AI the tone felt, which was the key validation point going into this sync.

---

## Relevance

**To GrowthX Delivery:**
- Confirmed Exec's tone preferences and GPT-4 output quality meets expectations — Sean validated first article as natural and non-AI-like despite using AI in production workflow
- Established content production ramp: starting with 2 calibration pieces, scaling to 5-10/week by next week, targeting 1200 articles annually (roughly 25/week)
- Identified key CMS requirements: no staging environment (changes publish directly to production), H1 tags reserved for article title only, H2+ for content headers, sidebar CTA feature configurable per article
- Image strategy confirmed: will use Midjourney AI for initial generation; Exec open to abstract/vector art styles; may refine approach later if needed
- CMS training plan: Elvis or Daniel will be primary content publisher; Sean will share Contentful training guide via Notion to team@growthx.com

**To GrowthX Business Development:**
- Account health signal: Exec is investing in expanded content strategy and platform capabilities, good indicator of expansion potential
- Client sophistication level: Exec has built proprietary AI-powered features and custom Contentful implementation, suggests they value technical depth and may expand scope to leverage other GrowthX capabilities
- Hiring signal: Kyle mentioned planning 70-80 headcount additions over next few months, indicating high confidence in growth and opportunity for expanded services

**To CheckThat / AI Visibility:**
- Exec already running AI-powered interactive tools on their learn section (GPT bots for job applications, resume builders, professional tone rephrasing)
- Discussion of GPT model economics: Sean noted how cost of intelligence is approaching zero, driving competitive dynamics
- Potential AI visibility opportunity: as Exec ramps content to 1200+ articles yearly, they may benefit from CheckThat audits to ensure AI visibility and AEO positioning of learn section

---

## Overview

- Exec's learn section (exec.com/learn) will host new SEO-optimized content
- GrowthX to ramp up content production to 5-10 articles/week, aiming for 1200 annually
- Exec's Contentful CMS setup is robust, with custom AI-powered interactive elements
- GrowthX to use Midjourney for article images initially; may refine approach later

---

## Key Topics

### Content Calibration and Production

  - Sean reviewed initial article, found it impressively non-AI-like in tone
  - GrowthX uses GPT-4 for content generation, goes through multiple refinement stages
  - Aiming to ramp up to 5-10 articles/week, with a long-term goal of 1200 articles annually
  - GrowthX to get Contentful CMS access; Sean shared training guide

### Exec's CMS and Website Setup

  - Exec uses Contentful CMS with custom React app for rendering
  - Learn section (exec.com/learn) hosts content in series/categories
  - Custom AI-powered interactive elements (e.g., resume builders, rephrasing tools)
  - New website design in progress with updated color palette

### SEO and Technical Considerations

  - Remove "explore page" links from articles (custom workshop pages)
  - GrowthX to conduct technical SEO audit to identify potential improvements
  - Exec working on performance optimizations (Lighthouse scores)
  - H1 tags used only for article titles; H2 and below for content headers

### Image Creation for Articles

  - GrowthX to use Midjourney AI for initial image creation
  - May refine approach later if needed; Exec open to abstract/vector art style

### CTA and Publishing Process

  - Exec has a "sidebar CTA" feature configurable per article
  - No staging environment; changes publish directly to production
  - Fast feedback loop for content adjustments

---

## Action Items

**Kyle Gaudreau (GrowthX)**
- Loop in Enica for technical SEO audit of exec.com

**Sean Linehan (Exec)**
- Add "Learn" section to top navigation of exec.com
- Share Contentful CMS training access via Notion to team@growthx.com

**Elvis Goren (GrowthX)**
- Remove links to explore pages in drafted articles (per Sean's feedback that explore pages are custom workshops not meant for public discovery)

---

## Transcript

**Elvis Goren:** Oh, hello.

**Elvis Goren:** It'd be like zero degrees this weekend here, so I'm pretty excited about that.

**Kyle Gaudreau:** That's an improvement. That's amazing, dude.

**Elvis Goren:** Last year was awesome because it was that El Niño situation.

**Elvis Goren:** Hey, Sean. Hey, guys.

**Sean Linehan:** How are you guys? Good man. How are you?

**Elvis Goren:** Not too shabby.

**Sean Linehan:** Not too shabby.

**Kyle Gaudreau:** The tourists in SF in their shorts and t-shirt and flip flops — you're like, "Oh, you are not gonna have a good time." They think it's gonna be California.

**Sean Linehan:** No, sir. It's gonna be San Francisco. You always know because there will be entire families wearing matching sweaters that they bought at some resort.

**Kyle Gaudreau:** Good to catch up again. Kyle's been having some things to take care of, but fortunately had a chance to reconnect.

**Sean Linehan:** I have a two-month-old who's not super healthy, so I understand. Life gets in the way sometimes.

**Elvis Goren:** Yeah, let's jump into it.

**Elvis Goren:** So basically just some catch up, Sean. I guess you had a chance to look at the article. Any other things that you noticed?

**Sean Linehan:** Well, some of the explore page links — those are custom workshops we created for single customers. To the public, they're technically discoverable, but we don't really have any expectation they'll be found or used. We probably just want to remove the explore page backlinks and cross-linking.

**Sean Linehan:** Otherwise, it was pretty good. The content quality was impressive.

**Elvis Goren:** I ran some content from existing Exec pages and tried to get AI to mimic that tone. I was wondering where this new content is going to live on the site.

**Sean Linehan:** Good question. Let me show you where this is going.

**Kyle Gaudreau:** This is part of what we wanted to talk through. There are a few different approaches. For many clients, we start with a blog-based approach while we validate signals, then we can create templates for programmatic generation.

**Kyle Gaudreau:** There's friction in creating new templates, and we need to know: is this content actually going to rank in volume? So in the early phase, we get signals, learn, and ask ourselves, do we feel confident? When we do, do we double down and create a different experience?

**Kyle Gaudreau:** The other element is what search tells us — what type of content will be more effective than others. I thought you had some apprehension around blogs?

**Sean Linehan:** No apprehension around blogs at all.

**Sean Linehan:** It all lives here on exec.com/learn. Let me show you the structure. Everything will be organized through the redesigned entry point with series and categories relevant to the buyer's journey. These are the series — content is organized into categories and subcategories that can all be cross-linked. Articles have dedicated pages, and if an article is in multiple series, we show previews of related articles at the bottom for cross-linking. Everything is managed and published in Contentful.

**Kyle Gaudreau:** This Contentful setup looks robust. I was telling some folks recently about the sophisticated stuff we've seen built on this platform.

**Sean Linehan:** Our system has really powerful capabilities. Everything is powered by our React app. We have rich cards, an AI builder for configurable GPT queries, a resume writer (you paste in a job description and it generates a resume), video embeds, and callout cards with different styles — blue for default, yellow for warning, green for success. We use these for controversy statements ("Some say X, others say Y") or mid-article upsells. All of this is configurable in Contentful.

**Elvis Goren:** How does the AI part work? What's going on in the backend?

**Sean Linehan:** I'll walk you through it. The resume writer has a title, subtitle, and user prompts like "What job are you applying to?" and "Share your work experience." Users can enter long or short answers, which save in local storage. Then there's a system prompt that goes to GPT: "You're a job search coach. The user previously shared their experience, now synthesize that into a resume." We use few-shot prompting with placeholders referencing the user's answers, and a backend system stitches it all together. We currently use GPT-3.5 Turbo but should upgrade to GPT-4.

**Elvis Goren:** These GPT bots are super impressive. How hard would it be to build something like this?

**Sean Linehan:** It's actually trivial. You just need solid prompt engineering, but it's not that complicated. These bots are totally configurable — we have resume writers, a professional tone rephraser, resignation letter generators. They're reusable across articles, so once you build one, you can plug it in anywhere. We also have a feedback rating system for tuning.

**Kyle Gaudreau:** You've obviously built something incredibly sophisticated here. The combination of Contentful configuration plus your custom system that makes it smart is really elegant.

**Kyle Gaudreau:** How do you split the instances between Placement and Exec? Is it a separate Contentful instance?

**Sean Linehan:** It's the same piece of software and database. We just use exclusion flags in the sitemap. By default, content publishes to Exec with Exec as the canonical, while Placement isn't published. We can tweak this per-article if needed.

**Kyle Gaudreau:** You clearly know what you're doing, but we have some really deep technical SEOs who could do a full audit and identify anything that might be flying under the radar. I'd love to loop in Enica — she's excellent with technical SEO.

**Sean Linehan:** I appreciate that. I've done the Lighthouse and Core Web Vitals testing, and we're in good shape overall.

**Kyle Gaudreau:** One thing we should do — the Learn section isn't in your top navigation yet. Adding it signals to search that this is an important section you're investing in. It's a small signal, but it helps.

**Sean Linehan:** Completely agree. I can add that back quickly. It's trivial to put it in the top navigation.

**Elvis Goren:** Have you provided CMS access to our team yet?

**Sean Linehan:** I haven't yet. I was waiting to hear who would be getting access so we can do some training. The interface is complex overall, but the basics are pretty straightforward. I actually have a training guide I made for my last content person — it looks pretty accurate still.

**Kyle Gaudreau:** If that's up to date, we can start with that and ask follow-up questions as we go. Elvis or Daniel would be the right person to get trained. We'll get them access and they can start publishing. For now, we'll keep this human-led while we ramp up, but longer term I'm exploring auto-publishing integrations.

**Sean Linehan:** That makes sense. We looked at AirOps, which has an auto-Contentful integration, but there's not many CMSs people use at scale — Contentful, Sanity, and maybe Framer, though Framer isn't really a traditional CMS. Webflow also has a proper CMS these days.

**Kyle Gaudreau:** For us, it's Contentful, Sanity, and Framer. Those three cover a lot of ground. Anyway, we're solid on the calibration side.

**Sean Linehan:** I was honestly expecting to be less impressed. What model are you using for the final article? It looked like GPT-4 or O1 because the writing wasn't goofy like typical GPT output.

**Kyle Gaudreau:** I don't actually know the latest version because Daniel's been updating the workflow. It's changed a bunch. Marcel showed me the whole process, and it goes through multiple revisions before the final.

**Sean Linehan:** The final compilation is really good from a tone perspective. Most GPT writing, I can immediately spot that it was written by an AI — it has very particular sentence constructions and words. I didn't feel that way with this article, which I'm really happy about.

**Sean Linehan:** Love it.

**Elvis Goren:** It's very encouraging.

**Elvis Goren:** It looks like just O1, I'm not mistaken.

**Elvis Goren:** Good, so I have another article I worked on today with a couple of variations. I'll fix the explore page links and get them ready. So we're looking to ramp up to 5-10 articles next week?

**Kyle Gaudreau:** Yeah, that's the target range. We have the capability to generate articles quickly, but we don't want to inundate you with tons of fixes. We're looking for that balance. We'll start with two calibration pieces, then ramp to 5-10 next week depending on your feedback. The goal is roughly 1200 pages annually — that's about 25 a week — so we ramp up to that level and keep it quality.

**Sean Linehan:** When should we start getting these published with graphics?

**Kyle Gaudreau:** ASAP on the two we have now. Let's get those live next week. We need to dial in the image strategy — do you want to reuse existing images or create new ones for each article?

**Sean Linehan:** We create new ones each time. We have some existing styles for Exec and Placement, but I'm not super attached to any particular style. It depends on what you can create.

**Kyle Gaudreau:** We typically start with Midjourney to see what works for your brand. Not all clients love the result — sometimes the colors or vibe doesn't feel right. For some clients, we take the repeatable brand elements like iconography and use those as the wrapper, then let AI generate the middle, which helps us scale while staying true to the brand. We're actually hiring a creative lead this week to help build a better process since this is becoming a key friction point.

**Sean Linehan:** Every client has different needs. Ours were made by a designer years ago, and honestly, I'm not super attached to them. The vibe feels off compared to our new website design. We're not precious about it, though.

**Kyle Gaudreau:** I really like your new website's color palette, by the way. Definitely worth complementing that.

**Sean Linehan:** Thanks. We spent a lot of time on it. Do you have images that match the new design for blog posts yet?

**Kyle Gaudreau:** Not yet. Let's see how far we can push Midjourney. The goal is to reduce friction, get things published, and gather signals. It doesn't have to be perfect on day one. We can always go back and refine later.

**Sean Linehan:** Especially for abstract or vector art — Midjourney is pretty good at that stuff.

**Kyle Gaudreau:** Sweet. Elvis and Daniel can take that back and work on the approach. That all looks good.

**Elvis Goren:** Just to confirm — you're going to share the CMS training guide via Notion with team@growthx.com, right?

**Sean Linehan:** Yeah, I'll share it. Just a heads up — it has some irrelevant stuff in there too, but the core is solid. You can share with team@growthx.com so everyone gets access.

**Kyle Gaudreau:** Perfect. I imagine it wouldn't be hard to create new segments within your learn section as we propose new content categories. Just let us know what structure makes sense.

**Sean Linehan:** Creating new series and categories is trivial. It's all configured in Contentful. We can easily nest series and create cross-links.

**Kyle Gaudreau:** That makes things simpler.

**Sean Linehan:** One technical note — we don't use H1 tags in the article body because the article title is the only H1. In Contentful, we follow a convention of only using H2 and below for content headers. The article title as H1 is all that really matters for SEO.

**Kyle Gaudreau:** That makes sense — since the article title is tagged as H1 at the page level, that's what counts.

**Sean Linehan:** Exactly. We spent a lot of time building this system because it was actually a core product experience for us. We have guides integrated into our internal training programs with read receipts so we can track progress. It's become a much better CMS than most off-the-shelf options.

**Elvis Goren:** One last thing — do you have any specific CTA instructions for the article content? Like what you want in the closing sentences or sidebar CTA?

**Sean Linehan:** Good question. We have a sidebar CTA feature on each article — it's configurable with a title, description, and button. You just set it and publish. No staging environment though — it goes straight to production, so be careful when hitting publish.

**Kyle Gaudreau:** Direct-to-production feedback loop is actually a benefit. You catch issues fast and fix them immediately.

**Sean Linehan:** Exactly. We have Contentful set up so you just adjust the content and republish. It updates the server, database, and cache instantly. No staging headaches.

**Sean Linehan:** You've built something incredible. I've been thinking about how we can leverage those GPT bots. When we first built ours, GPT was expensive so we had a wallet system with 500 free runs a day. Now that it's dirt cheap, we removed it. The cost of intelligence is approaching zero — you see that in our 80% margins. That human touch is what commands premium pricing. Even if the operational cost is $1, the fact that someone talks to you on Zoom instead of filling out a form means you can charge $1,000.

**Kyle Gaudreau:** Exactly. We automate to reduce friction, but it's not automation for its own sake. It's about freeing up space for creative thinking. These conversations — brainstorming with you — that's what the automation enables.

**Sean Linehan:** And that's how we run Exec too. We automate the AI role-plays, but then we have a head of learning review them to make sure they're actually fun. The manual tweaks feed back into the system, so over time it generates better ones automatically. But you always need that human layer.

**Kyle Gaudreau:** We're actually planning for significant growth — heading toward 70-80 new hires over the next few months. We're getting investment and have big news coming soon.

**Sean Linehan:** That's awesome. Just don't drop the ball on Exec.

**Kyle Gaudreau:** No, we won't. That's the focus.

**Sean Linehan:** I'm pumped to get started. Thank you guys for your time.
