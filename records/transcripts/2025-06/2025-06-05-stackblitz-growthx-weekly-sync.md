# Stackblitz <> GrowthX Weekly Sync

<metadata>
date: 2025-06-05
time: 21:01 UTC
duration: 35 minutes
organizer: mariana@growthxlabs.com
participants: Marcel Santilli, Mariana Montezzana, Mitchell Wright
fathom_recording_id: 66837186
fathom_url: https://fathom.video/calls/316603946
share_url: https://fathom.video/share/nCpkzhssx2yWS12AH4Fnaspzgfkp41xo
source: fathom
enriched_on: 2026-03-03 09:15 UTC
</metadata>

---

## Summary

GrowthX and StackBlitz aligned on building a high-opportunity website template gallery as a subdirectory on stackblitz.com. Marcel presented research showing 1.9 million monthly searches across template-related keywords with low keyword difficulty, and outlined a strategy to create a searchable, descriptive template library with built-in prompts for customization. The team agreed to move forward with two parallel tracks: building a template database with metadata and taxonomy, and producing mock pages and prompts for an MVP, with a visual mockup and progress update due by Monday.

---

## Context

StackBlitz is a web-based IDE and development platform used for building web applications. This is a weekly sync between GrowthX (a B2B content marketing services and AI visibility platform) and the StackBlitz team to collaborate on a strategic content initiative. The meeting focused on planning a template gallery product — a major SEO and user acquisition play to capitalize on the massive search volume around website templates and starter kits. StackBlitz was exploring this as a way to drive organic traffic and improve user onboarding by providing pre-built, customizable starting points that users can immediately open and modify within the platform.

---

## Relevance

- **To GrowthX Delivery:** Programmatic SEO expansion — GrowthX is scaling its pSEO capabilities (already proven on Fathom's project with 96/100 new pages getting impressions within 5 days). Template gallery represents a large-scale application of pSEO taxonomy, data modeling, and content generation to a 1.9M-volume keyword set. Requires building category/subcategory taxonomy, metadata models, and prompt-based content generation frameworks.

- **To CheckThat / AEO:** Prompt generation as a strategic asset. The template gallery will showcase prompt engineering in action — Marcel emphasized that having visible prompts (what was used to generate each template) creates significant user learning and differentiation. This aligns with CheckThat's AI visibility thesis and could be a future showcase for prompt quality and AI-assisted creation workflows.

- **To GrowthX Business Development:** StackBlitz partnership signal and expansion. Strong quarterly activity, collaborative planning, and mutual willingness to invest time/resources indicate account health. Template gallery, if successful, could become a reference case for programmatic content generation at scale.

---

## Overview

- A website template gallery could be a significant opportunity for StackBlitz, with high search volume and relatively low keyword difficulty
- The team will focus on creating a subdirectory on the StackBlitz domain as an orphan page to host the template gallery
- The project will involve building a database of templates, generating template pages, and creating a user-friendly interface for browsing and filtering

---

## Key Topics

### Market Research and Opportunity

  - Analyzed existing template marketplaces (Webflow, Wix, Envato, etc.) and inspiration sites (Landbook, Site Inspire)
  - Identified high search volume (1.9 million) for template-related keywords with relatively low difficulty
  - Opportunity to create more descriptive, user-friendly template browsing experience

### Project Scope and Features

  - Focus on website and landing page templates initially, not full applications
  - Create a comprehensive database of templates with detailed metadata and descriptions
  - Develop a user-friendly interface for browsing, filtering, and selecting templates
  - Include prompts for each template to aid in customization and learning

### Technical Implementation

  - Build the gallery as a subdirectory on the StackBlitz domain (orphan page)
  - Use Superbase for the backend database, potentially synced with Airtable for CMS-like interface
  - Host the site using Vercel or similar platform
  - Utilize ShadCN or similar framework for frontend development

### Content Generation Strategy

  - Develop a data model and taxonomy for categorizing templates
  - Use a combination of manual creation and AI-assisted generation for template content
  - Explore programmatic generation of simple templates using tools like Plot.ly

### Integration with StackBlitz

  - Implement easy "open in StackBlitz" functionality for templates
  - Provide prompts and instructions for customizing templates within StackBlitz

### Potential Future Developments

  - Explore partnerships or integrations with other platforms (e.g., Webflow)
  - Consider adding more advanced features like stack customization or agency connections

---

## Action Items

**Mitchell Wright (StackBlitz)**
- Seek internal approval for orphan page approach for template gallery project

- Generate coupon for highest tier plans for GrowthX team to use for template creation

**Marcel Santilli (GrowthX)**
- Report progress on website template project by Monday; deliver initial mockup/prototype by next week

- Begin building database of content to feed template gallery pages

- Start producing mock pages and prompts for template gallery MVP

- Create visual mock-up of orphan page concept for template gallery by Monday

---

## Transcript

**Mariana Montezzana:** I'm doing great. How are you doing?

**Marcel Santilli:** It's crazy, but it's been fun getting a bit more involved on some of these accounts.

**Mariana Montezzana:** I saw you were talking about programmatic SEO. Hopefully they will be joining us today.

**Marcel Santilli:** Yeah, Alex is out, but Mitch will be joining.

**Mariana Montezzana:** Let me check with Dave as well.

**Marcel Santilli:** He was on another call with me just now, so he might join a little late.

**Mitchell Wright:** Hey, how's it going?

**Marcel Santilli:** All right, let me send you a quick agenda, but we can keep this kind of fairly interactive as well. Do you mind dropping the link, Mariana, to the agenda really quickly?

**Mariana Montezzana:** Let me drop it.

**Marcel Santilli:** All right, Mitchell. Let's jump in.

**Marcel Santilli:** Based on our earlier conversation, there are multiple directions we could take this. We have the comparisons project and the starter kit. Let me send you the correct project link. We could go into each of those projects or focus on one at a time.

**Mitchell Wright:** Which link should I be looking at?

**Marcel Santilli:** Look at the second one.

**Mitchell Wright:** Okay, I see where you're at. Yeah, let's start with starter kits and templates.

**Marcel Santilli:** All right, so we did a little bit of work here. One of the main use cases we uncovered was that people building websites and landing pages had a huge aha moment when they could see something working immediately. So I started researching what's out there right now — what are people ranking for when they're trying to find templates or inspiration? We focused on websites and landing pages specifically, knowing that apps are kind of a different environment altogether.

**Marcel Santilli:** The main examples we found were platform-specific — Webflow templates, Bigfoot community, and others. They all have a navigational and marketplace mentality as opposed to helping people find the right template. And honestly, it's really hard to find what you're looking for based on just filters. For example, if I want a template with a grid and resource hub that's black and white and modern, even that combination becomes hard to find. Most of these sites aren't descriptive at all. The burden is very much on the user to dig through and find what they need.

**Marcel Santilli:** Then there are marketplaces like Envato where the search is a bit better because if you can't find it, you won't buy it. And then there's Squarespace, Wix, Landbook, Site Inspire, WWW Awards, and Dribbble. My thought was, how can we quantify the opportunity across all of these? So we took Wix and looked at their pages, filtering out branded keywords. We found about 352 pages with significant non-branded keywords they rank for.

**Mitchell Wright:** I'm still seeing a sales dashboard page. Is your screen share stuck?

**Marcel Santilli:** Let me try sharing the whole screen again.

**Mitchell Wright:** Okay, I can see it now. But it's stuck on the WWW Awards page.

**Marcel Santilli:** Let me try one more time.

**Mitchell Wright:** Okay, I can see the Airtable now.

**Marcel Santilli:** Great, stay on that.

**Marcel Santilli:** So looking at Wix, for example, this one page ranks for company website templates, construction site templates, construction web, builder web templates — all super relevant. Combined, that's about 15,000 monthly searches with an average keyword difficulty of only 28. The current template marketplaces show mostly examples, but there's a lot more we could do to be more descriptive, walk people through what types of pages they need, and give them something they can immediately play with — not just inspiration.

**Mitchell Wright:** If you click edit on the Wix site, does it pull you into the editor?

**Marcel Santilli:** It does, but then there's also the barrier of learning the platform. With Webflow, where I've used their templates, the editing is at such a granular level that you're modifying everything from scratch. With something like StackBlitz, you'd have a better foundation you can remix and immediately work with. Some of these other template sites are just inspiration only — they don't have any actionable option at all.

**Marcel Santilli:** The TLDR is that across these two sites alone, there's about 1.9 million total search volume. The keyword difficulty for most of them is below average, though the generic ones like "website templates" are harder. But the number is massive. And we're not even including components yet — single-page components like grids, hero sections, and so on. You can decompose the opportunity down to page and component levels. So these are the starting opportunities where we know there's search demand.

**Marcel Santilli:** One of the things we started doing was creating a data model. Think of these as the different categories we can go after. For example, business and corporate, then we define subcategories like consulting firm or law firm. But then you can go deeper — not just law firm, but IP law firm, family law firm, etc. Then you can multiply by style, color, typography, and other dimensions. You can really open up the branches and expand over time.

**Marcel Santilli:** The really cool thing we're seeing with Fathom's programmatic content project is that out of 100 pages we published last week, 96 are getting impressions within five days, and 16 are getting clicks. And those were all zero-volume keywords. In this case, with template categories, the opportunity is even bigger. For instance, is anyone searching for "website template for IP law firms"? Yes — and that's already ranking as a search result. So the likelihood that if we own that long-tail space, we'll perform well and get people clicking and using the templates is much higher.

**Mitchell Wright:** Yeah.

**Mitchell Wright:** Yeah.

**Mitchell Wright:** Yeah.

**Mitchell Wright:** I mean, I like this.

**Mitchell Wright:** I like this play, especially because we perform very well with, you know, kind of the design aspect.

**Mitchell Wright:** And that's a little bit easier for people to actually get something and do something with it versus, you know, a full app can be more complex.

**Mitchell Wright:** And sometimes people can struggle with that.

**Mitchell Wright:** So this is an interesting route to go.

**Marcel Santilli:** So what I was thinking was, like, I don't know, like, how all feel about the term vibe overall?

**Marcel Santilli:** Like, is that a thing that you all are, like, going with it?

**Marcel Santilli:** I mean, not that you're the only one.

**Mitchell Wright:** I think it's kind of playing out a little bit.

**Mitchell Wright:** It's lost a lot of the appeal, which is kind of funny because it has only been a thing for, like, a handful of months.

**Mitchell Wright:** It's like, You're – Yeah.

**Mitchell Wright:** Yeah, yeah, yeah.

**Mitchell Wright:** So I think, yeah, I wouldn't lean too hard into that.

**Mitchell Wright:** Okay.

**Marcel Santilli:** We can come up with different concepts.

**Marcel Santilli:** I had, I bought a few domains that were kind of like along those lines of like VibeWeb, you know, .ai, or like VibeSites, or, you know, like things like that, or VibeGallery, but it can be kind of different, you know, like .ai things.

**Marcel Santilli:** Like that's one play we can have.

**Marcel Santilli:** Another play can be, like we talked about as a subdomain and almost treated as a completely separate entity altogether in the sense of like, it doesn't need to connect super hard from your main site initially, or you can A-B test it a little bit to see like what happens to traffic that lands there.

**Marcel Santilli:** But, you know, like it can be treated very much like this navigation.

**Marcel Santilli:** And, and then it's just like, do you want to go with something that bolt is upper, you know, center?

**Marcel Santilli:** And then.

**Marcel Santilli:** Like have more of kind of like a easy filtering, right?

**Marcel Santilli:** Like, so, so the idea is like, I think I showed you the one that we just did or that we're still doing for where as you go through, we can kind of define what filtering we want to have, you know, for and make this as visual as, as we want to be, you know?

**Marcel Santilli:** And so, so, so then like what we can do really quickly is define the, the content model, if you will, right?

**Marcel Santilli:** Like what are tags, what are the different, if you will, like taxonomy that's important.

**Marcel Santilli:** And then over time, the, the thing that I was kind of playing with just so that you kind of see is like things like, for example, like all the possible taxonomies you can have around like websites, but also later on, like what is every single piece of a stack of a website, right?

**Mitchell Wright:** Like what

**Marcel Santilli:** Another lane that this can gear towards where in some of these we can actually define.

**Marcel Santilli:** So think of like StackShare, what it used to be, you know, what's this website stack?

**Marcel Santilli:** It's like, here's a template, but like, what is this template stack?

**Marcel Santilli:** know, you can kind of play with the stack and say, I like this template, but can you tweak the stack for me?

**Marcel Santilli:** And then auto-generate a prompt using kind of some of our workflows as a prompt generator, you know, where it's less of a prompt and more of a plan, right?

**Marcel Santilli:** And so, like, that's one of the things that we're doing, for instance, like, for augment code, because there's all these, like, cursor rules.

**Marcel Santilli:** Are you familiar with cursor rules?

**Marcel Santilli:** Yeah.

**Marcel Santilli:** Yeah, so, like, with cursor rules, like, you're going in and you're seeing, like, kind of, like, all these rules.

**Marcel Santilli:** And these rules are really just, like, a basic plan, you know, of, like, almost, like, what's important, what version of things are you using, what kind of, you know, so in some ways, like, the plant, the prompt here is the plan and the guideline.

**Marcel Santilli:** And the roles as well as like the place you're starting from, right?

**Marcel Santilli:** Like the scaffolding you're starting from potentially, you know?

**Mitchell Wright:** Yeah.

**Mitchell Wright:** One of the main issues, like I like generally where this is, but I think when we start talking about getting like deep into the, you know, what's the stack here?

**Mitchell Wright:** From the research we've done, that really starts straying from kind of our core use case, right?

**Mitchell Wright:** At least right now where, yeah, the people, our users generally don't care.

**Mitchell Wright:** What the stack is, they, they actually are just caring about the end result.

**Mitchell Wright:** So, so that piece probably not as relevant, but I think the overall idea here, I do like.

**Mitchell Wright:** Got it.

**Mitchell Wright:** Okay.

**Marcel Santilli:** Being more opinionated gets you better results faster. When you start with a good foundation like ShadCN blocks, you get much better results than starting from scratch. With the right instructions on components and stack, it's night and day. When you click in and it's polished and has wow elements, that's what we want.

**Mitchell Wright:** Yeah, ShadCN gives you a lot of nice interactivity out of the box. We're open to being opinionated about that stuff in the prompts, though the end user doesn't need to know the details — we just embed them.

**Marcel Santilli:** So what I'm thinking is we build this internally, tweaking what we've already got into this concept, then building a database with metadata and descriptions for all the templates. We start with a comprehensive data model and gradually expand it.

**Marcel Santilli:** So you can visually browse like "construction website template." The tech stack is similar to what I've done before — we build the scaffolding, hook up Supabase, connect it to Airtable for easier QA. Supabase has a table editor, so we import content easily. The bottleneck is figuring out how many templates we can create programmatically. But here's the thing — even if users don't tweak the prompts, having the prompts visible is incredibly valuable. I love the idea of exposing what prompt generated each template.

**Mitchell Wright:** Yeah, I'm curious to see what prompts created things. You can learn a lot from that. I'm all for exposing the prompts so people can study and edit them. A lot of people will just use the template as-is or copy the prompt and use it elsewhere.

**Marcel Santilli:** What could really take this to the next level — I reached out to Rachel, the CPO at Webflow. There's a tool that converts HTML plus CSS into Webflow components via copy-paste. Not many people know Webflow supports headless. If we build a really solid template database, there's user-generated content angles, direct product integrations, and partnership opportunities. Supabase exploded because of by.coding integrations. Similarly, V0 is now a major revenue driver.

**Mitchell Wright:** V-Zero was doing about $15 million in ARR in December, whereas everything else combined was around $160,000. It's grown significantly as a percentage of overall revenue now — they're cross-selling heavily to existing customers.

**Marcel Santilli:** Every founder and company we work with has the same challenge — they don't want to hire an agency, they want to quickly get to something they feel good about, then hook it up to a CMS to control parts of it. That's what competitors like Tempo are doing with the PRD → prototype → code flow.

**Mitchell Wright:** Yeah, that's what we've discussed — the agency play. But Tempo is pushing hard on the hire-an-agency angle.

**Marcel Santilli:** So what are your thoughts? Do you think this is worth pursuing? We could touch on comparison pages, but I think this template gallery is something we could ship quickly and see results.

**Mitchell Wright:** Yeah, I think shipping something and getting it out there is what would make everyone feel good. As for comparison pages, Alex had some pushback — he doesn't think we should automate those. He wants us to own that piece internally, not outsource to an agency.

**Marcel Santilli:** So we have a few options here. Subdomain gives us brand attribution but is slightly harder. Off-domain gives us no attribution but is a bigger lift. Subfolder is the best approach, even if it's orphaned. We're seeing orphan pages get traffic immediately, even for companies smaller than StackBlitz. That's the preferred path. What are the restrictions on doing a subdirectory with DNS we control?

**Mitchell Wright:** If we did it as an orphan page in a subdirectory, nobody would find it unless they discover it organically, so it feels less scary from a design standpoint. We could do a reverse proxy and host it however we want without buying our own infrastructure.

**Marcel Santilli:** So we'd build this on our end. Have you guys done programmatic template generation before? We could use your API with prompts or I can give you coupons for credits. Even manually, we could build an approach where we have description pages while we're building full apps in parallel. How many templates could a production manager crank through in a day?

**Mitchell Wright:** We have a URL parameter where you can embed a large prompt and it'll kick off a project. That might work. I'll generate coupons for our highest tier plans for you to use.

**Marcel Santilli:** Great. If we can do that across multiple accounts, we'll have parallel tracks going. Would you be okay with us building templates offline and uploading them to Bolt as apps? We could use Plot.ly or similar to programmatically generate simpler ones.

**Mitchell Wright:** I'm totally fine with that. We can generate in Bolt, but if generating offline is easier, that works for me too.

**Marcel Santilli:** Perfect. I'll report back by Monday with progress. We'll get something in front of you by next week — probably not a thousand pages, but we'll have two parallel tracks. We're focused only on this for you. One track builds the database and content model for the pages. The other produces mock pages and prompts for the gallery MVP. If you can clear the path for the subdirectory approach, we'll have a visual mockup by Monday at the latest so you can show people. Worst case, we buy a domain and host it separately.

**Mitchell Wright:** Love that. Let's move forward with this approach.

**Mitchell Wright:** One more thing — what tech stack will you use for the backend? Supabase for the database?

**Marcel Santilli:** Yeah, it's pretty simple. We'll use ShadCN for the frontend. For hosting, we can host it on Vercel or you can host it yourselves. We'll put everything in a GitHub repo, sync to Supabase, and optionally sync Supabase to Airtable for a CMS-like interface. Our goal is to hand you a working site and say "point your DNS here." We don't need to worry about scaling until you're getting a million visitors. Keep it simple — Vercel, Supabase, GitHub repo.

**Mitchell Wright:** Perfect. That works for me.

**Marcel Santilli:** Awesome. We'll keep you posted.

**Mitchell Wright:** Thanks so much. Talk soon.
