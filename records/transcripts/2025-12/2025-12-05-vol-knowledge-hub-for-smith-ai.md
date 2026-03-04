# Vol - Knowledge Hub for Smith.ai

<metadata>
date: 2025-12-05
time: 18:31 UTC
duration: 21 minutes
organizer: jo@growthx.ai
participants: Jo Kaminska, Volodymyr Popovych
fathom_recording_id: 106713701
fathom_url: https://fathom.video/calls/497249870
share_url: https://fathom.video/share/n6s77PqFHZFmDxBpK1kuaFJzoUvo44jh
source: fathom
enriched_on: 2026-03-01 00:00 UTC
</metadata>

---

## Summary

Jo and Volodymyr decided to build the Smith.ai Knowledge Hub as a new, separate Webflow collection rather than trying to fit it into the existing blog collection, which has technical constraints that prevent flexible template usage and custom URL structures. The team will implement 301 redirects from old blog URLs to the new Knowledge Hub pages while keeping article listings visible in the blog's category filters for seamless user discovery. Jo will document the URL structure and explain the technical rationale to internal stakeholders; Volodymyr will build the new collection and templates based on Figma designs.

---

## Context

Jo Kaminska (GrowthX) is working with Volodymyr Popovych, a Webflow developer, to define the technical architecture for Smith.ai's Knowledge Hub—a comprehensive resource center organized around topic pillars and subtopics. The hub is meant to provide in-depth content on call center technology topics, supporting both user education and SEO strategy. Jo and Volodymyr initially explored building the hub within Smith.ai's existing blog collection, but discovered that Webflow's technical constraints (single template per collection, reserved URL paths) made that approach unviable. This meeting focused on deciding whether to build static pages pulling from the blog CMS, or create an entirely new Webflow collection designed specifically for the hub's structure.

---

## Relevance

**To GrowthX Delivery:**
- Established the Knowledge Hub architecture as a separate Webflow collection, enabling independent template and design flexibility for pillar pages (black hero) vs. cluster pages (gray hero).
- Planned scalability from 6 pillars (initially) to up to 15 pillars, with 20+ cluster pages per pillar—this structure choice supports long-term content growth without CMS constraints.
- Identified SEO migration strategy: 301 redirects from existing blog URLs to new Knowledge Hub URLs, with old articles kept in blog for category filter discoverability.

**To CheckThat:**
- Knowledge Hub architecture demonstrates content organization patterns that could inform AI visibility and SEO strategy for other clients.

**To GrowthX Business Development:**
- Smith.ai engagement includes infrastructure/technical design consulting, signaling depth of GrowthX's Webflow and content strategy expertise.
- Client requires both design coordination (with Figma mockups) and technical implementation—opportunity to upsell design or ongoing optimization services.

---

## Overview

- **Decision:** Build the Knowledge Hub as a new, separate Webflow collection, abandoning the original plan to use the existing blog collection.
- **Rationale:** This is the only viable path to support the hub's distinct pillar/cluster page designs and URL structure, which the rigid blog collection template cannot accommodate.
- **Migration Plan:** Move existing hub-related content (e.g., "AI Calling System") to the new collection, then implement 301 redirects from the old blog URLs to preserve SEO.
- **Hybrid Discovery:** Keep old articles in the blog collection (but redirected) so they remain discoverable via the main blog's category filters, creating a seamless user experience.

---

## Key Topics

### The Problem: Webflow Constraints

  - The original plan to build the Knowledge Hub within the existing `blog` collection was blocked by Webflow's technical limitations:
      - **Single Template:** A CMS collection can only use one template for all its pages.
      - **Reserved URL Path:** The `/blog/` folder is reserved for the blog collection, preventing custom subfolders like `/blog/knowledge-hub/`.

### The Solution: A New CMS Collection

  - The team agreed to build the hub as a new, separate Webflow collection.
  - **Why it works:**
      - **Design Flexibility:** Enables the hub's unique pillar (black hero) and cluster (gray hero) page designs.
      - **Scalability:** Supports the planned growth from 6 to \~15 pillar pages and 20+ cluster pages per pillar.
      - **Clean CMS:** Keeps the content organized and manageable.

### Implementation Plan

  - **URL Structure:** Jo will define a new, SEO-friendly URL structure for the hub (e.g., `/knowledge-hub/pillar-name/article-name/`).
  - **Content Migration:**
      - Move content from existing hub-related blog articles to the new collection.
      - Implement 301 permanent redirects from the old blog URLs to the new hub URLs.
  - **SEO & User Experience:**
      - Keep the old articles in the blog collection (though redirected) so they still appear in the main blog's category filters.
      - This creates a seamless discovery path for users browsing the main blog.

---

## Action Items

**Jo Kaminska**
- Send URL structure to Volodymyr; then Volodymyr builds new collections/templates, migrates content, Slack updates Jo
- Brief Maddy re: hub plan, SEO/redirections

---

## Transcript
**Jo Kaminska:** Hi.

**Volodymyr Popovych:** Hi, Jo.

**Volodymyr Popovych:** How are doing?

**Jo Kaminska:** This meeting is being recorded.

**Jo Kaminska:** I'm good.

**Jo Kaminska:** How are you?

**Jo Kaminska:** Nice to meet you.

**Volodymyr Popovych:** Nice to meet you as well.

**Volodymyr Popovych:** I'm doing pretty fine.

**Volodymyr Popovych:** I'm excited to really get to know stuff about this project because really like I saw the stigma and like building stuff is not hard, but it's just like the concept of where we pull the content from and all that stuff is kind of the thing that's blocking me right now.

**Jo Kaminska:** Yeah, yeah, yeah.

**Jo Kaminska:** For sure.

**Jo Kaminska:** I think like you shared with us the files, right?

**Jo Kaminska:** Let me just check the state. Let me close tabs because I had a previous meeting and got a bit busy.

**Jo Kaminska:** Okay, so I'll share my screen with the two of you. So, we're starting with the content hub.

**Jo Kaminska:** So, um, first of all, I think, like, the project, like, constraints that we have are related to the technical things related to CMS, right?

**Jo Kaminska:** So, if I understand you correctly, if we have a collection in Webflow related to blog, then there is just one template that we can use on blog specifically.

**Jo Kaminska:** We cannot, like, swap templates based on a specific URL.

**Volodymyr Popovych:** Yeah, unfortunately not. Just one other thing you mentioned in Slack—you wanted to have these pages live under the blog folder, and that's kind of not possible with Webflow because we only have this blog collection.

**Volodymyr Popovych:** And since we have this CMS collection, it kind of reserves the blog folder, and we cannot put anything under that URL subfolder except the blog articles.

**Volodymyr Popovych:** If we're going for this URL structure, this is the only template we can use for these blogs. There's a way to display blog content on separate static pages, but that would require building and setting up those pages in a way that's more related to the designer stuff in Webflow.

**Jo Kaminska:** So it will not be as simple as just like adding a blog article right now.

**Volodymyr Popovych:** So, yeah, so I guess for me to understand this better, could you just like share your vision, your initial vision for what it was supposed to do?

**Volodymyr Popovych:** We'll see.

**Volodymyr Popovych:** I'll try to understand what's possible and whatnot.

**Jo Kaminska:** Yeah.

**Jo Kaminska:** So the general idea behind like content hub around like a receptionist knowledge base is that we would like to build a central hub for six different pillar pages.

**Jo Kaminska:** And pillar page is like a longer form content, like let's say over three.

**Jo Kaminska:** And then cluster page is something between 1,500, 1,800 word article that is like a subtopic of this like, you know, bigger pillar.

**Jo Kaminska:** And this concept is well explained through graphics.

**Jo Kaminska:** Because it's like, you know, SEO related.

**Jo Kaminska:** So like maybe HubSpot explains it through this graphic very well.

**Jo Kaminska:** So the model is as follows.

**Jo Kaminska:** So this is the pillar page.

**Jo Kaminska:** This is the central page, right?

**Jo Kaminska:** And then this page links to all these smaller pages that go in depth into the topic.

**Jo Kaminska:** So pillar page is more like general overview.

**Jo Kaminska:** And then it goes, you know, to thematically related but develops the thing.

**Jo Kaminska:** This is the exact way we are thinking about how the design works.

**Jo Kaminska:** So each one of these is a specific pillar, right?

**Jo Kaminska:** So if you click here, you basically have a pillar page displayed.

**Jo Kaminska:** And then this pillar page links to other blog posts related to Coldflow design and architecture.

**Jo Kaminska:** So that's why you had a design for the pillar that is a little bit different.

**Jo Kaminska:** I think when it comes to Figma, this is, I think, this is the right one.

**Jo Kaminska:** Yeah, so this is the navigational page.

**Jo Kaminska:** And then for the...

**Jo Kaminska:** So pillar page, you have a specific design, you know, with the black headline, let's say, the hero section.

**Jo Kaminska:** And then for a pillar page, you have this gray hero that kind of differentiates, you know, as you saw in the model.

**Jo Kaminska:** This is the black one, these are the gray ones.

**Jo Kaminska:** So that's why we were, like, we are introducing this structure of, this is the central hub.

**Jo Kaminska:** People want to read about call flow design, which is a central, like, this links to, you know, a very specific, um, what is call flow design and architecture, like why is it important?

**Jo Kaminska:** It's already published under blog, so this will be another discussion for us today, how to, like, tackle it.

**Jo Kaminska:** And then from this blog post, we are linking to the cluster pages, right?

**Jo Kaminska:** Okay.

**Jo Kaminska:** In doing internal links, so using these anchors, you know, to these smaller pages.

**Jo Kaminska:** So the smaller page, or like the more in-depth pages that are shorter, they are not displayed in any way here, but at the same time, you can see here that you have like key areas to explore, and then you can change the pillar, you know, to another pillar.

**Jo Kaminska:** So literally, if you are here, then the options here are the remaining ones.

**Jo Kaminska:** So call intelligence, and analytics should be here, and call routine and distribution should be, you know, like displayed below.

**Jo Kaminska:** Okay.

**Jo Kaminska:** And then, you know, when it comes to specific cluster, then like linked related topics, so like other topics in the cluster.

**Jo Kaminska:** So let's say other cluster, like other smaller pages.

**Volodymyr Popovych:** Okay.

**Volodymyr Popovych:** Okay.

**Volodymyr Popovych:** I'm trying to wrap my head around about, with like, how to...

**Volodymyr Popovych:** Okay.

**Volodymyr Popovych:** We do this with our current blog structure because what I understand here is that there's this one page that is supposed to be like this main category article page.

**Volodymyr Popovych:** And then the second page is like the sub-article, if can say that.

**Volodymyr Popovych:** But basically the content on those pages you would imagine to be pulled from the blog collection.

**Volodymyr Popovych:** Is that correct?

**Jo Kaminska:** Yeah, so like this is ideal scenario, I think, considering like the, considering that we already started publishing, so you can see here, you know, this is already published like under AI calling system, right?

**Jo Kaminska:** So, uh,

**Jo Kaminska:** This is the one of, like, this is the one of content pieces that belongs here to this one.

**Jo Kaminska:** And, yeah, like, do you see any way currently that, like, would let us have this central hub and still, like, I mean, maybe just reframe the question.

**Jo Kaminska:** Is there any way of pulling the already published content on blog to the template?

**Jo Kaminska:** Or is it only possible with changing the URL structure?

**Volodymyr Popovych:** Well, it's kind of possible, but not ideal.

**Volodymyr Popovych:** So let's say we have these six pillar pages.

**Volodymyr Popovych:** I would say that we could just have them built as static pages since we're only having six of them.

**Volodymyr Popovych:** Is that correct?

**Volodymyr Popovych:** Just six of them.

**Jo Kaminska:** Yeah, but maybe in the future we'll have more.

**Jo Kaminska:** So that's something, you know.

**Volodymyr Popovych:** Not like a hundred pages more, right?

**Jo Kaminska:** Not like a hundred pages.

**Jo Kaminska:** No, like pillars are usually like, this is the bigger group.

**Jo Kaminska:** So maybe up to, let's say, 15.

**Volodymyr Popovych:** Okay.

**Volodymyr Popovych:** Okay.

**Volodymyr Popovych:** So this, I think we could build a static pages and just pull content from the CMS.

**Volodymyr Popovych:** But then again, and let me share my screen this time.

**Volodymyr Popovych:** And then again, what I'm thinking, so we could have this page as a static page.

**Volodymyr Popovych:** We could pull this content from the CMS.

**Volodymyr Popovych:** But, and this content blog, this exists in the blog collection.

**Volodymyr Popovych:** But what about these sections?

**Volodymyr Popovych:** This does not exist in the blog collection.

**Jo Kaminska:** Is that correct?

**Jo Kaminska:** No, don't know.

**Jo Kaminska:** Like the blog.

**Jo Kaminska:** Collection doesn't have this glossary of times, or this was dedicated to this hub.

**Volodymyr Popovych:** Okay.

**Volodymyr Popovych:** So I would think that building this as a static page would be a better way of tackling this.

**Volodymyr Popovych:** And yeah, I would be able to just pull content from these specific blogs on those static pages.

**Volodymyr Popovych:** If it's just building a couple of those pages, it's not that problematic. It's just building them in a way that would be sustainable in the future for adding more content. Since we're not having that many pillar pages, I think it's pretty sustainable to just have them as static pages, and I'll be able to help you add more in the future.

**Volodymyr Popovych:** And this is not something that is going to be added at a new page like every week or so.

**Volodymyr Popovych:** So, well, about these guys, this is probably a more complex question because we're going to have many more of these pages, right?

**Volodymyr Popovych:** Like for each category.

**Jo Kaminska:** So, okay.

**Jo Kaminska:** So, I'll maybe reset this conversation to something that I was thinking about what to do instead.

**Jo Kaminska:** Because if we started from like the ideal path that you would take to build anything, we are not talking about blog, but we are talking about new hub, right?

**Jo Kaminska:** Then, can I share my screen to lead you through?

**Jo Kaminska:** So, let's say that this will be built as a new collection.

**Jo Kaminska:** Like, I don't know, the hierarchy probably is that, you know, this is a central page and then under this, the whole hub lives.

**Jo Kaminska:** And then we would just make redirections.

**Jo Kaminska:** So, let's say this is AI calling system, this was already published on blog, and there are already many of these published.

**Jo Kaminska:** So, we already started publishing the, you know, things that are under this hub, just because, like, we wanted to, you know, to check the performance, et cetera.

**Jo Kaminska:** But if we make redirections, I can come up with a taxonomy structure for the new hub. So I could imagine something like `/knowledge-hub/`, the subfolder would be like a pillar name, and then the URL stays as is, right?

**Jo Kaminska:** But it would be a redirection.

**Jo Kaminska:** Then would it be sustainable to literally build this hub as a new collection, make the redirections from all these pages to the new collection?

**Volodymyr Popovych:** And when we make the redirection, we're basically getting rid of those blog pages.

**Volodymyr Popovych:** So we'll basically move the content to a new collection.

**Jo Kaminska:** Yeah, exactly.

**Volodymyr Popovych:** Yeah, that seems more feasible, actually, because, yeah, like the main constraint was just keeping all of this to the existing blog collection.

**Volodymyr Popovych:** And that was really the main constraint.

**Volodymyr Popovych:** We're doing this as a separate collection. We have much more flexibility in terms of what we can have for each of those pages and content.

**Volodymyr Popovych:** I can create a new collection and add different fields and connections between collections that would work better with this design.

**Jo Kaminska:** So that is possible.

**Jo Kaminska:** Okay.

**Jo Kaminska:** Just a quick question.

**Jo Kaminska:** If I go to company blog and I see these categories, can we still link?

**Jo Kaminska:** Because you see that these categories, AI calling system, call flow design, call routing and distribution, they're all from this hub, right?

**Jo Kaminska:** Like, I would like to see that, like, people who are visiting blog, they can actually, like, you know, through...

**Jo Kaminska:** Okay.

**Jo Kaminska:** Blog category, they can also find this content.

**Jo Kaminska:** Is it possible to keep this and display still something that is not under blog?

**Jo Kaminska:** Or is it just too much of a lift and we should remove and separate the blog from like Knowledge Hub?

**Volodymyr Popovych:** It's possible we would have to keep those blog articles probably in the blog collection and just have them redirected to the Content Hub pages.

**Jo Kaminska:** That's how I would do it. So this will be displayed, but the URL would be in a different subfolder.

**Volodymyr Popovych:** Yeah, yeah.

**Jo Kaminska:** Okay.

**Volodymyr Popovych:** Yeah, perfect.

**Jo Kaminska:** I think like this is the best route just because I think like, you know, as you mentioned, creating six to 15 pillars is not a problem.

**Jo Kaminska:** But then under these pillars, we have like 20 plus probably content pieces.

**Jo Kaminska:** I want to take care of the user experience and how tidy the CMS is. I think this strikes the best balance between design and technical constraints.

**Volodymyr Popovych:** Yeah, so I think I have what I need to start working on it.

**Volodymyr Popovych:** I mean, what I probably need from you is just the URL structure that you would imagine for this.

**Volodymyr Popovych:** That it's not going to be under blog, but something different.

**Volodymyr Popovych:** I'll start building out these pages in this new collection way that we came up with.

**Volodymyr Popovych:** And we can then touch base.

**Volodymyr Popovych:** Maybe not next week.

**Volodymyr Popovych:** I can just slack you with what I have built.

**Volodymyr Popovych:** And if there's any confusion or anything, we can.

**Volodymyr Popovych:** Meet again.

**Volodymyr Popovych:** If not, we can probably just go ahead and work on that.

**Jo Kaminska:** Yep.

**Jo Kaminska:** I have a call with Maddy next week, so I can communicate it to her as it requires some SEO explanation, et cetera, and she always wants to know the details.

**Jo Kaminska:** So you can leave the tech why behind to me, so I'll explain to her next week.

**Jo Kaminska:** But yeah, what I hear from you is this is the best way to handle when it comes to technical and how the setup works.

**Jo Kaminska:** Do you have anything else to share that I should share with her regarding this?

**Volodymyr Popovych:** I don't think so.

**Volodymyr Popovych:** The big thing is the website is built within Webflow ecosystem, and it has its constraints.

**Volodymyr Popovych:** Like, some of them are, like, really stupid when you think about them.

**Volodymyr Popovych:** But yeah.

**Volodymyr Popovych:** It's just they're there, and we have to take them into account.

**Volodymyr Popovych:** And for this content hub, I think just building separate collections would be the best way of just handling them.

**Volodymyr Popovych:** And having this separate content hub that people can go through and look for content and the search engines and all those other AI engines can go through and index all that stuff.

**Volodymyr Popovych:** I think that's a good way of handling this.

**Volodymyr Popovych:** Yeah, it'll be much more clear when I have those collections built.

**Volodymyr Popovych:** But my main constraint was just having all of those designs integrated with the current collection. Now that we're creating a new collection, I have much more flexibility.

**Jo Kaminska:** Uh, cool.

**Jo Kaminska:** So, I think like to make also the redirection smooth, we can catch up one week or the other.

**Jo Kaminska:** Maybe it will be closer to the third week of December.

**Jo Kaminska:** It depends on how we progress with work, but we can also catch up in January, beginning of January, to actually start redirections.

**Jo Kaminska:** On my SEO end, I want to make sure we redirect them all at once with 301s—permanent redirects—and that they're taken down from the blog so there's no duplicate content with the redirected pages.

**Jo Kaminska:** So we have, like, cleaned up the space.

**Volodymyr Popovych:** Yeah, yeah, that sounds good.

**Volodymyr Popovych:** That's totally possible.

**Volodymyr Popovych:** We'll get that done.

**Jo Kaminska:** Okay, okay, perfect.

**Jo Kaminska:** Thank you so much for your time and for explaining all of this.

**Volodymyr Popovych:** Likewise.

**Jo Kaminska:** Have a good day. Bye-bye.
