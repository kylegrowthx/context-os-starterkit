# Panther <> GrowthX CMS walkthrough

<metadata>
date: 2026-01-16
time: 21:29 UTC
duration: 21 minutes
organizer: Kathy Lam (GrowthX)
participants:
  - name: George Haikal
    affiliation: GrowthX
  - name: Katie Campisi
    affiliation: Panther
  - name: Kathy Lam
    affiliation: GrowthX
fathom_recording_id: 115042811
fathom_url: https://fathom.video/calls/534781021
share_url: https://fathom.video/share/vf9mjU8rJnWsrbFsmpBpimdWhK9gYLy_
source: fathom
enriched_on: 2026-02-28 13:45 UTC
</metadata>

---

## Summary

GrowthX presented a validated SEO content strategy with six approved topic clusters (led by AI SOC for Panther's March launch) and defined a three-step Framer CMS workflow for blog publishing. A new design system for blog images will streamline Katie's workload while maintaining consistency.

---

## Context

Panther and GrowthX are scaling the blog content program to support a major AI feature launch in March. Panther's CEO (Jack) closely monitors website quality, making rigorous approval workflows essential. GrowthX had previously developed a comprehensive competitor analysis and SEO research to identify high-value, low-difficulty keywords; this meeting formalized the content strategy and established operational processes for publishing through Framer, Panther's CMS.

---

## Relevance

**Content & SEO Strategy**
- Validation of six topic clusters targeting keywords with high search volume and low difficulty
- AI SOC positioned as critical priority for March launch
- Content strategy backed by competitive analysis and white-space identification

**Operations & Workflows**
- Three-stage publishing process: Google Doc review → Staging preview → Live publication
- Critical publication gate: checking `#web-dev-updates` for deployment freeze notifications
- Image creation workflow delegated to GrowthX to free Katie's capacity

**Tools & Platforms**
- Framer CMS configuration: Post collection, First/Second Feature flags, blog filters, author fields
- Slack integration for deployment coordination
- Profound SEO tool for ongoing performance tracking and opportunities

---

## Overview

- **Content Strategy Validated:** GrowthX's 6 SEO topic clusters (e.g., AI SOC, Threat Hunting) were approved. The "AI SOC" cluster is a top priority, aligning with Panther's major AI feature launch in March.
- **Framer Workflow Defined:** A strict approval process was set: Google Doc draft review → Staging link review → Publish. This ensures quality control and prevents errors from reaching the CEO.
- **Critical Publication Rule:** Before publishing, check the `#web-dev-updates` Slack channel for a "freeze" notice. If active, publishing is blocked to prevent conflicts with major site deployments.
- **Image Creation Delegated:** GrowthX will create blog images via a new workflow, freeing up Katie's time. Samples are due next week for approval.

---

## Key Topics

### Content Strategy & SEO

  - GrowthX's content strategy, based on competitor SEO analysis, was reviewed and approved.
  - **6 Approved Topic Clusters:**
      - AI SOC
      - Detection Engineering & Threat Hunting
      - Cloud Security Threats & Detection Guides
      - Incident Response & SOC Operations
      - SIM Alternatives & Comparisons
      - Security Data Architecture & Log Management
  - **Rationale:** The clusters target keywords with high search volume and low difficulty, filling content gaps relative to competitors.
  - **Priority:** The "AI SOC" cluster is critical for supporting Panther's major AI feature launch in March.

### Framer CMS Workflow

  - **Process:**
    1.  **Draft:** GrowthX shares a Google Doc for review by Katie and Seema.
    2.  **Staging:** After edits, GrowthX stages the post in Framer and sends a preview link for final approval.
    3.  **Publishing:**
          - **Check Slack:** Before publishing, check `#web-dev-updates` for a "freeze" notice.
          - **If Active:** Publishing is blocked.
          - **If Clear:** Publish the post.
  - **Rationale:** This multi-step review process ensures quality control and prevents errors from reaching the CEO, who is highly attentive to website content.

### Framer CMS Details

  - **Post Collection:** Use the "Post" collection for all new blog items.
  - **Fields:**
      - **First Feature/Second Feature:** Tag only one post as "First Feature" to avoid multiple banners on the blog page.
      - **Subtitle:** Optional; appears below the title.
      - **Blog Filters:** Katie will update the filter list to better reflect content topics, adding:
          - AI SOC
          - Cloud Security, Detection Response, Data Engineering
          - Threat Research
      - **Author:** Use "Panther" for now. A future update will add author photos and titles.
      - **Reading Time:** Not used.

### Blog Image Creation

  - **New Workflow:** GrowthX will create blog images using a new, consistent design workflow.
  - **Rationale:** This frees up Katie's time and provides a scalable solution, as Katie is running out of unique stock photos.
  - **Deliverable:** GrowthX will provide sample images next week for Katie's approval.

---

## Action Items

**Katie Campisi (Panther)**
- Review GrowthX competitor/keyword docs; add comments re: competitors/keywords/clusters
- Update Framer blog filters: add AI SOC + Threat Research; re-tag Threat Research posts
- Add GrowthX (Kathy + 1+) to Slack freeze channel (#web-dev-updates); notify team; ping Cindy if needed

**Kathy Lam (GrowthX)**
- Share 2 calibration article drafts with Katie (Panther) + Seema; then send sample images for review

---

## Transcript

**Katie Campisi:** Hey, how's it going?

**Kathy Lam:** Good. I'm so sorry—I went to grab some water.

**Katie Campisi:** You're fine. I wanted to ask—Seema asked me earlier about reviewing some of the artifacts you shared, specifically the competitor content analysis. Let me pull it up to make sure I focus on the right thing.

**Kathy Lam:** Yes, let me show you. We don't have to get too in the weeds on this. Since we have some time, I'm happy to review it completely with you.

**Katie Campisi:** I appreciate it. Can you share your screen?

**Kathy Lam:** Okay, perfect. Do you see the same page? So there's a couple of artifacts. Probably the best one to look at is in docs—we have direct and organic competitors. These are the ones we pulled, and if this is accurate, we're good. We also found a few other audience competitors. Now, if you scroll down to the six topics, if there are keywords where you think they don't belong, let us know. The way we did this: we looked at all your competitors, did the SEO research on what they rank for, looked at the white space where Panther is versus competitors, and honed in on keywords with good search volume but not too high difficulty. The six topic clusters are: AI SOC, Detection Engineering and Threat Hunting, Cloud Security Threats and Detection Guides, Incident Response and SOC Operations, SIM Alternatives and Comparisons, and Security Data Architecture and Log Management. These target lower-funnel research topics. If any of these clusters don't make sense, just add a comment and we can review them this afternoon.

**Katie Campisi:** Yeah, I added links for reference. So today we're primarily focused on the workflow for updating your CMS, right? And any approval flows.

**Kathy Lam:** Yes, exactly. Any guidance there would be awesome.

**Katie Campisi:** Let's start with Framer. You've used it before?

**Kathy Lam:** Yeah, a little bit.

**Katie Campisi:** Good, then the flow won't be unfamiliar. We use the Post collection for all our blog items. We create a new item with First Feature and Second Feature fields. If you tag multiple items as First Feature, you'll get multiple banners on the blog page instead of just one, which we want to avoid. Title is required, subtitle is optional but looks nice. We use blog filters, and I want to update them because I don't think they actually reflect our content properly. I want to add AI SOC and Threat Research filters. We have a threat research team churning out weekly blogs, and they're currently tagged as thought leadership, which isn't right. For author, we use "Panther" for now. Our CEO eventually wants blog photos and titles for each author, but we'll figure that out later. We don't use the reading time field.

**Kathy Lam:** Got it. So for the AI SOC blog filter—that'll be one main category?

**Katie Campisi:** Yes. And if content doesn't fall under AI SOC, it probably falls under Cloud Security, Detection Response, or Data Engineering, depending on the topic cluster. For images, I'd suggest keeping them consistent. Since I do most of them, I usually create them in Figma. But you mentioned a workflow—what's that look like?

**Kathy Lam:** Let me show you. This is from one of our other customers, so it won't be part of your workflow, but you'll see how we approach it. We looked at their current images and designed something similar by filling in parameters. We're creating two calibration articles right now. Once they're in draft, we'll share them with you and Seema. Then next week, we'll have sample images for your approval. If you like them, great. If not, we can handle them ourselves.

**Katie Campisi:** I like that idea. Honestly, I have a tendency to volunteer for things and then get overloaded. So let's try your approach and see how it goes. Running out of stock photos anyway—blocks, clouds, networks. A consistent design system with background and text would be perfect.

**Kathy Lam:** Excellent. And once we stage the post, should we just send you the link for preview before we go live?

**Katie Campisi:** Yes, please. Our CEO—he has this uncanny ability to notice anything published to the site within a minute. If there's an error, he catches it. So I like to check before anything goes live. Normally what we'll do: you share a Google Doc draft, I review it, you make edits, I look again to confirm everything's good, then you stage it. Once staging is ready, send me the link for approval and we'll go live.

**Kathy Lam:** Got it. Anything else on the publication side?

**Katie Campisi:** One thing: when we stage, we check the `#web-dev-updates` Slack channel for a deployment freeze notice. If there's a freeze in place, we wait. If not, we can publish. When we're staging a blog, it's usually only in staging for five or ten minutes, so it's not a huge deal, but the web dev team uses freezes for major product page overhauls or template changes affecting the whole site. So whoever is publishing from GrowthX needs to be in that channel to check. We'll add you and ping Cindy if needed.

**Kathy Lam:** So we just need to be added to the channel?

**Katie Campisi:** Yes, I'll let the team know you're contractors in there. Probably at least two of you will be posting. It's pretty straightforward—just check for the freeze, and you're good. If there's a freeze and it's been more than a day, I might ping the web dev team, but I don't think any blog posts are emergencies.

**Kathy Lam:** Who's been reviewing blogs in the past?

**Katie Campisi:** Seema usually reviews content, but our CEO is very entrenched in the marketing process. However, he's getting better about not being in the day-to-day weeds. For reactive content—announcements, product releases—he definitely looks at it. But how-to guides and thought leadership, like our threat research posts, are just me.

**Kathy Lam:** Got it. So before we wrap, what do you think of what we've shared so far?

**Katie Campisi:** Very encouraged. We bought Profound back in October or November. At that point, we thought we wouldn't get approval to pay for GrowthX, so we were going to bootstrap it ourselves. But the data hasn't changed much because we haven't had time to roll out a full content strategy. Seeing what you've put together is exactly what we need. I'm stoked on the AI SOC topic especially. We're releasing tons of new AI features next week and planning a formal launch in March. That's where we want improvement. I just met with our Profound rep right before this and asked what topic we should focus on—we both said AI SOC.

**Kathy Lam:** It doesn't hurt to have both tools for now. We're also working on CheckThat—our AI visibility tool. Once it's fully populated, I want to share it so you can compare. It offers suggestions too, and it's still in beta, but you'll like what you see when we deploy it.

**Katie Campisi:** One of my favorite Profound features is the task list—it tells me what to do if I have time. In my role, there are so many nebulous goals and different paths to them. I love just being told what to prioritize. There are so many competing priorities that even after two days of work, I don't feel like I have much to show for it.

**Kathy Lam:** Exactly. Sometimes you make 5% progress on 20 things instead of 50% progress on three. If you can focus on fewer things, done better, it makes a huge difference.

**Katie Campisi:** That's my goal this year—fewer projects, better execution. I've even said we need to outsource this work. At one point, they asked me to basically do what GrowthX does on my own.

**Kathy Lam:** If that comes up again, here's what to tell them: you need a content strategist, an SEO specialist, a content engineer, an editor, and a designer. We're aiming for five articles a week. That's not one person's job.

**Katie Campisi:** Exactly. I told them I can't generate five articles alone—they'd be garbage. We need a full team.

**Kathy Lam:** And what we've done to ensure quality is put heavy effort into the research phase. It looks at what's performing well, builds logical frameworks for articles, brings in relevant links, does fact-checking, and then someone manually edits. One person could do it, but you'd get one or two articles a week instead of five.

**Katie Campisi:** Right. Glad we're doing this properly. Well, thanks so much for this time. I'll send you the first two draft articles in an hour or two.

**Kathy Lam:** Thank you. Have a great weekend.

**Katie Campisi:** You too. Bye.
