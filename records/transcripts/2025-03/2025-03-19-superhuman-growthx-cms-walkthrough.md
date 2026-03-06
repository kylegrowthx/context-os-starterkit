# Superhuman <> GrowthX CMS Walkthrough

<metadata>
date: 2025-03-19
time: 20:31 UTC
duration: 24 minutes
organizer: Elvis Goren (elvis@growthxlabs.com)
participants: Elvis Goren (GrowthX), Alex Rodrigues (Superhuman)
speaker_note: Wiets Rossouw and Nemanja were invited but did not speak during the call. Only Elvis Goren and Alex Rodrigues participated actively.
fathom_recording_id: 52803710
fathom_url: https://fathom.video/calls/256447577
share_url: https://fathom.video/share/oh5b47fxtFh2HYzE2StWkMKoaGrkB1yG
source: fathom
enriched_on: 2026-03-04 14:30 UTC
</metadata>

---

## Summary

Alex Rodrigues from Superhuman walked Elvis Goren through Superhuman's Ghost CMS, covering blog structure, publishing workflows, and content strategy for their upcoming SEO collaboration. The team discussed expanding blog categories to include AI content, leveraging product imagery and interactive Arcade demos in blog posts, and establishing guidelines for CTAs, cover images, and social proof. Elvis agreed to explore using Recraft for AI-generated cover imagery, while Alex committed to compiling feature assets and sharing Ghost login credentials via 1Password.

---

## Context

Superhuman is a Y-Combinator-backed email productivity tool with a distributed team (offices in San Francisco and LA, plus remote staff). The company has built a strong brand presence on Twitter, with CEO Rahul Vohra commanding 60-70k followers. GrowthX is preparing to launch a significant SEO content collaboration with Superhuman, creating content around core product features like email tracking, inbox zero, and AI capabilities. This CMS walkthrough was a foundational working session to align on Superhuman's Ghost CMS, publishing process, and content asset availability before GrowthX begins writing SEO articles.

---

## Relevance

**To GrowthX Delivery:**
- Ghost CMS uses command-based structure (slash commands) with native rich text editor, image uploads, embeds (YouTube, Twitter), and custom HTML for CTAs — informs how GrowthX will structure and format SEO content for Superhuman
- Superhuman uses product imagery, GIFs, and interactive Arcade feature demos as content assets — GrowthX should request these assets upfront rather than creating custom imagery
- Superhuman blog redesign planned for Q2 2025 with potential information architecture updates — GrowthX should align SEO content strategy timing and category structure with the redesign
- CMS access still pending via 1Password share — may delay initial content uploads until access established

**To CheckThat:**
- Superhuman's social proof strategy includes Twitter embeds, LinkedIn reviews, and their "Love" testimonial page — relevant for AEO visibility and AI-generated social proof sourcing
- Superhuman CEO has strong Twitter presence (60-70k followers) with active brand building — good reference for how B2B SaaS leverages CEO social for distribution

**To GrowthX Business Development:**
- Superhuman appears early-stage with distributed team and is investing in brand and content strategy — potential for ongoing retainer or expanded engagement beyond initial SEO project
- Team structure shows Harmony (leading blog redesign), Alex Rodrigues (content/demand gen), Morgan (new demand-gen leader) — opportunities to expand relationship across multiple stakeholders

---

## Overview

- Superhuman's Ghost CMS blog has four main categories (News, Sales, Productivity, Leadership) with plans to add AI category in Q2 2025 redesign
- Blog redesign in Q2 will update information architecture and brand design; CMS supports rich text, custom HTML snippets, embeds (YouTube, Twitter), and command-based structure
- Content strategy includes multiple CTAs (buttons, HTML snippets, hyperlinks), product screenshots, AI-generated imagery (using Recraft), and interactive Arcade feature demos
- Superhuman will provide library of ~12 key product assets (feature videos, GIFs, Arcade demos, approved images) and HTML snippets for brand-compliant CTAs
- Twitter/social proof integration leverages Superhuman CEO's 60-70k followers and "Love" testimonial page; Superhuman does not use free trials by default
- CMS access pending — Alex to share Ghost login via 1Password once internal team structure allows; team to test content creation during initial calibration phase

---

## Key Topics

### Blog Structure and Categories

  - Blog separate from main site, moving from subdomain to main domain
  - Current categories: News (product announcements), Sales, Productivity, Leadership
  - Considering new AI category due to high content volume
  - Blog redesign planned for Q2 2024, including potential information architecture updates

### CMS Walkthrough (Ghost)

  - Login via <ghost@superhuman.com> (specific access details pending)
  - Post management: Drafts, Scheduled, Published sections
  - Rich text editor with various formatting options (headings, bold, italics, quotes)
  - Command-based structure for adding elements (images, HTML, dividers)
  - Custom HTML snippets used for brand-consistent CTAs

### Content Strategy and Best Practices

  - Multiple CTAs throughout content, including image elements to break up text
  - Hybrid approach: buttons, styled elements, and hyperlink CTAs
  - No free trial by default; potential for testing in SEO article flow later
  - Social proof integration: Twitter embeds, testimonials from "Love" page
  - Leveraging CEO's social media presence (60-70k followers) for brand building

### Imagery and Asset Management

  - Current use of stock imagery and product screenshots
  - GrowthX suggests using Recraft for AI-generated images based on templates
  - Superhuman to provide library of approved product images, GIFs, and HTML files
  - Arcade tool for interactive feature demos, embeddable via iFrame

### Publishing Process

  - Option to schedule posts or publish immediately
  - Ability to edit publication date retroactively

---

## Action Items

**Alex Rodrigues (Superhuman)**
- Discuss potential new blog categories (e.g. AI) with Harmony for Q2 redesign
- Follow up on sharing Ghost CMS login via 1Password with team@growthx.ai
- Compile list of ~12 key feature assets (videos, GIFs, Arcade demos) for blog use
- Share HTML snippets for CTA buttons matching brand style

**Elvis Goren (GrowthX)**
- Discuss imagery guidelines and Recraft tool usage for blog post covers

---

## Transcript

**Elvis Goren:** I'm doing well, thanks. It's good.

**Elvis Goren:** Guys are busy over there. Oh, and you have no idea.

**Alex Rodrigues:** Let me try to get my headphones going. I'm going to ping them.

**Elvis Goren:** I think he's supposed to be in this meeting. Is someone else joining us?

**Alex Rodrigues:** I guess not.

**Elvis Goren:** Well, it's going to be recorded.

**Alex Rodrigues:** How do you pronounce his name? Is it "Weets"?

**Elvis Goren:** "Wits."

**Alex Rodrigues:** Nice. He accepted the invite. If you want to give it a second, that's fine too.

**Elvis Goren:** No, he doesn't want to go up against anyone.

**Alex Rodrigues:** He's the account manager for Superhuman, so he's working with me a lot on the content. But he can just watch the recording — it's all good. If he joins, he joins. Okay, cool. All right, so let's see. A real quick orientation — I think you've already seen this, but our blog sits separately from the site. There's going to be some backend infrastructure work that pulls this off a subdomain onto the main domain, but we largely have things bucketed into News, which are for product announcements. This is where everything my team or Rahul, our CEO, are putting out around things we're launching. Not everything gets a blog post for it, right? It varies in terms of how we approach it.

**Alex Rodrigues:** Then we've got all our content related to sales, which I don't know if we've chatted that much about. In 2024 particularly, the sales team was a really huge difference for us, so we've got a bunch of content there. Then there's General Productivity, which is largely for the topics we've been chatting about — the most relevant stuff. And then Leadership is more of a relic of the past. I can talk about the implications, but within our target audience, leadership ends up being a really core ICP, right? We know that we just over-index on our ability to acquire leaders.

**Elvis Goren:** Are there any plans to expand that list of categories at all? We have a pretty wide range of topics, and a lot of the AI-focused stuff overlaps with sales. I'm just asking now before we run into something.

**Alex Rodrigues:** Yeah, I think we should have that conversation with Harmony because she has the best vision for where the blog will go. But I'm totally open to launching new categories. We also need to redesign the blog page because it's still in our old brand design. That's a project we expect to take on in Q2, and updating information architecture during the redesign would make total sense. Maybe we want to launch an AI category, for example, because there's just so much that is AI — sure it might apply to sales and productivity, but we just want to own it. That would be totally reasonable in my mind.

**Elvis Goren:** Awesome. Cool. Okay, are you familiar with Ghost?

**Alex Rodrigues:** Have you used Ghost before?

**Elvis Goren:** No, I've used a bunch of different CMSes. There are so many, it's tough to keep track sometimes.

**Alex Rodrigues:** How much do you want me to go through? Do you want me to walk you through logging in and all that stuff, or what works best?

**Elvis Goren:** As much as we can, because we want to have the process down so we're not asking every time.

**Alex Rodrigues:** Okay, my cat just joined me here. Let me make sure there's room for her. All right, so I think I can share these externally too. Actually, you guys haven't given us access to the CMS yet. How do you guys share access?

**Elvis Goren:** I'm assuming you share an invite and we create an account and password?

**Alex Rodrigues:** No, with Ghost I have the password for this in 1Password. Let me see... So I'll just share the login info with you and you'd be able to log in directly. But we don't actually have... that's a good question. It looks like it's an issue with our seat type. We use 1Password, so I think I should be able to share the login via 1Password, but I'll double check and come back to you. Basically, you just log in through ghost@superhuman.com, which is how I normally log in. I'm not sure why that didn't work just now, but that's the one I would probably share. So, you can see three categories of posts: Drafts, Scheduled, and Published. The Published category is everything that's currently online.

**Alex Rodrigues:** For new posts, there are a few different things you can do. The URL pulls in based on the subject line, but you can edit the date and time. All the tags we talked about are here — there are other tags that aren't currently featured. Design used to be a big focus, and "Getting Started" was help content that we migrated to a help center. The most important tags are Leadership, News, Productivity, and Sales. We should talk about adding an AI tag. You can tag posts to multiple categories so they show up across those. Everything we do is public — we don't have any hidden content. For SEO-related content, we typically list the author as "Superhuman Team," and we reserve Rahul, our CEO, for more product announcement stuff. We don't typically feature SEO content with the big hero image on the blog post. We reserve that for product announcements. You can also add feature images. Have we talked about our plan for imagery yet?

**Elvis Goren:** I was going to bring that up either today or at our next meeting tomorrow. I noticed you guys use a lot of stock imagery. The biggest thing is once we ramp up, it's going to be a lot of volume, so we need to be mindful of that. We have workflows to create cover imagery for each post, but I'd love to hear your guidelines for cover imagery.

**Alex Rodrigues:** That's a good question. Let me show you one thing. One of the things about the product is when you reach Inbox Zero, we show this really cool image that mirrors the experience in the product. We can give you the full library of images we have already piped into the product as one avenue. You could also see in some of our last SEO content there's AI-generated imagery and different things. So yeah, I'm open to how we approach it.

**Elvis Goren:** Yeah, I can tell you what we're doing with other clients is using a tool called Recraft. It really depends on the requirements. The great thing about it is if we have templates — whether it's a graphic, a simple vector-style image, or a background — we can take five to ten images as style guides and it easily creates cover imagery. We run through the entire workflow, and at the very end when we have the final article, it creates an image based on that. So we can go a lot of directions with it. Adding a screenshot from a feature would be more difficult, but we can think about that.

**Alex Rodrigues:** Our team can potentially be a blocker on getting you product videos. To the extent we can default to not relying on product imagery, that's faster. But we could share examples of our product launch videos explaining specific features like AI features, or we could share approved images, GIFs, and other assets that might work. We should identify the top 10 features that come up a lot — the heavy-hitting AI features, Inbox Zero, comments, shared threads — and give you a handful of plug-in assets. Are you familiar with Arcade?

**Elvis Goren:** Arcade?

**Alex Rodrigues:** It's basically a tool where you can build interactive demos. We have some of these built for our features. You can embed them into the blog post — it's kind of like a video that you can annotate, and the person can control the speed and advance on their own. So I can come up with a list of about a dozen assets that work well and aren't overwhelming — good examples of our marquee feature set.

**Elvis Goren:** That would be great. How easily does that work? What kind of file is it, and is it easily implementable?

**Alex Rodrigues:** It's hosted on their own site, and you can just embed the iFrame. You can also do videos and GIFs too. If you guys have a library of that, including the HTML files, we can pick appropriate places to use them. Depending on the blog, not every piece is going to be as extensive as what I sent recently, but having a library of images, GIFs, and HTML files that we can use where we see fit would be awesome.

**Elvis Goren:** Yeah, totally.

**Alex Rodrigues:** Okay, I'll start working with my team on pulling that together. So, let me show you Ghost itself. I've copied some content here so we can play around with it. In Ghost, there are different heading styles — it's basically a rich text editor. There are headings 1 through 8, bold, italics, quotes with different styles, and hyperlinks. There's also a command-based structure where you either hit the plus button or forward slash. You can add images, markdown, HTML, dividers, bookmarks. The native button styles in Ghost don't match our brand styles, so for CTAs we use HTML snippets. I can show you an example in a second.

**Elvis Goren:** What are your best practices for CTAs? I'm curious about spacing them throughout content.

**Alex Rodrigues:** It really depends on the content. Our product announcements usually have a try Superhuman CTA above the fold, then we bring it in at the end with a hyperlink, and we end every post with another CTA button. Do you have a sense of best practices?

**Elvis Goren:** I think it really depends, but ideally there are a few CTAs peppered throughout. If you look at top SEO websites, a lot of times they include an image element that breaks up the content — whether it's a block for email signup or a try-now button. I've used those a lot and they work if they're relevant to the topic. For example, if it's about a specific feature people struggle with, and you have a relevant CTA like "Find your email faster — try it today." I don't know if you guys have a free trial, but that's significant.

**Alex Rodrigues:** Sounds good. I think you should implement a hybrid of buttons, styled elements, and hyperlink CTAs. The try Superhuman button is an HTML snippet I can share with you. Do you guys have a free trial?

**Elvis Goren:** We don't have a trial by default. We offer it for some channels like our affiliate program, but we find trials lower intent — slightly more revenue but much lower quality. Once we get a program up and running, I'd be open to testing SEO article flows into a trial, but maybe not as default.

**Alex Rodrigues:** That makes sense. You can also embed YouTube, and we're really active on Twitter — that's where a lot of our target audience hangs out. We've embedded tweets too. Have you seen our "Love" page on our website? It's basically testimonials about the product. We pull from LinkedIn, reviews, and other sources. I have a library of about 20 best tweets on different topics — productivity, AI — that we use across the website, so that's another area we might be able to share.

**Elvis Goren:** Good to know. I checked your guys' Twitter last week and saw 50k followers with really sweet content. That's cool.

**Alex Rodrigues:** Thanks. Our CEO, Rob Hall, actually has even more followers — 60 to 70k — so we leverage his presence a lot for brand building. And then just to finish up, you can hit review to see how it looks on the blog, and you can toggle for mobile too. When you hit publish, you can schedule it or publish immediately. You can pick a different time, and you can also edit the published date retroactively. So if you publish at 11 PM, you can have it show as 9 AM that morning.

**Elvis Goren:** Cool.

**Alex Rodrigues:** And then it goes through final review and publishes. Seems straightforward enough.

**Elvis Goren:** So for 1Password, do you want me to try and share it with team@growthxlabs.com?

**Alex Rodrigues:** Let me just make sure, because there's a weird team factor with the account I was just logged into. That's why I want to share the other one. I'll follow up and get the right one.

**Elvis Goren:** Yeah, we're still doing content calibration. I think after we get close on tone and voice, we'll circle back and get that access.

**Alex Rodrigues:** Let me see if I can do this real quick. Any other questions?

**Elvis Goren:** No, if we come across something while uploading, that's usually the best way to address it. If we run into anything, we'll ping you.

**Alex Rodrigues:** Just ping me in the channel or call — whatever works. Where are you based, by the way?

**Elvis Goren:** I'm in Winnipeg, Canada. Above North Dakota.

**Alex Rodrigues:** Nice. Our team is pretty distributed. Harmony and I are in San Francisco, Morgan is our new demand-gen leader, and Rahul is in LA. So we've got a good chunk of the team in SF but pretty scattered overall.

**Elvis Goren:** I think Morgan was on a call last week?

**Alex Rodrigues:** She might have been. It's her first couple weeks, so things blur together.

**Elvis Goren:** I didn't recognize her at first and thought I was in the wrong call.

**Alex Rodrigues:** That makes sense. It's been a good time and cold here in Winnipeg?

**Elvis Goren:** Yeah, it sucks. It was close to zero, but I'm happy with that now. So let me look at the 1Password sharing settings real quick. I can't share it indefinitely, but I can give you a temporary code for 7 to 30 days. Do you guys have a way to add it into your 1Password?

**Alex Rodrigues:** I'm not sure. Let me check with our team.

**Elvis Goren:** Okay, I'll reach out and see if there's another option, because I want to make sure we set this up right.

**Alex Rodrigues:** Yeah, I'll check with our team too. Let me know what works.

**Elvis Goren:** I think we're good. See you, man. Bye.
