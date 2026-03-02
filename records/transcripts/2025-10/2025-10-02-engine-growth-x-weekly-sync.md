# Engine <> Growth X - Weekly Sync

<metadata>
date: 2025-10-02
time: 18:30 UTC
duration: 43 minutes
organizer: team@growthxlabs.com
participants: Carrie Chowske, Joel Murphy
fathom_recording_id: 91516818
fathom_url: https://fathom.video/calls/427808781
share_url: https://fathom.video/share/kiUCS4ZbiX96t4SyE3QA9Wc4MXjBQ9Jp
source: fathom
enriched_on: 2026-03-02 14:35 UTC
</metadata>

---

## Summary

Carrie Chowske (GrowthX) and Joel Murphy (Hotel Engine) reviewed content performance, which shows month-over-month growth across most clusters, with industry-specific content and practical tools performing particularly well. The team discussed shifting from cluster-based tracking to persona-based tagging to better align reporting with how customers actually benefit from content, and decided to explore direct access to Hotel Engine's AI analysis tool—which ingests sales call data—to improve GrowthX writing guidelines and content tone. Key next steps include finalizing persona tracking implementation, running new pages through the AI tonality tool, and beginning a programmatic per diem content cluster.

---

## Context

Hotel Engine is a travel and expense management platform for mid-market companies. GrowthX handles content marketing for Hotel Engine, creating educational and SEO-focused articles targeting decision-makers and administrators who book corporate travel. This is a weekly sync to review content performance data, discuss strategy refinements, and align on new initiatives. Kyle Gaudreau (GrowthX's performance analyst) was out sick, so Carrie took the lead on performance updates. The relationship is six months into content delivery, having moved past "low-hanging fruit" SEO wins and now focusing on deeper, persona-targeted content that addresses specific customer pain points and business outcomes.

---

## Relevance

**To GrowthX Delivery:** Hotel Engine's AI analysis tool (built on vectorized sales call data) can directly inform GrowthX writing guidelines. Carrie wants to test feeding the AI's tonality and confusion-point data into Atlas (GrowthX's LLM writing system) to improve content specificity and voice. This requires exploring direct API access or a workflow with Hotel Engine's Rory (who built the tool) so GrowthX team can prompt it directly rather than manually transcribing results.

**To Hotel Engine Business Development:** Persona-based content tracking will provide Hotel Engine with better ROI metrics tied to customer segments (e.g., construction admins spend more, are the highest-value segment). Monthly growth across most clusters suggests content strategy is working; industry-specific and practical tools outperform other content types. New per diem cluster (state-by-state GSA rates) launching in October with Alaska as a pilot.

**To Content Strategy Alignment:** Current cluster-based tracking is manual and internal-only (weekly Airtable exports). Shifting to persona-based tagging via Amplitude will automate reporting and surface which content drives conversions by buyer role. Proposed new cluster structure: travel/spend integration, cashflow/financial strategy, travel policy/compliance, maximizing ROI, modern travel tech—organized around customer pain points rather than topics.

---

## Overview

- Month-over-month growth across most content clusters; travel management/corporate travel down 7% due to lack of new content, but industry-specific content and calculators showing strong performance
- Testing persona-based content tagging (via Amplitude) instead of cluster-based tracking to better align reporting with business outcomes
- Exploring direct integration with Hotel Engine's Cargo-powered AI tool that analyzes sales calls to inform content tone, specificity, and customer confusion points
- Proposing consolidated content cluster structure (5 core clusters based on customer pain points) instead of current broader approach
- Launching programmatic per diem cluster with state-specific GSA/ACONIS rate content, starting with Washington D.C. and other high-search-volume states
- Reconciling two "What is Hotel Engine" product pages with canonicalization and AI tonality review

---

## Key Topics

### Content Performance Update

  - Month-over-month growth seen across most content clusters
  - Travel management and corporate travel down 7%, likely due to lack of new content
  - Industry-specific content and calculators/practical tools showing strong performance
  - Technology and software solutions cluster unexpectedly high, warranting further investigation

### Content Tagging and Tracking

  - Discussing implementation of attribute tagging for GrowthX-created content
  - Considering persona-based tagging over cluster-based for better alignment with business goals
  - Joel to provide insights from AI analysis of sales calls to inform persona-specific content strategies

### Content Clustering Refinement

  - Current approach has too many clusters; proposing consolidation from current structure to 5 core clusters organized around customer challenges and pain points rather than topics
  - Proposed new core clusters: travel and spend management integration (cross-sell opportunity for Engine + EngineX), cashflow and financial strategy, travel policy and compliance, maximizing travel ROI, modern travel management technology
  - Consolidating some clusters into tags within core clusters to streamline tracking and reporting
  - Aim to align content structure with how customers actually think about problems, not just topics

### AI-Powered Content Optimization

  - Hotel Engine using an AI tool analyzing sales call data to improve content tone and specificity
  - Exploring ways to integrate this tool's insights with GrowthX's content creation process
  - Discussing potential for direct access to the AI tool for GrowthX team

### Per Diem Content Strategy

  - Planning mini-cluster of programmatic content for per diem rates
  - Focusing on high-search volume states and specific cases (e.g., Washington D.C., international rates)
  - Testing approach with Alaska-specific content before expanding

### Product Page Content Review

  - Identified newer "What is Hotel Engine" page, considering consolidation with older version
  - Joel to review both pages and determine best approach for canonicalization and content updates

---

## Action Items

**Carrie Chowske (GrowthX)**
- Flag convo re: performance tracking for Kyle Gaudreau. Discuss clustering/persona tracking options when he returns
- Talk with Kyle when he's back regarding subreddit content and scrunch prompts progress


**Joel Murphy (Hotel Engine)**
- Share doc with points of confusion from sales calls. Include persona-specific confusion points (e.g., finance admins, construction admins, travelers)
- Ask Rory (Hotel Engine marketing team) about connecting GrowthX team directly to AI analysis tool for prompting, or determining most efficient workflow for providing AI outputs
- Run newer "What is Hotel Engine" product page through AI tonality tool. Provide output to GrowthX team, including line-by-line recommendations
- Run 4-5 additional product pages through AI tool to develop writing guideline training data
- Reconcile older and newer "What is Hotel Engine" pages: determine which has more traffic and use as canonical, redirect the other

---

## Transcript
**Carrie Chowske:** Hey, how are you?

**Joel Murphy:** Good, how are you doing?

**Carrie Chowske:** Good, good, good, good.

**Carrie Chowske:** I think it's just probably the two of us today.

**Joel Murphy:** All right.

**Carrie Chowske:** I think we can make it fairly quick, unless you have a ton of questions for me.

**Carrie Chowske:** But Kyle's out sick, and I think he had planned on having something with the new scrunch prompts, but I don't have that from him. So I'll just do a review of what I could see and give you a little bit of an update on that. Let me share my screen. Why do I always have so many windows open? I would learn at some point, like, Carrie, why don't you close one of your tabs? But that doesn't happen for me. So thank you so much for reading that content. Last night I saw your comments coming in, and I was like, do I get up out of the recliner and go check my email? No, not going to do it. But I did check it first thing this morning.

**Joel Murphy:** So I think we have all but one already published. Yeah, I was just looking through the remaining one. I didn't see my comments. I guess they were resolved.

**Carrie Chowske:** Okay, I'm sorry about that.

**Joel Murphy:** I just wanted to make sure I wasn't crazy.

**Carrie Chowske:** No, you're not crazy. I had said to.

**Carrie Chowske:** I said to Faye not to like resolve them, but I'll talk to her again.

**Carrie Chowske:** She was out of office yesterday.

**Carrie Chowske:** So I didn't get a chance.

**Carrie Chowske:** I didn't think she would be doing anything with them.

**Carrie Chowske:** And I think because she's just on a different, she's in a different time zone.

**Carrie Chowske:** So I think probably she just got to them before I did.

**Carrie Chowske:** And that was why.

**Carrie Chowske:** But I see your comment about there was like a feature mentioned that didn't exist or whatever.

**Carrie Chowske:** I'm going to have to go back in and look at what our guidelines are feeding because it's supposed to be referencing the docs that you gave us.

**Carrie Chowske:** So like, it shouldn't be bringing up stuff other than that.

**Carrie Chowske:** And so I hadn't had to check it, double check that directly recently.

**Carrie Chowske:** So I didn't check that against that list.

**Carrie Chowske:** So that's probably how that ended up in there, but I'll go in and I'll make sure that we have it correct.

**Carrie Chowske:** And the place like have what we're feeding at least correctly and then see if our engineering team needs to step in and fix anything.

**Joel Murphy:** Cool.

**Carrie Chowske:** All right.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Um, but were there any other major, major ones?

**Carrie Chowske:** Besides the one you tagged me in?

**Joel Murphy:** No, no, no.

**Joel Murphy:** There were, I think it was just that one.

**Joel Murphy:** And then there might've been a couple other like small tweaks.

**Joel Murphy:** They were in stuff that I approved just like, you know, not blockers, just like very minor tweaks.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I mean, we definitely want to get it right.

**Carrie Chowske:** We shouldn't need, you know, super crazy stuff.

**Carrie Chowske:** And certainly for getting stuff wrong about the product.

**Carrie Chowske:** mean, we've been a little more, putting a little bit more of a laser focus on that.

**Carrie Chowske:** But I know with like, like I said, with Faye being out too, sometimes it's, things get lost in that shuffle.

**Carrie Chowske:** So I'll make sure to pay a little more attention until we know that we're getting there a hundred percent.

**Carrie Chowske:** Cool.

**Carrie Chowske:** As far as performance, I pulled back a little bit this week since we talked some about that issue with Google and the way that it's like, um, allowing, like how many, how many, like...

**Carrie Chowske:** Queries per page.

**Carrie Chowske:** It's basically saying, like, instead of looking at 100, which you had to modify anyway.

**Carrie Chowske:** Google is apparently claiming we never supported that.

**Carrie Chowske:** So it's fine.

**Carrie Chowske:** It's fine.

**Carrie Chowske:** Yes, you did.

**Carrie Chowske:** But that's fine.

**Carrie Chowske:** Maybe not officially.

**Carrie Chowske:** Don't you love that?

**Carrie Chowske:** But anyway, we've kind of leveled off from that.

**Carrie Chowske:** So that's good.

**Carrie Chowske:** I think just I will tentatively say I think we can rely on the impressions and clicks data as much as we could before, which, you know, I'm just going to laugh at that.

**Carrie Chowske:** But I don't think we're going to see any other effects from that.

**Carrie Chowske:** The impressions that were lost are lost, lost in quotes.

**Carrie Chowske:** I just don't think that that's going to continue to be an issue.

**Carrie Chowske:** I think what I've noticed across the board, across all of our clients, and I'm hearing other editors say, is that we're seeing the drop in impressions, an increase in clicks.

**Carrie Chowske:** And that's kind of translating to a lot more, you know, page one and two ranked keywords.

**Carrie Chowske:** So let's...

**Carrie Chowske:** Be real, nobody's scrolling past that second page anymore nowadays anyway.

**Carrie Chowske:** So in a lot of ways, some of that's really good that we're able to focus on what is performing.

**Joel Murphy:** Okay, cool.

**Carrie Chowske:** But I'll keep an eye on it and let you know if I notice anything else.

**Carrie Chowske:** But Google's saying, we're not going to go back to supporting that, even though we never supported it before.

**Carrie Chowske:** Okay.

**Carrie Chowske:** Really Google.

**Carrie Chowske:** Anyway.

**Carrie Chowske:** And again, things are going to continue to change, obviously, with the AIO reviews and stuff.

**Carrie Chowske:** But there's good news in that department, too.

**Carrie Chowske:** So I'll talk about that in a second.

**Carrie Chowske:** Month over month, too, saw some pretty good growth.

**Carrie Chowske:** This chart's a little misleading because the way that – I hate the way that our cohorts group this.

**Carrie Chowske:** But because the way they each grew, because certain ones grow and then other ones – anyway, it's just funny to me the way that this always works out.

**Carrie Chowske:** But there's pretty good growth across pretty much all of the clusters.

**Carrie Chowske:** I want to say there was, like, one or two that didn't growth – didn't show, like, growth over this period.

**Carrie Chowske:** And –

**Carrie Chowske:** The lack was really small.

**Carrie Chowske:** Travel management and corporate travel is down almost 7%, but we've also not published anything in that cluster.

**Carrie Chowske:** So I'm not surprised by that.

**Carrie Chowske:** And also trying to not use that framing of corporate.

**Carrie Chowske:** But the areas where we have been really focusing, that's where we're seeing the most growth, although this one was kind of surprising.

**Carrie Chowske:** So I want to go see what was going on in that technology and software solutions cluster.

**Carrie Chowske:** I wasn't able to tell just like at the top level, so I'm to see if I can dig into it a little bit more.

**Carrie Chowske:** But also not surprising, because we've had success for it before, is the industry-specific content.

**Carrie Chowske:** We know that performs pretty well.

**Carrie Chowske:** And then the calculators and practical tools.

**Carrie Chowske:** I suspect that a lot of this kind of has to do with, too, though, some of the stuff that Barry's been doing.

**Carrie Chowske:** Obviously, the stuff he does isn't categorized in with this.

**Carrie Chowske:** This is just going to, any of these cohorts are going to be just the growth X.

**Carrie Chowske:** Content, but that also could be creating additional like, you know, draw for us.

**Carrie Chowske:** So I'm not surprised by that, though, because it's, know, it's about making things usable and making things, you know, useful to people.

**Joel Murphy:** And that's always going to be good for content.

**Joel Murphy:** Cool.

**Joel Murphy:** So related to this, we had talked about at some point last couple of weeks, adding some sort of attribute on page for the content.

**Joel Murphy:** you guys are creating that would allow us to better report on, I think, I want to say we talked about personas.

**Joel Murphy:** And maybe that, that's, I'm connecting that to our clusters.

**Joel Murphy:** I don't remember if was clusters or if it was personas or.

**Carrie Chowske:** Might have been.

**Carrie Chowske:** I know we talked, well, one thing I remember is were talking about like having some sort of like query parameter so we could look at like specifically more about like what, where are, where people were going after.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** And I hit any of the GrowthX created content, but.

**Joel Murphy:** Yeah, maybe that's, that was the, the idea.

**Joel Murphy:** So I looked into it and so we can include like, let's say a dropdown field in a blog post that when you guys are creating content, you tag it with whatever value we want.

**Joel Murphy:** And we can on the, the amplitude side, bubble that up to amplitude on the page view event.

**Joel Murphy:** Okay.

**Joel Murphy:** And then we would be able to, in, in amplitude, see any traffic that included that parameter.

**Joel Murphy:** So that in theory would include everything you guys are working on.

**Joel Murphy:** And then wherever they went after that, we could also segment it by that value as well.

**Joel Murphy:** So we could say, you know, this group of posts is performing better than this other one, that kind of thing.

**Joel Murphy:** So my question is, how do we want to segment it?

**Joel Murphy:** What parameter do we want to use?

**Joel Murphy:** Is it cluster?

**Joel Murphy:** Is it persona?

**Joel Murphy:** Is it something else?

**Carrie Chowske:** I mean, I think it comes down to what's going to be more useful for you in terms of who, you know, like I would instinct is to say persona, because I feel like that's going to be more useful to you and looking at it that way rather than looking at these clusters.

**Carrie Chowske:** I also kind of, I have a, I have a thought about maybe changing some of the clusters.

**Carrie Chowske:** The other issue with the clustering is that that's almost exclusively internal to us.

**Carrie Chowske:** So for us to be able to track it and what we're doing to do that is an manual like export from Airtable every, every week to add new URLs to that, that cohort.

**Carrie Chowske:** So we have to like, so I mean, we could easily give you that same information, but it would be.

**Carrie Chowske:** I don't think it would give us enough data that would be beneficial for the amount of effort it would take on both our parts to do it.

**Carrie Chowske:** I just don't think it would give you as much as it would to say, well, if you're tracking other things to look at your personical cohorts, that might be the better route for you.

**Joel Murphy:** Right, okay.

**Joel Murphy:** So do you feel that the content that you guys are creating, because I know a lot happened before I started reviewing it, so I'm looking for a gut check more than anything.

**Joel Murphy:** Do those neatly enough map to personas that we, like construction or maybe it's more than one persona in certain cases?

**Carrie Chowske:** It is largely what we aim for.

**Carrie Chowske:** Like, so we try to incorporate various personas unless the content specifically mentions, like, in construction or doing something.

**Carrie Chowske:** Or construction crews or something like that.

**Carrie Chowske:** generally, we're aiming for like a project manager or a site, you know, a site supervisor or, you know, a foreman or something like that, where it's like somebody who's going to be in charge of this crew and needs this information, you know, that kind of thing, they're going to be in a position of, if not a decision maker, they'll have the ear of a decision maker.

**Carrie Chowske:** So that's kind of where we aim for.

**Carrie Chowske:** So it's kind of really written for the person who's booking the travel or the person that's annoyed because the person that's booking the travel can't do XYZ.

**Carrie Chowske:** Right.

**Carrie Chowske:** You what I mean?

**Carrie Chowske:** So like, it's that, it's that kind of area.

**Carrie Chowske:** So I don't think it's, it's very like specific to an industry, but it is specific to a role, if that makes sense.

**Joel Murphy:** Okay.

**Joel Murphy:** So, yeah.

**Joel Murphy:** I don't know.

**Joel Murphy:** Let me think about that.

**Joel Murphy:** Maybe it's more than one, one value that we use, like construction admins, just as a random.

**Joel Murphy:** Example.

**Joel Murphy:** Example.

**Joel Murphy:** Um, construction travelers and admins.

**Joel Murphy:** Construction and oil and gas.

**Carrie Chowske:** You know what I mean?

**Carrie Chowske:** Like.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Like how, how are you, how are you tracking your, your like customer journey right now?

**Carrie Chowske:** Are you doing that by persona or?

**Joel Murphy:** We don't do it well enough.

**Carrie Chowske:** Period.

**Joel Murphy:** Yeah.

**Carrie Chowske:** Understood.

**Joel Murphy:** I'm just trying to look for some signal to say, I feel good.

**Joel Murphy:** Like, you know, the, what you guys are doing.

**Joel Murphy:** Is, is working.

**Joel Murphy:** I don't know.

**Joel Murphy:** I'm just, I guess I'm looking for a signal that, that says this, this content is working especially well with a particular audience that we're, we're concerned with.

**Joel Murphy:** It also, I'm looking at it from a perspective of like, like the reporting structures on the marketing team is changing and, and I'm just prepared, trying to prepare for people to ask like, why do we do this?

**Joel Murphy:** Like, why does this matter?

**Carrie Chowske:** Yeah.

**Joel Murphy:** And trying to.

**Joel Murphy:** Yeah.

**Joel Murphy:** And give them an answer.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** I'll tell you what, I'm going to flag this conversation for Kyle, too, because he's got a stronger background in this kind of performance tracking than I do.

**Carrie Chowske:** Mine's more on the SEO side.

**Joel Murphy:** His is more in the conversion side.

**Carrie Chowske:** And he might have some thoughts on it, too.

**Carrie Chowske:** But my instinct is, like, it is going to be about, like, who you want to make it.

**Carrie Chowske:** It's, I would think you would want it to be traceable in terms of, like, who this person is and who's converting, you know, because you want to know who's converting and what they're doing to get to that point.

**Carrie Chowske:** It's going to help you trace that customer journey, whether you're doing that for content performance or you're doing it for, you know, performance marketing.

**Carrie Chowske:** Like, you're, you know what I'm saying?

**Carrie Chowske:** Like, you're definitely, you definitely want to understand that journey.

**Carrie Chowske:** So I think that there's going to be, but I just don't know what that grouping would be or, like, I also don't know enough about how those tracks.

**Carrie Chowske:** Like, I'm

**Carrie Chowske:** Like something like an amplitude, like how those tracking, that tracking occurs, be able to say to you, yes, we can definitely do that.

**Joel Murphy:** Kyle will be able to tell you that for sure.

**Joel Murphy:** I know that we can do it.

**Joel Murphy:** I'm more just thinking out loud on like the values that we want to feed into it.

**Carrie Chowske:** Right, right.

**Carrie Chowske:** That's kind of what I meant.

**Carrie Chowske:** Like in terms of like me saying to you, the cohorts that we have, like, yeah, I could give you those.

**Carrie Chowske:** But I know that like, it's hard to, unless we're like every week giving you an updated, you know, spreadsheet or, you know, CSV or something of all that.

**Carrie Chowske:** Like it, unless, I don't know, can, can amplitude connect to air cable?

**Carrie Chowske:** But imagine it can.

**Joel Murphy:** I don't know.

**Joel Murphy:** I don't know if it can or not.

**Joel Murphy:** But I'm to say your point a couple of minutes ago about like the clusters are more for internal use.

**Joel Murphy:** And I agree.

**Joel Murphy:** I'm just thinking like, okay, if I had to explain this and I did, I, you know, I shared a team web team newsletter today and I shared some of the, the progress that you guys shared last week.

**Joel Murphy:** Yeah.

**Joel Murphy:** Organized it by cluster, and I think that's fine, but I think if someone were really going in the weeds with it, it's like these clusters, they make sense, but I think it would make more sense if I could say the content clusters are X, Y, and Z, and then where we're seeing some progress is with just, again, going back to construction admins.

**Joel Murphy:** So construction's a huge industry for us.

**Joel Murphy:** Admins do the booking and spend the most accounts with admins, spend more than ones that don't have one.

**Joel Murphy:** So that's a way for me to say from a revenue angle, right?

**Joel Murphy:** Like this content works for these people who spend the most money.

**Carrie Chowske:** Yeah, no, that makes sense.

**Carrie Chowske:** I, we can, that's something too, for like a, if, if we're trying to make that case, that's a, that's even a one-off thing we could do also, like.

**Carrie Chowske:** Do those things like quarterly or something to look at.

**Carrie Chowske:** We definitely have been doing more content in construction.

**Carrie Chowske:** And I probably am looking for, I'm trying to talk and think at the same time, why do I do this to myself?

**Carrie Chowske:** But I'm thinking like in terms of those clusters, there's an industry specific one.

**Carrie Chowske:** And I feel like if I pull that, I can look at some of those specific, like how they're performing compared to other ones in the cluster.

**Carrie Chowske:** So there's things we can do.

**Carrie Chowske:** It's just a matter of like, I want to make it easy lift on both our ends so that we can rely on the data and not be constantly, you know, updating random spreadsheets or something.

**Carrie Chowske:** You know, that's kind of, that's not the antithesis of why we have all these tools, right?

**Joel Murphy:** Yeah, yeah.

**Carrie Chowske:** But yeah, let me, let me talk to Kyle too when he's back and we can kind of dig into that a little bit more.

**Carrie Chowske:** But I think like there's definitely a way and I'm actually, we can even jump ahead if you want a little bit.

**Carrie Chowske:** I wanted to talk about the clustering because I think we've got too many and some of them are just kind of.

**Carrie Chowske:** Out there and not really where we want to focus.

**Carrie Chowske:** We've been talking a lot about focusing some of this stuff.

**Carrie Chowske:** And I just started doing in my preliminary review of your stuff on the new card.

**Carrie Chowske:** I kind of started uncovering like, there's a lot of like, there's four, there's like four or five.

**Carrie Chowske:** This is not in a state that I want to share it with you yet.

**Carrie Chowske:** But like eliminating some of the clusters that we have and having them more as like tags so that they're not full cohorts.

**Carrie Chowske:** We want to look at and looking at travel and spend management integration.

**Carrie Chowske:** Like that's literally going to be the cross section between engine as the platform and engine X as, as a, as a product, you know, and then looking at, you know, cashflow and financial strategy for travel.

**Carrie Chowske:** That's something else that an admin, you know, is going to be looking at.

**Carrie Chowske:** But, and then travel policy and compliance, maximizing your travel ROI and then modern travel management technology.

**Carrie Chowske:** So there's ways for us to talk about.

**Carrie Chowske:** So

**Carrie Chowske:** There's aspects of the product and all of those, but then we're not just all over the place with all these different things.

**Carrie Chowske:** And they're more focused on challenges and pain points than on the topic, if that makes sense.

**Carrie Chowske:** To me, that always makes more sense in an organization structure for tracking than looking.

**Carrie Chowske:** Because when I think about content and how and why we're creating it, I'm thinking about what are we trying to help somebody solve?

**Carrie Chowske:** Because there's human beings on the other end, right?

**Carrie Chowske:** They're not researching a That's where my brain goes as well.

**Joel Murphy:** And so I'm curious.

**Joel Murphy:** I don't remember if I shared this with you guys or not, but I have this content and design guide that I created last month.

**Joel Murphy:** And for the most part, it's like performance and engagement metrics for key pages across our website.

**Joel Murphy:** So when people come in and say, hey, I...

**Joel Murphy:** I want to do something with this page, or I want to redesign it, or whatever.

**Joel Murphy:** It's just like, here's how far people scroll, here's the amount of time they spend, here's where they typically go next, that kind of stuff.

**Joel Murphy:** But an appendix I added on to it is, we have these AI analysis tools that I've mentioned a bunch of times that are based on our sales calls.

**Joel Murphy:** That's the data set that it analyzes with each prompt.

**Joel Murphy:** And I've saved a few of them that are pretty high value in this same doc that I'm talking about.

**Joel Murphy:** And one of them that I asked a couple weeks ago was, what are the main points of confusion or hesitation for people that are considering engine?

**Joel Murphy:** And it gave me a list that I've been using as just sort of my guidepost for like, we're redoing the pricing page right now.

**Joel Murphy:** And I use that as like, okay, what content needs to be here based on what?

**Joel Murphy:** But this thing has told me prospects express about engine pricing.

**Joel Murphy:** And that thing is like, how is engine free?

**Joel Murphy:** I don't get it, right?

**Joel Murphy:** That was one kind of thing that like immediately like, oh, yeah, of course, like that makes sense.

**Joel Murphy:** So anyway, what I'm getting at is I can share that stuff with you guys if it will help to maybe give us some direction for clustering.

**Carrie Chowske:** Yeah, yeah.

**Carrie Chowske:** I definitely think so.

**Carrie Chowske:** So I think is that you shared a doc that was similar to that with us before?

**Joel Murphy:** Is it update?

**Joel Murphy:** Does it get updated regularly?

**Joel Murphy:** Like you have newer data with?

**Joel Murphy:** It depends.

**Joel Murphy:** Well, so that that one, I think I shared the points of confusion with you guys.

**Joel Murphy:** If I remember correctly, that's it's a static doc.

**Joel Murphy:** It's based on a one time thing.

**Joel Murphy:** I'll update it like probably, you know, every few months, I guess, to just see if it's different.

**Joel Murphy:** But the the master doc that contains all of this other stuff that probably a lot of it.

**Joel Murphy:** Well, you guys wouldn't touch a lot of this stuff on the other side.

**Joel Murphy:** That is a living doc and does get updated, but it's not really pertinent.

**Carrie Chowske:** I mean, share with whatever you think will be helpful.

**Carrie Chowske:** I definitely think that that's worth revisiting and looking at because I think like the more too that I personally and Kyle as well have, you know, get to know your product, like the more insight we're able to give too.

**Carrie Chowske:** And I feel like I've got a much bigger, better handle on it now than I did just even like a month ago.

**Carrie Chowske:** Um, and, uh, like you, I inherited some, some content things.

**Carrie Chowske:** So I'm kind of like, well, I think this is going to work.

**Carrie Chowske:** Um, and I'm just finding that like what we were seeing early on, yes, we, we, we grabbed some low hanging fruit, but now it's time to really like hone that strategy a little bit more and really focus it in on, on, you know, um, building out like literally targeting those, those personas.

**Carrie Chowske:** I think that that's a great way to be looking at it right now because the traction you're going to get from that versus say those top.

**Carrie Chowske:** The funnel kind of, you know, low-hanging fruit keywords.

**Carrie Chowske:** Like, we've got all that that we're going to get.

**Joel Murphy:** You guys have a ton of content on your site.

**Carrie Chowske:** Like, there's no reason that we shouldn't be grabbing that stuff.

**Carrie Chowske:** Okay, now what's next, you know?

**Carrie Chowske:** And, like, looking at, I don't know if you saw, Colm had asked me for some traffic on Spaces. And even just looking at that, like, using Perplexity, I had to analyze a bunch of data and it said, like, you know, what do you think based on this, and where it would be. And it's looking at your traffic, your domain authority, all these different things, your backlink profile, everything, and going, yeah, I think you can grab a substantial portion of this. Here's something really reasonable. Like, I think this is totally doable. And here's a high-end, pie-in-the-sky kind of moment, right? And both of those, compared to the search volume on the few keywords that I gave it, it's about 60% of the search volume. That's monthly. And so that seems pretty solid. So that says to me that there are good things there, but the more that you can convert on those clicks, that's where we really should be looking. And I don't want to get that wrong, you know?

**Joel Murphy:** I mean, not that we can't.

**Joel Murphy:** So it seems like we have, like, as far as clusters, and maybe they're not mutually exclusive, but we have these clusters that are kind of, like, laying the groundwork for new products, EngineX, and Spaces, right?

**Joel Murphy:** And then there is, the Venn diagram is inevitably going to overlap with, like, more persona-based stuff with those products as well, right?

**Joel Murphy:** So it's, like, travel, groups, EngineX, Spaces.

**Joel Murphy:** And what I like about using those points of confusion is...

**Joel Murphy:** And it'll make more sense when you see it, but it's kind of like taking the straight from the horse's mouth.

**Joel Murphy:** Like what do we need to help them solve?

**Carrie Chowske:** It's these things.

**Carrie Chowske:** Yep.

**Carrie Chowske:** Yep.

**Carrie Chowske:** That's what, that's really, yeah.

**Carrie Chowske:** And that's going to, think going to be the key.

**Carrie Chowske:** If you're going to diversify like what you're offering to your ICP, you've got to be able to talk about it in terms that are like, well, what can you do?

**Carrie Chowske:** It's the old, well, what can you do for me?

**Carrie Chowske:** Like, what's that mean for me?

**Carrie Chowske:** I don't care about what your product does.

**Carrie Chowske:** I want to know what it does that, you know, I want to know what it's going to do to make my day easier, you know, standard, standard B2B stuff.

**Carrie Chowske:** But it is, it is really the, I mean, you think about, I don't know about you, but like for me deciding on, on stuff like that, that's what I want to know.

**Carrie Chowske:** Like, tell me how it's going to make my day-to-day tasks that I do all the time easier.

**Carrie Chowske:** And if you can't tell me, that's like, that's me telling Marcel that the other day on our product, like, or, you know, not, not him, it's not directly to him, but like filling out, you know, you're answering questions.

**Joel Murphy:** It's like, what do you think should improve about XYZ?

**Carrie Chowske:** And.

**Carrie Chowske:** That's me.

**Carrie Chowske:** If it can't make this easier for me, if I'm having to work around it, it isn't working.

**Carrie Chowske:** If it's not working for me, it's not working.

**Carrie Chowske:** Which is hard to say, right?

**Carrie Chowske:** Because a tool can work in a lot of ways, but if it's not hitting those use cases of the people that are using it every day, it's not useful to them.

**Joel Murphy:** Right.

**Joel Murphy:** Yeah.

**Joel Murphy:** That can turn one product cluster, say Nginx, that kind of fans out to all these personas, right?

**Joel Murphy:** And makes just that product cluster alone pretty big, right?

**Joel Murphy:** Because there's people that are going to care about the finance side.

**Joel Murphy:** You know, there's going to be some, I'm a traveler benefit, right?

**Joel Murphy:** Like, hey, you don't have to use your own credit card to check in.

**Joel Murphy:** mean, we have incidentals coverage.

**Joel Murphy:** And I asked, does this replace an incidental coverage?

**Joel Murphy:** And they don't know.

**Joel Murphy:** Let's just say that it does, right?

**Joel Murphy:** So this is like introducing that so they can then prompt their admin, can we please you as engine so I don't have to use my credit card, you know, that kind of thing.

**Joel Murphy:** And I think it grounds all of our work in thinking about it from an executive standpoint.

**Joel Murphy:** Of course, they care about our new product launches.

**Joel Murphy:** And if I can say that these personas relative to these products are all based on things that we pulled from sales calls, it's really tying it all together for them, I think.

**Carrie Chowske:** Yeah, I agree.

**Carrie Chowske:** I think that grouping them in ways that are about those problems or those, you know, those questions that they're having, the points of confusion, I think that's going to make a lot more sense in the long run.

**Carrie Chowske:** And that's pretty much, more or less, mean, different wording maybe, but like, kind of where I was thinking too, because what's cool with the, I mean, first of all,

**Carrie Chowske:** Like there's a lot that's really a differentiator about the about the Nginx product, you know, like that's there's a lot of differentiation there from and there's also the appeal of people do like those.

**Carrie Chowske:** They love travel rewards.

**Carrie Chowske:** Like those are the kinds of things that, you know, sell people on cards, you know, and and especially I can say this, especially my my brother has held on to he's I think I told you this, but he does like maintenance.

**Carrie Chowske:** he builds, maintains, repairs, troubleshoots, all these like gigantic manufacturing machines, like things and builds them from scratch, not just like, you know, but like so that make like laminate flooring and stuff like that.

**Carrie Chowske:** And he goes all over the world repairing these things, troubleshooting them on site and everything.

**Carrie Chowske:** And the only thing right now, I think keeping him doing that job is the amount of airline miles that he racks up so he can go wherever he wants.

**Carrie Chowske:** He's going he's going to Japan and like February, you he went to Puerto Rico this, you know, he's he went to Ireland and Scotland this year, like.

**Carrie Chowske:** You know, that stuff.

**Carrie Chowske:** He couldn't afford to do or have, you know, or, and certainly not in travel and business class, you know, so like there's a, there's a lot of, there's a lot of thing there that's appealing to this particular, like these, all these industries that you serve too about that, you know.

**Joel Murphy:** Yeah.

**Joel Murphy:** So here's what I'll do.

**Carrie Chowske:** I'll share that doc.

**Joel Murphy:** I really don't remember if I shared it with you guys or not.

**Joel Murphy:** And then what I can't, what I can do in the tool is, you know, I just asked it.

**Joel Murphy:** What are basically all the confusion, points of confusion across every type, but I can narrow it down.

**Joel Murphy:** Like how about finance admins?

**Joel Murphy:** How about, you know, this person, that person and see what the subtle differences are between those.

**Joel Murphy:** And then, you know, maybe that can guide us a little bit better.

**Carrie Chowske:** Cause that's going to help tie it to, for tracking purposes, to your personas better.

**Carrie Chowske:** And also there, it's going to be some overlap.

**Carrie Chowske:** So that'll also tell us too, that it's, you can say, you know, this cluster is, is this persona and this persona, you know.

**Carrie Chowske:** You can kind of see that, but I think it'll serve both purposes, I think, really well.

**Joel Murphy:** Cool.

**Joel Murphy:** All right.

**Joel Murphy:** I'll work on that and send that over.

**Carrie Chowske:** Okay.

**Carrie Chowske:** That sounds good.

**Carrie Chowske:** A couple other very quick things.

**Carrie Chowske:** You'll start to see, did a little, we did a little mini PSEO cluster, some programmatic stuff for you in this per diem thing.

**Carrie Chowske:** When I started looking at, like, calendar-wise, like, they just released the 2026, you know, GSA and ACONIS rates, which are the same as 2025.

**Carrie Chowske:** It's no different.

**Carrie Chowske:** But I did notice Barry just updated his post on it.

**Carrie Chowske:** And so we have this per state one, and we're going to just do, we're going to knock out a few states because these had some pretty significant search volume.

**Carrie Chowske:** So specifically one for D.C.

**Carrie Chowske:** because no one ever knows where it goes because it's not a state.

**Carrie Chowske:** And the answer's really easy, actually.

**Carrie Chowske:** They're using the GSA lookup, but anyway.

**Carrie Chowske:** But, like, international per diem, that ACONIS one, there's some different states.

**Carrie Chowske:** We've already done one for Alaska to see how well, if we were able to kind of like replicate it.

**Carrie Chowske:** And so these are ones we can relatively easily do.

**Carrie Chowske:** They're ones that have some variants from, so they have variants from the GSA lookup and variants from, and they have pretty good search volumes.

**Carrie Chowske:** So we're just going to run like a few, see if it gets any additional traffic.

**Carrie Chowske:** It's a good time to do it.

**Carrie Chowske:** And we can do them relatively quickly and, you know, just bing, bang, boom, knock a few out.

**Carrie Chowske:** So anyway, if that's cool with you, we'll just move forward on it.

**Carrie Chowske:** Yeah, sounds good.

**Carrie Chowske:** Okay.

**Carrie Chowske:** And then, yeah, this was, this, oh, this was another thing.

**Carrie Chowske:** So I also noticed that in addition to the page that you reviewed about what is engine, there's a newer page that I did not know was there.

**Carrie Chowske:** That's not it.

**Carrie Chowske:** That's the older one.

**Carrie Chowske:** Carrie, what are you doing?

**Carrie Chowske:** Now I've got the freaking, now I have the Zoom like toolbar in my way.

**Carrie Chowske:** It's this one.

**Carrie Chowske:** Um, that's newer.

**Carrie Chowske:** This is from just a few weeks ago.

**Carrie Chowske:** So I'm wondering if like, maybe we should just focus on this one and redirect that older page to this, like just put in a redirect for it or the other, or the other way around.

**Joel Murphy:** I don't know, whichever one's got more traffic, we should use as the main, use the canonical.

**Joel Murphy:** Yeah.

**Joel Murphy:** Let me take that away and take a look because I already knew just scrolling through it quickly.

**Carrie Chowske:** I just saw stuff that's outdated.

**Joel Murphy:** So, um, and also I really want to lean into this tonality analysis tool that we have.

**Joel Murphy:** It's not really practical.

**Joel Murphy:** I don't think for us to use it across all of our content, but I started with that, with the page that I made the recommendations on because I was thinking, okay, let me just match the tone and then I'll try to be more specific about, um, the actual, like how the product does this thing, whatever it is.

**Joel Murphy:** Right.

**Joel Murphy:** And then I realized as it was feeding me information, it was kind of already doing both.

**Joel Murphy:** It was kind of giving me like a tonality that matches how customers talk.

**Joel Murphy:** But also because it was doing that, was so specific.

**Joel Murphy:** Like here's an example.

**Joel Murphy:** Like it said something about I was using something yesterday on a page, our product page about reporting.

**Joel Murphy:** And specifically, you know, we use tag travel by job code.

**Joel Murphy:** Like we say that a lot.

**Joel Murphy:** But it referenced GL codes, general ledger codes, job codes, and then something else.

**Carrie Chowske:** And I was like, okay, that right there is huge.

**Joel Murphy:** Yeah, right. So it's saying the tonality should be this, but it's also being so specific about what these people call these things. I was like, okay, this is giving me both. So I've been really leaning on it heavily. So whatever post we go with, the one with my suggestions is the new one.

**Carrie Chowske:** That new one's going to go through the same process.

**Carrie Chowske:** So this spreadsheet that you gave me, is that the output that it gives you?

**Carrie Chowske:** Or is this just like you just kind of copied over from the tool that you're using or whatever?

**Joel Murphy:** So it is the output it gives me. It just doesn't format it this way. I formatted it in spreadsheet format, so if you guys wanted to feed that in, it would be able to semantically read this from left to right. But what I get back from the tool is that it can run in either Slack or Gemini, so it's just kind of like a wall of text.

**Carrie Chowske:** And I just figured it would be easier to feed it.

**Carrie Chowske:** What is it called that you're using?

**Joel Murphy:** Well, it's built on cargo.

**Joel Murphy:** So it takes, so we have all of our sales calls for a couple of years vectorized.

**Joel Murphy:** using and and

**Joel Murphy:** And as the data set, and so we can prompt it using Gemini or Slack channel, and it's prompted to say, like, analyze these calls for these personality types or personas, whatever, and match the input from the user prompt to match.

**Joel Murphy:** I think it's, like, voice of customer or something like that, and.

**Carrie Chowske:** Okay, a couple things we can do, because we can actually use this.

**Carrie Chowske:** This is great.

**Carrie Chowske:** I love that you sent this, because, so our input on Atlas, we give it a writing guidelines, right, and we tell it, you know, you can be as specific as, like, never use this word, use these words instead.

**Carrie Chowske:** You know, you can, you can tell it very specific, or you can be more broad, you know, like, one of the things that, that ours checks for is that it's, you know, speaking to somebody on a crew, not, not someone in an office, right?

**Carrie Chowske:** Like, we want to talk to people that are in the field working.

**Carrie Chowske:** Not people who are sitting behind a desk all day.

**Carrie Chowske:** Like we want to talk about those realities.

**Carrie Chowske:** So like I'm wondering if I'm going to try and see because what we do when we craft that document is we give it some content and we go write me up, you know, writing guidelines based on this feedback or this content.

**Carrie Chowske:** Like what would you say?

**Carrie Chowske:** And I'm wondering what's going to be the best way to do it.

**Carrie Chowske:** Like if you're, if you can, if you can, the way you're prompting yours, if you can prompt it to like, see if you want to give it our writing guidelines and say, hey, can you tweak this for the, you know, things that you've been updating lately?

**Carrie Chowske:** Like give it better guidelines so that we get, because, because that's what we're checking against.

**Carrie Chowske:** So if we're checking against the same thing that you are, we should be getting kind of similar things.

**Carrie Chowske:** So I don't know which is going to work better.

**Carrie Chowske:** If I feed you what you just gave me into ours to try to recreate a writing guidelines, or if you can prompt on your end, giving it our writing guidelines and say, can you put, can you rewrite these guidelines based on our recent interaction?

**Joel Murphy:** Let me see what gives us better results.

**Joel Murphy:** Let me ask Rory, who's on the marketing team, who built all this stuff.

**Joel Murphy:** I'm wondering if there's a way for you guys to just be able to prompt it yourselves or connect to it somehow or something like that rather than doing more of what I did here, which took a few minutes to do.

**Carrie Chowske:** Right.

**Carrie Chowske:** Yeah, it sounds very similar to kind of how we're using ours.

**Carrie Chowske:** And I think that the fact that you have all this valuable information feeding into it, I think is going to be a game changer for the content we're creating.

**Carrie Chowske:** If we can get the right, you know, we can give our LLM, you know, the right tool like this.

**Carrie Chowske:** You know, we can get it from one LLM to the other.

**Carrie Chowske:** We can go, hey, this is great.

**Carrie Chowske:** So, yeah, that would be awesome.

**Joel Murphy:** Cool.

**Joel Murphy:** Yeah, let me add...

**Joel Murphy:** Hopefully it's something, in the meantime, like, you know, I don't mind.

**Carrie Chowske:** Yeah, this, this five articles worth of this, you know, or five, I don't know if it's all, it's all from the same one, but I mean, five little, this might even be enough for it to go, oh, let me change these things.

**Carrie Chowske:** We might start getting closer just, just from this one document.

**Joel Murphy:** So, yeah, so this was four, this is five, like, content blocks down a product page.

**Joel Murphy:** So I separated them just because it was too difficult to, like, put them in one sheet, but yeah, there's some good stuff in there.

**Joel Murphy:** And what I thought would help the LLM is that it does kind of make, like, here's, it gives you notes about, like, why.

**Joel Murphy:** It gives you the original kind of, like, some of the original line-by-line copy and says, you know, here's how I would change that.

**Joel Murphy:** And then it gives you the full-on copy, right?

**Joel Murphy:** So, like, it really is, like, good training to say, like, here's.

**Joel Murphy:** Here's what the original was, here's why I would change it based on the data, here's a couple of line-by-line examples, and then here's the full thing.

**Carrie Chowske:** Yeah, let me show you, what, where are you, actually, let me just pull it up in Atlas, it'll be easier.

**Carrie Chowske:** So on our end, like, I always go to the wrong place when I'm looking for the artifacts.

**Carrie Chowske:** So we have all our personas separated out, too, so, like, if we ever need to do anything specific, we do that, too, but the writing guidelines is, you know, like, we will put in here, like, here's a good example, here's a bad example, so we can literally take those sentences that it rewrote and put them side-by-side and go, this is bad, this is good, and that helps the most, honestly, in terms of telling the LLM what to do.

**Carrie Chowske:** Like, you can see here, we have these good examples, and we have these bad examples, and they're full paragraphs, so, yeah, we can, you know, even just replacing those examples will go a longer way.

**Carrie Chowske:** So it sounds like it's giving very similar output. This is how we guide our model: okay, now take the article you wrote and rewrite it based on these guidelines. It does that as part of its writing process. But I think it actually skips that step now and writes it based on the guidelines directly, so it doesn't have to do a check after the fact as it's writing.

**Joel Murphy:** Okay.

**Joel Murphy:** So I'll see if Rory can figure out how to either connect you guys directly so you guys can use it. I do have four or five more product pages to do in the same way. And I'm also going to run that newer post you just pointed out through there, so I'll have more stuff to give you guys.

**Carrie Chowske:** Cool. Yeah, send me whatever you've got and we'll work with it. That's honestly what will make the difference in terms of tone and everything. We get really good results the more specific we can be with the writing guidelines. We'll get really close, if not right on the money, to what you want it to be.

**Carrie Chowske:** Cool.

**Carrie Chowske:** Sounds good.

**Carrie Chowske:** Awesome.

**Carrie Chowske:** Awesome.

**Carrie Chowske:** Awesome.

**Carrie Chowske:** I think that was everything.

**Carrie Chowske:** Like I said, I'll get with Kyle and find out where he is with like the subreddit stuff and kind of working on the scrunch prompts there.

**Carrie Chowske:** But, you know, that's the, once we get that in there, we'll be able to see that, that, that data.

**Carrie Chowske:** And then I'll keep digging into on the corporate card stuff.

**Carrie Chowske:** I know we've got time on that.

**Carrie Chowske:** It's Q1 of next year.

**Carrie Chowske:** You guys are thinking of like actually having it public facing.

**Carrie Chowske:** So we've got some time, but it's kind of good to look at.

**Carrie Chowske:** Cause I, I like to think about that stuff so that we're not shooting ourselves in the foot now for later, you know, that by the time we get there, we're limping.

**Carrie Chowske:** Cause we forgot to staunch the leading, you know?

**Carrie Chowske:** So yeah, I want to keep us, keep the data on our end organized too, so that we can actually track what we want to track and see what, see those outcomes.

**Joel Murphy:** Cool. I think we got a lot out of that.

**Carrie Chowske:** Great conversation. All right, well, have a good weekend and we'll talk to you next week.

**Joel Murphy:** Thanks, Carrie.

**Carrie Chowske:** Thanks. Bye.

**Joel Murphy:** Bye.
