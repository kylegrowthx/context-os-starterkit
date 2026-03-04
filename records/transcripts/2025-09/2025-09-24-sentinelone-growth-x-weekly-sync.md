# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-09-24
time: 13:29 UTC
duration: 24 minutes
organizer: Aida Knezevic (GrowthX)
participants: Aida Knezevic (GrowthX), Georgemaine Lourens (GrowthX), Sydney Go (GrowthX), Marisol Smith (GrowthX), Ankit Pahuja (SentinelOne), Mansi Bhalothia (SentinelOne), Mahati Rapol (SentinelOne), Drew Hoffman (SentinelOne)
fathom_recording_id: 89452159
fathom_url: https://fathom.video/calls/418855483
share_url: https://fathom.video/share/LMVggMd7xNm4J8-ShfktD8QQd2a9isFG
source: fathom
enriched_on: 2026-03-03 20:32 UTC
</metadata>

---

## Summary

GrowthX and SentinelOne aligned on a mid-October launch timeline for the CVE database project, with design feedback nearly finalized and development ready to begin. Content production is on track with 10 articles ready for SentinelOne review and 5 new posts in progress; the prompt hacking report blog is already ranking 4th-5th position. The team agreed to determine the optimal CVE publishing cadence (~100 per week) starting with 2025 CVEs and working backwards through 5,000+ total entries, with GrowthX managing content generation and SentinelOne's web team handling technical integration.

---

## Context

GrowthX is executing a major content and product launch partnership with SentinelOne, a cybersecurity company. The engagement centers on two key initiatives: (1) a "Cybersecurity 101" educational blog to position SentinelOne as a thought leader, and (2) a searchable CVE (Common Vulnerabilities and Exposures) database—a strategic bet to capture organic search traffic for vulnerability-related queries. This weekly sync tracks progress across design, content production, and technical integration. The CVE database project is particularly significant because it involves generating and managing 5,000+ vulnerability pages, requiring careful coordination between GrowthX's content production pipeline and SentinelOne's web development team to avoid SEO penalties from low-quality bulk publishing.

---

## Relevance

**To GrowthX Delivery:**
- CVE database project demonstrates GrowthX's ability to scale content production programmatically—critical capability for similar projects requiring 5,000+ pages
- Identified need to balance publishing volume (~100 CVEs/week) with SEO safety, underscoring importance of editorial oversight on bulk-generated content
- Sydney Go has CMS access to SentinelOne's platform, enabling direct publishing support if bottlenecks emerge
- Content OS (Notion workspace) integration is working; 10 articles in review stage, 5 in progress

**To CheckThat:**
- Prompt hacking report blog (likely generated with AI tools) is ranking 4th-5th position and driving Google Search Console clicks—validates CheckThat's content quality and SEO positioning
- CVE database will generate hundreds of pages on vulnerability-related topics, providing rich training data for AEO/AI visibility research

**To GrowthX Business Development:**
- Mid-October launch target indicates strong account momentum; both teams aligned on aggressive timeline
- Positive early SEO results (prompt hacking blog ranking high) increases renewal confidence and reference-ability
- Project complexity (5,000+ CVE pages, custom publishing pipeline) demonstrates deep technical execution and potential for upsell to other SentinelOne initiatives or similar clients

---

## Overview

- CVE page designs nearly finalized; development can begin while awaiting minor tweaks
- Content production for CS 101 blog progressing; 10 articles ready for review, 5 new in progress
- CVE database launch targeted for mid-October; specifics on content volume and publishing cadence TBD
- Prompt hacking report blog already showing positive SEO results (4th-5th position)

---

## Key Topics

### Design Updates and Approval

  - Most design feedback implemented; awaiting final color codes from Christian
  - Team alignment on current designs allows move to responsive design and development
  - Minor UI tweaks may occur, but component development can proceed
  - Georgemaine requested internal sign-off to finalize designs

### Content Production and Review

  - 10 articles in "content ready for review" status in Notion
  - 5 new blog posts in progress this week
  - Additional keyword research planned for AI-related content
  - Mansi to share S1's content calendar to avoid duplication
  - Some TOC concerns noted; feedback expected by tomorrow

### SEO Performance

  - Prompt hacking report blog already ranking 4th-5th position
  - Showing clicks and impressions in Google Search Console
  - Performance tracking via Looker dashboard

### CVE Database Strategy

  - Considering CVEs from 2020-2025 (potentially 5000+ entries)
  - Aida to consult team on optimal publishing cadence (suggested \~100/week)
  - Start with 2025 CVEs and work backwards
  - SEMrush keyword list for CVE-2025 includes \~2,600 keywords (pre-deduplication)
  - Marisol has begun generating CVE content to test the pipeline

### Development and Launch Timeline

  - Mid-October targeted for CVE database go-live
  - Nicholas and S1 web team to discuss specifics in today's meeting
  - GrowthX team flexible to accommodate dev team's timeline

### Design Clarifications

  - Color palette updates not critical; can be adjusted in production
  - Responsive designs can follow initial component development
  - Development can proceed with desktop experience, then adapt for mobile

---

## Action Items

**Mansi Bhalothia (SentinelOne)**
- Share content calendar for CS one-on-one blog with GrowthX team to avoid duplication

**Aida Knezevic (GrowthX)**
- Check with managing director on best practices for CVE page publishing cadence (to avoid SEO penalties)
- Sync with Sydney Go and Marisol Smith on CVE content generation timeline and backlog
- Message Nicholas with projections for CVE pages go-live date before SentinelOne web team meeting

---

## Transcript

**Georgemaine Lourens:** Hello.

**Aida Knezevic:** Hi.

**Mansi Bhalothia:** Hello.

**Georgemaine Lourens:** Hello, hello.

**Mansi Bhalothia:** Hello, hello.

**Mansi Bhalothia:** I don't think I have access to Notion.

**Mansi Bhalothia:** Can you please add me?

**Mansi Bhalothia:** Yeah.

**Aida Knezevic:** I'll add you to the base and you should have access to everything that's in Notion in our workspace.

**Mansi Bhalothia:** That would be great.

**Mansi Bhalothia:** Thank you.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I just sent you an invite over email.

**Aida Knezevic:** All right.

**Aida Knezevic:** Hi, Ankit.

**Ankit Pahuja:** How are things going?

**Ankit Pahuja:** Yeah, thanks a lot.

**Ankit Pahuja:** How's it for you?

**Aida Knezevic:** Good, good.

**Aida Knezevic:** Busy, busy week.

**Aida Knezevic:** But I know that Nicholas and your web team, they're meeting later today, just to discuss anything to do with the page integrations into content stack.

**Aida Knezevic:** But Georgemaine is here today as well, just to discuss like anything design related, any design questions that you might have.

**Aida Knezevic:** I don't know, did you want to go over the Figma design again, in case you have any additional feedback?

**Ankit Pahuja:** Yeah, I think should be good.

**Ankit Pahuja:** Most of the things are taken care of.

**Ankit Pahuja:** We were able to do it.

**Ankit Pahuja:** George, if there's anything you'd like to touch upon, we could.

**Ankit Pahuja:** I know there's some design color codes that are pending on Christiansen, some that you requested.

**Ankit Pahuja:** So I'll follow up with him on checking those color codes and we'll get you those.

**Georgemaine Lourens:** Okay.

**Georgemaine Lourens:** No, that's great.

**Georgemaine Lourens:** Yeah.

**Georgemaine Lourens:** So it would be nice if we could get like a color palette and gray scale so we can kind of like finalize the designs.

**Georgemaine Lourens:** But in terms of like feedback, I think the greatest thing, the most useful thing to me would be kind of like us aligning on that the pages that we designed so far are kind of like exactly what you guys are looking for.

**Georgemaine Lourens:** So we can move on to responsive design and also kind of like hand it over to the engineers and start building it.

**Georgemaine Lourens:** So if you guys could internally kind of like sign off on that, that would be great.

**Ankit Pahuja:** No, that's.

**Ankit Pahuja:** That's a valid point.

**Ankit Pahuja:** So I did speak to Mahati yesterday.

**Ankit Pahuja:** I hoping Mahati to join this call.

**Ankit Pahuja:** But yes, during her office hours with the larger brand team, she is going to bring that up and get final checks so that we could pull those components or just pull those design into dev states.

**Ankit Pahuja:** But meanwhile, I think we could start the development.

**Ankit Pahuja:** I'm sure that development has already started, at least for the components that we have, because components largely wouldn't change from here.

**Ankit Pahuja:** What might change is just the UI things bit here and there.

**Ankit Pahuja:** And personally, all the feedback has been taken care of.

**Ankit Pahuja:** We involved everyone from the team who's now also going to review earlier in the V1 feedback.

**Ankit Pahuja:** So their feedback's already taken.

**Ankit Pahuja:** You've ensured that feedback's taken care of.

**Ankit Pahuja:** So...

**Ankit Pahuja:** So...

**Ankit Pahuja:** I think we're almost there, only a minor tweaks, maybe in some color or some, you know, placement or position.

**Ankit Pahuja:** I think that also would be a larger change as a feedback that would come, but I think we are almost there.

**Ankit Pahuja:** I personally like what we have created, so I think we should be good, yeah.

**Georgemaine Lourens:** Okay, cool.

**Georgemaine Lourens:** That's great to hear.

**Georgemaine Lourens:** Thank you.

**Aida Knezevic:** All right, perfect.

**Aida Knezevic:** And I think in terms of the content updates that I shared in Notion, so right now we have 10, just a quick, to share my screen.

**Aida Knezevic:** Yeah, so right now if you go to the content OS and let me know if somebody doesn't have access to it, I can send email invites.

**Aida Knezevic:** But if you go to this view that says content ready for review, it's going to give you a clear breakdown of everything.

**Aida Knezevic:** think that's currently being reviewed by your team.

**Aida Knezevic:** Let us know if there's any, I mean, I'm sure we can change the status to, for example, growthx revisions when you send something back to us.

**Aida Knezevic:** But I assume that most of these maybe are under review by the product team.

**Mansi Bhalothia:** Yeah, that's correct.

**Mansi Bhalothia:** I think the product manager last week was out of office.

**Aida Knezevic:** It did promise to somebody did by this week.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** All of the blogs, so the five blogs from last week, they're all in.

**Aida Knezevic:** And we are working on five new blogs this week, which is this batch right here.

**Aida Knezevic:** And we're also going to do another round of keyword research for additional AI related content.

**Aida Knezevic:** I was wondering if, excuse me, I was wondering.

**Aida Knezevic:** I if you had any kind of content calendar for the CS one-on-one blog that you could share with us just so that we know what's like coming up for you so we don't suggest anything that's duplicative.

**Mansi Bhalothia:** I think we do have created a content calendar.

**Mansi Bhalothia:** I'll share it.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Then we can just go and we'll do another round of keyword research and then we can present those assignments as well.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Perfect.

**Aida Knezevic:** Did you have any additional feedback on the blogs that came in last week?

**Aida Knezevic:** Was there anything maybe that was missing or that you, you know, had to spend a lot of time editing?

**Mansi Bhalothia:** I did not spend a lot of time editing, but I did have some concerns over the TOC—table of contents.

**Mansi Bhalothia:** I have asked my colleague who is reviewing the TOC, and he might suggest some changes to them.

**Aida Knezevic:** Sorry, could you repeat that? My Wi-Fi is a little choppy.

**Mansi Bhalothia:** I think there could be some additions to the TOC. Mahinder, my colleague, is looking at it and we can provide you the feedback latest by tomorrow.

**Aida Knezevic:** Okay, okay, that works.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Sydney is the one who's been editing the content. She was out for the first three days of this week, so she's coming back tomorrow and will take a look at it then.

**Aida Knezevic:** I wanted to share something quickly—since we've only published one blog so far, I took a look at your Google Search Console to see if it's been indexed.

**Aida Knezevic:** I could see that the prompt hacking report is already getting clicks and impressions, which is good.

**Aida Knezevic:** It has a pretty high average position.

**Aida Knezevic:** So I think this is a good result, but it's also helped by your domain authority.

**Aida Knezevic:** But as we start publishing more content, we're going to be tracking the results in the Looker dashboard that I shared with you a few weeks ago.

**Mansi Bhalothia:** Yeah, we were also discussing about it.

**Mansi Bhalothia:** I think it's ranking also.

**Mansi Bhalothia:** It's at some fourth or fifth position as well.

**Mansi Bhalothia:** That's the discussion we had in that team meeting in the morning.

**Aida Knezevic:** Ah, okay.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Yeah, that's good to hear.

**Aida Knezevic:** I mean, there's a bunch of queries that it's already ranking for in here.

**Aida Knezevic:** I haven't had the chance to check SEMrush yet, but, you know, we have a Looker dashboard that's kind of goes into more, more when it comes to performance.

**Aida Knezevic:** Um.

**Aida Knezevic:** If there's, mean, I know, Mansi, that you are staging and publishing the content, right?

**Mansi Bhalothia:** No, that's done by Kathy and Mahindra.

**Mansi Bhalothia:** They take a look at publishing stuff.

**Aida Knezevic:** Okay, all right, all right.

**Aida Knezevic:** As we talked about before, with SentinelOne it's a tricky situation because getting access to your CMS requires security training. But Sydney has access to your CMS.

**Aida Knezevic:** If you need help with publishing—if you notice that blogs are ready to be published but aren't getting published—you can let us know and we can stage them for you.

**Mansi Bhalothia:** Perfect.

**Mansi Bhalothia:** That makes sense.

**Aida Knezevic:** Thank you.

**Aida Knezevic:** Yeah, yeah, no problem.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** All right, perfect.

**Aida Knezevic:** So we're at the stage where hopefully the CVE pages get launched soon. That project is now in the hands of the web team.

**Aida Knezevic:** These meetings will mostly focus on content production and the broader content strategy for the Cybersecurity 101 blog. If you have any ideas for content or areas you want us to focus on, let us know.

**Ankit Pahuja:** Right now we're focusing on ideation and keyword research for the upcoming weeks. When you say keyword research—is that specific to CS 101, the CVE database, or just in general?

**Aida Knezevic:** CS 101—that's what we've been focusing on. But do you have any additional needs?

**Ankit Pahuja:** No, I think that should be good.

**Ankit Pahuja:** What we haven't discussed is the CVE database—specifically what pages we'll create. When we scope this, we're thinking about vulnerabilities from 2020 to 2025, which would be almost 5,000 CVEs or more. The questions we need to answer are: What's the total volume we're looking at? What does the first batch look like? What's the timeline for the complete rollout? We should find answers to these questions so we're in sync with the development.

**Ankit Pahuja:** So when we really want to launch, we know our strategy.

**Aida Knezevic:** That's a good call-out. When we publish pages programmatically, we can do scale, but we don't want to publish at such a high volume that we hurt your SEO. There have been websites that published lots of programmatic content, got traffic, and then Google penalized them. I'll check with our managing director on best practices.

**Aida Knezevic:** I was thinking maybe publishing about 100 a week would be realistic and feasible, but I'll check with the team to make sure we hit the right number. I don't want us to publish too much too quickly.

**Aida Knezevic:** My idea is to start with 2025—the most recent CVEs—and work our way backwards to 2020. That's totally fine. I can pull a list of keywords from SEMrush for CVEs by year—they all start with CVE-year, so it's easy to filter. That's how we'll build the CVE content calendar.

**Ankit Pahuja:** So when you say CVE content calendar, we're talking about individual readable pages, right?

**Aida Knezevic:** Yes, exactly. For CVE 2025, we have close to 2,600 keywords just for that year. There will be duplicates, but we can filter those out pretty easily. We'll export the keyword list, remove duplicates, and use that for the first round of publishing.

**Aida Knezevic:** In terms of the timeline, I'll talk to Sydney and Marisol on our end and give you a better outlook on content generation and cadence. But for launching, we also need to align with the dev team to see how that's progressing and how quickly everything can be integrated into your content stack.

**Ankit Pahuja:** Yep, sounds good. Given that these will be generated with your software and the workflow you created for the database to populate and generate content, I'm looking for visibility into our strategy, what to expect, and the timelines.

**Aida Knezevic:** For sure. I'll sync with Sydney when she's back tomorrow and Marisol to get clarity. Marisol actually started generating some CVE content ahead of time to test the pipeline. I'll double-check how that's progressing—we might already have a backlog of CVE pages.

**Ankit Pahuja:** I'm being asked about the go-live date. We need to check internally and have at least a week-level go-live target so we know when we'll launch the database.

**Aida Knezevic:** I'll message Nicholas before his meeting with your team to get projections on when we could go live with the CVE pages. Then we can give you an idea of which week.

**Ankit Pahuja:** Yeah, just drop him a message beforehand so he's thinking about that timing.

**Aida Knezevic:** Yes, I'll draft that now.

**Ankit Pahuja:** I have a quick question for Georgemaine. I'm looking at your message from this week where you asked Christian to respond.

**Georgemaine Lourens:** Is that all you need from him?

**Georgemaine Lourens:** I wouldn't prioritize these colors too much—they're one of those things you can always change in production.

**Ankit Pahuja:** Yeah, I think the same. I've asked the team to get us their feedback. Drew, our VP of Brand, has already looked at those and given feedback. I think we're just waiting on one final piece from him. It should just be small changes, so we can start with dev.

**Georgemaine Lourens:** That was my takeaway too. Let's just start development and tackle responsive design as we go.

**Ankit Pahuja:** So would dev need responsive designs before starting, or can they begin with components and add mobile designs later?

**Georgemaine Lourens:** I'd have to check with Nicholas, but I assume we can start with the components and build the desktop experience first. Then we fit it for mobile based on the website's existing breakpoints.

**Ankit Pahuja:** As next steps, let's get the web team started. We're meeting today between the two web teams, so they can get going. Nicholas can come prepared with what he needs from SentinelOne's web team, and we're happy to help however we can.

**Aida Knezevic:** We're pretty flexible. Whatever timeline the dev team comes back with—whether it's three weeks or whatever—we'll adapt. We're happy to accommodate the plan Nicholas and your team come up with.

**Ankit Pahuja:** From what I'm hearing, mid-October is our target go-live date. We don't have a specific date in mind yet—let the dev teams decide, and they'll set the week or date for launch. Mid-October is important because this is a critical project for both the brand and SEO teams. We're aiming to generate significant traffic from it, so sooner we go live, the better.

**Aida Knezevic:** Totally understand that. Anything else?

**Ankit Pahuja:** I think that's all.

**Aida Knezevic:** Nothing else from me either. I'll follow up on Slack with notes and action items, sync with Sydney and Marisol when they're back, and come up with a content plan for the CVE pages. I'll keep in touch with Nicholas about how the meeting goes.

**Ankit Pahuja:** Thank you.

**Aida Knezevic:** Thank you. See you next week.

**Ankit Pahuja:** Bye.
