# Weekly CheckThat Pipeline review

<metadata>
date: 2026-02-17
time: 17:31 UTC
duration: 39 minutes
organizer: Jesus Yepez (jesus@growthx.ai)
participants:
  - Bridget McGillivray (bridget@growthx.ai) - GrowthX
  - Jason Gong (jason@growthx.ai) - CheckThat Product Lead
  - Nigel Hammett (nigel@growthx.ai) - CheckThat Sales Lead
  - Jesus Yepez (jesus@growthx.ai) - CheckThat Ops/Setup
fathom_recording_id: 123042836
fathom_url: https://fathom.video/calls/569081080
share_url: https://fathom.video/share/PNyZCRt654fp3Rru7hcGtimR565EsmR7
source: fathom
enriched_on: 2026-02-27T00:00:00Z
</metadata>

---

## Summary

The CheckThat team standardized their demo process around a single, sharp competitor example to create urgency with prospects, and identified critical blockers in workspace setup and category mapping that require immediate attention. Lead generation remains bottlenecked by overly strict qualification filters and the absence of new competitor categories (e.g., Web Scraping, Wholesale Marketplace), which Jesus and Jason will address through process documentation.

---

## Context

This meeting represents a critical operational checkpoint for CheckThat as the product moves from ad hoc sales conversations toward a repeatable, scalable sales process. The team is balancing rapid customer acquisition against the infrastructure required to properly configure workspaces and demo environments for each prospect segment. Nigel, newly hired as sales lead, is building outbound momentum through LinkedIn while Jesus handles technical setup and Jason maintains product strategy alignment. The tension between speed and precision—particularly around category definition and lead qualification—is shaping near-term roadmap work.

---

## Relevance

- **Demo & Sales Strategy**: Refining how prospects experience CheckThat's core value proposition; focus on single competitor example vs. broad category overview directly impacts conversion likelihood.
- **Product Decisions**: Workspace model (single per client) and prompt-count gating (not per-workspace fees) have downstream implications for customer tiers, post-sale implementation, and pricing.
- **Operations**: New categories (Web Scraping, Wholesale Marketplace) and competitor mapping processes are blocking immediate demos; lack of playbook slows setup time.
- **Lead Generation**: 40 manual outreach attempts with minimal response suggests current cold-outreach approach underperforms vs. warm network connections; Sales Navigator + GrowthX asset leverage may improve efficiency.
- **Resource Planning**: Heavy dependency on Jesus (workspace setup), Jason (category playbooks), and Nigel (demos + outbound) suggests staffing constraints.

---

## Overview

- **Demo Strategy:** Focus on a single, sharp competitor example to create urgency and demonstrate immediate value, rather than a broad category overview.
- **Lead Nurturing:** Create a shared Slack channel with qualified prospects post-demo, using a value-add (e.g., slides) as the incentive to join.
- **Pipeline Blockers:** The current lead-gen workflow is too strict, filtering out qualified sign-ups. The product also lacks a process for defining new competitor categories (e.g., "Web Scraping"), which is critical for demo prep.
- **Outbound Plan:** Nigel will begin manual, targeted outreach using LinkedIn Sales Navigator, leveraging GrowthX resources (e.g., content, events) to secure demos.

---

## Key Topics

### Demo Strategy & Process

  - **Goal:** Create urgency by showing a prospect where a competitor is winning and they are not, providing a clear path to action.
  - **Process Guide:**
    1.  **Prep:** Jesus creates the workspace, ensuring correct categories and competitors are loaded.
    2.  **Prompts:** Jesus generates custom prompts using Cursor (a self-serve site is in development).
    3.  **Demo:** Nigel drives, focusing on the single, sharp competitor example.
    4.  **Post-Demo:** For qualified leads, create a shared Slack channel.
          - **Incentive:** Offer a value-add (e.g., slides) in the channel to drive adoption.
          - **Rationale:** Slack enables unencumbered follow-up, unlike email.
  - **Workspace Model:**
      - **Decision:** Use a single workspace per client to centralize data and reduce post-sale setup.
      - **Pricing:** Gate on total prompt count shared across workspaces, not per-workspace fees.

### Pipeline Review & Demo Prep

  - **Music Spirit (Today):**
      - **Status:** Likely unqualified for the business tier.
      - **Action:** Nigel will take the call as practice, redirecting to the Pro plan if appropriate and gathering product feedback for Stevie.
  - **Fair (This Week):**
      - **Status:** High-potential lead from Jason's network.
      - **Business:** Wholesale marketplace with two main user types: merchants (B2C-like) and brands (B2B).
      - **Strategy:** Focus the demo on the merchant side, as it offers a larger, more relevant AI visibility opportunity.
      - **Blocker:** "Wholesale Marketplace" is a new category. Jesus must sync with Saskia to define it and map competitors.
  - **PuppyGraph (This Week):**
      - **Status:** Warm lead from the community.
      - **Action:** Jason will introduce; Nigel will drive the demo.
  - **Bardeen (Next Week):**
      - **Status:** Warm lead from Nigel's network.
      - **Business:** Pivoted to a web scraping tool.
      - **Blocker:** "Web Scraping" is a new category. Jesus must define it and map competitors.
  - **Viscus (Next Week):**
      - **Status:** Advisory firm for dental tech companies.
      - **Qualification:** Potentially qualified, but CheckThat is not designed for location-based services. The focus is B2B SaaS.

### Lead Generation & Outbound Strategy

  - **Current Performance:**
      - **Outreach:** 40 people contacted (Director+ level).
      - **Results:** Low demo volume, with recent bookings (Fair, Bardeen) coming from existing network connections, not cold outreach.
  - **Workflow Blocker:** The Clay enrichment workflow is too strict, filtering out qualified sign-ups. Jason will loosen the criteria.
  - **Outbound Plan (Nigel):**
      - **Tools:** LinkedIn Sales Navigator (purchase pending), Ordinal (for lead capture from posts).
      - **Process:** Start with manual outreach to identify effective patterns, then scale with Understory.
      - **Leverage GrowthX Assets:** Offer free resources (e.g., AEO workshop recordings) to secure demos.

---

## Action Items

**Nigel Hammett (CheckThat Sales Lead)**
- Send Marcel's CheckThat deck to Jason; then Jason add Augment Code color
- Start manual LinkedIn outbound via LinkedIn Sales Navigator
- Add Music Spirit notes to Notion
- Run Music Spirit call; if qualified create HubSpot deal; send recording to Jason
- Run PuppyGraph call (Jason intro, Nigel drives demo)

**Jesus Yepez (CheckThat Ops)**
- Set up remaining CheckThat workspaces including Fair, Bardeen, and Viscus
- Sync with Saskia (GrowthX) to define Wholesale Marketplace category and map competitors
- Co-create playbook/process for defining new competitor categories

**Jason Gong (CheckThat Product Lead)**
- Co-create playbook/process for defining new competitor categories with Jesus
- Verify post-onboarding email automation is functioning correctly
- Loosen Clay enrichment qualification criteria; update signup enrichment/qualification flow
- Loop Nigel into AEO workshop planning for lead generation leverage
- Run PuppyGraph call (intro only; Nigel drives demo)

---

## Cleaned Transcript

**Jason Gong:** Hey, everyone. So new meeting. This meeting is being recorded. It's mainly just to keep on top of the sales funnel and business plan. Today I mainly wanted to talk about the companies we have coming up and this demo process I tried to create. Jesus is here to help Nigel, because at some point creating all these workspaces might be a lot to do.

**Nigel Hammett:** Appreciate that. On my side, we have the Music Spirit call coming up. They're probably not qualified at the business tier, but I want to get that first conversation going and see what they're looking for. I still owe you the slide deck—I'm putting it together based on what we already had. It'll be good for official clients that want to see visuals and walk through things.

**Jason Gong:** I think the deck would be great to look at since the example you're using is probably Augment Code, which was my client until a month ago when I handed it off. I could add a lot more color and surface interesting things to show.

**Nigel Hammett:** Please.

**Jason Gong:** Send that over to me. I have a setup guide here. Right now step one is setting up the workspace, making sure the artifacts are in place, categories are right, and competitors are filled in. Step two is generating prompts. I've set Jesus up to do this in Cursor, and I've been trying to get a self-serve site working. At some point this becomes a button in the product. For demo prep, the key insight is to show one really sharp example where they feel like a competitor has shown up and they haven't. We want them to feel like we've told them exactly what they need to do for the rest of their business.

**Nigel Hammett:** For sure.

**Jason Gong:** After the call, if they're qualified, we add them to a Slack channel. That gives us an unencumbered way to reach out, unlike email they'll keep ignoring. The key is to give them a reason to join—like, I'll send you the slides in the Slack channel. Once they're in there, it's 10 times easier to get a hold of them. Any thoughts on this process?

**Nigel Hammett:** Yeah, pretty much spot on. Quick question on the Slack setup. Should we do that before contract negotiations, or right after the first call?

**Jason Gong:** I think we set it up right after the first call. The invite probably works better at the end of the call. I talked to Bridget last week, and they have an itemized deal object in HubSpot, so we can track whether it's a GrowthX or CheckThat deal. For the folks we're talking to today, maybe after them we can set that up. Nigel, send that sales deck when you can.

**Jesus Yepez:** I've only set up the workspace for Music Spirit so far, but I plan to set up Fair today since that call is in two days.

**Jason Gong:** Any parts of that process that seemed broken or blocked you?

**Jesus Yepez:** When I created the brand profile, it created a company overview that was different from the context company overview in the other section of CheckThat.

**Jason Gong:** Was it inaccurate or just worded differently?

**Jesus Yepez:** Just worded differently.

**Jason Gong:** That's okay. We have a public page for Google that has more context, and the internal artifact is stripped down. Its main purpose is to help generate the right prompts. It's totally okay that they're different. Let me know if anything else is blocking. As long as it's working for you, let's set up the rest of these spaces.

**Jason Gong:** For these call candidates, some are probably disqualified, but Nigel, feel free to take them as practice and maybe redirect to Pro if appropriate. Gather product feedback for Stevie. Fair is different—they're a wholesale marketplace and extremely qualified. I'm connected with their SEO lead. Last time I talked to them, they were looking at Profound and Peak. They'd be awesome GrowthX and CheckThat customers. The challenge is they have two main user types: merchants (end stores buying wholesale) and brands (companies looking to sell through Fair). We should focus the demo on the merchant side since there are 10 times more merchants than brands. That's the bigger AI visibility opportunity.

**Nigel Hammett:** For customers with multiple products, getting an understanding of what's most important in the first call makes sense.

**Jason Gong:** Cool. On pricing, we want to gate on total prompt count across workspaces, not per-workspace fees. That way, if they split 2,000 prompts across three workspaces, that's fine. If they need 2,000 each, then we can charge extra. But the bigger issue is we don't have a category for wholesale marketplaces. Jesus, you need to sync with Saskia to define it and map competitors.

**Nigel Hammett:** That makes sense. We did it that way at WriteSonic, and I see it across the industry.

**Jason Gong:** PuppyGraph looks good. I checked the prompts and the space is set up well. They actually show up for quite a few of them. The founder is pretty active in our community and has come to events, so she's friendly. Nothing else to flag there. Bardeen is different—they've pivoted, and now their main product is a web scraping tool. I don't know if we have a category for that. If not, we should probably make one. The issue is our categories are kind of right, but not what companies call themselves. Clay might call themselves an enrichment tool, but we have them categorized differently. We need a better process to define new categories before we get on calls and try to charge money.

**Nigel Hammett:** That seems like a common problem, honestly.

**Jason Gong:** Exactly. So I'll create a playbook with Jesus. We can use search engine tools to find good product categories and then map competitors. Bardeen is probably web scraping, maybe lead prospecting or account research. We'll see which terms people actually search for. It's next week, so we have time. Viscus is interesting. They're an advisory firm for dental tech companies, next Friday. They're more of a services business, which we don't necessarily cover with CheckThat. If it's location-based, like a local plumber, CheckThat wouldn't work. Our first iteration stays with B2B SaaS since that's where GrowthX has expertise. Viscus is probably not the highest priority, but higher than Music Spirit.

**Jason Gong:** On sourcing, we haven't gotten many calls. How many people have you reached out to so far?

**Jesus Yepez:** 40 people.

**Jason Gong:** 40. And they're all qualified companies at what level?

**Jesus Yepez:** Director, manager, senior executive level.

**Jason Gong:** Okay. So one thing is the post-onboarding email—let me double-check that's working. The other is the Clay enrichment workflow is probably too strict. It's filtering out qualified sign-ups. I'll loosen that criteria.

**Nigel Hammett:** Fair and Bardeen came from our network. The Bardeen one even got an AEO session request this morning. So outside of network connections, has the cold outreach produced anything yet?

**Jesus Yepez:** Nigel, I'm CCing you on those outreach emails. I wanted to know if you're receiving them in your inbox or spam folder.

**Nigel Hammett:** Just the ones that go out?

**Jesus Yepez:** Yeah, just the ones that go out.

**Nigel Hammett:** Let me check. For my GrowthX email?

**Jesus Yepez:** Yeah, GrowthX.

**Nigel Hammett:** I don't think I've been receiving them, but I do get responses when people reply. I get the ones from Jason though.

**Jesus Yepez:** Okay, got it.

**Nigel Hammett:** Sorry, they just haven't gone out the past couple of days over the weekend, but I'm getting them. Also, I was working on that slide deck and I forgot—Marcel already has a CheckThat overview from a few years ago. I can utilize that and combine it with what I have.

**Jason Gong:** I didn't know he already had stuff. That's great. How much did he have?

**Nigel Hammett:** About 50 pages.

**Jason Gong:** That's great. We used to run workshops with a 50-slide thing we'd bounce through. Most of the time we never take folks through a slide deck though—we just talk and pop up slides as needed. The Clay workflow isn't great. Everyone who signs up comes through, gets enriched, gets qualified, and if qualified gets an email. It might be a little strict. I'll work on loosening that.

**Jason Gong:** On outbound, I'm purchasing LinkedIn Sales Navigator today. I'm going to use my platform—I post about sales and tech anyway. I'll reach out to different brands, startups, folks who aren't on big competitors. Just start conversations and see where it goes.

**Jason Gong:** Cool. We have Understory who can help automate outreach once you find patterns. But start manual. We can also help amplify your content. If you post about AEO and people engage, we have tools that capture those engaged leads. There's Ordinal which pulls leads from your posts. If you find a pattern that works—like reaching out to SEO guys at a certain company type gets replies—we can scale that later. We basically have a lot of GrowthX resources: ads, people for socials, events. We're doing an AEO workshop later this month. I'll loop you into that. If we get a couple hundred people, that generates leads, and you can use it in outreach. You can offer people free resources—like AEO workshop recordings. If you think they're a really good fit, like VP level, you could invite them to dinners too. It'll help get the call.

**Nigel Hammett:** I'm a member of some of these resources, but I may need admin access later.

**Jason Gong:** I'll set that up. For the demos, send the sales deck. For Music Spirit, feel free to run it as practice and maybe redirect to Pro if appropriate. Gather feedback for Stevie. Fair is high priority. Use the network connections to get them on the calendar. PuppyGraph—I'll do a quick intro since I know her, but you drive the demo.

**Nigel Hammett:** I'll send the slide deck, at least Marcel's version. I'll double-check it for Music Spirit and drop some notes in Notion. The Music Spirit call is happening soon—it'll be good practice before PuppyGraph.

**Jason Gong:** If you want me on the Music Spirit call, I could totally join.

**Nigel Hammett:** No, it doesn't seem qualified, so I'll take it solo. If it's interesting, I'll send you the recording and share learnings later.

**Jason Gong:** For PuppyGraph, I'll do a quick intro but you drive. You'll have the Music Spirit call in 20 minutes as mini practice for PuppyGraph. We'll see where we end up by end of day.

**Nigel Hammett:** Throughout the day I'll send those emails and work on battle cards.

**Jason Gong:** Sounds good. We're all set.

---

## Original Transcript
**Jason Gong:** Hey, everyone.

**Nigel Hammett:** Hey, Jason.

**Jesus Yepez:** Hey, Hey, Nigel.

**Nigel Hammett:** Hey, Jesus.

**Jason Gong:** All right.

**Jason Gong:** So new meeting.

**Jason Gong:** Also just copied what Bridget does over on the...

**Jason Gong:** This meeting is being recorded.

**Jason Gong:** Keeps everything super organized, but I'll share my screen.

**Jason Gong:** Yeah, basically like a few things.

**Jason Gong:** It's mainly just to like keep on top of like the funnel we have for the business, the business plan.

**Jason Gong:** So this week, I think it's...

**Jason Gong:** it's...

**Jason Gong:** Uh...

**Jason Gong:** We'll see just chatting about all the demos we have coming up, but we'll also talk about like different things we're doing to drive more.

**Jason Gong:** You know, like at some point we'll probably like bring in the understory guys and do a bit of outbound.

**Jason Gong:** I don't know if we'll totally have time for that today, but like today I mainly just wanted to talk about the companies we have coming up and then this process that I tried to create.

**Jason Gong:** And Jesus is here to help Nigel, because I know at some point like creating all these workspaces might be a lot to do.

**Jason Gong:** don't think it is yet, but Jesus is here to help kind of set things up.

**Nigel Hammett:** Appreciate that.

**Jason Gong:** Yeah.

**Jason Gong:** Sorry, go ahead.

**Nigel Hammett:** Yeah, yeah.

**Nigel Hammett:** My side really quickly, I know we have the call coming up for Music Spirit.

**Nigel Hammett:** Definitely probably not qualified at the business tier.

**Nigel Hammett:** I really just want to kind of get that first conversation going.

**Nigel Hammett:** See what they're looking for, see how I can help.

**Nigel Hammett:** And then I still owe you the slide deck.

**Nigel Hammett:** I'm kind of just passionate.

**Nigel Hammett:** I'm up together based off what we already had.

**Nigel Hammett:** may probably won't even use that today, but it will be good, especially for like those official clients that actually want to see some visuals and kind of walk through some things.

**Nigel Hammett:** Yeah, and that was music spirit.

**Jason Gong:** But yeah, I don't want to take you anything right now.

**Nigel Hammett:** want to take all calls and then, you know, when I get more booked up, we can go from there.

**Jason Gong:** Okay, cool.

**Nigel Hammett:** Are you sick a little bit?

**Jason Gong:** Yeah.

**Nigel Hammett:** I'm sorry, I'm going to blow my nose.

**Nigel Hammett:** It's all good.

**Nigel Hammett:** Come on, Entology Sims.

**Nigel Hammett:** Okay, cool.

**Jason Gong:** I think the deck would love to look at just because I think the example you're going to use is probably Augment Code, and that was my client up until like a month ago when I handed it off.

**Jason Gong:** So I could like add a bunch more color and surface-like things that would be interesting to show.

**Nigel Hammett:** Please.

**Jason Gong:** So yeah, send that over to me.

**Jason Gong:** So

**Jason Gong:** You have it.

**Jason Gong:** Yeah, but let's go through these.

**Jason Gong:** And then the only other thing I'll flag is, so I have this setup guide.

**Jason Gong:** I think at some point this will be automated, but right now it's like step one is kind of setting up the workspace and making sure the artifacts are in there, the categories are right, and they have a few competitors filled in.

**Jason Gong:** And then step two is generate the prompts.

**Jason Gong:** I think I got Jesus set up, let me know if it actually works, Jesus, but to do it in cursor like I've been doing it, and then I've been trying to get this site working, so I might, if I have like an hour later today, I'll do that just because it'll be more self-serve.

**Jason Gong:** And then at some point this becomes a button in the product, hopefully, but I know Marcel's been kind of swamped, so he hasn't gotten to productizing what he's been working on there.

**Jason Gong:** And then...

**Jason Gong:** Yeah, and then as far as prep for the meeting, mean, totally yours to drive, Nigel, but I guess my thought just based on working with clients is like, and to Marcel's point of like, it's hard to, I guess, pull the ocean and show like the entire category.

**Jason Gong:** Like we want to show is like, just one really sharp example where they feel like , you know, my, my competitors shown up and I, I should be, but I'm not.

**Jason Gong:** And these guys have kind of told me exactly what I need to do.

**Jason Gong:** And I need that for the rest of the, you know, business essentially.

**Nigel Hammett:** For sure.

**Jason Gong:** And then after the call, I think we do this really well on the growthx side, but we essentially like, as long as you think they're qualified, like we add them all to a Slack channel and then that just gives us a really kind of like unencumbered way to like reach out to them.

**Jason Gong:** That is an email, something they'll keep ignoring.

**Jason Gong:** Um, and then the main key there is to.

**Jason Gong:** Give them a reason to join the Slack.

**Jason Gong:** like, hey, you know, I'll shoot you over the, like, link to the slides or something, like, in the Slack channel.

**Jason Gong:** You know, like, you want to frame it like that just so they're in the Slack.

**Jason Gong:** And then once they're in there, it's just, like, 10 times easier to kind of get a hold of them.

**Jason Gong:** Feel free to totally ignore this.

**Jason Gong:** I kind of just generated this.

**Jason Gong:** Yeah, any thoughts on this process?

**Jason Gong:** I know it's, like, very simple, but is this what you had in mind, Nigel?

**Nigel Hammett:** Yeah, no, pretty much spot on.

**Nigel Hammett:** Quick question on the Slack setup.

**Nigel Hammett:** Is that something that we should do here in terms of if we do feel like there's a good, strong business case?

**Nigel Hammett:** Do we start that Slack channel before, you know, contract negotiations and the sales process?

**Jason Gong:** Yeah.

**Jason Gong:** Yeah.

**Jason Gong:** I think in general, like, even on GrowthX, we set it up basically, like, right after that first call.

**Jason Gong:** And even if you want to do it before the call.

**Jason Gong:** I think it could work, but I don't know.

**Jason Gong:** I feel like the invite probably works better, like, at the end of that call.

**Jason Gong:** So we need to do that.

**Jason Gong:** I think the best approach is probably to create a new workspace.

**Jason Gong:** I don't know.

**Nigel Hammett:** Did you do this at WriteSonic at all or no?

**Nigel Hammett:** No, we keep the workspaces the same and, you know, you just transfer over the license and if they want to edit it, change it, you know, they can do that from there.

**Jason Gong:** Okay, got it.

**Jason Gong:** I think...

**Nigel Hammett:** Because ideally, we want all the data to live in one place and if we're setting it up good, it's, like, less work for them to do once they get, you know, once they get it set up.

**Jason Gong:** Oh, I see.

**Jason Gong:** But, like, did you do Slack channels with your customers or...?

**Nigel Hammett:** Oh, yeah, but only after, you know, they sign.

**Jason Gong:** Okay, got it.

**Jason Gong:** I think we can do it without.

**Jason Gong:** I'm just going to create...

**Nigel Hammett:** But that's a good idea, though, to drive up implementation.

**Jason Gong:** Yeah, I mean, at some point, it might be, like, oh, man, there's two...

**Jason Gong:** So I talked to Bridget last week, and they do have an itemized deal object in HubSpot, meaning all the deals are tracked in HubSpot, and then you can kind of select whether it's a growthx deal or a check that deal.

**Jason Gong:** So, yeah, I mean, for the folks we're talking to today, maybe after them, we can try to create that in HubSpot.

**Jason Gong:** Anyway, Jesus, okay, cool.

**Jason Gong:** we have that sales deck, shoot that over when you can, Nigel.

**Jason Gong:** then, okay, so for the demos, just some things to flag.

**Jason Gong:** I guess first thing, Jesus, were you able to set up these workspaces?

**Jesus Yepez:** Only the one for music spirits, but I plan to set up those today, especially the fair one, because with HubSpot.

**Jesus Yepez:** of Thank

**Jesus Yepez:** I think it's in two days.

**Jason Gong:** Like any parts of that process that seemed broken or it was like a blocker for you to do it very quickly?

**Jesus Yepez:** I was just confused on...

**Jesus Yepez:** So when I created the brand profile, it created the company overview.

**Jason Gong:** And it was different from the context company overview in the other section of CheckDot.

**Jason Gong:** I see.

**Jason Gong:** What was it like inaccurate or was it just like a little bit worded differently?

**Jesus Yepez:** Yeah, worded differently.

**Jason Gong:** Okay.

**Jason Gong:** I think that's okay.

**Jason Gong:** I guess the way we do those pages is there's a public page that people on Google see and that page will have like more text and it'll have more kind of context.

**Jason Gong:** And then the internal artifact is a little bit more kind of stripped down.

**Jason Gong:** And the main purpose of that artifact is to help generate the right prompts.

**Jason Gong:** So it's totally okay.

**Jason Gong:** They're different.

**Jesus Yepez:** Okay.

**Jesus Yepez:** Okay.

**Jason Gong:** Okay, cool.

**Jason Gong:** If nothing's blocking, let me know.

**Jason Gong:** I know the custom prompting probably could be better, so I'll work on that a little bit later, but as long as it's working for you, let's try to set up the rest of these spaces.

**Jason Gong:** Okay, great.

**Jason Gong:** And then as far as calls go, yeah, these are probably disqualified, but Nigel, feel free to just take those to get a rep, and then it's actually not a bad spot to try to redirect them to pro if you think they're just totally unqualified, and then see if they're running into any blockers, and then we can share with Stevie.

**Jason Gong:** Absolutely.

**Nigel Hammett:** So this one I might not join, just because if it's cool, it's probably not going to be a deal.

**Jason Gong:** I'll kind of work on something else.

**Jason Gong:** then these four I'll see pretty good.

**Jason Gong:** So just to call out, so Fair, I'm connected with their SEO lead, and I asked them to kind of try that.

**Jason Gong:** So I don't know if the commercial intent is super, super high on that one, but it'll be good to get feedback.

**Jason Gong:** As a company, they're extremely qualified.

**Jason Gong:** think last time I talked to them, he was looking at Profound and Peak, maybe, but I don't know if they ended up actually buying anything.

**Jason Gong:** They would be an awesome growthx customer, and they would be an awesome checkback customer.

**Jason Gong:** So it's a really, really good relationship to build there.

**Jason Gong:** Their product is like a wholesale marketplace.

**Jason Gong:** So it's like, cool, if I run a little convenience store or like, you know, sometimes like LA, whatever, like you just have these shops that stock like mugs and like cool shirts like that.

**Jason Gong:** Like basically, to stock that store, they would go on fair to buy all this stuff wholesale.

**Jason Gong:** And I shared a few keywords they might care about, but they say that the difficulty with fair is like they have three different, like, I guess, stakeholders to their business.

**Jason Gong:** want on doesn't it

**Jason Gong:** They have, like, the end merchant, who's, like, the store who's Googling, like, mugs wholesale or, like, t-shirts wholesale or something like that.

**Jason Gong:** They have the brands, which is, like, the companies that, like, want to unlock ways to sell their product.

**Jason Gong:** That isn't them, like, hitting people up or hitting up Target.

**Jason Gong:** And then they also have, actually, wait, is it just two?

**Jason Gong:** Yeah, it might just be two.

**Jason Gong:** Sorry, it's not working.

**Jason Gong:** So, like, you can map out either of those, but I think mapping out the merchant side is a little bit, makes a little bit more sense for AI visibility just because there's, like, 10 times more merchants than there are, like, brands they stock.

**Jason Gong:** Yeah, so that's that one.

**Jason Gong:** Any questions on Fathom?

**Nigel Hammett:** So in a situation where they have multiple products, and this is going to be done in the first call, I would imagine kind of just getting an understanding what's the most important.

**Jason Gong:** If we have any of those customers, yeah.

**Jason Gong:** But if we do, we should probably flag it because engineering needs to build that in.

**Jason Gong:** But right now they would need like a separate workspace.

**Nigel Hammett:** Yeah.

**Nigel Hammett:** And just so I know that wouldn't be, would that be an additional cost per workspace?

**Jason Gong:** I think we still want to charge just, we still want to gate on number of prompts and then.

**Nigel Hammett:** For sure.

**Jason Gong:** I don't know, actually, let's see.

**Jason Gong:** Did you all charge for that at RightSonic?

**Jason Gong:** Do you think it makes sense to like charge for that?

**Nigel Hammett:** Yeah.

**Nigel Hammett:** So we had it in two ways and I see this across the industry as well.

**Nigel Hammett:** really based off the number of prompts.

**Nigel Hammett:** So you could say, hey, we're going to have like us 2,000 prompts and split those across three workspaces.

**Nigel Hammett:** That doesn't cost us extra money.

**Nigel Hammett:** So, yeah, I think that's fine.

**Nigel Hammett:** long as they're willing to split the number of prompts that we're giving.

**Nigel Hammett:** Now, if they need 2,000 each, which is a lot, or whatever number each, then, you know, it could be additional costs.

**Jason Gong:** couloucaz.

**Jason Gong:** Because So.

**Jason Gong:** So, you.

**Jason Gong:** Cool.

**Jason Gong:** So I think one thing, just because I'm pretty sure we do not have that, is we should probably set up the category, Jesus, sync with Saskia, to learn how to do that.

**Jason Gong:** But I'm just going to put this here.

**Jason Gong:** Basically, it'll be, like, I don't think they'll have any competitors right now if we just loaded them in, because I don't think we've ever mapped out wholesale marketplaces.

**Jason Gong:** So we need to do that.

**Jason Gong:** Puppygraph, I looked at the prompts.

**Jason Gong:** I think the space is, like, set up pretty well.

**Jason Gong:** And surprisingly, they actually show up for quite a few prompts.

**Jason Gong:** The founder is, like...

**Jason Gong:** Pretty active in our community.

**Jason Gong:** She's come to a couple events, so she's quite friendly there.

**Jason Gong:** Nothing else I'd call out.

**Jason Gong:** Any questions from your side on PuppyGraph?

**Jason Gong:** Oh, you're muted.

**Nigel Hammett:** Sorry.

**Nigel Hammett:** I was saying it seems pretty straightforward for PuppyGraph.

**Nigel Hammett:** I'm looking forward to that one.

**Nigel Hammett:** And I'm realizing that Marcel, yourself, just the team, we have a lot of great relationships.

**Nigel Hammett:** So a lot of folks are familiar with what we've done on the content side.

**Nigel Hammett:** I just kind of want to take a look and see if it can work for them at Check That.

**Jason Gong:** Yeah.

**Jason Gong:** And I think it'll be good to get the zero to one here.

**Jason Gong:** And then at some point, we got to go outside the network.

**Jason Gong:** But Bardeen's also a relationship.

**Nigel Hammett:** I used to be head of growth at Bardeen.

**Jason Gong:** And the founder wanted to work with us on GrowthX side, but it's a little bit expensive.

**Jason Gong:** Bardeen is kind of an interesting case where they've pivoted.

**Jason Gong:** And now their main product.

**Jason Gong:** product.

**Jason Gong:** is a scraping tool.

**Jason Gong:** So I don't know if we have a category for that, actually.

**Jason Gong:** If not, we should probably make one.

**Nigel Hammett:** know this is like, this seems to be a common thing, honestly.

**Jason Gong:** So they would categorize themselves as probably like web scraping.

**Jason Gong:** Or let's see, maybe like lead.

**Jason Gong:** Like, I don't know what category clay is in, but they kind of like, like, they're not exactly that, but they're like a researcher, you know?

**Jason Gong:** Let's see, clay.

**Jason Gong:** But that probably needs to be cleaned up a bit.

**Jason Gong:** ABM software, okay.

**Nigel Hammett:** Lead management, eh.

**Jason Gong:** Not really.

**Jason Gong:** Where's clay?

**Jason Gong:** I'm here.

**Jason Gong:** Clay.

**Jason Gong:** Clay.

**Jason Gong:** See, it's like our categories are like kind of right, but they're definitely not the one they use to describe themselves.

**Jason Gong:** Like Clay, like they might call themselves like an enrichment tool.

**Jason Gong:** Maybe they call themselves like...

**Nigel Hammett:** Yeah, do some sequencer maybe.

**Nigel Hammett:** Not really.

**Nigel Hammett:** CRM.

**Jason Gong:** Maybe.

**Nigel Hammett:** Yeah, CRM.

**Jason Gong:** Yeah, so I think that, okay, so that needs a process actually.

**Jason Gong:** Need a better process to, what do we call it?

**Jason Gong:** Kind of define random categories.

**Jason Gong:** Like we're aware of this problem, but I guess we're actually getting on a call and trying to charge a bunch of money.

**Jason Gong:** Like, this is probably the highest bar we need to hit and end clients, I guess.

**Nigel Hammett:** Right.

**Jason Gong:** So...

**Jason Gong:** I need a playbook plus process to update the workspace.

**Jason Gong:** So I'll do this one with Jesus.

**Jason Gong:** I'll do a similar thing.

**Jason Gong:** I'll just create a doc for it.

**Jason Gong:** I think you could basically use search engine tools to get a good list of product categories and then the competitors do all that stuff.

**Jason Gong:** Yeah, but anyway, like Bardeen's kind of web scraping, maybe like lead prospecting, you know, account research.

**Jason Gong:** I mean, we'll see which one of these terms, like what web scraping for sure is like a term people search for in these two.

**Jason Gong:** I'm not totally sure.

**Jason Gong:** This one's next week.

**Jason Gong:** So we have time.

**Jason Gong:** And then this one's like super interesting.

**Jason Gong:** I don't know who they are, but it looks like they're like one of those roll up, like, like small business things.

**Jason Gong:** Like it's like a business partners.

**Jason Gong:** Yeah.

**Jason Gong:** I the viscus, so strategic growth mark, oh actually, what are they, dental tech companies, have you looked at this one yet, Jesus, or not, not yet?

**Nigel Hammett:** I haven't seen these guys either, no, he's dental partners, Deidre's dental tech, AI, huh, it's kind of nifty.

**Jason Gong:** Yeah, this one is, can't find, when the call is, oh, this one's next Friday, okay, so we have quite a lot of time for this one.

**Jason Gong:** Oh, this one's more advisory, okay, so this one might be a little bit less qualified, or it's Switzerland, yeah, okay, nevermind, I think it sounds great, I think it's qualified.

**Jason Gong:** I'm just trying to appear, but I think it's kind of interesting, it's like more of like a services business, which we don't necessarily cover with CheckVat.

**Jason Gong:** Like if it was like a, like if it was local, CheckVat would not be able to cover for it, like if it like a local plumber or something like that, like we don't do the whole location to work for something like that, but this.

**Jason Gong:** This is potentially.

**Nigel Hammett:** And why don't we do the localization just like, that's not our focus at slash ICP or.

**Jason Gong:** Yeah, I think our like, like our first iteration of this, we wanted to kind of keep to B2B SaaS.

**Nigel Hammett:** Got it.

**Jason Gong:** Just because that's where our expertise is on growthx.

**Nigel Hammett:** For sure.

**Jason Gong:** And then dental.

**Jason Gong:** Okay, so I think this one, baby, like.

**Jason Gong:** Weird, probably not the highest priority, but I would put it higher than these two.

**Jason Gong:** And then, let's see.

**Jason Gong:** And then as far as sourcing goes, I feel like we're still just not getting many calls.

**Jason Gong:** Were you able to check, Nigel, on the outreach we've done?

**Jason Gong:** Like, if anyone replied saying anything, even?

**Nigel Hammett:** Yeah, I think over the weekends, I mean, some calls came in.

**Nigel Hammett:** I would also keep in mind, we haven't even emailed the entire list yet, so.

**Jason Gong:** We're still going through it.

**Jason Gong:** I mean, this one's Bardeen.

**Jason Gong:** This one's Fair.

**Nigel Hammett:** Like, I got the AEO session for next Tuesday.

**Nigel Hammett:** That just came in 2 o'clock this morning from, yeah, the Bardeen one.

**Jason Gong:** Yeah, that was the Bardeen one.

**Jason Gong:** So I feel like outside of those, which are like our own network.

**Jason Gong:** Has anything happened there?

**Jason Gong:** Like, how many folks have you reached out to so far?

**Jesus Yepez:** 40.

**Jesus Yepez:** 40 people.

**Jason Gong:** 40.

**Jason Gong:** And they're all kind of, like, you know, qualified company plus, like, what level do you think that would be?

**Jesus Yepez:** Like, mid-level, director?

**Jesus Yepez:** Yeah, director, manager, senior executive.

**Jason Gong:** Yeah.

**Jason Gong:** Okay, so that's one, I guess, Nigel, working for sign-up list, and the other one, we already have the, like, post-onboarding email that is, let me just double-check that's actually working.

**Jason Gong:** Whoops.

**Jesus Yepez:** Nigel, I'm CCing you on those outreach emails.

**Jesus Yepez:** emails.

**Jesus Yepez:** Emails, but I wanted to know if you're receiving them on your inbox or spam folder.

**Nigel Hammett:** In terms of responses or like just the ones that go out?

**Jesus Yepez:** No, just the ones that go out.

**Nigel Hammett:** Let me check.

**Nigel Hammett:** Thought I was.

**Nigel Hammett:** For my check that email or for my growthx email?

**Jesus Yepez:** Growthx, yeah.

**Nigel Hammett:** I don't think I've been receiving them, but I get the responses, obviously, you know, when somebody replies, et cetera.

**Jesus Yepez:** Okay.

**Jesus Yepez:** Got it.

**Nigel Hammett:** Well, I get the ones from Jason.

**Jesus Yepez:** Okay, great.

**Nigel Hammett:** Yeah, I'm getting them.

**Nigel Hammett:** Sorry.

**Nigel Hammett:** It's just they haven't gone out in a couple of days over the weekend.

**Nigel Hammett:** I'm getting them.

**Nigel Hammett:** I'm getting them.

**Nigel Hammett:** And then, too, I was working on that slide deck, Jason, and I forgot.

**Nigel Hammett:** Just remember, Marcel already has the check that overview.

**Nigel Hammett:** few years ago,

**Nigel Hammett:** Which I can utilize as well.

**Nigel Hammett:** Just kind of combine what I have in the slides that he made.

**Jason Gong:** Okay, cool.

**Jason Gong:** I actually didn't know he already had some stuff.

**Jason Gong:** That's great.

**Nigel Hammett:** He's got a lot.

**Nigel Hammett:** He went like 50 pages.

**Jason Gong:** That's great.

**Jason Gong:** Yeah, for the longest time, think Tyler was using just like we used to run these workshops.

**Jason Gong:** So there's like a 50 slide thing and he would just kind of like bounce through it.

**Jason Gong:** Because like most of the time, yeah, we never take folks through a slide deck.

**Jason Gong:** It'll just be like talk and then pop up the slides.

**Jason Gong:** This looks qualified.

**Jason Gong:** feel like this clay workflow isn't great.

**Jason Gong:** Okay, I'll work on this.

**Jason Gong:** Basically right now what's happening is like everyone that signs up, they come here.

**Jason Gong:** And then this enriches them and then qualifies them.

**Jason Gong:** And if they're qualified, they'll get an email.

**Jason Gong:** So maybe it's being a little strict.

**Jason Gong:** Okay, so there'll be another to-do.

**Jason Gong:** Be less strict on the clay.

**Jason Gong:** Do anything else on Pipeline?

**Jason Gong:** I guess maybe after you work through that list, Nigel, we can start doing some more targeted outbound, maybe.

**Nigel Hammett:** Like, again, not expecting you to do all of it, but we'll work on something together.

**Nigel Hammett:** Yeah, no, totally fair.

**Nigel Hammett:** I'm purchasing LinkedIn.

**Jason Gong:** LinkedIn Sales Navigator.

**Jason Gong:** Oh, did you get that from us yet?

**Nigel Hammett:** No, yeah, that's happening today.

**Nigel Hammett:** You guys sent me over the cart.

**Nigel Hammett:** Yeah, it's getting purchased today, long story short.

**Jason Gong:** Okay, you got it.

**Jason Gong:** Okay, so LinkedIn Sales Navigator.

**Nigel Hammett:** So to that point, I'm going to be utilizing, you know, I have a pretty big LinkedIn as well.

**Nigel Hammett:** And I always post, you know, content about sales, tech, or whatever.

**Nigel Hammett:** But just using my platform to reach out to folks cold, whether it's different brands.

**Nigel Hammett:** Maybe if I know that they're not, you know, on a big competitor, any startups, et cetera.

**Nigel Hammett:** And just kind of reaching out, starting that conversation and going from there.

**Nigel Hammett:** And I'll do that.

**Jason Gong:** Cool.

**Jason Gong:** That would be awesome.

**Jason Gong:** Let's see.

**Jason Gong:** Let me know what you need there.

**Jason Gong:** We have, I guess, lot of, we have Understory who can help us automate some of the outreach.

**Jason Gong:** Okay, that would be can hear, just so you can see, like, stuff we're doing.

**Jason Gong:** Okay.

**Jason Gong:** Oh, you're here already.

**Nigel Hammett:** Yeah.

**Jason Gong:** So they could do that.

**Jason Gong:** Like, if you find a pattern that works, like, cool.

**Jason Gong:** If I reach out to the SEO guy and I say this and this is the type of company, like, they usually reply.

**Nigel Hammett:** can kind of, like, add scale to that later.

**Nigel Hammett:** Nice.

**Jason Gong:** But I would start, like, manual.

**Jason Gong:** And then we can also enrich some of your info.

**Jason Gong:** So, like, like, if you start posting about AEO and people engage with it, we have a tool.

**Jason Gong:** Actually, I'll add you right now.

**Jason Gong:** Actually, we have a couple tools here, so I'll you to all of them.

**Nigel Hammett:** This tool.

**Jason Gong:** This tool basically, like, takes all the people that engage with your LinkedIn and then, oh, I think you can sign it.

**Nigel Hammett:** We have tools for everything.

**Jason Gong:** I love it.

**Jason Gong:** And then, if you want to post more on socials, we have this.

**Nigel Hammett:** SIF data?

**Jason Gong:** Yeah, it's called Original.

**Jason Gong:** Basically, it also does something where it can pull, like, leads from.

**Jason Gong:** So, like, for example, I made this post.

**Nigel Hammett:** Okay.

**Jason Gong:** Seemed to do pretty well, I guess.

**Jason Gong:** But then you can kind of see all the people that like it and then use it to pick out, like, you know, cool, CEO, maybe their company, you know, makes sense.

**Jason Gong:** Yeah, I guess not many marketers.

**Jason Gong:** So...

**Jason Gong:** So...

**Jason Gong:** Thank

**Jason Gong:** MVP of go-to-market.

**Jason Gong:** Oh, this is a client.

**Jason Gong:** Yeah, but this too could help.

**Jason Gong:** But if you want to be more consistent, post it on socials.

**Nigel Hammett:** Sift it or try ordinal.

**Jason Gong:** Yep.

**Jason Gong:** And then this one's called, this one's called ordinal.

**Jason Gong:** Cool.

**Jason Gong:** Okay.

**Jason Gong:** try some outbound.

**Jason Gong:** I guess we can add that here.

**Jason Gong:** And then, cool.

**Jason Gong:** So, basically, this one, I think the, like, if you find anything that works, then, you know, it'll be my job to, like, amplify it.

**Jason Gong:** We're also bringing on, I mean, we, we.

**Jason Gong:** We basically just have a lot of resources on the growthx side.

**Jason Gong:** Because check that so early, haven't totally brought them here yet.

**Jason Gong:** We have ads, have people that go straight for socials, we have events.

**Jason Gong:** That's actually something to flag later this month.

**Jason Gong:** We're trying to do a workshop on AEO.

**Jason Gong:** I'll loop you into that, but hopefully if we get a couple hundred people to that, that'll generate a bunch of leads as well.

**Jason Gong:** And then that can also be something you can use in your outreach, actually.

**Jason Gong:** So I can show you what we do.

**Jason Gong:** An example of the Fletch workshop that we're doing.

**Jason Gong:** That's what we're

**Jason Gong:** Flow on how, you know, we optimize that for them.

**Jason Gong:** Nice.

**Jason Gong:** Would you like the recording?

**Jason Gong:** then it's like more people are willing to kind of engage with that.

**Jason Gong:** And then once they engage, they're like, oh, yeah, thank you.

**Jason Gong:** This is awesome.

**Jason Gong:** Then you're like, cool.

**Jason Gong:** You know, we'd love to kind of do a session with you and kind of like look through your strategy live.

**Jason Gong:** You know, here's my calendar.

**Jason Gong:** So if you want to do that, we have a ton of resources basically here.

**Jason Gong:** Like if you see it, if you see it here, like you can offer it to, like we usually charge for it, but you can offer it to people for free if you think it'll get you a demo call.

**Nigel Hammett:** I'm a member, but I may need admin access.

**Nigel Hammett:** I don't need it now.

**Nigel Hammett:** When the time comes, I may need that.

**Jason Gong:** Okay, cool.

**Jason Gong:** So let's see the slide.

**Jason Gong:** So offer people LG resources or...

**Jason Gong:** slide.

**Jason Gong:** And if you think they're, like, a really good fit, you could even, like, generally, if they're, you know, like, VP level, plus you could invite them to, like, a dinner or running as well.

**Jason Gong:** Nice.

**Jason Gong:** It'll help you get a call with them.

**Nigel Hammett:** Oh, yeah.

**Jason Gong:** Okay, cool.

**Jason Gong:** I think that's it on my side.

**Jason Gong:** Do you think, do you think we missed, Nigel?

**Nigel Hammett:** No.

**Nigel Hammett:** No.

**Nigel Hammett:** I'm going to send over Slide Deck, at least the one that Marcel has, so you can at least view it.

**Nigel Hammett:** And just double-check everything for music slides.

**Nigel Hammett:** And I'm to drop a couple notes in our Notion doc.

**Nigel Hammett:** For the call coming up, obviously, we're both on it together.

**Nigel Hammett:** Yeah.

**Nigel Hammett:** Do you?

**Nigel Hammett:** No, it was probably, just because they don't seem that qualified, I'm going to suck.

**Nigel Hammett:** Cool, cool, yeah.

**Jason Gong:** If you want me on it, I could totally enjoy it.

**Nigel Hammett:** No, no, no, no.

**Nigel Hammett:** Oh, good.

**Nigel Hammett:** That makes it easier.

**Nigel Hammett:** I'll take it.

**Nigel Hammett:** And then if it's interesting, shoot you over the recording and share my learnings later.

**Jason Gong:** Okay.

**Jason Gong:** That sounds good.

**Jason Gong:** And then for the call with PuppyGraph later, I'll let you drive, honestly, but I'll, you know, like I think she came to an event or she knows me.

**Jason Gong:** So I'll just like do a quick little intro, but I'll let you try.

**Nigel Hammett:** Cool.

**Jason Gong:** Okay.

**Nigel Hammett:** It works.

**Nigel Hammett:** I'll use the next, the call in 20 minutes is like mini practice for PuppyGraph.

**Nigel Hammett:** And then we'll see where we end up by the end of the day.

**Nigel Hammett:** And then throughout the day, I'm to be, of course, sending out those emails, working on the battle cards.

**Nigel Hammett:** And yeah, those are my tasks.

**Jason Gong:** Okay.

**Jason Gong:** Sounds good.

**Jason Gong:** All right.

**Jason Gong:** Talk to you later, Nigel.

**Jason Gong:** Okay.

**Jason Gong:** Thanks, Wilson.
