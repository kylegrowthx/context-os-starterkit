# Pod weekly catch up

<metadata>
date: 2025-09-12
time: 14:01 UTC
duration: 24 minutes
organizer: Mara Leighton
participants: Mara Leighton, Vivek Shankar, Nika Narimanidze, Ismail Ajagbe, Usman Ghani
fathom_recording_id: 86878260
fathom_url: https://fathom.video/calls/408088742
share_url: https://fathom.video/share/so8xBZsWkJn5FVszKDwFs7qeEmJyZbPv
source: fathom
enriched_on: 2026-03-03 09:45 UTC
</metadata>

---

## Summary

GrowthX Rapid AI content team reviewed operational status before Vivek's two-week vacation, with focus on Airtable data quality, Strapi workflow improvements, and Galileo blog migration remediation. Mara will notify the client (Jackson) about extended timeline for the Galileo work while delegating 35 remaining blog fixes to Suleiman and a freelancer via Linear. Team confirmed contingency plans for Looker stability, discussed Rapid's content strategy staying general-audience focused, and confirmed next steps for comparison page updates with new CTA images.

---

## Context

This is a weekly synchronization for the Rapid AI content team at GrowthX. Vivek Shankar is the team lead departing for a two-week vacation to Peru, so the team is aligning on operational handoff points. The broader context involves GrowthX's ongoing content delivery engagements for multiple clients (Rapid AI, Galileo, Strapi-related work), with current bottlenecks around blog migrations, content workflow orchestration, and client communication around timelines. Rapid AI is a fintech/payment operations client with a focus on general payment ops audience, while Galileo is a product platform where blog content migrated from Sanity to Framer, creating broken links and missing content that requires tedious manual remediation.

---

## Relevance

**To GrowthX Delivery:**
- Airtable data hygiene is critical for reporting accuracy — teams must update statuses immediately to avoid cascading downstream issues
- Strapi workflow now requires real-time status movement (move articles to "Add" stage as soon as marked "good to go") to prevent reporting artifacts of stalled work
- Galileo Sanity-to-Framer migration is highly tedious (10-15 minutes per article for 35 remaining pieces), requiring outsourced labor — Suleiman + freelancer assigned to handle Monday-Wednesday workload
- Looker contingency: new Looker dashboards are stable for most date ranges; if issues occur, reduce to one-week range or escalate to Suleiman; GSC screenshots acceptable as last resort

**To Rapid AI Business:**
- Current content strategy remains general payment ops audience; specific personas (merchants, high-risk industries) determined by article category only
- Rapid may provide new ICP personas post-SOW review; if received, GrowthX can map to clusters/assignments after Vivek returns; general audience framework applies in interim
- Pillar page refreshes launching next week; model pages dependent on client feedback, likely week after next
- Code inclusion in articles deferred pending SOW discussion

**To GrowthX Delivery Operations:**
- Jackson (client) must be notified this week that Galileo blog migration will take ~1 month vs. original estimate; need confirmation it's acceptable as bonus deliverable
- Comparison pages: six pages (three existing, three new) publishing this week without new CTA image; next week's articles and all existing pages to be updated with new Gurzhar-provided CTA image
- Victoria reviewing RAMP data wrapper structure for vendor integration; GrowthX can implement manually at smaller scale pending her spec

---

## Overview

- Airtable must be kept up-to-date to avoid reporting issues; statuses should be moved promptly
- Galileo blog migration fix will be delegated to Suleiman and his freelancer to complete \~35 remaining articles
- Rapid AI may provide new ICP personas; current content strategy remains focused on general audience
- Vivek provided updates on various projects (Strapi, Galileo, Rapid) and addressed team questions

---

## Key Topics

### Airtable and Strapi Updates

  - Emphasis on keeping Airtable updated for accurate reporting
  - Strapi articles should be moved to "Add" stage when ready
  - Engineering requests need consistent follow-ups

### Looker Stability and Contingency Plans

  - New Lookers are more stable; date range issues unlikely
  - If problems occur, reduce date range or consult Suleiman for fixes
  - GSC screenshots as a last resort for one week

### Galileo Blog Migration

  - 35 out of 70 blogs still need fixing after Sanity to Framer migration
  - Process is tedious, taking 10-15 minutes per article
  - Task to be delegated to Suleiman and his freelancer
  - Mara to inform Jackson about extended timeline

### Rapid AI Content Strategy

  - Current focus remains on general payment ops audience
  - Specific audiences (e.g., merchants, high-risk industries) determined by article content
  - Potential inclusion of more technical details (code) to be discussed after SOW review

### Upcoming Content Updates

  - Pillar page refreshes scheduled for next week
  - Model pages may start the following week, pending client feedback

---

## Action Items

**Mara Leighton (GrowthX)**
- Message Jackson (client) this week about Galileo blog migration timeline. Explain that the work will take approximately one month instead of the original timeline, and confirm if this is acceptable.

- Tag Suleiman (GrowthX) for Galileo blog migration work. Create Linear ticket for him and his freelancer to complete the remaining 35 articles. Suleiman has capacity Monday-Wednesday before publishing workload ramps Thursday-Friday.

**Nika Narimanidze (GrowthX Labs)**
- Run basic technical audit for Galileo. Include click depth, 404s, broken redirects, and flag JavaScript vs non-JavaScript homepage rendering differences if it can be done easily. This is lower priority if it conflicts with other sprint work (RAMP, etc.).

**Usman Ghani (GrowthX Labs)**
- Next week, update all comparison pages (both new and previously published) with the new CTA image from Gurzhar. This will apply to the six pages publishing this week (three existing, three new in queue) as well as older published comparison pages.

---

## Transcript
**Vivek Shankar:** Just wanted to catch up with everyone.

**Vivek Shankar:** If there's anything that, obviously, there are some things that are going to spill over the next week.

**Vivek Shankar:** Just generally, you know, please make sure that Airtable is up to date.

**Vivek Shankar:** Because if it's not, you know, it creates a lot of other problems in terms of reporting, cetera.

**Vivek Shankar:** So please just make sure fields are filled, statuses are moved.

**Vivek Shankar:** For Strapi this week, Usman, I moved some of the articles to add to stage based on, you know, which ones were good to go, et cetera.

**Vivek Shankar:** From next week, please just make sure you do that.

**Vivek Shankar:** So as soon as an article is marked, like, good to go or something, just push it into the next status so that it's not, it doesn't look like we're working on 10 things at the same time.

**Vivek Shankar:** So I've done that.

**Vivek Shankar:** Some of the other articles are remaining.

**Vivek Shankar:** I guess we can catch up about that.

**Vivek Shankar:** But please, for everyone, please remember to update your engineering requests and keep...

**Vivek Shankar:** Following up with them, repeatedly, and Usman, I know we have a couple for Strapi that we just need to follow up with them about, so please remember that.

**Vivek Shankar:** Other than that, I think that's pretty much it.

**Vivek Shankar:** There is the Galileo thing, which we can discuss shortly, but before that, just wanted to check, is there anything else you guys wanted to bring up, or any questions, et cetera?

**Nika Narimanidze:** Well, look, you will be out for two weeks, right?

**Nika Narimanidze:** And sometimes there are issues with Looker, so just like it was back then, when you returned, everything was messed up.

**Nika Narimanidze:** I've seen that you sent the Notion file of the Looker, and does it include some common things that get messed up in Looker, and how to fix it?

**Nika Narimanidze:** Not really.

**Vivek Shankar:** The new Lookers are pretty stable, I don't think.

**Vivek Shankar:** there's going to be any issues.

**Vivek Shankar:** The only issue will...

**Vivek Shankar:** So the reason the old looker was breaking was because the dates that we were choosing in there was, I think, it was too far a range, basically, to be old looker.

**Vivek Shankar:** So like there was a date range limit within which the data would be displayed.

**Vivek Shankar:** If it was more than that, the thing would just say like data source issue or whatever.

**Vivek Shankar:** In the new lookers, I don't think that's going to be an issue.

**Vivek Shankar:** If you do see that happening again, just reduce it to maybe one week or something like that.

**Vivek Shankar:** That should fix it.

**Vivek Shankar:** If even that breaks, you can ask Suleiman to take a look at it and fix it.

**Vivek Shankar:** If even he can't fix it, just go with, I guess, GSC screenshots.

**Vivek Shankar:** We can get away with it for one week.

**Vivek Shankar:** Suleiman, the publisher. He's been helping me build a Looker. So any issues, you can check with him.

**Nika Narimanidze:** Okay, good to know that. Thank you.

**Nika Narimanidze:** Cool.

**Nika Narimanidze:** Any other questions?

**Vivek Shankar:** Yes, not.

**Vivek Shankar:** All right.

**Vivek Shankar:** For the Galileo stuff, yeah, I think, Ismail, you have best insight into that.

**Vivek Shankar:** I don't know if anything can be outsourced, but, yeah, what do you think?

**Mara Leighton:** But, yeah, Ismail, would you mind giving us sort of like, or giving me, I should say, like a quick TLDR of the process for what we're doing? And it sounds like Isra just hasn't been responding, so I want to understand what her function was. And then, yeah, we can kind of back into it from there.

**Ismail Ajagbe:** Yeah, sure. The older Galileo blogs, most of them are broken.

**Ismail Ajagbe:** After the migration from Sanity to Framer, all our blogs got broken. The task is that we have to go into Sanity, open the old blog, look for the missing content, and then update it in Framer.

**Ismail Ajagbe:** So, the process for just an article takes about 10 or 15 minutes, and currently we have like 35 blocks to go through.

**Ismail Ajagbe:** So, the entire list was about 70, about, Yisra got that down to like 35.

**Ismail Ajagbe:** Okay.

**Ismail Ajagbe:** And we have about 35 pieces left.

**Mara Leighton:** And when we're going through and determining what's missing and updating it in Framer, what are the things that are typically missing? Like, is it something where if we just have an SOP, we could...

**Ismail Ajagbe:** We can't really come up with an SOP because in some articles, the entire content is missing, in some bullets are missing, in some the images are missing. It just takes going through the entire article, seeing what's missing, going to the old blog and bringing everything back.

**Mara Leighton:** Do you mind, by any chance? I know this is tedious, I'm sorry to put you on the spot. Would you mind sharing your screen and showing how the process works? I'm thinking, if there's a perfect prototype or a version that's correct, maybe I could step in and do a portion of it.

**Vivek Shankar:** I wouldn't volunteer yourself. The reason we gave it to Isra is it's really tedious work. Like, the images need to be moved over, et cetera. Since these aren't our blogs, I'm thinking we should bring this up to Jackson and just be like: "This is taking longer than expected because the blogs are pretty different — there's no standard process." I think we should tell him we'll take another month or so.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Yeah, that sounds good.

**Mara Leighton:** If that's like the timeline that we're comfortable with, that's what I'll share with them.

**Mara Leighton:** I also might just shoot the message over today and give them a sense.

**Mara Leighton:** Like this is kind of like a bonus thing.

**Mara Leighton:** So while I don't want us to retract it, I also think it's fine to say like, it's going to take us a little bit.

**Mara Leighton:** It's going to take us this long.

**Mara Leighton:** Does that work for you?

**Mara Leighton:** Otherwise, we need to split up the work a bit.

**Mara Leighton:** And then now you and I can kind of talk about what feels feasible for you.

**Mara Leighton:** I don't want it to become like.

**Mara Leighton:** So I'll check in with you, just like if we are going to split it, depending on what the timeline is, blah, blah, blah.

**Vivek Shankar:** regarding assigning the work, I think we can give it to Suleiman.

**Vivek Shankar:** I know Suleiman has like a freelancer assigned to him by Andy.

**Vivek Shankar:** So the publishing workload starts for him on Thursday and Friday.

**Vivek Shankar:** So Monday to Wednesday, he's pretty much, his workload is lowered.

**Vivek Shankar:** Great.

**Vivek Shankar:** So I think we can give it to him and just have it on a linear ticket and have him and the freelancer execute it.

**Vivek Shankar:** Yeah, that sounds perfect.

**Mara Leighton:** Let's try that.

**Mara Leighton:** So I'll still message Jackson and give him a sense that it might take a little bit longer.

**Mara Leighton:** And then in parallel, we'll tag in Suleiman.

**Vivek Shankar:** Yeah, that's the best way forward. Honestly, we don't have the capacity to do this because it's super tedious work. I want you to avoid doing the tedious stuff too if we have anyone else to tag in.

**Mara Leighton:** Okay, that was my question around delegation.

**Mara Leighton:** I was like, maybe we can tag him in.

**Mara Leighton:** So, okay, cool.

**Mara Leighton:** Let's do that.

**Vivek Shankar:** Crisis averted.

**Mara Leighton:** I'll let Jackson know just to give us a little bit of breathing room that it might take a little bit longer and see if that works for him.

**Mara Leighton:** But since it means that they don't have to do it, I'd imagine they'll be fine with it.

**Mara Leighton:** We'll see.

**Mara Leighton:** Cool.

**Mara Leighton:** All right.

**Mara Leighton:** Anything else?

**Mara Leighton:** Like, Vivek, either that's on your to-do list to run through or also, like, team, obviously, Vivek will be out for a couple weeks.

**Mara Leighton:** And he's given me great context on, like, you know, when you typically share articles, what's typically expected for those reviews.

**Mara Leighton:** But are there any questions or things that, like, you want to chat through while you have both of us here?

**Mara Leighton:** Otherwise, I know you have context. I can always message you, and we can clear things up if needed, but I just want to give you the opportunity if there's anything.

**Nika Narimanidze:** Not about processes.

**Nika Narimanidze:** I had a question about Galileo.

**Nika Narimanidze:** Vivek, do you remember the issue of no hallucination index that Galileo had on SERPs?

**Vivek Shankar:** I think that was being fixed.

**Vivek Shankar:** For the homepage, Galileo AI started showing up.

**Nika Narimanidze:** For like 95 pages, it will be fixed, but there will be some pages that would still keep the issue.

**Nika Narimanidze:** It just needs time just to accelerate this.

**Nika Narimanidze:** I've identified only one URL.

**Nika Narimanidze:** I've been going through this and monitoring and requesting re-indexing on Search Console.

**Nika Narimanidze:** So if I bump with same problem for other pages, we just have to request re-indexing, and that's it.

**Nika Narimanidze:** But the main issue is images — the logo icon. It's still not present, and that's basically a Framer issue, but there should be some fix. But why do people choose Framer?

**Mara Leighton:** I think the logo thing — he had responded in there, right?

**Vivek Shankar:** He basically left a link to the logo, and that's the best solution we have. With normal CMS platforms it's straightforward, but here it's complicated. Honestly, I wouldn't waste time on this. If they bring it up, we can say the logo is a Framer issue and leave it at that. Troubleshooting Framer isn't close to what we're actually doing here.

**Nika Narimanidze:** Okay, Vivek, should I prioritize the technical audit for next week?

**Vivek Shankar:** Just run it. There was one issue we saw where the JS version and non-JS version of their homepage is very different. That's a tough issue, but run a very basic technical audit with click depth, 404s, redirects, and broken redirects. If there's an easy way to flag the JS versus non-JS difference, let's do it. The technical audit was mainly because I was worried about performance dropping, but that's fine now. Run it and it's good to send, but if it's clashing with RAMP or other sprint team issues you're tagged on, then skip it.

**Vivek Shankar:** Okay.

**Nika Narimanidze:** And additional question, Vivek, about the RAMP and the publishing.

**Nika Narimanidze:** Like, Victoria will review the SEO patch.

**Nika Narimanidze:** And we have this flow set up, right, in the atlas for publishing.

**Nika Narimanidze:** And does it align with the non-internal data template?

**Vivek Shankar:** Oh, .

**Vivek Shankar:** Yeah, okay.

**Vivek Shankar:** That's why we decided to not publish.

**Vivek Shankar:** What I discussed with Victoria when you were out was she needs to figure out how the data wrappers will work because some of these vendors will not be present in their snowflake.

**Vivek Shankar:** So she needs to figure that out.

**Vivek Shankar:** Once she lets us know what the structure is, then maybe we go to Marcus and say, hey, listen, it's basically the same flow, except we don't have these steps present.

**Vivek Shankar:** So I think it shouldn't take him like four months this time, but, you know, we can still, we have Suleiman now.

**Vivek Shankar:** So I think we can send smaller passes to manually publish and test with the automated patch.

**Nika Narimanidze:** Oh, sorry.

**Nika Narimanidze:** Just to jump in there.

**Mara Leighton:** Is that one where we should be, like, should I be paying Victoria next week or the week after for that?

**Mara Leighton:** Or is it kind of like to our benefit that it might take her a little bit longer to review?

**Vivek Shankar:** It's to our benefit if she takes a little longer.

**Nika Narimanidze:** Vivek, next question about RAMP vendor pages. Are we creating the assignments ourselves, or will Victoria handle it?

**Vivek Shankar:** We create them ourselves. It's pretty simple. I think I dropped the spreadsheet in the internal bookmarks. Essentially, if in doubt, check bookmarks. There's a lot of stuff there and we need to organize it at some point, but for now everything's there.

**Usman Ghani:** Can I add something?

**Vivek Shankar:** Yeah, sure, go ahead.

**Usman Ghani:** Well, for high-level approaches, how are we sharing it?

**Usman Ghani:** I saw your comment to Gurzhar about the CTA image. I thought the workflow was about infographics?

**Vivek Shankar:** The workflow generates images like Napkin does. It should also be able to generate images based on their Figma board, which was part of the original spec I sent. If it's not doing that, that's a defect we need to flag. Since it's not working right now, I asked Gurzhar to just send us the CTA image. Gurzhar will send it, and you'll need to add it to all comparison pages next week. We're publishing five or six comparison pages this week — three older ones and three in the queue — without the CTA. Next week we'll include the new CTA in new pages and update all older published comparison pages with it.

**Usman Ghani:** Yeah.

**Nika Narimanidze:** For Rapid, I've noticed we've been identifying new audiences for articles. Do we have a document listing all audiences relevant for Rapid?

**Vivek Shankar:** Broadly speaking, Rapid has two audiences: general payment ops audience, or it depends on the article itself. If an article mentions merchants, it's merchants audience. If the category says high-risk industry, we focus on high-risk industries. But a lot of their articles are just general payment ops audience — like the stablecoin and LATAM content.

**Nika Narimanidze:** One more thing — when I was on vacation, Tiago mentioned we should include more technical details, like code, in editorials. Should I reframe my article generation prompts to include code when relevant?

**Vivek Shankar:** Let's do it after the SOW is discussed. For now, let's keep running as is — it's not a disruption.

**Vivek Shankar:** Just as an update, I walked Nika through the strategy building process in Airtable that we discussed, in case we need to do it.

**Mara Leighton:** I'd also be curious about that. Maybe I'll review the call so you don't have to discuss it with me again. Thanks for doing that — I'll share the recording after the call.

**Nika Narimanidze:** Cool.

**Mara Leighton:** If Rapid sends us new ICP personas (which I don't expect), they'd be net new and we'd discuss which articles to apply them to. But let me know if there's anything else to keep in mind for that process.

**Vivek Shankar:** The articles we're writing are still for a general audience. Even if they send new ICP personas, I think general audience applies. The only work needed is developing content assignments for those personas and clusters. We can handle that once I come back. Just keep status quo until they send it.

**Mara Leighton:** Okay, cool.

**Mara Leighton:** Sounds good.

**Ismail Ajagbe:** So for pillar and model pages, are we starting to update them next week?

**Vivek Shankar:** Yes. Next week we'll be sending the pillar page refreshes. The week after, we might start the model pages. I haven't heard updates from them yet, but I'll include a couple anyway in case they come back and say they're ready. We'll see.

**Mara Leighton:** Vivek, I know we'll have more chatting today, but have so much fun on your vacation. Where are you going?

**Vivek Shankar:** I'm going to Peru. I'm doing the Machu Picchu hike. I've always wanted to go. I'll be there till early December. It's at about 4,000 meters altitude, and the best way to deal with altitude sickness is to chew coca leaves. Should be an interesting trip.

**Mara Leighton:** That's amazing. They have llamas there too — send us some pictures. Well, I hope you have a great weekend. Thanks for the great work, everyone. Bye, guys.

**Vivek Shankar:** Thank you. Bye.
