# Netwrix <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-25
time: 16:00 UTC
duration: 25 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic, Kathy Lam, Mariel Grinstein, Philipp Denisenko
fathom_recording_id: 125260250
fathom_url: https://fathom.video/calls/578565752
share_url: https://fathom.video/share/zyMfQYzNAM147jWRJ6VqkNRksA9yixhR
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Netwrix reviewed content progress, technical blockers, and content strategy refinements. GrowthX has published 7 articles and is delivering 7 more this week; Netwrix requested the ability to hide niche articles from the blog index and confirmed that Sanity production (not staging) should be used to avoid sync issues. The "Shadow AI Security" article is a top performer, validating the executive-focused strategy, and the team agreed to research related subtopics like "how to monitor AI apps" to expand the cluster. Netwrix also requested a workflow to repurpose their PR and thought leadership content (e.g., Forbes articles by Grady and Michael Watzel) into enriched blog posts without duplicating content.

---

## Context

Netwrix is a cybersecurity company providing unified visibility and threat management for IT environments. This is an ongoing content partnership where GrowthX is managing a full content production lifecycle: researching, writing, editing, and publishing articles on the Netwrix blog that target CISOs and security leaders. The engagement is in week 7, moving from initial content creation into regular publishing and refresh cycles. Mariel Grinstein is the primary Netwrix contact managing the CMS, working with the web team, and providing feedback on content. Aida Knezevic leads content production for GrowthX. The meeting focused on operational progress, resolving technical bottlenecks in their CMS workflow, and discussing content strategy to maximize performance.

---

## Relevance

**To GrowthX Delivery:**
- Content performance validation: "Shadow AI Security" article is driving the highest organic traffic and earning LLM referral traffic, validating the strategy of targeting executives with high-level overviews rather than deep technical detail.
- CMS workflow optimization required: Sanity staging/production confusion was blocking content updates; clarification that all edits should use production environment will streamline the publication process.
- New artifact opportunity: Repurposing PR and thought leadership content (e.g., Forbes articles) into unique blog posts by enriching with expert insights. GrowthX has successful precedent from a tax software client (interviewing internal experts).
- Guide ungating pipeline: New workflow being built to convert gated PDFs into refreshed articles with new CTAs, ready for deployment this week.

**To GrowthX Business Development:**
- Account health strong: 7 articles published and indexed; 3 in review; 7 more being delivered this week. On track to catch up on delivery schedule.
- Expansion opportunity: Netwrix explicitly requested new artifacts (hide articles from index, repurpose PR content), signaling appetite for expanded service scope beyond core content production.
- Potential long-term relationship: Move from phase 1 (content creation) to phase 2 (regular publishing and refreshing) indicates account maturity and commitment.

---

## Overview

- **Sanity Workflow Blockers:** Publishing is blocked by two issues: 1) content not syncing from Sanity to the live site, and 2) no option to hide specific articles from the main blog index.
- **"Shadow AI" Article Success:** The "Shadow AI Security" article is a top performer, driving the most organic traffic and receiving 3 visitors from LLMs. This validates the strategy of targeting executives with high-level content.
- **Content Repurposing:** Netwrix requested a new artifact to repurpose their PR/thought leadership content (e.g., Forbes articles) into unique blog posts, enriching content with expert insights without creating duplicates.
- **Guide Ungating:** A new pipeline is being built to ungated guides, using the PDF as a research input to create refreshed articles with new CTAs.

---

## Key Topics

### Sanity Workflow Blockers

  - **Content Syncing Failure:** Edits in Sanity are not appearing on the live site.
      - **Cause:** GrowthX was using the Sanity staging environment, which requires a web team sync to push changes live.
      - **Solution:** Use the Sanity **production** environment for all edits.
      - **Context:** Mariel noted sync issues have affected the production environment itself on recent days (Fri, Mon, Tue), which the web team has fixed.
  - **Blog Index Visibility:** Netwrix wants to hide specific articles (e.g., podcast recaps) from the main blog index page.
      - **Rationale:** These articles are highly niche and not relevant to a general audience.
      - **SEO Impact:** Hiding them will not hurt SEO, as the articles remain discoverable via direct links and are in the same subfolder.
      - **Action:** GrowthX will draft a request for the web team to add this feature to Sanity.

### Content Performance & Strategy

  - **"Shadow AI Security" Article:**
      - **Performance:** Top performer by organic traffic and average position (per Looker dashboard).
      - **Feedback:** A Netwrix security director called the article "super high level."
      - **Validation:** The article is successful because it targets executives (CISOs) who need high-level overviews, not deep technical detail.
      - **Next Step:** Research more specific topics within the AI security cluster (e.g., "how to monitor AI apps") to balance the strategy.
  - **Content Repurposing:**
      - **Request:** Create a new workflow to repurpose Netwrix PR/thought leadership content (e.g., Forbes articles by Grady and Michael Watzel) into unique blog posts.
      - **Goal:** Enrich content with expert insights without creating duplicate content.
      - **Precedent:** GrowthX has successfully used a similar process (interviewing internal experts) for a past client.

### Content Pipeline & Status

  - **Published:** 7 articles are live and indexed, including new Varonis and CyberArk alternative articles.
  - **In Review:** 3 articles are awaiting Netwrix feedback.
  - **Upcoming:** 7 new articles will be delivered this week to catch up on the schedule.
  - **Guide Ungating:** A new pipeline is being built to ungated guides.
      - **Process:** Use the PDF as a research input → refresh the article with new online research → add new CTAs.
      - **Timeline:** The pipeline will be ready this week, with content production to follow.

---

## Action Items

**Philipp Denisenko (Netwrix)**
- Confirm w/ John re: updated product messaging; share w/ Kathy

**Aida Knezevic (GrowthX)**
- Send 7 articles this week to Mariel/Philipp for review
- Prepare Sanity instructions (hide from index, use production); send to Mariel to forward to web team
- Check w/ Ade re: Sanity production sync issues
- Research shadow AI subtopics; propose new articles
- Explore repurposing PR/leadership content (Grady, Michael Watzel); report back to Mariel

**Mariel Grinstein (Netwrix)**
- Send miniature logo to Aida/Kathy via Slack
- Review 3 articles; send feedback to Aida/Kathy

---

## Transcript
**Aida Knezevic:** This meeting is being recorded.

**Kathy Lam:** Hello.

**Kathy Lam:** Good evening.

**Aida Knezevic:** Good afternoon.

**Aida Knezevic:** For me, it's 5 p.m.

**Kathy Lam:** Hey, Philip.

**Kathy Lam:** We heard you for a second, but I think you're on mute.

**Philipp Denisenko:** Yeah, I'm in Starbucks, so I'm muted myself.

**Kathy Lam:** Excellent. Were you able to get either any of our emails or Slack messages this week?

**Philipp Denisenko:** Yes.

**Kathy Lam:** I had spoken to John on Thursday and he mentioned you guys have some updated product messaging. Hoping to see if we can get a copy of it to incorporate into our artifacts.

**Philipp Denisenko:** Well, it's hard to say what exactly John mentioned, honestly. Let's double check with John, I guess.

**Aida Knezevic:** Hi, Mariel.

**Aida Knezevic:** Were you, are you able to access Slack?

**Aida Knezevic:** Because I know a bunch of you guys were removed from the Slack channel.

**Mariel Grinstein:** So I was wondering if you are able to access it now.

**Mariel Grinstein:** Hi, yes.

**Mariel Grinstein:** Because.

**Mariel Grinstein:** Let me see.

**Aida Knezevic:** Yes.

**Mariel Grinstein:** Oh, no, I see the channel.

**Mariel Grinstein:** Yes.

**Aida Knezevic:** Okay.

**Mariel Grinstein:** All good.

**Aida Knezevic:** Okay, perfect.

**Aida Knezevic:** Right.

**Aida Knezevic:** Okay, great.

**Aida Knezevic:** Let's get started then.

**Aida Knezevic:** In that case, I'm going to go ahead and share my screen.

**Mariel Grinstein:** Okay, so we have a lot of articles to review, I think.

**Aida Knezevic:** Yeah, yeah, you're, we are also kind of working on a batch of content that we'll send over to you soon.

**Aida Knezevic:** But yeah, so yeah, before we get into the feedback, I did want to share some content updates.

**Aida Knezevic:** So yeah, the drafts that are still with your team for review are these three drafts right here, while the Airtable loads.

**Aida Knezevic:** So let's, Airtable isn't always good to us, so let's just.

**Aida Knezevic:** Yeah, but there are three articles.

**Aida Knezevic:** Yeah, exactly.

**Aida Knezevic:** So, yeah, these are the three articles that are ready for you guys' review.

**Aida Knezevic:** And we will be sharing seven this week, just to catch up with the two from last week, because we had to update some of the artifacts, especially in regards to the competitive product listicles that we had.

**Aida Knezevic:** John shared some additional competitors that we should include in one of the articles from last week.

**Aida Knezevic:** So we updated those articles first.

**Aida Knezevic:** So these are the three that are ready for your review now.

**Aida Knezevic:** I will ping you as soon as the new articles are ready for your review.

**Aida Knezevic:** And then we have published four new blogs.

**Aida Knezevic:** So we now have seven articles that are live.

**Aida Knezevic:** They have all been indexed, which is great.

**Aida Knezevic:** And this week we actually published our first alternative article.

**Aida Knezevic:** With Varonis, and also CyberArk Alternatives.

**Aida Knezevic:** So by this time next week, we should be able to see the impact in terms of at least search traffic and impressions.

**Aida Knezevic:** So I will keep you posted on that front.

**Mariel Grinstein:** One thing that we didn't want to happen, that is happening, that we didn't want them to be seen on the main level page.

**Aida Knezevic:** Okay.

**Mariel Grinstein:** Yeah, I don't know if I think we spoke about it.

**Mariel Grinstein:** Like, but I don't know if it's possible to actually do that.

**Aida Knezevic:** Is it, is it?

**Mariel Grinstein:** and the Netwix team logo still, like, if you open that link, the resources blog, I just sent it on the chat.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So let me actually see really quickly.

**Mariel Grinstein:** I already sent that pop-up to the web team that they did.

**Aida Knezevic:** already sent team team

**Mariel Grinstein:** You see the Netwrix logo is like condensed.

**Aida Knezevic:** Ah, condensed, okay.

**Aida Knezevic:** Do you have one that you want us to use?

**Aida Knezevic:** We can use that one.

**Mariel Grinstein:** Yeah, I think you could use the miniature.

**Mariel Grinstein:** Let me see.

**Aida Knezevic:** If you could send it in Slack, that would be helpful.

**Mariel Grinstein:** Yeah, yeah.

**Mariel Grinstein:** Let me grab it.

**Aida Knezevic:** Okay, I think when it comes to, let me check with Ade to see if this is something that if we have the option when publishing to remove some articles from the index page, we will do it.

**Aida Knezevic:** If that option doesn't exist, then we need to, we just need to contact your, like, web team or whoever's in charge of sanity.

**Aida Knezevic:** To set that option for us.

**Mariel Grinstein:** Okay.

**Mariel Grinstein:** can check quickly in Sanity if there's an option.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Cool.

**Mariel Grinstein:** And if not, yeah, we'll have to talk to the web team.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Sorry.

**Aida Knezevic:** Go ahead.

**Mariel Grinstein:** I feel like you did it.

**Mariel Grinstein:** What do you think about having them published right now like that?

**Mariel Grinstein:** Are you okay with it?

**Philipp Denisenko:** Well, I was wondering whether if we remove them from the index page, it would kind of hurt the, you know, authority that's getting passed from the domain nav to this page or not.

**Aida Knezevic:** Uh, no, we should be fine.

**Aida Knezevic:** Um, it's the same subfolder and, um, it's discoverable.

**Aida Knezevic:** Um, everything gets indexed super fast.

**Aida Knezevic:** So as long as it's discoverable on the website through other links, and we'll be adding links to this content as well, it shouldn't really be an issue for us.

**Philipp Denisenko:** Okay, so I'm with Mariel here.

**Philipp Denisenko:** I guess, you know, there's no point in having this article there for everyone because, you know, it's only relevant for a very specific podcast, right?

**Aida Knezevic:** Yeah, yeah.

**Philipp Denisenko:** That's my take on it.

**Aida Knezevic:** Yeah, yeah.

**Aida Knezevic:** Okay, that sounds good.

**Aida Knezevic:** We will...

**Mariel Grinstein:** No, yeah, I'm checking and there's no way of just finding it.

**Aida Knezevic:** Okay, then in that case, we can prepare just like a quick doc with instructions of what we need to be able to do in Sanity, and then you can just forward it to the web team. They can implement it quickly.

**Aida Knezevic:** No, I mean, while we're still talking about sanity, so the thing that we're still dealing with is, let's say, for example, we publish something or we have to update an article that we refreshed, the changes are not showing up on the main site.

**Aida Knezevic:** And we don't really know why that happens.

**Aida Knezevic:** And Ade also told me, like, you have two versions of sanity, like the production side, and then...

**Mariel Grinstein:** Yeah, staging.

**Aida Knezevic:** And sometimes it doesn't, like, the content doesn't match.

**Aida Knezevic:** So some content is live in one version of sanity and not in the other one.

**Mariel Grinstein:** You always need to use a production.

**Aida Knezevic:** Okay, okay, cool.

**Mariel Grinstein:** Not staging.

**Mariel Grinstein:** Yeah, because, yeah, they, if, to think changes...

**Mariel Grinstein:** From staging to production, you need the web team.

**Aida Knezevic:** So just go ahead and edit on production.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** That's good for us to know in that case.

**Aida Knezevic:** So hopefully that will help us.

**Aida Knezevic:** But that's like the one thing because now we're kind of like we're in week seven.

**Aida Knezevic:** We're like preparing for you guys to enter phase two.

**Aida Knezevic:** We'll be like publishing content regularly every week and refreshing a lot of content.

**Aida Knezevic:** And so that's just the one thing because we don't want it to be a burden on you, Mariel.

**Aida Knezevic:** If we have to like tag you every time and be like, hey, like, can you please check what's happening in Sanity and like, why isn't this live?

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** So we're just trying to think ahead.

**Aida Knezevic:** But if we can, if I will ask Ade to check and then if everything's okay on the production side, then we will, we will.

**Mariel Grinstein:** There was one day, like, I think it was Monday that even if you were editing production, the changes didn't sync.

**Mariel Grinstein:** On Friday, it happened the same.

**Mariel Grinstein:** So I don't know when you guys were editing, but there were two days that nothing synced from the background to production.

**Mariel Grinstein:** Yeah.

**Mariel Grinstein:** But I raised it to the web team and they fixed it.

**Aida Knezevic:** Okay.

**Mariel Grinstein:** And yesterday, yeah, yesterday also we had some issues.

**Aida Knezevic:** Okay.

**Aida Knezevic:** So we were publishing yesterday.

**Mariel Grinstein:** Okay.

**Mariel Grinstein:** It depends on the time.

**Mariel Grinstein:** In the afternoon, it worked okay, but in the morning, it didn't.

**Mariel Grinstein:** I also had like a call with someone from the PML team because they were having issues and saying what's happening to me.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Then we'll keep that in mind.

**Aida Knezevic:** All right.

**Aida Knezevic:** All right.

**Aida Knezevic:** We'll see.

**Aida Knezevic:** I'll check in with Ade and see if he ran into some issues as well.

**Aida Knezevic:** All right.

**Aida Knezevic:** And then on, I know last week we were talking about ungating some guides.

**Aida Knezevic:** Uh,

**Aida Knezevic:** And James gave us feedback on which two guides we should prioritize.

**Aida Knezevic:** So we are in the process of building the new pipeline for just like updating those blog posts.

**Aida Knezevic:** We want the ability to use the PDF gated guide that you have as an input at the research stage.

**Aida Knezevic:** And in order for us to do that, we have to build an extra step at the research stage where we will just be able to like upload the PDF or just copy a markdown version of the PDF so that when we refresh the article, it uses information from the gated guide as well as like new research that it finds online.

**Aida Knezevic:** And then we can refresh that content as well and add new CTAs to it.

**Aida Knezevic:** So I'm hoping that that will be done this week and then we can...

**Aida Knezevic:** Plan and add in that content to production for the next couple of weeks.

**Aida Knezevic:** In terms of content that we've published so far, the article around shadow AI is doing really well.

**Aida Knezevic:** If you go to your Looker dashboard, and let me just switch the...

**Aida Knezevic:** So this is your Looker dashboard, and when you access it, you should all have access to it.

**Aida Knezevic:** If you sent me your Gmail account, you should have access to it.

**Aida Knezevic:** If you didn't, just send me your Gmail account, and I'll add you to it.

**Aida Knezevic:** But when you go to the cohorts report, you can see this is just a page that contains GrowthX content.

**Aida Knezevic:** Make sure to uncheck non-GrowthX URLs so it doesn't show up in the data set.

**Aida Knezevic:** And then you'll be able to see just the performance of the content that we've published so far.

**Aida Knezevic:** This is data from Google Analytics 4, and you can...

**Aida Knezevic:** Just the data source here.

**Aida Knezevic:** So you can uncheck, for example, direct traffic or referral traffic.

**Aida Knezevic:** So you can just focus on organic traffic.

**Aida Knezevic:** And then if you scroll down, this is obviously data from Google Analytics 4.

**Aida Knezevic:** And then this is data just from Google Search Console and the organic traffic that we've gotten from Google so far.

**Aida Knezevic:** In both cases, shadow AI security is getting the most traffic and the average position is quite high.

**Aida Knezevic:** And I think if you go to the LLM referral report and you exclude non-growthx traffic, yeah, it's also gotten three visitors just from LLMs.

**Aida Knezevic:** So this type of content just around shadow AI security, like AI security, we're going to do additional topic research for that cluster.

**Aida Knezevic:** here we already have, let me.

**Mariel Grinstein:** A note from our director of security research around the shadow AI security risks.

**Mariel Grinstein:** So he told me like it was super high level and that it wouldn't be interesting to the readers.

**Mariel Grinstein:** I'm not sure because he's like way super technical and he writes with code snippets.

**Mariel Grinstein:** So interesting.

**Aida Knezevic:** mean, who is like, who, who is the reader that he has in mind?

**Mariel Grinstein:** Yeah, that's a good question.

**Mariel Grinstein:** But do you think it was like two CISOs?

**Aida Knezevic:** Yeah, yeah, yeah.

**Aida Knezevic:** This is the one and he was okay with it, right?

**Aida Knezevic:** Yeah, yeah.

**Mariel Grinstein:** I think with he thinks it's good, it's fine because he's a CISSP.

**Aida Knezevic:** Yeah, yeah, yeah.

**Aida Knezevic:** No, with the content strategy that we built.

**Aida Knezevic:** S.

**Aida Knezevic:** Yeah,

**Aida Knezevic:** We are trying to reach more like executives and many of them might not be like as well versed in the details.

**Aida Knezevic:** So but we can explore like the topics that are under shadow AI, like how to like monitor AI apps, for example, or how to like monitor what people are using AI apps for.

**Aida Knezevic:** Like those are all topics that I've seen in SEMrush.

**Aida Knezevic:** So that's something that we could add.

**Aida Knezevic:** And that would be like pretty, I think it would be pretty specific, not vague at all.

**Mariel Grinstein:** Yeah, that would be cool.

**Mariel Grinstein:** Yes.

**Aida Knezevic:** Okay.

**Mariel Grinstein:** Yeah.

**Mariel Grinstein:** Cool.

**Mariel Grinstein:** Yeah, maybe it is too informational, but.

**Mariel Grinstein:** Yeah, I actually think that article is good, but.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Okay.

**Mariel Grinstein:** Just so you know, he commented that.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Okay.

**Aida Knezevic:** Yeah.

**Aida Knezevic:** Thanks for the heads up.

**Aida Knezevic:** That's.

**Aida Knezevic:** That's that is helpful context.

**Aida Knezevic:** All right.

**Aida Knezevic:** I think those are all the updates that we had.

**Aida Knezevic:** Kathy, did you have anything else?

**Kathy Lam:** No, I think I think that was primarily it.

**Kathy Lam:** Yeah.

**Aida Knezevic:** OK.

**Aida Knezevic:** OK, cool.

**Aida Knezevic:** Is there anything else on your guys' ends that you would like to discuss or any feedback or just anything that we haven't covered so far that you want us to address?

**Mariel Grinstein:** Um, this is one thing that I would like to do that it would be cool if you can guys do it because we are now like going to change our AI.

**Mariel Grinstein:** So it's not wise for me to be with it right now.

**Mariel Grinstein:** And like Grady and Michael Watzel, they do a lot of PR articles.

**Aida Knezevic:** Okay.

**Mariel Grinstein:** And like when they do that, it's like a really soft leadership content that it's really good.

**Mariel Grinstein:** So you.

**Mariel Grinstein:** you.

**Mariel Grinstein:** Maybe if we could find a way to scrap those and get new content out of them.

**Mariel Grinstein:** I don't know if you've ever done something like that.

**Mariel Grinstein:** Like if he goes and does a podcast or writes an article for Forbes.

**Mariel Grinstein:** I don't know.

**Mariel Grinstein:** I was thinking about how to repurpose those, but not being flagged as duplicating content or doing something different.

**Mariel Grinstein:** But yeah, just an idea to see if it's an artifact that you could guys build.

**Aida Knezevic:** Yeah, yeah, that is helpful.

**Aida Knezevic:** And we could, yeah, it's totally an artifact that we could build and use it to enrich existing content.

**Aida Knezevic:** I mean, I remember this was like last summer.

**Aida Knezevic:** We were working with a startup in the tax space last summer. There's a lot of content on the internet about taxes, but a lot of it is very generic. So we actually ended up interviewing the people on their sales team and internal experts. We used their quotes in the content or any points they were making. Sometimes when you have actual experience with something, there are things that people do and notice that aren't part of content on the internet.

**Mariel Grinstein:** Interesting, so I'm glad Gavin had this insight.

**Aida Knezevic:** I think we can definitely explore this. I'll look into that and get back to you.

**Aida Knezevic:** All right then, keep us posted on the three articles you are reviewing.

**Mariel Grinstein:** Yeah, I left myself a task for tomorrow and I'll give you feedback tomorrow.

**Aida Knezevic:** Amazing, thank you. I'll send you a follow-up in Slack later. Bye!
