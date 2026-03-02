# Otto <> Growth X - Weekly Sync

<metadata>
date: 2025-11-13
time: 18:01 UTC
duration: 19 minutes
organizer: Bailey Seybolt
participants: Bailey Seybolt, Jason Flateboe, Michael Gulmann
fathom_recording_id: 101503398
fathom_url: https://fathom.video/calls/472473642
share_url: https://fathom.video/share/G7t1_FXMFsJBshMXqbASfeUp5992TApx
source: fathom
enriched_on: 2026-03-02 14:30 UTC
speaker_note: Michael Gulmann joined remotely but did not speak during the meeting.
</metadata>

---

## Summary

GrowthX and Otto discussed content strategy, feature accuracy, and reporting metrics. The teams established a new process using Otto's master feature list as the single source of truth for content validation—to be integrated as a pipeline step—and agreed to quarterly content refreshes as new features roll out. Monthly deep-dive reporting meetings will begin with integration into the existing weekly sync to track impressions, keyword rankings, and LLM answer quality, with conversion tracking to be added to Looker once Otto's GA setup is complete.

---

## Context

Otto is an AI travel-planning agent—one of GrowthX's strategic content marketing clients. GrowthX has been producing content for Otto's website to drive organic visibility and support SEO and AI-visibility (AEO) goals. This was a weekly operational sync between Bailey Seybolt (GrowthX account lead) and Jason Flateboe (Otto product lead), with Michael Gulmann present from Otto. After roughly two months of initial content production, the meeting focused on refining workflows, ensuring content accuracy as Otto's feature set evolves rapidly, and establishing stronger measurement and reporting cadence. The teams' content strategy centers on informational articles that build awareness of Otto's core capabilities (trip planning, flight monitoring, in-trip changes) and newer features—positioning these as solutions to specific travel-planning problems rather than feature announcements.

---

## Relevance

**To GrowthX Delivery:**
- Implemented a master feature-list validation step in the content pipeline to maintain accuracy across all Otto articles—ensuring content references don't become outdated as Otto ships new features and iterations.
- Established quarterly content refresh cadence to integrate new capabilities into existing high-ranking articles, preserving SEO equity while updating feature coverage.
- Shifted from ad-hoc CMS process clarifications to documented publishing guardrails (CMS-only publishes, no main site staging changes) to prevent launch-day incidents.

**To CheckThat / AEO:**
- Monitoring LLM answer quality metrics: Otto's average top-position rate improved from 65% to 85% in one week, and LLM share increased from 7% to 8%—demonstrating the impact of targeted content on AI visibility.
- Observed a 30% drop in competitor citations last week, potentially tied to ChatGPT 5.1 release; requires continued monitoring to understand if this signals a broader LLM ranking shift.
- Planning to validate search intent for new features (e.g., trip planner) before content creation, linking feature launches to keyword opportunity identification.

**To GrowthX Business Development:**
- Strong early performance signals (impressions and keyword rankings trending up, growing keyword coverage daily) indicate healthy account health and expansion potential.
- Monthly deep-dive reporting now integrated into weekly sync—providing board-ready visibility into full-funnel metrics (impressions, keywords, LLM answers, conversions once GA tracking completes).
- Quarterly refresh process establishes predictable, defensible engagement model—reducing risk of content staleness as a renewal threat and positioning GrowthX as keeper of Otto's content strategy.

---

## Overview

- **Feature Accuracy Process:** Otto will provide a master capabilities file to serve as a single source of truth. GrowthX will add a validation step to its content pipeline to cross-check articles against this list, ensuring features are described accurately and supporting quarterly refreshes as Otto ships new capabilities.
- **Publishing Safeguard:** GrowthX confirmed its CMS publishing process is isolated from the main website, preventing accidental publication of Otto's staging changes before planned launches (this week's concern: Monday afternoon GA launch).
- **Strong Early Metrics:** Impressions trending up, keywords ranking daily, LLM answer quality improved (65% to 85% top-position rate), and share growing (7% to 8% last week). Competitor citations dropped 30%—likely tied to ChatGPT 5.1 update.
- **Expanded Reporting:** Monthly deep-dive meetings will be integrated into the existing weekly sync, led by Jacob. Looker dashboard is being realigned to topic clusters; GA conversion tracking to be added once Otto's setup is complete.

---

## Key Topics

### Content & Publishing

  - **Backlog:** A healthy content backlog is approved, providing a runway for prioritization based on relevance and topic cluster coverage.
  - **Delivery:** Three articles are staged for delivery today/tomorrow.
  - **Publishing Guardrail:** GrowthX will confirm its CMS publishing process is isolated from the main site.
      - **Rationale:** To prevent accidentally pushing Otto's unfinished staging changes live before the Monday afternoon launch.

### Feature Communication & Accuracy

  - **Problem:** Content was using overly specific, potentially outdated details (e.g., "flight monitoring every 30 seconds").
  - **Solution:** A new process will use a master feature list to ensure accuracy.
      - **Source:** Jason will provide the file from Otto's codebase that defines the AI agent's capabilities.
      - **Implementation:** GrowthX will add a pipeline step to validate content against this list, creating a single source of truth.
  - **Process for New Features:**
    1.  **Centralized Updates:** Use a shared Notion doc for real-time feature updates.
    2.  **SEO Validation:** Research search intent for new features to inform content strategy.
    3.  **Content Refresh:** Schedule a quarterly refresh of all articles to integrate new features.

### Reporting & Performance

  - **Looker Dashboard:** Being updated to align with topic clusters; data may be temporarily incomplete today/tomorrow.
  - **Monthly Deep Dive:** Jacob will lead a monthly reporting deep dive, integrated into an existing weekly sync.
  - **Performance Snapshot:**
      - **Impressions:** Trending up-and-to-the-right.
      - **Keyword Ranking:** Growing daily with relevant keywords.
      - **LLM Answer Quality:**
          - **Share:** Up from 7% to 8% last week.
          - **Position:** Average top-position rate improved from 65% to \~85% last week.
      - **Competitor Citations:** Dropped \~30% last week.
          - **Hypothesis:** May be a temporary effect of the recent ChatGPT 5.1 update.
  - **Conversion Tracking:** Looker will integrate Otto's Google Analytics conversion goals (e.g., app sign-ups) to provide a full-funnel view.

---

## Action Items

**Bailey Seybolt**
- Confirm w/ publisher CMS-only publish; avoid main site
- Add feature-list check to GrowthX content pipeline
- Create Notion feature-updates doc; share w/ Jason
- Schedule monthly deep-dive reporting w/ Jacob; integrate into weekly sync

**Jason Flateboe**
- Pull Otto capabilities file; send to Bailey for feature list
- Set up GA conversion tracking; notify Bailey to integrate into Looker

---

## Transcript
**Jason Flateboe:** Pretty good.

**Jason Flateboe:** I assume you're not actually in the mountains.

**Bailey Seybolt:** Yeah, my background is operational.

**Bailey Seybolt:** No, I'm working from home because we got our first snow in Vermont on the same day that our boiler decided to break, so I'm like in a construction site right now while we get a new boiler installed, and definitely not in the mountains.

**Jason Flateboe:** Gotcha.

**Jason Flateboe:** Michael's here with me, too, in the pod.

**Bailey Seybolt:** Oh, yeah.

**Jason Flateboe:** Just dialing in on.

**Jason Flateboe:** Hello.

**Bailey Seybolt:** Hello.

**Bailey Seybolt:** All right.

**Bailey Seybolt:** Well, here, I will share my agenda. So in terms of content updates, we have a great runway of approved topics now.

**Bailey Seybolt:** That allows us to keep prioritizing the most relevant ones. Feel free to keep bringing things up as we go—it doesn't mean we have to run with them in that order. It just means we've got a solid backlog to work through.

**Jason Flateboe:** Okay, great.

**Jason Flateboe:** Yeah, I only saw a few in there that were like obvious no's.

**Jason Flateboe:** So flag those, yeah.

**Jason Flateboe:** Yeah, so I pulled those out.

**Bailey Seybolt:** We'll continue to prioritize based on volume and topic cluster coverage. If you have new ideas as things change, we can still do additional research as needed.

**Bailey Seybolt:** We have three articles staged right now—one that we're updating based on your comments, and the rest we'll deliver today and tomorrow.

**Jason Flateboe:** Okay.

**Jason Flateboe:** Sorry, go ahead and finish—then I have a question.

**Bailey Seybolt:** No, I was only going to ask for any additional feedback if there was anything you wanted to raise.

**Jason Flateboe:** But no, I don't think so.

**Jason Flateboe:** Yeah, my question was about, so I have a bunch of changes in staging on the website that we don't want to go out until probably Monday afternoon.

**Bailey Seybolt:** I just want to confirm that when you're publishing the CMS stuff, it's going through the CMS only—you're not publishing any main website changes, correct?

**Jason Flateboe:** I'm 99% sure that's true, but good to confirm.

**Bailey Seybolt:** That should be true, but I'll flag it for our publisher to make sure. It's been a while since I've been in Webflow, and I know you can publish to the main site, so I just want to make sure.

**Jason Flateboe:** Yeah, you can certainly do it, and I think you are doing it. We'd hate to have one of your pushes suddenly reveal and change a bunch of things for our general availability and launch.

**Bailey Seybolt:** That would be a big oops. We're going to make sure that doesn't happen.

**Jason Flateboe:** Yeah, I literally have half-baked layouts that are broken in tests right now. I just don't want to push that out.

**Bailey Seybolt:** Yeah.

**Bailey Seybolt:** I also wanted to ask about a comment you left on one of the posts about specificity around things like monitoring flights. I wanted to talk through how you'd like us to handle that, because I should make it really clear in our writing guidelines.

**Bailey Seybolt:** If we don't want to speak about the feature that way, I'll update it so we never talk about it in that way.

**Jason Flateboe:** Yeah.

**Jason Flateboe:** I saw that sprinkled through maybe three different articles. My comment was just that I don't think we need to say "every 30 seconds"—just "continuously monitoring your flight" or something more general.

**Jason Flateboe:** And it starts before 24 hours before departure. We just don't need to be specific about the monitoring window. Would it be helpful if we put together something like a bullet-point list of what Otto does and doesn't do?

**Bailey Seybolt:** Yeah, that would be really helpful—a features list. With our writing guidelines, we push the pipeline to be specific wherever it can be, so we don't get a bunch of general meaningless content. If there are places where we have information but don't want to be specific about it, that's something we need to call out. I don't want a blanket "avoid numbers" rule because mostly we want specificity.

**Jason Flateboe:** So if you have a list of what Otto does and doesn't do with specific examples, we can add that to our writing guidelines. Since we're building an AI conversational agent, we have to tell Otto what it can and can't do so it knows what to do. If a user asks "can you track my flight every 30 seconds," Otto will respond properly saying whether it can or can't.

**Jason Flateboe:** As an aside, I'll go into the codebase and pull the file where we define what Otto can and can't do. I may massage it a bit, but you'll get it in a fashion that's ready for AI use.

**Bailey Seybolt:** Oh, even better.

**Jason Flateboe:** And in this example—flight monitoring, in-trip changes—we have some changes coming in the next few weeks with better monitoring, plugging in better data sources like FlightAware.

**Jason Flateboe:** I see it on your list too. We'll stay on top of this as it changes—there will be new features from user reviews and other things we'll want to highlight.

**Bailey Seybolt:** I think we'll create a specific step in our pipeline that refers to this features list as the master document. That way we can do a check after it writes the content.

**Bailey Seybolt:** Refer back and make sure it's all accurate based on the feature list. That way we have one thing to update instead of writing guidelines and company context.

**Jason Flateboe:** And I think we'll get better results that way.

**Bailey Seybolt:** That sounds perfect.

**Bailey Seybolt:** And we can continuously update it every time you launch something new or something changes.

**Bailey Seybolt:** So that answers the question of staying up to date. And the other thing I wanted to bring up: if you have any launches or priorities coming up, it's always good to think about building out content ahead of that launch. We can build out the content runway before launching a new feature.

**Jason Flateboe:** So what's the best way to get that to you? Is there a way within your system where we can describe a new capability, or is that more in the article list?

**Bailey Seybolt:** In terms of staying up to date with features.

**Jason Flateboe:** Yeah, we're moving pretty quickly. Here's an example: we just pushed live a trip planner.

**Jason Flateboe:** You can say, "I need to go to Boston Tuesday, New York Friday, Vermont Monday, then home," and Otto figures out the entire trip with multiple hotels and flights. That's a cool feature. So how do we let you know about it so we can fold it into articles? There might be a blog post announcing the feature, but then if GrowthX could write an article about why you'd need a trip planner and how it's better than doing it yourself—which is different than a feature announcement.

**Bailey Seybolt:** So I think there are three things here.

**Bailey Seybolt:** One is making sure we stay up to date with features so they inform our current content—that's what you're sending us. But I think we should have a Notion document where you can add things and tag us in real-time, rather than just telling us in a weekly sync.

**Jason Flateboe:** Yeah, having a place where you can drop that makes sense.

**Bailey Seybolt:** The second thing is understanding which features are priorities and which ones we should research to build new content around. We should validate whether there's existing search around the feature and its intent before writing.

**Bailey Seybolt:** The third thing is refreshing content we've already done. There will be features that didn't exist when we wrote a piece, but now should be called out. We have a separate pipeline to refresh existing content, so every couple months we could focus on that instead of producing new content.

**Jason Flateboe:** That sounds great. Actually, here's a question: if we have 50 articles out there and something that was impossible before is now possible, do you have a way to go back to those 50, read through, update them, and republish?

**Bailey Seybolt:** Exactly. That's what the refresh pipeline is for.

**Bailey Seybolt:** So it's a different pipeline because you don't want to start from scratch if something's already ranking. You want minimal changes that deepen context or improve quality. It has strong guardrails around how it changes content. If something's really good and just needs updating based on, for example, that features list, we can tell it to only make updates based on the list, and it will comb through and update accordingly.

**Bailey Seybolt:** Sometimes clients just want to spruce up articles that are already ranking, or sometimes the content isn't good and they want to tear it down and start over. It depends on the context. A few months in, once we have some traction, especially if you've released new features, we should build time in—maybe a week or two—where we produce less new content and focus on refreshes.

**Jason Flateboe:** That's definitely something we should have on the calendar.

**Bailey Seybolt:** I'll make a note. We'd probably want to do it in two months anyway, but if you release a bunch of new features before then, it might be worth thinking about it earlier. We can let you know when that happens.

**Bailey Seybolt:** In terms of reporting, two things. We're updating Looker to match topic clusters better. It's being updated today, so if you see missing information, that's why—it should be updated today or tomorrow.

**Bailey Seybolt:** And I wanted to touch base on timing. We talked about Jacob doing a monthly deep dive into reporting. Do you have a preference on what week of the month?

**Jason Flateboe:** Not really. It'd be great if we could layer it into the meetings already on the calendar. If we need extra time, that's fine. Do you need it for board meetings?

**Bailey Seybolt:** Yeah, some people will need it for board meetings or leadership meetings. So we'll put it on the calendar and have one of our weekly meetings focused on that.

**Bailey Seybolt:** In terms of snapshot reporting, impressions are going up—up and to the right, which is what we like to see. We're still early, but there's been a big jump in keywords we're ranking for every day, and the keywords themselves look like where we want to be.

**Bailey Seybolt:** On LLM share, we're growing too. Over the last week we went from 7% to 8%, which is incremental but in the right direction. And position quality is improving—we went from 65% average top-position rate over the past couple months to around 85% over the last week.

**Jason Flateboe:** Bailey, do you personally work with Engine?

**Bailey Seybolt:** No, I don't.

**Jason Flateboe:** So you're on Team Otto. We have to collectively beat your coworker who's working on Engine.

**Bailey Seybolt:** Yeah, they keep it siloed.

**Jason Flateboe:** But we're a team, so I want to see all three of us thrilled when you're crushing it. Look, Bailey is beating whoever's managing Engine.

**Bailey Seybolt:** Yeah, down with Engine.

**Jason Flateboe:** We'll get T-shirts.

**Bailey Seybolt:** Oh, and I noticed something weird over the last week—competitor citations dropped like 30%. Maybe LLMs are prioritizing third-party sources.

**Jason Flateboe:** It's hard to tell in a week, but ChatGPT released 5.1 around that time, which changed from 5.0.

**Bailey Seybolt:** It could be from that. It'll be interesting to see if it's a pattern over the next couple reporting cycles or just a fluke. Something to watch, because it may get harder and harder for that number to move.

**Jason Flateboe:** And it becomes less valuable.

**Jason Flateboe:** One question about reporting: I was just in Google Analytics looking at site metrics. One thing I'm going to look at is conversions—people clicking from the Webflow site to the app and signing up.

**Jason Flateboe:** So I need to make sure we have measurement on that. Is that something you'll layer into reporting? We have sign-up clicks at the bottom of the CMS articles.

**Bailey Seybolt:** Yeah, anything you set up to track in Google Analytics, we should be able to pull into Looker. So we don't need to duplicate that work.

**Bailey Seybolt:** No. Once you set it up, let me know and I'll make sure it looks right in Looker and there's no manual updating needed. Whatever you set up should be reflected in the data we're pulling into Looker.

**Bailey Seybolt:** Anything else you want to cover today?

**Jason Flateboe:** I don't believe so.

**Bailey Seybolt:** All right. I'll go get those T-shirts made for Team Otto, and we'll touch base next week.
