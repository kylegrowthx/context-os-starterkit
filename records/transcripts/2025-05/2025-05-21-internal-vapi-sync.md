# Internal Vapi sync

<metadata>
date: 2025-05-21
time: 18:30 UTC
duration: 30 minutes
organizer: Jürgen Linde (GrowthX)
participants: Jürgen Linde, Kirkland Gee, Matthew Alves-Hill
fathom_recording_id: 63985844
fathom_url: https://fathom.video/calls/306793003
share_url: https://fathom.video/share/JVVzTKZUog4dWTWvh7gnZg9dTFhQCcFB
source: fathom
enriched_on: 2026-03-04 17:30 UTC
</metadata>

---

## Summary

GrowthX's internal team synced on critical blockers for the Vapi programmatic pages project. One page is live but incomplete (contains mock-up elements); the team identified two main blockers — image generation standards and voice sample recording workflows — that must be resolved to scale programmatic page creation. The team agreed to prioritize launch velocity over perfection, with Matthew compiling keyword variations across medical, sales, and B2B tech verticals, Jürgen generating 10-15 persona images, and Kirkland coordinating with Daniel on project prioritization to establish a realistic delivery timeline.

---

## Context

This is an internal GrowthX sync on the Vapi engagement, a content marketing project focused on building programmatic pages for Vapi's AI voice agent product. Vapi is the external client and their team (particularly Jordan, the main contact) is eager to see programmatic pages launch. The team has been split between editorial content (which is progressing well) and programmatic pages (the higher-priority deliverable from Vapi's perspective). Kirkland Gee, the lead engineer, was out the previous week due to family medical issues, creating some backlog. Jürgen is acting as lead on the GrowthX side managing the client relationship, while Matthew handles keyword research and SEO strategy, and Kirkland owns the technical implementation of the programmatic workflow.

---

## Relevance

**To GrowthX Delivery:**
- Programmatic page workflows need to scale from 1 page live to hundreds of pages to meet client expectations and timeline. Image generation standards and voice sample recording processes are the blocking technical challenges.
- Team learned from Kirkland's ClickUp experience that long-tail keyword volume scales naturally; 1,000 pages vs. 100 pages has zero incremental cost when using JSON-driven page generation via static assets.
- Client would prefer speed and breadth (500+ keyword variations across medical, sales, B2B tech) over pixel-perfect design — "focus on scale instead of the nitty-gritty details."

**To GrowthX Business Development:**
- Vapi shows classic oversell/under-deliver dynamic: client expectations set higher than current delivery pace. Kirkland framed this as normal in growth-stage services and predicted it will resolve once programmatic pages launch at scale.
- Account health signal: client anxiety is high but team confidence is moderate. Marketing-side work (editorial) is proving GrowthX's competence; engineering-side work (programmatic) is proving the bottleneck.
- Client lacks attribution system to track conversion impact of organic traffic increases. Jürgen flagged opportunity to help Vapi set up basic attribution to demonstrate value and identify high-performing content categories.

**To CheckThat:**
- None identified in this call.

---

## Overview

- Programmatic page creation is a priority; one page live, more needed urgently
- Image generation and voice samples are key blockers for scaling programmatic pages
- Client (Vapi) is anxious for progress, particularly on programmatic pages
- Editorial content is progressing well, but programmatic pages are seen as higher value
- Team agreed to prioritize launch velocity over design perfection
- Matthew to compile extensive keyword variations across medical, sales, and B2B tech verticals
- Jürgen to generate 10-15 persona images using GPT/Image Journey
- Kirkland to confirm project prioritization and realistic timeline with Daniel

---

## Key Topics

### Programmatic Page Creation Status

One page is currently live but incomplete — it still contains mock-up elements and hasn't been finalized. Before the team can scale programmatic page creation, two critical technical blockers must be resolved:

1. **Image generation standards**: The mock-up used placeholder images that Ren generated, but there's no defined standard for how images should be sourced, generated, or styled at scale. Kirkland needs clarity from the team on whether Vapi wants AI-generated human faces, stock images, or another approach. Final decision: generate 10-15 reusable persona images and rotate them across pages rather than creating unique images per page.

2. **Voice sample recording workflow**: The live page includes audio samples of the AI voice agent in action, but recording and hosting custom audio files at scale is more complex than anticipated. Kirkland hasn't yet determined how to automate voice sample generation within the programmatic workflow. Potential solution: set up a script, record a call using Vapi's own API, and store the audio file for use on pages.

### Keyword Strategy for Programmatic Pages

The approach is long-tail keyword volume — generate hundreds of variations and let SEO performance data guide iterations (kill non-performing pages after 60-90 days). Matthew has done keyword research for medical, sales, and B2B tech verticals. Kirkland shared his ClickUp experience: he published 4,000 pages per month there, killed half a month later, and still generated significant traffic from ultra-specific long-tail keywords (e.g., "Packing Checklist for New York in February"). Recommendations: use ChatGPT to generate extensive lists, sort by search volume in SEMrush, focus on breadth. Matthew to compile a master list of AI voice agent use case variations from Airtable data.

### Client Expectations and Management

Jordan (Vapi's main contact) is excited about the project but pushing for constant visible progress. He's focused on programmatic pages as the high-value deliverable, while editorial content (which the team is shipping daily) is less important to him. Client mood: anxious but not angry. Kirkland's perspective from agency experience: this is normal for growth-stage deals — oversell followed by pressure to deliver. Once programmatic pages launch at scale, expectations will reset. The team's confidence: moderate. Engineering capacity is the real constraint, not marketing or SEO strategy.

### Strategic Account Insights

Vapi currently lacks an attribution system to track which content drives signups. Their goal is to increase organic signups from their website. They have strong traction on social media and brand searches, but want to improve organic channel performance. Team opportunity: offer to help Vapi implement basic attribution (e.g., UTM parameters, conversion tracking) so they can see the ROI of the content work. This would also help GrowthX demonstrate impact.

### Technical SEO Setup

Vapi's docs pages are indexed and properly discoverable. The sitemap exists at docs.vapi.ai/sitemap.xml, and the pricing page is indexed (verified via site:vapi.ai/pricing search). No technical SEO concerns. Kirkland walked the team through how to verify these facts quickly (site: operator, sitemap.xml URL check) so they can confidently answer client questions in the future.

### Process and Workflow

The programmatic page workflow is template-driven. Matthew provides use case keywords → workflow generates all page content (text, call-to-action, configuration) → pages are deployed via JSON files to a static site generator. Static assets (feature icons, images) stay the same across all pages; only the dynamic content (headline, description, specific voice agent configuration) changes. This is what allows scale without incremental effort.

### Next Steps and Action Items

- **Matthew**: Compile a comprehensive list of AI voice agent use case keywords across medical, sales, and B2B tech. Variations on specialties (eye doctor, neurologist, etc.). Use ChatGPT to generate breadth, then cross-reference with Airtable data.
- **Jürgen**: Generate 10-15 persona images using Image Journey's GPT integration. Similar style to the current "Susan" image on Vapi's site. Mix of industries/professions. These will be rotated through programmatic pages.
- **Jürgen**: Respond to the external Slack channel confirming docs sitemap existence and pricing page indexation status.
- **Kirkland**: Discuss project priorities, capacity, and realistic timelines with Daniel (Vapi's technical lead). Return to team with updated delivery estimates for next programmatic pages.
- **Optional opportunity**: Explore helping Vapi set up a basic attribution system so they can track organic traffic → signup conversion and better understand the ROI of the content work.

---

## Action Items

**Matthew Alves-Hill (GrowthX)**
- Create list of keywords for programmatic pages. Use ChatGPT to generate extensive list of AI voice agent use cases. Include variations focused on medical, sales, and B2B tech verticals. Be specific: eye doctor, neurologist, etc. Pull reference data from Airtable. Kirkland's guidance: don't stress keyword research granularity — go wide rather than narrow, 500+ keywords is fine. Conversions often come from 2-click/month pages.

- Create variations/chat examples for Kirkland. Build a database of ideas for programmatic pages to demonstrate breadth of approach to client.

**Jürgen Linde (GrowthX)**
- Generate 10-15 persona images using GPT on Image Journey. Match the style of the current "Susan" image on Vapi's site. Mix of industries and professions (medical, sales, tech backgrounds). Goal: have 10-15 reusable persona assets to cycle through programmatic pages rather than generating unique images per page.

- Respond in external Slack channel addressing Bronco's questions: confirm docs sitemap exists at docs.vapi.ai/sitemap.xml and pricing page is indexed (verified via site:vapi.ai/pricing search). Not a concern; no action needed.

**Kirkland Gee (GrowthX)**
- Discuss Vapi project priorities and engineering capacity with Daniel. Report back to team with a realistic timeline for when additional programmatic pages can go live. Current state: only 1 page live (incomplete, contains mock-up elements). Main blockers: image generation standards and voice sample recording workflow. Action: resolve these blockers with team so workflow can be templated for scale.

---

## Transcript

**Kirkland Gee:** So that being said, with Vapi, I know Branko had a few things here, but I'm definitely a little unclear on, like, where we're at in terms of next steps for programmatic, just because I was out of office all last week.

**Jürgen Linde:** I know there's a page live.

**Jürgen Linde:** I still had a couple of outstanding questions, but, like...

**Jürgen Linde:** Yeah, I was hoping to find out from you, because as far as I know, we have only published one post, one page.

**Jürgen Linde:** And I just want to know when the next few pages would go live.

**Jürgen Linde:** That's kind of the only thing I need to...

**Kirkland Gee:** I'm trying to find the thread where I was asking about this.

**Kirkland Gee:** Basically, there were two, I mean, part of it is just trying to manage time.

**Kirkland Gee:** I'm actually the only engineer that's not in San Francisco this week.

**Kirkland Gee:** I wasn't able to make it because of some medical stuff with my family, but now I'm trying to manage, you know, all these different things.

**Kirkland Gee:** Let's see.

**Kirkland Gee:** Here's this.

**Jürgen Linde:** Well, I know so far that we have one page live, but it's not like final state.

**Jürgen Linde:** There's some mock-up stuff still in there.

**Jürgen Linde:** So I don't even know that's technically done.

**Jürgen Linde:** Okay.

**Jürgen Linde:** Okay.

**Kirkland Gee:** Um.

**Kirkland Gee:** Yeah, so the two pieces that I need to sort out before I can just make a bunch of these is images, which I was trying to understand from Ren and Bronco what the plan was there, and Bronco didn't actually know, because those were just images that Ren came up, generated for the mock-up, and he's like, oh, we'll just use ones like that.

**Kirkland Gee:** But like, it's not that simple.

**Kirkland Gee:** Like, I need to know where they're being generated from, what the standards are, like what we want those to be, which I don't really have a clear answer on.

**Kirkland Gee:** And then the other one is voice samples.

**Kirkland Gee:** That's still, we talked about not doing that, but that's still a part of the one page that's live.

**Kirkland Gee:** And the issue is, to generate voice samples is weirdly more complicated than just like doing a live call demo, for example.

**Kirkland Gee:** And right now, the page is set up to just pull an audio file and play that live when you click the button.

**Kirkland Gee:** But that means the audio file has to be custom.

**Kirkland Gee:** I got to figure out some way to record all of those.

**Kirkland Gee:** So I don't know if I can just record a call.

**Kirkland Gee:** I have to figure that piece out of what that needs to look like.

**Jürgen Linde:** I think the idea is that you can build your own voice agent.

**Jürgen Linde:** And you can just, whenever you have a use case, just build, like, you can, like, replicate a specific script and just ask it, like, this is what you can just say when you answer the call.

**Jürgen Linde:** This is what you have to say when you, like, answer a question.

**Jürgen Linde:** And then it can be pretty much just self-autopilot in that sense.

**Jürgen Linde:** Yeah.

**Kirkland Gee:** I guess the issue is the way the page has been built.

**Jürgen Linde:** Let me just show my screen.

**Kirkland Gee:** Because these are the only things stopping me from being able to finish the workflow.

**Kirkland Gee:** This is just connected to a voice agent with a configuration.

**Kirkland Gee:** That's fine.

**Kirkland Gee:** All this configuration is pretty creatable.

**Kirkland Gee:** It's not that hard to do.

**Kirkland Gee:** All this text is generatable.

**Kirkland Gee:** All these images are going to be static.

**Kirkland Gee:** But this image here, how is this going to be generated?

**Kirkland Gee:** This here?

**Kirkland Gee:** Right now, it's just one image for everything.

**Kirkland Gee:** I assume we don't want to do that.

**Kirkland Gee:** I don't know what those images need to be.

**Kirkland Gee:** And then this here, this is Susan with GrowthX AI.

**Kirkland Gee:** This audio sample is playing an audio file that lives somewhere.

**Kirkland Gee:** And if we're going to be like, I don't know how to create those at scale just yet.

**Kirkland Gee:** Like for every, is that just a part of the workflow?

**Kirkland Gee:** Is that based on these?

**Kirkland Gee:** I know that you can start a call, I guess, and record it.

**Kirkland Gee:** So I think it's doable.

**Kirkland Gee:** I just haven't figured that out.

**Jürgen Linde:** I think there's, it's pretty simple just to set up like a script and then you can replicate that in the record.

**Jürgen Linde:** Audio file, but I don't know how you can record the file without whatever software you should use.

**Kirkland Gee:** Right, it's like, how do I, in our workflow, record that and get the URL for that audio file back in order to put into the content?

**Jürgen Linde:** I'm sure it's doable.

**Kirkland Gee:** Like I said, it's not.

**Kirkland Gee:** Those are the two things that I don't have figured out.

**Jürgen Linde:** Pretty much everything else makes sense.

**Jürgen Linde:** Yeah, sounds like something we can ask about, be like, how do they, or like, how do you like prompt a call and then get that audio file stored somewhere?

**Jürgen Linde:** Maybe that's something we can ask them tomorrow.

**Kirkland Gee:** think you necessarily need to ask them because I know you can do it and I'm sure I can figure it out.

**Kirkland Gee:** I'm just letting you guys be like, I haven't sat down to sort that out yet.

**Kirkland Gee:** The only thing I really do need to know is like how they want to do images.

**Kirkland Gee:** Like, do they want AI-generated fake human images for that?

**Kirkland Gee:** Or are there some other kind of asset we want to create?

**Jürgen Linde:** I will tell you right now, based off of what they've created so far, their blog pages are basic.

**Jürgen Linde:** They don't seem to have a design team that's nitpicky about quality.

**Jürgen Linde:** They just kind of go with it.

**Jürgen Linde:** So I don't think they'd complain about images that aren't perfect.

**Jürgen Linde:** I think they'd easily gloss over that.

**Jürgen Linde:** Do you guys have an opinion on what you want to do with images?

**Jürgen Linde:** I'd say something that just has a human face in it that looks natural — doesn't have 60 fingers on one hand.

**Kirkland Gee:** Okay.

**Matthew Alves-Hill:** I think from the previous interactions with them, Jordan is so eager to see pages going out that if the images aren't perfect, he won't care. I think we should find the simplest way to do it and prioritize getting pages live rather than letting that block us. All the pressure is on the programmatic side from them. They keep asking, "Why aren't pages up?"

**Jürgen Linde:** Yeah, he doesn't care about the technicalities. He just wants to see stuff going up.

**Kirkland Gee:** Do you guys have a list of keywords for those pages?

**Kirkland Gee:** Essentially, all I need is an input for the workflow. I'm going to build a workflow in AirOps where you put in the use case, click play, and get the complete page output that goes into Qwilr, right?

**Jürgen Linde:** Yeah, we have the Airtable map. We have use cases per industry, and each industry has sub-use cases that could become supporting keywords.

**Matthew Alves-Hill:** Yeah, I think the discussion we haven't had yet with Bronco is the keyword strategy for programmatic pages. We've got the editorial side figured out, but we're waiting for direction on the programmatic strategy.

**Matthew Alves-Hill:** I haven't even had that chat with Bronco yet, but I've done a lot of keyword research for healthcare, sales, and other verticals from an editorial perspective. I don't know if Bronco has a different approach based on his experience.

**Jürgen Linde:** Matt, I think what you can just do to get this thing rolling is to take that industry, the core keyword, take the sub-use cases from what you have on an Airtable, throw them in something and just get a ball of keywords and sub-keywords, and then throw that together, and then we can use that for the programmatic pages.

**Kirkland Gee:** Let me give you some advice from my experience with programmatic pages at ClickUp. I generally erred on the side of publish and iterate. I was publishing 4,000 pages a month there, and we'd kill half of them a month later. But even keywords with zero search volume might generate 50 to 100 page views.

**Kirkland Gee:** Here's the key: if it reasonably makes sense that someone might want an AI voice agent for a use case, don't stress about it. The difference between 100 pages and 1,000 pages is zero work — Marcus has set this up so you're just dropping JSON files into the repo and pages exist. Go wider rather than super specific.

**Kirkland Gee:** From what you're telling me, the client would be much happier if you said, "We want to move fast and we have 500 keyword ideas. If in 60-90 days they're not performing, we kill them and swap in 100 new ones." It's no additional work for us now that the setup is done.

**Matthew Alves-Hill:** Yeah, and even with the editorial perspective, there's so much long tail. Conversions often come from pages that get two clicks a month. So I need to build a list of every conceivable medical AI assistant variation.

**Kirkland Gee:** What I'd do is sit down with ChatGPT and have it generate more and more variations until you have hundreds. Then throw that comma-separated list into SEMrush, get search volumes, and sort by priority.

**Jürgen Linde:** That's literally what Marcel did with the original Airtable. He told me, "I'm going to do this dirty" — threw it in ChatGPT and created the initial cluster that way.

**Kirkland Gee:** The complexity isn't in keyword research — it's in getting a page that works and knowing what to change to differentiate it. Keyword research is the easiest part. Just go more specific rather than less specific. At ClickUp, I did packing checklists for every single month to New York — "Packing Checklist for New York in February" — and all of them got their own specific clicks. Cost was zero, benefit was real.

**Matthew Alves-Hill:** So narrow.

**Kirkland Gee:** So your next step is compile a list of AI voice agent use cases — those are the inputs we need. My idea is that each use case input feeds into a workflow that generates the entire page. Each piece of content is differentiated, but most visual assets stay the same — feature images, icons, etc.

**Kirkland Gee:** The easiest approach is to generate 10-15 different persona images upfront and rotate them through pages.

**Matthew Alves-Hill:** Just industry-specific — use the same ones and loop through them.

**Jürgen Linde:** It's not going to matter at the end of the day.

**Kirkland Gee:** Exactly. From what you're telling me about the client, they'd much rather have us do that than spend time making unique images for every page.

**Jürgen Linde:** They focus on scale, not nitty-gritty design details. That approach will work.

**Matthew Alves-Hill:** I'm sending you the Airtable link. The Specific Grid has all the broadest industries, and the use cases are there so you can reference them when thinking about images and personas.

**Kirkland Gee:** Got it. Now, something else from Bronco's notes — he had a technical question about indexing the docs pages.

**Jürgen Linde:** Yeah, we talked about this yesterday. Bronco asked a follow-up question about docs indexing.

**Kirkland Gee:** His question was: "We recently updated our docs. Do we have/need a sitemap for docs so the right ones show up?"

**Jürgen Linde:** Matthew, when you did the site audit, was docs indexing an issue?

**Matthew Alves-Hill:** No, they were already indexed. They already have a sitemap.

**Kirkland Gee:** Let me show you how to quickly answer questions like this. Check if a sitemap exists by going to the URL and adding /sitemap.xml at the end. In this case, docs.vapi.ai/sitemap.xml is there, so it's fine. To check if the pricing page is indexed, use a site: search. site:vapi.ai/pricing — yes, it's indexed.

**Kirkland Gee:** Short answer to both questions: we have a sitemap, pricing page is indexed. Not a concern.

**Kirkland Gee:** Whether the pricing page is getting traffic is a different question.

**Jürgen Linde:** So the key question we need to answer tomorrow is: when are the next programmatic pages going to be live? We've only published one. The editorial stuff is done and dusted — we're doing that fine. But Bronco isn't here to tell us the timeline.

**Kirkland Gee:** I'm juggling a bunch of things, so let me talk to Daniel about priorities and get back to you on timing.

**Jürgen Linde:** I can tell them we're working on it. I'll say, "Bronco's not available right now, but here's what we're doing in advance to get this live as soon as we get back on track."

**Kirkland Gee:** Can you guys help me generate those 10-15 persona images? Do we have access to GPT for image generation?

**Jürgen Linde:** We have GPT on Image Journey.

**Kirkland Gee:** Perfect. If you guys can just get me 10-15 good-enough persona images, I can focus on the workflow. Similar style to the "Susan" image that's on the site now.

**Matthew Alves-Hill:** Susan — though she's got a man's voice in the demo, which is interesting.

**Kirkland Gee:** Yeah, if you can work on that, I'm going to touch base with Daniel right now about priorities and timelines, then I'll get back to you on when I can have this done.

**Jürgen Linde:** Matt's doing as much as he can on the editorial side and supporting work. I'm available if you need anything else.

**Matthew Alves-Hill:** From my conversations with Bronco, the client has been anxious about progress.

**Jürgen Linde:** Not angry, just anxious and wanting to see momentum.

**Kirkland Gee:** They were sold something and experienced something different. Did you guys come from agencies before?

**Jürgen Linde:** I did.

**Kirkland Gee:** This is textbook oversell-and-under-deliver. It's par for the course in growth-stage deals. Hopefully we can course-correct.

**Jürgen Linde:** In my opinion, if you start low, it's easy to blow expectations away later. It feels better than executing well from day one.

**Kirkland Gee:** I was the SEO director at an agency, then went to ClickUp, and now I'm here. I fought with sales for years at ClickUp — they grew from zero to $20M+ ARR. Our co-founder was great at selling but not at selling services we could actually deliver. This situation with Vapi is textbook, but it's not as bad as it could be. The issue isn't that we can't deliver what was sold — it's that we don't have engineering capacity because we're onboarding new engineers and juggling multiple projects.

**Kirkland Gee:** Look, you guys are doing great. Keep doing what you're doing. Don't kill yourselves over this.

**Jürgen Linde:** I think we'll be fine.

**Kirkland Gee:** If we get these programmatic pages out, I think we'll be fine. The hard part is that the client expects constant effort. They don't understand that once the workflow is set up, it's done — pages just auto-generate. That's a sales/expectations issue, not a capability issue.

**Jürgen Linde:** I'm managing expectations by explaining that editorial works over time — you don't publish pages and immediately get traffic. As long as they see visible progress (pages going live), it feels like we're delivering.

**Matthew Alves-Hill:** We're giving good signals now — editorial pages go out every day. Jordan is fixated on programmatic pages, though. That's his priority.

**Jürgen Linde:** He wants to see progress because he's excited about the project, not because he's impatient. It's a little of both.

**Kirkland Gee:** Okay, let me go talk to Daniel about priorities and timelines, and I'll follow up with you guys soon. In the meantime, can you respond to the external channel about the docs sitemap and pricing page indexing? Not a concern.

**Matthew Alves-Hill:** Do we have conversion data from Vapi yet?

**Jürgen Linde:** No, they don't have attribution in place, so they don't even know where signups are coming from. Their goal is just to increase organic signups. They have strong social traction and brand search volume, but they want to improve organic.

**Matthew Alves-Hill:** Bummer. I was hoping to pull conversion insights.

**Jürgen Linde:** I still need to ask them if we can help set up a basic attribution system, which would help them understand the impact of the content work.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Yeah, it wouldn't.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** Yeah, okay.

**Matthew Alves-Hill:** Bummer.

**Matthew Alves-Hill:** I'll compile the keyword variations tomorrow so we can show them we have a database of ideas. This approach is keyword-research-focused instead of listing gaps. Many gap keywords have the wrong intent. This makes sense and gives us easier articles to write. Let me know if you see anything to add. Hopefully we get on a normal publishing cadence.

**Jürgen Linde:** The engineering team is concerned about resource allocation. But I think that can be fixed.
