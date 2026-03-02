# Airbyte <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-13
time: 16:29 UTC
duration: 32 minutes
organizer: team@growthxlabs.com
participants: Erik O'Brien, Nithin M, Tanmay Sarkar, Kushal Chatterjee
fathom_recording_id: 122335322
fathom_url: https://fathom.video/calls/565597919
share_url: https://fathom.video/share/pxQzZpD4sWxy5bvd7Q1fBmmdt__HovhM
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Airbyte aligned on three major initiatives for their content partnership: shifting keyword strategy toward high-volume competitor research terms to capture initial demand, refocusing the "Check That" tool prompts on tool-based queries where Airbyte can be a direct answer, and establishing a new publishing workflow where Erik drafts articles in Webflow and Nithin publishes them post-launch on Tuesday to prevent accidental publication. The team also identified website issues on the Agent Connectors page—a missing Granola icon and a misplaced Salesforce section—that need staging and review before going live.

---

## Context

This is a weekly sync between the GrowthX content marketing team (Erik O'Brien leading) and Airbyte's product and marketing stakeholders (Tanmay Sarkar, Nithin M, Kushal Chatterjee). The meeting is part of an ongoing engagement where GrowthX is building out Airbyte's content strategy and SEO visibility for a new product they're launching. The launch was originally scheduled for this week but slipped to the following Tuesday due to product bugs and team capacity constraints. The team had just completed a strategy sprint earlier in the month and is now moving into execution mode on three parallel workstreams: keyword prioritization and content writing, refinement of their "Check That" monitoring tool (which tracks how LLMs respond to various queries), and website updates ahead of the launch.

---

## Relevance

- **To GrowthX Delivery:** The keyword strategy pivot—away from low-volume topics toward competitor research—demonstrates a key principle GrowthX applies across clients: demand capture over thought leadership for product launches. This validates the keyword prioritization methodology and may inform similar strategy shifts for other clients in high-growth B2B markets.

- **To CheckThat:** Direct mention of "Check That" tool refinements, including the need for topic clustering, tagging capabilities, and region-based visibility. Nithin flagged that current prompts have weak correlation to tool-based questions; the team is building a new prompt list where Airbyte is a direct answer rather than informational context. UI feedback about single-line prompts suggests product refinements needed in the CheckThat dashboard.

- **To GrowthX Business Development:** Airbyte's product launch timeline (Tuesday) suggests momentum in the partnership. The scope of work—content writing, tool setup, website updates—indicates continued engagement depth. Risk: the product launch slip reflects internal Airbyte constraints but could impact content velocity if website isn't stable post-launch. Opportunity for reference case study if launch succeeds and the agentic data content strategy drives meaningful traffic.

---

## Overview

- **Content Strategy Shift:** Prioritize high-volume keywords from competitor research to capture demand and drive initial traffic, deprioritizing topics with no search volume.
- **"Check That" Tool Refocus:** Revise prompts to target tool-based queries (e.g., "AI tools for data integration") where Airbyte can be a direct answer, driving high-intent traffic.
- **New Publishing Workflow:** Erik will draft all new articles in Webflow; Nithin will publish them post-launch to prevent accidental publication before the site is ready.
- **Website Fixes:** The "Agent Connectors" page requires fixes for a missing Granola icon and a misplaced Salesforce section.

---

## Key Topics

### Content Strategy & Keyword Prioritization

  - **Problem:** The Airtable topic backlog contains many topics with zero search volume, yielding no traffic.
  - **Solution:** Shift focus to high-volume keywords from competitor research to capture demand and drive initial traffic.
  - **Action:** Tanmay will review the competitor keyword list and the Airtable backlog, then share a prioritized list with Erik.
  - **Implementation:** Erik will add these to Airtable, potentially in a new "Competitor Keywords" cluster for clear tracking.

### "Check That" Tool Strategy

  - **Problem:** Current prompts for the "Check That" tool (which monitors how LLMs answer questions) are too generic, leading to informational answers that don't drive traffic to Airbyte.
  - **Solution:** Revise prompts to target tool-based queries where Airbyte can be a direct answer.
      - **Example:** "Platforms for building AI agents with direct connectors."
  - **Action:** Tanmay will send a new list of tool-based prompts to Erik.
  - **Implementation:** Erik will add these to the tool, using tags to group and filter prompts by topic.

### Publishing Workflow & Website Updates

  - **Context:** The main product launch is delayed until next Tuesday.
  - **New Workflow:** To prevent accidental publication before the site is ready, Erik will draft all new articles in Webflow, and Nithin will publish them after the launch.
  - **Website Fixes:**
      - **Agent Connectors Page:**
          - **Granola Icon:** Missing because it's not a "Data Replication" connector. Erik has a draft fix in Webflow.
          - **Salesforce Section:** A misplaced Salesforce section appears at the bottom of the Granola page. Erik will investigate with Kurt.
      - **Process:** All fixes must be staged for review before publishing. Nithin will monitor new connectors added via GitHub to ensure they display correctly.

---

## Action Items

**Kushal Chatterjee (Airbyte)**
- Review Erik's 'The Decline of RAG' article

**Erik O'Brien (GrowthX)**
- Draft all articles; coordinate w/ Nithin to publish
- Add 'New keywords' cluster in Airtable; import Tanmay's list
- Send CheckThat UI feedback to product re: single-line prompts
- Fix Granola page issue (shows Salesforce); coordinate w/ Kurt to stage
- Add 2 new agentic data articles to review

**Tanmay Sarkar (Airbyte)**
- Review keyword sheet; share prioritized list w/ Erik
- Send updated CheckThat prompts to Erik; then Erik uploads/tags
- Draft use-case landing page; share w/ Erik

**Nithin M (Airbyte)**
- Check internally if content exists for CheckThat prompts
- Publish Granola icon on Agent Connectors page (Webflow)
- Monitor GitHub for new connectors; ensure site accuracy

---

## Transcript
**Erik O'Brien:** Hey, Nithin.

**Erik O'Brien:** Just saw Tanmay said he was going to be about 5, 10 minutes late.

**Nithin:** Yep, yep.

**Erik O'Brien:** How's the week been?

**Erik O'Brien:** Big launch week?

**Nithin:** Actually, we couldn't launch it.

**Erik O'Brien:** Oh, no.

**Nithin:** It is pushed to next week.

**Erik O'Brien:** Gotcha.

**Nithin:** Tuesday, too.

**Nithin:** It might be on Tuesday.

**Nithin:** Yep.

**Nithin:** All the website, tech, like, content design, everything is ready.

**Erik O'Brien:** We just need to go live.

**Erik O'Brien:** Yeah.

**Kushal Chatterjee:** Thank you.

**Erik O'Brien:** Yeah, Tame is running like five to ten minutes late, so we're kind of just hanging out here, but.

**Kushal Chatterjee:** Okay, I'm on my commute, so let's just talk.

**Kushal Chatterjee:** Do you need anything from me?

**Kushal Chatterjee:** You guys can wait for Tame if you need anything from him.

**Erik O'Brien:** Yeah, I sent over the new Thought Leadership article for this week, The Decline of RAG, so I think that's the only action item for you.

**Kushal Chatterjee:** Okay, sweet.

**Kushal Chatterjee:** I'll take a look at it probably early next

**Erik O'Brien:** All right.

**Erik O'Brien:** Sounds like a plan.

**Kushal Chatterjee:** Sounds good.

**Kushal Chatterjee:** Talk to you guys later.

**Erik O'Brien:** See ya.

**Nithin:** All right.

**Erik O'Brien:** Efficient.

**Nithin:** Yep.

**Erik O'Brien:** Any questions on that updated list I sent over earlier this week?

**Nithin:** Just a couple things.

**Nithin:** I'm pulling it up, Erik, just a second.

**Nithin:** I'll share my screen.

**Nithin:** Okay.

**Nithin:** Can you hear my screen?

**Erik O'Brien:** Yep.

**Nithin:** Yep.

**Nithin:** Like, apart from published, all the others have not been written, correct?

**Erik O'Brien:** Correct.

**Nithin:** Okay, okay.

**Nithin:** Like, there are a couple of docs, but those are also published as well.

**Nithin:** Are there any that is written but not published, Erik?

**Erik O'Brien:** No, any of them that we had written had been published.

**Nithin:** Got it, got it.

**Nithin:** This one is skipped.

**Nithin:** And there is one more.

**Nithin:** Got it, Erik.

**Nithin:** So, we'll take it from here.

**Erik O'Brien:** That one that has a Google Doc, what was that one?

**Nithin:** Is there a link to the right of it?

**Nithin:** I don't have access to this.

**Erik O'Brien:** Is there a publish link to the right?

**Nithin:** Yes.

**Nithin:** So, yeah, I just forgot to flip that one to published.

**Nithin:** No problem, just published.

**Nithin:** Yep.

**Nithin:** Only that one.

**Nithin:** And others are, others look good.

**Nithin:** Take it from here.

**Nithin:** Thank you.

**Erik O'Brien:** Yep.

**Erik O'Brien:** And then for, um, the I want

**Erik O'Brien:** Updating the check that prompts, I saw there was some new Identic Data article prompts.

**Nithin:** Yes, yes.

**Nithin:** So yesterday we were trying to like look into the articles based on articles, what we have written and what we are going to check as prompts.

**Nithin:** So we didn't find like a proper correlation between the tool-based questions like where the answer is Airbyte.

**Nithin:** so we have positioned Airbyte, but it is not about, the whole article is not about Airbyte, like for example, whatever KV, a topic about KV caching, key value caching, but it is not that a tool needs to be an answer there.

**Nithin:** We have written like more information and stuff in the article.

**Nithin:** So we were trying to redo the prompts.

**Nithin:** So I have written the prompts.

**Nithin:** Once Tanmay gives a sign off, we can update it.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Wonderful.

**Tanmay Sarkar:** Eric.

**Erik O'Brien:** Hey, Tanmay.

**Nithin:** Hey, Tanmay.

**Tanmay Sarkar:** Yeah, I think we can start.

**Tanmay Sarkar:** Nobody else will try and probably forget.

**Erik O'Brien:** Great.

**Erik O'Brien:** It's been a busy week.

**Tanmay Sarkar:** It's busy week.

**Tanmay Sarkar:** Our kind of yearly meetup happened, back-to-back workshops, events, party.

**Tanmay Sarkar:** So I'm very tired.

**Erik O'Brien:** Yeah, I bet.

**Erik O'Brien:** And then Nithin was saying the launch got pushed back the next week.

**Tanmay Sarkar:** Yes, because everyone was busy and there was some error in the product.

**Tanmay Sarkar:** So we fixed it.

**Tanmay Sarkar:** So it took that this whole week.

**Nithin:** Yeah, single pages we can publish, Erik.

**Tanmay Sarkar:** Yeah, but if by chance, if they publish and everything go live, I would say what you can do, Erik, probably draft it.

**Tanmay Sarkar:** Don't publish.

**Tanmay Sarkar:** Just draft it on the website, Nithin can go ahead and click publish and publish.

**Tanmay Sarkar:** That we can do.

**Tanmay Sarkar:** You just draft all the articles in the category, Nithin can publish those.

**Nithin:** Yeah.

**Tanmay Sarkar:** You don't publish.

**Tanmay Sarkar:** Yeah, it would be better.

**Erik O'Brien:** Because your process is automated, if you publish and by chance, all the website goes live, then you're in a problem.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So we have been trying to use the kind of automated publishing through Atlas, and it's been giving us just a couple issues with like tables and any code snippets that we do have in there.

**Erik O'Brien:** So we've, we're probably going to do it manually, just to...

**Tanmay Sarkar:** That's fine.

**Tanmay Sarkar:** I think we have done competitor research and collected some keywords, which we will also share it with you.

**Tanmay Sarkar:** Meanwhile, if you go to, can you just screen and go to that air table master list of the topics?

**Erik O'Brien:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** So just go to the backlog ones, which we didn't write yet.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** No, there was a table which shows the volume as well for the keywords.

**Tanmay Sarkar:** I think ideas ready for you.

**Tanmay Sarkar:** Which one was that?

**Nithin:** All the tables has volumes.

**Nithin:** Yeah, Eric, you can go to by status and filter out all the others.

**Erik O'Brien:** This one?

**Nithin:** Yep.

**Nithin:** Here, yeah, filtered by status.

**Tanmay Sarkar:** No.

**Tanmay Sarkar:** There are so many.

**Nithin:** Yeah.

**Tanmay Sarkar:** This one has such volume?

**Nithin:** Yes, it does.

**Erik O'Brien:** This one does have four, a lot of them.

**Tanmay Sarkar:** Yeah, so you can see, this is for, okay, you can see clearly there is no volume.

**Erik O'Brien:** Yeah, that's what I was going to have Joe do, but I'll have the new managing editor kind of go in and fix these.

**Erik O'Brien:** I think from the original list that we got from you, I think when we were going through the strategy sprint, there was a lot of different keywords or topics that you recommended that didn't have search volume.

**Erik O'Brien:** So we went in and tried to update.

**Tanmay Sarkar:** Correct, correct.

**Tanmay Sarkar:** So my take is whatever we wrote till now, we can't undo that.

**Tanmay Sarkar:** Those are fine.

**Tanmay Sarkar:** We'll publish the space.

**Tanmay Sarkar:** But moving forward, the competitors' keywords list, which we have researched, that has huge search volume.

**Tanmay Sarkar:** So our priority should be writing those, not the ones which don't have any search volume, because those don't give us any tractions.

**Tanmay Sarkar:** So first, I would say we have to take this approach to capture demand because it's a product that we are building from scratch.

**Tanmay Sarkar:** So we need very much initial tractions on the website.

**Erik O'Brien:** Absolutely.

**Tanmay Sarkar:** So I'll review the list today and share it with you.

**Tanmay Sarkar:** Then you can add those in this list and move these things down.

**Tanmay Sarkar:** I think, Nithin, you have collected these also, right?

**Nithin:** And added in that sheet.

**Nithin:** This one's the considering one, right?

**Tanmay Sarkar:** So, you remember we talked yesterday, I told you to export this whole.

**Tanmay Sarkar:** Yeah, yeah.

**Tanmay Sarkar:** So all these are also added in that sheet?

**Nithin:** Not yet, I don't have edit access for this.

**Nithin:** I'm not able to put it, like, get it all.

**Tanmay Sarkar:** Not here, I'm talking like in that sheet.

**Nithin:** I know, I know.

**Tanmay Sarkar:** Okay, cool, cool.

**Tanmay Sarkar:** Yeah, I'll review the sheet and I'll share it with you, Erik.

**Tanmay Sarkar:** So, I'll just speak based on the keywords and remove some keywords which don't have volume.

**Erik O'Brien:** Probably any volume.

**Tanmay Sarkar:** And I will share you the list and then you can update it here.

**Tanmay Sarkar:** That's what I'm saying.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Perfect.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** We'll get it added to Airtable so we have a clean view of it.

**Erik O'Brien:** And then we will probably just add a different cluster for that competitor research and keywords.

**Tanmay Sarkar:** Just so we have visibility into that specifically.

**Tanmay Sarkar:** Yeah, sure.

**Tanmay Sarkar:** You can add that.

**Tanmay Sarkar:** But like in competitor keywords also, we will have these ones which we didn't write and I'll pick from there also which are the ones which has volume.

**Tanmay Sarkar:** So, yeah, you can just create a new list like new keywords or something.

**Erik O'Brien:** Perfect.

**Tanmay Sarkar:** Like are you asking that you will track these also based on like uncheck that or something or is just for you to understand which are the things.

**Tanmay Sarkar:** Thanks.

**Tanmay Sarkar:** Because it will be mixed of all clusters.

**Erik O'Brien:** It's not all one.

**Erik O'Brien:** Okay, I got you.

**Erik O'Brien:** Yeah, I thought you were just talking about the competitor-specific keywords, but I got you.

**Tanmay Sarkar:** Not competitor-specific, like whatever content they have produced, and they are ranking and getting interactions.

**Tanmay Sarkar:** It's any keywords.

**Erik O'Brien:** Perfect.

**Tanmay Sarkar:** That makes sense.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** The next thing which I wanted to talk is, how can we set up the check that, like I know current setup is there, but I want to set up it in a way where we can see that there will be obviously five, six topics or clusters, and each topic has, let's say, certain prompts, whatever we want to add.

**Tanmay Sarkar:** And I am, like, we have a prompt.

**Tanmay Sarkar:** I think we should create a list of prompts and the focus should be on tools or company-based keywords where there are probability to show the Airbyte name for example like what are the platforms where you can use direct connectors to build like to help AI agents then they say Airbyte, Marge, Composio, something like that.

**Tanmay Sarkar:** So these kind of prompts are very important because this gives you direct visibility.

**Tanmay Sarkar:** Others, let's say some definition like "what is data integration" and one of our articles is ranking—it might show different answers depending on the LLM, but people might not go to Airbyte website because that's just an informational query.

**Tanmay Sarkar:** So they get the answer from ChatGPT or Claude and they drop off, right?

**Tanmay Sarkar:** There's no action after that.

**Tanmay Sarkar:** So my belief is we should focus only or mostly those kind of keywords which will show the answer, like which will show Airbyte in the answer.

**Tanmay Sarkar:** Yes, you got my point.

**Tanmay Sarkar:** The query should be like that.

**Tanmay Sarkar:** So we have some keywords I'll send, sorry, prompts which I'll send you.

**Tanmay Sarkar:** But if you have any other thing, like how do you want to set up this, let me know.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** So you want to kind of like tag them separately so we can filter by like tool-based recommendations.

**Tanmay Sarkar:** Like currently, do you have any such filter?

**Tanmay Sarkar:** Like I will show you.

**Tanmay Sarkar:** So, do you have Profound access?

**Erik O'Brien:** Not for years, no.

**Tanmay Sarkar:** Okay, let me show you how it shows in Profound.

**Tanmay Sarkar:** Can you see my screen?

**Erik O'Brien:** Yep.

**Tanmay Sarkar:** So we have two instances.

**Tanmay Sarkar:** This is for the old product.

**Tanmay Sarkar:** This is for the new product.

**Tanmay Sarkar:** So prompts are grouped by topic. You can see here. You can also go by region to see different markets.

**Tanmay Sarkar:** Okay, if I try to add a tag, what can I add?

**Tanmay Sarkar:** Okay, I hope I can add a tag.

**Erik O'Brien:** So yeah, we don't have any tags right now, so we can kind of start from scratch.

**Erik O'Brien:** As we continue to add prompts, just make sure we tag them correctly.

**Tanmay Sarkar:** Cool.

**Tanmay Sarkar:** And the topics or the prompts that we have added here, do we have content on all these prompts?

**Erik O'Brien:** I think that was the content we developed last week from that question list that you sent us of like the tool-based topics.

**Erik O'Brien:** And so I don't know if we have it for AI tools for data integration, but if we don't, that's stuff we can put in the backlog.

**Tanmay Sarkar:** Okay, what is the tag?

**Erik O'Brien:** Archive?

**Erik O'Brien:** Yeah.

**Tanmay Sarkar:** So it'll stop tracking it in the overall view.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** I think, like, it's kind of showing like this, but if you make it in one line, that would look better because here it's tough to read also.

**Tanmay Sarkar:** Like, I'm just telling, like, you can share this feedback with the product link.

**Erik O'Brien:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** I think what we can do is, Nithin has access to this now, right?

**Erik O'Brien:** Yeah.

**Nithin:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Okay.

**Tanmay Sarkar:** So what we can check internally, if we have produced the content for this or not, you can also check it.

**Tanmay Sarkar:** And then we can just upload a new list of prompts and check that and rank those.

**Tanmay Sarkar:** Yeah.

**Erik O'Brien:** Or if you just want to send me the list, I'm happy to do that, too.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Once we are done, we will send you the list.

**Tanmay Sarkar:** Where are these prompts?

**Tanmay Sarkar:** Like, like, is there any country or region?

**Erik O'Brien:** It's just, overall, once we send it to the LLMs.

**Tanmay Sarkar:** No, like, from where, like, let's say, I have not picked any country, I think.

**Tanmay Sarkar:** So how do you decide from which country you are asking this?

**Tanmay Sarkar:** Because Profound has this feature called Regions.

**Tanmay Sarkar:** I have added all the Regions.

**Tanmay Sarkar:** So it shows me visibility based on Regions.

**Tanmay Sarkar:** You can see?

**Erik O'Brien:** So is that, like, based off the region, it'll give you different answers?

**Tanmay Sarkar:** Yes, yes, there are chances.

**Tanmay Sarkar:** It doesn't give same answer to everyone.

**Tanmay Sarkar:** Probably all of our servers are U.S. based.

**Tanmay Sarkar:** Okay, cool.

**Tanmay Sarkar:** Yeah, let's do this.

**Tanmay Sarkar:** Yeah, I think these are the two main things which I wanted to discuss.

**Tanmay Sarkar:** And third thing is case study, sorry, not case study, use case landing page, which you have sent.

**Tanmay Sarkar:** I have checked that and I am also doing my research and trying to make a page.

**Tanmay Sarkar:** I will work on that probably from next week on the use case landing page and share with you.

**Tanmay Sarkar:** Then we have to think how we can programmatically build that to expand.

**Tanmay Sarkar:** Yeah, I have already started working on the landing page how I want it, but it's not yet ready.

**Tanmay Sarkar:** So, we basically, that's not the final version.

**Tanmay Sarkar:** I'm thinking through seeing more use case pages doing research.

**Tanmay Sarkar:** So, we'll share it soon, and then probably we can do it from there.

**Erik O'Brien:** Okay, that works.

**Erik O'Brien:** Just a quick note on the Agent Connectors page.

**Erik O'Brien:** I noticed that Granola is a new connector that wasn't supported by Data Replication, so it's missing its icon.

**Tanmay Sarkar:** I updated that in Webflow.

**Tanmay Sarkar:** You've seen Agent Connectors?

**Erik O'Brien:** Yep.

**Tanmay Sarkar:** So then let me check it right now.

**Erik O'Brien:** Yes, I drafted the update in Webflow, but I didn't hit publish.

**Erik O'Brien:** So it'll show the logo there.

**Nithin:** Okay.

**Nithin:** I'll take it.

**Tanmay Sarkar:** Okay.

**Erik O'Brien:** Yeah, I tried to look and it didn't, I didn't see the granola as a like data replication connector.

**Erik O'Brien:** So it wasn't able to automatically pull the logo from that.

**Tanmay Sarkar:** I see.

**Tanmay Sarkar:** Nithin, there are some issues also, I think.

**Tanmay Sarkar:** If you go down to granola page, you can see it's showing Salesforce.

**Tanmay Sarkar:** This was connected.

**Tanmay Sarkar:** Can you see, Erik?

**Tanmay Sarkar:** Just scroll down at the end.

**Nithin:** Yeah.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** I think you can take internally what is the issue.

**Erik O'Brien:** Yeah.

**Tanmay Sarkar:** Just make sure you don't publish anything.

**Tanmay Sarkar:** Push it to staging.

**Tanmay Sarkar:** We take care of that after that.

**Tanmay Sarkar:** Just to update in the flow and don't publish.

**Tanmay Sarkar:** And yeah, whenever we launch any new connectors, Nithin, just keep an eye.

**Tanmay Sarkar:** Because whenever engineering team is adding a new connector in GitHub, it is populating automatically on our site.

**Tanmay Sarkar:** Yes.

**Tanmay Sarkar:** So we should make sure that everything that is showing there is correct here too.

**Tanmay Sarkar:** Oh, I think the below box is Salesforce, for example.

**Tanmay Sarkar:** Is that a part of design or like it was like that or no?

**Tanmay Sarkar:** Erik, do you know?

**Erik O'Brien:** I don't know if that was in the template and it just got pulled over, but I will.

**Erik O'Brien:** Yeah, you can check.

**Erik O'Brien:** We should just be able to kind of replicate this with a different copy.

**Tanmay Sarkar:** Yeah, so whatever page is that, we should just use that thing there as well.

**Erik O'Brien:** Okay, yep.

**Erik O'Brien:** I'll talk to Kurt and get it updated and have him stage it.

**Erik O'Brien:** We'll stage it and then I'll let you know.

**Tanmay Sarkar:** Yeah, yep, yep.

**Tanmay Sarkar:** Makes sense.

**Tanmay Sarkar:** Cool.

**Tanmay Sarkar:** Works.

**Tanmay Sarkar:** Awesome.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** I know we didn't get to the typical update this week, but we've got 15 agentic data articles in the review stage.

**Erik O'Brien:** And then I got two more that we're just wrapping up today that I'll push on there when they're ready.

**Tanmay Sarkar:** Yeah.

**Tanmay Sarkar:** Yeah, that's fine.

**Tanmay Sarkar:** I'll check all the agentic articles, and you can just add it to draft, and Nithin will then take care of publishing for just this week until we make those things live.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Sounds like a plan.

**Tanmay Sarkar:** Okay.

**Erik O'Brien:** All right.

**Tanmay Sarkar:** Thanks, Erik.

**Erik O'Brien:** Thanks, guys.

**Erik O'Brien:** Have a good weekend, and safe travels next week, TMA.

**Tanmay Sarkar:** Yep.

**Tanmay Sarkar:** Thank you.

**Nithin:** Bye.

**Erik O'Brien:** Bye.
