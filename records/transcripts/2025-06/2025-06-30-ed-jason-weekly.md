# Ed <> Jason Weekly

<metadata>
date: 2025-06-30
time: 15:40 UTC
duration: 16 minutes
organizer: Jason Gong (GrowthX)
participants: Edin Abazi (Raze Growth), Jason Gong (GrowthX)
fathom_recording_id: 71287576
fathom_url: https://fathom.video/calls/339169865
share_url: https://fathom.video/share/De8zy6fR9wy3x5y6Xg-btfsS6nnTxebC
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

Jason and Edin aligned on a minimalist V1 website launch for tomorrow (July 1) using either a Framer prototype or Edin's Next.js implementation. The core challenge is finalizing content and design from Marcel and Renan—the team decided Edin should proceed building scrollable sections in Next.js with different backgrounds per slide while Jason threads the conversation with Renan about the Framer vs. Next.js decision. They'll reconvene after Marcel becomes available to lock in copy and design details.

---

## Context

Edin is a developer from Raze Growth working with Jason Gong at GrowthX on a website launch scheduled for July 1. This appears to be a client project where GrowthX is delivering web development services. The team is balancing speed-to-launch (tomorrow) against design polish and content completeness. Marcel (seemingly a GrowthX lead or product person) is handling content and design direction, and Renan (likely another designer/developer) has built a Framer prototype. The conversation reveals cross-functional confusion about which tool to use (Framer vs. Next.js) and missing content from Marcel that's blocking progress on later sections.

---

## Relevance

- **To GrowthX Delivery:** Fast-tracked website launch requiring trade-offs between tool choice (Framer vs. Next.js) and design refinement. Edin's Next.js version offers better mobile responsiveness than the Framer prototype. Clear design pattern emerging: minimalist, high-polish, scrollable sections with fading graphics and animated text—similar to high-end SaaS landing pages.

- **To GrowthX Business Development:** Client is a high-value data/ML company (appears to work with customers spending hundreds of millions annually). V1 launch tomorrow, V2 will add blog with deep-dive content on data labeling, model training, and quality benchmarking. Future V3 hands off pattern to client for self-service. Indicates potential for expanded content services post-launch.

---

## Overview

- Launch planned for tomorrow (2025-07-01) with a minimalist V1 design, expanding to V2 with rich content later
- Confusion exists between Framer prototype and Next.js implementation; decision needed on which to use
- Content and design specifics still pending from Marcel and Renan; Ed to proceed with building scrollable sections

---

## Key Topics

### Website Version Strategy

  - V1: Minimalist design, similar to Framer prototype but with more slides and polish
  - V2: Addition of blog and rich content (e.g., data labeling, model training, quality benchmarking)
  - V3: Potential handoff to client for further development

### Design and Content Status

  - Figma designs available, particularly page 3 as a reference for desired look
  - Framer prototype exists but may have limitations (e.g., mobile responsiveness)
  - Final logo and branding elements not yet confirmed
  - Content for sections still pending from Marcel

### Technical Implementation

  - Ed has coded a layout with closable sidebar, similar to OpenAI's design
  - Decision needed: proceed with Ed's Next.js version or use Renan's Framer prototype
  - Key features to implement:
      - Scrollable sections with fading graphics
      - Different backgrounds per section
      - Smooth text animations and transitions

### Client Requirements

  - Emphasis on high-quality, minimalist design (clear typography, no rounded corners)
  - Mobile-friendly implementation crucial
  - Future need for interactive displays to explain complex concepts

---

## Action Items

- **Edin Abazi (Raze Growth):** Continue building out sections in Next.js with scrollable layout, different backgrounds per slide, fading graphics, and text animations—focused on mobile responsiveness and slide-like feel. Plan to publish preview version for comparison.
- **Jason Gong (GrowthX):** Start a thread with Renan to decide between Framer prototype and Next.js implementation; confirm that Page 3 of Figma is the design reference.
- **Jason Gong (GrowthX):** Follow up with Marcel when available (expected within ~1 hour) to finalize copy, headline/paragraph content, and design decisions for launch.
- **Team:** Reconvene in approximately one hour to review Edin's built version and compare against Framer prototype before tomorrow's launch.

---

## Transcript

**Jason Gong:** Oh, wait, I don't hear you, one sec.

**Jason Gong:** Oh, here we go.

**Edin Abazi:** Yeah, I can hear you now.

**Jason Gong:** How it goes?

**Edin Abazi:** Good. A little lost on everything.

**Jason Gong:** Is Renan, are you, like, driving there? Do you need me to help him block anything?

**Edin Abazi:** Well, we're, Renan's designing something, but we asked him for some ideas around what the content's gonna look like, and he doesn't know either. So we're a little stuck on moving forward with the rest of the sections and the pages.

**Jason Gong:** Okay, let me take a look at that.

**Edin Abazi:** So we're going live with this tomorrow, like code and everything.

**Jason Gong:** Yeah.

**Edin Abazi:** And how many pages are there?

**Jason Gong:** I guess it depends how that's defined. I mean, the thing that Renan sent is kind of pretty close.

**Edin Abazi:** I think there was the homepage, if I'm not mistaken.

**Jason Gong:** Yeah, think the homepage. But it kind of is just that—just that one page with a few more words, then maybe that scrolls down, like new picture, new set of words, maybe a new background, and that's it.

**Edin Abazi:** That's the whole thing? Oh, we're not doing the blog and everything?

**Jason Gong:** We don't need any of that for V1.

**Edin Abazi:** Well, theoretically, do we need the sidebar, then, if we don't have any other pages?

**Jason Gong:** Well, they will have careers and contact. Whatever runs that is already pretty polished.

**Edin Abazi:** Do you have Figma open?

**Jason Gong:** Let me open that real quick. I do have it open, but is there a link I'm looking for?

**Edin Abazi:** Do we have the logo and everything finalized in terms of branding?

**Jason Gong:** Renan hasn't talked to you at all? Because I feel like Renan's the one that's driving there, so I'm kind of out of the loop.

**Edin Abazi:** We're going to ask him a couple of questions today, but no, we didn't really talk to him too much.

**Jason Gong:** Okay, got it. Somebody needs to drive. I feel like Marcel's in those contexts, but he obviously doesn't have time right now. Do you think we're running built in Framer—if our goal is just to have exactly what he has but a few more slides and maybe a transition as you scroll through them—is that the best path? Or should we still try to build something in Next.js?

**Edin Abazi:** I mean, if we have the final design, building it out in code is going to take too long. It's just about knowing exactly what we're doing. I did start—I basically coded the layout with the sidebar, like closable, basically a copy of OpenAI.

**Jason Gong:** Yep.

**Edin Abazi:** So in code, I just have to go through the sections and add them in.

**Jason Gong:** I feel like what's in Framer honestly is pretty good. Let me see how that looks. Do you know what the "7 out of 7" means in the button?

**Edin Abazi:** No, what is that?

**Jason Gong:** Oh, that's just the date we have the announcement. We're doing a lot of production in the office to do a video. So I think what we're trying to go live with here is just almost what's in the Framer, except with more copy and as many cool little designs that have high polish as we can get.

**Edin Abazi:** Yeah. But in order to form the rest of the sections, we need the content.

**Jason Gong:** Right. Marcel is kind of the most sensitive to design polish. Honestly, I need to get Marcel to pull the content together. He did mention last night that he was going to send it over in the morning, but he didn't. Yeah, if you look at page three in the Figma, it's kind of an idea of what he wanted to go for. I guess we "choose silence or spectacle"—there's supposed to be multiple versions of that.

**Edin Abazi:** There's basically just different slides that you scroll through.

**Jason Gong:** Exactly. Would you be able to build that?

**Edin Abazi:** Yeah, yeah, yeah.

**Jason Gong:** Just get that vibe—where the copy can be changed. The main thing that matters is these tiny polish details: how the text fades in, how the animations feel. As long as you have that skeleton for animations and text, that will probably get us 90% of the way there. Once Marcel's out of his meeting, I can grab him and finalize the copy.

**Edin Abazi:** So I'll focus on creating this logic where we have different sections to scroll through, with the graphic fading in and out depending on the section, then the headline and paragraph.

**Jason Gong:** It seems like we have built it in Framer, and I'm not sure if it runs on the same page or if you're duplicating stuff. Have you seen Renan's Framer?

**Edin Abazi:** No, I haven't seen anything.

**Jason Gong:** Okay, let me send it to you—he actually built this. Has Renan talked to you at all today?

**Edin Abazi:** Just a couple of messages back and forth in terms of design. He was like, no, we want to keep it minimal—clear typography, no rounded corners.

**Jason Gong:** I feel like there's cross-wires here where different folks were both working on the same thing. So, do you think just using Renan's would be more effective? I know you've already started, and we'll probably use yours in the next version.

**Edin Abazi:** Honestly, it's up to you. Either way, I'm okay with it.

**Jason Gong:** Let me start a thread right now. I think Marcel's busy for the next hour, but once he's done, we can keep going. I know it's the end of your day too, so I'm really sorry. But to keep going with what you have—add more slides—I think that would be the thing to do. And as far as the design goes, that's where Renan should be making a decision. But I think the best reference for what we want is page three in the Figma.

**Edin Abazi:** I'll build out these sections, and then based on that, we can make a decision. If we want to go the Framer route or whatever, I think it's going to look about the same. My version is probably going to be more mobile-friendly because the Framer one isn't right now.

**Jason Gong:** Okay, that's great. And if you could map it to what Marcel has even a little bit—the main thing is the background. I think that had the right feeling he wanted to create. Each slide should have a different background.

**Edin Abazi:** Yeah, so it should feel like a slide. I'll continue building it out and then publish a version somewhere for a preview. We can look at both versions and see which one we want to go with. I can stay on a little later today—it doesn't matter. I just want to make sure we do this right. And then if we're expanding into V2 with more content and pages, it's probably best to continue with the Next.js version.

**Jason Gong:** I think that makes sense. The main thing for V2 will be a blog. They're taking complicated concepts around training models and making it accessible to decision makers. Having interactive displays to explain those concepts is probably the key thing there.

**Jason Gong:** Give me probably an hour, and then we'll sync up again.

**Edin Abazi:** Okay, sounds good.

**Jason Gong:** All right, cool. Appreciate that. We'll talk to you soon. See ya.
