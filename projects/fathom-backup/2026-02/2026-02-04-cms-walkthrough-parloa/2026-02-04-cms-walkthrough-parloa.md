# CMS walkthrough - Parloa

<metadata>
date: 2026-02-04
time: 15:02 UTC
duration: 16 minutes
organizer: William Leborgne (GrowthX)
participants: William Leborgne (GrowthX), Dora (Parloa), Tom Nguyen-Phuoc (Parloa)
fathom_recording_id: 119656249
fathom_url: https://fathom.video/calls/556692665
share_url: https://fathom.video/share/sx7xoN4V4G4-vyVbcAu_Lx1tMiauQTr9
source: fathom
enriched_on: 2026-02-27 14:27 UTC
</metadata>

---

## Summary

William Leborgne (GrowthX) walked through the Storyblok CMS workflow with Tom and Dora (Parloa), demonstrating how to clone, edit, and publish blog posts to streamline Parloa's content publishing process. The team identified a critical SEO gap: the absence of a schema markup field in the CMS, which Tom committed to reviewing with the web developer for feasibility. Parloa will provide a batch of approved, abstract images by end of week to replace GrowthX's AI-generated designs, which didn't meet Parloa's design standards.

---

## Context

This meeting was part of GrowthX's SEO revamp project for Parloa, a B2B content marketing client. The goal is to simplify Parloa's publishing workflow by having GrowthX stage all content in Storyblok, leaving Parloa with a single final "publish" button to press. This reduces friction and ensures quality control on GrowthX's side before content goes live.

The discussion also surfaced two operational decisions: Parloa plans to implement an author rotation strategy based on content clusters and expertise (e.g., assigning technical content to their Head of Product), and they will provide a curated set of abstract images for blog posts rather than accepting GrowthX's generated designs.

---

## Relevance

- **CMS Implementation:** Validates Storyblok's simplicity for staged content workflows; critical for scaling GrowthX's delivery process.
- **SEO & Technical:** Schema markup is a priority for LLM citation; feasibility assessment required from Parloa's web dev.
- **Design & Brand:** Parloa's design standards require curated, abstract imagery rather than AI-generated assets; impacts content delivery timeline.
- **Operational Efficiency:** Author rotation strategy improves content credibility and expertise alignment; Dora to finalize cluster-to-author mapping.
- **Project Status:** Meeting confirms CMS workflow is ready for GrowthX to begin staging content; no blockers identified.

---

## Overview

- **CMS Workflow:** The Storyblok content workflow is simple: clone a post, add content, and publish. GrowthX will stage posts, requiring only a final review and publish from the client.
- **Schema Markup:** A feature request was made to add a schema markup field to the CMS. This is a key SEO tactic for improving visibility in search results and LLM-powered summaries.
- **Blog Imagery:** GrowthX's AI-generated images were rejected for not meeting the client's high design standards. The client will provide a batch of approved, abstract images by EOW.
- **Author Strategy:** The client is defining a new author strategy to assign specific authors to content clusters based on their expertise, replacing the current single-author approach.

---

## Key Topics

### Storyblok CMS Workflow

  - **Goal:** GrowthX will stage content in Storyblok, simplifying the client's role to a final review and publish.
  - **Process:**
    1.  Navigate to `Content` → `E` (English) or `N` (German) → `blog`.
    2.  Clone an existing post to create a new draft.
    3.  Edit content fields: topic, author, image, excerpt, and rich text body.
    4.  Use H2s to automatically generate a table of contents on the left side of the post.
  - **Status Indicators:**
      - **Green:** Published
      - **Half-Green:** Saved changes, but not yet published

### Feature Request: Schema Markup

  - **Request:** Add a schema markup field to the SEO section of the CMS.
  - **Rationale:** Schema markup is a critical SEO tactic for improving content visibility in search results and for being cited by LLMs.
  - **Action:** Tom will consult the web developer on the feasibility and effort required.

### Blog Imagery & Authors

  - **Imagery:**
      - GrowthX's AI-generated image examples were rejected for not meeting the client's high design standards.
      - The client will provide a batch of abstract, approved images by EOW.
      - **Constraint:** The featured image is also used as the social media thumbnail; a separate thumbnail cannot be set.
  - **Authors:**
      - The client is defining a new author strategy to replace the current single-author approach.
      - **Goal:** Assign specific authors to content clusters based on their expertise (e.g., Head of Product Paul for technical content).

---

## Action Items

**Dora (Parloa)**
- Email William author-to-cluster mapping; categorize Storyblok authors; set rotation
- Review GrowthX blog image samples; send feedback to William (GrowthX)
- Send abstract blog image batch to William (GrowthX) by Feb 6

**Tom Nguyen-Phuoc (Parloa)**
- Email web dev re: Storyblok schema markup field; update William (GrowthX) on feasibility/timeline

---

## Transcript

**Dora:** I think I shared with you a little bit before, like GrowthX is our SEO agency, and then William is our point of contact and leading the whole SEO revamp project with us. He had some questions about how we track the CMS. I cannot stay in this meeting for the entire time, but I will stay for about 10 minutes. Tom is the expert here.

**William Leborgne:** Yeah, no problem. Really, Tom, what we're doing here is just getting a brief walkthrough of how you would publish content.

**William Leborgne:** The idea is we'll be producing content and staging it in your CMS. Then you just press the publish button—we simplify everyone's job. If you can share your screen and show me your process for publishing blog posts, we should be in and out in 10 minutes.

**Tom Nguyen-Phuoc:** Okay. So once you have access to Storyblok, select the account. On the left side, you'll see the Content section with two folders: N (German) and E (English). Click on the blog folder—or search for it. In the blog section, you'll see all blog posts on the website. Green means published. Half-green means changes were saved but not published yet.

**Tom Nguyen-Phuoc:** What we usually do is clone an existing post—select it, clone it, duplicate it. Once you're there, it's simple. You select the topic we have. If you need new ones, Brad or I can help create them. You can also select from multiple authors. If you need to add authors later, we duplicate an old one and change the text.

**William Leborgne:** We'll need to clarify which author goes with what type of content. We could have one author for everything, or rotate them.

**Dora:** That's what I'm working on now. I asked a freelancer to pull all the authors in Storyblok. Some of them aren't working with us anymore, so I'm going to categorize them and set up a rotation. Right now it looks like our single content marketer on the website, but rotating would be better.

**William Leborgne:** Some clients assign authors based on content clusters and expertise. For technical content, you might use your Head of Product, Paul. For other clusters, different authors.

**Tom Nguyen-Phuoc:** You can select or upload images from your design team. You have an excerpt field and a rich text editor. To create the table of contents on the left, use H2 headers (H1 is for the title). You can add bold, bullets, and other formatting. The SEO section lets you add meta title and meta description. To link an English post to a German one, select the German post and save. You can also add forms and buttons by selecting the section and configuring the CTA redirect.

**William Leborgne:** This is great. Storyblok is very simple. One question though: for SEO, we typically include schema markup. I don't see a place for that in the SEO section. It's not mission-critical, but it's ideal—especially for being cited by LLMs. Could you check with your web developer on adding a schema markup field?

**Tom Nguyen-Phuoc:** Yeah, we'll ask our web developer. And one more thing: the thumbnail is automatically pulled from the featured image on the website. You can't set a separate thumbnail.

**William Leborgne:** That's fine. Makes it easy.

**William Leborgne:** Dora, we put together some blog image examples I want to show you. We created an image generator based on your existing website imagery. Here are some samples. Does this feel like the right direction, or do you want to change it?

**Dora:** I think we might need to adjust. Can you share these with me? I'd like our designer to review them too. We have very high design standards on our website. We may need to provide our own images, but please share these. I'll double-check. If we can get a batch of abstract images with no specific correlation to individual blogs, we're happy. I think we can get you a batch by end of week. We have an inventory of images, so it should be fine.

**William Leborgne:** Great. I'll send these over Slack. Schema markup is the other request—Tom's checking on that with your web developer.

**Dora:** Yes, Tom, thank you so much for jumping in. If you have any questions, send them to me.

**Tom Nguyen-Phuoc:** Sounds good.

**Dora:** Okay, bye.

**William Leborgne:** Bye.
