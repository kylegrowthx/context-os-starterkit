# SentinelOne <> Growth X - Weekly Sync

<metadata>
date: 2025-10-16
time: 14:01 UTC
duration: 20 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Ankit Pahuja, Katya Luscomb, Mansi Bhalothia, Marcus Derencius
fathom_recording_id: 94638971
fathom_url: https://fathom.video/calls/441982298
share_url: https://fathom.video/share/Vs3ug9smRz6WTBtNsJqXxavu1r4ndSzu
source: fathom
enriched_on: 2026-03-02 02:45 UTC
</metadata>

---

## Summary

SentinelOne and GrowthX reviewed the CVE vulnerability database launch timeline, with 800 articles generated and loaded in Atlas, waiting for a ContentStack management token and GitHub access to unblock backend integration and frontend testing. GrowthX is shipping 5 content pieces by Friday with 5 more assignments queued, while Mansi's team has 9 articles ready to publish and is refining content per PMM feedback from Cameron (cloud security) and Jeremy (threat intelligence, AI). Early performance data shows strong LLM visibility — the three published blogs generated ~150 sessions with ChatGPT referrals particularly strong for cybersecurity 101 content, which hasn't experienced the August drop-off other competitors saw.

---

## Context

SentinelOne, a cybersecurity company, is an active GrowthX client working on a major content initiative focused on CVE (Common Vulnerabilities and Exposures) vulnerability education and SEO visibility. GrowthX is running their content delivery side (copywriting, content strategy, optimization), while SentinelOne's internal team (Ankit, Mansi, and stakeholders) handles product integration, design, and publishing. The relationship is 3-4 months in (based on reference to "last week's strategy" and ongoing weekly syncs), and this is a high-volume content play — the team is targeting publication of many "cybersecurity 101" educational pieces by quarter-end to capitalize on LLM visibility through ChatGPT and Perplexity. The meeting happened to unblock technical integration work (ContentStack management token, GitHub access) that's delaying the CVE database launch.

---

## Relevance

**To GrowthX Delivery:**
- Content pipeline feedback: Adding specific SentinelOne product offerings and more relevant conclusions to each blog piece to improve CTR and engagement. Cameron and Jeremy (Mansi's PMMs) are guiding cloud security and threat intelligence verticals.
- Volume cadence: 5 pieces/week is shipping on schedule; 9 articles already queued for publishing. Team is tracking weekly assignment pipeline to extend runway between meetings.
- Integration dependencies: Cannot finalize release timeline until Marcus gets ContentStack management token and GitHub access — creating integration bottleneck.

**To CheckThat:**
- LLM visibility evidence: ChatGPT referrals strong and steady despite August algorithmic shift that hit competitors. Cybersecurity 101 foundational content is winning in LLM search results (featured in responses).
- Perplexity growth: Organic LLM referral growth from Perplexity is consistent — indicates broad AI visibility across multiple LLM platforms, not just ChatGPT.
- SEO schema execution: Ankit is pushing structured data (schema) implementation on CVE hub and details pages by end of week. Marcus will build conditional logic to only show related CVEs section if 3+ entries available.

**To GrowthX Business Development:**
- Account health signal: SentinelOne is shipping aggressively (800 CVEs loaded, 5/week content, Q4 push) — indicates confidence in content ROI and partnership momentum.
- Renewal/expansion potential: Client is adding new feature requests (related CVEs section, schema improvements) mid-project, suggesting satisfaction and willingness to invest more.

---

## Overview

- CVE database frontend is ready for testing, but backend integration is pending due to access token issues
- 800 CVE articles have been generated and are ready for deployment once the system is set up
- 5 new content pieces will be ready by Friday, with 5 more assignments for next week
- LLM referrals, particularly from ChatGPT, remain steady for SentinelOne, with cybersecurity 101 content performing well

---

## Key Topics

### CVE Vulnerability Database Progress

  - Frontend is ready for testing, needs design refinement
  - Backend integration pending due to lack of management token for ContentStack
  - Marcus awaiting GitHub access for website work
  - 800 CVE articles generated and loaded in Atlas platform, ready for push
  - New feature request: Add related CVEs/technology section to individual CVE pages
  - Schema implementation for SEO structure data on CVE hub and details pages forthcoming

### Content Updates and Review Process

  - 5 new content pieces ready by Friday, 5 more assignments for next week
  - 9 articles ready to go live
  - Content review process ongoing, with specific PMM input for cloud security and threat intelligence
  - Adjustments to content structure: adding product offering specifications and more relevant conclusions

### Performance Metrics

  - 3 published blogs received \~150 sessions across all search channels
  - Organic search performance varies: AI threat landscape blogs ranking on page 1, others on page 2
  - LLM referrals remain steady, unlike some competitors who saw drops
  - ChatGPT referrals strong, particularly for cybersecurity 101 content
  - Perplexity referrals growing steadily

### UI and Feature Updates

  - New related CVEs/technology section to be added to individual CVE pages
  - Logic to be implemented: only show related section if 3+ entries available

---

## Action Items

**Ankit Pahuja (SentinelOne)**
- Send schema types and implementations for CVE hub and details pages to dev team by end of week

**Aida Knezevic (GrowthX)**
- Tag George Main in internal channel re Ankit's UI change comment on Figma file

**Marcus Derencius (GrowthX)**
- Implement logic for related CVEs section to only display if 3+ entries available

---

## Transcript
**Katya Luscomb:** Morning, everyone.

**Katya Luscomb:** This meeting is being recorded.

**Katya Luscomb:** Most of you.

**Katya Luscomb:** Ada, can you lead the bit on reporting on their traffic that you had added?

**Katya Luscomb:** I would just love to see how you frame it.

**Aida Knezevic:** It'd be super helpful.

**Aida Knezevic:** Yeah, I mean, it's not like a huge update because we haven't published a whole lot.

**Katya Luscomb:** Yeah, there's only those three.


**Ankit Pahuja:** Hey, I was in another meeting that just took a while.

**Ankit Pahuja:** How's it going?

**Aida Knezevic:** Good.

**Aida Knezevic:** How are you?

**Ankit Pahuja:** I'm good.

**Aida Knezevic:** Okay.

**Aida Knezevic:** I'm going to share my screen.

**Aida Knezevic:** So I wanted to just dive in.

**Aida Knezevic:** Unless, Ankit, you have any updates on your end?

**Aida Knezevic:** We could just dive into the CVE vulnerability updates.

**Aida Knezevic:** All right.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** So the update is that we have a pipeline hooked up to ContentStack, the temporary instance.

**Aida Knezevic:** Marcus, do you have any, since yesterday, has anything changed?

**Marcus Derencius:** Do you have access to the stuff that you need?

**Marcus Derencius:** No, not yet.

**Marcus Derencius:** I was with Nico.

**Marcus Derencius:** was trying to create, set up the content, the SentinelOne ContentStack instance.

**Marcus Derencius:** So I could set up.

**Marcus Derencius:** But I still...

**Marcus Derencius:** They don't have the token to insert the content in there.

**Marcus Derencius:** So it is kind of ready.

**Marcus Derencius:** So I still don't have the access.

**Marcus Derencius:** I can read content from the production content stack, but I cannot insert.

**Marcus Derencius:** So that's the management token.

**Marcus Derencius:** That's, yeah, that would be helpful to get that.

**Marcus Derencius:** And meanwhile, I just got a message that they are working on my GitHub account so I can access and try to work on the website site.

**Marcus Derencius:** So there's still no news.

**Aida Knezevic:** OK.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** Yeah, for a reason, I know it's quite a process to onboard to the tech stack.

**Ankit Pahuja:** It takes a week or more sometimes, even longer.

**Ankit Pahuja:** But I'd suggest either when you put a kind of an update or just follow up with you.

**Ankit Pahuja:** I think he's the best person to get this quickly, and he's already on it, so I think just a nudge would do.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** All right, so Marcus, you're meeting this week with the SentinelOne web team, right?

**Aida Knezevic:** Is that meeting, was it yesterday?

**Marcus Derencius:** I sent them, it was not a proper meeting, I was just sending a message to them on Slack, they said they were checking, but not a proper meeting.

**Aida Knezevic:** Ah, okay, okay, got it, yeah.

**Aida Knezevic:** All right, well, yeah, I mean, feel free to kind of nudge them, follow up with them, just to make sure that we get you the access.

**Marcus Derencius:** Yeah, just this management, not just this, this management token is not.

**Marcus Derencius:** Associate to my account on ContentStacks, so maybe we can try to get someone to get the talking, inserting their content in there, and then, yeah, it should speed things a little bit.

**Aida Knezevic:** Ah, okay, okay.

**Ankit Pahuja:** On an additional note, I see Nicolas had said that meeting, it was until the two, three weeks, so probably this week that meeting wasn't scheduled, so I think possibly the reason Marcus didn't meet the team.

**Ankit Pahuja:** So, you probably would want to say that again.

**Aida Knezevic:** Oh, yeah, yeah, yeah, you are correct, yeah, yeah, I can set something up again with the team.

**Aida Knezevic:** Okay, good.

**Aida Knezevic:** I did put together kind of like a release timeline plan that I shared, but I think until Marcus gets the token, it's just hard to make any predictions on the timeline.

**Aida Knezevic:** So, as soon as he gets the token, I'll...

**Aida Knezevic:** Like, sync with Marcus and try to provide you with, like, specific dates.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** A quick question, Marcus.

**Ankit Pahuja:** So do we have the frontend ready, backend ready?

**Ankit Pahuja:** It's just the migration bit to our system?

**Marcus Derencius:** Yeah.

**Marcus Derencius:** The frontend, we need to refine, like, do a pass on the design.

**Marcus Derencius:** So it's, I can share the temporary URL so you can start playing with it.

**Marcus Derencius:** But still need refining on the looks.

**Marcus Derencius:** But in the future, we can start testing.

**Marcus Derencius:** So I'll share that.

**Ankit Pahuja:** Okay.

**Ankit Pahuja:** Got it.

**Ankit Pahuja:** Sorry.

**Aida Knezevic:** Okay.

**Aida Knezevic:** And we've already, I mean, in the, in our Atlas platform, we've already started, like, generating all of the content.

**Aida Knezevic:** So we've just loaded it up.

**Aida Knezevic:** So once it's ready to go, we can just push.

**Aida Knezevic:** We don't have to wait for

**Aida Knezevic:** For us to generate, we've tested, we started testing it last week and there we discovered some bugs that we've been, like, we were able to fix on time.

**Aida Knezevic:** So I don't think there should be, like, any surprises on that end.

**Ankit Pahuja:** All right.

**Ankit Pahuja:** So when you say content's loaded, that's loaded for the scope.

**Ankit Pahuja:** decided for upwards of 500 or so articles that we discussed?

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** think it was, Katya, I think it was, like, 800 CVEs, right?

**Katya Luscomb:** Yeah, we looked at that list on Kit that you sent with the volume and the recency, and we aligned our database in Airtable with your content and then polled based on that strategy that you shared last week.

**Ankit Pahuja:** That was good.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** Marcus, do you have any other updates, anything else you want to share on the CVE stuff?


**Marcus Derencius:** I'll just share the site, so we can start looking and refining, and then, yeah, just play with that, give feedback, so we can fix any major UI design issue.

**Marcus Derencius:** So, yeah, that'll be the next, like, I'll just update the last version, release it for the last adjust, then we can start playing.

**Ankit Pahuja:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Cool.

**Aida Knezevic:** So, Katya, did you want to go over the content updates?

**Katya Luscomb:** Yeah, just real quick.

**Katya Luscomb:** We have, as noted in there, we've got five pieces of content that we're prepping this week, those will be ready for you by Friday, and we have five more assignments that are ready for next week.

**Katya Luscomb:** I did want to check on the assignments in our Airtable that we sent over.

**Katya Luscomb:** There's a handful in there that looks like maybe haven't been reviewed, but I wanted to make sure that you're all still looking those over, and I don't need to just archive them for my planning. I keep working on building out some of those assignments as well, so that we get some longer runway between these meetings in the future.

**Mansi Bhalothia:** That's great.

**Mansi Bhalothia:** The articles that you sent last week are still in the process of being reviewed.

**Mansi Bhalothia:** We will have them ready by, I think, today or tomorrow max.

**Mansi Bhalothia:** Apart from that, there are nine articles that are ready to go live.

**Mansi Bhalothia:** And we also have the topic of approvals for the next section, which is done.

**Katya Luscomb:** Okay. And I was noticing, I was snooping around a little bit in some of the articles that I think you had made some edits to last week.

**Katya Luscomb:** And it looks like you're adding some more specifications.

**Katya Luscomb:** In terms of what SentinelOne product offerings are, and a brief or more specific conclusion relevant to the content of the blog, we can refine our pipeline so that those components are in there.

**Katya Luscomb:** I just wanted to make sure that that was sort of consistent with the content that you guys were really wanting to produce and align with so that we can adjust.

**Mansi Bhalothia:** That's correct.

**Mansi Bhalothia:** So I did resolve Cameron's comment, but in the comment section, you can go through his comments.

**Mansi Bhalothia:** So Cameron is specifically for cloud security data, and there's one more PMM, Jeremy.

**Mansi Bhalothia:** He's working with threat intelligence, AI, and other sets.

**Mansi Bhalothia:** So I did resolve his comments as well.

**Katya Luscomb:** Perfect.

**Katya Luscomb:** Yeah.

**Katya Luscomb:** I'll make sure to look through those, and I was looking through them last week a little bit as well.

**Mansi Bhalothia:** Yeah, for your reference, if you want to go back, I just highlight it in yellow so that you can just go back and see.

**Katya Luscomb:** Yeah, saw those highlights, and that's kind of where my ideas were coming from in our adjustment.

**Katya Luscomb:** So, yeah, perfect, helpful.

**Katya Luscomb:** That is, that's everything from my end for this week.

**Ankit Pahuja:** Cool.

**Ankit Pahuja:** I have a quick addition for CVE database.

**Ankit Pahuja:** I just made a comment on individual CVE pages.

**Ankit Pahuja:** That's towards the end of the page where the idea is to have related CVEs or related technology section, which kind of lists related CVEs to this particular vulnerability that we are on, like the user is on while they're reading.

**Ankit Pahuja:** It is to enhance internal linking.

**Ankit Pahuja:** So that came as a suggestion from one of the teammates while they were reviewing it for SEO.

**Ankit Pahuja:** I've tagged George.

**Ankit Pahuja:** You should be able to take that up.

**Ankit Pahuja:** Also sharing here so that Marcus can have that in plan while that's being built.

**Marcus Derencius:** How do we get the related CVEs? I don't remember.

**Ankit Pahuja:** There's a technology field for that.

**Ankit Pahuja:** OK.

**Ankit Pahuja:** And on the pages implementation side, I think that's more on the dev side of work, nothing to do with design. We built a list of schema that we want to implement on both the CVE hub page and the CVE details page. So we'll share schema types and implementations that would be inside the head tag — some SEO structured data for each page. We've documented it and will send it over so that you could include it in the templates. I'll send that over probably before end of this week so that it can be included in the scope.

**Ankit Pahuja:** But yeah, no more changes. I've had this reviewed with other folks in the company and this should just go live.

**Aida Knezevic:** Okay, that's good.

**Aida Knezevic:** All right.

**Aida Knezevic:** So I just wanted to give you just a quick performance update on the three blogs that we've published so far.

**Aida Knezevic:** So it sounds like we're going to be publishing a lot more this week, but I still wanted to kind of show you in our looker performance report.

**Aida Knezevic:** So, so far from the three blogs that we've published, the search data is from Google Analytics 4, which includes all search channels, not just organic, but also referral and direct traffic.

**Aida Knezevic:** So the blog so far have received almost 150 sessions.

**Aida Knezevic:** And if you want to look at just organic search traffic, this is the table from Google Search Console. You can see the three clusters that the blogs belong to here.

**Aida Knezevic:** So there's foundational AI cybersecurity knowledge, AI threat landscape, and defensive innovation.

**Aida Knezevic:** And you can see like how many URL clicks each of the published blogs have received so far.

**Aida Knezevic:** The two in the AI threat landscapes have a pretty high average position so far.

**Aida Knezevic:** So it seems like they're on page one for the keywords that they're ranking.

**Aida Knezevic:** The other one seems to be on page two on average, but yeah, hopefully, you know, once we start, like, scaling publishing this week, we're just going to be seeing, like, additional growth here.

**Aida Knezevic:** And then, to take a really quick look at the LLM referral breakdown, sorry, it's a little slow.

**Aida Knezevic:** Looker is not the fastest data dashboard.

**Ankit Pahuja:** Yeah, I was saying that Looker actually launched a premium plan.

**Ankit Pahuja:** Looks like Google wants to make money everywhere.

**Aida Knezevic:** That's news to me, but not surprising. I also saw that ChatGPT is considering adding ads — they recently hired an ad specialist.

**Aida Knezevic:** I just wanted to give you a quick LLM referral breakdown. Over the past couple of months, it seems to be pretty steady. There are some websites that saw a big drop-off in LLM referrals and specifically ChatGPT referrals around August because ChatGPT started favoring more answer-rich websites like Wikipedia when answering informational queries. However, it doesn't appear to have dramatically impacted your website — there was only a slight decrease in August and then you continued moving up. I think the strength of your brand plays a big role in your LLM referrals, which is why it hasn't gone down dramatically.

**Aida Knezevic:** And other referrals like from Perplexity have also been growing at a pretty steady rate.

**Aida Knezevic:** And you're also, I want to like point out that the landing pages that are getting a lot of traffic from ChatGPT include cybersecurity one-on-one content.

**Aida Knezevic:** So it's being picked up by LLMs and it's clear that it provides like enough information to be seen as more valuable than websites that are like Wikipedia that contain information about everything.

**Aida Knezevic:** So I think that's pretty great.

**Aida Knezevic:** And it's something that like I would, you know, it's like a testament that the cybersecurity one-on-one idea was a really good idea on your team's part.

**Aida Knezevic:** Just in terms of, like, improving your LLM visibility.

**Ankit Pahuja:** I mean, a lot of this here is just, like, cybersecurity one-on-one content, which is pretty great.

**Ankit Pahuja:** Could you share this report with us?

**Aida Knezevic:** You should have access via your email, but I'll drop a link in the channel. Let me check who else needs access. Okay, so you have access — I'll make sure Mansi has editing access as well.

**Aida Knezevic:** I'll give you editing access, so you can kind of play around with the data.

**Ankit Pahuja:** Okay, cool.

**Aida Knezevic:** I think those are all the updates that we had.

**Aida Knezevic:** Do you have any other questions or anything else that we can help you with this week?

**Ankit Pahuja:** I think, no, just wanted to make sure and also bring to light the two things that we have for vulnerability database.

**Ankit Pahuja:** Two things for the vulnerability database: one around UI change and feature addition, and second being schema implementation before we go live.

**Ankit Pahuja:** That's it.

**Ankit Pahuja:** Myself and Mansi, were estimating number of pages we look forward to publishing with GrowthX this month as a part of ending the quarter.

**Ankit Pahuja:** She had numbers and she forecasted a pipe given our weekly number that we do.

**Ankit Pahuja:** So, yeah, I'm just looking forward to publishing those many pages on CS101 as well.

**Aida Knezevic:** Awesome.

**Aida Knezevic:** Yeah, same here.

**Aida Knezevic:** I will tag George Main in our internal channel just to make sure that he sees your comment on the Figma file.

**Aida Knezevic:** And yeah, Marcus, you can also keep that in mind for the design of the webpage.

**Ankit Pahuja:** Yeah, just last thing, Marcus, while you build that up, right, so given we are launching...

**Ankit Pahuja:** Vulnerability Database with 800 of those and will gradually build up content.

**Ankit Pahuja:** So related section, if you could put a logic there, if there are three entries or more, then only that table shows up because we don't want to end up showing an empty table there.

**Ankit Pahuja:** So that's just some logic you might want to build with.

**Aida Knezevic:** OK, cool.

**Aida Knezevic:** All right.

**Aida Knezevic:** Well, I'll keep in touch these next couple of days.

**Aida Knezevic:** I'll keep you posted as soon as we have any updates.

**Ankit Pahuja:** I'll let you know.

**Ankit Pahuja:** But thank you.

**Ankit Pahuja:** All right.

**Aida Knezevic:** Thanks.

**Aida Knezevic:** Thank you.

**Katya Luscomb:** See you next week.

**Katya Luscomb:** Have a good one.
