# Strapi <> GrowthX -  Weekly Sync

<metadata>
date: 2026-02-03
time: 17:29 UTC
duration: 21 minutes
organizer: team@growthxlabs.com
participants:
  - Carrie Chowske (GrowthX)
  - Victor Coisne (Strapi)
  - Theodore Kelechukwu Onyejiaku (Strapi)
  - Paul Bratslavsky (Strapi)
fathom_recording_id: 119362448
fathom_url: https://fathom.video/calls/552943262
share_url: https://fathom.video/share/JvzpXJfk7v5ZMz2xKWZ3743qfEQVs8SK
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Strapi aligned on pausing form snippets pending V5 migration, implemented new Airtable pipeline for real-time content visibility with webhook automation, and reviewed January performance hitting all-time highs with +25% traffic and +400% newsletter signups. Committed to accelerated review process for integration and comparison pages to increase publishing velocity.

---

## Context

GrowthX is working with Strapi on CheckThat's content operations, managing a high-volume integration and comparison article pipeline while Strapi undergoes a V5 migration. Carrie Chowske (GrowthX) and Victor Coisne (Strapi) lead content strategy and engineering respectively, with Theodore handling implementation and Paul supporting operational execution. Usman (GrowthX) manages the day-to-day content production on Strapi. This weekly sync addresses blocking issues, performance review, and process optimization to maintain publishing velocity during the migration.

---

## Relevance

**Content Operations & Quality**
- Form snippets paused on all integration pages due to slow preview bug; will be removed from Strapi V5 migration
- Image placement and optimization issues identified; Strapi engineering team working on fix by end of week
- 25 articles in review with 2 older duplicates cleaned up; process refocused on integration and comparison pages

**Content Marketing Performance**
- January traffic +25% MoM (all-time high); impressions +40%; newsletter signups surged +400%
- Contact Sales clicks exceeded 5,000; demo form drop traced to infrastructure issue, not content quality
- Content library now drives 53% of organic traffic; top performers include "Markdown editors for React," "best CSS frameworks," "React markdown guide," "NextJS 16 features"

**Content Pipeline & Automation**
- New Airtable view deployed for real-time pipeline visibility (staging → review → published)
- Strapi webhook automation planned to sync publish status to Airtable, eliminating manual tracking
- Integration page cohort on Looker dashboard in progress; "refreshes" cohort to be added for strategy validation

**Product & Engineering**
- Strapi V5 migration underway with code-based rewrite; form snippet implementation paused to avoid rework
- Proposed topics from Usman include Next.js templates; review and prioritization pending Theo's feedback

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

## Decisions & Commitments

**Form Snippet Pause:** Form snippets will be removed from all new integration pages and the four already-staged pages, with fixes deferred until post-V5 migration. Victor to communicate preview delay context to Usman.

**Airtable Pipeline Automation:** New Airtable pipeline view is live and shared with stakeholders. Carrie to implement Strapi webhook for automatic "Published" status updates, eliminating manual Airtable sync.

**Accelerated Review Process:** Integration and comparison pages will receive minimal review prior to publication, with fixes handled post-launch to increase velocity. Theodore committed to this lean process.

**Performance Tracking Cohorts:** Carrie to add "refreshes" and "integrations" cohorts to Looker dashboard for strategy validation and next-week reporting.

---

## Open Questions

- Integration page performance validation pending Looker cohort analysis (Carrie to deliver)
- Details on "ride the wave" keyword strategy and Usman's proposed Next.js template topics pending Theo's review

---

## Action Items

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Check Usman’s Slack questions re: form snippet preview + content refresh visibility; reply in Slack
- Review Usman’s proposed Next.js template topics; tell Carrie which to proceed with

**Victor Coisne (Strapi)**
- Inform Usman re: form-embed preview delay status; note that Notom is working on fix post-migration

**Carrie Chowske (GrowthX)**
- Tell Usman to remove form embeds from all new integration pages and four already-staged pages
- Share Airtable pipeline link with Theo; group by content type (integrations, comparisons, articles) for clarity
- Implement Strapi publish webhook to automatically update Airtable status when content goes live
- Add "refreshes" cohort to Looker dashboard; analyze integration page performance and send analysis to Victor for next week

---

## Transcript

**Carrie Chowske:** This meeting is being recorded. Let me make sure we have the recorder in here.

**Victor Coisne:** I was just reading the long message from Usman.

**Carrie Chowske:** He's very thorough. He asked me if I could relay some questions, but I told him to just ask directly and I'd follow up in the meeting.

**Victor Coisne:** So he's got all his technical questions for Theo, I'm sure. That's good.

**Carrie Chowske:** Theo has some outstanding questions. Usman posted a super long question in our Slack channel. A lot of it's related to him not being able to see things in preview, so he's worried something's wrong. He didn't want to do a big batch until he confirmed with Theo if the form snippets were rendering properly.

**Carrie Chowske:** The other issue is that he refreshed some content but the changes aren't showing up, so he's not sure if something else needs to be done.

**Theodore Kelechukwu Onyejiaku:** Yeah, sure. I'll definitely check them out because currently I'm working on the integration. I'll get back to his questions soon. Concerning the form embed, it's embedded code in the content. The only issue is preview takes a while. Even if I embed it, I'd have to wait quite a long time for it to preview. I've already shared the issue with Notom, so I'm waiting on that.

**Victor Coisne:** I just had a chat with Notom about this. To give you context, we're migrating our website to Strapi V5 with a code-based rewrite. I'm reluctant to fix things on the old website when we're moving to the new one. I think we should put the form on hold and remove it altogether from all pages. The goal is for users to download the software anyway. We should tell Usman to remove that snippet from all new integration pages.

**Carrie Chowske:** I think he stopped after those first four pages, so he probably won't need to remove anything beyond those. I'll check with him to make sure.

**Carrie Chowske:** He staged seven articles last week. There are 25 still in review, but he cleaned it up so we're down to two older pieces that aren't duplicates. I pulled up this view so you can see which ones we have. There are some comparison ones and most are integrations.

**Theodore Kelechukwu Onyejiaku:** When I'm done with the current work, I'll need the list. I went to Airtable but couldn't find the review list except for what Vivek shared in chat. Can you share that link with me?

**Carrie Chowske:** Absolutely. I created this view because Victor wanted visibility into the whole pipeline. Since I just came on to these accounts, I wanted to give you guys a clear view into what you need without confusion. The link is always live, so you can check what's going on and what needs review. If you need a different view or more information, just let me know and I'll update it.

**Victor Coisne:** This is great.

**Carrie Chowske:** The full pipeline shows everything currently in production, whether it's under review, in progress, backlogged, or published. I've included published URLs and go-live dates. How do we know when Theo publishes articles? How do you update the status?

**Victor Coisne:** Either you're notified or I can give Theo access to update the status himself. What do you prefer, Theo?

**Theodore Kelechukwu Onyejiaku:** I'd appreciate that.

**Victor Coisne:** We shouldn't do this manually. There's webhooks in Strapi, right?

**Carrie Chowske:** Yes, we could use a webhook.

**Victor Coisne:** Perfect.

**Carrie Chowske:** There was another issue with image placement. Usman updated the post noting that the image was wrong and optimization was off. But our engineering team is working on a fix to the pipeline so we won't have that issue in the future.

**Victor Coisne:** That should be fixed by end of week. That's what he's working on.

**Theodore Kelechukwu Onyejiaku:** Good.

**Carrie Chowske:** I'll follow up with Usman after our meeting. Usman also worked up some proposed topics. He pulled keywords in line with the "ride the wave" ideas, including stuff about Next.js templates. He's got a few ideas. Can you look at it after the meeting, Theo? Let us know which ones you want to move forward with.

**Victor Coisne:** That sounds like a good plan.

**Carrie Chowske:** I want to pull a January performance summary. Vivek had noted we were on track to beat December's numbers, which is what happened. January was an all-time high for traffic, 25% over December. That's impressive coming out of Q4 into Q1 when many struggle. Search visibility surged with impressions up 40%. Engagement is mixed but directly related to the traffic spike. We went from 47% to 40% engagement rate, which scales well with our impressions—a positive trend. Conversion intent signals are up. Contact sales clicks were over 5,000 for January.

One thing I wanted to flag: the demo form numbers from HubSpot fell off a cliff, which looks like maybe an error rather than real numbers.

**Victor Coisne:** No, that's an infrastructure issue with the demo we had. We understand what happened.

**Carrie Chowske:** Good, I wanted to make sure you saw it because I had to look at it twice.

**Carrie Chowske:** Newsletter signups jumped 400% month-over-month, another big leap. Top gainers: "Markdown editors for React," "best CSS frameworks," "React markdown guide," "NextJS 16 features." Notable declines: "BUN vs. Node.js" and "JS frameworks." JS frameworks is still the number one performer, so no immediate concern. BUN vs. Node.js is worth monitoring. The content library now drives 53% of organic traffic. Overall, solid picture—growth across traffic, impressions, clicks, and conversion signals. The engagement rate decline is expected with traffic spikes and actually signals good engagement scaling.

**Victor Coisne:** Some of this is seasonal. December is always peak. I think we're going in the right direction. I saw good trends on integration pages too. Right now we mostly report on blog posts. It would be helpful to get visibility on integrations and refreshes—understanding before/after performance on refreshed articles. Are we seeing uptick?

**Carrie Chowske:** Do we have an integrations cohort in Looker for you?

**Victor Coisne:** I saw on GA that overall integrations are up 40% engaged sessions month-over-month, which is where we want to be. I just don't know how much is from recently added ones and which are taking off. We need to validate: are we creating the right ones? Are they ranking?

**Carrie Chowske:** Let me dig into that for next week, or even later this week. I have integration pages in Looker as a cohort. I don't see refreshes yet, but that's easy to add. I want to make sure we're tracking the right things going forward so you have a clear picture of what's working, where to move the lever, and where to double down.

**Victor Coisne:** Good deal. Sounds good.

**Carrie Chowske:** I think that's all I've got. Any questions?

**Victor Coisne:** I'm going to follow up offline with Usman. Let me go back to the Airtable view. The "in progress" section is all the content sitting with SEO, right? The red items are under Strapi review?

**Carrie Chowske:** Yes, that's the same as the "ready for review" tab. The section you're looking at shows Usman's current work. The other section is approved but not started yet.

**Victor Coisne:** Got it. So "ready for review" is what I was looking for.

**Carrie Chowske:** Yes. Would it help if I grouped these by type for you, Theo?

**Theodore Kelechukwu Onyejiaku:** Yes, that would be great.

**Carrie Chowske:** No problem. I can organize this view any way you need. I just want to make sure you have visibility into what you want to see. Would it be helpful to group by content type?

**Victor Coisne:** For integration pages, we should publish pretty quickly without extensive review, especially for comparison pages and integrations. Do a small review and publish.

**Paul Bratslavsky:** We can update later if we catch something.

**Victor Coisne:** That's my recommendation.

**Paul Bratslavsky:** We talked about this in our one-on-one to keep moving things forward. Appreciate the callout, Victor.

**Theodore Kelechukwu Onyejiaku:** I'd love it if the status column updated once I publish. I could track what's still pending.

**Victor Coisne:** The webhook would be perfect for that, Carrie. The list stays updated daily.

**Carrie Chowske:** Perfect. If anything changes, just let us know. Usman will probably follow up a few more times, Theo, but he provides thorough info so I want to capture it. I'll let him know about removing the form snippets and that we'll worry about that after the site migration.

**Victor Coisne:** Perfect.

**Carrie Chowske:** Great. Well, have a great week and we'll talk soon.

**Victor Coisne:** Talk on Slack.

**Paul Bratslavsky:** Thanks, everyone.

**Carrie Chowske:** Bye. Thank you.
