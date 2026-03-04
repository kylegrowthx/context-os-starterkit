# Webflow <> GrowthX Weekly Sync

<metadata>
date: 2025-06-25
time: 17:30 UTC
duration: 33 minutes
organizer: jason@growthx.ai
participants: Jason Gong (GrowthX), Vivian Hoang (Webflow), Luke Stahl (Webflow)
fathom_recording_id: 70518017
fathom_url: https://fathom.video/calls/335165683
share_url: https://fathom.video/share/16LZAdeLGErFkXA2qTRUqsarqVoF_imv
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX and Webflow discussed progress on AI-generated integration pages and editorial content strategy. GrowthX demonstrated improved accuracy on various integration types (Stripe, Instagram, Zoho Flow, Donately) and is segmenting integrations by importance to prioritize editing. They've categorized editorial content into three buckets—SEO-focused, Reddit-style, and Hacker News-style—with Luke Stahl building a developer persona guide and AI reference guide to improve writing quality for developers. Key next steps include Jason sending new integration page batches for review, sharing an editorial topics list for approval, and providing access to the prompt tracking dashboard and AEO resources.

---

## Context

This is a weekly sync between GrowthX (a B2B content marketing agency) and Webflow (a no-code web platform). GrowthX is executing a major content initiative for Webflow that includes hundreds of AI-generated integration pages (connecting Webflow to external tools like Stripe, Instagram, Zapier, etc.) and thematic editorial content targeting different audiences. The meeting follows a previous content alignment call where Luke Stahl was onboarded; he's now actively involved in defining how GrowthX should write for Webflow's developer audience. Meg Murray (product/design lead) is currently at an offsite and is blocking the Webflow project setup decision in Figma/Webflow, so the team is waiting for her input on whether to import styles or add GrowthX to an existing Webflow project.

---

## Relevance

### To GrowthX Delivery

- AI validation workflow is maturing: GrowthX demonstrated improved accuracy on a representative slice of integration types, with human review catching edge cases (e.g., Donately, Supabase) where generation may be incomplete.
- Developer-focused content requires specialized knowledge: Luke is building an 18-page AI reference guide condensing best practices for writing to developers—this is now a gating input for GrowthX's prompts.
- Integration prioritization model working: Segmenting by "importance" to de-prioritize long-tail integrations (200+ of ~700 may not be relevant) reduces scope and improves quality ROI.
- Code snippet validation tools needed: Jason is exploring Cursor/V0 to validate generated code at scale, moving beyond human code review.

### To CheckThat

- AEO opportunity in developer education: GrowthX is building Hacker News-style content involving expert interviews with Webflow's core platform team, creating original research rather than curated content.
- Prompt auditing continues: GrowthX is now iterating prompts with client-provided frameworks (Webflow's developer persona, editorial guides) rather than generic models.

### To GrowthX Business Development

- Webflow engagement is high-touch and slow: Project dependencies (Meg's design decision) and topic-level vetting is slowing publication velocity; this is a complex customer management situation.
- Expansion opportunity: Webflow is open to docs support work (mentioned but not yet scoped), which could be a higher-margin service than content creation.
- Reference potential: Webflow's willingness to invest in developer personas and custom writing guides suggests a strong partnership and potential co-marketing content.

---

## Overview

- GrowthX is making progress on integration pages, with improved accuracy for various integration types
- Editorial content strategy is being refined, categorized into SEO, Reddit-style, and Hacker News-style content
- Webflow team to provide more guidance on developer-focused content and product positioning
- Need for careful vetting of integration topics to ensure relevance to Webflow's current offerings

---

## Key Topics

### Integration Page Progress

  - Reviewed examples of integration pages (Stripe, Instagram, Zoho Flow, Donately)
  - AI-generated content showing improved accuracy for different integration types
  - Segmenting integrations by importance for prioritized editing
  - Discussion on validating integration functionality and relevance to Webflow

### Content Strategy and Categorization

  - Content mapped into three categories: SEO-focused, Reddit-style, and Hacker News-style
  - SEO and Reddit-style content ready for production
  - Hacker News-style content requires more development, involving expert interviews

### Product Understanding and Alignment

  - Identified need for better understanding of Webflow's developer-focused products (e.g., Webflow Cloud)
  - Luke Stahl developing a developer persona guide and AI reference guide for writing to developers
  - Discussion on relevance of certain topics (e.g., Angular CMS) to Webflow's current offerings

### AI and Code Snippet Generation

  - GrowthX using a mix of OpenAI and Anthropic models for content generation
  - Exploring methods to validate generated code snippets, potentially using tools like Cursor

---

## Action Items

**Jason Gong (GrowthX)**
- Send new batch of integration pages for Webflow team review
- Follow up w/ Meg in Slack re: Webflow project import/migration
- Share list of editorial topics for Webflow team approval
- Give Vivian access to prompt tracking dashboard
- Share SEO primer & 40-min founder chat recording w/ Webflow team

**Vivian Hoang (Webflow)**
- Review new batch of integration pages when received from Jason

**Luke Stahl (Webflow)**
- Finish draft of developer persona guide, share w/ team for review
- Complete AI ref guide for dev writing, get approval before sharing

---

## Transcript

**Jason Gong:** Hello, how's it going?

**Jason Gong:** Do any of you live in, or I guess Vivian, I know you live in the Marin, but do you live in the Bay Area?

**Luke Stahl:** No, no, I'm north of Chicago, so I'm in the Midwest.

**Jason Gong:** So, Luke, Colin, Sydney, and I met up yesterday to talk through content. Colin can't make it but will watch the recording. TLDR, we looked through the Stripe article.

**Jason Gong:** I think at a high level it seemed very happy. The main question for us was whether it would get longer tail integrations right—ones that aren't super straightforward. Instagram was an example. What does it even mean to integrate Instagram with Webflow? At first we thought maybe the pixel or embedding, but actually it's about embedding the feed widget in rich text. We wanted to test our workflow across a representative slice of different integration types to show you the accuracy is improving. We reviewed Stripe yesterday and it was pretty good. Instagram was interesting because it's not super clear to a human either. The main thing for search is embedding a widget for the post, or using the API for entire feeds. Our model got that right and referenced the right API docs from Facebook since Instagram doesn't have their own docs. It even caught Instagram shopping features you could integrate. At least at a topic level, it covered it well. We didn't do human review yet, but this gave us confidence on these kinds of integrations.

**Jason Gong:** Another category we looked at: products that are pretty broad, like Zoho. We want to break these apart and have integration pages for sub-products. Zoho Flow is an example—when our model writes about Zoho Flow, it correctly limits scope to just that product, not Zoho broadly. It links to Zoho Flow in your marketplace and compares it to Zapier. When it talks about the API, it covers data syncing. This one may or may not be perfect—we need to tune it—but the high-level approach is good. Similar idea with Stripe: we could break it into Stripe Checkout, Stripe Payments, Stripe Risk, each with separate pages.

**Jason Gong:** One thing we talked about last week: our writing was too high-level. So this week we went deeper—we want sections about integrating to be more specific. Instead of just linking to Webflow's Content API docs, we reference the actual endpoints you'd use. That's why these look different. The last one we reviewed was Donately, which is a longer tail product without a huge doc site. Our model got it right. We structure these starting with the low-code version—if you can embed HTML or use a marketplace app, write about that first, then move to API for developers. It looks largely good. Directionally, our workflow is getting different integration categories right. We've also started segmenting integrations by importance—we'll prioritize editing the important ones, and since we're publishing hundreds, we'll edit the long tail stuff last.

**Jason Gong:** I also tested Supabase—not the most straightforward one. It would involve syncing the CMS with a Supabase table. The point is, there are a few hundred integrations, categorically quite different from each other, and we're able to generate content for each type.

**Luke Stahl:** I have a question since I'm new here. These integration pages look like just a logo and a sentence, then you go externally to the integration's docs. How did you determine which integrations should be on the page? Who verified they actually work beyond just sticking an icon and linking outward? As a developer, I see a logo, then I'm on Stripe's docs—there's no detail as to what will actually work with Webflow or how to build it. I might need to talk to Colin about this.

**Jason Gong:** So Webflow has an old integrations directory under the university that we're improving. We validated our list three ways: one, we used existing Webflow pages that made sense to improve; two, we checked if there's already a marketplace app for the tool—that suggests integration makes sense; three, we crawled Zapier, Make, N8N to see what gets traffic. That gave us about 700 integrations. We started with the safe ones. I'm guessing 100-200 don't actually make sense, but our approach is we'll create them, see if they work, and if not, we have other content to work on for you.

**Luke Stahl:** I need to figure out who decided what goes on that old page. Stripe's just an icon and two links to external docs. I get the marketplace side because you install within Webflow. But this is just pointing to Stripe's docs without description. We should have content explaining how to actually do it. I don't think there's a verification process behind this. Are we publishing things we're not certain work? Is Colin vetting every single one?

**Jason Gong:** Yeah, that's a good question.

**Jason Gong:** I think at some point somebody floated the idea of like, I think I'd have encouraged that you guys know, you know, all the embeds and integrations people do already.

**Jason Gong:** And you can kind of use that to at least validate, like, what in this list makes sense.

**Jason Gong:** But I do think we should go through that.

**Jason Gong:** That process.

**Jason Gong:** I will say there's at least like a hundred here that seem like no brainers, but I guess, you know, I'll leave that up to you to decide.

**Jason Gong:** Like, at least for me, like these ones all make sense, you know, and then once we start getting to like the more long tail stuff, yeah, I think probably should, you know, look through them a little bit deeper.

**Jason Gong:** Sure.

**Jason Gong:** Like, type four makes sense.

**Jason Gong:** You know, you're like a lot of these is literally just like, they're embeddable on a site and it's like, you know, talk about how you would do that with Webflow, you know, there's probably some slice of the users that like search up and care about that.

**Luke Stahl:** Yeah.

**Jason Gong:** Like this one should probably be a few different pages.

**Jason Gong:** Yeah.

**Jason Gong:** But anyway, maybe that answers your question.

**Luke Stahl:** Yeah, it was, it was, it was more me just kind of thinking out loud here, knowing that I need to do a little bit more learning on my end.

**Jason Gong:** Yeah.

**Luke Stahl:** Yeah.

**Luke Stahl:** Not trying to derail things by any means.

**Luke Stahl:** It was just more of a.

**Luke Stahl:** How did we even decide this stuff of prior?

**Jason Gong:** I think about that too.

**Jason Gong:** guess it's like, you know, when I read this, it seems logical, but like, how do I validate how we're doing that now?

**Jason Gong:** I mean, there's a human in the loop at the end to ultimately check it, but like, we're validating by like, you know, restricting all of this.

**Jason Gong:** Like, you won't see a link to anything other than Webflow and the tool that we're attempting to integrate with.

**Jason Gong:** So I guess that's one way we control for it.

**Jason Gong:** But I mean, I guess there's always a risk.

**Jason Gong:** It just makes up something random.

**Jason Gong:** So at least for now, our process is catching that at the end when we review.

**Luke Stahl:** Okay.

**Jason Gong:** Yeah, so I guess where this is at, I think we'll shoot over another batch.

**Jason Gong:** Again, like we didn't go into line edits yesterday, but it seemed like at least.

**Jason Gong:** And Colin read through the Stripe one and was reasonably happy with it.

**Jason Gong:** So we'll still send those your way.

**Jason Gong:** And then as far as the website goes, we're still waiting on Meg to, I don't know, I guess it seemed like it could have gone two ways.

**Jason Gong:** One of like, you'll somehow import your style into our Webflow project, or you'll just add us to some other Webflow project and we'll like migrate all the stuff we already built.

**Jason Gong:** In there, but we are still waiting for Meg on that.

**Jason Gong:** So I guess I'll follow up in Slack or something.

**Luke Stahl:** Yeah.

**Luke Stahl:** So, you know, Meg is at, she's in San Fran at like an offsite type thing.

**Jason Gong:** So she might be slow to respond this week.

**Luke Stahl:** So if she doesn't get it back to it, it'd probably be something next week.

**Jason Gong:** Okay.

**Jason Gong:** I mean, I just want to make sure, like, we're not, I mean, at this point, I don't think we're blocking anything.

**Jason Gong:** So we'll, and we're not blocked either.

**Jason Gong:** Like we can get all these pages up.

**Jason Gong:** It's just like, they won't be live and indexed.

**Jason Gong:** We make it look nice, and then, you know, you guys reverse proxy to it.

**Jason Gong:** Yeah, so that's integrations.

**Jason Gong:** And then with content, the editorial content, again, just to look at Vivian, I guess yesterday we spent time kind of showing a few of the clusters we mapped out.

**Jason Gong:** We kind of had this, like, rough heuristic of, like, you know, some things are kind of SEO, kind of thinking about the audience.

**Jason Gong:** Some things are, you know, hey, if I was writing for a Reddit-type audience, what would be interesting?

**Jason Gong:** And then the last bucket, like, very challenging to write, but something they'll kind of attempt to iterate on is kind of writing for an audience where you need more novel content that's, you know, talking about something new from a different angle for the Hacker News audience.

**Jason Gong:** And we've, I don't know, Sydney, if you have a link, I don't have it handy, but we've, like, kind of segmented all of our content that we've mapped out into those.

**Jason Gong:** Um, and I guess our, our approach will be to like, I mean, the, the bread and butter stuff is like here, um, the Reddit stuff as well.

**Jason Gong:** And then the kind of hack news content, I think we want it to kind of just kick off.

**Jason Gong:** Like, I don't think we'll be able to create that one overnight, but it'll essentially involve like a kind of picking a topic first, finding the right person kind of on your team.

**Jason Gong:** Who's actually an expert at it.

**Jason Gong:** I'm almost doing like a little interview with them and then trying to use that as like the base material to, to create, um, a piece of content.

**Jason Gong:** That's a little bit more, uh, opinionated.

**Jason Gong:** Um, so that's where we end up there.

**Jason Gong:** Um, we, uh, also had a discussion.

**Jason Gong:** Do you have a Google sheet?

**Jason Gong:** I think that was the one I looked at yesterday, Sydney.

**Jason Gong:** Oh, okay.

**Jason Gong:** So, um, let's see.

**Jason Gong:** Luke had a thought around, uh, how do you like this by cluster?

**Jason Gong:** Oh, this is by cluster.

**Jason Gong:** Okay.

**Jason Gong:** Um, yeah, like Luke had a thought around.

**Jason Gong:** Unlike some of these topics are like pretty high level, like, you know, how do they relate to Webflow?

**Jason Gong:** You know, like we have, what is the REST API?

**Jason Gong:** Like what exactly is the kind of connection to Webflow, right?

**Jason Gong:** Like, okay, Webflow has a REST API, but like, you know, like what's the purpose?

**Jason Gong:** And I think at least our approach is, you know, there are topics that relate to me building a website or kind of having a presence on the internet that relate to Webflow.

**Jason Gong:** And in each of these clusters, there's like some stuff that's like more directly related, like what CMS has the best API or something like, I'm just making that up.

**Jason Gong:** Like that's more bottom of the funnel.

**Jason Gong:** And then there's going to be some stuff at the top of the funnel that honestly is like not super related in terms of to your product, but it gives you kind of topic authority there.

**Jason Gong:** So that the stuff you write for the bottom of the funnel, you know, does rank was kind of our approach.

**Jason Gong:** I can't remember where we left it off, Luke.

**Jason Gong:** Like whether...

**Jason Gong:** whether...

**Jason Gong:** whether...

**Jason Gong:** You guys were okay with that, or you guys were going to think about it, you know, and kind of tell us, like, what sort of content you are okay kind of publishing.

**Jason Gong:** Our reference point is Cloudflare—they think of themselves as core to the web and publish anything related to that.

**Luke Stahl:** We left off needing to vet some topics. Angular CMS was in the mix, but we don't support Angular, so we shouldn't write about it. Obviously we can write "What is a REST API" and tie it back to Webflow APIs like I did at Builder—broad topic then specific to our APIs. But just writing about Angular CMS without support is weird. We'd be like HubSpot, just defining things with no tie-in.

**Vivian Hoang:** For topics that don't relate to us, like Angular CMS, maybe do a comparison article instead—Angular CMS versus Composable CMS.

**Jason Gong:** That makes sense. We'll send you drafts for vetting. It's not straightforward for every topic. I'm curious—isn't Webflow Cloud supposed to be a backend for anything? Wouldn't Angular work with that?

**Luke Stahl:** Webflow Cloud is getting there. Right now it supports React, Next.js, and Astro, but not everything. We're working toward being language and framework agnostic, but we're not there yet. Angular CMS is different—if you're building on Angular, we have an SDK for our CMS. Webflow Cloud is about building an app and deploying it through Webflow. They're separate use cases.

**Jason Gong:** Got it. Let's start with what you do today, then write Angular stuff later if you add it. SEO takes time to rank.

**Luke Stahl:** All headless CMS vendors write about every framework because headless means any tech stack should integrate. So they all write about it, making it harder to rank if you don't support it.

**Jason Gong:** I still have a gap understanding Webflow Cloud and how you position the developer-focused products. Did Michael share any docs? Do you have a roadmap? I don't really understand it that well and want to understand it more deeply.

**Luke Stahl:** I'm building out the developer persona, which I just started Monday. By end of week I'll share it for team review and feedback, then fine-tune it. I'm also creating an 18-page AI reference guide for writing to developers—similar to what I did at my previous company. It compiles my projects, resources, references, do's and don'ts, and things like Webflow Cloud and other projects in flight. I want some sign-off before I share it, but it should help you train your AI to speak to our devs better.

**Jason Gong:** That would be really cool. We keep some of this in our internal tool, but mostly at the company level—writing guides and style guides. Developer persona is different.

**Luke Stahl:** Right, and we have general company stuff that's great, but developer persona is its own thing.

**Jason Gong:** So for next steps: we'll send more integration pages. Go through them and give feedback if they're ready to publish, or flag issues. We get more feedback on calls and have to unpack it, so the more feedback upfront, the better. For editorial, we'll send a topics list for approval first, then you can review before we publish. We're tracking prompts and want to give you dashboard access soon. We also have an AEO primer and a 40-minute founder chat recording that helps explain what we're doing—I'll share those too.

**Luke Stahl:** Sounds good.

**Jason Gong:** I'll send the recording to Colin too.

**Luke Stahl:** Quick question on the AI side: who are you using to create code snippets? Claude?

**Jason Gong:** We don't have code snippets in these yet, but we have access to basically every model. We use our own platform now. For research we use Perplexity, and for writing it's a mix of OpenAI and Anthropic models.

**Luke Stahl:** Good to know. Anthropic models have better, more up-to-date code, usually Sonnet 3.5, though that changes over time. They just released some newer model. We used to prefer Anthropic over ChatGPT for code at Builder.

**Jason Gong:** Yeah, one thing we haven't tackled is helping you with docs. It's hard for a human editor to review code snippets and say "that looks right." We want to validate code by actually running it using Cursor or V0—"Is this real code that works?"—then run it to see what breaks. We'll go deep once we write code snippets.

**Luke Stahl:** That's a solid validation approach. Using Cursor to test it catches real snags.

**Jason Gong:** I use Cursor a lot too. We'll figure out what works for you.

**Luke Stahl:** Yeah, for sure. I'm working on that AI reference guide I mentioned—a compilation of my projects so I can feed it to my own ChatGPT and maybe share with you. It's how I talk about developers, write to devs, and who influences really good developer content. I want some review before sharing.

**Jason Gong:** That would be great.

**Luke Stahl:** Cool.

**Jason Gong:** Thanks for your time, Luke.

**Luke Stahl:** Good chatting.

**Jason Gong:** Bye, everyone.
