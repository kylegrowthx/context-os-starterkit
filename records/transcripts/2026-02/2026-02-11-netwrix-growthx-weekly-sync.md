# Netwrix <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-11
time: 16:00 UTC
duration: 38 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic (GrowthX), Mariel Grinstein (Netwrix), Philipp Denisenko (Netwrix), John Knightly (Netwrix), Ani Grigoryan (Netwrix), James Levin (Netwrix), Ralph Marino (Netwrix), Chanel Chambers (Netwrix), William Leborgne (GrowthX), Kathy Lam (GrowthX)
fathom_recording_id: 121587967
fathom_url: https://fathom.video/calls/563227926
share_url: https://fathom.video/share/7AD6sRKeXmK5ojFU7W8oQwik1BcdqRjA
source: fathom
enriched_on: 2026-03-01 00:00 UTC
speaker_note: "Netwrix SEO" speaker labels refer to Ralph Marino (Netwrix's VP of SEO); mapped based on context and action item assignments.
</metadata>

---

## Summary

Sync on content strategy, audit findings, and publishing blockers.

---

## Context

Netwrix, a cybersecurity and IT visibility company, is a significant GrowthX client. This is a weekly operational sync between Netwrix's marketing team (led by Mariel Grinstein, with Philipp Denisenko leading strategy and Ralph Marino overseeing SEO) and GrowthX's delivery team (Aida Knezevic leading the engagement). The meeting focuses on content strategy execution, CMS challenges, and content performance metrics. Netwrix has contracted GrowthX to execute a comprehensive content refresh and expansion program targeting high-impact blog articles and PDF guides, with emphasis on SEO performance, lead quality, and pipeline impact.

---

## Relevance

**To GrowthX Delivery:**
- Sanity CMS setup limitations are blocking efficient content publishing; publishing failures and language redirect bugs require web dev escalation. GrowthX's auto-publishing integration (Atlas → Sanity) is critical to solve these workflow friction points.
- Headless CMS complexity requires careful component mapping — Tanmay's work to integrate Atlas with Sanity's component structure is essential for scalable content production.
- Content audit methodology (combining GSC organic traffic data with MQL/AQL pipeline impact) is a replicable, data-driven approach that can be applied to other client engagements.
- Shift toward real author bylines (E-E-A-T compliance) is becoming a hard requirement across clients; Dirk serving as author for 2 new articles sets a precedent.

**To GrowthX Business Development:**
- Netwrix is scaling content operations from weekly syncs to 6-week production plans — expansion signal suggesting growth in engagement scope and potential for additional work.
- P1 refresh list (40 high-impact articles) plus 4 new articles this week demonstrates strong execution velocity, supporting account health and renewal confidence.
- Ungate PDF strategy signals strategic shift from lead volume to lead quality — indicates Netwrix is optimizing funnel conversion and may expand performance expectations in next planning cycle.
- Client is experiencing real publishing blockers and manual CMS friction; GrowthX's forward-deployed engineer and auto-publishing roadmap addresses critical pain point and differentiates service delivery.

---

## Overview

- **Content Audit Delivered:** A new audit prioritizes 40 P1 articles for refresh based on pipeline impact (MQLs, AQLs), with GrowthX owning the work.
- **Sanity CMS Blockers:** Critical bugs are preventing content updates from publishing and auto-redirecting users to foreign language sites, risking high bounce rates.
- **Gated Content Strategy Shift:** All gated guides will be ungated to improve lead quality over quantity, with exceptions for high-ranking content.
- **Publishing Pipeline:** GrowthX will deliver 6 articles this week (2 new, 4 in progress) to accelerate content indexing and traffic generation.

---

## Key Topics

### Sanity CMS Blockers

  - **Publishing Failure:** A recent content refresh failed to publish, and the Sanity document history shows no record of the update.
  - **Language Redirect Bug:** Users are being auto-redirected to German/Portuguese sites, risking high bounce rates.
      - **Cause:** Suspected backend cache issue, not user error.
      - **Action:** Mariel will create a web dev request to investigate.
  - **Usability Issues:** The CMS is difficult for marketers to use due to poor search and a rigid component structure that requires web dev requests for simple elements like tables.

### Content Audit & Refresh Strategy

  - **Audit Methodology:** Analyzed \>500 URLs from GSC, combining organic traffic data with Netwrix pipeline data (MQLs, AQLs) to create an "opportunity score."
  - **Priority Tiers:**
      - **P1 (40 articles):** High pipeline impact → Full refresh.
      - **P2:** Update title/meta description → Monitor rankings.
      - **P3–P5:** Low-impact content → Lower priority.
  - **Ownership:**
      - **GrowthX:** Owns all P1 refreshes.
      - **Netwrix:** Can handle P2 metadata updates.

### Content Calendar & Production

  - **Calendar Refinement:** The Airtable calendar is now clean of duplicates and will be updated with Dirk's topic suggestions.
  - **New Column:** A "Funnel Stage" column will be added to ensure a focus on Bottom/Middle of Funnel topics.
  - **6-Week Plan:** Aida will create a 6-week production plan based on the finalized calendar.
  - **Authoring:**
      - **Requirement:** Use real authors to meet Google E-E-A-T guidelines.
      - **Plan:** Use Dirk as the author for the 2 new articles, pending his approval.
      - **Fallback:** A "Netwrix Team" placeholder can be used temporarily for publishing speed.

### Gated Content Strategy

  - **Decision:** Ungate all PDF guides to improve lead quality, accepting a temporary drop in lead volume.
  - **Exceptions:** High-ranking blog posts will remain gated.
      - **Rationale:** Don't "fix what's not broken."
      - **Action:** Add more CTAs (e.g., after intro, mid-page) to these posts to capture more leads.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Merge P1 refreshes into Airtable calendar; tag as refreshes
- Send audit methodology + Philipp's URL/AQL/MQL sheet to Ani Grigoryan
- Consult Sydney re: metadata updates; align with Ralph Marino
- Stage 2 new articles in Sanity; ping Dirk for authorship; publish on approval
- Add funnel stage column to content calendar
- Add Dirk's requested topics to content calendar
- Tag Mariel Grinstein in Slack re: 2 Apr topics GrowthX can take
- Draft 6-week content plan for Dirk
- Email Philipp re: un-gating PDFs; note AQL impact
- Mark gated guides to keep gated; share with Philipp; then Philipp analyze conversion

**Mariel Grinstein (Netwrix)**
- Create Asana web request to web dev re: Sanity language/cache issue
- Cancel duplicate meeting invite

---

## Transcript
**Aida Knezevic:** Good, how are you?

**Ralph Marino:** Yeah, good.

**Aida Knezevic:** Hello, Philip.

**Philipp Denisenko:** This meeting is being recorded.

**Philipp Denisenko:** Hey, Rolf.

**Ralph Marino:** Hello.

**Aida Knezevic:** Alright, I hope the change of meeting times is okay for everyone.

**Aida Knezevic:** I didn't get any messages about anybody else not being able to attend, so hopefully we'll have everyone on the call that we need.

**Philipp Denisenko:** Did you sync with John, Chanel, and James?

**Philipp Denisenko:** Because usually their schedules are the most packed ones.

**Philipp Denisenko:** And like last time when I tried to schedule the, you know, common call, it was quite challenging.

**Philipp Denisenko:** So I would rather, you know, check with them first, because, you know, I can be flexible.

**Philipp Denisenko:** But, yeah.

**Philipp Denisenko:** Oh, you know, we can...

**Philipp Denisenko:** I'll just check their availability basically through Outlook.

**Philipp Denisenko:** And if it doesn't work usually, because they're all ENDSCO this week, if it's not going to work next week, I'm going to kind of, you know, propose.

**Ralph Marino:** That's essentially what I did, Phil. I was looking at the Outlook calendar and trying to coordinate with Aida.

**Ralph Marino:** But yeah, there's always like some kind of discrepancy or somebody not available. It was very tough.

**Philipp Denisenko:** So was it green for everyone, Rolf?

**Ralph Marino:** Everyone except John Knightley.

**Ralph Marino:** So I threw that in the team's chat to just see if he would be available moving forward. It looked like everyone but John Knightley.

**Philipp Denisenko:** Okay, so yeah, let's see what he replies then.

**Philipp Denisenko:** Okay, cool.

**Aida Knezevic:** All right, let me share my screen and we can get started.

**Aida Knezevic:** Combined all of the insights into one spreadsheet and then categorized refreshes into different priorities.

**Aida Knezevic:** So the top priority ones are the ones that had a high impact on pipeline and just refreshing them would give them an even bigger boost.

**Aida Knezevic:** The second priority refreshes are articles where we might just need to update the title and the meta description.

**Aida Knezevic:** And then you can monitor how like their rankings afterwards.

**Aida Knezevic:** And if it turns out that just the title change doesn't result in a better position, then it might also require like a content update.

**Aida Knezevic:** And then P3, 4, and 5 are lower priority refreshes.

**Aida Knezevic:** P3 is older content that doesn't have a lot of impressions or clicks and hasn't had a lot of impact on revenue or opportunity.

**Aida Knezevic:** So if you go to the content audit, you can see a breakdown of all the different URLs.

**Aida Knezevic:** And you also have, you can see the opportunity score, meaning you have like demand generators, opportunity creators, revenue drivers.

**Aida Knezevic:** Those are like the top three categories based on the data that Philip shared.

**Aida Knezevic:** And then each tab has the appropriate URLs.

**Aida Knezevic:** Any questions?

**Aida Knezevic:** I mean, you know, if you have like, if you take a look at this later and have any questions, feel free to just drop them in the Notion doc and we'll follow up.

**John Knightly:** No pressure to review this now.

**John Knightly:** Sorry, Aida, John just got in late.

**John Knightly:** So the idea is we go ahead and do these updates automatically, or you wanted us to review them one by one? What's the ask?

**Aida Knezevic:** So you don't really need to review them.

**Aida Knezevic:** I'm happy if the team wants to go through, but what we can do is in Phase 2, we can prioritize these P1 refreshes alongside creating Netnew content.

**Aida Knezevic:** So, for example, each week we could refresh one or two articles from the priority refresh list.

**Aida Knezevic:** Because you already have a content team internally, and I'm sure that they already kind of are working on some content refreshes, they can also use this spreadsheet to just organize and prioritize the content refreshes.

**Aida Knezevic:** But again, I just wanted to share this with you so you have insight into the methodology and the data, but this is for us to understand how we're going to prioritize things, because there's a lot of content.

**Aida Knezevic:** So we want to make sure we're focusing on the revenue.

**John Knightly:** New drivers.

**John Knightly:** Makes sense.

**Philipp Denisenko:** So by the way, based this, you're going to create some sort of a calendar of the content update, right?

**Aida Knezevic:** Yeah, exactly.

**Aida Knezevic:** So we are going to merge this in Airtable.

**Aida Knezevic:** So everything is in one place.

**Aida Knezevic:** And so basically the priority refreshes will move them to our Airtable content calendar.

**Aida Knezevic:** We'll tag them as refreshes so that we know that it's not new content.

**Aida Knezevic:** And then it's just production as usual.

**Philipp Denisenko:** Wondering since, you know, having a fresh content or a recency factor is a huge one these days.

**Philipp Denisenko:** Wondering which portion of the whole bulk will you be able to take care of?

**Philipp Denisenko:** And then, you know, I'm not, I'm quite sure it's not like 100% of it, right?

**Philipp Denisenko:** So...

**Philipp Denisenko:** Wondering.

**Philipp Denisenko:** So then there comes a question, like, how do we divide and conquer here?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So we're happy to just take care of the P1 refreshes.

**Aida Knezevic:** There are 40 topics here.

**Aida Knezevic:** So that's certainly doable for us.

**Aida Knezevic:** And there's, you know, articles here that go back to like 2023.

**Aida Knezevic:** So they're quite old.

**Aida Knezevic:** So we're happy to do the P1.

**Aida Knezevic:** And then if you want, you can like focus on like, this is like lower lift of just updating metadata that would just require you to go into CMS and change the title based on what's already ranking in the SERP.

**Aida Knezevic:** All right.

**Ani Grigoryan:** Great.

**Aida Knezevic:** One more question.

**Ani Grigoryan:** Can you please tell how did you choose this blog post like to include exactly these ones?

**Aida Knezevic:** So there's a methodology. I'll send it over. It's in Notion.

**Aida Knezevic:** So we basically exported everything that's in Google Search Console.

**Aida Knezevic:** So there are over 500 URLs that we found in Google Search Console from the blog and resources pages. We're looking at organic traffic data from Google Search Console, and we combine that with the spreadsheet that Philipp shared that contains data around MQLs and lead opportunities created.

**Aida Knezevic:** So there are different, I can share that as well, just so you can see what was the data we were working off of.

**Aida Knezevic:** You can find it here — if you scroll all the way to the right, you'll see the spreadsheet that Philipp shared with all the URLs and the AQLs and MQLs.

**Mariel Grinstein:** Hey, how are you? I'm wondering — when we launched the new website, we did the same exercise.

**Mariel Grinstein:** So Ralph, are we okay to change metadata again?

**Ralph Marino:** Yeah, I guess on a case-by-case basis. I don't know if we necessarily need to, but I'm always open to proposed updates and maybe having a discussion around it.

**Aida Knezevic:** Okay. If that happened, let me take this back to Sydney, who worked on the audit, and I'll let her know.

**Mariel Grinstein:** So you updated all of the metadata for the content?

**Mariel Grinstein:** Yeah, for all the blogs that were getting AQLs, for all the blogs that were getting pipeline, for all the MRPs, and the main resources pages like e-books. We also got the ones getting pipeline.

**Mariel Grinstein:** And we also took all the queries that were ranking lower than position 10 and updated metadata for them. That was just in October, about three months ago.

**Philipp Denisenko:** So the question is, how often do we need to do this? What's the ideal frequency?

**Aida Knezevic:** Typically, you check on performance maybe every four to five months.

**Aida Knezevic:** There was a Google Core update in December that shook up a lot of websites, so there could have been changes that happened then. I checked it from my browser and one of our teammates did too.

**Aida Knezevic:** So the article is still not updated — the date is old and the content is still the old version of the blog post. We tried to publish it again and it hasn't had an effect.

**Mariel Grinstein:** That's weird.

**Mariel Grinstein:** Yesterday, there was something happening with Sunny Day because I had an issue.

**Mariel Grinstein:** Okay.

**Mariel Grinstein:** Yeah, it's the same thing that I published stuff and it didn't happen.

**Aida Knezevic:** So let me check again.

**Aida Knezevic:** Oh, okay.

**Mariel Grinstein:** Yeah.

**John Knightly:** We're also getting like German language again on the website, like from multiple stakeholders.

**John Knightly:** I get Portuguese.

**John Knightly:** Yeah, wouldn't normally click German.

**John Knightly:** So it sounds like there's some sanity issue.

**John Knightly:** I don't know if it's automated workflows or some trigger that maybe got set behind the scenes unknowingly, but something's off.

**John Knightly:** I couldn't replicate it, but a bunch of people in the U.S. got German redirects, and they wouldn't be clicking on German. It's not like we clicked on German and it stayed in German.

**John Knightly:** So we keep using that excuse that, oh, just reset the language to English.

**John Knightly:** But I think there's something, some weird trigger going on in Sanity that's causing this.

**John Knightly:** Maybe when we're making an update on the other languages, it somehow triggers on non-German or Portuguese sites or something. I don't know.

**John Knightly:** But I don't know if this is something we need our web dev team to look into, or who has the most sanity knowledge.

**Mariel Grinstein:** No, yeah, it's something for the web dev team. Every time we ask Terra, they say it's that we selected, but I don't think that's true anymore.

**John Knightly:** The U.S. salespeople — there's no way they're clicking on these other languages, right?

**Ani Grigoryan:** It also has something to do with caches.

**Ani Grigoryan:** It caches another language and then redirects to that version.

**Ani Grigoryan:** That cache thing needs to be solved from the back end.

**John Knightly:** Yeah, I don't know if you guys have an Asana task where you could put a web request to spend a little bit more time QAing that issue, because it keeps coming up. Grady's getting it, Britt's getting it, I get it, everyone's getting it. It's not really triggered by the user going to the other language site.

**Mariel Grinstein:** Yeah, I will.

**John Knightly:** Anyway, that might not have anything to do with this issue, but...

**Aida Knezevic:** But it is important because...

**Aida Knezevic:** Because it could impact bounce rates.

**Aida Knezevic:** And if people start bouncing from the website, that's not going to be good.

**Aida Knezevic:** And we've been getting it as well, just like looking at the website.

**Mariel Grinstein:** I like to shoot me the URLs that I need to publish, like here in the chat, because now I, yeah.

**Aida Knezevic:** Sorry.

**Aida Knezevic:** So, yeah.

**Aida Knezevic:** So this one, this is the question that I had.

**Aida Knezevic:** So this blog that was published.

**Mariel Grinstein:** Yeah, yeah.

**Mariel Grinstein:** Okay, can you shoot me the URL in the chat? Because I cannot seem to find it by title.

**Aida Knezevic:** It's no rush to figure it out right now, but just wanted to flag it for you.

**Aida Knezevic:** So I'm not sure what could be happening with sanity.

**Aida Knezevic:** But we do have a forward deployed engineer on our team who's working on automating publishing to your CMS.

**Aida Knezevic:** So what we will do — James gave us API access to Sanity, which allows us to connect Atlas, our content generation platform, to your Sanity instance, and we'll be able to push drafts to Sanity.

**Aida Knezevic:** It's not going to auto-publish, but we can, like, at least it's going to save us time on staging the content.

**Aida Knezevic:** So that's currently being developed, and we'll keep you posted as it happens.

**Aida Knezevic:** For the two articles that Mariel reviewed last week, we're staging them in your CMS today. I'm planning on pinging Dirk to see if he wants to be the author. In the meantime, do you have a generic Netwrix team author we could use as a placeholder until Dirk approves?

**Mariel Grinstein:** I think, John, that's your call.

**Philipp Denisenko:** Does it align with best practices?

**John Knightly:** It's kind of a no-no.

**John Knightly:** We had this fake name, Ryan Brooks, and he was cropping up all over the place, and he got called out on, like, Reddit that we were using someone that didn't exist.

**John Knightly:** And so we just said we're never going to do that again.

**John Knightly:** So we removed him.

**John Knightly:** Our CEO is complaining about it and stuff like that.

**John Knightly:** If we really need a human name, we can use Dirk.

**Aida Knezevic:** Perfect. Mariel gave me a list of authors you've been using, and Dirk is already in Slack. I can ping him and ask if he's cool being the author.

**Aida Knezevic:** But we do have, like, obviously it's all...

**Mariel Grinstein:** No, yes, I think Dirk is fine.

**Mariel Grinstein:** Dirk is available for both.

**Mariel Grinstein:** Yeah.

**Mariel Grinstein:** One thing is, I know I published the link you sent me, but when I go into that specific blog, I don't see a document history — nothing showing that anything changed.

**Aida Knezevic:** That's strange.

**Aida Knezevic:** Ade, who's our editor, went in today and re-staged and re-published it, but nothing happened. There's definitely something in Sanity that's not working right.

**Aida Knezevic:** The thing is, when Sanity is set up well, it's great. But CMS setups can get really tricky depending on how they're customized.

**Mariel Grinstein:** Finding an article is almost impossible. I don't know why the search functionality is so bad.

**Aida Knezevic:** Yeah, I struggle with it too.

**Aida Knezevic:** No, but there's an even worse Sanity Setup.

**Aida Knezevic:** I won't name the client, but there's an even worse customization.

**Aida Knezevic:** So, all right.

**Aida Knezevic:** So, I will ping Dirk for these two, and then we'll go ahead and publish them.

**Aida Knezevic:** Hopefully, we won't have an issue here because these are new articles, and the one that we're having an issue with is a refresh.

**Aida Knezevic:** So, that will hopefully be taken care of.

**Aida Knezevic:** And we're also working on four articles this week that we'll deliver by the end of the week, so hopefully we can start scaling publishing this week.

**Mariel Grinstein:** The director hasn't approved the images yet, so we've been running without them. We need to create custom images for social media.

**Aida Knezevic:** That makes sense. Sometimes images just slow web pages down anyway, so that's totally fine. We do have them as a backup if you need them.

**Aida Knezevic:** All right, so those are the content updates. On the content calendar — Dirk has reviewed it and had some questions around hierarchy. For simplicity, we can organize content according to the stage of the funnel that articles address.

**Aida Knezevic:** This allows us to just check ourselves so that we're not creating a lot of very general, very broad content.

**Aida Knezevic:** We are going to be focusing on a lot of like...

**Aida Knezevic:** Bottom of the funnel topic.

**Aida Knezevic:** So that's a column that we can add.

**Aida Knezevic:** And then anybody who's reviewing the content calendar can see, okay, we are really focusing on like bottom and middle of the funnel content.

**Aida Knezevic:** These are the topics and it allows us to kind of keep ourselves on track.

**Aida Knezevic:** And he did have some feedback for topics that he would like us to add, and we can add those into the content calendar.

**Aida Knezevic:** So we're going to do that.

**Aida Knezevic:** But we did clean up the content calendar by this.

**Aida Knezevic:** mean, all of the conversation that we had last week about like duplicate topics or topics that you don't want us to do because you're doing them for other projects.

**Aida Knezevic:** We removed all of them from the content calendar.

**Aida Knezevic:** So there really shouldn't be anything here that is an overlap.

**Aida Knezevic:** There are just two topics that you guys scheduled for April that are also in our content calendar. We can do them if you want — we can take them off your plate if you want to focus on something else.

**Mariel Grinstein:** Sure. Which ones?

**Aida Knezevic:** I'll tag you in Slack.

**Mariel Grinstein:** I sent a message yesterday. I know it's the non-human identities topic.

**Mariel Grinstein:** I already flagged it on Asana so my team wouldn't do it. Let me know after you update.

**Aida Knezevic:** Perfect. Now that the content calendar has been reviewed by Dirk, I'm going to come up with the six-week plan.

**Aida Knezevic:** That way you'll know exactly what topics we'll be working on each week, and we'll be working on separate lanes. The final update is on gated guides — Philipp sent over a list of...

**John Knightly:** The ratio is really high with collateral downloads — they're not getting to those anyway. I told Philipp we're probably going to un-gate them. That'll remove those from our lead volumes, but hopefully we'll get more qualified leads when people come back wanting a demo. He seemed fine with it. I mean, you can put it in writing to him — just say John spoke with you and we're going ahead with un-gating the PDFs. It'll reduce lead volumes but improve quality. Our year-on-year AQLs will go down, but hopefully we'll go up in high-value leads.

**Philipp Denisenko:** Okay, great. Then nothing holds us.

**Aida Knezevic:** I've already started going through the ones highlighted in green — the ones with the highest number of opportunities, pipeline impact, or AQL volume. I'm working through those first and leaving comments.

**Aida Knezevic:** Some of them rank quite well in search, so I wouldn't touch them. I'd just add more CTAs — one right after the intro and another in the middle of the page. Right now you only have CTAs after the conclusion and in the sidebar. For the high-performing ones, don't fix what's not broken — leave them as is. For the ones performing okay-ish, we could update them with information from the gated guide. I'm still working through this list, so I'll keep you posted on my progress.

**Philipp Denisenko:** So if you could just mark the ones you recommend keeping as gated, we'll investigate the actual conversion rate on page. If they rank well but people aren't willing to exchange contact details for a PDF, it doesn't make sense to keep them gated.

**Aida Knezevic:** Yeah, totally. I wouldn't touch the blog post content itself, but you could definitely ungate the PDF while keeping the blog post the same.

**Philipp Denisenko:** Gotcha.

**Aida Knezevic:** I think those are all the updates for today. My super high priority this week is getting the two new blogs published. I'll ping Dirk immediately and get the four new blog posts to you by the end of the week so that hopefully by next week, we have six articles published plus the one refresh. The refresh has been published but it's not showing up as published, so hopefully we can get that sorted. My top priority is seeing that the content gets indexed, gets traffic and impressions in Google Search, and gets cited by different LLMs. That's the most important thing for phase one.

**Aida Knezevic:** Do you have any other questions?

**John Knightly:** Just so you know, Dirk will be on planes, trains, and automobiles tonight getting back to Germany, but hopefully he'll be on tomorrow.

**Aida Knezevic:** Is he based in Germany?

**John Knightly:** Yeah. There was a Lufthansa strike, so he was leaving this afternoon to get home.

**Aida Knezevic:** Oh, no.

**Aida Knezevic:** I got back from San Francisco on Monday morning and everything was fine. Lufthansa is very temperamental though.

**Philipp Denisenko:** And if he decides to take Deutsche Bahn, he'll probably get to Germany in a week.

**John Knightly:** Yeah, who knows?

**Aida Knezevic:** I have my older brother who lives in Germany, so I visit quite often. Two years ago I took the plane and Deutsche Bahn, and it was so horrible with delays everywhere. The next time I drove my car from Bosnia to Germany — a two-day trip, but I wanted to avoid Deutsche Bahn.

**Philipp Denisenko:** Their on-time rate is around 60% — that's an infrastructure issue. Anyway, I had a question on the author thing. To Ralph's point, having a real person as an author is a requirement for Google and LLM algorithms. The recommendation is to have a real person, but let's keep Netwrix team as a temporary placeholder if we need to move fast. Just make sure to reach out to the actual author.

**Mariel Grinstein:** I know you're having the same CMS problems we are, so please flag them.

**Aida Knezevic:** Yeah, no worries. We'll be annoying about it.

**Ralph Marino:** Yeah, we didn't build it, so please do flag them.

**Aida Knezevic:** When Ade is staging the content, I'll tell him to create a new Netwrix Team author. If he runs into problems, I'll tag you guys, but hopefully there won't be any.

**Aida Knezevic:** But the sanity thing is, yes, we have one customer who has a really great sanity setup, but they're a web development agency.

**Aida Knezevic:** So they are really experienced when it comes to CMS, like headless CMS platforms, and actually wrote and edited a lot of content for them when I first joined GrowthX.

**Aida Knezevic:** The issue with headless CMS platforms is that if they're just set up by developers, they're not very helpful for marketers. You need developer involvement for simple things.

**Mariel Grinstein:** I hate that you can't add models to folders — you only have five available models, and if you want to add a table, it's not there. You have to put in a whole request to the web team. I've been waiting a month to get a table added to a builder.

**Aida Knezevic:** The table thing is horrible.

**Aida Knezevic:** We have another client with Sanity where you need to add every H2 title and section separately — it's really bad and annoying.

**Mariel Grinstein:** Yes, same issue here. The snippets are super annoying.

**Aida Knezevic:** When Sanity is set up well, it's great — it can be easy to publish. Yes, we have some magic for that.

**Aida Knezevic:** The thing is, our engineer Tanmay has to map all the different components to Atlas. She'll get it done. We auto-publish to Webflow, which is a lot easier.

**Mariel Grinstein:** In the future, it would be great if the content we produce could auto-publish to Sanity too, because publishing there is very painful.

**Aida Knezevic:** We'll definitely keep you updated on auto-publishing and I'm confident we can get it set up. From our end it should be straightforward.

**Mariel Grinstein:** I'm good. You guys?

**Ralph Marino:** Yeah, all good.

**Philipp Denisenko:** Thank you, thank you.

**Mariel Grinstein:** Do we have a meeting in two hours or not? I had it twice in my calendar.

**Aida Knezevic:** No, I'll cancel that one.

**Mariel Grinstein:** Okay, perfect.

**Aida Knezevic:** Okay, thank you. All right, thank you guys. I'll see you next week.

**Ralph Marino:** Bye-bye.
