# Content Audit: Jess & Fatima

<metadata>
date: 2025-05-28
time: 14:55 UTC
duration: 29 minutes
organizer: Matthew Panzarino (GrowthX)
participants: Fatima Ismail (GrowthX), Jess Scott (GrowthX), Matthew Panzarino (GrowthX)
fathom_recording_id: 65108413
fathom_url: https://fathom.video/calls/310969726
share_url: https://fathom.video/share/iCDMCUnG_YdJBysRmwDeLZsJnYLszYFr
source: fathom
enriched_on: 2026-03-04 15:30 UTC
</metadata>

---

## Summary

Matthew conducted a comprehensive content audit of live client work and identified systematic issues with LLM-generated content, particularly "bullet point sandwich" structures and thin sections that undermine human readability and user engagement. The team discussed workflow bottlenecks with AirOps (poor linking, hallucinations, structural issues) versus ChatGPT (faster tone calibration for clients like Seat), and Matthew outlined the new sprint model approach where clients will receive fully customized polishing instructions and workflows during onboarding, moving away from generic word-count targets toward sustainable, quality-first delivery. Key focus areas include developing fact-checking workflows for health-content clients like InterVest, improving linking capabilities, and designing handoff processes for transitions from sprint teams to regular delivery pods.

---

## Context

Matthew recently joined GrowthX's delivery team and conducted a broad audit of content currently live across all GrowthX clients to assess quality and establish baseline standards. Rather than focusing purely on SEO metrics (which he found largely sound), Matthew emphasized human readability—the end consumer experience—as the area requiring immediate attention. Fatima (a content editor) and Jess (head of content delivery) have been managing multiple client accounts under varying constraints: Seat with strict formatting preferences shifting toward long-form content, InterVest with programmatic health content requiring significant fact-checking, and others like HomeBase and Tribe using AirOps workflows. This audit fed directly into conversations about the upcoming sprint model, a new onboarding approach where clients will spend 8-12 weeks with a dedicated sprint team to build out customized workflows, polishing instructions, and handoff documentation before transitioning to steady-state delivery pods.

---

## Relevance

**To GrowthX Delivery:**
- LLM-generated content relies heavily on "bullet point sandwich" structures (introductory sentence, then single-sentence bullets, then closing line) that appear generated and thin out narrative depth; this pattern is addressable through specific polishing instructions ("avoid bullet point sandwiches, build 2-5 sentence paragraphs with narrative arc")
- Current AirOps workflows have critical gaps: poor linking capabilities, fact-checking hallucinations (especially risky for health-related clients), and weak content structuring—these are not client-specific issues but platform limitations requiring workflow redesign
- InterVest programmatic content currently requires ~1 hour of post-editing per piece for fact-checking against health sources; Matthew recommends ingesting client-provided primary sources and building a dedicated fact-checking workflow during sprint phase rather than manual human review
- Word count as a success metric drives poor content; moving to "as long as it needs to be and then slightly shorter" philosophy eliminates filler and improves user signal
- New sprint model will ship with client-specific documented workflows, polishing instructions, and responsible team assignments—eliminating "try whatever tools we have" ad-hoc approach

**To GrowthX Business Development:**
- Seat account health signal: client was skeptical of long-form content due to short average dwell time (35 seconds), but team successfully pitched narrative-driven longer-form as performance lever; client approved shift, indicating openness to methodology education
- Reddit account showing strain: team is on manual edit round 5-6 on 4 pieces within a 4-week engagement wind-down period; Matthew flagged for review—potential contract scope creep or unsustainable editing cycles
- Fatima integration signal (positive): Jess publicly praised Fatima's rapid adoption, feedback integration, and collaborative impact across team; strong team fit indicating retention stability

**To CheckThat:**
- Health-content verification (InterVest use case) highlights broader B2B challenge: LLMs hallucinate medical/technical facts at scale; dedicated fact-checking workflows using trusted sources are table-stakes for category coverage
- Content quality expectations rising: moving toward human-narrative-quality output rather than "machine-readable SEO" positions GrowthX as premium provider, raising CheckThat's visibility standard by association

---

## Overview

- **Bullet point sandwiches are a systemic LLM weakness:** Single-sentence paragraphs separated by bullet lists create skeletal, generated appearance; fixable with client-specific polishing instructions
- **AirOps has hard limitations:** Poor linking, frequent hallucinations, weak content structuring; team is defaulting to ChatGPT for Seat despite prior AirOps investment due to speed and tone calibration advantages
- **InterVest's 1-hour-per-piece post-editing is unsustainable:** Programmatic health content requires professional-grade fact-checking; sprint model will ingest primary sources and build dedicated verification workflow
- **Sprint model shifts onboarding fundamentally:** Instead of "service client with available tools," teams will spend 8-12 weeks engineering client-specific workflows, documented polishing instructions, and responsible handoffs—reducing steady-state manual intervention
- **Word count metrics are obsolete:** Moving to "as long as it needs to be and then slightly shorter" eliminates filler while improving engagement and user intent alignment
- **Reddit engagement showing friction:** Multiple edit rounds within wind-down period may indicate scope creep or unsustainable client expectations; contract terms need review

---

## Key Topics

### Content Quality and Readability

Matthew's content audit identified that the vast majority of LLM-generated content is sound from an SEO perspective, but human readability is the primary issue. LLMs exhibit a strong predilection for "bullet point sandwich" structures—where a single introductory sentence precedes a bulleted list, followed by a closing statement—which makes content appear skeletal and generated. The team discussed the importance of varied paragraph structures and narrative flow; Matthew emphasized that content should be treated like "geometry," with a mix of shapes (paragraphs, bullets, imagery, headers) to create visual relief and maintain reader engagement. He also highlighted that critical thinking is essential when reviewing thin content sections—rather than accepting LLM output as final, editors should expand anemic sections with details, examples, and context. The team is moving away from word count as a primary metric; the new philosophy is "as long as it needs to be and then slightly shorter," prioritizing user intent and engagement over arbitrary length targets.

### Workflow and Tool Usage

AirOps is currently deployed for InterVest, HomeBase, and Tribe, but team feedback reveals significant limitations: poor linking capabilities, hallucinations (especially problematic for fact-checking), and weak content structuring that produces the bullet-point-sandwich pattern. For Seat, the team abandoned AirOps in favor of ChatGPT because calibrating tone to match Seat's brand voice was too slow and resource-intensive with AirOps; ChatGPT's faster inference and familiar interface make it more practical despite prior AirOps investment. The content grid improvements—specifically the assignment brief field and feedback column—have proven helpful for directing output and capturing editorial notes post-generation. Matthew emphasized that the new sprint model will address these ad-hoc tool choices by building deeply customized workflows and client-specific polishing instructions during the onboarding phase, so that steady-state delivery doesn't require constant tool switching or manual intervention.

### Client-Specific Challenges

**Seat:** The client initially resisted moving beyond short-form, scannable content (<1,000 words) designed for developers and engineers, but the team discovered their average page dwell time is only 35 seconds—indicating that ultra-scannable content may actually be self-defeating. Jess successfully pitched longer-form, more narrative-driven content as a performance lever; the client approved the shift, suggesting openness to content methodology education if tied to outcomes.

**InterVest:** Programmatic content generation for this health-services client requires approximately 1 hour of post-editing per piece due to the need for fact-checking against trusted sources. Matthew identified this as a workflow problem rather than a content quality problem—the current approach (generate, then manually verify facts) is unsustainable and should be replaced with ingested primary sources and a dedicated fact-checking workflow during sprint onboarding.

**Reddit:** The team is experiencing escalating friction on an engagement that's winding down; Jess flagged that they're on manual edit round 5-6 for only 4 pieces within a 4-week timeline, suggesting either scope creep or unrealistic client expectations. Matthew committed to reviewing the contract terms and edit scope.

### Future Improvements

The sprint model will ship with documented, client-specific polishing instructions that codify the patterns Matthew identified—such as "avoid bullet point sandwiches, use 2-5 sentence paragraphs with narrative arc" or "keep keywords early in headlines but avoid colons." All new clients will receive 8-12 weeks of sprint team investment to build workflows, test outputs, and engineer handoff documentation before transitioning to regular delivery pods. The team also needs to design a retcon process for existing clients to backfill improvements discovered during new client onboarding—e.g., applying InterVest's fact-checking workflow to similar health-content clients retroactively. Linking improvements in tools like AirOps are a known gap that should be addressed through workflow design (e.g., prompting for specific linking targets) rather than waiting for platform upgrades.

---

## Action Items

**Fatima Ismail (GrowthX)**
- Review polishing instructions for InterVest, HomeBase, and Tribe. Revise to address: reduce bullet point sandwiches (favor 2-5 sentence narrative paragraphs), improve internal linking quality, enhance fact-checking rigor especially for health-related content.

**Jess Scott (GrowthX)**
- Follow up with Matthew regarding Reddit account issues. Provide breakdown of manual edit rounds (currently in round 5-6 on 4 pieces), actual time spent, and client's stated expectations versus contract scope.

**Matthew Panzarino (GrowthX)**
- Review Reddit account issues escalated by Jess. Assess contract terms, verify whether edit rounds are within scope, and evaluate time allocation against engagement profitability and sustainability.

---

## Transcript

**Jess Scott:** Hey, how's it going? Writers have too many words.

**Matthew Panzarino:** Yeah, imagine that.

**Jess Scott:** Writers being wordy. How many more meetings do you have left?

**Matthew Panzarino:** Today, two. Tomorrow, four or five. And Friday, apparently everybody likes to meet on Friday—seven meetings. My family's at Disneyland, so that'll be fun.

**Jess Scott:** Oh, wow, just salt in the wound.

**Matthew Panzarino:** Yeah, exactly.

**Matthew Panzarino:** I'll be down south in a hotel room and they'll be at Disneyland.

**Matthew Panzarino:** So it is what it is.

**Matthew Panzarino:** Hi, Fatima, how are you doing?

**Fatima Ismail:** Hi, I am good.

**Matthew Panzarino:** Good.

**Matthew Panzarino:** Good.

**Matthew Panzarino:** Okay.

**Matthew Panzarino:** So a quick overview on this exercise before we just talk a little bit.

**Matthew Panzarino:** So this exercise had a couple of purposes.

**Matthew Panzarino:** One, just to give me like a broad overview of the content that we've been producing for clients, the stuff that's actually live, kind of getting a little bit of a taste for what level we've been publishing at, where it kind of falls short in just in terms of, mostly in terms of human readability.

**Matthew Panzarino:** I think the vast majority of it is pretty decent from an SEO perspective.

**Matthew Panzarino:** There's a handful of things here and there, but largely, you know, LLMs and then a lot of our Emmys and directors have SEO experience, but LLMs are also pretty sound at like SEO fundamentals.

**Matthew Panzarino:** That's what they've been trained on largely is web content, which has been trained by Google, so to speak.

**Matthew Panzarino:** So it's a big reciprocal thing.

**Matthew Panzarino:** So the vast majority of my edits and tweaks and kind of pushes and prods and notes were about human readability, which our clients are human.

**Matthew Panzarino:** Theoretically, they are trying.

**Matthew Panzarino:** And to address humans with the content.

**Matthew Panzarino:** So pushing our content to be better in that regard is part of this exercise.

**Matthew Panzarino:** Getting an idea of what the current state of all of that was.

**Matthew Panzarino:** And then reciprocally, you know, talking to CMS about their experience using workflows and how much of it they're doing manually and, you know, all of that stuff to try and get an idea of, okay, cool.

**Matthew Panzarino:** How many of our customers for our platform, a.k.a.

**Matthew Panzarino:** the CMS mostly, are happy with the product or using it at all or what issues do they have?

**Matthew Panzarino:** So it's a little bit of bulk.

**Matthew Panzarino:** And then let me jump in.

**Matthew Panzarino:** I had just grabbed a piece of your content, but, of course, you know, it was content that you had worked on in your previous pod because that's what I had.

**Matthew Panzarino:** I think, let's see here.

**Matthew Panzarino:** Oh, yeah, it was this.

**Matthew Panzarino:** And I'm sorry, I didn't record a loom on this one.

**Matthew Panzarino:** So I'm a little behind on my loom.

**Matthew Panzarino:** I have a handful left, and I got into these meetings, and my days disappeared.

**Matthew Panzarino:** But let me share this here.

**Matthew Panzarino:** So on this here, there are a handful of things.

**Matthew Panzarino:** Most of it was pretty fine.

**Matthew Panzarino:** This is a fairly straightforward article, nothing incredibly complex about this topic.

**Matthew Panzarino:** There was a handful of things that I noticed here, though.

**Matthew Panzarino:** One, this, the original title here was not really semantically correct.

**Matthew Panzarino:** So keep an eye out for that.

**Matthew Panzarino:** LLMs do this weird thing sometimes where they'll generate titles that aren't actually correct from an English language perspective.

**Matthew Panzarino:** And so you have to, like, just make sure you say it out loud in your head before you publish, because Lover's Beach Cabo, seven best things you can do there is not actually semantically correct.

**Matthew Panzarino:** So I just really just rotated this to be semantically accurate.

**Matthew Panzarino:** There is a second.

**Matthew Panzarino:** In this case, this title is probably fine with a colon, but I want to keep an eye out for LLM's tendency to rely on headlines with colons in them.

**Matthew Panzarino:** It really, really, really loves them.

**Matthew Panzarino:** Most LLMs really love them for some reason.

**Matthew Panzarino:** I don't know why.

**Matthew Panzarino:** It's probably some sort of training data set that they've got over-indexed on.

**Matthew Panzarino:** But the vast majority of headlines almost never meet a colon.

**Matthew Panzarino:** It's just not really necessary.

**Fatima Ismail:** I would say it's a fraction of the overall that actually needs it.

**Fatima Ismail:** this case, it's probably fine.

**Fatima Ismail:** I feel like maybe they do it because to keep the keyword right in the start.

**Matthew Panzarino:** Yeah, sometimes they can make for awkward positioning to keyword stuff at the beginning of the sentence.

**Matthew Panzarino:** But usually there are ways to like, because I can rewrite this without a colon of four different ways.

**Matthew Panzarino:** There are ways to keep the early on and yet not rely on a colon, you know?

**Matthew Panzarino:** So just flagging.

**Matthew Panzarino:** That's something to watch out for if you can, and you can tell it, hey, keep the keyword early, just add it in your polishing instructions.

**Matthew Panzarino:** It's totally fine to keep the keyword early, but avoid using a colon.

**Matthew Panzarino:** Thank you, right?

**Fatima Ismail:** Colons and commas are generally bad in headlines, if you can avoid them.

**Matthew Panzarino:** The vast majority of this stuff is just fine.

**Matthew Panzarino:** This section here on the seasons, so this is kind of an easy win, and this is one of those things where, you know, there's a couple of things going on in this section that I think are worth talking about and worth paying attention to and keeping an eye on.

**Matthew Panzarino:** One, single sentence paragraphs are a big LLM crutch when you give it instructions about, that include words like brevity or clarity or conciseness or, you know, make this concise, keep it brief.

**Matthew Panzarino:** It's like, cool, I'm going to give you one sentence, right?

**Matthew Panzarino:** It loves a single sentence or a bullet list.

**Matthew Panzarino:** We know this.

**Matthew Panzarino:** They have a predilection for it.

**Matthew Panzarino:** So keep an eye out for those.

**Matthew Panzarino:** Generally speaking, if you get a block of single sentences, that's an opportunity to go back either into the polishing instructions or the workflow or an LLM box and run it again and say, hey, this information seems sound.

**Matthew Panzarino:** Could you build a narrative out of this for me?

**Matthew Panzarino:** And then, of course, the asterisk here would be if the client is really in love with single sentences or bullet points or whatever.

**Matthew Panzarino:** You know, the client needs to supersede anything I'm saying here or their explicit desires.

**Matthew Panzarino:** But it does not mean you can't push back and say, hey, I know you love bullet points, but I think this is a really good opportunity to expand this a little bit.

**Matthew Panzarino:** So, you know, that's the client is always right until they're not.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** That's the way I look at it.

**Matthew Panzarino:** And we ultimately are not responsible for the thing we're most responsible for is outcomes, not matching what they think is the right thing to do.

**Matthew Panzarino:** It is really up to us to go like, hey, this content.

**Matthew Panzarino:** We'll perform better if X.

**Matthew Panzarino:** And if they're like, oh, that's cool, but we don't like it, great.

**Matthew Panzarino:** You've said your piece and you've tried it best for what they want, you know.

**Matthew Panzarino:** So it's a little bit of a push and pull.

**Matthew Panzarino:** Generally speaking, I think it's important to remember that clients, the vast majority of our clients, depending on the exact stakeholder level, they're not content writers.

**Matthew Panzarino:** They're not writers.

**Matthew Panzarino:** They're not editors.

**Matthew Panzarino:** They don't understand the process of creating content.

**Matthew Panzarino:** don't understand the, like, nuances of it.

**Matthew Panzarino:** They are, in general, going to be most interested in outcomes.

**Matthew Panzarino:** And the opinions they have about content are often wrong or misguided.

**Matthew Panzarino:** And your job is to not then, like, spit on that, but then to find a way to, like, get them to a place where they're, like, you know, understanding, hey, maybe it would be better if we did this.

**Matthew Panzarino:** Maybe it would be better if we did this.

**Jess Scott:** It's a little bit of a narrative, that sort of thing.

**Jess Scott:** I've been telling my team, like, we are in content creation and we are, like, we are in marketing, but, like, it's.

**Jess Scott:** The base of it, we are in customer service.

**Jess Scott:** So we have to walk that line of like, there is a customer here, and we have to pander to that a little bit.

**Matthew Panzarino:** Yeah, I like to think of it as like you're dealing with your team's most ego-driven writer, where you have to come at it and like, you can't make hard edits on them because they have an ego, right?

**Matthew Panzarino:** You have to go like, hey.

**Jess Scott:** If you thought about, what if?

**Matthew Panzarino:** Right, exactly.

**Matthew Panzarino:** And then the second part of it is like on the larger critical thinking piece, so when is the best time to visit Lover's Beach in this section?

**Matthew Panzarino:** And the paragraphs are correct.

**Matthew Panzarino:** Like, I mean, the sentences that you had are correct, like May to June offers warmer crowds, all this stuff.

**Matthew Panzarino:** But the fact is like, weather is probably the biggest deal.

**Matthew Panzarino:** Like that's like the biggest thing that people think about with travel right behind like cost, right?

**Matthew Panzarino:** Like cost is a big deal.

**Matthew Panzarino:** And then right behind.

**Matthew Panzarino:** And that is when should I go is a huge deal because it's like if they're traveling to someplace where they have to fly or drive a very long distance, the first thing they're going to think about is like I want to have a good time when I'm there.

**Matthew Panzarino:** want the weather to be nice, all this stuff.

**Matthew Panzarino:** Now, fortunately for Cabo, it's usually nice.

**Matthew Panzarino:** It's not really like, OK, it's not that big of a deal.

**Matthew Panzarino:** But I just wanted to note this as like a critical thinking piece where you're like, hey, most of these other sections are pretty well fleshed out.

**Matthew Panzarino:** Like you've got tours, you've got links, obviously, the client wants.

**Matthew Panzarino:** You've got some detail about like why would you take this tour and what you might be able to see on the tour.

**Matthew Panzarino:** Pretty well fleshed out.

**Matthew Panzarino:** But this section was pretty anemic.

**Matthew Panzarino:** And then it's like, hey, this is a good opportunity to really ask an LLM.

**Matthew Panzarino:** No, give me some details about the weather.

**Matthew Panzarino:** Give me temperatures.

**Matthew Panzarino:** Give me times.

**Matthew Panzarino:** Give me seasons.

**Matthew Panzarino:** And honestly, the prompting is not that hard in this one.

**Matthew Panzarino:** It's like, hey, expand this out with more detail and you'll generally get something closer to this.

**Matthew Panzarino:** So keep an eye out for that where you're like, oh, this is thin.

**Matthew Panzarino:** You're like, is this real?

**Matthew Panzarino:** And if it's not, maybe just delete it if it's really thin.

**Matthew Panzarino:** But if it is germane, take an opportunity to expand it, you know?

**Jess Scott:** So that's just something to keep in mind.

**Jess Scott:** And too, Fatima, to kind of tie that into, like, our current clients, like, that's kind of what I was saying, too, about, like, Seat specifically, of, like, being able to, like, really leverage, like, Panzar, I was just telling Fatima before you joined, like, she's been here so long that, like, I can see the residual effects of, like, I got to get 50 pieces of content out, and I'll have to meet this word count.

**Jess Scott:** And we're kind of restructuring and being able to, like, really leverage our content managers for their expertise.

**Jess Scott:** And so being able to, like, yeah, look at a section like that and have the time to think through, like, how do we make this better?

**Jess Scott:** And is this serving user intent?

**Jess Scott:** And really lean into, like, some creative freedom to be able to build better pages.

**Matthew Panzarino:** Yeah, word count is, like, a bad motivator in almost any case, you know?

**Matthew Panzarino:** I just don't think it was a good way to get our content and we're moving away from it.

**Matthew Panzarino:** But, you know, like, I always told my writers when they were talking to me about length,

**Matthew Panzarino:** We had discussions about length.

**Matthew Panzarino:** My tagline is as long as it needs to be and then probably slightly shorter.

**Matthew Panzarino:** know, like that's really the length any content needs to be.

**Matthew Panzarino:** Like, okay, have you said what you need to say?

**Matthew Panzarino:** No, add a little more.

**Matthew Panzarino:** Have you said what you need to say?

**Matthew Panzarino:** Cool, stop.

**Matthew Panzarino:** You know, and I think that's, it's bad.

**Matthew Panzarino:** It's a bad motivator to say, like, add a bunch of .

**Matthew Panzarino:** Pardon my friend.

**Matthew Panzarino:** But add a bunch of unnecessary stuff just to meet a word account.

**Jess Scott:** It's crazy.

**Jess Scott:** This is just good life advice, too.

**Jess Scott:** Yeah, exactly.

**Matthew Panzarino:** I'm talking.

**Matthew Panzarino:** Unfortunately, if you ask my wife, it's like, I am unable to take my own advice.


**Matthew Panzarino:** And the rest of this, like, there was just some more stuff that was really along the same lines.

**Matthew Panzarino:** Like, the section about what to know before visiting Lover's Beach.

**Matthew Panzarino:** The single sentence, bullets, single sentence structures.

**Matthew Panzarino:** This is very common with LLMs.

**Matthew Panzarino:** Keep an eye out for it.

**Matthew Panzarino:** It's not like it always needs to go away.

**Matthew Panzarino:** Sometimes that's what matters.

**Matthew Panzarino:** It's like, if you're wondering.

**Matthew Panzarino:** to mean?

**Matthew Panzarino:** What we do for you.

**Matthew Panzarino:** Here's the four bullets.

**Matthew Panzarino:** know, okay, cool.

**Matthew Panzarino:** If it works, it works.

**Matthew Panzarino:** I'm not saying never, ever do it.

**Matthew Panzarino:** However, it can make content look very skeletal and very generated to have that structure.

**Jess Scott:** You've been calling it the bullet point sandwich because it's literally one line, then bullet points, then another line, then the next section.

**Jess Scott:** And it's like, it's very like, yeah, it's, I just flagged it a couple of times on a different piece because it's like, and then you get three of them stacked.

**Jess Scott:** It's like, this is too much.

**Matthew Panzarino:** The cool thing about it is it's straightforward to write into polishing instructions.

**Matthew Panzarino:** Keep an eye out for this.

**Matthew Panzarino:** You can literally tell it, hey, I know what you're about to do.

**Matthew Panzarino:** I know you're about to do these sandwiches, bullet point sandwiches.

**Matthew Panzarino:** Please don't do that.

**Matthew Panzarino:** Like instead, give me a paragraph.

**Matthew Panzarino:** You can be hyper explicit.

**Matthew Panzarino:** Give me paragraphs that are two to five sentences in length.

**Matthew Panzarino:** You can use single sentence paragraphs, but only sparingly and only to end.

**Matthew Panzarino:** Emphasize the core point of the section.

**Matthew Panzarino:** This is the way humans write.

**Matthew Panzarino:** Like, in a good narrative, it's like a setup, maybe a little bit of context, and then, bam, the point.

**Matthew Panzarino:** And then a little bit of, like, you know what I'm saying?

**Matthew Panzarino:** Outro, example, seed it in, you know, real world or whatever.

**Matthew Panzarino:** That's what a narrative feels like.

**Matthew Panzarino:** And it's okay to isolate important points as sentences or, in this case, bullet points or whatever, but not to do it too much.

**Matthew Panzarino:** There was a lot of content, not this piece, but there was a lot of content that I reviewed that was essentially all bullet point sandwiches, top to bottom.

**Matthew Panzarino:** know, like two sentences intro, and then two sentences outro.

**Matthew Panzarino:** That's incredibly lazy.

**Matthew Panzarino:** And if a client notices, we're in trouble.

**Matthew Panzarino:** Like, there's stuff that's live now where I'm like, Jesus, you know.

**Matthew Panzarino:** Like, so it's, we are fortunate that only a machine has been looking at that, you know, or at least a very low expectation, you know, stakeholder.

**Matthew Panzarino:** On the client side, there's just some of that stuff we need to be careful for.

**Matthew Panzarino:** It's not that it can never work or it's never good.

**Matthew Panzarino:** And sometimes it can be good to think of things.

**Matthew Panzarino:** I know this is going to sound weird, but it can be good to think of pieces as geometry.

**Matthew Panzarino:** And they should be made up of a variety of shapes so that you don't end up with.

**Matthew Panzarino:** Also, you don't end up with a lot of like really chunky sections over and over either.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** Because they could be exhausting to a reader.

**Matthew Panzarino:** It's like they almost need relief.

**Matthew Panzarino:** It's like you go on a run and then you do a walk and then you run again.

**Matthew Panzarino:** You know, do a sprint and then you walk.

**Matthew Panzarino:** You vary your pace.

**Matthew Panzarino:** You know, you have a little drink and then a appetizer and then a meal.

**Matthew Panzarino:** And then it's like a little dessert, a little dinner drink.

**Matthew Panzarino:** Right.

**Matthew Panzarino:** You need that kind of like leavening.

**Matthew Panzarino:** So rectangles, vertical rectangles, ovals, you know, different shapes.

**Matthew Panzarino:** Now, part of this is stuff like interstitial imagery and, you know, lists and then paragraphs.

**Matthew Panzarino:** And then.

**Matthew Panzarino:** then...

**Matthew Panzarino:** Narrative and then, you know, headers, this just breaks it up because walls of text is also not a great way to like live life.

**Matthew Panzarino:** You know, you're, you're, it's also not very human readable to be presented that way.

**Matthew Panzarino:** Only academics love reading walls of text.

**Jess Scott:** This is something we just flagged for Seat. Matthew, that's the account you reviewed.

**Jess Scott:** And it's very much those bullet point sandwiches.

**Jess Scott:** And we actually just talked about it today on the client call because the client was like, yeah, like we've been doing this long form content.

**Jess Scott:** I was like, need to stop you.

**Jess Scott:** We've not been doing long form.

**Jess Scott:** We've been doing the short form, less than a thousand words, scannable for your dev and engineer folks.

**Jess Scott:** was like, we need to be moving into longer form content that like people can actually digest because, and Fathom, this is just good for you to know because it's your account.

**Jess Scott:** Like their average spend time on their site is like 35 seconds.

**Jess Scott:** And so having this content that's so scannable, it's actually like shooting them in the foot.

**Jess Scott:** So we finally got the like green light to do long form content from the client because we've been having this.

**Jess Scott:** It was pushback.

**Jess Scott:** so, like, that's what you just said about, like, the same, like, stacking those and not having that depth.

**Fatima Ismail:** Like, it is really something we have to be thinking about a lot more critically.

**Matthew Panzarino:** Yeah.

**Jess Scott:** Yeah.

**Matthew Panzarino:** Cool.

**Jess Scott:** Yeah, it doesn't have that making effect.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** I don't need to believe in the point more on the content.

**Matthew Panzarino:** I think you can kind of see where I was poking and prodding there.

**Matthew Panzarino:** I'm not saying the content is bad or evil.

**Matthew Panzarino:** It's just things we need to think about and be cognizant of.

**Matthew Panzarino:** So there are certain patterns there that can just become, like, standardized parts of our polishing instructions.

**Matthew Panzarino:** The polishing instructions really should be incredibly hyper-customized per client.

**Matthew Panzarino:** And that's something we have to work on.

**Matthew Panzarino:** But it's also something that as we move into the sprint model, it will come out of that phase more fully formed.

**Matthew Panzarino:** You know, so we've all just been sort of, like, trying to do whatever with whatever client.

**Matthew Panzarino:** By we, I mean you.

**Matthew Panzarino:** I just joined too.

**Matthew Panzarino:** But, like, you know, mostly you've been trying.

**Matthew Panzarino:** Just service the client with whatever tools you have available, and we should be coming out of these sprint phases with a more focused and detailed set of polishing instructions, likely customized, if not completely custom, but mostly customized workflows for those clients, and already delivering to spec so that it is more steady state.

**Matthew Panzarino:** And of course, if we do upsells or change their SOP or the add-on services, we'll need to make adjustments, but engineers will have been involved, designers, prompt engineers, people just trying to make sure that everything is set up properly to deliver what that client is happy with, and then the client's like, awesome, you're like, great, so happy to have spent this 12 weeks with you, now it's time for you to transition to one of our pods, right?

**Matthew Panzarino:** And then we'll take over, and then obviously we have to design that transition process of like, okay, cool, how do we hand off, like, we'll do meetings, but we also need documentation, right, on how.

**Matthew Panzarino:** How these things work that you've built and where the resources are and all of that.

**Matthew Panzarino:** So it will be different.

**Matthew Panzarino:** Like all new clients will feel different going forward from about eight to nine weeks from now on.

**Matthew Panzarino:** All of this will feel a bit different, which is a good thing because it will be calmer, you know, I think, overall.

**Matthew Panzarino:** And then from your side, Fatima, happy to hear the reciprocity.

**Matthew Panzarino:** Like talk to me a little bit about how you're using the workflows, what percentage of your work is going through there, how much you're adjusting afterwards.

**Matthew Panzarino:** If you're not using them at all, I won't, you know, I won't be angry.

**Fatima Ismail:** I just want to know, you know.

**Fatima Ismail:** Yeah, no, we've been using, actually, I've been doing most of the work in aerobs.

**Fatima Ismail:** But there are some clients right now that we have to, like, skip aerobs and go for chat GPD.

**Fatima Ismail:** But like, aerobs does a good job in researching, but not really.

**Fatima Ismail:** Structuring the content well, so there's a lot that needs to be done there, and then the linking, it's terrible.

**Fatima Ismail:** It's absolutely terrible, and you'll have to, like...

**Fatima Ismail:** hearing that, for sure.

**Matthew Panzarino:** Yeah.

**Fatima Ismail:** Yeah.

**Fatima Ismail:** And fact-checking—it hallucinates a lot. It's not reliable.

**Matthew Panzarino:** Like "Summer in Cabo is 22 degrees," you know?

**Fatima Ismail:** Yeah.

**Fatima Ismail:** Yeah, so those kind of things, that is what makes us, like, rethink about using Aerobs for all the clients, yeah.

**Fatima Ismail:** So we have to do a lot of manual research.

**Fatima Ismail:** So, you know, between all of this, it feels like using Aerobs is completely useless, because it's not really doing much for us, because we have to fact-check, and then we have to go over the links, and we have to restructure it a lot.

**Fatima Ismail:** So, yeah.

**Fatima Ismail:** But the feedback column has really helped. We can add feedback after the final draft to make the article better.

**Matthew Panzarino:** So, yeah.

**Matthew Panzarino:** Yeah, adding that to the grid, you mean?

**Jess Scott:** Have you leveraged, Fathom, have you leveraged much of the, like, assignment brief?

**Jess Scott:** Yeah, yeah.

**Fatima Ismail:** Yeah, assignment brief has helped a lot, too, because we can just add the outline that we, how we want the output to look like, and then it would pretty much follow it.

**Fatima Ismail:** But, um, even after that, um, the issue that you were pointing out about, like, it adds a lot of bullet points, random, like, one heading would have a lot of bullet points, and the other won't, and it just looks pretty off.

**Fatima Ismail:** So, yeah, it helps, but it still needs a lot of work.

**Fatima Ismail:** Okay, cool.

**Matthew Panzarino:** So what, what, um, uh, are you using them on, is it called seat or sit?

**Matthew Panzarino:** Seat, right?

**Jess Scott:** is, yeah, it is pronounced seat.

**Matthew Panzarino:** Are you running them on seat as an example?

**Fatima Ismail:** No?

**Jess Scott:** Um, I mean, well, Fatima, you correct me if I'm wrong.

**Fatima Ismail:** It's all GPT, right?

**Fatima Ismail:** Yeah, yeah, it's GPT.

**Matthew Panzarino:** Okay, so you're not, you're not using the assignment creation or article.

**Fatima Ismail:** We're using it for InterVest.

**Jess Scott:** InterVest, okay.

**Jess Scott:** It's only using HomeBase and InterVest for pair of things.

**Matthew Panzarino:** Okay.

**Fatima Ismail:** And Tribe.

**Fatima Ismail:** And Tribe, yeah.

**Matthew Panzarino:** Okay, and Tribe.

**Matthew Panzarino:** Yeah, I'm just looking at the, the workflows here that you're running on, um, on InterVest.

**Jess Scott:** So, and that's been really tough too, because this is programmatic.

**Jess Scott:** And so not to like, not to dive into the whole InterVest issue, but like.

**Jess Scott:** We're supposed to have 25 of those pages done end of each week, and Aerofs is not really.

**Jess Scott:** Fatima, how long are you spending to generate and edit, finalize one programmatic blog for Interwell?

**Fatima Ismail:** Yeah, again, that whole issue with fact checking and everything for Interwell, it's a lot because the template that we have right now, it needs to have correct information.

**Fatima Ismail:** So, the generation really doesn't take that long, but the post-editing is a lot.

**Fatima Ismail:** Yeah.

**Fatima Ismail:** Yeah, I mean, I think Interwell, like an hour spent, do you have like a rough timeline on how long one would take?

**Fatima Ismail:** I think it was taking a whole hour to edit it.

**Jess Scott:** Just for it.

**Fatima Ismail:** Okay.

**Matthew Panzarino:** Yeah, mean, Interwell seems like a prime candidate for an additional fact checking workflow.

**Matthew Panzarino:** It's built specifically, you know, like, because they deal obviously in, you know, drug therapies.

**Matthew Panzarino:** So in another, you know, health related topics.

**Matthew Panzarino:** So like having, or non-drug therapies, hopefully as well.

**Matthew Panzarino:** But I think it's a prime candidate for like, okay, here are four major academic sources on these topics.

**Matthew Panzarino:** Let's fact check this article against those and flag anything that seems like it doesn't match reality, right?

**Matthew Panzarino:** Those sources, you know, I'm speaking in like, okay, what if we were to sprint with Interwealth?

**Matthew Panzarino:** Like what if the sprint team was to have done this, gotten this client set up?

**Matthew Panzarino:** It's very likely during the kickoff that we probably asked them this, but then maybe did nothing with it afterwards.

**Matthew Panzarino:** But we may have asked them like, okay, what are, what are primary sources of truth that you use?

**Matthew Panzarino:** You know, what can you provide us with some?

**Matthew Panzarino:** Great sources of accurate information on these topics that you use or that you are fine with us using to fact-check any articles we produce for you.

**Matthew Panzarino:** Ingest those or reference those in a fact-checking workflow specifically for this client.

**Matthew Panzarino:** Of course, build the templates, build the dashboards, you know, engineer the solutions so that we're ready to deliver.

**Matthew Panzarino:** And then get the workflows in a steady state where they're generating things that are fact-checked enough to be understandable and to be like, hey, this is probably in the 90th percentile.

**Matthew Panzarino:** And I'm going to do my human-readable work on it to get it, you know, to brush up things like tone or shape or whatever.

**Matthew Panzarino:** That's, you know, that's something we probably need to then retcon in to existing clients because this is the way that new clients will be built.

**Matthew Panzarino:** But then we'll need to, like, you know, brush up on existing clients.

**Matthew Panzarino:** I don't know what that process looks like, but it's clear that we're going to need to do it.

**Matthew Panzarino:** And on the link side of it, that's something.

**Matthew Panzarino:** I've been hearing from everybody, so the blinking needs to be better.

**Matthew Panzarino:** So AirOps isn't being used on Seat at all?

**Jess Scott:** The tone hasn't, we weren't able to strike the right tone with AirOps.

**Jess Scott:** And so, to be honest, just fully transparent, we couldn't get the right tone at a speed that was like making the client happy, like it was taking too long to try and calibrate AirOps.

**Jess Scott:** And so, it was just faster for us to use ChatGPT, and now we can do it really fast.

**Jess Scott:** And so, it's kind of like, at this point, like, leveraging ChatGPT for the accounts we use it for, we are just really fast with it, and it's a lot easier.

**Jess Scott:** And like, especially where like Seat doesn't have a lot of external linking.

**Jess Scott:** So, it's just a matter of, once you know the client really well, like I built a channel for Seat that we can go in, and prompt, and it just builds the page.

**Jess Scott:** And like my team has the prompts they need and then they go and they build it.

**Jess Scott:** And then once you know the client, you just know where to drop your links and you know how their website is.

**Jess Scott:** So it's kind of like that's the reason like we've spent some time trying to get C pushed over to AROPS, but it's just never been like it's never been an easy enough like we've never gotten it calibrated fast enough that we're like, OK, cool.

**Matthew Panzarino:** Push everything over there.

**Matthew Panzarino:** So that's kind of logic.

**Matthew Panzarino:** Got it.

**Matthew Panzarino:** Yeah, thanks.

**Matthew Panzarino:** And then let's see, what other clients?

**Matthew Panzarino:** Those are your two major ones.

**Jess Scott:** Any other ones?

**Jess Scott:** I mean, no.

**Jess Scott:** So right now we have C, Interwell, Homebase are the three that are staying.

**Jess Scott:** We're wrapping up Tribe and Reddit.

**Jess Scott:** I also like not to hijack this call.

**Jess Scott:** We're having a big issue with Reddit and I put it in the external Reddit.

**Jess Scott:** I can flag it to you directly if you want, but like we are on like round five or six of manual edits.

**Jess Scott:** And I just feel like they're taking advantage of the contract at this point because like we're like we owed them 25 pieces of.

**Jess Scott:** Content at the end of their engagement when they canceled and didn't renew.

**Jess Scott:** And four weeks later, we are still on the first four pieces of content because they are doing round after round of edits and bringing people in and it's all manual.

**Jess Scott:** And it's just taking a lot of time.

**Jess Scott:** But that's my account.

**Jess Scott:** Okay, got it.

**Matthew Panzarino:** Yeah.

**Matthew Panzarino:** Thanks for flagging.

**Matthew Panzarino:** I'll take a look at what's going on there.

**Jess Scott:** Yeah.

**Jess Scott:** But the other thing, too, as far as Fatima's content, I just want to say it's been great having her on the team.

**Matthew Panzarino:** I dropped you a note about it this morning.

**Jess Scott:** The edits, she's taking feedback, she's making the edits, and she's just been so willing and so invaluable.

**Jess Scott:** It's been genuinely a pleasure to have her on the team, and she's made everyone's life so much easier and better.

**Jess Scott:** So she's helped our content, she's helped our clients, she's helped our team.

**Jess Scott:** So, yeah, very, very thrilled with this edition.

**Matthew Panzarino:** Cool.

**Matthew Panzarino:** Sounds great.

**Matthew Panzarino:** All right.

**Matthew Panzarino:** Thanks for the chat.

**Matthew Panzarino:** appreciate it.

**Matthew Panzarino:** have to jump to my next.

**Matthew Panzarino:** But it sounds good.

**Matthew Panzarino:** And then, yeah, I've got the...

**Matthew Panzarino:** But I've got the notes about what we need to be focused on, so I appreciate it.

**Jess Scott:** Ciao.

**Jess Scott:** Thanks.

**Jess Scott:** Bye.

**Fatima Ismail:** Bye.
