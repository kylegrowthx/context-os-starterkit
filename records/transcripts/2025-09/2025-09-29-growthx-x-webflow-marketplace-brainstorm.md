# GrowthX x Webflow — Marketplace Brainstorm

<metadata>
date: 2025-09-29
time: 16:30 UTC
duration: 43 minutes
organizer: Tyler Pavlas
participants: Tyler Pavlas, Marcel Santilli, Rachel Wolan, Kirat Chhina
fathom_recording_id: 90505743
fathom_url: https://fathom.video/calls/423531818
share_url: https://fathom.video/share/MJJeVktFQzaCQ7Qsw85E6FodZtSN8Sci
source: fathom
enriched_on: 2025-03-03 16:45 UTC
</metadata>

---

## Summary

GrowthX and Webflow discussed a major opportunity to build an SEO-friendly, curated marketplace for CodeGen-generated templates, combining the best practices from Notion, Dribbble, and Mobin. Marcel presented a vision for an enriched template library with easy search, remixing, and comprehensive metadata that freelancers and agencies can leverage. Webflow's marketplace is currently a mixed collection of coded and Webflow-native elements, but the CodeGen launch in October creates an opportunity to establish a high-quality showcase with proper discovery and the ability to support future user-generated content. The team agreed on an 8-week strategy sprint involving deep dives with product teams to understand CodeGen capabilities, API access, and how to bridge Webflow and static-code stacks.

---

## Context

GrowthX is conducting a marketplace advisory engagement with Webflow around two key initiatives: optimizing the marketplace as Webflow launches its CodeGen product in October, and exploring how GrowthX's content and marketplace expertise can help structure a high-quality template discovery and remixing experience. Webflow's current marketplace is a hybrid of Webflow-native elements and coded content, making it difficult for users to discover, understand, and reuse templates. Kirat Chhina leads the marketplace PM effort at Webflow, while Rachel Wolan owns business alignment and budget. Marcel is pitching this work as an 8-week strategy sprint. The conversation draws on GrowthX's recent work with Lovable and other builder platforms, using those case studies to frame what success looks like: searchable, well-categorized, high-quality starter kits that serve freelancers and agencies looking to integrate with backend systems (CRMs, payment processors, etc.) rather than pure AI-generated UI components.

---

## Relevance

**To GrowthX Delivery:**
- Validates the marketplace template strategy as a repeatable offering (following Lovable, Bolt, and internal content work)
- Highlights the importance of SEO-friendly taxonomy and metadata architecture — lessons GrowthX can package for other platforms
- Establishes that end-to-end engagement (design, strategy, taxonomy, implementation) is more successful than piecemeal consulting

**To CheckThat:**
- SEO-friendliness of marketplaces is a core discovery problem: templates, galleries, and content libraries often miss indexing opportunities (V0, Lovable, Airtable all have poor SEO)
- Webflow's scale (potential for thousands of templates) makes this a visible test case for search visibility of AI-generated and user-generated content

**To GrowthX Business Development:**
- Webflow is a strategic partnership opportunity: they're aware of competitive threats from Lovable (database connections, CMS lite) and see value in expert-guided marketplace strategy
- Rachel Wolan flagged willingness to review budget with CFO, indicating serious intent
- Phased approach (8-week sprint followed by implementation) creates natural expansion opportunities
- Potential to establish a reference case with a major platform (good for sales and credibility)

---

## Overview

- GrowthX proposes building a SEO-friendly, curated marketplace for Webflow's CodeGen product launching in October, inspired by Notion's template model
- Current marketplace is "a mess" of mixed Webflow and coded elements; opportunity to establish clean, discoverable taxonomy focused on freelancers and agencies
- Key challenges: CodeGen API access for automation, bridging Webflow's internal language with static code stacks, and respecting community promises around template usage
- GrowthX recommends an 8-week strategy sprint for product deep-dives, followed by phased implementation starting with static websites, then translated to Webflow-ready templates
- Competitive urgency: Lovable's upcoming database and AI service connections pose a threat unless Webflow accelerates similar integrations

---

## Key Topics

### GrowthX's Marketplace Vision

- Inspired by successful models: Mobin (UI element search), Dribbble (design discoverability), Notion (curated + user-generated at scale)
- Focus on three core capabilities: easy navigation with rich filtering, ability to preview and fork/remix templates, comprehensive taxonomy and descriptions
- Aim to create SEO-friendly pages for each template so searches like "construction website with modern style" land on relevant starter kits (addressing V0 and Lovable's current indexing failures)
- Start with high-quality, company-curated templates to establish quality baseline, then layer user-generated content following Notion's model
- Comprehensive prompts and source code explanations enable users to understand and replicate designs, or vibe-code variations

### Webflow's Current Situation and Goals

- Marketplace is fragmented: part built on Webflow, part coded — making it hard to maintain brand consistency or quality standards
- Launching private beta of CodeGen product in October — a critical moment to establish best practices before user adoption
- Target audience: freelancers and agencies building production websites, not hobbyists making hobby projects
- Key requirement: templates must support practical integrations (CRM connectors, payment systems, applicant tracking) so creators can differentiate their offers
- Opportunity to refresh marketplace search and discoverability as part of CodeGen launch

### Technical Challenges and Considerations

- Stack mismatch: Webflow templates use Webflow's internal language, which doesn't translate cleanly to HTML/CSS; CodeGen prefers Tailwind
- No current API access to CodeGen limits automation possibilities for enrichment and template generation
- Hosted approach vs. subdirectory approach: how to host thousands of templates without fragmenting the product
- Database-driven architecture likely better than CMS for maintaining consistency and enabling search features
- Phased approach: start with static websites (easier to enrich and SEO), later translate to Webflow-ready templates once stack questions are resolved

### Proposed Strategy and Next Steps

- 8-week strategy sprint led by GrowthX to deep-dive with Webflow's CodeGen PM and marketplace PM
- Discover CodeGen API capabilities and database access for GrowthX enrichment systems
- Develop taxonomy, categorization framework, and content strategy before October launch
- Define quality bar and curation process to differentiate from competitors' user-generated chaos
- Plan phased rollout: begin with static sites, then build translation layer to Webflow collections if needed
- Establish community guidelines and template contribution process

### Market Positioning and Competition

- Lovable's upcoming database and CMS-lite features seen as potential threat to Webflow's appeal
- Wix and Webflow both have strong marketplace models; opportunity for Webflow to establish CodeGen as the premium option
- Risk: if Lovable ships one-click database connections and Webflow doesn't match that capability, CodeGen loses a key selling point
- Webflow's maturity and technical sophistication are advantages — better positioned than Lovable or Bolt to execute a sophisticated marketplace

---

## Action Items

**Kirat Chhina (Webflow)**
- Contact CodeGen PM and marketplace PM; discuss API availability and database access needed for GrowthX enrichment systems
- Schedule deep-dive meeting with Marcel's team, CodeGen PM, and marketplace PM to align on CodeGen capabilities and technical constraints

**Rachel Wolan (Webflow)**
- Review budget for GrowthX 8-week strategy sprint proposal and prepare for CFO discussion to secure approval

---

## Transcript

**Tyler Pavlas:** Can you hear me okay?

**Tyler Pavlas:** Yeah, you sound good.

**Tyler Pavlas:** Say a little more.

**Tyler Pavlas:** A little fuzzy, a little fuzzy.

**Tyler Pavlas:** Getting worse.

**Marcel Santilli:** Getting worse about now.

**Tyler Pavlas:** Getting better.

**Tyler Pavlas:** Getting better.

**Marcel Santilli:** Getting better.

**Marcel Santilli:** I have these headphones on on a coffee shop, but these headphones are not really good for...

**Marcel Santilli:** Let me try a couple other things.

**Tyler Pavlas:** It's pretty good now.

**Tyler Pavlas:** Is it better this way?

**Tyler Pavlas:** Oh, way better, way better.

**Marcel Santilli:** Okay, cool.

**Marcel Santilli:** All right.

**Tyler Pavlas:** Well, there's just some background noise.

**Marcel Santilli:** All right.

**Marcel Santilli:** Yeah, these headphones are kind of weird because they...

**Marcel Santilli:** So I'm going to actually just put the speakers on one second.

**Tyler Pavlas:** Some audio difficulties, but we're working them out.

**Rachel Wolan:** How's it going?

**Tyler Pavlas:** How's it going, Rachel?

**Rachel Wolan:** How are you doing, Tyler?

**Tyler Pavlas:** Great to see I'm doing great. I'm the founding AE here at GrowthX, so I work hand-in-hand with Marcel on quite a bit.

**Marcel Santilli:** How's it going? Happy Monday.

**Rachel Wolan:** Yeah, happy birthday, man.

**Marcel Santilli:** You guys did something fun?

**Rachel Wolan:** What's that?

**Rachel Wolan:** Did you do something fun?

**Marcel Santilli:** Yeah, we went to Hillsburg. It was really nice. So we got an Airbnb, and it had a nice pool in the backyard. Nice. I've and I ate steaks for six meals in a row.

**Rachel Wolan:** That is so Brazilian.

**Marcel Santilli:** They have this butcher called Journeyman in Hiltzburg, and you go and you pick, like, any wagyu steak, and they'll make it, like, right there on the, like, brick oven, and it's, like, that's so good.

**Rachel Wolan:** Their bacon is, like, on top of that.

**Marcel Santilli:** Yeah, I even have a t-shirt from them. That's how much I love them.

**Rachel Wolan:** Amazing. So, hey, I know we only have 30 minutes or even less than that. So, shall we jump in? I feel like maybe everybody's up to date on what we're trying to accomplish here. Maybe you want to do, like, quick recap?

**Marcel Santilli:** Yeah. So, I think what I kind of read is all the examples you all sent are things we're super familiar with, because either we built it or we advise or we study, but I guess like maybe one place to help like kind of just understand like in a perfect case scenario, like where do we plug in and how do we plug in, right? Like, and what I mean by that is like, I think for instance, like with Lovable right now, they're kind of like take it end to end because all these teams got stuck, right? So they want us to do like the design, the implementation, the workflows, the strategy, like end to end. And then with like Bubble, for example, it's more of like, no, no, we already have sections on the site. Like we're going to be very selective where we want you to plug in. Like with Bolt, was more like give us the strategy, you know, and to help us think about like the different categories, the filters, like how we should approach this. So maybe that would be super helpful as like in an ideal case scenario, like the role you think would be ideal for us to help you.

**Kirat Chhina:** Yeah. So, Marcel, would be useful to understand what you're driving for Lovable in terms of what properties you're owning. So, I think probably end-to-end would be better, maybe a better approach. Because, I mean, in the existing project, you guys have executed kind of faster. I mean, there have been ups and downs. There have been kind of, but getting our brand team to support launching some of the Webflow properties has also been hard. So, what would be useful is if we kind of work backwards from, hey, this is possible. This is what we pulled off for Lovable. Well, okay, what pieces of this do you want? And I think the only concern one piece for us would be around. How does it fit into our marketplace and what bandwidth do we have need to kind of add in there, but, but yeah, so, so welcome back.

**Marcel Santilli:** That's super helpful. Okay. So let me share my screen at a high level just to kind of show you this. Okay. Can you see this? Yeah. Okay. Cool. Okay. So this is only a very early on prototype, but the whole idea is like the inspiration here is Mobin and Dribbble in some ways. And so what we proposed to them was like, Hey, how do you create kind of a easy to navigate library that then allows people to just like gain inspiration, but also be able to like fork and remix anything really quickly. Right. And so the idea is like a lot of their competitors, including like both and others, like we'll have like galleries, if you will, but the process to remix is either not there or it's really hard to search. Right. Like, so, you know, I'm a heavy V0 user, like you go in here and, and like you click on browse all one, it's not SEO friendly. So it's like actually not getting indexed the way it should, but for you to say like, Hey, I want to find, let's just say like a grid, like the, like, it's just like, you're not finding like all the right things you want, you know, but there, I think catching onto it and improving over time. And so those are the things that we're trying to kind of make it a lot easier. then the experience, ideally, it's more like if you're on Dribbble or Behance or any of those experiences, right? Like where there's both like ways to filter and navigate, but I'll. So if you search for things like, let's say, like a construction website with modern style, right? Like you will land on things like that, right? Which is what Wix did. I think you all did a good job with that as well. But also Wix probably did some of the better job with it of like ranking for all the different like terminology that you can possibly rank for across like websites or apps. In lovable cases, also like internal apps. So they're in landing pages, websites, as well as like overall apps, you know, like categories. And so then the idea is once you land on the page, it makes it super easy for you to preview and then remix. Again, it's just a prototype. But then also add all this taxonomy and description around what it is, you know. I know with Made in Webflow, there's like features, for example. So kind of like similar to that. But, but, but. Also, like, things that are essentially the idea here is like looking at the repo of the source code and then analyzing that repo and understanding like all the things that are built in there, right? Like, and then the last part is also like making it easier for someone that wants to replicate how to achieve the same results. And so in this case, like, we also write like the super comprehensive prompt and so that people can kind of learn like the thought process of if they wanted to kind of vibe code this themselves, you know, from scratch. And then later on, be able to show things from the community or related projects and things like that, right? So that's what we're doing for them. And then for Bolt, what we did was kind of these starter kits, right? And so these starter kits were like very much kind of similar in some ways where you could preview this one-shot app that we built programmatically using their APIs. And so this is like one-shot app built using our prompt, and then here's like explaining how the prompt worked and the actual prompt, as well as like one click to then fork this in Bolt, and then we also gave them like all the categories for them to use, and so if you look over here, like we gave them this design, as well as like all these categories for them to use, based on research and where the opportunities are. But then the direction they ended up taking this was 100% user-generated, which is not what we recommended. What we recommended for them was like start with starter kits, and then later on people can kind of layer the user-generated stuff, because there's just so much garbage in the user-generated. Then the other thing they also didn't do is the ability to fork it. So then this is kind of useless, because it's like, okay, this is beautiful, but I can't replicate this, and I don't even know how to replicate this. And then the description was really garbage, because it's used in general. So it didn't tackle the pain points that we were trying to solve for, if that makes sense. And so we know there's a massive need where people want to be able to duplicate things or start from a better place. And so the other inspiration is Notion templates. If you think about the Notion templates as well, I think what they've done a really good job is both the ability to search really, so all the templates are really well described and categorized, ability to navigate in almost like collections, if you will. But also they started with a lot of like Notion created templates, but then later on, they were able to kind of layer in a curated set of like builders, you know, or creators that are, you know, you can see here there's 15,000 creators. So that's kind of the idea. Think Notion is one of the only ones that are able to do it. Whereas like companies like Airtable real. F'd it up, in my opinion, because they created this templates thing here, right? And it's cool, it's okay, but none of them are, like, you can tell it's done by someone that is not really in the weeds, right? Like, so they're too basic, almost. And then they never join with, like, the, what is it called, universe, I think. They never join with this. So then they had completely separate environments, right, like, for user-generated versus Airtable-generated templates, and they never brought it together in any way, whereas, like, Notion was able to kind of bring it all together. And where, and so the idea is, like, trying to create a strategy that starts with company-generated, highly curated, like, really high-quality, well-described, right, so that it ranks well, and then, but then use that scaffolding to be able to pull in user-generated. But even if it lives somewhere else, if we can pull it in, then I think that's where, like, you can really turn this into a model, you know, better. So I don't know if that helps give the context, but again, like it can be completely different for Webflow. This is just like what we've recommended for different customers, essentially, you know.

**Kirat Chhina:** Yeah, no, this helps a lot. And for example, Lovable has their community right now where you can go to lovable.com slash community. I'm just curious, how will this fit with that? Will the community be ported over to use this and use all the richer tags? So the community at the top? Yeah, like the community piece right now. I think it's the gallery, my brand.

**Marcel Santilli:** Yeah, yeah. Yeah, so they have these kind of templates, right? And then from the community here, but it's the same thing. The challenge is, like, if you click on any of these. Once, one, it's not indexable, which is a huge mistake that they're all making right now, right? two, it's described only based on whatever your slug is, which is horrible, right? And so even if you open the project, like, this is just not a good experience. This is more like a preview. And what they got right is that you can remix pretty easily, which is great. But, like, you don't understand, like, what this is or what is actually built here, right? Like, so essentially what we're doing is building a version of this that allows you to actually understand what's built and describe it in a way that's SEO-friendly as well and categorize and tag in a way that's easy for people to discover. And then later on, these starter kits, like, you can actually pull in these projects from that same experience, right? Like, so if you look at something like this, later on, you can bring in, like, user-generated content as well. So it's kind of similar to how Notion did it, where at first, it was very happy on Notion, so then Notion is kind of like one of the users, if you will, right? But then the way they approach this is very much curated, so they don't just throw all the templates at you, they kind of curate the experience quite heavily, you know? And so that's kind of the idea, because one of the challenges is like, okay, here's a site that was vibe-coded, I don't know if this is actually well-built, so why would you want to push this to users to use it as a starting point if it's poorly built, you know? And so the idea is like kind of accelerating people's like path to actually forking something that's more of like a starter kit is kind of the idea there.

**Kirat Chhina:** And the last one is, in terms of if Lovable ends up using this, this, I'm guessing this is a completely coded experience. So how are you kind of making sure that it's the same stack? Are you folks working on their code? Is it being hosted separately and being pointed to? Just kind of curious, just trying to map it back to the way our marketplace is designed.

**Marcel Santilli:** Honestly, it's a mess. All these companies are a mess. Like, if you go in each section here, and this is public information, so you can just check it out, but it's like all of these are run completely different. They barely have a CMS. They barely have a website. Like, they're all in different stacks. So, like, if you go to this, all of these experiences, like, they're clearly completely different. Like, and so right now, they're kind of went probably too much in the move fast and don't worry about it, you know, and so part of their ask is for us to do something that feels a little bit more like this site that we built, right, like, which is kind of like more consistent experience as well. But they're, they're not super. I guess one way to think about it is they're asking for help, but they don't want to necessarily slow things down and say, hey, use this stack or that stack, because there hasn't been a standard way to do it either. You know, so in some ways they know that it's an issue, but I think, like, the ideal scenario for Webflow, I think, is, like, if it can live in a subdirectory, and because of the amount of pages this could potentially be, I think the way we've done it before with, like, Code Library and others is, like, connect this to a database, right? Like, so we can work with any database, and so, like, if you look at something like this, for example, like, every, all the data here is stored in the database, as opposed to a CMS, right? Like, but obviously we have all the integrations with Webflow, too, so if we wanted to turn this into collections, or whatever, like, we're pretty, pretty flexible. And so it kind of, you know, we're flexible because I think you all are way more mature than these other companies. These other companies are kind of, like, hacked their way there a little bit, you know.

**Kirat Chhina:** Yeah, yeah.

**Rachel Wolan:** No, go ahead, Kirat.

**Kirat Chhina:** Oh, no. So I think, yeah, we are actually, when it comes to the marketplace, we are in a similar place. Like, these companies, like, part of it's built on Webflow, part of it's coded, so it's kind of a mess. Our marketplace is also fairly a mess. And we are right now kind of migrating it and trying to build a new search on top. And I think, Marcel, in terms of what you've shared, a lot of this is very relevant to us, both in terms of creating and seeding a marketplace and then getting creators to build on top and then sharing on top. I think the one additional insight is we are not targeting complete vibe coders. We want our freelancers and agencies to get benefit out of that. And so freelancers and agencies look for specific integrations when it comes to some of these apps rather than, you know, a chess game or some kind of a Mario game. That's not what they're selling on. That might look cool, but they want to integrate with a recruiter system or applicant system on the background or some stuff like that. Interesting. Yeah. So just sharing out loud.

**Marcel Santilli:** Yeah. I think the main thing is, like, here's what we are pretty good at that we can do, right? Like, we can take, we have deep researchers and so we can enrich any page. We can come up with any. And we can programmatize almost anything. I think the part that's unclear to me right now is just, like, are we trying to take a bunch of user-generated, you know, templates, which are marketplace templates, which they're high quality, which is different from everybody else, because, like, everybody else has a bunch of truly user-generated stuff that's just, like, not a marketplace level of quality, right? Like, where's marketplace, there's a level of quality, because they're trying to sell it eventually, right? Or build reputation, right? And then enrich these pages further, and then pull it? Or is the goal more to use a programmatic, like, API or something to be able to, like, auto-generate these templates or something else?

**Kirat Chhina:** Yeah, our goal and intent is the second one. So, we have launched, or we will be launching, the private beta of our CodeGen product. Yeah. What we want to do is we want the ability to have, we need some kind of, you know, showcase. That showcase hopefully over time will be remixable or can be cloned. And then that showcase will be contributed to by the folks who are creating on Webflow. So those are the three things. And the first part of the showcase, again, this is very, very early because right now we are in the build. And it will go, we just announced it, it will go live sometime in October. The first part would be, should be more from a lens of what would be useful to our freelancers and agencies. Going back to some of the Notion templates that you showed, which is it's been created by Notion and it's solving for a particular use case. So it could be, hey, payments is a use case, XYZ is a use case, et cetera, et cetera. And so you can have some of those. Those categorizations there. So that's where we are right now in terms of thinking about it, yeah.

**Marcel Santilli:** Yeah, so maybe Mobin is probably the best example here where it's like, you can do it by screens or sort by UI element or flows. And so it makes it a lot easier. And this is mostly for inspiration, right? Like, whereas in this case can be more like a starter kit that kind of ability to fork, right? I think the, what I do know is that there's like a massive amount of like volume in just like things like templates. Like for instance, it's just a difficulty level, easy or average. So I think the idea is like you could have a really high taxonomy that makes it easy to discover. And then as far as Lovable and that community, like I think ultimately you want to understand like how the community is growing and what are the best performing ones, because I think if you're not looking at analytics on top, then you don't really know what people want, right? But I think the idea is like, it's super important that you're not going to manage all of that, right? Like, I mean, I think part of what GrowthX would be doing is basically being like a thought partner or a strategy partner for you all. So I think what would be useful is for me to see what the budget looks like soon. So I can go and run it past our CFO so that, you know. But yes, I think what would be useful is getting on a call with both the CodeGen PM and the marketplace PM just to kind of understand what we're working with technically and then kind of confirm, like, what would be the most efficient way for us to help you all. I think it's also really important to understand, like, you know, I mentioned to Rachel last week that I think are the biggest pain points right now is the fact that like people are vibe coding all these things, but today like lovable launch, lovable cloud, that's going to make like connecting to databases like insanely easy and even connecting to AI services. So I think that's more of a threat to Webflow than anything else because one of the main points is people are building all these things, but then there's no one button to connect to a CMS, right? And so one button to connect to a database, it's like the next best thing, but I think eventually my guess is like this is not proprietary information that anyone has given us, just like my personal opinion, like is that eventually they're going to do it, right? They're either going to do a CMS Lite and then like that just is like could be a huge threat, I think, to Webflow, you know, especially, whereas like if you all can do that ahead of everything else, like they're all built the same way. There's nothing that special about like, honestly, like about Lovable and Volts and, you know, Wraplet is a little different, but it's like, you know, they're all built on kind of the similar engines and Cloud Code can do a much better job than Lovable on building things, you know? So it's like, so, so anyways, I hope that's helpful, but we would love to help Webflow in, you know. Cool. Yeah. Marsha, we can follow back with times with your team, and I can get these folks on a call to kind of move forward, yeah. Sounds good. I'm going to go jump. We're meeting with Guy on the workshop, so I'll talk to you all in a little bit. That sounds good. All right. Thanks, guys.

