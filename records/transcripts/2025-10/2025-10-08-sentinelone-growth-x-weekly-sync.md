# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-10-08
time: 13:59 UTC
duration: 27 minutes
organizer: Aida Knežević (GrowthX)
participants: Aida Knežević (GrowthX), Marcus Derencius (GrowthX), Nicolas Castellanos (GrowthX), Katya Luscomb (GrowthX), Ankit Pahuja (SentinelOne), Mansi Bhalothia (SentinelOne), Drew Hoffman (SentinelOne), Mahati Rapol (SentinelOne)
fathom_recording_id: 92690268
fathom_url: https://fathom.video/calls/434652790
share_url: https://fathom.video/share/sSxL4YvqHD5uXzJp2VhyHXyt8QfsBiQM
source: fathom
enriched_on: 2026-03-02 18:30 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne aligned on the CVE vulnerability database launch strategy, with Marcus confirming the demo ContentStack integration is ready and a phased rollout plan targeting 50 initial entries scaling to 500 over approximately 10 days. Aida committed to creating a release plan by week's end (using the Cybersecurity 101 launch as a template) while Marcus identified October 15th as tentative pending completion of a working prototype by end of week. Separately, the content production pipeline is on track with six editorial pieces delivering by week's end, four articles pending PMM feedback revisions, and Katya building out additional content assignments to maintain velocity—meanwhile the Looker dashboard is being updated with blog traffic data, with the first published piece already receiving over 50 clicks.

---

## Context

This is a weekly sync between GrowthX's delivery team and SentinelOne's product and content leadership on two concurrent initiatives. The primary focus is SentinelOne's CVE vulnerability database—a new public-facing feature that will aggregate CVE information with threat analysis and publishing directly to SentinelOne's website via ContentStack. SentinelOne is under internal pressure to launch soon, and this sync ensures alignment on technical implementation (Marcus's Atlas workflow integration), release readiness (Aida's rollout plan), and content strategy (Ankit's search volume-based prioritization of 500+ CVEs). Secondarily, the team discusses progress on Cybersecurity 101 content production, which includes both native GrowthX pieces and SentinelOne-branded editorial content with PMM review cycles. This is an ongoing engagement with significant technical and editorial complexity, requiring weekly coordination between GrowthX's engineering, product, and editorial teams and SentinelOne's product, marketing, and web engineering teams.

---

## Relevance

**To GrowthX Delivery:**
- CVE database is a new content production methodology at scale (500+ pages, automated content generation with NVD + GitHub exploit validation). Requires coordination between development (Marcus/Nicolas), product (Aida), and editorial (Katya).
- Phased rollout strategy (50 → 500 over ~10 days) de-risks launch and protects against bugs at scale—good model for future client launches.
- Content pipeline pressure: six pieces due by end of week (Oct 11), four articles in PMM review cycles. Mansi is embedded client-side handling feedback.

**To CheckThat:**
- CVE database includes GitHub exploit detection and automated vulnerability analysis—directly leverages threat intelligence and GitHub data capabilities that align with CheckThat's AEO research.
- ContentStack migration is broader SentinelOne initiative; CVE database is first phase after Cybersecurity 101 launch.

**To GrowthX Business Development:**
- SentinelOne is experiencing internal pressure to launch—indicates high visibility within their org and suggests expansion/upsell opportunity if execution is flawless.
- Ankit's involvement in publishing strategy and search volume analysis shows SentinelOne investing heavily in SEO impact, not just feature parity.
- Reference potential: Cybersecurity 101 launch was successful (went live Tuesday Oct 7). CVE database success will strengthen relationship and case study for similar B2B software clients.

---

## Overview

- CVE database integration complete; Marcus publishing test batch (15-20 entries) to temp ContentStack account before full 500-entry rollout
- Publishing strategy: Focus on CVEs from 2020+ with 200+ monthly search volume; phased launch with 50 entries first, scaling to 500 over ~10 days
- Release plan: Aida to draft by week's end using Cybersecurity 101 launch as template; Oct 15 tentative pending Marcus's working prototype
- GitHub access: Nicolas flagged need for SentinelOne web team access to integrate CVE database into production codebase
- Content pipeline: 5 articles in production, 1 receiving PMM feedback revision; 6 total pieces to SentinelOne by end of week (Oct 11)
- PMM review: 4 articles reviewed; Mansi handling feedback incorporation (prompt injection attack, AI pen testing sections)
- Traffic tracking: Blog traffic being imported to Looker dashboard; first published piece exceeded 50 clicks; URL display glitch being resolved

---

## Key Topics

### CVE Database Development Progress

  - Marcus updating Atlas workflow to generate individual CVE pages for ContentStack
  - Demo account integration complete; ready to start publishing to ContentStack
  - Plan to publish test batch (15-20 entries) before full 500-entry launch
  - Ankit shared publishing strategy: focus on recent CVEs (2020+) with 200+ monthly search volume
  - Phased rollout: 50 entries at launch, gradually increasing to 500 over \~10 days

### Release Plan and Timeline

  - Aida to create release plan by end of week, using Cybersecurity 101 launch as template
  - Tentative launch date: October 15th (pending developer confirmation)
  - Marcus to create working prototype by tomorrow to assess timeline feasibility
  - Nicolas raised need for GitHub access to integrate with SentinelOne's codebase

### Content Generation Pipeline

  - Uses CVE number as input, fetches data from NVD and other sources
  - Searches for GitHub exploits and confirms if active
  - Generates detailed markdown article with threat analysis
  - Capability to process multiple CVEs in parallel
  - Plan to implement watcher for new CVE releases

### Content Production Update

  - 5 articles in production this week, 1 article being revised
  - 6 total editorial pieces to be delivered by week's end
  - Katya developing additional assignments to maintain content pipeline
  - 4 articles reviewed by PMM team; some require minor changes
  - 4 articles (including behavioral detection attack and NIST attack) to be published this week

### Traffic Monitoring

  - Looker dashboard being updated with blog traffic data
  - First published blog received over 50 clicks
  - Temporary glitch preventing URL display in Looker, being addressed

---

## Action Items

**Marcus Derencius (GrowthX)**
- Publish initial batch of CVE data to temporary ContentStack account for testing
- Develop working prototype of CVE database integration with ContentStack by end of week

**Aida Knežević (GrowthX)**
- Create & share CVE database release plan by end of week, including timelines, roles, responsibilities, contingency plan
- Record & share video demo of CVE content generation pipeline for documentation
- Resolve URL display issue in Looker dashboard for blog traffic tracking

**Nicolas Castellanos (GrowthX)**
- Raise GitHub access request with SentinelOne web team during upcoming call

**Katya Luscomb (GrowthX)**
- Review 5 articles in production, apply edits to 1 article, deliver 6 editorial pieces to SentinelOne by end of week
- Create additional content assignments, cross-referencing existing Cybersecurity 101 content

**Mansi Bhalothia (SentinelOne)**
- Apply PMM feedback to prompt injection attack article
- Update SentinelOne sections in AI pen testing article

---

## Transcript
**Aida Knežević:** Thanks for joining Marcus, there's just a lot of like back and forth, and I just was like, let's just get Marcus here so he can answer questions directly, because I know the team is like anxious to get this set up on their website and launched.

**Aida Knežević:** I think they're facing like a lot of like internal pressure to launch this, so it would just be helpful to hear from you like the timeline and how things are progressing.

**Aida Knežević:** Have you been joining the calls with the dev team, or is that something that Nicolas has been working on?

**Marcus Derencius:** Yeah, he did the last one, so this is going to be my first one.

**Aida Knežević:** Okay, do you want me to add you to that call, or did he add you already?

**Marcus Derencius:** He didn't.

**Marcus Derencius:** He did not, so, yeah.

**Aida Knežević:** Okay, I can add you right now.

**Marcus Derencius:** Okay.

**Marcus Derencius:** I think this is awesome.

**Ankit Pahuja:** Hi everyone.

**Katya Luscomb:** Good morning.

**Aida Knežević:** Hi everyone. Sorry, I'm camera off today.

**Aida Knežević:** I'm dealing with an allergic reaction on my face, so it's a little bit red and I'm just not camera ready, but I'm here.

**Aida Knežević:** I'm listening.

**Aida Knežević:** So I just wanted to flag that.

**Aida Knežević:** So yeah, thanks for joining.

**Aida Knežević:** I have on the call today, we have Katya, who's a managing editor who's been editing the CS one-on-one content for you.

**Katya Luscomb:** Katya, do you want to just do a quick intro?

**Katya Luscomb:** Yeah, it's nice to actually meet you guys.

**Katya Luscomb:** I know we've chatted a little bit on Slack.

**Katya Luscomb:** I am ramping up with GrowthX.

**Katya Luscomb:** I have a variety of editorial experience in my back pocket. Before this, I was actually doing a lot of editing and creating content to train LLMs, so I'm really familiar with some of the nonsense that it spits out and how to fix it.

**Katya Luscomb:** But excited to be working with you guys, and yeah, it's been fun digging into all your content.

**Ankit Pahuja:** Nice to meet you, Katya.

**Aida Knežević:** And then we also have Marcus here.

**Aida Knežević:** He is another software developer on our team, along with Nicolas, who's working on setting up the CVE vulnerability database on your website.

**Aida Knežević:** So I've brought both Nicolas and Marcus here so they can answer any questions that you have about timelines.

**Aida Knežević:** Marcus is also going to join the sync with your web team tomorrow.

**Aida Knežević:** But I think I can actually just share my screen to share the agenda.

**Aida Knežević:** And then, Ankit, you can just, you know, let us know what's, you know, the most pressing thing on your mind.

**Ankit Pahuja:** What do you want to discuss first?

**Ankit Pahuja:** All right.

**Ankit Pahuja:** I think we can start with the vulnerability database itself.

**Ankit Pahuja:** And I do have some ideas to share on the publishing side also how we were talking on Slack on how we'd like to approach that.

**Ankit Pahuja:** I was able to put together some things for that, something visual that kind of can explain how we'd like to go around, and publishing.

**Ankit Pahuja:** I think that's one agenda.

**Ankit Pahuja:** I'd like to spend some time on that.

**Ankit Pahuja:** Rest, let's go through the agenda you had set.

**Aida Knežević:** Yeah, yeah, for sure.

**Aida Knežević:** Okay, so to give you a quick update on the CVE database process.

**Aida Knežević:** So, Marcus, do you want to share just, you know, what the changes were made to the Atlas workflow?

**Marcus Derencius:** What are the next steps with ContentStack and, like, building out the CVE index?

**Marcus Derencius:** Yes, sure.

**Marcus Derencius:** So today, I just start changing our workflow so we can generate the page, each page with all the separate data, so we can easily insert in ContentStack.

**Marcus Derencius:** So right now, I have a demo account with ContentStack that I can insert the data automatically, so we can start publishing to ContentStack, all the CVE pages that we generate from Atlas, so that's the next step.

**Marcus Derencius:** So it's working, the integration, I just need to start that publishing on the instance of content stack.

**Marcus Derencius:** And the next step is going to be the web page is going to be able to load the CVEs, so that's the next change that's going to be working.

**Marcus Derencius:** So for today.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** So today.

**Marcus Derencius:** Yeah.

**Marcus Derencius:** Yeah, today I hope to get it published to ContentStack.

**Marcus Derencius:** It's going to be to my trial account, or we get the final tokens and access to the production one.

**Aida Knežević:** So right now we have access to a temporary ContentStack account. Once Marcus publishes everything to the temporary account and it looks good, then we can get access to the actual SentinelOne ContentStack production account, and then we can publish there, right?

**Aida Knežević:** That's like the process?

**Aida Knežević:** Okay, okay, all right.

**Aida Knežević:** Okay, so we're on the right track.

**Aida Knežević:** And then we wanted to, this is also a question for you, Marcus.

**Aida Knežević:** So I know that SentinelOne wants to, Mahati said that you would like to launch the database with around at least like 500 CVE entries.

**Aida Knežević:** And that's fine. We just want to avoid a situation where we publish 500 right off the bat, and then there's, you know, a bug that impacts all of those pages.

**Aida Knežević:** So I was thinking maybe we just publish a test batch first of around 15, 20, make sure that they look good, and then we can, like, publish the remaining ones.

**Marcus Derencius:** Yeah, that works well.

**Aida Knežević:** Okay.

**Aida Knežević:** Does that work for you as well, Ankit?

**Ankit Pahuja:** Yeah, that's right.

**Aida Knežević:** Yeah.

**Aida Knežević:** Okay.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** And I know that, Ankit, you would like to kind of see a release plan for the vulnerability database.

**Aida Knežević:** I'm happy to put it together for you.

**Aida Knežević:** If you could just let me know, like, what specifically you would like to see in it, especially if you're presenting it to other people in the company, you can let me know, like, what kind of information you want me to put in there.

**Ankit Pahuja:** Do you mind if I share my screen?

**Aida Knežević:** Yes, of course.

**Ankit Pahuja:** I to touch upon both the things just a moment.

**Ankit Pahuja:** Yeah, just a second, I'm just fetching the right documents before I could share around it.

**Ankit Pahuja:** So, two things.

**Ankit Pahuja:** First one being the publishing plan.

**Ankit Pahuja:** So we were able to do some analysis around what CV pages we'd want to put together.

**Ankit Pahuja:** I was seeing that this document is shared with team at growthlabs.com.

**Ankit Pahuja:** Would you want me to share individually with all of you or would that work?

**Aida Knežević:** We can access it via the team account and then, like, grant additional access.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** Sounds good.

**Ankit Pahuja:** The most important tab that I wanted to talk through in this call is the publishing strategy.

**Ankit Pahuja:** So, we are keeping recency of CV pages or vulnerabilities found.

**Ankit Pahuja:** And also search volumes that, you know, the CVE pages have most for.

**Ankit Pahuja:** So we are trying to combine the two as part of our strategy in terms of what we publish.

**Ankit Pahuja:** And we figured out that, you know, there are only a few, I mean, if we talk about how many CVEs that came out in, say, year 2020 and onwards until today, there are upwards of 8,000 of those, but we, because we want to go around recency and what's being searched on SERP is what we had shortlisted.

**Ankit Pahuja:** So this filter should help.

**Ankit Pahuja:** So this basically is search volume, filter for anything with monthly volume of over 200 for a CVE search.

**Ankit Pahuja:** These are the pages, these are the number of vulnerabilities that are there per year. So let's do 500 of those in the first phase.

**Ankit Pahuja:** The first phase is just after we develop the vulnerability database. When we release 500 over ContentStack, that's what we do as the first phase. The first 500 are from the year 2023 to 2025—these are the ones with over 200 monthly search volume for each. So it covers both recency and volume, and that's how we choose the ones to publish to have the most impact with this project.

**Ankit Pahuja:** And how we publish?

**Ankit Pahuja:** I think we were thinking the same.

**Ankit Pahuja:** Aida, like you mentioned, let's do 50 as first in the launch and then we can.

**Ankit Pahuja:** Gradually in the stage of like 15 days or whatever the timelines are, again, these are indicative.

**Ankit Pahuja:** We can decide those together as we put up our release plan.

**Ankit Pahuja:** So, but yes, we can have a 10-day period where we gradually roll out 500 of those over content stack.

**Ankit Pahuja:** So, again, timelines are really indicative.

**Ankit Pahuja:** The dates are just indicative.

**Ankit Pahuja:** I know we are not going live October 15th for sure, but let's, however we keep the release plan, we progress from there.

**Ankit Pahuja:** I'll stop there.

**Ankit Pahuja:** Any questions on the plan and the thoughts and how we were thinking for this?

**Aida Knežević:** Yeah, quick question.

**Aida Knežević:** This is for Marcus.

**Aida Knežević:** So, do we have the capability to schedule the publishing or does this have to be done manually?

**Marcus Derencius:** schedule done manually?

**Marcus Derencius:** I have to confirm, because we can put the data in content stack as draft, and then later we change the publish.

**Marcus Derencius:** So even if it's required like a manual, probably it's going to be on content stack.

**Marcus Derencius:** So we can try to automate that, but I just have to confirm if we can schedule a way to change that in content stack.

**Ankit Pahuja:** Yeah, in content stack, what's possible is, say for a batch, say we put 500 of those as drafts in content stack, and then we can select multiple, hit publish in one.

**Ankit Pahuja:** So I think this is a small number, even our internal SEO team can help do that.

**Marcus Derencius:** Yeah, that's why I think that's the manual solution would be quick list stacks.

**Ankit Pahuja:** That's right, yeah.

**Aida Knežević:** Okay, sounds good.

**Aida Knežević:** Okay.

**Aida Knežević:** So, is this list of CVEs the one that we also have in Airtable or it's filtered, right?

**Ankit Pahuja:** Yeah, the only thing we did as on today was we fetched, I think what we did the last week, we did today, fetched newer CVEs that were added to the list of 2025.

**Ankit Pahuja:** REST, it would be the same, but we can refer to the sheet because of some filters we have in here.

**Ankit Pahuja:** So, when we apply this filter, everything filters up here and we can exactly get these CVEs that we want to go after.

**Aida Knežević:** Okay, okay, perfect.

**Aida Knežević:** Yeah, think, Katya, we could just then copy this into Airtable.

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** We came, we are trying to publish or have the strategy just in the idea that we keep crawl budgets in mind for SERP and then...

**Ankit Pahuja:** We get the most of the indexation, and of course on the dev side and the tech side we don't leave behind any buggy environment in production. With a lot of pages there's a lot of traffic coming in, but we'll be able to do the QA together and take care of things before we publish. Anyway, next up is the release plan. I'm sure all of you know that ContentStack is the new CMS we're going to have and we're gradually moving from WordPress to ContentStack for the entire SentinelOne web property. We did our first push

**Ankit Pahuja:** Tuesday, yesterday, where we released Cybersecurity 101, the English version of the site, and I'm presenting the release plan for that.

**Ankit Pahuja:** So this could be a good reference point with all the necessary details. The GrowthX web team meets with SentinelOne's web team weekly, so we could tailor the approach. This is something we could prepare in terms of a release plan. It's more about timelines, roles and responsibilities, and kind of a contingency plan just in case something goes south. I'll share this with you.

**Aida Knežević:** Sure, sure.

**Aida Knežević:** No, I can put this together for you by the end of the week.

**Aida Knežević:** Share it.

**Ankit Pahuja:** That's it.

**Ankit Pahuja:** And once we finalize, I use this to talk through internally, and the idea would be to keep up the dates that we decide to go live with.

**Aida Knežević:** Okay, okay.

**Aida Knežević:** I know this could be, Marcus and Nicolas, I know this could be, like, a bit of a question that you can't answer right now, but does October 15th, that's next week, so does that sound like a realistic live date for you, or do you think we're going to be a little bit late?

**Aida Knežević:** Like, what's all dependent?

**Marcus Derencius:** Okay.

**Marcus Derencius:** Yeah, we need to do a first draft, try to do work, like, today and tomorrow to get a first, like,

**Marcus Derencius:** Working prototype that we can be sure about this date.

**Marcus Derencius:** So it looks doable, but yeah, I just need to get like this first prototype working.

**Aida Knežević:** Okay.

**Aida Knežević:** Okay.

**Nicolas Castellanos:** Thank you.

**Nicolas Castellanos:** One thing we're going to need is access to GitHub, which still we don't have.

**Nicolas Castellanos:** If we can get that soon, that will be perfect.

**Nicolas Castellanos:** Because, yeah, at some point we're going to need to integrate this into your code and that's going to take a little bit of time.

**Ankit Pahuja:** The sooner we get, the better.

**Ankit Pahuja:** Nicolas, I think it would be great if we could raise this up with the web team.

**Nicolas Castellanos:** Yeah.

**Ankit Pahuja:** And I think we have a call in a few hours with the web team.

**Ankit Pahuja:** So I think that's the great place because I think resolution would be faster with them.

**Nicolas Castellanos:** Nice.

**Nicolas Castellanos:** Thanks.

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** I'll share both the documents also over Slack so that everyone has access to it.

**Aida Knežević:** Thank you.

**Aida Knežević:** Okay, I know that you were also curious about seeing, like, the content generation pipeline for the CVE pages.

**Aida Knežević:** I think, I mean, I can share it.

**Aida Knežević:** I can show it right now just so you, it's not very, because it's connected to different APIs in the background.

**Aida Knežević:** So I can just share, like, what it looks like.

**Aida Knežević:** So we just used the CVE number as the input, and then it connects to different APIs.

**Aida Knežević:** You can see in the input, so it fetches NVD data, it enriches the vulnerability information, and then it produces a detailed markdown article with threat.

**Aida Knežević:** going it.

**Aida Knežević:** Analysis.

**Aida Knežević:** So the output, and this is like the first one that we generated.

**Aida Knežević:** I'm sure that like it looks different right now.

**Aida Knežević:** But for example, this is the output that we get.

**Aida Knežević:** I don't know, Marcus, Nicolas, you have like any additional insights here?

**Aida Knežević:** Because you were the ones who set this up.

**Nicolas Castellanos:** So I'm sure you could like provide additional info to Ankit.

**Nicolas Castellanos:** Yep.

**Nicolas Castellanos:** Yeah, as Aida was saying, it takes a CVE number and then it goes to the NVD and this other, I can't remember which one is the other source, but it's NVD and this other one that it's well known.

**Nicolas Castellanos:** And then it tries to look for like exploits on GitHub.

**Nicolas Castellanos:** If it finds one, it tries to confirm it's an action exploit.

**Nicolas Castellanos:** Right.

**Nicolas Castellanos:** And generates that markdown that you're seeing down there.

**Ankit Pahuja:** So would it import or take input as a batch of CVEs and then give output?

**Nicolas Castellanos:** in that page Aida was showing, you can submit plenty of CVEs.

**Nicolas Castellanos:** Each of those will be a row and they will get processed in parallel.

**Nicolas Castellanos:** So, yeah, you can just batch as many as we want.

**Ankit Pahuja:** Okay, sounds good.

**Ankit Pahuja:** So in the documentation or the release plan or anything that we created on this, it would be great if you could record a little video of how all this is happening and just place in there so that every time we talk about it, I could point people to that video and save your time.

**Nicolas Castellanos:** Yeah.

**Nicolas Castellanos:** Oh, one thing I have, I remember having the idea that we wanted to have like a watcher that was like listening for know.

**Nicolas Castellanos:** I

**Nicolas Castellanos:** Newer CVEs released to the world.

**Nicolas Castellanos:** Is that a thing?

**Nicolas Castellanos:** Yeah, have that on the plan too.

**Nicolas Castellanos:** So how that will work is we will have a watcher that will look into the internet for new CVEs and prepare the CVE directly from there.

**Nicolas Castellanos:** Like newer ones probably won't have much information because until there is an exploit or there is like information from vendors or whatever, maybe there is much.

**Nicolas Castellanos:** But at least we'll have something prepared to ship as soon as like we're ready.

**Ankit Pahuja:** Sounds good.

**Ankit Pahuja:** Yeah, exactly.

**Ankit Pahuja:** That was my next question for maintenance of CVEs and the ongoing database.

**Ankit Pahuja:** It's great that we have this in plan already and that can also take place in the release plan and the documentation we do.

**Aida Knežević:** Perfect.

**Aida Knežević:** Do you have any other questions around the CVE database?

**Ankit Pahuja:** I think I'm good with the database conversation.

**Ankit Pahuja:** Let's put together that release plan.

**Ankit Pahuja:** I think it's the time when we should really talk about go-life date, and that's one question I keep getting whenever I meet people.

**Aida Knežević:** Yep.

**Aida Knežević:** I know.

**Aida Knežević:** I know.

**Aida Knežević:** I bet.

**Aida Knežević:** So yeah, that's why I wanted to get everyone in the same room, just to get you answers immediately.

**Aida Knežević:** So hopefully I think by the end of this week, Marcus will have an idea of how the staging went and the prototypes, so that can give us a better idea of when these pages can go live.

**Ankit Pahuja:** But it is in progress.

**Ankit Pahuja:** Sounds good.

**Aida Knežević:** Okay.

**Aida Knežević:** Um, Katya, did you want to give a quick content update?

**Aida Knežević:** Just what's in production right now?

**Aida Knežević:** What's waiting for revisions?

**Aida Knežević:** What's ready for review?

**Katya Luscomb:** Yeah, we have five articles that are in production for this week.

**Katya Luscomb:** I'll be taking a look at those later today or early tomorrow.

**Katya Luscomb:** But all five of those will be overdue by the end of the week.

**Katya Luscomb:** And then we have one that we received some edits from you guys at the end of last week that I'm going to apply those edits and get over to you as well.

**Katya Luscomb:** So we'll have six editorial pieces delivered to you by the end of this week.

**Katya Luscomb:** And then I am also working on, because we had five assignments that were approved for this week, I'm working on building out some additional assignments for everybody to take a look at.

**Katya Luscomb:** So hopefully we can buff up our list and we all have to ask you for approval every week.

**Ankit Pahuja:** Yeah, I remember we having some, so Mansi was out of office and then we wanted some approvals.

**Ankit Pahuja:** So the process for us is...

**Ankit Pahuja:** So, we have a central SEO team who knows what sits in Cybersecurity 101, what are other people working on in terms of content.

**Ankit Pahuja:** we just want no duplicacy happens for any effort that we put up.

**Ankit Pahuja:** Hence, we take a little time for approvals just to make sure we are avoiding any duplicate efforts.

**Katya Luscomb:** 100%.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** And as I'm building out the assignment list, I'm trying to cross-reference existing CS101 content.

**Katya Luscomb:** But yeah, totally appreciate that you guys are keeping an eye on what you have in the pipeline as well.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** Mansi, anything you have for Katya in terms of any pieces of content you had received that's pending reviews, absolute any conversation, any feedbacks from the PMM team, for growthx team?

**Mansi Bhalothia:** Yeah, we got four articles reviewed by PMM.

**Mansi Bhalothia:** If I'm going to make some changes to prompt injection, prompt injection attack, but if Katya wants to have a look at PMM comment, she can for that particular article.

**Mansi Bhalothia:** And then we have PMM comments and AI pen testing, testing articles.

**Mansi Bhalothia:** So the S1 sections, since they gave me a bit of feedback on them, I'll make the changes.

**Mansi Bhalothia:** But if you want to have a look at the comments they gave and the links they shared to the S1 articles, you can have a look at them.

**Mansi Bhalothia:** And then we will be proceeding to publish four articles this week.

**Mansi Bhalothia:** That would also include behavioral detection attack and NIST attack.

**Mansi Bhalothia:** So these two will also go like this week.

**Katya Luscomb:** Fabulous.

**Katya Luscomb:** Thank you.

**Katya Luscomb:** Yeah, and I'll take a look at that feedback because we can probably incorporate it into some of our artifacts so that going forward we can just get tighter and tighter with how we're describing your products and different aspects as well.

**Mansi Bhalothia:** Makes sense.

**Aida Knežević:** Okay, perfect.

**Aida Knežević:** I don't think, just yeah, yeah, one last update is that we are updating the Looker dashboard with all the blogs that we publish.

**Aida Knežević:** We have been, like, especially the first blog that we published, it's gotten over 50 clicks so far, and the other blogs have been getting traffic as well.

**Aida Knežević:** But, and we just import those URLs into the Looker dashboard.

**Aida Knežević:** There is a glitch, however, so those URLs aren't showing up in Looker, but we're looking into it right now.

**Aida Knežević:** And hopefully by the end of the week, you can start checking the Looker dashboard for traffic updates.

**Ankit Pahuja:** All right, yep, I look forward to that.

**Aida Knežević:** Okay, awesome.

**Aida Knežević:** Well, if that's everything, I think.

**Aida Knežević:** We can call it a day.

**Aida Knežević:** I'll be in touch, Ankit, with the vulnerability release plan.

**Aida Knežević:** And, yeah, if you need anything in the meantime, just send me a message.

**Ankit Pahuja:** Sure.

**Aida Knežević:** Thanks, babe.

**Aida Knežević:** All right.

**Aida Knežević:** Thank you.

**Aida Knežević:** See you.

**Ankit Pahuja:** Thanks, everyone.

**Katya Luscomb:** Bye.

**Katya Luscomb:** to you all.
