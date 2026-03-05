# Datagrid <> GrowthX Weekly Sync

<metadata>
date: 2025-03-27
time: 18:59 UTC
duration: 41 minutes
organizer: vivek@growthxlabs.com
participants: Kyle Gaudreau, Jimmy Pal, Mara Leighton, Vivek Shankar, Kaitlin Quimby, Miles Gordenker, Thiago da Costa
fathom_recording_id: 54240459
fathom_url: https://fathom.video/calls/262149226
share_url: https://fathom.video/share/uRBkYpr-qGoNAkK1exxTQyn9yR-g4DhB
source: fathom
enriched_on: 2026-03-04 02:15 UTC
</metadata>

---

## Summary

GrowthX and Datagrid discussed progress on a 257-article content push due Saturday, with focus on productivity techniques and data extraction use cases. Miles presented a low-fidelity prototype for an AI-assisted image selection workflow in Datagrid — the team assessed complexity versus webinar impact and agreed the initial version might be too simple, then discussed a more ambitious approach with dynamic column generation and potential Webflow integration. Kyle and Kaitlin will test the workflow and schedule the webinar date (targeting approximately 6 weeks out), while the team plans to explore an additional webinar topic to maintain roughly 6-week intervals between events.

---

## Context

GrowthX is in a content production engagement with Datagrid, an AI platform for workflow automation and data transformation. Vivek Shankar (GrowthX) organized this sync with Datagrid team members (Kyle Gaudreau, Kaitlin Quimby, Miles Gordenker, Thiago da Costa) to review weekly content progress and plan upcoming webinars. Mara Leighton, newly onboarded to GrowthX as Associate Director after background in journalism and content marketing agencies, joined to observe and contribute.

The partnership centers on creating high-volume content (257 articles this week alone) while simultaneously building webinar-based marketing demonstrations of Datagrid's capabilities. The webinar strategy is critical for both customer acquisition and product validation — GrowthX benefits from deepening the client relationship and creating case studies, while Datagrid gains product-qualified leads and feedback on feature requests (like Webflow integration for draft uploads). This is a multi-quarter engagement requiring close technical and product collaboration.

---

## Relevance

- **To GrowthX Delivery:** Webinar-driven content marketing at scale (257 articles in one week) requires tight QA/quality control workflows. Miles demonstrated how Datagrid's AI scoring columns can automate quality checks on GrowthX's own article output — this is dogfooding that could become a repeatable methodology across other clients.

- **To GrowthX Delivery:** Webflow integration is explicitly on Datagrid's roadmap and Miles signaled willingness to prioritize it as a proof-of-concept if conversion probability is strong. This dependency impacts content-to-publication workflow design for the engagement.

- **To GrowthX Business Development:** Client engagement health is strong — Datagrid ran a 200-signup webinar in 2.5 weeks using email + LinkedIn promotion, indicating brand awareness and audience interest. Team appetite for 6-week webinar cadence (vs. ad-hoc) signals scaling intent and renewal confidence.

- **To GrowthX Business Development:** Mara Leighton (newly hired at GrowthX) replacing a team member on Datagrid calls shows client continuity management. Datagrid acknowledged her background and she's already contributing in first week — low onboarding friction.

- **To CheckThat:** The image selection workflow uses a stock-photo library as AI agent knowledge source. Miles mentioned skepticism about AI-generated selections ("your audience has probably been burned by AI hype before") — human approval layers are critical for this use case.

---

## Overview

- Content production on track: 257 articles publishing Saturday, focused on productivity techniques, document data extraction, and e-commerce use cases
- Webinar planning: Miles presented low-fidelity prototype for AI-assisted image selection workflow; team discussed scope and feasibility, decided to explore enhanced version with dynamic column generation and potential Webflow integration
- Image selection workflow design: AI agent analyzes article content, suggests relevant image passages with multiple options per passage, user reviews and approves before publication
- Link building continuing; new links added to tracking table
- Team targeting webinar cadence of approximately 6 weeks between events; planning to identify second webinar topic to maintain schedule

---

## Key Topics

### Content Production Update

  - 257 articles to be published by Saturday
  - Focus areas: productivity techniques, document data extraction, e-commerce use cases
  - Some volatility in local report metrics (clicks/impressions); team monitoring for seasonal vs. trend patterns

### Webinar Planning: AI-Assisted Image Selection

  - Miles presented low-fidelity prototype in Datagrid for AI-assisted article image selection workflow
  - Core workflow:
      - Import articles into spreadsheet view
      - AI agent analyzes content, suggests relevant image passages based on article topic and section context
      - Multiple image options provided for each passage (user can compare and select)
      - User reviews/approves selections before publication with option to re-prompt agent
      - Final output in markdown or blog-friendly format ready for CMS
  - Team assessed complexity: Initial version has appeal but may not provide enough "wow factor" for full webinar; discussed more ambitious approach
  - Potential enhancements under discussion:
      - Dynamic column generation based on article structure (agent determines how many sections to highlight)
      - Integration with Webflow for draft uploads (Miles checking with engineering on feasibility as proof-of-concept)
      - Quality control checks using existing AI scoring capabilities (e.g., grade output based on GrowthX content standards)

### Webinar Logistics

  - Previous webinar achieved 200 signups, organized in approximately 2.5 weeks
  - Promotion channels: Email campaigns to customer lists (2-3 emails), LinkedIn posts, direct messaging via LinkedIn to interested prospects
  - Platform: Zoom Webinar
  - Registration: Currently sends direct Zoom link via email; considering HubSpot landing page to improve conversion tracking and data capture
  - Next steps: Kaitlin to schedule image selection webinar date targeting ~6 weeks out; team also evaluating Slack community as channel for user testimonials and use case sharing post-webinar

### Link Building

  - Continuing as usual
  - New links added to tracking table

### Additional Webinar Planning

  - Team aims for webinars every \~6 weeks
  - Considering additional topic alongside AI image selection use case
  - Exploring potential to leverage Slack community for user engagement/testimonials

---

## Action Items

**Miles Gordenker (Datagrid)**
- Create table with image selection workflow schema in GrowthX Datagrid instance; invite GrowthX and Datagrid team members for testing

**Kyle Gaudreau (GrowthX)**
- Test image selection workflow in Datagrid once access granted; provide feedback on functionality, UX, and webinar readiness

**Kaitlin Quimby (Datagrid)**
- Schedule date for image selection webinar with team; aim for approximately 6 weeks out
- Schedule planning meeting for additional webinar topic (non-image selection) to maintain 6-week cadence

---

## Transcript

**Vivek Shankar:** Well, just before we dive in, just want to introduce Mara, she has recently joined us here at GrowthX, so I'm going to let Mara introduce herself and we can take it from there.

**Vivek Shankar:** I'm so excited to meet you.

**Mara Leighton:** I'm Mara. I just joined the team here. This is my second week. I started my career in journalism, so I worked at Business Insider for consulting and then joined a content marketing agency, worked with venture-backed startups for about a year and a half there and did all types of long form content. I'm now joining the team here as an Associate Director. So I'll be joining the calls, getting up to speed, and you'll probably see me in Slack as well. I've been watching some of the calls so it feels like I already know everyone and I'm excited to work together.

**Kaitlin Quimby:** Happy to have you on board.

**Vivek Shankar:** Moving into our weekly updates. We'll have 257 articles published by this Saturday. For this week we're focusing on productivity techniques, document data extraction, and e-commerce use cases. We saw some good results from e-commerce a couple of weeks back so we're exploring that more. We're also seeing some volatility in our local report metrics — clicks and impressions dipped a bit this week. We're monitoring to see if this is seasonal or a bigger trend, but at this point we suspect it's seasonal since we've seen similar patterns before.

**Vivek Shankar:** We can dive into the webinar work now. Kyle, do you want to kick that off?

**Kyle Gaudreau:** Good to see you again. I had a chance to look at the feedback I sent yesterday. I can see some value in what you showed if I'm interpreting it correctly, but I wasn't sure if it was really hitting the complexity and scale we were trying to solve for. Let me walk through this at a high level. For reference, one of our clients — Adventures Group — might have an article with almost 10 images. The goal isn't just finding any images, it's finding ones that are highly relevant to specific sections within the article. So the question is: could we build something that understands both the high-level topic and the context within each article section to suggest and place the right images? That would have real wow factor. I'm curious if the approach you presented could evolve in that direction, or if I'm misinterpreting your vision.

**Miles Gordenker:** That feedback doesn't surprise me at all. We actually covered it on our first call — the workflow of someone searching for images is cool but doesn't have enough wow factor for a full webinar. But I came prepared with how I think this could work with minimal effort on our end because the use case does seem compelling. Even beyond your ICP, the workflow of taking text, enhancing it with images, and publishing it is pretty universal across industries. Let me show you a low-fidelity prototype of how we could build this in Datagrid.

The idea is: figure out what's absolutely needed for the webinar and what high-ROI additions we could include without too much effort. I put together a sample dataset with articles in a spreadsheet view. Once they're in the system, users can use AI agents to transform the data. So imagine an agent with access to a stock photo library that analyzes each article and suggests relevant image passages, then outputs multiple options per passage in a blog-friendly format. And I think the critical insight is that your audience won't trust AI blindly — they've probably been burned by hype before. So we need to give them an easy review and approval workflow. The agent suggests passages and image options, the user reviews in context, approves, and then it publishes.

**Kyle Gaudreau:** So if there were five sections in an article, you'd have columns for passage one, passage two, et cetera, with image options next to each?

**Miles Gordenker:** Exactly. And we can control this tightly or let the agent do it dynamically. I'm not sure yet what prompt will perform best or what column count balances comprehensiveness and accuracy, but I think we can set it up to resonate with your audience.

**Kyle Gaudreau:** And then we could add a wrap-up column at the end to bring it all together?

**Miles Gordenker:** Yes. A wrap-up column where the user specifies the output format and the system generates the final article. We could also showcase interactive agent refinement — if the user doesn't like selections on a specific row, they can tweak the prompt and hit re-run to regenerate just that row.

**Kyle Gaudreau:** The big question is how do we get it from the spreadsheet to actually published on their website generating clicks? And specifically, how do we close the loop between selecting images and getting the article live?

**Miles Gordenker:** That's a good topic to explore. As an intermediate step, we could set up a column that emails the draft article to a human for approval and manual upload to their CMS. And depending on ROI and conversion probability, I'd be willing to check with Tiago and our engineering team about building a proof-of-concept for Webflow draft uploads, since Webflow seems to be your most dominant CMS.

**Kyle Gaudreau:** That could be really valuable. I also want to stress-test this and see if we can dogfood it with our own content for Datagrid. We've discussed Adventures Group as a use case, but we could also show how we're using this to scale our own content. The stock photo angle is a limitation for your brand, but we could demonstrate how we applied this to our own workflow.

**Miles Gordenker:** Definitely an opportunity. I think the lowest hanging fruit is quality control — making sure standards are met. We demo this to customers a lot: put text in one column, then create AI columns to grade or score based on criteria. We could have Thiago apply his content standards to your generated articles using our existing connectors.

**Kyle Gaudreau:** So we could pull articles from Google Drive and have Tiago quality check them that way?

**Miles Gordenker:** Exactly.

**Kyle Gaudreau:** I know you've done webinars in the past. How do you typically promote and run them?

**Kaitlin Quimby:** We've sent emails to customers, done email campaigns and LinkedIn posts. Our last webinar had 200 signups and we put it together in about 2.5 weeks. I posted on LinkedIn, people reached out, I sent invites and messaged everyone. We sent a few reminder emails beforehand. We used Zoom Webinar as the platform, and the link just goes straight to Zoom — we were going to set up a HubSpot landing page for tracking but went with direct links instead.

**Kyle Gaudreau:** When would be a good time to test this workflow and get hands on to see if there's additional feedback?

**Miles Gordenker:** Whenever you want really. The core functionality is there. I'd expect some bugs and edge cases. Before we promote, we want to make sure we have all the functionality we need — especially the ability to email a completed article to someone for approval. We can set you up with an account with unlimited credits so you can play around.

**Kyle Gaudreau:** I think our team account already has limited credits. Can you set up a schema in our Datagrid instance and invite us?

**Miles Gordenker:** I'm running this in our dev instance so I can't send it directly. But I can either set up a Google Sheet with the schema or, even better, you invite me into your instance and I'll create the table and populate the skeleton.

**Jimmy Pal:** I was helping Marcel back in the day with his GrowthX community. Do you guys push people to a Slack community where they build workflows and share use cases? That could be good marketing collateral.

**Miles Gordenker:** We have a Slack community but haven't promoted it aggressively.

**Jimmy Pal:** That could be really powerful. Give people templates and use cases, let them build on their own, and then you'll get people posting about how GrowthX workflows benefited them — great material for Tiago and your team to repost on LinkedIn.

**Miles Gordenker:** I think the next steps for me are clear. We'll send you an invite and get this set up.

**Kyle Gaudreau:** We want to make sure we stay on timeline and don't push the date back too far. We'll start testing where we can. But Jimmy, anything on link building we should cover today?

**Jimmy Pal:** Link building is business as usual. New links have been added to the tracking table, nothing new beyond that.

**Kyle Gaudreau:** Kaitlin, anything else we should cover?

**Kaitlin Quimby:** I think we just need to get a date on the calendar sooner than later for the image selection webinar. And we also want to plan the second webinar topic.

**Miles Gordenker:** We probably want to find another topic because this one is pushing the boundaries of what's possible and will take some work. Maybe something closer to what's possible today?

**Kyle Gaudreau:** Are you trying to get to monthly webinars or what cadence are you thinking?

**Kaitlin Quimby:** Every six weeks would be ideal.

**Kyle Gaudreau:** Got it. Well, thanks for the time. Let us know if anything comes up, but we'll start testing and send you feedback.

**Kaitlin Quimby:** Thank you. Bye everyone.
