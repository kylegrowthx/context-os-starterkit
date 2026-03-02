# Strapi <> Growth X -  Weekly Sync

<metadata>
date: 2025-12-10
time: 17:00 UTC
duration: 27 minutes
organizer: team@growthxlabs.com
participants: Vivek Shankar, Theodore Kelechukwu Onyejiaku, Victor Coisne
fathom_recording_id: 107750204
fathom_url: https://fathom.video/calls/500566179
share_url: https://fathom.video/share/Az6Z4L-Y67exPJSJx-rg8minetK2cb-C
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

GrowthX and Strapi aligned on content publishing priorities: Theodore will publish 28 pages (comparators, integrations, blogs) by end of week after light review, with integration pages prioritized due to their impact on partner backlinks. The team also discussed a critical FAQ bug causing some pages to display FAQs open by default despite CMS settings — Victor will escalate to the web agency (Notum) while GrowthX standardizes FAQ placement above related articles. Most significantly, Victor proposed a new "Jump the Wave" workflow using Airtable to capture trending topics (like the React security vulnerability) so GrowthX can rapidly draft content and Strapi can polish and promote it, with future automation planned for the Atlas platform.

---

## Context

This is a weekly sync between GrowthX (a B2B content marketing agency) and Strapi (a headless CMS company), representing an ongoing partnership where GrowthX produces content for Strapi's website to drive SEO visibility and lead generation. Strapi is a major client and strategic partner; GrowthX recently shifted from focusing on broad GA4 metrics to HubSpot contact attribution to better measure content impact. Victor Coisne replaced GoalsR as Strapi's point of contact at the start of this call. The timing aligns with December's strong performance (driven partly by news of Anthropic acquiring Bun), and the team is planning for Q1 by mapping new integration pages and targeting the agency owner persona.

---

## Relevance

**To GrowthX Delivery:**
- New "Jump the Wave" workflow (Airtable interface) will formalize rapid-response content creation for trending topics — GrowthX drafts, Strapi polishes internally, then heavy promotion. This addresses a gap exposed by missing content on the React security vulnerability.
- Established FAQ standardization (placement above related articles) — GrowthX will enforce this across all new integration pages starting immediately.
- Monthly reporting shifting from GA4 to HubSpot data for clearer attribution of GrowthX's impact on contact generation.

**To GrowthX Business Development:**
- Integration pages are proving high-impact (partner backlinks, strong performance metrics) — doubling down on this category signals expansion opportunity for 2026.
- Q1 content planning includes agency owner persona targeting (in addition to developer focus) — represents potential new vertical or persona for account growth.
- December performance off to strong start with increased conversion events (pricing link clicks, contact sales link clicks) — healthy signal for renewal and upsell conversations.

**To CheckThat:**
- LLM referral traffic remains low (~1k/week) — opportunity to audit CheckThat's visibility strategy or product positioning in Strapi content.

---

## Overview

- **Content Pipeline Unblocked:** Theo will publish 28 pages (comparators, integrations, blogs) by EOW, prioritizing integration pages due to their high impact on partner backlinks.
- **FAQ Bug Fix:** A web agency bug is causing FAQs to display open by default. Victor will create an issue for a fix, while GrowthX will standardize their placement above related articles.
- **New "Jump the Wave" Workflow:** A new Airtable will capture urgent topics (e.g., React vulnerabilities) for rapid content creation, enabling Strapi to capitalize on trending news.
- **Performance Reporting Shift:** GA4 data is too broad. Monthly reporting will now focus on HubSpot to isolate and measure the direct impact of GrowthX content.

---

## Key Topics

### Content Pipeline & Publishing

  - **Blocker:** Theo was blocked from publishing 28 pages by a broken preview feature on comparator pages.
  - **Resolution:** Victor advised publishing with a light review.
      - **Rationale:** Comparator pages receive low traffic, and their large tables are being removed, making the preview issue a low priority.
  - **Video Update:** Add the "Getting Started with Strapi V5" video to all comparator pages as the default.
      - **Exception:** Use more specific videos (e.g., the WordPress migration webinar) where a better fit exists.

### FAQ Bug & Placement

  - **Problem:** FAQs on some pages are stuck open, despite the CMS toggle being set to "false."
  - **Cause:** A web agency bug, not a CMS configuration error.
  - **Action → Bug Fix:** Victor will create an issue for the web agency (Notum) to fix the bug.
  - **Action → Placement Standard:** GrowthX will standardize FAQ placement *above* the related articles section.
      - **Rationale:** This places the FAQ in the user's immediate reading flow, whereas related articles are primarily for SEO.

### Performance & Strategy

  - **December Performance:** Off to a strong start.
      - **Traffic Spike:** The "BUN vs. Node.js" page saw a \~230% traffic increase, driven by news of BUN's acquisition by Anthropic.
      - **Conversion Events:** Increased WoW, with "Click on pricing link" and "Click on contact sales link" showing the most growth.
      - **LLM Referral Traffic:** Remains low at \~1k/week.
  - **Reporting Focus:** Shift from GA4 to HubSpot for monthly reporting.
      - **Rationale:** GA4's last-touch attribution is too broad to isolate GrowthX's impact. HubSpot provides a clearer view of contacts created by GrowthX content.
  - **Q1 Content Planning:** GrowthX will propose topics for new integration pages and content targeting the agency owner persona by mid-next week.

### New "Jump the Wave" Workflow

  - **Problem:** Strapi cannot quickly create content for trending news (e.g., React security vulnerability).
  - **Solution:** A new workflow to capture and prioritize urgent topics.
      - **Mechanism:** GrowthX will create an Airtable interface for Strapi to submit topics.
      - **Process:** GrowthX drafts content → Strapi polishes internally → Heavy promotion.
  - **Future State:** This will be automated via an "agentic layer" in the Atlas platform, which is still under development.

### Administrative

  - **Hotjar Access:** Victor will grant access to `team@growthxlabs.com` so the entire GrowthX team can use the tool.
  - **Strapi Contact Change:** GoalsR is no longer with Strapi. Victor is the new point of contact for all related topics.

---

## Action Items

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Publish comparator pages after light review

**Victor Coisne (Strapi)**
- Raise issue w/ Notum re: FAQs stuck open; then align w/ Vivek on FAQ-above-Related
- Add Hotjar access for team@growthxlabs.com

**Vivek Shankar (GrowthX)**
- Resend comparison page video list to Theo; then Theo adds Strapi V5 default
- Prepare Jan monthly report w/ deeper article performance analysis
- Create Airtable 'Current Topics' interface; share link w/ Theo/Victor

---

## Transcript
**Theodore Kelechukwu Onyejiaku:** Teaching the MCP in general, he wants to be known as the guy teaching MCP.

**Theodore Kelechukwu Onyejiaku:** So, yeah, it was a great session.

**Theodore Kelechukwu Onyejiaku:** This meeting is being recorded.

**Victor Coisne:** That's great.

**Victor Coisne:** Did you see that Anthropic donated MCP to a new foundation?

**Theodore Kelechukwu Onyejiaku:** Yeah, the one I saw was OpenAI, Anthropic, and I think they joined to create a new foundation.

**Victor Coisne:** Yeah, posted a message yesterday in, like, the LearnAI channel.

**Victor Coisne:** It's called the AgenticAI Foundation.

**Theodore Kelechukwu Onyejiaku:** Yeah, and it's MCP, Goose, and Agents.md.

**Theodore Kelechukwu Onyejiaku:** Oh, let me do that.

**Theodore Kelechukwu Onyejiaku:** It seems good.

**Theodore Kelechukwu Onyejiaku:** They are not...

**Theodore Kelechukwu Onyejiaku:** Should I ping them?

**Victor Coisne:** Let me check...

**Victor Coisne:** Let's see if they posted a message or something.

**Victor Coisne:** It says they will be five minutes late.

**Theodore Kelechukwu Onyejiaku:** Oh, okay.

**Victor Coisne:** How are you doing with the review of the pages?

**Victor Coisne:** Because I think that's what I'm seeing from the agenda.

**Victor Coisne:** It looks like 28 pages under a strapi review.

**Theodore Kelechukwu Onyejiaku:** Do you need some help with that?

**Theodore Kelechukwu Onyejiaku:** Yeah, I was going to chat with Norton to understand why the comparator pages, they've not been able to fix the preview because I remember that was where I was stuck.

**Theodore Kelechukwu Onyejiaku:** I wasn't able to preview the comparator pages, and I don't think it's a good idea to publish them right away.

**Theodore Kelechukwu Onyejiaku:** And for the integration pages, I noticed there are new ones, so I'll have to review and publish them.

**Theodore Kelechukwu Onyejiaku:** And for the blog posts, they are actually the ones I left for fix.

**Theodore Kelechukwu Onyejiaku:** So I guess they must have fixed it.

**Theodore Kelechukwu Onyejiaku:** So I'll check them out again by the end of tomorrow.

**Victor Coisne:** And have them published.

**Victor Coisne:** Got it.

**Victor Coisne:** Okay.

**Victor Coisne:** Well, in that case, let's, I mean, for the comparator pages, I wouldn't worry too much with the preview because I think like the, those pages get like little traffic.

**Victor Coisne:** So honestly, I don't, I don't think we need to worry too much about the review.

**Victor Coisne:** And they're going to remove the table as well, right?

**Victor Coisne:** Like they're in the process of removing the big table.

**Victor Coisne:** So I think it would be good to have the, as we remove the table, we should have like more pages that have like the actual text from, from GrowthX.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** So all you're saying is I should go ahead and publish them, right?

**Victor Coisne:** Yeah.

**Victor Coisne:** I wouldn't worry too much about that.

**Victor Coisne:** Like, cause again, like the traffic is so little that I don't think like the, I think you can do a light review, making sure like it, you know, nothing is like crazy, but I wouldn't spend too much time on it.

**Theodore Kelechukwu Onyejiaku:** Oh, okay.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** And then I was looking at the, um, the fact that David.

**Theodore Kelechukwu Onyejiaku:** It's shared, and I don't seem to understand what it's actually like, if it's the Notum that has to fix it, because I checked the ones that were working and the ones that were not working, and I didn't see any difference.

**Theodore Kelechukwu Onyejiaku:** Or what did you notice?

**Victor Coisne:** I shared the feedback from David.

**Victor Coisne:** I think the main issue with the FAQ is the fact that they are stuck open, so it doesn't look good.

**Victor Coisne:** That's the main issue.

**Victor Coisne:** And I think his other feedback was that they are not always consistent in terms of where they are.

**Victor Coisne:** In some cases, they are below the related article, and in some cases, they are above the related article section.

**Victor Coisne:** So I think it's just being consistent and always having the FAQ.

**Victor Coisne:** you.

**Victor Coisne:** think we wanted it to be above, I think, above the related article, right?

**Vivek Shankar:** Yeah, guys, how are you?

**Victor Coisne:** Hi, good.

**Vivek Shankar:** Sorry I'm late.

**Vivek Shankar:** One of my meetings has run over.

**Vivek Shankar:** It's just cascading everything.

**Vivek Shankar:** Yeah, I heard this is about the FAQs.

**Vivek Shankar:** I had a quick question about that.

**Vivek Shankar:** Is that something to fix on the front end, or is it something that needs to be fixed in the CMS?

**Victor Coisne:** I wasn't quite sure in terms of how those elements are placed.

**Victor Coisne:** Well, it's a bit odd, because in the CMS, there is a toggle that says, like, open by default, the FAQ, and they're all set to false.

**Victor Coisne:** So, like, it should mean, like, they should all be collapsed.

**Victor Coisne:** Yeah.

**Victor Coisne:** But in some cases, we see them open.

**Victor Coisne:** So I wonder if it's a bug.

**Victor Coisne:** And, yeah, so it's...

**Victor Coisne:** Probably something that we should flag for our web agency.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Yeah, do let me know if there's anything we can do in terms of the CMS, because I know that we kind of double-checked which way the positions were, whether the elements were right, etc.

**Vivek Shankar:** So it was a bit surprising to see that.

**Victor Coisne:** I think that on the topic of FAQ while we're on this one, I think there's really two things.

**Victor Coisne:** The first one is making sure all the FAQs are collapsed so it doesn't look odd.

**Victor Coisne:** So that's the first one.

**Victor Coisne:** As I just said, I think I'll raise an issue with Notum.

**Victor Coisne:** For the second one, it's the fact that the positioning on the page is not always consistent.

**Victor Coisne:** And I think that's a GrowthX issue.

**Victor Coisne:** I think, personally, that we should have the FAQ above the related articles.

**Victor Coisne:** Because I think related articles is more like for SEO, for cross-linking.

**Victor Coisne:** FAQ, it's kind of like nice.

**Victor Coisne:** Yeah.

**Victor Coisne:** To have it in the flow of like, okay, I'm reading the page.

**Victor Coisne:** So that's my opinion.

**Victor Coisne:** But I think it doesn't matter that much.

**Victor Coisne:** It just needs to be consistent across all the pages, right?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Yeah, it makes sense.

**Vivek Shankar:** Yeah, just, yeah, just, I guess you're doing a review internally.

**Vivek Shankar:** then just let us know, like, in terms of where you'd like to move it.

**Vivek Shankar:** And we'll get it done.

**Vivek Shankar:** We're almost done with the FAQs for the integration page.

**Vivek Shankar:** I think we're doing a final review.

**Vivek Shankar:** So that should be done as well.

**Vivek Shankar:** Let me share my screen real quick.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Cool.

**Vivek Shankar:** So, yeah, just running through the updates.

**Vivek Shankar:** We delivered nine articles last week and seven scheduled for this week.

**Vivek Shankar:** Just quickly running through the issues.

**Vivek Shankar:** Yeah, there we go.

**Vivek Shankar:** So, yeah, the comparison page, I think this was in progress as of last week.

**Vivek Shankar:** I think Notum was kind of doing this.

**Vivek Shankar:** Yeah, I just want to check if there's any updates there or...

**Victor Coisne:** Yeah, the process of shipping, that is just like, there was, I don't know if you followed, but there was an issue in the Node.js community, like with NPM, like vulnerability.

**Victor Coisne:** So we had to do a security audit first.

**Victor Coisne:** Long story short, it is going to ship this week.

**Vivek Shankar:** Cool.

**Vivek Shankar:** And then Theo, there was this one which was adding the videos to the comparison pages.

**Vivek Shankar:** We sent you that list.

**Vivek Shankar:** I don't know if...

**Vivek Shankar:** Do you want me to send you that list again or...

**Theodore Kelechukwu Onyejiaku:** Yeah, you could, you could.

**Theodore Kelechukwu Onyejiaku:** But if, like I discussed with Victor, I would definitely check them out.

**Theodore Kelechukwu Onyejiaku:** One thing that has been a blocker was the preview.

**Theodore Kelechukwu Onyejiaku:** So...

**Theodore Kelechukwu Onyejiaku:** I won't waste much time on that, so I'll just make sure things are okay and then publish them.

**Theodore Kelechukwu Onyejiaku:** Then for the videos, are you like, what videos in particular are you referring to?

**Vivek Shankar:** So some of these pages, they had either old videos or no videos.

**Vivek Shankar:** It was inconsistent.

**Vivek Shankar:** So the idea that we discussed was we would add a strapi V5 video to these pages, and then basically we just needed that video to get added.

**Vivek Shankar:** That was pretty much it, and I think that was something strapi wanted to handle internally, because in some cases, in some of the comparison pages, you had a webinar or something like that, so it was more a question of which video needs to go away.

**Victor Coisne:** So it's the new video from Paul, the Getting Started with Strapi V5.

**Victor Coisne:** That's the one we should include in most of the comparator pages.

**Theodore Kelechukwu Onyejiaku:** Okay, okay.

**Vivek Shankar:** Cool.

**Victor Coisne:** Cool.

**Victor Coisne:** Right, Andrew.

**Victor Coisne:** If we have a better video, like for instance, like WordPress, we have a better video that speaks to that use case specifically.

**Victor Coisne:** So if we have something better, let's use like that better video.

**Victor Coisne:** But as a default, let's just use the getting started.

**Vivek Shankar:** I think WordPress already has a migration webinar, which is a good fit.

**Vivek Shankar:** I think that's already a pretty good fit.

**Vivek Shankar:** In terms of the integrations pages, as I said, the integration page FAQs are under final review.

**Vivek Shankar:** And yeah, we should have that out by either Friday or early next week.

**Victor Coisne:** On this one, let's just make sure like, as part of your review, if you can check that it's above the related article across all the pages, that would be great.

**Victor Coisne:** Because I think let's just, this is the right place to put it.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** I'll just, uh...

**Vivek Shankar:** All right, noted there.

**Vivek Shankar:** Cool.

**Vivek Shankar:** So, then, just one more thing, Victor, just want to flag the hotjar, thank you for the access, but could you give it to this email instead, team at growthxlabs.com, because then, you know, the whole team can access it.

**Victor Coisne:** Yeah, let me do that right away.

**Vivek Shankar:** Send it in the chat.

**Vivek Shankar:** Where's the chat?

**Victor Coisne:** You can keep going, but I'll add the access to that email.

**Vivek Shankar:** All right.

**Vivek Shankar:** Can you still see my screen?

**Vivek Shankar:** Or is it...

**Theodore Kelechukwu Onyejiaku:** Yeah, I can see your screen.

**Vivek Shankar:** Okay, cool.

**Vivek Shankar:** Just wanted to check.

**Vivek Shankar:** Okay, so quick performance update. Nothing too major — this is just a weekly check.

**Vivek Shankar:** December is off to a good start.

**Vivek Shankar:** The "BUN versus Node.js" page saw a huge leap — almost 230% compared to Thanksgiving week.

**Vivek Shankar:** Generally, the top pages were much the same as usual.

**Vivek Shankar:** Conversion events increased week-on-week — a nice start to December.

**Vivek Shankar:** The click on pricing link was the one that, you know, quantitatively jumped up the most.

**Vivek Shankar:** Percentage-wise, click on contact sales link.

**Vivek Shankar:** And then across all cohorts, performance was pretty strong.

**Vivek Shankar:** LLM referral traffic was low — this is across the entire website.

**Vivek Shankar:** As you can see, November fell off a bit because of the Thanksgiving week gap, and the first week of December we hit about 1K, which isn't great if you spread it across four weeks.

**Vivek Shankar:** Overall, LLM referral traffic aside, we're off to a pretty good start.

**Vivek Shankar:** We're expecting December to slow down with about two weeks of holiday season toward the end, but it's still a good start.

**Vivek Shankar:** In terms of SEMrush data, no major changes.

**Vivek Shankar:** Strapi is still ahead of competitors that we're tracking.

**Vivek Shankar:** Some of those — there was a spreadsheet where we highlighted things competitors rank for but Strapi doesn't.

**Vivek Shankar:** We actually found a way to work some of those into the FAQs across all our pages.

**Vivek Shankar:** And then coming up next, we'll start working on proposed topics for new integration pages and Q1 content to target the agency owner persona.

**Vivek Shankar:** And yeah, we will have that for your review either middle or end of next week.

**Vivek Shankar:** So yeah, that's pretty much the update.

**Victor Coisne:** Okay.

**Victor Coisne:** So a couple of comments.

**Victor Coisne:** Like the first one, like the reason why there was a big increase on the BUN versus Node.js performance is because BUN was acquired by Anthropik.

**Victor Coisne:** That's why I think it was very, it's very much like in the news cycle.

**Victor Coisne:** So that's great.

**Victor Coisne:** But just to explain the growth.

**Victor Coisne:** For the events — these are all-inclusive, right? Not just GrowthX sessions.

**Victor Coisne:** This doesn't tell us much about GrowthX's performance — it tells us overall Strapi performance.

**Victor Coisne:** I'm wondering if it would make sense to do a cohort analysis specifically on GrowthX traffic.

**Vivek Shankar:** Yeah, GA4 actually doesn't let us do that.

**Vivek Shankar:** So GA4 basically has, like, last touch attribution.

**Vivek Shankar:** That's it.

**Vivek Shankar:** So we can list the pages where, you know, these events occurred, but it's not going to show, like, what the funnel was, essentially.

**Vivek Shankar:** We, there is a way to build that report, but it's exceedingly complex.

**Vivek Shankar:** And since we're already tracking in HubSpot in terms of the context created, the effort might just be a little duplicative.

**Vivek Shankar:** So that's the, that's the limitation, unfortunately.

**Vivek Shankar:** That's why we can't cohort it to just GrowthX pages and GrowthX contribution.

**Victor Coisne:** Okay, so let's focus on HubSpot reporting. This data is correlated but not entirely tied to GrowthX's impact.

**Victor Coisne:** I think we'll get better insights from HubSpot data than from GA events.

**Vivek Shankar:** Yeah, for sure.

**Vivek Shankar:** GA events give us week-on-week context, but for monthly reporting we'll look at HubSpot.

**Vivek Shankar:** So definitely on board with that.

**Victor Coisne:** Okay.

**Victor Coisne:** We were talking with the CEO about bandwidth for reviewing all the GrowthX content.

**Victor Coisne:** Just to summarize — comparison pages won't get a deep review since they get low traffic. We're shipping those.

**Victor Coisne:** Integration pages are where we're seeing success, especially with our strategy to reach out to partners for backlinks.

**Victor Coisne:** We're going to double down on that in 2026.

**Victor Coisne:** For articles, I'd love to understand which ones are really performing and how we adjust strategy based on that. The top-five list in the report is just weekly data. For monthly reporting, we should audit which article types perform well and adjust strategy accordingly.

**Victor Coisne:** So yeah, that's my...

**Vivek Shankar:** In terms of our pipeline, we've been prioritizing comparison pages, recently launched a batch of new integration pages, and we're also doing refreshes.

**Vivek Shankar:** Refreshes are pages that lost traffic or important keywords based on SEMrush data, but really 95% of refreshes are pages that lost offline traffic.

**Vivek Shankar:** We balance these together.

**Vivek Shankar:** New topics are a mix of competitor gaps.

**Vivek Shankar:** Paul and Theo suggested topics about a month ago — a mix of current topics and competitor gaps.

**Vivek Shankar:** The ones that we have added are a mix of the Reddit monitoring as well as general topics that we've been seeing floating around.

**Vivek Shankar:** We map those back to SEO terms. That's why I asked about Q1 priorities last week — to get the mapping right.

**Vivek Shankar:** But yeah, I mean, totally agree on doubling down on integration pages and going ahead with that.

**Vivek Shankar:** My guess is for the content itself, in terms of the cohorts that have been doing well, we have been internally sort of cohorting them, despite the fact that we're tagging everything as ecosystem in the CMS.

**Vivek Shankar:** We're not seeing major opportunities.

**Vivek Shankar:** Performance trends across all four of them, they tend to be doing quite well.

**Vivek Shankar:** And really, it's the refreshes that are giving us insights into how to boost traffic.

**Vivek Shankar:** Because, you know, we publish something, we kind of see the performance, and then a few months later, we kind of understand, like, okay, this is how we need to refresh it.

**Vivek Shankar:** Either sections are missing or either we're targeting sort of not exactly targeting the right keywords, etc.

**Vivek Shankar:** And that's how we are optimizing it for performance.

**Vivek Shankar:** So that's kind of the high level of it.

**Vivek Shankar:** And I think, you know, it's geared towards hitting strappy's goals.

**Vivek Shankar:** So, yeah, totally open to any feedback on that.

**Vivek Shankar:** Or if you think you need a little more visibility into it, I can certainly put something together.

**Victor Coisne:** Yeah, I think, like, diving a bit deeper during the next, in the monthly reporting, I think would be super good.

**Victor Coisne:** I love the Reddit monthly and the mapping work. I think it's worth having a deeper dive session in January, thinking long-term beyond just monthly data. The new year is an opportunity to identify bigger topic clusters we want to address.

**Vivek Shankar:** Since we're doubling down on the developer persona and exploring the agency owner persona, we'll do that naturally when we start the year.

**Vivek Shankar:** In January, when we recap the year's performance, we can look ahead and put that together for you.

**Victor Coisne:** Cool.

**Victor Coisne:** Sorry, go ahead, Theo.

**Theodore Kelechukwu Onyejiaku:** Is there a workflow that automatically detects current trends, like the Bun vs. Node story, and quickly generates a draft we can review and enhance?

**Vivek Shankar:** There's nothing connecting our Looker or GA4 data to Atlas yet.

**Vivek Shankar:** It's manual. If a news item suddenly explodes and we want to respond quickly, there's lag.

**Vivek Shankar:** This is part of the analytics project — we're building Atlas to centralize workflows, content, and performance data. It will replace Airtable. On top of that, there's an agentic layer that will surface these kinds of events or trends automatically.

**Vivek Shankar:** The analytics piece is still in progress — coming but not ready yet. For now, it's manual: someone flags a trend, we generate content, and send it to you for review.

**Theodore Kelechukwu Onyejiaku:** That would have been great for the React security vulnerability — we could have published quickly. Could you create a section where we can flag current topics and you prioritize them?

**Vivek Shankar:** I can create an Airtable interface where you can enter events and links, and we'll automatically prioritize them for the following week.

**Victor Coisne:** I see three buckets of content: "jump the wave" (riding news cycles), keyword-driven (what GrowthX does), and deep technical (Paul and Theo's tutorials with influencers). We need to cover all three. We should quickly draft trending topics through GrowthX, polish internally, then promote heavily.

**Victor Coisne:** Speed to market is critical, especially as we add AI topics to the mix.

**Vivek Shankar:** That's a use case we've proposed from delivery to engineering, and they're working on it. It needs the analytics build-out, but it's definitely on the roadmap.

**Victor Coisne:** Cool.

**Victor Coisne:** Awesome.

**Vivek Shankar:** All right.

**Vivek Shankar:** Thanks, everyone.

**Victor Coisne:** Yeah, one last quick thing.

**Victor Coisne:** Did you see Theo's feedback on the image?

**Vivek Shankar:** I did. The AI rendered an A as an O due to text squishing. We deleted that image — it's a Nano limitation. We're generating alternates to reduce error frequency.

**Victor Coisne:** Got it.

**Vivek Shankar:** Have a good week, everyone. We'll follow up in Slack.

**Victor Coisne:** One last thing — GoalsR is no longer with Strapi. If you had topics to discuss with her, let me know instead.

**Vivek Shankar:** Sure, no problem. Take care.
