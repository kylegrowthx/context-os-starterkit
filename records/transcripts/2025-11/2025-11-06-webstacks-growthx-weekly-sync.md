# Webstacks <> GrowthX - Weekly Sync

<metadata>
date: 2025-11-06
time: 17:29 UTC
duration: 39 minutes
organizer: team@growthxlabs.com
participants: Jesse Schor, Rachel Pasche, Jakub Rudnik, Jessalynn Jones (she/her)
fathom_recording_id: 99779958
fathom_url: https://fathom.video/calls/464555729
share_url: https://fathom.video/share/6o86J1VVpmcdJvTFkjevnF-BYjmP8o9i
source: fathom
enriched_on: 2026-03-02 16:45 UTC
</metadata>

---

## Summary

GrowthX and Webstacks reviewed monthly analytics showing 4% overall traffic growth with domain authority up 12 points YTD, but identified two content performance concerns: the high-value "CMS platforms" cluster is declining and the "AI content" cluster has stalled at ~70 visits/month. GA4 significantly undercounts AI-driven traffic (misattributing it as organic/direct), but Jesse's form submission data shows users self-reporting ChatGPT as their source, so Jakub will begin combining organic and referral data in reports. The team introduced a streamlined Content OS workflow in Airtable with Slack automation to simplify Webstacks' content approval process, while Jessalynn kicks off supporting content for the "Coffee Chat" series and Jesse adds new HubSpot tracking fields to improve lead source attribution.

---

## Context

Webstacks is a GrowthX client operating in content and software space. This is a recurring weekly sync between the Webstacks team (led by Jesse Schor) and the GrowthX content and analytics team (Jessalynn Jones, Jakub Rudnik, Rachel Pasche). The meeting reviews monthly performance metrics from Webstacks' blog and content properties using tools like GA4, Ahrefs, and a custom Looker dashboard. A major focus this month is improving attribution accuracy (especially around AI traffic from ChatGPT, Perplexity, and Gemini), rolling out a simplified content workflow to accelerate publication, and conducting a comprehensive content audit to inform future strategy. The relationship appears collaborative with trust on both sides — Webstacks gives GrowthX latitude to execute while GrowthX provides detailed analysis and strategic recommendations.

---

## Relevance

**To GrowthX Delivery:**
- Validated the importance of combining GA4 "organic" and "referral" data to account for AI attribution gaps — actionable insight for similar clients experiencing underreporting of LLM traffic.
- Successfully deployed a simplified Airtable-based content workflow with Slack automation to reduce approval friction; may be replicable for other clients managing high-volume content production.
- Identified need for detailed content audits (site structure, internal linking, consolidation opportunities) as strategic foundation for both short-term quick wins and long-term roadmap.

**To CheckThat:**
- Real-world evidence that GA4 systematically undercounts AI-driven traffic by misattributing it as "organic" or "direct," reinforcing the value of dedicated AI visibility tools like CheckThat for accurate attribution and visibility tracking.
- Webstacks seeing strong visibility growth in AI citations (via Scrunch pool) even as direct LLM referral traffic fluctuates, suggesting CheckThat's focus on citation-based visibility is distinct and valuable from GA4's click-based metrics.

**To GrowthX Business Development:**
- Positive account health signal: Webstacks expanding workflow and data infrastructure with GrowthX (new HubSpot fields, expanded reporting), indicating deepening integration and reliance on GrowthX expertise.
- Jesse and team demonstrating trust in GrowthX to operate independently on content ideation, approvals, and strategic choices — signs of maturity and potential for scope expansion on consulting or retainer work.
- Coffee Chat series and content audit represent potential expansion opportunities if Webstacks decides to formalize more strategic planning or monthly consulting alongside production work.

---

## Overview

- **Analytics:** Site traffic is up \~4% MoM, but the high-value "CMS platforms" content cluster is down, and AI content growth has stalled.
- **Attribution:** GA4 undercounts AI traffic by misattributing it as "organic" or "direct." Jesse's form-submission data will be used to create a more accurate report.
- **Workflow:** A new, simplified Content OS in Airtable and Slack bots will streamline Webstacks' content review and approval process.
- **Content Strategy:** Jessalynn will create supporting content for the "Coffee Chat" series, while Jakub's full content audit will inform a larger, long-term strategy.

---

## Key Topics

### Analytics & Performance Review

  - **Site-Wide Metrics:**
      - Overall traffic growth: **+4% MoM**.
      - Page 1 keywords: **+4% MoM**.
      - Domain Rating: **+12 points YTD** (per Ahrefs).
  - **Content Cluster Performance:**
      - **High-Growth:** "CMS platforms" & "AI clusters" are seeing strong growth (10-18%).
      - **Underperforming:** The "CMS platforms" cluster is down. Jakub will investigate the cause (e.g., publish dates) during the full audit.
      - **Stagnant:** The AI content cluster is flat at \~70 visits/month.
          - **Hypothesis:** Content cannibalization.
          - **Action:** Jakub will investigate for potential consolidation or refreshes.
  - **LLM Referral Traffic:**
      - **Trend:** Down **-15% MoM** (Sep→Oct).
      - **Context:** Still significantly higher than August levels.
      - **Hypothesis:** A recent change in how ChatGPT displays links could be the cause. Jakub will monitor for a wider industry trend.

### Attribution & Reporting Accuracy

  - **Problem:** GA4 undercounts AI traffic by misattributing it as "organic" or "direct."
  - **Evidence:** Jesse's form-submission data shows users self-report "ChatGPT" as a source, even when GA4 doesn't.
  - **Solution:** Jakub will combine "organic" and "referral" (from LLMs) data in reports to create a more accurate picture of AI-driven traffic.

### Content Strategy & Audit

  - **Short-Term Plan:** Jessalynn is creating supporting content for the "Coffee Chat" series.
      - **Process:** Break down each Coffee Chat blog → identify internal linking opportunities & new content ideas.
      - **Approval:** Jesse will review the plan but trusts the team to proceed without individual article-level approvals to maintain momentum.
  - **Long-Term Plan:** Jakub's full content audit is ongoing.
      - **Goal:** Map all content to inform site structure, internal linking, and future ideation.
      - **Opportunity:** Refreshing and consolidating overlapping content for quick performance gains.

### New Workflow & Reporting

  - **Content OS (Airtable):** A simplified view was created to streamline Webstacks' review process.
      - **Features:** Direct tabs for "Topics Awaiting Approval," "Ready for Review," and "Published Articles."
      - **Functionality:** In-app buttons ("Approve," "Reject," "Hold") automate status updates.
  - **Slack Automation:** A bot will notify Webstacks in the shared channel when content is ready for review.
  - **HubSpot Data Sheet:** Jesse added new fields to improve lead source tracking.
      - **New Fields:** `First Page Seen`, `Last Page Seen`, `Recent Page Seen`, `Recent Conversion Date`, `MQL Date`, `Opportunity Date`.
      - **Challenge:** The `Date Added` field is problematic because the current workflow creates duplicate records on updates.
      - **Workaround:** Use `Recent Conversion Date` and `MQL Date` to infer the timing of blog influence on a lead.
      - **Data Joining:** `Contact ID` on the deal tab (semicolon-separated) enables joining contact and deal data. `Company ID` can also be used to link content views to company-level deals.

---

## Action Items

**Jakub Rudnik (GrowthX)**
- Investigate CMS Platforms cluster traffic decline; review published dates
- Investigate AI cluster impression stagnation; assess cannibalization; propose merges/refreshes
- Investigate LLM referral drop; check ChatGPT citation changes; report back
- Add GA4 organic+referral stacked bar to next report for Jesse

**Jessalynn Jones (GrowthX)**
- Share Coffee Chat supporting content map in Slack for Jesse and Eric
- Link Content OS at top of all agendas and in Slack for Jesse and Eric
- Consult reporting team re: 'Date added' formula; implement if needed

**Jesse Schor (Webstacks)**
- Add HubSpot properties to reporting sheet: first/last/recent page seen, recent conversion date

---

## Transcript
**Jakub Rudnik:** This meeting is being recorded.

**Rachel Pasche:** Wow, Shika, did you get a haircut?

**Jakub Rudnik:** Thank you.

**Jesse Schor:** What's up, guys?

**Jessalynn Jones (she/her):** Hey, how's it going, Jesse?

**Jesse Schor:** Pretty good.

**Jesse Schor:** How are we doing?

**Jessalynn Jones (she/her):** Good.

**Jessalynn Jones (she/her):** How was the Halloween photo shoot?

**Jessalynn Jones (she/her):** Did it end up happening?

**Jesse Schor:** It didn't.

**Jesse Schor:** We didn't have the heart to answer the door with my wallet.

**Jesse Schor:** It was a bag of cocaine.

**Jessalynn Jones (she/her):** That's mean.

**Jessalynn Jones (she/her):** Oh my gosh, that's great.

**Jesse Schor:** An adorable DEA vest for our dog.

**Rachel Pasche:** That's so clever.

**Jessalynn Jones (she/her):** That's awesome.

**Jessalynn Jones (she/her):** Oh my gosh.

**Jesse Schor:** Yeah, I feel like we'll have to save it for like a adult party, Halloween party.

**Jessalynn Jones (she/her):** If we ever wear one of those in the future.

**Jessalynn Jones (she/her):** Yeah.

**Jessalynn Jones (she/her):** Nice.

**Jesse Schor:** You guys, how was, how was the weekend?

**Jesse Schor:** How, how was, uh, Jacob taking kiddos, uh, trick or treating?

**Jakub Rudnik:** Uh, it was fun.

**Jakub Rudnik:** Frankie was, he had like, my parents had a Halloween thing.

**Jakub Rudnik:** He didn't really get it.

**Jakub Rudnik:** And then he went and did something with school and like kind of got it.

**Jakub Rudnik:** And then Halloween, he was actually getting it.

**Jakub Rudnik:** But like two of the first four houses.

**Jessalynn Jones (she/her):** So he turned two this weekend.

**Jessalynn Jones (she/her):** So that's how old he is.

**Jessalynn Jones (she/her):** He just like, they're like trick or treat and holding the, or, you know, the bag of candy, like the owners.

**Jessalynn Jones (she/her):** And he just ran.

**Jessalynn Jones (she/her):** Like he just ran straight in and they're like, sorry, but he got it, he mostly got it. He was like shouting and then like "trick-or-treat." That was really funny. And then we just had like a bonfire in the driveway and just sat around and gave out candy, so him and like four kids were just sprinting around us, being weird and staying up way too late. It was a good time. Yeah, Rachel, you guys have kids? I have one of my own and then I have three step kids, so I have a house full. How was your Halloween? Yeah, it was good. Although like, I don't know, I'm trying to remember if I told you this, but I was, my son dressed up as like Hiccup from How to Train Your Dragon, the main character. Yeah. And I just wore like a black cat onesie. I was like super boring and walked around with him, but everybody thought

**Jessalynn Jones (she/her):** I was the black dragon toothless from How to Train Your Dragon because he was Hiccup and he was like so embarrassed by that.

**Jessalynn Jones (she/her):** He was like, "Mom, this is so uncool.

**Jessalynn Jones (she/her):** I'm not having a matching Halloween costume with you and was like very sure to explain to everybody that I was a black cat and not his dragon.

**Jessalynn Jones (she/her):** But anyway, but it was good.

**Jesse Schor:** Yeah.

**Jessalynn Jones (she/her):** He's like just hitting that age where he's embarrassed of me and I'm like, okay, well, this is bound to happen sometime.

**Jessalynn Jones (she/her):** Buckle up, buddy."

**Jesse Schor:** Do you have kids, No, no kids.

**Jesse Schor:** Just English Bulldog that...

**Jesse Schor:** Oh my gosh, I have an English Bulldog too.

**Jesse Schor:** Oh really?

**Jesse Schor:** How have we not talked about this?

**Jessalynn Jones (she/her):** I know.

**Jesse Schor:** They are the best.

**Jesse Schor:** So yeah, you understand all the things that come with.

**Jessalynn Jones (she/her):** The high maintenance diva personality, the drooling and farting.

**Jesse Schor:** Yeah.

**Jesse Schor:** No, right.

**Jessalynn Jones (she/her):** Oh yeah.

**Jesse Schor:** Yeah.

**Jesse Schor:** I'm surprised you guys haven't heard him on.

**Jesse Schor:** Been like working from home.

**Jesse Schor:** A little bit more over the past few weeks, and he definitely shows up on some of the calls when he's snoring underneath my desk here.

**Jessalynn Jones (she/her):** Oh my gosh.

**Jessalynn Jones (she/her):** I finally had to give some of my coworkers a disclaimer because now I have a separate office, but when I was working in my home office more, my bulldog would hang out with me, and she would snore super loudly or fart really loudly.

**Jessalynn Jones (she/her):** So I finally had to like give all my coworkers a disclaimer.

**Jessalynn Jones (she/her):** like, I'm not snoring or farting on calls.

**Jessalynn Jones (she/her):** I promise it's the dog.

**Jessalynn Jones (she/her):** But yeah, it's fun.

**Jesse Schor:** I just like feverishly watch the like mic and like if it's picking it up or not.

**Jessalynn Jones (she/her):** Yeah, same, same.

**Jessalynn Jones (she/her):** Yeah.

**Jessalynn Jones (she/her):** Although she was lucky because she didn't get dressed up this year.

**Jessalynn Jones (she/her):** Usually my stepdaughters dress her up and torture her somehow.

**Jessalynn Jones (she/her):** Like last year she was a dragon with like little.

**Jessalynn Jones (she/her):** Wings and everything, and she hates getting dressed up, so she got away this year with not getting dressed up and was very happy about that, but… Ugh.

**Jessalynn Jones (she/her):** All right.

**Jessalynn Jones (she/her):** Should we talk about work stuff?

**Jessalynn Jones (she/her):** We actually have kind of exciting stuff to do, to go over today.

**Jessalynn Jones (she/her):** Jacob, do you want to start with the analytics, or should I walk through the new content interface really quick?

**Jakub Rudnik:** Uh, yeah, I'll walk through.

**Jakub Rudnik:** That's pretty, pretty quick.

**Jakub Rudnik:** Um, yeah, just our general monthly overview of where things stand.

**Jakub Rudnik:** Uh, site-wide, looking, like, fairly solid and steady, 4% overall growth.

**Jakub Rudnik:** Uh, generally, like, page one keywords, so I don't know if you use Ahrefs regularly or any of the other SEO tools, Jesse, but… I basically just started turning these all off because of the way that, like, Google has turned off the crawl of 100.

**Jakub Rudnik:** It's all plummeted, but when we're looking at just the page ones, it's harder to tell what's going to happen down the road, because we just have lost those impressions and keywords, but overall, page one stuff is growing about 4%, so mirroring that overall traffic growth, and then we haven't really talked about this, and it's a culmination of other things, it's not just what we're doing or anything, but this year, your domain rating is up 12 points, just really, really solid, yeah, you don't see growth like that too often, so I just wanted to call that out, I was poking around and saw that, so, I think that, it's just, it's a little bit of a vanity metric, in a way, but also, it can be an indicator of, like, overall success and health, and that looks really good, at the blog level, not just GrowthX stuff, very similar to the site level, 4.7% at the keyword level, so, very similar here, but growing and coming out of, like, summer slumps, seeing some of this,

**Jakub Rudnik:** Steady accumulating growth here.

**Jakub Rudnik:** On our content, that 4% number is just like where we're at, we're just like inflation or something right now, 4% on the clicks for the content that we've created for you all time.

**Jakub Rudnik:** We have so much content and traffic, and I think I'll be able to dive in deeper coming out of the larger audit, which is still ongoing.

**Jakub Rudnik:** But cluster level, have some, like these are some of the clusters that have a thousand plus visits every month.

**Jakub Rudnik:** So there's like much bigger.

**Jakub Rudnik:** And then we have with some other clients, but these two are really successful right now.

**Jakub Rudnik:** 10, 18, 12% growth.

**Jakub Rudnik:** The CMS platforms is the one that is down.

**Jakub Rudnik:** I don't have details on like the specifics or have hypotheses on why I want to look at published dates and some other things.

**Jakub Rudnik:** This is just something I saw this morning.

**Jakub Rudnik:** So this is like an action item for me to spend time on where, but also I'm working on that.

**Jakub Rudnik:** Holistic.

**Jakub Rudnik:** Holistic.

**Jakub Rudnik:** So I think more will come out of this, but this is like the one flag, and I feel like this is some content that should be converting for you all in that space more than some other cluster.

**Jakub Rudnik:** So this is definitely something we want to investigate further.

**Jakub Rudnik:** The AI clusters, so those chapters we did plus the AI cluster before, traffics, okay, not really, even 70 visits was pretty stagnant month over month.

**Jakub Rudnik:** Impressions, don't look at the clicks here, this graph gets, like pulls in, clicks incorrectly, I think, but impressions, there's that impression issue from September 15th or so, it's hard to tell exactly what's going on, but we're not seeing growing impressions.

**Jakub Rudnik:** So this is another one of those focus areas for me coming out of the audit is, like we had the hypothesis that we have cannibalizing content, tried some quick fixes there, but I think there's more to do, both in a lot

**Jakub Rudnik:** I need the content, possibly combining things.

**Jakub Rudnik:** And so this is one of the areas that I'll spend time.

**Jakub Rudnik:** Like there is traffic, but it's not growing anymore.

**Jakub Rudnik:** It's hard for me to pull these URLs out and just look at them from a keyword standpoint.

**Jakub Rudnik:** So I can't do that very scalably, but using impressions and clicks were just kind of stalled here.

**Jakub Rudnik:** LM referrals, it was like a massive grower last month.

**Jakub Rudnik:** We have about 40% from September to August, down 15% both at the site level and then our content level.

**Jakub Rudnik:** Still way up from August and the summer.

**Jakub Rudnik:** Still honestly the best LM referral traffic I've seen from any of our clients or anything.

**Jakub Rudnik:** But down slightly, I don't know.

**Jakub Rudnik:** I don't have an answer for this.

**Jakub Rudnik:** It's the first like drop we've had in a while.

**Jakub Rudnik:** So it's a thing to double click into potentially.

**Jakub Rudnik:** I don't know if it's like, like we're sticking traffic up, but oh, I'm...

**Jakub Rudnik:** The referrals are down, are we seeing, I don't know, I don't have a good answer for this, because on the other side, like our visibility, so that scrunch pool that I believe we sent access over to last month, we're starting to see, you we only set it up about a month ago, but we've been growing in visibility and citations there, so theoretically we could be seeing more citations and visibility, but if like ChatGPT does something that decreases people leaving ChatGPT for another website, like making links less obvious or something, potentially that's this, I haven't seen that trend wise across clients though, you're only the second one I've done this for this month, so I'll report back if I'm seeing that across the larger.

**Jesse Schor:** So just so I'm clear, like I understand, so like this LLM referral traffic you're saying, like this is from GA4, and then, but we're not seeing the same thing in scrunch?

**Jakub Rudnik:** GA4, GA4, so yes.

**Jakub Rudnik:** GA4, traffic, month over month down, month over two months, still up, LM visibility, so citations, not clicks, from scrunch, appears up just the one month, we don't have data back further, so we're looking at different horizons there, also the scrunch data, we did a lot of focus on the AI, so some of that newer content, there was like your high level, most important pieces as well, but there's, this will be less, comprehensive, yes, that's the word, so it, there will be gaps in this, doesn't tell that full picture, and I want to get the longer horizon here too, before I feel good, like, I would, I've, this is real clicks, and real visitors to the site, right, this is, incomplete and shorter, so, I'd put less stock into this.

**Jesse Schor:** Last thing, uh, I've noticed, I mean, for what it's worth, um, and I was working on some of the, like, data, uh,

**Jesse Schor:** Like fixes before we hopped on here and I added something, it wasn't a part of your guys' talk, but we have like a deal source indicator.

**Jesse Schor:** I'm noticing more and more that in GA organic or direct is what's being applied.

**Jesse Schor:** But when I look at their form submission for, you know, like their first person source, they're putting like chat, researching on chat GPT or something like that.

**Jesse Schor:** And so I do think like to an extent, there's probably some like unreliable data in GA4 when it comes to tracking.

**Jesse Schor:** I don't really know how it works, why it works sometimes, like sometimes it's, you know, referral.

**Jesse Schor:** So.

**Jesse Schor:** There's the referral, ChatGPT, Perplexity, Gemini, it's very clear, other times it's like direct and can't really see why but that might be helpful when we can get that data to look at as well, not just from like pipeline but like our organic and direct related traffic or I should say like organic and direct related like forms submissions, source form submissions is like the highest it's been over the past few months and I'm kind of just like anecdotally like lumping all of that into organic AI just because often that is the case, I think.

**Jakub Rudnik:** Yeah, that's a really good call out.

**Jakub Rudnik:** I think we've talked about like we've had a version of this conversation, I think this is like an offshoot of what we've done before but the general path of like seeing is like...

**Jakub Rudnik:** So webstacks name in GPT and then go to Google and type either, you know, your actual URL or search, then you get a different attribution.

**Jakub Rudnik:** And so that's why the first person makes a ton of sense.

**Jakub Rudnik:** I've been starting to, I think for the results here, I've been using just organic filter in our looker dash, but I've been toying around with also using referral as well for that purpose.

**Jakub Rudnik:** And then the direct, it's like direct, direct gets wonky cause you get the like none in parentheses and then it can be a mix of things.

**Jakub Rudnik:** So I'd stay away from that, but I think that's, there can be a black box there.

**Jakub Rudnik:** So it's worth saying to myself, like looking at that for trends as well.

**Jakub Rudnik:** And I think somewhat of what you said in there too, is like, like I remember a few months ago that ChatGPT like started hiding links much better in their citations.

**Jakub Rudnik:** And then everyone saw the referral traffic fall off.

**Jakub Rudnik:** I don't know if there's been a recent change of some sort there.

**Jakub Rudnik:** appear.

**Jakub Rudnik:** If

**Jakub Rudnik:** I have not seen anything, but I've also not been spending my time, like, as much of my time on LinkedIn or reading other articles recently, so something I can poke around with, but.

**Jesse Schor:** Yeah, yeah, definitely.

**Jesse Schor:** Yeah, it would be helpful if, like, we can add in the referral.

**Jesse Schor:** Like, usually that's what I'm doing when I'm in GA is, like, I'm just kind of lumping organic and, like, referral LLMs into, like, one type of report when, like, I'm trying to get, get a sense of, like, our organic in general.

**Jakub Rudnik:** Mm-hmm, mm-hmm.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** Yeah, that's, just see what the best way for me to do that, but I can do, like, I think having a stacked bar graph with the two of those can help us to, to better, have a better picture.

**Jesse Schor:** Um, yeah, I just use, like, source and medium.

**Jesse Schor:** We also can always, like, like, I can update default, like, uh, GA's default, uh, channel sources, if that's, like, easier.

**Jesse Schor:** Um, we can, like, add.

**Jesse Schor:** And a tag, it'll obviously just be like, you know, from whenever we set it moving forward, but if we like notice something really strongly, there's some I've noticed, but like on a, I haven't like updated our default groupings in GA4 because of it, I'd usually just like when I'm creating a report kind of manually add in the referral traffic just through like source medium.

**Jakub Rudnik:** Mm-hmm.

**Jakub Rudnik:** Yeah, it makes sense.

**Jakub Rudnik:** I default to our Looker dashboard doesn't have as, it's harder to get some of that.

**Jakub Rudnik:** So I'll probably just start using GA4 for some of these where it seems like we have gaps.

**Jakub Rudnik:** So this is a good shout.

**Jakub Rudnik:** This, I'll just make a graph for this next time.

**Jakub Rudnik:** was pretty short in time, but I pulled from our, from your like marketing 2025 report, just the total number of leads.

**Jakub Rudnik:** Like I don't see a trend line.

**Jakub Rudnik:** The number is generally too small to feel like I'd see a trend at this stage, but maybe it's six leads.

**Jakub Rudnik:** It's from blog, according to that report.

**Jakub Rudnik:** I don't know if there's a better thing to use or what you're

**Jakub Rudnik:** Like sources of truth or other HubSpot reports.

**Jakub Rudnik:** So I put this like little, yeah.

**Jakub Rudnik:** If there's other metrics you wanna see, Jesse, from this let me know so I can start pulling more data in and make this more useful for everybody.

**Jesse Schor:** Cool.

**Jakub Rudnik:** I think that's what I had at the high level, get more to double click into coming out of the review and audit.

**Jakub Rudnik:** So I'll have more on that next week.

**Jakub Rudnik:** Sweet.

**Jakub Rudnik:** It's a big project.

**Jakub Rudnik:** There's a lot of content and a lot of different things to map out.

**Jakub Rudnik:** So thanks for bearing with, but I think it'll be useful for both new content and ideation, site structure and internal linking, things like that.

**Jakub Rudnik:** And then as I kind of mentioned with the AI, there's a lot of content that I think has overlapping that we can combine, refresh and see fairly quick boosts from because we've just got such a sprawling set of content at this point.

**Jakub Rudnik:** Mm-hmm, so.

**Jessalynn Jones (she/her):** It's done.

**Jessalynn Jones (she/her):** Yeah, kind of along the same lines, like I know in the short term while Jakub's working on the larger audit, we're kind of going piece by piece with looking at supporting content for the Coffee Chat series and share my screen here.

**Jessalynn Jones (she/her):** I just wanted to kind of get your eyes on this and see if this kind of makes sense from your perspective.

**Jessalynn Jones (she/her):** So basically what I've been doing is just breaking down each of the Coffee Chat blogs and then identifying internal linking opportunities and then new content opportunities for each of those topics that are covered in the Coffee Chat series and just breaking them out this way.

**Jessalynn Jones (she/her):** I know this is like kind of a short term solution to a larger like content mapping and audit that Jakub's doing, but does this make sense to you?

**Jessalynn Jones (she/her):** What this look like in line with what you were hoping for in terms of supporting pieces for the Coffee Chat series?

**Jessalynn Jones (she/her):** Just kind of gist of it?

**Jesse Schor:** Yeah.

**Jesse Schor:** Yeah, definitely.

**Jesse Schor:** I like this a lot.

**Jesse Schor:** I think it's really clear.

**Jessalynn Jones (she/her):** Okay, cool.

**Jessalynn Jones (she/her):** Go ahead.

**Jesse Schor:** These are all, so like these ones here are like new versus like internal linking.

**Jessalynn Jones (she/her):** Cool.

**Jessalynn Jones (she/her):** Yeah.

**Jessalynn Jones (she/her):** So the internal linking is here at the top and then we've got new content ops below that.

**Jessalynn Jones (she/her):** And I'm just trying to identify like a handful for each of the Coffee Chat series because we are doing that larger content audit.

**Jessalynn Jones (she/her):** So I'm sure there's going to be a lot more opportunities coming out of that, but I just want to have at least a few supporting pieces for each of the Coffee Chat series in the noontime while we kind of work on that larger content strategy and audit, if that sounds okay to you.

**Jessalynn Jones (she/her):** Yeah, definitely.

**Jessalynn Jones (she/her):** Do you want me to share this with you?

**Jessalynn Jones (she/her):** Is this something that you want to have eyes on each individual article title for each one or do you want us to just kind of run with it?

**Jesse Schor:** Yeah, definitely share it with me.

**Jessalynn Jones (she/her):** I'll go like poke around.

**Jesse Schor:** Okay.

**Jesse Schor:** And this is really helpful also, I would say for Eric to have, he's out of office saying tomorrow, but like we talked about on one of our previous calls, like I'm kind of like trying to centralize more of our content that like we're distributing across our emails, getting like our email program, like really humming has been like a priority over the last month.

**Jesse Schor:** And same across like our, our social, where we get a good amount of visibility week over week.

**Jesse Schor:** And so he can use this to, to be like preparing for those schedules and calendars as well.

**Jessalynn Jones (she/her):** But, but yeah, I can, I linked it from the agenda, but I can share it in Slack as well.

**Jessalynn Jones (she/her):** And then did you want to just get some eyes on it kind of generally speaking?

**Jessalynn Jones (she/her):** Thank

**Jessalynn Jones (she/her):** Can we leave feedback on stuff, or should we go ahead and kind of run with it, and then just give us feedback if something comes up after you scan it, or do you want to individually approve each one before we get started on it?

**Jesse Schor:** No, definitely, I would say, like, keep running with it.

**Jesse Schor:** If I see anything, like, that really jumps out to me, but, again, I think we're, like, I trust you guys.

**Jesse Schor:** Like, I think we're in a good flow.

**Jesse Schor:** I think, like, especially the coffee chats, like, those are kind of, like, a approval point, I would say, for us.

**Jesse Schor:** Like, so, if it's making it to you guys, you're already kind of getting that perspective, and then I would say, like, you know, I trust your guys' judgment with, like, choosing the right, like, kind of complementary things here.

**Jesse Schor:** Just, like, run.

**Jesse Schor:** Yeah, I don't want to hold us up.

**Jessalynn Jones (she/her):** Sounds like a plan.

**Jessalynn Jones (she/her):** We can do that.

**Jessalynn Jones (she/her):** Awesome.

**Jessalynn Jones (she/her):** So, that's what I have there.

**Jessalynn Jones (she/her):** I'm still adding some stuff to that for each of the coffee chats, but I'll share what I have with you.

**Jessalynn Jones (she/her):** And you can take a look at it, and we'll just.

**Jessalynn Jones (she/her):** Keep cranking away at them.

**Jessalynn Jones (she/her):** The other thing that I wanted to share with you really quick that I've been working on is we are trying to simplify our content OS systems.

**Jessalynn Jones (she/her):** Just because we kind of have a lot in our air table that's not super relevant that you guys need to worry about.

**Jessalynn Jones (she/her):** So we're trying to simplify it for everybody involved.

**Jessalynn Jones (she/her):** Part of that is also setting up some Slack automation.

**Jessalynn Jones (she/her):** So you may or may not have seen these already popping up.

**Jessalynn Jones (she/her):** But basically, you'll get a little Slack bot notification anytime there's something specifically that you need to review.

**Jessalynn Jones (she/her):** Because you don't review necessarily every single piece, you probably will get a ton of these.

**Jessalynn Jones (she/her):** But anytime like a coffee chat blog, for example, is done, you'll get a little Slack bot notification like this.

**Jessalynn Jones (she/her):** And then we also created like a more simplified content OS view for you guys, which hopefully this will make it easier to approve stuff when you do want to get specific approvals on things.

**Jessalynn Jones (she/her):** Go ahead and launch this.

**Jesse Schor:** Very cool.

**Jesse Schor:** Definitely seems helpful.

**Jesse Schor:** You said I might have seen some of these.

**Jesse Schor:** Is this just hooked up through like our main like shared Slack channel or is this like a separate app?

**Jessalynn Jones (she/her):** Yeah, this will just go into our shared Slack channel.

**Jessalynn Jones (she/her):** So anytime like Rachel or I would move something to like ready for webstacks review, it would, it would just shoot you a little link to the doc and then also like a notification there.

**Jessalynn Jones (she/her):** But hopefully this is a little bit easier.

**Jessalynn Jones (she/her):** If you, so there's tabs here on the side that kind of simplify the view for each task.

**Jessalynn Jones (she/her):** So topics awaiting approval, you can click into any of these and instead of trying to figure out which one you should toggle to, you can just say either approve or reject and the automation will click in and update the status for us.

**Jessalynn Jones (she/her):** So you don't need to worry about that.

**Jessalynn Jones (she/her):** You can see details here, and then under ready for review, so like right now you have two coffee chats that are awaiting review, again, you can just click approve or hold article, depending on whichever one you want, there's a link to the doc, additional information here, you can also click into these and blow them up if you want more details on it, and then ready the stage is just like if you guys had approved something and you're wondering if it had been published or not, like basically if it was pending publishing, you will see it here, and then all the published articles, you can find here, if you ever want to look back at them, with all of the meta information and all of that.

**Jesse Schor:** Okay, awesome.

**Jesse Schor:** Yeah, this is great.

**Jesse Schor:** Can you share the link for this?

**Jessalynn Jones (she/her):** I just like looked through our Yeah.

**Jesse Schor:** Slack.

**Jesse Schor:** I see your screenshot in the agenda, but Yeah.

**Jesse Schor:** I'm not seeing that on my end.

**Jesse Schor:** Was that from here or is this?

**Jessalynn Jones (she/her):** Oh, the screenshot in the agenda was just from my own Slack box.

**Jesse Schor:** I ran a test.

**Jessalynn Jones (she/her):** So you probably haven't gotten any notifications yet, but that's what it will look like when you do get it.

**Jessalynn Jones (she/her):** But yeah, I just shared a link to this specifically.

**Jessalynn Jones (she/her):** Go ahead and share.

**Jessalynn Jones (she/her):** Let's see.

**Jessalynn Jones (she/her):** I, is there.

**Jessalynn Jones (she/her):** I'm trying to think if any, does anyone else want access to this?

**Jessalynn Jones (she/her):** You think on your.

**Jesse Schor:** would say Eric.

**Jesse Schor:** Yeah.

**Jesse Schor:** If you can give Eric access as well.

**Jesse Schor:** That should be it from our end.

**Jessalynn Jones (she/her):** Perfect.

**Jessalynn Jones (she/her):** All right.

**Jessalynn Jones (she/her):** So I just invited both of you guys.

**Jessalynn Jones (she/her):** I will link this at the top of all of our agendas and all

**Jessalynn Jones (she/her):** Get in Slack, too, the content OS, so you guys have that simplified view and easy access to it.

**Jessalynn Jones (she/her):** But yeah, that's about it for me this week, I think.

**Jessalynn Jones (she/her):** Yeah, I think that was all that we had, sure.

**Jessalynn Jones (she/her):** Anything else that you need from us, though, right now?

**Jessalynn Jones (she/her):** Or any questions on the content OS or any of that workflow?

**Jesse Schor:** No, no, I love that.

**Jessalynn Jones (she/her):** Okay, cool.

**Jesse Schor:** Yeah, I think that will definitely help me help you guys.

**Jessalynn Jones (she/her):** Better.

**Jesse Schor:** Awesome.

**Jesse Schor:** But no, that's very cool, yeah.

**Jesse Schor:** Jacob, I know as you're going through the audit more and everything, if like you have questions or if like there's data, like additional data that would be helpful or anything like that, let me know.

**Jesse Schor:** We use SEMrush, Ahrefs, I have a lot of things running in there, so like if I can export any of the like reports from there, things like that.

**Jesse Schor:** If would help you with anything, just like let me know.

**Jesse Schor:** I know you guys probably have those things set up on your end too, but yeah, we might have like more historical data and stuff.

**Jesse Schor:** And otherwise, the dashboard updates or the pages or data points, sorry, on the Google Sheet, I started adding in a few more fields that should start populating on here.

**Jesse Schor:** Sure.

**Jesse Schor:** Okay.

**Jesse Schor:** So I added in like a few additional fields based off of the doc.

**Jesse Schor:** There's a few things that I am able to like get some of the data in for.

**Jesse Schor:** But I don't know that it's, like, the best way to do it, in particular with our pages seen.

**Jesse Schor:** So getting, like, the way HubSpot does it is, like, they have, like, events for pages.

**Jesse Schor:** They're not, like, individual properties for, like, the pages that are seen.

**Jesse Schor:** So, like, we have first page seen, they also have last page seen, and recent page seen.

**Jesse Schor:** So those are ones that are properties, they're updated after someone completes a session.

**Jesse Schor:** I can add those in as properties in here.

**Jesse Schor:** But to add, like, every page, I agree 100%, it would be super helpful.

**Jesse Schor:** But we probably would want to, like, set up APIs to, like, a database where, like, that can all live.

**Jesse Schor:** Um.

**Jesse Schor:** Because it's, it's like different, a different object within HubSpot, they don't like, keep track of all those things, contact record, it's all like based off the like session event, basically, so it's in HubSpot, like, it's doable to like, pull reports now like, first page scene, last page scene, recent page scene.

**Jesse Schor:** It's not like necessarily the best, like reflection of everything, but I figured that's like a stopgap that like we can have for now.

**Jesse Schor:** Yeah, for sure.

**Jessalynn Jones (she/her):** Yeah.

**Jesse Schor:** And then I think, for the most part, everything else should be in here.

**Jesse Schor:** The other thing is with updated date, we have like date added and updated date.

**Jesse Schor:** I think your team needs to do these like last updated date.

**Jesse Schor:** And.

**Jesse Schor:** Like date added, we might be able to like add something in here that like does it automatically, but we might, if like we're going to have like last updated date, we might have to have like a separate sheet because like this is last updated date, if I'm understanding correctly, it's the last updated date in like this sheet, but HubSpot, like the workflow that we have set up, it's kind of like rudimentary.

**Jesse Schor:** So like it doesn't like find an update, it would basically add a new record all together.

**Jessalynn Jones (she/her):** Oh, okay.

**Jesse Schor:** So that makes it like a little bit challenging.

**Jesse Schor:** We could create like a separate sheet for this and like kind of like duplicate some of the efforts, but I don't know if that's like the best approach.

**Jessalynn Jones (she/her):** Yeah, so the date added, think, I'm to remember from this, do we have like create date for the contact in here?

**Jesse Schor:** We have create date for the contact.

**Jesse Schor:** We don't, so like date added, I think is like, add it to this, you know.

**Jessalynn Jones (she/her):** Yeah, to this spreadsheet.

**Jessalynn Jones (she/her):** Right.

**Jesse Schor:** And that's like, we can create a formula basically for like, you know, updating anytime a new record gets added in here.

**Jessalynn Jones (she/her):** Yeah.

**Jesse Schor:** That's pretty straightforward to do, but I don't know if there's like another way you guys would want to do that.

**Jesse Schor:** I would say like, if we're going to do that, then like, we probably want to omit this like, last updated date, just because it's going to trigger the workflow right when like, the contact meets that like, criteria.

**Jessalynn Jones (she/her):** Right.

**Jessalynn Jones (she/her):** Yeah, that makes sense.

**Jessalynn Jones (she/her):** And I felt like it had something to do with, like, when contacts were updated and HubSpot potentially changing or something after, like, being added to the sheet.

**Jessalynn Jones (she/her):** Can you remind me, like, what the thought process was behind having that?

**Jessalynn Jones (she/her):** Because, like, if I remember correctly, that was something that you had brought up, that the create date was not going to be sufficient enough, that you wanted the date added as well?

**Jesse Schor:** Yeah.

**Jesse Schor:** So some of the contacts, like, exist, right?

**Jesse Schor:** Right.

**Jesse Schor:** So, like, the date that they're created is going to be, you know, when they fill out an ad a year ago.

**Jessalynn Jones (she/her):** Right.

**Jesse Schor:** Right.

**Jesse Schor:** So, like, when they convert on something or view one of our pages, and we want to be able to, like, capture that information, we want to be able to, like, look back on, like, what was the date that, like, this event took place?

**Jessalynn Jones (she/her):** Right.

**Jesse Schor:** Right.

**Jesse Schor:** Okay.

**Jesse Schor:** That makes sense.

**Jessalynn Jones (she/her):** Okay.

**Jesse Schor:** This is, like, it's not necessary.

**Jesse Schor:** Necessary here, like, we can put together a pretty good story, for sure, using some of these other things, especially adding in, like, recent conversion date, so this will be, like, the last date that they filled out a form, so, like, we can kind of, like, piece together some of these things, but because in the workflow, we're basically just saying, like, they viewed one of our blog pages, and they filled out a form, were basically saying, like, if they viewed a blog a month ago, and then saw one of our ads, we came up in ChatGPT, whatever it is, and then, you know, they converted again, like, technically, they would run through this, but we wouldn't necessarily be tying it back to, like, the blog happened in the session that led, right?

**Jesse Schor:** Now, like, I don't think that's, like, the biggest deal in the world, and especially, like, we have...

**Jesse Schor:** MQL date, opportunity date, like, these should start coming in now.

**Jesse Schor:** And so, like, across, like, these, we should be able to kind of have a good sense of, like, based off timing, you know, initially converted to, you know, when they became pipeline, et cetera, like, whether or not the blog is something that influenced, you know, that.

**Jessalynn Jones (she/her):** Yeah.

**Jessalynn Jones (she/her):** That makes sense.

**Jessalynn Jones (she/her):** Well, that case, I feel like we can just use, like, a generic formula for the date added or just get rid of it altogether if you're comfortable just going off of recent conversion date or MQL date to kind of get a picture of when their latest action was.

**Jesse Schor:** Okay.

**Jesse Schor:** Cool.

**Jesse Schor:** I would say, like, if we want, just because, like, you guys had, this is from your, like.

**Jesse Schor:** Our reporting team, yeah.

**Jesse Schor:** Right.

**Jesse Schor:** So, like, maybe if you want to double check with them if, like, they want to add.

**Jesse Schor:** The formula in here, that's going to be best for them to work with, to fill this in.

**Jesse Schor:** Good with like having that in here as just like, yeah, something that gets populated and then we'll have these things in here as well.

**Jesse Schor:** So like, yeah, moving forward, we'll be able to kind of put it together and I think we'll continue with it as we see how the results look.

**Jessalynn Jones (she/her):** All right.

**Jessalynn Jones (she/her):** Sounds good.

**Jessalynn Jones (she/her):** I will go ahead and share this back over to them and see if they need anything else, but thanks for working on getting those extra data points pulled in.

**Jessalynn Jones (she/her):** That'll be really helpful.

**Jesse Schor:** Yeah, totally.

**Jesse Schor:** I guess one more thing to call on, sorry, I just realized we're like five minutes over, but really, really fast.

**Jesse Schor:** The, I include it like contact ID on the deal tab.

**Jesse Schor:** HubSpot basically sends it over as like an array.

**Jesse Schor:** So like, it's possible that there's like multiple.

**Jesse Schor:** Contacts associated, so just so your team knows, they shouldn't be separated by semicolons, but that's how they'll be able to kind of match up against that contact data of like the contacts, you know, page that they viewed, what blog they looked at, when, et cetera, when they convert it, and then match that type of data to join with the deal data that that contact is associated with.

**Jesse Schor:** And you can even do that at a company level with the company ID, so once you guys kind of like get into the reporting and the tables are joined, even if a contact isn't associated to a deal, because it's possible, like, yeah, they're not part of the sales process, but like they're part of the company, that is, you know, a way that you guys can also kind of check against to see, like, did someone from this company, maybe check out content.

**Jesse Schor:** Maybe there was, you know, conversation about it, word of mouth, whatever, but like, eventually, you know, someone reached out and started a sales conversation.

**Jessalynn Jones (she/her):** Yeah, that makes sense.

**Jessalynn Jones (she/her):** All right, cool.

**Jessalynn Jones (she/her):** Well, thank you again for pulling that together.

**Jessalynn Jones (she/her):** I'll get with our reporting team either later today or tomorrow and see if there's anything else I need, but that'll be super helpful.

**Jesse Schor:** So thank you.

**Jessalynn Jones (she/her):** Sounds good.

**Jesse Schor:** right.

**Jessalynn Jones (she/her):** Thanks, guys.

**Jessalynn Jones (she/her):** Have a great rest of your week.

**Jessalynn Jones (she/her):** Good to see Good to see you.
