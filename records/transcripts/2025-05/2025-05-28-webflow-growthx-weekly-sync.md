# Webflow <> GrowthX Weekly Sync

<metadata>
date: 2025-05-28
time: 17:31 UTC
duration: 28 minutes
organizer: jason@growthx.ai
participants: Jason Gong (GrowthX), Vivian Hoang (Webflow), Colin Lateano (Webflow), Anushri Gupta (Webflow), Kirat Chhina (Webflow), Kyle Gaudreau (GrowthX), Sydney Go (GrowthX), Daniel Lopes (GrowthX), Rachel Wolan (Webflow), Darin LaFramboise (Webflow), Kelly We (Webflow)
fathom_recording_id: 65180065
fathom_url: https://fathom.video/calls/310938214
share_url: https://fathom.video/share/r5FXu1haaxi1WKMbp7vRTekPvoe1stNn
source: fathom
enriched_on: 2026-03-04 14:32 UTC
</metadata>

---

## Summary

GrowthX and Webflow aligned on a major content strategy overhaul, splitting developer content into two distinct hubs: a standalone Integrations hub (modeled after Ramp) and a Developer Blog as an extension of Webflow's main blog with expanded cluster tagging for better discoverability. GrowthX will own the tagging matrix strategy and suggest related articles to create a more interconnected content experience, while Webflow's Product Marketing and Michael will provide brand messaging guidelines to ensure consistency across all developer content. The team also explored expanded LLM citation monitoring beyond the developer persona and discussed leveraging Webflow's unique traffic data showing 10x growth in AI crawler activity, representing a significant opportunity for thought leadership content.

---

## Context

Webflow is a low-code web development platform and is one of GrowthX's strategic content clients. This weekly sync between GrowthX's content team (Jason Gong, Kyle Gaudreau, Sydney Go, Daniel Lopes) and Webflow's product and content leadership (Colin Lateano, Vivian Hoang, Anushri Gupta, Michael, and others) is core to aligning on content strategy for Webflow's developer audience. The meeting reflects ongoing evolution in how Webflow structures developer-focused educational content, with leadership consensus shifting toward creating separate, specialized content hubs rather than trying to duplicate or aggregate content across multiple properties. This represents a maturation of the relationship and Webflow's thinking about developer audience engagement.

---

## Relevance

**To GrowthX Delivery:**
- Expanded scope: GrowthX now owns the entire tagging strategy (no upper bound on tags per article), positioning it as a strategic content partner beyond just writing articles
- Two discrete content production tracks (Integrations hub and Developer Blog) allow for parallel workflows and clearer ownership boundaries
- Webflow wants GrowthX to flag content relationships and suggest existing articles that need updates to reference new content — adds a strategic editorial layer to content planning
- Upcoming PMM involvement signals elevated strategic status of the developer content program within Webflow's organization

**To CheckThat:**
- LLM citation monitoring expanding beyond developer persona to track Webflow's brand visibility as a CMS, creating broader AEO/CheckThat opportunities
- Opportunity to build thought leadership content around AI crawler insights (ChatGPT 10x growth vs static Google crawler activity on Webflow properties)
- Traffic shift from SERPs to direct suggests ChatGPT/LLM is becoming a discovery mechanism for Webflow content

**To GrowthX Business Development:**
- Account health signal: Webflow investing significantly in developer content strategy, product marketing alignment, and brand messaging consistency (positive expansion)
- Potential for expanded scope: Webflow exploring multi-dimensional content strategy (integrations, developer blog, guides, learn section) across multiple properties
- Reference potential: This content model could be a repeatable framework for other platform/infrastructure clients with developer audiences

---

## Overview

- Two new content hubs: Integrations (standalone) and Developer Blog (extension of main blog)
- GrowthX to own tagging strategy and suggest related content for improved discoverability
- Shift towards more granular, clustered content with multi-dimensional tagging
- Increased focus on brand messaging consistency and LLM citation monitoring

---

## Key Topics

### New Content Hub Strategy

  - Creating two distinct content hubs on Webflow:
    1.  Integrations hub: Standalone folder, similar to Ramp's integration page
    2.  Developer blog: Extension of main Webflow blog
  - Integrations hub to include:
      - Lead page with all integrations
      - Tagging for marketplace apps vs. self-built integrations
      - Default template for each integration (explanation, usefulness, implementation)
  - Developer blog to feature:
      - Expanded cluster tags for better content identification
      - Suggestive content and nested keystone content for deeper discussions
      - New content hub under main blog, separate from dev docs

### Content Tagging and Clustering

  - GrowthX to own and propose clustering of articles using multiple tag sorts
  - No upper bound on tags per article
  - Aim for suggestive "related posts" and improved content discoverability
  - Tagging to grow over time as more pillars and keystone content are established
  - Only existing tag is "developer"; new matrix tagging system to be implemented

### Content Relationships and Updates

  - GrowthX to suggest related articles and potential updates to existing content
  - Goal: Create a more fluid and interconnected blog experience
  - When suggesting new articles, indicate which existing posts should be updated to reference the new content

### Brand Messaging and Content Review

  - Need for better alignment on brand messaging, especially regarding Webflow as a CMS
  - Product Marketing and Michael to provide guidelines on presenting Webflow consistently
  - Weekly meetings to focus on high-level strategy rather than individual content reviews

### LLM Citation Monitoring

  - GrowthX to help monitor LLM citations and mentions of Webflow
  - Expand monitoring beyond developer persona to track Webflow as a brand for CMS in general
  - Aggregate citation sources for brand marketing and community teams

### AI Crawler Insights

  - Significant growth in ChatGPT crawler activity on Webflow properties (10x increase in a few months)
  - Google crawler activity remains static
  - Observed shift in traffic from search engine results pages to direct traffic

---

## Action Items

**Jason Gong (GrowthX)**
- Create suggestions for integrations page structure + content types; share with Webflow team
- Develop comprehensive tagging strategy for blog content; include matrix for evolving tags
- Compile + share list of prompts for LLM citations/mentions monitoring; include general CMS brand visibility
- Schedule separate meeting for in-depth content review with Webflow team

**Vivian Hoang (Webflow)**
- Coordinate with PMM team + Michael to share brand messaging guidelines with GrowthX

---

## Transcript
**Jason Gong:** Hello.

**Anushri Gupta:** How are you?

**Anushri Gupta:** Good.

**Jason Gong:** Busy as always.

**Colin Lateano:** Hello.

**Jason Gong:** Colin.

**Colin Lateano:** Jason, great to see you.

**Colin Lateano:** How many note takers are we at today?

**Jason Gong:** Is it four?

**Jason Gong:** Only three.

**Colin Lateano:** Only three.

**Colin Lateano:** Zoom's actually recording.

**Jason Gong:** Is that really?

**Colin Lateano:** Yeah.

**Jason Gong:** I wonder if that's us.

**Jason Gong:** We really need to consolidate these.

**Colin Lateano:** You're the host. That's okay.

**Colin Lateano:** So I promised you last week we'd come back with a strategy of what's going on, where content lives, and overall how we're approaching it. I do have that strategy, though I don't have a good visual for you.

**Colin Lateano:** So we're going to bounce around for a second while I show other example sites that we're going to pull inspiration from and explain it. First off, we're going to create two content hubs on Webflow. One is going to be a hub for integrations that is going to move off from the university.

**Colin Lateano:** We're going to move integrations to its own standalone folder. I'm not saying this is exactly how it's going to look or feel, but more or less, it's going to follow something like Ramp or other fintech platforms that have a large-scale integrations grouping.

**Colin Lateano:** It will be a lead page of everything you want to consider.

**Colin Lateano:** Maybe some will get tagged as this is an app on our marketplace.

**Colin Lateano:** Some will get tagged as this is an integration that you have to build yourself, or here's the guides to do it.

**Colin Lateano:** And when you click into one, there is some sort of default template we use to explain the integration, maybe a little bit of why this integration is useful, what it does with Webflow, and how you engage on it.

**Colin Lateano:** We do not need to look into videos of it.

**Colin Lateano:** Ramp went above and beyond, but more or less, this is going to be its own CMS and content hub on Webflow.

**Colin Lateano:** Now we're going to invest a little bit of time into making this sing, but what we would love from you.

**Colin Lateano:** Is some strategic thinking of what, in your mind, for an integration with Webflow, with what you've been thinking about, maybe the content sections, the hierarchy, how you would want to potentially, because we don't have a template at all for this yet, what you think is important information to include to optimize for the flywheel that we talk about.

**Colin Lateano:** Because truth be told, the integrations page is very important to a lot of customers.

**Colin Lateano:** They make buying decisions on, will Webflow work with my existing tech stack?

**Colin Lateano:** And so this is useful to know that there is a way for them to connect on it.

**Colin Lateano:** In my mind, this is part of the product-led growth lifecycle in the flywheel.

**Colin Lateano:** So that's one hub integrations.

**Colin Lateano:** By all means, we can test out, if we have the right format and structure in place, we can test out how we can generate articles.

**Colin Lateano:** I have read the Stripe one.

**Colin Lateano:** I don't think the Stripe one was bad.

**Colin Lateano:** And I think there are categories of how we can make it easier for someone to scroll around on, but this is no longer part of the dev website conversation.

**Colin Lateano:** It's really different than the dev site because many times it is install an app or insert a JavaScript.

**Colin Lateano:** So this is going to live separately, so we don't need to inspire ourselves from a dev docs type of framework.

**Colin Lateano:** This can be its own standalone universe.

**Jason Gong:** So that's super clear.

**Jason Gong:** I think, yeah, I mean, a couple days we'll have some ideas here for sure, the suggestions, and then we can even put together like a rough, you know, mock-up.

**Colin Lateano:** Killer. Outstanding.

**Jason Gong:** So integration.

**Jason Gong:** I'm almost thinking if we did these for them or not.

**Jason Gong:** I'm not sure.

**Jason Gong:** I'll talk to the guy that works on Rant.

**Colin Lateano:** Cool.

**Colin Lateano:** Perfect.

**Colin Lateano:** Yeah.

**Colin Lateano:** Well, I'd love to learn about that.

**Colin Lateano:** I came from Bill.com.

**Colin Lateano:** So we watched this site get developed in with bated breath.

**Colin Lateano:** Ram's our biggest competitor.

**Colin Lateano:** The next part is we're also going to make a content hub, and that hub is going to be an extension of our developer blog.

**Colin Lateano:** There were a lot of debates about the content being competitive to our developer blog, canonical listings.

**Colin Lateano:** Should we have two duplicate blogs?

**Colin Lateano:** Should the developer blog just be a hub that aggregates from the CMS of the main blog?

**Colin Lateano:** And we kept circling back to this is going to be very convoluted engineering to do that.

**Colin Lateano:** And then we started finding that a lot of platforms just took a carve out and made universes of very specific content hubs that had their own derivative.

**Colin Lateano:** We have filter controls and suggestions and even their own theming.

**Colin Lateano:** So there were branches between different structures.

**Colin Lateano:** Tutileo is one example.

**Colin Lateano:** We're not mirroring Twilio, but more or less, the main Webflow blog will be the canonical CMS that we have our developer content on.

**Colin Lateano:** And what we're going to expand into is a graduation of many different cluster tags to help identify developer content and then have suggestive content and nested keystone content that goes into deeper level conversations.

**Colin Lateano:** That's what we were always talking about, but where it lived and how it lived has been unclear. Now it's pointing to being a new content hub under our blog.

**Colin Lateano:** So this also is not on the developer site, but the developer site will link to it. The developer site is still the dev docs.

**Colin Lateano:** We will have this link in our learn section, but it points to a universe of the main blog.

**Colin Lateano:** What that then means is, because we are canonically within the content marketing universe of the main blog, Michael, who you've seen, will also be part of this group to make sure we have alignment on strategy, voice, and signal.

**Colin Lateano:** I'm trying to loop in more people so that we have a steady who to ask questions.

**Colin Lateano:** Before talking about strategy more, I want to make a note for clarity: there's been so much discussion about strategy, ownership, and alignment over the last month. We're moving forward with this methodology now. We'll have myself, a product marketing hire, Vivian, and Michael as the main strategic points of contact for our content strategy and the developer relationship.

**Colin Lateano:** Anushri is DevRel, very insightful on how we communicate to our developers for voice and information and how we display it.

**Colin Lateano:** But this is not going to be owned by the DevRel platform of our DevDocs.

**Colin Lateano:** So content marketing is going to be our main stakeholder in this.

**Colin Lateano:** So strategy-wise, what we need to start talking about, I still don't have access to the Airtable, but I looked at it.

**Colin Lateano:** Because a lot of is going to be based on, a lot of what we want to do is proper clustering of content.

**Colin Lateano:** And...

**Colin Lateano:** Seeing things like this as inspiration, or in your original example, we had a headless CMS article and a mono-repo article.

**Colin Lateano:** What I would love to do on your content targeting map is I would love it if GrowthX started to own and propose the clustering of the articles by multiple tag sorts.

**Colin Lateano:** If you have an article on MCP, that could be AI, that could be serverless, that's developer, of course, that's API.

**Colin Lateano:** Like, there are many tags that I think you need to start helping us cluster into because what we want to do is have the blogs also be suggestive of your learning experiences.

**Colin Lateano:** So as you're going through this blog, there can be related posts or you might want to read as well.

**Colin Lateano:** Having the right, our upgrade to the Webflow blog is going to be much more on how we can have.

**Colin Lateano:** What is the next best article, related articles?

**Colin Lateano:** And you see we have some that are all about development, but we want to be much more targeted on unique cluster tagging so we can sort and filter appropriately.

**Colin Lateano:** That's straightforward.

**Colin Lateano:** Any questions on the hub strategy or tagging strategy so far?

**Jason Gong:** No, I think it all makes sense.

**Jason Gong:** So basically, it'll live as a branch of the blog, essentially, with, I guess, a shared set of tags, I guess, in some cases, with the blog, and then maybe, like, a front page that looks different.

**Jason Gong:** I guess that one's not too much of a concern, since we're just doing the content.

**Colin Lateano:** That's right, there'll be a front page, and there'll be some filter conditions on the front page of the hub that, again, this

**Colin Lateano:** Not going to be exactly mirroring Twilio, but we will have topics, different types of major categorical filters, and as we grow the content repository, we'll be adding more filters to control on, and there'll be a matrix type of search of, I want to see topics about AI and, I don't know, AI and data.

**Colin Lateano:** And maybe, maybe we have a multi-step matrix, or we have a search of it, but more or less, 6,000 articles, very granular, detailed articles, we need to have a way to have developers be able to find what they want to find, and so, the filter controls are going to be a factor in this one, so we just want to make sure they're, the tagging is considered at the article creation.

**Jason Gong:** Okay, so, that makes sense to me.

**Jason Gong:** I um, next, um, I think Mike brought up a few things, I mean, we're getting into the weeds of writing.

**Jason Gong:** Like, you know, more on the product marketing side, how do we talk about Webflow and position it?

**Jason Gong:** Yeah, but we can get to that.

**Colin Lateano:** I have two more small strategy points before we dive in.

**Colin Lateano:** This is like the core trying to address is, as you can see on this, we don't want the Webflow blog to be competitive with itself as well.

**Colin Lateano:** So part of this as well in the content strategy and the content that you'll be creating, if you can, at least suggest in your suggestions which blogs are either part of the nested association, either in a pillar strategy or a keystone with subsidiary pieces.

**Colin Lateano:** If you are aware, or if your service can be aware, of other blogs or posts either you've created or the Webflow team have created that share a relationship with the article you're suggesting.

**Colin Lateano:** And ideally, we would love to be able to know how these are nested and related.

**Colin Lateano:** I don't know about the content structure hierarchy that you want to play into on that one, but order the content management system article is fine, but it would be very helpful.

**Colin Lateano:** If we knew when you were suggesting a new article of, hey, you should definitely update the content management system article to include a reference to the next piece as well.

**Colin Lateano:** So what we'll be doing with the content marketing team is when we have these waves or batches of publications, we also would want to go back and look at our other content and see what we need to shore up to reflect that we have interrelated content.

**Colin Lateano:** For example, if you start talking about a headless CMS, and we mentioned it in an earlier article, then in the next post that discusses a headless CMS, we could update the earlier article to include a link to the new content.

**Colin Lateano:** I'm not saying we need GrowthX to say, suggest updates to previous articles, but at least if you can call out articles that are related that should be considering the new article you're producing, that would be an ideal way to make this a much more fluid public blog.

**Jason Gong:** Yep.

**Colin Lateano:** Is that possible or feasible in your approach?

**Jason Gong:** Yeah, I think so.

**Jason Gong:** I mean, I'm trying to think what that'll look like, but essentially for every article that we're writing, maybe there's just another column of like, here are the kind of pillar or like related articles that should reference this or may need to be updated, I guess, to reference.

**Colin Lateano:** Yeah, and even if that's just a semantic search you run, that's fine, but just a call-up would be really great in the inventory mapping calendar that we're doing.

**Colin Lateano:** Those are all the strategic things that we have aligned on in the last week or so on this game plan.

**Colin Lateano:** I can also write that up and share that in the channel, but that's the fundamentals of what we're doing for.

**Jason Gong:** Yeah, no, I think that's recorded, so that's great.

**Jason Gong:** I think there are two very clear lanes that we can start pushing on for the integrations. We'll start with a suggestion on page structure and what kind of content goes on it. Once we align on that, we can start producing. And then on the blog side...

**Jason Gong:** It sounds like I owe you and Vivian our Webflow org — we're still setting that up — then you can clone the project there. From our side, it's about having a content catalog with all the tags.

**Jason Gong:** But for tags, is that already decided by you guys, or do you want us to kind of take a look and have a suggestion there as well?

**Colin Lateano:** Actually, we're not even going to be close to doing the tags justice.

**Colin Lateano:** From what I've seen — and I need to get proper Airtable access — we have such a granular level of detail. As we publish articles, there will be more long-tail keywords we're trying to capture. Our tagging infrastructure is going to grow significantly.

**Colin Lateano:** And I would love it if GrowthX actually owns the tagging matrix.

**Colin Lateano:** And the way we're evolving our blog is to have no upper bound of tags on an article.

**Colin Lateano:** So if GrowthX wants to establish a tagging strategy and grow those tags over time as more pillars are established, more keystone content is created, that would actually benefit us for suggestive-related content and that type of play.

**Colin Lateano:** The only tag we have right now that we track is developer, because we haven't evolved to have a matrix tagging system yet on our blog.

**Colin Lateano:** So this is all fresh, and you can definitely lead that for us and help us establish our developer content tagging strategy.

**Jason Gong:** I think it's all very straightforward. I do have questions on the actual kind of content though, because I think Vivian and her team have reviewed a few at this point, so we'd love to hear some feedback.

**Jason Gong:** But as far as like overall strategy, pretty clear.

**Colin Lateano:** The actual content is Vivian's area. But next week we'll also have a product marketing manager joining, and Michael will start attending to help discuss reviews.

**Colin Lateano:** But one thing also is this meeting should probably not be the formal review of individual content.

**Colin Lateano:** I think this should be more stand-up, weekly check-ins, round-up, because if we're going to start pushing batches, this whole meeting will just be discussions on individual article and that type of thing.

**Colin Lateano:** But for now, while we're still establishing ground rules, I waive my time.

**Vivian Hoang:** On the content side, you saw Michael's feedback.

**Vivian Hoang:** We really need to get a better understanding of the brand messaging, how we present ourselves as a CMS, because we don't want conflicting viewpoints across different pieces of content.

**Vivian Hoang:** So I think, yeah, having the PMM team and Michael share those guidelines with you will be helpful.

**Jason Gong:** That would be great. I know that's evolving for you guys as well. If you need help refreshing articles, that's something we're pretty good at. Let's schedule something to get into the weeds of the articles.

**Jason Gong:** From my side, this is great. It gives us clear lanes to keep publishing. One thing to chat about: we want to help you guys monitor LLM citations and mentions.

**Jason Gong:** What we set up was very much geared towards developers, and it would be helpful for the Webflow team to review to see if we're on the right page about the awareness we're trying to build. If you want us to monitor broader brand visibility beyond just developer mentions, that's also a discussion we can have.

**Vivian Hoang:** Yeah, I looked at the prompts.

**Vivian Hoang:** They look good from a developer persona standpoint.

**Vivian Hoang:** And, yeah, I think if you are working on, like, you know, brand visibility tracking, it be great to, like, just see how Webflow as a brand shows up for CMS in general, not just targeting, like, developer persona.

**Jason Gong:** I'll compile the list and share it with you.

**Jason Gong:** I'm not sure who on the Webflow team focuses on this, but from the SEO side, it's about the awareness layer — people searching or prompting about things that don't necessarily mention Webflow directly.

**Jason Gong:** But where it's actually more useful is when people search for "How much does Webflow cost?" or "Does Webflow offer this feature?" — that's probably what your product marketing team cares about. There's a huge volume of prompts there.

**Vivian Hoang:** Yeah, definitely.

**Vivian Hoang:** I am starting to think about that a lot more and, like, we are forming a strategy around it.

**Vivian Hoang:** So, like, I think if you can help us with, like, the brand tracking, that would be great.

**Vivian Hoang:** And then if your tool or whatever you're using can aggregate, like, citation sources, we can definitely pass that along to, like, our brand marketing team, like, community team.

**Vivian Hoang:** Just to see if, like, we can, you know, gain traction in, like, those external sources.

**Jason Gong:** I think that would be great. I have the founder of one of the tools in today to do an interview, but it's all so nascent — nobody really knows what they're doing yet.

**Jason Gong:** Essentially, everyone's trying to monitor what's cited and what's driving these answers.

**Jason Gong:** If you have an article that's being cited, great. If you don't, you should write it. If you have it but it's not ranking, you need to refresh, enrich, and build links.

**Jason Gong:** And when it's citing sources, getting yourself into those looks like a mix of link building and partnerships.

**Jason Gong:** I think right now, GrowthX is covering the, like, the stuff that...

**Jason Gong:** So...

**Jason Gong:** So...

**Jason Gong:** So...

**Jason Gong:** So...

**Jason Gong:** you.

**Jason Gong:** We'll publish, and then it sounds like you guys already have a team for link building and also CRAN, so we'll cover monitoring and then using that information to feed our kind of like backlogs of content for now.

**Jason Gong:** We'll go from there.

**Jason Gong:** I'll share a list of prompts and then you guys can improve and we'll start tracking it.

**Kirat Chhina:** Yeah, Jason, on the same theme, we also have tons of traffic coming to Webflow, so we can monitor these bots. I've been going deeper on this topic, looking at how ChatGPT has trended compared to Google as a crawler.

**Kirat Chhina:** We serve thousands of gigabytes of data, in fact terabytes of data. It's interesting that ChatGPT has grown 10x.

**Kirat Chhina:** on Webflow properties in just a few months in terms of bandwidth and requests. Google crawler has remained static, though we've seen other bots from Meta become fairly aggressive.

**Kirat Chhina:** We've got some interesting learnings there. Another thing you'd probably be interested in: traffic is shifting to direct more than coming from search engine result pages.

**Kirat Chhina:** You can see the impact of ChatGPT flowing through here.

**Jason Gong:** Yeah, I mean, I think we have access to search console and then we have Google.

**Kirat Chhina:** But I'm not talking about webflow.com.

**Kirat Chhina:** Of course, you have access.

**Jason Gong:** I'm talking about all the other sites.

**Jason Gong:** Oh, right.

**Kirat Chhina:** You see everything.

**Kirat Chhina:** Okay, sorry.

**Kirat Chhina:** We see millions of sites.

**Jason Gong:** So that's...

**Kirat Chhina:** I know, valuable data.

**Kirat Chhina:** But we were thinking of some kind of thought leadership articles, et cetera, in this space, and I've been kind of digging in.

**Jason Gong:** Let's do something there.

**Jason Gong:** What these tools lack is the network effect to correlate all this stuff.

**Jason Gong:** What you see is referrer equals ChatGPT, but you have no idea what prompt drove it.

**Jason Gong:** But there's a way to correlate that if you're tracking all the prompts over time.

**Jason Gong:** And tracking referral traffic over time to understand volume. But nobody's done that yet.

**Jason Gong:** We've looked at a bunch of tools.

**Jason Gong:** Some tools have something close to that, but they're very slow. There's a tool called Scrunch that could work. If you want to publish a concept together, let's do it.

**Vivian Hoang:** Yeah.

**Jason Gong:** I think we have clear action items on integrations, the blog, and LLM monitoring.

**Jason Gong:** We'll push on that. There were some earlier ideas when we first started chatting about the docs.

**Jason Gong:** But it sounds like that whole part is being restructured. When that has a stable form, we can discuss code snippets and other details.

**Jason Gong:** But for now, we'll focus on the other clusters.

**Jason Gong:** Cool.

**Colin Lateano:** That's the best way to start. We'll bridge back to the learn and guide sections of the dev site relatively soon, but we've nailed down these two sections. I think it's better to start there and expand over the summer as we approach other content sections.

**Jason Gong:** Yeah, that makes sense.

**Jason Gong:** All right, I think we're clear. I appreciate all this. I know it's time spent aligning, which is very helpful, and now we're clear on what to do. I'll schedule something to review the content in more detail, and then we'll chat later.

**Vivian Hoang:** Sounds good.

**Colin Lateano:** Thanks. Appreciate it, Jason.
