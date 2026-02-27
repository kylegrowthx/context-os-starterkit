# Strapi <> GrowthX -  Weekly Sync

<metadata>
date: 2026-02-10
time: 17:29 UTC
duration: 33 minutes
organizer: Carrie Chowske (GrowthX)
participants:
  - Victor Coisne (Strapi)
  - Paul Bratslavsky (Strapi)
  - Theodore Kelechukwu Onyejiaku (Strapi)
  - Carrie Chowske (GrowthX)
  - Usman (GrowthX)
fathom_recording_id: 121257882
fathom_url: https://fathom.video/calls/561182213
share_url: https://fathom.video/share/5pRCVzTAM_1xr5SjqtTowBNBRUiv6Xr9
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

Carrie presented strong performance data: content refreshes generated ~70k organic sessions with 45% QoQ growth, while niche integration pages (Clerk, Coolify, Railway) significantly outperformed flagship topics, suggesting AI Overviews are cannibalizing broad keyword traffic. The team agreed to scale refreshes and prioritize emerging tool integrations, shift syncs to bi-weekly, and automate Airtable tracking via Strapi webhook to reduce manual overhead.

---

## Context

Strapi and GrowthX collaborate on content strategy for Strapi's open-source CMS. This is a recurring weekly sync between Victor Coisne (Strapi), Paul Bratslavsky and Theodore Kelechukwu Onyejiaku (Strapi developers), and Carrie Chowske with Usman from GrowthX. The meeting reviews SEO performance metrics, content production pipeline, and operational improvements. GrowthX uses AI visibility tools (CheckBat/CheckThat) to measure Strapi's share of voice against competitors like Contentful, Sanity, and Storyblock in evaluation-stage search queries.

The discussion reflects broader content marketing trends: Google's recent algorithm updates favor fresh content, and AI search (Claude, ChatGPT) is dramatically reshaping traffic distribution. Niche integration topics attract high-intent users when broad keyword pages get answered directly in AI Overviews. The team is also exploring Strapi's Content OS as a potential open-source launch, with GrowthX positioning to support go-to-market strategy.

---

## Relevance

- **Content Strategy & SEO**: Data-driven evidence that content refreshes and niche topics outperform flagship pages; AI search fundamentally changes keyword targeting
- **AI Visibility & Competitive Analysis**: Strapi's 39% share of voice in evaluation-stage queries; competitive benchmarking vs. Contentful, Sanity, Storyblock, HighGraph
- **Operations & Tooling**: Airtable webhook automation, Looker analytics filtering, CheckBat trial access, Content OS integration exploration
- **Product-to-Market Fit**: Integration pages (Clerk, Coolify, Railway) signal developer-centric demand; emerging frameworks outperform legacy tools
- **Team Coordination**: Bi-weekly cadence shift, asynchronous Slack updates, direct Usman-Theo communication reducing bottlenecks

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

## Action Items

**Theodore Kelechukwu Onyejiaku (Strapi)**
- Share list of manually updated integration pages w/ Carrie
- Implement Strapi webhook to Airtable w/ Carrie's payload (granted Super Admin access by Victor)
- Add integration/blog topics to Airtable for Usman

**Carrie Chowske (GrowthX)**
- Add integration-related prompts to AI visibility tracking
- Ping Usman to update Looker refresh filter; confirm coverage
- Confirm CheckThat extended trial details; update Victor
- Notify Marcel + JSON (GrowthX) re: Victor's outreach

**Victor Coisne (Strapi)**
- Add integration/blog topics to Airtable for Usman
- Create CheckThat account w/ Strapi email for extended trial
- Email Marcel + JSON (GrowthX) re: Content OS; explore integration/launch support

**Paul Bratslavsky (Strapi)**
- Add integration/blog topics to Airtable for Usman
- Prioritize Clerk integration (currently using it in a project)

---

## Transcript

**Victor Coisne:** This meeting is being recorded.

**Paul Bratslavsky:** Hey, Victor. I went to the coffee shop this morning—needed to get out of the house. It's within walking distance, so it's a nice walk. Beautiful day.

**Victor Coisne:** You don't have a co-working space near you guys?

**Paul Bratslavsky:** Not next to us.

**Victor Coisne:** But this works well. Looking at the data they sent... Oh, hi, Carrie.

**Carrie Chowske:** Hello. How are things going?

**Victor Coisne:** Things are going pretty well. How about you?

**Carrie Chowske:** I'm doing great. I was trying to find the agenda on my desktop—finally got it. I'm sorry I was late sending it; I thought I hit send and it was stuck in draft. But we should be good. Usman was out of office, but he popped in this morning and gave me a rundown. Theo just approved a bunch of Next.js topics, so we're good there. We're kind of running out of approved topics though. That might depend on what we talk about with refreshes and integration pages. There's also a pause on editorial with a few approved titles on hold.

**Victor Coisne:** Sounds good.

**Carrie Chowske:** For Looker, the refresh filter was added, but I'm not 100% sure all our refreshes are in there. I pulled some data manually using Search Console and GA4. Usman flagged a couple of refreshes he'd done recently with strong week-over-week traffic. I also wanted to ask how you'd feel about going bi-weekly for our meeting cadence. We'd focus more on performance and strategy, with production updates handled in Slack. We'd have more time for deeper performance reporting.

**Victor Coisne:** As long as we keep momentum and don't stall production through Slack back-and-forth, I'm fine with bi-weekly.

**Carrie Chowske:** It won't affect production. Usman's been communicating directly with Theo on finer details, which helps—no telephone game. That's worked really well this week. Now for performance: refresh content is driving about 70,000 sessions, roughly 45% QoQ growth, looking at organic and referral traffic. I manually pulled data on some refreshes. We saw 48% growth and 42% engagement increase on "best JavaScript frameworks," and 144% growth with 173.5% engagement increase for "open source CMS platforms."

**Victor Coisne:** That's exciting. We should keep scaling refreshes. It's obvious they're driving organic traffic, LLM traffic, and citations. We have a lot of outdated content.

**Carrie Chowske:** Exactly. Usman said the same thing. When I looked at integration pages, niche ones are outperforming flagship topics. We see increased search visibility but clicks going the other direction—industry-wide issue. Google probably released an update. AI Overviews are answering broad queries directly, similar to featured snippets. But niche topics aren't seeing that impact as much. We should focus on emerging tool integrations and hosting providers. Auth0 is a duplicate of Okta and should be removed.

**Victor Coisne:** Agreed. It boils down to identifying new integration candidates. I'd like to review the table and see how many are in the pipeline and if we need another identification round.

**Carrie Chowske:** We're running out of some things, but we have quite a few approved and Usman is working on some this week. These are ones he's currently working on, and these are in the queue.

**Victor Coisne:** There's quite a bit there, but I feel like there are still some duplicates. Is that Auth0? It's been acquired by Okta. We might be showing it as Okta and having both. Paul and Theo, developer insights are really important. Keep reading ecosystem newsletters to see what frameworks are picking up. Please flag new ones.

**Paul Bratslavsky:** We'll keep that in mind. If possible, prioritize Clerk—I'm actually working on a project using it and can add context once it's done. I could review it as well.

**Theodore Kelechukwu Onyejiaku:** For the declining flagship integration pages, what date filter did you use?

**Carrie Chowske:** Last 90 days over the previous 90, so six months of data comparing three-month periods. Quarter-over-quarter essentially.

**Theodore Kelechukwu Onyejiaku:** I think another thing we could do is update them. I recently updated Next.js, but the others still need updates. Would that help?

**Victor Coisne:** Yes.

**Carrie Chowske:** Absolutely. Updating old, underperforming content always helps. Refreshing is moving the needle across all our accounts. Google prefers fresh content, and AI search even more so. I've seen content published that day show up in searches. So refreshing top performers that have fallen is an opportunity.

**Victor Coisne:** Exactly. One thing I'm seeing: hosting is going to be important. Strapi can be hosted anywhere. AWS is on the list, but maybe we should add cooler hosting platforms like Coolify and Railway. Do we have those?

**Theodore Kelechukwu Onyejiaku:** Yeah, we have Railway already.

**Paul Bratslavsky:** We also have a blog post on Coolify. Should that be moved to integration?

**Theodore Kelechukwu Onyejiaku:** Let me check. I think it was converted from a blog post to a Railway integration page with Strapi by a community member.

**Victor Coisne:** It might be good to add a couple of other hosting experts like Coolify and other providers.

**Paul Bratslavsky:** Do you still have that list of integration pages you manually update? Just want to make sure they don't get auto-updated.

**Theodore Kelechukwu Onyejiaku:** Yeah, I can share it with Carrie so she knows to keep track of them.

**Paul Bratslavsky:** Thanks. I just forgot about that.

**Carrie Chowske:** If you gave it to Vivek, I should have it. He gave me everything, though I might need to find it. He was pretty organized.

**Victor Coisne:** On the Airtable webhook, are you all set with that?

**Carrie Chowske:** I sent it over to Theo. I'm not sure if it was implemented, but I gave him the token for our Airtable. It should catch when you publish.

**Victor Coisne:** Theo, you good to go?

**Theodore Kelechukwu Onyejiaku:** We're going to implement it, but I had to add it manually to the publishing table. Do you need anything from me to complete it?

**Victor Coisne:** You create a Strapi webhook on the Strapi admin, and every time you publish, it triggers. Theo, you need admin permissions.

**Theodore Kelechukwu Onyejiaku:** I don't have access.

**Victor Coisne:** Let me know, and I can change your permissions.

**Carrie Chowske:** What I sent to Theo is raw code with the fields we're populating in Airtable and the token. I shared it via 1Password.

**Victor Coisne:** I've updated your permission to Super Admin, Theo. Don't do anything crazy.

**Theodore Kelechukwu Onyejiaku:** Thanks. I've seen everything.

**Carrie Chowske:** That'll make both our jobs easier. I'll get started on the prompts and make sure we get Looker updated. Usman's on a much-needed vacation, so I'm not going to bother him too much. I'll ping him later in the week to update the refresh filter. The filter is there; we just need all the right articles.

**Victor Coisne:** Paul and I should do a quick check on ensuring we have enough in the pipeline for integration and blog topics.

**Paul Bratslavsky:** From integration pages and recently approved topics, there's plenty to do. Theo and I will focus on updating top-performing articles that need updates.

**Victor Coisne:** That makes sense. Can I add integration topics directly in Airtable to the approved column?

**Carrie Chowske:** Yeah, we'd love that. We have enough for the next couple weeks, so if you could get more topics in there for Usman in the next couple weeks, we'll be all set.

**Paul Bratslavsky:** Theo and I will do the same directly in Airtable.

**Victor Coisne:** Is CheckThat access coming?

**Carrie Chowske:** Yes. They had a meeting yesterday to finalize pricing, but that shouldn't affect your free trial. We're giving extended trials to current clients. I'll find out exactly what that is, but I think it happens this week.

**Victor Coisne:** And the AEO equivalent?

**Carrie Chowske:** There was some movement on that today. We talked about it in our all-hands this morning. When we developed CheckThat, we also worked on the public-facing component of our workflows alongside it, and we tested it in real time. We created our content for CheckThat using it, so it's coming sooner than expected.

**Victor Coisne:** I'd love to play with that once we have more visibility.

**Carrie Chowske:** It's live now. You can create an account using your Strapi email, and we'll add the extended trial access as soon as it's available.

**Victor Coisne:** What about the Content OS?

**Carrie Chowske:** That'll be a different URL. Marcel was talking about it earlier today.

**Victor Coisne:** I'll ping him. We should discuss whether we can do an integration with the Content OS on launch. If it's open source, we should think about how to support the launch. I'll contact both Marcel and JSON.

**Carrie Chowske:** Ping them both. They'll probably both be involved. They'd love to hear from you.

**Victor Coisne:** If it's open source, it makes sense. We're open source too.
