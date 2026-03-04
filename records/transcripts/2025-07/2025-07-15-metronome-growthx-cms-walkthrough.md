# Metronome/GrowthX - CMS Walkthrough

<metadata>
date: 2025-07-15
time: 20:34 UTC
duration: 20 minutes
organizer: Sydney Go
participants: Stephanie Keep, Chang Li, Nemanja Simic, Sydney Go, Megan LaFlamme, Maggie Lin, Maddy Fennessy
fathom_recording_id: 74364180
fathom_url: https://fathom.video/calls/351737111
share_url: https://fathom.video/share/qmrGWyMFVHAHRmtg9S_7G_f__svHBSta
source: fathom
enriched_on: 2026-03-03 12:15 UTC
</metadata>

---

## Summary

Stephanie Keep walked through Metronome's Webflow CMS system, showing the GrowthX content team how to create and publish blog posts, including navigating the blog editor, formatting requirements (AVIF images for optimization, JPEG/PNG for social sharing), and handling custom HTML for tables and styled quotes. The team confirmed access is still pending (hit seat limits on the team account) and discussed author rotation between Stephanie, Chang, and Maggie to maintain content diversity, plus next steps on blog image templates and glossary feature support.

---

## Context

Metronome is a product company that GrowthX is creating content for (Series C announcement already published on their blog). Metronome's website runs on Webflow, and the team built out a CMS for managing blog posts and glossary entries. Stephanie Keep from Metronome is the primary content operations contact, while GrowthX's content team (Nemanja, Sydney, with input from the broader team) needs hands-on access to the CMS to publish blog posts at regular cadence. This walkthrough happened because the GrowthX team needed training on the CMS workflows—how to structure posts, handle images, format custom HTML, and manage author attribution. The CMS access was still pending due to Webflow seat limits, which Stephanie committed to following up on with Metronome's account team.

---

## Relevance

**To GrowthX Delivery:**
- CMS training completed; GrowthX team (content + ops) now understands Webflow blog workflow and image requirements (AVIF primary, JPEG/PNG for socials)
- Author rotation strategy established (Stephanie Keep, Chang Li, Maggie Lin) to diversify bylines and reduce perception of AI-generated content
- Custom HTML approach documented for complex elements (tables, quotes) — team can reference existing posts or use ChatGPT for generation, but QA required post-publish since preview doesn't render custom code
- Pending blocker: Webflow seat limit reached; Stephanie to resolve with Metronome account team

**To GrowthX Business Development:**
- Active engagement signal: Metronome content strategy is progressing toward regular publishing cadence with defined author rotation and asset pipeline
- Team expansion visible: Megan LaFlamme coordinating with Ada on featured image strategy and template creation; planning to streamline asset creation process
- Glossary feature request: Sydney Go flagged opportunity to implement custom glossary support (possibly Charge B style); awaiting feedback on complexity

---

## Overview

- GrowthX team needs access to Metronome's Webflow CMS; Stephanie will follow up on this
- Blog posts require specific image formatting (AVIF for most, JPEG/PNG for social sharing)
- Custom HTML/CSS may be needed for certain elements (tables, quotes); GrowthX can reach out for guidance
- Author rotation (Stephanie, Chang, Maggie) recommended to avoid appearing AI-generated

---

## Key Topics

### CMS Navigation and Blog Post Creation

  - Access Webflow CMS via "Metronome New" build
  - Create new posts under "Blogs" tab
  - Fields include title, slug, author, tags, publication date, images, meta description, and article body
  - Custom formatting available (headings, HTML, code blocks)
  - Table of contents and CTA options at bottom of post editor

### Image Requirements

  - Most images need to be in AVIF format for optimization
  - Social sharing image should be a small JPEG or PNG
  - Stephanie will share developer's notes on image specifications

### Custom Styling and HTML

  - Some elements (quotes, tables) may require custom HTML
  - GrowthX can use existing posts as references or ask GPT for HTML generation
  - Webflow preview doesn't show custom HTML; always QA after publishing

### Glossary Items

  - Glossary entries also managed through CMS
  - Potential for more complex implementation (e.g., Charge B style) may require additional work

### Webflow Collaboration

  - Multiple users can work simultaneously without being kicked out
  - Unclear if concurrent editing of the same post is possible; to be tested

### Content Assets

  - Plan for blog post images and assets to be discussed further
  - Ada to provide examples of featured images in Slack
  - Possibility of template images with updatable text to streamline process

---

## Action Items

**Stephanie Keep (Metronome)**
- Follow up on Webflow access issues for GrowthX team (team account / seat limit)

**Sydney Go (GrowthX)**
- Provide feedback on glossary items support for Metronome team

**Megan LaFlamme (Metronome)**
- Coordinate with Ada to pull together examples of featured images for Metronome blog in Slack

**Stephanie Keep (Metronome)**
- Request template images from Chris and Carolyn for streamlined blog post creation (with updatable text)

---

## Transcript
**Stephanie Keep:** Can you get in?

**Nemanja Simic:** I haven't.

**Nemanja Simic:** Sydney, do you know if we've gotten the access or anything like that?

**Sydney Go:** We've not gotten access to my knowledge, but I can ask around if you think that you've already given an answer to us.

**Stephanie Keep:** I know that Maggie was asking, I think she asked if you guys had like maybe a team account or something.

**Stephanie Keep:** I think we may have hit our limit on seats. So I won't hold this up with this. I will take that as an action item to follow up on wherever that landed.

**Stephanie Keep:** Alright, let me just share my screen here. Sorry, one sec, we're not on Google that often, so I'm slower than usual here. I'm going to have to hop off and restart so I can show my screen to you.

**Nemanja Simic:** I'll make sure to know for next time that we can make it a Zoom call.

**Chang Li:** I'm surprised you folks are still on Google Meet.

**Nemanja Simic:** Honestly, it's been me — I'm also used to it, so when I set the invite it's just automatic for me. Yeah, it looks like I'm on Webflow right now, but it looks like we don't have access to anything for Metronome.

**Stephanie Keep:** Alright, let's try this again. Alright, here we go. Can everyone see that?

**Nemanja Simic & others:** Yes.

**Stephanie Keep:** Awesome. Okay, so when you guys log in for the first time, this is always where I end up landing when I go into Webflow. You might actually end up here too. Thank you, Chang.

**Stephanie Keep:** So if you're in here, you can see we have a few different builds. The current one that we're on is Metronome New, so you would just go ahead and open that in Webflow. You'll come in here, and to get into where you're going to actually publish the blog post, you're going to hit this CMS button — it looks like a little stack of coins up here on the upper left. Click on that, and then on this side here, let me see if I can make this bigger. Okay.

**Stephanie Keep:** On this left-hand side, you can see "Blogs" is the tab where you can edit, add, or create new authors. If you need to create a new author, you would enter their title, name, and photo. One important thing to note with images: they need to be in AVIF format (A-V-I-F) instead of PNG or JPEG to optimize file size. I can share our web developer's notes on that. You probably have a tool for that already, but basically all images need to be AVIF except for one — the social sharing image.

When you create a new blog post, you click the "new blog" button. This is where the title goes. The slug automatically fills in (like "usage-based-billing"), and you can change it but we usually leave it as-is. The "Featured" field puts it at the top of the blog — right now we have our Series C announcement up there. Tags are used as categorization (pricing, engineering, etc.) but not super frequently. You can add a publication date — make sure you set this manually before publishing, as it doesn't default to today.

The featured image needs to be AVIF format, and there are notes from our developer here. For social sharing, you need a small JPEG or PNG. Pretty much everything will be AVIF except the social sharing image. The meta description has a limit of around 300 characters and 55 words. Then you plop in your article body.

You can do custom formatting with headings and HTML/code blocks. Chang, do we have a style guide for attributed quotes and custom styling?

**Chang Li:** Absolutely. We don't have a UI component for things like tables and quotes, so we have to use custom HTML. That's where custom code comes in.

**Stephanie Keep:** Yeah, we could probably provide those resources. For that, I just go and grab the code from another blog post, inspect the element, and adjust it as needed. Nemanja, do you need to go over this?

**Nemanja Simic:** I've done it on Webflow before. Normally I'll have the info in a doc, convert it, put HTML, and embed it. I can just ask GPT to make it HTML for me.

**Stephanie Keep:** Yeah, ChatGPT is a great option. If you need to render it, you can use w3.org or similar, but ChatGPT exists now — easy to forget that.

**Sydney Go:** I did have one question. Do you have custom CTA codes that you use in Webflow? Some of our customers have custom CTAs in HTML brackets. Do you have a list of those we could get?

**Stephanie Keep:** I don't think we do currently, but I'd be interested in seeing examples if you can share them. That might be something we'd want to implement.

**Sydney Go:** Sure.

**Stephanie Keep:** This is pretty much the core of it. It's self-explanatory, but if you guys run into anything, I'm happy to be your point person.

**Stephanie Keep:** Oh, sorry.

**Chang Li:** Stephanie, there were two very minor, but I want to just call up.

**Chang Li:** Do you want to scroll to the bottom?

**Chang Li:** Mm-hmm.

**Chang Li:** Scroll up a little bit.

**Chang Li:** Sorry.

**Chang Li:** Oh, yeah.

**Chang Li:** Yeah.

**Chang Li:** So it's.

**Chang Li:** Stuck here.

**Chang Li:** Great.

**Chang Li:** So there are two buttons where you see, one is show table of content.

**Chang Li:** So this one is like, we're only surf, I think we're only show H2 or H3 at this moment.

**Chang Li:** So if any header, headlines are made H2 or H3 will be auto shown here if we enable the table of content.

**Chang Li:** And the show CTA button shows our permanent CTA, which is "subscribe to our blog." If you enable it, it will pop up on the site. It hasn't worked well in the past, but with more regular content cadence now, it might be worth trying.

**Stephanie Keep:** Should we have someone flip it on for everything?

**Chang Li:** Yeah, we'd have to intentionally enable it. Otherwise, they're off by default.

**Stephanie Keep:** Let me show you an example of the table of contents in action. It appears here on the side. One important thing with Webflow: if you add custom HTML or code blocks and then preview it, the code won't show up in the preview. So I always do a quick QA right after publishing to make sure nothing broke. Also, the back button doesn't work in preview mode — you have to go back to your CMS and re-enter the blog draft.

For glossaries, we do have those managed here too. If you want to do something like the Charge B style, that might require more work than just editing the entries here. We can help figure that out if needed.

**Chang Li:** Did I miss anything you guys should know?

**Stephanie Keep:** Anything else we should go over?

**Nemanja Simic:** I'm assuming Webflow kicks people out if multiple people are editing at once. With another client, I get signed out every 10 seconds when someone else is in Webflow. Is that the case here?

**Stephanie Keep:** I don't think ours has that. I can see a bubble with other people, like in Google Docs, but I've never been kicked out. I'm not sure if you and I can edit the same blog post simultaneously, though.

**Nemanja Simic:** Yeah, we'll find out when we all try working together. Sometimes I'll publish early in the morning when I'm on the East Coast and people are on the West Coast, so I can finish before anyone wakes up.

**Stephanie Keep:** That works too. Chang, one quick comment: can you rotate between me, Stephanie, and Maggie as authors? If it's just one person, it feels AI-generated. We want to distribute across the team.

**Chang Li:** Sounds good.

**Stephanie Keep:** Alright, I think that covers it. If you run into anything odd, feel free to tag me. Is there anything else you need before we wrap?

**Nemanja Simic:** I think we're good on our end, Sydney?

**Sydney Go:** Thank you so much for the walkthrough. That was really clear and quick. I'll get back to you on glossary items if we can offer deeper support. This was amazing, thank you.

**Stephanie Keep:** I appreciate it. One more thing: have you discussed images and assets for the blog posts? Do we have a plan for that?

**Sydney Go:** Do you have a specific style guide to share?

**Megan LaFlamme:** We just discussed this with Ada right before the call. She's going to pull together examples for us in Slack of what they'd provide for featured images. We can decide if we want to leverage what they have or have Chris help.

**Stephanie Keep:** Should we loop Chris in? I don't think that'll be sustainable long-term. I also asked about template images where we could just update the text — that would make it much more streamlined.

**Megan LaFlamme:** Yeah, that makes sense.

**Stephanie Keep:** Alright, let me know if there's anything else. Megan, thanks for coordinating. If you guys have any other questions, just let me know. I'm really excited about this. Thank you for the partnership.

**Megan LaFlamme:** Thank you for doing this walkthrough.

**Stephanie Keep:** Thanks, everyone.

**Nemanja Simic:** Bye.
