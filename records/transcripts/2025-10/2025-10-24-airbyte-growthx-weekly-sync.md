# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-24
time: 15:30 UTC
duration: 27 minutes
organizer: carrie@growthx.ai
participants: Carrie Chowske (GrowthX), Jakub Rudnik (GrowthX), Mario Moscatiello (Airbyte), Tanmay Sarkar (Airbyte)
fathom_recording_id: 96633369
fathom_url: https://fathom.video/calls/451560149
share_url: https://fathom.video/share/KDKeBaysFZRUHKxrBR4yzxq5MsKnLbmZ
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

Carrie reviewed the live industry page pipeline with Tanmay, showing strong progress with the first page published but pipeline bugs preventing full scale-out. The team approved an A/B test adding TLDRs to 25 underperforming articles to test if summaries improve SERP visibility and LLM citations, and discussed expanding the Scrunch prompt list from 54 to hundreds to get complete LLM performance visibility. Jakub committed to building an SEO forecasting model projecting traffic growth scenarios based on publishing volume.

---

## Context

Airbyte is a GrowthX client running a major content marketing initiative focused on industry verticals and data engineering topics. Carrie Chowske (GrowthX delivery lead) and Jakub Rudnik (GrowthX SEO) work closely with Tanmay Sarkar (Airbyte product/content) and Mario Moscatiello (Airbyte co-founder) to manage content strategy, SEO performance, and experimentation. This is part of an ongoing weekly sync focused on scaling industry pages, tracking LLM visibility (where Airbyte sees significant traffic via ChatGPT and Perplexity), and improving content performance through data-driven testing.

---

## Relevance

### To GrowthX Delivery
- Automated industry page pipeline now live; major scaling opportunity once bugs are fixed (Carrie working on content transfer to Webflow)
- Clear template pattern emerging: industry hub page, dynamic connector lists, case study quotes, and related resources — replicable for use cases and personas
- Content production workflow accepts TLDRs natively; easy to add new content features once pipeline is stable

### To CheckThat / AEO
- LLM traffic is Airbyte's strongest engagement signal: ~10% of all citations come via ChatGPT/Perplexity, with users spending significantly more time on-page than Google search visitors
- Scrunch tracking critically underfunded at 54 prompts vs. hundreds of published articles; expansion directly supports LLM visibility measurement
- TLDR hypothesis testing aligns with CheckThat focus: compact summaries may improve LLM scraping and citation rates

### To GrowthX Business Development
- Airbyte launching AI data product with strategy sprint kicking off in ~1 week; strong parallel to Augment engagement and expansion opportunity for CheckThat/AEO consulting
- Account health signals positive: weekly syncs active, production pipelines scaled, cross-functional buy-in on experimentation

---

## Overview

- The automated industry page pipeline is live, but a data transfer bug is blocking scale. Tanmay will review the first page to validate the output before a full rollout.
- A/B test approved: Add TLDRs to 25 underperforming articles to test if summaries improve SERP visibility and LLM citations.
- LLM traffic is highly engaged (higher time-on-page) but under-tracked. The Scrunch prompt list will be expanded from 54 to match the content library.
- A new SEO forecasting model will be built to project traffic growth from publishing volume, providing a "good, better, best" scenario.

---

## Key Topics

### Industry Page Pipeline

  - The first automated industry page is published, but a pipeline bug is blocking scale by preventing content from transferring to Webflow.
  - **Tanmay's Feedback & Decisions:**
      - **"Real-time" keyword:** Remove from all generated content.
      - **Use Cases link:** Update text to "Explore Articles" until dedicated use case pages exist.
      - **Industry hub page:** Create a central `/industries` page to list all sub-pages.
  - **Content & Design Adjustments:**
      - **Logos:** Use static images for pillar industries (e.g., Healthcare) instead of dynamic, sub-category logos to simplify the pipeline.
      - **Quotes:** Pull from a pre-curated list of case study quotes.
      - **Connectors:** Generate descriptions via pipeline research.
  - **Next Steps:**
      - **Tanmay:** Review the live page and provide final feedback.
      - **Carrie:** Fix the pipeline bug and implement Tanmay's feedback.
      - **Carrie & Tanmay:** Merge their industry lists (\~60 and \~100+ pages) to create a master list for prioritization.

### Performance & Tracking

  - **SEO Performance:**
      - SERP visibility for Airtable pages is improving.
      - CTR is rising, and traffic is stable week-over-week.
      - Content clusters for the Flex product and security are showing strong momentum.
  - **LLM Performance:**
      - **Traffic:** ChatGPT is the top source, followed by Perplexity.
      - **Engagement:** LLM users are highly engaged (higher time-on-page) and represent \~10% of all citations.
      - **Tracking Gap:** The Scrunch prompt list is limited to 54, providing an incomplete view of performance.
  - **Action Items:**
      - **Jakub:** Build an SEO forecasting model to project traffic growth from publishing volume.
      - **Carrie:** Expand the Scrunch prompt list to match the content library.

### Experimentation: TLDRs

  - **Hypothesis:** Adding a TLDR (Too Long; Didn't Read) summary improves SERP visibility and LLM citation rates.
  - **Experiment Design:**
      - **Test Group:** 25 articles with significant Ahrefs position drops since April.
      - **Control Group:** 25 similar articles.
      - **Action:** Add a TLDR to the top of each test article.
      - **Tracking:** Monitor keyword positions and Scrunch visibility for both groups.
  - **Rationale:** The experiment isolates the TLDR variable by making no other content changes. A CMS limitation will auto-update the publish date, but this is acceptable as a secondary variable.

### Future Focus: AI Product

  - Airbyte is launching an AI data product, with a strategy sprint kicking off in about a week.
  - This creates new opportunities for content and marketing support, similar to work for other GrowthX clients (e.g., Augment).

---

## Action Items

**Carrie Chowske (GrowthX)**
- Update industry page template: set pillar logos, remove 'real-time' directive, fix placeholder
- Create /industries listicle page; link to industry pages
- Email Tanmay: industry page link + case-study quotes list
- Merge industry lists w/ Tanmay; dedupe; expand to 100–150
- Upload Scrunch prompts sheet; expand tracking to hundreds
- Run TLDR experiment: add TLDRs to 25 articles; track in Scrunch + SEO

**Tanmay Sarkar (Airbyte)**
- Merge industry lists w/ Carrie; dedupe; expand to 100–150

**Jakub Rudnik (GrowthX)**
- Build SEO traffic forecast model (good/better/best) w/ new SEO; share w/ Carrie + Tanmay
- Update TLDR experiment doc: note CMS auto-updates publish date

---

## Transcript
**Carrie Chowske:** It's hailing right now.

**Carrie Chowske:** It's hailing?

**Jakub Rudnik:** Yeah, there's hail hitting our windows and stuff.

**Carrie Chowske:** Oh my gosh.

**Jakub Rudnik:** Hey, Mario.

**Mario Moscatiello:** Hey, have you moved, Jakub?

**Jakub Rudnik:** Yeah, new house.

**Jakub Rudnik:** You can see, like, stuff's on the floors.

**Mario Moscatiello:** Nice.

**Jakub Rudnik:** Is that a mattress on the floor or not?

**Jakub Rudnik:** No, just a chair behind me.

**Mario Moscatiello:** Okay, okay, okay.

**Jakub Rudnik:** But I was spending some of my morning ordering things for this office to, like.

**Mario Moscatiello:** Yeah, that's always fun, though.

**Jakub Rudnik:** It is fun.

**Jakub Rudnik:** And so, like, trying to get, like, the monitors and the cables and all that.

**Mario Moscatiello:** I go to my office, so.

**Carrie Chowske:** Oh, I love your window.

**Mario Moscatiello:** Oh, that's Oh, yeah, it's beautiful.

**Mario Moscatiello:** With the outside, it's nice.

**Mario Moscatiello:** And then, yeah, got a pretty nice setup.

**Jakub Rudnik:** Nice.

**Jakub Rudnik:** That's what I'm aiming for right now.

**Jakub Rudnik:** It feels chaotic.

**Jakub Rudnik:** And I'm, like, spending eight hours, nine hours in here and, like, not loving it.

**Mario Moscatiello:** So I need.

**Mario Moscatiello:** No, I know, I know.

**Mario Moscatiello:** It's that Amazon basket goes up pretty quick.

**Jakub Rudnik:** I know.

**Mario Moscatiello:** It up pretty quickly.

**Jakub Rudnik:** It's like...

**Mario Moscatiello:** Yeah.

**Jakub Rudnik:** Thank you.

**Carrie Chowske:** I'm like on this mission to like not buy anything new and just keep buying like, you know, buying secondhand or like getting antiques and things and that makes it even harder.

**Carrie Chowske:** And I'm just like, I still haven't gotten this office the way I want it.

**Carrie Chowske:** We lived in the house for over a year, so it's fine.

**Carrie Chowske:** Can't find a spot where I'm not like that backlit by windows.

**Carrie Chowske:** Excuse me.

**Carrie Chowske:** Hey, Tanmay, how are you?

**Tanmay Sarkar:** Hey, Carrie, I'm doing good.

**Tanmay Sarkar:** How are you?

**Carrie Chowske:** I'm great.

**Carrie Chowske:** I have good news.

**Carrie Chowske:** We have an industry page.

**Tanmay Sarkar:** Wow.

**Carrie Chowske:** We have one, one whole one.

**Carrie Chowske:** Okay.

**Tanmay Sarkar:** It exciting.

**Carrie Chowske:** It doesn't sound very promising, but no, I promise it is.

**Carrie Chowske:** I will get to it because I know you'll probably have a lot of questions about that.

**Carrie Chowske:** But the good news is we are in, we're in good shape.

**Carrie Chowske:** We're cooking with gas, as they say.

**Carrie Chowske:** So we've, and we've published this week's content already.

**Carrie Chowske:** So it's really just a matter of getting the first few of these out and then hopefully next week we can just really start cranking out.

**Carrie Chowske:** So.

**Carrie Chowske:** to more of those industry pages and really get those going pretty quickly.

**Carrie Chowske:** And we've got a pretty good backlog of topics we can work on on the editorial side, so there's nothing really crazy there to worry about.

**Carrie Chowske:** Here's where we are with this page.

**Carrie Chowske:** There are a few little hiccups yet, but I just wanted to give you an opportunity to look at it and let us, if we need to make any more tweaks to our pipeline or to the template before we start doing a bunch of these.

**Carrie Chowske:** So this is currently, we have, there's like three in Webflow, a couple of them, if you were to look at them, you'd be like, there's no content here, and that's the issue that we're fixing.

**Carrie Chowske:** For some reason, our pipeline did not toss all of the info that it generated to Webflow properly, even though it created the page.

**Carrie Chowske:** So we're trying to figure that out at present.

**Carrie Chowske:** But this one, we, this came from what was generated on the pipeline.

**Carrie Chowske:** And then, and with minimal edits to it.

**Carrie Chowske:** And so all of these things.

**Carrie Chowske:** These being pulled from the data sources that we have.

**Carrie Chowske:** So we can make some adjustments to it.

**Carrie Chowske:** Some things are more complex than others, obviously, but these are all mostly dynamic from one industry to the next, if that makes sense.

**Tanmay Sarkar:** So, yeah.

**Tanmay Sarkar:** Let me have a look.

**Carrie Chowske:** Yeah, yeah, yeah.

**Carrie Chowske:** Let me drop you the link, too.

**Carrie Chowske:** Well, it's in the, I didn't even give you guys the agenda.

**Carrie Chowske:** See, I'm all over the place today.

**Carrie Chowske:** I'm so sorry.

**Carrie Chowske:** Okay, so this section here, this is coming, our pipeline is pulling these based on industry research.

**Carrie Chowske:** So it's like doing research every time we run it, and it is pulling these five things.

**Carrie Chowske:** This right now goes to the tutorials.

**Carrie Chowske:** We can, when we have use case pages, we could make it go.

**Carrie Chowske:** There.

**Carrie Chowske:** So right now, it goes to this page.

**Carrie Chowske:** And then, I'm just going to, let me explain too where these are pulling from, and then I'll let you take a deep look at it.

**Carrie Chowske:** So these here also, same thing, we use that list of connectors, and it's kind of connecting them to the industry and pulling some use cases from there.

**Carrie Chowske:** Right now, this is a static image.

**Carrie Chowske:** What I'm going to do, before we start really pulling into these out, is to do them by some pillar industries.

**Carrie Chowske:** So we'd have one for healthcare and life sciences.

**Carrie Chowske:** We'd have one for financial services.

**Carrie Chowske:** We'd have one for retail and use those for any subcategories beneath them, because it got a little too complex trying to swap out all of these logos every time and use the pipeline to do it.

**Carrie Chowske:** It got a little crazy.

**Carrie Chowske:** So we'll get that updated.

**Carrie Chowske:** And then this year, I pulled quotes from all the live case studies, and then there were...

**Carrie Chowske:** Pulling them based on industry.

**Carrie Chowske:** And so as close as they can get it, they're pulling from that.

**Carrie Chowske:** But I can give you also the list of those.

**Carrie Chowske:** And then same, this is a research step.

**Carrie Chowske:** And then same thing here.

**Carrie Chowske:** It's connecting those lists of connectors and pulling from them and then using the research step to generate these descriptions of what they do.

**Tanmay Sarkar:** Oh, got it.

**Tanmay Sarkar:** I think everything looks fine.

**Tanmay Sarkar:** And for the tutorials and use cases where we are linking, I think we can just change the text. We are saying use cases, but sending to tutorials. We can just say explore something, articles or resources.

**Carrie Chowske:** I mean, yeah, and we could move the link too.

**Tanmay Sarkar:** I don't think that's necessary right now.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** I mean, I like having something there for use cases, but since we don't have any pages yet, that doesn't make any sense.

**Tanmay Sarkar:** Actually, we can have a listicle category page where we list all these industries pages. We should have that, so we can leave that link here.

**Carrie Chowske:** Okay.

**Tanmay Sarkar:** So the URL path should be /industries. If you open that page and click on healthcare, then the industry page will open. You're getting my point, right?

**Carrie Chowske:** Yeah.

**Tanmay Sarkar:** Yeah, like that, with all the industries listed there.

**Carrie Chowske:** And then this was one that I think we had a lot of concern over making sure that we got it right.

**Carrie Chowske:** Nothing jumped out at me that was really crazy.

**Carrie Chowske:** It's a lot of, again, this is coming straight from the pipeline.

**Carrie Chowske:** So when I'm looking at it, I'm relying that it got it right to begin with.

**Carrie Chowske:** But if you see anything that's jumping out at you is crazy.

**Carrie Chowske:** I did notice that it has a tendency to insert real-time, you know, data things into everything.

**Carrie Chowske:** And I think we've got to direct it to take that out because I know that that was an issue, especially with the healthcare stuff, right?

**Tanmay Sarkar:** Yeah, I think we should not say real-time.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Okay, we can put in a thing for that.

**Carrie Chowske:** And then just to give you, I'll send this to you as well, Tanmay, but I literally just went through all the case studies and grabbed a full quote for each one.

**Carrie Chowske:** These are quotes that say something relevant about Airbyte, so it's pulling from these as its source.

**Tanmay Sarkar:** Cool, yeah, I can check and update.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And then...

**Carrie Chowske:** This right now, this, and this does go to the connectors page, like you were saying about the industries, well, it's supposed to.

**Carrie Chowske:** Why is it not working?

**Carrie Chowske:** Oh, okay.

**Carrie Chowske:** Well, I haven't fixed it.

**Carrie Chowske:** It was working yesterday.

**Tanmay Sarkar:** I don't know if it did.

**Tanmay Sarkar:** Yeah, cool.

**Carrie Chowske:** This can go to the connectors page.

**Tanmay Sarkar:** Yeah, it went to your main connectors page. We can just redirect it to connectors.

**Carrie Chowske:** Yeah, okay.

**Carrie Chowske:** And then this here is also then pulling that way.

**Carrie Chowske:** It's grabbing from tutorials.

**Carrie Chowske:** It's pulling from data engineering resources.

**Carrie Chowske:** I think these three are all data.

**Carrie Chowske:** This one's pulling from a tutorial.

**Carrie Chowske:** But again, it's pulling related topics for that.

**Tanmay Sarkar:** Yeah, it's not only going to tutorials; it's going to data engineering resources also based on the website.

**Carrie Chowske:** And that is fine.

**Carrie Chowske:** I'll leave it with you.

**Carrie Chowske:** I'm not saying you have to put your final okay on it right now. Let me know what you think after you review.

**Carrie Chowske:** I also need to make sure they fix this because it's showing your little placeholder that you've got internally.

**Carrie Chowske:** We don't want that to show, but we'll get those little things fixed and it should be good to go.

**Carrie Chowske:** So I just want to make sure that we have, like, the pipeline's giving us solid results and that we can, you know, scale it.

**Tanmay Sarkar:** Sounds good.

**Carrie Chowske:** Great.

**Carrie Chowske:** I'm glad to hear it.

**Carrie Chowske:** We're very proud of what we've got, but we always know there's room for improvement.

**Carrie Chowske:** So, okay, so if, depending on any major changes, we can, my hope is to try to get those other four pages up today yet if we can, but if we have major changes, we'll have to just hold it and we'll get to it, you know, as soon as possible, but shouldn't be too crazy.

**Carrie Chowske:** And then, and then after that, and I don't know if we, we never really discussed in terms of prioritizing, like, which industry pages we wanted to do next.

**Carrie Chowske:** Like, I have the full list, but, like, is there anything that we wanted?

**Carrie Chowske:** to do to prioritize, or if we just want to kind of go through them as we go, like, is there anything in particular?

**Tanmay Sarkar:** How long is the list?

**Carrie Chowske:** It is 60-something at the moment.

**Tanmay Sarkar:** I can share my list, and we can merge them together, dedup, and expand to probably 100–150 pages.

**Carrie Chowske:** Okay, okay, not a problem.

**Carrie Chowske:** Okay, that's easy.

**Carrie Chowske:** And then, you know, again, once we've got this pipeline, too, it'll be easy for us if we wanted to expand this and do, like, use cases and personas and things like that.

**Carrie Chowske:** It'll be pretty easy to replicate, I think, especially now that our team understands what we're trying to do.

**Carrie Chowske:** Let me just go over some performance things really quickly. No major changes since last week.

**Carrie Chowske:** It's nice to see that one of the things that continues to happen is Airtable pages are appearing in the SERP position moving higher, which is obviously a good thing because that brings it to the top of the list.

**Carrie Chowske:** And it's gone down even against last week, so that was nice to see.

**Carrie Chowske:** And click-through rate's going up, too.

**Carrie Chowske:** And traffic's pretty much consistent.

**Carrie Chowske:** You can see here, we have a little variation in impressions, but clicks are consistent week over week.

**Carrie Chowske:** And then the growing clusters, this is positive.

**Mario Moscatiello:** Just how do we have, and maybe this is more like a broader question, do you have any ability at this point? I don't want to say to forecast, but if we were to say, in terms of correlating outputs to traffic and stuff, how should we think about it? If we were to publish double the pages or whatever, or if we keep publishing what we publish,

**Mario Moscatiello:** Which now with the growth and click-through rate and so on and so forth that we're seeing, like, is there any way of seeing, like, where, in theory, we should land, like, at any given time or?

**Mario Moscatiello:** Maybe I'm not asking the question in the right way.

**Jakub Rudnik:** No, I know what you mean.

**Jakub Rudnik:** Yeah, we haven't done that here and we've, I've done that kind of ad hoc, like, for a couple projects or clients.

**Jakub Rudnik:** So I think it could make sense here.

**Jakub Rudnik:** We have a new SEO who is starting Monday. He's client agnostic and did some forecasting for a theoretical client that I liked. I think we could apply his model here.

**Jakub Rudnik:** I'll flag this to him. We can use his model, input our publishing volume, and pull metrics from SEMrush or Ahrefs plus our publishing cadence to build a forecast with good, better, and best scenarios. I can take this on and share a peek at what that looks like. Might not have it before next call, but I'll prioritize it for the next couple of weeks.

**Carrie Chowske:** Thanks, Jakub.

**Carrie Chowske:** What's really positive for me, and this relates to what you're saying, Mario, is there's obviously a clear correlation.

**Carrie Chowske:** You know, the more you publish, the more growth you're going to see, right?

**Carrie Chowske:** Because there's just more there to discover.

**Carrie Chowske:** We're seeing steady growth, especially in areas we specifically targeted. The Flex product cluster, for example, and the security and privacy cluster. We're talking a lot about cloud and hybrid architecture security.

**Carrie Chowske:** And those are the areas where we're seeing a lot of momentum.

**Tanmay Sarkar:** Yeah, those are really good signals.

**Carrie Chowske:** With LLM performance, we talked last week about the growth with Claude and some quirks we've seen since the beginning of the year.

**Carrie Chowske:** I narrowed this to the last three months to look at sessions and what traffic we can actually see to your site.

**Carrie Chowske:** ChatGPT is obviously the clear leader, followed by Perplexity.

**Carrie Chowske:** The number of sessions from other LLMs is lower, but what's interesting is the engagement rates. People coming from LLMs are staying longer and engaging more than your average Google searcher, and that's continuing to go up.

**Carrie Chowske:** Citations have increased over the last 12 weeks. Scrunch estimates LLM sources account for about 10% of all citations. You have a strong presence compared to competitors when you stack it up on the Scrunch dashboards, so we're doing really well.

**Carrie Chowske:** Do we have a limit in Scrunch? It seems like we're only tracking 50-54 prompts, but we've published so many more articles.

**Tanmay Sarkar:** Yeah, we need to increase our prompt numbers to track. We're only seeing a very small portion of our data.

**Jakub Rudnik:** Yeah, the limits are based on what we're paying, and we have headroom. Let's take this as an action item: convert our keywords to prompts to match what we've built, especially for the industry pages and other folders. We should set this up now so we can track visibility as we publish.

**Jakub Rudnik:** But, yeah, let me, 54 PROMPs.

**Jakub Rudnik:** Yeah, we have room, Tanmay.

**Jakub Rudnik:** So I think we'll easily be able to move that to a few hundred.

**Jakub Rudnik:** I forget what our exact limit is.

**Jakub Rudnik:** We can easily go up to a few hundred, so no problem there. Good call.

**Carrie Chowske:** Do we need admin access to add prompts?

**Jakub Rudnik:** I have admin access now, so I can get you whatever access is needed if you don't have it.

**Tanmay Sarkar:** You can just upload a sheet of prompts. Put all the prompts in one column and upload instead of adding them manually.

**Carrie Chowske:** Great, we have good records on our end with the keywords, so we should be able to do that exactly.

**Carrie Chowske:** Did you have any updates on experimentation?

**Jakub Rudnik:** I created a document on that. I was in another meeting earlier, so I didn't get to share it. All good though.

**Jakub Rudnik:** So I did this early in the week.

**Jakub Rudnik:** I wrote up an experiment on adding TLDRs to pages that have lost traffic and keyword position since April.

**Jakub Rudnik:** I picked 50 articles that have dropped the most in position using Ahrefs data rather than GSC, since AI Overviews have impacted traffic. The experiment: add TLDRs to 25 of those articles (test group) and 25 stay untouched (control). We'll track keyword positions and Scrunch visibility for both. The hypothesis is that TLDRs help LLMs scrape better summaries and cite more effectively, and it should have a similar effect on SEO. We can create these in a week on top of our regular publishing.

**Jakub Rudnik:** I want to run this experimentally to see if it's worth rolling out across your entire data engineering resources and other blogs. If we see positive results, we can scale it.

**Tanmay Sarkar:** Yeah, I think we can definitely try.

**Carrie Chowske:** Yeah, it should be pretty easy.

**Carrie Chowske:** It doesn't require engineering resources. We can do it on the content side by just updating our initial prompt and final check to ask for the TLDR.

**Carrie Chowske:** And then if it does, then we'll add it into the, we can add it into the pipeline and just make it part of normal content production.

**Jakub Rudnik:** We previously talked about doing FAQs and TLDRs.

**Jakub Rudnik:** FAQs are already on a decent number of pages, so it would be messier. TLDRs are net new, so let's run this experiment and build the motion first.

**Jakub Rudnik:** This works from a publishing and tooling standpoint. We can have content managers and publishers do this next week on top of regular work, then track results over the next month or two. If we see positive traction, we can roll it out further.

**Tanmay Sarkar:** And you're adding this as a new section, not removing existing content?

**Jakub Rudnik:** For this experiment, I don't want to touch anything else. I just want to add TLDRs at the top of the pages that pull from existing content. It should be a true summary without touching anything else, so we can revert if needed. The goal is to isolate this variable.

**Carrie Chowske:** Just to flag, when we update the page in the CMS, it automatically updates the publish date. I don't think we can stop that.

**Jakub Rudnik:** That's fine, I was planning to note that the date auto-updates as a secondary variable. That's acceptable for V1 of this experiment.

**Carrie Chowske:** As long as we're limiting variables, that works fine.

**Jakub Rudnik:** Cool, thanks.

**Carrie Chowske:** I think that's everything. Anything you guys need from us?

**Tanmay Sarkar:** No, I think this is good.

**Mario Moscatiello:** We'll have a separate stream for our AI product. One of our co-founders, Jean, met Marcel yesterday, so they had a chat. We're launching an AI data product, which is exciting. We're kicking off a strategy sprint in about a week. We realized we're launching a bit later than originally planned, but we'll figure out the production impact. It opens up a lot of possibilities similar to what you're doing with clients like Augment. Should be fun.

**Jakub Rudnik:** That sounds fun. We'll monitor those calls and let us know how we can shift or support them.

**Mario Moscatiello:** Of course. Have a great weekend.

**Jakub Rudnik:** Thanks, Tim. You too.

**Tanmay Sarkar:** Bye, thanks.
