# Stackblitz <> GrowthX Weekly Sync

<metadata>
date: 2025-06-11
time: 16:12 UTC
duration: 10 minutes
organizer: mariana@growthxlabs.com
participants: Matthew Panzarino, Dave Capone, Mitchell Wright, Daniel Lopes, George Haikal, Alexander Berger, Marcel Santilli, Mariana Montezzana
fathom_recording_id: 67800796
fathom_url: https://fathom.video/calls/322501080
share_url: https://fathom.video/share/1WzGLYiRiAjTqe9eBBVVkRq_9Y_fM9LV
source: fathom
enriched_on: 2026-03-03 18:30 UTC
</metadata>

---

## Summary

Marcel and Mitchell aligned on StackBlitz's preference for a subdirectory implementation (/templates/) on the main domain for SEO benefits, with the GrowthX team transitioning the demo from V0 to Bolt for internal StackBlitz approval. The 4-week project will focus on handoff-ready deliverables including a Bolt-like repo, data model documentation, sample pages, example websites, sample prompts, and optionally the Supabase instance. Marcel will prepare a detailed list of deliverables to align expectations before finalizing the handoff strategy.

---

## Context

GrowthX is building a large-scale website template generation system for StackBlitz, focusing on long-tail keyword opportunities discovered through research (e.g., "notary website templates" with 1,800 monthly searches and keyword difficulty of 8). The engagement identified niche website templates as a high-potential use case with millions of long-tail search variations and minimal competition. This weekly sync serves to clarify implementation strategy, timeline, and handoff expectations as the project moves toward completion, with StackBlitz indicating limited interest in a long-term partnership but recognizing the value of the research and insights GrowthX provided to identify the use case.

---

## Relevance

- **To GrowthX Delivery:** The project validates GrowthX's research methodology for identifying untapped keyword opportunities in niche categories. The workflow of starting from a best-practice frontend repo and adapting for different brands and use cases could become a repeatable service model for template-based content generation.
- **To CheckThat:** The website templates use case demonstrates a large, underserved SEO opportunity with millions of long-tail variations. The insights from session data analysis align with CheckThat's visibility indexing mission and could inform AEO strategy for similar niches.
- **To GrowthX Business Development:** Mitchell Wright (StackBlitz) indicated internally the team is "not likely open to continuing partnership long-term," signaling this engagement will close in ~4 weeks. However, the research and insights delivered have proven value, and StackBlitz may serve as a reference case for similar template-based or niche category projects.

---

## Overview

- StackBlitz prefers subdirectory implementation (/templates/) on main domain for SEO benefits
- Project to wrap up in \~4 weeks; focus on handoff-ready deliverables
- Need to migrate from V0 to Bolt for internal StackBlitz approval
- Clarification needed on final deliverables; Marcel to provide detailed list

---

## Key Topics

### Implementation Strategy

  - Three potential paths discussed:
    1.  Speed-optimized proof of concept
    2.  Subdomain implementation (bolt-like instance)
    3.  Subdirectory implementation (preferred)
  - StackBlitz favors subdirectory (/templates/) on main domain for SEO
  - Importance of making community content highly visible (cf. VZero, Lovable)

### Project Timeline and Expectations

  - \~4 week timeframe for project completion
  - Focus on creating handoff-ready deliverables
  - StackBlitz team not likely open to continuing partnership long-term
  - Need for clear, itemized list of deliverables from GrowthX

### Technical Considerations

  - Current demo built with V0, not Bolt (StackBlitz's product)
  - Internal StackBlitz team sensitive to use of non-Bolt tools
  - GrowthX to migrate/rebuild demo using Bolt for better reception
  - Mitchell open to V0 if it expedites process; prioritizes having a workable repo

### Value Proposition and Insights

  - GrowthX provided valuable insights through research and data analysis
  - Identified website templates (esp. niche types) as high-potential use case
  - Example: "notary website templates" - 1,800 monthly searches, keyword difficulty of 8
  - Millions of long-tail searches for various website template categories
  - Strategy involves scaling to thousands of high-quality templates
  - Proposed workflow: Start with best-practice frontend repo, adapt for different use cases

### Deliverables Discussion

  - Repo with Bolt-like experience, implementable in subdirectory
  - Details on overall data model for pages
  - Sample pages with example websites
  - Sample prompts for generation
  - Potentially transferable Supabase instance
  - Comprehensive strategy for scaling template generation

---

## Action Items

**Marcel Santilli (GrowthX)**
- Convert current site to more Bolt-branded repo OR replicate site using Bolt

- Prepare handoff materials (repo, data model, samples) for subdirectory implementation

- Create list of deliverables for handoff (repo w/ Bolt-like exp, data model details, sample pages/websites, sample prompt)

---

## Transcript
**Marcel Santilli:** For example, with argument is that there's kind of two paths here, right?

**Marcel Santilli:** And we discussed last week was do we want to have a path where we're just optimizing for speed just to prove out the value and show the signals and show this thing working?

**Marcel Santilli:** There's a second path, which is like you get approval on your end to throw this in a subdomain and we make this look more like a bolt instance, you know?

**Marcel Santilli:** And so then the domain is not even relevant at all.

**Marcel Santilli:** And then the third would be putting it in a subdirectory, which would be the ideal from an SEO and, you know, and integrate it more with the bolt experience on the homepage a bit more, right?

**Marcel Santilli:** Like, at least link to it a bit more.

**Marcel Santilli:** But even just having it as a subdirectory would go like, be like massive, right?

**Marcel Santilli:** So if you, you know, what VZero and Lovable are doing essentially where like the community stuff is pretty, pretty in your face.

**Marcel Santilli:** It's impossible to miss essentially.

**Mitchell Wright:** I mean, I think for us doing something like orphaned pages on the main domain is probably what I would like to go with.

**Mitchell Wright:** So that's where, like, having the data model so that we could know what we would need to build as far as what are the different pieces, right, that would plug into whatever kind of we put on the site.

**Mitchell Wright:** I think that's kind of the main thing.

**Mitchell Wright:** So you're saying subdomain or subdirectory?

**Mitchell Wright:** A directory. It'll be on our main domain slash templates slash whatever is kind of how I'm envisioning it because I think that will give us the best results from an SEO perspective.

**Mitchell Wright:** And then that's, you know, the best opportunity for us to show that, like, this was a good partnership, actually.

**Marcel Santilli:** Yeah, yeah.

**Marcel Santilli:** Okay, so what do you think, let's call it in the next four weeks would be, and it's okay if the answer is like, sorry, dude, we're just going to take this, get as much value as we can, we paid good money and call it a day.

**Marcel Santilli:** Or do you see this as like, should we in our mental model be, let's set what we want in the next four weeks to have done and shipped and proven in order to continue?

**Marcel Santilli:** Or you're thinking more of like, and it's okay either way, right? I just want to clarify there's kind of two modes of operations. One is it goes super fast, so there's enough signals so that in four weeks we can prove this out and then figure out the long-term sustainable path. The other is getting this to as handoff-ready as possible in the next four weeks. Those are just slightly different ways that we can operate.

**Mitchell Wright:** I don't see internally people being open to continuing. That's the vibe.

**Mitchell Wright:** I think this looks really good, but this obviously was built with V0, not Bolt. That's another thing — I can't show this to anyone internally because they're not going to like that.

**Mitchell Wright:** I personally don't care because I'm like, let's get something done and start getting results. But if I go show people, they're going to be like, we're definitely not working with these people ever again. They're not even using their own product to build the stuff they're asking us to build.

**Marcel Santilli:** But then the website itself — this is the next thing I was going to show you. This is an example of one of the websites that we built, and this is fully on Bolt. It's mostly in one shot.

**Mitchell Wright:** I get what you're saying. Yeah, that makes sense.

**Marcel Santilli:** Based on our conversation last week, it was optimized for getting the right site and the right experience in place. I'm totally fine with moving forward with either approach, but I understand it's the kind of thing that people internally would not like.

**Marcel Santilli:** So let us regroup internally. I think what we could do is turn this over the next week as a more Bolt-branded repo, or try to replicate this using Bolt itself.

**Mitchell Wright:** If it's easier and faster for you guys in V0, feel free. As long as we have a repo at the end of the day, that's what I care about. Whatever helps you guys move faster, feel free.

**Mitchell Wright:** Okay, perfect.

**Marcel Santilli:** That sounds good. Okay, so I'll follow up with the details. What I'm hearing is as we wrap up the project over the next three to four weeks, the handoffs will be: a repo with an experience that looks a lot more like Bolt that you can put in a subdirectory, details on the overall data model of those pages, a few sample pages with sample websites, and a sample prompt that we can hand off.

**Mitchell Wright:** Yeah, so what does that look like as far as number of pages that we're actually putting here?

**Mitchell Wright:** I guess my question is, what are we actually, like, what's the result here?

**Mitchell Wright:** Like, is it the site that you're building, or is it the actual, like, generated pages?

**Marcel Santilli:** Yeah, I think there's a bit of a disconnect. It's easy to look at this and go, "This is the site," but it's informed by a lot of insight, a lot of research, and workflows that will inform scaling this up. Obviously, you all can do that as well. But the insight here is what I think is most valuable — we figured out what the use case was, which your data science team didn't have as much clarity on.

**Marcel Santilli:** We processed a ton of session data and figured out that lending pages and website templates were a huge use case we can double down on. Then we figured out there are long-tail keywords. For instance, "notary website templates" gets 1,800 searches a month and has a keyword difficulty of eight.

**Marcel Santilli:** There is literally millions and millions of searches of long-tail website templates for every single category possible.

**Marcel Santilli:** And there's very little competition for it.

**Marcel Santilli:** And so then it just becomes, how do you scale this to thousands and thousands of templates that are actually really, really, really good?

**Marcel Santilli:** That was the whole engagement, right? The long-term plan is to scale that with humans in the loop — produce these templates and build them as starter kits so they start from a common place, not from a blank slate. Ideally, you take a repo that already has frontend best practices baked in, then adapt it to different brands and use cases, add different content, and create the descriptions.

**Marcel Santilli:** What I would do in your case from this handoff is to say you'll need to hire somebody to scale this out. You'll have the strategy, the website built out, the template. You can connect to your own Supabase instance or we can transfer ownership. It should be pretty plug and play, and we'll get this to a deliverable state and publishing the site in four weeks.

**Mitchell Wright:** I think it would be great if you could put together a list of the deliverables we're handing off, just so we're very clear on what that will look like and then go from there.

**Marcel Santilli:** Yeah, that sounds good. We'll follow up.

**Mitchell Wright:** Sounds good. Thanks, I appreciate it. Bye.

**Mariana Montezzana:** Bye.
