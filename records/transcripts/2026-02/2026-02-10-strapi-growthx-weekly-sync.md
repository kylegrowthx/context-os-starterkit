# Strapi <> GrowthX -  Weekly Sync

<metadata>
date: 2026-02-10
time: 17:29 UTC
duration: 33 minutes
organizer: Carrie Chowske (GrowthX)
participants: Carrie Chowske (GrowthX), Usman (GrowthX), Victor Coisne (Strapi), Paul Bratslavsky (Strapi), Theodore Kelechukwu Onyejiaku (Strapi)
fathom_recording_id: 121257882
fathom_url: https://fathom.video/calls/561182213
share_url: https://fathom.video/share/5pRCVzTAM_1xr5SjqtTowBNBRUiv6Xr9
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

GrowthX and Strapi reviewed content performance and alignment on content strategy. Content refreshes are driving strong results—the "open source CMS platforms" refresh saw 144% session growth and 173.5% engagement increase—prompting a decision to scale refresh efforts across the portfolio. The team also identified niche integration pages (Clerk, Coolify, Railway) as higher-impact targets than flagship topics, which are being cannibalized by AI Overviews. Operationally, the meeting cadence shifts to bi-weekly to focus on strategy and performance, with production updates handled asynchronously in Slack. Theo will implement an Airtable webhook to automate content tracking once Victor grants the necessary admin permissions.

---

## Context

Strapi is an open-source headless CMS that GrowthX provides content marketing and AI visibility services for. This is a recurring weekly operational sync between Carrie Chowske (GrowthX's content strategist), Usman (GrowthX's content producer), and three members of the Strapi team: Victor Coisne (strategy), Paul Bratslavsky (developer/writer), and Theodore Kelechukwu Onyejiaku (operations). The meeting reviews content performance metrics, discusses strategic pivots, and coordinates on action items. The Strapi account is significant for GrowthX—it's a $200k+ engagement focused on organic visibility and AI search performance. Recent wins include Strapi achieving a 39% share of voice against competitors like Contentful, Sanity, and Storyblock.

---

## Relevance

**To GrowthX Delivery:**
- Content refresh strategy is working at scale—70k sessions driven by refreshes at +45% QoQ growth. This validates the refresh-focused approach and should be replicated across other GrowthX accounts.
- Niche integration pages outperforming flagship topics shows the shift toward long-tail, high-intent content is the right play against AI Overviews cannibalizing broad queries.
- Airtable webhook automation reduces manual tracking burden on the GrowthX ops team and improves real-time visibility into content performance.

**To CheckThat:**
- Strapi leads competitors with 39% share of voice on evaluation-stage queries, demonstrating effective AI visibility positioning.
- Integration-related prompts need to be added to CheckThat tracking to monitor AI citation performance on new niche content.
- New category-based comparison posts (e.g., "Best Hosting for Strapi") should be tracked for AI search lift to validate the cross-linking strategy.

**To GrowthX Business Development:**
- Meeting cadence shift to bi-weekly is a positive signal—it indicates the account is stable and production flows are working without heavy coordination overhead.
- Usman's direct relationship with Theo (async coordination) is reducing friction and improving delivery velocity—strong account health indicator.
- Victor's interest in potential Content OS integration (if open-sourced) represents expansion opportunity that could deepen the strategic partnership with Strapi.

---

## Overview

- **Performance:** Content refreshes are highly effective (e.g., `open source CMS` refresh saw +144% sessions), while niche integration pages outperform flagship topics due to AI search cannibalizing clicks on broad queries.
- **Strategy:** Scale content refreshes and prioritize niche integration topics (e.g., emerging frameworks, hosting providers) to capture high-intent traffic.
- **Operations:** The sync cadence shifts to bi-weekly, freeing up meeting time for strategy. Theo will implement an Airtable webhook to automate tracking and improve visibility.

---

## Key Topics

### Content Performance & Strategy

  - **Content Refreshes:**
      - **Performance:** Driving \~70k organic/referral sessions (+45% QoQ).
      - **High-Impact Examples:**
          - `best JavaScript frameworks`: +48% sessions, +42% engagement.
          - `open source CMS platforms`: +144% sessions, +173.5% engagement.
      - **Rationale:** Aligns with Google's preference for fresh content and captures AI search citations.
  - **Integration Pages:**
      - **Performance:** Niche pages outperform flagship topics.
      - **Rationale:** AI Overviews cannibalize clicks on broad queries, while niche topics retain high-intent traffic.
      - **Action:** Prioritize emerging tools and hosting providers.
          - **Examples:** Clerk, Coolify, Railway.
          - **Note:** `Auth0` is a duplicate of `Okta` and should be removed.
  - **AI Visibility:**
      - **Status:** Strapi leads competitors (Contentful, Sanity, Storyblock, HighGraph) with a 39% share of voice for evaluation-stage queries.
      - **New Tactic:** Create category-based comparison posts (e.g., "Best Hosting for Strapi") to drive cross-linking to individual integration pages.

### Operational Updates

  - **Meeting Cadence:**
      - **Decision:** Shift to bi-weekly syncs.
      - **Rationale:** Focus meetings on strategy and performance, with production updates handled asynchronously in Slack.
  - **Airtable Webhook Implementation:**
      - **Goal:** Automate content tracking in Airtable, replacing manual updates.
      - **Blocker:** Theo lacked admin permissions to create the webhook.
      - **Resolution:** Victor granted Theo Super Admin access. Theo will now implement the webhook using the code and token Carrie provided.
  - **Tooling & Partnerships:**
      - **CheckBat:** Extended trial access for Strapi is expected this week.
      - **Content OS:** Victor will contact Marcel and Jason about a potential integration if the project becomes open source.

---

## Decisions & Commitments

**Strategic Decisions:**
- Scale content refresh efforts across the portfolio based on proven ROI (45% QoQ growth, 70k sessions, examples of +144% session growth).
- Shift focus to niche integration pages (Clerk, Coolify, Railway, emerging frameworks) over flagship topics due to AI Overviews cannibalizing broad queries.
- Create category-based comparison posts (e.g., "Best Hosting for Strapi") to drive cross-linking and capture evaluation-stage AI search traffic.

**Operational Decisions:**
- Move to bi-weekly meeting cadence starting with next week's sync, then every two weeks after. Production updates will flow asynchronously via Slack.
- Implement Airtable webhook automation to replace manual content tracking and improve real-time visibility into publication.
- Victor will grant Theo Super Admin access to Strapi to enable webhook implementation.

**Partnerships & Tools:**
- CheckThat extended trial access expected this week; Victor to create account using Strapi email.
- Victor will contact Marcel and Jason about potential Content OS integration if the project becomes open source, with possible launch support from GrowthX.

## Open Questions

- Exact details of CheckThat extended trial period and terms (Carrie to confirm).
- Final scope of Content OS integration and timeline if project is open-sourced (Victor to discuss with Marcel/Jason).
- Which manual integration pages need to be excluded from auto-update pipeline (Theo to share list with Carrie).

---

## Transcript
**Victor Coisne:** This meeting is being recorded.

**Paul:** Hey, Victor.

**Victor Coisne:** How's it going?

**Victor Coisne:** Good, good.

**Victor Coisne:** Different setup today.

**Paul:** I went to the coffee shop.

**Paul:** Needed to get out of the house, you know?

**Paul:** So it's within walking distance, so it's like a nice walk.

**Paul:** It's beautiful.

**Victor Coisne:** You don't have the co-working space next to you guys?

**Paul:** Not next to us.

**Paul:** No.

**Victor Coisne:** But this works well.

**Victor Coisne:** Okay.

**Victor Coisne:** Sounds good.

**Victor Coisne:** It's just looking at the data they sent.

**Victor Coisne:** Oh, hi, Carrie.

**Carrie Chowske:** Hello.

**Victor Coisne:** Good morning.

**Paul:** Hello.

**Carrie Chowske:** How are things going?

**Victor Coisne:** Things are going pretty well.

**Carrie Chowske:** How about you?

**Carrie Chowske:** I'm doing great.

**Carrie Chowske:** I'm trying to find where I opened up the agenda on my desktop.

**Carrie Chowske:** That's always my...

**Carrie Chowske:** I'm looking for what I'm...

**Carrie Chowske:** I can never find what I'm looking for.

**Carrie Chowske:** Hey, wait.

**Carrie Chowske:** There we go.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Cool.

**Carrie Chowske:** Oh, all right.

**Victor Coisne:** Here's you.

**Victor Coisne:** Perfect.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So, I'm sorry.

**Carrie Chowske:** was a little late sending it.

**Carrie Chowske:** I thought I had hit send on it, and it was still sitting in the draft in...

**Carrie Chowske:** Good

**Carrie Chowske:** Slack.

**Carrie Chowske:** apologize for that.

**Carrie Chowske:** But we should be good here.

**Carrie Chowske:** I was having a little trouble figuring out where we were with production because Usman is out of office this week, but he popped in this morning, so I was able to get this updated.

**Carrie Chowske:** He just kind of gave me a rundown of where we're at with content for the next few weeks.

**Carrie Chowske:** think Theo just approved a bunch of those Next.js topics that he had proposed, so we're good there.

**Carrie Chowske:** But just that we're kind of, after that, we're kind of running out of what has been approved, so I didn't know if we wanted to, what we wanted to look at, and that may hinge, I think, a little bit on what we're going to talk about with, like, the refreshes and integration pages, but I just wanted to bring to your attention that's kind of where we're at with production, and that we had, I know that there had been a pause on editorial, and I didn't know if there were anything there that we wanted to move forward with.

**Carrie Chowske:** We've got a few titles under approved, but they are on hold, so just something to kind of keep in the back of your mind.

**Carrie Chowske:** As we talk about performance.

**Carrie Chowske:** And then for this list that we had, I think the only thing here that's really kind of pressing, I did get that the refresh is added to Looker, but I don't think everything is in there.

**Carrie Chowske:** I was looking at it and I was like, I'm not 100% sure this is everything.

**Carrie Chowske:** So I wanted to make sure that we had that updated before we really start using it.

**Carrie Chowske:** But I did pull some data and look at the refreshes separate from that.

**Carrie Chowske:** So I do have some data to share, but just so you know, it is in there, but I'm not 100% sure that all of our refreshes are in there.

**Carrie Chowske:** So that's where we're at with that.

**Victor Coisne:** Sounds good.

**Carrie Chowske:** I also wanted to see how you guys felt about going to biweekly for our meeting cadence.

**Carrie Chowske:** This is just something we're kind of doing across the board, but now that we're focusing more, our, our weekly.

**Carrie Chowske:** We'll be%

**Carrie Chowske:** Thanks for our bi-weekly in this case, more on performance and strategy that we, you know, aren't having to, we're not keeping up.

**Carrie Chowske:** We'd be keeping up with production in our weekly Slack updates.

**Carrie Chowske:** And then we'd have, you know, this time to kind of really talk about any changes we wanted to make to strategy or, you know, just for us to do some deeper performance reporting.

**Carrie Chowske:** So I don't know how you guys feel about that.

**Victor Coisne:** Yeah.

**Victor Coisne:** I mean, as long as, like, we don't lose momentum through, you know, we have a back and forth on Slack and make sure, like, we don't stall, you know, production, I'm fine with bi-weekly, yeah.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Yeah, it won't have an effect on production at all.

**Carrie Chowske:** And again, I can continually, like, update that in Slack.

**Carrie Chowske:** I think also Usman's been really good about communicating with Theo directly, too, which has been nice because the two of them can hash out the little finer details.

**Carrie Chowske:** And, and, and, and then we know that.

**Carrie Chowske:** Things are getting, rather than constantly playing a game of telephone, think that works, that's worked really well.

**Carrie Chowske:** I don't know how you feel about that, Theo, but it felt like it was a good, it helped smooth things along this week.

**Victor Coisne:** Yeah.

**Carrie Chowske:** Okay.

**Theodore Kelechukwu Onyejiaku:** Oh, yeah, it's cool, baby.

**Carrie Chowske:** Yeah?

**Carrie Chowske:** Okay, just making sure, just making sure.

**Carrie Chowske:** Okay, so for performance, I looked at primarily refreshes and the integration pages, this go around, this chart is pretty much unchanged from what we shared last week because we're just, including January, we haven't started adding the February data to this because it's going to be way down here because we're only two weeks into the month, but we're still seeing that upward trajectory overall when it comes to sessions, so it continues to grow month over month.

**Carrie Chowske:** The refresh content is driving about 70,000 sessions, same filters on this as well, so we're looking at just organic and referral traffic here, and that's about 45% growth, this is looking at it.

**Carrie Chowske:** So for these, I looked at a 90 days, so 90 days over the previous.

**Carrie Chowske:** And then we've got that set up, like I said, but I'm not sure that we've got the full picture.

**Carrie Chowske:** So these I actually did manually via using Search Console data and some GA4 data.

**Carrie Chowske:** And then Usman flagged a couple refreshes that he said he had done recently, that he saw some week-over-week traffic looking really strong.

**Carrie Chowske:** And he and I were talking about, like, whether that would be, make that a good idea to continue refreshing some of the content.

**Carrie Chowske:** And I've got a couple things that might tell us a little bit about where we can focus that.

**Carrie Chowske:** But we could identify more pages to refresh and do some more of that and hopefully grow some of that traffic.

**Carrie Chowske:** Saw 48% growth in sessions and a 42% increase engagement on the best JavaScript frameworks.

**Carrie Chowske:** And then 144% growth and 173 points.

**Carrie Chowske:** 5 increase in engagement for the open source CMS platforms, refreshes that we did.

**Victor Coisne:** Yeah, that's exciting.

**Victor Coisne:** I really think that we should keep scaling the refresh.

**Victor Coisne:** I think it is obvious that it's playing a big role, not only in kind of organic traffic, but also like in LLM traffic and citation.

**Victor Coisne:** So I really think we have a lot of content and a lot of it, I think, is outdated.

**Carrie Chowske:** Exactly.

**Carrie Chowske:** Yeah, that was the exact same thing Usman said.

**Carrie Chowske:** And I said, you're right.

**Carrie Chowske:** We probably should get on that.

**Carrie Chowske:** So, yeah, I agree completely.

**Carrie Chowske:** Cool.

**Carrie Chowske:** And then kind of tied into that a little bit was when I started looking at the integration pages that we've been working on.

**Carrie Chowske:** And what we're seeing is kind of these more like, I guess, a way to talk about be like niche integration pages performing quite a bit better than some of the more like flags, what we might consider flagship.

**Carrie Chowske:** Thank you.

**Carrie Chowske:** leadership topics.

**Carrie Chowske:** And that kind of means that because what's happening is we're seeing an increase in search visibility, but the clicks are kind of going the other direction.

**Carrie Chowske:** And that's not an indication of that we have poor content necessarily.

**Carrie Chowske:** We're seeing this across accounts.

**Carrie Chowske:** This is an industry-wide thing.

**Carrie Chowske:** There's a suspicion that we finally got a Google update, so that's part of it.

**Carrie Chowske:** But they're answering more of those queries via AI overviews, just like when they introduce the snippets and everything like that.

**Carrie Chowske:** It's kind of having an impact on clicks.

**Carrie Chowske:** But where we're not seeing that impact quite as much is on those more niche topics.

**Carrie Chowske:** So I think that what that says is that we should really look at some of these more emerging tool integrations and see where we can really move the needle on those.

**Carrie Chowske:** Because it's going to be harder to do with these more saturated types.

**Carrie Chowske:** These bigger, the bigger names, obviously, might make that more difficult.

**Carrie Chowske:** Doesn't mean we want to abandon those or anything or not, but that just recognizing that the more emerging frameworks that we can find and we can talk about, the better, the more that we're going to see that growth and hopefully more clicks.

**Victor Coisne:** Yeah, agreed.

**Victor Coisne:** So I think, like, it boils down to identifying new integrations candidates, right?

**Victor Coisne:** So I want to, ideally, I'd like to review that during this call, like, look at the table and see how many we have left in the pipe and see, like, if we need to do another round of identification of the integrations.

**Victor Coisne:** Because, yeah, I think there's still a lot of opportunities there.

**Carrie Chowske:** Yeah, yeah, yeah.

**Carrie Chowske:** We'll do this right now.

**Carrie Chowske:** We can take a look at that.

**Carrie Chowske:** Yeah, I think, I think we're.

**Carrie Chowske:** We're kind of in a, I think like what Usman was saying is that we're in a, we're basically running out of some things, but we do have quite a few that are approved and he's working on some of these this week.

**Carrie Chowske:** So these are the ones he's currently got in here.

**Carrie Chowske:** Looks like he's planning on delivering these.

**Carrie Chowske:** And then these are the ones that are in the queue.

**Victor Coisne:** Okay.

**Victor Coisne:** So there is quite a bit in there.

**Victor Coisne:** Uh, there, I feel like there's still some, some duplicate, um, OzZero.

**Carrie Chowske:** Yeah, that's, I was just looking at that too.

**Victor Coisne:** I think we do.

**Victor Coisne:** Yeah.

**Victor Coisne:** Well, it's, it's been acquired by Okta.

**Carrie Chowske:** Right.

**Victor Coisne:** It's probably like, maybe it's showing up as Okta and like, we have like both under Okta?

**Victor Coisne:** Um, but yeah, this is really where like Paul and Theo, like, I think you're, um, you'll, you'll, you'll.

**Victor Coisne:** Developer insights are really important and making sure you keep reading the different ecosystem newsletter to see what are some of the frameworks that are picking up.

**Victor Coisne:** I've tried to do that myself as well, but obviously I'm not a developer, so I don't have as much visibility to that.

**Victor Coisne:** So please do flag new ones.

**Paul:** Yeah, we'll keep that in mind and it'll add new ones.

**Paul:** I was going to say, if it's possible to prioritize Clerk, I'm actually just working on a project that using Clerk, so I'll be able to add some additional context to that once it's done.

**Paul:** But that'll be pretty awesome.

**Paul:** And I could like review it as well.

**Theodore Kelechukwu Onyejiaku:** Then for the declining integration pages, the ones we tagged as flagships, what date did you like?

**Theodore Kelechukwu Onyejiaku:** test.

**Theodore Kelechukwu Onyejiaku:** let's Good Well,

**Theodore Kelechukwu Onyejiaku:** Use for the filtering, like.

**Carrie Chowske:** You're talking about when we were recording these?

**Carrie Chowske:** Yeah.

**Carrie Chowske:** This was last 90 days over the previous 90.

**Carrie Chowske:** So you're looking at six months of data and kind of comparing those three-month periods across that.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Carrie Chowske:** Quarter over quarter, essentially.

**Carrie Chowske:** And it would have been.

**Carrie Chowske:** Oh, sorry.

**Carrie Chowske:** Go ahead.

**Theodore Kelechukwu Onyejiaku:** Yeah.

**Theodore Kelechukwu Onyejiaku:** Like, I think another thing we could do is how about updating them?

**Theodore Kelechukwu Onyejiaku:** Because recently I updated the next, but I think the other one still needs some updates.

**Theodore Kelechukwu Onyejiaku:** So do you think it will help to, like.

**Victor Coisne:** Yes.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And yeah, in my experience, it never hurts to update content that's been there, sitting there for a while, especially if it's not performing.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** Because so far, we've only been, like, focusing on.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** The blog posts that need updates.

**Theodore Kelechukwu Onyejiaku:** So we could also take a look at the integration pages we are handling or we are managing and update them as well.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah, I think so.

**Carrie Chowske:** Yeah, we're like one of the things that seems to be kind of moving the needle quite a bit, and this is across all of our accounts right now, is keeping up with refreshing.

**Carrie Chowske:** Because, I mean, we've known this for a while, obviously, about Google, right, that they prefer new content.

**Carrie Chowske:** But we're really seeing that to be the case with AI search.

**Carrie Chowske:** And that's really an indication there that, like, I've seen things that were published that day show up in searches, you know.

**Carrie Chowske:** So it's even more recent, and we get faster traction out of that even through AI than we do through, you know, so traditional search.

**Carrie Chowske:** So I think, you know, that's another reason, too, to come

**Carrie Chowske:** Kind of look at what have traditionally maybe been some of your, you know, top performers that have fallen maybe a little bit.

**Victor Coisne:** And those would be an opportunity as well if they haven't been updated in a while.

**Victor Coisne:** Yeah.

**Victor Coisne:** One thing that I am seeing as well is the category of hosting.

**Victor Coisne:** I think it's going to be important for us.

**Victor Coisne:** But, so, there is a, Strapi, Strapi can be hosted anywhere, right?

**Victor Coisne:** So, like, I see AWS is on the list, but, so, like, trying to see if we can maybe add some of the cooler hosting platform, like, I guess, Coolify is one of them.

**Victor Coisne:** What are some of the other popular ones?

**Victor Coisne:** Like, Railway.

**Victor Coisne:** I don't know if we have those.

**Theodore Kelechukwu Onyejiaku:** Yeah, think we have Railway already.

**Victor Coisne:** Okay.

**Carrie Chowske:** Yeah, I think.

**Paul:** We also have this blog post on Qualify.

**Paul:** wonder if that should be moved to integration.

**Victor Coisne:** don't post it here in the chat.

**Victor Coisne:** I think.

**Theodore Kelechukwu Onyejiaku:** Let me confirm.

**Theodore Kelechukwu Onyejiaku:** I think that was the one.

**Theodore Kelechukwu Onyejiaku:** Hold on, please.

**Theodore Kelechukwu Onyejiaku:** Let me check.

**Theodore Kelechukwu Onyejiaku:** Let me check.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** Yeah.

**Theodore Kelechukwu Onyejiaku:** It's the one from the author.

**Theodore Kelechukwu Onyejiaku:** That is one of the community members.

**Theodore Kelechukwu Onyejiaku:** converted his blog post to a railway integration page with Strapi.

**Victor Coisne:** Yeah.

**Theodore Kelechukwu Onyejiaku:** This is the link.

**Theodore Kelechukwu Onyejiaku:** Let me share it here.

**Victor Coisne:** Yeah.

**Victor Coisne:** Well, I just, just thinking like.

**Victor Coisne:** Um.

**Victor Coisne:** It might be good to add some couple other expert like Coolify and some other hosting providers.

**Paul:** Yeah, other providers that do Sumo services, yeah, that makes sense.

**Paul:** The question I have, Kerry, I don't recall, I don't remember, so I apologize if you've already been asked this.

**Paul:** In the past, there's a certain integration page that we manually update.

**Paul:** Do you still have that list to make sure that they don't get auto-updated?

**Theodore Kelechukwu Onyejiaku:** Yeah, I could still share it with Kerry, so she knows, she keeps the tab of them.

**Paul:** Okay, cool, thank you.

**Paul:** I just forgot about that.

**Carrie Chowske:** If you've given it to Vivek, I should have it.

**Carrie Chowske:** He's given me everything, just doesn't mean I necessarily know right where it is, but I can find it.

**Carrie Chowske:** He was pretty organized, so.

**Carrie Chowske:** Perfect.

**Carrie Chowske:** Thank you, Theo.

**Carrie Chowske:** Okay.

**Carrie Chowske:** The last thing I had in here was talking about AI visibility.

**Carrie Chowske:** We're kind of seeing, you know, quite a good...

**Carrie Chowske:** ...

**Carrie Chowske:** ...

**Carrie Chowske:** ...

**Carrie Chowske:** ...

**Carrie Chowske:** A set of data in here.

**Carrie Chowske:** They've made some additional updates for CheckBat.

**Carrie Chowske:** In terms of AI visibility, you're ahead of Contentful, Sanity, Storyblock, HighGraph as competitors, and you've got about 39% of the share of voice in AI search.

**Carrie Chowske:** Now, keep in mind, again, I think I talked about this when I demoed it, but we are predominantly tracking evaluation stage prompts.

**Carrie Chowske:** So if we wanted to broaden that, we certainly can add more prompts to that based on that, but it is those listicle type and versus type queries that we're really targeting.

**Carrie Chowske:** And predominantly because that's where those decisions are getting made, where people are finding out about brands and they're asking those questions.

**Carrie Chowske:** They're asking AI to basically look at all the crap that us in content have been doing for the last 15 years and go, okay, tell us.

**Carrie Chowske:** Tell

**Carrie Chowske:** That's the real story.

**Carrie Chowske:** And so that's why that content has been kind of the cornerstone of AI strategy.

**Carrie Chowske:** We're looking at that's one part of it, but we're seeing kind of some of the models start to kind of fight back against that and really look at the whole picture.

**Carrie Chowske:** And I think that's going to become more of a, we're going to see a resurgence of what we would call like traditional SEO best practices, where it's like, we're wanting to make sure that we're almost, almost like a reporter on ourselves, right?

**Carrie Chowske:** Like we're talking about our, about a brand that we're representing like more objectively rather than in a lot of marketing terms.

**Carrie Chowske:** But I think, I think we're doing a lot of that.

**Carrie Chowske:** think the advantage of a lot of those comparative lists is, is it allows you a moment to differentiate.

**Carrie Chowske:** And so as long as we're thinking in those terms, I don't think we're going to see any problems come up because of any content we've done in that vein.

**Victor Coisne:** Yeah.

**Carrie Chowske:** And citation shares, go ahead.

**Carrie Chowske:** I'm sorry.

**Victor Coisne:** Thank

**Victor Coisne:** Yeah, sorry to interrupt.

**Victor Coisne:** Speaking of that, I do agree that historically we've seen some good success with comparison lists and especially front-end comparison lists.

**Victor Coisne:** So what I would suggest we do is, and it's potentially a good way to, we have integration categories, right?

**Victor Coisne:** So we could do like a review of the integration within a category because then we can do a lot of cross-linking to the integration pages.

**Victor Coisne:** I'd say like, hey, like best hosting solution for Strapi and like we could like kind of review the options and obviously we would want to have Strapi Cloud like highlighted in there.

**Victor Coisne:** But I feel like same thing with Search, same thing with DAM, same thing with, I feel like it could be a good way to cross-link and, yeah, KeelTubers as well.

**Carrie Chowske:** Yeah, absolutely.

**Carrie Chowske:** And also then...

**Carrie Chowske:** And two, one of the things that I want to look at this week is for the prompts that we are tracking.

**Carrie Chowske:** Because we've been doing so much content with integrations, we should have some prompts in there related to integrations, making sure that we're covering what we're writing about so that we can track if that's getting cited in AI search as well.

**Carrie Chowske:** So I'm going to spend a little time probably later today just making sure that we've got a good breadth of that's covering the content we're creating so we can track that.

**Victor Coisne:** Cool.

**Victor Coisne:** That's great.

**Victor Coisne:** Great.

**Victor Coisne:** Just to go back to your Airtable view that you created last time, like you all set with that webhook?

**Carrie Chowske:** Yeah, I sent the webhook over to Theo.

**Carrie Chowske:** I don't know if it was implemented or not, but I gave him, we had, I had a token in there for our Airtable, so it should be catching when we publish, when you publish.

**Victor Coisne:** Theo, you're good to go with that?

**Victor Coisne:** Do I have copy side?

**Theodore Kelechukwu Onyejiaku:** Yeah, but I think I must admit.

**Theodore Kelechukwu Onyejiaku:** That, but I remember you, like, we are going to implement it, but the last ones I did, I had to add it down at the, I don't know if you saw that in the publishing table.

**Theodore Kelechukwu Onyejiaku:** I was adding down to any content I publish.

**Theodore Kelechukwu Onyejiaku:** So are you like, do you need anything from me to complete it?

**Carrie Chowske:** I just think you have to implement it on your end.

**Victor Coisne:** Yeah.

**Victor Coisne:** Yeah.

**Victor Coisne:** So you create a strapi web web on the strapi admin.

**Victor Coisne:** And then, so like every time we publish.

**Theodore Kelechukwu Onyejiaku:** I don't have access to that.

**Theodore Kelechukwu Onyejiaku:** I don't know if you recall.

**Victor Coisne:** Okay.

**Victor Coisne:** Well, then let me know.

**Victor Coisne:** I think I have the great powers of changing your permissions.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** sent, what I sent over to Theo too, is I didn't know how it, how it, um, I'm assuming that there's, it's more like a widget.

**Carrie Chowske:** .

**Carrie Chowske:** In StratBee, but I did send over raw code as well, if that's helpful, but it has the fields that we're populating in our Airtable, and then the token for our Airtable is in there as well, and I just shared it via 1Password, so.

**Victor Coisne:** All right, I have updated your permission to super admin, Theo, so.

**Victor Coisne:** Oh, don't do anything crazy.

**Theodore Kelechukwu Onyejiaku:** Yeah, yeah, yeah, I just wanted to know, like, okay, okay, I've seen it, okay, okay, okay.

**Carrie Chowske:** Do you want me, I can tag you in that Slack, that Slack message again, too, in case I got buried.

**Theodore Kelechukwu Onyejiaku:** Yeah, yeah, I probably missed it, because, yeah, I've seen it.

**Theodore Kelechukwu Onyejiaku:** Did you, like, add, is everything in the link you shared?

**Theodore Kelechukwu Onyejiaku:** Like, the JavaScript, what is good, and the, okay, it's all in there.

**Theodore Kelechukwu Onyejiaku:** Link, right?

**Carrie Chowske:** Yeah, I just shared it all in one password.

**Carrie Chowske:** So I created like a, I don't know what, what do they call them?

**Carrie Chowske:** Like it's like a note or whatever that I can share.

**Carrie Chowske:** And I gave you the token by itself, but also the tokens in the JavaScript.

**Theodore Kelechukwu Onyejiaku:** Yeah, I've seen it.

**Theodore Kelechukwu Onyejiaku:** I've seen it.

**Theodore Kelechukwu Onyejiaku:** Yeah.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** Okay.

**Theodore Kelechukwu Onyejiaku:** Thank you.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Thank you.

**Carrie Chowske:** That'll make, that'll make both our jobs easier.

**Carrie Chowske:** love it.

**Carrie Chowske:** I like being able to see what's been taken care of.

**Carrie Chowske:** That was me.

**Carrie Chowske:** I had a bunch of people out on Friday and I was trying to write up notes for my Monday updates and I was looking, was going, this air table does not look updated.

**Carrie Chowske:** I don't know what I'm looking for.

**Carrie Chowske:** So I was spent like two, so I'm glad we have that in place.

**Carrie Chowske:** Cause that'll mean I don't have to do that again.

**Carrie Chowske:** But anyway, yeah, I think that's everything that I had.

**Carrie Chowske:** We can, I'm going to be, I might, I'm thinking I'm going to be out of the office on the 24th, which would be our next, if we went bi-weekly starting with today.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Be our next sync.

**Carrie Chowske:** do you want to keep our meeting for next week and then start two weeks after that?

**Victor Coisne:** Or how do you want to handle?

**Victor Coisne:** That sounds like a plan.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Sounds good to me too.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Easy peasy.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Let me know if there's anything in the meantime that you need.

**Carrie Chowske:** I'll get started kind of looking through those prompts and make sure that we get the looker updated.

**Carrie Chowske:** I just need to, it might be end of the week.

**Carrie Chowske:** Usman took a much needed vacation.

**Carrie Chowske:** And so he's kind of like popping in to make sure he got production done and that's about it.

**Carrie Chowske:** So I'm trying to not bother him as much as I possibly can.

**Carrie Chowske:** So I'll ping him later in the week and make sure that he updates that so we can track the refreshes.

**Carrie Chowske:** But it is, the filter is there.

**Carrie Chowske:** We just need to make sure we've got all the right articles in there.

**Victor Coisne:** All right.

**Victor Coisne:** Good deal.

**Victor Coisne:** And yeah, Paul and Sue, I think like maybe the three of us should do a quick check on, you know, making sure we have enough pipe, both like on integration side and blockbust side.

**Victor Coisne:** So So

**Victor Coisne:** So, yeah, the GrowthX team has a lot to work with.

**Victor Coisne:** So, anyway.

**Paul:** I feel like from the integration pages and from the topics we just recently approved, there's got plenty of stuff to do, but we'll start thinking of additional topics outside of the ones that they recommend as well.

**Paul:** But for Theo and I, because updates are important, we are going to focus on some of the top-performing articles that we wrote that needed updates, and that's kind of what we're doing on our end.

**Victor Coisne:** Yeah.

**Victor Coisne:** That makes sense.

**Victor Coisne:** And just to make sure, it's cool if I go directly in Airtable and add those integration as I see them.

**Victor Coisne:** I just add them to the approved column.

**Carrie Chowske:** Yeah.

**Victor Coisne:** Perfectly fine.

**Carrie Chowske:** We'd love that.

**Carrie Chowske:** Yeah, we've got enough for the next couple weeks in there, so just as long as we get that, you know, yet this month, we're probably pretty good.

**Carrie Chowske:** So, you know, whatever you, however you're going to prioritize.

**Carrie Chowske:** But, yeah, if we could in the next couple weeks, just have.

**Carrie Chowske:** More topics in there for Usman to get started on.

**Carrie Chowske:** We'll be all set to go.

**Paul:** Yeah, Thea and I will do the same directly in Airtable.

**Victor Coisne:** think that makes sense.

**Victor Coisne:** And I have to ask, the access to check that coming?

**Carrie Chowske:** Yes.

**Carrie Chowske:** I know that they had a meeting about it yesterday to finalize a couple of pricing things, but that shouldn't affect your free trial access.

**Carrie Chowske:** We're giving extended trials to everybody that are current clients.

**Carrie Chowske:** I'll have to find out what that exactly is.

**Carrie Chowske:** But I think that it should happen this week.

**Carrie Chowske:** That's what I read between the lines of what I heard yesterday.

**Carrie Chowske:** So I will let you know as soon as I know for sure.

**Victor Coisne:** But I do think it's going to be this week.

**Victor Coisne:** And what about the aerobs equivalent?

**Victor Coisne:** So if we want to do...

**Victor Coisne:** as

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I heard there's some movement on that today.

**Carrie Chowske:** We were talking about in our all hands meeting this morning.

**Carrie Chowske:** So I think there's more coming on that soon too.

**Carrie Chowske:** But part of when we developed Check That, we were kind of using that opportunity to also work on that public facing component of our workflows.

**Carrie Chowske:** And so I think that moved forward significantly alongside the Check That just because we were able to test it in real time.

**Carrie Chowske:** So we created our content for Check That using it.

**Victor Coisne:** So, yeah.

**Carrie Chowske:** So I think that's coming sooner than I thought it might have been because I think we were able to stand it up alongside Check That sort of.

**Victor Coisne:** Okay.

**Carrie Chowske:** Yeah.

**Victor Coisne:** All right.

**Victor Coisne:** Sounds good.

**Victor Coisne:** I'll look forward to getting access to or like getting updates on that once you have a bit more visibility.

**Victor Coisne:** It's something that, you know, we'd love to play with.

**Carrie Chowske:** I mean, it is live, so you can.

**Carrie Chowske:** Create an account now and then it would just be a matter of us like adding on the access, like the extended trial for you.

**Carrie Chowske:** So if you want to just, you know, using your strapi email, then we know it's you and we can grant that as soon as it's available.

**Victor Coisne:** Yeah, yeah.

**Victor Coisne:** I was also talking about the content OS.

**Carrie Chowske:** Oh, yeah, yeah, That'll be a different URL.

**Carrie Chowske:** I don't know if, let's see if it's, Marcel was talking about it earlier today.

**Victor Coisne:** Yeah, I might just ping him.

**Victor Coisne:** It's been a while since I talked to Marcel, so I'll, separately, like we should discuss, like on the integration side of things, like there's a, if I remember correctly, he was thinking about open sourcing this thing.

**Victor Coisne:** So, you know, if that's still the case, I want to talk about, you know, potentially doing an integration with the content OS and thinking about how.

**Victor Coisne:** about it.

**Victor Coisne:** We can support the launch and so more of a, I don't know if it's a JSON topic or a Marcel topic, but either way, I'll just ping them.

**Carrie Chowske:** Yeah, I think if you, I think, I think ping them both.

**Carrie Chowske:** I think it's probably, yeah, it's probably going to be, they'll probably both be involved, I would think.

**Carrie Chowske:** But yeah, definitely reach out.

**Carrie Chowske:** I'm sure they would love that.

**Victor Coisne:** Yeah.

**Victor Coisne:** I mean, if it's open source, I think it makes a lot of sense.

**Victor Coisne:** Like, you know, we're open source and so, yeah.

**Victor Coisne:** Okay.

**Carrie Chowske:** Awesome.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I'll let them know.

**Victor Coisne:** Okay.

**Carrie Chowske:** Thank you so much.

**Carrie Chowske:** I'll talk to you guys next week.

**Victor Coisne:** Bye.

**Carrie Chowske:** Bye.

**Theodore Kelechukwu Onyejiaku:** Bye.
