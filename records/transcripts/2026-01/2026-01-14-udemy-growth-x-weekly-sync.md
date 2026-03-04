# Udemy <> Growth X - Weekly Sync

<metadata>
date: 2026-01-14
time: 16:59 UTC
duration: 22 minutes
organizer: team@growthxlabs.com
participants: Katya Luscomb (GrowthX), Justin Luebke (Udemy), Jay Perlman (Udemy), Krista Chism (Udemy), Jennifer Shepherd (Udemy)
fathom_recording_id: 114243546
fathom_url: https://fathom.video/calls/530450887
share_url: https://fathom.video/share/i-DLnAzKCH5Akv34mCJNs6dcQgK5WFuC
source: fathom
enriched_on: 2026-02-28 15:40 UTC
</metadata>

---

## Summary

Weekly sync between GrowthX and Udemy focused on content quality improvements and strategic initiatives. Key issues: GA4 access is blocked by a Data Processing Agreement, preventing data-driven optimization. Leadership Pillar Page review strategy clarified—Udemy will handle final SEO while retaining style/tone guidance from Heather (internal product person). Content feedback emphasizes casuality, readability, unique intent, and varied internal linking. Future work includes automating AI Overview (AIO) content summaries and exploring in-article UI elements for Blog V2. Udemy blog launched successfully; next content batch due end of week.

---

## Context

GrowthX and Udemy are executing a B2B content marketing engagement focused on AI in leadership development and change management. Udemy's blog launched in early 2026 with content from GrowthX. The engagement centers on collaborative content refinement, workflow optimization, and technical capability building (analytics, automation, UI enhancements). Previously, DPA/GA4 access was identified as critical blocker; discussions have progressed on workarounds. Katya Luscomb leads for GrowthX; Justin Luebke and Jay Perlman represent Udemy product/editorial. Jennifer Shepherd (Udemy) mentioned but not actively speaking. This is a standing weekly sync; this session occurs after launch with focus on post-launch optimization.

---

## Relevance

This sync directly impacts GrowthX's content delivery pipeline and Udemy's SEO strategy. Decisions made here (e.g., secondary keyword handling, external linking standards, AIO automation) will be operationalized across future content batches. Leadership Pillar Page clarity prevents rework; internal vs. external optimization split decision is critical to workflow. Analytics blocker (GA4/DPA) affects both teams' ability to measure impact. Blog V2 roadmap (homepage V2 then article-level UI) shapes technical requirements GrowthX must support. These discussions are also input for GrowthX's new LLM tracking tool and content OS visibility system—both strategic bets.

---

## Overview

- **GA4 Access Blocked:** A Data Processing Agreement (DPA) is blocking GA4 access, which is critical for moving from instinct-based content decisions to data-driven optimization.
- **Content Direction Shift:** Content must become more casual, focus on business impact, and improve readability by breaking up dense paragraphs and varying anchor text.
- **New Content Summary Process:** Udemy's manual process of incorporating Google's AI Overviews into summaries will be automated to improve ranking potential.
- **Leadership Pillar Page:** A new draft by a product person is approved for style and tone, but Udemy will handle the final SEO optimization internally.

---

## Key Topics

### GA4 Access & Data Strategy

  - GA4 access is blocked by a Data Processing Agreement (DPA).
  - **Impact:** This prevents data-driven optimization, forcing content decisions to rely on instinct.
  - **Status:** GrowthX is assessing technical feasibility; progress is expected.
  - GrowthX will hold off on sharing Looker setup notes for one week to see if the DPA resolves.

### Content Feedback & Refinement

  - **Overall Tone:** Shift from dense to more casual and readable.
  - **Focus:** Emphasize business impact and outcomes, especially in conclusions.
  - **Readability:** Break up long sentences and dense paragraphs for better flow.
  - **Repetition:** Ensure each article has a unique intent and avoids content overlap.
  - **Internal Linking:** Vary anchor text (e.g., not just "change management") to improve SEO value.
  - **External Linking:** Include relevant external links in all articles.

### Process & Workflow Updates

  - **Content OS Clarity:** GrowthX will implement a new system to track the status of \~15 articles in review, replacing long Slack updates.
  - **Leadership Pillar Page:**
      - A new draft ("Heather's version") is approved for style and tone.
      - **Rationale:** The author is a strong writer but not an SEO expert.
      - Udemy will handle the final SEO optimization internally.
      - GrowthX will inform Simran to pause work on this page.
  - **Secondary Keywords:**
      - **Current Process:** Used for research and outline generation, not explicit section titles.
      - **Decision:** Continue the current process to avoid an overly "SEO-heavy" feel.

### Future Initiatives

  - **Automated Content Summaries:**
      - **Udemy's Manual Process:** Create a 50-word summary using ChatGPT, incorporating bolded text from Google's AI Overviews (AIOs) to improve ranking potential.
      - **GrowthX Action:** Investigate automating this process. If full automation is not feasible, GrowthX will manually add the AIO text as an input to its pipeline.
  - **Blog V2 & On-Page Elements:**
      - **Udemy Plan:** After homepage additions (resource/case study tiles), the team will add in-article elements like related blog cards.
      - **GrowthX Action:** Will incorporate any required HTML/tags into its pipeline once V2 launches.
  - **GrowthX LLM Tracking Tool:**
      - GrowthX is building an internal LLM tracking tool (similar to Scrunch/Profound).
      - **Key Feature:** Analyzes prompts from established industry leaders, providing deeper insights into citations and authority than tools requiring user-defined prompts.

---

## Action Items

**Katya Luscomb (GrowthX)**
- Prep Looker setup notes for Justin/Jay by EOW; withhold sending for 1 week pending DPA resolution
- Send Content OS clarity notes to Justin/Jay by EOW (addresses ~15 articles in review tracking)
- Notify Simran (GrowthX) to pause work on Leadership Development pillar page; Udemy will handle final SEO internally
- Update content pipeline prompts to ensure: varied anchor link text, external links in all articles, secondary keywords deeply integrated, reduced content overlap, longer sentences/paragraphs broken up
- Audit the model for secondary keyword usage; adjust if it has begun straying from intent-based incorporation toward explicit section titling
- Consult engineering team on feasibility of automating AIO (Google AI Overview) text incorporation into content summaries; report feasibility assessment to Justin/Jay
- Send next content batch end of day today or tomorrow morning; request feedback by Thursday midday

**Justin Luebke (Udemy)**
- Explore in-article UI options for Blog V2: sidebar elements, callouts, related blog cards
- Share sidebar/callout design recommendations and constraints with Katya

---

## Transcript

**Katya Luscomb:** Hi, hi. Sorry.

**Justin Luebke:** Too many screens open.

**Katya Luscomb:** Oh, you're good. How's it going? How's your day?

**Justin Luebke:** Pretty good.

**Katya Luscomb:** Jay joining us today?

**Justin Luebke:** Yeah, he said he was going to be a few minutes late, though.

**Katya Luscomb:** Okay, no stress. Pretty quick meeting since we just connected last week.

**Katya Luscomb:** I know you sent me the update on the DPA for GA4. I saw some chatter about it in my team space as well. On all sides, we're working on getting that through.

**Justin Luebke:** Okay. How are they feeling about it?

**Katya Luscomb:** I think they're feeling okay about it. There's a couple of things we're working through to make sure of feasibility, but it seems like we'll be able to do it. So it's quite general, but that's the vibe I'm getting right now.

**Justin Luebke:** Yeah. I opened the document because I was CC'd and I was like, I don't know what any of this even means.

**Katya Luscomb:** Yeah, I know there's some technicalities—making sure we can give you guys updates when there are certain changes in our systems and getting all that through. So with that context, last week we had talked about me sending over some notes on how we have Looker set up. Are you feeling like you still want to look into trying to do that with the recent progress?

**Justin Luebke:** Let's maybe give it another week or so, and then just go from there.

**Katya Luscomb:** Okay, cool. I'll have it prepped by the end of this week and then we'll see what's moving.

**Katya Luscomb:** When it comes to our content OS, I'm going to play with a couple of ideas to bring clarity. There's a point in the week when we basically have 15 articles in review with you guys, and I want to make sure it's clear where each piece is at. I've got some ideas on how to more effectively implement that and I can send notes over by the end of this week. I know I sent a couple of long updates in our Slack channel, but I want to replace those with something clearer.

**Justin Luebke:** Yeah, I have been going through and doing the published updates, but I have a hard time remembering to hit "revisions needed," which I know is even more important.

**Katya Luscomb:** We can see the revisions come through, so it's fairly intuitive for us when we need to apply edits. It's really just making sure everyone who needs to review has visibility. Simran has started saving time on Fridays to go through any final open comments, which helps.

**Katya Luscomb:** We did have a question on the Leadership Development pillar page. There's a new tab—Heather's version—which looks like a fairly substantive rewrite with really good reframing. Since it's a pillar page, I wanted to check what big trends we should be looking for in that rewrite. We could potentially use it to train our model and improve overall performance.

**Justin Luebke:** Yeah, so Heather is a product person and a very good writer, but sometimes she writes things that aren't SEO optimized. You could take her content for style and tone and use that for the future, similar to how we handled case studies. But she's a strong writer, so I think there are some SEO needs we need to fit in as well.

**Katya Luscomb:** That makes sense. We've worked a lot on improving internal linking and optimizing headers with keywords. I just wanted to gut-check that there wasn't a major quality issue with the piece. It sounds like she had some stylistic ideas she wanted to run with. When it comes to open feedback, if there are specific comments we need to close out, can you flag those for Simran since we have two different versions? I saw you and Jay chatting about some things, and I want to make sure we don't leave anything open-ended.

**Justin Luebke:** At this point, I feel like it's Jay and I.

**Jay Perlman:** Yeah, that's what I was just about to say. Since Heather is such a thought leader in our business, we figured Justin and I should probably tackle it and just leave that one internally.

**Katya Luscomb:** Okay, cool. Then I'll make sure Simran knows to let this one lie. Great, wanted to make sure we were all coordinated.

**Katya Luscomb:** I know a couple weeks ago you flagged a bunch of quality concerns, and we've been working to address those. I wanted to get a quick pulse check based on the content that's come through. It looks like there are fewer edits in general, but still some repetition and clunky sentences.

**Justin Luebke:** Yeah. So Jay's been more on it than I have. Jen's been really busy, so she hasn't been in some of the latest ones either. But in general, we were hoping they could read more casual—less dense. And one of our main goals is to shift language to focus on business impact and outcomes. I think conclusions would be a really good spot to showcase that. Also, I noticed the anchor links are almost always the same. For example, "AI change management" is always linked as "change management" or "AI change management." We'd love some diversity there. And the last couple batches have had no external links.

**Katya Luscomb:** Oh, good flag. We'll definitely make sure those are in there.

**Jay Perlman:** The latest batch has had a few more, maybe not external links but at least case studies that were very helpful. But yeah, maybe there's still a slight lack of external links.

**Justin Luebke:** And they are a little repetitive. We want to make sure each blog is unique in intent and content.

**Jay Perlman:** Yeah, I noticed that particularly in the last five I was editing. Each piece seemed to have overlapping content. And in terms of clunkiness, I find each piece will have one to two, sometimes more, run-on sentences and really long, dense paragraphs. If we could break up long sentences and paragraphs more often, that would be helpful.

**Katya Luscomb:** It's a tough balancing act. Getting AI not to just give you all short, choppy sentences, but also not a massive block. When short, choppy sentences are the only thing in content, ideas feel really jumpy. You lose the connection between ideas. But you don't want a sentence that garbles the whole thing either.

**Jay Perlman:** Right, exactly. It's a tough balancing act, but if we can refine it a bit more, that would help.

**Katya Luscomb:** AI models can be finicky, but we'll work on echoing this feedback. Any other thoughts on all that?

**Justin Luebke:** I have a couple more things. One is feedback and one is a question I've been passively wondering about for a few weeks: how are the secondary keywords on the briefs being used? Are they in the content? Are they section headers?

**Katya Luscomb:** Right now, in the initial research and article intent, we put those secondary keywords in for consideration. We give the assignment a direction: title, primary keyword, and secondary keywords. It does research and creates an outline based on what it finds and that direction. We don't have specific instructions to use secondary keywords as explicit section titles. If that's something you want us to build in, we can. Right now, it's more about making sure those ideas are incorporated and there's density of secondary keywords in the content. But we can be more intentional if that's a goal.

**Justin Luebke:** I'm okay with that approach as long as the ideas are there and keywords are in there somehow. I don't think they need to be in the title—that would look too SEO-heavy. But as long as they're in there and actively being used, especially in the context of the idea and intent of the keywords, that's good.

**Katya Luscomb:** That would be good. I'll follow up on that as well. We've been implementing this for a while, but if the model has started to stray, I can definitely check on that.

**Justin Luebke:** Last thing. When we give WordPress access for publishing, something we do every time is create a content summary. We prompt ChatGPT for a 50-word summary, and we also search Google for the main term. If there's an AI Overview, we take part of the bolded overview and ask ChatGPT to include that in the content summary. That's what we do manually on the backend before publishing. We saw a video on it, tested it, and it seems to be working. The goal is essentially to grab the AIO content and put it into our content to see if it will rank or get the feature.

**Katya Luscomb:** Yeah, that makes sense. Especially with definitions, clear snippets, and things to pull—it makes sense to grab directly from the AIO. Before this job, I was actually editing and creating content that trained AI Overviews, so I'm very familiar with the nuance of what goes into them. Let me chat with my engineering team about feasibility. Creating the summary is definitely doable. For grabbing specifically from the AI Overview, I'll see if our pipeline can do it. If not, we can manually do that step and add it as an input to our pipeline.

**Justin Luebke:** Yeah, that would be good. And if you need examples, literally every blog we've published has them. They're accessible.

**Katya Luscomb:** Is it at the very top of the blog?

**Justin Luebke:** Yeah, right under the title.

**Katya Luscomb:** I saw the blog is officially live. I was poking around it today and working on getting tags and things to track events on the page. I looked at how you have the new one set up to understand the structure. I know the next step is phasing in cards for related content. Is there a plan for any sidebar materials or callouts to link across the site?

**Justin Luebke:** Not yet. Do you have ideas?

**Katya Luscomb:** Across a couple accounts, I've seen various things—like newsletter signups if there's something thematically relevant. I'd need to explore your site more specifically, but wanted to see if that was something you had in mind. It could be callouts to other courses or something.

**Justin Luebke:** We don't have a newsletter yet. That's future state. I'll noodle on the sidebar/callout options though. So for V2, we're currently working on homepage additions—tiles for resources and case studies. Then we'll move to article pages with cards, related blogs, and things like that.

**Katya Luscomb:** That makes sense. Keep us posted if there are any HTML codes or tags we need to incorporate.

**Justin Luebke:** Once that launches, we can work on getting that in the pipeline.

**Katya Luscomb:** That sounds good.

**Katya Luscomb:** Anything else top of mind before we meet again in a couple weeks?

**Justin Luebke:** I think that's all I have for now. Jay, is there anything else or is that comprehensive?

**Jay Perlman:** No, I think that was comprehensive. It covered everything I had questions about.

**Katya Luscomb:** Great. I know a lot of what we've covered is content refinement and edits. I'm definitely excited once we get GA4 access to start digging into analytics and optimizing. Right now it's a lot of our instinct. So I'm excited to see the signals. Also, we're building an in-house AI LLM tracking tool—similar to Scrunch or Profound—that we'll offer to GrowthX customers. It'll give deeper insights into citations and authority. Unlike Scrunch, it analyzes prompts from well-established industry leaders rather than requiring user-defined prompt lists. I'm excited to share more as we get closer to launch.

**Justin Luebke:** Nice.

**Katya Luscomb:** If anything comes up, I'll mention it with the next content batch, which should be end of today or first thing tomorrow. We'll get feedback by Thursday midday, and the batch will go to publishing. How did Monday's publish go?

**Justin Luebke:** Good. We hit some internal hiccups on the dev side, not ours, but it was good.

**Katya Luscomb:** Perfect. Keep us posted if there's any way we can support. I'll catch you guys in a couple weeks.

**Justin Luebke:** Sounds good.

**Katya Luscomb:** Talk soon.

**Justin Luebke:** Have a good one.

**Katya Luscomb:** Bye.

**Justin Luebke:** Bye.
