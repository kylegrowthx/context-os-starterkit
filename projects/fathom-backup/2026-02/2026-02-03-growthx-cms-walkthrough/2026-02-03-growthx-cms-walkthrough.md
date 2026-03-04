# GrowthX CMS walkthrough

<metadata>
date: 2026-02-03
time: 15:30 UTC
duration: 27 minutes
organizer: william@growthx.ai
participants: Reza H. Javanian, William Leborgne, Kathy Lam
fathom_recording_id: 119294080
fathom_url: https://fathom.video/calls/552827024
share_url: https://fathom.video/share/8ajsNTpnoab1ZsRJieCK-dCAUz7hxyJz
source: fathom
enriched_on: 2026-02-27 00:45 UTC
</metadata>

---

## Summary

Reza (Talon.One) walked William and Kathy (GrowthX) through Storyblok workflows for publishing blog posts: duplicating existing posts to preserve layout, using content blocks (gray box, quote page, image with description), and configuring SEO metadata. Key decision: CTAs use hyperlinked text only—no button components available. Next step: Reza will provide an author-mapping guide and clarify the "Global Riff" layout with the agency.

---

## Context

GrowthX is managing blog content production for Talon.One via Storyblok CMS. William Leborgne and Kathy Lam lead editorial at GrowthX; Reza Javanian (Talon.One's CMO/product leader) owns the technical setup. This walkthrough standardizes the workflow so GrowthX editors can publish independently without blocking on technical questions. The discussion surfaced operational decisions (duplicate-don't-create, hyperlinked CTAs over buttons) and gaps (author selection logic, layout template clarification) that need documentation before scaling output.

---

## Relevance

**GrowthX Delivery**
- Blog publishing workflow for Talon.One engagement—directly impacts editorial cadence and turnaround time.
- Author-selection logic needed from Reza to avoid blocking Kathy's editor instructions.
- Hyperlinked CTAs (not buttons) must be communicated to writers and editors to prevent rework.
- Sticky card requirement (always-on right sidebar) needs to be documented as a mandatory step.

**CheckThat / AI Content Strategy**
- SEO metadata section currently lacks structured data / schema markup—opportunity to improve AI discoverability (mentioned in discussion).
- Canonical URL and OG image configuration will improve content performance in AI indexing.

---

## Overview

- **Workflow:** Duplicate existing posts to preserve the correct layout (`Global Riff`) and save time.
- **Content:** Use specific blocks for quotes (`quote page`), highlighted text (`gray box`), and images (`image with description`).
- **SEO:** Manually configure each post's SEO, including a self-referential canonical URL and the main card image for the OG image.
- **CTAs:** Use hyperlinked text, optionally within a `gray box` for emphasis; dedicated CTA buttons are not available.

---

## Key Topics

### Workflow & Setup

  - **Duplication:** Always duplicate an existing post.
      - **Why:** This preserves the correct layout (`Global Riff`), which is not applied when creating from scratch.
  - **General Fields:**
      - **Author:** Select based on content type (e.g., Reza/Isabel for top-of-funnel). Reza will provide a full author list.
      - **Published At:** Set manually; the time field is for internal reference only.
      - **Categories:** Use for internal sorting; not visible on the website.
          - **Primary:** `Marketing` or `Development`
          - **Related:** `Loyalty`, `Promotions`, etc.

### Content Formatting & Blocks

  - **Headings:** Use the rich text editor to apply H1, H2, and H3 tags.
  - **Gray Box:** For highlighting text (e.g., CTAs).
      - **Path:** `Add block` → `gray box` → `rich text`
      - **Spacing:** Set to `XS` to prevent excessive vertical space.
  - **Quote Page:** Embeds pre-created quotes.
      - **Path:** `Add block` → `quote page`
      - **Source:** Quotes are stored in the `quotes` folder. Search by topic (e.g., "Omnichannel") to find relevant options.
      - **Creation:** New quotes require a logo, quote text, headshot, name, position, and company.
  - **Image with Description:** For images within the article body.
      - **Path:** `Add block` → `image with description`
      - **Fields:** Image file, description, and source URL (must open in a new tab).

### SEO & Sticky Card

  - **SEO Section:**
      - [**Meta Title:** `[Topic] - Talon.One`](https://fathom.video/share/8ajsNTpnoab1ZsRJieCK-dCAUz7hxyJz?tab=summary&timestamp=964.0)
      - **Index/Follow:** Always set to `index` and `follow`.
      - **Structured Data:** Currently unused. GrowthX may add schema markup to improve LLM compatibility.
      - **Canonical:** The full URL of the post itself.
      - **Image OG:** The same image used for the main card.
  - **Sticky Card:** The fixed sidebar on the right.
      - **Requirement:** Every post must include one.
      - **Path:** `Add block` → `sticky card`
      - **Content:** Typically promotes a gated report.
          - **Headline:** Report title
          - **Image:** Report cover mockup
          - **Link:** URL to the report's download page

---

## Action Items

**Reza H. Javanian (Talon.One)**
- Send author-mapping list to William + Kathy (logic for picking authors by content type).
- Ask agency in chat about 'Global Riff' layout behavior when duplicating vs. creating from scratch; share findings with William + Kathy.

**Kathy Lam (GrowthX)**
- Update editor instructions: Storyblok has no CTA buttons—use hyperlinked text only (optionally wrapped in gray box for emphasis).

---

## Transcript
**Reza H. Javanian:** Nice.

**Reza H. Javanian:** Is it just you?

**Reza H. Javanian:** Yeah, it's me.

**Reza H. Javanian:** From your side, is Cathy joining?

**William Leborgne:** No, we can go ahead and jump right in.

**William Leborgne:** Honestly, this should be very fast.

**William Leborgne:** Exactly.

**Reza H. Javanian:** I don't think it takes more than 10 minutes.

**Reza H. Javanian:** Working with StoryBlock is pretty straightforward, I would say.

**Reza H. Javanian:** Let me share my screen.

**Reza H. Javanian:** So, can I see my screen?

**William Leborgne:** Yes.

**William Leborgne:** Yes.

**William Leborgne:** Okay.

**Reza H. Javanian:** So, once you are in StoryBlock in this environment, so this is blogging, let go one step back.

**Reza H. Javanian:** So, once you click on content, you will be in this environment here.

**Reza H. Javanian:** And so, I think the two...

**Reza H. Javanian:** folders that you will need are blog and glossary, mostly blog and sometimes glossary.

**Reza H. Javanian:** But you can see everything else here as well, which is all the content on our website.

**Reza H. Javanian:** So for example, this folder has all our product pages, all the incentivized, which is our flagship summits.

**Reza H. Javanian:** All the incentivized pages are created in this folder, mockups, login, all the thank you pages, for example.

**Reza H. Javanian:** So different folders for different parts of the website, events, and everything else.

**Reza H. Javanian:** So think I, yeah, it must be here, yes.

**Reza H. Javanian:** So also we have download here, which is a folder for our reports, our gated contents.

**Reza H. Javanian:** We put them all here, and this is our blog folder.

**Reza H. Javanian:** So once you go into the blog, you have this create new.

**Reza H. Javanian:** you.

**William Leborgne:** This here.

**Reza H. Javanian:** Honestly, I never use this create new.

**Reza H. Javanian:** always use one of the duplicate logs and duplicate it and then I change the name and everything.

**Reza H. Javanian:** So once you change the name, this log would automatically change as well.

**Reza H. Javanian:** And then you duplicate it.

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**Reza H. Javanian:** So let's, uh, but for the sake of this, uh, one, let's create a new one.

**Reza H. Javanian:** And so we create a new story and let's call it test, test, test, test, test.

**Reza H. Javanian:** Uh, sorry.

**Reza H. Javanian:** Oh, my laptop, sorry.

**Reza H. Javanian:** We won't fix this problem.

**Reza H. Javanian:** Uh, and create.

**Reza H. Javanian:** Okay.

**Reza H. Javanian:** So, uh, now we are into that, uh, slog.

**Reza H. Javanian:** And.

**Reza H. Javanian:** Okay, so to create everything from scratch, would say, but again, I say, but the simplest thing is to duplicate a previous story, but to do everything from scratch, we need the time to read, so you can do it five minutes or whatever, title, whatever it is, the title goes here, the title of the blog post.

**Reza H. Javanian:** You can select the author from here, so we have a list of authors here that you can select from, myself, for example.

**William Leborgne:** there a logic to the authors in terms of what the subject is, or the content that we're going to be creating, you're okay with just using a single author?

**William Leborgne:** What are you thinking?

**Reza H. Javanian:** I'd say, if it is more business on top of the funnel, me or Isabel, if it is more product-led, we can choose.

**Reza H. Javanian:** These are, for example, CPO or CTO are one of our product persons, but I can give you a list on that.

**Reza H. Javanian:** Yeah, that'd be great.

**William Leborgne:** If you just give us a list of which authors you want to use in which circumstances, that'll make it really easy.

**William Leborgne:** Hey, Kathy.

**William Leborgne:** Hi, my apologies.

**Kathy Lam:** Hey.

**Kathy Lam:** No worries.

**William Leborgne:** Of course.

**William Leborgne:** worries.

**William Leborgne:** worries.

**Reza H. Javanian:** So, yeah, as I was saying, so now we are in the StoryBlock environment block, and we are creating the block.

**Reza H. Javanian:** So we started with setting the time, so you can basically set any time that you think makes sense.

**Reza H. Javanian:** Title here, and then author, published at, and this is something that we need to do manually as well.

**Reza H. Javanian:** So, let's say it's today, and for time, it doesn't, it doesn't matter what you select here.

**Reza H. Javanian:** It doesn't show up on the website.

**Reza H. Javanian:** So, this is time, and then for category.

**Reza H. Javanian:** Category, if it is marketing, development, or research and development focused, so to make your life easier, if it is more business and marketing, let's select marketing.

**Reza H. Javanian:** If it is more tech, let's select development.

**William Leborgne:** Got it.

**Reza H. Javanian:** And related category, again, so it's very clear.

**Reza H. Javanian:** If it is more into loyalty, you choose loyalty.

**Reza H. Javanian:** If it is more promotions, promotions or both.

**Reza H. Javanian:** So again, it doesn't show up on the website.

**Reza H. Javanian:** And then here we have the text.

**Reza H. Javanian:** So we paste the text here from our docs.

**Reza H. Javanian:** And here you can select different options here.

**Reza H. Javanian:** If it is a normal text, or if you want this to be H1, or if you want this to be H2, H3, or others.

**Reza H. Javanian:** So you can select it, you select it right here.

**Reza H. Javanian:** And so now we have, for example, this.

**Reza H. Javanian:** Heading H2, and then you want to start with this, whatever, and then, but you want to use, sometimes in order to highlight, especially if it is like the beginning of the text, or if you did the CTA, or sometimes important points that we want to highlight in a box or something, we use gray box option, and that you use a block from here, add block, and then when you add block, you just like, gray box, gray box, and then you click on it, add block, rich text, and then in the rich text, you write your copy, so, something like this, and then, for spacing, we always set it on XS, because if you don't, the space between the text on the upper and down, the bottom box will be, too much.

**Reza H. Javanian:** So, XS is the size, and now we have a gray box.

**Reza H. Javanian:** Yeah, of course, we will see it again.

**Reza H. Javanian:** But, yeah, but this gray box will be something that we want to highlight in the text.

**William Leborgne:** Normally, when you click on save, you should see it on the left, I'm assuming.

**William Leborgne:** Yes, exactly.

**William Leborgne:** Yeah, exactly.

**Reza H. Javanian:** You will see it for a minute.

**Reza H. Javanian:** So, again, we have H2, and then I just want to show you different features that we use in the blog.

**Reza H. Javanian:** something that's also we use quite often is a quote within the text, whether from our partner or customer or one of our own people, for example, our CEO, our CTO, et cetera.

**Reza H. Javanian:** Again, for this, you go to add a blog, and then you write quote page.

**Reza H. Javanian:** You select quote page.

**Reza H. Javanian:** And when you click on it, you can choose a code from all of the codes previously created in StoryBlog.

**Reza H. Javanian:** All the codes are in another folder in StoryBlog you can select from.

**Reza H. Javanian:** If you want to create a new one, I will show you later how to do it in the folder.

**Reza H. Javanian:** But let's say we want to select this code from Sydney Segal Working at Build and then color is fine.

**Reza H. Javanian:** Whatever that is.

**Reza H. Javanian:** So now we have a code page here.

**William Leborgne:** Real quickly, because we're not going to know what it doesn't give you the details.

**William Leborgne:** Can you open another tab and just show me how we look at those quotes?

**William Leborgne:** Of course.

**Reza H. Javanian:** Yep.

**Reza H. Javanian:** So let's go to this one.

**Reza H. Javanian:** So we have.

**Reza H. Javanian:** So folder for quotes, so we have this folder for quotes, all of them are here, and then, so you see all the quotes here, so let's go to one of them, for example, this one from Panera, so once you're there, these are the assets that you need, you need a logo for that, a quote itself, headshots of the person, their name, their position, and their company, so the company, so once you have all of them, you click on Save and Publish, then it is published, and then you can go, if you want to use this one in the blog, you'd select it in the, in the, in quote page that I, I don't want to imagine that we'll be adding many quotes, but I think it's a possibility that the writer, the, the, our editor, will look at quotes that exist, that you guys already have.

**William Leborgne:** And so being able to go to it and then go find the quote and read it is helpful.

**Reza H. Javanian:** Yeah, it makes a lot of sense because, yeah, I think it's easy to find because most of the codes, we've tried to use them, the topic in the name of the slug here.

**Reza H. Javanian:** So, for example, if you search Omnichannel, you will probably find quotes about Omnichannel here.

**William Leborgne:** Oh, okay.

**William Leborgne:** Yeah, so.

**William Leborgne:** That makes it easier.

**Reza H. Javanian:** Exactly, so you don't need to, or if you, I don't know, use it, I don't know, for integration maybe or something.

**Reza H. Javanian:** Yeah, you see, like, internet, you find quotes about integration and then you can select them.

**Reza H. Javanian:** So it makes it a lot easier.

**William Leborgne:** Yeah, that's a lot easier.

**William Leborgne:** Okay, great.

**William Leborgne:** Super.

**William Leborgne:** Cool.

**Reza H. Javanian:** So back to this one.

**Reza H. Javanian:** So we also use the code page.

**Reza H. Javanian:** We used, yeah.

**Reza H. Javanian:** Yeah, so now we need to...

**Reza H. Javanian:** to...

**Reza H. Javanian:** to...

**Reza H. Javanian:** So in order to hyperlink something, you just select them from here, from here, from link, you use link, and then you use the page here that you want to link to.

**Reza H. Javanian:** So, for example, I want to link to one of our product pages, for instance, or one of our blogs, this one, for example.

**Reza H. Javanian:** So you use this, and then please activate this so that it opens in a new time.

**William Leborgne:** Okay.

**Reza H. Javanian:** And then you're done, and then we created this one.

**Reza H. Javanian:** Sorry, go back to the link real quickly.

**Reza H. Javanian:** This one?

**William Leborgne:** You know, yeah, so here, when you do the dropdown, it's got internal link, email.

**William Leborgne:** URL, asset, right?

**William Leborgne:** Yeah.

**William Leborgne:** Let me just clarify one thing.

**William Leborgne:** If the editor wants to link to a product page, to an existing product page, is it okay if they select URL and put the entire URL?

**William Leborgne:** Exactly.

**Reza H. Javanian:** That's what I always do.

**Reza H. Javanian:** I select URL and then I paste the URL here.

**William Leborgne:** I just want to clarify because I have done this with other CMSs where they're like, you have to find the internal link and it's going to take too much time.

**Reza H. Javanian:** No, you can use it from our website and then paste it here.

**William Leborgne:** Okay, super.

**Reza H. Javanian:** any other thing, any other website that you want.

**Reza H. Javanian:** Okay, so hyperlink here, and then codes, gray box, I think that's on H1, H2, H3.

**Reza H. Javanian:** Okay, let's go ahead and then we'll come back.

**Reza H. Javanian:** So card headline is the same as the title that we use for the piece.

**Reza H. Javanian:** It's the same one.

**Reza H. Javanian:** It's what appears in the hub, in the blog hub, the intro here.

**Reza H. Javanian:** For the blog post, CTA is always read more, and persona, you can select if it is like for developer or for marketer.

**Kathy Lam:** question about the CTA.

**Kathy Lam:** Can we modify the CTA sometimes so that it's either a demo or something else?

**Kathy Lam:** Definitely.

**Reza H. Javanian:** Yeah, definitely.

**Reza H. Javanian:** Hold on, this is not the CTA.

**William Leborgne:** I think this is the CTA of the little, like on the blog page.

**William Leborgne:** On the card.

**William Leborgne:** Oh, on the card.

**Kathy Lam:** On the card.

**William Leborgne:** Yeah, exactly.

**William Leborgne:** The CTA for the blog.

**William Leborgne:** For that blog, yeah.

**William Leborgne:** So I think there's a separate CTA for inside the blog.

**William Leborgne:** Exactly.

**William Leborgne:** Exactly.

**William Leborgne:** Okay.

**Reza H. Javanian:** So this is, it's this one.

**Reza H. Javanian:** It's this read more here.

**Reza H. Javanian:** Yep.

**Kathy Lam:** Okay.

**Kathy Lam:** It's this one, on the cart.

**Reza H. Javanian:** And I don't know why, but we don't have it even here.

**Reza H. Javanian:** I'm not sure why.

**Reza H. Javanian:** We used to have it, but maybe in the new, yeah, they have removed it from here, so you don't need to worry about it at all.

**Kathy Lam:** While you're here, is there a special option for it to be like the featured blog versus one of the blogs on the bottom?

**Reza H. Javanian:** You mean moving it like up here?

**Reza H. Javanian:** Yes.

**Kathy Lam:** Yes.

**Kathy Lam:** I will show you how.

**Reza H. Javanian:** Yeah.

**Reza H. Javanian:** Yeah.

**Reza H. Javanian:** It's, again, it's like by moving the slugs when you get up, but I'll be sure.

**Reza H. Javanian:** Yeah, we can do that.

**Kathy Lam:** Got it.

**Reza H. Javanian:** So is CTA here?

**Reza H. Javanian:** Again, I don't know why it doesn't appear on the website, but developers or whatever else you put for personal.

**Reza H. Javanian:** And for main cart image, you click on it, and we have a list of files.

**Reza H. Javanian:** It's here.

**Reza H. Javanian:** If you want to use something pre-existing from our depository, can use, or if you want to upload something, you can upload files.

**Reza H. Javanian:** Let me do that.

**Reza H. Javanian:** You can upload files and whatever.

**Reza H. Javanian:** Let me select this one.

**Reza H. Javanian:** Just when you want to use it, you have to fill something for advanced options, title, caption, and a title, whatever the topic is.

**Reza H. Javanian:** Loyalty Promotion is something, something general, something very generic.

**Reza H. Javanian:** And then we save it and upload it.

**Reza H. Javanian:** And it's uploaded here.

**Reza H. Javanian:** And then we click on it and it appears on here and you can use it for main image.

**Reza H. Javanian:** Super.

**Reza H. Javanian:** Or if you want to use something pre-existing, so for example, you need something for, let's say, loyalty.

**Reza H. Javanian:** You type loyalty and then we have a lot of loyalty images here.

**Reza H. Javanian:** And so you can, you can select one of them.

**Reza H. Javanian:** Okay, that's it.

**Reza H. Javanian:** We don't need anything else here, so let's go to the SEO part.

**Reza H. Javanian:** For the SEO part, we use whatever that you want, whatever the topic is, we use this for meta title, and then at the end of all of them, we put Talon.One.

**Reza H. Javanian:** This is what we do.

**Reza H. Javanian:** But yeah, this is like the way we do it, and then something for meta description.

**Reza H. Javanian:** For index, we always put it on index.

**Reza H. Javanian:** For follow, we put it on follow.

**Reza H. Javanian:** Structured data, nothing from our side.

**Reza H. Javanian:** For canonical, you need to provide the link to the same block that you're creating.

**Reza H. Javanian:** So here we are creating test, test, test, test, yeah.

**Reza H. Javanian:** Yeah, it's here.

**Reza H. Javanian:** So you use the same name, and then you use it for canonical.

**Reza H. Javanian:** And for image OG, the same image that you selected for main part.

**Reza H. Javanian:** Okay.

**William Leborgne:** So I think it was this one.

**Reza H. Javanian:** The section above, above canonical.

**William Leborgne:** Structure data, I mean?

**Reza H. Javanian:** Yeah, is this where the schema markup goes?

**Reza H. Javanian:** Yeah, exactly.

**Reza H. Javanian:** Yeah, yeah.

**Reza H. Javanian:** Okay.

**William Leborgne:** So you guys do not have schema?

**Reza H. Javanian:** No.

**Reza H. Javanian:** Oh, I see.

**Kathy Lam:** Okay.

**William Leborgne:** No, it is We most likely do want to include schema because it's preferred by LLMs, but it's good just to know where to put it.

**Kathy Lam:** Okay.

**Kathy Lam:** Yeah.

**Kathy Lam:** Okay.

**Reza H. Javanian:** Okay.

**Reza H. Javanian:** Canonical, image OG.

**Reza H. Javanian:** this is the civil part.

**Reza H. Javanian:** And then for a sticky card, so this is what we mean by, let me share this.

**Reza H. Javanian:** This is what we mean by a sticky card.

**Reza H. Javanian:** This one on the right.

**William Leborgne:** Okay, got it.

**William Leborgne:** This one on the right.

**Reza H. Javanian:** So back to this one.

**Reza H. Javanian:** So add block, sticky card, headline.

**Reza H. Javanian:** So headline is, for example, loyalty strategies for 2026.

**Reza H. Javanian:** And I'm assuming you always want one on the right.

**William Leborgne:** Like any blog that we publish, we should have a sticky card on the right.

**William Leborgne:** Yes, exactly.

**Reza H. Javanian:** Yeah, okay.

**Reza H. Javanian:** And then for image, for example, now I'm using this loyalty strategies for 2026.

**Reza H. Javanian:** We always have this here.

**Reza H. Javanian:** We have a cover mockup for that.

**Reza H. Javanian:** So this is the cover mockup for this one.

**Reza H. Javanian:** We use the cover mockup for that report.

**Reza H. Javanian:** Text alignment center.

**Reza H. Javanian:** Content nothing.

**Reza H. Javanian:** Link.

**Reza H. Javanian:** commons for 6026.

**Reza H. Javanian:** We create a link to that one.

**Reza H. Javanian:** The name of the author, the image, and this was the gray box, it's not that gray, but it was the gray box that we talked about, and all the H2s, for example, and this is the codes that we use from the code page, the hyperlink, and once you click on it, it opens in a new page, and yeah, think that's, we have created the sticky card here.

**Reza H. Javanian:** Yes, that's it.

**William Leborgne:** Okay, great.

**William Leborgne:** That's it.

**William Leborgne:** Do you mind going back to the very, to the article, just the regular view?

**Reza H. Javanian:** Sorry, that first view where you're putting in the content, I think, there we go.

**William Leborgne:** Is this it?

**William Leborgne:** No, no, no, you're still in the sticky card.

**William Leborgne:** Can you just click back on article?

**William Leborgne:** Sure.

**William Leborgne:** And go to general?

**Reza H. Javanian:** on the article general, okay.

**Reza H. Javanian:** Okay, so this, this, no, no, sorry, go back up.

**William Leborgne:** I mean, that'll just allow us to move a little more quickly, because then we can stage all the content, and then when you have time, you can do a quick review and then publish.

**Reza H. Javanian:** Exactly.

**Reza H. Javanian:** Super.

**Reza H. Javanian:** I have one question.

**Kathy Lam:** If we're doing any content updates versus new posts, does this change at all?

**Kathy Lam:** Like, we go into a current post, and then we make changes?

**Reza H. Javanian:** Yeah, you can go there, and then you can save it.

**Reza H. Javanian:** Let me do that for you.

**Reza H. Javanian:** So, now we are out of this one.

**Reza H. Javanian:** So, this is our blog, all the blog articles here.

**Kathy Lam:** So, let's, for example, let's go to this one.

**Reza H. Javanian:** Oh, it's in the layout is Global Riff.

**Reza H. Javanian:** Sorry.

**Reza H. Javanian:** It's something here.

**Reza H. Javanian:** I said that we don't use it, but that's because I always duplicate things, so it's duplicated.

**William Leborgne:** I mean, it might be worth asking your agency, just explain.

**William Leborgne:** Yeah, yeah, I will do this.

**Reza H. Javanian:** I will do on the chat.

**Reza H. Javanian:** Okay.

**Reza H. Javanian:** Okay, so we are in this blog, which is already live.

**Reza H. Javanian:** So what, oh, one is image with description.

**Reza H. Javanian:** I forgot this one.

**Reza H. Javanian:** I will talk about this.

**Reza H. Javanian:** So whatever change that you want to make, everything, so you do it and then you can save it.

**Reza H. Javanian:** Okay, got it.

**Kathy Lam:** Yeah.

**Kathy Lam:** Perfect, thanks.

**Kathy Lam:** Of course.

**Kathy Lam:** And yeah, so not good that we are here.

**Reza H. Javanian:** So another thing that we probably will need is image with description.

**Reza H. Javanian:** If you want to use images inside the blog, so again, from this plus sign, we add a blog, and that is called image with description.

**Reza H. Javanian:** And image with description is always an image that you use, you upload or you use a pre-existing image, a description for the image, and also a source.

**Reza H. Javanian:** Okay?

**Reza H. Javanian:** Again, source, can always use, you can select the URL and paste the URL.

**Reza H. Javanian:** And then, again, please use this one so that it opens in a new window.

**Reza H. Javanian:** And that's how we use images on the website, in the blocks.

**Reza H. Javanian:** And I'm assuming adding a CTA within the article is the same thing.

**William Leborgne:** You add a block and you find CTA?

**Reza H. Javanian:** Yes, exactly.

**William Leborgne:** Yeah.

**William Leborgne:** Okay.

**Reza H. Javanian:** If you want to highlight the CTA in a gray box, you just use a gray box and then you type it and create a hyperlink.

**Reza H. Javanian:** It's like that.

**Reza H. Javanian:** you just want to use a CTA without a gray box, you just hyperlink part of the text and then you create a link to whatever.

**William Leborgne:** Oh, no, no.

**William Leborgne:** When I say CTA, I'm not saying hyperlinking.

**William Leborgne:** I'm saying literally a button, a CTA button.

**William Leborgne:** I'm assuming that you have a block for that, like a little...

**William Leborgne:** Can you guys add buttons?

**William Leborgne:** You

**William Leborgne:** No.

**William Leborgne:** You don't have any buttons in your content?

**Reza H. Javanian:** No, like watch more, see more, discover more, these sort of things.

**William Leborgne:** Or yeah, or book demo or read more about this topic and this, et cetera.

**Reza H. Javanian:** No, we don't use this as like with buttons.

**Reza H. Javanian:** We write the text and then we create a hyperlink.

**Reza H. Javanian:** Okay, you just hyperlink.

**William Leborgne:** Okay.

**William Leborgne:** That's good to know.

**William Leborgne:** Okay.

**William Leborgne:** We have to make sure to include that in our instructions to our editor.

**William Leborgne:** Yep.

**Kathy Lam:** I will do that.

**William Leborgne:** Okay.

**Reza H. Javanian:** Just now that you're here, let me just go down a little bit to see if there is anything that I have missed.

**Reza H. Javanian:** Image description, description.

**Reza H. Javanian:** Great box.

**Reza H. Javanian:** No, you see, for example, this is for this CTA, we have used a gray box.

**Reza H. Javanian:** And this is how like we were keen to join for incentive with whatever.

**William Leborgne:** then blah, blah, blah.

**William Leborgne:** then dig right here and create a hyperlink.

**William Leborgne:** That's like your CTA got it.

**William Leborgne:** Okay.

**William Leborgne:** lot.

**William Leborgne:** Yeah.

**William Leborgne:** Thank you.

**William Leborgne:** Okay, great.

**William Leborgne:** Thank you so much.

**William Leborgne:** really appreciate your time.

**Reza H. Javanian:** Yeah, thank you so much.

**Reza H. Javanian:** Of course.

**Reza H. Javanian:** I'm sure that you guys are experts, but if you have any questions, feel free to ask.

**William Leborgne:** I appreciate it.

**William Leborgne:** Thanks so much.

**Kathy Lam:** Thank you.

**Kathy Lam:** Have a good rest of the day.

**Kathy Lam:** Bye-bye.

**Kathy Lam:** Bye.
