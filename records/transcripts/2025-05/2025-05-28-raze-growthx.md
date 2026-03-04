# raze <> growthx

<metadata>
date: 2025-05-28
time: 14:03 UTC
duration: 23 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Ed Abazi (Raze)
fathom_recording_id: 65094251
fathom_url: https://fathom.video/calls/312128697
share_url: https://fathom.video/share/SztxQJ6HX4ZAeShPE7t7QeVGxdwomwwQ
source: fathom
enriched_on: 2026-03-04 18:32 UTC
</metadata>

---

## Summary

Jason and Ed aligned on the design, development, and launch strategy for GrowthX's new publication platform. The design direction was approved — featuring a distinctive color palette that moves beyond standard black-and-white, allowing featured graphics to stand out. Development will use Next.js or Astro with a custom CMS (likely Strapi or Statomic) to enable customizable post layouts similar to Sequoia's blog. The first piece of content will be a video about AI SEO and LLM tracking for brand mentions, paired with a written guide, both launching on the publication with YouTube hosting.

---

## Context

Raze is a digital agency partnering with GrowthX on a content publication project. Ed Abazi is the developer leading the technical build; Jason Gong is the GrowthX project lead. This meeting reviewed progress on the visual design (handled by a separate designer), the tech stack decisions for the platform, and the content rollout plan. The publication is intended to showcase GrowthX's expertise in AI visibility and content marketing, with the ability to gate early content for newsletter subscribers and experiment with AI-generated content (showing prompts publicly, inspired by Sequoia's "Inference" Substack).

---

## Relevance

- **To GrowthX Delivery:** The publication model could be a replicable service offering (Colin is exploring selling similar "publication as a service" packages to clients). Visual differentiation through custom design and layout customization (per-post placement of text/graphics) is a key selling point vs. standard Substack.

- **To CheckThat:** The first content piece focuses on AI SEO and LLM tracking — directly aligned with CheckThat's core value prop. This is an ideal proving ground for AI-generated content experiments (showing prompts, process transparency).

- **To GrowthX Business Development:** Raze/Ed's involvement signals capacity and specialization in publication/CMS platforms. Visual approval from the team shows momentum. Ed still needs GrowthX Slack/email access, which Jason is handling.

---

## Overview

- Design direction for the publication is progressing well, with a distinctive (non-standard) color palette and layout approved
- Development will use Next.js or Astro, with a custom CMS (Strapi or Statomic) to support per-post layout customization similar to Sequoia's blog
- Content strategy includes articles, videos, and AI-generated content with visible prompts shown to readers
- First video and article are coming soon: a chat with AI SEO experts on LLM tracking for brand mentions, paired with a written companion guide
- Videos will be hosted on YouTube and embedded in blog posts for better tracking and presentation
- Publication will support gated content features (e.g., latest article behind newsletter subscription for first week)

---

## Key Topics

### Design Direction & Approval

- Webflow templates for graphics have been sent to the design team
- Design direction approved: distinctive color palette (not standard black/white) that lets article graphics visually stand out
- Inspired by Sequoia's blog aesthetic, with per-post customizable text placement on listing/index pages
- Goal is visual differentiation while keeping content the primary focus
- Design is "old school" feeling, heavy use of color — signals not just another generic publishing platform

### Development & Tech Stack

- Ed recommends Next.js or Astro (Next.js is overkill for a publication but works; Astro is a better fit)
- Custom CMS is essential to support per-post layout customization (text placement, image positioning, styling)
- Top CMS contenders: Statomic (Ed has prior experience) or Strapi (GrowthX is a Strapi customer; could test their headless CMS offering)
- Will include gated content: latest article behind newsletter subscription for the first week, then unlocked
- Sequoia's blog has interactive components (grids, large mid-post images) — GrowthX can build similar customization

### Content & Launch Plan

- First piece is a video: panel discussion with AI SEO experts on LLM tracking and brand mentions
- Companion written guide will dive deeper into the concepts covered in the video
- Videos hosted on YouTube (better tracking, easier embedding, cleaner presentation)
- Considering AI-generated content as an article format, with visible prompts shown to readers (inspired by Sequoia's "Inference" Substack experiment)
- Publication will support both text and video content types

### Branding & Naming

- Publication name leaning toward "Yelp" (Jason still exploring other options)
- Jason will discuss branding direction and design feedback with Ren, share alignment loom/video with team
- Design should be ready for launch in initial form; can iterate post-launch

---

## Action Items

**Jason Gong (GrowthX)**
- Review Webflow templates sent by Ed for graphics
- Talk to Ren about branding direction; send Zoom or loom video to align team on publication design
- Provide a sample post to Ed for page layout design reference
- Ping team to provision Ed's access to GrowthX email and Slack
- Send chat message with Ren's feedback on publication design to team

**Ed Abazi (Raze)**
- Start scaffolding the publication platform
- Explore Strapi as a potential CMS option (or test as a headless CMS), Statomic as alternative
- Review documentation for Strapi's headless CMS use case; provide feedback notes if undocumented

---

## Transcript

**Jason Gong:** Hey, can you hear me?

**Ed Abazi:** Yeah, yeah, I can.

**Ed Abazi:** Are we in the office?

**Jason Gong:** Yes. We're doing a bunch of filming back here, or at least a plan. I like the whole studio you made there.

**Ed Abazi:** Cool.

**Jason Gong:** Anyway, how is it going? I know we haven't queued up a bunch of stuff recently. I haven't had a ton of time.

**Ed Abazi:** Yeah, of course.

**Ed Abazi:** We sent the Webflow stuff. I don't know if you got a chance to see that.

**Jason Gong:** Which one's that?

**Ed Abazi:** The templates for the graphics and everything.

**Jason Gong:** Oh, for Webflow — okay. Not actually. Yeah, that would be helpful, because we're meeting with them today.

**Jason Gong:** Right. They looked at that design.

**Jason Gong:** I feel like they're all kind of roughly in agreement, but the main person who owns that is in his first week or second week at this point, and he needs to align people on his side to figure out how to even get that on the website. We'll just have to wait it out. I'll look at the Webflow stuff and flip this by them.

**Jason Gong:** I haven't looked at their blog. Do they do stuff like this already?

**Ed Abazi:** Something similar with those glowy types of things. That's what they use on the blog. I've seen it — their YouTube videos come up as well, and that's basically their design language for this kind of creative.

**Jason Gong:** Makes sense. Great.

**Jason Gong:** I think the main thing to talk about is the output and execution. I tried looping Colin in because I know he's in the middle of selling to a bunch of companies, and similar to what we did with Webflow, there's a way for us to support him since we have capacity here. But he hasn't said anything yet.

**Jason Gong:** So maybe look out for that. I know there are some customers where, in the pitch, we're doing the same thing as we're doing for Webflow — we say, "Hey, we're going to help you create a publication." And I think just visually seeing it is a great unlock. Let's see if he says anything. He'll be on in a few hours.

**Jason Gong:** How I've been thinking about this is there's a design thread and a development thread. Is that how you guys work, or do people flex in either direction?

**Ed Abazi:** The designer handles strictly design — all the creative stuff. I can help from time to time with my skills, but I do most of the coding. Once we have an agreement on what we're going to continue with, I'm probably going to start coding the output immediately.

**Ed Abazi:** In terms of the technical side of things, do we have some kind of preferences? Or do we want a very simple publishing platform?

**Jason Gong:** That's a good question. I'm trying to think of capabilities.

**Jason Gong:** Are there out-of-the-box things? I know everyone tries to use Substack, but in terms of creating our own property, is there a CMS behind all that, or is it special?

**Ed Abazi:** Having a CMS helps, definitely. In terms of the tech stack itself, we can go with Next.js or Astro. Next.js is a bit overkill for this kind of thing — it's meant for apps — but it can also work for a publication of this type. We'll see. Once we get to that point, I've been doing some research, just clearing my mind to get clarity on how to approach this. I'll figure something out.

**Jason Gong:** From your end, you don't have any kind of specific preference?

**Ed Abazi:** No, there's nothing specific.

**Jason Gong:** I've been looking at a lot of these kinds of publications, and they all bias very hard toward simplicity. Like, the number I've seen on Substack makes me almost think, do we just need a nice logo and throw it on Substack? I've considered that a bunch. Maybe one day we end up doing that. But right now, there's kind of an idea that I think we'll stand out more doing our own thing.

**Ed Abazi:** Because you're kind of limited on Substack. I do want it to stand out.

**Jason Gong:** Yeah.

**Jason Gong:** I'm talking to Ren in a bit to think through branding. I want it to stand out. I want the content to be the focus.

**Ed Abazi:** When you said you want to stick with "Yelp," did you mean the name or design-wise?

**Jason Gong:** The naming. I thought about a bunch of other options, but I couldn't think of anything better. Yelp was something really good.

**Ed Abazi:** Did you see the name options we sent a couple of days ago?

**Jason Gong:** I saw the exploration yesterday. I'll talk to Ren and send a Zoom video, but for me, the skeleton everything's on should be very minimal. Every article should be where your eyes go — where the life is in the website.

**Jason Gong:** In terms of how to set it up, we want a website that could support some interactive features. It might be overkill — I'm still thinking about it — but the New York Times-style scrolling behavior would probably be the ceiling for how much fancy interactive stuff we want.

**Ed Abazi:** I think it depends on the content we want to publish. Should we do something like gated content?

**Jason Gong:** I think we probably should, yeah.

**Ed Abazi:** Maybe we could publish an article just for subscribers for the first week, then unlock it afterward?

**Jason Gong:** Yeah, that would be interesting. Like, the latest article is just, "Hey, you've got to subscribe to our newsletter."

**Ed Abazi:** Yeah, that would be really nice.

**Jason Gong:** I imagine that's why people go with Substack if they don't have a development team — it's all baked in.

**Ed Abazi:** I haven't used Substack as a publisher, so I don't know what customization possibilities they have. I'm guessing it's not that much.

**Jason Gong:** Yeah, I haven't looked at it either.

**Ed Abazi:** If we want to do something like Sequoia, where they have a huge image in the middle of a post or interactive grids with images, those are all components we can build ourselves. Substack would give us a hard time with that kind of customization.

**Jason Gong:** Sequoia also has a Substack called "Inference" where they use AI to summarize their videos. They even say it's an experiment in using AI. What they're doing is not great, but they show their prompts, which is kind of interesting. They probably want to do it because other people will ask us to do the same.

**Ed Abazi:** That's very interesting. I love the idea of showing the prompts.

**Jason Gong:** Yeah, so I think for us, we can even consider some of our articles being like that. It's like, "Hey, this article is generated," and you hover over it to see the prompts and workflow. I love that idea. I'm trying to give you as much as possible to start building. We'll have our first article soon, and then our first video, which we'll probably repurpose into an article.

**Ed Abazi:** How do we want to present a video in the blog?

**Jason Gong:** I don't know. All I've seen is people embedding it. Do you think there's a nicer way?

**Ed Abazi:** I think it should live under its own URL, like its own post.

**Ed Abazi:** Embedding is the default. Do we write an article behind the video, or just put it out there?

**Jason Gong:** I think we should have both. The video will be a chat with people working on AI SEO and LLM tracking for brand mentions. Then we'll have a companion guide that goes deeper into the concepts.

**Ed Abazi:** That would be the perfect pairing. Will it be uploaded on YouTube or embedded directly?

**Jason Gong:** It'll be on YouTube.

**Ed Abazi:** That makes more sense and will be much easier to present in the blog.

**Ed Abazi:** We can just embed the YouTube video and track the views. That's what Ren did on Figma recently.

**Jason Gong:** I had some notes and Ren also put some notes in.

**Ed Abazi:** Let's see what Ren said.

**Jason Gong:** Cool, yeah.

**Jason Gong:** This looks good to me. Pretty good.

**Ed Abazi:** It doesn't look like other websites. The colors are quite heavy — that's what gauges your interest. It's not just another black-on-white or white-on-black website. This color palette allows the graphics behind the articles to breathe.

**Jason Gong:** Yeah, I like it.

**Ed Abazi:** We can try different branding, but this gives it an old-school feeling. We should screenshot and show folks in the channel.

**Jason Gong:** This is really good. I think you can even start on the scaffolding behind this.

**Jason Gong:** I'll make sure Ren gets a loom video today so we're all aligned. If we had this, I'd be really happy as the first version we throw out there.

**Ed Abazi:** One thing on Sequoia's blog — on the listing page, some text is placed in the middle, some at the bottom, some at the top right, depending on the graphic. I'm thinking about how to make that customizable from the CMS. It's doable, but there's a line between "just write the title and post" and "full customizability." I'm probably going to build full customizability with some sensible defaults, so people don't have to do too much just to post an article.

**Ed Abazi:** Yeah, I'm going to start playing with this very soon.

**Jason Gong:** What are these types? I guess they use different categories like "Spotlight" and "Perspective" — so that's how they decide the structure. Some have background images, some don't. It's interesting.

**Ed Abazi:** Yeah, they all use the same basic structure.

**Ed Abazi:** The article image at the top is different for almost every post. Some have it, some don't. It's customizable per post.

**Jason Gong:** This one's totally different — they removed the lines and added images, with a different font for the title. I don't hate it. That's the kind of customization we want.

**Ed Abazi:** It's crazy customizable between each post. It's close enough to Sequoia for it to be interesting and interactive, but far enough to not look like a copy.

**Ed Abazi:** I might end up using a CMS called Statomic. I've worked with it before — it's really good. I'll give it some thought.

**Jason Gong:** Yeah, let me know what CMS to pick.

**Jason Gong:** We've already used Strapi on the main sites, but we're not obligated to use them just because they're a customer. They keep saying they can use their platform as a headless CMS. I wonder if we just try and see what happens. But I don't want to make your life hard.

**Ed Abazi:** I can give it a try. Do they have documentation for that use case?

**Jason Gong:** They probably don't have documentation framing it as a headless CMS use case. But if you poke around and give me feedback notes, it would be a fun exercise for them.

**Ed Abazi:** I could do it in Webflow, but I think that would mess up our idea of per-post customizability.

**Jason Gong:** Yeah. I'll chat with Ren, but I think this is directionally really good. Can you guys think about what a page might look like?

**Jason Gong:** And I can give you guys a sample post to use as a reference.

**Ed Abazi:** It's crazy how Substack is basically Medium — just a blogging platform.

**Jason Gong:** Yeah. I'll pull a sample post for you.

**Jason Gong:** You're still waiting on access for the GrowthX email and Slack, right?

**Ed Abazi:** No, I didn't get it yet.

**Jason Gong:** I'll ping the team.

**Ed Abazi:** Yeah, just email and Slack access.

**Jason Gong:** That'll be good — then I can start inviting you to channels where we do other work.

**Ed Abazi:** Okay, sounds good.

**Jason Gong:** I'll send you a message once I touch base with Ren, but feel free to start scaffolding everything.

**Ed Abazi:** Okay, definitely.

**Jason Gong:** All right, thanks, Ed. See you.

**Ed Abazi:** See you. Bye.
