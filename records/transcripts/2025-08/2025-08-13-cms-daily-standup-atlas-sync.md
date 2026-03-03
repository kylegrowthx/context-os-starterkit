# CMs Daily Standup – Atlas Sync

<metadata>
date: 2025-08-13
time: 15:31 UTC
duration: 34 minutes
organizer: Saskia Wartnaby (GrowthX)
participants: Matthew Panzarino (GrowthX), Matthew Alves-Hill (GrowthX), Tiandra Burns (GrowthX), Iana Medvedeva (GrowthX), Jenn Peters (GrowthX), Saskia Wartnaby (GrowthX), Mariana Montezzana (GrowthX)
fathom_recording_id: 80318065
fathom_url: https://fathom.video/calls/378008004
share_url: https://fathom.video/share/oNDKDbTsMzq8JahtJyoAtbpvrKwgE71s
source: fathom
enriched_on: 2026-03-03 12:45 UTC
</metadata>

---

## Summary

Matthew Panzarino led the team through major Atlas updates including a new AI Assistant with contextual window capabilities for drafting and a redesigned sidebar for rich text editing that auto-populates with client artifacts. Image generation templates have been moved into artifacts for better management, with the Monograph client using this workflow to generate branded graphics. Matthew emphasized the importance of identifying and filing tickets for repetitive manual tasks to continuously improve pipeline efficiency, pushing the team toward delivery-ready output.

---

## Context

This is a GrowthX internal standby for the Content Management Systems (CMS) team focused on Atlas, the platform powering their content delivery pipeline. The meeting reviews recent platform improvements and unblocks technical issues. All attendees are GrowthX team members working on content operations, design, and platform optimization. The team manages multiple client pipelines and workflows, including work for clients like Monograph, Biologica, and Aimbit.

---

## Relevance

- **To GrowthX Delivery:** New AI Assistant sidebar and contextual artifact capabilities enable faster drafting and editing. Image generation templates now live in artifacts rather than input fields, improving maintainability. Team should adopt these features immediately and file tickets for any bugs or limitations.
- **To GrowthX Delivery:** Adventures Group client has a multi-location artifact issue where all location guidelines appear in all pipeline contexts. Workaround: change artifact type from "guidelines" to "rule" to prevent auto-population. Long-term solution needed for multi-pipeline clients.
- **To GrowthX Delivery:** External data point linking for articles remains manual. Requested capability: centralized URL management system (similar to Biologica's knowledge base or Aimbit's glossary) to inject consistent source citations into fact-checking workflows.
- **To GrowthX Business Development:** Matthew reframed pipeline customization as a core competitive advantage — teams should continuously optimize workflows by articulating pain points, not just accept generic pipelines. This drives efficiency and delivery speed.

---

## Overview

- New AI Assistant contextual window enables drafting with auto-populated client artifacts and customizable context selection
- Improved sidebar in rich text editor automatically surfaces field content and contextual artifacts; users can add or remove artifacts as needed
- Image generation templates moved from input fields into artifacts for better management and easier tweaking (Monograph using this workflow for branded graphics)
- Team encouraged to identify and file detailed tickets for repetitive manual tasks to unlock pipeline automation opportunities
- Emphasis on continuous pipeline customization: teams should articulate pain points, not accept generic workflows

---

## Key Topics

### AI Assistant Enhancements

The new Assistant is a contextual window designed to help teams draft articles and outlines with embedded client context. It auto-populates with core contextual artifacts and can accept additional artifacts defined in the client workspace. Users can remove specific artifacts if they want to focus on a single resource. The sidebar (new in this update) automatically surfaces field content and all related artifacts as context, so teams don't need to manually paste copy or external documents into Claude projects. Matthew stressed this is faster and cleaner than external workflows.

### Image Generation Templates

Templates for image generation are now stored as artifacts instead of scattered across input fields. This makes them easier to maintain and iterate. The Monograph client provides a concrete example: the design team creates an HTML template specifying canvas dimensions, text placement, logo position, and brand elements. The pipeline then uses this template to feed into Recraft (the image generation tool) and produces consistent branded graphics. A custom text field allows overriding auto-generated captions when needed.

### Adventures Group Multi-Location Issue

Adventures Group has three separate location pipelines, but all location artifacts (writing guidelines, context) appear in the AI chat context for all pipelines. This causes confusion about which guidelines apply where. Matthew suggested a quick workaround: change the artifact type from "guidelines" to "rule" in the artifact settings—this prevents auto-population in the AI assistant sidebar. Long-term, a more systematic approach is needed for multi-pipeline clients with shared or location-specific artifacts.

### External Data Point Linking

Tiandra Burns raised a request: can Atlas create a centralized repository for frequently-used URLs (external data points) so they're automatically injected during fact-checking? Currently, she manually adds the same URLs to every article. Matthew pointed to existing knowledge base implementations (Biologica's ingredients database, Aimbit's glossary and technical documentation) as potential models. These could be adapted to work with URLs instead of full content. He recommended filing a detailed ticket with the URL list, pipeline link, and use case for further exploration.

### Continuous Pipeline Optimization Philosophy

Matthew closed with a broader message: teams should stop accepting generic pipelines as-is. The bicycle analogy: don't just pull a bike out of the box; adjust the seat, check the brakes, and customize it for your use. Similarly, teams should identify where manual work is happening (anything done 2-3 times a week), articulate it, define the logic, and file a ticket. This feeds back into development to convert manual steps into automated workflows. The goal: drop something at the pipeline's start, wait a few minutes, and get near-delivery-ready output at the end.

---

## Action Items

**Tiandra Burns (GrowthX)**
- Test changing 1 Adventures Group artifact to "rule" to prevent auto-population in AI chat. Verify the change doesn't break the primary pipeline.

- File ticket documenting Adventures Group artifacts appearing across all three location pipelines. Tag Matthew Panzarino and Pedro for engineering review.

- Create detailed ticket for centralized URL/data point management system. Include the URL file, relevant pipeline link, and use case from Aimbit. Tag Matthew Panzarino and Pedro.

---

## Transcript
**Matthew Panzarino:** The Assistant is basically a contextual window that you can use to start anything you want.

**Matthew Panzarino:** So as an example, some of you have been asking about generating outlines with all of the context.

**Matthew Panzarino:** Some of you may even have cloud projects for generating outlines or doing it in ChatGPT, which is fine.

**Matthew Panzarino:** I get it.

**Matthew Panzarino:** You need to generate them, so you need to give it context and have it generate outlines for you.

**Matthew Panzarino:** This Assistant can do that.

**Matthew Panzarino:** You can see here it currently auto-populates with all of the contextual artifacts, so the core three, I should say.

**Matthew Panzarino:** You can call any other artifacts as well.

**Matthew Panzarino:** So if you have additional artifacts defined here, so in Biologica we have some of these dossiers defined, you can add these other dossiers.

**Matthew Panzarino:** We'll work on the little ellipses here, but at the very least you can hover them to see which ones you've picked.

**Matthew Panzarino:** So you can add other contextual documents to this as well, and then

**Matthew Panzarino:** And you can say, hey, I'd like you to create an outline for this kind of article, or I'd like you to draft for me an article, whatever.

**Matthew Panzarino:** You can do that work here.

**Matthew Panzarino:** And the fun thing about it is that it kind of comes with built-in context for the client that you're working on.

**Matthew Panzarino:** So that you can pull your favorite Claude, only at the moment, but pull your favorite Claude model and do a little work on it.

**Matthew Panzarino:** You can paste copy in here and edit it.

**Matthew Panzarino:** You can do all kinds of stuff.

**Matthew Panzarino:** So I just want to throw it out there that this is like a built-in Claude project where you can call in context that you're working on with the client and then do work in here.

**Matthew Panzarino:** So putting that out there, should experiment with that, play around with it.

**Matthew Panzarino:** The second thing is in the AI assistant. So the way that the AI assistant works has been updated as well.

**Matthew Panzarino:** So as an example, we've got a rich text window here that is obviously any of the outputs should be rich text windows.

**Matthew Panzarino:** Some of the input windows are as well.

**Matthew Panzarino:** When you click into this window, you can see that the assistant in the sidebar will automatically pop open.

**Matthew Panzarino:** It's no longer just the little hover pop-up thing.

**Matthew Panzarino:** It now is a sidebar, which is, in my opinion, improvement.

**Matthew Panzarino:** It also calls the contextual artifacts.

**Matthew Panzarino:** You can take them out if you only wanted to work with one particular artifact at a time, let's say, just writing guidelines.

**Matthew Panzarino:** But it starts with them as default.

**Matthew Panzarino:** And it also takes this field content, so all of the content that is in this field, and it embeds that as context.

**Matthew Panzarino:** You see the field content here?

**Matthew Panzarino:** So you can start working on this with some understanding.

**Matthew Panzarino:** it's time

**Matthew Panzarino:** Understanding that it is calling all of the artifacts that are related to your client, or at least the three core artifacts. And then, of course, once again, you can add additional artifacts in here that you've defined.

**Matthew Panzarino:** So any artifacts you've defined in the artifacts for this client, you can call into this window.

**Matthew Panzarino:** But it also works with the full context.

**Matthew Panzarino:** It takes all this text, and it knows it's working on that text.

**Matthew Panzarino:** So if you ask it to do something, you don't need to paste in text or whatever.

**Matthew Panzarino:** It already has the context of this field, plus the contextual artifacts here.

**Matthew Panzarino:** So you can start working on it, reflow it, apply writing guidelines again, double check this to make sure writing guidelines are applied.

**Matthew Panzarino:** You know, anything that you want to do there, you can start working on it right here, and then it will go through the normal process.

**Matthew Panzarino:** So I wanted to call out those improvements to the way that this is working, and encourage you to experiment with it, because it basically is like a built-in, fully contextualized Claude editor that you can use, rather than having to jump out and embed contextual artifacts into a Claude window and do that. This is built-in Claude, so it's going to be very similar.

**Matthew Panzarino:** So give that a stab and play around with that.

**Matthew Panzarino:** I think it's important to kind of understand and see the improvements there.

**Matthew Panzarino:** So those are some things that I wanted to flag off the top.

**Matthew Panzarino:** Any questions about that?

**Matthew Panzarino:** Okay, Ratsky will continue to work on that, and it will continue to improve.

**Matthew Panzarino:** If you see bugs or issues with it, especially anything that occurs more than once, please do file a ticket.

**Matthew Panzarino:** But the improvements there are continuing to be pretty rapid.

**Matthew Panzarino:** You know, the inclusion of the context and the sidebar, the assistant, all of that stuff is relatively fresh.

**Matthew Panzarino:** So keep playing around with that.

**Matthew Panzarino:** It will get better as we go.

**Matthew Panzarino:** Matt, you had a question, and I didn't quite understand it, I'm sorry, but in the learnings channel, you said something about HTML Atlas.

**Matthew Panzarino:** Talk to me about that.

**Matthew Panzarino:** What's your question there? And welcome back.

**Matthew Alves-Hill:** Yeah.

**Matthew Alves-Hill:** I think it's literally just related to this image, Jen, that was added while I was out of office, and Katya wasn't up yet.

**Matthew Alves-Hill:** So I think it seems very straightforward.

**Matthew Alves-Hill:** Basically, it's just setting rules for the image generation.

**Matthew Alves-Hill:** So I wasn't sure if it was article layout related or anything.

**Matthew Panzarino:** Yeah, so for clients with image gen, you define the images in the input stage. I can't remember—do any of our clients use this, or are we experimenting with it? Is it Monograph?

**Iana Medvedeva:** Yeah.

**Matthew Panzarino:** it's Monograph.

**Matthew Panzarino:** Yeah, yeah.

**Matthew Panzarino:** So, just so anybody knows, if Katya specs out an image pipeline or image workflow for your client, the input will have additional fields. Some of those fields will be image aspect ratio and stuff like that. The image template field only appears on new creation, though—we may have moved it.

**Iana Medvedeva:** Monograph doesn't have it in.

**Iana Medvedeva:** There is no field to put HTML code, or it's somewhere inside, or it's somewhere built in, right now, so you don't need to manually put it there, just choose a ratio.

**Matthew Panzarino:** Yeah, it makes it hard to demonstrate, because I was looking for something that doesn't exist.

**Matthew Panzarino:** But the way it works is that there's a field where you choose your aspect ratio based on what the client wanted. And by the way, we filed a ticket so you should be able to enter custom text as well.

**Matthew Panzarino:** If yours, if your image gen does not support this, let us know, but custom text would be like custom caption over the top of the image.

**Matthew Panzarino:** There's also a field—the template—that feeds into Recraft to create the image. It's basically a template that says, "Make a canvas like this, put the text here, put images here." That's what the HTML is, Matt, and you're exactly right—it's for image gen.

**Matthew Panzarino:** It's not related to article format at all.

**Matthew Panzarino:** Even though it may look like a formatting document for an HTML templated page, it is not related to that.

**Matthew Panzarino:** It is all about creating the image, making sure that the image looks the way you want it to look.

**Iana Medvedeva:** I see it in artifacts right now.

**Iana Medvedeva:** In the context of artifacts.

**Iana Medvedeva:** I see it in artifacts right now.

**Matthew Panzarino:** Oh, yeah.

**Matthew Panzarino:** And so I'm glad that happened because I think it needs to live in artifacts versus in the input field. You can see here that the templates are now there, and the formatting is a bit unusual.

**Matthew Panzarino:** So if you see any of this, that's what it is. You can see it defines a canvas width and height, and a container, etc.

**Matthew Panzarino:** This is something the design team would be doing for you, obviously.

**Matthew Panzarino:** You would give it the specs, you would give them the specs, give them all the information that you need, and then they would build this for you so that we can output a reliable.

**Matthew Panzarino:** image repeatedly.

**Matthew Panzarino:** And it lives in artifacts now instead of just in the random input field to a pipeline, which is really where it should live. The resulting output is relatively repeatable.

**Matthew Panzarino:** So Monograph likes this particular design, which now comes out at the end of every article. The custom text caption here is what the custom text field can do.

**Matthew Panzarino:** So we can override the auto-generated text with custom text. This text is normally pulled from the body copy by the workflow.

**Matthew Panzarino:** It asks, "What would be a good caption text for this?" and puts it there. So we can override that with custom text.

**Matthew Panzarino:** Anyhow, long-winded way of saying, Matt, that's an image template.

**Matthew Alves-Hill:** Thanks.

**Matthew Panzarino:** Mm-hmm.

**Matthew Panzarino:** And I just realized I wasn't sharing my screen, so I was poking at stuff and pointing at it, but no one could see it.

**Saskia Wartnaby:** I was going to say something, but I wasn't sure.

**Jenn Peters:** I wasn't sure if we were meant to be seeing that, or if you were just describing it.

**Matthew Panzarino:** So just a quick tour of the artifacts: the template is here. It's hard to see, but basically it specifies logo, custom text, etc. This template was created by the design team.

**Matthew Panzarino:** So you would file a ticket and have them build this image template for you. The template lives as an artifact, which is how it should be, because it can be tweaked if we need to change something.

**Matthew Panzarino:** The image gen will then produce graphics like this. Monograph likes this particular design.

**Matthew Panzarino:** So you can see that the caption appears here.

**Iana Medvedeva:** I think Marcus is working on it because we had a bug. It was putting random phrases like "hello world."

**Matthew Panzarino:** The idea is it defines a caption that it pulls from the body copy and then puts graphics that have been defined by the client. You need brand guidelines, fonts, and examples of what they want.

**Matthew Panzarino:** Then we go through a process of generating different variants, they pick one or ask for tweaks, and once you get to something they like, that template becomes part of the pipeline.

**Matthew Panzarino:** And then the image gen can happen.

**Matthew Panzarino:** We can build something like this for any client. If it's more complicated with specific brand placement and guidelines, it'll take longer, but it's almost certain we can create it.

**Matthew Panzarino:** So if you have a client that needs this, file a ticket and get with the design team. The custom text override is something we built for Monograph because they wanted very specific captions in some cases.

**Matthew Panzarino:** So you should be able to override that caption using this field. That's a quick visual tour of what I was explaining earlier. Any questions about that?

**Matthew Panzarino:** Okay, opening the floor to any other blockers or questions or issues.

**Tiandra Burns:** I have two things. As far as the field content:

**Tiandra Burns:** For the adventures group, we have three separate pipelines for the three different locations, and it seems that it's calling in all of the artifacts in the field context.

**Tiandra Burns:** I mean, I can delete them, the ones that I don't need, but I've noticed for one of my pipelines, it has the other two location writing guidelines and things like that.

**Tiandra Burns:** I haven't really noticed that it's changing the context or anything, but just to...

**Matthew Panzarino:** And you're talking about specifically in the AI chat?

**Tiandra Burns:** Yeah, in the field context AI chat at the bottom. It takes in all of them from the three locations.

**Matthew Panzarino:** So you'd see the ones from all locations—Cabo, Vallarta, etc. Okay, interesting. I'm trying to think about the best way to solve that.

**Matthew Panzarino:** What pulls them is anything defined in the guidelines section. So one easy way for you to fix that might be to take them and make them rules.

**Matthew Panzarino:** And see if it auto-populates them. Try one first: change its type to a rule. It won't affect where it gets called. The fact that it's a writing guideline or under the guidelines section doesn't matter to the system.

**Matthew Panzarino:** To the article generation system or to the workflows—the outline generator or brief generator—the label doesn't mean anything.

**Matthew Panzarino:** This labeling is for humans mostly. However, I have a hunch that the AI assistant uses this labeling to pull whatever's in the guidelines section in as context by default.

**Matthew Panzarino:** So experiment with changing one to a rule and see if it still auto-populates after you save. If it doesn't, change them all to rules.

**Matthew Panzarino:** I don't think it should affect anything else.

**Matthew Panzarino:** It will just affect whether or not they get called.

**Matthew Panzarino:** That means it won't call any of them automatically. You'd just need to add them manually. So if you're in the editor and something is not there, you just use the add button and it gives you the other available artifacts.

**Matthew Panzarino:** So that's a quick fix you can implement. Long-term, this is a client-specific thing.

**Matthew Panzarino:** This is the best-case scenario because other clients will likely have the same issue—artifacts that work on some pipelines and not others. So we should file a ticket about it.

**Matthew Panzarino:** It's tough because defining a universal rule is hard. The universal rule "if it's in the artifacts section, call it" is probably good. And this is an easy workaround.

**Matthew Panzarino:** So give that a try and see if that works.

**Tiandra Burns:** I have a hunch it will.

**Tiandra Burns:** Great.

**Tiandra Burns:** And I have another thing I was working on with Immubit, and it's concerning the external links for data points that we use.

**Tiandra Burns:** And I was wondering if there would be a way to, like, put all of the links that we would use as external links to data points into one place.

**Tiandra Burns:** And so whenever it goes through and fact checks, it not only fact checks that information, but also puts the external link.

**Tiandra Burns:** Because I'm using the same, for instance, I'm using the same data points in most of the articles.

**Tiandra Burns:** I'm using the same sources.

**Tiandra Burns:** instead of adding it at the inputs, adding all of those ones we would use, would there be a way to create, like, a central system for all of the URLs or places we want to use for data?

**Matthew Panzarino:** Maybe. So there's a project we're working on that's been implemented in a couple of instances. It applies knowledge bases to articles.

**Matthew Panzarino:** Aimbit needs this. We needed it for Biologica. It may work with URLs. The only caveat is that it's links, not content.

**Matthew Panzarino:** It's not like copy. But with Biologica, for instance, they need certain things injected into the pipeline.

**Matthew Panzarino:** So they have a document with ingredients.

**Matthew Panzarino:** And the ingredients need to be sort of, like, injected in the appropriate way.

**Matthew Panzarino:** It's not an artifact, so I can't show you. It's hard-coded. But basically, they have a list of ingredients they want injected into articles and mentioned for certain products.

**Matthew Panzarino:** We have a list of about 35 ingredients. There are 150 fields in the database because we need to track which product it's in,

**Matthew Panzarino:** the brand name, the dosage, all that stuff—so it can pull that information if we need it.

**Matthew Panzarino:** That's applied as a style adapter with logic that says, "If the product contains this ingredient, include it."

**Matthew Panzarino:** Make sure to include the brand name, and if there are applicable ingredients on the list not yet mentioned, include them too.

**Matthew Panzarino:** And then Pedro wrote a workflow that takes that knowledge base and applies it. Aimbit is in a similar scenario where they have very specific definitions, terms, and technical documentation they want their articles to reflect.

**Matthew Panzarino:** Their definitions are different from everybody else's. The Internet's definition of "secretless security" is different from Aimbit's.

**Matthew Panzarino:** Aimbit has a specific way they want to refer to things. If you let a deep researcher look at the Internet, it comes up with whatever the consensus is. And Aimbit is not happy with that.

**Matthew Panzarino:** So we're taking a knowledge base of theirs—glossary, technical documentation, etc.—and a workflow applies that as a style adapter.

**Matthew Panzarino:** It's custom writing guidelines that are explicitly about this database and knowledge. The only caveat is I don't know whether that'll work with a list of URLs.

**Matthew Panzarino:** It seems likely. I know I could do it in a Claude project in about three seconds. So if we do it in a Claude project, we can do it in a workflow. It's just a matter of effort.

**Matthew Panzarino:** Write a detailed ticket of exactly what you want to do. Include a file with all of the URLs and the pipeline link where you'd like it to happen.

**Matthew Panzarino:** Tag me and tag Pedro, and say this might be related to the knowledge base work we're doing. I can chime in and say I'm not sure if this will work with URLs, but it might.

**Matthew Panzarino:** The reason it's worth filing a ticket is that the work is close to what you want and we're already doing it. Also, I know there are people here who have lists of URLs they want included in articles or selected from. This could be a way to make that happen.

**Matthew Panzarino:** I've written linking logic that could be applicable here. I like links to be two to three words and contextually relevant. That logic doesn't always work in the internal links workflow, so we're improving it.

**Matthew Panzarino:** So long story short: file a ticket and let's see if this work is related.

**Matthew Panzarino:** We may hit a blocker where it's not designed for URLs. Then we'll figure out how to build it from scratch. But let's start and see where it goes.

**Tiandra Burns:** Okay.

**Tiandra Burns:** Thank you.

**Matthew Panzarino:** Anybody else have any questions or weird stuff? When I ask for questions, I mean: what are you doing more than two or three times a week manually that's annoying you?

**Tiandra Burns:** For me, that was the linking of the data points, using the same list of data points.

**Matthew Panzarino:** Yep, you got it.

**Matthew Panzarino:** Yeah, makes sense. Let me set the stage for you here.

**Matthew Panzarino:** Many of you are working with a generic standard article generation pipeline: create a draft, make an outline, generate an article, do internal linking and fact-checking, then metadata or publishing or image. That's like taking a bicycle out of the box without adjusting the seat, checking the pedals, or making sure the brakes work. You could do it, but it wouldn't be very comfortable.

**Matthew Panzarino:** So what you need to do now is get extremely articulate about what is and isn't working. The process toward efficient operation of your pipelines is defining exactly where things fall down or aren't working, then adding workflows or tweaking existing ones to make them more efficient on a continuous basis.

**Matthew Panzarino:** Your job is not to just press play at one end and then do manual work in Claude projects afterwards. But if you do that, whatever you're doing in Claude projects is replicable.

**Matthew Panzarino:** It's not magic. It's exactly what we're using on the back end. So if you have processes you define and repeat every week, that's a workflow.

**Matthew Panzarino:** That's a column that should exist in your pipeline. Find those opportunities, articulate what they are, define the logic, and make sure it's explicit what you're doing and how, what artifacts you're using (on-prem or off-prem), then write a ticket.

**Matthew Panzarino:** Then we build that workflow and put it in your pipeline. When you hit play, what you were doing manually or with external assistance is now automatic. You move on to the next thing until you can drop something at the pipeline's start and get something delivery-ready at the end in a few minutes.

**Matthew Panzarino:** Most of you are far from that, which isn't your fault—except for one: file a ticket. Don't just suffer or do something externally without mentioning it.

**Matthew Panzarino:** Do whatever it takes to get the client work done. I get it. But then mention it. Say something, articulate it, and file a ticket.

**Matthew Panzarino:** Because it's a product you're using and you can directly affect its efficiency. That's rare. Typically, you use a product, it's bad, and you deal with it.

**Matthew Panzarino:** In this case, you do not. We're working on fundamental improvements to how pipelines generate content. Daniel's working on improvements to article generation, assignment creation, and article drafting that should flow out soon and provide massive improvements in writing quality.

**Matthew Panzarino:** Less adherence to weird outlines, better writing, more efficient use of bullet points.

**Matthew Panzarino:** Those are well known and we've talked about them. What I'm asking for is specific stuff for your pipelines: what stands between you and a more automated, less manual process?

**Matthew Panzarino:** Keep an eye on those things. If you don't know if something fits, mention it. Ask in the learnings channel, ask a director, ask me. I'll tell you honestly: is it impossible, already being worked on, or something we can do.

**Matthew Panzarino:** We don't have infinite engineering resources, so I can't promise immediate fixes. But we won't get anywhere if we don't mention it. So bring these things up. Anyone got any questions?

**Matthew Panzarino:** All right. I'm going to call it. Have a good one.

**Saskia Wartnaby:** Thanks, Matthew.

**Mariana Montezzana:** Thank you. Bye.
