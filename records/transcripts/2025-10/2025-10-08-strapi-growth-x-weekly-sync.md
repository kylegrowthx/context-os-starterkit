# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-10-08
time: 16:28 UTC
duration: 29 minutes
organizer: Mara Leighton (GrowthX)
participants: Victor Coisne (Strapi), Vivek Shankar (GrowthX), Theodore Kelechukwu Onyejiaku (Strapi), Mara Leighton (GrowthX), Golzar Yaghoubpour (Strapi)
fathom_recording_id: 92767219
fathom_url: https://fathom.video/calls/434294636
share_url: https://fathom.video/share/VRaUq9x7stsBZq-42W5Xc64EzzL16Wcd
source: fathom
enriched_on: 2026-03-02 14:32 UTC
</metadata>

---

## Summary

GrowthX and Strapi reviewed content production metrics (9 articles delivered, 7 scheduled), confirmed progress on multiple workflow implementations (comparison pages, CMS publishing, Medium integration), and prioritized FAQ automation across key page types. The team decided to narrow scope on content gap analysis by starting with Kappa's existing feature rather than building a new work stream, with Vivek committing to validate feasibility by end of week. Performance data showed strong LLM visibility across most categories, positive trending on influenced contacts, and new content creation as the key metric for top-of-funnel growth.

---

## Context

This is an ongoing weekly operational sync between GrowthX (content and SEO services) and Strapi (a headless CMS platform). GrowthX is responsible for creating content and optimizing SEO/LLM visibility for Strapi, with the engagement focused on driving top-of-funnel awareness and new contact generation. The meeting covers content delivery cadence, workflow automation progress (integration of Strapi's CMS with GrowthX's publishing pipelines), and performance metrics across search, HubSpot conversion events, and LLM prompt visibility. Victor Coisne leads strategy for Strapi, while Vivek Shankar and Mara Leighton manage execution on the GrowthX side.

---

## Relevance

**To GrowthX Delivery:**
- Content production velocity is strong (9 delivered, 7 scheduled weekly); comparison pages workflow is now moving to competitor-vs-competitor variants
- FAQ automation represents a pragmatic quick-win: can be integrated into existing content generation workflows without new tool development
- CMS publishing workflow is nearly complete despite minor code block display issues; Medium API deprecation is blocking H2/H3 formatting but testing underway
- ImageGen automation delayed but in progress; team exploring Notebook.lm as a lower-effort alternative for video content creation

**To CheckThat:**
- Strapi shows strong LLM visibility across 15 tracked prompt categories; only lagging in 4 categories (customizable admin interfaces, database options, Git-based workflows, self-hosted vs cloud)
- Contentful is the primary competitor limiting Strapi visibility in database-related prompts; recommend competitive content focus there
- FAQ and question-based H2/H3 formatting strategy appears effective for LLM visibility

**To GrowthX Business Development:**
- Strapi account is healthy: production on track, strategic alignment clear (new contacts/top-of-funnel focus), and expanding scope (FAQ automation, content refresh strategy)
- Social media automation out of scope due to engineering constraints; represents potential future expansion opportunity if priorities shift
- Notebook.lm video content strategy may become repeatable pattern across other clients; worth tracking for future service offerings

---

## Overview

- 9 articles delivered last week, 7 scheduled for this week; content production on track with focus on high-performing pages
- Multiple workflows nearing completion: comparison pages ready to proceed with competitor-vs-competitor variants; CMS publishing workflow done except for minor code block display issues; Medium integration staged despite API deprecation H2/H3 formatting limitation
- Social post automation confirmed out of scope for now; narrowed content gap analysis scope to leverage Kappa's existing feature rather than build new work stream
- Strong LLM visibility across most prompt categories (ahead of Contentful in all but database options); new contacts trending positively; FAQ automation prioritized for landing pages, feature pages, and use cases

---

## Key Topics

### Content Production and Workflow Updates

  - 9 articles delivered last week, 7 scheduled for this week
  - Comparison pages staged; proceeding with competitor vs. competitor pages
  - Integration page workflow testing in progress
  - CMS publishing workflow nearly complete; minor issues with code block display
  - Medium workflow staged; facing H2/H3 formatting limitations due to API deprecation
  - ImageGen publishing automation in progress; styling refinements ongoing

### Content Gap Analysis and Ideation

  - Discussed narrowing scope to existing workflow vs. new work stream
  - Exploring Kappa's content gap feature as starting point
  - Victor suggested focusing on auto-tagging questions lacking bot answers
  - Team to investigate feasibility and provide update by week's end

### FAQ Implementation

  - Victor proposed automating FAQ addition to various page types
  - Currently done manually for some feature pages
  - Vivek: No separate workflow, but can be incorporated into content generation
  - Agreement to prioritize adding FAQs to landing pages, feature pages, and use cases

### Performance Metrics

  - Slight dip in non-branded impressions, potentially due to Google updates
  - HubSpot data shows sessions ahead of goals; influenced contacts trending positively
  - LLM visibility strong across most prompt categories
  - Focus on new contacts as key metric for top-of-funnel performance

### Content Optimization Strategy

  - Emphasis on refining high-performing GrowthX-created pages
  - Refreshing older content underway (2 pieces this week)
  - Exploring video addition to boost SERP visibility and user experience
  - Considering tools like Notebook.lm for efficient video creation

---

## Action Items

**Vivek Shankar (GrowthX)**
- Follow up with Jason re social media content redistribution workflow mentioned by Gong. Report back findings.

- Explore using Kappa for content gap identification. Check with engineering on scope/resourcing. Provide answer by end of week.

- Merge issues for extrapolating send info & content gap monitoring into single tracking item.

- Add FAQs to existing content (comparator, integration, new, refresh pages). Prioritize landing pages, then assess blog posts for enhancement.

- Refine performance table in reports to show only GrowthX-created pages.

- Add new content topics to Airtable for Theodore's review (for pipeline ~2.5 weeks out).

---

## Transcript
**Victor Coisne:** Hey, Vivek, how are you?

**Vivek Shankar:** Hey, Victor, how are you?

**Victor Coisne:** I'm good.

**Vivek Shankar:** Excited to hear it.

**Victor Coisne:** Me as well.

**Vivek Shankar:** No, I'm good as well.

**Vivek Shankar:** I was saying it's a little cold where I'm at, so I got my layers on and everything.

**Victor Coisne:** Where are you at?

**Vivek Shankar:** I am in Peru right now, so yeah, I'll be here for this month, and then I'm back in Lisbon end of this month.

**Victor Coisne:** Fun.

**Victor Coisne:** Exciting.

**Vivek Shankar:** Yeah, it's nice.

**Vivek Shankar:** Yeah, going on a few hikes and whatnot.

**Vivek Shankar:** So it's pretty good for all that.

**Victor Coisne:** That's awesome.

**Victor Coisne:** I've never been, but it's on my list.

**Vivek Shankar:** Yeah, it's pretty awesome.

**Vivek Shankar:** We've been going around a little bit.

**Vivek Shankar:** The altitude is a bit of a challenge.

**Vivek Shankar:** Sometimes you literally can't breathe, but you get used to it after a while.

**Victor Coisne:** Right.

**Victor Coisne:** Awesome.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** How's everything going?

**Victor Coisne:** It's good.

**Victor Coisne:** It's launch day today.

**Victor Coisne:** We had a big, big launch.

**Victor Coisne:** So, yeah, we're waiting to see if the, you know, the community and the customers are happy about it.

**Vivek Shankar:** Nice.

**Vivek Shankar:** Hey, Mara.

**Victor Coisne:** Hey, Golzar.

**Victor Coisne:** Hey, Mara, Golzar.

**Mara Leighton:** Hey, how's it going?

**Victor Coisne:** Good, good.

**Vivek Shankar:** Thank you for joining us.

**Vivek Shankar:** Well, I guess we're waiting on Paul.

**Victor Coisne:** I think Paul is not going to join today because he's at a conference.

**Vivek Shankar:** Okay, cool.

**Victor Coisne:** Hey, Theo.

**Theodore Kelechukwu Onyejiaku:** Hi, everyone.

**Vivek Shankar:** All right, let me share my screen and then get started.

**Vivek Shankar:** Sorry, I'm still getting used to Zoom a little bit.

**Vivek Shankar:** Okay, should be good now.

**Vivek Shankar:** Okay, just walking through the updates.

**Vivek Shankar:** So new content, we delivered nine articles last week.

**Vivek Shankar:** We've got seven scheduled for this week.

**Vivek Shankar:** Generally, things are going pretty smooth over there.

**Vivek Shankar:** I thought I could walk through the action items real quick because we made some updates over here.

**Vivek Shankar:** So the first one, just wanted to get your clarification.

**Vivek Shankar:** We staged all the comparison pages, so strapi versus competitor pages.

**Vivek Shankar:** I know there are more pages, like competitor versus competitor.

**Vivek Shankar:** Not sure if you want us to...

**Vivek Shankar:** Do with that before making changes to the pages, or do you want to get started with it right now?

**Vivek Shankar:** So I just wanted to check about that.

**Victor Coisne:** I think we can proceed with the competitor pages. That sounds good to me.

**Vivek Shankar:** So there were some add-on action items like widening the comparison page columns.

**Vivek Shankar:** So we'll do that after the competitor versus competitor pages are done.

**Victor Coisne:** Yeah, sounds good.

**Theodore Kelechukwu Onyejiaku:** I think Paul already created an issue for that. So you can go ahead with other tasks.

**Vivek Shankar:** Good. The next thing is the integration page workflow. We're testing it today and it's almost done.

**Vivek Shankar:** Just a fair warning—there will be one or two dummy pages showing up as drafts in the CMS while we test whether the meta updates are going out. The next thing is the CMS publishing workflow, which is almost done.

**Vivek Shankar:** We're having some weird issues with code block display, but generally it's pretty much done and we're using the flow to stage articles within the CMS. The next issue is the Medium workflow.

**Vivek Shankar:** Theodore sent a few Slack threads about this.

**Vivek Shankar:** Basically, we staged a test article in Medium. The problem is that all the H3s and H2s are defaulted to H3 because of how Medium's API handles it.

**Vivek Shankar:** The engineer says the API has been deprecated with no documentation, so we're not sure how to fix it. But it's there for you to test.

**Vivek Shankar:** If you can look at it and let us know if everything is good. We reviewed the latest fixes and everything seemed to be taken care of.

**Victor Coisne:** Yeah, I'll give you a review by the end of tomorrow.

**Vivek Shankar:** Awesome, sounds good.

**Vivek Shankar:** The next one, based on Paul's request last week, is the social posts.

**Vivek Shankar:** We checked with engineering and this is out of scope for us right now. Given our engineering priorities and resources, we might not be able to build a workflow.

**Vivek Shankar:** That would completely satisfy your needs. Unfortunately, we cannot work on this right now. We can address it later, but it's not in the priority queue.

**Victor Coisne:** I have a question on this one.

**Victor Coisne:** You're not doing anything like that with any other customer?

**Vivek Shankar:** Currently, we don't.

**Vivek Shankar:** We don't actually automate social posts or social post creation based on existing content.

**Victor Coisne:** Okay.

**Victor Coisne:** All right.

**Victor Coisne:** We'll investigate Fathom.

**Victor Coisne:** Yeah.

**Theodore Kelechukwu Onyejiaku:** I remember Gong saying something like brand or personal brand content redistribution on socials.

**Theodore Kelechukwu Onyejiaku:** I think there was something he said related to you having a workflow that helps with social media.

**Vivek Shankar:** I can check with Jason about that, but as far as I know, and based on current priorities, I think it's not feasible for us to build this out.

**Vivek Shankar:** I think the main concern is that social posts generally require a lot of testing in terms of voice, and we just want to make sure we get it right.

**Vivek Shankar:** So I think given existing priorities, just fine-tuning that, there's not much space for us.

**Vivek Shankar:** I think that's the real thing, but I'll follow up with Jason just to check what he informed you and get back to you.

**Victor Coisne:** That sounds good.

**Vivek Shankar:** For the next two issues, I created a separate discussion. Basically, Paul mentioned monitoring for content gaps and generating content ideas.

**Vivek Shankar:** I followed up with Paul, who sent a few sources in Slack.

**Vivek Shankar:** Strapi is using a tool to gather everything in one place and monitor additional sources like GitHub. Paul's feedback was that it takes a lot of manual work.

**Vivek Shankar:** We're building this as a separate work stream for our other clients. I wanted to discuss how we can deliver the output for you.

**Vivek Shankar:** Essentially, we'd monitor different sources and generate a content digest—what was discussed this past week, what's popular, and which topics make sense strategically.

**Vivek Shankar:** We're thinking of it as a work stream rather than one particular workflow. And this would apply to all your content, not just what we're creating.

**Vivek Shankar:** I wanted to highlight that it can be tool agnostic or we can use your current tool. But I want to point out that this would be a separate work stream with broader scope than one particular workflow.

**Victor Coisne:** To be honest, to me it feels like a step in the existing workflow—a discovery step—rather than a whole new work stream. It's more like research on content gaps. I'd see it as part of the existing workflow to automate the manual work that Theo, Paul, and the team do on identifying topics.

**Victor Coisne:** It's complementary to research on keyword ranking and search volume. Pragmatically, I'd narrow scope first and deliver value as part of the existing work stream rather than building something new.

**Vivek Shankar:** Fair enough. We can check on the scope with engineering. And if it's easier, we can create a webhook to your existing tool—Octolence.

**Victor Coisne:** That was the one that Paul had mentioned.

**Vivek Shankar:** Yeah, that's Octolence.

**Victor Coisne:** If we want to start small and iterate, we can potentially start with Kappa—we already have it as a fact checker.

**Victor Coisne:** Kappa just released a new feature that looks for content gaps. Now the chatbot is deployed across our entire website.

**Victor Coisne:** We're getting a lot more questions, and sometimes the bot has no information to answer. Kappa's feature auto-tags questions with missing sources or data.

**Victor Coisne:** That's our content gap right there. We can start with Kappa's content gap and over time add social gaps or Octolence data.

**Vivek Shankar:** Sure, we can explore that. I'll check internally on resourcing and have an answer by end of week.

**Vivek Shankar:** Next is ImageGen publishing automation.

**Vivek Shankar:** We're trying to generate images based on the Figma board. There are a few hiccups—images are finicky and we want to get the styling right.

**Vivek Shankar:** We should have an update in the next few days. It's in progress.

**Vivek Shankar:** The last one is extrapolating send information—it's tied to the discussion we just had. Paul sent that information, so we can tie this to the other issue.

**Victor Coisne:** Yeah, I think it'd be good to merge them so we track everything in one place.

**Victor Coisne:** I know you guys work with Webflow quite a bit as a customer.

**Victor Coisne:** I know Josh Grant, the CMO of Webflow, and he's looking at some content they've been doing with Aerobes.

**Victor Coisne:** What's working really well for them is adding FAQs to all their pages.

**Victor Coisne:** This is something where I see a gap. I've started doing it on some feature pages, but it seems like it could be easily automated rather than done manually.

**Victor Coisne:** Is there a workflow where we could identify pages where an FAQ would make sense and add them automatically?

**Vivek Shankar:** From what I know, there's no independent workflow for it. FAQs are generated as part of regular content generation.

**Vivek Shankar:** Adding FAQs is good for SEO, especially on topics that attract a lot of questions.

**Vivek Shankar:** In terms of LLM visibility, FAQs do help.

**Vivek Shankar:** One way we address this is by formatting H2s and H3s as questions to make topics explicit.

**Vivek Shankar:** That way, LLMs view them as questions and answers. In terms of adding FAQs to content we generate, we can certainly do that.

**Vivek Shankar:** That's where we're at.

**Victor Coisne:** Yeah, I think it'd be good to start adding that to our existing workstream—comparator pages, integration pages, new content, refresh content.

**Victor Coisne:** For your Strapi integration—Atlas to Strapi—are you doing actual field mapping where you can say this goes into that field, or is it just dumped into the text editor?

**Vivek Shankar:** No, I think there is a field mapping that's happening there.

**Victor Coisne:** Okay, cool.

**Victor Coisne:** Because it would be easy to format in a spreadsheet—questions and answers—and add them to those pages.

**Victor Coisne:** It seems like a pretty easy win.

**Vivek Shankar:** Yeah, for sure. We're doing FAQs on integration pages and comparison pages as well.

**Vivek Shankar:** Landing pages should be the priority. For blog pages, we can see which ones we can enhance.

**Vivek Shankar:** As part of periodic refreshes, we can certainly add FAQ elements.

**Victor Coisne:** Yeah, sounds good.

**Victor Coisne:** Yeah, for me, feature pages would be a good one—features, use cases, and other parts of the site that would really benefit from FAQs.

**Vivek Shankar:** Yeah, we can look at that and prioritize refreshes over the next few weeks.

**Victor Coisne:** That sounds good.

**Vivek Shankar:** So moving on to the performance side of things—yeah, we made a high about two weeks ago and we're slightly off of it right now.

**Vivek Shankar:** This past week, the top five pages included an integration page created by GrowthX.

**Vivek Shankar:** Performance seems to be holding pretty decently. Non-branded impressions fell last week.

**Vivek Shankar:** It may be tied to Google updates from the past couple weeks. I recommend waiting.

**Vivek Shankar:** All accounts seem to be losing non-branded impressions, so it's a widespread issue.

**Vivek Shankar:** I've included HubSpot data in this report. Looking forward to your feedback on whether this is what you want to see.

**Vivek Shankar:** In terms of conversion events, clicks on contact sales link and pricing increase week on week.

**Vivek Shankar:** We're ahead of our stated goals on sessions. Influenced contacts declined since January, but we're heading in the right direction compared to last month and reversed the decline from June.

**Vivek Shankar:** On LLM visibility:

**Vivek Shankar:** So this data comes from Scrunch. Generally, things are looking good for prompt software tracking.

**Vivek Shankar:** Strapi appears more often and in higher positions than competitors. Positioning is towards the top and middle, not the bottom. Sentiment is overwhelmingly positive.

**Vivek Shankar:** We're ahead of competitors in pretty much all prompt categories.

**Vivek Shankar:** We track 15 categories. We're lagging in customizable admin interfaces, database options, Git-based deploying workflows, and self-hosted versus cloud CMS.

**Vivek Shankar:** Contentful outpaces us in database options for content management. In the rest, we're ahead. Overall, performance is strong.

**Vivek Shankar:** We have a solid topic pipeline for the next few weeks—topics that Theodore and Paul have marked as well as high-opportunity ones we identified.

**Vivek Shankar:** We'll continue with competitor and comparison pages to boost LLM visibility. That covers the performance update. If you need additional HubSpot data, let us know.

**Victor Coisne:** On that note, new contacts are key. The overall workflow is non-branded keyword search leading to new users creating contact.

**Victor Coisne:** We want to bring new folks to the site and ensure they create contacts. New contacts are very important.

**Victor Coisne:** That's why we focus on those events. We're top of funnel, so attribution isn't perfect—many users just run commands and install locally without creating contacts.

**Victor Coisne:** It's a bit of a black box with open source. Anyway, new contacts are important. Looking at the top five pages' performance would help.

**Victor Coisne:** React CMS is a Strapi integration type, right?

**Vivek Shankar:** Yes, React and Next.js are yours.

**Victor Coisne:** I think it would be good to focus on GrowthX-created pages. GrowthX is giving us more shots on goal, and when we score, those are clearly our goals.

**Victor Coisne:** I want to extract everything from those goals. For content already ranking and seeing success, we should keep making it better—maybe through refreshing. That's an impactful way to optimize what's working.

**Vivek Shankar:** Totally on board with that. I went to the top five to give a holistic view since you wanted to track integration pages too.

**Vivek Shankar:** And we've started looking at past content that could use a refresh.

**Vivek Shankar:** This week we're doing a couple of actual content refreshes—not just adding updates on top as before. We'll refine this table to show only GrowthX-created pages.

**Victor Coisne:** Yeah.

**Victor Coisne:** What I've heard—and I'm not sure if it's a fact—but adding a video to an article can sometimes really lift the results.

**Victor Coisne:** Because it starts showing up in, like, SERP and, like, you know, with the video meta and whatnot.

**Victor Coisne:** So that's what I mean by keep optimizing.

**Victor Coisne:** If we see something that's working really well, we can create a short video that speaks to the topic and to make the post even more appealing or maybe add some images when we have that workflow finally working.

**Victor Coisne:** Just how do we make it more visual and even more pleasant to read from the end user experience?

**Vivek Shankar:** Yeah, for sure. Anything that improves UX is always good. Video is interesting because now there are tools like Notebook.lm where you can put the article into it and it generates a video. So the effort required to improve UX on the page is definitely decreased.

**Vivek Shankar:** So it's something we can definitely look at.

**Vivek Shankar:** Of course, we're working on the image flow, but you have video as well.

**Vivek Shankar:** So we do have another client that's kind of experimenting with it.

**Vivek Shankar:** So basically, they take their podcast, documentation, and research reports, put them into Notebook.LM, and it generates a custom video that they upload to YouTube and embed in blogs.

**Vivek Shankar:** So that's another approach in terms of content redistribution.

**Vivek Shankar:** So yeah, that was pretty much the update for this week. We'll follow up on all the issues discussed.

**Theodore Kelechukwu Onyejiaku:** Yeah, about the topics—are we expecting the list of topics on Airtable this week so we could approve?

**Vivek Shankar:** We already have quite a few topics in the pipeline that you'd approved previously. We prioritized those plus the ones you and Paul sent over a couple weeks back. New topics will show up in another two to two-and-a-half weeks. I'll add some topics in there for you, Theodore.

**Theodore Kelechukwu Onyejiaku:** All right.

**Theodore Kelechukwu Onyejiaku:** Thank you.

**Victor Coisne:** One question, like, and it's related to, you know, your message, Theo, like, Usman said there's 54 articles that are currently staged and waiting for us to review.

**Theodore Kelechukwu Onyejiaku:** That seems like a lot. Yeah, he said it and Paul and I had to react, and we discovered it was a mistake on his side.

**Victor Coisne:** Yeah, there's not 54 articles that are staged.

**Vivek Shankar:** No, no.

**Vivek Shankar:** Yeah, I think the number is closer to 20.

**Vivek Shankar:** was a bit of a mistake on Usman's part.

**Vivek Shankar:** He was looking at wrong statuses within the CMS.

**Theodore Kelechukwu Onyejiaku:** So it was just a question of updating Airtable on our end. The ones in staging are the drafts, comparators, and some article updates that need review.

**Victor Coisne:** Okay.

**Victor Coisne:** Okay, good.

**Victor Coisne:** Sounds good.

**Vivek Shankar:** All right.

**Vivek Shankar:** Yeah, that was pretty much it.

**Vivek Shankar:** So we'll follow up on everything.

**Vivek Shankar:** And yeah, I'll drop some updates regarding the issues that we discussed.

**Vivek Shankar:** And we'll take it forward from there.

**Victor Coisne:** Thank you.

**Mara Leighton:** Thanks, guys.

**Victor Coisne:** Nice to see you.

**Golzar Y.:** Yeah.

**Vivek Shankar:** I can see you.

**Mara Leighton:** Bye.
