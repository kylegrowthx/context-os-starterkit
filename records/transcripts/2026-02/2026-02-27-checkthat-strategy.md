# CheckThat Strategy

<metadata>
date: 2026-02-27
time: 17:30 UTC
duration: 60 minutes
organizer: daniel@growthxlabs.com
participants: Marcel Santilli (GrowthX, CEO), Anna Baird (GrowthX, CCO), Ella Dillon (GrowthX, Strategy/Delivery), Stevie Kim (GrowthX, Product/Admin), Jason Gong (GrowthX, Sales), Daniel Lopes (GrowthX, CTO/Co-founder)
fireflies_id: 01KHY43R7XYJ2FD179XYFRTEZN
transcript_url: https://app.fireflies.ai/view/01KHY43R7XYJ2FD179XYFRTEZN
keywords: CheckThat, ContentOS, sales enablement, workspace setup, data analytics, Clickhouse migration
source: fireflies
enriched_on: 2026-03-03 12:00 UTC
</metadata>

---

## Summary

GrowthX leadership decided to pause active selling of CheckThat and reposition it as a free lead generator feeding into ContentOS, the company's core revenue product. The key technical blocker — migrating from DuckDB to Clickhouse — is estimated at two weeks and will unlock the filtering and data-slicing features the team needs. The group committed to a unified enablement session by Monday, with Ella Dillon delivering a prioritized list of team pain points by end of day and Stevie Kim creating a comprehensive onboarding Loom.

---

## Context

This was an internal GrowthX strategy meeting convened to align leadership on CheckThat's product direction after weeks of internal confusion. CheckThat is GrowthX's AI visibility and open index product that tracks brand citations across AI responses. The meeting was organized by Daniel Lopes (CTO) and expanded by Marcel Santilli (CEO) to include Anna Baird (CCO), Ella Dillon (strategy/delivery lead), Stevie Kim (product/admin), and Jason Gong (sales). Anna and Ella had been escalating concerns from the sales and delivery teams that CheckThat was too complex to sell or use effectively, with engagement managers reverting to the legacy tool Scrunch.

The meeting followed a week where Anna formally pulled CheckThat from the active sales invoice and instructed the sales team to stop demoing it. The core tension: CheckThat has strong underlying data and unique AI visibility metrics, but the UI lacks filters and easy analysis, the setup process is too manual for salespeople, and conflicting internal documentation has created chaos across teams. ContentOS — GrowthX's content strategy platform and primary revenue driver — remained the top engineering priority, making CheckThat resource allocation a sensitive tradeoff.

---

## Relevance

**To CheckThat Product**
- CheckThat is paused as a standalone sales item — repositioned as a free lead generation and data collection tool supporting ContentOS
- DuckDB-to-Clickhouse migration is the critical technical unblock; Jacopo validated Clickhouse on the OS side with data matching Google Analytics perfectly; Jose will execute the CheckThat migration over ~2 weeks
- Automated tagging, grouping, and taxonomy features (built by Daniel last week) are nearly ready to ship and will eliminate manual workspace setup friction
- Admin panel needs more granular role-based permissions before sprint teams can get full access — ticket exists but not yet prioritized
- Marcel demonstrated a 3-minute workspace setup for Flodesk during a live sales call (Flodesk at 3% AI visibility vs. MailerLite at 37.7%), proving the tool's value when operated by an expert

**To ContentOS**
- ContentOS remains the undisputed top engineering priority — Anna explicitly offered to sacrifice CheckThat resources if needed
- CheckThat workspace setup shortcuts the ContentOS workspace setup by pre-populating competitor data, categories, and market context
- The two products share infrastructure: features Daniel built for CheckThat (tagging, grouping) are also being deployed in ContentOS

**To GrowthX Sales & Business Development**
- Sales team instructed to stop demoing or invoicing CheckThat until enablement is complete — focus all selling energy on ContentOS
- Tyler and Nigel identified as the test cases for CheckThat enablement; if they can use it easily, the broader sales team can be trained
- Jason Gong sees a major opportunity to use CheckThat snapshots for director-level outbound lead gen, replacing expensive dinner-based pipeline generation
- Profound's Series C announcement is creating competitive pressure — prospects are asking about Profound, making strong ContentOS positioning urgent
- Nigel moved from CheckThat sales to broader GrowthX services selling

**To GrowthX Delivery/Sprint Teams**
- Sprint engagement managers are currently confused about whether to use CheckThat or Scrunch — some are reverting to Scrunch
- Ella will deliver a prioritized list of team pain points, feature asks, and positioning clarifications by end of day Friday
- Monday targeted for an all-EM enablement meeting; Marcel wants his weekly sprint call expanded to include all EMs to reduce knowledge silos (Carly's team disconnected from William's learnings)

---

## Decisions & Commitments

**Decisions Made**
- Pause active selling of CheckThat — remove from invoices, stop demoing to prospects until enablement is complete
- Reposition CheckThat as a free lead generator feeding into ContentOS rather than a standalone paid product
- Do not push customers to self-serve in CheckThat; instead, GrowthX team delivers conclusions and insights from the data
- CheckThat remains part of the strategy sprint process as a data collection and workspace setup tool for ContentOS
- Customers who already have access can keep it (public beta), but team should frame it as "our tool for understanding your space" rather than a product they need to operate
- ContentOS is the top priority — if engineering resources conflict, CheckThat gives way

**Commitments**
- Ella Dillon: deliver prioritized list of team pain points, feature asks, and positioning clarifications by end of day Friday
- Daniel Lopes: get Jose and Jacopo collaborating on Clickhouse migration; ship automated tagging/grouping features
- Stevie Kim: create comprehensive enablement Loom tying together workspace creation, caveats, and FAQ
- Anna Baird: coordinate sales asset creation (short videos, case studies, updated sales deck); schedule cross-team enablement session
- Marcel Santilli: continue MVP for advanced data slicing; expand weekly sprint call to all EMs; prepare enablement materials
- Bridget (via Ella): placeholder for Monday all-EM enablement meeting already created
- Tyler and Nigel to be used as test cases for CheckThat enablement validation

---

## Open Questions

- Should customers currently using CheckThat in sprint have their direct access restricted, or just reframed? Ella noted customers "want to play" and if told no, they request Scrunch seats instead — no firm resolution reached
- When Clickhouse migration is complete and filters ship, does CheckThat go back on the sales invoice as an add-on or stay permanently free?
- How should engagement managers handle existing customer requests for Scrunch seats in the interim — approve them or push CheckThat usage?
- Admin panel granular permissions ticket: when will it be prioritized relative to ContentOS work?
- What specific "three things" should the sales loom video highlight to create FOMO without requiring live setup?
- Can the all-EM enablement meeting actually happen Monday, or does it need to wait a week (Ella flagged dependency on readiness)?

---

## Overview

- **CheckThat Repositioned:** Pause active selling of CheckThat; reposition as a free lead generator feeding into ContentOS sales conversations.
- **Technical Unblock:** DuckDB-to-Clickhouse migration (~2 weeks) will enable filters, data slicing, and faster feature shipping. Jacopo validated the approach on ContentOS side.
- **Sales Enablement Gap:** Teams struggling with CheckThat usability and conflicting documentation. Unified enablement session and Loom videos planned for Monday.
- **Sales Focus on ContentOS:** All selling energy directed at ContentOS as the core revenue product. CheckThat supports it as a complementary data and insight tool.
- **Three-Layer Roadmap:** Layer 1 = enable sales with quick visuals and Loom videos; Layer 2 = ship filters and grouping for sprint teams; Layer 3 = Marcel's advanced multi-metric analytics (AI visibility + 4 more metrics no competitor supports).

---

## Key Topics

### CheckThat Product Strategy and Positioning

The team agreed to pause selling **CheckThat** to focus on simplifying it as a lead generator feeding into **ContentOS** .

- Anna Baird emphasized that **CheckThat** has great potential but is currently too complex for easy use or to deploy as a standalone sales engine.
- The decision was made to pull it temporarily from selling due to excessive setup time and a price point mismatch.
- The goal is to create a lighter version that sales and marketing can quickly use to highlight client challenges and generate leads without heavy setup.
- This approach supports positioning **CheckThat** as a free tool to spark conversations leading to the higher-value **ContentOS** product.

Marcel Santilli explained that **CheckThat**'s data and competitor mapping provide unique AI visibility insights but require better UI and filtering to unlock value .

- The main blockers are missing filters and difficulty analyzing data easily, limiting team adoption and replacement of legacy tools like **Scrunch**.
- Marcel is building workarounds using external querying and filtering while the team plans a migration to **Clickhouse** to improve performance.
- The migration is estimated to take about **two weeks** and will enable faster feature development and better user filtering.
- Improved filtering and grouping features are in progress to help internal sales and delivery teams rely less on **Scrunch**.

### Sales Enablement and Usage Clarity

There is a pressing need to provide clear, unified guidance and training for sales on how and when to use **CheckThat** .

- Ella Dillon requested a prioritized list of feature and positioning clarifications to create one source of truth, reducing confusion and conflicting docs.
- Anna suggested one major enablement session plus a couple of short Loom videos to centralize training materials for sales and delivery teams.
- Stevie Kim highlighted the need for education on manual grouping, tagging, and the current limitations until automated features arrive.
- Marcel stressed the importance of framing feature requests by outcomes and business impact, not just UI fixes.

Anna and others agreed that salespeople, especially new hires, cannot be expected to do deep research or complicated setup in calls .

- The team discussed automating workspace setup with pre-tagging and grouping to enable fast demos within **30 minutes** or less.
- Quick visuals showing client positioning versus competitors are seen as the most valuable sales asset.
- If the tool remains too complex, the fallback is to use Loom videos or demos prepared by experts rather than live setups by sales.
- The sales team's main focus should remain on selling **ContentOS**, with **CheckThat** acting as a free, easy-to-understand entry point.

### Technical Infrastructure and Feature Roadmap

Technical improvements are underway to enhance **CheckThat**'s backend and UI to support feature requests and scalability .

- The migration from **DuckDB** to **Clickhouse** promises better performance and faster shipping of requested filters and data slicing.
- Jacopo completed Clickhouse migration on the OS side with perfect data matching to Google Analytics, validating the approach.
- Jose will learn from Jacopo to expedite the migration, estimated to take a few weeks.
- Feature layers were outlined: quick workspace setup for sales, filters and grouping for sprint teams, and advanced metrics for future strategic advantage.

Stevie Kim noted ongoing admin panel improvements and automation efforts to reduce manual work and improve role-based access control for delivery teams .

- Current admin access is limited due to risks of unwanted changes; more granular permissions are planned but not yet prioritized.
- Automations will help streamline workspace setup and management, which is critical as the team scales.
- Enabling sales and delivery teams effectively depends on these backend improvements.

### Sales Process Integration and Market Positioning

The team agreed to reshape the sales message to focus on **ContentOS** as the core offering, with **CheckThat** supporting it indirectly .

- Marcel recommended positioning **CheckThat** as a data collector and insight generator, with the sales team delivering conclusions, not pushing customers to use it themselves.
- Anna stressed that customers want to "play" with the tool, but this should be controlled to avoid confusion until the product is more mature.
- Current public beta access exists, but the practical approach is to limit direct customer use and emphasize expert-led insights.
- Competitors like **Profound** and **Scrunch** influence market expectations, but **CheckThat** offers unique data coverage and AI visibility metrics.

Jason Gong highlighted the opportunity to use **CheckThat** for earlier-stage outbound lead generation targeting director-level prospects to reduce reliance on expensive dinners .

- A simple, compelling snapshot of client weaknesses drives urgency and pipeline growth.
- Marketing and sales will collaborate on case studies, short videos, and demos to support this approach.
- Tyler and Nigel will be used as initial test cases to validate ease of use and enablement success.

### Team Collaboration and Next Steps

The team committed to coordinated efforts to resolve feature gaps, improve training, and align messaging by early next week .

- Ella will deliver a prioritized list of asks and customer pain points by end of day to help engineering and product focus.
- Marcel plans to consolidate sprint team EMs into a weekly one-hour call to unify knowledge and reduce disconnects.
- Monday is targeted for a major enablement meeting for sales and delivery teams to ensure readiness.
- The overall priority remains finishing **ContentOS** while maintaining **CheckThat** as a strategic lead tool without distracting from core revenue drivers.

---

## Action Items

**Ella Dillon (GrowthX)**
Compile and deliver a prioritized list of explicit UI and positioning clarifications, including customer asks and examples — due end of day Friday Feb 27

**Daniel Lopes (GrowthX)**
Collaborate with Jose and Jacopo to facilitate the Clickhouse migration for CheckThat backend; oversee feature rollout for automated tagging, grouping, and taxonomy; validate ease of workspace setup for sales enablement

**Marcel Santilli (GrowthX)**
Continue developing MVP for advanced data slicing and insight generation; expand weekly sprint call to include all EMs; prepare sales enablement materials and support demos

**Stevie Kim (GrowthX)**
Create comprehensive enablement Loom video that ties together CheckThat workspace creation and usage, addressing caveats and FAQ; improve admin panel automation and granular role permissions; provide ongoing education and support for sales and delivery teams

**Anna Baird (GrowthX)**
Coordinate creation of sales assets including short videos, case studies, and updated sales deck integrating CheckThat insights with ContentOS; lead decision on positioning CheckThat access for customers; facilitate cross-team enablement session scheduling

**Jason Gong (GrowthX)**
Collaborate with marketing on outbound strategy leveraging CheckThat lead generation capabilities once enablement content is ready

**All Engagement Managers (GrowthX)**
Participate in upcoming all-EM enablement meetings starting Monday to synchronize knowledge and share best practices

---

## Transcript

**Ella Dillon:** Anna.

**Anna Baird:** Happy Friday.

**Ella Dillon:** Happy Friday.

**Anna Baird:** This company is a Slacking machine. I'm trying to follow, like, what are the 50,000 things we're talking about at all of these threads? And, you know, I'm only two days a week, so trying to balance all these things is getting interesting.

**Ella Dillon:** I'm like the opposite of ADHD. I'm a synthesizer. I'm meeting with Valentina later — I've done it myself, but I haven't perfected it where I need to basically use AI to trawl all of the things and just give me a summary.

**Anna Baird:** Yeah, I do too. Same thing.

**Ella Dillon:** The other thing is that people still have a bias for jumping. So, for example, CheckThat relative to this, there's so much swirl. People are like, do I just not use it? Do I let people have Scrunch? People don't know what to do.

**Anna Baird:** Right.

**Ella Dillon:** And others are wonderful. Like, I love the bias to action, but they are coming up with directions based on all the conflicting information that's out there. The bias to action is great, but it's a lot. I'm trying to pull all the things together.

**Anna Baird:** Jason and I were talking about that yesterday. We've got to do more collaboration and, like, who's on first to make sure we're not duplicating or going down a path that ends up having to be corrected. It's a lot going on right now.

**Ella Dillon:** The anointed owner so that everybody knows to defer.

**Anna Baird:** Hi, Stevie. I'm Anna. Nice to meet you.

**Stevie Kim:** Nice to meet you all, too.

**Ella Dillon:** This meeting is being recorded.

**Jason Gong:** Daniel, thanks for letting us into your meeting.

**Daniel Lopes:** No, it's not my meeting. Marcel should be joining us, I think.

**Stevie Kim:** Yeah, I think he's the one who added people.

**Daniel Lopes:** Oh, we have full house today. I didn't see that you're there, Ella.

**Anna Baird:** We've all been talking a lot about CheckThat. And so we —

**Stevie Kim:** No, this is good because I've been fielding a lot of questions on that.

**Anna Baird:** Yeah, we have a lot of questions, a lot of thoughts and it'd be great for us all to make some choices and we can figure out how we move forward. How did Marcel make it through his podcast yesterday? His voice was so horrible.

**Jason Gong:** I didn't talk to Marcel, but Will was saying it was a good episode.

**Anna Baird:** He was losing his voice yesterday morning and still hadn't done the podcast. He was barely talking on our call — kept just putting things in chat because he didn't want to use his voice.

**Marcel Santilli:** So what's up?

**Anna Baird:** Hi. You sound a little better today.

**Marcel Santilli:** Getting there.

**Anna Baird:** I heard you made it through the podcast. Awesome.

**Marcel Santilli:** Yeah, I have my recipe — 8am radio host, midnight DJ. Drinking a lot of whiskey and singing jazz late nights.

**Stevie Kim:** We wish that's what we were all doing.

**Marcel Santilli:** Yeah, exactly.

**Anna Baird:** I know we all kind of hijacked this meeting a little bit so we could all get aligned on CheckThat. Can I do a quick summary of some stuff that's happened this week to kick off?

**Anna Baird:** Big picture, obviously from my perspective the most important thing for GrowthX is getting ContentOS in a really great place and launched. CheckThat was an awesome addition, icing on the cake if we could make that all work. But what's come out is it has so much capability but is still a little bit difficult to use, difficult to get up and running. Not something that we can just PLG and throw out there and use as an engine.

**Anna Baird:** So the final decision beginning this week — let's pull it out from selling it for a minute because we have too many things, too much time to get it up and running. For the price point we were thinking of, you probably don't want to spend a bunch of time getting it up and running yet.

**Anna Baird:** But what we're thinking about is — could we skinny it down and use it as a lead generator? The question is, what could we show in it that gets somebody to say, ooh, I want to understand more about that? Really that comes to highlighting challenges we see.

**Anna Baird:** Without a ton of effort — because if there's a ton of effort, we should have a different discussion — could we make it lighter so that the sales team and marketing could use it to say, hey, look what we're seeing as we look at your results? Either they could do it on their own or we could quickly do it. Not a half hour, not two hours to set up, but something we could quickly do and use as a lead generator.

**Anna Baird:** Plus a case study, plus the shortened video we did with Marcel — we're starting to get this really beautiful package together to get people excited about talking to us. Then in our Sprint, do the deeper dive as the product gets simpler. We can use it in the Sprint process as one of the deliverables.

**Anna Baird:** And then I think we all just want to make sure we're also on the same page about what we're saying to current customers and what we're saying to prospects. Is that an accurate summary? Ella, Jason, Daniel, Marcel?

**Ella Dillon:** May I add one ask on top of that?

**Anna Baird:** Absolutely.

**Ella Dillon:** So I am so on board with everything you said and the simplification. I think the one step further — even in the Sprint right now the team is struggling and even talking about reverting to Scrunch. They don't know what they can show.

**Ella Dillon:** My ask would be: we have the simplification, but then we have a very explicit decision about how we want our team to use it. Do we want them to be able to not use Scrunch? What is the displacement or the strategy of how our team uses it in Sprint? Because there is a lot of swirl about how they can use it or can't use it today, and I need to stick that landing for them — and that has some feature functionality prioritization.

**Daniel Lopes:** I don't see why — if we're at a point where we cannot replace Scrunch, that is a big problem because we should be at the point where it should have replaced Scrunch for everybody. So anything that's blocking the team from being able to replace it should be priority. What's your take there, Marcel?

**Marcel Santilli:** Yeah, the biggest blockers right now are just that there's no filters, there's no easy ways to analyze the information. That's why I'm trying to set up essentially an MCP server to be able to query the data. It's not related to the data — it's related to, okay, you have certain computed things in overview, I can't get to those because there's no filters. The fundamental probing and data is there, but drawing the insights that people need to draw very easily is limited by the UI and the interactions and the filters.

**Marcel Santilli:** The other one I heard was around LLM bot traffic — people are starting to pay more attention to that. It's additional features for more advanced users.

**Daniel Lopes:** Bot traffic is non-trivial to add because it's a whole Google Analytics integration. The filtering stuff is what Jose is already working on. On the flip side, Jacopo finished the Clickhouse migration on the OS already — it's working 100%, matching perfectly with Google Analytics. So probably Jose and Jacopo can get together and switch us to Clickhouse, because that's just a technical difficulty — we built the filters but couldn't ship because of performance of the DuckDB setup. Clickhouse solves that.

**Daniel Lopes:** The main thing is that Jacopo is full-on building a ton of stuff on the OS, so he wouldn't be able to do the CheckThat part himself. But if Jose can learn from him, spend an hour or two just learning what he did, we can probably put Jose on it. It will probably take a couple of weeks max to do the migration.

**Marcel Santilli:** Just for context for Anna and Ella — as we started going through this, we were planning for a lot of data, but then the amount of data and computing graphs we had to do is like terabytes of data daily. It's crazy exponential. Every time we needed to add another feature, another filter, another computed chart, it was compounding.

**Marcel Santilli:** The engineers and Daniel started looking into alternatives — we already built on Postgres, so trying to find an alternative there. But Clickhouse is the standard now. We did a prototype with Clickhouse on the OS side, which had less data. That prototype was done pretty quickly and it's validated.

**Marcel Santilli:** So it's looking like we can do a migration to Clickhouse on all our data for CheckThat — let's call it a two-week amount of work which we need to do no matter what. That would unlock our ability to do a lot more things faster. It's also why in the meantime I've been trying to query the data directly to validate what kind of views we need. We don't want to tell engineering, go spend two weeks building a view and filter and not have already validated that's the right thing to build.

**Daniel Lopes:** But if we had filters, we essentially have parity with Scrunch for the use cases we have. That's what we were building towards all the way until February.

**Marcel Santilli:** Okay, so are we missing anything here?

**Stevie Kim:** No, I think there's also just a little bit of education. It might not be as easy to figure out how to get the information that people need as it is through Scrunch. I've been walking people through it ad hoc. I need to put something together like a Loom. Being able to tag and group the prompts and do taxonomy —

**Daniel Lopes:** Stevie, that's what we should —

**Stevie Kim:** No, it exists now. A lot of the things they're looking for actually exist now. They just maybe weren't aware. They didn't see the Loom I created. They can group by categories — that's a lot of times what they're asking for. They can add tags and group the prompt view to see trends. They can compare different prompt variants by using tags. It's just very manual right now — you have to do everything yourself. That's where V2 is going to remove a lot of that manual work, but

**Marcel Santilli:** That's coming in the future. In the meantime, what I've been doing is — any view, as long as you have a slice of the data, last seven days, and that data is mostly already computed, you can do almost any analysis using an agent or Claude. That's not ideal, and that's why I'm not trying to open it up to the whole team.

**Marcel Santilli:** But the other thing here is — one of the reasons our teams are struggling with it is why the whole market is struggling with it. When you look at any chart that has 30,000 things and you're trying to look at AI visibility, there's like 700 prompts, 2,700 URLs that have been cited, 50 metrics. This is too much.

**Marcel Santilli:** A lot of what we're trying to do in product R&D is figure out how to show them in a way that's just one grid — here you go, you are here. And then build up from there. That's the thing no one else is doing — they're just approaching it as an analytics dashboard.

**Anna Baird:** Right, 100%. That's what we need from a sales version — just a quick snapshot that shows the challenge so that we can talk about it. There's ways around this. If we can't simplify it, the sales team could do it quickly, or a customer could put in their own thing — ideally they could just see it and click to book a demo.

**Anna Baird:** We could even do a quick Loom — let me give you visibility into what CheckThat will do when you're in the Sprint. If our team could actually do it with all the things you guys are talking about, maybe we could do a video of it in the sales process. I'm trying to think of workarounds, depending on how hard that is.

**Daniel Lopes:** Maybe a path here would be to try to set up a workspace, time it, and build enough. We have a couple of features that are already there that will automate all the tagging, automate all the grouping — that's what I was working on last week. If we ship that feature and validate that you can set up a workspace in 30 minutes with all the grouping and metrics, then that becomes something you could use in the sales process. But if folks are struggling and it takes multiple days or hours, then it can't be used.

**Daniel Lopes:** If it's like any lead that comes in, you can probably automate the whole thing. With the features we did, any lead that comes in gets a workspace, and if it's categorized and tagged correctly, you could take a few screenshots or have a Loom and show — this is what we have on your workspace that we looked into.

**Anna Baird:** As long as it's easy — because if it's not, we should just do a video. Let me say the flip side. That's the grand idea in the perfect world. But ContentOS is the most important thing you guys spend time on. If you told me, Anna, it's going to take us a month to get this done —

**Daniel Lopes:** No, no.

**Anna Baird:** — then we should pause. Right?

**Daniel Lopes:** No, I think we have all the features. That was actually the feature I was working on last week — the final feature that we're going to use on ContentOS too. I built it in both places and handed off to the team, and that's what Jose was finishing. So we have two things in motion.

**Daniel Lopes:** The filters — I don't think they're going to ship in two weeks. But the grouping and taxonomy stuff that organizes the whole product, organizes all your prompts — that is essentially ready. My hunch is that if we ask Jose to ship it and validate that the auto-tagging works, that is enough. Every person that comes in as a lead, we create their account, auto-generate the taxonomy, auto-tag the prompts, and then Tyler or anybody else can record a Loom and send it ahead or use it as a demo during the call.

**Anna Baird:** We stopped demoing it now, right? We're not demoing it. We're taking it out of the invoice. I told them not to talk about it for a minute until we figure all this out so we know what to say. I don't want to mislead a customer and I don't want to promise something we can't show them how it works. We've got a great story right now and this is another great piece of it if we can get it to work. And if we can't, it's something we could pause and pick back up after you guys do ContentOS.

**Daniel Lopes:** It's a separate team. We have five people with me on ContentOS and three people with Stevie on CheckThat. Some of those things are already in motion. The only one that's going to take longer than a couple of days is the stuff Marcel is talking about — the filters for mix and matching, slicing the data in different ways and extracting information. If we're just going to use it as "hey, we're tracking your brand for data collection, here's all the prompts we have for you and here's how you compare with competitors" — that is like a day of work if the features we did last week work. I hope they do.

**Anna Baird:** Let's validate that, because really what they need is even just one or two of those visuals. I love the one where here's where everybody else is and here's where you are. Something simple. Let's talk about what we're going to do about it — because I really want it as a lead into ContentOS. That's where all of our money is going to come from.

**Anna Baird:** If we give this away for free, I'm totally good with that. You have a problem, let us show you how to solve it. In my perfect world, we could load a whole bunch of ICP subscribers in and say which ones have the biggest problems — let's go call them first. We can use that as an outbound lead generator as well. I just want to make sure I'm understanding what might be possible.

**Ella Dillon:** Yeah, I think it's fine. We started with "we're going to sell it," and reverted back to free. But now literally where the team is — maybe I shouldn't be using this at all. Which is a problem. If our own team can't sell it and we're not using it and we're reverting to Scrunch —

**Daniel Lopes:** That is a problem.

**Ella Dillon:** Yeah, it is a problem. Some of it's enablement, but if it's that hard, it shouldn't be this hard. I've asked the team to compile all the asks they've had into a prioritized list with examples of what customers are asking for and why we're struggling. Some will be usability asks of the product. Some will be "we don't even know how to position this yet — can someone just give us the talking points?"

**Ella Dillon:** The bouncing ball has been all over — do we sell it? Do we not? What do we say? I think I've laid that to rest. But I want just one document because a lot of people are creating their own sources of truth now. It's chaos.

**Ella Dillon:** Net, my promise to you is that today I'm going to get you that request from us to you on prioritization. And Daniel, if I could have your help making sure we have a cogent, crisp, one source of truth for the team to know what is true about what we're doing and how to position it — so I can stop the self-creation of conflicting documentation.

**Anna Baird:** Yeah, I think when we're product launching, what's super important is one major enablement session across the whole team and then one or two Loom videos as follow-up — here, let me show you that again, here's some FAQs — so we have one place where everything resides. We don't want things sitting in multiple different locations that are hard for the team to find.

**Marcel Santilli:** Just want to add a few things. From a positioning perspective, the way I've been using it on sales calls is pretty simple: "Part of our process is we need to understand your company, your audience, what market you're in, what buying categories you play in. By the way, we've already done that. We also need to map out all your competitors in your entire buying category to have a contextual understanding of your space. By the way, we've already done that."

**Marcel Santilli:** "Next we need to understand where you are — your site, your content, your competitors' content. We also need to understand where you are from an AI visibility perspective. By the way, if we start collecting that data today, it's going to take a while to get insights. So we already started doing that and we have 90-plus days of data and millions of AI responses we can analyze backwards."

**Marcel Santilli:** "That comes included in working with us. We're collecting that data, and insights from it will come after we start working together. Rest assured, that data is in an open index and it's free — you don't have to spend two, three grand trying to collect this data yourself." In none of that do you actually need to mention CheckThat.

**Anna Baird:** That's the place I was going — if we don't have a lead-in where they can play with CheckThat themselves, we could show them a quick Loom video that validates what you just said. Here's what's going to come as part of the Sprint and why we do that. I love the way you just articulated that. It totally plays into our talk track. We're redoing the sales decks to make it easier for the team to follow.

**Marcel Santilli:** Super quick, just a very concrete example. Yesterday we were on Flodesk and they mentioned MailerLite. In three minutes I set up the entire workspace, backfilled with 90 days worth of data, shared my screen and showed them they were at 3% and MailerLite was at 37.7%. Their eyes went — "fuck." As they should.

**Marcel Santilli:** That took no time. All I did was go in and select competitors that were relevant based on what they told me at the beginning of the call. Within three minutes it was fully set up. Then I went into sources and showed them by domain how their competitors have a lot more citations and how they're essentially nowhere to be found.

**Marcel Santilli:** That was enough for them to be like, "yeah, why do you think that is?" Then I went into Semrush — MailerLite only has 331 pages, Flodesk has almost 2,000 pages. I showed them an example of a MailerLite page and the quality of their content, then showed them their own page and how it's garbage. They were like, "yeah, there's a clear gap here. Move forward, we need help."

**Anna Baird:** That's beautiful. But the team doesn't know how to do that in three minutes. Your capability with this system is not going to translate. I need either the product to translate fast enough — because especially as we scale the sales team, maybe we could train Tyler, but training three, five, seven more salespeople to know the system this well to do it on the fly is not going to be possible.

**Anna Baird:** The thing that was tripping up Nigel — they say different competitors, we have to rerun the whole thing. The prompts are wrong, we have to rerun. I don't think we need to go that far in a sales call. All we need to show them is you've got a problem, here's the three things we see, now let's talk about how we solve that in the Sprint.

**Anna Baird:** What is the simplest thing we can give the sales team? I'm okay if that just needs to be a Loom video. I love the specific company approach, but —

**Ella Dillon:** I would also offer — if you're showing it in sales, the sprint team does need to know it too, 100%.

**Anna Baird:** That is the next given that is important. But Marcel helped build the product — they can't just replicate what he does. We don't have any more Marcels.

**Marcel Santilli:** I'm already cloning myself. Daniel, I processed over a billion tokens this month already.

**Anna Baird:** Are you the most expensive client we have?

**Marcel Santilli:** No — a billion tokens took only two grand worth of credits.

**Daniel Lopes:** George May beats you at five grand a month for Lovable templates.

**Marcel Santilli:** I'm catching up fast.

**Jason Gong:** Let me summarize the stuff Anna's talking about and what's on my mind. Our product is a little hard to use, takes a long time to set up. There's a gap right now for sales — I have thousands of director-plus level people where if I could send them something like "here are your opportunities and here's how we could help you," we'd drive a bunch of them into pipeline. Right now we drive them to dinners, which is a very expensive and heavy way to convert that group.

**Anna Baird:** Great thoughts on how we can start doing more outbound between marketing and sales. This opportunity is not small — it's a big opportunity if we can get the right assets.

**Jason Gong:** Driving earlier tactically — it sounds like, Marcel, that's currently in your court and you're doing the MVP, and then eventually we'll get access.

**Marcel Santilli:** I'm doing the MVP. The biggest blocker has been meetings on my calendar all day. I have agents working throughout the meetings to try to get to a good place. By next week I'll have more to show.

**Daniel Lopes:** That all makes sense. I'm trying to think about layers here. What Marcel just showed — big part of it is just enablement. Folks don't know those features exist. Setting up a workspace like Marcel did is literally probably five clicks — select the competitors you should know based on the call or your pre-meeting research.

**Daniel Lopes:** And the OS consumes data from CheckThat. So if the workspace and competitors exist on CheckThat, that shortcuts the whole research process on the OS. We're not pitching a Profound replacement — we're pitching "we're understanding your space, we need to know you well and your category well." That will shortcut the workspace setup on the OS by a lot.

**Daniel Lopes:** So the layers: validate if Tyler and Nigel can learn how to set up a workspace from scratch. Use them as the validation for "is this easy enough?"

**Anna Baird:** If they can use it easily, you're good. They're a great test ground.

**Marcel Santilli:** Let me show them really quickly if we have three minutes.

**Daniel Lopes:** Just to finish my chain of thought — layer one: see if we can enable Tyler and Nigel. Layer two: ship filters and grouping to enable the sprint team so they don't have to use Scrunch. Those are two different enablement documents. Layer three: what Marcel is working on now — we're not talking about Profound and Scrunch replacement anymore. It's a completely different way of thinking about the market where he has five different metrics. AI visibility is one, there's four more. Nobody else supports them because they don't have this open graph of all the competitors.

**Daniel Lopes:** We have these three layers to crack. Layer one for Tyler and Nigel, we're pretty much in the state to give it a try and see how well it goes.

**Anna Baird:** If we can enable them and they're like, "oh man, I got this," then we're probably good. Then we can do Loom videos. Jason, you and I can chat about what we do on the marketing side. Between the shortened video with Marcel, plus case studies, plus a Loom video on "look at what we already start to learn about you to inform our strategy" — we have a nice combination for lead generation.

**Ella Dillon:** Is it worth having William in that meeting as well to expedite? He can do the demo and address the inevitable follow-up questions.

**Anna Baird:** Yep, I'll do that in parallel.

**Ella Dillon:** I talked to Andy. I will have by end of day the team's prioritized list for explicit clarifications — either UI and/or positioning. Daniel and Stevie, just so you have it in one clear space. Help us knock those down or at least close the loop, because I think you're doing things but they don't know where it is or who to go to.

**Stevie Kim:** Did you have them add the why? Feature requests — what tasks they're trying to do, why they're trying to do it, how they're doing it now — that would be really helpful.

**Marcel Santilli:** And Ella, for everyone — the mental model I've been trying to instill is: outcome, output, work, input. A feature ask should be "I need this feature in order to enable me to do this type of output in order to move this one metric for the client." If they don't have that clarity and they're just like "I need to be able to click here" — to Stevie's point, why?

**Marcel Santilli:** Let me put it super quickly. Nerdio — we're kicking off on the 9th. There's no workspace created here. If I'm on a call with Nerdio, I would search for them — they're already public, there's already a profile. I can always rerun the deep researcher, but I'll quickly check if the categorization is wrong.

**Marcel Santilli:** I go create a new workspace — Nerdio, prospect. Add myself, backfill last 70 days to kick it off. You can enroll all the admins and every single admin gets added to it. Then I go to CheckThat, it shows up in my list. I click add competitors — if it's not clear which ones to add, I can look into their CheckThat page and see what the deep researcher says about their direct competitors and AI visibility competitors for that category.

**Anna Baird:** Right.

**Marcel Santilli:** You can see Workspot, and this can always change. These get a little complicated — MSP optimized, multi-tenant architecture. You can go into review platforms. For now I'll select Citrix and the obvious ones. But if I start seeing a lot that doesn't match what the deep researcher tells me, it usually means we have the wrong category.

**Marcel Santilli:** This is the only part of the process that requires judgment — are these categories correct or not? If they're not, that's why you're not getting the competitors you want. Either way, as soon as this is done running — a few minutes — all of this will be populated and we can tell them their visibility and citation scores. But you're right, as a self-serve experience they're going to run into zeros and wonder why they're not seeing the obvious competitors. That's why I set it up myself.

**Anna Baird:** What you don't want a salesperson to do is get confused, put the wrong stuff in, not understand the category well enough, and then show the customer something wrong. I'm trying to solve for debugging errors as much as possible. If you really need to have done deep research on their space, for a salesperson that's going to be tough. We're trying to get them to process more volume, get more pipeline. Marcel, you're an expert — you're going to be way faster at this than they will.

**Stevie Kim:** I can speak to that. We've been trying to carve out time — there were hiccups this week due to sicknesses and infrastructure outages. We have quite a few tickets and we've made a little bit of progress, but I'd like to make a lot more on automating these admin processes. Marcel was flipping back and forth between the admin panel and CheckThat — there's a lot we can do and want to do to improve and automate that.

**Stevie Kim:** Another thing we probably need to bump up — right now not everybody on the sprint team has admin access because there's too much they could do that we don't want them to do, like changing a brand's public pages category just because the company says so. There's a lot of nuance there. We have a ticket for creating more granular roles and permissions for admins, but we haven't been able to prioritize it. Right now we're limiting who has admin access.

**Anna Baird:** So do we need some time to get automations in play before we do enablement for the sales team?

**Stevie Kim:** No. You asked what could make this easier — those automations are part of it. But what's been missing is one large Loom that ties everything together about creating a workspace and going through everything. We've been good about short Looms on new features, but not the comprehensive one. In that Loom, we'll go through the caveats — like Marcel was saying, if you don't see your category, you're not going to get the right results. That education plus the FAQ will help.

**Anna Baird:** I'm a little concerned about the complexity it's going to take to set this up. But let's try and enable the sales team — at minimum we'll get product feedback.

**Stevie Kim:** Honestly, it just takes Googling. I have domain expertise in MLS and labeling, not in any of the other areas. The only thing is, it takes time.

**Anna Baird:** Right now we have one salesperson who's also doing contracting and all these other things. We need to get pipeline. Adding more work onto the plate — I'm not going to do that. Especially as we're onboarding new salespeople — learn this, then learn this — it's compounding. Speed and ease of understanding is critical.

**Anna Baird:** If the sales process becomes "go do this research, put this in, check that, and if it doesn't work go to the admin panel and change this" — I would vote to have a quick Loom video instead.

**Stevie Kim:** Shouldn't they understand the business vertical they're trying to serve?

**Anna Baird:** What I need them to understand is ContentOS, because that's what we're going to sell. That is the big ticket item that's going to drive revenue for this company. Tyler is really good at talking about what we can do for them. We're going to make it even better with the flywheel of AI workflows plus skilled expertise — truly quality at scale.

**Anna Baird:** CheckThat is a beautiful gateway into those discussions if it's easy. It creates a flywheel — giving them FOMO about why they need to do something different. But if I have to spend all the time to get

**Anna Baird:** CheckThat up and running just to get a little bit of FOMO, I'd rather do a Loom video and get them into ContentOS.

**Stevie Kim:** That's clear. I was thinking of more Nigel than —

**Anna Baird:** Nigel's not selling CheckThat. Sorry, we just did this this week — it's too hard to sell CheckThat separately because of everything customers need to do. Our price point is probably off with that level of work. So we're gonna offer it for free.

**Marcel Santilli:** Talking about CheckThat, sorry.

**Anna Baird:** Right. We are offering CheckThat for free. It's a beautiful lead generator if we can get it simple enough — "hey, look where you are" or "let me show you on this quick call where you are." Just using it as a line in the sand.

**Anna Baird:** Just using it as a line in the sand.

**Anna Baird:** Say, look at this.

**Anna Baird:** Let me talk to you about how we fix it with ContentOS. We moved Nigel over — he's just going to be helping sell broader services.

**Daniel Lopes:** For the three layers — for Nigel and Tyler, a video. We still need enablement for the strategy sprint because the better the workspace is set up in CheckThat with categories and competitors, the better data we have on the OS. The workspace setup on the OS is all about understanding the topics, the sites that get most traffic, the thought leaders. There's a lot of automation and we pull that data from CheckThat.

**Daniel Lopes:** CheckThat will be the first step on the workspace setup of the OS for the long run. If the brand has a public profile on CheckThat with top competitors, it shortcuts everything and improves quality all the way down.

**Anna Baird:** I love that connectivity — all the work we need to do to understand you is already happening in the background through CheckThat. We can weave that into the sales decks. Ella's team's enablement and ability to use it is the most critical thing.

**Marcel Santilli:** Cool. I know we gotta run to another meeting. Daniel, I'll hit you up later — we have calls next week to think through the work-backward plan for ContentOS.

**Anna Baird:** I would sacrifice CheckThat if I had to, if you needed more engineers on ContentOS. Just my personal two cents. Quick recap: we're gonna do a Loom video for Tyler and Nigel, then spend time updating CheckThat's UI to enable the delivery team better.

**Anna Baird:** Right now we've been saying "in the Sprint, you get free beta access to CheckThat." Should we not say that and just leave it for our team to utilize, saying "this is part of our process and our AI"?

**Ella Dillon:** We can say that, but practically what's happening is customers see it and want to play anyway.

**Anna Baird:** That's why I'm saying — should we not let them? Should we pull it back and put it as part of our AI workflow, show it to them but don't let them play with it?

**Marcel Santilli:** My hope is that we use CheckThat in the sales process but don't push people into logging in themselves and trying to draw conclusions for a few more weeks at least. We put all our effort on sales enablement for telling the right story about ContentOS — because those are things people are willing to pay for. No one's going to pay much for CheckThat or any visibility tool.

**Marcel Santilli:** And now Profound just announced their Series C. Everyone's like, "they're worth a billion dollars, there must be special sauce, I should go talk to them." Heard it from every person this week. They have this big event next week about agents, selling autonomous agents for all their website tasks. We can't be talking about "here's this analytics tool over here" — we gotta lead with ContentOS. It doesn't need to be next week. But the things the team has built and is building now, we can already start to prepare how to talk about it from a sales perspective.

**Anna Baird:** So we're gonna pull back on letting them use it in the Sprint for now, until you guys say. Is that correct?

**Ella Dillon:** The problem is it's already out in the wild.

**Stevie Kim:** There are already customers logged in themselves. Public preview or public beta is a way to position it. Once Marcel has the shaping done, we can put together enablement material to educate the sprint and delivery teams on how to talk about the future.

**Daniel Lopes:** You could frame it as "this tool is for us to understand your space. You can log in if you want, but drawing conclusions and insights is our team's job. You're not required to operate it."

**Marcel Santilli:** Yeah — we have agents that in the background query the data and come with insights. That's how we generate opportunities for you and come up with your strategy. You can log in and play with it, but this is a way for you to visualize the millions of AI responses we're collecting every month.

**Ella Dillon:** The practical thing that's happening is — when we try to say that, customers then want to use Scrunch. If we say no to CheckThat, they want Scrunch seats, and then we're promoting Scrunch.

**Marcel Santilli:** We're not saying no, Ella. We're saying yes — but we're not positioning it as a Scrunch replacement right now. We're positioning it as: here it is, we're collecting all this data for you, and we're using this data to shape our opportunities. But it's a lot easier when you can say "this EM is talking to this customer and the customer wants to use Scrunch for this reason" — otherwise, the hypothetical doesn't land.

**Daniel Lopes:** But.

**Marcel Santilli:** But it's kind of like, look, sure, like, you want to spend 500, like, go for it.

**Marcel Santilli:** Who cares?

**Marcel Santilli:** Like, a little bit.

**Marcel Santilli:** The more bandwidth EMs are focusing on that stuff, I'm jumping on these accounts and the content sucks, the strategy is horrible, and we're not growing their traffic.

**Ella Dillon:** That's my point.

**Anna Baird:** I would like to take distraction off their plate.

**Marcel Santilli:** As long as we're nailing this, it will matter a lot. If we're doing the right things, they're going to start to be cited whether they're using CheckThat or not to measure it. They're going to see that we're doing great work.

**Ella Dillon:** I'm totally with you, Marcel. We can provide clarity so they're not distracted. This is a mental tax that we should fix for them so they can focus on the right thing. My thing is to provide the explicit things they're navigating so you guys can explicitly answer them. I will have that written up much more clearly for you by end of day.

**Marcel Santilli:** As an action — I was talking to Bridget about this, but I would prefer the one hour I'm spending every week with sprints to be all the EMs. I spent a ton of time with Carly and others — they're on another planet. They have no idea what William is learning. They're getting miles disconnected. If I spend that hour with them as well, they'll get to a better place.

**Ella Dillon:** Bridget already put up a placeholder for Monday. I've talked to one EM this morning to see if he can be pivoted and ready on Monday. We're confirming that everything will be locked and loaded. It might have to wait a week depending on how fast he can land the plane, but — done. I agree with you.

**Marcel Santilli:** Awesome. We got to run to this other meeting.

**Anna Baird:** Thanks everyone for spending the time. Really appreciate it. We'll talk to you soon.
