# GrowthX Deep Dive (Allison Gregory)

<metadata>
date: 2025-11-03
time: 16:01 UTC
duration: 46 minutes
organizer: erik@growthx.ai
participants: Erik O'Brien, Allison Gregory (Redis)
fathom_recording_id: 98694938
fathom_url: https://fathom.video/calls/460595191
share_url: https://fathom.video/share/rAy7orRjtTcyw3J_xq8EtgZj578Ny6RS
source: fathom
enriched_on: 2026-03-02 00:00 UTC
</metadata>

---

## Summary

Erik O'Brien from GrowthX received a comprehensive onboarding on Redis's brand voice, AI messaging strategy, and content approach from Allison Gregory (Redis). The dual-persona framework (Expert: confident and direct; Builder: relatable and peer-to-peer) uses three voice attributes (Direct, Relatable, Irreverent) to speak authentically to developers. Redis positions itself as a "real-time context engine" solving LLM context problems through speed, accuracy, and scalability. GrowthX will shift Redis from reactive blog content to a proactive, audience-driven topic cluster strategy spanning 3-6 months, requiring critical inputs from Allison including product terminology rules, portfolio architecture documentation, and the final AI Playbook.

---

## Context

Redis is a high-performance data platform known for speed, scalability, and real-time capabilities. GrowthX is a B2B content marketing firm engaged to overhaul Redis's content strategy and ensure brand consistency across developer-focused messaging. This deep-dive session with Allison Gregory (Redis's Senior Marketing Manager) was Erik O'Brien's (GrowthX) foundational onboarding to Redis's brand guidelines, voice frameworks, and product messaging architecture. The meeting established the shared language and ground truth for how GrowthX will create and audit all Redis-branded content moving forward, ensuring alignment with Redis's evolved brand identity (post-rebrand, ~2 years prior) and AI-forward messaging.

---

## Relevance

**To GrowthX Delivery:**
- Dual-persona voice model (Expert + Builder) with three attributes (Direct, Relatable, Irreverent) provides a clear framework for content calibration and AI prompt refinement. The direct/relatable split maps to branded vs. technical content.
- Writer tool integration enables style rules enforcement; GrowthX must coordinate with Redis's Writer instance to pull terminology rules, approved abbreviations (docs, apps), and no-pun policies.
- Portfolio architecture terminology shift (e.g., "Redis Cloud" vs. "Redis Enterprise") is a critical input for content calendar planning; without this doc, GrowthX risks misalignment on product naming.
- Topic cluster strategy (50-80 ideas, audience-specific messaging tied to developer/operator/architect personas) requires persona artifacts and competitor/keyword gap analysis as inputs.

**To CheckThat:**
- Redis's core positioning as a "real-time context engine" for LLM memory and context management is directly relevant to CheckThat's AEO research and AI visibility strategy. This meeting confirms developer-first messaging as the default, even when targeting operators or architects.
- AI guardrails (no puns, sentence-case titles, no verbose/jargon language) align with CheckThat's clean-data requirements for AI-generated content quality.

**To GrowthX Business Development:**
- Redis engagement size and scope: brand guidelines deep-dive suggests a mature, well-resourced engagement with critical path dependencies (Allison owns term list export, portfolio architecture doc, AI Playbook). Expect follow-ups and iterative refinement.
- Action items assigned to Allison (term list, portfolio architecture, final AI Playbook, blog examples) due within days; Erik's writing guidelines draft due before Thursday meeting. Tight timeline suggests urgency and alignment pressure.

---

## Overview

- **Brand Voice:** A dual persona (Expert + Builder) with three attributes (Direct, Relatable, Irreverent) is used to speak confidently to developers as peers, avoiding jargon and verbosity.
- **AI Messaging:** The core message is positioning Redis as the "real-time context engine" that solves LLM context issues with speed, accuracy, and scalability, building on its trusted brand.
- **Content Strategy:** GrowthX will replace the current reactive blog process with a proactive, audience-driven topic cluster strategy to build a 3–6 month content calendar.
- **Critical Inputs:** Allison will provide key documents: a "yes/no" term list, a portfolio architecture doc, and the final AI Playbook.

---

## Key Topics

### Brand Voice & Messaging

  - **Dual Persona:**
      - **Expert:** Confident, direct, authoritative.
      - **Builder:** Relatable, conversational, peer-to-peer with developers.
  - **Voice Attributes:**
      - **Direct:** Concise sentences, active voice, periods only (no exclamation points).
      - **Relatable:** Conversational tone, universal humor (no slang), and developer terminology.
      - **Irreverent:** Punchy headlines, clever wordplay (no puns), and sentence-casing for all titles.
  - **Core Product Messages:**
      - **Fast Work:** Seamless integration & easy startup.
      - **Fast Apps:** High performance & low latency.
      - **Fast Answers:** Accessible expertise (docs, demos).
  - **Audience-Specific Messaging:** The brand guide details how core messages resonate with each audience (Devs, Operators, etc.).

### AI Playbook

  - **Problem:** LLMs forget context between sessions, causing hallucinations, repetition, and poor personalization.
  - **Current Solution:** Developers use brittle, expensive, and complex "Frankenstein stacks."
  - **Redis's Solution:** The "real-time context engine" provides a single, managed system for memory, caching, and orchestration.
  - **Key Capabilities:**
      - **Speed:** Fastest benchmarked vector database → lower latency, more processing.
      - **Accuracy:** Right data at the right time → smarter, personalized responses.
      - **Scalability:** Foundational infrastructure for startups → enables growth.
      - **Integration:** Works with 30+ AI frameworks → helps developers build the best apps.

### Content Strategy & Logistics

  - **Current Process:** Reactive blog content driven by product launches.
  - **New Strategy (GrowthX):**
      - **Topic Clusters:** Audience-based topics.
      - **Analysis:** Competitor & keyword gap analysis.
      - **Ideation:** Generate 50–80 topic ideas for Redis approval.
      - **Calendar:** Build a 3–6 month content calendar.
  - **Key Logistics:**
      - **Term Usage:** Use "fast" for branded content, "real time" for technical content.
      - **Product Naming:** Use the new portfolio architecture (e.g., "Redis Cloud" instead of "Redis Enterprise").
      - **Blog Examples:** Use for thematic guidance only; style is not the target.

---

## Action Items

**Allison Gregory (Redis)**
- Export Writer terms/names list; share w/ Erik
- Create portfolio architecture rules doc; share w/ Erik
- Share high-quality blog examples w/ Erik
- Share final AI playbook w/ Erik
- Update onboarding doc w/ portfolio architecture rules doc

**Erik O'Brien (GrowthX)**
- Draft writing guidelines; share w/ Allison before Thu

---

## Transcript
**Allison Gregory:** How are you?

**Allison Gregory:** Doing well.

**Erik O'Brien:** How's your week starting?

**Erik O'Brien:** Just getting started.

**Allison Gregory:** 9 a.m.

**Allison Gregory:** in my world, so how about you?

**Erik O'Brien:** Oh, I've had a couple hours to get going.

**Erik O'Brien:** I'm in central time.

**Erik O'Brien:** Okay, gotcha.

**Allison Gregory:** Where are you based?

**Allison Gregory:** I'm in Iowa.

**Erik O'Brien:** Oh, okay, nice.

**Erik O'Brien:** I spent about 15 years in Chicago and then just moved back to my hometown a few months ago just to take a break from the city life for a while.

**Erik O'Brien:** I get that.

**Allison Gregory:** I was in Chicago for five years.

**Allison Gregory:** It gets to you after a while.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** All the commuting, all the different things we had to start paying for.

**Erik O'Brien:** I was just like, I just want to break from this for a while.

**Erik O'Brien:** Yeah, that's fair.

**Allison Gregory:** And now's the time before it gets to be the tundra for like eight months.

**Erik O'Brien:** Yeah.

**Allison Gregory:** Well, I've got a handful of resources that I can take you.

**Allison Gregory:** Through, I kind of would leave it up to you for what's the most helpful.

**Allison Gregory:** Like, I could go in-depth through the training, but I'm almost wondering if it's better to go through kind of a lay of the land of the different resources that we have that could be inputs, but you let me know.

**Erik O'Brien:** Yeah, I'd say let's do a high-level pass-through first, and then we can kind of dive deep on which ones make sense.

**Erik O'Brien:** We did have a chance to go through, like, the Redis writing guidelines, I believe, style guide, but other than that, I think I'm starting from scratch.

**Allison Gregory:** Okay, good deal.

**Allison Gregory:** I will just share my screen then, and I'll show you what we've got.

**Allison Gregory:** Okay, this is kind of an extended list that I actually put together recently for

**Allison Gregory:** For one of our freelance writers, but I can share it with you, or I'll add it to the full onboarding doc.

**Allison Gregory:** This is the first and third bullets here are the ones that you would have seen already.

**Allison Gregory:** I'll start with guidelines because that will be the most comprehensive.

**Allison Gregory:** Under how we sound, that's where you'll find all of our verbal guidelines.

**Allison Gregory:** Our personality, we think of this as kind of the, really the persona of our brand and kind of the, the tone that our voice embodies whenever we're writing as Redis.

**Allison Gregory:** The important thing to call out here, I think, is just kind of the duality of expert being very kind of confident, direct to the point.

**Allison Gregory:** And builder being more relatable. It's about not speaking as though we are above the developers that we're communicating with. We kind of speak as though we're part of the developer community.

**Allison Gregory:** This is especially relevant for branded content for something like a technical piece or something long form, like, which lives in our blogs often.

**Allison Gregory:** That would be, we would lean more into the kind of just direct and relatable piece.

**Erik O'Brien:** So our voice, we have three different voice attributes.

**Allison Gregory:** Just touched on these a little bit.

**Allison Gregory:** The main thing is we try, and this is something that is kind of a common AI issue that we struggle with, is a lot of AI can be very verbose, very, like, long sentences connected by lots of phrases and punctuation. We just, that would be kind of an important piece of our brand is to have short, concise, meaningful sentences that just get you where you're going as quick as possible.

**Allison Gregory:** Very active voice, lots of starting sentences with verbs if it's a headline, just kind of keeping that fast value of our brand active in our voice as well.

**Allison Gregory:** Relatable, this is what I was talking about before.

**Allison Gregory:** We used to have a lot of language pre-rebrand, which happened two years ago now, that was very much like build, it was very lofty, like if you can dream it, you can build it, like that sort of thing.

**Allison Gregory:** We try to just like, we're not subservient to developers, we talk to them eye to eye, we use a very conversational tone, but also developer terminology whenever we can so that it kind of feels like we're on the same as them. The irreverence piece, again, this is the one that probably leans the most heavily into ads, short, punchy headlines for email, social media, that sort of thing.

**Allison Gregory:** So I do think for the purposes of the content that GrowthX will be focusing on, probably direct and relatable is mostly where you guys will live.

**Allison Gregory:** That said, I think a headline, something at that sort of altitude could lean into irreverence a little bit.

**Allison Gregory:** Maybe the first sentence of an intro or conclusion paragraph, like those might be the places where that could live.

**Allison Gregory:** But really, this is just supposed to be kind of a punchy, confident tone of voice.

**Allison Gregory:** We always use periods, never exclamation points, because we just want to sound confident and like we know what we're talking about.

**Allison Gregory:** Yep.

**Allison Gregory:** I won't go through all of these, but just to kind of orient you in what's in here.

**Allison Gregory:** For each of the attributes.

**Allison Gregory:** For

**Allison Gregory:** So we kind of have these guardrails for tonally what it is and what it's not.

**Allison Gregory:** And then there's three different voice techniques for each of the attributes.

**Allison Gregory:** So for direct, like these are just before and after examples of how we would remove words to say something more concisely.

**Allison Gregory:** I'm not sure if this is the kind of thing that could be an input.

**Allison Gregory:** Maybe the afters would be.

**Allison Gregory:** I'm not sure exactly how that would work on the back end.

**Erik O'Brien:** Yeah, we can, we include quite a bit of examples in our writing guidelines.

**Erik O'Brien:** Okay.

**Erik O'Brien:** So yeah, we'll definitely take this.

**Erik O'Brien:** And I think is the redis style guide that has writing guidelines fairly similar to this version.

**Erik O'Brien:** The style guide is editorial rules.

**Allison Gregory:** Okay.

**Allison Gregory:** It won't have the tonal guidance like this does.

**Erik O'Brien:** So we'll have the examples here.

**Erik O'Brien:** Yeah.

**Allison Gregory:** Yeah.

**Allison Gregory:** So for each of the three attributes, we have examples.

**Allison Gregory:** Get to the point and state the benefit are very much focused on leading with something that matters to our audience.

**Allison Gregory:** I think a lot of times with technical content, we get very caught up in talking to ourselves and pushing product versus pushing a benefit to the end user.

**Allison Gregory:** And so that's kind of what the emphasis is here.

**Allison Gregory:** Relatable, I think the most important thing here would be we're not, we don't verge into slang.

**Allison Gregory:** So we, particularly because we want our copy to always feel universal.

**Allison Gregory:** So even whenever we use humor, kind of in the more of the irreverent tone, we try to make sure that that's something that could translate across different audiences.

**Allison Gregory:** We've got a team of international copywriters also who kind of help us, you know.

**Allison Gregory:** So make sure that if something's being recreated in Brazil, for example, we're not just translating directly because especially some of that humor stuff won't translate.

**Allison Gregory:** It's more transcreated to be rewritten in a way that ends with the local markets.

**Allison Gregory:** A couple notes here.

**Allison Gregory:** Keep it casual.

**Allison Gregory:** This one, we use abbreviations, so that will be included in the style guide.

**Allison Gregory:** Docs, apps.

**Allison Gregory:** Oh, gosh, what are the other ones I'm forgetting?

**Allison Gregory:** There's a full list.

**Allison Gregory:** Forgive me, it's early for me.

**Allison Gregory:** There's a full list of all of the words that we abbreviate in the editorial section, though.

**Erik O'Brien:** Okay.

**Allison Gregory:** Name the challenge.

**Allison Gregory:** Kind of the flip side of naming the benefit.

**Allison Gregory:** If we know that there's a particular struggle that our offering is overcoming for developers, we like to lead with that.

**Allison Gregory:** And just...

**Allison Gregory:** State it clearly.

**Allison Gregory:** Something like compliance is a time suck.

**Allison Gregory:** then state the benefit.

**Allison Gregory:** Be a peer.

**Allison Gregory:** This one's more about kind of situational language.

**Allison Gregory:** So this bottom right example of eight hours into one small change, we've got you.

**Allison Gregory:** It's more about like demonstrating that we kind of get what it's like to be in a developer's seat and kind of what the the daily pains are that they might experience.

**Allison Gregory:** And then irreverent.

**Allison Gregory:** I think we've got four techniques here.

**Allison Gregory:** Embody the expert is kind of the most holistic definition of what we mean by irreverent, which is that we don't say something soft, like we save you precious time and energy, we would just say you have better things to do.

**Allison Gregory:** So it's kind of stating it very clearly and confidently and behaving or speaking as though we know what

**Allison Gregory:** That's best for you.

**Allison Gregory:** Cheekiness.

**Allison Gregory:** We do, we'll use some clever wordplay.

**Allison Gregory:** We never use overt puns.

**Allison Gregory:** That's a hard line for us, unless it's, pretty much unless it comes from our brand team and we're using it for swag at an event or something.

**Allison Gregory:** As a company, we used to abuse puns pre-rebrands, so we took them away.

**Erik O'Brien:** Yeah, it's always hard to get AI to do puns anyway, so that works easy.

**Erik O'Brien:** Good.

**Allison Gregory:** Okay, punch it up.

**Allison Gregory:** This one's mostly about punctuation, and some of this should be in the style guide as well.

**Allison Gregory:** But anytime we can break up a long sentence, make it several short sentences for a headline, or break it up with an M-dash.

**Allison Gregory:** AI loves an M-dash.

**Allison Gregory:** Yes, it does.

**Allison Gregory:** We just like.

**Allison Gregory:** So that's part of how we kind of create that bold tone.

**Allison Gregory:** And I don't think this will be relevant to blogs, but we use sensory words kind of more in experiential spaces.

**Allison Gregory:** Something like smells like new business feels pretty disruptive at a tech event.

**Allison Gregory:** Moving into messaging, we break down our audiences here.

**Allison Gregory:** Pretty much our default as a brand is to speak as though we're talking to developers, regardless of who our audience is.

**Allison Gregory:** The reason we do that is because while developers are not usually the decision makers at a company, they have a lot of sway on what technology their teams will end up using.

**Allison Gregory:** And as part of a formerly fully open source kind of dev community brand, that's just something that we try to maintain.

**Allison Gregory:** Just scroll down here.

**Allison Gregory:** think I'm actually going to, well, I'll hit up this one first.

**Allison Gregory:** These are our three product messages that sit at the highest level for our brand.

**Allison Gregory:** I think we talked about this a little bit on the briefing call the other day.

**Allison Gregory:** These are basically the three things that we are known for and that since the rebrand, we've been trying to own at the highest level for our brand.

**Allison Gregory:** So the first is fast work, which is that we're seamlessly integrated into their stack.

**Allison Gregory:** It's very easy to get started with Redis.

**Allison Gregory:** And so also once you get started, it's very easy.

**Allison Gregory:** There's less data management needed from us, less sort of having to accommodate different programming languages and that sort of thing.

**Allison Gregory:** So everything about the working process is faster.

**Allison Gregory:** Fast apps.

**Allison Gregory:** Fast

**Allison Gregory:** is the fast performance piece.

**Allison Gregory:** This is kind of our bread and butter, the thing that we've always been known for.

**Allison Gregory:** And fast answers.

**Allison Gregory:** This one's more about that in-house technical expertise.

**Allison Gregory:** So being able to just work without interruption because you have resources in people form, in demo form, documentation, whatever you need.

**Allison Gregory:** You can kind of keep working quickly.

**Allison Gregory:** So those are the three things that we try to weave in wherever possible, not verbatim with these birds.

**Allison Gregory:** But just thematically, those are the three that we're reiterating.

**Allison Gregory:** This chart here is not the most visually appealing.

**Allison Gregory:** Let see if I can make this a little bit easier to digest.

**Allison Gregory:** For each of our four audiences, and really we can kind of ignore the employees column for now, we've basically broken out strategically what each of those three brand messages characters.

**Allison Gregory:** Yeah.

**Allison Gregory:** Or three product messages mean to each of our audiences.

**Allison Gregory:** So, fast work, for example, means something different to a developer.

**Allison Gregory:** means they can integrate with any language.

**Allison Gregory:** They can keep working in their tech stack than it would to an operator who's more concerned with scaling solutions and solving challenges for their team very quickly.

**Allison Gregory:** So, that's what these columns are.

**Allison Gregory:** For fast work, fast apps, and fast answers, we've kind of broken down.

**Allison Gregory:** This is what it means to each of these different audiences.

**Allison Gregory:** I'm not sure.

**Allison Gregory:** I guess I would love to know from you.

**Allison Gregory:** think tonally, I understand how we can give good examples of what tone is.

**Allison Gregory:** can give the guidelines.

**Allison Gregory:** With messaging, is this something that we can kind of input and say?

**Allison Gregory:** I guess the audience-specific messaging feels a little bit hard.

**Erik O'Brien:** Yeah, so we also have another key artifact is personas.

**Erik O'Brien:** And so if we can, you know, in the kind of outline that we create prior to the full kind of article, like specify like this one, like target developers and architects or just specifically developers, then we should be able to kind of hone in on what they care about, what messaging resonates with them.

**Erik O'Brien:** And so it'll take some calibration to get there, but we are able to kind of pinpoint like this one, this specific for developer audience, this one is for architect audience, and then follow the guidelines and kind of what matters most to them.

**Erik O'Brien:** So I've also seen it like break out different artifacts if we need to get very specific to kind of have their own writing guidelines per audience.

**Erik O'Brien:** So we'll...

**Erik O'Brien:** Kind of get through calibration and see how much we need to tune those.

**Erik O'Brien:** Okay.

**Allison Gregory:** Sounds good.

**Allison Gregory:** The other thing to include or to mention here, we have these different, this asset section.

**Allison Gregory:** It has our latest boilerplate.

**Allison Gregory:** It also has kind of the short, medium, and long version of how we describe Redis.

**Allison Gregory:** So these are good ones, just truly can be just grabbed verbatim for how the actual words that we use to describe ourselves.

**Allison Gregory:** And then quick references.

**Allison Gregory:** This is, I believe most of this should be reflected in our style guide, as I'm saying that out loud.

**Allison Gregory:** So the style guide is actually built from an AI tool that we use on the writing team.

**Allison Gregory:** It's called Writer.

**Allison Gregory:** And it's preset rules that we can basically choose what we want the correct answer to be, like how we treat AM and PM.

**Allison Gregory:** And how we use periods, that sort of thing.

**Allison Gregory:** There are some specific rules that, like in this case, we have different rules for a digital ad versus web and email style that we can't get that granular on Writer.

**Allison Gregory:** So some of the pieces that live in this quick references section will be a little bit deeper than what's in that style guide, if that makes sense.

**Allison Gregory:** A lot of these, if not all of these, are things that I've kind of covered along the way.

**Allison Gregory:** We, one big thing here is that we always use the word fast, if it's in a headline or if it's branded content.

**Allison Gregory:** If it's, if we're referring to Redis or one of our capabilities in a paragraph where it's technical, we refer to it as real time.

**Allison Gregory:** So there's kind of a distinction there. Otherwise I think I covered those.

**Allison Gregory:** We always use second person.

**Allison Gregory:** So instead of saying developers, we would say you, instead of saying redis, we would say we. Rules on Oxford commas, that sort of thing.

**Allison Gregory:** The biggest thing that we struggle with, even with writer, is that we use sentence casing everywhere always.

**Allison Gregory:** So in a headline, we only capitalize the first word, even in subheadings, titles of a blog, whatever it may be.

**Allison Gregory:** Um, we've found that AI has a little bit of a hard time learning that sometimes, but it depends on the platform.

**Allison Gregory:** So, um, just something to flag.

**Allison Gregory:** Gotcha.

**Allison Gregory:** Here's our list of abbreviations.

**Allison Gregory:** Docs, devs, devs would be only in a headline.

**Allison Gregory:** And most of these abbreviations are really like headline specific.

**Allison Gregory:** If it's a technical long form piece, we can use the long form version of the word.

**Allison Gregory:** Skipping ahead, there's a handful of phrases that we don't use anymore from kind of the old version of the brand.

**Allison Gregory:** And this one is maybe worth asking about.

**Allison Gregory:** Now, also in Writer, and actually I could download, I think I can export this for you, and I should have done that before.

**Allison Gregory:** But we have a list of terms that we basically built rules around so that anytime someone submits a piece of content to Writer, it will flag different terms.

**Allison Gregory:** Like Redis Enterprise is a good example.

**Allison Gregory:** They used to call our paid offering Redis Enterprise, and now it's just Redis Cloud and Redis Software.

**Allison Gregory:** That's something that we've tried to make a wholesale change on.

**Allison Gregory:** And there's still.

**Allison Gregory:** Well, documentation that says Redis Enterprise, product teams will never use it the correct way.

**Allison Gregory:** So there are places like if you were to give a broad resource like our website, then it could extract Redis Enterprise and that would be incorrect.

**Allison Gregory:** So maybe the best thing to do would be I can just export that list of yes, no terms and share that with you guys.

**Allison Gregory:** And we can create tools around that or rules, excuse me.

**Erik O'Brien:** Yep, that would be wonderful.

**Allison Gregory:** Okay, let me make a note to myself to do that.

**Allison Gregory:** Okay.

**Allison Gregory:** Other than that, the name and number formatting, all of these different pieces, should live in our guidelines or the style guidelines.

**Allison Gregory:** Okay. So here, this is where this will have most of our terms, if not all.

**Allison Gregory:** I think we did actually add, yeah, there is a no-go phrases section, but it doesn't have the comprehensive list of terms, so I'll add that to the list.

**Allison Gregory:** This is something, I'm not sure the best way to use this as an input, but I do think it's important.

**Allison Gregory:** We, this is going to look really tiny on the screen.

**Allison Gregory:** Basically, about six or eight months ago, we did this exercise of creating our portfolio architecture for the company.

**Allison Gregory:** Basically, we had just a whole slew of different types of offerings, and there was much debate, especially anytime we wanted to name something, going to over.

**Allison Gregory:** We,

**Allison Gregory:** What's a solution?

**Allison Gregory:** What's a product?

**Allison Gregory:** What's a package?

**Allison Gregory:** What's a tool?

**Allison Gregory:** And so we made definitions for all of those things, and then we categorized all of them so that we could kind of make sense of the web of our offerings.

**Allison Gregory:** All that's to say, this is still relatively new in the world of Redis.

**Allison Gregory:** People are still learning it.

**Allison Gregory:** Some people don't use it, but we are trying to enforce that.

**Allison Gregory:** But, yeah, I think I'd be looking for guidance on this.

**Allison Gregory:** If there's any way that we can somehow create, like, input these definitions or share buckets of, like, what's what so that it knows, like, okay, if you see the term caching, that's a solution.

**Allison Gregory:** That would be best.

**Allison Gregory:** I don't know if that's too in the weeds.

**Allison Gregory:** I would say...

**Erik O'Brien:** say...

**Erik O'Brien:** We typically have, like, a separate artifact that we create that's around products and solutions.

**Erik O'Brien:** Okay.

**Erik O'Brien:** And so I know we did get a deck of, like, all use cases plus solutions with technical implementations with those.

**Erik O'Brien:** From?

**Erik O'Brien:** That was from John Hoonan, the solutions library.

**Erik O'Brien:** Okay.

**Allison Gregory:** He, the solutions library is kind of an extension of this.

**Allison Gregory:** So that's great that you guys have that.

**Allison Gregory:** I do think I'll, if you have that, do you have that link handy by chance?

**Allison Gregory:** Yes.

**Allison Gregory:** This is kind of the preamble to the solutions library.

**Allison Gregory:** That goes into the weeds of, like, all of the benefit messaging around each of the.

**Allison Gregory:** Different solutions.

**Allison Gregory:** I'm just not sure if it will have the simple articulations and bucketing of what's what.

**Erik O'Brien:** Do you want me to share the link or do you want me to show you what we have?

**Allison Gregory:** Yeah, here I can stop sharing if you want to just bring it up.

**Allison Gregory:** Thank All right.

**Erik O'Brien:** So.

**Erik O'Brien:** Let's skip to solutions and tech implementations.

**Allison Gregory:** Gotcha.

**Allison Gregory:** Okay.

**Erik O'Brien:** Scashing, then tech implementation, definitions, and how it works.

**Allison Gregory:** Okay.

**Allison Gregory:** Yeah.

**Allison Gregory:** These are really great slides.

**Allison Gregory:** I think it would still be helpful, and if we need to, I can also pull it into, like, a Word document that just bullets out, like, if you see this term, refer to it as a solution, like those sort of rules.

**Allison Gregory:** I think there's just, like, the one step above this.

**Allison Gregory:** That's just how we refer to these different things.

**Allison Gregory:** Okay.

**Allison Gregory:** So I can make a note to do that.

**Allison Gregory:** Would that be the best format, like, just to create a rule?

**Allison Gregory:** Around those things and put it in a doc?

**Allison Gregory:** Yeah, I think so.

**Erik O'Brien:** That way, because we'll create an artifact and we can have you guys review it just to make sure it's all accurate.

**Erik O'Brien:** But that would probably be the best way to go about it.

**Erik O'Brien:** Okay, good deal.

**Allison Gregory:** Other than that, I think that is everything.

**Allison Gregory:** So I'll bring, I'll export the terms and names from Writer for you.

**Allison Gregory:** I'll turn the portfolio architecture, that one-up slide into some rules in a doc.

**Allison Gregory:** But otherwise, I think that's what we've got.

**Allison Gregory:** Is there anything?

**Allison Gregory:** The other question, I guess, would just be, do you need examples of like, I know this kind of came up on the call the other day about like, what would be good examples?

**Allison Gregory:** I'll bring, bring, bring, bring, bring, you.

**Allison Gregory:** To use as inputs.

**Allison Gregory:** Our blog has not historically been the best examples of how we want content to look.

**Allison Gregory:** So while like it's true that there's content that has performed well and that's great, but I think we should use that as like thematic guidance, not style guidance.

**Allison Gregory:** Yeah.

**Allison Gregory:** Yeah.

**Erik O'Brien:** And I met with Fung Lin and Alexis on Friday just to go over kind of more of like performance and keyword strategy.

**Erik O'Brien:** So I think we've gotten that direction.

**Erik O'Brien:** But yeah, if there's specific pieces that do follow kind of the rules very well, that would be fantastic to reference.

**Allison Gregory:** Yeah, I can share.

**Allison Gregory:** We've got a few of those going.

**Allison Gregory:** Actually, a guy on my team has been working on building a GPT for our team.

**Allison Gregory:** So he's been compiling some of those examples.

**Erik O'Brien:** Yeah, I of love GPTs.

**Erik O'Brien:** We have one client that's in the financial industry, and they have a GPT just for all of their compliance rules.

**Erik O'Brien:** And so we've kind of borrowed their version to create our own of just like, anytime you mention specific features, has to have this compliance byline.

**Erik O'Brien:** And we're just like, yeah, that's a bit detailed for our pipelines.

**Erik O'Brien:** But GPT seems to work really well for like post-processing.

**Erik O'Brien:** Yeah, it's pretty cool.

**Allison Gregory:** I guess my other question would just be more broadly, like, I think I mentioned this on the call, but we've never had like a blog strategy.

**Allison Gregory:** It's very reactive, like, oh, product is rolling out this thing.

**Allison Gregory:** I guess we better whip up a blog.

**Allison Gregory:** And that's more coming from like, like, I think our product marketing team.

**Allison Gregory:** And...

**Allison Gregory:** It's not their fault.

**Allison Gregory:** Like, our product team doesn't exactly have a pristine roadmap for us to work from.

**Allison Gregory:** But I guess, what's the next step or recommended process for building out, like, a sort of a cadence of a content strategy?

**Erik O'Brien:** Yeah, so our approach is typically to go with topic clusters.

**Erik O'Brien:** So very much audience-based of, like, what does the audience want to read about, care about.

**Erik O'Brien:** And so we develop these clusters that will have many different kind of topics under those.

**Erik O'Brien:** And based off those topic clusters, we curate anywhere from, like, 50 to 80 kind of topical or assignment ideas.

**Erik O'Brien:** And then we'll have your guys' team just kind of go through and approve, like, you know, these ones seem to match well with our audience and kind of thematically of what we want to go for.

**Erik O'Brien:** And so that'll help us build out a content calendar of sorts for us to kind of...

**Erik O'Brien:** They can choose which ones we go after sooner than later, and then also have a backlog of ideas that are just, again, really kind of resonate with the audience.

**Erik O'Brien:** And so for us, it starts with the topic clusters, and then we go in and do a bunch of competitor and keyword gap analysis to kind of see, you know, what's the market talking about that we're not quite talking about yet, especially as you guys transition or at least try to move into more of that AI infrastructure kind of play in audience.

**Erik O'Brien:** So we'll come up with plenty of at least topic ideas to go after with those topic clusters.

**Erik O'Brien:** And then that helps us at least create, you know, a laundry list of topics to go after for the next, you three to six months.

**Erik O'Brien:** And then we continually kind of refresh that, you know, if there's product moving or product launches that might adjust some of the topic clusters or even kind of micro content that we go after.

**Erik O'Brien:** So that'll be at least the way that we approach.

**Erik O'Brien:** I'm kind of building out a content calendar for you guys.

**Erik O'Brien:** Okay, great.

**Allison Gregory:** You also mentioned AI, which I should mention.

**Allison Gregory:** Our updates, our final edits to the AI playbook that I mentioned last week are going to be inputted this week.

**Allison Gregory:** So I should be able to share that playbook with you very shortly.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Yeah, that was the other part of today.

**Erik O'Brien:** I wasn't sure if we were going to get to, but yeah, let's wait until that's finalized.

**Erik O'Brien:** And then we can take a look at it, and then if we need another deep dive or kind of walkthrough of, you know, what does this mean in context of what we're doing, we might just schedule that as well.

**Erik O'Brien:** Yeah, I actually think we've got a few minutes.

**Allison Gregory:** It's close enough that I could share with you what we've got, and then I'll just send over the final version.

**Erik O'Brien:** Okay.

**Allison Gregory:** If you want me to just go ahead and take you through that now.

**Erik O'Brien:** Yeah, let's do it.

**Allison Gregory:** The pieces that we don't have are kind of the, like, do's and don'ts.

**Allison Gregory:** It's kind kind

**Allison Gregory:** Kind of rules, like we do say this, we don't say that, we do have our key messages built up.

**Allison Gregory:** Okay.

**Allison Gregory:** I'm going to skip around here a little bit.

**Allison Gregory:** This was just one of our internal decks, but basically the way this starts is that this is kind of the big problem as articulated by our CEO, the big problem in terms of what Redis can solve, is that in between sessions, LLMs forget everything and they need to have the exact right information at the right time.

**Allison Gregory:** If they don't, this results in content.

**Allison Gregory:** Text problems that show up in the form of hallucinations, repetition, poor personalization.

**Allison Gregory:** The way that developers are currently kind of combating that is by cobbling together these Frankenstein stacks that have a vector DB from one place, a cache from another place, an external API and all of these pieces kind of work for now, but as they try to scale, that's going to be really brittle and expensive and complex to manage.

**Allison Gregory:** So what that means for us, basically this boils down into three key problems that LLMs forget data in between sessions, meaning that the dev outcome for that is lost context, having to redo work in consistent outputs.

**Allison Gregory:** Number two, models don't have access to the right context at the right time, and they have these issues that we just talked about.

**Allison Gregory:** And number three, there's no single stack currently that has the right mix.

**Allison Gregory:** And

**Allison Gregory:** Of both traditional and AI dev tools that will be able to scale with them.

**Allison Gregory:** So they have these Frankenstein stacks.

**Allison Gregory:** So for us, the outcome or the benefit that we provide in a variation of combinations really comes down to speed, accuracy, and scalability.

**Allison Gregory:** I think this would be probably an important slide.

**Allison Gregory:** These are kind of broken down bullets on the capabilities that we do provide.

**Allison Gregory:** So we consider Redis a strong offering to gather, sync, and serve data from all of these different places, both your short-term memory, your long-term memory, your live external data, and your system knowledge.

**Allison Gregory:** And then the way we do this is through in-memory speed for real-time lookup, vector search for long-term semantic memory, streams and pub subs, flexible data structures, and think difference in think

**Allison Gregory:** RDI, which is Redis Data Integration, so helps kind of support that story of extracting context at the right time and place.

**Allison Gregory:** Is RDI a newer product or offering?

**Allison Gregory:** I think we rolled it out about a year and a half ago.

**Allison Gregory:** This is kind of a common challenge that we have, which is that there will be a big push about something right whenever the release happens, but then we get excited about the next thing.

**Allison Gregory:** And so we actually just had an event series this summer where we had a big push for RDI, and then all of a sudden, because we had one big push, we talk about it as if everyone knows it.

**Allison Gregory:** But in our keynote, our CEO, like, we were in Bangalore, which is one of our largest markets, and he was like, raise your hand if you've heard of RDI or Redis Data Integration.

**Allison Gregory:** Maybe like six people out of 500 raised their hand.

**Allison Gregory:** So we have this issue.

**Allison Gregory:** Two of like losing track of releases after the initial push.

**Allison Gregory:** Gotcha.

**Allison Gregory:** So these are kind of, this is what we know about where we can and can't win.

**Allison Gregory:** The places where we cannot win our cost and distribution, hyperscalers like Amazon and Google will always have us beat because their CSPs, they just have all of their tools and services under one umbrella and people, there's also lock-in.

**Allison Gregory:** So once people start using them, they're kind of, they're, it serves them well to just stay with the one company.

**Allison Gregory:** The places where we can win our speed.

**Allison Gregory:** We have the fastest benchmarked vector database.

**Allison Gregory:** We have data to show that.

**Allison Gregory:** think there was a blog that performed relatively well about that actually.

**Allison Gregory:** So when it comes to fast memory retrieval, so being able to.

**Allison Gregory:** To extract data from any source in real time, we deliver there.

**Allison Gregory:** That's probably the easiest thing for us to sell as far as benefits because speed is the thing that we're known for in every other offering as well.

**Allison Gregory:** Accuracy is a bit of an outcome of speed.

**Allison Gregory:** So because we can retrieve data faster, you can do more processing at lower latency, which then results in better output.

**Allison Gregory:** And then scale and versatility.

**Allison Gregory:** We have hybrid search capabilities.

**Allison Gregory:** We integrate with 30-plus different AI frameworks that are already on the market today.

**Allison Gregory:** We have one managed system that brings together vectors, JSON, and search.

**Allison Gregory:** And then we have easy integration into any enterprise stack.

**Allison Gregory:** So our AI positioning.

**Allison Gregory:** This first line of who we are, this is the short.

**Allison Gregory:** The one-line version of how we refer to ourselves in the context of AI, which is the real-time context engine.

**Allison Gregory:** What we do is help developers build fast, accurate AI apps that scale.

**Allison Gregory:** And then how we do it, we search, gather, and serve AI data in one place, providing the memory, caching, and orchestration that agents need to perform personalized tasks fast.

**Allison Gregory:** This is one thing that might be changing.

**Allison Gregory:** I think they wanted to, I think collaboration or something was the, I won't even guess because I can't remember what it is right now.

**Allison Gregory:** Orchestration might be changing.

**Allison Gregory:** Gotcha.

**Erik O'Brien:** And that was, I was going to have a question on LLMs versus agents, but that seems to have resolved that question.

**Erik O'Brien:** Oh, okay.

**Allison Gregory:** Gotcha.

**Allison Gregory:** The why behind all of this is essentially that, whoops, without Redis, apps, apps,

**Allison Gregory:** And AI tech stacks will inevitably hit a wall, either with speed, because as they grow users or add different functionality, it just won't be able to scale and maintain all of that change.

**Allison Gregory:** It'll be harder to manage.

**Allison Gregory:** In time, it likely will break.

**Allison Gregory:** And the thing that we know to be true about AI is that there are so many options, there's really zero tolerance for something that doesn't work, because there's another option that they can go to.

**Allison Gregory:** So in order to maintain happy users, you really have to be the best, the best, fastest, smartest, et cetera.

**Allison Gregory:** So kind of the why behind it is that Redis has kind of always just been known pre-AI days as just a service that just works.

**Allison Gregory:** You can trust it.

**Allison Gregory:** It's very credible.

**Allison Gregory:** And we kind of want to just maintain that and say you've always known us and loved us for caching.

**Allison Gregory:** as your in-memory database.

**Allison Gregory:** Now, that same source of reliability is providing you AI functionality.

**Allison Gregory:** So the four different elements that we've leaned into are fast, accurate, scalable, and integrated.

**Allison Gregory:** And then this will be an important slide.

**Allison Gregory:** Make it a little bit bigger, actually.

**Allison Gregory:** This is essentially what we mean by each of those different things.

**Allison Gregory:** So for us, fast is about fast data retrieval.

**Allison Gregory:** It means you're going to have less latency, more processing.

**Allison Gregory:** One thing that we know is that anyone who chooses Redis for AI has to care about latency.

**Allison Gregory:** If they don't, at the end of the day, they probably won't go with us.

**Allison Gregory:** The big selling point for us is that they can stop wasting money on expensive LLM calls.

**Allison Gregory:** They'll have better throughput, guaranteed sub-millisecond responses, et cetera.

**Allison Gregory:** So these bullets across across the...

**Allison Gregory:** Bottom of the screen are all proof points, so there's verticals here.

**Allison Gregory:** So for FAST, these are the proof points, basically the facts that are true about Redis today that give us permission to claim each of the four messages.

**Allison Gregory:** I won't go into all of those because some of them are actually, that's the main thing that we'll be tweaking whenever we share this over.

**Allison Gregory:** Most of them are true, but a couple of tweaks from the technical team.

**Allison Gregory:** For accuracy, that's all about getting the right data to the right, to the right place at the right time, so that your LLM can translate that into smart, personalized responses.

**Allison Gregory:** This idea that users won't settle for anything less than that, and that we have, we can easily access your relevant short and long-term memory.

**Allison Gregory:** For scalability, the main thing here is that in order to, or the message that we want to deliver is that.

**Allison Gregory:** In order to scale your AI app, you have to start with the right infrastructure.

**Allison Gregory:** This really supports that Redis is trying to kind of get in the door with a lot of startups that are kind of building their tech stack from the ground up.

**Allison Gregory:** So they're trying to kind of be that foundational level for AI so that everything can build off of that and they can scale in the way that they need to.

**Allison Gregory:** And then integrated.

**Allison Gregory:** The sentiment here really is just that we're not trying to be the next AI company.

**Allison Gregory:** We're not just innovating and slapping our name on something with AI on it just for the sake of it.

**Allison Gregory:** Really, we're innovating in service of helping you integrate with other strong AI offerings that are out there as well.

**Allison Gregory:** So we're not kind of trying to corner the block, I guess.

**Allison Gregory:** So we're innovating so that you can keep using the tools that you are using and just build the best AI apps possible.

**Allison Gregory:** And

**Allison Gregory:** That kind of sums us up there.

**Allison Gregory:** This will become a simpler playbook, but hopefully that gives you the gist.

**Allison Gregory:** Yeah, absolutely.

**Erik O'Brien:** Cool.

**Erik O'Brien:** Awesome.

**Erik O'Brien:** So out of the docs that you had on your list, is there any that we don't have access to that we should?

**Allison Gregory:** I don't, portfolio architecture, but I'm going to turn that into a separate Word doc.

**Allison Gregory:** I'll go ahead and share it with you now, just so you have it, but I'll get you a more usable version.

**Allison Gregory:** What's your email?

**Erik O'Brien:** Erik, E-R-I-K, at growthx.ai.

**Allison Gregory:** Oh, there you are.

**Allison Gregory:** Okay.

**Allison Gregory:** Okay, that's coming your way, but I will send you a new one, and I'll add it to that.

**Allison Gregory:** That full list from the team of onboarding docs.

**Allison Gregory:** Wonderful.

**Allison Gregory:** Awesome.

**Erik O'Brien:** So, yeah, I'll try to get the team to pull all this into kind of writing guidelines, and then we'll work on the product and solutions artifact once we get that doc from you.

**Erik O'Brien:** Okay.

**Erik O'Brien:** We will try to share those prior to our meeting on Thursday, just so you guys can start to get feedback.

**Erik O'Brien:** The writing guidelines is, quite honestly, the one that gets the most feedback and has the most revisions as we get through calibration.

**Erik O'Brien:** So we won't expect it to be perfect out of the gate, but the more feedback we get, the closer we get to having it be as accurate as we can.

**Erik O'Brien:** Perfect.

**Allison Gregory:** Sounds good.

**Allison Gregory:** Wonderful.

**Erik O'Brien:** Well, appreciate the walkthrough, Allison, and let us know if you have any other kind of content or questions, and we'll be on Slack.

**Erik O'Brien:** Perfect.

**Erik O'Brien:** Will do.

**Allison Gregory:** Thank you.
