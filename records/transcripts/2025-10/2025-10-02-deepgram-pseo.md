# Deepgram pSEO

<metadata>
date: 2025-10-02
time: 15:30 UTC
duration: 27 minutes
organizer: Erik O'Brien (erik@growthx.ai)
participants: Andi Bailey, Erik O'Brien, Kirkland Gee
fathom_recording_id: 91437002
fathom_url: https://fathom.video/calls/428978650
share_url: https://fathom.video/share/Uh25jHQPDiS6Bg1nCSzwNbi6VRbtPMzG
source: fathom
enriched_on: 2025-10-02 15:57 UTC
</metadata>

---

## Summary

GrowthX engineering team reviewed PSEO pipeline best practices for the Deepgram project, focusing on publishing automation, content creation requirements, and data structure needs. Kirkland outlined that PSEO requires solving two key problems at scale: automated publishing (which depends on CMS type and page structure) and content generation (which may need external research, proprietary data, or localization via hreflang and subfolders). The team also discussed image generation text customization for Understory and llms.txt implementation, with action items filed for both blockers.

---

## Context

This was a technical working session between GrowthX delivery (Andi Bailey, Erik O'Brien) and engineering lead Kirkland Gee to align on PSEO implementation for current and prospective clients. The conversation focused on clarifying scope and requirements for the Deepgram pSEO project (ticket #604), which Andi and Erik had questions about following a client discussion. The team recorded the session to build internal PSEO documentation—this represents their effort to systematize knowledge around PSEO scope, complexity, and implementation decisions.

---

## Relevance

**To GrowthX Delivery:**
- PSEO complexity tiers from simple to complex; publishing automation is the baseline requirement and depends on CMS type and data structure (markdown, custom elements, interactive components)
- Content creation varies significantly: open-web research only vs. proprietary data ingestion vs. localization (hreflang tags, language subfolders)—each has different engineering lift
- For Deepgram specifically: must ask about publishing destination, CMS, page structure, case study integration (single vs. rotating vs. unique per page), and code snippet sourcing
- Localization adds enormous complexity; recommend English-first launch, then consider Spanish/French as secondary phase with full product/docs/homepage localization
- Recommend starting simple (markdown, 100 pages, open-web research) and validating before adding interactive features

**To GrowthX Business Development:**
- Deepgram project moving forward with scope-setting phase; Andi and Erik managing delivery
- Understory is a current blocker on image text customization—Kirkland flagged this as a workflow adjustment that requires engineering coordination
- Bubble/Ghost CMS client also in scope (separate from Deepgram); referenced WordPress client with 4,000 articles as potential complexity benchmark

**To CheckThat & Product:**
- llms.txt implementation discussion relevant to AI visibility strategy; two formats emerging (topic-URL markdown vs. full raw markdown); Firecrawl example shows topic-URL format starting point, can auto-generate from sitemap

---

## Overview

- PSEO requires solving two problems: automated publishing (depends on CMS and data structure) and content generation (may need research, proprietary data, or localization)
- Publishing automation is critical for scale (100+ pages); markdown is usually easiest starting point, but custom elements and interactive features add complexity
- For Deepgram: must ask about CMS, page structure, case study integration, and code snippet sourcing before finalizing scope
- Localization (hreflang, language subfolders) adds enormous complexity; recommend English-first then consider translations as secondary phase
- Image generation text customization for Understory requires workflow adjustment; can use separate inputs for hero and secondary text
- LLMs.txt implementation has no standard; common approaches are topic-URL markdown file (token-efficient) or full raw markdown (token-heavy); Firecrawl example shows topic-URL format; workflows can auto-generate from sitemap

---

## Key Topics

### PSEO Pipeline Setup & Best Practices

Kirkland outlined PSEO complexity as tiered; the baseline requirement is solving publishing (how is content actually getting published at scale?) and content creation (how are pages generated?). Publishing automation requires knowing the CMS type and data structure: Is it markdown-only? Does it require custom elements, interactive features, or CTAs embedded throughout? Markdown is the easiest starting point. Content creation varies significantly—some projects need only open-web research (can use GrowthX's agentic researcher, which can target specific domains or government resources), while others require proprietary data ingestion (e.g., client CSV with case studies or product examples) or localization. For Deepgram specifically: must ask about CMS, page structure, whether case studies are single/rotating/unique-per-page, and code snippet sourcing (use their docs as reference rather than researching). Localization is an enormous complexity tier—requires hreflang tags, subfolders/subdomains, localized homepage, localized product, localized docs. Recommend English-first launch with validated performance before considering translations. An example page mockup or wireframe is helpful early to catch misalignments between design and CMS data structure.

### Image Generation for Understory

Understory wants text overlaid on generated images. Current workflow uses the page topic as the custom text input. The HTML template and mapping determine what text appears where. Adjusting text requires either tweaking the topic input (hero text comes from title, subtext comes from article content via AI prompting) or modifying the HTML template and variable mappings. Full custom control (specifying exact headline and subheading) would require a significant workflow rewrite. Potential workaround: add separate input fields for hero text and secondary text, then map those into the HTML template. This is a current blocker for Understory publishing and Andi flagged it as high-priority for Katya to file.

### LLMs.txt Implementation & Standardization

No standard exists yet for llms.txt files; different companies implement them differently. Two common approaches: (1) Markdown file with topic-URL pairs and brief descriptions (token-efficient, easier for API consumption), or (2) Full raw markdown content of all pages (token-heavy, useful for in-app context but impractical for API calls as it consumes context window). Firecrawl's example shows approach #1—topic-URL pairs with brief descriptions. The file should be hosted on the client's website (e.g., domain.com/llms.txt). GrowthX has a workflow that can auto-generate llms.txt from a sitemap; Kirkland recommended starting with the topic-URL approach. For Bubble (Ghost CMS), Erik should file a ticket for the llms.txt pipeline.

### Framer Publishing

Framer previously required building a custom Framer app embedded in the client's codebase—not reusable across clients, would have to rebuild for each project. Framer recently launched MCP support, which may simplify this. Kirkland hasn't investigated fully yet but notes MCP support could make automation significantly easier. Flagged as something to revisit.

---

## Action Items

**Andi Bailey (GrowthX)**
- File high-priority ticket for Understory image text customization issue (blocking Understory publishing; Katya already investigated; needs engineering coordination on workflow adjustment)

**Erik O'Brien (GrowthX)**
- File ticket for llms.txt pipeline for Bubble (Ghost CMS)

---

## Transcript
**Andi Bailey:** Hello.

**Andi Bailey:** How are you doing?

**Erik O'Brien:** I'm good.

**Kirkland Gee:** Hey, guys.

**Andi Bailey:** How are you?

**Andi Bailey:** Hi, Kirkland.

**Andi Bailey:** Oh, you're somewhere nice, huh?

**Andi Bailey:** Just at a coffee shop, but there was a Dollar General right there, so really I thought you were outside.

**Andi Bailey:** I was like, oh, look.

**Kirkland Gee:** Not quite.

**Andi Bailey:** Almost.

**Andi Bailey:** Clean windows.

**Kirkland Gee:** Yeah, and, like, the doors open.

**Kirkland Gee:** Super nice outside today, so.

**Kirkland Gee:** I have to get out of my dungeon basement sometimes, you know?

**Andi Bailey:** Yeah, the heat went on in my house for the first time this fall.

**Kirkland Gee:** Yeah, got, like, 40-something last night, so it's wonderful.

**Andi Bailey:** Potato, potato, there.

**Andi Bailey:** Okay, so we have a bunch of questions for you really about setting up PSEO pipelines in general, and this comes from the DeepGram ticket that we talked about on Tuesday, and the questions that you had.

**Andi Bailey:** So let me link it to you.

**Kirkland Gee:** Yeah, this is not the, like, 604, do think it's the one?

**Andi Bailey:** Yeah, is 604, yeah.

**Kirkland Gee:** Yeah.

**Andi Bailey:** Okay, perfect.

**Andi Bailey:** So we, like, this is kind of, like, the high level that the client was thinking about, but I think Erik and I both, and maybe other people too, so it's good we're recording this, and we can start to, like, put this into documentation, but, like, we're not really sure, kind of, like, what format we need, what we need to ask the client for.

**Andi Bailey:** Or of that list of things, I know you said, like, okay, they're publishing, what are they publishing to, and then the languages that they have, and then the code snippets.

**Andi Bailey:** But, yeah, like, if you were to say, this ticket is 100% ready, what would it need, what would it look like?

**Kirkland Gee:** Yeah, I'm going to ramble a little bit, probably, and then we'll get to an answer, but just let me kind of talk out loud, because it's helpful.

**Kirkland Gee:** So, when I'm thinking about PSEO, programmatic SEO, there are different, I there are different layers of complexity, but let's just assume we're doing, like, the most complex version of this, right, and then work backwards.

**Kirkland Gee:** Of, like, number one solved is publishing, like, how is that content actually getting published?

**Kirkland Gee:** Because you're always doing this at scale—you're never doing just 20 PSEO pages—so you need to know how you're going to automate publishing.

**Kirkland Gee:** So that requires knowing what CMS they're on and what the data structure of those pages is. Is it a header with a markdown block of content and that's it? Or is it something more complex where code snippets are in markdown—that's not a big deal.

**Kirkland Gee:** But like, do we need anything interactive, right?

**Kirkland Gee:** Is there any, so for Deepgram, for example, do they want some kind of button you can click on the page that's going to translate some text on the page to a different language, right?

**Kirkland Gee:** Or let you speak into a microphone and display the text on the page?

**Kirkland Gee:** Are they going to do anything like that?

**Kirkland Gee:** Yes or no, like that obviously adds a pretty significant layer of complexity in terms of actually delivering it.

**Kirkland Gee:** So I tend not to recommend doing that at first, because it's like, why put all those engineering resources into a page you don't even know if it's going to work or not?

**Kirkland Gee:** Right?

**Kirkland Gee:** So in general, to get things started, markdown is easiest most of the time. If they're on a CMS like Webflow, you might end up with more than just markdown—maybe you have a header, then a paragraph, then an image somewhere in the middle of the content. That might also change the data structure.

**Kirkland Gee:** So, you know, if I'm going build a workflow that's going to do the PSEO, we can kind of, like, make markdown and then translate that into whatever structure it needs to be.

**Kirkland Gee:** But it's just helpful to understand up front if there are any custom elements and how it's getting uploaded.

**Kirkland Gee:** Is that all clear so far?

**Kirkland Gee:** And then the other side of that is thinking about, like, what is the actual content?

**Kirkland Gee:** Like, how are we going to create it?

**Kirkland Gee:** So this is, like, what goes into the creation of the PSEO pages.

**Kirkland Gee:** Do we need any external research?

**Kirkland Gee:** Are there any proprietary data sources we need to get information from?

**Kirkland Gee:** So, again, thinking about just some examples, let's say we want to do PSEO for, like,

**Kirkland Gee:** LLC creation requirements in different states.

**Kirkland Gee:** That requires a lot of external research.

**Kirkland Gee:** need to have some research agent go find information and have some way of validating it.

**Kirkland Gee:** But then like in this case, like Deepgram wants to do a case study or a customer story.

**Kirkland Gee:** How are we going to integrate that?

**Kirkland Gee:** Is there just one?

**Kirkland Gee:** Or, you know, are they going to rotate a random out of 10 different case studies regardless of the page and we just pick one of 10?

**Kirkland Gee:** Or is there a unique case study for every single page?

**Kirkland Gee:** And that's going to be related to the content itself.

**Kirkland Gee:** Like, what does that look like?

**Kirkland Gee:** Right?

**Kirkland Gee:** Is it a couple or is it a couple hundred in a big CSV file or something?

**Kirkland Gee:** And there, that can get like infinitely complex depending on what you're doing, like what the inputs are.

**Kirkland Gee:** But the biggest delineation, like even if you don't have all the details is being able to say like all the information we need from this can just come from researching the the open web.

**Kirkland Gee:** Versus, we have some sort of proprietary data from the client that we need to include in each one of these pages, because those are two very different engineering means.

**Kirkland Gee:** Like, ingesting data is like a separate sort of thing, we also have to get it from the client, and then make sure the right data goes to the right pages, all that kind of stuff.

**Kirkland Gee:** So that's the basic picture—publishing and content creation.

**Kirkland Gee:** So with external data, we can specify which sites it should go to, right?

**Andi Bailey:** Okay, and we don't need to create our own database from those sources ahead of time?

**Kirkland Gee:** Nope. We can just say go to those sites.

**Kirkland Gee:** Yeah, our researcher is really good these days—the agentic one that Daniel put together. So if you want to say, let's use the LLC example again because it's super specific, you can literally say only use government-specific resources for these states, or even just look at these specific URLs or these specific domains.

**Kirkland Gee:** There might be sometimes it goes a little bit outside of that, but not enough to really matter for the most part.

**Kirkland Gee:** And that does a really good job. So the other thing is, it's helpful early on to have an example of what the page is going to look like. If you're filing a PSEO ticket, just go into Claude and do a mock-up of what the content might look like structure-wise. One finished page is really helpful to have.

**Andi Bailey:** Erik has that. But they were going to send us some wireframes too next week.

**Kirkland Gee:** And that's where things can start to get tricky, because often we might have a design wireframe that doesn't think about how the data is going to go into the CMS, and they're a bit different sometimes. Again, if the CMS is just an H1 and markdown block, that's easy enough. But sometimes they want CTAs embedded throughout the article with custom text, or custom images, or interactive components.

**Kirkland Gee:** With SaaS companies in particular, if you want the page to do well, having something interactive is always good. But it takes more resources and time to set up initially. You're always weighing the tradeoffs—how important is it to get pages live and see how they do versus perfecting everything first? And we can always do more complicated things; it's just going to take more time. One of the pitfalls with programmatic is you spend 6, 8, 12 weeks getting the page structure and all the details perfect. When really you should just throw up some content, put 100 pages up that are kind of close, see what performs and what doesn't, then change them later. That's always an option.

**Andi Bailey:** Super helpful. Now, a question on language. Since this is about languages and one of the goals is global reach, if we're publishing in English and talking about translations, could we also publish in another language? I know we have hreflang tags, but how do we feel about that generally?

**Kirkland Gee:** We definitely can. But that's an enormous layer of complexity—even more so than adding interactive features. We'd have to do hreflang tags and set up either subfolders or subdomains. Subfolders would probably be preferable. And when you start doing other languages, you want each language subfolder to live within itself. You really don't want anything in /es linking to the main website or /fr or /de.

**Kirkland Gee:** If you're going to localize these pages, you should also have a localized homepage, or at least a localized landing page they can convert on. The product needs to be localized and the docs need to be localized. If you just throw up Spanish pages with no Spanish support anywhere in your product, it's probably not going to perform well. But it's totally doable. If you wanted to do that as a secondary phase, I think it's a great idea. Just know it needs a lot of work across their whole website, not just us creating content in other languages.

**Andi Bailey:** Got it.

**Andi Bailey:** Okay.

**Andi Bailey:** And we have 11 Labs pages as a reference. So it sounds like we need to ask them about the code snippets and case studies. You already told us what to ask.

**Kirkland Gee:** Yeah, because with code snippets of their own product, we probably don't want to just trust the researcher. We'd like guaranteed good examples, but they probably have that in their docs already. It's helpful if they can just give us good examples instead of us having to read through their documentation and figure it out ourselves.

**Andi Bailey:** Perfect. Okay, that's Deepgram. Erik, we had other questions on HyperExponential—that was the MCP versus API for Framer. They wanted to do an MCP instead of an API.

**Kirkland Gee:** Framer Publishing. Yeah. I don't think I can give you a ton right now because I looked into Framer stuff a while back. The only way to automate publishing on Framer was to build a custom Framer app and put code in your own codebase. The biggest issue is it only works for that specific client's Framer—we can't reuse it everywhere. You'd have to rebuild it for each client. But Framer just launched MCP support super recently, so I haven't looked into it much yet. That could be really interesting and might make things a lot easier.

**Andi Bailey:** Okay, that's fine. And did you set up PSEO for Ramp?

**Kirkland Gee:** I didn't do Ramp. That was Marcus.

**Andi Bailey:** Okay, so that's a question for Marcus.

**Kirkland Gee:** Yeah, because there was a ton of stuff with Sanity he figured out. Annoying but he got there.

**Andi Bailey:** And do you do the ImageGen stuff?

**Kirkland Gee:** I've done quite a bit of ImageGen stuff, yeah.

**Andi Bailey:** Okay, so we had another bug for Understory. I figured if I have you, I'm just going to throw things at you and knock them all out. Understory wants text in their images, and we were having trouble figuring out how to specify what that text is. Katya was playing around with it and couldn't specify the generated text. She's going to file a ticket. Is there a way to do that?

**Kirkland Gee:** Is there something in their pipeline I can look at?

**Andi Bailey:** Let me see.

**Kirkland Gee:** I'm looking at their article gen pipeline and the HTML templates. I think I understand, but let me share my screen.

**Kirkland Gee:** We're looking at controlling the text in these final images. You should be able to do that. The workflow takes the article content and comes up with some text. Are you saying you want to specify the exact headline and subheadline for each row?

**Andi Bailey:** I think so. That would be helpful. But if we could tweak it at this stage, even.

**Kirkland Gee:** That's definitely not doable as an image generation tweak. But you could set up a separate input for hero text and secondary text in the workflow input, then map that in this step. You can already put a custom text variable. So the header image title becomes the hero text, and the topic becomes the secondary text. But right now it takes whatever the topic is.

**Kirkland Gee:** The Final Cover Images step. So you'll have a bit of a headache because the custom text is dependent on the HTML template, and the subtext is dependent on the article content and prompting. There are ways to influence it—you could tweak the topic and rerun, or tweak the HTML template and mappings. But you can't just type in exactly what you want in both places right now. You could add a separate input for subtext with options and let it choose at random to test different variations.

**Andi Bailey:** But if it's important enough, we could adjust the workflow. So filing a ticket and coordinating with you will be good. This is a blocker for Understory publishing, so we'll mark it high when Katya files it. The question is what do they want it to say that it's not saying? Is there a way to solve it without rewriting the workflow?

**Kirkland Gee:** The AI determines the subtitles, so even if you give specific ones, it still does its own thing. But if you write really good subtitles, maybe it would work better.

**Andi Bailey:** Erik, anything else you want to ask? Do we have anything on Bubble we wanted to ask?

**Erik O'Brien:** No. But on llms.txt, how do we actually use those files?

**Kirkland Gee:** They just need to be hosted on the client's website somewhere. The URL would be domain.com/llms.txt. It's usually just a text file. Depending on the CMS, there are different ways to get it there.

**Andi Bailey:** I think Ghost supports llms.txt. So Erik, file a ticket for the llms.txt pipeline for Bubble.

**Kirkland Gee:** They use Ghost as a CMS in 2025? That's crazy—I haven't heard that name in so long. By the way, ClickUp runs their whole blog on WordPress with 4,000 articles.

**Erik O'Brien:** Does HockeyStack do it for each blog post?

**Kirkland Gee:** No, there's no right way to do llms.txt yet. It's not a standard thing—everyone's doing it differently. Firecrawl's example shows a markdown file with topic-URL pairs for their relevant pages. Some sites also have an llms-full version with all the raw markdown content of those pages, which can be token-heavy (Firecrawl's is 150,000 tokens). That only works if there's retrieval-based ingestion; if you're just passing it to an API call, most of the context window gets wasted on irrelevant content. Good place to start is topic-URL links with brief descriptions. We have a workflow that takes a sitemap and generates something like that.

**Andi Bailey:** You already submitted a ticket for Levels to have one?

**Erik O'Brien:** Yeah.

**Andi Bailey:** Thanks, Kirkland. Really appreciate your time.

**Kirkland Gee:** Of course. Thanks, guys. Bye.
