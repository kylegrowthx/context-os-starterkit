# Strapi <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-21
time: 18:59 UTC
duration: 26 minutes
organizer: team@growthxlabs.com
participants:
  - name: Victor Coisne
    organization: Strapi
    email: victor.coisne@strapi.io
  - name: Paul Bratslavsky
    organization: Strapi
    email: paul.bratslavsky@strapi.io
  - name: Theodore Kelechukwu Onyejiaku
    organization: Strapi
    email: theodore.onyejiaku@strapi.io
  - name: Golzar Yaghoubpour
    organization: Strapi
    email: golzar.yaghoubpour@strapi.io
  - name: Carrie Chowske
    organization: GrowthX
    email: carrie@growthx.ai
  - name: Vivek Shankar
    organization: GrowthX
    email: vivek@growthxlabs.com
  - name: Usman
    organization: GrowthX
    email: usman@growthxlabs.com
fathom_recording_id: 116083994
fathom_url: https://fathom.video/calls/538013034
share_url: https://fathom.video/share/J2yKVJyewG3PGeyd1gdkNfUcgCqy7Gco
source: fathom
enriched_on: 2026-02-28 02:15 UTC
</metadata>

---

## Summary

Weekly sync between Strapi and GrowthX teams addressing content blockers, integration page form standardization, and new CMS best practices blog workflow. Carrie Chowske is transitioning in from Vivek Shankar, with demo of GrowthX’s new AI visibility tool (evaluation-stage query focus) scheduled for the following week.

---

## Context

Strapi and GrowthX maintain a content partnership where GrowthX provides blog posts, integration pages, and comparison pages for the Strapi CMS documentation site. This sync occurs weekly to resolve content blockers and align on new initiatives. The partnership aims to improve Strapi’s SEO visibility through high-quality, technical content. As of this call, Carrie Chowske is assuming leadership of the GrowthX side from Vivek Shankar, who will join one more call for handover. On the Strapi side, Victor Coisne drives strategy and visibility, Theodore manages CMS publishing, and Paul focuses on technical implementation and code examples.

---

## Relevance

- **Content Production:** Status on comparison pages (30 delivered, next batch due this week), integration pages (form standardization pending), and blog posts (volume tracking after new content type additions).
- **New Workflow:** CMS best practices blog post using two-step skeleton-then-technical approach, with Launchpad demo app as the standard for all future code examples.
- **Staffing Transition:** Carrie Chowske stepping in as primary contact for GrowthX, Vivek Shankar providing transition support.
- **Product Development:** GrowthX’s internal AI visibility tool (focused on evaluation-stage queries) delayed Atlas, demo scheduled for next week.

---

## Overview

- **Comparison Page Blocker:** The missing `CM` collection type is blocking the launch of comparison pages, which currently appear blank. GrowthX will deliver the next batch this week.
- **Integration Page Fix:** The form component is broken on many integration pages. This is a CMS fix (not a dev task) to standardize on a newsletter signup form.
- **New Content Workflow:** A new technical blog post will use a two-step workflow: GrowthX provides the skeleton, and Paul adds technical details using the Launchpad demo app.
- **Tooling Update:** GrowthX's internal AI tool (a Scrunch alternative) is delayed, as engineering is focused on a new AI visibility tool that Carrie will demo next week.

---

## Key Topics

### Content Production & Blockers

  - **Comparison Pages:**
      - **Problem:** Pages are blank because the required `CM` collection type is missing.
      - **Status:** \~30 pages delivered; Theo awaits the next batch and the `CM` entries.
      - **Resolution:** GrowthX will deliver the next batch and `CM` entries this week.
  - **Integration Pages:**
      - **Problem:** The form component is broken or missing on many pages.
      - **Solution:** Standardize on a single "Subscribe to Newsletter" form.
      - **Action:** This is a CMS content fix, not a dev task. Theo will provide a working example to GrowthX for replication.
  - **Blog Posts:**
      - **Blocker:** Theo is awaiting new blog images to meet the new year's visual standards.
      - **Volume:** Production volume has dropped from 7 posts/week. Carrie will investigate if this is a temporary effect of prioritizing new content types.
      - **Quality:** In-post images are meeting expectations.

### New Content Initiative: CMS Best Practices

  - **Goal:** Create a technical blog post on CMS best practices, inspired by Vercel's "Next.js Bucks" guide.
  - **Rationale:** A single, comprehensive post will maximize SEO and promotion impact.
  - **Workflow:**
    1.  **GrowthX:** Delivers the initial skeleton draft.
    2.  **Paul:** Adds all technical details and code snippets.
  - **Standard:** All future blog posts will use the Launchpad demo app for code examples.
  - **Future Idea (V2):** Publish Strapi "skills" on CloudCode (like Medusa). This is deferred to V2 due to bandwidth and the need for engineering alignment.

### Tooling & Transition

  - **Tooling:**
      - **Atlas:** Delayed.
      - **New AI Tool:** GrowthX is building an internal AI visibility tool (a Scrunch alternative) focused on high-intent evaluation-stage queries. It offers instant data and custom prompts. Carrie will demo it next week.
  - **Transition:** Carrie is taking over from Vivek. Vivek will join next week's call for a final handover.

---

## Action Items

**Victor Coisne (Strapi)**
- Review Airtable tabs; request additions from Carrie if needed

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Send LLM topics chat thread to Carrie
- Check for and publish new blog posts/integration pages from GrowthX
- Share working newsletter form config + screenshots w/ Carrie; then Carrie ensures new integrations use it

**Paul Bratslavsky (Strapi)**
- Add Launchpad code snippets and technical details to ‘Ride the Wave’ CMS best practices skeleton draft

**Carrie Chowske (GrowthX)**
- Send ‘Ride the Wave’ skeleton to Paul; then Paul adds Launchpad code
- Check blog post volume; report to Victor
- Demo AI visibility tool next sync (Tue 9:30 PT)

---

## Transcript
**Paul:** Hello.

**Carrie Chowske:** Hi, how are you? My name is Carrie.

**Paul:** Nice to meet you.

**Carrie Chowske:** Vivek wasn’t available, so I’m going to be flying solo, so hopefully you guys will have a little patience with me.

**Paul:** Yeah, no worries. Just checking in if Victor’s here.

**Carrie Chowske:** Let me double-check with Theo. He didn’t respond to the meeting invite.

**Victor Coisne:** I know Victor was coming.

**Paul:** We moved the meeting to Tuesdays at 9:30 PT.

**Victor Coisne:** Hi, can you hear me? I was going to touch base quickly with Carrie. Vivek responded in the thread about updates on integration pages and comparison pages. I want to make sure I have visibility into where we are. That’s what I wanted to cover today.

**Paul:** I’ll stay for the call.

**Victor Coisne:** Perfect.

**Carrie Chowske:** Awesome.

**Carrie Chowske:** Did you have any questions?

**Carrie Chowske:** I'm meeting with Vivek several times this week and next as part of the transition.

**Carrie Chowske:** So, if there's anything else, too, that he didn't get to.

**Carrie Chowske:** It looks like he covered everything that you asked about, but I just wanted to make sure that you were good there.

**Victor Coisne:** I’m lacking visibility on what’s missing. Is everything in Airtable? I need to dive deeper on the tabs to see GrowthX’s status and understand our SEO volume queue.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I can update the Airtable tabs if you need additional visibility. Content is on track for this week. Vivek sent over new topics that need review, mostly for LLM gaps.

**Theodore Kelechukwu Onyejiaku:** We've reviewed these topics. They look good except for one. I'll send you the chat thread.

**Carrie Chowske:** Most is already in progress. We're waiting on the CM entries for the comparison page list—that should be done by Friday.

**Victor Coisne:** The first action item is shipped. We used to have a big table that was removed, now pages are showing blank. You’ve received about 30 comparison pages—have these been published? Vivek said the next batch will be delivered this week as planned.

**Theodore Kelechukwu Onyejiaku:** We’ve published some entries using Pages. I’m waiting for the next batch and need to create the CM collection type entries.

**Victor Coisne:** Good. On the integration side, what’s in your queue? Did you publish everything from GrowthX so far?

**Theodore Kelechukwu Onyejiaku:** I’ve published the latest batch of blog posts and integration pages. I’ll check for new ones this week. The main blocker was getting the right images, but that’s resolved.

**Victor Coisne:** The related integration pages have been shipped—the cross-linking between pages. The FAQ component looks good. The main remaining issue is the form component.

**Victor Coisne:** The form component is inconsistent. Some pages don’t have the form showing. We need to standardize on a "subscribe to newsletter" form across all integration pages. This is a CMS content fix, not a dev task. Theo, can you find one that renders correctly with the newsletter form, then share that config and screenshots with Carrie so new pages use the right form ID?

**Theodore Kelechukwu Onyejiaku:** I’ll do that for new entries and share screenshots for context.

**Victor Coisne:** We’ll also need to go back and fix existing pages. That covers integration.

**Victor Coisne:** The next topic is the "Ride the Wave" CMS best practices blog post, following Vercel’s "Next.js Best Practices" approach. GrowthX doesn’t have all the Strapi knowledge for a complete article. Paul, how do you want to collaborate?

**Victor Coisne:** GrowthX provides the skeleton draft, then you fill in technical details and code snippets.

**Paul Bratslavsky:** I see two paths: one is exactly what you described, with a skeleton draft. Or GrowthX provides a top-level overview, we create an in-depth guide, and they publish separately.

**Victor Coisne:** I recommend one comprehensive post to maximize SEO and promotion impact.

**Paul Bratslavsky:** That makes sense. We can do the first pass, and I’ll add technical details afterwards.

**Victor Coisne:** And as we discussed earlier, you’re going to use Launchpad, right? Launchpad is our official demo app for showcasing Strapi with Next.js frontend. Moving forward, Launchpad should be the standard code example for all blog posts.

**Paul Bratslavsky:** Got it. That’s the standard going forward.

**Victor Coisne:** I’ve also seen other companies like Medusa publish skills on CloudCode. Could we do that for Strapi?

**Paul Bratslavsky:** That would be cool, but it would need alignment with our engineering team on best practices, and we’d have bandwidth constraints.

**Victor Coisne:** Let’s focus on V1 first—GrowthX skeleton, your Launchpad code. If it gets good traction, we can discuss publishing skills in V2.

**Paul Bratslavsky:** Makes sense.

**Carrie Chowske:** I’ll get that to our content team.

**Victor Coisne:** Is there anything blocking you, Theo? We want to make sure we’re not the bottleneck and keep velocity up.

**Theodore Kelechukwu Onyejiaku:** The main blocker is getting the right images for the new year standards. Volume has been inconsistent—we used to do seven a week. I’m not sure if it’s temporary or related to ramping up on integration and comparison pages.

**Victor Coisne:** Let me know if it’s a seasonal effect or related to the new content types.

**Carrie Chowske:** Adding new content types can affect volume. I’ll follow up to make sure we’re meeting our commitments.

**Victor Coisne:** Do you have any update on Atlas?

**Carrie Chowske:** Not at the moment. Our engineering team has been focused on building our own internal AI visibility tool—similar to Scrunch but with instant data and custom prompts pre-loaded. It’s focused on evaluation-stage, high-intent queries. I’ll demo it next week. Atlas has been delayed because of that, but we’re refining it.

**Victor Coisne:** That sounds good.

**Carrie Chowske:** Next week Vivek will join for his final call. He’s getting me up to speed on everything for a smooth transition.

**Victor Coisne:** Are the in-post images meeting quality expectations? We’ve discussed that several times.

**Theodore Kelechukwu Onyejiaku:** So far, so good. I’ll flag any typos, brand issues, or clarity problems.

**Victor Coisne:** Great.

**Victor Coisne:** All right. Talk to you next week.

**Carrie Chowske:** Thanks, team. Bye.

**Paul Bratslavsky:** Thanks, everybody. Bye.

**Theodore Kelechukwu Onyejiaku:** Bye, everyone.
