# GrowthX CMS walkthrough

<metadata>
date: 2026-02-03
time: 15:30 UTC
duration: 27 minutes
organizer: william@growthx.ai
participants: William Leborgne, Kathy Lam, Reza H. Javanian, Isabelle Watson
fathom_recording_id: 119294080
fathom_url: https://fathom.video/calls/552827024
share_url: https://fathom.video/share/8ajsNTpnoab1ZsRJieCK-dCAUz7hxyJz
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Reza from Talon.One walked William and Kathy through the Storyblok CMS for managing Talon.One's blog content, covering the complete workflow from post creation (via duplication to preserve layout) through SEO configuration. Key decision: GrowthX will use hyperlinked text for CTAs instead of dedicated buttons, and every post must include a sticky card with a gated report. Reza committed to sending an author-mapping guide.

---

## Context

William and Kathy are building out Talon.One's content operations at GrowthX, a B2B content marketing firm. Reza runs content for Talon.One and needed to train GrowthX on how to use Storyblok, the CMS powering Talon.One's blog and website. This was a practical walkthrough session designed to get the team up to speed on the specific workflow, content blocks, and configuration requirements for blog publishing.

---

## Relevance

**Content Operations & CMS**
- GrowthX must always duplicate existing blog posts instead of creating from scratch to preserve the Global Riff layout automatically.
- Blog posts require manual configuration of: author (based on content type: Reza/Isabelle for top-of-funnel, others for product-led), published date, primary category (Marketing or Development), and related categories (Loyalty, Promotions, etc.).
- SEO configuration is manual for every post: meta title format `[Topic] - Talon.One`, canonical URL (full post URL), OG image (same as main card image), index/follow set to true.

**Content Formatting & Blocks**
- Use specific content blocks: `gray box` for highlighting (set spacing to XS), `quote page` to embed pre-created customer/partner quotes (searchable by topic in quotes folder), `image with description` for in-article images (with source URL opening in new tab).
- CTAs are not available as dedicated buttons; use hyperlinked text instead, optionally within a gray box for emphasis.

**Sticky Cards & Lead Gen**
- Every published blog post requires a sticky card (fixed sidebar on right) promoting a gated report.
- Sticky card requires: report title (headline), cover mockup image, and link to download page.

**Next Immediate Steps**
- Reza to provide author-mapping list showing which Talon.One team member (CPO, CTO, etc.) should be attributed to which content types.
- Reza to clarify the Global Riff layout requirement with Talon.One's agency and share guidance with William and Kathy.
- Kathy to update editor instructions to emphasize no CTA buttons and hyperlinked text approach.

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
- Send author-mapping list to William + Kathy
- Ask agency in chat re: 'Global Riff' layout; share guidance w/ William + Kathy

**Kathy Lam (GrowthX)**
- Update editor instructions: no CTA buttons; use hyperlinked text (optional gray box)

---

## Transcript
**Reza H. Javanian:** Nice.

**Reza H. Javanian:** Is it just you?

**Reza H. Javanian:** Yeah, it's me.

**Reza H. Javanian:** From your side, is Kathy joining?

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

**Reza H. Javanian:** For the sake of this walkthrough, let's create a new one. We'll call it "test" and then create. Okay, so to create everything from scratch, I would say the simplest thing is to duplicate a previous story. But if you want to do everything from scratch, you'd set the title here, which is the title of the blog post.

**Reza H. Javanian:** You can select the author from here, so we have a list of authors here that you can select from, myself, for example.

**William Leborgne:** Is there a logic to the authors in terms of what the subject is, or the content that we're going to be creating? Are you okay with just using a single author? What are you thinking?

**Reza H. Javanian:** I'd say, if it is more business on top of the funnel, me or Isabel, if it is more product-led, we can choose.

**Reza H. Javanian:** These are, for example, CPO or CTO are one of our product persons, but I can give you a list on that.

**William Leborgne:** Yeah, that'd be great. If you just give us a list of which authors you want to use in which circumstances, that'll make it really easy. Hey, Kathy, welcome.

**Kathy Lam:** Hey, no worries about joining late.

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

**Reza H. Javanian:** So back to this one. Now I want to show you how to hyperlink something. You just select the text, go to link, and then use the page here that you want to link to.

**Reza H. Javanian:** So, for example, I want to link to one of our product pages, for instance, or one of our blogs, this one, for example.

**Reza H. Javanian:** You use this, and then please activate this so that it opens in a new tab. And then you're done.

**William Leborgne:** Okay. So when you do the dropdown, it's got internal link, email, URL, asset, right? Let me just clarify one thing.

**William Leborgne:** If the editor wants to link to a product page, is it okay if they select URL and put the entire URL?

**Reza H. Javanian:** Exactly. That's what I always do.

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

**Kathy Lam:** Quick question about the CTA. Can we modify the CTA sometimes so that it's either a demo or something else?

**Reza H. Javanian:** Yeah, definitely. Hold on, this is not the CTA I'm talking about. This is the CTA on the card on the blog listing page.

**William Leborgne:** So there's a separate CTA for inside the blog itself?

**Reza H. Javanian:** Exactly. It's this "read more" here on the card.

**Reza H. Javanian:** I don't know why, but they have removed the CTA option from here in the new version, so you don't need to worry about it.

**Kathy Lam:** One more question: is there a special option to feature a blog at the top versus the others at the bottom?

**Reza H. Javanian:** You mean moving it like up here? Yes, we can do that. It's like moving the slugs when you want to move something up. I'll make sure to clarify that.

**Kathy Lam:** Got it.

**Reza H. Javanian:** So is CTA here?

**Reza H. Javanian:** Again, I don't know why it doesn't appear on the website, but developers or whatever else you put for personal.

**Reza H. Javanian:** And for main cart image, you click on it, and we have a list of files.

**Reza H. Javanian:** It's here.

**Reza H. Javanian:** If you want to use something pre-existing from our depository, can use, or if you want to upload something, you can upload files.

**Reza H. Javanian:** Let me do that.

**Reza H. Javanian:** You can upload files and whatever.

**Reza H. Javanian:** Let me select this one.

**Reza H. Javanian:** When you want to use it, you have to fill in advanced options: title, caption, and description for the image. Something like "Loyalty Promotion" or whatever the topic is. Then we save and upload it. Once it's uploaded, you click on it and it appears and you can use it for the main image. Or if you want to use something pre-existing, you can search for it. For example, if you need something for loyalty, you type "loyalty" and we have a lot of loyalty images here you can select from.

**Reza H. Javanian:** Okay, that's it.

**Reza H. Javanian:** We don't need anything else here, so let's go to the SEO part.

**Reza H. Javanian:** For the SEO part, we use whatever topic it is for the meta title, and then at the end, we put "Talon.One". Then set the meta description. For index, we always put it on index. For follow, we put it on follow. For canonical, you need to provide the link to the same post you're creating. So if we're creating this test post, you use that same name for the canonical. And for image OG, use the same image you selected for the main card image.

**William Leborgne:** So the structured data section is above the canonical?

**Reza H. Javanian:** Yes, the section right above canonical is structured data.

**William Leborgne:** Structure data, I mean?

**Reza H. Javanian:** Yeah, is this where the schema markup goes?

**Reza H. Javanian:** Yeah, exactly.

**Reza H. Javanian:** Yeah, yeah.

**Reza H. Javanian:** Okay.

**William Leborgne:** So you guys do not have schema?

**Reza H. Javanian:** No.

**Reza H. Javanian:** Oh, I see.

**Kathy Lam:** Okay.

**William Leborgne:** Actually, we most likely do want to include schema because it's preferred by LLMs, but it's good just to know where to put it.

**Reza H. Javanian:** Okay. So that's the SEO section with canonical, image OG, all of that. Now let me show you the sticky card. This is what we mean by a sticky card—this sidebar on the right.

**William Leborgne:** Got it, the one on the right side.

**Reza H. Javanian:** So back to this one.

**Reza H. Javanian:** So add block, sticky card, headline.

**Reza H. Javanian:** So headline is, for example, loyalty strategies for 2026.

**Reza H. Javanian:** And I'm assuming you always want one on the right.

**William Leborgne:** Like any blog that we publish, we should have a sticky card on the right.

**William Leborgne:** Yes, exactly.

**Reza H. Javanian:** Yeah, okay.

**Reza H. Javanian:** Then for the image, we use the cover mockup for the report. For example, if it's "Loyalty Strategies for 2026", we use that report's cover mockup. We set text alignment to center, and then create a link to the report download page.

**Reza H. Javanian:** The name of the author, the image, and this was the gray box, it's not that gray, but it was the gray box that we talked about, and all the H2s, for example, and this is the codes that we use from the code page, the hyperlink, and once you click on it, it opens in a new page, and yeah, think that's, we have created the sticky card here.

**Reza H. Javanian:** Yes, that's it.

**William Leborgne:** Okay, great.

**William Leborgne:** That's it.

**William Leborgne:** Can you go back to the article view? That way we can stage all the content first, and you can review it before publishing.

**Reza H. Javanian:** Got it.

**Kathy Lam:** One question: if we're doing content updates versus new posts, does this change at all? Like, we go into a current post and make changes?

**Reza H. Javanian:** Yeah, you can just go in there and save it. So now we're out of the new post editor. This is our blog with all the blog articles. Let me show you editing an existing post. The layout should be Global Riff. That's the layout we always use because I always duplicate existing posts.

**William Leborgne:** It might be worth asking your agency to explain the Global Riff layout requirement.

**Reza H. Javanian:** Yeah, I'll do that in the chat.

**Reza H. Javanian:** Okay.

**Reza H. Javanian:** Okay, so we're now in this blog, which is already live. Whatever changes you want to make, you just do it and then save. Now let me show you the image with description block, which we'll probably need to use often.

**Reza H. Javanian:** If you want to use images inside the blog, you add a block called "image with description". It includes the image itself (either uploaded or pre-existing), a description for the image, and a source URL. You can select URL and paste the link, and make sure to set it to open in a new tab. That's how we use images in the article blocks.

**William Leborgne:** About CTAs within the article—do you have a dedicated button block for CTAs, like "book demo" or "read more"?

**Reza H. Javanian:** No, we don't have dedicated CTA buttons. We don't use buttons like that. Instead, we write the text and create a hyperlink. If you want to highlight it, you can put it in a gray box, but it's always just hyperlinked text, not a button.

**William Leborgne:** Got it, so just hyperlinked text.

**Reza H. Javanian:** Okay, you just hyperlink.

**William Leborgne:** That's good to know. We need to make sure to include that in our instructions to the editor.

**Kathy Lam:** I'll update the editor instructions to reflect that.

**Reza H. Javanian:** Let me scroll down to see if there's anything I've missed. You can see here how we use a gray box for CTAs. That's the pattern—you put the CTA text in a gray box and hyperlink it.

**William Leborgne:** Perfect, I got it. Thank you so much, I really appreciate your time.

**Reza H. Javanian:** Yeah, thank you so much. I'm sure you guys are experts, but if you have any questions, feel free to ask.

**William Leborgne:** I appreciate it. Thanks so much.

**Kathy Lam:** Thank you. Have a great rest of your day.
