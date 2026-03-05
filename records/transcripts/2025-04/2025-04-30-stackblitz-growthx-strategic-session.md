# Stackblitz <> GrowthX Strategic Session

<metadata>
date: 2025-04-30
time: 16:00 UTC
duration: 30 minutes
organizer: mariana@growthxlabs.com
participants: Daniel Lopes, Mitchell Wright, Dave Capone, Matthew Panzarino, Mariana Montezzana
fathom_recording_id: 60048240
fathom_url: https://fathom.video/calls/288104725
share_url: https://fathom.video/share/zExnxnHbxx2Uu2s4_jejhQZ2jcw9CeBP
source: fathom
enriched_on: 2026-03-04 14:30 UTC
</metadata>

---

## Summary

Daniel Lopes and the GrowthX team aligned with Mitchell Wright at StackBlitz on a comprehensive content strategy for Bolt: building SEO-optimized competitor comparison pages (targeting Lovable, Cursor, Winsurf, and emerging players like Tempo Labs), creating ~100 highly curated premium templates with 600+ line one-shot prompts, and leveraging community-created content to generate dynamic tutorials. The team agreed to prioritize English-language content first, with localization focus on French (StackBlitz's second-largest paying customer base), and to start with data collection and CMS structure definition before implementation.

---

## Context

StackBlitz is an AI-powered web development platform (Bolt product) that competes with tools like Lovable, V0, and Cursor. Daniel Lopes initiated the relationship with StackBlitz after seeing their product pivot and messaging, and this meeting represents the first strategic alignment with the StackBlitz team on content marketing. GrowthX is positioned to help StackBlitz build SEO authority and organic visibility through high-quality, templated content that differentiates Bolt from competitors and teaches users how to leverage the platform's strengths (design quality, streamlined integrations like Stripe, easy deployment).

Mitchell Wright leads the product side at StackBlitz and has been working with an internal data scientist on user research, prompt analysis, and persona development. The meeting brought together GrowthX's content strategy expertise (Daniel, Mariana, Dave) with StackBlitz's product and community insights to design a content roadmap that treats templates as products in an e-commerce catalog model.

---

## Relevance

- **To GrowthX Delivery:** Template strategy parallels Envato's e-commerce approach — curating ~100 premium templates as "products" that can be SEO-optimized individually and grouped in category pages. This is a scalable, repeatable content pattern. Implementation will use Strapi CMS with flexible content models to handle different competitor types (direct vs. tangential competitors) and support multi-language content (starting with French). Dave Capone will lead the Strapi architecture guidance.

- **To GrowthX Business Development:** StackBlitz is a fast-growing AI dev platform with paying customers across multiple regions (English-speaking, French, German, India). Positioning for expansion work: templates, localization, community content workflows. The Jobs-to-be-Done research angle (connecting George with KJ) creates deeper strategic insight. Potential reference customer for case studies on AI platform content strategy.

- **To CheckThat:** Implicit AI visibility opportunity: Bolt needs to be discoverable in AI-powered searches alongside Lovable, V0, Cursor. The competitor comparison strategy is partly about SEO/AEO positioning. Community-generated tutorials (reverse-engineered from prompts) are content-rich, multi-framework examples that could inform AEO strategy for dev tools and low-code platforms.

---

## Overview

- Focus on creating high-quality comparison pages for direct competitors (e.g., Lovable) and complementary tools (e.g., Cursor, Winsurf)
- Develop a curated list of \~100 premium-quality templates/starter kits, emphasizing customizability and one-shot prompts
- Leverage community-created content to generate dynamic, SEO-friendly pages with auto-generated tutorials
- Localization efforts to prioritize French, with potential expansion to other key markets

---

## Key Topics

### Competitor Landscape Analysis

  - Expanded competitor list to include emerging players like Tempo Labs (tempo.new) and Spawn.co
  - Differentiation strategy: Emphasize Bolt's strengths in design, easy integrations (e.g., streamlined Stripe), and deploy simplicity
  - Persona-targeted comparisons: Developer-focused for Winsurf/Cursor, core ICP for Lovable/direct competitors

### Template and Starter Kit Strategy

  - Create \~100 highly curated, premium-quality templates (e.g., portfolio sites, landing pages)
  - Implement detailed, customizable one-shot prompts (600+ lines) for non-technical users
  - Design template pages with embedded previews, long-form prompts, and easy customization options
  - Categorize templates (e.g., portfolio, e-commerce) with SEO-optimized category descriptions

### Community Content Utilization

  - Explore featuring community-created content alongside curated templates
  - Generate auto-created tutorials from community projects, explaining frameworks and techniques used
  - Implement user opt-in for template sharing to expand content library

### SEO and Content Strategy

  - Treat templates as products in an e-commerce catalog approach
  - Target long-tail searches with individual templates
  - Create category pages for broader keyword targeting
  - Develop feature-specific content (e.g., "how to build a contact form in Bolt")

### Localization and International Markets

  - Primary focus on English-speaking audience
  - French identified as second-largest paying customer base
  - Consider localization for French and German markets, where users tend to search in their native language

### Technical Implementation

  - Bolt frontend: JavaScript (possibly Remix)
  - Backend: Rails (carried over from StackBlitz infrastructure)
  - In-house team handling homepage redesign; potential for GrowthX assistance with development

---

## Action Items

**Mitchell Wright (StackBlitz)**
- Share existing user data, research findings, and persona information with GrowthX team

- Grant GrowthX team access to StackBlitz's Strapi CMS account

- Pull and share stats on paying customers and account users by language


**Daniel Lopes (GrowthX)**
- Connect George (GrowthX researcher) with KJ from StackBlitz for user research collaboration


**Dave Capone (GrowthX)**
- Provide guidance on Strapi CMS setup for category structure and URLs

---

## Transcript

**Dave Capone:** Hi, everyone.

**Matthew Panzarino:** Hey, Mitchell. Nice to meet you.

**Daniel Lopes:** Let me introduce myself real quick.

**Daniel Lopes:** I think I'm the only one, the first one here that you probably haven't met yet, but I'm Daniel.

**Daniel Lopes:** I'm Marcel's co-founder and I saw your message that you said, I sent to him this weekend and I'm super pumped about what you guys are doing.

**Daniel Lopes:** I use your product a ton.

**Daniel Lopes:** I used Lovable, VZero, Cursor, Replit, and I was head of product for If This Then That.

**Daniel Lopes:** So I've been thinking about these kinds of problems for a long time.

**Daniel Lopes:** I'll be involved more closely here and help be some of the personas that embrace some of the personas that...

**Daniel Lopes:** That would be using, that we think is like the use case for Bollet.

**Daniel Lopes:** So super pumped to be here.

**Daniel Lopes:** Yeah, for the call today, we had some, we were thinking about the strategy and how we could approach a few things here, both the comparison part that you guys brought up, but also like seeing what V0 and Lovable, I think Lovable changed their homepage last week and the kind of stuff that they are doing.

**Daniel Lopes:** And I think we can do a better job there.

**Daniel Lopes:** I have no doubt, right?

**Mitchell Wright:** Like also Lovable is going after some type of programmatic SEO pages, but I think it's, the only thing they're changing is like a headline.

**Mitchell Wright:** So I think, I think based on what I said you all, we can really crush what they're doing.

**Mitchell Wright:** It's going to be so good.

**Daniel Lopes:** Yeah, so I'll share my screen and I'll walk you through.

**Daniel Lopes:** The kind of stuff that Mariana is putting together and then the stuff that our folks in the technical side are putting together.

**Daniel Lopes:** And you let me know if we're in the right direction.

**Daniel Lopes:** So for the comparison part, Mariana put this together.

**Daniel Lopes:** Let me get the list of competitors.

**Daniel Lopes:** So we have Replit, Cursor, V0, Lovable, all the usual suspects there.

**Daniel Lopes:** We're going to expand this and then we're also checking the volumes and keyword difficulty and all that.

**Daniel Lopes:** But the main question that I have for you there would be if anything else stands out.

**Daniel Lopes:** Is there any other players that there's so many different smaller ones popping up for different use cases?

**Daniel Lopes:** Like if you could, I can send them afterwards?

**Daniel Lopes:** There was a document, I think, in Notion where I added some additional ones that you all had asked me to add.

**Mitchell Wright:** But I don't remember the URL there and which ones I had added. I have it here. Yeah, yeah, yeah.

**Mitchell Wright:** So, oh, yeah, and I even, I feel like I missed a couple here.

**Mitchell Wright:** So, like, Tempo, Tempo Labs.

**Mariana Montezzana:** I didn't like Tempo because it's impossible to find their, like, if you type Tempo to the search, and even on SEMrush, a lot of other pages, I couldn't find the tool.

**Mariana Montezzana:** Yeah, so they go by Tempo.

**Mitchell Wright:** Their URL is Tempo.new, but their company is called Tempo Labs.

**Mitchell Wright:** Tempo Labs.

**Mitchell Wright:** Yeah, yeah, but they are one that I've seen getting a little bit of traction.

**Mitchell Wright:** I'm trying to think if there was a data button.

**Mitchell Wright:** Yeah, we got that.

**Mariana Montezzana:** Ron is not there, too, because the same reason that all you can find is a movie that is called Sponsible.

**Mariana Montezzana:** So, yeah, I, like, I'm not sure what keywords people type when.

**Mitchell Wright:** see.

**Mitchell Wright:** I don't know that that one has like a ton of organic, but it's getting traction on social.

**Mitchell Wright:** So that's where like some of these like Tempo and Spawn, they're getting traction on social, you know, like Instagram, TikTok, YouTube, Twitter.

**Mitchell Wright:** I'm talking about Spawn.co.

**Matthew Panzarino:** Yeah, yeah, cool.

**Daniel Lopes:** Yeah, I mean, there's always ones popping up.

**Mitchell Wright:** A lot of them don't get any real meaningful traction.

**Mitchell Wright:** But the ones on here, I think, do have enough traction that I keep an eye on them at least.

**Mitchell Wright:** Sounds good.

**Daniel Lopes:** Yeah, so the plan that we're thinking here is to

**Daniel Lopes:** One thing we might have to take offline and we can probably discuss is what are the things that you think both is super good at or at least the things that you see your community talking about compared to the things that the competitors are doing?

**Daniel Lopes:** At least on my end, when I do a lot of stuff with both, I think you guys are super good with landing pages, marketing stuff, and then the deploy is super easy with Netlify, for example, compared to a years, like a pain, yes, to deploy anything.

**Mitchell Wright:** So I don't know.

**Daniel Lopes:** If you have a bunch of things like this that you guys are tracking in the product side that you see yourself, that would be super helpful.

**Mitchell Wright:** Yeah, I think we released a new, our latest releases helped a lot with the design of things.

**Mitchell Wright:** So like from the design side, I feel like we are doing a lot better than other people.

**Mitchell Wright:** I feel like we also make a...

**Mitchell Wright:** It's point of trying to make the integrations that we have really easy and straightforward.

**Mitchell Wright:** So, you know, some of the competitors, they have, for example, a Stripe integration, but it's pretty hard to actually do it.

**Mitchell Wright:** It's not really streamlined. That's the thing we've tried to really do — make our Stripe integration really streamlined. The challenge is that a lot of these tools converge to the same point because we're using a lot of the same underlying infrastructure as far as LLMs and things like Supabase and Stripe.

**Daniel Lopes:** So when you're thinking about the competitor pages, who are the personas that you want to land on these pages? Are those going to be the usual personas that would come to the homepage, or are you trying to attract different kinds of people?

**Mitchell Wright:** Well, for things like Winsurf, Cursor, and GitHub Copilot comparisons, those are going to be more directed towards developers, I think.

**Mitchell Wright:** And the idea that, you know, those, like Cursor and Bolt, I don't actually consider them quite direct competitors.

**Mitchell Wright:** They're a little bit more like tangential competitors, or they can be used in a complementary way.

**Mitchell Wright:** Versus like Bolt and Lovable, it's going to be our core ICP could use either of these and probably have a decent experience.

**Mitchell Wright:** But Bolt will be the better product for certain use cases.

**Daniel Lopes:** Yeah, exactly how I was thinking about it too.

**Daniel Lopes:** And then, so we're going to come up with those competitors and we're going to work through that list and like think about how they compare to both.

**Daniel Lopes:** And maybe the pages will be different and the kind of things we compare that are different because like if you're Cursor, Windsurf, Zed, we want to have the more like, hey, how you start with both and you continue with Cursor and vice versa.

**Daniel Lopes:** Yeah, yeah, yeah, exactly.

**Mitchell Wright:** That's a great idea, a great way to think about it.

**Daniel Lopes:** And another thing I wanted to ask you, like, we're probably going to have George.

**Daniel Lopes:** George is our in-house researcher and he's an expert in jobs to be done.

**Daniel Lopes:** If there is any chance we could get access to like some of the users that you have that love the product or people that are outspoken about the product or like let us like one of our photos.

**Daniel Lopes:** We talked to them, so we can come up with things that we could list on the website, or what are the things that we could be answering on the website, when do they come up with the journey, the job should be done journey, when do they go to both, and what do they do after?

**Daniel Lopes:** So we can probably develop a lot there.

**Daniel Lopes:** I don't know if it would be direct impact on this page, but just do a bit of job should be done research, have our team do that.

**Daniel Lopes:** Yeah, happy to put you in touch with users.

**Mitchell Wright:** We also have a data scientist in-house, and we've been doing a lot of research on the actual prompts that people are doing.

**Mitchell Wright:** Nice.

**Mitchell Wright:** I was going to ask that next.

**Mitchell Wright:** I think you'd find a lot of interesting information from it, and it's pretty in-depth.

**Daniel Lopes:** Perfect.

**Daniel Lopes:** That was my next question.

**Daniel Lopes:** If you had that happening inside, amazing.

**Mitchell Wright:** That would be great.

**Mitchell Wright:** Yes.

**Daniel Lopes:** That covers the competitor comparison project. We also have another thing we're thinking about: templates and starter kits. I don't see a lot of amazing stuff coming out of the community. The prompts are mostly one-shot prompts. What I was working on yesterday is creating a curated list of maybe 100 highly curated prompts with a template list — like Vercel has, where you have all the templates available. When you go in, it's not super flat, it's not easy to customize, and there's no real explanations of what's going on. Lovable is even worse — it's just community stuff, and a lot of it's really not great. Why are they surfacing all this janky content?

**Daniel Lopes:** But when you go to Envato, the people selling templates have everything polished and usable. What I was doing yesterday is analyzing what people pay for on Envato and the main categories. Then I created super polished, one-shot prompts. For example, one is 600 lines of code that defines the overall structure using Tailwind with the grid system. Anyone could come in and adjust it. We have the copy and everything, so you can change the language. One-shot this in Bolt and it always looks awesome. I'd buy this and customize it easily. We came up with a few other examples — like a landing page coming soon template. Same idea: you can change colors, tweak as much as you want. All one-shot. So we could come up with a curated list of amazing templates that people would pay for on Envato, but now we can customize because it's text.

**Daniel Lopes:** Our designer was working on a Figma mockup yesterday showing how the homepage could look. Instead of a lot of community crap, it could be our templates.

**Mitchell Wright:** Yeah, we're actually working on a redesign of the homepage and want to have a section exactly like this.

**Daniel Lopes:** And then like the way we're thinking the next page here could be like, like, just Ren was just spending some time here, but just to give an idea.

**Daniel Lopes:** So there's like all of our templates like featured first, and then later we could have the community stuff under.

**Daniel Lopes:** What doesn't exist today in these pages is a description of what makes a good portfolio website. We could have a page that describes the category, what is great about a portfolio website, e-commerce websites, or coming soon websites. That's the SEO play. Then when you go into the template itself, there's a description of that template and a hero with the embedded version. Under it, there's the super long prompt that explains how you could change it. You can remix it right there, press play, and we'll generate and start the experience.

**Mitchell Wright:** Yeah, love that.

**Daniel Lopes:** That's the direction we're thinking. It's awesome that you're already thinking about the homepage redesign. So how are you guys staffed, and how can we get this built? We have design and engineers on our end. Do you guys have Rails backend developers?

**Mitchell Wright:** A lot of Bolt is JavaScript and I think it might be a Remix app, if I remember correctly.

**Mitchell Wright:** And then we do have a Rails backend as well.

**Mitchell Wright:** When Bolt was originally launched, they reused a bunch of infrastructure from the StackBlitz product, which was Rails.

**Mitchell Wright:** And so that's a little bit of an artifact of using that infrastructure.

**Mitchell Wright:** That makes sense.

**Daniel Lopes:** So what's the team working on the homepage? Is it in-house or an agency?

**Mitchell Wright:** In-house. We have in-house product designers iterating through different concepts, and developers to handle the implementation.

**Daniel Lopes:** So we'd be happy to allocate engineers from our side to code the changes, or you can handle it. Whatever works best.

**Mitchell Wright:** Yeah, let's talk more about the starter kit template page — what we want it to look like and whether we need dev assistance.

**Daniel Lopes:** Sounds good. Dave, can you talk about the SEO play here? This is essentially an e-commerce catalog approach.

**Dave Capone:** The templates themselves would be similar to products in an e-commerce catalog.

**Dave Capone:** So if you're thinking about like e-commerce catalog, so the templates themselves will rank for very long tail searches.

**Dave Capone:** We would then have categories and all those products would be or templates would be in a category which would give us kind of like the body or the neck turns that we would want to go after.

**Dave Capone:** And we would just be able to scale out at that point and create tons of content around the different types of categories that we create for these types of websites.

**Dave Capone:** And eventually I'd love to get into features.

**Dave Capone:** So if we're building a portfolio website, there could be a contact form that's on there.

**Dave Capone:** And folks might want to learn how to build a contact form in Bolt or figure out how to build it.

**Dave Capone:** So we can go out and create content for all those different features and it would be all interlinked and internally linked and everything through all that.

**Dave Capone:** So that's how we're looking at it is like kind of like the catalog approach.

**Dave Capone:** We would look at, like, ThemeForest or Envato and see what the most popular categories are and populate those and really use that as kind of the pulse of what folks are searching for and then create those categories and go after those templates that are, like, similarly the most popular in each one of those categories.

**Daniel Lopes:** One thing I don't know if you're already considering: we could have the templates as the featured section on top, super high quality. Me and a few engineers could create super detailed prompts. Then we can have community stuff as well, but instead of what V0 or Lovable do (which is pretty bland with no text), the volume play is to service community submissions intelligently. I don't know if you have a checkbox or mechanism for the community to opt-in to have their work surfaced publicly. If you do, we could create auto-generated content from whatever they build. We look at their initial prompt and the whole thread to get to the final product, then create a description explaining it's a Remix app, Svelte app, Next.js app, or whatever. We can build mini tutorials explaining how it was built.

**Daniel Lopes:** For example, they might build something using shadcn-UI dropdown components with additional styling.

**Mitchell Wright:** Yeah, V0 is focused on Next.js and shadcn-UI as the base for everything. Whereas we can do any JavaScript framework. We can have tutorials where you click and see how they achieved the animation.

**Daniel Lopes:** We can generate that at scale for any content you have. So if you have the thread from a session, we can turn that into a tutorial. Every community submission becomes its own page with dynamic content. We tap into what Claude can do for code and reverse-engineer to create content so people can learn about all these frameworks.

**Mitchell Wright:** That's really interesting. I like the idea of letting users select to have their work used as templates, then running that through different LLM workflows. We get everything — the package.json, all the prompts they used. We can put those together to produce some really interesting outputs.

**Daniel Lopes:** That would be a cool project to work on right after the templates.

**Mitchell Wright:** Yes. Doing the templates and the comparisons first, then moving into the community side is very interesting. That's exactly the kind of thing we're very aligned on.

**Daniel Lopes:** Do you have anything else you could share?

**Daniel Lopes:** I'm thinking like personas, top of mind challenges, all the things that the market has changed.

**Mitchell Wright:** We've been working through on the data science side.

**Mitchell Wright:** And then we're also doing a bunch of user interviews, some surveys on user registration.

**Mitchell Wright:** We'll have more data in like the following weeks around personas and yeah, just some more quantitative and qualitative that we can share with you.

**Mitchell Wright:** But I'll share what we have so far and we can go from there.

**Daniel Lopes:** Can we get George in touch with your team that's doing this research? George is our lead researcher in jobs to be done — just to understand the direction you're going, even before you have everything ready.

**Mitchell Wright:** Yeah, that'd be great. Who's in charge of that on your team?

**Daniel Lopes:** KJ.

**Daniel Lopes:** Does anybody have any other questions? I think we're pretty aligned here.

**Dave Capone:** Mitchell, I saw that you set up Strapi. Can you give us some guidance on the setup — category structure, URLs, and what access we need?

**Mitchell Wright:** Yeah, I'm happy to do whatever we need to do to get you guys access.

**Dave Capone:** Yeah, I'll go back to the team and see if we have guidance on category structure and URLs. We'll probably have a standard we can reference.

**Daniel Lopes:** I'm familiar with Strapi, so if you give us access to your account, we can start thinking about content blocks and sections. We'd start with the comparison pages. These will probably be quite different because we have clusters of different types of competitors — supporting players versus direct competitors, so probably different content models for those. Plus we're thinking about different languages, which might impact the structure. I'll pull in folks from our team who are better at CMS than me. But next week, once we have a better idea of the comparison page features, sections, and data you want to display, the CMS becomes easy. Same thing for the starter kits — once we have categories and a detailed Figma, we can think about the CMS structure.

**Daniel Lopes:** But I think this week and next, we'll be essentially figuring out the data structure, figuring out what we show, figuring out the project, and the CMS will come after.

**Mariana Montezzana:** What languages do you think would be interesting to localize? You and competitors have a lot of audience in Brazil, Spanish-speaking regions, French, and German. Do you think it would be valuable to localize these pages, especially the comparisons?

**Mitchell Wright:** English is our largest audience, and the second largest group of paying customers is French. India also uses our product, but they do research in English, and they're only about 2% of ARR, so it's not a priority.

**Mariana Montezzana:** In French and German, people do their actual research in their native language, so those are good targets.

**Daniel Lopes:** Thanks for your time, Mitchell. We're excited about this and will keep you in the loop. If anything comes up in the meantime, let us know.

**Mitchell Wright:** Awesome. Thank you all so much.
