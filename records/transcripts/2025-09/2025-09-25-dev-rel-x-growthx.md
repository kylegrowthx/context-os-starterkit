# dev rel x Growthx

<metadata>
date: 2025-09-25
time: 18:01 UTC
duration: 30 minutes
organizer: jason@growthx.ai
participants: Jason Gong (GrowthX), Vic Plummer, Colin Lateano, Luke Stahl
fathom_recording_id: 89907882
fathom_url: https://fathom.video/calls/421585911
share_url: https://fathom.video/share/CSKEzP6h4_9TbZMGf85kvRvgXq8aZmvy
source: fathom
enriched_on: 2025-03-03 15:42 UTC
</metadata>

---

## Summary

Jason Gong and the Webflow DevRel team (Colin Lateano, Vic Plummer, Luke Stahl) discussed a strategic pivot from SEO content to developer enablement, focusing on code components and React apps for the Webflow Marketplace. GrowthX committed to delivering 30 code components by Halloween (with at least 10 being "materially interesting") along with integration pages and use case guides, with Colin requesting timeline estimates for resource planning. The team outlined a phased approach: shipping raw code snippets immediately through a developers subdomain or GitHub, with full marketplace integration coming in "months," and discussed potential for future React app components with backend functionality.

---

## Context

Webflow is a leading website builder platform with an expanding developer ecosystem. Colin Lateano leads DevRel and is shifting the team's focus away from organic/SEO-driven content toward technical enablement — specifically building a developer-centric component marketplace. This represents a significant strategic pivot from the previous engagement model. GrowthX's previous work focused on integration guides and SEO content; this call clarified that the partnership is now centered on generating code components and guiding Webflow's product-led growth motion through a searchable, customizable marketplace. The meeting happened because Jason Gong (GrowthX account owner) needed to align on scope, complexity, timelines, and resource allocation before committing to delivery targets.

---

## Relevance

**To GrowthX Delivery:**
- Major engagement pivot from SEO/listicle work to component generation and app development. Requires engineering resources, not just writers.
- Scoping: Components are "easier" than guides in terms of QA (just verify they upload and render), but require technical integration knowledge with Webflow's code component system.
- Capacity planning critical: Jason needs to assess current team bandwidth and provide timeline estimates early next week to set client expectations.
- Integration guides and use-case documentation remain high-priority evergreen content; Colin sees these as discovery top-of-funnel and wants to maintain pace.

**To GrowthX Business Development:**
- Account expansion opportunity if GrowthX can deliver on component targets. Colin signaled willingness to trade SEO budget for components/apps work if necessary.
- Long-term potential: React apps with backend functionality opens new revenue/scope discussions (Figma Make Marketplace is the strategic reference).
- Risk: If GrowthX can't deliver timeline estimates early, Webflow may hire additional resources internally or shift to a different vendor.

**To CheckThat:**
- No direct CheckThat mention in this call, but developer enablement and product-led growth through a component marketplace could be future channel for AI visibility tools and prompt optimization.

---

## Overview

- Shifting focus from SEO content to developer enablement, particularly code components and React apps
- Aiming for 30 code components by Halloween, with at least 10 being "materially interesting"
- GrowthX to provide timeline estimates for deliverables across different workstreams (integrations, guides, components)
- Webflow planning a marketplace for components, including both native Webflow and code-based options

---

## Key Topics

### Integration and Guide Progress

  - Published multiple integrations, targeting 20-30 per week
  - Working on workflow to generate integration guides more efficiently
  - SEO articles progressing well, with some brand guideline adjustments

### Code Components Vision

  - Focus on generating raw code snippets for functional components
  - Components will eventually be listed individually in Webflow Marketplace
  - Aiming for flexibility and creativity beyond basic UI elements (e.g., "glassy button")
  - Future potential to include React apps with backend functionality

### Marketplace Integration

  - Planning to break up existing component libraries into individual, searchable listings
  - Will include both native Webflow components and code-based options
  - Long-term goal: surfacing components directly in Webflow designer

### Resource Allocation

  - Prioritizing integration pages and use cases as evergreen content
  - Considering reallocating resources from SEO to generative work for components and apps
  - GrowthX to assess current capacity and provide timeline estimates

### Project Timeline and Expectations

  - No firm deadline for marketplace launch (expected in "months")
  - Interim solution: DevRel team to showcase components through developers subdomain or GitHub
  - Targeting 30 components (10 "materially interesting") by Halloween, but flexible based on difficulty

---

## Action Items

**Jason Gong (GrowthX)**
- Create proof of concept for code components (button and table). Verify upload/functionality in Webflow system to understand integration requirements before full production work.
- Estimate timeline for integration docs, guides, and code components across all workstreams. Send estimates to Colin early next week to inform DevRel roadmap and set expectations with internal teams.
- Check Colin's Wednesday availability via Slack and reschedule next meeting accordingly given DevRel team offsite next week.

**Colin Lateano (Webflow)**
- Confirm Wednesday availability slot for follow-up meeting with Jason via Slack. Backup option: Friday or following week if Wednesday doesn't work.

---

## Transcript
**Colin Lateano:** It's crazy. The whole week of missed work, apparently, is how everyone's acting.

**Colin Lateano:** Conference was good.

**Colin Lateano:** Conference was good and got a lot of great conversations in.

**Colin Lateano:** How are you doing?

**Colin Lateano:** How's everything happening over here?

**Jason Gong:** Yeah, we're doing great. We're doing some stuff with a guy from Webflow, promoting a little workshop with him.

**Jason Gong:** One of my other clients is Surge AI, and our engagement with them is quite large.

**Jason Gong:** We almost kind of just own their marketing, which is kind of a weird engagement, but it is what it is.

**Colin Lateano:** Yeah, Roger.

**Jason Gong:** Cool. So we did an update yesterday. Should I go through that?

**Colin Lateano:** I did not get a chance to watch. I read a summary, but if you want to voice it over, that'd be really nice.

**Jason Gong:** Yeah, I can skim really quickly over that, and then we can go deeper into any of the areas you're interested in.

**Jason Gong:** So we've talked through integration stuff. We've published a bunch.

**Jason Gong:** I think we got the new API key from your new project to speed that up. Send that over.

**Jason Gong:** I checked it yesterday, and it seemed like we had a lot of integrations. There were more integrations than we thought before that we held back because we just wanted to tweak a little bit.

**Jason Gong:** So that's why I think we're trying to target 30 or 40 a week, but maybe it's closer to 20-something.

**Jason Gong:** So that's going. I shared kind of a draft of what our workflows are spitting out, but I haven't sent any of that over because we've been iterating on that internally.

**Jason Gong:** Just for context, the first one I did was kind of manual. Now we're creating a workflow that could do these at scale. We're trying to target tomorrow to have a version you can look at. Once you're happy with it, we'll start doing maybe three to five a week to start.

**Jason Gong:** For components, we spent a bunch of time yesterday talking through that. I'm pretty sure we can do it. There was an open question around what exactly the scaffolding or website would look like.

**Jason Gong:** Are we generating just 30 or 40 lines like ShadCN, or something more involved? The GitHub repo had everything from dependencies to READMEs — a lot more.

**Jason Gong:** Knowing what it would look like on the page would be helpful.

**Colin Lateano:** Is it helpful if I walk through that right now?

**Jason Gong:** Yeah, that'd be helpful.

**Jason Gong:** Other than that, we had a few articles in the SEO bucket.

**Jason Gong:** Luke had some comments, but largely they seem pretty good. Vivian was on the call yesterday to note brand guidelines for images that we'll follow going forward. That was basically the call yesterday.

**Colin Lateano:** Okay.

**Colin Lateano:** Code components will be stepwise. The first answer to your question is we're aiming closer to just the code necessary to have that work in the Webflow code component container — like in ShadCN, it's just 30 lines of code and just works.

**Colin Lateano:** But depending on the use case the AI identifies, there may need to be a guide to explain if it uses a CMS resource. For example, if you're making a component that pulls a profile of a collection item, you'd probably want to document that it uses that resource.

**Colin Lateano:** Err toward the raw code — you don't need to build a whole site. Right now, we don't have a great way to market these yet. We might make an example landing page of a few so people can see them and choose.

**Colin Lateano:** Eventually, I want the actual marketplace to feature a list of components with standard listings showing the code, like ShadCN. For now, it's going to be hacky. The code is fine enough with READMEs explaining what it does and its intent. As DevRel, we're trying to figure out how to merchandise this before the official Marketplace pages exist.

**Jason Gong:** What would the Marketplace look like? Is it a subsection of made-in-webflow or templates?

**Colin Lateano:** Made-in-webflow is being merged into other parts, but yes. What I want to do is take our libraries example and instead of a full site, render it as embedded Webflow with the component name and eventually a description of what it does.

**Colin Lateano:** People can then say, I want this on my site. Right now, libraries is a collection, but we're breaking it up into individual component parts with the marketplace team. Code components fit nicely into that vision where you can pull individual components.

**Jason Gong:** Are you imagining a world where you'll have, say, a two-column pricing page for SaaS with Webflow variants and code component variants all in one place?

**Colin Lateano:** The goal is we're installing a search system on the marketplace.

**Colin Lateano:** You'd see a searchable library like Framer's, where you filter and search for things like "pricing table".

**Colin Lateano:** You click on it to see a render of how it works, and there's a button to see the code to insert as a code component. For now, there won't be a button to insert directly into the designer — that's more complex. I'd like it to eventually download to your library, but that's being worked through.

**Jason Gong:** You're still kind of in this spot where it's for organic reach and enablement.

**Colin Lateano:** We've walked so far past organic at this point. I'm sorry to say that.

**Jason Gong:** But this is super good for organic reach. In your marketplace with all these components, will there be a code variant for almost every component, all competing if someone's searching on Google?

**Colin Lateano:** They'll compete, absolutely. But most of our component library isn't made by Webflow — it's community components. We don't want Nixar's hero component displayed side by side with Webflow's getting-started version on the same page.

**Colin Lateano:** The library will have ones we make available from Webflow for free, and community ones that can be uploaded and charged for. We don't restrict how they operate. Code components supplement this because they're novel — right now, all these component libraries are Webflow-native.

**Jason Gong:** We need code ones available too that can do more flexibility.

**Colin Lateano:** And that gives us a greater range — there's no way I'd ask AI to generate 100+ Webflow-native components.

**Jason Gong:** So the library is broken up into individual components?

**Colin Lateano:** Each component will have its own page.

**Colin Lateano:** The library will be broken up into hundreds of thousands of searchable component listings. GrowthX generates code component ones that are functional and searchable in the marketplace. You find what you want and insert it — labeled as a code component, not a native one.

**Jason Gong:** If you keep going in that path, will the future have a NavBar category with Webflow code components and other creators' components?

**Colin Lateano:** Yes, that's my intent.

**Colin Lateano:** I honestly view code components as our escape hatch for limitations in our existing component functionality. React code can do more flexible things than native components.

**Colin Lateano:** In the nav bar section, there might be native nav bars and code component variants like a fade-in nav bar that pixelates and disappears.

**Colin Lateano:** Once the marketplace is sufficient, I'd want this surfaced in the designer so people can go to "find new components" and search for a nav bar directly.

**Jason Gong:** Okay, got it.

**Jason Gong:** That makes sense.

**Jason Gong:** I want to make sure there's a lane where this can get better and better — not just 30 things, but hundreds.

**Colin Lateano:** This is hundreds of things with flexibility for interesting creativity and functionality.

**Colin Lateano:** Not just simple things like a glassy button — there's a lot more to consider than what ShadCN does.

**Jason Gong:** Yeah, for sure.

**Colin Lateano:** We can go way more interesting with tons of components allowing people to flex creativity.

**Jason Gong:** This could really be like Canva's craziness with all their design templates.

**Colin Lateano:** The next evolution is when components become related to a React app — that's where things get really interesting. We're talking about enablement and usability now, still product-led growth because you can download and pull into your site.

**Colin Lateano:** Really great apps and code components will reference a small React app you can throw on GitHub or Webflow Cloud to handle backend functionality, with a component related to it.

**Jason Gong:** That makes sense. That's cool.

**Colin Lateano:** That's the next domain. This is one part of the future. Let me show you the Figma Make Marketplace as a reference.

**Colin Lateano:** Figma Make has actual apps as well, like a MIDI controller app. It has hosted code and frontend React components. Once we're in a groove with front-end React components, we want to build toward full React apps for the marketplace.

**Colin Lateano:** A big part is the remix functionality — being able to pull the code and update it with AI tools like Orion to say, "remix this MIDI controller to be a guitar," and the AI adjusts the code. That's why I wanted this call — to make sure you understand where we want to go with GrowthX.

**Jason Gong:** Yeah, okay.

**Jason Gong:** This is very clear. The next step is getting into the weeds about how code components hook up and what we need to generate. I'll pick a few easy things like a button or table and do a proof of concept.

**Colin Lateano:** That sounds absolutely great. Integration pages and use cases are evergreen — that program should live forever. I want it to keep going at the current pace. It's great for discovery and top of funnel.

**Colin Lateano:** If there's a challenge with GrowthX resourcing availability, I'm willing to trade SEO work for generative component and app work.

**Jason Gong:** I don't know if you've done a resource allocation assessment yet, but I don't want to abuse what we have.

**Jason Gong:** I'll tell you when we're hitting that limit. This engagement initially assumed low-barrier SEO work, so we might rework that at some point. Right now, our engineers are working on the guide workflows one thing at a time.

**Jason Gong:** Once that machinery is built, it becomes about editing. We can only edit so many things per week to keep quality good. Right now we're at 20-30 integration articles, which are easy to edit with good workflows. The docs are more involved, so we can probably only do 3-5 per week until we get better.

**Colin Lateano:** You mean the use case guides?

**Jason Gong:** Yeah, the use case guides. There's a lot to verify. Components might be easier — if we can verify they work and aren't ugly, that's less work than reading a full guide.

**Colin Lateano:** I'd argue components are probably easier than guides — most models know React. But there's nuance: our code components aren't infinitely nestable like React is today. There are limitations. Zach shared some guides with you. This should be faster as long as we verify they upload and work.

**Jason Gong:** This one seems like more work upfront on the engineering side, but I'll do the proof of concept first. Once the engineering frees up from guide pages, we'll shift here.

**Colin Lateano:** I'd love to understand the timing of assignments and when you expect to roll off and roll into components — just a swag estimate so I can set team expectations. DevRel is the last mile for all developer products. The full conference was entirely developer-focused.

**Colin Lateano:** People are asking when we'll deliver these things. I can hold them off for a while, but I need to know when we can start setting expectations.

**Jason Gong:** Let me get back to you on that, especially now that I understand the scale of what you're trying to get to.

**Jason Gong:** Is there anything you could share about deadlines? They mentioned ideally having a library that looks full by end of October.

**Colin Lateano:** We won't have the actual marketplace listing system for months. Anything in the fall will be DevRel hacking together merchandising through our developers subdomain or GitHub.

**Colin Lateano:** The actual delivery to end users will be underwhelming until we have marketplace connectivity. I'm flexible on delivery channels — platform work is never easy. I'd love 30 components (at least 10 materially interesting) by Halloween. 30 components would be 2-3 pages of display. I'm willing to work with reality — if these are harder to make, we do 5 or fewer.

**Colin Lateano:** Let me...

**Jason Gong:** Let me get back to you on that. For a lot of our other customers, it's listicles and how-to articles. For you guys, we're doing fairly special things.

**Colin Lateano:** The problem is they put a product manager on this instead of keeping marketing.

**Jason Gong:** I think it's interesting. The North Star is creating valuable content. Soon, boilerplate glossaries and how-tos won't be valuable anymore.

**Colin Lateano:** Search metrics show that random text content is cheap now. Our obligation is developer enablement. You guys made a good integration guide, so now we're thinking what else we can enable.

**Jason Gong:** That's a good problem, I think.

**Jason Gong:** Resourcing this is challenging on my side. Let me figure out what we can do. We're happy to expand once you're happy — maybe make the contract bigger. I'll get back to you early next week.

**Colin Lateano:** That absolutely works.

**Colin Lateano:** Oh, and all of DevRel is at an offsite next week, so Wednesday won't work. I can check in late Wednesday night (East Coast) at the end of your work hours, or Friday. The general meeting next week won't work for us.

**Jason Gong:** I'm off Thursday, Friday next week.

**Colin Lateano:** Maybe we'll call a week later. As for point of contact — as we move beyond SEO, there's less involvement from product marketing. Rachel and Karat held the contract originally, but this falls under DevRel ownership now. You'll see less of Vivian, definitely less of Michael Hart (he's been out for months), and probably less of Luke too.

**Jason Gong:** I'll say the more you can help us, the more work we can do. I know you guys work with another agency on SEO, but we still want to do that work.

**Colin Lateano:** I'm supportive of it.

**Colin Lateano:** I don't know enough about SEO and honestly don't care enough compared to other projects to analyze why your content engine is taking so long to accelerate. I think components are more rewarding and interesting for our community. SEO is your bread and butter, but I only have 10 hours in a day.

**Jason Gong:** For what you have and where you're allocating, it makes total sense to me. That sounds good.

**Jason Gong:** I'll send stuff over early next week and let me know in Slack where your open slot is on Wednesday.

**Colin Lateano:** We'll figure it out. All right, good talking to you.
