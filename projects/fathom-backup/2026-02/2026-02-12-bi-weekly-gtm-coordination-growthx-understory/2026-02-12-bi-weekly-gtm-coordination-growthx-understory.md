# Bi-Weekly GTM Coordination — GrowthX & Understory

<metadata>
date: 2026-02-12
time: 18:33 UTC
duration: 35 minutes
organizer: Jesus Yepez (GrowthX)
participants: Alexander Fine (Understory), Naufal Nugroho (Understory), Josh Solomon (Understory), Jason Gong (GrowthX), Tyler Pavlas (GrowthX), Natalia Moura Gaal (Understory), Mark Lim (Understory), Gloria Willis (GrowthX), Danni Roseman (GrowthX), Andrew Osborne (Understory), Jeffrey Ignacio (GrowthX), Jesus Yepez (GrowthX)
fathom_recording_id: 122055857
fathom_url: https://fathom.video/calls/564335141
share_url: https://fathom.video/share/k1YEsDFyWoNpgDWZz6t3zybRtUxY9aEm
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX and Understory teams aligned on fixing the Clay enrichment workflow's unsustainable credit consumption by narrowing HubSpot list triggers to intent signals. The group prioritized campaign launches: Breakfast/Fletch events first, then the new "Webflow Lookalike" campaign targeting companies similar to successful customers. Natalia will build HubSpot positive-reply segments to enable follow-up workflows with engaged prospects.

---

## Context

This bi-weekly GTM coordination sync brings together the GrowthX team (Jason Gong, Gloria Willis, Jeffrey Ignacio, Jesus Yepez) and the Understory Agency team (Mark Lim, Natalia Moura Gaal, Andrew Osborne, others) to align on paid acquisition, cold outreach, and content marketing campaigns. The meeting focused on two critical operational issues: Clay enrichment cost overruns consuming $1000s in credits due to re-enriching a 17k-record HubSpot list daily, and campaign prioritization as the team realigns to higher-performing audience segments (Fletch LinkedIn followers showing 1:15 reply rates vs. cold prospects). Mark Lim announced his departure at month-end, with Andrew Osborne taking over his responsibilities.

---

## Relevance

- **Clay/Data Stack:** Cost control, workflow optimization, data enrichment strategy for outbound
- **Paid Acquisition:** Campaign prioritization, audience segmentation, reply rate analysis
- **Cold Outreach:** Fletch campaign performance, LinkedIn follower targeting, email sequence optimization
- **HubSpot Operations:** Outbound Sync integration, segment creation, positive-reply workflows
- **Team Transitions:** Mark Lim departure, Andrew Osborne onboarding as replacement
- **Content Marketing:** Growth Cafe campaign, workshop recording funnel, event follow-up strategy

---

## Overview

- **Clay Enrichment Overhaul:** The Clay enrichment workflow is being rebuilt to fix high costs. The current daily sync re-enriches the entire 17k-record list, causing exponential credit consumption. The new workflow will use a webhook trigger to process records incrementally and will only enrich contacts who show intent (e.g., email reply).
- **New Campaign Priority:** A new "Webflow Lookalike" campaign is now a top priority to build pipeline. It will target companies similar to successful customers (Lovable, Webflow) by offering a workshop recording, then pitching a strategy session to positive repliers.
- **Outreach Strategy Shift:** The team will prioritize outreach to Fletch's LinkedIn followers, as this audience yields a significantly higher reply rate (1:15) than cold prospects. Cold outreach for Fletch and the Answer Engine event will be de-prioritized.
- **Positive Reply Follow-up:** HubSpot's existing Outbound Sync segments will be used to build a workflow for following up with positive repliers. Natalia will create a new "positive reply" segment to enable targeted outreach.

---

## Key Topics

### Clay Enrichment Workflow Overhaul

  - **Problem:** The Clay enrichment workflow is consuming credits at an unsustainable rate.
  - **Root Cause:** The workflow's daily sync re-enriches the entire 17k-record HubSpot list, leading to exponential credit consumption.
  - **Solution:** The workflow will be rebuilt with two key changes:
      - **Trigger:** Switch from a daily sync to a webhook to enable incremental, record-by-record processing.
      - **Scope:** Narrow the HubSpot list trigger to only enrich contacts who show intent (e.g., email reply, new deal created).
  - **Interim Fix:** Natalia will disable the "auto update" toggle in the Clay workbook and columns to stop the current process.

### Outreach Campaign Performance & Prioritization

  - **Recent Performance:**
      - **HeyReach:** 36 positive replies
      - **Instantly:** 131 positive replies
      - **Fletch:** 109 positive replies
  - **Fletch Campaign Analysis:**
      - **Followers:** \~10-15k qualified leads from Fletch's LinkedIn followers.
      - **Performance:** 109 replies from \~1,500 finished sequences → **1 reply per 15 leads**.
      - **Strategy:** Prioritize this high-performing audience over cold outreach.
  - **Growth Cafe Campaign:**
      - **Issue:** Low reply rates due to a spam trigger word in the copy.
      - **Action:** Mark has fixed the copy and will relaunch the campaign tomorrow after Gloria's review.
  - **New "Webflow Lookalike" Campaign:**
      - **Goal:** Build pipeline by targeting companies similar to successful customers (Lovable, Webflow).
      - **Funnel:** Offer a workshop recording → Nurture via newsletter → Pitch a strategy session to positive repliers.
      - **Priority:** High. Mark will build the list today; the campaign will launch this week.
  - **Campaign Priority Stack:**
    1.  Breakfast & Fletch events
    2.  "Webflow Lookalike" campaign
    3.  Answer Engine event
    4.  SIFT segmentation campaign

### Positive Reply Follow-up Workflow

  - **Goal:** Create a workflow to follow up with positive repliers from event invites, pitching a free strategy session.
  - **Solution:** Use HubSpot's existing Outbound Sync segments (e.g., "HeyReach replied").
  - **Action:** Natalia will create a new "positive reply" segment to enable more targeted outreach.

### Team Transition

  - **Mark Lim:** Leaving Understory at the end of the month.
  - **Andrew Osborne:** Taking over Mark's responsibilities. Mark will ensure a smooth transition.

---

## Action Items

**Jason Gong (GrowthX)**
- Send Clay contact table link to Natalia; she'll disable auto-update
- Send final HubSpot enrichment lists (companies + contacts) to Natalia by EOD; she'll rebuild Clay with Jeff review
- Coordinate post-call sync with Gloria (10 minutes)

**Mark Lim (Understory) – Departing Feb 28**
- Send Growth Cafe copy to Gloria for review; launch Feb 13 if approved
- Prioritize Fletch emails to Fletch's LinkedIn followers over cold sends
- Send website hosting/CMS ICP list to Jason for "Webflow Lookalike" campaign; then draft outreach copy
- Ensure smooth knowledge transfer to Andrew Osborne on all ongoing accounts

**Natalia Moura Gaal (Understory)**
- Disable Clay workbook auto-update toggle and column-level enrichment toggles to stop credit consumption
- Schedule Outbound Sync review call with Jason, Jeffrey, and Andrew (start of next week); demo HubSpot setup and segments
- Create HubSpot "positive reply" segments for HeyReach and Instantly (excluding customers)
- Rebuild Clay enrichment workflow using template method once final HubSpot lists are confirmed

**Gloria Willis (GrowthX)**
- Review and approve new Growth Cafe campaign copy from Mark
- Send 10-minute post-call calendar invite to Jason; hold brief sync after this meeting
- Begin creating event briefs for March/April upcoming dates

**Jeffrey Ignacio (GrowthX)**
- Review Clay enrichment workflow and webhook setup before going live
- Participate in Outbound Sync review call to advise on HubSpot configuration

**Andrew Osborne (Understory) – Taking over Mark's role**
- Participate in Outbound Sync review call to learn HubSpot setup and segments
- Take ownership of ongoing account relationships and campaign management post-transition

---

## Transcript

**Jason Gong:** So I guess a few things on my mind today. The biggest one is the enrichment workflow. I know we have campaigns running, but the LinkedIn automation we wanted to spin up—mining for triggers and emailing folks—those two things are top of mind for me.

**Mark Lim:** Yeah, I have it all written down in the meeting notes, so we can go through that and discuss.

**Jason Gong:** Okay, so let's start with Clay enrichment. I have no idea how it works. I thought I understood it, bought credits, and it immediately consumed all of them. My money is gone.

**Natalia Moura Gaal:** I saw the list you shared yesterday. My question is: the Clay workbook we saw enriches companies only. Is the goal to enrich companies only from outbound activities, or any companies with no domain?

**Jason Gong:** I'm working with a HubSpot list. The issue is the membership is too broad, consuming credits. I'm not sure how the workflow works. If I tighten the HubSpot list definition, we should be good, but I thought I did that yesterday and it immediately consumed all my credits.

**Natalia Moura Gaal:** I only saw the company one—that's what Jeff mentioned too. It pulls from a HubSpot list with about 17k records, which is why it consumed so many credits. You also have expensive enrichments—some related to funding consume four or more credits per record. We can double-check and improve the workflows, but if you want to keep it simple, improve the HubSpot list and leverage existing segments in HubSpot for outbound sync activity.

**Jason Gong:** Cost isn't the main concern. I just need to enrich only people showing intent—email replies, new deals. There are multiple triggers. One is replying to an email, another is our team uploading a new deal. I want to narrow it down because right now we're enriching every company we cold email, which is expensive and unnecessary.

**Natalia Moura Gaal:** Maybe I can pair with Jeffrey. I don't have visibility on all the signals important to you internally. Jeff can help with that, and I can layer in Outbound Sync activity. We can review the HubSpot list and change the trigger in Clay.

**Jeffrey Ignacio:** When you click that data—open import object from HubSpot—what triggers it?

**Jason Gong:** It's on a schedule. It looks like every day.

**Jeffrey Ignacio:** And how does it identify which records to pull?

**Jason Gong:** It pulls from this list. It's 17,000 records.

**Jeffrey Ignacio:** Does it pull incrementally or all records each time?

**Jason Gong:** That's a good question. I'm not sure where that's defined. I think that's what consumed all the credits. It looks like it tried to re-enrich the entire table yesterday.

**Jeffrey Ignacio:** What I'd do instead is set this table up on a webhook. That way you only get one record going in, and the table builds incrementally instead of appending cumulatively, which causes exponential credit consumption.

**Natalia Moura Gaal:** When you change the source in Clay, it doesn't delete what you added before—it just changes from that point forward. The way this workbook was built, it updated everything, which consumed all the credits. There's a way to save a table as a template and duplicate it with a different source. If you organize all the HubSpot list filters first and rebuild with a template, it won't happen again because it starts from scratch.

**Jason Gong:** All I need from you is the two HubSpot lists—one for companies, one for people—that define who should be enriched. Then you set up Clay.

**Natalia Moura Gaal:** Once you send the lists, I can turn off the auto-update toggles. Each table and column has an auto-update setting. Turn those off when making changes.

**Jason Gong:** I'll send you the contact list right now. I'll update the lists after this call and ping in Slack.

**Mark Lim:** Now for the LinkedIn trigger and email workflow. We had 36 positive replies from HeyReach, 131 from Instantly—the most we've ever gotten—and 109 from Fletch. Growth Cafe had lower reply rates due to a spam trigger word in the copy. I fixed that, so I'm relaunching with the new copy. I'll send it to Gloria for review, and if approved, we'll launch tomorrow.

**Jason Gong:** Are we still sending cold emails for Fletch, or only to his LinkedIn followers?

**Mark Lim:** We're sending to the cold audience now. The LinkedIn follower sequence is still going. We filtered about 10 to 15k qualified followers from his 60k total.

**Jason Gong:** So you got 109 replies from roughly 1,500 finished leads. That's one positive reply per 15 leads—much better than cold.

**Mark Lim:** Yes, one per 15 finished leads.

**Jason Gong:** The followers approach is much more impactful than cold outreach. Prioritize emails to followers. Growth Cafe is higher priority, but don't message cold if you can use his follower base instead.

**Mark Lim:** For the ICP list you requested—website hosting and CMS companies—it's almost done. I'll send it today.

**Jason Gong:** Context: we have customers in certain industries. We want to experiment with outreach to similar companies. We've done workshops with Lovable and Webflow. I'd send those recordings or ask if they want one, nurture via newsletter, and if they reply positively, offer a free strategy session using the same playbook. I'd like this campaign to launch this week if we have email queue space. It's pretty high priority for building pipeline.

**Mark Lim:** So we also have the Answer Engine campaign to launch. How should we distribute sending volume and prioritize?

**Jason Gong:** Finish the Fletch one and the three upcoming events first. Prioritize Fletch and Breakfast events, then the Webflow Lookalike campaign, then Answer Engine. Historically, AEO outreach hasn't performed as well as targeting someone's followers. We'll spend more effort on social posting and ads for existing audiences. The SIFT segmentation campaign is priority four—lowest priority for totally cold campaigns.

**Mark Lim:** For positive reply follow-up, I think we'd want that as a list in HubSpot. Instantly toggles a "has replied" field. Does HeyReach have something similar?

**Natalia Moura Gaal:** Maybe we should schedule another call—you, me, Jason, Jeffrey, and Andrew if you want to participate. I want to show you what we have in HubSpot so far. Kyle downloaded all the Outbound Sync packages. We have segments for HeyReach, Instantly, and a dashboard showing all information. We can review and I can explain how it works, Jeff.

**Jason Gong:** Let me share my screen. I pulled this list yesterday. I want to see all people who replied positively to previous offers—workshop invites, breakfast, dinner. Then follow up saying we can set up a free strategy session. I filtered by first touch channel from Instantly and fit score equals good based on persona calculations in Clay. I need to filter out negative replies, but this is basically the list I'm trying to build.

**Natalia Moura Gaal:** We have HeyReach reply segments in HubSpot. I can build something on your end or work with Jeff.

**Jason Gong:** This is great. I'm looking for HeyReach message reply. Could you create a segment for positive reply, not just any reply? That would be perfect. When someone responds positively to an invite, I want to follow up saying we can help them when they seem qualified and offer a free strategy session.

**Natalia Moura Gaal:** Schedule that Outbound Sync review call for the beginning of next week. I want to show you the existing segments and dashboard.

**Gloria Willis:** I was concerned the Growth Cafe numbers were so low, but I see why now—the spam trigger word. Once we fix that and relaunch, it should be better. I have the Answer Engine copy ready—everything on my side is set. I have dates through March and half of April, so I'll start working on briefs for those and send them soon.

**Gloria Willis:** I'm going to send you a calendar invite, Jason. I need 10 minutes with you after this call.

**Jason Gong:** We could just chat right after.

**Jason Gong:** Thanks, everyone.

**Mark Lim:** Before we go, I have news. This is my last month at Understory. I'm transitioning to a marketing agency in Germany. Andrew will take over my responsibilities. I'm ensuring everything is clear with instructions and context.

**Jason Gong:** Appreciate the help. Nice to meet you, Andrew. Congratulations.

**Andrew Osborne:** Lovely to meet you, Gloria, Jason, Jeffrey. I'm looking forward to our conversations and getting to know you all better. Mark's told me a lot.

**Gloria Willis:** Great, nice to meet you too.

**Jason Gong:** All right, talk to you all later.

**Gloria Willis:** Thank you.

**Mark Lim:** See you later.

**Natalia Moura Gaal:** Bye.
