# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2026-02-25
time: 13:30 UTC
duration: 16 minutes
organizer: team@growthxlabs.com
participants: Bailey Seybolt (GrowthX), Karthipriya S (SentinelOne), Mansi Bhalothia (SentinelOne)
fathom_recording_id: 125192405
fathom_url: https://fathom.video/calls/578565750
share_url: https://fathom.video/share/Sr7X6EdveZ7ecjnfnxdAiJTWzwvWgorr
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

GrowthX reported softening LLM referral traffic from ChatGPT and Perplexity over the past two weeks and committed to diagnostic analysis, while SentinelOne holds content refresh strategy pending internal review and continues CVE expansion list with improved search volume data. Bailey will build the refresh pipeline in parallel to avoid delays, with next week's report including specific landing pages losing LLM traffic and optimization recommendations.

---

## Context

This is a weekly operational check-in between GrowthX's account lead Bailey Seybolt and SentinelOne's product/strategy leads Mansi Bhalothia and Karthipriya S. The engagement involves ongoing content marketing for SentinelOne's product categories (CS101 threat training, CVE database), with performance tracked through Google Analytics and the CheckThat AI visibility tool. The previous month saw strong gains on non-branded search rankings (avg position 22→12 for CS101), but a recent LLM referral traffic decline warrants investigation into citation patterns and tracked search prompts. Strategy decisions on content refresh and CVE list expansion were deferred for SentinelOne's internal alignment, with GrowthX building execution pipelines in parallel to maintain momentum.

---

## Relevance

- **Performance Diagnostics**: LLM referral traffic decline (ChatGPT, Perplexity) requires root-cause analysis; cross-referencing citation vs. referral data and CVE page impact identified as priority
- **Content Strategy**: Content refresh pipeline approved in principle; SentinelOne deferring decision to internal review; calibration approach with 2-article test recommended to validate methodology
- **CVE Expansion**: Revised 2024–25 list being corrected for missing SEMrush search volume; execution to commence week of Feb 26
- **Tooling**: CheckThat access blocked by known authentication bug affecting Karthipriya; escalation to tech team required; Mahendra access pending
- **GA4 Instrumentation**: Full event mapping needed to properly interpret custom report data; Ankit (SentinelOne) to provide mapping
- **Competitive Research**: Threat Actor Database moving forward pending internal appetite discussion; GrowthX to share competitor examples for review

---

## Overview

- **LLM traffic is softening,** driven by declines from ChatGPT and Perplexity. GrowthX will diagnose the cause (e.g., low-value pages) and report back next week.
- **Content refresh strategy is on hold** pending internal SentinelOne review. GrowthX will build the technical pipeline in parallel to avoid delays.
- **The 2024–25 CVE expansion list is being revised** by a technical SEO expert to correct for missing SEMrush search volume data, ensuring the new list is comprehensive.
- **Check That tool access is blocked** by a known bug preventing login. GrowthX is escalating the issue to its tech team for a fix.

---

## Key Topics

### Performance & Diagnostics

  - **CS101 Performance:**
      - Non-branded search position improved from 22 → 12.
      - Impressions and engagement are scaling; top pages show 65–80% engagement.
  - **LLM Referral Traffic Softening:**
      - **Problem:** Referral traffic from ChatGPT and Perplexity has declined over the last two weeks.
      - **GrowthX Diagnostic Plan:**
          - Cross-reference citation data with referral data to identify which pages are losing traffic.
          - Analyze CVE pages' specific impact on LLM referrals.
          - Review tracked prompts to ensure they accurately reflect SentinelOne's target audience.
      - **SentinelOne Request:** Identify the specific directory (CS101 vs. CVE) and pages losing traffic.

### Content Strategy & Pipeline

  - **Content Refresh Strategy:**
      - **GrowthX Proposal:** A separate pipeline to improve existing content.
          - **Goal:** Boost ranking for articles stuck on pages 2–3.
          - **Method:** Update and deepen context while preserving current rankings.
          - **Process:** Calibrate the approach with a 2-article test.
      - **Decision:** On hold for internal SentinelOne review (Mansi, Karthi, Ankit).
  - **2024–25 CVE Expansion List:**
      - **Problem:** SEMrush data was missing search volume, creating an incomplete list.
      - **Solution:** A technical SEO expert is revising the list to ensure it is comprehensive.
      - **Action:** Execution on the new list will begin next week.
  - **CS101 Content Pipeline:**
      - **Status:** Healthy backlog of \~30 topics in production.
      - **Action:** SentinelOne to review keyword recommendations for future planning.
  - **Threat Actor Database:**
      - **Action:** GrowthX to share competitor examples ("comps") on Slack today.
      - **Decision:** SentinelOne to discuss the project's internal appetite after reviewing the comps.

### Tooling & Admin

  - **Check That Tool Access:**
      - **Problem:** Karthi was blocked by a known bug ("couldn't find your account") during login.
      - **Action:** GrowthX to escalate the issue to its tech team for a fix.
      - **Access Request:** Mahendra also requires access.
  - **GA4 Event Mapping:**
      - **Need:** A full mapping of GA4 events is required to interpret data from the new custom report.
      - **Action:** Ankit (SentinelOne) will provide the mapping.

---

## Action Items

**Mansi Bhalothia (SentinelOne)**
- Confirm refresh approach with Ankit; update Bailey by Feb 26

**Bailey Seybolt (GrowthX)**
- Build separate content refresh pipeline; prep calibration artifacts
- Post Threat Actor Database competitor examples in Slack for Karthipriya/Mansi
- Add Mahendra (SentinelOne) to CheckThat tool access
- Fix Karthipriya's CheckThat login issue; escalate known account bug to tech team; update Karthipriya on Slack
- Diagnose LLM referral drop: cross-reference citation data with referral data, assess CVE page impact, review tracked prompts for audience relevance; report findings and optimization recommendations next week

**Karthipriya S (SentinelOne)**
- Share CS101 keyword recommendations feedback with Bailey

**Ankit Pahuja (SentinelOne)**
- Provide complete GA4 event mapping to Bailey for custom report interpretation

---

## Transcript
**Bailey Seybolt:** This meeting is being recorded.

**Bailey Seybolt:** Hi, team.

**Karthipriya S:** Mansi.

**Mansi Bhalothia:** Hi.

**Bailey Seybolt:** How are you all today?

**Karthipriya S:** Yeah, good, Bailey.

**Karthipriya S:** Hope you are doing good.

**Bailey Seybolt:** I'm good.

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** I'm good.

**Bailey Seybolt:** We've had some crazy weather on the east coast of the U.S.

**Bailey Seybolt:** last week.

**Karthipriya S:** Okay.

**Karthipriya S:** Hope things are fine now.

**Bailey Seybolt:** Yeah, we're, I'm all good now, but I think we've had like three feet of snow.

**Bailey Seybolt:** So it's been kind of a crazy week for a lot of people here, but all good now.

**Karthipriya S:** Stay safe.

**Bailey Seybolt:** Yeah, thank you.

**Bailey Seybolt:** Do you know, is Ankit coming today?

**Bailey Seybolt:** Should I jump in or should I wait a minute to see?

**Karthipriya S:** No, Ankit is not joining.

**Karthipriya S:** I think we can continue.

**Bailey Seybolt:** Okay, I will just jump right in then.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So I think no big, huge updates published.

**Bailey Seybolt:** We're continuing to publish the CVEs as usual.

**Bailey Seybolt:** We're creating the expansion list for 2024 and 2025.

**Bailey Seybolt:** I've asked our technical SEO experts to step in and help us create the list because I found that I felt like the data in SEMrush was missing some of the search volume there.

**Bailey Seybolt:** So hopefully we'll have a full list for that and we can start, go back and start executing on that next week.

**Bailey Seybolt:** I just wanted to make sure we weren't missing anything.

**Bailey Seybolt:** For CS101, we're all good.

**Bailey Seybolt:** We still have about 30 topics.

**Bailey Seybolt:** So I think a good runway of content there.

**Bailey Seybolt:** So foreign production, and then we have some time to kind of review some of those recommendations that I shared.

**Bailey Seybolt:** with you as well and kind of for your team to decide.

**Bailey Seybolt:** What direction we want to take to act on those.

**Bailey Seybolt:** So no big concerns there.

**Bailey Seybolt:** In terms of just the content strategy review I shared, oops, that should be, for last time, I didn't know if your team had had a chance to kind of dig into some of those recommendations and want to make sure if you had any questions or kind of any concerns that we had time to talk talk through them now.

**Bailey Seybolt:** I realize without Ankit here, if it makes more sense, we can also touch base about those next week when he's on the call as well.

**Mansi Bhalothia:** So I just went through the list of the recommendation phases.

**Mansi Bhalothia:** With approach and guidelines for refresh, I just wanted to confirm, will you give suggestions that we can incorporate or will you directly do those?

**Mansi Bhalothia:** In that particular article.

**Mansi Bhalothia:** So how is it going for the refreshes?

**Bailey Seybolt:** Yeah, no, that's okay.

**Bailey Seybolt:** So for the refreshes, I think we would take a slightly different approach.

**Bailey Seybolt:** Usually what we do, one of the reasons I asked about this is we usually create a separate pipeline to refresh articles than we do for the normal pipeline.

**Bailey Seybolt:** And the reason there is because it depends a little bit on the article itself.

**Bailey Seybolt:** But for anything that's already been indexed and is ranking, we obviously, we don't want to just toss it all out and start all over again.

**Bailey Seybolt:** The goal there would be to improve the content, to update it, to deepen the context with the idea of giving it a boost and kind of pushing it on to page one.

**Bailey Seybolt:** If it's especially content that's sort of kind of stuck at page two or three, this is often the best way to just kind of give it that push it needs to climb the rankings.

**Bailey Seybolt:** And then I think if there's content that's kind of old, that's not.

**Bailey Seybolt:** Ranking, we would sort of assess that and see if we should just kind of take a different angle on it and start over again.

**Bailey Seybolt:** But the goal here is really to kind of, for things that are already ranking or performing, to change them as little as possible in a way that's going to hurt the rankings, just to kind of improve the content, to give it that extra boost.

**Bailey Seybolt:** So, and then obviously, you know, I think if your team has specific guidelines in terms of the way you would want us to approach refreshes, we could build that into the pipeline as well.

**Bailey Seybolt:** And I think we would treat this a bit like a calibration like we did in those early articles where I would love to run, you know, maybe two and just get a sense from you and get feedback from your team on if that feels like kind of the right approach.

**Bailey Seybolt:** So we wouldn't just kind of start, jump right in.

**Bailey Seybolt:** We would want to kind of calibrate.

**Bailey Seybolt:** And make sure that you were comfortable with the approach we were taking.

**Mansi Bhalothia:** Yeah, that makes sense.

**Mansi Bhalothia:** Karthipriya and I were also discussing. I think we can discuss more once Ankit is there, and we can internally also review how we can approach for those particular articles.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So maybe I'll plan to – we'll hold off on this for now until you sort of have a chance to discuss the approach internally, or would you prefer we run one just as a test?

**Mansi Bhalothia:** Can I just discuss it with Hunkit and get back to you by tomorrow, UD?

**Bailey Seybolt:** Yes, of course.

**Bailey Seybolt:** Yeah, no problem.

**Bailey Seybolt:** Sometimes I find it's easier to, like, have an actual article to inform your discussion, but I'm also happy to just press pause until you have a chance to discuss it internally and define that.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** So I'll wait to sort of hear back from you all, but we'll go ahead and get started on just

**Bailey Seybolt:** Creating that pipeline, because that takes a bit of engineering time to do that.

**Bailey Seybolt:** So we can get started on that.

**Bailey Seybolt:** So hopefully it's ready to go once you have a chance to talk through it.

**Bailey Seybolt:** And we can kind of create separate artifacts to refine the approach there as well.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** And then for the CS101, I was wondering if you had had a chance to take a look at that list of keywords and had any kind of overall overall feedback there.

**Mansi Bhalothia:** Karthi, do you have, did you get a chance to run through those keywords?

**Karthipriya S:** Mahendra will have more clarity on this. I'll get back to you on that, Bailey.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** Sounds good.

**Bailey Seybolt:** Like I said, we have some articles in the backlog to run on.

**Bailey Seybolt:** So this is really just kind of for planning what our next stage is.

**Bailey Seybolt:** For the Threat Actor Database, I know Ankit asked to pull together some comp examples.

**Bailey Seybolt:** So I'm pulling those together.

**Bailey Seybolt:** Our technical SEO expert who did the research was out of office.

**Bailey Seybolt:** So I asked him yesterday to see if he had some good comps.

**Bailey Seybolt:** So I will share those as soon as I have those today.

**Bailey Seybolt:** I'll just put them in Slack.

**Bailey Seybolt:** And then I know that there was going to also be some kind of conversations gauging the internal appetites to do that too.

**Bailey Seybolt:** So I'll share those.

**Bailey Seybolt:** But I'll just assume that we'll kind of circle back on that when you've had a chance to talk about that internally.

**Bailey Seybolt:** Okay.

**Bailey Seybolt:** think that was – go ahead.

**Karthipriya S:** When will we get the competitor examples for the Threat Actor Database? I'm hoping that's coming soon.

**Bailey Seybolt:** I was hoping to just drop it on Slack today.

**Karthipriya S:** Okay, got it.

**Bailey Seybolt:** So I'll share those on Slack today.

**Bailey Seybolt:** And then I know we talked for the GA4 event mapping, we sort of talked about the most kind of important event yesterday, but I think it would probably still be helpful to sort of have a mapping to the full list.

**Bailey Seybolt:** As we kind of, now that we have this custom report, as we start kind of sharing those findings, it would be useful to have an understanding, I think, of what those events map to.

**Bailey Seybolt:** So I think when you get a chance, it would be helpful for your team to share that.

**Karthipriya S:** Yeah, either Ankit will be, mostly Ankit will be sharing you with the GA4 events.

**Bailey Seybolt:** Okay, perfect.

**Bailey Seybolt:** Thank you.

**Bailey Seybolt:** For CheckThat, I've added your team. You should have a link in your email inbox that allows you to connect to the SentinelOne account and access our CheckThat AI visibility tool. It's a new tool and there have been a few bugs with account setup. If you have any issues, let me know on Slack and I'll look into it.

**Bailey Seybolt:** Hopefully it all goes smoothly.

**Bailey Seybolt:** If there's anyone else on your team who needs access, let me know and I can add them.

**Karthipriya S:** Mahendra will need access.

**Bailey Seybolt:** Okay, perfect. I'll add him.

**Karthipriya S:** I got the invitation email, but when I tried to log in, it asked for my email and said "couldn't find your account." Do I need to sign up, or just log in?

**Bailey Seybolt:** The link should take you to a page where you can accept the invitation directly. That's the bug we've been seeing—it's not connecting to your account properly. Let me look into that with our tech team and get back to you. We'll see if there's something you need to do on your end or if we need to fix it from our side. Sorry about that.

**Karthipriya S:** No issues.

**Bailey Seybolt:** In terms of reporting, we'll do full February performance reporting next week with a full retrospective on the month. But here's a quick snapshot. This data is from CheckThat, the new tool we're moving to from Scrunch. The data looks solid. CS101 is still holding steady at the top position, up from 39% over the last 30 days, and trending in the right direction. For CS101, non-branded search position improved from 22 to 12 over the last month, impressions are scaling, and engagement is trending up. The top landing pages are hitting 65–80% engagement rates consistently, which is great to see.

**Bailey Seybolt:** The one thing I'd like to look into more is that over the last two weeks, LLM referral traffic has been softening—not drastically, but enough that I'd like to dig into it more for diagnostics.

**Bailey Seybolt:** There are a couple things I want to look at. First, I'm going to cross-reference citation data with referral data to see which pages are losing traffic. Sometimes it's just a refinement where low-value pages are losing traffic, which may not materially impact overall value. Second, I'd like to look at CVE pages specifically to see how they're affecting LLM referrals. Third, I want to review the prompts we're tracking to make sure our visibility and citation numbers accurately reflect your audience and the questions you care most about. It's not a direct connection, but we rely on this to understand performance, so I want to make sure we're not missing anything. I'd like to dig in more on these diagnostics and see what's actually happening.

**Bailey Seybolt:** I'll follow up with the full report next week with more detailed information.

**Karthipriya S:** That would be helpful. I'd also like to understand which directory specifically—CS101 or CVE—is seeing the LLM traffic drop.

**Karthipriya S:** And also if it is something on CS101, we'd like to know what are those pages that is losing the traffic, LLM traffic.

**Bailey Seybolt:** Yeah, exactly.

**Bailey Seybolt:** So I'll see that's where I'll start to see what landing pages are losing the LLM traffic.

**Bailey Seybolt:** So we can get a sense of what the value is there and kind of that I think.

**Karthipriya S:** And I could say it's only specifically.

**Karthipriya S:** can

**Karthipriya S:** On ChatGPT, mainly?

**Bailey Seybolt:** Yes, yes.

**Bailey Seybolt:** ChatGPT and Perplexity have both declined.

**Bailey Seybolt:** But I think, yeah, ChatGPT, because that's obviously been most of the referral traffic, is the one that's sort of the one that I would like to dig into the most since it accounts for such a large percentage of it.

**Bailey Seybolt:** The newer platforms are still growing from a smaller base. Doing more diagnostics on which pages are losing traffic will give us a better sense of what's happening. I'll dig into that for next week's report and come back with diagnostics on what's going on and suggestions for optimization.

**Karthipriya S:** Sounds good.

**Bailey Seybolt:** That's it from my end. Is there anything else you wanted to discuss?

**Karthipriya S:** Nothing else. For the CVE series we've published, we're waiting for the revised 2024–25 list with the higher search volume data that we missed in the initial list.

**Bailey Seybolt:** We should have that this week so we can start executing on it next week.

**Bailey Seybolt:** I'll get you those competitor examples for the Threat Actor Database and drop them in Slack as soon as I have them.

**Karthipriya S:** Thanks. That would be helpful.

**Bailey Seybolt:** Thanks to you both. Have a good day.

**Karthipriya S:** You too. Thanks for the update.
