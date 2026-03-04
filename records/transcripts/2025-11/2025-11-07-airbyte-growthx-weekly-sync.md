# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-07
time: 16:30 UTC
duration: 30 minutes
organizer: carrie@growthx.ai
participants: Carrie Chowske, Jakub Rudnik, Mario Moscatiello, Tanmay Sarkar, Nithin Mahalingam
fathom_recording_id: 100075421
fathom_url: https://fathom.video/calls/466828502
share_url: https://fathom.video/share/wRq29LouJCHwuyj-UkKxpg8yAShKycS8
source: fathom
enriched_on: 2026-03-02 02:15 UTC
</metadata>

---

## Summary

GrowthX and Airbyte aligned on strong content progress: the first batch of ~40 industry pages launched with plans to scale to 30 pages/week for completion by year-end, and a 50-article A/B test confirmed that TLDRs significantly boost organic clicks. Airbyte continues to dominate AI-related search with 9% citation share in Scrunch (vs. 8% for all competitors combined), while new content drives ~7,000 weekly sessions. The team discussed building a new "Integration Pages" cluster for each connector and launching "Use Case Pages" as the next PSEO project, with internal linking across all three page types to maximize SEO impact.

---

## Context

GrowthX and Airbyte have an ongoing content marketing partnership where GrowthX is responsible for producing PSEO (programmatic SEO) content at scale. Airbyte provides strategic direction and feedback on content performance, while GrowthX executes production, design, and analytics. This weekly sync is the standing operational meeting to track content launches, review performance metrics, and align on the editorial calendar and pipeline. The relationship focuses on driving organic traffic and establishing Airbyte as the authoritative voice in data integration and modern data stack topics.

---

## Relevance

**To GrowthX Delivery:**
- Successfully scaled from manual categorization to automated pipeline for industry pages; demonstrates process maturity that reduces delivery risk for future PSEO projects
- TLDR experiment validates low-effort, high-impact content optimization tactic applicable to other client engagements
- Established repeatable wireframe-to-pipeline workflow for launching new page types (Industry → Use Cases → Integrations)

**To CheckThat / AI Visibility:**
- Airbyte's 9% citation share in Scrunch vs. 8% for all competitors combined confirms content strategy is moving the needle on AI-related search visibility
- TLDR additions increase both SEO and GEO (AI) performance; signals that content optimization benefits both search channels
- New focus on "hybrid data deployment" and "data sovereignty" as emerging demand signals in AI search; these topics should be monitored for CheckThat positioning

**To GrowthX Business Development:**
- Airbyte account showing strong delivery velocity and positive results; demonstrates proof of concept for PSEO scaling with other enterprise clients
- Client expanding scope: moving from content-only to content clusters with internal linking strategy, showing confidence in approach
- Discussion of split experiments (TLDRs vs. AI summaries) and Cloudflare/Profound integration suggests deepening analytical capability and client sophistication

---

## Overview

- **Industry Pages Live:** The first batch of \~40 industry pages is live, with a plan to scale production to 30 pages/week for completion by EOY.
- **TLDRs Boost Clicks:** A 50-article A/B test shows TLDRs significantly increase organic clicks. The next step is to test them on top-performing pages and analyze their impact on LLM traffic.
- **New Page Clusters Planned:** Airbyte is building new "Integration Pages" for each connector. These will be internally linked with the Industry and Use Case pages to form a powerful content cluster.
- **Strong Performance:** New content drives \~7k weekly sessions. Airbyte's 9% citation share in Scrunch (vs. 8% for all competitors combined) confirms its leadership in AI-related search.

---

## Key Topics

### Content Performance & SEO

  - **Traffic Growth:** New GrowthX content drives \~7,000 weekly sessions, with strong growth in topics related to Flex pricing and plans.
  - **AI Search Leadership:** Airbyte's 9% citation share in Scrunch (vs. 8% for all competitors combined) confirms its leadership in AI-related search, especially for new topics like "hybrid data deployment."
  - **TLDR A/B Test Results:**
      - **SEO:** The 50-article (25 control, 25 test) experiment shows TLDRs significantly increase organic clicks, confirming a low-risk, high-reward tactic.
      - **GEO:** Test articles account for \~26% of citations for related queries, indicating strong early traction.
      - **Next Step:** Analyze the impact on LLM referral traffic by tagging test/control URLs in Looker.

### New Page Launches & Pipeline

  - **Industry Pages:**
      - The first batch of \~40 pages is live.
      - **Production Plan:** Scale to 30 pages/week for completion by EOY.
      - **Improvements:**
          - Add industry-specific icons to fill blank thumbnail space.
          - Update the "Data Engineering Resources" link to point to current content, replacing the outdated "Tutorials" link.
  - **Use Case Pages:**
      - The next PSEO project.
      - **Process:** Start with a wireframe for the design team, then build the automated pipeline.
      - **Content:** Carrie will review Jakub's existing list of use cases for verification.
  - **Integration Pages:**
      - Airbyte is building new pages for each connector (e.g., "Notion Integrations").
      - **Strategy:** These will be internally linked with Industry and Use Case pages to create a powerful, interconnected content cluster.

### Editorial & Experimentation

  - **Editorial Mix:**
      - **Current Focus:** Hybrid deployment and data sovereignty.
      - **Flexibility:** The team can pivot to new topic clusters from Airbyte to capture specific demand.
  - **New Experiment:**
      - **Context:** A 100-page batch of "Data Engineering Resources" is available for testing.
      - **Plan:** Split the batch 50/50 between TLDRs and Airbyte's own AI summary feature to compare their effects.

---

## Action Items

**Carrie Chowske (GrowthX)**
- Add industry-specific icons to category page thumbnails
- Update category page links to Data Engineering Resources; remove Tutorials
- Draft Use Cases page wireframe; share w/ Tanmay for pipeline setup
- Compile and share Use Cases list w/ Tanmay for verification
- File Looker ticket to add control/test cohorts; share recording; connect Jakub

**Jakub Rudnik (GrowthX)**
- Share examples of AI summary implementations from other companies
- Stay connected on Looker ticket for LLM referral traffic cohort setup

**Tanmay Sarkar (Airbyte)**
- Share topic cluster lists for next editorial batch w/ Carrie
- Review Scrunch prompts for TLDR experiment; send feedback to Carrie
- Initiate Scrunch-Cloudflare setup; add Cloudflare security to Slack

**Nithin Mahalingam (Airbyte)**
- Share 15 AI-summary test pages in Slack for TLDR/AI-summary split

---

## Transcript

**Carrie Chowske:** So good news to start off with.

**Carrie Chowske:** We do have the landing page done for the category.

**Carrie Chowske:** Yay.

**Carrie Chowske:** Literally right before the meeting, they messaged me and were like, here, it's done.

**Carrie Chowske:** So I went ahead and pushed.

**Carrie Chowske:** They hadn't made the filtering part live.

**Carrie Chowske:** So I went ahead and pushed that live for us.

**Carrie Chowske:** So right now...

**Carrie Chowske:** This is about 30, I think it's like 30 some pages, maybe 40 in here total, and they're just categorized into these larger groupings right now.

**Tanmay Sarkar:** Okay, this looks great.

**Carrie Chowske:** And we are not using any graphics for this, right?

**Carrie Chowske:** We did not have them, no.

**Tanmay Sarkar:** Okay, yeah.

**Carrie Chowske:** Yeah.

**Tanmay Sarkar:** Cool.

**Carrie Chowske:** Okay.

**Carrie Chowske:** But, yeah, take a look.

**Tanmay Sarkar:** I was thinking probably there is a blank space we are seeing in that thumbnail, right?

**Tanmay Sarkar:** Probably we can use one icon for each of those things that will fill that space and that will look good.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Do you want like something representative of like the industry or would you want something?

**Tanmay Sarkar:** Yeah, yeah, yeah.

**Tanmay Sarkar:** Something representative of that industry, yeah.

**Carrie Chowske:** Like photography or you think in illustration, you want us to kind of go with it?

**Tanmay Sarkar:** Yeah, like anything, I think you can get those in flat.

**Tanmay Sarkar:** Icon and all those things.

**Carrie Chowske:** Just like icons.

**Carrie Chowske:** Let's say if I'm talking about e-commerce, there are icons of e-commerce.

**Carrie Chowske:** Okay.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** No problem.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And then one of the things that I think we talked about, too, is that depending on what the industry grouping is, that this is getting swapped out, although this testimonial is probably the most common one that we're using, and then so does this graphic.

**Carrie Chowske:** So we tried to pull some things that were more specific to industries.

**Carrie Chowske:** So like, you know, we're, you know, we're using connectors that are more likely to be used in those industries as opposed to general, yeah, generic ones.

**Carrie Chowske:** So at least there's some, there's some variants in that.

**Carrie Chowske:** And then one of the things we talked about is updating those links depending on the industry grouping.

**Tanmay Sarkar:** Yeah, data engineering resources would be better.

**Tanmay Sarkar:** Tutorial is also fine, but we don't update tutorials anymore.

**Mario Moscatiello:** Is that the old font?

**Tanmay Sarkar:** Yeah, these are all old. We don't produce articles in tutorials anymore. That was mostly done by DevRel.

**Carrie Chowske:** Okay, I can swap that out.

**Tanmay Sarkar:** Yeah, we can just link to data engineering resources instead of tutorials.

**Carrie Chowske:** Easy enough.

**Carrie Chowske:** We should be able to start scaling that up to at least 30 a week. I didn't want to do too many until they make one final adjustment to the pipeline to automatically categorize them. Right now we did these manually. We have next week's batch ready to go; we just need to update the categories. So if we want to get started on Use Cases next — Jakub, originally you had use cases in mind, right?

**Jakub Rudnik:** I think that's right. Yeah, I was open to whichever way everybody wanted to go.

**Carrie Chowske:** I think that was our next one. We could get started on that pipeline. This one hopefully will go a little smoother now that we've been through the process with the engineering team.

**Tanmay Sarkar:** Yeah, that makes sense.

**Tanmay Sarkar:** What content mix or editorial topics do you have approved right now?

**Carrie Chowske:** For editorial, we're using the Flex-based topics. We're working in roughly three different topic areas right now.

**Tanmay Sarkar:** Do you have enough in the pipeline? We have topics we can give you for the next batch.

**Carrie Chowske:** We've got quite a few ready. We can swap things out at any time.

**Tanmay Sarkar:** I'll share lists of topic clusters where we want to capture demand.

**Carrie Chowske:** We're mostly focused on hybrid deployment and data sovereignty topics at the moment. We could shift that mix now if you want.

**Carrie Chowske:** We've got about 200 more industry pages coming. We should knock those out in three to four weeks, then start on Use Cases. We'll need a rough wireframe for the design team first so they can build the pipeline with precise specs. The industry pages are coming out really clean with minimal spot-checking. We're just pulling out any draft connectors or case studies to avoid empty spots.

**Tanmay Sarkar:** Once you have the use cases list, we can verify and confirm them.

**Carrie Chowske:** Jakub had some already. I'll go back and check. Right now we're doing 6 editorial and 25 industry pages a week. After next week, we'll scale to 30 a week and be done in about four weeks, so definitely by end of year.

**Carrie Chowske:** For performance, I pulled figures from the last 60 days. We're looking at sessions more than clicks now because of recent Google changes. On GrowthX content alone, we're at about 7,000 weekly sessions with steady engagement. We're not losing traction and continuing to see more traffic to those pages.

**Tanmay Sarkar:** Are these fresh editorial pieces or refreshed content?

**Carrie Chowske:** I excluded refreshes from this. This is net new content. I pull out our batch refreshes because they're such a large group. We're seeing steady upward trajectory on new content, and really strong growth specifically in the Flex pricing and plans topics.

**Carrie Chowske:** For AI/GEO, Scrunch shows strong citations. We saw a small falloff this period, but 9% of total citations go to Airbyte — that's higher than all competitors combined at 8%. There's 83% from third-party sources we could capture. Competitors are making small gains in LLM search, but Airbyte is the main player, especially in emerging areas like hybrid data deployment. That's a newer topic area we're capturing traffic from.

**Tanmay Sarkar:** ChatGPT did an entity update recently that changed how they show brands. Research shows brand visibility fell about 31% in the last two weeks.

**Carrie Chowske:** That will have an impact, but overall the profile is strong. It's one of the stronger ones I've seen. Good SEO practices help with AI-related search too — they're not separate. The TLDR experiment is looking good. We're more than halfway through.

**Jakub Rudnik:** The batches have 25 articles in control and 25 in test, and we're seeing good growth in clicks. This is organic-focused, and we set up Scrunch reporting for individual topics, though it's harder to parse at the macro level. The SEO impact is clearer — adding TLDRs at the top has definitely worked. I want to let it run another week for a complete dataset, but it's really good overall. I don't see why it would hurt SEO or GEO. If it continues, we should consider rolling it out to a hundred or couple hundred, or to content already generating traffic. We've already done a lot with GEO optimization, but the TLDR impact is pretty resounding.

**Tanmay Sarkar:** We can continue and roll it out to more pages. Pick the top 100 based on traffic. Is this SEO data from Google search only?

**Jakub Rudnik:** Yeah, it's Search Console data.

**Jakub Rudnik:** Yeah, so, I mean, Carrie, will you make an action item to, we should look at, I think we can get something out of either Profound or Scrunch.

**Jakub Rudnik:** Again, it's just a little bit murkier looking at individual prompts that doesn't tell the whole, you all the surface area.

**Jakub Rudnik:** But we can also look at these individual URLs for LLM referral traffic potentially.

**Jakub Rudnik:** So, that won't be, like, we, I don't know how much we're seeing to these type of URLs on an Airbyte site.

**Jakub Rudnik:** Like, some of my clients get no referral traffic from LLMs.

**Jakub Rudnik:** Others are getting, like, thousands a week.

**Jakub Rudnik:** So, yeah.

**Jakub Rudnik:** I have to look at how that is and these specifics, but if we can see a growth area there, there might be some more, that will at least give us another like rock to overturn to get a better sense.

**Jakub Rudnik:** But again, it's like a lot of other people have said TLDRs are working for them.

**Jakub Rudnik:** We're seeing it on the SEO front.

**Jakub Rudnik:** It's just like adding up that it seems like a win, a pretty easy win.

**Jakub Rudnik:** So I don't want to overthink it at the same time.

**Carrie Chowske:** I think maybe we could, if we want to look at, would we be able to, since we have in Looker the referrals from specific LLMs, would we be able to maybe blend that with data on those 25, just looking at those 25 URLs versus the 25 control and kind of see if any of that traffic is coming from those posts in particular?

**Carrie Chowske:** Do you think we would be able to use that too?

**Jakub Rudnik:** Yeah, I'm trying to think, like, the easiest way would be to do that same LLM, or not the, the way that I would love it is if it's, we have that same LLM.

**Jakub Rudnik:** Report that is in Looker, and then there was like a cohort or a tag for the control and the experimental, and then we could just flip that on and off within Looker, and then see how that, if and how that traffic from referrals has changed.

**Mario Moscatiello:** makes all sense.

**Jakub Rudnik:** So Carrie, it's probably like a slightly custom, like you wouldn't want to set up a new cohort long term for those, but maybe like we can duplicate that tab, or that tab, and then make like a tag that could be done in the same way as the cohorts.

**Jakub Rudnik:** I would just, I'd probably just file a ticket to the team over there.

**Jakub Rudnik:** And if you give them that recording and connect me, it'd be, I think it's easy to do.

**Carrie Chowske:** I just probably won't be the one to do it.

**Jakub Rudnik:** Yeah, I think it can probably be done pretty easily with just using like regular expression to like, you know, quickly say like, these equal this and these equal that.

**Carrie Chowske:** But I, yeah, I don't know how to set that up from scratch.

**Carrie Chowske:** I just know how to make the list.

**Carrie Chowske:** So I'll run that by, I'm not a problem.

**Carrie Chowske:** Cool.

**Carrie Chowske:** Yeah, because that'll tell us, I think, a little bit more if we can see that.

**Carrie Chowske:** Yeah, the thing I did see with Scrunch, just kind of dug into this a little bit, was too, that the citations for those tests, for queries that are related to those test posts, make up like about 26% of the citations, and when you compare that against your competition, it's significantly higher, so it does look like we're making some inroads there.

**Carrie Chowske:** Again, it's a little more of an estimate, but even if it's marginally correct, it's still significantly higher, so it's a good sign.

**Tanmay Sarkar:** And how many prompts are you tracking on Scrunch now?

**Tanmay Sarkar:** Total?

**Jakub Rudnik:** Yeah.

**Carrie Chowske:** Let me see real quick.

**Jakub Rudnik:** I just had it pulled up, and I don't know where it went.

**Carrie Chowske:** It goes to just, that's just the subset.

**Tanmay Sarkar:** And we can just, based on on the content you created.

**Jakub Rudnik:** It's a mix, so we carry set up specific prompts for this experiment, so we could see how those track, again, it's wonky, and how we actually interpret that, it was set up originally with like, Scrunch, we put in Airbytes, you know, your URL plus some competitive URLs, net polls, common, and like it suggests prompts from that, so there's some of that batch, some that we've done with content that's outside of the experiment, and then some that's the experiment specifically.

**Jakub Rudnik:** So, we can definitely take those different directions.

**Tanmay Sarkar:** Yeah, yeah, I think I'll just go through Scrunch and see those prompts, and then if I have anything, any feedback, I'll just let you know.

**Carrie Chowske:** Yeah, cool.

**Carrie Chowske:** What I did for the, what I did specifically for the experiment, Tanmay, was I pulled keywords that those posts were already ranking for, and then Scrunch will do like a query based off those keywords, and that's where those came from specifically for that.

**Carrie Chowske:** I just determined whatever their top ranking keyword was, and pulled the prompts.

**Carrie Chowske:** From that to kind of see if we were getting traffic related to those topics.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** So there are two kinds of things what these geo tools do.

**Tanmay Sarkar:** One is if you ask certain prompts where they have to say brands, then your brand show up and it shows brand visibility.

**Tanmay Sarkar:** But there are also any random questions for where they can actually pull data from your websites, but they don't show your brand.

**Tanmay Sarkar:** And in those cases also, many times they don't mention because airbait is not mentioned there.

**Tanmay Sarkar:** So I'll just check those prompts.

**Tanmay Sarkar:** Based on that, I'll just let you know.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** No problem.

**Carrie Chowske:** Okay.

**Carrie Chowske:** And then I think we had, this looks like it's been started to be set up.

**Carrie Chowske:** That's the wrong one.

**Carrie Chowske:** I'm in my wrong account.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Yeah, so for this, I think if you wanted us, I think we talked about setting this up and Scrunch isn't giving me a fit right now, won't let me do it.

**Carrie Chowske:** But you guys are on Cloudflare, right?

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** So the last time we did this with Cloudflare and our security guy, like, because we have a channel with Profound and we took so much thing, but I'll initiate this.

**Tanmay Sarkar:** But, like, he might ask a lot of questions, so I might have to add him in the Slack channel.

**Carrie Chowske:** It's only if you want to do it.

**Tanmay Sarkar:** I just was offering it up because I know we talked about it.

**Tanmay Sarkar:** I think it's good because we get to see data from both the tools and evaluate, like, if we are seeing the same thing or not.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Yeah.

**Carrie Chowske:** Okay.

**Carrie Chowske:** I think that's all that I have.

**Carrie Chowske:** I will add in those other action items.

**Tanmay Sarkar:** Does anybody else have anything that we wanted to go over before we wrap it up?

**Tanmay Sarkar:** No.

**Tanmay Sarkar:** And I just want to go over one thing.

**Carrie Chowske:** Okay.

**Tanmay Sarkar:** So we are building this kind of integrations page for each of our connectors.

**Tanmay Sarkar:** So this is a new clusters what we are trying to build.

**Tanmay Sarkar:** I shared some integration page designs in the chat. Last week I went to your office for the AI product kickoff. It went well; we'll launch our open source and MCP version soon. This is the Integration Pages template we're building — source on left, destination on right. Mostly the connector name changes, like "Notion Integrations" or "integrate Notion connector with Airbyte."

**Jakub Rudnik:** Do you have a visual sitemap showing the different PSEO site sections you have and anything else planned? As we add more PSEO sections, I want to think about internal linking strategy.

**Tanmay Sarkar:** Once the Industry Pages go live, they should link to Use Cases, which we'll also build, and Integration Pages. These three should be internally linked. We can add one section at the end and update it programmatically.

**Jakub Rudnik:** If it's just those three page types, then you don't need anything else. If you had six different page types planned over the next year, I'd want to see the full picture.

**Tanmay Sarkar:** Just these three: industry, use case, and integrations.

**Nithin:** We have 100 pages for the TLDR experiment. We're testing 15 pages with AI summary first, then we can pick more pages.

**Jakub Rudnik:** I'll share those 15 pages. You can pick more from there.

**Jakub Rudnik:** Thank you.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Oh, okay.

**Tanmay Sarkar:** We are doing that AI summary thing also, right?

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Let's split it: half the pages with AI summary, half with TLDR. The Data Engineering Resources section has 600-700 pages, so we can easily run this experiment.

**Jakub Rudnik:** Are you using the basic "Summarize with GPT" and "Summarize with Claude" buttons, or more advanced features?

**Nithin:** Yeah, plus a little bit of content.

**Jakub Rudnik:** I've been sharing examples with everyone doing this type of experiment. My last company's software was already doing this. There aren't many examples out there yet, so I'm building a database to share better.

**Tanmay Sarkar:** I have a hard stop and need to jump on another call. I think we're good here.

**Jakub Rudnik:** I'll share the 15 pages in Slack for the experiment.

**Tanmay Sarkar:** Everyone have a good weekend. Thanks, Carrie.
