# Rapyd <> GrowthX Weekly Sync

<metadata>
date: 2025-04-23
time: 17:31 UTC
duration: 31 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Mark Stiltner, Jakub Rudnik, Nicolette Mychajluk
fathom_recording_id: 58801114
fathom_url: https://fathom.video/calls/282441076
share_url: https://fathom.video/share/MN24KJqWhMFY8HUp_PBk3sW52BtthWfw
source: fathom
enriched_on: 2026-03-04 22:15 UTC
</metadata>

---

## Summary

Rapyd and GrowthX reviewed content production progress (6 published, 5 ready for review, ramping to 7/week) and diagnosed a critical GA4 tracking bug showing a 98% traffic drop in April (from 33,596 users in March to 7 in April). The team explored automating blog uploads via WPML plugin with CSV/API integration, agreed that Rapyd should track first-touch blog conversions alongside last-touch attribution to measure content's impact on the sales funnel, and discussed shifting blog image sourcing from generic stock photos to lifestyle imagery featuring Rapyd's customer personas.

---

## Context

Rapyd is a fintech payments platform and a GrowthX client six weeks into a content marketing engagement. GrowthX is producing blog content targeting fintech operators, payment professionals, and mid-market finance leaders — with the goal of capturing search traffic for payment-related keywords and eventually converting readers to qualified sales leads. This is an active content ramp, with Rapyd's editorial team (Mark Stiltner leading) and GrowthX's delivery team (Aida Knežević leading) coordinating weekly on production velocity, performance measurement, and workflow optimization. The engagement includes not just content creation but also measurement strategy and progressive optimization of image, copy, and distribution approaches to match Rapyd's brand.

---

## Relevance

**To GrowthX Delivery:**
- Content production is on track — 6 published with 5 ready for review and ramp to 7/week validates the content engine and delivery process
- CTA customization (adapting provided templates per article topic) adds a new QA layer that will improve conversion relevance across the blog
- WPML + CSV automation opportunity could become replicable playbook for other clients if GrowthX IT integration succeeds
- Image sourcing shift from generic stock to lifestyle photography matching customer personas demonstrates brand-integrated content approach

**To GrowthX Business Development:**
- Week 6 parity with comparable clients suggests strong account health and execution on a strategic ramp
- Strong communication and weekly cadence indicate good account management and potential for expansion (Nicolette added as new reviewer, signaling Rapyd's growing internal investment)
- Multi-touch attribution discussion (first-touch + last-touch blog conversions) shows Rapyd is thinking about content ROI, setting up data for upsell on performance analytics

**To CheckThat:**
- GA4 traffic drop investigation surfaced a potential platform-wide reporting issue (Jakub noted seeing this with other clients), worth tracking as pattern for CheckThat AI visibility audits
- Rapyd's focus on organic first-click conversions aligns with AEO strategy — organic traffic dominates the blog mix (85–95%), giving GrowthX AI visibility metrics direct impact on Rapyd's KPIs

---

## Overview

- 6 articles published so far; 5 more ready for review; ramping up to 7 articles/week
- GA4 tracking issue discovered for April; needs investigation and fixing
- Exploring WPML plugin for automated content uploads to reduce manual work
- Adjustments needed for blog post images to better align with Rapyd's brand

---

## Key Topics

### Content Production and Review

  - 6 articles published; 5 more ready for review
  - Ramping up to 7 articles/week for next batch
  - Next week's content tailored to recently shared documents
  - CTA incorporation: Will customize provided CTAs to fit each article's topic

### Performance Tracking

  - GA4 issue: Dramatic drop in April traffic (from 33,596 users in March to 7 in April)
  - Mark to investigate and fix GA4 tracking problem
  - Rapyd to track "first page blog then converted" metric, from initial visit to closed deals
  - Consider tracking both first-touch and last-touch attribution for blog conversions

### Content Upload Automation

  - Exploring WPML plugin for automated uploads using CSV files
  - Potential API integration to simplify the process
  - Mark to discuss further with IT teams from both sides

### Blog Image Improvements

  - Current process pulls stock photos from Unsplash or similar sites
  - Rapyd prefers lifestyle imagery representing their customers (e.g., business people with a cool, quirky twist)
  - GrowthX to adjust image selection process to better align with Rapyd's brand

### Blog Pruning and URL Structure

  - Jacob shared a spreadsheet for blog pruning (via Slack)
  - Initial review needed to identify irrelevant or low-performing content
  - '/insights' URL structure performing poorly compared to '/blog' - advised to keep all content under '/blog' for better SEO performance

---

## Action Items

**Mark Stiltner (Rapyd)**
- Fix GA4 tracking issue — investigate April traffic drop (33,596 to 7 users), consult with web manager on potential reporting bug or tracking code issue

- Add Nicolette Mychajluk to recurring meeting invite and Airtable access

- Schedule meeting with GrowthX IT (Kirkland) to discuss CSV file integration and WPML API automation for blog uploads

- Review blog pruning spreadsheet from Jakub Rudnik — mark questionable entries based on GSC and SEMrush data (ran in March, not affected by April GA4 issue)

**Aida Knežević (GrowthX)**
- Incorporate provided CTAs into blog posts, customizing language to match each article's topic and preceding section for natural flow

- Discuss with Daniel about implementing AI-generated lifestyle images (not stock photos) for blog posts matching Rapyd's brand style — people-focused, quirky, diverse representation (Southeast Asian/Indian representation priority)

---

## Transcript
**Mark Stiltner:** Thank you everybody.

**Aida Knežević:** How's it going?

**Mark Stiltner:** Good. I'm doing good.

**Aida Knežević:** How's your week going? We, I saw that you guys published six of our articles so far. So, off to a good start. I uploaded them into our local performance report, but it doesn't contain any data yet. For next week, we can, we're going to start seeing some data coming.

**Mark Stiltner:** Yeah, had a couple of questions on the looker performance just in terms of how it was structured and how it was it.

**Mark Stiltner:** So, that was one of the things I wanted to cover. What are your questions?

**Mark Stiltner:** We'll just jump right into that. So, let me pull up here so that I'm looking at it. So, it's a pretty general looker report right now. It's not specific to your blog. If I go to, like, weekly performance in here. You've got it just locked down to your blog URL. Now we'll start seeing that.

**Aida Knežević:** So, then for your URLs, we're going to be tracking clicks and impressions. So, the clicks and impressions of the first page is just Google search console data. So, that's just organic traffic. The next page is page two.

**Mark Stiltner:** This is page two of the URL. I think it's going to be referral traffic from AI, right? Exactly. Which is interesting to see.

**Mark Stiltner:** So, I actually had a question related to your GA4. I was looking at trying to find your current blog traffic. Usually I go to Acquisition > Traffic Acquisition, and I try to type in blog. Nothing really shows up. But I can give you a shortcut — go back over to your left menu, scroll down, click on Rapyd.net Traffic, then slash blog. You should have blog traffic there. I've been using this myself a day or two ago.

**Aida Knežević:** Yeah, because this is what I was looking at too.

**Mark Stiltner:** Let me go in there and see what I'm doing that you're not. Okay, something's gotten screwed up. I was just worried that maybe the tracking code broke. Give me a second here. I think if something's happened just recently in April. If I get Traffic Acquisition report and do April, I see four visitors to my website. That's really, really weird. Okay, so yeah, we've somehow gone off. I'm going to go to home and look at active users. In the last 30 minutes, I'm still seeing 167 active users on the site, so I don't know what's happened.

**Aida Knežević:** It could be a reporting issue. Because it's interesting in the looker report when you go to the LLM traffic summary for the last four weeks, there's just like a huge drop-off in referral traffic. Like right here, eight sessions per week, then a hundred sessions per week, and then it just goes dramatically down. That's just too big of a drop-off to actually be real. Somehow in April something's gone off on my traffic.

**Jakub Rudnik:** Yeah, okay, I got to figure that out. I feel like I've seen that with at least one other client. I'm trying to figure out if I can find it right now, but something with the LLM traffic, I've seen that drop. Maybe I'm remembering this one specifically, but I think I've seen it elsewhere and I'll try to replicate it if I can. I can't tell if it's a reporting issue or lag, but I don't know if there's something there, so I'll see if I can.

**Mark Stiltner:** We haven't changed anything on my end in April that I can think of, but it does look like something has gone wrong in GA4. If I can look at my home page and see there's 168 active users on the site right now, and then I do a traffic report and see four total users on the site, something's gone off. Yeah, there could be a filter somewhere. This is very odd. Let me look at March traffic — 33,596 total users. If I switch to April on the traffic acquisition report and apply that filter, it drops to seven. So something broke somewhere. I'm gonna have to go in and figure out what's going on there. I'll ping my web manager and have him get on it.

**Aida Knežević:** I noticed it in the Looker report that I couldn't pull any data for April, so that's when I started looking into this. I'm sure it's hopefully not going to be a big issue.

**Aida Knežević:** So go to go back to just the content real quickly.

**Aida Knežević:** We do have five articles that are ready for review, but this week, so the content that's in production this week, we're ramping up to seven.

**Aida Knežević:** So next week you'll have seven articles for review, just to give you like a heads up.

**Aida Knežević:** And the batch that we work on next week is going to be tailored according to the documents that you shared this week, because we already started the content like Monday.

**Aida Knežević:** And then one quick question regarding the CTA's.

**Aida Knežević:** And then one quick question regarding the CTAs. Yeah, so I had a question. You wanted us to incorporate it into the blog. Are you going to have conversion blocks and templates the way your existing conversion panels do, or do you just want us to copy and paste these?

**Mark Stiltner:** I think there's two ways you can do it. You can copy and paste it in. Or if you want to get more sophisticated, I think Jakub did mention maybe using these as guidelines and having your system sort of customize it or tailor it for each blog. So I was going to kind of leave it up to you if they should just be copied and pasted in or if we should kind of customize them.

**Jakub Rudnik:** If I'm taking this and then repurposing slightly or tweaking to the exact title topic would be my ideal state. So it's like using this as parameters and then modifying some language to make it feel like it really belongs in that article and not just in that cluster.

**Aida Knežević:** Yeah, that's not going to be an issue. I think that most, if not all of the articles that we've done so far mention Rapyd explicitly and mentioned certain features or capabilities. So we could take these and tweak them so that they flow naturally from the preceding section and maybe also refer to the specific topic of the article. That's not going to be a big lift, so we can definitely do that. I actually prefer having something like this. It makes it easier to incorporate it into the content and make sure that it's accurate.

**Mark Stiltner:** Yeah.

**Mark Stiltner:** So to do list item for me is fix GA4, and to do item for you is to incorporate those CTAs. I was going to say, Nicolette, do you have access to our Airtable?

**Nicolette Mychajluk:** I don't think I have access.

**Aida Knežević:** Would you all share that with her and add her to the recurring meeting invite?

**Mark Stiltner:** And will you also add Nicolette to the recurring meeting? I added her manually today. Okay, Nicolette is going to help me out with some of this stuff. The next action item I had for you guys was an update on how we want to integrate automation of these posts.

**Mark Stiltner:** Okay, so I'll probably have to have a meeting with your IT guy soon, but after looking at the requirements, I think what we're going to be able to do is have you guys turn this into a CSV file, which is what your IT guy suggested. It would basically be mapping columns at the top with where the content goes on the blog. We were looking at the easiest way to do it might be using a plugin called WordPress Multi Language (WPML). Interestingly enough, we do multilingual work with other companies where it enables them to do translations and automatically upload those to our website. We realized we could use that same plugin to just upload English language content to the site. So we might set up an API integration with WPML so that it can be outputted as a spreadsheet and then just automated onto the website without anybody having to do any work. I'm not sure quite how that's gonna work yet. I've got my IT looking into it and I'll have to probably have a meeting with your IT guy again too to just make sure that works. That's what I'm thinking might be a good way to get it in there. It would hopefully reduce the human workload to just outputting a CSV file instead of a Google Doc, and then it's just upload and press the button.

**Aida Knežević:** Yeah, that sounds like a good idea. You would have to discuss that in more detail with Kirkland, but I think that's definitely doable and it's not a huge lift from our end. It actually saves us a ton of time because we usually just do all the manual uploads. So that should be fairly straightforward.

**Mark Stiltner:** And then the only other outstanding item I had for you today. We're going to be doing some reporting of our own, and I wanted to talk about how we coordinate on it. What we're going to be doing internally is tracking a metric we call "first page blog then converted." What that means is the first page they viewed on the site was one of your blog posts, and then from that visit they filled out some form somewhere to get within our lead pipeline. We're going to be tracking that from first page blog conversions all the way to closed deals. That gives us kind of some augmented tracking on top of the top-of-funnel tracking that you're putting in place in Looker. I'll share that document with you — it'll probably be either a dashboard that we create or a Google sheet that we pull from monthly and update. But I wanted to get your thoughts on that top-of-funnel metric. What I mean is having the benchmark be the first page they viewed as the blog and then they converted, versus they came to the site, looked around, and found your blog on the second or third click or something. I wanted to get thoughts on having that be the kind of benchmark.

**Jakub Rudnik:** Yeah, I think that's the right one with any of these blogs. Of course, there should be other distribution plays, but organic is like the blogs — the average visitor, it's like 85, 90, 95% of those come from organic, and then they're first click there, and then they move from there. So that's the bulk of our strategy. Of course, we build into those other distribution channels and things and we want your website to be clickable on those, but we're there to find people who didn't know they were looking for your product and they search something that will eventually lead to that. So that first touch makes the most sense. With different companies, I've seen first touch, and then you have up to 30 days for a conversion. I've seen 90 to 180 days, so it just depends on what you're doing there. That would be interesting and we would want to know that, but you can measure it in a bunch of different ways. Definitely depends on user journey and sales timeline. But someone's seeing one blog, not converting, but then going to another article and converting two weeks later when they've consumed a couple of pieces of content — is that being captured now? I would just want to know how that's tracked.

**Mark Stiltner:** That unfortunately is the one that I really struggle with. Somebody comes and reads one of our blogs, reads 10 of our blogs, and then a month later comes to our website and fills out a contact form. Especially with GDPR rules, it makes it really, really hard to know. So I must just take that as a wash.

**Jakub Rudnik:** I mean, with a metric, the data in general is like directional, right? We're gonna be missing conversions. We only have the data we have, and so we just have to work with that. That's what it is. There's always just gonna be unattributed stuff. I do think it's worth knowing the last touch too — someone comes in elsewhere and then they click around and the blog converts from there, still useful. So I would want that one as well. That first one is like 70, 80% of importance, at least. Everything else is nice to know, supplemental in that general report.

**Mark Stiltner:** So maybe track last touch also.

**Jakub Rudnik:** Yeah.

**Mark Stiltner:** My final action item is some image issues. Let me share my screen. On some of these images, they're not quite right. I'll give you an example. "What is a payment rail guide for businesses?" shows an old school card machine with a ticker tape. That isn't really right for a payment rail because payment rails are typically for digital payments and a lot of times they're bank transfers and things. Another example, "What are ACH transfers?" — ACH is a bank transfer and the picture shows a card. So it's just not quite right. What's the right way to handle this? Is it incremental feedback on each one? Do I just write in here, "Give me a new blog image and here's what's wrong with this one?" What's the process here?

**Aida Knežević:** That's a good question. So the way they work right now, Daniel built a workflow in AirOps that pulls images based on the blog content from Unsplash or another free stock photo website. I could send a message to Daniel and tell him that we might want to start generating AI images that are more illustrative, more lifestyle and lifestyle-focused. I know we've done it for other accounts, so we can do it for you too. I could do that and share some examples with you, and maybe you end up liking those better.

**Mark Stiltner:** Those illustrative images tend to be off-brand for us. We focus very much on lifestyle imagery — things that are not your typical, boring, bland stock photography. If you look at our website's blog right now, we try to find people that represent our customers and just show them. Like this guy — payment facilitators are typically business people. We wanted somebody who was Southeast Asian or Indian because that was underrepresented on our site, and we still wanted him to feel cool because that's kind of the Rapyd brand. We picked somebody we liked and added a t-shirt and blazer, or we find somebody with a smirk and some subtle tattoos — just to set it off a little bit. That tends to be more the Rapyd brand. My preference would be to represent these less tangible concepts with actual people that are representative of our audience, as opposed to arbitrary hacker imagery. I would think that would be an easier ask if you could dial in on the look of the people.

**Aida Knežević:** I think this is definitely doable. It's just an easy fix for us, and the imagery just reinforces your brand. It doesn't have to be super literal. I'll talk to Daniel about this and let you know what he says.

**Aida Knežević:** Do you have anything else you wanted to talk about? I know Jakub, you had that list for blog pruning, but maybe we could take that offline.

**Jakub Rudnik:** I put it in Slack, just did that yesterday. Yeah, take a look through if there's any questions. I pulled from GSC and SEMrush, so I would just want to confirm that there's not some URLs that are missing from WordPress. Like if something truly has zero impressions and zero clicks, it could be missing from that list. But that's part of the sweep — is this relevant or not? That would be really helpful as that first pass. And anything that's questionable, just mark it, and we can do that first prune and then work on what the decision is on each of those, because there's kind of like a decision tree from something that doesn't have traffic but does have a link. I do need to supplement some more data on the conversion side for that decision. But just that first list, you can take a pass through and we'll build off of it.

**Mark Stiltner:** What was your timeframe when you were looking for traffic? Since you just established that my blog traffic is broken in April, did you run it during a good time?

**Jakub Rudnik:** I ran it in March and ran it again in August — two different timeframes, six months apart.

**Mark Stiltner:** Perfect. So neither was during the broken time.

**Mark Stiltner:** Final question for you, we're doing some AI-generated blogging also.

**Mark Stiltner:** And to keep track of it better, I started using slash insights instead of slash blog for those articles.

**Mark Stiltner:** I started generating AI blog posts under slash blog URLs.

**Mark Stiltner:** And those have actually done really well.

**Mark Stiltner:** But the ones that I've done under slash insights have done poorly, comparatively, even though it's the same content with just a different URL chain.

**Mark Stiltner:** Can that URL in the slash bloggers and slash insights impact that?

**Mark Stiltner:** Yeah, 100%.

**Jakub Rudnik:** Yeah, 100%. All the equity — both topical relevance and topical authority that you've built under blog, plus any links that are attached to that subfolder — links power your whole domain. But they also power subfolders and subclusters that are URL structured. All that stuff, you're basically restarting the wheel there. I would double check things like sitemaps and make sure everything's indexed too, just in case. But just in general, especially if there's not a difference in topics, I would just keep them on the blog. You're probably losing power there and it will be slower. It may ultimately be fine, but you'll see slower results.

**Mark Stiltner:** That's helpful because I really did see a discrepancy between same archetypes published on slash blog versus slash insights. I didn't think it would matter beyond the domain.

**Jakub Rudnik:** Yeah, good to know.

**Mark Stiltner:** That's all I got today, guys. I'm going to get into these articles. Nicolette, I'm going to be talking to you and Vanessa about helping me review some of these articles, which is one of the reasons why I wanted to have you on these calls moving forward. Thanks, everybody. In terms of ramp-up progress, how are we doing comparative to your other clients and in terms of your expectations?

**Aida Knežević:** So right now we're on week six. In terms of publishing, I think we are one week behind normal, but that's normal considering the CMS stuff. You're pretty much on track. It's not a big issue. The most important thing is that we've started publishing.

**Mark Stiltner:** Okay, we'll get into these ones that are ready to be reviewed then. Thanks, everybody.
