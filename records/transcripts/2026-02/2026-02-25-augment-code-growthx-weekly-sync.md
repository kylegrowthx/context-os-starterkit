# Augment Code <> GrowthX Weekly Sync

<metadata>
date: 2026-02-25
time: 18:00 UTC
duration: 24 minutes
organizer: Liz Kushnereit
participants: Sylvain Giuliani, Liz Kushnereit, Molisha Shah
fathom_recording_id: 125332143
fathom_url: https://fathom.video/calls/578884393
share_url: https://fathom.video/share/xqsxwKZnBhszkMByakUQj_nxjBhpG8qG
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Align on growth priorities and OKRs for the new Intent app.

---

## Context

This is a weekly sync between GrowthX and Augment Code. GrowthX provides B2B content marketing services (primarily SEO and AEO strategy) for Augment Code, a developer tools company. Sylvain Giuliani (Augment Code) leads these syncs with Liz Kushnereit (GrowthX's head of content), discussing progress toward shared OKRs and making strategic decisions about product positioning and content priorities. This particular sync focuses on the launch of Augment Code's new "Intent" app — a free AI-powered code intelligence tool — and how GrowthX's content strategy should shift to drive adoption.

---

## Relevance

**To GrowthX Delivery:**
- New product launch (Intent) requires immediate content strategy pivot toward bottom-of-funnel (BOFU) articles, replicating the success model used for Code Review.
- CTA library architecture shift: moving from inline CTAs to a component-based system that dynamically changes CTAs based on article product tags (`product: intent` vs `product: code-review`).
- PostTag reporting setup needed to track Intent downloads by content source, enabling data-driven content decisions.
- Confirmed article tagging structure uses "funnel" and "product" fields; Intent articles need to be tagged for CTA system to work.

**To GrowthX Business Development:**
- Account health signal: Augment Code is accelerating product development (shipping Intent updates twice daily) and expanding GTM aggressively, indicating strong investor backing and confidence.
- Opportunity to help Augment Code build category ownership for Intent (similar to Code Review's positioning challenge), positioning GrowthX as critical to product launch success.

---

## Overview

- **Intent Downloads are the \#1 Priority:** The primary goal is driving 500 Intent downloads/day to build a community and accelerate growth.
- **New OKRs Set:** New targets are 500 Intent downloads/day and 50k weekly organic traffic (up from a 34k 4-week average).
- **Immediate CTA Pivot:** Blog CTAs will be updated to promote Intent, starting with a quick sidebar change and followed by a more robust, component-based solution.
- **Code Review Trial Launching:** A new free trial for the Code Review product is launching next week to improve its "garbage" conversion rate.

---

## Key Topics

### New OKRs & Growth Strategy

  - **Intent Downloads:** The top priority.
      - **Goal:** 500 downloads/day.
      - **Rationale:** Build a community and accelerate growth toward a 50k user target.
      - **Current Performance:** The Intent landing page converts at a high 18%, validating the product experience and shifting focus to top-of-funnel traffic.
  - **Organic Traffic:**
      - **Goal:** 50,000 weekly organic visitors.
      - **Baseline:** 34,000 weekly average over the last four weeks.
  - **Code Review:**
      - **Goal:** Improve the "garbage" conversion rate of Code Review content.
      - **Solution:** Launch a new free trial next week (e.g., 10-20 free pull requests) to provide a stronger CTA.

### Intent Content & CTA Pivot

  - **Content Strategy:**
      - **Focus:** Create bottom-of-funnel (BOFU) content (e.g., "alternatives" articles) to capture high-intent users.
      - **Guidance:** Use PostTag data to identify top-performing content and replicate its success.
  - **CTA Implementation:**
      - **Problem:** Current blog CTAs promote the main product, not the new Intent app.
      - **Immediate Fix:** Change the sidebar CTA on relevant articles to promote "Download Intent for free."
      - **Longer-Term Solution:** Build a component-based CTA library that dynamically updates based on article tags (e.g., `product: intent`).

---

## Action Items

**Liz Kushnereit**
- Set up PostTag reporting for Intent downloads by content; then send weekly summary to Sylvain
- Send weekly Intent GrowthX update to Sylvain for Thu memo
- Publish high-SV BOFU Intent content
- Implement dynamic sidebar CTA (Intent vs Code Review) across blog
- Tag Intent articles in Spectrum; then update sidebar CTA to Intent

---

## Transcript
**Liz Kushnereit:** Thank you.

**Sylvain Giuliani:** What's up, Liz?

**Liz Kushnereit:** Nothing.

**Sylvain Giuliani:** I'm back at your office.

**Sylvain Giuliani:** You know, I feel like it's a, you're the excuse as I go to growthx, you know, one of the people on this course to be at the office.

**Liz Kushnereit:** Yeah, okay.

**Liz Kushnereit:** That's funny.

**Liz Kushnereit:** I was watching some of y'all's videos, which were also filmed at the office.

**Liz Kushnereit:** And I was like, okay.

**Sylvain Giuliani:** Oh, yeah, yeah, with, I mean, yeah.

**Liz Kushnereit:** Yeah, I mean, it's a nice office, right?

**Sylvain Giuliani:** It's cute.

**Sylvain Giuliani:** Yeah, it's a good backdrop, you know, makes us look like cool startup compared to a  office in Palo Alto that looks like a 90s business park with yellow lights and drop ceiling, you know.

**Liz Kushnereit:** Yeah, also the plants.

**Liz Kushnereit:** I feel like the plants make the office look really, really good.

**Sylvain Giuliani:** Yeah, yeah, like a mid-century modern, like aesthetic.

**Sylvain Giuliani:** Yeah, repurposed firehouse, blah, blah, kind of thing.

**Sylvain Giuliani:** Okay, I got some OKR for you.

**Sylvain Giuliani:** I got a bunch of things to discuss, too, so we can, I mean, I think we can go for the motion, right?

**Sylvain Giuliani:** And then we can discuss this at the end, too.

**Liz Kushnereit:** Yeah, I mean, it's kind of quick because it's a lot of, I'm just building a lot right now.

**Liz Kushnereit:** But I put in some OKRs based on some baselines I could get for SEO, which was mostly like 10% increase month over month.

**Liz Kushnereit:** But we can change these if you have some.

**Liz Kushnereit:** And then I need to establish AEO OKRs going forward, but that's a much different process and I need someone with more capacity. But overall, things are still trending up with even more ownership of code review. The only thing is that a lot of it is related to open source code review, so there's still room for a canonical piece that recommends Augment Code.

**Liz Kushnereit:** And then, oh, sorry, I made this into a column, but just overall, I'm working on the post-QBR with a big project plan I need to work through.

**Liz Kushnereit:** CJ library is still P0 and then working through the other lanes like this here.

**Liz Kushnereit:** OK, and then intent app.

**Liz Kushnereit:** I put it in one of the threads with the gals, but this is everything we're shipping.

**Liz Kushnereit:** And then I also dropped in what our product matrix looks like.

**Liz Kushnereit:** So I'll drop that.

**Sylvain Giuliani:** So the focus is intent, intent, intent, intent. Because it's so new and the trackability is clear, the focus is just getting intent downloads, right? In PostTag, there's an event for download intent. So the goal is: can we get SEO to pump 500 downloads a day? That's just a click on the page. Right now, the goal is to pace as fast as possible to 50,000, building community, even getting to 3,000-4,000 a day.

**Sylvain Giuliani:** So I was, like, you know, growthx should be able to carry his own share.

**Sylvain Giuliani:** Like, I know it's going to be a slow start, you know what I mean, right?

**Sylvain Giuliani:** And also, looking at our landing page right now, the product landing page itself has a pretty high conversion rate at 18% of the people on that page who load the app and sign up.

**Sylvain Giuliani:** I mean, we'll worry about that later, you know, at like end of March, like April, right?

**Sylvain Giuliani:** But like right now, I'm like, I'm just writing the team to be like, what have we done today to get more downloads, right?

**Sylvain Giuliani:** Like that is basically because that's the not, like if people are not downloading, people are not aware and people are not trying, right?

**Sylvain Giuliani:** So that's kind of like a bit, like that's kind of the reasoning behind that.

**Sylvain Giuliani:** Having said that on the code review stuff, I think it's really exciting what you showed me. Hopefully next week — famous last words — we'll have a nicer free trial of code review that's a lot better for the conversion of that traffic.

**Sylvain Giuliani:** The conversion rate of that content is garbage because the rest of the flow is garbage. But now we'll have a good CTA to be like, "Start using OpenCodeReview — the first 10 or 20 pull requests are free." That's the big thing.

**Sylvain Giuliani:** So that's like a big focus.

**Sylvain Giuliani:** After that, OKL is the same as getting more weekly traffic from Organic, right?

**Sylvain Giuliani:** So how do we go from the 34,000 weekly average over the last four weeks to 50,000? That's the high-level goal. We can add more goals as we move forward.

**Liz Kushnereit:** The category ownership, but the Bofu strategy should work, especially if it's so easy to install.

**Sylvain Giuliani:** I hear you on the CTA and the priority there. Roz is working on positioning docs that should help everyone understand what Intent is and how it's different.

**Sylvain Giuliani:** I mean, it is, we are shipping a new version every day right now, at least twice a day, right?

**Liz Kushnereit:** So there's like a lot of new stuff coming out.

**Liz Kushnereit:** Okay.

**Sylvain Giuliani:** But yeah, it's a free app.

**Sylvain Giuliani:** You can use Cloud Code for it, to power it, whatever.

**Sylvain Giuliani:** You don't have to give us any money. You don't have to sign up — you just download Intent, use Claude Code or Claude Desktop or whatever, and you're on your way.

**Sylvain Giuliani:** So it should be pretty straightforward, you know?

**Liz Kushnereit:** Yeah.

**Sylvain Giuliani:** This should be pretty straightforward.

**Sylvain Giuliani:** Right now I want to look at the data. We should be able to see which guides are driving Intent downloads. Actually, the fact that 31 people visited guides and then wandered across the website and stumbled into downloading Intent is actually shocking.

**Sylvain Giuliani:** We should be able to look at the conversion rate by content type and see which pieces drive the most Intent downloads. For example, the "code review vs Augment Code" piece has driven 81 downloads, but only 10 people came from that article. So we should be able to slice that data and see what's working.

**Liz Kushnereit:** Yeah, I can prioritize those too, like those top of work.

**Sylvain Giuliani:** Every Thursday I write an internal memo to the company about our Intent goals and what's happening. What you shared with me today tells me what GrowthX is doing to drive downloads. For your update, the main things are: you're writing more content, optimizing it, and I'll use PostTag as a data source to see what's changing and what drives downloads. As long as you keep updating your work, that should work. This is week one, so we're just starting the work to have an impact next week.

**Liz Kushnereit:** Yeah, we're going to publish a bunch of content.

**Sylvain Giuliani:** That's basically the update. I just want to know what we did this week and what we're doing next week to grow the numbers.

**Liz Kushnereit:** Okay. Specifically with Intent, we're still shipping new features.

**Sylvain Giuliani:** Right. For Intent, I basically have to send a memo to the company with Intent download charts, DAUs, and all that. The update will be: "What have we done to grow downloads this week? Well, Liz published blog posts. It's SEO, it'll take time, but we got to publish them." Then we look at the charts showing them starting to live. We also track what our video team is doing — five tutorial videos, etc.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** I'll get you a summary. I'll prioritize high-search-volume BOFU content since we're not looking for paid. Intent is a priority and we'll shift capacity to focus on that. Fingers crossed it works well.

**Sylvain Giuliani:** Easy.

**Liz Kushnereit:** Yeah, I think it is easy.

**Liz Kushnereit:** I'm just like nervous now, but it'll be fine.

**Sylvain Giuliani:** Why are you nervous?

**Liz Kushnereit:** Oh, because I mean, it's like we did so we did really well with code review, like owning the category, but we didn't necessarily own or we're not fully the recommended choice.

**Liz Kushnereit:** Now we have the opportunity to like take all the learnings from code review and become the recommended choice with intent.

**Liz Kushnereit:** So it's a good thing.

**Liz Kushnereit:** It's just like, like, I feel like there's an opportunity to do it really, really well.

**Sylvain Giuliani:** I we, we, we still, we should still do code review.

**Sylvain Giuliani:** We're not giving up.

**Liz Kushnereit:** No, a hundred percent.

**Liz Kushnereit:** Not going to stop doing that.

**Liz Kushnereit:** But I mean, like now we're like very set up to be successful on intent.

**Sylvain Giuliani:** And so it's like, let's, yeah, a little bit of pressure.

**Sylvain Giuliani:** Let's go all arms.

**Liz Kushnereit:** Yes.

**Liz Kushnereit:** Yeah.

**Liz Kushnereit:** Okay.

**Sylvain Giuliani:** We'll also write pillar pieces for leadership content around Intent that you can anchor on for backlinks. That should be a source of ideas for other SEO work and things like that.

**Liz Kushnereit:** Yeah.

**Sylvain Giuliani:** We're about to ship a feature, I mean, hopefully this week or next week, about the RALF loop.

**Sylvain Giuliani:** So it's like, cool, Liz, everything that we talked about the RALF loop in the past, let's go update the CTA on intent.

**Sylvain Giuliani:** Let's do that again, right?

**Sylvain Giuliani:** So I think like the P0 CTA management is like critical, yeah.

**Liz Kushnereit:** Yes, heard.

**Liz Kushnereit:** Okay.

**Liz Kushnereit:** All right.

**Liz Kushnereit:** I'll try to get that tomorrow then.

**Sylvain Giuliani:** But do you have a plan for that?

**Liz Kushnereit:** I was going for a complex variable library, but that might take a few more days. Right now the editors are doing inline CTAs, but we could use the component better. It's in the project plan, but I need to think through it.

**Sylvain Giuliani:** And I need to dig into Intent a little bit more about like what the Do we tag, that's one thing I was going to ask you, like, do we tag content nowadays?

**Liz Kushnereit:** We're tagging it with funnel and product.

**Liz Kushnereit:** So there's, yes, that can like inform the library, like the decision of which CTA it puts in at the field.

**Liz Kushnereit:** But I mean, one thing I can do, like literally right now, right?

**Sylvain Giuliani:** I can change the sidebar CTA to download Intent based on the blog post category. That'll take five minutes. The call to action on this blog post should say "download Intent" not "install Augment." Right now Intent is buried and nobody sees it. I'll reuse the same component from the Intent page where you can select what you want. The CTA will change based on whether the article is tagged as Intent.

**Liz Kushnereit:** I think it's at the article level. We could go back into Spectrum and update the tags.

**Sylvain Giuliani:** Right, and we can use the AI agent to help tag them. Have you tried it?

**Liz Kushnereit:** Yeah, it works really well.

**Sylvain Giuliani:** Let me test by changing one article to Intent.

**Liz Kushnereit:** Great. Let's do it. Alright, team break.

**Sylvain Giuliani:** Thanks, Liz. Talk to you later.

**Liz Kushnereit:** Okay, bye.
