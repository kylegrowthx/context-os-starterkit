# SentinelOne Weekly Sync

<metadata>
date: 2025-09-03
time: 13:31 UTC
duration: 20 minutes
organizer: Aida Knežević
participants: Aida Knežević, Ankit Pahuja, Mansi Bhalothia, Marisol Smith, Sydney Go
fathom_recording_id: 84618951
fathom_url: https://fathom.video/calls/397678240
share_url: https://fathom.video/share/yGFr5fDcMjJQjdxnx532SjZDtvzXerHB
source: fathom
enriched_on: 2025-03-02 02:15 UTC
</metadata>

---

## Summary

GrowthX shared 5 sample CVE pages with AI-generated content and pseudocode (pending SentinelOne's security team review) and confirmed a dev meeting with Nicholas and Jory to map the ContentStack CMS integration with GrowthX's publishing workflow. Two new blog posts are in progress and Sydney has revised the first CS 101 blog (3000+ words) for publishing, while SentinelOne is conducting additional keyword research to refine topic assignments. The priority now is nailing down a go-live timeline for the CVE/vulnerability database after the dev meeting.

---

## Context

SentinelOne, a cybersecurity company, engaged GrowthX to develop a content strategy for their CVE (Common Vulnerabilities and Exposures) and vulnerability database, which will be a major asset in their product offering. GrowthX is using an AI-powered content workflow to generate sample CVE pages and supporting blog content, while working with SentinelOne's product and web teams to integrate the content into their ContentStack headless CMS. This is an active delivery engagement with tight timelines — Ankit is pushing the team to establish a clear go-live date for the CVE database.

---

## Relevance

**To GrowthX Delivery:**
- AI-generated code validation: GrowthX's past experience with code snippets in CVE content across clients (including previous CVE project with developer review) shows the approach is working; SentinelOne's security team will review for final sign-off.
- Headless CMS integration: ContentStack is confirmed (not Sanity); expected to be smoother than Prismic for programmatic publishing.
- URL-based keyword volume in SEMrush assignments may confuse stakeholders; consider switching to single-keyword volumes for clarity (action: relay to Sydney).
- CMS access bottleneck: Nicholas needs ContentStack credentials to map workflow correctly; dev meeting scheduled to align integration bandwidth.

**To CheckThat:**
- Content strategy pivot in progress: shift from broad top-of-funnel to deep-dive verticals (cybersecurity 101); listicles paused pending legal/brand review.
- Keyword targeting: pillar-and-cluster strategy in use; SentinelOne wants to avoid comparative language when mentioning competitors (legal risk mitigation).

**To GrowthX Business Development:**
- Account health signal: Project is on track with executive visibility (Ankit driving urgency on timelines) and expanding deliverables (CVE pages, blogs, keyword research refinement).
- Timeline pressure: CVE/vulnerability database go-live is high priority; GrowthX will establish timelines post-dev meeting for renewal/expansion discussion.

---

## Overview

- 5 sample CVE pages created; AI-generated content (incl. pseudocode) awaiting security team review
- ContentStack CMS integration meeting scheduled; Nicholas needs access for workflow mapping
- 2 new AI-generated blogs in progress; 1st blog revised (3000+ words) ready for review
- Timeline for CVE/vulnerability database go-live needed; high priority for SentinelOne

---

## Key Topics

### CVE Page Samples and Content Workflow

  - 5 random CVE pages created using AI-powered content workflow
  - Structure consistent across all CVE pages
  - AI-generated pseudocode included with disclaimer
  - Previous code reviews for other clients found AI-generated code accurate
  - Ankit to share pages internally, including with security team for review

### CMS Integration and Dev Team Meeting

  - SentinelOne uses ContentStack (headless CMS), not Sanity as previously thought
  - Meeting scheduled with Nicholas, Jory, and web teams to discuss CMS access and integration
  - Nicholas needs CMS access to map workflow correctly
  - Integration help and bandwidth allocation to be discussed

### AI Content Updates

  - 2 new blogs in progress, to be delivered by end of week
  - 1st blog revised (3000+ words) ready for review and publishing
  - Mansi to handle next steps for content review

### Keyword Volume Data in Airtable

  - Data sourced from SEMrush
  - Search volumes may reflect multiple keywords for URL-based assignments
  - Consideration to simplify by using single keyword search volume in future
  - SentinelOne follows pillar and cluster strategy for content structuring

### Content Strategy Adjustments

  - Listicle articles paused due to internal discussions about competitor visibility
  - Some topics adjusted based on SEO analysis and keyword targeting
  - Legal considerations for mentioning competitors in content

### Additional Keyword Research

  - Sydney and Marisol conducting further keyword research based on feedback
  - New assignments to be uploaded to Airtable for review and approval

---

## Action Items

**Ankit Pahuja (SentinelOne)**
- Review 5 CVE pages in Figma doc; share with Mahati and security team for feedback

**Aida Knežević (GrowthX)**
- Inform Nicholas re ContentStack CMS use (not Sanity)
- Relay keyword volume feedback to Sydney (consider switching to single-keyword volumes for simplicity)
- Discuss CVE database timeline with team post-dev meeting; prepare timeline for Ankit

**Mansi Bhalothia (SentinelOne)**
- Review updated 3000+ word CS 101 blog post; decide on publishing

**Sydney Go (GrowthX)**
- Continue keyword research based on feedback; upload new assignments to Airtable for review

**Marisol Smith (GrowthX)**
- Finalize 2 new blogs for delivery by end of week; prepare content samples for review

---

## Transcript

**Aida Knežević:** Hi!

**Ankit Pahuja:** Hey, how are you?

**Aida Knežević:** Are we waiting on anybody else or is it just going to be you and Mansi today?

**Ankit Pahuja:** We can get started.

**Aida Knežević:** So I shared the agenda with you previously. The most important updates that we have are the five CVEs in the Figma doc. So we just picked like five random ones, uploaded the content. Pretty brief, you know, so feel free to take a look and see the structure, but also the depth of content and the detail. And then, when you provide feedback, Marisol, who did these pages, is going to see it and she can implement it.

**Ankit Pahuja:** So just to confirm that this content came out from the tool that you have, like the content workflow that you're creating?

**Aida Knežević:** Yes, yeah. The workflow that they created specifically for CVE pages — it's all going to have the same structure. Very similar across the board.

**Ankit Pahuja:** And it would be right to assume an output like this for the rest of the pages that we build out of the workflow?

**Aida Knežević:** Yes, yes.

**Ankit Pahuja:** And for the part that has code in it — there's attack vectors and certain sections that have configuration lines or code in it. So that's also AI generated. Do we validate it or is it fine to keep as-is?

**Aida Knežević:** This is AI generated and it includes a disclaimer that says it's pseudocode representation of how unauthorized access might be simulated. This is going to be reviewed by someone from your security team, right?

**Ankit Pahuja:** Yeah.

**Aida Knežević:** From our experience, the AI generated code is accurate. We haven't had issues with code snippets being incorrect. At one point, we were creating CVE pages for a different client, and a developer reviewed all of the code and said it was correct. Feel free to take a look and let me know what you think.

**Ankit Pahuja:** All right, I'm trying to be proactive here so things are taken care of. I'll look at these pages and pass them internally to Mahati. She'd also be sharing these pages with someone from the security team who wants to see the structure, content, and how the pages would be set up.

**Aida Knežević:** I'm going to drop it in chat and send them also in Slack so that Mahati can see it. You all should have access, and I think you might also have editing permissions to add other people.

**Ankit Pahuja:** I've been adding some folks from my team to have comments. There will be comments from other team members like Christian and Patrick on the design elements, and we want to make sure those are addressed for the development phase.

**Aida Knežević:** Perfect. I'll be taking notes on the design feedback for the next steps.

**Aida Knežević:** Okay, we have a meeting later today with Nicholas and Jory. I'm going to be there as well. I have a conflicting meeting towards the end, so I'm going to jump a little earlier, but I'll be there to give context to Nicholas and Jory about the CMS integration. Nicholas needs access to the CMS so he knows how to map everything correctly from our workflow to your CMS. I know you have strong access controls, so it's just about ironing that out.

**Ankit Pahuja:** I wasn't aware that you hadn't met Yuri and his team earlier. Glad you raised it last week. I checked in with Yuri and learned that our web teams haven't met yet. That was the gap. I thought it's best to have those guys meet who essentially are going to build this. It's also important for our web team to know what integration help we need to offer and what bandwidth we need to free up. It's going to be late for me, but if I'm up, I'll try to join the call because this project's important. I'll mostly be consuming and making sure things are aligned.

**Aida Knežević:** No worries. Even if you don't make it, that's totally fine. I have enough context from you and our meeting so far to help everyone get on the same page.

**Ankit Pahuja:** So the workflow is ready on the publishing side for integrating with ContentStack as our CMS. Have thoughts been given by your web team already, or will we explore once you get access?

**Aida Knežević:** I thought you were using Sanity, but you're on ContentStack. As soon as we get access to the CMS, they can immediately start understanding how the CMS works — the structure, templates, and so on. It can move pretty quickly from here.

**Ankit Pahuja:** Let Nicholas know about ContentStack and that it's our CMS.

**Aida Knežević:** ContentStack is a headless CMS, right?

**Ankit Pahuja:** Yeah, it's a headless CMS.

**Aida Knežević:** I don't anticipate big issues. The one CMS that's been problematic is Prismic — it's incredibly complicated to set up programmatic content publishing. I'll let Nicholas know for sure.

**Aida Knežević:** For the AI content update, Marisol is working on two blogs this week. We'll have them ready by end of week. Sydney has also implemented edits on the first blog we delivered. It's over 3,000 words long. You can let her know if it's hitting the marks on what you want for CS 101 content.

**Ankit Pahuja:** I think that Mansi can take up this next step.

**Mansi Bhalothia:** Okay, perfect.

**Aida Knežević:** Where do we get the data for keyword volumes in the Airtable?

**Ankit Pahuja:** We took the approved topics and adjusted the data. The keyword search volume comes from SEMrush. Sometimes it depends on how we generate assignments — we can use a keyword or a URL. If you find a competitor blog post and want to publish something similar, we can use that URL and plug it into our workflows. In that case, the search volume contains the search volume for all keywords that blog post ranks for. It's not just one specific keyword; it's all of them.

**Aida Knežević:** So sometimes you see high volumes for something like "prompt hacking" not because it's a single keyword, but because it's all the keywords that URL ranks for.

**Ankit Pahuja:** Got it. For the "behavioral AI versus traditional security" topic with 3600 volumes — someone from my team reported this number mismatches. But I understand now — it's not just the direct term but around the topic overall.

**Aida Knežević:** You're not the first to ask. We had another client in healthcare who saw high search volumes and asked how that was possible. Same reason — multiple keywords, not one. I'll pass this along to Sydney. Maybe switching to single-keyword search volumes would be simpler.

**Ankit Pahuja:** Internally, we follow a pillar and cluster strategy — parent topics are pillars, supporting topics become clusters. That's how we structure content. Some of the skips and approvals are influenced by that analysis. We paused listicles since last quarter because there was discussion within our brand about giving visibility to competitors. That's still being discussed. We want to snooze listicles for now and push them maybe to next month. Also, from SEO analysis, we want to target "AI versus traditional security" as the primary keyword because our SEO person got confused between that and "behavioral AI versus traditional security."

**Aida Knežević:** I do remember you talking about listicles. It's fine if you want to put it on the back burner. With LLMs and AI now, marketing teams can use that in discussions — a lot of content is going to be read by LLMs. It's a good opportunity to convince people. We do see greater visibility from these types of assignments, even though they're pure SEO plays. I totally understand that companies don't want to talk about competitors, especially big enterprises. Some are concerned about legal implications. And when they do allow it, we can only talk about them factually — never their cons or what they don't do well.

**Ankit Pahuja:** Yeah, even for the posts we've put out, we made sure anything we write about competitors is just factual with no comparative language.

**Aida Knežević:** It's the safest way to go about it. Another pending item — Sydney and Marisol have been doing additional keyword research based on feedback you've provided. They're going to upload those assignments to Airtable, and we'll let you know when it's ready for review and approval.

**Ankit Pahuja:** I look forward to the meeting with devs. After that, with visibility to the whole project on CVE and vulnerability databases, we can put forward a timeline on the go-live date. It's a priority I'm being pushed on, so I want to set the right expectations.

**Aida Knežević:** That's good to know. I'll mention this to the team in our stand-up so we can brainstorm a timeline for you.

**Ankit Pahuja:** Okay, perfect. Do you have anything else?

**Aida Knežević:** I think I'm good.

**Ankit Pahuja:** Sounds good. Thank you so much. I'll see you later.

**Aida Knežević:** All right. See you. Bye.
