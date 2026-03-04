# Impromptu Google Meet Meeting

<metadata>
date: 2025-04-21
time: 13:38 UTC
duration: 26 minutes
organizer: kirkland@growthx.ai
participants: Kirkland Gee (GrowthX), Prateek Gupta (Good Call)
fathom_recording_id: 58212776
fathom_url: https://fathom.video/calls/281643635
share_url: https://fathom.video/share/LyU6UrzbXMCBfd_yP1-nXkit1g6eaUhX
source: fathom
enriched_on: 2026-03-04 20:15 UTC
</metadata>

---

## Summary

Kirkland Gee walked Prateek Gupta through setting up a publishing workflow from AirOps to Webflow CMS collections for Good Call's programmatic SEO content. The system maps AirOps grid columns (title, description, slug, HTML content, images) directly to Webflow fields, with staged content status before publication. Key takeaway: consolidating multiple Webflow collections into a single "programmatic SEO" collection with subfolder slugs in the URL structure (goodcall.com/p/[content-type]/[slug]) would simplify long-term management versus maintaining separate collections for each content type.

---

## Context

Good Call is using AirOps and Webflow to manage programmatic SEO content generation at scale. They currently have multiple separate Webflow collections for different content clusters (e.g., Appointment Scheduling Software, Answering Services, etc.), with content sourced from AirTable and article content written in Markdown in AirOps. This impromptu working session was a hands-on configuration call where Kirkland from GrowthX showed Prateek how to set up the publishing pipeline—converting Markdown to HTML, mapping fields between systems, handling image URLs, and testing the workflow with a live example.

---

## Relevance

- **To GrowthX Delivery:** AirOps-to-Webflow publishing is a foundational pattern for programmatic SEO projects. This workflow demonstrates field mapping, Markdown-to-HTML conversion, and image handling best practices. The recommendation to consolidate CMS collections rather than creating separate templates per content type is a scalability lesson applicable to other client setups.

- **To GrowthX Business Development:** Good Call is executing a sophisticated content strategy at scale (100+ articles planned across multiple content types). Account shows strong execution capability and potential for expansion into other content-driven channels. Health signal: hands-on collaboration with client suggests high engagement and partnership maturity.

- **To CheckThat:** Programmatic SEO content targeting services like appointment scheduling software, answering services, and other niche B2B categories is precisely the use case CheckThat helps with—optimizing for AI visibility across distinct topical clusters.

---

## Overview

- AirOps can directly publish content to Webflow CMS collections, mapping grid columns to Webflow fields
- Multiple Webflow collections exist for different content clusters, but consolidating into a single CMS collection with subfolder slugs could simplify management
- The process involves converting Markdown to HTML, mapping fields, and handling image URLs properly
- Updating existing content is possible, but creating new pages with existing slugs will result in errors

---

## Key Topics

### AirOps to Webflow Publishing Configuration

  - New column added in AirOps: "Export to CMS to Webflow"
  - Webflow authentication set up for Good Call account
  - Status set to "queued" for staging in Webflow before publishing
  - Fields mapped between AirOps grid columns and Webflow CMS fields
  - Demonstration using "Appointment Scheduling Software" collection

### Content Preparation and Field Mapping

  - Markdown content converted to HTML using "Convert Markdown to HTML" workflow
  - Image URLs need to be accessible; AirTable image URLs worked in this case
  - [Slug field manually entered, following the pattern "/appointment-scheduling-software/\[article-name\]"](https://fathom.video/share/LyU6UrzbXMCBfd_yP1-nXkit1g6eaUhX?tab=summary&timestamp=568.0)
  - Most fields (title, description, meta title, etc.) mapped directly from existing columns

### Multiple Collections and Management

  - Currently using separate Webflow collections for different content clusters
  - Suggestion to consolidate into a single "programmatic SEO" collection for easier management
  - [Proposed URL structure: goodcall.com/p/\[content-type\]/\[article-slug\]](https://fathom.video/share/LyU6UrzbXMCBfd_yP1-nXkit1g6eaUhX?tab=summary&timestamp=1092.0)
  - Separate tabs in AirOps for different page types, each with its own publish column

### Content Updates and Slug Handling

  - Updating existing content works by running the publish action on the same row
  - Attempting to create a new page with an existing slug results in an error
  - System prevents accidental overwriting of existing pages with different content

---

## Action Items

**Prateek Gupta (Good Call)**
- Set up mappings in AirOps for each Webflow collection (title, meta description, slug, content, images, etc.)
- Add image URLs from AirTable to AirOps for article cover images
- Test publishing articles from AirOps to different Webflow collections
- Create new columns in AirOps for each Webflow collection to publish to (e.g., appointment scheduling, answering service)

---

## Transcript
**Kirkland Gee:** Now it's recording. Okay, great. So let me walk through how this works simply and then kind of go through what we need to do to get it the rest of the way. I'm going to share my screen on this window here. Can you see my screen?

**Prateek Gupta:** Yep.

**Kirkland Gee:** For now, set this column up to the blog posts collection on Good Call's Webflow. Is that, or are you going to be publishing articles to different collections?

**Prateek Gupta:** It's going to be random collections.

**Kirkland Gee:** So I'll just add a new column and walk through the configuration. The new column is "Export to CMS to Webflow." We use this Webflow authentication which covers all of our different Webflow accounts. This one is particularly for Good Call. This shows all of the different Good Call collections that exist. Are any of these related to the posts in this grid?

**Prateek Gupta:** One would be appointment scheduling software. Let's use that one for now.

**Kirkland Gee:** We're going to set the status to "queued," so when it pushes to Webflow, it's not going to publish immediately. It's going to stage it and then someone could go into Webflow and publish it live. You could change that if you prefer it to just publish when you hit the button. Then what you have to do is map the fields in that collection to the columns in the grid. Item ID is going to be created automatically—that's coming back from Webflow when you make the post. Name is typically just going to be the title. Post content is going to be the HTML content column. For category, image, and meta description, we already have those. Open graph is going to be the same as the meta title. We'll call this "Appointment Scheduling Software to Publish." Now if I hit this button on this row, it would take all of the columns we mapped, publish to Webflow, and give us back the item ID. Since we're not publishing to the blog post collection, I'm just going to delete that column.

**Kirkland Gee:** Basically the only thing you'll have to do is a lot of the stuff is in AirTable. Those things will have to come back over to AirOps to be able to publish. For the columns we're missing—we need alt text for images and a category. We can add those as simple text columns. Image alt text maps to that field, category maps to category, featured image maps to cover image. I'm not sure if the banner image and featured image are different in Webflow.

**Prateek Gupta:** We'll have to test that out.

**Kirkland Gee:** Yeah, let's go look at the Webflow fields. So post banner image is actually the featured image. We'll go back to AirOps and map that to our cover image. I'm trying to understand what all of those fields are actually mapping to. For image alt text, we're just using the title of the article, which makes sense. So we actually don't need a separate image alt text column. Just use the meta title for that and remove this column. We don't need the category field.

**Kirkland Gee:** But let's say we wanted to publish insurance appointment scheduling software. The first thing you have to do is use the "Convert Markdown to HTML" workflow. It only takes a few seconds. All it does is take the article with links and instead of Markdown, make it HTML because you have to have that to send it over to Webflow. The slug is manual, so you just type it in or paste it. Following the pattern /appointment-scheduling-software/[article-name].

**Prateek Gupta:** So I can remove the publish date field?

**Kirkland Gee:** You can keep it if you want. You can just pick a date. We'll call it today. For the cover image, if we go to AirTable we can grab an image. The only thing about images is you have to put a URL. Webflow is going to upload their own version. They may just need a place to pull the image from. Let's try it and see if it works.

**Kirkland Gee:** OK, so once I've mapped the slug, the content, and all the other stuff like the title and description, I should be able to just click this button and it's going to publish that right over to Webflow. We can check in our settings for this collection. Let's look at the Appointment Scheduling Software collection. We see "Top 8 Insurance Appointment Scheduling Softwares." Everything except the post content came through. Let me show you where the content is. It shows here when you select the staged page. This is the one that just came in from AirOps. Okay, the content is there—it just hadn't loaded yet. And now it's queued, so it's not published, but staged in Webflow.

**Prateek Gupta:** Do you want it staging before publish, or direct publish?

**Kirkland Gee:** The project should publish directly.

**Prateek Gupta:** But quick question—if I'm working with 10 different collections, I have to make 10 different columns, right?

**Kirkland Gee:** That's correct. The best way to deal with that is to make different tabs in your article generation sheet. You can duplicate this sheet and make a separate tab for each page type you're generating. So one tab for appointment scheduling, another for answering service, and so on. Most of these collections are pretty much the same in terms of field mappings. The image did get pulled from AirTable, so now there's a Webflow version of that image. You just need to copy the image URL from AirTable and paste it directly into AirOps.

**Prateek Gupta:** Got it. Perfect.

**Kirkland Gee:** Yeah, for each page type you'll need to create a new column, set it to Webflow, pick the collection you're writing to, and set up the mappings. Most of these collections are pretty much the same in terms of basic mappings.

**Prateek Gupta:** Is there a reason they're set up as different collections?

**Kirkland Gee:** We're trying to do experiments with content for a specific cluster. We're making sure we have separate clusters for each type of content we create. But here's what I'm thinking—you could make your life a lot easier. You don't have to have different CMS collections. You could just have a single "Programmatic SEO" collection and then in the slug you can put subfolders even if they're not at the top level. So you could say /answering-service/ or /appointment-scheduling/ and use the same page template.

**Prateek Gupta:** That's totally up to us. If we want to create under one CMS with the same page layout, we can stack it under one CMS and only change the subfolders. What would be the URL structure?

**Kirkland Gee:** One way I've solved that in the past is doing something like goodcall.com/p/[content-type]/[slug]. So you put all of those pages in one subfolder for reporting and then break them out by page type. It can make things a little easier. But if you're going to have 100 different clusters, it's probably worth doing one CMS in Webflow instead of having 100 because that's just going to get really hard to manage. Even if these collections are completely identical in template and you're only changing the slug, if you get into 20 different collections, you'll have 20 different places tracking these and 20 different ways managing them in Webflow. Eventually that's going to be a headache.

**Prateek Gupta:** So if there's an existing URL slug and the writer publishes an exact identical URL, what happens?

**Kirkland Gee:** If you have two rows with the same slug, it's probably going to give you an error saying "already exists." But if you run the publish action on the same row that already published it, it's going to try to update the existing one. It will actually update the page that's already there as long as that is the page that was published from that row. So if you try to create a new page with a slug that already exists, it's not going to let you. It's going to give you an error. Once you've created it with the proper slug generated from Webflow, if you come back and hit run again, it's going to update that existing post with the new content.

**Prateek Gupta:** So if the slug already exists in the system, it'll give me an error.

**Kirkland Gee:** Correct. But once you've published from that specific row, updating it will work.

**Prateek Gupta:** Okay, perfect. Does this all make sense?

**Kirkland Gee:** Any other questions?

**Prateek Gupta:** I did have one, but I can't quite recollect it right now.

**Kirkland Gee:** No problem. The next steps would be to go through and set up the mappings for each of your content categories.

**Kirkland Gee:** Yeah, so basically the only like thing you'll have to do is I know a lot of the stuff is in era are in air table Like a lot of the final details get added there Those things will have to come back over to air ops to be able to publish from here Um But if we look at our columns that we're missing like we need An alt text for image in a category All we really need to do Is just add some text columns So this can be our you know image alt text We'll add a category And then we can go over here and say okay for image alt text we want to map that to that field Categories going to map category Uh Featured image is going to go to cover image And then i'm not sure like this is actually probably just going to be the same one The same for twitter image I don't know if the banner image and the featured image are different in webflow really

**Prateek Gupta:** Up to back, we'll have to test that out.

**Prateek Gupta:** What does a feature image is and what is a manual image?

**Kirkland Gee:** Yeah, let's go just to go look.

**Kirkland Gee:** I don't want to back up.

**Kirkland Gee:** The real one.

**Kirkland Gee:** So we'll look at in.

**Kirkland Gee:** Oh, gosh.

**Kirkland Gee:** They changed the layout of this where you have to like go through this to get to collections these collections in the sidebar and I'm like, why did they do that?

**Kirkland Gee:** Okay, so we want to look at the fields here.

**Kirkland Gee:** So post string isn't filled out here featured image post banner image is actually the.

**Kirkland Gee:** Yeah.

**Kirkland Gee:** We didn't change anything.

**Kirkland Gee:** So this is the post banner.

**Kirkland Gee:** image.

**Kirkland Gee:** So we'll go back to AirOps and we'll map that to our cover image.

**Kirkland Gee:** And essentially, what I'm trying to do is just understand, okay, what are all of those fields actually mapping to?

**Kirkland Gee:** Got content.

**Kirkland Gee:** So this one alt text for image.

**Kirkland Gee:** Yeah, we're just using the title of the article, which makes sense.

**Kirkland Gee:** That's fine.

**Kirkland Gee:** So we actually don't even need a separate image alt text.

**Kirkland Gee:** Just use our meta title for that and remove this column.

**Kirkland Gee:** Is this making sense?

**Kirkland Gee:** Like how?

**Kirkland Gee:** yeah, yeah.

**Kirkland Gee:** And actually, we're not even using these fields.

**Kirkland Gee:** So actually, I don't

**Kirkland Gee:** I don't think that we can just go back to air ops.

**Kirkland Gee:** We don't need this category.

**Kirkland Gee:** Let's see, yeah, the answering servers for small business.

**Kirkland Gee:** This is gonna be an imagine some point in scheduling software.

**Kirkland Gee:** Sorry, I'm like my brain is moving too fast and I'm like not speaking.

**Kirkland Gee:** But let's say that we wanted to publish, is there any insurance appointment scheduling software?

**Kirkland Gee:** have this row here.

**Kirkland Gee:** The first thing you just have to do is use this convert markdown to HTML workflow.

**Kirkland Gee:** only takes a few seconds.

**Kirkland Gee:** All it's gonna do is take the article with links and instead of being marked down, this is gonna make it HTML because you have to have that to be able to send it over to webflow.

**Kirkland Gee:** And then publish date.

**Kirkland Gee:** I don't even think that's a part of this.

**Kirkland Gee:** Mapping.

**Kirkland Gee:** Yeah, we don't even have that.

**Prateek Gupta:** So I can remove it.

**Prateek Gupta:** you can keep it if you want to, like back.

**Prateek Gupta:** Yeah.

**Prateek Gupta:** Yes, let's keep it.

**Prateek Gupta:** They just other things for me.

**Prateek Gupta:** Yeah, so you can just pick a date.

**Kirkland Gee:** We'll just call it, you know, this is going to be today.

**Kirkland Gee:** The slug right now is just manual.

**Kirkland Gee:** So you just type it in or paste it.

**Kirkland Gee:** You could probably.

**Kirkland Gee:** I don't know how the slugs on this slash appointment scheduling software slash again.

**Kirkland Gee:** So this would adjust the insurance.

**Kirkland Gee:** Yep.

**Kirkland Gee:** Cover image.

**Kirkland Gee:** I don't have one right now, but if we go to air table.

**Kirkland Gee:** Give this a second to load.

**Kirkland Gee:** So we'll grab this image.

**Kirkland Gee:** Now, the only awkward thing about the images is you just have to put a URL and when it goes into air table, like you're not going to give it the air table URL of the cover image, you'll want whatever the, like, well, listen, I mean, make this, actually, let's try it and just see if it'll work.

**Kirkland Gee:** Because I imagine Webflow is going to upload their own version.

**Kirkland Gee:** They may just need a place to pull the image from, but I don't know if that's accessible.

**Kirkland Gee:** pull to them, we'll have a little up here.

**Kirkland Gee:** OK, so once I've mapped the slug, the content, and all the other stuff that's already here, like the title, the description, and all of that, I should be able to just click this button.

**Kirkland Gee:** And that's going to go ahead and publish that right over to Webflow.

**Kirkland Gee:** We'll come over here.

**Kirkland Gee:** And we can check in our settings for this collection.

**Kirkland Gee:** I want to get to, yeah.

**Kirkland Gee:** Let's look at the appointment scheduling software.

**Kirkland Gee:** We see top eight insurance appointment scheduling softwares.

**Kirkland Gee:** It looks like that's still sort of loading in, but OK, everything except the post content.

**Kirkland Gee:** I this cartridge is exactly what

**Kirkland Gee:** Okay.

**Kirkland Gee:** So the content didn't come through.

**Kirkland Gee:** Let's figure out why.

**Kirkland Gee:** What's content?

**Kirkland Gee:** me show you content to see.

**Kirkland Gee:** All right, so it'll actually show here like when you go to select one stage changes.

**Kirkland Gee:** So these are the one this is one that just came in from Air Ops.

**Kirkland Gee:** Okay, great.

**Kirkland Gee:** that is there.

**Kirkland Gee:** Just hadn't loaded yet.

**Kirkland Gee:** And now that's queued, so it's not published, but staged in Webflow.

**Kirkland Gee:** If you wanted to, you could just come back over here and edit this.

**Kirkland Gee:** Oh, you'd have to redo the connect.

**Kirkland Gee:** I guess you'd have to make a column actually to be able to change the...

**Prateek Gupta:** Do you want it be where it's just staging them to publish, or do you want it to?

**Kirkland Gee:** The project is direct published.

**Prateek Gupta:** But quick question here, we'll have to always create.

**Prateek Gupta:** So if I'm working with 10 different collections, I have to make 10 different columns.

**Prateek Gupta:** That's correct.

**Kirkland Gee:** So what's probably going to be the best way to deal with that is to make different tabs in your article generation sheet.

**Kirkland Gee:** So you can just duplicate this sheet over and make a separate tab for each page type of article that you're going to be generating.

**Kirkland Gee:** So like

**Kirkland Gee:** You know this one's got it got it got it appointment scheduling right and then that's what this publish works with And then we can make another one that's you know answering service right whatever that might be But I would say I mean if they're pretty much the same And this and it did access a table so Image right it did get the image from the table if I'm not done.

**Prateek Gupta:** Yep.

**Kirkland Gee:** Yeah, it just pulled that in and so now there is a You know web flow version of that image so you can just from air table Uh, you know, you just need to copy the URL of that image Got it So not sorry to open the image and then copy the image address But then you can paste this directly into air ops Got it perfect Perfect

**Prateek Gupta:** I guess that's all just my problem.

**Kirkland Gee:** Yeah, so basically what you'll need to do for each page type, and I can help with this if you need it, but what you'll have to do is just create a new column, Webflow, continue, and then pick the collection that you're going to be writing to, like, you know, mapping, this is the title, this is the, and actually it looks like most of these collections are pretty much the same, right, in terms of it's going to be the same basic mappings.

**Prateek Gupta:** Is there a reason they set them up as different collections?

**Prateek Gupta:** Yeah, we are trying to do experiments with content of a specific cluster.

**Prateek Gupta:** So, in this category, this specific category, content in this, also,

**Kirkland Gee:** thing about something else is on a different cluster and then doing all the internal linking and all that in terms of having like 500 800 articles in one single cluster it's more about just making sure that we have some bits of it clusters for each type of content that we create yeah you the only thing i'm thinking about is you like yeah i mean this is like you know the client could do it however they want to but what you could do to make your life a lot easier and you don't have to have different cms collections like you could just have a let's call it a programmatic seo collection and then in the slug like you can put sub folders in the slug even if they're not in like the top level of the collection so you could say slash you know answering service

**Kirkland Gee:** slash whatever, and use the same page template, and then change your slug to appointment scheduling.

**Kirkland Gee:** If all of these collections are going to be pretty much exactly the same.

**Prateek Gupta:** That's totally up to If you want to create under one CMS, you're seeing the page layout is the same and everything, then we can stack it under one CMS.

**Prateek Gupta:** And only the subfolders would change.

**Prateek Gupta:** In this solution, would all the subfolders, what would be the URL structure?

**Prateek Gupta:** Would there be added subfolders before?

**Kirkland Gee:** I guess that would be the one, you'd have to put something there.

**Kirkland Gee:** You could do the way that I've solved that in the past is doing something like goodcall.com slash p slash, and then everything else.

**Prateek Gupta:** I've seen that a lot, yes.

**Kirkland Gee:** So that way, you put all of those pages in one subfolder for reporting, and then you have them broken out again by page type, it can make things a little easier, but it's not a big deal.

**Kirkland Gee:** can do whatever you want, but if you're going to have 100 different clusters, for example, it's probably worth doing one CMS in Webflow instead of having 100 of them, because that's just going to get really hard to manage.

**Kirkland Gee:** Once you get past, even...

**Kirkland Gee:** this is a lot of different templates for them all to you know if you're looking at like this one is completely identical to you know appointment dancing service salon and couple of other temperatures exactly the same right so it's like the only thing you're doing is changing the slug yeah if you're only doing three or four not a big deal if you're getting into 20 you know you're going to have 20 different places you're tracking these and 20 different ways you're keeping them up with them in web flow eventually that's likely going to get to be a bit of a headache but for the time being you know type of other things nice addition that so in the long run it's definitely gonna help us also just so if there's a URL slug for example and existing URL slug and we post like the writer is not aware of it and just once

**Prateek Gupta:** So, quick question there, if there is an existing URL structure that there is an existing page and if the writer or me or anyone we publish an exact identical URL then what happens in that case?

**Kirkland Gee:** So, if you tried to say, let's say we have two rows with the same slug, I think it's probably going to give you an error and say, hey, already exists, if let's say we change, you know, just for the sake of it, let's just say the roles and benefits, just

**Kirkland Gee:** for the, for the sake of like showing this and you click run on the same row.

**Kirkland Gee:** It's just update, it's going to try to update the existing one.

**Kirkland Gee:** But yeah, so slug unique how you already exist in the database.

**Kirkland Gee:** So it's going to kick that back to you.

**Kirkland Gee:** thought it would just update, but I guess that's not true.

**Prateek Gupta:** But we are updating the content, like you're not updating the slug.

**Prateek Gupta:** So shouldn't it get published?

**Kirkland Gee:** slug description already in database.

**Kirkland Gee:** Yeah, I thought it would just update the one that's there, but it doesn't look like that's case.

**Kirkland Gee:** It just gives you an error.

**Kirkland Gee:** But I think that might be, ah, that's because the insurance one is already there separately, like that had already been manually published.

**Kirkland Gee:** So the one that, so hold on.

**Kirkland Gee:** This created this variant of the slug because that page already existed.

**Kirkland Gee:** If we try to do it with this, and we change this to just, I'll undo that in a second.

**Kirkland Gee:** Yeah, so it will actually update the page that's already there, as long as that is the page that was published from that row.

**Kirkland Gee:** So if you try to create a new page with a slug that already exists, it's not going to let you do that.

**Kirkland Gee:** It's going to say, hey, error that already exists.

**Kirkland Gee:** Once you've created it.

**Kirkland Gee:** If now that this is created with the proper slug that it generated from Webflow, and I come over here and say the roles and benefits and hit run again, it's going to update that existing post with this new content here.

**Kirkland Gee:** Got it.

**Kirkland Gee:** And so, if I do any content changes, it's going to update the content.

**Prateek Gupta:** But if the slug already exists in the system, then it's going to give me an error.

**Prateek Gupta:** Correct.

**Prateek Gupta:** Okay.

**Prateek Gupta:** Okay, perfect.

**Prateek Gupta:** Awesome.

**Prateek Gupta:** Does this all make sense?

**Kirkland Gee:** Any other questions?

**Kirkland Gee:** I did.

**Prateek Gupta:** I did.

**Prateek Gupta:** have one.

**Prateek Gupta:** Maybe I'll just like you or something.

**Prateek Gupta:** I'm not able to recollect it.

**Prateek Gupta:** Yeah.

**Kirkland Gee:** So, I would say who can kind of the next steps would be like, you can go through, at least you just have a couple of categories for now.

**Kirkland Gee:** yes.

**Kirkland Gee:** And just great.

**Prateek Gupta:** Yes.

**Prateek Gupta:** Sorry.
