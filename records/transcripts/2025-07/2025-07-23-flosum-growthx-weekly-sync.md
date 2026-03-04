# Flosum <> GrowthX Weekly Sync

<metadata>
date: 2025-07-23
time: 16:00 UTC
duration: 29 minutes
organizer: jessalynn@growthx.ai
participants: Saakshi Jain (Flosum), Beau Beamon (Flosum), Rachel Pasche (GrowthX), Jakub Rudnik (GrowthX), Jessalynn Jones (GrowthX)
fathom_recording_id: 75982048
fathom_url: https://fathom.video/calls/359470132
share_url: https://fathom.video/share/qFM1CDoLTQ8CZnj5WasP3LSzYRvU5v_S
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

GrowthX and Flosum completed a major redirect cleanup that fixed roughly 90% of Flosum's 404 errors by redirecting old blog, resources, and customer story pages to relevant current pages. Jakub committed to providing URL validation guidance using Ahrefs and Screaming Frog tools to support Beau's lead scoring work in Warmly, which has already delivered 7,800 net new leads this year by segmenting de-anonymized traffic by product interest. The team also agreed to restructure their monthly meeting cadence to include one dedicated deep-dive analytics call per month plus a quarterly business review before end of August, with improved Looker Studio dashboards shipping by next week.

---

## Context

Flosum is a DevOps compliance platform that partners with GrowthX for content marketing services. This weekly sync is part of an ongoing engagement where GrowthX creates content and manages reporting while Flosum handles distribution and lead operations. The relationship is now 11+ weeks in, and both teams are optimizing their workflows — GrowthX is improving its analytics dashboards and meeting structure, while Flosum is refining how it segments and scores leads from organic web traffic. The meeting also touched on content production blockers (Webflow bandwidth issues affecting publishing) and new content requests (DORA compliance guides for DevOps).

---

## Relevance

- **To GrowthX Delivery:** Large-scale redirect projects (1,000+ redirects) need phased validation to avoid quality issues. Monthly deep-dive analytics calls unlock content ideation opportunities (lookalike pages for high-traffic content) and content maintenance workflows. Flosum's 7,800 net new leads from Warmly show strong organic demand signals that GrowthX content is driving.
- **To GrowthX Business Development:** Flosum is healthy and expanding — 11+ weeks in with accelerating scope (new meeting cadence, quarterly reviews, DevOps compliance content requests). Lead scoring improvements and NERFA program segmentation indicate account is scaling operationally.
- **To CheckThat:** None directly mentioned this call, but Flosum's reliance on Warmly and lead scoring sophistication suggests potential for CheckThat AI visibility audits for their target audiences (DevOps, backup/archive admins).

---

## Overview

- Redirect list completed by Jakub, cleaning up ~90% of 404 errors; to be re-checked in 2-4 weeks
- Webflow publishing issues encountered; potentially due to bandwidth limitations
- New Looker Studio dashboards in development for improved reporting and insights
- Monthly deep-dive sessions and quarterly review planned to analyze performance and strategy

---

## Key Topics

### Redirect List Completion

Jakub finished the redirect list with about a dozen redirects. They were largely batched quickly, focusing on blog, resources, and customer stories. Low risk due to low/zero traffic on affected pages. Plan to rerun in 2-4 weeks to check for new issues after re-crawling and indexing.

### URL Validation and Segmentation

Beau inquired about URL validation tools for the Warmly platform. Discussion on cleaning up old URLs and redirecting to newer, more relevant content. Exploration of Ahrefs and Screaming Frog as potential tools for URL validation. Importance of segmenting de-anonymized traffic for NERFA programs and lead scoring.

### Webflow Publishing Issues

Rachel encountered problems publishing approved articles in Webflow. Platform kept kicking her out and preventing content updates. Saakshi suggested it might be a bandwidth issue, potentially requiring an upgrade. Rachel to try clearing cookies and attempt publishing again.

### Looker Studio Reporting

Current Looker Studio dashboard not functioning optimally. New dashboards in development with more depth and value. Timeline: V1 expected by next week, with ongoing improvements over the next month. Plan to dedicate one call per month for in-depth data analysis and insights.

### Meeting Cadence and Strategy Review

Proposed new meeting structure: 3 regular syncs, 1 deep-dive session per month. Quarterly business review (QBR) planned before the end of August. Aim to analyze overall strategy, identify gaps, and potentially adjust focus areas.

### DevOps Compliance Content

Saakshi requested creation of DORA compliance content for DevOps. Suggested a generic approach with organic inclusion of Flosum where relevant. Offered additional information if needed by the content team.

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Create step-by-step guide for using Ahrefs to validate URLs
- Investigate Screaming Frog for URL validation, consult with technical team on capabilities
- Continue work on new Looker Studio dashboards; aim for V1 delivery by next week
- Schedule QBR/quarterly look-back meeting with Flosum before end of August

**Beau Beamon (Flosum)**
- Prepare Warmly reports showing account-level page visits and lead-level last page data for next meeting

**Rachel Pasche (GrowthX)**
- Clear browser cookies and attempt Webflow article publishing again
- Inform Saakshi of results to determine if bandwidth upgrade is needed

**Saakshi Jain (Flosum)**
- Discuss proposed meeting cadence (3 weekly syncs + 1 monthly deep-dive) with Matt Lyman and finalize with GrowthX team

---

## Transcript

**Jessalynn Jones:** How's your week going so far?

**Saakshi Jain:** The week's been great so far. Thanks so much for asking. Just staying busy.

**Jessalynn Jones:** We're halfway through the week. I feel like this week has gone by pretty quickly. I can't believe it's already Wednesday.

**Jessalynn Jones:** Hey Beau, how's it going?

**Beau Beamon:** Good, good.

**Jessalynn Jones:** Yeah, I was just telling Saakshi that this week has just flown by. I know that someone said they might not be joining today, so is there anyone else we should wait for, or should we go ahead and jump in?

**Jessalynn Jones:** I don't think there's anybody else joining.

**Saakshi Jain:** We should definitely get started.

**Jessalynn Jones:** Great. So before we dig in, I just wanted to check in on the backup and archive messaging. I know we have a couple of pieces on hold for that. Any updates in refining the messaging that we can apply?

**Saakshi Jain:** Yes, we've been able to make some progress there. I think Sidney and Matt should be updating you guys by next week. We definitely have made great progress.

**Jessalynn Jones:** And then Jakub finished the redirect list for you guys. Jakub, any added context?

**Jakub Rudnik:** Yes, I completed that this morning. There are about a dozen redirects. They were largely batched pretty quickly — anything in blog or resources that seemed to be previously a blog gets redirected to the blog homepage. There's a lot of customer stories that I redirected to the customer stories homepage. That took care of about 90% of it. For one-off pages where there's no clear destination, we redirect to the homepage.

You've got a list of 1,000 redirects to hand off to the website team. That should eliminate the vast majority of 404 errors. We probably want to rerun this in two weeks or a month to see if anything new comes up and to give time for re-crawling and indexing. I found a few in this report that had already been redirected, which is fine to add again.

With the low to zero traffic and impressions across the board, there's not much risk here. This should clean up about 90%.

That was the big batch we've been focused on. The other error types — image captions, missing metadata — should be much quicker. Let me know if you have questions.

**Saakshi Jain:** Thank you so much for doing that. This has been hanging on us for about six months. Every time I'd open it thinking I'd confirmed it, I'd see 300 errors again. Thank you for taking care of it. I'll get these uploaded and let's crawl it again in two weeks like you said.

**Jakub Rudnik:** And Matt's been using Ahrefs as a health score indicator. We should see that going up. You're using Ahrefs, so just keep us in the loop on what results we see. It's such a tedious exercise to see a number that shows it made a difference. Looking through your site structure, a lot of it makes more sense now. I didn't see anything that seemed wrong. You cleaned up a lot of stuff that makes sense. I'll async reach out if I have questions. It seems like you're on the right path.

**Saakshi Jain:** Awesome.

**Saakshi Jain:** Yeah, Beau, I think you have something.

**Beau Beamon:** Does Ahrefs have any URL validation capability? Would you recommend something that would validate URLs? I can show you why I'm asking.

**Jakub Rudnik:** Yeah, I think that context would be good. Ahrefs does identify errors and pages with issues. I use GSC as the source of truth, but Ahrefs is good for surfacing everything in one look. What exactly are you looking for?

**Beau Beamon:** Let me share my screen. So this is Warmly, a de-anonymization platform that sends us leads based on buyer persona from companies who have visited our site. This is our DevOps visitors report, and there are many URLs here — some valid, many not. I have old URLs mixed in with new ones. For example, when someone signs up for the 2024 State of DevOps ebook, I want to redirect them to the 2025 version instead. I can set up redirects in Marketo, but I need to know all the valid pages we have for each product. That's why I'm asking about URL validation tools.

**Jakub Rudnik:** Yeah, I can see old URL formats in there. If you can validate what's currently live, you can remove or redirect anything that's no longer current. So I'll pull up my Ahrefs instance and create a step-by-step guide. Screaming Frog is a technical SEO tool that will crawl your entire site and give us the source of truth on what's live.

My real question is: can Warmly export a list of all pages where Flosum qualified leads are visiting, ordered by volume? That would help us identify both content opportunities and old pages that need refresh or redirects.

**Beau Beamon:** Yes, they retain that information. I can pull account-level reports showing all the pages people from that account visited, plus lead-level reports showing the last page visited. I can prepare these for next meeting.

And here's the bigger picture — I'm segmenting de-anonymized traffic by product so I can assign them to NERFA programs and score them properly. So far this year, Warmly has delivered 7,800 net new leads. If someone visits DevOps pages, they get a DevOps solution interest. If they visit backup and archive pages, they get that interest instead. That's why I need to know every page we have for each product so I can segment them properly and put them in the right nurture programs.

**Jakub Rudnik:** Okay, I'm connecting the dots now. If you pull that report, we can look for opportunities on new content and identify what needs refreshing or updating. We can see where there's actual traffic and what old content we should clean up. That would be huge for both sides.

**Jessalynn Jones:** Other thing I wanted to mention briefly is that Rachel's been trying to publish all of those approved articles. She's been going through and resolving all the comments and trying to get them published, but Webflow has been kicking her out and not even letting her update content. There's some kind of issue happening with Webflow.

**Saakshi Jain:** I think there is a bandwidth issue. I think we need to upgrade. But if you could just try clearing your cookies in incognito mode, let me see if that's still causing a problem, then I'll go ahead and fix it. If it's not, then whenever we actually log in tomorrow, we can take it up then. But as we speak, I'm trying to upload the CSV with all of those redirects, and that's working fine for me.

**Jessalynn Jones:** All right. Rachel, do you want to try clearing your cookies and all of that, and then just let Saakshi know if we're still running into issues with that after this call?

**Rachel Pasche:** Yeah, I'll clear out my cookies and then try another upload after this, and then let you guys know.

**Rachel Pasche:** Okay. Yeah, thanks so much for this.

**Jessalynn Jones:** And then we're also working through reviewing some more articles. So you'll have some more articles by end of day today to look at for this week. And then other than that, I think we just have Looker Studio to go over.

**Jessalynn Jones:** Jakub, did you want me to share my screen or do you want share yours?

**Jakub Rudnik:** I don't think it's working, frankly. So we can talk about this offline. The big update I have is that we're not in love with our Looker Studios client-wide, and we're taking that on. Some things seem to be working, but even a V1 doesn't look right. I'm changing the date range and nothing's changing — this looks the same as four weeks in a row. There's two folks now working on net new Looker dashboards. There's a lot more value we need to get into this. So as of today, they had bandwidth to work on this. V1 should be here by next week with a bit more depth. Then we'll be rolling out new pages and reporting each week to get to steady state.

We'll want like our head of customer ops to get a sense of what's working and what's not across all clients so she can dive in and understand specifics. I'll work on connecting those dots and we'll get some potential dates for that.

I also wanted to bring up that we want to start using more time — at least once a month — to dive in deeper to where we're seeing performance and where we're seeing gaps. I don't know if we've talked about that with Flosum, but the goal would be to use one of our four calls a month, at least half of that call, to dive in deeper. So we take time on our end to dig in, where are the insights, have more of a conversation with that depth. Certainly like check at the weekly cadence. But I think doing it four times, we're not getting to enough depth. So dedicating one of those calls — probably the first call of a new month so we can get that data and look-back, or maybe the second one, so we have enough time for GSC data to come through.

**Saakshi Jain:** That was one of the closing questions I had for you guys. Like when is it that we can actually dig in on all of these things? You've been doing it for like 12 weeks now, so when do you think it's a good time to actually start deep diving? So thank you for answering that preemptively. Yeah, for sure. I think at that level, the monthly cadence, we should also schedule a look-back both at the analytics and the strategy. Why do that like a QBR of our first quarter together? So that would make sense, I think, before end of August. So we're using one of these and maybe extending half an hour if there's a bandwidth on your side, or we can just keep it contained. But want to put that in your brains as well.

**Saakshi Jain:** And we will also be able to identify if there are any other gaps that we have overlooked. Like, I know we've been super focused on just backup and archive. Like do we want to actually change course from there? Do we want to stay put on it? This session would probably help us just dive deep into all of that as well, because you can't do that in regular calls. You have just so much to do.

**Jakub Rudnik:** Totally agree. Okay, so I'll take that on, put some thought on when would be best and ask for your feedback on timing. But again, let's do that by end of August. We'll have some of that reporting piece in place that'll help enable us to do that deeper. And then yeah, we'll want our head of customer ops. I'm not sure if you've met her. She's been joining some of those too to get a sense so she can dive in and understand what's working, what's not across all clients, but specific things I think are going well here, but to bring her in so she can see those things too. So I'll work on connecting those dots and then we'll get some potential dates for that.

**Jessalynn Jones:** Yeah, I just added here at the bottom of our agenda. But this is kind of like the meeting cadence that we were talking through — just trying to utilize our time better for y'all. So we can not just go deeper on the analytics side of things, but also learn from y'all what you are seeing and be able to implement that and do our strategy more.

So if y'all want to talk with Matt and the internal team and see if this kind of aligns with your vision for what would be most beneficial and helpful for y'all during these meetings, that would be great.

**Saakshi Jain:** I think end of August now is great, but I'll definitely sync with that and keep you guys updated on that as well.

**Jessalynn Jones:** Great. Well, I think that's all that we had for today, but is there anything else that you need from us right now?

**Saakshi Jain:** The only other thing that I wanted to mention was that we need to do that DORA compliance thing for DevOps. I've already sent you everything that I had information on, and we could keep it generic. We could actually organically put in Flosum wherever we can. So that's the approach that we could take. But in case you need any other details from me, I'm very happy to supplement that because I know you guys haven't done DevOps for us so much.

**Jessalynn Jones:** We'll definitely tap into you as a resource if we run into anything as we start digging into that. But I think that the doc that you sent over had a lot of really great starting points, especially that resource doc that kind of broke down y'all's perspective on it and how it works in Flosum. So that'll be super helpful. But yeah, if Rachel needs anything, she'll be able to find you.

**Saakshi Jain:** Thank you so much. Yeah, have a great day, y'all.

**Jessalynn Jones:** You too. Thanks everyone.
