# Webflow <> GrowthX - Weekly Sync

<metadata>
date: 2025-09-24
time: 17:31 UTC
duration: 27 minutes
organizer: team@growthxlabs.com
participants: Jason Gong (GrowthX), Vivian Hoang (Webflow), Vic Plummer (Webflow), Luke Stahl (Webflow), Zach Plata (Webflow)
fathom_recording_id: 89569833
fathom_url: https://fathom.video/calls/418855631
share_url: https://fathom.video/share/wJ1kws4ecQNhwNz6BJPY1awLvQA5mCsX
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX and Webflow reviewed three active content initiatives: 30-40 integration pages per week targeting 300-400 of 600-700 mapped pages, SEO content in review with a need for brand-aligned visuals, and integration guides aiming for 3-5 per week with first draft ready by week's end. Webflow outlined code component requirements with a target of example components ready by end of October for WebflowConf, and the team agreed to prioritize Webflow-native solutions (Webflow Cloud, D1, KV, object storage) over generic alternatives.

---

## Context

This is a standing sync between GrowthX, a B2B content marketing agency, and Webflow, a no-code web design platform. GrowthX is handling multiple content and integration initiatives for Webflow: building integration guides (like Stripe + Webflow membership setups), creating SEO content to drive organic visibility, producing integration pages across dozens of third-party tools, and now expanding into code components. Jason Gong leads the GrowthX side; Vic Plummer and Luke Stahl are primary stakeholders from Webflow's product and content strategy teams, with Vivian Hoang managing visual/brand compliance and Zach Plata leading the code components effort.

---

## Relevance

### To GrowthX Delivery
- Operating at scale: 30-40 integration pages/week and 3-5 integration guides/week requires operational rigor to maintain quality
- Brand alignment is critical path: SEO articles blocked until Vivian can access brand guidelines and apply them consistently
- Component building is new domain: Zach's Shadcn PR provides reference; team needs Webflow's vision on component scope and presentation before full-scale production

### To GrowthX Business Development
- Account health: Client is actively shipping (code components launched this week) and expanding scope (adding component library, scaling guides from concept to 3-5/week)
- Expansion opportunity: If GrowthX can reliably deliver components at scale, this opens a new revenue line within the engagement

### To CheckThat
- Webflow Cloud positioning: Discussion emphasized recommending Webflow-native solutions (D1, KV, object storage) over Firebase/Supabase—relevant to AEO and developer education

---

## Overview

- GrowthX is currently focused on three main areas: integration pages, SEO content, and integration guides
- Code components project is in early stages; team to provide more specific guidance on requirements
- End of October target for having a set of example code components ready for WebflowConf
- SEO articles need adjustments to align with Webflow's brand guidelines for faster production

---

## Key Topics

### Integration Pages Progress

  - Team is producing 30-40 integration pages per week
  - Mapped out 600-700 potential pages; focusing on 300-400 that make most sense
  - Aiming to complete remaining pages and evaluate additional ones afterwards

### SEO Content Development

  - One article completed, several in review
  - Sydney leading this effort; async communication ongoing
  - Vivian highlighted need for visuals to align with Webflow's brand font and colors

### Integration Guides

  - Currently in early stages; aiming for 3-5 guides per week
  - Focus on Webflow-specific solutions (e.g., Webflow Cloud) when possible
  - Team to provide draft for review by end of the week

### Code Components Project

  - Zach shared PR for base Shadcn components as a starting point
  - Discussion on how to present components (e.g., individual vs. library approach)
  - Team to provide clearer vision and example of desired output
  - Target: Have a set of popular/desirable code components ready by end of October for WebflowConf

### SEO Article Refinements

  - Vivian shared feedback on brand alignment in thread
  - Luke emphasized importance of following brand guidelines for faster production
  - Composable Commerce and REST API articles approved; others pending review

---

## Action Items

**Zach Plata (Webflow)**
- Get PR in for base Shadcn components as example reference for Jason

**Vivian Hoang (Webflow)**
- Update visuals in SEO articles to match brand guidelines (fonts, colors)

**Jason Gong (GrowthX)**
- Give Vivian access to brand guidelines for SEO articles
- Clean up name field for integration pages (remove extra words like "animation")
- Type up meeting notes, update Colin, ask if he still wants to chat tomorrow

**Luke Stahl (Webflow)**
- Review remaining 3 SEO articles

---

## Transcript
**Vivian Hoang:** This meeting is being recorded.

**Jason Gong:** Hi.

**Jason Gong:** I wasn't sure if anyone was going to join because Colin said he wanted to move it, but I figured I'd just hang out. I know this company, Surge, but we took this crazy engagement with them where we're kind of just their head of marketing now, which I have to juggle with every other job I have.

**Vivian Hoang:** No, I didn't go in person, but yeah, a lot was going on that week with the conference. We migrated the site to a different project.

**Jason Gong:** I saw that. It's all in one now instead of like spread over a bunch, which has also taken a lot of work.

**Vivian Hoang:** Hey, Vic.

**Jason Gong:** I guess I could do the update anyway. I wasn't sure if Colin just wanted to do this tomorrow, but since you guys are here, we can.

**Vic Plummer:** Yeah, he's getting a little slammed. I think a quick update would be great.

**Jason Gong:** So I guess you guys don't typically join the calls, but like how we're structuring the work we do is just through these lanes.

**Jason Gong:** So at any given time, we're kind of working on two or three of them, and we'll shuffle priorities depending on what help you guys need the most. Right now the one that's the most mature is integration pages. We mapped out almost six or seven hundred, but there's maybe around three or four hundred that make sense to do, and then the rest we can debate once we get there. We're doing maybe 30 to 40 a week at the moment.

And then the other one is the SEO content. There's a little bit of back and forth figuring out what sort of content we wanted to do, and now we're kind of trying to wrap that up. We got one through the door and then we have a few in review. Sydney's the one that's owning that, so we'll probably chat about that async.

And then the last one is integration guides. This one's more in the early stages. Typically our process is we write one article—doesn't matter humans, AI, whatever—just to get it to the quality that you want. Once we do that, which we did with this integration like how to set up a membership site with Stripe and Webflow, we try to create a machine that can do that at higher scale.

**Jason Gong:** So that's high-level what we're doing right now—basically these three: SEO content, integrations, and integration guides. We have an update of how many we've done, and you can always keep a tab on that in the table. The guides themselves, we're not going to go through a ton of how to do this at scale on our end, but in case you care, you can see some of the problems we're having and how we're working through it.

The question is: when these guides link to code examples, would they be standalone or just within the text itself? We're still working through that, but we've aligned on: as much as possible, we won't pull code examples in here—we'll just link to the appropriate API docs and give a high-level overview of what's happening. So it would mostly not be possible to fully build it out just reading the article. It would serve as your entry point, highlighting the docs and the approach you'd have to take.

**Vic Plummer:** One thing I mentioned on our intro call last week is there's some guidance around products we'd want you to recommend first. So with Sydney's comment about using Webflow Cloud instead, we'd recommend using that—it's basically Cloudflare first, but with Webflow's platform it offers D1, KV, and object storage. Anytime you'd normally say use S3 or Firebase or Supabase, we'd want you to direct people to Webflow Cloud to keep them all in a Webflow solution. But if you guys have questions or ideas come up, please feel free to ping us.

**Jason Gong:** So we can say, yeah, that's a good use of it, or no, it's not. That makes sense. Yeah, whenever possible, we want to mention the Webflow way of doing it. But in general, I'm still not super happy with what our workflows are spitting out. We're targeting end of the week to have something good there. And this one's a little bit more effort to write at scale, so we're going to try to ramp up to maybe three to five a week, and once we get that stable, we can decide how to ramp further.

**Vic Plummer:** For each one that you're doing, you kind of recommend what to build, so you'd think you'd want us to have a first review of what is being put out by the end of this week?

**Jason Gong:** That would be good. I think Colin was trying not to have too many cooks in the kitchen, but this one is helpful to review. This is kind of the best part where we're at least trying to make our initial pass automated.

**Vic Plummer:** I'll put some of these comments back in my calendar to start repeating this, so we can give you guys significant feedback.

**Jason Gong:** Yeah, so that's mostly what we're doing on integrations. Components was the other one that Colin highlighted as interesting. My thought is we can totally do it, but I was trying to get a little bit more specific on what exactly we would create and how this would appear on the site.

**Vic Plummer:** So right now, this is from our Docs repo, and I'm happy to share that with you. It's kind of a JSON payload with metadata and the live example. We have a published Webflow site that actually uses the code component as well.

**Jason Gong:** So it doesn't have to be one-to-one. For example, if I was doing a three-column feature module, what exactly are the things I would need to create? I would obviously have to create the module and figure out a way to have one site that has that on it with many things.

**Vic Plummer:** That was our initial approach because we were kind of scrambling. Zach right now has a PR in that is a library of Shadcn components, so you don't have to make a single site for an accordion if they're all on one page. I think we can put our heads together about the best code components we'd want to see. We're trying to compete with Framer's code components. I don't really see a library from them right now though.

**Zach Plata:** Yeah, I don't think they have much. It'll just be the community providing resources. Jason, I can share something really quick. Like Vic mentioned, there's a PR out right now that pulls in some base Shadcn components—buttons, badges, and more complex ones like cards that give a good example. We could do something similar, and we can also create a gallery showing the various components that can be built. I included a reference link to a Google Doc that lays out caveats of how Webflow renders these code components. For example, accordions will be tricky to add in, but the doc explains why and how to work around it if you're using AI to scaffold Shadcn components. We can give you guardrails so they render cleaner and easier. We can absolutely get you in our workspace with a site where you can sync the code components over to Webflow and just drag and drop.

**Jason Gong:** And so then you don't have to fuss about the actual design of the site.

**Jason Gong:** Yeah, mean, I feel like the best thing is, like, if you could just share one version of what, like, one that you did looks like, then it'd be a lot easier for me to, like, replicate.

**Zach Plata:** For sure.

**Jason Gong:** Yeah, I think we should be able to get that PR in so that you have something to reference, but we'll include that link in the Notion doc.

**Jason Gong:** And then are you, like, envisioning, like, kind of the archetype of the component and just...

**Jason Gong:** Having one there, or would you have, like, for example, one of the examples you have is, like, a, you know, price and quote calculator.

**Jason Gong:** Like, for me, like, I don't know, this is, like, an archetype of, like, a form, for example, right?

**Jason Gong:** Like, would you want every kind of, like, reasonably interesting, like, fermentation of, like, a particular component in this library?

**Jason Gong:** Like, we would have a, you know, like, a lead form.

**Jason Gong:** would have a, you know, a branch not working.

**Jason Gong:** But, like, we would have every, you know, like, type of form, mostly because people search for it, right?

**Zach Plata:** And, like, we would probably find it useful.

**Zach Plata:** That'd be a good use case for sure. Like, this component can easily be adapted to include any kind of equation. This one's life insurance, but you could have something for a pricing table for SaaS plans. For Shadcn components that we can pull in, it makes sense to include that all in one project, one folder in that repo, so when you're exporting or importing into Webflow, you're pulling in all the Shadcn components from one library, rather than having a specific library for each component.

**Jason Gong:** Let me try and pull in that PR just so we can have something to reference.

**Zach Plata:** Yeah, exactly.

**Jason Gong:** That's where I think the more you guys can shape that, just because from our side, I don't have any context for it.

**Vic Plummer:** Yeah. I just wanted to show you the Framer Marketplace with the components there. These are components that people have already submitted. Some are monetized, some aren't. But I think maybe we can also start getting ideas from here in terms of what people would want to see, or what kind of package looks like. One thing is how do we want to present these, and Vivian's probably thinking about how this overlaps with the main Webflow templates.

**Vic Plummer:** Right now, the code components are not connected to the main Webflow, from what I understand.

**Vivian Hoang:** So I think there is work being done to migrate everything into a more unified marketplace experience, which will include components.

**Vivian Hoang:** John and Aaron from the marketplace team are starting to think about that.

**Vic Plummer:** For now, our goal is to seed interest in this very new product by providing examples. It wouldn't necessarily be a marketplace, but more inspirational—to get people excited without the nervousness of going straight to GitHub. We want to provide a better landing page on what you can do. What we're looking for is components that people would want to see.

**Jason Gong:** That makes sense. Just thinking about our engagement—if it's just a one-time thing with 30 components, I'm not sure that's the best approach. But if it's a code component equivalent of what's here or expanding Webflow's template library to include code versions, that's a lot more valuable.

**Vic Plummer:** Yeah, that's what will eventually happen. If we open it up, we'll need stuff there to begin with. Right now, the current examples are too one-off compared to the Shadcn components where there's multiple components within one.

**Jason Gong:** For example, if I was doing this for you, it's pretty clear that all we'd have to generate is the component itself and make sure it works. But depending on how you're planning to present this, I'm not sure if you want me to generate the entire folder with dependencies.

**Vic Plummer:** So what you mean is like a scaffold?

**Jason Gong:** Yeah, if you have a vision for what that might look like.

**Zach Plata:** Yeah, I think let's get the PR in so we have the base for the Shadcn components, and then you can just work off of that. For more complex ones from the framework marketplace, we can probably spin up a scaffold-like thing too.

**Vic Plummer:** Okay, that makes sense.

**Jason Gong:** Are there any deadlines or targets in your mind for what you want in this components starter pack?

**Vic Plummer:** We definitely shouldn't use the word marketplace because that would confuse people. For us, it's more like a starter pack so people can start riffing on their own. For WebflowConf, if we could have a set of examples, it would be good timing for anything you guys are planning.

**Luke Stahl:** Is end of October an unrealistic ask? We could have not all of them, but a chunk of the most popular or desirable code components. Would that be doable?

**Jason Gong:** Totally doable. It's just on our end we're using our engineering resources one lane at a time right now. They're on integration guides, but as soon as they're done, I'll get them on code components.

**Luke Stahl:** Because we just rolled out code components this week, and people are gonna start diving in. By end of month, having more components for them to use would be a great next step for product adoption.

**Jason Gong:** The last thing is the SEO articles. Is there anything to flag there?

**Vivian Hoang:** Yeah, I shared it in the thread, but there are some visuals in the articles that need to be in our brand font and colors.

**Luke Stahl:** If these things are applied, it will help get these to production faster because Vivian can actually stage them, versus me going to the content team asking for specific design work. We have reusable heroes that Vivian can use, so we could produce these at a faster pace if we tackle these brand guidelines.

**Jason Gong:** Yeah, I'll give you access to that.

**Luke Stahl:** The Composable Commerce and REST API articles are approved. I need to look at the other three.

**Jason Gong:** Awesome. I think we covered a lot. Tomorrow we'll probably get a little deeper into the integration.

**Vivian Hoang:** I also saw your comment in the channel about updating the page titles. We can do that pretty simply. We'd just need to make sure all the names in the field include just the plain name, not extra words like "animation."

**Jason Gong:** On our end, the main goal is to get the integration guides up and running, and then components is a second priority after that.

**Luke Stahl:** What is tomorrow's call?

**Jason Gong:** Colin couldn't make this one, and I think it might be almost exactly the same as what we talked about.

**Luke Stahl:** If it's going to be a duplicate, we might not need to have it. I'll take that internally and check with Colin.

**Jason Gong:** I'll type up the notes from this meeting, update Colin, and ask if he still wants to chat. Thank you all for your time.
