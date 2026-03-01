# Prophecy <> GrowthX - Weekly Sync

<metadata>
date: 2026-01-21
time: 18:00 UTC
duration: 18 minutes
organizer: vivek@growthxlabs.com
enriched_on: 2026-02-28 16:32 UTC
source: fathom
fathom_recording_id: 116051269
fathom_url: https://fathom.video/calls/538212923
share_url: https://fathom.video/share/vzQ4o9hQssQkHERUKv2yTwobK-bHGCxx

participants:
  - name: Vivek Shankar
    email: vivek@growthxlabs.com
    affiliation: GrowthX
    role: Account Manager (departing)
  - name: Carrie Chowske
    email: carrie@growthx.ai
    affiliation: GrowthX
    role: New Account Manager for Prophecy
  - name: Cody Carmen
    email: carmen.cody@prophecy.io
    affiliation: Prophecy
    role: Head of Marketing / Product Lead
  - name: Matt Turner
    email: matt@prophecy.io
    affiliation: Prophecy
  - name: Roderick Bishop
    email: roderick@prophecy.io
    affiliation: Prophecy
  - name: Raveena Kapatkar
    email: raveena@prophecy.io
    affiliation: Prophecy
  - name: Wilton Kuffel
    email: wilton@prophecy.io
    affiliation: Prophecy
  - name: Ehtisham Hussain
    email: ehtisham@growthx.ai
    affiliation: GrowthX
  - name: Saskia Wartnaby
    email: saskia@growthx.ai
    affiliation: GrowthX
  - name: Kyle Doherty
    email: c-kyle.doherty@growthx.ai
    affiliation: GrowthX
  - name: Kyle Gaudreau
    email: kyle@growthxlabs.com
    affiliation: GrowthX

</metadata>

---

## Summary

Vivek Shankar departing GrowthX introduces Carrie Chowske as Prophecy's new account manager. The team diagnosed three critical indexing failures preventing prophecy.ai from gaining organic visibility: Webflow's slow sitemap updates, unparseable schema errors blocking crawling, and unoptimized legacy content lacking SEO signals. GrowthX pivots strategy to prioritize rewriting old posts for SEO fit before creating new content, while transitioning AI visibility tracking from Scrunch to GrowthX's internal tool, CheckThat, which offers historical data and superior AEO tracking.

---

## Context

Prophecy is a data platform company building AI-native analytics solutions. This weekly sync marks a significant transition in account management while also diving into concrete technical and content challenges limiting organic discovery. The account is currently stuck with only 4 indexed pages on prophecy.ai, creating a major blocker for organic growth and AI visibility. The conversation surfaces a common post-launch challenge: initial content and technical setup may not prioritize SEO signals that search algorithms need to rank and index content effectively.

GrowthX's strategic shift toward content rewriting reflects a mature approach—recognizing that fixing foundations (indexing, on-page signals) must come before scaling new content creation. This positions both teams to work together systematically on three distinct problems: technical (schema, sitemap), content (SEO optimization), and tracking (CheckThat integration).

---

## Relevance

- **For Prophecy (Client):** Critical operational sync addressing the core blocker to organic growth—indexing failure—and introducing new account management structure. Directly impacts roadmap prioritization and content strategy.

- **For GrowthX (Services):** Demonstrates typical B2B SaaS content challenges and GrowthX's systematic diagnostic approach. Case study potential for post-launch optimization and AI visibility strategy.

- **For CheckThat (Internal Product):** Live use case of CheckThat deployment with a real client, validating its competitive advantages (historical data, evaluation-stage focus, AEO tracking) over incumbent tools like Scrunch.

- **For SEO & AEO Practice:** Shows the intersection of technical SEO, content optimization, and AI visibility—three pillars of modern B2B growth that must work in concert.

---

## Overview

- **Account Leadership Change:** Vivek Shankar is departing GrowthX; Carrie Chowske assumes account management for Prophecy effective immediately. Carrie brings agency and SaaS background to the relationship.

- **Indexing Crisis:** Prophecy.ai has only 4 indexed pages, with many others blocked or missing entirely. Three root causes diagnosed:
  1. Webflow's sitemap updates lag ~2 weeks, causing Google to miss new pages on the new domain with limited crawl budget.
  2. Webflow template generates unparseable structured data errors, visible in Google Search Console, blocking indexing on affected pages.
  3. Older published content lacks SEO optimization signals, reading as "thought leadership" rather than answerable search queries. Example: November post "You don't need a BI tool..." remains unindexed despite being live since publication.

- **Content Strategy Pivot:** GrowthX will pause new content production and prioritize rewriting existing posts to add SEO sections, target keywords, and maintain Prophecy's POV. Rewrites go to Cody for review before live updates.

- **AI Visibility Tool Transition:** Moving from Scrunch to CheckThat (GrowthX's internal tool). CheckThat advantages: hundreds of pre-existing prompts for immediate historical data, focus on evaluation-stage (high-intent) queries, and superior visibility into Google AI Overviews citations. Carrie will populate Prophecy's competitors in CheckThat and demo next week.

---

## Key Topics

### SEO Indexing Diagnosis

**Problem:** Only 4 pages on prophecy.ai indexed, blocking organic search visibility and traffic.

**Root Causes Identified:**

1. **Sitemap Submission Lag**
   - Webflow's XML sitemap updates every ~2 weeks, not real-time.
   - New domains have limited Google crawl budget; without frequent crawls, Google doesn't fetch the updated sitemap.
   - Result: New pages added to site aren't discovered for weeks, missing the crawl window.
   - Solution: Manually submit sitemap to Google Search Console to force immediate discovery.

2. **Webflow Schema Errors**
   - All affected pages show "unparseable structured data" errors in GSC.
   - Appears to be a template-level issue, not individual page errors.
   - GSC provides exact code location and error details for developer fix.
   - Must be fixed before pages can be indexed.

3. **Unoptimized Content**
   - Legacy posts optimized for thought leadership, not search algorithm signals.
   - Lack keywords, clear problem-solution structure, and SEO metadata.
   - Algorithm cannot match content to search intent or clusters without these signals.
   - Example: "You don't need a BI tool..." post from November remains unindexed despite being live for months.

**Validation:** Looker dashboards confirm minimal traffic and zero engaged sessions, validating that indexing is the primary blocker.

### Content Strategy Pivot

**Decision:** Halt new content creation; prioritize rewriting old posts for SEO fit.

**Rationale:**
- Unindexed content cannot drive traffic regardless of quality.
- Fixing indexing foundations first ensures all new and existing content can be discovered.
- New posts will be created at scale once rewrite foundation is in place.

**Rewrite Framework:**
- Add SEO sections with target keywords and problem-solution framing.
- Maintain "Prophecy's POV" section to preserve brand voice and differentiation.
- Structure: opening hook → problem statement → Prophecy's unique insight → solution/recommendations.
- Rewrites submitted to Cody for review before updating live pages.

**Timeline:** Rolling rewrites over next couple of weeks.

### AI Visibility Tracking

**Current State:** Prophecy has zero referral traffic from LLMs because sites must pass SEO signals first.

**Goal:** Once indexing is fixed, track two dimensions:
1. Organic referral traffic from LLM citations (once SEO enables it).
2. Citation frequency and placement in LLM responses and Google AI Overviews.

**Tool Transition: Scrunch → CheckThat**

**Why CheckThat:**
- **Historical Data:** Pre-loaded with hundreds of existing prompts; CheckThat can show historical citations immediately rather than requiring weeks of data accumulation.
- **Evaluation-Stage Focus:** Tracks high-intent prompts where users are actively evaluating solutions. This is where purchase intent concentrates and brand differentiation matters most.
- **AEO Tracking:** Better visibility into Google AI Overviews citations compared to Scrunch, which is increasingly important as more users interact with AI through Google Search.
- **Multi-Model Support:** Can view data by model, understanding which LLMs are citing Prophecy.

**Next Steps:** Carrie adds Prophecy's competitors to CheckThat; full demo for Cody next week.

---

## Action Items

**Cody Carmen (Prophecy)**
- Fix schema errors in Webflow template using GSC error details; validate all affected pages resolve in GSC
- Confirm XML sitemap is updated with dev; manually resubmit sitemap URL in Google Search Console to force indexing
- Review GrowthX content rewrites in Airtable and provide feedback on SEO fit and brand voice alignment

**Carrie Chowske (GrowthX)**
- Add Prophecy's competitors to CheckThat instance
- Prepare and deliver CheckThat demo to Cody next week, showing historical data, competitor tracking, and AEO insights

**Vivek Shankar (GrowthX)**
- (Transitioning out; knowledge transfer to Carrie)

---

## Transcript

**Cody Carmen (Prophecy):** Hey, team.

**Cody Carmen:** No worries.

**Cody Carmen:** Hey, Vivek.

**Vivek Shankar (GrowthX):** How are you?

**Cody Carmen:** How are you, Cody?

**Cody Carmen:** Good.

**Cody Carmen:** I'm doing well.

**Cody Carmen:** Can't complain.

**Vivek Shankar:** Well, I'll get right into it.

**Vivek Shankar:** I wanted to introduce Carrie.

**Vivek Shankar:** So as my note mentioned, I will be leaving GrowthX until this month.

**Vivek Shankar:** So Carrie will be taking over Prophecy.

**Vivek Shankar:** And yeah, I'm going to toss it over to Carrie for a quick intro.

**Cody Carmen:** Cool.

**Carrie Chowske (GrowthX):** Hello, Cody.

**Carrie Chowske:** I have a brother named Cody.

**Cody Carmen:** Nice.

**Carrie Chowske:** Good name.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** Good Good Good name.

**Carrie Chowske:** Good name.

**Carrie Chowske:** Good name.

**Carrie Chowske:** Yeah.

**Carrie Chowske:** So I'm really excited to be taking on the Prophecy account.

**Carrie Chowske:** I come from an agency background and have a lot of experience in SaaS products and different platforms.

**Carrie Chowske:** I'm here and ready to hopefully fill Vivek's shoes and deliver what you expect.

**Cody Carmen:** So.

**Cody Carmen:** Awesome.

**Cody Carmen:** Yeah.

**Carrie Chowske:** I'm looking forward to working together.

**Carrie Chowske:** Thanks.

**Carrie Chowske:** Me too.

**Vivek Shankar:** All right.

**Vivek Shankar:** Let me share this screen.

**Vivek Shankar:** All right.

**Vivek Shankar:** So, you know, obviously the big news coming into this week is that we're having some indexing issues.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** So three main reasons that we basically just diagnosed.

**Vivek Shankar:** All right.

**Cody Carmen:** One is some of the URLs seem to be missing in your sitemap.

**Cody Carmen:** Yeah, I asked Yee, our contractor, on this, and he said that he could find them in the sitemap, and that he thought those were in there.

**Cody Carmen:** I did not double-check his work on that.

**Cody Carmen:** Okay.

**Cody Carmen:** And anyway, they should be auto-getting added to the sitemap based on our Webflow settings.

**Cody Carmen:** Okay.

**Cody Carmen:** Um, well, I think that if there was any lag on that, it is taken care of, but do you know when the sitemap gets pushed to Google?

**Cody Carmen:** I don't know, but I see on our XML sitemap, I see it.

**Vivek Shankar:** Um, okay.

**Vivek Shankar:** So maybe sometimes what happens is Webflow sends it once every two weeks or something.

**Vivek Shankar:** So even if your sitemap is updated, Google necessarily doesn't have that copy of the sitemap because it hasn't crawled your site.

**Vivek Shankar:** And I think with prophecy.ai, we are having crawl budget issues.

**Vivek Shankar:** It's not an issue as much as the fact that Google just isn't crawling the website as often as we'd like because it's still a new website and so on.

**Vivek Shankar:** So that's why the Google version of the sitemap is not quite matching the XML.

**Vivek Shankar:** Well, what I would ask them to do is maybe manually submit the sitemap onto Google Search Console.

**Vivek Shankar:** That's going to be an easy fix.

**Vivek Shankar:** And then these pages over here, some of them are indexed, some of them are not, but all of them have a schema error.

**Cody Carmen:** Yeah, and he asked what you guys mean by schema error.

**Vivek Shankar:** Yeah, I can, yeah, let me just, an example.

**Vivek Shankar:** So all of this is in Search Console, and I'll just show you an example, but basically, if you just copy-paste any of these URLs in here, so let me take this one, and then, oh.

**Vivek Shankar:** So this is basically what it says.

**Vivek Shankar:** You know, URL is on.

**Cody Carmen:** Google, but it has some issues.

**Vivek Shankar:** And then if you basically go to this unparseable structured data over here, click on it, and then click on this, it just shows you the exact location of the error.

**Cody Carmen:** So I think this is more of a web dev thing.

**Vivek Shankar:** My guess is this looks like a Webflow template issue.

**Vivek Shankar:** It's just something that maybe needs to be fixed in the template.

**Vivek Shankar:** Yeah, okay.

**Cody Carmen:** I'll chase that one down.

**Cody Carmen:** So, yep, that makes sense.

**Cody Carmen:** I'm not surprised that we're running into more technical web dev issues based on how we have done this.

**Cody Carmen:** So I will keep chasing these down as they pop up.

**Cody Carmen:** So I, as always, appreciate the GrowthX team's help on finding these because they're hiding all over the place.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Um, and then the other issue, of course.

**Vivek Shankar:** I think we may have flagged this initially, but some of our content is not getting indexed because it's a bit too thought leadership-like, which is, of course, not a bad thing.

**Vivek Shankar:** But the problem is that the algorithm doesn't associate a particular search or a search cluster with the topic if we don't give it enough signals.

**Vivek Shankar:** So the issue is just that, you know, the one example, of course, is I think the first one that we published, which is, you don't need a BI tool, you need something else.

**Vivek Shankar:** I forget the exact title.

**Vivek Shankar:** Like that hasn't been indexed despite being published in November.

**Vivek Shankar:** The reason is because it's not really optimized for the algorithm.

**Vivek Shankar:** So a lot of our content from back then has this issue, and we didn't see it, mainly because we didn't have the GSC access or the GFO access.

**Vivek Shankar:** We only received it in January.

**Vivek Shankar:** So that's why we couldn't pick it up before this.

**Vivek Shankar:** But looking at it now, we have a plan in terms of rewriting that content.

**Vivek Shankar:** We just need to make it a better SEO fit.

**Vivek Shankar:** We've identified which keywords need to go with them, and we have a good structure in place.

**Vivek Shankar:** So we're going to start churning that out over the next couple of weeks just to make sure that, you know, these things get indexed, et cetera.

**Vivek Shankar:** What the hell?

**Vivek Shankar:** Did I lose everybody?

**Carrie Chowske:** I'm still here.

**Carrie Chowske:** I'm still here.

**Vivek Shankar:** Oh, okay.

**Vivek Shankar:** My screen just closed all of a sudden.

**Vivek Shankar:** I was like, okay.

**Carrie Chowske:** Cody just said what the hell, and then was gone.

**Carrie Chowske:** So maybe he had something happen.

**Vivek Shankar:** I think I said what the hell, so.

**Vivek Shankar:** Oh.

**Carrie Chowske:** It sounded like him.

**Vivek Shankar:** I just looked at my little second screen, and everybody was frozen.

**Vivek Shankar:** Nobody was moving, so I was like, I guess we'll wait for them to return.

**Vivek Shankar:** You're still there, right?

**Carrie Chowske:** Me?

**Carrie Chowske:** Yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay, cool.

**Vivek Shankar:** Yeah, you're there.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Yeah, because I think it minimizes it, and everybody looks like they're frozen on screen for some reason.

**Carrie Chowske:** I was holding very still while I typed a note to Stevie.

**Carrie Chowske:** We got all the EMs are asking for like, and I just noticed this with the client we were just talking about, but anyway, I was trying to add their competitors, and they don't have profiles.

**Carrie Chowske:** So I was like, is there any reason I can't auto, because I think they auto-generate once you initiate it.

**Carrie Chowske:** Is there any reason I...

**Vivek Shankar:** Do we want to talk about CheckThat over here, or?

**Carrie Chowske:** I can just give the brief overview like I did, because I want to make sure that they have some data in their space before I show it to them.

**Carrie Chowske:** And the problem I was having is if their competitors aren't already in there, I can't.

**Carrie Chowske:** There's nothing to show, so I just want to make sure that I have that in there, but I can show it next week for sure.

**Vivek Shankar:** Okay, so I'll just preview it like I did if you want.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Hey, Cody, sorry about that.

**Vivek Shankar:** Internet dropped.

**Cody Carmen:** Yeah, no worries.

**Cody Carmen:** I thought it was my internet, and I was like, what the hell?

**Vivek Shankar:** Gary was like, why are you cursing?

**Cody Carmen:** Yeah.

**Cody Carmen:** No worries.

**Vivek Shankar:** So, yeah.

**Cody Carmen:** Some of the older content, yeah, is just not cutting it.

**Vivek Shankar:** Yeah, it's too the quality is good.

**Vivek Shankar:** It's just that it's not SEO optimized.

**Vivek Shankar:** So the structure we're thinking of is just like, as I discussed with you, like, just have the regular SEO sections, one section of Prophecy's POV, and then, you know, move on to that.

**Vivek Shankar:** So, yeah, that's the priority over the next couple of weeks.

**Cody Carmen:** Okay.

**Cody Carmen:** Yeah, that makes sense to me.

**Cody Carmen:** So, you're thinking right now priority is rewrite and basically resubmit for a review for me, and then we update the published content?

**Vivek Shankar:** Pretty much, yes.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So, we'll probably scale down on the new content just a bit because, you know, that's the priority.

**Cody Carmen:** We're not going to completely eliminate it, but we can always catch up down the road.

**Vivek Shankar:** But I think for now, we need to prioritize rewrites.

**Cody Carmen:** Okay.

**Cody Carmen:** Yeah.

**Cody Carmen:** That makes sense to me.

**Vivek Shankar:** Yeah, I'm good with that.

**Vivek Shankar:** Just wanted to drop some screenshots of our Looker dashboard.

**Vivek Shankar:** I mean, this looks pretty sad, but, you know, just wanted to show you that we are tracking things.

**Vivek Shankar:** You know, as you can see, like, these four pages are all that we've had indexed.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** And this...

**Vivek Shankar:** This traffic actually is including organic as well as sources where the traffic medium is not set.

**Vivek Shankar:** So basically Google just hasn't found any sort of, what do you call it, medium from it.

**Vivek Shankar:** Like it's not been able to say is this paid traffic, this organic traffic, et cetera.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So yeah, generally we haven't been getting too many sessions over here.

**Vivek Shankar:** We haven't had engaged sessions either.

**Vivek Shankar:** So this clearly points.

**Cody Carmen:** This is the fact that, you know, we do need to rewrite the older content.

**Cody Carmen:** Okay.

**Cody Carmen:** And then are we prepared to take a look at here?

**Cody Carmen:** Anything that's basically referral traffic from the LLMs?

**Cody Carmen:** You know, obviously the questions I'm going to be getting here are more AEO, GEO oriented than SEO.

**Cody Carmen:** And I know that SEO optimization is obviously going to give us a better shot there as well, but yeah.

**Vivek Shankar:** Yes.

**Vivek Shankar:** So there's two parts to the LLM visibility picture.

**Cody Carmen:** One is of course SEO.

**Cody Carmen:** you.

**Cody Carmen:** Referral traffic that we get from LLMs.

**Vivek Shankar:** As of now, we haven't had any because the LLMs, as you said, they are following SEO signals.

**Vivek Shankar:** We haven't seen any referral traffic.

**Vivek Shankar:** The other part of it, of course, is tracking how often Prophecy shows up in LLM responses.

**Vivek Shankar:** So right now we're using a tool called Scrunch and we do have the prompts set up over there.

**Vivek Shankar:** But the reason I haven't included that here is because we are transitioning to an internal tool called CheckThat, which actually Carrie has been working on quite extensively.

**Vivek Shankar:** So, yeah, Carrie, do you want to talk about that?

**Carrie Chowske:** Just give us a little preview and so on.

**Carrie Chowske:** Yeah, I'll give you like a full demo on it hopefully next week.

**Carrie Chowske:** We're still populating out some of the stuff, but it looks and functions a lot like some of the other AI visibility tools.

**Carrie Chowske:** The big difference is going to be, one, you get data, like historic data.

**Carrie Chowske:** And so is really beneficial, like some of these other platforms, you have to kind of tell it your prompts, and then it takes and it just starts getting the data, then ours already has some, we have hundreds of existing prompts, and we're and we're focused a lot on evaluation stage.

**Carrie Chowske:** So people that have a higher intent, they're looking for solutions, they're looking for essentially your brand, right, they're looking to make a decision.

**Carrie Chowske:** And so you'll have some already in your account based on like your category, the way we've categorized different brands, but they'll also be some if we did we already have ones in there, Vivek for in, in Scrunch for Prophecy.

**Carrie Chowske:** Okay, so those will be ported over automatically.

**Carrie Chowske:** So we'll have some some of that.

**Carrie Chowske:** So there'll be data.

**Carrie Chowske:** But one of the things that we're kind of doing a little bit manually at the moment is going in and adding competitors.

**Cody Carmen:** And I still need to do that for your account.

**Carrie Chowske:** But then I should be able to right away pretty much show you show you how it works.

**Cody Carmen:** But it's going to be really cool.

**Carrie Chowske:** And they've got some really great features planned.

**Carrie Chowske:** And at the beginning,

**Carrie Chowske:** It's going to be a little more similar to some of the other tracking tools, but apart from the variety of prompts and you can look at everything by different models.

**Carrie Chowske:** What I'm seeing right away is a lot more visibility into citations for Google's AI overviews on the search page, which I think is still how a lot of people are interacting with AI, to be honest, because they're used to Google, right?

**Carrie Chowske:** So they're seeing that, and we're seeing a lot of that, and even for brands that weren't previously seeing a lot of citations.

**Carrie Chowske:** And so that's good, too, that we're able to get that data.

**Carrie Chowske:** Gives you a lot more visibility.

**Carrie Chowske:** So hopefully I'll have that ready.

**Cody Carmen:** I should.

**Cody Carmen:** I don't see any reason why I won't have it for you.

**Cody Carmen:** Cool.

**Cody Carmen:** Awesome.

**Cody Carmen:** Sweet.

**Cody Carmen:** Yeah, definitely excited to see that.

**Cody Carmen:** And yeah, that is something for us.

**Cody Carmen:** I want to make sure that I've got kind of an understanding of the tooling you're using for this, just so we can kind of be satisfied with the on our end.

**Cody Carmen:** Sweet.

**Cody Carmen:** That makes sense.

**Cody Carmen:** Yeah.

**Cody Carmen:** So, you know, I'm going to go chase down whatever's going on with schema issues right now, and try to figure out, and also look into the, you know, the sitemap crawling issue.

**Cody Carmen:** If that's, is this something that I can just, I have Search Console access, can I just reload that sitemap URL into the, like, Search Console sitemaps thing, and just have it run again?

**Vivek Shankar:** Yeah, you can do that yourself.

**Vivek Shankar:** I would just check with the web dev to make sure that the XML page is updated.

**Vivek Shankar:** If it's updated, you can resubmit the sitemap yourself.

**Cody Carmen:** Okay, cool.

**Cody Carmen:** All right.

**Cody Carmen:** So I'll ask him about that as well.

**Cody Carmen:** And then, yeah, I'm sure there's a few things for me to go look at in Airtable as far as other content that's already ready to be reviewed.

**Cody Carmen:** But then I'll start keeping an eye out for, you know, the rewrites.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Sounds good.

**Vivek Shankar:** That's, that's all we had.

**Vivek Shankar:** And yeah, we'll catch up.

**Vivek Shankar:** Sweet.

**Vivek Shankar:** It's like.

**Cody Carmen:** Awesome.

**Cody Carmen:** Cool.

**Carrie Chowske:** Thanks, team.

**Vivek Shankar:** Nice meeting you.

**Vivek Shankar:** All right.

**Vivek Shankar:** Thanks.
