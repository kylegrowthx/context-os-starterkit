# Tyler Phelps

<metadata>
date: 2025-08-08
time: 14:03 UTC
duration: 29 minutes
organizer: dave@growthx.ai
participants: Tyler Phelps (Diligent), Dave Capone (GrowthX)
fathom_recording_id: 79383281
fathom_url: https://fathom.video/calls/371357657
share_url: https://fathom.video/share/tYRbkDDmiyYG34ZLJNqznDNA_3RqvoRo
source: fathom
enriched_on: 2026-03-03 02:15 UTC
</metadata>

---

## Summary

Tyler Phelps, leading Diligent's newly formed growth engine division after a major organizational restructuring, met with Dave Capone to align on SEO strategy for improving product page rankings. Diligent's core challenge: strong brand SEO performance but product/solution pages rank 4th-5th when they should rank 1st-2nd. The team discussed technical SEO quick wins (auditing multi-hop redirects from recent acquisitions, migrating high-performing content from acquired sites), the need for better coordination across Diligent's content, web, and SEO teams, and how to balance LLM optimization with maintaining authoritative blog content. Key next steps: audit redirect chains from Vault, BoardFX, and BoardDocs acquisitions; develop LLM tracking dashboards in Looker; and establish Monday afternoon working sessions to move from strategy to execution.

---

## Context

Tyler Phelps is the newly appointed leader of Diligent's growth engine, overseeing SEO, Geo, and SEM — a position created as part of a major reorganization shifting Diligent's 110-person demand generation team from functional to business-unit focus. Diligent is a large enterprise GRC (governance, risk, compliance) and board collaboration software company that has grown primarily through aggressive M&A, acquiring Vault, BoardFX, BoardDocs, and Galvanize in recent years. The company maintains strong brand authority in its space but is struggling to convert that authority into product page rankings, where it's being challenged by emerging competitors. GrowthX is three to four weeks into their engagement with Diligent when this call happened, and the relationship is at a critical juncture: Tyler is still onboarding, wrestling with data source inconsistencies, and trying to get visibility into what GrowthX is actually responsible for delivering under the SOW. He needs GrowthX to operate as a strategic partner across Diligent's multiple internal teams (content, web, product marketing, the Diligent Institute thought leadership org, and web implementation teams), not just deliver content in a silo.

---

## Relevance

**To GrowthX Delivery:**
- Diligent's complexity (multiple product lines, recent acquisitions, three to four teams creating content) requires GrowthX to provide governance on content strategy, not just execution — specifically: preventing cannibalization, coordinating internal linking strategy, and owning the "who's responsible for what" clarity
- Client is pushing back on blog-heavy delivery and wants richer, more strategic product page enrichment; contract/SOW review needed to clarify baseline vs. expansion expectations
- LLM optimization (schema, FAQs, content freshness, chunking for AI prompts) is now a core delivery component; opportunity to build repeatable LLM-optimization workflows into standard engagements
- Site migrations from acquired companies present technical SEO risk (multi-hop redirects, content consolidation, domain authority flows) — this is a quick-win delivery area

**To CheckThat:**
- Diligent is actively tracking LLM visibility and prompt performance and needs a dashboard to monitor which queries CheckThat tracks are driving traffic; opportunity to upsell CheckThat integration into the GrowthX engagement
- Client explicitly mentioned balancing SERPs and LLM ranking — direct signal that AEO is becoming table stakes for enterprise B2B clients

**To GrowthX Business Development:**
- Strong account health signal: new executive onboarding, C-suite engagement (CMO/CEO operating review), multi-team complexity, and high visibility into account — Tyler is well-positioned to expand relationship across product lines
- Diligent's aggressive growth strategy (M&A, SEM expansion, CRO initiatives) suggests expansion opportunity: SEO is foundational but could expand into paid search, conversion optimization, or product positioning strategy
- Risk signal: Tyler is in "prove value" mode with a 2-4 week timeframe and is holding GrowthX accountable to business unit reporting and ranking improvements; early wins and strategic partnership positioning are critical

---

## Overview

- Diligent undergoing major internal reorganization; need for better cross-team coordination
- Focus on improving product page rankings and enriching content for LLMs
- Importance of maintaining blog content while optimizing for authority and internal linking
- Need for better reporting aligned with business units and focus on improving rankings

---

## Key Topics

### Diligent's Organizational Changes

  - Demand gen team (110 seats) reorganizing from functional to business unit focus
  - Tyler overseeing new growth engine: SEO, Geo, and SEM
  - Web team working on site migration and CMS update
  - Multiple recent acquisitions (Vault, BoardFX, BoardDocs) being integrated

### SEO Strategy and Challenges

  - Strong brand SEO, but product/solution pages ranking 4th-5th
  - Goal: Improve product page rankings to 1st-2nd positions
  - Need for better internal linking and content contextualization
  - Balancing blog content with strategic product page optimization

### Cross-Team Collaboration

  - Multiple teams working on content (SEO, web, content, Diligent Institute)
  - Risk of conflicting strategies and content cannibalization
  - Need for improved visibility and communication between teams and growthx.ai

### Technical SEO Considerations

  - Audit redirects from acquired sites to ensure proper mapping
  - Migrate high-performing content from acquired sites
  - Focus on enriching product pages with fresh, relevant content

### Reporting and Metrics

  - Develop reporting based on business units
  - Focus on improving rankings as a key metric
  - Connect SEO efforts with CRO to drive tangible outcomes

### LLM Optimization

  - Keep content fresh and enriched for LLM signals
  - Utilize schema, FAQs, and other tactics to influence LLMs
  - Balance between product page optimization and maintaining authoritative blog content

---

## Action Items

**Dave Capone**
- Check w/ Joe re LLM tracking dashboard; add prompts to Looker if exists

- Send Tyler Mon PM meeting times via Slack


**Tyler Phelps**
- Create abbrev org chart for growthx team; incl content, SEO, web teams

- Review growthx contract & SOW; focus on product content vs blogs

---

## Transcript
**Dave Capone:** Hey, Tyler. How's it going?

**Dave Capone:** Yep, can't hear you.

**Tyler Phelps:** All right.

**Dave Capone:** There we go.

**Tyler Phelps:** Okay, sweet. How are you doing? I'm doing great.

**Dave Capone:** Finally, nice to meet you.

**Tyler Phelps:** I'm sorry I had to pump this a couple days. This is my second full week under my belt here at Diligent. And we have this pretty intensive operating review coming up for our CMO and CEO. So we had somebody on my team who was out. So jumping in the deep end, just trying to figure out all of our data sources, finding the incongruencies, really kind of testing the process or lack of process that we have. So I needed all the time that I could buy back this week. So I appreciate your flexibility.

**Dave Capone:** Yeah. So I did a quick audit and ran through some things. I know Joe had done an audit as well, but there were two major things that I saw that potentially could fix a bunch of things. And I think we could talk through how to implement some of these redirects where they're multi-chain redirects that we've identified where there's like three or four different hops. But yeah, I'm happy to talk high level strategy, however it's best to utilize this time.

**Tyler Phelps:** I mean, I don't have a ton of insight into just the scope of work that GrowthX is working on. I know I've met with Ada and Joe — you guys are fairly new, I think what, three or four weeks in onboarding with us at this point. Um, so really, it seems like we're at the point of technical audits, crossing the T's and dotting the I's, cleaning up a lot of the underbelly to get domain rankings, site health, all those technical improvements so that we're getting the most out of the content that we're revamping. So yeah, let's start there. And then the only thing that I kind of want to touch on in the last few minutes is just getting, making sure that we don't have kind of a bottleneck with getting visibility around LLM reporting with you guys. And I know Scrunch is an internal tool we have, you guys are using SEMrush in a mix of our GA4 instance. And we have Ahrefs, so really just making sure that we have congruency across our data sources and then access when we need it. Because I ran into a couple of issues this week with Aiden and Joe being out. I know we were not monitoring all the prompts that we want, and it's very early in that cycle. But, you know, if something happened where they're out on vacation and we get a request from Brian, our CEO, that's a kind of an ASAP inquiry for the board — I want to be able to not kind of have our hands behind our back there. So really, internalizing tools and finding congruency between data sources would be the only other thing I'd like to touch on today.

**Dave Capone:** Yeah. So I think we can let me talk to Joe and see if they've started working on a dashboard. If they do have one, I can start adding in the prompts that we're tracking into the Looker dashboard, so everything's in one place. And then we can start adding in from GA4 — we can start adding in referrals from LLM traffic. So you can get an idea of what visibility you have per prompt and the breakdown of traffic that you're getting or clicks that you're getting. So that should be super helpful there. Let me double check. I don't see it yet. So looks like I'll have to talk to her when she gets back, but that shouldn't be an issue. Let me find your content — I think she has a bunch of stuff loaded in there.

**Tyler Phelps:** Let's see. That might be in Slack. Is it the Notion? It is the Airtable. I know I have the Airtable access. We can find that in Slack.

**Dave Capone:** So typically my role is I kind of hover around all the pods. So basically, I'm providing SEO guidance, working on audits, and really just kind of helping across all the boards for all the clients. So my level of familiarity is pretty high level. Like I'm not very granular with how much knowledge I have on each account. Let me see if I have a Notion here.

**Tyler Phelps:** Yeah, and I know that this kind of got kicked off, or at least Ada introduced us when we were discussing our internal reorganization. We have a lot of internal reorganization going on throughout the team. Our demand gen team, which is a large majority of our total marketing team — around 110 seats internally — is getting reorganized from a functional standpoint to more of a business unit standpoint. So the way that's shifting: our previous senior director of demand gen had multiple direct reports rolling up to her, and they were focused on specific functions across all products, all revenue lines, and every business unit. Now those are rolling up into individual business units on the demand side. And then our VP of demand is working on building out growth and performance marketing, which is where I sit. This is kind of one of the first seats established to build out this growth engine. So I oversee SEO, Geo — which is pretty much the same thing at this point — and then SEM. So we're bringing in an SEM manager. We have Kezia and Festus on the SEO side and Geo side. And one of my primary focuses is creating that connective tissue between us and the other teams as they're settling into this new organization. One of the pretty major projects is that we have our web team that sits under our demand gen — a group focused on a site migration, so updating our CMS, really overhauling the way that we manage our website. But we also have somebody who used to be a director of brand moving into a more strategic web role. Their focus is a little bit more on the CRO side, identifying what groups of core pages were missing, how to improve engagement on those pages, which is great for us because those are going to be drivers of on-page engagement, click-through, conversions. And all of those — if we can nail the content and context behind what we're delivering on-page — all of those are like the cherry on top that can really accelerate SEO value. But we just don't have a history or frame. So what they're working on right now is a group of role pages. They passed it over to my desk and said, can you look over this and let me know what you suggest for SEO? It's pretty hard to do that without visibility into what other pages we have out there. Are we going to cannibalize traffic by introducing these new sets of pages? So what I tried to do was create guidelines for SEO for them — when you are developing these pages, these are your considerations in order of importance. But I'd love for GrowthX to have line of sight into those type of projects that we're working on. And not just the five pieces of content that you guys are refreshing, but having total line of sight. I think it's not just beneficial, but necessary for us to do a great job together. I tossed the doc into a chat. Ada had replied and said she wanted to connect us. So I know that was the genesis behind this conversation, but I'm happy to dig into the immediate quick wins as well. Like what you think is most important — let's drive home. And then if we need to set up additional time talking through how we best support our internal teams with you guys by our side.

**Dave Capone:** So it sounds like you're going to have multiple teams working within content. SEO is a big part of that, but you don't want to create conflict in the strategy with multiple teams. So like too many cooks in the kitchen can get kind of messy, which totally makes sense. And if you already have an article about corporate governance, how can you create more content without cannibalizing or competing with stuff that's ranking now or what GrowthX is doing? I think in larger organizations that I've worked with, it's typically an editor who is going through that. They typically have the responsibility and understand all the content that's on the site, working on a content calendar, coordinating cross-functionally with different teams. Typically it's like a meeting where everybody gets together and says, okay, these are the articles that are on deck that we're publishing this week. This is what we've got in the pipeline. Do we see any conflict or issues? I don't know if that's in scope on our SOW, but typically as the relationship matures, we should be able to operate at that level regardless, right? Because we're going to know the content that we've written and whatever contributions other teams make — we should be aware of at that point. So I think it's maybe just like, here's a heads up on what these teams are publishing and is that competing with any of the stuff that GrowthX is doing?

**Tyler Phelps:** Yeah, and I don't know if that initial audit included those considerations — do we have existing pages that are competing with each other that are cannibalizing traffic or sharing a voice? Maybe for a follow-up conversation between you and me: what I can do is once the dust settles in terms of the reorganization, provide an abbreviated org chart for the GrowthX team. Because we do have a content team. I work closely with our senior director. His name's John Habib, and they work out of Optimizely, which gives them full visibility in terms of content workflows. They're getting requests from different business units. We have something called the Diligent Institute, which is a thought leadership organization underneath the parent company of Diligent. And then we've grown through a series of acquisitions — I think the pace is two to three a year. Most recently, we acquired Vault, then BoardFX and BoardDocs. So we have sites that are either in the process of getting migrated over into the Diligent site — getting integrated and deprecated — or standalone but being brought into the Diligent CMS as a separate domain and separate site, but all managed within the same Sanity platform. All of those details are really important for you guys. We have Kezia, who's our senior manager of demand but focused on the SEO side. And really what I'd like to do is pull back and look at a 10,000 foot overview of how we're working with teams, how we're connecting our agency and support in the right places, so that everybody has clarity and visibility around who's doing what. We're not stepping on toes because this is a larger organization. We have a champion brand, we are enterprise. And the sense that I've gotten is that the team has struggled with operating like an enterprise brand at the scale that we are. Our growth has primarily been driven through acquisitions rather than us actually generating pipeline in a strategic manner. I think we've done a lot of spray and pray and been pretty successful because we have a lot of authority within the space. But how do we take that to the next level through strengthening that adhesion between teams?

**Dave Capone:** It sounds like your M&A team is pretty busy.

**Tyler Phelps:** That's at least my understanding. It's been two weeks in, but we've got Vault, we're doing a migration of Fortifacts, BoardDocs, and Galvanize was the recent one on the risk side. So we made our bread and butter in GRC, primarily in board and leadership collaboration. That is our flagship. That's the easiest thing for us to expand into. But we're doing a great job with risk, entities, and market research. And we do have challenger brands nipping at our heels — you have companies like Banter. We're also doing risk with trendy startups that are making big splashes in the industry. I think we can really rely on our authority in the space. I think we're benefiting from good SEO ranking on the brand side. On the product and solution side, there's no real reason why we should be fourth or fifth in the rankings. We have enough mass and pull in the space to bring those from four or five to one and two, so we can start running better incrementality tests, really test our elasticity on the paid search side, and find ways to create feedback loops for SEO using paid search rather than operating in two different silos with no visibility into each other. For me, my perspective right now is I'm in the weeds, but that's really just to get a crash course into everything Diligent. But very soon, I'd like to pull out and make sure that we have our internal SEO teams, you, and our content teams all communicating and collaborating in the right way. That's also providing insights to our business units and collecting feedback from those business units — product marketing, field marketing, boots on the ground — getting that good, rich, in-market feedback that we could use to drive better content and content refreshes. Then we can also use the paid search side to run very quick tests and get empirical answers to hypotheses we want to test with SEO. So that is kind of my perspective right now. And I hope it's helpful in setting the groundwork for how we work together moving forward.

**Dave Capone:** Yeah. So what I'm hearing is a lot of M&A happening where you've got a lot of sites that you're migrating over to the main Diligent site. You're seeing success in SEO in some places, but not on the product side where you want to push a little bit more. I think if you've got a lot of migrations happening, a lot of content inventory, I would take a look at the redirects from the old sites to make sure they're going to the proper pages. An SEO team should identify pages that are similar and you should always redirect to similar content. And if you don't have matching content, you should link it to the homepage, for example. If you have that one-to-one detail of where links went, that's super helpful. And if there's really great performing content on those acquired sites, then I would migrate that content over and do a one-to-one link to that content and try to integrate it or use it completely on the new site, giving it a new home. So I would start there, focusing on the product pages mostly, right? Because I think that's the key takeaway — everything else seems to be performing well, but the products aren't. So double check that you don't have a bunch of links going to the homepage that should have gone to a product page, for example.

**Tyler Phelps:** Yeah, and I think it's an assignment for me to review the contract and scope of work. My initial instinct over the last two weeks is like, we don't need more blogs. We need richer product, more strategic content on the product pages. And we need to allow SERPs and LLMs to better contextualize our ecosystem of content because we do have authority in the space. If you look at our geo-reporting, we are top position and we have high presence against our competitors. That's a good indicator that we are seen as a domain with authority across these topics. How do we lean into that and kind of supercharge that? Because we might be slipping with these product pages as more challenger brands get up to speed and take market share. So that'll be a task for me over the next week or so. Let's touch on these quick win things and then maybe we'll set up some time next week when I have more focus.

**Dave Capone:** And I think from a product enrichment side, that's something we can help with — creating content to enrich those pages, keep them fresh, which are two good signals for LLMs at this point. So as we kind of think through how we can better work with one another, I think those are some areas where we can do that. But also to your point of the blog post, you still want to continually blog in the space. Even if it's thought leadership or direct content to your ICP, content in general about your space — because that shows more authority and that you're an active participant in the topic. When you stop doing those things and really concentrate on product pages, it kind of bleeds over to where you're not as active, you're not getting as many links, and you're not as authoritative. So that kind of backfires a little bit. Continuing to invest in blog content is still best practice. And then if there's no food for the spider to crawl — for example, internal linking — yeah, we don't have great internal linking. Going through blogs on our site, we just do not have great internal linking.

**Tyler Phelps:** And I think that is part of how we help search engines and LLMs contextualize and find what is connected content. Like an example: we got a request from one of our business units to launch a second blog about an ICP market scape — like an industry analyst. We ranked at the very top and we did a blog on it. No internal links to product pages. They want another blog. That blog has only gotten 32 views since it launched. It's not generating for us, and the amount of time our content team spent on it is significant. Then we have that thought leadership team, the Institute, wanting another one. And it's like, well, we're probably going to eat into that already low-performing blog. How do we do a better job connecting those things, having bi-directional linking between the content we're talking about? That's where I need to dig into the content with you guys and say, like, what actually matters? Because if we aren't generating the outcomes and results, this working relationship is going to have a shorter end. And the way I want to simplify it into two core areas is reporting based off our business units, where we're looking at our top pages — are we improving ranking? That's on the top end of the spectrum of are we improving our posture? Because we can't influence seasonality. We can't influence market surges or demand surges. There is going to be an explosion of parity across every industry with AI. And that's a great opportunity for us to capture that. We don't know when that's going to happen. So if we can improve our ranking, that improves our positioning to capture that when it does happen. And then the other thing is outcomes. We've conflated that in the past between traffic, on-page conversion rate equals outcomes equals revenue. And that's a whole lot of problems to try to solve. How do we focus in on what we can influence ourselves — connecting SEO and the strategic web team that's focusing on CRO and actually driving the results that we want. So I know we're at time here. I do have to jump. Can we set up more time? I think this conversation was helpful for me, just setting the groundwork with you. I hope it was helpful. I know it was just a lot of context and not a whole lot of getting into the stuff that we wanted to. But maybe do you have some time on Monday and we can be a little bit more hands-on with this stuff?

**Dave Capone:** Yeah, Monday afternoon should be pretty good for me. Are you East Coast?

**Tyler Phelps:** Yeah, I'm in D.C.

**Dave Capone:** I'm in Charlotte. Nice. I'm a transplant though.

**Tyler Phelps:** So me and my wife, we want to end up in North Carolina. We don't know if it's going to be the Triangle, Charlotte, or Emerald Isle or Wilmington. But I see that in our future in the next, like, five years.

**Dave Capone:** Yeah, all beautiful areas. You can't go wrong with any of them. And you're three hours from everything. If you want to go to Tennessee or Pisgah Forge, you're three hours away. So you're close to everything. But we got to talk shop because I see that guitar back there. I play also.

**Tyler Phelps:** Nice. Yeah, let's do it, Dave. I appreciate the time today. Great meeting you. You said afternoon on Monday. After 2 p.m. for me is wide open.

**Dave Capone:** Yeah, I'll send over some times in my calendar over Slack.

**Tyler Phelps:** Thanks. See you.
