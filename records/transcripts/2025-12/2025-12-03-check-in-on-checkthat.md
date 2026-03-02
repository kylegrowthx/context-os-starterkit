# Check in on CheckThat

<metadata>
date: 2025-12-03
time: 19:59 UTC
duration: 28 minutes
organizer: talal@growthx.ai
participants: Talal Syed, Kyle Gaudreau, Nika Narimanidze
fathom_recording_id: 106087828
fathom_url: https://fathom.video/calls/494354062
share_url: https://fathom.video/share/ZuyAG3cPkYsb2S6mmcX6PsVu1F5DjCiQ
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Talal, Kyle, and Nika aligned on critical CheckThat priorities: fixing the indexing failure that blocks SEO strategy, migrating all client prompts from Scrunch to CheckThat to preserve quality during the transition, and building a scalable workflow for automated prompt creation. The team clarified operational needs including a dedicated engineering POC for prompt automation, strategic SEO planning to index only 100-200 high-quality pages initially, and establishing the #account-strategy Slack channel as the primary communication hub to replace the overly noisy #project-check-that-ai-v1 channel.

---

## Context

CheckThat is GrowthX's strategic AI visibility software product—a bet that sits alongside the core B2B content marketing services business. The team has been working on launching CheckThat with a focus on SEO as a core differentiator: the product allows clients (and GrowthX itself) to monitor AI visibility across models and optimize prompts to improve search rankings. This internal alignment call was scheduled because the team noticed confusion spreading across multiple Slack channels and needed to consolidate understanding before executing the month's highest-priority work. Talal (product/strategy lead) recognized that communication about CheckThat had fractured into "bits and pieces across different channels" and called the meeting to ensure Nika (marketing/SEO) and Kyle (operations) shared a unified picture of what to ship and in what order.

---

## Relevance

**To GrowthX Business Development:**
- CheckThat is now the highest-priority product initiative (higher than base business delivery), requiring dedicated focus and capacity management through year-end
- Nika's SEO expertise will directly influence strategy; her input on 100-200 page indexing strategy is essential to avoid domain-authority damage
- Prompt migration and automated workflow are key conversion levers for moving strategy sprint leads into CheckThat retainers

**To CheckThat Product:**
- Indexing bug fix was already completed by engineering, unblocking SEO strategy execution
- CSV bulk upload feature is missing and blocking scalable prompt migration; needs to be flagged to engineering as a blocker
- Automated prompt creation workflow is a critical selling point and must be operationalized (not manual) to be viable for clients
- Domain authority strategy requires starting with only 100-200 high-quality indexed pages to prevent ranking penalties on new domain

**To Operational Execution:**
- Engineering coordination bottleneck: no clear POC or recurring sync established for CheckThat; Kyle will identify the right engineer
- Communication structure needs fixing: #project-check-that-ai-v1 is too noisy for cross-functional work; #account-strategy channel designated as primary hub
- Talal will be available during last week of December (returning to US on-site); capacity considerations noted for other GrowthX initiatives

---

## Overview

- **Top Priority: Fix Indexing.** The primary goal is to resolve CheckThat's indexing failure, which is blocking its SEO strategy.
- **Prompt Migration is Urgent.** To prevent client quality drops, all Scrunch prompts must be migrated to CheckThat ASAP, starting with high-priority clients like Augment Code.
- **New Workflows Needed.** The team requires a dedicated engineering POC to automate prompt creation and a clear process for reporting product bugs (e.g., the missing CSV upload).
- **Strategic Indexing Plan.** To protect the site's authority, only 100–200 high-quality pages will be indexed initially, with a focus on defining their content and template.

---

## Key Topics

### Problem: CheckThat Indexing Failure

  - CheckThat pages are not being indexed by Google, preventing the SEO strategy from working.
  - The team needs to align on priorities and consolidate communications, which are currently fragmented across multiple channels.

### Solution: Prompt Migration & Automation

  - **Goal:** Migrate all client prompts from Scrunch to CheckThat to ensure a smooth transition and prevent service quality drops.
  - **Process:**
      - **Export:** Use the "Export your current prompts for review" feature in Scrunch (under `Context > Prompts`).
      - **Upload:** The current UI requires manual copy-pasting, as a CSV bulk upload feature is missing.
      - **Vetting:** No pre-migration vetting will occur to avoid delays. A cleanup process will be developed later.
  - **Automation:** A custom workflow is needed to automate prompt creation, making the process scalable and a key selling point for new clients.
  - **Engineering Support:** The team needs a dedicated engineering POC to build this workflow and fix bugs like the missing CSV upload.

### Solution: Strategic SEO & Backlinks

  - **Strategic Indexing:** To protect the site's authority, only 100–200 high-quality pages will be indexed initially.
      - **Rationale:** Indexing too many low-quality pages can negatively impact the entire domain's ranking.
      - **Immediate Need:** Define the content and template for these initial pages.
  - **Backlink Strategy:**
      - **Directory Listings:** A vendor will provide up to 100 listings. The team must vet the list, approving only unique, high-quality domains.
      - **Medium Backlinks:** While no-follow, these links are approved for building initial domain trust.

### Operational Improvements

  - **Communication:** The `#Project Check That AI V1` Slack channel is too noisy for marketing/engineering collaboration.
      - **Action:** Post bug reports in the channel, but ask engineers for their preferred reporting process (e.g., a Linear board).
  - **Channel Usage:** Use the `#account-strategy` channel for all CheckThat-related discussions.

---

## Action Items

**Nika Narimanidze (External)**
- Mark directory list for vendor approval; request more options from vendor if fewer than 100 quality options
- Start prompt collection and prepare backlink file for SEO strategy
- Ping Jason & Andy in #account-strategy channel to identify highest-priority clients for prompt migration; start migration workflow with Augment Code as first client
- Begin playing around with prompt upload to CheckThat; monitor for technical issues and report any bugs discovered

**Kyle Gaudreau (External)**
- Identify the right engineer or engineering POC on CheckThat team to own prompt automation workflow; schedule recurring sync to build scalable prompt creation process

**Talal Syed (GrowthX)**
- Post in #project-check-that-ai-v1 channel to ask engineering about preferred bug reporting process (Slack vs. Linear); request guidance on communication workflow
- Provide Nika with on-site SEO context and strategy for selecting and optimizing the initial 100-200 high-quality pages for indexing

---

## Transcript

**Nika Narimanidze:** Hi, how are you?

**Talal Syed:** I'm doing well.

**Nika Narimanidze:** Yeah, I'm doing well.

**Talal Syed:** One quick thing before Kyle jumps on—I was just about to respond as well.

**Talal Syed:** So that list of directories that I tagged you in, so we need to essentially go through that list and mark the ones that we actually want to get listed on.

**Talal Syed:** The vendor is going to work with us until they give us about like 100 places they could feature us on.

**Talal Syed:** So, like, if we don't like a bunch of them, I can just, like, add you to the thread and we can tell them to give us more options.

**Talal Syed:** So just, like, go through the list, mark the ones that we should get listed on with the check mark.

**Talal Syed:** And if there's, like, significantly less than 100, we can just go ahead and ask them for more options.

**Nika Narimanidze:** Yeah.

**Nika Narimanidze:** Okay.

**Nika Narimanidze:** What about the point that the backlink from Medium is not to follow backlink, just as other UGC content-generated websites.

**Nika Narimanidze:** So, uh, agencies too.

**Talal Syed:** That makes sense.

**Talal Syed:** Like, context was that stuff on check that wasn't getting indexed at all.

**Talal Syed:** So we just wanted to kickstart that very quickly.

**Talal Syed:** The directory stuff I've seen works semi well for new domains sometimes.

**Talal Syed:** Just sends a bunch of trust signals that seem to matter.

**Talal Syed:** So we are building some backlinks to it separately and I tagged you in that thread as well.

**Talal Syed:** But we also thought that we would just go ahead and do it on the directories too.

**Talal Syed:** It can't hurt, right?

**Talal Syed:** So, and it's like relatively cheap for us to do that.

**Talal Syed:** So that was the context behind doing the whole thing.

**Nika Narimanidze:** If subdirector is repeat constantly, would this be a problem?

**Talal Syed:** I think so.

**Talal Syed:** Like, I would want the links to be from unique domains.

**Talal Syed:** Yeah, aligned.

**Talal Syed:** Like the ones you identified, like if they're part of the same template or the same network, we definitely don't want them.

**Nika Narimanidze:** We want them to be ours.

**Talal Syed:** think so.

**Nika Narimanidze:** It was in total up to 16.

**Talal Syed:** Yeah, just one from each particular directory or one template on network, that should be fine.

**Talal Syed:** Other than that, I don't think it makes sense.

**Talal Syed:** I think that was spot on.

**Nika Narimanidze:** Yeah, so I'm going to mark the backlinks of medium green as well.

**Nika Narimanidze:** I agree that it gives you trust, but they should have identified that this is not a default backlink.

**Nika Narimanidze:** That was my point.

**Nika Narimanidze:** When do you want this done?

**Talal Syed:** What was the email?

**Talal Syed:** Not urgent, so fit it.

**Talal Syed:** Like, if you have other stuff that you're working on for Check That or some other clients, would put it definitely below that.

**Talal Syed:** So whenever you have capacity this week, I think that would be okay.

**Nika Narimanidze:** Yeah, I think I'll be able to start the prompt collection as the backlink file tomorrow, so that won't be a problem.

**Talal Syed:** Sounds good.

**Talal Syed:** Sounds good.

**Talal Syed:** Let's see where Kyle is.

**Nika Narimanidze:** Tal, regarding the George message, I think everything was clear.

**Talal Syed:** Yes.

**Nika Narimanidze:** Was it the same from your side?

**Talal Syed:** Yeah, things are super clear.

**Talal Syed:** I just need more context from Kyle because maybe his understanding of, like, where things are going is a little bit different.

**Talal Syed:** So I just want to make sure that all of us are on the same page, just because, unfortunately, the conversation is happening in bits and pieces across different channels and threads.

**Talal Syed:** So I just want to, like, consolidate all of that because I don't want anything to be miscommunicated, especially because CheckDart is such a higher priority project.

**Talal Syed:** So I just want to be, like, clearly aligned.

**Talal Syed:** What are we working on this month and what is expected from us?

**Talal Syed:** Just so, like, it doesn't happen that three weeks later, by the time we're wrapping up holidays, we figured out that we weren't supposed to work on a particular thing or we didn't move the needle on something that actually mattered.

**Talal Syed:** So, like, just...

**Talal Syed:** This is just an exercise to get as much alignment as possible before we actually dig into the work itself.

**Nika Narimanidze:** Yeah, good point.

**Nika Narimanidze:** Talal, just one thing that I've noticed in the Project Check That AI V1 channel, there are tons of notifications going, and I don't think we have a separate place to discuss some topics and organize, and it's bugging me a lot because it feels unstructured, and yeah, you know.

**Talal Syed:** So I think the context behind that is that Project Check That was being driven by engineering mostly, and it's okay for them because they're, like, talking about tickets, et cetera, but now that sort of marketing is getting involved, we need some separation, so stuff is a bit more cleaner because I agree with you that there's a lot of notifications.

**Talal Syed:** I've actually muted the whole channel.

**Talal Syed:** I only get notified when somebody personally mentions me, so that's been my solution to the flood of notifications.

**Talal Syed:** Mm-hmm.

**Talal Syed:** But I think it might make sense to just start another channel that is dedicated towards like engineering and marketing working together and check that.

**Nika Narimanidze:** So we can bring that up.

**Nika Narimanidze:** Yeah, yeah, yeah.

**Nika Narimanidze:** Absolutely.

**Nika Narimanidze:** I thought that was the issue a lot.

**Nika Narimanidze:** Yeah.

**Nika Narimanidze:** I had some questions.

**Nika Narimanidze:** Oh, okay.

**Kyle Gaudreau:** Hey, sorry, guys. I had an in-person meeting. For whatever reason, I thought I had more time and then I looked at the clock.

**Talal Syed:** Oh, gosh, I'm not used to this in-person stuff.

**Talal Syed:** How's it going?

**Kyle Gaudreau:** Good, good.

**Kyle Gaudreau:** Busy in the office today.

**Kyle Gaudreau:** It's office spaces at a premium.

**Kyle Gaudreau:** So I was fortunate enough to snag a room.

**Kyle Gaudreau:** But so anyway, it sounds like you guys were just chatting.

**Talal Syed:** Like, we may not even need 30 minutes here.

**Kyle Gaudreau:** I just want to make sure we're chatting live knowing there was some telephone game happening and some confusion. Like, the TLDR—my understanding is that Nika is where...

**Kyle Gaudreau:** The most support is needed is the P0 here—we have this big SEO bet around CheckThat and it's just not indexed. Like, obviously there's a lot of different layers: how to think about the off-site side of it, but also whether the important technical SEO boxes are being checked. I keep unintentionally making puns whenever I think of CheckThat, but anyway, the primary place to start is checking if there are any table-stakes things you guys haven't done yet that are obviously preventing indexing. I'm sure there are off-page things that are going to be critical to help here. And then there's also going to need to be some work around the company profiles themselves because that's a key layer of this SEO play. Like, are there elements of the structure that we want to provide guidance on? Are there technical elements to include? We might need to supplement with some research about the topical things we could be capturing and how that informs what we do on these pages. Obviously, that's a balancing game—we don't want to over-SEO this. It still needs to be functional content. That perspective would be helpful. Keep me in the loop of what the commitment and what you're finding is needed here, and pull me in where I can help. I have SEO experience I can lend. Let me know how much capacity you may have for other things, and if you're feeling stretched, let's talk about it. We can plan accordingly. Talal, knowing you're halfed this month is a curveball we can manage, but I just want to be mindful of it.

**Talal Syed:** Makes sense. And by the way, for some context, the last week of the month I'm actually going to be back in the U.S., and I don't plan to take any time off, so I can put in some work at that time. My wife will be working anyway, so that should be fine. I have some capacity there. We got some context from George in terms of what's important, so I think we should focus on exporting all the prompts we have in Scrunch for all existing clients and then loading them into CheckThat.

**Kyle Gaudreau:** I think that's something we should be able to action ASAP. Should we be scrubbing some of that? That's kind of what's on my mind. I don't want to overcomplicate this. I realize we're looking at it from the perspective of data loss if we wait, and I don't want to let perfect get in the way of better. But at the same time, I've occasionally seen accounts where there are so many prompts that aren't needed. With the context you both have, you might find it tough to assess. That's just a layer to maybe consider. There might be things that are obvious, and if we want to flag them, we can ask: do we really want to carry this over? But again, I don't want to overcomplicate the work.

**Talal Syed:** Yeah, it's just something on my mind too.

**Talal Syed:** I think for me, we can definitely add in a layer of vetting when we're doing the exports. But at the same time, I do want to move very quickly on it. Marcel was very clear that we need to make sure the quality doesn't drop from Scrunch to CheckThat for clients, and we need to get there ASAP. If we add a review step in between, it's just going to slow us down. If we can get all the prompts into CheckThat and test the workflow of adding custom prompts to make sure everything's working, that should be good. Some clients have 200 prompts, some have 5,000, and both are good edge cases to look at. We can dogfood the product while we're doing that. In parallel, I expect we're going to work on a process for how we can create prompts for any particular client and make that a workflow. Once that's in pilot and we can do it for a bunch of clients, I expect to go back and remove a lot of the crappy prompts. So I don't think we'll incur a ton of costs for the next month or two because we'll look at that soon rather than later.

**Kyle Gaudreau:** Got it, that makes sense. How much time and support do you feel like you need from Nika on the prompt side specifically?

**Talal Syed:** We haven't synced on that yet. I feel like it's pretty straightforward—Nika could probably take care of all of it. Where I want to spend time is understanding how engineering can help us create a custom workflow for generating prompts, because that's a big question mark. It wasn't super clear after the call with Marcel either. He seems to have a good process, but if it's operationalizable, then we need to turn that into a workflow that can be used in Atlas and CheckThat because we don't want to be doing this manually. Getting to a place where we can tell any client coming into a strategy sprint that we have an industry-best process for researching prompts that matter for their brand—and then showing them CheckThat—will be a huge boost for converting strategy to retainer. And it'll be important for people considering paying for CheckThat too. While Nika does the migration, I can work on how we actually coordinate with engineers. I don't think we have a recurring sync or anything right now. We probably need a POC on the engineering side who can help us build this because we'll definitely need support. I don't want delivery folks doing this because they won't compare Scrunch and CheckThat and flag issues. That's just nice-to-have. We need to automate as much of that process as possible. That's how I'm thinking about it.

**Kyle Gaudreau:** I think that makes sense. What isn't clear to me is who the right engineer or engineers are that should be on our radar. It seems like a client ops thing in Atlas, but do they have enough context on CheckThat? That's what I'm less certain about. I can try to get some clarity and figure out who we can coordinate with. Nika, pick an account, start doing some of the uploading, and monitor to see if anything's breaking. I know Marcel ran into some issues with line breaks that were breaking prompts—they were supposed to be a single prompt but uploaded as multiple. Just watch out for weird oddities like that. If something's notable, spot it early so we're not hitting the same issue across 10 uploads. But if it's all smooth, it should be a relatively quick and easy process.

**Nika Narimanidze:** Do you have admin on Scrunch so you can see all Scrunch accounts?

**Kyle Gaudreau:** George said he could show me one example of how to do this correctly because I'd never used Scrunch before and never had access. There's a CSV download thing that can get all the prompts.

**Nika Narimanidze:** I received admin access about an hour ago and signed into CheckThat. I already played around with it, but I want to avoid hiccups. I had already checked everything and I think I know how to do it.

**Kyle Gaudreau:** It's easy, but let's just do this now for time's sake.

**Nika Narimanidze:** Yeah, that would be great.

**Kyle Gaudreau:** Let me refresh my view. In Scrunch, under Context, there's "Export your current prompts for review" that downloads the CSV. It exports the prompts and category. Some accounts have 50 prompts, some have more. The platform can be buggy at times, but theoretically you should be able to download from there. There are duplicate prompts in detailed prompts too, so maybe it only showcases the unique ones.

**Nika Narimanidze:** When I looked it up, I found the same path you did—going to settings and downloading prompts. What about uploading to CheckThat? Is there a bulk upload feature?

**Kyle Gaudreau:** I haven't done that myself yet, so I think you're going to have to play around with it and see what works best. Ideally, we should support CSV upload, but maybe we just haven't added that feature.

**Nika Narimanidze:** Someone from engineering said you should copy and paste directly, so maybe that's the appropriate field, but I don't want to break things.

**Talal Syed:** Kyle, while we're on this topic, I don't know the best way to flag bugs and issues to engineering. The #project-check-that-ai-v1 channel is super noisy because there's a ton of dev stuff going on. Do we need another channel? Is there another place we can flag these things—maybe Linear? CSV upload is something that's super important.

**Kyle Gaudreau:** The way Marcel referenced it in your chat, it didn't even seem like they had a clear Linear board, but I could be wrong. I don't see anything obvious. For now, submit to that channel but also ask them: what's the best way to flag these so they don't get lost in the noise? Maybe they just need to spin something up.

**Talal Syed:** That's a good call.

**Talal Syed:** One more thing I wanted to flag. I also dropped a doc in the chat that Jason is working on—the marketing strategy for CheckThat itself. A lot of the work we're going to be doing on the site will fall under that umbrella. I talked to him yesterday, and some of the first things we need to do are make sure indexing starts. Engineering has already fixed the bug that was stopping pages from being indexed, and we've already started building some backlinks to the site. But we need to be mindful about how many pages we ask Google to index as a new site. If pages aren't high enough quality, it'll wreck the entire site. So how Jason and I are thinking about it is that we select the first 100 to 200 pages that we want Google to index and leave everything else unindexed. Questions are: what are the pages? What does the template look like? What content needs to be on each page? Those are the immediate things we need to work on. Nika, I'm going to loop you in to that work as well. So we need to work on both the product itself and CheckThat marketing at the same time.

**Kyle Gaudreau:** Absolutely. I think outreach is probably one of those high-priority clients. I know Joe created a ticket about outreach earlier. Augment and the biggest clients should be high on that list.

**Talal Syed:** Yeah.

**Talal Syed:** And one last small thing before we jump off.

**Talal Syed:** Kyle, are you thinking about spinning up a new channel for directors or is there an existing channel where we should, like, direct all of the stuff that we're working on?

**Kyle Gaudreau:** For now, let's use the #account-strategy channel. I'm trying not to create too many channels, and that's one we've had in the past that fits this type of stuff well. I don't want to inundate us with meetings, but we probably need a dedicated cadence for broader strategic discussions in the not-too-distant future. Clearly, we're all being pulled in a lot of different directions, so I'm trying to see where things shake out and figure out what we need to actually keep us aligned.

**Talal Syed:** Makes sense. So Nika, in terms of next steps, ping Jason and Andy in the #account-strategy channel and ask them which clients are more important. Just play around with migrating the prompts yourself. If you run into any issues, make a thread and tag me. If you need help from George, reach out to him too. I'll provide you with more context on the on-site stuff we need to do, but for now let's just get the prompts migrated.

**Nika Narimanidze:** Yeah, okay. Just to conclude, my priorities are the prompt library migration, then the off-page backlinks work, plus technical SEO support. I just want to make sure I export correctly from Scrunch to CheckThat. The engineering team cautioned us to be mindful of how we do this, which is why I was waiting for George to show me the right way.

**Kyle Gaudreau:** The main concern is not breaking the existing prompts that are there.

**Nika Narimanidze:** Okay, then I'll play around with it. I'm not going to wait for George, but if the video arrives, that's great.

**Talal Syed:** Cool. I appreciate the time, guys.

**Kyle Gaudreau:** That was a good plan.

**Talal Syed:** Thanks, guys. Bye-bye.
