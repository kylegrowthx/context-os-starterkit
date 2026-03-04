# Dimmo <> GrowthX Weekly Sync

<metadata>
date: 2025-05-15
time: 19:03 UTC
duration: 25 minutes
organizer: Prateek Gupta (GrowthX)
participants: Prateek Gupta (GrowthX), Troy Munson (Dimmo), Lucas Swartsenburg (Dimmo)
fathom_recording_id: 62937985
fathom_url: https://fathom.video/calls/300279135
share_url: https://fathom.video/share/Hra_2yaay4kiPDNASDzeo_3TJk9inoyp
source: fathom
enriched_on: 2026-03-04 12:00 UTC
</metadata>

---

## Summary

GrowthX and Dimmo aligned on resolving content quality issues caused by UI presentation problems (spacing and bullet point formatting) rather than content itself. The team has published 30 product review pages (targeting 45 more this week) out of a planned 90 total, with SEO showing early gains: 2 keywords now ranking in top 3 and 25 in positions 11-20, though clicks remain flat at 20/week. Key technical priorities include fixing bullet point display, implementing 301 redirects from blogs to product pages, adding listing pages for content clusters, and preserving formatting when copying content from CMS to Strapi CMS.

---

## Context

Dimmo is a B2B SaaS platform in the review/comparison space. GrowthX is executing a 14-week content engagement creating 200+ product review articles (15/week) to drive organic search traffic. This weekly sync reviews content publishing progress, SEO performance, and technical blockers that affect the publishing workflow. Previously, Troy had flagged concerns about content quality, but the conversation clarified that the issue was primarily visual presentation (tight spacing, missing bullet points) rather than the actual written content. The team is balancing content volume with UI/UX improvements and internal linking strategy to maximize SEO impact once product pages fully launch.

---

## Relevance

**To GrowthX Delivery:**
- Content publishing process is inefficient (45 mins/page) due to formatting loss when copying from CMS to Strapi. Prateek asked Lucas to investigate preserving H2, H3 headers, and bullet points during copy-paste operations.
- UI fixes (spacing, bullet points) are low-effort wins that significantly improve readability. Simple design tweaks with adequate paragraph spacing yield stronger visual impact than content rewrites.
- SEO strategy focus is shifting toward product pages as primary traffic drivers rather than blog-based approaches; internal linking and listing pages are critical infrastructure for discovery.

**To GrowthX Business Development:**
- Dimmo appears healthy and collaborative; strong momentum on publishing 30 pages in 2 weeks clears backlog.
- Client responsiveness and quick iterative improvements (Lucas fixed bullet and "Read More" button issues mid-call) suggest good working relationship.

**To CheckThat:**
- Not discussed in this meeting.

---

## Overview

- Content quality concerns traced to UI presentation issues (spacing, bullet point rendering), not the written content itself; Lucas is rolling out fixes
- Publishing progress: 30 pages live (clearing 2-week backlog), 60 more pending in pipeline, targeting 45 additional pages live this week
- SEO performance: 2 keywords now ranking top 3 (up from 0), 25 keywords in positions 11-20, but click volume remains flat at 20/week despite ranking improvements
- Critical workflow bottleneck identified: 45-minute publishing time per page due to formatting loss when copying from CMS to Strapi; Lucas to investigate preservation solutions
- Technical priorities: 301 redirects (blog to product pages), listing pages for content clusters in footer, internal linking implementation, content backup before deletion

---

## Key Topics

### Content Quality and UI Improvements

Prateek's initial concern about content quality turned out to be a visual presentation issue rather than written content. The problem: paragraphs and bullet points were too tightly spaced and bullet formatting wasn't rendering correctly despite being in the CMS. Troy shared a reference page showing proper spacing between title and content sections. Lucas immediately began fixing the bullet point display and spacing issues during the call, with updates rolling out live. The team agreed the simplified version (with a "Read More" for expanded content) is the right approach to avoid duplicate content while providing enough value that users don't need to click through.

### Content Publishing Progress

  - 30 pages published in the last two weeks (2 weeks of backlog cleared)
  - 90 product reviews total: 30 live, 60 pending
  - Targeting 45 more to go live this week
  - Total content approaching 200 articles (15/week pace)

### SEO Performance

  - Slight improvements in keyword rankings:
      - 2 keywords now in top 3 positions (up from 0)
      - 25 keywords in positions 11-20
  - Clicks remain stagnant at 20/week, 75,000 impressions/week
  - Focus on improving product page rankings to drive relevant traffic

### Technical Improvements Needed

  - 301 redirects for blog posts to product pages (list to be provided)
  - Create listing pages for Software Alternatives and Software Features clusters
  - Add listing pages to website footer for improved indexing
  - Internal linking implementation pending
  - Backup of old content before deletion
  - Streamline content publishing process (currently 45 mins/page due to formatting issues)

### CMS and Publishing Workflow

  - Webhook trigger process explained for pushing CMS updates live
  - Content formatting loss when copy-pasting into Strapi CMS identified as major time sink

---

## Action Items

**Lucas Swartsenburg (Dimmo)**
- Fix bullet points not displaying correctly on product pages (in progress; rolling out during call)
- Remove "Read More" button when no long-form content exists (completed during call)
- Create listing pages for Software Alternatives and Software Features clusters
- Add links to new listing pages in website footer
- Implement internal linking for product pages
- Create backup of existing content before further deletions
- Investigate ways to preserve formatting (H2, H3, bullet points) when copying from CMS to Strapi CMS (major workflow bottleneck at 45 mins/page)

**Prateek Gupta (GrowthX)**
- Create list of blog posts needing 301 redirects to product pages (~15 URLs minimum)
- Update Slack channel with complete list of technical needs for Lucas

**Troy Munson (Dimmo)**
- Coordinate with Lev on creating overview/listing pages and internal linking tasks

---

## Transcript

**Prateek Gupta:** First thing that I'm worried about is on the content side. Troy, you had mentioned something about not being happy with the content quality. So that's something which we can definitely take up. Before we move on to the normal agenda, can we discuss that? The reason why I asked is because we have written almost 60, 80 articles already completed.

**Prateek Gupta:** If needed, I can revamp. That's not the concern, but we can finalize on the approach before we move ahead. Let's take that up first. Yeah, the way the pages should look.

**Troy Munson:** Is that what you're talking about? Maybe I'm wrong. I thought what we agreed on was the very simplified version and then the larger version.

**Prateek Gupta:** Yes, that's the approach. You wanted to make sure the simplified version covers everything so people don't have to always click on the "Read More" version. That was my main reason. And the second reason is I didn't want people to feel like the simplified version is just small bullet points and they always have to click "Detail" or "Read More." So I also try to give them a paragraph or summary so they don't always have to look at the detailed version. I'm trying to avoid people clicking on the detailed version. The shorter version should do it justice. That was the whole idea behind it.

**Prateek Gupta:** Let me just share my screen for now.

**Lucas Swartsenburg:** Okay.

**Prateek Gupta:** Is my screen visible? It's not loading. It's a screen sharing issue. I had this problem the other day, Lucas.

**Lucas Swartsenburg:** Yeah, it's visible now.

**Prateek Gupta:** Perfect.

**Prateek Gupta:** So this was the final version we discussed initially. We'll have a shorter version with a "Read More." In the pricing section, we just mention the plans like Essential, Advanced, Professional, Enterprise in the shorter version to avoid duplicate content. The idea is to give them a quick summary. The enterprise plan starts from $14 and goes up to $70. Then there are some add-ons. So this gives them additional content compared to the simplified version. In the simplified version, we just give them the plan details but not what they get from each plan. Here we also give them extra things like leads, boosters, and those kinds of add-ons. So that's the difference. More importantly, which one would you prefer? To be honest, the simplified version is easier to create. This one is tougher. But we thought if this gives more value to the visitor, that's why we opted for it.

**Troy Munson:** Yeah, no, that all makes sense.

**Lucas Swartsenburg:** Hold on, I'm trying to go to a page right now.

**Troy Munson:** I looked at it and I just think to my eye it didn't look appealing from a UI perspective.

**Prateek Gupta:** I think that might be on us, to be honest.

**Troy Munson:** We might need to change how that looks. I know we need to delete our summaries and company overviews. Are they already deleted, Lucas?

**Lucas Swartsenburg:** Lev tackled all that stuff the other day.

**Troy Munson:** Awesome. So there are a couple of things we need to do.

**Prateek Gupta:** For example, I had put bullet points here. The bullet points are not coming in despite putting them in the CMS. That's an issue I called out. Here, it's mine and the publisher's mistake. We added single space whereas we should have added double space. We should have added more space between paragraphs. Currently it looks very stacked up because there's no space added between paragraphs. That's why it doesn't look right.

**Troy Munson:** Yeah, that's it. It's almost like I can't focus on it because it's too much. That's what I was thinking, maybe we should go with the bullet point approach. But I know what you mean, give them just enough so they don't always need to click. I totally understand. With a few fixes here and there it'll look a lot cleaner. We used to reference this page all the time. I'm going to send it in the chat. This is what we modeled it after.

**Troy Munson:** Yep.

**Troy Munson:** Um.

**Troy Munson:** Um.

**Troy Munson:** Uh, yeah, you.

**Troy Munson:** Yeah.

**Troy Munson:** Um, um, Thank

**Troy Munson:** But yeah, it looks, it just looks easier to read.

**Prateek Gupta:** Way easier to read because there's a lot of space here.

**Troy Munson:** Yeah, they do a space between the title and the word and like the, like they do like one little sentence and then some bullet points.

**Troy Munson:** Yeah.

**Troy Munson:** And so like that's, I think like that's it.

**Troy Munson:** really seems like, and I think that's just a UI thing and how we do, how we present it on the front end possibly.

**Prateek Gupta:** So here, for example, here, for example, if you see, I've added here bullet points, but these bullet points, I'm not sure why they're not getting translated in this on the UI side.

**Prateek Gupta:** On the back end, if you see there are bullet points here.

**Prateek Gupta:** Okay, Lucas, that's something that we'll need to look into.

**Troy Munson:** We can get Lev to possibly do it as well.

**Troy Munson:** We can have him knock that out soon.

**Troy Munson:** Yeah, I'm updating it right now.

**Lucas Swartsenburg:** And what I can do is I can add some spacing here.

**Prateek Gupta:** Maybe this is fine.

**Troy Munson:** For you right there, like that looks like what I'm looking at looks like how I would imagine it looking and how I, yeah.

**Troy Munson:** So like yours is, yeah, yours is set up correctly.

**Troy Munson:** Well, Lucas will fix that.

**Troy Munson:** And those spaces definitely look good too.

**Prateek Gupta:** Yep.

**Prateek Gupta:** It's just a spacing issue.

**Prateek Gupta:** I guess I should have that fixed.

**Prateek Gupta:** Yeah.

**Prateek Gupta:** This looks good.

**Troy Munson:** Okay. Looks good.

**Prateek Gupta:** Also, Lucas, I wanted to check on something. For example, for an intro, the intro does not have any long form content. Is it possible to give me flexibility to disable long form content if I want? So if a particular section like the intro and conclusion don't have long form, when I click "See Detail" it becomes empty. Is there an option where I can just remove that button or disable it so it doesn't show up?

**Lucas Swartsenburg:** Yeah, I can do that.

**Prateek Gupta:** Good. Apart from that, we published almost all articles this week, so we covered a lot of backlog—two weeks of backlog we covered. We still have two weeks of backlog left but we should be able to cover it this week. That's on the publishing side. So a couple of other things I wanted to discuss. Let me backtrack. I also wanted to talk about the 301 redirects for the blogs. All the blogs where we have written about product pages, we're doing a 301 redirect from them to the product pages. If you're confused about it, I can restart that conversation.

**Lucas Swartsenburg:** So 301 redirects.

**Prateek Gupta:** It's from blog post to product page. Do you have a list of the ones we're doing?

**Lucas Swartsenburg:** If you have that list, I can easily create the redirects.

**Prateek Gupta:** I can create that list. I'll get it done. There are some existing pages we missed doing a 301 redirect on. They're still in the blog folder but they should be going to the new Software Alternatives folder instead.

**Lucas Swartsenburg:** Sounds good.

**Prateek Gupta:** I'm also facing some challenges on the indexing side. Can we link our content clusters from the footer? We've created two clusters: Software Alternatives and Software Features. I'm thinking if we can create a listing page where we list all articles under those clusters and then link that listing page in the footer.

**Lucas Swartsenburg:** Yep.

**Prateek Gupta:** Here's an example from another client we're working with. They have clusters for answering surveys and appointment scheduling. We created a listing page and listed all 100 appointment scheduling articles. That boosted their indexing significantly.

**Lucas Swartsenburg:** Can you make sure it's added to my notes and to-do list?

**Prateek Gupta:** Yeah, I'll do that. Any update on the internal linking?

**Lucas Swartsenburg:** No, I haven't worked on that yet, so I'll work on it soon.

**Prateek Gupta:** Okay. I'll share all this in the notes. I need help with about 15 URL redirects. I'll create a list of all the blog pages that should redirect to product pages. I'll add to the notes the footer linking pages creation and internal linking tasks and the product page UI fixes with the bullet points.

**Prateek Gupta:** We've published all 30 pages this week—two weeks of content cleared. Pages include Hunter.io features, Outreach, Apollo, Templatemonster reviews. Lucas, my only request is if one of you could review them from the CMS backend once to say everything is good.

**Lucas Swartsenburg:** If the product pages are appearing correctly, it should be fine. I don't think there's anything I need to check.

**Prateek Gupta:** Good. One thing—I'm deleting old content while publishing. Are you finding that I'm losing any content or having issues?

**Lucas Swartsenburg:** No, it's all good. But do we need to make a quick backup before we delete the old content?

**Troy Munson:** Yeah, I think we should do a backup just in case.

**Lucas Swartsenburg:** I'll work on that.

**Prateek Gupta:** Perfect.

**Prateek Gupta:** I'll give you a list of all the tech support I need. In terms of our activities, as part of our 14-week engagement we're doing 15 articles per week, hitting the 200-article mark. Out of those, 90 are product reviews. So far 30 have gone live, 60 are pending including this week. We should be taking close to 45 live this week. Before our next call, I'll try to cover as much backlog as possible.

In terms of performance, here's the keyword ranking data. From April 27 to May 3 we were ranking for zero keywords in the top three. Right now we have two keywords ranking in the top three—that's some improvement. In positions 4-10, we have one keyword. In positions 11-20, we have 25 keywords. But despite keyword ranking improvements, we haven't seen a great increase in clicks. Clicks are stagnant at 20/week with 75,000 impressions per week. The two keywords in top three are "Best virtual selling software" and "Maximizer features." We should see better clicks and performance in coming weeks as product reviews go live.

**Troy Munson:** I would have never guessed those two keywords.

**Prateek Gupta:** Yeah, I know Maximizer CRM, but I'm shocked.

**Troy Munson:** Maybe they do good marketing and people are looking at Maximizer features. They're not a really popular tool though.

**Prateek Gupta:** Also, look at this quick question.

**Prateek Gupta:** Once I update the CFS here, how long does it take for it to get updated on the life?

**Lucas Swartsenburg:** So there's another like when you're done with that, there's like a webhook that you need to trigger.

**Lucas Swartsenburg:** If you go to the settings, so the radar thing on the left side, yeah.

**Lucas Swartsenburg:** And then you go to webhooks, is it here, right?

**Lucas Swartsenburg:** Yeah, webhooks.

**Lucas Swartsenburg:** Okay, where is that?

**Prateek Gupta:** It's in the menu bar on the left.

**Prateek Gupta:** Okay, so this is on.

**Prateek Gupta:** Fathom, yeah.

**Lucas Swartsenburg:** And then redeploy.

**Lucas Swartsenburg:** Where is the, yeah, this one.

**Prateek Gupta:** Yeah.

**Prateek Gupta:** What should I do?

**Prateek Gupta:** Should I just click it?

**Prateek Gupta:** What should I do?

**Prateek Gupta:** Yeah.

**Troy Munson:** Click it and then top right do trigger, I think it says something like that.

**Troy Munson:** Oh, don't check it.

**Troy Munson:** Just click it.

**Lucas Swartsenburg:** Yeah.

**Prateek Gupta:** Okay.

**Lucas Swartsenburg:** And then right top corner, there's a button called trigger.

**Lucas Swartsenburg:** Yeah.

**Prateek Gupta:** That doesn't.

**Lucas Swartsenburg:** And you can also just take that URL that you see there.

**Lucas Swartsenburg:** Yep.

**Lucas Swartsenburg:** Okay.

**Lucas Swartsenburg:** Okay.

**Lucas Swartsenburg:** Thank

**Lucas Swartsenburg:** Do that one?

**Lucas Swartsenburg:** If you enter that in a menu bar, you just copy paste it in a URL bar.

**Lucas Swartsenburg:** That's it.

**Lucas Swartsenburg:** And then it will take three to five minutes after you do that for the new page to be live.

**Lucas Swartsenburg:** Got it.

**Prateek Gupta:** Perfect.

**Prateek Gupta:** Thank you.

**Prateek Gupta:** It's very important.

**Prateek Gupta:** Another thing, one major challenge what I'm facing while developing is, I wanted to share is, whenever I copy paste the content from our CMS to the Stapi, let me go back to those pages.

**Prateek Gupta:** Okay.

**Prateek Gupta:** Yeah.

**Prateek Gupta:** So whenever I just copy.

**Prateek Gupta:** Okay.

**Prateek Gupta:** Yeah.

**Prateek Gupta:** Whenever I copy paste, what happens is the bullet points and everything and the.

**Prateek Gupta:** H2, H3.

**Prateek Gupta:** They disappear.

**Prateek Gupta:** So is there an option where if I paste those things?

**Prateek Gupta:** Because what happens is each time, whenever I copy paste, I have to re-tag it as an H2, H3.

**Prateek Gupta:** I have to re-put the bullet points.

**Prateek Gupta:** So it's taking me at least 45 minutes to publish one page.

**Prateek Gupta:** Oh, that's awful.

**Lucas Swartsenburg:** Before you do that, I can take a look to see what we can do.

**Lucas Swartsenburg:** Yeah.

**Prateek Gupta:** Generally, across others, what we are doing is we are just publishing within five minutes max.

**Prateek Gupta:** It takes here because we have a lot of content, we need to put it in the short version, long version, we have to put it and then we have to put the heading.

**Prateek Gupta:** So what happens is if I take any content and I paste, this heading does not get, the structure does not stay the same.

**Prateek Gupta:** And I have to every time select it as an H2, H2.

**Prateek Gupta:** We have to always put the bullet points manually.

**Prateek Gupta:** It also causes human errors.

**Prateek Gupta:** Plus what happens is it takes almost 45 minutes to do one.

**Prateek Gupta:** Yeah, add it to the list and I'll see what I can do.

**Lucas Swartsenburg:** Perfect.

**Lucas Swartsenburg:** OK.

**Prateek Gupta:** Lucas, get left on an example of these?

**Troy Munson:** Sounds like a lot.

**Lucas Swartsenburg:** Yeah, we can.

**Lucas Swartsenburg:** Yeah, I just fixed the bullet points right now.

**Prateek Gupta:** Yeah, I'm adding.

**Lucas Swartsenburg:** I'm rolling that out right now.

**Lucas Swartsenburg:** And I fixed the "Read More" button so it shouldn't appear when you don't have any long text.

**Prateek Gupta:** Perfect.

**Prateek Gupta:** Maybe next week I can sit with you for half an hour to get all the fixes done. I'll get you a coffee or something.

**Lucas Swartsenburg:** Beer is the way to go if you want me to get work done!

**Prateek Gupta:** I'll post a list in Slack of everything I need help with. If you have any doubts, let me know. I'm happy to connect quickly and get it done.

**Lucas Swartsenburg:** Yeah, the one thing I could use help with Troy and Lev is creating that overview listing page and the internal linking tasks.

**Prateek Gupta:** Yeah, we'll talk about that tomorrow. Sounds good. Alright, let's wrap up. Thanks everyone.
