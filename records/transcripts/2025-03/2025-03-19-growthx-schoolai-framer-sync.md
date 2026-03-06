# GrowthX / SchoolAI Framer Sync

<metadata>
date: 2025-03-19
time: 19:02 UTC
duration: 23 minutes
organizer: Jenn Peters (GrowthX)
participants: Jenn Peters (GrowthX), Deya Bhattacharya (GrowthX), Colton Taylor (SchoolAI), Nikki Muncey (SchoolAI)
fathom_recording_id: 52773462
fathom_url: https://fathom.video/calls/254749190
share_url: https://fathom.video/share/bzuGAZd2v_vYQCrVWaxQr2VxE-kqbpzs
source: fathom
enriched_on: 2026-03-04 15:32 UTC
</metadata>

---

## Summary

Colton Taylor walked the GrowthX team through SchoolAI's Framer CMS, establishing the content publishing workflow where GrowthX writes drafts, SchoolAI's education and marketing team vets for resonance and performance, and SchoolAI's creative director generates on-brand tile images before final publishing. The team agreed to coordinate via a shared Slack channel and established that Jenn Peters will track all published URLs weekly in Looker Studio for performance monitoring. SchoolAI is simultaneously undergoing a website redesign and positioning exercise ahead of their Series A announcement on April 2nd, with detailed brand guidelines coming within weeks.

---

## Context

SchoolAI is an education technology company building personalized learning solutions. GrowthX is providing content marketing services, writing blog posts and long-form content for SchoolAI's resource center. This meeting was the first technical walkthrough of SchoolAI's content publishing infrastructure—the Framer CMS where GrowthX will submit drafts. The context for this meeting reflects SchoolAI's growth stage: they're preparing for a Series A announcement on April 2nd, which means their positioning, website design, and brand messaging are all being refined simultaneously. This creates urgency around establishing clear, repeatable content workflows before the rebrand launches.

---

## Relevance

- **To GrowthX Delivery:** Clear, repeatable content submission workflow via shared Slack channel. GrowthX writes drafts; SchoolAI handles creative (tile images), internal vetting with educators, and final publishing. CMS fields are straightforward (title, author, body, tags, meta description). No complex build-out required on GrowthX's end. Weekly URL tracking in Looker Studio is a lightweight reporting requirement.

- **To GrowthX Business Development:** SchoolAI is mid-growth (Series A in April) with intentional hiring across education and go-to-market talent. Strong emphasis on SEO and content performance (Colton mentioned SEMrush benchmark anxiety). Potential for expanded scope as the resource center grows (webinars, podcasts, press coverage). Contract likely has upsell opportunity post-launch if performance metrics are strong.

- **To Content Strategy:** SchoolAI's audience is educators and school administrators. The internal vetting process with former educators ensures content resonates in K-12 context. Key takeaways and table of contents are under consideration for list-style posts. Main CTAs are "Sign up for free" and "Request a demo." Brand style guide and tone documentation shipping within weeks—will enable more aligned content generation.

---

## Overview

- SchoolAI is building a full resource center, including blog posts, webinars, podcasts, and press media
- Content goes through internal vetting process with former educators and marketing team before publishing
- SchoolAI is undergoing website redesign, positioning/messaging update, and preparing for Series A announcement on April 2nd
- GrowthX to use Slack for notifying SchoolAI team of ready articles; SchoolAI handles image creation and final publishing

---

## Key Topics

### CMS Structure and Access

  - Blog posts accessed via SchoolAI project \> CMS \> Blog
  - Fields include title, author, tile image, tags, and body content
  - Extra image fields exist but not currently implemented in design

### Content Creation Process

  - GrowthX writes initial drafts
  - SchoolAI's content marketing team (former educators + marketing) reviews for resonance and performance
  - Creative director creates on-brand tile images
  - SchoolAI team handles final vetting and publishing

### SEO and Tracking

  - Meta descriptions and tags used for SEO
  - Two main CTAs: "Sign up for free" and "Request a demo"
  - GrowthX to track published URLs in Looker Studio weekly

### Upcoming Changes

  - Website redesign in progress
  - Positioning and messaging exercise underway
  - Detailed style guide, tone, and voice documentation coming soon

### Content Formatting

  - Basic HTML formatting (headers, bullets) available in CMS
  - Considering adding key takeaways section to articles
  - Table of contents may be implemented for list-style posts

---

## Action Items

**Jenn Peters (GrowthX)**
- Track published blog post URLs in Looker Studio weekly and update before weekly sync with SchoolAI team

**Colton Taylor (SchoolAI)**
- Define clear ownership among Colton, Nikki, and Cam for content publishing workflow (scheduled for Friday meeting with growth/demand-gen/performance marketing teams)

---

## Transcript

**Jenn Peters:** Hey, everyone. Thank you so much for taking the time to give us the Framer walkthrough. I'm super excited because I was watching a little demo video from one of our other accounts and I was like, whoa, that's exactly what we need.

**Colton Taylor:** It should be pretty straightforward. Jenn, this is your meeting, so you tell me if you want me to jump in right away and show you around, or if there's anything else you need at the beginning to provide context.

**Jenn Peters:** Yeah, honestly just diving in. I think that's probably the best way. I have a couple of questions, but I'm guessing all of those will be covered through the walkthrough.

**Colton Taylor:** Perfect. So I think I added you, and you do have access.

**Jenn Peters:** Yeah, I've been in and looked around.

**Colton Taylor:** Cool.

**Colton Taylor:** So the SchoolAI project is where everything will be housed. Pretty straightforward as far as getting to the blog. We're building a full resource center—right now these are just long-form blog posts, but it'll include webinar replays, podcasts, and press media. Accessing the CMS is easy: go to the SchoolAI project > CMS > Blog, and there you are.

**Jenn Peters:** Easy.

**Colton Taylor:** When you create a new item, it populates with all the different fields: title becomes the slug, author, tile image, tags, body content. On the author side—we haven't fully aligned internally, but there are a lot of authors across the SchoolAI team. Some are educators. We hire intentionally across two realms: former educators and excellent technologists, go-to-market people, developers. That balance is something we care about.

When you send us a draft blog post, what we do is set up a content marketing Slack channel with our former educators and marketing team. We say, "Here's this blog post," the marketing team gives it a cursory read, and then the educators read through it from an education lens. Our team—Nikki, Cam, and I—focus on performance and keywords. They focus on whether it resonates for educators.

On the creative side, Megan leads our brand initiative and handles look, feel, tone, and voice. She'll make sure everything is on brand and create tile images. We also set tags—good ones are "student outcomes," "student success," "personalized learning." Almost everything we do is around those two things. Those tags are configurable and searchable on the front end.

What else is important for you to know?

**Jenn Peters:** A lot of my questions are around the flow of how we'd be uploading and what happens on your end versus what we do. For fields, I think you've covered everything except where meta descriptions go. And I'd love to know about text formatting preferences for headers and style.

**Colton Taylor:** The meta description has a field—let me figure out exactly where for you. The extra image fields exist in the CMS but we haven't built a place for them to land on the canvas yet. We thought about using them for research projects with charts, but that's a future thing. We're in the middle of a website rebuild right now.

**Jenn Peters:** That's okay. We can reference a published post to understand the formatting. Headers, H2s, bullets—it looks really easy. I do have a question about CTAs and parameters in URLs. We've been using "Sign up for free" generically, but if you have different CTA links for different use cases or want to track where traffic comes from, I wanted to check what we should be using.

**Colton Taylor:** We don't have anything up and running yet. In previous companies, we'd run different logic for blog posts—parameters on the form to pass through to the demo request form, so we'd know what's generating demos. Right now, we really care about two CTAs: "Sign up for free" and "Request a demo."

**Jenn Peters:** That's what we've been using. Good to confirm.

**Deya Bhattacharya:** I have a quick question about the extra images. Once we populate all the fields, do we keep it as a draft, or what's the process for submitting it to you?

**Colton Taylor:** To me, it makes sense to use the shared Slack channel with GrowthX. Drop the articles in there and tag the three of us—the SchoolAI stakeholders. Let us know articles are ready. We run them through our internal vetting process with the education team and pass them to our creative director for tile images. While the team is vetting, she'll be generating the image. Then we publish.

**Deya Bhattacharya:** That makes sense.

**Jenn Peters:** One thing we need to make sure of: whoever publishes needs to mark it as published in Airtable so I can pull all the published URLs and feed them into Looker Studio for weekly tracking. Maybe we could do this once a week before our weekly sync.

**Colton Taylor:** Tag all three of us to start—that's important. We'll have a clearer owner as we define it. The three of us have an hour blocked Friday to identify clear owners for growth marketing, demand-gen, and performance marketing. There's overlap, and this is one of those areas. You'll have one core point person publishing, but if any of us gets to it earlier, fine. You're using Airtable, right?

**Jenn Peters:** Yeah, Airtable. It's literally just a dropdown menu and plugging in the published URL. Even if you don't have time, you can put it in Slack and I can add it after. We appreciate your patience. This is all new for all of us and we'll be tweaking as we go. Content refreshes will be part of that—going back in and adding images or updating things.

**Colton Taylor:** Key takeaways sound like a good idea.

**Nikki Muncey:** I laughed because that's literally my whole process right now—key takeaways.

**Jenn Peters:** We have some list-style posts that might work with a table of contents at the top. One more question: if a post is published and you want to update it later, can we just click on the individual post and make changes?

**Colton Taylor:** Super simple. I can go in, change whatever I want, hit save, and it goes to draft. Everything below the title slug is published. You'd just drag it back to confirmed state. The core thing is we're moving as fast as possible. I have a SEMrush chart burned in my memory of competitors who got a head start on domain authority and backlinks. It's a nightmare that keeps me up at night. So the more we can do on SEO, the better. We're highly invested in making this really great.

**Jenn Peters:** That's awesome. We were talking to Dave yesterday about programmatic ideas and ways to position topics in Airtable strategically, including worksheet-type topics that are smart and unique.

**Colton Taylor:** All good stuff. One note: Megan and I are doing a big web redesign project in tandem with a positioning and messaging exercise, all leading up to our Series A announcement on April 2nd. We're doing this as a forcing function to get it right. We'll have detailed style guides and tone and voice documentation that you can feed into your content generation model. It'll automatically adjust to our brand. We're weeks away—like two weeks or less.

**Jenn Peters:** That's awesome. It's an exciting time for your company, and we're happy to jump in at this stage.

**Colton Taylor:** April 2nd is the Wednesday before a huge industry event, which is why we chose that timing.

**Jenn Peters:** Thank you so much. This has been really helpful and straightforward. We'll be posting in the channel soon with articles we've already staged.

**Colton Taylor:** We have a few calibration articles done, and more in our queue being edited.

**Jenn Peters:** See you tomorrow.

**Colton Taylor:** Thanks.

**Jenn Peters:** Appreciate it. Ciao.

**Deya Bhattacharya:** See you. Bye.
