# Stackblitz <> GrowthX Weekly Sync

<metadata>
date: 2025-05-07
time: 16:01 UTC
duration: 30 minutes
organizer: Dave Capone (GrowthX)
participants: Daniel Lopes (GrowthX), George Haikal (GrowthX), Dave Capone (GrowthX), Mariana Montezzana (GrowthX Labs)
fathom_recording_id: 61273590
fathom_url: https://fathom.video/calls/293701631
share_url: https://fathom.video/share/jYEboM-vZvKgAg1VAgZYmXSdfWsdbFyP
source: fathom
enriched_on: 2026-03-03 14:30 UTC
</metadata>

---

## Summary

GrowthX and Stackblitz aligned on three main user categories for template development (web design, internal tools, mobile development) and discussed competing strategic approaches for comparison pages. The team decided that Daniel will drive a style guide for Bolt's tone and finalize comparison page strategy in a Slack message to Mitchell, while George will validate template categories against Stackblitz customer data and Mariana will research competitor feedback on Reddit and YouTube. By mid-next week, they'll have direction locked on comparison strategy, category structure, and CMS approach before starting to publish starter kit pages.

---

## Context

Stackblitz is an AI-powered IDE and code generation platform where GrowthX is engaged in content strategy for their template starter kit and competitor comparison pages. The partnership began with Stackblitz providing activity feed data to help identify which use cases their users are actually building with. Daniel and George have been analyzing this data to categorize users into distinct segments, and GrowthX is now working to define content strategy, template structure, and SEO approach across both the starter kit and comparison page projects. Mitchell Wright (Stackblitz) was invited but did not join the call; Daniel will sync him via Slack on key decisions needed before the next weekly sync.

---

## Relevance

**To GrowthX Delivery:**
- Starter kit project requires balancing SEO intent with practical usability — key tension between generic prompt engineering content versus customization tutorials that users actually need
- Stackblitz wants to generate 100+ templates across categories, so GrowthX is building a workflow that can manually create prompts and auto-generate supporting articles, requiring careful consideration of CMS integration and content scalability
- Decision needed on comparison page approach: direct competitors only (editorial, 10 pages) vs. expanded landscape (programmatic, including indirect competitors like Retool)

**To CheckThat:**
- Comparison page strategy for Bolt vs. Lovable and other AI builders is directly relevant to AI visibility and competitive positioning; SEO strategy around these comparisons impacts visibility for Bolt
- Starter kit categories and keywords (coming soon pages, e-commerce dashboards, internal tools, SaaS, etc.) feed AEO visibility research

**To GrowthX Business Development:**
- Stackblitz is focused on expanding beyond technical users to mainstream audiences (EMs, non-technical folks), signaling market segment shift
- Account is moving into deeper strategic work — template categorization, content structure, prompt engineering — indicating potential for expansion and longer engagement

---

## Overview

- Data analysis confirmed three main user categories: web design, internal tools, and mobile development — aligns with prior insights from KJ
- Stackblitz wants to target less technical users (EMs, internal tool builders) as primary audience alongside technical developers
- Comparison pages strategy decision pending: target top 10 direct competitors only (editorial approach) or expand to indirect competitors like Retool (requires programmatic generation)
- Bolt outperforms Lovable and other competitors on detailed, complex prompts with high visual fidelity — strong differentiator for prompt-based content
- Starter kit approach: manually create 100+ prompts across categories (admin/dashboard, e-commerce, SaaS, etc.), auto-generate article content with repeatable layout (prompt explanation, customization guide, keyword optimization)

---

## Key Topics

### Data Analysis and User Categories

Daniel presented analysis of Stackblitz activity feed data that he and George processed through a custom Airtable workflow. The workflow parses activity timelines, captures category shifts (users often start with full-stack and pivot to web design or other categories), and classifies each session into the dominant category. Analysis identified three main user categories: web design, internal tools, and mobile development. This aligns with previous insights KJ shared, validating the segmentation approach.

### Comparison Pages Strategy

Two competing approaches emerged for comparison pages: either compare Bolt directly against single competitors (e.g., "Bolt vs. Lovable for web design") or compare against competitors within specific use cases (e.g., "Bolt vs. Lovable for e-commerce"). Bolt has distinct advantages on specific use cases — for example, it's the only tool supporting Expo for mobile development. The team debated whether to pursue a purely editorial strategy targeting top 10 competitors or expand programmatically to include indirect competitors like Retool, which internal tool builders use even though it's not an AI builder. Mitchell's input is needed to finalize approach before next sync.

### Starter Kit Prompts and Templates

Daniel demonstrated several complex prompts he's tested that generate high-fidelity outputs: e-commerce dashboards, CRM systems, agency portfolio sites, all created in one shot with detailed prompts. Bolt significantly outperforms Lovable and V0 on these detailed prompts, matching the positioning Daniel observed on Reddit. The team aims to build a library of 100+ templates across categories, starting with 15 core categories and expanding during the 12-week engagement.

### Content Strategy for Starter Kit Pages

Key tension emerged around whether to focus pages on prompt engineering (how Bolt creates things) versus prompt customization (how to modify prompts to your needs). Dave advocated for the customization approach — explaining what the prompt does and how to change it for your desired output — as more directly serving user intent. The team will use a repeatable layout: title, category page with keyword targets, and product pages with prompt explanation, customization guide, and keyword optimization. They'll manually create prompts and use a workflow to auto-generate articles.

### Technical and CMS Considerations

The team needs to align with Mitchell on CMS approach: whether to build pages behind their Strapi endpoints connected to GitHub, or to host generated templates as screenshots. Daniel will send a Slack message to Mitchell to clarify CMS strategy and GitHub access before the next sync. This decision affects how scalable the programmatic content generation can be.

### Category Structure and Granularity

Main categories are Internal App and Web Design, with potential for Mobile Apps. Subcategories include admin/dashboard, e-commerce, SaaS, portfolio, coming soon pages, and others. The team debated whether to go granular with feature-level templates (e.g., "build a calculator") or full-fledged templates (e.g., "build an e-commerce site"). Coming soon pages are important because they're a separate category in major template marketplaces.

### User Audience and Market Positioning

Stackblitz is intentionally pivoting to target less technical users — EMs, internal tool builders, business users — rather than just developers. This affects both the starter kit and comparison page content strategy. The team needs to understand whether buyers and users are the same persona or different, which could impact page structure and comparison depth.

---

## Action Items

**Daniel Lopes (GrowthX)**
- Create style guide for Bolt's writing tone and finalize comparison page strategy (direct competitors vs. expanded landscape)
- Research competitors for editor comparisons and send Slack message to Mitchell with questions about project direction, CMS setup, and GitHub access
- Continue developing complex prompts; pause template creation to focus on finalizing categories, design approach, and programmatic workflow

**George Haikal (GrowthX)**
- Cross-check the top templates list with customer data from upcoming call with Stackblitz's customer experience person to validate category choices

**Mariana Montezzana (GrowthX Labs)**
- Conduct deeper research on Reddit and YouTube comments about competitors; capture findings in table format starting with Lovable, then replicate approach for other tools
- Note potential features mentioned by Mitchell and any user feature requests visible in community discussions

---

## Transcript

**Daniel Lopes:** Let me just record this. I don't know who owns the meeting. Okay, let's see.

**George Haikal:** Oh, I'll switch.

**Daniel Lopes:** One sec. There's like 10 recordings. Yeah, let's see. Somebody's taking notes, I guess somebody's recording. Mine is not.

**Dave Capone:** I think mine's, my Fathom is working. Cool. Okay.

**Daniel Lopes:** Yeah, so. One second. Yeah, so I was going to let me just show you all what I was working through, and then we can calibrate on there, and then I don't know if we need to send. All two mutual assets, but we can decide later. Like the thing that I don't know if we had a chance to see, but let me move my screen to the side, so let's all see. The stuff that I was doing, like George and I were doing with the data that we have from then, so we have, they gave us access to a ton of, they gave us access to a lot of data. So the data came in this form, it came in like an activity feed like this, a pretty long format, and you can see this bit of what people are trying to do on each section. We didn't have the precise, like we have like the prompts, what they're trying to do with each step and then but like it's pretty long pretty hard to parse and not categorized so what we did was to create a custom workflow for them that went through each of the activities. This workflow we have in Airtable. I linked there. You guys have access to that if you want to check it out.

**Daniel Lopes:** The workflow is just going to parse the activity and summarize including the days split so you can see what people started doing and then what they came back to later. So many times people start doing like an app, like an internal app, just like trying something out full stack, and then they will come back and like do something else like do a web design, like create a website, create a landing page. So people were doing two different things. But then I also asked it to categorize. The category is not super, super precise. It's just going to be whatever was more prevalent in the session. So in this case, for example, the person was creating a full stack app with Tailwind, and then was single page. And then it came back later and added multiple pages, integrated Supabase for the database. So the result was like that because they started creating this no-code team design. So it's not super, super precise, but it can give you an idea of more or less what people are trying to do better than just looking at the sessions.

**Daniel Lopes:** And the output of that was a mix of things. So people are doing three main things. People are doing web design, they're doing internal tools, and they're doing mobile development. And that aligns with what KJ was showing us. So if we do the analysis on the category that he sent us, this is aligned with what KJ was thinking. So I think the way we can think about this is that we have these three main categories, and then we need to decide if we're going to target based on that, or are we just going to target based on the competitors, because competitors can do anything.

**Daniel Lopes:** That's the thing on the comparison pages we'll have to figure out. I will probably need to align that with Mitchell whenever we can, probably just send a message to him. So I was thinking from the comparison side, we could either do comparison Bolt versus X, or we can do Bolt versus X for Y, you know, and then we can do like for web design, for mobile. So for mobile, for example, Bolt is the only one that I think supports Expo. So Expo is a way to create mobile apps using React. And Bolt is also really good at creating really great websites, almost one shot. They do that much better than everyone else. So if you do Bolt versus Lovable for web design, Bolt is way better. And I don't know if people would be searching for that. That's the problem, though. So I don't know what's the SEO strategy there, but the usability of the page would target their persona that is paying more, I think. So that's the thing we can talk about later.

**Daniel Lopes:** But from the other stuff that I was doing yesterday. So we're essentially like mid-week three. And we have essentially three projects in progress. So we have the comparison and supporting tools. So as far as I'm thinking would be like Cursor and Windsurf, the coding editors. I don't know if we should have two different templates for that, or if it should be the same. And then in the content of the comparison, we explained that they're not direct competitors, they're more supporting tools. So that would change the design or change the title. I don't know what's the strategy there, Dave, for SEO reasons, but something to keep in mind.

**Daniel Lopes:** And so like for this week, I think if we could get this week and by next week have like a style guide for how we write, like the tone that Bolt uses, and we're like pretty happy with the result. And you can have like one real calibration protocol for like the comparison, Lovable versus Bolt. Or if we go to the use case, Lovable versus Bolt for X, like have these articles like handcrafted. Because as we start going through the articles, like there might be things that we want to do automated, like a workflow would generate some of that. Or if another thing we need to check is if we want to do all like their top competitors, let's say like 10, because that's kind of what they have, or do we want to do an expanded list of where you compare to almost everything? And we compare like not only to their direct competitors, but also to indirect competitors. Like Retool is not an AI building tool, but it's an internal tool building tool. So people would not be looking for that, but people that are building internal tools are using Retool. So I don't know if there is a play there, Dave, if we want to do that or not. But if it's like 10 competitors, it's easy to do editorial. If we want to do all the tools that you can use to build no-code stuff, like Retool and the others, then we need to be programmatic for sure. So that's another decision we have to make, and we probably should align with Mitchell there.

**Daniel Lopes:** So this week, by mid-next week, when we meet with him again, if we have all these things figured out for the comparisons, I think we're in a good spot. And then next week, we also, like for both projects, the Starter Kit and the comparisons, we need to start figuring out how we can do CMS. And so that's something I need to calibrate with him, like what's going to be the technical team collaboration there. They give us access to their project, like their GitHub, and we connect to the Strapi endpoints. We can set up the Strapi side. That's not a problem. The problem is how we build the UI, I think. But I think we can get there.

**Daniel Lopes:** And maybe the following week, once we have the CMS set up and we have these things figured out, we can start thinking about publishing some of those pages on the comparison side. And then the starter kit side, we're still figuring out the prototype, what kind of prompt should we have, the design, and we're going to have to also figure out the CMS. And then at the same time, George is also starting the process of jobs to be done. I think jobs to be done would help us recalibrate the style and the articles. Once we have the tone right, who are the main personas? It might even change the level of the comparison pages if we see that people that actually buy are different people. But the main thing that I keep coming to is that do we want to make this just an SEO play just to rank or do we want to make the pages perform? And that's what I think will change quite a bit for the comparison pages and maybe even the starter kit.

**Daniel Lopes:** And for the starter kit, what I was working on this week was essentially trying a bunch of different complex prompts and seeing if we can get really good results. For example, this is the prompt, like a pretty long prompt, but it's easy to understand. So a non-technical person can read this and understand that this is an e-commerce dashboard. And then you can change the menu items here, you can change the behavior, you can make it red instead of blue, stuff like that. And the result of that prompt is this. So like one shot, no changes, you get this. So we're putting together a list of prompts that do things like that. This is another one, pretty good. It's essentially a CRM. Some pages don't work, but the first page will work really well. And then we have some agency-related stuff like websites. There's a website for an agency. This one has all the animations, has all the details. These are fantastic. This one is pretty cool. And Bolt gets everything 100% right if it's detailed like the way I'm doing. The other ones don't. So Lovable and Vercel's V0 can't do that in the same way. And you see people talking about it on Reddit as well.

**Daniel Lopes:** So I'm going through some of the common categories that people would be looking for. And I think we have 15. I think it would be pretty easy to get to, maybe not in the beginning, but throughout the 12 weeks, we can easily get to 100, I think. And the main thing here would be like we create these prompts and we have a page like this, where we would have the content of that page. And that's the thing that I'm still figuring out, Dave. Maybe I need your help here. Is like this would be a third page in. So like they have their homepage and they might have like a catalog, like an index page with the category. And then this would be the third page. And I think we need to find the keywords that would be things that people would be searching for based on no code, low code, or AI generation for very specific things. So it would be probably like no code AI, like generate a splash page or a coming soon page using AI, something like that.

**Dave Capone:** Yeah, I talked to Ren about this about 15 minutes ago, and what we're thinking is that you're right, this is a third-level page. This would be like a product detail page. So what we are going to build is a category page. So we'll go from their index to a category. Category would be like coming soon. And then we would have all the different designs for coming soon as the product pages. So that layout we'll have an example later on today. How are you thinking about the content of those pages, though?

**Daniel Lopes:** That's what I'm trying to figure out, the strategy around the keywords that we'd be trying to rank for. Because they're pretty niche. They would be like coming soon, like creating a coming soon page, essentially. That's the people that we're trying to look for. So we would insert those keywords into those categories.

**Dave Capone:** So it would be typically like a starter kits would be your index page, right? Where you're coming in on that page, then splash pages or coming soon, right? So like if coming soon would be your category page, we would just have how to build coming soon landing pages with no code or low code coming soon landing pages. So we can add those keywords to any of those categories to go after it. But ideally, it'd be great to rank for those broad keywords as well so that we can get coming soon landing pages and no code coming soon. Yeah, so we'll build it in that way where we can capture the most traffic.

**Daniel Lopes:** Got it. So that's the workflow that we're going to have to do. Because let's say we put together the content of the article here, this one is all about prompt engineering. I don't know if that's the level that they want to be with, or if it should be about the prompt itself. But I was writing this article, which would be more like what is the starter kit? And we probably could have a bunch of the primary and secondary keywords at the top. And then the bottom part would be explaining how to customize the prompt to your needs. So that's the split between usability of the prompt versus trying to rank for different things here. So we should have similar content article for everything, but just vary a little bit of the content. But if we had an article written for each prompt explaining how to change the prompt, that was a tutorial for the prompt itself, you know what I mean, Dave?

**Dave Capone:** Yeah, that's where I was leaning towards, because if we can explain what the prompts are doing and how to change the prompts to get your ideal generation or output, that would probably be better than having like the generic layout the way this is now. From an e-commerce perspective, the content could be a little bit similar on how we walk the user through the experience of like, here's the prompt, this is what the prompt does, here's how to customize that prompt. That layout can be repeatable, that's fine. But we just have to be more succinct on the content that we give or on the prompting. So I think best success would be to go the route of what you're thinking of: let's give them the prompt, let's tell them what the prompt does, and then have to change that prompt to get the specific output that you want. I think that would probably be, from an SEO perspective, we can sprinkle in the keywords we need. But from an intent perspective, I think the main intent of the page is someone wants to build this, and we have to provide that to them.

**Daniel Lopes:** Yeah, okay, so I'll tweak this. The way I'm thinking is that we would manually create all the prompts and then we have a workflow that would generate the articles. So the workflow would be like the title, like H1, the sub description, the intro, and we have whatever other titles we need that are important for SEO and then generate the whole bottom part one shot based on the prompt. And so if we have the place where we could keep adding things to their template library and we can generate more articles for them, so I could see the case where in the future we could pay somebody to just continue to generate the templates based on the original that I'm starting. But it would always be a little slower than creating traditional articles because you have to write the template, run it, see if you actually generate something. And you also have to host it. So we're also going to need to check with Mitchell if this is even possible in their setup. If it doesn't work, we'd have to take a screenshot, so that would be another workflow.

**Daniel Lopes:** Yeah, so this is the direction for the templates project.

**Dave Capone:** Daniel, you have a list of the current categories that we have? Like, I'm thinking that I could potentially put together like a hierarchy for that, so we can kind of put a mock category structure together to understand what the different categories could be and then the different templates that we can have in each individual one.

**Daniel Lopes:** The areas would be like macro-level areas would be like internal app and web design. And then each one of those would probably have like a bunch of categories. So I have some of that here in a separate document that I was just like doing some research. And with the stuff that we got from KJ, I think it still applies. So top categories like admin and dashboard that fits their internal app. E-commerce templates fit the web design, SaaS, internal app. So I was just going to organize this based on these two main areas, like internal apps and web design. We might want to add another one for mobile apps that they don't have.

**Dave Capone:** This works. So if you're building a SaaS template for your website, you're going to start with a splash page. And then once your site is up, then you'll switch over to one of the SaaS templates. So it's almost like we have two different types of templates. We have the features one where it's like build a calculator, build a reporting dashboard. Like those are the different types of features or things you can do with it. These are more of like a full-fledged e-commerce website, right? Like a full-fledged template of that website.

**Daniel Lopes:** I think we need to think about this because you have it might go super granular if we start thinking about chunks of the products, you know?

**Dave Capone:** So my point was that what we're presenting in the mock-up in Figma, we should be really focused on building an e-commerce website and then show that as the mock, if this is the route that we want to go, versus just the coming soon page.

**Daniel Lopes:** The main reason for the coming soon page is because it's actually a category in a lot of the template stores. People buy coming soon pages, standalone coming soon pages. So that's where I start from. But that's a fair point.

**George Haikal:** Daniel, can you cross-check that top templates list that you just showed? We don't need to go super deep on the jobs to be done to get a better understanding from their customer experience person that I'm talking to in an hour on what their users are actually trying to build. So I can cross-check what you populated there with any and all data she has on their current users that's more specific to help.

**Daniel Lopes:** Because like, this is like, it's essentially handcrafted templates. I don't even know if the category will be, like if we're going to have a ton per category, you know? Like with sales, if they have use cases, if you filter for portfolio, they have like six. If you filter for SaaS, they have a bunch. But if you filter for e-commerce, they also have a bunch. If you filter for certain things, they actually have quite a few. For some stuff, they don't have a lot. So very specific. So I don't think they would be ranking for any of this stuff. So I don't think they're targeting. They're just going based on community contributions. But these are featured. Like they're flagging this from the community as high-value stuff just to show. This is a consulting shop, for example. It's pretty technical, though.

**Daniel Lopes:** Like, this is different than V0. So Vercel is the hosting company, the same way as StackBlitz is the hosting for Bolt. And V0 is their competitor for Bolt. So V0, the way I see V0 is for more technical users, even just because of the audience of Vercel. Lovable and Bolt are more like higher-level folks that don't have that much technical skills. So it's EMs, people who build internal tools. That kind of fits the profile of technical folks. They have a mix. So that's the thing that we need to think about their audience. They have a mix of both, but I think they want to target the less technical folks for a business reason.

**Daniel Lopes:** So I'm going to pause a bit on creating the prompts, because like it's pretty clear that they work. So I'm just going to think about the categories, find the source for them, and thinking about the design a little bit further. But think about the programmatic parts that we need for creating the workflow to generate the data for those pages, and start thinking about the CMS. And I think we need to work on the editor stuff, maybe closer together, Mariana, because I understand their space really well, so I can probably do a little bit of research on some of the competitors at the same time today and share with you. So we have like use cases and stuff like that. And then we have to decide if we do stay like high level or if we go lower level on the use case. But I can write the message after this call. So then we ask those questions to Mitchell or we can pull him into a separate meeting if we need to get him to answer those things.

**Daniel Lopes:** That would be the main thing. I think for the comparisons, I figure out the level.

**Mariana Montezzana:** I'll do a deeper research on what people are saying on Reddit and on YouTube. So I already saw a bunch of threads on Reddit and YouTube, but I'll start capturing that information in a table form.

**Daniel Lopes:** I can read that too. Cool. I'll start with Lovable and then find a way to do it and replicate to the rest of the competitors.

**Mariana Montezzana:** Sounds good.

**Daniel Lopes:** I put in the folder in the documents. I kind of changed their documents for quite a bit. There's potential features that Mitchell gave us. So when you're going through, it would be nice to think about them, but there are other things that the users are also talking about in Reddit and stuff like that. Cool. I got to run, but I don't think we need to send this video to Mitchell. We are talking a lot about running over planning, but I can send an email to him, send a message in Slack. I have a call now in two minutes, but after that I can write the email, the Slack message. Thank you, everybody.

**Mariana Montezzana:** Thanks, Daniel.

**Daniel Lopes:** All right. Bye-bye.
