# Lovable <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-20
time: 15:29 UTC
duration: 30 minutes
organizer: team@growthxlabs.com
participants:
  - name: Megan Dickey
    email: megan@growthx.ai
    affiliation: GrowthX
    role: Content Lead
  - name: Sam Vinden
    email: sam.vinden@lovable.dev
    affiliation: Lovable
    role: Content Strategy
  - name: Johanna Ydergård
    email: johanna@lovable.dev
    affiliation: Lovable
    role: Engineering/Product
  - name: Anton Osika
    email: anton@lovable.dev
    affiliation: Lovable
    role: Co-founder (invited, not present)
  - name: Marcel Santilli
    email: marcel@growthx.ai
    affiliation: GrowthX
    role: CEO (invited, not present)
  - name: George Haikal
    email: george@growthx.ai
    affiliation: GrowthX
    role: (invited, not present)
  - name: Cecilia Stallsmith
    email: ceci@lovable.dev
    affiliation: Lovable
    role: (invited, not present)
  - name: Fern
    email: fern@lovable.dev
    affiliation: Lovable
    role: (invited, not present)
fathom_recording_id: 115584204
fathom_url: https://fathom.video/calls/536817543
share_url: https://fathom.video/share/fbC5LuqCy2wt1sPfhjhsK88RuxbSPyZW
source: fathom
enriched_on: 2026-02-28 00:00 UTC
</metadata>

---

## Summary

Weekly operational sync between Lovable and GrowthX on template categorization strategy and content performance. Key outcomes: GrowthX to confirm engineering capacity for adding SEO-aligned categories to Lovable's template gallery; Megan to update Looker dashboard to surface conversion metrics alongside SEO performance. Guide production (13x impressions growth vs. November) exceeds template conversion effectiveness, prompting a production increase to 10 templates/week starting January 26.

---

## Context

Lovable and GrowthX maintain an ongoing partnership on content creation and SEO strategy. Lovable's content library drives discovery and user acquisition, while GrowthX oversees production, SEO analysis, and reporting infrastructure. This meeting addressed two critical gaps: the template gallery lacks user-facing categories based on search intent, and current reporting dashboards obscure the conversion performance of different content types. The team is also exploring how to measure Lovable's share-of-voice in AI search (AEO) as LLMs become distribution channels alongside traditional search.

---

## Relevance

**Content & SEO Strategy**
- Template categorization directly supports SEO hub page architecture
- Performance data informs production priorities (guides drive impressions; templates drive conversions)
- Prompt gap analysis identifies content opportunities where competitors rank but Lovable doesn't

**Product & Engineering**
- Template page categorization requires frontend work; backend structure partially exists
- GrowthX engineering capacity constraints; escalation path to Lovable team identified

**Metrics & Analytics**
- Reporting gaps in Looker dashboard make it difficult to connect top-funnel (SEO) metrics to bottom-funnel outcomes (signups, purchases)
- AEO tracking via Scrunch shows Lovable vs. Replit competitive positioning
- LLM referral tracking requires separate analysis layers (Looker + PowerGA)

---

## Overview

- **Template Page Categories:** Megan (GrowthX) will confirm engineering capacity for adding template categories based on Lovable's "SEO plan sheet." If GrowthX cannot prioritize, Lovable's team (Tom/Olivia) will own implementation.
- **SEO Performance:** Guides are driving 13x impressions growth (January vs. November), with continued momentum from late December onward. Guide production scales from 4/day (current) to 5/day (next week).
- **Conversion Effectiveness:** Templates significantly outperform guides at converting traffic to signups; template production increases from 5/week to 10/week starting January 26.
- **Reporting Gaps:** Current Looker dashboard conflates top-funnel (impressions/clicks) and bottom-funnel (signups/purchases) metrics. Megan will restructure to show conversion impact per content type, including separate LLM referral views for guides vs. templates.

---

## Key Topics

### Content Performance & Reporting

  - **SEO Growth:** Guide production is driving strong SEO performance.
      - Impressions are up 13x in January vs. November.
      - Clicks and impressions show significant growth since late December.
  - **Conversion Effectiveness:** Templates are more effective than guides at converting traffic into subscribers.
      - This insight, which was not immediately clear from the Looker dashboard, was discovered by Sam via separate analysis combining data from Looker and PowerGA.
  - **Reporting Gaps:** The current Looker dashboard doesn't clearly show conversion impact per content type.
      - **Required View:** A single chart showing SEO metrics (e.g., clicks) alongside a down-funnel metric (e.g., purchases, sign-ups) to directly link traffic to business outcomes.
      - **AEO Tracking:** The dashboard also lacks a clear view of how guides impact AI search (AEO).
          - **Current Method:** GrowthX tracks AEO share-of-voice against competitors (e.g., Replit) using Scrunch.
          - **New Initiative:** A "prompt gap analysis" is underway to identify prompts where competitors rank but Lovable doesn't, informing new content creation.

### Template Page Categories

  - **Goal:** Add categories to the template page to improve user experience and SEO.
  - **Implementation:** Megan will confirm if GrowthX engineering can handle the work.
      - **Rationale:** The feature may be simpler to implement than it seems, as some backend categorization already exists but is not visible on the frontend.
      - If GrowthX cannot prioritize it, Lovable's team will add it to their work log.
  - **Category Source:** The "SEO plan sheet" document will be the source for categories.
      - **Rationale:** These categories are based on keyword research and align with user search intent, creating a foundation for SEO hub pages.
      - **Examples:**
          - **App Templates:** Operations, HR, Sales, Product Management
          - **Website Templates:** Business Services, Shopping, Creative, Community

---

## Action Items

**Megan Dickey (GrowthX)**
- Confirm with GrowthX engineering on template categories; send ETA to Sam/Johanna by end of day. If blocked, escalate to Tom/Olivia (Lovable) to log in their work queue.
- Update Looker dashboard: replace impressions metric on secondary Y-axis with purchases or sign-ups. Add separate LLM-referral views for guides vs. templates to surface conversion quality.

**Sam Vinden (Lovable)**
- Email Tom to request the "SEO plan sheet" (cluster ideas/categories document); share with Megan for Airtable alignment.

---

## Transcript

**Sam Vinden (Lovable):** Hey Megan.

**Megan Dickey (GrowthX):** Hey Sam, how are you doing?

[Small talk on weekends omitted]

**Megan Dickey:** So George isn't joining us today, and I wasn't sure if Fern was going to join or be more involved in the background.

**Sam Vinden:** He's working on the technical pieces, less on the content side. We chat with him about the work we're doing with you, but he's pushing forward different technical work and the technical work for our users' apps as well. He's specializing on that side.

**Megan Dickey:** Okay, great. Well, yeah, let's start. Sam, I saw your note about the sections on the template site. I think that's definitely a good idea. I just need to sync with our engineering team to see what their capacity is and how long it might take. It feels like something we can do, but they're working on improving the tools workflow for the template so we can get production going. I don't want this to take away from that.

**Sam Vinden:** I don't know if it would be easy for you all to implement the categorical changes.

**Sam Vinden:** Johanna, do you think it's something we can do?

**Johanna Ydergård (Lovable):** We can do anything, but it's code. I don't know.

**Sam Vinden:** Megan, I think what would be great is if you give a rough estimate of if and when your team could work on that. If not, we'll ask Tom and Olivia to add it to their work log in priority order.

**Megan Dickey:** For sure. I'll sync with them today and let you know before end of day what it's looking like. There are already some categories on the backend—templates, websites, portfolios—but it's not visible on the front end. So the ingredients are already there.

**Megan Dickey:** In terms of actual categories, what would those be? We have portfolios, resumes, e-commerce, landing pages, marketing in our Airtable.

**Sam Vinden:** I didn't actually think about what exact categories would be good to have.

**Johanna Ydergård:** I think Tom has thought of a couple of categories. In the documents where you had the SEO clusters, Sam, there were categories we could share.

**Sam Vinden:** The doc's called the "SEO plan sheet."

**Johanna Ydergård:** Right, there are cluster ideas in columns C31 through 46. The top ones are app types divided by different types of teams—operations, HR, sales, product management, education, charities, communities. The second part, rows 42 through 46, is different types of websites people search for: business services, shopping, creative, community.

**Megan Dickey:** Yeah, this definitely looks like the answer. He's thinking in terms of hub pages.

**Sam Vinden:** So these are like business services, website templates, and all the different things beneath that?

**Johanna Ydergård:** Yeah, exactly. Apps and websites. Internally, Sebastian is building more apps, and we'll give creators direction on what non-website apps to build.

**Sam Vinden:** Well, Megan, can your team help us on this? If it's going to take a long time, we'll solve this ourselves and keep you updated so things are tagged correctly.

**Megan Dickey:** My bet is yes, we can do it. I'll confirm with engineering and get a timeline from them later today. Are you able to share that spreadsheet with me? I want to make sure our Airtable keywords match as closely as possible.

**Sam Vinden:** Yes, I will. Let me ask Tom if he'll share it.

**Megan Dickey:** Great. And as you know, we started ramping up guides production. Looking at the performance—specifically clicks and impressions—we're seeing a nice uptick. This is November through January 18th. Really good solid growth that amplified starting late December, especially in January. January's weekly average of impressions is 13 times November's weekly average. We've seen lots of click growth and impressions growth in the past three weeks. So far, the strategy is working, and we'll keep checking. This week we're at four guides a day, so 20 this week. Next week will be five a day. We'll keep doing that until we hit the 381 target, then go back down to 10 a week steady state.

**Johanna Ydergård:** Can I ask a question? When we're looking at impressions and clicks, do we have an idea of how this is impacting AEO? Do we have an idea of the quality of visits—are people actually reading the content?

**Megan Dickey:** Yeah, for sure. We do monthly performance reports. What we've seen is that guides and templates are driving a good number of conversions. Specifically, templates are driving more conversions than guides, which is why we felt it was important to increase templates as well. Starting next week, on the 26th, we'll move from five to ten templates a week. Let me pull up the Looker dashboard.

**Johanna Ydergård:** Yeah, I remember us having conversion tracking. What's best practice today to understand if you're ranking in AI search as well?

**Megan Dickey:** We're looking at LLM refers—ChatGPT, Claude, etc. Week-by-week breakdown December 1 through January 19. This is conversion events for guides specifically.

**Johanna Ydergård:** So that's visits to guides overall. Do we have an idea of LLM referrals for guides versus templates?

**Megan Dickey:** I'm interested in seeing that too, but it's sort of Sam's area.

**Johanna Ydergård:** I just find it interesting since this is very SEO-skewed content. Do people actually read it, or are we driving traffic? We have very poor AEO at the moment.

**Sam Vinden:** Yeah, I know what you're getting at, Jana. When I spent time between Christmas and New Year looking deeper at templates versus guides—the conversion of traffic going to each—I found templates were higher performing in driving conversions. That's why we've pushed to get more templates as a share of total content creation.

**Sam Vinden:** Megan, I'd say it's not easy to digest from the Looker Dashboards right now. It took me analyzing separately from that dashboard to get the answer: what is the higher impact work here?

**Megan Dickey:** So you're finding it hard to see how guides are performing across SEO, AEO, and conversion all together?

**Sam Vinden:** The question I wanted to answer between Christmas and New Year was: it seemed we were driving progress on SEO and AEO, but what return were we getting on driving new Lovable subscribers? Were different work streams doing better than others? The Looker Dashboard isn't hard to use, but I couldn't immediately take away the answer. I had to look at the Looker Dashboard and PowerGA and various things to get a sense of it.

**Megan Dickey:** Okay, so you mean within SEO—what was driving SEO growth, both from traffic and from conversion perspective?

**Sam Vinden:** Right. Does that make sense?

**Megan Dickey:** Yeah, let me share my screen. There are so many ways to configure this dashboard. I'm trying to understand specifically what I need to change to make it easier for you.

**Sam Vinden:** I think what I would do is change the right-hand Y-axis from impressions to purchases or sign-ups—some down-funnel metric.

**Johanna Ydergård:** Yeah.

**Megan Dickey:** You want it all on one chart?

**Sam Vinden:** That would be easier.

**Megan Dickey:** This is specific to guides, but I see what you mean. We could put key events versus purchases. But I'm not totally sure how that's set up in GA4.

**Sam Vinden:** I don't know either, to be honest.

**Johanna Ydergård:** My point was: we can look at traffic guides drive and conversion from guides. But it's also an indirect effect. If guides improve AEO, people don't go to guides at all. They end up on lovable.dev and buy from ChatGPT telling them to. But the guides made that happen.

**Megan Dickey:** I see. Just tracking traffic to guides is flawed. You want to make sure we're capturing the impact of guides and templates—specifically how guides inform LLM rankings.

**Johanna Ydergård:** Yeah. In my previous company, I built an app that ran a prompt 100 times to see what share of answers mentioned Lovable. But that seems over the top. Are there tools to track if this improves?

**Megan Dickey:** We also look at Scrunch—tracking how Lovable compares to competitors. We dive into that in monthly performance reports. Replit has the highest share, but Lovable comes next. We're tracking how Lovable performs against certain prompts broken down by topic—no code web app development, building a page with AI. I'm doing a prompt gap analysis, looking at prompts where Replit ranks and Lovable doesn't, then backing into what's being cited and creating similar Lovable content. I can poke around the Looker dashboard and try to get it all in one place and show guides and templates performance for LLM refers to make it more digestible.

**Johanna Ydergård:** Cool.

**Megan Dickey:** Okay, I guess we're running low on time. Anything else you wanted to talk about?

**Sam Vinden:** I don't think so. We're chatting with a technical writer to start that conversation so she can produce high-quality content complementing what GrowthX is doing on a broader spectrum.

**Megan Dickey:** That sounds good. So we'll continue four guides a day this week, and on Monday, we'll start with ten templates a week. I'll get back to you by end of day on the categories for the template page, and I'll start improving the Looker dashboard. Let me know when you can take another look.

**Sam Vinden:** Great, cool. All right.

**Megan Dickey:** Thank you. Thanks so much. Take care, y'all. Bye.
