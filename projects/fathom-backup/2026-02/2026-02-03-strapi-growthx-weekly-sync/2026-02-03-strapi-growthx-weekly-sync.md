# Strapi <> GrowthX -  Weekly Sync

<metadata>
date: 2026-02-03
time: 17:29 UTC
duration: 21 minutes
organizer: team@growthxlabs.com
speakers: Victor Coisne (Strapi), Theodore Kelechukwu Onyejiaku (Strapi), Paul Bratslavsky (Strapi), Carrie Chowske (GrowthX)
fathom_recording_id: 119362448
fathom_url: https://fathom.video/calls/552943262
share_url: https://fathom.video/share/JvzpXJfk7v5ZMz2xKWZ3743qfEQVs8SK
source: fathom
enriched_on: 2026-02-27 14:27 UTC
</metadata>

---

## Summary

GrowthX and Strapi synced on resolving content pipeline blockers: pausing form snippets due to preview bugs ahead of the V5 migration, implementing an automated Airtable pipeline for real-time visibility, and accelerating review cycles for integration and comparison pages. January delivered strong results with traffic up 25%, impressions up 40%, and newsletter signups surging 400%, with the content library now driving 53% of organic traffic.

---

## Context

Strapi and GrowthX are partnering on content strategy with Carrie now managing performance analysis and pipeline coordination. The partnership is ramping: Strapi handles engineering and reviews while GrowthX manages content operations, pipeline visibility, and analytics. Both teams are focused on increasing publishing velocity for integration and comparison pages, which show strong engagement signals (40% month-over-month growth). The upcoming Strapi V5 site migration is reshaping technical priorities, prompting decisions to defer lower-value fixes (like the form snippet preview bug) and streamline content workflows. January's all-time-high traffic (+25% MoM) and 400% newsletter signup surge validate the content strategy, setting the stage for continued optimization of integration page performance and refreshed content.

---

## Relevance

- **Content Operations**: Airtable pipeline automation and review process acceleration directly drive publishing velocity and team efficiency.
- **Performance Tracking**: New Looker cohorts for refreshes and integration performance validate content strategy ROI and guide future investment decisions.
- **Technical Roadmap**: Form snippet pause aligns with Strapi V5 migration priorities, deferring non-critical fixes until site rewrite.
- **Product Validation**: January surge in integration page engagement (+40% MoM) signals product-market fit and justifies continued investment in this content type.
- **Partnership Coordination**: Formalized pipeline views and webhook automation reduce friction between Strapi (engineering/review) and GrowthX (operations/analytics) teams.

---

## Overview

- **Form Snippets Paused:** Due to a slow preview bug and the upcoming Strapi V5 migration, all form snippets will be removed from new pages.
- **Airtable Pipeline Live:** A new Airtable view provides real-time visibility into the content pipeline; a Strapi webhook will automate status updates to eliminate manual tracking.
- **January Performance Surged:** Traffic hit an all-time high (+25% MoM), driven by a 40% jump in impressions and a 400% increase in newsletter signups.
- **Review Process Accelerated:** To increase publishing velocity, reviews for integration and comparison pages will be minimal, with minor fixes handled post-publication.

---

## Key Topics

### Content Pipeline & Process

  - **Problem:** Usman reported issues with form snippet previews and content refresh visibility, which were blocking the publication of new integration pages.
  - **Solution → Pause Form Snippets:**
      - **Rationale:** The preview bug is low-priority due to the upcoming Strapi V5 migration and site rewrite.
      - **Action:** All form snippets will be removed from new pages. Usman will also remove them from the four pages already staged.
  - **Solution → New Airtable Pipeline:**
      - Carrie created a new Airtable view for real-time visibility into the content pipeline, replacing scattered tracking methods.
      - **Automation:** A Strapi webhook will automate status updates (e.g., "Published") in Airtable, eliminating manual tracking.
  - **Solution → Accelerated Reviews:**
      - To increase publishing velocity, reviews for integration and comparison pages will be minimal.
      - **Process:** Publish quickly → Fix minor issues later.

### January Performance Review

  - **Overall:** Strong growth, with traffic hitting an all-time high.
  - **Key Metrics (MoM):**
      - **Traffic:** +25%
      - **Impressions:** +40%
      - **Engagement Rate:** Scaled well with traffic (47% → 40%).
      - **Newsletter Signups:** +400%
  - **Conversion Signals:**
      - **Contact Sales Clicks:** \>5,000
      - **Demo Form Submissions:** Sharp drop confirmed as an infrastructure issue, not a content problem.
  - **Top Performers:** "Markdown editors for React," "best CSS frameworks," "React markdown guide," "NextJS 16 features."
  - **Declining Performers:** "BUN vs. Node.js" (monitor), "JS frameworks" (still \#1 overall).
  - **Content Contribution:** The content library now drives 53% of all organic traffic.

### Future Reporting Needs

  - **Request:** Victor requested performance tracking for specific content types (integrations, refreshed articles) to validate strategy.
  - **Action:** Carrie will add a "refreshes" cohort to the Looker dashboard and analyze integration page performance for next week.

---

## Action Items

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Check Usman’s Slack questions re: form snippet preview and content refresh issues; reply directly in Slack
- Review Usman’s proposed topics and tell Carrie which ones to proceed with

**Victor Coisne (Strapi)**
- Inform Usman that form-embed preview delay is waiting on Notom for fix; communicate Strapi’s decision to pause form snippets until V5 migration

**Paul Bratslavsky (Strapi)**
- (No explicit action items assigned; confirmed alignment on accelerated review process for integration and comparison pages)

**Carrie Chowske (GrowthX)**
- Tell Usman to remove form embeds from all new integration pages (currently staged on four pages)
- Share Airtable pipeline link with Theo and group entries by content type (integrations, comparisons, etc.)
- Implement Strapi publish webhook to automatically update Airtable status when articles go live
- Add refreshes cohort in Looker dashboard and analyze integration page performance; send insights to Victor by next week

---

## Transcript

**Carrie Chowske:** This meeting is being recorded.

**Victor Coisne:** Hey, Carrie. How are you?

**Carrie Chowske:** Good. How about yourself?

**Victor Coisne:** Not bad. Busy.

**Carrie Chowske:** Yeah, I can relate. Do you know if Theo is coming?

**Victor Coisne:** I think so.

**Carrie Chowske:** I was just reading the long message from Usman.

**Victor Coisne:** So he's got all his technical questions for Theo, I'm sure. That's good.

**Carrie Chowske:** Hey, Theo, how are you?

**Victor Coisne:** Yeah, Theo, we can't hear you.

(Audio/connection issues resolved)

**Carrie Chowske:** Let's go ahead and get started. I've got quite a few questions, Theo. Usman just posted another super long question in our Slack channel. A lot of it's related to him not being able to see things in preview, so he's worried something's wrong. He didn't want to do a big batch until he confirmed with you if the form snippets were rendering properly. And he also refreshed some content, but the changes aren't showing up.

**Theodore Kelechukwu Onyejiaku:** Yeah, sure. I definitely will check them out because currently I'm working on the integration. So I'll soon be done and I'll get back to the questions he has. Concerning the form embed, the only issue at the moment is that it takes a while to preview. So even if I should embed it, I'd have to wait for quite some time for it to preview. I've already shared the issue with Notom, so I'll be waiting for that.

**Carrie Chowske:** I just told him I would follow up.

**Victor Coisne:** I will let him know that you're waiting on Notom for that. I just had a chat with Notom and we were discussing this. Just to give you full context, we are migrating our website to Strapi V5 and doing basically a code-based rewrite. I'm a little reluctant to fix stuff on the old website as we are moving to the new website. For that reason, I think we should put on hold the form and remove it altogether from all the pages. The goal is for them to download the software anyway. So I think we should just tell Usman to remove that snippet from all the new integration pages as well.

**Carrie Chowske:** Okay. I think he stopped after those first four, so he probably won't have to remove anything but from those. I think we should be good. So there were, I think he staged seven articles last week. There's still those 25 in review, but he cleaned it up so we're down to, I think, like two older pieces that are not duplicates.

**Theodore Kelechukwu Onyejiaku:** Is this articles or integrations?

**Carrie Chowske:** I pulled up this field so you guys can see which ones they are. There's some comparison ones and then there's, most of these are integrations though. I created this because I know Victor wanted visibility into the whole thing. It's less confusing because I know, as someone who just came on to these accounts, I have my own methods for how I keep things in Airtable versus how Vivek was doing it and how Usman does it. I'm going to give you guys full view into what you need and nothing more. That way we're always on the same page. This link is live always, so you can always come in here and go, okay, here's what's going on. Here's what I need to review. If you need a different view or other information that's not showing up here, just let me know and I can update it.

**Victor Coisne:** No, I think this is great. Yeah.

**Carrie Chowske:** And there's also the full pipeline. So anything in here is what's currently in production, whether it's things under review or that we're currently working on or that are backlogged. And then of course we have them for published as well. So I tried to make sure we got the published URL in here and then the date when it went live. We're trying to stay on top of it and making sure we have all the right information in the right fields.

**Victor Coisne:** And does it get automatically updated, right? When the article gets published, how do you know when Theo publishes those articles? How do you update the tag?

**Carrie Chowske:** Either he has to tell us or I can give Theo access to change the status if he wants to. That's okay with us. Whatever works better for you. We have some people that love to update themselves and others that just dump us a list at the end of the week.

**Victor Coisne:** You know, either one's fine. It feels like we should not do manually. There's webhooks in Strapi, so like whatever, you know.

**Carrie Chowske:** Yeah, we could do it with a webhook.

**Victor Coisne:** Yeah. Perfect.

**Carrie Chowske:** Okay. So the rest of what I have to kind of talk about is, oh, I didn't want to forget this. Usman also worked up some proposed topics. He pulled some keywords kind of in line with those ride the wave ideas. Some stuff about Next.js templates, and so he's got a few ideas in here. You can look at it after the meeting if you want, Theo, but let him know if there's any of these or all of them that you want to move forward with.

**Victor Coisne:** That sounds like a good plan.

**Carrie Chowske:** Okay. So I just want to pull a January performance summary just to kind of see where we're at. I wanted a clear picture coming into this with fresh eyes, like where we were at for the month of January, especially because Vivek had noted that we were on track to beat December's numbers, which is actually what happened. So January was, you know, all-time high for traffic. It was 25% over December, which I think that's pretty impressive. A lot of people struggle coming out of Q4 into Q1, it sometimes can be a little bit of a slog. So I think it's pretty impressive that your content continued to grow over that time.

Search visibility kind of surged as well because the impressions went up quite a bit, about 40%. Engagement is a little mixed, but I think that's directly related to the traffic spike, and we didn't lose much. We went from about 47% engagement rate to about 40. That's kind of a flat trend over time, so it's kind of scaling with our impressions as they scale. So that's a positive trend, in my opinion. We're not seeing it just fall off a cliff.

Conversion intent signals are up. Contact sales clicks, if these events in GA4 are accurate for you guys, if these are still ones you're tracking, for January we had over 5,000 contact sales links. One thing that I did notice that I wanted to flag for you is the demo form data from HubSpot. It fell off a cliff, but it fell so far that it looks like maybe it's an error rather than actual numbers.

**Victor Coisne:** No, it is something that we had an issue with the infrastructure of the demo. So we understand what happened.

**Carrie Chowske:** Okay, good. I just wanted to make sure you saw it because I had to look at it twice. I was like, that can't be right.

**Victor Coisne:** Okay, good.

**Carrie Chowske:** And then you had, you know, newsletter signups jumped pretty good. It went up about 400% month over month, which is another pretty big leap. The biggest gainers in terms of clicks, we had markdown editors for React, best CSS frameworks, the React markdown guide, NextJS 16 features. And then some notable declines here is the BUN versus Node.js and JS frameworks. This one's still a number one performer. I wouldn't say we need to worry about anything there yet. But this one's probably one to keep an eye on a little bit more. Overall, we're seeing growth in traffic, growth in impressions and clicks. The conversion signals are positive. The content library is creating 53% of organic traffic now. But overall, I think it's a pretty solid picture. There's a few little things here and there where you see some small drops, but when you look at the top level picture, it's just one little drop in a bucket of pretty solid increases.

**Victor Coisne:** I think some of it is seasonal. December is all months, right? So yeah, I think that we're going in the right direction. I think it is a good sign that we are seeing those trends and I'm kind of really curious to see if it continues. But yeah, I saw some really good trend on integration as well. I think that's what would be interesting. Because right now we're mostly reporting on the blog post. I think it would be helpful to get visibility on the other ones, the integration, and maybe for the refreshes as well. Because that's another bucket of work, right? It's like trying to understand like before, after, refresh, like are we seeing uptick in those articles?

**Carrie Chowske:** Right. Did we add a cohort for that in our Looker for you? If not, I can put in something. Yeah, we've got those in there as a cohort. Let me share this. We do have the integration pages in here. And then, I don't see refreshes, but that's an easy one to add.

**Victor Coisne:** Okay. Sounds good. Yeah, I'll do some digging on Looker. I looked on GA, and I know that overall integrations are seeing like a plus 40% engaged session month over month, which is definitely where we want to be going. I just don't know how much of it is attributed to the ones that we added recently and which ones are taking off. I think that's kind of what we're trying to validate. Are we creating the right one? Are they actually ranking?

**Carrie Chowske:** Yeah. Let me dig into that and I can give you some insights for next week for sure. Or even later this week there. I just want to make sure that we're tracking the right things so that you've got a clear picture into what's working, what isn't, kind of where we need to move the lever and where we can double down.

**Victor Coisne:** Yeah. Good deal. Sounds good.

**Carrie Chowske:** I think that's all that I've got. Do you guys have any questions or anything you want to discuss?

**Victor Coisne:** No, I'm just going to follow up offline with Usman. And yeah, maybe if we go back to the view you created in Airtable. Just trying to get a sense of the in progress view. Basically that's all the stuff that is sitting with SEO, right? The stuff that's in red, it's under Strapi review, that's the stuff that's with SEO.

**Carrie Chowske:** That's the same thing that's in the ready for review tab. It's just kind of within the big picture here. This is stuff that Usman is currently working on. And then this is stuff that's been approved, but hasn't been started yet. And if you want, I can group these by type if that would make it easier for you, Theo, to see what you're looking at.

**Theodore Kelechukwu Onyejiaku:** Yeah, okay, I'll do that. Not a problem.

**Carrie Chowske:** Yeah, there's basically I can do anything with it that I can do in Airtable. It's just that this helps kind of focus in on exactly what we're looking at without a million different views. We have so many different views in some of our Airtables. But that's how I keep myself organized.

**Victor Coisne:** Yeah, and if you want to reiterate something, like, for integration pages, I think we should publish pretty quickly. You don't have to do an extensive review. So, ideally, we see that, especially for the ones that are maybe less critical, like the comparator pages and the integration pages. Feel free to do like a very small review and publish those.

**Paul Bratslavsky:** And then we can, if we catch something, update it later.

**Victor Coisne:** But that's my recommendation.

**Paul Bratslavsky:** Yeah, we actually talked about this in our one-on-one to make sure that we keep moving things forward. So it's definitely something we discussed. Thanks for the call out with Victor too, though.

**Theodore Kelechukwu Onyejiaku:** Yeah, and I think it would be great if we have the status column so that once I've published one, we could see the update here. So that I would keep in track the ones that are yet to be published.

**Victor Coisne:** Yeah. Yeah, so that webhook would be perfect if we can capture that information, Carrie. And that way, that list constantly gets updated on a daily basis.

**Carrie Chowske:** So that would be perfect. Okay, got it. That was pretty easy. Hey, listen, we're getting off to a good start. Yeah, if anything changes, just let us know, and I'm sure Usman will follow up a couple more times, Theo, but every time he gives me such thorough information, I'm like, I don't want to lose anything in the translation, so I've just been having him kind of post those questions. But I'll let him know about removing the form snippets and that we will just kind of not worry about those until after the site migration.

**Victor Coisne:** Perfect.

**Carrie Chowske:** Awesome. Well, you all have a great week, and we'll talk soon.

**Victor Coisne:** All right, talk on Slack.

**Paul Bratslavsky:** Thanks, everyone.

**Carrie Chowske:** Bye. Thank you.
