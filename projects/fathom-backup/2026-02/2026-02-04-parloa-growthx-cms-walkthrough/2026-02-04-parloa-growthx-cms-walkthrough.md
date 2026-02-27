# Parloa <> GrowthX CMS Walkthrough

<metadata>
date: 2026-02-04
time: 14:59 UTC
duration: 18 minutes
organizer: team@growthxlabs.com
participants: Dora Kuo (Parloa), Tom Nguyen-Phuoc (Parloa), William Leborgne (GrowthX)
fathom_recording_id: 119651749
fathom_url: https://fathom.video/calls/554059476
share_url: https://fathom.video/share/u1j-57daGKs2mDL-fuzuD78_fmGBj3QM
source: fathom
enriched_on: 2026-02-27 14:32 UTC
</metadata>

---

## Summary

Tom Nguyen-Phuoc walked William Leborgne through Parloa's Storyblok CMS workflow, covering content staging, publishing, and SEO practices. The team identified a critical gap: schema markup support for LLM citations. Parloa committed to providing a batch of high-design blog images by end of week, as GrowthX's AI-generated examples didn't meet design standards.

---

## Context

GrowthX is a B2B content marketing services partner managing Parloa's blog content strategy. William Leborgne leads the SEO and content project for GrowthX. The goal is to establish a streamlined workflow where GrowthX stages content in Storyblok (pre-publishing) and Parloa's team reviews and publishes it. This meeting documented the technical publishing process and identified blockers: missing schema markup field and imagery quality concerns.

Dora Kuo (Parloa) is also establishing a new author strategy to improve content credibility by rotating bylines across content clusters rather than attributing all posts to a single author.

---

## Relevance

- **Content Operations:** Storyblok CMS setup, publishing workflow, and template cloning process for rapid content deployment.
- **SEO & LLM Visibility:** Schema markup is critical for citation by large language models; Parloa will investigate adding this field.
- **Design & Brand:** AI-generated blog images were rejected; Parloa will provide design-approved imagery by end of week.
- **Author Strategy:** Implementing author rotation tied to content clusters to build subject matter authority.

---

## Overview

- **Workflow:** GrowthX will stage content in Storyblok; Parloa will review and publish.
- **Schema Markup:** A critical SEO feature for LLM visibility is missing. Parloa will investigate adding it.
- **Imagery:** GrowthX's AI-generated images were rejected. Parloa will provide a new batch by EOW to meet the project's high design standards.
- **Authors:** Dora is creating a new author strategy (e.g., assigning authors to content clusters) to improve credibility and rotation.

---

## Key Topics

### CMS Publishing Workflow

  - **Goal:** GrowthX stages content in Storyblok for Parloa to review and publish, streamlining the workflow.
  - **Process:**
    1.  **Locate Content:** Navigate to `Content` → `EN` or `DE` → `blog`.
    2.  **Create Post:** Clone an existing post to preserve the template.
    3.  **Populate Fields:**
          - **Topics:** Select from existing tags.
          - **Author:** Select from the dropdown.
          - **Image:** Upload the main blog image.
          - **Excerpt:** Write a short summary.
    4.  **Format Content:**
          - Use the rich text editor for the main body.
          - **Critical:** Use `H2` tags for section headers to auto-generate the on-page table of contents.
    5.  **Add SEO & CTAs:**
          - **SEO Section:** Add meta title/description and link to the corresponding translated post.
          - **CTAs:** Use the `form section` or `button` components to add interactive elements.
  - **Status Indicators:**
      - **Green:** Published
      - **Half-green:** Saved but not published

### Schema Markup Gap

  - **Problem:** The CMS lacks a field for schema markup.
  - **Rationale:** This is a key SEO feature for improving content visibility and citation by large language models (LLMs).
  - **Solution:** Parloa will ask its web developer about the feasibility and effort required to add this field.

### Blog Imagery

  - **Problem:** GrowthX's AI-generated image examples were rejected for not meeting Parloa's high design standards.
  - **Constraint:** Storyblok uses the main blog image as the social media thumbnail; a separate thumbnail cannot be set.
  - **Solution:** Parloa will provide a new batch of approved images by EOW.

### Author Strategy

  - **Problem:** The current author list in Storyblok is outdated and lacks a clear strategy.
  - **Goal:** Create a new author strategy to improve content credibility and rotate authorship.
  - **Potential Model:** Assign specific authors (e.g., Head of Product Paul for technical topics) to content clusters defined in the SEO strategy.

---

## Action Items

**William Leborgne (GrowthX)**
- Email Dora Storyblok author rotation/cluster mapping

**Tom Nguyen-Phuoc (Parloa)**
- Email web dev re: add schema markup field to Storyblok blog SEO

**Dora Kuo (Parloa)**
- Review GrowthX blog image examples w/ designer; send feedback to William
- Send GrowthX batch of blog images by EOW

---

## Transcript

**Dora Kuo:** Hey, can you hear me?

**William Leborgne:** Yes, hi.

**Dora Kuo:** Hi, how are you?

**William Leborgne:** I'm doing pretty good. How are you?

**Dora Kuo:** I'm doing good. I just wish the snow in New York City would go away. Travel times take forever because the streets are already packed and narrow. With the snow, when people collect garbage, it takes forever. I feel bad for them because they have to climb on the ice. It's a crazy winter.

**William Leborgne:** Yeah, that's tough. Is there some part of you that likes it though—that magical New York with the Christmas tree and snow falling?

**Dora Kuo:** Usually that only lasts about 30 minutes. Then with too many people and cars, the snow becomes black with grease. It's not very pretty.

**William Leborgne:** No, that's not so pretty.

**Dora Kuo:** Let me pin Tom really quick. I might have to hop off the call halfway because I'm double booked, but Tom is the expert here. I'll stick around for about 10 minutes.

**Tom Nguyen-Phuoc:** Yeah.

**Dora Kuo:** So Tom, I want to give you some context. GrowthX is our SEO agency, and William is our point of contact leading the entire SEO project. He had some questions about how we work with the CMS.

**William Leborgne:** Right. Honestly Tom, we're just here to get a brief walkthrough of how you publish content. The idea is that we'll produce content and stage it in your CMS, and then you guys just press the publish button. This simplifies everyone's job. Can you share your screen and walk me through your blog publishing process? We should be in and out in 10 minutes.

**Tom Nguyen-Phuoc:** Yeah, okay. That's quick. I can show you. So once you have access to Storyblok, you select the account. On the left side, you'll see the content section with two folders: DE for the German website and EN for the English one. The blog folder is here. If I go into the blog, you'll see all the blog posts on the website. If they're green, the post is published. If they're half green, changes have been saved but not published yet. Usually, we clone an existing post to preserve the template. Once you're there, it's pretty simple. You can select the topic from the dropdown. If you need new topics, Brad can help Dora, or I can look into it. Then you have the author dropdown with multiple options. If you need to add new authors, it's in another folder—you duplicate an old one and change the text.

**William Leborgne:** We probably won't need to duplicate authors, but we do need to clarify which author is for what type of content. Or you could use one author for everything.

**Dora Kuo:** That's what I'm working on. I asked our freelancer to pull out all the authors in Storyblok. Some of them aren't working on Parloa anymore.

**William Leborgne:** Right. So you'll categorize them and set up a rotation. On our website, it looks like a single content marketer. But rotating authors across content types would be better.

**Dora Kuo:** Exactly. That's a side project I'm working on now. I'll share that information with you too.

**William Leborgne:** What some of our clients do is map authors to the content clusters from the strategy we shared. For example, a technical cluster might use your head of product, Paul, and a different cluster would use someone else. That makes sense?

**Tom Nguyen-Phuoc:** Right. So you can select or upload an image for the blog post. You have the excerpt field. And then the main body is just a rich text editor. The key thing is: if you want the table of contents on the left side, you have to use H2 tags for section headers. It's a bit confusing here because the first header is H1, but it should be H2. We can sort that later. H2 tags generate the on-page table of contents. You can add bold, bullet points, and so on. You have the SEO section where you add the meta title and description. If you need to link an English version to a German one, just select the German blog post and save it. And if you need to add a form or button, you can do that too—just select the form section or button component, and then pick the page for the CTA redirect. That's pretty much it. If you have questions, send me an email or Slack message and I'll help.

**William Leborgne:** This is great. Storyblok is very simple. I'm glad you're using it. I do have one question though. Typically for SEO purposes, we include schema markup. In your SEO section, I don't see a field for that. It's not mission critical, but it's really ideal, especially for getting cited by LLMs. Could you look into how difficult it would be to add a schema markup section in the SEO part?

**Tom Nguyen-Phuoc:** Yeah, we'll just have to ask our web developer about that.

**Dora Kuo:** Yeah. I could either take it or handle it.

**Tom Nguyen-Phuoc:** One more thing: the thumbnail is pulled from the blog image you upload. You can't have a different thumbnail than the main image on the website.

**William Leborgne:** That's fine. That makes it easy. Well actually, Dora, we put together some example blog images. I was going to share this later, but since I have you here, I'll show it now. We created an image generator based on the imagery on your website. Here are some examples we'd use for the blog. Does this feel like the right direction?

**Dora Kuo:** I think we might need to change it a bit. Can you share this with me? I'd like our designer to take a look. We have a very high standard for design. Maybe we'll have to provide our own images at the end, but please share that with me and I'll double-check.

**William Leborgne:** Yeah, that's great. I'm excited about this. Let me put these in our Slack chat. Our biggest concern is just getting a batch of abstract images—no specific correlation to individual blogs. If we get that by end of week, we're happy.

**Dora Kuo:** I think we should be able to give you those by end of this week. We have an inventory of images across all languages, so it should be fine.

**William Leborgne:** Okay, super. Great.

**Dora Kuo:** Anything else?

**William Leborgne:** That's it. I'll see you in a bit.

**Dora Kuo:** Tom, thank you so much for jumping in. If you have questions, send them to me.

**William Leborgne:** I'll answer them. Sounds good.

**Dora Kuo:** Bye.

**William Leborgne:** Bye.
