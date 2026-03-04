# Joe -- Pipeline Insights

<metadata>
date: 2025-05-12
time: 17:13 UTC
duration: 18 minutes
organizer: Kyle Gaudreau
participants: Kyle Gaudreau, Joe Lehr
fathom_recording_id: 62073459
fathom_url: https://fathom.video/calls/297109677
share_url: https://fathom.video/share/WvoYj-mUhTzYtxp78WxDpidaZNTYs7VX
source: fathom
enriched_on: 2026-03-03 20:31 UTC
</metadata>

---

## Summary

Kyle and Joe aligned on strategies to enhance pipeline visibility and meeting quality metrics using data enrichment and automation. Joe is building a data enrichment project for Jason that adds triggers like webinar attendance and LinkedIn engagement to customer journeys, with initial focus on qualifying webinar attendees — work that directly supports Kyle's need for enriched lead data (SEMrush metrics, contact titles, website content analysis). They identified three priority metrics for assessing website maturity during meeting prep: organic traffic, SEMrush authority score, and number of organic pages, with Joe committing to automate authority score collection and investigate ways to pull website content data.

---

## Context

Joe Lehr and Kyle Gaudreau (GrowthX) met to discuss operational improvements around pipeline tracking, data enrichment, and meeting qualification. Joe recently started on a data enrichment project for Jason that aims to unify customer data from multiple triggers — webinar attendance, LinkedIn engagement, and other signals — into cohesive customer journeys with automation capabilities. This work intersects directly with Kyle's day-to-day challenge: accessing enriched firmographic and website data when preparing for and analyzing customer meetings. Kyle is responsible for evaluating website maturity and SEO sophistication as part of GrowthX's service delivery, and currently does much of this analysis manually (checking SEMrush metrics, reviewing website structure, looking up contact roles on LinkedIn). They discussed how Joe's enrichment tooling could help automate these checks and surface key metrics in GrowthX's systems (Adio, Slack notifications).

---

## Relevance

- **To GrowthX Delivery:** Kyle uses organic traffic, authority score, and organic page count to quickly assess website maturity and SEO program sophistication during client calls — feeds directly into service scope, messaging, and success metrics. Automating these metrics (e.g., pushing SEMrush authority score via Slack on inbound leads) saves Kyle preparation time and ensures consistency. Contact role/title enrichment reduces manual LinkedIn lookups.

- **To GrowthX Operations:** Joe's data enrichment work may surface automation opportunities across GTM systems (Adio, Zapier, Slack). The shift to Zapier for calendar/email tracking and qualification could change how "no meeting, did not book" leads are counted (one-touch vs. two-touch). Documenting these metric definitions is critical for pipeline reporting.

- **To CheckThat / AEO:** The discussion of website maturity assessment — content types, page distribution, SEO-ified assets like calculators vs. docs pages — represents a core AEO/content strategy signal. Patterns Kyle observes (blog-only sites vs. mature programs with case studies, interactive tools, programmatic pages) inform CheckThat's positioning and competitive differentiation.

---

## Overview

- Implementing Zapier flow for tracking email replies, potentially affecting qualification process
- Exploring data enrichment opportunities (e.g., SEMrush data, LinkedIn info) to enhance pipeline analysis and meeting prep
- Identifying key metrics for assessing website maturity and SEO efforts (organic traffic, authority score, page count)
- Automating data collection to streamline processes and free up team resources

---

## Key Topics

### Fathom Calendar Integration Update

  - Dynamic calendar naming issue persists; workaround involves copying variables from email body to title
  - Switching to Zapier flow may impact tracking of email replies and meeting qualification process
  - "No meeting, did not book" qualification may become a one-touch point instead of two

### Data Enrichment Project

  - Jason's project aims to enrich data from various triggers (webinars, LinkedIn engagement) for cohesive customer journeys
  - V1 focus: Streamlining engagement with qualified webinar attendees
  - Potential to backfill information using SEMrush data, company size, LinkedIn profiles for more comprehensive analysis

### Key Metrics for Pipeline Analysis

  - Organic traffic (monthly basis)
  - Authority score (SEMrush metric for domain weight)
  - Number of organic pages
  - Role/title of meeting attendee (to be consistently included in contact records)

### Website Analysis for Meeting Prep

  - Examine blog content and resource pages
  - Assess total page count and content distribution (e.g., product pages vs. blogs)
  - Look for signs of SEO program maturity (varied content types beyond basic blog posts)
  - Examples of mature content: downloadable case studies, interactive calculators, programmatic pages

---

## Action Items

**Joe Lehr**
- Link additional SEMrush metrics (authority score, number of organic pages) to inbound lead data
- Override contact title/role field in Adio with data from default source
- Investigate ways to automate collection of website content data (blog posts, resources) for analysis

---

## Transcript
**Joe Lehr:** Yeah, all good, man.

**Kyle Gaudreau:** I was...

**Kyle Gaudreau:** Oh, man, it's just been a busy morning.

**Joe Lehr:** My internet's been spotty, so it's been impossible to have a normal conversation.

**Joe Lehr:** I was just talking with Jason about the project — I was going over it with him. He's going to be out, and I just want to get this project with some legs under it.

**Joe Lehr:** Anywho, how are you doing?

**Kyle Gaudreau:** I've been a little under the weather, but, you know, you have kids, you understand how it goes.

**Joe Lehr:** Yeah, man.

**Joe Lehr:** I've been up so early this entire weekend.

**Joe Lehr:** Great Mother's Day, though, so I can't complain.

**Joe Lehr:** It's good.

**Joe Lehr:** I'm going to try and turn on the video, so let's see if I can...

**Joe Lehr:** How was your weekend?

**Kyle Gaudreau:** I was sick most of it, but...

**Kyle Gaudreau:** I was able to still do some things here and there, but I don't know what it is.

**Kyle Gaudreau:** Maybe COVID?

**Kyle Gaudreau:** We'll see.

**Joe Lehr:** Fun. Yeah, that's so fun. All right, well, I apologize.

**Joe Lehr:** Again, Fathom's way late.

**Joe Lehr:** I have a couple things.

**Joe Lehr:** We chatted last week about better clarity into data, pipeline data, right, and qualification.

**Joe Lehr:** I have some interesting thoughts there, but I just want to share some quick updates and then see if you have anything you want to quickly add to it.

**Joe Lehr:** The dynamic calendar naming piece, that's just default being default.

**Kyle Gaudreau:** I kind of figured, yeah, it's all good.

**Kyle Gaudreau:** I mean, it's not a huge deal.

**Kyle Gaudreau:** It obviously would be great to have something dialed in, but it's not terribly urgent.

**Kyle Gaudreau:** But, yeah, so they just, like, have weird things or how they're parsing the data.

**Kyle Gaudreau:** It's not super consistent in there.

**Kyle Gaudreau:** They don't have an answer for me.

**Joe Lehr:** The way that I was told — just copy the dynamic variable from the body of the email and paste it into the calendar title. I was like, okay, I wonder if this works. It looks like it works, but yeah, it's not the most intuitive approach.

**Kyle Gaudreau:** Kind of odd, but this doesn't feel like an edge case, you know? I know you'd expect this as table stakes for a scheduling tool.

**Joe Lehr:** We'll see what happens.

**Joe Lehr:** But, yeah, for the most part, like, outside of that, like, it does appear to be working well.

**Joe Lehr:** I do have to switch over to the Zapier flow.

**Joe Lehr:** That may mean I have to see how the data plays in.

**Joe Lehr:** That may mean that, like, the no meeting, did not book a meeting qualified is a one-touch point, not two.

**Joe Lehr:** Just because I just need to see if we're able to track accurately if someone replies to the email or not.

**Kyle Gaudreau:** Yeah. I mean, we haven't even been getting many of those replies.


**Kyle Gaudreau:** At least I don't recall seeing any replies to me.

**Joe Lehr:** Yeah, one partner did reply. They were disqualified (DQ) but still got back to us.

**Joe Lehr:** We'll see what happens.

**Joe Lehr:** But that's the big piece we're looking at.

**Kyle Gaudreau:** The one I tend to get replies on is from unqualified leads.

**Joe Lehr:** And that email will come out from Owen and the VCC.

**Joe Lehr:** So the sales will be able to see it.

**Joe Lehr:** Okay.

**Joe Lehr:** But was there anything you wanted to add before jumping into pipeline clarity and meeting quality metrics?

**Kyle Gaudreau:** No, I think we're good. We can jump into that.

**Joe Lehr:** So I'm working on this project for Jason — I just started. And it's very relevant to what we're talking about. Jason's project is pretty large, but essentially it's about enriching data tied to different trigger events — like attended webinar, LinkedIn engagement — and adding it to a cohesive customer journey. Then we can trigger automated actions off of that. For example, send an automated email if someone attends a webinar and they're qualified.

**Joe Lehr:** That's a very basic example — it could also be if they're an existing customer and they attend the webinar. We're thinking through those kinds of journeys.

**Joe Lehr:** But for V1, we're just trying to figure out how to get qualified webinar attendees engaged more easily. I use Clay a lot for different customers, and I was playing with some of this basic data and thinking about how it could help with the reporting you're looking to do.

**Joe Lehr:** Because we could backfill a lot of information from SEMrush data — like, what's their organic traffic, authority score, and other interesting data points pulled from their website. I don't know SEO really well, but there are definitely signals there. Then we could use that to run reports — like, show me close-lost deals versus close-won deals and compare them against firmographic data like company size, LinkedIn profile info, and company LinkedIn info. That gives us a much more cohesive story to analyze.

**Kyle Gaudreau:** Where did this entry come from? They're a competitor — actually our biggest competitor.

**Joe Lehr:** Yeah. They attended one of our webinars.

**Kyle Gaudreau:** Oh, the show? Not surprised.

**Joe Lehr:** Some people we didn't accept for the invite, but this person was allowed.

**Kyle Gaudreau:** I don't know how long they attended.

**Joe Lehr:** But when we talk about pipeline clarity, age, and quality — some of this comes from Bruno analyzing the data, but there's a lot of firmographic data and website data we can also pull. There are other sources too that could help us analyze this further.

**Joe Lehr:** The real question is: was this a meeting worth it? I was curious to get your thoughts on that because it was kind of an aha moment for me — this data could be really helpful for your work.

**Kyle Gaudreau:** Yeah, 100%. We have some of it in Adio, but it's been inconsistent. I'd love to automate it.

**Joe Lehr:** I was just looking for screenshots of the website metrics — do you use screenshots in the notes section?

**Kyle Gaudreau:** Is that something Bruno's been putting in?

**Kyle Gaudreau:** I think Alice manually takes a screenshot from the website and drops it in.

**Kyle Gaudreau:** Yeah, I could train Owen to do that, but it feels like it should just be automated. The few things I'd want to look at are: their organic traffic on a monthly basis (which you have), their authority score, and the number of organic pages.

**Joe Lehr:** What's the authority score exactly?

**Kyle Gaudreau:** It's a metric from SEMrush that helps you understand the relative weight of the domain. I'd be surprised if it's not in their API somewhere.

**Joe Lehr:** I was trying to find sitemap URLs, but I'm not sure that's the right approach.

**Kyle Gaudreau:** That's tertiary — there's complexity in where sitemaps are stored, and some companies intentionally hide them. But those three metrics — organic traffic, authority score, and number of organic pages — give me a quick snapshot of website maturity.

**Joe Lehr:** So moving in a day or so, I'm going to push the organic score with inbound leads. We're collecting that data — it was hard to do via API, but using the native integration, it'll show up in the Slack notification. That's one piece. I'll link to the other metrics too.

**Joe Lehr:** Is there anything else you need — website data or contact LinkedIn info?

**Kyle Gaudreau:** Yeah, one other thing — I want to enrich contact titles/roles. I always check manually, but it should be easy to pull.

**Joe Lehr:** The title, yeah.

**Joe Lehr:** It's included in Alerts New Leads — that's the title.

**Kyle Gaudreau:** But we don't consistently have it, that's my point.

**Kyle Gaudreau:** Sometimes we have it and sometimes we don't. It's not a huge deal — takes two seconds to find on LinkedIn — but if we could automate it, I could have the team do other things.

**Joe Lehr:** Where would you want it? On the contact record?

**Kyle Gaudreau:** Yeah, on the person record.

**Joe Lehr:** Adio tries to enrich data automatically, but it's not always successful. You can override fields though. I'll probably override the title field with data from Clay (our default enrichment source), which should be more reliable.

**Joe Lehr:** From an analysis standpoint, when you look at pipeline — close-lost versus close-won deals and the meetings booked — what other data would you want? Just website URLs, or is there more?

**Kyle Gaudreau:** There is, but it's about making it easy and repeatable. Let me figure out the specifics.

**Joe Lehr:** Maybe it's not doable. Totally understand.

**Kyle Gaudreau:** One thing is the number of pages. Another is how much blog content or SEO-like content they have. I typically check that in SEMrush or by looking at their website directly.

**Joe Lehr:** Both ways work.

**Kyle Gaudreau:** Thanks, Joe. Let me show you how I typically do this in SEMrush.

**Kyle Gaudreau:** Here's an example I was looking at earlier. In SEMrush, go to Keywords > Details > Organic, and you get a breakdown. Then click Pages. This one's a small website. Sometimes you see high page counts, but they're mostly docs or customer success pages rather than blog or resource content. We also usually check that against competitors, though that gets complex. That's the high-level process.

**Joe Lehr:** That's helpful. How do you do that directly on a website?

**Kyle Gaudreau:** I look at what content exists outside of product pages. Take Passpool — they don't have blogs or resources. But some companies have both. Looking at their site structure, they have decent blog content. Then I cross-check in SEMrush. Here's a better example — this company has 800 pages, but when you drill in, most are community pages.

**Joe Lehr:** So you're looking for blog and resources?

**Kyle Gaudreau:** Usually. Blog is easiest — almost every site has /blog. Resources is variable. At minimum, I check /blog page count. In this case, about 39 pages.

**Joe Lehr:** What counts as resources? Help Center articles?

**Kyle Gaudreau:** SEO programs can have different content types. Some create unique experiences — maybe interactive or game-like — that signal program maturity. An immature program just has product pages and blogs, nothing else. Like what we just saw.

**Joe Lehr:** So gated content like downloadable case studies is a maturity signal?

**Kyle Gaudreau:** Yeah. Or like Ramp — we did per-game calculator pages for them. That's programmatic content, not blogs. Those kinds of unique assets signal maturity.

**Joe Lehr:** I could pull some of this info. Meeting prep and post-close analysis go hand-in-hand, right?

**Kyle Gaudreau:** Exactly.

**Kyle Gaudreau:** This could be automated in theory, but website structure inconsistencies make it complex. The juice may not be worth the squeeze.

**Joe Lehr:** Totally. Well, we'll circle back. This is helpful — glad I could provide context. I'll work on the data and we can talk about reporting when you're back.

**Kyle Gaudreau:** Sounds good. Thanks, Joe.

**Joe Lehr:** Appreciate it.
