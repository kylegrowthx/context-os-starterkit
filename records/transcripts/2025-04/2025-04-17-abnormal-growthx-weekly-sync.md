# Abnormal <> GrowthX Weekly Sync

<metadata>
date: 2025-04-17
time: 17:30 UTC
duration: 23 minutes
organizer: sydney@growthx.ai
participants: Jason Gong, Sydney Go, Jade Hill, Emily Burns, Abdallah AlHakim
fathom_recording_id: 57931538
fathom_url: https://fathom.video/calls/278955712
share_url: https://fathom.video/share/6iqhZXZXC1b3maZiL6K6ySxXKc8FQUXT
source: fathom
enriched_on: 2026-03-04 20:15 UTC
</metadata>

---

## Summary

GrowthX and Abnormal Security reviewed blog performance analytics via a new Looker Studio dashboard tracking impressions, clicks, CTR, and position, with a single GrowthX article already ranking at 1.5% CTR within three days. The team discussed the successful website migration—with minor canonical tag issues being addressed—and confirmed a 4-6 week recovery timeline for any temporary traffic dips. GrowthX demoed AI-driven image and infographic generation using a configuration-based assembly approach (rather than pixel generation), with plans to incorporate Abnormal's updated brand guidelines and ship the capability by week's end to enhance both new and existing glossary content.

---

## Context

GrowthX is delivering a comprehensive content marketing engagement with Abnormal Security, a B2B email security platform. This weekly sync brings together Abnormal's content marketing leadership (Abdallah as lead, Emily on brand/design, Jade on strategy) with GrowthX's product team (Jason leading the engagement, Sydney on analytics) to align on content production, performance measurement, and technical enhancement initiatives. The relationship is in active execution phase—GrowthX has begun producing glossary refreshes and new articles targeting Abnormal's buyer personas (security operators, CISOs), with initial results validating the strategy (1.5% CTR from three-day-old content is a strong early signal).

---

## Relevance

**To GrowthX Delivery:**
- Looker Studio dashboard now live for content performance tracking, with segmentation for GrowthX articles planned. Conversion tracking mechanism still being finalized (GA events vs. HubSpot/Amplitude—Abnormal leaning on GA with some form submission limitations to resolve).
- Content production ramping to 10-15 pieces/week across glossary refreshes, new glossary articles, and blog posts. Currently 5-7 published with strong early CTR signals. Emily Burns (brand) will share updated brand style guide by end of day for AI image generation integration.
- FAQ generation capability flagged as next feature to ship after image/infographic assembly, targeting easier implementation than visual generation.

**To GrowthX Business Development:**
- Strong early account health signal: 1.5% CTR from day-3 content indicates product-market fit in Abnormal's content strategy. Website migration executed cleanly despite minor canonical tag issues (already being addressed).
- Production velocity on track: 10-15 pieces/week target achievable. Abnormal team engaged and collaborative; no friction signals on delivery or brand alignment.
- Expansion potential: Abnormal's emphasis on internal education and AI visibility ("big initiative for all teams") suggests broader organizational buy-in. FAQ generation and visual enrichment of glossary (especially Proofpoint top-10% benchmark referenced) creates opportunity for scope expansion.

**To CheckThat:**
- Abnormal explicitly focused on AI capabilities and internal education—team discussing "how we're doing this stuff under the hood." CheckThat's AI visibility audit and prompt analysis mentioned in context of content enhancement, validating fit for Abnormal's AI-first content strategy.

---

## Overview

- New Looker Studio Dashboard created for blog performance tracking, with plans to segment GrowthX content specifically
- Website migration went smoothly with minor issues; traffic may dip temporarily but should recover in 4-6 weeks
- AI-driven image and infographic generation in development, aiming to enhance content visuals across articles
- Content production ramping up to 10-15 pieces/week, blending glossary refreshes, new glossary articles, and blog posts

---

## Key Topics

### Analytics Dashboard Development

  - Sydney built a Looker Studio Dashboard for overall blog performance
  - Dashboard includes impressions, clicks, CTR, position, and will incorporate conversions
  - Currently showing all blog articles; will be segmented for GrowthX content specifically
  - Sample report demonstrated granular metrics like week-over-week improvements and per-article performance
  - Conversion tracking to be implemented; team discussing best approach (GA events vs. HubSpot/Amplitude)

### Content Production and Performance

  - One GrowthX-produced article ranking so far (take-butching), with 1.5% CTR after 3 days
  - Production goal: 10-15 pieces/week, mixing glossary refreshes, new glossary articles, and blog posts
  - 5-7 articles published so far, with more in the pipeline for quick turnaround

### Website Migration Review

  - Migration executed well, with some metrics showing improvement (e.g., site load speed)
  - Minor issues identified, main concern being canonical tags (team already addressing)
  - Potential temporary traffic dip expected, with full recovery anticipated in 4-6 weeks

### AI-Driven Content Enhancement

  - Developing capability to generate images and infographics for blog/content
  - Current approach: generating configuration for image assembly rather than pixel-by-pixel generation
  - Demo showed workflow for creating relevant images and text layouts based on article topics
  - Plans to incorporate Abnormal's brand guidelines into the generation process

---

## Action Items

**Jason Gong (GrowthX)**
- Share Google sheet detailing migration issues with Abnormal team

**Emily Burns (Abnormal Security)**
- Send updated brand style guide to Sydney Go and Jason Gong for AI image generation integration

**Abdallah AlHakim (Abnormal Security)**
- Check with development team regarding key events for conversion tracking in GA and HubSpot; report back on what's feasible for blog post pages

---

## Transcript

**Jason Gong:** How are you, how's the offsite?

**Jade Hill:** It was nice to see some boats. Got some of the destinations done at a destination, or virtual.

**Jason Gong:** It was in Boston.

**Jade Hill:** So not somewhere like Hawaii.

**Jason Gong:** Yeah, when you say destination, what's the destination?

**Jade Hill:** So we work in a major city?

**Jason Gong:** You said you're in the Bay Area normally?

**Jason Gong:** I live outside Chicago, kind of in like South Bay.

**Jade Hill:** But yeah, I came to travel probably like at least once a month, a lot of times the Bay Area.

**Jade Hill:** She's a Delta super member.

**Emily Burns:** I'm yeah.

**Jason Gong:** It's like fun, but now it's just painful to fly with how much I think it is.

**Jade Hill:** Yeah, and I like to not book my flights. I was just telling somebody here I was flying back from RSI. I waited too long to fly from San Francisco to LA to Minneapolis to my home airport.

**Jade Hill:** That's horrible.

**Jason Gong:** Okay, we got a pretty packed agenda today. Before we kick off, any urgent questions you guys wanted to start with? Otherwise we'll go on.

**Jason Gong:** So today, Sydney will go through some of the stuff she's been building around analytics. You'll have a way to see how the content is performing, some very early results from the few articles we published, and she'll give a quick update on content production. Then I'll cover the migration, which you guys did an amazing job on. We've also done some AI workflow developments. Last week we shipped ingesting your non-indexable stuff, and this week I wanted to show we're pretty close to being able to create images and infographics at scale and enrich a lot of old content.

**Abdallah AlHakim:** I love the video you posted last week. It's good for you to keep posting what you guys are doing, because we're trying to educate folks here on what we're doing in AI. It's kind of a big initiative for all the teams, so it helps me share and helps everybody. It would be cool to see how you're doing that, take a peek under the hood and stuff, so it helps to go deeper.

**Jason Gong:** Yeah, any feedback helps. Okay, let's kick it off, Sydney.

**Sydney Go:** So I built your Looker Studio Dashboard. The only caveat is that most of our articles were published very close to your migration date, so a lot of them haven't been indexed yet. This is your overall blog performance. If there's a specific path that you'd like me to pull this data from, I know you were publishing under Abnormal AI, then there's intelligence and other factors. If you want me to pull from that specific path, we can do that. But this is the overall blog performance, and it'll help us build a baseline for where we want GrowthX content to be contributing to your overall blog performance. We've got impressions, clicks, CTR, position. The version has been set up and we'll hook that up as soon as we have the conversion information. Can you see it okay?

**Emily Burns:** It's a little bit small.

**Sydney Go:** Yeah, let me make it a little clearer before I present. And this is all blog articles, right, not just what you guys have written?

**Abdallah AlHakim:** Correct.

**Sydney Go:** Currently this is all blog articles for the past week. We're going to do this on a week-by-week basis, and you can also see month-by-month here. But we'll set this up so you have overall blog performance, then our stuff, then enriched, with lots of different ways to segment. I built a sample report because we don't have a lot of data yet. You'll have impressions, clicks, and then the number down here shows how it's improved week over week. This will be for GrowthX content, and then you'll have clicks, keywords, pages, list of articles published, per-article performance, and top keywords. At some point, it will all have conversions so we can track it on a more granular basis and see specifically what's working and what's not. We'll also build this out for your refreshes and down the line your new glossary pages. So what do you need for conversion data?

**Abdallah AlHakim:** Do you just need the page path or the link they convert on? What do you need?

**Sydney Go:** Conversion events in Google Analytics. You want whatever one you want. We can do that and attach it to the specific blog posts.

**Sydney Go:** Google Analytics should be tracking that. Do you have something like that, or have you mentioned HubSpot before?

**Abdallah AlHakim:** We do. I'm pretty sure we have GA set up and access to that. If you have a bunch of key events set up, can you tell us which one specifically you want us to focus on? For us, key events usually is phone submissions, any phone submission. Right now we don't have anything tracked on the blog pages. They don't have forms on the page. But I could take a look and start the thread.

**Jason Gong:** I think when I took a quick look at GA, there were quite a few events. GA has some limitations. I'll tell you the page the event happened on, but tracking the progression—they hit that page, they hit the homepage, then they submit a form—is a little bit clunkier to put together. That's why HubSpot or Amplitude helps track it more accurately. With the forms going into Mercato, we can definitely track overall form completions and website events. I'm able to link every blog to something. Let's talk about this next few weeks.

**Sydney Go:** Awesome. The last thing I wanted to show you is that currently only one blog post is ranking because the other ones weren't indexed under abnormal security.ai. We can't see GSC data for abnormal.ai or abnormal security.com yet.

**Jason Gong:** That's just because of the migration. I think it'll take a few days for that to pop up.

**Sydney Go:** Yeah, so I took a screenshot of abnormal security.com's GSC for the take-butchering article. We have 1.5% click-through rate, total impressions. I think this was published three days ago. So we're seeing early results that look good, and hopefully that'll continue.

**Emily Burns:** Just might be a silly question, but I was curious if the articles I've already published that haven't indexed since the migration—would it help at all to unpublish and republish them, or should I just not touch them? They're already indexed.

**Sydney Go:** I'm so glad to be fine with them. We have a link in the meeting doc for your dashboard specifically, and then for the sample report if you want to just see what that would look like.

**Abdallah AlHakim:** That's awesome. And you have a link for the local dashboard there somewhere for us to contact later?

**Jason Gong:** And then there's just production updates. We're trying to have a blend of glossary refreshes, new glossary articles, and blog articles. So we'll keep you updated there. We're ramping it up right now, trying to go for 10-15 a week. Once we tune it, we can adjust from there.

**Sydney Go:** Sorry, quick question before you continue. Emily, when will the glossary refresh have been published?

**Emily Burns:** I'm working on them right now. Should be by end of day today.

**Sydney Go:** Okay, no rush. I just wanted to make sure they live in the same place.

**Emily Burns:** Should I update the Airtable the same way I did for the articles, or is there a way to mark them done or just let you know?

**Sydney Go:** I can use the column that you can fill in.

**Jason Gong:** Cool. For the migration, I think your team did a great job. I saw a bunch of metrics actually improve from it. I don't know if you did stuff to make your site load faster or whatever, but overall it's great. I have a Google sheet that goes over some of the issues. I'd say all of them are fairly minor. The main one I flagged already that I think someone on your team is already looking at is the canonical tag. I won't go into it, but I think you guys already looked into it. I'll share this after. Most of the other issues are very minor. The migration went super well. I talked to Dave on our team. He used to work for a bunch of really big e-commerce brands that care a lot about SEO. He said even if you do a migration really well, sometimes it just takes Google a while to move everything over. You might see a decrease in traffic for a few weeks, but usually it pops back up in 4-6 weeks.

**Abdallah AlHakim:** I'll let them know you guys are impressed with the migration. I'm happy since I know it's been a lot of work and stress over here about this, so it's good to hear.

**Jason Gong:** Okay, cool. So the last part I wanted to show is a little demo. It's probably not done yet, so whatever we actually ship will look a hundred times better. What we're looking into is basically the ability to generate images and infographics for Abnormal within your blog or content. The state of AI generation isn't at a place where anyone should just be using ChatGPT. We see a lot of problems when people try to do that. Generating a picture of a dog is one thing, but trying to generate text that makes sense is different. Trying to generate it pixel by pixel doesn't really make sense right now. One of our customers had someone on their team putting this stuff together. You can see there are some problems. The text, no matter how accurate the prompt is, just gets random things. Text is disappearing or things are weird and blurry. We're making some LinkedIn posts and it just can't get our logo right because they're not generating actual text the same way you would on a web page. We're trying to generate text like pixel by pixel. At least at the moment I think it'll get better. What we're doing is kind of assembling a picture instead of trying to generate the whole thing. We have a language that can describe how a picture should be assembled, like an infographic—what text to use, where it is. It's almost like creating an HTML landing page. You have styling, text, pictures, but they're all separated. Instead of trying to generate the image, we generate that configuration. We have a tool that assembles the image, and then we screenshot that image. We'll have different pieces of this. One is creating the images. For example, this workflow takes the topic of the blog post and generates a relevant image. This is cybersecurity, which is generic. This one is spam email. And we try to follow the style of your website. This one is clone fishing. For a writer, we give them a few options and they pick the one that looks best. This is the image layer. This is the other layer where we look at text. This layer we're generating the text we want on the page and how it's placed. So for example, let's say we want a graphic for this. Sometimes an infographic is just repackaging the text into a graphic. This configuration language for how the graphic should look is like HTML—here's all the text, here's where it is, here's the size. And then we assemble all these things together. Again, this is going to look really ugly, but conceptually, we're taking information, we have the text, we're combining it with the background image perhaps that we generated, adding styling. At the end, you're not trying to generate a whole image from scratch and having weird things happen. You're assembling it. I hope we'll have something we can use starting next week and then add it to the new articles we're generating. If we like what we see there, we can start trying to enrich images, especially with glossary. When I look at Proofpoint, only their top 10% glossary articles have images. We could honestly do it with every single glossary article.

**Emily Burns:** With these, I'm sorry if you said this, but with the new brand style guide we can put the inputs with our specific brand. Did you share that with Sydney?

**Jason Gong:** Not yet.

**Emily Burns:** I'm going to send it over. We have an updated one because of the new design. We can totally dump it all in you guys.

**Jason Gong:** We'll figure it out. If you have random little shapes you like in the background, we can incorporate all of that for the styling.

**Jason Gong:** Cool. So yeah, we're focused on shipping this. Once we're done, the next thing I really want to add is FAQs, which honestly will be easier than this. This was a little harder than I initially thought. At the end of your glossary, you have a few questions that people commonly ask. We're trying to ramp a few writers in our pod so we can push that number higher. How many articles do we have right now, Emily, that we're ready to publish?

**Emily Burns:** We've published five already and I'm updating glossary entries today. I think you sent me a new batch of like 10. That should be a quick turnaround.

**Sydney Go:** I think we may have missed one article for publication—the cybersecurity and AI one. It was part of that first batch, so we did publish six articles. It should be seven.

**Abdallah AlHakim:** Hopefully that will unblock the motions and offers, too, so that'll be good.

**Jason Gong:** Any feedback so far on what we've been doing?

**Abdallah AlHakim:** No, I'm excited to see what gets published. I'll look at the dashboard results for that, and yeah, that'll be exciting. For the key events, I will check with the development team on what maybe we have. I think I've told you the key events we want to track, so I'll see what they have. If they're not on the blog pages, I don't think we'd track too much from that. I'll look into that bit and see. I'm not worried about it yet. It's just more like we should update it to make it more proper.

**Abdallah AlHakim:** Sounds good. Thank you guys much for your work.
