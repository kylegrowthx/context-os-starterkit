# Impromptu Google Meet Meeting

<metadata>
date: 2025-05-13
time: 09:41 UTC
duration: 15 minutes
organizer: renato@growthx.ai
participants: Renato Valdes Olmos (GrowthX), Ed Abazi (external)
fathom_recording_id: 62217134
fathom_url: https://fathom.video/calls/299670425
share_url: https://fathom.video/share/SssWBsEMtxMGLoDpZAUsP2w74MiuASGt
source: fathom
enriched_on: 2026-03-03 02:15 UTC
</metadata>

---

## Summary

Renato Valdes Olmos (recently joined GrowthX as Design Lead) and Ed Abazi (design-focused developer) discussed the Series A announcement project, including blog layout redesign and graphics production. GrowthX is transitioning the blog to a two-column layout inspired by Sequoia Capital's design, and needs two main graphics: a fundraise hero image and a bento-style social media graphic highlighting the $12M Series A round, Madrona as lead investor, and founder photos. Ed will handle the technical implementation and graphics production while Renato will curate and approve founder photos for public use, with real-time feedback via Figma.

---

## Context

Renato Valdes Olmos recently joined GrowthX's design team about two to three weeks before this call, bringing 20+ years of tech experience as a designer, founder, and executive. He's now leading design efforts across GrowthX while building out an internal design team. Ed Abazi is a design-capable developer with 10+ years of SaaS experience who works closely with his co-founder (Jason) in a 360 m² office space with a team of 10 people. The two are meeting to coordinate on GrowthX's Series A funding announcement, which requires both design work and technical blog implementation. This is an early sync to establish the scope, timeline, and handoff process for the announcement graphics and blog redesign.

---

## Relevance

- **To GrowthX Delivery:** Renato is a new design hire establishing GrowthX's in-house design capabilities. This meeting shows early collaboration between design leadership and external technical partners, suggesting a hybrid model. Blog redesign and announcement graphics are foundational brand assets for Series A positioning.

- **To GrowthX Business Development:** Series A announcement is a critical milestone for customer credibility and market positioning. The $12M round with Madrona as lead investor is a strong signal to prospects. The multi-channel graphics strategy (hero + bento) maximizes social reach and press coverage.

- **To Execution:** Technical debt in Strapi setup needs cleanup before the announcement goes live. Featured image integration and blog post image handling require Ed's attention today to avoid blocking the announcement. Real-time feedback loop via Figma between Renato and Ed will keep iteration cycles tight.

---

## Overview

- Two main graphics needed: 1) Series A hero image, 2) Bento-style graphic with key info
- Blog layout updated to two-column style, similar to Sequoia Capital's blog
- Ed to work on integrating newsletter into blog and make technical changes
- Renato to provide approved founder photos and real-time feedback via Figma

---

## Key Topics

### Team Introduction and Background

- Ed: Developer with design skills, 10+ years SaaS experience
- Ed's co-founder (Jason): Creative powerhouse
- Working together for 6-7 years, best friends
- Team of 10 people in 360m² office space
- Renato: Recently joined GrowthX (2-3 weeks ago), 20+ years in tech
- Renato's role: Leading design, contributing and assembling team

### Blog Layout Updates

- Changed to two-column layout with square images and text on top
- Inspired by Sequoia Capital's blog design
- Content page updated with centered post layout
- Current typeface not ideal for long-form reading
- Ed made fixes to the blog, but it's currently empty (only one post)

### Series A Announcement Graphics

- Blog feature image needed
- Fundraise hero image: Similar to provided example
- Bento-style graphic for social media sharing
  - Key info: $12M Series A round, Madrona (lead investor), other notable investors
  - Founder photos (separate or combined)
  - Product system representation

### Technical Considerations

- Ed to work on integrating newsletter into the blog
- Need to address messy Strapi setup from previous agency
- Figuring out how to handle featured images and in-blog images

### Brand Consistency

- Graphics should align with GrowthX brand
- Emphasis on minimal and simplistic design
- Flexibility to tweak brand components as needed

---

## Action Items

**Ed Abazi (external)**
- Create blog post cover img for Series A announcement
- Integrate newsletter into blog
- Create fundraise hero img for Series A blog post
- Design bento-style graphic w/ key info from Series A announcement
- Modify Strapi setup for featured img & blog post imgs

**Renato Valdes Olmos (GrowthX)**
- Select & approve founder photos for public use in blog post
- Share Figma file w/ approved photos for real-time feedback

---

## Transcript

**Renato Valdes Olmos:** Okay, I have never been. How's it up there?

**Ed Abazi:** It's hectic, but fun.

**Renato Valdes Olmos:** I'm actually about 30 minutes north from Amsterdam. So we're in the countryside. Once we had kids, we decided to take balance. Before that, we were in San Francisco for a long time. And before that, I was in Amsterdam, too. But yeah, back in Europe, so good to be at least in the same time zone.

**Ed Abazi:** Oh, yeah, for sure.

**Renato Valdes Olmos:** Tell me a little about yourself.

**Ed Abazi:** Well, I'm a little bit of a designer. I'm mostly a developer. I don't know if Jason, like both my co-founder and I are in this together. He's the creative powerhouse. I've been building stuff for SaaS companies for the past 10 years, probably more than 10 years, almost. Yeah, I just like building stuff. I just like building websites. I like seeing brands come to life, like well-built, well-designed brands, and being able to convey that in a way that sells, because at the end of the day, you have to sell, right?

**Renato Valdes Olmos:** How long have you been doing it together?

**Ed Abazi:** We're almost like six, seven years together, yeah, and we're best friends in real life as well.

**Renato Valdes Olmos:** So work's well, so work feels like play.

**Ed Abazi:** Oh, yeah, yeah, for sure. And because we sit next to each other, he's over there right now. As he's designing, like if we know what we're going to do, I just start developing it. And we don't waste time with going back and forth. And we can make changes directly in code because we're in each other's worlds, basically.

**Renato Valdes Olmos:** You got a little studio space there, too?

**Ed Abazi:** We do have quite a big office here. We're kind of expanding slowly. We have like 360 meters squared.

**Renato Valdes Olmos:** Just for the two of you.

**Ed Abazi:** Well, not just the two of us. Like, we have some other things going on here. We're like 10 people over here.

**Renato Valdes Olmos:** Cool. All right, man. Yeah, very cool. Yeah, I just started working with GrowthX just, I don't know, it's like two or three weeks ago. I have been in tech for, well over two decades now. Started out as a designer, became a founder, then was an exec for a while for some of the larger tech companies. And now back in the game, leading design, both contributing and assembling a team for GrowthX internally as well. So, yeah, just like diving in and getting a full purview of everything that we're doing. We're doing quite a broad range of design work across the company, which is a lot of fun. There's multiple design disciplines that get to contribute, and everything is rooted in engineering, which is really awesome. I'm sure you could appreciate that, too. So, yeah, we're working on the Series A announcement now. I don't know how much you've been working on that with Jason already.

**Ed Abazi:** On the announcements, specifically not that much. I know he asked me to make some changes on the blog, which I did. I guess we just need to prepare a cover post for the blog post.

**Renato Valdes Olmos:** Yeah, it's a couple of images that we're thinking about, and we'll help you out with some of that or some real-time feedback as we go along. Do you have cycles today to work on that?

**Ed Abazi:** Yeah. I'm going to work on integrating the newsletter in the blog.

**Renato Valdes Olmos:** Got it, got it.

**Ed Abazi:** I did make some changes. I don't know if you've seen the current blog. So if you go on the current blog, it's a little messy. I mean, it's empty. There's only one post right now. But I did make some fixes. Jason asked me to change the layout to look more like Sequoia Capital's blog. I don't know if you've seen that one. It's basically a two column layout with square images with the text on top.

**Renato Valdes Olmos:** Yeah, yeah. Yeah.

**Ed Abazi:** And he asked me to change the content page. This cover doesn't work with this layout. I just created a basic one just to go more with this layout for the old blog. And I'm guessing we're going to design the new one with this logic. So basically, the bottom left and the top right side, there shouldn't be any overlapping content within it. And then inside the post, it's a little cut off on the sides. And then the post itself, with Jason's direction, I made it centered in the middle, easier to read. I'm not a huge fan of this typeface. It's not very natural in terms of longer reading. But I just kept it for now, and then if we ever rebrand, we'd probably want to pick a better font.

**Renato Valdes Olmos:** I think that's all right for now. Then on the, aside from this, any updates?

**Ed Abazi:** Regarding the blog, no.

**Renato Valdes Olmos:** Got it, got it. Yeah, the images that we're going to have to create will live within the context of the blog, of course. And it's a couple that we want to get done. So let me walk you through this.

**Ed Abazi:** I'll be right back. One second.

**Renato Valdes Olmos:** All right. So they're working on the content for the blog post right here. I'll share this with you as well, which is still in progress, as you can see. There's still a bunch of things that need to be set on the top end. We need the blog feature image. I think it could be slightly different. We're going to be using a system within the grid of the index page. So it would be nice if there would be some consistency between the image styles already. So I would consider that a separate thing, probably. But for the blog feature image, I want to try a couple of variations. First off, a fundraise hero image. Of course, something along the lines of this. I'll send this over to you as well. I'll paste everything in the message afterwards. This would be one variation, I think. Another potential variation could be, since this is probably the graphic that would be shared most across social media as well, is to do with a bento-style graphic over here that takes bits and pieces of the most salient information from the post and perhaps puts that in a little block, so lead investor, perhaps a bit of the product, or the overall system architecture, the amount of funding raised, the founders there. Potentially something like that. But let's see. This is the overall information, other notable investors. I still need to select a picture and also needs to get onto the blog. But these are a ton that they've provided. I'll go ahead and select one of Marcel, one of Daniel, and one of them together and approve those for public use. So you can spend time on creating the actual graphics, which is the highest priority. Let's see. Just to give you an example of how they want that set up. It's pretty much something like that, right? Like a call out of probably both of them and maybe like a little accompanying text. Yeah. A team shot. Right. So just add humanity to the post. Any other graphic? I think if we have the main graphics or a graphic with just like the big Series A call out and perhaps a bento that talks a little bit or that grabs some of the information from the actual post are in a really good spot. So if you could prioritize those two, that would be absolutely fantastic.

**Ed Abazi:** So what are you imagining exactly within the bento? Like the value?

**Renato Valdes Olmos:** Yeah, let's go in here. Within the bento, I would say it's like at the very least we put it's like a big call out of the 12 million Series A round, then another component could be Madrona lead. Then another little component could be other notable folks. And we perhaps have a range or a selection of people there. Another block within the Bento could be either each founder separately as a little block within the Bento or one of them combined. It's like depending on the amount of space that we have. And then the last block, I think, should talk a little bit about the interaction of the products within the system. Now, the products are described over here. So it would be like a little representation of that, perhaps a little abstracted graphic. I will think a bit about this. It would be super helpful if y'all could share a Figma file or something, I can drop photos in there, the approved photos as well, and provide feedback real-time if necessary. I'll be online this afternoon. But I'll share this. I'll get this over to you ASAP.

**Ed Abazi:** Yeah, can you share the notes from this call as well?

**Renato Valdes Olmos:** Yeah, for sure. Absolutely.

**Ed Abazi:** We'll work on this throughout the day. I'm probably going to have to make some changes on the technical side of things for the blog because the way Strapi was set up previously by the previous agency is kind of messy. I need to figure out the way, like, how we're going to handle the featured image and the images within the blog itself. Yeah, I'll make those changes as well today.

**Renato Valdes Olmos:** Awesome. Yeah, if anything or any questions around, you know, like design specifically or how to translate any of the information in the press release, feel free to just send me a DM and I'll react as soon as possible.

**Ed Abazi:** In terms of style, we're sticking to the GrowthX brand, right?

**Renato Valdes Olmos:** Yeah, yeah, yeah. I would say just keep it as much inline as possible and feel free to keep it even a bit more minimal, a bit more simplistic. This is just the first draft based on the actual information that we have and then we can tweak some of the brand components a little bit further where necessary. But it's all supportive to the blog post. Yeah, sounds good. Awesome. All right, man. Thanks so much.

**Ed Abazi:** Thank you.

**Renato Valdes Olmos:** All right. Have a good one. Cheers. Bye.
