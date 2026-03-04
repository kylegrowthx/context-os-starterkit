# CRV - CMS Walkthrough

<metadata>
date: 2026-01-09
time: 18:00 UTC
duration: 23 minutes
organizer: william@growthx.ai
participants: Tony D'Amico, Tanya, Hassan, William Leborgne
fathom_recording_id: 113154165
fathom_url: https://fathom.video/calls/526830030
share_url: https://fathom.video/share/zQtsbJvqCmg6qLjaaFhq1NVN8wXwcFZ9
source: fathom
enriched_on: 2026-02-28T21:30:00Z
</metadata>

---

## Summary

Tony D'Amico (frontend developer/designer) walked through the new Webflow CMS interface for CRV's content platform, covering field structure, SEO capabilities, and content creation workflow. The team clarified implementation details for meta tags, schema markup, author bios, and table support—establishing next steps for both development and content strategy.

---

## Context

CRV is preparing a content publication platform built on Webflow. This meeting served as the operational handoff between the development team (Tony) and the editorial/strategy team (William, Tanya) to ensure everyone understood the CMS structure and could begin creating content. William Leborgne works at GrowthX as a strategic lead; Tony D'Amico is an external developer/designer; Tanya works at Underbelly (likely the agency running this engagement); Hassan from GrowthX was invited but unable to attend. The CMS includes fields for published content, author information, and SEO metadata—all essential for a content-first publication strategy.

---

## Relevance

- **Content Operations:** Establishes the technical foundation for content creation workflow, directly enabling publication strategy execution.
- **SEO Requirements:** Clarifies how to implement SEO fields (Meta Title, Meta Description, Schema Markup) needed for search visibility.
- **Content Governance:** Defines author bio requirements and workflow to establish expertise signals for content credibility.
- **Content Discovery:** Addresses sitemap footer implementation to reduce click depth and improve findability of new content.
- **Client Readiness:** Tony will delete placeholder content, build author CMS, and set up footer; Tanya will request bios from Krista (likely the editorial lead); William will follow up on schema markup implementation.

---

## Overview

- **CMS Fields Added:** New fields for `Meta Title`, `Meta Description`, and `Schema Markup` were added to enable SEO customization for each post.
- **Author Bios Required:** A new author bio section will be built, requiring 60–80 word bios from Krista to establish author expertise.
- **Content Navigation:** A new footer with a sitemap will be added to ensure content is discoverable and to maintain a low click depth.
- **Table Support:** Webflow lacks native table support; content creators must use custom code blocks for tables.

---

## Key Topics

### CMS Functionality & SEO

  - The CMS is in Webflow under `Contents` → `Content`.
  - **Table of Contents (TOC):** Auto-generates from H2 and H3 tags in the body text.
  - **SEO Fields:**
      - `Meta Title` & `Meta Description`: Added as distinct fields for custom SEO titles and descriptions.
      - `Schema Markup`: Added as a text field. The technical implementation for Google to recognize this markup is TBD.

### Author Bios

  - **Requirement:** A bio and image are needed at the bottom of each post to establish author expertise.
  - **Implementation:**
      - A new `Teams` CMS collection will store author data (bio, avatar).
      - The author field in the `Content` CMS will become a dropdown linking to this collection.
  - **Action:** Tanya will request 60–80 word bios from Krista.

### Content Navigation

  - **Problem:** The site lacks a sitemap footer, making new content hard to find.
  - **Solution:** Add a new footer column with a sitemap.
  - **Action:** William will ask Krista for approval.
  - **Related Action:** Remind Krista to provide the missing Privacy Policy page for the new footer.

### Tables in Content

  - **Limitation:** Webflow's rich text editor does not support native tables.
  - **Workaround:** Use a custom code block to embed tables.
  - **Decision:** Proceed with this workaround for now and revisit if a custom solution is needed later.

---

## Action Items

**Tony D'Amico (Freelance Frontend Developer/Designer)**
- Delete placeholder CMS items in Webflow
- Add Meta Title + Description to CMS as separate fields; map OG Image to Main Image; update page template
- Confirm schema markup implementation approach with William; implement custom code block in Webflow if needed
- Build author CMS (Teams collection); add post-bottom bio block with avatar; link to Content CMS author field; load William's bio
- Design and implement sitemap footer (pending Krista's approval via William)

**Tanya (Underbelly)**
- Email Krista: request 60–80 word author bios (emphasizing expertise focus); confirm footer placement; remind her to provide missing Privacy Policy page

**William Leborgne (GrowthX)**
- Follow up with other GrowthX managing directors on how they implement schema markup in Webflow
- Ask Krista for approval to add sitemap footer to website

---

## Transcript
**Tony D'Amico:** It looks like you're trying to connect to audio.

**Tony D'Amico:** There.

**Tony D'Amico:** Now it says you're not connecting to audio.

**Tanya:** Can you hear me now?

**Tanya:** There we go.

**Tanya:** Okay.

**Tanya:** Sorry, I couldn't get Zoom to open.

**Tony D'Amico:** I'm pinging them right now, okay?

**Tony D'Amico:** Yeah, no worries.

**Tony D'Amico:** Yeah, that's what was on my other computer, and it was like, oh, great, Zoom, and I can't install anything on my other computer.

**Tanya:** I usually don't have issues with it, but today it was not.

**Tony D'Amico:** Oh, every time I open Zoom, it's like, update, you need to do that.

**Tanya:** It's like.

**Tanya:** I know.

**Tanya:** I'm writing them right now.

**Tanya:** Okay, I just sent him a message.

**Tanya:** Busy, busy.

**Tony D'Amico:** Yeah, it's my day.

**Tanya:** Same.

**Tony D'Amico:** Okay, and they just want me to walk through how to use?

**Tanya:** The new shadow area, yeah.

**Tanya:** Okay.

**Tanya:** Yep.

**Tanya:** They should be hopping on because this is their invite, so.

**Tanya:** Sorry, I'm just sending a quick message to Sam.

**Tanya:** Thank you.

**Tanya:** Let me see if they had a phone number by chance in their email signature.

**Tanya:** They do not.

**Tanya:** So we'll give it a couple more minutes.

**Tony D'Amico:** Sounds good.

**Tony D'Amico:** I mean, I can even walk you through it.

**Tony D'Amico:** This meeting's recording even.

**Tanya:** So let me.

**Tanya:** Yeah, how about we do that?

**Tony D'Amico:** I'll just start sharing my screen.

**Tony D'Amico:** And then if they hop on, we can always just revisit.

**Tanya:** over.

**Tanya:** That sounds great.

**Tony D'Amico:** All right.

**Tony D'Amico:** Okay.

**Tony D'Amico:** So, I mean, it's literally just set up like any other CMS.

**Tony D'Amico:** CMS.

**Tony D'Amico:** So when you're logged in, I don't have, this isn't the edit view, obviously, but that's where they're going to have is edit view.

**Tony D'Amico:** But you go to the CMS, it's contents, and then.

**Tanya:** Perfect.

**Tony D'Amico:** Yeah, you just go through, fill out the information.

**Tanya:** Populate unless you manually change the top, right?

**Tony D'Amico:** Yeah.

**Tony D'Amico:** Sorry, say that again.

**Tanya:** If you, like, hit the plus sign and make a new page, the slug will auto-populate when you make the title.

**Tanya:** But if you change the name here, you'll have to redo the slug, yeah?

**Tony D'Amico:** Like if you use something pre-populated?

**Tony D'Amico:** Yeah, these were just pre-populated.

**Tony D'Amico:** We should just delete all of them.

**Tony D'Amico:** I just had them in here for testing purposes.

**Tony D'Amico:** But yeah, we would just go new, name.

**Tony D'Amico:** The slug will automatically create.

**Tony D'Amico:** I think I just have main image.

**Tony D'Amico:** And then this is like a future proof thing.

**Tony D'Amico:** And if we do need it.

**Tony D'Amico:** It on a list.

**Tony D'Amico:** Actually, no, I'm sorry.

**Tony D'Amico:** There is a list.

**Tony D'Amico:** So this thumbnail, this is the main image, the published date, author, outlet.

**Tony D'Amico:** I did this just in case it was like it was like, say, they're pushing something out from TechCrunch and then they're writing about it.

**Tanya:** We can put the outlet.

**Tony D'Amico:** This is optional.

**Tony D'Amico:** It's not required.

**Tony D'Amico:** Oh, there we go.

**Tanya:** Hey, William.

**William Leborgne:** I am so sorry, y'all.

**William Leborgne:** I was stuck on a call and I could, I was just like, I need to go.

**William Leborgne:** I need to go.

**Tony D'Amico:** I'm so sorry.

**Tony D'Amico:** Hey, no worries.

**Tony D'Amico:** I had my issue this, like my other job.

**Tony D'Amico:** They scheduled a meeting that was anyway.

**Tony D'Amico:** So thanks for being flexible on my side.

**William Leborgne:** No worries.

**William Leborgne:** No worries.

**William Leborgne:** Cool.

**William Leborgne:** Okay.

**William Leborgne:** Let's, let's dig in.

**Tanya:** I know this will probably be very fast.

**Tony D'Amico:** Yes.

**Tony D'Amico:** Um, I think that I have this, let me double check that it's live.

**Tony D'Amico:** Yeah, it is.

**Tony D'Amico:** Okay.

**Tony D'Amico:** So, um, are you.

**Tony D'Amico:** Are familiar with Webflow?

**Tony D'Amico:** Yeah.

**Tony D'Amico:** Okay.

**Tony D'Amico:** So, I mean, that's really, it's just using that CMS under Contents.

**Tony D'Amico:** I think you guys will probably just get an edit access.

**Tony D'Amico:** I don't know if you'll have a design one, but the CMS is Contents.

**Tony D'Amico:** And basically, it's pretty straightforward.

**William Leborgne:** These ones were just auto-populated so we can delete them.

**William Leborgne:** I just used them for testing.

**Tony D'Amico:** Yep.

**Tony D'Amico:** But you've got Name, the Slug, which will automatically create under Content.

**Tony D'Amico:** Content, the Main Image, the Thumbnail Image, a Published Date, Author.

**Tony D'Amico:** I didn't do like an image for the author.

**Tony D'Amico:** If we need to add one, we can.

**Tony D'Amico:** And then Outlet is, I did, if there was like a news outlet that it's related to, because they use a lot of it.

**Tony D'Amico:** So, you can add it.

**Tony D'Amico:** It's not required.

**Tony D'Amico:** It doesn't need to go in if you don't need it.

**William Leborgne:** It's just, again, more of an optional thing.

**William Leborgne:** Okay.

**Tony D'Amico:** Post Summary.

**Tony D'Amico:** And then Body Post.

**Tony D'Amico:** The thing is with the Table of Contents, it's related to the H.

**Tony D'Amico:** So you do need to at least put in, it'll do H1, 2, or 3.

**Tony D'Amico:** So you just have to highlight your header and then give it an H1, 2, or 3 tag, and it will populate for the table of contents.

**William Leborgne:** Okay, got it.

**William Leborgne:** And the table of contents is just H2s or also H3s?

**Tony D'Amico:** It's all of them, yeah.

**William Leborgne:** Oh, wow, okay.

**Tony D'Amico:** Yeah, I think we can change it because it's just a plug-in from, oh gosh, what is that place called?

**Tony D'Amico:** F and Sweet.

**Tony D'Amico:** It's one of their plug-ins.

**Tony D'Amico:** I think that it is actually, let me double check.

**Tony D'Amico:** So this one is the Promoting Diversity.

**Tony D'Amico:** It might not be the H1 tag business case for diversity.

**Tony D'Amico:** Yeah, so it's not H1.

**Tony D'Amico:** It's probably H1 and H...

**Tony D'Amico:** Actually, it might just be H2s.

**Tony D'Amico:** I think it's just H2s.

**William Leborgne:** Okay, that's great.

**William Leborgne:** That's better.

**Tony D'Amico:** Let double check.

**Tony D'Amico:** That's published.

**Tony D'Amico:** Yeah, it looks like it's H2s or H3s.

**William Leborgne:** Okay.

**Tony D'Amico:** But the, yeah, H1 tag is not in there.

**William Leborgne:** Okay, got it.

**Tony D'Amico:** Featured, that's just if it needs to be featured.

**Tony D'Amico:** And then sitemap indexing, there's not, we can turn that off if we don't want, that's, I think, what we don't want.

**Tony D'Amico:** It's really just for, like, the search engine on the site itself.

**Tony D'Amico:** But I don't think this will cause problems with.

**Tony D'Amico:** Yeah, it's just, no, actually, this will probably be.

**Tony D'Amico:** So I would keep that on for those.

**Tony D'Amico:** And then that's it.

**Tony D'Amico:** This color doesn't need to be there.

**Tony D'Amico:** can't believe that.

**Tony D'Amico:** That was just from, again, the template that it used for the content.

**William Leborgne:** Okay.

**William Leborgne:** A couple questions.

**William Leborgne:** Where can I, I don't know if I missed that already, where can I update meta descriptions and schema markup and some of those things?

**Tony D'Amico:** If we need a meta description, let me just add it really quick.

**Tony D'Amico:** It's not on there.

**William Leborgne:** These were, these are things that if there's, I need to add, we can add really quick.

**William Leborgne:** Okay.

**William Leborgne:** Yeah.

**William Leborgne:** We need meta title, meta description, and schema.

**William Leborgne:** Those are three that we definitely need.

**Tony D'Amico:** Okay.

**Tony D'Amico:** So let me see.

**Tony D'Amico:** Oh, yeah.

**Tony D'Amico:** So we'll do, it doesn't need to rich text, meta description.

**Tony D'Amico:** And the meta title you want different than.

**William Leborgne:** Yeah.

**William Leborgne:** Meta title, meta description needs to be two different fields.

**Tony D'Amico:** Well, I'm from the regular title.

**Tony D'Amico:** Yeah.

**William Leborgne:** Yeah.

**William Leborgne:** Yeah.

**William Leborgne:** Yeah.

**William Leborgne:** Yeah.

**William Leborgne:** Different.

**Tony D'Amico:** Yep.

**Tony D'Amico:** Okay.

**Tony D'Amico:** So I will do, let's see.

**Tony D'Amico:** And then the schema, what is, how do you want that, what it, sorry, I'm not familiar with that.

**William Leborgne:** So how do you want that set up?

**William Leborgne:** Schema is typically just a text field as well.

**Tony D'Amico:** Okay.

**William Leborgne:** I just want to make sure that like, because you're adding it just as a text field.

**William Leborgne:** Because usually it's like a, I'm not technical enough to know if there's like something specific we need to do, but like Google needs to know that it's a schema markup.

**William Leborgne:** And I wonder if it can just pick it up by the title.

**William Leborgne:** It's too bad Hassan couldn't join because he would have known this.

**Tony D'Amico:** I'll follow up with you guys on the schema markup thing.

**Tony D'Amico:** Okay.

**Tony D'Amico:** Yeah, let me know on that one.

**Tony D'Amico:** That one's easy.

**Tony D'Amico:** Or if it's just the, if we need to change it to like anything else, I could probably do it pretty quick.

**Tony D'Amico:** Yeah, so MetaTitle, I just need to save that then, and on the page itself, I'm going to need to change that, because that is going to be, oops, let's keep doing that.

**William Leborgne:** You probably know this already, but MetaTitle, Description, and Schema Markup don't show up on the page.

**Tony D'Amico:** Correct, but they, there's on the, in Webflow, you have to attach it for it to come up, because if not, it's just going to be, so see where it's like MetaDescription?

**Tony D'Amico:** Yeah, yeah, okay.

**Tony D'Amico:** I have to go in and put MetaDescription, and then the same thing with, so the title tag, that one will also be, the MetaTitle, so then that will pull that data in here, instead of using from, Okay, cool.

**Tony D'Amico:** the other places.

**Tony D'Amico:** Open graph image, we'll do main image.

**Tony D'Amico:** Okay.

**Tony D'Amico:** Yeah, was, like, wondering if it'll let me customize that if we don't want the H3s on there.

**William Leborgne:** That's fine.

**William Leborgne:** Don't worry about it.

**William Leborgne:** We don't, we honestly don't use H3s that much.

**William Leborgne:** Okay.

**William Leborgne:** Cool.

**William Leborgne:** And, and the meta, and sorry, the schema markup was in there, too?

**Tony D'Amico:** Yeah, that's, that, but that one, I don't know how it would come up on the page, because there's not, like, a, on the template, page template, there's not, like, a schema markup.

**Tony D'Amico:** So we have to do, like, a custom code for that one.

**William Leborgne:** We can add it in.

**Tony D'Amico:** Okay.

**William Leborgne:** I can follow up with you on that.

**William Leborgne:** Because we have a number of other clients using Webflow, so I can just ask, like, some of the other managing directors how they do it, and maybe they can just, like, hand that over.

**Tony D'Amico:** Yeah, and I can, I, okay, yeah, let me know.

**William Leborgne:** Cool.

**William Leborgne:** you.

**William Leborgne:** And then for the author, we do need a blurb and an image.

**William Leborgne:** Image is optional, but it's ideal.

**William Leborgne:** But definitely we need a blurb because that's how they see the author as an expert.

**William Leborgne:** So typically that's either at the bottom of the blog or it can be its own page.

**William Leborgne:** I don't know how you guys want to set that up.

**Tony D'Amico:** Okay.

**Tony D'Amico:** We can do that.

**Tony D'Amico:** So like, so like at the bottom, you'd have like an avatar and be like, you know, Krista, and then it would have like a brief bio of her.

**William Leborgne:** That's right.

**Tony D'Amico:** Okay.

**Tony D'Amico:** Let's, do you know, is it only going to be people from their team that we're going to be putting in content from, or do you know if it's going to be others?

**William Leborgne:** For now?

**William Leborgne:** No, I think it's really going to be internal experts.

**Tony D'Amico:** So probably Krista and other people on the team.

**Tony D'Amico:** Okay.

**Tony D'Amico:** Cause then what I'll do, we'll just have to have them.

**Tony D'Amico:** So, Tanya, let me write this down because I will forget.

**Tony D'Amico:** We'll set up on the Teams CMS.

**Tony D'Amico:** I'll put in all the info there and then tie it to this page.

**Tony D'Amico:** So she's just going to need to write, or I'm not sure, William, if you guys are going to need to write, but for the bios.

**Tony D'Amico:** We'll put that in on the Teams page.

**William Leborgne:** I'll do like a bio for that.

**Tony D'Amico:** That's a small one.

**Tony D'Amico:** And then we'll do, we can just pull in the avatar because those are already there.

**William Leborgne:** Okay, great.

**Tony D'Amico:** And then I'll just design a quick thing to go at the bottom of the page with that for them.

**William Leborgne:** Super.

**Tanya:** Awesome.

**William Leborgne:** And then I just had one last, two last little things.

**William Leborgne:** One is just a note from Hassan who is saying, Webflow can be a little tricky with tables.

**William Leborgne:** Because we do create quite a lot of content that has tables.

**William Leborgne:** Is that...

**William Leborgne:** Is something that is already built into your Webflow?

**Tony D'Amico:** No, Webflow does not have a native, unfortunately, native table for their media-rich text boxes.

**Tony D'Amico:** So you have to do a custom code for it, unfortunately.

**Tony D'Amico:** You can do a code block and then just add it.

**Tony D'Amico:** So I did mention that to Krista.

**Tony D'Amico:** She must have not have passed that along.

**Tanya:** No, we talked to someone on your team.

**Tanya:** It was a lady.

**William Leborgne:** Oh, sorry.

**William Leborgne:** Yes, I'm so sorry.

**William Leborgne:** Because I think Hassan brought it up and I forgot that you had the email chain about it.

**Tanya:** Okay.

**Tanya:** It's fine.

**Tanya:** And she said we can start with what Webflow has for now and revisit it if you guys want us to look at making something custom.

**William Leborgne:** Okay.

**Tanya:** All right.

**Tanya:** Cool.

**Tanya:** Great.

**William Leborgne:** And then my last nugget is just figuring out, like, just so I know where will the link to content exist on the website itself?

**William Leborgne:** Is it going to be in the main nav?

**William Leborgne:** Is it going to be in the footer?

**William Leborgne:** What's the – my understanding was they didn't

**William Leborgne:** We want it to be super in the, you know, available, but we would at least need it in the footer because, you know, because of click depth.

**Tony D'Amico:** You are going to need to work that out with Krista, Tanya, because there is no, there's no footer on their site.

**Tony D'Amico:** Oh, yeah, there is.

**William Leborgne:** But it's, well, footer as in like sitemap footer.

**William Leborgne:** Yeah, yeah, yeah.

**Tony D'Amico:** It's just, they're at, so we could do in a quick, just another column with like all of the normal links that we'd have like in the bottom of a table, a footer.

**Tony D'Amico:** Why am I, why is my brain shutting down?

**Tony D'Amico:** Just like the sitemap.

**Tony D'Amico:** Yeah.

**Tony D'Amico:** Like we can throw all that in there.

**Tony D'Amico:** And then again, they still don't have their privacy policy page.

**Tony D'Amico:** So that's something you can remind her that she needs to get up.

**Tanya:** Okay.

**Tanya:** William, did you want to ask her if she wants to add that to the footer?

**William Leborgne:** Did you need me to?

**William Leborgne:** I'm good either way.

**William Leborgne:** No, I can, I can do it.

**William Leborgne:** Okay.

**William Leborgne:** Ask Krista.

**William Leborgne:** Okay.

**Tony D'Amico:** We can design that real quick.

**Tony D'Amico:** That won't take but maybe like 20 minutes to add in.

**William Leborgne:** Okay.

**Tony D'Amico:** It's just whether or not this was like, I don't remember.

**Tony D'Amico:** was so long ago when we built this site.

**William Leborgne:** I don't remember if there was like an intentional reason of not having that in the footer.

**William Leborgne:** Got it.

**William Leborgne:** Okay.

**William Leborgne:** Okay, cool.

**William Leborgne:** So just jumping back into Webflow, if I want to get to content, it's really just straightforward.

**William Leborgne:** I just go to CMS, and that's the very top one, content.

**Tony D'Amico:** And then I just do new content, and I can build out my new blog post and publish it.

**Tony D'Amico:** Yep.

**Tony D'Amico:** And we'll delete out these ones that are in there right now because those are just placeholders, so they'll be out of there.

**William Leborgne:** Okay.

**Tony D'Amico:** Super.

**Tony D'Amico:** Yeah, and that should be it.

**Tony D'Amico:** And if you guys run into any issues as you're building it that need to just be custom to how you guys want to build, I mean, just shoot it over.

**Tony D'Amico:** We can easily change whatever.

**William Leborgne:** Yep.

**William Leborgne:** Okay.

**Tanya:** Sounds good.

**Tanya:** And then Tony will work on.

**Tanya:** Adding a bio section on the team page of the site so that it pulls into this along with their headshot.

**Tanya:** But we will need bios generated, you said, right, Tony?

**Tanya:** Yeah.

**Tony D'Amico:** Okay.

**William Leborgne:** Yeah, because on the current team's pages, mean, they're massive.

**Tanya:** Yeah.

**Tony D'Amico:** Yeah.

**Tony D'Amico:** So I just need something specific that I can add in as a content block on these.

**Tony D'Amico:** Yeah.

**Tony D'Amico:** With that, so.

**Tanya:** Are you William going to ask for that or did you need me to ask Krista for that?

**William Leborgne:** If you don't mind asking her for this one because you're more connected to this thing, that would be great.

**William Leborgne:** And then just, so that means that once I'm in this content CMS and I go to the author page, I would just get a dropdown or something, right?

**William Leborgne:** then I just.

**Tony D'Amico:** Yeah.

**Tony D'Amico:** So like what I'll end up doing is on, it'll look, let's see, on the news items, this will be the best example.

**Tony D'Amico:** So what I did here was I created a database of like images so that if we ever needed to update them, we could do it from.

**Tony D'Amico:** it from, from, could it from, could we do could could do we

**Tony D'Amico:** One place, news images.

**Tony D'Amico:** I could get the concept, though.

**Tony D'Amico:** Yeah, one of these has them on there where you just grab, it'll be like a drop down, and then you just select it.

**Tony D'Amico:** Yeah.

**Tony D'Amico:** Awesome.

**Tony D'Amico:** Oh, newsroom, that's what it was.

**Tony D'Amico:** Yeah, so, yeah, it'll be like this.

**Tony D'Amico:** It'll say, we'll see people, and then you just can select from the person, and then it'll load in all this stuff.

**Tanya:** Do we want, do you guys want me to tell Krista a word limit to try to keep those short bios, too, or?

**William Leborgne:** Yeah, I think probably no more than 80.

**Tanya:** Okay.

**William Leborgne:** But between 60 and 80, I think it's probably fine.

**William Leborgne:** Okay.

**William Leborgne:** I think the focus should just be like what their expertise is.

**Tanya:** Okay.

**Tanya:** I'll let her know.

**William Leborgne:** Great.

**Tony D'Amico:** I probably will now.

**Tony D'Amico:** I be able to get to that today.

**Tony D'Amico:** I'll be able to definitely buy it over, like, the weekend.

**Tony D'Amico:** So I will get those pieces, like, built out.

**William Leborgne:** So my money should be done from my side.

**William Leborgne:** Super.

**William Leborgne:** Yeah, no rush on our part because we're still building up the content strategy.

**Tony D'Amico:** So we'll probably only start publishing by end of next week.

**Tony D'Amico:** Okay, perfect.

**Tony D'Amico:** Yeah, they'll be done by then.

**William Leborgne:** Super.

**Tanya:** Okay.

**Tanya:** Thanks, y'all.

**William Leborgne:** I appreciate it.

**Tony D'Amico:** No problem.

**Tony D'Amico:** All right.

**Tony D'Amico:** Talk soon.

**Tony D'Amico:** Yeah.

**Tony D'Amico:** Bye.
