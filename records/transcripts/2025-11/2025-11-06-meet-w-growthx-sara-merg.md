# Meet w/ GrowthX (Sara Merg)

<metadata>
date: 2025-11-06
time: 15:01 UTC
duration: 11 minutes
organizer: erik@growthx.ai
participants: Sara Merg, Erik O'Brien
fathom_recording_id: 99699001
fathom_url: https://fathom.video/calls/465885564
share_url: https://fathom.video/share/nXo_ojhJPFdquzsxoybsLyQTVFm6BVvx
source: fathom
enriched_on: 2026-03-02 12:00 UTC
</metadata>

---

## Summary

Onboard growthx.ai to Bubble's Ghost CMS publishing process.

---

## Context

Sara Merg is the publishing operations lead at Bubble, a low-code platform for building web applications. GrowthX has begun a content partnership to draft SEO-focused blog posts for Bubble's blog, which runs on Ghost CMS. Sara conducted a walkthrough of Bubble's Ghost publishing environment to onboard Erik O'Brien's GrowthX publishing team on the technical setup, content formatting standards, and editorial workflow. The meeting established the foundation for GrowthX to begin drafting the first 2-3 SEO articles, with Bubble handling the review and publication step.

---

## Relevance

- **To GrowthX Delivery:** Established clear technical and editorial standards for Bubble's Ghost CMS, including specific tagging rules (primary tag determines homepage placement), table styling preferences (Table Style 2 for versatility), and mandatory alt text for images. This ensures GrowthX's drafts will meet Bubble's formatting requirements before review.
- **To GrowthX Delivery:** Identified a critical Ghost CMS bug (slug reset to title on publish) that the team must monitor before each publication. This operational knowledge prevents broken URLs and maintains SEO integrity.
- **To GrowthX Delivery:** Clarified the author field convention (use "Bubble" for all SEO content) and the importance of updating publish dates on article updates to maintain content freshness signals.
- **To GrowthX Delivery:** UTM parameter tracking requirement for all CTA links — Sara will send the UTM builder format to Erik's team for consistent campaign tracking across SEO content.

---

## Overview

- **Publishing Workflow:** growthx.ai will draft the first 2–3 articles; Bubble will review and publish to ensure correct formatting and process adherence.
- **Tagging is Critical:** The first tag assigned to a post determines its primary category on the blog's homepage.
- **Table Style 2 is Preferred:** Use `Table Style 2` (normal header row) for versatility, as `Table Style 1` (locked left header) can break on wider screens.
- **Key Formatting Rules:** Use the `Callout Box` for CTAs, add simple alt text to all images, and ensure H1/H2s are *not* bolded.

---

## Key Topics

### Publishing Workflow & Review

  - **Process:** growthx.ai drafts → Bubble reviews & publishes.
  - **Rationale:** This initial review ensures correct formatting and validates the onboarding instructions.

### General Post Settings

  - **Author:** Use "Bubble" for all SEO content.
  - **Date Published:** Update the date on any article update to keep content current.
  - **Slug:** Double-check the slug before publishing. Ghost has a known bug that can reset it to the title, breaking the URL.

### Tagging Strategy

  - **Purpose:** Tags categorize content and determine its homepage placement.
  - **Primary Tags for SEO:** `guides`, `building a startup`, `starting a business`, `programming`.
  - **Rule:** The first tag assigned becomes the post's primary category on the blog homepage.
      - **Example:** A post tagged `AI` and `Community` will appear under `Community` if `Community` is listed first.

### Content Formatting & Blocks

  - **Tables:**
      - Use the `/table` command to insert a pre-styled block.
      - **Recommendation:** Use `Table Style 2` (normal header row) for versatility.
      - **Avoid:** `Table Style 1` (locked left header) can break on wider screens.
      - **Custom HTML:** If using, ensure the Bubble-specific `class` line is at the top of the code block to apply the correct styling.
  - **Headings (H1, H2):**
      - **Rule:** Do not bold headings.
  - **Images:**
      - **Alt Text:** Required for all images; simple descriptions are sufficient.
      - **Captions:** Optional, unless crediting a source.
  - **Callout Box (CTAs):**
      - **Purpose:** For prominent calls-to-action.
      - **Style:** Use the default blue background.
      - **Formatting:** The arrow (`→`) must be typed in a separate editor (e.g., Google Docs) and pasted, as Ghost does not auto-format `-->`.
      - **Tracking:** Include UTM parameters in all final CTA links.

---

## Action Items

**Sara Merg**
- Email Erik UTM builder link + format; then Erik's team adds UTMs to final CTA links

**Erik O'Brien**
- Draft first 2–3 SEO posts in Ghost; then Sara reviews/publishes

---

## Transcript
**Sara Merg:** Starting.

**Sara Merg:** Good.

**Sara Merg:** It's just starting.

**Sara Merg:** Sorry, it's going to be right at the top of the day.

**Sara Merg:** Oh, no worries.

**Sara Merg:** I start early.

**Erik O'Brien:** I've been up for a couple hours.

**Sara Merg:** So how does this work?

**Sara Merg:** I pulled up the ghost CMS and stuff, and I was figuring I could just show you some of the weird stuff or show you how I build one of the blogs that you guys have drafted for us or something, but let me know.

**Erik O'Brien:** Yeah, that sounds great.

**Erik O'Brien:** Yeah, just trying to get enough context for our publishing team so that when they get into staging and publishing the articles, they kind of know what to look out for, any specific fields that are tricky or weird, and then just the overall process to get things up and running.

**Erik O'Brien:** Okay, cool.

**Sara Merg:** Yes, let me share my screen.

**Sara Merg:** Can you see that okay?

**Erik O'Brien:** Yep.

**Erik O'Brien:** Okay, perfect.

**Sara Merg:** So, okay, so let me just back up.

**Sara Merg:** I was just making sure that I had a doc set up.

**Sara Merg:** So once you're in Bubble.Ghost.io's, like, login state, you'll probably be sent to, like, this homepage, which is, like, a mock-up of the actual homepage, which is Bubble.io slash blog.

**Sara Merg:** And then you can see, like, the published stories are under published, and you can see, like, featured ones, which are up here at the Hero.

**Sara Merg:** I'm predicting that because these are SEO blogs, this won't, like, ever, we don't, like, really ever, like, feature those.

**Sara Merg:** We mostly feature, like, product announcements and stuff.

**Sara Merg:** But if you want to feature something, you would basically just, like, go in and select feature this post, and then you would have to go into the featured.

**Sara Merg:** posts and like basically unselect the last one or else it'll like show an extra one in a row.

**Sara Merg:** That's like one weird thing.

**Sara Merg:** But I don't think I don't expect to use that.

**Sara Merg:** Typically, typically not, but just just FYI.

**Sara Merg:** And then to start a new post, you could either click on this.

**Sara Merg:** You could click on this.

**Sara Merg:** I have one set up just to make sure it was all going well.

**Sara Merg:** So this is like for headline.

**Sara Merg:** This is the excerpt section.

**Sara Merg:** You might see it depending on how your toggles are on.

**Sara Merg:** You might see it right here above the post URL.

**Sara Merg:** This is where you put the slug.

**Sara Merg:** Date published.

**Sara Merg:** Like we don't really like ever backdate anything.

**Sara Merg:** But if we are updating an article, I just would want to make sure that we update the date as well so that it feels like as current as possible.

**Sara Merg:** For an SEO blog, would typically do, we have kind of a number of topics or like tags.

**Sara Merg:** I can go to that page.

**Sara Merg:** These ones right here, programming, using bubble, and community are sort of like three like core tags, but we have like a ton.

**Sara Merg:** I would say that like they're pretty self-explanatory.

**Sara Merg:** Usually for SEO blogs, because they're so general, I'm usually using like guides, building a startup, starting a business, and then like if it's like AI specific or mobile specific, that one as well.

**Sara Merg:** And if it's like something about like how to build, I would probably also select programming.

**Sara Merg:** And then if we are using, like I would use like the most specific tag as the first one, because that's what will like show up on the page.

**Sara Merg:** So for example, like if I go into the AI, this is also tagged as community.

**Sara Merg:** And so because community is the first page, even though it'll show up under AI, but because it's community is the first tag, it's showing up.

**Sara Merg:** As under the community tag, first and foremost, if that makes sense.

**Sara Merg:** Yep.

**Sara Merg:** And then everything else is pretty self-explanatory.

**Sara Merg:** If we want to do tables, we have, which I know we're in that first draft, Ada sent over, I'm pretty sure.

**Sara Merg:** You could just go here and using this forward slash is usually the command to pull up the menu.

**Sara Merg:** You can just do table and there's, we have two tables like styled in here that we can like use.

**Sara Merg:** I'll just preview those so you can see the difference.

**Sara Merg:** We have sort of like a locked left like header row almost.

**Sara Merg:** And then also just like a normal, one normal header row.

**Sara Merg:** You can obviously add columns to these and add rows.

**Sara Merg:** You would, I would recommend like not typing the HTML in ghost.

**Sara Merg:** I would recommend like if you have like any type of like CSS or HTML built like.

**Sara Merg:** Like, Builder, like, either the free one or, like, I've used, like, VS Code for it before just to, like, copy and paste it all in.

**Sara Merg:** The one thing is to make sure that the, oops, sorry, this, like, class line is up at the top or else it won't show, like, in the proper, like, preset styles.

**Sara Merg:** It'll just show, like, ghosts, like, generic styling.

**Sara Merg:** But if there's anything weird with that, you can always just, like, let us know and we can, like, play with it.

**Sara Merg:** I would say that probably this one, which I think is Styling 2, is probably the more versatile one.

**Sara Merg:** And you can, like, bold all the entrants over here.

**Sara Merg:** For example, if you want to add columns, I find that sometimes this format gets weird as it gets wider.

**Sara Merg:** Gotcha.

**Sara Merg:** So I would say probably you'll want Table Style 2.

**Sara Merg:** Okay.

**Erik O'Brien:** The other stuff is, like, pretty self-explanatory.

**Sara Merg:** Maybe I'll go into a draft that we've already published to show what I'm talking about.

**Sara Merg:** So this is like a, this is like an SEO blog, obviously.

**Sara Merg:** Pretty, pretty standard.

**Sara Merg:** We use H1s and H2s.

**Sara Merg:** These should not be bolded as like one styling note.

**Sara Merg:** And then I just want to make sure that we do like any alt text.

**Sara Merg:** It can be like super simple, but if there's any images attached, I definitely want the alt text to be in.

**Sara Merg:** I'm not very picky about captions.

**Sara Merg:** I don't really need a caption unless it's like via somebody else.

**Sara Merg:** We want to like credit in the caption.

**Sara Merg:** And then we have like drop quotes.

**Sara Merg:** There's like a couple stylings.

**Sara Merg:** That one we don't use.

**Sara Merg:** This will be like, it'll be the styling of the first one that pops up when you like basically like pull up the styling menu.

**Sara Merg:** Yep.

**Erik O'Brien:** And then we have like one, I feel like this one maybe doesn't have any.

**Sara Merg:** Oh, at the, at the footer.

**Sara Merg:** then anytime we want to do like any type of call out, we use like the call out box.

**Sara Merg:** Which can come up.

**Sara Merg:** up with the command slash and then just like start typing you can like set this emoji to anything you can we usually are including like a link there obviously and we like using this like like arrow that comes up when you're like in Google Docs or word if you do like what is it like dash dash and then the little carrot that doesn't set automatically in ghost which is like randomly kind of a pain to me so you have to like type it elsewhere but um that should be fine um feel free to get creative with the emoji you pick we're not picky there and then usually we do blue and that's like pretty much it's like pretty honestly it's quite straightforward um yeah I think we usually do like a UTM in the final like CTA or like just to like make sure that we're like tracking as much as possible um

**Sara Merg:** I can, like, send you how those are formatted.

**Sara Merg:** We have, like, a little, like, builder, but it's usually just, like, the post title.

**Sara Merg:** Okay.

**Sara Merg:** Is there anything that you are thinking of that I have not included?

**Erik O'Brien:** Don't think so.

**Erik O'Brien:** So far, it's you showed me.

**Sara Merg:** Yeah.

**Sara Merg:** Because it's ghost and not, like, proprietary or anything.

**Sara Merg:** Like, I feel like I've worked at places where, like, if there's been a proprietary CMS and it's been way weirder, I think ghost is, like, pretty standardized and pretty, like, self-explanatory.

**Sara Merg:** So that should be good.

**Sara Merg:** The one note I have is sometimes if you've copied and pasted the text, you should just double-check the slug before you hit publish to make sure it stayed what you intended, because sometimes it resets to the title, which is a bug on the ghost side of things.

**Sara Merg:** But other than that, honestly, like, pretty self-explanatory.

**Sara Merg:** You, it's really, like, just copy, paste, drag, and drop kind of style.

**Erik O'Brien:** And then for authors, we just use Bubble.

**Sara Merg:** Yeah, I think we'll use Bubble for any SEO piece, and also for product announcements once we're announced.

**Erik O'Brien:** Cool.

**Sara Merg:** Obviously, if, like, any other weird things come up or if I realize that I forgot something critical that's, like, kind of weird or strange, like, I'll definitely let you know.

**Sara Merg:** But let me know if any other things come up as your team is, like, building.

**Sara Merg:** Absolutely.

**Erik O'Brien:** And then for the first few, do you guys want us to draft them and you hit publish?

**Sara Merg:** Maybe for the first two or three, we could just take a look to make sure the formatting is not strange or abnormal.

**Sara Merg:** And that would also help us know if we've like covered everything that we should be telling you.

**Sara Merg:** Absolutely.

**Erik O'Brien:** Awesome.

**Sara Merg:** Awesome. Super helpful.

**Erik O'Brien:** Yeah, you too, Sara. Have a great rest of your day.

**Sara Merg:** Bye.
