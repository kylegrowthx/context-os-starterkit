# Biologica <> Growth X - Weekly Sync

<metadata>
date: 2025-10-03
time: 19:58 UTC
duration: 31 minutes
organizer: team@growthxlabs.com
participants: Matthew Panzarino (GrowthX), Brian Magida (Biologica), Elizabeth Zwillinger (Biologica)
fathom_recording_id: 91828034
fathom_url: https://fathom.video/calls/427808747
share_url: https://fathom.video/share/PxkTutmuWVpiz2MJdMzBw69M7udpzGUA
source: fathom
enriched_on: 2026-03-02 14:30 UTC
</metadata>

---

## Summary

Biologica and GrowthX reviewed progress on AI-generated content and identified opportunities to improve intro paragraph quality through examples-based AI prompting. The team flagged staging site issues requiring dev fixes (text pop-in effect, gray text color, spacing, excerpt duplication) and agreed to prioritize a new batch of articles on reproductive years and postmenopause topics, with medical review by Nancy. Image generation has improved significantly with Nano Banana's skin texture rendering, and the team will define clearer style guidelines for abstract, black-and-white photography.

---

## Context

Biologica is a women's health supplement company partnering with GrowthX on content marketing. This is a weekly operational sync between Biologica's leadership (Brian and Elizabeth) and GrowthX's content team (Matthew) to review article drafts, styling issues, and production planning. The partnership centers on AI-assisted content generation for their blog, with Biologica providing medical review and final design direction, and GrowthX handling the AI workflow, copywriting, and technical implementation. The team is in active production mode, moving from draft review to staging and publication.

---

## Relevance

**To GrowthX Delivery:**
- AI prompt engineering: Using examples of good intro paragraphs instead of instruction-based rules produces better stylistic results — implement this pattern in other client AI workflows
- Instruction vs. examples trade-off: Detailed rule sets can overflow context windows; examples-based prompting is more efficient and delivers style without losing coherence
- GPT-4.5 significantly improves output quality; team has upgraded Biologica pipeline to 4.5 and sees measurable improvements in flow, repetition reduction, and mention handling
- CSS/styling issues in CMS require dev coordination to fix visual rendering (font consistency, text color, spacing, pop-in effects)

**To GrowthX Business Development:**
- Account health: Strong, active production momentum; Biologica providing timely feedback and clear priorities (reproductive years/postmenopause next)
- Medical review bottleneck: Nancy handles all Biologica medical reviews; content scheduling should account for her bandwidth
- Client engagement: Brian and Elizabeth actively participating in production decisions; clear expectations about style and image direction
- Potential expansion: Image generation and styling represent a service layer GrowthX could scale beyond Biologica

---

## Overview

- AI-generated content quality is improving, but intro paragraphs need refinement
- New image generation using Nano Banana shows promise for skin textures
- Blog layout on staging site needs adjustments (font, spacing, excerpt placement)
- Next batch of articles to focus on reproductive years and postmenopause topics

---

## Key Topics

### Content Quality Improvements

  - AI-generated content showing better flow and fewer repetitions
  - Mentions in articles are improving but need smoother transitions
  - Compound sentences reduced, favoring clearer, shorter sentences
  - Using GPT-4.5 has noticeably improved output quality

### First Paragraph Refinement

  - Intro paragraphs still need work; often too generic or disconnected
  - Strategy: Provide 10 examples of good intro paragraphs for AI to model
  - Elizabeth to compile examples from existing approved articles

### Blog Layout and Styling Issues

  - Staging site shows font inconsistencies and unusual spacing
  - Excerpt placement needs adjustment (currently appears twice)
  - Text color rendering as gray instead of black in some sections
  - Pop-in text effect may negatively impact Google indexing

### Image Generation

  - New batch of AI-generated images using Nano Banana shows improved skin textures
  - Team to provide more specific guidelines for desired image style (e.g., abstract, black and white photography)
  - Consider adding interstitial images after content is finalized

### Next Batch of Articles

  - Focus on reproductive years and postmenopause topics
  - Prioritize content that can be reviewed by Nancy (medical perspective)
  - Matt to propose topics for Brian's approval

---

## Action Items

**Matthew Panzarino**
- Add instruction for contextually appropriate conclusion headers, avoid repetitive use of "moving forward"

- Review Elizabeth's good intro paragraph examples, implement in AI system for both composition and post-processing

- Review content OS, propose new batch of articles focusing on reproductive years and post-menopause


**Elizabeth Zwillinger**
- Compile 10 good intro paragraphs from existing articles into Word doc. Include article title for each.

- Collaborate w/ Brian, define 4-5 lines describing desired blog image characteristics (abstract, framing, style)


**Brian Magida**
- Flag to dev team: remove text pop-in effect, fix excerpt display, resolve gray text color, adjust spacing/padding

- Review Matthew's proposed article topics, provide feedback (thumbs up/down, other ideas)

---

## Transcript

**Matthew Panzarino:** Hello, hello.

**Matthew Panzarino:** Oh, sorry, you're muted.

**Elizabeth Zwillinger:** Sorry. I just requested access to the documents when you get a SAC that you put in Slack.

**Matthew Panzarino:** Oh, really? Oh, okay. I think it's because we had to set it up as a team and then add it to you later. Let me find them really quickly.

**Brian Magida:** What's going on, Matt?

**Matthew Panzarino:** Hey, how's it going?

**Brian Magida:** Not too bad.

**Elizabeth Zwillinger:** Brian is just trying to get me access to the Google Doc, the new articles that he sent over.

**Matthew Panzarino:** I'll make sure that when we share them in the future, you're added to that list. I think it's just that you're not part of the org on the drive. So we'll get you added. That way it's automatic in the future. You should be added to both now as an editor.

**Brian Magida:** Yeah, so I had a chance to read through them quite quickly. I'm not the writing expert, so I kind of defer a lot of that over to Liz. It does feel like we are getting tighter. There was one tactical thing that I thought of as I was going through it — overall the mentions are good. In the key takeaways, I thought those mentions are good.

**Matthew Panzarino:** The way they're written is better.

**Brian Magida:** So I feel good about that. But it's almost like from a pipeline perspective with the mentions that are in the article itself, I just wanted to clarify with you how that happens. Because I think they're also getting better, but there's sometimes like it writes the content, then it knows, okay, we need to insert a mention here. And then it inserts the mention, but does it then go back and look at the copy that's before it just to make sure that there's like a transition between the two?

**Matthew Panzarino:** Yeah, it does. I'll explain the way it works from a functional perspective. When it composes the article, it knows from the beginning that a mention needs to be there. So it puts a mention there, but then it goes back and ensures that the ingredients mentioned have the proper brand names and trademarks. So when the native mention — I could dig one out and show you — but the native mention is pretty much the same context, but it is written so that the ingredients are just like, "Biologica's Midlife Essentials contains calcium. It contains L-theanine and Saffron," but no trademarked names. So it should write it holistically. The alcohol one, I actually think I was looking back at the draft. I think that's my fault as an editor because I didn't like the way that the trademarks were inserted there. So I fixed them and I think I deleted the connection sentence. So I apologize. And if you look at the calcium one, I actually do think it flows better. Like it said, "Hey, this routine can be complex. We have a solution for that complexity, and it's that this is a well-integrated system that we have composed in a way that actually treats your body right and gives good saturation." So yes, I will go check the actual instructions in the compose portion to add an explicit instruction to ensure that there's a natural and organic transition between the section before and after the CTA, because it's fully valid and it should flow. And like, you want it to be, "Hey, we're building up the complexity of doing this yourself, and then guess what? We've got a solution for you," or some other natural way to integrate it. So that's valid.

**Brian Magida:** Yeah, cool. And then I think you saw this, but many articles have like a start, middle, and an end, and it's like "now we're going to do this moving forward." It's like, in this example, "moving forward" was used twice, and I think it might just be a function of the types of articles that we were reviewing, because not all the articles have this moving forward thing. But I don't know if there's like some way to get around it.

**Matthew Panzarino:** I'll look at it. That's an instruction we can give — we can say, "Don't use something simple and generic like moving forward. Make sure that it's a contextually appropriate call out for the conclusion." We read a ton of articles that have conclusions, and usually it's pretty good about creating contextually appropriate H3s or H2s. So that's fine, we'll figure it out. We'll make sure that it's not repetitive. And it's the same thing with the "broken" and "failure" bits. Those are used a lot, because frankly, they're part of our original system, where we're saying, "Hey, we want to be empathetic. We want people to understand that their bodies are broken, it's not a personal failing, this is a biological reality." So I will just add some instructions in post-process to say, "If you're using these phrases, find other ways to say them." We'll do that going forward.

**Brian Magida:** Yeah, that was really the feedback that I can be the most constructive with. I think the rest is good.

**Matthew Panzarino:** Yeah, yes. A couple of the things that you mentioned as well — and you may see as you go through Liz — like we dial back on the compound sentences quite a bit. There's still a handful of them letting a few trickle through, but they should not be like three or four clauses deep, which is the big problem.

**Elizabeth Zwillinger:** Yeah, I think it's good. And Brian, I hear you that when it's three short sentences, it feels like robotic. I'm okay with it. Like, "The effect is measurable. It's also significant." I'm fine. But unless there's an easy way for you to dial it back a teeny bit, I don't want to overcorrect again. I know it's a seesaw, and I'd rather err on the side of shorter, clearer sentences than the other way.

**Brian Magida:** Yeah, and also, I noticed in another article a four or five-word sentence that felt totally appropriate. So I'm with you. I don't want to overcorrect.

**Matthew Panzarino:** Yeah, it's a hard one. It's a hypersensitive dial. And so when you tweak it a little bit, it's like "oh no, wow, where are we?" But I will look at it, and we'll keep tweaking it. We'll keep polishing. The public has a rough 8th to 10th grade reading level, you know. I don't want to talk down to anybody, but I also don't want to get too complex. So I think direct sentences are usually the best, because you can get too fancy and then kind of get in your own way. Yeah, I think the dial where it is now, we should just leave it.

**Elizabeth Zwillinger:** So the only other comment I have — I was talking to Brian about this separately. The first paragraphs of these articles are really hard to have AI write, because trying to strike that balance of good examples, a little bit of warmth, but also being direct is difficult. I very rarely find paragraphs that actually do that without trying to edit them. The first sentence in the Calcium article reminds me of something my fifth grader would say — it's ultra generic, doesn't mean anything. Like, "What do you mean changes?" It's not a great way to start. And the alcohol intro paragraph had a book club and margarita example that I loved from the first version, but then there's so much overlap with the second paragraph. It feels like we Frankensteined it and cut from two different places, and so it doesn't actually flow.

**Matthew Panzarino:** Okay, got it. Let me take this — maybe we just have to dedicate a workflow to the first paragraph since it's so important and just take a little time to write some really specific instructions for it. The problem is, when we start writing a ton of instructions to architect the whole article at once, you can end up dribbling out the other end of the context window and it starts ignoring instructions.

**Elizabeth Zwillinger:** So instead of making instructions, can we include like 10 examples of good first paragraphs?

**Matthew Panzarino:** Yeah, absolutely. If there are examples that we can include to give it like, "Hey, here's what we mean by this," it's always valuable. Yes, it works great.

**Elizabeth Zwillinger:** I can combine the first and second paragraph of the alcohol article to make it into a great first paragraph. And from the saffron piece and other ones, we'll create examples from those as well. So how do you want me to mark that so you see what the good first paragraphs are?

**Matthew Panzarino:** You can just do it here. You don't have to be too complex. You can edit the intro paragraphs and then just mark them with a comment and I'll look at them. But what about the good ones like Saffron? I don't want to start marking up articles that have already passed all the reviews.

**Matthew Panzarino:** Oh, yeah, I see what you mean. How do we tell you that ones are good?

**Elizabeth Zwillinger:** I want to open 10 articles and get 10 first paragraphs and be like, "All these 10 are good. Use this as a model." Drop them into a Word doc.

**Matthew Panzarino:** Okay, like no extra labor needed. Just drop them into a Word doc and call it "Examples of Good Intro Paragraphs."

**Elizabeth Zwillinger:** I'll include the article name at the top of each paragraph, right?

**Matthew Panzarino:** I would say yes, the title and the intro paragraph for each article so we know what it's related to, and then we can give that as an example of good. That's how we do the mentions — "Hey, this is what a good mention kind of looks like." Examples of good would be wonderful. Thank you.

**Matthew Panzarino:** And then in the rest of the piece, the flow, I was really kind of critical about the flow of these, and it tends to flow better now. Like no repetition, no circling back in weird ways. Not a lot of incredibly off-the-wall euphemisms. And I edited these pieces, so I didn't have to edit any of those out. It's less descriptive and hyper-personal as a side effect, but I think for the bulk of the sentence, that works.

**Brian Magida:** Matt, just a question for you going back to the first paragraph stuff. This might be like an awful idea, but is there a process where, now that it wrote the article, it knows exactly what the article is about, and then goes back and rewrites the first paragraph or two paragraphs knowing the full context? Is there any benefit to going backwards or no?

**Matthew Panzarino:** No, I don't think so. I mean, we can absolutely look at it as a post-processor. Once we have these examples of good, we're going to provide them to the agentic pipeline to build the article from scratch, but we can also include them as examples of good for the post-processors. As far as composing the article, it already does that in context. The stuff it's mentioning at the beginning is already in context. It's just we don't really like the way it's putting things. It's more of a stylistic thing than a factual inclusion thing. The new pipeline doesn't have the issue it did before, where it produces each section of the article essentially in isolation and then tries to retcon them into a cohesive article.

**Brian Magida:** Okay. This is a technical question, but GPT-4.5 just came out. What do you all use for writing?

**Matthew Panzarino:** Yeah, this is written with 4.5.

**Brian Magida:** Have you noticed any big changes?

**Matthew Panzarino:** It's way better. In my personal testing, it's a lot better. It has one-shot a lot of things that 3.5 struggled with a lot. I highly suggest testing it out for any personal or internal use. I actually pushed the deadline to upgrade the pipeline to 4.5 to get it to do this stuff. So it is upgraded to 4.5. We're still acclimating a little bit to how it likes to be prompted, but in general, it's producing better results.

**Brian Magida:** Yeah, I used it once. Liz, I'm not sure if you read through the Maha brief, but it was using 4.5, and I thought that was pretty good. We're doing some separate marketing-related stuff, and I was pretty impressed with what it put together.

**Matthew Panzarino:** Yeah, yeah, I've been pretty impressed so far. I did a handful of tasks with it. I have a handful of things I give to new models when I want to test them. Is this any good? Is this any better than last time? And so far, it's pretty great. So I think we did a nice job of it.

**Brian Magida:** Okay. So unless you had other thoughts, I just want to talk briefly because I'm not sure if you saw the updates in Slack. So we're working on the content. We'll get the content dialed in, feel optimistic about that. The next phase is publishing the content. So Liz, just so you know, there are two examples that are in staging right now. And we're discovering just a couple of almost minor bugs as it relates to how the content is getting presented back to the user on the front end.

**Matthew Panzarino:** Yeah, I could talk you through a couple of things. The font thing, that's something that has to be defined on the CMS side. Once you define your font, it should carry the font over. This is probably not your system font, or if it is, we got lucky, but it will adhere once you define it. A couple of other things, spacing — it's up to you, but this feels pretty loose to me overall. So this is not something we can control. We're entering the text as is, so there's probably just some extra line breaks or padding in the template. So I would check that out and see what's going on. Overall, I am not a huge fan of this pop-in, the way the text pops in. And neither does Google. Google hates it. It needs to scan the page the same way a human would do, and so when you do pop-in, it can truncate, and then it's like it doesn't index properly.

**Brian Magida:** Yeah, I'll flag that to the team. We have the ability to control that. Then, Liz, this is getting in the weeds, but we're running into a similar style issue with these weird breaks on the ingredient pages. All of this has been flagged to the team. And then there's the excerpt — it's supposed to appear like if you're on the main blog page when you see an article summary. I don't know why it's coded to also appear on the article page. So for whatever reason, the excerpt appears twice, which is weird. Because we want to be able to target actual copy there. Maybe it's the first paragraph goes there. And then the key insights are fixed at the top, which maybe is fine for some. But for others, it might be better to be after the first paragraph. We just don't have the ability to move that content around. So I think it's an easy change on their end, but we just have to build that. And the font thing is driving me insane.

**Matthew Panzarino:** We'll get that resolved. And then I wanted to flag that I'm not sure why these are rendering gray, not black. We didn't obviously format them as gray.

**Brian Magida:** The CSS does weird stuff with text. On the blog, it's like a rich text editor. On the ingredient pages, it's like a standard text editor, where you can code in various text treatments. And for whatever reason, if you create a list in there, it creates a ton of extra space, and then you have to manually remove space. But it depends where the list is in the block. Further down, if you have two lists, you have to adjust the spacing differently, depending on where the list is inserted. It's all controlled by the CSS in some odd way, and the font changes midway through. But the gray thing I didn't notice, so I'll make sure to flag it.

**Matthew Panzarino:** Yeah, other observations — we've got a new batch of images for you to look at. Give us feedback. We updated the pipeline to Nano Banana, which is a lot better at skin texture, specifically. I looked at them, and I think they look pretty great. We're talking like arm hair and various skin texture stuff that is much improved, less plasticky. And we also used your guidelines or your images you provided us.

**Elizabeth Zwillinger:** Where can I see those?

**Matthew Panzarino:** They are in the channel.

**Brian Magida:** I think we still need work on them. The actual images that were created are quite impressive. It's just, they're not the right type of images that we want for the content. Like poses and stuff or like framing?

**Brian Magida:** I think for the blog, it's more like we want pictures of people, but like you shouldn't know who they are. It's kind of like more of like an abstract image. But we should just talk about it — we have time to figure it out.

**Matthew Panzarino:** So my ask on that would be figure it out, and then basically come up with like four or five lines describing the kinds of images that you want. I can refine those into prompts. You don't need to go crazy. But basically, what are the characteristics? Is it abstract? Is it a tight shot that obscures the identity? Is it the backs of heads? Like, basically art direction.

**Elizabeth Zwillinger:** Yeah, you know, because our site is a lot of black and white photography. Beautiful black and white photography of like an orchid or in a glass of water — kind of blurry, a little more abstract. It doesn't necessarily mean something specific, like we don't have to have a picture of a glass of wine for the alcohol article. It's just, you know, evocative. Flowers is like a safe, easy option, but kind of blurry, black and white, that kind of vibe. I think we can put some of that into the huge blocks of text just to make it a little more interesting.

**Matthew Panzarino:** Yeah, we can look at that. The good news is that kind of stuff is easy to generate. I think we should put interstitial images behind getting the content right and then going into high production mode so you have plenty of content when the site goes live. Once we have something dialed in, we'll produce a new batch for you. I think it's time for us to just produce a whole new batch for you so you see this in practice. We'll take into account all the feedback, including this session. And once we get a base layer of stuff for the site, let's revisit the interstitial images. The format of the blog, the way it's laid out right now, I don't think it's mission critical that we have something because most of the text won't be too long. But we can do something fairly straightforward that has a similar image styling, like something in a horizontal format that just breaks up the text. The alternative would be creating an illustration that matches both your brand guidelines and topics in the article, which is more complicated. But either way, we could do something for you. I think we should nail the content, make sure you have a base layer of content provided for site launch, and then we can go from there.

**Brian Magida:** I have a hard stop in three minutes. So for the next batch of articles, can you just shoot me over what you were thinking you want to do, just so I can quickly review it relative to what we already have written. I just forget where we're at.

**Matthew Panzarino:** I can go look at the content OS and see where we're at. Did we want to focus on premenopause?

**Brian Magida:** Yeah, I think I need to double check. I think there was some posts that we need to fill in, and then some reproductive years content.

**Matthew Panzarino:** I think we did a bunch of perimenopause stuff already, if I'm not mistaken. Yeah, we did the bulk of that, and then obviously some standalone ingredient-based stuff.

**Brian Magida:** For right now, I want to prioritize reproductive years and postmenopause just because we have capacity with Nancy to review all the copy from a medical perspective. All the ingredients stuff has to go through Maggie and she's kind of bogged down with a bunch of other review stuff right now.

**Matthew Panzarino:** Yeah, fair enough. I'll propose some things and you can give me a thumbs up.

**Brian Magida:** Okay, cool. Thanks. Appreciate it. Ciao.
