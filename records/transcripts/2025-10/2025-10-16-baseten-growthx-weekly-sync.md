# Baseten <> GrowthX - Weekly Sync

<metadata>
date: 2025-10-16
time: 16:00 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Aida Knezevic (GrowthX), Andi Bailey (GrowthX), Sydney Go (GrowthX), Mike Bilodeau (BaseTen), Marylise Tauzia (BaseTen), Kenzie Amack (BaseTen)
fathom_recording_id: 94696210
fathom_url: https://fathom.video/calls/441982290
share_url: https://fathom.video/share/Rzwe6pA8V6YYH12HBsohXxDGqcN_ueaD
source: fathom
enriched_on: 2026-03-02 16:45 UTC
</metadata>

---

## Summary

GrowthX and BaseTen reviewed critical improvements to content accuracy processes after initial outlines had factual errors—introducing expert review by BaseTen's CTO Daniel, constraining data sources to verified documentation, and adding manual fact-checking against each claim. BaseTen emphasized that LLM training data is too outdated (last updated June 2024) for fast-moving AI industry commentary, so they need high-confidence content with aggressive editorial oversight. GrowthX committed to delivering a conviction matrix showing which content types they can confidently produce and exploring off-site publishing options to influence LLM rankings, since independent third-party sources carry more authority than vendor content.

---

## Context

BaseTen is an AI inference platform—a core part of GrowthX's content marketing engagement. This weekly sync follows up on content outlines that GrowthX delivered the previous week, which contained factual errors (e.g., incorrect information about NVIDIA hardware). Mike Bilodeau (VP of Growth at BaseTen) and Marylise Tauzia (leading content strategy) flagged that these were not expert mistakes but basic information lookup failures, raising concerns about whether GrowthX's LLM-driven processes could reliably produce high-quality content for a technical audience in a rapidly evolving space. The core problem: LLMs trained on June 2024 data lack the recent information needed for accurate content about AI infrastructure, yet online sources are often low-quality or outdated. GrowthX and BaseTen are working through how to calibrate processes—especially human review and fact-checking—to maintain BaseTen's brand authority while leveraging GrowthX's content production capabilities.

---

## Relevance

**To GrowthX Delivery:**
- Content accuracy is now a critical service differentiator—adding domain expert review (e.g., CTO sign-off) significantly increases confidence but requires longer timelines and deeper subject-matter expertise than pure LLM generation
- Fact-checking process must move beyond automated model runs to manual verification of each claim against trusted sources; this is labor-intensive but essential for technical B2B content
- The 80/20 model (LLM gets 80%, editorial adds 20%) may not apply to highly technical or fast-moving industries; BaseTen needs closer to 50/50 or higher editorial involvement

**To CheckThat:**
- LLM training data staleness is a critical blocker for authority and trust in fast-moving verticals; this is a strong use case for CheckThat's AI visibility capabilities to identify which sources influence LLM outputs
- BaseTen is explicitly trying to influence LLM rankings by seeding content in authoritative third-party publications rather than vendor sources; this ties directly to AEO strategy

**To GrowthX Business Development:**
- BaseTen's brand protection and authority concerns are account health signals—they're willing to invest in longer timelines and more rigorous processes, indicating high commitment but also rising expectations
- Off-site publishing and third-party authority plays could unlock new service lines (managed PR placements, authority-building content networks)
- The "conviction matrix" (which content types GrowthX can deliver with high confidence) is a key artifact for scoping and pricing future work

---

## Overview

- GrowthX is implementing stricter fact-checking and expert review processes to improve content accuracy, including adding domain expert (BaseTen CTO Daniel) to review outlines before delivery
- BaseTen emphasizes the critical need for very recent information (3-6 months max, not 12 months) and high-quality editorial oversight, as LLM training data from June 2024 is dangerously outdated for fast-moving AI infrastructure market
- GrowthX to provide a "conviction matrix" showing which content types they can confidently produce at high confidence, and will explore off-site publishing options to increase authority with LLMs (independent sources rank higher than vendor domains)
- New Looker dashboard integrates Google Search Console and GA4 data, showing organic traffic by source, landing page performance, query rankings (branded vs. non-branded), and LLM referral traffic with top-performing pages

---

## Key Topics

### Content Creation Process Improvements

GrowthX acknowledged previous inaccuracies in outlines (including basic factual errors about NVIDIA hardware that a college student should catch) and has implemented new measures:
- Constrained information sources to BaseTen product documentation and recent, verified data (less than one year old)
- Added expert review step with BaseTen's CTO Daniel before client delivery to ensure domain expertise, not just fact-checking
- Running each claim through manual Google verification in addition to automated fact-checkers (Perplexity)
- Adding dedicated content manager (Ife) to support full editorial pass

BaseTen's core concerns:
- LLM training data is severely outdated (June 2024), making it unreliable for fast-moving AI infrastructure market where products launch and change constantly
- Models lack discernment—they pull from low-quality blog posts and vendor sources rather than authoritative information; higher-quality sources (like NVIDIA official docs or market reports) aren't consistently weighted
- Market-level insights (e.g., "who are the top inference providers?") require human judgment and recent information, not just product documentation

GrowthX's commitments:
- Send detailed approval process and quality inputs that will guide future outlines, so BaseTen can evaluate the pipeline
- Deliver a "conviction matrix" showing which content types GrowthX can confidently produce (with explicit boundaries of what they cannot deliver)
- Explore off-site publishing options—seeding content in authoritative third-party publications where LLMs will discover it, since independent sources influence LLM rankings more than vendor domains

### Analytics Dashboard Review

Aida walked through a new Looker dashboard that integrates Google Search Console and Google Analytics 4, providing visibility into BaseTen's organic traffic and content performance:

**Dashboard structure:**
- Sessions vs. engaged sessions (engagement rate target: >50% for long-form content; Google weights engagement in ranking signals)
- Landing page performance broken down by traffic source (organic, referral, paid, email)
- Query ranking distribution showing how many keywords rank in position 1, page 1 (2-10), page 2 (11-20), page 3 (21-30), etc., separated by branded vs. non-branded queries
- Conversion events tracked from GA4 (though team needs to confirm what each event represents)
- Cohort report showing performance of GrowthX-published content grouped by topic cluster
- LLM referral traffic showing which pages generate the most traffic from ChatGPT, Claude, etc.

**Outstanding items:**
- Add leading zeros to non-branded query stack graph so stacked area chart displays in sequential order (Arjun's request)
- Check definitions of conversion events with GA4 setup team
- Explore PostHog integration (Mike looks at PostHog; BaseTen sees different results there than GA4)
- Show search queries that lead to LLM referrals (not just traffic volume), so BaseTen understands what LLMs are asking and what answers they're finding

### Content Strategy Considerations

**Freshness requirements:** Marylise pushed back on the 12-month data window, arguing that 3-6 months max is required for the AI infrastructure market. Mike's example: B200 GPUs launched in May 2025, so any content older than ~6 months misses major developments. Even more problematic—an old article they found (from January 2025) comparing inference providers didn't mention BaseTen because BaseTen only launched public model APIs 5 months ago (around May 2025). This illustrates why stale content is both inaccurate and bad for BaseTen's visibility.

**Publishing strategy:** Marylise is convinced that content must be published outside BaseTen's domain to influence LLMs. LLMs trust independent third-party sources more than vendor claims—if you ask "who are the best inference providers?", the model assumes BaseTen will claim it's #1, so it looks elsewhere. GrowthX is exploring options for seeding content in authoritative third-party publications (experimental at this point), but this could be more valuable than on-domain content for LLM influence.

---

## Action Items

**Sydney Go (GrowthX)**
- Send revised outline to Marylise/Mike/Kenzie (after CTO Daniel completes expert review)

**Andi Bailey (GrowthX)**
- Send detailed approvals/inputs process document + conviction matrix to Marylise/Mike/Kenzie (within one week)
- Investigate LLM seeding options and off-site publishing; send recommendations on where and how to place content for LLM authority influence

**Aida Knezevic (GrowthX)**
- Update Looker dashboard: add leading 0s to non-branded query stack so sequential order displays correctly
- Check PostHog integration and bring PostHog data into dashboard for comparison with GA4

---

## Transcript
**Marylise Tauzia:** This meeting is being recorded.

**Marylise Tauzia:** Good morning.

**Aida Knezevic:** Hi, good morning.

**Marylise Tauzia:** I'm not sure if anybody else is doing it from our end.

**Aida Knezevic:** Rachel is on vacation.

**Marylise Tauzia:** Let me see if Erik wants to join.

**Marylise Tauzia:** Kenzie is here?

**Aida Knezevic:** Yeah.

**Marylise Tauzia:** Hi, Kenzie.

**Kenzie Amack:** Hi, guys.

**Kenzie Amack:** How are you?

**Aida Knezevic:** Good, good.

**Marylise Tauzia:** Let's get going.

**Aida Knezevic:** Yeah, I think we can get going. So the most important thing on our agenda is to discuss the outlines that we shared last week.

**Aida Knezevic:** Just wanted to acknowledge that they weren't technically accurate. We've done a lot of work this week to improve them. I think Sydney can share details on how that happened and what we've done since.

**Sydney Go:** We calibrated the articles using your feedback and your internal documentation. We've constrained our sources to pull information from BaseTen and research we're sure is 100% accurate. I've also started looping in an expert to review your content before we deliver it, which is why I don't have the outline with you today yet. They're looking it over so we have another layer of review before delivery. And I have a small ask—if you have any internal docs about your products with very specific information, that would help.

**Marylise Tauzia:** Mike, you on?

**Mike Bilodeau:** Yeah, sorry, my Wi-Fi in the office is not good. Who is the expert?

**Andi Bailey:** Hi, Mike. I'm Andi. I lead customer ops and can give you some background. But for right now, Daniel, one of our co-founders and CTO, is going to review the outline one more time.

**Andi Bailey:** So the first round of...

**Andi Bailey:** reviews we did was like our standard where we had the, the pipeline has a fact checker and then we ran it through one model and we ran it through perplexity just to double check.

**Andi Bailey:** We've now since, as Sydney said, constrained it to BaseTen documentation and used Marylise's feedback directly and added it directly into the pipeline fact checker.

**Andi Bailey:** So, but we really, like, we don't want this, we want to make sure that we're like super confident, so Daniel's going to review it, and then we are going to bring, like, we're going to find somebody that on an ongoing basis can continue to check this.

**Andi Bailey:** So I think part of this calibration piece is making sure that the process is the right process and we have the right people in place to review.

**Andi Bailey:** So, human in the loop in this case, like, we just don't have the expertise and our client ops engineer who normally helps with this sort of review.

**Andi Bailey:** So,

**Andi Bailey:** You know, on the second round was like, look, this is not my area of expertise either.

**Andi Bailey:** So we're going to make sure that we have somebody that's more of an authority in the space to be that additional human in the loop with the three checks on the models and the product documentation.

**Andi Bailey:** So that's why we're just asking for additional product documentation on your end if you have it as well.

**Mike Bilodeau:** Yeah, I think my concern is that, like, the mistakes were not expert mistakes.

**Mike Bilodeau:** They were, like, Google search mistakes.

**Mike Bilodeau:** They weren't things that, they were things that, you know, I would expect a, like, college student writer to realize that, like, hey, the highest level of NVIDIA hardware is, like, that's not an expert thing.

**Mike Bilodeau:** That's, I think that's where I'm coming from, the concern level is, like, if we're starting from that.

**Mike Bilodeau:** And, you know, starting point with content, like, it doesn't feel like a great use of our time.

**Mike Bilodeau:** So, yeah, I think I'm trying to understand better, like, a little bit of how that happens.

**Mike Bilodeau:** Because, again, like, if we're starting at that point, I don't have the expectation that we're going to have, like, 100% correct things.

**Mike Bilodeau:** But the absolute, like, false negatives are concerning.

**Andi Bailey:** In this next round of review, we went through fact by fact and did manual Google searches of each claim. Sometimes when we run articles through LLMs, they miss pieces or parts get lost in chunking. We're going piece by piece this time, with Sydney and our content manager Ife double-checking everything. We're triple-checking and now need to nail down the process and scale production going forward.

**Kenzie Amack:** So I know you use LLMs for outline creation. Who writes the articles?

**Andi Bailey:** Our system writes the first draft as well.

**Kenzie Amack:** And how much do you edit? We use LLMs to support generation, but we're very protective of our brand and authority. We want it factually correct but also well-written content that someone has taken time to clean up. How do we ensure both?

**Andi Bailey:** Our editing assumes the AI gets us 80% of the way there, with 20% editorial. We can strengthen the editorial side by bringing in the expert and setting aside time for additional review.

**Marylise Tauzia:** What's missing is an expert in the space to really fact-check and get the outlines where they need to be. We definitely want strong editorial, especially if it goes on our site. We can't have brand issues like this.

**Andi Bailey:** Once we nail down the process, we'll share the steps we're taking every time so you feel confident. Our standard process is: AI gets us 80% there, then a round of fact-checking in the workflow, then running the full article through Perplexity. We need additional rounds of fact-check and manual editing.

**Marylise Tauzia:** Mike and I have a big concern that LLMs haven't updated their data in over a year. The training data is from June 2024. That's why the human in the loop is so important—I'm having anxiety about trusting LLMs at this point. If we only rely on them, we'll go in the wrong direction.

**Mike Bilodeau:** I asked who the person is because investing in this makes sense if there's incremental knowledge gain and space understanding.

**Mike Bilodeau:** Kenzie wasn't an expert months ago, but now I'd trust her. Marylise wasn't an expert six months ago, but now I do, because you build context over time. If we're starting from square zero, that's a big time investment with unclear iterative improvement. The second issue: LLM training data is out of date and the space moves very fast. There are a lot of low-quality sources online. When I ask ChatGPT "who are the top inference providers?", it cites a three-year-old Helicone blog post. Models aren't discerning about information quality. My heartburn: will we get discernment about what's good information? Our documentation is product information, not market information.

**Andi Bailey:** We've restricted to information less than a year old. We can also constrain to specific sources—in regulatory spaces we restrict to .gov, for example. If there are sources you trust more, we can look there. We can talk to Daniel about adding artifact fact checkers as additional pipeline steps. We have writing guidelines and can double-check articles against your documentation after generation. If you have other places where information is accurate, we can prioritize those for fact-checking.

**Mike Bilodeau:** I'm confused about what we hope to get from our docs for market-level info like GPU specs. That's market-level stuff, not documentation.

**Marylise Tauzia:** You could check NVIDIA for that, or other GPU providers.

**Andi Bailey:** I was thinking product marketing assessments or internal evaluations you've done. We're not doing that in the docs yet—they're very engineering-driven, but we're moving in that direction in a couple months.

**Mike Bilodeau:** I thought you meant documentation, not a platform.

**Andi Bailey:** Right, not just engineering docs—if you have done assessments, that helps.

**Marylise Tauzia:** That's what we're extending to you because we don't have resources—we're stretched. Eventually we'd love to build authority and thought leadership, but it's hard to find time.

**Andi Bailey:** The next step to build confidence is sending you the approvals process and inputs for generating outlines—step-by-step, what sources, how we're assessing market space. We'll get you the outline and process document. It may take longer to ensure it's scalable.

**Mike Bilodeau:** What I need to know is which types of articles you can generate with high conviction and confidence. We need different content types and distribute through various channels. The main ask: where's the conviction line? If we can't get to a certain confidence level for some pieces because we lack in-house expertise, that's easier to know than "do you feel good about it or not?"

**Andi Bailey:** We owe you that. I can't tell you what's in and out right now, but we can get you that within the next week before our next call.

**Marylise Tauzia:** Another question related to what Mike said: we've talked about content on our properties, our website, blog, guides. But I'm convinced that to influence LLMs, content must be outside our domain. Do you have recommendations on where we can publish? Because we'll only get authority if it's not on our site. LLMs trust independent sources more than vendors. If you ask who's the best inference provider, they won't look at BaseTen because BaseTen will claim it is.

**Andi Bailey:** We're exploring options for places to seed content that LLMs will recognize as more authoritative. Some are experimental, so let me check results and get you stronger recommendations.

**Mike Bilodeau:** That might be more valuable than on our properties. Most content older than six months is out of date anyway.

**Marylise Tauzia:** Twelve months is too long for this fast-moving space. Three to six months max. Things are evolving rapidly.

**Mike Bilodeau:** B200 GPUs came out in May—that's just too wide a window.

**Marylise Tauzia:** Right. An article from January didn't even mention BaseTen compared to competitors. By now, with our public APIs five months old, we should be on the map with independent sources.

**Mike Bilodeau:** So we need to understand: where can we put 80%-ready content that we'll finish with editing? And where do we have high conviction? What's the boundary?

**Andi Bailey:** Yeah, yeah.

**Andi Bailey:** It sounds like we can get you a matrix there.

**Andi Bailey:** And also thinking about, like, where else?

**Andi Bailey:** We might be able to add content that can build authority back to you guys.

**Marylise Tauzia:** Cool.

**Marylise Tauzia:** Cool.

**Andi Bailey:** All right.

**Andi Bailey:** Aida, is there anything else that you want to talk about?

**Aida Knezevic:** I did share access to a Looker dashboard with everyone maybe an hour ago.

**Aida Knezevic:** I did see that, let me just take a look really quickly.

**Aida Knezevic:** I did see that Arjun had some questions about the Looker dashboard.

**Aida Knezevic:** So if, you know, you all have time, I could just like answer them really quickly and go through it.

**Aida Knezevic:** I think it might be helpful just to like, if you're looking into your organic search traffic, it might be interesting to kind of take a look.

**Aida Knezevic:** Won't take too long.

**Marylise Tauzia:** Yeah, that sounds great.

**Aida Knezevic:** Okay, cool.

**Aida Knezevic:** So I'm going to share my screen really quickly.

**Aida Knezevic:** So yeah, this is a Looker dashboard report.

**Aida Knezevic:** That includes data from your Google Search Console and Google Analytics 4.

**Aida Knezevic:** So the first page breaks down your overall sessions versus engaged sessions, and this is data from your Google Analytics 4 account.

**Aida Knezevic:** I see that Arjun had a question about, like, what's the definition of an engaged session?

**Aida Knezevic:** So Google qualifies a session as engaged when it lasts longer than 10 seconds, or it includes a page scroll, or it involves the user clicking on a link on your website.

**Aida Knezevic:** So this is usually, so the engagement rate is basically the opposite of the bounce rate.

**Aida Knezevic:** We want to make sure that this engaged session rate, at least on the content that we're publishing, because it is long-form content, it should have an engagement rate that is

**Aida Knezevic:** So high, so over 50%.

**Aida Knezevic:** Right now for your website, this is pretty standard.

**Aida Knezevic:** This is for the entirety of your website.

**Aida Knezevic:** But for the content that we're publishing, we usually track this information so we understand what types of content perform better with your audience.

**Aida Knezevic:** Google uses the engagement rate as a slight ranking factor.

**Aida Knezevic:** So if a page is able to capture someone's attention for longer than 10 seconds, then it means it's valuable.

**Aida Knezevic:** So they're more likely to prioritize that page and that website in search results.

**Aida Knezevic:** So that is sort of the definition of an engaged session.

**Aida Knezevic:** Further down, you have the landing page performance.

**Aida Knezevic:** Again, this is data from Google Analytics 4.

**Aida Knezevic:** You can see sessions, engaged sessions, and the overall engagement rate.

**Aida Knezevic:** This is data from all sources.

**Aida Knezevic:** You can...

**Aida Knezevic:** Kind of take a look at the session medium here and filter the views.

**Aida Knezevic:** So you can filter out just organic traffic or referral or paid or email and kind of do additional explorations.

**Aida Knezevic:** You can also change the date here.

**Aida Knezevic:** Right now it's set to show data from the last month.

**Aida Knezevic:** It also breaks down the sessions by referrers.

**Aida Knezevic:** So you can see which referrers bring the most traffic to your website.

**Aida Knezevic:** And this includes all referral traffic.

**Aida Knezevic:** So including organic search, organic social, LLMs, platforms like GitHub.

**Aida Knezevic:** And it also breaks down, this is data from a Google search console.

**Aida Knezevic:** It breaks down the query ranking distribution.

**Aida Knezevic:** So these are basically the keywords that you rank for and the positions that you rank for.

**Aida Knezevic:** So you can see like how many keywords you're ranking for in position one versus page one versus page two.

**Aida Knezevic:** Those are like 11 through 20.

**Aida Knezevic:** 20.

**Aida Knezevic:** is page 2, for example, 21 through 30 is page 3.

**Aida Knezevic:** The non-branded report shows data for URLs that rank for keywords that don't include your brand name.

**Aida Knezevic:** So, you know, all of your blog posts or, you know, if any of your product pages or any other parts of your website rank for keywords that don't include your brand name, that data is going to be represented here.

**Aida Knezevic:** I think that Arjun had a question.

**Aida Knezevic:** For the non-branded query stack graph, can we add a leading 0 in front of the 1 and the 210 so that the stacked area chart is broken out in sequential order?

**Aida Knezevic:** Yes, we can do that.

**Aida Knezevic:** Yeah, I can get in touch with our team who puts these together, and I think we'll be able to tailor that for you.

**Aida Knezevic:** and it gives you kind of, if you scroll down, you can have, you can take a look at the performance.

**Aida Knezevic:** Thank

**Aida Knezevic:** of URLs for these non-branded queries over time.

**Aida Knezevic:** The conversion events are taken directly from Google Analytics 4.

**Aida Knezevic:** I know that Arjun had a question about where these conversion events were taken from and what each of them means.

**Aida Knezevic:** That's something that I would check with the team that set up your GA4.

**Aida Knezevic:** So they should be able to know what each of these descriptions mean and what kind of activity they're tracking on your website.

**Aida Knezevic:** So this is just, we don't, we cannot influence these names because they're just being retrieved from your Google Analytics property as they are.

**Aida Knezevic:** You can also see a more detailed breakdown of these events below.

**Aida Knezevic:** And the cohort report is intended to show a breakdown of the traffic.

**Aida Knezevic:** So is like

**Aida Knezevic:** Of blog posts published by GrowthX, so right now that's obviously empty, but this is how we track the performance of all the content that we publish.

**Aida Knezevic:** In this graph, so we, in this chart, we categorize it by cluster, so last week we presented the content calendar with multiple like topic clusters, and we grouped them here as well, so we can see which ones are performing better than others.

**Aida Knezevic:** And we also include a breakdown here, so you can see the, like, the performance of URLs on your website that are not, that were not created by GrowthX, and you can also see the performance of GrowthX content, and also the individual page performance.

**Aida Knezevic:** And then the landing page report, I believe this is also pulled from Google Analytics 4, sorry it's a little slow, Looker isn't the fastest data.

**Marylise Tauzia:** so you, is

**Marylise Tauzia:** I have a question.

**Marylise Tauzia:** Will you pull anything from PostHog, or is it just going to be Google Analytics?

**Aida Knezevic:** I think we can.

**Aida Knezevic:** Yeah, right now we can only do GA4 and GSC.

**Aida Knezevic:** I'm not sure if, I mean, I think if we have access to your PostHog, I'm sure that we might be able to pull some data in, but I would have to check with our data person.

**Marylise Tauzia:** Okay, because we see different kind of results, so, and I think Mike looks at PostHog mostly.

**Aida Knezevic:** Okay, okay, yeah, that makes sense.

**Aida Knezevic:** Okay, this is loading, taking way too much time, but this is just an overall breakdown of the landing page performance.

**Aida Knezevic:** I believe this is, okay, this is data from Google Search Console, so the landing page performance report on the overall page displays data from GA4, so that's the difference.

**Aida Knezevic:** The queries report just goes into more detail around all of the keywords that you're ranking for in Google.

**Aida Knezevic:** So, So,

**Aida Knezevic:** So you can kind of see what are the keywords that you're ranking for.

**Aida Knezevic:** Obviously, there's going to be a lot of branded queries there, but you can also see some non-branded queries as well.

**Aida Knezevic:** And then the last report is related to LLM referral traffic.

**Aida Knezevic:** So it shows which LLMs are driving the most traffic to your website.

**Aida Knezevic:** I know that you had a question around whether we can see, like compare, do a comparison report with your top competitors.

**Aida Knezevic:** We can't do that here because this is data from your Google Analytics 4, but we can track your competitors in Scrunch.

**Aida Knezevic:** I think I showed you your Scrunch dashboard last week.

**Aida Knezevic:** So that's where we can kind of track your AI visibility and visibility of your competitors.

**Aida Knezevic:** And this LLM report is just to see which pages are getting the most attention from LLMs.

**Aida Knezevic:** So, for example, if you scroll down, you can see like, okay, you have a blog post that's gotten...

**Aida Knezevic:** ...

**Aida Knezevic:** Like close to five, like over 500 clicks from LLMs this year.

**Aida Knezevic:** And you also have like additional blog posts that have been getting a lot of traffic from LLMs.

**Aida Knezevic:** So yeah, if you have any additional questions, feel free to drop them on Slack and I can answer.

**Mike Bilodeau:** We're more curious about what people are searching for and why these pages show up, not just traffic volumes.

**Aida Knezevic:** I understand. We've updated the prompts in the Scrunch dashboard as you requested, Marylise. Next week, once that data is collected, we can show AI visibility data, which prompts you have the most visibility on, and topics. That should be more interesting.

**Aida Knezevic:** Thank you for your time. We'll be in touch with the new outline.

**Andi Bailey:** And the process showing what's possible and what's not.

**Marylise Tauzia:** Thanks.

**Andi Bailey:** Thank you. Bye.
