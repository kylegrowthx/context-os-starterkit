# Vivek / Nathan Sync

<metadata>
date: 2025-11-10
time: 14:30 UTC
duration: 62 minutes
organizer: nathan@growthx.ai
participants: Nathan Navidzadeh, Vivek Shankar
fathom_recording_id: 100372071
fathom_url: https://fathom.video/calls/470083060
share_url: https://fathom.video/share/YtBRaJtGHyNSZyRxz9zx-p4ZDY_viMD9
source: fathom
enriched_on: 2026-03-02 18:45 UTC
</metadata>

---

## Summary

Nathan and Vivek reviewed feedback on recently published DataGrid articles and refined the workflow to improve draft quality and reduce editing time. Vivek identified issues with long sentences, tone drift ("software manual" style), and inconsistent table formatting, which revealed gaps in the assignment brief template. The team decided to front-load these edits into the brief itself—adding specific negative prompts (e.g., "avoid software-manual tone"), pre-defining CTAs, and clarifying SEO-vs-insight balance—rather than fixing them post-generation. Next steps include updating the brief template, fixing the DataGrid agentic pipeline's recurring "unexpected error," revising three specific articles (AI Product Manager, LLM metrics, Agentic vs non-agentic), and standardizing Webflow table implementation with a shared HTML template.

---

## Context

Nathan Navidzadeh and Vivek Shankar are content strategists at GrowthX working on the DataGrid knowledge base—a core product for delivering SEO-optimized, AI-focused B2B content. Nathan manages day-to-day content production and article assignments, while Vivek provides editorial feedback and refines content strategy. This meeting kicked off a quality improvement initiative after Nathan received Vivek's critical feedback on several published articles. The context is operational: GrowthX charges $200k+/year for content services, and DataGrid content quality directly affects client deliverables, team efficiency, and SEO performance. The feedback loop revealed a systemic issue—the assignment brief template wasn't detailed enough to guide AI content generation properly, causing multiple rounds of manual edits post-generation.

---

## Relevance

**To GrowthX Delivery:**
- Front-loading brief details (tone, CTAs, SEO expectations) will reduce editing time from 2+ hours to the 45–60 minute target, improving team efficiency and margins.
- The fix addresses a core pain point: LLMs tend to generate long, complex sentences; specific negative prompts in briefs ("write concisely," "avoid software-manual tone") measurably fix this.
- Standardizing Webflow table implementation using a shared HTML template + Claude substitution will reduce table re-work and ensure brand consistency.

**To CheckThat:**
- The "balance human & algorithm" framework is directly applicable to CheckThat's AEO strategy: foundational SEO sections + deep insights for AI PM personas.
- LLM metrics article revision (listing specific metrics like BLEU, ROUGE, Precision, Recall instead of categories) improves SEO signal and user value for AI visibility tools.

**To GrowthX Business Development:**
- Fixing the DataGrid agentic pipeline's recurring "unexpected error" unblocks scalable workflow and enables faster turnaround times for future clients.
- Quality improvements in published articles strengthen DataGrid's portfolio for client pitches and reference-ability.

---

## Overview

- **Front-load the workflow:** Move post-generation edits (tone, CTAs) into the assignment brief to reduce editing time from 2+ hours to the 45–60 minute target.
- **Balance human & algorithm:** Structure articles to satisfy both the ICP (deep insights) and search engines (foundational SEO sections) for optimal performance.
- **Fix the agentic pipeline:** Report the recurring "unexpected error" in the `#internal-datagrid` Slack channel to escalate the fix and enable the scalable workflow.
- **Standardize tables:** Use a shared HTML template and Claude to generate consistent, on-brand tables for Webflow.

---

## Key Topics

### Content Feedback & Workflow Refinement

  - **Problem:** Recent articles had issues like long sentences and a "software manual" tone.
  - **Root Cause:** Insufficiently detailed assignment briefs.
  - **Solution:** Front-load the workflow by moving post-generation edits into the brief.
      - **Rationale:** This improves the initial draft quality, reducing editing time to the 45–60 minute target.
      - **Method:** Use specific negative prompts (e.g., "avoid a software manual tone") and pre-define CTAs in the brief.

### Article Strategy: Balancing Human & Algorithm

  - **Problem:** The "AI Product Manager" article was too narrow, focusing only on agent deployment instead of the role's broader scope.
  - **Cause:** A conflict between the Airtable brief (which implied a deep dive) and the AI agent persona (which assumes foundational knowledge).
  - **Solution:** Balance content for both audiences.
      - **Algorithm:** Include foundational SEO sections (e.g., "What is an AI Product Manager?") to meet search engine expectations.
      - **Human:** Condense these sections into a single H2 and dedicate the rest of the article to deep, persona-relevant insights.
  - **Action:** Revise the "AI Product Manager" article to broaden its scope.

### Technical & Process Improvements

  - **Agentic Pipeline:** The tool remains broken with an "unexpected error."
      - **Action:** Report the issue in the `#internal-datagrid` Slack channel to ensure visibility for engineering, Mara, and Andy.
  - **Webflow Tables:** Tables appear unstyled due to missing CSS.
      - **Solution:** Use a shared HTML template and Claude to generate consistent, on-brand tables for Webflow.
  - **LLM Metrics Article:** The article lists metric *categories* (e.g., "Accuracy Metrics"), not the specific metrics themselves.
      - **Action:** Revise the article to list and briefly describe actual metrics (e.g., BLEU, ROUGE, Precision, Recall) to improve SEO and user value.

### Admin: Content Pillars & Out-of-Office

  - **Pillar Merging:** The goal is to simplify content categories for an upcoming DataGrid website redesign.
      - **Rationale:** To avoid a messy backend and prepare for a cleaner navigation structure.
      - **Status:** Not a performance concern; keyword cannibalization is not a current issue.
  - **Out-of-Office:** Nathan is eligible for the "quiet week."

---

## Action Items

**Nathan Navidzadeh (GrowthX)**
- Update assignment brief template: add tone prompt 'avoid software-manual tone'
- Post Linear link re: DG agentic pipeline error in #engineering-issues; update thread w/ fixes
- Revise 'AI Product Manager' article: add 'What is…' + skills sections; reframe ROI hypothetical
- Fix 'Agentic vs non-agentic' article: set publish date in Webflow CMS
- Update LLM benchmarks article: list 10+ specific metrics/benchmarks (e.g., BLEU, ROUGE, Precision, Recall) with 1-sentence descriptions to improve SEO and user value

**Vivek Shankar (GrowthX)**
- Add primary keywords to Airtable for refreshes/new articles
- Send preliminary pillar-to-category mapping to Nathan
- Send table HTML template to Nathan for Claude substitution implementation and briefing

---

## Transcript
**Nathan Navidzadeh:** Not much, Nathan.

**Nathan Navidzadeh:** How are you?

**Vivek Shankar:** Good.

**Vivek Shankar:** Happy Monday.

**Nathan Navidzadeh:** Happy Monday.

**Nathan Navidzadeh:** When I'm on call.

**Vivek Shankar:** No worries.

**Nathan Navidzadeh:** It's all good.

**Nathan Navidzadeh:** Yeah, it's 9.30 for you?

**Vivek Shankar:** It is 2.30 for me.

**Nathan Navidzadeh:** 2.30?

**Nathan Navidzadeh:** Oh, okay.

**Nathan Navidzadeh:** You're four hours in front of me.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** Yeah, I'm back in Lisbon now.

**Vivek Shankar:** Oh, that's right.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** We're in Peru, thankfully.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** I can breathe again.

**Nathan Navidzadeh:** Oh, man.

**Nathan Navidzadeh:** Cool.

**Nathan Navidzadeh:** Thanks for the feedback on the stuff, because that's stuff that I won't know, right?

**Nathan Navidzadeh:** I won't know automatically.

**Nathan Navidzadeh:** So I'd love to just go over some of that stuff.

**Nathan Navidzadeh:** Maybe I'll share my screen and we can go over it.

**Nathan Navidzadeh:** I'll figure out the best way to tackle that.

**Nathan Navidzadeh:** also moving forward.

**Nathan Navidzadeh:** Let me see here.

**Nathan Navidzadeh:** Sure.

**Nathan Navidzadeh:** Let's do this.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** So this one, I didn't, I don't know if you had attached an image, but I didn't see an image.

**Vivek Shankar:** It was just the same image, like just the block of text.

**Vivek Shankar:** Like this paragraph here?

**Nathan Navidzadeh:** Sort of thing?

**Vivek Shankar:** saw, yeah, I saw bigger ones, but I just figured the tables there.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** Okay.

**Nathan Navidzadeh:** So, so in your mind, these are, these are too big.

**Nathan Navidzadeh:** Yeah, it's kind of, yeah.

**Vivek Shankar:** I would maybe break it up like.

**Nathan Navidzadeh:** Like it's two sentences, but I guess they're, the first sentence is a little long because it has examples in it.

**Vivek Shankar:** I mean, yeah, I would just, you know, put it, put that, the workflows, I can say.

**Vivek Shankar:** I would just put it as a separate, I don't think it's a big deal, but it's tough because the LLMs, so this particular thing is actually something to watch out for.

**Vivek Shankar:** I haven't told the CMs this because, you know, I think it would just confuse them further, but usually the LLMs has a tendency to just write these ginormous sentences, right?

**Vivek Shankar:** I mean, they've shoved in, like, they follow the rule of three, but each of the things is like something massive, so it leads to these huge sentences.

**Vivek Shankar:** One thing that I found is that if it's doing that, it's probably lacking something in terms of writing guidelines.

**Vivek Shankar:** So if we tell it something like, you know, write in a concise manner or something like that, it usually fixes it.

**Vivek Shankar:** And the same goes for the second thing that I had sent over, which was the, in the follow-up message, to Kitson.

**Vivek Shankar:** Thread somewhere, I could have sworn I sent it.

**Vivek Shankar:** Yeah, think this one.

**Nathan Navidzadeh:** Yeah, this one.

**Vivek Shankar:** This one, like, if you look at the tone and everything, like math, investment against this, this, this, exploration, validates data availability and trust lightweight prompts, like, you know, it's very passive voice and it's very, like, software manual-like.

**Vivek Shankar:** So this just means, like, the writing guidelines are probably, they're not being followed and it leads to, like, long sentences sometimes.

**Vivek Shankar:** So, you know, if you see this generally, I would say, like, immediately that's a clue, like, instead of fixing it with Ask.ai, maybe just go into the artifact, the writing guidelines and just be like, okay, stop doing this nonsense, you know.

**Vivek Shankar:** So that's, like, a clue you can pick up sometimes.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** No, I've seen that before and I've seen it happen when I've asked it to do something concisely.

**Nathan Navidzadeh:** So because I tell it to make.

**Nathan Navidzadeh:** Something smaller, then it ends up becoming very dry and condensed, so it'll do these, like, map investment, explore, blah, blah, blah.

**Nathan Navidzadeh:** I'm like, what does that mean?

**Nathan Navidzadeh:** Like, what do you, and then I just get to be efficient or elaborate, give more information.

**Nathan Navidzadeh:** That's when I've noticed that actually happening.

**Nathan Navidzadeh:** This particular one, I didn't catch it, I guess, but...

**Vivek Shankar:** Yeah, I think the best way to mitigate this is to just say, like, maybe give it a negative prompt.

**Vivek Shankar:** Just be like, do not follow a software manual tone.

**Vivek Shankar:** It seems to understand that, because I, when I had this issue, I popped it, we had this issue massively for Galileo.

**Vivek Shankar:** It does it for, like, technical articles.

**Vivek Shankar:** So we popped it into Claude, and then just asked, like, okay, analyze this, and just tell me, like, as if I were instructing somebody, what would you say to Ovoid?

**Vivek Shankar:** And it just said software manual tone, right?

**Vivek Shankar:** So maybe try that.

**Nathan Navidzadeh:** Yeah, you know, yeah.

**Nathan Navidzadeh:** That might work.

**Nathan Navidzadeh:** Okay, and then you also said like the case study is off, so in what sense, because I don't see it off in my eyes, so I don't know if I see what you see.

**Nathan Navidzadeh:** I mean, these real world ROI, like we need links and I'm pretty sure data grid, these are not data grid examples because No, no, we don't have any, yeah, exactly, but I just thought, so I'm always kind of in this situation with data grid, obviously, where it's like, in our writing guidelines and what we want is for them to use real examples, real, like, tangible, tangible examples, right, to show the value of the product, but we don't have any actual examples or case studies, right?

**Nathan Navidzadeh:** So, so with this, I thought it was, I remember seeing this and thinking, this is good.

**Nathan Navidzadeh:** Because it gives you the sentiment, the idea of what happens, right?

**Nathan Navidzadeh:** So, you know, an enrichment system auto-populates the formal graphics, so then the sales reps don't have to do the manual research work to, you know, fill out that information.

**Nathan Navidzadeh:** This is how much, like, how many hours, you know, they gained because of it.

**Nathan Navidzadeh:** And, yeah, I guess this number here at the end is kind of, like, unnecessary, because what is that, you know, comes out of mind.

**Vivek Shankar:** Yeah, I mean, if you're, like, if we're going to say real-world ROI examples, then it has to have a link.

**Vivek Shankar:** Like, I would just keep that as, like, basic.

**Vivek Shankar:** You can rework this by saying, like...

**Vivek Shankar:** Just ROI, general ROI examples.

**Vivek Shankar:** Well, not even that, like, example, like, ROI scenarios.

**Vivek Shankar:** Practical scenarios or practical benefits.

**Vivek Shankar:** Yeah, anything to convey that this is not, you know, that this is hypothetical, that the numbers aren't, but...

**Vivek Shankar:** The scenario is, or you could even write it in.

**Vivek Shankar:** instead of real-world ROI examples, you can say, here's a hypothetical scenario.

**Vivek Shankar:** A sales operations company or whatever, a construction company did this.

**Vivek Shankar:** Each rep can gain eight hours weekly.

**Vivek Shankar:** And then you can have a calculation.

**Vivek Shankar:** So, you know, like the $240,000, you can reverse engineer it.

**Vivek Shankar:** Like it's basically calculating it for...

**Nathan Navidzadeh:** just calculating, yeah.

**Vivek Shankar:** Yeah, so just like, you know, it's a bit of a pain in the , but I think you can use Ask.ai to...

**Vivek Shankar:** It'll take a couple, three prompts, but you can use Ask.ai to basically expand this example and make it very clear that this is a hypothetical example.

**Vivek Shankar:** So something like that, like that's the workaround.

**Nathan Navidzadeh:** Yeah, I mean, I'm usually...

**Nathan Navidzadeh:** My workflow so far, what happens is I, you know, put the topic in Atlas, get it to generate the first kind of little assignment brief, but then I take that...

**Nathan Navidzadeh:** Assignment brief, I put it into Claude, and I massage it there.

**Nathan Navidzadeh:** I put it back into Atlas, run it through.

**Nathan Navidzadeh:** When it comes out with the article draft, that's when I put that into Claude, and Claude has the writing guidelines, it has the checklist, it has all the stuff, and I kind of do all the edits there.

**Nathan Navidzadeh:** So I start adjusting for tone, I start adjusting for, you know, I do the LLM visibility thing on it there, so that actually helps with a lot of breaking it up and, you know, making your statements pop out.

**Nathan Navidzadeh:** Yeah, so that's helped in different ways.

**Nathan Navidzadeh:** So I do all this kind of, it's already in Claude, so for me, yeah, that's easy.

**Nathan Navidzadeh:** I just have to spot this, and I mean, I would probably just edit this myself, but, you know, don't do real-world example.

**Nathan Navidzadeh:** If it's not a real example, call it a hypothetical or call it a scenario.

**Vivek Shankar:** Yeah, mean, generally, my impression is that process that you're using right now.

**Vivek Shankar:** I don't think it's going to scale.

**Nathan Navidzadeh:** No, it doesn't, no.

**Vivek Shankar:** Yeah, so I think, I know Panzer absolutely loves Claude, and he does a lot of stuff on Claude.

**Vivek Shankar:** My advice would be, don't do it, because it's, the marginal gain that you get from whatever Claude gives you in terms of editing, it's not worth the performance trade-off, and it's not worth the loss of your time.

**Vivek Shankar:** If you were in-house, I would say totally do this, like perfect it or whatever, but I think sometimes, you know, this is not a criticism of Panzer, it's just an observation.

**Vivek Shankar:** It's just like, I think he gets a little too editorial sometimes, and it's not practical, or when you're generating God knows how many articles per week, you can't do it.

**Vivek Shankar:** What I would suggest is, use the agentic pipeline, because we have that for data.

**Nathan Navidzadeh:** It's still broken.

**Nathan Navidzadeh:** Why is it broken?

**Nathan Navidzadeh:** Can you try a test?

**Nathan Navidzadeh:** I mean, I put a ticket last week, but I just sent a follow-up message this morning.

**Nathan Navidzadeh:** Oh, .

**Nathan Navidzadeh:** Okay.

**Vivek Shankar:** Yeah, if you're opening tickets, just create a thread in the internal DataGrid channel with, I just call it, like, engineering issues.

**Vivek Shankar:** If you scroll back up, in that channel, you'll see examples of it.

**Vivek Shankar:** So that's basically how we keep track of everything that is kind of being worked on, et cetera.

**Vivek Shankar:** So, yeah, articles, agent, with publishing, right?

**Vivek Shankar:** And.

**Vivek Shankar:** Yeah, I don't think I put the ticket here.

**Nathan Navidzadeh:** This one is still, this one didn't work.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** I mean, sorry.

**Nathan Navidzadeh:** I'm looking at it.

**Vivek Shankar:** Can you show that again?

**Vivek Shankar:** Yeah, sorry.

**Vivek Shankar:** Let's just disappear.

**Nathan Navidzadeh:** You want to see this one?

**Nathan Navidzadeh:** No, sorry.

**Vivek Shankar:** Is this the one, which is the ticket that you...

**Vivek Shankar:** It is, oh, it's not here.

**Nathan Navidzadeh:** me just create a thread in the channel and then you can drop it in there.

**Nathan Navidzadeh:** Okay.

**Vivek Shankar:** So every Monday I would just do it.

**Nathan Navidzadeh:** So the one that I created was this one.

**Vivek Shankar:** So this was opened on...

**Nathan Navidzadeh:** Where does it say that?

**Vivek Shankar:** It's probably, if you scroll the way down, it might say...

**Nathan Navidzadeh:** It three days ago.

**Vivek Shankar:** Okay.

**Vivek Shankar:** So it was on Friday.

**Vivek Shankar:** Yeah.

**Nathan Navidzadeh:** So what was the issue?

**Vivek Shankar:** Sorry.

**Vivek Shankar:** Okay.

**Nathan Navidzadeh:** So this is...

**Nathan Navidzadeh:** This is what happens.

**Nathan Navidzadeh:** So you go, you click Add, you put a topic in, whatever you want, you click Create, and right after you click Create, you just get this error, an unexpected error occurred, undefined method for blah, blah, blah.

**Nathan Navidzadeh:** So it doesn't even launch.

**Nathan Navidzadeh:** I can't do anything.

**Vivek Shankar:** Yeah, yeah, I'm getting that error too.

**Vivek Shankar:** Okay.

**Nathan Navidzadeh:** So they haven't fixed it.

**Vivek Shankar:** But yeah, what I would do is just take a link from this thread.

**Vivek Shankar:** So the linear on the top right, you'll see it's behind your Fathom corner.

**Vivek Shankar:** So if you just move that, you'll see the under Properties, it's down.

**Vivek Shankar:** There you go.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** And then the thread I tagged you on just now, the internal channel.

**Vivek Shankar:** It says Engineering Issues.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** You can just...

**Vivek Shankar:** Where'd it go?

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** You can just enter the issue like...

**Vivek Shankar:** DG, agentic pipeline, not working, and then just link, hyperlink, link.

**Vivek Shankar:** So, yeah, there you go.

**Vivek Shankar:** And then I usually tell the guys to switch off URL previews.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** Switch that off because it just clogs the entire command.

**Vivek Shankar:** Is there a way to, like, actually tell it to stop doing that?

**Nathan Navidzadeh:** I think there's a setting somewhere.

**Nathan Navidzadeh:** I always have to do that.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** So, anyway, just, and what you do is, like, if whatever updates you get for this particular thing, just keep updating that thread.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Because the reason we recorded this way is because I look at it, Mara looks at it, even Andy looks at it.

**Vivek Shankar:** So then in case something's being delayed, we can jump on engineering and they proactively just jump it and flag it.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** Okay.

**Vivek Shankar:** You don't have to bookmark the issue, but as long as it's there in the engineering thread, it's fine.

**Vivek Shankar:** For your reference, if you want to bookmark it, go ahead.

**Vivek Shankar:** Oh, no, that's fine.

**Vivek Shankar:** It's your account, so, you know, feel free.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** No, no, I find it in linear.

**Nathan Navidzadeh:** That's fine.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** So, yeah, getting back to this thing, until that thing is being fixed, what I would do is I would generate that assignment brief one shot in Claude, and then after that, I would use Ask AI to edit.

**Vivek Shankar:** If you're getting too many edits in the...

**Nathan Navidzadeh:** Yeah, all the edits that I do in Ask AI are kind of like the ones that I would do in Claude, but I just feel like Ask AI doesn't...

**Nathan Navidzadeh:** Here, like, I'll give you...

**Nathan Navidzadeh:** I have them all listed now, so it makes it easier for me, but this is one of the first ones that I usually do, right?

**Nathan Navidzadeh:** So I say, make sure all the headings are scannable, value-driven, and direct instead of editorial magazine-style headers, right?

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** So then Claude goes through, fixes all the headings.

**Nathan Navidzadeh:** Great.

**Nathan Navidzadeh:** ...

**Nathan Navidzadeh:** ...

**Nathan Navidzadeh:** ...

**Nathan Navidzadeh:** ...

**Nathan Navidzadeh:** ...

**Nathan Navidzadeh:** Usually I have something that talks about remove jargony terms.

**Nathan Navidzadeh:** So I can definitely plug in the kind of manual, what do you say, avoid software manual language.

**Nathan Navidzadeh:** Then I copy paste this thing, which I grabbed from your SOP, right?

**Nathan Navidzadeh:** And that helps.

**Vivek Shankar:** So this thing, I don't think you need to do it because if the assignment brief, that process kind of takes care of this.

**Vivek Shankar:** It's not going to make it 100%, but a lot of this is experimental.

**Vivek Shankar:** So the main thing that we want to hit is just each H2 and H3 stands by itself.

**Vivek Shankar:** As long as that is good, I don't think we need to optimize for anything else.

**Vivek Shankar:** So the stuff like assess sentence structure for citation-friendly formatting, feature snippet potential, I don't think we need to do that.

**Nathan Navidzadeh:** So it runs the analysis, but I don't end up choosing it.

**Nathan Navidzadeh:** Everything that it does.

**Nathan Navidzadeh:** So Always.

**Nathan Navidzadeh:** Always.

**Nathan Navidzadeh:** But I can't do this in Ask.ai.

**Nathan Navidzadeh:** So if you're saying just don't do it, can just not do it.

**Vivek Shankar:** I think Ask.ai can do it, actually, because it's basically, it's just a cloud wrapper, Ask.ai.

**Vivek Shankar:** So it can do it.

**Vivek Shankar:** It can give you suggestions.

**Vivek Shankar:** But my point is, I wouldn't even do this step, because if the assignment brief is followed well, then I don't think there's much of an issue there.

**Vivek Shankar:** So it should be good to go.

**Vivek Shankar:** So, yeah, the data grid value naturally introduced.

**Vivek Shankar:** See, that as well, I would take care of in the assignment brief section.

**Vivek Shankar:** So when you're creating the outline, you just make sure manually that data grid is in there, you know.

**Vivek Shankar:** And I think it's not like it ignores it.

**Vivek Shankar:** It's pretty much, it does it.

**Vivek Shankar:** And then the CTA section as well, I would take care of that in the assignment brief stage.

**Vivek Shankar:** Just, you know, you can do this one of two ways, right?

**Vivek Shankar:** I didn't develop a process for this, but for Galileo, for example, what we do is they like a very specific CTA, so we just copy-paste that thing every single time into every article.

**Nathan Navidzadeh:** So what I've been doing is, so this is the CTA section that you provided again in the SOP, the one with the bulleted list where it kind of like, you know, one that there's one that you had written out before.

**Nathan Navidzadeh:** It says, like, mention how DataGrid naturally supports the article context in a bullet-pointed, concentrated list of, you know, four to five points, one to two sentences each that reinforce what we have discussed, then include a single-sentence CTA that invites the reader, blah, blah, blah.

**Nathan Navidzadeh:** So I don't always say four to five points.

**Nathan Navidzadeh:** If I feel like it doesn't need four to five points, I'll shorten it to two to three.

**Nathan Navidzadeh:** But I generally found that, you know, I like that style of CTA.

**Nathan Navidzadeh:** CTA for this, and if it's mentioned throughout the article a couple of times, and then there's that CTA at the end, it seems pretty good.

**Nathan Navidzadeh:** Yeah, exactly.

**Vivek Shankar:** You could even have that how data grid helps section before the CTA, so you don't need a massive CTA at the end.

**Vivek Shankar:** So that could be another waste.

**Vivek Shankar:** But whatever this you're doing, I would take care of all this in the assignment brief stage.

**Vivek Shankar:** I wouldn't do it in post-editing, because if you give it clear writing instructions in the old pipeline, it will do all this for you, and then you'll just kind of save time for yourself, you know?

**Vivek Shankar:** Yeah.

**Nathan Navidzadeh:** Trying to find you.

**Nathan Navidzadeh:** Where did you go?

**Vivek Shankar:** Yeah.

**Vivek Shankar:** I thought you were looking at me all this while.

**Nathan Navidzadeh:** All right.

**Nathan Navidzadeh:** No, I'm trying to find you.

**Nathan Navidzadeh:** I'm looking at my screen, trying to find you, man.

**Nathan Navidzadeh:** You got too many screens, man.

**Nathan Navidzadeh:** I got too much stuff going on.

**Nathan Navidzadeh:** Is this you?

**Nathan Navidzadeh:** This is my screenshot.

**Nathan Navidzadeh:** is so funny.

**Nathan Navidzadeh:** That's just...

**Vivek Shankar:** There you go.

**Vivek Shankar:** That's my, no, that's just me.

**Vivek Shankar:** Oh, you don't see me?

**Nathan Navidzadeh:** No, I can't see.

**Nathan Navidzadeh:** Well, your screen sharing stops, so.

**Vivek Shankar:** Yeah.

**Nathan Navidzadeh:** Okay, it's down here.

**Nathan Navidzadeh:** Allow this time.

**Nathan Navidzadeh:** Oh, I think it got minimized or something.

**Nathan Navidzadeh:** Yeah, I got minimized.

**Nathan Navidzadeh:** That's what happened.

**Nathan Navidzadeh:** Okay, so it's you now.

**Nathan Navidzadeh:** Okay, that's cool.

**Nathan Navidzadeh:** That's helpful.

**Nathan Navidzadeh:** Let me also, I'm to continue sharing my screen.

**Nathan Navidzadeh:** I'm going to do something different here because this is better.

**Nathan Navidzadeh:** Because I have two screens, right?

**Nathan Navidzadeh:** then.

**Vivek Shankar:** But, yeah, I think a lot of the, at least the time sinks you're facing, I think it's happening because maybe the assignment brief is not well-tuned enough.

**Vivek Shankar:** So even the tone, right?

**Vivek Shankar:** The software manual.

**Vivek Shankar:** I think if you, you can add that as a copy paste in each section in the assignment brief and just say, like, write this in this tone and avoid the software manual, technical software manual tone, right?

**Vivek Shankar:** It'll do it for you in that section.

**Vivek Shankar:** Like specifically for the section, yeah, if I think it's good.

**Nathan Navidzadeh:** Yeah, I mean, it's also about, I mean, yeah, hopefully I can see that.

**Vivek Shankar:** Yeah, the reason I'm saying it is because I'm just trying to help you out with your time because there's like, you know, we're going to get newsletters on board and then we're going to get the programmatic pages on as well.

**Vivek Shankar:** and, you know, all those things are going to need a lot of coordination.

**Vivek Shankar:** So, um, if editorial, like I would, um, I would encourage you to time yourself.

**Vivek Shankar:** So your editorials get it done under like 60 minutes, like 45 to 60 minutes.

**Vivek Shankar:** I know, I know.

**Nathan Navidzadeh:** They're like two hours plus right now.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** And that's after I've got a process.

**Nathan Navidzadeh:** But before, it was taking like three hours or more.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** I would look at it.

**Nathan Navidzadeh:** like, this doesn't look good.

**Nathan Navidzadeh:** So all the steps that I wrote out for you, that's kind of where I could get it to a level where I was happy with it.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** still, like, the, you know, pumping them out for me to have to, like, you know, I need to be able to look over it at some point.

**Nathan Navidzadeh:** And so to catch things like this.

**Nathan Navidzadeh:** an hour should be good if the article that gets pushed out is good from the assignment.

**Nathan Navidzadeh:** Yeah, but that depends on the input.

**Vivek Shankar:** So that's why I would say, like, maybe this is the next step of evolving that process, right?

**Vivek Shankar:** So whatever you're doing in the post-editing, post-generation stage, editing stage, I would just port that over to the assignment-free stage.

**Vivek Shankar:** Like, for the CMs, I told the CMs I spend at least 30 to 45 minutes creating that assignment-free stage.

**Vivek Shankar:** Because that is your output, really.

**Vivek Shankar:** As long as that is good, the rest of the flow runs in like 15 to 20 minutes.

**Vivek Shankar:** It's super simple.

**Vivek Shankar:** And then the editing is just basic .

**Vivek Shankar:** So I would think of it in that sense.

**Vivek Shankar:** Just front load everything as much as possible.

**Vivek Shankar:** And then I think once you do that, you find that it saves you a lot of time.

**Vivek Shankar:** The other thing I would say is like, if you ever find yourself in a situation where you need to deliver like three, four articles, in one day, that's a bad position to be in.

**Vivek Shankar:** It's way too much.

**Nathan Navidzadeh:** That was my whole week yesterday, like the last week.

**Nathan Navidzadeh:** was every single day.

**Vivek Shankar:** Yeah, I noticed like that is just way too much.

**Vivek Shankar:** I mean, when I say articles, I'm talking about full articles.

**Vivek Shankar:** So refresh for me is like half an article.

**Vivek Shankar:** But data refreshes are like full articles.

**Nathan Navidzadeh:** Yeah, exactly.

**Vivek Shankar:** Yeah, so, um, yeah, yeah, think.

**Vivek Shankar:** So,

**Nathan Navidzadeh:** Yeah, those refreshes were not refreshes, honestly.

**Nathan Navidzadeh:** were like...

**Nathan Navidzadeh:** Yeah, they're like full rewrites.

**Vivek Shankar:** To be honest, like, I don't know.

**Vivek Shankar:** And there's the other tasks as well that we need to do, which is like, you know, just remapping those content pillars.

**Vivek Shankar:** Like, I can do that.

**Vivek Shankar:** It's not an issue.

**Vivek Shankar:** But for the refreshes as well, I'm realizing that maybe it might make your life easier if I just tag those articles with a primary keyword.

**Vivek Shankar:** I don't know if that would help.

**Vivek Shankar:** And then, you know, we could go from there.

**Nathan Navidzadeh:** It would, because for those ones, I don't really have direction.

**Nathan Navidzadeh:** So things that have been helpful are in Airtable when there is the little description of what you expect.

**Nathan Navidzadeh:** Although I didn't hit it for the AI Project Manager one.

**Nathan Navidzadeh:** I thought that one aligned with what you wanted.

**Nathan Navidzadeh:** But if you have something specific in mind for the article, put that somewhere in Airtable, right?

**Nathan Navidzadeh:** It's what I can, you know, so if it's keywords, if it's, you know.

**Nathan Navidzadeh:** Because otherwise, the way that I start is I, if there's keywords, okay, I'm going to try to see how this keyword works with that topic.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** Are you just, because I'm not fully familiar with your background, are you comfortable kind of going into SEMrush?

**Vivek Shankar:** And if I give you the keyword, are you comfortable going to SEMrush, looking at competitor articles and just seeing like, okay, these sections need to be present?

**Vivek Shankar:** Like, are you comfortable with that?

**Nathan Navidzadeh:** Yes, I have a background in SEMrush, but I don't, we don't have access to that.

**Nathan Navidzadeh:** And when I was using SEMrush and I put the keyword in.

**Nathan Navidzadeh:** Really?

**Nathan Navidzadeh:** You should.

**Nathan Navidzadeh:** No, no, do, we do.

**Nathan Navidzadeh:** No, no, sorry, sorry.

**Nathan Navidzadeh:** I'm thinking when I put the, when I put our old article in, so this is what I was doing with the refreshes.

**Nathan Navidzadeh:** I would take the URL for our existing one, put it in SEMrush to see which keywords we're ranking for already, to see if we can try to improve the ranking on those existing ones, but it doesn't, yeah.

**Vivek Shankar:** So that's, yeah, those ones kind of were ahead of SEMrush.

**Vivek Shankar:** Many things, and yeah, but okay, I'll start adding those keywords.

**Vivek Shankar:** think that should help.

**Vivek Shankar:** For the AI product manager, I'm just, well, let's take this as an example.

**Vivek Shankar:** Let me just share my screen because I just want to make sure I give you everything you need.

**Vivek Shankar:** So for this one, it said this guy covers everything these people need, essential competency, competencies, stakeholder management, unique challenges of shipping AI-powered.

**Vivek Shankar:** Yeah, okay.

**Vivek Shankar:** And the article I felt was, yeah, it was, it felt like a subset.

**Vivek Shankar:** So it was just about how to deploy agents.

**Vivek Shankar:** It wasn't so much what is an AI product manager, right?

**Vivek Shankar:** But how has this role evolved, essential skills needed, and this kind of thing.

**Vivek Shankar:** Like, see stakeholders in here, but, yeah, this one seemed disconnected from this a bit.

**Vivek Shankar:** Like, you know, we're talking about aligning stakeholders, and then how do they prioritize agent workflows, calculating ROI, which you're correct about.

**Vivek Shankar:** That was my mistake.

**Vivek Shankar:** Like, then, yeah, it just felt a little, here we're getting into it, but, yeah, it was like, you know.

**Vivek Shankar:** It builds up into it.

**Nathan Navidzadeh:** I know what you're saying, but that one, it did build up, but I also see what you mean.

**Nathan Navidzadeh:** Like, if you wanted it to be more of a general guide, and it looked like it was a bit too specific into something.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** Like, if you go in here, and if you look at this, I think this was the keyword, yeah.

**Vivek Shankar:** You can see, like, the questions, how to become one, will AI replace product managers, how can product managers use AI, this is, like.

**Vivek Shankar:** Useful section header information.

**Vivek Shankar:** But then over here, I look at some of these competitive articles, like straight up, what is an AI, what is AI product management?

**Vivek Shankar:** You don't need these stupid Venn diagrams or whatever, but, you know, like evolution of the role, this kind of thing.

**Vivek Shankar:** Right, right.

**Nathan Navidzadeh:** So I guess that's when, so do I prioritize the keyword that you provide or do I prioritize the little blurb about it in Airtable?

**Nathan Navidzadeh:** That you provide.

**Nathan Navidzadeh:** Because the article was written based on kind of both, I guess, but I think the Airtable is what I, is what I would, I would tell in the assignment brief and in Claude, I would say, make sure everything aligns with the main topic, which was this.

**Nathan Navidzadeh:** I would always give it this exact paragraph and I would say, make sure it hits all of these notes.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** Which doesn't have, which doesn't have things like what is a product manager, you know, those.

**Nathan Navidzadeh:** Okay.

**Vivek Shankar:** Okay, I see what you mean, like, okay, because from my perspective, this covered that, so I can see it doesn't explicitly mention it, so obviously that can cause confusion.

**Vivek Shankar:** All right, I see that.

**Vivek Shankar:** What I would say is this, like, you have plenty of leeway in just, like, massaging these to whatever you think is fit, right?

**Vivek Shankar:** Like, my, the ultimate aim here is that this thing needs to perform, that's it.

**Vivek Shankar:** So when we're performing, so in terms of performance, really, we're talking about two things, which is the human side, the algorithm side.

**Vivek Shankar:** So I would just say, like, I would approach this with the, and I've told this to the CMs as well, like the CMs, I think they don't even read this sometimes.

**Vivek Shankar:** They just kind of look at the keyword and then they think like.

**Vivek Shankar:** Okay, this needs to be for the human being, which is a persona, and this needs to be for the algorithm.

**Vivek Shankar:** Okay, how do I satisfy the intent over here?

**Vivek Shankar:** And then just build it out based on that.

**Vivek Shankar:** So this over here is like, this is like an AI generated thing.

**Vivek Shankar:** And, you know, I can't list like every single thing that should go in here because then I'm basically running the article structure, right?

**Vivek Shankar:** And it's going to take too long.

**Vivek Shankar:** So I would say think of it in that terms, right?

**Vivek Shankar:** Like, okay, this thing needs to perform.

**Vivek Shankar:** How do I address the ICP?

**Vivek Shankar:** How do I address the whatever, the algorithm?

**Vivek Shankar:** Okay, so what are my sections?

**Vivek Shankar:** And I will go from there.

**Vivek Shankar:** So the algorithm side is basically addressed by SEMrush and all of this stuff, right?

**Vivek Shankar:** And then, yeah, like the ICP stuff, you know, we already have it in our artifacts.

**Vivek Shankar:** So you can use that to build some sections.

**Vivek Shankar:** Does that help at all?

**Vivek Shankar:** It does.

**Nathan Navidzadeh:** Because it's just there's always...

**Nathan Navidzadeh:** Compost.

**Nathan Navidzadeh:** It's like conflicting things, right?

**Nathan Navidzadeh:** Like even for that article, like if you look at, so it's about AI product managers, right?

**Nathan Navidzadeh:** But previously, you know, so I had to make a call, obviously, in this situation.

**Nathan Navidzadeh:** But previously, you said anything that goes into the AI at scale category, that we're going to be targeting the AI agent persona, right?

**Vivek Shankar:** AI product manager, AI agent architect, they're the same kind of person, really.

**Nathan Navidzadeh:** Right, but if you look at what's written in that persona, what the AI generator, what Claude does, or what Atlas does, is they say, well, somebody that's an AI architect, or an AI product manager, like they already know what an AI product manager is.

**Nathan Navidzadeh:** They already know these things that you are saying, all those basic things.

**Nathan Navidzadeh:** So it doesn't include them.

**Nathan Navidzadeh:** It literally, there's other sections that will say like, yeah, exactly, yeah.

**Nathan Navidzadeh:** So I can, but for me, so then I have to.

**Nathan Navidzadeh:** And understand, like, okay, what is the goal of this article?

**Nathan Navidzadeh:** So if you're saying it's just performance, then, yeah, what I would do is do the keyword research, like you said.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** And I would make a judgment call and probably say, okay, right now it might be too early to go this deep for an AI product manager.

**Nathan Navidzadeh:** When people are asking about that, they just want to know what an AI product manager is.

**Nathan Navidzadeh:** They just want to know these basic things.

**Vivek Shankar:** Yeah, like I would say those sections are for the algorithm.

**Vivek Shankar:** Because the algorithm and the LLMs, they kind of expect, like, okay, if these people are talking about AI product managers, based on the universe of what already exists, I expect to see what is an AI product manager section in there.

**Vivek Shankar:** I expect to see a skill section.

**Vivek Shankar:** So, yeah, these people, the persona knows about it, but we're kind of balancing.

**Vivek Shankar:** That's where the balancing act comes in, right?

**Vivek Shankar:** We're kind of balancing the machine and the human, unfortunately.

**Vivek Shankar:** At least, like, we'd love to write for humans, but if we did that, we wouldn't get found.

**Vivek Shankar:** yeah, that's kind of where the thing comes.

**Vivek Shankar:** What you can do, maybe, like, I mean, I agree, they're kind of  sections, like, what is an AI product manager is a  section.

**Vivek Shankar:** You can condense all that SEO  into, like, one H2, maybe, and then put under H3s, and then get into the real meat of the stuff with the rest of the article.

**Vivek Shankar:** Like, feel free to do that.

**Vivek Shankar:** You can structure it that way as well, Fathom.

**Nathan Navidzadeh:** So, okay, yeah, no, that makes sense.

**Nathan Navidzadeh:** Yes.

**Nathan Navidzadeh:** So, practically speaking, then, for this article, are we going to revisit this, or is this just a learning moment for me to move on for the next articles?

**Nathan Navidzadeh:** Like, does that matter?

**Nathan Navidzadeh:** we?

**Vivek Shankar:** I would revisit this because, yeah, like, and it's not like, I mean, you can just work on it this week, you know, like, and feel free to push an editorial out to next week if it's too much of a workload for you.

**Vivek Shankar:** So, like, one article here and there, it's fine, you know, like, nothing, it's not like, and.

**Vivek Shankar:** He's going to get on you and be like, oh, what the hell are you doing or whatever.

**Vivek Shankar:** You have that much judgment and I would say leeway.

**Vivek Shankar:** It's just that let's just not make a habit of it is all I'm saying.

**Vivek Shankar:** Like this kind of thing happens a lot with the CMs and it's why I got them to send me those high-level outlines because we'd often end up with like this article and I'd be like, okay, what the heck is this?

**Vivek Shankar:** You know, it's not saying this is like that, but I'm saying like, at least the situations where it's like they need to work on it again and they're not sure.

**Vivek Shankar:** So what I do in that situation is I push out a few articles here and there.

**Vivek Shankar:** The client doesn't really care that much.

**Vivek Shankar:** It's just that if we keep doing it for a month or two months, then they'll start noticing.

**Vivek Shankar:** Week or two.

**Nathan Navidzadeh:** Yeah, No, no, absolutely.

**Nathan Navidzadeh:** No, I just, yeah.

**Nathan Navidzadeh:** Until that gap is filled, like I'm able to see, I can sort of see it like definitely more than some of the CMs.

**Nathan Navidzadeh:** Like what the article should contain based on.

**Nathan Navidzadeh:** And what's an air table?

**Nathan Navidzadeh:** But sometimes I miss things.

**Nathan Navidzadeh:** And I don't want to message you for an individual article to be like, hey, what are you actually really looking for?

**Nathan Navidzadeh:** I mean, I could message you about that if you want, but I feel like that's not going to scale if I have to do that.

**Nathan Navidzadeh:** So I just want to be able to develop the vision to be like, oh, yeah, I see kind of what we're looking for.

**Nathan Navidzadeh:** So this ties into the conversation about kind of merging the pillars.

**Nathan Navidzadeh:** So two questions there.

**Nathan Navidzadeh:** So merging the pillars in terms of tracking purposes is one thing, right?

**Nathan Navidzadeh:** So we're talking about Looker.

**Nathan Navidzadeh:** We're talking about how we're tracking them.

**Nathan Navidzadeh:** And if you want to combine categories like that or bring them all to the same floor that we have, okay, that's one thing that we can try to figure out to do.

**Nathan Navidzadeh:** But my bigger concern with our articles so that we can make sure...

**Nathan Navidzadeh:** that everything continues to perform well is the whole, do you know about keyword cannibalization?

**Nathan Navidzadeh:** So that's what I'm worried about, right?

**Nathan Navidzadeh:** So do we have pillar pages, as they call them?

**Nathan Navidzadeh:** So if we have the guide to AI product management, that's the pillar page, and then it has sister, or like parent page, and then there's sister pages about specifics to AI product management.

**Nathan Navidzadeh:** So you know all about this, right?

**Nathan Navidzadeh:** So we got to figure out the structure like that, if we want to make sure that everything performs well, which ideally, we come up with that kind of content structure before we push out 10 articles a week.

**Nathan Navidzadeh:** But because you want to make sure that your smaller pages are all feeding internal links back up to the parent pages, so that then this is all grouped together, and Google sees them like that.

**Nathan Navidzadeh:** But that's Google, right?

**Nathan Navidzadeh:** So that's how Google sees things.

**Nathan Navidzadeh:** I don't know how LLMs...

**Nathan Navidzadeh:** Yeah, I mean, I think they'll take their...

**Vivek Shankar:** From Google.

**Vivek Shankar:** But in terms of pillar versus cluster pages, so that's where the programmatic pages come in.

**Vivek Shankar:** So that was my original plan, actually.

**Vivek Shankar:** So this was, I proposed this to them back in February, right?

**Vivek Shankar:** And they were supposed to redesign the website.

**Vivek Shankar:** Well, here we are.

**Vivek Shankar:** So the only reason we don't have the hub and spoke model or the pillar and satellite model is because we're just waiting on them to design stuff.

**Vivek Shankar:** And I'm not like, if we were to have pillar pages, I would rather they not sit under the blog subfolder.

**Vivek Shankar:** I would rather they sit in resources and then we, whatever, push it out.

**Vivek Shankar:** But that's going to need further redesign.

**Vivek Shankar:** And it's, it's, I don't know when that's going to happen.

**Vivek Shankar:** So basically, you know, we're just going to have to make sure with whatever is best here.

**Vivek Shankar:** In terms of cannibalization, I'm not too worried because we have some very clear pillars.

**Vivek Shankar:** There hasn't been any major topic overlap for the experimental articles that we were pushing out.

**Vivek Shankar:** Some of them are like child articles and stuff like that.

**Vivek Shankar:** And I think the internal linking takes care of that because this was when we were on Aerobs.

**Vivek Shankar:** The internal linking on that used to work much better.

**Vivek Shankar:** And we made sure that we were linking within specific categories.

**Vivek Shankar:** So I think that's taken care of.

**Vivek Shankar:** In terms of cannibalization, I don't think that's a concern right now, given our volumes and just given the number of pages we have.

**Vivek Shankar:** We honestly don't have that many pages, despite the 500, 600 that we published.

**Vivek Shankar:** So I'm kind of putting that as a next year's problem, this time next year, maybe.

**Vivek Shankar:** So for now, it's more that, you know, looking at that long  list of like pillars or whatever.

**Vivek Shankar:** Like, for example, AI agents, right?

**Vivek Shankar:** AI agents has talked about, yeah, it's a cash roll because it was just like an experimental pillar that worked well.

**Vivek Shankar:** And then we dove deeper into it.

**Vivek Shankar:** So I think that needs to map back somehow to sales use cases, CS, project management, AI product at scale, and miscellaneous, obviously.

**Vivek Shankar:** So yeah, that's the kind of thing that we need to do and just so that it looks cleaner.

**Vivek Shankar:** For performance tracking, it doesn't really matter because we're changing labels on it.

**Vivek Shankar:** The overall numbers are going to be the same, but it's more that at some point, DataGrid's going to finish their website updates, and it's going to be a huge mess on their back end in terms of how things are categorized.

**Vivek Shankar:** So I just want to have those categories mapped in advance so that we are not playing catch up with them.

**Vivek Shankar:** It's a whole long story, but basically the way they've designed their website, their new website, the categories are dropped.

**Vivek Shankar:** And right now, if anybody clicks the dropdown, you see a hundred things.

**Vivek Shankar:** So Thiago is going to come back to us and say, this sucks.

**Vivek Shankar:** Let's fix this.

**Vivek Shankar:** So we'll be like, hey, we have these seven things.

**Vivek Shankar:** Okay, great.

**Vivek Shankar:** Just push it out.

**Vivek Shankar:** Okay, got it.

**Vivek Shankar:** Got it.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** No, I wasn't aware that those categories were being used anywhere other than tracking purposes.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** I mean, technically nobody's using them, but their website has it.

**Nathan Navidzadeh:** They're in Webflow.

**Nathan Navidzadeh:** So Suleiman, he, okay, yeah.

**Nathan Navidzadeh:** So like that, I didn't know that, right?

**Nathan Navidzadeh:** So I haven't looked at the Webflow at all yet, so I have no idea.

**Nathan Navidzadeh:** Yeah, yeah.

**Vivek Shankar:** But yeah, that's kind of the thing.

**Vivek Shankar:** I would say, you know, I don't think it's a huge kind of...

**Vivek Shankar:** Yeah, we got to go over it and we got to figure out which ones we can probably...

**Vivek Shankar:** Yes, I can run a quick mapping and just send over a preliminary list.

**Vivek Shankar:** So it's not an issue.

**Vivek Shankar:** But I would say for now, yeah, I would just focus on...

**Vivek Shankar:** Let's do it again.

**Vivek Shankar:** In your position, I would just focus on the time usage because there's a  ton more coming and, you know, it's not kind of, yeah, so I just want to make sure you have everything.

**Nathan Navidzadeh:** Yeah, I got to make sure I'm set up to be able to push these out fast because, yeah, there's, there's what I get, I have maybe 15 minutes per article to actually, like, look over the article.

**Nathan Navidzadeh:** So I need to make sure the content is good enough so that it only takes me 15 minutes to do the, or 20 minutes to do the rest.

**Nathan Navidzadeh:** Yeah, pretty much, yeah.

**Nathan Navidzadeh:** Cool.

**Nathan Navidzadeh:** So, so I know we're almost running out of time, but I just want to go over a couple of things real quick here.

**Nathan Navidzadeh:** So there, there was the, the table that looked weird.

**Nathan Navidzadeh:** So that shouldn't look like that.

**Nathan Navidzadeh:** Is that just a.

**Vivek Shankar:** I think the HTML is often that because I'm wondering if, yeah, maybe the text color or something is like, well, it doesn't look like the.

**Nathan Navidzadeh:** You know, the nice one that time that we had seen that Nika had made.

**Nathan Navidzadeh:** So I don't know.

**Nathan Navidzadeh:** And there's probably other tables.

**Vivek Shankar:** I think if you pop this, let me pop this into Claude real quick.

**Vivek Shankar:** I think I can, I think I know what the issue is like.

**Vivek Shankar:** Just give me one second.

**Nathan Navidzadeh:** But, you know, that's the thing.

**Nathan Navidzadeh:** If I want that to scale, then I, we have to, obviously we have to get the publishing workflow to work properly.

**Nathan Navidzadeh:** But for now, I'll also need to get Suleiman to do it properly.

**Nathan Navidzadeh:** Because I can't go in every time in Webflow and fix the table every time.

**Vivek Shankar:** No, I think if we give him like, yeah, I think there's a way.

**Vivek Shankar:** Basically, just have, we can just have like a sample HTML, like a templated HTML.

**Vivek Shankar:** And then we just use, we just substitute the content over and over.

**Vivek Shankar:** What am I looking for?

**Vivek Shankar:** There we go.

**Vivek Shankar:** Okay, let's see what Claude gives me.

**Vivek Shankar:** Sorry, I'm just testing something.

**Nathan Navidzadeh:** It's okay.

**Vivek Shankar:** Okay, so I asked Claude to basically fix the thing.

**Vivek Shankar:** Now let me go into Webflow.

**Vivek Shankar:** Oh, come on.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Okay.

**Vivek Shankar:** you.

**Vivek Shankar:** Why is it doing this?

**Vivek Shankar:** It's going to separate Webflow.

**Vivek Shankar:** Oh, okay.

**Vivek Shankar:** That explains it.

**Vivek Shankar:** There we go.

**Vivek Shankar:** All right.

**Vivek Shankar:** So DataGrade, then 2025.

**Vivek Shankar:** Over here.

**Vivek Shankar:** Log.

**Vivek Shankar:** This is AI product.

**Vivek Shankar:** This one.

**Vivek Shankar:** Okay.

**Vivek Shankar:** This thing.

**Nathan Navidzadeh:** How did you open up this window?

**Vivek Shankar:** That's not going to work.

**Vivek Shankar:** Okay.

**Vivek Shankar:** You click on CMS here on the top left.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** And then you...

**Vivek Shankar:** come to blogs, and then it will show you the list of blogs, and I just clicked on the AI Product Manager blog.

**Nathan Navidzadeh:** Yes, no, I mean the custom code block.

**Nathan Navidzadeh:** this thing.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** I just clicked, like if you hover over this, it goes got it.

**Nathan Navidzadeh:** I didn't see that.

**Nathan Navidzadeh:** Okay.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** So here, I'm going to take this.

**Vivek Shankar:** Oh, you don't mean block type and anything, but anyway.

**Vivek Shankar:** Save, Close, Click Publish now.

**Vivek Shankar:** Let's see if anything happened.

**Vivek Shankar:** There we go.

**Vivek Shankar:** Okay.

**Nathan Navidzadeh:** It's basically the text is white.

**Vivek Shankar:** The problem is, oh, man, okay.

**Vivek Shankar:** So the headers are white.

**Nathan Navidzadeh:** It looks fine on mine, though.

**Nathan Navidzadeh:** just opened it.

**Nathan Navidzadeh:** Yeah, that's so weird.

**Nathan Navidzadeh:** Maybe it's a cache issue.

**Nathan Navidzadeh:** Can you see the headers?

**Nathan Navidzadeh:** Yeah, yeah.

**Nathan Navidzadeh:** No, the background for the headers is gray for me, not white.

**Vivek Shankar:** Okay, maybe it's the font on my thing.

**Vivek Shankar:** Well, let me make the header black.

**Vivek Shankar:** Well, let me just make the header black because if it's messed up on mine, it'll be messed up on someone else's too.

**Vivek Shankar:** You don't think it's a cache issue?

**Vivek Shankar:** don't see how.

**Vivek Shankar:** mean, because the rest of it is fine.

**Nathan Navidzadeh:** That's true, yeah.

**Nathan Navidzadeh:** I don't know.

**Vivek Shankar:** But yeah, it's weird.

**Vivek Shankar:** I don't know.

**Vivek Shankar:** Here it is.

**Vivek Shankar:** The column label, is that what they're called?

**Vivek Shankar:** The column label.

**Vivek Shankar:** black.

**Vivek Shankar:** There's a gray background.

**Vivek Shankar:** Okay.

**Nathan Navidzadeh:** So, you know, you're saying, okay, let's, we're going to find a piece of code here that works, and then we'll give that to Suleiman?

**Vivek Shankar:** Well, let's see if this works first, and we'll take it one by one.

**Vivek Shankar:** What are you saving?

**Vivek Shankar:** Publish now.

**Vivek Shankar:** It's published.

**Vivek Shankar:** Okay, there we go.

**Vivek Shankar:** So, it's pretty clear on my thing.

**Vivek Shankar:** Okay, so we know that this works.

**Vivek Shankar:** Now, basically, this is our templated section over here.

**Vivek Shankar:** All this padding and all of this, all this is, because this is the one with the color code and all this, right?

**Vivek Shankar:** And then, yeah, basically everything.

**Vivek Shankar:** So, so, in our Google.

**Vivek Shankar:** Doc, let's open the Airtable.

**Vivek Shankar:** So in our Google Doc, which is here.

**Vivek Shankar:** So when we're generating the article, I think what we can do is, where is it?

**Vivek Shankar:** Oh, yeah, OK.

**Vivek Shankar:** I think we just give him the HTML, because I don't think he's going to have time to run the whatever.

**Vivek Shankar:** So we can say building blocks, core HTML, OK.

**Vivek Shankar:** And then I take my, what you call this?

**Vivek Shankar:** So obviously, this is going to be saved somewhere.

**Vivek Shankar:** OK.

**Vivek Shankar:** OK.

**Vivek Shankar:** OK.

**Vivek Shankar:** Thank

**Vivek Shankar:** So this initial part, I think I'd say we need to stay and save it.

**Vivek Shankar:** Everything under the style tag, right?

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** We just save all of this.

**Vivek Shankar:** And then we just change the title.

**Vivek Shankar:** And obviously we substitute stuff for the body.

**Vivek Shankar:** And we could just come into Claude, give it a table, right?

**Vivek Shankar:** And be like, okay, in this particular code, substitute table contents for whatever I'm pasting.

**Vivek Shankar:** So let's take another table, for example, and then we just paste it in here.

**Vivek Shankar:** Yeah.

**Nathan Navidzadeh:** So go, there's another table actually we're going to do in, if you go to Webflow, the agentic, the one right below it, agentic versus non-agentic.

**Nathan Navidzadeh:** This one also, I don't know if it has a date because it's not showing up on the blogs.

**Nathan Navidzadeh:** Do you know why that happens?

**Vivek Shankar:** Yeah, the date isn't fixed.

**Nathan Navidzadeh:** All

**Nathan Navidzadeh:** Right, so that's why it's not showing up, yeah.

**Vivek Shankar:** Yeah, that's why it's now.

**Vivek Shankar:** And, okay, so, well, let me go to the Google Doc, I think.

**Vivek Shankar:** This will be, that will have the actual table.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Let take, I'm in here, then I take this, and then I say, So I say, it will be included HTML below, substitute table contents with the content below.

**Vivek Shankar:** Yes, I am a master prompter, really.

**Vivek Shankar:** Anyway, so I take this.

**Vivek Shankar:** And then I say HTML and let's this.

**Vivek Shankar:** Let's see if this thing understands what I want.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Well, it's kept the title, which is understandable, but we don't have a title on our webflow, so that's fine.

**Vivek Shankar:** Seems to have substituted it.

**Vivek Shankar:** Let's take this.

**Vivek Shankar:** And then over here, I come in and I say code, code block HTML.

**Vivek Shankar:** I just paste it.

**Vivek Shankar:** Cool.

**Vivek Shankar:** And then I go into webflow.

**Vivek Shankar:** Let's see.

**Vivek Shankar:** Save and close.

**Vivek Shankar:** Publish now.

**Vivek Shankar:** I think it's published.

**Vivek Shankar:** Oh, man.

**Nathan Navidzadeh:** It saved this, but it's not done this.

**Nathan Navidzadeh:** Yeah.

**Nathan Navidzadeh:** See, is, oh, man.

**Nathan Navidzadeh:** But basically, I see what you're saying.

**Nathan Navidzadeh:** If I come up with a flow like that, then I'll just, I'll have to make it in.

**Nathan Navidzadeh:** Claude, and then try to find a way to do it quickly.

**Nathan Navidzadeh:** There was also this article that, oh, I sent it in the thread, that Nika had done before.

**Nathan Navidzadeh:** the ChatGPT versus Claude one, and he used HTML, and the HTML code in that one looked really good.

**Nathan Navidzadeh:** So I wonder if we can imitate that instead.

**Vivek Shankar:** Yeah, we just need to take one template and then get it.

**Vivek Shankar:** Sure.

**Vivek Shankar:** Thank

**Vivek Shankar:** Like, don't, I think it's a, yeah, I think it's a straightforward thing, but let's see.

**Nathan Navidzadeh:** Should be.

**Vivek Shankar:** Yeah, has it changed 09933, planning, hover.

**Vivek Shankar:** It's weird, man.

**Vivek Shankar:** I don't know.

**Vivek Shankar:** It added important?

**Vivek Shankar:** Is that even a thing?

**Nathan Navidzadeh:** Yeah, it is.

**Nathan Navidzadeh:** It overrides certain CSS rules.

**Nathan Navidzadeh:** So if there's already baked in CSS rules, then it has to put important in order for it to override.

**Nathan Navidzadeh:** For Webflow, you logged in using, was it pod A?

**Vivek Shankar:** It was Teams at Gmail.

**Vivek Shankar:** Okay, it works now.

**Vivek Shankar:** Yeah, it just needs some tweaking, but I would say this, yeah, I would say this is our template, and then I would, let me send this to you.

**Vivek Shankar:** Yeah, send that, please.

**Vivek Shankar:** So the cloud I've been using is pod A, so you should be able to see it.

**Vivek Shankar:** Okay.

**Vivek Shankar:** It's this chat.

**Vivek Shankar:** All right, let me send it to you.

**Vivek Shankar:** Where is it?

**Vivek Shankar:** Here.

**Vivek Shankar:** Here.

**Vivek Shankar:** What's that?

**Vivek Shankar:** There's some formatting issues, but yeah.

**Nathan Navidzadeh:** Okay, so for this one.

**Nathan Navidzadeh:** So this is just one that had a really nice...

**Nathan Navidzadeh:** Here.

**Nathan Navidzadeh:** Here.

**Nathan Navidzadeh:** Here.

**Nathan Navidzadeh:** If you scroll down.

**Nathan Navidzadeh:** Oh, yeah, this one.

**Vivek Shankar:** Yeah, I think there's some background  going on over here, clearly.

**Vivek Shankar:** But if we can grab that style, that would be nice.

**Vivek Shankar:** I think this is more of a global...

**Vivek Shankar:** I'm not using the right words here, but this design is very different from the rest of the site.

**Vivek Shankar:** Like, they have this lavender background.

**Nathan Navidzadeh:** Right.

**Vivek Shankar:** If I go here, it's just all black.

**Vivek Shankar:** Right, okay.

**Nathan Navidzadeh:** For some reason...

**Nathan Navidzadeh:** It was a special thing.

**Vivek Shankar:** Yeah, I don't know what's going on.

**Vivek Shankar:** This table looks pretty nice, and I think this is their internal template.

**Vivek Shankar:** Right.

**Vivek Shankar:** I don't think it's...

**Vivek Shankar:** Yeah, we didn't give this for sure.

**Nathan Navidzadeh:** Okay, okay.

**Vivek Shankar:** So, yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Yeah.

**Vivek Shankar:** Okay.

**Nathan Navidzadeh:** Okay, I think that, I mean, the other thing you mentioned was that Nika needs to list the actual metrics and benchmarks in his article.

**Vivek Shankar:** Yeah, because it's like, if it's LLM benchmarks or something, and I remember discussing this with him at some point.

**Vivek Shankar:** Maybe he just forgot.

**Nathan Navidzadeh:** Yeah, can you go over, because there are numbers in there, so I don't know if those specific ones that you were talking, I looked at it briefly, but if there's something you saw specifically, I just want to see exactly what you saw.

**Vivek Shankar:** Sure.

**Vivek Shankar:** can, yeah, do you me to share my screen?

**Nathan Navidzadeh:** No, no, I got it.

**Vivek Shankar:** So this one, when he's talking about five important metrics, right?

**Vivek Shankar:** Accuracy metrics, gen quality metrics, these are like metric groups.

**Vivek Shankar:** These are not metrics.

**Vivek Shankar:** By themselves.

**Vivek Shankar:** So blue, meteor, rouge, exact match, precision, recall, F1 score.

**Vivek Shankar:** These are actual metrics.

**Vivek Shankar:** And we need to have like, yeah, like five metric categories.

**Vivek Shankar:** This is not, it doesn't give me any information, right?

**Vivek Shankar:** I need actual metrics.

**Nathan Navidzadeh:** You want the numbers you mean?

**Nathan Navidzadeh:** Like you want the numbers?

**Vivek Shankar:** Not numbers, but metrics are like, in the context of LLM performance, metrics are basically like, you know, it's like saying, how do I measure a sofa?

**Vivek Shankar:** Okay, I measure the length, the breadth, and the width.

**Vivek Shankar:** That's what I need to know.

**Vivek Shankar:** And the height, right?

**Vivek Shankar:** So that's what this is.

**Vivek Shankar:** So I need to say length, I need to say breadth, I need to say width, and I need to describe what that is.

**Vivek Shankar:** So I need to describe what exact match is.

**Vivek Shankar:** I need to describe what precision is.

**Vivek Shankar:** Like this needs to be the list.

**Vivek Shankar:** It's not the group, which is accurate.

**Vivek Shankar:** Accuracy metrics or generation quality metrics.

**Nathan Navidzadeh:** Right, right, right.

**Nathan Navidzadeh:** Yeah.

**Vivek Shankar:** And I would make this 10.

**Vivek Shankar:** I mean, there's a lot of metrics.

**Vivek Shankar:** And it just needs to be bulleted.

**Vivek Shankar:** So bulleted, exact match, one sentence, that's it.

**Vivek Shankar:** Like bird score, mover score, these are like really easy to describe.

**Vivek Shankar:** So yeah, same for the benchmarks.

**Vivek Shankar:** Like, you know, Hella Swag and all of this and MMLU and all this, this needs to be individual bullets.

**Vivek Shankar:** So instead of having them grouped under these particular things.

**Nathan Navidzadeh:** I guess they could still be grouped, but then they could be separated out as individual bullets.

**Nathan Navidzadeh:** Because grouping them is, I mean, for me, I think it's nice to have groupings so that you know what kind of category the metric falls under other than just a big list of.

**Nathan Navidzadeh:** Yeah, sure.

**Vivek Shankar:** I mean, if, yeah, I don't see any issues with that.

**Vivek Shankar:** But definitely more of a description.

**Nathan Navidzadeh:** for like accuracy metrics.

**Nathan Navidzadeh:** It's exact match, like, you know, there needs to be a sentence saying what is exact match, what is precision, what is...

**Vivek Shankar:** Yeah, maybe you can have accuracy metrics.

**Vivek Shankar:** These answer one question, did the model get it right?

**Nathan Navidzadeh:** And then some bullet, exact match, precision, whatever.

**Nathan Navidzadeh:** So you can have it that way.

**Vivek Shankar:** The reason, again, is because all articles about LLM evaluation, they need to have this, like, for example, if you look at Galileo, you know, they have AI evaluations.

**Vivek Shankar:** It's not quite LLM, but, you know, they...

**Vivek Shankar:** Okay, this doesn't have it.

**Vivek Shankar:** I think it's in testing AI regions.

**Vivek Shankar:** Okay, it's not this either.

**Vivek Shankar:** Brilliant.

**Vivek Shankar:** LLM benchmarks.

**Vivek Shankar:** Yeah, this is just benchmarking, though, so you can see they have, like, actually broken out the name of the benchmarks for it.

**Vivek Shankar:** So you can see, like, they're actually discussing these, you know, in detail because that's their business.

**Vivek Shankar:** But this is kind of what I had in mind, like, it just needs to be bullets and actual mentioning them.

**Vivek Shankar:** Because if these are like H2s or H3s, that's pretty powerful because these themselves, people search for these things, you know.

**Vivek Shankar:** So that's like a good way of just tapping into that traffic.

**Nathan Navidzadeh:** Okay, so that might be a case to not have them in categories then, or?

**Vivek Shankar:** Yeah, I mean, yeah, like, just for, you know, if I'm thinking in terms of chunking information, if the section says five important metrics or ten important metrics.

**Vivek Shankar:** Yeah, and then it's categories.

**Vivek Shankar:** Yeah, it's going to expect the metrics themselves as opposed to categories.

**Vivek Shankar:** You can, if you want to have categories, you can have a table of these.

**Vivek Shankar:** You can say, like, yeah, accuracy metrics, example of what it does or what they do or whatever.

**Vivek Shankar:** You can have that.

**Vivek Shankar:** But I think definitely having some sort of a bullet list with each metric and describing what that metric is, I think that's pretty, yeah, important.

**Nathan Navidzadeh:** Yeah, I like that.

**Nathan Navidzadeh:** I like that.

**Nathan Navidzadeh:** Okay, I'll get on in for that.

**Nathan Navidzadeh:** And then the last thing I wanted to talk about is, oh, yeah, so the out-of-office stuff.

**Nathan Navidzadeh:** So where do I stand for that?

**Nathan Navidzadeh:** Do I, am I allowed to take time for doing the quiet week?

**Nathan Navidzadeh:** Is it different for me because I'm new?

**Nathan Navidzadeh:** Do you know anything about that?

**Vivek Shankar:** Yeah, one second.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Okay.

**Vivek Shankar:** Thank
