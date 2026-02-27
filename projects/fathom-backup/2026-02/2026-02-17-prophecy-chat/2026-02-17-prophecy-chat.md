# Prophecy Client Account Handover

<metadata>
date: 2026-02-17
time: 16:01 UTC
duration: 29 minutes 19 seconds
organizer: Andrew Bishara (andrew@growthx.ai, GrowthX)
participants:
  - Andrew Bishara (andrew@growthx.ai, GrowthX)
  - Sucheta Biswas (GrowthX)
fathom_recording_id: 122992097
fathom_url: https://fathom.video/calls/571128831
share_url: https://fathom.video/share/4cs2cyHQ59x1FQo8XrQ7AqPmjLndsQ9-
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Andrew walked Sucheta through the complete Prophecy account handover: client context, the Article Agents Test Pipeline (new content generation), multi-step post-processing (Atlas > Claude > Atlas), Webflow staging, and analytics tracking. Critical bottleneck: 18 articles await Cody's review; do not move any to production without his approval.

---

## Context

Prophecy is an AI data prep and analysis platform. They're a strategic GrowthX client with unpredictable content strategy—they change direction every few weeks, creating feast-or-famine workloads. Cody is the main decision-maker and approval gatekeeper. The team is transitioning from legacy workflows to a new "Article Agents Test Pipeline" while maintaining 5 published articles per week. All articles go through client feedback loops and require multi-tool post-processing to enforce branding, fix formatting, and update broken links (old prophecy.io domain must become prophecy.ai). Final publishing happens on Webflow's "Guides" section, with Cody handling the final publish step.

---

## Relevance

- **Operations & Delivery:** Content generation pipeline shift, process automation, client-specific workflow constraints, bottleneck management.
- **Client Management:** Strategy volatility, review/approval delays, protecting team from client-side blockers.
- **Product & Quality:** Multi-step post-processing requirements, brand alignment, link validation, analytics tracking via Google Analytics 4 and Search Console.
- **Team Onboarding:** Full account transition from Andrew to Sucheta with documented processes, autonomy parameters, and escalation paths.

---

## Overview

- **Client Bottleneck:** Prophecy's inconsistent strategy has created a backlog of ~18 unreviewed articles, stalling the 5-article/week quota. Do not publish anything without Cody's explicit approval.
- **New Pipeline:** Use the "Article Agents Test Pipeline" for all new content. It's a test run, so you have full autonomy to edit its YAML code or request engineering changes to improve output.
- **Post-Processing:** All articles require a multi-step review (Atlas → Claude → Atlas) to enforce branding, fix formatting, and correct broken `prophecy.io` links.
- **Webflow Staging:** Stage articles as drafts in Webflow's "Guides" section for Cody's review. Do not publish; Cody handles the final step.

---

## Key Topics

### Client Context & Bottleneck

- **Client:** Prophecy, an AI data prep/analysis company.
- **Challenge:** Strategy changes every few weeks, creating an unpredictable workload (e.g., a sudden focus on "Alteryx alternatives").
- **Bottleneck:** ~18 articles are awaiting review from Cody (main contact), representing ~3.5 weeks of work.
  - **Action:** Do not move any article from "Considering" to "In Production" without Cody's approval.
  - **Rationale:** This protects our team from client-side delays. If asked about the quota, cite the backlog as proof we've delivered.

### Content Workflow: Generation & Post-Processing

- **Generation:**
  - Use the "Article Agents Test Pipeline" for all new content.
  - **Autonomy:** Edit the pipeline's YAML code or request engineering changes to improve output.
  - **Fallback:** The old pipeline is available but requires heavy editing for its 5,000-word output.
- **Post-Processing (Multi-Tool Review):**
  - **1. Atlas:** Use Andrew's "post-processing process" prompts to enforce branding, revise sections, and format elements like intros, conclusions, and FAQs.
  - **2. Claude:** For client feedback, use the "Prophecy editorial section" tool to analyze comments. Then, manually verify all changes in the "Prophecy Claude" channel.
  - **3. Atlas (Final Check):** Run the revised article through Atlas again.
    - **Compare to Artifacts:** Check against the "Test Run" audience personas and the writing guide.
    - **Regenerate Summaries:** Re-create the intro, conclusion, and TL;DR, as the content will have changed significantly.
- **Critical Fix:** All links must be updated from the old `prophecy.io` domain to the current `prophecy.ai` domain to prevent broken links.

### Publishing & Performance Tracking

- **Webflow Staging:**
  - **Location:** Stage articles in Webflow's "Guides" section (not "Blog Posts").
  - **Process:** Create a draft, assign to "Prophecy Team," and set its status to "Client Review."
  - **Handoff:** Tag Cody and comment, "Created a draft on Webflow. Please finalize. Do not publish."
  - **Note:** Cody will review and publish the article himself.
- **Performance Tracking (Lucas Studio):**
  - **Task:** Weekly, add new article URLs to the "URL Cohorts" sections in Google Analytics 4 and Search Console.
  - **Tool:** Use Claude to format the URLs correctly for each data source.

---

## Action Items

**Andrew Bishara (GrowthX)**
- Post Prophecy channel comment tagging Carrie + Sucheta re: 18 articles in "Considering"; hold until Cody OK
- Send Prophecy + Sunbit Fathom recordings to Sucheta

**Sucheta Biswas (GrowthX)**
- Generate 1 test article in Article Agents Test Pipeline; do not send to Cody; test for confidence before starting production
- Send 25 Sunbit articles to upline backend by Feb 19

---

## Transcript

**Sucheta Biswas:** Hello? Can you hear me?

**Andrew Bishara:** I can hear you. I'll be quick today. Won't take up too much of your time.

**Sucheta Biswas:** Great, thank you. Do you have any questions for me?

**Andrew Bishara:** So today I'm going to walk you through Prophecy. I've prepped everything for you. Let me know if you have any questions as we go.

**Andrew Bishara:** This client is an AI data prep and analysis company. The big thing with them is that they change their strategy every couple of weeks. Sometimes there's tons of new articles to write, sometimes there's nothing. Cody is the main point of contact—he's your approval gatekeeper for all content decisions.

**Andrew Bishara:** We're trying new things with pipelines and processes. I've updated the operating manual with all the details. If you find things that can be improved, just list them and we'll get engineering involved.

**Andrew Bishara:** This is the new Article Agents Test Pipeline. You can use it freely—just use it. Because it's new and we're trialing it, it might not be perfect yet. Feel free to change the YAML code or ask engineering to edit things. You have full permission—don't worry about asking me or Carrie. This is a test run, and we want to make it work long-term. If the new pipeline isn't working, you can fall back to the old one, but you'll get 5,000 words and have to do quite a bit of editing.

**Andrew Bishara:** I've created a post-processing process. It's enforcing branding and language rules, revising sections, handling the intro, conclusion, too long didn't read, and FAQ formatting. Now, here's a critical thing: when you get an article, check all the links. They'll have old prophecy.io links from their old website, which they destroyed without migrating properly. Those links are broken. Change them all to prophecy.ai. This applies to CTAs and internal/external links.

**Andrew Bishara:** The post-processing flow is: Atlas first, then Claude, then Atlas again. Atlas enforces branding and revises sections. Once you have client feedback, download the Google Doc with their comments, copy the content into markdown, and use the Prophecy editorial section tool to analyze and implement the changes. Then paste the revised article into the Prophecy Claude channel and verify manually that all changes were made correctly. After Claude, run it through Atlas one more time—compare it to the Test Run audience personas and the writing guide. Check if it aligns. Atlas might suggest adding sentences to hit the audience better. Do that. Check the narrative flow, logic, and readability. Since you'll have made changes, regenerate the intro, conclusion, and TL;DR.

**Andrew Bishara:** For publishing, you stage articles as drafts in Webflow's "Guides" section, not "Blog Posts"—they've been doing guides since November. Log into the team account (not personal), go to Prophecy AI > CMS > Guides. Add a new guide: name, slug, copy and paste the body. Grab the images from the Atlas pipeline and upload as main feature and thumbnail. Set the guide category to "AI Native Analytics," assign to "Prophecy Team," and set status to "Client Review." Create a draft—don't publish. Then change the status to "Ready to Publish" and tag Cody with the comment: "Created a draft on Webflow. Please finalize. Do not publish." Cody will review and publish it himself.

**Andrew Bishara:** Weekly, check the Prophecy Guides page to see what was published. Then add the URLs to Lucas Studio in Google Analytics 4 and Search Console. Grab the published article URLs, ask Claude to format them correctly for each system, and paste them into the URL Cohorts section in both platforms. It's simple once you see the format.

**Andrew Bishara:** Now, here's the bottleneck: there are currently 18 articles awaiting review from Cody. They're in "Considering" status. They've been there because Cody changed strategy. Some go back to November or December. Do not move any articles from "Considering" to "In Production" until Cody explicitly approves them. This protects us from client delays. If anyone asks where the 5 articles per week are, you say: "We actually have 18 articles ready for review that need Cody's finalization. Once he approves them, we can publish them—that's 3.5 weeks of work."

**Andrew Bishara:** Currently, there are two new articles: "Top Alteryx Alternatives" posts. I sent those to Cody this morning for review. He might come back with feedback, send them straight to ready-to-publish, or publish them himself. Everything's up in the air. The most likely next step is you'll implement edits on those two or stage them on Webflow.

**Sucheta Biswas:** So with the bottleneck, what if you want to generate a test article on Prophecy to see how the pipeline works? I'm a bit worried about whether I'm going in the right direction.

**Andrew Bishara:** Yeah, you can give it a test run. Grab any topic from the "Considering" articles and just try it out. Don't send it to Cody or anything—he wants to do his own approval. Just do it as a test to build confidence.

**Sucheta Biswas:** What about timing on Sunbit articles?

**Andrew Bishara:** For Sunbit, the 25 articles this week are already prepped—they just need editing. Grab them from the upline backend. Put all 25 in by Thursday or Friday, then they'll be ready for you to work on Monday. That way you're not scrambling.

**Andrew Bishara:** Each article takes about an hour to an hour and five minutes, depending on the topic. Once you get whatever article Cody wants, just throw it into the pipeline and go from there. We've narrowed down the fields so it shouldn't take long.

**Sucheta Biswas:** I'm pretty busy with other accounts, so I'll catch up tomorrow. You said you're there tomorrow?

**Andrew Bishara:** Yeah, half day tomorrow. I'm flying out in the afternoon. It's 10 PM for you right now?

**Sucheta Biswas:** Yes, 10 PM. And I have to leave for the airport pretty soon.

**Andrew Bishara:** So I'll be available until about 1:30 AM your time, which is about 12:30-1:00 my time. That's roughly three hours from now. Let's say 1:30 your time, and I'll be here if you have questions.

**Sucheta Biswas:** Perfect. Thanks, Andrew. I appreciate the walkthrough.

**Andrew Bishara:** If you have any other questions, reach out. I'm happy to help. If there's anything coming up, let me know.

**Sucheta Biswas:** Thanks, Andrew. Have a good day. Bye.
