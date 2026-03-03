# Strapi<>GrowthX Weekly Sync

<metadata>
date: 2025-08-13
time: 16:29 UTC
duration: 14 minutes
organizer: vivek@growthxlabs.com
participants: Vivek Shankar, Mara Leighton, Paul Bratslavsky, Golzar Yaghoubpour
fathom_recording_id: 80341396
fathom_url: https://fathom.video/calls/378098142
share_url: https://fathom.video/share/bPh7VnvC9TNwpxkoi992RjR-z1MgaHzy
source: fathom
enriched_on: 2026-03-03 20:15 UTC
</metadata>

---

## Summary

Vivek Shankar provided a comprehensive update on Strapi's content strategy, SEO performance, and ongoing engineering initiatives. GrowthX has shifted to lighter, documentation-heavy refreshes at the top of integration pages and is finalizing automation workflows for comparison pages and image processing. Performance metrics show sessions have plateaued slightly below all-time highs, with Google remaining the top referral source but an uptick in LLM referrals (especially ChatGPT and Perplexity). The team identified that integration page SEO has likely peaked due to limited search volume, and discussed AI visibility strategies for general content and competitor comparison pages.

---

## Context

Strapi is a headless CMS platform, and this meeting is part of GrowthX's ongoing content marketing engagement. Vivek Shankar serves as the primary account lead from GrowthX, presenting performance analytics and strategy updates. The weekly sync structure covers content delivery workflows, performance metrics, and technical integrations. This particular week focused on finalizing documentation-heavy content refreshes, monitoring AI referral trends in light of changing search behaviors, and addressing UX inconsistencies across Strapi's integration documentation pages. Theodore Onyejiaku (a Strapi team member) was invited but absent due to illness, and Victor Coisne (another Strapi team member) was on the invite but did not participate in the discussion.

---

## Relevance

**To GrowthX Delivery:**
- Content refresh strategy has evolved toward "lighter updates" with grouped documentation links (both Strapi docs and vendor docs), indicating a shift toward modular, link-heavy content that may apply to other technical documentation clients.
- Ongoing engineering-led automation projects (comparison page generation, image workflows, publishing/staging improvements) demonstrate GrowthX's capability to scope and support platform-level content systems beyond manual publishing.
- Integration page SEO review revealed plateau despite Strapi having ~4-5 well-performing pages, suggesting keyword volume limits on technical integration content—useful benchmark for similar engagements.

**To CheckThat / AI Visibility:**
- LLM referrals increased week-over-week, with ChatGPT as top referrer and new Perplexity traffic observed. This validates AI visibility as a growing channel for developer-focused content.
- GrowthX implemented question-based H2 formatting (mimicking search queries) in general content and "Why choose X over Y?" format for competitor comparison pages—both tactics designed for LLM context window optimization.
- Integration pages show limited AI visibility opportunity because content is high-level ("integration" not "Strapi"), but general and competitor content have higher potential.

**To GrowthX Business Development:**
- Strapi account appears healthy: regular sync cadence, collaborative attitude toward UX feedback, willingness to invest in engineering automation, and data-driven approach to performance measurement (GA4, Scrunch setup).
- HubSpot access request for team@growthx.ai (Golzar to follow up with Tori) suggests potential deeper data sharing and account expansion.

---

## Overview

- Content refreshes refined: lighter updates added to top of posts with grouped Strapi and vendor documentation links for better UX
- Integration pages SEO review complete; 4-5 high-performing pages identified but overall performance plateauing due to existing keyword search volume limits
- LLM referrals trending up week-over-week; ChatGPT remains top referrer, with new Perplexity referrals appearing
- Ongoing engineering projects: comparison page automation (template-based), image workflow refinements, publishing/staging infrastructure improvements, and Octave integration automation being scoped
- AI visibility strategy adapted for general content (question-based H2s mimicking search queries) and competitor pages ("Why choose X over Y?" format)

---

## Key Topics

### Content Updates and Workflows

  - Refreshes: Lighter updates added to post tops w/ grouped doc links (Strapi + vendor)
  - New content on track; no major surprises
  - Comparison page: Engineering team working on automation flow (template-based)
  - Image workflow: In progress, style tweaks ongoing
  - Publishing/staging: Improvements ongoing; unexpected blog post issue resolved
  - Octave integration: Manual updates continuing; automation being scoped

### Performance Metrics

  - Sessions: Leveled off past 3-4 weeks, slightly below all-time high
  - Google remains top referral source
  - Non-branded impressions increasing
  - Conversion events:
      - HubSpot form events ↑
      - Contact sales & pricing links ↓
      - Month-to-month event triggers stable

### Integration Pages SEO Review

  - Content generally on-point; no major recommendations
  - Previous FAQ UX concerns reiterated
  - Inconsistent UX noted (e.g., missing header images, FAQs on some pages)
  - \~4-5 pages performing well; others limited by search volume
  - Performance likely peaked due to existing keyword search volume

### LLM Referrals

  - Week-on-week increase
  - GPT remains top referrer
  - New referrals from Perplexity observed

### AI Visibility Strategies

  - For integration pages: Limited opportunities due to content nature
  - General content: Incorporate question-based H2s mimicking search queries
  - Competitor pages: Utilizing comparison formats (e.g., "Why choose X over Y?")

---

## Action Items

**Vivek Shankar (GrowthX)**
- Resurface Slack thread re inconsistent UX on integration pages (missing header images, FAQs)

**Paul Bratslavsky (Strapi)**
- Review Vivek's Slack messages re integration pages UX inconsistencies

**Mara Leighton (GrowthX)**
- Analyze Scrunch data and report major movements to Golzar

**Golzar Yaghoubpour (Strapi)**
- Follow up with Tori re HubSpot access invite for team@growthx.ai

---

## Transcript
**Paul BRATSLAVSKY:** Good, good.

**Vivek Shankar:** You had two of your note-takers join the call for some reason, so I had to kick one out.

**Vivek Shankar:** That's so weird.

**Paul BRATSLAVSKY:** I've got to figure out what's going on with it.

**Paul BRATSLAVSKY:** It's going wild.

**Vivek Shankar:** Yeah, I think it's the first time it's happened, so it's kind of weird seeing that.

**Vivek Shankar:** It was too excited.

**Paul BRATSLAVSKY:** It was like, yeah, let's take some notes.

**Vivek Shankar:** It usually joins about within, like, 10 seconds of me joining.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Always on, though.

**Paul BRATSLAVSKY:** Hello.

**Vivek Shankar:** Hey, how's it going?

**Mara Leighton:** Pretty good.

**Mara Leighton:** How are you?

**Mara Leighton:** Pretty well.

**Mara Leighton:** Vivek and I have talked about this, but dealing with a little bit of a heat wave, so that's always fun.

**Mara Leighton:** Yeah.

**Paul BRATSLAVSKY:** Oh, look at the kitty cat.

**Paul BRATSLAVSKY:** Oh, my gosh.

**Paul BRATSLAVSKY:** Hi.

**Paul BRATSLAVSKY:** He's in and out.

**Mara Leighton:** Goelzer, what's your cat's name?

**Mara Leighton:** Just a family.

**Golzar Yaghoubpour:** Millie.

**Golzar Yaghoubpour:** Oh, you can't see her because of my filter.

**Golzar Yaghoubpour:** But if I turn off my filter, you'll see my messy background.

**Golzar Yaghoubpour:** Yeah.

**Mara Leighton:** I'm happy to see, though.

**Golzar Yaghoubpour:** I have two cats.

**Golzar Yaghoubpour:** I don't know where the other one is.

**Golzar Yaghoubpour:** She's probably just chilling by a window somewhere.

**Golzar Yaghoubpour:** Yeah.

**Golzar Yaghoubpour:** This is Millie, though.

**Vivek Shankar:** She's extra.

**Mara Leighton:** I love that she heard us talking about her.

**Mara Leighton:** Just like, yeah, let me walk around.

**Mara Leighton:** Yeah, let me let me let you know that I'm watching you.

**Mara Leighton:** Oh, my God.

**Mara Leighton:** Yeah.

**Vivek Shankar:** Amazing. Paul, what were you going to say?

**Paul BRATSLAVSKY:** I was just going say, cats take a lot of my time. I used to have cats. Now I give them back to my daughter. But the fact that I watch cat shorts for hours is probably an issue that I need help with.

**Mara Leighton:** Do they both like to hang out with you while you work, Golzar?

**Golzar Yaghoubpour:** They will come sit on my keyboard.

**Golzar Yaghoubpour:** They will chew cables, which is not so great.

**Mara Leighton:** That's a tricky one. The rest of it sounds great, but that sounds stressful.

**Golzar Yaghoubpour:** They're really sweet.

**Golzar Yaghoubpour:** Like if I, it's funny, they're like work-life backwards.

**Golzar Yaghoubpour:** If I am logged on, like past what I normally work, like Millie will come and start chewing by cable, like log off.

**Golzar Yaghoubpour:** I like that.

**Mara Leighton:** Respect.

**Mara Leighton:** She's like, I have an internal clock and we're past it. But they're great.

**Golzar Yaghoubpour:** And Paul, I don't think it's an issue to watch cat videos.

**Golzar Yaghoubpour:** They bring me joy.

**Golzar Yaghoubpour:** My whole social media feed is just cat.

**Vivek Shankar:** Yeah, I don't think videos are an issue. I mean, you know, the ancient Egyptians built temples and statues and stuff. That makes perfect sense. Thank you for the perspective.

**Golzar Yaghoubpour:** They were just way ahead of their time, and it's great like they just knew.

**Vivek Shankar:** I read somewhere that's their version of memes. They obviously didn't have any other way of doing it, so those statues are like ancient Egyptian memes.

**Paul BRATSLAVSKY:** Here's a funny thing I heard. There's all these conspiracy theories going on because a lot of historians will find these old books where they're like, "Oh, that must have been written a long time ago, so it's got to be true." But not realizing that like memes today, I'm sure there were people making sensationalized stuff. And that was supposed to be exactly like memes are today. And then historians are taking it out of context, being like, "Oh, that's exactly what they thought." Because imagine in the future, somebody finds us and they just find memes. So they're like, "Oh, what does this mean?"

**Mara Leighton:** It's essentially like reading a gossip column and being like, "See, that's all true." I think Theo is sick today. He was sick yesterday, so he's probably taking some time off.

**Vivek Shankar:** All right.

**Vivek Shankar:** So, yeah, just some quick updates regarding the refreshes from this week. We'll be sending them in with lighter updates on top of the post as we discussed. We're looking at which parts of the article need to be refreshed, and then we're essentially dropping links—either Strapi documentation or vendor documentation—and we're grouping those together so that they're useful, and we're just dropping them at the top. So do take a look at that and let us know if that works.

**Vivek Shankar:** For new content, we're on track, so no major surprises.

**Vivek Shankar:** The comparison page is in progress—the engineering team is working on the automation flow based on the template, so we should have an update there in the next couple weeks. That should be done on Friday from what I heard. And yeah, even if the automation is not fully ready, we can manually generate those and start pushing a few. Regarding the other workflows, the image workflow is in progress right now. We're just tweaking the style a little bit. Hopefully, we'll have an update to share by the end of the week.

**Vivek Shankar:** The publishing and staging is also ongoing. Apologies for the blog post that showed up out of nowhere. Kirk deleted it, and I don't think that should happen anymore. Moving forward, we're also creating the comparison page flow.

**Vivek Shankar:** For the Octave integration as well, we have a request with our engineering team to build out the automation. That's being scoped out right now. Meanwhile, we're still manually updating the artifacts to make sure everything is up to date.

**Vivek Shankar:** Moving on to the performance side of things. The number of sessions have kind of leveled off over the past three to four weeks.

**Vivek Shankar:** We're just off the all-time high, and Google remains the top referral source. No major trends or anything alarming. It seems to be one of those seasonal patterns that takes place. Things seem to be consolidating.

**Vivek Shankar:** On the non-branded impressions, they continue to increase, so there's nothing to worry about.

**Vivek Shankar:** Regarding the conversion events, HubSpot form events increased over the past week, and the contact sales and pricing links decreased a little bit. On a month-to-month basis, events are being triggered at the same levels, so no major drop-off.

**Vivek Shankar:** On the integration pages, we did a full SEO review. In terms of the content itself, things are pretty much on point. We didn't actually have any major recommendations to make other than the previous points we'd raised about the FAQ UX around it, which I think is a bit of an element issue within Strapi. That's the only recommendation at this point, though some of the other pages seem to have inconsistent UX as well.

**Vivek Shankar:** I dropped a couple examples in Slack. Some of the pages were missing header images, and some were missing FAQs. I can bring that thread up again in Slack after the call to point those out. But generally speaking, we have about four or five pages that are doing really well. The rest of them don't have much search volume connected to them. So it seems like we've hit the peak of integration-based performance based on the existing keyword search volume.

**Vivek Shankar:** With regards to LLM referrals, we increased week on week. ChatGPT was again the top referrer, and we got some referrals this week from Perplexity as well. Any questions I can answer about all of this? I've been talking for a while.

**Paul BRATSLAVSKY:** For me, at the moment, all that makes sense. If something comes up, I could let you know in Slack, but I'll look at the messages you posted on Slack and review. I know that Theodore is out, just to make sure that we keep things moving.

**Golzar Yaghoubpour:** Sorry, Vivek, I had one question before you move on.

**Golzar Yaghoubpour:** For ChatGPT being the top referrer, which tool are you pulling that from?

**Golzar Yaghoubpour:** Are you pulling that from GA or somewhere else?

**Vivek Shankar:** This is from GA4. I just wanted to double check.

**Golzar Yaghoubpour:** Excellent. Thank you.

**Vivek Shankar:** Regarding Scrunch, I think we're still setting that up, Mara?

**Mara Leighton:** We have it set up, but I would say the data is still a little early. I can share a little bit more in depth of what we're seeing week over week. I'll take a look after the call and see if anything major has moved. But typically, it tends to follow what we see from GA4. I'll take a deeper look and let you know.

**Golzar Yaghoubpour:** Great. Thank you.

**Vivek Shankar:** Just one point I wanted to clarify. The HubSpot access we discussed last week—did you send the invite to the team email? I don't think I saw it.

**Golzar Yaghoubpour:** I will double check with Tori.

**Golzar Yaghoubpour:** I did tag him, so I will follow up. It's the team at growthx.ai email.

**Vivek Shankar:** Perfect. I'll follow up with him.

**Vivek Shankar:** So that was pretty much it.

**Vivek Shankar:** That's the update for this week. Is there anything else we can answer or clarify for you?

**Golzar Yaghoubpour:** So earlier you said that the integration pages were going to be kind of like plateaued with the current keywords and strategy.

**Golzar Yaghoubpour:** And I wanted to know if you had any other suggestions based on how basically people are now going to ChatGPT for answers. Are there additional things that we can do differently either on the existing integration pages or create new ones where we're also showing up in ChatGPT or any other AI?

**Vivek Shankar:** Yeah, so in terms of the content on page itself for the integration pages, things are pretty much on point.

**Vivek Shankar:** There's a couple of factors here. To answer about LLM visibility, general guidelines are that you want to chunk the way you mention your brand and the way you associate yourself with information.

**Vivek Shankar:** That can look something like, you know, in your H2s, for example, instead of making statements, have a question, which can closely mimic what somebody is searching for.

**Vivek Shankar:** Speaking of integration pages, those opportunities are a bit low because we're not necessarily talking about Strapi, we're talking about just an integration and it's a bit more high level. On the rest of the content, there is definitely room to improve and we are doing that with our current content. That's kind of the approach we're taking.

**Vivek Shankar:** In regards to more pages, which can be programmatic, we have the competitor pages, where we have incorporated this by comparing the two tools and saying why this tool is better than that, and asking "Why should I choose this over that?" using that format. That's kind of the approach we're taking.

**Vivek Shankar:** I guess that's it, everyone.

**Paul BRATSLAVSKY:** Sounds good. Thank you. Nice to see you guys.

**Vivek Shankar:** Nice to see you too. Thanks a lot. Bye.
