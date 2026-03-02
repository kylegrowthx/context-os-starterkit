# 35/GrowthX checkin

<metadata>
date: 2025-10-29
time: 13:03 UTC
duration: 16 minutes
organizer: Renato Valdes Olmos (GrowthX)
participants: Renato Valdes Olmos (GrowthX), Frank Slangen (35), Sem Stassen (35), Pascal (35)
fathom_recording_id: 97617296
fathom_url: https://fathom.video/calls/457769645
share_url: https://fathom.video/share/7gyYAZKuvw-yS9eCURWuYRTqoBQZmGGH
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

GrowthX and 35 aligned on a composable Sanity CMS architecture for the redesigned growthx.ai website, solving the current bottleneck where hardcoded pages require developer involvement for marketing updates. The plan: 35 owns the full Sanity setup and frontend build while GrowthX provides design direction and analytics requirements; mobile layouts will be designed in parallel with backend work. Frank will deliver a project proposal with hours and timeline by end of week.

---

## Context

GrowthX is working with 35, a digital agency in Maastricht, Netherlands, to redesign and rebuild growthx.ai. The site is currently fully hardcoded (frontend built without a CMS), with only the blog running on Strapi and a separate Edge blog on Sanity. This hardcoded approach creates friction: non-technical marketing staff cannot publish new pages or update content without developer help, and launching a new page takes days instead of hours. GrowthX's goal is to enable marketing to launch new pages in under one day through a composable architecture where designs are broken into reusable blocks. 35 has experience with Sanity across other projects and is proposing that approach, though GrowthX explored alternatives like Framer.

---

## Relevance

**To GrowthX Delivery:**
- Website redesign is core to marketing's ability to ship content. Moving from hardcoded pages to a composable CMS directly improves delivery velocity for GrowthX's own content marketing.
- Sanity schema and frontend templates must support reusable block-based composition so Ed and non-technical staff can build pages without developer help.
- Analytics migration (PostHog, Google Analytics, custom GTM tags) is critical — all existing tracking must carry forward to maintain data continuity.

**To GrowthX Business Development:**
- Ed is the primary GrowthX contact for implementation and design decisions. Shared Slack channel (Frank, Sam, Pascal, Renato, Ed) reduces communication friction and keeps iteration fast.
- Timeline is "as soon as possible" with no hard deadline, giving 35 flexibility to balance this with other work.
- Future expansion: Renato flagged a follow-on project to build a custom meeting-booking experience to replace the current Default form integration.

**To CheckThat:**
- No direct mention, but the redesigned site will be a high-quality reference for GrowthX's own AI visibility and composable design practices.

---

## Overview

- **Problem:** The current hardcoded site prevents non-technical marketing staff from making content updates, creating a bottleneck.
- **Solution:** A Sanity CMS will be implemented to enable a "composable" architecture, allowing marketing to build new pages from a library of reusable blocks.
- **Ownership:** 35 will own the full Sanity setup and frontend build to ensure a seamless, integrated workflow.
- **Next Step:** Frank will provide a project proposal with a timeline and cost estimate.

---

## Key Topics

### Problem: Hardcoded Site Bottleneck

  - The growthx.ai site is hardcoded, preventing non-technical marketing staff from making content updates.
  - This creates a dependency on developers for simple tasks, such as adding new pages or components.
  - **Goal:** Enable marketing to launch new pages in under one day.

### Solution: Composable Sanity CMS

  - A Sanity CMS will be implemented to support a "composable" architecture.
  - **How it works:** Designs are broken into reusable blocks → marketing staff can drag-and-drop these blocks to build any page layout.
  - **Rationale:** This approach directly solves the content bottleneck and aligns with 35's preferred workflow.
  - **Decision:** 35 will own the full Sanity setup (schema, config) and frontend build.
      - **Why:** To ensure a seamless, integrated workflow and avoid communication overhead between two teams.

### Project Logistics

  - **Timeline:** "As soon as possible," but no hard deadline exists.
  - **Communication:** A shared Slack channel will be created for progress tracking.
      - **Contacts:** Renato (growthx.ai), Ed (growthx.ai), Frank, Pascal, & Sam (35).
  - **Design Process:**
      - Mobile designs will be created in parallel with the backend build.
      - The Figma file will be used for asynchronous feedback.
      - A formal design system can be developed later if needed.
  - **Dark Mode:** A site-wide toggle will be implemented for a consistent user experience.

### Technical Requirements

  - **Analytics:** Existing analytics (PostHog, Google Analytics) must be migrated.
      - Renato will provide a full list of required tags.
  - **Forms:** The current Default form integration will be retained.
      - **Context:** A future project may involve building a custom meeting-booking experience.

---

## Action Items

**Renato Valdes Olmos (GrowthX)**
- Create Slack channel with Frank Slangen, Sem Stassen, Pascal, and Ed (GrowthX); add Ed to analytics overview
- Email Sem Stassen analytics overview (GA, PostHog, GTM, tags) for website migration

**Frank Slangen (35)**
- Email Renato Valdes Olmos with project proposal: hours/timeline for Sanity setup and frontend template
- Design mobile layouts for unique pages and modules in parallel with backend work

---

## Transcript

**Pascal:** This meeting is being recorded.

**Renato Valdes Olmos:** Hi Sam, nice to meet you.

**Renato Valdes Olmos:** Hi Sam, nice to meet you.

**Sem Stassen:** Hallo, aangenaam.

**Renato Valdes Olmos:** Hey, gentlemen, thanks for taking the time to chat with me.

**Renato Valdes Olmos:** Updating things is difficult because it requires setting up the code locally, and not everyone can do that quickly.

**Frank Slangen:** Exactly. We have brand new people coming into the team on the marketing side, not the development side. So we just want to be able to quickly adjust content or add new pages.

**Renato Valdes Olmos:** Updating a component is something that's not really easy right now. But I know it would be much easier in Sanity.

**Frank Slangen:** So that composable piece is really important for both content and maybe also new elements we might build in the future.

**Renato Valdes Olmos:** Yes, ideally. It should take us no more than one day to get a new page live.

**Renato Valdes Olmos:** That's where we want to go. Internally, we have more Framer experience than Sanity experience. But your opinions are very welcome. We can do the migration ourselves, that's not a problem. So I think if we get a nice frontend or template from you, the rest will fall into place. Ed will be our main contact on our side. I can start a Slack channel with all of us in it so we can track progress.

**Frank Slangen:** That sounds good. I think Slack is ideal. Sometimes things are about design, sometimes they're about development. I'd rather leave that to Sam and Pascal. That's the best approach. Do you have a timeline for this?

**Renato Valdes Olmos:** Everything for us is as soon as possible. So as soon as you can get it functional, that's important for us. But we're not on a hard deadline.

**Frank Slangen:** Okay. I think we just need to look at the info we have now. How we'll set it up exactly — Sanity or whatever — there are a certain number of hours involved. And a timeline. Let me send that to you via email. We've already sketched some things out and iterated well. I think that works well. We have some comments to work through. My assumption is we might want a full design system down the road, but we can keep moving forward.

**Renato Valdes Olmos:** If there's a need later for Figma to be more concrete, that's fine. That can always happen.

**Frank Slangen:** There was a big Figma update yesterday about design systems, which is nice.

**Renato Valdes Olmos:** I haven't had a chance to look at it yet.

**Frank Slangen:** I need to catch up too, but it's nice. We need to look at the other pages that will have the most unique design.

**Renato Valdes Olmos:** Mobile is still a thing though.

**Frank Slangen:** We really need to design those still. At least the unique pages and modules. We work here as a team non-stop, so it's not that we're all remote and separate. We walk over to each other and check things. We need a few things in place. I think in this phase it can run parallel, so we can start setting up the backend while I continue with mobile and maybe fix some components so you have something more structured to work with.

**Renato Valdes Olmos:** That sounds good. I don't see major things missing right now.

**Frank Slangen:** There might be more pages like "Origin Story" that could be one-off.

**Renato Valdes Olmos:** We have that at the end already.

**Frank Slangen:** The whole idea should be that we set it up really composable. So if we later say in Figma that a component doesn't work well for us, we can just build a new component without getting locked in. Instead of having to redo whole pages.

**Renato Valdes Olmos:** It needs to be flexible for you.

**Frank Slangen:** I'll look at my colleagues about setting up the Sanity backend. Would it be possible to just develop a template?

**Sem Stassen:** The way we work with Sanity is what Frank mentioned — composable. We break the design into different blocks, and you can assemble them to create any page layout. We can set up templates for a blog page, homepage, whatever. But ultimately you can customize those, move blocks around, adjust things. So templates are pretty well integrated if you choose Sanity, which we prefer.

**Renato Valdes Olmos:** I understand. But I meant more about setting up the Sanity instance. Are there things we could handle internally? I'm just thinking through the balance and how you all prefer to work.

**Sem Stassen:** We'd prefer to set up the Sanity environment ourselves because it's closely connected to the code you'll write. If two different teams work on it, communication becomes much harder and the whole project could face delays. We'd rather handle that on our end. We can do it on your accounts if you want to manage it, but we'd take on the setup since it's tied to code.

**Renato Valdes Olmos:** That works. Good, that sounds great. Frank, I'll need a breakdown from you on what this means in terms of hours.

**Frank Slangen:** I'll take care of that.

**Renato Valdes Olmos:** One quick design question.

**Frank Slangen:** The last screen is about dark mode. I wanted to ask: do you want dark mode for the whole site, or just specific pages like unique ones?

**Renato Valdes Olmos:** For the GrowthX context specifically, I'd implement a toggle instead of unique pages.

**Frank Slangen:** Exactly. I'll check if we do that at the system level or set a default. Those are details we can look at later. Just fill in the Figma as you go, otherwise I'll continue with mobile. Get back to me soon with those hours.

**Renato Valdes Olmos:** Thanks for your time, gentlemen.

**Sem Stassen:** Can I ask two quick questions?

**Renato Valdes Olmos:** Of course.

**Sem Stassen:** Do you have specific requirements or wishes around analytics? I saw you're already doing some things with PostHog and Google Analytics.

**Renato Valdes Olmos:** And various tags. Do we want to migrate those to the new site?

**Renato Valdes Olmos:** Yes, we'd prefer to. I'll make an overview for you. Ed, who's also in the Slack channel, can give more details.

**Sem Stassen:** You'll get an overview from me too. And the same goes for Default, which you use as a contact form right now. I think we keep that.

**Renato Valdes Olmos:** For now, yes. Although that could be the next follow-up project. We want to invest more in the whole meeting-booking experience. But that's to be continued.

**Sem Stassen:** Understood.

**Renato Valdes Olmos:** Thanks. Great.

**Frank Slangen:** Bye guys.

**Renato Valdes Olmos:** Thanks for your time, everyone. I'm looking forward to the collaboration. Talk soon. Cheers.
