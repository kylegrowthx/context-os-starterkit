# Raze // GrowthX Sync

<metadata>
date: 2025-04-21
time: 16:31 UTC
duration: 18 minutes
organizer: jason@growthx.ai
participants: Ed Abazi (Raze), Jason Gong (GrowthX)
fathom_recording_id: 58265374
fathom_url: https://fathom.video/calls/281720911
share_url: https://fathom.video/share/rMeUpRBaRQwzKynua2ydgdfEWXyKucXx
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

GrowthX and Raze synced on website development progress and upcoming priorities. The pricing page is nearly complete with improved logo display and table design; the demo page and AI-led growth page are next in priority. The team aims to complete all pages by end of week to allow time for testing, with longer-term considerations including performance optimization (currently scoring low), CMS integration for easier content management, and mobile optimization for the pricing table.

---

## Context

Raze is an external development partner working with GrowthX on the redesign and development of the GrowthX website. This sync brought together Ed Abazi (Raze lead developer) and Jason Gong (GrowthX) to review progress on multiple pages and align on timelines ahead of a website launch planned for the following week. The meeting focused on technical implementation details, design dependencies, and unblocking work to hit the tight launch deadline.

---

## Relevance

- **To GrowthX Delivery:** Website launch timeline is next week; performance scores on growthx.com are currently low and need optimization after launch (tracking scripts and attention to detail on optimization are key blockers; Ed recommends targeting 90+ for both mobile and desktop).
- **To GrowthX Business Development:** The site relaunch includes pricing, demo, and AI-led growth pages; demo page routes qualified leads directly to Kyle and Marcel's calendars, and unqualified leads to a secondary form (conversion mechanics are now live).
- **To GrowthX Business Development:** Case studies page development noted as future priority to improve credibility; currently most clients are new with limited case study material.

---

---

## Overview

- Pricing page is nearly complete; demo page and AI-led growth page are next priorities
- Performance optimization for GrowthX site needed (currently low scores)
- Aim to complete current tasks by end of week, leaving time for testing
- Long-term considerations: CMS integration, brand cohesion, and scalability

---

## Key Topics

### Website Development Progress

  - Pricing page:
      - Nearly complete with improved logo display and table design
      - Minor tweaks needed (e.g., text adjustments for one-line descriptions)
  - Demo page:
      - Utilizes Default for routing logic and iframe integration
      - Styling needed for the non-iframe half of the page
  - AI-led growth page:
      - Design in progress by Mergem
      - Will be a single page with button likely linked to Default or Typeform

### Technical Considerations

  - Sticking with Next.js for tech stack, particularly for TechStock project
  - Future considerations for logged-in experience and course platform integration
  - Performance optimization needed for GrowthX site (currently low scores)
      - Plan to address after launch week
      - Potential issues with tracking scripts and lack of optimization

### Project Management

  - Estimated timelines:
      - Demo page: \~1 day
      - AI-led growth page: Couple of days once design is finalized
  - Priority on proving out partnership with one project in each lane (GrowthX, micro tool, client)
  - Aim to complete current tasks by end of week for testing buffer

### Future Improvements

  - Potential CMS integration for easier content management
  - Mobile optimization for pricing table (card-based layout)
  - Case studies page development for GrowthX

---

## Action Items

**Ed Abazi (Raze)**
- Develop demo page for GrowthX website (estimated 1 day).
- Estimate time for AI-led growth page dev once design received from Mergim.
- Optimize GrowthX website performance scores (after launch week) to target 90+ on both mobile and desktop.

**Jason Gong (GrowthX)**
- Tweak pricing page text for one-line descriptions to fit on single line (improves table appearance).
- Send headshots for AI-led growth page (Marcel and others as needed).
- Schedule follow-up meeting for Wed/Thu.

---

## Transcript

**Ed Abazi:** Now we can, I think.

**Jason Gong:** How is it now? Can you hear me?

**Ed Abazi:** Yeah, I hear you. What's up? How are you?

**Jason Gong:** I'm doing good. How are you doing?

**Ed Abazi:** Pretty good. Just figuring out the repository for the website.

**Ed Abazi:** I know there's a lot to wrap up on there.

**Jason Gong:** I still haven't figured out a recurring meeting, but I thought it'd be good to just sync on the different tasks. On admin stuff, Bridget mentioned Ericsson is our new accounting person, but he's away. Just ping me if there's anything there.

**Ed Abazi:** She mentioned that she was going to take a look this week. So that sounds good.

**Jason Gong:** So I have those three tasks. I know you're almost done with the pricing page, so that's great. Once you do that, if you have a sense of how long things will take—like two days or a week—I think it'd be good to flag that somewhere.

**Ed Abazi:** The pricing page is pretty much done. The demo page, I still need to take a deeper look. What was that service called? Default?

**Jason Gong:** You don't need to touch Default at all. I already set that up. It's basically two columns—one is an iframe to Default, and the other side needs styling. Hopefully I hooked it up right, but not much work needed there.

**Ed Abazi:** How does the form on the hero route people? Are they routed to a page where they fill out a form instead of...

**Jason Gong:** Yeah, I mean, there's a little bit of logic, but I can show you real quick. The logic is already baked in there, and that's why we got Default.

**Ed Abazi:** I thought the entire site was going to be CMS-oriented, but it seems like all the content is baked into the codebase.

**Jason Gong:** That probably requires a little migration at some point. But for now it's simple. The deadline is probably sometime next week for launch. We really need all these things up in some form. If we need to reduce scope to make sure we have pages there to catch people, let's do that. As for migrating to Strapi or another system for copy, we can do that later.

**Ed Abazi:** I was thinking, since I don't know how invested you are in the entire brand right now, it's a good idea to take a step back and think about the brand presentation on the website. If you want to publish tons of blog posts—the blog is already linked to Strapi—or landing pages and content-based pages, you'd want a CMS system handling that, not hard-coded content.

**Jason Gong:** In my head, that's a lower priority than proving out a good partnership here with one project in each lane.

**Jason Gong:** For Default, you don't need to do much. We have criteria—once you fill in your email, it enriches in the background. Then there's a route that goes directly to Kyle and Marcel's calendars, or a secondary form if they're not immediately qualified. Default handles all that logic; you just need to style one half of the page and make it look nice.

**Ed Abazi:** Is the form an iframe as well?

**Jason Gong:** Yeah, the form is all iframe. This part that needs styling is the other column. Let me know if it takes longer than a day. Default actually has its own form, it's just uglier.

**Ed Abazi:** It shouldn't take longer than a day. The pricing page is done. This should take a day. How are we feeling about the AI-led growth page?

**Jason Gong:** Mergim is working on the design as we speak.

**Ed Abazi:** That's amazing. So it'll be a single page?

**Jason Gong:** Yeah, I'll probably hook the button up to Default as well, or maybe just a Typeform.

**Ed Abazi:** That makes sense. What about TechStock? Should we stick to Next.js?

**Jason Gong:** It's up to you guys if you want to experiment with anything. My main concern is speed and how fast we can get it up.

**Jason Gong:** Looking forward for TechStock, since it's a course platform, think through whether we need an out-of-the-box logged-in experience for courses or if we link to a platform that does that.

**Ed Abazi:** If we end up doing that, Next.js is good to stick with.

**Jason Gong:** The Output publication is separate—that one will be more SEO-heavy and content-focused. So there will be three flavors: GrowthX (the mysterious service), TechStock (the course), and Output (the publication).

**Ed Abazi:** I want to go back and look at the GrowthX site performance scores at some point. They're pretty low right now.

**Jason Gong:** Really?

**Ed Abazi:** Yeah. I personally finish the whole website and then optimize. I try to get above 90 for both mobile and desktop performance, and obviously SEO should be 100. It doesn't have to be right now, but let's take a step.

**Jason Gong:** We need to walk the walk. We're giving people advice on page performance and our site sucks—that's not great. Let's look at this maybe after next week when we get all the launch stuff up.

**Ed Abazi:** There's a lot of little changes needed to boost the score. A lot of the numbers drop if you're loading a lot of tracking scripts.

**Jason Gong:** I don't think we have anything super complicated. Let me know if there's anything I can do to help unblock the AI-led growth page—that one's quite a bit of work.

**Ed Abazi:** Once we have a V1 design, we'll send it over. If we're happy, I'll start coding and hopefully a couple days will be enough to get it up.

**Jason Gong:** This first month, I really appreciate you guys moving so fast. Let's just prove out how this will work. I want one project in each lane: one for GrowthX, one for the micro tool area, and one for a client. If those work out, I want to scale it up from there.

**Ed Abazi:** That sounds really good.

**Ed Abazi:** You notice the small changes I made to the navigation bar?

**Jason Gong:** I think I fixed that in one of my branches. I'm not sure how someone missed that for so long.

**Ed Abazi:** It's been there for a while. For the pricing page, I made some updates. I added logos—Superhuman was tricky because it's very wide.

**Jason Gong:** The original looks really ugly and doesn't scale properly for the logos.

**Ed Abazi:** I made one small change on hover—I made part of it not green because having both green looked off. The line height was also really off. I came up with this table design, trying to stick to the current style while giving GrowthX a highlight with a blue stroke. It scales on mobile as well. If we have more time, I could turn each row into a card on mobile for better UX, but let's leave it for now. If we have time towards the end of the week, I'll get it.

**Jason Gong:** That looks good. I'll tweak the text—maybe it'd look better as one line.

**Ed Abazi:** If you tweak the text to fit on one line, it'll definitely work better. I'm not sure what else is needed for the pricing page. I think that's it. I'll get on the demo page next, and then hopefully we'll have a final design for ai.growth.com and I'll work on that too. Let's try and finish everything by end of week so we have time to test.

**Jason Gong:** That would be great. I'm going to show Marcel the pricing and demo pages today. The AI-led growth is the main one. Once we align on the design, I'm not worried if we get it out Monday. I'm really happy with the detail and polish.

**Jason Gong:** Lightbox is expensive for what they do. I think the problem with scaling is founders always do great work, but then once you're bigger, it kind of falls apart.

**Ed Abazi:** Yeah, I know what you mean. But at that point, your name is on the company. Make sure what goes out there is double-checked.

**Ed Abazi:** One question for the AI-led Growth page. We have a picture of Marcel in the hero. Is there another picture we can add?

**Jason Gong:** Do you have the one on his LinkedIn? Or are you talking about another person?

**Ed Abazi:** The hero title says "Taught by those that built it," so we'd want multiple people.

**Jason Gong:** The design has space for two. I'll grab some headshots and send them over.

**Jason Gong:** About Lightbox—if it's not a secret, how much do they cost?

**Jason Gong:** They charge 80 bucks an hour. Right now I'm paying them hourly, but they wanted to fully load two people full-time at 80 an hour as their minimum for a month.

**Ed Abazi:** That makes sense. If that's where they start, you could probably push it down.

**Jason Gong:** The one or two examples they show are really nice. They always show the Mother Duck website—it's cohesive, feels nice. I think that helps them sell their expensive plan more than anything.

**Ed Abazi:** Their website is nice, but the case studies were weak.

**Jason Gong:** A case studies page for GrowthX would be something to work on at some point.

**Ed Abazi:** I saw you had planned case studies for each client in the table.

**Jason Gong:** Yeah, we're trying to get them. A lot of our clients are new, so there's nothing yet.

**Jason Gong:** All right, I think that's it. I'll try to schedule something for Wednesday or Thursday.

**Ed Abazi:** We'll send the design over as soon as we have something. Let me know if you need access to anything.

**Jason Gong:** Thanks, man. I'll talk to you later.

**Ed Abazi:** Thanks, Ed. See you.
