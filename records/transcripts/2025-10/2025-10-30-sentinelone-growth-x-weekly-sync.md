# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-10-30
time: 13:59 UTC
duration: 30 minutes
organizer: Marisol Smith
participants: Aida Knezevic, Ankit Pahuja, Katya Luscomb, Marisol Smith
fathom_recording_id: 97979287
fathom_url: https://fathom.video/calls/457284697
share_url: https://fathom.video/share/V91Sr4Qwm3YF3rSezTv-WAboFYqauz-v
source: fathom
enriched_on: 2026-03-02 12:45 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne confirmed the CVE project launch for next Thursday (tentative), pending a Friday demo by Marcus and George and full QA review by SentinelOne's India-based teams through Monday. The strategy pivoted from a gradual SEO-driven rollout to publishing all CVEs from 2020 onward year-by-year to build a comprehensive vulnerability database, with initial publishing starting at 1,000 CVEs per month. The team also finalized the CS101 content workflow: Google Docs for drafting and feedback, then push final versions to ContentStack as drafts for preview and publishing, with future topic suggestions focused on unique, high-volume keywords.

---

## Context

This is a weekly sync between GrowthX's delivery team and SentinelOne, a cybersecurity platform client. SentinelOne and GrowthX are partnering on two major content initiatives: a CVE (Common Vulnerabilities and Exposures) database project and CS101 (Cybersecurity 101) educational content. The CVE project has been in development for three months and is nearing launch. SentinelOne's content team operates in India with India-based QA and SEO teams; GrowthX's team includes Aida (project coordinator), Katya (content operations), and Marisol (analytics). Ankit Pahuja is the primary stakeholder from SentinelOne coordinating strategy and approvals.

---

## Relevance

**To GrowthX Delivery:**
- CVE project pivoting from gradual 20/day rollout to 1,000/month comprehensive database — major acceleration requiring revised publishing workflow and Atlas template refinement.
- CS101 workflow formalized: Google Docs (drafting) → Atlas (generation) → ContentStack (preview as draft) — Katya to coordinate with engineering on implementation.
- Topic approval process tightening: future CS101 suggestions must target unique, high-volume keywords, not broad modifiers like "AI endpoint security" when base topic lacks search demand.

**To GrowthX Business Development:**
- CVE database strategy shift demonstrates demand-led approach — publishing all vulnerabilities from 2020 onward (not SEO-tool-limited lists) — positioning SentinelOne and GrowthX as comprehensive reference.
- Three-month CVE project nearing go-live signals strong delivery capability; Ankit explicitly flagged excitement about launch and readiness to support expansion.
- Ongoing new CVE workflow requirement identified — database must accept fresh vulnerabilities continuously, creating recurring services opportunity.

**To CheckThat:**
- Atlas and NVD API integration demonstrating automated content generation at scale (1,000+ CVEs/month) — potential case study for AI-driven vulnerability content.
- Topic-strategy refinement (keyword volume filtering, pillar-based prioritization) applicable to CheckThat prompt optimization and demand-led content planning.

---

## Overview

- **CVE Launch Timeline:** The CVE project launch is set for next Thursday (tentative), pending a Friday demo by Marcus and George, and a full QA and SEO review cycle starting Monday by SentinelOne's India-based teams.
- **CVE Strategy Shift:** Strategy pivots from gradual 20 CVEs/day to a comprehensive database approach, publishing all CVEs from 2020 onward year-by-year, scaling to 1,000+ CVEs per month based on strong indexing performance (929 French pages indexed in 2-3 days).
- **CS101 Workflow:** The workflow finalizes as Google Docs (drafting and feedback) → ContentStack (pushed as draft for preview and publishing), with Katya coordinating with engineering on Atlas integration.
- **Topic Strategy Refinement:** Future CS101 topic suggestions must target unique, high-volume keywords, not broad modifiers. SentinelOne's demand-led strategy requires matching search volume.

---

## Key Topics

### CVE Project Launch & Strategy

  - **Launch Timeline:** Launch set for next Thursday (tentative).
      - **Friday (Tomorrow):** Marcus and George demo the instance to SentinelOne's web team.
      - **Monday:** SentinelOne's India-based QA and SEO teams begin a full review; Ankit and Marcus provide feedback.
      - **Next Thursday:** Go-live, pending fixes from the QA cycle.
  - **Publishing Cadence & Indexing Evidence:**
      - **Original Plan:** 20 CVEs/day (now superseded).
      - **Evidence for Acceleration:** SentinelOne published 929 French CS101 pages; 800 indexed within 2–3 days (near 100% coverage), proving fast indexing and comprehensive rollout viability.
  - **New Strategy — Build a Comprehensive Vulnerability Database:**
      - **Goal:** Create a definitive reference by publishing all CVEs from 2020 onward, year-by-year.
      - **Execution:** Start with all 2025 CVEs, then all 2024, then 2023, etc., maintaining ongoing updates for newly discovered vulnerabilities.
      - **Publishing Scale:** Aim for 1,000+ CVEs per month (vs. original 200/week plan), balanced with ongoing new CVE intake.
      - **Data Source:** Use NVD API pulls to ensure completeness, not just SEO-tool-driven lists (which may underrepresent older or less-searched vulnerabilities).
      - **Integrity Note:** Ankit emphasized database integrity — include all vulnerabilities within the target year range, tag CVEs by source (NVD API vs. SEMrush suggestions) for transparency.

### CS101 Content & Workflow

  - **Q3 Deadline Crunch:**
      - **7 Article Revisions:** Katya delivering by end of day Thursday to meet Q3 deadline; Ankit to review Friday for publishing.
      - **5 New Articles:** Bumped to next week due to revision priority.
  - **Finalized ContentStack Workflow:**
      - **Process:** Draft → Feedback in Google Docs (superior for comments and change tracking) → Final approval by Mansi (SentinelOne) → Push to ContentStack as draft → SentinelOne preview and publish.
      - **Next Step:** Katya to coordinate with engineering to map data structure and add ContentStack push to Atlas workflow.
      - **P1 Priority:** The ContentStack pipeline is prioritized as P1; CVE database go-live remains P0 and should launch first.
  - **Topic Strategy Refinement:**
      - **Pattern Identified:** Current rejections show broader keywords (e.g., "endpoint security") command higher search volume than modifiers (e.g., "AI endpoint security"), creating false demand signals.
      - **New Requirement:** Topic suggestions must target unique, high-volume keywords with proven search volume (from SEMrush or similar tools).
      - **Future Refinement:** Katya exploring narrower, more specific content pillars (beyond the current broad set) to streamline research, reduce overlap, and align with demand-led strategy.

### Looker Dashboard Updates

  - **Action:** Remove non-GrowthX URLs from the Looker dashboard.
  - **Rationale:** This will isolate GrowthX content performance, making it easier to analyze.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Update CVE release plan: set go-live to next Thursday (tentative); scale from 20/day to 1,000+/month; integrate NVD API data source; add ongoing new-CVE workflow to database maintenance plan.
- Follow up with Marcus to confirm Friday demo scheduled with George for SentinelOne's web team.

**Katya Luscomb (GrowthX)**
- Deliver 7 CS101 Q3 revisions to Ankit by end of day Thursday; 5 new articles bumped to next week.
- Define CS101 ContentStack pipeline (Google Docs → final approval → ContentStack as draft); coordinate with engineering team on Atlas integration; update Ankit with implementation timeline.
- Refine topic-suggestion process: prioritize unique, high-volume keywords; explore narrower content pillars to reduce overlap and better align with demand-led strategy.

**Marisol Smith (GrowthX)**
- Remove non-GrowthX URLs from Looker topic-cluster view to isolate GrowthX content performance.

---

## Transcript
**Aida Knezevic:** Hi, everyone.

**Katya Luscomb:** Hello.

**Katya Luscomb:** How are you?

**Aida Knezevic:** Good.

**Marisol Smith:** Hi, Ankit.

**Ankit Pahuja:** Hey, how's it going?

**Aida Knezevic:** Good, how are you?

**Ankit Pahuja:** Things are good.

**Aida Knezevic:** We are almost at the finish line with the CVE project.

**Aida Knezevic:** I don't know if Mahadi is going to join.

**Aida Knezevic:** Maybe I shall wait for her to give an update.

**Ankit Pahuja:** I'm not sure.

**Ankit Pahuja:** I haven't had a chance to speak to her today.

**Aida Knezevic:** Okay, no worries.

**Aida Knezevic:** I added her to the agenda so she can kind of see what's happening.

**Aida Knezevic:** But yeah, I did update the release plan.

**Aida Knezevic:** So I got in touch with Marcus.

**Aida Knezevic:** He has access to content stack, the production instance.

**Aida Knezevic:** So he is pushing 500 CVEs to your content stack today.

**Aida Knezevic:** And then from there, my idea was, so I've kind of put together like a plan.

**Aida Knezevic:** So this is what's already been done.

**Aida Knezevic:** And then our idea was today, George Maine is also working on just improving the design.

**Aida Knezevic:** And then tomorrow, your team would review the drafts.

**Aida Knezevic:** And then on Monday, I was thinking if everything is fine, everything works out.

**Aida Knezevic:** So then we could publish the first 20 CVEs and then continue with 20 per day.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** I think there's some gap here.

**Ankit Pahuja:** We met yesterday. There's a weekly web meeting between the two. I was in that meeting to pass along the initial feedback we had.

**Ankit Pahuja:** So Friday, tomorrow, is when Marcus and George do a demo on the instance to the web team.

**Ankit Pahuja:** And when that happens, there'll be a round of QA by QA team and also the content side, SEO side of QA that we start on Monday.

**Aida Knezevic:** Okay.

**Ankit Pahuja:** Things we uncover in the QA run will need some time to fix, and then we can do a go-live.

**Aida Knezevic:** Okay. Makes sense.

**Ankit Pahuja:** I do see us going live next week. I haven't seen the frontend yet, but I was able to review ContentStack and the CMS push Marcus did. There are some changes, and I passed feedback yesterday so those could get incorporated. Any findings in the QA run will then need a fix.

**Aida Knezevic:** Okay. Let's move the go-live to next Thursday.

**Ankit Pahuja:** I'd suggest we keep the word "tentative" for the date.

**Aida Knezevic:** Okay. So tomorrow Marcus will do a demo for your team.

**Aida Knezevic:** And at the same time, probably tomorrow you can start the QA.

**Ankit Pahuja:** Actually, the QA teams and SEO team are based in India. When they do the demo, we probably can't jump on the QA or the SEO content side of things. But we could have feedback Monday when Marcus or the web team here starts. That's the plan we discussed internally.

**Ankit Pahuja:** And one thing like we publish 20 CVEs, do a kind of check. What we figured out with a couple of CS101 releases is that our crawling and indexing on Google is good.

**Ankit Pahuja:** So probably we could publish one batch and after making sure things are good, publish the rest of them the next click. We have evidence with CS101 and our localization strategy.

**Ankit Pahuja:** Like, for example, we localized and translated the entire CS101 to French language and posted it live — that was 929 pages in total, and within two to three days, 800 of those were indexed. There were a few errors, but essentially that's near 100% coverage.

**Ankit Pahuja:** That's the reason we can go live with phase one in a relatively shorter timeframe. In a couple of places I've seen, we write 800, and in others it's 500. I wanted to make sure we're on the same number.

**Aida Knezevic:** 500. I confirmed that with Marcus today.

**Ankit Pahuja:** One last thing I have to mention. After meeting yesterday with Marcus, he was to schedule a meeting on Friday with George, but that meeting is yet to be scheduled.

**Aida Knezevic:** He mentioned about a half hour ago that he's going to schedule it, but I'll follow up with him to make sure it's scheduled today.

**Aida Knezevic:** And then, Katya, do you want to go over, I mean, the.

**Aida Knezevic:** The initial 500 articles, I know that you were looking to understand, like, what's the future publishing cadence going to be like?

**Aida Knezevic:** But now with what you said about indexing, I'm wondering if this is going to be, like, if this is helpful.

**Aida Knezevic:** I mean, we were going to, Katya's plan was to push 200 pages on Friday, and then you can publish those the following week.

**Aida Knezevic:** So then every week we'll be publishing 200.

**Aida Knezevic:** But let us know if that's, like, maybe a little too gradual considering your indexing is good.

**Katya Luscomb:** Yeah, we can definitely increase that if we need to.

**Katya Luscomb:** I did one of the things that I had set up that might be helpful to run through.

**Katya Luscomb:** I can share my screen because this is a lot of words.

**Katya Luscomb:** doesn't necessarily show it clearly.

**Katya Luscomb:** But I added to your content OS.

**Katya Luscomb:** All right.

**Katya Luscomb:** Can you see my screen now?

**Katya Luscomb:** Perfect.

**Katya Luscomb:** All right.

**Katya Luscomb:** I added a CV content calendar.

**Katya Luscomb:** I'm thinking that this can give a good overview of the CVs that we're planning to push out on a rolling weekly basis.

**Katya Luscomb:** And I can adjust which CVs are on here.

**Katya Luscomb:** I just wanted to create a mock-up so that we can refine this and then get a really solid plan going out.

**Katya Luscomb:** A couple things that I was looking at.

**Katya Luscomb:** So this was based on just an initial idea of around 200 a week.

**Katya Luscomb:** And that number came from looking at the number of high-volume CVs and recent CVs and thinking that we could have all of those published by the end of the year.

**Katya Luscomb:** But we can definitely up that if we want to get all those published in the next, like, month, say.

**Katya Luscomb:** But then I also have this split up so you can see the number from each year that would be published in each week.

**Katya Luscomb:** And then if you expand this, it shows the search volume and the actual CV ID.

**Katya Luscomb:** So I just wanted to give a visual for everyone so that we could see this, and then this CV pages by status will still show like as they get pushed to content stack and published and all those different pieces.

**Katya Luscomb:** But let me know, yeah, if we want to up that number beyond 200, I can kind of crunch the actual year and search volume data again and recalibrate where I have everything organized in here.

**Katya Luscomb:** And I've only done four weeks out.

**Katya Luscomb:** I wanted to start there and get a sense of if 200 seemed reasonable or if we needed to make adjustments.

**Ankit Pahuja:** Quick questions here on some strategic bets we might want to revisit is, so when we started with the project and ideating it, we thought, okay, it makes sense to not go too far in the year when we create the vulnerability database.

**Ankit Pahuja:** For example, let's not gather vulnerabilities.

**Ankit Pahuja:** From the year 2011, because that's like history, and if people are essentially searching for vulnerabilities from that time or not.

**Ankit Pahuja:** I'm sure there might be few, because it tends to be the case there are evergreen vulnerabilities in a technology, that kinds of come up.

**Ankit Pahuja:** But I think with time, the demand for vulnerabilities and the searches fades.

**Ankit Pahuja:** So, that's the reason in all the docs that we put up, we made sure to add vulnerabilities from the year 2020 and onwards.

**Ankit Pahuja:** So, is this what we should do from a strategic bet?

**Ankit Pahuja:** Probably we might want to revisit again.

**Ankit Pahuja:** Probably from the data that we have from SEMrush or some other tool in terms of demand search.

**Ankit Pahuja:** I think a quick search or some time spent here should help.

**Ankit Pahuja:** I

**Ankit Pahuja:** That's an answer we might want to look for.

**Ankit Pahuja:** Second, I just wanted to ask, is all the content coming from Atlas or do we have manual intervention here for the CVE pages and the content?

**Katya Luscomb:** So for CVE pages specifically, the idea is that Atlas is generating those from a template and it shouldn't need human intervention once we get all of the exact portions that we want dialed in.

**Katya Luscomb:** So we shouldn't be having to go in and manually edit those, whereas the CS101 pages, those get a lot more human intervention as we go along.

**Ankit Pahuja:** Alright, so then can we just like pump this number up to, I don't know what should be the right frequency, just looking at the screen out of the box, but if it's the tool generating, then why not generate a thousand of those in the month?

**Katya Luscomb:** Yeah, we can definitely up that number.

**Katya Luscomb:** I was also thinking through, I know it came up in a call, if we wanted to do the CVEs with really low search volume, but if we're pushing out a lot and everything's getting indexed, doesn't seem like it's going to hurt anything to use up all the ones that have a search volume of 10.

**Katya Luscomb:** Because I know there's like 4,000 of those across, you know, 2020 to 2025.

**Katya Luscomb:** So I can definitely up this number and then update this plan here as well, looking at like 1,000 a month to start.

**Katya Luscomb:** And can do some more digging into seeing if there's older CVEs that have higher search volume that we'd want to include as well.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** And one call out here for the lists that we had put together, they were also SEO tools driven.

**Ankit Pahuja:** So probably they are not coming from, say, an API pull from an NVD database.

**Ankit Pahuja:** So this number itself could be a bit skewed.

**Ankit Pahuja:** So.

**Ankit Pahuja:** Say, if we look for vulnerabilities by the year, so what CMS would have and what actuals would be for the number of vulnerabilities that would have come up, there must be a delta there.

**Ankit Pahuja:** That's at least how I think because everything would not have some demand there.

**Ankit Pahuja:** So I think if we could have Marcus or someone pull the number of vulnerabilities from the NVD or the API pull the mechanism we have and maybe match what's there, and then say our list coming from SEMrush or the one that you put up now, pull up now, versus what's inside of NVD that I think should be a starting point looking at the complete scope of vulnerabilities from the year 2020.

**Ankit Pahuja:** I hope that makes sense.

**Katya Luscomb:** I think so.

**Katya Luscomb:** And once we add those, if it would be helpful, I can add a tag of the CVEs we got from your database and then the extra ones that come from that NVD pull. That makes it easy if you want to add any CVEs to your internal data as well.

**Ankit Pahuja:** The initial strategy of publishing by volume and recency is great, but to maintain database integrity, a database should be a database of everything. If you think so too, let's actually build a database that has all CVEs with internal linking and all content, so we could proudly say this is a comprehensive database of vulnerabilities for this decade.

**Katya Luscomb:** Okay.

**Katya Luscomb:** In that case, instead of balancing recency and search volume, we can start with all 2025 vulnerabilities, then all of 2024, and stay consistent updating 2025 and 2026 as they come out. That makes the strategy way easier.

**Ankit Pahuja:** Given we're now aligned to populate the database for all vulnerabilities in phases throughout November, I think that solves the purpose and builds the database year by year.

**Katya Luscomb:** Makes sense. Anything else on this point?

**Ankit Pahuja:** No, this view is looking good and strong. I'm really excited for the database we've been working on. It's been about three months now, and we're all working to get this out.

**Katya Luscomb:** It'd be nice to get it across the finish line.

**Aida Knezevic:** Yeah, it's been a minute.

**Katya Luscomb:** That was everything for the CVE pages. I did have a couple CS101 updates to share.

**Katya Luscomb:** I got the request to prioritize revisions for this week since it's the end of Q3. We'll be delivering all 7 article revisions by the end of today, so hopefully there's time to review tomorrow and send to publishing.

**Katya Luscomb:** The five new articles are going to get bumped to next week. A question came up about sending CS101 articles to ContentStack like we're doing with CVE pages — do you want to do revisions and feedback in ContentStack, or do an initial pass in Google Docs with revisions before pushing through?

**Ankit Pahuja:** I think the ideal process is once the docs are finalized after all reviews, then we push through ContentStack. Formatting and publishing happens inside ContentStack, so if you can push to ContentStack, our team can look at it as part of preview before publishing.

**Ankit Pahuja:** Would you be publishing or sending them as drafts?

**Katya Luscomb:** I think the best would be to send it as drafts so that you could all take a look.

**Katya Luscomb:** And then if it gets to a point where there aren't any revisions happening after we send it, then we could look into changing that to publishing.

**Katya Luscomb:** But submitting as draft seems like the safest option for everything.

**Ankit Pahuja:** I think we should only send once Mansi tells us everything's reviewed and we're good, then we could publish.

**Katya Luscomb:** Okay. I'll need to check with our engineering team on setting up that workflow.

**Aida Knezevic:** This is certainly possible. We already have access to ContentStack for the CVE pages, so it's just a matter of mapping the data structure and adding a final step to the Atlas workflow to push it live. We'd need the option to edit, and we can copy the final draft from Google Docs back into Atlas. Google Docs is the best way to share drafts because it's easier for comments and visibility into changes. We can just copy the final version.

**Katya Luscomb:** That was the outstanding question. So we'll draft in Google, get final approval, then send as a draft to ContentStack. I'll work with engineering and give you an update next week.

**Aida Knezevic:** We've updated your Looker dashboard with all the URLs published over the last couple of weeks. If you scroll down, you can see the performance of individual clusters and sessions. Non-GrowthX URLs are making it hard to see our cluster performance. I suggest removing non-GrowthX URLs so we can clearly see our content performance in the table. The rest of the report still shows your website performance. Marisol, we need to remove non-GrowthX URLs from the filters and same for the Google Search Console data.

**Ankit Pahuja:** There's a process where you send topics for approvals before we start writing. While reviewing, I was sitting with the team to understand how to make that process better. For all suggestions right now, we'd want you to focus on unique keywords with search volume. There's a pattern — topics like "endpoint security" have search volume, but modifiers like "AI endpoint security" don't have the same volume. That's the gap we want to fill. Our strategy has been demand-led, and that's taken CS101 to this stage. We want to continue focusing on topics with demand. That's why we approve a few from the list and not others. I just wanted to pass that feedback so you understand the reasoning, and when you suggest topics next time, you could keep that in mind.

**Katya Luscomb:** I really appreciate that. I was noticing that pattern myself in reading rejection reasons, and I was going to refine my approach. I know a few of our content pillars are fairly broad. Something we can explore is if there are more specific pillars to fine-tune the specific keywords we're targeting. That might make research more streamlined, reduce overlap, and if there's a particular pillar you want more content for, we can prioritize that and grab those, then we don't have to do line-by-line review on a weekly basis.

**Ankit Pahuja:** That makes sense. The ContentStack workflow for CS101 articles is P1, and P0 is still the CVE database we're trying to put out. I'm just prioritizing it in terms of engineering effort.

**Ankit Pahuja:** The idea is the database goes live sooner before we build the ContentStack pipeline. Next time we meet, if you could get answers and prioritize the CVE-specific things we discussed, that should be great so we have a strategy for what's next with the database. Another area to think about is the workflow for new CVEs discovered — it needs to be ongoing intake for the database.

**Katya Luscomb:** Definitely. That was in the notes. We didn't go through it thoroughly because we're upping the number, but I was considering making sure we're tracking and adding those. There's lots of room to add new CVEs as they come along, and I can more specifically add that into the plan.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I think those are all the updates.

**Aida Knezevic:** We'll be in touch over Slack, and I'll follow up with Marcus to make sure that meeting is scheduled.

**Aida Knezevic:** Thank you.

**Katya Luscomb:** Have a good one.

**Ankit Pahuja:** Bye-bye.
