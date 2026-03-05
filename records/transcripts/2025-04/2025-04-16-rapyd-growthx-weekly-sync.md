# Rapyd <> GrowthX Weekly Sync

<metadata>
date: 2025-04-16
time: 17:31 UTC
duration: 35 minutes
organizer: aida@growthxlabs.com
participants: Aida Knežević, Jakub Rudnik, Kristin Reischel, Marc Winitz, Mark Stiltner, Nicolette Mychajluk
fathom_recording_id: 57692156
fathom_url: https://fathom.video/calls/277025606
share_url: https://fathom.video/share/fzHNhspMmans_tx8NgKsDnH26gpJSXkF
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

Rapyd and GrowthX realigned their blog content strategy to focus on mid-to-enterprise merchants and payment processing solutions, shifting away from broad geographic markets like Thailand and Brazil. The team decided to track GrowthX content performance using a Looker Studio dashboard instead of modifying URL slugs for SEO reasons, while Rapyd committed to pruning irrelevant existing content and creating standardized CTAs for payments, payouts, multi-currency accounts, and all-in-one solutions. Going forward, GrowthX will deliver blog content as CSV/JSON files for Rapyd's automated WordPress integration, improving the content delivery workflow.

---

## Context

Rapyd is a fintech platform offering global payment solutions and is one of GrowthX's enterprise clients. This is a recurring weekly sync to align on content marketing strategy for Rapyd's blog, which is co-managed by both teams. GrowthX handles content creation and strategy, while Rapyd manages publishing and owns the product messaging. The relationship is mature — they're several months into content publishing and now shifting strategy based on performance data and SEO learnings. A key tension in this meeting is that Rapyd's historically best-performing blog content targets geographic payment method articles (Thailand, Brazil, China) that don't align with their new target audience of mid-to-enterprise merchants in Europe. This contextual conflict drives the decision to be more selective about which high-traffic articles to refresh, and why establishing clear content relevance criteria becomes critical for content pruning decisions.

---

## Relevance

**To GrowthX Delivery:**
- Shifting from URL slug modification to Looker Studio dashboard tracking removes a post-production touch and streamlines the reporting workflow
- Rapyd will now receive blog content as CSV/JSON files instead of individual documents, requiring GrowthX to standardize content structure and metadata
- Blog content relevance and audience targeting are now explicit requirements — GrowthX needs to validate audience assumptions (mid-to-enterprise merchants) during content planning
- Content pruning exercise signals that Rapyd values quality and focus over volume, aligning with strategic positioning efforts

**To GrowthX Business Development:**
- Account health signal: Client is refining strategy and taking content pruning seriously — indicates mature engagement and trust in GrowthX's counsel
- Expansion opportunity: Rapyd is standardizing CTAs across product categories (payments, payouts, accounts, all-in-one). GrowthX could own CTA testing and optimization for future upsell value
- Reference potential: This strategic pivot from broad geo content to enterprise-focused messaging is a strong case study for GrowthX's ability to influence product positioning through content

---

## Overview

- GrowthX to provide a Looker Studio report for tracking blog performance instead of modifying URL slugs
- Rapyd to review and provide relevance feedback on existing blog content for potential pruning/updating
- New standardized CTAs to be created for main product categories (payments, payouts, accounts, all-in-one solution)
- Process change: Rapyd to receive blog content as CSV/JSON file for easier WordPress integration

---

## Key Topics

### Blog Performance Tracking

  - Mark initially considered adding "-GX" to blog post slugs for easier tracking in GA4
  - Jakub advised against modifying URLs for SEO reasons
  - Aida proposed using Looker Studio report with manually added URLs to track GrowthX content performance
  - Team agreed to use Looker Studio approach and explore potential GA4 workarounds

### Content Optimization Strategies

  - Jakub identified opportunities to improve conversion sections at the bottom of blog posts
  - Discussed adding product-specific content to increase conversions on high-traffic pages
  - Noted overall decline in blog traffic (6-8 months), partially due to AI search results
  - Proposed refreshing high-performing articles that have seen traffic drops

### Content Relevance and Pruning

  - Mark emphasized the need to focus on content relevant to mid to enterprise-level merchants and partners
  - Jakub suggested a pruning exercise to remove irrelevant or low-performing content
  - Agreed to create a spreadsheet for Mark to review blog relevance (Yes/No/Maybe)
  - Will include traffic and conversion data to inform decision-making
  - Aim to improve crawl budget and search engine understanding of Rapyd's focus

### Standardized CTAs

  - Decision to create general CTAs for main product categories:
    1.  Payments
    2.  Payouts
    3.  Multi-currency business accounts
    4.  Rapyd's all-in-one solution
  - Nicolette assigned to draft these CTAs
  - GrowthX to integrate these into their content workflow

### Content Delivery Process

  - New process: GrowthX to deliver blog content as CSV/JSON file
  - Rapyd to implement WordPress plugin for automated blog post creation from the file
  - Aida to update Airtable with publish dates and live URLs once blogs are published

---

## Action Items

**Mark Stiltner (Rapyd)**
- Review remaining 2 blog posts in Airtable, provide feedback
- Review pruning spreadsheet and indicate yes/no/maybe relevance for each blog post

**Aida Knežević (GrowthX)**
- Add Tom to Airtable for blog management access

**Jakub Rudnik (GrowthX)**
- Explore GA4 workarounds for tracking specific page groups, report back to Mark
- Create spreadsheet for blog content pruning analysis, include traffic and conversion data

**Nicolette Mychajluk (Rapyd)**
- Create standardized CTAs (1 paragraph, H2, button) for payments, payouts, multi-currency accounts, and all-in-one solution
- Remove glossary from document, send to Kristin

**Kristin Reischel (Rapyd)**
- Send updated document (without glossary) to Aida

---

## Transcript
**Jakub Rudnik:** So yeah, it's just that's just a learning for me with going to the agency side from in-house, like in-house.

**Jakub Rudnik:** I have three projects and it's all one website.

**Jakub Rudnik:** Now I'm like, I have one project across eight, but also you all are working on different things.

**Jakub Rudnik:** I'm like, where's that at?

**Jakub Rudnik:** So just a lot of context switching.

**Aida Knežević:** I've never worked in-house.

**Aida Knežević:** I wanted to, but it was just after I got laid off from my last agency.

**Aida Knežević:** I just kind of was like, okay, let me just relax for a month as I'm looking for a new job, and then month to month three I kept getting work.

**Aida Knežević:** I was like, okay, I'll just, you know, it on the back burner.

**Aida Knežević:** I would like, at one point, it would be nice to work in-house just to see what it's like.

**Aida Knežević:** And that's all over the place too.

**Jakub Rudnik:** I'm sure it is with agencies.

**Jakub Rudnik:** Like we're going so fast because we are going so fast and that's the company culture.

**Jakub Rudnik:** I don't know if that's always how it is.

**Jakub Rudnik:** It can be very slow and sometimes in a positive way, sometimes like in the worst way, where you're like, nothing can get done.

**Jakub Rudnik:** Sometimes it's here too though, right?

**Jakub Rudnik:** Like you're like, we're ready to publish and we can't show you results until we get through things.

**Jakub Rudnik:** So, but other times it's really cool and you're like different projects and things every month quarter, like G2 for the first few years was like that was like every quarter, new project, new role, new, but I've been at very slow companies where it's not at all.

**Jakub Rudnik:** Hey, Mark.

**Jakub Rudnik:** Hi.

**Mark Stiltner:** I was sitting here typing and looked up and all of a sudden three minutes passed.

**Mark Stiltner:** So sorry about that.

**Aida Knežević:** Hi, Nicolette.

**Aida Knežević:** I haven't met you yet.

**Aida Knežević:** It's nice to meet you.

**Mark Stiltner:** Nicolette is on my team.

**Mark Stiltner:** She's going to be helping me out with reviewing blog posts, so I wanted her to join Nick and I need everybody.

**Mark Stiltner:** Yeah, that's great.

**Aida Knežević:** That was actually the first thing that I wanted to talk to you about.

**Aida Knežević:** So I saw that you were in the docs today.

**Aida Knežević:** You have some comments that took a look.

**Aida Knežević:** And I know like in the beginning, obviously, usually customers leave more comments and until we like figure out how we're supposed to talk about the product.

**Aida Knežević:** But I don't want these reviews to take up too much of your time.

**Aida Knežević:** So if you notice that there's anything that's taking up significant time during edits, let me know and we'll like try to figure out a way to like avoid that in the future.

**Aida Knežević:** Whether that's, I don't know, for some clients, was like removing external links or like adding internal links or whatever.

**Aida Knežević:** So whatever it is, you can let me know.

**Mark Stiltner:** Okay.

**Mark Stiltner:** I've reviewed two of the posts.

**Mark Stiltner:** You said five, but I saw four in there.

**Mark Stiltner:** Is there five in there?

**Mark Stiltner:** There should be five.

**Mark Stiltner:** I might have just not seen it on the little list there.

**Mark Stiltner:** I might have just not seen it on the list.

**Mark Stiltner:** And I left comments in it really more is just like an FYI for you.

**Mark Stiltner:** So, there weren't a lot of comments, things that did change.

**Mark Stiltner:** I just wanted to explain why I was changing them so that we can continue to dial things in.

**Mark Stiltner:** The second one that I'm in right now is requiring some more edits.

**Mark Stiltner:** So that one I'll probably revise.

**Mark Stiltner:** Then I might even send it off to you to take a look at.

**Mark Stiltner:** It's on the benefits of refunds versus chargebacks, which as a topic in general is like, it's really talking to merchants about like, hey, here's why you might want to do a refund as opposed to risking chargebacks or have a good refund policy in place.

**Mark Stiltner:** But it gets into some nitty-gritty details there, where I thought it deserves a bit more oversight.

**Mark Stiltner:** As I get through these, I think I'll get a better idea for like, which ones are easier to kind of sail through and what

**Mark Stiltner:** Don't you require more oversight?

**Mark Stiltner:** OK, that makes sense.

**Aida Knežević:** Yeah, yeah, let me actually show you in air table.

**Aida Knežević:** So I know sometimes you might be seeing a different view.

**Aida Knežević:** So these are there are four right now that are ready for your review.

**Aida Knežević:** So one that's what happens.

**Mark Stiltner:** I scheduled one and it went off list.

**Mark Stiltner:** So if you scroll up, it's as scheduled now.

**Mark Stiltner:** OK, yeah.

**Mark Stiltner:** Yeah.

**Mark Stiltner:** So that's it.

**Aida Knežević:** So I did add images.

**Aida Knežević:** Oh, yeah, where do I find those?

**Aida Knežević:** Yeah, there's an image column here now.

**Aida Knežević:** Yeah, so if you just scroll to, what is it, is this the right?

**Aida Knežević:** Yeah.

**Aida Knežević:** So you just have an image column right here and you can open it up and download it.

**Aida Knežević:** Then you just upload it to your blog.

**Aida Knežević:** Can I add members of my team to this air table or do you need to do it?

**Mark Stiltner:** I think you might have permission.

**Aida Knežević:** You might be able to do it, but if you can't, just shoot me an email and I'll add them.

**Mark Stiltner:** Okay, I'm actually just going to throw, okay, I tried and it didn't work, so I'm going to throw the address of one of my team members here to you if you could add him to this air table because he's the one who actually is adding these to the blog right now, his name is Tom.

**Mark Stiltner:** Okay, and it'll be helpful to just be able to have him get in there to be able to get at a tags and images and such.

**Mark Stiltner:** Okay, and there and his name is Tom, if you would add him.

**Mark Stiltner:** Okay, adding him now.

**Aida Knežević:** Okay, so yeah, we are sort of right now in the process of like publishing the first couple of articles, so nothing to report yet in terms of performance.

**Aida Knežević:** But Jacob did have some things he wanted to talk about performance wise related to your whole blog.

**Aida Knežević:** Oh great, and I have some notes for you on how we're publishing so we're doing a couple of things on our end right now.

**Mark Stiltner:** We've published two of the articles so far.

**Mark Stiltner:** We're amending your slugs slightly by putting GX at the end.

**Mark Stiltner:** So actually, if you could do that, it'd be easier.

**Mark Stiltner:** So, you know, if the blog post was chargebacks, you know, slash chargebacks, we're doing slash chargebacks dash GX.

**Mark Stiltner:** That way, when I go into Google Analytics, I can just do a search for GX and I can pull up all the blogs and look at it.

**Mark Stiltner:** I wanna make sure that doesn't screw with any SEO issues, but it was an easy way for us to pull it and track it.

**Mark Stiltner:** Think about that.

**Jakub Rudnik:** So I 100% see what you're doing in Analytics and it's a very common issue.

**Jakub Rudnik:** I've been first time really on the agency side.

**Jakub Rudnik:** I don't know how to approach it from that direction, even like by the writer or by the theme or whatever, I've like struggled with how to attribute to some sort of subsection.

**Jakub Rudnik:** Let me see. In GA4, I feel like you spent a little bit more time, but there's definitely a way we can put together a report and just add the URLs we're creating into a single report. We can build that in a way that you can report on just GrowthX content without changing the URL.

**Jakub Rudnik:** I want to explore what that is from an SEO standpoint, slightly worse.

**Jakub Rudnik:** I don't think it's that big of a deal, but it would like, I think the average user does not see your URL or the slug at all.

**Jakub Rudnik:** They just like are on the page, they're not seeing it.

**Jakub Rudnik:** I think they're just like, you're looking at fringe details.

**Jakub Rudnik:** And I've never actually seen someone make that change with something that's not related to content — just adding something to the slug like that.

**Jakub Rudnik:** So when I go to the team and see if anybody has an opinion on that, but I could see some sort of like, I don't know, it doesn't feel like it's going to be a major penalty or something.

**Jakub Rudnik:** It would just be slightly off.

**Jakub Rudnik:** practices and it's like, that's setting up like alarm bells, but it's not what I would want to do if I was running my own content program.

**Jakub Rudnik:** That makes sense.

**Jakub Rudnik:** I just wanted to see if anybody has like this be a big risk or if it's like the tiniest risk and I'm just over indexing on like, this isn't how I would do it.

**Mark Stiltner:** If you can aggregate and provide a report that just includes all those blogs in a better way, totally happy to do that.

**Mark Stiltner:** We were just on our end sitting there saying like, how do we look at all these and we just say yes.

**Aida Knežević:** Yeah, so if you remember last week, I showed you the Looker Studio report that we were going to use just for our blogs. In that report, there's a data control where I just add the URLs of all the content that we've published so far.

**Aida Knežević:** So every week when we publish content, I basically just copy them from Airtable, add them to the Looker report, and it pulls in data from Google Search Console and GA4 into that report.

**Aida Knežević:** Unfortunately, Google Analytics 4 is really horrible at setting up individual reports for groups of pages.

**Aida Knežević:** It doesn't let you do that.

**Mark Stiltner:** You can do it for a small group of pages.

**Aida Knežević:** The Regex code limits are insanely short, which is frustrating because I spent a couple of hours trying to do that for clients.

**Aida Knežević:** I hate everything about GA4.

**Mark Stiltner:** And everything that I want to do with it seems like it's difficult like that.

**Aida Knežević:** Yeah, it used to be a feature of the previous version.

**Aida Knežević:** And now it's no longer possible.

**Aida Knežević:** But it is possible if you use Looker Studio reports.

**Aida Knežević:** So I don't necessarily have to change the slug.

**Aida Knežević:** We can easily track it in Looker Studio if you want.

**Mark Stiltner:** Okay, we'll do it that way then.

**Mark Stiltner:** I'll just tell Tom not to add that at the end.

**Mark Stiltner:** I'll change it on the ones that are already published so that they line up.

**Mark Stiltner:** So your Looker report will be good to go.

**Jakub Rudnik:** Well, I think I'll check with other folks internally and then I'll send one to a friend who is much better at GA4 and see if there's any workaround we're not aware of.

**Jakub Rudnik:** To do it in GA4 so you can have that even beyond our single looker studio report as well.

**Mark Stiltner:** Okay.

**Mark Stiltner:** Yeah, if you can find me a worker on a GA4, that would be great.

**Mark Stiltner:** Just for my own benefit, I like to be able to parse things easily in there.

**Mark Stiltner:** 100%.

**Jakub Rudnik:** Yeah, I've definitely dealt with this exact issue and how to handle it in Google Analytics before, and I've just stayed away from GA4 as much as I can because it's the worst change to a tool I've ever seen.

**Jakub Rudnik:** Yeah, let me jump in here, unless you have anything else, Mark, on the Looker report.

**Jakub Rudnik:** There are two things I was trying to dig into. One is something we were talking about in the conversion section

**Jakub Rudnik:** And the discussion we had a week or two ago about the content at the bottom of the page and how we're positioning your products. Is it just the CTA? Is it some content? I've been going through old content and seeing a mix of ways that's done — sometimes just the CTA, sometimes like a form.

**Jakub Rudnik:** Sometimes you do have a full section, so we're kind of all over the board.

**Jakub Rudnik:** I just want to call this out. This is something we could consider doing either immediately or in the near to medium term. We could write those sections and use some of our workflows. If we're doing this, I know the focus is certainly on traffic to some extent, but also on conversions. We could be testing this on high traffic and high intent pages already, trying to add value to pages that are already seeing visibility.

**Jakub Rudnik:** So it's one area. I have an example here — the article just ends with "learn more" and there's nothing else. There's a CTA below, but this could be a whole section on Rapyd positioning.

**Jakub Rudnik:** For example, the article on Thailand's payment solutions. Instead of rewriting the whole article, could we add this section and just add some rich text to increase conversions where we see an opportunity already?

**Jakub Rudnik:** We can narrow this a little and increase it a little bit on the agenda, and then work the URL in as well.

**Jakub Rudnik:** So conversion sections is like something to raise up.

**Jakub Rudnik:** The other piece is noticing that blog traffic has fallen overall. I picked 6 and 8 months as some natural reference points.

**Jakub Rudnik:** But this is happening at both the universal blog level and the individual page level.

**Jakub Rudnik:** Everyone's dealing with AI search results showing up, right?

**Jakub Rudnik:** There are just fewer clicks to go around.

**Jakub Rudnik:** But it's also happening page by page.

**Jakub Rudnik:** Some pages have dropped in traffic. I wish I had saved more of these screens, but I noticed some blogs that skyrocketed for you, then kind of fell off after a few months.

**Jakub Rudnik:** I don't know how deep we've talked about this, but we could build in some refreshing of those articles — the ones Google has shown it's willing to rank you really high for.

**Jakub Rudnik:** We've had traffic before.

**Jakub Rudnik:** Should we be, whether it's adding new sections, adding internal links, stuff like that?

**Jakub Rudnik:** We can build that into the work we're doing.

**Jakub Rudnik:** It'd be a matter of allocating resources slightly differently, but we want to gauge your appetite for that. There are definitely opportunities here where there's been traction before.

**Jakub Rudnik:** So there's two things that are happening here.

**Mark Stiltner:** One reason I'm engaging you is because we've seen our SEO performance go down and I want to start bringing it back up.

**Mark Stiltner:** Interesting to hear that some of the like AI generated content, you're seeing that across the board.

**Mark Stiltner:** That's actually good to know.

**Mark Stiltner:** More than the AI overviews at the top of search.

**Mark Stiltner:** payment strategy and those kind of posts like even the ones that still are some of our best performing posts today are things on like how to generate a QR code for payments and like that's great for a small business it's actually not our audience so what we're trying to do is like grow the SEO but also shift it to a very more focused niche audience of you know kind of mid to enterprise level merchants partners and high opportunity businesses so there is definitely going to be some value in going back and improving some past posts but we're going to need to be judicious about what they are and then even the way that we that we like work out these call to actions for instance like we don't want to sell payment processing in Thailand so before like one of some of our best performing blogs are like top payment methods in Thailand top payment methods in Brazil top payment methods in China whatever like like those just have done really well for us

**Mark Stiltner:** But again, we're focusing right now on accepting credit cards only in Europe.

**Mark Stiltner:** So there's this misalignment between some of the stuff that is really strongly driving traffic and the things that we want to talk about.

**Mark Stiltner:** And so we've got to be judicious about what we go back and update, but I do want to do some of that.

**Mark Stiltner:** I think it's just we're not going to be able to choose it based on the amount of traffic that it had and what we have to choose it on also if it aligns with the current target audience.

**Mark Stiltner:** then on new stuff coming in, there's going to be blogs that we write that are kind of like casting a white mat, but where the call to action won't really be based off the content of that blog.

**Mark Stiltner:** An example of that actually like, you know, that was just written recently on like chargebacks and disputes.

**Mark Stiltner:** Payout blog, it gets our payout CTA.

**Mark Stiltner:** it's a payment blog, it gets our card acquiring CTA.

**Mark Stiltner:** it's a wallet blog, it gets our multi-currency business account CTA, and we just keep it like that simple.

**Mark Stiltner:** The CTA duplicate doesn't, yeah, it is correct.

**Jakub Rudnik:** I didn't see any issue there at all.

**Jakub Rudnik:** doing content, think it's overblown.

**Jakub Rudnik:** Having worked at G2 and seeing 90% of some of the templates are the exact same, it's just filled in with some data information from a database, and that worked.

**Jakub Rudnik:** I'm definitely, I think, I'm under index there, so I think you're fine there.

**Jakub Rudnik:** In some of these articles that are testing, it's depending on how far away from your products, some of these are.

**Jakub Rudnik:** I think it would be definitely not, for both of those strategies, wouldn't just be a one-size-fits-all.

**Jakub Rudnik:** I think if there's content that is much closer to the product, having a section that really drives home what are the challenges and then how does that relate specifically to Rapyd — that's something I'd make sure exists. And then for the traffic falloffs, those are definitely the two prongs we're looking at.

**Jakub Rudnik:** Looking at where traffic and keywords are falling — seeing if it's just content degradation over time or if other stuff has surpassed it. But also looking at conversions.

**Jakub Rudnik:** Did this piece ever generate conversions or leads? Is it really in your wheelhouse? Is this the type of topic you want to own? Do we believe it would work if you were seeing more traffic or if you had positioned yourself better in the article?

**Jakub Rudnik:** My starting point is looking at Google Search Console to see where you've dropped in traffic or keywords, and from that list, I identify the most relevant pieces.

**Jakub Rudnik:** Or what's not relevant, we can just push to the side — either the traffic is fine or not. But the last point I want to discuss is this:

**Jakub Rudnik:** If there's content you created historically that was generating traffic but it's just irrelevant traffic, or articles that never generated traffic and aren't relevant,

**Jakub Rudnik:** You should consider a pruning exercise to remove those pages. Let's use your crawl budget really wisely.

**Jakub Rudnik:** Let's really show Google and search engines what Rapyd does.

**Jakub Rudnik:** This what our publication does.

**Jakub Rudnik:** So we can remove some of that noise and clutter.

**Jakub Rudnik:** Each piece would have different criteria — does it have traffic, does it have links, and so on. But we can go through that exercise.

**Jakub Rudnik:** And I think you'll see a lift from that. When I joined an Active Campaign,

**Jakub Rudnik:** We cut 20% of the blog and saw the 25% increase in a month.

**Jakub Rudnik:** It was just so counterintuitive removing that old stuff. It could be useful to do the same as we stand up a lot of new content over the next quarter or so.

**Marc Winitz:** I think that would be really useful. My question is how big of a lift is that analysis? I think we should do it, but I'm not sure what I'm asking for exactly.

**Marc Winitz:** I have a big idea too.

**Marc Winitz:** Pulling a list of blogs is obviously simple.

**Jakub Rudnik:** It's simple, like setting up a spreadsheet where you indicate if a post is relevant or not from your end. That would really help. Just give me a yes, no, or maybe for each one, and that would be the best approach. If I get that support, I can do the analysis on the other side — stuff like whether it has traffic and backlinks. That's pretty easy once I have the relevance data. It's really just a decision tree: if this has these characteristics, what do we do next?

**Marc Winitz:** So but that's that's pretty easy once I know how Much you believe in that topic as you know, it relates to Yeah, I think there would be mark a Vector of this or a pillar of this would be just what's the relevance to us in general Regardless of performance and conversion and then at a conversion level What is it and then is the can maybe a sub of the conversion is is a conversion that turned into something relevant that we care about at a Level

**Marc Winitz:** So maybe something like that.

**Marc Winitz:** I don't know.

**Marc Winitz:** It's just sort of one way to think about it, but I think we need to which I think we should do this if we can handle it.

**Marc Winitz:** I don't know what this takes besides what Jacob described it.

**Mark Stiltner:** Yeah.

**Jakub Rudnik:** And again, I can support a lot of that and making those recommendations on the other side of like how to implement a lot of it would be this deleting slash adding redirects to a bunch of content.

**Jakub Rudnik:** So it's not that big of a lift on the other side.

**Jakub Rudnik:** I really think like if I had the the relevance information, like I can make some guesses, but you'll be a better expert there and what the product like how it's connecting.

**Jakub Rudnik:** I can make a bunch of those recommendations lot.

**Jakub Rudnik:** then we err, I think on the side of safety up front, we do it in small batches of like, this is the 5% that's just not relevant, no traffic.

**Jakub Rudnik:** We cut like, let's just do that right away.

**Jakub Rudnik:** Then we have slowly shipped over.

**Jakub Rudnik:** And so I don't think it's that big of lift from either side.

**Jakub Rudnik:** And I think that's what I'm here to support on for sure.

**Jakub Rudnik:** So I would say I need to give you two pieces of information.

**Mark Stiltner:** One is for all the blogs — yes/no/maybe relevance for a pruning exercise. The other piece is for blogs where we're driving strong results that have dropped. Do we update them or not? I think those are the two pieces of information I need to give you.

**Mark Stiltner:** Yeah, I think so.

**Jakub Rudnik:** It depends on the order — if we're focused on new publishing and refreshes, we can even pause the pruning as we work on this. Having traffic and conversion data is relevant for me in the pruning exercise, but the relevance yes/no/maybe is most important. We can build from there. I'd start with that and then add conversion and related data to supplement. If you put the spreadsheet together, I can review it.

**Mark Stiltner:** Okay, if you can get that spreadsheet together, I can go through it.

**Mark Stiltner:** It would be useful to have traffic data on there. Traffic and conversion data will give me insight because there might be some blogs where I think, "this isn't relevant," but it's getting a lot of traffic. I might take a second look to see why. And the other thing I'm always looking at is — yes, maybe not relevant, but what can we do with that traffic?

**Jakub Rudnik:** I hate to get rid of 500 visits a month. Could these people be relevant to a newsletter? Could we show them something else? I'd err on the side of caution unless it's truly irrelevant.

**Jakub Rudnik:** So we would start with those.

**Jakub Rudnik:** Yeah, I like what your brain is doing — "what's the opportunity? What might be making sense here that I didn't see on first pass?"

**Jakub Rudnik:** But yeah, there's no traffic and no conversions, or tons of traffic but no conversions.

**Jakub Rudnik:** Those are good spots to say there's something off here.

**Jakub Rudnik:** Um, okay.

**Jakub Rudnik:** I don't have conversion data. I don't think I have HubSpot access. You could pass that along — I assume you have GA4 or HubSpot access?

**Mark Stiltner:** Okay, I can get conversion data. Yeah, whatever you're looking for — obviously traffic. In GA4, on the events tab, if you're looking at traffic reports for pages on rapyd.net, there's a tab called "Key Events."

**Mark Stiltner:** That's the data we want. There are two things — "Event count, all events," and then "Key Events."

**Mark Stiltner:** It's that key events column that we want to look at.

**Mark Stiltner:** What is the key event that you are tracking for these blogs?

**Aida Knežević:** There are a few in there.

**Mark Stiltner:** The easiest key event to track is "form submit," which is one of the options. But GA4 breaks it out, and that doesn't always capture everything because of how our GA4 is set up.

**Mark Stiltner:** So I track account created, global contact us form submission, any other form submission, gated contact submission, client portal submission, and people who viewed the contact us form but didn't complete it.

**Mark Stiltner:** So all of those together give me an idea of somebody did this blog and then took an extra step to interact with Rapid.

**Mark Stiltner:** So in aggregate, I use that whole key event column as my conversion high-level number.

**Jakub Rudnik:** Yeah, that makes sense.

**Jakub Rudnik:** Alright, I'll set up that spreadsheet and show you the information. I'll build that column of yes/no/maybe relevance and then we can iterate on it. We can supplement it later and build it together. This exercise should be pretty quick for you on the first pass. We can have a big "maybe" bucket, and if we're doing this in batches, let's cut the most obvious candidates and then work from there. It can be simple on your first pass.

**Mark Stiltner:** I like yes/no/maybe. That's a good idea.

**Mark Stiltner:** Back to something else we discussed and then got off the topic of — CTAs.

**Mark Stiltner:** And Nicolette, thank you for being on the call.

**Mark Stiltner:** If I assigned you to create a general CTA for each of our top-level blog topics, could you put that together? I'm thinking Jakub, this would be like a one-paragraph H2 banner with a button — right?

**Mark Stiltner:** Yeah I think that's far right at the highest level.

**Jakub Rudnik:** So kind of like what we do for the pink box now Nicolette.

**Mark Stiltner:** But can you create a standardized CTA for.

**Mark Stiltner:** Let me just make sure that we want to do it for every one of those topics real quick here.

**Mark Stiltner:** There are one, two, four, five, six, eight, nine, ten.

**Mark Stiltner:** Actually, I wouldn't do it for all the topics.

**Mark Stiltner:** I would only do it for the product-focused topics.

**Mark Stiltner:** So basically, we need one for payments.

**Mark Stiltner:** need one for payouts.

**Mark Stiltner:** We need one for multi-currency business accounts, and probably one for just like Rapids all-in-one solution.

**Mark Stiltner:** I think really that would cover it.

**Mark Stiltner:** Sweet.

**Mark Stiltner:** Kristen, real quick, actually, can I get your pulse on that?

**Kristin Reischel:** If we're doing kind of more general CTAs that we could put on blogs, it would be...

**Mark Stiltner:** one for payments, one for payouts, one for accounts, and maybe one for like just into in payment solutions.

**Kristin Reischel:** Sure.

**Kristin Reischel:** Yeah, I mean, I guess, yeah, I mean, I think that sounds fine, but if you want to run those past me, is that what you're making?

**Kristin Reischel:** Yeah, I'm just making sure that we don't need to get more granular than that.

**Mark Stiltner:** Like, for instance, I feel like the blogs are general enough that if we try to do a CTA for global payments API and another CTA for hosted checkout and another CTA for developer toolkit, then we get so granular they'd end up not getting used in a lot of blogs.

**Mark Stiltner:** Yeah, yeah.

**Kristin Reischel:** No, I think it's okay to keep that high level and tie it back to the you know, the topic somehow, our product and the topic, right?

**Mark Stiltner:** And then Jacob, I think that would be actually the task on your end is taking those generic ones that we have and working into the workflow so that it kind of integrates with the topic.

**Mark Stiltner:** Yeah, that's right.

**Jakub Rudnik:** I like this approach.

**Jakub Rudnik:** This is like uplevel the conversion right away and then can be tested and iterated upon as you dig in, but the universal cycle a good first step.

**Jakub Rudnik:** Okay.

**Jakub Rudnik:** I heads up for you guys.

**Mark Stiltner:** I did talk to your IT guys and I also talked to our IT or dev team this morning.

**Mark Stiltner:** Looks like what as like a CSV file or a JSON file or something like that that's mapped to our blog and then we would have a plug-in and WordPress on our end where we just put that file into it and it would digest it and turn into a blog post.

**Mark Stiltner:** So it would automate it on our end and your deliverable would be that CSV or JSON file.

**Mark Stiltner:** That was the recommendation that keeps Ada, you from having to manually create the blogs.

**Mark Stiltner:** So it still becomes like a programmatic process.

**Mark Stiltner:** Oh, yeah.

**Mark Stiltner:** I would just take out the glossary.

**Nicolette Mychajluk:** Yeah, they'll be having to take out the glossary.

**Nicolette Mychajluk:** We're working on that.

**Kristin Reischel:** Yeah.

**Kristin Reischel:** So, Nicholas, take out the glossary and shoot it to me and I'll send it over to Ada today.

**Mark Stiltner:** Wonderful.

**Nicolette Mychajluk:** And if you could make a copy because my team's actively, yeah, we have a separate one in the template.

**Nicolette Mychajluk:** Thank you.

**Nicolette Mychajluk:** Okay, so that covers that.

**Mark Stiltner:** In terms of process, I think normally you guys schedule the blogs that I've been tagging them as scheduled when I send them off to Tom to publish and with this process with the CSV file, I just had to talk real quick about like what's the proper way to indicate that this has been published or whatever?

**Mark Stiltner:** Should I change that and?

**Aida Knežević:** Yeah, yeah, this is a this is a novel one because usually we're doing the publishing, but you can feel free to change the status.

**Aida Knežević:** The one thing that I do recommend is you either let me

**Aida Knežević:** or somebody on the team, I think, Tom, he can let me know when you've published the blogs, and then I add them right here, so to the publish date, and then I'll remove these URLs.

**Mark Stiltner:** These are just the top competitors.

**Aida Knežević:** So you just add the publish date here and the URL for the blog, for the live blog right here, and that's it.

**Aida Knežević:** Great.

**Mark Stiltner:** Okay, anything else?

**Aida Knežević:** Mark, Kristin?

**Aida Knežević:** All right, great.

**Aida Knežević:** Thank you.

**Aida Knežević:** Okay, great.

**Aida Knežević:** I'm looking forward to the product docs.

**Aida Knežević:** I did incorporate some of the POV stuff that we were talking about last week into this week's blogs, that's going to get a whole lot sharper once we have all of the input from your end.

**Aida Knežević:** Okay, thank you so much for your time.

**Aida Knežević:** We'll chat on Slack and see you next week.

**Aida Knežević:** Alright, thank you.
