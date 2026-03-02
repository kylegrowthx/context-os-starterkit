# CMS walkthrough - Parloa

<metadata>
date: 2026-02-04
time: 15:02 UTC
duration: 15 minutes
organizer: william@growthx.ai
participants: William Leborgne (GrowthX), Dora (Parloa), Tom Nguyen-Phuoc (Parloa)
fathom_recording_id: 119656249
fathom_url: https://fathom.video/calls/556692665
share_url: https://fathom.video/share/sx7xoN4V4G4-vyVbcAu_Lx1tMiauQTr9
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX walked through the Storyblok CMS workflow with Parloa's team, establishing a staged content publishing model where GrowthX prepares blog posts and Parloa handles final review and publication. Three key decisions emerged: Parloa will provide abstract blog images by end of week (rejecting GrowthX's AI-generated samples), Parloa will map authors to content clusters by expertise, and GrowthX requested schema markup functionality to improve SEO and LLM citation potential.

---

## Context

This meeting was part of GrowthX's ongoing SEO content marketing engagement with Parloa, a conversational AI company. William Leborgne (GrowthX SEO Lead) requested a CMS walkthrough with Parloa's technical team to establish the blog publishing workflow. The goal was to streamline content production by having GrowthX stage fully-edited posts in Storyblok, leaving Parloa responsible only for final review and publication. Dora, likely a marketing or product operations lead at Parloa, joined the call alongside Tom Nguyen-Phuoc, the technical expert responsible for maintaining the CMS infrastructure and making feature requests to the web development team.

---

## Relevance

**Delivery & Content Execution**
- Established operating model for Parloa content staging in Storyblok—GrowthX prepares, client publishes, reducing friction and validation cycles
- Defined CMS workflow (clone → edit fields → publish) with clear status indicators (green = published, half-green = staged)
- Identified H2 requirement for auto-generating table of contents, impacting content formatting standards

**SEO & Content Optimization**
- Schema markup feature request directly addresses LLM citation potential—critical for content visibility in AI-powered search and summaries
- Established that featured blog images double as social thumbnails (no separate thumbnail capability), affecting design strategy
- Author rotation strategy by content cluster improves topical authority and citation credibility for specialized content (e.g., technical content under Head of Product Paul)

**Client Relationship & Execution**
- Clarified Parloa's design standards are higher than AI-generated imagery—commitment to provide approved abstract images by Feb 6 ensures design consistency
- Tom Nguyen-Phuoc owns CMS technical questions; web developer consultation needed for schema markup feasibility—clear ownership prevents delays

---

## Decisions & Commitments

**Agreed Workflow**
- GrowthX will stage blog posts in Storyblok with content fully prepared; Parloa responsible for final review and publish
- Content must use H2 headings to auto-generate table of contents on blog pages

**Image Strategy**
- GrowthX AI-generated imagery rejected; Parloa will provide batch of approved, abstract images by Feb 6, 2026
- Featured image serves as social media thumbnail—no separate thumbnail field available

**Author Strategy**
- Parloa will map authors to content clusters based on expertise (e.g., Head of Product Paul for technical content)
- Dora to share author-to-cluster mapping and author rotation plan with GrowthX

**Feature Request**
- Tom to consult web developer on feasibility and effort to add schema markup field to SEO section in Storyblok

---

## Open Questions

- What is the timeline for Parloa's web developer to evaluate schema markup implementation?
- Will Parloa provide the abstract image batch on schedule (Feb 6)?
- Are there any technical constraints on the author rotation system in Storyblok?

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
- Email William (GrowthX) author-to-cluster mapping; categorize Storyblok authors; set rotation
- Review GrowthX blog image samples with internal design team; send feedback to William
- Send abstract blog image batch to William (GrowthX) by Feb 6

**Tom Nguyen-Phuoc (Parloa)**
- Email Parloa web developer re: Storyblok schema markup field; update William (GrowthX) on feasibility/timeline

**William Leborgne (GrowthX)**
- Share AI-generated blog image samples with Dora for review

---

## Transcript

**Dora (Parloa):** I think I shared with you a little bit before, like GrowthX is our SEO agency, and then William is our point of contact and leading the whole SEO revamp project with us. And he had some questions about how we manage the CMS. I cannot stay in this meeting for the entire time, but I'll stay for about 10 minutes. Tom is the expert here.

**William Leborgne (GrowthX):** Yeah, no problem. Really, what we're doing here is just getting a brief walkthrough of how you publish content. Because the idea is that we would be producing content and staging it in your CMS, setting it up. Then you guys just have to press the publish button to simplify everyone's job and make sure everything goes smoothly. So if you just want to open up and share your screen, show me your process for publishing blog posts. Maybe we'll be in and out in 10 minutes.

**Tom Nguyen-Phuoc (Parloa):** Yeah.

**Tom Nguyen-Phuoc (Parloa):** Okay, that's super fast. I can show it to you. So basically, once you have access to Storyblok, you'll just have to select the account. Then you'll arrive on that page. On the left side, you'll have the content section. And then you'll see two folders: N and E.

**William Leborgne (GrowthX):** So E for English and N for the German site?

**Tom Nguyen-Phuoc (Parloa):** Right. So when you click, you'll have new folders here. You just have to find the blog one—it's right here. Otherwise, you can just search for it in the search bar. If I go into the blog folder, you'll see all the blog posts we have on the website. If they're green, it means they're published. If they're half green, it means there were changes saved but not yet published.

**William Leborgne (GrowthX):** Got it.

**Tom Nguyen-Phuoc (Parloa):** What we do usually is clone an existing post. So we select it, clone it, name it—let's say "test"—and then duplicate it. Once you're there, it's pretty simple. You can select the topic that we have. If you need new ones, we can create them. Then you have the author that you could select. We have multiple authors. If you need to add more later, you can ask us. It's in another folder where you'd duplicate an old one and change the name.

**William Leborgne (GrowthX):** I don't think we need to duplicate authors, but what we do need to clarify is which author is for what type of content. Or you could have one author for everyone.

**Dora (Parloa):** That's actually what I'm working on right now. I asked a freelancer to pull the list of authors in Storyblok and see who's still active. I want to categorize them and set up a rotation. Right now on your website, it looks like you have a single content marketer, but I think it would be good to rotate. I'll share that information with you.

**William Leborgne (GrowthX):** What some of our clients do is map authors to content clusters from the strategy—assign specific experts to specific topics. So if it's technical content, you'd have your Head of Product Paul. If it's something else, someone different. That kind of thing.

**Tom Nguyen-Phuoc (Parloa):** Right.

**Tom Nguyen-Phuoc (Parloa):** Once you're there, you can select or change the image, or upload one from your design team. You have the excerpt here that you can edit. Below that is the rich text editor. The only thing to know is that if you want the table of contents on the left side, you have to use H2 headings. Those will automatically generate the index.

**William Leborgne (GrowthX):** Got it.

**Tom Nguyen-Phuoc (Parloa):** You can add bold, bullet points, and other formatting. Below that is the SEO section where you can add meta title and meta description. If you need to link an English version to a German version, you just select the German post and save it. The connection happens automatically. You can also add forms and buttons—just click and select the relevant page or form section. That's pretty much it.

**William Leborgne (GrowthX):** This is great. Storyblok is very simple, and I'm glad that's what you're using. I do have one question though. For SEO purposes, we typically include schema markup, and I don't see a place for that in your SEO section. It's not mission critical, but it's ideal for getting cited by LLMs. Could you look into how difficult it would be to add a schema markup field to the SEO section?

**Tom Nguyen-Phuoc (Parloa):** Yeah, we'd just have to ask our web developer about that.

**William Leborgne (GrowthX):** Okay, great.

**Tom Nguyen-Phuoc (Parloa):** One more thing—the thumbnail for social media is taken from the featured image you add here. So you can't have a separate thumbnail.

**William Leborgne (GrowthX):** That's fine. Actually, Dora, I put together some blog image examples. Since you're here, let me share them with you. We created an image generator based on your existing website imagery. Here are some examples of what we'd use for the blog. Does this feel like the right direction?

**Dora (Parloa):** I think we might need to change this a bit. Would you mind sharing it with me? I'd like our designer to review it. I think the style is close, but we have very high design standards for our website. We may have to provide our own. But please send it to me, and I'll double-check.

**William Leborgne (GrowthX):** Let me put these blog images in our Slack chat. Our main concern is avoiding any delay, obviously.

**Dora (Parloa):** If you can just get us a batch of abstract images with no specific correlation to the blog topics, we're happy with that. We actually have an inventory of images we can provide. We should be able to give you a batch by end of this week.

**William Leborgne (GrowthX):** Okay, super. Anything else?

**Dora (Parloa):** No, I think we're good. Tom, thank you so much for jumping in.

**Tom Nguyen-Phuoc (Parloa):** Of course. If you have any questions, just send me a message or email.

**William Leborgne (GrowthX):** Sounds good. Thanks, both of you.
