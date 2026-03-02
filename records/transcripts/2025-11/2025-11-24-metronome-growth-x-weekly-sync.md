# Metronome <> Growth X - Weekly Sync

<metadata>
date: 2025-11-24
time: 21:14 UTC
duration: 17 minutes
organizer: Matthew Panzarino (GrowthX)
participants: Matthew Panzarino (GrowthX), Katya Luscomb (GrowthX), Will Watters (Metronome), Megan LaFlamme (Metronome)
fathom_recording_id: 104016979
fathom_url: https://fathom.video/calls/484162090
share_url: https://fathom.video/share/yXhysQiyw1gGtJrdxJvqhG8upJsHwY_X
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

GrowthX introduced Katya Luscomb as the new project lead to replace Matthew Panzarino, who is moving to other roles. The team confirmed that only 9% of AI pricing companies require custom pricing table templates (3+ products), with the remaining 91% automating via API, reducing scope and complexity. Will Watters will simplify the overly granular tagging taxonomy to just Industry + Pricing Model, and complete a full review of sample pages to align copy with Metronome's brand voice (R speak) and provide structural feedback.

---

## Context

Metronome and GrowthX are building an AI pricing index platform—a comprehensive directory of AI companies and their pricing models. GrowthX is the delivery partner responsible for building out the content, structure, and templating; Metronome (specifically Will Watters, who is new to the role, and Megan LaFlamme) is the client coordinating approvals and brand voice alignment. Matthew Panzarino had been leading the GrowthX side, but is transitioning to other responsibilities. This meeting was a handoff to Katya Luscomb, a GrowthX strategist with hands-on editorial experience, while Matthew remains available for guidance. The core tension is balancing automation (to ship 91% of companies quickly via API) with quality control (custom handling for the 9% edge cases, and ensuring all content reflects Metronome's specific voice and standards).

---

## Relevance

- **To GrowthX Delivery:** Staffing handoff from Matthew Panzarino to Katya Luscomb as project lead; internal alignment is solid and no service interruption expected. Data audit work (auditing ~100 AI companies) reduced scope complexity by validating that 3+ product pricing is a 9% edge case, not a widespread problem, enabling pragmatic manual-vs-API split.

- **To GrowthX Business Development:** Client is actively engaged and happy with the direction; Metronome is iterating on tagging and page review (Will Watters new to role, still learning the product). Brand alignment ("R speak") is a key driver for iteration cycles—expect ongoing feedback loops on page content and structure over next 1-2 weeks.

- **To Product & Delivery:** Airtable workflow improvement flagged: GrowthX will create a separate "problem companies" tab in Airtable to segregate the 9 companies with 3+ products, preventing manual outliers from breaking automated publishing workflows. Custom table format for multi-product companies will need CMS handling with potential JSON formatting adjustments.

---

## Overview

- **Staffing Change:** Katya Luscomb is now the GrowthX project lead, replacing Matthew Panzarino.
- **Multi-Product Strategy:** A data audit confirmed that only \~9% of companies have 3+ products. These will be handled manually in the CMS, while the rest automate via API.
- **Tagging Simplification:** The proposed taxonomy is too complex. Will Watters will simplify it to a core `Industry` + `Pricing Model` structure to improve user navigation.
- **Page Review:** Will Watters will review all sample pages to align content with Metronome's brand voice ("R speak") and provide consistent structural feedback.

---

## Key Topics

### Staffing & Introductions

  - Katya Luscomb is the new GrowthX project lead, replacing Matthew Panzarino, who is moving to other roles.
  - Katya has been fully briefed and will ensure a seamless transition.

### Multi-Product Company Strategy

  - **Problem:** The standard pricing table template doesn't support companies with 3+ products, which require custom table structures.
  - **Solution:** A data audit of \~100 companies confirmed this is a low-volume issue, making a custom approach feasible.
      - **Findings:** 1-product (79%), 2-product (12%), 3-product (9), 4+ product (2).
      - **Decision:** Automate 1-2 product companies via API. Manually build custom tables for 3+ product companies in the CMS.
  - **Workflow:** GrowthX will create a separate "problem companies" tab in Airtable to flag these for manual handling.

### Tagging Taxonomy Simplification

  - **Problem:** The initial taxonomy is overly complex, with too many granular tags (e.g., "action-based pricing," "agent time-based pricing").
  - **Solution:** Simplify the tagging structure to improve user navigation and reduce complexity.
      - **Core Structure:** `Industry` (e.g., "Image Generation") + `Pricing Model` (e.g., "Output-Based").
      - **Rationale:** This combination provides sufficient filtering power for the initial launch. More granular tags can be added later if needed.

### Page Content & Structure Review

  - **Status:** Will Watters has started reviewing sample pages and will complete the full review in the next few days.
  - **Feedback Goals:**
      - **Content:** Align all copy with Metronome's brand voice ("R speak").
      - **Structure:** Provide consistent feedback on page layout.
  - **Process:** GrowthX will use this feedback to refine the page template and content guidelines, ensuring future pages are aligned from the start.

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Add Airtable tab "Non-standard companies" to flag 9 multi-product outliers for manual CMS handling

**Katya Luscomb (GrowthX)**
- Incorporate feedback from Will Watters' page review into page template and content guidelines

**Will Watters (Metronome)**
- Simplify tagging taxonomy: consolidate to core Industry + Pricing Model structure; send suggestions to Matthew/Katya
- Complete full review of all sample pages and add markups/comments for brand voice ("R speak") and structural alignment

---

## Transcript

**Matthew Panzarino:** Hello.

**Katya Luscomb:** All the meetings today.

**Matthew Panzarino:** Oh, my audio is going somewhere. There it is—figured it out. Turns out you have to actually turn your volume up to hear. Sometimes Zoom gremlins just really get to me.

**Matthew Panzarino:** I like your cozy, Christmassy background.

**Katya Luscomb:** It's chilly here in Reno now.

**Matthew Panzarino:** Yeah, it's getting chilly here too in Central California. Our winters are pretty mild. Still, chilly for us here is anything below 65 degrees—it's cold.

**Katya Luscomb:** What part of Central California are you in?

**Matthew Panzarino:** Fresno. Dead center, basically. The old Central Valley.

**Will Watters:** Hello.

**Matthew Panzarino:** Howdy, howdy. Hey, Will.

**Katya Luscomb:** Hey, hi.

**Matthew Panzarino:** Okay, pretty straightforward agenda today, but I wanted to first introduce Katya. She's going to be stepping in, and you'll be seeing her face on these calls more. I'll probably be on next week again, but I fully briefed Katya on the project last week and will still be around. Not just vanishing on you. It's just a matter of us stepping into some other roles here. Katya will be your point of contact and kind of driving the project, make sure everything stays on track. But internally, I think we're in lockstep, so there should be no service interruptions at all. But I'm happy to have you introduce yourself, Katya.

**Katya Luscomb:** Yeah, sure. Nice to meet you, Will. I've been helping out leading strategy with some of the clients here at GrowthX and pretty hands-on with some of their editorial work as well. Excited to be joining you guys and helping brainstorm and discuss strategy and keeping everything flowing for you all.

**Will Watters:** Awesome. Great to meet you.

**Matthew Panzarino:** Will's a couple months in at Metronome as well. It's a fresh take on all things, I think, on both sides.

**Matthew Panzarino:** We did a multi-product exploration to see how many companies were actually going to be non-standard. We found that there were a decent amount of two-product companies—they have a sub and a per-token model, for example. We've solved those because the pricing logic is similar. We can just do the OpenAI treatment: one page per sub and one page for per-token pricing. We found very few with three or four or more products. I think it's best to just handle those custom. We'll build tables by hand and ship them on your side in the same template box. We can brief Chris on that handful of custom ones if he needs to make adjustments to the template.

**Matthew Panzarino:** The vast majority are one product, a very decent amount with two products—consumer-enterprise pricing. Then we have a handful with three products, nine with three, and two with four or more. I really don't think it's going to be a huge problem. We scraped about a hundred companies. Statistically speaking, I think the proportions will be relatively the same. I don't think we should drive ourselves nuts for 9% of scenarios. We'll just build those custom.

**Will Watters:** Cool. That all makes sense. Can you clarify what all that means for the work with Chris? I've been following the thread in the channel but I'm not totally making the connection between what's going on and what's needed for me.

**Matthew Panzarino:** Right. So the issue is in the pricing snapshot section—the model, price, input, output, context window, API status. That's standard for token-based pricing. But there are a handful of companies where additional columns are needed because they're non-standard. Those nine companies need custom handling. So Chris was asking, how do we handle these? I wanted to do a quick audit to see how many we were talking about. If half the companies had more than this, we'd need big adjustments. But because only a few are, we can build a table format for those nine and tell Chris what they look like. He can make sure they fit into the standard format. We can provide whatever JSON formatting or padding is necessary.

**Matthew Panzarino:** For the vast majority, he's taking them in via API—taking the JSON files and using the API to establish the pages. That's the right approach. We do that with a lot of clients. But for those nine companies, we'd go into the CMS and make sure it looks good. If Chris wants to handle that himself, that's cool too by our standards.

**Megan LaFlamme:** That makes sense to me. One question: where in the phases are those nine companies? How will we notify Chris so the automated workflows don't break?

**Matthew Panzarino:** We'll ship them separately. We'll put a separate tab in the Airtable and say, here's the problem companies. That way he'll know when those come down the pipe. You can see here this one has three products—Claude: API, web subscription, and Claude Code. Because it's such an important one, we'd do three separate pages. DeepL has five: translator, voice, DeepL agent. We'd build a non-standard version with pricing snapshot and normalize it across the different ones.

**Megan LaFlamme:** That makes sense.

**Matthew Panzarino:** The big takeaway is the vast majority will be no problem. It's just a handful of outliers, and we'll handle those ad hoc. We can deliver whatever we need. I don't think even the ones with four or three products, aside from Anthropic, are that much of a problem. We'll be fine. We'll be able to deliver them in whatever data format is necessary.

**Matthew Panzarino:** Oh, tagging. The original taxonomy was built off the initial proposal, basically by category. But we can make the tagging whatever you like. How do you want users to navigate this from the hub? Do you want it by model, usage-based, outcome-based? We can go as deep as you want. It's really a matter of what will be exposed now and what you may want to slice by in the future.

**Will Watters:** Yeah, that makes sense.

**Megan LaFlamme:** I think we just have to review the tagging that was proposed and make sure we're still good with that.

**Will Watters:** Can you scroll down while we're on this?

**Matthew Panzarino:** These are all the pricing models. And there's the packaging models.

**Will Watters:** I think there are a lot of them. Output-based pricing seems... there's a lot of granular detail here. Some of these seem more detailed than we need.

**Megan LaFlamme:** Yeah, I think we could simplify this. Action-based pricing, automation-based pricing—we probably don't need those.

**Will Watters:** Yeah, agent time-based pricing is effectively time-based or compute-based pricing, right? If we cut it by eight different things, does that actually make it seem more complex than it is? I want to know a company that monetizes based on output in the image generation category. That gets you to what you want versus calling it something else. I'll take a pass at this and provide some suggestions. I think the matrix is pricing model and industry—that's what matters.

**Matthew Panzarino:** Right. Industry and pricing model. Those two should give you a pretty decent way to group, cluster, and slice and present them—from the main site or bundling them for campaigns later. That gives you decent flexibility.

**Will Watters:** Yep. That sounds good.

**Matthew Panzarino:** And Chris is looking at the latest sample JSON. I think we're okay there. We're really close. We just added some additional padding and fields he wanted.

**Matthew Panzarino:** I noticed you jumped in and started commenting on the sample pages.

**Will Watters:** Yeah. I've been caught up with another project that's taking longer. But over the next couple of days, I plan to go through every page and provide more markups. I think some will be consistent—pretty consistent comments on page structure. But I do want to make sure I read through each one in case there's wording and phrasing that's a little more R speak.

**Matthew Panzarino:** Yeah. Remember that anything you mark up or comment, we will ingest and make sure goes forward. We should have less errata over time, especially on brand alignment and tone. If something's too flippant or too acerbic, just let us know and we'll tweak it.

**Matthew Panzarino:** We've put in the Metronome's take placeholder for Chris so he knows how to format the page. We can fill that in at any point with actual data.

**Will Watters:** Sounds good.

**Matthew Panzarino:** I think that's about it from our side. At scale, measure twice, cut once is always the better approach. When it comes time to cut, we can cut very fast. We'll have it ready for delivery whenever you need it.

**Will Watters:** And I appreciate your patience with me as I go through this as a newbie. It just takes me longer to read through and digest to make sure I'm making appropriate suggestions.

**Matthew Panzarino:** Totally fine.

**Will Watters:** Cool. Sounds good.

**Matthew Panzarino:** Thanks, folks.

**Katya Luscomb:** Nice to meet you.

**Megan LaFlamme:** Yeah, nice to meet you. Have a good holiday.

**Will Watters:** You too. See ya.
