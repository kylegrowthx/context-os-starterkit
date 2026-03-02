# GrowthX <> N-able PMM Sync

<metadata>
date: 2025-11-17
time: 21:04 UTC
duration: 44 minutes
organizer: Aida Knežević
participants: Andi Bailey (GrowthX), Aida Knežević (GrowthX), Erik O'Brien (GrowthX), Andrew Beyer (N-able), Nicholas Smarrelli (N-able), Joe Kern (N-able), Jen Thompson (N-able), Garret Stegeland (N-able), Stuti Jhunjhunwala (N-able)
fathom_recording_id: 102281096
fathom_url: https://fathom.video/calls/475191812
share_url: https://fathom.video/share/djxUDKFwgzxj9ayqCBPB6yKFYK9EpUNz
source: fathom
enriched_on: 2026-03-02 12:30 UTC
</metadata>

---

## Summary

GrowthX and N-able identified that AI-generated blog content was factually inaccurate due to insufficient product detail in foundational artifacts (Company Context doc). The teams agreed on a two-part remediation: PMMs will provide high-level product overviews for the Company Context doc and curate deep-dive product documentation by end of week, while GrowthX will create a dedicated Product Artifact for AI generation and update permissions in the Content OS (Airtable) to enable collaborative topic review starting next week.

---

## Context

N-able is a software company operating in the IT management and automation space. GrowthX was engaged in month 7 of an 8-week strategic sprint to build out N-able's organic content engine and reduce reliance on paid search. The engagement aims to increase visibility in search engines and AI search results (e.g., ChatGPT, Perplexity, Claude) through educational, SEO-optimized blog content. The immediate blocker: early drafts were flagging accuracy issues (e.g., describing N-able's offering as "incident response remediation" when it's actually an "AI SOC agent"), revealing gaps in the product context provided to the AI generation system.

---

## Relevance

**To GrowthX Delivery:**
- Artifact quality directly impacts draft accuracy. Shifting responsibility to client PMMs for deep-product input (via curated docs) rather than GrowthX guessing from competitor research reduces edit-heavy cycles.
- Two-tier input model (high-level Company Context + deep Product Artifact) is a repeatable, scalable pattern for future clients with product-heavy services.
- EOW deadline (end of 2025-11-21) is tight but critical—delays push content publishing into week 8, compressing the validation cycle.

**To GrowthX Business Development:**
- N-able's PMM team (Joe Kern, Jen Thompson, Garret Stegeland, Stuti Jhunjhunwala) is engaged and accountability is clear, signaling account health and willingness to invest effort.
- Content OS (Airtable) access for the N-able team enables collaborative topic review next week, de-risking topic-market fit before drafting.
- Successful resolution of accuracy issues this week sets up for expanded scope (broader topic production, refinement loops) post-sprint.

**To CheckThat:**
- Conversation underscores importance of accurate product context for LLM citations. N-able's content will directly compete in AI search results (ChatGPT, Perplexity, Claude) for IT automation and security topics.

---

## Overview

- **Problem:** Content drafts are inaccurate (e.g., "incident response remediation"), requiring heavy PMM edits. This stems from GrowthX's foundational artifacts lacking sufficient product detail.
- **Solution:** PMMs will provide detailed product input by EOW. GrowthX will use this to update the `Company Context` doc and create a new, deep-dive `Product Artifact` for AI generation.
- **Process:** The immediate priority is fixing the input artifacts. PMMs will review blog topics in the `Content OS` (Airtable) starting next week.

---

## Key Topics

### The Problem: Inaccurate Content Drafts

  - The "incident response automation" draft was flagged as inaccurate because N-able's offering is an "AI SOC agent," not a remediation tool.
  - This inaccuracy stems from the foundational artifacts (`Company Context`, `Audience Personas`) used for AI generation being too shallow on product details.
  - **Goal:** Shift from paid search to organic traffic by publishing educational, SEO-optimized content. This content must be factually correct to build trust and drive results.

### The Solution: A Two-Part Input Process

  - PMMs will provide two types of input to fix the accuracy issue:
    1.  **Update `Company Context` Doc:** Add a high-level (approx. 0.5 page) overview for each product.
    2.  **Share Deep-Dive Docs:** Provide internal materials (e.g., "get to know our products" folder, "resiliency" docs) for a new, dedicated `Product Artifact`.
  - **Rationale:** This two-part approach keeps the `Company Context` document concise while providing the AI with the deep, accurate product knowledge needed for generation and fact-checking.

### The Tool: Content OS (Airtable)

  - The `Content OS` is the central hub for managing blog topic ideas.
  - **Purpose:** PMMs will use it to approve topics, provide strategic angles, and prioritize ideas.
  - **Key Fields:**
      - `N-able Feedback`: For PMM comments (permissions will be updated for public visibility).
      - `Target Keyword`: The term the post is optimized for.
      - `Volume`: Search volume, indicating traffic potential (high volume = broad top-of-funnel, low volume = specific ICP).
  - **Process:** PMMs will review topics starting next week, after the input artifacts are updated.

---

## Action Items

**Jen Thompson (N-able)**
- Review incident response automation draft; comment on product mentions only

**Aida Knežević (GrowthX)**
- Email Joe Kern, Jen Thompson, Garret Stegeland, and Stuti Jhunjhunwala: Send Notion (Company Context/Audience Personas) and Airtable (Content OS) links
- Request curated product documentation (top 3-4 files per product, e.g., "Get to Know N-able [Product]")
- Set end-of-week (2025-11-21) deadline for updates

**Andi Bailey (GrowthX)**
- Coordinate with Yusef to enable public/shared comments in Airtable Content OS so all PMMs can see feedback without drilling into nested comment threads

---

## Transcript
**Aida Knežević:** Hey there.

**Aida Knežević:** Hey, Stuti.

**Aida Knežević:** Sorry to keep you waiting.

**Aida Knežević:** We did not realize there was a meeting lobby, so.

**Erik O'Brien:** All right, Stuti, Andrew, Garret.

**Erik O'Brien:** Anybody else we're waiting for?

**Erik O'Brien:** Yeah, think Joe and Jen should be coming in.

**Stuti Jhunjhunwala:** We just finished another meeting.

**Stuti Jhunjhunwala:** Okay.

**Nicholas Smarrelli:** Cool.

**Nicholas Smarrelli:** Looks like we got everybody now.

**Nicholas Smarrelli:** All right.

**Nicholas Smarrelli:** Thanks, PMM team, for joining with us here.

**Nicholas Smarrelli:** I know there's some feedback in terms of blog quality that we want to get to, and we have the folks over here on the GrowthX side that will...

**Nicholas Smarrelli:** Certainly dive into some questions here, but Aida, Erik, do you all want to kick it off and get us started here?

**Stuti Jhunjhunwala:** Hey, guys, can you please step back and maybe refresh everybody's memory on what the project is all about and what we are trying to collectively achieve?

**Stuti Jhunjhunwala:** So it'll be great to hear from you guys from like the start.

**Stuti Jhunjhunwala:** Absolutely.

**Stuti Jhunjhunwala:** Thank you.

**Erik O'Brien:** So, yeah, for the growthx side, so we are really here to help enable, kind of grow their content engine.

**Erik O'Brien:** So we do that through multiple different venues, but for now we're focused really on blog content.

**Erik O'Brien:** And so really we take an audience first approach of kind of understanding what topics your audiences are either talking about or searching for, and so part of our process.

**Erik O'Brien:** is to come up with what we call artifacts that are called the company context, so how do we speak about your company and the products that you serve to the market, the writing guidelines, which kind of shape the tone and voice of the content that we generate, then audience personas, basically the people that you serve.

**Erik O'Brien:** And so we've started the engagement with kind of a deep dive into both, you what's driving this engagement now, really what we heard from the team was kind of looking to backtrack or not backtrack, but kind of have a less reliance on paid search.

**Erik O'Brien:** And so how do we start to boost more organic and web traffic, paid search is kind of strongly capturing demand, but again, really trying to remove the need for paid search.

**Erik O'Brien:** And so we really kind of focused on building a content strategy around some topics.

**Erik O'Brien:** clusters that we can share with you guys or walk through today, but really, again, kind of focused on what are the jobs to be done for enable products to kind of serve your customers.

**Erik O'Brien:** Sorry, go ahead, Stuti.

**Stuti Jhunjhunwala:** And how do you prioritize the topics if you can walk through the decision or the data behind choosing which topic to prioritize?

**Stuti Jhunjhunwala:** Yeah, I can help answer this.

**Aida Knežević:** Yes, so I linked our content strategy in our chat.

**Aida Knežević:** So the way we develop content strategies, so primarily we are here to grow enable visibility in SEO, so organic traffic, and also increase your LLM visibility.

**Aida Knežević:** From the data that we see with clients that we've worked with so far, customers with...

**Aida Knežević:** So we're we're working so so we're we're so so

**Aida Knežević:** Bigger content engines, meaning they publish more content on their blog.

**Aida Knežević:** Educational content, so that means the product can be mentioned in the content, but the primary goal is to produce like educational content, which is slightly different from what the blog has been focused on in the past.

**Aida Knežević:** So, for example, when we're analyzing your existing content, you have like almost 800 pieces of content on your blog, but a lot of it is product-centric, which is great, and it fulfills a specific purpose for your audience.

**Aida Knežević:** However, what GrowthX is here to do is publish content that is optimized for search engines and AI search so that we can drive more visibility in those areas, and this is the type of growth that compounds over time.

**Aida Knežević:** So the more that we publish, you get more traffic to your website, and your visibility increases in AI search.

**Aida Knežević:** That's what I wanted to say.

**Aida Knežević:** In the beginning is that the companies that we work with that have more educational content published on their blogs, they get higher citations from LLMs like ChatGPT, Perplexity, Claude, et cetera.

**Aida Knežević:** The way we pick the topics, we take kind of a multi-pronged approach.

**Aida Knežević:** So we analyze your top competitors, and we also analyze what are your goals, why did you come to us in the first place, and we also take into account the audience personas that we develop in collaboration with your team, and we focus on really, okay, what are their primary pain points, what are their jobs to be done.

**Aida Knežević:** We analyze the competitor content because we want to understand what are the top content opportunities that we need to capture from your competitors, like increase your overall visibility.

**Aida Knežević:** And not all of those, like, ideas are going to be relevant for your company, which is why we also factor in, okay, what are your current priorities and all.

**Aida Knežević:** Sorry, go ahead.

**Aida Knežević:** Sorry, just have a quick question regarding this.

**Jen Thompson:** like, right, there's the current one around the incident response automation.

**Jen Thompson:** Right.

**Jen Thompson:** That is stuck in review with me.

**Jen Thompson:** But part of the reason why it's been stuck with me is because, like, I don't think that we do incident response remediation.

**Jen Thompson:** Like, what we're doing from an automation standpoint is more of, like, an AI SOC or an AI, like, SOC agent than the incident response.

**Jen Thompson:** So, like, should I be reviewing it, like, in the sense of, like, is the content accurate or does the content relevant to what we're doing or both?

**Jen Thompson:** All right.

**Aida Knežević:** So, I think that's a great question.

**Aida Knežević:** When we are suggesting topic ideas as part of these clusters, on that's on

**Aida Knežević:** We want the majority of them to be able to map in some way to your product.

**Aida Knežević:** Not all of them are going to map exactly to your product, so they might not be, you know, you might not have a product, like you said, like that directly solves a specific pain point.

**Aida Knežević:** However, it does allow us to get in front of an audience that belongs to your broader audience.

**Aida Knežević:** So, in this case, reviewing that blog post, if there are any N-able mentions, we would like for you to still review it to make sure that it's being mentioned in the right context so that we're not misrepresenting the features of the product.

**Aida Knežević:** But when we typically get product teams to review content, we, you know, the best use of your time, so you're not like reviewing, you know, entire like 2000 word blog posts, is to just focus on the product mentions.

**Aida Knežević:** And if you think that mentioning...

**Aida Knežević:** The product in a specific blog post doesn't make sense because it could be misleading.

**Aida Knežević:** That is a valuable piece of feedback for us.

**Aida Knežević:** So, yeah, not all of the ideas are going to map 100% to the product, but we want to make sure that the majority of them do.

**Aida Knežević:** And in the cases where they don't, we want to, like, make sure that we're not misrepresenting the capabilities.

**Aida Knežević:** Thank you.

**Aida Knežević:** Aida, have they seen the content OS?

**Andi Bailey:** Because that might be a good way to think about, like, the way that we're clustering everything and structuring the approvals process before we even get started.

**Andi Bailey:** Yes.

**Aida Knežević:** Yeah, sure.

**Aida Knežević:** Stuti, go ahead while I pull up the content OS.

**Stuti Jhunjhunwala:** In the similar vein to Jen's question, would it also make sense to sort of align on topics?

**Stuti Jhunjhunwala:** Like, you know, there could be topics like that have zero intersection with.

**Stuti Jhunjhunwala:** be topics that,

**Stuti Jhunjhunwala:** Enable, and should those, like, should we discuss that prior to you guys going and creating that blog, or are you thinking that even if there's zero connection to enable, we still want to have that topic?

**Stuti Jhunjhunwala:** Right, okay.

**Aida Knežević:** Yeah, so I think it would be helpful to get insights from at least, you know, one person on the product team when it comes to these topics, because we want to be able to make sure that we're prioritizing the topics that are most relevant to your product.

**Aida Knežević:** So, not to say that, like, incidence response automation isn't important, but I'm sure that there are other topics that would be more relevant to your product, and as such, we should prioritize them.

**Aida Knežević:** So, the way that, so we have this, like, content OS setup, which is an Airtable base with the topic clusters laid out.

**Aida Knežević:** And then each cluster has multiple blog post ideas under it.

**Aida Knežević:** And where we would love to get your input even before we send you a draft is, you know, going in.

**Aida Knežević:** There are a couple that have been already approved to start by the marketing team.

**Aida Knežević:** But, for example, into ones that are still, if you could switch to buy status, sorry, we can find ones that are still in considering.

**Aida Knežević:** So they haven't been reviewed.

**Aida Knežević:** I can also group them by topic clusters so that you can see like individual clusters under each status.

**Aida Knežević:** And that's where we would love to get your thoughts on, okay, like, this is a great idea.

**Aida Knežević:** Here's like, you know, you could just tell us, okay, we want to do this.

**Aida Knežević:** Or you could tell us, like, this is a great idea.

**Aida Knežević:** We should be talking about this product and specifically like this functionality, which really like is a huge differentiator for us.

**Aida Knežević:** you.

**Aida Knežević:** Thank

**Andi Bailey:** Yeah, but taking, I do want to add, just taking a step back to the way that we think about this content OS and the way that we go after the keywords, while maybe not everything is directly relevant to your product offering, we're looking at kind of search volume.

**Andi Bailey:** And if you're thinking about top of funnel going as wide as you can with the aperture, we want to have, if people are searching in this space and you want to build awareness and kind of funnel them through a flow to really specific parts of your product, like we do want to have topics that people might be searching for that are relevant to the space, even if Enable isn't, like offering the exact product solution, as long as we can tie it back to something that Enable would offer that would be valuable to somebody who's searching for something like that.

**Stuti Jhunjhunwala:** Makes sense.

**Stuti Jhunjhunwala:** And one last question.

**Stuti Jhunjhunwala:** Really on the input, so what all, I mean, I've of course seen the three input required documents, which had like blobs on maybe what our products do, etc.

**Stuti Jhunjhunwala:** But what other product level data have you fed your AI engine?

**Stuti Jhunjhunwala:** So we use, we use the product deep dive session, the transcript.

**Aida Knežević:** We use insights from that conversation to update the company context and the audience personas.

**Aida Knežević:** We also do, we use perplexity research to just research like the, for the, it's like the base of the company context and the audience personas.

**Aida Knežević:** And then we enrich it with further input, like the kickoff call, the product deep dive conversation.

**Aida Knežević:** And then any further feedback that we get from the team, we also went back in and.

**Aida Knežević:** Adjusted the artifacts.

**Aida Knežević:** I already told Nicholas and the marketing team that we can create a separate artifact that would just serve as a single source of truth on just a product.

**Aida Knežević:** So we could lay out the three main products in that artifact with just a bullet list of, okay, what are the features?

**Aida Knežević:** How do these features benefits your audience?

**Aida Knežević:** Like what are the specific results that they could be expecting by using these products?

**Aida Knežević:** So that's something that we could also incorporate into our article generation pipeline to make sure that the product mentions are as accurate as possible.

**Aida Knežević:** Makes sense.

**Aida Knežević:** I I think we still need a lot more work on those, though.

**Joe Kern:** Yeah, yeah.

**Joe Kern:** Like, in general, like, before we start creating content, it would be good to make sure that we get those nailed down.

**Andi Bailey:** Do you guys have additional product documentation that you can share with us that we can feed into that and start to refine?

**Andi Bailey:** Yeah, and I was, yeah, so there's a couple things.

**Joe Kern:** One, we can go through your documents, right, the company contacts and audience personas, and we can provide comments, more detail, et cetera.

**Joe Kern:** We've got other documents that we could supply to you that would actually help build story and foundational message for each of those products.

**Joe Kern:** And we should probably think about sharing that.

**Joe Kern:** And then the last part I was thinking was, I don't know what capabilities your AI tooling has, and we could check with ours.

**Joe Kern:** So we've got some AI tools that you might even be able to query and say, hey, like, you know, most of the time our product documentation, right?

**Joe Kern:** Like, we can give you all the product documentation user guides where you could crawl those and get access.

**Joe Kern:** A lot of them are, like, three, four.

**Joe Kern:** Or, you know, let's say directories of the web deep.

**Joe Kern:** So I don't know if your AI tool can crawl that deep or whether it just sticks to like the shallow two directories, right?

**Joe Kern:** But if you're able to hook up to another AI component, maybe we could do that too.

**Joe Kern:** I don't know.

**Joe Kern:** Yeah.

**Andi Bailey:** So the way that we build these workflows is we're generating that content and then querying kind of the output that we have in that like product documentation as sort of a check layer.

**Andi Bailey:** We can go pretty deep.

**Andi Bailey:** I don't know if we can go that deep.

**Andi Bailey:** it would be, I think, ideally, if you can send us things, we can adjust them and put them into different reference points in the AI saying like, this can be part of the fact check or go through this documentation rather than trusting that it will query different sections as we're going.

**Andi Bailey:** And do you think user guides are a good tool for that?

**Joe Kern:** Or do you think it's got a lot of fluff in there that might?

**Joe Kern:** Yeah, would say we don't go, yeah, yeah, exactly.

**Andi Bailey:** I think, like, user guides were probably, like, if you have kind of more of your internal documentation, that would be better.

**Andi Bailey:** Yeah.

**Aida Knežević:** Okay.

**Aida Knežević:** I think, yeah, any internal documentation would be helpful.

**Aida Knežević:** think now, if we don't have any other questions, I think we, Erik, we could go through the company context first, and then move on to the personas.

**Aida Knežević:** Yep.

**Aida Knežević:** All right.

**Erik O'Brien:** So, this one you guys should have, looks like, Joe, you're in here.

**Erik O'Brien:** So, you guys have access to this.

**Erik O'Brien:** think, this is,

**Erik O'Brien:** Again, one of the key artifacts that we use for content generation, the one Aida was referencing is a new one that we would create.

**Erik O'Brien:** So on top of these core three, we could create that specific for your products, which we would generate based off the documents that you share.

**Erik O'Brien:** But I think from the top level, if there's anything in this company context, Doc, that you guys feel is either too shallow or even kind of unnecessary to include here, we would love to kind of have your guys' thoughts on any of these pieces.

**Erik O'Brien:** I know it's quite a bit to read, so we can also, again, share those things.

**Erik O'Brien:** don't think you're going to, Erik, I don't think you're going to get that on this call.

**Joe Kern:** I think what we need to do is say, here's the prescriptive homework that we need to do by a date, right?

**Joe Kern:** Like, I think that would help everybody and say, okay, you know.

**Joe Kern:** We all need to go to a certain spot, go through this content and check it off, right?

**Joe Kern:** Like that's what's going to move the needle.

**Stuti Jhunjhunwala:** And I would also say let's get the product-specific content prioritized because some of the persona and all of that like is higher level at enable stuff.

**Stuti Jhunjhunwala:** So, again, if we are trying to break it down and prioritize the work that we want PMMs to do, would say making sure that whatever is the additional few documents that we want to share.

**Stuti Jhunjhunwala:** again, Joe, I would keep it not going super deep because, again, we could get lost versus sharing like few critical documents and updating the basic stuff on the products as maybe the first action item.

**Stuti Jhunjhunwala:** And I guess if there's another one is like maybe even aligning on X number of, you know, whether it's two, three top topics that we want to say yes.

**Stuti Jhunjhunwala:** So from a blog perspective.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So I think of the company context, the product overview is definitely the section I would want PMM to take a look at so I can tag you guys in this.

**Erik O'Brien:** And then I would say for each product itself, we would want any internal documentation that you have that talks about the product key capabilities, features.

**Erik O'Brien:** Yeah.

**Stuti Jhunjhunwala:** And probably start there.

**Stuti Jhunjhunwala:** Hey, guys, can I, Joe, Jen, and Garrett, we just created a folder of, you know, getting to know our products for somebody joining enable.

**Stuti Jhunjhunwala:** Would you think that folder would be really valuable?

**Stuti Jhunjhunwala:** Like just the content that we collected in there?

**Stuti Jhunjhunwala:** That's going to link to all sorts of stuff, right?

**Joe Kern:** There's going to be like enable you courses and not all of it will be easily shareable.

**Joe Kern:** But what we can share, sure.

**Stuti Jhunjhunwala:** Yeah, that and in that folder, if you also want to add, like, maybe a couple more pieces, like, is that a good starting point rather than creating new work?

**Stuti Jhunjhunwala:** Because that's literally like, hey, get to know our products if you know nothing about us.

**Erik O'Brien:** Yeah, would say from our perspective, that would be helpful.

**Erik O'Brien:** Understanding that some of it will link out to other resources that will probably go a little bit deeper.

**Erik O'Brien:** But as long as we have kind of that top level view of, like, what somebody new to enable would be trying to learn about each product, I think that's at least a good starting point.

**Stuti Jhunjhunwala:** And one other thing, like, guys, even those resiliency documents that were written, you know, those word docs, what do you guys think as, additional resources?

**Stuti Jhunjhunwala:** Yeah, that's what I was thinking would be really helpful, right?

**Joe Kern:** Like, so we have that brand better together, and then you have each, like, here's the top-level brand, but then it flows into a particular BU, right?

**Joe Kern:** Like, those story documents, that kind of layer each other.

**Stuti Jhunjhunwala:** So, guys, can I ask, like, so do we send you guys the documents, or do we, do you want this notion updated?

**Stuti Jhunjhunwala:** Because, like, and what's the level of depth?

**Stuti Jhunjhunwala:** Because the notion paragraphs are really small, that, you know, it's like two paragraphs versus, like, what we are talking about has, like, a lot more richness.

**Stuti Jhunjhunwala:** So, what do you guys want?

**Erik O'Brien:** Yeah, I would say we would take the documents, because we want to keep the company context kind of a cohesive view of the company, instead of going super deep on the products themselves.

**Erik O'Brien:** And then we can make updates to the company context based off what we learned from those product documents, and then create the separate fourth artifact that's just specific and go deep on the products themselves.

**Aida Knežević:** Does that sound right, Aida?

**Aida Knežević:** Yeah, yeah, I think, yeah, we can do more in-depth documentation.

**Aida Knežević:** Like, it's not an issue for us if, you know, you send us a slide deck.

**Aida Knežević:** We can use that for the fourth artifact that we're going to create about the product.

**Stuti Jhunjhunwala:** But, so, I guess, just to get clear, like, you still want the Notion company context page with the product overviews updated, correct?

**Stuti Jhunjhunwala:** Yes, yes, we do need, that's a, the company context should be updated, yes.

**Aida Knežević:** Okay, so there are two asks for us, like, go into the product section.

**Stuti Jhunjhunwala:** In that Notion file, update it, and then send a collection of get-to-know ABC product documentation.

**Aida Knežević:** Yes, so to kind of give you an overview of where everything is in Notion, so client docs, files, and shared context, you can drop, you can upload files here, or you can drop the links.

**Aida Knežević:** Just make sure to share the access with team at growthxlabs.com.

**Aida Knežević:** I can drop that in the chat, that email in the chat.

**Aida Knežević:** So you can upload any files here.

**Aida Knežević:** And then for the company context, this is where we can, you can drop your feedback.

**Aida Knežević:** Joe has already left feedback that we've implemented, so we can, you can leave any additional comments.

**Aida Knežević:** You can also use the suggesting mode to kind of make changes while-

**Aida Knežević:** Allowing us to see the changes that you've made.

**Nicholas Smarrelli:** I'm also happy to project manage anything rather than you all needing to remember who to send emails to, Stuti, Joe, Jen, Garrett, if you want to send stuff to myself or Andrew Beyer, we can coordinate everything back and forth between our teams.

**Joe Kern:** Yeah, I think that would be great.

**Joe Kern:** You know, I work really well through guilt.

**Joe Kern:** So if you give me a date, I'll try to finish.

**Joe Kern:** But, you know, I did a first pass on the company context, but it wasn't like a deep dive because there's so much there that it's been impossible.

**Joe Kern:** So I think this just needs dedicated time.

**Stuti Jhunjhunwala:** Let's break it down.

**Stuti Jhunjhunwala:** So we're saying first phase, let's go update what is in the company context.

**Stuti Jhunjhunwala:** Let's give a reasonable date.

**Stuti Jhunjhunwala:** What do we think?

**Stuti Jhunjhunwala:** And I'm assuming you want like shot.

**Stuti Jhunjhunwala:** Go.

**Stuti Jhunjhunwala:** You

**Stuti Jhunjhunwala:** You literally have, like, one page of products-level stuff in Bullets, that's what you're wanting, right, on the company context?

**Stuti Jhunjhunwala:** Yes.

**Stuti Jhunjhunwala:** So we're not looking for crazy details, just highest level, like half a page worth of content, like, when do we think it's real to do this?

**Joe Kern:** Is that a question for us?

**Joe Kern:** Well, I think it'd be that little bit of, that block of text, right, the key ones, but then if we wanted to have deeper descriptions and more content, we can then add a file to it or add a document that goes along with it.

**Joe Kern:** Yep.

**Stuti Jhunjhunwala:** So, Joe, yeah, the first question, yeah, let's update this with the critical capabilities and be true, and then ask two would be, hey, give your top three files or four files about get-to-know ABC product.

**Stuti Jhunjhunwala:** so, so, so, so, so, so, so, so, so, so.

**Stuti Jhunjhunwala:** It's and they create a fourth page or a fourth context.

**Joe Kern:** Right, and then I think maybe as a group, Stuti, we come together on the personas and ideal customers and just review those to make sure that.

**Stuti Jhunjhunwala:** Yeah, no, 100% agree with that, Joe, but I would say that let's, so I would say persona, let's prioritize, and I'll ask him also to take a lead a little bit on the persona piece.

**Stuti Jhunjhunwala:** But let's get, make sure that the product piece is done, because everything, like if you're getting a blog that misquotes a product, that's a bigger problem than the persona being slightly not as detailed or whatever.

**Stuti Jhunjhunwala:** Got it.

**Stuti Jhunjhunwala:** Yeah, I don't think the persona stuff will take very long.

**Joe Kern:** It's just like, hey, as a group, we review it, sign off, say, okay, this is good now.

**Joe Kern:** And we each take our own product bits, and we do those.

**Joe Kern:** Here's the key ones, supporting elements.

**Joe Kern:** We then have pain points and product solves, do we want these?

**Joe Kern:** It doesn't seem like they're necessarily broken down by product or not?

**Joe Kern:** In the company context?

**Erik O'Brien:** Correct.

**Erik O'Brien:** Yeah, these are not broken down by product.

**Aida Knežević:** I'm just thinking we could break them down by product.

**Stuti Jhunjhunwala:** So guys, is it reasonable that we update this company context product overview by end of the week and choose maybe the top three for product documents that we want to send for for additional context?

**Stuti Jhunjhunwala:** you.

**Stuti Jhunjhunwala:** Thank

**Stuti Jhunjhunwala:** By end of this week.

**Stuti Jhunjhunwala:** I'm just trying to prioritize like, like, what's the, like, you know, Yeah, if we think that's the biggest impact.

**Stuti Jhunjhunwala:** Yeah, like, that's why I'm trying to ask, like, because the impact I heard was like, hey, our product information doesn't seem right.

**Stuti Jhunjhunwala:** And if that's what's being used to generate, how we fit in, how Enable fits in, then that seems to me to be the biggest problem.

**Stuti Jhunjhunwala:** And that needs to be 100% factually correct.

**Stuti Jhunjhunwala:** And that's where we have to spend a lot of our time editing if we don't have our input right.

**Stuti Jhunjhunwala:** Please speak up, guys, if you all think that's the right approach.

**Joe Kern:** Yeah, I mean, if that's what we're basing a lot of it on, that's the best place to get healthy.

**Joe Kern:** Yep.

**Erik O'Brien:** So, think, I mean, end of week for us would be a great timeline.

**Erik O'Brien:** I just want to ask the team if that's reasonable for them.

**Andi Bailey:** I will add the one additional contextual layer that right now enables in what we call the onboarding period strategy sprint.

**Andi Bailey:** So, these first eight weeks are all about calibration.

**Andi Bailey:** You guys are in week seven.

**Andi Bailey:** So, that doesn't mean that after week eight, we wouldn't continue to work on this.

**Andi Bailey:** But I think GrowthX's model is about getting content out there, getting signals, and refining from there, which is also maybe why we moved a little fast past some of these product pieces.

**Andi Bailey:** So, yeah, if we can get this turned around by the end of the week and we can start to refine things that we...

**Andi Bailey:** We would love to start publishing.

**Aida Knežević:** But also I would, I think that if the product team is just, you know, like has a lot on their plate, I would be happy to, if you could provide me with the documentation, I can use the documentation to first update the artifacts, and then I can notify you, like, if you give me the documents today, I can update the artifacts tomorrow.

**Aida Knežević:** And then because I'm based in Europe, so by the time you guys start working tomorrow, you would have like an updated version of the artifacts to go through.

**Aida Knežević:** That would be like more in line with your existing documentation, and you will hopefully have less to edit.

**Aida Knežević:** I think maybe that would be a faster way to do things, but I'm open to your suggestions.

**Erik O'Brien:** This is a quiet group.

**Erik O'Brien:** Jen, Garrett, Joe, what do you guys think?

**Garret Stegeland:** There's so much debate over what we're doing.

**Garret Stegeland:** I just need to know what needs to be done.

**Garret Stegeland:** Like, just need someone to spell it out for me and I'll do it.

**Garret Stegeland:** Just show me where and what.

**Garret Stegeland:** Same here.

**Jen Thompson:** And I'll get it done whenever it needs to be done.

**Aida Knežević:** Okay, so I will send a follow-up email with links to these two artifacts that you can go through and then leave comments on.

**Aida Knežević:** And then as you are reviewing...

**Aida Knežević:** Any additional PDF documentation or, you know, like links to any other resources that you think would be helpful to like get to know the product better, you can also leave those in.

**Aida Knežević:** Does that, is that a good path forward for you guys?

**Aida Knežević:** Sounds good.

**Aida Knežević:** Yeah, okay.

**Joe Kern:** And so once we provide the updates, you ingest, do we plan to, then does it make sense to have like three or four topics or articles then to look at post?

**Joe Kern:** Yes, yes, we are planning to do that.

**Joe Kern:** Because I think there's still like that, that idea of tone and enable brand kind of feel that we need to make sure that we kind of train it on.

**Aida Knežević:** Yeah, yeah, so I think once we get your feedback on the artifacts, once we update them, then, yeah, we would be working on additional blocks this week that we would send to you for review.

**Aida Knežević:** Okay.

**Aida Knežević:** Okay.

**Aida Knežević:** Great.

**Aida Knežević:** Anything else that, any other questions that you had about the strategy, the approach, I am happy to give everyone access to the content OS, and then when you have time, you can also take a look at the topic ideas, and kind of help us, like, help guide us from that perspective as well.

**Aida Knežević:** It should not take you that long to go through them.

**Aida Knežević:** Yeah.

**Aida Knežević:** Yeah, that was actually going to be something that I suggested as well.

**Andrew Beyer:** If everyone on this group can get ContentOS access, especially with that topic list, that'd be helpful.

**Andrew Beyer:** And I know you and I have chatted about this, but if there's any way around the current permissions issues so that comments can be more public, so that everyone can see what, you know, the respective group is commenting, I think that that would be helpful.

**Andrew Beyer:** Yeah.

**Aida Knežević:** Andy, do you think we could work with Yusef to, like, increase permissions here?

**Aida Knežević:** Yeah, I think so.

**Aida Knežević:** Okay.

**Andrew Beyer:** Yeah, that would be beneficial so it could be seen, like, in the table rather than needing to, like, click a few levels deeper for every single topic.

**Andrew Beyer:** Yeah, yeah, for sure.

**Aida Knežević:** And then if I can, yeah, I will send everybody invites to the ContentOS then, and we can, we

**Aida Knežević:** can take it from there.

**Aida Knežević:** So yeah, I think that would be helpful from just the content planning perspective and also any additional like blog topic ideation that we do in the future that can also help like understand, okay, what should we be going after as a priority?

**Aida Knežević:** Yeah, that would be great.

**Andrew Beyer:** And maybe what would be helpful too is just quickly pulling up the table just so that the PMM org can see it just because what I just did was exported what I could so I could show them currently what we were, you know, what was being considered, but knowing their way around what this looks like would be helpful.

**Andrew Beyer:** Yeah, yeah, for sure.

**Aida Knežević:** So right now, so the air table looks like this.

**Aida Knežević:** There are three views that are going to be most relevant for you.

**Aida Knežević:** Those are blog ideas for review.

**Aida Knežević:** That's where we have all of the topics that we are suggesting to you.

**Aida Knežević:** And we would love to get your feedback on.

**Aida Knežević:** I did put a column here that just says N-able Feedback.

**Aida Knežević:** So once we increase your permissions, you will be able to leave a comment in this column, and then everybody will be able to see it.

**Aida Knežević:** The goal is really, like, you can take a look at the titles.

**Aida Knežević:** The titles are suggestions, so we can change the framing.

**Aida Knežević:** The titles are generated by our AI, who takes a look at the top-ranking content on Google.

**Aida Knežević:** And decides on a title that would be the best to serve a specific search intent and rank on page one.

**Aida Knežević:** However, once we start drafting a piece of content, we typically change the title.

**Aida Knežević:** So we're not married to it.

**Aida Knežević:** That's all I'm saying.

**Aida Knežević:** And then you can see the topic cluster it belongs to.

**Aida Knežević:** You can see the target keyword that we are trying to rank for, the overall volume of a specific keyword.

**Aida Knežević:** And the difference.

**Aida Knežević:** The higher the volume, the more potential traffic that we could get by ranking for that keyword, but it also means that it's a broader topic, so it's going to be drawing in people who might not 100% be our ICP, but it's still a valuable topic to go after.

**Aida Knežević:** And the lower the volume, that's kind of the opposite.

**Aida Knežević:** So we're getting closer to the product and to your actual ICP.

**Aida Knežević:** We want to be targeting a mix of these type of volumes, just to make sure that we are publishing content that, you know, can get to your audience as efficiently as possible, but also show that you are getting that top of the funnel traffic to your site.

**Aida Knežević:** And I think if you also, if you go to the topic clusters, you can kind of see a quick description of each cluster, but again, if you want to see like a more in-depth description of each, can go to the content.

**Aida Knežević:** Strategy, Document, and Notion.

**Aida Knežević:** And yeah, I think so far what we've done is Elaine would leave a comment on each blog post to let us know if it's approved or if it's not approved.

**Aida Knežević:** But after this call, we'll update the permissions so that everybody can kind of leave feedback in this column right here.

**Aida Knežević:** And we can go from there.

**Aida Knežević:** I think, yeah, like what would be helpful is to understand, okay, is like, is this a good topic to target?

**Aida Knežević:** If yes, why?

**Aida Knežević:** And what, is there any specific angle that we want to take when mentioning your product?

**Aida Knežević:** Again, you don't have to, we, you know, if you don't have time, you can just leave a simple thumbs up, thumbs down emoji.

**Aida Knežević:** Okay.

**Aida Knežević:** Okay.

**Aida Knežević:** Okay.

**Aida Knežević:** I I

**Aida Knežević:** Yeah, that's the content OS breakdown.

**Aida Knežević:** So I don't know if anybody else that has any other questions.

**Andrew Beyer:** Just one more for me.

**Andrew Beyer:** So if we're in the final two weeks of the strategy sprint, you know, looking at these topic clusters with all of the different topics, does that mean that portion needs to be, like, set in stone at the end of next Friday, or is there room to iterate as we move forward?

**Andrew Beyer:** No, there's definitely room to iterate.

**Andi Bailey:** That was just a sort of flag that we're in, we're sort of in calibration, so this would be the ideal time.

**Andi Bailey:** You'll go, you'll move on to a pod that manages kind of long-term clients.

**Andi Bailey:** They definitely are versed in developing content strategy.

**Andi Bailey:** We shift strategies quarterly, normally, or kind of re-evaluate where we're going based on, like, product and development, but, yeah, just...

**Andi Bailey:** Thinking about kind of where you are in the life cycle.

**Andi Bailey:** Okay.

**Andi Bailey:** sense.

**Aida Knežević:** And when we developed the first version of the content calendar, we definitely can refine this list even during the duration of the sprint.

**Aida Knežević:** So if you have like any other ideas that you want to explore, you know, even if it's like, hey, like we would love to explore like this topic.

**Aida Knežević:** Is there anything that we could potentially target there?

**Aida Knežević:** I'm happy to get those suggestions.

**Aida Knežević:** The content calendar, like we iterate on it.

**Aida Knežević:** So, you know, we kind of, the process is meant to show us, okay, what you want to be targeting and what you want to be, you know, kind of putting on the back burner for now.

**Aida Knežević:** Great.

**Aida Knežević:** Yeah.

**Aida Knežević:** All right.

**Aida Knežević:** So, so next steps for me, I'll send everyone an email.

**Aida Knežević:** now, week.

**Aida Knežević:** I'll 더 send the done them next week, send

**Aida Knežević:** To the artifacts, I will send a link to the content OS with, you should all have access to it via your work email.

**Aida Knežević:** If anybody, you should, I will also give everybody access to Notion in case you don't have it yet.

**Aida Knežević:** So yeah, next steps would be review the company context, leave any additional product documentation, either as a link in the comments or you can upload it into the Notion doc.

**Aida Knežević:** I will kind of break this down in the email.

**Aida Knežević:** And then I will resolve update artifacts as soon as we get your feedback.

**Aida Knežević:** And then we will move forward with generating content.

**Aida Knežević:** And yeah, you can also leave feedback on the topics themselves to help us prioritize better.

**Stuti Jhunjhunwala:** So guys, just so that it's not confusing, let's maybe prioritize this week's action to be all about the input.

**Stuti Jhunjhunwala:** do...

**Stuti Jhunjhunwala:** sorts people...

**Stuti Jhunjhunwala:** do...

**Stuti Jhunjhunwala:** ...

**Stuti Jhunjhunwala:** things

**Stuti Jhunjhunwala:** Do the product section and any about us documents and then maybe next week we can pick up and review the blog topics and provide content.

**Stuti Jhunjhunwala:** I think it's just too much asks.

**Stuti Jhunjhunwala:** So I would just say ignore feedback on the blog topics for this week.

**Stuti Jhunjhunwala:** Let's make sure the product level input is correct.

**Stuti Jhunjhunwala:** Would you guys agree?

**Stuti Jhunjhunwala:** Like the more things we ask people to do, the more confusing it gets.

**Stuti Jhunjhunwala:** I think that's totally fine.

**Aida Knežević:** Yeah.

**Aida Knežević:** Perfect.

**Aida Knežević:** Yeah.

**Aida Knežević:** Oh, wow.

**Aida Knežević:** Garret's a happy man right now.

**Stuti Jhunjhunwala:** saw a hundred thumbs up.

**Stuti Jhunjhunwala:** So, so yeah, I think like, and Andrew Beyer, I don't know who said it.

**Stuti Jhunjhunwala:** Maybe it was Joe.

**Stuti Jhunjhunwala:** He loves being made to feel guilty.

**Stuti Jhunjhunwala:** So if it's not done by, I mean, if you don't mind pushing on Thursday to make sure that the inputs all good input notion document and any files that we want to share.

**Aida Knežević:** Okay.

**Stuti Jhunjhunwala:** Thank

**Aida Knežević:** Yeah, I will definitely be making you feel guilty, so no problem following up over email.

**Stuti Jhunjhunwala:** Cool, and then if needed, next week we can revisit how we go over feedback on ideas and things like that, but let's partition the ask.

**Andrew Beyer:** Yeah, yeah, for sure.

**Aida Knežević:** Okay, I think if you don't have any other questions, I think we can wrap up.

**Aida Knežević:** Okay, all right, perfect.

**Aida Knežević:** Yeah, I will send a follow-up email in a couple of minutes with next steps.

**Aida Knežević:** Thank you so much for taking the time to meet with us.

**Aida Knežević:** Of course.

**Aida Knežević:** you so much.

**Aida Knežević:** Thank you, bye.

**Aida Knežević:** Bye.

**Aida Knežević:** Thank you.

**Aida Knežević:** Thank you.
