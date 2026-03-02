# Metronome <> Growth X - Weekly Sync

<metadata>
date: 2026-01-27
time: 21:00 UTC
duration: 33 minutes
organizer: team@growthxlabs.com
participants:
  - name: Katya Luscomb
    email: katya@growthx.ai
    affiliation: GrowthX
    role: Content & SEO Lead
  - name: Will Watters
    email: will.watters@metronome.com
    affiliation: Metronome
    role: Content Director
  - name: Kris Carter
    email: null
    affiliation: Metronome
    role: Web & Content Operations
  - name: Will Proctor
    email: c-will.proctor@growthx.ai
    affiliation: GrowthX
    role: Team Member
  - name: Mlaflamme
    email: mlaflamme@metronome.com
    affiliation: Metronome
    role: Team Member
fathom_recording_id: 117605212
fathom_url: https://fathom.video/calls/545675190
share_url: https://fathom.video/share/paxwmUZh8hMBv1K3vWoXjhsukkzm5Ka8
source: fathom
enriched_on: 2026-02-28 03:15 UTC
</metadata>

---

## Summary

Katya Luscomb from GrowthX identified a critical SEO issue—a disabled Webflow sitemap preventing Google indexing—which Kris Carter resolved by enabling it during the call. The team aligned on three content priorities: consistent terminology across pages, objective tone in "Metronome's Take" sections, and direct source attribution. GrowthX introduced "Check That," a new AI visibility tool launching in February that tracks Metronome's mentions across LLM responses against competitors like WithOrb, GetLogro, Tabs, and Maxio.

---

## Context

This weekly sync focused on Metronome's pricing index content performance and the relationship between organic search visibility and LLM-driven discovery. The critical sitemap issue meant that 97% of the content was invisible to Google, making performance data unreliable. With the sitemap fix in place, GrowthX expects to validate content quality through improved indexing data. The conversation bridged technical SEO fixes with product marketing strategy—specifically how to optimize content for both traditional search and emerging AI visibility channels. This reflects a broader industry shift where B2B SaaS pricing comparison content must work across multiple discovery mechanisms.

---

## Relevance

**GrowthX Context**
- Katya Luscomb leading the content partnership for Metronome's pricing index
- Demonstration of GrowthX's "Check That" tool (launching Feb 2026) as key competitive differentiator
- Opportunity to define attribution and KPI reporting between GrowthX and client

**Metronome Context**
- Will Watters owns content quality and editorial direction at Metronome
- Kris Carter handles technical implementation and site operations
- Focus on building credible, sourceable content that performs in both organic and AI-driven discovery

**Product & Technology**
- "Check That" tool uses 100k+ pre-built prompts with historical LLM response data
- Potential to influence backlinking strategy for AEO (AI Engine Optimization)
- HubSpot/Salesforce integration planned for attribution tracking

---

## Overview

- **Critical SEO Issue Resolved:** A disabled Webflow sitemap was causing widespread indexing failures. Kris Carter enabled it during the meeting, which should fix the problem.
- **Content Strategy Aligned:** Will Watters defined three priorities: consistent terminology, an objective "Metronome's Take" tone, and sourcing information directly on pages.
- **New AEO Tool Demoed:** Katya Luscomb demoed "Check That," a new tool launching in February that tracks AI visibility against competitors (WithOrb, GetLogro, Maxio, Tabs).
- **Reporting KPIs Defined:** Katya Luscomb will DM Will Watters for Metronome's KPIs and attribution setup (HubSpot/Salesforce) to enable more strategic reporting.

---

## Key Topics

### Critical SEO Issue: Sitemap & Indexing

  - **Problem:** A 404 sitemap error was preventing Google from indexing most site content, causing poor organic visibility.
  - **Root Cause:** Webflow's sitemap feature was disabled.
  - **Resolution:** Kris Carter enabled the sitemap during the call.
  - **Next Step:** Katya Luscomb's technical SEO expert will now re-evaluate the site to confirm the fix and identify any other indexing issues.

### Content Strategy & Quality

  - **Will Watters' 3 Priorities:**
    1.  **Consistency:** Use similar terminology (e.g., "good, better, best") across pages to improve user experience.
    2.  **Tone:** Maintain an objective, informative voice in the "Metronome's Take" section.
    3.  **Sourcing:** Link directly to sources on pages to build credibility and enable verification.
  - **Logo Workflow:**
      - **Current:** Kris Carter sources/creates logos as needed.
      - **Proposed:** GrowthX can source logos and upload them to Airtable for Kris Carter.
      - **Decision:** Kris Carter will continue the current process for now, but may adopt the new workflow if volume increases.

### Performance & Reporting

  - **Current Performance:**
      - Only 3 pricing index pages are indexed (Grok, AWS Lambda, main hub).
      - Indexed pages show good session volume but low engagement.
      - **Hypothesis:** Engagement is low because CTAs are only at page bottom.
      - **Data Anomaly:** The December traffic spike was due to the Stripe acquisition announcement, not organic growth.
  - **AI Visibility Tool: "Check That"**
      - **Purpose:** Track how Metronome and competitors appear in LLM responses.
      - **Features:**
          - Uses a library of 100k+ pre-built prompts with historical data.
          - Compares brand visibility, citation count, and sentiment.
      - **Competitors to Track:** WithOrb, GetLogro, Maxio, Tabs.

---

## Action Items

**Katya Luscomb (GrowthX)**
- Brief tech SEO expert re: Webflow sitemap enabled; request follow-up + noindex list
- Research AEO backlinking implications; share findings w/ Will Watters
- Add WithOrb, GetLogro, Tabs, Maxio to Check That tool; add more prompts from library
- DM Will Watters reporting/attribution questions; Will to forward to Maddie at Metronome

**Kris Carter (Metronome)**
- Send logo dimensions/specs to Katya; GrowthX to source 1 test logo for workflow validation

**Will Watters (Metronome)**
- Provide KPI priorities and attribution setup (HubSpot/Salesforce) to Katya for enhanced reporting

---

## Transcript

**Katya Luscomb:** I was just checking my email to make sure there wasn't a reschedule request that I missed.

**Will Watters:** Yeah, we had a brainstorm session with the team before, so we just got caught up. Productive stuff.

**Katya Luscomb:** Awesome. I have a long agenda today. There's some sitemap indexing things I flagged in the chat. High level, there's an issue with the sitemap that's really impacting visibility on Google. Google is having a hard time finding the content, and it's impacting sitewide performance.

**Katya Luscomb:** You guys are on Webflow, correct?

**Will Watters:** Yeah, that's my understanding.

**Katya Luscomb:** Webflow automatically creates a sitemap, but you can turn that off and use a custom one instead. The issue is that your sitemap is returning a 404 error. How we fix it depends on which setup you're using.

**Will Watters:** Let me Slack Kris to see if he can join.

**Katya Luscomb:** Sure. I've tagged him. I can answer questions or loop in our technical SEO expert.

**Will Watters:** Kris just joined.

**Katya Luscomb:** I also want to mention—you're incorporating logos. We could source those and put them in Airtable so they're pre-uploaded and ready for Kris to use instead of him having to hunt them down.

**Will Watters:** Yeah, I'm not sure about the specifics. Kris handles that on his end.

**Katya Luscomb:** Okay, I'll follow up with him separately about logo specs and the sitemap questions.

**Katya Luscomb:** Awesome.

**Katya Luscomb:** As far as we talked a little bit about pages that don't have public pricing available and like some sourcing, like adding sources to those, that is currently with our engineering team to implement in our pipeline.

**Katya Luscomb:** We've added a content calendar view that flags whether companies have public pricing pages. We're focusing on those first, and should finish the initial batch of 40 within a month. Once we fix the indexing, we'll have much better performance data across industries and can strategize on the next batch of companies.

**Will Watters:** Yeah, that makes sense. Our next meeting is in two weeks, but we might need to move it—we have a marketing onsite that week. We can review what's currently live and discuss categorization coverage.

**Kris Carter:** Before we dive in, I wanted to understand why the sitemap wasn't being used. I just enabled the Webflow sitemap XML feature, but let me know if you need more.

**Katya Luscomb:** Thanks. A widespread indexing issue triggered our investigation. I'll confirm with our technical SEO expert that the enabled sitemap addresses it or if further changes are needed. I also noticed noindex tags on some pages—are those intentional?

**Kris Carter:** Most are intentional. There might be some on specific landing pages I didn't index because they were for webinar signups. Let me know which pages you're seeing, and we can adjust them.

**Katya Luscomb:** I'll get you a full list of noindex pages. On another topic—how do you source logos? We could upload them to Airtable so you don't have to search for them.

**Kris Carter:** I usually make or source them and size them in the editor. It takes about five minutes. For now, I'm happy doing this, but if volume increases, I'll let you know.

**Katya Luscomb:** Cool. Just send us your specifications—dimensions, file format, any special requirements—and we can test one logo to see if the workflow works.

**Kris Carter:** Let's try that. I prefer SVGs when available, but sometimes I need to recolor them for dark backgrounds.

**Katya Luscomb:** Our design team might be able to convert files to SVG. Let's start with what we can find. I appreciate all the detail work on the XML—that was solid collaboration.

**Will Watters:** Cool.

**Katya Luscomb:** Cool.

**Katya Luscomb:** One thing to standardize is when we combine pages without public pricing. Are there other patterns you see that we should follow to reduce your review workload?

**Will Watters:** There are three key priorities. First, consistency in terminology. For example, Metronome uses "good, better, best" with freemium models. The more consistent we are across pages, the better the user experience—fewer lookups needed. Second, maintain an objective tone in the "Metronome's Take" section. Third—and this is most important—make sure we can point to sources directly. If our information is questioned, I need to show where it came from without hurting SEO.

**Katya Luscomb:** That's helpful. Our bibliographies are running multiple pages because of our in-depth research. We're pulling only the most relevant sources and placing them under tables that lack inline citations. For pricing history sections, we can use just the most recent source.

**Will Watters:** I've been testing our content in Claude and ChatGPT to see where Metronome ranks on comparison queries—like "how does X pricing compare to Y?" LLMs mostly point directly to company documentation. I'm curious if sourcing helps visibility there.

**Katya Luscomb:** I can research backlinking's AEO impact. Speaking of which—I have a demo of "Check That," our new AI visibility tool. It has 100k+ pre-built prompts with historical data, so you don't wait a month for results like with other tools. Want to see it?

**Will Watters:** I did some broad testing but nothing deep. Comparison queries around tools like Lovable vs. Cursor would be helpful to track. Obviously, we won't rank above the primary products, but I'd like some visibility.

**Katya Luscomb:** Let me quickly cover performance data with a caveat: only three pricing index pages are indexed by Google, so conclusions are limited. After the sitemap fix, we'll have much better data.

**Will Watters:** Yeah, with whatever.

**Katya Luscomb:** Cool.

**Katya Luscomb:** I can just do some high level notes.

**Katya Luscomb:** The pricing index pages show good session volume but low engagement. Let me fix indexing first to see if that changes the engagement rate. Then we can determine if people aren't finding what they're looking for on the page.

**Will Watters:** We're only giving them CTAs at the bottom of the page. Maybe we should add comparison tools or mid-page CTAs—like credit card comparisons. I also notice sourcing links point to AWS directly. We'll eventually have a "see this model in action" CTA, so maybe we hold for that.

**Katya Luscomb:** For stickiness, the positive is that weekly sessions are growing. Sitewide traffic is flat with slight January growth. The December spike was from the Stripe acquisition announcement. Once we fix the sitemap, I expect bigger improvements across the entire site, not just our content. Google referrals are currently very low—90% of visits come from direct clicks rather than organic search. But when content is indexed, it performs well. The Grok page ranks 11th on Google—nearly first-page territory. The AWS Lambda page and main hub also indexed. We'll learn patterns once more pages are live.

**Will Watters:** That makes sense.

**Katya Luscomb:** I'm capturing a baseline now so we can compare after fixes.

**Katya Luscomb:** I want to demo "Check That," our new AI visibility tool launching in February. Unlike Scrunch or Profound, we have 100k+ pre-built prompts with historical data, so you get insights immediately without waiting a month. It shows where you rank against competitors in LLM responses, brand positioning, citation counts, and sentiment. The dashboard shows overall visibility level plus detailed breakdowns by specific prompts. I've added some competitors already, but we can add more. Which ones matter most?

**Will Watters:** WithOrb and GetLogro are my primary focus, but Tabs and Maxio could be useful too.

**Katya Luscomb:** Perfect. I'll add those today. The tool shows brand position (high, medium, low), how LLMs describe you, and citation counts versus competitors. You can drill into specific prompts and see how visibility varies across different LLM models. It gives you actual data instead of just gut-checking your content against an LLM.

**Will Watters:** Interesting. We're learning the AEO landscape, so this helps.

**Katya Luscomb:** Absolutely. You can optimize snippets and content in Q&A formats to help LLMs pick it up. This tool shows if that's actually working rather than guessing.

**Katya Luscomb:** One last thing—I need to align on KPIs and reporting. What are your priorities for organic content and organic growth? Where should GrowthX be contributing? What metrics would excite you in six months? Also, we want to track beyond sessions and clicks—we're looking at attribution to leads and conversions. Do you have HubSpot or Salesforce tracking we can connect to?

**Will Watters:** Maddie on our team would know more about the attribution setup. I'll need to think about KPI priorities. Send me your questions in Slack, and I'll forward them to her.

**Katya Luscomb:** I'll DM you right after the call.

**Will Watters:** Perfect. Thanks for walking through all this. Great conversation.
