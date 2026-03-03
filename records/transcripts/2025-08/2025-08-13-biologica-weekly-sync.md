# Biologica Weekly Sync

<metadata>
date: 2025-08-13
time: 15:00 UTC
duration: 28 minutes
organizer: matthew@growthx.ai
participants: Matthew Panzarino (GrowthX), Brian Magida (Biologica)
fathom_recording_id: 80301707
fathom_url: https://fathom.video/calls/378613662
share_url: https://fathom.video/share/Pd8HcdDGizXDG3xMh1T2yHbHGCsz7tCA
source: fathom
enriched_on: 2026-03-03 18:45 UTC
</metadata>

---

## Summary

Matthew and Brian aligned on Biologica's ingredient-focused content strategy, prioritizing a new cluster emphasizing the deliberate combinations of ingredients like K2, D3, and calcium for Biologica's supplement products. GrowthX is building automated logic into their content pipeline to ensure proper ingredient mentions and groupings based on Biologica's ingredient database, while the team is also implementing Shopify integration, developing image specifications using Biologica's brand guidelines and Future font, and managing parallel review cycles for tone (led by co-founder Liz), regulatory approval (handled by Maggie), and content artifacts. A photo shoot scheduled for September 3-5 will provide assets for content creation and as training material.

---

## Context

Biologica is a women's health supplement company that competes in the perimenopause and menopause wellness space. GrowthX is managing Biologica's content marketing, focusing on creating blog posts that are informational, keyword-focused, and slightly editorialized to drive traffic and establish brand authority. The relationship is collaborative and ongoing—Matthew leads the GrowthX side, working closely with Brian who manages strategy and product messaging. This meeting is part of a regular cadence to review content progress, handle feedback incorporation, and align on technical integrations. Brian emphasized that competitors like Mibi (which recently moved into supplements) often have thin ingredient formulations, but Biologica's products are deliberately combined for efficacy, a differentiator the content needs to communicate clearly.

---

## Relevance

**To GrowthX Delivery:**
- Successfully built automated ingredient integration logic into content pipeline to match products with relevant ingredient mentions and groupings—reducing manual editorial overhead and improving consistency
- Implementing Shopify integration in next engineering sprint to enable automated publishing of content to templated pages, eliminating manual placement work
- Developing repeatable image specification and creation workflow using Recraft and client brand assets, already proven with other clients

**To GrowthX Business Development:**
- Biologica demonstrates strong expansion potential—monthly content batches, ongoing feedback cycles, technical integrations, and September photo shoot indicate a maturing, well-resourced engagement
- Client is actively recruiting multiple reviewers (co-founder Liz, brand marketing, regulatory team, user testers) showing high organizational investment in content quality
- Opportunity to position repeatable templated publishing and automated ingredient logic as reusable frameworks for other supplement/health product clients

**To CheckThat:**
- Biologica's emphasis on ingredient combinations and efficacy messaging could serve as a case study for AI-assisted ingredient knowledge mapping and E-E-A-T content optimization
- Regulatory review coordination and tone/scientific accuracy balance demonstrate the need for AI systems that can handle nuanced health content with compliance constraints

---

## Overview

- New ingredient-focused content cluster is prioritized, with K2, D3, and calcium topics added to the postmenopause category
- GrowthX is building logic to automatically match ingredients with product mentions and group complementary ingredients (e.g., L-theanine and GABA) for effectiveness
- Parallel review processes are running: tone review by co-founder Liz, regulatory review by Maggie next week, and brand marketing feedback being gathered
- Shopify integration is moving into next engineering sprint for automated publishing; image spec is in development using Future font and Biologica's brand guidelines
- Product card placement and embedding needs clarification with dev team on whether cards are templated page components or inline embed code

---

## Key Topics

### Content Creation and Prioritization

  - New cluster of ingredient-focused content for the blog
  - Content should be informational, keyword-focused, and slightly editorialized
  - K2, D3, and calcium topics to be added to the postmenopause cluster
  - Two-week buffer maintained for content delivery, incorporating feedback

### Ingredient Integration and Grouping

  - Emphasis on deliberate combination of ingredients for effectiveness
  - Logic flow being built into the content pipeline for automatic ingredient integration
  - Importance of grouping ingredients (e.g., L-theanine and GABA) highlighted

### Content Review and Feedback

  - Dossier updates expected in the coming weeks
  - Brand marketing team member reviewing artifacts for additional input
  - Liz (co-founder) reviewing articles for tone and creating a list of do's and don'ts
  - Nancy's mom reviewing current menopause content
  - Maggie focusing on regulatory review for email content next week

### Email and Website Copy

  - Team creating a document expanding on do's and don'ts for tone
  - Final copy (post-regulatory review) to be shared for AI analysis

### Technical Updates

  - Shopify integration ticket in next engineering sprint
  - Image spec being developed by Katia (design engineer)
  - Font files shared for use in image creation
  - Product card integration needs clarification from dev team

### Upcoming Assets

  - Photo shoot scheduled for September 3rd-5th, with assets available \~2 weeks after

---

## Action Items

**Matthew Panzarino (GrowthX)**
- Ensure Katya (design engineer) receives Future font files for blog title cards and coordinates with Biologica's brand guidelines for image spec development

- Follow up with Matthew (Biologica dev team) on product card architecture: clarify whether cards are templated page components or inline embed code for body copy placement

---

## Transcript
**Matthew Panzarino:** We can start talking about the new cluster, the new content.

**Matthew Panzarino:** You had dropped in some topics that you wanted to work on.

**Matthew Panzarino:** You had mentioned kind of like two.

**Matthew Panzarino:** So there was a previous chat we had about, oh, maybe we can do this next.

**Matthew Panzarino:** And then you kind of pasted in this next bit about with these sort of like kind of ingredients.

**Matthew Panzarino:** Yeah, ingredients.

**Matthew Panzarino:** I'm sorry.

**Matthew Panzarino:** Yes, the ingredients focused stuff.

**Matthew Panzarino:** And so I'm happy to prioritize those.

**Matthew Panzarino:** We would, we would do.

**Matthew Panzarino:** The great thing is, is like we can work off these titles.

**Matthew Panzarino:** We can create outlines and stuff that work for them.

**Matthew Panzarino:** And basically two major questions.

**Matthew Panzarino:** Do you want us to prioritize like keyword focused top, top, keyword focused like formats for these?

**Matthew Panzarino:** Or did you have a really specific idea about the format that you'd like?

**Matthew Panzarino:** Like, you know, do you want

**Matthew Panzarino:** To be, you know, a definition page or something more like informational, we can do our own deal on this.

**Matthew Panzarino:** I just want to make sure you didn't have like something in your mind where these are going to sit on the site so that we don't make something that doesn't really map well, you know.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Right.

**Brian Magida:** Yeah.

**Brian Magida:** So we essentially have separate ingredient pages that are, right, that exist with a very specific format.

**Brian Magida:** These, want to be informational, but like slightly editorialized, if you will.

**Brian Magida:** Like the purpose is, it's existing on the blog, and so they should be keyword focused, but, and it should be written with information, but it's kind of like threading the line between like, yeah, it needs to be specific, scientific, but also like, yeah, a person's, it's living on the blog.

**Matthew Panzarino:** So obviously like romanticize, it's probably the wrong word, but.

**Matthew Panzarino:** No, give it to me.

**Matthew Panzarino:** Yeah, I get it.

**Matthew Panzarino:** Yeah, that sounds good.

**Matthew Panzarino:** And then.

**Matthew Panzarino:** The K2, D3, and calcium topics, we can also add to the list.

**Matthew Panzarino:** I didn't see them either, so we can get them on there, and we'll make sure that that ends up in the postmenopause cluster.

**Matthew Panzarino:** We, I think, are working, we will have the last of the perimenopause stuff generated.

**Matthew Panzarino:** So we're two weeks ahead, right?

**Matthew Panzarino:** Like, that's the way we're working.

**Matthew Panzarino:** We want to make sure that we have a buffer of content.

**Matthew Panzarino:** Well, the only reason we're not sort of saying, here's, you know, three weeks for the content or whatever, is because we need to, we want to make sure that any feedback makes it in.

**Matthew Panzarino:** So we're taking the feedback, and then say, okay, cool, what's, what, what needs to be updated in this next batch of content?

**Matthew Panzarino:** So we're going to keep on pace for you on your side.

**Matthew Panzarino:** You'll keep, you'll get delivery on pace, but that will hopefully be updated with whatever comment has last been left.

**Matthew Panzarino:** So they don't have to re-review.

**Matthew Panzarino:** The next cluster, we can focus on this as the next cluster, though, is totally fine.

**Matthew Panzarino:** And this is like...

**Matthew Panzarino:** Week and a half's worth of content, so we should be able to get that going for you.

**Matthew Panzarino:** And then we will take that and incorporate it into the context artifact that people have to put in there.

**Brian Magida:** That's cool.

**Brian Magida:** I think I should make sure.

**Brian Magida:** I think I showed this with you before.

**Brian Magida:** I just dropped into the chat.

**Brian Magida:** This doc.

**Matthew Panzarino:** Let's take a look.

**Matthew Panzarino:** Yeah, we have this.

**Brian Magida:** Okay.

**Brian Magida:** I just want to call out, there's a column, H, where you'll see, like, there's notes in there about groupings, which I think is helpful, where, like, this came up kind of actually recently, where not a competitor, per se.

**Brian Magida:** There's a company called Mibi, which focused on, like, women's HRT.

**Brian Magida:** They're now moving into supplements, and so they've launched the perimenopause supplement.

**Brian Magida:** And when you're actually, like, it's pretty interesting, because I've gone through this process where I'm starting to learn a little bit more about products that are targeting like a specific hormonal stage.

**Brian Magida:** It's like people kind of put whatever they think is interesting in there.

**Brian Magida:** But I'm finding like most are actually like super thin as far as the ingredients go.

**Matthew Panzarino:** Like there's like very little actually in their product and they charge a lot for it.

**Brian Magida:** And one like interesting example is of the B complex, they literally just have B12.

**Brian Magida:** Like they don't have anything else.

**Brian Magida:** And so I just use that as an example where like we're very deliberate about the combination of ingredients.

**Brian Magida:** Because like in combination out these dosages, like they're quite effective.

**Brian Magida:** But like individually, they may not be as effective.

**Brian Magida:** And that also goes, I think in the content, there might have been stuff with like L-theanine and GABA.

**Brian Magida:** Like those things individually are great, but like combined are actually like quite powerful.

**Brian Magida:** So I would just like, as you go through the content.

**Brian Magida:** Just make sure there's opportunities to group ingredients where it makes sense to group them.

**Brian Magida:** And it's just, yeah, that's really my point.

**Brian Magida:** So that goes back to K2, D3, calcium, common.

**Brian Magida:** That's great.

**Brian Magida:** And this is really timely because right now I'm working with the ENG team.

**Matthew Panzarino:** So the way that this ingredient integration has worked for the batches that we've been delivering for you is that our context, this is defined as a contextual artifact, right?

**Matthew Panzarino:** This document.

**Matthew Panzarino:** So our system has this document with all the columns and priorities and, of course, the product.

**Matthew Panzarino:** Did you add any of this just recently?

**Brian Magida:** is this?

**Brian Magida:** No, no.

**Matthew Panzarino:** Okay, cool.

**Matthew Panzarino:** That's fine.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** So we have this information and we, right now we are applying it in like a post-processing flow.

**Matthew Panzarino:** So it'll go back and look at the article and say, hey, you know, I wrote the logic for it, right?

**Matthew Panzarino:** So the logic is basically.

**Matthew Panzarino:** Is this a product that integrates any of these ingredients?

**Matthew Panzarino:** Obviously, it uses the product column to say, hey, this ingredient is in this product.

**Matthew Panzarino:** Starting with the highest priority ones, make sure that we mention them when appropriate, and then make sure we mention their effects and that the brand names are in there, right?

**Matthew Panzarino:** So basically, I just wrote a little logic to say, double check this, make sure that these things are in there, and that they're mentioned for the appropriate product, and not mentioned for the not appropriate product, right?

**Matthew Panzarino:** So that we're not saying that an ingredient exists in the midlife essentials that doesn't exist in it, right?

**Matthew Panzarino:** It exists in one of the other products.

**Matthew Panzarino:** And then the second bit of logic is look for ingredients that are not mentioned, that are applicable to symptoms talked about in this particular article, symptoms or conditions or whatever, you know, effects that they want them to have.

**Matthew Panzarino:** So it will then look at this list and basically say, oh, you mentioned inflammation, but you did not bring up the ingredient that tackles inflammation.

**Matthew Panzarino:** So we're going to go ahead and tuck a mention of it in there because this

**Brian Magida:** also exists in this product that we're stumping in this thing.

**Matthew Panzarino:** So it basically is like a logical framework for applying these things.

**Matthew Panzarino:** We're doing that in a sort of standalone post-process right now.

**Matthew Panzarino:** right now, literally today, I was talking back and forth with one of our engineers, but he's building that into your pipeline so that any article that gets produced down the line will get this logic automatically applied to it.

**Matthew Panzarino:** Of course, it's self-serving because there's less editorial process for us at the end.

**Matthew Panzarino:** But, of course, serves you as well because that means if you update this document and add new ingredients or a new product or anything like that at any time, we can take that and put that artifact into the pipeline, and then that same logic will work on it.

**Matthew Panzarino:** So you can expand this, change this, update this, as long as you tell us about it, of course, then we'll be able to integrate it well.

**Matthew Panzarino:** And that's the process that we're going through.

**Matthew Panzarino:** That is why I'm here, basically, is to make sure that we build out these logic flows properly to get you good.

**Matthew Panzarino:** through.

**Matthew Panzarino:** Content, you know, that, that integrates stuff as deeply as possible.

**Matthew Panzarino:** So any additional information, databases, or context that you give us, you know, I'll take it, squint at it, and figure out how to, how to integrate it so that, you know, everything, at least that table stakes is all the basics are covered and then we can go stylistically over the top and go like, okay, cool.

**Brian Magida:** Like, what do we want?

**Brian Magida:** How do we want this to feel?

**Matthew Panzarino:** Okay.

**Brian Magida:** Yeah.

**Brian Magida:** That's a good reminder.

**Brian Magida:** On the dossier side, they, there's going to be additional sort of updates to dossiers, just like more content added.

**Brian Magida:** Maggie, who's writing them, she's out this week.

**Brian Magida:** I think that's going to be completed in the next couple weeks, I think I said, like sooner.

**Brian Magida:** So I'll just let you know as soon as those are done.

**Brian Magida:** And we already have access to those actual files.

**Brian Magida:** So like the updates will happen there.

**Brian Magida:** So I'll just like, you know when those get updated.

**Brian Magida:** Perfect.

**Brian Magida:** Yep.

**Brian Magida:** The, the other thing, so I sent.

**Brian Magida:** You guys, I think yesterday, this, like, founder's letter that we were going be sending out through email.

**Brian Magida:** So hopefully that can get, like, leveraged within a company context in some way.

**Matthew Panzarino:** Yeah, it was updated yesterday.

**Brian Magida:** So it's in company context artifacts.

**Brian Magida:** Okay, great.

**Brian Magida:** The other thing that the team is working on is someone's on the team who's part-time is, like, actually going to go through and just, like, review the artifacts just to see if there's any additional, like, additions.

**Brian Magida:** She would add, she's on the brand marketing side.

**Brian Magida:** So just letting you know that she's going to, I think, either comment in Notion or just send me some comments.

**Brian Magida:** So I'll let you know when that happens.

**Brian Magida:** Great.

**Brian Magida:** The other thing, two other things.

**Brian Magida:** So, one, I told you we're working on, like, all this email content, all this website content.

**Brian Magida:** As such, the co-founder, Liz, is, like, kind of keeping creating a list that she'll send me when she thinks it's in a pretty good spot.

**Brian Magida:** Of how, like, essentially the artifacts are adjusting copy, like, for email and the website.

**Brian Magida:** Because the good net benefit is, is, like, we're seeing it come up with, like, certain phrases that either, like, we love or we're just, like, we don't like.

**Brian Magida:** And so we're going to put together, like, a document for you that kind of, like, I think expands on the do's and the don'ts section for Tone.

**Brian Magida:** perfect.

**Brian Magida:** I don't know exactly when we'll have that, but I'll share that with you once, once we have it.

**Brian Magida:** Because I think that'll actually be quite helpful.

**Brian Magida:** I don't know, like, if it's going to manifest itself in article generation, but, like, it might, so.

**Matthew Panzarino:** Yeah, it absolutely might.

**Matthew Panzarino:** And the do's and don'ts bit is so important, obviously, for specific examples, but also for pattern matching, right?

**Matthew Panzarino:** It's like, oh, okay, we can see what you don't like here, right?

**Matthew Panzarino:** You know, you don't like platitudes or whatever the case.

**Matthew Panzarino:** It's like this kind of language is showing in repeating ways.

**Matthew Panzarino:** So absolutely happy to take that.

**Matthew Panzarino:** That's.

**Matthew Panzarino:** It's incredibly valuable.

**Matthew Panzarino:** It's like royal jelly for the algorithm for us, you know, so sounds good.

**Brian Magida:** guess a question I have is, I have these like Google Docs that contain essentially like all the email copy or like as it currently stands.

**Brian Magida:** So is it helpful for you to have like what we're deeming to be at its current state, like final for you to analyze?

**Brian Magida:** Or do you actually need like, this is where it started, this is where it ended, and like your system sort of deduces the changes and like maybe why we made those changes to then incorporate back in the artifacts?

**Brian Magida:** Like what would be helpful, if anything at all there?

**Matthew Panzarino:** Let me think about it.

**Matthew Panzarino:** I think for sure the content would be useful.

**Matthew Panzarino:** So if you have the content available, just like what you consider to be final, that is absolutely useful just on a table stakes way because it helps us to understand the voice better.

**Matthew Panzarino:** So that...

**Matthew Panzarino:** That part of it is great.

**Matthew Panzarino:** We're happy to take that.

**Matthew Panzarino:** Let me think about whether the diffs are useful or not.

**Matthew Panzarino:** I won't spend my time staring at the camera thinking about it on this call.

**Matthew Panzarino:** I'll think about it and get back to you.

**Matthew Panzarino:** But for sure, the final copy.

**Matthew Panzarino:** Absolutely.

**Matthew Panzarino:** Yes.

**Brian Magida:** It's useful.

**Brian Magida:** It has to still go through some regulatory, but is it better just to wait until it's gone through regulatory, or is it helpful just to say, like, here's the copy, like, just look at town or something like that and not look at anything, like, scientific?

**Matthew Panzarino:** Let's wait.

**Matthew Panzarino:** Let's make sure that it's locked because I don't want it to pick up a scientific, you know, argument that is denied by regulatory and you have to elide, and then we end up integrating it, right?

**Matthew Panzarino:** And then we just pop up in some edge case.

**Matthew Panzarino:** I don't want to introduce any fuzziness into it with the medical, you know, content, given that that's already something we're trying to really fine-tune, so.

**Brian Magida:** Okay.

**Brian Magida:** Cool.

**Brian Magida:** Yeah, the other just like updates.

**Brian Magida:** Nancy was his mom is reviewing a bunch of current menopause content.

**Brian Magida:** I'm hoping that I get some feedback there, certainly when she's back from vacation.

**Brian Magida:** And then as I alluded to, Maggie is on vacation this week.

**Brian Magida:** She's going to like completely over-rotate next week just doing all the regulatory stuff for email.

**Brian Magida:** Wow.

**Brian Magida:** And so that's kind of like where we're at.

**Brian Magida:** And then Liz is reviewing the articles for Tone.

**Brian Magida:** She's going to get through like the backlog of those.

**Brian Magida:** Okay.

**Brian Magida:** So I guess like you tell me, there's already a bunch of comments.

**Brian Magida:** not sure if you've seen those comments that she's made.

**Brian Magida:** I probably told you just to be like, whatever, you can wait until they get reviewed on the medical side.

**Brian Magida:** But it's just, there's going to be this like near term delta between like tone review and medical review.

**Brian Magida:** So I kind of defer to you how you want to go about taking that feedback and making a job.

**Brian Magida:** If you want to do it in like steps or if just want to wait until those articles have been reviewed by both parties before incorporating, but I kind of prefer to you.

**Matthew Panzarino:** Yeah, we took everything already.

**Matthew Panzarino:** So everything that's in there is already in the artifacts.

**Matthew Panzarino:** We just were like, you know, hey, we have some time in our cycle, so let's grab it.

**Matthew Panzarino:** So that's already in there.

**Matthew Panzarino:** But yeah, just flag it for us as they get released or as they're – I guess we're just using the Airtable status, right?

**Matthew Panzarino:** So just move them to reviewed and then we'll jump on it from there.

**Matthew Panzarino:** We're going to keep delivering, so don't be anxious about it.

**Matthew Panzarino:** You know, it's all good from our end.

**Matthew Panzarino:** You know, we're just going to keep cruising.

**Matthew Panzarino:** And then as I mentioned, we didn't want to wait too long for the artifacts to get updated, so we just scraped the latest comments.

**Matthew Panzarino:** And we'll continue to do that on a weekly basis unless it's like, oh, we just – we did a burst, you know, and we released a bunch for review.

**Matthew Panzarino:** And we're like, oh.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** We have like eight new articles to like grab the comments from.

**Matthew Panzarino:** We'll do it then, you know, but in general, we just don't like to do it every day because it's actually a little laborious process.

**Brian Magida:** So, yeah.

**Brian Magida:** Okay.

**Brian Magida:** Well, so yeah, that's kind of where we're at.

**Brian Magida:** Oh, the other thing too, Liz is reviewing those incontinence pages.

**Brian Magida:** She's like, I think one tenth of the way through it, but that's another, that'll be like a big area.

**Matthew Panzarino:** I think where tone will come through.

**Brian Magida:** She's like, it obviously has to be reviewed by regulatory, but there's gonna be a lot of tone and stuff in there that I think will be kind of quite helpful.

**Brian Magida:** Yep.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Sounds good.

**Matthew Panzarino:** We can tackle it.

**Matthew Panzarino:** And then the two process-based updates, we have the Shopify ticket going into the next end sprint because we actually don't ironically have any other clients on Shopify.

**Brian Magida:** the moment.

**Matthew Panzarino:** Fine.

**Matthew Panzarino:** That's great.

**Matthew Panzarino:** This is good news because

**Brian Magida:** That means we have something to build.

**Matthew Panzarino:** We'll build that, make sure it's good.

**Matthew Panzarino:** The good news is that Shopify is very straightforward.

**Matthew Panzarino:** mean, I have run Shopify sites, so I'm not concerned about it.

**Matthew Panzarino:** So if we get down to crunch time and for any reason we need to do it manually, we're fine, right?

**Matthew Panzarino:** But we love to build an automated process here so that everything, as it gets released, we can publish it to schedule and to spec.

**Matthew Panzarino:** So we'll get that set up, and then I'll keep you abreast of that.

**Matthew Panzarino:** We have all the information, I think, that we need at this point, but then Inge will at some point have, like, a list of things.

**Matthew Panzarino:** Oh, we need, you know, these things, EPI key, and these other things, whatever.

**Matthew Panzarino:** And I'll get that spec together and then sent over to you or you and the website team, and then we can get that going.

**Matthew Panzarino:** And then on the images, Katia, one of our design engineers, is working on the image spec.

**Matthew Panzarino:** I believe we do need your font.

**Matthew Panzarino:** Okay, I guess, yeah.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** And then...

**Matthew Panzarino:** Outside of that, think she has what she needs from the tone stuff that you and Marcel had chopped up and then the things you had sent over.

**Matthew Panzarino:** So we'll just start, right?

**Matthew Panzarino:** We'll give you something and then we can tune from there.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** But yeah, we're pretty confident we can come up with something that is repeatable and straightforward.

**Matthew Panzarino:** We have some other clients that we're doing similar work for that they've been pretty happy with the repeatable result.

**Matthew Panzarino:** As long as you don't get like crazy complex with the design, which in general is not really necessary for blog images.

**Matthew Panzarino:** So we'll get something that aligns well with your brand and it's repeatable, you know, so it's crisply.

**Brian Magida:** We get what we're expecting every time.

**Brian Magida:** That's the important thing.

**Matthew Panzarino:** Yeah.

**Brian Magida:** Yeah, I can get you.

**Brian Magida:** I can get you that spot.

**Brian Magida:** Let me just, since I have you right now.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Oh, I guess that this is sort of related, but the product cards, you'd mentioned something about the product cards.

**Brian Magida:** Talk to me about that.

**Brian Magida:** Yeah.

**Brian Magida:** Um, let me, let me show you, I can show you like what this looks like in design, I mean obviously I don't know what everything actually looks like in dev yet.

**Brian Magida:** Yeah, yeah.

**Brian Magida:** Because that's, haven't seen, but.

**Brian Magida:** Sorry.

**Matthew Panzarino:** Can you see this thing?

**Brian Magida:** Yeah.

**Brian Magida:** Okay.

**Brian Magida:** So a product card would be something like this.

**Brian Magida:** Oh, okay.

**Brian Magida:** It's like featured products.

**Brian Magida:** I don't know if there's any other.

**Brian Magida:** I think that's like the only one that we have designed at the moment within the blog.

**Brian Magida:** But that's what we mean by these products.

**Matthew Panzarino:** Yeah, that's great.

**Matthew Panzarino:** And I think that's the only thing that would be important for us is just, you know, how to call those cards.

**Matthew Panzarino:** Once it comes time for publishing, obviously, that's, you know, something your website team is building.

**Matthew Panzarino:** But that would allow us to place them where we wanted them, basically.

**Matthew Panzarino:** You know, like an injectable version of those cards or a call out so that we can embed them properly.

**Matthew Panzarino:** Or if it's in the template, we don't even have to worry about it, right?

**Matthew Panzarino:** It doesn't affect us at all if it's already like templatized that way.

**Matthew Panzarino:** We just want to make sure that it appears at the appropriate places.

**Matthew Panzarino:** If want it to appear in the copy, and if we need to put it at certain places, or you're like, oh, we always want it to be right before the key takeaways, or whatever the case may be.

**Matthew Panzarino:** If it's in the template that way, and we're publishing to a Shopify page template, we're golden, right?

**Matthew Panzarino:** We don't have to do anything.

**Matthew Panzarino:** But if it's something that's embedded in the text, where it's like an embed that's called, and we need to put that script in, we don't want you to have to do that.

**Matthew Panzarino:** We can do that for you.

**Matthew Panzarino:** We can make sure that it ends up in there.

**Matthew Panzarino:** So we have clients that work both ways.

**Brian Magida:** So I just wanted to make sure that we're figuring that out.

**Brian Magida:** Yeah.

**Brian Magida:** Yeah, the dev team will be the right people to talk to you about that.

**Brian Magida:** Cool.

**Brian Magida:** What's your email again?

**Matthew Panzarino:** Panzer?

**Matthew Panzarino:** No, actually, it's Matthew.

**Matthew Panzarino:** Matthew, M-A-T-T-H-E-W at growthx.ai.

**Matthew Panzarino:** Although I should get Panzer as an alias.

**Brian Magida:** There's no reason why I don't.

**Brian Magida:** Yeah, absolutely.

**Brian Magida:** Okay, I just shared with you a folder on fonts.

**Brian Magida:** Just let me know.

**Matthew Panzarino:** I said for view access, which I think you should see.

**Matthew Panzarino:** I'll be able to download, but just let me know if you can.

**Matthew Panzarino:** Sounds good.

**Matthew Panzarino:** I will make sure that Katya gets that.

**Brian Magida:** In the brand, you guys have the brand guidelines, like they're, I think, right?

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** I think you linked it in the channel, I believe, right?

**Brian Magida:** Okay, I think so.

**Brian Magida:** It's more just like reference that as far as how to use the...

**Matthew Panzarino:** Yeah, yeah, absolutely.

**Matthew Panzarino:** She has that information.

**Matthew Panzarino:** Yeah, so the brand book and the mood imagery she has, and then she just needed the font so that we can put it...

**Matthew Panzarino:** So we're using a handful of different tools, like Recraft and some other things.

**Brian Magida:** We'll also have our photo shoot.

**Brian Magida:** This actually might be helpful for you guys.

**Brian Magida:** Our photo shoot's scheduled for September 3rd, 4th, and 5th.

**Matthew Panzarino:** So we'll have actual offsets delivered, call it plus or minus, two weeks after that.

**Brian Magida:** Okay.

**Brian Magida:** And then...

**Brian Magida:** And obviously, like, you can use those and or leverage them as training material for content creation.

**Brian Magida:** Yeah, that's great.

**Matthew Panzarino:** Sounds good.

**Matthew Panzarino:** Yeah, I don't see, I didn't see that folder show up.

**Matthew Panzarino:** Usually, it's pretty instant, so I just want to make sure.

**Brian Magida:** I'll simply set it right here.

**Matthew Panzarino:** Because I want to unblock her.

**Matthew Panzarino:** I don't want to wig any cycles or let it slip the cracks.

**Matthew Panzarino:** And then, yeah, we can follow up.

**Matthew Panzarino:** I can follow up in that thread, I guess, with Matthew about the product cards.

**Matthew Panzarino:** Yeah, cool.

**Matthew Panzarino:** I'll do that.

**Matthew Panzarino:** And it's basically, it's a simple question.

**Matthew Panzarino:** It's like, is it in the templated page or is it an embed or a bit of code that we need to integrate into the body copy?

**Matthew Panzarino:** Not a huge deal.

**Matthew Panzarino:** This is very low stakes.

**Brian Magida:** We can, we'll figure it out.

**Brian Magida:** My assumption, I could very well be wrong, is the way that it's being built—it'll be a block within the CMS, I think is the technical term.

**Brian Magida:** So, presumably those blocks can be placed really kind of wherever.

**Brian Magida:** Yeah.

**Brian Magida:** That would be my guess.

**Matthew Panzarino:** So, but yeah, talk to Matthew.

**Matthew Panzarino:** He'll be able to.

**Brian Magida:** Yeah, sounds good.

**Matthew Panzarino:** Because the way, the way it works is, you know, if we, if you're publishing to a template that we just need to insert.

**Matthew Panzarino:** Text into certain components of it, then the API will typically allow that.

**Matthew Panzarino:** You know, it'll have endpoints for the different blocks that you've established on the page.

**Matthew Panzarino:** If, however, it's like, hey, you have a bucket that you need to pour, copy any blocks that you have or whatever into.

**Matthew Panzarino:** We just need to then call the block, you know, so that when we're publishing, we create and stage the entire flow the way you want it to.

**Matthew Panzarino:** So I'll talk to them.

**Matthew Panzarino:** We'll figure it out.

**Matthew Panzarino:** All good.

**Matthew Panzarino:** And then the Bradford or the Future is the font that we're looking for, for the title cards.

**Brian Magida:** I honestly don't remember.

**Brian Magida:** I'd have to look at.

**Brian Magida:** Let me see.

**Matthew Panzarino:** I want make sure we're chasing the right one.

**Brian Magida:** Thank you.

**Brian Magida:** Your question is title cards for the blog.

**Matthew Panzarino:** Yeah, specifically for that because I'm assuming you use them for different purposes.

**Brian Magida:** Yeah.

**Brian Magida:** I think it's going to be the future is my guess.

**Matthew Panzarino:** Yeah, it will be the future.

**Matthew Panzarino:** Sure.

**Matthew Panzarino:** You got it.

**Matthew Panzarino:** Okay, sweet.

**Matthew Panzarino:** I'll plug that for Katya.

**Matthew Panzarino:** We will get rolling.

**Matthew Panzarino:** Sweet.

**Matthew Panzarino:** Anything else for me?

**Brian Magida:** No, I think that's it.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** Yeah, we'll have another batch for you this week, and we'll keep an eye out for those comments.

**Matthew Panzarino:** As soon as they get released, we'll polish them up and move them into the ready for the rest of the process column.

**Matthew Panzarino:** And then I have somebody working on that linking scenario, so we know the breadcrumbs.

**Matthew Panzarino:** So we'll figure out how to make sure that those links are live when it gets published, and then what order they need to go out in.

**Brian Magida:** But yeah, other than that, we're good.

**Brian Magida:** Okay, great.

**Matthew Panzarino:** Thanks.

**Brian Magida:** sir.

**Brian Magida:** Ciao.

**Brian Magida:** Bye.
