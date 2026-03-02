# Hubspot walkthrough

<metadata>
date: 2025-12-16
time: 15:30 UTC
duration: 24 minutes
organizer: Erik O'Brien
participants: Erik O'Brien, Sulaman Ahmed, Sara Randall
fathom_recording_id: 109068596
fathom_url: https://fathom.video/calls/507332532
share_url: https://fathom.video/share/LKLunfzsoJUYjuP-LquhSY6SA_uMjuNo
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Sara Randall walked GrowthX through Fieldguide's HubSpot blog publishing workflow for the "Resource Articles" blog, covering a two-step process: publishing articles with specific metadata (Deirdre Dolan as author, sequential Abstract featured images, Read More separator) and then populating the resource library via HubDB. The team clarified content formatting best practices, link handling (open external links in new tabs by default, except final CTAs), and table/heading management, while Sulaman awaited resolution of his multi-factor authentication issue to gain HubSpot access.

---

## Context

Fieldguide is an external client for whom GrowthX is creating content. Sara Randall, Fieldguide's operations/systems lead, scheduled this training session to onboard GrowthX team members (Sulaman Ahmed and Erik O'Brien) on the specific workflow and requirements for publishing GrowthX-authored articles in Fieldguide's HubSpot instance. The blog articles will be published under the byline of Deirdre Dolan, Fieldguide's corporate voice, and will populate a resource library visible on Fieldguide's website. This is part of an ongoing content marketing engagement where GrowthX writes substantive articles for Fieldguide's blog and resource section.

---

## Relevance

### To GrowthX Delivery

- **Blog workflow documentation:** Clear two-step publishing process (blog post → HubDB row) reduces operational friction for content uploads; table copy-paste and heading formats established as standards.
- **Formatting requirements:** Standardized on Deirdre Dolan as corporate author, sequential Abstract image series (purple → green → yellow → blue → pink), and Read More separator placement — simplifies QA and reduces revision cycles.
- **Content optimization:** All external links default to new-tab opening (except final CTAs) keeps users engaged with articles longer, improving time-on-page metrics.

### To GrowthX Business Development

- **Client account health:** Fieldguide implementing security compliance (MFA rollout) — positive signal of operational maturity; IT responsiveness (Robert) to access issues suggests solid partner.
- **Expansion opportunity:** Sulaman positioned as primary publisher with edit/publish access; implies GrowthX will handle ongoing content flow, not one-off deliverables.
- **Support continuity:** Sara available through end of week; knowledge base referenced as self-service option suggests transition toward customer-led operations (scalable for GrowthX).

---

## Overview

- **Publish to the "Resource Articles" blog first.** This is the dedicated library for growthx.ai content.
- **Use the two-step publishing process:** 1) Publish the article in the blog editor, then 2) add a row to the "resources" HubDB table to populate the main library cards.
- **Follow strict formatting rules:** Use "Deirdre Dolan" as the author, apply the correct sequential "Abstract" featured image, and insert a "Read More" separator after the first paragraph.
- **Open all links in new tabs** to keep users on the article page, except for final, explicit CTAs (e.g., "Request a Demo").

---

## Key Topics

### HubSpot Access

  - **Problem:** Sulaman cannot log in due to a multi-factor authentication (MFA) issue.
  - **Resolution:** Robert (Fieldguide IT) is working on a fix.
  - **Permissions:** Sara confirmed Sulaman has the necessary access for the blog and HubDB.

### Step 1: Create the Blog Post

  - **Location:** `Content > Blog`. Select the "Resource Articles" blog from the dropdown.
  - **Content Formatting:**
      - **Source:** Paste content into a plain-text editor first to strip hidden formatting.
      - **Tables:** Copy-paste works cleanly.
      - **Headings:** Reapply manually. Use `H2` for main sections and `H3` for sub-sections, referencing existing posts for the style guide.
      - **Fonts:** The template automatically applies the correct font ("Inter").
  - **Required Metadata (`Settings` gear icon):**
      - **URL Slug:** Create an SEO-friendly URL.
      - **Author:** Select "Deirdre Dolan" as the corporate face.
      - **Featured Image:** Use the next image in the "Abstract" series (purple, green, yellow, blue, pink).
  - **In-Post Elements:**
      - **"Read More" Separator:** Insert after the first paragraph (`Insert > Read More Separator`) to create the preview text for search results.
      - **Links:** Open in a new tab by default to keep users on the article page.
          - **Exception:** Final, explicit CTAs (e.g., "Request a Demo") can redirect in the same tab.

### Step 2: Add to HubDB

  - **Purpose:** Populates the article cards in the main "Resource Library" section of the website.
  - **Location:** `HubDB > resources`.
  - **Process:**
    1.  Click `Add Row`.
    2.  Enter the blog title.
    3.  Upload the same "Abstract" image used in the blog post.
    4.  Add the meta description.
    5.  Paste the live article URL.
    6.  Publish the HubDB row.

### Previewing & Support

  - **Article Preview:** The `Preview` button generates a shareable link.
  - **HubDB Preview:** Not available; the table is a raw data backend.
  - **Support:** Sara is available via Slack until Friday. For general HubSpot questions, use the platform's knowledge base.

---

## Action Items

**Sara Randall (Fieldguide)**
- Delete lorem ipsum demo blog post from HubSpot

**Robert (Fieldguide IT)**
- Resolve Sulaman Ahmed's multi-factor authentication (MFA) login issue to enable HubSpot access

**Sulaman Ahmed (GrowthX)**
- Gain HubSpot access once IT issue is resolved
- Publish first article using the two-step workflow: 1) Create and publish post in "Resource Articles" blog, 2) Add row to "resources" HubDB table with matching Abstract featured image and meta description

---

## Transcript
**Sulaman Ahmed:** A few things before Sara arrives, they shared an email account access with us, and that email account ultimately had access to the CRM, CMS.

**Sulaman Ahmed:** I was unable to log in.

**Sulaman Ahmed:** Hey, greetings, Sara.

**Sulaman Ahmed:** How are you?

**Sulaman Ahmed:** How are y'all?

**Sara Randall:** Good.

**Sulaman Ahmed:** Is it morning, afternoon, either way?

**Sara Randall:** Hello?

**Sulaman Ahmed:** Yep, it's different, different time zones.

**Sulaman Ahmed:** For me, it's night, I reckon it's morning.

**Erik O'Brien:** Yep.

**Erik O'Brien:** 9pm?

**Sara Randall:** Yep, it's 8.31pm for me.

**Sara Randall:** Thank you.

**Sara Randall:** So, Erik, Sulaman, great to- forget it.

**Sara Randall:** Do you you

**Sara Randall:** meet you and thanks for taking the time.

**Sara Randall:** If you wanted to go ahead, I see you have your note taker here, which is great.

**Sara Randall:** If you need to record, full permission, I'd like to do that as well.

**Sara Randall:** I guess the first question I'll ask is, I double checked that, Sulaman, I think you're the one who will be doing the uploads into our HubSpot account.

**Sara Randall:** And I do see that you have a user.

**Sara Randall:** But when I checked earlier today, I noticed that you hadn't logged in yet.

**Sara Randall:** So I just want to make sure that you're able to get in okay?

**Sulaman Ahmed:** Actually, this is the same thing I was explaining to Erik.

**Sulaman Ahmed:** I received an email, Gmail invitation.

**Sulaman Ahmed:** I was unable to accept it.

**Sulaman Ahmed:** I was facing an issue.

**Sulaman Ahmed:** So I informed earlier and I reckon someone from the team, Robert, has already reached out to me.

**Sulaman Ahmed:** He shared another link with me.

**Sulaman Ahmed:** Although I even though I tried from that link, I was still unable to log into the Gmail account.

**Sulaman Ahmed:** I have informed Robert back, but hopefully soon enough as soon as Rob.

**Sulaman Ahmed:** Field figures out a solution for that.

**Sulaman Ahmed:** I would have access to that.

**Sulaman Ahmed:** And definitely that email account has access to the HubSpot and other accounts.

**Sulaman Ahmed:** So that's the starting point.

**Sara Randall:** Okay.

**Sara Randall:** Very good.

**Sara Randall:** Just wanted to make sure you were, if you were in there, you were on track to working with our IT folks to get in there.

**Sara Randall:** So very, very good.

**Sara Randall:** He's definitely the right person to do the, I think it's like a multi-factor authentication issue.

**Sara Randall:** And we were just rolling out some security compliance stuff here.

**Sara Randall:** So that's where that comes from, for sure.

**Sara Randall:** All right.

**Sara Randall:** So I guess it probably makes most sense then.

**Sara Randall:** I think my preferred train, train the trainee is to sit on my hands and have you share your screen and I walk you through it.

**Sara Randall:** But let's kind of reverse the script here.

**Sara Randall:** And I'll kind of do the following along with the teacher method as a secondary here.

**Sara Randall:** And, of course, you've got your recording.

**Sara Randall:** So let's go ahead and do, I'll do a share screen.

**Sara Randall:** I think I'll just do my window.

**Sara Randall:** So.

**Sara Randall:** Just do entire screen.

**Sara Randall:** Screen to share.

**Sara Randall:** Okay.

**Sara Randall:** And then I'm going to move that window so we don't get camera ception.

**Sara Randall:** Let me know.

**Sara Randall:** Can you see my Google?

**Sara Randall:** Yep.

**Sulaman Ahmed:** Awesome.

**Sulaman Ahmed:** So I'm going to go into HubSpot.

**Sara Randall:** Everybody's kind of first splash page in HubSpot tends to be different, but there's, of course, a different selection of icons and whatnot along the side, depending on what your permissions are.

**Sara Randall:** And I did retune your permissions this morning, Sulaman, so that you have at least the two specific areas that I'm aware of that you need.

**Sara Randall:** If you need more access, just let me know.

**Sara Randall:** I think you have my direct access through our Slack.

**Sara Randall:** Just give me a holler there.

**Sara Randall:** But the two pieces will be through the content section, of course, to update the blog, which I'll go through the specific steps there to put the content in as a blog article.

**Sara Randall:** And then the second step will be publishing it through.

**Sara Randall:** PubDB.

**Sara Randall:** And if you're not familiar with that, I'll definitely give you kind of a round the horn in terms of what that means and why we use it.

**Sara Randall:** So I'll stop there.

**Sara Randall:** Sound good?

**Sara Randall:** Yep.

**Sulaman Ahmed:** Okay.

**Sulaman Ahmed:** Very good.

**Sara Randall:** So in content, we're going to pop over to the blog.

**Sara Randall:** And we have a couple of blogs.

**Sara Randall:** So this drop down here, you're going to see there's one that's like the true blog, right?

**Sara Randall:** Where we post like primarily the content that our content manager, Amanda, who I know you guys work with directly in terms of approvals.

**Sara Randall:** That's kind of the primary blog.

**Sara Randall:** Then we have a secondary blog that's dedicated.

**Sara Randall:** It's like a subset of our content libraries or case study content.

**Sara Randall:** That's just like the framework within which that we built that.

**Sara Randall:** Those articles live there.

**Sara Randall:** And then this resource articles is actually the blog where we've been posting everything from y'all.

**Sara Randall:** So I'm going to call this like the SEO rich article library is this third blog.

**Sara Randall:** And then if it's helpful to know where that then publishes is under our resource section, resource library, there's this articles sub-nav in here.

**Sara Randall:** And this is where we've got, this is kind of where HubDB comes into play a little bit, but you'll notice I've kind of selected that this is like a lorem ipsum design that we have in our larger design library.

**Sara Randall:** And so what we'll do is I'll show you how to apply this and kind of follow the color scheme, right?

**Sara Randall:** It's like purple, green, yellow, blue, pink, purple, green, yellow, blue, pink.

**Sara Randall:** Kind of follows like one after the other in terms of whatever is next will be purple because that's what comes after pink.

**Sara Randall:** Got it.

**Sara Randall:** So that's a pattern.

**Sara Randall:** It's the pattern, yeah.

**Sara Randall:** So like we have a set of five, right?

**Sara Randall:** One of each color and then whatever is next will follow it, fall in line in terms of what color featured image that it uses.

**Sara Randall:** And I'll show you how to get that in here.

**Sara Randall:** So pretty straightforward, right?

**Sara Randall:** You're in the right blog.

**Sara Randall:** Make sure to toggle resource articles when you're in the blog section of HubSpot here so that you're in the right space to create the content.

**Sara Randall:** Of course, click the create button here and it'll default to say that's the right blog.

**Sara Randall:** English, of course, is what we'll default to, at least for now.

**Sara Randall:** We will hopefully one day become multilingual, but for now we're sticking with English.

**Sara Randall:** And then it's pretty self-explanatory, but I'm going to go through the core parts of it, right?

**Sara Randall:** There's the blog title.

**Sara Randall:** You'll click into this editor box and put in the title of the blog.

**Sara Randall:** Click in the pencil box here, and this is, of course, where the core content will go.

**Sara Randall:** Some of the metadata is obviously going to be what you're going to access and apply through these settings.

**Sara Randall:** So this little gear icon up here on the right-hand side, you'll come here, where you could also apply the blog title so you don't necessarily have to do it in line.

**Sara Randall:** In the editor, you could do it all through here if you prefer.

**Sara Randall:** So you could do that.

**Sara Randall:** And then here is where you would put the URL slug or, you know, what comes after fieldguide.io.

**Sara Randall:** This is just the subset where we park it on the blog.

**Sara Randall:** And then, you know, your SEO friendly URL string would go here.

**Sara Randall:** Scroll down just a tick.

**Sara Randall:** The author that we've decided is Dee, which I think she comes up as Deirdre.

**Sara Randall:** So Deirdre Dolan, as you might have noticed, is kind of our corporate face of these articles.

**Sara Randall:** That's the fieldguide person that we're kind of putting on as the author for these posts that y'all are creating.

**Sara Randall:** So you'll select her.

**Sara Randall:** And it'll automatically apply her, like, author information, her profile picture, bio, and things like that.

**Sara Randall:** No need to do that blog over blog.

**Sara Randall:** And then this is that featured image I was telling you about.

**Sara Randall:** If you click on Browse Images, the easiest way to find it, I've noticed, is Abstract.

**Sara Randall:** And you're going to see the library of those.

**Sara Randall:** And you'll notice there's kind of a different variety of like how the shapes play.

**Sara Randall:** And so there's ones that are like a circle on the bottom and the half circle on the top.

**Sara Randall:** I don't really have a unique naming convention for those.

**Sara Randall:** It's just you'll notice that they're part of this larger image set.

**Sara Randall:** And as I mentioned, kind of cascading one, three, four, five, one, three, five through the.

**Sara Randall:** Great.

**Sara Randall:** So that's how you apply that.

**Sara Randall:** The only other content thing that's just like best practices that I think are helpful to know is when you're copy pasting things out of probably Word, right, into the HubSpot editor, it oftentimes will like take and try and kind of butcher the styling quite a bit.

**Sara Randall:** And so I usually copy pasted into say like a plain text editor before ushering it over into HubSpot just to like kind of get.

**Sara Randall:** of any of that weirdness and allow you to inline, like reapply, cleanly, bolds, any italicized or any links and things like that into the body content.

**Sara Randall:** Another thing here, I'm just going to say, showing growthx.

**Sara Randall:** Blog, here is another sentence.

**Sara Randall:** So usually what we do is we apply a read more tag between kind of the intro paragraph and what's following on as the next piece.

**Sara Randall:** And so how you would do that is here through the insert, and there should be the read more separator.

**Sara Randall:** And what this is, it's kind of like indicating to the user, and it helps kind of show in some search engine result pages.

**Sara Randall:** It's kind of like that preview text, the lead in, where it then will naturally break.

**Sara Randall:** And so you'll notice if I go into one of these guys.

**Sara Randall:** And so

**Sara Randall:** Let me actually go into the edit post.

**Sara Randall:** You should see it applied.

**Sara Randall:** Maybe not to this.

**Sara Randall:** Yeah, see, it's like more dot, dot, dot.

**Sara Randall:** That's how it is naturally applied to the post.

**Sara Randall:** So I would just insert that using this drop down here after the first para.

**Sulaman Ahmed:** Recorded.

**Sulaman Ahmed:** So that's pretty much getting the blog in.

**Sara Randall:** And then, of course, when you're ready to go, and it's yelling at me because I haven't put in the metadata, but we just walk through how to apply all these individual pieces.

**Sara Randall:** Once those are in there, the tool will allow you to click publish.

**Sara Randall:** Got it.

**Sulaman Ahmed:** Again, there would be a drop feature in there too.

**Sulaman Ahmed:** So like usually what we do is I drop and then after the final review, we publish.

**Sulaman Ahmed:** Or obviously we can agree if I can get access till the end of the publication or if someone wants to review first and I can save the article in drop.

**Sulaman Ahmed:** So that depends.

**Sulaman Ahmed:** How team actors to continue that.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** There is one more quick question on this side.

**Sulaman Ahmed:** Usually in our content, we do have tables.

**Sulaman Ahmed:** Does this HubSpot directly copy-paste the tables or do we need to add that HTML code for that?

**Sulaman Ahmed:** That's a good question.

**Sara Randall:** I think there's one of these has a table, right?

**Sara Randall:** Let me just try to.

**Sara Randall:** I think that does copy-paste with no problem.

**Sara Randall:** Let me just test my theory here.

**Sara Randall:** Yeah, that should be no problem.

**Sara Randall:** That's like one of the very few components, content components that does cleanly copy-paste.

**Sara Randall:** That's a great question.

**Sara Randall:** I think a lot of the time, other kinds of formatting, like bullets in particular get really weird.

**Sara Randall:** Some bullets, like it'll choose like squares, like by default.

**Sara Randall:** And even though the overall CSS and template is meant to do circles.

**Sara Randall:** So this kind of person got it.

**Sulaman Ahmed:** And sometimes there is another pattern we have observed with different CMS is that if on the Google Doc we are using

**Sulaman Ahmed:** A different font, your CMS would pick up that font, which was on the Google Docs.

**Sulaman Ahmed:** So does it add a default font, or would it pick up the font we have just used on the Google Docs?

**Sara Randall:** That's a good question.

**Sara Randall:** I don't remember if I, I think I did have to re, re, I don't think I had to change the font, because our font, default font in the blog is Enter.

**Sara Randall:** And so I think it automatically will reformat the right font, but the font sizing and heading types, like if it's like an H1, H2, H3, when I was talking about where I did have to redo some of those.

**Sara Randall:** And so it's, sometimes it's good, and you do have edit access as well as publish access.

**Sara Randall:** Sometimes just going in and clicking on one of the existing ones and saying, okay, well, how did we type these and like cascade the H1, H2, H3s all the way through existing blogs as a point of reference for you?

**Sara Randall:** And like...

**Sara Randall:** Typically, anything that's not the title will go two.

**Sara Randall:** And then if there are any kind of, I think, did we type these as three?

**Sara Randall:** No, heading two, heading two.

**Sara Randall:** Might be a heading two.

**Sara Randall:** Got it.

**Sulaman Ahmed:** I think for the first article, yes, you are absolutely right.

**Sulaman Ahmed:** I think for the first article, when I publish, I will understand these things a lot more better.

**Sara Randall:** The nuance.

**Sara Randall:** The editor, yeah.

**Sulaman Ahmed:** Or how weird does the formatting go if I directly copy it.

**Sara Randall:** So I think that's fair enough.

**Sulaman Ahmed:** Also, Erik, would we like to cover those best practices like if we have an in-link, like embedded link, do we want to open it a new tab or do we want to be redirected within the same website?

**Sara Randall:** Yeah, that's a question.

**Sara Randall:** I would say.

**Sara Randall:** Sorry, go ahead.

**Sulaman Ahmed:** The best practice that I've usually followed across other clients is if it's an external link and not a link for our own company, we open it in a new tab.

**Sulaman Ahmed:** And if it's the link, please… you.

**Sulaman Ahmed:** If it's within our website, then we switch the same tab.

**Sulaman Ahmed:** So a new tab would open if it's an external website link.

**Sulaman Ahmed:** So shall we be good with that, Ruth, or any specific?

**Sara Randall:** Good question.

**Sara Randall:** I mean, that's a little bit more of a, we don't, we don't really have a standard for y'all to adopt.

**Sara Randall:** I think in general, we do open in a new tab regardless of the destination in real estate or out of real estate.

**Sara Randall:** Um, because the thinking, the thinking that we have there is, um, you know, you're on the blog and these are quite hefty blogs, very content rich, right?

**Sara Randall:** And so if they're, they click a link in like the midst of a blog, we want them to be able to access, whether it's like a source, a source for data, but then continue reading.

**Sara Randall:** And so if you redirect them, at least from a blog, it feels like a disjointed experience, Because we want them to be able to continue.

**Sara Randall:** I would say the only exception to that rule.

**Sara Randall:** That I've adopted is like, if it's at the very, very end, like last paragraph, last few sentences, if it's like, if it's, for instance, like request a demo, and that's like the very last sentence, right?

**Sara Randall:** Like, clearly, I think that's perfectly fine to redirect without opening a new page, because like, it's not its natural end, and clearly, we want to drive them to sales.

**Sara Randall:** So, that would be the only exception, I'd say, but...

**Sulaman Ahmed:** Just a slight confusion, so, but what we want, the links to open in a new tab, or do we want them to be redirected on the same page?

**Sulaman Ahmed:** I just like this.

**Sara Randall:** Yeah, I would do this.

**Sara Randall:** So, you would put the URL, put the URL here, and then just click this box, so that it does open.

**Sara Randall:** Open in a new tab, got it, got it.

**Sulaman Ahmed:** Perfect, I think we have covered...

**Sulaman Ahmed:** Putting the blogs in?

**Sara Randall:** Yeah, 100%.

**Sara Randall:** Awesome.

**Sara Randall:** So, I would recommend doing this step for...

**Sara Randall:** Once you have the post ready to go, published, it'll then be, of course, live in this section of the site.

**Sara Randall:** And then the secondary piece, which is what then applies it to these cards, and it adds it in to kind of the larger library outside of that specific dedicated section of the website, is HubDB.

**Sara Randall:** And so I'm going to take you over to that section next, and I'm going to get out of this.

**Sara Randall:** I'll delete this lorem ipsum post, so it doesn't cloud our CRM, but just for demonstration purposes, then we go to HubDB.

**Sara Randall:** And then you're going to notice there's a couple of different sections here that, for other purposes, resources is like that card library that's relevant to this.

**Sara Randall:** You scroll all the way to the bottom, and you're going to see, like, here are the most recent ones that we've posted on y'all's behalf.

**Sara Randall:** And it has just a couple of requirements.

**Sara Randall:** You would click Add Row to have a new dedicated unique row for the new content.

**Sara Randall:** This is where, like, the blog...

**Sara Randall:** Title will go, leave this as it is, mimic the same abstract image that you chose for the blog, and add that here so that it's consistent.

**Sara Randall:** If it's pink, it's pink, it's blue, it's blue.

**Sara Randall:** The description, of course, is where your meta description will go, and then the link of the blog.

**Sara Randall:** So it's pretty much one, two, three, four, publish, and then it'll go into that other larger library.

**Sara Randall:** Perfect.

**Sara Randall:** That's lot easier.

**Sara Randall:** Perfect.

**Sulaman Ahmed:** So I think we would publish the article first, and once it's published, only then we can add it to this hub database.

**Sulaman Ahmed:** Perfect.

**Sara Randall:** Yeah, because you need the URL to be live, right, before you'd want to publish it.

**Sara Randall:** So that's why the order of operations here is...

**Sara Randall:** Got it, got it.

**Sulaman Ahmed:** One small thing I would like to ask again, there is a preview button I can already see.

**Sulaman Ahmed:** So for some CMS, the preview buttons sometimes just not show up a specific section.

**Sulaman Ahmed:** Does the preview button for the HubSpot works?

**Sulaman Ahmed:** With all the data we use, or is there anything that it does not show clearly in the preview, like the full publishing, I would like to see the preview file.

**Sara Randall:** Yeah, yeah, for the article itself, not for this component, right?

**Sara Randall:** We're going back to the article itself.

**Sara Randall:** I was going to say, unfortunately, HubDB is just like, this is like the front-end raw code part, so there's no way to preview the way that this will card.

**Sara Randall:** But if we're talking about the blog itself, absolutely.

**Sara Randall:** Let me go back to that section really quick.

**Sara Randall:** So, coming over here, and so, yep, you would click the preview button here, and what it does, you can open it in a new tab, and it basically has this temporary slug, and like, basically, this query for preview link.

**Sara Randall:** And so, this would be something that I think you might, it might require HubSpot login is the only thing to be mindful of.

**Sara Randall:** Let me just double check it in and then take, you know, oh, no, you could actually share it outside of, so that's actually good.

**Sara Randall:** But no one else would know how to get here.

**Sara Randall:** That's, I think, why they make this real ugly and awful.

**Sara Randall:** And who would ever manually type that to try to find it?

**Sulaman Ahmed:** Also, the table does not seem to be too pleasant compared to the...

**Sulaman Ahmed:** Is there an option to customize it?

**Sulaman Ahmed:** Or is this the way HubSpot will place it?

**Sulaman Ahmed:** Oh, good question.

**Sara Randall:** Let's see if I go back.

**Sara Randall:** I think you can come in.

**Sara Randall:** You can change the alignments gently.

**Sara Randall:** Doesn't seem to be doing too, too much.

**Sara Randall:** Spacing.

**Sara Randall:** Maybe I just needed to add, like, a color.

**Sara Randall:** Let me save that.

**Sulaman Ahmed:** So it seems like there are a few options we can utilize.

**Sulaman Ahmed:** I can just centerline them just to make it look a bit better.

**Sulaman Ahmed:** Got it.

**Sulaman Ahmed:** That's good to know.

**Sara Randall:** Worst case scenario, I guess the copy-paste doesn't allow you...

**Sara Randall:** Yeah.

**Sara Randall:** ...

**Sara Randall:** You-I think I

**Sara Randall:** Some of the, like, this looks kind of, it does have some border-style solid table with pixels.

**Sara Randall:** And then it's applying some custom CSS for some reason.

**Sara Randall:** I don't know why.

**Sara Randall:** But if you do have to rebuild the table because the copy piece didn't do the job, it does have an insert table option, I believe.

**Sara Randall:** Can you tell it's been a long time since I've drafted a blog myself?

**Sara Randall:** But you could insert a table, and really it's just, like, how many rows do you need?

**Sara Randall:** And then it would auto-insert that.

**Sara Randall:** In terms of how that previews, I'd be curious to know.

**Sara Randall:** Let's see how that previews.

**Sara Randall:** It's the same.

**Sulaman Ahmed:** I think they have the styling option, and worst case scenario, the customized style option would work exactly like the HTML code we chose.

**Sulaman Ahmed:** So we can just link through CSS classes to make it look good, but obviously got the point.

**Sara Randall:** And then it should adapt to the style sheet, I think, whatever you...

**Sara Randall:** I'll leave it in there if it's helpful.

**Sara Randall:** Awesome.

**Sara Randall:** Well, let me know.

**Sara Randall:** Any other questions or is this all pretty straightforward, the one to punch you?

**Sulaman Ahmed:** I think this is pretty straightforward.

**Sulaman Ahmed:** Just to refresh the crux of this one, we will use blog resources, not the simple blogs, and then we have a dedicated author.

**Sulaman Ahmed:** We don't want a loop between different authors, we will use one dedicated author.

**Sulaman Ahmed:** Then we have a pattern in the pictures and one specific structure like light on the top and on the bottom left.

**Sulaman Ahmed:** So we will use that in the same sequence.

**Sulaman Ahmed:** And then we have view and if needed, we can use the custom tables and things like that.

**Sulaman Ahmed:** think it's pretty clear.

**Sulaman Ahmed:** And lastly, after publishing them, we again add that article to the articles database.

**Sulaman Ahmed:** So it seems pretty clear for now.

**Sara Randall:** Awesome.

**Sara Randall:** Very good.

**Sara Randall:** Thank you.

**Sara Randall:** you.

**Sara Randall:** you.

**Sara Randall:** Thank

**Sara Randall:** Great.

**Sara Randall:** Well, thank you guys so much for taking the time to go through our process, and I'm happy to enable you guys to do this and to support Yazina in this program.

**Sara Randall:** Just so that you're aware, I will be here through to the end of the week if any other, like, you're like, oh, geez, we just got phones there, but I have a quick follow-up question.

**Sara Randall:** You're all the way through Friday, and then I'm out of office for the holiday, traveling to Buffalo with my family.

**Sara Randall:** So if you do need support, that doesn't mean that, you know, just because I'm not here doesn't mean the world isn't it.

**Sara Randall:** So I'm sure Yazina could help, or, you know, the knowledge base in HubSpot is actually pretty helpful, too, in case you're just like, it's just like a brick and mortar, like, how does HubSpot blog, ABCD?

**Sara Randall:** Very content-rich knowledge base there, in case it's more like a, less about the way, the custom way that we do it, which is what we walked through today, and more of just like, how does HubSpot work?

**Sara Randall:** That's helpful to know.

**Sara Randall:** Perfect.

**Sara Randall:** Thank you so much.

**Sara Randall:** Yeah, of course.

**Sulaman Ahmed:** Anything, Erik, you would like to ask?

**Erik O'Brien:** No, I think it's all covered.

**Erik O'Brien:** So very much appreciate it, Sara.

**Erik O'Brien:** Yeah, no worries.

**Sara Randall:** I'm going to stop sharing.

**Sara Randall:** It's been a while since I've done Teams, so I'm like, sometimes I hang up on the call and I stop sharing.

**Sara Randall:** Like, didn't want to just cut up a book.

**Sara Randall:** But thank you both, and I hope you have a good rest of your day.

**Sara Randall:** Thank you so much, Sara.

**Sara Randall:** Have a nice day.

**Sara Randall:** Have a nice day.

**Sara Randall:** Bye.

**Sara Randall:** Bye now.
