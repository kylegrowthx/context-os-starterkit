# DataAnnotation Internal Sync

<metadata>
date: 2025-12-02
time: 15:59 UTC
duration: 31 minutes
organizer: ismail@growthxlabs.com
participants: Jason Gong, Liz Kushnereit, Ismail Ajagbe, Sucheta Biswas, Ed Abazi
fathom_recording_id: 105582813
fathom_url: https://fathom.video/calls/491319544
share_url: https://fathom.video/share/Ho2A8uwMY_ag4bL3DyMF_9e7AAa5S8Lb
source: fathom
enriched_on: 2026-03-01 21:44 UTC
</metadata>

---

## Summary

GrowthX and Surge aligned on a content strategy overhaul to fix poor Atlas tool output. The team is rewriting ~80 existing articles to meet Surge's brand standards using a new pipeline (personas, brief, guidelines), with Sucheta scaling article rewrites via Claude Projects at ~5/day. Ed is generating abstract meta-image options for client presentation tomorrow, and the team is planning a quality escalation framework: Level 1 (deeply researched), Level 2 (first-hand expert experience), and Level 3 (video integration). Jason will send a proactive client update today highlighting the rewritten articles and new prioritization strategy.

---

## Context

GrowthX is working with Surge, a B2B data annotation company, on a content marketing engagement. The DataAnnotation project is focused on writing high-quality, SEO-driven blog content for Surge's platform. Prior to this sync, the team discovered that the "Atlas" content generation tool was producing output that failed to meet Surge's brand standards — primarily appearing too commodified and not aligned with Surge's positioning. This sync brought together the content, design, and delivery teams to reset strategy and execution.

---

## Relevance

- **To GrowthX Delivery:** The DataAnnotation engagement is shifting from automation-first to a hybrid human-AI approach. The team is overhauling the content pipeline (new personas, briefs, guidelines) and scaling human expert involvement (SME pilots for first-hand experience, video integration). This represents a significant methodology change requiring new processes, tools (Claude Projects, MidJourney), and quality gates (6-question brand-alignment checklist).
- **To GrowthX Business Development:** Client communication is critical — Jason is sending a proactive update highlighting team progress and new prioritization strategy. The account is showing strong signal: client is willing to invest in quality escalation (Level 2/3 content), has provided detailed feedback on brand alignment, and is prepared to review meta images and revised content. This suggests account health is good and potential for expansion exists if execution delivers.
- **To Content & SEO:** The team is implementing a multi-level content quality framework. Level 1 (current) is research-driven and well-structured; Level 2 aims to inject first-hand expert experience; Level 3 incorporates video. The prioritization strategy focuses on articles already ranking, which improves efficiency. New emphasis on detailed reasoning in content comments signals the client values strategic transparency.

---

## Overview

- **Content Overhaul:** Overhauling the content pipeline with new artifacts (personas, brief, guidelines) to fix poor outputs from the "Atlas" tool. The immediate goal is to rewrite all \~80 existing articles to meet Surge's brand standards.
- **Image Redesign:** Redesigning all meta images to be more artistic and align with Surge's brand. Ed will create stylistic options for two key articles ("Data Annotation Legit" & "Developer Burnout") to present to the client tomorrow.
- **Quality Escalation:** Planning to elevate content quality by adding first-hand, expert experience (Level 2) and eventually video (Level 3) to create unique, high-performing assets that cannot be easily replicated.
- **Client Communication:** Jason will send a proactive update to the client today, highlighting the four rewritten articles, the new prioritization strategy (focusing on articles that are already ranking), and the team's weekly progress goal.

---

## Key Topics

### Content Pipeline Overhaul

  - **Problem:** The "Atlas" tool is producing poor-quality content that fails to meet Surge's brand standards.
  - **Solution:** Overhauling the content pipeline with new artifacts to improve output quality.
      - **Completed:** Audience Personas, Company Brief
      - **In Progress:** Guiding Guidelines (EOD today)
  - **Process:** Test the new artifacts with the current pipeline to compare outputs. This will determine if engineering fixes are needed or if better inputs alone are sufficient.
  - **Sucheta's Role:**
      - **Interim Workflow:** Use a direct Claude project with prompts from Ismail to bypass the broken Atlas tool.
      - **Goal:** Rewrite as many of the \~80 existing articles as possible, targeting a pace of \~5 per day.
      - **Onboarding:** A call with Ismail and Martha tomorrow for hands-on training.

### Brand Alignment & Communication

  - **Core Principle:** All client-facing communication (Slack, comments) must align with Surge's brand, which opposes a "commodified BPO" image.
  - **Content Comments:** Provide more detailed, fleshed-out reasoning for all content choices (e.g., SEO risks) to demonstrate strategic thinking.
  - **Quality Gate:** Before delivery, all content must pass a 6-question brand-alignment checklist.

### Image Redesign

  - **Problem:** Current meta images are "low signal" and don't match Surge's artistic brand.
  - **Solution:** Create new, abstract meta images.
      - **Tool:** MidJourney (for its style references and potential API).
      - **Process:** Generate stylistic options for two articles ("Data Annotation Legit" & "Developer Burnout") to present to the client tomorrow.
  - **In-Article Diagrams:**
      - **Status:** Current diagrams are acceptable.
      - **Future:** Explore an operational workflow to generate diagrams at scale (e.g., ASCII diagrams → image generator).

### Content Quality Escalation

  - **Goal:** Elevate content quality beyond the current "Level 1" (deeply researched, well-written) to create unique, high-performing assets.
  - **Level 2: First-Hand Experience**
      - **Concept:** Inject genuine, first-hand experience (like Reddit or the Augment example) that cannot be easily replicated.
      - **Path 1 (Primary):** Recruit a subject matter expert (SME), even at a high cost (e.g., $1k), to test this model.
      - **Path 2:** Ismail to create a "wish list" of anecdotes the workflow can't generate, providing specific requirements for an SME.
  - **Level 3: Video Integration**
      - **Concept:** Incorporate video (e.g., product demos) into articles to further increase difficulty and value.

---

## Action Items

**Ismail Ajagbe (GrowthX)**
- Set up Claude project for Sucheta with prompts/resources; she rewrites ~5/day starting after tomorrow's training
- Add in-article image/diagram suggestions (ASCII format) to content workflow for MidJourney scaling
- Compile 4 remediated articles + priority list with ETA and send to Jason for client update today
- Create a "wish list" of anecdotal pieces needed for Level 2 (first-hand expert experience) content

**Liz Kushnereit (GrowthX)**
- Build sensitivity checker for client Slack comms and content comments against Surge's brand principles
- Send meta-image style/direction doc (artistic references, blend of diagrams/graphs) to Ed today
- Ask Andy (engineering) to identify the owner for image design problem; write spec for long-term solution
- Source and onboard a developer SME (~$1k budget) for first-hand experience pilot; test viability within 1-2 weeks

**Ed Abazi (GrowthX)**
- Generate 2-3 stylistic meta-image options for "Is data annotation legit" and "Why does developer burnout persist"; present to client tomorrow
- Explore operationalizing in-article diagram generation at scale (ASCII → image generator via MidJourney)

---

## Transcript

**Liz Kushnereit:** So I think everyone's had a chance to take a look at the notes. I guess we can just dive in on Ismail's updates, if you have any.

**Jason Gong:** I think Ismail's, like, really quiet on my side, I'm not sure.

**Ismail Ajagbe:** I updated Surge's internal weeklies. I dropped the updates right in there. Sorry for the delay. Okay, let me jump right in with my update.

**Ismail Ajagbe:** So yesterday, we completed the backlinks on lists and I shared that with Jesus. I think he's going to share the list with the client today. Then for the content, yesterday I dropped an update — we're going to start with overhauling the artifacts. For today, I'm done with the audience personas and the company brief. I'm expecting to be done with the guiding guidelines by EOD. Afterwards, we'll test the new artifacts with the current pipeline to compare output and see if we can scale the content. We'll also need to look into engineering, but I want to see the results from the artifact changes first. Based on those results, we'll know where engineering needs to come in and where better inputs alone can change the content quality.

**Liz Kushnereit:** Okay, so you're going to try putting all of these artifacts in and see where that gets you. That's kind of a version one. The personas looked good from a quick look. So I think today, Jason mentioned, we'll post the other four that you did. Is there any other amount that we want to try to get done this week, Jason, you think?

**Jason Gong:** I think our process now is just rewrite as many as we can. Just assume they've said these are good to go, because I'm not sure how to allocate effort otherwise. I don't want to wait for them. Everyone on the team, if we can get into a pace of just writing at the quality that Ismail has been publishing at, that would be ideal.

**Liz Kushnereit:** Honestly, the more the better. So how can Sucheta support you with that, Ismail, considering you're building out this process? What kind of opportunities are there for her to help?

**Ismail Ajagbe:** So what I'm going to do is set up a Claude project for her to come in. Atlas can't really give us the content we need right now. I'll set up a Claude project and share prompts with her so she can get started on content generation while we determine if we need engineering fixes. I'll also share resources on the internal channel so you get up to speed.

**Sucheta Biswas:** So basically we're using Claude right now and then building a workflow from scratch for this. Okay, all good. I'm taking everything from the top. Tomorrow Liz and Martha will join a call with Ismail where we'll get hands-on experience.

**Liz Kushnereit:** And you've had a chance to look at these already, right?

**Sucheta Biswas:** Yeah, started. I have questions so I'll ask them tomorrow.

**Liz Kushnereit:** Perfect. So just as many as we can work through. Hopefully the feedback won't push us in an entirely different direction, just small changes.

**Jason Gong:** Could we set a goal for how many you think you'll be able to do by the end of the week that Ismail reviews and thumbs up in terms of quality?

**Ismail Ajagbe:** After tomorrow I'll go back to content generation once I've confirmed the artifacts work and we've got engineering in to fix what's wrong with the pipelines.

**Jason Gong:** Is that a ticket? Would you be able to tag me on that?

**Liz Kushnereit:** We don't have enough content yet to make it a ticket because our specs aren't set. But Andy's aware it's coming, so we want him to prioritize once we're ready to cut the ticket. Everyone should take time to read through these today. Sucheta, if you can ramp on them and get to a daily goal, that would be great. Obviously the first day you can't do that many, but maybe five or so rewrites. We have 80 total, Ismail has done six, and there's about 10 more in the ready-to-publish queue. And just be aware all of these need to be updated in tandem. Always make sure there's no mention of video or image annotation.

**Liz Kushnereit:** So one more thing I wanted to mention — anytime you have Slack comms with the client, especially the data annotation team, build out some kind of sensitivity checker to check it against the Surge brand. Edwin's feedback was absolutely correct about how much we violated the brand's core principles. They stand against being this commodified BPO type, and they're paying someone who's doing exactly all the things he stands against. Ismail has grasped this and it's coming through in the content, but try to think through that in general. When leaving comments on the content for the client about the reasoning behind certain choices or SEO risks, give it more thought and flesh it out more. Put that through a sensitivity checker so you can be empowered to write more and give more insight into your thought process. Think from the service point of view, as if we worked for them. If you've had a chance to look through this, Sucheta, the most important thing is this block here — what we validate for presenting to Surge. All of these six questions need to answer yes for anything we deliver to them. That's the quality gate, based on their brand.

**Sucheta Biswas:** Just one question — I logged into our PodC system. Should I be updating that for Surge as well?

**Liz Kushnereit:** Yes. Okay, now let's talk about images.

**Liz Kushnereit:** After reflecting on this more, the reason I'm looping you in, Ed, is because I think our meta images are kind of low signal and not following Surge's brand. They have this more artistic thing on their website — they quote Hemingway on the landing page. I'm trying to think through how to fix those at scale. I started working on a doc but didn't get too far. I have some examples like the Fly.io blog — not exactly their aesthetic but this level of cool and interesting. We have 80 articles with meta titles, so images could be related to the content. Do you think that's realistic at scale?

**Ed Abazi:** I think OpenAI has some pretty cool ones too. So we're talking about abstract images? MidJourney would be the best tool because it has style references and an API. Doable at scale. We'd get an excerpt from the post for context on what objects to include in the image, but stylistically it'll be abstract. We just need to land on a style first, then we can generate them.

**Jason Gong:** I looked at what Morgan did for the previous ones. There were two patterns — icons and humans. We want to stay away from humans. Icons are okay, but I wonder if there's a way to make it feel a little bit more artistic like this.

**Jason Gong:** Can we just try with the six that Ismail did already and use those as test subjects? They'd like options, so if we can present how we thought through it and what we're deciding between. We have a call with them tomorrow. The two we shared with Edwin are "Data Annotation Legit" and "Why Does Developer Burnout Persist?" Can we narrow down to those two?

**Ed Abazi:** I don't know if we can have something extremely definitive today, but we can find a few stylistic options for you to present.

**Jason Gong:** Stylistic options would be awesome. We'll figure something out.

**Liz Kushnereit:** How much more direction do you need to move forward on this? I did a bunch of suggested content which I could send over or clean up and send.

**Ed Abazi:** Whatever you have, anything helps. But if we're going with diagrams, what kind of artistic style can you apply to diagrams? That's why I thought there was a difference between meta-images and images within articles.

**Liz Kushnereit:** Yes, exactly. Meta-images need to be high signal and much cooler. The diagrams in articles are not as important. The ones we have now are acceptable and solve the purpose. But meta-images could be improved.

**Ed Abazi:** Diagrams at scale is possible. The AI can return diagrams in ASCII format, and you can feed those to an image generator with a reference style. That's doable at scale.

**Liz Kushnereit:** Can we build that into the content refresh, like suggestions for diagrams, Ismail?

**Ismail Ajagbe:** Yeah, we can build it into the flow. It'll pass through the entire article and layout suggestions for in-article images.

**Ed Abazi:** One thing to note — fonts and typography are tricky in generation and won't always look perfect. We'll have to hope for the best there.

**Liz Kushnereit:** Okay, so I owe you that style doc today. I have some idea of what I want it to look like. But options are key, like Jason said. If we have six different stylistic options that are slightly different, that would be great.

**Jason Gong:** The article meta images are in explore mode now. The article diagrams look pretty good, and we have our own workflow for those. What are we doing for meta-images long-term? I know yesterday you mentioned asking engineering for a long-term solution, but short-term we might need to help out.

**Liz Kushnereit:** I don't even know who the engineering person is for the image design problem. But based on Ed's work, I can give them a better spec. At least from where we're prioritizing content pipeline and image redesign, if we can solve it quicker with Ed, I'd prefer that. But I can ask Andy about who to contact in engineering. At our current pace, we're doing five to ten a week, so maybe we can just ask Ed to create those graphics.

**Jason Gong:** I want to talk about content quality escalation. We want to keep showing a pattern of improving the content. The ones we shipped last week are really good. Level Zero is generic SEO content that everyone does — Edwin didn't like it. Level One is where we're at now — research deeply, write well, structure well. The stuff Ismail's been writing is pretty close to as good as Level One can get. But to have a step change, you layer in actual first-hand experience. I can share an example from Augment — they share who's writing and inject firsthand insights that no one else could replicate. That just outperforms from an SEO perspective and for readability. Level Three brings in video — product demos, genuine demos. The bar for difficulty keeps going up. We need to operationalize at scale something of higher quality. For Level Two on data annotation, we could try sourcing a developer SME at ~$1k to inject first-hand experience into articles. If we can show that to Edwin in a week or two, that will go a long way because they do the work and share that perspective, which you can't easily copy.

**Ismail Ajagbe:** Yeah, that makes sense. We're pretty close to that level of content already, and it's visible.

**Jason Gong:** There are multiple paths. The easiest is hiring an experienced developer to inject that experience. Reddit ranks so high because it's genuine first-hand experience. We need to recruit someone to do that.

**Liz Kushnereit:** And as you're going through content, if there's something you can't solve with the workflow, create a wish list of anecdotal pieces you'd need an SME for. That's one of the best ways we can support you if the workflow can't accomplish it.

**Sucheta Biswas:** One thing — the snippet that Jason showed had a very separate look. If we can do that, it really stands out and gives a visual break from blocks of text.

**Liz Kushnereit:** Yeah, we can work with their dev. Gene over at data annotation would be helpful with that. Thanks everyone. We'll keep communicating async. Ed, I owe you that document today.

**Jason Gong:** Actually, before we sign off, I want to send them a message today. We have those four articles. I'll review them first. I want to show them everything we've done and how we're thinking about working through previous articles to make them better.

**Liz Kushnereit:** Could you do that today or when Natalie's online? They want another filter showing what we're reviewing at the client view.

**Ismail Ajagbe:** The four remediated articles are in production. We have some in client review. I didn't want to mix that up.

**Jason Gong:** It doesn't have to be in the content OS, but I'm trying to show them: here are four articles we rewrote, here's our priority list based on articles already ranking well, we're working down that list, and here's how many we expect by end of week.

**Ismail Ajagbe:** Okay, I think I can get that done and send it to you quickly.
