# Bi-Weekly GTM Coordination — GrowthX & Understory

<metadata>
date: 2026-02-12
time: 18:33 UTC
duration: 35 minutes
organizer: jesus@growthx.ai
participants: Jason Gong, Gloria Willis, Danni Roseman, Jesus Yepez, Jeff Ignacio, Tyler Pavlas, Mark Lim, Natalia Moura Gaal, Andrew Osborne, Alexander Fine, Naufal Nugroho, Josh Solomon
fathom_recording_id: 122055857
fathom_url: https://fathom.video/calls/564335141
share_url: https://fathom.video/share/k1YEsDFyWoNpgDWZz6t3zybRtUxY9aEm
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Align on GTM workflows, campaign prioritization, and Clay enrichment costs.

---

## Context

This is a bi-weekly synchronization between GrowthX (a B2B content marketing firm) and Understory, an agency partner. GrowthX and Understory collaborate on outbound campaigns, HubSpot setup, and data enrichment workflows to drive pipeline for both teams. The meeting surfaced a critical cost problem with the Clay enrichment workflow—Jason had just spent significant credits re-enriching a 17k-record list unnecessarily—and shifted to discussing campaign performance data and prioritization across multiple outreach initiatives.

---

## Relevance

**To GrowthX Delivery:**
- Clay enrichment workflow is bleeding credits — redesign from daily sync to webhook-triggered, intent-based enrichment to fix cost structure
- HubSpot Outbound Sync setup is foundational for follow-up workflows — need to review segments, build "positive reply" filters, and automate follow-up to event replies
- Positive reply follow-up playbook depends on clean segmentation; "reply sentiment" fields from HeyReach and Instantly need to be mapped to HubSpot

**To GrowthX Business Development:**
- Fletch's LinkedIn followers represent a high-signal audience (1:15 reply rate) — prioritize this over cold outreach; reflects repeatable pattern for other channels
- "Webflow Lookalike" campaign is a new lever for pipeline — targeting companies similar to successful customers (Lovable, Webflow) with workshop recordings + strategy sessions
- Campaign performance baseline: HeyReach 36 replies, Instantly 131 replies, Fletch 109 replies; Growth Cafe underperforming due to copy issue (now fixed)
- Team transition: Mark Lim is leaving Understory at month-end; Andrew Osborne taking over — smooth handoff critical for campaign continuity

---

## Decisions & Commitments

- **Clay workflow redesign**: Switch from daily sync to webhook-triggered processing; narrow HubSpot list to only intent-based records (email replies, new deals). Jeff will review before deployment.
- **Campaign priority stack**: (1) Breakfast & Fletch events, (2) Webflow Lookalike campaign, (3) Answer Engine event, (4) SIFT segmentation campaign.
- **Fletch followers first**: Deprioritize cold outreach for Fletch; concentrate on 10-15k LinkedIn followers (delivering 1:15 reply rate vs. cold rates).
- **Growth Cafe relaunch**: Mark will send copy to Gloria for review; launch Feb 13 if approved (spam trigger word fixed).
- **Positive reply follow-up**: Use existing HubSpot Outbound Sync segments; create new "positive reply" segment to enable strategy session follow-ups.
- **Outbound Sync review call**: Schedule for beginning of next week with Jason, Natalia, Jeff, and Andrew to review HubSpot dashboard and Outbound Sync workflow.

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

## Open Questions

- **HeyReach reply sentiment**: Does HeyReach send back reply sentiment data like Instantly does? Need to clarify for building positive-reply filters.
- **Webflow Lookalike launch timeline**: Target is "this week," but depends on Mark building the ICP list and Jason approving the outreach copy. Confirm exact launch date.
- **Outbound Sync dashboard review**: The team (Kyle, Natalia) has built HubSpot segments and a dashboard for Outbound Sync metrics. Need to review these with the full team to ensure alignment and identify any missing filters.
- **Cold outreach for Answer Engine event**: Performance was historically ~50 replies. Is the team pivoting away from cold entirely, or just deprioritizing to focus on existing audience + social/ads?

---

## Action Items

**Jason Gong (GrowthX)**
- Send Clay contact table link to Natalia; she'll disable auto-update
- Send updated HubSpot enrichment lists to Natalia; she'll rebuild Clay with Jeff's review
- Request website hosting/CMS ICP list from Mark; use to draft outreach copy

**Mark Lim (Understory)**
- Send Growth Cafe copy to Gloria for review; launch Feb 13 if approved
- Prioritize Fletch emails to LinkedIn followers; reduce cold sends
- Send website hosting/CMS ICP list to Jason by EOD

**Natalia Moura Gaal (Understory)**
- Disable Clay workbook and column "auto update" toggles to stop credit consumption
- Schedule Outbound Sync review meeting with Jason, Jeff, and Andrew; demo HubSpot setup
- Create HubSpot positive-reply segments for HeyReach and Instantly (excluding existing customers)

**Jeff Ignacio (GrowthX)**
- Review new Clay enrichment workflow before deployment; validate HubSpot list logic and intent triggers

**Gloria Willis (GrowthX)**
- Review Growth Cafe copy from Mark; approve for Feb 13 launch
- Send 10-minute post-call calendar invite to Jason
- Begin creating briefs for March/April events

---

## Transcript
**Jesus Yepez:** Hey, Mark.

**Jesus Yepez:** How's it going?

**Mark Lim:** Great.

**Mark Lim:** How are you?

**Jesus Yepez:** Great.

**Jesus Yepez:** Great.

**Jesus Yepez:** Nice to hear that.

**Naufal Nugroho:** Hey, Jason.

**Jason Gong:** Hey, Jesus.

**Jason Gong:** How are you all?

**Jason Gong:** I think Jeff accepted, but we can get started without him as well.

**Mark Lim:** Is Gloria joining?

**Jason Gong:** Gloria, probably.

**Mark Lim:** There she is.

**Jason Gong:** Cool.

**Jason Gong:** So I guess a few things on my mind today.

**Jason Gong:** The biggest one is just this, like, enrichment workflow.

**Jason Gong:** And then I know we have campaigns running, but, like, the kind of the LinkedIn automation that we wanted to spin up, like, mining for triggers and then emailing folks.

**Jason Gong:** Like, those two things are kind of top of mind for me.

**Mark Lim:** Yeah, I have it all written down in the meeting note, so I guess we can just like go through that real quick and then discuss.

**Jason Gong:** Okay, yeah, so if can get started with that clay enrichment, I definitely just have no idea how it works.

**Jason Gong:** I thought I, you know, maybe understood it and then I bought some credits and then it immediately just consumed all the credits and my money is gone.

**Jason Gong:** So I don't know how you want to get started on this.

**Natalia Gaal:** Yeah, I think, so I saw the list that you shared yesterday and I think my question is, is the enrichment, because the clay workbook that I saw, it's to enrich companies only.

**Natalia Gaal:** And then, is the goal to enrich companies only from outbound activities or like any companies with no domain?

**Jason Gong:** Yeah, so I have a list in HubSpot and the definition of who should be in that list is what I was playing around with. We can kind of talk through the logic, but I think what's happening is the membership to that list is a little bit too broad, and because of that it's kind of just consuming a bunch of credits.

**Jason Gong:** What I don't really understand is just like how this workflow works at all and it's like what I described is actually how it works because if it is how I described it then really all we have to do is just like tighten up the description of that HubSpot list and then we're good to go which I thought I did yesterday but then it just immediately consumed all my credits which is pretty sad.

**Natalia Gaal:** Yeah, so I only, to be honest, I only saw the company one, I think it was the one that Jeff was mentioning as well in one of the messages.

**Natalia Gaal:** So the one that I saw, it is what you mentioned.

**Natalia Gaal:** So it's pulling from a HubSpot list.

**Natalia Gaal:** And then I think we had like 17K people there.

**Natalia Gaal:** That's why it consumed a lot of credits.

**Natalia Gaal:** And then you also have enrichments that are pretty expensive.

**Natalia Gaal:** I think like one related to funding or something like this, that is consuming like four credits or more by role.

**Natalia Gaal:** So what I mentioned to Mark is like, if you want us to double check and improve these two workflows, we can do that with some tips.

**Natalia Gaal:** But if you want to keep the same, then it's just a matter of, you know, like improve the HubSpot list, as we mentioned.

**Natalia Gaal:** And if it's only outbound sync activity, then we can leverage some of the segments that we already have as well in HubSpot.

**Jason Gong:** Yeah, I think, I mean, honestly, like how expensive the workflow is here for enrichment.

**Jason Gong:** bit bit of of a

**Jason Gong:** It's fine to me.

**Jason Gong:** The only thing I really am looking for is just how do I make it only enrich people that, like, signal some intent.

**Jason Gong:** And there's probably, like, multiple kind of triggers for that definition.

**Jason Gong:** Like, one is replying to an email.

**Jason Gong:** One is, like, you know, just our team, like, uploading a new deal.

**Jason Gong:** So, yeah, so I'm really just looking to, like, narrow that down.

**Jason Gong:** Because I think right now what's happening is, like, it's literally enriching every company you're cold emailing, which is just really expensive and unnecessary.

**Natalia Gaal:** Yeah, maybe I can pair with Jeff.

**Natalia Gaal:** Because I don't have visibility on, you know, like, all the signals that are important for you internally.

**Natalia Gaal:** So I think maybe Jeff can help me with that.

**Natalia Gaal:** And then I can jump in with Outbound Sync activity as well.

**Natalia Gaal:** And we can review the HubSpot list and then just change the trigger in the Claywork.

**Natalia Gaal:** I don't know if that helps, Jeff, as well.

**Jeff Ignacio:** By the way, nice meeting you.

**Jeff Ignacio:** Nice meeting you, too.

**Jeff Ignacio:** So when you click, Jason, can you click on that data on open import object from HubSpot?

**Jason Gong:** It's on a schedule, it looks like.

**Jason Gong:** Yeah, so it looks like it's every day.

**Jeff Ignacio:** And how is it identifying the records to pull?

**Jason Gong:** It's pulling from this list.

**Jeff Ignacio:** Okay, so can you go up to that table, then?

**Jeff Ignacio:** The company table?

**Natalia Gaal:** Let me take this one here.

**Jason Gong:** Let me double check.

**Jason Gong:** Well, I said 17,000, but it should be this table.

**Jeff Ignacio:** Okay.

**Jeff Ignacio:** So it's...

**Jeff Ignacio:** So...

**Jeff Ignacio:** It's combing this table each day, and is it pulling incrementally, or is it pulling the record each time, all the records each time?

**Jason Gong:** That's a good question.

**Jason Gong:** don't where does it define that.

**Jason Gong:** I think that is what consumed all the credits.

**Jason Gong:** It looked like it just tried to re-enrich the entire table yesterday.

**Jeff Ignacio:** Yeah, because what I would do instead is have this table set up on a webhook instead.

**Jeff Ignacio:** So that way you only get per record going in, and the table is built incrementally as opposed to appending.

**Jason Gong:** Yeah.

**Jeff Ignacio:** It's appending cumulatively, actually, so it's going to be an exponential consumption of credits.

**Jason Gong:** Right.

**Jeff Ignacio:** If that's what I just heard.

**Jason Gong:** I agree.

**Jason Gong:** I don't know.

**Jason Gong:** Is this the setting in clay?

**Jeff Ignacio:** I'm just trying to understand. I haven't looked at this too deeply, so I thought you guys were triaging it. I just moved on to other projects.

**Natalia Gaal:** So Jason, you said you changed the source list yesterday and Clay re-enriched everything again, is that what happened?

**Jason Gong:** Yeah, I'm pretty sure that's what happened.

**Natalia Gaal:** When we change a source in Clay, it doesn't delete everything that we added before—it just changes from that point onwards. But the way this Clay workbook was built, it updated everything again, which is why it consumed all the credits.

**Natalia Gaal:** There is a way to save a table as a template, and then you can, you know, like duplicate and just change the source.

**Natalia Gaal:** Because I don't think, I mean, we can do the webhook as Jeff mentioned, but I think if we tailor, if you like organize all the filters in the HubSpot list, and then we do everything again with the template, it's not going to happen again because, you know, it's going to start from scratch.

**Natalia Gaal:** So that's how, that's another option as well to go.

**Natalia Gaal:** But I just need to know if we, and we can try, I can show you before running it, like anything.

**Natalia Gaal:** I just need to know if this is the final list that you guys are aiming to enrich.

**Jason Gong:** Yeah.

**Jason Gong:** I can, I feel like this needs to be cleaned up a little bit, but I can, so like all you need from me is the two HubSpot lists.

**Jason Gong:** That define who, what companies and what people should be enriched.

**Jason Gong:** And then you'll set up the clay.

**Natalia Gaal:** Yeah, we can do that.

**Natalia Gaal:** And then if you need help with the HubSpot list on, you know, like outbound sync properties that we are adding into HubSpot, I can take a look as well.

**Natalia Gaal:** But when we have the final HubSpot list, then we can work a little bit better.

**Natalia Gaal:** And then maybe Naufal and Mark can also check, double check to see if everything is correct.

**Natalia Gaal:** But yeah, I would go that route.

**Jason Gong:** Okay.

**Jason Gong:** Okay.

**Jason Gong:** That sounds good.

**Jason Gong:** I'll send you the two lists.

**Natalia Gaal:** How long do you think it'll take to do that?

**Natalia Gaal:** It's pretty quick, like to save as a template and then we connect.

**Natalia Gaal:** And then me, probably me and Mark, we can double check.

**Jason Gong:** It's maybe like half a day.

**Jason Gong:** Okay.

**Natalia Gaal:** And then I guess I'm still unclear on like what re-triggered all that.

**Jason Gong:** Like would it not do that the next time you...

**Natalia Gaal:** Let me try to open the Clay workbook here so I can show you.

**Natalia Gaal:** The first one is because it's running every day.

**Natalia Gaal:** So if you want to double check everything, you can change to manually before turning on.

**Natalia Gaal:** And then if you go to the foundation data, for example, and then there's the setting symbol at the bottom right, you're going to see an auto update toggle on.

**Natalia Gaal:** So that's what makes Clay run everything automatically.

**Natalia Gaal:** So you can turn this one off whenever you're making any changes on Clay.

**Natalia Gaal:** And you also have the auto update like option in each column.

**Natalia Gaal:** So each column that you are running some sort of enrichment or, you know, it's suspending some sort of some credits.

**Natalia Gaal:** You can toggle off the auto update.

**Jason Gong:** I guess I'll turn these two clay tables off first.

**Jason Gong:** I don't know how to do that.

**Natalia Gaal:** I can turn it off for you.

**Natalia Gaal:** I think if you want to send me both, I have the company one.

**Natalia Gaal:** I don't know if Jeff has the contact or you have the contact one, but I can turn them off.

**Jason Gong:** Yeah, I'll send you the contact one right now.

**Jason Gong:** Okay.

**Jason Gong:** So after this call, I'll just update the lists and then I'll ping in Slack.

**Natalia Gaal:** Okay.

**Natalia Gaal:** Sounds good.

**Jason Gong:** Cool.

**Jason Gong:** Yeah, I don't remember who set up this table.

**Jason Gong:** It's consumed, like, a lot of money.

**Jason Gong:** Okay.

**Jason Gong:** I think that's it on that table.

**Jason Gong:** I guess the next thing is the LinkedIn trigger, the email workflow you're all building.

**Jason Gong:** Any update on that?

**Mark Lim:** Yeah.

**Mark Lim:** Let me share the screen real quick and then we'll get through that. Thank you.

**Jason Gong:** I guess, Jeff, for that enrichment thing, if you could just take a look before we turn that live, because you have more context on our whole HubSpot setup, that would be awesome.

**Jason Gong:** then this other stuff, I guess you could stay for if you want more context, but it's mostly our cold outreach motion.

**Jason Gong:** Okay.

**Jeff Ignacio:** Yeah, I think for cold outreach, I don't know if we should be enriching those in the first place. I think we should only enrich the inbound ones.

**Jason Gong:** Yeah, I agree.

**Jason Gong:** I mean, I think we're just working on enriching the ones that reply, really.

**Mark Lim:** Right.

**Mark Lim:** Yeah, so since we have a lot to cover, I'm just going to briefly explain the results for this week.

**Mark Lim:** So we had 36 positive.

**Mark Lim:** Replies from HeyReach, and 131 from Instantly, it's like the most we've ever gotten, 109 from Fletch, and the rest, a little bit low.

**Mark Lim:** There's some issue with the deliverability, and I checked it, and then there was like an issue with like a spam trigger word, so I fixed that.

**Mark Lim:** So I'm planning to run the Growth Cafe campaign once again with the new copy.

**Mark Lim:** I'm going to send it to you, Gloria, so you can just review it, and then if it's good, then I will launch it again probably tomorrow.

**Mark Lim:** And yeah, we should be able to get a decent amount of replies, just like we got from last month's Growth Cafe.

**Jason Gong:** So on the Fletch one, are we still sending cold emails for Fletch?

**Jason Gong:** Are we only sending it to his LinkedIn followers?

**Mark Lim:** We are sending to the cold audience now.

**Jason Gong:** Oh, because we've, have we like gone through his LinkedIn followers?

**Mark Lim:** Is that why?

**Mark Lim:** Yeah.

**Jason Gong:** Got it.

**Jason Gong:** So there is, okay, so you sent like 9,000.

**Jason Gong:** Like how many LinkedIn followers did we end up filtering from his like 60,000?

**Mark Lim:** So there were, there were around, um, it's not fully done yet.

**Mark Lim:** The sequence is still going for the LinkedIn engager and follower.

**Mark Lim:** And there were about 15, yeah, 10 to 15,000 that were qualified.

**Jason Gong:** Okay.

**Jason Gong:** So we got a hundred, I know it's not done yet, but I just want to like kind of keep tabs on like the response rate.

**Jason Gong:** So you have 109 replies out of 15,000 followers?

**Mark Lim:** Right, so far we're getting about one positive reply per 15 leads based on finished sequences. We're sending a two-step sequence.

**Jason Gong:** So then there's only 1,500?

**Jason Gong:** Because you have 100 replies, right, and you're saying 1 in 15, so there's 1,500 people that have finished the sequence so far?

**Mark Lim:** Yeah, yeah, it's in the queue, like, there's other campaigns running.

**Mark Lim:** Like Growth Cafe and Fletch, so it is in the queue, the leads.

**Mark Lim:** So it's not fully done sending yet.

**Jason Gong:** Okay.

**Jason Gong:** I guess my only ask is, it seems like the stuff to followers is much more impactful than the just straight up cold.

**Jason Gong:** So whatever you need to do to prioritize the emails to followers.

**Jason Gong:** I mean, the Growth Cafe stuff is higher priority, but like, I guess don't message people cold if you can use that for, you know, his follower base.

**Mark Lim:** Yeah.

**Mark Lim:** Yeah.

**Mark Lim:** Yeah, we'll do that.

**Jason Gong:** Okay.

**Jason Gong:** All right.

**Mark Lim:** Cool.

**Mark Lim:** And, yeah, and for the ICP list that you requested, that's like website hosting and CMS companies, it's almost done.

**Mark Lim:** I'm going to send it to you today.

**Jason Gong:** Okay.

**Mark Lim:** Cool.

**Mark Lim:** Yeah.

**Jason Gong:** So just context for that one—we have customers that fit certain industries or verticals, and we want to experiment with outreach to similar-looking companies to try to get them interested in GrowthX. I'm thinking the sequence roughly looks like this: we've done workshops with Lovable and Webflow, and those are super relevant to this group of people.

**Jason Gong:** I'd send them the recording and ask if they want it. If they do, we get their email and nurture them through our newsletter. Then if they reply positively, we follow up with a strategy session offer where we apply that same playbook and give them a teaser of what we can do. On the copy for that one, I'd love for you guys to own this campaign.

**Mark Lim:** Right.

**Mark Lim:** So you said you wanted to launch it this week, right?

**Mark Lim:** So should it be, like, tomorrow, possibly?

**Jason Gong:** Yeah, I mean, if we have space in our cold email queue, I'd love to get started on this. It's pretty high priority for building our pipeline at the moment.

**Mark Lim:** Yeah, I actually wanted to talk about that. So we have the Answer Engine campaign that needs to be launched as well.

**Jason Gong:** Yeah, so I would say let's prioritize finishing up the Fletch one and the breakfast events first. Then, if we need the room, I'd do the Webflow Lookalike campaign, and then the Answer Engine campaign.

**Mark Lim:** Okay.

**Jason Gong:** I guess the thinking there is, like, I feel like historically the outbound for our AEO stuff hasn't done as well as the, like, going after somebody's followers.

**Jason Gong:** So we're going to spend a bit more effort on, like, the social posting and maybe, like, running some ads and going after our existing audience to get them to show up versus, like, trying to get new people.

**Jason Gong:** So it seems like when we did cold outreach for Answer Engine before, it wasn't that impactful. I think we got maybe 50 replies.

**Mark Lim:** Okay.

**Mark Lim:** Yeah, yeah, okay.

**Mark Lim:** Sounds good.

**Mark Lim:** And the SIFT segmentation campaign, so is that, like, priority number four?

**Jason Gong:** Let's see.

**Jason Gong:** Okay, like, I would almost put anything that's just totally cold, like, the lowest, and then the SIFT one, yeah, I guess it is four, so it's the Breakfast, Fletch, and Lookalikes, those are first, and then I would put SIFT after that.

**Mark Lim:** Okay.

**Mark Lim:** Okay.

**Mark Lim:** Yeah, yeah, that's good.

**Jason Gong:** So if that's possible, I mean, I would rather have it as a list in HubSpot.

**Jason Gong:** So I think with instantly, if they reply, it does toggle this like has replied field.

**Jason Gong:** I don't know if you have something similar for HeyReach, but if you do, you could just make a list in HubSpot, because then all the information is there, you know, and it's easy for Jesus and folks on the team to just just like click and see who they are, and then like send a reply, or send a follow-up.

**Mark Lim:** Okay, yeah, Natalia.

**Natalia Gaal:** Yeah, so maybe we can have another call, because I, maybe Jason and Jeff and I, Mark and Andrew, if you want to participate as well, because I want to show you what we have so far in HubSpot.

**Natalia Gaal:** Kyle downloaded all the packages. We should have all the segments for HeyReach and Instantly, and a dashboard showing all the information from Outbound Sync.

**Natalia Gaal:** We can maybe review that, and I think it would be nice to explain, Jeff, how it works as well.

**Natalia Gaal:** And if you want to make some changes, then we can do with the Outbound Sync team.

**Natalia Gaal:** So we can maybe schedule this for beginning of next week, if that's okay.

**Jason Gong:** Okay.

**Jason Gong:** I mean, I know we still have like half an hour on this call.

**Jason Gong:** Like, if I just, I don't know if you should see my screen.

**Jason Gong:** So this is the list I pulled yesterday that was trying to get at this.

**Jason Gong:** I guess, stepping back, what we're trying to do is like, cool, I want to see all the people that replied positively to some previous offer we sent.

**Jason Gong:** Like, hey, come to the workshop.

**Jason Gong:** Hey, come to a breakfast, come to a dinner.

**Jason Gong:** And then, because we didn't do this before, we'd follow up and say: hey, but if you want help, we'd love to set up a strategy session with the team at GrowthX to see if we can help you grow faster. That's the reason behind this.

**Jason Gong:** When I try to filter this list, I see you populate a "first touch channel" from Instantly. I'm not sure if that's something you're updating or if it's a workflow on our side.

**Jason Gong:** And then I filtered by like fit score equals good, which is based on some persona things that are calculated in this clay table.

**Jason Gong:** And then, so like, this is the list, you know, and it's like full of people I would love to like, message.

**Jason Gong:** So it's like, cool, VP of marketing at JotForm.

**Jason Gong:** If I open this up.

**Jason Gong:** Okay, so like, I guess, I guess we need something to filter out like negative replies.

**Jason Gong:** But if like that person said, like, hey, cool, invite me to the workshop.

**Jason Gong:** Like, that's what I'm, that's the list I'm trying to build.

**Natalia Gaal:** Yeah, if you go to segments, I can build something for you. We already have HeyReach templates set up, and I can work with Jeff to review them.

**Jason Gong:** This is great. I think this is basically what I'm looking for—HeyReach message replies.

**Jason Gong:** I guess I want to maybe filter out customers, but.

**Jeff Ignacio:** So HeyReach actually sends back, like, sentiment as well as a data point?

**Jason Gong:** That one, I guess, we'll have to look at.

**Jason Gong:** So this is HeyReach replied.

**Jason Gong:** Okay, so let's do, like, you don't actually have to make a list.

**Jason Gong:** It looks like we actually have it right here.

**Jason Gong:** But the, yeah, the one update is if you could create a segment for positive reply and not just reply.

**Jason Gong:** That would be, yeah, like, this is literally, like, perfect, right?

**Jason Gong:** Like, it's cool.

**Jason Gong:** I mean, I know we're just starting to do this, but what I would love to do is, like, well, we just invite them to something and they respond positively.

**Jason Gong:** I want to follow up with this person now and just say, like, you know, hey, but, like, we can actually help you when you seem qualified.

**Jason Gong:** Like, let's do a free, like, strategy session.

**Jason Gong:** Okay, cool.

**Jason Gong:** I think that's very helpful. Thanks for pointing me in the right direction. That covers my end. Gloria, is there anything from your side on invites?

**Gloria Willis:** No, not that we haven't already talked about.

**Gloria Willis:** I mean, I was a little concerned that the numbers were so low on replies for the Growth Cafe, but I mean, I see why now.

**Gloria Willis:** So, I mean, at this point, there's not really that much we can do.

**Jason Gong:** Wait, so it was the reason, what is the reason?

**Jason Gong:** Like, we're just not sending the emails?

**Gloria Willis:** Yeah, think, like you said, was a spam trigger word?

**Gloria Willis:** Yeah, yeah, possibly.

**Mark Lim:** Reply rates are quite, comparatively lower than the previous campaigns.

**Mark Lim:** So, yeah, I'm guessing that was the case.

**Mark Lim:** So, yeah.

**Mark Lim:** I fixed it now, and then I'll launch it again tomorrow with a new copy.

**Gloria Willis:** Yeah.

**Gloria Willis:** So it should be good.

**Gloria Willis:** You have everything you need for the Answer Engine, which is our AEO event, and you're already working on Fletch.

**Gloria Willis:** So that's everything on my side.

**Gloria Willis:** I do have most of my dates through March and maybe half of April.

**Gloria Willis:** So I will start working on briefs for those as well for you and get those out as soon as possible.

**Mark Lim:** All right.

**Mark Lim:** Sounds good.

**Gloria Willis:** If we are done here, Jason, I'm going to send you another calendar invite because I need 10 minutes with you after this.

**Jason Gong:** All right.

**Jason Gong:** We could just chat right after this call.

**Jason Gong:** Okay.

**Jason Gong:** All right.

**Jason Gong:** Thanks, everyone.

**Mark Lim:** Sorry.

**Mark Lim:** Before we go, I just have to drop the news.

**Mark Lim:** So this is my last month at Understory. I'll be joining a marketing agency in Germany. Andrew will be taking over my responsibilities, and he's already been following up with me on the accounts. I'll make sure everything is clear with instructions and context before I leave.

**Mark Lim:** So, yeah.

**Jason Gong:** Okay, well, I mean, appreciate the help.

**Jason Gong:** Nice to meet you, Andrew.

**Jason Gong:** What company are you joining?

**Jason Gong:** That's awesome.

**Mark Lim:** it's a marketing agency.

**Jason Gong:** Okay, cool.

**Mark Lim:** Yeah.

**Jason Gong:** All right.

**Jason Gong:** Well, thanks for letting us know.

**Gloria Willis:** Congrats.

**Jason Gong:** Yeah, congrats.

**Mark Lim:** Thank you.

**Gloria Willis:** Cool.

**Gloria Willis:** Well, nice to meet you, Andrew.

**Andrew Osborne:** Lovely to meet you guys, Gloria, Jason, Jeff.

**Andrew Osborne:** Looking forward to more conversations and getting to know you guys better.

**Andrew Osborne:** So, yeah, we're looking forward to it.

**Andrew Osborne:** Mark's told me a lot, so I'm really interested to speak with more of you guys.

**Gloria Willis:** Great.

**Jason Gong:** Good.

**Jason Gong:** Good.

**Jason Gong:** All right, talk to you all later.

**Gloria Willis:** Cool, thank you.

**Mark Lim:** See you later.

**Natalia Gaal:** Bye.

**Natalia Gaal:** Bye.

**Natalia Gaal:** Bye.
