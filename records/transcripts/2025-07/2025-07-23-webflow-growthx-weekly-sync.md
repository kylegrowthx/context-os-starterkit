# Webflow <> GrowthX Weekly Sync

<metadata>
date: 2025-07-23
time: 17:31 UTC
duration: 31 minutes
organizer: jason@growthx.ai
participants: Jason Gong (GrowthX), Sydney Go (GrowthX), Colin Lateano (Webflow)
fathom_recording_id: 76022695
fathom_url: https://fathom.video/calls/359257001
share_url: https://fathom.video/share/v-i7fwePNzm2pDSi3yuoVdqZVVmxsgMe
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

GrowthX and Webflow reviewed progress on the live integrations page—now accessible with CMS access and API key support coming for GrowthX. The team discussed research limitations affecting integration page accuracy (especially Zapier and Medium content) and agreed to tighten domain/URL filtering. Strategically, both teams are shifting editorial focus away from broad, mixed-format topics toward separate SEO-focused articles and deeper developer guides, with new content pillars around subscription services, usage-based billing, and global e-commerce.

---

## Context

GrowthX is Webflow's content delivery partner on the integration pages project, producing both integration page content and editorial guides. This is a weekly sync between Jason Gong (GrowthX lead) and Colin Lateano (Webflow dev relations) to align on deliverables, editorial direction, and process refinements. The relationship is active and strategic—Webflow is planning a full site redesign and relies on GrowthX to manage content quality and workflow. Sydney Go from GrowthX joined for research and editorial discussion. The meeting took place the week before a Webflow conference where a full site redesign would be announced.

---

## Relevance

**To GrowthX Delivery:**
- Research tooling limitations (Perplexity, OpenAI, ChatGPT) don't support granular URL/domain filtering—GrowthX needs custom post-processing to prevent hallucinations about third-party tool integrations like Zapier.
- Editorial strategy pivot from mixed-purpose content to segmented approach: SEO articles (definitions only) vs. developer guides (practical Reddit-tier how-tos).
- New content pillars: subscription services w/ Stripe, usage-based billing, global e-commerce / localization.
- Zach (Webflow dev rel) reviews integration pages; Vic (tech writer) is heads-down on product launches. Expect slower review velocity in the near term.

**To GrowthX Business Development:**
- Webflow has approved programmatic CMS and API access for GrowthX—signals investment in scale and trust.
- Full website redesign underway; integration pages are part of larger brand refresh.
- Integration pages strategy: keep content pragmatic and avoid empty pages while structural issues are resolved.

**To CheckThat:**
- Media bias in AI research pipelines: Medium posts rank high in search results but lack official documentation. Tools like ChatGPT, Perplexity, and OpenAI don't offer subdomain/path-level filtering—surfaces AEO opportunity for domain authority and content freshness signals.

---

## Overview

- Integrations page is live at webflow.com/integrations with 5 pages ready for Zach's review; CMS and API access confirmed for GrowthX
- Research limitations with third-party AI tools (Perplexity, OpenAI) are causing inaccurate Zapier and Medium content; GrowthX implementing custom URL/domain filtering
- Editorial strategy pivot: splitting mixed-format content into separate SEO articles (definitions/descriptions) and developer guides (practical Reddit-tier how-tos)
- New content pillars approved: subscription services with Stripe+Webflow, usage-based billing, global e-commerce/localization
- Process improvement: use direct Slack/email links to Airtable queue instead of channel notifications; expect 2-4 pages reviewed per week from Zach and Vic

---

## Key Topics

### Integrations Page Launch

- Page is live at webflow.com/integrations with redirects from old university pages
- CMS migrated all previous data; GrowthX to receive invites for CMS and API key access
- Demo loom created by Corey for CMS management; Webflow team unhappy with template aesthetics but deferring changes to full site redesign planned for next phase
- Five integration pages (Medium, Stripe, and others) ready for Zach to review; Stripe flagged by Colin as acceptable

### Research and Content Accuracy Issues

- Research tools (Perplexity, OpenAI, ChatGPT) don't support granular URL/domain filtering—only high-level domain-level blacklist/whitelist
- Zapier content lacks accuracy because research is scoped only to Webflow and Zapier domains, preventing tools from knowing what Zapier actually integrates with
- Medium posts rank highly in SEO but lack official documentation; tool hallucinated Medium API capabilities after Medium deprecated the API
- GrowthX manually fixed structural issues to maintain velocity; need systemic fix on research side before volume scales

### Content Review Workflow

- Zach (most technical member of Webflow dev rel) is primary reviewer; Vic (tech writer) heads-down on agentic hosting launch
- Target: 2-4 pages reviewed per week; use direct Airtable links in Slack/DM rather than channel notifications
- GrowthX maintains content queue in ContentOS Airtable; Webflow team updates status or adds comments
- Colin will identify who reviews listicles/non-integration content and inform Jason

### Editorial Strategy Pivot

- Splitting one mixed-format article into two distinct content types: SEO articles (definitions, high-level) vs. developer guides (practical, Reddit-tier how-to)
- SEO articles: "What is composable commerce?"—focus on definition, not developer implementation
- Developer guides: practical walkthrough (e.g., "How to build a subscription membership site with Webflow + Stripe")—Reddit-level discussion of nuances and decisions
- Approved topics for developer guides: subscription services, usage-based billing, global e-commerce with localization
- Composable Commerce shelved as topic because Colin sees it as internal debate at Webflow; will propose alternative expert contributions later

---

## Action Items

**Jason Gong (GrowthX)**
- Set up integration account on GrowthX side
- Prepare batch of 3-4 SEO editorial articles for review
- Start creating guide on building subscription membership site with Webflow + Stripe

**Colin Lateano (Webflow)**
- Identify review team for listicle/non-integration SEO content and inform Jason
- Ensure GrowthX team receives CMS access invites by Friday morning; follow up with Corey if not sent

---

## Transcript

**Jason Gong:** Hey.

**Sydney Go:** Hey, how's it going?

**Jason Gong:** Pretty good. I don't think I've taken a call at home in a few weeks—I'm just always in the office now.

**Sydney Go:** That red pillow behind you is new, I think.

**Jason Gong:** Yeah, it's like a chair. I tried to get my dog to go on it, but he's just on the ground.

**Sydney Go:** I got a new perch for the cat on the window. Problem is, she has to jump on the shelf beside it first, and then she jumps on my head, which is always fun and surprising. She hasn't done it on a call yet, but the days are numbered.

**Jason Gong:** That's funny.

**Sydney Go:** Luke said he can't make the call.

**Jason Gong:** Yeah, I really want to try to get the editorial style tuned in. Did Zach review any other integration pages yet?

**Sydney Go:** It doesn't look like it. I checked last night and he hadn't.

**Jason Gong:** Is he in the channel? Sometimes I feel like it's just nicer to direct message them. Let's try to just send direct links in chat and DMs instead of relying on the Airtable.

**Sydney Go:** Okay.

**Jason Gong:** I find the Webflow team's more responsive to direct messages. For the editorial drafts—the "What Is Composable Commerce" article—it did a really good job on structure. When it came to listicles, it's still struggling. I had to generate it through ChatGPT and Perplexity.

**Sydney Go:** I've been trying to look for time to work on that, but I'm on calls generally from 7 to 12. I've never had this many calls in my life, to be completely honest.

**Jason Gong:** I've been working with the engineers to try to make the research piece better. Anyway, let's talk integrations. Zach reviewed Medium and flagged some structural issues, so I went back and redid some of that. We basically have five integration pages here for him to review. Is he the main reviewer now?

**Colin Lateano:** There are two members of my dev rel team right now. He's the most technical member. The other one is our current tech writer, Vic. She's heads down for the launch of our agentic hosting service because she also writes all the docs for product releases. So Zach was reviewing things and flagging them.

**Jason Gong:** That makes sense. We flagged a few things with the integration pages. When I think about how we do research, I actually don't think there's any way for the LLM to know what Zapier can even do, because we scoped the research only to the domain of the tool and the domain of Webflow. That's something I need to fix. And another problem is with Medium—it just starts citing Medium posts. Medium ranked highly in SEO and did a good job with it. The thing is, a lot of these tools do a bunch of SEO, and their blogs are vague about what their products can do.

**Jason Gong:** None of the deep research tools—Perplexity, ChatGPT, OpenAI—give you the ability to really granularly limit based on URL. They only have high-level domain blacklist/whitelist, not subdomain or path filtering. You can put instructions in the research prompt, but they don't respect it. So we need to do some stuff on our side. I think that'll fix problems like this. Medium had an API at some point, and now it doesn't. So the tool found old Medium posts from a long time ago, which is why that was in there. Anyway, we manually fixed a few just so we don't slow anything down. These ones are in our ContentOS Airtable and ready for Zach to review.

**Colin Lateano:** It looks like Stripe's already up. I was okay with Stripe because I'm pretty confident I know how those work. Integrations page is live. We migrated all the data from the previous university pages. As you want to upload your data, you replace them in the CMS. The demo Loom Corey made will be followed by another one on CMS management. I'm not happy with the template look, but we're doing a full revamp of the Webflow website, so you can change it after. Just accept that you have content now that can be logged and people can find it. Integrations is live, and it redirects, so all the old university pages now go to webflow.com/integrations.

**Jason Gong:** Oh, it's like live right now?

**Colin Lateano:** It is a sample one. I gave him two—Facebook and this one—so he should have put both in. You should get invites to the CMS to help manage this. Once you've accessed the CMS, you should be able to get an API key to manage it programmatically. If you really enjoy this kind of work, we also have an MCP server for CMS management on our public GitHub.

**Jason Gong:** Yeah, we can play with that. So I'm blocked until I get CMS access. Until we get the API key, we'll just import in batches via the CMS. No issues there. So we basically have five here for him to review. I'm going to ask—is he the main reviewer now?

**Colin Lateano:** I ran that through with the team at our last team meeting last Thursday. I asked everyone to please review 2 to 4 pages this week. Vic will probably get ahead of it at the end of the week, but Zach started, so that's great. I gave him the guides to go to the status and change it, or if you don't want to change it, put comments in.

**Jason Gong:** Sounds good. So we'll make sure there's always a queue, but sometimes we might grab a bunch and redo them when we find structural problems we think we can fix. I was going to ask if you wanted us to do a whole batch on things that are more straightforward to create, just so those pages don't look as empty.

**Colin Lateano:** I have no good opinion on that one. I'm hoping we can move up enough velocity that that won't be an issue.

**Jason Gong:** Got it. Great. So I think we're in a good place. I'll set up the integration account on our side. For editorial, so the main one is we're kind of taking the one Luke reviewed as the first calibration. I read through that, and I think my main thought is that this article has a weird purpose. I think the problem is we took a topic that was for SEO and we tried really hard to make it Reddit-tier, really wordy, and I don't think it serves any purpose super well. I kind of want to break it up almost because as a topic, it's trying to mix too many things together. There's quite a lot of SEO stuff here. These are the topics I want to do for SEO. And we already started on briefs for those—just like very basic SEO purpose. Like "What is composable commerce?"—it doesn't try to get into anything developer-centric. It's really just the definition. For the more developer chunk, I kind of want to try something a little bit more in depth. So I was wondering—if there's any, I don't know, if you have any thoughts for how we can seed it with more opinion from Webflow.

**Colin Lateano:** There definitely are people who could do this. The topic you're picking is a debate. I'm currently a dissenting party in this debate at Webflow. There's a fight happening about how we're going to handle the next era of composable commerce. It's about fundamental platform changes around dynamic binds and data layers versus live structure runtime requests. So how to design it the Webflow way is an ongoing conversation, but everyone agrees on what composable commerce is.

**Jason Gong:** That's really cool. What you just said—even if those become Zoom calls at some point—that would be like a Hacker News level debate. And then the best practices you're trying to share with the world—that's more of a Reddit level post. So we'll shelve that and pick something else. Is there any topic that's top of mind for you that you think would be a good candidate? Just because you guys are already thinking about it, where we can write something and get feedback for a Reddit-tier article.

**Colin Lateano:** I'm thinking. My head immediately goes back to the flywheel we talked about on integrations. I'm wondering if it would be an easy example to generate one of the sub-articles about how you would pull off one of those clever ones. But just how these things get made and all the nuances to consider is really interesting to people. And that is a Reddit post. Like: "Here's how I built a membership page for my monthly candy delivery service" or "How to build a subscription membership site with Webflow and Stripe." That would get a bunch of clicks on Reddit. Or usage-based billing and how you can understand that is also a really cool idea. Or global e-commerce is a really fun idea because we're very proud of our localization services. Being able to talk about how you can have products that go across different locales is a neat idea.

**Jason Gong:** Cool. Yeah, like, how would you build the subscription membership site? Yeah. Like if we had to pick an example—would you think more e-commerce or more like an information product, like a newsletter, or a course?

**Colin Lateano:** I think staying in the e-commerce realm would be fun. You could say how to build a monthly subscription service. You could also do something like how you would build a membership page or the back end of a membership system—where you log in and get to your member portal, check your active subscription status against your username and password, and see what your membership entitles you to. But just how these things get made is really interesting.

**Jason Gong:** I think this is easier because the LLM already has large language training on the most publicly available services. You just run Cursor docs or whoever you use on Stripe and Webflow and then ask, what else should I need to use to build this? This one is more of an exercise than facilitating a conversation and repackaging it to an article with seed information.

**Colin Lateano:** And the guide concept shouldn't be a step-by-step "here's the exact code you need to use." I think it really should be framed as inspirational—giving you a seed of an idea about how you could approach it and explaining why you'd want to think about it that way. That's Reddit thinking—I did these things, here's what happened, you could do it too. You don't need to lay out every command.

**Jason Gong:** Yeah, I agree. We don't have to nail down the framework. It could just be somewhat high level. I mean, it'd be good if you could pick one topic. But in general, this is a nice category of things. And the nice thing is we're already mapping that out because we're doing the integration pages. So happy to just start there. Do you know who would review listicles for SEO content?

**Colin Lateano:** No, I don't. I can ask Michael if he wants anyone to review it. I believe the way they operate is kind of just doing biopsies, but they're not going to review every single one.

**Jason Gong:** For our side, we'll just shoot over a batch—like three or four articles—and then you let us know what we need to do after that.

**Colin Lateano:** That'd be great. I'll figure out who's the review team for that service. If you do not get added to the CMS by Friday morning, let me know and I'll make sure Corey forces that.

**Jason Gong:** Sounds good. All right, thank you Colin.

**Colin Lateano:** Thank you.
