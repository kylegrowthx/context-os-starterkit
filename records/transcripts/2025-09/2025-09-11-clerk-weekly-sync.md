# Clerk Weekly Sync

<metadata>
date: 2025-09-11
time: 16:01 UTC
duration: 35 minutes
organizer: andi@growthx.ai
participants: Andi Bailey (GrowthX), Alex Rapp (Clerk), Brian Morrison II (Clerk)
fathom_recording_id: 86632098
fathom_url: https://fathom.video/calls/406203675
share_url: https://fathom.video/share/M94NKNYBUC1P2Y8-PfP1sbikLtAhnC6t
source: fathom
enriched_on: 2026-03-03 02:15 UTC
</metadata>

---

## Summary

GrowthX presented three versions of authentication content (original, human rewrite, and agentic rewrite) showing measurable progress from its AI-powered workflow, with full prompt transparency to address Clerk's skepticism. The team will conduct a technical deep dive with Jeff (Clerk's engineering authority) to finalize preferences on cryptographic recommendations (Bcrypt vs Argon2) and password policy standards (NIST compliance), after which these guidelines will be embedded into the generation system to ensure accuracy at scale. Clerk's Iceland offsite next week will slow feedback cycles, but both sides committed to async calibration and a plan to generate 5-6 additional articles testing "auth" vs "authentication" terminology for LLM discoverability.

---

## Context

GrowthX is delivering content marketing services for Clerk, an authentication platform. This is an ongoing weekly sync between Andi Bailey (GrowthX CTO) and Alex Rapp and Brian Morrison II (Clerk's content leadership). The team is working through content calibration for authentication and security topics — establishing what Clerk considers best practices and ensuring GrowthX's agentic content generation workflow aligns with Clerk's technical standards. The Clerk team is heading to an offsite in Iceland next week, which is expected to slow down review cycles. A deeper technical discussion with Jeff (Clerk's technical authority) is scheduled to resolve remaining preferences around authentication terminology, password policies, and cryptographic recommendations.

---

## Relevance

**To GrowthX Delivery:**
- Agentic workflow is showing measurable progress — three versions of authentication vulnerability content (original, rewrite, agentic rewrite) demonstrate clear calibration trajectory
- GrowthX successfully implemented a prompt-based system that constrains AI generation to Clerk's documentation and eliminates competitor scraping, addressing trust concerns
- Next iteration depends on technical deep dive with Jeff to lock down specific preferences (Bcrypt vs Argon2, NIST password policy stance) — these will be baked into generation rules
- Content structure guidelines are shifting toward LLM discoverability (TLDRs, chunkability, FAQ placement) rather than traditional article structure; Alex requesting detailed playbook for this approach

**To GrowthX Business Development:**
- Clerk is skeptical but willing to run head-to-head tests (Colin challenged Jeff to competitive evaluation vs. Clerk's own prompt-based approach) — strong signal they're taking the partnership seriously
- Client is planning to scale to 5-6 articles next week pending technical alignment, indicating expansion potential if quality bar is met
- Ada (GrowthX strategist) is on vacation this week but returning next week — continuity depends on her re-engagement in calibration cycles
- Clerk's Iceland offsite next week (Sept 18-20) will slow feedback velocity, but Alex and Brian committed to async calibration and noted they're working with limited review bandwidth

**To CheckThat:**
- Authentication terminology (auth vs authentication) conversation directly relevant to LLM search optimization — team noted LLMs pull from social/conversational sources (Reddit) favoring shorter terms, diverging from traditional SEO
- Clerk is investing in AI-driven content generation and sees it as core to their strategy going forward

---

## Overview

- GrowthX's agentic workflow is demonstrating measurable progress through three-version comparison (original, rewrite, agentic rewrite) of "Top Authentication Vulnerabilities" article
- The agentic system uses constrained prompts (limited to Clerk's own documentation) with human-in-the-loop review at every stage, building trust with skeptical stakeholders
- Jeff (Clerk's technical authority) is running competitive head-to-head testing against his own prompt-based approach; CEO Colin challenged him to evaluate fairly rather than dismiss the partnership
- Unresolved technical preferences (Bcrypt vs Argon2, NIST password policy stance) will be clarified in a technical deep dive and then baked into the generation system as validation rules
- Team plans to test "auth" vs "authentication" terminology across articles to optimize for LLM search discoverability alongside Google SEO
- Clerk team heading to Iceland offsite next week; Alex and Brian will determine post-offsite availability for deep dive and next Thursday's meeting

---

## Key Topics

### Clerk Team Offsite

  - Team heading to Iceland for an offsite next week
  - Activities planned: Northern Lights tour, Blue Lagoon visit, food tours
  - Potential impact on content review and progress

### Content Generation Progress and Agentic Workflow

  - GrowthX has implemented a full agentic pipeline with human-in-the-loop at every stage
  - Three versions of "Top Authentication Vulnerabilities" available for side-by-side comparison: original, human rewrite by Andi and Yusuf (GrowthX technical expert), and agentic rewrite
  - The agentic system constrains AI to Clerk's own documentation (scraping Clerk's support docs, not the broader internet) to eliminate competitor scraping and ensure accuracy
  - System includes a "proofreader checklist" that validates output against Clerk-specific rules: terminology preferences (sign in/sign up, not log in), no em dashes, hyperlink principles, and exact component capitalization
  - Focus is on accuracy and technical alignment before any design elements; Andi explicitly advised against introducing design/images until content is locked down

### Authentication Terminology

  - Discussion on using "auth" vs "authentication" in content
  - Google Trends shows higher search volume for "authentication" but "auth" not far behind
  - Consideration of LLM searches potentially favoring conversational terms like "auth"
  - Proposal to test both terms in content to determine best approach

### Addressing Skepticism with Competitive Testing

  - Alex warned Andi that Jeff is extremely skeptical of the entire AI-powered approach and has been creating his own competing content
  - Colin (Clerk CEO) challenged Jeff to run head-to-head tests rather than dismissing the partnership outright — positioned as both sides proving their approach works
  - Alex frames this positively: even if both approaches produce different content for the same topic, it's coverage expansion, not redundancy
  - This competitive dynamic is actually an opportunity to build trust; if GrowthX's agentic approach proves comparable or better, it shifts the narrative

### Technical Preferences and Best Practices

  - Unresolved technical preferences needed on specific recommendations: Bcrypt vs Argon2, NIST password policy stance (special character requirements), other cryptographic details
  - These preferences will be documented in writing and baked into the agentic workflow as validation rules so they're enforced automatically in future generations
  - Alex wants detailed playbook on how GrowthX structures content to be prepared for pushback from Clerk's internal teams

### Content Structure and Best Practices

  - Alex requested GrowthX's best practices for content structuring and post-processing (Markdown to HTML conversion)
  - GrowthX is emphasizing elements like TLDRs, FAQs, and inline Q&A, but optimized for LLM discovery rather than traditional article structure
  - Focus on "chunkability" — content segments that LLMs can extract and use, particularly important since LLMs pull from social/conversational sources (Reddit) not just traditional web search
  - Ongoing A/B testing to evaluate what gets picked up by LLM indexes and search engines; results will inform future structural recommendations

---

## Action Items

**Alex Rapp (Clerk)**
- Review 3 versions of "Top Authentication Vulnerabilities" article in blog folder (original, rewrite, agentic rewrite)
- Check Iceland offsite schedule and determine availability for next Thursday's meeting with Andi

**Brian Morrison II (Clerk)**
- Review 3 versions of "Top Authentication Vulnerabilities" article in blog folder (original, rewrite, agentic rewrite)

**Andi Bailey (GrowthX)**
- Ask Jeff (Clerk's technical authority) about Clerk's stance on NIST recommendation for eliminating special character/number requirements in passwords during technical deep dive
- Share GrowthX's best practices for content structure and post-processing with Alex, including guidance on FAQs, TLDRs, and Markdown-to-HTML conversion for LLM discoverability

---

## Transcript
**Brian Morrison II:** Good. Honestly, pretty busy. We're going to be out. The entire team is going to an offsite next week. So it's just been a lot of prep work to get things ready for that.

**Andi Bailey:** Yeah. Are you guys going to do any activities? Iceland sounds amazing.

**Brian Morrison II:** Yeah, we've got a Northern Lights tour is one of the things. And then we also have a visit to Blue Lagoon, which is a natural hot springs. Besides that, a lot of food tours and tasting the flavors of Iceland.

**Andi Bailey:** Are you an adventurous eater?

**Brian Morrison II:** Perhaps. I may try it. I may try whatever they have available, but it depends on how I'm feeling in the moment.

**Andi Bailey:** I imagine it's a lot of salted fish and stuff. Hey, Alex.

**Alex Rapp:** I'm assuming you guys are talking about Iceland. I was looking at some restaurants to try to get bookings ahead of time. It's quite an eclectic mix of food over there. I actually stumbled upon a Twitter post, a meme about frozen grocery goods in Iceland that mimics food looking appetizing to an American. It did not look appetizing whatsoever.

**Andi Bailey:** What's in a Lunchables in Iceland? Sardines?

**Alex Rapp:** I have no idea. Viking food?

**Andi Bailey:** Well, you can find an Irish pub anywhere.

**Alex Rapp:** So worst comes to worst, you can always go to an Irish pub. I'll keep this short because we need to jump into the work, but I moved into a newer development a couple years ago where they're all about convenience. There's no restaurants or grocery stores nearby, so you have to drive 10 minutes to get anything. There are two girls with a pickup truck and an Airstream trailer they converted into a mobile salon. They cut every guy's hair in the neighborhood, including mine. One of them had been to Iceland with her husband and said Icelandic people are the hardest partiers she's ever come across. After work hours they just go out and party. It's not uncommon to see people passed out on sidewalks and in alleyways.

**Andi Bailey:** I didn't figure that to be the case.

**Alex Rapp:** I figured they might be more reserved and prideful of their isolated community.

**Brian Morrison II:** It'll be an interesting cultural experience in general.

**Andi Bailey:** You guys are going to have to have a work conversation before you go.

**Alex Rapp:** I don't think so. There's not really anybody on the team looking to party hard at night. It's just more casual unwinding. We definitely had experiences like that at other offsites, but not so much for our company. We had a guest attendee at one of our offsites who got a little too loose.

**Andi Bailey:** I joined Uber in 2017, so I missed the Beyonce concert Vegas extravaganza by a couple of months. But the stories that reverberated through time were quite shocking. Okay, well, I can jump in. Today I want to talk about our agentic pipeline. Daniel, our engineering co-founder and CTO, has been experimenting with more agentic workflows. We set it up for you guys over the first half of this week and have been testing it out. I put three comparison articles from "Top Authentication Vulnerabilities" — the original, a rewrite, and an agentic rewrite. For you guys, it will be useful to see the progress we're making with the calibration feedback. In the blogs folder now there should be articles including "8 SSO Best Practices." This is the agentic rewrite for that calibration. I didn't want to share it ahead of time because there are still comments from our technical authority — our IT security person — who identified a couple of places where the agentic workflow was differing from Clerk's best practices. For example, we reference Argon2 versus Bcrypt. We know you guys are advocating for Bcrypt over Argon2. Those are the sort of nuances I want to get into with Jeff this afternoon. That's scheduled for this afternoon, and Daniel's very confident that once we have that kind of nuance, we'll be in a really good place. This is quite close to being ready to go. But there are positioning pieces we want to make sure we're not missing before you share it with the rest of the team.

**Alex Rapp:** Okay, that all sounds good. Let me think about how I want to say this. As a precaution for your conversation with Jeff — he is, I can't understate it, a thousand percent skeptical of this entire process. So much so that he's taken it upon himself to create his own prompt to write content. And we decided we're going to run head-to-head tests. I had a conversation with him and Colin, our CEO. Colin got fed up with Jeff dismissing everything and not focusing on what we can do from a solution-oriented standpoint. So he challenged Jeff to a head-to-head test, which I think is great because it's going to produce the best outcome on all sides. And to be honest, if we have content that's even slightly different for the same topic, I just see that as covering more ground, not redundancy. I want you to have that context heading into your conversation with him. I want to prepare you and think of ways to build trust with him. I didn't want you to walk in and step on a landmine right out of the gate.

**Andi Bailey:** Yeah, I appreciate that. I think you alluded to that, and I kind of assumed he was working on generating his own stuff. I'll be curious about how his approach goes. I also want to show you guys, and I'm happy to show him as well, our agentic workflow.

**Alex Rapp:** Had Ada walked you through Atlas yet?

**Andi Bailey:** No. Okay, so I'll show you everything we're leveraging and how the deep dive will come into play. We have a Clerk implementation cheat sheet where we scraped all your support documentation. Daniel generated common code recommendations. He's inserted code and we want to make sure everything is accurate. It will only reference this if we're recommending code pieces.

**Alex Rapp:** That's really good, because I know Jeff's going to ask what your prompts look like for these workflows.

**Andi Bailey:** Yeah. We limit the reference points to Clerk's website so the AI isn't looking at the whole internet or scraping competitor sites where we'd get conflicting data. So this is clerk.com products and features pulled from the site. We can then create a fuller, more comprehensive article. These are the audience personas Aida generated, company context, writing guidelines — tone, principles, language guidelines. And we have a proofreader checklist with writing guideline validation: no em dashes, hyperlink principles, terminology and language positioning — you sign in and sign up, never log in. Exact capitalization of components. Never shorten authentication to auth. These are all things baked into generation. Once we hone in on all preferences during calibration, they get put into the system. So when the AI edits, it checks: did we do all of these things? Then we do another round of human edits. This allows us to scale. And this is the quick start guide, and a template overlay when we generate the article so we can space for the header image. This is what we've generated. We've run agentic tests. We start with the research topic, and at every stage there's human-in-the-loop — you can see the output, highlight something, and our AI assistant can help make edits. We pulled from Airtable, the content OS we share with you — short description, title, keywords — then it does deep research. You can see the inputs: variable parameters like Clerk, persona, target length, research source quality standards. This is just the first step. You can see the persona of the technical founder, authentication methods and securities — all pulling from artifacts.

**Alex Rapp:** Quick question — how much adjusting did the team do from what you're showing me now versus where we were initially when signing off on artifacts?

**Andi Bailey:** We usually do another round of edits after deep dives. When Ada got the overview, she probably edited the artifacts again. Aside from the writing guidelines piece, probably not much on personas and company context — mostly on writing guidelines and preferences. Whenever we get more information on product details, we'll update it, probably on a monthly basis.

**Alex Rapp:** Okay, got it. That's helpful. Brian, how do you feel about "auth" versus "authentication"? I know our standard is to spell out authentication, but auth is probably around the same search volume, maybe a quarter less.

**Brian Morrison II:** What are your thoughts? Does Google treat them differently? Does ChatGPT? Because in SEO, two similar terms can be construed as the same thing.

**Alex Rapp:** I don't know if answer engines do the same. It's essentially phrase match versus exact match logic. Andi, do you have any POV on that?

**Andi Bailey:** I'd be curious what your decision-making was — why you chose authentication.

**Alex Rapp:** Just for a more polished, professional appearance. The term "auth" is more conversational speech, what you see on social. When it comes from a company, you generally see it spelled out. But on Twitter I see a mixed bag of both. Looking at Google Trends, authentication clearly has higher search volume, but auth isn't too far behind.

**Brian Morrison II:** I think we should test this and sprinkle in some instances where both appear. For example, I just wrote an article targeting "Next.js authentication" as the primary keyword. If we sprinkled in "Next.js auth" as well to see how it performs, that could help us determine which is better or if a hybrid approach nets us the most traffic.

**Alex Rapp:** As long as we can rally behind it as a team and defend the decision, I'm okay with sprinkling it in.

**Andi Bailey:** The interesting thing about "auth" is that LLMs pull from social conversation — Reddit pulls a lot of stuff. If you're searching on an LLM, it pulls social conversations. So we'll probably start seeing a shift in how language is influenced by conversation and vice versa. It's already moving along the same lines as authentication. With people searching in their own parlance using natural language, you'll probably see a lot more "auth" anyway. It might be a good way to show up more in LLM searches versus Google.

**Brian Morrison II:** Are those the same? Does the LLM treat auth and authentication as the same — vector embedding?

**Andi Bailey:** I think embedding might be the right term. I don't have an answer for that. I can ask.

**Alex Rapp:** I would guess no because it's not as focused on keywords as on longer-form content. But from what I've seen tracking specific prompts in Scrunch, I see citations for the same prompt that include both versions. So my assumption is it would treat them very similarly.

**Brian Morrison II:** Okay.

**Alex Rapp:** I don't think we need to get too hung up on it. Obviously right now the content is unlisted, so we have more latitude to test. But once we put this public-facing on our domain, Colin's going to want it to look very polished and professional.

**Brian Morrison II:** Yeah, but unlisted just hides it from the blog index. It still shows up in search engines.

**Alex Rapp:** Right, but not everyone who comes to clerk.com will access it unless they've visited the subdirectory before and know how to get to it. We only have seven minutes left. Brian, can you remind me which article you started looking at?

**Brian Morrison II:** I think it was the 8 SSO.

**Andi Bailey:** The 8 SSO is the calibration article, so everybody went through that. You started on "Top Authentication Vulnerabilities."

**Brian Morrison II:** Yeah, I remember going through this.

**Andi Bailey:** Yeah, this is the one you started on. It was version zero from last week. We did a rewrite with myself and Yusuf, our technical expert, then the agentic rewrite. All three are now in the blog folder. There are still unresolved comments from our technical expert on preferences — Argon2 recommendations, NIST recommendations. This is a bit controversial. Where does Clerk land? Do you want us to adhere to NIST? Do you have best practices different from that?

**Alex Rapp:** I think NIST, right Brian?

**Brian Morrison II:** Well, I didn't catch what that's highlighting.

**Andi Bailey:** This is about password policy. The NIST recommendation eliminates requirements for special characters or numbers, but many organizations still impose complexity requirements. You have built-in support for ZXCVBN to check password complexity entropy. What's your preference here?

**Brian Morrison II:** I backed off on requiring special characters or numbers in favor of passphrases. To play it safe, probably lean toward the NIST recommendation.

**Andi Bailey:** Because if it's more exclusive and specific, it's probably the safer way to create complex passphrases. These are the little nuanced things where we want to know your preference so we can document it. These are nitpicky things where someone like Jeff might catch it, but they're a bit more subjective than objective.

**Brian Morrison II:** This would be a good question for Jeff since he's more into the product nuts and bolts than we are. I would definitely ask and relay the information.

**Andi Bailey:** Okay, perfect. It's almost like you have to create your own style guide, and the limit doesn't exist in terms of where you go with each preference. These are the kinds of questions our agentic flow didn't resolve, which is why we didn't want to share with everyone. Take a look at this versus the first one. You can see the progression. This was our first tool and this is the agentic rewrite. You can see the evolution without more back and forth from you. Hopefully with the deep dive we can close the loop and say this is our new bar. I think we're getting a lot closer and I'd love for you to take a look at this one.

**Alex Rapp:** Really quickly with the last minute we have — we'll definitely take a look at those new drafts. As I mentioned, both Brian and I are heading to the offsite next week, so it may be slower next week in terms of progress. Two things I wanted to mention — I saw the posts about Furo Images. Thank you for generating those. Let's table all that for right now and really focus on getting the content in a strong place. I'll have hellfire thrown my way if I introduce these while we're still getting content in shape. Playing devil's advocate, there's going to be pushback saying we'll want to use our own design resources. Let's focus on getting content sharp and accurate. Down the road, if we need these resources, we can revisit. I don't want to waste your team's time. They're great and consistent, but I can already see where that conversation goes.

**Andi Bailey:** Okay, sure.

**Alex Rapp:** Secondly, I've been putting together my own playbook for long-term use and as we build up a team, I want people educated in this area. I'd love it if you could share general notes on how you ensure structure and best practices are in place. What are your best practices for structuring content? Not creating it, but structuring it throughout the article — inline Q&A, FAQ sections, TLDRs at the top. I'd love your perspective on what you've seen, because there's so much conflicting information out there. To me, it seems logical to include FAQs because you're capturing more prompts. But you've had more cycles than I have. What learnings can you share? And from a post-processing standard, transitioning from Markdown to HTML — what are best practices there? Whatever you're comfortable sharing would help.

**Andi Bailey:** Yeah, we can definitely do that. I'll say some best practices are going to be — we're gearing more toward LLM. So yes to FAQs, but also yes to TLDR sections almost at the top, which isn't classically written. There are things like that where we're thinking about chunkability for LLM discovery, which is different. We're running formal experiments with A-B testing what's getting picked up. We'll have more insight. I can share stuff like that. But I'll warn you — some of it won't be what you learned in English class. Depending on who's reviewing it and their proximity to content generation these days, it might matter.

**Alex Rapp:** Yeah, we're seeing so much inconsistency in our data that I'm essentially an open book right now. I'm not going to have a hard stance against anything until we have data to suggest otherwise.

**Andi Bailey:** Cool.

**Alex Rapp:** All right. Awesome. Thank you, Andi. Is Ada still on our account, or is she out of office?

**Andi Bailey:** Ada's on vacation this week. She'll be back next week, but I think we'll be partnering on this.

**Alex Rapp:** Cool. I'll try to figure out what we do about next Thursday once we're boots on the ground in Iceland and have a sense of schedules. We have a calendar booked out, but I need to look closer to see when we can meet. Where are you located? Remind me.

**Andi Bailey:** I'm on the East Coast.

**Alex Rapp:** I'm East Coast too.

**Andi Bailey:** Oh, okay.

**Alex Rapp:** Good. I was going to say if you're West Coast, that's a tough time difference. But that's manageable.

**Andi Bailey:** Okay, so I think these will be done with the deep dive. Hopefully we'll send you something end of this week. Even if we don't talk, async calibration is something we can continue. Honestly, if we get these right, we can generate five or six more articles next week and really calibrate all of them to make sure we're covering all bases from a technical standpoint.

**Alex Rapp:** Okay, cool. Right now we should just focus on revision to the SSO article, right?

**Andi Bailey:** Well, yeah, and it's not 100% done. There's still comments because we want to get technical details finalized.

**Alex Rapp:** Okay, so wait for your signal before really looking at content.

**Andi Bailey:** But if you're curious about progress, just take a look at the three comparisons and see where we've come. You guys probably have a lot going on anyway.

**Alex Rapp:** Yeah, okay, cool. All right. Thank you so much. Have a great weekend and hope your conversation with Jeff goes well. Feel free to DM me if you need to share anything.

**Andi Bailey:** Okay.

**Alex Rapp:** Sounds good.

**Andi Bailey:** Thanks, Alex.

**Brian Morrison II:** Thanks, Brian. Bye. Thank you.
