# Relay <> Growth X - Weekly Sync

<metadata>
date: 2025-11-20
time: 16:02 UTC
duration: 24 minutes
organizer: bailey@growthx.ai
participants: Bailey Seybolt, Relay Marketing Team Contact
fathom_recording_id: 103165124
fathom_url: https://fathom.video/calls/482510552
share_url: https://fathom.video/share/e3Ay43Xgv3sAkvEojSjj1GqnUNpcVw4b
source: fathom
enriched_on: 2026-03-02 12:30 UTC
speaker_note: "Relay Marketing Team" represents the Relay-side contact(s) participating in the call; the specific individual is not consistently identified on the recording.
</metadata>

---

## Summary

GrowthX and Relay aligned on three major initiatives to improve content production workflow and LLM visibility. On process, they pivoted from a broken multi-team staging workflow to a simpler model where Relay approves content in Google Docs and GrowthX owns staging in Contentful, with a proposal to automate the staging step entirely. On content strategy, the team agreed to add FAQ sections to all new articles (a tactic showing consistent lift in LLM traffic) and Relay will investigate adding FAQ schema to blog templates. To maintain publishing velocity through the December holiday shutdown, Relay will front-load topic approvals now, getting GrowthX one week ahead on production.

---

## Context

Relay is a GrowthX B2B content marketing client on an ongoing engagement. The relationship spans content production (GrowthX writes articles, Relay approves and publishes), reporting (traffic, LLM visibility, SEO performance), and platform integration (Contentful CMS, Airtable project management, Google Search Console tracking). Bailey Seybolt (GrowthX Services Lead) runs weekly syncs with the Relay team to coordinate editorial workflow, address blockers, and review performance metrics. This meeting follows recent friction in the content staging process—a manual handoff between teams created errors and tracking lags—prompting a conversation about process consolidation and eventual automation.

---

## Relevance

**To GrowthX Delivery:**
- New workflow model (Relay approves in Docs, GrowthX stages in Contentful) reduces handoff risk and consolidates control over staging and tracking. This aligns with the broader services playbook of streamlining client workflows.
- Contentful automation is feasible and has precedent (other clients use it), but requires IT approval due to access restrictions. Bailey will investigate with engineering to determine what's possible with current permissions.
- Topic vetting is now a documented pipeline step: GrowthX will filter proposed topics against published content and keywords to prevent cannibalization as volume grows.
- FAQ automation (adding 3-5 FAQs to end of every article) is now a standard output; requires coordination with Relay on Contentful schema implementation.

**To CheckThat / AEO:**
- FAQ schema is a proven LLM visibility tactic: Relay will add FAQ schema to blog templates (low lift, high impact). This is a live test case of FAQ + schema impact on LLM traffic attribution.
- Brand citation tracking is trending positive (Relay mentions LLMs citing their website more frequently), validating the FAQ + schema strategy. Jacob will send deeper LLM metrics next week.
- GSC "not set" traffic spike (likely from podcast) indicates attribution gaps; Relay investigating. This aligns with ongoing work to improve LLM visibility measurement.

**To GrowthX Business Development:**
- Account is healthy and expanding: Relay is approving more topics, planning ahead for holiday production, and investing in LLM visibility—all signals of engagement and confidence.
- No renewal risk signals. The team is problem-solving together on process and strategy, not pushing back on scope.

---

## Overview

- **Staging Process:** To fix manual errors, Relay will now approve content in Google Docs, and GrowthX will own all staging in Contentful. GrowthX is also exploring automated staging.
- **Content Strategy:** To boost LLM visibility, GrowthX will add 3–5 FAQs to all articles. Relay will investigate adding FAQ schema to blog templates, a low-effort, high-impact tactic.
- **Holiday Buffer:** To maintain publishing velocity during December shutdowns, Relay will approve more topics now, allowing GrowthX to get one week ahead on content production.
- **Performance:** Positive signals continue (impressions, avg. position, brand citations). Relay will investigate a GSC "not set" traffic spike to improve attribution.

---

## Key Topics

### Staging & Publishing Workflow

  - **Problem:** The current manual workflow is error-prone and lacks a single source of truth.
      - **Staging:** Content was staged in the wrong Contentful instance.
      - **Handoff:** A manual handoff to a separate publishing ops team creates delays and errors.
      - **Tracking:** Airtable, the source of truth, is updated manually, causing lag between publishing and status updates.
  - **Solution 1: New Manual Process**
      - **Approval:** Relay approves content by commenting in the Google Doc.
      - **Staging:** GrowthX owns updating Airtable and staging in Contentful.
      - **Publishing:** Relay notifies GrowthX via Slack when a batch is live → GrowthX updates Airtable immediately.
  - **Solution 2: Automated Staging (Proposed)**
      - **Concept:** A pipeline step to auto-draft content in Contentful, giving editorial direct control.
      - **Constraint:** Requires IT approval due to strict access policies. GrowthX will investigate feasibility.

### Content Strategy & Quality

  - **Problem:** High content volume risks topic duplication and keyword cannibalization.
  - **Solution:** GrowthX will add a vetting step to its pipeline to check proposed topics against published content and keywords.
  - **New Tactic: FAQs for LLM Visibility**
      - **Rationale:** Adding FAQs to articles has shown a consistent lift in LLM traffic without harming human readability.
      - **Action (GrowthX):** Add 3–5 FAQs to the end of all new articles.
      - **Action (Relay):** Investigate adding FAQ schema to blog templates, a low-effort, high-impact technical change.

### Holiday Production & Reporting

  - **Goal:** Maintain publishing velocity during the December holiday shutdown.
  - **Plan:** Relay will approve more topics now → GrowthX will get one week ahead on content production.
  - **Reporting Snapshot:**
      - **Positive Signals:** Impressions, average position, and brand citations are all rising.
      - **Anomaly:** A large traffic spike to a "not set" landing page in GSC, likely from the podcast. Relay will investigate the GSC configuration to enable proper attribution.

---

## Action Items

**Bailey Seybolt (GrowthX)**
- Schedule 2026 goals scoping with Relay Marketing; include Relay team
- Consult engineering re: Contentful staging automation; assess access; report back to Relay
- Research Airtable/Looker auto-publish-link automation; share findings with Relay
- Build 3–5 FAQ auto-add into pipeline; coordinate with Relay on Contentful FAQ schema
- Send async update to Relay next week
- Confirm wrong-instance staging moved; update Relay in Slack

**Relay Marketing Team**
- Approve more topics in Airtable for next week buffer + December holidays
- Investigate 'not set' traffic spike in GSC; improve attribution

---

## Transcript
**Bailey Seybolt:** It's just me on our...

**Bailey Seybolt:** I think she is not, because already touched base with her, because we wanted to talk more about the 2026 goals, and I think she's not going to make it today.

**Bailey Seybolt:** So we're going to find a different time.

**Bailey Seybolt:** Actually, that's a good question.

**Bailey Seybolt:** And do you, should you and you be at that meeting, too?

**Bailey Seybolt:** I was trying to find a time that worked for all of the, everyone.

**Bailey Seybolt:** So it's good to know how many people to triangulate between.

**Relay Marketing Team:** If you can, if you can manage to get me in there, I think that I'm happy to join.

**Relay Marketing Team:** I don't think you need to worry about trying to find time with Katie for that one, if it is difficult.

**Relay Marketing Team:** But yeah, feel free to add me and we'll figure it out on our end.

**Bailey Seybolt:** Okay, perfect.

**Bailey Seybolt:** I'm figuring out the best people to bring from our end so we can sort of get all the information that we need to like fully scope it.

**Bailey Seybolt:** And then I will find time with you all.

**Bailey Seybolt:** Probably it may not be next week because we have Thanksgiving next week.

**Bailey Seybolt:** So it's going to be a pretty short week, but we will find a time soon.

**Relay Marketing Team:** Cool.

**Relay Marketing Team:** Sounds good.

**Bailey Seybolt:** All right, I will share our agenda.

**Bailey Seybolt:** So in terms of content updates, things are moving along.

**Bailey Seybolt:** In terms of this, oh yeah, the staged post.

**Bailey Seybolt:** So what I was, I realized this has just been like a little bit of a circus trying to keep track of.

**Bailey Seybolt:** And I think some of it's on our end and I'm trying to diagnose, I think, where the breakdown exactly is happening.

**Relay Marketing Team:** And I think, I mean, some of it would just be the staging in the wrong instance was just a mistake on our part.

**Relay Marketing Team:** Yeah, and then that's totally like understandable because it's been a confusing thing even for us, which one to build in.

**Relay Marketing Team:** And I think it sometimes just switches between the two randomly.

**Relay Marketing Team:** So all good there.

**Bailey Seybolt:** And I think for us too, you know, I think because publishing like ops is separate, it feels like it's just another person to touch it and another opportunity for something manual to break down.

**Relay Marketing Team:** Yeah, I hear you.

**Bailey Seybolt:** So one thing we've done with some clients, which I think could work here, is build an automated publishing step into the pipeline itself that creates the content and connects directly to your CMS.

**Bailey Seybolt:** Editorial can just press a button and it drafts it in Contentful. That means editorial has more control and visibility into exactly when things get staged. I think that would work really well here.

**Bailey Seybolt:** And I think we've done it with Contentful before.

**Bailey Seybolt:** I know like your IT team is like very conscious of what kind of access people have and how much they need.

**Bailey Seybolt:** So I was thinking I would then talk to our engineering team and see if that is something that's easy to do with the level of access we have now, or if that's something that we would have to get like more additional access, which obviously may not then be possible.

**Bailey Seybolt:** But it is something that worked really well to streamline the process in other cases, I think.

**Relay Marketing Team:** And so walking through how that would work, it's just, it's literally just like an automated process where when something is ready to go, we hit a button and it kind of.

**Bailey Seybolt:** Exactly. We then just hit a button and it goes into your Contentful instead of having someone come and manually do it.

**Relay Marketing Team:** Right.

**Bailey Seybolt:** Because right now how it works is we sort of take the editorial that's ready, we hand it off to the publishing ops team, and then they get it set up and Contentful and kind of, like, update the Airtable, let us know when it's ready.

**Bailey Seybolt:** But like all manual processes, there's always a sense that it might, you know, if someone forgets to update the Airtable, then you have inaccurate information. And I think especially in this case, because you're using Airtable as a source of truth for what you're trying to show to your partner and understanding where things are in the pipeline.

**Bailey Seybolt:** It feels like this would give us the ability to just kind of, like, take a manual step away entirely that's owned by a different team so that, like, our team can be responsible for knowing exactly where everything is in the process.

**Relay Marketing Team:** Yeah, that makes sense to me if we're able to swing it just with the limitations, you know, that our IT.

**Relay Marketing Team:** Exactly.

**Bailey Seybolt:** In the end, like, it wouldn't change anything for you except that we would sort of know exactly where everything is and there would be just, like, one less person touching it.

**Relay Marketing Team:** And then what about just getting things flagged as being published?

**Relay Marketing Team:** Because that's another thing that's just kind of a little bit cumbersome for me is that, you know, it wouldn't be an issue if it wasn't for this kind of in-between interim step that we have to deal with with our compliance partner to get everything through.

**Relay Marketing Team:** And it's just, you know, it's important for me to be able to have, like, real clear...

**Relay Marketing Team:** ...

**Relay Marketing Team:** ...

**Relay Marketing Team:** Overview of exactly what stage everything is at.

**Relay Marketing Team:** So is there like another way to build in like a link back that shows like if I publish on something like that's going to get updated in the Airtable as well?

**Relay Marketing Team:** Or like what's the I guess what's the best process for you?

**Relay Marketing Team:** I've been tagging stuff in there, but I don't know if that's the best way.

**Relay Marketing Team:** Like what's a good?

**Bailey Seybolt:** Yeah, I think.

**Bailey Seybolt:** Do you tend to publish in batches when things get approved or?

**Relay Marketing Team:** I would.

**Relay Marketing Team:** Yeah, but it's like it's kind of inconsistent.

**Relay Marketing Team:** Just in that you never quite know how it's going to line up in terms of like what's ready on your end, what's ready with the compliance partner, what's ready with our like other designs.

**Relay Marketing Team:** So sometimes I'm just kind of publishing as as we can.

**Relay Marketing Team:** So it's not necessarily always in batches.

**Relay Marketing Team:** Yeah.

**Bailey Seybolt:** On our side, I think this isn't something we have a perfect answer for yet.

**Bailey Seybolt:** When things are going live, we were automatically pulling the links into our Looker, but it broke the Looker basically.

**Bailey Seybolt:** And we were unable to find a way to fix it. So we're going in and manually updating Looker on a weekly basis. And then because we're doing that, that's when the Airtable gets updated too.

**Bailey Seybolt:** So I'll ask around and see because that was a little bit ago and see if anyone, other teams managing this problem have found a better way to automate this.

**Bailey Seybolt:** I think realistically right now, even if you just dropped us a message in Slack and just said new articles this week, like we can go in and make sure that the Airtable is updated because we report it in a new way.

**Relay Marketing Team:** Yeah, I think one of the breakdowns for me, and maybe I'm sure it's just as frustrating for you, is that like in some cases I'm commenting on Google Docs.

**Relay Marketing Team:** In some cases I'm commenting in the Airtable. If we could just have a single source of truth where we can align on how to do that best, that would help. The whole compliance thing just adds another layer of complexity.

**Relay Marketing Team:** Because then another thing is like, I want to make sure things are getting staged as they're ready.

**Relay Marketing Team:** But at the same time, there is always a potential for them to come back and say, we need this change.

**Relay Marketing Team:** And that's something else that I need to be able to manage.

**Relay Marketing Team:** And I hate to kind of slow down the process of getting in stage without doing that.

**Relay Marketing Team:** Anyway, that's kind of a me problem.

**Relay Marketing Team:** But I'm just kind of, you know, there's a lot of moving parts that I'm just trying to focus as many of them as possible to make sure that everything runs smoothly.

**Bailey Seybolt:** I think for now, I definitely think like commenting, just commenting in the doc when something is ready to go makes the most sense.

**Bailey Seybolt:** Because that's where you are, right?

**Bailey Seybolt:** Like when you're signing off on the content, you're in the doc.

**Bailey Seybolt:** So just put a comment at the top and let us know it's ready to go.

**Bailey Seybolt:** And assume that we're going to then take care of like letting, you know, staging it, like updating it to ready to stage.

**Relay Marketing Team:** Like that's on us to update it.

**Bailey Seybolt:** Airtable at that point, because we're the ones who are owning getting it in Contentful, right?

**Bailey Seybolt:** And then I think in terms of publishing, making sure that it's updated in Airtable and stuff, I think if you just drop a Slack and sort of, I mean, we check on a weekly basis to check, like, if any of the articles that are staged have been published, it's on us to, like, check on a weekly basis to see what's gone live.

**Bailey Seybolt:** If, you know, you want to drop a message in Slack and just let us know you're publishing a batch, it's helpful in the sense that we can then go in, like, right then and make sure it's all updated so you don't have a lag.

**Bailey Seybolt:** Because right now, what we do is someone, like, usually towards the end of the week, will go in and update Looker with any, like, new published links.

**Bailey Seybolt:** They'll check to make sure that the Airtable is up to date.

**Bailey Seybolt:** But obviously, if you publish a bunch of stuff on a Monday and we're not going in there until Friday, there could be a lag.

**Bailey Seybolt:** So if you publish a batch and just let us know, then we would prioritize closing that gap.

**Relay Marketing Team:** Cool.

**Relay Marketing Team:** Okay.

**Relay Marketing Team:** Yeah, that works.

**Bailey Seybolt:** And then I think, and then I will, I'll look, I'll ask around to see how other teams are managing it and see if they found a better system for making that more automated, like along the lines of automating that publishing step.

**Bailey Seybolt:** And if I, if I find anything that feels like it might be useful, I'll, I can bring that back and see if it might work.

**Relay Marketing Team:** Okay.

**Relay Marketing Team:** Okay.

**Bailey Seybolt:** That's cool.

**Bailey Seybolt:** Yeah, I hear you. The manual aspect is confusing, especially if you don't know where you're supposed to be commenting or what you're supposed to do.

**Relay Marketing Team:** So while we're on the topic of the content, there is something else that I've been kind of noticing and I'm starting to worry about a little bit because there's such a volume.

**Relay Marketing Team:** I start to forget what I've already approved.

**Relay Marketing Team:** And then I kind of find myself, I'll see another piece of content that I've approved like a couple of weeks later.

**Relay Marketing Team:** And it's very similar to one that we've already kind of pushed through, pushed through the pipe.

**Relay Marketing Team:** I just wonder if you have any thoughts on that, whether that's even a risk when it's kind of taking a bit of a different angle or if there's kind of any kind of solution to make sure we're not repeating ourselves too much as the volume continues to grow and grow.

**Bailey Seybolt:** Yeah, I think as the volume continues to grow, we'll have to run more checks on our end, basically like feeding in the data on like what keywords we've already used, what topics we've already published to make sure we're kind of not cannibalizing that.

**Bailey Seybolt:** You don't want to create content for keywords that are all almost the same—that's just wasted effort. Sometimes you end up with similar content, but if it's taking a very different angle and targeting a different keyword, then it can still be worth publishing. When you're producing large volumes of content, you're going to have some overlap in themes, but as long as you're not cannibalizing keywords and going for exactly the same thing, it's okay. If you see something that feels like a duplicate, flag it. But it's also on our team to run those checks when presenting article topics to make sure we haven't already covered them.

**Relay Marketing Team:** Okay, cool.

**Relay Marketing Team:** Yeah, there's only been a couple of instances, but I've noticed in the new ideas coming through there are often some that are very similar, almost identical. I've had to stop myself a few times thinking, wait, I just approved this exact story with a different headline.

**Bailey Seybolt:** Yeah, we'll make sure we're building that into our list of proposed topics in Airtable. Those should be vetted and filtered to make sure we haven't already covered them. As a human, your brain stops being able to see the difference when there's a lot of volume—that's why we have LLMs to help filter out duplicates. We'll make sure we're doing that as the volume continues to grow.

**Relay Marketing Team:** Okay, that works.

**Bailey Seybolt:** So in terms of article topics, I saw we have enough for next week.

**Bailey Seybolt:** I'd love to get your eyes on a few more topics because we're going to prioritize new keywords and topics based on the documentation you shared. Given that next week is short, I'd like to make sure we have a buffer in case we don't have the bandwidth.

**Bailey Seybolt:** I'm hoping we can get it done early next week, but just in case, I'd like to make sure we keep moving on production and have more topics in our pocket.

**Relay Marketing Team:** Yeah, definitely. I can go in and approve a bunch more topics. I'm also thinking we should plan ahead for the December holidays. If we can front-load getting some assignments through, I want to make sure we maintain our publishing volume.

**Bailey Seybolt:** Our goal right now is to produce an extra week ahead. That way we can line up an extra week or two of content that's already been delivered to you so it can be scheduled for publishing when people have time off. This helps avoid delays in the approval process. We want to try and get at least one week ahead every week.

**Bailey Seybolt:** Yeah, we have the same situation. I think it would be great to try and get ahead so we're not losing velocity during the shutdown.

**Bailey Seybolt:** I think that's it for me on content updates. Do you have anything else?

**Bailey Seybolt:** I was curious if your team had any thoughts on the CTA modules.

**Relay Marketing Team:** Yeah, we already have CTA modules built in Contentful, but the way they're currently built doesn't have the ability to add a disclosure line. We flagged this to our dev team to see if they can add another field in Contentful so we can build out these CTA blocks. We're waiting to hear back on their capacity and whether that's possible.

**Bailey Seybolt:** Keep us updated on that.

**Bailey Seybolt:** I wanted to mention something we've been testing with clients on LLM visibility, which I know is a big focus for you. We've seen some lift from adding FAQs as a standard to the end of every post. Some clients have also tried TLDRs at the beginning, though those make for a weird reading experience. The results have been a bit inconsistent—one client saw a 6% lift one month but it went back to normal the next. But adding FAQs and schema are things we've seen consistently improve traffic. Adding FAQs doesn't negatively impact the human reading experience, so there's nothing to lose. We could build a step into our pipeline to add three to five FAQs to the end of every article, or just specific types if you want to test it first.

**Relay Marketing Team:** Yeah, I think we should definitely do that. I'm all for it. Are there any best practices on how to incorporate FAQs or formatting preferences? I've seen them sometimes as collapsible sections. I'm not sure if we should ask our dev team to build that functionality, or if it even matters as long as we just add the FAQs.

**Bailey Seybolt:** From a readability perspective, it doesn't really matter for LLM information—more readable content gets treated better by search engines. Having a table of contents so you can jump around does make a difference. Whether FAQs are collapsible, I haven't seen data either way, so I'd treat that as a human readability thing. Where you put the FAQ matters—putting it in the middle would be awkward. Put it at the end.

**Bailey Seybolt:** The other thing we've seen data on is adding schema to blog pages—FAQ schema specifically has shown lift. You could also add schema to your homepage and product pages, though that's not something we do on the content side. But it could be worth looking into. We've seen it work, and a lot of companies are testing it. They're finding that adding schema is another low-risk, high-potential thing—it can't hurt, and some people are seeing big spikes in LLM traffic just from that.

**Relay Marketing Team:** Yeah, definitely.

**Relay Marketing Team:** I'll take a look.

**Bailey Seybolt:** For the blog schema, if you add it to your templates, it's a one-time effort that applies across all blogs going forward. It's a fairly low lift. I'm not an expert on the technical side, but we have another client who just did it in Contentful and it automatically applied to all their blog templates.

**Bailey Seybolt:** Great. So I'll start getting that built into the pipeline going forward. One more thing—next week we'll be closed on Thursday for Thanksgiving. Are you okay with an async update, or could I try to spend time on Wednesday?

**Relay Marketing Team:** Yeah, async is fine for next week.

**Bailey Seybolt:** Great.

**Bailey Seybolt:** On the reporting side, Jakub will send a deep dive async to Bethany and you all to review, and then we can touch base live if you have questions. For the snapshot this week, impressions are continuing to climb, average positions are improving—all good signals. One thing I noticed is a big spike in traffic to your "not set" landing page that aligned with the podcast. I'm not exactly sure what's happening, but it might be a Google Search Console configuration issue. It's worth investigating to better attribute that traffic and understand what's going on.

**Bailey Seybolt:** On LLM signals, we're seeing more positive signals. Brand citations are rising—LLMs are actually citing your website and driving traffic to your content, which is what we like to see. Over the last month, we've also seen engagement numbers improve across all LLM platforms. Jakub will dive deeper into this next week, but nice to see these positive signals.

**Relay Marketing Team:** Great. I think we covered everything I had on my list.

**Relay Marketing Team:** Do you have any insight into when we'd be able to move those articles that were initially staged in the wrong instance?

**Bailey Seybolt:** I just sent a message to our publishing ops team on Slack to see if they can do that today. I'll drop a note in Slack once I hear back from them.

**Relay Marketing Team:** Yeah, that'll definitely unlock us to be able to publish a good chunk of content.

**Bailey Seybolt:** I flagged it as urgent, so I'm hoping they can do it today. I'll let you know once it's done and will follow up either way today.

**Relay Marketing Team:** Sounds good. Thanks, Bailey.

**Bailey Seybolt:** Thanks.
