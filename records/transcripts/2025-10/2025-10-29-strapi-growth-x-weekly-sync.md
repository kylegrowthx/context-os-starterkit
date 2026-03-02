# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-10-29
time: 16:31 UTC
duration: 19 minutes
organizer: Mara Leighton
participants: Mara Leighton, Vivek Shankar, Victor Coisne, Paul Bratslavsky, Golzar Yaghoubpour, Theodore Onyejiaku
fathom_recording_id: 97726557
fathom_url: https://fathom.video/calls/455590522
share_url: https://fathom.video/share/RhqXVTssQgnQ24uJh8LeVQBRxjBcNXTL
source: fathom
enriched_on: 2026-03-02 01:15 UTC
</metadata>

---

## Summary

Strapi and GrowthX reviewed content performance, discussed removing comparison tables to boost site performance, and confirmed upcoming contract renewal and product pilot. The team resolved a data discrepancy showing that GrowthX-created content is growing but overall site LLM traffic is declining, and agreed to expand analysis across all URLs to identify growth opportunities. Key action items include removing comparison tables, auditing comparison pages for outdated videos, and updating analytics reports to surface all traffic sources.

---

## Context

Strapi is a major GrowthX client engaged in a content marketing partnership covering SEO content, technical comparisons, and AI visibility. The client team includes Victor Coisne (leading the engagement), Paul Bratslavsky (engineering), Theodore Onyejiaku, and Golzar Yaghoubpour. Mara Leighton leads from the GrowthX side with support from Vivek Shankar on analytics and content performance tracking. This is a weekly operational sync focused on content production, site performance optimization, and product roadmap alignment. Strapi's engineering capacity is constrained, making efficiency a critical concern for both content updates and new feature pilots.

---

## Relevance

### To GrowthX Delivery
- **Content production cadence**: Nine articles publishing this week (vs usual seven) due to code formatting bug fix—demonstrates ability to recover from technical blockers quickly.
- **Content quality assurance**: Victor identified outdated V4 videos on high-traffic comparison pages; GrowthX conducting full comparison page audit this week to ensure all videos are current.
- **Performance optimization strategy**: Decision to fully remove (not toggle) comparison tables is lowering engineering overhead and improving site speed on top-performing pages.
- **Video strategy expansion**: Adding migration stories and V5 getting-started guides to text-heavy pages to improve digestibility and engagement on top performers.

### To CheckThat
- **LLM traffic insights**: Overall site LLM referral traffic is declining while GrowthX-created content shows growth—suggests opportunity for targeted AI content that drives LLM adoption.
- **Data discrepancy resolved**: Vivek's filtered view (GrowthX URLs only) vs Victor's full view clarified the performance story; now analyzing all URLs to identify content gaps in LLM visibility.

### To GrowthX Business Development
- **Account health**: Contract renewal in validation stage; no blockers on Strapi's side.
- **Expansion signal**: Strapi eager to pilot GrowthX's new self-serve product to reduce engineering bottlenecks—strong indicator of satisfaction and willingness to expand.
- **Resource constraints as upsell**: Strapi's engineering capacity limitations directly motivate adoption of the self-serve product; this is a repeatable problem for enterprise clients.

---

## Overview

- **Content Pipeline:** Two articles delayed by a code formatting bug will be published this week, bringing the total to nine.
- **Comparison Pages:** The large comparison table will be removed from high-traffic pages to boost performance. A full removal is preferred over a toggle to avoid engineering overhead.
- **LLM Traffic:** A data discrepancy was resolved: GrowthX-created content is growing, but overall site LLM traffic is declining. The team will now analyze all URLs to find growth opportunities.
- **Renewal & Pilot:** The contract renewal is in validation. Strapi will pilot GrowthX's new self-serve product to reduce engineering bottlenecks.

---

## Key Topics

### Content Pipeline & Quality

  - **Publishing Schedule:** Two articles were delayed by a code formatting bug (code escaping the formatter).
      - **Resolution:** The bug fix is in progress.
      - **Impact:** Nine articles will be published this week instead of the usual seven.
  - **Video Quality Control:** Incorrect, outdated V4 videos were embedded on the high-traffic WordPress and Contentful comparison pages.
      - **Action:** Victor fixed the two pages.
      - **Preventative Action:** GrowthX will audit all comparison pages this week to ensure videos are current and relevant.
      - **Strategy:** Add videos (migration stories or V5 getting-started guides) to top-performing, text-heavy pages to improve digestibility.

### Website Issues & Performance

  - **Integration Page Logos:** Logos are missing from the main landing page.
      - **Status:** The issue is a low priority due to a website bottleneck.
  - **Comparison Table Removal:** The large table at the top of comparison pages will be removed to boost performance.
      - **Decision:** A full removal is preferred over a toggle button to avoid engineering overhead.
      - **Fallback:** If removal is too complex, the table will be moved to the bottom of the page.
  - **October Performance (YTD):**
      - **Pace:** On track to match or outpace September for non-branded impressions and conversion events.
      - **Top Performers:** VS Code Extensions and Next.js for SEO articles.
      - **Hypothesis:** The May conversion peak was an unintended side effect of a massive, temporary increase in non-branded search traffic from bad forum links.

### LLM Traffic Analysis

  - **Data Discrepancy:** A conflict between Victor's and Vivek's LLM traffic data was resolved.
      - **Cause:** Vivek's chart was filtered to show only GrowthX-created URLs, which are growing.
      - **Clarification:** Overall site LLM traffic is declining, which is a concern as it should be growing with general LLM usage.
  - **New Strategy:** The team will now analyze LLM traffic across *all* URLs to identify growth opportunities.

### Renewal & Product Pilot

  - **Contract Renewal:** The renewal contract is in validation on Strapi's end.
  - **Product Pilot:** Strapi will pilot GrowthX's new self-serve product.
      - **Rationale:** To reduce engineering bottlenecks and enable the Strapi team to self-serve content updates.
      - **Status:** GrowthX is aware of Strapi's interest and will provide a timeline for the pilot.

---

## Action Items

**Paul Bratslavsky (Strapi)**
- Remove comparison table from published Strapi vs pages; if blocked, move to bottom

**Vivek Shankar (GrowthX)**
- Audit comparison pages; update/add videos; share recommendations with Paul & Theodore; implement updates
- Update Looker LLM referral report to include all URLs (not just GrowthX-created)

---

## Transcript
**Theodore Kelechukwu Onyejiaku:** How's it going?

**Theodore Kelechukwu Onyejiaku:** Hi, everyone.

**Mara Leighton:** Good.

**Vivek Shankar:** Are we, I guess we're waiting for a Yes.

**Mara Leighton:** Golzar, I appreciate your Halloween-themed background.

**Mara Leighton:** You're actually the first person I've seen with that, so I very appreciate it.

**Golzar Y.:** Thank you.

**Mara Leighton:** That's cute.

**Golzar Y.:** Thanks.

**Vivek Shankar:** It's a Google Meet.

**Vivek Shankar:** Golzar, you've had it for two weeks now, right?

**Golzar Y.:** I remember seeing it last week as well.

**Mara Leighton:** I Yeah.

**Golzar Y.:** fun.

**Golzar Y.:** I made it a couple weeks ago, and Zoom doesn't have fun backgrounds, so I took a screenshot of the Google Meet background and uploaded it to Zoom.

**Mara Leighton:** There you go.

**Mara Leighton:** Creative.

**Mara Leighton:** I'm glad you did.

**Mara Leighton:** Hey, Victor.

**Mara Leighton:** Victor, how are you?

**Victor Coisne:** Hey, everyone.

**Victor Coisne:** I'm good.

**Mara Leighton:** How are doing?

**Mara Leighton:** Good.

**Mara Leighton:** Nice to see you.

**Victor Coisne:** Good to see you, too.

**Victor Coisne:** Good to you, everybody.

**Victor Coisne:** Good morning, everybody.

**Victor Coisne:** How are you doing?

**Vivek Shankar:** Good, good, good.

**Vivek Shankar:** Good.

**Vivek Shankar:** Thank you.

**Vivek Shankar:** Thank you for the podcast mention, Victor.

**Mara Leighton:** Super, super appreciate Absolutely.

**Victor Coisne:** Sure, yeah.

**Victor Coisne:** You guys are doing great work.

**Victor Coisne:** Happy to give the credit to the people and do the work.

**Mara Leighton:** That was very thoughtful of you.

**Mara Leighton:** So we really appreciate it.

**Victor Coisne:** Awesome.

**Vivek Shankar:** All right.

**Vivek Shankar:** Let me share my screen.

**Vivek Shankar:** Sorry.

**Vivek Shankar:** I don't know which Windows went.

**Vivek Shankar:** There we go.

**Vivek Shankar:** Cool.

**Vivek Shankar:** So just running through the updates real quick.

**Vivek Shankar:** We had a bit of a technical issue with code formatting in our pipeline last week.

**Vivek Shankar:** So that delayed two articles.

**Vivek Shankar:** It's a pretty small issue, basically, when articles are super cold.

**Vivek Shankar:** The code kind of escapes that formatting and it gets published as plain text, so it's a simple enough fix that we're addressing this week, so this week we'll have nine articles instead of the usual seven, and then just a quick review of the outstanding issues, etc., we basically created a new artifact for Strapi.ai using the information that you've given us, and we're trying to just sort of see if there's any opportune insertion or any opportunities for that in articles moving forward.

**Vivek Shankar:** Running over on the issues real quick, I think the main things were from last week—there was that issue of the integration page missing their logos in the main landing page. All I know, you'd mentioned you were taking a look at it. I don't know if there's any updates.

**Victor Coisne:** I don't think so.

**Victor Coisne:** We talked about it yesterday.

**Victor Coisne:** Do you get any response to your issue, Paul?

**Paul:** No, not yet.

**Victor Coisne:** Yeah, but it's a bit of a bottleneck at the moment with the website.

**Victor Coisne:** It's like a more pressing issue.

**Victor Coisne:** So it will, hopefully we will be able to move on this later this week.

**Vivek Shankar:** Cool, no worries. And I guess you kind of answered the next one as well, but I'll check nonetheless. Is it possible to remove all the comparison pages that we've already published? I know we discussed removing it after everything is done, but since there are so many of those pages, I was wondering the ones that, especially the strapi versus ones that we've already published, is it possible to remove it just for those pages? Or is that something you feel we should do after everything is published? Mainly because those pages are getting good traffic, and we feel like removing that initial big table will certainly boost performance over there.

**Victor Coisne:** I'll let Paul answer that question.

**Paul:** So at the moment, we were discussing, like, if it would be worthwhile for us to add a toggle button.

**Paul:** Ideally, it would be great if all the comparison pages are done so we could just remove it completely, because there is, you know, like, engineering overhead from the standpoint of adding a toggle button in Strapi, and then updating our front-end UI to reflect that, and we're just not sure if that would make sense to do because it's easier just to remove that component completely.

**Vivek Shankar:** Okay. All right. I guess the trade-off is how much performance improvement versus the work—the pages are performing well, it's just that they're slightly ahead of what they were historically in terms of traffic. So I just wanted to throw it out there.

**Paul:** Like, if it's not too much of a lift, maybe removing that. Yeah, so maybe what we could do—here's an idea that I have to think out loud. Maybe if we can't remove it because there's a little bit more work, maybe if we change the order where your content shows up first and that table is just at the bottom, that could be something that's easily done and not going to require a lot of time or adding any additional features.

**Paul:** And so maybe that could be, like, a good compromise.

**Paul:** I don't know what you think, Victor.

**Victor Coisne:** Yeah, that's a good idea for sure.

**Victor Coisne:** Let's try to remove it.

**Victor Coisne:** And if this takes too much time, let's just put it at the bottom.

**Victor Coisne:** But I do want to call out something that I noticed yesterday.

**Victor Coisne:** I was on the Strapi versus Contentful page, and I noticed that there was a video that was getting started with Strapi V4.

**Victor Coisne:** So it was an embedding of a wrong video.

**Victor Coisne:** So I don't know how we missed that one, but that's something that's pretty bad, because if the page is getting traffic, we're just linking to an old video.

**Victor Coisne:** So I fixed it for both WordPress and Contentful on the fly yesterday when I saw it, but we really want to make sure it doesn't happen again for other comparative pages.

**Vivek Shankar:** We'll take a look.

**Vivek Shankar:** I think from our end, we sort of focused on the content, and I think some of those pages had videos, some of them didn't.

**Vivek Shankar:** So we'll take another look this week and just make sure, like, all the videos are kind of up to date.

**Vivek Shankar:** I think the reason we did that is because we assumed the videos were kind of the same, and it was a basic page template, so we just hit the text.

**Vivek Shankar:** But yeah, we'll take a look again at that and sort of flag those and fix it wherever it needs to be done.

**Victor Coisne:** Yeah, let me check real quick, like, if on the other strapi...

**Victor Coisne:** Versus Sanity, for instance.

**Victor Coisne:** It looks like it's not there.

**Victor Coisne:** It's only on Contentful and WordPress, but it's a shame that those two are the ones that are linked from the footer of our site.

**Victor Coisne:** They are definitely the ones that get the most juice.

**Victor Coisne:** Yeah.

**Victor Coisne:** In general, I do think if we have some videos to add to those pages, I find that if we have pages that are super text heavy, we need to make those pages more digestible by adding some visual, whether it's videos or illustrations.

**Victor Coisne:** And so I think for those ones that are getting the most traffic, let's try to see if we can put videos in there.

**Victor Coisne:** And I tried for, you know, WordPress, we have content on people migrating from WordPress to Strapi.

**Victor Coisne:** And from Contentful, think we, I forgot which one I added, but I think we can tailor, if we have like a migration story, let's put that video in there.

**Victor Coisne:** If not, we just do like a blank, you know, whatever, like getting started with strapi.v5.

**Victor Coisne:** So, yeah, I think adding videos, I think would be a good use of, if we're going to, if we see like traction with those pages, I think that's a good addition.

**Vivek Shankar:** Yeah, we'll do a little review and then sort of follow up with Paul and Theo in the channel to figure out which videos to go on, et cetera.

**Vivek Shankar:** We'll handle that.

**Vivek Shankar:** Okay, so just a quick performance update.

**Vivek Shankar:** So, yeah, basically this last bar, by the way, is October, so it's a work in progress.

**Vivek Shankar:** But obviously we have one more week of measurement to go for October.

**Vivek Shankar:** And as you can see, we're on pace to match or at least outpace.

**Vivek Shankar:** September, the top performers for the past week, pretty much the same articles that we're used to seeing.

**Vivek Shankar:** There is a VS Code Extensions article which popped up, which was pretty good.

**Vivek Shankar:** And then also the Next.js for SEO article, which I believe is a recent article that we published, I think, two, three weeks back, that showed up as well.

**Vivek Shankar:** Generally, non-branded impressions are on pace to match September.

**Vivek Shankar:** In terms of conversion events, again, October looks like it's going to match September.

**Vivek Shankar:** Obviously, we had that peak in May, and then July kind of came close to it.

**Vivek Shankar:** But then since then, we've been in this little range over here.

**Vivek Shankar:** Back in May, of course, this is just a hypothesis, but back in May, we had that huge sort of increase in non-branded search from the bad forum links.

**Vivek Shankar:** And then maybe the conversion clicks were an unintended side effect from that.

**Vivek Shankar:** Massive exposure because the number of clicks absolutely went through the roof in those few months.

**Vivek Shankar:** But generally, we're on pace to mid-September as well.

**Vivek Shankar:** In terms of cohort performance, week-on-week, all clusters saw higher traffic.

**Vivek Shankar:** Positions as well are pretty promising.

**Vivek Shankar:** And then, yeah, the next point is just regarding, this one is just regarding the strapi comparison pages, which we discussed already.

**Vivek Shankar:** But generally speaking, all clusters seem to be doing well.

**Vivek Shankar:** there is potential for refreshes, of course, which we're looking at.

**Vivek Shankar:** But generally, we're trying to balance that with new content, especially the AI content that we have been developing this week.

**Vivek Shankar:** In terms of LLM traffic, referral traffic is growing steadily.

**Vivek Shankar:** So for September, we hit a new high.

**Vivek Shankar:** October looks like it should outpace it.

**Vivek Shankar:** So generally, things are going quite well there.

**Vivek Shankar:** I haven't included the scrunch dashboard because we didn't see any changes week-on-week.

**Vivek Shankar:** I will include it next week since it will be an end-of-the-month kind of a thing.

**Vivek Shankar:** So...

**Vivek Shankar:** Generally, we're holding positions based on what we did last week, and there's no major changes in terms of what we're seeing in this group.

**Victor Coisne:** Any questions?

**Victor Coisne:** Yeah, a question on this one, Vivek.

**Victor Coisne:** I'm not seeing the same thing when I go to the Luka dashboard and look at the LLM.

**Victor Coisne:** To me, I see a decrease, so I'm not sure how yours is different from mine.

**Vivek Shankar:** Is it?

**Victor Coisne:** Is this what we picked in July?

**Victor Coisne:** Okay.

**Victor Coisne:** Yes, I'm not sure.

**Victor Coisne:** I'm not seeing the same data.

**Vivek Shankar:** Well, let me try filtering it again. Maybe this is a dashboard issue. Okay, is this what you're seeing?

**Victor Coisne:** Something like this one?

**Victor Coisne:** Yeah, correct.

**Vivek Shankar:** Yeah, yeah. Okay, this is some kind of a weird Looker dashboard issue. I'm not sure why it's doing this. We have a lot of filters on this chart, and sometimes it reacts weirdly.

**Victor Coisne:** Well, actually, I'm not seeing the same thing.

**Vivek Shankar:** Sorry, let me share my screen so you can see what I'm looking at.

**Victor Coisne:** Yeah. So I'm not filtering on anything here.

**Vivek Shankar:** Okay, so the screenshot I shared was only the ones that GrowthX has created. So under URL cohorts, if you filter out non-GrowthX URLs and integration page non-GrowthX URLs, yeah, it should show that.

**Victor Coisne:** Okay.

**Victor Coisne:** Yes, just overall, when I look at it holistically, we still have a decrease. I feel like the main issue is that referral traffic to strapi.io, the home page, is going down. To me, this is a bigger issue in terms of overall traffic, and I want to do some digging. I'm not seeing any kind of data on the Scrunch dashboard that explains that yet. But this should be growing, right, as users of LLMs in general are growing. I feel like we should be growing. I don't know why it's taking so long on Looker, but anyway.

**Vivek Shankar:** Yeah, on Looker, this chart takes a while to load, but yeah, generally, you are right.

**Vivek Shankar:** One thing that we're hoping for is maybe the comparison pages kind of boost the performance of that.

**Vivek Shankar:** We can certainly take a look at the rest of the website to see if there are any opportunities for that. But generally speaking, the ones that we've been producing show encouraging performance, as you saw from the chart. Maybe we can take the best practices we've been trying—like chunking sections and choosing certain topics—and condense them a bit to see if we can push them to other parts of the website. That might be one way to mitigate the overall traffic decline.

**Victor Coisne:** Yeah, I think that would be great.

**Victor Coisne:** For LLM, like referral traffic, I think we should include all URLs and use that as a way to identify opportunities.

**Vivek Shankar:** Okay.

**Vivek Shankar:** All right, so let's do that. Yeah, I think the only other point of discussion was the renewal. Mara?

**Mara Leighton:** Yeah, I think, correct me if I'm wrong, I think Bridget sent a contract.

**Mara Leighton:** I just wanted to confirm that she did, and if you have any questions whatsoever.

**Victor Coisne:** Nothing, I'm good.

**Victor Coisne:** We're just validating.

**Victor Coisne:** Okay.

**Victor Coisne:** That's it on our end, so it should be good to go.

**Mara Leighton:** Sounds good.

**Victor Coisne:** Yeah, and I got a preview of the upcoming product from Marcel last week, so I'm excited to get my hands on that. You know, what I shared in our last meeting, Mara, is that I want to ensure our team doesn't become a bottleneck. I want to be excited about self-serving content updates in some cases, and it seems like the new product will allow us to do that. Yeah, so we're looking forward to getting more information on when this is going to land.

**Mara Leighton:** Yep, totally.

**Mara Leighton:** I know, I'm sure you mentioned that to Marcel, maybe when you're walking through the product.

**Mara Leighton:** I also mentioned it to engineering and our operations team, just to like make it exceedingly obvious that whenever that rolls out, we would love to pilot it with you.

**Mara Leighton:** So, I'll keep you posted there, but it is definitely...

**Mara Leighton:** Top of mind for us.

**Mara Leighton:** And there's visibility like internally, obviously, that there's interest from Strapi.

**Mara Leighton:** So I'll keep you posted on the timeline once I have it.

**Victor Coisne:** That sounds good.

**Mara Leighton:** Yeah.

**Mara Leighton:** Cool.

**Mara Leighton:** Great.

**Mara Leighton:** All right.

**Mara Leighton:** Well, thanks so much, everyone.

**Victor Coisne:** Thank you.

**Golzar Y.:** Thank you.

**Mara Leighton:** Bye.

**Vivek Shankar:** Bye.

**Victor Coisne:** Bye.
