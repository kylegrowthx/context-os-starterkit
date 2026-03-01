# Outreach <> Growth X - Weekly Sync

<metadata>
date: 2026-01-28
time: 17:30 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
enriched_on: 2026-02-28 12:00 UTC
participants:
  - name: Jo Kaminska
    email: jo@growthx.ai
    company: GrowthX
    role: Engagement Manager
  - name: Maria Akhter
    email: maria.akhter@outreach.io
    company: Outreach
  - name: Hadassah Pegado
    email: hadassah.pegado@outreach.io
    company: Outreach
    role: PMM
  - name: Andrew Arasaki
    email: andrew.arasaki@outreach.io
    company: Outreach
    role: Analytics/GTM Lead
  - name: Paul Galvin
    email: paul.galvin@outreach.io
    company: Outreach
    status: Not present (conflicting meeting)
fathom_recording_id: 117878684
fathom_url: https://fathom.video/calls/545967415
share_url: https://fathom.video/share/eFbWNyDxvywzPkojkBiMKieAkZhSxbFd
source: fathom
</metadata>

---

## Summary

GrowthX and Outreach aligned on finalizing a new persona-led LLM content strategy (370 prompts ready, pending Hadassah's review EOW) while uncovering critical GA4 tracking errors where sessions exceed clicks and contaminated UTM parameters obscure organic performance. GrowthX agreed to audit Outreach's GTM scripts and SPA tracking setup.

---

## Context

Outreach is shifting content strategy from generic topic coverage to persona-specific messaging targeting CROs, CFOs, and other decision-makers with day-to-day focused content (e.g., pipeline velocity vs. budget alignment). GrowthX has prepared 370 prompts tagged to new topic clusters and is awaiting Hadassah's async review to finalize the content calendar and assign 60-80 topics. In parallel, data quality issues emerged: GA4 shows sessions exceeding GSC clicks (Nov: 21k clicks → 11k sessions), contradicting normal funnel logic, and custom UTM scripts are polluting GA4 with non-standard mediums (article: 55k, blog: 11k, organic: <10k). Andrew suspects Outreach's Single Page Application architecture may compound the issue.

---

## Relevance

**Content & Strategy**
- New persona-led approach aligns across marketing (PMM feedback from Hadassah) and content execution (GrowthX strategy).
- 370 prompts ready; 60-80 assignments pending strategy sign-off and writing guideline updates.

**Data & Analytics**
- Critical GA4/GSC discrepancy indicates fundamental tracking error, not normal margin.
- UTM contamination via GTM cookies obscures true organic performance; SPA architecture suspected as contributing factor.
- GrowthX to review GTM scripts and GA4 channel definitions; Andrew to provide Google's recommended definitions.

**Execution & Dependencies**
- Hadassah's EOW review is a hard blocker for content calendar finalization and topic assignments.
- GTM access grant and technical audit by GrowthX required before resolving data issues.

---

## Overview

- **Critical Data Discrepancy:** GA4 sessions now exceed GSC clicks (e.g., 21k clicks → \~11k sessions in Nov), reversing the normal funnel and indicating a major tracking error.
- **GA4 Data Contamination:** Custom GTM scripts are polluting GA4 data with non-standard mediums like `article` (55k sessions) and `blog` (11k sessions), obscuring true organic performance.
- **Content Strategy Blocked:** The new LLM-driven strategy is blocked pending async review by Hadassah (due EOW), which is required to finalize the content calendar and assign 60–80 new/refresh topics.
- **Action Plan:** GrowthX will audit Outreach's GTM scripts and GA4 configuration to diagnose and fix the data issues.

---

## Key Topics

### Data Tracking Issues

  - **Problem 1: GA4 vs. GSC Discrepancy**
      - **Finding:** GA4 sessions now exceed GSC clicks, reversing the expected funnel.
      - **Significance:** This indicates a fundamental tracking error, as clicks should always be ≥ sessions.
      - **Example (Nov):** 21k GSC clicks → \~11k GA4 sessions.
  - **Problem 2: GA4 Data Contamination**
      - **Finding:** GA4 data is polluted with non-standard mediums, obscuring true organic performance.
      - **Example Mediums & Sessions:**
          - `article`: 55k
          - `blog`: 11k
          - `organic`: \<10k
      - **Cause:** A GTM script sets UTMs as cookies, which are then reapplied on return visits.
      - **Hypothesis:** The site's Single Page Application (SPA) architecture may be interfering with standard tracking.

### Content Strategy & Execution

  - **New Strategy Status:**
      - 370 prompts are ready in Sprint, tagged to new topic clusters.
      - **Blocker:** Execution is paused pending async review by Hadassah (due EOW).
      - **Goal:** Secure buy-in to finalize the content calendar and assign 60–80 topics.
  - **Persona-Led Content:**
      - **Goal:** Shift from generic topics to persona-specific content (e.g., CROs, CFOs).
      - **Rationale:** To address specific, day-to-day goals (e.g., pipeline velocity) instead of general concepts (e.g., budget alignment).
      - **Action:** Hadassah to provide benchmark examples (good/bad) to update writing guidelines.
  - **Listicle Refresh:**
      - **Goal:** Refresh the "11 tools..." listicle to improve its \#6 rank.
      - **Plan:** Add more tools and categories.
      - **Decision:** Include competitor Gong if a strong value-based use case can be made to overcome internal resistance.

---

## Action Items

**Jo Kaminska (GrowthX)**
- Draft call-chucking listicle brief and propose Gong inclusion to Hadassah
- Confirm GrowthX GTM reviewer with Kyle, then coordinate GTM access grant with Andrew
- Review GA4/GSC and SPA tracking with GrowthX technical team; follow up with Andrew by EOW with findings and next steps

**Hadassah Pegado (Outreach)**
- Complete async review of new content strategy by end of week
- Share persona-led content examples (good and bad) with Jo to update writing guidelines
- Ensure PMM feedback on "11 tools..." listicle brief is collected and shared

**Andrew Arasaki (Outreach)**
- Grant GrowthX team member GTM access for script audit
- Send GA4 channel definitions document (Google's recommended definitions) to Jo

---

## Transcript
**Jo Kaminska:** This meeting is being recorded.

**Maria Akhter:** Hi, Jo.

**Maria Akhter:** How's it going?

**Jo Kaminska:** Good.

**Jo Kaminska:** Can you hear me all right?

**Maria Akhter:** Like, is there any noise?

**Maria Akhter:** Yeah, no, totally fine.

**Jo Kaminska:** Are you at a coffee shop today?

**Jo Kaminska:** No, I'm working in a co-working space.

**Jo Kaminska:** And I don't know why, but today's super busy.

**Jo Kaminska:** So I have many folks around and many people chatting.

**Jo Kaminska:** So just checking in.

**Maria Akhter:** No worries.

**Maria Akhter:** I can hear you totally fine.

**Maria Akhter:** That sounds fun.

**Maria Akhter:** Co-working spaces are...

**Maria Akhter:** I need to check that out, too, because I work fully remote.

**Jo Kaminska:** So sometimes it's nice to kind of go into, like, a space with other people, too.

**Jo Kaminska:** Yeah.

**Jo Kaminska:** Yeah, yeah, for sure.

**Jo Kaminska:** Are you also in SF or?

**Maria Akhter:** I'm in Sacramento, Davis.

**Maria Akhter:** Like I'm an hour and a half north of SF.

**Jo Kaminska:** Okay.

**Maria Akhter:** So there isn't like an office near me necessarily that I could go to.

**Maria Akhter:** think there's like one co-working space they opened up downtown.

**Jo Kaminska:** So maybe I'll check that out.

**Jo Kaminska:** Yeah, I do recommend.

**Jo Kaminska:** Hi, Andrew.

**Andrew Arasaki:** Hi everyone.

**Jo Kaminska:** Hi.

**Jo Kaminska:** Hi, everyone.

**Hadassah Pegado:** How are you doing?

**Jo Kaminska:** Good, good.

**Jo Kaminska:** How are you doing?

**Hadassah Pegado:** We're good.

**Hadassah Pegado:** How are you?

**Jo Kaminska:** Yeah, I'm very good.

**Jo Kaminska:** Thank you.

**Jo Kaminska:** Andrew, I think we've been having a chance to meet, I guess.

**Jo Kaminska:** So just saying hi.

**Jo Kaminska:** I'm an engagement manager here at GrowthX and happy to chat about data analytics today.

**Jo Kaminska:** Cool.

**Jo Kaminska:** So I think we could start. We have a couple of things on our agenda. Let me pull up the documents.

**Hadassah Pegado:** Andrew, you know if Paul is going to be joining us too or if it's just going to be you?

**Andrew Arasaki:** He has a conflicting DNA meeting, so it's just going to be me.

**Jo Kaminska:** No worries.

**Jo Kaminska:** Okay.

**Jo Kaminska:** Yeah, I think we can manage and we can dive into data and any questions that you may have.

**Jo Kaminska:** Just a quick note for the content team. We've updated two topics for this week based on feedback from your team on the listicles. As part of the LLM strategy, we're prioritizing customer intelligence platforms and sales forecasting tools. We're also refreshing the "11 tools" listicle we created in October, which is currently ranking at position six. Our goal is to move it to the first position by adding more tools and categories. We'd like PMM feedback on the brief before execution. One question: would you like us to include Gong in the listicle? It would be natural to include them, but we understand there's some hesitation around featuring direct competitors.

**Hadassah Pegado:** I think people won't want to include Gong outright, but if we have a strong use case showing the value of including them, we might get buy-in. I'm leaning toward they'll say no, but it's worth bringing it up and seeing if we can make the value case work.

**Jo Kaminska:** Makes sense. We can approach it that way. We're planning to include tools like Mystical, Cloud Talk, Sales Loft, and HubSpot. We could position Gong similarly if the use case aligns with how we're presenting these tools.

**Hadassah Pegado:** Yeah, perfect. That works.

**Jo Kaminska:** Great. We've also prepared several pieces for your review from last week. We have 370 prompts ready in our Sprint environment, divided by tags that correspond to topic clusters according to the new content strategy. Since Andrew is here and we want to focus on analytics, I'll defer the detailed strategy discussion. But I wanted to check on timelines for your async review and see if there's anything else you need from our end right now.

**Hadassah Pegado:** What do you mean by the timeline aspect?

**Jo Kaminska:** I want to ask if you can review the new strategy, the overall strategy direction, and the topic clusters—especially the division between decision makers and users and their corresponding clusters. I'm happy to address your comments asynchronously. Once we have your buy-in on the content strategy, we can finalize the content calendar and assign 60 to 80 topics (both new and refreshes) to align execution with the strategy.

**Hadassah Pegado:** Got it. I can have that completed by end of week. By Friday, I'll have my notes in there and provide input on the overall strategy. I did a quick glance and it looked really great.

**Jo Kaminska:** Great. I'll dive in deeper to make sure we haven't missed anything, but I'll have it wrapped up by end of week.

**Jo Kaminska:** One thing I'm considering is adding a competitive landscape analysis comparing Outreach with Clarity and Sales Loft—showing their organic presence and how you stack against them. Let me know if you'd like to see that. Also, on the audit front, we have a new single plugin starting this week. I've reviewed the first version and it looks good. On the artifact updates, the articles are live on your site. If you have questions or comments, talk to Joanne about any updates.

**Hadassah Pegado:** Everything looks good based on PMM feedback. I got a couple of notes that I'll add to Notion for Jen. The materials you shared were incredibly helpful—they're based on our LDPDFs and make everything align perfectly. Our PMMs will share any updates they make to the bill of materials with us, so we can keep everything fresh and in sync with what we have in RN2.

**Jo Kaminska:** Perfect. Your materials have been incredibly helpful to us since we're building on top of LDPDFs.

**Jo Kaminska:** And a quick note on the changes we're planning for content execution. We want to add more persona-led content—especially hooks and messaging specific to CROs and CFOs. For example, instead of generic messaging, if you're a CFO, we'd show a sales topic but frame it around budget and consolidation. It's about addressing their specific day-to-day concerns rather than general concepts.

**Jo Kaminska:** I already shared some great examples from the automation space and enterprise platforms for mid-market and enterprise audiences. It's about talking to the CRO about pipeline velocity—their actual day-to-day focus—rather than generic budget alignment. Each piece should target one persona and address their specific day-to-day goals and concerns.

**Hadassah Pegado:** I love that. That's exactly where we want to move forward from a content perspective, not just SEO but across the website. We're making sure we're hitting the personas we really want to target. This is definitely aligned with what we're doing.

**Jo Kaminska:** If you have examples of content—landing pages, white papers—that show the tone and approach you want, sharing those as benchmarks would really help us update our writing guidelines. Show us good examples and bad examples so we can calibrate our work.

**Hadassah Pegado:** Will do. Sounds good.

**Jo Kaminska:** Great. We're getting closer to the finish line on the new content calendar. We still have a few topics from the old calendar, but the new one will be strongly based on the new strategy. I think we're in a good place. Now let's move to the data analysis—do you have any questions before we dive in?

**Jo Kaminska:** Andrew, did you have a chance to review the data analysis? Any questions before we dive in?

**Andrew Arasaki:** Thanks for taking the time to go through this with us. Paul and I looked through the data analysis. I requested direct access but haven't gotten it yet, so I haven't been able to do a deep dive myself. But we have some questions about how you're pulling the data and how Looker Studio is potentially pulling it in.

**Andrew Arasaki:** The GSC data looks straightforward, but we're wondering how you're defining sessions when comparing clicks to sessions. Are you pulling raw data from Looker or from GA4 directly?

**Jo Kaminska:** Good question—this comes up with most customers. Our Looker dashboards pull from two data sources: Google Analytics and Google Search Console. We're pulling your instances and reshaping the data into specific dimensions and metrics. For example, the first tab pulls from GA4, non-branded impressions from GSC, conversion data from GA4. We also have cohorts—think of them as topic clusters—pulled from our Airtable. This shows how specific content clusters perform. Landing pages and queries pull from GSC. LLM traffic pulls from GA4 with regex filtering. The last tab compares GA4 and GSC directly. That's the core data flow. On your second question—clicks in GSC are actual clicks users performed, but not all clicks result in a session. Some are bot clicks, some have timeout issues or connection problems, so there's always a gap.

**Jo Kaminska:** In GA4, a session is a 30-minute window of activity—a cookie is dropped and the session ends after 30 minutes of inactivity. Engaged sessions are different. GA4 defines an engaged session as one lasting at least 10 seconds with two or more events (scroll, click, page navigation, or conversion). A user landing on a blog post, then another blog post, then a final page would be an engaged session. We use this to understand how engaged your audience is and whether the topics resonate. A normal discrepancy between clicks and sessions is up to 20%. So clicks should roughly equal sessions, but never perfectly. When I pulled your data comparing GSC clicks to organic sessions, I noticed a concerning trend. In the early months, GSC clicks exceeded sessions by normal amounts. But starting in November and December, the variance got much worse. In November, you had 21k GSC clicks but only about 11k GA4 sessions—that's a significant reversal and a red flag. Normally, clicks are higher than sessions because not all clicks convert to sessions. This suggests a tracking change happened on your site.

**Andrew Arasaki:** Are these organic sessions or UTM-based clicks?

**Jo Kaminska:** These are organic sessions. Let me walk you through the session medium breakdown, because that's where the real problems are. Normally, you'd see standard mediums: direct, CPC, and organic. But your data shows blog (11k sessions), article (55k sessions), email, referral (LLM, LinkedIn, social), and various parameter combinations. The issue is that "blog" and "article" are not standard GA4 mediums—they shouldn't be there. And "organic" is just a small portion of overall sessions, when it should be the dominant channel. It looks like custom UTM parameters are being automatically applied and carried forward as users navigate. The tracking isn't transparent—I can't see which URLs map to which mediums or whether these sessions belong to content you created. How are these parameters working on your site? Are they being automatically injected across pages?

**Andrew Arasaki:** Yes, it definitely looks that way. Let me break this into two issues. First, the GA4 vs. GSC discrepancy. Second, the parameters. Our UTM parameters are set through Google Tag Manager via a script. We also cookie users who come in, storing any UTM parameters as cookies. When they return, the script looks up that cookie, pulls the data, and sends it to GA4. I've updated that script, but your team is welcome to review it. I can grant Tag Manager access.

**Jo Kaminska:** Yes, our team can definitely review that. Can you share the Tag Manager access with us?

**Andrew Arasaki:** Sure. Is there an email I can send the access to?

**Jo Kaminska:** Let me check with Kyle, our VP of Customer Growth. We have technical folks who can review the script. We can reconnect over Slack to set that up.

**Andrew Arasaki:** Sounds good.

**Jo Kaminska:** I have a list of all these parameters. One thing I'm wondering—can you pull specific URLs that map to these mediums? I know some CMSs don't allow that, but I'm curious about your setup.

**Andrew Arasaki:** Not really in Craft. GA4 is our most concrete data source. The script is set up to fire through Tag Manager, so it doesn't send data back to Craft.

**Jo Kaminska:** That makes sense. How do you internally report on organic traffic or media in general? Are you mostly using GSC or GA4?

**Andrew Arasaki:** We mostly use GA4. We don't use GSC much. Also, I recently updated the channel definitions in GA4 to match Google's recommended definitions for organic, paid, and social. That change might also be affecting the numbers we're seeing.

**Andrew Arasaki:** I'm a bit confused because I've never seen this before. I've always let Google Analytics handle the tracking automatically. What are your thoughts? Do you have other customers using SPAs?

**Jo Kaminska:** SPAs? Single Page Applications—is that what you mean?

**Andrew Arasaki:** Yes, a headless site built with React, like our site. That's the only issue I can think of that might explain this. We have a custom routing system, so tracking across pages might be getting disrupted.

**Jo Kaminska:** That's helpful to know. I worked with an analytics company in the past and SPAs definitely needed custom setups. Tracking across pages was always tricky with those architectures. Normally, when I look at customer data, session mediums are standard—organic, referral, maybe a campaign or two. Not all these custom values. This is valuable insight for our team. Would you mind sharing your documentation on the GA4 channel definitions? That could really help us diagnose the issue.

**Andrew Arasaki:** Absolutely. I'll find that Google Doc and send it over.

**Jo Kaminska:** Perfect. Thanks, Andrew. With this information and your documentation, I can go back to the team and work through the setup. We'll get back to you by end of week with our findings and next steps.

**Andrew Arasaki:** Great. Thanks for taking the time on this deep dive. Sorry we took up so much time today—I'm happy to jump on a separate call if that would help.

**Jo Kaminska:** Absolutely. We'll reconnect by end of week with recommendations on how to address the tracking issues.

**Hadassah Pegado:** Thanks, Andrew. I appreciate you jumping in on the technical details, even though I was a bit lost in there.

**Andrew Arasaki:** No worries. It's good information to have.

**Jo Kaminska:** Great. Thank you, Andrew, and thank you, Hadassah and Maria, for your time today.

**Hadassah Pegado:** Thank you, Jo. Have a good rest of your day. Bye!

**Jo Kaminska:** Bye everyone!
