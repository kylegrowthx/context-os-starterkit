# Galileo <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-11
time: 18:30 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants:
  - name: Carrie Chowske
    email: carrie@growthx.ai
    affiliation: GrowthX
    role: Content & AEO Manager
  - name: Jackson Wells
    email: jackson.wells@galileo.ai
    affiliation: Galileo
    role: Content Lead
fathom_recording_id: 121677270
fathom_url: https://fathom.video/calls/562611198
share_url: https://fathom.video/share/1vKM2bxg6cB5rPSX7eaKTYYq5nzdeE3M
source: fathom
enriched_on: 2026-02-27T18:45:00Z
</metadata>

---

## Summary

Galileo's new publishing workflow unblocks 15 pending blogs and restores weekly cadence, while a new Check That categorization feature enables granular AEO/GEO reporting without affecting public data. GrowthX will provide AI training artifacts to fix content hallucinations and over-linking issues, while a data integrity audit resolves discrepancies between SEMrush and Looker dashboards.

---

## Context

Galileo is implementing an AEO strategy to increase visibility in AI-powered search results. This weekly sync coordinates between Jackson (Galileo's content lead) and Carrie (GrowthX's AEO manager) on content quality, publication velocity, and performance measurement. The partnership addresses Galileo's immediate need to clear a publishing backlog, improve AI-generated content accuracy, and establish reliable metrics for AEO success—specifically responding to Jason's (Galileo exec) requests for transparent AEO/GEO performance reporting.

Check That (GrowthX's proprietary AEO platform) recently rolled out a dual-categorization feature that separates internal reporting categories from public-facing data, giving teams like Galileo the ability to segment performance by niche topic for internal analysis without altering transparency. This is a critical capability for Jason's demand for more granular AEO metrics and helps address the challenge that AEO success is a long-term strategy requiring consistent execution, not a quick tactical win.

---

## Relevance

- **AEO Strategy**: Clarifies how Check That enables internal reporting segmentation, creating pathway for Jason's requested metrics without compromising data integrity. Third-party syndication (Reddit, YouTube, dev.to) emphasized as preferred over branded listicles.
- **Product Development**: Check That's dual-categorization feature (internal vs. public) unblocks reporting use cases—directly applicable to any client needing niche segmentation without altering public facing data.
- **Content Operations**: Publishing blocker resolution addresses the fundamental bottleneck in velocity. Corpus/artifact sharing pattern establishes reusable workflow for fixing AI-generated content at scale.
- **Data Integrity**: SEMrush/Looker discrepancy audit surfaces potential dashboard formula issues—relevant to any client relying on blended GA4/Search Console data for reporting.
- **LLM & AI Visibility**: Ongoing discussion of Google's AI Overview integration and how it impacts search behavior. Emphasis on why AEO is execution-heavy (not tooling-heavy) resonates with broader trends in AI-powered search.

---

## Overview

- **Publishing Blocker Cleared:** The new publishing workflow is ready for testing this Friday, unblocking \~15 pending blogs and restoring the weekly cadence.
- **AEO Reporting Unlocked:** Check That's new dual-categorization feature enables internal reporting on niche topics without altering the public profile, directly addressing Jason's request for AEO/GEO metrics.
- **Data Integrity Audit:** A technical SEO audit is underway to resolve a data discrepancy between SEMrush and Looker (GA4/Search Console), ensuring accurate performance reporting.
- **Content Quality Fixes:** GrowthX will provide its AI corpus to help Galileo fix content hallucinations (e.g., misstating product strengths as weaknesses) and spammy internal linking.

---

## Key Topics

### Content Quality & Pipeline

  - **Problem:** AI-generated content has quality issues requiring manual fixes.
      - **Hallucinations:** Content misstates product strengths as weaknesses.
      - **Spammy Linking:** Over-linking to the "State of Eval Engineering" report (4-5+ times/post).
  - **Solution:** GrowthX will provide its AI corpus (artifacts) for Galileo to review and update, ensuring the AI uses the latest product info.
  - **Blocker:** The publishing queue has \~15 pending blogs (12 needing minor edits, 3 queued).
  - **Resolution:** The new publishing workflow is ready for testing this Friday. Carrie may test it sooner to expedite publishing.

### Performance Reporting & Strategy

  - **Problem:** A data discrepancy between SEMrush and Looker (GA4/Search Console) is delaying performance reporting.
      - **Discrepancy:** SEMrush shows a traffic spike, while Looker shows dips.
      - **Cause:** Suspected issue with Looker's data blending formulas.
  - **Resolution:** A technical SEO audit is underway to validate Looker's data integrity.
  - **New AEO Reporting Strategy:**
      - **Context:** Jason is requesting more granular AEO/GEO performance metrics.
      - **Solution:** A three-part metric system will be implemented.
        1.  **Weighted Metric:** Broad performance data.
        2.  **LLM Referral Traffic:** Secondary metric.
        3.  **Core Prompt Weighted Metric:** Performance on a curated list of high-value prompts.
      - **Execution:** Jackson and Carrie will co-create the "core prompt" list and tag them in Check That for tracking.

### AEO Strategy & Syndication

  - **Context:** AEO is a long-term strategy, not a quick fix, requiring consistent execution.
  - **Tactic:** Increase third-party content syndication (Reddit, YouTube, dev.to) to build referential citations.
  - **Caution:** Do not duplicate content verbatim.
      - **Rationale:** This avoids SEO penalties and is less effective, as AI often cites unique third-party content over branded listicles.

---

## Action Items

**Carrie Chowske (GrowthX)**
- Email Jackson: agenda + performance notes
- Email Jackson: corpus/artifact list (incl product/features)
- Coordinate w/ Usman: test publishing workflow early this week (Friday target, potential earlier testing)
- Add Galileo category in Check That (unblocked by dual-categorization feature launch)
- Email Jackson: Check That access instructions/invite
- Email Jackson: AEO/GEO update + feedback on 2025 SEO article

**Jackson Wells (Galileo)**
- Email Carrie: proposed core prompts for weighted metric (to be co-created with Carrie)

---

## Transcript

**Jackson Wells:** Hey, Carrie, how's it going?

**Carrie Chowske:** It's going well. I'm so sorry I was running late—I didn't get a chance to finish the performance part of the agenda, but I have the rest of my day open and will get that to you after the meeting.

**Jackson Wells:** That's all good. I have an 11 o'clock after this, but we can go over whatever's prepared. I was just in the middle of editing one of the blogs. Would you mind sending over a succinct collection of what you all are using as a corpus—like your artifacts? I'd like to review and potentially trim older stuff or replace assets with newer versions. There are still some gaps, and some refreshes likely have outdated terminology that I want to verify.

**Carrie Chowske:** Yep, absolutely. I can send that over.

**Jackson Wells:** Thanks. Also, we're definitely getting closer on quality, but internal linking is still an issue. There are instances where we're linking the "State of Eval Engineering" report four or five plus times in a single post, which feels spammy. And there are a couple of hallucinations—one particularly bad example says our platform's weaknesses are actually strengths. I'm not sure where that came from.

**Carrie Chowske:** We definitely want to check the product and features artifact to make sure everything's correct. Sometimes when we run a workflow, it'll claim to check something but gets a little lazy toward the end. You have to do a final validation pass against everything.

**Jackson Wells:** That makes sense. I've actually adopted a new workflow—running Claude in the browser to validate everything against the most recent docs and product pages, then generating lists of what needs fixing.

**Carrie Chowske:** That's exactly my trick for when our pipelines aren't working as expected. I run it through Claude and ask what's getting missed consistently, then go back and fix the pipeline. It helps identify when context is too large and things are breaking down.

**Jackson Wells:** Did you hear back on the publishing pipeline?

**Carrie Chowske:** I haven't heard back yet, but last I checked it was in the works. Let me pull up the ticket and see if it's been moved. [checking] It's ready to test the publishing workflow—the update just came through today. Usman's out this week, but he said he'll test it Friday. I might try to run it earlier if I can grab him. The publishing workflow is one of the easiest to set up anyway.

**Jackson Wells:** Great. It looks like we have 12 blogs in the needs-edits category with pretty minor changes, and three queued for publishing—roughly 15 in the queue. It'd be good to get that cleared.

**Carrie Chowske:** On the internal linking front, Usman is working on adding that artifact too—he was prioritizing the publishing workflow first. But he wanted me to mention something: he has a gut feeling the data in Looker isn't displaying correctly. We've put in a ticket with our director-level team to run a quick technical SEO audit to verify that Looker matches what we're pulling from GA4 and Search Console. We're seeing more positive data in SEMrush than in Looker, which is odd, and Looker isn't showing some of the dips we're seeing elsewhere. Since Looker blends GA4 and Search Console data, we need to audit the formulas.

**Jackson Wells:** What's your gut reaction on the discrepancy?

**Carrie Chowske:** We're seeing more positive results from SEMrush, but it's not just showing overall positive data—it's missing dips that appear elsewhere. So we're seeing completely different numbers in Looker versus SEMrush. Vivek reported some valleys that don't show up anywhere else. I want to make sure I'm not giving you someone else's data, so we're double-checking the settings.

**Jackson Wells:** That shouldn't take very long to audit. [pausing] Sorry, I need to give someone a verification code. Let me just... okay, I'm back.

**Carrie Chowske:** I'm also refining the prompts in Check That. I was going to pull that up to show you an update on the categorization feature.

**Jackson Wells:** Do we have an update on the potential recategorization?

**Carrie Chowske:** Yes, actually—I just got this today. They switched how categorization works. Before, if we changed your category in the workspace, it would also change the public-facing data. But Check That's model is similar to G2 reviews or Crunchbase financials—the public-facing data should be trusted research that brands can't edit. The backend is separate so you can categorize your own data for reporting the way you want without affecting public visibility. It keeps things more manageable and lets us go deeper into niches for reporting versus using broader categories publicly.

**Jackson Wells:** Got it. That makes sense.

**Carrie Chowske:** So now I can add the Galileo category without pushback.

**Jackson Wells:** That is great. That will definitely help with internal visibility and segmentation. I'm definitely getting pressure from Jason on AEO and GEO reporting though. I like the three-tier metric idea: a broader weighted metric covering all performance data, LLM referral traffic as a secondary metric, and then the weighted metric applied to a specific collection of core prompts spanning subcategories like observability and eval. I think those three would help him understand it better.

**Carrie Chowske:** Do you want to identify those core prompts, or should I make suggestions?

**Jackson Wells:** Maybe we both come up with a list and meet in the middle.

**Carrie Chowske:** Perfect. We can then tag them in Check That. Right now we can filter by library vs. custom prompts and branded vs. non-branded. We can add a "core prompts" tag and filter. He was envisioning a monthly report on that?

**Jackson Wells:** Yeah, and he's been very hands-on with organic search and AEO recently.

**Carrie Chowske:** I can get you access to Check That. I'll need to check if you need to create an account first or if I can set it up and send it to you. Either way, you can see the exact prompts and the data alongside them.

**Jackson Wells:** That would be great. LLM referral traffic has been dropping month-over-month for a couple of months now, and that's definitely going to raise concerns. I haven't reported on it visibly for obvious reasons, but I'm thinking about other strategies we can employ to improve it. What's our regular publishing cadence? Are we still behind on publishing?

**Carrie Chowske:** Are we doing weekly blogging?

**Jackson Wells:** Yeah, we were doing weekly—I think we published at the start of last week. It was typically Fridays for a while, then switched to Mondays, but it was a weekly cadence. That's why I called out the 15 articles almost ready to publish.

**Carrie Chowske:** Okay, so getting the publishing queue cleared is critical.

**Jackson Wells:** Yeah, the good news is that should help with overall velocity. The FAQ/question-and-answer format feels like the assumed AEO silver bullet right now for blog content.

**Carrie Chowske:** There's some pushback starting on that. I think it'll follow a similar pattern to keyword stuffing from the old days. I don't want to put too many eggs in that strategic basket, but for now it's working. Even if they shift away from it, you still need that content because it signals to the algorithm that if your name and someone else's name are both on a list, you must be similar.

**Jackson Wells:** Yeah, I get what you mean. At the end of the day, AEO is a new and emerging field. A lot of people claim to know what's going on, but I don't think anyone really does. But marketing executives want to pretend it's concrete, so I'm trying to play middleman.

**Carrie Chowske:** The concrete reality is: if you don't do anything, you won't show up in these queries. Doing something produces way more results than not trying or being unable to publish. The challenge is that in the tech space, the people using AI are your competitors, so there's intense competition to appear in AEO searches. It's just like traditional SEO. That's the core problem Marcel is trying to solve with Check That—we were tired of not understanding how SEMrush, Profound, and Peak were determining their rankings. Now we know how it works and can confidently say this is accurate. We know people are actually searching these things and we can show exactly which page on your site was cited—that level of transparency isn't consistent across other platforms.

**Jackson Wells:** For sure. On our end, I'm pushing for more third-party content syndication—Reddit posts, optimized YouTube descriptions, and potentially repurposing content on dev.to to get third-party citations linking back to Galileo.

**Carrie Chowske:** Just make sure you're not doing one-to-one duplication, even with canonicals. We've had issues with that in the past. We thought it wouldn't work, and it didn't—we had to backpedal and it took a while to get things indexed again. Also, when AI cites listicle-type content from third parties like Reddit or dev.to, they're more likely to cite those than branded listicles.

**Jackson Wells:** I wish people would give this enough time to research and understand it. There are a lot of assumptions about how it works and how easy it is to optimize. It's not easy at all. I'm trying to rewrite marketing priorities to position ourselves as AEO experts. People think we need more tooling, but it's not a tooling problem—it's a strategy and resourcing thing. We have the tools we need. You're not going to see immediate one-to-one gains.

**Carrie Chowske:** Exactly. The more people claim to know, the less they actually do. I go with "here's what I know." Today I was thinking about Google's influence on the AI game. That's why we're starting to see upticks. It's basically CRO—especially on mobile, when you search traditionally on Google, it shows an AI Overview and immediately prompts you to use their full AI search. People are responding because it's asking them. And honestly, it's really nice. I used it the other day and got answers with citations. It has the accessibility of ChatGPT—everyone knows the name—but with the citation and accuracy of Perplexity. People trust Google, right or wrong, but they don't trust ChatGPT. So consumers are shifting toward Google's offering.

**Jackson Wells:** For sure. It's hard with our persona being so AI-focused to know what typical user behavior looks like. I also sent you an article I found on 2025's SEO and GEO updates—I'd like your take on it.

**Carrie Chowske:** I have to run to my next meeting, but I'll add the performance data as soon as I have more details. I can get you the AEO/GEO stuff and send it today. Sorry about that—it's been a weird morning.

**Jackson Wells:** It's all good. I appreciate it as always. Ping me if anything else comes up.

**Carrie Chowske:** Will do. Thanks, Jackson.

**Jackson Wells:** Thanks, Carrie. Have a good one.

**Carrie Chowske:** You too. Bye.
