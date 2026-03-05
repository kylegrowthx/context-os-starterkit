# Rapyd <> GrowthX Weekly Sync

<metadata>
date: 2025-04-30
time: 17:31 UTC
duration: 37 minutes
organizer: aida@growthxlabs.com
participants: Jakub Rudnik (GrowthX), Rachel Pasche (GrowthX), Aida Knežević (GrowthX), Kristin Reischel (Rapyd), Marc Winitz (Rapyd), Mark Stiltner (Rapyd), Francine Harris (Rapyd), Nicolette M. (Rapyd)
fathom_recording_id: 60084474
fathom_url: https://fathom.video/calls/287904272
share_url: https://fathom.video/share/R-qTMdat1NTgH1uUpxuevKQasyAzfEy7
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

Rapyd and GrowthX discussed a comprehensive blog content audit—identifying ~400 URLs for review with 27 already marked for redirection—aimed at improving SEO performance by removing outdated/irrelevant content and consolidating related pieces. The team outlined an automated publishing workflow using WP All Import and XML files to increase publishing velocity to 8 articles per week (~50,000 words monthly), with GrowthX's new Chief Content Officer (Matthew Panzarino, formerly of TechCrunch) supporting workflow improvements and content quality. Early momentum is visible: 7 newly published pieces generated 4 clicks and 3000+ impressions in the first week.

---

## Context

Rapyd is a fintech platform serving the payment infrastructure space, and this is a weekly sync within an ongoing GrowthX content marketing engagement. Aida Knežević leads content delivery for Rapyd at GrowthX; she works with Rachel Pasche (editor), Jakub Rudnik (SEO strategist), and the GrowthX dev team to create and publish content. Rapyd's team includes Mark Stiltner (content reviewer), Kristin Reischel (team liaison), Marc Winitz (stakeholder), and others who provide feedback and assignments. The meeting centers on execution: the blog audit is designed to clean up years of accumulated content and establish a repeatable workflow that lets GrowthX publish more consistently while Rapyd's team members help with content review and relevance assessment.

---

## Relevance

**To GrowthX Delivery:**
- Blog audit playbook is reproducible: ~400 URLs assessed for relevance (Yes/Somewhat/No), then redirected or refreshed. Applied successfully at Active Campaign (700→600 blogs = 10-15% traffic lift).
- New publishing workflow using WP All Import + XML files removes WordPress staging bottleneck and scales to 8 articles/week (~50,000 words/month).
- Team-based content review model: distributing blog review across Rapyd's team by subject-matter expertise instead of centralizing in Mark Stiltner reduces bottleneck.
- Chief Content Officer (Matthew Panzarino) newly embedded at GrowthX to support workflow improvements and hiring for all delivery teams.

**To GrowthX Business Development:**
- Early-signal metrics visible: 7 new articles → 4 clicks, 3000+ impressions in week 1.
- Rapyd content strategy pivoting toward high-opportunity verticals (cross-border payments, payment infrastructure, niche industries) signals confidence in GrowthX's strategy.
- Account expansion potential: Rapyd asking about next-level optimizations (CTA variants, UK English consistency, GA4 integration) suggests room for deeper engagement on analytics and conversion.

**To CheckThat:**
- Rapyd's blog strategy now focused on specific product/vertical clusters; CheckThat audit of Rapyd's content visibility in AI engines would align with this narrower, more targeted approach.
- Discussion of content relevance decay and SEO strength aggregation (outdated content dragging overall domain authority) demonstrates Rapyd's sophistication around AI/SEO visibility.

---

## Overview

- Initiating blog audit to remove/redirect irrelevant content, potentially boosting overall SEO performance
- Implementing new automated blog ingestion process using XML files and WP All Import plugin
- Increasing publishing velocity by involving more team members in content review process
- Early traction seen in newly published content, with 4 clicks and 3000+ impressions in the past week

---

## Key Topics

### Blog Content Audit

  - Identified \~400 URLs for review, with 27 already marked for redirection
  - Goal: Remove outdated/irrelevant content to improve overall site SEO performance
  - Process: Quick assessment of relevance (No/Somewhat/Yes) for each URL
  - Next steps: Redirect obvious irrelevant content, then develop playbooks for refreshing/combining/updating remaining content

### AMP Page Deprecation

  - Recommendation to deprecate AMP (Accelerated Mobile Pages) versions of blog posts
  - Rationale: Improved site speed metrics, low AMP traffic (100 clicks in 3 months), reduced technical debt
  - Action: Mark to confirm with team and implement deprecation

### Content Performance Tracking

  - New performance report created in Google Data Studio
  - Shows early traction: 4 clicks, 3000+ impressions for 7 newly published pieces
  - GA4 data to be incorporated once analytics issues are resolved

### Publishing Workflow Improvements

  - New automated ingestion process using WP All Import plugin and XML files
  - GrowthX to output approved blogs as XML files for easier import
  - Kirkland (IT) to implement workflow in AirOps

### Content Review Process

  - Mark unable to review all content alone; recruiting team members for help
  - Kristin to provide list of team members and their subject matter expertise
  - Goal: Assign \~1 blog per week to each team member for review

### CTA Implementation

  - Generic CTAs provided by Mark are being added to new and recent blog posts

### Miscellaneous

  - UK English consistency to be double-checked in content generation process
  - Publishing target: 8 articles per week, \~1500 words each (50,000 words/month)
  - New Chief Content Officer (Matthew Panzarino) joined GrowthX, focusing on workflow improvements and content quality

---

## Action Items

**Mark Stiltner (Rapyd)**
- Review & categorize ~150 remaining blog posts for relevance (no/yes/somewhat)
- Redirect batch of ~20 blogs identified for removal
- Share content board with Vanessa Johnson (email provided in chat)

**Kristin Reischel (Rapyd)**
- Second-pass review blog posts Mark categorizes for relevance
- Provide list of team members' product expertise areas to Mark for blog review assignments

**Aida Knežević (GrowthX)**
- Add missing images to blog posts marked as ready

---

## Transcript
**Jakub Rudnik:** Let me make sure I didn't miss something from you, Mark. I took the original list. Stop me if I'm missing anything here.

**Mark Stiltner:** Yeah, and then the spreadsheet below. I got this spreadsheet now.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** It took everything that was marked in the Relevance column. There's still more analysis to do on "Somewhat" entries, but before we jump into it, I'm going to give Kristin a quick update on what we're looking at.

**Mark Stiltner:** So Kristin, Jakub basically said that if you have a bunch of old blog posts that aren't performing well, they can drag down your overall SEO performance. It's helpful to go through and remove posts that aren't relevant anymore, or ones that are dropping in search rankings. You should also revisit posts that are performing well but starting to decline, and update those.

**Jakub Rudnik:** Yeah, that's a good summary. We essentially did this at Active Campaign—had about 700 blogs, cut 15-20% of them, and saw a 10-15% jump in traffic without publishing anything new. It was just cutting old stuff, redirecting it, and cleaning up. Some content gets stale and needs updating.

**Jakub Rudnik:** If content isn't performing, it holds you back. If you've created content historically that's further from your current product focus or different from what you're targeting now, it has different relevance. Google is getting better at spotting that disconnect, and it drags down your overall site strength. You want every piece to perform at a high level and be relevant. Cut out what's not performing, cut out what's not relevant, and overall you'll see strength increase.

**Jakub Rudnik:** Mark will supplement that with conversion and link data as well, but these are straightforward decisions. For redirects, sometimes it's as simple as the blog home page. If there's any remaining crawlability, send it to the blog. For relevant content, I suggest redirecting to specific product or landing pages—like Japan payment methods blog to the Japan payment methods product page. Some are obvious, others need sanity checks. But they all have low traffic and should have low conversions.

**Mark Stiltner:** We're going through the site and identifying old content to remove because weak content makes the whole website look worse to Google. The blogs that aren't getting attention are old payment method type posts that have just aged out of relevance.

**Marc Winitz:** It's interesting—Jakub was supportive of this approach, and it makes sense.

**Marc Winitz:** I guess my question on this, Jacob, would be, have we from the printed?

**Marc Winitz:** I was totally down with doing this, like, have we printed enough?

**Marc Winitz:** No, I don't think so.

**Jakub Rudnik:** So the first crack on the relevance, moving through, I have to go to the agenda.

**Jakub Rudnik:** I got a lot more here.

**Jakub Rudnik:** I filtered out tags, categories, and AMP pages from the list to make it shorter. We're under 400 URLs for you to review. I'd recommend doing a first pass marking the obviously relevant or irrelevant ones. Focus on the low-hanging fruit first—anything with no clicks, no keywords, no impressions. Those are faster to process. For anything truly irrelevant, mark it "No" and we can redirect immediately.

**Marc Winitz:** I'm looking at some of these, like "What are B2B payment methods" and "What is Google Pay"—those might be important. How do we determine if something with zero or one click could actually be relevant? Is there something we could do with AI to make that content more resonant, or is it about the title and URL?

**Jakub Rudnik:** Some content was published three years ago and either lost traffic or never ranked. We're developing a playbook as we go. So far, we've added relevance tags to about 100 URLs, and we've already redirected 27. The next step is reviewing the remaining 376 for relevance. The tags are: No (kill it), Somewhat (leave it for now), or Yes (keep and potentially improve it). When evaluating: Is this good content? Will it attract the right audience? If it's marked No and has no traffic, it's an easy redirect.

**Marc Winitz:** Understood. I want to prioritize the obvious ones first.

**Jakub Rudnik:** Right. Next, we evaluate the remaining blogs. Something already doing well with traffic should be kept—it's not necessarily a priority, but it should stay. Content that had more traffic six months or a year ago suggests Google gave it good signals at one point—those should be updated. Content that never had traffic doesn't automatically mean it's worthless—there could be publishing issues, technical errors, or competing pages on the site.

**Jakub Rudnik:** So there's like more analysis to be

**Jakub Rudnik:** when we've got this bucket, but we find good topics that have key words that are relevant.

**Jakub Rudnik:** This would be a big bucket for potential refreshes or combinations of blogs.

**Jakub Rudnik:** Sometimes you find three topics that are very similar.

**Jakub Rudnik:** If you turn them into one big page, suddenly that's ranking much better.

**Jakub Rudnik:** So there's a few playbooks within this one.

**Jakub Rudnik:** And then new content, you may have stuff that doesn't have any traffic as never, but it was published two months ago, and that's just part of its organic growth.

**Jakub Rudnik:** So I would like leave these alone for three to six months at least, probably six months at least.

**Jakub Rudnik:** But we're really looking for these, especially these two that used to have traffic or they never quite worked as well as they showed.

**Jakub Rudnik:** then we would kind of bring these into different ways that we can prioritize, but that's what we would want to be getting to, I think, within a month or so, we're publishing so much new content.

**Jakub Rudnik:** There's plenty of work to be done, but this will help.

**Jakub Rudnik:** And there will be typically faster traffic growth when we're finding articles that used to work, and just adding sections or refreshing, doing the inter-

**Jakub Rudnik:** linking, work straight, or workflows, things like that.

**Jakub Rudnik:** there's a little bit longer of a playbook, definitely more depth and more things to talk about.

**Jakub Rudnik:** that's why I envision it as like V2, once we get through the most obvious cut and do those redirects, where do we take next steps and start to prioritize those pieces of content?

**Mark Stiltner:** OK.

**Mark Stiltner:** How do I get a hold of this notion?

**Jakub Rudnik:** This is, yeah, I put it in, create a new doc.

**Jakub Rudnik:** So in our work today, Docs, there is a folder for website and technical audit.

**Jakub Rudnik:** I've just added a blog audit.

**Jakub Rudnik:** So I'll do kind of as long as we're continuing on this.

**Jakub Rudnik:** I'm sure I can practice this right now.

**Mark Stiltner:** Yeah.

**Jakub Rudnik:** Have an update each week with any, you know, next steps and updates here so we can keep track and those will fold in.

**Jakub Rudnik:** It's got a checklist.

**Jakub Rudnik:** I think this will expand as we get more details, but try to do a V1 of this with look a lot.

**Jakub Rudnik:** So, I started to check these off, but as y'all go through, we'll just keep tabs on this, and then the last thing that I wanted to talk through was I did see a bunch of the AMP pages, and this expands with little bit of a write up, but in general, I would want us to deprecate those AMP versions of those blogs.

**Jakub Rudnik:** Do you me to hear all of them?

**Jakub Rudnik:** I think so.

**Jakub Rudnik:** There's very little traffic to them.

**Jakub Rudnik:** AMP stands for Accelerated Mobile Pages. Google prioritized them heavily about three to seven years ago, but not anymore. Looking at your site, your overall site speed is excellent—your Core Web Vitals pass on mobile, which makes me really happy. You've got about 100 clicks to AMP pages in the last three months. Google isn't surfacing these pages more than your other content. By maintaining AMP versions, you're just forcing Google to crawl every page twice and adding technical debt.

**Mark Stiltner:** If our site performance is good and AMP isn't relevant, I have no problem killing them. We also fixed our analytics—we found an issue with Google Consent Mode and OneSignal that had broken. Google wasn't giving permissions to track, so we've got that sorted now.

**Jakub Rudnik:** The biggest takeaways are we can redirect the batch of ~20 obvious blogs right now. Next, whoever can do it fast should skim the most irrelevant content and move it to redirect mode. Once we have the low-hanging fruit handled, we'll develop playbooks for what gets refreshed, what gets combined, and what needs deeper investigation.

**Mark Stiltner:** Kristin, I'd like a second set of eyes. If I do a first pass, can you review and provide a second look?

**Kristin Reischel:** Absolutely. If we think something's relevant but not getting traffic, should I provide guidance on what to do with it?

**Jakub Rudnik:** We can develop that context for each bucket as we go. The 400 URLs is manageable in batches. You got through 127 last week, so 150 a week is realistic.

**Jakub Rudnik:** If something's marked "Somewhat," that's where I'd want more context. It's easy to add. Otherwise, we can come back to those—they'll be more conversation-based. You can ping me throughout the week if you have questions. When you say you've redirected these, you've got the URL suggestions in place. You still need to send it to your team to implement the actual redirects.

**Aida Knežević:** On my end, I wanted to go over performance for last week and show what we did with your POV document. We're seeing early traction—we've published seven pieces so far. In week 16, we got 4 clicks and over 3000 impressions. The two articles that got clicks were the "Chargeback vs. Refund" piece and the "Payment Gateway API" article. This data comes from Google Search Console, which has a 48-hour delay. Week 17 data is still in progress. I've left a link to the performance doc in the agenda and will send it in Slack—you should have editing permissions to change dates and landing pages as needed. I'm hoping that by next week, we'll see GA4 data showing bounce rates and engagement rates. I'm also hoping the AI referral traffic picks up since it was affected by the GA4 issue.

**Aida Knežević:** That's what that is.

**Mark Stiltner:** Yeah, yeah, exactly.

**Mark Stiltner:** So that's it for performance.

**Aida Knežević:** This is super like normal.

**Aida Knežević:** So in the first like couple of weeks of publishing content, the impressions are a lot higher than clicks.

**Aida Knežević:** Content will build traffic over time. The most important thing is getting it indexed and visible in search. Traffic should pick up over the next couple of weeks. Kirkland is building a workflow to automatically upload articles to your WordPress, so publishing should be sorted.

**Mark Stiltner:** I figured out how to ingest blogs automatically. We're using a WP All Import plugin. We need approved blogs output as XML files instead of text—ChatGPT can do that conversion. I sent Kirkland (your IT guy) a message about it.

**Aida Knežević:** He responded and will build that workflow in AirOps. I left him a note about title tags and meta tags. It should be doable.

**Mark Stiltner:** On the CTA front, I sent a document of generic CTAs. What's the implementation status?

**Aida Knežević:** We've been adding them to this week's and last week's content from your document.

**Mark Stiltner:** I noticed some blogs dropped UK English spelling. Was that intentional or oversight? I saw it in a couple of payment-related articles.

**Aida Knežević:** I'll tell the writer to pay attention to that. We use the feedback column to check for British vs. American spelling, but sometimes the introduction gets tweaked in a different way. I'll talk to him about being consistent.

**Marc Winitz:** That's a huge, huge few things.

**Marc Winitz:** One is just a question about the upcoming content.

**Marc Winitz:** Do we have like a content calendar for like the next set of blogs being created and it's easy to look at?

**Marc Winitz:** So the air table, let me send you the link.

**Aida Knežević:** So everything that's in ready to start is content that is going to be done at some point.

**Aida Knežević:** But every week I go in and I pick like eight assignments that we're going to do that week.

**Aida Knežević:** And I prioritize the clusters that you decided to focus on in our initial strategy call.

**Aida Knežević:** So there are three clusters.

**Aida Knežević:** I can't remember them right now, like off the top of

**Aida Knežević:** ahead.

**Aida Knežević:** But I think it's cross-border payments, payment infrastructure, like the niche, like high-opportunity industries.

**Aida Knežević:** So those are the three clusters that we are prioritizing.

**Aida Knežević:** So that's where I'm like pulling assignments from, those are the one that are being worked on right now.

**Marc Winitz:** So like I'm in the air table, if I were to look at that list, what am I looking at?

**Aida Knežević:** So let me show, okay.

**Aida Knežević:** So let's just close all of this up so you get like a better overview of what's going on.

**Aida Knežević:** Does it look like this for you?

**Aida Knežević:** Everything's expanded, so maybe that's part of it.

**Marc Winitz:** Yeah, yeah.

**Aida Knežević:** So when it's expanded, it looks a little confusing, but basically everything and ready to start, there are like a hundred, over a hundred assignments and ready to start.

**Marc Winitz:** How many articles are you publishing per week? The editorial SEO target is 50,000 words per month—that's roughly ten articles, but if yours are longer, maybe eight a week?

**Aida Knežević:** Every week I pick assignments from the priority clusters and move them through the workflow. Rachel edits everything, and this week she finished with no backlog. Once edited, they move to ready for publish. For publishing cadence, we're targeting 8 articles per week since ours average longer than 1,200 words.

**Marc Winitz:** I also saw that GrowthX brought in a new head of content from TechCrunch. What's that person's role and will they intersect with our work?

**Aida Knežević:** We brought in Matthew Panzarino as Chief Content Officer. He was at TechCrunch for 10 years. He's above all the managing directors and is working to support the dev team with additional workflows and helping editors with hiring and content quality improvements. He joined recently, so it's still a work in progress. If you want to know more, you could reach out to Marcel to set up a call.

**Marc Winitz:** Thanks for your time. I'll reach out if I have more questions.

**Aida Knežević:** We'll be in touch on Slack. See you next week.
