# Vizcom <> GrowthX - Image Sync

<metadata>
date: 2026-01-23
time: 17:30 UTC
duration: 12 minutes
organizer: carly@growthx.ai
participants:
  - name: Katia Pembayun
    email: katia@growthx.ai
    company: GrowthX
    role: AI Designer/Image Generation Specialist
  - name: Carly Piekos
    email: carly@growthx.ai
    company: GrowthX
    role: Content Operations/Airtable Lead
  - name: Maura Kelly
    email: maura.kelly@vizcom.co
    company: Vizcom
    role: Brand Lead/Creative Director
fathom_recording_id: 116751335
fathom_url: https://fathom.video/calls/543570797
share_url: https://fathom.video/share/yyQR9to2T6xf63_J6sYx9gEzj74F5uc7
source: fathom
enriched_on: 2026-02-28 11:45 UTC
</metadata>

---

## Summary

GrowthX and Vizcom established the image production workflow for blog posts: Vizcom generates AI images with refined visual style (removing sketchy elements), delivers at 1920x1080, and Maura approves selections in Airtable; GrowthX handles resizing for all platforms and uploads to Webflow. Key alignment on brand aesthetics, sizing specs, and safety zones for cropping across different formats.

---

## Context

This meeting operationalizes the Vizcom/GrowthX partnership for AI-generated blog imagery. Katia Pembayun (GrowthX AI Designer) implemented image generation in the editorial pipeline, producing multiple 3D render options for each blog post topic. Maura Kelly (Vizcom Creative Director) reviewed initial outputs and provided critical feedback on visual style—images contained "sketchy tidbits" (decorative icons, underlines) that conflicted with GrowthX's clean, modern brand direction.

The discussion established technical requirements (1920x1080 source, platform-specific resizing), approval workflow (MEs select options in Airtable, Maura approves), and handoff points (Carly confirms Webflow upload responsibility, alt-tag generation, and safety zones for cropping).

---

## Relevance

**Content & Editorial Operations**
- Defines the visual production pipeline for blog assets—critical to publishing cadence
- Establishes approval process: MEs curate, Maura decides, ensures brand consistency

**Design & Creative**
- Brand aesthetic decision: clean, minimal 3D subjects; eliminates decorative sketchy elements
- Safety zones & cropping requirements protect composition across blog, OG, thumbnail contexts

**Product Integration**
- Links Airtable (selection), Figma (revisions), Webflow (publishing) into single workflow
- Clarifies roles: GrowthX handles resizing/upload; Vizcom delivers refined prompts

**Team Coordination**
- First cross-company workflow alignment; establishes feedback cadence and handoff points
- Addresses unknowns: alt-tag generation (Jenny), Webflow seat access (Emily), Airtable interface design (Carly)

---

## Overview

- **Visual Style:** Remove "sketchy tidbits" from images to align with the brand's clean, modern aesthetic.
- **Image Specs:** Vizcom will provide one 1920x1080 image per post; GrowthX will handle resizing for all platforms (blog, OG, thumbnail).
- **Workflow:** GrowthX MEs will select image options in Airtable for Maura's final approval; Carly will build a dedicated Airtable interface for this.
- **Ownership:** GrowthX will upload approved images to Webflow, maintaining their current content management process.

---

## Key Topics

### Visual Style Feedback

  - **Problem:** New AI-generated images include "sketchy tidbits" (e.g., icons, underlines) that conflict with the brand's clean aesthetic.
  - **Solution:** Katia will update the image generation prompts to remove these elements.
  - **New Direction:** Focus on clean, 3D subjects centered in the frame. Minimal, functional elements (like underlines) are acceptable if used sparingly.

### Image Sizing & Specs

  - **Vizcom Deliverable:** One high-res image per post (1920x1080, 16:9 ratio).
  - **GrowthX Responsibility:** Resize the single source image for all required formats:
      - Blog Image
      - Open Graph (OG) Image (e.g., 1200x630 for social)
      - Thumbnail (e.g., 1280x720)
  - **Vizcom Action:** Maura will provide "safety zones" for the 1920x1080 image to ensure key elements are not cropped on different platforms.
  - **Alt Tags:** Carly will confirm with Jenny if alt tags are auto-generated or if manual creation is needed.

### Production Workflow

  - **Image Selection:** GrowthX MEs will select a few image options in Airtable for each article.
  - **Approval:** Maura will review and approve the selections directly in Airtable.
  - **Airtable Interface:** Carly will build a dedicated interface for Maura to easily track upcoming blog posts and manage approvals.
  - **Webflow Upload:** GrowthX will upload approved images to the Webflow CMS, maintaining their current content management process.

---

## Action Items

**Katia Pembayun (GrowthX)**
- Update image guidelines: remove sketchy elements; center 3D subject; minimal underlines/circles

**Carly Piekos (GrowthX)**
- Confirm alt-tag generation w/ Jenny; report back to Maura
- Create Airtable interface for Maura; tag her in image selections
- Confirm Webflow image upload owner w/ Emily; report back to Maura

**Maura Kelly (Vizcom)**
- Send Webflow safety zones to Carly; Carly forward to Katia

---

## Transcript

**Katia Pembayun:** Hi, Carly.

**Carly Piekos:** How are you?

**Katia Pembayun:** I'm good.

**Carly Piekos:** I understand the content pipeline and things of that nature, but I'm still trying to figure out the image. So bear with me while we go. Hi, Maura. How are you? Happy Friday.

**Maura Kelly:** Good.

**Carly Piekos:** So I just wanted to take the time to go through the agentic pipeline for the visuals. Katia, you did cover images for five pieces of content. Did you want me to share my screen?

**Katia Pembayun:** I could share my screen.

**Carly Piekos:** I have it pulled up. Okay, perfect.

**Katia Pembayun:** Maura, don't know if you had any initial questions in your mind or burning thoughts, but these are some of the latest examples that we have. If you have any thoughts.

**Maura Kelly:** Yeah, I think these definitely are a big improvement and feel more like what we were seeing in the last version of Figma. So I'm just a little confused about the process. Are these all different options for the same article?

**Katia Pembayun:** Yes, exactly. We generate a bunch of different options for one specific topic. If we go to a different topic, you'll see kind of different generations. It gives you a lot of variety to choose from. The process is that our managing editors will select a few that fit best with the brand guidelines and share them back with the team. Those samples from Figma were all for one specific article, and that's basically how the whole process is. We take the topic, the generator references the topic or content of the article, then generates a variety of ideas and possible imagery.

**Maura Kelly:** Okay. I think these are still incorporating some of the sketchiness from Figma that I wasn't really resonating with. Like some of the images, the briefcase in the middle, looks like it doesn't have anything around it. I think we're leaning more towards clean visuals. I'm not sure if there's more, but I think if we could refine the visual style. That's like the only note I have—just the sketchy tidbits.

**Katia Pembayun:** Yeah, for sure. I think that's definitely something I can try to get rid of. A few of the reference images I'd been pulling from had some sketchy elements. If I just get rid of it, that should help lessen it. So we just want the 3D subject centered in the frame without anything else, right?

**Maura Kelly:** Yeah, I think so right now. Our brand is very flexible, but we're trying to define it. But it's hard to give you a good reference point. I think we're trying to stick away from sketchy elements added as icons. We don't mind underlines or circles or things like that, but it's very minimal. These renders look really good.

**Katia Pembayun:** Okay, sweet. I'm glad. The other thing is that you guys have a few different sizing requirements for these. If there are any specific sizing guidelines, I can set it up so each image gets resized differently for whatever platforms.

**Maura Kelly:** Perfect. Yeah. These are just for the blog, right? I can also check with my team if you don't know that.

**Katia Pembayun:** I'm not 100% sure the use case other than an OG image or a header image.

**Carly Piekos:** Yeah, so we want an open graph image, we need a thumbnail, and then the blog image, correct?

**Maura Kelly:** Yeah, right now all three of those are the same size. It's just one image that gets reused throughout the site.

**Carly Piekos:** Okay, so we don't need to make separate sizes? The thumbnails are usually 1280 by 720 pixels. And then the open graph, if you're doing for Facebook and LinkedIn, is usually 1200 by 630.

**Maura Kelly:** Okay. Let me check our site in the backend because I'm pretty sure it just resizes our image. We use a 16 by 9 ratio. We have different safety zones, which I still need to figure out because when we redid the site, they changed some of our ratios for blog.

**Carly Piekos:** And Katia, do you know if once the images are approved, can we create alt tags for those images?

**Katia Pembayun:** I think in the pipelines, they might have alt tags generated in them. I'm not 100% sure about that.

**Carly Piekos:** I can check with Jenny. If that's more on her end, I can check with her.

**Maura Kelly:** Yeah, it looks like Webflow just takes our main image—1920 by 1080—and reuses it. It must crop it to some degree. As long as things are centered, it will probably have a centered focus for the image. I can get you different safety areas for the image. I'll just have to look deeper.

**Carly Piekos:** Okay. If you look into that, send over the sizes and I can send them to Katia.

**Maura Kelly:** Yeah.

**Katia Pembayun:** Perfect.

**Carly Piekos:** Sounds good. So now that this is in the pipeline, what are the next steps for review? Will Maura get a selection of images with each blog post—just a few for her to pick from? Within Airtable?

**Katia Pembayun:** For most of our clients, the typical process is that we'll have the MEs—the managing editors—share a few selections in Airtable. In terms of the sketchy stuff, I'm happy to send that back in Figma if you wanted to look at it again, Maura. It should be a pretty simple tweak—just adding guidelines to not include the sketchy stuff. The managing editors will have it in Airtable, and then they can share that with the Vizcom team if they want a few selections or more revisions.

**Carly Piekos:** Does that work for you, Maura?

**Maura Kelly:** Yeah, so I should just keep an eye out on Airtable. I've never used Airtable before, but can you tag a way to see an inbox of things?

**Carly Piekos:** Yep. I will tag you in that, and I'm actually going to create an interface for you so we know which blog posts are coming up week over week.

**Maura Kelly:** Perfect. And then is that something that you guys would upload in the Webflow CMS, or would I?

**Carly Piekos:** I believe we would upload it. It really is dependent on what Emily wanted from the beginning. I will look into that and get back to you on it.

**Maura Kelly:** I think your team was definitely doing all the other content, so I would assume the image just gets uploaded when you do the content too.

**Carly Piekos:** Yeah, I would assume that would be the case, but some clients don't want that to happen—they want to approve everything immediately. But I think once you approve it, we just upload it into Webflow. Also, let me know if you had any issues with Webflow getting your seat added. Otherwise, I can remove it.

**Carly Piekos:** Yeah, I'm good. I have access to Webflow now, so we're all good to go.

**Maura Kelly:** Great.

**Katia Pembayun:** All right.

**Carly Piekos:** Thank you, Katia, for joining. I really appreciate it. Maura, thank you too for taking time out of your day.

**Katia Pembayun:** I hope you both have a wonderful weekend.

**Maura Kelly:** Thank you. Nice meeting you. Bye.
