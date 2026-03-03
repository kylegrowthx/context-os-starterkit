# Product Deep Dive (Gene Moran)

<metadata>
date: 2025-09-08
time: 20:00 UTC
duration: 54 minutes
organizer: Erik O'Brien (GrowthX)
participants: Erik O'Brien (GrowthX), Gene Moran (Hyperexponential)
fathom_recording_id: 85757380
fathom_url: https://fathom.video/calls/401822619
share_url: https://fathom.video/share/6xycUVwRKoC4ZfiJw_hHpx71dxLZLshi
source: fathom
enriched_on: 2026-03-02 19:45 UTC
</metadata>

---

## Summary

Gene Moran from Hyperexponential conducted a detailed product walkthrough of HX Renew, the company's flagship pricing and rating platform for insurance carriers and MGAs, demonstrating its Python-based underwriting workflow with API integrations, real-time validations, and comprehensive audit history. The conversation also covered two emerging capabilities—submission triage (launching at HX Live for pre-pricing automation of PDF submissions) and portfolio intelligence (for post-pricing batch rating and portfolio-level scenario analysis)—addressing the core pain point that large carriers and smaller MGAs struggle to write all business due to capacity constraints and complex workflows that Excel cannot handle at scale.

---

## Context

Hyperexponential is an insurance technology company whose core product, HX Renew, is an eight-year-old pricing and rating platform that has primarily served UK Lloyd's market customers (large carriers like Stomp, Markel, Munich Re, AIG). Gene Moran is a Solutions Architect at Hyperexponential focused on integrations. Erik O'Brien is leading GrowthX's engagement with Hyperexponential to create market-focused content for both the company's legacy UK business and its expansion into the US market, targeting actuaries, underwriters, and chief information/digital officers. The meeting was set up through David (likely a mutual contact), and GrowthX is gathering product intelligence to understand Hyperexponential's positioning, customer personas, and pain points so they can generate audience-focused content artifacts—treating it as a sales demo walkthrough but specifically for content research rather than a direct sales pitch.

---

## Relevance

**To GrowthX Delivery:**
- Hyperexponential's positioning contrasts large carriers (who want best-in-class point solutions: policy admin, workbench, claims, pricing) vs. MGAs and smaller insurers (who want integrated solutions that replace multiple tools). GrowthX's content strategy should segment messaging accordingly.
- The core pain point—Excel raters lack integration, scalability, and auditability for complex risks—is the primary competitive narrative against the status quo, not feature-to-feature competition with point solutions.
- Submission triage uses AI to extract and map ACORD form data to pricing models, replacing manual re-keying; this is a live capability launching at HX Live (a US summit in September 2025).
- HX Renew's Python-based backend (rating.py deterministic algorithm, async tasks, custom React components) is only accessible to actuaries/model developers, not underwriters; positioning should make this distinction clear.

**To CheckThat:**
- Hyperexponential's "Actuarial Agent" (beta) is an AI assistant within HX Renew that helps actuaries build models using natural language prompts. This is a direct application of frontier LLM capability for domain-specific tasks—relevant to CheckThat's AI visibility research and how AI is being embedded in vertical software.
- Portfolio intelligence uses batch rating, granular metrics segmentation (by LOB, geography, underwriter), and scenario/impact analysis. Understanding how their AI/data stack enables this could inform CheckThat research on AI-driven BI tools.

**To GrowthX Business Development:**
- Hyperexponential has a multi-tier sales motion: Solutions Architects (like Gene, focused on integrations), Solutions Engineers (ex-actuaries doing day-to-day demos), and a broader field engineering team. Utsav and Pernob on Gene's team are noted as world-class presenters. GrowthX should reference specific team members for follow-up deep dives.
- Customer segments: Lloyd's market (UK behemoths), US large carriers, and fast-growing MGA segment. MGAs are described as "really getting popular right now" in the US market—this is a high-growth TAM that Hyperexponential is actively pursuing.
- Gene flagged that portfolio intelligence and submission triage are "nebulous roadmap items evolving a little bit," indicating potential fluidity in product positioning. GrowthX should track updates before finalizing content.

---

## Overview

- HX Renew is a best-in-class pricing and rating platform for complex insurance, used by actuaries and underwriters
- New capabilities in development include submission triage (for pre-pricing workflow) and portfolio intelligence (for post-pricing analysis)
- Platform offers significant advantages over Excel-based workflows, particularly for complex risks and scalability
- Target customers range from large carriers to smaller MGAs, with varying needs for integrated vs. point solutions

---

## Key Topics

### HX Renew Overview

  - Core pricing and rating platform for insurance carriers and MGAs
  - Replaces Excel-based workflows with a more robust, integrated system
  - Key features:
      - API integrations with policy admin systems and third-party data sources
      - Customizable workflow with Python-based backend for actuaries
      - Real-time pricing updates and validations
      - Auditability through comprehensive change history
      - Portfolio analysis capabilities at point of pricing

### Submission Triage and Ingestion

  - Pre-pricing capability to manage high volumes of submissions
  - Uses AI to extract and map data from PDFs (e.g., ACORD forms) to pricing models
  - Allows for automatic rejection, flagging for review, or acceptance of submissions
  - Particularly valuable for MGAs and smaller insurers seeking integrated solutions

### Portfolio Intelligence

  - Post-pricing analysis tool for viewing and steering business at a portfolio level
  - Key capabilities:
      - Batch rating for rapid portfolio-wide updates (e.g., in response to new cyber threats)
      - Granular metrics segmentation by various factors (LOB, geography, underwriter)
      - Scenario and impact analysis for portfolio changes
  - Competes with dedicated BI tools, especially attractive for smaller insurers

### Actuarial Development Environment

  - Integrated Python-based environment for actuaries to build and maintain pricing models
  - Features version control and collaborative tools
  - Includes "Actuarial Agent" (beta) - an AI assistant to help build models using natural language prompts

---

## Action Items

- **Erik O'Brien (GrowthX):** Use product intelligence from this call to update GrowthX content artifacts for Hyperexponential, focusing on audience-specific messaging for actuaries, underwriters, and CDOs in the US market.
- **Erik O'Brien (GrowthX):** Request follow-up deep dive with Hyperexponential Solutions Engineers (Utsav and Pernob noted as "world class") if more detailed product information or sales-focused walkthrough is needed for content development.
- **Gene Moran (Hyperexponential):** Available to assist with follow-up questions about system integrations and can facilitate introductions to Solutions Engineers or broader field engineering team as needed.

---

## Transcript
**Erik O'Brien:** How's your Monday starting?

**Erik O'Brien:** Yeah, pretty good.

**Gene:** A fast start to the week.

**Gene:** A lot of things cooking right now.

**Gene:** I'm in the same boat.

**Erik O'Brien:** Yeah.

**Gene:** We have a lot of counterparts in London, like a lot of people I work with.

**Gene:** So day starts at, you know, as soon as you wake up, pretty much the team's messages are flying in.

**Gene:** Oh, yeah.

**Erik O'Brien:** I've got a little bit of that.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Some of the people that are working with me on hyperexponential are in India, one's in Africa, one's in Bosnia.

**Erik O'Brien:** So it's just like somebody's working all around the clock.

**Erik O'Brien:** So at some point I just drop my notifications.

**Gene:** Yeah.

**Gene:** Yeah.

**Gene:** You get the every time zone covered there pretty much.

**Gene:** A blessing and a curse.

**Erik O'Brien:** Absolutely.

**Erik O'Brien:** But thanks for taking the time today.

**Erik O'Brien:** I'm not sure how much or how little context David provided prior to my outreach.

**Gene:** Yeah.

**Gene:** Happy to.

**Gene:** I spoke with David.

**Gene:** Big kind of in passing, you mentioned a little bit of the context around this, and yeah, happy to dive into it.

**Gene:** I have a bit of an idea, but any additional context you can provide I think would be helpful.

**Erik O'Brien:** Yeah, so you can kind of treat this as like a customer demo or sales kind of product walkthrough, but for us, it's really just kind of understanding core features, functionality, and like for each one of the products, like who are the main buyers, personas that it addresses.

**Gene:** Yeah.

**Erik O'Brien:** But yeah, overall, you can kind of just treat it like a, you know, if it was a sales demo or product demo.

**Erik O'Brien:** Got it.

**Gene:** Okay.

**Gene:** Yeah.

**Gene:** Anything else before we go into it?

**Gene:** I don't think so.

**Erik O'Brien:** Unless you got any questions I can answer.

**Gene:** Maybe one question.

**Gene:** Maybe this is.

**Gene:** That's something I have to straighten out with David.

**Gene:** So something you were asking was about our portfolio intelligence capabilities that are coming out as well as submission triage.

**Gene:** I'm just wondering what the end product of this looks like because those two products in particular are a bit like nebulous roadmap type items that are evolving a little bit.

**Gene:** But like portfolio intelligence, probably more so.

**Gene:** We're really like launching submission triage next week or the week after next at a big like U.S.

**Gene:** summit we're having called HX Live.

**Gene:** We're really like unveiling it there.

**Gene:** But those two in particular are kind of like in their infancy as far as like products that we're coming out with.

**Gene:** Yeah.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So I'd say a little context on GrowthX.

**Erik O'Brien:** So we're going to be helping.

**Erik O'Brien:** I think both in the U.S.

**Erik O'Brien:** kind of break into the market, but also for like your legacy kind of U.K.

**Erik O'Brien:** business, more so putting out content that's relevant to the audiences in which you guys serve.

**Erik O'Brien:** So a lot of actuarial audiences underwriting chief information or chief digital officers here in the U.S.

**Erik O'Brien:** And so the content that we generate is going to be based off like what are their needs, pain points, how are they kind of thinking about products like yours?

**Erik O'Brien:** And so for us to get just the context around these products helps us just to kind of identify, you know, what are the pain points that they, you this product or product suite is trying to solve for them.

**Erik O'Brien:** So even if it's, you know, nebulous or kind of a roadmap item, there's probably still some insights that you have on like, why are we building this product?

**Erik O'Brien:** What's, what's it solving?

**Erik O'Brien:** How are we going to push it to the market?

**Erik O'Brien:** Yeah.

**Gene:** And so, yeah, a lot of, a lot of the content we will generate is.

**Erik O'Brien:** Very audience focused.

**Erik O'Brien:** so I'm going to dig into like the product was built for X reason for X audience.

**Gene:** Yeah, that makes sense.

**Gene:** I think then probably for this session, makes sense to speak to those two items, portfolio analysis and submission triage and our thoughts around that and why that's coming out.

**Gene:** And then for the core platform of HX Renew, which really focuses on the pricing and rating, that I can dive into a little bit deeper, show some of the product here, give our normal, usual top track around that.

**Gene:** Okay.

**Erik O'Brien:** Yeah, sounds great.

**Gene:** Okay.

**Gene:** I can open up my screen then.

**Gene:** Kind of go through a typical HX Renew top track here.

**Gene:** This is going to give me an issue.

**Gene:** Shoot.

**Gene:** Google me.

**Gene:** I the screen sharing permissions.

**Erik O'Brien:** Oh, yeah.

**Erik O'Brien:** You might have to grant permission and then leave and join again.

**Gene:** Yeah.

**Gene:** Looks like I might need administer permissions as well.

**Gene:** I don't typically use Google Meet.

**Gene:** Would Zoom be better?

**Gene:** Let me see.

**Gene:** Do I have the desktop version of that?

**Gene:** Maybe a question to the outputs here.

**Gene:** The way David described them is like it takes the transcripts.

**Gene:** Growthx would take the transcripts and then like put those into, like use those as the input.

**Gene:** Essentially, is the screen share component of it like something that's an input as well?

**Erik O'Brien:** No, I think that's just for human understanding.

**Erik O'Brien:** So we won't see the video into it.

**Erik O'Brien:** We just take the transcript.

**Erik O'Brien:** Yeah.

**Gene:** Let just see here.

**Gene:** Let's see if that works.

**Gene:** Are you seeing that now?

**Gene:** Yep.

**Erik O'Brien:** Oh, cool.

**Gene:** All right.

**Gene:** Wonderful.

**Gene:** Okay.

**Gene:** That's good, then.

**Gene:** I'll back up and figure it out.

**Gene:** All right.

**Gene:** So I'll walk through this.

**Gene:** This is a typical demonstration that we gave.

**Gene:** It doesn't have a lot of tailoring around it, but what, yeah, a typical process of demoing HX Renew.

**Gene:** So HX Renew, essentially what it is, is the pricing and rating platform, both for underwriters and actuaries.

**Gene:** Now, as a part of the entire underwriting workflow, there's a number of steps that happened prior to this, usually in an upstream system, like a policy administrator.

**Gene:** Now, what we usually see is people doing a process like this in an Excel rater that has all of these different inputs from third parties.

**Gene:** You need manual re-keying.

**Gene:** There's a lot of pain in the process of an underwriting.

**Gene:** The writer moving throughout their Excel rater to come up with a price that they eventually pass on that.

**Gene:** Within HR Renew, the actuary on their side uses Python to build out the entire process that you're seeing here that goes from the inputs and outputs, the different actual positioning of the different items you see on the screen here, and can put it into a paginated view where you step up.

**Gene:** Page by page through the underwriter workflow to come out with a price at the end that you'll eventually move back into one of the systems of records that you have as part of your architectural stack there.

**Gene:** So we'll start off this.

**Gene:** This is a professional indemnity line of business specifically.

**Gene:** And there's a number of different inputs we're going to use to ultimately come up with a premium that we'll move forward with.

**Gene:** So one of the big parts of HX Renew that makes it incredibly valuable for the underwriting workflow is the ability to connect with the other systems.

**Gene:** So in this first example here, we actually have a policy administration system that sits above this, a duck creek, a guide wire, something of that nature.

**Gene:** And we're actually going to pull all of the records there that we then we can use as reference material.

**Gene:** For everything to come after this.

**Gene:** So I'll choose an example here.

**Gene:** And we're just going to pull this data.

**Gene:** This is the kind of high-level data that we're then going to import to get a better view exactly of what's in there.

**Gene:** So we can see all of this information is in one place here without having the underwriter having to re-key any of that.

**Gene:** What we can do now is take this and then move it and use it again in each subsequent step that we have for the entire life of the workflow there.

**Gene:** Once we have a little bit of the policy details, we're going to do a few steps here.

**Gene:** Sanction screening, financial API, Moody's analytics, which essentially just brings in third-party data sources that we have.

**Gene:** And make sure that everything looks correct prior to actually moving forward with it.

**Gene:** And we're enriching the data that exists within there.

**Gene:** So this one might be actually that that talk track.

**Gene:** Yeah, we'll skip through that.

**Gene:** It's OK if I bounce around a little bit, right?

**Gene:** Yeah, yeah, absolutely.

**Gene:** OK, yeah.

**Gene:** OK, yeah, let's change this.

**Gene:** We're going to change the assured name to Apple Inc here.

**Gene:** Then this is going to change here in one of our fields that we can use here.

**Gene:** So this Apple Inc, this is the assured name.

**Gene:** You can actually see in this top right here, this is a calculated field, but we can manually override this.

**Gene:** If an underwriter wants to change this for whatever reason, usually you'll see that.

**Gene:** With different fields, actual.

**Gene:** So values that are calculated, sometimes there's a case where we might manually override them.

**Gene:** I'll show what that looks like a little bit later on.

**Gene:** But we have this information here.

**Gene:** Now I'm going to call to a third-party API, specifically a financial API that's going to look at all of the companies that match Apple.

**Gene:** And we're actually going to pull a stock ticker here.

**Gene:** And then now we're enriching this with two third-party data sources.

**Gene:** One is actually ChatGPT, where we can get information on this specific brand, Apple, some of the things it does at a high level.

**Gene:** This information can be useful for a number of different things.

**Gene:** And you can imagine having a prompt here where this can be tweaked essentially to have any type of information that you want coming in that's relevant to the pricing journey.

**Gene:** Along with it, we have a financial API in here where you can actually see the stock history and the ticker data.

**Gene:** Once again, fully customizable to whatever makes most sense for the information that the underwriter will want to get across here.

**Erik O'Brien:** Just to confirm, these steps, it's underwriters are the main user.

**Gene:** That's right.

**Gene:** So I can go into it a little bit after what it looks like for the actuary side, but essentially they are building everything that you see here.

**Gene:** We have a development environment that's embedded directly in the platform where the underwriter, the actuaries would use pure Python to build everything that you're seeing here.

**Gene:** Gotcha.

**Gene:** Yeah.

**Gene:** Okay.

**Gene:** Okay.

**Gene:** Okay.

**Gene:** Yeah.

**Gene:** Yeah.

**Gene:** You is I'm Thank

**Gene:** This is another example of a third-party integration that we see people use.

**Gene:** So we're actually looking at Moody's here.

**Gene:** That is actually, let me change the city and country here.

**Gene:** Once we change that information, it's going to pull the correct apple here.

**Gene:** And then we're going to get all of this data that we can enrich the price and journey with.

**Gene:** Should be the right one.

**Gene:** Yeah.

**Gene:** Let me move through this one.

**Gene:** But essentially this is, oh, here we go.

**Gene:** Okay.

**Gene:** So this is a connection with Moody's.

**Gene:** So all of this information would be, it's like stored in a place you can access.

**Gene:** Like if you have a Moody subscription here, we're making it easier, even less of a touch, where we can just put this on a single pane of glass in a dashboard here for someone to look at.

**Gene:** And now actually these inputs here, like operating revenue, that might be an input that goes into the algorithm that affects what the professional indemnity premium that eventually goes forward for this carrier.

**Gene:** So not only are we surfacing this information, but we can actually take this, use them as inputs further down as we're coming up with pricing and rating, so on and so forth.

**Gene:** A good amount of like back and forth, give and take too.

**Gene:** If you have any like questions as well, like I know I'm kind of just doing the monologue here just because, you know, just trying to get the information across.

**Gene:** But if you do have any questions, please let me know.

**Gene:** Yeah, we'll do.

**Gene:** Cool.

**Gene:** Okay.

**Gene:** Moving on a little bit through this then as well.

**Gene:** Yeah.

**Gene:** We'll go through this.

**Gene:** So this revenue number here, that's a good example of something we pulled from the financial API.

**Gene:** That number comes directly in here now.

**Gene:** And now we can kind of move through the actual work split details.

**Gene:** Now this is specific to this line of business of professional indemnity.

**Gene:** So we're going to fill out certain things here, like a percentage of the type of work that they do.

**Gene:** The validations are going to come in place here.

**Gene:** You know, so that term from red to green.

**Gene:** Now that this is validated, we can actually move things through a state where if we want to move this from a draft to a bind, those actual statuses can reflect real parts of the workflow.

**Gene:** So like sending it back to a policy administration system where it ultimately gets quoted and bind and moves forward there.

**Gene:** All of these validations that we put in place kind of protect the underwriter, the actuary, making sure that we have strong governance in place.

**Gene:** Just to make sure that nothing's slipping through the cracks here where some of the alternatives don't have the same type of validation to make sure that we're only moving forward with things that we are actually pricing and are real policy options.

**Gene:** So some of what that also looks like is the history here.

**Gene:** This is a good time to show this.

**Gene:** So every single step that I have shown so far actually shows up in a history pane here where this is auditable, searchable.

**Gene:** This is all API driven as well.

**Gene:** So we can call on this information too.

**Gene:** And that's a stark difference to some of the realities of what a lot of big carriers have who are not pricing on HX for new.

**Gene:** There's not a lot of information around the changes that are made as an underwriter is going through the pricing.

**Gene:** Now, this is helpful for the auditability, as I mentioned, but also for the ability to have a relationship between the underwriter and actuary.

**Gene:** If we can actually kind of look at a replay like this and see how the underwriter is actually using.

**Gene:** The pricing tool in Raider that has been put forth, it can actually add to the synchronicity of what changes we want to make.

**Gene:** How do we iterate on this?

**Gene:** How do we improve it?

**Gene:** That's a very big part of it as well.

**Gene:** A lot of times, we'll advise customers on putting out the rating tools quickly, getting feedback, iterating on that, and making it better continually.

**Gene:** And we have the technology guardrails in place, where we put them in a position that they feel very comfortable to do that fast generation without worrying if things will break or what will happen as far as a version history perspective.

**Gene:** So, we'll do a last part of this risk information, where we just look at the account assessment.

**Gene:** We can see we're going to give them a grade essentially on each of these items here.

**Gene:** And this is an area where the rating adjustment, given years in business, for example, is going to change the actual rating adjustment here.

**Gene:** But if we want to override this directly and, you know, for whatever reason, change the weights, we can do that.

**Gene:** It's going to ask us to provide a comment here.

**Gene:** And once we've done that, that's a satisfactory response.

**Gene:** And we're actually incorrect validation with the model.

**Gene:** So it's essentially saying that, yeah, you're in bounds here.

**Gene:** Even a comment, there's an area we can look at just to make sure that you're not incorrectly using the model.

**Gene:** And all of these tasks have been finished, when they're validated, it's saying the policy must be peer-reviewed before being bounced.

**Gene:** That's the last validation error.

**Gene:** Not so much an error, but before we can move on from this, that's what's in place there, just to put some guardrails around it there.

**Gene:** This is the actual pricing of the option itself.

**Gene:** From each of the previous steps, we have everything in here from the revenue to the base rate, all of the account assessment adjustments that we've made.

**Gene:** And with this, we have the base premium calculations that have been put out.

**Gene:** Out here, and now we can start putting options together for this.

**Gene:** So, I think that's a good limit.

**Gene:** So, I've put together one option here.

**Gene:** You can add additional rows if you'd like to have other options.

**Gene:** That's usually the relationship between carriers who are pricing here.

**Gene:** They'll often want to go to a broker with a number of different options and work backwards from there.

**Gene:** So, you can provide an area on here where you can do that price multiple options at once directly within this policy option, or you can actually...

**Gene:** So, you...

**Gene:** So that in another way within the platform where you have multiple options going outside of themselves and kind of like start this up again.

**Gene:** So there's a few different ways to do that.

**Gene:** But, you know, we have a team of model developers ultimately who can advise on all of that.

**Gene:** So we're happy with our options pricing, we can go forth and do a bit of portfolio analysis.

**Gene:** So this is a big portion, I would say, here of portfolio analysis at the point of pricing.

**Gene:** So we are going to look.

**Gene:** That's actually not right.

**Gene:** Thank you.

**Gene:** It's not right as well.

**Gene:** Let's get these numbers right.

**Gene:** So now we're looking at a portfolio analysis where we achieve the, we look at the loss ratios for this risk in particular and see how it stacks up against the rest of our book.

**Gene:** And underwriters can do this before they actually go ahead with the book, with the, with the pricing rather.

**Gene:** So we can see, you know, we want to compare it to all policies within.

**Gene:** In the United States, or specifically for accountants, we can look at the different things here.

**Gene:** And all of this is just like pure Python in the background, using a library where you can have these type of charts put in directly.

**Gene:** So that's helpful.

**Gene:** And this is a number of other analytics that we can look at where you can see, you know, what the strength of this risk looks like versus some of the other stuff in our book.

**Gene:** And all the charts here are useful in a number of different ways.

**Gene:** And as I mentioned, fully customizable here.

**Gene:** This is a last one real quick that we can look at.

**Gene:** So a lot of people have processes in place where they want to get something reviewed by a peer before they can move forward with it.

**Gene:** So this is actually an integration with a third.

**Gene:** Group party system like Teams, where this is going to go send a message off into a channel or an individual.

**Gene:** I actually have that.

**Gene:** I don't have to show it right now, but we'll get a message.

**Gene:** We can look at that, pull it up.

**Gene:** It's going to open up the UI of HX for New.

**Gene:** They can peer review it, market as peer reviews, and then it's good to go from there.

**Gene:** That would happen from somebody actually clicking an email option here as well.

**Gene:** Yeah, and then we can move on from there, quote it.

**Gene:** This is another ability to create a quote document here.

**Gene:** We actually get a file from this that we can look at that shows all the inputs that came in here.

**Gene:** Some people use that actually for an auditability standpoint, like we want to see the inputs in here.

**Gene:** In some cases, in some U.S.

**Gene:** admitted markets, they actually need something like that.

**Gene:** Some people use a workbench for that capability. Others can do it directly within here using the Python backend.

**Gene:** They have that full optionality as well.

**Gene:** Yeah, and that's essentially high level, quick, what the platform looks like.

**Gene:** An example, one underrated workflow for a professional indemnity model.

**Gene:** Gotcha.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So, for, can give me just like a two sentence, like, HX Renew is for actuaries and underwriters, the purpose of?

**Gene:** Yeah, best in class pricing and rating for insurance carriers and MGAs.

**Gene:** Yeah.

**Gene:** Right.

**Gene:** Okay.

**Gene:** Thank you.

**Gene:** Thank you.

**Gene:** Thank you.

**Gene:** Yeah, I just like to get those little snippets into the transcript.

**Gene:** Yeah, absolutely.

**Gene:** So we've seen HX Renew.

**Gene:** Yeah.

**Gene:** So all that right there is really the flagship product that is what was built eight years ago.

**Gene:** So it's really like, you know, what most people use us for.

**Gene:** Gotcha.

**Gene:** Yeah.

**Erik O'Brien:** And typically, I think you mentioned it during the early part of the demo.

**Gene:** Most teams that don't have a platform like HX Renew are doing this in Excel.

**Gene:** Yeah, that's the biggest, I'd say, competition that we face.

**Gene:** Usually it's people that have accelerators in place.

**Gene:** And they want to, we want to convince them to move off of that.

**Erik O'Brien:** Do you have like an estimate of like how much time they would save using your guys' products versus continuing to use it in Excel?

**Gene:** So, yeah, that one's a bit tricky because honestly, the initial investment, the time savings are not like, you don't see the time savings initially.

**Gene:** Initially, actually, there's a bit of investment to get up and running on this.

**Gene:** The benefit can come from the scalability that we offer.

**Gene:** So a lot of the problems people face in Excel is like if you have super complex risk, which that's actually probably also in the one liner, like where the pricing and rating platform specifically built for complex.

**Gene:** The more complicated the risk gets and the more complicated the model gets, those workflows don't really scale in Excel.

**Gene:** Excel isn't built for integrating the other data sources that you have in there.

**Gene:** And then if you want to get up quicker, you'll probably use Excel, but you're starting a new line of business from Fresh and you do it in Renew, you give yourself a lot of ability to capture that scale in the long run too.

**Gene:** Because a lot of problems these big carriers face is actually around, they can't actually write all the business that comes to them.

**Gene:** That's why they're using like MGAs and other sources.

**Gene:** There's just too much to write.

**Gene:** Half of what comes to them, they just have to get rid of because they don't have, there's not enough hours in the day to get through all of this.

**Gene:** So we give you the option to get through things quickly, safely, reliably, in a way where

**Gene:** You can put changes to pricing models that you can feel confident in actually putting together technical premiums for everything that's coming through.

**Gene:** That, yeah, you can just do it in a more reliable, scalable way.

**Gene:** Gotcha.

**Gene:** And then, yeah, if we can just talk through submission, ingestion, triage, and then whatever you have on portfolio intelligence.

**Erik O'Brien:** Yeah, have a tip.

**Gene:** So those two items are really outside of pricing and rating specifically.

**Gene:** So if you look at the insurance pricing workflow, portfolio analysis kind of happens at the end once everything's been priced and done there.

**Gene:** Submission triage is a pre-pricing capability at the front end.

**Gene:** And that kind of a little bit what I just spoke to earlier, like a lot of the big carriers face the problem of not being able to give their underwriters the correct things to even, first of all, they have a problem with the actual volume.

**Gene:** Like there's too much business out there.

**Gene:** So when underwriters ultimately do decide to work on pricing certain risks, we want to make sure that they have the best things in front of them to work on.

**Gene:** So we have, and this goes in tangent with the data ingestion agent, which is another capability that we have.

**Gene:** And this one's live, but this looks at submissions.

**Gene:** Usually these are like for property, it's like an accord submission, which is essentially just a giant PDF with a bunch of information in it about actual like properties.

**Gene:** And that gets submitted into our data ingestion agent, which uses.

**Gene:** AI to take out all the information that's within there and then can actually map that to what I just showed earlier, the actual data schema of the model that has been built before.

**Gene:** And with that, we can use that Python engine in the backend to calculate a lot of the different information that's in these submissions and we can extract, enrich it, and then prioritize those broker submissions to automatically reject certain things.

**Gene:** If we need to flag things for underwriter review, or we can, in some cases, automatically accept submissions, quote things, move it forward if a carrier wanted to prioritize speed in particular.

**Erik O'Brien:** Gotcha.

**Gene:** Yeah.

**Gene:** I'm taking notes to fill in some gaps with the transcript.

**Gene:** Yeah.

**Erik O'Brien:** Is it not catching everything?

**Erik O'Brien:** Well, it may, but I have like a personal note taker that.

**Gene:** Oh, cool.

**Gene:** Yeah, yeah.

**Gene:** To fill in the stuff.

**Gene:** Cool.

**Erik O'Brien:** So is that good for submission, ingestion, and triage?

**Gene:** I guess, is there a different audience outside of like who would be looking to?

**Gene:** Yeah.

**Gene:** So that's a good question.

**Gene:** It's interesting the way we've seen it evolve in the U.S.

**Gene:** So a lot of large carriers who are a lot of our current customers, that's Stompo, Markel, Munich Re.

**Gene:** AIG, all these giant carriers that we've captured first in the UK with our UK-based business.

**Gene:** These are all like behemoths who, from a tech stack perspective, want to go after the best in class for each point solution.

**Gene:** That means having the best policy administration, the best underwriting workbench, the best claim system, broker portal, and then pricing and rating as well.

**Gene:** So for them, because they, you know, have so much capital and revenue, like they can justify the cost of doing something like that.

**Gene:** And the Lloyd's market is the biggest market in insurance, essentially, which is the UK business.

**Gene:** So a lot of like, a lot of just insurance runs through that.

**Gene:** The US market actually has a lot, they have like large insurers too.

**Gene:** Of course, they have huge ones.

**Gene:** But for, like, ENS risk and, like, large, complex PNC, property and casualty insurance, we see a lot of, like, MGAs are popping up, which I forgot to ask, Erik, too, like, do you have, like, a big involvement with insurance in particular, or, like, knowledge?

**Gene:** You don't.

**Gene:** Yeah.

**Gene:** Okay.

**Gene:** So probably some of the stuff I'm saying here is, yeah.

**Erik O'Brien:** It's not to be dangerous, but, like, for these types of conversations, I like to act like I know nothing because it's better for the transcript anyway.

**Erik O'Brien:** A hundred percent, yeah.

**Gene:** So the MGAs are these managing general agents, which, taking on the capital risk, but can write the business on a carrier's paper on behalf of them.

**Gene:** And what that allows them to do is actually solve for them some of that.

**Gene:** It's issue where the carriers can't write enough.

**Gene:** They have the capital.

**Gene:** They just don't have the capacity to write everything.

**Gene:** So they'll hand some stuff off to these MGAs who can take it and be very specific on one thing, like Inland Marine in Mississippi or something.

**Gene:** If they're very good at that, they can take that and run with that.

**Gene:** So those MGAs we're speaking to a lot, and there's a ton of them in the U.S., and that model is actually really getting popular right now.

**Gene:** Those customers in particular are asking for their insurance software to do a lot more.

**Gene:** They want the pricing and rating.

**Gene:** They want that tied in with the source of truth in the policy administration system.

**Gene:** That's something they have to solve first, ultimately.

**Gene:** And then they may want a submission triage as well, where they have some pre-pricing here so they can actually decide what to work on.

**Gene:** If they're working with multiple carriers, they have a lot.

**Gene:** I mean, in, they want AI and automation to decide what are the best risks for them to even look at in the first place.

**Gene:** So we see the more down market we go, the more people are asking for out of their insurance technology solutions that they're buying.

**Erik O'Brien:** So the submission, ingestion, and triage, those guys, MGAs are kind of core audience for that specific or will be kind of audience for that specific product line.

**Gene:** Yeah, but I'd be careful.

**Gene:** I don't want to say it's not for the big boys either, like the people at the top.

**Gene:** It is for everybody, but I think we see the smaller you are, the more you're asking from us.

**Gene:** Not just pricing rating, but...

**Gene:** Portfolio analysis, you want us to be a source of truth, want us to be a data platform, you want us to be an underwriter workbench and pricing, where the larger companies are more comfortable with having just point solutions at each set.

**Gene:** Gotcha, that makes sense.

**Gene:** Yeah.

**Gene:** And that's unique to what we're hearing in the U.S.

**Gene:** too.

**Erik O'Brien:** All right, and then any talk tracks or specifics on portfolio analysis, any kind of differentiators that we need to know about there?

**Gene:** Yeah, so portfolio analysis is something we're hearing a lot in the U.S.

**Gene:** that people are pretty attuned to.

**Gene:** So I actually showed a little bit in the demonstration.

**Gene:** What we call the portfolio intelligence part of it, or portfolio analysis, kind of interchangeable there.

**Gene:** That's at the point of pricing, where in that example, you can pull information from a source of truth, get it into a portfolio analysis chart there, and look at everything before you bind a risk.

**Gene:** Portfolio intelligence, the capabilities we're coming out with, actually gives you the ability to view, analyze, steer your business, not just at the point of pricing, but at a higher level.

**Gene:** We can look at the whole portfolio at any given moment, really, not just as we're writing something.

**Gene:** So there's a few big parts of the capabilities within this.

**Gene:** Batch rating is something that you can do in the platform currently, but it's like, there's stuff coming out around this, where it...

**Gene:** So, yeah, there's a lot more coming for batch ratings in particular.

**Gene:** Let me just look at a few notes here.

**Erik O'Brien:** That's where David was mentioning, like, say there's a new cybersecurity threat.

**Erik O'Brien:** I can go into my portfolio and look at, like, what's the risk across everyone versus just having to go in each individual account.

**Gene:** Exactly, yeah.

**Gene:** So you can re-rate large groups of policies at one moment to see where you're essentially exposed.

**Gene:** Where's the, like, what would this look like with this new information?

**Gene:** Exactly.

**Gene:** And then, yeah, there's ways where you can look at granular portfolio metrics, like, and ultimately what you're trying to achieve as a business, so you can segment things out by line of business, where it's written.

**Gene:** What underwriters writing it, anything you have as an input, you can dig into that and see how your book looks, how different scenario analysis could affect it.

**Gene:** That's like an impact analysis or dislocation analysis.

**Gene:** I've heard it called as well.

**Gene:** That's when you can use like, what if scenarios simulate changes across the portfolio too.

**Gene:** That's kind of all tied together there, the batch rating, the dislocation analysis.

**Gene:** But it adds on like a whole nother layer outside of what we see in, in the actual just pricing and rating module, which forever, like that was the platform, like just that pricing and rating piece that I showed you.

**Gene:** It adds a whole new module where you can see a reporting layer with everything that's been written. It adds data management capabilities that replace a large swath of BI tools and other ways that people were already doing this in the past, but it directly puts it on the platform.

**Gene:** So this, I think, this capability in particular will be big, again, with those down market folks that are asking for more out of any tech spend that they have, where some of the bigger carriers, they're going to continue to use data platforms like Databricks, Snowflake, Palantir.

**Gene:** A lot of those large ones do have those in place and probably might do some portfolio analysis with us, but largely are going to aggregate everything into a data warehouse or a data lake and use that as a source of truth.

**Gene:** For all the reporting that goes on.

**Erik O'Brien:** So they can use it for, like you said, the big data providers and clouds for what's happening, but are they able to do kind of that batch rating?

**Gene:** Yeah, so, yeah, no, that's a good point.

**Gene:** They wouldn't, yeah, unless they like use our APIs within that platform, which is something they can do.

**Gene:** Everything you saw through that little demo and like anything that an underwriter can do on the platform can also be an API that's called in any other system.

**Gene:** So that's like a huge part of the architecture, but they wouldn't be able to do that without like some level of lift and involvement there.

**Gene:** So there is an advantage just to having that directly on the platform.

**Gene:** Awesome.

**Erik O'Brien:** Anything else we haven't chatted through yet?

**Gene:** I think that's a big part of it right there.

**Gene:** I hope the demo is all right.

**Gene:** I'm myself, I'm a solutions architect, so I'm not giving the demos like day in and day out.

**Gene:** have before, but it's, yeah, that's like a high level, quick and dirty one.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** I think we've got what we need.

**Erik O'Brien:** If it ever comes to light that we need more, I'll ask David.

**Erik O'Brien:** Yeah, I think we got to the key features and functionality.

**Erik O'Brien:** functionality.

**Erik O'Brien:** We've got got We've got got

**Erik O'Brien:** Let's through the three big ones that David wanted us to touch on.

**Gene:** Actually, there's one thing I'm remembering now that maybe we didn't discuss is the actual back end for the actuaries themselves.

**Gene:** Okay.

**Gene:** So everything I showed in the beginning, the underwriters as they go through the actual pricing journey of the inputs, calling the different information, all of that, that's all enabled and built here in the back ends by the actuaries or, you know, the model developers on a team.

**Gene:** And then we're going in, everything you see here is just like native Python.

**Gene:** If you make a change in here, it's going to show up in the actual model itself.

**Gene:** And then...

**Gene:** And there's like a secret sauce within here too and how all this works.

**Gene:** So like the rating.py, for example, I assume in here, this is like a deterministic algorithm that every single time there's a keystroke or a click in the platform or an underwriter makes a change, this rating.py file runs through.

**Gene:** So it means anytime you're doing anything in there, it constantly is updating, making sure that the price and everything in there is updating right away.

**Gene:** Where we also have like a tasks file in here where this is where like async tasks run.

**Gene:** So like a button I clicked for different things in there.

**Gene:** These happen anytime you want to take an action that would be done in a different file here for things to move forward in that way.

**Gene:** There's a few clever things within here.

**Gene:** It's not like a pure development environment or an IDE.

**Gene:** There's specific things in here that are unique to HX, where it's really the three components of the algorithms, the actual data schema itself, so the data that goes into it, and then we have the view as well, where we have custom React components, which is JavaScript here, but it's, like, only within the HX world of what goes in here, but this just is what the front end looks like, and that's just the other component to it.

**Gene:** Gotcha.

**Erik O'Brien:** So these, you said this is specific to actuaries?

**Gene:** Yes.

**Gene:** This is, yeah, this is only really the actuary side of the platform.

**Gene:** They'll come in, do this, underwriters will use the outputs.

**Gene:** Gotcha.

**Gene:** Yeah.

**Gene:** Yeah.

**Gene:** And having, like, an integrated development environment like this has a lot of advantages, too, where you can have version history, you have a lot of controls around it, you understand who is working on what.

**Gene:** But, and, like, the alternative to that is an Excel model where, sure, there might be, like, some version history, but it's, like, very spotty as opposed to, like, a development environment like this.

**Erik O'Brien:** Yes, I can imagine Excel, you know, auto-stating every five to ten minutes, and you get every five to ten minute version of it, but then you can't see exactly what changes are made.

**Gene:** Yeah, yeah, we've heard a lot of horror stories there, people trying to update these models that are probably, like, the biggest Excel files you've ever seen, just, like, beasts, and it's, like, trying to maintain version history with this.

**Gene:** Good luck.

**Erik O'Brien:** Sounds like something that I would be interested in.

**Gene:** Yeah.

**Erik O'Brien:** Cool.

**Erik O'Brien:** Anything else on this kind of integrated workspace?

**Gene:** This is something, too, which is something we're coming out with, the actuarial agent.

**Gene:** It's actually in beta stages now, so we do have some customers using this, actually.

**Gene:** But this is essentially a chatbot that is aware of the context of your model, and you can ask it to build something, and it's actually going to come in here and build out the Python directly in your file.

**Gene:** If you say, I want a professional indemnity model that has a financial API call in there to this specific website, Yahoo Finance, or something like that, it can then go in there and build all of that for you.

**Gene:** Now, this is a pretty cool capability.

**Gene:** We're pretty excited about it.

**Gene:** It's in beta now. It's not perfect right now, but it's something that can go a very long way for helping people get up on the platform pretty soon.

**Gene:** Like some of the pushback we hear sometimes is that certain people are a little bit scared of like the Python, for example.

**Gene:** Like we speak to teams who have actuaries that don't know Python, they'd have to learn it.

**Gene:** This is a way to get a shortcut for people who want to like build stuff quickly.

**Gene:** They can use AI directly in the platform that's aware of some of that specific syntax that's unique to HX that was mentioning earlier and get a head start and like spin things up like new lines of business very quickly.

**Gene:** And it's only going to get better as the frontier models get better and the capability just expands.

**Erik O'Brien:** It's pretty awesome.

**Erik O'Brien:** Thank you.

**Gene:** Thank

**Gene:** A cloud code for actuaries.

**Gene:** Exactly.

**Gene:** Yeah.

**Gene:** No, this is really cool.

**Gene:** I think that's pretty much everything now.

**Gene:** Awesome.

**Gene:** Yeah.

**Gene:** Well, Gene, appreciate the time and the walkthrough.

**Erik O'Brien:** We'll use all this to kind of update some of our artifacts that will generate some content for you guys.

**Erik O'Brien:** I guess I'll be in touch if David wants us to go another deeper route, but I think for his product deep dive past, this is good enough.

**Erik O'Brien:** Yeah.

**Gene:** Wonderful.

**Gene:** Happy to help, Erik.

**Gene:** Yeah.

**Gene:** Happy to help again, too, if we need anything.

**Gene:** We have a team of, as I mentioned, I'm a solutions architect.

**Gene:** We have a broader field engineering team.

**Gene:** My job is, like, mostly focusing on the integrations.

**Gene:** Yeah.

**Gene:** Customers look at with their other systems.

**Gene:** Our solutions engineers are really only focused on like HX Renew and the platform itself.

**Gene:** We have a lot of people that are like ex-actuaries that work within the platform and just like demo it all day.

**Gene:** So maybe if like you need like a second pass or something like that or a follow-up, I can put you in touch with some of those guys.

**Gene:** Utsav and Pernob on our team are, you know, world class at that.

**Gene:** Sweet.

**Gene:** Yeah.

**Gene:** I will keep you posted on that one.

**Gene:** But if we need to get another deep dive, more of like a sales call one, then we'll let you know.

**Gene:** Yeah, absolutely.

**Gene:** Awesome.

**Erik O'Brien:** Well, appreciate the time, Gene, and enjoy the rest of your Monday or hopefully not too much longer.

**Erik O'Brien:** Yeah, likewise.

**Erik O'Brien:** Thanks, Erik.

**Erik O'Brien:** Have a good one.

**Erik O'Brien:** You too.

**Erik O'Brien:** See you.

**Erik O'Brien:** Bye.
