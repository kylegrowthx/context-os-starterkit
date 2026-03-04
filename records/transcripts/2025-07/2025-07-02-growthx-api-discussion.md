# GrowthX API discussion

<metadata>
date: 2025-07-02
time: 17:00 UTC
duration: 56 minutes
organizer: Jason Gong (GrowthX)
participants: Jason Gong (GrowthX), Jennifer Hampton (Abnormal), Abdallah AlHakim (Abnormal), CJ Cunniff (Abnormal)
fathom_recording_id: 71872093
fathom_url: https://fathom.video/calls/340916044
share_url: https://fathom.video/share/-Wc63gkYJzgDUS1Rgcscs97gc5a4S8o2
source: fathom
enriched_on: 2026-03-03 14:32 UTC
</metadata>

---

## Summary

GrowthX and Abnormal aligned on a strategy to add API integration for automated content publishing to Abnormal's Craft CMS. Rather than trying to build complex API support for Abnormal's existing modular content builder, Jennifer proposed adding a simple rich text field that would take priority over the modular builder, allowing GrowthX to post content programmatically while maintaining the flexibility for manual posts that need advanced formatting. Jennifer will deliver a GraphQL schema for blogs, glossaries, and AI glossaries by end of next week, and GrowthX's engineering team will assess feasibility of implementing mutations alongside read queries.

---

## Context

GrowthX is a content marketing services firm creating high-volume content for clients. Jason Gong leads GrowthX's content generation operations, which use a mix of LLMs and people. The team has been manually copy-pasting generated markdown content into clients' CMS systems, which creates friction and limits velocity. Abnormal Security (the client on this call) operates a Craft CMS headless backend for their blogs, glossaries, and other content properties. The modular content builder in Abnormal's CMS is powerful but complex—it supports "bells and whistles" for advanced posts (Evan's blogs being the canonical example), but that complexity makes it difficult to wire up API integration. GrowthX has successfully done API integrations with other platforms like Webflow, so they understand the patterns. This call was focused on finding a pragmatic way to let GrowthX automate content pushes without requiring API support for every field in the modular builder.

---

## Relevance

**To GrowthX Delivery:**
- Enables automation of content publishing for Abnormal, reducing manual copy-paste steps and improving velocity
- Establishes pattern for API-first content delivery across clients (Webflow experience shows GrowthX can handle CMS API integrations)
- Rich text field approach is pragmatic: supports 80% of use cases without requiring API support for modular builder complexity

**To GrowthX Business Development:**
- GraphQL API schema delivery by end of Q3 week 1 unblocks engineering assessment and implementation timeline
- Account health signal: Abnormal is prioritizing this as a Q3 OKR, indicating committed investment in the partnership
- Potential for expansion: Jennifer mentioned other related capabilities that API integration would unlock, signaling opportunity for follow-on work

**To CheckThat:**
- Craft CMS uses GraphQL for content structure queries, which is relevant to CheckThat's AEO analysis and prompt optimization for CMS queries

---

## Overview

- Decided to add a simple rich text field for API-driven content posting instead of trying to build complex API support for the modular builder
- Rich text field will take priority over modular builder if content exists, allowing API automation while keeping manual advanced formatting as an option
- Jennifer will create GraphQL schema for blogs, glossary, and AI glossary entries by end of next week; GrowthX team will review documentation and assess implementation feasibility
- GrowthX to handle image upload workflow as separate API call step: determine placement, upload to CMS, grab URL, insert into rich text before final post submission
- API permissions will be limited to draft status only; GrowthX will never publish directly
- Short-term: v1 basic API integration for rich text content; long-term: explore building out modular builder API support or using custom shortcodes for advanced components like accordions

---

## Key Topics

### Current CMS Setup and Challenges

  - Craft CMS with modular builder component
  - Modular builder clunky but necessary for some posts (e.g., Evan's blogs with "bells and whistles")
  - API integration challenging due to numerous fields in modular builder

### Proposed Solution

  - Add simple rich text field, possibly as sub-tab or "alternate content field"
  - If content exists in new field, prioritize it over modular builder content
  - Allows for easier API integration while maintaining existing capabilities

### Image Handling in Posts

  - Images need separate upload before inclusion in content
  - GrowthX can handle image insertion as a separate step in their pipeline:
    1.  Determine image placement
    2.  Upload image to CMS via API
    3.  Retrieve URL
    4.  Insert image tag in content before final CMS submission

### FAQ/Accordion Component

  - Currently used in glossary and some blog posts
  - Typically placed at end of content
  - Options for integration:
    1.  Custom shortcode in rich text field
    2.  Manual insertion using existing modular builder
    3.  Potential future API adaptation for full modular builder capabilities

### GraphQL API Integration

  - Jennifer to create GraphQL schema for blogs, glossary, and AI glossary
  - Will provide credentials for GrowthX to query and potentially create/edit entries
  - Allows for both reading existing content structure and pushing new content
  - GrowthX team to review GraphQL documentation and assess feasibility

### Content Publishing Safeguards

  - GrowthX to only save as drafts, not publish directly
  - Jennifer to ensure API permissions limit to draft status only

---

## Action Items

**Jennifer Hampton (Abnormal)**
- Create GraphQL schema for blogs, glossary, and AI glossary by end of next week. Set up credentials and send to Jason for testing.
- Send GraphQL documentation link to Jason's engineering team for review.
- Set up access to staging CMS environment for GrowthX team to test GraphQL queries and mutations.

**Jason Gong (GrowthX)**
- Have engineering team review GraphQL documentation and assess feasibility of implementing mutations to create and update entries (in addition to read queries).

---

## Transcript

**Jason Gong:** Jennifer, how's it going?

**Jennifer Hampton:** Good. It's nice to get to connect with you face to face.

**Jason Gong:** Yeah, for sure. We're really seeing each other on Slack a bunch. You're located East Coast, West Coast?

**Jennifer Hampton:** Yeah, I'm in New York, well, just outside of New York. This whole room is a lot of space for New York City.

**Jason Gong:** I lived in San Francisco, I live in Oakland, but the rents here are crazy. I look at YouTube and all those "tour my apartment in New York" videos.

**Jennifer Hampton:** It's like another level. My closet with a bathroom and a microwave.

**Jason Gong:** Yeah, I was paying like six, seven grand for a one bedroom. I know those are like the nicest buildings, but still.

**Jennifer Hampton:** It takes a type of person to really want to live in the city and be willing to pay the premium.

**Jason Gong:** Raising a family there, that's part of it. I think living there when you're young and working a bunch is one thing, but I don't know.

**Jason Gong:** Yeah, but I'm super excited. We have personally felt the pains of uploading content to CMS now for a few weeks. I feel like we can help multiple people on the Abnormal team if we can get this working.

**Jennifer Hampton:** Yeah, and I don't know if Abdallah is joining us.

**Jason Gong:** I think he's running sales masters, so he may be running a little later. Yeah, I think he's getting pulled into something from the looks of it.

**Jennifer Hampton:** Gotcha. So we can get started though, and just kind of catch him up, because it's mostly for us to connect anyway.

**Jennifer Hampton:** So one of the considerations we have to balance is that the CMS fields—I know the modular builder is a little bit clunky today, but it was built at a time when that was required.

**Jason Gong:** I inherited it. It predates me, so it's a little bit of reverse engineering the logic behind it.

**Jennifer Hampton:** Right. Before we had other options for building, the modular builder was a globally used component throughout the website. It made sense and it still makes sense for the content team because they're trained on it—it offers the same flexibility the other areas of the website offer. But sometimes we do get posts that require it, so we can't just fully replace it. For example, when Evan wants to post a blog, he tends to want to add a bunch of bells and whistles. Having those capabilities is helpful, but it makes it very hard to set up an API because there are just so many little fields.

**Jason Gong:** Is there a way to just add a module?

**Jennifer Hampton:** My plan is rather than trying to phase out the modular builder and go through a cost-benefit analysis—what happens to historical post content, what happens with the capabilities we need in the future—my intention is to add a simple rich text field. Even if we tuck it into a sub-tab as an alternate content field, if something is in that field, we put that content first.

**Jennifer Hampton:** So you can still add into the modular builder if you want to. If people prefer to post that way, they can. But the rich text field needs to be capable of all the different capabilities we need. You could route an API call to post the content directly into that field.

**Jason Gong:** That would be amazing.

**Jennifer Hampton:** Out of the box with Craft, there isn't an API, but we have a plugin that allows us to set up an API feed, and we have a GraphQL API layered into it. So we can do whatever calls we need to post content. It just requires more manual configuration than something like WordPress, where it comes more out of the box.

**Jennifer Hampton:** So what I'd love to see—and I think the reason why Abdallah set this call was—I'd love to see what your current setup is, where all this content is being collected, and what capabilities you can show me that you have to do an API connection, an outward call to the website.

**Jennifer Hampton:** So that we can tailor the solution coming from both sides to find the sweet spot.

**Jason Gong:** If you asked me two months ago it would have been more restricted, but essentially on my side, we're just writing the code, so we can adapt to anything. Since we're open-ended on how we can construct it right now, we have the opportunity to build it in a way that makes the most sense from what we generate and what you can intake.

**Jennifer Hampton:** Yeah, because we can find the happy medium in between. Is this a Sanity CMS backend?

**Jason Gong:** No, this is kind of our own tool. I don't know if I've given you context for what we do, but we create a lot of content with a mix of LLMs and people, and this is the tool we built ourselves to do that.

**Jason Gong:** If it was comparable to anything, it'd be like AirOps.

**Jennifer Hampton:** Yeah, I'm familiar. I think someone showed me AirOps before.

**Jason Gong:** Yeah, so this is kind of like our AirOps, but it works a lot better for our use case of having a lot of clients and a lot of content. Basically, the output of all of these is markdown at the moment, but then we take that and depending on the client, we shape it. Right now it all ends up going into a Word doc and then we manually copy and paste it into the CMS.

**Jennifer Hampton:** I forget if our system would take Markdown. It looks like, no, it doesn't happily take Markdown, but you could convert the Markdown into HTML.

**Jason Gong:** Yeah, I mean, we could just convert this whole thing.

**Jennifer Hampton:** Okay, and you use images in the content. The content you'd be able to just drop in is fairly straightforward, but when you want to include an image, it needs to be uploaded. So whether we can have a secondary API call that uploads the image, grabs the URL, and then you can incorporate that. Or if it would be simpler to automate everything except the image uploads and you manually throw the images in. I'm thinking about how a dependent API call would work, where you want to include the image in the rich text area, but first it needs to exist somewhere we can attach it.

**Jason Gong:** Yeah, that makes sense.

**Jennifer Hampton:** Have you done that in the past with other clients? What's the approach?

**Jason Gong:** We adapt to whatever CMS. With Webflow, I've done this. They have a rich text field, and you have to give it certain HTML flavors with certain tags. For images, we just have an image tag in the HTML with a URL. It's opinionated about what URL is okay. We usually store it in S3, grab that URL, and use that. You could use an image tag with a URL, but it would have to link to an external asset.

**Jennifer Hampton:** Can we have it upload into an internal bucket in the CMS, grab that information, and replace the area with the correct URL?

**Jason Gong:** Right, we can totally do that. If there's an API where we can give it an image and it returns the URL, we can create the image tag with that URL.

**Jennifer Hampton:** So you'd do that manipulation on your side? Unless you had a separate field for the image to trigger the API call, or if you could code something to say, when there's an image, run this separate API call, pause, fetch that information, and insert it.

**Jason Gong:** I mean, we could totally do that. We do a lot of things in steps. For example, with our other clients like Webflow, when we're writing content, image insertion is a step. We read the article and figure out where an image makes sense, then iterate through and insert it.

**Jennifer Hampton:** So you'd have a step to figure out where you want images, and if it decides you want one there, it calls to upload it to the CMS and gets the URL?

**Jason Gong:** I would do that before we even upload to the CMS. Going section by section, I'd identify where images make sense, create the image, upload it to your CMS, grab that link, and create the image tag.

**Jennifer Hampton:** So before you push the post to the CMS, you'd know you want an image, know what it should be, send the API call to upload it, get the physical URL, include it in the post, finalize it, and then ship to the CMS in a later step.

**Jason Gong:** Right, exactly. And then the last step would be uploading the glossary page or whatever.

**Jennifer Hampton:** Cool, okay, that could work.

**Jennifer Hampton:** So you're not posting resources right now, right?

**Jason Gong:** Nope, just glossary, AI glossary, and blog.

**Jennifer Hampton:** Okay, the resources have more fields outside the modular builder, but blogs don't have too many required fields. Besides the open-ended content field, we'd have SEO fields—those are always present, not conditional—a toggle for whether to show the summary in the header, the hero image, and a mobile version if you want one, and the blog category.

**Jason Gong:** The FAQ would also be nice, but not required.

**Jennifer Hampton:** The FAQ—do you put that in your content?

**Jason Gong:** There's an accordion component. We've been using it for the glossary, and I'm not sure if we've been doing it for blogs.

**Jennifer Hampton:** Do you always add it at the end, or would you want to put it within the content body?

**Jason Gong:** I think basically always at the end.

**Jennifer Hampton:** I'm wondering, on the list of many things I'd love to do if we had unlimited time and resources, I want to clean up these content sections. There are settings that are no longer applicable, but they're required because we haven't turned them off. I have to see how the modular content builder structures data. I think it might generate IDs for each element, in which case you couldn't just push them with an API call—you'd need to know the IDs.

**Jason Gong:** I see.

**Jennifer Hampton:** But if the order determines the ID, like the first element is ID zero, you could build it procedurally. I'm thinking: could we use a custom shortcode as a place trigger, where you put the information in shortcode format and we expand it to the component on rendering? Or we could use this rich text field as a short-term solution for V1, and then in V2, see if we can adapt the API to use the modular builder for full capabilities. The third option is we leave it as the rich text field and don't worry about the accordion. But since I'm not removing the content sections area, if there are posts where you want to manually insert FAQ, we could set it up so the rich text goes first, and the modular builder goes below. You could add only the modular builder for the accordion manually where you wanted it. You'd be able to do everything except that one piece.

**Jason Gong:** I think whatever would get the rich text field first is what I'd do.

**Jennifer Hampton:** No matter what, that needs to happen first. Is that the end of our work there, or can we go back to using the modular builder with API calls in V2? Or use shortcodes inside the rich text editor? There are a couple different ways we could play with it.

**Jason Gong:** Right.

**Jennifer Hampton:** The priority is getting the initial API set up so you can start pushing content programmatically.

**Jason Gong:** That makes sense. And will that be for posting new articles? Can we also do updates of existing articles?

**Jennifer Hampton:** I would presume we could do both—post new and update existing. You'd need read and write options to read the original content and then repost new stuff. I don't see why not. But I will say this is going to be one of our Q3 OKRs. I'm still trying to understand all the requests coming in to see where I can prioritize it. To me, it seems important from a velocity standpoint, but I have to weigh that against new capabilities and launches with specific timings. I don't know exactly where it'll fall in the next quarter, but I'm prioritizing it. I think this is important functionality not just for your use case, but it would unlock some related capabilities.

**Jason Gong:** Yeah, for sure. I think we're on the same page about our wish list.

**Jennifer Hampton:** We'll work regardless, but yeah, that would be really nice. I'm just going to look at one more thing before we wrap. We have just a minute or two. Let me check if I can make a new schema. Are you familiar with GraphQL as a data structure?

**Jason Gong:** Not really.

**Jennifer Hampton:** It's like SQL. You query the database for information, and you can also update with it. You can do mutations, so we can toggle those on to allow you to create. What I can do in the short term before putting work in is set up a schema that would allow you to query the blogs, glossary, and AI glossary. You can see the structure of current posts and work at the GraphQL syntax to build a mutation. You can create entries. I'm going to share my screen. We can create a GraphQL schema where you can query and view entries, or edit and create them. This may be enough for what we need. We'd still have to add fields, adjust the layout, and share it. Before I go that far, I can do the schema by end of next week. I can create it and get you credentials to make calls and see what the data looks like. Each content section has a unique ID, so I'm not sure about posting into them, but the rich text field we can definitely do. You could query to see how those are structured and push back in a similar way. Here's the GraphQL documentation. Let me know if this would work for your team.

**Jason Gong:** I'll show our engineer. I won't be writing this myself.

**Jennifer Hampton:** I'll loop in our developer. It's very similar to SQL, but structured like a JSON query with key-value props. You can pull information directly from the database and push it back. So we could create posts that way.

**Jason Gong:** Yeah, that sounds amazing. I've never heard of Craft CMS before, but it looks quite flexible.

**Jennifer Hampton:** On my end it felt painful, but you have limited permissions, and the staging environment has different settings than production. It's a headless CMS with PHP and JSON files. I think we'll get to a solution, and if we can do this, it would help escalate it. We just need to add the field and where it renders, then you can tweak and use it.

**Jason Gong:** And we would never publish directly. I don't think you should give us the ability to publish—just save as draft.

**Jennifer Hampton:** We can have it so you create them but only save as draft. One of the fields is status, and you just need to make sure you're not pushing to published status.

**Jason Gong:** That makes sense.

**Jennifer Hampton:** So have your team look at the documentation, and I'll set up the schema and get you credentials to fetch and test. We can give you staging environment access if you want. It's a separate CMS for testing—it never pushes to production.

**Jason Gong:** Sounds good.

**Jennifer Hampton:** Thanks, Jason. Mind sending me the note-taker information? I couldn't get Companion to record it.

**Jason Gong:** Yep, sounds good. Thanks very much. Talk to you soon. Bye.
