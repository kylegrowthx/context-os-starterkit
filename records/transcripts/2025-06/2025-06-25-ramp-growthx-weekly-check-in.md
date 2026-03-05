# Ramp<>GrowthX Weekly Check-In

<metadata>
date: 2025-06-25
time: 18:01 UTC
duration: 13 minutes
organizer: vivek@growthxlabs.com
participants: Mara Leighton, Vivek Shankar, Nika Narimanidze, Bisera Stankovska, Matt Angelosanto, Victoria Naef
fathom_recording_id: 70531267
fathom_url: https://fathom.video/calls/334419890
share_url: https://fathom.video/share/z6uKXzbo2KSdbo1bDMgNu4cpCV2tZn6X
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX's content performance for Ramp remained stable across most page categories, with 34 new vendor pages ready for publication and ongoing work on CRM and AI pages targeting delivery by June 27. Vivek reported stable blog performance, slight declines in per-diem pages (attributed to Travelperk's improved UX), and continued struggles with the expense category following a ranking update. The team identified table rendering in Sanity CMS as a persistent technical challenge—requiring a workaround that Mara engineered—and agreed that Matt would follow up with Luke on exploring HTML/markdown copy-paste solutions to streamline future table implementation.

---

## Context

Ramp is a B2B fintech expense management platform, and this meeting is part of GrowthX's ongoing content marketing engagement. GrowthX created and maintains a content hub for Ramp covering topics like per diem policies, expense categorization, cash flow statements, and vendor-specific guides (e.g., Shopify, DevOps tools, web hosting). The recurring weekly check-ins allow the two teams to review content performance metrics from Ramp's website, track progress on newly published pages, address publishing bottlenecks, and align on upcoming deliverables. Luke Tubinis typically leads on Ramp's side but did not attend this particular meeting; Victoria Naef and Matt Angelosanto represented Ramp's web engineering and editorial interests.

---

## Relevance

**To GrowthX Delivery:**
- Content hub scale-up proceeding smoothly: 34 vendor pages queued for publication by Friday (June 27), with new pages like DevOps already attracting traffic. CRM and AI pages on track for delivery by June 27 (deadline noted as "B27").
- Sanity CMS table rendering remains a structural blocker. Mara's manual workaround is not repeatable; Matt indicated the solution likely requires HTML or markdown copy-paste support—a 2-month backlog item for Ramp's web engineering team. Follow-up with Luke Tubinis needed.
- Editorial reflection work (2 pieces in progress) competing with vendor page publishing, but tone calibration toward "center" is improving. Sample 5 articles being reviewed with focus on consistency.

**To GrowthX Business Development:**
- Account health: High production velocity (34 pages + 2 editorials + new batch of 2 pages = significant output) signals strong team alignment and project momentum. Ramp team expressing gratitude for last week's high-effort table implementation work.
- Expansion signal: Audience segments are diversifying (blog, per-diem, expense, tuning, treasure, vendor pages covering multiple use cases). Sample 5 articles and tone refinement suggest content strategy maturity.
- Renewal/retention: Technical friction (Sanity CMS limitations) being treated seriously; both teams working toward infrastructure improvements to enable faster publishing.

---

## Overview

- Content performance remains stable across most page types, with slight fluctuations in specific areas
- Progress on vendor pages and editorial reflections is on track, with 34 new pages to be published by Friday
- Table formatting in Sanity CMS remains a challenge; web engineering team is working on a solution
- Automation of vendor page publishing process to resume next week after internal projects wrap up

---

## Key Topics

### Content Performance Overview

  - Blog pages: Sessions held steady, consistent with recent trends
  - Per-diem pages: Slight drop, potentially due to Travelperk's UX improvements
  - Expense category: Continuing steady decline, limited options for improvement
  - Tuning pages: Session jump, driven by cash flow statement blog performance
  - Treasure pages: Maintained usual range
  - Vendor pages: Sessions stable, new pages (e.g., DevOps) gaining traction

### Ongoing Projects and Updates

  - Two editorial reflections in progress, balancing with vendor page creation
  - Sample 5 articles being sent, aiming for a more centered tone
  - 34 vendor pages to be published by early Friday
  - Data wrapper IDs received and implementation begun
  - Overview pages for content creation and web hosting under review
  - Shopify page drafted without line chart, as requested
  - CRM and AI pages on track for delivery on B27

### Table Formatting in Sanity CMS

  - Current method for rendering tables is complex and not easily replicable
  - Web engineering team exploring solutions for 2 months
  - Potential future solution: HTML or markdown copy-paste for entire tables
  - Matt to follow up with Luke on progress and potential editor changes

### Vendor Page Publishing Automation

  - Project temporarily slowed due to internal audit and other projects
  - Full-speed work to resume early next week
  - Team anticipates progress updates soon

---

## Action Items

**Matt Angelosanto (Ramp)**
- Follow up with Luke Tubinis re table component issue in Sanity CMS. Explore HTML or markdown copy-paste solution to enable easier table publishing.

---

## Transcript

**Mara Leighton:** But I love how collaborative they are. Yeah, how's it going?

**Vivek Shankar:** Hello, I'm good.

**Victoria Naef:** How are you? Doing well.

**Mara Leighton:** I'm in San Francisco for a director on site this week, which is why you'll see this comically large whiteboard behind me, full of ideas. Yeah, it's a good week.

**Victoria Naef:** It's a good week to escape New York. So it's very good.

**Mara Leighton:** I should have asked you first and foremost, like, are you sweltering? Are you surviving? It was 95 when I left, and I think it's above 100 today?

**Victoria Naef:** It was above 100 yesterday, too, but I'm spending most of the time inside on the AC, so I'm good.

**Mara Leighton:** I think I went to the post office on Monday, and I was like, oh, this felt like a marathon. Like, I've been walking for a million years.

**Victoria Naef:** The walk from the train here is super fast. I was already sweating.

**Mara Leighton:** You just feel so fatigued, which is so, like, that plus, like, the grind of New York City is just, like, really takes it out of you.

**Mara Leighton:** Matt, how are you doing?

**Matt Angelosanto:** I am well, thanks. It is also hot in Boston.

**Matt Angelosanto:** I don't think it's quite as hot as New York. I read recently that New York City's climate was upgraded, if you want to call it that.

**Matt Angelosanto:** Too bad for us.

**Mara Leighton:** Well, I think Luke is not joining today, just based on the participants we have here. So we can probably just get started.

**Victoria Naef:** All right, let me share my screen.

**Vivek Shankar:** Before we begin, I do want to know, what does weather getting upgraded mean?

**Matt Angelosanto:** Yeah, there's, I believe it's related to hardiness zones. So certain plants can survive under certain conditions, and so they categorize those hardiness zones slightly differently. So there's an alphanumerical range, but then there's also a range that's based on general weather patterns—humid continental, humid subtropical, and tropical and subtropical. I think it has to do with the general climatic trends over time. The implications are how comfortable it is as a person, but also what plants can actually survive there. So now in New York, probably some warmer weather plants would be able to survive. We were looking into this recently because we do a lot of gardening, but I could probably look it up and let you know if you're interested.

**Mara Leighton:** I didn't expect you to have such a thorough summary. If I ever end up with outdoor space in New York, I will get a little subtropical plant and we can see how she does.

**Vivek Shankar:** So, diving quickly into the performance side of things. Generally, overall, all types of pages held their usual performance range with no major changes. The blog pages held pretty much the same as last week and in the range we've been seeing for a while. The per-diem pages had a slight drop, mainly because of Travelperk hopping ahead of us based on their UX design improvements.

**Vivek Shankar:** Expense category, unfortunately, is continuing to steadily decline. We're still ranking for the core search terms, but there's not much we can do with these pages at this point—it's just one of the consequences of the update that happened last month.

**Vivek Shankar:** With the tuning pages, we saw a jump in sessions back into the usual average. Most of it was driven by the cash flow statement blog performing quite well. Cash flow statement and LIFO received quite a bunch of views. The second batch of tuning pages saw quarterly taxes jump up—not quite sure why it's jumping in June, but there we go.

**Vivek Shankar:** Treasure pages held in the range we've been seeing with no major changes observed. For vendor pages, sessions held pretty much the same as last week. Some of the newer pages got some hits. We had the DevOps page receive about four sessions, so that's pretty nice. Generally, it seems like things are taking shape as we publish and generate more of these pages.

**Vivek Shankar:** We're working on two editorial reflections this week. We're balancing these pages along with the vendor pages. We're sending over the Sample 5 articles, and we want to be a little conscious of the tone. We've been swinging a bit back and forth. We just want to land in center now, so that should help.

**Vivek Shankar:** The vendor page updates: we've begun working on publishing the 34 pages and expect to get done early Friday. Thanks, Victoria, for sending over the data wrapper IDs. We've already got started on those. I think we staged them, and Nika is reviewing a bunch of them as we speak. The overview pages are done for the content creation and a few for web hosting.

**Vivek Shankar:** We've addressed all edits. The Shopify page has been drafted, and we didn't include the line chart—it just has a pie chart. We checked the other pages for any sort of negative sentiment. We didn't find any. Everywhere the tone was pretty neutral, so pretty good on that.

**Vivek Shankar:** The new batch of pages to generate—the CRM and AI pages—we will deliver those on B27. So that's going pretty well. Any questions?

**Victoria Naef:** No questions, that's all clear and sounds good. I also wanted to acknowledge and thank you guys for publishing all those pages last week. There were lots of tables, so lots of work there, and I sent more pages than I did initially, so thanks. It was good.

**Mara Leighton:** There were a lot of tables, but that's completely fine. It was just a fun exercise for us.

**Vivek Shankar:** Mara figured out how to get the tables to render properly using this bizarre method that will never be replicated again. He was sending a bunch of looms in the thread like, hey, I think this works. We learned a lot about Sanity, for sure.

**Mara Leighton:** It's that or take up Sudoku, and I don't really like Sudoku. So this was a perfect little mental brain teaser.

**Vivek Shankar:** I had tagged Luke on maybe getting HTML or JSON access so that we could just pop those tables in. We couldn't find a way of doing it, sadly. But then Luke mentioned the editor maybe needs changing, so that could follow up with them in thread. Just wanted to surface that.

**Matt Angelosanto:** You can import JSON directly into Sanity through a CLI, but it does kind of defeat the purpose of using a component-based CMS because all of the styling is tightly scoped to the individual components. This has been on our web engineering team's board for like two months because it's not quite as simple as it seems. A table component for Sanity or Contentful just kind of sucks. The biggest issue is the use of Sanity's inbuilt rich text editor in the table component. The next solution is probably going to be some sort of HTML or markdown copy-paste where we can just drop the entire table in all at once. I will follow up with Luke on that. I'm meeting with him immediately after this.

**Vivek Shankar:** Yeah, I think it's not an issue for the editorial articles. It's not so much for the vendor pages, but we are still kind of working away at automating the publishing process for the vendor pages. We've been having a few internal projects going over the past couple weeks, including the internal audit. We're just coming off that and we should be full speed ahead on that early next week. That's pretty much it for the update this week.

**Victoria Naef:** Awesome. Thanks so much.

**Mara Leighton:** Great to see you guys. Same for you, Matt. I think the heat's supposed to be over tomorrow, right? So, fingers crossed.

**Matt Angelosanto:** That's what I've heard.

**Mara Leighton:** That's what they've promised.

**Victoria Naef:** Enjoy San Francisco, Mara.

**Mara Leighton:** Thanks so much. Appreciate it.

**Victoria Naef:** Thanks, Mara. Bye, guys.
