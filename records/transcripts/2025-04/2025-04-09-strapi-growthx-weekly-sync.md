# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-04-09
time: 16:31 UTC
duration: 26 minutes
organizer: Sydney Go
participants: Sydney Go, Golzar Yaghoubpour, Theodore Onyejiaku, Jason Gong
fathom_recording_id: 56396325
fathom_url: https://fathom.video/calls/272200562
share_url: https://fathom.video/share/89DoxR3rVNBFFg6w1hVyRAwEu6DHAUrJ
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

Sydney Go walked through GrowthX's content delivery progress and analytics reporting for Strapi's Q1 content, covering 23,400 page views with 78 referring domains and 244 backlinks. The team discussed content repurposing strategy for Strapi Comp (May 13), analytics setup with Amplitude and Common Room, and internal linking priorities to boost conversion metrics—deferring detailed analysis until Victor returns and data cleanup completes (June 1).

---

## Context

Strapi is a headless CMS platform serving developer-focused companies. GrowthX has been engaged in a content marketing engagement to drive SEO visibility and conversions for Strapi through article production and analytics. This weekly sync is the standing delivery cadence between Sydney Go (GrowthX) and Golzar Yaghoubpour (Strapi) with occasional input from Theodore Onyejiaku (Strapi product) and Jason Gong (GrowthX strategy). Victor Coisne (Strapi) was traveling and absent from this call; Paul Bratslavsky was not feeling well. The team is in the onboarding and catch-up phase—Sydney joined recently—and planning a major content push around Strapi Comp, the company's flagship developer event.

---

## Relevance

- **To GrowthX Delivery:** Sydney (new to the account) is catching up on 5+ articles and documenting reporting workflows. Integration pages and internal linking are key content leverage points for the engagement. GA4/GTM cleanup arriving end of week will unlock better data consolidation in Looker Studio. Heavy conversion-focus signals demand for analytics expertise.
- **To CheckThat:** Strapi has Amplitude product analytics but data quality cleanup runs through June 1. Ungated content strategy under discussion—Strapi is exploring Common Room + Amplitude workflows to track developer intent signals without gating. This is a real-world use case for AI visibility in developer content.
- **To GrowthX Business Development:** Strapi Comp (May 13) is a major content-generation event with repurposing potential. Golzar flagged need for alignment with Paul on content prioritization before the event. Victor's return expected soon—strategy reset planned. Expansion potential: deeper collaboration on conversion tracking and content repurposing post-event.

---

## Overview

- GrowthX caught up on 5 articles and launching by next week with heavy conversion focus
- Q1 reporting dashboard shows 23,400 page views, 20,000 organic, 78 referring domains, 244 backlinks; weekly/monthly/quarterly cadence in Looker Studio
- Integration pages workflow clarified with Theodore—no template required for all integrations; Sydney to pull top 10-30 priority links for internal linking strategy
- Strapi Comp (May 13) triggers major content repurposing effort; Amplitude data cleanup delays deeper analysis until June 1; Common Room + ungated content strategy for developer audience

---

## Key Topics

### Content Production Status

Sydney reported GrowthX team catching up on all articles by end of week with new focus on conversions metrics. Five articles already uploaded to Strapi CMS. Integration pages workflow discussed—Theodore clarified that templates are not required for all integrations; he will review and update pages as needed. GA4/Google Tag Manager documentation expected from Strapi contractor by Friday or Monday.

### Reporting Dashboard and Analytics

New Looker Studio reporting dashboard in staging. Q1 metrics: 23,400 total page views (20,000 organic), 244 backlinks across 78 referring domains, keywords ranked, engagement rates. Sydney will provide weekly, monthly, and quarterly reports. Challenge: aggregating conversion events in Google Sheets—Sydney still working on formula. Ahrefs backdata limitations force quarterly pulls; April data sparse but page views/engagement accurate.

### Internal Linking Strategy and Content Improvements

Theodore requested internal linking to top integration pages—currently missing from many articles. Jason asked for Sydney to compile top 10-30 priority integration pages for systematic linking. Theodore also left comments requesting Airtable workflow instructions for AI to add new frameworks (e.g., T3 Stack) to existing articles. Sydney will follow up with Daniel (GrowthX CTO) on feasibility; if not possible via Airtable, feedback will feed into backend AI workflows.

### Analytics Tools and Conversion Tracking

Jason inquired about Amplitude/Mixpanel access. Golzar confirmed Strapi uses Amplitude but data cleanup by Strapi's data team not complete until June 1—better to revisit end of May. Meanwhile, Golzar uses HubSpot lead conversion dashboard for landing page pipeline analysis. Discussion: gated vs. ungated content for developers. Golzar explained Common Room strategy—no gating, but use engagement signals (visiting docs, clicking copy-script button) to create cohorts and track intent. Aligns with bottom-up growth strategy for 2025.

### Strapi Comp Content Strategy

Major splash event May 13 with announcements and content generation opportunities. Golzar emphasized huge repurposing potential from workshops and talks. Noted Paul owns content creation, Theodore owns product content, Golzar owns conversion and amplification. Proposed follow-up call (Paul, Sydney, Jason, Theodore) before May 13 to prioritize repurposing content and identify where AI ops can accelerate workflow. Strategy reset planned upon Victor's return.

---

## Action Items

**Sydney Go (GrowthX)**
- Stage reporting dashboard in Looker Studio with weekly, monthly, and quarterly reports including engagement rates
- Follow up with Daniel (GrowthX CTO) on feasibility of adding instructions to Airtable for AI workflow enhancement
- Compile and share top 10-30 priority integration pages for internal linking strategy across Strapi content

**Golzar Yaghoubpour (Strapi)**
- Share updated GA4 and Google Tag Manager documentation from contractor once received (expected Friday or Monday)
- Schedule call with Paul Bratslavsky, Sydney Go, Jason Gong, and Theodore Onyejiaku to align on content repurposing priorities for Strapi Comp (May 13)

---

## Transcript

**Sydney Go:** Yeah so we should be caught up with all of our articles by next week and I know that Jason is also working on digging through your strategy and seeing if there's anything that we can do to improve that as well and we're going to do a heavy focus on conversions so that moving forward instead of just page views and organic page views we can see what's working conversions wise.

**Theodore Onyejiaku:** I'm glad you're getting momentum with the hooks process.

**Theodore Onyejiaku:** Yeah I hope by next week everything should be up and running.

**Sydney Go:** That's good.

**Golzar Yaghoubpour:** I'm sorry I was running behind from another call.

**Golzar Yaghoubpour:** No worries, but Victor is out of office and Paul's not feeling too great right now so it's just going to be us.

**Sydney Go:** Okay awesome, um Jason might jump in at some point. Let me ping him just to see if he's available.

**Sydney Go:** So how are you guys doing? How's everything going?

**Golzar Yaghoubpour:** How are you doing?

**Sydney Go:** Doing good honestly, your account is massive and I'm trying to get my feet under me and figure out how to work with all the processes. So today I just wanted to give you a little update on what's happening. I've uploaded five articles to the CMS and I'm working on the integration pages.

**Sydney Go:** Theo, I actually wanted to ask you about that because Andre sent me a template that we use. For the integration pages, is there anything else that I need to know?

**Theodore Onyejiaku:** Well for now there is none. Although some integrations require templates, not all. As Victor stated, we don't need the template for all the integration pages. For now you could work with them, and later when I review and evaluate them, I could maybe make some updates.

**Sydney Go:** I'm going to share my screen just for a moment. This is where we're supposed to put the integration pages, right? Did Andre do the ideation for you or did you add them on your end?

**Theodore Onyejiaku:** We do that on our end, mostly manually. I or Paul will add them when we find an integration that's important.

**Sydney Go:** Okay, that's good to know. So there are no records right now, which is why I've kind of paused on that for a bit.

**Theodore Onyejiaku:** There should be some. I remember I left some in draft that I didn't find content for in the Strapi backend.

**Sydney Go:** I've been refreshing this view for the last few days but haven't seen anything, so maybe it's an issue on my end. I did get your Slack message with all the updates.

**Theodore Onyejiaku:** I think there's nothing in draft because I published as many as I could last week. The ones still in progress are there. I left some comments on certain items like that Apple integration.

**Sydney Go:** Thank you so much. I'll look into that and figure out what's happening with the docs.

**Sydney Go:** And then the next thing I wanted to show you is what your reporting dashboard will look like. I'm going to stage this in Looker Studio to make it look better. Moving forward we're going to track page views, organic page views, average engagement time, keywords, top keywords, and backlinks across referring domains.

**Sydney Go:** Thank you for the sheet you sent. I'm working on aggregating all your conversion events into one Google Sheet and summing them. I did this per quarter and it will look cleaner in Looker Studio. For the last quarter, across all the GrowthX articles we've done together, we have 23,400 page views, almost 20,000 organic page views, 78 total referring domains and 244 backlinks. I'm pulling quarterly data because Ahrefs doesn't do backdata. Since we're so early in April, the March data is accurate. Once I get your conversions data I'll create a quarterly report and stage it in Looker Studio.

**Sydney Go:** I was thinking about doing this weekly, monthly, and quarterly. What do you think about weekly reports?

**Theodore Onyejiaku:** From previous meetings, weekly reports with comparisons of past week and present week help show overall engagement and click-through rates.

**Sydney Go:** Okay, I'll add engagement rates and continue doing this on a weekly basis as well as monthly and quarterly. So you'll have all three cadences with all your data staged in Looker Studio.

**Sydney Go:** March data showed 10,000 page views and 9,044 organic page views. So those are the two main things on my agenda—catching you back up on content status and setting up the reporting dashboard. I'll also work on the integration pages. Outside of that, is there anything you have major concerns about or anything you want to add?

**Golzar Yaghoubpour:** I just wanted to say we have a GA4 contractor who's been cleaning up our GA4 and Google Tag Manager. She's supposed to deliver by Friday, possibly Monday with updated documentation. I'll make sure to share that with you. It will make consolidating everything a bit simpler. So just don't work too much on that because there will be changes coming in a couple days.

**Sydney Go:** Okay, awesome, good to know.

**Theodore Onyejiaku:** My concern is about adding instructions to the Airtable so the AI workflow could update drafts. There was a week when I was traveling and it came up between Paul and Victor. They wanted to introduce something to allow adding instructions. I was trying to see if I could add instructions for the workflow to add T3 Stack to the top Next.js alternative development frameworks. I don't know if that's been implemented.

**Sydney Go:** I'm going to follow up on this because I do have a request. You said you were talking to our CTO Daniel?

**Theodore Onyejiaku:** Not me exactly, but the whole team discussed it.

**Sydney Go:** Okay, I'll tag him in to see if that's possible. If not, the best course of action would be to tell me your major feedback and I can feed it into our backend AI workflows. There might be issues with adding those directly to Airtable that could break things. I'll ask Daniel to be sure.

**Jason Gong:** I don't think it's hooked up. But I wanted to clarify—are these notes for articles you've already written or things in the backlog?

**Theodore Onyejiaku:** These are articles we've already written. For instance, the "modern top frameworks for 2025" article—T3 Stack wasn't mentioned but it's one of the big ones now and trending. I'd like to add it to the list.

**Jason Gong:** I see. Well, we'll log that. We're building something where for backlog items we can comment with feedback like "make sure you include this" and resources. But for refreshing old articles, we can take a look.

**Theodore Onyejiaku:** I left comments on what I wanted to do. One other concern is that in our articles, a key thing we consider is integration pages and internal links. I've found that integration page links are missing from many articles, so I always add them myself. I'd love if they were well included—we do well with marketplace pages and Strapi plugins, but less so with integration pages.

**Jason Gong:** Do you have a top 10, 20, or 30 list of priority links that convert best? We can figure it out, but a list would help.

**Theodore Onyejiaku:** I mean the top 10 integration pages. Perhaps you could work with a list of the top 10 integration pages and check your dashboard to start using them for internal links.

**Jason Gong:** I did have a question. For Strapi, do you use Amplitude or Mixpanel or another product analytics tool we could access?

**Theodore Onyejiaku:** Yeah, we use Amplitude. Golzar can tell you more about that.

**Jason Gong:** I was wondering if we could get access. I think that would help a lot.

**Golzar Yaghoubpour:** Our data team is working on Amplitude data cleanup and won't be done until June 1st. It probably won't be very helpful until then. What specifically did you want to track in Amplitude?

**Jason Gong:** When Victor gets back, we want to take a deeper look at what SEO content converts best. For Strapi, conversion is more complicated—it's a series of events showing intent like visiting docs or clicking the copy script button. It's much easier in Amplitude to create workflows around those events and see which landing pages drive the most conversions.

**Golzar Yaghoubpour:** I think for now the data team is still cleaning up the data you're describing. Let's check back at the end of May when they're expected to be done. In the meantime, I rely on HubSpot for this. I have a lead conversion analysis dashboard that shows which landing pages generate the most pipeline. It's usually homepage or contact sales, which isn't super helpful, but it lets us reverse-engineer how people got there using GA. That might be more work than you need right now as you catch up on the account, but June 1st is a good target to start.

**Jason Gong:** Yeah, it would mostly just help us move faster. If it's not set up, no problem. I think we're prepping a strategy reset and want to look at things with fresh eyes. On a bigger note, with everything happening in the world, is there anything top of mind for you as far as marketing goes? Any new launches or initiatives?

**Golzar Yaghoubpour:** We have Strapi Comp on May 13th—a big splash event with announcements. There's going to be a lot of content coming out of it we can repurpose, reuse and recycle. Workshops and talks will be a huge undertaking. We'd love to leverage AI ops to make repurposing smoother. Paul owns content creation, Theodore owns product content, and I own conversion and amplification. It would be great to sit down with Paul outside this call to walk through priority lists for repurposing and where we can leverage AI ops. Hopefully Paul feels better next week and we can schedule a five-person call before May 13th.

**Jason Gong:** One thing I noticed—Strapi currently drives people to the open source repo. But as you move up the funnel, like HubSpot does with lead magnets, you could experiment with gated collateral.

**Golzar Yaghoubpour:** There's debate on whether to gate things for developers. But we invested in Common Room—it collects all your data points in an organized table, kind of like Clay or Mad Kudu. You create workflows to act on engagement signals. So ideally we don't gate content since developers don't like sharing info, but we create cohorts in Common Room based on engagement—like visiting pages or forking repositories—and they end up in specific cohorts. Gating doesn't always work in this industry unless it's events. For us, bottom-up growth is the main strategy this year, so Common Room and Amplitude are better bets than gating.

**Jason Gong:** That makes sense. I think that's it from our side. You'll see content from us this week.

**Golzar Yaghoubpour:** If you have any other questions as you catch up, just post them. We're happy to answer. You don't have to wait until the next call. Hopefully you're all caught up soon and I look forward to strategy planning next week.
