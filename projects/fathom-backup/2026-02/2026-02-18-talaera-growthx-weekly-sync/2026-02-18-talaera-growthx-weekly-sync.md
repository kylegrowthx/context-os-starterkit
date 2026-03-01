# Talaera <> GrowthX - Weekly Sync

<metadata>
date: 2026-02-18
time: 17:00 UTC
duration: 19 minutes 9 seconds
organizer: Aida Knezevic (GrowthX)
participants:
  - Aida Knezevic (aida@growthx.ai, GrowthX)
  - Anita Anthonj (anita@talaera.com, Talaera)
  - Mel MacMahon (mel@talaera.com, Talaera)
  - Paola Pascual (paola@talaera.com, Talaera)
  - William Leborgne (william@growthx.ai, GrowthX)
  - cc: Kathy Lam (kathy@growthx.ai, GrowthX)
fathom_recording_id: 123389117
fathom_url: https://fathom.video/calls/570059801
share_url: https://fathom.video/share/kxK-PNxUiam7mfCHhzduu-fYUY_xWxwZ
source: fathom
enriched_on: 2026-02-27T17:30:00Z
</metadata>

---

## Summary

Talaera's new content achieved 200+ clicks from Google Search within weeks of launch, signaling strong early performance and fast indexing. A GA4 data discrepancy was identified—tracking only 80-90 clicks versus 200+ in Google Search Console—likely caused by CookieBot's recent implementation blocking cookie consent. GrowthX will investigate the GA4/CookieBot conflict while Talaera prioritizes the final 5 blog articles for B2B and customer support topics; Aida transitions to delivering a Phase 1 summary report before handing off account management to a dedicated long-term growth manager.

---

## Context

This is the Phase 1 checkpoint meeting for Talaera's SEO and content visibility engagement with GrowthX, taking place at week six of an eight-week sprint. Talaera is an English language training and corporate communication platform serving B2B and international teams. GrowthX executed a rapid content launch strategy—publishing content fast and measuring results in real time using Google Search Console, GA4, and proprietary AI visibility monitoring. The engagement focuses on proving content velocity and early performance before the account transitions to a dedicated long-term manager for Phase 2. Key dependencies include resolving the GA4 tracking issue and securing Amplitude funnel analytics access to better understand user behavior.

---

## Relevance

- **Content Strategy & SEO:** Early validation of rapid publishing approach; decision to prioritize B2B/customer support content over remaining generalist topics
- **Analytics & Data Quality:** Critical GA4/CookieBot conflict investigation impacts future performance reporting and business decision-making
- **AI Visibility Monitoring:** Introduction of proprietary bottom-of-funnel prompt tracking to measure content presence in AI model responses—novel for GrowthX client work
- **Account Handover & Continuity:** Phase transition demonstrates GrowthX's engagement model: intense sprint phase (launch & measurement) followed by managed long-term optimization phase
- **Cross-functional Coordination:** Identifies tech debt (GA4 config, CookieBot integration) requiring Talaera dev team (Victor) involvement to resolve

---

## Overview

- **Strong Early Performance:** New content is performing well, with \>200 clicks from Google Search in under a month.
- **GA4 Data Discrepancy:** GA4 traffic data is significantly lower than Google Search Console (GSC) data, indicating a tracking error likely caused by the recent CookieBot implementation.
- **Content Strategy Shift:** Talaera requested prioritizing the 5 remaining blog posts for B2B and customer support topics to align with current business goals.
- **Phase 1 Wrap-up:** Aida will deliver a summary report with Phase 2 recommendations before handing off the account to a new GrowthX manager.

---

## Key Topics

### GA4 Data Discrepancy

  - **Problem:** GA4 traffic data is significantly lower than GSC data for the same period.
  - **Cause:** GA4 shows a "Google tag code isn't configured correctly" error.
      - **Hypothesis:** The error is likely caused by the recent CookieBot implementation, which may be blocking GA4 from collecting data until a user accepts cookies.
  - **Impact:** Inaccurate GA4 data hinders a full understanding of content performance across all traffic sources (organic, referral, direct).
  - **Resolution:**
      - Aida will ask the GrowthX team to investigate the GA4/CookieBot conflict.
      - Mel suggested Victor (Talaera) may have relevant technical context.
      - **Note:** Amplitude remains the primary source for funnel tracking, which is more critical for business metrics.

### Content Performance & Strategy

  - **Early Results:** Content is indexing fast and generating strong initial traffic.
      - **Performance:** \>200 clicks from Google Search in under a month.
      - **Top Performers:** Broad topics ("how to sign off an email") and "alternatives" articles.
  - **Strategy Adjustment:** Talaera requested prioritizing the 5 remaining blog posts for topics relevant to B2B and customer support.
  - **AI Visibility Tracking:**
      - **New Prompts:** 50+ bottom-of-funnel prompts (e.g., "best corporate English training platforms") were added to the proprietary monitoring tool.
      - **Rationale:** This tracks AI visibility for high-intent keywords where AI models may not cite external sources, ensuring Talaera's content is still seen.
      - **Tool Access:** Mel has an invitation to the tool, which shows Talaera's "best prep alternatives" article is cited \>30 times.

### Phase 1 Wrap-up & Handover

  - **Phase 1 Summary Report:** Aida will deliver a report covering:
      - Project overview & artifacts
      - Early performance results
      - Recommendations for Phase 2
      - A case study of another client's long-term traffic growth
  - **Handover Process:** Aida will hand off the account to a new GrowthX engagement manager for Phase 2.
      - **Rationale:** The new manager focuses on long-term performance, iteration, and topic refinement.
      - **Continuity:** The new manager is already familiar with the project's process and goals.

---

## Action Items

**Aida Knezevic (GrowthX)**
- Prioritize next week's 5 blog articles to focus on B2B and customer support topics (align with Talaera's current business goals)
- Request GrowthX team investigation into GA4/CookieBot conflict; coordinate with Mel MacMahon and Victor (Talaera dev) on root cause and remediation
- Collect email addresses from GrowthX team and send to Mel MacMahon for Amplitude funnel analytics access provisioning
- Research Amplitude's AI visibility monitoring capabilities; compare findings with CheckThat's LLM referral tracking approach
- Draft and deliver Phase 1 summary report to Talaera team covering project overview, performance results, Phase 2 recommendations, and competitor case study example
- Send Slack follow-up to Talaera team with takeaways and next steps

**Mel MacMahon (Talaera)**
- Provide Amplitude funnel analytics access once email addresses are received from GrowthX
- Accept invitation to GrowthX's proprietary AI visibility monitoring tool and review Talaera's content citation data

**Victor (Talaera)** (implied, not on call)
- Investigate and resolve GA4 tag code configuration issue; assess CookieBot implementation's impact on data collection

---

## Transcript (Cleaned)

_[Aida shares screen to show proprietary AI monitoring tool]_

**Aida Knezevic:** They don't have any data yet—it's collecting. But I also just added a couple of new bottom-of-the-funnel prompts, like "best corporate English training platforms for international teams." And then the ones related to target keywords, for example, "what are the best ways to practice business English speaking" or "what software engineering English terminology should developers know."

For this type of content, the chances are higher that some AI models might not cite other websites. But we still want to make sure. Perplexity, for example, always cites different websites. So we still want to track these types of prompts. Granted, once data starts coming in, the overall visibility across competitors is probably going to go down because we're tracking prompts that aren't very bottom of the funnel. Just want to note that.

Before we jump in, anything you want to discuss?

**Anita Anthonj:** Nothing on our side?

**Paola Pascual:** [Implied—no, I saw the next blog post.]

**Anita Anthonj:** Next week we'll still have five more?

**Aida Knezevic:** Exactly. Yeah.

**Anita Anthonj:** Would you be able to prioritize only the ones that fit—things for B2B and/or customer support?

**Aida Knezevic:** Yeah, yeah, we can prioritize that.

**Anita Anthonj:** I don't want to force anything, but I know we have a lot of content. So if it can go in that direction, then great.

**Aida Knezevic:** This is a great result, and it's not something I see that often at this stage of the sprint. You've been very fast to review content, we've been publishing very fast. I wish I could show this every time a client says "maybe we should check this before we publish." I'm like, no, let's just publish so you can see the data, then we can start learning from it and getting signals.

Overall, we have over 200 clicks in just under a month of publishing, which is great. The articles that are more broad—like "how to sign off a professional email," "how to disagree"—those are getting a lot of clicks. Even the alternatives articles are doing well.

Now, there's a tracking issue with GA4. The data from Google Search Console is just from Google Search. So if you have 200+ verified visitors from Google Search, Google Search Console is pretty trustworthy. GA4 data has to be higher, especially because it's tracking not just organic search traffic but also referral, direct, everything.

When I went into your GA4 property, it said "the Google Tag Code isn't configured correctly." GA4 is sometimes tricky because of cookie policies. If an extension on your website blocks GA4 from being activated before somebody accepts cookies, that interferes with tracking. I just wanted to put this on your radar—I don't think it's collecting all the data from your website.

**Anita Anthonj:** Is that something we can fix, Mel?

**Anita Anthonj (to implied Paola/others):** Mel should be here in a moment.

**Paola Pascual (implied):** I was actually going to ask—is this something you could help us with? In the past, we had some issues with GA4 that said Google Search Console was kind of blocking stuff. I can't remember how we solved it, but it'd be great. I'm sure there's something that's not right. Did you get to talk to Mel?

**Aida Knezevic:** Typically we don't do deep code investigations, so we haven't done this before. But I can ask if someone can just double-check what the potential issue is. Typically, the tag code is straightforward to set up. I'll ask around the GrowthX team to see if someone can take a quick look.

**Paola Pascual (implied):** That'd be super helpful.

**Aida Knezevic:** Yeah, once you figure out the Google Tag, the data is going to be a lot clearer. But I just know that if you want to follow GDPR, you can't let GA4 collect data without consent. They have to click yes. We had a client with a cookie compliance popup that was interfering with data tracking.

Sometimes companies don't use GA4—they might use PostHog, which allows you to collect data that isn't super identifiable (doesn't collect IP addresses). Analytics is a whole other beast. It's not always straightforward when it comes to performance tracking.

**Paola Pascual (implied):** We did start using CookieBot for GDPR opt-in. That was about a month ago.

**Aida Knezevic:** Ah, okay. That's good to know. That's probably what it is. But we'll see.

At the end of the day, you use Amplitude for funnel tracking, and that's more important than GA4.

Let me just take a look at this report. Yeah, this one's only captured one session so far.

The TLDR is we're doing really well in Google Search. All the articles are being indexed super fast. Those are all really positive signals.

_[Mel MacMahon joins]_

**Mel MacMahon:** Hi, how's it going?

**Aida Knezevic:** Good. We were just talking about GA4 data. It appears not all traffic data is being collected on the site. When I logged into your GA4 property, it says the Google tag code isn't configured correctly. Paola mentioned you do have a CookieBot compliance plugin. I was wondering if maybe you knew if that's the reason why this is misconfigured.

**Mel MacMahon:** I'm not sure. I don't know much about CookieBot. You'd have to ask Victor. I think he was the one who installed it. I'm not much help here—I haven't looked at either GA4 or the CookieBot.

**Aida Knezevic:** No worries. We'll look into the configuration.

Mel, I'm going to follow up on Amplitude access. Two weeks ago, you mentioned you could get us access. Is it okay if you give access to our team account or does it have to be a specific person?

**Mel MacMahon:** I think they go based on emails.

**Aida Knezevic:** Okay. If you have email addresses, I can have those.

**Mel MacMahon:** I'm not sure if you already provided them, but yeah, if you have emails, I can set that up.

**Aida Knezevic:** All right, perfect. I'll follow up with emails.

And the new prompts—50+ new prompts. I added them to CheckThat, so you should see data come in within the day. These are the articles we're working on this week.

**Mel MacMahon:** Aida, are you familiar with Amplitude's AI monitoring capability?

**Aida Knezevic:** No, I don't think any of my clients are using Amplitude for that.

**Mel MacMahon:** In that case, nevermind. I was curious if it was similar to CheckThat.

**Aida Knezevic:** Well, what we do with CheckThat is track referral traffic from different LLMs. That's hard data. But I'll look into what Amplitude does and see how it compares.

For next week, we'll work in the articles Paola mentioned.

Since we're in week six, at this stage, I typically prepare a summary document of everything we've done so far—early results, recommendations for Phase 2. If there's any particular insight you'd like me to add, let me know. It's an overview of everything we've covered, all artifacts, early results. I typically provide an example from an existing customer who's been publishing since October, so you can see long-term how traffic plays out.

You can click on a prompt, see the AI response, and click through to see how it compared you to different competitors. So it allows us to monitor your visibility.

**Mel MacMahon:** You just add representative prompts there?

**Aida Knezevic:** Yes. If you go to "sources" and type in your domain name, you can see which pages are getting cited in those prompts the most. For example, the "best prep alternatives" article is being picked up quite often—it's been cited over 30 times, as well as other alternatives content.

**Mel MacMahon:** This is one of your proprietary tools, right? Not some external service?

**Aida Knezevic:** Yes, it's proprietary. You have access. I think I invited you—you might not have accepted yet. You have an invitation in your inbox. If it doesn't work, I can resend it.

I'll be in touch with the Phase 1 summary soon, and I'll provide recommendations for Phase 2.

Overall, I feel really good about the results so far. On a personal level, it's been great to work with you. For Phase 2, a different engagement manager takes you on because they really focus on long-term performance, constantly measuring and iterating on results and tweaking topics. It's always a bit hard for me when I find a client I work with really well and it's so smooth—it's a little bittersweet to hand you off to our growth team.

**Anita Anthonj:** Yeah, you've been great to work with, Aida.

**Aida Knezevic:** No, totally. Most of the long-term engagement managers have worked with me in the sprint, so they know what this process looks like and what you've been through. Once you're on their team, we all work for the same company, so we can work together on anything that comes up. But yeah, it's been really fun.

**Anita Anthonj:** We still have two more weeks to go.

**Mel MacMahon:** Sweet.

**Aida Knezevic:** I'll send a follow-up in Slack once I get out of these meetings. In the meantime, if you have any questions, just drop me a message.

**Anita Anthonj:** Awesome. Thank you so much, Aida.

**Paola Pascual (implied):** Thank you so much.

**Aida Knezevic:** Thank you. See you next week. Bye.
