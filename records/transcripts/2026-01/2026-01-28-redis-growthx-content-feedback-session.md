# Redis <> GrowthX | Content Feedback Session

<metadata>
date: 2026-01-28
time: 19:30 UTC
duration: 31 minutes
enriched_on: 2026-02-28 15:30 UTC
organizer: Erik O'Brien (GrowthX)
source: fathom
fathom_recording_id: 117943181
fathom_url: https://fathom.video/calls/546444702
share_url: https://fathom.video/share/352dPqRL6HyLmjbTCHUCjR86ymcwyyXt

## Participants

| Name | Role | Affiliation | Email |
|------|------|-----------|-------|
| Erik O'Brien | Engagement Manager | GrowthX | erik@growthx.ai |
| Gabrielle Brogan | Managing Editor | GrowthX | gabrielle@growthx.ai |
| Fung-Lin Wu | Product Manager | Redis | funglin.wu@redis.com |
| Jim Tessier | Senior Competitive Intelligence Manager | Redis | jim.tessier@redis.com |
| Jim Allen Wallace | Senior Product Marketing Manager, AI | Redis | jim.allenwallace@redis.com |
| Fionce Siow | Product Manager, Community & Ecosystem | Redis | fionce.siow@redis.com |
| Alexis Ruiz | Product Manager | Redis | alexis.ruiz@redis.com |
| Allison Gregory | — | Redis | allison.gregory@redis.com |
| John Noonan | — | Redis | john.noonan@redis.com |
| Talon Miller | — | Redis | talon.miller@redis.com |
</metadata>

---

## Summary

Redis and GrowthX reviewed content quality and pipeline accuracy for AI-generated articles. The session focused on three key issues: articles missing Redis's unique value proposition in vector databases, the need for more granular audience personas and reference documents to improve content accuracy, and implementation of an automated review workflow triggered at 150 page views to scale publishing while maintaining quality.

---

## Context

GrowthX partners with Redis on B2B content marketing at scale, using AI pipelines to generate articles on vector databases, key-value systems, and semantic caching. The partnership aims to improve SEO and AEO visibility while maintaining technical accuracy and brand voice.

During this session, Redis stakeholders provided critical feedback on content that had drifted from Redis's competitive positioning and contained inaccurate citations. The feedback surfaces a core tension in scaling: AI pipelines produce content quickly, but without precise inputs (reference docs, detailed personas) and rigorous post-processing, they generate articles that miss the mark for enterprise audiences and erode credibility through overstatement of sources.

---

## Relevance

**For GrowthX (Internal):**
- Pipeline quality depends on upstream inputs—reference docs, personas, tone/voice artifacts.
- Post-processing workflows (fact-checking, technical review) must catch errors before publishing.
- Automation via PMM review thresholds (150 page views) scales publishing without overloading Redis stakeholders.

**For Redis:**
- Content directly impacts buyer perception; misalignment on value prop and overstatement undermine trust.
- Detailed personas (e.g., MLOps Engineer, solution architect) are essential for framing content correctly.
- Enterprise campaign materials require nuanced positioning around trade-offs and concerns.

**For Both:**
- Governance model: GrowthX authors articles, Redis reviews on-demand via triggered workflows, not blanket approval.
- Iteration: Build feedback loops to refine pipeline inputs continuously.

---

## Overview

**Content Quality Issues**

- **"Choosing a Vector Database" article:** Missed the core Redis narrative—the "best of both worlds" positioning (performance + accuracy of purpose-built DBs, familiarity of platform DBs). Failed to hook enterprise architects and IT decision-makers who need to weigh trade-offs.
- **"What is Key Value Databases?" article:** Citations were imprecise. Sources were cited for inferences or broad claims (e.g., citing AWS latency under specific parameters as universal truth) rather than their exact findings. This overstates claims and erodes credibility.

**Pipeline Input Gaps**

- **Reference documents:** Pipeline pulls generic sources, not Redis-specific material. Need audit of current source list and Redis suggestions for better alternatives.
- **Audience personas:** Current personas (Full-stack dev, VP of Engineering, CTO) are too high-level. Require nuanced personas (MLOps Engineer, solution architect) that capture specific trade-offs and motivations.

**Workflow Solution**

- **Publish with GrowthX authorship** to scale output.
- **Trigger PMM review at 150 page views** to focus review effort on high-performing content.
- **Phased rollout:** Activate workflow per PMM topic cluster as confidence grows.

---

## Key Topics

### Problem: Content Misses the Mark

**"Choosing a Vector Database" Article**

- **Audience Mismatch:** Content failed to hook enterprise architects, systems architects, and IT decision-makers. Lacked clarity on what these personas care about when selecting a vector DB for an AI stack.
- **Value Prop Gap:** Article presented a simple comparison (purpose-built vs. platform DBs) without Redis's nuanced position: "best of both worlds"—performance and accuracy (like purpose-built DBs) plus familiarity and no new technology overhead (like platform DBs).
- **Root Cause:** Pipeline did not pull the right source documents or apply the Redis competitive lens when building the article.

**"What is Key Value Databases?" Article**

- **Inaccurate Citations:** Article cited sources but did not accurately reflect them. Examples:
  - Used inferences from a source (A + B = C) without explicit support.
  - Cited AWS latency under very specific parameters as a universal truth.
- **Impact:** Overstating sources damages credibility. Readers who check sources find the article's claims don't hold.
- **Fix:** Be more precise. Use phrases like "one of the problems" or "many people face" instead of universal claims like "everyone experiences" or "all architects see."

### Solution: Improve AI Pipeline Inputs

**Reference Documents**

- Pipeline must ingest specific, up-to-date source materials that are factually accurate.
- GrowthX will share the current source document list used by the pipeline; Redis will audit and suggest better alternatives.
- Jim Tessier to identify which documents were actually used in "Choosing a Vector Database" so both teams understand what was pulled.

**Audience Personas**

- Current personas are too broad. Pipeline needs granular personas: MLOps Engineer, solution architect, backend engineer specializing in retrieval-augmented generation (RAG), etc.
- Each persona should map to specific concerns, trade-offs, and decision criteria.
- Jim Allen Wallace will share Redis's persona docs (including Fionce's enterprise campaign mapping) with GrowthX for audit and integration.
- Fung-Lin to verify persona docs are included in onboarding materials and add any that are missing.

**Citation Accuracy**

- Sources must be cited for their exact findings, not for inferences or broad applications.
- Post-processing workflow must include fact-checking (ChatGPT, Claude, Perplexity) to catch overstatement before publishing.

### New Workflow: Automate & Scale Reviews

**Publishing Model**

- Articles publish with GrowthX authorship (not Redis) to scale output and reduce individual PMM review burden.
- Goal: Shift from blanket pre-publication review to triggered, on-demand review.

**Triggered Review Threshold**

- When an article reaches 150 page views, a PMM review is automatically triggered.
- Review focuses on accuracy, tone, and opportunities for enrichment (e.g., additional imagery, diagrams).

**Phased Rollout**

- Each PMM cohort (topic cluster) rolls into the new workflow as they become comfortable with GrowthX quality.
- Fung-Lin to check in with Jim Allen Wallace and John Noonan on comfort level; if both align, their topic clusters can begin free-publishing.
- Weekly check-ins with Redis PMMs to track progress.

---

## Action Items

**Erik O'Brien (GrowthX)**
- Share vector-DB article source list with Jim Tessier and Jim Allen Wallace; identify which documents were actually used in "Choosing a Vector Database" article to enable better feedback on source selection.
- Update pipeline post-processing to improve citation accuracy; eliminate overstatement and absolutist language ("one of the problems" vs. "all architects face").

**Jim Allen Wallace (Redis)**
- Send persona docs to Erik and Gabrielle; docs should include enterprise campaign mapping. GrowthX will audit and integrate into pipeline artifacts.
- Grant team@growthxlabs.com view/comment access to newly added onboarding docs on persona materials.

**Fung-Lin Wu (Redis)**
- Verify all persona docs are included in onboarding materials; identify and add any missing docs.
- Add enterprise persona mapping link to onboarding doc comments and tag Erik and Gabrielle for visibility.
- Check in with John Noonan on comfort level with GrowthX authorship model; align with Jim Allen Wallace on when their topic clusters can begin free-publishing.

---

## Transcript

**Erik O'Brien:** Hey, how's going?

**Erik O'Brien:** Good.

**Gabrielle Brogan:** Yes.

**Erik O'Brien:** Hey, Alexis.

**Alexis Ruiz:** Hey, how are you all?

**Erik O'Brien:** Doing well.

**Erik O'Brien:** How's your week going so far?

**Alexis Ruiz:** Oh, it's going good.

**Alexis Ruiz:** How about yours?

**Erik O'Brien:** Busy, but not bad.

**Fung-Lin Wu:** Hi.

**Erik O'Brien:** Hey, Fung-Lin.

**Fung-Lin Wu:** How are you guys?

**Erik O'Brien:** Good.

**Fung-Lin Wu:** It looks like Jim Tessier's here.

**Fung-Lin Wu:** Great.

**Fung-Lin Wu:** Jim, welcome.

**Jim Tessier:** Hey.

**Jim Tessier:** What's up?

**Erik O'Brien:** Hey, Jim.

**Erik O'Brien:** Nice to meet you.

**Jim Tessier:** Hi, you too.

**Jim Allen Wallace:** Hello.

**Erik O'Brien:** Good to put a face to the name.

**Erik O'Brien:** Hey, Jim.

**Erik O'Brien:** Number two.

**Jim Allen Wallace:** Yes.

**Erik O'Brien:** Or number one.

**Jim Tessier:** We call him JAWS.

**Fung-Lin Wu:** Yeah, we call him JAWS.

**Fung-Lin Wu:** There's too many Jims, and Jim Tessier joined first.

**Jim Tessier:** I was here first.

**Alexis Ruiz:** This meeting is being recorded.

**Jim Tessier:** Also, JIVIT isn't really a cool acronym.

**Jim Allen Wallace:** Jim stands for something.

**Fung-Lin Wu:** Yeah, JAWS works. Were you called JAWS at other companies or no?

**Jim Allen Wallace:** No, only because there are multiple Jims here.

**Fung-Lin Wu:** Our old CMO's name was Keith. When another Keith joined, he had to be called by his last name.

**Alexis Ruiz:** Yeah.

**Alexis Ruiz:** And he actually hated it.

**Alexis Ruiz:** So now he's back to being Keith.

**Alexis Ruiz:** It was so hard to switch from calling him by his last name to Keith again.

**Fung-Lin Wu:** It's okay.

**Fung-Lin Wu:** I still call him by a different name.

**Fung-Lin Wu:** Alright, I think we have everyone here now, Erik.

**Fung-Lin Wu:** So it might be helpful if Jim, JAWS, and Fionce give you guys a quick intro.

**Fung-Lin Wu:** I know John and Talon couldn't make it.

**Erik O'Brien:** Sure thing.

**Fung-Lin Wu:** Anyone want to start?

**Jim Allen Wallace:** Jim?

**Jim Allen Wallace:** You want to go?

**Jim Tessier:** The first Jim.

**Jim Tessier:** Oh, sure.

**Jim Tessier:** So I'm Jim Tessier.

**Jim Tessier:** My focus is competitive intelligence.

**Jim Tessier:** Some of the GrowthX blogs have fallen to me. Think of anything like Redisverse, ElastiCache, or more of the landscape stuff. Like the "Choosing a Vector Database" article—competitive elements like market positioning, cloud partners, that type of thing falls to me.

**Erik O'Brien:** Gotcha.

**Jim Allen Wallace:** Yeah, that's Jim Tessier, or JAWS.

**Jim Allen Wallace:** I do product marketing for AI.

**Jim Allen Wallace:** Vector stuff, LOMs, context engine, context engineering, feature stores—anything in that space, I'm your guy.

**Erik O'Brien:** Right.

**Fionce Siow:** I'm not a Jim, but you can call me Redis Insight Jim if you'd like.

**Fionce Siow:** I'm in charge of our products that are technically free to the Redis community but are ways to upsell and get folks down the funnel to convert them to paying Redis users. That's Redis Insight, which is our free developer tool, clients—the way users interact with Redis or get data from it—and our ecosystem partnerships. I'm mostly looking at articles broadly, so that's where I usually interact with GrowthX.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** And just as a quick intro, I'm Erik O'Brien, the engagement manager, handling all the day-to-day stuff with our partnership with Redis. I've also got here with me Gabby, who is our managing editor and creates most of the content for you.

**Gabrielle Brogan:** Yeah.

**Gabrielle Brogan:** Hi, I'm Gabby.

**Gabrielle Brogan:** I'm a managing editor, so I'm building content.

**Gabrielle Brogan:** It's great to meet you all.

**Gabrielle Brogan:** And like Erik said, great to put faces to names.

**Jim Tessier:** Yeah.

**Jim Tessier:** You're breaking up a little.

**Fung-Lin Wu:** The audio was a little spotty.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** So we do have at least one article from each of you and would love to have you guys talk us through qualitatively what you're seeing that's missing the mark at the top level. Anything nuanced about brand mentions that may be off. I think the goal for us is to refine these AI pipeline artifacts. We have engineers working on the pipeline, so we'll continue to refine the AI portions. But for the most part, Gabby and I can control some of the inputs. Hearing from you guys directly on these articles would be fantastic—qualitative feedback and thoughts.

**Erik O'Brien:** I think this one goes to Jim.

**Jim Allen Wallace:** Yep, that'd be me.

**Erik O'Brien:** Number two, AI Jim.

**Jim Tessier:** I think this was mine, actually.

**Jim Allen Wallace:** I think you did look at it, Jim.

**Jim Allen Wallace:** Yeah, I also looked at it after you.

**Jim Tessier:** Yeah. So I added a lot of comments on this one. Overall, I think what was missing was the audience. I know these are mostly for SEO and AEO, but from the very beginning, it kind of missed the hook for enterprise architect, systems architect, IT decision maker. What they care about when choosing the best vector database for your AI stack. And then the second key thing was it missed the context of Redis. Here, if you want to skip down to "How to Evaluate"—it read like a comparison between custom-built vector databases and existing databases that have added vector search, which is a high-level way to think of it. But the way we fit into that is we get the best of both worlds. It didn't really convey where our value proposition is. I have this in the competitive landscape. I want to understand why that didn't translate to this doc. But basically, the idea is: custom or purpose-built vector databases are fast, accurate, configurable, tunable. The platform approach is lagging—offers basic vector search but you don't have to bring in new technology or learn anything new. Our value prop with Redis is that you already have Redis, so you don't have to worry about learning something new, but it's also very performant, very accurate. Maybe we're not quite as advanced as purpose-built vector databases, but you get basically everything you need to build an application. That nuance was missed. It took a basic look at the market without the Redis lens. So it didn't get that part right.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** That's helpful.

**Jim Allen Wallace:** I have a question for you.

**Jim Allen Wallace:** Like, what's the best way to add feedback? There's specific things here—comments, right? But it sounds like for your pipeline and artifacts, like, do you have a style guide? The main feedback I have is certain specific parts aren't super accurate, which is always the problem with LLMs. Do you have inputs and documents and evaluation? Like, what's the best way to get feedback? I can give you six examples, but if you're looking for an algorithm or a guide or rules that are always true, is that the type of thing you're looking for to make these pipelines more accurate?

**Erik O'Brien:** Yeah, I would say any of those are helpful. We can point the pipelines to certain reference documentation. If there's an easier way for you to give feedback like "check these docs" and then rerun the article to base it in these factual documents, that helps. There's definitely about four or five artifacts we have. One is brand context. The other is tone of voice, which we spent a lot of time on with Allison early in the engagement. Others are products and services—trying to get a full product feature matrix with correct terminology. I will say that's part of the engineering effort right now: checking if the pipeline is pulling those reference documents at appropriate times and if there's convolution between instructions in one place and another. But yeah, if there's specific reference documentation that you think would be helpful for us to ingest or point the models toward, we'd take those very happily.

**Jim Tessier:** Yeah, I think that's probably the key. For this one, it didn't seem to take the right source documents to build around. If we had some look into what documents it was pulling, we could help you understand which documents it should have pulled.

**Erik O'Brien:** Gotcha.

**Erik O'Brien:** Yeah, we can go back and see if we can find that resource list that it was pulling and share that with you guys.

**Jim Allen Wallace:** On my end, connected to this, one of the things is the personas and their perspective. Jim had some comments on the trade-offs that an MLOps engineer makes, what choices they're weighing, and framing it in a way that makes sense. Some of the trade-offs described seem off the mark. If that's your role and your audience, and this doesn't make sense to them—we do have a doc on personas that could help. But some of these trade-offs in the new AI space just aren't well-documented yet. There are articles out there, and if you scrape them, you might have something, but you're not going to find a lot of resources on these types of trade-offs and best practices. But we can give you what we have.

**Erik O'Brien:** Yeah, I think that'd be helpful for us to do an audit. We do have audience personas as an artifact, and we've got a few different ones. They seem probably high-level compared to what you have. We have full-stack devs, VP of Engineering and Technology Leadership, CTOs and Engineering Directors. Yeah, some of those more nuanced personas you may have, I think we can enrich ours and get deeper into their actual concerns, motivations, how we win their trust.

**Jim Allen Wallace:** Yeah, I can't say I love our persona decks either. They don't have all the detail you'd be looking for, but they'll give you something to work with and help if that's a prioritized input.

**Erik O'Brien:** And I'm not sure, Fung-Lin, if that was on our original list, but I can check if we have those.

**Fung-Lin Wu:** Yeah, I'm double-checking all the onboarding docs we included for personas. I don't know if that was included. We only included the ICP analysis and some materials from Jim Tessier, JAWS, and Fionce that we worked on with Ryan, because I don't know if we have any other documented ones.

**Fionce Siow:** Which ones that we worked on with Ryan?

**Fung-Lin Wu:** Yeah, it might have been before Fionce's time.

**Jim Tessier:** ICP meaning ideal customer profile.

**Fung-Lin Wu:** Yes.

**Fung-Lin Wu:** You guys did a comprehensive ICP analysis with Ryan Powers and Charlie.

**Jim Tessier:** But I think that was only... Yeah, but we're doing that as our target, but we want the person, the persona. Like the type of person we're targeting, not the customer or company.

**Fung-Lin Wu:** But if you want, we also sent resources like the AI playbook. I can put this in the chat—all the resources we sent over to GrowthX. If you want to take a second look and add on, Jim, you had added a bunch related to competitive stuff.

**Fionce Siow:** I created an enterprise campaign persona mapping. Remember, Fung-Lin? Maybe that would be helpful because it's from the perspective of the solution architect or how they think, what they care about.

**Fung-Lin Wu:** Do you have the link to that?

**Fung-Lin Wu:** If you have it, feel free to add it in the comments here in the Customer Insights section. Then I can make a comment to Erik and Gabby about this being a new one we've added.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Knowing we've only got 13 more minutes here, Gabby, do you want to talk to this refreshed one a bit—what we've seen in the newer one?

**Gabrielle Brogan:** Yeah, sure.

**Gabrielle Brogan:** So with the refresh logs, we're taking existing articles and updating them to increase effectiveness. In the areas where there's a green highlight in the background and I've highlighted it with a comment, that's net new or adapted content. I can see some comments there around accuracy and perspective. We also have some original content that was on the website, and I see some comments around accuracy there too. I'd love some insight into a baseline here—what we can be aiming for in terms of accuracy.

**Erik O'Brien:** Yeah, I think the short version is some of this was written by some of your solution engineers or PMM teams. Some of the comments we've gotten are accuracy errors in what they had written. We're trying to better understand, at a higher level, what's the most appropriate way to take feedback on previous written content from Redis.

**Jim Allen Wallace:** Do you have an example?

**Jim Tessier:** From a high level, vector databases are evolving a lot faster than most of the rest of our core business. So what we might have thought a year ago could certainly be very different today.

**Erik O'Brien:** That makes sense.

**Erik O'Brien:** So we'll take AI Jim's feedback as the most accurate, up-to-date reference.

**Jim Allen Wallace:** I mean, voice of truth here and happy to help. But yeah, I think the goal is to get to a point where things don't need reviewing, right? I think you can get feedback from a number of people. If I look at it, I'll give feedback. But some things are wrong, and a lot of things could just be unclear, too.

**Jim Tessier:** One thing I did was put it into ChatGPT and asked it to review it for a technical audience and gave it three personas to look at it through. Then asked for the plain review and see what it says. You could ask it for three things to fix. That was probably like 90% of the way there, whereas what I originally got was maybe only 50% of the way there.

**Erik O'Brien:** Yeah, we did get that feedback. Since then, that's what triggered the larger engineering review of the pipeline for technical accuracy. Ideally, we'd be able to do those reviews for accuracy within our pipelines. We have a researcher step and a fact-checking step. So some of those were concerns on our end too—if these aren't being caught during those critical steps, what else might be having an issue? We've definitely taken that feedback and done some post-processing as we wait for the engineers. I think hopefully going forward, the reviews will include comments because we have at least Perplexity, Claude, and ChatGPT all checking for factual errors.

**Jim Tessier:** Yeah, and we mostly use ChatGPT because we have the license, but I've also found that Claude is the most technically accurate. But again, a lot of these things move really fast, so you have to make sure it's using right now, not cached data.

**Erik O'Brien:** Trained, yeah.

**Erik O'Brien:** Absolutely.

**Fionce Siow:** Something I'll add regarding technical accuracy: I just reviewed a new article, "What is Key Value Databases?" It was definitely an improvement from the very first one I reviewed. The only nitpick I'd have is that I appreciate there were cited sources, but when I went to check them, the content seemed to overstate or didn't accurately cite them. For example, there was one where they cited a source using an inference—A plus B equals C—but that inference wasn't explicitly stated in the source. And there was another where they cited AWS latency, but that was within very specific parameters yet was being applied broadly. Very small nuances, but to have credibility, we need to be very specific in how and why we cite certain things.

**Erik O'Brien:** Does that make sense?

**Erik O'Brien:** Yes, absolutely.

**Erik O'Brien:** And I think that's, correct me if I'm wrong, something we were fixing in a different pipeline as well. It's either overstating or understating the source content. We've been able to fix that for a couple others, so we'll definitely take that back and make sure our team looks at how we can optimize for accuracy and citing relevant sources. I think that's another thing we can start to point to sources that are more accurate and more appropriate for this type of content development.

**Fionce Siow:** It was machine learning inferences and cost of performance.

**Erik O'Brien:** Sorry, not this one.

**Jim Tessier:** Yeah, and I think one big takeaway from there is we talked about universal claims being a stretch. But I think you can get away with more if you just don't make it universal. Like, here's one of the problems. Even if nobody is actually running into that problem, they can read that and say "oh, that's not a problem I'm having." It doesn't hurt credibility. Whereas if we say "the problem is this" and everyone's like "no, that's not my problem," we hurt credibility.

**Erik O'Brien:** Yep.

**Erik O'Brien:** I think we've tried to make some changes to the artifacts and post-processing that we use in the pipeline to reduce or eliminate absolutist language, especially in conversational pieces. Like "when you're an architect and you run into this problem" instead of "every architect runs into this problem on a day-to-day basis," which just isn't true.

**Erik O'Brien:** So I think, Gabby and correct me again, but we've at least updated the artifacts to reduce some of those previous issues.

**Fionce Siow:** I think what Jim is saying here is we could even add a bit more back in to still have some bolder claims while still being accurate. Like "one of the problems is" or "many people face" instead of what it was before, which I think was "all" or "most," which is still overstating. So it's just finding that balance so we can still have a voice in these articles.

**Erik O'Brien:** Super helpful.

**Erik O'Brien:** And then this is the last article. "What is Semantic Caching?" I guess we can focus on this one, or if there are other larger comments you guys have, I'd definitely welcome them in the next few minutes we have left. Talon's not here, but if there are larger comments or other additional feedback, we're open to it.

**Jim Allen Wallace:** One thing that we talked about is, in my view, we only have to look at things after they've reached a certain threshold. I don't know if there's a decision on what that threshold is and how we'll get alerts, but if things aren't getting views, then I'm not too worried about it.

**Erik O'Brien:** Yeah, and that's something we could definitely incorporate into the review cycle. If an article passes, you know, 100 views, then it gets triggered for a deeper review, just to check for any accuracy or tonal changes. Or just enriching it with additional imagery and diagrams is another thing we do with other clients. We're definitely open to that once we get to a point where we feel comfortable publishing straight away and having that be our trigger for additional reviews.

**Fung-Lin Wu:** Alexis and I also mentioned that once all the PMMs are comfortable with launching via the blog with your authorship, we will also do a due diligence of checking weekly. But if GrowthX can do it even better, where once it hits 100 page views—we were looking at our benchmark, and it looks like it's 150 page views—we have a PMM take a look.

**Alexis Ruiz:** Yeah, I think it was 150, online.

**Alexis Ruiz:** 150, sorry.

**Fung-Lin Wu:** Yeah. But I think it's just that we need PMMs to be comfortable signing off. I think, Josh, you're almost getting there. So it's just Jim, Fionce, and John. I'll check in with John later. And actually, I think if JAWS is comfortable, we can chat separately offline. I know we're at time, but maybe as each of you becomes comfortable, then your cohort of topic clusters can just kind of go free first.

**Jim Allen Wallace:** That worked for me.

**Fung-Lin Wu:** Yeah. Eric, I set up another meeting with the PMMs, I think next week, for us to just check back in. I'll let the GrowthX team know.

**Erik O'Brien:** Okay.

**Erik O'Brien:** Yeah.

**Erik O'Brien:** Sounds wonderful.

**Erik O'Brien:** Well, this has been incredibly helpful. I really appreciate everybody taking the time out of their busy days to give us this feedback and help make this program better. I think the new personas will be a great addition to overall voice and tone, making sure we're hitting the audience with the right notes. And then for the technical issues we're experiencing, our team is working through that ticket and hopefully will have it resolved soon. So Gabby can have a little bit of time back and not have to send every article through ChatGPT, Perplexity, and Claude. But as we continue to push out new content, we still welcome all and any feedback, as direct as possible, so we can continue to make these pipelines better.

**Fung-Lin Wu:** Yeah. One last thing.

**Fung-Lin Wu:** Fionce and JAWS, the two of you are...

**Fung-Lin Wu:** There are new docs that I just added to the onboarding doc for GrowthX. Erik, I tagged you in both. JAWS and Fionce, I think you guys own the two that you added. I just need to see—can you guys make sure team@growthxlabs.com has access to at least view or comment?

**Fionce Siow:** Yeah, anyone with the link should be able to view the one I posted.

**Fung-Lin Wu:** Okay.

**Erik O'Brien:** Looks like I can access that one.

**Fung-Lin Wu:** Okay.

**Fung-Lin Wu:** Okay, I think you're good.

**Fung-Lin Wu:** That's it then.

**Erik O'Brien:** Wonderful.

**Erik O'Brien:** Well, again, appreciate everyone's time and your continued collaboration as we push out this program. We'll keep at it. And again, appreciate the time.

**Jim Tessier:** Talk to you guys later.

**Jim Tessier:** Yeah, you too.

**Jim Tessier:** And just ping the team if you have any questions that come up. Happy to help.

**Erik O'Brien:** Absolutely.

**Jim Tessier:** Will do.

**Fung-Lin Wu:** Thank you.

**Jim Tessier:** Thank you.

**Gabrielle Brogan:** Thank you.

---

## Related Files

- Source recordings: https://fathom.video/calls/546444702
- Shared recording: https://fathom.video/share/352dPqRL6HyLmjbTCHUCjR86ymcwyyXt
